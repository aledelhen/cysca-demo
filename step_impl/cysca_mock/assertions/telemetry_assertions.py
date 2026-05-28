import logging


logger = logging.getLogger("cysca_mock")


def _assert_equal(actual, expected, message):
    if actual != expected:
        detail = f"{message}: expected={expected!r}, actual={actual!r}"
        logger.error(detail)
        raise AssertionError(detail)


def assert_event_emitted(state, expected_event):
    """Assert the latest telemetry event matches expectation."""
    _assert_equal(
        state["telemetry"]["last_event"],
        expected_event,
        "Telemetry event assertion failed",
    )


def assert_audit_sequence(state, expected_event):
    """Assert the audit trail ends with the expected event."""
    _assert_equal(
        state["telemetry"]["audit_sequence"][-1],
        expected_event,
        "Telemetry audit sequence assertion failed",
    )
