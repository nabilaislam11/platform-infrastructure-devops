# Evidence and Validation Index

This index separates **documented procedures**, **automated tests**, and **future lab experiments**. A technical explanation does not by itself establish successful execution.

| Area | Current artifact | Evidence status | Next reproducible validation |
|---|---|---|---|
| Verified log archiving | [Python utility](../../scripts/archive_verified.py) and [SOP](../sops/verified-log-archiving.md) | Automated disposable-data test via [GitHub Actions](../../.github/workflows/archive-utility-tests.yml) | Test changed-file and interrupted-copy failure handling |
| Node Exporter | [Deployment SOP](../sops/node-exporter-deployment.md) | Reference lab procedure; no recorded run | Deploy on disposable Linux VM and capture sanitized checks |
| SNMPv3 | [Deployment SOP](../sops/snmpv3-monitoring-deployment.md) | Reference lab procedure; no recorded run | Verify authPriv, denied identity, and loopback exposure |
| Redis Sentinel | [Client runbook](../runbooks/redis-sentinel-client-connectivity.md) | Read-only lab commands documented; no recorded run | Run disposable Sentinel topology and test discovery |
| Service troubleshooting | [systemd runbook](../runbooks/linux-systemd-service-failure.md) | Analytical reference | Induce a safe unit failure and record diagnosis |
| Container persistence | [Engineering study](../engineering-studies/container-persistence-and-recovery.md) | Proposed experiment | Recreate disposable stateful container and verify restore |
| Monitoring alerts | [Observability study](../engineering-studies/observability-design-and-failure-analysis.md) | Proposed experiments | Collect actual scrape/alert/delivery timestamps |
| Patch updates | [Patch management SOP](../sops/linux-patch-change-management.md) | Reference procedure; no recorded run | Test on disposable RHEL-compatible environment |

## Evidence rules

- **Automated test passed:** Link to the exact workflow and commit when reporting a test outcome.
- **Documented only:** Commands and expected behavior are illustrative, not execution evidence.
- **Observed:** Include the test environment, commands, sanitized output, date, and result.
- **Inferred:** Separate analysis from observations and state uncertainty.
- **Employer operations:** Do not publish internal records, screenshots, logs, hostnames, network details, or proprietary artifacts.

This index is intentionally conservative. Do not change an evidence status to *validated* until a reproducible test has actually run and the evidence is publishable.
