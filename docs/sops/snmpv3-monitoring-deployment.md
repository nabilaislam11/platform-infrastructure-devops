# SOP: Secure SNMPv3 Monitoring on Linux

**Classification:** Public, independently authored reference  
**Status:** Example procedure; not executed or validated for this publication  
**Scope:** Authorized Linux lab with a compatible Net-SNMP installation

## 1. Purpose

Configure and verify authenticated, encrypted SNMPv3 monitoring using the `authPriv` security level. SNMPv3 is preferred over community-string-based SNMPv1/v2c when supported and appropriately configured.

## 2. Preconditions

- Approved monitoring requirement, access, and change window.
- Supported Linux distribution and Net-SNMP package version.
- Authorized monitoring collector and documented access policy.
- Approved secret-generation and storage process.
- Baseline service state, configuration backup, and rollback plan.

**Do not copy credentials or endpoint information from any production system.**

## 3. Security design

| Control | Requirement |
|---|---|
| SNMP version | SNMPv3 |
| Security level | `authPriv` |
| Authentication | Supported secure algorithm chosen per organizational policy |
| Privacy | Supported encryption algorithm chosen per organizational policy |
| Network exposure | Restrict to authorized management collectors |
| Identity | Dedicated monitoring identity with minimum necessary read access |
| Credentials | Generate unique strong secrets; store in an approved secret manager |

Algorithm availability and configuration syntax vary across Net-SNMP releases and distribution builds. Validate supported algorithms before selecting them.

## 4. Deployment procedure

1. **Inventory:** Record OS version, Net-SNMP version, service name, interface binding, and current monitoring state in an approved internal change record.
2. **Backup:** Make a permission-preserving backup of the relevant configuration before changes.
3. **Install:** Use the operating system's approved package repository to install the SNMP agent and supported utilities.
4. **Create a monitoring identity:** Use the distribution-supported Net-SNMP user creation workflow. Supply generated secrets through a secure interactive or secret-management mechanism; do not paste them into public scripts or shell history.
5. **Limit access:** Configure read-only access to only the required management information, with `authPriv` enforced.
6. **Restrict network exposure:** Bind the agent and apply host/network access controls consistent with the approved collector design.
7. **Start/restart the service:** Use the distribution's service manager after reviewing configuration changes.
8. **Validate locally:** Perform a read-only SNMPv3 query using securely supplied credentials and an approved test OID.
9. **Validate remotely:** Repeat from the authorized collector; confirm that unapproved sources cannot query the agent.
10. **Review logs:** Confirm no unexpected authentication failures, restarts, or access-policy regressions.

## 5. Safe illustrative commands

These commands only inspect service and socket state. They do not configure users or expose secrets.

```bash
rpm -q net-snmp net-snmp-utils
systemctl status snmpd --no-pager
journalctl -u snmpd -n 50 --no-pager
ss -lunp
```

Package names and service units may differ by distribution.

A **documentation-only** query structure is:

```text
snmpget -v3 -l authPriv -u <LAB_MONITOR_USER> \
  [authentication/privacy options supplied securely] \
  <LAB_HOST> <APPROVED_TEST_OID>
```

Avoid placing authentication and privacy passphrases directly in shell commands on shared systems because they may be exposed through process listings or shell history. Use the secure mechanism approved for the selected Net-SNMP version and environment.

## 6. Verification checklist

- [ ] SNMP agent is active and stable.
- [ ] Monitoring identity has read-only access.
- [ ] SNMPv3 `authPriv` query succeeds from the approved collector.
- [ ] Queries from unauthorized sources are blocked.
- [ ] Credentials are absent from shell history, logs, tickets, and public files.
- [ ] Baseline host performance and service availability are unchanged.
- [ ] Change record contains sanitized verification evidence.

## 7. Troubleshooting

| Symptom | Diagnostic area |
|---|---|
| Timeout | Agent state, bind address, firewall, routing, approved collector path |
| Authentication failure | Username, algorithm compatibility, credentials, engine synchronization |
| Privacy/decryption failure | Encryption algorithm and key configuration |
| Permission denied / missing OID | SNMP view/access configuration and supported MIB/OID |
| Intermittent polling | Network loss, agent resource pressure, collector timing |

Never disable authentication or encryption merely to make a production polling test succeed.

## 8. Rollback

Restore the previously approved configuration and service state, revert network-policy changes through the change process, and verify expected baseline behavior. Remove test identities only when their lifecycle and impact have been reviewed.

## 9. Scope limitations and references

This is an educational SOP, not a verbatim internal procedure. No real monitoring identity, secret, management address, or employer topology is included.

- [Net-SNMP documentation](https://www.net-snmp.org/docs/)
- [Net-SNMP project](https://www.net-snmp.org/)
