from ..domain.controller import inject_failure, recover_controller, reload_controller, start_controller
from ..domain.device import connect_device, disconnect_device
from ..domain.telemetry import emit_event
from ..domain.state import reset_state, load_state


def boot_controller():
    """Reset persisted state and boot the controller."""
    reset_state()
    return start_controller()


def handshake_device():
    """Reset persisted state and connect the device."""
    reset_state()
    return connect_device()


def reload_runtime_config(version=2):
    """Reload the controller with a new config version."""
    state = reload_controller(version)
    return state


def simulate_failure_and_recovery():
    """Trigger a failure and immediately recover the controller."""
    inject_failure()
    return recover_controller()


def trigger_operational_command(event_name):
    """Emit a telemetry event representing an operational command."""
    state = emit_event(event_name)
    return state


def stop_device():
    """Disconnect the device."""
    return disconnect_device()
