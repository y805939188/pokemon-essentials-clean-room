"""Write this reviewer's scoped decision and exact input receipt."""
import datetime,json,os
from pathlib import Path
E=Path(__file__).resolve().parent;F=E/'inputs'
def write(name,v):(E/name).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat();ctx=os.environ['CODEX_THREAD_ID']
freeze=json.loads((F/'candidate-input.json').read_bytes());audit=json.loads((E/'input-validation.json').read_bytes());extra=json.loads((E/'additional-input-validation.json').read_bytes())
config={'requested':{'model':'gpt-6.1-sol','reasoning_effort':'ultra','service_tier':'default','speed':'normal','Fast':'PROHIBITED'},'effective':{k:'UNVERIFIED' for k in ['model','reasoning_effort','service_tier','speed']},'qualification':'No effective platform configuration echo. Request, PID, environment identity and successful tooling cannot attest model/effort/tier/speed. No quota or authentication inspection.'}
identity={'thread_id':ctx,'session_id':os.environ['CODEX_SESSION_ID'],'parent_source_thread_id':'01a13f49-a154-7054-9b04-ce31f924d01c','platform_task_id':'NOT_EXPOSED','internal_task_id':'NOT_EXPOSED','recording_pid':os.getpid(),'utc':now,'role':'R7-U07-reviewer-r2','auxiliary_agents_or_model_calls_created':0,'actual_environment_id':'ccarenv_b64_Y2NhcmVudl9iMzZiZWVjYjE0M2M4MTkxYmY0MTMzMWJkOGJhZjhlNw','qualification':'Actual visible environment CODEX_THREAD_ID/CODEX_SESSION_ID; no opaque platform identity inferred from role/PID.'}
independence={'author_context':'01a13f7f-7ae8-735b-86d1-876a3b9fe03b','old_r1_context':'01a13ff0-841d-7542-9d3a-d87b0e0cb00d','parent_source_context':'01a13f49-a154-7054-9b04-ce31f924d01c','reviewer_context':ctx,'different_visible_actual_contexts':ctx not in ['01a13f7f-7ae8-735b-86d1-876a3b9fe03b','01a13ff0-841d-7542-9d3a-d87b0e0cb00d','01a13f49-a154-7054-9b04-ce31f924d01c'],'author_internal_context':'Exposed in exact author per-id/report/001 identity; matches externally supplied author ID. No role-name equivalence inference.','subtasks_created':0,'qualification':'New context; no subtask/agent/model created before or after reading the full dispatch. No self-authoring or self-integrated-review role.'}
premises='受控直接工具边界：训练家索引0、类型、姓名及胜负台词有效，相关训练家表两次读取一致；候选[]、模板[]、建议3；有效受伤非空玩家队伍，Tower单场，明确无等级调整，非debug skip，场景创建及之前依赖正常。无默认PBS/Demo可达或外层统一恢复断言。'
def src(path,scope):return {'commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','path':path,'lines':scope}
foes='Data/Scripts/018_Alternate battle modes/001_Battle Frontier/003_Challenge_ChooseFoes.rb';session='Data/Scripts/018_Alternate battle modes/001_Battle Frontier/001_Challenge_BattleChallenge.rb';battles='Data/Scripts/018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb';rules='Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/001_Challenge_ChallengeRules.rb';data='Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb';trainer='Data/Scripts/015_Trainers and player/001_Trainer.rb';recorded='Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb';battle='Data/Scripts/011_Battle/001_Battle/001_Battle.rb'
rows=[
('C1',110,'零候选', '[]/[]、建议3令短名单分支零次迭代；NPC初始队伍为空；会话不做补齐/整队校验，填文本后调用包装。包装先治疗、取物品，正常场景之后记录构造继承空对手门拒绝。',[src(foes,[39,83]),src(trainer,[163,194]),src(session,[95,104]),src(battles,[40,59]),src(recorded,[15,22]),src(recorded,[228,232]),src(battle,[98,103])]),
('C2',111,'正编号缺模板','[0]/[]实际调用缺失条目的个体创建，在生成入口失败，未进入包装治疗；与零候选明确分阶段。',[src(foes,[59,68]),src(session,[95,104])]),
('C3',112,'普通短名单','合法[0,1]/两模板及[0]/一模板按原序返回2/1；短名单分支没有补齐或最终整队校验。不据此保证完整对局。',[src(foes,[59,83])]),
('C4',113,'无调整与物品','无调整返回nil，不产生经验数组；之后玩家物品逐位置取值，对手迭代零次得到[]，nil和[]不混同。排除原提案的宽经验快照叙述。',[src(rules,[9,14]),src(rules,[61,68]),src(battles,[50,59])]),
('C5',114,'跳过与取消','调试跳过先清临时记录并返回true，尚未治疗/调整/构造；UI nil是另外入口，条件不提交旧报名P，活动会话亦不覆盖。保留WS-W29/W35，不以取消替代空对手。',[src(battles,[40,50]),src(data,[38,49]),src(session,[196,203])]),
('C6',115,'异常部分提交','构造拒绝在正常还原70行、末尾清记录85行和胜负统计89行之前；玩家治疗已提交，旧临时记录可保留，统计不增。记录构造的局部初始化不等于清全局旧记录；无统一回滚或未来必须保留策略。',[src(battles,[40,96]),src(recorded,[15,22]),src(battle,[98,103])])]
vectors=[{'id':'GR7-M12-001-'+i,'label':label,'static_content_result':'PASS_SCOPED_CANDIDATE','candidate_catalog_line':line,'reason':reason,'source_support':sources,'evidence_stage':['SOURCE_STATIC','DERIVED_VECTOR'],'execution':'NOT_EXECUTED','reference_execution':'NOT_EXECUTED','model_execution':'NOT_EXECUTED','host_execution':'NOT_EXECUTED'} for i,line,label,reason,sources in rows]
history=[{'id':'WS-W31','result':'PRESERVED_STATIC','evidence':'B catalog97 == current catalog97; generator62–68; full old catalog bytes preserved.'},{'id':'QC-Q46','result':'PRESERVED_STATIC','evidence':'B/current catalog56 unchanged; wrapper40–96; constructor failure adds earlier pre-battle prefix, no rollback.'},{'id':'FC-17','result':'PRESERVED_STATIC','evidence':'Fixed B factory catalog70–90, WP57 9–57/87–116, different factory generator88–164; empty pool still attempts creation and may retain temporary number. No new factory runtime certification.'},{'id':'WP54 §4','result':'PRESERVED_STATIC','evidence':'Read65–110; §4.1 no-adjustment nil remains controlling exception to generic adjusted-flow summary.'},{'id':'WP76 scope/estimator','result':'PRESERVED_STATIC','evidence':'Read1–47; author generation and estimator remain separate from regular NPC generation and real battle behavior.'},{'id':'Other QC/WS/PA/RC rows','result':'BYTES_PRESERVED_ONLY','evidence':'Complete B/current catalogs read; exact only insertion103→104–116. No new semantic certification of unrelated rows.'}]
unmet=['R7-I serial clause-level integration of actual candidate bytes and shared catalog/semantic-owner reception','Fresh different-context R7-IR of exact actual cumulative integrated commit/tree','Precise original historical regression and direct/transitive domain dependency reception before root formal acceptance/closure']
per={'schema':'r7.u07.r2.reviewer-per-id.v1','batch_id':'R7-U07','review_round':'r2','utc':now,'actual_context':identity,'independence':independence,'configuration':config,'dispatch_commit':'c64774c60d91e522cb515ef71e3e9d4ea6b4712c','freeze_commit':'aa369555b0e8b6c8b077f964b54ed63d3b924f26','freeze_tree':'08bd0f362c74ef7645b5bbd70b557489c122ae29','candidate_commit':freeze['candidate_commit'],'candidate_tree':freeze['candidate_tree'],'required_ids':['GR7-M12-001'],'records':[{'record_id':'GR7-M12-001','classification':'required','severity':'P3','decision':'PASS_SCOPED_CANDIDATE','candidate_blockers':[],'premises':premises,'full_original_seven_groups_read':True,'raw_original':'e0c5ebb227169d6a24ca470630bdc0c22f4ea8f8a70a89951fae64546dde22ae:/records/14; bytes416485..450531','raw_nonauthor':'bcf3539beb2c1c24c44f3cd426dd4b4a49752b1a39d30925effb32a36b6329d6:/challenges/3; bytes50839..68277','vectors':vectors,'historical_regressions':history,'conditional_sync':{'requested_targets':[],'needed_extra_targets':[],'reason':'Only §2.5 precise attempted-creation and no-adjustment branch plus §4 cross-link, adjacent new vectors; WP54 existing no-adjustment exception retained, no contradiction requiring broader policy adoption.'},'shared_contribution':{'conflict_groups':[],'blocking_author_edges':[],'record_to_record_direct_transitive_scheduling_edges':[],'qualification':'Empty schedule/conflict set does not certify other batches or eliminate domain/shared-catalog obligations. R7-I must apply clauses, not whole-mirror overwrite.'},'unmet_integration_closure_dependencies':unmet,'candidate_files':[r for r in freeze['candidate_and_author_evidence_file_identities'] if r['role']=='candidate_mirror']}],'old_r1':{'commit':'c651d5599badf5fb9f99c05d307f1d7d70374ab7','tree':'515114b8ea1fdf7154ed47d812c88cb0eed5716c','reported_content_assessment':'PASS_SCOPED_CANDIDATE','final_qualification':'WAIT_INPUT_OR_INDEPENDENCE','prohibited_helper_creation_disclosure':'RETAINED_UNWAIVED','semantic_PASS_inherited':False,'blame_not_reassigned_to_author':True},'execution':{'source_static':'Fresh named scopes and complete B/candidate documents read','derived_vectors':'Six manually reconciled; NOT_EXECUTED','tool_validation':'Fixed bytes/modes/scope/raw bindings/manifest only','reference_observation':0,'reference_processes':0,'behavior_models':0,'independent_full_model':0,'game_host':0,'Demo':0,'native_media':0,'real_save_replay':0},'retained_boundaries':{'L01_L14':'RETAINED exactly in inputs/limits-and-alias-reception.json','old56_92':'UNCHANGED','denominator':'27 required / 13 batches','unadopted':'7 optional / 2 navigation facets / 1 no-required / 2 policy','R7_aggregate_H14_UTIL03':'Existing1 isolated Ruby2.6.10 reference process /10 inputs remains aggregate historical fact; this reviewer adds0, old NOT_EXECUTED not rewritten.'},'gates':{'candidate':'PASS_SCOPED_CANDIDATE','integrated_PASS':'NOT_ASSERTED','ACCEPTED':'NOT_ASSERTED','CLOSED':'NOT_ASSERTED'}}
write('per-id.json',per)
receipt={'schema':'r7.u07.r2.review-input-receipt.v1','utc':now,'actual_context':identity,'independence':independence,'configuration':config,'fixed_B':freeze['fixed_B'],'base_top_tree':extra['base_top_tree'],'base_formal_tree':extra['base_formal_tree'],'dispatch':next(x for x in audit['fixed_byte_inputs'] if x['name']=='dispatch'),'original_contract':freeze['original_contract_commit_path_identity'],'freeze':{'commit':'aa369555b0e8b6c8b077f964b54ed63d3b924f26','tree':'08bd0f362c74ef7645b5bbd70b557489c122ae29','input_path':'review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U07/candidate-input.json','frozen_review_round_field':'r1 retained original freeze; current dispatch r2 explicitly reuses same unchanged candidate'},'candidate':{'commit':freeze['candidate_commit'],'tree':freeze['candidate_tree'],'author_branch':freeze['author_output_branch'],'author_context':freeze['author_task_id'],'files_received':audit['candidate_files_count'],'bytes_received':audit['candidate_bytes'],'file_identities':audit['candidate_files'],'complete_diff_against_B':audit['complete_diff']},'original_restoration':{'destination':'/workspace/r7-context/R7-U07-reviewer','files':23,'bytes':5526711,'receipt':next(x['path'] for x in extra['copied_exact_inputs_and_receipts'] if '/receipts/original-' in x['path'])},'candidate_restoration':{'destination':str(Path('/workspace/r7-review-input/R7-U07-r2-2649ed2bd2cc3afdfa636cd643fc1975de5eae32')),'receipt':next(x['path'] for x in extra['copied_exact_inputs_and_receipts'] if '/receipts/candidate-' in x['path'])},'byte_qualification':'All32 exact restored candidate bytes independently matched actual fixed commit/tree/blob/mode and freeze/root tables; original23 matched plan; 54 restored raw references and31 author manifest nonself declarations verified. This is TOOL_VALIDATION only.','detailed_validation':['input-validation.json','additional-input-validation.json','read-ledger.json','supplemental-input-receipt.json'],'skills':extra['skills_probe'],'initial_logging_gap':'Pre-001 bootstrap fetch/raw reads/AGENTS/tool/plan/worktree/original restore were real visible tool calls without independent per-command UTC/PID/separated-stream files. Original restore has genuine per-HTTP receipt; later fixed-byte rereads are separately logged. Do not retroactively invent initial logs. Initial git show before fetch failed128 because fixed object absent; successful exact fetch followed.','reviewer_validation_correction':'Log030 matched bytes/scope/raw refs but mistakenly counted0 manifest declarations due nested after schema. Corrected checker directly validates all31 manifest files with assertion; log031 records31. Log030 retained without semantic credit for absent manifest check. No candidate edits.','artifact_scope':'Only candidates/R7-U07/evidence/reviewer/r2/; own clean checkout from B; sole ordinary-push output branch codex/r7-u07-reviewer-20261015-r2; no force, author/formal/shared/main/tag writes.','prior_r1_preserved':'Exact four fixed r1 files retained under prior-r1/ for history only, old final WAIT not waived and no semantic reuse.'}
write('review-input-receipt.json',receipt)
report='''# R7-U07 r2 新 context 完整独立候选复审

GR7-M12-001：**PASS_SCOPED_CANDIDATE**，仅限固定候选的 P3 最低行为合同。C1–C6 均通过本次独立静态内容核对，执行全部 **NOT_EXECUTED**。本审者没有创建任何辅助 agent、子任务、子会话或模型调用；未参与作者修改，不担任实际整合后的 R7-IR。没有宣告实际整合 PASS、正式接受或关闭。

## 身份、固定版本与输入

实际可见 reviewer thread/session 为 `CTX`（环境 CODEX_THREAD_ID/CODEX_SESSION_ID，日志001）；父 source thread `01a13f49-a154-7054-9b04-ce31f924d01c`。作者真实 context `01a13f7f-7ae8-735b-86d1-876a3b9fe03b` 在冻结、作者报告、per-ID及001身份日志中一致；旧 r1 为 `01a13ff0-841d-7542-9d3a-d87b0e0cb00d`，与当前均不同。独立 platform task/cloud 创建回执、内部 task ID 未暴露，不用角色名/PID伪造。当前记录 PID/UTC 见 receipt/真实日志。

本轮完整派发固定 `c64774c60d91e522cb515ef71e3e9d4ea6b4712c`，路径 `review/remediation-seventh-20261015-prepare/review-rechecks/R7-U07/r2/reviewer-dispatch.md`，14,677字节，SHA256 `4deae80f611a66adfc14f86345ab49eecb5c14208c1a1cccd57990db76aafba3`。最初直接读该路径的Git对象因未fetch而失败128，随后固定raw全文读取和指定远端fetch均取得相同合同；从未委派工作。旧通用“尚未创建/禁止推送”时点及旧eligible列表由本轮具名r2/普通推送授权覆盖，其它输入/边界不变。

| 输入 | 固定身份 |
| --- | --- |
| B | `e646432c644dec04d306842cc5a559a29c718fbc`；顶层tree `84f79ec6e772aacbf3a464fde68cdc5a280e2950`；正式子树 `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c` |
| 原七组完整合同 | `f622356f3beb9e84ea8cff9db07c7fb382565d3f:review/remediation-seventh-20261015-prepare/delegation/contracts/R7-U07.json`；31,810字节，SHA256 `dc8947aa7703ac5805cd55355ca4a072df2c5835c96661102d2a4fb0d203f920` |
| 固定恢复工具/原清单 | `658488c81f1f3181a488298ab27850c8af951d73`；全文读后运行 |
| 冻结 | commit `aa369555b0e8b6c8b077f964b54ed63d3b924f26` / tree `08bd0f362c74ef7645b5bbd70b557489c122ae29` |
| 候选 | commit `2649ed2bd2cc3afdfa636cd643fc1975de5eae32` / tree `6b2e6a6122cb24b330a052137750dc985908e796`；作者分支 `codex/r7-u07-author-20261015-wave1` |
| R | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，给定tree `7589c800b61ba13a13040ed0d686979b80a84fd0`；仅具名快照，不声称重核参考整树 |

按合同在本容器分两次实际恢复，未假定共享目录：原输入到 `/workspace/r7-context/R7-U07-reviewer`，23文件/5,526,711字节；候选到 `/workspace/r7-review-input/R7-U07-r2-2649ed2bd2cc3afdfa636cd643fc1975de5eae32`，32文件/241,426字节。真实HTTP回执在 `receipts/`，工具返回均完整。原输入/候选未改写，也未执行下载的作者、参考或native程序。

重新核全部32个候选文件的bytes/SHA256/Git blob/100644模式及实际Git tree，冻结表和根完整远端接收表逐项一致；作者31个非自身manifest声明全部匹配，自身由固定commit/tree绑定。54处已恢复raw字段/成员的偏移、raw SHA、JSON pointer与canonical SHA重新匹配。上游inventory/别名元资料未选原件不获新增语义信用，也不被标成材料limit。详情 `input-validation.json`、`additional-input-validation.json`、`review-input-receipt.json`。

项目AGENTS.md全文已读，遵守clean-room行为规格约束。workspace、两个项目checkout与可见agent-home `.agents/skills` 均不存在；固定派发tree无 `.agents` 载荷；未声称使用缺失技能，未访问认证/额度。

## 独立内容判断

本次亲自读原七组、normalized本记录七组、根 `/records/14` 全文（含原提案和缩窄裁决）及非作者C05 `/challenges/3` 全文，分别绑定raw区间416485..450531和50839..68277；最低修订与全部保留项由C05已接缩窄P3合同支配。较宽P2、普通Demo受阻、无调整仍存经验数组等原主张不恢复。

两份B原正文/目录以及两份完整候选正文/目录全部新读：候选WP55为152行/24,678字节，目录190行/35,869字节；读取与证据范围见 `read-ledger.json` 和日志003–039。源/消费者具名链实际读ChooseFoes1–164、BattleChallenge1–429、Challenge_Data1–219、Challenge_Battles1–144、ChallengeRules1–150、Trainer150–194、RecordedBattle1–40和215–245、Battle85–150。其它未读补集不冒称完成。

主要夹具仅是受控直接工具输入：训练家0及类型、姓名/胜负台词有效，相关训练家表两次读取一致，候选[]/模板[]/建议3，玩家有效非空且受伤，Tower单场、明确无等级调整，非debug skip，场景创建及之前依赖正常。生成和会话分别读取训练家内容，故不能省略读取一致/文本正常前提；不推默认PBS或普通Demo能产生本例。

| 向量 | 本次结论及理由 | 候选目录行/主要源依据 |
| --- | --- | --- |
| C1 | PASS：空名单令短分支零次创建，NPC初始空队伍原样返回；会话填台词后才进包装，先治疗，后于记录构造继承空对手门拒绝 | 110；ChooseFoes39–83、Trainer163–194、BattleChallenge95–104、Challenge_Battles40–59、RecordedBattle15–22/228–232、Battle98–103 |
| C2 | PASS：正编号[0]/空模板确实尝试缺项，在个体创建入口失败；还没进入单场治疗 | 111；ChooseFoes59–68、BattleChallenge95–104 |
| C3 | PASS：合法两项/一项按原序返回2/1，不补齐、不最终整队校验；不保证完整战斗成功 | 112及原WS-W31；ChooseFoes59–83 |
| C4 | PASS：无调整返回nil，非经验数组；随后按位置取物品，空对手物品列表是[]，两个值不混同 | 113；ChallengeRules9–14/61–68、Challenge_Battles50–59 |
| C5 | PASS：debug skip先清临时记录、返回true，治疗/调整/场景构造均未到；UI nil另入口不提交也不覆盖旧报名P | 114及WS-W29/W35；Challenge_Battles40–50、Challenge_Data38–49、BattleChallenge196–203 |
| C6 | PASS：构造异常发生在正常还原、末尾清记录和统计之前；治疗已提交，旧记录可保留，统计不增，无统一回滚 | 115；Challenge_Battles40–96、RecordedBattle/Battle具名构造链 |

还独立尝试以下反驳：短名单既有规则逻辑包含零，却不能消除旧末句对空模板的局部全称误述；WP39后阶段空队门也不能让错误的早失败预期成立。记录构造的局部数组初始化不会清全局旧临时记录。debug skip与入口nil取消须分开，不反驳非skip的空候选例。无调整在WP54 §4.1明列返回空记录，候选§2.5再次明列；WP55 §3引用主合同的通常调整流程不能被读为覆盖无策略分支，不需要越出本合同改写该泛化接点。原作者较宽“经验分量”表述已被C05反证排除，本候选没有带回。

## 最小范围、保留与接收

对B完整差异是32个新增且全在 `candidates/R7-U07/`。两份完整镜像只有WP55原93行→候选93–95、原124行→候选126；目录仅原103行后插入候选104–116，其余33,561个B目录字节全保留。新正文与向量是独立行为说明，没有移植结构、引擎/适配器实现或参考程序修补。具体差异在 `wp55-diff.patch` / `catalog-diff.patch`，是审查证据，不是实际整合补丁授权。

WS-W31长度1/2原序不补齐与QC-Q46正常/异常/部分提交范围均新核且原行保留。另从固定B定向新读FC目录70–90及WP57 9–57/87–116，结合独立工厂生成88–164：空工厂池仍实际抽取/创建，临时人数可能滞留，不能套用普通训练家零迭代结论。WP54 65–110的无策略/索引还原、WP76 1–47的作者生成器/真实与估算分流保持；其它QC/WS/PA/RC行的原字节保留不代表本审者重新认证所有无关行为。

无conditional目标、无已登记共享冲突组、无作者阻塞边，也未接具名record→record直接/传递排程边；这不消除领域依赖。仅能由R7-I按条款串行接收WP55局部贡献及相邻六向量，不能整份镜像覆盖其他累计贡献。Feature Matrix/追溯与公共台账仍归R7-I，其他批次接收未在本轮认证。

待满足：R7-I真实条款整合及共享目录/语义owner接收；新不同context R7-IR审真实累计整合commit/tree；原验收/精确历史回归与直接/传递领域依赖完整接收后，根再处理正式接受与关闭。当前候选级没有新增语义/输入/独立性阻塞；以上后续门继续保留。

## 历史资格、执行与发布

旧r1固定 `c651d5599badf5fb9f99c05d307f1d7d70374ab7` / tree `515114b8ea1fdf7154ed47d812c88cb0eed5716c` 的四文件完整按固定URL读取、再与Git blob核等，原样保存在 `prior-r1/`。旧报告的内容PASS及“合同前创建只读辅助”披露保留，其最终资格 **WAIT_INPUT_OR_INDEPENDENCE** 未豁免，未归为作者语义错误。读取旧报告仅用于历史保留，在本次源/候选/反证独立核对之后；没有迁移旧PASS。

请求gpt-6.1-sol/ultra/default/普通速度、禁Fast；实际model/effort/tier/speed无有效回参，逐项 **UNVERIFIED**。环境thread/PID、请求或exit0均不证明有效模型配置。SOURCE_STATIC、六个DERIVED_VECTOR与TOOL_VALIDATION分别登记；本审者新增参考观察/进程、行为模型、独立完整模型、宿主、Demo、native媒体和真实存档回放均0。所有向量NOT_EXECUTED。原R7整体H14/UTIL03的一进程十输入仍是原聚合事实，不改写旧任务的NOT_EXECUTED，也不算本审者执行。

L01–L14已全文读并原样保留于 `inputs/limits-and-alias-reception.json`；旧56/92、27项/13批分母和7 optional/2导航facet/1 no-required/2 policy未采用边界不变。可读但未读补集不以limit豁免。

初始fetch/原始读取/worktree/第一次恢复发生在公开工具会话，尚无单独逐命令UTC/PID/分离流档案，不补造初始日志；第一次恢复自带逐HTTP真实回执。日志001起完整保存具名命令的公开argv/cwd/PID/UTC/stdout/stderr/exit，不保存私有模型流。日志030首次审计因author manifest的after嵌套结构漏遍历，明确计数0；其字节/范围/raw匹配不冒充manifest核验。修正后日志031断言全部31项，旧日志不删除。作者旧001/009失败和初始日志缺口亦保留，没有被成功机械检查洗掉。

所有仓库新写入限 `candidates/R7-U07/evidence/reviewer/r2/`，从B独立干净worktree创建唯一成果分支 `codex/r7-u07-reviewer-20261015-r2`；建前同名远端无成果，发布前再核。只普通commit/push，无force；未checkout作者分支或改作者候选、正式正文/公共台账、main/tag/旧r1。载荷先发布并全量远端读回，再仅收入真实发布回执及manifest；最终commit/tree与最终所有文件（含manifest自身）的完整远端读回在最终工具回传包外绑定，避免循环自引用。传输成功不赋实际整合/接受/关闭资格。
'''.replace('CTX',ctx)
(E/'report.md').write_text(report)
with (E/'report.md').open('a') as f:
 f.write('\n发布前manifest自检另发现自写生成器按文件名排除自身，误把r2内原样保留的 `prior-r1/artifact-manifest.json` 也排除。首次公开组合检查失败；随后日志043真实复现AssertionError/exit1，旧r1副本始终未丢失或改写。已改为仅排除根manifest精确路径，再生成并核对完整文件集。该问题仅在本审者证据打包，未修改候选，也不提高语义/运行资格。最终成功检查及完整远端回读另作真实记录。\n')
 f.write('\n日志046保留全证据 `git diff --cached --check` 的exit2：仅三份.patch原样证据中的14个统一diff空上下文行被判尾空白。此类行的单空格是patch数据，冻结mirror-diffs与新独立diff均保持实际字节；不修剪证据。日志047具名排除这三份patch后其余文件检查exit0，范围/身份审计仍全量覆盖三份patch。\n')
receipt['reviewer_manifest_correction']='Prepublication generator incorrectly excluded all artifact-manifest.json basenames including exact old-r1 copy. Actual files intact; validator caught missing declaration. Log043 preserves real AssertionError/exit1; corrected exclusion only root manifest exact path; final complete inventory and remote readback required.'
receipt['whitespace_check_qualification']='Log046 full staged diff --check exits2 solely for14 single-space unified-diff context lines in3 exact .patch evidence files. Preserve these data bytes. Log047 names exactly3 exclusions and checks all nonpatch files exit0; identity/scope checks still include every patch.'
write('review-input-receipt.json',receipt)
print(json.dumps({'written':['report.md','per-id.json','review-input-receipt.json'],'record':'GR7-M12-001','decision':'PASS_SCOPED_CANDIDATE','vectors':6,'vector_execution':'NOT_EXECUTED','actual_context':ctx,'configuration':'UNVERIFIED'},ensure_ascii=False))
