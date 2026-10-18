from pathlib import Path
import json,hashlib,subprocess,datetime,re,collections
P=Path('/workspace/pokemon-essentials-clean-room');O=P/'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/ui_navigation_audit';NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(p):return json.loads((O/p).read_text())
def write(p,v):(O/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
ids=read('identities.json');contracts=[]
for rel in ['AGENTS.md','review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/inputs/eighth-global-review-prompt.md','review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/inputs/review-SKILL.md']:
 b=(P/rel).read_bytes();contracts.append(dict(path=rel,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),blob=subprocess.check_output(['git','-C',str(P),'rev-parse','HEAD:'+rel]).decode().strip(),lines=len(b.splitlines()),read_status='FULL_READ',reader='/root/ui_navigation_audit'))
ids['contract_inputs']=contracts;ids['head_observed']='7478d8daf357d569ac12bea211b4b5f257861930';ids['head_scope']='合法报告后继；受审字节始终固定B8/R，不要求HEAD等于B8';write('identities.json',ids)
refpath=P/'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/world_topology_audit/refutation-ui001.json';b=refpath.read_bytes();ref=json.loads(b)
p=read('proposals.json');p['records'][0]['status']='INDEPENDENT_REFUTATION_COMPLETE_ROOT_CLASSIFICATION_PENDING';p['records'][0]['independent_decision']={'reader':'/root/world_topology_audit','path':str(refpath.relative_to(P)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'recommendation':ref['independent_recommendation'],'source_fact':'CONFIRMED','reason':ref['reason'],'root_final_decision':None};p['records'][0]['proposer_after_refutation']='接受实际反证对阶段scope的合理限缩：不再坚持该候选必须为required，保留可选澄清提案和最小事实；不撤销原提案/反证历史。';p['updated_utc']=NOW;write('proposals.json',p)
intf=read('interfaces.json');intf['accepted_external_source_scope'].append({'reader':'/root/pbs_world_record_audit','scope':'PBS TownMap36行/27点及default MapSize记录→RegionMap指定字段读取；phone record facts并非本导航wholePhone接收','receipt':'实际collaboration双向消息：对方已读本UI-I14/04限定并接收RegionMap全356 source；本任务仅接收其TownMap producer记录事实','evidence_path':'tasks/pbs_world_record_audit/records.json; field-contracts.json; forward.json; reverse.json','not_accepted':'全WP63、Phone UI、Summary或其它屏幕内部'});intf['records'][-2]['status']='INDEPENDENT_REFUTATION_COMPLETE_ROOT_DECISION_PENDING';write('interfaces.json',intf)
# Recover test rows by explicit NV/CH/TC families; the entire catalog was read separately.
cat='deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md';lines=(P/cat).read_text().splitlines();f=read('forward.json')['facts'];vectors=[]
for n,line in enumerate(lines,1):
 if not (135<=n<=173 or 179<=n<=183 or 189<=n<=196):continue
 cells=line.split('|')
 if len(cells)<5:continue
 k=cells[1].strip();family='NV' if 135<=n<=173 else 'CH' if 179<=n<=183 else 'TC';links=sorted({z['id'] for z in f if any(q['line']==n for q in z.get('test_routing_locations',[]))})
 vectors.append({'id':family+'-'+k,'path':cat,'line':n,'input_and_premise':cells[2].strip(),'expected':cells[3].strip(),'source_fact_ids':links,'status':'STATIC_EXPECTATION_READ_AND_NAVIGATION_SOURCE_RECONCILED; ATOMIC_CHILD_LINK_CLOSURE_NOT_CLAIMED','execution':'NOT_EXECUTED','reader':'/root/ui_navigation_audit','qualifier':'只限给定合法依赖/明确有限输入前提；命令请求不是实际媒体/宿主/存档观察。'})
write('vectors.json',{'schema':'r8-ui-navigation-vectors-v1','count':len(vectors),'families':dict(collections.Counter(x['id'].split('-')[0] for x in vectors)),'records':vectors,'all_ui_catalog_vectors_source_accepted':False})
# All 1127 line units remain independently visible, including the unaccepted catalog clauses.
rev=read('reverse.json');status=collections.Counter(x['disposition'] for x in rev['records'])
limits=[{'id':'UI-L01','kind':'MATERIAL_AND_HOST_LIMIT','scope':'真实标题/背景/字体/图集/音频及物理输入、窗口缩放/显示/音频最终输出','reason':'此任务未取得完整工程和目标宿主运行；已经读到的脚本仍有其静态信用。','execution':'NOT_EXECUTED'}, {'id':'UI-L02','kind':'MATERIAL_CALLER_LIMIT','scope':'Controls、PC/玩家PC真实地图事件与Demo调用点','reason':'脚本检索未定位Controls实际caller；缺工程事件材料不推其不存在。'}, {'id':'UI-G01','kind':'READING_AND_RECEPTION_GAP_NOT_LIMIT','scope':'完整Party/Summary/Storage/Pokedex/Bag/ItemStorage/Marts/MysteryGift/Mail/Phone/Jukebox/Hall/Purify UI内部','reason':'只有具名局部receiver/controlflow或额外Credits/Pokegear/RegionMap完整源读；其它内部没有实际全文接收。','owner':'/root待派实际UI shard'}, {'id':'UI-G02','kind':'FORMAL_ATOMIC_MAPPING_GAP_NOT_LIMIT','scope':'全部复合formal clause精确子断言分母与其逐断言反向链接','reason':'1127只是全文非空非标题行底表；320是具名source语义断言，不能冒充formal原子条款总数；183行已精确链接有限断言，但其它子断言仍须关闭。','owner':'/root/ui_navigation_audit已提交当前实读贡献；后继实际reader继续精确分解'}, {'id':'UI-G03','kind':'CURRENT_QUALIFICATION_RECEPTION_GAP','scope':'WP65正文引用历史批准、B16、U01–U10/G01–G12/AX01–AX20等现行资格字节','reason':'已读当前formal语句，但本导航子任务没有重新恢复全部历史原记录/当前binding，不能授予其引用独立历史资格。','owner':'/root历史实际reader'}]
write('boundaries.json',{'schema':'r8-ui-navigation-boundaries-v1','updated_utc':NOW,'records':limits,'unread_reference_ranges_in':'reading-ledger.json','no_local_whole_ui_pass':True})
write('execution.json',{'schema':'r8-ui-navigation-execution-v1','reference_observations':0,'independent_behaviour_models':0,'host_or_demo_runs':0,'native_media_runs':0,'real_save_runs':0,'evidence_levels_used':['SOURCE_STATIC','DERIVED_VECTOR','TOOL_VALIDATION'],'not_executed':'全部行为向量未执行。工具只读Git/文件、行定位、哈希、枚举和生成审计JSON；不得把Python退出0当参考行为测试。','tool_failures_retained':'平台工具流包含少量路径猜测读取失败、一次本地映射脚本IndexError及后继断言/类型匹配失败，均在写集内修正重跑。它们不是参考行为观察，不转成运行成功；最终validation.json记录修正后机械检查。','platform_log_path':'UNVERIFIED；实际tool stream为当前context平台记录，未声称能公开远端读回私有流。','update_started':False})
counts=read('counts.json');counts['exact_formal_factlink_line_units']=sum(bool(x['linked_source_fact_ids']) for x in rev['records']);counts['reverse_dispositions']=dict(status);counts['navigation_vector_rows']=len(vectors);counts['source_identity_records']=len(ids['inputs']);write('counts.json',counts)
progress=read('progress.json');progress.update(updated_utc=NOW,status='COMPLETED_BOUNDED_CONTRIBUTION_WITH_EXPLICIT_OPEN_COVERAGE',stage='LOCAL_REPORT_FROZEN_FOR_PARENT_RECEPTION',start_utc='UNVERIFIED',first_verified_utc='2026-10-16T02:58:55Z',completed_utc=NOW,counts=counts,independent_refutation={'reviewer':'/root/world_topology_audit','status':'COMPLETE; ROOT_DECISION_PENDING','proposal':'GR8-UI-001','recommendation':'NO_REQUIRED_REVISION_OR_OPTIONAL_CLARIFICATION'},remaining_blockers=['UI-G01','UI-G02','UI-G03'],whole_ui_pass=False,update_started=False);write('progress.json',progress)
text=f'''# R8 UI navigation bounded source review

实际context `/root/ui_navigation_audit`；请求 `gpt-6.1-sol / ultra / default 普速 / Fast off`，实际 model/effort/tier/speed/Fast、opaque平台ID均 **UNVERIFIED**。首个可核UTC为2026-10-16 02:58:55；平台启动精确时点未知。独占写集为本目录。未改正式规格/参考/公共台账，未commit/push/安装/spawn，**UPDATE_NOT_STARTED**。

固定B8 `fd1df570cad987dc3852a3b958f03916e317f7fe` / tree `751dfde81048c81390f89a65ca1d1a565ba8e1ca` / formal `f292698cdd4a8e725525a9be6dc34b75faaf151e`；R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。所读R/正式文件均逐字节等于固定blob，身份见identities.json。HEAD7478d8da为合法报告后继，不被用作当前受审基线。

本context全文读WP65主合同263行、Controls61行、TrainerCard59行及共享UI测试目录1111行，共4正式文件1494行。Prompt36653bytes SHA25663944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b、根AGENTS和3598bytes review-SKILL已全文读。SKILL的适用场景是最终态修订，本任务保留审计记录，没有借它修正文。

参考全文实读37文件8374行，另24文件只审具名range及完整入口/返回单元。新增完整Pokegear、RegionMap、Credits、PictureEx、EventScene/Event/handler、SaveData及注册、Settings/PokemonSystem/音频系统等；Party、Storage、Bag、MysteryGift、Purify、Hall等保持真实局部边界。reading-ledger.json逐文件给连续读区间、未读区间和结构单元定位。检索和脚本没有获得语义阅读信用；初次组合输出截断处已重读，MessageConfig仅具名重读部分有信用。

已整理320个手工具名source语义断言，forward.json逐条给固定source身份引用、前提、消费者及精确formal位置。reverse.json保留1127个非空非标题行定位单元；其中183行有明确有限断言链接。这1127行**不是最终formal原子分母**，320 source断言也不是formal条款数；复合条款剩余子断言、共享测试目录其它UI条款和部分当前历史资格尚未逐项接收。因此此交付是实读证据与有限事实贡献，**不是完整导航原子闭合、整UI或全系统PASS**。不得把“已读全test catalog”解释成全部向量已反查源码。

52个导航向量（NV39/CH5/TC8）正文、前提与静态预期已完整读并同导航source核对，见vectors.json；每行下的全部细化子断言精确链接仍未声称最终闭合。其它测试系列全文已读但领域source接收待实际owner。接口16链见interfaces.json：菜单可见与执行门、请求生产与消费、四会话组合、父子屏返回、设置即时/结束应用/语言直写、保存/退出与布尔结果、快捷候选/游标/道具消费、绝对行走预览相位和相对标题图片过程时钟分别记录。

唯一提案GR8-UI-001的地图名称首次读取前缀成立；实际独立非提案者 `/root/world_topology_audit` 全读保存与完整名称getter链后反证：WP65§4.1 L90已保留确认前修改，L88“无副作用”可合理限于信息窗已建好后的No分支，故不支持仅凭字面强解释定必修。提案者接受这一scope反证，不再坚持required；推荐optional澄清或no-required由/root最终裁定。完整原提案、最小例、普通对照、保留scope、A1–A4和反证身份/hash均在proposals.json。没有把该提案重复记作KER001/002/003；它们的原独立反证精确scope由root保持。本context未审其全部其它clauses，不借旧结果扩充信用。

额外反例搜索保留：紧急保存无玩家提前返回未恢复旧场景；Ready负索引未夹下界及窗口索引→共享数组写入先后；默认handler返回true前自行关闭菜单。这些作为明确source facet列入forward，不擅自升级为新required。现有正文的早退/合法输入/默认注册scope可合理限制它们；需要更宽规范时仍须另作具名反证。

正常退出只对已读层可证：scene=nil使脚本场景循环结束；无效存档拒绝调用语言级exit。未观察宿主进程退出、窗口、像素、发声、物理输入或真实存档结果。全部行为向量 **NOT_EXECUTED**，新增行为执行0。真实素材/宿主缺口见UI-L01/L02；可读未读/未接收另列UI-G01/G02/G03，不能改标成材料limit。

可恢复入口：`identities.json`、`reading-ledger.json`、`forward.json`、`reverse.json`、`interfaces.json`、`vectors.json`、`proposals.json`、`boundaries.json`、`execution.json`、`counts.json`、`validation.json`与`progress.json`。后继审者应从未读range和无精确子断言接收的条款继续，不从本报告复制全UI批准。
'''
(O/'review.md').write_text(text)
# Integrity validation only; no semantic closure conferred.
by_path={x['path']:x for x in ids['inputs']}; errors=[];factids={x['id'] for x in f}
for x in f:
 for s in x['source']:
  a=by_path[s['path']]
  if not 1<=s['line_start']<=s['line_end']<=a['lines']:errors.append(['range',x['id'],s])
  if not any(lo<=s['line_start'] and hi>=s['line_end'] for lo,hi in a['read_ranges']):errors.append(['unread',x['id'],s])
 for s in x['spec_locations']:
  if not 1<=s['line']<=by_path[s['path']]['lines']:errors.append(['formal_range',x['id'],s])
for c in rev['records']:
 for q in c['linked_source_fact_ids']:
  if q not in factids:errors.append(['missing_fact',q])
if len(by_path)!=len(ids['inputs']):errors.append(['duplicate_identity'])
if len(factids)!=len(f):errors.append(['duplicate_factid'])
write('validation.json',{'schema':'r8-ui-navigation-integrity-validation-v1','updated_utc':NOW,'status':'PASS' if not errors else 'FAIL','errors':errors,'checks':['fixed source/spec disk equals blob','unique identity paths','unique source fact IDs','every source locator lies in credited read interval','every formal locator in bound file','reverse fact IDs resolvable','39NV+5CH+8TC row inventory'],'semantic_approval':False,'behaviour_execution':False})
# Manifest excludes itself to avoid recursive hash; no future git identity.
manifest=[]
for p in sorted(O.iterdir()):
 if p.is_file() and p.name!='artifact-manifest.json':
  b=p.read_bytes();manifest.append({'path':str(p.relative_to(P)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob_if_added':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()})
write('artifact-manifest.json',{'schema':'r8-ui-navigation-artifacts-v1','frozen_utc':NOW,'files':manifest,'self_excluded':True,'publication_commit':'PARENT_TO_BIND','semantic_scope':'bounded contribution only; formal atomic closure open','update_started':False})
print(json.dumps({'counts':counts,'validation_errors':errors,'manifest_sha256':hashlib.sha256((O/'artifact-manifest.json').read_bytes()).hexdigest()},ensure_ascii=False))
