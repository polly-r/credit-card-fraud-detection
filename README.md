# Card Fraud Detection

An end-to-end analysis of one million card transactions, framed around a single
question: not "can we predict fraud" (on this data, almost any model can), but
"what actually distinguishes a fraudulent transaction, and where would a real
fraud system set its threshold given that a missed fraud costs more than a false
alarm?"

## About the data

1,000,000 transactions, 8 columns, no missing values and no duplicates. The
target `fraud` is positive in 8.74% of rows (mild imbalance). Features:

| Column | Type | Meaning |
| --- | --- | --- |
| `distance_from_home` | continuous | distance from the cardholder's home |
| `distance_from_last_transaction` | continuous | distance since the previous transaction |
| `ratio_to_median_purchase_price` | continuous | purchase price over the median purchase price |
| `repeat_retailer` | binary | transaction at a previously used retailer |
| `used_chip` | binary | chip used |
| `used_pin_number` | binary | PIN used |
| `online_order` | binary | online order |
| `fraud` | binary | target |

The data is clean and the classes are highly separable, so headline accuracy is
not the point. See `docs/decisions.md` for how that shapes the approach.

## Project structure

```
card-fraud-detection/
├── data/raw/         # the CSV lives here, not committed (see data/README.md)
├── notebooks/        # the analysis narrative
├── src/              # reusable code the notebooks import
├── reports/          # exported figures and the final model card
└── docs/             # the decision log
```

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Get the data (see data/README.md) and place it at:
#    data/raw/card_transdata.csv

# 4. Sanity check
python -m src.data
```

## Progress

- [x] v0.1.0 — project scaffold, environment, data loader
- [ ] v0.2.0 — exploratory data analysis
- [ ] v0.3.0 — preprocessing pipeline
- [ ] v0.4.0 — baseline model and evaluation harness
- [ ] v0.5.0 — model comparison and tuning
- [ ] v0.6.0 — interpretation, calibration, threshold choice
- [ ] v1.0.0 — final report and model card
