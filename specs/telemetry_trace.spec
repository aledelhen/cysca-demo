# Telemetry trace

Objective: ensure operational events are emitted and recorded in the correct audit sequence.

## Events are recorded in order
* Trigger an operational command "command_issued"
    | key        | value          |
    | event_name | command_issued |
    | source     | operator       |
* Verify the telemetry event is emitted as command_issued "command_issued"
* Verify the audit trail keeps the same sequence for command_issued "command_issued"

## Parameterized telemetry flow
* Trigger an operational command "command_issued" from "operator"
* Verify the telemetry event "command_issued" was emitted
* Verify the telemetry source "operator" was recorded
