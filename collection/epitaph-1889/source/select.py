"""Prepare disposable row selections; inspect before editing tracing.json."""
from pathlib import Path
import subprocess
import sys

family = Path(__file__).resolve().parents[1]
root = family.parents[1]
if len(sys.argv) != 2:
    raise SystemExit("Usage: python source/select.py workspace/review-directory")
subprocess.run([sys.executable, str(root / "scripts/select_display_rows.py"),
                str(family), "--output", sys.argv[1]], check=True)
