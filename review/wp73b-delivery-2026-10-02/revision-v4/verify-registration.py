#!/usr/bin/env python3
"""第一百十五轮登记复核：TSV 全部行与 manifest §1 全部带哈希行对磁盘 0 偏差、无重复路径。"""
import hashlib, re, sys, json, os

ROOT = "/Users/dingshinn/Desktop/pokemon-framework-reference"
TSV = f"{ROOT}/review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv"
MANIFEST = f"{ROOT}/planning/review-manifest-2026-09-19.md"

def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

errors = []
checked_tsv = 0
checked_manifest = 0

tsv_paths = {}
with open(TSV, encoding="utf-8") as f:
    for lineno, line in enumerate(f, 1):
        line = line.rstrip("\n")
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) != 3:
            errors.append(f"TSV line {lineno}: bad column count {len(parts)}")
            continue
        h, b, p = parts
        if p in tsv_paths:
            errors.append(f"TSV line {lineno}: duplicate path {p} (first at {tsv_paths[p]})")
        tsv_paths[p] = lineno
        try:
            actual_h = sha256_of(f"{ROOT}/{p}")
            actual_b = os.path.getsize(f"{ROOT}/{p}")
        except OSError as e:
            errors.append(f"TSV line {lineno}: {p}: unreadable: {e}")
            continue
        if actual_h != h or actual_b != int(b):
            errors.append(f"TSV line {lineno}: {p}: registered {h}/{b} != disk {actual_h}/{actual_b}")
        checked_tsv += 1

with open(MANIFEST, encoding="utf-8") as f:
    text = f.read()
sec1 = text.split("## 1.", 1)[1].split("## 2.", 1)[0]
manifest_paths = {}
row_re = re.compile(r"^\| `([^`]+)`(?:（[^|]*）)? \| `[0-9a-f]{8}` \| `([0-9a-f]{64})` \| ([\d,]+) \|$")
for lineno, line in enumerate(sec1.splitlines(), 1):
    m = row_re.match(line.strip())
    if not m:
        continue
    p, h, b = m.group(1), m.group(2), int(m.group(3).replace(",", ""))
    if p in manifest_paths:
        errors.append(f"manifest §1: duplicate path {p}")
    manifest_paths[p] = lineno
    try:
        actual_h = sha256_of(f"{ROOT}/{p}")
        actual_b = os.path.getsize(f"{ROOT}/{p}")
    except OSError as e:
        errors.append(f"manifest §1: {p}: unreadable: {e}")
        continue
    if actual_h != h or actual_b != b:
        errors.append(f"manifest §1: {p}: registered {h}/{b} != disk {actual_h}/{actual_b}")
    checked_manifest += 1

nohash_rows = [l.strip() for l in sec1.splitlines()
               if l.strip().startswith("| `") and not row_re.match(l.strip())
               and not l.strip().startswith("| 文件") and not l.strip().startswith("| ---")]

result = {
    "tsv_rows_checked": checked_tsv,
    "manifest_sec1_hashed_rows_checked": checked_manifest,
    "manifest_sec1_nohash_rows": len(nohash_rows),
    "deviations": errors,
    "zero_deviation": len(errors) == 0,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(0 if not errors else 1)
