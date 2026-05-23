import logging

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
from step_impl.cysca_mock.domain.controller import inject_failure, recover_controller
from step_impl.cysca_mock.helpers.table_utils import table_to_key_values
from step_impl.cysca_mock.logs.system_logs import startup_log_lines
from step_impl.cysca_mock.workflows.controller_flows import (
    boot_controller,
    handshake_device,
    reload_runtime_config,
    trigger_operational_command,
)


_runtime_state = {}
_profile = {}


logger = logging.getLogger("cysca_mock")
if not logger.handlers:
    logging.basicConfig(level=logging.INFO, format="%(message)s")


def _log(message):
    logger.info(message)


@step("Start the controller service <boot_mode> <table>")
def start_the_controller_service(boot_mode, table):
    global _runtime_state
    global _profile
    _log(f"🚀 Starting controller service in {boot_mode} mode")
    _profile = table_to_key_values(table)
    _profile["boot_mode"] = boot_mode
    _runtime_state = boot_controller()
    _log("✅ Controller service started")


@step("Verify the service reports healthy <health>")
def verify_the_service_reports_healthy(health):
    _log(f"🩺 Verifying controller health is {health}")
    assert _runtime_state["controller"]["health"] == health
    assert_controller_healthy(_runtime_state)
    _log("✅ Controller health verified")


@step("Verify startup logs contain no errors <log_state>")
def verify_startup_logs_contain_no_errors(log_state):
    _log(f"🧾 Checking startup logs are {log_state}")
    assert log_state == "clean"
    assert_startup_logs_clean(startup_log_lines())
    _log("✅ Startup logs are clean")


@step("Connect to the device bridge <device_id> <table>")
def connect_to_the_device_bridge(device_id, table):
    global _runtime_state
    global _profile
    _log(f"🔗 Connecting to device bridge for {device_id}")
    _profile = table_to_key_values(table)
    _profile["device_id"] = device_id
    _runtime_state = handshake_device()
    _log("✅ Device bridge connected")


@step("Send a handshake request <mode>")
def send_a_handshake_request(mode):
    _log(f"📨 Sending {mode} handshake request")
    assert mode == "trusted"
    _log("✅ Handshake request sent")


@step("Verify the device responds with an accepted state <state>")
def verify_the_device_responds_with_an_accepted_state(state):
    _log(f"📡 Verifying device state is {state}")
    assert state == "accepted"
    assert_device_accepted(_runtime_state)
    _log("✅ Device accepted state verified")


@step("Update the runtime configuration <config_version> <table>")
def update_the_runtime_configuration(config_version, table):
    global _runtime_state
    global _profile
    _log(f"⚙️ Updating runtime configuration to version {config_version}")
    _profile = table_to_key_values(table)
    _profile["config_version"] = config_version
    _runtime_state = reload_runtime_config(int(config_version))
    _log("✅ Runtime configuration updated")


@step("Reload the controller <action>")
def reload_the_controller(action):
    _log(f"🔄 Reloading controller via {action}")
    assert action == "restart"
    _log("✅ Controller reload acknowledged")


@step("Verify the new configuration is active <config_version>")
def verify_the_new_configuration_is_active(config_version):
    _log(f"📋 Verifying configuration version {config_version} is active")
    assert_config_active(_runtime_state, int(config_version))
    _log("✅ New configuration is active")


@step("Verify existing state is preserved <state>")
def verify_existing_state_is_preserved(state):
    _log(f"🧩 Verifying controller state is preserved as {state}")
    assert_state_preserved(_runtime_state, state)
    _log("✅ Existing state preserved")


@step("Inject a communication failure <failure_type> <table>")
def inject_a_communication_failure(failure_type, table):
    global _runtime_state
    global _profile
    _log(f"⚠️ Injecting communication failure: {failure_type}")
    _profile = table_to_key_values(table)
    _profile["failure_type"] = failure_type
    _runtime_state = inject_failure()
    _log("✅ Failure injected")


@step("Verify the watchdog detects the failure <status>")
def verify_the_watchdog_detects_the_failure(status):
    _log(f"🐕 Verifying watchdog status is {status}")
    assert status == "triggered"
    assert_watchdog_triggered(_runtime_state)
    _log("✅ Watchdog detected the failure")


@step("Verify the service restarts successfully <state>")
def verify_the_service_restarts_successfully(state):
    global _runtime_state
    _log(f"♻️ Recovering service to {state}")
    _runtime_state = recover_controller()
    assert state == "running"
    assert_service_recovered(_runtime_state)
    _log("✅ Service recovered successfully")


@step("Trigger an operational command <event_name> <table>")
def trigger_an_operational_command(event_name, table):
    global _runtime_state
    global _profile
    _log(f"📣 Triggering operational command {event_name}")
    _profile = table_to_key_values(table)
    _profile["event_name"] = event_name
    _runtime_state = trigger_operational_command(event_name)
    _log("✅ Operational command triggered")


@step("Trigger an operational command <event_name> from <source>")
def trigger_an_operational_command_from(event_name, source):
    global _runtime_state
    global _profile
    _log(f"📣 Triggering operational command {event_name} from {source}")
    _profile = {"event_name": event_name, "source": source}
    _runtime_state = trigger_operational_command(event_name)
    _log("✅ Operational command triggered")


@step("Verify the telemetry event is emitted as command_issued <event_name>")
def verify_the_telemetry_event_is_emitted_as_command_issued(event_name):
    _log(f"📈 Verifying telemetry event {event_name} was emitted")
    assert_event_emitted(_runtime_state, event_name)
    _log("✅ Telemetry event emitted")


@step("Verify the audit trail keeps the same sequence for command_issued <event_name>")
def verify_the_audit_trail_keeps_the_same_sequence_for_command_issued(event_name):
    _log(f"🧾 Verifying audit trail sequence for {event_name}")
    assert_audit_sequence(_runtime_state, event_name)
    _log("✅ Audit trail sequence verified")


@step("Verify the telemetry event <event_name> was emitted")
def verify_the_telemetry_event_was_emitted(event_name):
    _log(f"📈 Verifying telemetry event {event_name} was emitted")
    assert_event_emitted(_runtime_state, event_name)
    _log("✅ Telemetry event emitted")


@step("Verify the telemetry source <source> was recorded")
def verify_the_telemetry_source_was_recorded(source):
    _log(f"🧭 Verifying telemetry source {source} was recorded")
    assert _profile["source"] == source
    _log("✅ Telemetry source recorded")
