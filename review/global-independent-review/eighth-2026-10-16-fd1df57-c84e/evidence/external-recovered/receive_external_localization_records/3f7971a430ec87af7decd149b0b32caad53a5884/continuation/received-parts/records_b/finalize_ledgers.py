"""Assemble recorded, already completed readings. Never grants credit by parsing.

Run from repository root. Inputs remain fixed; only this script's directory is written.
The human-authored semantic review and explicit platform chunk IDs are the basis
of the reading decisions. The assertions below are mechanical consistency checks.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess

OUT = Path(__file__).resolve().parent
TASK = OUT.parents[2]
ROOT = Path.cwd()
CONTRACT = TASK / "continuation/contracts"
FIXED = "d14a4bf68776ac7aacf54065c28ed982a054c8a8"
READSET = json.loads((CONTRACT / "readsets/records_b.complete.json").read_text())
CONTEXT = "01a1448a-24b4-73d7-aa11-96a1ddb0400a"


def put(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def git(*args, cwd=ROOT):
    return subprocess.check_output(["git", *args], cwd=cwd)


def identity(repo, commit, path):
    line = git("ls-tree", commit, "--", path, cwd=repo).decode().strip()
    meta, actual_path = line.split("\t", 1)
    mode, kind, blob = meta.split()
    assert actual_path == path and kind == "blob"
    data = git("cat-file", "blob", blob, cwd=repo)
    assert (repo / path).read_bytes() == data
    return dict(commit=commit, path=path, mode=mode, git_blob=blob,
                bytes=len(data), sha256=hashlib.sha256(data).hexdigest())


BATCHES = [
    ("B01", "MOVE_DESCRIPTIONS", 115, 274, 7, 166, "f9e68b",
     "电系控制至幽灵攻击叙述；R199的If may与R204的hurt原拼写保留；先后/比例均只为描述。"),
    ("B02", "MOVE_DESCRIPTIONS", 275, 434, 167, 326, "2fed4f",
     "影子、草、地、冰至普通攻击；R287的storm of sharp保留；野外移动/金币叙述未升级为实际接线。"),
    ("B03", "MOVE_DESCRIPTIONS", 435, 594, 327, 486, "826f11",
     "普通辅助、毒与部分超能文本；R504的suceeds、R588的This move the higher原样保留；名称和描述非逐号对应数组。"),
    ("B04", "MOVE_DESCRIPTIONS", 595, 725, 487, 617, "5194c7",
     "超能、岩、钢、水及Withdraw叙述读到末条；R674的The foe slams保留。"),
    ("B05", "MOVE_NAMES", 1, 131, 620, 750, "5194c7",
     "从Megahorn至Magnetic Flux；Feint/Faint、Dragon Breath/DragonBreath、Thunder Punch/ThunderPunch等逐个文本键。"),
    ("B06", "MOVE_NAMES", 132, 761, 751, 1380, "af8f93",
     "Thunder Wave至Withdraw全部名称；Vise/Vice/ViceGrip、含空格/连字符/撇号及旧拼法均保留，未做别名迁移。"),
    ("B07", "POKEDEX_ENTRIES", 1, 80, 1383, 1462, "c5bdb6",
     "Bulbasaur至附着Shellder的Slowbro叙述；距离、速度、18小时/每小时Teleport是叙事数据，不立计时规则。"),
    ("B08", "POKEDEX_ENTRIES", 81, 160, 1463, 1542, "3bb7ca",
     "磁体至Feraligatr叙述；F温度、300百万年、人工遗传及变形均只作文字；stream- beds原间隔保留。"),
    ("B09", "POKEDEX_ENTRIES", 161, 248, 1543, 1630, "04329d",
     "Sentret守卫至Tyranitar筑巢末条；季节/天气、64F、suction- cupped及5,000标记原样保留，不推出生态模拟。"),
]

rows = json.loads((OUT / "mechanical-record-bindings.json").read_text())["rows"]
assert len(rows) == 1620
assert [x["id"] for x in rows] == READSET["record_ids"]
original = json.loads((CONTRACT / "readsets/records_b.original-semantic-fields.json").read_text())
idx = json.loads((CONTRACT / "readsets/records_b.identity-only-index.json").read_text())
index_by_id = {x["id"]: x for x in idx["rows"]}
view_path = str((CONTRACT / "views/records_b.records.view.txt").relative_to(ROOT))
sem_path = str((OUT / "semantic-review.md").relative_to(ROOT))
binding_path = str((OUT / "mechanical-record-bindings.json").relative_to(ROOT))

batches = [dict(id=b, domain=d, first=a, last=z, count=z-a+1,
                view_lines=[ls, le], platform_chunk=chunk,
                tool_exit=(2 if b == "B02" else 0), output_truncated=False, semantic_observation=note,
                exit_qualification=("sed and complete menu text presented; final rg guessed path failed, preserved below. Exit2 is not a truncated literal reading." if b == "B02" else "Actual combined command exit0."),
                stdout_scope="Record lines specified; command also printed separately identified definitions.",
                recovery=dict(commit=FIXED, path=view_path, lines=[ls, le]),
                exact_private_platform_event_export="UNVERIFIED",
                per_read_utc="UNVERIFIED")
           for b, d, a, z, ls, le, chunk, note in BATCHES]

definitions = [
    ("D01", "Data/Scripts/001_Technical/003_Intl_Messages.rb", [[1, 823]], ["1869a8", "a9f044", "ad1c7b"],
     "全文823行；收集/转义/导出/导入/加载/默认过滤/查询/31域/包装/参数及全部结束行。"),
    ("D02", "Data/Scripts/021_Compiler/001_Compiler.rb", [[59, 182], [255, 293], [384, 436], [690, 737], [952, 1037]],
     ["ad1c7b", "027975", "b97849"],
     "完整分节/预处理、PBS节读取、CSV相关入口、目录与编译主次序；没有批准其它全部PBS函数或无界枚举。"),
    ("D03", "Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb", [[4, 68], [205, 230], [283, 538]],
     ["123199", "d64665"], "完整通用编译、Move及Species基础/形态的编译与验证方法；保留所有先行门、异常及set/add区别。"),
    ("D04", "Data/Scripts/010_Data/001_GameData.rb", [[1, 283]], ["7caecd"],
     "全文注册/读取/遍历/保存加载及schema入口；对象身份与文本键分开。"),
    ("D05", "Data/Scripts/010_Data/002_PBS data/005_Move.rb", [[1, 73]], ["123199"],
     "完整schema、构造、默认、name/description；其余招式玩法不在本任务签字。"),
    ("D06", "Data/Scripts/010_Data/002_PBS data/008_Species.rb", [[1, 241]], ["d64665"],
     "完整schema、构造、形态选择/统计及文本getter；非pokedex领域未作整文件批准。"),
    ("D07", "Data/Scripts/001_Technical/002_Files/001_FileTests.rb", [[4, 61]], ["f9e68b"],
     "Dir.get排序、Dir.all递归/文件、safe?、create及all_dirs完整定义；导出只删除列举文件。"),
    ("D08", "Data/Scripts/001_Technical/002_RubyUtilities.rb", [[390, 392]], ["f9e68b"],
     "nil_or_empty?完整定义；缺值/非字符串/空串的门。"),
    ("D09", "Data/Scripts/019_Utilities/001_Utilities.rb", [[114, 144]], ["f3663a"],
     "hasConst?/getConst/getConstantName完整定义及所处上下文；只为节名/域名解析。"),
    ("D10", "Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb", [[1423, 1477]], ["2fed4f"],
     "导出与编译两个完整菜单注册单元；选择/取消/原位去前缀及调用参数。"),
    ("D11", "Data/Scripts/001_Settings.rb", [[415, 428]], ["5194c7"], "LANGUAGES完整配置段及空默认。"),
    ("D12", "Data/Scripts/999_Main/999_Main.rb", [[1, 60]], ["5194c7"],
     "实际启动定义/循环完整当前文件；只签默认加载与随后初始化的有限顺序。"),
    ("D13", "Data/Scripts/003_Game processing/001_StartGame.rb", [[1, 35]], ["af8f93"],
     "完整Game.initialize和set_up_system；只为数据加载、语言配置门，不签其它保存/新游戏定义。"),
]
definition_ledger = []
for did, path, ranges, chunks, meaning in definitions:
    ident = identity(Path("/workspace/pokemon-essentials"), READSET["R"], path)
    definition_ledger.append(dict(id=did, identity=ident, actual_complete_required_ranges=ranges,
                                  platform_chunks=chunks, meaning=meaning,
                                  status="NECESSARY_DEFINITIONS_FULLY_READ_SOURCE_STATIC",
                                  irrelevant_file_remainder="NOT_CLAIMED"))
for did, path, ranges, chunks in [
    ("B8-WP08", "deliverables/final-specification-set/generic-kernel/wp08-localization.md", [[1, 231]], ["123199", "7caecd"]),
    ("B8-LZ", "deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md", [[110, 154], [277, 288]], ["c5bdb6", "3bb7ca"]),
]:
    definition_ledger.append(dict(id=did, identity=identity(ROOT, READSET["B8"], path),
                                  actual_complete_required_ranges=ranges, platform_chunks=chunks,
                                  status="FULL_REQUIRED_TEXT_READ", behavior_execution="NOT_EXECUTED"))

reading_records = []
reception_records = []
meaning_templates = {}
for domain in original["templates"]:
    role = "S2-DEX" if domain == "POKEDEX_ENTRIES" else "S2-MOVE"
    meaning_templates[domain] = dict(
        complete_meaning_refs=[f"{sem_path}#S0", f"{sem_path}#S1", f"{sem_path}#{role}"],
        complete_original_semantics=original["templates"][domain],
        complete_original_fact_group=next(x for x in original["fact_groups"] if x["domain"] == domain),
        necessary_premises_ref=f"{sem_path}#S0",
        source_definition_ids=["D01", "D02", "D03", "D04", "D06" if domain == "POKEDEX_ENTRIES" else "D05"],
        B8_reverse_refs=["WP08-30", "WP08-51", "WP08-130", "WP08-153", "WP08-155"],
        consumer_join=("Species.real_pokedex_entry→POKEDEX_ENTRIES(3) hash getter" if domain == "POKEDEX_ENTRIES" else
                       "Move.real_name→MOVE_NAMES(5) hash getter" if domain == "MOVE_NAMES" else
                       "Move.real_description→MOVE_DESCRIPTIONS(6) hash getter"),
        reason="本域每ID的完整原键/译文已实际读；对应原业务字段严格相等共享且全文已读；域内文本数据意义、完整producer/构造/getter和反向条款见精确引用。不由名称/叙述推玩法。",
        finite_unresolved=[], parent_only_open_ref=f"{sem_path}#S5",
        original_reviewer_status_preserved=True,
        behavior_execution="NOT_EXECUTED")
for position, row in enumerate(rows):
    n, domain = row["record"], row["domain"]
    matches = [b for b in batches if b["domain"] == domain and b["first"] <= n <= b["last"]]
    assert len(matches) == 1
    batch = matches[0]
    assert row["view_line"] == batch["view_lines"][0] + n - batch["first"]
    link = dict(binding_row=position, view_line=row["view_line"])
    reading_records.append(dict(id=row["id"], domain=domain, record=n,
                                literal_read_here=True, fields_read=["source_key", "translation_value"],
                                reading_batch=batch["id"], platform_chunk=batch["platform_chunk"],
                                literal_binding=link, source_lines=index_by_id[row["id"]]["lines"],
                                raw_key_and_translation_sha256=index_by_id[row["id"]]["key_sha256"],
                                status="COMPLETE_LITERAL_FIELDS_ACTUALLY_READ"))
    reception_records.append(dict(id=row["id"], domain=domain,
        reception="COMPLETE_FOR_THIS_FINITE_SHARD_AWAIT_PARENT_RECEPTION",
        literal_binding=link, complete_meaning_template=domain,
        original_identity_ref=dict(index_row=position),
        evidence=dict(batch=batch["id"], platform_chunk=batch["platform_chunk"], view_line=row["view_line"]),
        finite_unresolved=[]))

failure_history = json.loads((OUT / "reading-ledger.json").read_text()).get("failures_and_corrections", [])
# Idempotent: preserve original attempts without adding duplicates on rerun.
extra_failures = [
    dict(tool_chunk="73fcc1", problem="fixed d14 object absent locally; git fetch exact SHA succeeded at aa3382; no missing material remains"),
    dict(tool_chunk="b17f7c", problem="rg guessed 000_Config path absent, exit2; actual 001_Settings complete languages segment read by 5194c7"),
    dict(tool_chunk="2fed4f", problem="rg guessed 016_UI/001_UI_Load.rb absent, exit2; actual013_UI_Load located by5194c7; UI load is parent scope, no current full-reading claim"),
    dict(tool_chunk="68c12b", problem="initial mixed worktree-equality check 15/18; three parent successors atd14 differ from805; fixed805 bytes all valid, separately restored in write set byb17f7c"),
    dict(tool_chunk="027975", problem="navigation range included unused oldCSV methods and partial unrelated methods; no necessary-definition credit for partial unrelated units; actual split/cast complete byb97849"),
]
for item in extra_failures:
    if item not in failure_history:
        failure_history.append(item)

put("reading-ledger.json", dict(schema="r8-elr-records-b-reading/v1",
    status="READY_FOR_PARENT_RECORD_RECEPTION", actual_context=CONTEXT,
    contract_commit=FIXED, records=reading_records, literal_batches=batches,
    record_denominator=1620, actual_records_read=1620, actual_fields_read=3240,
    unread_records=0, unread_fields=0,
    reference_namespace=dict(contract_commit=FIXED, literal_view_path=view_path,
        literal_binding_rows_file=binding_path,
        literal_binding_rule="binding_row identifies rows[index].literal, which is both complete original fields. view_line is exact presentation line.",
        original_identity_index_path=READSET["pure_identity_index"]["path"],
        raw_identity_rule="Same ordered row in fixed identity index; both hashes independently equal per record.",
        all_record_evidence_level="SOURCE_STATIC", all_record_behavior_execution="NOT_EXECUTED"),
    complete_required_definitions=definition_ledger,
    original_semantic_fields_read=dict(path=READSET["required_original_semantics"]["path"], chunk="b3a233",
                                       templates=3, fact_groups=3, current_business_fields_omitted=0,
                                       strict_comparison="semantic-sharing-validation.json"),
    readset_purpose=dict(complete_non_identity_fields_chunk="4a653c",
                         record_ids="All1620 exact identity membership mechanically compared, included individually in these rows and literal presentations.",
                         pure_identity_index=idx["pure_identity_fields"],
                         purpose="ID/path/line/record/hash only; no literal or original semantic fields exempted."),
    headers=[dict(domain=d, source_lines=[1, 4], present_in_batch=b, status="FULL_HEADER_READ")
             for d, b in [("MOVE_DESCRIPTIONS", "B01"), ("MOVE_NAMES", "B05"), ("POKEDEX_ENTRIES", "B07")]],
    contract_reads=[dict(path="AGENTS.md", chunk="e6d2da"),
                    dict(path="inputs/review-SKILL.md", chunk="7fc2e1"),
                    dict(path="delegation/prompts/receive_external_localization_records.md", chunk="7fc2e1"),
                    dict(path="inputs/eighth-global-review-prompt.md", chunks=["be5259", "2a1fe6", "b3a233"], lines=[[1, 90], [91, 165], [166, 241]]),
                    dict(path="continuation/contracts/START.md", chunk="5a7426"),
                    dict(path="continuation/contracts/COMMON-CONTRACT.md", chunk="5a7426"),
                    dict(path="continuation/contracts/prompts/records_b.md", chunk="b3a233")],
    shared_reports_read=dict(parent805_report="027375", parent805_interfaces="826f11",
                             original_target_review="027375", original_target_continuation="04329d",
                             parent805_reception_top_level_current_meanings="6735f7",
                             parent805_other433_and36image="Navigation only; not needed as this shard evidence, no new credit"),
    failures_and_corrections=failure_history,
    I_O_qualification=dict(platform_chunks="Actual tool output identifiers from this session; exact fixed presentations recoverable by path/range.",
                           full_private_platform_event_export="UNVERIFIED", per_read_utc="UNVERIFIED",
                           separate_stdout_stderr="UNVERIFIED; tool output combined", generation_grants_reading_credit=False),
    behavior_execution="NOT_EXECUTED", UPDATE_NOT_STARTED=True))

put("reception-ledger.json", dict(schema="r8-elr-records-b-reception/v1", actual_context=CONTEXT,
    status="READY_FOR_PARENT_RECORD_RECEPTION", record_denominator=1620,
    finite_records_received_here=1620, finite_records_unreceived_here=0,
    independent_from_excluded_authors=CONTEXT not in READSET["excluded_author_contexts"],
    records=reception_records, complete_semantics="semantic-review.md",
    meaning_templates=meaning_templates,
    reference_namespace=dict(contract_commit=FIXED, literal_view_path=view_path,
        literal_binding_rows_file=binding_path,
        original_identity_index_path=READSET["pure_identity_index"]["path"],
        index_rule="literal_binding.binding_row and original_identity_ref.index_row use rows[index], same exact frozen ordering.",
        definition_ids="reading-ledger.json#/complete_required_definitions",
        template_rule="Every record explicitly binds its own literal and domain to the entire complete_meaning_template; original semantics were strictly compared for every ID before sharing.",
        all_record_behavior_execution="NOT_EXECUTED"),
    original_full_status_is_not_new_credit=True,
    parent_final_reception="PENDING; this report offers the contribution, parent must actually read it.",
    parent_seven_interfaces_closed=0, global_task_final_signed=False,
    behavior_execution="NOT_EXECUTED", UPDATE_NOT_STARTED=True))

put("interfaces.json", dict(schema="r8-elr-records-b-interfaces/v1",
    finite_direct_interfaces=[
        dict(id="ELR-RECORD-PIPELINE", status="COMPLETE_FINITE_SOURCE_STATIC", records=1620,
             support=["S0", "S1", "S3", "S4", "D01", "D02", "D07", "D08", "D09", "D10"], unresolved_here=[]),
        dict(id="ELR-DOMAIN-PRODUCER-GETTER", status="COMPLETE_FINITE_SOURCE_STATIC",
             support=["S2-MOVE", "S2-DEX", "D01", "D03", "D04", "D05", "D06"], unresolved_here=[]),
        dict(id="ELR-TO-PARENT-SEVEN-INTERFACES", status="ROUTED_PARENT_FINAL_OPEN",
             support=["S5"], global_signature=False),
    ],
    parent_interfaces=[
        dict(id="ELR-I01", contribution="Intl823/WP08全文及分节完整定义、五个原forward定位有限反向核验。", remains_open="KER-F102–112原贡献及125反向对象由父实际累计接收。"),
        dict(id="ELR-I02", contribution="Move及Species基础/非零形态完整producer、自有静态接合。", remains_open="其余producer和15+TrainerType/3共同合同原贡献由父全接。"),
        dict(id="ELR-I03", contribution="三域1620对和Move/Species完整必要schema、构造、缺省、getter。", remains_open="35PBS全部必要原值、530487B字段包及各owner贡献未在本组全读。"),
        dict(id="ELR-I04", contribution="固定文本原行→分节/逆转义/键值→显式语言加载→getter的有限链。", remains_open="原序列化消息/178链接全文与其它shard由父完成；本组未独立解码。"),
        dict(id="ELR-I05", contribution="止于三个数据getter返回值。", remains_open="UI36/Dex7、图鉴/招式界面与图像后继原贡献未在本组接收。"),
        dict(id="ELR-I06", contribution="作者菜单取消和无语言配置启动的完整必要单元。", remains_open="保存直写、地图名可变值、物品及窗口提示后继由父接收；不签整域。"),
        dict(id="ELR-I07", contribution="保留原作者WAIT/提案与父805有限requiredP3各自时点；本次新增票0。", remains_open="历史原56/37、limits、optional/Float/policy/no-required及canonical/alias由父实际核验。"),
    ], parent_interfaces_closed=0, parent_scope_unread_is_not_host_limit=True,
    parent_owned_125_reverse_and_213_payloads=True,
    excluded_ranges=[dict(domain="MOVE_DESCRIPTIONS", records=[1, 114], owner="records_a"),
                     dict(domain="POKEDEX_ENTRIES", records=[249, 1028], owner="records_c")],
    behavior_execution="NOT_EXECUTED", UPDATE_NOT_STARTED=True))

put("proposal-counters.json", dict(schema="r8-elr-records-b-proposals/v1",
    new_proposals=[], new_proposed=0, new_required=0, new_optional=0, new_policy=0,
    new_independent_countervotes=0, new_global_no_required_decision=False,
    finite_review_reason="全部1620对作为本地化数据及现WP08有限合同已有覆盖；具体反方及正确scope见semantic-review S4。",
    retained_parent_status=dict(id="GR8-ELR-001", source="fixed805/report.md完整阅读027375",
        status_as_reported="主审有限required/P3; historical canonical/alias OPEN",
        adopted_as_new_independent_vote=False,
        full_proposal_counterreview_history_received_here=False,
        current_global_adjudication="PARENT/ROOT_EXCLUSIVE"),
    UPDATE_NOT_STARTED=True))

frozen = json.loads((OUT / "frozen-denominator.json").read_text())
frozen.update(input_status="ALL_FIXED_IDENTITIES_VALID; parent_worktree_successors_separate",
              status="READY_FOR_PARENT_RECORD_RECEPTION", record_ids_exact=True,
              actual_records_read=1620, actual_fields_read=3240,
              actual_context=CONTEXT, actual_agent_id="UNVERIFIED",
              self_spawned_contexts=0, actual_configuration={k: "UNVERIFIED" for k in ["model", "effort", "tier", "speed", "Fast"]})
put("frozen-denominator.json", frozen)

assert sum(x["count"] for x in batches) == 1620
assert set(x["id"] for x in reading_records) == set(READSET["record_ids"]) == set(x["id"] for x in reception_records)
assert all(not x["finite_unresolved"] for x in reception_records)
put("local-validation.json", dict(evidence_level="TOOL_VALIDATION", exact_id_sets=True,
    count=1620, fields=3240, continuous_assigned_runs=READSET["ordered_runs"],
    complete_literal_batches=9, batch_gaps=0, batch_overlap=0,
    unread_records=0, unresolved_necessary_shard_definitions=0,
    new_behavior_executions=0, tests="No gameplay/model/old-script execution; mechanical ledger and input checks only.",
    UPDATE_NOT_STARTED=True))
print("Final ledgers: exact1620 IDs /3240 fields,9 complete literal batches,15 necessary R/B8 file scopes; no record gaps.")
