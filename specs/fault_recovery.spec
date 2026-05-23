# Fault recovery

Objective: prove the watchdog detects a communication failure and the service recovers cleanly.

## Service recovers after a simulated failure
* Inject a communication failure "link-drop"
    | key              | value      |
    | failure_type     | link-drop  |
    | watchdog_timeout | 5s         |
* Verify the watchdog detects the failure "triggered"
* Verify the service restarts successfully "running"
