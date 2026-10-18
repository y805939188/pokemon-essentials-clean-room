#!/usr/bin/env python3
"""Capture read-only command I/O, then emit the exact captured stdout/stderr."""
import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

base = pathlib.Path(__file__).resolve().parent
label, cwd, *command = sys.argv[1:]
prefix = base / "read-io" / label
if prefix.with_suffix(".json").exists():
    raise SystemExit("Refusing to replace prior execution evidence")
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
result = subprocess.run(command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ended = datetime.datetime.now(datetime.timezone.utc).isoformat()
prefix.with_suffix(".stdout").write_bytes(result.stdout)
prefix.with_suffix(".stderr").write_bytes(result.stderr)
metadata = {"schema":"reference-metadata-read-io/v1", "label":label,
    "started_utc":started,"ended_utc":ended,"cwd":cwd,"argv":command,
    "exit_code":result.returncode,"stdout_bytes":len(result.stdout),
    "stderr_bytes":len(result.stderr),
    "stdout_sha256":hashlib.sha256(result.stdout).hexdigest(),
    "stderr_sha256":hashlib.sha256(result.stderr).hexdigest(),
    "evidence_level":"TOOL_VALIDATION"}
prefix.with_suffix(".json").write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+"\n")
sys.stdout.buffer.write(result.stdout)
sys.stderr.buffer.write(result.stderr)
raise SystemExit(result.returncode)
