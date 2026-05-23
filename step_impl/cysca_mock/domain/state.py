import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "control_state.json"


def load_state():
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def save_state(state):
    DATA_FILE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def reset_state():
    state = load_state()
    save_state(state)
    return state
