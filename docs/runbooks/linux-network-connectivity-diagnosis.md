# Runbook: Linux Network and Service Connectivity Diagnosis

**Type:** Diagnostic runbook  

## Question
Where does a connection fail: name resolution, route, transport handshake, TLS negotiation, proxy, or application protocol?

## Investigation sequence
1. Define the expected **source**, **destination**, **protocol**, and **port** using approved internal records; never publish the real values.
2. Confirm whether the issue affects one client, many clients, or one destination.
3. Inspect name resolution and routes before modifying firewall rules.
4. Test transport reachability; distinguish timeout from immediate refusal.
5. If transport works, inspect TLS and application responses.
6. If a proxy is involved, verify the approved proxy path separately.
7. Correlate findings with recent authorized changes.

## Diagnostic commands
```bash
getent ahosts example.org
ip route
ip -br address
ss -ltnp
curl -I --connect-timeout 5 https://example.org/
```

`example.org` is a reserved example domain. Internet tests should only be performed when permitted by the environment's egress policy.

## Interpretation matrix
| Symptom | Possible layer | Useful next check |
|---|---|---|
| Name does not resolve | DNS | Resolver configuration and approved DNS service |
| Network unreachable | Routing | Interface, route, gateway, network policy |
| Connection refused | Transport/listener | Destination service and listening socket |
| Connection timeout | Filtering/path/service | Firewall, ACL, route, packet loss |
| TLS verification error | Trust/identity | Certificate chain, hostname, system clock |
| HTTP 4xx/5xx | Application | Authorization, upstream dependencies, application logs |
| Works directly but not via proxy | Proxy | Proxy policy, authentication, CONNECT behavior |

A successful TCP connection does not establish application readiness. Likewise, a failed ICMP probe alone does not prove that TCP is blocked.

## Evidence and escalation
Record sanitized timestamps, error class, test direction, and whether failure is reproducible. Escalate with a precise hypothesis and supporting evidence; do not disclose actual endpoints in public issues.

## Safety
Do not scan unknown networks, disable firewalls, or change routes as a first diagnostic step. Use authorized targets only.
