# Repository Quality Assurance Checklist

## Navigation and structure

- [ ] Every published document is discoverable from the README or a relevant index.
- [ ] Relative Markdown links resolve to tracked files.
- [ ] Headings, titles and document classifications are consistent.
- [ ] References use authoritative public sources where feasible.

## Technical correctness

- [ ] Commands specify required OS/tool versions and privileges.
- [ ] Read-only and state-changing commands are clearly distinguished.
- [ ] Destructive actions require explicit authorization.
- [ ] Each SOP and MOP includes prerequisites, success criteria, and rollback/recovery.
- [ ] Runbooks distinguish symptom, hypothesis, observation and conclusion.
- [ ] Test results are reported only when evidence exists.

## Confidentiality and integrity

- [ ] No employer infrastructure identifiers, real addresses, credentials or topology.
- [ ] No private or proprietary configurations, internal logs, screenshots or customer data.
- [ ] Examples are generic and independently authored.
- [ ] No invented benchmarks, deployments, incident outcomes or academic claims.
- [ ] Automated checks are supplemented by human review.

## Publication acceptance

- [ ] `python3 scripts/validate_repository.py` passes locally.
- [ ] GitHub Actions documentation-validation job succeeds.
- [ ] External links are spot-checked manually.
- [ ] Document owner reviews technical and confidentiality requirements.

A passing automated check is not proof of technical correctness or confidentiality.
