"""Runs the ranking evaluation over a labelled fixture and prints the metrics."""

from metrics import precision_at_k, recall_at_k

GOLD = {"c1", "c4", "c7"}
RANKING = ["c1", "c2", "c4", "c9", "c7"]


def main() -> None:
    print("precision@5:", precision_at_k(RANKING, GOLD))
    print("recall@5:", recall_at_k(RANKING, GOLD))


if __name__ == "__main__":
    main()
