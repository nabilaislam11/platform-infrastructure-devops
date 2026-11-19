# Engineering Study: Diagnosing Application Startup Failures

**Type:** Applied diagnostic analysis  
**Focus:** Java/Spring startup diagnostics and dependency fault isolation

## Research question
How can an engineer distinguish an application defect from a dependency, network, credential, or runtime failure when a Java/Spring application does not become ready?

## Diagnostic layers
1. **Process and runtime:** Java version, process exit status, memory limits, JVM options.
2. **Configuration:** Effective application profile, required properties, environment-variable injection.
3. **Network:** DNS, route, firewall, proxy, destination listener.
4. **TLS/authentication:** Certificate chain, identity, secrets injection, account status.
5. **Dependency:** Database, cache, broker, or external service health.
6. **Application:** Framework initialization, schema compatibility, migrations, bean creation.

## Example: connection pool initialization failure
A Spring Boot application using HikariCP may fail during datasource initialization if its database is unreachable. A top-level `BeanCreationException` or `UnsatisfiedDependencyException` may be a wrapper; the most useful clue is often the deepest causal exception.

| Evidence | Hypothesis | Verification |
|---|---|---|
| Name resolution failure | DNS misconfiguration | Resolve configured hostname through authorized resolver |
| Connection timeout | Routing, filtering, or destination availability | Check approved transport path and listener |
| Connection refused | Listener absent or wrong port | Confirm approved endpoint and service state |
| TLS handshake failure | Certificate or protocol mismatch | Validate trust, hostname, and protocol compatibility |
| Authentication rejected | Credential or authorization problem | Validate approved secret source and database account status |
| Connection established, query fails | Schema or database issue | Review database-side sanitized errors and application query context |

## Recommended workflow
1. Capture startup timestamp, release identifier, and sanitized error chain.
2. Find the deepest causal exception; distinguish wrapper exceptions from initiating failures.
3. Compare intended configuration with effective runtime configuration without printing secrets.
4. Verify one dependency at a time, from DNS to application-level response.
5. Correlate the failure with recent changes and known-good behavior.
6. Make only authorized corrective changes, with a rollback path.
7. Verify readiness and a meaningful functional test after recovery.

## Anti-patterns
- Repeated restarts without understanding the failure.
- Treating a successful ping as proof of database connectivity.
- Publishing stack traces containing internal addresses, usernames, tokens, or JDBC URLs.
- Changing hosts files when the application uses a literal IP address and DNS is not involved.
- Disabling TLS verification to bypass certificate problems.

## Proposed lab validation
Build a local demonstration app and database; independently induce DNS failure, refused connection, invalid credentials, and unavailable database. Record sanitized logs and actual recovery times.

## Diagnostic interpretation
Interpret exception chains alongside application configuration, dependency health, and observed network behavior. Validate each root-cause hypothesis with a targeted check.
