from pathlib import Path

import yaml

_CONFIG_PATH = Path(__file__).resolve().parents[2] / "config" / "model_config.yaml"


def load_model_config() -> dict:
    """Loads the model + inference settings from config/model_config.yaml."""
    with open(_CONFIG_PATH, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)
