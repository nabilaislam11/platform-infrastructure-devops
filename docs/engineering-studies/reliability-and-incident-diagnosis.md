# Reliability Engineering and Incident Diagnosis for Linux Services

**Type:** Applied engineering study  
**Focus:** Reliability modeling, fault isolation, and recovery verification

## Abstract

Service reliability is a system property, not a process-state property. A running service can fail to satisfy its users, while a healthy host can still be unable to reach a critical dependency. This study presents a structured method to define reliability signals, localize failures, reduce diagnostic uncertainty, and validate recovery.

## 1. Reliability model

Separate the following dimensions:

| Dimension | Question | Example evidence |
|---|---|---|
| Availability | Can a client use the intended service? | Synthetic request success |
| Correctness | Does the operation return the expected result? | Contract and data-integrity checks |
| Latency | Does it respond within an agreed bound? | Request-duration distribution |
| Capacity | Is demand approaching a limiting resource? | Queue depth, CPU throttling, connection-pool use |
| Recoverability | Can service be restored safely? | Tested rollback and restoration |
| Observability | Can failures be detected and explained? | Metric, log, trace and probe coverage |

An SLO should define an observable outcome and a measurement window. A host's uptime is not automatically the service's availability.

## 2. Failure isolation workflow

1. **Establish impact:** What failed, for whom, and since when? Distinguish partial from total outage.
2. **Identify a known-good baseline:** Compare current behavior with previous verified behavior and recent changes.
3. **Check from outside inward:** Client request → DNS/TLS/network → listener → application readiness → dependencies → host resources.
4. **Correlate evidence:** Align timestamps from metrics, sanitized logs, changes, and probes. Account for clock skew.
5. **Test competing hypotheses:** Choose the lowest-risk observation that can eliminate the most possibilities.
6. **Stabilize before optimizing:** Restore service through an authorized, reversible change.
7. **Verify recovery:** Repeat meaningful functional checks and monitor for recurrence.
8. **Document learning:** Capture confirmed causes separately from contributing factors and unresolved hypotheses.

### Diagnostic decision tree

```text
User-visible failure?
  |
  +-- No --> Monitoring-only symptom?
  |           Check telemetry freshness and probe validity.
  |
  +-- Yes --> Name resolution and network path valid?
              |
              +-- No --> DNS / routing / policy / proxy investigation
              |
              +-- Yes --> Listener and TLS negotiation valid?
                          |
                          +-- No --> Service socket / certificate investigation
                          |
                          +-- Yes --> Application readiness valid?
                                      |
                                      +-- No --> Runtime / configuration / dependency investigation
                                      |
                                      +-- Yes --> Functional correctness and latency investigation
```

A passing check at one layer does not prove that all higher layers are healthy.

## 3. Incident severity and communication

Severity should be based on impact, not on how alarming a metric looks. Assign an incident owner, record timestamps, define a communication cadence, and document the next decision point. Do not publish internal incident channels or contacts.

## 4. Failure-mode and effects analysis

| Failure mode | Impact | Detectability | Mitigation to evaluate |
|---|---|---|---|
| DNS resolution failure | Client cannot reach endpoint | Resolver test | Redundant resolver configuration and change validation |
| Database unavailable | Application requests fail | Dependency probe and error rate | Connection handling, failover testing, rollback |
| Disk exhaustion | Writes fail or services degrade | Capacity and inode alerts | Retention, capacity planning |
| Exporter failure | Monitoring blind spot | Scrape health | Collector self-monitoring and independent checks |
| Misconfigured release | Readiness or correctness regression | Smoke tests and release comparison | Preflight checks and rollback |
| Notification delivery failure | Incident response delayed | Test notification | Receiver health and escalation verification |

## 5. Quantitative evaluation

For an agreed measurement period:

- **Availability ratio** = successful eligible requests / total eligible requests.
- **Error rate** = failed eligible requests / total eligible requests.
- **Detection latency** = first detection timestamp − fault onset timestamp.
- **Recovery duration** = verified restoration timestamp − incident start timestamp.

State how eligible requests and timestamps are defined. If traffic is absent, a request-based availability ratio may not measure the period meaningfully; use suitable synthetic checks and disclose the measurement method.

For an SLO of 99.95% across a 30-day period, the nominal unavailability budget is 21.6 minutes **only if availability is defined as a time fraction**. Request-based SLOs require request-count-based budgets.

## 6. Recovery verification

A reliable incident response connects failure detection to root-cause isolation, service restoration, and post-recovery checks. Key signals include application readiness, dependency connectivity, metrics freshness, alert resolution, and functional correctness.

## 7. Operational lessons

Reliable operations require a distinction between symptom and cause, process liveness and functional readiness, and apparent recovery and verified recovery. Effective incident response also depends on reversible changes and trustworthy evidence.

## References

- [Google SRE Book: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
- [Prometheus alerting practices](https://prometheus.io/docs/practices/alerting/)
- [systemd documentation](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html)

