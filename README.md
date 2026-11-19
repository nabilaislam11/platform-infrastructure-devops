# Platform Infrastructure & DevOps Engineering

**Applied Systems Engineering | Enterprise Linux | Observability | Reliability | Security Operations**

A technical engineering portfolio covering enterprise Linux administration, observability, security operations, deployment verification, and reliability engineering. It brings together practical system administration workflows, troubleshooting runbooks, standard operating procedures, engineering studies, and automation utilities.

## Documentation Library

### Architecture & Engineering Studies

| Document | Engineering focus |
|---|---|
| [Linux Infrastructure Observability](docs/architecture/linux-infrastructure-observability.md) | Monitoring architecture, signal coverage, operational trade-offs |
| [Observability Design & Failure Analysis](docs/engineering-studies/observability-design-and-failure-analysis.md) | Failure modes, alert quality, monitoring validation methodology |
| [Application Startup Failure Analysis](docs/engineering-studies/application-startup-failure-analysis.md) | Java/Spring initialization, database dependencies, diagnostic reasoning |
| [Container Persistence & Recovery](docs/engineering-studies/container-persistence-and-recovery.md) | Durable storage, backup consistency, recovery planning |
| [Reliability & Incident Diagnosis](docs/engineering-studies/reliability-and-incident-diagnosis.md) | Service reliability, fault isolation, SLO measurement and incident response |

### Standard Operating Procedures

| Document | Engineering focus |
|---|---|
| [Node Exporter Deployment](docs/sops/node-exporter-deployment.md) | Secure agent deployment and scrape validation |
| [SNMPv3 Monitoring Deployment](docs/sops/snmpv3-monitoring-deployment.md) | Authenticated and encrypted infrastructure monitoring |
| [Verified Log Archiving](docs/sops/verified-log-archiving.md) | Source counts, member hashes, destination verification; [Python utility](scripts/archive_verified.py) |
| [SSH Access & Sudo Validation](docs/sops/ssh-access-and-sudo-validation.md) | Access controls, least privilege, safe validation |
| [Application Deployment Verification](docs/sops/application-deployment-verification.md) | Release integrity, readiness, rollback criteria |
| [Linux Patch Change Management](docs/sops/linux-patch-change-management.md) | Patching risk, canary validation, recovery planning |

### Troubleshooting Runbooks

| Document | Engineering focus |
|---|---|
| [Nessus Agent Connectivity](docs/runbooks/nessus-agent-connectivity.md) | Enrollment, connectivity, and agent-health diagnosis |
| [Linux systemd Service Failure](docs/runbooks/linux-systemd-service-failure.md) | Exit status, dependencies, permissions, restart loops |
| [Linux Network Connectivity Diagnosis](docs/runbooks/linux-network-connectivity-diagnosis.md) | DNS, routing, TCP, TLS, and proxy failure isolation |
| [Container Service Troubleshooting](docs/runbooks/container-service-troubleshooting.md) | Container startup, networking, mounts, resource limits |
| [Redis Sentinel Client Connectivity](docs/runbooks/redis-sentinel-client-connectivity.md) | Discovery, authentication, failover and dependency diagnosis |

### Engineering Templates

| Template | Purpose |
|---|---|
| [Engineering Case Study](templates/case-study.md) | Structured evidence, investigation, validation, and conclusions |
| [Method of Procedure (MOP)](templates/mop.md) | Change planning, execution, rollback, and sign-off |
| [Incident Review](templates/incident-review.md) | Evidence-led review, root-cause analysis and preventive actions |

## Engineering verification

- [Engineering Verification Index](docs/standards/evidence-and-validation-index.md) — procedures, automated checks, and lab validation plans.

## Repository quality controls

- [Quality Assurance Checklist](docs/standards/quality-assurance-checklist.md) — technical review, confidentiality, navigation, and evidence requirements.
- [Verified Log Archive Utility](scripts/archive_verified.py) — non-destructive archive creation and content verification.
- [Automated Markdown Validation](scripts/validate_repository.py) — local link verification and heuristic sensitive-pattern warnings; run with `python3 scripts/validate_repository.py`.
- [GitHub Actions Validation](.github/workflows/docs-validation.yml) — runs documentation checks on Markdown changes.

## Engineering approach

- **Operational reliability:** establish baselines, diagnose failures systematically, and validate recovery.
- **Controlled change:** define prerequisites, verification criteria, and rollback steps.
- **Automation:** use repeatable scripts and explicit integrity checks.
- **Observability:** correlate host metrics, service health, and actionable alerts.

## Author

**Nabila Islam Borno**  
**System Engineer — Platform Infrastructure & DevOps**  
**Nagad Limited | Dhaka, Bangladesh**  
Email: **nabila.borno@nagad.com.bd**  
GitHub: [nabilaislam11](https://github.com/nabilaislam11)

