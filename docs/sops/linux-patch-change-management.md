# MOP: Linux Package Patching with Verification and Recovery Planning

**Type:** Generalized Method of Procedure  
**Status:** Template for authorized change planning; not an executed change

## Objective

Apply approved Linux package updates while maintaining change control, documenting impact, and validating service health.

## Preconditions

- Approved scope, package advisories, maintenance window, and rollback owner
- Verified backups or snapshots appropriate to the workload
- Known application compatibility and reboot requirements
- Access through an authorized recovery channel
- Baseline health, storage capacity, service dependencies and monitoring state

## Phase 1 — Assess

1. Identify OS release, package manager, enabled repositories and approved patch baseline.
2. Review applicable security advisories and package dependencies.
3. Identify kernel, library, and service updates that may require restart or reboot.
4. Confirm sufficient disk space, backup integrity, and recovery constraints.
5. Define the canary scope and success criteria.

## Phase 2 — Prepare

Record package versions and service status in the approved internal change record. Obtain required approvals before modifying packages. Do not expose repository credentials or internal package mirrors in public documentation.

## Phase 3 — Execute

Use the organization's approved package-management workflow for the target distribution and version. Apply changes first to the authorized canary environment where practical. Monitor the update for dependency conflicts, transaction failures, and unexpected service restarts.

This document deliberately does not provide an unconditional mass-update command for production hosts.

## Phase 4 — Validate

| Check | Acceptance criterion |
|---|---|
| Package transaction | Completed without unresolved errors |
| Installed versions | Match approved patch baseline |
| Service health | Required services stable and ready |
| Functional checks | Approved application smoke tests pass |
| Security | Expected controls remain enforced |
| Monitoring | Telemetry and alerts restored to expected state |
| Reboot | Performed and verified only if required and approved |

## Phase 5 — Recovery

Package downgrades are not universally safe, especially after schema, kernel, or library changes. Choose a previously tested restoration mechanism appropriate to the system. Stop rollout on failed canary validation and escalate according to the change plan.

## Evidence

Record sanitized change timing, version deltas, validation results, unresolved issues, and reviewer sign-off. Never publish real host inventories or internal patching schedules.

## References

- [Red Hat Enterprise Linux documentation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/)
