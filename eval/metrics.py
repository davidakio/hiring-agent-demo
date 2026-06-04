"""Offline evaluation metrics for ranking quality."""


def precision_at_k(predictions: list, labels: set, k: int = 5) -> float:
    hits = sum(1 for p in predictions[:k] if p in labels)
    return hits / k


def recall_at_k(predictions: list, labels: set, k: int = 5) -> float:
    if not labels:
        return 0.0
    hits = sum(1 for p in predictions[:k] if p in labels)
    return hits / len(labels)
