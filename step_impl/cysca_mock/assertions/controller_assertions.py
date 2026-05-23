def assert_controller_healthy(state):
    assert state["controller"]["health"] == "healthy"


def assert_startup_logs_clean(log_lines):
    assert "ERROR" not in "\n".join(log_lines)


def assert_config_active(state, expected_version):
    assert state["controller"]["config_version"] == expected_version


def assert_state_preserved(state, expected_state):
    assert state["controller"]["state"] == expected_state


def assert_watchdog_triggered(state):
    assert state["controller"]["watchdog"] == "triggered"


def assert_service_recovered(state):
    assert state["controller"]["state"] == "running"
