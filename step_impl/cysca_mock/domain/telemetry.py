from .state import load_state, save_state


def emit_event(event_name):
    """Record the latest telemetry event and append it to the audit trail."""
    state = load_state()
    state["telemetry"]["last_event"] = event_name
    state["telemetry"]["audit_sequence"].append(event_name)
    save_state(state)
    return state
