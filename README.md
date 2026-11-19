# Platform Infrastructure & DevOps Engineering

**Applied Systems Engineering | Enterprise Linux | Observability | Reliability | Security Operations**

An independent engineering knowledge base informed by hands-on Platform Infrastructure & DevOps experience at **Nagad Limited**. It presents Linux administration, observability, security operations, deployment verification, and reliability practices through technical studies, runbooks, SOPs, and reusable lab utilities. This is not official employer documentation.

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

### Documentation Standards

- [Documentation & Confidentiality Standard](docs/standards/documentation-and-confidentiality.md) — evidence labeling, publication safety, and technical review requirements.

## Engineering verification

- [Engineering Verification Index](docs/standards/evidence-and-validation-index.md) — procedures, automated checks, and lab validation plans.

## Repository quality controls

- [Quality Assurance Checklist](docs/standards/quality-assurance-checklist.md) — technical review, confidentiality, navigation, and evidence requirements.
- [Contribution and Review Guide](CONTRIBUTING.md) — documentation conventions and publication checks.
- [Verified Log Archive Utility](scripts/archive_verified.py) — independently authored, non-destructive archive creation and content verification.
- [Automated Markdown Validation](scripts/validate_repository.py) — local link verification and heuristic sensitive-pattern warnings; run with `python3 scripts/validate_repository.py`.
- [GitHub Actions Validation](.github/workflows/docs-validation.yml) — runs documentation checks on Markdown changes.

## Engineering principles

- **Accuracy:** distinguish observed behavior, hypotheses, and verified results.
- **Safety:** assess impact, obtain authorization, and plan rollback before changes.
- **Verification:** define explicit success criteria and retain non-sensitive evidence.
- **Confidentiality:** never publish employer IP addresses, hostnames, credentials, internal diagrams, or proprietary configuration.
- **Reproducibility:** use generic examples and independently controlled lab environments.

## Author

**Nabila Islam Borno**  
**System Engineer — Platform Infrastructure & DevOps**  
**Nagad Limited | Dhaka, Bangladesh**  
Email: **nabila.borno@nagad.com.bd**  
GitHub: [nabilaislam11](https://github.com/nabilaislam11)

*Independent personal repository; not affiliated with, endorsed by, or maintained on behalf of Nagad Limited.*
