# Obtaining the data

The dataset is not stored in this repository. Download it and place the file at:

```
data/raw/card_transdata.csv
```

## Source

Kaggle: "Credit Card Fraud" by Dhanush Narayanan R
<https://www.kaggle.com/datasets/dhanushnarayananr/credit-card-fraud>


## Option A — download from the website

Sign in to Kaggle, open the dataset page, click **Download**, unzip, and move
`card_transdata.csv` into `data/raw/`.

## Option B — Kaggle CLI

```bash
pip install kaggle
# Place your kaggle.json API token as described in the Kaggle docs, then:
kaggle datasets download -d dhanushnarayananr/credit-card-fraud -p data/raw --unzip
```

## Check it loaded

From the project root, with the environment active:

```bash
python -m src.data
```

You should see 1,000,000 rows and a fraud rate of 0.0874.
