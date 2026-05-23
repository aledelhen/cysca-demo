from .state import load_state, save_state


def connect_device():
    state = load_state()
    state["device"]["connection"] = "connected"
    state["device"]["handshake"] = "accepted"
    save_state(state)
    return state


def disconnect_device():
    state = load_state()
    state["device"]["connection"] = "disconnected"
    state["device"]["handshake"] = "pending"
    save_state(state)
    return state
