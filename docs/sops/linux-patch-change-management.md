# Linux Server Patch Management and Update Procedure

**Document type:** Standard Operating Procedure / Method of Procedure (SOP/MOP)  
**Platform:** Red Hat Enterprise Linux (RHEL 8/9); adapt for other releases  
**Focus:** Security patching, package updates, change control, verification, and recovery

## Purpose

Provide a controlled workflow for updating Linux servers while protecting service availability, system security, and operational continuity. This procedure covers assessment, preparation, approved execution, post-update checks, and change closure.

## 1. Change scope and prerequisites

Before any production change, establish:

- Approved server scope, maintenance window, change owner, and communication plan
- Applicable security advisories, target packages, and dependency impact
- Application compatibility and required service restart or reboot
- Verified backup/snapshot and an environment-appropriate restoration plan
- Authorized console or recovery access
- Baseline monitoring, application health, disk capacity, and system state
- A canary/rolling sequence when architecture permits

**Stop condition:** Do not proceed if approval, recovery readiness, or critical baseline checks are missing.

## 2. Pre-update assessment

Run read-only checks on an authorized host. Save evidence in the approved internal change record, not in a public repository.

```bash
cat /etc/redhat-release
uname -r
uptime
df -h
df -i
free -h
systemctl --failed
rpm -qa --last | head -20
```

Review available updates and advisories:

```bash
dnf check-update
dnf updateinfo list security
dnf updateinfo info security
```

**Note:** `dnf check-update` can return exit code **100** when updates are available; that is not necessarily a command failure. Advisory information depends on enabled repository metadata.

Check package history before and after the change:

```bash
dnf history list
```

For RHEL 7, use the supported `yum` workflow and verify version-specific syntax. Do not assume RHEL 7 and RHEL 8/9 have identical patching or lifecycle support.

## 3. Risk and dependency assessment

| Risk | Assessment | Mitigation |
|---|---|---|
| Kernel update | Reboot requirement and driver compatibility | Confirm supported kernel and recovery path |
| Shared-library update | Dependent processes may require restart | Identify affected applications and schedule checks |
| Service package update | Runtime or configuration compatibility | Validate canary and approved smoke tests |
| Package conflict | Dependency resolution may fail | Review transaction before confirmation |
| Repository issue | Updates unavailable or inconsistent | Validate authorized repositories and package provenance |
| Resource pressure | Update may exhaust storage | Verify filesystem and inode headroom |

Do not disable security controls or modify repository policy merely to make a transaction succeed.

## 4. Approved patch execution

### A. Review the proposed transaction

For an approved target package in a test environment, inspect the package and transaction impact before installation:

```bash
dnf info <PACKAGE_NAME>
dnf upgrade --assumeno <PACKAGE_NAME>
```

`--assumeno` declines confirmation, but package managers may still refresh metadata; it is not a guarantee of zero side effects.

### B. Apply the approved scope

After explicit change approval, the execution owner may use the organization's authorized package workflow. Example commands:

```bash
sudo dnf upgrade <PACKAGE_NAME>
```

For broader approved maintenance, a full `dnf upgrade` may be appropriate, but it can affect many packages and services. Never treat it as a default command to run indiscriminately on production hosts.

Record the resulting transaction identifier. Review output for conflicts, scriptlet errors, package exclusions, and restart notices. Do not proceed to additional hosts if canary acceptance criteria fail.

## 5. Post-update verification

```bash
cat /etc/redhat-release
uname -r
systemctl --failed
dnf history list
rpm -q <PACKAGE_NAME>
df -h
df -i
```

If the approved environment has `needs-restarting` available:

```bash
needs-restarting -r
```

Availability and exact behavior depend on OS release and installed utilities. A kernel package update does **not** mean the running kernel changed; `uname -r` reflects the currently booted kernel.

| Verification | Pass condition |
|---|---|
| Transaction | Approved packages installed without unresolved errors |
| Versions | Installed versions match change scope |
| System | Required mounts, capacity, and critical services healthy |
| Application | Functional smoke tests and readiness checks pass |
| Network | Authorized service endpoints respond as expected |
| Security | SELinux, firewall, access policy, and required agents remain operational |
| Observability | Metrics and alerting resume expected behavior |
| Reboot | Completed only when approved and required, with post-boot checks |

Do not declare success solely because the package manager exited with code zero.

## 6. Recovery and rollback

1. Stop the rollout on failed validation.
2. Preserve diagnostic evidence and communicate impact through approved channels.
3. Determine whether the problem is a package conflict, service regression, configuration issue, or unrelated fault.
4. Use the **preapproved, tested** recovery method: application rollback, snapshot/backup restoration, or a supported package recovery path.
5. Verify application correctness and monitoring after recovery.
6. Record the outcome and defer remaining hosts until the cause is understood.

**Important:** `dnf history undo` and package downgrades are not guaranteed to restore the prior system state. Kernel, database, filesystem, or application changes may require different recovery mechanisms.

## 7. Change record template

| Field | Record |
|---|---|
| Change identifier | Internal system only |
| Approved scope | Authorized inventory only |
| Reason | Advisory / defect / planned maintenance |
| Baseline | OS, kernel, package and service state |
| Recovery plan | Backup or tested restoration procedure |
| Execution | Approved package transaction and timestamps |
| Validation | Functional and operational evidence |
| Result | Successful / rolled back / deferred |
| Review | Authorized change owner |

## 8. Practical engineering considerations

- Prefer risk-based prioritization for security advisories, not indiscriminate patching.
- Coordinate patching with application owners and service dependencies.
- Use rolling maintenance only where redundancy and failover behavior are understood.
- Validate actual application functionality, not merely process existence.
- Treat security-agent health and monitoring coverage as post-change acceptance criteria.
- Keep real infrastructure details and change evidence within authorized systems.

## References

- [Red Hat Enterprise Linux documentation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/)
- [DNF command reference](https://dnf.readthedocs.io/en/latest/command_ref.html)
- [Red Hat security advisories](https://access.redhat.com/security/security-updates/)

