#!/usr/bin/env python3
"""Archive selected top-level regular files; verify membership, hashes, and destination.

Example (disposable lab):
python3 scripts/archive_verified.py --source ./sample-logs --destination ./archives \
  --pattern '*-2025-*.log' --name logs-2025.tar.gz

Never deletes source files. Requires stable inputs; avoid active log rotation.
"""
import argparse
import fnmatch
import hashlib
import os
from pathlib import Path
import shutil
import sys
import tarfile
import tempfile

def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def members_and_verify(archive, expected):
    with tarfile.open(archive, "r:gz") as tf:
        members = tf.getmembers()
        names = [m.name for m in members]
        if any(not m.isfile() for m in members):
            raise ValueError("Archive contains non-regular entries")
        if len(names) != len(expected) or set(names) != set(expected):
            raise ValueError("Archive membership/count mismatch")
        for m in members:
            h = hashlib.sha256()
            stream = tf.extractfile(m)
            if stream is None:
                raise ValueError("Missing archive member stream")
            with stream:
                for block in iter(lambda: stream.read(1024 * 1024), b""):
                    h.update(block)
            if h.hexdigest() != expected[m.name]:
                raise ValueError("Content mismatch for archive member")

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--destination", type=Path, required=True)
    p.add_argument("--pattern", required=True)
    p.add_argument("--name", required=True)
    a = p.parse_args()
    if Path(a.name).name != a.name or not a.name.endswith(".tar.gz"):
        p.error("--name must be a basename ending .tar.gz")
    src, dest = a.source.resolve(), a.destination.resolve()
    if not src.is_dir() or not dest.is_dir() or src == dest:
        p.error("source and destination must be existing, distinct directories")
    selected = sorted(
        (x for x in src.iterdir()
         if not x.is_symlink() and x.is_file() and fnmatch.fnmatch(x.name, a.pattern)),
        key=lambda x: x.name
    )
    if not selected:
        p.error("no regular files match the selection")
    expected = {x.name: digest(x) for x in selected}
    print(f"Source-file count: {len(expected)}")
    target = dest / a.name
    if target.exists():
        p.error("destination archive already exists; refusing to overwrite")
    with tempfile.TemporaryDirectory(prefix="verified-archive-") as tmp:
        staged = Path(tmp) / a.name
        with tarfile.open(staged, "w:gz", dereference=False) as tf:
            for x in selected:
                if x.is_symlink() or not x.is_file() or digest(x) != expected[x.name]:
                    raise ValueError("source changed before archiving")
                tf.add(x, arcname=x.name, recursive=False)
        members_and_verify(staged, expected)
        print(f"Staged archive entries: {len(expected)} (verified)")
        # Exclusive create prevents overwrite if another process creates the target.
        try:
            with target.open("xb") as out, staged.open("rb") as inp:
                shutil.copyfileobj(inp, out)
        except Exception:
            # Keep the failed destination for investigation; never delete source logs.
            raise
        members_and_verify(target, expected)
        if digest(staged) != digest(target):
            raise ValueError("destination archive checksum mismatch")
    print(f"Destination entries: {len(expected)} (verified)")
    print(f"PASS: {len(expected)} source files == {len(expected)} archive entries")
    print("No source files were deleted.")

if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, tarfile.TarError) as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
