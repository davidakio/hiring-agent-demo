import sys
from pathlib import Path

# Make the (non-package) eval/ scripts importable in tests.
sys.path.insert(0, str(Path(__file__).resolve().parent / "eval"))
