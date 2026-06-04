def precision_at_k(predictions, labels, k=5):
    hits = sum(1 for p in predictions[:k] if p in labels)
    return hits / k
