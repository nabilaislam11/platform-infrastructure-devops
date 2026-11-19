# SOP: Deploy and Validate Prometheus Node Exporter on Linux

**Type:** Standard Operating Procedure  
**Scope:** Linux hosts with systemd  

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

## Node Exporter systemd configuration

The following example assumes an **already downloaded and checksum-verified** Linux-compatible Node Exporter binary. The service runs with a dedicated non-login identity and listens on loopback, so a remote Prometheus collector cannot scrape it until an explicitly approved exposure or secure collection design is configured.

```bash
# Install the verified binary and create the service account.
sudo useradd --system --no-create-home --shell /sbin/nologin node_exporter
sudo install -o root -g root -m 0755 ./node_exporter /usr/local/bin/node_exporter
/usr/local/bin/node_exporter --version
```

Create `/etc/systemd/system/node_exporter.service`:

```ini
[Unit]
Description=Prometheus Node Exporter
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=node_exporter
Group=node_exporter
ExecStart=/usr/local/bin/node_exporter --web.listen-address=127.0.0.1:9100
Restart=on-failure
RestartSec=5
NoNewPrivileges=true
ProtectSystem=strict
ProtectHome=true
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

Activate and validate:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now node_exporter
systemctl is-active node_exporter
systemctl status node_exporter --no-pager
curl --fail --silent http://127.0.0.1:9100/metrics | head
```

**Caution:** Piping `curl` into `head` may cause a benign broken-pipe message. For a strict check, use `curl --fail --silent --output /tmp/node-exporter-lab.metrics http://127.0.0.1:9100/metrics` and inspect the file. The hardening directives may restrict collectors or filesystem visibility depending on the host; test before adapting this unit.

A collector on a different host **cannot** reach a loopback-bound exporter directly. For remote collection, review supported TLS/authentication options, the approved listener interface, and firewall restrictions rather than exposing metrics broadly.

### Rollback

```bash
sudo systemctl disable --now node_exporter
sudo rm -f /etc/systemd/system/node_exporter.service
sudo systemctl daemon-reload
```

Removing the binary or service identity is a separate approved cleanup decision. Review host-specific requirements before applying configuration changes.

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
Do not expose Node Exporter publicly. Use authenticated or encrypted transport where required by the architecture and supported by the deployment design.
