"""Serialize the parent's completed reads and recorded judgments; no auto-review."""
import collections
import hashlib
import json
import pathlib
import re
import subprocess

W=pathlib.Path('/Users/dingshinn/.codex/worktrees/review-fifth-9366d9d/pokemon-framework-reference')
R=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
O=pathlib.Path(__file__).resolve().parents[1]
B='9366d9d17aaeac3b4414236468affa650fb3dd27'
RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
F='deliverables/final-specification-set/'
S='Data/Scripts/'
checkpoint=O/'reading-coverage-before-map.json'
if not checkpoint.exists():checkpoint.write_bytes((O/'reading-coverage.json').read_bytes())
base=json.loads(checkpoint.read_text())
findings=json.loads((O/'findings.json').read_text())['findings']

def dump(name,value):
    (O/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def blob(path,root=W,commit=B):
    return subprocess.check_output(['git','-C',str(root),'rev-parse',commit+':'+path],text=True).strip()

def intersects(a,b):return a[0]<=b[1] and b[0]<=a[1]

spec_for_source={
 '005_Player_Pokedex.rb':['pokemon-rules/wp62-pokedex-records-regions-and-content.md'],
 '002_UI_Pokedex_Menu.rb':['pokemon-rules/wp62-pokedex-records-regions-and-content.md','user-interface/wp66-b-storage-and-pokedex-ui.md'],
 '003_UI_Pokedex_Main.rb':['pokemon-rules/wp62-pokedex-records-regions-and-content.md','user-interface/wp66-b-storage-and-pokedex-ui.md'],
 '004_UI_Pokedex_Entry.rb':['pokemon-rules/wp62-pokedex-records-regions-and-content.md','user-interface/wp66-b-storage-and-pokedex-ui.md'],
 '004_Item_Phone.rb':['user-interface/wp63-pokegear-map-music-and-phone.md'],
 '008_UI_Pokegear.rb':['user-interface/wp63-pokegear-map-music-and-phone.md'],
 '009_UI_RegionMap.rb':['user-interface/wp63-pokegear-map-music-and-phone.md'],
 '010_UI_Phone.rb':['user-interface/wp63-pokegear-map-music-and-phone.md'],
 '011_UI_Jukebox.rb':['user-interface/wp63-pokegear-map-music-and-phone.md'],
 '001_Minigame_Duel.rb':['user-interface/wp68-duel.md'],
 '002_Minigame_TripleTriad.rb':['creature-rpg/wp68-triple-triad.md'],
 '003_Minigame_SlotMachine.rb':['user-interface/wp69-slot-machine.md','user-interface/wp69-slot-reels.md'],
 '004_Minigame_VoltorbFlip.rb':['pokemon-rules/wp69-voltorb-flip.md','pokemon-rules/wp69-voltorb-layouts.md'],
 '005_Minigame_Lottery.rb':['pokemon-rules/wp70-lottery.md'],
 '006_Minigame_Mining.rb':['user-interface/wp70-mining.md','user-interface/wp70-mining-data.md'],
 '007_Minigame_TilePuzzles.rb':['user-interface/wp71-tile-puzzles.md']
}
# These subdivisions refine already-read whole-body semantic records.
refinements={
 '004_Item_Phone.rb':[(1,210,'电话对象、查找/注册/可见排序/对象级与公开入口的相异实参域'),(211,313,'联系人类型、字段默认、可见性setter、相对版本/下一版本/倒计时与自开关'),(314,449,'呼出和呼入的前门/候选、记录vs身份、共同事件与对话生成、旗标1→2'),(450,538,'播放分段/本地化/颜色、每通TP/TE一次抽样及队伍与遭遇前四槽/地图名'),(539,561,'每帧持机/菜单/消息/路线/解释器门与双计时更新'),(562,706,'18个旧入口的默认/转发/返回/首次错误与写入前缀')],
 '008_UI_Pokegear.rb':[(1,110,'性别图逐项回退、按钮选中裁片与初始化/释放'),(111,159,'按钮循环BACK>USE>UP>DOWN及效果返回true退出'),(160,206,'Map10/Phone20/Jukebox30注册、联系人条件停用、飞行目标写入与退出哨兵')],
 '009_UI_RegionMap.rb':[(1,157,'30×20格/16单位、最终地区选择、地图/玩家初始位置、尺寸仅长度与资源初值'),(158,247,'地点编辑/保存、三种首条查询、开关/墙面门、附加图与飞行刷新'),(248,320,'先八向逻辑位移/插值门，再BACK/飞行USE/编辑USE/ACTION，目标返回/取消'),(321,356,'普通/飞行包装与wallmap写目标门')],
 '010_UI_Phone.rb':[(1,138,'可见列表、信号/再战统计/头像、初始化及刷新/释放'),(139,189,'普通与移动模式键优先、游标实时写底层顺序及BACK还原'),(190,271,'空联系人入口、呼叫/移动/删除仅训练家、三排序与删光关闭')],
 '011_UI_Jukebox.rb':[(1,90,'Custom六扩展、去扩展去重/小写排序/空目录与子列表选择取消'),(91,149,'固定命令选择、电台与默认覆盖/两个遭遇旗标、Stop和退出不回滚')]
}
for source in base['sources']:
    name=pathlib.Path(source['path']).name
    if source.get('scope_role')=='primary' and name in refinements:
        source['semantic_ranges']=[{'lines':[a,b],'entries_and_rules':fact} for a,b,fact in refinements[name]]

capabilities=[]
for source in base['sources']:
    if source.get('scope_role')!='primary':continue
    name=pathlib.Path(source['path']).name
    for unit in source['semantic_ranges']:
        matches=[]
        for finding in findings:
            if any(a['path']==source['path'] and any(intersects(unit['lines'],v) for v in a['lines']) for a in finding['source_anchors']):matches.append(finding['id'])
        status='partial' if matches else 'supported'
        cid='M11-S'+str(len(capabilities)+1).zfill(3)
        caps={'capability_id':cid,'module':'M11','behavior_purpose':unit['entries_and_rules'],
          'source_anchors':[{'path':source['path'],'version':RC,'lines':[unit['lines']],'git_blob':source.get('git_blob')}],
          'spec_anchors':[{'path':F+p,'version':B,'section':'Relevant named domain contract; per-clause receiving anchors in spec-to-source.json'} for p in spec_for_source[name]],
          'entry_or_caller':'Primary entry/handler and necessary callers inventoried in reading-coverage.json; for minigame wrappers external map/event caller unavailable, not claimed reachable in demo.',
          'preconditions':['Legal domain inputs and preceding scene/data dependencies as explicitly described in referenced current clauses','No unlisted plugin override; conditional bad-input/exception branches retain own listed preconditions'],
          'data_config_host_limits':'Default and optional data separated; all179 literal minigame rows and region/phone/map projections recorded in data-comparison.json. Missing assets and compatible native host do not imply callable source absent.',
          'reviewed_scope':{'source_semantic_range':unit['lines'],'complete_within_assigned_range':True,'necessary_projections':'reading-coverage.json dependency ranges','originals':'original-range-comparison.json exact ranges + actual delta reads'},
          'status':status,'status_reason':('Existing gameplay/IO/state/math contract statically sufficient within this unit; normal, rejection, cancellation, partial commit and explicit unknown boundaries compared.' if not matches else 'Existing contract receives part of this unit; concrete additional range independently challenged under '+','.join(matches)),
          'supported_static':status=='supported','material_availability':'available_text','review_extent':'full','evidence_level':['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR'],
          'reviewer':'root firsthand','reviewer_task_id':base['task_id'],'findings':matches,
          'dependencies':['Shared services retain canonical owners; see shared-interfaces.json'],
          'unverified':['Native UI/assets/audio/keyboard scheduling/demo event reachability','Unlimited plugin/runtime combinations'],
          'execution_status':'R5-REF-004 limited reel methods only' if name=='003_Minigame_SlotMachine.rb' and unit['lines'][0]==1 else 'NOT_EXECUTED'}
        capabilities.append(caps)
        unit.update(status=status,comparison=caps['status_reason'],capability_id=cid,evidence_level=caps['evidence_level'])
    source.update(review_extent='full',unreviewed_ranges=[],unreviewed_semantic_obligations=[],scope_completion=True)

# Actual read source/data ranges added after the first dependency checkpoint.
extra=[('010_Data/001_Hardcoded data/004_BodyShape.rb',1,9999,'Full14shape registry/default/name/icon/order consumer'),('010_Data/001_Hardcoded data/005_BodyColor.rb',1,9999,'Full10color registry/default/name/order consumer'),('021_Compiler/002_Compiler_CompilePBS.rb',1,101,'Generic repeated fields andTownMapcompile/translation generation'),('021_Compiler/002_Compiler_CompilePBS.rb',593,629,'Regionalflatorder/duplicate/no-sectionfailure/save phase'),('021_Compiler/002_Compiler_CompilePBS.rb',1173,1191,'MapMetadata validation doesnotrestrictmasktext'),('021_Compiler/002_Compiler_CompilePBS.rb',1237,1269,'Default phone identity/compoundID/repeatedtexttranslation')]
for path,a,b,fact in extra:
    path=S+path;n=len((R/path).read_text().splitlines());b=min(b,n)
    row=next((x for x in base['sources'] if x['path']==path),None)
    if row is None:
        row={'path':path,'version':RC,'line_count':n,'scope_role':'dependency_projection','material_availability':'available_text','review_extent':'partial','body_read_ranges':[],'semantic_ranges':[]};base['sources'].append(row)
    row['body_read_ranges'].append([a,b]);row['semantic_ranges'].append({'lines':[a,b],'entries_and_rules':fact,'status':'supported','comparison':'Actual source projection compared to current M11 data consumer contracts; M01 retains complete compiler/schema responsibility','evidence_level':['SOURCE_STATIC','SPEC_STATIC']})
for path in ['PBS/regional_dexes.txt','PBS/town_map.txt','PBS/phone.txt']:
    n=len((R/path).read_text(encoding='utf-8-sig').splitlines());base['sources'].append({'path':path,'version':RC,'line_count':n,'git_blob':blob(path,R,RC),'scope_role':'complete_data_consumer_projection','material_availability':'available_text','review_extent':'full','body_read_ranges':[[1,n]],'semantic_ranges':[{'lines':[1,n],'entries_and_rules':'All records/fields read; corresponding registry/parser and M11 consumers inspected. Perrecord ordered identities and contract outcomes in data-comparison.json','status':'supported','comparison':'No record identity/order/default discrepancy found in current projection; compiler primary review M01 remains separate'}],'unreviewed_ranges':[]})
base['data_record_projections']={'artifact':'data-comparison.json','reviewer':'root firsthand','scope':['all407 orderedregionalmembers','all27townpoints','all3phone recordseveryfield','all69defaultmapmetadata relevantfields','all48miningcandidate identity/pocket records','all179minigame literal rows including75distribution/61item/13iron/22reel/8frequency'],'evidence_level':['SOURCE_STATIC','SPEC_STATIC','TOOL_VALIDATION'],'behavior_execution':False,'note':'Data comparison is exact field support, not game simulation. Other PBS fields/variants remain under M01/M04/M06 primary roles.'}

# Assigned test projections were read as exact rows; foreign sections stay excluded.
test_ranges={
F+'test-catalog/pokemon-rules-wp53-60-61-62-69-70.md':[[112,222]],
F+'test-catalog/creature-rpg-wp35-36-57-64-68.md':[[129,158]],
F+'test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md':[[53,130],[267,282],[284,287],[433,533],[584,589],[596,597],[607,609],[710,710],[775,787]]}
for path,ranges in test_ranges.items():
    base['specifications'].append({'path':path,'version':B,'body_read_ranges':ranges,'review_extent':'partial','scope_role':'complete M11 projection of shared catalogue; foreign rows excluded','semantic_status':'Alllisted current input/expected rows directly compared with source and corresponding formal/original; noexecution claimed'})

fullspecs=[x for x in base['specifications'] if x['path'].startswith(F) and '/test-catalog/' not in x['path']]
for item in fullspecs:
    if pathlib.Path(item['path']).name!='wp66-b-storage-and-pokedex-ui.md':
        item.update(review_extent='full',scope_completion=True,semantic_status='Full body, tables and implicit/explicit exceptions reverse-checked; candidate omissions tracked separately, not falsely converting all content to PASS')

def atomic_units(path,ranges):
    lines=(W/path).read_text().splitlines();section='preamble';buffer=[];start=None
    def emit():
        if buffer:
            return {'lines':[start,start+len(buffer)-1],'section':section,'text':'\n'.join(buffer)}
    for i,line in enumerate(lines,1):
        active=any(a<=i<=b for a,b in ranges)
        if not active or not line.strip() or line.startswith('#') or line.startswith('|'):
            value=emit()
            if value:yield value
            buffer=[];start=None
            if not active:continue
            if line.startswith('#'):section=line.lstrip('# ').strip();continue
            if line.startswith('|') and not re.fullmatch(r'[| :\-]+',line):
                yield {'lines':[i,i],'section':section,'text':line}
            continue
        if start is None:start=i
        buffer.append(line)
    value=emit()
    if value:yield value

def matching_caps(path,unit):
    name=pathlib.Path(path).name
    text=unit['text'];section=unit['section']
    if '/test-catalog/' not in path:
        candidates=[c for c in capabilities if any(s['path']==path for s in c['spec_anchors'])]
        chapter=re.match(r'(\d+)',section)
        chapter=int(chapter[1]) if chapter else 0
        local_ranges={
          'wp68-duel.md':{2:[[57,137],[383,394]],3:[[138,314]],4:[[110,137]],5:[[94,137],[315,339]],6:[[57,92],[138,339]]},
          'wp68-triple-triad.md':{2:[[8,134]],3:[[717,760],[950,1043],[1294,1300]],4:[[700,805],[258,345]],5:[[371,943],[647,696]],6:[[860,944]],7:[[1048,1289]]},
          'wp69-slot-machine.md':{1:[[427,456]],2:[[8,103]],3:[[147,193]],4:[[313,407]],5:[[194,273],[408,415]],6:[[15,32],[313,456]]},
          'wp69-voltorb-flip.md':{1:[[120,125],[170,255],[646,705]],2:[[8,168]],3:[[319,458],[528,580]],4:[[452,526],[667,674]],5:[[381,429]],6:[[319,526],[695,705]]},
          'wp70-mining.md':{1:[[624,645]],2:[[147,227],[336,350]],3:[[233,335],[352,390]],4:[[39,142],[392,527]],5:[[474,612]],6:[[266,298],[496,527],[600,618]]},
          'wp71-tile-puzzles.md':{1:[[600,608]],2:[[25,39],[90,147],[148,249]],3:[[189,367],[369,509]],4:[[250,367],[369,572]],5:[[189,249]],6:[[503,572]],7:[[25,147],[148,187],[307,495]],8:[[189,509]],9:[[189,304],[412,495],[511,572]]}
        }.get(name,{}).get(chapter)
        if local_ranges:return [c for c in candidates if any(intersects(a['lines'][0],v) for a in c['source_anchors'] for v in local_ranges)]
        if name=='wp63-pokegear-map-music-and-phone.md':
            keys={2:['008_UI_Pokegear.rb'],3:['009_UI_RegionMap.rb'],4:['004_Item_Phone.rb','010_UI_Phone.rb'],5:['004_Item_Phone.rb'],6:['011_UI_Jukebox.rb']}.get(chapter)
            if keys:return [c for c in candidates if any(pathlib.Path(a['path']).name in keys for a in c['source_anchors'])]
        if name=='wp62-pokedex-records-regions-and-content.md':
            keys=['005_Player_Pokedex.rb'] if chapter in [2,3,4] else None
            if keys:return [c for c in capabilities if any(pathlib.Path(a['path']).name in keys for a in c['source_anchors'])]
        return candidates
    if name=='creature-rpg-wp35-36-57-64-68.md':key='002_Minigame_TripleTriad.rb'
    elif name=='pokemon-rules-wp53-60-61-62-69-70.md':
        key='004_Minigame_VoltorbFlip.rb' if section.startswith('VF') else '005_Minigame_Lottery.rb' if section.startswith('LT') else None
        if key is None:return [c for c in capabilities if any('/005_Player_Pokedex.rb' in a['path'] or '/003_UI_Pokedex_Main.rb' in a['path'] or '/004_UI_Pokedex_Entry.rb' in a['path'] for a in c['source_anchors'])]
    else:
        prefixes={'DU':'001_Minigame_Duel.rb','SL':'003_Minigame_SlotMachine.rb','MN':'006_Minigame_Mining.rb','TP':'007_Minigame_TilePuzzles.rb'}
        key=next((v for k,v in prefixes.items() if section.startswith(k)),None)
        if key is None:
            if section.startswith('PG'):return [c for c in capabilities if any('/004_Item_Phone.rb' in a['path'] or pathlib.Path(a['path']).name in ['008_UI_Pokegear.rb','009_UI_RegionMap.rb','010_UI_Phone.rb','011_UI_Jukebox.rb'] for a in c['source_anchors'])]
            return [c for c in capabilities if any(pathlib.Path(a['path']).name in ['005_Player_Pokedex.rb','002_UI_Pokedex_Menu.rb','003_UI_Pokedex_Main.rb','004_UI_Pokedex_Entry.rb'] for a in c['source_anchors'])]
    return [c for c in capabilities if any(pathlib.Path(a['path']).name==key for a in c['source_anchors'])]

clauses=[]
seen=set()
for item in base['specifications']:
    path=item['path']
    if path in seen:continue
    seen.add(path)
    owned_ranges=item['body_read_ranges']
    if pathlib.Path(path).name=='wp66-b-storage-and-pokedex-ui.md':
        owned_ranges=[[124,218],[224,224],[226,226],[236,247],[257,257],[268,269],[271,271]]
        item['inverse_owned_ranges']=owned_ranges
        item['excluded_from_this_inverse_signature']='Foreign storage portions, including mixed clause225, are owned and fully reviewed by M10; body reading is broader than this M11 signature.'
    for unit in atomic_units(path,owned_ranges):
        selected=matching_caps(path,unit)
        meta=any(x in unit['section'] for x in ['未决','来源','依赖','边界与保留']) or unit['section']=='preamble'
        record={'clause_id':'M11-C'+str(len(clauses)+1).zfill(4),'path':path,'version':B,'git_blob':blob(path),'lines':unit['lines'],'section':unit['section'],
          'clause_kind':'scope_dependency_or_audit' if meta else 'table_or_vector' if unit['text'].startswith('|') else 'behavioral_prose',
          'clause_digest_sha256':hashlib.sha256(unit['text'].encode()).hexdigest(),'summary':unit['text'][:220],
          'capability_ids':[c['capability_id'] for c in selected],
          'source_anchors':[a for c in selected for a in c['source_anchors']],
          'preconditions':'The exact current clause/vector inputs and normal/contrasting limits were read in full; inherited domain/source conditions stay local, not universalized.',
          'shared_contracts':'shared-interfaces.json; unique producer/consumer role, no duplicate global ownership',
          'status':'supported','supported_static':True,'reason':'Existing factual contract/vector is supported in its explicit scope; additional source behavior omitted by this bounded contract is separately partial in source-to-spec/findings. Scope/history text is retained as qualified audit context, not new acceptance.',
          'reviewer':'root firsthand','material_availability':'available_text','review_extent':'full','evidence_level':['SPEC_STATIC','SOURCE_STATIC'] if not meta else ['SPEC_STATIC'],
          'execution_status':'NOT_EXECUTED; separate R5-REF-004 doesnotexecute these catalogue vectors',
          'related_candidate_findings':[f['id'] for f in findings if path in f['affected_files']],
          'unverified':['Runtime/host/assets and dynamic combinations beyond exact clause premises']}
        # Explicit non-01 reservations are reviewed but leave a known receiving gap.
        if ('非01' in unit['text'] or '非 01' in unit['text'] or '01文本' in unit['text']) and ('MapSize' in unit['text'] or '转换' in unit['text'] or '扩张' in unit['text']):
            record.update(status='partial',supported_static=False,reason='Current01scope itselfaccurate; available non01ASCIIconsumer rule intentionallyunreceived, GR5-M11-001 pendingindependentresolution')
        clauses.append(record)

dump('source-to-spec.json',{'schema_version':'gr5.review.v1','module':'M11','source_baseline':RC,'specification_baseline':B,'reviewer':'root firsthand','counting_unit':'Bounded semantic source segments; overlap ofconsumerprojections is not unique productfeaturecount','capabilities':capabilities,'data_record_mappings':'data-comparison.json','external_caller_note':'Missing serialized map/events prevent demo reachability; no assertion minigamesabsent'})
dump('spec-to-source.json',{'schema_version':'gr5.review.v1','module':'M11','source_baseline':RC,'specification_baseline':B,'clauses':clauses,'originals':'original-range-comparison.json all12 originals by exactequalranges and fullyread changedranges','scope':'All12 owned formal bodies/appendices plus complete Pokedexprojection ofWP66B andexact M11 rows in3 sharedcatalogues; no signature forforeignUI/storage/testsections'})
base['semantic_completion']='All owned readable body/data/clauses compared; remaining independent counterreview doesnotmean primary unread'
dump('reading-coverage.json',base)
print(json.dumps({'primary_files':sum(x.get('scope_role')=='primary' for x in base['sources']),'capability_units':len(capabilities),'statuses':dict(collections.Counter(x['status'] for x in capabilities)),'inverse_units':len(clauses),'inverse_statuses':dict(collections.Counter(x['status'] for x in clauses)),'not_a_global_completion':True},ensure_ascii=False))
