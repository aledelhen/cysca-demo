import logging


logger = logging.getLogger("cysca_mock")


def _assert_equal(actual, expected, message):
    if actual != expected:
        detail = f"{message}: expected={expected!r}, actual={actual!r}"
        logger.error(detail)
        raise AssertionError(detail)


def assert_device_accepted(state):
    """Assert the device connection and handshake were accepted."""
    _assert_equal(state["device"]["connection"], "connected", "Device connection assertion failed")
    _assert_equal(state["device"]["handshake"], "accepted", "Device handshake assertion failed")
