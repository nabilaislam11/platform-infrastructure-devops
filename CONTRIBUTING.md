# Engineering Review Checklist

## Technical review

1. Confirm commands and configuration examples are appropriate for the stated Linux distribution and tool versions.
2. Define prerequisites and expected results for operational procedures.
3. Include pre-change checks, post-change verification, and recovery steps where applicable.
4. Validate shell and Python utilities with the repository's automated checks.
5. Verify Markdown links, command syntax, and referenced documentation.
6. Distinguish measured outcomes from proposed configurations when presenting technical results.

## Validation

```bash
python3 scripts/validate_repository.py
```

The repository's GitHub Actions workflow also runs documentation checks on relevant changes.
