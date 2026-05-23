def assert_device_accepted(state):
    """Assert the device connection and handshake were accepted."""
    assert state["device"]["connection"] == "connected"
    assert state["device"]["handshake"] == "accepted"
