# Runbook: Redis Sentinel Client Connectivity and Failover Diagnosis

**Type:** Technical troubleshooting runbook  
**Scope:** Authorized test environments and generalized production principles  
**Status:** Reference procedure; no specific incident or deployment is claimed

## Problem statement

An application configured for Redis Sentinel may fail to discover the current primary, connect to a discovered node, authenticate, or recover cleanly after failover. A working TCP connection to one Sentinel does not prove that the application can reach the elected primary.

## System model

Sentinel provides monitoring, notification, and coordination for Redis primary/replica failover. Application clients typically discover the current primary using a configured Sentinel master name and a set of reachable Sentinel endpoints. Application behavior also depends on client-library capabilities and timeouts.

## Diagnostic sequence

1. Confirm whether the symptom is a new deployment failure, intermittent timeouts, or a failover-related regression.
2. Review the effective application configuration **without printing passwords or real endpoints**.
3. Validate that the Sentinel master name used by the client matches the intended logical name.
4. Confirm that the application can reach its approved Sentinel endpoints.
5. Query Sentinel state from an authorized lab host using authenticated tools where required.
6. Check whether the primary address returned by Sentinel is reachable from the application network.
7. Review authentication, TLS support, DNS behavior, client timeouts, and connection-pool behavior.
8. Correlate the incident with controlled failover events or configuration changes.

## Read-only lab examples

```text
redis-cli [approved connection and authentication options] SENTINEL masters
redis-cli [approved connection and authentication options] SENTINEL get-master-addr-by-name <LAB_MASTER_NAME>
redis-cli [approved connection and authentication options] SENTINEL sentinels <LAB_MASTER_NAME>
```

Use only authorized endpoints. Prefer secure credential injection; avoid exposing secrets in shell history, process arguments, or screenshots.

## Diagnostic matrix

| Observation | Possible explanation | Next check |
|---|---|---|
| Cannot contact any Sentinel | Network, DNS, policy, listener | Validate authorized transport path |
| Sentinel reachable, master name unknown | Incorrect logical name | Compare effective client and Sentinel configuration |
| Master discovered but unreachable | Route, ACL, bind, announced address | Test connectivity to discovered endpoint |
| Authentication failure | Wrong identity, ACL, secret source | Validate approved credential management |
| Failover occurred, clients still failing | Client refresh/reconnect behavior | Inspect client library and connection pool |
| Some Sentinels disagree | Convergence or partition issue | Inspect quorum, connectivity and authoritative state |

## Configuration change safeguards

Changing the number of Sentinel endpoints in an application configuration is **not** equivalent to changing the Sentinel quorum. Validate the actual cluster design, master name, and client library property namespace. Do not assume that every Spring application uses the same property key.

Avoid forced failover or destructive Redis commands during diagnosis without explicit change approval.

## Recovery verification

- Application discovers the intended primary.
- Authorized read/write test succeeds against a disposable test key when permitted.
- Application error rate and connection pool recover.
- Behavior remains stable through an agreed observation window.
- No sensitive configuration or real topology is published.

## References

- [Redis Sentinel documentation](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/)
- [Spring Data Redis reference](https://docs.spring.io/spring-data/redis/reference/)

*This runbook contains no actual employer configuration, node inventory, or operational event record.*
