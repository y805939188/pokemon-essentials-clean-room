"""Serialize this context's completed readings and independent judgments; never run reference or recovered programs."""
import json,hashlib,subprocess,datetime
from pathlib import Path
P=Path(__file__).resolve().parent
W=Path('/workspace/r8-receptions/combat-presentation')
R=Path('/workspace/pokemon-essentials')
C='18d21310bdc360c87d7ffd886df7d06aef8604a7'
B='fd1df570cad987dc3852a3b958f03916e317f7fe'
RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
I=P/'input-cache'/C
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(n):return json.loads((I/n).read_text())
def save(n,o):(P/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def git(repo,*args):return subprocess.check_output(['git',*args],cwd=repo)
def ident(repo,path,commit):
 d=(repo/path).read_bytes(); fixed=git(repo,'show',commit+':'+path)
 assert d==fixed,(path,'working bytes differ')
 return {'path':path,'commit':commit,'blob':git(repo,'rev-parse',commit+':'+path).decode().strip(),'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'lines':len(d.splitlines())}
f=read('forward-mapping.json');a=read('atomic-assertions.json');rv=read('reverse-mapping.json')
notes='''世代8下提示条开；坐标是席位函数，焦点常量不等于精灵实际坐标。
动画队列先推进再移除；BACK中止与普通菜单取消是不同出口。
五种可见模式逐项设置；brief等待由后继消息入口消费。
块只在首次全显执行；自动快进不跳过全显后的计时。
Scene第三参必填，Battle包装默认-1；初始Yes/索引0不等于取消值。
新建普通精灵的局部救援不传递到平面；换位还须同步记忆和成员绑定。
结束清理是正常路径；显示个体与真实物种门需分别保留。
视口、记忆及队列先建，初始图形之后才调用开场等待。
存在的席位分别建框/立绘/影子；野生初态暗色与后继恢复相接。
base0存在控制双方共同前缀；消息时段是独立资源选择。
只有成员构造接收动画队列；影子独立持有动画位图，不接收该队列。
Call双门、模式表和BACK许可分别对照；返回码交命令阶段消费。
普通招式需块接受，Mega/Shift码有独立处理；记忆写回不消耗PP。
展示序号反查原队伍后交战斗域校验；列表取消和子菜单取消不合并。
过滤后的物品身份与原口袋索引分离；各取消层只退相应画面。
nil候选不可选，空串仍有按钮；NearAlly对象传参和执行资格分层。
导航只检查非nil，USE不重复合法性；真实目标登记在接收者。
三个淡出桥各传自己的长度/预览/成员；遗忘槽位由摘要接收。
开场队列与野生恢复共同等待；异色公共动画受开关而固定开场仍在。
多球与训练家共同更新，各框等自身球；召回的球/框两阶段有序。
已有提示条先退，后显示新条；replace不旁路出现流程。
HP公共效果开关不控制HP条；零EXP差与无成员是分别早返。
升级两窗有序；濒死框和成员并行，投球还等待队列空。
影子恢复仅在yield正常返回后；源码没有异常确保恢复。
精确映射与类型默认路径不同；hitNum不能随意加到默认映射。
招式播放包影子，Common入口不包；焦点/原点恢复也仅正常后段。
球公共动画是入队非阻塞；移除成员参与不等于销毁原成员。
菜单整体门和子精灵门叠加；dispose幂等不证明其它入口事务性。
五种命令图块映射完整；文本替代分支仍按相同返回协议。
成员重绑、shift变化触发各自刷新；构造/销毁分支区分两菜单样式。
图形总PP0省文字，文本显示占位；名称颜色采样并非招式规则。
成员为空早返在外层refresh，不在每个附加按钮刷新方法内。
非对称席位布局、空串及nil图块各有分支；没有文本替代。
单席玩家才开启数字和EXP；重新初始化不会主动撤销已开的门。
补间HP与显示整数分开；EXP无范围和无差值各自早返。
图标的状态、异色、Mega/Primal/owned门互相不替代。
条宽偶数舍入与颜色比较独立；颜色读取浮点补间值和整数阈值。
HP1秒和EXP比例时长分开；满条闪与选择摆动有各自相位。
背景属性跟随条本身传播；成员名与能力名不是战斗能力触发器。
metrics参与真实基点，选择偏移另算；叫声回调是请求而非听觉观测。
影子没有场景动画队列；位图更新、位置metrics及资源重选独立。
本轮起始running即继续等待，最后结束可需下一轮才done。
球RGB只定三通道，alpha由派出/召回/捕获调用者各设。
出现叫声绑定缩放完成回调；该缩放与XY同长，但不是XY回调。
16×14字段与释放consumer完整对照；CHERISH射线两tone被分支绕过。
循环有限范围覆盖15对粒子/10射线；随机请求域不认证真实抽样。
16×17字段独立于释放表；NEST字段读取与后继同刻隐藏都保留。
9组完整内外路径、NET网页/尾环与球时长标记逐支对照。
成功点击声、三星曲线和透明度是静态请求；星寿命靠临时销毁。
回收5粒子及两环时序独立，poke_ball参数本入口不消费。
背景/平台/成员起点按侧，奇数宽用实际整数偏移而非强制对称。
对方条最终X248减位图宽；球(174,84)，不能写成0减宽。
框8单位位移与特性条出现音/消失隐藏是不同轨道。
隐藏时复位opacity不撤销已登记运动；fullAnim不控制训练家全部行为。
玩家与对手基点不同，只有对手开场额外10；原影子可见才恢复。
收回使用绝对音/淡出点，伤害恢复原可见而不改变濒死状态。
三类叫声/75音高/等待+2有独立反证；运动除法需附整数前提。
展示摇动压缩不改变原成功判据；成功球移出临时销毁所有权。
挡球只走返回轨迹；不接吸入/成功球保留。
Debug空操作与blitz随机不提供真实玩家UI证据。
Debug固定返回须由caller解释；日志不等于呈现。
Debug缺失move读取在抽样前失败；Call总概率7/75，不写成1/10。
命名、送旧成员盒、删除和记忆左移分序；无回滚保证。
每只按图鉴到存放完整处理；最后清队列，异常可留下已处理前缀。
无存活替代目标在nil状态查询先失败；捕获成功先移除再经验。
HP/状态浮点结果最后floor；暴击入口与普通最多四次各有边界。
27索引与25属性口径不同；焦点变换退化轴置0。
转换和append都组装数据；没有活动默认转换caller的负证据限脚本树。
五种时序的默认及nil兼容与一基显示帧分开。
构造至少1不代表resize守卫；selected可等于len。
speed20仅元数据，实际播放器固定20fps；允许零帧输入边界。
前景旧透明度取自身；共享渐变旧值按访问顺序更新，nil坐标会先失败。
普通图案192五列与负图案整图分开；编辑器隐藏比较不成立。
借用成员位图不拥有销毁；58粒子和四平面归播放器。
跳帧不补timing；焦点和反向镜像实际分支，编辑器另偏移64。
四个handler集合各有回退；失败统计先写后调handler。
倍率按真实球种/环境/轮数/世代门，未登记球维持原值。
Level无参查询固定玩家侧0的活成员；不能泛称目标方本侧。
Dream视为睡眠与真实状态倍率分层；Heal和Friend在成功后提交。'''.splitlines()
assert len(notes)==79,len(notes)
cor={
'EXTCP-F005.A04':('QUALIFIED_LAYER','Scene普通列表参数必填；Battle.pbShowCommands834–835才默认-1并传下。原默认说法在公开包装层成立，不判正文错误。'),
'EXTCP-F011.A04':('CORRECTED_SOURCE_FACT','仅成员精灵接收@animations；影子构造无队列参数，更新自己的AnimatedBitmap。Initialize185/187，Objects524–540/646–653。'),
'EXTCP-F032.A03':('QUALIFIED_METHOD','无成员的早返在FightMenu.refresh431–436；不能扩大到直接调用refreshMegaEvolutionButton/refreshShiftButton。'),
'EXTCP-F044.A14':('QUALIFIED_CALLBACK','出现叫声绑定moveZoom完成回调，XY恰与缩放同为5单位；不要把回调归到moveXY。Base239。'),
'EXTCP-F052.A03':('CORRECTED_SOURCE_FACT','对手排列条barX=248后减bitmap.width，最终(248-width,114)；球(174,84)。Animations105–110。'),
'EXTCP-F057.A02':('QUALIFIED_NUMERIC_DOMAIN','源码除以整数8但Ruby除法取决于被除数类型；整数几何时floor，浮点几何不强制floor，均至少10。'),
'EXTCP-F078.A02':('QUALIFIED_COLLECTION','Level调用allSameSideBattlers无实参；接收者默认索引0，取玩家侧活场上成员，非任意目标所在侧。Battle458–461。')}
groups=[]
for i,g in enumerate(f['facts']):
 groups.append({'id':g['id'],'source':g['reference'],'full_read_range':g['source_range'],'independent_judgment':notes[i],'assertion_ids':g['atomic_assertion_ids'],'status':'RECEIVED_BOUNDED_STATIC_WITH_EXPLICIT_CLARIFIERS','not_whole_formal_acceptance':True})
objects=[]
for x in a['assertions']:
 g=next(g for g in groups if g['id']==x['group']);z={'id':x['id'],'original_complete_meaning':x,'source':g['source'],'source_read_range':g['full_read_range'],'independent_group_reason':g['independent_judgment'],'status':'RECEIVED_SOURCE_FACT_WITH_BRANCH_PREMISES','formal_scope':'Scoped interface comparison only; no whole-section PASS','actual_read_evidence':'reading-ledger.json; views/manual lossless complete text; full primary source read','execution':'NOT_EXECUTED'}
 if x['id'] in cor:z['status'],z['effective_meaning_and_reason']=cor[x['id']]
 else:z['effective_meaning_and_reason']=x['assertion']
 if x['id'] in ['EXTCP-F057.A03','EXTCP-F057.A04','EXTCP-F057.A05','EXTCP-F057.A06','EXTCP-F057.A07']:z['formal_scope']='Finite REQUIRED_PROPOSED CP002 counterreview, root decision pending'
 elif x['disposition']=='PROPOSED_SCOPE_GAP_GR8_EXTCP_002':z['formal_scope']='Exact static request received; broad mandatory precision NOT decided; strongest NO_REQUIRED accepted for media freedom outside finite faint-cry counterexample'
 objects.append(z)
for fn in ['release-variance-fields.json','capture-variance-fields.json']:
 q=read(fn)
 for row in q['records']:
  for x in row['fields']:
   z={'id':x['id'],'original_complete_meaning':x,'ball':row['ball'],'source':q['source'],'group':q['group'],'status':'RECEIVED_TYPED_VALUE_AND_CONSUMER_BRANCH','effective_meaning':{'field':x['field'],'index':x['index'],'value':x['value'],'scalar_leaves':x['scalar_leaves']},'reason':f"{row['ball']}的{x['field']}，索引{x['index']}，值{json.dumps(x['value'],ensure_ascii=False)}；按consumer_range所示完整消费者读取，类型值不是额外标量原子。",'formal_scope':'Source request only; no automatic required transcription of all ball fields','actual_read_evidence':'views/'+('release' if fn.startswith('release') else 'capture')+'-lossless-compact.json plus complete source table and consumer','execution':'NOT_EXECUTED'}
   if fn.startswith('release') and row['ball']=='CHERISHBALL' and x['index'] in [0,1]:z['status']='CORRECTED_RUNTIME_PURPOSE';z['reason']='值确实定义且已实读；CHERISH分支条件绕过这两个variances索引，不是先读后覆盖；逐色循环请求取代普通tone读取。'
   if fn.startswith('capture') and row['ball']=='NESTBALL' and x['index'] in [12,13,14]:z['runtime_qualifier']='依实际index crosswalk；下粒子仍建立/读取其参数，显示同刻又隐藏；不能写成未消费或无记录。'
   objects.append(z)
q=read('ball-color-fields.json')
for x in q['records']:objects.append({'id':x['id'],'original_complete_meaning':x,'source':q['source'],'status':'RECEIVED_TYPED_RGB','effective_meaning':{'ball':x['ball'],'rgb':x['rgb']},'reason':f"{x['ball']}三通道{json.dumps(x['rgb'])}完整匹配源分支；派出/召回/捕获调用另设alpha，DEFAULT是显式回退，不额外增通道原子。",'actual_read_evidence':'ball-color-fields.json FULL and BaseAnimation65–166 plus all named consumers','formal_scope':'media precision policy remains root decision, not blanket required','execution':'NOT_EXECUTED'})
assert len(objects)==1045 and len({x['id'] for x in objects})==1045
save('reception-ledger.json',{'schema':'r8-independent-reception/v2','status':'EXTRA_INDEPENDENT_FINITE_RECEPTION_COMPLETE_NOT_CANONICAL_TASK_FINAL','role_redirect':'redirect-receipt.json','recorded_utc':now,'denominator':{'groups':79,'objects':1045,'manual':533,'variance_fields':496,'RGB_fields':16,'scalar_leaves_not_extra_atoms':1248},'groups':groups,'objects':objects,'no_template_pass':'This serialization preserves per-object full text/value and 79 independently authored judgments. It grants no global/whole-formal PASS; seven manual clarifiers and two runtime-purpose corrections are explicit. Reading happened before serialization.'})
# Exact manual reverse meanings and their bounded formal/source interpretation.
reverse=[]
rcor={'EXTCP-R016.6':'伙伴身份错配需跨引已读WP38§6；所链WP67-A§8不是该细节的完整当前条款。','EXTCP-R018.4':'HP宽2像素量化为源事实；不能把当前WP67-A§9.2当成已有该精度文字的证据。','EXTCP-R019.4':'倒下裁底细节为源事实；当前§9.3不完整规定该参数，音频有限required另见CP002。','EXTCP-R019.6':'影子包装异常恢复定位应落§9.4相关核心播放，不能只用§9.3来授全部覆盖。'}
for c in rv['clauses']:
 for x in c['subassertions']:
  reverse.append({'id':x['id'],'complete_meaning':x['assertion'],'formal':c['formal'],'formal_range':c['range'],'source_groups':c['source_groups'],'status':'RECEIVED_SCOPED_PROPOSITION_NOT_WHOLE_CLAUSE_PASS' if x['id'] not in rcor else 'FORMAL_LINK_CLARIFIER','reason':rcor.get(x['id'],'按所列完整有关条款与必要源单位比较此列明命题；该组范围内其它文字不自动获得本命题信用。'),'independent_evidence':'reading-ledger.json; primary source full; dependency units; same source groups already received once'})
assert len(reverse)==150
save('reverse-reception.json',{'status':'COMPLETE_BOUNDED_INTERFACES_WITH_LINK_CLARIFIERS','primary_formal_clause_denominator':0,'legacy_groups':31,'legacy_propositions':reverse,'selected_interface_assertions':rv['selected_interface_assertions'],'selected_interface_disposition':'All20 complete meanings actually read; accept bounded producer/receiver comparisons under interfaces.json, no whole-formal census','whole_formal_acceptance':False})
# Typed purpose for all original files. Provenance fields do not become business credit.
semantic={'atomic-assertions.json':'533原子完整意义逐个在reception-ledger；table_artifacts为已实读的3个有限表入口。','forward-mapping.json':'79组完整范围/前提/消费者/原子成员，逐组在本台账独立判定。','reverse-mapping.json':'31/150列明命题及20选择接口全文已读，主formal分母0；反链纠正在reverse-reception。','release-variance-fields.json':'全部224完整逻辑字段、544标量及消费者crosswalk；CHERISH两字段用途纠正。','capture-variance-fields.json':'全部272完整逻辑字段、656标量及消费者crosswalk；NEST读取后隐藏保留。','ball-color-fields.json':'全部16RGB完整值及48标量，alpha不在此表，默认回退独立。','proposals.json':'完整CP002和撤回H001、全部八节/前提/正常取消异常/验收，独立counter文件逐项反证。','interfaces.json':'IF01–09加continuation的IF09/IF10完整边；重复IF09按edge区分，见本interfaces。','bounded-contributions.json':'六个provider单位66命题完整实读；必要源Producer重新实读，不继承provider全文件或签字。','review.md':'完整作者结论及其NOT_RECEIVED/候选/范围边界，未当独立批准。','limits.json':'14条当前范围处置全文；旧full_read布尔仅作者历史声明，不继承R6PASS。','validation-incidents.json':'全部2失败及4continuation更正、目录误计纠正原样保留；不撤销真实失败历史。','progress.json':'全文作者时序/分母/配置/未执行/未接收声明；非本context实际证据。','reading-ledger.json':'全部primary/dependency/合同/continuation/纠正全文；作者read不是本contextread，逐路径分开。','environment-checks.json':'全部16历史命令及stdout/stderr/exit/UTC全文；只证明作者当时工具观测，不认证业务或本配置。'}
pur=[]
for e in json.loads((P/'input-identities.json').read_text()).get('files',[]):pass
for file in sorted(x for x in I.rglob('*') if x.is_file()):
 rel=file.relative_to(I).as_posix();d=file.read_bytes();z={'path':rel,'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'original_binding':'input-identities.json','purpose':semantic.get(rel),'execution':'NOT_EXECUTED','business_credit':False}
 if file.suffix=='.json':z['complete_top_level_field_purposes']={k:('Semantic/provenance meaning as described for this file; identity/read/pass/count fields never imply own reading' if rel in semantic else 'Inventory/identity/transport/bookkeeping only; no new behavior verdict adopted') for k in json.loads(d).keys()}
 if not z['purpose']:
  if rel.endswith('.py'):z['purpose']='作者惰性构建/校验程序，仅语法解析并把未精确嵌入其它报告的长字符串无损呈现实读（views/procedural-literal-view.json）；包含的533业务文字与已接收对象同义，不增原子；不执行、不中继其PASS或时间。'
  elif rel.startswith('inputs/') and rel.endswith('.json'):z['purpose']='完整库存身份/路径/散列/归属，不是业务正文。全部字段仅冻结12主R/0主F及95+38/51+18发现依赖；库存不授阅读信用。'
  elif rel.startswith('publication'):z['purpose']='完整发布transport记录：commands/remote entries/mode/blob/bytes/SHA/tree/UTC只作作者旧发布出处；本次自己的独立恢复和发布另核，不继承语义。'
  elif rel=='validation.json':z['purpose']='required_files/json_files/73identitychecks/6inputcopies/R6limitidentity/mappingcounts为机械一致性；semantic_review_pass=false、业务NOT_EXECUTED已读，不继承PASS。'
  elif rel=='coverage-and-gaps.json':z['purpose']='217files/16partialgaps/9continuation paths为覆盖库存及作者阅读声明；remaining_semantic_decisions、global gap全文保留并按当前任务重判；不把103/45发现池未读改limit或自动追加主责。'
  elif rel=='inputs/combat_presentation.md':z['purpose']='完整原委托prompt和边界全文；仅采用固定有效任务约束，原禁发布被后续明确授权覆盖。'
  elif rel.endswith('eighth-global-review-prompt.md') or rel.endswith('review-SKILL.md'):z['purpose']='完整36653B全局合同/3598B最终态修订约束全文实读，同字节别名只一次阅读信用。'
  else:z['purpose']='精确身份/checkpoint元资料全文；只绑定冻结输入与原配置未知，不构成业务通过。'
 pur.append(z)
assert len(pur)==31
save('input-purpose.json',{'schema':'r8-complete-input-purpose/v1','files':pur,'all_current_business_meanings':'1045 primary objects, 150 scoped legacy propositions,20 selected interfaces,66 provider assertions, candidate and withdrawn H001, failures/qualifiers fully presented and independently assessed. No recovered script executes.','limits':'Old historical full_read/procedural receipts are retained as attributed author claims, not inherited current signatures.'})
# Provider payloads, all finite assertions kept exactly; source re-read is separately explicit.
bc=read('bounded-contributions.json')
save('bounded-reception.json',{'provider_artifact':bc['exact_provider_artifact'],'units':[{**u,'independent_disposition':'RECEIVED_FINITE_SOURCE_AND_CONSUMER;no provider-whole-file signature inherited','independent_evidence':'reading-ledger.json:TrainerType whole134;prepare_battle209–304 complete;player whole844;SceneInitialize whole191;Scene primary helper whole419;IconSprite wrapper whole243'} for u in bc['payloads']],'assertions':66,'same_byte_duplicates':'D28/D07/D08 overlap own primary, no extra primary count or vote','canonical_reception':'ROOT_ONLY_NEW_ROUTED_RECEIVER; this is extra contribution'})
# Actual source and formal intervals. No historical author ranges are promoted.
ledger=json.loads((P/'reading-ledger.json').read_text())
ledger['status']='ACTUAL_READS_COMPLETE_FOR_FINITE_EXTRA_CONTRIBUTION';ledger['recorded_utc']=now;ledger['read_utc_qualification']='Exact start/end per reading tool not separately captured; authoring UTC above is not retroactive reading UTC.'
ledger['role_redirect']='redirect-receipt.json; actual original logical agent remains same; no new context count on rename'
ledger['reads'] += [{'path':'views/manual-041-048.txt through manual-073-079.txt','range':'FULL all individual assertion texts','output':['486fea','c9b02c','6c0e78','7f2eaa','6e9d51','af5b2e','51f8c8'],'qualification':'Original session actual complete lossless views; output handles are aids, not stable platform UUIDs'}, {'path':'views/release-lossless-compact.json + capture-lossless-compact.json','range':'FULL reversible complete16rows each','output':['989b6d'],'qualification':'Reconstruction equality verified; earlier truncated verbose view0e344f retained, superseded by full compact read'}, {'path':'reverse-mapping.json','range':'All31 groups150 propositions + all20 selected interfaces','output':['f19914','1de97d','27f45f'],'qualification':'1de97d truncation supplemented by27f45f; repetitive source-ID arrays represented only after exact set equality proof'}, {'path':'reading-ledger.json AUTHOR','range':'All61dependency entries and corrections/root metadata','output':['0ab1e9','5161b3'],'qualification':'Provenance only, not own source credit'}, {'path':'views/procedural-literal-view.json','range':'FULL two contiguous Unicode slices0:7800,7800:end; no content omitted','qualification':'Only strings not identically embedded elsewhere are additional readings; all code remains inert'}, {'path':'limits.json,validation-incidents.json,progress.json,environment-checks.json,inputs/combat_presentation.md','range':'FULL each','qualification':'Actually presented in this context; old pass/read/config claims not adopted'}]
actual=[]
def add(root,path,intervals,purpose,whole=False):
 y=ident(root,path,RC if root==R else B);y.update({'read_intervals':intervals,'whole_file':whole,'purpose':purpose,'evidence':'Actual numbered full continuous text presented in this independent context before serialization','execution':'NOT_EXECUTED'});actual.append(y)
for x in f['facts']:
 path=x['reference']['path']
 if not any(y['path']==path for y in actual):
  n=len((R/path).read_text().splitlines());add(R,path,[[1,n]],'12 primary complete definitions, every79group and1045 objects',True)
source_extra={
'Data/Scripts/010_Data/002_PBS data/009_Species_files.rb':([[1,246]],'cry selection and length'),
'Data/Scripts/005_Sprites/010_PictureEx.rb':([[1,548]],'process scheduling,SE registration and receiver'),
'Data/Scripts/008_Audio/002_Audio_Play.rb':([[1,278]],'audio default resolution and request delivery'),
'Data/Scripts/008_Audio/001_Audio.rb':([[1,154]],'duration decoder request static only'),
'Data/Scripts/001_Technical/002_Files/001_FileTests.rb':([[1,142],[181,242]],'complete necessary pbResolveAudioSE/pbResolveBitmap/RTP exists,getPath,eachPathFor,eachPath; incidental prefixes no complete credit'),
'Data/Scripts/004_Game classes/002_Game_System.rb':([[237,249]],'complete se_play and se_stop'),
'Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb':([[1,160]],'complete HP/faint/PP through151;156–160 form prefix not whole method credit'),
'Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb':([[1,55],[247,317],[405,515]],'complete pbAbort,pbStartBattle/Core,pbEndOfBattle;prefixEnsure not whole credit'),
'Data/Scripts/001_Technical/002_RubyUtilities.rb':([[390,406]],'complete nil_or_empty and lerp'),
'Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb':([[1,265]],'full command registration,rollback and return receivers'),
'Data/Scripts/011_Battle/001_Battle/006_Battle_ActionUseItem.rb':([[1,149]],'full item families consume/refund'),
'Data/Scripts/011_Battle/007_Other battle code/004_Battle_Peers.rb':([[1,77]],'full capture storage peer'),
'Data/Scripts/011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb':([[1,132]],'complete move selection,target registration/permitted-target receiver;priority sort outside this unit'),
'Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb':([[1,128],[220,302]],'complete canSwitch family,partyScreen,recall/replace/sendout'),
'Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb':([[92,271]],'complete gainExpOne and learnMove'),
'Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb':([[120,177],[212,252],[355,366]],'complete storage lookup/assign/caught store and regional delegation'),
'Data/Scripts/016_UI/005_UI_Party.rb':([[479,533],[705,713],[746,853],[912,925],[958,990],[1023,1036]],'complete relevant scene start/end,summary,choose/navigation and wrapper receivers'),
'Data/Scripts/016_UI/006_UI_Summary.rb':([[184,215],[814,845],[929,993],[1232,1381]],'complete forget setup/detail,move reorder,choose,main scene and screen wrappers'),
'Data/Scripts/011_Battle/003_Move/001_Battle_Move.rb':([[1,135]],'complete move wrapper initialization,PP/target relevant methods;no entirefile claim'),
'Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb':([[1,64]],'full distinct animation/data caches'),
'Data/Scripts/007_Objects and windows/009_Planes.rb':([[1,76]],'full animated/colored plane receiver'),
'Data/Scripts/010_Data/002_PBS data/010_SpeciesMetrics.rb':([[1,101]],'full metric registration/default and application'),
'Data/Scripts/019_Utilities/003_Utilities_BattleAudio.rb':([[1,149]],'full battle music priorities'),
'Data/Scripts/011_Battle/008_Other battle types/001_SafariBattle.rb':([[218,271],[295,365],[387,502]],'complete scene/hook/menu/body,constructor and caught/seen gates;not ThrowBait/Rock wholeproducer'),
'Data/Scripts/011_Battle/008_Other battle types/002_BugContestBattle.rb':([[1,83]],'full bug override'),
'Data/Scripts/011_Battle/008_Other battle types/003_BattlePalaceBattle.rb':([[1,167]],'complete tables/category/player automatic selection and pinch;AI switching outside finite UI assertion'),
'Data/Scripts/011_Battle/008_Other battle types/004_BattleArenaBattle.rb':([[41,204],[222,366]],'complete battle constructor/menu/score/counter/replacement and scene judgment receivers;success-state internals not separately signed'),
'Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb':([[74,135],[182,226]],'complete record registration/command reception/paused display;not serialization wholefile'),
'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb':([[1270,1321]],'complete compile_animations and inactive conversion call'),
'Data/Scripts/011_Battle/001_Battle/001_Battle.rb':([[98,177],[215,328],[444,482],[505,577],[582,600],[816,844]],'complete needed ctor/owners/party/collections/opposing order/near/removal/displaywrappers;othermethods not full credit'),
'Data/Scripts/007_Objects and windows/005_SpriteWindow_text.rb':([[368,420],[526,622]],'complete busy,pausing,resume,position,maxPosition,skipAhead,updateInternal/update/curcharSkip;not whole renderer'),
'Data/Scripts/016_UI/025_UI_TextEntry.rb':([[180,247],[666,722],[739,779]],'complete keyboard/grid entry and naming wrapper finite cancel contract;not full editor component'),
'Data/Scripts/016_UI/007_UI_Bag.rb':([[1,44],[145,246],[337,455]],'complete item filtered mapping,scene init/fade/dispose/filter/choose'),
'Data/Scripts/020_Debug/002_Animation editor/001_AnimEditor_SceneElements.rb':([[451,511]],'complete preview play;no cache save'),
'Data/Scripts/020_Debug/002_Animation editor/005_AnimEditor_Functions.rb':([[376,677]],'complete timing list and SE/BG/edit property commit/cancel'),
'Data/Scripts/007_Objects and windows/001_RPG_Cache.rb':([[1,144]],'full cache/refcount wrapper'),
'Data/Scripts/007_Objects and windows/007_BitmapSprite.rb':([[1,243]],'full IconSprite/AnimatedSprite/BitmapSprite wrappers'),
'Data/Scripts/007_Objects and windows/008_AnimatedBitmap.rb':([[1,228]],'full animated image request wrappers'),
'Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb':([[71,142],[530,619]],'complete brief initialization,end/update,brief scene,dex entry wrapper;partial dummy/update and precedingnormal scene not whole credit'),
'Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb':([[95,220],[680,724]],'complete HP/status/display properties and opposes,near,ownership wrappers;edge prefixes not complete'),
'Data/Scripts/010_Data/002_PBS data/014_TrainerType.rb':([[1,134]],'full providerD05 identity/outfit selection'),
'Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb':([[165,207],[209,304]],'complete partner gate/shared identity setup,scene factory,prepare_battle providerD13;165–169 priorprefix not complete'),
'Data/Scripts/002_BattleSettings.rb':([[1,140]],'full named battle settings defaults'),
'Data/Scripts/001_Settings.rb':([[1,30],[205,230],[294,328]],'named constants generation8/party6/storage40/healfalse/dex entries only;credits/roamerprefixes no fullmethod credit'),
'Data/Scripts/018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb':([[1,144]],'full variant creation,wrapper,playback route and abortable scene'),
'Data/Scripts/018_Alternate battle modes/001_SafariZone.rb':([[118,163]],'complete pbSafariBattle budget writeback'),
'Data/Scripts/018_Alternate battle modes/002_BugContest.rb':([[361,418]],'complete pbBugContestBattle through404;later pauseprefix not accepted'),
'Data/Scripts/011_Battle/001_Battle/008_Battle_ActionOther.rb':([[1,201]],'full Shift/Call/Mega registration and request execution'),
'Data/Scripts/011_Battle/001_Battle/010_Battle_AttackPhase.rb':([[1,202]],'full actual family dispatch and phase caller'),
'Data/Scripts/011_Battle/001_Battle/007_Battle_ActionRunning.rb':([[1,160]],'full Run result producer/cancel/refusal/static probability')}
for path,(rs,purpose) in source_extra.items():add(R,path,rs,purpose,rs==[[1,len((R/path).read_text().splitlines())]])
formal_extra={
'user-interface/wp67-a-battle-interaction-and-presentation.md':([[1,348]],'whole parent battle presentation contract'),
'demo-dx/wp74-battle-animation-authoring-and-exchange.md':([[1,521]],'whole animation authoring/player scope'),
'engine-overworld/wp15-resource-matching-and-audio.md':([[1,224]],'whole resource/audio shared contract'),
'engine-overworld/wp16-world-rendering-and-visual-transitions.md':([[1,343]],'whole visual scheduler/host contract'),
'scope-statement.md':([[1,155]],'whole scope/history/limits;middle truncation supplemented45–100'),
'pokemon-rules/wp38-capture-and-receiving.md':([[1,146]],'whole capture/storage/current partial-commit clauses'),
'combat-requirements/wp40-commands-obedience-and-action-order.md':([[45,123]],'complete current command phase/registration/item/target sections'),
'combat-requirements/wp41-switching-positioning-and-escape.md':([[46,113]],'complete current eligibility/UI/recall/replace/sendout units'),
'combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md':([[59,96],[251,260]],'complete growth and explicitabort/ordinaryexception clauses'),
'creature-rpg/wp20-hp-status-moves-helditem.md':([[46,81],[121,171]],'complete HP and PP/persistent wrapper sections;trunc159–171 supplemented'),
'user-interface/wp66-a-party-and-summary-ui.md':([[15,65],[134,175],[192,199]],'complete relevant selection/navigation/reorder/forget contracts;trunc supplemented'),
'test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md':([[1,7],[360,426]],'all BT K01–K59 and R7HP vectors, staticnotexecuted'),
'combat-requirements/wp56-palace-and-arena-variants.md':([[1,141]],'whole Palace/Arena;scoring internals not independently main signed'),
'combat-requirements/wp58-battle-recording-and-playback.md':([[138,164]],'complete playback6.1–6.5 boundary'),
'pokemon-rules/wp53-safari-and-bug-catching-contest.md':([[49,113],[149,186]],'complete Safari battle and bug battle sections4/6,not whole session'),
'user-interface/wp17-messages-windows-input.md':([[59,85],[161,199],[268,286]],'complete shared message state,mode cancellation and update/failure clauses')}
for path,(rs,purpose) in formal_extra.items():
 full='deliverables/final-specification-set/'+path;add(W,full,rs,purpose,rs==[[1,len((W/full).read_text().splitlines())]])
ledger['actual_source_and_formal_reads']=actual
ledger['not_adopted_external_bodies']='No whole combat/UI/world/host/global-history reception. Author discovery157R/60F and own partial tails retain available-unread status outside the finite selected unit; never hostlimit.'
if 'source_reads' in ledger:ledger['source_reads_initial_records_preserved']=ledger.pop('source_reads')
if 'formal_reads' in ledger:ledger['formal_reads_initial_records_preserved']=ledger.pop('formal_reads')
ledger['identity_checks']='Each actual file compared byte-for-byte to fixed R/B8 git object by newly authored bookkeeping script; this is not reading or behavior execution.'
ledger['truncation_history']='Known truncated outputs preserved; ae8757 complemented42da4b,0e344f completed989b6d,1de97d completed27f45f,d52962 scope completed d053a8; later WP40/WP20/WP66 middles explicitly reread. No truncated total promoted.'
save('reading-ledger.json',ledger)
# Independent interface joins: producers/receivers actually read, not author declarations.
edge_notes=[
('IF01','command','CommandPhase full265 + ActionOther full201','主菜单及fight返回码→choice；失败继续，撤销Mega/退款/清槽的路径不合并。'),
('IF02','party-summary','Party scene/selection wrappers and Summary full necessary reorder/forget units + Switching1–128','显示下标反查后由域校验；Summary换序改持久列表而PP沿原move关联，不按槽推错写。'),
('IF03','item','Bag filtered item/choose units + UseItem whole149 + CommandPhase whole265 + normalEnd405–512','登记即时消费；1/2/3/5资格失败退款保留身份，球不共用复检退款，终局再消费残留身份。'),
('IF04','HP-EXP','Battler HP setter/ChangeSelf1–151 + GainExpOne92–224 + SceneObjects full698','实际HP/经验段先写再阻塞展示；后备/零差早返；异常不证明撤回领域写入。'),
('IF05','capture','CatchAndStore full271/PokeBallEffects full198/Peer full77/storage caught methods/dex brief/naming receivers','逐个caught→seen/owned→昵称→存储→队列尾清；送盒先于记录移位，伙伴共享身份+终局按旧索引消费可错配。'),
('IF06','author-player','MiscPBS full64,Compiler1274–1320,editor timings376–677/preview451–511,player full844','创作五时序正常OK才写可选字段；编译文件与两缓存寿命不同；player固定20fps跳帧不补timing，前景旧opacity自身。'),
('IF07','request-host','PictureEx full548 + metrics101 + planes76 + Bitmap243 + AnimatedBitmap228 + Cache144','过程登记顺序→属性/SE请求；真实像素音频/原生成功无观察。RGB/typed字段已接而全部精度是否必须留root政策。'),
('IF08','variants','Safari必要完整单位/包装118–160,Bug whole83/包装361–404,Palace1–164,Arena41–200/scene222–366,Recorded74–134/182–222,Challenge whole144','专用预算与背包分离；裁判显示一般消息；回放非全无交互，中止只场景；普通终局和设施wrapper善后分开。'),
('IF09','background-music','Initialize whole191 + BattleAudio whole149 + prepare_battle209–304 + TrainerType134','显式/next/地图/全局/回退；洞穴时段门读地图metadata不是覆盖后environment；底图与消息图独立时段。'),
('IF09','fixed-tracks','BaseAnimation/Animations/PictureEx/Species/Audio/SE resolver complete necessary units;WP67A/WP74/WP15/WP16 whole','重复IF09是不同edge，完整保存；有限濒死音频22/29/12反证独立成立，未扩大全部颜色为required。'),
('IF10','target-PP-HP','Battle505–577/ActionPriority1–132/Battler HP/status/display/ChangeSelf/Move wrapper units','nearBattlers不将对象转index，Battler.near会转但不是该caller；USE登记与执行资格分层，PP关联原对象。')]
save('interfaces.json',{'status':'EXTRA_INDEPENDENT_FINITE_JOINS_COMPLETE_ROOT_CANONICAL_ROUTE_PENDING','interfaces':[{'original_id':i,'edge_key':i+'-'+k,'independent_actual_units':units,'joined_facts':meaning,'evidence':'SOURCE_STATIC_NOT_EXECUTED','root_scope':'No whole foreign-domain or global PASS'} for i,k,units,meaning in edge_notes],'duplicate_id_preserved':'Original IF09 appears twice for different edges; edge_key disambiguates without rewriting original IDs','provider_receipt':'bounded-reception.json,6units66assertions;no double count','root_new_receiver':'01a14479-e75c-7131-85ed-aec1de217031; this redirected contribution is not its automatic task-final signature'})
save('proposal-counters.json',{'status':'COMPLETE_REAL_NONPROPOSER_COUNTER_CONTRIBUTION_ROOT_DECISION_PENDING','original_candidate':'GR8-EXTCP-002','counterreview':'cp002-independent-counterreview.md','eight_sections_complete':True,'strongest_no_required':'Media freedom and high-level interface scope valid for arbitrary trajectory/color detail; fails finite faint audio resource/pitch/wait request counterexample','disposition':'REQUIRED_PROPOSED_FINITE_AUDIO_REQUEST_CONTRACT_P3','finite_vectors':{'dedicated_1s':22,'ordinary_1s_pitch75':29,'neither':12},'vectors_status':'DERIVED_STATIC_NOT_EXECUTED','H001':'WITHDRAWAL_INDEPENDENTLY_CONFIRMED; foreground100→200 midpoint150, not background20→200=110','existing_ELR':'READY dispatch without actual receipt; not impersonated','root_canonical_authority':True,'automatic_duplicate_vote_or_acceptance':0,'new_actual_contexts_this_agent':1,'actual_parameters':{k:'UNVERIFIED' for k in ['model','effort','service_tier','speed','Fast','UUID']},'requested':{'model':'gpt-6.1-sol','effort':'ultra','service_tier':'default','speed':'normal','Fast':False},'business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'})
save('independent-clarifiers.json',{'manual':cor,'typed_runtime_purpose':['EXTCP-RELEASE-CHERISHBALL-ray.start_tone','EXTCP-RELEASE-CHERISHBALL-ray.end_tone'],'formal_link_clarifiers':rcor,'no_original_artifact_modified':True,'new_canonical_findings_created':0,'root_decides_whether_report_clarifier_or_formal_update':True})
print(json.dumps({'serialized_objects':len(objects),'groups':len(groups),'reverse_propositions':len(reverse),'selected_interfaces':20,'provider_assertions':66,'actual_source_formal_files':len(actual),'target_file_purposes':len(pur),'status':'EXTRA_FINITE_COUNTER_CONTRIBUTION_READY_TO_PUBLISH'},ensure_ascii=False))
