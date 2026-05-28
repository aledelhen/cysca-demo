import logging


logger = logging.getLogger("cysca_mock")


def _assert_equal(actual, expected, message):
    if actual != expected:
        detail = f"{message}: expected={expected!r}, actual={actual!r}"
        logger.error(detail)
        raise AssertionError(detail)


def assert_controller_healthy(state):
    """Assert the controller health flag is healthy."""
    _assert_equal(state["controller"]["health"], "healthy", "Controller health assertion failed")


def assert_startup_logs_clean(log_lines):
    """Assert startup logs do not contain any error lines."""
    actual = "ERROR" not in "\n".join(log_lines)
    _assert_equal(actual, True, "Startup log cleanliness assertion failed")


def assert_config_active(state, expected_version):
    """Assert the active controller config version matches expectation."""
    _assert_equal(
        state["controller"]["config_version"],
        expected_version,
        "Controller config version assertion failed",
    )


def assert_state_preserved(state, expected_state):
    """Assert the controller state value was preserved."""
    _assert_equal(state["controller"]["state"], expected_state, "Controller state assertion failed")


def assert_watchdog_triggered(state):
    """Assert the watchdog flag was raised."""
    _assert_equal(state["controller"]["watchdog"], "triggered", "Watchdog assertion failed")


def assert_service_recovered(state):
    """Assert the controller returned to running state."""
    _assert_equal(state["controller"]["state"], "running", "Controller recovery assertion failed")
