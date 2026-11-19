# Runbook: Containerized Service Troubleshooting


## Symptom categories
- Container exits immediately or enters a restart loop.
- Container runs but its application is not ready.
- Host port is unreachable.
- Persistent data appears missing.
- Resource limits or permissions prevent startup.

## Read-only triage
```bash
docker ps -a --format '{{.Names}} {{.Status}}'
docker inspect <LAB_CONTAINER> --format '{{.State.Status}} {{.State.ExitCode}}'
docker logs --tail 100 <LAB_CONTAINER>
docker stats --no-stream
```

Use equivalent Podman commands where applicable. Inspection output and logs can contain secrets; review locally and sanitize before sharing.

## Diagnostic matrix
| Symptom | Candidate cause | Verification |
|---|---|---|
| Exited with nonzero status | Application exception, missing config, permission issue | Exit code, sanitized logs, image entrypoint |
| Repeated restarts | Restart policy masking underlying failure | Restart count, startup logs |
| Running but unhealthy | Failed readiness check or dependency | Healthcheck details and app probe |
| Port unreachable | Incorrect publishing, listener, host policy | Runtime port mapping, `ss`, authorized network test |
| Data missing after recreation | Incorrect or absent mount | Compare expected and effective mount configuration |
| Permission denied | UID/GID, SELinux labels, read-only mounts | Filesystem ownership and audit evidence |
| Resource termination | Memory/cgroup limit | Container state, kernel journal, resource telemetry |

## Safety and recovery
1. Capture baseline evidence before restarting or recreating the container.
2. Verify mount mappings and backup availability before any destructive operation.
3. Avoid pruning images, volumes, or containers during incident triage.
4. Obtain approval before changing network exposure or security policy.
5. Validate recovery at the application level, not only by checking container status.

## Scope
No real company images, container names, network addresses, logs, or proprietary runtime configuration are included.
