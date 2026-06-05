"""Data loading and splitting for the card fraud project.

Note on the raw file: card_transdata.csv uses carriage-return (\\r) line
endings. pandas reads this correctly, so no special handling is needed here;
the quirk only affects shell tools such as head, wc and grep.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

# Paths are resolved relative to this file, so the code runs from anywhere.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "card_transdata.csv"

TARGET = "fraud"
BINARY_FEATURES = ["repeat_retailer", "used_chip", "used_pin_number", "online_order"]
CONTINUOUS_FEATURES = [
    "distance_from_home",
    "distance_from_last_transaction",
    "ratio_to_median_purchase_price",
]
FEATURES = CONTINUOUS_FEATURES + BINARY_FEATURES


def load_data(path: Path | str = RAW_DATA_PATH) -> pd.DataFrame:
    """Load the raw transactions CSV.

    Parameters
    ----------
    path:
        Location of the CSV. Defaults to data/raw/card_transdata.csv.

    Returns
    -------
    A DataFrame with 1,000,000 rows and 8 columns.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"Could not find the data at {path}. "
            "See data/README.md for how to obtain it."
        )
    df = pd.read_csv(path)
    # The four flags and the target load as float; cast them to a small int.
    for col in BINARY_FEATURES + [TARGET]:
        df[col] = df[col].astype("int8")
    return df


def split_data(
    df: pd.DataFrame,
    test_size: float = 0.2,
    random_state: int = 42,
):
    """Split into train and test sets, stratified on the fraud label.

    Stratifying keeps the fraud rate (around 8.74%) almost identical in both
    sets, which matters when the classes are imbalanced.

    Returns
    -------
    X_train, X_test, y_train, y_test
    """
    X = df[FEATURES]
    y = df[TARGET]
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )


if __name__ == "__main__":
    # Sanity check. Run from the project root with: python -m src.data
    data = load_data()
    print(f"Loaded {len(data):,} rows, {data.shape[1]} columns")
    print(f"Fraud rate: {data[TARGET].mean():.4f}")
    X_train, X_test, y_train, y_test = split_data(data)
    print(f"Train: {len(X_train):,} rows   Test: {len(X_test):,} rows")
    print(
        f"Train fraud rate: {y_train.mean():.4f}   "
        f"Test fraud rate: {y_test.mean():.4f}"
    )
