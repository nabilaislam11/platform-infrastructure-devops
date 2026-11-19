# Engineering Verification Index

This index organizes practical engineering references, automated checks, and operational verification methods.

| Engineering area | Technical resource | Verification approach |
|---|---|---|
| Verified log archiving | [Python utility](../../scripts/archive_verified.py) and [SOP](../sops/verified-log-archiving.md) | [Automated archive tests](../../.github/workflows/archive-utility-tests.yml) exercise member integrity, source preservation, and filename handling |
| Node Exporter | [Deployment SOP](../sops/node-exporter-deployment.md) | Service state, local metrics, and collector access |
| SNMPv3 | [Deployment SOP](../sops/snmpv3-monitoring-deployment.md) | Authenticated and encrypted polling, identity access, and listener scope |
| Redis Sentinel | [Client runbook](../runbooks/redis-sentinel-client-connectivity.md) | Sentinel discovery, primary reachability, and client failover behavior |
| Service troubleshooting | [systemd runbook](../runbooks/linux-systemd-service-failure.md) | Service state, journal evidence, root-cause isolation, and recovery checks |
| Container persistence | [Engineering study](../engineering-studies/container-persistence-and-recovery.md) | Data persistence across recreation and backup/restore checks |
| Monitoring alerts | [Observability study](../engineering-studies/observability-design-and-failure-analysis.md) | Scrape, alert, notification, and recovery timestamp comparison |
| Patch updates | [Patch management SOP](../sops/linux-patch-change-management.md) | Package inventory, preflight checks, canary rollout, and rollback verification |

