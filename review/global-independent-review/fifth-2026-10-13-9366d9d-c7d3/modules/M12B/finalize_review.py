from pathlib import Path
import json,re,hashlib,datetime
P=Path(__file__).parent
RV='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';BV='9366d9d17aaeac3b4414236468affa650fb3dd27';FT='d5a462b4c6f8b78c3264a25d6b5495230fa265e2'
base=dict(schema_version='gr5.review.v1',module='M12',reviewer='M12B',source_baseline=RV,specification_baseline=BV,formal_tree=FT)
def save(p,x):(P/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
shared=[]
def sh(id,owner,providers,consumers,rule,state='supported',exceptions=[]):
 shared.append(dict(shared_capability_id=id,primary_contract_owner=owner,source_provider_paths=providers,consumer_projections=consumers,behavioral_contract=rule,state=state,supported_boundary='supported_static within the named direct source slices/current contracts; source representation is not a future API requirement.',exceptions=exceptions,unique_count_policy='One shared identity, any number of consumer projections; do not count provider and consumers as separate copies of this capability.',evidence_level='SOURCE_STATIC/SPEC_STATIC',execution_status='NOT_EXECUTED'))
sh('shared.ui.number-and-text-cancellation','WP17; WP73-A property consumers',['007_Objects and windows/011_Messages.rb','020_Debug/002_Editor_DataTypes.rb'],[
 {'consumer':'WP72 sleep/daycare/foreign ID','projection':'No dedicated cancel means clamped default returned and caller may still write.'},
 {'consumer':'WP73-A nullable numbers and pocket','projection':'Nullable -1→empty differs from pocket old0 BACK0 and confirmed first row→1.'},
 {'consumer':'WP76 generation questions','projection':'Initial cursor and BACK choice are distinct parameters.'}],
 'Default/clamping, explicit cancel, USE return and text ESC old-value semantics are one input service, with caller-specific state consequences. Accepted B21 CASE-DISPATCH used as data, not execution.')
sh('shared.content.registration-and-persistence','WP03/WP04; consumer contracts WP73-A/B/WP76',['010_Data/001_GameData.rb','021_Compiler/003_Compiler_WritePBS.rb','021_Compiler/002_Compiler_CompilePBS.rb'],[
 {'consumer':'WP73-A type/item/species/metadata','projection':'Immediate registration→archive→PBS; aliases/default projections may change values before/after archive.'},
 {'consumer':'WP73-A trainer editor','projection':'Outer No reload does not undo nested type PBS writes.'},
 {'consumer':'WP73-B encounters/metrics','projection':'Registered values, file output path and current runtime layout/snapshot are different stages.'},
 {'consumer':'WP76 trainer lists','projection':'Archive precedes interleaved total/sub-PBS writes; partial failures survive.'}],
 'One phased contract, no implicit atomicity or runtime broadcast. Defaults belong to specific constructors/properties; source equality is not assumed.', 'partial',['GR5-M12-101','GR5-M12-102','B21 CHAIN-6','B19-C004/C005/C016/C022'])
sh('shared.creature.form-submission-and-pokedex','WP18 §3.4/WP21 §4/WP62 §3',['014_Pokemon/001_Pokemon.rb','015_Trainers and player/005_Player_Pokedex.rb','011_Battle/002_Battler/001_Battle_Battler.rb'],[
 {'consumer':'WP72 nonbattle form editor','projection':'Ordinary form setter registers even when the following explicit call has setup/egg gate.'},
 {'consumer':'WP72 battle form editor','projection':'No battler→simple write only; battler sync→ordinary write-through submission.'},
 {'consumer':'WP77 Giratina map example','projection':'Dynamic read must pass forced/battle/storage guards before possible ordinary commit.'}],
 'Ordinary versus simplified submission are distinct; no generic no-registration promise for debug. Register sets seen/form/initial last, not owned/seen_egg.','partial',['GR5-M12-103'])
sh('shared.battle.persistent-write-through','WP39/WP42 plus WP72 debug projection',['011_Battle/002_Battler/001_Battle_Battler.rb','011_Battle/002_Battler/002_Battler_Initialize.rb','011_Battle/001_Battle/009_Battle_CommandPhase.rb'],[
 {'consumer':'WP72 battle individual','projection':'HP/status/item/level/form write original; stats/stages/types/effects are local; each field checked.'},
 {'consumer':'WP72 return from F9','projection':'Named weather/terrain/forms and scene refresh chain only.'},
 {'consumer':'WP76 real simulation','projection':'Player AI control reaches AI command selection; unused random scene helper is separate.'}],
 'Do not model every battler edit as temporary or every debug close as full resynchronization.')
sh('shared.animation.collection-cache-identity','WP74 with WP04 clear-data projection',['010_Data/002_PBS data/001_MiscPBSData.rb','011_Battle/007_Other battle code/007_BattleAnimationPlayer.rb'],[
 {'consumer':'editor','projection':'Valid cache reused; nil/empty-first entrance may create uncached temporary collection.'},
 {'consumer':'organizer','projection':'Requires first valid entry; deletion can save zero entries; No does not roll back cached edits.'},
 {'consumer':'bulk import/export and combat','projection':'Null versus empty object gates differ; clearing affects future retrieval, not old aliases.'}],
 'File persistence, cached object and editor canvas references are distinct observable identities.')
sh('shared.animation.cel-and-timing-consumption','WP67-A combat playback / WP74 authoring projection',['011_Battle/007_Other battle code/007_BattleAnimationPlayer.rb','011_Battle/004_Scene/004_Scene_PlayAnimations.rb'],[
 {'consumer':'WP74 canvas','projection':'25properties, conventional0–59 rendering, stored60 edited but not rendered; invisible0 stays hidden.'},
 {'consumer':'WP74 preview','projection':'20fps visited frames, focal transform and placeholder cry silence; timing shared old-state captures.'},
 {'consumer':'WP74 compiled association','projection':'Side mapping and Common exact name lookup use their own whitespace rules.'}],
 'Authoring does not invent a separate combat implementation; only required inputs/outputs and current data compatibility described.')
sh('shared.resource.safe-copy-identity','WP73-A utility / WP74 exchange',['020_Debug/001_Editor_Utilities.rb','001_Technical/002_Files/001_FileTests.rb'],[
 {'consumer':'bulk export','projection':'Source and output usually provide two locations.'},
 {'consumer':'bulk import','projection':'Resolved comparison and local write destination passed separately; usual current-directory resolution is same path.'}],
 'Existence/content comparison and prompt can concern a different path from eventual write; third-destination variant is a narrow compatibility detail.','partial',['GR5-M12-104 optional'])
sh('shared.facility.rules-copy-and-validation','WP54 rules / WP76 generation',['018_Alternate battle modes/002_Battle Frontier rules/001_Challenge_ChallengeRules.rb','018_Alternate battle modes/002_Battle Frontier rules/002_Challenge_Rulesets.rb'],[
 {'consumer':'candidate/team/simulation','projection':'Uses rule copy with team size2, including copy minimum/reset semantics.'},
 {'consumer':'final tiers/trainer allocation','projection':'Returns to original rules; current chosen members must satisfy relevant gates.'}],
 'Suggested level/number, individual/team/subset checks and clear-individual-rule copy are different projections; no global two-member invariant.')
sh('shared.facility.template-ev-versus-training','WP19/WP54 template and WP28 training; WP76 projection',['018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb','013_Items/001_Item_Utilities.rb','014_Pokemon/001_Pokemon.rb'],[
 {'consumer':'facility template creation','projection':'Split510 by all emphasis entries, repeat writes do not add; no252 clamp in stats.'},
 {'consumer':'normal EV training','projection':'Incremental headroom clamps per-stat and total; does not redefine template creation.'}],
 'B17 PA040 two255/duplicate170/training252 cases are one shared distinction. Historical static fixtures are not new executions.')
sh('shared.engine.wait-and-route-requests','WP13 command/move matrices; WP16 tone clock',['021_Compiler/004_Compiler_MapsAndEvents.rb'],[
 {'consumer':'WP75 generated door/transfer','projection':'Concrete direction/audio/wait/tone recipe must supply numbers; generic command support does not supply them.'},
 {'consumer':'follower door helpers','projection':'Asynchronous wrapped route plus explicit event210; no independent total-duration guarantee.'}],
 'Route/event wait units1/20s and tone request duration are separate from update opportunities and actual visual completion.','partial',['M12-OBS-003 confirmed parameter gap'])
sh('shared.demo.evidence-levels','WP01/WP77',['PBS/metadata.txt','PBS/map_metadata.txt','PBS/map_connections.txt','PBS/town_map.txt','PBS/dungeon_parameters.txt','PBS/encounters.txt','PBS/trainers.txt','PBS/phone.txt','PBS/battle_facility_lists.txt'],[
 {'consumer':'WP77 config tables','projection':'All assigned root data rows independently read and cross-reference values checked.'},
 {'consumer':'WP72–76 tools','projection':'Static entry definition does not establish runnable Demo interaction.'},
 {'consumer':'future verification','projection':'12 missing event chains; media/system/map evidence needed for real reachability.'}],
 'Configuration facts, static consumer capability, actual event chain and runtime observation remain different evidence levels.','unresolved',['Missing demo maps/system/media; parent owns full media inventory'])
sh('shared.startup.external-loader-diagnostics','WP75/root with WP05/WP07/WP09 projections',['Data/Scripts.rxdata decoded Main1–49'],[
 {'consumer':'external script discovery','projection':'Files before subdirectories, hidden-directory exclusion but hidden.rb inclusion, suffix case-insensitive.'},
 {'consumer':'failure handling','projection':'Pre-eval file read outside local rescue; ScriptError replacement and ordinary900-message log branch.'}],
 'This loader is not the plugin manager or later main critical-code wrapper; newly readable static behavior needs root-owned contract.','partial',['M12-OBS-001'])
save('shared-interfaces.json',{**base,'interfaces':shared,'policy':'Source paths are traceability only. No new framework/API/class design. Cross-module ownership references preserve one shared capability identity and concrete consumer projections.'})
# Resolve provisional work log into the new canonical candidate list; retain file as readable navigation.
save('working-observations.json',{**base,'state':'superseded_by_structured_findings','canonical_findings_file':'findings.json','candidate_ids':['GR5-M12-101','GR5-M12-102','GR5-M12-103','GR5-M12-104'],'note':'No pending source-reading work remains in assigned available scope; candidates still need independent counterevidence before final required signoff.'})
rc=json.loads((P/'reading-coverage.json').read_text());ss=json.loads((P/'source-to-spec.json').read_text());rev=json.loads((P/'spec-to-source.json').read_text());ff=json.loads((P/'findings.json').read_text());ce=json.loads((P/'counterevidence.json').read_text())
primary=[r for r in rc['records'] if r.get('assigned_role')=='primary']
# Only artifact integrity is checked; do not run any behavioral/model test.
errors=[]
if len(primary)!=23:errors.append('Expected23 independently assigned primary scripts')
for r in primary:
 if r['review_extent']!='full' or r['unreviewed_ranges']:errors.append('Primary incomplete '+r['path'])
 for g in r['semantic_ranges']:
  if not g.get('capability_ids'):errors.append('Missing primary semantic mapping '+r['path'])
ids=[r['id'] for r in ff['findings']]
if len(ids)!=len(set(ids)) or ids!=['GR5-M12-101','GR5-M12-102','GR5-M12-103','GR5-M12-104']:errors.append('Finding identities')
required=['id','title','module','severity','disposition','status','reviewer','category','source_baseline','specification_baseline','source_anchors','spec_anchors','expected_reference_behavior','current_spec_behavior','gap','preconditions','minimal_counterexample','normal_case','failure_or_boundary_case','impact_on_independent_implementation','negative_evidence_search','proposed_spec_change','affected_files','shared_contracts','acceptance_criteria','dependencies','related_capabilities','related_findings','root_cause_group','priority','batch_owner','history_links','evidence_level','execution_status','confidence','unknowns','excluded_claims','user_decision_needed','review_resolution']
for f in ff['findings']:
 for key in required:
  if key not in f:errors.append(f['id']+' missing '+key)
 if f['status']!='candidate_pending_independent_counterevidence' or f['review_resolution']['final_required_signoff']:errors.append('Improper self-final finding')
if len(ce['observations'])!=7:errors.append('Root observations count')
if len([u for u in rev['clause_and_table_units'] if u['kind']=='effect_parameter'])!=120:errors.append('Effect row mapping count')
anchors={a['anchor_id'] for a in rev['source_anchor_catalog']}
for group in ['sections','clause_and_table_units','vectors']:
 for u in rev[group]:
  if any(a not in anchors for a in u['source_anchor_ids']):errors.append('Unresolved reverse anchor')
# Compare vector identities/occurrences with actual fully-read catalog; this verifies serialization, not source behavior.
test=Path('deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md')
actual=[]
for ln,l in enumerate(test.read_text().splitlines(),1):
 if l.startswith('| '):
  t=l.split('|')[1].strip()
  if re.match(r'(?:DG|CE|WE|AN|CV|GN|DM)-[A-Z]\d+|B\d\d-',t):actual.append((t,ln))
encoded=[(v['id'],v['lines'][0]) for v in rev['vectors']]
if actual!=encoded:errors.append('Vector catalog serialization mismatch')
# Verify source/formal anchor line domains. Decoded Main uses its own49-line coordinates.
for f in ff['findings']:
 for a in f['source_anchors']:
  q=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')/a['path']
  n=len(q.read_text().splitlines())
  if any(lo<1 or hi>n or lo>hi for lo,hi in a['lines']):errors.append('Source anchor bounds '+a['path'])
 for a in f['spec_anchors']:
  n=len(Path(a['path']).read_text().splitlines())
  if any(lo<1 or hi>n or lo>hi for lo,hi in a['lines']):errors.append('Spec anchor bounds '+a['path'])
for p in P.glob('*.json'):
 try:d=json.loads(p.read_text())
 except Exception as e:errors.append('JSON parse '+p.name+':'+str(e));continue
 if d.get('schema_version')!='gr5.review.v1':errors.append('Schema '+p.name)
qa={**base,'kind':'artifact_integrity_only','checks':{'json_parse_and_schema':True,'primary_body_records':len(primary),'primary_lines':sum(r['total_lines'] for r in primary),'primary_semantic_groups':sum(len(r['semantic_ranges']) for r in primary),'behavioral_capability_identities':len(ss['capabilities']),'reverse_sections':len(rev['sections']),'reverse_clause_table_units':len(rev['clause_and_table_units']),'effect_rows_exact_mapped':120,'test_vector_occurrences_exact_mapped':len(encoded),'root_observations':len(ce['observations']),'candidate_ids_unique':True,'finding_required_fields':True,'anchor_bounds_checked':True},'errors':errors,'result':'PASS' if not errors else 'FAIL','not_behavioral_validation':'These checks validate artifact references and structure only; no Ruby, host UI, reference functions, independent behavioral model or scenario execution.'}
save('artifact-validation.json',qa)
if errors:raise SystemExit('\n'.join(errors))
summary={**base,'complete':True,'status':'assigned_available_static_scope_complete_candidates_pending_independent_review','model_request':{'model':'gpt-6-astra','reasoning_effort':'ultra','service_tier':'default','fast':False,'actual_echo':'UNVERIFIED'},'execution_status':'STATIC_ONLY_NO_REFERENCE_OR_MODEL_EXECUTION','last_completed_range':'All23 primary source bodies (16,151 lines), six assigned formal main contracts plus root WP75 counterevidence context, complete current Demo/DX catalog, originals/applicable supplements, necessary callers/data, bidirectional mappings, seven root counterevidence decisions and artifact QA','next_range':'Root independently counterchecks GR5-M12-101–104 and merges own observations; no available assigned source body remains for M12B','not_reviewed_assigned_available':[],'outside_assigned_or_unavailable':[{'scope':'root tools/media/full converter beyond independent slices','status':'root_owned_not_independently_full_reviewed','identity':'../M12/reading-coverage.json'},{'scope':'backup encounter datasets','status':'inventory_only; WP77 full data review explicitly root current table'},{'scope':'missing demo map/system/media and runtime host','status':'unresolved_missing_material; all available relevant text reviewed'}],'candidate_counts':ff['counts'],'counterevidence_counts':ce['decision_counts'],'artifact_validation':'artifact-validation.json','complete_does_not_mean':'No final required disposition, no global M12 pass, no runnable-demo or host-runtime verification.'}
save('progress.json',summary)
report=f'''# M12B 独立静态审查报告

本次分配的可得静态范围已完成，`complete=true`。结论是 **3 条拟必修 P2、1 条可选 P3，均待父审独立反证**；没有自行签署最终必修或宣告全局 M12 PASS。

- 固定规格 B5：`{BV}`；正式子树 `{FT}`。
- 固定参考 R：`{RV}`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。
- 模型请求：`gpt-6-astra / ultra / service_tier=default / Fast=false`；实际回显 **UNVERIFIED**。没有替换、配置或认证调查。
- 仅写本 `modules/M12B` 目录；没有修改正式规格、参考、历史证据或父审报告，没有提交/推送/更新/安装，也没有执行参考程序或行为模型。

## 已审范围与方法

独立逐段审完剩余 **19 份 Debug 脚本＋4 份设施生成器，共 16,151 行**。{qa['checks']['primary_semantic_groups']} 个语义区段记录入口、分支、默认值、参数表、失败和调用交界；这些分段不是功能数量。6 份主责正式稿（WP72、WP73-A/B、WP74、WP76、WP77）及 WP75 反证上下文均读完，当前 Demo/DX 测试目录 **215 个向量出现位置**逐项映射，含全部 **120 个效果条款**。映射数量只验证产物完整性，不作为语义审查证明。

必要调用链已补核：注册/构造/反写、输入取消、菜单入口、形态/图鉴、战斗写穿、动画容器与播放器/位图/控件、地图连接/遭遇快照、设施模板/规则/评级、电话/地图旗标/平衡等级。WP77 的9份根目录数据正文逐条核对，类型、具体招式、形态和进化条件使用具名补证切片。每个依赖仅按实际行范围记录；没有把定点阅读冒充该依赖全模块审完。

全部7份对应原稿与适用覆盖附表已比较；完全相同段落复用已独立读过的正式正文，每个不同原稿段实际阅读。未发现独有且正确的行为事实在迁移中另有实质遗失。原稿的历史状态、源标识、过时 EV/进化/计数说法与现行合同分开处理，详见 [原稿对照](original-comparison.json)。B21 CASE-DISPATCH/CHAIN-6、B17 PA040 和 B20 六族18夹具按精确 archive commit 读取，未把历史 PASS 或旧执行当本轮证据。

父审负责的根工具、媒体及转换器完整范围仅复用其实际已读身份；M12B 对七条观察只在直接重读的源码/正文范围签反证。副本遭遇表只记存在性，缺失地图/系统/媒体无法提供事件链与真实宿主结果。这些是范围/材料界限，不是尚未读取的主责内容。

## 新候选

| ID | 提议 | 具体差异 |
| --- | --- | --- |
| GR5-M12-101 | P2 / required 候选 | 新建类型保存名称为 Unnamed；新建道具保存单/复数名为 Unnamed、描述为 ???。输入仍用于ID与成功消息；已有项编辑是正常对照。 |
| GR5-M12-102 | P2 / required 候选 | 既有道具原样确认可把 BP1 保存为0，并把未指定份量名称写成???。No、非默认BP和明确份量文本须分列。 |
| GR5-M12-103 | P2 / required 候选 | 外层准备/蛋门未阻止普通形态提交的图鉴登记；战斗有在场对象的同步也会进入该提交，无在场简化写不同。只登记见过相关字段，不据此写拥有/见过蛋。 |
| GR5-M12-104 | P3 / optional 候选 | 安全复制的比较资源和最终写入位置可不同；当前单一“目标”表述可澄清。默认同路径行为不扩大为缺陷。 |

各条的前提、最小反例、正常/边界对照、完整反向检索、影响、静态验收与排除主张见 [findings.json](findings.json)。最终状态全部是 `candidate_pending_independent_counterevidence`，最终必修数仍为0。

## 对父审观察的独立反证

| 父审观察 | 结果 | 有界理由 |
| --- | --- | --- |
| M12-OBS-001 | 确认，限静态装载合同 | 实际 Main 压缩成员已安全解码读完49行；排序、隐藏目录/文件区别、异常与900消息门未被现行内核/工具合同覆盖。 |
| M12-OBS-002 | 确认，限定字面行边界 | 六旧调用模式按行锚定，合法调用行前后独立行可被丢弃；不冒充六族已执行。 |
| M12-OBS-003 | 确认，限定配方参数 | 具体门/独立转移资源、方向、等待与色调时长缺失；通用命令与跟随合同不能补数值。 |
| M12-OBS-004 | 确认，限定两个布尔族 | DoubleBattle/Continue 的重复注释只会置真，后续假不清；不是通用最后值覆盖。 |
| M12-OBS-005 | 排除必修 | 具体当前文本/向量限定 TrainerBattle；revisit 标签不等于所有野外分支插退出。 |
| M12-OBS-006 | 收窄为可选 | 全串每处替换的事实成立，但正文未明确承诺仅首次，通常向量无重复字面。 |
| M12-OBS-007 | 排除必修 | 当前地图/公共事件的具体管线已足够区分通用35替换阶段。 |

直接证据与排除过程见 [counterevidence.json](counterevidence.json)。父审保有原观察身份及最终合并责任。

## 交付与剩余边界

- [reading-coverage.json](reading-coverage.json)：精确版本、实际行区段、材料状态及未审的非主责区间。
- [source-to-spec.json](source-to-spec.json)：40个行为能力身份及共享消费者，`supported` 均限 `supported_static`。
- [spec-to-source.json](spec-to-source.json)：逐节/条款/表/向量反向映射及可解析源码锚点目录。
- [shared-interfaces.json](shared-interfaces.json)：12个共享合同身份与消费投影，不重复计数。
- [artifact-validation.json](artifact-validation.json)：JSON、ID、锚点、参数表/向量序列检查通过；这是产物检查，非行为测试。
- [progress.json](progress.json)：`complete=true` 及明确排除/材料界限。

随机名称的格式/音节数据已读；当前合同只给性别选择、重试、大小写及长度界限，精确默认造词词汇仍是可选内容兼容政策边界，未据此立必修。其余缺宿主、素材、地图事件和实际执行的未知保持。未重开 `GR3-M09-001` 暂缓项或 `GR3-M02-003 NO_REQUIRED`。
'''
(P/'report.md').write_text(report)
with (P/'progress.md').open('a') as f:
 f.write('\n## Completed assigned available static scope\n23/23 primary source bodies (16,151 lines) and required current text/tests/originals/supplements closed. 3 P2 required candidates + 1 optional P3; all pending independent counterevidence. Root observations:4 confirm/narrow-confirm,2 no-required,1 optional. Full bidirectional mappings, shared contracts and artifact checks written. complete=true describes reviewer work, not final required approval or global M12 pass. No reference/model executions.\n')
print(json.dumps({'complete':True,'artifact_integrity':'PASS','primary_scripts':len(primary),'vectors':len(encoded),'candidates':ff['counts'],'root_decisions':ce['decision_counts']},ensure_ascii=False))
