"""Recompute ref/protection and locator facts only; no semantic acceptance.

Loads fixed JSON and document bytes. It never executes routing.py, any old
guard/main function, candidate source, Ruby, game or reference program. The
heading convention is reproduced from the inspected pure routing locator
functions; this is declared-inventory recoverability, not a web renderer claim.
Only new final-ultra/r1 evidence is written.
"""
from collections import Counter, defaultdict
from datetime import datetime, timezone
import ast
import gzip
import hashlib
import json
from pathlib import Path
import re
import subprocess
import traceback
import unicodedata

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / ".git").exists())
P = "review/remediation-eighth-20261016-prepare/"
INV = "planning/implementation-routing/r8-20261017/"
FORMAL = "deliverables/final-specification-set/"
A = "fd414a2c6ec0a0f746b48e0924e5692221ea5d5a"
B = "8ab43a609e60430492b219f0dce14ef4fdb8e47f"
BASE = "4575e80d041ab0c74a42e2e36399d05791dbaa5b"
ALLOWED = str(HERE.relative_to(REPO)) + "/"
commands = []
loaded = {}
trees = {}
data_cache = {}
parse_cache = {}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def git(*args):
    begin = now()
    proc = subprocess.run(["git", *args], cwd=REPO, capture_output=True, check=False)
    row = {"argv": ["git", *args], "cwd": str(REPO), "started_utc": begin,
           "finished_utc": now(), "exit_code": proc.returncode,
           "stdout_bytes": len(proc.stdout), "stdout_sha256": sha(proc.stdout),
           "stderr_utf8": proc.stderr.decode(errors="replace")}
    if len(proc.stdout) <= 8192:
        row["stdout_utf8"] = proc.stdout.decode(errors="replace")
    commands.append(row)
    if proc.returncode:
        raise RuntimeError(row)
    return proc.stdout


def data(commit, path):
    key = (commit, path)
    if key not in data_cache:
        data_cache[key] = git("show", commit + ":" + path)
    return data_cache[key]


def tree(commit, path):
    key = (commit, path)
    if key not in trees:
        result = {}
        for line in git("ls-tree", "-r", commit, "--", path).decode().splitlines():
            header, name = line.split("\t", 1)
            result[name] = header.split()
        trees[key] = result
    return trees[key]


def identity(commit, path):
    raw = data(commit, path)
    entry = tree(commit, path)[path]
    return {"commit": commit, "path": path, "mode": entry[0], "blob": entry[2],
            "bytes": len(raw), "sha256": sha(raw), "git_blob": entry[2]}


def load(path, commit=A):
    raw = data(commit, path)
    value = json.loads(raw)
    loaded[path] = {"identity": identity(commit, path), "complete_JSON_parse": True,
                    "top_keys": list(value) if isinstance(value, dict) else None,
                    "worktree_full_bytes_equal": (REPO / path).read_bytes() == raw}
    return value


def check(rows, name, value, evidence, boundary):
    rows.append({"name": name, "matched": bool(value), "evidence": evidence,
                 "semantic_boundary": boundary})


def slug(title):
    text = re.sub(r"<[^>]*>", "", title)
    text = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", text).lower()
    return "".join(c for c in text if c in " -_" or unicodedata.category(c)[0] in "LN").replace(" ", "-")


def headings(commit, path):
    key = (commit, path)
    if key in parse_cache:
        return parse_cache[key]
    lines = data(commit, path).decode().splitlines(keepends=True)
    result, used, fence = [], Counter(), None
    for number, line in enumerate(lines, 1):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            char = marker.group(1)[0]
            fence = char if fence is None else None if fence == char else fence
            continue
        if fence:
            continue
        match = re.match(r"^(#{1,6})[ \t]+(.+?)[ \t]*\n?$", line)
        if not match:
            continue
        title = re.sub(r"[ \t]+#+[ \t]*$", "", match.group(2))
        base = slug(title)
        anchor = base + ("-" + str(used[base]) if used[base] else "")
        used[base] += 1
        result.append({"level": len(match.group(1)), "title": title, "anchor": anchor,
                       "line_start": number, "heading_sha256": sha(line.encode())})
    for index, row in enumerate(result):
        row["line_end"] = next((other["line_start"] - 1 for other in result[index + 1:]
                                if other["level"] <= row["level"]), len(lines))
    parse_cache[key] = (result, lines)
    return result, lines


def locator(commit, path, declared, purpose):
    hs, lines = headings(commit, path)
    selected = next((h for h in hs if h["anchor"] == declared["anchor"]), None)
    fields = {"heading_exists": selected is not None,
              "heading_title": selected is not None and selected["title"] == declared["heading"],
              "heading_level": selected is not None and selected["level"] == declared["heading_level"],
              "heading_hash": selected is not None and selected["heading_sha256"] == declared["heading_sha256"]}
    ranges = declared["line_ranges"]
    fields["ranges_inside_heading"] = selected is not None and bool(ranges) and all(
        selected["line_start"] <= first <= last <= selected["line_end"] for first, last in ranges)
    unit = "".join("".join(lines[first - 1:last]) for first, last in ranges).encode()
    ident = identity(commit, path)
    fields.update(unit_hash=sha(unit) == declared["unit_sha256"],
                  file_hash=ident["sha256"] == declared["file_sha256"],
                  file_blob=ident["blob"] == declared["file_git_blob"])
    return {"commit": commit, "path": path, "purpose": purpose, "anchor": declared["anchor"],
            "line_ranges": ranges, "unit_bytes": len(unit), "unit_sha256": sha(unit),
            "observed_heading": selected, "checks": fields, "matched": all(fields.values())}


def current_view(current, historical):
    old_counts, counts = Counter(), {}
    for row in historical["sections"]:
        old_counts[row["document_id"]] += 1
    for row in current["sections"]:
        counts.setdefault(row["document_id"], {"path": row["path"], "headings": 0,
                                               "events": row["accepted_events"]})["headings"] += 1
    lines = ["# 当前源章节覆盖", "",
             "此表由 current-section-coverage.json 生成；历史源定位完整保留在 section-coverage.json。章节导航与源规格接受不证明未来去向兼容、阶段批准或实现验收。", "",
             f"当前固定快照：`{current['snapshot']['commit']}`；当前标题 {len(current['sections'])}；历史标题 {len(historical['sections'])}。", "",
             "| 文档 | 历史标题 | 当前标题 | 新增标题 | 源接受事件 |", "| --- | --- | --- | --- | --- |"]
    for did, row in counts.items():
        lines.append("| " + " | ".join([row["path"], str(old_counts[did]), str(row["headings"]),
                                           str(row["headings"] - old_counts[did]),
                                           ", ".join(row["events"]) or "源字节未变；无新增接受事件"]) + " |")
    return ("\n".join(lines) + "\n").encode()


def run():
    started = now()
    m = load(P + "final/independent-review-input.json", B)
    protection = load(m["protection_baseline_path"])
    validation = load(m["integration_checks"]["path"])
    source_ids = load(P + "integration/tagging-final-7ed3e05/source-file-identities.json")
    routing = load(INV + "routing-manifest.json")
    coverage = load(INV + "current-section-coverage.json")
    historical = load(INV + "section-coverage.json")
    new_mappings = load(INV + "revisions/r3/new-heading-mappings.json")
    wp = json.loads(data(BASE, routing["source_baseline"]["wp_index"]["path"]))
    valid_wp = {r["wp"] for r in wp["rows"]}
    head = git("rev-parse", "HEAD").decode().strip()
    branch = git("branch", "--show-current").decode().strip()
    git("merge-base", "--is-ancestor", B, head)
    protected_checks, location_checks = [], []
    tag = "refs/tags/" + protection["protected_tag"]["name"]
    old_refs_path = P + "cleanup-preflight/snapshot-20261017-162220Z/raw/remote-refs.start.tsv"
    old_refs = {line.split()[1]: line.split()[0] for line in data(A, old_refs_path).decode().splitlines() if line.strip()}
    expected_tag = old_refs.get(tag)
    remote = git("ls-remote", "origin", "refs/heads/main", tag, tag + "^{}").decode()
    remote_refs = {line.split()[1]: line.split()[0] for line in remote.splitlines()}
    local = git("for-each-ref", "--format=%(refname) %(objectname)", "refs/heads/main", "refs/remotes/origin/main", tag).decode()
    local_refs = dict(line.split() for line in local.splitlines())
    check(protected_checks, "current remote main and protected tag retain exact preflight refs",
          remote_refs.get("refs/heads/main") == m["historical_main_commit"] and expected_tag is not None
          and remote_refs.get(tag) == expected_tag,
          {"remote": remote_refs, "protected_tag_preflight_identity": identity(A, old_refs_path), "expected_tag_oid": expected_tag},
          "Present-time ref equality only; no merge/cleanup authorization or historical-operation reconstruction.")
    check(protected_checks, "local protected tag/main are unmodified when present",
          (tag not in local_refs or local_refs[tag] == expected_tag)
          and ("refs/heads/main" not in local_refs or local_refs["refs/heads/main"] == m["historical_main_commit"]),
          {"local_refs": local_refs, "absent_local_tag_permitted_by_baseline": protection["protected_tag"]["local_ref_state"]},
          "No missing ref is fabricated, created or moved by this verification.")
    reference = protection["reference"]
    reference_head = git("-C", reference["path"], "rev-parse", "HEAD").decode().strip()
    reference_tree = git("-C", reference["path"], "rev-parse", reference["commit"] + "^{tree}").decode().strip()
    reference_status = git("-C", reference["path"], "status", "--porcelain", "--untracked-files=all").decode()
    check(protected_checks, "separate fixed reference HEAD tree and worktree retain recorded identity",
          reference_head == reference["commit"] and reference_tree == reference["tree"] and not reference_status,
          {"head": reference_head, "tree": reference_tree, "status": reference_status},
          "No reference program, Ruby, host or framework behavior is run.")
    protected_review = protection["original_review_subtree"]
    review_trees = {label: git("rev-parse", commit + ":" + protected_review["path"]).decode().strip()
                    for label, commit in [("baseline", BASE), ("artifact", A), ("binding", B), ("head", head)]}
    review_work_diff = git("diff", "--name-status", A, "--", protected_review["path"]).decode()
    check(protected_checks, "original global review subtree remains identical",
          all(value == protected_review["tree"] for value in review_trees.values()) and not review_work_diff,
          {"trees": review_trees, "worktree_diff": review_work_diff}, "Preserves fixed history without reopening its semantics.")
    formal_trees = {label: git("rev-parse", commit + ":" + FORMAL.rstrip("/")).decode().strip()
                    for label, commit in [("prepared", m["prepared_formal_source_commit"]), ("artifact", A), ("binding", B), ("head", head)]}
    formal_diff = git("diff", "--name-status", A, "--", FORMAL).decode()
    check(protected_checks, "131 formal tree remains exact prepared artifact binding HEAD and worktree",
          all(value == m["formal_current_tree"] for value in formal_trees.values()) and not formal_diff
          and len(tree(A, FORMAL)) == 131,
          {"trees": formal_trees, "worktree_diff": formal_diff, "formal_count": len(tree(A, FORMAL))},
          "Tree identity is not a new full semantic review of 131 documents.")
    scope_rows = git("diff", "--name-status", B).decode().splitlines()
    untracked = git("ls-files", "--others", "--exclude-standard").decode().splitlines()
    scope_paths = [p for row in scope_rows for p in row.split("\t")[1:]]
    check(protected_checks, "all current tracked and untracked review changes are only final-ultra r1",
          all(path.startswith(ALLOWED) for path in scope_paths + untracked),
          {"tracked_name_status": scope_rows, "untracked_paths": untracked, "head": head, "branch": branch},
          "No candidate/formal/registration/old-evidence change is authorized by this helper.")
    previous_raw = gzip.decompress((HERE / "final-mechanical.json.gz").read_bytes())
    previous = json.loads(previous_raw)
    reused = {"logical_path": ALLOWED + "final-mechanical.json", "plain_bytes": len(previous_raw), "plain_sha256": sha(previous_raw),
              "pointers": ["/payload_1008", "/tagging_175_and_review_75_plus111", "/nine_batch_source_groups"],
              "original_all_mechanical_assertions_pass": previous["all_mechanical_assertions_pass"],
              "qualification": "Original complete byte proof reused only as mechanical evidence, never semantic/FULL credit."}
    check(protected_checks, "integration validation and source identity groups correspond to existing full byte proof",
          len(source_ids["files"]) == 361 and sorted(group["files"] for group in source_ids["groups"]) == [75, 111, 175]
          and validation["formal_current_tree"] == m["formal_current_tree"]
          and validation["exact_imported_candidate_files"] == 175 and validation["exact_imported_current_review_files"] == 75
          and validation["exact_imported_prior_R3_FAIL_files"] == 111 and previous["all_mechanical_assertions_pass"],
          {"validation": loaded[m["integration_checks"]["path"]], "source_groups": source_ids["groups"], "reused": reused},
          "Prior source/review verdicts remain with original reviewers; no new independent vote or actual acceptance.")

    docs = {row["document_id"]: row for row in routing["documents"]}
    active = {row["feature_id"]: row for row in routing["features"]}
    retired = {row["feature_id"]: row for row in routing["retired_features"]}
    meta = {row["metadata_id"]: row for row in routing["metadata_records"]}
    decision_ids = {row["id"] for row in routing["decisions"]}
    prototype_ids = {row["id"] for row in routing["prototypes"]}
    document_rows, historical_locators, current_locators, references = [], [], [], []
    occupied = defaultdict(set)
    for index, doc in enumerate(routing["documents"]):
        source = doc["source"]
        old = identity(source["commit"], source["path"])
        current = doc["current_applicability"]
        new = identity(current["snapshot_commit"], current["path"])
        actual = identity(A, current["path"])
        same = all(old[k] == source[k] for k in ["bytes", "sha256", "git_blob"])
        same = same and all(new[k] == current["identity"][k] for k in ["commit", "path", "bytes", "sha256", "git_blob"])
        same = same and all(new[k] == actual[k] for k in ["bytes", "sha256", "blob"])
        same = same and set(doc["feature_ids"]) == {fid for fid, row in active.items() if row["document_id"] == doc["document_id"]}
        same = same and set(doc.get("retired_feature_ids", [])) == {fid for fid, row in retired.items() if row["document_id"] == doc["document_id"]}
        same = same and not ((set(doc["wp_refs"]) | set(doc["dependency_wp_refs"])) - valid_wp)
        document_rows.append({"pointer": "/documents/" + str(index), "document_id": doc["document_id"],
                              "source": old, "current": new, "artifact": actual, "matched": same})
    for group, rows in [("features", routing["features"]), ("retired_features", routing["retired_features"]), ("metadata_records", routing["metadata_records"])]:
        for index, row in enumerate(rows):
            rid = row.get("feature_id", row.get("metadata_id"))
            where = "/" + group + "/" + str(index)
            source = row["source"]
            result = locator(source["commit"], source["document"], source, "declared immutable historical source")
            result.update(pointer=where + "/source", record_id=rid, group=group)
            historical_locators.append(result)
            doc = docs.get(row["document_id"])
            refchecks = {"document_id": doc is not None and source["document"] == doc["source"]["path"]}
            deps = row.get("dependencies", {})
            refchecks["feature_refs"] = not (set(deps.get("feature_refs", [])) - (set(active) if group == "features" else set(active) | set(retired)))
            refchecks["wp_refs"] = not ((set(deps.get("wp_refs", [])) | set(deps.get("document_wp_refs", []))) - valid_wp)
            refchecks["decision_refs"] = not (set(row.get("decision_refs", [])) - decision_ids)
            refchecks["prototype_refs"] = not (set(row.get("future_plan", {}).get("prototype_refs", [])) - prototype_ids)
            direct_refs = []
            for dep in deps.get("direct_refs", []):
                old_h = headings(source["commit"], dep["document"])[0]
                new_h = headings(A, dep["document"])[0]
                direct_refs.append({"document": dep["document"], "anchor": dep["anchor"],
                                    "historical_anchor_exists": dep["anchor"] in {h["anchor"] for h in old_h},
                                    "current_anchor_exists": dep["anchor"] in {h["anchor"] for h in new_h}})
            refchecks["direct_refs"] = all(x["historical_anchor_exists"] and x["current_anchor_exists"] for x in direct_refs)
            if group == "features":
                current = row["current_applicability"]
                current_result = locator(current["snapshot_commit"], current["document"], current["locator"], "declared current source at final byte-identical formal snapshot")
                current_result.update(pointer=where + "/current_applicability/locator", record_id=rid)
                current_result["snapshot_and_doc_role_match"] = current["snapshot_commit"] == routing["current_snapshot"]["commit"] == doc["current_applicability"]["snapshot_commit"] and current["document"] == doc["current_applicability"]["path"]
                nums = {n for first, last in current["locator"]["line_ranges"] for n in range(first, last + 1)}
                key = current["document"]
                current_result["range_does_not_overlap_other_current_feature_units"] = not occupied[key].intersection(nums)
                occupied[key].update(nums)
                current_result["matched"] = current_result["matched"] and current_result["snapshot_and_doc_role_match"] and current_result["range_does_not_overlap_other_current_feature_units"]
                current_locators.append(current_result)
                refchecks["excluded_child_refs"] = all(fid in active and fid != rid and active[fid]["document_id"] == row["document_id"] for fid in row["functional_scope"]["excluded_child_refs"])
            elif group == "retired_features":
                retirement = row["retirement"]
                refchecks["retirement_metadata"] = retirement["metadata_record_id"] in meta
                refchecks["replacement_feature_refs"] = not (set(retirement["replacement_feature_refs"]) - set(active))
            else:
                refchecks["metadata_feature_refs"] = not (set(row["feature_refs"]) - set(active))
                refchecks["metadata_retired_refs"] = not (set(row["retired_feature_ids"]) - set(retired))
            references.append({"pointer": where, "record_id": rid, "group": group, "checks": refchecks,
                               "direct_refs": direct_refs, "matched": all(refchecks.values())})
    expected_sections = []
    fields = ["document_id", "path", "level", "title", "anchor", "line_start", "line_end", "heading_sha256"]
    for doc in routing["documents"]:
        for h in headings(A, doc["current_applicability"]["path"])[0]:
            expected_sections.append({"document_id": doc["document_id"], "path": doc["current_applicability"]["path"], **h})
    actual_fields = [{k: row[k] for k in fields} for row in coverage["sections"]]
    expected_fields = [{k: row[k] for k in fields} for row in expected_sections]
    section_rows = []
    for index, section in enumerate(coverage["sections"]):
        doc = docs[section["document_id"]]
        flags = {"exact_heading_fields_and_order": index < len(expected_fields) and actual_fields[index] == expected_fields[index],
                 "feature_refs_resolved": not (set(section["feature_refs"]) - set(active)),
                 "metadata_refs_resolved": not (set(section["metadata_refs"]) - set(meta)),
                 "accepted_event_list_equals_document": section["accepted_events"] == doc["upstream"]["accepted_events"]}
        section_rows.append({"pointer": "/sections/" + str(index), **actual_fields[index], "checks": flags, "matched": all(flags.values())})
    old_keys = {(row["path"], row["anchor"]) for row in historical["sections"]}
    new_sections = [row for row in coverage["sections"] if (row["path"], row["anchor"]) not in old_keys]
    new_rows = []
    for index, mapping in enumerate(new_mappings["accepted_mappings"]):
        path = mapping["document"]
        hs, lines = headings(A, path)
        h = next(x for x in hs if x["anchor"] == mapping["anchor"])
        unit = "".join(lines[h["line_start"] - 1:h["line_end"]]).encode()
        declared = mapping["source_identity"]
        ident = identity(A, path)
        flags = {"title_heading_hash_convention": declared["heading_sha256"] == sha(h["title"].encode()),
                 "raw_heading_hash": declared["raw_markdown_heading_sha256"] == h["heading_sha256"],
                 "exact_ranges": declared["line_ranges"] == [[h["line_start"], h["line_end"]]],
                 "unit_hash": declared["unit_sha256"] == sha(unit),
                 "file_identity": declared["file_sha256"] == ident["sha256"] and declared["file_git_blob"] == ident["blob"] and declared["file_bytes"] == ident["bytes"],
                 "consumer_ids": not (set(mapping["feature_refs"]) - set(active)) and not (set(mapping["metadata_refs"]) - set(meta)),
                 "consumer_fixed_fields": all(item["feature_id"] in active and all(item["source"][k] == active[item["feature_id"]]["source"][k] for k in ["commit", "document", "anchor", "line_ranges"]) for item in mapping["consumer_fixed_sources"])}
        new_rows.append({"pointer": "/accepted_mappings/" + str(index), "document": path, "anchor": h["anchor"], "checks": flags, "matched": all(flags.values())})
    check(location_checks, "131 document declared baseline/current identities and memberships recover exactly",
          len(document_rows) == 131 and all(row["matched"] for row in document_rows), {"documents": len(document_rows)},
          "Document identity and declared membership only; no classification correctness judgment.")
    check(location_checks, "all 736 active 33 retired and 33 metadata historical locators recover",
          len(historical_locators) == 802 and all(row["matched"] for row in historical_locators), {"counts": dict(Counter(row["group"] for row in historical_locators))},
          "Retired and metadata original sources remain historical; no forced current-purpose or semantic transfer.")
    check(location_checks, "all 736 current active locators recover exact current paths anchors ranges and unit bytes",
          len(current_locators) == 736 and all(row["matched"] for row in current_locators), {"current_active_locators": len(current_locators)},
          "Recoverable bytes and nonoverlap do not establish the labels or dependency meanings.")
    check(location_checks, "all declared ID and direct heading references recover",
          len(references) == 802 and all(row["matched"] for row in references), {"records": len(references), "direct_reference_occurrences": sum(len(row["direct_refs"]) for row in references)},
          "Reference existence is not behavioral compatibility or semantic completeness.")
    check(location_checks, "2704 current sections exactly match recomputed formal headings in order",
          len(section_rows) == len(expected_sections) == 2704 and actual_fields == expected_fields and all(row["matched"] for row in section_rows),
          {"declared": len(section_rows), "recomputed": len(expected_sections), "historical": len(historical["sections"]), "new_current": len(new_sections)},
          "This is the repository's declared heading convention, not a live GitHub renderer assertion.")
    check(location_checks, "21 explicit new-heading evidence entries match current bytes and exact consumer source fields",
          len(new_sections) == len(new_rows) == 21 and all(row["matched"] for row in new_rows)
          and {(row["path"], row["anchor"]) for row in new_sections} == {(row["document"], row["anchor"]) for row in new_rows},
          {"new_current_sections": len(new_sections), "explicit_mapping_count": len(new_rows)},
          "Same source fields and resolved consumer IDs do not verify the consumer assignment's meaning.")
    rendered = current_view(coverage, historical)
    view_raw = data(A, INV + "current-coverage.md")
    check(location_checks, "current readable coverage view is an exact in-memory rendering of current rows",
          rendered == view_raw, {"render_bytes": len(rendered), "render_sha256": sha(rendered), "actual_sha256": sha(view_raw)},
          "Rendering freshness only; no old B8-only scope guard or source program main is run.")
    scripts = []
    for path in [INV + "routing.py", INV + "revisions/r3/tools/current-coverage-check.py", INV + "revisions/r3/tools/accepted-binding-regressions.py", INV + "revisions/r3/tools/final-calibration-proof.py"]:
        script = data(A, path)
        parsed = ast.parse(script.decode(), filename=path)
        scripts.append({"identity": identity(A, path), "complete_bytes_and_AST_read": True,
                        "function_definitions": [{"name": node.name, "line": node.lineno, "end_line": node.end_lineno} for node in ast.walk(parsed) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))],
                        "executed": False})
    end_head = git("rev-parse", "HEAD").decode().strip()
    check(protected_checks, "HEAD unchanged during bounded fact verification", head == end_head,
          {"start_head": head, "end_head": end_head}, "No commit push checkout or ref mutation is performed.")
    common = {"started_utc": started, "finished_utc": now(), "artifact": A, "binding": B,
              "qualification": "MECHANICAL_FACTS_ONLY; no semantic/FULL/configuration/acceptance credit or new global tagging review.",
              "business_execution": "NOT_EXECUTED", "script_identity": {"path": str(Path(__file__).relative_to(REPO)), "bytes": Path(__file__).stat().st_size, "sha256": sha(Path(__file__).read_bytes())}}
    protect_out = {**common, "schema": "r8-final-protection-live-ref-facts/v1", "checks": protected_checks,
                   "all_mechanical_comparisons_matched": all(row["matched"] for row in protected_checks),
                   "complete_bound_inputs": loaded, "reused_complete_byte_evidence": reused, "commands": commands}
    locator_out = {**common, "schema": "r8-final-current-locator-recoverability-facts/v1", "checks": location_checks,
                   "all_mechanical_comparisons_matched": all(row["matched"] for row in location_checks),
                   "documents": document_rows, "historical_locators_802": historical_locators,
                   "current_active_locators_736": current_locators, "reference_records_802": references,
                   "current_sections_2704": section_rows, "new_heading_mappings_21": new_rows,
                   "inspected_original_scripts_not_executed": scripts,
                   "semantic_exclusions": ["No plan/destination/classification/dependency semantic verdict", "No source game/Ruby/native/host run", "No B8 author-only diff confinement guard", "No semantic FULL or original reviewer/context/model credit transfer"]}
    for name, value in [("final-protection-facts.json", protect_out), ("final-current-locator-facts.json", locator_out)]:
        output = HERE / name
        output.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({"path": str(output.relative_to(REPO)), "bytes": output.stat().st_size,
                          "sha256": sha(output.read_bytes()), "all_mechanical_comparisons_matched": value["all_mechanical_comparisons_matched"],
                          "check_count": len(value["checks"])}, ensure_ascii=False))
    if not protect_out["all_mechanical_comparisons_matched"] or not locator_out["all_mechanical_comparisons_matched"]:
        raise SystemExit(1)


if __name__ == "__main__":
    try:
        run()
    except Exception as error:
        failure = {"recorded_utc": now(), "error": str(error), "traceback": traceback.format_exc(), "commands": commands,
                   "qualification": "Mechanical tool failure only; zero semantic/FULL credit."}
        (HERE / "final-protection-locator-failed-attempt.json").write_text(json.dumps(failure, ensure_ascii=False, indent=2) + "\n")
        raise
