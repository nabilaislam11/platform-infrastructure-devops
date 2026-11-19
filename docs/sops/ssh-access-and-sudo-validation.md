# SOP: SSH Access and Least-Privilege Sudo Validation

**Type:** Access-control validation SOP  
**Status:** Generalized reference, not an employer-specific policy

## Purpose
Validate that a provisioned Linux identity can perform only the explicitly approved actions, without weakening authentication or exposing secrets.

## Preconditions
- Approved access request and scope
- Defined role and required command permissions
- A separate administrator recovery path
- Approved maintenance window if SSH or sudo policy will change

## Validation
1. Confirm account identity and group membership using `id <LAB_USER>`.
2. Review the applicable SSH daemon policy with an administrator. Evaluate effective configuration, including `Match` blocks, rather than assuming a single file line governs access.
3. Inspect account expiry and password policy through approved administrative tooling.
4. Confirm login through the authorized access path.
5. Check allowed sudo commands with `sudo -l` from the intended user context.
6. Test approved operations and carefully chosen denied operations in an isolated lab; never attempt prohibited actions against production systems merely to demonstrate a restriction.
7. Verify auditability and record sanitized results.

## Read-only examples
```bash
id
sudo -l
sshd -t
```

Run `sshd -t` only where you have authorization and an appropriate administrative context. It validates syntax, not the security of the complete policy.

## Design cautions
- `NOPASSWD` does not imply least privilege; command scope and argument handling matter.
- Broad commands, shells, editors, interpreters, and unrestricted service management can allow privilege escalation.
- Restrictions on `su` alone do not prevent equivalent root access through other sudo-allowed commands.
- Validate SSH changes before reload and retain a tested recovery session.
- Do not add or replace `AllowUsers` directives without reviewing the complete effective policy and access impact.

## Acceptance criteria
Only authorized login paths and commands work; denied operations remain denied; access is logged; recovery remains possible.

## Rollback
Restore approved policy from backup and validate access from an existing administrative session before closing it.

## Public documentation rule
No real usernames, credential material, access lists, internal jump-host details, or employer-specific sudo policy.
