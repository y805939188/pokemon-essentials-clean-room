"""Review-only PBS lexical inventory. No Ruby/reference/game/model execution.
Preserves ordered source records/properties; does not compile or simulate behavior.
Opaque prose fields are hashed in saved artifacts. Numeric and identity atoms may
be recorded to permit data compatibility review; every semantic status starts open.
"""
from pathlib import Path
from collections import Counter,defaultdict
import re,json,hashlib
import review_state as s
TEXT_KEYS={'Name','NamePlural','PortionName','PortionNamePlural','Description','Pokedex','Category','FormName','BeginSpeech','EndSpeechWin','EndSpeechLose','LoseText','StorageCreator','Intro','IntroMorning','IntroAfternoon','IntroEvening','Body','Body1','Body2','BattleRequest','BattleRemind','End'}
def h(b):return hashlib.sha256(b).hexdigest()
def family(p):
 n=p.stem
 if n in ['items_shadow_pkmn','moves_shadow_pkmn','types_shadow_pkmn']:return n.split('_')[0]
 if n.endswith('_pkmn') or n.endswith('_pkmn_single') or n=='battle_tower_pokemon':return 'facility_pokemon'
 if n.endswith('_trainers') or n.endswith('_trainers_single'):return 'facility_trainers'
 return n
all_files=[];unique={};unexpected=[];fields=defaultdict(Counter);marked=[]
for p in sorted((s.REF/'PBS').rglob('*.txt')):
 b=p.read_bytes();blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(); lines=b.decode('utf-8-sig').splitlines();fam=family(p)
 recs=[];current=None; specials=[]
 for i,line in enumerate(lines,1):
  stripped=line.strip()
  if not stripped or stripped.startswith('#'):continue
  m=re.match(r'^\s*\[(.*)\]\s*(?:#.*)?$',line)
  if m:
   if current:current['lines'][1]=i-1
   current={'record_key':m[1],'lines':[i,len(lines)],'properties':[],'raw_rows':[],'semantic_status':'not_reviewed'};recs.append(current);continue
  m=re.match(r'^\s*(\w+)\s*=\s*(.*)$',line)
  if m and current:
   key,val=m[1],m[2];fields[fam][key]+=1
   v={'key':key,'line':i,'value_sha256':h(val.encode()),'semantic_status':'not_reviewed'}
   if key not in TEXT_KEYS:v['data_value']=val
   else:v['text_length']=len(val);v['is_empty']=not val
   marks=[n for n,test in [('hash_suffix','#' in val),('quotes','"' in val),('angle_escape','<<' in val),('trailing_comma',val.endswith(',')),('empty',not val)] if test]
   if marks:v['lexical_markers']=marks;marked.append({'path':str(p.relative_to(s.REF)),'record':current['record_key'],'field':key,'line':i,'markers':marks})
   current['properties'].append(v);continue
  row={'line':i,'sha256':h(stripped.encode()),'semantic_status':'not_reviewed'}
  if fam in ['facility_pokemon','encounters','regional_dexes','map_connections']:row['data_value']=stripped
  else:row['classification']='unexpected_non_property';unexpected.append({'path':str(p.relative_to(s.REF)),'line':i})
  if current:current['raw_rows'].append(row)
  else:specials.append(row)
 info={'path':str(p.relative_to(s.REF)),'version':s.R,'git_blob':blob,'sha256':h(b),'family':fam,'line_count':len(lines),'record_count':len(recs) if recs else len(specials),'records':recs,'unsectioned_rows':specials,'review_extent':'inventory_only','semantic_review_complete':False,'same_blob_as':unique.get(blob)}
 unique.setdefault(blob,info['path']);all_files.append({k:v for k,v in info.items() if k not in ['records','unsectioned_rows']})
 # Per-path ledger retains generation/path context even exact blob duplicates.
 name='pbs-records-'+str(p.relative_to(s.REF/'PBS')).replace('/','--').replace(' ','_')+'.json'
 s.write(name,{'schema_version':'gr5.review.v1',**info})
s.write('pbs-data-inspection.json',{'schema_version':'gr5.review.v1','module':'M01','source_baseline':s.R,'warning':'Full lexical inventory only; per-key source/consumer/spec adjudication required before semantic extent advances. No reference execution.','files':all_files,'unique_blobs':len(unique),'properties_by_family':{k:dict(v) for k,v in fields.items()},'lexical_markers':marked,'unexpected_non_property_rows':unexpected})
print('FILES',len(all_files),'UNIQUE BLOBS',len(unique))
for f in all_files:print(f['family'],f['path'],'records',f['record_count'],'lines',f['line_count'],'same_blob',f['same_blob_as'])
print('FIELD KEYS')
for k,v in fields.items():print(k,','.join(v))
print('unexpected rows',len(unexpected),'marked fields',len(marked))
