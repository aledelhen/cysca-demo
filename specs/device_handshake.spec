# Device handshake

Objective: validate that the controller can establish a trusted handshake with the device bridge.

## Device connects and responds
* Connect to the device bridge "DEV-2048"
    | key        | value     |
    | device_id  | DEV-2048  |
    | protocol   | unix-socket |
* Send a handshake request "trusted"
* Verify the device responds with an accepted state "accepted"
