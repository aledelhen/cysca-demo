from .state import load_state, save_state


def emit_event(event_name):
    state = load_state()
    state["telemetry"]["last_event"] = event_name
    state["telemetry"]["audit_sequence"].append(event_name)
    save_state(state)
    return state
