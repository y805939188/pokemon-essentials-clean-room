"""Read this helper first. Restore inert evidence bytes only, to a fresh target."""
from pathlib import Path, PurePosixPath
import gzip
import hashlib
import json
import os
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
destination = Path(sys.argv[1]).absolute()
if destination.exists() or destination.is_symlink():
    raise SystemExit("destination must not exist")
if any(p.is_symlink() for p in destination.parents):
    raise SystemExit("destination parents must not be symlinks")
manifest = json.loads((root / "publication/compressed-artifacts.json").read_text())
prepared = []
for row in manifest["artifacts"]:
    rel = PurePosixPath(row["original_path"])
    container = PurePosixPath(row["container_path"])
    if rel.is_absolute() or container.is_absolute() or ".." in rel.parts or ".." in container.parts:
        raise SystemExit("unsafe evidence path")
    source = root.joinpath(*container.parts)
    if source.is_symlink() or any(p.is_symlink() for p in source.parents if p != root.parent):
        raise SystemExit("symlink input prohibited")
    packed = source.read_bytes()
    assert len(packed) == row["container_bytes"]
    assert hashlib.sha256(packed).hexdigest() == row["container_sha256"]
    assert len(packed) < 100000000 and row["original_bytes"] < 250000000
    raw = gzip.decompress(packed)
    assert len(raw) == row["original_bytes"]
    assert hashlib.sha256(raw).hexdigest() == row["original_sha256"]
    assert subprocess.check_output(["git", "hash-object", "--stdin"], input=raw).decode().strip() == row["original_git_blob"]
    prepared.append((rel, raw))
destination.mkdir(mode=0o700, parents=True)
for rel, raw in prepared:
    target = destination.joinpath(*rel.parts)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("xb") as out:
        out.write(raw)
    os.chmod(target, 0o644)
print(json.dumps({"destination": str(destination), "restored_files": len(prepared),
                  "bytes": sum(len(raw) for _, raw in prepared), "behavior_executed": False,
                  "qualification": "Inert exact evidence bytes restored, no semantic reading credit"}))
