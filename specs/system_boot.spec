# System boot

Objective: verify the controller boots into a healthy state and produces clean startup logs.

## Controller starts cleanly
* Start the controller service "normal"
    | key      | value  |
    | boot_mode | normal |
* Verify the service reports healthy "healthy"
* Verify startup logs contain no errors "clean"
