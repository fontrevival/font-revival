#!/usr/bin/env python3
"""Assemble the public gallery; keep large downloads on the repository host.

The editable masters, native scans and full proofs remain in the repository.
Local galleries retain relative paths. Staged downloads and comparison previews
link to the same committed files on GitHub, avoiding duplicate large assets
in GitHub Pages' 1 GB published-site allowance.
"""
import argparse
import base64
import gzip
import hashlib
from html.parser import HTMLParser
import html
import os
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import quote, unquote, urlsplit

REPO = Path(__file__).resolve().parents[1]
SITE_BASE = 'https://haroldus-.github.io/font-revival/'
DOWNLOAD_BASE = 'https://raw.githubusercontent.com/haroldus-/font-revival/main/'
CSS_URL = re.compile(r'url\(\s*[\'"]?([^\s\)\'"]+)[\'"]?\s*\)')
DETAIL_SVG = re.compile(r'(<svg\b[^>]*\bdata-icon-format="(multitone|monochrome)"[^>]*>)(.*?)(</svg>)', re.S)
PACKING_VERSION = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def pack_detail_artwork(content, helper_url, minimum=100_000):
    """Losslessly pack large preview paths in the published HTML only.

    The ordinary SVG download is also a visible fallback. The browser restores
    the exact inline paths so the existing size and colour controls still work.
    Local repository pages and downloadable artwork stay plain SVG.
    """
    packed = False

    def replace(match):
        nonlocal packed
        opening, kind, artwork, closing = match.groups()
        if len(artwork.encode()) < minimum:
            return match.group()
        prefix = 'multitone/' if kind == 'multitone' else ''
        download = re.search(r'<a download href="([^"]+/svg/' + prefix + r'[^/"<>]+\.svg)">', content)
        viewbox = re.search(r'viewBox="([^"]+)"', opening)
        if not download or not viewbox:
            return match.group()
        x, y, width, height = viewbox.group(1).split()
        payload = base64.b64encode(gzip.compress(artwork.encode(), compresslevel=6, mtime=0)).decode('ascii')
        if len(payload) >= len(artwork):
            return match.group()
        packed = True
        fallback = (f'<image data-fallback-href="{download.group(1)}" x="{x}" y="{y}" '
                    f'width="{width}" height="{height}"/>')
        return opening + fallback + '<script type="application/octet-stream" data-packed-svg>' + payload + '</script>' + closing

    content = DETAIL_SVG.sub(replace, content)
    if packed:
        script = f'<script defer src="{html.escape(helper_url, quote=True)}"></script>\n'
        content = content.replace('</body>', script + '</body>')
    return content


def cached_artwork(content, helper_url, cache=None):
    """Reuse losslessly packed pages; invalidate on input or assembler changes."""
    if cache is None or len(content) < 100_000:
        return pack_detail_artwork(content, helper_url)
    key = hashlib.sha256('\0'.join((PACKING_VERSION, helper_url, content)).encode()).hexdigest()
    cached = cache / (key + '.html')
    if cached.is_file():
        return cached.read_text()
    packed = pack_detail_artwork(content, helper_url)
    cache.mkdir(parents=True, exist_ok=True)
    temporary = cached.with_suffix('.tmp')
    temporary.write_text(packed)
    temporary.replace(cached)
    return packed


def committed_files(root):
    """Read path metadata without fetching archival blobs in a partial clone."""
    listing = subprocess.check_output(['git', 'ls-tree', '-rz', '--name-only', 'HEAD'], cwd=root)
    return {Path(os.fsdecode(name)) for name in listing.split(b'\0') if name}


def materialize(root, files, tracked):
    """Fetch missing inline dependencies together, leaving downloads on GitHub."""
    missing = []
    for file in sorted(files):
        if file.is_file():
            continue
        relative = file.relative_to(root)
        if relative not in tracked:
            raise ValueError(f'Missing gallery asset: {relative}')
        # Non-cone sparse patterns are rooted and literal, even for names with
        # glob characters or spaces. Updating the sparse checkout uses Git's
        # bulk blob prefetch; restoring individual paths can fetch serially.
        pattern = relative.as_posix()
        for char in ('\\', '*', '?', '[', ' '):
            pattern = pattern.replace(char, '\\' + char)
        missing.append('/' + pattern)
    if missing:
        subprocess.run(['git', 'sparse-checkout', 'add', '--stdin'],
                       cwd=root, input=('\n'.join(missing) + '\n').encode(), check=True)


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = set()
        self.downloads = set()
        self.comparison_images = set()
        self.inline_assets = set()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == 'meta' and (attributes.get('property') in ('og:image', 'og:image:secure_url')
                              or attributes.get('name') == 'twitter:image'):
            if attributes.get('content'):
                self.urls.add(attributes['content'])
                self.inline_assets.add(attributes['content'])
        if tag == 'a' and 'download' in attributes and attributes.get('href'):
            self.downloads.add(attributes['href'])
        comparison = tag == 'img' and 'comparison' in attributes.get('class', '').split()
        if comparison and attributes.get('src'):
            self.comparison_images.add(attributes['src'])
        for key, value in attrs:
            if key in ('src', 'href', 'data-art-chunk') and value:
                self.urls.add(value)
                if key in ('src', 'data-art-chunk') and not comparison:
                    self.inline_assets.add(value)


def local_path(root, origin, url, tracked=None):
    # Social previews need absolute public URLs, but remain local dependencies.
    if url.startswith(SITE_BASE):
        url = '/' + url[len(SITE_BASE):]
    parts = urlsplit(url)
    if parts.scheme or parts.netloc or not parts.path:
        return None
    target = ((root if parts.path.startswith('/') else origin.parent) /
              unquote(parts.path).lstrip('/')).resolve()
    target.relative_to(root.resolve())
    if not target.is_file() and (tracked is None or target.relative_to(root) not in tracked):
        raise ValueError(f'Missing gallery asset: {target.relative_to(root)}')
    return target


def assemble(root, output, download_base=DOWNLOAD_BASE, cache=None, git_source=False):
    root, output = root.resolve(), output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    pending = [root / name for name in ('index.html', 'icons.html', 'catalog.json', 'icons.json', 'LICENSE')]
    # The private checkout is built before assembly. Include its complete,
    # explicit browser distribution: OAuth, privacy and agent routes are reached from
    # JavaScript and therefore are not discoverable by the HTML reference scan.
    # Never recursively copy the private source checkout or source maps.
    if (root / 'editor/index.html').is_file():
        for name in ('index.html', 'app.js', 'app.css', 'oauth.html', 'privacy.html',
                     'agents.html', 'document-schema.json', 'agent-tools.json',
                     'LICENSE.txt', 'THIRD-PARTY.txt'):
            file = root / 'editor' / name
            if not file.is_file():
                raise ValueError(f'Missing editor distribution file: {name}')
            pending.append(file)
    tracked = committed_files(root) if git_source else None
    written = set()
    while pending:
        batch = sorted({file for file in pending if file.relative_to(root) not in written
                        and file.suffix.lower() not in ('.pdf', '.zip')})
        pending = []
        if git_source:
            materialize(root, batch, tracked)
        for file in batch:
            relative = file.relative_to(root)
            stage_file(root, output, file, pending, download_base, cache, tracked)
            written.add(relative)
    total = sum((output / name).stat().st_size for name in written)
    if total > 1_000_000_000:
        raise ValueError(f'Published site exceeds 1 GB: {total:,} bytes')
    return total, len(written)


def stage_file(root, output, file, pending, download_base, cache, tracked):
    relative = file.relative_to(root)
    destination = output / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    if file.suffix in ('.html', '.css'):
        content = file.read_text()
        if file.suffix == '.html' and '</body>' in content:
            helper = os.path.relpath(root / 'site/unpack-art.js', file.parent)
            content = cached_artwork(content, Path(helper).as_posix(), cache)
        references = set(CSS_URL.findall(content))
        downloads, comparisons, inline = set(), set(), set(references)
        if file.suffix == '.html':
            parser = References(); parser.feed(content)
            references.update(parser.urls)
            downloads, comparisons = parser.downloads, parser.comparison_images
            inline.update(parser.inline_assets)
        for url in sorted(references):
            target = local_path(root, file, url, tracked)
            if target is None:
                continue
            remote_asset = target.suffix.lower() in ('.pdf', '.zip') or url in downloads or url in comparisons
            if remote_asset:
                remote = download_base + quote(target.relative_to(root).as_posix())
                fragment = urlsplit(url).fragment
                if fragment:
                    remote += '#' + fragment
                if url in comparisons:
                    content = content.replace('src="' + url + '"', 'src="' + remote + '"')
                if url in downloads or target.suffix.lower() in ('.pdf', '.zip'):
                    content = content.replace('href="' + url + '"', 'href="' + remote + '"')
            if not remote_asset or url in inline:
                pending.append(target)
        destination.write_text(content)
    else:
        shutil.copyfile(file, destination)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=REPO / '_site')
    parser.add_argument('--cache', type=Path, help='Cache packed artwork between builds')
    parser.add_argument('--git-source', action='store_true',
                        help='Fetch missing inline assets from HEAD in a sparse checkout')
    args = parser.parse_args()
    total, count = assemble(REPO, args.output, cache=args.cache, git_source=args.git_source)
    print(f'Staged {count:,} files, {total / 1_000_000:.1f} MB, in {args.output}')
