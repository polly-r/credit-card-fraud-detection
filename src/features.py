"""Feature engineering and preprocessing pipeline."""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, StandardScaler
from sklearn.compose import ColumnTransformer

from src.data import CONTINUOUS_FEATURES, BINARY_FEATURES


def build_pipeline() -> ColumnTransformer:
    """Build the preprocessing pipeline.

    Continuous features: log1p transform, then standard scaling.
    Binary features: passed through unchanged.

    The pipeline must be fitted on training data only.

    Returns
    -------
    An unfitted ColumnTransformer.
    """
    continuous_pipeline = Pipeline([
        ('log1p', FunctionTransformer(np.log1p, validate=True)),
        ('scaler', StandardScaler()),
    ])

    return ColumnTransformer([
        ('continuous', continuous_pipeline, CONTINUOUS_FEATURES),
        ('binary', 'passthrough', BINARY_FEATURES),
    ])