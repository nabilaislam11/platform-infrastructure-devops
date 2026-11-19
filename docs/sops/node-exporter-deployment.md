# SOP: Deploy and Validate Prometheus Node Exporter on Linux

**Type:** Standard Operating Procedure  
**Scope:** Authorized Linux lab or managed host  
**Status:** Reference procedure; version and platform compatibility must be verified before use

## Preconditions
- Approved change and maintenance window where required.
- Supported Node Exporter release and verified artifact checksum.
- Authorized administrator access, approved firewall rules and Prometheus collector.
- Rollback plan and baseline host/service observations.

## Procedure
1. Record OS, architecture, current exporter status, and active monitoring configuration.
2. Obtain a release from the official Prometheus Node Exporter project and verify its published checksum before installation.
3. Create a dedicated non-login service identity and install the binary with restrictive ownership and permissions.
4. Create a systemd unit using the verified binary path. Bind the listener only to an approved interface and restrict network access to authorized collectors.
5. Run `systemctl daemon-reload`, enable/start the unit as approved, and inspect `systemctl status node_exporter` and `journalctl -u node_exporter`.
6. Confirm that the exporter serves `/metrics` locally; then verify access from the authorized Prometheus collector.
7. Add or update the Prometheus scrape target through the organization's change process.
8. Confirm the target is UP and expected metrics are queryable; observe behavior across at least one scrape interval.

## Verification checklist
- [ ] Binary checksum matches the official release
- [ ] Dedicated service identity and expected permissions
- [ ] Systemd unit active without repeated restarts
- [ ] Metrics endpoint accessible only from approved networks
- [ ] Prometheus target UP and metrics current
- [ ] No unexpected host resource or security impact

## Rollback
Restore the previous unit and binary or stop/disable the new service, revert scrape configuration and network changes, then verify baseline monitoring behavior. Preserve non-sensitive change evidence.

## Notes
Do not expose Node Exporter publicly. Use authenticated or encrypted transport where required by the architecture and supported by the deployment design. This SOP is an educational adaptation, not an employer procedure.
