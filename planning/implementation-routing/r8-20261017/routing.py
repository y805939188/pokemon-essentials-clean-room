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
ROOT = HERE.parents[2]
FORMAL = "deliverables/final-specification-set/"
B8 = "fd1df570cad987dc3852a3b958f03916e317f7fe"
DELIVERY = "4575e80d041ab0c74a42e2e36399d05791dbaa5b"
REPORT = "review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/"
INDEX = REPORT + "tasks/inventory_denominator/formal-inventory.json"
WP_INDEX = REPORT + "coverage/wp-final-coverage.json"
BATCH_INDEX = REPORT + "handoff/batch-assignment.json"
REPO_URL = "https://github.com/y805939188/pokemon-essentials-clean-room/blob/"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


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


def seed():
    target = HERE / "routing-manifest.json"
    if target.exists():
        raise ValueError("Refuse to reseed existing IDs; edit manifest and retain original source locators")
    policy = read_json(HERE / "routing-policy.json")
    assigned = {}
    for key, names in policy["document_groups"].items():
        for name in names:
            if name in assigned:
                raise ValueError(f"Duplicate document profile: {name}")
            assigned[name] = key
    index, wp, batches = fixed_inputs()
    docs, features, coverage = [], [], []
    next_id = 1
    for item in sorted(index, key=lambda x: x["path"]):
        path = item["path"]
        data = blob(B8, path)
        if item["sha256"] != digest(data) or item["git_blob"] != git("rev-parse", f"{B8}:{path}").decode().strip():
            raise ValueError(f"Index identity mismatch: {path}")
        hs, lines = headings(data)
        stem = Path(path).stem
        shared = path in [FORMAL + "README.md", FORMAL + "scope-statement.md", FORMAL + "test-catalog/README.md"]
        catalog = "/test-catalog/" in path and not shared
        key = None if shared or catalog else assigned.pop(stem, None)
        if not shared and not catalog and key is None:
            raise ValueError(f"No explicit document profile: {path}")
        wps, deps, upstream = doc_bindings(path, wp, batches)
        ident = identity(B8, path)
        doc = {"document_id": f"DOC-{len(docs) + 1:04}", "source": ident,
               "document_role": "shared-governance" if shared else "test-design" if catalog else "behavior-or-data",
               "source_classification": next((l.strip() for l in lines if l.startswith("分类：")), "共享导航、范围或测试设计；无独立实现承诺"),
               "wp_refs": wps, "dependency_wp_refs": deps, "profile": key,
               "upstream": upstream, "feature_ids": [],
               "current_applicability": {"snapshot_commit": DELIVERY, "path": path, "identity": ident,
                                         "source_equivalence": "SAME_BYTES", "status": "固定基线粗标"},
               "semantic_reading": "正文入口、行为章节及混合边界抽读；不声称逐条全文语义审查"}
        nodes = []
        overrides = [o for o in policy["section_overrides"] if o["document"] == stem]

        def choose(h):
            selected = {"profile": key}
            matches = []
            for o in overrides:
                sec = h.get("section") or ""
                if o["section"] == "*" or sec == o["section"] or sec.startswith(o["section"] + "."):
                    matches.append(o)
            for o in sorted(matches, key=lambda x: len(x["section"])):
                selected.update(o)
            return selected

        if key:
            for h in hs:
                if h["level"] == 2 and not any(re.search(p, h["title"]) for p in policy["metadata_heading_patterns"]):
                    nodes.append((h, choose(h)))
            if not nodes:
                nodes.append((hs[0], choose(hs[0])))
            for o in overrides:
                if o["section"] == "*":
                    continue
                exact = [h for h in hs if h["section"] == o["section"]]
                if not exact:
                    raise ValueError(f"Override points to absent section: {stem} {o['section']}")
                h = exact[0]
                if h["level"] <= 2:
                    continue
                parent_nodes = [(n, c) for n, c in nodes if n["line_start"] <= h["line_start"] <= n["line_end"]]
                if not parent_nodes:
                    continue
                _, parent_choice = max(parent_nodes, key=lambda x: x[0]["level"])
                parent_prof = policy["profiles"][parent_choice["profile"]]
                new_choice = choose(h)
                prof = policy["profiles"][new_choice["profile"]]
                if (prof["route"], new_choice.get("scope", prof["scope"]), new_choice.get("prototype")) != (
                        parent_prof["route"], parent_choice.get("scope", parent_prof["scope"]), parent_choice.get("prototype")):
                    nodes.append((h, new_choice))
            for h, choice in sorted(nodes, key=lambda x: x[0]["line_start"]):
                prof = policy["profiles"][choice["profile"]]
                children = [(n["line_start"], n["line_end"]) for n, c in nodes
                            if n["level"] > h["level"] and h["line_start"] < n["line_start"] <= h["line_end"]]
                ranges = subtract_range(h["line_start"], h["line_end"], children)
                fid = f"FR-{next_id:06}"
                next_id += 1
                source = {"commit": B8, "document": path, "heading": h["title"], "anchor": h["anchor"],
                          "heading_level": h["level"], "heading_sha256": h["heading_sha256"],
                          "line_ranges": ranges, "unit_sha256": digest("".join("".join(lines[a - 1:b]) for a, b in ranges).encode()),
                          "file_sha256": ident["sha256"], "file_git_blob": ident["git_blob"],
                          "fact_excerpt": excerpt(lines, ranges), "evidence_type": "SOURCE_SPECIFICATION_ONLY"}
                scope = choice.get("scope", prof["scope"])
                proto = choice.get("prototype")
                decisions = ["DEC-ROUTING-VERIFY", "DEC-PHASE-SCOPE"]
                if scope == "待决策":
                    decisions.append("DEC-SPECIAL-AND-HOST-SCOPE")
                if prof["route"] in ["showdown", "cooperation"] or proto:
                    decisions.append("DEC-SHOWDOWN-VERSION-FORMAT")
                features.append({
                    "feature_id": fid, "name": f"{hs[0]['title']} / {h['title']}",
                    "document_id": doc["document_id"], "source": source,
                    "current_applicability": {"snapshot_commit": DELIVERY, "document": path,
                        "source_state": "固定基线来源合同", "status": "待整改后核对" if upstream["batches"] else "固定基线粗标",
                        "target_scope": scope, "source_classification": doc["source_classification"]},
                    "future_plan": {"destination": policy["route_labels"][prof["route"]],
                        "partners": prof["partners"], "proposal_status": "建议待验证",
                        "rationale": choice.get("reason", prof["rationale"]),
                        "questions": prof["questions"], "prototype_refs": [proto] if proto else [],
                        "stage": "待定", "stage_approval": "未批准", "exclusion_decision": None},
                    "destination_verification": {"status": "待验证", "evidence": [], "source_only_is_compatibility_evidence": False},
                    "implementation": {"status": "未实现", "acceptance_status": "未验收", "evidence": []},
                    "dependencies": {"wp_refs": deps, "document_wp_refs": wps, "feature_refs": []},
                    "differences": ["来源规格事实与未来实现政策分别处理；既有异常/兼容差异待用户及原型判定。"],
                    "decision_refs": sorted(set(decisions)), "upstream": copy.deepcopy(upstream)})
                doc["feature_ids"].append(fid)
                h["feature_id"] = fid
        for h in hs:
            owning = [(n, c) for n, c in nodes if n["line_start"] <= h["line_start"] <= n["line_end"]]
            direct = max(owning, key=lambda x: x[0]["level"])[0].get("feature_id") if owning else None
            coverage.append({"document_id": doc["document_id"], "path": path,
                             **{k: h[k] for k in ["level", "title", "anchor", "line_start", "line_end", "heading_sha256"]},
                             "mapping_kind": "behavior-unit" if direct else "section-metadata",
                             "feature_refs": [direct] if direct else list(doc["feature_ids"]),
                             "related_wp_refs": wps,
                             "metadata_reason": None if direct else "本节保留来源范围、术语、配置、测试或证据边界；通过本篇/同WP功能行消费，不伪造独立功能。"})
        docs.append(doc)
    if assigned:
        raise ValueError(f"Profiles for absent formal documents: {sorted(assigned)}")
    # Catalog/shared metadata link to actual same-WP behavior rows, never synthetic implementation rows.
    doc_by_id = {d["document_id"]: d for d in docs}
    for c in coverage:
        d = doc_by_id[c["document_id"]]
        if c["mapping_kind"] == "section-metadata" and not c["feature_refs"]:
            own_wp = set(c["related_wp_refs"])
            c["feature_refs"] = [f["feature_id"] for f in features
                                 if own_wp.intersection(f["dependencies"]["document_wp_refs"])]
            if not c["feature_refs"]:
                c["metadata_reason"] += " 此项为全集治理/证据元数据，关联功能全集，由coverage_scope指示。"
                c["coverage_scope"] = "ALL_FORMAL_FEATURES"
    manifest = {
        "schema_version": "implementation-routing.v1", "status": "BASELINE_COARSE_CANDIDATE",
        "source_baseline": {"commit": B8, "formal_tree": git("rev-parse", f"{B8}:{FORMAL.rstrip('/')}").decode().strip(),
                            "delivery_commit": DELIVERY, "index": identity(DELIVERY, INDEX),
                            "wp_index": identity(DELIVERY, WP_INDEX)},
        "current_snapshot": {"commit": DELIVERY, "formal_tree": git("rev-parse", f"{DELIVERY}:{FORMAL.rstrip('/')}").decode().strip(),
                             "upstream_calibration": "AWAITING_UPSTREAM_CALIBRATION"},
        "count_policy": "分母由固定索引和实际Git树计算；历史131文档/87WP仅核对，不作为硬编码约束。",
        "decisions": [
            {"id": "DEC-ROUTING-VERIFY", "status": "待决策", "question": "逐章节确定承载职责；本候选不证明目标实现支持。", "authority": "用户去向打标授权；最终去向待验证"},
            {"id": "DEC-PHASE-SCOPE", "status": "待决策", "question": "确定首版/后续范围及阶段；当前没有首版全面批准。", "authority": "用户未全面批准首版范围"},
            {"id": "DEC-SPECIAL-AND-HOST-SCOPE", "status": "待决策", "question": "确定Shadow、特殊模式、小游戏、调试/编辑工具、XP工程迁移及旧格式支持范围。", "authority": "只能由用户明确范围决定排除"},
            {"id": "DEC-SHOWDOWN-VERSION-FORMAT", "status": "待决策", "question": "固定Showdown源commit、规则世代/格式、配置和差异政策，再开展原型及行为验证。", "authority": "尚无固定目标版本或原型证据"}],
        "prototypes": [
            {"id": "PROTO-CAPTURE", "status": "未运行", "checks": ["菜单/目标许可、登记扣球与取消", "随机消费、目标移除、经验触发及终局", "接收队列、图鉴/命名/队伍/盒子、还原、异常前缀"]},
            {"id": "PROTO-BATTLE-ITEM", "status": "未运行", "checks": ["NPC资源与玩家背包区分、目标/效果家族", "登记扣物、执行复检、退款残留、再次撤销及容量异常", "状态写穿、行动占用、下一命令与终局清理"]},
            {"id": "PROTO-ESCAPE", "status": "未运行", "checks": ["查询/尝试/强制入口差异、拘束与必逃", "尝试计数、随机消费、失败行动占用", "原始结果、世界包装返回、漫游持久与终局还原"]},
            {"id": "PROTO-IN-BATTLE-GROWTH", "status": "未运行", "checks": ["经验/EV接收、逐级升级及HP/能力/PP刷新", "学招暂停、替换/放弃、继续回合", "捕获成长、Shadow暂存、战后进化与异常前缀"]}],
        "documents": docs, "features": features}
    save_json(target, manifest)
    save_json(HERE / "section-coverage.json", {"schema_version": "routing-section-coverage.v1", "source_commit": B8,
                                                "coverage_claim": "ALL_PARSED_HEADINGS_MAPPED; NOT_FULL_SEMANTIC_REVIEW", "sections": coverage})
    save_json(HERE / "accepted-source-updates.json", {"schema_version": "routing-accepted-source-updates.v1", "events": [],
        "state": "AWAITING_UPSTREAM_CALIBRATION", "instruction": "协调方提供实际ACCEPTED提交、批次、受影响全文差分与精确验收回执后逐项回填；保留source历史定位。"})


def errors(manifest, coverage):
    import jsonschema
    found = []
    schema = read_json(HERE / "routing-manifest.schema.json")
    found += [f"schema:{'/'.join(map(str, e.path))}: {e.message}" for e in
              jsonschema.Draft202012Validator(schema).iter_errors(manifest)]
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
            for a, b in s["line_ranges"]:
                if a < selected["line_start"] or b > selected["line_end"] or a > b:
                    found.append(f["feature_id"] + ": invalid source range")
                nums = set(range(a, b + 1))
                if occupied.intersection(nums):
                    found.append(f["feature_id"] + ": overlapping functional source units")
                occupied.update(nums)
            unit = "".join("".join(lines[a - 1:b]) for a, b in s["line_ranges"]).encode()
            if digest(unit) != s["unit_sha256"] or s["file_sha256"] != d["source"]["sha256"]:
                found.append(f["feature_id"] + ": immutable source unit hash mismatch")
    declared = [(c["path"], c["line_start"], c["anchor"], c["heading_sha256"]) for c in coverage["sections"]]
    if sorted(actual_headings) != sorted(declared) or len(set(declared)) != len(declared):
        found.append("heading coverage has a missing, duplicate or stale source anchor")
    for c in coverage["sections"]:
        if set(c["feature_refs"]) - idset:
            found.append(c["path"] + ": unknown coverage feature ID")
        if not c["feature_refs"] and c.get("coverage_scope") != "ALL_FORMAL_FEATURES":
            found.append(c["path"] + ": unmapped heading")
    return found


def report(manifest, coverage):
    es = errors(manifest, coverage)
    return {"schema_version": "routing-validation.v1", "result": "PASS_TOOL_VALIDATION" if not es else "FAIL",
            "errors": es, "documents": len(manifest["documents"]), "functional_rows": len(manifest["features"]),
            "headings": len(coverage["sections"]),
            "heading_levels": dict(collections.Counter(str(c["level"]) for c in coverage["sections"])),
            "destinations": dict(collections.Counter(f["future_plan"]["destination"] for f in manifest["features"])),
            "destination_verification": dict(collections.Counter(f["destination_verification"]["status"] for f in manifest["features"])),
            "implementation_stage": dict(collections.Counter(f["future_plan"]["stage"] for f in manifest["features"])),
            "pending_upstream_rows": sum(bool(f["upstream"]["batches"]) for f in manifest["features"]),
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
                current = f"{f['current_applicability']['status']}；快照 `{f['current_applicability']['snapshot_commit']}`；目标范围：{f['current_applicability']['target_scope']}"
                refs = f"WP依赖：{', '.join(f['dependencies']['wp_refs']) or '无独立WP依赖'}；差异：{' '.join(f['differences'])}；决策：{', '.join(f['decision_refs'])}；原型：{', '.join(p['prototype_refs']) or '待设计'}；整改：{', '.join(f['upstream']['batches']) or '无当前已知正式写批'}（{f['upstream']['status']}；整文件保守绑定）"
                cells = [f"{f['feature_id']} / {s['heading']}", source, current,
                         f"{p['destination']}（{p['proposal_status']}）；{' / '.join(p['partners'])}",
                         p["rationale"] + " " + " ".join(p["questions"]), f["destination_verification"]["status"],
                         f"{p['stage']}（{p['stage_approval']}） / {f['implementation']['status']} / {f['implementation']['acceptance_status']}", refs]
                text.append("| " + " | ".join(md_cell(c) for c in cells) + " |")
            text += [""]
        (views / f"{domain}.md").write_text("\n".join(text) + "\n")
    cov_text = ["# 全部正式文档与章节覆盖", "", "所有实际标题的固定定位、映射与哈希见 section-coverage.json。这里按文档汇总；标题覆盖不等于全文语义审查或去向验证。", "", "| 文档 | 角色 | 标题数 | 功能行 | WP | 整改批次 |", "| --- | --- | --- | --- | --- | --- |"]
    counts = collections.Counter(c["document_id"] for c in coverage["sections"])
    for d in manifest["documents"]:
        cov_text.append("| " + " | ".join(md_cell(x) for x in [d["source"]["path"], d["document_role"], counts[d["document_id"]], ", ".join(d["feature_ids"]) or "元数据关联同WP功能/全集", ", ".join(d["wp_refs"]), ", ".join(d["upstream"]["batches"]) or "无当前已知正式写批"]) + " |")
    (HERE / "coverage.md").write_text("\n".join(cov_text) + "\n")
    save_json(HERE / "validation-result.json", result)
    save_json(HERE / "coverage-summary.json", {"schema_version": "routing-coverage-summary.v1", **{k:v for k,v in result.items() if k not in ["errors"]},
        "unmapped_headings": 0, "semantic_reading": "ENTRY_AND_BEHAVIOR_SECTION_EXCERPTS_WITH_TARGETED_BOUNDARY_READING; NOT_FULL_CLAUSE_REVIEW",
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
    check("源单元漂移拒绝", lambda m,c: m["features"][0]["source"].update(unit_sha256="0"*64), "unit hash mismatch")
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
