# Platform Infrastructure & DevOps Engineering

**Applied Systems Engineering | Enterprise Linux | Observability | Reliability | Security Operations**

An independently authored engineering knowledge base informed by hands-on experience in platform infrastructure and DevOps at **Nagad Limited**. It documents operational methodologies, engineering trade-offs, troubleshooting techniques, and safe verification procedures. This is not official Nagad documentation.

## Documentation Library

### Architecture & Engineering Studies

| Document | Engineering focus |
|---|---|
| [Linux Infrastructure Observability](docs/architecture/linux-infrastructure-observability.md) | Monitoring architecture, signal coverage, operational trade-offs |
| [Observability Design & Failure Analysis](docs/engineering-studies/observability-design-and-failure-analysis.md) | Failure modes, alert quality, proposed validation experiments |
| [Application Startup Failure Analysis](docs/engineering-studies/application-startup-failure-analysis.md) | Java/Spring initialization, database dependencies, diagnostic reasoning |
| [Container Persistence & Recovery](docs/engineering-studies/container-persistence-and-recovery.md) | Durable storage, backup consistency, recovery planning |

### Standard Operating Procedures

| Document | Engineering focus |
|---|---|
| [Node Exporter Deployment](docs/sops/node-exporter-deployment.md) | Secure agent deployment and scrape validation |
| [SNMPv3 Monitoring Deployment](docs/sops/snmpv3-monitoring-deployment.md) | Authenticated and encrypted infrastructure monitoring |
| [Verified Log Archiving](docs/sops/verified-log-archiving.md) | Source counts, archive integrity, destination verification |
| [SSH Access & Sudo Validation](docs/sops/ssh-access-and-sudo-validation.md) | Access controls, least privilege, safe validation |
| [Application Deployment Verification](docs/sops/application-deployment-verification.md) | Release integrity, readiness, rollback criteria |

### Troubleshooting Runbooks

| Document | Engineering focus |
|---|---|
| [Nessus Agent Connectivity](docs/runbooks/nessus-agent-connectivity.md) | Enrollment, connectivity, and agent-health diagnosis |
| [Linux systemd Service Failure](docs/runbooks/linux-systemd-service-failure.md) | Exit status, dependencies, permissions, restart loops |
| [Linux Network Connectivity Diagnosis](docs/runbooks/linux-network-connectivity-diagnosis.md) | DNS, routing, TCP, TLS, and proxy failure isolation |
| [Container Service Troubleshooting](docs/runbooks/container-service-troubleshooting.md) | Container startup, networking, mounts, resource limits |

### Engineering Templates

| Template | Purpose |
|---|---|
| [Engineering Case Study](templates/case-study.md) | Structured evidence, investigation, validation, and conclusions |
| [Method of Procedure (MOP)](templates/mop.md) | Change planning, execution, rollback, and sign-off |

## Engineering principles

- **Accuracy:** distinguish observed behavior, hypotheses, and verified results.
- **Safety:** assess impact, obtain authorization, and plan rollback before changes.
- **Verification:** define explicit success criteria and retain non-sensitive evidence.
- **Confidentiality:** never publish employer IP addresses, hostnames, credentials, internal diagrams, or proprietary configuration.
- **Reproducibility:** use generic examples and independently controlled lab environments.

## About This Repository

This repository presents technical documentation, engineering methodologies, operational procedures, and troubleshooting practices developed from hands-on experience in enterprise Platform Infrastructure & DevOps.

It focuses on Linux systems administration, infrastructure observability, security engineering, application operations, and reliability, with an emphasis on practical implementation, systematic troubleshooting, and operational best practices.

## Author

**Nabila Islam Borno**  
**System Engineer — Platform Infrastructure & DevOps**  
**Nagad Limited | Dhaka, Bangladesh**  
Email: **nabila.borno@nagad.com.bd**  
GitHub: [nabilaislam11](https://github.com/nabilaislam11)

*Independent personal repository; not affiliated with, endorsed by, or maintained on behalf of Nagad Limited.*
