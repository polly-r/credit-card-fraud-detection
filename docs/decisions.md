# Decision log

Short, dated notes on choices made and why. The point is that "why did you do
it that way?" always has an answer here, including the dead ends.

## 2026-06-05 — Project setup

- **Dataset.** Card transactions (1M rows, 8 columns). Chosen for scale and a
  tight feature set that rewards understanding over feature padding. Caveat
  recorded up front: the data is clean and highly separable, so the project is
  framed around reasoning, calibration and threshold choice rather than headline
  accuracy.
- **Environment.** Plain `venv` plus `pip` with a `requirements.txt`, kept
  simple for a first project. Versions can be frozen later for an exact lock.
- **Data not committed.** `data/raw/` is gitignored. The 73MB file would bloat
  the repo and the acquisition steps belong in `data/README.md` instead.
- **Notebook hygiene.** `nbstripout` strips notebook outputs on commit so the
  repo stays small and diffs stay readable.
- **Line endings.** The raw CSV uses carriage-return (`\r`) endings. pandas
  reads it fine; shell tools (`head`, `wc`, `grep`) do not. Noted so it is not
  rediscovered as a bug later.
- **Split.** Stratified train/test split on `fraud`, fixed seed 42, to hold the
  8.74% fraud rate constant across sets and keep results reproducible.
