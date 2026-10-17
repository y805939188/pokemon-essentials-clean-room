#!/usr/bin/env python3
"""Document-only routing inventory. Does not load or execute reference/game code."""
from __future__ import annotations

import argparse
import collections
import copy
import hashlib
import functools
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import shutil
import unicodedata

HERE = Path(__file__).resolve().parent
DATA_HOME = HERE
ROOT = HERE.parents[2]
FORMAL = "deliverables/final-specification-set/"
B8 = "fd1df570cad987dc3852a3b958f03916e317f7fe"
DELIVERY = "4575e80d041ab0c74a42e2e36399d05791dbaa5b"
REPORT = "review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/"
INDEX = REPORT + "tasks/inventory_denominator/formal-inventory.json"
WP_INDEX = REPORT + "coverage/wp-final-coverage.json"
BATCH_INDEX = REPORT + "handoff/batch-assignment.json"
REPO_URL = "https://github.com/y805939188/pokemon-essentials-clean-room/blob/"
INITIAL_CANDIDATE = "d62b41f4d620e50bb04c80a7505374bd284d8210"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, stderr=subprocess.PIPE)


@functools.lru_cache(maxsize=1024)
def blob(commit, path):
    return git("show", f"{commit}:{path}")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


@functools.lru_cache(maxsize=4096)
def identity(commit, path):
    data = blob(commit, path)
    return {"commit": commit, "path": path, "bytes": len(data),
            "sha256": digest(data), "git_blob": git("rev-parse", f"{commit}:{path}").decode().strip()}


def slug(title):
    title = re.sub(r"<[^>]*>", "", title)
    title = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", title).lower()
    title = "".join(c for c in title if c in " -_" or unicodedata.category(c)[0] in "LN")
    return title.replace(" ", "-")


def headings(data):
    lines = data.decode().splitlines(keepends=True)
    out, used, fence = [], collections.Counter(), None
    for i, line in enumerate(lines, 1):
        fm = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if fm:
            mark = fm.group(1)[0]
            if fence is None:
                fence = mark
            elif fence == mark:
                fence = None
            continue
        if fence:
            continue
        m = re.match(r"^(#{1,6})[ \t]+(.+?)[ \t]*\n?$", line)
        if not m:
            continue
        level, title = len(m.group(1)), re.sub(r"[ \t]+#+[ \t]*$", "", m.group(2))
        base = slug(title)
        anchor = base + (f"-{used[base]}" if used[base] else "")
        used[base] += 1
        num = re.match(r"^(\d+(?:\.\d+)*(?:-[A-Z]\d+)?)\.?\s", title)
        out.append({"level": level, "title": title, "anchor": anchor,
                    "section": num.group(1) if num else None, "line_start": i})
    for i, h in enumerate(out):
        h["line_end"] = next((n["line_start"] - 1 for n in out[i + 1:]
                              if n["level"] <= h["level"]), len(lines))
        h["heading_sha256"] = digest(lines[h["line_start"] - 1].encode())
    return out, lines


def excerpt(lines, ranges, size=105):
    for start, end in ranges:
        for line in lines[start - 1:end]:
            line = line.strip()
            if line and not line.startswith(("#", "|", "```", "---", "分类：")):
                return line[:size]
    return "本来源单元以表格或行为数据列出合同；完整内容见固定源定位。"


def subtract_range(start, end, children):
    ranges, cursor = [], start
    for a, b in sorted(children):
        if cursor < a:
            ranges.append([cursor, a - 1])
        cursor = max(cursor, b + 1)
    if cursor <= end:
        ranges.append([cursor, end])
    return ranges


def fixed_inputs():
    index = json.loads(blob(DELIVERY, INDEX))
    wp = json.loads(blob(DELIVERY, WP_INDEX))
    batches = json.loads(blob(DELIVERY, BATCH_INDEX))["batches"]
    indexed = [x["path"] for x in index]
    actual = git("ls-tree", "-r", "--name-only", B8, "--", FORMAL).decode().splitlines()
    actual = [p for p in actual if p.endswith(".md")]
    if sorted(indexed) != sorted(actual) or len(set(indexed)) != len(indexed):
        raise ValueError("Fixed formal index differs from actual formal Markdown tree")
    return index, wp, batches


def doc_bindings(path, wp, batches):
    wps, deps = [], set()
    for row in wp["rows"]:
        if any(path in row.get(k, []) for k in ["formal_payloads", "catalogs", "data_appendix", "shared_formal_payloads"]):
            wps.append(row["wp"])
            deps.update(row.get("dependencies", []))
    affected = [b for b in batches if path in b.get("actual_target_write_set", [])]
    return sorted(wps), sorted(deps), {
        "binding_basis": "DOCUMENT_WRITE_SET_CONSERVATIVE",
        "batches": [b["id"] for b in affected],
        "required_ids": sorted({x for b in affected for x in b["required_ids"]}),
        "status": "待整改后核对" if affected else "固定基线待后继差分核对",
        "authority": {"commit": DELIVERY, "path": BATCH_INDEX},
        "accepted_events": []}


def effective_doc_bindings(path, wp, batches, events):
    """Keep original planned gates; fixed accepted events may add actual receivers."""
    wps, deps, binding = doc_bindings(path, wp, batches)
    actual_batches = {batch for event in events.values() if path in event.get('documents', [])
                      for batch in event.get('batches', [])}
    binding['batches'] = sorted(set(binding['batches']) | actual_batches)
    binding['required_ids'] = sorted(set(binding['required_ids']) | {
        item for batch in batches if batch['id'] in actual_batches for item in batch['required_ids']})
    return wps, deps, binding


def covered_batches(upstream, events):
    return {batch for eid in upstream['accepted_events'] if eid in events
            for batch in events[eid].get('batches', [])}


def seed():
    raise ValueError("Refuse to reseed stable IDs; revise the explicit manifest and retain original source locators")


def integrity_errors(manifest, coverage, accepted_updates=None):
    """Check Git identities and declared relationships, never authenticate semantics."""
    found = []
    baseline, snapshot = manifest["source_baseline"], manifest["current_snapshot"]
    active = {f["feature_id"]: f for f in manifest["features"]}
    if len(active) != len(manifest["features"]):
        found.append("duplicate feature IDs")
    retired_rows = manifest.get("retired_features", [])
    retired = {f["feature_id"]: f for f in retired_rows}
    metadata_rows = manifest.get("metadata_records", [])
    metadata = {r["metadata_id"]: r for r in metadata_rows}
    documents = {d["document_id"]: d for d in manifest["documents"]}
    by_path = {d["source"]["path"]: d for d in manifest["documents"]}
    _, wp, batches = fixed_inputs()
    valid_wp = {r["wp"] for r in wp["rows"]}
    valid_batches = {b["id"]: b for b in batches}

    def fail(message):
        found.append(message)

    def get_identity(commit, path, label):
        try:
            return identity(commit, path)
        except (subprocess.CalledProcessError, ValueError, UnicodeDecodeError):
            fail(label + ": missing Git commit/path")
            return None

    def check_identity(declared, label):
        actual = get_identity(declared["commit"], declared["path"], label)
        if actual is not None and declared != actual:
            fail(label + ": complete Git identity mismatch")
        return actual

    for key, commit in [("source_baseline", baseline["commit"]), ("current_snapshot", snapshot["commit"])]:
        try:
            tree = git("rev-parse", f"{commit}:{FORMAL.rstrip('/')}").decode().strip()
            if manifest[key]["formal_tree"] != tree:
                fail(key + ": formal tree mismatch")
        except subprocess.CalledProcessError:
            fail(key + ": missing formal snapshot")
    if baseline["commit"] != B8 or baseline["delivery_commit"] != DELIVERY:
        fail("immutable baseline/delivery authority changed")
    for key, path in [("index", INDEX), ("wp_index", WP_INDEX)]:
        if baseline[key] != identity(DELIVERY, path):
            fail("source_baseline: " + key + " authority/identity mismatch")
    if coverage.get("schema_version") != "routing-section-coverage.v1" or coverage.get("source_commit") != baseline["commit"]:
        fail("heading coverage baseline/schema mismatch")

    original = json.loads(blob(INITIAL_CANDIDATE, str((DATA_HOME / "routing-manifest.json").relative_to(ROOT))))
    original_rows = {f["feature_id"]: f for f in original["features"]}
    if len(retired) != len(retired_rows) or set(active).intersection(retired):
        fail("duplicate or reused retired feature IDs")
    if set(original_rows) - (set(active) | set(retired)):
        fail("original stable feature IDs must remain active or retired")
    if len(metadata) != len(metadata_rows):
        fail("duplicate metadata record IDs")
    for fid, f in active.items():
        if fid in original_rows and f["source"] != original_rows[fid]["source"]:
            fail(fid + ": original immutable source changed")
    for fid, f in retired.items():
        saved = {k: v for k, v in f.items() if k != "retirement"}
        if fid not in original_rows or saved != original_rows.get(fid):
            fail(fid + ": retired record must preserve complete original row")
        reason = f["retirement"]
        if reason["metadata_record_id"] not in metadata or set(reason["replacement_feature_refs"]) - set(active):
            fail(fid + ": unresolved retirement metadata/replacement")

    accepted_updates = accepted_updates if accepted_updates is not None else read_json(DATA_HOME / "accepted-source-updates.json")
    events = {}
    if not isinstance(accepted_updates, dict) or not isinstance(accepted_updates.get("events"), list):
        return found + ["accepted events: malformed registry"]
    for event in accepted_updates.get("events", []):
        if not isinstance(event, dict):
            fail("accepted events: malformed event")
            continue
        eid = event.get("event_id")
        if not eid or eid in events:
            fail("accepted events: missing/duplicate event ID")
            continue
        events[eid] = event
        if (event.get("status") != "ACCEPTED" or not event.get("documents") or not event.get("batches")
                or not event.get("evidence") or set(event.get("batches", [])) - set(valid_batches)):
            fail(eid + ": accepted event requires exact batch/document/evidence binding")
        commit = event.get("commit", "")
        if not re.fullmatch(r"[0-9a-f]{40}", commit) or commit == "0" * 40:
            fail(eid + ": accepted event requires real commit")
        else:
            try:
                git("cat-file", "-e", commit + "^{commit}")
                git("merge-base", "--is-ancestor", commit, snapshot["commit"])
            except subprocess.CalledProcessError:
                fail(eid + ": accepted event commit not in current snapshot history")
        for evidence in event.get("evidence", []):
            if not isinstance(evidence, dict) or set(evidence) != {"commit", "path"}:
                fail(eid + ": accepted event evidence must name fixed Git commit/path")
            else:
                get_identity(evidence["commit"], evidence["path"], eid + " evidence")
        try:
            receipt_ref = event['evidence'][0]
            receipt = json.loads(blob(receipt_ref['commit'], receipt_ref['path']))
            pointer = event['receipt_record_pointer']
            if not re.fullmatch(r'/records/\d+', pointer):
                raise ValueError('record pointer')
            record = receipt['records'][int(pointer.rsplit('/', 1)[1])]
            identities = record.get('actual_target_identities') or [record['actual_target_identity']]
            if (record.get('ACCEPTED') is not True or record.get('actual_integrated_PASS') is not True
                    or event['commit'] != record['actual_artifact_commit']
                    or event['batches'] != [record['batch']]
                    or set(event['documents']) != {item['path'] for item in identities}):
                raise ValueError('receipt scope')
            for item in identities:
                actual = identity(event['commit'], item['path'])
                if any(actual[key] != item[raw] for key, raw in [('git_blob', 'blob'), ('sha256', 'sha256'), ('bytes', 'bytes')]):
                    raise ValueError('receipt target identity')
        except (KeyError, IndexError, TypeError, ValueError, subprocess.CalledProcessError):
            fail(eid + ': accepted event requires matching fixed ACCEPTED receipt record and target identities')

    def check_upstream(upstream, path, label):
        _, _, expected = effective_doc_bindings(path, wp, batches, events)
        if upstream["authority"] != {"commit": DELIVERY, "path": BATCH_INDEX}:
            fail(label + ": batch authority mismatch")
        if set(upstream["batches"]) - set(valid_batches):
            fail(label + ": unknown R8 batch")
        expected_batches, expected_ids = set(expected["batches"]), set(expected["required_ids"])
        if upstream["binding_basis"] == "DOCUMENT_WRITE_SET_CONSERVATIVE":
            if set(upstream["batches"]) != expected_batches or set(upstream["required_ids"]) != expected_ids:
                fail(label + ": known conservative batch binding mismatch")
        elif (not upstream["accepted_events"] or set(upstream["batches"]) - expected_batches
                or set(upstream["required_ids"]) - expected_ids):
            fail(label + ": section binding requires accepted evidence within fixed authority")
        for eid in upstream["accepted_events"]:
            event = events.get(eid)
            if not event or path not in event.get("documents", []) or not set(event.get("batches", [])).issubset(upstream["batches"]):
                fail(label + ": unresolved or unrelated accepted event")
        if expected_batches - covered_batches(upstream, events) and upstream["status"] != "待整改后核对":
            fail(label + ": unaccepted batch must retain calibration gate")

    parsed = {}
    current_parsed = {}
    current_occupied = collections.defaultdict(set)
    expected_headings = {}
    for did, doc in documents.items():
        path = doc["source"]["path"]
        if check_identity(doc["source"], path + " source") is None:
            continue
        if doc["source"]["commit"] != baseline["commit"]:
            fail(path + ": document source baseline mismatch")
        for key in ["wp_refs", "dependency_wp_refs"]:
            if set(doc[key]) - valid_wp:
                fail(path + ": unknown dependency WP")
        check_upstream(doc["upstream"], path, did)
        declared_retired = set(doc.get("retired_feature_ids", []))
        if declared_retired != {fid for fid, f in retired.items() if f["document_id"] == did}:
            fail(path + ": document retired feature membership mismatch")
        current = doc["current_applicability"]
        if current["path"] != path and not doc["upstream"]["accepted_events"]:
            fail(path + ": renamed applicability requires accepted event")
        expected_current = get_identity(current["snapshot_commit"], current["path"], path + " current")
        if expected_current and current["identity"] != expected_current:
            fail(path + ": current applicability complete identity mismatch")
        if current["identity"]["path"] != current["path"]:
            fail(path + ": current identity path mismatch")
        if current["source_equivalence"] == "SAME_BYTES" and current["identity"]["sha256"] != doc["source"]["sha256"]:
            fail(path + ": false source equivalence")
        if current["identity"]["sha256"] != doc["source"]["sha256"] and not doc["upstream"]["accepted_events"]:
            fail(path + ": changed current source requires accepted calibration")
        hs, lines = headings(blob(doc["source"]["commit"], path))
        parsed[path] = (hs, lines)
        for h in hs:
            expected_headings[(path, h["line_start"])] = {"document_id": did, "path": path,
                **{k: h[k] for k in ["level", "title", "anchor", "line_start", "line_end", "heading_sha256"]}}

    for fid, f in active.items():
        doc = documents.get(f["document_id"])
        if not doc:
            continue
        path = doc["source"]["path"]
        current = f["current_applicability"]
        if current["snapshot_commit"] != snapshot["commit"] or current["snapshot_commit"] != doc["current_applicability"]["snapshot_commit"] or current["document"] != doc["current_applicability"]["path"]:
            fail(fid + ": current feature snapshot/path mismatch")
            continue
        if current["source_classification"] != doc["source_classification"]:
            fail(fid + ": current source classification differs from document")
        locator = current["locator"]
        current_key = (current["snapshot_commit"], current["document"])
        try:
            if current_key not in current_parsed:
                current_parsed[current_key] = headings(blob(*current_key))
        except subprocess.CalledProcessError:
            fail(fid + ": current feature locator missing snapshot/path")
            continue
        current_headings, current_lines = current_parsed[current_key]
        selected = next((h for h in current_headings if h["anchor"] == locator["anchor"]), None)
        if not selected or any(locator[k] != selected[hk] for k,hk in [("heading","title"),("heading_level","level"),("heading_sha256","heading_sha256")]):
            fail(fid + ": current feature locator heading mismatch")
        if selected and any(a < selected["line_start"] or b > selected["line_end"] or a > b for a,b in locator["line_ranges"]):
            fail(fid + ": current feature locator range mismatch")
        for a,b in locator['line_ranges']:
            nums = set(range(a,b+1))
            if current_occupied[current_key].intersection(nums):
                fail(fid + ": current feature locator ranges overlap")
            current_occupied[current_key].update(nums)
        current_unit = ''.join(''.join(current_lines[a-1:b]) for a,b in locator['line_ranges']).encode()
        current_identity = doc['current_applicability']['identity']
        if digest(current_unit) != locator['unit_sha256'] or locator['file_sha256'] != current_identity['sha256'] or locator['file_git_blob'] != current_identity['git_blob']:
            fail(fid + ": current feature locator identity mismatch")
        if current_identity['sha256'] == doc['source']['sha256'] and locator['line_ranges'] != f['functional_scope']['line_ranges']:
            fail(fid + ": unchanged current feature locator range mismatch")
        check_upstream(f["upstream"], path, fid)
        if f["upstream"]["accepted_events"] != doc["upstream"]["accepted_events"]:
            fail(fid + ": feature/document accepted event mismatch")
        if set(f["dependencies"]["wp_refs"] + f["dependencies"]["document_wp_refs"]) - valid_wp:
            fail(fid + ": unknown dependency WP")
        plan = f["future_plan"]
        parties = {r["party"] for r in plan["responsibilities"]}
        if not plan["partners"] or parties != set(plan["partners"]):
            fail(fid + ": nonempty collaborators and responsibilities must agree")
        for dep in f["dependencies"]["direct_refs"]:
            target = parsed.get(dep["document"])
            if not target or dep["anchor"] not in {h["anchor"] for h in target[0]}:
                fail(fid + ": unresolved direct source dependency")
        scope = f["functional_scope"]
        source_lines = {n for a, b in f["source"]["line_ranges"] for n in range(a, b + 1)}
        selected_lines = {n for a, b in scope["line_ranges"] for n in range(a, b + 1)}
        if not selected_lines or selected_lines - source_lines or any(a > b for a, b in scope["line_ranges"]):
            fail(fid + ": invalid current functional scope")
        excluded = set()
        for child_id in scope["excluded_child_refs"]:
            child = active.get(child_id)
            if not child or child_id == fid or child["document_id"] != f["document_id"]:
                fail(fid + ": invalid excluded child reference")
                continue
            child_lines = {n for a, b in child["source"]["line_ranges"] for n in range(a, b + 1)}
            if not child_lines or child_lines - source_lines:
                fail(fid + ": excluded child outside immutable parent source")
            excluded.update(child_lines)
        if source_lines - excluded != selected_lines:
            fail(fid + ": current functional scope does not match excluded children")

    for mid, record in metadata.items():
        doc = documents.get(record["document_id"])
        if not doc or record["source"]["document"] != doc["source"]["path"]:
            fail(mid + ": metadata document mismatch")
            continue
        if set(record["feature_refs"]) - set(active) or set(record["retired_feature_ids"]) - set(retired):
            fail(mid + ": unresolved metadata navigation reference")
        s = record["source"]
        hs, lines = parsed[s["document"]]
        h = next((h for h in hs if h["anchor"] == s["anchor"]), None)
        if not h or h["title"] != s["heading"] or h["level"] != s["heading_level"] or h["heading_sha256"] != s["heading_sha256"]:
            fail(mid + ": metadata source heading mismatch")
        if s["commit"] != doc["source"]["commit"] or (h and any(a < h["line_start"] or b > h["line_end"] or a > b for a,b in s["line_ranges"])):
            fail(mid + ": metadata source commit/range mismatch")
        unit = "".join("".join(lines[a-1:b]) for a,b in s["line_ranges"]).encode()
        if digest(unit) != s["unit_sha256"] or s["file_sha256"] != doc["source"]["sha256"] or s["file_git_blob"] != doc["source"]["git_blob"]:
            fail(mid + ": metadata source identity mismatch")
    for c in coverage["sections"]:
        expected = expected_headings.get((c["path"], c["line_start"]))
        if expected is None or any(c.get(k) != v for k,v in expected.items()):
            fail(c["path"] + ": complete heading coverage fields mismatch")
        if set(c.get("metadata_refs", [])) - set(metadata) or set(c.get("retired_feature_refs", [])) - set(retired):
            fail(c["path"] + ": unresolved metadata/retired coverage reference")
        if c.get("coverage_scope") == "ALL_FORMAL_FEATURES" and documents.get(c["document_id"], {}).get("document_role") != "shared-governance":
            fail(c["path"] + ": ALL_FORMAL_FEATURES only applies to shared governance")
    return found


def errors(manifest, coverage, accepted_updates=None):
    import jsonschema
    found = []
    schema = read_json(HERE / "routing-manifest.schema.json")
    found += [f"schema:{'/'.join(map(str, e.path))}: {e.message}" for e in
              jsonschema.Draft202012Validator(schema).iter_errors(manifest)]
    if found:
        return found
    found += integrity_errors(manifest, coverage, accepted_updates)
    if found:
        return found
    ids = [f["feature_id"] for f in manifest["features"]]
    if len(ids) != len(set(ids)):
        found.append("duplicate feature IDs")
    idset = set(ids)
    decs = {d["id"] for d in manifest["decisions"]}
    protos = {p["id"] for p in manifest["prototypes"]}
    docs = {d["document_id"]: d for d in manifest["documents"]}
    if len(docs) != len(manifest["documents"]):
        found.append("duplicate document IDs")
    paths = [d["source"]["path"] for d in manifest["documents"]]
    index, _, _ = fixed_inputs()
    if sorted(paths) != sorted(x["path"] for x in index):
        found.append("document coverage differs from fixed actual index")
    for f in manifest["features"]:
        prefix = f["feature_id"] + ": "
        p, v = f["future_plan"], f["destination_verification"]
        if f["document_id"] not in docs:
            found.append(prefix + "unknown document ID")
            continue
        if f["source"]["document"] != docs[f["document_id"]]["source"]["path"]:
            found.append(prefix + "document identity mismatch")
        if f["source"]["commit"] != docs[f["document_id"]]["source"]["commit"]:
            found.append(prefix + "immutable source commit mismatch")
        if set(f["decision_refs"]) - decs or set(p["prototype_refs"]) - protos:
            found.append(prefix + "unknown decision/prototype reference")
        if set(f["dependencies"]["feature_refs"]) - idset:
            found.append(prefix + "unknown feature dependency")
        if p["destination"] == "不纳入目标":
            e = p["exclusion_decision"]
            if not isinstance(e, dict) or not all(e.get(x) for x in ["user_decision_ref", "exact_scope", "decision_quote"]):
                found.append(prefix + "exclusion requires explicit user scope decision")
            if p["stage"] != "明确不纳入":
                found.append(prefix + "excluded scope/stage must agree")
        elif p["stage"] == "明确不纳入":
            found.append(prefix + "excluded stage requires excluded destination and user decision")
        if p["stage"] in ["首版", "后续"] and p["stage_approval"] != "用户已批准":
            found.append(prefix + "unapproved phase cannot be presented as committed")
        if v["status"] in ["已验证", "已否决"]:
            if not v["evidence"]:
                found.append(prefix + "verification result requires target evidence")
            if all(e.get("kind") in ["SOURCE_SPECIFICATION_ONLY", "SOURCE_STATIC", "NUMERICAL_ONLY"] for e in v["evidence"]):
                found.append(prefix + "source/numerical evidence cannot certify routing compatibility")
            if p["destination"] in ["Showdown承担", "框架与Showdown协作"] and not any(
                    e.get("kind") in ["TARGET_BEHAVIOR_PROTOTYPE", "TARGET_INTEGRATION_SCENARIO"]
                    and re.fullmatch(r"[0-9a-f]{40}", e.get("target_commit", ""))
                    and e.get("scope") and e.get("result") for e in v["evidence"]):
                found.append(prefix + "Showdown result requires fixed-target scoped behavior evidence")
        implementation = f["implementation"]
        if implementation["status"] == "实现完成" and not implementation["evidence"]:
            found.append(prefix + "implementation completion requires separate implementation evidence")
        if implementation["acceptance_status"] == "已验收" and not any(
                e.get("kind") == "IMPLEMENTATION_ACCEPTANCE" for e in implementation["evidence"]):
            found.append(prefix + "implementation acceptance requires separate acceptance evidence")
        if f["upstream"]["batches"] and not f["upstream"]["accepted_events"] and f["current_applicability"]["status"] != "待整改后核对":
            found.append(prefix + "affected baseline must retain upstream calibration gate")
    actual_headings = []
    feature_units = collections.defaultdict(list)
    for f in manifest["features"]:
        feature_units[f["source"]["document"]].append(f)
    for d in manifest["documents"]:
        path = d["source"]["path"]
        data = blob(d["source"]["commit"], path)
        hs, lines = headings(data)
        if digest(data) != d["source"]["sha256"]:
            found.append(path + ": immutable source file hash mismatch")
        expected_ids = {f["feature_id"] for f in feature_units[path]}
        if set(d["feature_ids"]) != expected_ids:
            found.append(path + ": document feature ID membership mismatch")
        current = d["current_applicability"]
        if current["snapshot_commit"] != manifest["current_snapshot"]["commit"]:
            found.append(path + ": current applicability snapshot mismatch")
        current_data = blob(current["snapshot_commit"], current["path"])
        if digest(current_data) != current["identity"]["sha256"] or current["identity"]["commit"] != current["snapshot_commit"]:
            found.append(path + ": current applicability identity mismatch")
        for h in hs:
            actual_headings.append((path, h["line_start"], h["anchor"], h["heading_sha256"]))
        occupied = set()
        for f in feature_units[path]:
            s = f["source"]
            selected = next((h for h in hs if h["anchor"] == s["anchor"] and h["heading_sha256"] == s["heading_sha256"]), None)
            if not selected:
                found.append(f["feature_id"] + ": missing source heading")
                continue
            if selected["title"] != s["heading"] or selected["level"] != s["heading_level"]:
                found.append(f["feature_id"] + ": source heading fields mismatch")
            for a, b in s["line_ranges"]:
                if a < selected["line_start"] or b > selected["line_end"] or a > b:
                    found.append(f["feature_id"] + ": invalid source range")
            for a, b in f["functional_scope"]["line_ranges"]:
                nums = set(range(a, b + 1))
                if occupied.intersection(nums):
                    found.append(f["feature_id"] + ": overlapping functional source units")
                occupied.update(nums)
            unit = "".join("".join(lines[a - 1:b]) for a, b in s["line_ranges"]).encode()
            if digest(unit) != s["unit_sha256"] or s["file_sha256"] != d["source"]["sha256"] or s["file_git_blob"] != d["source"]["git_blob"]:
                found.append(f["feature_id"] + ": immutable source unit hash mismatch")
    declared = [(c["path"], c["line_start"], c["anchor"], c["heading_sha256"]) for c in coverage["sections"]]
    if sorted(actual_headings) != sorted(declared) or len(set(declared)) != len(declared):
        found.append("heading coverage has a missing, duplicate or stale source anchor")
    for c in coverage["sections"]:
        if set(c["feature_refs"]) - idset:
            found.append(c["path"] + ": unknown coverage feature ID")
        if not c["feature_refs"] and not c.get("metadata_refs") and c.get("coverage_scope") != "ALL_FORMAL_FEATURES":
            found.append(c["path"] + ": unmapped heading")
    return found


def report(manifest, coverage):
    es = errors(manifest, coverage)
    updates = read_json(DATA_HOME / 'accepted-source-updates.json')
    events = {e['event_id']: e for e in (updates.get('events', []) if isinstance(updates, dict) else [])
              if isinstance(e, dict) and 'event_id' in e}
    def pending(f):
        return bool(set(f['upstream']['batches']) - covered_batches(f['upstream'], events))
    return {"schema_version": "routing-validation.v1", "result": "PASS_TOOL_VALIDATION" if not es else "FAIL",
            "errors": es, "documents": len(manifest["documents"]), "functional_rows": len(manifest["features"]),
            "headings": len(coverage["sections"]),
            "retired_rows": len(manifest.get("retired_features", [])),
            "metadata_records": len(manifest.get("metadata_records", [])),
            "heading_levels": dict(collections.Counter(str(c["level"]) for c in coverage["sections"])),
            "destinations": dict(collections.Counter(f["future_plan"]["destination"] for f in manifest["features"])),
            "destination_verification": dict(collections.Counter(f["destination_verification"]["status"] for f in manifest["features"])),
            "implementation_stage": dict(collections.Counter(f["future_plan"]["stage"] for f in manifest["features"])),
            "known_upstream_rows": sum(bool(f["upstream"]["batches"]) for f in manifest["features"]),
            "pending_upstream_rows": sum(pending(f) for f in manifest["features"]),
            "backfilled_upstream_rows": sum(bool(f['upstream']['batches']) and not pending(f) for f in manifest['features']),
            "partially_backfilled_upstream_rows": sum(bool(f['upstream']['accepted_events']) and pending(f) for f in manifest['features']),
            "historical_count_comparison_only": {"formal_documents_observed": len(manifest["documents"]),
                "wp_plan_rows_observed": len(json.loads(blob(DELIVERY, WP_INDEX))["rows"]),
                "hardcoded_denominator_enforced": False},
            "scope": "JSON schema, identity, references and structural section coverage only; no semantic review, compatibility approval, game execution or upstream acceptance"}


def md_cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def render(manifest, coverage):
    result = report(manifest, coverage)
    if result["errors"]:
        raise ValueError("Cannot render invalid manifest: " + str(result["errors"][:5]))
    by_doc = collections.defaultdict(list)
    linked_children = {child for f in manifest['features'] for child in f['functional_scope']['excluded_child_refs']}
    for f in manifest["features"]:
        by_doc[f["document_id"]].append(f)
    groups = collections.defaultdict(list)
    for d in manifest["documents"]:
        rel = d["source"]["path"][len(FORMAL):]
        domain = rel.split("/")[0] if "/" in rel else "shared"
        if by_doc[d["document_id"]]:
            groups[domain].append(d)
    views = HERE / "views"
    views.mkdir(exist_ok=True)
    for domain, ds in groups.items():
        text = [f"# {domain}：章节去向候选", "", "固定来源与未来计划分栏。去向均为建议；阶段、实现与验收分别登记。完整结构以 routing-manifest.json 为准。", ""]
        for d in ds:
            text += [f"## {Path(d['source']['path']).name}", "", f"{d['document_id']}；来源分类：{d['source_classification']}；关联WP：{', '.join(d['wp_refs'])}", "", "| 功能ID / 名称 | 来源事实与固定定位 | 当前适用定位 | 未来去向 / 协作方 | 依据与待验证问题 | 去向验证 | 阶段 / 实现 / 验收 | 依赖 / 差异 / 决策 / 原型 / 整改 |", "| --- | --- | --- | --- | --- | --- | --- | --- |"]
            for f in by_doc[d["document_id"]]:
                s, p = f["source"], f["future_plan"]
                ranges = ",".join(f"L{a}-L{b}" for a,b in s["line_ranges"])
                url = f"{REPO_URL}{s['commit']}/{s['document']}#L{s['line_ranges'][0][0]}"
                source = f"{s['fact_excerpt']} <br>[{s['heading']} · {ranges}]({url})；锚点 `#{s['anchor']}`；源 `{s['commit']}`"
                current_ranges = ','.join(f'L{a}-L{b}' for a,b in f['functional_scope']['line_ranges'])
                current_locator = f['current_applicability']['locator']
                current_url = f"{REPO_URL}{f['current_applicability']['snapshot_commit']}/{f['current_applicability']['document']}#L{current_locator['line_ranges'][0][0]}"
                current = f"{f['current_applicability']['status']}；[当前章节 #{current_locator['anchor']}]({current_url})；快照 `{f['current_applicability']['snapshot_commit']}`；目标范围：{f['current_applicability']['target_scope']}；职责对应的固定源区间：{current_ranges}；{f['functional_scope']['reason']}"
                if f['functional_scope']['excluded_child_refs']:
                    current += '；排除的独立子功能：' + '、'.join(
                        f'[{child}](#{child.lower()})' for child in f['functional_scope']['excluded_child_refs'])
                direct = '；'.join(f"{r['document']}#{r['anchor']}（{r['reason']}）" for r in f['dependencies']['direct_refs']) or '无额外直接来源引用'
                refs = f"WP关联：{', '.join(f['dependencies']['wp_refs']) or '无独立WP依赖'}；来源合同/交界引用（性质见说明）：{direct}；功能依赖：{', '.join(f['dependencies']['feature_refs']) or '无独立功能依赖'}；差异：{' '.join(f['differences'])}；决策：{', '.join(f['decision_refs'])}；原型：{', '.join(p['prototype_refs']) or '待设计'}；整改：{', '.join(f['upstream']['batches']) or '无当前已知正式写批'}（{f['upstream']['status']}；整文件保守绑定）"
                responsibilities = '；'.join(r['party'] + '：' + r['scope'] for r in p['responsibilities'])
                feature_label = f"{f['feature_id']} / {f['name']}"
                if f['feature_id'] in linked_children:
                    feature_label += f' <a id="{f["feature_id"].lower()}"></a>'
                cells = [feature_label, source, current,
                         f"{p['destination']}（{p['proposal_status']}）；{responsibilities}",
                         p["rationale"] + " " + " ".join(p["questions"]), f["destination_verification"]["status"],
                         f"{p['stage']}（{p['stage_approval']}） / {f['implementation']['status']} / {f['implementation']['acceptance_status']}", refs]
                text.append("| " + " | ".join(md_cell(c) for c in cells) + " |")
            text += [""]
        (views / f"{domain}.md").write_text("\n".join(text) + "\n")
    metadata_text = ["# 元数据与退役功能ID导航", "", "以下记录承担来源覆盖、依赖、测试或历史导航，不登记为待实现的游戏功能。完整旧行保存在主清单 retired_features，原ID与source不变。", "", "| 元数据ID / 角色 | 固定来源 | 原功能ID | 关联活跃功能 | 依据 |", "| --- | --- | --- | --- | --- |"]
    for r in manifest.get("metadata_records", []):
        s = r['source']
        cells = [r['metadata_id'] + ' / ' + r['kind'], f"{s['commit']} / {s['document']}#{s['anchor']}", ', '.join(r['retired_feature_ids']) or '无', ', '.join(r['feature_refs']) or '纯导航元数据', r['reason']]
        metadata_text.append('| ' + ' | '.join(md_cell(c) for c in cells) + ' |')
    (views / "metadata.md").write_text('\n'.join(metadata_text) + '\n')
    cov_text = ["# 全部正式文档与章节覆盖", "", "所有实际标题的固定定位、映射与哈希见 section-coverage.json。这里按文档汇总；标题覆盖不等于全文语义审查或去向验证。", "", "| 文档 | 角色 | 标题数 | 功能行 | WP | 整改批次 |", "| --- | --- | --- | --- | --- | --- |"]
    counts = collections.Counter(c["document_id"] for c in coverage["sections"])
    for d in manifest["documents"]:
        cov_text.append("| " + " | ".join(md_cell(x) for x in [d["source"]["path"], d["document_role"], counts[d["document_id"]], ", ".join(d["feature_ids"]) or "来源元数据（见精确覆盖映射）", ", ".join(d["wp_refs"]), ", ".join(d["upstream"]["batches"]) or "无当前已知正式写批"]) + " |")
    (HERE / "coverage.md").write_text("\n".join(cov_text) + "\n")
    save_json(HERE / "validation-result.json", result)
    save_json(HERE / "coverage-summary.json", {"schema_version": "routing-coverage-summary.v1", **{k:v for k,v in result.items() if k not in ["errors"]},
        "unmapped_headings": 0, "semantic_reading": "REVISION_RECONCILES_EVERY_PRIOR_FEATURE_VERDICT_AND_TARGETED_SOURCE_BOUNDARIES; AUTHOR_RECONCILIATION_NOT_INDEPENDENT_REVIEW",
        "compatibility_claim": "NONE", "upstream_acceptance_claim": "NONE"})


def self_test(manifest, coverage):
    cases = []
    def check(name, mutate, expected):
        m, c = copy.deepcopy(manifest), copy.deepcopy(coverage)
        mutate(m, c)
        es = errors(m, c)
        cases.append({"case": name, "expected_error_contains": expected,
                      "rejected": any(expected in e for e in es), "errors": es[:4]})
    def excluded(m, c):
        m["features"][0]["future_plan"]["destination"] = "不纳入目标"
    check("排除需要用户明确范围决策", excluded, "exclusion requires explicit user")
    def verified(m, c):
        m["features"][0]["destination_verification"].update(status="已验证", evidence=[{"kind": "SOURCE_STATIC", "ref": "source"}])
    check("纯来源证据不能确认目标兼容", verified, "cannot certify")
    check("遗漏章节锚点拒绝", lambda m,c: c["sections"].pop(), "heading coverage")
    check("源单元漂移拒绝", lambda m,c: m["features"][0]["source"].update(unit_sha256="0"*64), "immutable source")
    check("未批准首版拒绝", lambda m,c: m["features"][0]["future_plan"].update(stage="首版"), "unapproved phase")
    check("重复稳定ID拒绝", lambda m,c: m["features"][1].update(feature_id=m["features"][0]["feature_id"]), "duplicate feature IDs")
    check("不存在去向拒绝", lambda m,c: m["features"][0]["future_plan"].update(destination="自动兼容"), "schema:")
    check("实现完成需独立证据", lambda m,c: m["features"][0]["implementation"].update(status="实现完成"), "completion requires separate")
    check("实现验收需独立证据", lambda m,c: m["features"][0]["implementation"].update(acceptance_status="已验收"), "acceptance requires separate")
    result = {"schema_version": "routing-validator-negative-checks.v1", "scope": "TOOL_VALIDATION_ONLY", "cases": cases,
              "all_rejected": all(c["rejected"] for c in cases)}
    save_json(HERE / "validator-negative-checks.json", result)
    if not result["all_rejected"]:
        raise ValueError("Validator failed a negative check")
    return result


def assess_current(manifest, commit):
    actual_paths = git("ls-tree", "-r", "--name-only", commit, "--", FORMAL).decode().splitlines()
    old_paths = {d["source"]["path"] for d in manifest["documents"]}
    changed = []
    for d in manifest["documents"]:
        p = d["source"]["path"]
        if p not in actual_paths:
            changed.append({"path": p, "status": "REMOVED_REQUIRES_APPLICABILITY_DECISION"})
        else:
            new = identity(commit, p)
            if new["sha256"] != d["current_applicability"]["identity"]["sha256"]:
                changed.append({"path": p, "status": "CHANGED_REQUIRES_ACCEPTED_SECTION_BACKFILL", "identity": new,
                                "feature_ids": d["feature_ids"], "known_batches": d["upstream"]["batches"]})
    return {"snapshot_commit": commit, "changed_or_removed": changed,
            "added_formal_markdown": [p for p in actual_paths if p.endswith(".md") and p not in old_paths],
            "state": "ASSESSMENT_ONLY_NOT_APPLIED", "source_history_retained": True}


def check_generated(manifest, coverage):
    global HERE
    original = HERE
    try:
        with tempfile.TemporaryDirectory(prefix="routing-generated-check-") as tmp:
            generated = Path(tmp)
            shutil.copyfile(original / "routing-manifest.schema.json", generated / "routing-manifest.schema.json")
            HERE = generated
            render(manifest, coverage)
            relative = [p.relative_to(generated) for p in generated.rglob("*")
                        if p.is_file() and p.name != "routing-manifest.schema.json"]
            stale = [str(p) for p in relative if not (original / p).exists()
                     or (original / p).read_bytes() != (generated / p).read_bytes()]
            expected_views = {str(p) for p in relative if p.parts[0] == "views"}
            actual_views = {str(p.relative_to(original)) for p in (original / "views").glob("*.md")}
            stale += sorted(actual_views - expected_views)
            return {"result": "PASS_GENERATED_FRESHNESS" if not stale else "FAIL", "errors": stale,
                    "generated_files_compared": len(relative), "scope": "TOOL_VALIDATION_ONLY"}
    finally:
        HERE = original


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("command", choices=["seed", "validate", "render", "self-test", "assess-current", "check-generated"])
    p.add_argument("--commit")
    args = p.parse_args()
    if args.command == "seed":
        seed()
    m, c = read_json(HERE / "routing-manifest.json"), read_json(HERE / "section-coverage.json")
    if args.command in ["seed", "render"]:
        render(m,c)
        result = report(m,c)
    elif args.command == "validate":
        result = report(m,c)
    elif args.command == "self-test":
        result = self_test(m,c)
    elif args.command == "check-generated":
        result = check_generated(m,c)
    else:
        if not args.commit:
            p.error("assess-current requires --commit")
        result = assess_current(m,args.commit)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result.get("errors") else 0


if __name__ == "__main__":
    sys.exit(main())
