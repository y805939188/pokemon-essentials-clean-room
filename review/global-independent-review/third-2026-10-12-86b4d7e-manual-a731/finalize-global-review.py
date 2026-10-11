"""Integrates completed independent scopes; preserves disputes and historical evidence."""
from pathlib import Path
import json,csv,datetime,hashlib,collections
OUT=Path(__file__).resolve().parent
REPO=OUT.parents[2]
I=OUT/'integration-history-coverage/m09-integration-20261012-a731'
def read(p):return json.loads(p.read_text())
def dump(n,d):(OUT/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
findings=read(OUT/'findings.json');byid={x['id']:x for x in findings}
j=read(I/'junction-54-and-chains-8.json');reg=read(I/'regression-229-joins.json');acc=read(I/'accepted-341-joins.json')
assert len(j['records'])==62 and len(reg['records'])==229 and len(acc['records'])==341
new_chains=[
('N01 内容文本→导出/导入→消费',['GR3-M01-001','GR3-M01-002','GR3-M01-003','GR3-M01-004'],'空译/井号/端部空格与稀疏地图桶的准入和输出不同；默认电话第二节覆盖，联系人重复仍拒；先删除/截断可能已发生。'),
('N02 通知/步骤→持久状态',['GR3-M02-001'],'计步/前处理器写入后中处理器异常，后订阅者/遭遇不能保证到达；正常顺序保持，异常不能自动作为隔离继续。'),
('N03 持久注册→保存/读取/撤销',['GR3-M02-002'],'同ID双注册保两个回调；保存后项值覆盖，读取两次同终值，验证各自谓词，撤销同ID全部；有效默认17单元不变。'),
('N04 查询未驻留图→地牢随机/暂存',['GR3-M03-002'],'临时建立也发生成通知，清待播种子/重播全局随机、成功摆放写transfer暂存；驻留复用不重建。默认地图缺失不证明可达。'),
('N05 读档→进入清记录→条件恢复',['GR3-M03-004'],'两读档分支先清地图变更记录，正常恢复辅助可见空表；额外/直接剩余异图同事件ID穿透真写在地图门外，缺事件首次失败。'),
('N06 SPECIAL→过场A开关/结束/重启',['GR3-M03-003'],'严格Cut Scene注释与主解释器/事件门；空数组存在；先A再结束再启动，同轮快捷消费另按实际门，不宣称输入独占。'),
('N07 镜头→商店等UI等待',['GR3-M03-001'],'速度4一格0.2秒，0.1秒64子像素；203新滚动不等，脚本包装等完成；SnapEdges与小地图限制独立。'),
('N08 编号/形状→真实前背精灵',['GR3-M04-001'],'非蛋个体前背位图逐帧经过斑点回调；默认形状/位输入/2×2采样/通道夹限可审但合同未自足；species-only/图标不套。'),
('N09 个体字段→尺寸辅助',['GR3-M05-001'],'原始六IV低4位/PID两低byte与物种height生成毫米，纯查询无随机/状态写；当前仅定义无静态caller，不伪造钓鱼/Demo。'),
('N10 隐藏事件→探测转向/消息/统计',['GR3-M05-002'],'hiddenitem名称/自开关A、dx<8/dy<6、Manhattan和枚举平局，脚下4右转，无结果仍统计+1/effect真；不拾物。'),
('N11 经验变化→消息→写入/成长',['GR3-M06-001'],'同级+1/−1也先差量提示后写经验，增经验友好与下降无友好分开；同值只提示早退。'),
('N12 登记消费→失败退款→同轮终局',['GR3-M07-001'],'POTION2→登记0→首成功次无效退1且旧消费身份尚在→NORMAL终局再退2；下一命令先清与使用者倒下是反向结果1。'),
('N13 每击反应→消费→续击/AI',['GR3-M08-001'],'NaturalGift/PARENTALBOND，H160/h81 ORAN，目标JABO存活：反伤20/恢复10后71且空物，第二基底nil身份访问失败；H101/单击对照不同；AI当前ORAN资格不模拟此反应。'),
('N14 BoxLink嵌套→旧持物提交',['GR3-M10-001'],'A持POTION→Move缓存→盒中取回袋1清A→原目标B空确认，袋1/B持POTION/A空，总1→2；BACK保取回但不复制，无嵌套总1。'),
('N15 数量/文本输入→提交',['GR3-M10-002','GR3-M10-003'],'同轮USE+BACK共享0/商店1，RIGHT+USE共享即1/商店11留；战斗列表busy未暂停只resume，普通消息skipAhead，全显才选项。'),
('N16 Arena领域→UI/记录',['GR3-M10-004'],'首次对阵提示、正常补位不复位累计，count3/4/5连续判；WP56/PA-P28正确，WP67-A残留需修；旧B028不重开。'),
('N17 MapSize/遭遇→Area与地图查询',['GR3-M11-001'],'Area正宽3/10000只有基格、11111为5格而非6；可见Point并集不同于WP63首条/只长度游标；缺省/零宽与隐藏门独立。'),
('N18 工具资源/评级历史→输出与阈值',['GR3-M12-001','GR3-M12-002'],'两246bytes/8×8 BMP可得但底图缺；结算70+12=82，238+12=250，历史0增0；异常不承诺评级全字段原子恢复。')]
root_records=[]
for x in j['records']:
 y=dict(x);y['independent_helper_current_status']=x['current_status'];y['root_canonical_adjudication_pending_separate']=False
 y['root_decision']={'reviewer':'/root','independent_integration_reviewer':'/root/m09_ai_facilities_v3','state':'LIMITED_STATIC_RECONCILIATION_COMPLETED_WITH_EXPLICIT_GAPS_AND_LIMITS','basis':'Root阅读全部62项当前normal/failure边界投影与最终integration报告；各独立module实际source/spec范围＋精确限定历史证据，不要求root重复所有源或旧raw。','scope_rule':'相关新finding有些是同域/同carrier关联，不自动证明本接口自身新反例；原helper状态和链接保留，不以广泛关联改旧CLOSED。','runtime':'NOT_EXECUTED'}
 root_records.append(y)
dump('junction-results.json',{'kind':'ROOT_ADJUDICATED_FINITE_JUNCTION_REVIEW','existing_junctions':54,'existing_chains':8,'records':root_records,'new_chains':[{'name':n,'finding_ids':ids,'normal_failure_boundary':b,'reviewers':['/root']+sorted({str(byid[x]['reviewer']) for x in ids}),'status':'STATIC_REQUIRED_GAP_RETAINED','execution':'NOT_EXECUTED'} for n,ids,b in new_chains],'historical_reuse_exclusions':j['navigation_corrections'],'signature_transfer':False,'formal_update':False})
md=['# 第三轮交界实质裁决','', '实际裁决者为独立主会话 /root；独立 integration reviewer /root/m09_ai_facilities_v3。固定输入及精确身份见baseline、每项source/spec证据和完整junction-results.json。原54交界/8链逐项有限归并完成，相关新缺口与未知保留；不使用整体PASS，不重开旧229，不移转签名。所有场景静态未执行。','', '表中关联finding可以是同域/同carrier关系，不自动把一个同文件缺口扩到每个接口。原helper结论及完整前提仍保留在JSON。','', '| ID | 能力/交界 | 本轮正常 | 失败/边界与判定 | 关联新ID |','| --- | --- | --- | --- | --- |']
for x in root_records:
 md.append('| '+x['id']+' | '+x['theme']+' | '+x['normal'].replace('|','／')+' | '+x['failure_and_boundary'].replace('|','／')+'；限定静态归并，具体资源/宿主/未读范围保留。 | '+','.join(z['id'] for z in x['related_new_findings'])+' |')
md+=['','伙伴链的完整当前反例由M06直接源核：实际伙伴参战建立旧合并集合；满队接收将同一A送盒而玩家记录左移，终局一次恢复使盒A的X被写Y、留队B空；无伙伴共享集合删A则A保持X、B=Y。外层伙伴治疗无第二恢复循环。B013/CP20原受限范围不变，CP21/22及CX40–42当前证据可复用；素材/默认实际可达/运行仍未证。','','新增链如下，仍以各finding完整前提和接受标准为准：','']
for n,ids,b in new_chains:md+=['- '+n+'（'+','.join(ids)+'）：'+b]
md+=['','复用排除：A022 withMoves=false跳创建form回调、A059无记忆Q设置timer两句不再作为依据；当前formal/source正确，旧原件与CLOSED保留。G2-5挖矿播种、G6-5按产量档加2/3/3为旧导航错误；实际Lottery/地牢播种、成功株+1/qty≥max另+1。G5-1音乐在内部/经验门前，不能将后门早退扩大。统计C01及管理G9-3已由独立integration有限补归属。','','M02-003原必修候选保留original_submission/M10反证/root裁决；完整WP65§4.2+WP10§5.2支持无旧档成功两提示但未复制，不列必修。M08 AI217导航含4标题，M09213实际测试设计补相应消费；未执行测试。']
(OUT/'junction-review.md').write_text('\n'.join(md)+'\n')
regby={x['id']:x for x in reg['records']};rows=list(csv.DictReader((OUT/'regression-229.tsv').open(),delimiter='\t'))
for x in rows:
 z=regby[x['original_id']];x['third_review_consumption']=z['status']+';scoped_projections_not_runtime_PASS';x['new_finding_relations']=';'.join(q['id'] if isinstance(q,dict) else q for q in z.get('new_finding_relations',[]));x['assigned_modules']=';'.join(sorted({a.get('module','') for a in z['current_module_joins']}));x['executed']='NO'
with (OUT/'regression-229.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
a=read(OUT/'accepted-341-scope.json');keys={x['record_key']:i for i,x in enumerate(acc['records'])}
for x in a['full_mapping']:
 k=x['record_key'];z=acc['records'][keys[k]];x['current_review_join']={'path':str((I/'accepted-341-joins.json').relative_to(REPO)),'pointer':f'/records/{keys[k]}','scope':'Exact batch/ID/candidate/ACT/independent_report qualified local contribution; no whole-ID/signature/runtime expansion','status':z.get('status','QUALIFIED_LOCAL_JOIN_COMPLETE')}
 x['new_finding_relationship']='See full qualified join and canonical history relation; no automatic reopening/closure'
dump('accepted-341-scope.json',a)
p=read(OUT/'progress.json');n=datetime.datetime.now(datetime.timezone.utc).isoformat();p['integration_auxiliary'].update(state='COMPLETED',updated_at=n,output=str(I.relative_to(REPO)),report=str((I/'integration-report.md').relative_to(REPO)),completion_reason='54+8/229/341 qualified substantive joins and432/131 attribution complete; limits/disputes preserved')
p['integration'].update(state='COMPLETED',updated_at=n,scope='62 existing junction/chain current judgments +18 new finite chains, canonical25 adjudication, 229/341 qualified mapping and limitations',completion_reason='Actual independent root and helper substantive reconciliation completed; no formal update or runtime claim')
p['phase']='REPORT_FREEZE_AND_AUTHORIZED_PUBLICATION';p['updated_at']=n;dump('progress.json',p);dump('module-results.json',p['modules']);dump('integration-results.json',{'primary':p['integration'],'independent_helper':p['integration_auxiliary'],'scope_helper':p['scope_auxiliary'],'denominators':{'existing_junction':54,'existing_chain':8,'new_chain':18,'regression':229,'accepted_contributions':341},'canonical_decisions':'findings.json/adjudications.json','finite_completion':'All12 agreed finite static module scopes completed; explicit available-but-not-fully-reviewed semantics, full content, activation, host/resource/runtime limits remain. Not full capability completeness/runtime PASS.'})
summary=read(OUT/'coverage-summary.json');required=[x for x in findings if x['disposition']=='REQUIRED_REVISION']
report=['# 第三轮全局独立评审总报告','', '**有限静态评审与集成已完成；当前规格仍有23项必修缺口，不能宣称完整内容、全部可得参数、实际启用或游戏运行通过。** 25保留ID为19项P2、6项P3；其中23 REQUIRED_REVISION、1 OPTIONAL、1 NO_REQUIRED_REVISION。未更新正式规格、参考、公共登记或历史裁决。未来update未启动。','', '本轮：第一轮本地WP review/update；第二轮全局review及B01–B21整改/229关闭/FINAL1–2；第三轮本次本地review，后接用户日后另行指示的云端update。今天只有review与成果发布。','','固定交付commit `86b4d7e1d8645e75af91a215240f8786a5bb4ca8`/tree `42c29efb5422772a1d90f657f25983600f500f28`。受审正式actual `167296dbe9e2384627b0ed696e87aeb01f211252`/tree `33598d8a2a3acdd093cc4fe23f48eea8666100f3`：131逐文件工作字节/blob/SHA256/bytes一致；交付整仓tree因报告导航不同，不要求等于actual。参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`/tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，432工作字节身份一致/无tracked dirty。必要151/13/14/2/控制与覆盖逐字节匹配，旧62候选完整保全。详baseline/protected-input-check。','','独立review实际任务、入口、角色和模型请求见[progress.json](progress.json)与[module-results.json](module-results.json)。主review /root独立于formal作者/登记，M02/M04/M05及跨模块亲审；其余为fresh可见subagent。gpt-6.1-sol/ultra/Standard(default)请求被接纳，回显UNVERIFIED；root回显同样未验证，无Fast/隐蔽CLI模型。平台实际4并发槽含主角色，分批公开派发；没有伪造Desktop独立链接，真实父会话入口 codex://threads/01a12bbf-9300-7833-82d7-d392ae9fa731。旧任务未恢复，停止回执完整复制静态审计/原件不变。','','独立能力分母从参考域入口、调用者、数据、配置、UI与工具发现，757分域行为族含共享投影：601 SUPPORTED_STATIC、139 PARTIAL、7 UNRESOLVED、9 MISSING_MATERIAL、1 NOT_REVIEWED。不是互斥Feature数、旧113、方法名或源文件数。432文件均分类归属，131正式均逆向归属，15856条导航记录保实际状态；条数不签语义。核心行为/数学/正常失败边界有审读范围，可供实现/测试设计；所有有效完整性/未读条件仍限定。','','| 模块 | 有限行为族 | 当前范围/产物 |','| --- | ---: | --- |']
for m in summary['modules']:report.append(f"| {m['module']} | {m['capability_families']} | [{m['module']}报告]({m['module']}/report.md)；source/spec/测试范围和限制见对应七产物 |")
report+=['','完整差异如下；每项精确source/spec身份、前提、最小反例、影响、风险、关联/异议、建议及可验证结束条件见[findings.json](findings.json)。','', '| ID | 严重性 | 处置 | 具体问题 |','| --- | --- | --- | --- |']
for x in findings:report.append('| '+x['id']+' | '+x['severity']+' | '+x['disposition']+' | '+x['title'].replace('|','／')+' |')
report+=['','优先顺序：先明确输入格式/通知异常/持久身份与世界恢复的合同，再处理消费/部分提交及每击失败链，之后补UI/图鉴消费者、数学/工具小缺口。可按[proposed-batches.json](proposed-batches.json)六个主题批并行与依赖整合；U07统一整合，U08仅用户选择的可选范围。所有23必修各有唯一主题批，跨批共享文件唯一写者及顺序交接见[shared-file-owners.json](shared-file-owners.json)。补当前事实不代表未来必须永远复刻旧bug，兼容政策由用户决定。','','229旧必修控制全部按有效qualified scope、原/批准对象、相应FINAL、当前模块投影映射；初始无模块分配的统计C01由独立integration补有界实际统计。341贡献逐exact五元组/local scope，不推整ID或新签名；21/21接受/229 CLOSED/0 OPEN仍是历史约定范围，未无证据改写或重新执行。旧A019/B030/D012/D017非必修保原裁决。[regression-229.tsv](regression-229.tsv)、[accepted-341-scope.json](accepted-341-scope.json)和完整integration附件可定位全部记录/关联。','','54既有交界/8链及18新增链由独立主角色和integration reviewer实质归并，[junction-review.md](junction-review.md)给具体正常/失败/边界，JSON保完整前提和局部未知。M02-003保原提交与M10反证/root NoRequired；旧A022/A059错误邻接片段剔除复用、G2-5/G6-5导航纠正，其余历史记录完整保留，未转移旧验收签名。','','可得但未全审：PBS/翻译语料/完整物种与设施名单组合；部分Transitions逐像素body/错误修复输出/具体消费者；完整皮肤字体长词矩阵/摘要坐标/球粒子参数与反馈显示；归档/字体/音色/exe/DLL内容；跨世代和动态插件/实际编译启用。这些不全是缺资源，逐能力记录见[limits-and-missing-materials.md](limits-and-missing-materials.md)及[范围审计](delivery-scope-audit/scope-audit.md)。未知不等于无问题，也不等于已支持。','','真实缺项为Graphics/Audio/Plugins/Game.ini/Game.rxproj、MapInfos/地图、System/Tilesets/CommonEvents/动画数据库等。knownpoint.bmp/selpoint.bmp实际可得；头部/身份并不证明工具渲染。真实地图/Demo接待/授予/收费奖励/解锁/录制回放、宿主时序/字体/输入/音频与异常效果均未证。运行观察、参考/行为/静态案例执行、真实Demo链均0；Git/hash/JSON/PBS字段/BMP头检查不当运行证明。','','净室质量：本轮按外部身份/顺序/数学/状态/异常/取消描述，源路径和函数身份只取证定位；不把源容器/类/继承强制成TypeScript API、RPG Maker模板或生产实现。新必修建议仍为文档/表/向量，并非实际修复。','','完整云端接手文件： [cloud-third-update-handoff-prompt.md](cloud-third-update-handoff-prompt.md) 与 [cloud-third-update-handoff-manifest.json](cloud-third-update-handoff-manifest.json)。完整提示词在所有实质review完成后生成，不预写PASS。成果独立review分支已授权发布；本次冻结时尚未提交/推送，实际精确发布/读回状态随后记publication receipts与本报告发布附记，不能把本地路径当云端可达。报告发布不授权今天update，不合并main。']
(OUT/'final-report.md').write_text('\n'.join(report)+'\n')
print('root finite integration/report frozen; publication still not started')
