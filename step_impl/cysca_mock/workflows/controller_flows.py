from ..domain.controller import inject_failure, recover_controller, reload_controller, start_controller
from ..domain.device import connect_device, disconnect_device
from ..domain.telemetry import emit_event
from ..domain.state import reset_state, load_state


def boot_controller():
    reset_state()
    return start_controller()


def handshake_device():
    reset_state()
    return connect_device()


def reload_runtime_config(version=2):
    state = reload_controller(version)
    return state


def simulate_failure_and_recovery():
    inject_failure()
    return recover_controller()


def trigger_operational_command(event_name):
    state = emit_event(event_name)
    return state


def stop_device():
    return disconnect_device()
