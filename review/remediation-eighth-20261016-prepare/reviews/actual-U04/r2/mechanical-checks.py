#!/usr/bin/env python3
"""Fixed-object R8-U04 r2 mechanical evidence; no semantic review vote."""
import collections
import difflib
import hashlib
import html
import json
import pathlib
import posixpath
import re
import subprocess
import unicodedata
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parents[5]
BINDING = "fbc17fc0dbc50c987a21fda4e10ea875d35186de"
SNAPSHOT = "5f87743293290de2e219ecdd6c19e88280f60c9a"
PRE = "e042c2f061eb2951a8d662a5987804e3314cb6b4"
ORIGINAL = "49a558f7d5498680ba88d532f3815e07d7844459"
R1 = "834888e29f939d0a5ed9478d763deb86eb021211"
R = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
B8 = "fd1df570cad987dc3852a3b958f03916e317f7fe"
BASE = "review/remediation-eighth-20261016-prepare/"
FORMAL = "deliverables/final-specification-set/"
INPUT = BASE + "integration/U04-repair-r1/actual-review-input.json"
UI65 = FORMAL + "user-interface/wp65-title-load-options-pause-and-pc.md"
R1_PREFIX = BASE + "reviews/actual-U01-U04-U05-U07-U08-U09/r1/"
OUTPUT = pathlib.Path(__file__).with_name("mechanical-checks.json")
COMMANDS = []
CACHE = {}


def git(*args, repo=ROOT, record=False):
    argv = ["git", "-C", str(repo), *args]
    p = subprocess.run(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if record:
        COMMANDS.append({"argv": argv, "exit_code": p.returncode,
                         "stdout_bytes": len(p.stdout),
                         "stdout_sha256": hashlib.sha256(p.stdout).hexdigest(),
                         "stderr": p.stderr.decode(errors="replace")})
    if p.returncode:
        raise RuntimeError(str(argv) + ": " + p.stderr.decode(errors="replace"))
    return p.stdout


def body(commit, path):
    key = (commit, path)
    if key not in CACHE:
        CACHE[key] = git("show", commit + ":" + path)
    return CACHE[key]


def tree(commit, prefix):
    result = {}
    for row in git("ls-tree", "-r", "-z", commit, "--", prefix).split(b"\0"):
        if row:
            meta, path = row.split(b"\t", 1)
            mode, kind, oid = meta.decode().split()
            result[path.decode()] = {"mode": mode, "type": kind, "blob": oid}
    return result


def identity(commit, path):
    rows = git("ls-tree", "-z", commit, "--", path)
    if not rows:
        return None
    meta, found = rows.rstrip(b"\0").split(b"\t", 1)
    mode, kind, oid = meta.decode().split()
    d = body(commit, path)
    return {"commit": commit, "path": found.decode(), "mode": mode,
            "type": kind, "blob": oid, "bytes": len(d),
            "sha256": hashlib.sha256(d).hexdigest()}


def compare(left, right, path, right_path=None):
    right_path = right_path or path
    a, b = identity(left, path), identity(right, right_path)
    return {"left": a, "right": b,
            "same_mode_and_blob": bool(a and b and a["mode"] == b["mode"] and a["blob"] == b["blob"]),
            "same_full_bytes": bool(a and b and body(left, path) == body(right, right_path))}


def slug(text):
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text).replace("`", "").replace("*", "").replace("~", "").strip().lower()
    return "".join(c for c in text if c in " -_" or unicodedata.category(c)[0] in "LMN").replace(" ", "-")


def anchors(path):
    result, counts = [], collections.Counter()
    for n, line in enumerate(body(SNAPSHOT, path).decode().splitlines(), 1):
        m = re.match(r"^ {0,3}(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if m:
            base = slug(m.group(2))
            suffix = counts[base]
            counts[base] += 1
            result.append({"line": n, "kind": "heading", "title": m.group(2),
                           "anchor": base if not suffix else base + "-" + str(suffix)})
        for a in re.finditer(r"<[A-Za-z][^>]*?\b(?:id|name)\s*=\s*([\"'])(.*?)\1", line, re.I):
            result.append({"line": n, "kind": "explicit_HTML_anchor", "anchor": html.unescape(a.group(2))})
    return result


def main():
    manifest = json.loads(body(BINDING, INPUT))
    batch = manifest["batches"][0]
    out = {"schema": "r8-u04-r2-fixed-object-mechanical-evidence/v1",
           "qualification": "Mechanical comparison only. No business-semantic reading, FULL claim, PASS/FAIL vote, or acceptance registration.",
           "fixed_objects": {"binding": BINDING, "snapshot": SNAPSHOT, "pre_repair": PRE,
                             "original_actual": ORIGINAL, "r1_report_commit": R1, "reference": R, "B8": B8},
           "input_manifest_identity": identity(BINDING, INPUT), "checks": []}

    def check(name, observed, expected):
        out["checks"].append({"name": name, "observed": observed, "expected": expected,
                              "matches": observed == expected})

    check("manifest_snapshot", manifest["artifact_snapshot_commit"], SNAPSHOT)
    check("snapshot_workspace_tree", git("rev-parse", SNAPSHOT + "^{tree}").decode().strip(), manifest["artifact_workspace_tree"])
    check("snapshot_formal_tree", git("rev-parse", SNAPSHOT + ":" + FORMAL.rstrip("/")).decode().strip(), manifest["artifact_formal_tree"])
    out["payload_identity_checks"] = []
    for row in manifest["payload_identities"]:
        actual = identity(row["commit"], row["path"])
        differences = {k: {"declared": row[k], "actual": actual.get(k) if actual else None}
                       for k in ("mode", "blob", "bytes", "sha256")
                       if k in row and (not actual or actual.get(k) != row[k])}
        out["payload_identity_checks"].append({"declared": row, "actual": actual, "differences": differences})
    check("all_payload_identities_match", all(not r["differences"] for r in out["payload_identity_checks"]), True)
    out["seven_target_identity_checks"] = []
    for row in batch["actual_target_identities"]:
        actual = identity(SNAPSHOT, row["path"])
        out["seven_target_identity_checks"].append({"declared": row, "actual": actual,
                                                    "matches_mode_blob_bytes_SHA": all(actual[k] == row[k] for k in ("mode", "blob", "bytes", "sha256"))})
    check("target_count", len(out["seven_target_identity_checks"]), 7)
    check("all_seven_targets_match", all(r["matches_mode_blob_bytes_SHA"] for r in out["seven_target_identity_checks"]), True)
    out["repair_mirror_equality"] = compare(SNAPSHOT, SNAPSHOT, UI65, batch["repair_candidate_mirror"])
    check("UI65_mirror_equal", out["repair_mirror_equality"]["same_mode_and_blob"] and out["repair_mirror_equality"]["same_full_bytes"], True)

    generated = git("diff", "--no-ext-diff", "--no-textconv", "--no-color", "--unified=0", PRE, SNAPSHOT, "--", FORMAL, record=True)
    recorded = body(SNAPSHOT, manifest["full_changed_lines_diff_path"])
    old, new = body(PRE, UI65).splitlines(keepends=True), body(SNAPSHOT, UI65).splitlines(keepends=True)
    changes = [{"line": n, "old": a.decode().rstrip("\n"), "new": b.decode().rstrip("\n")}
               for n, (a, b) in enumerate(zip(old, new), 1) if a != b]
    out["precise_diff"] = {"command": COMMANDS[-1], "recorded_identity": identity(SNAPSHOT, manifest["full_changed_lines_diff_path"]),
                           "strict_full_byte_equal": generated == recorded,
                           "generated_bytes": len(generated), "generated_sha256": hashlib.sha256(generated).hexdigest(),
                           "difference": [] if generated == recorded else list(difflib.unified_diff(recorded.decode().splitlines(), generated.decode().splitlines())),
                           "old_line_count": len(old), "new_line_count": len(new), "changed_line_pairs": changes,
                           "unchanged_line_count": sum(a == b for a, b in zip(old, new))}
    check("precise_patch_equals_fixed_formal_diff_U0", generated == recorded, True)
    check("UI65_old_line_count", len(old), 263)
    check("UI65_new_line_count", len(new), 263)
    check("UI65_only_changed_lines", [r["line"] for r in changes], [152, 210])
    check("UI65_other_unchanged_lines", out["precise_diff"]["unchanged_line_count"], 261)

    before, after = tree(PRE, FORMAL), tree(SNAPSHOT, FORMAL)
    changed = sorted(p for p in set(before) | set(after) if before.get(p) != after.get(p))
    out["formal_protection"] = {"before_count": len(before), "after_count": len(after), "changed_paths": changed,
                                "added_paths": sorted(set(after) - set(before)), "deleted_paths": sorted(set(before) - set(after)),
                                "protected_other_130": [{"path": p, "before": before[p], "after": after.get(p), "same": before[p] == after.get(p)} for p in sorted(before) if p != UI65]}
    check("formal_total", len(after), 131)
    check("formal_changed_only_UI65", changed, [UI65])
    check("formal_no_additions", out["formal_protection"]["added_paths"], [])
    check("formal_no_deletions", out["formal_protection"]["deleted_paths"], [])
    check("other_130_complete_preservation", all(r["same"] for r in out["formal_protection"]["protected_other_130"]), True)
    original_paths = [p for p in batch["actual_target_paths"] if p != UI65]
    out["original_U04_six_files"] = [{"path": p, "original_to_snapshot": compare(ORIGINAL, SNAPSHOT, p), "r1_commit_to_snapshot": compare(R1, SNAPSHOT, p)} for p in original_paths]
    check("all_original_U04_six_equal", all(r[k]["same_full_bytes"] and r[k]["same_mode_and_blob"] for r in out["original_U04_six_files"] for k in ("original_to_snapshot", "r1_commit_to_snapshot")), True)
    r1_before, r1_after = tree(R1, R1_PREFIX), tree(SNAPSHOT, R1_PREFIX)
    out["r1_preservation"] = {"source_count": len(r1_before), "snapshot_count": len(r1_after), "all_files": [compare(R1, SNAPSHOT, p) for p in sorted(r1_before)],
                              "added_paths": sorted(set(r1_after) - set(r1_before)), "deleted_paths": sorted(set(r1_before) - set(r1_after))}
    check("r1_original_file_count", len(r1_before), 19)
    check("r1_whole_tree_unchanged", r1_before, r1_after)
    out["acceptance_receipt_protection"] = [compare(PRE, SNAPSHOT, BASE + "acceptance/" + name + "/receipt.json") for name in ("U01-U05-U07-U08-U09", "U02-U03")]
    check("both_acceptance_receipts_unchanged", all(r["same_full_bytes"] and r["same_mode_and_blob"] for r in out["acceptance_receipt_protection"]), True)

    links = []
    old_links = collections.Counter(re.findall(r"\[[^\]]*\]\(([^)]+)\)", body(PRE, UI65).decode()))
    new_links = collections.Counter(re.findall(r"\[[^\]]*\]\(([^)]+)\)", body(SNAPSHOT, UI65).decode()))
    for url, amount in (new_links - old_links).items():
        u = urllib.parse.urlsplit(url)
        path = posixpath.normpath(posixpath.join(posixpath.dirname(UI65), urllib.parse.unquote(u.path)))
        fragment = urllib.parse.unquote(u.fragment)
        actual = identity(SNAPSHOT, path)
        headings = anchors(path) if actual else []
        links.append({"url": url, "new_occurrences": amount, "target_path": path, "target_identity": actual,
                      "fragment": fragment, "exact_anchor_matches": [r for r in headings if r["anchor"] == fragment], "target_anchor_catalog": headings})
    out["new_local_Markdown_links"] = links
    check("new_link_count", sum(r["new_occurrences"] for r in links), 1)
    check("new_link_target_and_anchor_found", all(r["target_identity"] and (not r["fragment"] or r["exact_anchor_matches"]) for r in links), True)
    out["catalog_preservation"] = []
    id_re = re.compile(r"(?<![A-Za-z0-9])(?:[A-Z][A-Z0-9]*-)+[0-9]+(?:[A-Z][A-Z0-9]*)?(?![A-Za-z0-9])")
    for catalog in (FORMAL + "test-catalog/engine-overworld-wp11-15-59-60.md", FORMAL + "test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md"):
        before_ids = id_re.findall(body(B8, catalog).decode())
        after_ids = id_re.findall(body(SNAPSHOT, catalog).decode())
        out["catalog_preservation"].append({"path": catalog, "pre_to_snapshot": compare(PRE, SNAPSHOT, catalog),
                                            "original_actual_to_snapshot": compare(ORIGINAL, SNAPSHOT, catalog),
                                            "ID_regex": id_re.pattern, "B8_ID_occurrences": before_ids, "snapshot_ID_occurrences": after_ids,
                                            "B8_unique_ID_count": len(set(before_ids)), "snapshot_unique_ID_count": len(set(after_ids)),
                                            "B8_occurrence_count": len(before_ids), "snapshot_occurrence_count": len(after_ids),
                                            "B8_ID_occurrence_order_equal": before_ids == after_ids,
                                            "snapshot_unique_ID_prefix_counts": dict(collections.Counter(r.rsplit("-", 1)[0] for r in set(after_ids)))})
    check("both_catalogs_preserved_exact_bytes", all(r["pre_to_snapshot"]["same_full_bytes"] and r["original_actual_to_snapshot"]["same_full_bytes"] for r in out["catalog_preservation"]), True)
    check("both_catalog_original_ID_occurrences_and_order", all(r["B8_ID_occurrence_order_equal"] for r in out["catalog_preservation"]), True)

    ref = pathlib.Path("/workspace/pokemon-essentials")
    head = git("rev-parse", "HEAD", repo=ref, record=True).decode().strip()
    status = git("status", "--porcelain=v1", "-z", "--untracked-files=all", repo=ref, record=True)
    out["reference"] = {"HEAD": head, "status_entries": [s.decode(errors="replace") for s in status.split(b"\0") if s], "ignored_files_not_audited": True}
    check("reference_HEAD_R", head, R)
    check("reference_tracked_and_untracked_clean", status == b"", True)
    remote = git("ls-remote", "--heads", "origin", "main", record=True).decode().strip()
    out["remote_main_readback"] = remote
    check("remote_main_B8", remote.split()[0] if remote else None, B8)
    out["commands"] = COMMANDS
    out["mechanical_differences"] = [r for r in out["checks"] if not r["matches"]]
    out["business_execution"] = "NOT_EXECUTED"
    out["Ruby_execution"] = "NOT_EXECUTED"
    OUTPUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"payload_count": len(out["payload_identity_checks"]), "mechanical_checks": len(out["checks"]),
                      "mechanical_differences": out["mechanical_differences"], "output_bytes": OUTPUT.stat().st_size,
                      "output_sha256": hashlib.sha256(OUTPUT.read_bytes()).hexdigest()}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
