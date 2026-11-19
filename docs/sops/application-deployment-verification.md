# SOP: Application Deployment Verification and Rollback Readiness

**Focus:** Release readiness, artifact integrity, deployment checks, and rollback

## Objective
Validate an authorized application deployment across artifact identity, runtime readiness, dependencies, functional checks, and rollback preparedness.

## Preconditions
- Approved change request, service owner, release identifier, and maintenance window
- Tested artifact and documented compatibility requirements
- Backup or immutable previous artifact available
- Approved access and rollback decision authority
- Baseline health, latency, and error-rate observations

## Pre-deployment
1. Record the approved release and cryptographic artifact checksum.
2. Verify target runtime and dependencies meet compatibility requirements.
3. Review configuration differences without printing secrets.
4. Confirm database/schema migration compatibility and rollback constraints.
5. Confirm health-check definitions and escalation contacts.

## Deployment
Follow the approved deployment mechanism. Avoid unreviewed manual edits to running application state. Record change timestamps and artifact identity.

## Post-deployment validation
| Layer | Check | Pass criterion |
|---|---|---|
| Artifact | Version or commit identifier | Matches approved release |
| Process | Service state and restart count | Stable over observation period |
| Network | Authorized listener and route | Expected endpoint reachable |
| Dependencies | Database/cache/broker connectivity | Required dependencies healthy |
| Application | Readiness and smoke test | Expected response and behavior |
| Reliability | Error rate, latency, saturation | Within agreed baseline or threshold |
| Security | Permissions and configuration | No unapproved exposure |

A successful process start does **not** prove application readiness.

## Stop and rollback triggers
- Persistent readiness failure or critical dependency error
- Material error-rate or latency regression
- Unexpected permission or security exposure
- Data migration incompatibility or integrity concern

Rollback may require more than replacing the binary if a schema or data migration has occurred. Verify compatibility and obtain authorization before executing.

## Evidence
Store sanitized release identifiers, test outcomes, timestamps, and approvals in the authorized change record. Do not publish internal endpoints, configuration values, credentials, or raw production logs.

## Application
Adapt acceptance criteria, release controls, and rollback triggers to the authorized application and change process.
