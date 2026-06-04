import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "eval"))

from metrics import precision_at_k, recall_at_k


def test_precision_at_k():
    assert precision_at_k(["a", "b", "c"], {"a", "c"}, k=3) == 2 / 3


def test_recall_at_k():
    assert recall_at_k(["a", "b"], {"a", "c"}, k=2) == 0.5
