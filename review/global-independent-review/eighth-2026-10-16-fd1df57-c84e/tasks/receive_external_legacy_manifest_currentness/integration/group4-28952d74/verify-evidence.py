"""Identity and set checks only. Never execute recovered programs or decide semantics."""
from pathlib import Path
import collections
import datetime
import hashlib
import json
import subprocess

TASK = Path(__file__).resolve().parent
REPO = TASK.parents[4]
REVIEW = TASK.parents[1].relative_to(REPO).as_posix()
CONTRACT = "2d44dafe215842de6355f46de7d4d273d8b4c264"
TARGET = "93d7df7f66adcaa25811fd6ff09352b754577af0"
CRE_D = "173c822a14d2fccb28083c24da03bee6b500e7b2"
B8 = "fd1df570cad987dc3852a3b958f03916e317f7fe"
R = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
SPLIT = REVIEW + "/tasks/receive_external_legacy_manifest_currentness/split-contracts/"
MANIFEST = "planning/review-manifest-2026-09-19.md"


def git(*args):
    return subprocess.check_output(["git", "-C", str(REPO), *args])


def raw(commit, path):
    return git("show", commit + ":" + path)


def obj(commit, path):
    return json.loads(raw(commit, path))


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def identity(commit, path):
    data = raw(commit, path)
    meta, actual_path = git("ls-tree", commit, "--", path).decode().rstrip().split("\t")
    mode, kind, blob = meta.split()
    assert actual_path == path and kind == "blob"
    return dict(commit=commit, path=path, mode=mode, blob=blob, bytes=len(data),
                sha256=hashlib.sha256(data).hexdigest())


def check_identity(row, commit=None, path=None):
    found = identity(commit or row["commit"], path or row["path"])
    assert found["mode"] == row["mode"]
    assert found["blob"] == row.get("blob", row.get("git_blob"))
    assert (found["bytes"], found["sha256"]) == (row["bytes"], row["sha256"])
    return found


def write(name, value):
    (TASK / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def main():
    utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    readsets = [obj(CONTRACT, SPLIT + s + ".complete.json") for s in ("S16", "S17", "S18", "S19", "S20")]
    root = readsets[0]
    assert git("rev-parse", B8+"^{tree}").decode().strip() == "751dfde81048c81390f89a65ca1d1a565ba8e1ca"
    assert git("rev-parse", B8+":deliverables/final-specification-set").decode().strip() == "f292698cdd4a8e725525a9be6dc34b75faaf151e"
    assert git("-C", "/workspace/pokemon-essentials", "rev-parse", R+"^{tree}").decode().strip() == "7589c800b61ba13a13040ed0d686979b80a84fd0"
    assert all(x["files"] == root["files"] for x in readsets)
    assert all(x["source_evidence_catalog"] == root["source_evidence_catalog"] for x in readsets)
    events = [e for x in readsets for e in x["events_all_fields"]]
    decisions = json.loads((TASK / "event-decisions.json").read_text())["events"]
    assert [e["id"] for e in events] == [e["id"] for e in decisions]
    assert len(events) == len({e["id"] for e in events}) == 40
    purposes = json.loads((TASK / "input-purposes.json").read_text())["files"]
    assert {r["file"] for r in purposes} == {r["relative_to_target_task"] for r in root["files"]}
    target_identities = [check_identity(r, TARGET, r["remote_path_at_target_commit"]) for r in root["files"]]
    prefix = root["files"][0]["remote_path_at_target_commit"].rsplit("/", 1)[0]
    actual_set = git("ls-tree", "-r", "--name-only", TARGET, "--", prefix).decode().splitlines()
    assert set(actual_set) == {r["path"] for r in target_identities}
    assert git("rev-parse", TARGET + "^{tree}").decode().strip() == root["target_checkout_tree"]
    assert git("rev-parse", TARGET + ":" + prefix).decode().strip() == root["target_task_tree_observed_from_fixed_commit"]

    data = raw(B8, MANIFEST)
    lines = data.splitlines(keepends=True)
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line))
    physical = [r for x in readsets for r in x["physical_line_identities"]]
    paragraphs = [r for x in readsets for r in x["paragraph_dispositions_all_fields"]]
    assert len(physical) == len({r["id"] for r in physical}) == 318
    for r in physical:
        n = r["line"]
        assert (r["byte_start"], r["byte_end"], r["bytes"], r["sha256"]) == (
            offsets[n - 1], offsets[n], len(lines[n - 1]), hashlib.sha256(lines[n - 1]).hexdigest())
    original_dispositions = {r["id"]: r for r in obj(TARGET, prefix + "/purpose-dispositions.json")["units"]}
    assert all(original_dispositions[r["id"]] == r for r in paragraphs)
    original_events = {r["id"]: r for r in obj(TARGET, prefix + "/semantic-purpose-review.v2.json")["units"]}
    assert all(original_events[e["id"]] == e for e in events)

    routes, providers = {}, {}
    for x in readsets:
        for r in x["current_routes_all_fields"]:
            assert r["id"] not in routes or routes[r["id"]] == r
            routes[r["id"]] = r
        for p in x["providers_all_fields"]:
            assert p["id"] not in providers or providers[p["id"]] == p
            providers[p["id"]] = p
    assert len(routes) == 119 and len(providers) == 20
    for r in routes.values():
        check_identity(r["current_formal_identity"])
        check_identity(r["fixed_readset"])
    provider_observations = []
    for p in providers.values():
        selected_events = [e["id"] for e in events if any(
            p["id"] in routes[r]["provider_ids"] for r in e["current_formal_routes"])]
        refs = []
        for f in p.get("fixed_items", []):
            found = check_identity(f)
            value = (dict(jsonl_records=[json.loads(line) for line in raw(f["commit"], f["path"]).splitlines() if line])
                     if f["path"].endswith((".jsonl", ".ndjson")) else obj(f["commit"], f["path"]))
            counts = {k: len(v) for k, v in value.items() if k in ("entries", "records", "jsonl_records") and isinstance(v, list)}
            refs.append({**found, "selected_list_counts": counts, "semantic_read_credit": 0})
        provider_observations.append(dict(id=p["id"], event_ids=selected_events, fixed_items=refs,
            status=("FINITE_SHARED_18_RECORDS_RECEIVED" if p["id"] == "SHARED" else
                    "SUPERSEDED_OLD_ABSENCE_USE_173c822a_FINITE_RECEPTION" if p["id"] == "CRE-D" else
                    "OPEN_CURRENT_DOMAIN_RECEPTION_NOT_INHERITED")))

    batches = [
        ("S16", 131, 134, "c47dbe"), ("S16", 135, 137, "1ac0dc"),
        ("S17", 138, 141, "ddd8cc"), ("S17", 142, 144, "bdaff9"),
        ("S18", 145, 148, "967fc6"), ("S18", 149, 154, "824bd6"),
        ("S19", 155, 159, "1fee51"), ("S19", 160, 164, "f2fbb6"),
        ("S20", 165, 171, "d1338d")]
    frozen_events, reception = [], []
    for event_number, (event, decision) in enumerate(zip(events, decisions)):
        chunks = []
        for start, end in event["line_ranges"]:
            selected = b"".join(lines[start - 1:end])
            chunks.append(dict(lines=[start, end], byte_start=offsets[start - 1], byte_end=offsets[end],
                               bytes=len(selected), sha256=hashlib.sha256(selected).hexdigest()))
        frozen_events.append(dict(id=event["id"], original_ranges=chunks,
            content_paragraph_lines=event["content_paragraph_lines"], current_route_ids=event["current_formal_routes"]))
        batch = next(b for b in batches if b[1] <= event["round"] <= b[2])
        pids = sorted({pid for rid in event["current_formal_routes"] for pid in routes[rid]["provider_ids"]})
        shard_events = next(x["events_all_fields"] for x in readsets if x["id"] == batch[0])
        reception.append({"id":decision["id"], "manual_decision":"event-decisions.json#/events/"+str(event_number), "event_ranges": event["line_ranges"],
            "output_receipt": batch[3], "original_complete_fields": SPLIT + batch[0] + ".complete.json#/events_all_fields/" + str(shard_events.index(event)),
            "actual_successors": event["actual_successor_events"], "current_route_ids": event["current_formal_routes"],
            "provider_ids": pids, "documentary_purpose": "RECEIVED_VERSION_BOUND_MEANING",
            "whole_current_behavior": "NOT_CERTIFIED_BY_THIS_RECOVERY",
            "remaining_current_providers": [p for p in pids if p not in ("SHARED", "CRE-D")]})

    content = [r for r in paragraphs if r["structure"] == "content_paragraph"]
    assert len(content) == 177 and sum(r["bytes"] for r in content) == 141686
    counts = dict(events=40, physical_lines=318, content_paragraphs=177, heading_layout_lines=141,
                  all_selected_bytes=145987, content_bytes=141686, target_files=33, target_bytes=3736917,
                  current_routes_identity_only=119, fixed_provider_routes=20)
    write("frozen-denominator.json", dict(schema="r8-legacy-g4-frozen-scope/v1", utc=utc,
        contract=CONTRACT, target=TARGET, target_checkout_tree=root["target_checkout_tree"],
        target_task_tree=root["target_task_tree_observed_from_fixed_commit"], B8=B8, R=R,
        manifest=identity(B8, MANIFEST), counts=counts, excluded_event="LM-E169 belongs another shard",
        readsets=[identity(CONTRACT, SPLIT + x["id"] + ".complete.json") for x in readsets],
        events=frozen_events, historical_original_thread="01a1448e-1b01-74ff-b293-3c4366072022",
        actual_recovery_thread="01a144ee-4708-7009-b631-eed985e38020", additional_votes=0))
    write("reception-ledger.json", dict(schema="r8-legacy-g4-reception/v1", status="INCOMPLETE",
        documentary_purposes_disposed=40, whole_current_behavior_event_certificates=0,
        parent_final="RESERVED_FOR_PARENT; do not count original plus recovery twice",
        events=reception, business_execution="NOT_EXECUTED", UPDATE_NOT_STARTED=True))
    write("interfaces.json", dict(schema="r8-legacy-g4-current-interface-reception/v1", status="INCOMPLETE",
        providers=provider_observations, shared=dict(commit=CONTRACT,
            authority="30cfed0996003b6ebf4b5c51cc04f31ca9255440:" + REVIEW + "/adjudication/root-primary-formal_shared/forward-mapping.json",
            selected_ids=["FS%02d" % n for n in range(1, 19)], receipt="509b59",
            accepted="历史层/输入批准/当前字节分开；人口不推PASS；源定位不代支持；保全部限词及未决。"),
        CRE_D=dict(commit=CRE_D, path=REVIEW + "/tasks/receive_external_creature_d/",
            fixed_items=[identity(CRE_D, REVIEW+"/tasks/receive_external_creature_d/"+f) for f in
                ("report.md", "continuation-closure.json", "finite-receptions.json", "continuation-fact-receptions.json")],
            full_files_read=["report.md", "continuation-closure.json", "finite-receptions.json"],
            selected_fact_ids=["RX-CD-F%02d" % n for n in (3,6,15,16,17,19,20,21,22,23,28,29,30,35,36,37,76,77)],
            evidence_receipts=["ee6646", "bfb244", "df8dad", "4f98fd"],
            finite_acceptance="已读全部十接口的完整意义/前提/排除，再接18具名事实全部字段；保周期与生成/领取时点、引用和写入前缀、有效重量与真实sleep、正常终局与Abort、第二dispose先于第二检查。原source reader保留，不授本片R全文信用。",
            superseded="旧30cfed0载体缺席判断仅留史；本次不得据它列CRE-D空贡献阻塞。",
            not_transferred="2078全体/190父条款/1681子义未在本片重读；root task-final和四提案独立裁决不转授。"),
        open_definition="上述18组OPEN是可得当前域贡献未在本片逐事实收齐；不称材料不可得、宿主limit或整域不存在。旧DEVELOPER/CRE-C两组映射为空，只是固定载体局部观察。",
        material_unavailable=[], business_execution="NOT_EXECUTED", UPDATE_NOT_STARTED=True))
    write("reading-ledger.json", dict(schema="r8-legacy-g4-actual-reading/v1", utc=utc,
        own_reference_R_whole_files=0, primary=dict(complete_events=40, content_paragraphs=177,
            physical_lines=318, all_selected_bytes=145987, batches=[dict(shard=s, event_rounds=[a,b],
                receipt=receipt, truncated=False) for s,a,b,receipt in batches]),
        contract_reads=dict(global_prompt=["072de9:1–225", "3679e1:225–241"],
            skill="072de9:完整review-SKILL；其范围排除审计报告，无正文整改", agents="4d61b9:根AGENTS完整297行",
            shard_headers="b27754:S16–S20完整头部", unique_attachment="3679e1:公共有限合同；global/skill/AGENTS按同字节复用",
            attachment_sha256="0dc5bd2129043e2abccad7b48138e70dbd3e52133b2ed65e3cefe33e198ea546",
            complete_base_readset="49574f", event_fields="ef5282:共同四层字段去重后40项不同字段全部呈现",
            routes=["3d699e:前60", "bfb244:后59"], purposes="d57f8e:段落角色/标签/共同限定独立集合；非截断前半授全读",
            old_author_fields_are_not_own_credit=True),
        navigation=[dict(commit=B8,path=MANIFEST,ranges=[[1,4],[4115,4127]],receipts=["509b59","d1338d"]),
            dict(commit=B8,path="planning/extraction-plan.md",ranges=[[1,5]],receipt="509b59"),
            dict(commit=B8,path="deliverables/final-specification-set/README.md",ranges=[[1,21]],receipt="509b59"),
            dict(commit=B8,path="deliverables/final-specification-set/scope-statement.md",ranges=[[1,21]],receipt="509b59"),
            dict(commit=B8,path="deliverables/final-specification-set/test-catalog/README.md",ranges=[[1,25]],receipt="509b59"),
            dict(commit=B8,path="CURRENT-DELIVERY.md",ranges="FULL",receipt="509b59"),
            dict(commit=B8,path="delivery/2026-10-16-seventh/README.md",ranges="FULL",receipt="509b59")],
        supplementary=[dict(commit=TARGET,path=prefix+"/review.md",scope="FULL",receipt="328481"),
            dict(commit=TARGET,path=prefix+"/purpose-rules.v2.json",scope="FULL",receipt="ee6646"),
            dict(commit=TARGET,path=prefix+"/interfaces.json",scope="FULL",receipt="ee6646"),
            dict(commit=TARGET,path=prefix+"/gaps.json",scope="FULL",receipt="ee6646"),
            dict(commit=CONTRACT,path=REVIEW+"/tasks/receive_external_legacy_manifest_currentness/counter-h001.md",
                 scope="完整资格/边界，非自身重读底层源或新增反证票",receipt="328481")],
        corrections=["首次将五附件合并显示被截断：不授完整信用，按同字节公共附件与独立头部补读。",
            "一次40事件重复共同字段显示截断：ef5282去重共同字段并完整呈现全部差异。",
            "一次路由/供应者大显示截断：3d699e与bfb244补全119路由；供应者身份由本工具逐项核，不冒完整语义。",
            "33输入首轮检查到read-chunks list调用keys报错：b5979c修正类型分支后重核全部33；未执行恢复脚本或业务。",
            "本片验证工具首次把两个.ndjson供应索引当JSON解析，报Extra data；识别.ndjson/.jsonl后重核成功，只影响工具计数。"],
        private_io="工具chunk为本平台呈现凭证，未声称原始完整平台流已公开远端回读；固定Git行段和字段可重现。",
        requested_configuration="gpt-6.1-sol / ultra / default / Fast off",
        actual_configuration={k:"UNVERIFIED" for k in ("model","effort","tier","speed","Fast")},
        business_execution="NOT_EXECUTED", UPDATE_NOT_STARTED=True))
    write("verification.json", dict(schema="r8-legacy-g4-tool-verification/v1", utc=utc,
        counts=counts, target_all33_modes_blobs_bytes_sha_and_set_match=True,
        target_identity_collection_sha256=hashlib.sha256(canonical(target_identities)).hexdigest(),
        all318_physical_offsets_and_sha_match_B8=True, all318_purpose_rows_equal_fixed_target=True,
        all40_complete_event_records_equal_fixed_target=True, all119_formal_and_owner_readset_identities_match=True,
        all_old_named_provider_items_match=True,
        old_named_provider_item_count=sum(len(p["fixed_items"]) for p in provider_observations),
        old_empty_provider_ids=[r["id"] for r in provider_observations if r["fixed_items"] and all(
            v == 0 for f in r["fixed_items"] for v in f["selected_list_counts"].values()) and all(
            f["selected_list_counts"] for f in r["fixed_items"])],
        semantic_credit_from_this_script=0, restored_programs_executed=False,
        expected_R_tree=git("-C", "/workspace/pokemon-essentials", "rev-parse", R+"^{tree}").decode().strip(),
        scope="本工具只编码手写结论与核身份/集合，不决定语义真值或把40实读变40完整当前行为接受。"))
    print(json.dumps(dict(status="TOOL_VALIDATION_ONLY", counts=counts), ensure_ascii=False))


if __name__ == "__main__":
    main()
