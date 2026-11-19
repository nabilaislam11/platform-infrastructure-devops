# SOP: Verified Linux Log Archiving

**Objective:** Archive selected log files while proving archive integrity and preserving source files until verification is complete.

## Preconditions
- Authorized source and destination paths
- Approved filename/date selection criteria
- Sufficient destination space
- Explicit retention and deletion authorization, if deletion is ever requested

## Procedure
1. Inventory the exact source files and record the **source-file count** before creating an archive. Use null-delimited filenames to handle spaces safely.
2. Create a tar archive with relative member paths using `tar -C "$SOURCE" ...`, avoiding absolute paths.
3. Run `gzip -t "$ARCHIVE"` and fail the operation if integrity validation fails.
4. List archive entries with `tar -tzf "$ARCHIVE"`; count regular-file entries and compare with the recorded source-file count. Account explicitly for any directory entries if included.
5. Transfer or move the verified archive to the authorized destination.
6. Run `gzip -t` and repeat the archive-entry count **at the destination**.
7. Record archive size, file counts, checksum, timestamp, and destination.
8. **Do not delete source logs** unless a separately authorized retention action requires it, and only after all validations succeed.

## Example verification commands
```bash
gzip -t "$ARCHIVE" || exit 1
tar -tzf "$ARCHIVE" >/dev/null || exit 1
```

For exact count comparisons, use a documented manifest of selected source filenames and compare that manifest with the archive's member list. Ensure the archive contains only the intended regular files; symlinks and directory entries require separate handling.

## Failure response
If any count, checksum, integrity, or destination verification fails, retain all source files and stop. Investigate selection criteria, concurrent log rotation, partial transfer, and unexpected archive members.

## Operational caution
Do not run destructive cleanup commands as part of an unreviewed example. This procedure deliberately does not include source deletion.
