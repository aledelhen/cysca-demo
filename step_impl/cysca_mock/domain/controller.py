from .state import load_state, save_state


def start_controller():
    """Initialize the controller as healthy and running."""
    state = load_state()
    state["controller"]["health"] = "healthy"
    state["controller"]["state"] = "running"
    save_state(state)
    return state


def reload_controller(config_version):
    """Update the stored controller configuration version."""
    state = load_state()
    state["controller"]["config_version"] = config_version
    state["controller"]["state"] = "reloaded"
    save_state(state)
    return state


def inject_failure():
    """Mark the controller as degraded and trigger the watchdog."""
    state = load_state()
    state["controller"]["health"] = "degraded"
    state["controller"]["state"] = "faulted"
    state["controller"]["watchdog"] = "triggered"
    save_state(state)
    return state


def recover_controller():
    """Restore the controller to a healthy running state."""
    state = load_state()
    state["controller"]["health"] = "healthy"
    state["controller"]["state"] = "running"
    state["controller"]["watchdog"] = "armed"
    save_state(state)
    return state
