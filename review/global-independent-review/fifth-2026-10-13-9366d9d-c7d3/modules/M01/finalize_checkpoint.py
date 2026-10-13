import review_state as s
from pathlib import Path
import re,json,datetime
C1='Data/Scripts/021_Compiler/001_Compiler.rb';C2='Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb';C3='Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb';GD='Data/Scripts/010_Data/001_GameData.rb';L='Data/Scripts/001_Technical/003_Intl_Messages.rb';P='Data/Scripts/010_Data/002_PBS data/';H='Data/Scripts/010_Data/001_Hardcoded data/';TC='deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md';LTC='deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md'
wp30='deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md';wp19='deliverables/final-specification-set/pokemon-rules/wp19-attributes-ability-and-stats.md'
for p,n,sem in [
(H+'001_GrowthRate.rb',188,[dict(lines=[1,73],entry_or_rule='max level, default construction, localized name, min/max exp, capped addition and inverse lookup',comparison='WP30 §3.1 matches return-error-object for invalid level vs name-resolution failure for invalid exp; cap-before-table and first-greater inverse explicit. Whole-domain caller/test reverse mapping pending.'),dict(lines=[75,188],entry_or_rule='all 6 registrations, 606 table cells including sentinels and all 6 outside-table formulas',comparison='All source rows read; table lengths and formula branches compared to WP30 §3.2. No claim independently recomputed all600 positive-level values; current spec earlier arithmetic result not reused as review proof. Per-cell calculation still not_reviewed.')]),
(H+'002_GenderRatio.rb',83,[dict(lines=[1,36],entry_or_rule='schema/default, localization and single-gender predicate',comparison='nil female chance alone determines single_gendered, not textual name. WP19 §3.2 and real Pokemon consumer checked.'),dict(lines=[40,83],entry_or_rule='8 registrations',comparison='Three fixed sex identities and five thresholds32/64/128/192/224 match WP19; source comment random wording is refined by actual consumer PID-low-byte. Supported_static data+consumer boundary, all wrappers read.')]),
(H+'003_EggGroup.rb',101,[dict(lines=[1,101],entry_or_rule='registration/default/localization and all 15 ordered identities',comparison='Undiscovered,Monster,Water1,Bug,Flying,Field,Fairy,Grass,Humanlike,Water3,Mineral,Amorphous,Water2,Ditto,Dragon all read; inheritance/daycare domain consumers not yet reverse-reviewed. Responsibility row alone not support.')])]:
 s.covered(p,[[1,n]],sem)
 d=s.read('reading-coverage.json');e=next(x for x in d['sources'] if x['path']==p);e['reading_extent']='full';e['review_extent']='partial';e['unreviewed_semantic_obligations']=['Per-record/registration downstream domain contract and test mapping incomplete'];s.write('reading-coverage.json',d)
for p,rr,sem in [
('Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb',[[1346,1422]],'PBS full/single export handler menu all22 entries/cancel and success feedback analyzed; rename only caller boundary.'),
('Data/Scripts/013_Items/004_Item_Phone.rb',[[435,505]],'Contact version/start-version/default selection; random localized strings, period overrides, rematch state1→2, request/remind fallback, body1+2 75% choice, optional end; full telephone consumer spec not yet read.'),
('Data/Scripts/014_Pokemon/001_Pokemon.rb',[[333,388]],'Gender actual consumer: single-gender mapping else PIDlow8<threshold; lazy cache; setters only nil/0/1 and ignored for single sex, all helpers read.')]:s.covered(p,rr,[dict(lines=rr[0],entry_or_rule=sem,comparison='Source-local semantics recorded; only stated data-interface projection verified, remainder of dependency file unread.')])
s.covered(wp30,[[1,130]],[dict(lines=[1,130],entry_or_rule='Purpose/concepts/growth §3 and experience/EV §4',comparison='Growth contract reverse-read vs GrowthRate. Combat paragraphs read but combat source not reviewed; not counted supported.')],'specifications')
s.covered(wp19,[[28,64]],[dict(lines=[28,64],entry_or_rule='types/gender/shiny and ability section opening',comparison='Gender thresholds and actual derivation match; shiny/other source dependencies not fully reviewed.')],'specifications')
s.covered('deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md',[[1,40]],[dict(lines=[1,40],entry_or_rule='scope and compiler sequencing',comparison='WP08 author localization expressly delegated. Later rg/output ranges were truncated and are not credited as fully read.')],'specifications')
# Explicit per-vector mappings for all read primary catalog rows, not an automated support inference.
def a(p,x,y):return dict(path=p,version=s.R,lines=[x,y])
settings=a('Data/Scripts/001_Settings.rb',1,524);battle=a('Data/Scripts/002_BattleSettings.rb',1,140)
vec={
'KC01':('supported',[settings,battle]),'KC02':('partial',[a('Data/Scripts/002_BattleSettings.rb',74,82)]),'KC03':('partial',[a('Data/Scripts/001_Settings.rb',107,124)]),'KC04':('partial',[a(C1,967,1018),a(C2,951,1063)]),'KC05':('supported',[a('Data/Scripts/003_Game processing/001_StartGame.rb',19,35),a('Data/Scripts/016_UI/013_UI_Load.rb',298,342)]),'KC06':('supported',[a('Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb',1423,1455),a('Data/Scripts/016_UI/013_UI_Load.rb',334,342)])}
kr={1:('supported',[a(P+'013_Encounter.rb',20,35)]),2:('supported',[a(P+'013_Encounter.rb',38,60)]),3:('not_reviewed',[a(GD,109,115)]),4:('supported',[a(P+'016_Metadata.rb',55,57),a(P+'017_PlayerMetadata.rb',45,49)]),5:('supported',[a(P+'010_SpeciesMetrics.rb',32,56)]),6:('supported',[a(P+'015_Trainer.rb',56,84),a(P+'021_PhoneMessage.rb',36,69),a(C2,1243,1255)]),7:('supported',[a(GD,83,85),a(C2,54,60)]),8:('supported',[a(C2,791,929)]),9:('supported',[a(C1,390,403)]),10:('supported',[a(P+'006_Item.rb',25,44),a(C1,438,483)]),11:('supported',[a(C1,1039,1116)]),12:('supported',[a(P+'011_ShadowPokemon.rb',27,30)]),13:('not_reviewed',[]),14:('supported',[a(C2,1237,1269),a(P+'021_PhoneMessage.rb',36,47),a('Data/Scripts/013_Items/004_Item_Phone.rb',447,459)]),15:('supported',[a(C2,54,60),a(C2,1243,1255),a(P+'021_PhoneMessage.rb',36,47)]),16:('supported',[a(C2,4,68)])}
for i,val in kr.items():vec[f'KR{i:02}']=val
for i in range(1,37):
 st='supported';aa=[]
 if i==1:aa=[a('Data/Scripts/999_Main/999_Main.rb',25,35)]
 elif i in [2,3,4,5,19,20,21]:aa=[a(C1,1039,1116)]
 elif i==6:aa=[a(C1,690,737)]
 elif i in [7,8,9,10]:aa=[a(C1,255,293),a(P+'006_Item.rb',167,177)]
 elif i in [11,12,13,14,15,16]:aa=[a(C1,95,145),a(C1,438,483),a(C2,4,68)]
 elif i==17:aa=[a(C1,921,1018)]
 elif i==18:aa=[a(C3,4,65),a(C3,105,132),a('Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb',1347,1409)]
 elif i==22:st='partial';aa=[a(C2,658,765),a(C3,403,442)]
 elif i in [23,24,25,26]:aa=[a(P+'010_SpeciesMetrics.rb',32,69),a(C3,291,351)];st='partial' if i in [23,24,25] else 'supported'
 elif i in [27,28]:st='partial';aa=[a(P+'008_Species.rb',391,453)]
 elif i==29:aa=[a(P+'008_Species.rb',391,453),a(C3,174,223)]
 elif i in [30,31,32]:aa=[a(C2,658,765)]
 elif i in [33,34,35]:aa=[a(C1,72,85),a(C1,95,145),a(C1,690,842),a(P+'008_Species.rb',52,111)]
 else:aa=kr[14][1]+kr[15][1]+kr[16][1]
 vec[f'KL{i:02}']=(st,aa)
for i in range(1,36):
 aa=[]
 if i<=3:aa=[a(L,589,632)]
 elif i==4 or i>=31:aa=[a(L,774,823)]
 elif i in [5,6]:aa=[a(L,350,372)]
 elif i in [7,8,9,10,11,17,26,27,28,29,30]:aa=[a(L,376,472),a(C1,155,182)]
 elif i==12:aa=[a(L,244,281),a('Data/Scripts/001_Technical/002_Files/001_FileTests.rb',1,50)]
 elif i in [13,14]:aa=[a('Data/Scripts/016_UI/013_UI_Load.rb',298,342)]
 elif i in [15,16]:aa=[a('Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb',1423,1455),a(L,244,348)]
 elif 18<=i<=22:aa=[a(L,214,240),a(L,350,472),a(C1,155,182)]
 else:aa=[a(L,244,348)]
 vec[f'LZ{i:02}']=('supported',aa)
cla=[]
for path in [TC,LTC]:
 for no,line in enumerate((s.ROOT/path).read_text().splitlines(),1):
  m=re.match(r'\| ((?:KC|KR|KL|LZ)\d+) \|',line)
  if not m:continue
  id=m[1];st,aa=vec[id];cla.append(dict(path=path,version=s.B,clause='vector '+id,lines=[no,no],status=st,source_anchors=aa,evidence_level='static_semantic_comparison' if st!='not_reviewed' else 'not_reviewed',supported_boundary='supported_static for expressly stated valid input/preconditions; no execution or UI/host guarantee' if st=='supported' else None,pending='Complete source/consumer prerequisite indicated in adjacent capability and coverage entries' if st!='supported' else 'Historical execution is not evidence for this review'))
s.append('spec-to-source.json','clauses',cla)
# Overall status must never treat full local source reading as completed semantic/domain review.
c=s.read('reading-coverage.json')
for e in c['sources']:
 if e.get('read_ranges')==[[1,e['line_count']]]:
  e['reading_extent']='full'
  if e['path'] in [C1,C2,C3,GD,L]:
   e['review_extent']='partial'
   e['unreviewed_semantic_obligations']=['All consumer/spec supplement/record contexts not yet closed; see per-range supported/partial/unresolved mapping. Full local source read is not end-to-end review completion.']
for e in c['specifications']:
 e['reading_extent']='full' if not e['unreviewed_ranges'] else 'partial'
 e['review_extent']='partial'
 e['unreviewed_semantic_obligations']=['Source evidence comparison is bounded; every field/consumer table projection and effective supplement must be closed before full status.']
s.write('reading-coverage.json',c)
inspection=s.read('message-data-inspection.json');total=sum(x['records'] for x in inspection['text_files'])
s.append('source-to-spec.json','capabilities',[dict(capability_id='M01-TEXT-CORPUS-DATA-INTEGRITY',status='partial',evidence_level='data_inspection_only',source_anchors=[a('Data/messages_core.dat',0,0)],spec_anchors=[dict(path='deliverables/final-specification-set/generic-kernel/wp08-localization.md',clause='§11 binary/corpus uncertainty')],comparison=f'Whitelist decoder consumed963270 bytes; all18 text files have {total} decoded key/value records identical to corresponding binary hash domains, with no extra/missing values under the decoder. Core EVENT_TEXTS contains no nonempty map buckets. This is content consistency only, not a compiler runtime test or full record semantics review.',record_ledgers='text-records-*.json',not_reviewed='All per-record real consumer mappings, interpolation argument compatibility and corpus semantics remain open.')])
s.append('shared-interfaces.json','interfaces',[dict(capability_id='M01-CONFIG-CONSUMER-HANDOFF',owner='M01/WP02 declaration baseline',contract='118 setting constants +3 callable content settings +3 engine metadata read against B5 formal dictionary; all effects must be verified at actual consumers.',consumer_projections=[dict(consumer='WP24',keys=['RIVAL_NAMES'],source='Data/Scripts/010_Data/002_PBS data/015_Trainer.rb:115–122',status='partial',fact='Only string-valued variable changes trainer name; first matching configured type wins.'),dict(consumer='WP43',keys=['MOVE_CATEGORY_PER_MOVE'],source='Data/Scripts/010_Data/002_PBS data/005_Move.rb:79–97',status='partial',fact='Physical/special checks first reject power0; switch then chooses move/category vs type. Damaging/status helpers use category independent of switch.'),dict(consumer='WP30',keys=['MAXIMUM_LEVEL'],source=H+'001_GrowthRate.rb:23–70',status='partial',fact='Cap before table/formula and used by compiler before normal game data; full numeric table verification still open.'),dict(consumer='WP08/WP09/UI load',keys=['LANGUAGES'],status='supported',supported_boundary='supported_static on already-read startup/load/debug paths; not all UI text projections')],not_reviewed='All remaining keys and all direct MECHANICS_GENERATION branch consumers; no completion inferred from default table.'),dict(capability_id='M01-GENDER-RATIO',owner='M01 fixed-data identity',contract='Eight identities, three no-female-chance fixed-sex records and five thresholds32/64/128/192/224.',consumer_projections=[dict(consumer='WP19 §3.2',source='Data/Scripts/014_Pokemon/001_Pokemon.rb:341–382',status='supported',supported_boundary='supported_static: PIDlow8 comparison and cache/setter gates; no generation or battle execution')])])
next_range=H+'004_BodyShape.rb:1–116, then 005_BodyColor.rb:1–78 and 006_Habitat.rb:1–76; continue fixed registries in source order'
s.progress(next_range,'Bounded checkpoint incomplete: primary compiler/localization source and all21 PBS-data files locally analyzed; all four formal primary specs read; every83 primary KC/KR/KL/LZ catalog row mapped individually with explicit partial/not_reviewed exceptions. Remaining full domain/source/data/counterevidence work listed.')
p=s.read('progress.json');p.update(status='in_progress',complete=False,review_extent='partial',checkpoint_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),model_parameters_actual='UNVERIFIED',candidate_findings=2,required_findings_finalized=0,source_local_full_read_files=sum(x.get('reading_extent')=='full' for x in c['sources']),source_entries_total=len(c['sources']),primary_record_data_inspection={'text_files':18,'records':total,'semantic_extent':'inventory_only','binary_decode':'whitelist_data_only'},remaining_work=[
'14 unread fixed registries, starting BodyShape; GrowthRate600 positive-level cells independent mathematical comparison incomplete',
'All73 PBS source files: complete records/fields/generation variants and explicit facility/tool consumer paths unread',
'All18 English text files: per-record human semantic/consumer/argument review not complete despite binary consistency',
'All118 setting consumers,3 callable config consumers,3 metadata consumers and direct generation branches; only bounded projections inspected',
'Current WP02 original+appendix and analysis/inventory scripts/output, all effective supplementary links and global feature/inventory mapping',
'Cross-domain detailed clauses/tables/vectors for every schema key and fixed registry, full negative evidence for two candidates',
'Independent counterevidence and final sanitized review disposition (no self-finalized required revision)'])
s.write('progress.json',p)
(s.OUT/'report.md').write_text(f'''# GR5 M01 独立审查阶段报告

**状态：PARTIAL / IN_PROGRESS，complete=false。不是全量完成、PASS 或最终必修清单。**

固定规格 B5：`9366d9d17aaeac3b4414236468affa650fb3dd27`；正式子树 `d5a462b4c6f8b78c3264a25d6b5495230fa265e2`。固定参考 R：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。身份沿用父会话已核事实；来源逐路径实际blob/SHA256已登记。

请求模型 `gpt-6-astra / ultra / service_tier=default`，禁Fast；实际参数回显 **UNVERIFIED**。未调查参数、额度、认证、私有会话或后端，未替换模型、开子agent、安装工具或改配置。

## 已完成的有限实质范围

- 本地化主源823行：收集/提取/导入/默认层/当前语言层/键/回退/插值全部函数与分支已作源内分析；正式WP08及现行原稿全文、LZ01–35逐行反查。
- 编译器001/002/003：1117/1321/821行全文源内分析，逐段记录通用和专用入口、预处理/解析、重复、终检、输出/省略、副作用与失败；正式WP03/WP04及现行原稿全文读完。
- GameData283行和002_PBS data全21文件：全部schema、构造默认、查找例外、PBS getter、资源/领域函数源内分析已登记。**消费者领域全文未闭合，review_extent仍为partial**。
- 主设置524行、战斗设置140行与正式WP02 278行全文比较声明值/派生门；少数真实消费者已核，不能将配置词典当逐键行为完成。
- 固定注册GrowthRate/GenderRatio/EggGroup全文已读并作源内分析；GrowthRate六表全部源行已读，但没有借用历史算术PASS或声称本轮已独立重算600值。
- KC/KR/KL/LZ合计{len(cla)}条主责目录向量已逐行建立源映射；尚未读齐前置来源的条目明确partial/not_reviewed。章节映射不完整处未计支持。

## 候选发现

| ID | 候选主题 | 当前处置 |
| --- | --- | --- |
| GR5-M01-001 | 活跃浮点字段实际接受/拒绝边界 | P2暂定；unresolved；待全领域当前合同反证及独立反证 |
| GR5-M01-002 | 默认消息差量生成及导出条目集合 | P2暂定；unresolved；待有效补充全文反证及独立反证 |

两条均为 `candidate_pending_independent_counterevidence`，**最终必修裁决0**。详细事实、最小反例、正常/失败对照、实际负证据范围、影响与静态验收在findings.json。不重报当前已覆盖的R4边界；GR3-M09-001暂缓、GR3-M02-003 NO_REQUIRED未重开。

## 全量数据只读辅助的实际边界

白名单基础类型解析完整消费 `Data/messages_core.dat` 的963270字节，拒绝对象/类/自定义加载钩子，未调用Ruby或Marshal.load。18文本共{total}条解码键值与对应二进制域逐记录一致；没有额外/缺失/差异记录。18份逐记录账本保留行号与散列，不复制整份原始语料。

此为 **DATA_INSPECTION_ONLY**：没有运行参考、编译器、模型或行为向量，也没有证明文本消费者、占位参数与全量语义兼容。18文本及dat保留inventory_only；安全解析不冒充语义审核。核心消息事件域没有非空地图桶，只是该二进制实际结构，不推广为game消息或真实Demo证据。

## 尚未完成与下一范围

- 73份PBS的全部记录字段、世代差异、设施/工具消费者仍未语义审查。
- 14份其余固定注册文件未读；配置逐键和直接世代分支消费者未闭合。
- WP02现行原稿/附表、analysis/inventory有效材料，以及所有领域当前补充合同仍须跟读；不能凭旧PASS或附表有名称判支持。
- 18文本每条记录的实际消费者语义/插值参数、全部反向章节/条款/表/向量映射及两候选反证未完。

**下一实际源范围**：`{next_range}`。

目录内七份必需产物与progress.md均已建立。reading-coverage.json区分实际读行、源内语义、未读区间和未闭合语义义务；source-to-spec.json区分supported_static的有限规则、partial/unresolved；shared-interfaces.json以唯一能力身份登记消费者投影。未写正式规格、reference、历史证据或共享报告；未提交、推送或启动update。
''')
with (s.OUT/'progress.md').open('a') as f:f.write(f'\n## 检查点 4（仍未完成）\n\n两条候选均 unresolved，等待独立反证，最终必修0。三个固定注册全文源内分析及GenderRatio真实消费已补登记；主责{len(cla)}向量逐行建立源映射，未审前置条目标partial/not_reviewed。\n\n下一实际范围：{next_range}。全部73 PBS与18文本消费者语义、其余14固定注册、配置逐键规则/直接世代分支、有效补充和全部反证仍待办。报告complete=false，不宣称全量完成。\n')
# Integrity checks on review artifacts only; do not execute reference or behavior models.
for f in s.OUT.glob('*.json'):
 d=json.loads(f.read_text());assert d['schema_version']=='gr5.review.v1',f
required={'id','title','module','severity','disposition','status','reviewer','category','source_baseline','specification_baseline','source_anchors','spec_anchors','expected_reference_behavior','current_spec_behavior','gap','preconditions','minimal_counterexample','normal_case','failure_or_boundary_case','impact_on_independent_implementation','negative_evidence_search','proposed_spec_change','affected_files','shared_contracts','acceptance_criteria','dependencies','related_capabilities','related_findings','root_cause_group','priority','batch_owner','history_links','evidence_level','execution_status','confidence','unknowns','excluded_claims','user_decision_needed','review_resolution'}
for x in s.read('findings.json')['findings']:
 assert required<=x.keys(),required-x.keys();assert x['disposition']=='unresolved';assert x['status']=='candidate_pending_independent_counterevidence'
print(json.dumps({'schema_valid':True,'candidate_fields_complete':True,'semantic_review_complete':False,'local_source_full_read':p['source_local_full_read_files'],'source_entries':p['source_entries_total'],'mapped_catalog_vectors':len(cla),'decoded_text_records':total,'next':next_range},ensure_ascii=False))
