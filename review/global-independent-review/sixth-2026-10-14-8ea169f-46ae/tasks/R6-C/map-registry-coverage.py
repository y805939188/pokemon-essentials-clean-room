import json,re
from pathlib import Path
b=Path(__file__).parent;facts=[json.loads(x)for x in(b/'forward-map.jsonl').read_text().splitlines()];rev=[json.loads(x)for x in(b/'reverse-map.jsonl').read_text().splitlines()];entries=[]
for kind,source,formal in [('Item','reference/pokemon-essentials/Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb','deliverables/final-specification-set/pokemon-rules/wp50-held-item-effect-coverage.md'),('Ability','reference/pokemon-essentials/Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb','deliverables/final-specification-set/pokemon-rules/wp48-ability-calculation-modifiers.md')]:
 lines=Path(source).read_text().splitlines();families={}
 for i,t in enumerate(lines,1):
  m=re.match(r'^Battle::'+kind+r'Effects::(\w+)\.(add|copy)\((.*)',t)
  if not m:continue
  a=i;z=i
  if not t.rstrip().endswith(')'):
   for j in range(i,len(lines)):
    if (m.group(2)=='copy' and ')' in lines[j]) or lines[j]==')':z=j+1;break
  # For copy, all identities are in its complete short declaration. For add, only the declaration's first identity is counted.
  if m.group(2)=='copy':ids=re.findall(r'(?<!:):([A-Z][A-Z0-9_]*)\b',' '.join(lines[a-1:z]))
  else:ids=re.findall(r'(?<!:):([A-Z][A-Z0-9_]*)\b',m.group(3))[:1]
  families.setdefault(m.group(1),[]).append({'start':a,'end':z,'operation':m.group(2),'ids':ids})
 fl=Path(formal).read_text().splitlines()
 for n,t in enumerate(fl,1):
  m=re.match(r'^\|\s*(\w+)（(\d+)）\s*\|',t)
  if not m:continue
  family=m.group(1);units=families.get(family,[]);direct=sum(x['operation']=='add'for x in units);dest=sum(max(len(x['ids'])-1,0)for x in units if x['operation']=='copy');expect=int(m.group(2));assert direct+dest==expect,(kind,family,direct,dest,expect)
  actual=set(x['ids'][0]for x in units if x['operation']=='add');actual.update(y for x in units if x['operation']=='copy'for y in x['ids'][1:]);formalids=set(re.findall(r'\b[A-Z][A-Z0-9_]+\b',t));assert actual<=formalids,(family,actual-formalids)
  fid=f'R6-C-F{len(facts)+1:03d}';s={'path':source,'start':min(x['start']for x in units),'end':max(x['end']for x in units)};c={'path':formal,'start':n,'end':n,'clause':family+'有界身份/本族复制方向'}
  r={'fact_id':fid,'source':s,'unit':family+'完整登记单位集合','fact':f'本族直接{direct}，复制新增{dest}，展开{direct+dest}个族身份；本轮已全文读每处理器，具体行为必须联同主文的对应入口/消费者，身份计数不当行为执行。','consumer':c,'preconditions':'固定源码文本；copy第一身份为本族来源；跨族同身份分别计数；实际source运行加载未执行。','evidence':'SOURCE_STATIC + TOOL_VALIDATION_TEXT_ONLY','disposition':'MAPPED_NEW_READ','qualification':'IDENTITY_COUNT_AND_DIRECTION_ONLY_BEHAVIOR_PARENT_REQUIRED','aggregate_pass':False};facts.append(r);rev.append({'clause':c,'source':s,'fact_id':fid,'preconditions':r['preconditions'],'verification':r['qualification'],'evidence':r['evidence'],'aggregate_pass':False});entries.append({'kind':kind,'family':family,'fact_id':fid,'source_units':units,'formal':c,'direct':direct,'copy_destinations':dest,'expanded':direct+dest,'new_full_source_read':True,'host_execution':0})
(b/'registry-coverage-map.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n');(b/'forward-map.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n'for x in facts));(b/'reverse-map.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n'for x in rev));print('Exact rows',len(entries),'item total',sum(x['expanded']for x in entries if x['kind']=='Item'),'abilitycalc total',sum(x['expanded']for x in entries if x['kind']=='Ability'))
