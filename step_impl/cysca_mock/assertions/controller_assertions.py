def assert_controller_healthy(state):
    """Assert the controller health flag is healthy."""
    assert state["controller"]["health"] == "healthy"


def assert_startup_logs_clean(log_lines):
    """Assert startup logs do not contain any error lines."""
    assert "ERROR" not in "\n".join(log_lines)


def assert_config_active(state, expected_version):
    """Assert the active controller config version matches expectation."""
    assert state["controller"]["config_version"] == expected_version


def assert_state_preserved(state, expected_state):
    """Assert the controller state value was preserved."""
    assert state["controller"]["state"] == expected_state


def assert_watchdog_triggered(state):
    """Assert the watchdog flag was raised."""
    assert state["controller"]["watchdog"] == "triggered"


def assert_service_recovered(state):
    """Assert the controller returned to running state."""
    assert state["controller"]["state"] == "running"
