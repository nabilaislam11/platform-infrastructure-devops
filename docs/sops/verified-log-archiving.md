# SOP: Verified Linux Log Archiving

**Objective:** Create and transfer an archive of explicitly selected regular log files, verify exact file membership and integrity, and preserve all source files.

**Environment:** Authorized Linux lab or managed system with GNU tar, gzip, find, sort, cmp, sha256sum and Bash. This is a reference workflow, not a record of an executed production change.

## Preconditions

- Confirm the exact approved source directory, destination directory, selection rule, and archive filename.
- Ensure sufficient free space, permissions, and a stable set of source files. Avoid concurrent log rotation or active writes during capture.
- Use a dedicated destination archive name that does not already exist.
- No source-file deletion is part of this procedure.

## Safe end-to-end example

The example selects **top-level regular files** matching a date-based filename pattern. It rejects symlinks and directory entries by design. Substitute only approved paths and patterns.

```bash
#!/usr/bin/env bash
set -euo pipefail

SOURCE="/path/to/approved/source"
DEST="/path/to/approved/destination"
PATTERN="*-2025-*.log"
ARCHIVE_NAME="logs-2025.tar.gz"

[[ -d "$SOURCE" && -d "$DEST" ]] || { echo "Missing source or destination"; exit 1; }
[[ "$SOURCE" != "$DEST" ]] || { echo "Source and destination must differ"; exit 1; }
[[ ! -e "$DEST/$ARCHIVE_NAME" ]] || { echo "Destination archive already exists"; exit 1; }

# Work in a private staging directory; do not stage manifests in the source.
WORK="$(mktemp -d)"
trap 'rm -rf -- "$WORK"' EXIT

# Null-delimited manifest supports spaces and unusual filenames.
# GNU find -printf '%f\0' emits names relative to SOURCE.
(
  cd "$SOURCE"
  find . -maxdepth 1 -type f -name "$PATTERN" -printf '%P\0' |
    LC_ALL=C sort -z > "$WORK/source.nul"
)
SOURCE_COUNT="$(tr -cd '\0' < "$WORK/source.nul" | wc -c)"
echo "Source files: $SOURCE_COUNT"
(( SOURCE_COUNT > 0 )) || { echo "No files selected"; exit 1; }

# Archive only the exact manifest; no directory entries or absolute paths.
tar -C "$SOURCE" --null -T "$WORK/source.nul" -czf "$WORK/$ARCHIVE_NAME"
gzip -t "$WORK/$ARCHIVE_NAME"
tar -tzf "$WORK/$ARCHIVE_NAME" > /dev/null

# Compare the actual archive member names with the source manifest.
# GNU tar --null is not a null-output listing option: use a newline listing
# only after explicitly rejecting source names containing newline characters.
if LC_ALL=C tr '\0' '\n' < "$WORK/source.nul" | grep -q $'\r'; then
  echo "Unexpected carriage return in filename; manual review required"; exit 1
fi
if LC_ALL=C tr '\0' '\n' < "$WORK/source.nul" | wc -l | grep -qx "$SOURCE_COUNT"; then
  :
else
  echo "Newline in filename or manifest mismatch; stop"; exit 1
fi
LC_ALL=C tr '\0' '\n' < "$WORK/source.nul" | LC_ALL=C sort > "$WORK/expected.txt"
tar -tzf "$WORK/$ARCHIVE_NAME" | LC_ALL=C sort > "$WORK/actual.txt"
ARCHIVE_COUNT="$(wc -l < "$WORK/actual.txt")"
echo "Archive entries: $ARCHIVE_COUNT"
[[ "$SOURCE_COUNT" -eq "$ARCHIVE_COUNT" ]] || { echo "Entry count mismatch"; exit 1; }
cmp -s "$WORK/expected.txt" "$WORK/actual.txt" || { echo "Archive member mismatch"; exit 1; }

# Transfer without overwriting an existing archive.
cp -n -- "$WORK/$ARCHIVE_NAME" "$DEST/$ARCHIVE_NAME"
[[ -f "$DEST/$ARCHIVE_NAME" ]] || { echo "Destination missing"; exit 1; }
gzip -t "$DEST/$ARCHIVE_NAME"
tar -tzf "$DEST/$ARCHIVE_NAME" | LC_ALL=C sort > "$WORK/destination.txt"
cmp -s "$WORK/expected.txt" "$WORK/destination.txt" || { echo "Destination member mismatch"; exit 1; }
[[ "$(wc -l < "$WORK/destination.txt")" -eq "$SOURCE_COUNT" ]] || exit 1
[[ "$(sha256sum "$WORK/$ARCHIVE_NAME" | awk '{print $1}')" == "$(sha256sum "$DEST/$ARCHIVE_NAME" | awk '{print $1}')" ]] || { echo "Checksum mismatch"; exit 1; }

echo "PASS: $SOURCE_COUNT source files, $ARCHIVE_COUNT archive entries; destination verified."
echo "No source files were deleted."
```

**Operational note:** The example is intended for conventional log filenames. If filenames contain newlines, use a separate null-safe tar member listing/manifest strategy; do not weaken the comparison. If `cp -n` encounters a pre-existing destination because of a race, its behavior can vary by platform. For concurrent workflows, use an exclusive destination creation mechanism.

## Acceptance criteria

1. Source file count recorded before archiving.
2. Archive passes `gzip -t` and `tar -tzf`.
3. Archive member count equals the source count.
4. Archive member names exactly match the source manifest.
5. Destination passes the same checks and checksum comparison.
6. Original source files remain intact.

## Failure handling

On any failure, **retain all source logs**, stop further action, and investigate changed files, log rotation, partial transfer, unusual filenames, insufficient storage, or permission issues. Do not remove originals without a separately approved retention operation.

*Independently authored reference procedure. Never substitute unreviewed production paths into a public example.*
