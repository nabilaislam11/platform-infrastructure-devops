# Engineering Verification Index

This index organizes practical engineering references, automated checks, and reproducible lab validation plans.

| Engineering area | Technical resource | Verification approach |
|---|---|---|
| Verified log archiving | [Python utility](../../scripts/archive_verified.py) and [SOP](../sops/verified-log-archiving.md) | [Automated archive tests](../../.github/workflows/archive-utility-tests.yml) exercise member integrity, source preservation, and filename handling |
| Node Exporter | [Deployment SOP](../sops/node-exporter-deployment.md) | Lab deployment, service state, local metrics, and controlled collector access |
| SNMPv3 | [Deployment SOP](../sops/snmpv3-monitoring-deployment.md) | Authenticated and encrypted polling, identity access, and listener scope |
| Redis Sentinel | [Client runbook](../runbooks/redis-sentinel-client-connectivity.md) | Sentinel discovery, primary reachability, and client failover behavior |
| Service troubleshooting | [systemd runbook](../runbooks/linux-systemd-service-failure.md) | Service state, journal evidence, root-cause isolation, and recovery checks |
| Container persistence | [Engineering study](../engineering-studies/container-persistence-and-recovery.md) | Data persistence across recreation and backup/restore checks |
| Monitoring alerts | [Observability study](../engineering-studies/observability-design-and-failure-analysis.md) | Scrape, alert, notification, and recovery timestamp comparison |
| Patch updates | [Patch management SOP](../sops/linux-patch-change-management.md) | Package inventory, preflight checks, canary rollout, and rollback verification |

## Verification practice

Document the environment, software versions, acceptance criteria, and sanitized outputs for each practical exercise. Link successful automated runs to their corresponding commits. Maintain a clear distinction between reference procedures and recorded test results, while keeping public documentation focused on the engineering method.

All examples use independent lab contexts and avoid employer infrastructure identifiers.
