import json,re,hashlib
from pathlib import Path
b=Path(__file__).parent;R='reference/pokemon-essentials/Data/Scripts/011_Battle/';D='deliverables/final-specification-set/test-catalog/';rows=[]
def S(p,a,z):return {'path':R+p,'start':a,'end':z}
B='001_Battle/';T='002_Battler/';O='007_Other battle code/';C='003_Move/';U='004_Scene/'
# A hand-selected consumer map by vector section; each printed row was actually read in full before this expansion.
# Identity-specific handlers are added below with exact units. This is static audit data, not executable combat behavior.
core={
'CM':[S(B+'009_Battle_CommandPhase.rb',5,265),S(B+'004_Battle_ActionAttacksPriority.rb',5,279),S(T+'009_Battler_UseMoveSuccessChecks.rb',10,302),S(T+'007_Battler_UseMove.rb',5,244)],
'SW':[S(B+'005_Battle_ActionSwitching.rb',9,468),S(B+'007_Battle_ActionRunning.rb',5,159),S(B+'001_Battle.rb',602,641)],
'G':[S(B+'003_Battle_ExpAndMoveLearning.rb',5,271),S(O+'009_Battle_ItemEffects.rb',1693,1748)],
'R':[S(B+'011_Battle_EndOfRoundPhase.rb',5,781),S(T+'002_Battler_Initialize.rb',93,280)],
'E':[S(B+'002_Battle_StartAndEnd.rb',405,516),S(O+'005_Battle_CatchAndStoreMixin.rb',5,107)],
'W':[S(B+'001_Battle.rb',694,779),S(B+'011_Battle_EndOfRoundPhase.rb',5,77),S(T+'001_Battle_Battler.rb',535,566)],
'T':[S(B+'001_Battle.rb',780,815),S(B+'011_Battle_EndOfRoundPhase.rb',471,509),S(T+'001_Battle_Battler.rb',499,517)],
'F':[S(B+'011_Battle_EndOfRoundPhase.rb',437,470),S(O+'002_Battle_ActiveField.rb',1,88)],
'S':[S(B+'011_Battle_EndOfRoundPhase.rb',135,155),S(B+'011_Battle_EndOfRoundPhase.rb',395,436)],
'H':[S(B+'005_Battle_ActionSwitching.rb',425,468),S(T+'003_Battler_ChangeSelf.rb',5,36),S(T+'005_Battler_StatStages.rb',9,300)],
'P':[S(B+'011_Battle_EndOfRoundPhase.rb',78,133),S(B+'005_Battle_ActionSwitching.rb',394,424),S(B+'001_Battle.rb',602,641),S(T+'002_Battler_Initialize.rb',93,280)],
'U04-RF':[S(B+'006_Battle_ActionUseItem.rb',34,76),S(B+'006_Battle_ActionUseItem.rb',87,149),S(B+'009_Battle_CommandPhase.rb',5,27),S(T+'003_Battler_ChangeSelf.rb',64,103),S(B+'002_Battle_StartAndEnd.rb',480,516)],
'R5-U04-FH':[S(T+'007_Battler_UseMove.rb',154,215),S(T+'009_Battler_UseMoveSuccessChecks.rb',183,302),S(B+'011_Battle_EndOfRoundPhase.rb',597,781)],
'R5-U04-MET':[S(T+'007_Battler_UseMove.rb',216,244),S(T+'002_Battler_Initialize.rb',215,215)],
'R5-U04-RANK':[S(B+'002_Battle_StartAndEnd.rb',16,246),S(B+'005_Battle_ActionSwitching.rb',228,288),S(T+'002_Battler_Initialize.rb',93,280)],
'R5-U04-ERR':[S(T+'007_Battler_UseMove.rb',5,59),S(B+'010_Battle_AttackPhase.rb',102,175),S(T+'007_Battler_UseMove.rb',154,762)],
'TD':[S(C+'003_Move_UsageCalculations.rb',5,484),S(C+'002_Move_Usage.rb',163,238),S(T+'003_Battler_ChangeSelf.rb',5,128)],
'SS':[S(T+'004_Battler_Statuses.rb',11,575),S(T+'005_Battler_StatStages.rb',5,387),S(T+'001_Battle_Battler.rb',248,276)],
'AB':[S(T+'001_Battle_Battler.rb',248,455),S(C+'003_Move_UsageCalculations.rb',5,484),S(T+'004_Battler_Statuses.rb',25,214),S(T+'005_Battler_StatStages.rb',9,300)],
'HI':[S(T+'006_Battler_AbilityAndItem.rb',212,476),S(C+'003_Move_UsageCalculations.rb',87,484),S(T+'010_Battler_UseMoveTriggerEffects.rb',5,218)],
'CP':[S(O+'005_Battle_CatchAndStoreMixin.rb',5,262),S(O+'010_Battle_PokeBallEffects.rb',4,198)],
'AB-PHASE':[S(T+'006_Battler_AbilityAndItem.rb',5,211),S(T+'010_Battler_UseMoveTriggerEffects.rb',5,218),S(B+'005_Battle_ActionSwitching.rb',303,375),S(B+'011_Battle_EndOfRoundPhase.rb',597,781)]}
unit=[json.loads(x)for x in(b/'source-unit-index.jsonl').read_text().splitlines()];handler=[]
for u in unit:
 if u['unit_kind'].startswith('handler'):
  content='\n'.join(Path(u['path']).read_text().splitlines()[u['start_line']-1:u['end_line']]);m=re.search(r'\.(?:add|copy)\((.*)',content,re.S)
  ids=re.findall(r'(?<!:):([A-Z][A-Z0-9_]*)\b',m.group(1)) if m else []
  if u['unit_kind']=='handler-add':ids=ids[:1]
  handler.append((ids,{'path':u['path'],'start':u['start_line'],'end':u['end_line'],'unit_id':u['unit_id']}))
files=['combat-requirements-wp39-40-41-42-45.md','combat-requirements-wp49-51-52.md','pokemon-rules-wp31-32-37-38.md','pokemon-rules-wp43-44-46-48-50.md']
ca=[json.loads(x)for x in(b.parent/'R6-CA/catalog-matrix.jsonl').read_text().splitlines()];ca={q['line']:q for q in ca if q['owned_ai_case']}
for file in files:
 p=D+file;lines=Path(p).read_text().splitlines()
 for n,t in enumerate(lines,1):
  m=re.match(r'^\|\s*([A-Z][A-Za-z0-9-]+)\s*\|',t)
  if not m or m.group(1)=='ID':continue
  id=m.group(1);owner='R6-C';sources=[];note='本轮整行输入/推导/排除门已读，以具名真实入口静态核对；不产生参考或模型执行。';status='STATIC_VECTOR_ENTRY_PREMISES_REVIEWED'
  if file.startswith('combat-requirements-wp49-51'):
   if n>=43:
    receipt=ca.get(n);assert receipt and receipt['status']=='LOCAL_VECTOR_ASSESSED_WITH_PRECONDITIONS',(id,n,receipt)
    q={'id':id,'path':p,'line':n,'owner':'R6-CA','status':'DELEGATE_RESULT_RECEIVED_PREMISES_REVIEWED_BY_CA','evidence':'R6-CA_SOURCE_STATIC + DERIVED_VECTOR','receipt':{'path':str(b.parent/'R6-CA/catalog-matrix.jsonl'),'id':receipt['id'],'line':n,'derivation_records':receipt['derivation_records']},'personally_new_formal_read':True,'personally_new_source_read_claim':False,'runtime_claim':False};rows.append(q);continue
   key='AB-PHASE';sources=core[key]
  elif file.startswith('pokemon-rules-wp31'):
   if id.startswith('CP'):sources=core['CP']
   else:owner='R6-K/R6-O';status='SHARED_CONTEXT_VECTOR_JOIN_PENDING';note='整篇目录实际已读，进化/世界源由K/O主审，未冒称本人核该生产者。'
  elif file.startswith('pokemon-rules-wp43'):
   if id.startswith('MH')or id.startswith('U04-MH')or id.startswith('R5-U04'):
    owner='R6-CM';status='MOVE_PRODUCER_JOIN_PENDING';note='当前已读core消费者；具体Move/unknown fallback生产者待CM最终整合。'
   elif id.startswith('U04-HI'):sources=core['HI']+core['R5-U04-ERR'];owner='R6-C/R6-CM';status='MOVE_PRODUCER_JOIN_PENDING';note='持物/续击/调度亲核，NaturalGift变化生产者需CM接合。'
   else:
    key=next((k for k in['TD','SS','AB','HI']if id.startswith(k)),None)
    assert key,(p,n,id);sources=core[key]
  else:
   key=next((k for k in ['U04-RF','R5-U04-FH','R5-U04-MET','R5-U04-RANK','R5-U04-ERR','CM','SW','G','R','E','W','T','F','S','H','P']if id.startswith(k)),None)
   if id.startswith('BC'):
    k=int(id.split('-')[-1]);
    if 13<=k<=21:sources=[S(B+'002_Battle_StartAndEnd.rb',16,165),S(B+'001_Battle.rb',185,577),S(O+'006_Battle_Clauses.rb',66,101)]
    else:owner='R6-O';status='WORLD_WRAPPER_JOIN_PENDING';note='完整formal向量亲读，入口/音频/生成覆写源在O本轮主审。'
   elif key:sources=core[key]
   else:owner='R6-CM';status='FIELD_PRODUCER_JOIN_PENDING';note='清场特殊招式producer由CM审，C消费者全读。'
   if id in['CM-17','CM-18','CM-21']or id.startswith('SW-')and 19<=int(id.split('-')[-1])<=24 or key in['F','S']:
    owner='R6-C/R6-CM';status='MOVE_PRODUCER_JOIN_PENDING'
   if id=='CM-06':owner='R6-C/R6-K';status='EXTERNAL_SHADOW_BINDING_RECEIVED_CORE_REVIEWED';note='K本轮Shadow覆写196–220实际持久对象/非倒下Hyper绑定已接合，C普通核心服从门已全文；K新读与C新读分归属。'
   if id.startswith('E')and not id.startswith('R5-')and n>=150:owner='R6-C/R6-O/R6-K';status='WORLD_END_JOIN_PENDING'
   if id.startswith('R5-U04-ERR'):owner='R6-C/R6-CM';status='MOVE_PRODUCER_JOIN_PENDING'
  tokens=set(re.findall(r'\b[A-Z][A-Z0-9_]+\b',t));specific=[loc for ids,loc in handler if tokens.intersection(ids)]
  if id.startswith('CP2') and id in['CP20','CP21','CP22']:sources += [S(O+'005_Battle_CatchAndStoreMixin.rb',35,80),S(B+'002_Battle_StartAndEnd.rb',480,516)]
  if id=='HI10':sources += [S(T+'009_Battler_UseMoveSuccessChecks.rb',10,18),S(B+'011_Battle_EndOfRoundPhase.rb',312,345)];note+=' C002普通选择/预先合法登记执行的反例扩展待root裁决，原本地字段预期正确。'
  rows.append({'id':id,'path':p,'line':n,'owner':owner,'status':status,'source_pipeline':sources,'identity_specific_source_units':specific,'evidence':'SOURCE_STATIC + DERIVED_VECTOR','personally_new_formal_read':True,'runtime_claim':False,'assessment':note,'literal_inputs_hash':hashlib.sha256(t.encode()).hexdigest()})
(b/'test-vector-map.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n'for x in rows));from collections import Counter;print(json.dumps({'cases':len(rows),'statuses':dict(Counter(q['status']for q in rows))},ensure_ascii=False,indent=2))
