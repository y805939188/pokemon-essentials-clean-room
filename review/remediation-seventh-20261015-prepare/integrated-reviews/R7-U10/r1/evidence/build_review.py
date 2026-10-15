"""Assemble the current review evidence; no reference behavior execution."""
from pathlib import Path
import os,json,hashlib,datetime,shutil,re,subprocess
R=Path('/workspace/r7-ir-R7-U10-wave3');REPO=R/'result-checkout';PREFIX='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U10/r1';O=REPO/PREFIX;E=O/'evidence'
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def git(*a):return subprocess.check_output(['git','-C',str(REPO),*a],stderr=subprocess.PIPE)
MI='e54f54a2cb32e546eabd46aaf53ed45b30a8af89';FI='b98fa82f8a08b5630ac568cbe8c34f607f623cfb';B='e646432c644dec04d306842cc5a559a29c718fbc'
UTC=datetime.datetime.now(datetime.timezone.utc).isoformat();thread=os.environ.get('CODEX_THREAD_ID');session=os.environ.get('CODEX_SESSION_ID')
j=json.loads((R/'actual-input/integration/applied-clauses.json').read_text());audit=json.loads((E/'byte-audit.json').read_text());checks=json.loads((E/'supplemental-checks.json').read_text())
# Preserve actual receipts and only audit tools that were read/executed here.
for name in ['original','actual-input']:
 for p in (R/name).glob('recovery-receipt-*.json'):shutil.copyfile(p,E/(name+'-'+p.name))
for name in ['audit_actual.py','final_checks.py','inspect_cil_read_and_rebased.py','restore_container_context.py','supplement-recovery.json']:
 shutil.copyfile(R/'bootstrap'/name,E/name)
shutil.copyfile(R/'bootstrap/integrated-input.json',E/'fixed-FI-integrated-input.json')
# Restore the old r1 artifacts for provenance only, without reusing their verdict.
old=json.loads((R/'actual-input/candidate-review/candidates/R7-U10/evidence/reviewer/r2/old-r1-reception.json').read_text())
old_results=[]
from urllib.request import urlopen
for x in old['files']:
 b=urlopen(x['url'],timeout=40).read();a=ident(b);assert all(a[k]==x[k] for k in a)
 p=R/'supplement/old-r1'/Path(x['path']).name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
 old_results.append({'url':x['url'],**a,'content_verdict_reused':False})
# Receipts describe what was actually read; complete byte acquisition is not full semantic reading.
open_gates=[
 {'id':'G-FULL-CURRENT-TEXT','state':'UNSATISFIED_REVIEW_OBLIGATION','reason':'完整MI正文/相关目录及18个具名目标和条件消费者未全部完成逐段内容审读；当前完成的是具名条款、源消费者及完整字节核验。材料可读，不能标作L01-L14或材料缺失。'},
 {'id':'G-SHARED-SEMANTICS','state':'UNSATISFIED_REVIEW_OBLIGATION','reason':'audit、matrix、DX目录的完整当前共享正文及所有贡献对应原独立批准尚未全部完成语义复核。完整文件恢复/72条日志重放不替代此门。'},
 {'id':'G-DOMAIN-HISTORY','state':'UNSATISFIED_REVIEW_OBLIGATION','reason':'先前8份已接受文件逐字保留已核；与本批领域相交处的完整语义回归、全部历史责任及接收证据尚未闭环。AN002/AN007、L06/L07等已读局部不授全部历史完成。'}]
base_deps={'direct_record_scheduling_edges':[],'transitive_record_scheduling_edges':[],'empty_edge_qualification':'原记录未分配具名record-to-record排程边；不是无领域依赖。','integration_receiver':'R7-I','shared_writer':'R7-I','post_review_gates':['R7-I实际接收与语义/共享贡献登记','精确领域依赖与历史责任接收','正式ACCEPTED与最后CLOSED分别登记'],'main_write_authority':False}
wp73='deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md';wp74='deliverables/final-specification-set/demo-dx/wp74-battle-animation-authoring-and-exchange.md';cat='deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md'
paths=[wp73,wp74,cat,'audit/source-traceability.md','planning/feature-matrix.md']
file_ids=[]
for p in paths:
 a=(R/'actual-input/actual'/p).read_bytes();b=(R/'actual-input/baseline'/p).read_bytes();c=(R/'actual-input/candidate/candidates/R7-U10'/p).read_bytes()
 file_ids.append({'path':p,'MI':ident(a),'B':ident(b),'approved_candidate_commit':'583330fb69935ff6b2eb32ca11ede6c23bde5ecd','approved_candidate':ident(c),'actual_equals_own_candidate_whole_file':a==c})
clause_rows=[x for x in audit['journal_hunks'] if x['batch_id']=='R7-U10']
assert len(clause_rows)==13 and all(all(x['checks'].values()) for x in clause_rows)
def vector(key,premise,expected,reason,source,clause):return {'id':key,'premise':premise,'expected_static':expected,'independent_reason':reason,'source_locator':source,'actual_clause':clause,'content_check':'SUPPORTED_IN_INSPECTED_SCOPE_ONLY','evidence_class':['SOURCE_STATIC','DERIVED_VECTOR'],'execution':'NOT_EXECUTED','gate_credit':False}
s1='R:Data/Scripts/020_Debug/001_Editor screens/004_EditorScreens_SpritePositioning.rb L91-136,L157-222,L282-308,L389-411; Species_files L156-169; SpeciesMetrics L71-87; IconSprite L175-207'
m15=[
 vector('C01-M15-BACK','合法物种/形态无自有阴影；通用1/2不同可加载、3首缺；正常窗口/输入/动画，无插件外改；旧尺寸1、绑定1、确认假；浏览2后BACK、不重选或重开','登记1、绑定2、确认假；主菜单可刷新位置，无本次文件写入','浏览显式选择资源；BACK仅恢复尺寸，主菜单与指标应用只重定位，普通位图更新不按尺寸选资源。',s1,'WP73 §7.3/7.5; WE-M17'),
 vector('C01-M15-NO-BROWSE','同一完整前提，进入1后不浏览直接BACK','登记1/绑定1/确认假','未发生新资源绑定；恢复旧值不新增确认。',s1,'WP73 §7.3; WE-M17'),
 vector('C01-M15-REOPEN','BACK主例之后，明确重开尺寸页且重载正常','重新按登记1绑定资源1','入口在显示尺寸列表前显式重选物种资源。',s1,'WP73 §7.3; WE-M17'),
 vector('C01-M15-USE','独立复位、旧1、浏览2后USE','登记2/绑定2/确认真，不前进','确认按与入口旧值的差异设标记；返回值未要求轮转。',s1,'WP73 §7.3; WE-M17'),
 vector('C01-M15-ACTION','独立复位、旧1、浏览2后ACTION','登记2/绑定2/确认真并前进到下一编辑项','同一差异设标记，ACTION返回轮转信号；不是切换物种。',s1,'WP73 §7.1/7.3; WE-M17'),
 vector('C01-M15-PREEXISTING','完整主例前提，但先前另有已确认改动、标记真','尺寸回1、绑定2、标记仍真','BACK没有清标记赋值；不能取消先前已确认改动。',s1,'WP73 §7.3; WE-M17'),
 vector('C01-M15-POSITION','背面/正面/阴影横移正常坐标编辑后BACK','坐标恢复且位置预览刷新','坐标取消分支显式刷新；不从尺寸绑定问题推出无任何刷新。',s1,'WP73 §7.2/7.5; WE-M17'),
 vector('M15-SAVE-GATE','无先前确认/同值确认/已改值确认；分别正常退出No或Yes，另档案先成功PBS后失败','无确认正常退出重载档案；改值有保存询问，Yes先档案再PBS；后失败无总回滚','资源身份与登记/确认/保存层分开；不由视觉残留推出持久化损坏。',s1+'; WP73 §7.5','WP73 §7.1/7.3/7.5; WE-M17/20'),
 vector('M15-RESOURCE-EXCEPTION','资源、输入或宿主失败，或出现物种自有阴影/首缺资源','前两类不保证正常返回/异常回滚/最终重画；自有阴影拒绝；首缺即停','反例的正常依赖前提不涵盖异常；候选保留旧守卫。',s1,'WP73 §7.3; WE-M17')]
s2='R:BattleAnimationPlayer.rb L334-390; AnimEditor_Functions.rb L91-183,L994-1001; SpriteWindow_text.rb L753-976,L1044-1248; Editor_Listers.rb L4-11; AnimEditor_SceneElements.rb L409-427'
m152=[]
for oldidx in [0,1]:
 m152.append(vector('M15-002-OLD-'+str(oldidx),'合法A0/A1/A2、正常画布/资源/控件，无外改或同步导航；原selected='+str(oldidx)+'，Resize3→2且尚未方向导航；Load/Rename/Delete各独立复位','Load/Rename取有效原成员；Delete只替换对应槽，长度2、另一槽不变','缩容只有旧selected≥新长度才写新长度；窗口赋值和无输入刷新不另钳。',s2,'AN-M09; WP74 §7.1'))
for action,exp,reason in [
 ('LOAD','可先绑定空动画并释放旧位图，再读图形属性失败；不保证无痕','赋画布对象与释放旧位图先于未保护的空属性读取。'),
 ('RENAME','空动画名读取失败；具体宿主报错和恢复未知','重命名入口先读取动画名字，空值无局部保护。'),
 ('DELETE-YES','槽2尾添新动画，长度3、旧0/1保持，无空洞','选中号恰等于长度；尾添不同于大于长度写入。'),
 ('DELETE-NO','长度仍2，不替换或追加','写入在确认Yes之后，No跳过。')]:
 m152.append(vector('M15-002-SELECTED2-'+action,'完整合法前提，原selected=2；Resize3→2，索引仍2且不导航，各动作独立样本',exp,reason,s2,'AN-M09; WP74 §7.1'))
m152+= [vector('M15-002-NAVIGATE','原2、缩3→2，先正常方向导航到有效位置再操作','按有效成员正常处理','窗口方向更新按项目数回绕；不同于无输入赋索引。',s2,'AN-M09; WP74 §7.1'),vector('M15-002-LIST-BACK-SAVE','Resize已截尾后列表BACK；外层Save与Exit选择分别指定','内存截尾保持；写盘须外层Save；正常退出的缓存失效仍独立','列表取消没有恢复集合副本，外层保存/退出是不同门。',s2,'AN-M09; WP74 §3.2/16')]
s3='R:animmaker.exe SHA256 bbbcd909bcd2310078def29f4889f6203e0bc1c8f6500d216440774f832cd96b; all15 method bodies/EH [592,2664), token0e/0f/09/0b'
reasons=[
 '总pattern数的零分支仍给一行；保存只有已到达请求资格。',
 '总数6使用两行；序号5按商余式进入第二行首格。',
 '槽0加(96−56,96−68)，尺寸倍增；源裁剪坐标没有加到目标槽原点。',
 '缺路径跳转仍经过索引递增；总数在循环前已读取，缺图不压缩槽或减画布。',
 '读取x并判空在其它数值转换之前；该支直接建立整图标记。',
 '外层逐动画枚举且无全局撤销；四finally只表示释放请求。',
 '零参数帮助支等待后直返；有参数只读数组0号。',
 '存在性检查与读取器构造的具名I/O异常门分开；不外推其它异常。',
 '四属性依次转换，负值比较小于0；正常依赖下请求退出1。',
 '局部检查非负，零通过；空矩形/零面积库行为仍未执行。',
 '数值辅助的局部EH只捕获指定FormatException。',
 '缺值交库转换，不据同名数值帮助函数承诺相同异常类别。',
 '局部EH没有溢出类型，不能把它并为格式错误统一退出。',
 'XML异常处理请求的格式占位超出所传参数；不能推出诊断成功或部分集合正常返回。',
 '新加载图像的alpha判断决定直接沿用或副本+左上颜色透明请求；缓存另有命中支。',
 '数值支只有非负门，未见96上限检查；文档建议不等于执行验证门。',
 '存在性通过后进入实际加载调用；其失败没有走缺路径跳过分支。']
lines=(R/'actual-input/actual'/cat).read_text().splitlines()
m17=[]
for line in lines:
 if not line.startswith('| TOOL-AN-'):continue
 cells=[c.strip() for c in line.split('|')[1:-1]];idx=int(cells[0].rsplit('-',1)[1]);m17.append(vector(cells[0],cells[1]+'；共同前提：完整合法XML、预期元素和先前依赖正常，除本例具名改变之处。',cells[2],reasons[idx-1],s3,'WP74 §18; DX目录'+cells[0]))
assert len(m17)==17
records=[]
for rid,vs,target,non_author,preserve,domain,history in [
 ('GR7-M15-001',m15,[wp73,cat],'C01 challenges/1: p02-8de3976333a24ccb24be；原M15较宽“无刷新”被反证，P3窄资源身份合同控制。',['首缺停止','自有阴影拒绝','登记/确认恢复','USE/ACTION轮转','保存与重载','普通战斗已有布局不广播刷新','不强制未来保留副作用'],['阴影选择/绑定/逐帧更新与指标应用','U01指标默认/克隆/后缀条件同步','WP73-B与WE-M17共享receiver'],['原C01六项向量','WE-M17既有同值/改值/先前true及WE-M20保存失败']),
 ('GR7-M15-002',m152,[cat],'C08 challenges/2: p02-06fb1af35df48b7d0842；原selected0为反例，只修测试前提，不重写正确WP74条件。',['有效槽删除替换','恰等长尾添无洞','导航回绕','WP74 §7.1正确条件','外层Save/Exit','NOT_EXECUTED与宿主未知'],['集合resize→窗口索引→Load/Rename/Delete','画布加载已到达前缀','列表BACK/外层Save/cache','目录owner及root精确历史去重'],['R6-U07 scope_contracts/1 AN002对象/焦点观察与AN-M12','R6-U07 scope_contracts/6 AN007默认近似控制点，Float facet optional','WP74 §8.6/B20-D024 N5保留']),
 ('GR7-M17-001',m17,[wp74,cat,'audit/source-traceability.md','planning/feature-matrix.md'],'C06 challenges/1: p02-33da3f93fd6480f9a050；五列几何已存在，新增只为XML工具分支及保存阶段。',['既有五列192格几何','≤96是文档建议','零非负门','alpha/非alpha请求','历史identity-only资格','无真实PNG/像素承诺','.anm类型门/停用转换/关联缓存','旧specs/demo保持身份'],['图像输出→图样选择，非.anm自动桥','WP74 §11/14.3/15/16，WP75 §14及WP77工具/Demo界线','T-WP74邻T-WP75，F18-03邻F18-04','U11 EOF先旧组后U10 TOOL-AN17行'],['R6 final-delivery L06/L07','当前C17 L01-L14','旧WP74批准身份与AN/CV编号'])]:
 relevant=[c for c in clause_rows if c['path'] in target]
 records.append({'id':rid,'verdict':'WAIT','verdict_reason':'完整当前正文/共享语义及领域历史义务未完成，不能签PASS_SCOPED_ACTUAL_INTEGRATION。已核局部未发现足够具体的FAIL反例；这不构成完整无缺陷断言。','MI':MI,'FI':FI,'actual_file_identities':[x for x in file_ids if x['path'] in target],'actual_clause_bindings':relevant,'original_nonauthor_scope':non_author,'vectors':vs,'preserved_correct_scope':preserve,'dependencies':{**base_deps,'domain_and_reverse_consumers':domain,'historical_responsibilities':history},'unmet_gates':open_gates,'ACCEPTED':False,'CLOSED':False,'behavior':'NOT_EXECUTED'})
per={'schema':'r7.actual-integration-review.per-id.v1','batch':'R7-U10','review_round':'r1','reviewer_thread':thread,'reviewer_context':session,'MI':MI,'FI':FI,'records':records,'execution':'NOT_EXECUTED','no_other_required_or_global_certification':True}
dump(O/'per-id.json',per)
receipt={'schema':'r7.actual-integration-review.input-receipt.v1','utc':UTC,'actual_thread':thread,'actual_context':session,'identity_origin':'Exact CODEX_THREAD_ID/CODEX_SESSION_ID; observed in own shell, no /root/PID/model-request inference','environment_id':'ccarenv_b64_Y2NhcmVudl8wY2Y3ODY2ODc5MjQ4MTkxYjc1ZTAyNWMyMzNkY2Y2YQ','delegation_source_thread':'01a13f49-a154-7054-9b04-ce31f924d01c','auxiliary_agents_or_model_calls_created':0,'auth_or_quota_queries':0,'effective_configuration':{k:'UNVERIFIED' for k in ['model','effort','tier','speed']},'requested_configuration':'gpt-6.1-sol / ultra / default / ordinary speed; no Fast','dispatch':{'commit':'72c93538d6e6cc15cb0be15ccfc3b8268d4b0af7','path':'review/remediation-seventh-20261015-prepare/integration/wave3/v1/dispatch/R7-U10-R7IR.md','blob':'f195258f056a20381b5ef5c50ffa6f56f82a573c'},'MI':{'commit':MI,'tree':'b3b6b166b69d2e4dc513cd8d72950b47306191fd','formal_subtree':'e1dfe28acd4f559b22da505238ef3a899aed4542'},'FI':{'commit':FI,'tree':'eaf9f0831cea151c8a77ad716ad4c8fc5b71dc66','entry_identity':ident((R/'bootstrap/integrated-input.json').read_bytes()),'plan_identity':ident((R/'actual-plans/R7-U10.json').read_bytes())},'fixed_B':B,'fixed_B_formal_subtree':'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c','fixed_R':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','R_qualification':'Named bounded snapshots; reference whole-tree identity not independently reconstructed','original_restore':{'files':39,'bytes':6796155,'root':str(R/'original')},'actual_restore':{'files':292,'bytes':9638588,'root':str(R/'actual-input')},'specific_supplement':{'files':10,'bytes':454772,'receipt':'evidence/supplement-recovery.json'},'old_r1_restored':old_results,'old_r1_qualification':'Unwaived WAIT_INPUT_OR_INDEPENDENCE; content PASS not inherited','candidate':{'commit':'583330fb69935ff6b2eb32ca11ede6c23bde5ecd','tree':'7a81a11b22d771fe79f165a265fa108c4a85502c','freeze':'aa369555b0e8b6c8b077f964b54ed63d3b924f26','r2_commit':'d7337be83dae5aa7b848cd6a603c2aa7048ffa0c','r2_tree':'d91ef8094aa6730dd1590ef26e7d037aca06bba5','candidate_PASS_migrated_to_actual':False},'file_identities':file_ids,'formal_counts':audit['formal_counts'],'source_semantic_read_scope':['SpritePositioning.rb complete 1-411','Species_files.rb 150-175; SpeciesMetrics.rb 60-90','IconSprite 165-215; MessageConfig 485-515; Debug_MenuCommands 1220-1245','AnimEditor_Functions 1-185,988-1010,1106-1122','BattleAnimationPlayer 334-391; SceneElements 400-435,717-727','SpriteWindow_text 753-976,1044-1248; Editor_Listers 1-15','AnimEditor_ExportImport complete1-147; Compiler_CompilePBS1260-1321','animmaker.txt complete; all15 CIL methods and11EH through read static decoder'], 'current_text_semantic_read_scope':'Affected U10 clauses and stated neighbors, shared contribution texts, WP73 §7, WP74 §7.1 and §8.6/§11/14.3/15/16/18, WP75 §14, WP77 L154-230, R6 L06/L07, C17 L01-L14. Some large tool displays truncated; no claim that full current shared files were semantically read. See unmet gates.','unmet_review_obligations':open_gates,'new_reference_observation':0,'reference_program_execution':0,'independent_complete_behavior_model_execution':0,'host_Demo_native_media_real_save_replay':0,'all_behavior':'NOT_EXECUTED','L01_L14':'RETAINED individually; unread accessible text is not relabeled a limit','old56_92':'UNCHANGED','denominators':{'required_items':27,'batches':13},'nonmandatory_adoption':'NONE:7optional/2navigationfacet/1no-required/2policy untouched','logging_qualification':'Initial tool commands exist in platform record; no local wrapper PID/UTC/stdout/stderr triple was captured for every initial command. Do not backfill invented receipts. Restore receipts contain actual per-fetch UTC; byte audit and supplemental check contain their own actual tool PID. Tool PID is not model identity.','result_branch':'codex/r7-ir-u10-20261015-r1','base_of_result_branch':B,'write_set':PREFIX+'/**','ACCEPTED':False,'CLOSED':False}
dump(O/'review-input-receipt.json',receipt)
report='''# R7-U10 独立实际整合复审 r1：WAIT

GR7-M15-001、GR7-M15-002、GR7-M17-001 均为 **WAIT**。本次已完成冻结输入恢复、完整字节身份核验、U10累计条款重放及下列具名静态核对；没有完成合同要求的全部当前正文、共享文件和领域/历史语义复核，因此不签署 PASS_SCOPED_ACTUAL_INTEGRATION。未在已读局部找到足够具体的 FAIL 反例，不等于完整内容无缺陷。候选r2 PASS、旧r1内容PASS、恢复成功和字节保留均没有迁移为实际PASS。

实际审者thread/context：`THREAD`，来自本容器CODEX_THREAD_ID/CODEX_SESSION_ID，二者相同。与派发合同列出的作者、r2审者、旧r1、整合者及父线程ID不同；不以/root或工具PID证明独立。全程未创建子任务、agent、子会话或辅助模型调用，未查认证或额度。请求配置与有效配置分开；model/effort/tier/speed均无有效回参，UNVERIFIED。

## 固定输入和实际恢复

| 项 | commit / tree |
| --- | --- |
| 实际MI | e54f54a2cb32e546eabd46aaf53ed45b30a8af89 / b3b6b166b69d2e4dc513cd8d72950b47306191fd |
| 正式131文件子树 | e1dfe28acd4f559b22da505238ef3a899aed4542 |
| FI | b98fa82f8a08b5630ac568cbe8c34f607f623cfb / eaf9f0831cea151c8a77ad716ad4c8fc5b71dc66 |
| B / 正式子树 | e646432c644dec04d306842cc5a559a29c718fbc / ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c |
| R | 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b；具名有界文件快照，不授参考整树或运行资格 |
| 固定派发 | 72c93538d6e6cc15cb0be15ccfc3b8268d4b0af7:integration/wave3/v1/dispatch/R7-U10-R7IR.md（完整路径前缀review/remediation-seventh-20261015-prepare/） |

实际先读派发全文、AGENTS全文，再读658488c固定恢复工具、恢复说明及原批计划后运行。仓库没有适用的.agents/skills，/workspace/.agents为空；没有可用的项目本地技能。只做规格和分析，没有实现引擎、TypeScript包、适配器或转译参考结构。

恢复严格在本容器 `/workspace/r7-ir-R7-U10-wave3/`：original为39文件/6,796,155字节，actual-input为292文件/9,638,588字节。FI运输计划150,732字节，SHA256 `30d48062e857f514a15855d4f4299f60d54a8998f0a4dd6cc1ed65c9c9cd4b7e`。每成员bytes/SHA256/blob均匹配。没有假设共享目录，没有80MB Manifest或core全包扫描。具名补取C06原解码证据和历史绑定10份/454,772字节；旧r1四文件也按固定94cdbf56完整恢复校验，仅保留原流程WAIT。当前原合同18个具名原片段范围/大小/SHA均核验通过。

Git实际对象的MI/FI树与合同一致。FI131份正式文件逐一与真实Git blob完整字节核对，30份相对B改变、101份相同；前一MI已接受8份完整字节保持。完整文件身份与五份本批目标的B/候选/MI对照在review-input-receipt.json、evidence/byte-audit.json，不以这些机械结果替代语义复审。

## 累计条款及共享receiver

独立按B行区间取removed、按固定候选行区间取added、逐条核其bytes/SHA/blob，再与MI登记位置对照并重建文件。本批U10为13处，U07为3处；全累计72处中71处的原始严格文本检查通过。28文件中27份全量重放完全等于MI。U10的全部13处及相关共享文件重放均完全匹配。

唯一严格重放差异为U12的current-navigation-errata.json：status、reception/candidate_review、reception/shared_integration三处由候选时点更新为接收时点；其余JSON字段一致。当前MI与前一45c80832实际MI该文件逐字相同，属于既有接收状态，没有新U10行为差异。初始byte-audit的两个严格检查差异原样保留，supplemental-checks另列精确字段和前一MI字节证明；没有倒改为“72处全部严格逐字通过”。本审者不替U12或root豁免其记录责任。

| 当前共享文件 | 已核贡献保留及交界 |
| --- | --- |
| audit/source-traceability.md | U13、U10、U11、U12、U01、U02各锚点原样；T-WP74追加未改历史批准身份，邻T-WP75的extendtext条款并存。U01→U02两EOF追加顺序保持。root当前阶段注记单列，不赋本次接受/关闭。 |
| planning/feature-matrix.md | F18-03的U10静态请求/未知追加与F18-04的U11独立工具条款相邻保留；U13/U12及U01→U02追加原样，不增覆盖分母。 |
| DX测试目录 | WE-M17保旧行追加资源身份；AN-M09修前提。EOF先U11 EXT01–12，后U10 TOOL-AN01–17，互不覆盖；其它旧AN/CV行不由本次重写。 |

上述为实际条款及字节核对，不冒充完整当前共享正文和每份原独立批准的全部语义复核。完整批准结果已恢复，仍有本报告末尾的未满足义务。本次不扩大其它批次新语义PASS。U03r2未整合；其它wave2任务继续绑定它们原MI/FI。旧56/92、27项/13批和未采用7optional、2导航facet、1no-required、2policy保持。

## 三项内容核对

GR7-M15-001：独立读完整411行定位器及具名阴影选择、指标应用、位图绑定/更新、调试入口链。浏览时显式选择绑定，BACK只恢复尺寸；主菜单refresh和指标应用只重定位，普通位图update也不根据尺寸重新选资源。合法物种/形态无自有阴影、1/2不同可加载、3首缺、正常窗口/输入/动画，旧尺寸1/绑定1/确认假且不额外重载时，浏览2再BACK为登记1/绑定2/确认假。返回主菜单的位置可刷新，不能写成完全无刷新。不浏览仍1/1；重开尺寸页显式重载回1；USE确认2不前进、ACTION确认2并前进；原确认真在BACK后仍真。普通坐标编辑BACK确实恢复并刷新。首缺停止、自有阴影拒绝、同值确认、外层保存/重载与PBS失败前缀保留。没有据此认证像素、异常回滚、普通游戏损坏或要求未来永久保留预览副作用。定位为实际WP73-B §7.3新L140、§7.5 L165及目录WE-M17 L139；精确片段身份见per-id。

GR7-M15-002：独立读集合resize、列表重建、窗口索引/无输入更新/导航、Load/Rename/Delete、画布载入和外层Save。原selected0/1缩3→2保有效；原2不导航才保留索引2恰等新长度。独立Load可先绑定空对象并释放旧位图，再在空图形属性失败；Rename读空名失败。Delete Yes只在此恰等长条件尾添槽2，长3、原0/1不变且无洞；No仍长2。方向导航后可恢复有效成员；列表BACK不撤销截尾内存，磁盘仍受外层明确Save门。宿主错误文字/恢复未知。实际目录AN-M09 L168已给原2、尚未导航及原0/1独立普通对照，WP74 §7.1正确正文未因该ID重写。R6-U07 AN002是集合/画布对象焦点观察，AN007必修是默认0.3333/0.6666控制点，Float端点另属optional，均不替代当前游标前提；旧N5/B20-D024边界保持。全领域/历史责任尚未完成，不能从这些局部推出全历史闭环。

GR7-M17-001：全文读r2静态PE/CLR解码审计工具后只重定位输入路径，实际运行该静态读取工具；没有加载或执行animmaker/CIL。当前输入10,240字节、SHA256 `bbbcd909bcd2310078def29f4889f6203e0bc1c8f6500d216440774f832cd96b`；全部15方法体、11EH和跳转目标已解码核对，方法/头部/对齐/异常表各段在[592,2664)，不说连续2072字节全是指令。输出全文留本容器，本证据仅刊身份/方法范围/分支计数，不刊移植代码。

正常门是首参数存在完整合法XML、库提供预期元素且此前构造枚举正常，先解析输入集合再输出。缺XML与具名构造I/O异常分别为诊断/退出1请求；无参帮助等待ENTER后返回不是业务取消。x缺/空不消费y/width/height，x非空才依次转换并检查非负；负、零、FormatException、缺值和溢出分流。零不改成严格正数；≤96仍是文档建议。XML异常诊断占位不匹配，不能保证诊断成功、部分集合正常返回或到输出阶段。

全部pattern计画布：n0=960×192，n6=960×384；槽i原点(192(i mod5),192floor(i/5))，目标加(96−w,96−h)、尺寸2w×2h。56×68在槽0请求(40,28,112,136)，缺原0而原1有效时仍槽1、目标(232,28,112,136)，可到保存请求；不紧排，也不将存在路径后的加载失败当缺路径跳过。新加载alpha沿用、非alpha请求副本和左上色透明，均无像素/编码保证。A保存确已成功、B后失败才说A可保留，不能保证B/后项完成；finally仅释放请求，不保证清理或保存成功。17行TOOL-AN逐一记录前提、预期、独立理由和NOT_EXECUTED。

反向消费者定点核：图样选择取PNG名称/hue；单项.anm解码后仍须动画对象类型；编译RMXP转换块停用，命名关联与缓存门保持。WP75 §14明确animmaker归WP74，extendtext不借其输出规则；WP77仍区分作者工具入口和Demo事件可达，不能由图像请求推出动画元数据、自动导入桥或真实Demo通过。T-WP74、F18-03追加仍具时点，旧specs/demo仅保历史身份，条件同步不自动触发。

## 未满足门与证据资格

1. 完整MI正文/相关目录及全部18个具名目标、条件消费者尚未全部逐段内容审读。
2. audit、matrix、DX目录的完整当前共享正文及各贡献对应原独立批准尚未全部完成语义复核；已核字节与共享新增条款不足以签该门。
3. 8份已接受文件的完整领域交叉语义回归、所有具名历史责任及接收证据尚未闭环。字节未改只证明保留。

这些是本次尚未完成的审读义务，材料可读，不伪标材料缺失或L01–L14，不用作者自审/r2 PASS/旧报告代签。因此三个ID统一WAIT，实际内容PASS为0。R7-I仍须实际接收并登记语义、共享、精确依赖及历史责任后，才可能分别正式接受/关闭；本审者没有宣布ACCEPTED/CLOSED，也无main写权。

全部行为NOT_EXECUTED；新增参考观察、参考程序、独立完整行为模型、宿主、Demo、native媒体、真实存档回放均0。SOURCE_STATIC、DERIVED_VECTOR与TOOL_VALIDATION分列；L01–L14逐项原资格、H14局部历史执行和旧日志缺口不回填。初始shell工具I/O在平台记录，未为每条捕获本地独立PID/UTC/stdout/stderr，未补造；恢复回执有真实请求UTC，独立审计工具PID在证据中，与模型身份分开。部分大段显示被截断，不把文件落盘/散列或工具exit0冒充全文模型审读。

成果从固定B创建的隔离checkout，唯一分支`codex/r7-ir-u10-20261015-r1`。唯一仓库写集为本目录report.md、per-id.json、review-input-receipt.json、artifact-manifest.json及真实审计证据；没有携带/修改MI正文、候选镜像、公共台账、main或tag。普通commit/push和最终完整远端bytes/SHA256/blob回读在包外绑定commit/tree，避免自引用。
'''.replace('THREAD',thread or 'UNEXPOSED')
(O/'report.md').write_text(report)
# Actual assembly metadata, not a retroactive wrapper for earlier tool invocations.
dump(E/'review-build-execution.json',{'utc':UTC,'pid':os.getpid(),'script':str(R/'bootstrap/build_review.py'),'inputs':['evidence/byte-audit.json','evidence/supplemental-checks.json','fixed recovered snapshots'],'outputs':['report.md','per-id.json','review-input-receipt.json'],'all_behavior':'NOT_EXECUTED','notes':'This metadata records the current assembly process only; it does not backfill initial commands.'})
print(json.dumps({'written':str(O),'thread':thread,'records':[{'id':x['id'],'verdict':x['verdict'],'vectors':len(x['vectors'])} for x in records]},ensure_ascii=False))
