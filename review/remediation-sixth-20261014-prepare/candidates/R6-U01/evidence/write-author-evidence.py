from pathlib import Path
import json,hashlib,datetime,subprocess
P=Path('review/remediation-sixth-20261014-prepare');E=P/'candidates/R6-U01/evidence';M=P/'candidates/R6-U01/mirror';c=json.loads((P/'contracts/R6-U01.json').read_text());pay=json.loads((E/'candidate-payload-identities.json').read_text());src=json.loads((E/'source-payload-identities.json').read_text());checks=json.loads((E/'validation.json').read_text());records=[]
ident=lambda b:{'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
examples={
 'GR6-K-001':[
  {'vector':'MG17','premise':'有效背包、低于20的版本、旧游标2／另一大小写旧值8／当前3；目标转换正常到达','derived':'当前2／旧游标仍2／另一旧值空。其它三个分支迁入清旧；旧游标空对照不覆写。'},
  {'vector':'MG18','premise':'MG17后普通导航写当前5；重复单对象入口收到同一旧版本上下文','derived':'当前回2／旧仍2；所给版本上下文不被该入口推进。没有默认普通启动反复执行的断言。'},
  {'vector':'MG19','premise':'完整正常链所有前后置成功、当前引擎至少20；或独立给20／21的单对象版本上下文','derived':'整链推进两个版本标记；后续普通读取或当前版本对照不再选择v20。真实文件I/O未执行。'}],
 'GR6-K-002':[
  {'vector':'CI-29','premise':'固定直接构造；普通整数／文本；无自定义相等／散列或包装；依次id/name/gender/language','derived':'(0,0,0,2)和(1,0,0,2)接受并原样存名字整数0；(0,Valid,0,2)正常文本接受。已有Owner的创建消费按原样接收，不保证后续畸形值可消费。'},
  {'vector':'CI-30','premise':'同条件；(1,0,1,2)与(0,0,1,2)独立','derived':'名字条件仍在，两者报参数错误且四字段未赋；只与前面的id同值不产生后项遮蔽。'},
  {'vector':'CI-31','premise':'已合法拥有者名字Valid，单字段写0／独立写New','derived':'0拒绝且原名Valid；文本New正常写入。语言来源／默认与单字段校验保留。'}],
 'GR6-K-003':[
  {'vector':'BR27','premise':'默认Shellos雌性物种亲本0和合法适配雄性；子代0／5120；无强制形态／插件／更早登记，依赖正常，玩家／Dex存在且记录初空','derived':'同值母系提交仍清特性缓存／重算／登记；蛋0／5120保持。填性别／普通异色，seen／seen-form／首写last；owned与seen-egg不写。概念省略提交的对照不是正常替代流程。'},
  {'vector':'BR28','premise':'BR27分别去掉全局玩家／Dex；另只给非空last','derived':'缺对象仍提交重算而跳过登记，无该登记填两缓存；非空last保持但seen／form仍写。'},
  {'vector':'BR29','premise':'同语种且无Charm，N=0，母系提交后已填普通异色；与此前未读取夹具独立比较','derived':'N0不读不清，已填保持／未填仍未填。N≥1轮首读与末次可能空、旧性格缓存按原BR10/22–24保留。'},
  {'vector':'BR30','premise':'独立受控故障前提：重算失败／登记刷新失败；另正常产蛋后队伍满领取拒绝','derived':'分别停于已写形态清特性而登记未到／seen-form-last和两缓存写入后刷新失败／未入队而先前登记保留。不是默认源失败必然性，不补回滚或后段成功。'},
  {'vector':'BR31','premise':'合法已登记的母系／族内／永石条件，母0父1，依赖正常；独立移除母方资格；另非零Shellos母系','derived':'母系0提交；首个合格母方永石0再次提交并停，不试父1。母不合格则父1提交；非零母系结果沿既有BR07。'}]
}
chains={
 'GR6-K-001':'005_Game_SaveConversions:207–230生产当前位置；003_SaveData_Conversion:170–223区分筛选／正常链版本写入／单对象不推进版本；008_PokemonBag:4–54提供当前游标；007_UI_Bag:145–224、388–423消费／导航写当前值，590–600过滤选择正常返回恢复当前游标。保存链版本推进保留WP10§3.4；普通UI及真实旧档未运行。',
 'GR6-K-002':'004_Validation:12–30检查已形成的值条件；005_Pokemon_Owner:19–25同时提交条件、成功后原样赋四项，45–65单项校验；001_Pokemon:1159–1227完整创建、1198–1205接收已有Owner原样使用，840–843物主赋值只验记录类型。foreign?:847–849读取id/name；不证明畸形名字可通过所有UI／存档消费者。',
 'GR6-K-003':'Species:175–221、243–253给base0／default-form；pokemon.txt:11113–11140完整Shellos记录，forms1119–1123形态1；完整FormHandlers1–792无Shellos默认处理器。DayCare21–90先设蛋步数后母系／永石裸提交；Pokemon159–184无同值／蛋守卫、341–399登记读缓存、1099–1127重算不读两缓存；Pokedex195–219写seen/forms/首次last而无owned／seen-egg写；DayCare239–255 N0不读不清、488–495产出后才检查领取容量。'}
failures={
 'GR6-K-001':'无交互取消。当前游标复制先于其它字段处理；后段失败不撤销前缀。整链失败不推版本或写回已成功；无一般异常对象全集保证。',
 'GR6-K-002':'无交互取消。未通过的构造校验早于四赋值；通过碰撞例四值原样赋。单字段错误早于该字段变更。记录类型接收不保证下游畸形值操作成功。',
 'GR6-K-003':'无生成通道交互取消。写形态／清特性先于处理器、重算、登记；登记读性别异色先于seen/form/首次last；刷新在其后。各故障只证明到达前缀；生成后的领取容量失败没有撤销图鉴记录。'}
repairs={
 'GR6-K-001':{'changed':['generic-kernel/wp10-migration-failure-recovery.md','test-catalog/generic-kernel-wp05-06-07-08-09-10.md'],'rule':'WP10§4目录行拆分旧游标复制／保留与其它三字段清旧；§4.3写旧上下文重复入口和整链成功版本对照；MG17–19同步。','preserved':'WP27§5 registered两字段改名清旧正确，整份原字节保留；WP10正常版本推进、其它13转换／两植物转换数据／回滚限制保留。'},
 'GR6-K-002':{'changed':['creature-rpg/wp18-creature-identity-species-ownership.md','test-catalog/creature-rpg-wp18-20-24-25-26.md'],'rule':'WP18§6.1保留校验存在、正常类型与语言来源，补同值直接构造例外及setter对照；§9收窄全称错型拒绝；CI29–31同步。','preserved':'合法输入、语言默认与GR-009；记录默认全集、普通创建回调／缓存、物主接收及外来判定、毫米尺寸；其余全部旧CI/HP/PT/PS/AQ行原字节。'},
 'GR6-K-003':{'changed':['pokemon-rules/wp34-inheritance-and-offspring.md','pokemon-rules/wp62-pokedex-records-regions-and-content.md','test-catalog/pokemon-rules-wp19-21-22-23-34.md'],'rule':'WP34§5.2连接既有WP21提交合同，§9.4纠正同值无操作，§8.2限定N0已填／未填；WP62§3.1/3.2/集合附表连接产蛋边界；BR27–31同步并跨图鉴引用。','preserved':'WP21整份正确同值规则原字节；WP62构造期UNOWN登记、全局／战斗接收者分层、普通形态首写last与owned/seen-egg独立、区域／显示门。亲本归一、地区／母系／永石顺序、所有随机通道、N≥1轮首／末次空与性格缓存原字节。'}
}
for old in c['scope_contracts']:
 id=old['id'];r=repairs[id];changed=['deliverables/final-specification-set/'+p for p in r['changed']];source_names={x['payload_identity']['path'] for x in old['bidirectional_evidence']['source']}
 if id=='GR6-K-003':source_names|={'Data/Scripts/010_Data/002_PBS data/008_Species.rb','PBS/pokemon_forms.txt'}
 records.append({'identity_and_verdict':{'canonical_id':id,'aliases':[],'root_cause':id,'classification':'required','severity':old['identity_and_verdict']['severity'],'original_decision':old['independent_adjudication']['decision_reason'],'author_state':'AUTHOR_COMPLETE_STATIC_CANDIDATE_READY','original_formal_primary':old['identity_and_verdict']['primary_contract'],'candidate_payloads':[x for x in pay if x['formal_path'] in changed]},'bidirectional_evidence':{'level':'SOURCE_STATIC','fixed_reference_commit':c['frozen_reference'],'source_identities':[x for x in src if x['path'] in source_names],'producer_consumer_save_display_chain':chains[id],'current_formal_read':'All nine specified formal files read fully from fixed main; hashes validated. Exact replacement replay and unchanged-span checks bind candidate.','original_proposal_read':'Complete original_full_proposal inside full byte-identical contract/prompt, not inherited reading credit.','nonproposer_counter_read':'Fresh full inputs/evidence/tasks/R6-O/counter-K-'+id[-3:]+'.json plus independent-K-'+id[-3:]+'.json; exact input identities in input-evidence-identities.json. Historical counter not current candidate review.','negative_scope':'No full-repository absence claim. Named complete source units/current formal files and focused two-PBS evolution field search only.'},'premises_and_counterexample':{'level':'DERIVED_VECTOR','valid_domain':old['premises_and_counterexample']['input_domain'],'normal_and_counterexamples':examples[id],'cancel_failure_partial_prefix':failures[id],'new_actual_execution':0,'historical_execution':'Original K missing UTC/independent Rubyexit preserved; O owner run remains historical. Neither promoted to this author run.'},'minimum_revision_contract':r,'acceptance_and_regression':{'author_static_vectors':[dict(x,author_static_result='SUPPORTED_BY_FRESH_SOURCE_READ',actual_execution='NOT_EXECUTED') for x in examples[id]],'tool_receipt':'validation.json: '+str(len(checks['checks']))+' finite checks; separate from behavioral execution','exact_historical_span_receipt':'historical-span-preservation.json','qualified_scope_inputs':'historical-qualified-scopes.json / historical-qualification-projections.json / fifth-closure-boundary-projection.json','regression':'Preserve original R1 WP scope; R2 exact B05 A021/A022/A026, B06 A033, B07 A026, B08 A053 owner qualifications; R3 dynamic image/optional/no-required boundaries; GR4-M04-001 (17/76 versus B5 16/75); selected R5 GR5-M01-006 and GR5-M04-002 plus untouched shared catalogue controls. Old verdicts not reused as new behavioral PASS. Actual old rows and specified unaffected clause spans byte-preserved; finite current source/formal consumption rechecked.','fifth_activation':'Only 92 original qualified items selected by13fddb...+044c348... and unique activation12df95.../0378dc...; 7optional/7no-required/6policy/13limits and old FAIL/MISMATCH/LF correction remain historical. No state registration written.','full_host_UI_Demo_real_save':'NOT_EXECUTED'},'independent_adjudication':{'original_proposer':'R6-K','original_nonproposer':'R6-O','original_root':'R6-I','current_author':'R6-U01-A','candidate_non_author_ultra_review':'PENDING_PARENT_ASSIGNMENT_AFTER_PUBLICATION','author_can_self_sign_independent_PASS':False,'formal_acceptance':'NOT_GRANTED','CLOSED':'NOT_REGISTERED','metadata':'Requested gpt-6.1-sol/xhigh/default/default; effective model/effort/tier/speed/platform UUID UNVERIFIED; no CLI/model probing/subagents.'},'dependencies_and_receivers':{'primary_batch':'R6-U01','author_blocking_interbatch_edges':[],'only_actual_integrator':'thread01a13a93-d1da-71e4-a488-63b8524f503d / R6-I','shared_receivers':'shared-context.json exact U01 conflict edges and nine path receivers','candidate_changed_paths':[str(M/x) for x in changed],'integration_requires':'Apply only seven changed-file deltas; WP21/WP27 retained baseline are read contexts, not replacement winners. Resolve WP18/U10/U14, WP62/U09/U11, test catalog/U14 with all counterpart candidates; no last-writer overwrite.','closure_gate':c['closure_gate'],'future_policy':'Document facts now; malformed-input/egg-Dex compatibility is independent, not an added mandatory revision.'}})
(E/'author-findings.json').write_text(json.dumps({'batch':'R6-U01','requested_author':'R6-U01-A','state':'AUTHOR_COMPLETE_STATIC_CANDIDATE_READY','records':records,'specification_blockers':[],'remaining_review_and_execution_limits':['Independent ultra reviewer not assigned by this author; parent will assign after publication','Effective runtime configuration / own platformUUID UNVERIFIED','Ruby unavailable; no new reference execution, host/UI/Demo/model/save execution'],'evidence_levels':['SOURCE_STATIC','DERIVED_VECTOR','TOOL_VALIDATION'],'new_reference_execution':0},ensure_ascii=False,indent=2)+'\n')
# Group actual reading receipts; no retroactive UTC for pre-instrumentation reads.
commands=[json.loads(x) for x in (E/'commands.jsonl').read_text().splitlines()];groups={}
for x in commands:
 if 'input' not in x:continue
 k=x['input'];g=groups.setdefault(k,{'path':k,'identity':x['input_identity'],'total_lines':x['total_lines'],'ranges':[]});g['ranges'].append(x['range'])
for g in groups.values():
 covered=set();[covered.update(range(lo,hi+1)) for lo,hi in g['ranges']];g['full_file_semantic_read']=len(covered)==g['total_lines'];g['scope']='own actual output reading; not file-byte hashing alone'
(E/'reading-ledger.json').write_text(json.dumps({'instrumented_reads':list(groups.values()),'pre_instrumentation':json.loads((E/'execution-snapshot.json').read_text())['full_prompt_read'],'contract_identity':ident((P/'contracts/R6-U01.json').read_bytes()),'prompt_identity':ident((P/'prompts/R6-U01-A.md').read_bytes()),'prompt_fence_closing_and_embedding':'Complete prompt1–4325 semantically read; embedded contract1–2888 byte-identical at prompt161–3048, common3051–4325 full; fence reads158–164/3046–3055. Early oversized truncation not credited;119–161 repaired.','AGENTS':'Root AGENTS.md full original tool output read before checkout; applicable nested AGENTS none at prepare; no old snapshot AGENTS applies.','candidate_read_scope':'Full fixed baseline plus complete new exact replacements and repaired full changed-doc diffs; not claiming a second full reread of unchanged candidate text.','original_runtime_read_credit':'Historical reading/execution remains attributed; no inherited own read credit.'},ensure_ascii=False,indent=2)+'\n')
report='''# R6-U01-A 作者候选交接

状态：AUTHOR_COMPLETE_STATIC_CANDIDATE_READY，等待父线程指定非作者 ultra 复审。没有正式接受或 CLOSED 登记。

固定准备提交 `469a268b92daed7b4d28d7fd0da75520cbb7228f`；正式基线 `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`；参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。作者分支 `codex/remediation-sixth-r6-u01-author-20261014`。实际根 `/workspace/pokemon-essentials-clean-room`；Mac 绝对根作等价只读映射，记录于 execution-snapshot.json。唯一正式整合者为 thread01a13a93-d1da-71e4-a488-63b8524f503d / R6-I。

请求 gpt-6.1-sol / xhigh / default tier / default speed；有效 model/effort/tier/speed/本人平台 UUID 均 UNVERIFIED。按委派直接作者工作，没有启动 Codex CLI 或额外代理证明配置。

| ID | 实际最小修订 | 新静态验收 |
| --- | --- | --- |
| GR6-K-001 / P3 | WP10 转换行拆开浏览位置复制保留与其它三项清旧；补旧上下文单对象重复／整链版本条件 | MG17–19：3→2且旧2保留；5→2；单对象上下文不推进；正常整链成功后不重选v20 |
| GR6-K-002 / P2 | WP18 §6.1保留校验存在／正常类型，补同值构造例外；§9收窄拒绝；保留setter | CI29–31：两碰撞整数名接受、合法文本接受、非碰撞／只碰前id拒绝，setter0拒绝且原名保持 |
| GR6-K-003 / P2 | WP34 §5.2／§9.4／N0缓存消费者、WP62产蛋边界及跨目录引用 | BR27–31：Shellos0蛋5120仍提交；seen/forms/首次last与缓存填充、owned/seen-egg不写；缺对象、旧last、N0、故障前缀及首合格永石对照 |

实际改动四份规格和三份测试目录，共7份镜像。WP27 的 registered 字段迁移以及 WP21 的同值提交合同本来正确，两份镜像保持固定 main 原字节；整合者只接收7份差量，不能把这两份 baseline 覆盖其它候选。全部9份指定正式文档新全文读取；11份脚本单元新全文读取；两个PBS仅具名完整Shellos记录／形态记录及有限字段检索，不冒称PBS全文。完整作者prompt／JSON合同、原始逐ID提案、三份独立反证及裁决已新读；reading-ledger.json保留具体范围。

逐ID七组完整作者内容在 author-findings.json。每组展开身份／裁决、源—消费者—正式双向证据、合法前提与反例／正常／失败前缀、实际最小修订、静态验收及历史回归、独立复审状态、接收者／关闭门。候选逐文件 bytes/SHA256/blob 见 candidate-payload-identities.json；13个源载荷 commit/tree/mode/type/bytes/SHA256/blob 见 source-payload-identities.json。源由只读固定对象验证，无checkout变更。

有限工具检查：validation.json 的115项通过，包含原正式保护、准备镜像确为baseline、26次精确替换回放、7改2保、所有既有目录行和指定历史clause原字节、链接文件、13个源身份、Shellos数据与局部负检索。它们是 TOOL_VALIDATION。新增11行目录向量是 SOURCE_STATIC/DERIVED_VECTOR 支持的设计，全部 NOT_EXECUTED，不把115次工具断言合成115次参考运行或行为模型。

安全／失败记录：Ruby版本检查在子进程创建前因找不到ruby失败，未加载R；早期包装未独立捕获UTC，如实保留 failed-runtime-availability.json。随后GitHub REST元数据请求收到代理403，失败stderr与exit1在commands.jsonl；正常Git固定对象fetch成功到独立/tmp裸对象库，后继验证解析真实R commit/tree及13项mode/blob，不覆写失败。没有安装、认证／安全配置更改、原源执行、Marshal/eval、真实存档、host/UI/Demo、独立完整模型或生产服务执行。

历史回归保留精确资格，不转签旧PASS：R1原WP；R2 B05 A021/A022/A026、B06 A033、B07 A026、B08 A053；R3动态图像与M09 optional／M02 no-required限定；GR4-M04-001及17/76与B5 16/75分层；第五所选候选13fddb…+审查044c348…的唯一92条activation。旧G03/G09 FAIL、U03旧FAIL及定向修复、两MISMATCH、SC-U07-001体内LF纠正均不改写。historical-qualified-scopes.json是精确资格字段新读，未继承归档R5 joins的语义阅读；historical-span-preservation.json与完整旧目录行比对是本次差集回归。没有重审全部历史或全仓700MB。

共享接收：WP18与U10/U14；WP62与U09/U11；两共享目录与U14。WP27保留原字节，仍向唯一写者说明U12/U14接点。独立候选准备无跨批作者阻塞；候选非作者PASS、唯一整合、整合后共享全文非作者PASS、接口／历史验收、正式接受、CLOSED分别待登记。作者没有自签独立通过。

没有未解决的本批事实修订阻塞。剩余为父线程非作者ultra审、正式整合后的接合复验，以及运行／配置元数据限制。源缺陷事实不选择未来畸形输入或蛋图鉴兼容政策。正式目录、公共ledger/task-register、其它候选及main/tag保持受保护。

发布身份由后继 publication-binding.json / 最终响应绑定实际core C与发布P；不要求本文件包含自身未知commit。
'''
(E/'author-report.md').write_text(report)
print(json.dumps({'records':len(records),'state':'AUTHOR_COMPLETE_STATIC_CANDIDATE_READY','tool_checks':len(checks['checks']),'new_design_rows':11,'execution':0,'evidence':str(E/'author-findings.json')},ensure_ascii=False))
