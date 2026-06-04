"""Fine-tuning pipeline for the candidate-ranking model. Prepares the dataset,
launches a fine-tune job, and returns the resulting model id."""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"


def build_dataset() -> list[dict]:
    # A real pipeline reads labelled hiring outcomes here; stubbed for the demo.
    return [{"prompt": "<cv>", "completion": "<decision>"}]


def run_finetune(base_model: str = "gpt-4o-mini") -> str:
    dataset = build_dataset()
    print(f"fine-tuning {base_model} on {len(dataset)} examples")
    return f"ft:{base_model}:hiring-agent"


if __name__ == "__main__":
    print(run_finetune())
