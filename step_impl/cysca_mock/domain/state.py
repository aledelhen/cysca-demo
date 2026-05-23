import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "control_state.json"
DEFAULT_STATE = {
    "controller": {
        "config_version": 1,
        "health": "starting",
        "state": "booting",
        "watchdog": "armed",
    },
    "device": {
        "connection": "disconnected",
        "handshake": "pending",
        "mode": "standby",
    },
    "telemetry": {
        "audit_sequence": [],
        "last_event": None,
    },
}


def load_state():
    """Load the persisted control state, seeding defaults if needed."""
    raw_state = DATA_FILE.read_text(encoding="utf-8").strip()
    if not raw_state:
        save_state(DEFAULT_STATE)
        return json.loads(json.dumps(DEFAULT_STATE))
    return json.loads(raw_state)


def save_state(state):
    """Write the given control state to disk."""
    DATA_FILE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def reset_state():
    """Reset the persisted control state back to defaults."""
    save_state(DEFAULT_STATE)
    return json.loads(json.dumps(DEFAULT_STATE))
