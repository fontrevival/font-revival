# Baltimore Bold 1832: source and method

The master follows **Two Lines Pearl**, PDF page 71 of the supplied
unpaginated Baltimore specimen. The original JP2 is retained unchanged. Read
`../font.json` and `../reference/rights.json` for source and rights evidence.

The page is read after a 90-degree counterclockwise rotation. `rows.json`
records the inspected transcription in a 1000-pixel-wide preview;
`tracing.json` records exact native crops with that rotation. Each caption and
neighbouring sort is excluded. The outline fitting uses Potrace 1.16 with
the recorded thresholds, blur and speck limits. Capitals and figures use a
700-unit median height while preserving their observed relative widths and
individual ink heights. Baselines compensate for page tilt; the Q tail is
measured against nearby capitals and retained below the baseline.

All capitals and digits are observed impressions. Other symbols and punctuation
are new project companions reused from explicit MIT companion drawings already
in this repository. Lowercase aliases capitals; no historical lowercase is
claimed for this titling cut. Word spacing and bearings are new digital choices.

Prepare with Python 3.12, the repository requirements, and Potrace 1.16:

```sh
python scripts/trace_specimen.py baltimore-bold-1832 --output workspace/BaltimoreBold1832-Regular.otf
python scripts/fontrevival.py import baltimore-bold-1832 workspace/BaltimoreBold1832-Regular.otf
python scripts/fontrevival.py sizecheck baltimore-bold-1832
python scripts/fontrevival.py build baltimore-bold-1832
```

Normal builds use `font.ttx`; retracing is an intentional preparation step.
Inspect the full character inventory, source comparison, preview and gallery.

Optional selection review uses `requirements-display.txt` and the local `select.py` wrapper. It writes candidate crops to a working directory only; inspect them before changing the final tracing recipe. The committed native crops and explicit companion paths remain sufficient for preparation.
