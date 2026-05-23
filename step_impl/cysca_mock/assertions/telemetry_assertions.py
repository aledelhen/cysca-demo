def assert_event_emitted(state, expected_event):
    assert state["telemetry"]["last_event"] == expected_event


def assert_audit_sequence(state, expected_event):
    assert state["telemetry"]["audit_sequence"][-1] == expected_event
