# SOP: Verified Linux Log Archiving

**Objective:** Archive an explicitly selected set of regular log files, prove source-file and archive-entry counts match, verify content and destination integrity, and retain originals.

**Implementation:** [Verified archiving utility](../../scripts/archive_verified.py) (Python 3 standard library).

## Preconditions

- Exact authorized source and destination directories and filename/date selection criteria.
- Sufficient disk space and read/write permissions.
- A stable file set: pause rotation/writes or work from a consistent snapshot where required.
- An archive name that does not already exist at the destination.
- Separate approval for any later deletion; **this workflow never deletes source files**.

## Procedure

1. Identify the source and destination directories and review the filename pattern.
2. Count the selected top-level regular source files. Exclude symlinks and directories.
3. Create a gzip-compressed tar archive with relative member names.
4. Verify every archive member is a regular file; compare **member count, member names, and SHA-256 content hashes** against the source manifest.
5. Copy to the destination without overwriting an existing archive.
6. Repeat member and content checks at the destination, and compare the archive checksum with the staged archive.
7. Report source-file count and verified archive-entry count; retain source files.

## Archiving example

```bash
mkdir -p ./sample-logs ./archives
printf 'example one\n' > ./sample-logs/service-2025-01.log
printf 'example two\n' > ./sample-logs/service-2025-02.log

python3 scripts/archive_verified.py \
  --source ./sample-logs \
  --destination ./archives \
  --pattern '*-2025-*.log' \
  --name logs-2025.tar.gz
```

**Expected behavior (not a measured run):** Two source files selected; two regular archive entries; staged and destination member/content checks pass; source files remain unchanged.

The script reports failure for an empty selection, changed content during staging, nonmatching archive membership, checksum mismatch, or a destination name already in use. The script does not guarantee an atomic snapshot of files being actively written: quiesce writers or use a consistent snapshot for such workloads.

## Acceptance criteria

- [ ] Source-file count recorded before archiving
- [ ] Archive count equals source-file count
- [ ] Member names and content hashes match source selection
- [ ] Destination archive reverified after transfer
- [ ] Source logs retained
- [ ] Authorized change record contains outcome and evidence

## Failure handling

Stop and investigate the selection rule, file rotation, changed content, partial transfer, or permissions. Retain all source files. An incomplete destination archive must be handled only under an authorized cleanup procedure; the utility does not automatically delete it.

