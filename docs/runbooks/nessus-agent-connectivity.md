# Runbook: Nessus Agent Appears Offline

**Type:** Troubleshooting runbook  
**Focus:** Agent connectivity, enrollment identity, and manager check-in troubleshooting

## Symptom
A previously enrolled vulnerability-scanning agent is reported offline or stops checking in with its manager.

## Diagnostic sequence
1. **Confirm scope:** Identify affected host count, last successful check-in, recent changes, and whether the manager itself is healthy.
2. **Check service state:** Inspect the installed agent's service using the platform's service manager and review recent agent logs without exposing credentials.
3. **Check connectivity:** Resolve the configured manager hostname and test approved outbound connectivity, TLS handshake, proxy behavior, and relevant firewall paths.
4. **Check system conditions:** Verify host clock synchronization, disk space, package integrity, and whether security policy changes block agent traffic.
5. **Check enrollment state:** Review the agent's reported link/enrollment state and compare it with the management portal. Look for stale records or identity collisions, particularly after cloning images or restoring hosts.
6. **Classify the cause:** Distinguish network/proxy failures, service failures, certificate/trust issues, manager-side issues, and duplicate identities.
7. **Remediate conservatively:** Apply the least disruptive documented vendor-supported fix. Re-enrollment or identity reset requires explicit approval because it can change the asset's identity and history.

## Evidence to capture
- Sanitized agent and OS versions
- Last check-in and relevant change window
- Service state and sanitized log excerpts
- DNS, route, proxy and TLS test outcomes
- Manager-side status before and after remediation

## Exit criteria
- Agent service stable
- Manager reports successful new check-in
- No duplicate or unintended asset record
- Follow-up monitoring confirms continued connectivity

## Safety
Never publish linking keys, tokens, real manager endpoints, host identities, or internal network details. Avoid deleting agent identity files as a first-line troubleshooting step.

## Diagnostic decision
Classify the issue from observed service, network, certificate, enrollment, and manager-side evidence before selecting a corrective action.
