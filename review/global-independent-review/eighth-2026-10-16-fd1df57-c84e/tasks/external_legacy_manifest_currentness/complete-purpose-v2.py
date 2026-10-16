"""Serialize reader-authored purpose judgments; no semantic credit from parsing.

The v1 builder is retained as historical method evidence and must not be rerun to
overwrite v2. This program writes only its adjacent task directory.
"""
import csv
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess

OUT=Path(__file__).resolve().parent
REPO=Path('/workspace/r8-external-legacy')
REF=Path('/workspace/pokemon-essentials')
ROOT='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
B8='fd1df570cad987dc3852a3b958f03916e317f7fe'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
C='30cfed0996003b6ebf4b5c51cc04f31ca9255440'
F='deliverables/final-specification-set/'
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()

def git(repo,*args):return subprocess.check_output(['git','-C',str(repo),*args])
def read(name):return json.loads((OUT/name).read_text())
def write(name,obj):(OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def identity(path,reference=False,commit=None):
    repo=REF if reference else REPO; revision=commit or (R if reference else C)
    raw=git(repo,'show',revision+':'+path)
    assert (repo/path).read_bytes()==raw,path
    return {'repository':'Maruno17/pokemon-essentials' if reference else 'y805939188/pokemon-essentials-clean-room',
     'commit':revision,'tree':git(repo,'rev-parse',revision+'^{tree}').decode().strip(),'path':path,
     'mode':git(repo,'ls-tree',revision,'--',path).decode().split()[0],
     'blob':git(repo,'rev-parse',revision+':'+path).decode().strip(),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

catalog=read('evidence-catalog.json')
def add(eid,path,ranges,reference=False,commit=None,scope='FULL_READ_RANGES_ONLY'):
    if any(x['id']==eid for x in catalog['items']):return
    item=identity(path,reference,commit or (R if reference else B8))
    lines=(REF/path if reference else REPO/path).read_bytes().splitlines(keepends=True)
    item.update({'id':eid,'physical_lines':len(lines),'ranges':ranges,'read_scope':scope,
      'whole_file_read':ranges==[[1,len(lines)]], 'reader':'actual /root external delegated context',
      'root_reception':'UNRECEIVED'})
    item['range_identities']=[{'lines':[a,b],'byte_start':sum(map(len,lines[:a-1])),
       'bytes':len(b''.join(lines[a-1:b])),'sha256':hashlib.sha256(b''.join(lines[a-1:b])).hexdigest()} for a,b in ranges]
    catalog['items'].append(item)

new_reads=[
 ('E-V2-WP11',F+'engine-overworld/wp11-map-topology-transfer.md',[[59,88],[166,194]],False),
 ('E-V2-WP12',F+'engine-overworld/wp12-terrain-movement-vehicles.md',[[52,89],[97,113],[182,198]],False),
 ('E-V2-WP13',F+'engine-overworld/wp13-map-events-npc-followers.md',[[94,109],[154,171]],False),
 ('E-V2-WP06',F+'generic-kernel/wp06-time-random-steps-stats.md',[[82,97]],False),
 ('E-V2-WP09',F+'generic-kernel/wp09-save-startup-continue.md',[[95,109]],False),
 ('E-V2-WP10',F+'generic-kernel/wp10-migration-failure-recovery.md',[[243,247]],False),
 ('E-V2-SCENE','Data/Scripts/003_Game processing/002_Scene_Map.rb',[[1,101],[116,252]],True),
 ('E-V2-PLAYER','Data/Scripts/004_Game classes/008_Game_Player.rb',[[141,275],[416,555],[575,616]],True),
 ('E-V2-CHARACTER','Data/Scripts/004_Game classes/006_Game_Character.rb',[[362,400],[893,993]],True),
 ('E-V2-OVERWORLD','Data/Scripts/012_Overworld/001_Overworld.rb',[[69,218],[223,285]],True),
 ('E-V2-INTERPRETER','Data/Scripts/003_Game processing/003_Interpreter.rb',[[138,206]],True),
 ('E-V2-COMMAND201','Data/Scripts/003_Game processing/004_Interpreter_Commands.rb',[[722,751]],True),
 ('E-V2-FOLLOWER','Data/Scripts/004_Game classes/010_Game_Follower.rb',[[7,215]],True),
 ('E-V2-FOLLOWER-FACTORY','Data/Scripts/004_Game classes/011_Game_FollowerFactory.rb',[[155,191]],True),
 ('E-V2-STARTGAME','Data/Scripts/003_Game processing/001_StartGame.rb',[[37,104]],True),
 ('E-V2-MAPFACTORY','Data/Scripts/004_Game classes/005_Game_MapFactory.rb',[[1,88]],True),
 ('E-V2-MAP','Data/Scripts/004_Game classes/004_Game_Map.rb',[[1,132]],True),
]
for args in new_reads:add(*args)

# These are fixed *contribution routes*, never imported FULL_READ/approval credit.
providers={
 'KERNEL':('coverage/root-active-snapshot-16/kernel_atomic_reception','manual-atomic-clauses.json','sourcefact-consumer-receptions.json'),
 'CORE':('coverage/root-active-snapshot-16/core_atomic_reception','manual_batch_05a.json','sourcefact-consumer-receptions.json'),
 'CRE-A':('coverage/root-active-snapshot-16/creature_a_atomic_reception','manual-atomic-clauses.json','sourcefact-consumer-receptions.json'),
 'CRE-B':('tasks/creature_b','forward-mapping.json','reverse-mapping.json'),
 'CRE-C':('coverage/root-active-snapshot-16/creature_c_existing_crea','forward-mapping.json','reverse-mapping.json'),
 'CRE-E':('adjudication/root-primary-creature_e','forward-mapping.json','reverse-mapping.json'),
 'WORLD':('tasks/world_full','forward-mapping.json','reverse-mapping.json'),
 'WORLD-INTERPRETER':('tasks/world_interpreter','forward-mapping.json','reverse-mapping.json'),
 'WORLD-RESOURCES':('tasks/world_resources_rendering','forward-mapping.json','reverse-mapping.json'),
 'UI':('tasks/ui_full','forward-mapping.json','interfaces.json'),
 'UI66':('tasks/ui_wp66','forward-mapping.json','reverse-mapping.json'),
 'MINIGAMES':('tasks/ui_minigames','forward-mapping.json','reverse-mapping.json'),
 'MOVE':('tasks/com_move','forward-mapping.json','reverse-mapping.json'),
 'ABILITY-ITEM':('coverage/root-active-snapshot-16/core_atomic_reception','ability-assertions.ndjson','ability-reception-unit-map.ndjson'),
 'AI':('tasks/com_ai','forward-mapping.json','reverse-mapping.json'),
 'FACILITY':('tasks/com_facility','forward-mapping.json','interfaces.json'),
 'DEVELOPER':('coverage/root-active-snapshot-16/developer_full_cloud','forward-mapping.json','reverse-mapping.json'),
 'SHARED':('adjudication/root-primary-formal_shared','forward-mapping.json','reverse-mapping.json'),
 'ACTIVITIES':('adjudication/root-primary-world_activities','forward-mapping.json','reverse-mapping.json'),
}
bound=[]
for pid,(directory,*names) in providers.items():
    items=[]
    for name in names:
        path=ROOT+'/'+directory+'/'+name
        assert (REPO/path).exists(),path
        items.append(identity(path))
    bound.append({'id':pid,'contribution_directory':ROOT+'/'+directory,'fixed_items':items,
       'use':'Exact current-primary handoff and recovery route; no whole contribution semantic reception inferred from presence/hash.',
       'reception':'ROOT_CURRENT_DOMAIN_RECEPTION_SEPARATE; not imported as this reader FULL_READ'})
bound.append({'id':'CRE-D','fixed_readset':identity(ROOT+'/delegation/readsets/creature_d.json'),
    'use':'Exact different primary for acquisition/breeding/encounter/capture. No completed CRE-D contribution was present at the fixed carrier in this route.',
    'reception':'UNRECEIVED_CURRENT_DOMAIN_CONTRIBUTION; cannot manufacture a complete contribution or close it by this purpose audit.'})

def provider(path,owner):
    m=re.search(r'/wp(\d+)',path)
    wp=int(m.group(1)) if m else None
    if '/test-catalog/' in path:
        if owner=='creature_review':return ['CRE-A','CRE-B','CRE-C','CRE-D','CRE-E']
        if owner=='combat_review':return ['CORE','MOVE','ABILITY-ITEM','AI','FACILITY']
        if owner=='ui_full':return ['UI','UI66','MINIGAMES']
        if owner=='world_full':return ['WORLD','WORLD-INTERPRETER','WORLD-RESOURCES']
    if owner=='formal_shared':return ['SHARED']
    if owner=='world_activities':return ['ACTIVITIES']
    if owner=='kernel_review':return ['KERNEL']
    if owner=='developer_full':return ['DEVELOPER']
    if owner=='world_full':return ['WORLD-INTERPRETER' if wp==13 else 'WORLD-RESOURCES' if wp in [15,16] else 'WORLD']
    if owner=='ui_full':return ['UI66','UI'] if wp==66 else ['MINIGAMES','UI'] if wp in [68,69,70,71] else ['UI']
    if owner=='creature_review':
        if wp in [27,28,29]:return ['CRE-B']
        if wp in [30,21,22,23,31,32]:return ['CRE-C']
        if wp in [26,33,34,35,36,37,38]:return ['CRE-D']
        if wp in [57,64,68]:return ['CRE-E']
        return ['CRE-A']
    if owner=='combat_review':
        if wp in [43,44,46,47]:return ['MOVE']
        if wp in [48,49,50]:return ['ABILITY-ITEM']
        if wp in [51,52]:return ['AI']
        if wp in [53,54,55,56,58]:return ['FACILITY']
        return ['CORE']
    raise ValueError((path,owner))

freeze=json.loads((REPO/(ROOT+'/delegation/scope-freeze.v1.json')).read_text())
formal_routes=[]
for owner,route in freeze['primary_assignments'].items():
    readset=json.loads((REPO/(ROOT+'/'+route['readset'])).read_text())
    for item in readset.get('formal',[]):
        path=item['path']
        formal_routes.append({'id':'CUR-'+hashlib.sha256(path.encode()).hexdigest()[:12],
          'path':path,'primary_owner':owner,'fixed_readset':identity(ROOT+'/'+route['readset']),
          'current_formal_identity':identity(path,commit=B8),'provider_ids':provider(path,owner),
          'purpose':'B8 engine/data/vector primary replaces a manifest stage paragraph as normative behavioral text; old approval remains provenance only.',
          'this_task_credit':'IDENTITY_AND_PURPOSE_ROUTE_ONLY unless explicitly E-WP23/E-UI66/E-V2 bounded range; not all131 FULL_READ'})
assert len(formal_routes)==131 and len({x['path'] for x in formal_routes})==131
write('current-primary-contribution-routes.v2.json',{'schema':'r8-legacy-current-primary-routes/v2','carrier':C,
 'qualification':'Fixed other-primary contributions/readsets, not an acceptance shortcut. CRE-D absence and other global outstanding receptions remain explicit.',
 'providers':bound,'formal_routes':formal_routes})

manual={int(x['round']):x for x in csv.DictReader((OUT/'event-judgments.v2.tsv').open(),delimiter='\t')}
semantic=read('semantic-purpose-freeze.v2.json')
assert set(manual)==set(range(16,172))
lines=(REPO/'planning/review-manifest-2026-09-19.md').read_text().splitlines()
effective=[
 {'kind':'VERSION_EVENT_NOT_CURRENT_NORMATIVE_RULE','evidence':'E-MANIFEST:3–4,4115–4127; E-FORMAL-README:5–9; E-SCOPE:5–9',
  'rule':'旧第170/171轮及此前所有行保持其时点，旧hash不表示当前新字节；原输入限定批准与新输出/current actual分列。具体历史行为仍是回归/追溯线索，不据此删规则。'},
 {'kind':'CURRENT_EXECUTION_AND_APPROVAL','evidence':'E-CURRENT FULL; E-R7 FULL; E-R8-INPUTS:/current_primary,/R7_required_scope,/historical_read_rule; E-GLOBAL:82–107,149–157,186–207',
  'rule':'本轮current primary为B8正式文与固定R；原输入旧PASS、自检、同blob、计数不能授当前批准；27/56/92各自旧范围保留。'},
 {'kind':'CURRENT_LIMITS_AND_WORKFLOW','evidence':'E-AGENTS FULL; E-GLOBAL:66–80,161–184; E-CURRENT FULL; latest user delegation',
  'rule':'本轮实际源/消费者缺读不可改limit；旧未读只证明当时scope，不能倒填为当前缺材料；宿主/真实Demo/实际配置/运行未知继续按现行合同保留。历史stop/no-agent/no-push不构成本轮权限，最新用户指令控制。'}
]
write('purpose-rules.v2.json',{'schema':'r8-legacy-purpose-rules/v2','rules':effective,
 'not_a_blanket_exemption':'Explicit B21 stage/identity qualification, each event version, actual successor correction, and current-primary route are combined. No old date/negative search alone disposes a paragraph. Mixed text is fully read and layered; only hash/path scalar fields are identity inventory.'})

units=[];unit_of_line={}
def route_topics(path):
    if '/test-catalog/' in path and '-wp' in path:
        return {int(x) for x in re.findall(r'\d+',path.split('-wp',1)[1])}
    m=re.search(r'/wp(\d+)',path)
    return {int(m.group(1))} if m else set()
for frozen in semantic['units']:
    n=frozen['round'];entry=manual[n];topics={int(x) for x in entry['WP_topics'].split(',')}
    routes=[x['id'] for x in formal_routes if route_topics(x['path']) & topics]
    if topics & {78,79,80}:routes.extend(x['id'] for x in formal_routes if x['primary_owner']=='formal_shared')
    routes=sorted(set(routes))
    assert routes,(n,topics)
    next_events=entry['exact_later_events'].split(',')
    successors=[f'LM-E{int(x):03}' if x.isdigit() else x for x in next_events]
    obj={**frozen,'WP_topics':sorted(topics),'reader_judgment':entry['current_purpose_judgment'],
      'actual_successor_events':successors,'current_formal_routes':routes,
      'effective_qualification':'purpose-rules.v2.json#/rules',
      'behavior_layer':'历史版本事实/修订/案例仍有追溯和回归用途；当前实施断言由列明B8正式文与固定R primary承担。不能从本事件的旧批准或作者概括直接导出当前全称规则。',
      'acceptance_layer':'原输入/旧阶段批准保留准确身份和范围；后继批准、R8事实与当前全局接受不转授。',
      'identity_layer':'路径/hash/计数是版本及可恢复性信息；同段非身份行为和资格没有被inventory_only豁免。',
      'workflow_layer':'本事件授权/stop和未执行只说明该阶段；现行权限及执行边界按最新用户与E-GLOBAL。',
      'purpose_review':'COMPLETE_LOCAL_PURPOSE_DISPOSITION','root_reception':'UNRECEIVED',
      'not_claimed':'No all-current-source semantic acceptance, no runtime observation, no global PASS.'}
    units.append(obj)
    for lid in frozen['primary_line_ids']:unit_of_line[int(lid[4:])]=obj
write('semantic-purpose-review.v2.json',{'schema':'r8-legacy-semantic-purpose-review/v2','utc':NOW,
 'reader':'actual /root external delegated context','denominator':156,'reviewed':156,'unreviewed':0,'root_unreceived':156,
 'unit_definition':semantic['unit_definition'],'freeze_qualification':semantic['freeze_qualification'],
 'scope':'Complete current-use disposition of the finite historical primary. Engine-wide clause/fact acceptance belongs to exact current primary routes; it is not silently claimed complete here.',
 'units':units})

process={'授权／预检','授权／固定','授权及输入','授权与预检','授权／固定','授权与预检基线','独立范围／预检','审查与预检','独立授权与预检','预检与保护','复审与预检','独立结论与预检'}
records={'材料','材料／登记','材料与登记','交付与清单','交付与登记','登记','登记与核验','登记／检查','级联／材料','批末交付','修订材料与交付','收尾材料与交付','摘要更正与级联','两层验证','矩阵同步','矩阵增量','矩阵与交付','矩阵／材料／登记','矩阵／C01／C02','矩阵／材料／登记','矩阵／C01／C02'}
workflow={'停止','停止点','通过与停止','登记与停止','登记／停止','登记后校验／停止','新观察／停止','范围与停止','批末出口','边界','本轮边界','继续','下一批','下一批授权','推进安排','既有事项','当前待修','批内顺序','批次授权与顺序','通过与交接'}
acceptance={'复审结论','闭合复审结论','回填','回填（管理性）','管理性回填','三包回填','两包回填','固定／回填','状态与矩阵','集中回填','WP23回填（管理性，行为未改）','WP66-C回填（管理性，行为未改）','两包回填（管理性，行为未改）','作者整体验收（程序化＋人工，结果写入完成报告 §4）'}
prior=read('purpose-dispositions.json')
for p in prior['units']:
    n=p['line'];event=unit_of_line[n];text=lines[n-1].strip()
    label=''
    if not text:role='LAYOUT_NO_ASSERTION'
    elif text.startswith('**第'):role='VERSION_EVENT_HEADING'
    elif n<=2079:role='MIXED_VERSION_EVENT_SYNOPSIS'
    else:
        m=re.match(r'- \*\*(.*?)\*\*',text)
        label=(m.group(1) if m else '').rstrip('：:')
        role=('HISTORICAL_PROCESS_IDENTITY' if label in process else
          'HISTORICAL_RECORD_AND_IDENTITY' if label in records else
          'HISTORICAL_WORKFLOW_WITH_SCOPE_QUALIFICATION' if label in workflow else
          'HISTORICAL_APPROVAL_PROVENANCE' if label in acceptance else
          'VERSION_BOUND_BEHAVIOR_OR_QUALIFICATION')
    p.update({'semantic_event':event['id'],'purpose_status':'COMPLETE_LOCAL_PURPOSE_DISPOSITION',
      'paragraph_role':role,'paragraph_label':label,'current_purpose_reason':event['reader_judgment'],
      'actual_successor_events':event['actual_successor_events'],'current_formal_routes':event['current_formal_routes'],
      'current_behavior_reliance':'B8_CURRENT_PRIMARY_SEPARATE; legacy fact/case is versioned provenance and regression input, never old approval transferred',
      'semantic_assertion_disposition':'All assertions in this complete paragraph retain their version-bound meaning. Mixed approval, identity, workflow and effective scope are separated at event-layer review; no punctuation/JSON atom requirement count.',
      'effective_qualification':'purpose-rules.v2.json#/rules','root_reception':'UNRECEIVED',
      'exemption':'No whole-paragraph inventory exemption. Hash/path scalar fields only; actual text FULL_READ.'})
    p.pop('atomic_assertions',None)
    p.pop('historical_context_reason',None)
    p.pop('exact_successor_or_qualification_evidence',None)
    p.pop('purpose_group',None)
prior.update({'schema':'r8-external-legacy-purpose/v2','utc':NOW,
 'status':'PRIMARY_PURPOSE_REVIEW_COMPLETE_PENDING_ROOT_RECEPTION','semantic_event_denominator':156,
 'qualification':'All881 content paragraphs fully read and current-use disposition completed under156 meaningful historical events, exact successors and current-primary routes. This is finite documentary purpose acceptance by this reader, not current engine-wide/source/global approval. All primary remains root-unreceived.'})
prior.pop('groups',None)
write('purpose-dispositions.json',prior)

# Selected complete contribution records were actually read, not the entire files.
selected=[]
for task,key,wanted in [('world_full','units',{'WFS-004','WFS-005','WFS-025','WFS-028','WFS-031','WFS-032'}),
                        ('world_interpreter','units',{'WI04','WI18','WI19','WI21','WI22','WI26'})]:
    path=ROOT+'/tasks/'+task+'/forward-mapping.json';payload=json.loads((REPO/path).read_text())
    records_read=[{'pointer':'/'+key+'/'+str(i),'id':x.get('unit_id',x.get('id')),'record':x} for i,x in enumerate(payload[key]) if x.get('unit_id',x.get('id')) in wanted]
    assert len(records_read)==len(wanted)
    selected.append({'identity':identity(path),'scope':'FULL_READ_SELECTED_RECORDS_ALL_FIELDS; not whole file',
       'records':records_read,'reception':'Finite meaning compared with newly read exact R/current formal below; no provider full-file reading transferred.'})
write('world-interface-reception.v2.json',{'schema':'r8-legacy-world-interface-reception/v2','utc':NOW,'fixed_contributions':selected,
 'scope':'Only the five coherent2849 assertions and their exact later qualifications; not allWORLD. Current source/clauses actually read independently as E-V2 evidence.',
 'runtime':'NOT_EXECUTED'})

five=[
 ('F-LMC-2849-VEHICLE','旧载具清理一致性保留为交界追溯，现行区分事件201保留游泳、直接默认取消及骑行目的地门；force_cycling只在实际进入通知时调整。',
  ['E-V2-SCENE:56–101,121–134,165–175','E-V2-COMMAND201:722–748','E-V2-PLAYER:575–616','E-V2-OVERWORLD:263–275'],
  ['E-V2-WP11:64–73','E-V2-WP12:184–196'],['WFS-005','WFS-028','WFS-032'],
  '有效对象、非战斗且201的已有转移/消息/转场守卫均放行；请求已到地图场景消费者且前序helper正常；普通201与直接调用分列；无插件。',
  '普通201保留冲浪/潜水；仅改为直接省参入口则清标志。临时基点另有后继通知门，不推全回滚。'),
 ('F-LMC-2849-STEP','旧计步不重复定义的主从关系仍有效；B8将开始写坐标/距离/条件离格与完成后合格玩家全局步数明确分离，并保留强制路线/解释器早退。',
  ['E-V2-PLAYER:141–193,416–555','E-V2-CHARACTER:362–400,893–993','E-V2-OVERWORLD:170–218'],
  ['E-V2-WP12:97–113','E-V2-WP06:82–97'],['WFS-025','WFS-031','WI26'],
  '有效普通玩家、已通过普通移动门；通知/更新正常，无额外改写。',
  '普通移动开始后尚未完成：坐标/距离已写但全局步数未因完成而加；正常完成且非强制路线/解释器后才进全局计步。'),
 ('F-LMC-2849-FOLLOW','旧跟随/路线通行一致性不是统一strict调用：当前跟随实际location入口、临时through、同轴1/2格与其他直接定位分列；显式传送写runtime和持久记录。',
  ['E-V2-FOLLOWER:7–215','E-V2-FOLLOWER-FACTORY:155–191','E-V2-CHARACTER:362–400','E-V2-SCENE:72–101'],
  ['E-V2-WP13:154–171','E-V2-WP12:52–89'],['WI18','WI19','WI21','WI22','WI26'],
  '固定R普通合法地图/角色，无外部覆写，前序与地形query正常；不保证全部地图实际可达。',
  '两格中间许可是两次一步尝试而非保证到达；非同轴(1,1)或同轴≥3走直接定位。through恢复只在正常返回，异常不附加ensure保证。'),
 ('F-LMC-2849-ERROR','旧脚本异常分层仍作追溯：SystemExit/名为Reset原样抛出，其他异常走带事件上下文的错误，不可当脚本成功返回或全回滚。',
  ['E-V2-INTERPRETER:138–206'],['E-V2-WP13:104–109'],['WI04'],
  '解释器execute_script已到达、有效错误对象/上下文，错误格式化本身正常；终端宿主呈现不认证。',
  '正常表达式保留其值；SystemExit/Reset与普通异常分支不同；抛错前状态修改不据异常包装撤销。'),
 ('F-LMC-2849-MISSINGMAP','旧缺图差异由v3及B8进一步按音频/入口限定：显式转移无选图恢复，有音频先读目标图而失败，皆无时可到重建；仅读档重建的ENOENT有调试选择/取消与非调试错误。',
  ['E-V2-SCENE:56–101','E-V2-STARTGAME:37–104','E-V2-MAPFACTORY:7–28','E-V2-MAP:38–75'],
  ['E-V2-WP11:64–66,171','E-V2-WP09:97–109','E-V2-WP10:243–247'],['WFS-004','WFS-005'],
  '目的图读取以ENOENT失败；前序对象/载具/helper正常；读档magic/safesave门成立；不执行真实Map/存档。',
  '仅切换有无播放BGM/BGS，就改变显式转移缺图时是否已到清桥/重建；读档调试取消退出不是显式转移的默认恢复。')
]
forward=read('forward-mapping.json')
forward['status']='FINITE_PURPOSE_LINEAGE_AND_SELECTED_CURRENT_FACTS_REVIEWED; current domain primary handoffs separate'
forward['semantic_purpose_units']='semantic-purpose-review.v2.json#/units'
for fid,fact,src,spec,peer,premise,control in five:
    if any(x['id']==fid for x in forward['facts']):continue
    forward['facts'].append({'id':fid,'fact':fact,'premise':premise,'source':src,'spec':spec,
       'actual_provider_record_reception':peer,'legacy':['LM-L2849','LM-E016','LM-E017'],
       'ordinary_boundary_control':control,'consumer':'Named real callers/receivers in source/current formal and full selected records in world-interface-reception.v2.json',
       'status':'SOURCE_STATIC_FINITE_CURRENT_PURPOSE_RECEPTION; ROOT_UNRECEIVED','execution':'NOT_EXECUTED',
       'excluded':'No other domain FULL_READ/PASS, real maps/save/host, unbounded dynamic consumers or all branch reception.'})
forward['remaining']='No undetermined primary historical purpose remains. Full current engine/source/data/vector acceptance belongs to current-primary-contribution-routes.v2.json and root receivers; never imported from historical PASS.'
write('forward-mapping.json',forward)
reverse=read('reverse-mapping.json')
reverse['status']='FINITE_DOCUMENTARY_PURPOSE_REVIEW_COMPLETE; source/formal clauses outside selected facts remain other-primary scope'
reverse['semantic_purpose_units']='semantic-purpose-review.v2.json#/units'
reverse['clauses']=[{'spec':s,'fact':f['id'],'premise':f['premise'],'source':f['source'],'qualification':f['status']} for f in forward['facts'] for s in f['spec']]
reverse['gaps']='Root reception and different current-primary engine-wide receptions remain explicit in interfaces.json; these are not881 still-undetermined historical paragraph purposes.'
write('reverse-mapping.json',reverse)

catalog['as_of_utc']=NOW;write('evidence-catalog.json',catalog)
ledger=read('reading-ledger.json')
ledger['updated_utc']=NOW
ledger['current_purpose']='ALL156 semantic version events / all881 content paragraphs locally purpose-reviewed with exact successors and current-primary routes; ROOT_UNRECEIVED'
ledger['actual_counts'].update({'semantic_purpose_events':156,'semantic_purpose_reviewed':156,'semantic_purpose_unreviewed':0,
 'currentness_unclosed_content_paragraphs':0,'bounded_fact_mappings':10,
 'purpose_assertion_denominator':'156 coherent version/review/authorization events;881 complete content paragraphs. Not punctuation/JSON fields or unique engine requirements.'})
ledger['actual_counts'].pop('atomic_assertion_denominator',None)
ledger['v1_precision_correction']='v1 conservatively marked all881 paragraphs UNDECOMPOSED/UNFROZEN, conflating this documentary-purpose task with the complete current engine atomic census. v2 explicitly freezes meaningful156 events, disposes every paragraph and separates mixed facets. Whole-engine/current other-primary atomic completeness is not claimed.'
ledger['v2_additional_reads']=[{'id':x[0],'path':x[1],'ranges':x[2],'scope':'Actual full continuous named ranges; not whole files unless explicitly stated'} for x in new_reads]
ledger['v2_peer_reads']='world-interface-reception.v2.json exact12 complete record pointers/identities. Fixed other-provider route JSON is identity/field routing only, not complete semantic receipt.'
ledger['v2_navigation_rereads']='Manifest1–65,4115–4127; CURRENT-DELIVERY andR7README full; root-primary-routes83lines andscope-freeze126lines full. Oversized1908–1932/progress composite display was truncated, not new full-read credit; these manifest ranges already fully read in v1.'
ledger['v2_provider_report_full_reads']=[ROOT+'/tasks/world_topology_audit/review.md',ROOT+'/tasks/world_full/reverse-mapping.json',ROOT+'/coverage/root-active-snapshot-14/kernel_atomic_reception/review.md',ROOT+'/coverage/root-active-snapshot-16/core_atomic_reception/review.md']
write('reading-ledger.json',ledger)

write('interfaces.json',{'schema':'r8-external-legacy-interfaces/v2','utc':NOW,'primary_purpose_review':'COMPLETE_LOCAL',
 'root_reception':'UNRECEIVED','interfaces':[
 {'id':'I-LMC-NAV','state':'PURPOSE_REVIEWED','producer':'E-EXTRACTION:3 / E-MANIFEST:3–4','consumer':'Current progress/history reader',
  'reception':'Historical execution progress remains a valid trace purpose; current stage is bounded byB21 exact old-row qualification andB8 rootR7 navigation. No old date/negative search exemption.'},
 {'id':'I-LMC-N01','state':'FINITE_LOCAL_SOURCE_CURRENT_FORMAL_RECEPTION','facts':['F-N01-01','F-N01-02','F-N01-03','F-N01-04','F-N01-05'],
  'current_provider_ids':['CRE-C','UI66','UI'],'retained':'All special-position descendants/host/save execution not certified; source/formal broader domain belongs exact fixed routes.'},
 {'id':'I-LMC-2849','state':'ALL_FIVE_CURRENT_PURPOSE_CHAINS_LOCALLY_REVIEWED','facts':[x[0] for x in five],
  'current_provider_ids':['WORLD','WORLD-INTERPRETER','KERNEL'],'receipt':'world-interface-reception.v2.json + E-V2 actual source/current formal ranges; no whole-domain approval.'},
 {'id':'I-LMC-CURRENT-DOMAINS','state':'EXACT_OTHER_PRIMARY_HANDOFFS_ROOT_RECEPTION_OPEN','fixed_routes':'current-primary-contribution-routes.v2.json',
  'scope':'Current source/default/backup/compiler/persistence/display/vector completeness belongs original frozen primary, not legacy-version prose. Exact available provider objects and the absent CRE-D complete contribution distinguished; no oldPASS/metadata completion shortcut.',
  'not_transferred':'All1413 legacy primary line purpose judgments remain this task responsibility and are now locally reviewed, not handed away.'},
 {'id':'I-LMC-HISTORY-APPROVAL','state':'QUALIFIED_HISTORICAL_PROVENANCE_NOT_CURRENT_APPROVAL','scope':'All156 old events/881 content paragraphs retain input identity and stage; latercurrent contribution acceptance must follow its ownactual receipts. No evidence0/WAIT/FAIL erased.'},
 {'id':'I-LMC-ROOT','state':'UNRECEIVED','scope':'Root receives all156purpose units/all1413primary lines and independently counters R8-LMC-H001; proposer does not self-adjudicate.'}
 ],'local_purpose_unreviewed':0,'source_business_execution':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'})

write('gaps.json',{'schema':'r8-external-legacy-gaps/v2','status':'PRIMARY_PURPOSE_REVIEW_COMPLETE_PENDING_ROOT_RECEPTION',
 'primary_purpose_unread_lines':0,'primary_purpose_undetermined_paragraphs':0,'primary_purpose_undetermined_events':0,
 'gaps':[
 {'id':'LMC-RECEPTION-ROOT','type':'ACTUAL_DIFFERENT_CONTEXT_ROOT_RECEPTION','unreceived_events':156,'unreceived_primary_lines':1413,'ranges':[[1933,2079],[2849,4114]],
  'action':'Main reviewer receives exact local purpose judgments/current-fact chains and independently counters H001; cannot use same-context role renaming.'},
 {'id':'LMC-INTERFACE-CURRENT-PRIMARY','type':'OTHER_PRIMARY_CURRENT_ENGINE_ACCEPTANCE','route':'current-primary-contribution-routes.v2.json',
  'scope':'Named frozen source/formal/data/vector primary responsibilities; fixed available contributions bound, CRE-D complete contribution absent at carrier explicitly. This task does not claim their all-consumer/global acceptance. No881paragraph undetermined-purpose gap remains.'},
 {'id':'LMC-EXECUTION','type':'NOT_EXECUTED','scope':'Reference observations/behavior model/host/Demo/native media/real save/replay/business vectors0.'},
 {'id':'LMC-CONFIG','type':'UNVERIFIED','scope':'Actualmodel/effort/tier/speed/Fast/session/logID not echoed.'}
 ]})
progress=read('progress.json')
progress.update({'updated_utc':NOW,'status':'PRIMARY_PURPOSE_REVIEW_COMPLETE_PENDING_ROOT_RECEPTION',
 'semantic_purpose_denominator':156,'semantic_purpose_reviewed':156,'semantic_purpose_unreviewed':0,
 'currentness_unclosed_content_paragraphs':0,'purpose_assertion_denominator':'156 coherent event units with881 complete paragraph dispositions; not unique engine requirement count',
 'v2_reading_and_purpose_review_end_utc':NOW,'publication':'V2_NOT_YET_PUSHED',
 'pending':['Root actual reception of156semantic purpose units/1413primarylines',
 'Different-context independent counter androot adjudication ofH001 withcontraryparentqualification',
 'Current fullengine/source/data/vector domain receptions at exact fixed contribution routes; separate primary scopes',
 'V2 ordinary push and complete immutable remote byte readback']})
progress.pop('atomic_assertion_denominator',None)
progress['primary_denominator'].pop('atomic_assertions',None)
write('progress.json',progress)

print(json.dumps({'semantic_events':156,'paragraphs':881,'purpose_unreviewed':0,'primary_unread':0,
 'primary_root_unreceived':1413,'new_bounded_current_fact_chains':5,'current_formal_routes':131,
 'fixed_provider_routes':len(bound),'status':progress['status']},ensure_ascii=False))
