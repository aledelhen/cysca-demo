from getgauge.python import step

from step_impl.cysca_mock.assertions.controller_assertions import (
    assert_config_active,
    assert_controller_healthy,
    assert_service_recovered,
    assert_startup_logs_clean,
    assert_state_preserved,
    assert_watchdog_triggered,
)
from step_impl.cysca_mock.assertions.device_assertions import assert_device_accepted
from step_impl.cysca_mock.assertions.telemetry_assertions import assert_audit_sequence, assert_event_emitted
from step_impl.cysca_mock.logs.system_logs import startup_log_lines
from step_impl.cysca_mock.workflows.controller_flows import (
    boot_controller,
    handshake_device,
    reload_runtime_config,
    trigger_operational_command,
)
from step_impl.cysca_mock.domain.controller import inject_failure, recover_controller


_runtime_state = {}


@step("Start the controller service")
def start_the_controller_service():
    global _runtime_state
    _runtime_state = boot_controller()


@step("Verify the service reports healthy")
def verify_the_service_reports_healthy():
    assert_controller_healthy(_runtime_state)


@step("Verify startup logs contain no errors")
def verify_startup_logs_contain_no_errors():
    assert_startup_logs_clean(startup_log_lines())


@step("Connect to the device bridge")
def connect_to_the_device_bridge():
    global _runtime_state
    _runtime_state = handshake_device()


@step("Send a handshake request")
def send_a_handshake_request():
    pass


@step("Verify the device responds with an accepted state")
def verify_the_device_responds_with_an_accepted_state():
    assert_device_accepted(_runtime_state)


@step("Update the runtime configuration")
def update_the_runtime_configuration():
    global _runtime_state
    _runtime_state = reload_runtime_config()


@step("Reload the controller")
def reload_the_controller():
    pass


@step("Verify the new configuration is active")
def verify_the_new_configuration_is_active():
    assert_config_active(_runtime_state, 2)


@step("Verify existing state is preserved")
def verify_existing_state_is_preserved():
    assert_state_preserved(_runtime_state, "reloaded")


@step("Inject a communication failure")
def inject_a_communication_failure():
    global _runtime_state
    _runtime_state = inject_failure()


@step("Verify the watchdog detects the failure")
def verify_the_watchdog_detects_the_failure():
    assert_watchdog_triggered(_runtime_state)


@step("Verify the service restarts successfully")
def verify_the_service_restarts_successfully():
    global _runtime_state
    _runtime_state = recover_controller()
    assert_service_recovered(_runtime_state)


@step("Trigger an operational command")
def trigger_an_operational_command():
    global _runtime_state
    _runtime_state = trigger_operational_command("command_issued")


@step("Verify the telemetry event is emitted")
def verify_the_telemetry_event_is_emitted():
    assert_event_emitted(_runtime_state, "command_issued")


@step("Verify the audit trail keeps the same sequence")
def verify_the_audit_trail_keeps_the_same_sequence():
    assert_audit_sequence(_runtime_state, "command_issued")
