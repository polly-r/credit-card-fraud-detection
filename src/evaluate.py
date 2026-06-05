"""Shared evaluation harness for all models."""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import (
    average_precision_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    PrecisionRecallDisplay,
    RocCurveDisplay,
    roc_auc_score,
)


def evaluate_model(
    model,
    X_test,
    y_test,
    model_name: str = "Model",
    threshold: float = 0.5,
    save_path: str | None = None,
):
    """Evaluate a fitted model and produce a standard set of metrics and plots.

    Parameters
    ----------
    model:
        A fitted sklearn-compatible model with a predict_proba method.
    X_test:
        Test features.
    y_test:
        True labels.
    model_name:
        Label used in plot titles and printed output.
    threshold:
        Probability threshold for converting scores to class predictions.
    save_path:
        If provided, saves the figure to this path.
    """
    y_prob = model.predict_proba(X_test)[:, 1]
    y_pred = (y_prob >= threshold).astype(int)

    pr_auc = average_precision_score(y_test, y_prob)
    roc_auc = roc_auc_score(y_test, y_prob)

    print(f"\n{'='*60}")
    print(f"  {model_name}")
    print(f"{'='*60}")
    print(f"  PR-AUC:  {pr_auc:.4f}")
    print(f"  ROC-AUC: {roc_auc:.4f}")
    print(f"  Threshold: {threshold}")
    print(f"\n{classification_report(y_test, y_pred, target_names=['Legitimate', 'Fraud'])}")

    fig, axes = plt.subplots(1, 3, figsize=(16, 4))

    PrecisionRecallDisplay.from_predictions(
        y_test, y_prob, ax=axes[0], name=model_name
    )
    axes[0].set_title(f"Precision-Recall Curve\nPR-AUC = {pr_auc:.4f}")

    RocCurveDisplay.from_predictions(
        y_test, y_prob, ax=axes[1], name=model_name
    )
    axes[1].set_title(f"ROC Curve\nROC-AUC = {roc_auc:.4f}")

    cm = confusion_matrix(y_test, y_pred)
    ConfusionMatrixDisplay(cm, display_labels=["Legitimate", "Fraud"]).plot(
        ax=axes[2], colorbar=False
    )
    axes[2].set_title(f"Confusion Matrix\nThreshold = {threshold}")

    plt.suptitle(model_name, fontsize=13)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches="tight")

    plt.show()

    return {"model_name": model_name, "pr_auc": pr_auc, "roc_auc": roc_auc}