# Engineering Documentation and Publication Standard

**Purpose:** Maintain technically useful, reviewable, and confidentiality-safe public documentation.

## 1. Document classifications

| Classification | Definition | Required handling |
|---|---|---|
| SOP | Repeatable approved process | Preconditions, actions, checks, rollback |
| MOP | Controlled change plan | Scope, risks, approvals, hold points, recovery |
| Runbook | Diagnostic and response workflow | Symptoms, evidence, decisions, safe resolution |
| Engineering study | Technical reasoning or comparison | Question, assumptions, analysis, limitations |
| Experiment | Reproducible test | Setup, procedure, raw evidence, actual outcomes |
| Case study | Examined event or problem | Evidence provenance, timeline, findings, uncertainty |

## 2. Evidence rules

Use clear labels:
- **Observed:** Directly supported by a documented test or authorized evidence.
- **Inferred:** A conclusion drawn from observations, with stated assumptions.
- **Proposed:** A plan, experiment, or recommendation not yet executed.
- **Illustrative:** A fabricated generic example used for explanation, not a real incident.

Never fabricate benchmark values, incident timelines, test results, change approvals, or successful deployments.

## 3. Publication safety checklist

Before committing a file, confirm:

- [ ] No real employer IP addresses, internal DNS names, server labels, inventories or network segmentation
- [ ] No credentials, secrets, tokens, private keys, certificates or authentication strings
- [ ] No actual production configuration files, unredacted logs, screenshots or internal URLs
- [ ] No proprietary incident records, diagrams, ticket references or customer data
- [ ] No internal software artifacts or company-owned code
- [ ] All examples are independently written with generic placeholders
- [ ] Commands are safe for the stated environment and warn about destructive effects
- [ ] Claims about tests, performance, incidents and deployments match evidence
- [ ] External references are public and relevant
- [ ] Links and Markdown formatting have been reviewed

## 4. Safe examples

Use placeholders such as `<LAB_HOST>`, `<SERVICE_NAME>`, and `<APPROVED_PORT>`. For network diagrams that genuinely require addresses, use documentation ranges reserved by RFC 5737, not remembered infrastructure values.

Do not merely replace an employer hostname while preserving a real internal topology or deployment relationship. Rewrite the example as a generic architecture.

## 5. Review workflow

1. Draft technical content.
2. Check correctness against official product documentation.
3. Review confidentiality and intellectual-property boundaries.
4. Verify links and internal navigation.
5. Record whether examples were executed or are illustrative.
6. Publish only the sanitized, independently authored material.

## 6. Professional attribution

The author may state her verified role and employer. This repository is independently maintained and does not represent official employer documentation or endorsement.
