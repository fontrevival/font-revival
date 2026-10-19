#!/usr/bin/env python3
"""Plan collection verification against the last successful CI commit."""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def select_checks(changed, available, full=False):
    changed, available = set(changed), set(available)
    full = full or any(
        path in ('LICENSE', 'requirements.txt', '.github/workflows/check.yml')
        or path.startswith('scripts/') and path != 'scripts/build_site.py'
        for path in changed)
    touched = {path.split('/')[1] for path in changed
               if path.startswith('collection/') and len(path.split('/')) > 2}
    selected = available if full else touched & available
    gallery = full or bool(touched - available) or any(
        path in ('catalog.json', 'icons.json', 'index.html', 'icons.html')
        or path.startswith(('site/', 'icons/')) and path != 'site/editor-release.json'
        or path.startswith('collection/') and (
            path.split('/', 2)[-1] in ('font.json', 'icons.json')
            or len(path.split('/')) > 3 and path.split('/')[2] in ('fonts', 'web', 'svg', 'downloads'))
        for path in changed)
    tests = full or bool(touched) or gallery or any(
        path.startswith(('tests/', 'scripts/')) for path in changed)
    return {'full': full, 'families': sorted(selected), 'gallery': gallery, 'tests': tests}


def plan(root, base='', full=False):
    available = [path.parent.name for path in (root / 'collection').glob('*/font.json')]
    changed = []
    # A missing or unavailable successful baseline requires a complete audit.
    if not re.fullmatch(r'[0-9a-f]{40,64}', base):
        full = True
    else:
        try:
            changed = subprocess.check_output(
                ['git', 'diff', '--no-renames', '--name-only', '-z', base, 'HEAD'], cwd=root
            ).decode().rstrip('\0').split('\0')
        except subprocess.CalledProcessError:
            full = True
    result = select_checks(changed, available, full)
    result['commit'] = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
    result['base'] = base
    return result


def run_checks(selection):
    import fontrevival
    if selection['families']:
        # package() verifies the selected families once before writing archives.
        fontrevival.package(selection['families'], check_catalog=selection['gallery'])
    elif selection['gallery']:
        fontrevival.check([], check_catalog=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    create = commands.add_parser('plan')
    create.add_argument('--base', default='')
    create.add_argument('--full', action='store_true')
    create.add_argument('--output', type=Path, required=True)
    run = commands.add_parser('run')
    run.add_argument('plan', type=Path)
    args = parser.parse_args()
    if args.command == 'plan':
        selection = plan(ROOT, args.base, args.full or os.environ.get('GITHUB_EVENT_NAME') == 'workflow_dispatch')
        args.output.write_text(json.dumps(selection, indent=2) + '\n')
        print(json.dumps(selection, indent=2))
        if os.environ.get('GITHUB_OUTPUT'):
            with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
                for key, value in {'tests': selection['tests'],
                                   'validate': bool(selection['families']) or selection['gallery'],
                                   'packages': bool(selection['families'])}.items():
                    print(f'{key}={str(value).lower()}', file=output)
    else:
        selection = json.loads(args.plan.read_text())
        head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
        if selection['commit'] != head:
            raise ValueError('The validation plan belongs to a different commit.')
        run_checks(selection)


if __name__ == '__main__':
    main()
