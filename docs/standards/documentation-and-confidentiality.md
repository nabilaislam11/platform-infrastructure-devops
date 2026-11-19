# Engineering Documentation and Publication Standard

**Purpose:** Maintain technically accurate, consistent, and reviewable engineering documentation.

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

## 5. Review workflow

1. Draft technical content.
2. Check correctness against official product documentation.
3. Review confidentiality and intellectual-property boundaries.
4. Verify links and internal navigation.
5. Record whether examples were executed or are illustrative.
6. Publish only the sanitized, independently authored material.

