"""Losslessly pack new large completed-task evidence, without altering originals."""
from pathlib import Path
import datetime
import gzip
import hashlib
import json
import subprocess

root = Path(__file__).resolve().parents[1]
repo = root.parents[2]
scope = json.loads((root / "publication/checkpoint-scope.json").read_text())
tracked = set(subprocess.check_output(["git", "-C", str(repo), "ls-files", "-z"]).decode().split("\0"))
outdir = root / "evidence/compressed"
outdir.mkdir(parents=True, exist_ok=True)
rows = []
excluded_caches = []
for name in scope["completed"]:
    for p in sorted((root / "tasks" / name).rglob("*")):
        if not p.is_file() or p.is_symlink():
            continue
        rel = p.relative_to(root)
        if any(s == "object-cache.git" or s.startswith(("recovered-", "readset-materialized-")) or s == "__pycache__" for s in rel.parts[2:-1]):
            excluded_caches.append(str(rel))
            continue
        if str(p.relative_to(repo)) in tracked or p.stat().st_size < 1000000:
            continue
        raw = p.read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        packed = gzip.compress(raw, compresslevel=9, mtime=0)
        assert gzip.decompress(packed) == raw
        target = outdir / (sha + ".gz")
        if target.exists():
            assert target.read_bytes() == packed
        else:
            target.write_bytes(packed)
        blob = subprocess.check_output(["git", "hash-object", "--stdin"], input=raw).decode().strip()
        cblob = subprocess.check_output(["git", "hash-object", "--stdin"], input=packed).decode().strip()
        rows.append({"original_path": str(rel), "original_mode": "100644", "original_bytes": len(raw),
                     "original_sha256": sha, "original_git_blob": blob,
                     "container_path": str(target.relative_to(root)), "container_mode": "100644",
                     "container_bytes": len(packed), "container_sha256": hashlib.sha256(packed).hexdigest(),
                     "container_git_blob": cblob, "codec": "gzip", "roundtrip": "EXACT_BYTES_VERIFIED",
                     "semantic_credit": "NONE; transport only, source original preserved locally"})
manifest = {"schema": "gr8-lossless-large-evidence/v1", "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "artifacts": rows, "count": len(rows), "original_bytes": sum(r["original_bytes"] for r in rows),
            "container_bytes": sum(r["container_bytes"] for r in rows),
            "local_only_reproducible_cache_paths": excluded_caches,
            "cache_qualification": "Exact historical caches and nested bare repository are not new report evidence; current recovery selections/receipts retain original fixed objects. Nothing deleted.",
            "source_originals_modified": False, "update_started": False}
(root / "publication/compressed-artifacts.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({k: manifest[k] for k in ["count", "original_bytes", "container_bytes"]}))
