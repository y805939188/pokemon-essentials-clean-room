"""Freeze bounded root decisions; this is never a whole-review completion claim."""
from pathlib import Path
import copy
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

def read(rel):
    p = ROOT / rel
    raw = p.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    snapshot = ROOT / "evidence/adjudication-inputs" / (sha + ".json")
    snapshot.parent.mkdir(parents=True, exist_ok=True)
    if snapshot.exists():
        assert snapshot.read_bytes() == raw
    else:
        snapshot.write_bytes(raw)
    return json.loads(raw), {"path": rel, "bytes": len(raw), "sha256": sha,
                            "frozen_snapshot": str(snapshot.relative_to(ROOT))}

inputs = []
def take(rel):
    data, identity = read(rel)
    inputs.append(identity)
    return data, identity

kernel, kb = take("tasks/counter_kernel_first/adjudications.json")
creature, cb = take("tasks/combat_review/adjudications-creature.json")
creature_proposal, cpb = take("tasks/creature_review/proposals/GR8-CRE-001.v2.json")
combat, bb = take("tasks/counter_combat_first/adjudications.json")
pbs, pb = take("tasks/pbs_world_record_audit/proposals.json")
pbs1counter, p1b = take("coverage/root-pbsw-001-counterreview.json")
pbs2counter, p2b = take("tasks/world_topology_audit/refutation-pbsw002.json")
ui, ub = take("tasks/ui_navigation_audit/proposals.json")
uicounter, ucb = take("tasks/world_topology_audit/refutation-ui001.json")
world_proposal, wpb = take("tasks/counter_world_first/proposals.v1.frozen.json")
world_counter, wcb = take("tasks/counter_world_first/adjudications.json")
world_identities, wib = take("tasks/counter_world_first/identities.json")

records = []
def add(id_, classification, severity, reason, evidence, binding, *, proposer=None, reviewer=None, extra=None):
    row = {
        "id": id_, "root_decider": "/root", "decision_utc": NOW,
        "classification": classification, "severity": severity,
        "status": "CLASSIFIED_BOUNDED_SCOPE_PENDING_GLOBAL_HISTORY_AND_INTERFACE_RECEPTION",
        "root_reason": reason, "complete_semantic_contract_received": copy.deepcopy(evidence),
        "contract_input_binding": binding, "proposer": proposer, "actual_nonproposer_reviewer": reviewer,
        "global_completion_granted": False, "update_started": False,
        "execution": "SOURCE_STATIC / DERIVED_VECTOR; NOT_EXECUTED behavior",
        "remaining_global_conditions": [
            "全量源与formal独立审读完成后，核任何相反条款及必要消费者；当前有限裁决不得代替全局覆盖。",
            "按所有当前有效历史资格完成根因去重；不修改原关闭台账。",
            "最终中文交接补齐唯一primary批次、共享接收、冲突与依赖，静态与真实运行分别验收。",
        ],
    }
    if extra:
        row.update(extra)
    records.append(row)

kernel_reasons = {
    "GR8-KER-001": "采纳P3最小顺序/失败前缀补记。主档先删、备份后删决定第二步失败后的剩余文件及下次主档存在门；既有UI条款已经承认部分失败和不回滚，不采纳原子性错误指控，不重复改正确UI规则。",
    "GR8-KER-002": "采纳P3，仅改WP09:102及UI65:27的穷尽启动二分。存在但可读的旧序列可适配为空，应按读取后数据空性决定boot默认装配；无文件的充分示例、正确WP08语言门及后续有效性/备份/删除/拒绝退出链必须保留。",
    "GR8-KER-003": "采纳P3，删除WP04:196对特定Changes made输出的无依据承诺。完整formatter与caller链确认仅构造未消费字符串；保留真实属性更名、整文件改写、其它编译输出及各阶段异常前缀。",
}
for row in kernel["records"]:
    add(row["id"], "required", "P3", kernel_reasons[row["id"]], row, kb,
        proposer=row["proposer"], reviewer=row["independent_reviewer"])

cr = creature["records"][0]
add("GR8-CRE-001", "required", "P3",
    "采纳有限数值前提/失败合同：合法模板生产255后显式进入普通EV分配，首HP余量为负时区间夹限先失败；默认设施internalBattle=false会提前阻断。不得扩大为默认设施故障、全部道具外层或Shadow/净化保证；WP28已有受限状态限定应保持。",
    cr, cb, proposer=cr["proposer"], reviewer=cr["reviewer"],
    extra={"original_proposal_binding": cpb, "original_proposal": creature_proposal})

one, two = combat["records"]
add("GR8-COM-001", "required", "P3",
    "采纳标识澄清：WP40同篇将懒惰用于TRUANT行动拒绝，却将其作排序档示例；用明确STALL替换即可。WP48排序表已正确，不声称全局算法缺失或源实现排序bug。",
    one, bb, proposer=combat["proposer"], reviewer=combat["reviewer"])
for index, canonical_id in enumerate(["GR8-COM-002", "GR8-COM-003"]):
    facet = two["facets"][index]
    detail = {k: copy.deepcopy(v) for k, v in two.items() if k != "facets"}
    detail["selected_canonical_facet"] = copy.deepcopy(facet)
    if index == 0:
        reason = "保留原提案ID用于零可战斗wild成员边界，P2。默认等边布局把缺失首计数传播到双边布局并在owner检查前失败；保留玩家skip、不同不等布局的首失败和历史NPC合同。"
    else:
        reason = "从原COM002组合提案分立新稳定ID，P2。正计数可通过参与者检查，但原顺序完整构造与布局限定行动集合不同；[HP0,存活]与逆序的存活行动身份有别。只改零计数不修这个根因，故分别登记；不声称所有布局/伙伴/真实画面或最终战果。"
    add(canonical_id, "required", "P2", reason, detail, bb,
        proposer=combat["proposer"], reviewer=combat["reviewer"],
        extra={"root_cause_key": facet["root_cause_key"], "origin_proposal_id": "GR8-COM-002",
               "origin_facet_id": facet["facet_id"], "split_relation": "原完整组合提案保留不改；002承接ZERO_ABLE，003承接MIXED_ORDER，各唯一根因。",
               "historical_reopening": False, "related_historical_root": "GIR-FD82-B002 (NPC input; scope preserved)"})

for index, proposal in enumerate(pbs["records"]):
    counter = pbs1counter if index == 0 else pbs2counter
    counter_binding = p1b if index == 0 else p2b
    reason = ("采纳P3，完整67显式记录只有5条匹配3/15/2..5，不能称多数；仅替换频数用语，保留真实构造缺省及CHERI数学向量。"
              if index == 0 else
              "采纳P3：默认PBS051已明确Dungeon=true，可得文本配置不得整体列为材料缺失；同时保留真实Map051、编译装载、tileset/area/event与Demo可达性未知。WP14两处与WP11同步一次。")
    add(proposal["id"], "required", "P3", reason, proposal, pb,
        proposer=proposal["proposer"], reviewer=proposal["independent_rebutter"],
        extra={"independent_counterreview": counter, "independent_counterreview_binding": counter_binding})

proposal = ui["records"][0]
add("GR8-UI-001", "optional", None,
    "不采纳required。完整WP65§4.1已明确确认前更改不回滚，因此普通No的无副作用可合理限于该确认分支；源事实没有被否定，首次打开时的共享名称替换应保留。可选将括注澄清为不调用持久层保存，避免跨阶段误读；不强制新增向量或第二地图命名规则。作者已接收此限缩。",
    proposal, ub, proposer=proposal["proposer"], reviewer=uicounter["actual_independent_reader"],
    extra={"independent_counterreview": uicounter, "independent_counterreview_binding": ucb,
           "required_rejected": True, "optional_adoption": "USER_DECISION; not automatically adopted",
           "root_direct_formal_read": {"commit": "fd1df570cad987dc3852a3b958f03916e317f7fe", "path": "deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md", "range": [70, 106], "scope": "§4.1 complete with surrounding contexts; not wholeUI credit"}})

for index, row in enumerate(world_counter["records"]):
    reason = ("采纳P3：已进入的邻图摆放异常可留下后续摆放受抑制状态，同实例重建/帮助缓存清理不独立恢复。必须明确外层捕获并继续，不能据此说默认流程会恢复、永久软锁或未来必须复制私有guard。"
              if index == 0 else
              "采纳P3：有连接分支末端范围门包含当前图；speed0远移后一次生命周期可返回空驻留集合，而全局仍指原图。直接保存可条件成功，后继取图失败；不能说保存必失败。保留26格仅删A留B、第二次补建、非零speed/UI时机和真实宿主未知。")
    add(row["id"], "required", "P3", reason, row, wcb,
        proposer=row["proposer"], reviewer=row["actual_independent_refuter"],
        extra={"original_proposal": world_proposal[index], "original_proposal_binding": wpb,
               "source_formal_identity_bindings": world_identities,
               "source_formal_identity_payload_binding": wib,
               "source_location_correction": "WORLD002 scroll source actual497–518; retain original proposed507–530 only as history, not support." if index else "No new source-location correction."})

out = {
    "schema": "gr8-root-bounded-decisions/v1", "utc": NOW, "decider": "/root",
    "B8": "fd1df570cad987dc3852a3b958f03916e317f7fe", "R": "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b",
    "status": "PARTIAL_REVIEW_NO_GLOBAL_PASS", "whole_review_required_count": None,
    "bounded_counts": {"required": 11, "required_P2": 2, "required_P3": 9, "optional": 1},
    "counts_qualification": "仅此已接收12项的有限裁决；不是本轮最终分母/最终必修数。后续全局读证可能需有据修订。",
    "records": records, "root_read_complete_payloads": inputs,
    "root_read_credit": "完整独立反证/提案文件的综合接收，不冒充root已逐个重读其全部原source/formal，也不授其它领域覆盖。PBSW001另有root真实独立全读证据。",
    "pending_proposals_outside_this_receipt": ["GR8-HIST-001"],
    "actual_configuration": dict.fromkeys(["model", "effort", "tier", "speed", "opaque_platform_id"], "UNVERIFIED"),
    "requested_configuration": {"model": "gpt-6.1-sol", "effort": "ultra", "tier": "default", "speed": "normal/Fast off"},
    "behavior_execution_credit": 0, "update_started": False, "final_marker": "UPDATE_NOT_STARTED",
}
assert len(records) == 12 and len({r["id"] for r in records}) == 12
assert sum(r["classification"] == "required" for r in records) == 11
p = ROOT / "adjudication/root-decisions.partial.json"
p.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"path": str(p), "bytes": p.stat().st_size, "sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "status": out["status"], "bounded_counts": out["bounded_counts"]}, ensure_ascii=False))
