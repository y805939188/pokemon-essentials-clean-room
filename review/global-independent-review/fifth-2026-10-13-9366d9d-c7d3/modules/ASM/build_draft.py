#!/usr/bin/env python3
"""Finite read-only ledger join. All writes are confined to this directory.

No reference program, behavior model, game, host or shader is executed. Git is
used only to classify already-recorded gap lines; this is not a semantic reread.
Field evidence is retained at its original JSON pointer. Lexical field indexing
does not certify completeness or invent a missing premise/caller.
"""
from __future__ import annotations

import collections
import datetime
import hashlib
import json
import pathlib
import re
import subprocess

OUT = pathlib.Path(__file__).resolve().parent
ROOT = OUT.parent.parent
REPO = ROOT.parents[2]
B5 = "9366d9d17aaeac3b4414236468affa650fb3dd27"
R = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
STAMP = datetime.datetime.now(datetime.timezone.utc).isoformat()
CACHE = {}
ERRORS = []
FIELDS = {}
GAPS = []
RELOCATIONS = []


def read(path):
    path = str(path)
    if path not in CACHE:
        CACHE[path] = json.loads((ROOT / path).read_text())
    return CACHE[path]


def esc(s):
    return str(s).replace("~", "~0").replace("/", "~1")


def ref(path, pointer=""):
    return {"path": str(path), "pointer": pointer}


def resolve(r):
    d = read(r["path"])
    for k in r.get("pointer", "").split("/")[1:]:
        k = k.replace("~1", "/").replace("~0", "~")
        d = d[int(k)] if isinstance(d, list) else d[k]
    return d


def deref(r):
    try:
        return resolve(r)
    except (KeyError, IndexError, ValueError, FileNotFoundError) as e:
        ERRORS.append({"kind": "input_pointer_unresolved", "ref": r, "error": str(e)})
        return {}


def child(r, key):
    return ref(r["path"], r.get("pointer", "") + "/" + esc(key))


def file_record_ref(input_ref, expected_path):
    """Resolve the current file record by path, not the stale array ordinal."""
    rr = ref(input_ref["path"], input_ref.get("pointer", ""))
    if rr["path"] != "modules/M05/spec-to-source.json":
        return rr
    parts = rr["pointer"].split("/")
    if len(parts) >= 3 and parts[1] in {"specifications", "effective_supplements"}:
        arr = read(rr["path"])[parts[1]]
        matches = [i for i, d in enumerate(arr) if isinstance(d, dict) and d.get("path") == expected_path]
        if len(matches) == 1:
            parts[2] = str(matches[0])
            nr = ref(rr["path"], "/".join(parts))
            if nr != rr:
                RELOCATIONS.append({"original_ref": rr, "current_ref": nr, "path_identity": expected_path, "basis": "C00 accepted M05 final record path identity; array position changed"})
            return nr
    return rr


def unique(items):
    out, seen = [], set()
    for x in items:
        key = json.dumps(x, ensure_ascii=False, sort_keys=True)
        if key not in seen:
            seen.add(key)
            out.append(x)
    return out


def field(r, value=None, supplied=False):
    if not supplied:
        value = deref(r)
    key = "EF-" + hashlib.sha256((r["path"] + "#" + r["pointer"]).encode()).hexdigest()[:20]
    FIELDS[key] = {"ref": r, "value": value, "authority": "inherited_review_record_not_new_ASM_semantic_finding"}
    return key


def save(name, value):
    p = OUT / name
    assert p.parent == OUT
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def ranges(v):
    if isinstance(v, list):
        if len(v) == 2 and all(isinstance(x, int) and not isinstance(x, bool) for x in v):
            return [v] if 0 < v[0] <= v[1] else []
        out = []
        for x in v:
            out += ranges(x)
        return out
    return []


def union(rs):
    out = []
    for a, b in sorted(ranges(rs)):
        if out and a <= out[-1][1] + 1:
            out[-1][1] = max(b, out[-1][1])
        else:
            out.append([a, b])
    return out


def intersect(a, b):
    return union([[max(x, u), min(y, v)] for x, y in ranges(a) for u, v in ranges(b) if max(x, u) <= min(y, v)])


def subtract(a, b):
    out = []
    bs = union(b)
    for start, end in union(a):
        cursor = start
        for x, y in bs:
            if y < cursor:
                continue
            if x > end:
                break
            if x > cursor:
                out.append([cursor, min(end, x - 1)])
            cursor = max(cursor, y + 1)
        if cursor <= end:
            out.append([cursor, end])
    return out


def get_ranges(d):
    if not isinstance(d, dict):
        return []
    return union([d.get(k, []) for k in ("lines", "ranges", "line_ranges", "source_lines", "read_ranges", "reviewed_line_ranges", "actual_semantic_read_ranges", "actual_read_ranges", "source_read_intervals", "semantic_compared_ranges")])


def leaves(d, r):
    if isinstance(d, dict):
        for k, v in d.items():
            yield from leaves(v, child(r, k))
    elif isinstance(d, list):
        for i, v in enumerate(d):
            yield from leaves(v, child(r, i))
    else:
        yield r, d


S = read("modules/GCV/normalized-source-to-spec.json")
SEM = read("modules/GCV/normalized-semantic-records.json")
INV = read("modules/GCV/normalized-spec-to-source.json")
FILES = read("modules/GCV/normalized-file-and-range.json")
ROOTMAP = read("modules/GCV/capability-root-map.json")
ADJ = read("coverage-adjudications.json")
BIN_JOIN = read("modules/C00/BIN-projection-join.json")
ATTACH = read("modules/C00/effective-attachment-join.json")
REG = read("modules/REG/original-comparison-joins.json")
M02 = read("modules/M02/followup-partial-dispositions.json")
CORRECTIONS = read("normalization-corrections.json")
assert [len(S["capability_rows"]), len(S["other_projection_rows"]), len(INV["inverse_units"]), len(SEM["records"]), len(FILES["files"])] == [1460, 1295, 25704, 3849, 723]
SCOPE_INDEX = {(x["reviewer"], x["local_id"]): x["canonical_root_id"] for x in S["capability_rows"]}
SCOPE_BY_ID = {x["canonical_root_id"]: x for x in S["capability_rows"]}
SEM_BY_ID = {x["semantic_record_id"]: x for x in SEM["records"]}
SEM_POS = {x["semantic_record_id"]: i for i, x in enumerate(SEM["records"])}
SEM_BY_PATH = collections.defaultdict(list)
for sem in SEM["records"]:
    SEM_BY_PATH[sem["path"]].append(sem)
ADJ_INDEX = {(x["module"], x["local_capability_id"]): (i, x) for i, x in enumerate(ADJ["rows"])}
M02_INDEX = {x["id"]: (i, x) for i, x in enumerate(M02["records"])}
REG_INDEX = {x["original"]: (i, x) for i, x in enumerate(REG["records"])}
ATTACH_INDEX = {x["path"]: (i, x) for i, x in enumerate(ATTACH["files"])}
FILE_INDEX = {(x["path"], x["version"]): (i, x) for i, x in enumerate(FILES["files"])}

# Consume current canonical dispositions once. Candidate prose never overrides it.
FINDINGS = {}
for p in sorted((ROOT / "counterevidence").glob("root-*/canonical-findings.json")):
    rel = str(p.relative_to(ROOT))
    d = read(rel)
    for i, f in enumerate(d.get("findings", [])):
        FINDINGS[f["id"]] = {"ref": ref(rel, f"/findings/{i}"), "record": f}

SHARED = []
SHARED_KEYS = ("capability_id", "shared_contract_id", "id", "shared_contract", "contract_id", "canonical_identity")
for mod in sorted({x["reviewer"] for x in S["capability_rows"]}):
    path = f"modules/{mod}/shared-interfaces.json"
    if not (ROOT / path).exists():
        continue
    d = read(path)
    for key, arr in d.items():
        if not isinstance(arr, list):
            continue
        for i, item in enumerate(arr):
            if isinstance(item, dict) and any(item.get(k) for k in SHARED_KEYS):
                SHARED.append((mod, ref(path, f"/{key}/{i}"), item))

# The names below index existing evidence; they do not assert new source facts.
FACT_KEYS = {
    "comparison", "current_contract_comparison", "comparison_result", "semantic_comparison", "rules_compared",
    "semantic_comparison_result", "rules_checked", "rules", "rules_reviewed", "semantic_rules",
    "rules_and_comparison", "entry_and_rules", "entries_and_rules", "actual_semantics",
    "behavior", "behavior_purpose", "purpose", "conclusion", "supporting_fact", "source_fact",
    "specific_field_rule", "construction_default", "contract", "normal_order", "semantic_result", "semantic_review", "semantic_disposition", "semantic_review_details",
    "rejection_cancel_exception_partial_commit", "current_statement_summary", "default_data",
    "inputs", "outputs", "failure_behavior", "failure_and_edges", "invariants", "observations",
}
EXPLICIT = {
    "purpose": {"purpose", "behavior_purpose", "title", "name", "entry_and_rules", "entries_and_rules", "rules_checked", "rules_compared", "rules", "outputs", "behavior", "comparison", "comparison_result", "semantic_comparison", "semantic_result", "semantic_disposition", "scope"},
    "caller_override": {"entry_or_caller", "callers", "caller", "caller_context", "caller/config", "override", "overrides", "consumer_projection", "consumer_projections", "normal_order", "producer_consumer_chain", "consumer_selection", "entry_points", "entry", "entries", "entry_or_rule", "source_scope_for_trace_only", "necessary_caller_ranges", "consumers", "provider"},
    "preconditions": {"preconditions", "premises", "conditions", "inputs", "failure_and_edges", "rejection_cancel_exception_partial_commit"},
    "configuration_host": {"data_config_host_limits", "data_contract", "configuration", "host_limits", "runtime_limits", "data_identities", "default_data", "construction_default", "material_availability", "data_boundary", "presentation_boundary", "unknowns", "unverified"},
    "dependencies": {"dependencies", "shared_contracts", "shared_contract", "shared_capability_id", "shared_contract_identity", "consumer_projection", "consumer_projections", "consumer_modules", "canonical_capability", "shared_owner_boundary", "definition_ledger", "consumer_ledger", "record_ledgers", "consumers", "necessary_caller_ranges"},
    "unknowns": {"unknown", "unknowns", "unverified", "not_reviewed", "unreviewed_obligations", "unreviewed_semantic_obligations", "open_consumer_or_data_review", "pending", "runtime_limits", "boundary", "support_boundary", "supported_boundary", "scope_boundary", "failure_behavior"},
    "reviewed_scope": {"reviewed_scope", "review_extent", "review_completion", "review_completion_scope", "semantic_comparison_complete", "in_scope_reading_complete", "scope_review_complete", "source_review_complete_for_range", "semantic_review_scope", "review_extent_boundary", "scope_boundary", "M08_scope_review_extent", "semantic_review_complete", "within_M08_unreviewed_ranges", "assigned_scope_complete", "scope_completion", "read_extent", "semantic_scope", "read_level", "read_origin"},
    "status_reason": {"status_reason", "comparison", "current_contract_comparison", "comparison_result", "semantic_comparison", "conclusion", "current_contract_status", "rules_checked", "rules_compared", "rules_and_comparison", "final_comparison", "rules_reviewed", "semantic_rules", "semantic_disposition", "source_fact", "semantic_result", "semantic_review", "counting_boundary", "final_binding_status"},
}
PATTERNS = {
    "caller_override": re.compile(r"caller|consumer|override|callback|dispatch|调用|消费者|回调|入口|覆盖|触发|request", re.I),
    "preconditions": re.compile(r"\bif\b|\bonly\b|\bwhen\b|requires?|\bbefore\b|\bafter\b|gate|guard|reject|false|nil|default|前提|条件|守卫|仅|只有|必须|则|拒绝|失败|之前|之后|门|缺省|默认|无目标|不满足", re.I),
    "configuration_host": re.compile(r"config|setting|generation|host|native|asset|resource|default|PBS/|Windows|RPGXP|RPG Maker XP|decoder|deserializ|配置|世代|宿主|原生|资源|默认|缺省|文件|素材|图形|音频", re.I),
    "dependencies": re.compile(r"caller|consumer|callback|shared|depend|调用|消费者|依赖|回调|读取|写入|交界|转交|查询|触发", re.I),
    "unknowns": re.compile(r"unknown|unverified|unproven|not.executed|unavailable|未证|未知|未验证|未执行|缺失.*(?:宿主|地图|素材)|不保证|不声称", re.I),
}
GENERIC = re.compile(r"^(?:Primary entry/handler and necessary callers inventoried|Legal domain inputs and preceding scene/data dependencies|Shared services retain canonical owners|All actual|See corresponding fully read source ledger|Existing gameplay/IO/state/math contract|静态源段比较完成|Compared with current|Compared to current complete)", re.I)
IGNORED_KEYS = {"initial_comparison_note", "preliminary_comparison", "preliminary_comparison_status", "original_mapping_note", "first_pass_capability_status", "initial_status", "original_status", "source_code", "code", "source_text", "body", "text"}


def index_payload(d, r, bags, *, context=False):
    """Retain exact named evidence fields, not synthesized domain assertions."""
    if not isinstance(d, dict):
        return
    for k, v in d.items():
        if k in IGNORED_KEYS or v in (None, "", [], {}):
            continue
        rr = child(r, k)
        text = json.dumps(v, ensure_ascii=False) if not isinstance(v, str) else v
        generic = isinstance(v, str) and bool(GENERIC.search(v))
        matched = [name for name, keys in EXPLICIT.items() if k in keys]
        if k in FACT_KEYS and not generic:
            matched += [name for name, pat in PATTERNS.items() if pat.search(text)]
        if matched:
            fid = field(rr, v, True)
            for name in set(matched):
                bags[name].append({"field_id": fid, "relation": "bounded_rule_context" if context else "recorded_field", "specificity": "generic_boundary_only" if generic else "recorded_fact"})
        # Source anchor rules are often richer than the enclosing capability.
        if k in {"source_anchors", "source_anchor", "spec_anchors", "specification_anchors", "semantic_ranges", "semantic_segments", "segments", "definition_projection", "actual_semantic_disposition", "subranges"}:
            if isinstance(v, list):
                for j, q in enumerate(v):
                    index_payload(q, child(rr, j), bags, context=context)
            elif isinstance(v, dict):
                index_payload(v, rr, bags, context=context)


def current_record(normal):
    rr = ref(normal["input_ref"]["path"], normal["input_ref"]["pointer"])
    d = deref(rr)
    local = normal.get("local_id")
    actual_id = d.get("entry_id", d.get("id", d.get("capability_id"))) if isinstance(d, dict) else None
    if local and actual_id and str(actual_id) != str(local):
        # Preserve stable scope identity; locate current record by local identity.
        doc = read(rr["path"])
        candidates = []
        for k, arr in doc.items():
            if isinstance(arr, list):
                for i, q in enumerate(arr):
                    if isinstance(q, dict) and q.get("capability_id", q.get("id")) == local:
                        candidates.append((ref(rr["path"], f"/{k}/{i}"), q))
        if len(candidates) == 1:
            return candidates[0]
        ERRORS.append({"kind": "stable_record_identity_mismatch", "ref": rr, "expected": local, "found": actual_id})
    return rr, d


def sem_links(normal):
    """Same reviewer and overlapping coordinates, never a whole shared-file join."""
    links, payloads = [], []
    for anchor in normal.get("source_anchors", []):
        ar = get_ranges(anchor)
        for sem in SEM_BY_PATH.get(anchor["path"], []):
            if sem["reviewer"] != normal["reviewer"]:
                continue
            if ar:
                hit = intersect(ar, sem.get("actual_read_ranges", []) + sem.get("semantic_compared_range_claims", []) + sem.get("decoded_line_ranges", []))
                if not hit and not (normal["reviewer"] == "M12" and sem["coordinate_system"] != "text_lines_1based_inclusive"):
                    continue
            else:
                # Binary/native records require explicit identities below, not file equality.
                if normal["reviewer"] == "BIN":
                    continue
                hit = []
            rr = file_record_ref(sem["input_ref"], sem["path"])
            raw = deref(rr)
            if not isinstance(raw, dict):
                raw = {}
            links.append({"semantic_record_id": sem["semantic_record_id"], "ref": rr, "source_path": sem["path"], "intersection_ranges": hit, "coordinate_system": sem["coordinate_system"], "record_extent": sem.get("review_extent_claim"), "scope_boundary": sem.get("reviewer_scope"), "does_not_transfer_full_file_or_neighboring_rules": True})
            # Only the bounded statements overlapping this scope are field evidence.
            for st in (sem.get("semantic_statements", []) if sem["reviewer"] != "M05" else []):
                sr = get_ranges(st.get("coordinates", {}))
                if ar and sr and not intersect(ar, sr):
                    continue
                stref = ref(st["record_ref"]["path"], st["record_ref"]["pointer"])
                payloads.append((stref, deref(stref), True))
            # M04's rich reviewed_ranges are not expanded in the GCV statements.
            for key in (("reviewed_ranges", "semantic_segments", "sections") if sem["reviewer"] == "M05" else ("reviewed_ranges",)):
                for j, item in enumerate(raw.get(key, []) if isinstance(raw.get(key), list) else []):
                    if isinstance(item, dict) and (not ar or intersect(ar, get_ranges(item))):
                        payloads.append((child(child(rr, key), j), item, True))
            # Take only top-level factual/boundary fields from the file record.
            raw_top = {k: v for k, v in raw.items() if k not in {"semantic_ranges", "semantic_segments", "segments", "clauses", "sections", "source_anchors"}}
            payloads.append((rr, raw_top, True))
    return unique(links), payloads


# Named BIN definitions and M09 segments are exact joins, not path matches.
BIN_DEFINITIONS = {}
for sem in SEM["records"]:
    if sem["reviewer"] == "BIN":
        rr = ref(sem["input_ref"]["path"], sem["input_ref"]["pointer"])
        raw = deref(rr)
        if not isinstance(raw, dict):
            continue
        for k in ("id", "source_record", "source_record_id", "block", "block_id"):
            v = raw.get(k)
            if isinstance(v, str):
                BIN_DEFINITIONS.setdefault(v, []).append((rr, raw, sem["semantic_record_id"]))
M09_SEGMENTS = {}
M09_SEGMENT_PARENTS = {}
for i, path in enumerate(read("modules/M09/source-to-spec.json")["source_paths"]):
    for j, seg in enumerate(path.get("segments", [])):
        M09_SEGMENTS[seg["id"]] = (ref("modules/M09/source-to-spec.json", f"/source_paths/{i}/segments/{j}"), seg)
        M09_SEGMENT_PARENTS[seg["id"]] = (ref("modules/M09/source-to-spec.json", f"/source_paths/{i}"), path)
M09_CLAUSES = {}
for key in ("documents", "test_documents"):
    for i, doc in enumerate(read("modules/M09/spec-to-source.json")[key]):
        for j, clause in enumerate(doc.get("clauses", [])):
            M09_CLAUSES[clause["id"]] = (ref("modules/M09/spec-to-source.json", f"/{key}/{i}/clauses/{j}"), clause, doc)
FIXTURE_REFS = {q["fixture_id"]: ref("modules/GCV/fixture-maps.json", f"/mappings/{i}") for i, q in enumerate(read("modules/GCV/fixture-maps.json")["mappings"])}
M01_FIELD_INDEX = collections.defaultdict(list)
for i, item in enumerate(read("modules/M01/schema-field-contracts.json")["fields"]):
    for local in item.get("capability_refs", []):
        M01_FIELD_INDEX[local].append((ref("modules/M01/schema-field-contracts.json", f"/fields/{i}"), item))


def declared_shared(d):
    vals = []
    for k in ("shared_contracts", "shared_contract", "shared_capability_id", "shared_contract_identity", "canonical_capability", "alias_of"):
        v = d.get(k)
        if isinstance(v, str):
            vals.append(v)
        elif isinstance(v, list):
            vals += [a for a in v if isinstance(a, str)]
    return unique(vals)


def owner_route(n, d):
    m, local = n["reviewer"], n.get("local_id")
    target = []
    relation = "reviewer_scoped_primary_or_projection"
    explicit_owner = d.get("canonical_owner", d.get("owner", m))
    if m == "RES":
        owners = {
            "RES-AUDIO-SF2": ["M12-ROOT-23"],
            "RES-ANIMMAKER": ["M12-ROOT-24"],
            "RES-EXTENDTEXT": ["M12-ROOT-24"],
            "RES-NATIVE-INTERFACES": ["M12-ROOT-25"],
            "RES-FONT-BMP-CONTEXT": ["M12-ROOT-21", "M12-ROOT-22"],
        }
        target = [SCOPE_INDEX[("M12", x)] for x in owners[local]]
        relation = "evidence_projection_to_existing_M12_scope_not_equivalence"
        explicit_owner = "M12"
    elif m == "M10" and local == "M10-C-DEX-SHARED":
        target = [x["canonical_root_id"] for x in S["capability_rows"] if x["reviewer"] == "M11" and any("Pokedex" in a["path"] for a in x.get("source_anchors", []))]
        relation = "delegated_to_named_M11_pokedex_scopes_not_M10_behavior_signoff"
        explicit_owner = "M11"
    for alias in declared_shared(d):
        for (mod, lid), sid in SCOPE_INDEX.items():
            if alias == lid and sid != n.get("canonical_root_id"):
                target.append(sid)
    return {"reviewer_owner_claim": explicit_owner, "target_scope_ids": unique(target), "relation": relation, "shared_aliases": declared_shared(d), "JXN_join_state": "pending_parent_final_delta", "JXN_join_keys": {"module": m, "local_id": local, "input_ref": n["input_ref"], "scope_id": n.get("canonical_root_id"), "shared_aliases": declared_shared(d)}, "identity_merge_authorized": False}


def status_for(n, d):
    raw = d.get("capability_status", d.get("status", d.get("state", n.get("support_status"))))
    standard = raw if raw in {"supported", "partial", "missing", "unresolved", "not_reviewed"} else "unresolved"
    reason_refs, overlays = [], []
    k = (n["reviewer"], n.get("local_id"))
    if k in ADJ_INDEX:
        i, adj = ADJ_INDEX[k]
        overlays.append(ref("coverage-adjudications.json", f"/rows/{i}"))
        decision = adj["final_bounded_disposition"]
        if decision.startswith("partial_required"):
            standard = "partial"
        elif decision == "missing_required":
            standard = "missing"
        elif decision.startswith("unresolved") or "unresolved_native" in decision:
            standard = "unresolved"
        elif decision.startswith("supported_scoped"):
            standard = "supported"
        elif decision == "delegated_consumer_projection":
            standard = "not_reviewed"  # Local projection did not sign the primary behavior.
        reason_refs.append(field(ref("coverage-adjudications.json", f"/rows/{i}/reason")))
    if n["reviewer"] == "RES":
        standard = "partial" if n["local_id"] in {"RES-ANIMMAKER", "RES-EXTENDTEXT"} else "unresolved"
    if n["reviewer"] == "M02" and n.get("local_id") in M02_INDEX:
        i, sub = M02_INDEX[n["local_id"]]
        overlays.append(ref("modules/M02/followup-partial-dispositions.json", f"/records/{i}"))
        statuses = [x["status"] for x in sub["subranges"]]
        if any(x.get("final_finding") for x in sub["subranges"]):
            standard = "partial"
        elif any("unresolved" in s or "runtime" in s for s in statuses):
            standard = "unresolved"
        else:
            standard = "supported"
    return standard, raw, reason_refs, overlays


def build_row(n, index, projection=False):
    rr, raw = current_record(n)
    n = dict(n)
    if not n.get("source_anchors") and raw.get("source_anchors"):
        n["source_anchors"] = raw["source_anchors"]
    if n["reviewer"] == "M12" and n.get("local_id") == "M12-ROOT-22":
        n["source_anchors"] = [{"path": f["path"], "version": f["version"], "git_blob": f["git_blob"], "ranges": [], "coordinate_system": "named_font_tables_cmap_metrics_encoded_glyphs", "scope": "Inherited M12 actual resource fields; native selection/hinting remain unverified", "original_directory_anchor_ref": child(child(rr, "source_anchors"), 0)} for f in FILES["files"] if f["bucket"] == "reference_files" and f["path"].startswith("Fonts/")]
    if n["reviewer"] == "M09" and not projection:
        extra_anchors, extra_spec = [], []
        for sid in raw.get("source_segment_ids", []):
            if sid in M09_SEGMENTS:
                sr, sd = M09_SEGMENTS[sid]
                pr, pd = M09_SEGMENT_PARENTS[sid]
                extra_anchors.append({"path": pd["path"], "version": pd["version"], "ranges": sd["line_ranges"], "coordinate_system": "text_lines_1based_inclusive", "entry": sd["entry_points"], "evidence_ref": sr})
        for cid in raw.get("spec_clause_ids", []):
            if cid in M09_CLAUSES:
                cr, cd, pd = M09_CLAUSES[cid]
                extra_spec.append({"path": pd["path"], "version": pd["version"], "ranges": cd["lines"], "clause_id": cid, "evidence_ref": cr})
        n["source_anchors"] = unique(n.get("source_anchors", []) + extra_anchors)
        n["formal_receiving_claims"] = {**n.get("formal_receiving_claims", {}), "exact_current_M09_clause_anchors": extra_spec}
    bags = {k: [] for k in EXPLICIT}
    index_payload(raw, rr, bags)
    links, payloads = sem_links(n)
    for r, d, context in payloads:
        index_payload(d, r, bags, context=context)
    for sid in raw.get("source_segment_ids", []) + raw.get("semantic_segment_ids", []):
        if sid in M09_SEGMENTS:
            sr, sd = M09_SEGMENTS[sid]
            index_payload(sd, sr, bags, context=True)
            pr, pd = M09_SEGMENT_PARENTS[sid]
            index_payload({k: v for k, v in pd.items() if k != "segments"}, pr, bags, context=True)
    for sr, sd in M01_FIELD_INDEX.get(n.get("local_id"), []):
        index_payload(sd, sr, bags, context=True)
    for bid in raw.get("source_ids", []) + ([raw["source_record"]] if raw.get("source_record") else []) + ([raw["block"]] if raw.get("block") else []):
        for sr, sd, semid in BIN_DEFINITIONS.get(bid, []):
            index_payload(sd, sr, bags, context=True)
            links.append({"semantic_record_id": semid, "ref": sr, "relation": "explicit_BIN_source_id", "source_id": bid, "does_not_transfer_native_selection": True})
    if n["reviewer"] == "RES" and n.get("local_id") == "RES-FONT-BMP-CONTEXT":
        bags["reviewed_scope"].append({"field_id": field(child(rr, "observations")), "relation": "exact_reuse_context_no_new_RES_format_review", "specificity": "recorded_fact"})
    if n["reviewer"] == "M12B" and n.get("local_id") == "M12-M02":
        bags["reviewed_scope"].append({"field_id": field(child(rr, "semantic_comparison")), "relation": "twelve_named_unavailable_chain_families_not_available_source_gap", "specificity": "recorded_fact"})
    if n["reviewer"] == "BIN" and n.get("local_id") == "BIN-C13":
        for name in ("reviewed_scope", "configuration_host"):
            bags[name].append({"field_id": field(child(rr, "conclusion")), "relation": "finite_dictionary_and_string_data_classification_excludes_native_error_path_proof", "specificity": "recorded_fact"})
    aliases = set(declared_shared(raw) + [n.get("local_id")])
    shared_refs = []
    for mod, sr, sd in SHARED:
        if mod != n["reviewer"]:
            continue
        if aliases.intersection(sd.get(k) for k in SHARED_KEYS if isinstance(sd.get(k), str)):
            index_payload(sd, sr, bags, context=True)
            shared_refs.append(sr)
    if n["reviewer"] == "M02" and n.get("local_id") in M02_INDEX:
        i, sd = M02_INDEX[n["local_id"]]
        sr = ref("modules/M02/followup-partial-dispositions.json", f"/records/{i}")
        index_payload(sd, sr, bags, context=True)
        for j, sub in enumerate(sd["subranges"]):
            for k in ("reference_facts", "semantic_reason", "bounded_controls", "policy_boundary", "no_required_revision_reason"):
                if sub.get(k) not in (None, [], ""):
                    fid = field(child(child(child(sr, "subranges"), j), k))
                    names = ["status_reason"]
                    if k in {"reference_facts", "bounded_controls", "policy_boundary"}:
                        names += ["preconditions"]
                    if k == "policy_boundary":
                        names += ["unknowns"]
                    for name in names:
                        bags[name].append({"field_id": fid, "relation": "accepted_finite_M02_subrange", "specificity": "recorded_fact"})
    stable = n.get("canonical_root_id") or ("ASM-PROJ-" + hashlib.sha256((rr["path"] + "#" + rr["pointer"]).encode()).hexdigest()[:20])
    standard, original_status, reason_refs, overlays = status_for(n, raw)
    for fid in reason_refs:
        bags["status_reason"].append({"field_id": fid, "relation": "root_accepted_disposition", "specificity": "recorded_fact"})
    fields = {}
    missing = []
    for name, items in bags.items():
        items = unique(items)
        specific = any(x["specificity"] == "recorded_fact" for x in items)
        fields[name] = {"state": "recorded" if specific else "not_separately_recorded", "evidence": items, "complete_condition_inventory_asserted_by_ASM": False}
        if not specific and name in {"purpose", "caller_override", "preconditions", "configuration_host", "dependencies", "status_reason", "reviewed_scope"} and not projection:
            missing.append(name)
            GAPS.append({"unit_id": stable, "module": n["reviewer"], "local_id": n.get("local_id"), "field": name, "input_ref": rr, "matrix_ref": ref(f"modules/ASM/{'projection-draft.json' if projection else 'matrix-'+n['reviewer']+'.json'}", f"/rows/{index}/{name}"), "searched_semantic_refs": [x["ref"] for x in links], "disposition": "field_not_separately_recorded_in_bounded_join; not an assertion of absent feature or unread source", "needed": "Exact caller/condition/configuration/extent fact at this scope, or evidenced not-applicable disposition"})
    classification = raw.get("classification")
    if not classification:
        domain_map = {"generic-kernel": "Generic Kernel", "creature-rpg": "Creature-RPG", "pokemon-rules": "Pokémon Rules", "combat-requirements": "Combat Requirements", "engine-overworld": "Engine / Overworld Integration", "user-interface": "User Interface", "demo-dx": "Demo / Developer Experience"}
        spec_text = json.dumps(n.get("formal_receiving_claims", n.get("source_projection", {})), ensure_ascii=False)
        classification = [v for k, v in domain_map.items() if "/" + k + "/" in spec_text]
    finding_ids = unique(n.get("finding_ids", []) + [x for k in ("related_findings", "findings", "candidate_refs") for x in raw.get(k, []) if isinstance(x, str)])
    if (n["reviewer"], n.get("local_id")) in ADJ_INDEX:
        finding_ids = unique(finding_ids + ADJ_INDEX[(n["reviewer"], n.get("local_id"))][1]["canonical_finding_ids"])
    if n["reviewer"] == "M02" and n.get("local_id") in M02_INDEX:
        finding_ids = unique(finding_ids + [x["final_finding"] for x in M02_INDEX[n["local_id"]][1]["subranges"] if isinstance(x.get("final_finding"), str)])
    findings = [{"id": fid, "canonical_ref": FINDINGS.get(fid, {}).get("ref"), "scope_not_expanded": True} for fid in finding_ids]
    row = {
        "scope_id": stable, "record_kind": "projection" if projection else "stable_audit_scope_not_product_feature",
        "module": n["reviewer"], "local_id": n.get("local_id"), "domain": classification or ["UNRESOLVED_domain_not_separately_recorded"],
        "original_input_ref": n["input_ref"], "current_input_ref": rr,
        "normalized_input_ref": ref("modules/GCV/normalized-source-to-spec.json", f"/{'other_projection_rows' if projection else 'capability_rows'}/{n['_gcv_index']}"),
        "source_anchors": [{k: v for k, v in a.items() if k not in {"actual_semantic_record_ids", "comparison_match_boundary"}} for a in n.get("source_anchors", [])],
        "specification_anchors": n.get("formal_receiving_claims", n.get("source_projection", {})),
        **fields,
        "actual_reviewed_scope": {"capability_scope_ref": rr, "matched_semantic_records": unique(links), "extent_evidence": fields["reviewed_scope"]["evidence"], "reviewer_scope_only": True, "ASM_new_source_semantic_review": False},
        "status": standard, "status_before_join": original_status, "status_scope": "named_behavior_or_definition_only; support_and_reading_are_separate",
        "accepted_disposition_refs": overlays, "reviewer_and_evidence": {"primary": n["reviewer"], "integrator": "ASM", "input_ref": rr, "shared_interface_refs": shared_refs, "evidence_levels": raw.get("evidence_level"), "new_execution": "NOT_EXECUTED"},
        "findings": findings, "ownership_and_alias": owner_route(n, raw), "missing_field_dispositions": missing,
        "source_scope_fingerprint": n.get("stable_source_scope_fingerprint"), "behavior_scope_fingerprint": n.get("behavior_scope_fingerprint"),
        "pending_final_delta": ["M01_finite60_parent_reception"] if n["reviewer"] == "M01" and original_status == "partial" else [],
        "global_product_feature_count_credit": False,
    }
    if n["reviewer"] == "M08":
        row["superseded_progress_language"] = {"ref": ref("modules/M08/reading-coverage.json", "/strict_review_interpretation"), "rule": "Earlier 待/未读 words in retained first-pass records are not current work remaining. Final completion covers assigned static scope only."}
        row["effective_parent_corrections"] = ref("modules/M08/source-to-spec.json", "/effective_parent_corrections/0")
        if raw.get("unknowns"):
            old_id = field(child(rr, "unknowns"))
            row["historical_unknown_field"] = old_id
            row["unknowns"]["evidence"] = [x for x in row["unknowns"]["evidence"] if x["field_id"] != old_id]
    if n["reviewer"] == "M11" and original_status == "partial":
        f = FINDINGS["GR5-M11-005"]
        row["M11_resource_facet_partition"] = {"canonical_ref": f["ref"], "required_subscopes_ref": child(f["ref"], "required_subscopes"), "optional_facets_ref": child(f["ref"], "optional_facets_not_authorized_as_required"), "no_required_facets_ref": child(f["ref"], "no_required_revision_facets"), "rule": "47 broad primary partial rows are reviewed scopes, not 47 mandatory resource gaps. Match each named consumer/predicate to the canonical facet; do not spread 005 over this entire range."}
        # Finite draft routing from the primary's named purpose to root005 facets.
        # Pure resource ranges within a consumer are not promoted to its timing gap.
        mandatory = {39: "005-REGION-MAP", 47: "005-DUEL-TIMING", 49: "005-DUEL-TIMING", 50: "005-DUEL-TIMING", 52: "005-TRIAD-MESSAGES", 69: "005-VOLTORB-TIMING", 71: "005-VOLTORB-TIMING", 75: "005-MINING-LOCK", 80: "005-MINING-LOCK", 84: "005-TILE-TIMING", 85: "005-TILE-TIMING", 86: "005-TILE-TIMING"}
        optional = {10: "005-POKEDEX-SEARCH", 11: "005-POKEDEX-SEARCH", 13: "005-POKEDEX-SEARCH", 14: "005-POKEDEX-SEARCH", 17: "005-POKEDEX-SEARCH", 20: "005-POKEDEX-ENTRY", 22: "005-POKEDEX-ENTRY", 23: "005-POKEDEX-ENTRY", 24: "005-POKEDEX-ENTRY", 62: "005-SLOT-DECORATION", 63: "005-SLOT-DECORATION", 64: "005-SLOT-DECORATION", 65: "005-SLOT-DECORATION", 76: "005-MINING-ATLAS"}
        no_required = {6: "005-POKEDEX-MENU", 7: "005-POKEDEX-MENU", 34: "005-POKEGEAR-VARIANTS", 41: "005-PHONE", 44: "005-JUKEBOX", 45: "005-JUKEBOX"}
        number = int(n["local_id"].split("S")[-1])
        key = mandatory.get(number) or optional.get(number) or no_required.get(number)
        facet_refs = []
        for family in ("required_subscopes", "optional_facets_not_authorized_as_required", "no_required_revision_facets"):
            for j, facet in enumerate(f["record"].get(family, [])):
                if facet["key"] == key:
                    facet_refs.append({"ref": child(child(f["ref"], family), j), "key": key, "disposition": facet["disposition"]})
        row["M11_resource_facet_partition"]["row_specific_005_join"] = {"primary_rule_ref": child(rr, "behavior_purpose"), "facets": facet_refs, "required_005_credit": number in mandatory, "rule": "Only the named timing/predicate portion in the cited primary rule receives a mandatory facet; other002/003/004/001 findings remain separately scoped.", "unmatched_scope": None if facet_refs else ("005 not cited by this row" if "GR5-M11-005" not in finding_ids else "Resource/setup/presentation part of the consumer; root005 does not authorize this whole range as mandatory. Parent may refine this alias without re-reviewing source.")}
    if n["reviewer"] == "M12B":
        row["review_summary_correction_ref"] = ref("normalization-corrections.json", "/corrections/0")
    return row


def build_matrix():
    by_module = collections.defaultdict(list)
    for i, normal in enumerate(S["capability_rows"]):
        normal = dict(normal, _gcv_index=i)
        mod = normal["reviewer"]
        by_module[mod].append(build_row(normal, len(by_module[mod])))
    for mod, rows in by_module.items():
        save(f"matrix-{mod}.json", {"schema_version": "gr5.asm.scope-draft.v1", "module": mod, "rows": rows})
    prows = []
    for i, normal in enumerate(S["other_projection_rows"]):
        normal = dict(normal, _gcv_index=i)
        row = build_row(normal, i, True)
        parents = list(normal.get("canonical_root_ids", []))
        parent_ref = None
        for j, binding in enumerate(BIN_JOIN["closed_GCV_unresolved_parent_projections"]):
            if binding["input_pointer"] == normal["input_ref"]["path"] + "#" + normal["input_ref"]["pointer"]:
                parents = [SCOPE_INDEX[("BIN", p)] for p in binding["primary_capabilities"]]
                parent_ref = ref("modules/C00/BIN-projection-join.json", f"/closed_GCV_unresolved_parent_projections/{j}")
                row["conditional_parent_bindings"] = {"accepted_rule_ref": parent_ref, "candidate_exact_definition_join_ref": ref("modules/C00/BIN-projection-join.json", "/program_candidate_exact_definition_joins") if binding["classification"] == "program_or_prefix" else None, "all_parent_scopes_simultaneously_applicable": False}
        if normal.get("kind") == "explicit_parent_ownership_projection":
            parents = [SCOPE_INDEX[("M12", x)] for x in [f"M12-ROOT-{j:02d}" for j in range(1, 26)]]
            row["ownership_navigation_only"] = {"ref": normal["input_ref"], "route": "root/M12 assigned source and resource scopes; destination scope selected by source coordinates", "behavior_support_credit": False}
        row["parent_scope_ids"] = parents
        row["parent_join_ref"] = parent_ref
        row["parent_identity_kind"] = "conditional_or_navigation" if parent_ref or normal.get("kind") == "explicit_parent_ownership_projection" else "explicit_declared_parent"
        row["parent_status_is_not_automatically_inherited"] = True
        for name in EXPLICIT:
            if row[name]["state"] == "not_separately_recorded":
                row[name]["state"] = "parent_scoped_context_not_independent_fact"
                row[name]["parent_field_refs"] = [{"scope_id": p, "field": name} for p in parents]
        if normal["kind"] in {"registration_ledger", "function_mappings", "long_block_mappings", "candidate_family_mappings"}:
            row["status"] = "supported"
            row["status_scope"] = "existing_explicit_projection_binding_only_not_independent_behavior_or_native_selection"
        prows.append(row)
    save("projection-draft.json", {"schema_version": "gr5.asm.projection-draft.v1", "rows": prows, "count": len(prows)})
    return by_module, prows


def build_inverse():
    routes = []
    index_rows = []
    route_path = "deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md"
    # Only the39 already-reviewed responsibility rows are consumed as routing text.
    route_lines = subprocess.check_output(["git", "-C", str(REPO), "show", B5 + ":" + route_path]).decode().splitlines()
    for i, u in enumerate(INV["inverse_units"]):
        rr = (file_record_ref(u["input_ref"], u["path"]) if "pointer" in u["input_ref"] else FIXTURE_REFS[u["input_ref"]["fixture_id"]])
        receiving_refs = []
        if u["reviewer"] == "M05" and "/sections/" in rr["pointer"]:
            base = ref(rr["path"], rr["pointer"].split("/sections/")[0])
            doc = deref(base)
            for j, section in enumerate(doc.get("sections", [])):
                if intersect(get_ranges(section), u.get("ranges", [])):
                    receiving_refs.append(child(child(base, "sections"), j))
            # The old inverse unit may now be several smaller current sections.
            # Retain its stable ID and attach those sections; do not invent equality.
            rr = receiving_refs[0] if len(receiving_refs) == 1 else base
        raw = deref(rr)
        row = {"inverse_unit_id": u["inverse_unit_id"], "normalized_ref": ref("modules/GCV/normalized-spec-to-source.json", f"/inverse_units/{i}"), "actual_record_ref": rr, "specification_path": u.get("path"), "version": u.get("version"), "ranges": u.get("ranges"), "canonical_root_ids": u.get("canonical_root_ids", []), "source_anchor_ids": u.get("source_anchor_ids", []), "mapping_granularity": u.get("mapping_granularity"), "kind": u.get("kind"), "not_a_capability_or_reading_count": True}
        if u["reviewer"] == "M05":
            row["M05_current_receiving_sections"] = receiving_refs
            row["scope_identity_preserved_not_recounted"] = True
            row["original_snapshot_ref"] = u["input_ref"]
        if raw.get("claim_kind") == "responsibility_assignment_only":
            targets = [SCOPE_INDEX[("M01", lid)] for lid in raw["capability_refs"] if ("M01", lid) in SCOPE_INDEX]
            row["routing_scope_ids"] = targets
            row["behavior_support_credit"] = False
            fields = []
            for lid in raw["capability_refs"]:
                fields += [r for r, _ in M01_FIELD_INDEX.get(lid, [])]
            line_number = raw["lines"][0]
            text = route_lines[line_number - 1]
            cells = [v.strip() for v in text.strip("|").split("|")]
            primary_text = cells[2]
            direction = "primary_domain_responsibility"
            if "各负责规格" in primary_text:
                primary_text = cells[1]
                direction = "per_fixed_rule_family_responsibility"
            elif "反向引用" in primary_text:
                primary_text = cells[3]
                direction = "reverse_reference_only_no_Move_field_owner"
            workpackages = unique(re.findall(r"WP\d+(?:-[A-C])?", primary_text))
            domain_routes = []
            for wp in workpackages:
                pattern = re.compile(r"^" + re.escape(wp.lower()) + r"(?:-|\.)")
                for fi, formal in enumerate(FILES["files"]):
                    if formal["bucket"] == "formal_files" and "/test-catalog/" not in formal["path"] and pattern.search(pathlib.Path(formal["path"]).name):
                        domain_routes.append({"workpackage": wp, "formal_path": formal["path"], "primary_reviewers": formal["owner"], "file_identity_ref": ref("modules/GCV/normalized-file-and-range.json", f"/files/{fi}"), "destination_kind": direction, "all_rules_in_document_not_automatically_claimed": True})
            routes.append({"inverse_unit_id": u["inverse_unit_id"], "ref": rr, "specification_path": u["path"], "ranges": u["ranges"], "primary_owner": "M01 for schema/field definition", "target_scope_ids": targets, "schema_field_refs": unique(fields), "responsibility_table_row": {"path": route_path, "version": B5, "lines": [line_number, line_number], "field_group": cells[1], "primary_receiver_cell": cells[2], "forward_dependency_cell": cells[3]}, "actual_domain_destinations": domain_routes, "status": "supported", "status_applies_to": "responsibility routing only", "consumer_domain_signoff": "The named current receiver/primary reviewer is the destination; source definitions keep their M01 scope, and JXN final shared identity is pending", "no_identity_merge": True})
        index_rows.append(row)
    save("inverse-index.json", {"schema_version": "gr5.asm.inverse-index.v1", "source_anchor_catalog_ref": ref("modules/GCV/normalized-spec-to-source.json", "/source_anchor_catalog"), "units": index_rows, "original_record_facts_retained_by_exact_ref": True, "count": len(index_rows)})
    save("owner-routing.json", {"schema_version": "gr5.asm.routing.v1", "M01_owner_routing_rows": routes, "count": len(routes), "counting": "39 inverse responsibility rows, not additional capabilities"})
    return routes


READ_KEYS = ("read_ranges", "read_line_ranges", "source_read_intervals", "actual_read_ranges", "actual_semantic_read_ranges", "actual_read_line_ranges", "reviewed_line_ranges", "physical_read_ranges_this_followup", "physical_read_ranges_new", "body_read_ranges", "read_intervals", "content_read_range")
CHILD_KEYS = ("semantic_ranges", "semantic_segments", "segments", "clauses", "sections", "data_semantic_ranges", "semantic_comparison_ranges", "reviewed_ranges")
READ_ONLY = re.compile(r"source read only|source-only|source read;|does not sign|not .*full.domain|inventory.only|not_reviewed", re.I)


def evidence_ranges(raw, sem):
    rs, refs = [], []
    rr = file_record_ref(sem["input_ref"], sem["path"])
    semantic = sem["semantic_disposition_kind"] not in {"inventory_or_explicit_unsigned_scope", "reading_or_inventory_statement_only"}
    if raw.get("semantic_comparison_complete_for_owned_ranges"):
        rs += ranges(raw.get("owned_ranges"))
        refs.append(child(rr, "owned_ranges"))
    if raw.get("assigned_semantic_ranges") and (raw.get("assigned_scope_complete") or raw.get("comparison_result")):
        rs += ranges(raw["assigned_semantic_ranges"])
        refs.append(child(rr, "assigned_semantic_ranges"))
    for key in CHILD_KEYS:
        for i, item in enumerate(raw.get(key, []) if isinstance(raw.get(key), list) else []):
            if not isinstance(item, dict):
                continue
            comparison = str(item.get("comparison_result", item.get("comparison", "")))
            if READ_ONLY.search(comparison):
                continue
            if any(k in item for k in FACT_KEYS | {"result", "status", "final_comparison", "source_anchors"}):
                rs += get_ranges(item)
                refs.append(child(child(rr, key), i))
    rs += sem.get("semantic_compared_range_claims", []) + sem.get("qualified_exact_reuse_ranges", [])
    # GCV named dispositions with real statement bodies justify their read scope;
    # inventory/hash/owner records alone do not.
    if semantic and (sem.get("semantic_statements") or raw.get("semantic_disposition") or raw.get("semantic_review_complete")):
        if not raw.get("owned_ranges"):
            rs += sem.get("actual_read_ranges", [])
    for reuse_key in ("qualified_reuse", "exact_reuse"):
        for i, item in enumerate(raw.get(reuse_key, []) if isinstance(raw.get(reuse_key), list) else []):
            rs += ranges(item.get("original_lines", item.get("original_ranges", [])))
            refs.append(child(child(rr, reuse_key), i))
    return union(rs), refs


def fixed_lines(f):
    # Read only the fixed object required to classify the recorded gap intervals.
    if f["bucket"] == "reference_files":
        source_repo = SEM["source_baseline"]["read_only_root"]
        command = ["git", "-C", source_repo, "show", f["version"] + ":" + f["path"]]
    else:
        command = ["git", "-C", str(REPO), "show", f["version"] + ":" + f["path"]]
    p = subprocess.run(command, capture_output=True, check=False)
    if p.returncode:
        ERRORS.append({"kind": "gap_fixed_object_unavailable", "path": f["path"], "version": f["version"], "reason": p.stderr.decode(errors="replace")[:300]})
        return None
    return p.stdout.decode("utf-8-sig", errors="replace").splitlines()


def layout_disposition(line, path):
    t = line.strip()
    if not t:
        return "blank_layout"
    if path.endswith(".md"):
        if re.fullmatch(r"[| :\-]+", t) or t in {"---", "***"} or re.fullmatch(r"```[a-zA-Z0-9_-]*", t):
            return "markdown_layout_delimiter"
        if t.startswith("#"):
            return "heading_navigation_with_separate_body_evidence"
        if re.match(r"\|\s*ID\s*\|", t):
            return "table_column_heading_no_new_rule"
        if t.startswith(("本文件登记", "本目录记录")) and ("静态" in t and "执行" in t):
            return "test_catalog_scope_metadata_static_not_execution"
        if t.startswith("B18 本地后继"):
            return "dated_approval_qualification_not_current_behavior_proof"
        if t.startswith(("历史异常的未来修正/兼容", "新116生产端范围为", "WP35 §5.2/§9与EG-13/20")):
            return "explicit_scope_or_historical_evidence_boundary"
    return "semantic_or_context_text_needs_recorded_disposition"


def build_files():
    results, flagged = [], []
    for i, f in enumerate(FILES["files"]):
        records, sem_rs, physical_current = [], [], []
        full_proofs = []
        for sid in f["semantic_record_ids"]:
            sem = SEM_BY_ID[sid]
            rr = file_record_ref(sem["input_ref"], sem["path"])
            raw = deref(rr)
            if not isinstance(raw, dict):
                raw = {}
            if raw.get("path") and raw["path"] != f["path"]:
                ERRORS.append({"kind": "file_record_identity_mismatch", "file": f["path"], "ref": rr, "actual": raw.get("path")})
                continue
            compared, specific_refs = evidence_ranges(raw, sem)
            sem_rs += compared
            for k in READ_KEYS:
                physical_current += ranges(raw.get(k, []))
            extent = raw.get("review_extent", raw.get("read_level", sem.get("review_extent_claim")))
            rec = {"semantic_record_id": sid, "reviewer": sem["reviewer"], "ref": rr, "review_extent": extent, "scope": raw.get("assigned_scope", raw.get("scope_role", raw.get("semantic_scope", sem.get("reviewer_scope")))), "compared_ranges": compared, "specific_evidence_refs": specific_refs, "semantic_disposition_kind": sem["semantic_disposition_kind"], "remaining_record": sem.get("excluded_or_unreviewed", {}), "coordinate_system": sem["coordinate_system"], "other_coordinates": sem.get("other_coordinates", {})}
            records.append(rec)
            excludes = [raw.get(k) for k in ("unreviewed_ranges", "unreviewed_intervals", "in_scope_unreviewed_intervals", "not_reviewed_ranges") if raw.get(k)]
            richer = bool(specific_refs or sem.get("semantic_statements") or raw.get("semantic_disposition") or raw.get("semantic_scope") or raw.get("semantic_review_complete") or (raw.get("semantic_status") and raw.get("scope_completion")) or raw.get("result"))
            if extent == "full" and not excludes and richer and not f["binary"] and sem["semantic_disposition_kind"] != "inventory_or_explicit_unsigned_scope":
                full_proofs.append({"ref": rr, "reviewer": sem["reviewer"], "basis": "explicit_complete_text_scope_with_actual_semantic_records", "detail_refs": specific_refs})
        recep = []
        named_scope_receipts = []
        # These source reviewers explicitly include the shared premise prose.
        # Receive those actual declarations instead of mistaking row-only indexes
        # for their complete reading scope. IF L242 has no such receipt here.
        named = {
            "deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md": [(260, "modules/M06/reading-coverage.json", "/current_contract_materials/10/semantic_scope", "All U03-EX rows and shared premise paragraphs explicitly reviewed")],
            "deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md": [(253, "modules/M06/reading-coverage.json", "/current_contract_materials/11/semantic_scope", "All BR/R4-IV rows and shared premise paragraphs explicitly reviewed")],
            "deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md": [(v, "modules/M03/reading-coverage.json", "/specification_reading/20", "Only excluded M10 ranges297–321/399–433; all allocated map/event/movement/dungeon/time/field/fishing comparisons complete") for v in (439, 475, 495, 528)],
            "deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md": [(v, "modules/M02/spec-to-source.json", "/specifications/8/boundary", "Preamble and family notes expressly read; only WP08/LZ110–154 excluded") for v in (56, 201)],
        }
        for line, p, ptr, why in named.get(f["path"], []):
            sem_rs.append([line, line])
            named_scope_receipts.append({"ranges": [[line, line]], "ref": ref(p, ptr), "reason": why, "new_ASM_semantic_review": False})
        fixture_refs = []
        fixture_ranges = []
        for j, fixture in enumerate(read("modules/GCV/fixture-maps.json")["mappings"]):
            if fixture["path"] == f["path"]:
                fixture_refs.append(ref("modules/GCV/fixture-maps.json", f"/mappings/{j}"))
                fixture_ranges += fixture["ranges"]
                recep.append(ref("modules/C00/GCV-increment-reception.json", "/previous_gaps/F002"))
        qualified_reuse = f.get("qualified_reuse_range_union", [])
        if f["path"] in REG_INDEX and f["bucket"] == "original_files":
            j, reg = REG_INDEX[f["path"]]
            if reg.get("primary_review_extent") == "full" and reg.get("REG_comparison_fields_reviewed"):
                full_proofs.append({"ref": ref("modules/REG/original-comparison-joins.json", f"/records/{j}"), "reviewer": reg["primary_reviewer"] + "+REG", "basis": "accepted_fresh_original_to_current_fact_dispositions_not_historical_approval", "primary_evidence": reg.get("primary_evidence")})
            recep.append(ref("modules/C00/REG-final-reception.json", "/actual_parent_reading"))
        if "M05" in f["owner"]:
            recep.append(ref("modules/C00/M05-final-reception.json", "/completion_evidence"))
        if f["path"] in ATTACH_INDEX:
            j, a = ATTACH_INDEX[f["path"]]
            recep.append(ref("modules/C00/effective-attachment-join.json", f"/files/{j}"))
            full_proofs.append({"ref": ref("modules/C00/effective-attachment-join.json", f"/files/{j}"), "reviewer": a["primary_reader"] + "+C00", "basis": "bounded_attachment_rows_and_administrative_layer_separately_disposed"})
        current_fields = [rec for rec in records if rec["review_extent"] == "full_current_semantic_fields"]
        raw_evidence_union = union(sem_rs + f.get("semantic_compared_range_claim_union", []) + qualified_reuse + f.get("inverse_clause_range_union", []) + fixture_ranges)
        effective_union = [[1, f["line_count"]]] if full_proofs and f["line_count"] else raw_evidence_union
        numeric_gaps = subtract([[1, f["line_count"]]], effective_union) if f["line_count"] and not f["binary"] else []
        need_classification = union((f["physical_read_gap_ranges"] or []) + (f["comparison_or_reuse_gap_ranges"] or []) + numeric_gaps)
        categories = collections.defaultdict(list)
        semantic_remaining = []
        fixed = None
        # JSON/TSV fields have their own coordinate system. Do not pretend their
        # entire serialised line range was semantically signed.
        field_mode = bool(current_fields) or (f["bucket"] == "effective_files" and pathlib.Path(f["path"]).suffix in {".json", ".tsv"})
        if need_classification and not f["binary"] and not field_mode and f["path"] != "LICENSE":
            fixed = fixed_lines(f)
            if fixed is not None:
                for a, b in need_classification:
                    for line in range(a, min(b, len(fixed)) + 1):
                        categories[layout_disposition(fixed[line - 1], f["path"])].append([line, line])
                harmless = union([v for k, v in categories.items() if k != "semantic_or_context_text_needs_recorded_disposition"])
                semantic_remaining = subtract(numeric_gaps, harmless)
            else:
                semantic_remaining = numeric_gaps
        elif numeric_gaps and not field_mode:
            semantic_remaining = numeric_gaps
        if full_proofs:
            disposition = "full_text_semantic_disposition_inherited"
            semantic_remaining = []
        elif f["binary"]:
            disposition = "decoded_definition_or_format_scopes_only_native_and_host_limits_preserved"
        elif f["path"] == "LICENSE" and f["bucket"] == "reference_files":
            disposition = "license_documentary_material_excluded_from_game_behavior_denominator"
            semantic_remaining = []
        elif f["path"] == "planning/review-manifest-2026-09-19.md":
            disposition = "historical_manifest_explicitly_excluded_from_current_behavior_review"
            semantic_remaining = []
        elif current_fields:
            disposition = "current_semantic_fields_complete_historical_fields_excluded"
            semantic_remaining = []
        elif field_mode:
            disposition = "bounded_structured_field_projection_not_full_serialized_text"
            semantic_remaining = []  # Unscoped fields are below, not hidden as host absence.
        elif not semantic_remaining and records:
            disposition = "semantic_ranges_joined_with_layout_disposition"
        else:
            disposition = "available_text_has_precise_remaining_semantic_or_context_ranges"
        # Do not elevate native resources, inventories or headers to a full signoff.
        if f["binary"]:
            full_proofs = []
        excluded_dispositions = []
        for remain in f.get("explicit_remaining_scopes", []):
            numeric = []
            for k, v in remain["excluded"].items():
                numeric += ranges(v)
            residual = subtract(numeric, effective_union)
            if fixed is not None:
                residual = subtract(residual, [v for k, v in categories.items() if k != "semantic_or_context_text_needs_recorded_disposition"])
            excluded_dispositions.append({"ref": remain["ref"], "reviewer": remain["reviewer"], "original_exclusion": remain["excluded"], "residual_numeric_ranges_after_other_reviewers_or_exact_reuse": residual, "disposition": "no_nonempty_exclusion" if not any(remain["excluded"].values()) else ("named_scope_exclusion_preserved_native_or_other_domain_not_global_unread" if not numeric else ("covered_by_recorded_other_review_or_reuse_or_layout" if not residual else "see_file_remaining_scope_and_owner_evidence"))})
        row = {
            "file_id": "ASM-FILE-" + hashlib.sha256((f["version"] + ":" + f["path"]).encode()).hexdigest()[:20],
            "path": f["path"], "version": f["version"], "git_blob": f["git_blob"], "bucket": f["bucket"], "owners": f["owner"], "line_count": f["line_count"], "binary": f["binary"],
            "normalized_ref": ref("modules/GCV/normalized-file-and-range.json", f"/files/{i}"),
            "disposition": disposition, "whole_native_semantic_full": False,
            "original_physical_gap_ranges": f["physical_read_gap_ranges"], "original_comparison_gap_ranges": f["comparison_or_reuse_gap_ranges"],
            "original_physical_read_union": f["actual_physical_read_range_union"], "current_explicit_read_range_union": union(physical_current),
            "recorded_semantic_or_inverse_range_union": raw_evidence_union, "qualified_reuse_range_union": qualified_reuse,
            "gap_layout_inspection": {"method": "fixed-object classification only; no new source behavior review", "version": f["version"], "ranges_by_kind": {k: union(v) for k, v in categories.items() if v}, "no_copied_source_text": True},
            "full_text_evidence": full_proofs, "recorded_review_scopes": records, "reception_refs": recep,
            "remaining_semantic_or_context_ranges": semantic_remaining,
            "remaining_is_available_material_not_missing_host": bool(semantic_remaining),
            "structured_field_scope_refs": [rec["ref"] for rec in current_fields],
            "accepted_fixture_refs": fixture_refs,
            "named_scope_receipts": named_scope_receipts,
            "structured_field_scope_descriptors": [{"ref": rec["ref"], "fields": {k: v for k, v in deref(rec["ref"]).items() if k in {"field_scope", "json_pointer", "substantive_fields_reviewed", "semantic_scope", "actual_read", "semantic_ranges", "not_reviewed_ranges", "unreviewed_ranges", "unreviewed_scope", "excluded_as_semantic_proof"}}} for rec in records if field_mode and isinstance(deref(rec["ref"]), dict)],
            "structured_unscoped_fields_not_inferred_reviewed": field_mode,
            "excluded_scope_dispositions": excluded_dispositions,
            "authority": "ASM_draft_for_parent_acceptance_only", "formal_support_is_separate": True,
        }
        if f["path"] in ATTACH_INDEX:
            row["attachment_disposition"] = ATTACH_INDEX[f["path"]][1]["recommended_file_disposition"]
        if f["bucket"] == "effective_files":
            row["fixed_historical_or_current_context_identity_preserved"] = True
        if f["path"] in {"animmaker.exe", "extendtext.exe", "soundfont.sf2", "Game.exe"} or f["path"].startswith("Fonts/"):
            row["resource_scope_boundary"] = "Use actual decoded fields/methods/sample relationships and their exclusions. Full PE/header/bytes, font metadata or symbol strings do not certify native algorithms, selection, rendering or audio output."
        if f["binary"]:
            resource_states = {
                "Data/Scripts.rxdata": "Decoded 49-line loader definition reviewed; its current contract remains missing_required under GR5-M12-001. No execution credit.",
                "Data/messages_core.dat": "Fixed decoded31-domain container and18 nonempty corpora content reviewed by M01; the real consumer and corpus-semantic scopes remain separate named M01 rows.",
                "Game.exe": "BIN completed assigned recoverable plaintext definitions, shaders, mappings, dictionaries and candidate dispositions. Native machine-code algorithms and actual branch/host selection remain outside that completion.",
                "animmaker.exe": "RES completed all15 managed-method definitions and metadata scope; filesystem/runtime output and external Rectangle.Empty/encoding/cleanup qualification follow root-RES/CRES.",
                "extendtext.exe": "RES completed named window predicates, single-instance/main loop and import-thunk projection; full CRT/exception/native Windows effect and process binding are not signed.",
                "soundfont.sf2": "M12/RES completed stored SF2 fields, PCM points and static selection/layer relations; synthesizer acceptance, modulation-default interpretation and actual sound remain qualified.",
                "knownpoint.bmp": "M12 full8×8 pixel content and consumer projection complete; host display is separate.",
                "selpoint.bmp": "M12 full8×8 pixel content and consumer projection complete; host display is separate.",
                "x64-msvcrt-ruby310.dll": "Metadata/import/interface projection only; no full native machine-code semantic reading or host-execution signoff.",
                "zlib1.dll": "Metadata/import/interface projection only; no full native machine-code semantic reading or host-execution signoff.",
            }
            row["resource_definition_or_format_disposition"] = resource_states.get(f["path"], "M12 complete recorded cmap/metrics/encoded-glyph relationships; unencoded glyph internals, hinting/bytecode, native font selection and rendered metrics remain qualified.")
            row["resource_definition_evidence_refs"] = [x["ref"] for x in records]
        results.append(row)
        if f["physical_read_gap_ranges"] or f["comparison_or_reuse_gap_ranges"]:
            flagged.append({"file_id": row["file_id"], "path": f["path"], "disposition": disposition, "remaining_ranges": semantic_remaining})
    save("file-dispositions.json", {"schema_version": "gr5.asm.file-dispositions.v1", "files": results, "counts_by_bucket": dict(collections.Counter(x["bucket"] for x in results)), "flagged_gap_files": flagged})
    return results


def build_semantic_index():
    entries = []
    for i, sem in enumerate(SEM["records"]):
        rr = file_record_ref(sem["input_ref"], sem["path"])
        raw = deref(rr)
        if not isinstance(raw, dict):
            raw = {}
        entries.append({"semantic_record_id": sem["semantic_record_id"], "normalized_ref": ref("modules/GCV/normalized-semantic-records.json", f"/records/{i}"), "current_record_ref": rr, "reviewer": sem["reviewer"], "source_path": sem["path"], "coordinate_system": sem["coordinate_system"], "snapshot_extent": sem.get("review_extent_claim"), "current_extent": raw.get("review_extent", raw.get("read_level", sem.get("review_extent_claim"))), "current_completion_scope_ref": ref(f"modules/{sem['reviewer']}/progress.json") if (ROOT/f"modules/{sem['reviewer']}/progress.json").exists() else None, "old_owner_progress_not_current_completion": True, "correction_refs": [ref("normalization-corrections.json", "/corrections/0")] if sem["reviewer"] == "M12B" and "EditorScreens" in sem["path"] else []})
    save("semantic-index.json", {"schema_version": "gr5.asm.semantic-index.v1", "records": entries, "count": len(entries), "no_new_semantic_reading_credit": True})


def main():
    save("progress.json", {"module": "ASM", "complete": False, "status": "building_finite_draft", "updated_at": STAMP, "model_request": {"model": "gpt-6-astra", "effort": "ultra", "service_tier": "default", "Fast": "forbidden", "actual_echo": "UNVERIFIED"}})
    matrix, projections = build_matrix()
    routes = build_inverse()
    files = build_files()
    build_semantic_index()
    same = []
    reasons = [
        "Follower container migration, bag cursor/registered-item migration, player/Pokédex migration and markings packing have different target state, predicates and compatibility inputs. Equal broad conversion-file coordinates do not make their four behaviors equivalent.",
        "Town-map page selection/coordinate/edit state differs from text import/export grammar, reset-before-parse failure and CRLF output. Sharing the same HTML/source range does not merge these workflows.",
    ]
    for i, group in enumerate(ROOTMAP["same_source_scope_candidates_not_merged"]):
        same.append({**group, "ASM_disposition": "retain_separate_scope_ids", "reason": reasons[i], "evidence_refs": [SCOPE_BY_ID[m["proposed_root_id"]]["input_ref"] for m in group["members"]]})
    save("identity-aliases.json", {"schema_version": "gr5.asm.identity-aliases.v1", "same_source_scope_decisions": same, "aliases": [{"scope_id": row["scope_id"], **row["ownership_and_alias"]} for rows in matrix.values() for row in rows], "JXN": {"expected_shared_identities": 97, "expected_domain_routes": 182, "state": "pending_parent_final_delta", "no_ASM_substitute_JXN_adjudication": True}, "join_rule": "Join module/local_id/input_ref/scope_id/declared shared aliases, preserving predicates and consumer boundaries; never equate identical paths/ranges alone."})
    # Preserve accepted finite findings/subscopes so no broad partial row invents
    # a mandatory revision. Copies contain review facts, never reference source.
    save("accepted-overlays.json", {"schema_version": "gr5.asm.accepted-overlays.v1", "coverage_adjudications": ADJ, "canonical_findings": FINDINGS, "M02_reception": ref("modules/C00/M02-followup-reception.json"), "M02_records": [{"ref": ref("modules/M02/followup-partial-dispositions.json", f"/records/{i}"), "id": x["id"], "subranges": [{"ref": ref("modules/M02/followup-partial-dispositions.json", f"/records/{i}/subranges/{j}"), "id": y["id"], "status": y["status"], "final_finding": y.get("final_finding"), "policy_boundary": y.get("policy_boundary")} for j, y in enumerate(x["subranges"])]} for i, x in enumerate(M02["records"])], "normalization_corrections": CORRECTIONS, "M08_correction": ref("modules/M08/source-to-spec.json", "/effective_parent_corrections/0"), "pending": ["M01 finite60 final parent reception", "JXN 97/182 final parent reception"], "stale_pending_in_root_coverage_adjudications_superseded_only_for": ["M02 by C00/M02-followup-reception", "REG by C00/REG-final-reception"]})
    for item in FIELDS.values():
        r = item["ref"]
        if r["path"] == "modules/M12B/reading-coverage.json" and r["pointer"] == "/records/0/semantic_ranges/5/rules":
            item["effective_value"] = item["value"].replace("forms99", "form input 0–999 (ability-index input remains0–99)")
            item["effective_value_authority"] = ref("normalization-corrections.json", "/corrections/0")
            item["original_value_is_superseded_for_form_upper_bound"] = True
        if r["path"] == "modules/M08/source-to-spec.json" and r["pointer"].endswith("/unknowns"):
            item["historical_progress_field_not_current_unread_obligation"] = True
            item["current_completion_ref"] = ref("modules/M08/reading-coverage.json", "/strict_review_interpretation")
        if r["path"] == "modules/M01/source-to-spec.json" and r["pointer"] == "/capabilities/111/not_reviewed":
            item["historical_progress_field_not_current_unread_obligation"] = True
            item["current_disposition_ref"] = ref("modules/M01/source-to-spec.json", "/capabilities/111/current_contract_comparison")
    save("evidence-fields.json", {"schema_version": "gr5.asm.evidence-fields.v1", "pointer_base": str(ROOT.relative_to(REPO)), "fields": FIELDS, "interpretation": "Exact field values from actual review records. Where an accepted effective_value is present it takes precedence over the preserved historical value. Historical progress fields do not become current unread obligations. A bounded rule context may contain several conditions: use its original source coordinates, not a blanket transfer to neighboring rules. Indexing does not certify premise/caller exhaustiveness."})
    save("field-gaps.json", {"schema_version": "gr5.asm.field-gaps.v1", "gaps": GAPS, "count": len(GAPS), "meaning": "Precise missing separately-recorded field disposition in this finite join; not a new source finding or evidence the feature/source is absent."})
    save("M05-pointer-relocations.json", {"schema_version": "gr5.asm.pointer-relocations.v1", "reception_ref": ref("modules/C00/M05-final-reception.json"), "relocations": unique(RELOCATIONS), "rule": "Current M05 file paths identify the document. Inverse units retain their GCV identity and receive current overlapping sections without claiming equal array ordinals or identical unit partition."})
    scope_rows = [r for rows in matrix.values() for r in rows]
    field_ref_errors = []
    for fid, item in FIELDS.items():
        try:
            if resolve(item["ref"]) != item["value"]:
                field_ref_errors.append({"field_id": fid, "ref": item["ref"], "error": "retained_value_does_not_match_current_pointer"})
        except (KeyError, IndexError, ValueError, FileNotFoundError) as e:
            field_ref_errors.append({"field_id": fid, "ref": item["ref"], "error": str(e)})
    ERRORS.extend(field_ref_errors)
    checks = {
        "1460_audit_scopes": len(scope_rows) == 1460,
        "1460_unique_scope_ids": len({r["scope_id"] for r in scope_rows}) == 1460,
        "1295_projections": len(projections) == 1295,
        "every_projection_has_parent_identity": all(p["parent_scope_ids"] for p in projections),
        "all_parent_scope_ids_exist": all(p in SCOPE_BY_ID for x in projections for p in x["parent_scope_ids"]),
        "39_M01_routing_rows": len(routes) == 39,
        "M01_routing_destinations_exist": all(x["target_scope_ids"] for x in routes),
        "M01_routing_actual_domain_receivers_exist": all(x["actual_domain_destinations"] for x in routes),
        "723_file_identities_preserved": len(files) == 723,
        "432_131_113_47_denominators": dict(collections.Counter(x["bucket"] for x in files)) == {"reference_files": 432, "formal_files": 131, "original_files": 113, "effective_files": 47},
        "standard_scope_statuses": all(r["status"] in {"supported", "partial", "missing", "unresolved", "not_reviewed"} for r in scope_rows),
        "text_full_has_specific_evidence": all(x["full_text_evidence"] for x in files if x["disposition"] == "full_text_semantic_disposition_inherited"),
        "native_full_never_inferred": all(not x["whole_native_semantic_full"] for x in files),
        "two_same_source_candidates_not_merged": len(same) == 2,
        "M02_37_finite_subranges_retained": sum(len(x["subranges"]) for x in M02["records"]) == 37,
        "all_input_refs_resolve": not ERRORS,
        "all_retained_field_values_match_exact_current_pointers": not field_ref_errors,
        "every_scope_has_source_anchors_including_explicit_missing_material": all(r["source_anchors"] for r in scope_rows),
        "every_scope_has_specification_anchors": all(r["specification_anchors"] for r in scope_rows),
    }
    save("validation.json", {"schema_version": "gr5.asm.validation.v1", "complete": True, "passed": all(checks.values()), "checks": checks, "errors": ERRORS, "counts": {"scope_rows": len(scope_rows), "projections": len(projections), "inverse_units": len(INV["inverse_units"]), "semantic_records": len(SEM["records"]), "file_records": len(files), "status_counts": dict(collections.Counter(r["status"] for r in scope_rows)), "field_gap_count": len(GAPS), "field_gaps_by_field": dict(collections.Counter(g["field"] for g in GAPS)), "file_dispositions": dict(collections.Counter(f["disposition"] for f in files)), "files_with_remaining_semantic_ranges": sum(bool(x["remaining_semantic_or_context_ranges"]) for x in files)}, "validation_scope": "Finite artifact identity/reference/range/status checks only; no behavior execution, no global semantic certification", "unique_product_capability_count": None, "pending_parent_reception": ["M01 finite60", "JXN 97 shared identities /182 domain routes"]})
    save("matrix-draft.json", {"schema_version": "gr5.asm.matrix-draft.v1", "created_at": STAMP, "module": "ASM", "complete": True, "acceptance_state": "draft_for_parent_only", "specification_baseline": B5, "reference_baseline": R, "model_request": {"model": "gpt-6-astra", "reasoning_effort": "ultra", "service_tier": "default", "Fast": "forbidden"}, "actual_runtime_echo": {k: "UNVERIFIED" for k in ("model", "reasoning_effort", "service_tier", "Fast")}, "scope_shards": [{"path": f"modules/ASM/matrix-{m}.json", "pointer": "/rows", "count": len(rows)} for m, rows in sorted(matrix.items())], "counts": {"stable_audit_scope_rows_not_product_features": 1460, "projection_rows": 1295, "inverse_units": 25704, "semantic_records": 3849, "files": 723, "unique_product_feature_count": None}, "artifacts": ["projection-draft.json", "inverse-index.json", "semantic-index.json", "evidence-fields.json", "field-gaps.json", "owner-routing.json", "identity-aliases.json", "file-dispositions.json", "accepted-overlays.json", "delta-join-report.md", "validation.json"], "field_contract": "All scopes expose required fields; explicit missing field dispositions remain exact gaps, not fabricated no-condition statements. Field values are resolved through evidence-fields.json /fields/<id> with original file/pointer.", "execution_counts": {"reference": 0, "behavior_model": 0, "host_or_demo": 0}, "pending_final_deltas": ["M01 finite60 parent reception", "JXN 97 identities /182 routes parent reception"], "global_matrix_written": False, "global_review_complete": False})
    residuals = [x for x in files if x["remaining_semantic_or_context_ranges"]]
    gap_counts = collections.Counter(g["field"] for g in GAPS)
    report = [
        "ASM 有限整合草案已完成；这里只完成本次接收与定位工作，不代表全局矩阵获批、规格全支持或全部最后增量已收齐。所有输出位于 modules/ASM/，未写根矩阵、源、规格或其他审者文件；未启动其他任务，未执行参考、行为模型或宿主。",
        "",
        "入口是 matrix-draft.json；按领域分片的 matrix-*.json 共1460个稳定审计 scope，绝非1460个独立产品功能。projection-draft.json 保留1295个投影，inverse-index.json 保留25704个逆向单位，semantic-index.json 保留3849个语义记录身份。723个文件保留432 R、131 formal、113 original、47 context的原分母和固定历史版本。",
        "",
        "每个范围均有目的、领域、源/规格锚点、caller/override、前提、配置/宿主、实际审查范围、标准status及理由、审者/证据、发现、依赖和未知字段。具体事实由 evidence-fields.json 中的字段值与原文件/JSON pointer承接；来源为原始能力记录、同审者且范围重叠的具名语义段、明确登记ID、共享合同和已接受有限处置。相邻范围的规则上下文不自动成为该行每个条件。主审完整声明与规格supported/partial/missing/unresolved/not_reviewed分开。",
        "",
        f"字段定位仍保留{len(GAPS)}项：" + "，".join(f"{k}={v}" for k, v in sorted(gap_counts.items())) + "。这些是本有限接收中未单独具名或仅有通用声明的字段定位，并非对应源未审或功能缺失判决；不能把列数当行为缺陷数。field-gaps.json逐项给scope、原始pointer、已查语义记录与草案字段位置。既有规则正文完整保留，未用统一‘无附加条件’补空。",
        "",
        "已接收的后继证据：M05最终38个能力记录与当前分段、C00/BIN的6个条件父映射及909个精确候选定义连接、M08的原稿差异/精确复用及Shadow参数纠正、M02的6条/37子范围和006–008规范发现、REG的113原稿比较与最终接收、10个有效附件以及0–999形态上界纠正。root的33条有限处置逐项按(module, local_id)接入，旧root pending仅M02/REG由相应C00回执替代。",
        "",
        f"发现并处理M05快照指针漂移：{len(unique(RELOCATIONS))}个不同旧/新pointer连接记录见 M05-pointer-relocations.json。按实际文件路径匹配当前记录；旧逆向单元可能对应当前多个更细分段，保留旧单位身份而不假装数组下标或分段不变。",
        "",
        "39条M01责任路由明确连接原capability_refs与247字段合同中的对应记录；仅证明责任路由，不取得行为支持分数。5条RES范围投影到M12-ROOT-21/22/23/24/25，保留新格式/定义证据和运行边界。M10图鉴外域行保留自身not_reviewed签名，同时明确投影到已完成M11主审，不形成全局图鉴未审结论。M11的47条宽partial另列具名005子范围接收：只有匹配时序/谓词部分接必修，资源/图集/布局可选或无必修部分不扩张为整个源范围必修。",
        "",
        "两个same_source_scope候选均不合并：四类迁移改变不同状态并具有不同兼容条件；区域地图页面交互与文本导入/导出是不同工作流。1295投影都有实际父身份；M12B root-tools一行仅责任导航，其余使用具名或条件化父连接。identity-aliases.json保留module/local_id/input_ref/scope_id/shared aliases，供父会话接JXN，未替代JXN裁决。",
        "",
        "file-dispositions.json逐文件保留旧物理缺口、比较缺口、当前实审范围、精确复用、字段坐标、限定排除与接收证据。88个旧物理gap文件均有处置。空白、Markdown标题/列头、静态/历史证据资格与真正夹具前提分开；M04 assigned_semantic_ranges、M06明示shared premises、M02家族注释、M03分配范围和GCV13夹具/67边均按实际记录承接。LICENSE与历史manifest不伪签游戏正文，JSON字段审查不伪签全序列化行。资源分别保留完整已解码定义/格式和native/host限制，不以header签full。",
        "",
        "剩余可得语义/上下文范围：",
    ]
    if residuals:
        for f in residuals:
            report.append(f"- `{f['path']}` {f['remaining_semantic_or_context_ranges']}：本草案没有找到覆盖这些具体段的主审接收记录，标为精确接收缺口；材料可得，不归缺宿主。详见该文件的 recorded_review_scopes 与 excluded_scope_dispositions。")
    else:
        report.append("本有限文件接收没有剩余数值化可得文本语义范围；这不解除结构字段范围之外、native/host以及最终delta资格。")
    report += ["", "M01的60项最后处置与JXN的97共享身份/182领域路由仍为 pending_parent_final_delta；没有读取未接受增量来伪造完成，也不等待它们阻塞本草案。父会话唯一负责根矩阵写入。", "", "validation.json仅校验固定分母、稳定身份、父连接、字段引用值、文件范围和状态词；不充当语义重审或行为测试。模型/推理档位/service tier/Fast实际回显均UNVERIFIED。"]
    (OUT / "delta-join-report.md").write_text("\n".join(report) + "\n")
    save("progress.json", {"module": "ASM", "complete": all(checks.values()), "status": "finite_draft_complete_for_parent_acceptance" if all(checks.values()) else "finite_validation_fix_required", "updated_at": STAMP, "model_request": {"model": "gpt-6-astra", "effort": "ultra", "service_tier": "default", "Fast": "forbidden", "actual_echo": "UNVERIFIED"}, "outputs": ["matrix-draft.json", "file-dispositions.json", "delta-join-report.md", "validation.json"], "pending_parent_final_delta": ["M01 finite60", "JXN 97/182"], "global_review_complete": False, "new_execution": {"reference": 0, "behavior_model": 0, "host_or_demo": 0}})
    print(json.dumps({"checks": checks, "errors": ERRORS[:12], "field_gaps": dict(collections.Counter(g["field"] for g in GAPS)), "file_dispositions": dict(collections.Counter(f["disposition"] for f in files)), "remaining_files": [{"path": f["path"], "ranges": f["remaining_semantic_or_context_ranges"]} for f in files if f["remaining_semantic_or_context_ranges"]]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
