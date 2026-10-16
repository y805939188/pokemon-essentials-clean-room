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
ai_proposals, aib = take("tasks/com_ai/proposals.json")
ai_counter, aicb = take("tasks/com_facility/adjudications-ai.json")
hist_proposals, hpb = take("tasks/history_current/findings.json")
hist_counter, hcb = take("adjudication/root-hist-001-counterreview.json")
hist_facets_counter, hfcb = take("adjudication/root-history-facets-counterreview.json")
u12_counter, u12b = take("adjudication/root-u12-receipt-scope-counterreview.json")
world003_counter, w003b = take("adjudication/root-world003-counterreview.json")
world_int_reception, wintb = take("adjudication/root-world-int001-reception.json")
world_int002, wint002b = take("adjudication/root-world-int002-counterreview.json")
ui003_counter, ui003b = take("adjudication/root-ui003-counterreview.json")
world004_counter, w004b = take("adjudication/root-world004-counterreview.json")
com004_counter, com004b = take("adjudication/root-com004-counterreview.json")
com005_counter, com005b = take("adjudication/root-com005-counterreview.json")
first_recorded, first_recorded_binding = take("adjudication/root-decision-first-recorded-bindings.json")

records = []
def add(id_, classification, severity, reason, evidence, binding, *, proposer=None, reviewer=None, extra=None):
    row = {
        "id": id_, "root_decider": "/root", "decision_utc": NOW,
        "decision_utc_qualification": "Legacy field is this aggregate build/reconfirmation UTC, not the original first decision/source-read operation UTC; no new independent vote.",
        "first_recorded_provenance": copy.deepcopy(first_recorded["records"].get(id_, {"status": "UNVERIFIED"})),
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

for index, proposal in enumerate(ai_proposals["records"]):
    required = index == 0
    reason = ("采纳有界P3定义补全：现存逐目标评分查询可直接调用，候选原类型按当代首槽/旧代全槽形成，PP过滤仅在伤害招匹配帮助函数，首个合格候选只加14一次。普通CONVERSION/User0不调用该目标评分的原合同正确，必须保留，不要求修改默认接线或真实纹理动作。目录的F/G标识及未知扩展不能代替已可读的查询定义。"
              if required else
              "仅列可选文字一致性：完整评级行为表及附表20条add、5个copy目标已给出；主稿23条登记的数字不一致不独立证明缺失行为，不计必修。可选澄清计数口径，不能据此改任何修正、拼写、默认或资格。")
    add(proposal["id"], "required" if required else "optional", "P3" if required else None,
        reason, proposal, aib, proposer="/root/com_ai", reviewer="/root/com_facility",
        extra={"independent_counterreview": ai_counter,
               "independent_counterreview_binding": aicb,
               "optional_adoption": None if required else "USER_DECISION; not automatically adopted",
               "root_direct_read_credit": "完整两项提案及独立反证；另实际逐行读有关source/formal结构，详见coverage/root-ai-reception.json；不是root全COM-AI源码/正式域信用。"})

hist_proposal = hist_proposals["proposals"][0]
add("GR8-HIST-001", "required", "P3",
    "采纳有限当前导航资格：同一current registry已称根有限关闭完成，阶段计数仍为3/2及0且未标历史投影；新后继overlay具名限定旧计数并链接准确27/13最终接收。原registry、ledger和全部关闭证据只读，不能补造旧计数生成时间或把R7关闭判作无效。",
    hist_proposal, hpb, proposer="/root/history_current", reviewer="/root",
    extra={"independent_counterreview": hist_counter, "independent_counterreview_binding": hcb,
           "required_future_new_write_set": ["review/remediation-eighth-20261016-prepare/navigation/current-r7-metadata-qualification.json"],
           "required_formal_write_set": [], "historical_reopening": False})
for row in hist_facets_counter["records"]:
    reason = ("采纳独立P3身份导航资格：U03/U07/U10同一最终batch的r2结果与reviewer_context已正确，但直接reviewer_task_id仍是被排除的r1。保留其初始派发历史，在新后继overlay具名标历史并链接准确r2结果/审者配对，不改原ledger或独立审者数。"
              if row["id"] == "GR8-HIST-R2-BINDING-001" else
              "采纳独立P3续审进度导航资格：U06最终batch保留未限定的启动WAIT字样，却已有同context签发完成结果/closed。后继overlay限定旧启动快照并另列准确完成身份；程序裁定自身未授PASS、旧WAIT和违例保持，续审不新增审者。")
    add(row["id"], "required", "P3", reason, row["retained_proposal"], row["proposal_binding"],
        proposer=row["proposer"], reviewer="/root",
        extra={"independent_counterreview": row, "independent_counterreview_binding": hfcb,
               "required_future_new_write_set": row["concrete_future_new_write_set"],
               "required_formal_write_set": [], "historical_reopening": False,
               "root_cause_qualification": "与HIST001阶段计数、另一facet分别可反证；共享一个未来overlay不合并根因。"})

add("GR8-HIST-U12-RECEIPT-SCOPE-001", "optional", None,
    "拒绝新增required，仅可选追溯说明。完整输入回执保留原输入UTC及旧发布句，同时具名历史WAIT和完成ledger；当前报告明确报告/per-id才是后继新判断，parent接收/eligibility均一致。按输入回执和当前裁决分层的完整读法成立，不能仅以孤立WAIT字段增加必修或假称15:43为完成时间。旧记录保持。",
    u12_counter["complete_proposal"], u12_counter["proposal_binding"],
    proposer="/root/h_r7_final_receptions", reviewer="/root",
    extra={"independent_counterreview": u12_counter, "independent_counterreview_binding": u12b,
           "required_rejected": True, "optional_adoption": "USER_DECISION; not automatically adopted",
           "historical_reopening": False, "required_formal_write_set": []})

add("GR8-WORLD-003", "required", "P3",
    "采纳有限跳跃组合定义补全。直接零偏移跳跃可在下一合格普通轮次仍活动，而无普通移动计时；末端ACTION/SPECIAL及已有调用消费不另检查跳跃。完整WP12/WP13事件正文未把静止精确定义为该有限门，须原位补齐，保留消息早退、登记/消费分层、顺序和请求级别；不保证完整UI、跳跃清理或Demo。",
    world003_counter["complete_proposal"], world003_counter["input_binding"],
    proposer="/root/world_full", reviewer="/root",
    extra={"independent_counterreview": world003_counter,
           "independent_counterreview_binding": w003b})
add("GR8-WORLD-INT-001", "required", "P3",
    "采纳有限117生产绑定缺项：携父事件编号但子取当前图，父保持原绑定。连接A/B例为子[B,7]与父[A,7]；失联仅清编号，子[B,0]/父[A,0]。一般启动身份正文不足以唯一给出该生产前提；保留角色当前图选择、缺省脚本键、同图/缺记录/深度/异常与无存档运行限定。",
    world_int_reception["complete_proposal"], world_int_reception["proposal_binding"],
    proposer="/root/world_interpreter", reviewer="/root/world_full",
    extra={"independent_counterreview": world_int_reception["complete_independent_counterreview"],
           "independent_counterreview_binding": world_int_reception["counterreview_binding"],
           "root_reception": world_int_reception, "root_reception_binding": wintb})

add("GR8-WORLD-INT-002", "required", "P3",
    "采纳直接119缺目标的有限正常控制补全：正常带终止项列表无命中时，119不改当前位置而返回继续，外层到下一命令；同列表命中跳过A而缺目标执行A/B的对照成立。当前119失败栏和未决整体未知过宽，须收窄；保留宿主未运行、末尾先结束、首命中/有限向后及101预读独立规则，不新增未来作者校验policy。",
    world_int002["complete_proposal"], world_int002["proposal_binding"],
    proposer="/root/world_interpreter", reviewer="/root",
    extra={"independent_counterreview": world_int002,
           "independent_counterreview_binding": wint002b})

add("GR8-UI-003", "optional", None,
    "保留Shadow INFO未满级仍按普通经验请求底条的真实源事实，拒绝新增required。完整WP66A的Exp区可合理限于被心量表/文案替换的经验数字区域，非Shadow正向条款未独立禁止Shadow底条；WP23成长概述也无全部图层禁令。可选澄清普通经验进度与saved_exp区别，不强制新增测试或领域修订。",
    ui003_counter["complete_proposal"], ui003_counter["proposal_binding"],
    proposer="/root/ui_full", reviewer="/root",
    extra={"independent_counterreview": ui003_counter,
           "independent_counterreview_binding": ui003b,
           "origin_proposal_id": "GR8-UI-003.v1", "required_rejected": True,
           "optional_adoption": "USER_DECISION; not automatically adopted"})

add("GR8-WORLD-004", "required", "P3",
    "采纳单一跨稿引用限定修正：WP61§3.3将Repel比较者写可战，但同篇可战排濒死，正确WP36及默认配置却选首非蛋可濒死。合法濒死50/后续可战10/野生20默认仍拒绝，不能被更早无可战门排除。只校正WP61括注，保持WP36、计数/续用/雷达/能力/GR011，不强制新增目录测试。",
    world004_counter["complete_proposal"], world004_counter["proposal_binding"],
    proposer="/root/world_full", reviewer="/root",
    extra={"independent_counterreview": world004_counter,
           "independent_counterreview_binding": w004b,
           "exact_history_dedup": "PENDING; no old closure reopened"})

add("GR8-COM-004", "required", "P3",
    "采纳最小局部矛盾修正：WP39§3.4引导括注仅有消息差异排除了真实结果分叉；正常零可战斗前提下wild helper返回1、trainer helper返回0，pbSet参数相应不同。同段line113及现有BC-09已正确，须保留且不强制新增用例；旧no-battle概念关闭项不重开，历史全量去重仍OPEN。",
    com004_counter["complete_proposal"], com004_counter["proposal_binding"],
    proposer="/root/core_atomic_reception", reviewer="/root",
    extra={"independent_counterreview": com004_counter,
           "independent_counterreview_binding": com004b,
           "origin_proposal_id": "GR8-CAR-CAND-001",
           "exact_history_dedup": "PENDING; no old closure reopened"})

add("GR8-COM-005", "required", "P3",
    "采纳最小动作谓词修正：WP39§7.4末尾玩家转向正前把实际动画复位写为方向动作。独立完整after_battle/继承straighten/转向方法与正常方向4、6静态对照确认尾call不写direction；完整正文没有将转向另定义为动画整理。仅替末短语，保POISON/形态/伙伴/治疗/等待/end事件，不要求新目录用例，不否定整场或回调曾改变方向；全量历史去重仍OPEN。",
    com005_counter["complete_proposal"], com005_counter["proposal_binding"],
    proposer="/root/core_atomic_reception", reviewer="/root",
    extra={"independent_counterreview": com005_counter,
           "independent_counterreview_binding": com005b,
           "origin_proposal_id": "GR8-CAR-CAND-002",
           "exact_history_dedup": "PENDING; no old closure reopened"})

counts = {"required": sum(r["classification"] == "required" for r in records),
          "required_P2": sum(r["classification"] == "required" and r["severity"] == "P2" for r in records),
          "required_P3": sum(r["classification"] == "required" and r["severity"] == "P3" for r in records),
          "optional": sum(r["classification"] == "optional" for r in records)}
out = {
    "schema": "gr8-root-bounded-decisions/v1", "utc": NOW, "decider": "/root",
    "B8": "fd1df570cad987dc3852a3b958f03916e317f7fe", "R": "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b",
    "status": "PARTIAL_REVIEW_NO_GLOBAL_PASS", "whole_review_required_count": None,
    "bounded_counts": counts,
    "counts_qualification": "仅此已接收25项的有限裁决；不是本轮最终分母/最终必修数。后续全局读证可能需有据修订。",
    "records": records, "root_read_complete_payloads": inputs,
    "root_read_credit": "完整独立反证/提案文件的综合接收，不冒充root已逐个重读其全部原source/formal，也不授其它领域覆盖。PBSW001另有root真实独立全读证据。",
    "separate_bounded_no_required_reception": "adjudication/root-binary-bounded-receptions.json: 四项实际非提出者有限接收，不计本25项required/optional或全域NO_REQUIRED_UPDATE。",
    "separate_rejected_original_candidate": "adjudication/root-ui002-reception.json: GR8-UI-002 v1异常反例已驳回，不计required/optional，不自动替换为显示缺项。",
    "pending_proposals_outside_this_receipt": ["后续新提案仍持续进入；全量未读、跨域及历史接收尚未完成。"],
    "actual_configuration": dict.fromkeys(["model", "effort", "tier", "speed", "opaque_platform_id"], "UNVERIFIED"),
    "requested_configuration": {"model": "gpt-6.1-sol", "effort": "ultra", "tier": "default", "speed": "normal/Fast off"},
    "behavior_execution_credit": 0, "update_started": False, "final_marker": "UPDATE_NOT_STARTED",
}
assert len(records) == 25 and len({r["id"] for r in records}) == 25
assert sum(r["classification"] == "required" for r in records) == 21
p = ROOT / "adjudication/root-decisions.partial.json"
p.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"path": str(p), "bytes": p.stat().st_size, "sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "status": out["status"], "bounded_counts": out["bounded_counts"]}, ensure_ascii=False))
