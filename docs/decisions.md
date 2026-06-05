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

## 2026-06-05 — EDA findings and preprocessing decisions

- **Log-transform continuous features.** All three continuous features are
  heavily right-skewed (e.g. distance_from_home median 9.97, max 10,632).
  Will apply log1p in Phase 2, fitted only on the training set.
- **Accuracy is the wrong metric.** A model predicting legitimate for every
  transaction would score 91.3%. Will use precision-recall AUC as the primary
  metric throughout.
- **repeat_retailer carries no signal.** Fraud rate is 0.09 regardless of
  whether the retailer is familiar. Will keep it in for now but flag it as
  a candidate for removal.
- **used_pin_number is the strongest protective feature.** Fraud rate drops
  to near zero when a PIN is used.
- **online_order is the strongest positive predictor.** 13% fraud rate vs 1%
  for in-person transactions.
- **ratio_to_median_purchase_price has the highest correlation with fraud**
  at 0.46. Distance from home and online order both sit at 0.19.
- **Features are largely independent.** Near-zero inter-feature correlations
  mean no multicollinearity to handle.
- **Data is highly separable.** The project will be framed around reasoning,
  calibration and threshold choice rather than headline accuracy.