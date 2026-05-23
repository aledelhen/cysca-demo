from .state import load_state, save_state


def connect_device():
    """Mark the device as connected with an accepted handshake."""
    state = load_state()
    state["device"]["connection"] = "connected"
    state["device"]["handshake"] = "accepted"
    save_state(state)
    return state


def disconnect_device():
    """Return the device to a disconnected pending-handshake state."""
    state = load_state()
    state["device"]["connection"] = "disconnected"
    state["device"]["handshake"] = "pending"
    save_state(state)
    return state
