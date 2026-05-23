# Configuration reload

Objective: confirm that runtime configuration changes apply without destabilizing controller state.

## Reload preserves system stability
* Update the runtime configuration "2"
    | key             | value |
    | config_version  | 2     |
    | profile_name    | ops   |
* Reload the controller "restart"
* Verify the new configuration is active "2"
* Verify existing state is preserved "reloaded"
