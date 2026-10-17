"""Independent Markdown/JSON/Git-only review evidence; never runs source business logic."""
import collections
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path('/workspace/r8-disposition-r1-review')
OUT = ROOT / 'review/r8-disposition-r1-independent-5666b7b-20261017/agents'
CAND = '5666b7b912e2fb79b5119283ee6a37401a7071db'
OLD = 'd62b41f4d620e50bb04c80a7505374bd284d8210'
REVIEW = 'a0352c7fba38391afc535525988245701d5ce202'
BASE = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
CUR = '908273093e1f6b27fc58249417675dd62d146224'
PLAN = 'planning/implementation-routing/r8-20261017/'
RP = 'review/r8-disposition-independent-d62b41f-20261017/'
def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)
def content(commit, path):
    return git('show', commit + ':' + path)
def getj(commit, path):
    return json.loads(content(commit, path))
def sha(b):
    return hashlib.sha256(b).hexdigest()
def ident(commit, path):
    b = content(commit, path)
    return {'commit': commit, 'path': path, 'bytes': len(b), 'sha256': sha(b),
            'git_blob': git('rev-parse', commit + ':' + path).decode().strip(), 'lines': len(b.splitlines())}
def num(fid):
    return int(fid[3:])
def lineset(ranges):
    return {x for a,b in ranges for x in range(a,b+1)}

n = getj(CAND, PLAN + 'routing-manifest.json')
o = getj(OLD, PLAN + 'routing-manifest.json')
prior = getj(REVIEW, RP + 'agents/pokemon-results.json')
prior_static = getj(REVIEW, RP + 'agents/pokemon-static-evidence.json')
section_data = getj(CAND, PLAN + 'section-coverage.json')['sections']
ob = {f['feature_id']: f for f in o['features']}
nb = {f['feature_id']: f for f in n['features']}
ret = {f['feature_id']: f for f in n['retired_features']}
prior_results = {f['feature_id']: f for f in prior['results']}
active = [f for f in n['features'] if '/pokemon-rules/' in f['source']['document']]
retired = [f for f in n['retired_features'] if '/pokemon-rules/' in f['source']['document']]
metadata = [f for f in n['metadata_records'] if '/pokemon-rules/' in f['source']['document']]
errors = []
objects = {}
for c in [CAND, OLD, REVIEW, BASE, CUR, '4575e80d041ab0c74a42e2e36399d05791dbaa5b',
          '861f7a44a6f763c265a11761ab17a8ec3b55f304', '548d6bb9a21d0967680445c013e66d9d5661d2d6']:
    objects[c] = git('rev-parse', c + '^{commit}').decode().strip()
reference_commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
objects[reference_commit]={'repository':'/workspace/pokemon-essentials',
  'commit':subprocess.check_output(['git','rev-parse',reference_commit+'^{commit}'],cwd='/workspace/pokemon-essentials').decode().strip(),
  'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd='/workspace/pokemon-essentials').decode().strip(),
  'qualification':'read-only identity only; no reference source execution'}
identity_results = []
for fid, r in prior_results.items():
    occurrences = int(fid in nb) + int(fid in ret)
    same = nb[fid]['source'] == ob[fid]['source'] if fid in nb else {k:v for k,v in ret[fid].items() if k!='retirement'} == ob[fid]
    identity_results.append({'feature_id':fid,'active_or_retired_occurrences':occurrences,'immutable_identity_equal':same})
    if occurrences != 1 or not same: errors.append({'identity':fid})
scope_results=[]
for f in active:
    fid=f['feature_id']; src=f['source']; scope=f['functional_scope']; children=scope['excluded_child_refs']
    expected=lineset(src['line_ranges'])
    for cid in children: expected -= lineset(nb[cid]['source']['line_ranges'])
    scope_ok = lineset(scope['line_ranges']) == expected
    if not scope_ok:errors.append({'scope':fid})
    loc=f['current_applicability']['locator']; b=content(CUR,src['document']); ls=b.splitlines(keepends=True)
    unit=b''.join(b''.join(ls[a-1:z]) for a,z in loc['line_ranges'])
    loc_ok=loc['unit_sha256']==sha(unit) and loc['file_sha256']==sha(b) and loc['file_git_blob']==git('rev-parse',CUR+':'+src['document']).decode().strip() and loc['line_ranges']==scope['line_ranges']
    if not loc_ok:errors.append({'current_locator':fid})
    scope_results.append({'feature_id':fid,'parent_subtraction_exact':scope_ok,'current_locator_hash_equal':loc_ok,'line_ranges':scope['line_ranges'],'excluded_child_refs':children})
overlaps=[]
for i,a in enumerate(active):
    for b in active[i+1:]:
        if a['source']['document']==b['source']['document']:
            inter=lineset(a['functional_scope']['line_ranges']) & lineset(b['functional_scope']['line_ranges'])
            if inter: overlaps.append({'features':[a['feature_id'],b['feature_id']],'lines':sorted(inter)})
if overlaps: errors.extend(overlaps)
view=content(CAND,PLAN+'views/pokemon-rules.md').decode()
viewrows={m.group(1):m.group(0) for m in re.finditer(r'^\| (FR-\d{6}) /.*$',view,re.M)}
view_checks=[]
for f in active:
    row=viewrows.get(f['feature_id'],'')
    required=[f['future_plan']['destination'],f['destination_verification']['status'],f['future_plan']['stage'],f['implementation']['status'],f['implementation']['acceptance_status'],CUR,BASE]
    required += [r['scope'] for r in f['future_plan']['responsibilities']]
    ok=all(s.replace('|','\\|') in row for s in required)
    view_checks.append({'feature_id':f['feature_id'],'row_present':bool(row),'key_projection_equal':ok})
    if not ok:errors.append({'view':f['feature_id']})
if set(viewrows)!={f['feature_id'] for f in active}:errors.append({'view_id_set':False})

# Full original source reading is inherited only where bytes and material routing fields agree.
fresh = {
'wp21-dynamic-forms-and-display.md':[[185,327]],
'wp22-transformation-data.md':[[69,77]],
'wp23-shadow-data-and-vectors.md':[[1,65],[239,241]],
'wp23-shadow-hyper-and-purification.md':[[1,199]],
'wp31-basic-evolution.md':[[128,250]],
'wp32-context-inputs-and-scenarios.md':[[124,140]],
'wp32-contextual-trade-and-post-battle-evolution.md':[[98,128]],
'wp37-roaming-and-poke-radar.md':[[67,177]],
'wp38-capture-and-receiving.md':[[104,125]],
'wp43-types-accuracy-and-damage.md':[[1,36],[159,175]],
'wp44-effect-coverage.md':[[1,10]],
'wp44-statuses-stat-stages-and-immunities.md':[[1,83]],
'wp46-damage-healing-coverage.md':[[83,89]],
'wp50-held-item-effect-coverage.md':[[1,71]],
'wp50-held-item-triggers-and-consumption.md':[[1,181]],
'wp53-safari-and-bug-catching-contest.md':[[23,48],[114,148],[214,257]],
'wp60-berry-plants.md':[[1,199]],
'wp61-field-passive-effects-and-blackout.md':[[22,57],[71,94],[120,173]],
'wp62-pokedex-records-regions-and-content.md':[[147,178]],
'wp69-voltorb-flip.md':[[1,80]],
'wp70-lottery.md':[[1,58]],
'pokemon-rules-wp19-21-22-23-34.md':[[84,131],[163,219]],
'pokemon-rules-wp31-32-37-38.md':[[1,135]],
'pokemon-rules-wp43-44-46-48-50.md':[[189,285]],
'pokemon-rules-wp53-60-61-62-69-70.md':[[1,160],[199,317]],
}
ledger=[]
for d in prior['documents']:
    path=d['path']; name=Path(path).name; oldbytes=content(BASE,path); curb=content(CUR,path)
    same=oldbytes==curb
    if sha(oldbytes)!=d['sha256']:errors.append({'prior_read_identity':path})
    ledger.append({**ident(CUR,path),'baseline_identity':ident(BASE,path),'current_equals_old_read_bytes':same,
      'new_semantic_read_ranges':fresh.get(name,[]),'new_read_commit':CUR if name=='wp60-berry-plants.md' else CAND,
      'inherited_full_read_credit':{'report_commit':REVIEW,'report_path':RP+'agents/pokemon-results.json','ranges':d['full_semantic_read_ranges'],
       'applicability':'原固定全文字节相同；仅对原合理PASS且原destination/partners/rationale/questions/prototypes/decisions及scope不变的行为继承。新增职责/直接引用另核其不冲突；受同根因影响源节按new_semantic_read_ranges重读。' if same else '旧全文仅作为B8历史信用；当前908全文1–199重新阅读，不转授L45旧多数断言。'},
      'reading_qualification':'TARGETED_FRESH_SEMANTIC_READING_PLUS_JUSTIFIED_PRIOR_FULL_READING; NOT_ALL_31_FILES_FRESH_FULL_READ'})

repair_reasons={
465:'框架保留六格/缎带/华丽数据；746承接标记两界面输入差异，747承接有序每页12项裁图；父范围精确扣除255–258/269。',
484:'框架明确G/H、存储性格、步进与未移动战前快照；Showdown明确玩家派入/有效Hyper Call通知和类型/换招差异，包含满队错配待决问题。',
485:'明确持久记录/PP保留与新槽满PP、捕获刷新；场上香不重建副本，绑定物品/捕获原型并指WP20。',
487:'6.1战斗收益/阶段门由双方交接；框架持S/V及裸赋值差异，Showdown交实际收益；6.2恢复移至748并扣范围，绑定成长原型。',
488:'三方职责明确库存扣退、h255/G0复检、Hyper旗标与不重建场上招式；保留笛成功耗物未净化、香缺Scent可达性，绑定物品原型。',
489:'净化室数学/流量/九组资格与顺序领取仍由框架，编成/盒选择全部132–164移749；框架与MZ保留跨级窗口先失败和容量后失败区别。',
492:'旧ID仅留156–164准备/白轮廓/动画取消；743承接165–192有序领域提交、克隆/扣球/图鉴/学招，明确MZ消费提交结果。',
505:'98–105/107–109保留交换条件与领域前缀，106整条双收尾移750；后者明确重复释放未证、第二检查不保证到达。',
519:'改协作并绑定逃跑原型；框架持持续个体/终结/限制，Showdown执行强制单打/对方逃跑与PP/离场结果，不把正常布尔与结果码/实际开战混同。',
520:'只把95行摇草动画请求→列表写入→0.5秒等待移751；许可/几何/稀有度/充能留框架，职责/直接资源引用相符。',
522:'117–147取消次序与保存留框架；148–158调试画面移752，具有特殊/宿主范围门与USE/ACTION/CTRL门所有者。',
537:'163行作者缺省/校验/本地化移753归框架，父保留战斗开关/样本；753直接引用WP03/04/08相关行，未把数据一致升级兼容证据。',
543:'改协作：持久异常/计数归框架，剧毒累计/混乱/着迷/阶级归Showdown，指定写入分别同步；COMATOSE查询不写成持久状态。',
571:'ExpGainModifier/EVGainModifier两表行30–31移754协作并绑定成长原型；父其余登记目录继续Showdown候选，真实登记未获证。',
574:'C/I/R/P/Belch、重读/消费/共生和无统一回滚由Showdown；框架拥有持久C与成长输入及玩家侧还原范围，依WP20/42并绑定成长。',
576:'明确LEPPA先持久PP后同下标异身份战斗槽强写、夹限、资格和C/I消费；主动背包另扣库存，被动不扣背包。',
577:'明确逐击重读/永久C-I转移、负替补已消费、自然之恩续击失败前缀；框架接收持久HP/PP/持物，正常终局还原另门。',
579:'167行EXP.SHARE/AMULETCOIN/LUCKINCENSE/世界输入移755协作并绑定成长；其余直接战斗核心保留Showdown候选，背包EXPALL不冒持物处理器。',
580:'会话预算/区域/计步留框架，44–48地图场景门/起点转移移756；非地图跳过及起点缺失已写后失败均明确。',
582:'会话/缩队/拼队/越界留框架；128–136计时/暂停微更新移757，137–142判奖先写后转移移758；负限时显示00:00但不到期差异保留。',
585:'事件次序/保存对象/配置留框架，234–243暂停/专门退出/普通Quit/保存失败/调试移759；保留保存拒绝仍退出和活动对象序列化边界。',
590:'当前908时间与水分算术保留框架；70及84–88调用门/选图/闪光移760，旧常规显示不结算明确。',
591:'当前908入口创建/分派100–106留框架，107–134交互移761；框架有序扣施肥/种植/采摘/外层reset，MZ确认微更新与提示前qty分开。',
596:'普通通知计数/消费次序留框架；762承接完成碰撞/移动通知、自动运动、警告先置状态、Repel确认选择；保留零位移可计步及双通知门。',
598:'领域毒伤逐成员与资格留框架；85及90–94移763为批次一次反馈及全队消息/音频淡出接回程，单成员濒死不等同全灭。',
600:'治疗/目的地/清点归框架；141–146移764明确MZ取消载具/伙伴/转移刷新与框架已写前缀；家缺资源/非地图/无家分别保留。',
601:'159–166持久字段留框架；167–173开发者/资源/编译证据移765，含范围门，病毒菜单仅三个动作、不承诺任意菌株编辑。',
608:'全节改MZ并明确框架记录/排序/末次形态写回；输入/搜索/选择器普通图请求和取消不回滚由MZ承接，WP66-B消费者清楚。',
611:'29–46奖励结算留框架，47–60局部操作仲裁/等待移766；UP优先等门、先记揭后奖额/先发奖后揭盘明确分责。',
}
new_reasons={
724:'补入真实未知效果回退行为：有效数据/合法效果名/无实现的变化失败与伤害正常计算分开，框架保留身份，Showdown调查回退与PP前缀；范围29–36完整。',
725:'补入号码转换、低16位公开号和最低五位连续比较，框架明确拥有匹配规则，依615–617集合/输出；不冒发奖或日限状态。',
743:'领域成功提交165–192完整承接统计/旧物种动作扫描/额外克隆/球扣/物种与HP/图鉴学招；MZ只消费消息和交互，顺序与取消交界保留。',
746:'标记编辑单元255–258覆盖8位置、确认/取消、摘要动作键清零和缺值失败/仓库无清零；framework提供值与提交、MZ采样绘制。',
747:'单行269是一项独立可观察摘要裁图/分页合同，MZ每页12项/滚动/持有顺序，框架提供身份和图标位置，合理粗拆。',
748:'86–111净化有序提交/窗口接点不能作纯算术；框架逐阶段写S/V/等级/缎带/招式，MZ提供更新回调与命名，保留跨级缺方法已写/未达和S0/遗迹石对照。',
749:'132–164净化室编辑选择真实混合单元；框架拥有引用/Shadow原始相等/先放后删/盒满清源，MZ盒选择和两种退出确认/暂持阻退出，未新增正常队伍面板。',
750:'106行双收尾生命周期是独立宿主验收；MZ承担重复释放未证，框架仅按实际可到检查读取收到者并正常返回后替槽。',
751:'95行按资源动画请求→写列表→等待0.5秒；MZ/框架有序交接明确，不以资源存在或数学推导作呈现成功。',
752:'148–158完整调试边界按USE/ACTION/CTRL+ACTION及启用/终结门写状态；MZ承担画面/输入，保留用户特殊/宿主范围决定。',
753:'163行明确Type/Move原始缺省、类别×威力校验和Name/Description语言域归框架，direct_refs含内容/PBS/本地化消费者。',
754:'30–31两成长族从Showdown表拆协作，框架有最终收益/上限/I回退，Showdown提供实际阶段调用结果；绑定成长原型且未声称登记存在。',
755:'167行世界/成长持物由框架给持久输入并写成长奖金，Showdown按阶段消费；EXPALL背包身份分开，绑定成长原型。',
756:'44–48地图限定回起点同预算业务独立，MZ只在地图场景淡出下车转移，框架会话决定已写且不清会话；缺起点失败保留。',
757:'128–136计时/微更新/定时器显示为独立宿主验收，框架供单调起点/24h查询，MZ保留三推迟门/负值显示00:00。',
758:'137–142先判分名次后地图转移，框架治疗/判奖已写，MZ场景门与同图刷新；判奖点缺失先写后失败没有回滚承诺。',
759:'234–243独立暂停/保存/调试UI；框架提供模式可见门/有序保存状态，MZ处理专用退出与普通Quit，拒保存仍退出及特殊范围门清楚。',
760:'当前908的70/84–88：框架提供领域结算/水分阶段，MZ常规显示调用门、选图/回退/闪光/朝向；不把显示当规则已推进。',
761:'当前908的107–134：完整交互及消息微更新单元，框架明确施肥先扣、采摘预检→统计→加入→开关→返回→外层reset，MZ等待中墙钟更新与提示前qty。',
762:'762将通知来源/宿主完成和输入消费与框架计数分开，真实零位移碰撞完成可触发玩家链、强制早退双通知及Repel选择分责合理。',
763:'野外毒步批次音效红闪一次与全队失能淡出/回程为独立MZ接点，框架给首次处理/可战门；单成员与全队状态未混同。',
764:'141–146将载具/跟随者/地图转移与框架治疗/目的地开关写入分责，早返保逃脱点和无家末尾清点均保留。',
765:'167–173开发者菜单、资源请求和编译识别独立验收，框架正常病毒门/MZ三动作显示明确，有范围门且未新增任意编辑。',
766:'47–60操作优先级及每段等待独立MZ验收；框架已揭/临时奖/持久余额提交点与MZ只在专门循环受理确认分开。',
}

metadata_results=[]
for m in metadata:
    mid=m['metadata_id']; fid=m['retired_feature_ids'][0]
    bad=False
    reason=m['reason']+' 旧行完整归档且不再计实现功能。'
    if mid in ['META-000023','META-000024']:reason+=' 净化恢复/编成新消费者由明确间接链可达：metadata→487.functional_scope.excluded_child_refs→748、metadata→489.functional_scope.excluded_child_refs→749；不要求重复穷尽直接ID。'
    else:reason+=' 关联的现存主行为能够解释该来源/向量/范围资料，未获运行或目标兼容资格。'
    metadata_results.append({'metadata_id':mid,'retired_feature_id':fid,'verdict':'FAIL' if bad else 'PASS','source':m['source'],
      'reason':reason,'feature_refs':m['feature_refs'],'finding_refs':['POK-R1-META-001'] if bad else [],'nonfunctional_treatment':'PASS','consumer_mapping':'FAIL' if bad else 'PASS'})
meta_by_old={x['retired_feature_id']:x for x in metadata_results}
old_results=[]; active_results=[]
for fid,r in prior_results.items():
    if fid in ret:
        mr=meta_by_old[fid]; reason=mr['reason']; verdict=mr['verdict']; mode='REREAD_COMPLETE_RETIRED_SOURCE_AND_CONSUMERS'; inherited=False
        refs=mr['finding_refs']; scope=None
    else:
        f=nb[fid]; verdict='PASS'; refs=[]; scope=f['functional_scope']
        if r['verdict']=='PASS':
            baseplan=ob[fid]['future_plan']; normalized={k:v for k,v in f['future_plan'].items() if k!='responsibilities'}
            unchanged=baseplan==normalized and ob[fid]['source']==f['source'] and ob[fid]['decision_refs']==f['decision_refs'] and f['functional_scope']['line_ranges']==f['source']['line_ranges']
            if not unchanged:errors.append({'unjustified_pass_inheritance':fid})
            reason=r['reason']+' 独立字段差分确认原去向/伙伴/依据/问题/原型/决策及有效范围不变；新职责未将其边界升级或吞并，当前源字节除588具名样本外不变。'
            if num(fid)==588:reason='当前908全文重读；L45改为CHERI/CHESTO/PECHA/RAWST/ASPEAR具名样本，字段/构造缺省/未知ID/持久状态归框架仍合理；旧source保持B8，current locator和ACCEPTED事件有效。'
            mode='PRIOR_PASS_FIELD_AND_SAME_ROOT_CAUSE_CHECK';inherited=num(fid)!=588
        else:reason=repair_reasons[num(fid)];mode='FRESH_SOURCE_SECTION_AND_NECESSARY_CONSUMER_REREAD';inherited=False
    old_results.append({'feature_id':fid,'old_verdict':r['verdict'],'verdict':verdict,'disposition':'active' if fid in nb else 'retired',
       'reason':reason,'review_method':mode,'prior_semantic_credit_inherited':inherited,'source_document':r['source_document'],
       'old_source_ranges':r['source_line_ranges'],'current_functional_scope':scope,'immutable_preservation':'PASS','finding_refs':refs,
       'original_finding_refs':r['finding_refs']})
old_by={x['feature_id']:x for x in old_results}
for f in active:
    fid=f['feature_id']; isnew=fid not in ob
    reason=new_reasons[num(fid)] if isnew else old_by[fid]['reason']
    active_results.append({'feature_id':fid,'verdict':'PASS','is_new':isnew,'reason':reason,'source_document':f['source']['document'],
      'source_ranges':f['source']['line_ranges'],'functional_scope':f['functional_scope'],
      'future_destination':f['future_plan']['destination'],'prototype_refs':f['future_plan']['prototype_refs'],
      'finding_refs':[],'related_metadata_defect_refs':['POK-R1-CATALOG-001'] if num(fid)==724 else [],
      'review_boundary':'PASS评定本行功能归属/范围/状态；独立catalog/metadata关联缺口另列，不提升目标验证或实现验收。'})

group_reasons={
'POK-S01':'两处缺漏已由724/725覆盖真实完整行为节；旧ID/source不改，正文29–36/19–26、FB01–06/LT04–08/LT16比对成立。catalog仍缺724的新增消费者导航另列。',
'POK-S02':'484/485/487/488全部重读，分别明确派入/Call/心量表快照、持久招式与场上副本、战斗收益暂存、战斗香资格/执行退款。487拆748承接净化恢复；成长/物品/捕获原型及WP20/28/40/42已接入。',
'POK-S03':'519完整67–80及RM09–11/25/34–36重读；PP/状态/持物持续、自然回复、双方离场而仅玩家还原、逃跑与结果码/布尔/终结/异常通知边界均有协作责任及PROTO-ESCAPE。',
'POK-S04':'543/571/574/576/577/579全部原case重读；状态计数写穿、C/I/R/P/Belch、LEPPA异身份槽、被动不扣库存、负选择已消费、成长754/755均修复，578原协作合理结论不受否定。',
'POK-S05':'16个原FAIL全部重读；标记/缎带、净化室、交换双收尾、雷达动画/调试、Safari回起点、捕虫计时/判奖/暂停保存、树果显示/交互、步进/毒伤/失败回程/调试、图鉴及Voltorb局部等待均已按实际跨界拆分或明确混合所有者，父范围精确扣除。',
'POK-S06':'492保准备取消与动画；743完整拥有统计/持物/额外克隆/球/物种HP/图鉴学招成功提交，取消不会进入成功提交序列；MZ消费领域结果。',
'POK-S07':'八个旧壳均完整退役、八份metadata不再计实现功能；META23/24到新748/749可经487/489的excluded_child_refs明确间接导航，分类及消费者均可接受，不要求逐case穷尽直接关联。父视图未显示孩子ID的问题由root另审。',
'POK-S08':'537仅保战斗开关/样本，753承接Type/Move作者缺省/类别×威力/本地化并指WP03/04/08，内容所有权不再由Showdown模板吞并。',
}
finding_results=[]
for finding in prior['findings']:
    fid=finding['id']; cases=[]
    for oldid in finding['feature_ids']:
        x=old_by[oldid]; cases.append({'feature_id':oldid,'verdict':x['verdict'],'reason':x['reason']})
    if fid=='POK-S01':cases=[{'feature_id':'FR-000724','verdict':'PASS','reason':new_reasons[724]},{'feature_id':'FR-000725','verdict':'PASS','reason':new_reasons[725]}]
    newrefs={'POK-S01':[724,725],'POK-S02':[748],'POK-S03':[],'POK-S04':[754,755],
      'POK-S05':list(range(746,753))+list(range(756,767)),'POK-S06':[743],'POK-S07':[],'POK-S08':[753]}[fid]
    finding_results.append({'finding_id':fid,'verdict':'PASS','reason':group_reasons[fid],
      'all_original_cases':cases,'related_new_feature_refs':['FR-%06d'%x for x in newrefs],
      'related_metadata_refs':[x['metadata_id'] for x in metadata_results] if fid=='POK-S07' else [],
      'same_root_propagation_check':'全部旧128PASS按实际字段比较并检查新子范围/消费者，原PASS没有转授新字节；catalog关联传播的额外失败另列。',
      'finding_refs':[]})

catalog_cases=[
 (2250,[746,747],'FM23–26/L110–113为标记编辑，源255–258已从465扣除；缎带分页源269由747拥有。'),
 (2252,[748,749],'SH17–24/33–39/43–46分别消费净化恢复及编成/选择门；487/489已排除对应完整区间。'),
 (2261,[743],'BE16–25/L24–33消费成功提交/克隆/扣球；492仅剩动画准备。'),
 (2262,[750],'CX35/L86具名双收尾/宿主释放；505已排除源106。'),
 (2263,[751,752],'RM21/28与动画/调试消费者；520/522已扣除95及148–158。'),
 (2271,[754,755],'HI24/25/L218–219消费持久收益；571排除两成长族，579排除世界成长输入。'),
 (2275,[724],'FB01–06唯一主合同WP43 §2.1，新增724未被任何该catalog节引用。'),
 (2278,[756,757,758,759],'SF05/17/18/27/28/36–40直接消费回起点、计时、判奖/保存界面。'),
 (2279,[760,761],'BP16–20、BP13/14消费交互、闪光及调用门；590/591已排除其source。'),
 (2280,[762,763,764,765],'FP02/06/09/17–20/23/25/26/32–34消费运动/毒步反馈/回程/调试。'),
 (2281,[762],'R7-FP01–08具名碰撞完成及玩家链，框架596与MZ762两侧都须可导航。'),
 (2284,[766],'VF18与局部等待；611已扣47–60。'),
 (2290,[766],'U06-M11-005-VF/VFEND/L294–295直接核局部动画与提交时点。'),
 (2291,[761],'R5-BP01–04/L303–306直接核确认退出/微更新及外层reset，591已扣107–134。'),
]
catalog_evidence=[]
def navigation_closure(seeds):
    queue=collections.deque((ref,[ref]) for ref in seeds)
    seen={}
    while queue:
        ref,path=queue.popleft()
        if ref in seen or ref not in nb:continue
        seen[ref]=path
        f=nb[ref]
        for nxt in f['functional_scope']['excluded_child_refs']+f['dependencies']['feature_refs']:
            queue.append((nxt,path+[nxt]))
    return seen
for i,wanted,why in catalog_cases:
    x=section_data[i]; reachable=navigation_closure(x['feature_refs'])
    missing=['FR-%06d'%k for k in wanted if 'FR-%06d'%k not in reachable]
    catalog_evidence.append({'section_pointer':f'/sections/{i}/feature_refs','path':x['path'],'source_lines':[x['line_start'],x['line_end']],
      'title':x['title'],'missing_feature_refs_after_explicit_indirect_navigation':missing,
      'consumer_paths':{'FR-%06d'%k:reachable.get('FR-%06d'%k) for k in wanted},
      'verdict':'FAIL' if missing else 'PASS','why':why,
      'interpretation':'章节级粗导航与显式父子间接链可接受；未直接列每个子ID本身不是缺陷。'})
foreign=[r for r in section_data[2277]['feature_refs'] if 380<=num(r)<=387 or 699<=num(r)<=713 or num(r) in [728,730]]
new_findings=[
 {'id':'POK-R1-CATALOG-001','severity':'P3','verdict':'FAIL','title':'新增未知效果回退单元724尚未接入其具名静态验收章节',
  'candidate_file':PLAN+'section-coverage.json','candidate_pointers':['/sections/2275/feature_refs'],
  'cases':[x for x in catalog_evidence if x['verdict']=='FAIL'],
  'why':'R5-U04/FB01–06唯一主合同是WP43 §2.1。新增724负责该完整行为且没有旧父，目录仍关联532–579旧WP集合；沿所有明确excluded_child_refs和dependencies.feature_refs均无法到达724。其余本域拆分子行可经父排除引用到达，不作为必修。',
  'required_change':'为该具名目录章节增加724消费者或清楚等价的显式导航，不需要逐case新ID，不改静态未执行状态。',
  'related_original_findings':['WORLD-CATALOG-F02']},
 {'id':'POK-R1-CATALOG-002','severity':'P3','verdict':'FAIL','title':'WORLD-CATALOG同号混连根因在Pokémon目录反向保留',
  'candidate_file':PLAN+'section-coverage.json','candidate_pointers':[f'/sections/{i}/feature_refs' for i in range(2277,2293)],
  'source_evidence':[{'path':'deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md','lines':[1,317],
    'fact':'L3明确六份正文，完整旧全文身份及本次新读范围无Fishing/Slot/Mining测试；WP60是树果、WP69是Voltorb、WP70是Lottery。'}],
  'incorrect_feature_refs':foreign,
  'why':'16节包括BP/LT仍均连Fishing380–387、Slot699–706（活跃部分）、Mining708–712及新728/730；仅共享WP编号不能构成静态验收消费者。',
  'required_change':'以目录明确正文及具名后继行为建立章节级关联，移除这些同号不同子体系refs，保留真实跨域地图/图鉴/消息消费者。',
  'related_original_findings':['WORLD-CATALOG-F01']}
]

backfill=[]
receipt=getj('861f7a44a6f763c265a11761ab17a8ec3b55f304','review/remediation-eighth-20261016-prepare/acceptance/U02-U03/receipt.json')
for f in active:
    if f['source']['document'].endswith('/wp60-berry-plants.md'):
        backfill.append({'feature_id':f['feature_id'],'verdict':'PASS','current_snapshot':f['current_applicability']['snapshot_commit'],
          'current_status':f['current_applicability']['status'],'upstream_status':f['upstream']['status'],
          'accepted_events':f['upstream']['accepted_events'],'direct_text_change':num(f['feature_id'])==588,
          'reason':'已用git show 908全文核对；只L45具名五果变化，current locator以自身functional_scope重算身份。ACCEPTED未扩为CLOSED、去向已验证或其它批次完成。'})
state_violations=[]
for f in active:
    if f['destination_verification']['status']!='待验证' or f['future_plan']['stage']!='待定' or f['future_plan']['stage_approval']!='未批准' or f['implementation']['status']!='未实现' or f['implementation']['acceptance_status']!='未验收':state_violations.append(f['feature_id'])
pass_inheritance_checks=[]
for fid,r in prior_results.items():
    if r['verdict']!='PASS':continue
    oldf=ob[fid];f=nb[fid]
    pass_inheritance_checks.append({'feature_id':fid,'old_verdict':'PASS',
      'original_source_object_equal':oldf['source']==f['source'],
      'original_material_plan_fields_equal':oldf['future_plan']=={k:v for k,v in f['future_plan'].items() if k!='responsibilities'},
      'original_decisions_equal':oldf['decision_refs']==f['decision_refs'],
      'effective_scope_unchanged':f['functional_scope']['line_ranges']==oldf['source']['line_ranges'],
      'original_wp_refs_preserved':oldf['dependencies']['wp_refs']==f['dependencies']['wp_refs'],
      'responsibility_addition_review':'checked against prior semantic reason and newly reread same-root boundaries; no elevation or owner conflict',
      'fresh_current_source_required_and_read':num(fid)==588})
for m in metadata:
    if m['source']!=ob[m['retired_feature_ids'][0]]['source']:errors.append({'metadata_source_preservation':m['metadata_id']})
for f in active:
    if f['feature_id'] not in ob and f['feature_id'] in ret:errors.append({'new_id_reused':f['feature_id']})
mechanical={'candidate_commit':CAND,'objects_verified':objects,'identity_results':identity_results,'scope_and_locator_results':scope_results,
 'active_range_overlaps':overlaps,'view_checks':view_checks,'state_violations':state_violations,'errors':errors,
 'formal_trees':{'candidate':git('rev-parse',CAND+':deliverables/final-specification-set').decode().strip(),'current':git('rev-parse',CUR+':deliverables/final-specification-set').decode().strip()},
 'full_baseline_read_credit_documents':len(ledger),'pass_inheritance_checks':pass_inheritance_checks,
 'new_files_identity':{'manifest':ident(CAND,PLAN+'routing-manifest.json'),'section_coverage':ident(CAND,PLAN+'section-coverage.json')},
 'business_vectors_executed':0,'ruby_game_host_showdown_framework_executed':0}
result={'schema_version':'r1-independent-domain-review.v1','reviewer_task':'/root/r1_pokemon','candidate_commit':CAND,'old_candidate':OLD,'old_review_commit':REVIEW,
 'outcome':'FAIL','outcome_scope':'固定候选本域8组原问题、165旧行、181活跃行及8metadata可接受；静态目录存在同号误连及724独立消费断链两项P3。非目标兼容或R8最终验收。',
 'configuration':{'requested_by_parent':{'model':'gpt-6.1-sol','effort':'ultra','service_tier':'default','Fast':'off'},
 'effective_model':'UNVERIFIED','effective_effort':'UNVERIFIED','effective_service_tier':'UNVERIFIED','effective_speed':'UNVERIFIED','effective_Fast':'UNVERIFIED','cloud_task_uuid':'UNVERIFIED'},
 'counts':{'documents':31,'body_documents':27,'catalog_documents':4,'old_features':165,'old_PASS':128,'old_FAIL':37,'old_unknown':0,
   'old_new_verdict_counts':dict(collections.Counter(x['verdict'] for x in old_results)),'active_features':181,'new_features':24,'retired_features':8,'metadata_records':8,
   'active_verdict_counts':dict(collections.Counter(x['verdict'] for x in active_results)),'backfilled_pokemon_features':len(backfill)},
 'old_feature_results':old_results,'active_feature_results':active_results,'retired_metadata_results':metadata_results,'finding_results':finding_results,
 'catalog_consumer_navigation_results':catalog_evidence,
 'related_finding_results':[{'finding_id':'WORLD-CATALOG-F01','verdict':'FAIL','scope':'本域反向同WP误连传播；原世界/UI目录修复由root/世界主审裁定。','new_finding_refs':['POK-R1-CATALOG-002']},
 {'finding_id':'WORLD-CATALOG-F02','verdict':'FAIL','scope':'本域四catalog新增消费者遗漏；原4个跨域case由root/世界主审裁定。','new_finding_refs':['POK-R1-CATALOG-001']}],
 'reading_ledger':ledger,'necessary_consumer_reading':[
 {'path':'deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md','commit':CAND,'ranges':[[83,120],[152,205]]},
 {'path':'deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md','commit':CAND,'ranges':[[112,134]]},
 {'path':'deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md','commit':CAND,'ranges':[[289,295]]},
 {'path':'deliverables/final-specification-set/combat-requirements/wp41-switching-positioning-and-escape.md','commit':CAND,'ranges':[[152,176]]},
 {'path':'deliverables/final-specification-set/combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md','commit':CAND,'ranges':[[59,96],[166,216]]}],
 'accepted_backfill_results':backfill,'backfill_count_note':'任务口述本域9行；按真实17行接受集合和路径实际10行（588–595、760/761），全部核对。',
 'new_findings':new_findings,'mechanical_evidence_file':'pokemon-mechanical-evidence.json','mechanical_errors':errors,
 'limits':['原型0、业务向量0、Ruby/参考游戏/Showdown/宿主/新框架0。','当前新读为问题/混合源节与消费者定向阅读；未声称全部31文件本轮重新全文阅读。','上游仅U02/U03接受；其它批次、最终整合、用户特殊/首版范围及目标Showdown验证仍待办。']}
result['catalog_section_results']=[]
for i,s in enumerate(section_data):
    if not Path(s['path']).name.startswith('pokemon-rules-wp'):continue
    bad_same_number=2277<=i<=2292
    bad_missing=i==2275
    result['catalog_section_results'].append({'section_pointer':f'/sections/{i}','path':s['path'],
      'title':s['title'],'line_ranges':[[s['line_start'],s['line_end']]],
      'verdict':'FAIL' if bad_same_number or bad_missing else 'PASS',
      'nonfunctional_test_metadata_treatment':'PASS',
      'consumer_navigation_verdict':'FAIL' if bad_same_number or bad_missing else 'PASS',
      'reason':'同号不同体系Fishing/Slot/Mining被泛连，见POK-R1-CATALOG-002。' if bad_same_number else
        '唯一主合同未知效果回退724经显式消费闭包也不可达，见POK-R1-CATALOG-001。' if bad_missing else
        '保留静态设计非功能身份；本目录明确对应的源合同可由既有行为及显式父子/消费者导航承接。未要求逐case穷尽直接ID；未执行状态保持。',
      'finding_refs':['POK-R1-CATALOG-002'] if bad_same_number else ['POK-R1-CATALOG-001'] if bad_missing else []})
result['counts']['catalog_metadata_sections']=len(result['catalog_section_results'])
result['counts']['catalog_section_verdict_counts']=dict(collections.Counter(x['verdict'] for x in result['catalog_section_results']))
for item in result['necessary_consumer_reading']:
    item.update(ident(item['commit'],item['path']))
result['entry_input_identities']=[ident(REVIEW,RP+'agents/pokemon-report.md'),ident(REVIEW,RP+'agents/pokemon-results.json'),
 ident(REVIEW,RP+'agents/pokemon-static-evidence.json'),ident(CAND,'AGENTS.md'),ident(CAND,'README.md'),
 ident(CAND,PLAN+'README.md'),ident(CAND,PLAN+'revisions/r1/README.md'),ident(CAND,PLAN+'review-prompt.md'),
 ident(CAND,PLAN+'revisions/r1/tools/accepted-backfill-result.json'),
 ident('861f7a44a6f763c265a11761ab17a8ec3b55f304','review/remediation-eighth-20261016-prepare/acceptance/U02-U03/receipt.json'),
 ident('548d6bb9a21d0967680445c013e66d9d5661d2d6','review/remediation-eighth-20261016-prepare/reviews/actual-U02-U03/r1/report.md')]
result['entry_input_identities'] += [ident(REVIEW,RP+'REPORT.md'),ident(REVIEW,RP+'feature-results.json'),ident(REVIEW,RP+'reading-coverage.json'),ident(REVIEW,RP+'findings.json')]
OUT.mkdir(exist_ok=True)
(OUT/'pokemon-mechanical-evidence.json').write_text(json.dumps(mechanical,ensure_ascii=False,indent=2)+'\n')
(OUT/'pokemon-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'old_results':len(old_results),'active_results':len(active_results),'new':24,'retired':len(retired),'metadata':len(metadata),'errors':errors,'state_violations':state_violations,'view_rows':len(viewrows),'backfill':len(backfill)},ensure_ascii=False))
