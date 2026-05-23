def assert_event_emitted(state, expected_event):
    """Assert the latest telemetry event matches expectation."""
    assert state["telemetry"]["last_event"] == expected_event


def assert_audit_sequence(state, expected_event):
    """Assert the audit trail ends with the expected event."""
    assert state["telemetry"]["audit_sequence"][-1] == expected_event
