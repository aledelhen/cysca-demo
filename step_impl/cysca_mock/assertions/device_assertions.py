def assert_device_accepted(state):
    assert state["device"]["connection"] == "connected"
    assert state["device"]["handshake"] == "accepted"
