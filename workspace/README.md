# Workbench

Put incoming scans, PDFs, trial fonts, research plans, work ledgers, maintainer
notes and temporary review proofs in this folder.

For specimen work, start with `revival-ledger/ledger.json`. It records the
book → section → design → source impression → review → release hierarchy,
priorities, completed coverage, source gaps and the exact next action.
Run `.venv/bin/python workspace/revival-ledger/status.py` from the repository
root for the queue, optionally followed by a book ID. Read linked inventories
before extracting anything. `revival-ledger/refresh.py` updates the derived
book, family, icon and legacy-candidate indexes without replacing decisions.
`revival-ledger/source-witnesses.json` links each released family's cited
sources to known books and explicit archive leaves. Read the source citation
for spreads or other locations that could not be mapped automatically.
`designs.json` links stable icon IDs to `impressions.json`, which indexes
released inventory decisions, including repeats and matches to existing icons.
`revival-ledger/pages/` keeps separate type and icon survey states for each
available or mapped leaf. Run `revival-ledger/survey_pages.py` after refreshing
the book index to append newly acquired pages while preserving decisions.
The ledger and its evidence remain local and ignored; retain public provenance
and completed design decisions with each released family.

Everything here except this README is ignored by Git. Move the chosen historical
references into `collection/<id>/reference/` before submitting a revival. Keep
release provenance, method notes and proofs that explain design decisions with
their family; public `docs/` describes use and contribution workflows.
