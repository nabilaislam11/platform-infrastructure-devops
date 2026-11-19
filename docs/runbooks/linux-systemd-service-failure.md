# Runbook: Linux systemd Service Fails to Start

**Type:** Generalized troubleshooting runbook  
**Focus:** systemd failure classification, evidence collection, and recovery

## Objective
Diagnose a failed or repeatedly restarting systemd-managed service while preserving evidence and avoiding unnecessary changes.

## Initial triage
1. Confirm the authorized host and service, impact, and change window.
2. Capture service status and recent events before restarting anything.
3. Identify whether the failure is a unit configuration issue, executable failure, dependency problem, permission denial, resource exhaustion, or application-level error.

### Read-only inspection
```bash
systemctl status example.service --no-pager -l
systemctl show example.service -p ActiveState -p SubState -p Result -p ExecMainStatus -p NRestarts
journalctl -u example.service -b --no-pager -n 100
systemctl cat example.service
systemctl list-dependencies example.service
```
Replace `example.service` with the target service. Logs can contain sensitive data: redact before sharing.

## Diagnostic matrix
| Observation | Possible explanation | Next verification |
|---|---|---|
| `status=203/EXEC` | Missing executable, invalid path, permissions, or execution policy | Inspect `ExecStart`, file mode, mount options, and SELinux audit events |
| `status=217/USER` | Configured service identity unavailable | Inspect unit `User=` and account existence |
| `start-limit-hit` | Repeated failures exceeded restart policy | Diagnose underlying failure before resetting state |
| `dependency` failure | Required unit failed or ordering issue | Inspect dependent units and boot journal |
| Permission denied | DAC, SELinux, or filesystem restrictions | Inspect ownership, context, and audit evidence |
| Address already in use | Another process owns the listening socket | Inspect listeners with `ss -ltnp` |
| OOM / killed | Memory pressure or resource limit | Review kernel journal and cgroup constraints |

## Safe investigation sequence
1. Compare the effective unit and drop-ins against the intended approved configuration.
2. Check executable existence, ownership, permissions, and required environment files.
3. Inspect socket conflicts, dependencies, disk/inode availability, and system resource limits.
4. For SELinux denials, collect audit evidence; do **not** disable SELinux as a troubleshooting shortcut.
5. Apply only the least disruptive approved correction.
6. Restart the service only after approval and when the impact is understood.

## Verification
- Service reaches its intended active state and stays stable across an agreed observation window.
- Application-specific health checks pass, not merely `systemctl is-active`.
- No unexpected restart loop, permission denial, or resource regression remains.
- Change evidence and any rollback actions are recorded in a restricted system.

## Rollback
Restore the previous approved unit, environment, and binary/configuration version as appropriate; run `systemctl daemon-reload` after unit changes and validate baseline behavior.

## Boundaries
