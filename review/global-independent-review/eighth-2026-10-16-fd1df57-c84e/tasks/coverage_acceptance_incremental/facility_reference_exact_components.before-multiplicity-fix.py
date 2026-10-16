"""Own static exact component aid for the finite PBS-reference carrier.

Order-preserving integer runs and complete ordered species arrays retain data.
Redundant reverse-reference trainer_positions are reconstructed from the fully
represented candidate memberships and asserted equal to every original value.
That equality is carrier identity, not source meaning or behavior acceptance.
"""
import datetime,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent.parent
begin=datetime.datetime.now(datetime.timezone.utc).isoformat()
l=json.loads((P/'reading-ledger.json').read_text());r=l['snapshot_payloads'][53];raw=(B/r['snapshot']).read_bytes();assert hashlib.sha256(raw).hexdigest()==r['sha256'];d=json.loads(raw)
assert set(d)=={'schema','utc','reviewer','evidence_level','execution','source_semantics','summary','trainers','row_references'}
def encode(a):
 out=[];i=0
 while i<len(a):
  start=a[i];end=start;i+=1
  while i<len(a) and a[i]==end+1:end=a[i];i+=1
  out.append(str(start) if start==end else str(start)+':'+str(end))
 return ','.join(out)
def decode(s):
 out=[]
 for x in s.split(',') if s else []:
  v=x.split(':');out.extend([int(v[0])] if len(v)==1 else range(int(v[0]),int(v[1])+1))
 return out
pools={'candidate_runs':[],'source_semantic_status':[],'consumer_fact':[],'derived_fancy30_total':[]}
look={k:{} for k in pools}
def intern(k,v):
 key=json.dumps(v,ensure_ascii=False,separators=(',',':'))
 if key not in look[k]:look[k][key]=len(pools[k]);pools[k].append(v)
 return look[k][key]
groups=[];gindex={};rebuilt=[]
for t in d['trainers']:
 assert set(t)=={'trainer_file','trainer_position','section','section_line','pokemon_file','candidate_numbers','candidate_count','source_semantic_status','consumer_fact','derived_fancy30_total'}
 key=(t['trainer_file'],t['pokemon_file'])
 if key not in gindex:gindex[key]=len(groups);groups.append({'trainer_file':key[0],'pokemon_file':key[1],'rows':[]})
 g=groups[gindex[key]];position=len(g['rows']);assert t['trainer_position']==position and t['section']==str(position).zfill(3)
 encoded=encode(t['candidate_numbers']);assert decode(encoded)==t['candidate_numbers'] and len(t['candidate_numbers'])==t['candidate_count']
 row=[t['section_line'],intern('candidate_runs',encoded),intern('source_semantic_status',t['source_semantic_status']),intern('consumer_fact',t['consumer_fact']),intern('derived_fancy30_total',t['derived_fancy30_total'])];g['rows'].append(row)
 rebuilt.append({'trainer_file':key[0],'trainer_position':position,'section':str(position).zfill(3),'section_line':row[0],'pokemon_file':key[1],'candidate_numbers':decode(pools['candidate_runs'][row[1]]),'candidate_count':len(decode(pools['candidate_runs'][row[1]])),'source_semantic_status':pools['source_semantic_status'][row[2]],'consumer_fact':pools['consumer_fact'][row[3]],'derived_fancy30_total':pools['derived_fancy30_total'][row[4]]})
assert rebuilt==d['trainers']
refgroups=[];refrebuilt={}
for file,rows in d['row_references'].items():
 represented=[];rr=[]
 for i,x in enumerate(rows):
  assert x['index']==i and x['line']==i+3
  q={'index':i,'line':i+3,'species':x['species']}
  if 'trainer_positions' in x:
   assert set(x)=={'index','line','species','trainer_positions'}
   q['trainer_positions']=[t['trainer_position'] for t in rebuilt if t['pokemon_file']==file and i in t['candidate_numbers']]
  else:assert set(x)=={'index','line','species','current_selected'};q['current_selected']=False;assert x['current_selected'] is False
  assert q==x;rr.append(q);represented.append(x['species'])
 refgroups.append({'pokemon_file':file,'reverse_field':'trainer_positions derived from all corresponding fully represented candidate memberships in source trainer order' if 'trainer_positions' in rows[0] else 'current_selected:false','species_order':represented});refrebuilt[file]=rr
assert refrebuilt==d['row_references']
lines=['{"exact_root_metadata":'+json.dumps({k:v for k,v in d.items() if k not in ['trainers','row_references']},ensure_ascii=False,separators=(',',':'))+',','"encoding":"All pools zero based. candidate_runs are exact ordered integers: comma separates entries; a:b expands every integer inclusively, preserving original order and duplicates. Each trainer group row ordinal gives trainer_position and exact3-digit section; rows=[section_line,candidateRunIdx,statusIdx,consumerIdx,derivedIdx]; count=len(decoded candidates). Each species ordinal gives original index and line=index+3. Reverse trainer_positions exactly derived from represented full memberships; not source reading or semantic proof.",']
for k in ['source_semantic_status','consumer_fact','derived_fancy30_total','candidate_runs']:
 lines.append(json.dumps(k)+':[')
 for i,v in enumerate(pools[k]):lines.append(json.dumps(v,ensure_ascii=False,separators=(',',':'))+(',' if i+1<len(pools[k]) else ''))
 lines.append('],')
lines.append('"trainer_groups":[')
for i,g in enumerate(groups):
 lines.append('{"trainer_file":'+json.dumps(g['trainer_file'])+',"pokemon_file":'+json.dumps(g['pokemon_file'])+',"rows":[')
 for j,row in enumerate(g['rows']):lines.append(json.dumps(row,separators=(',',':'))+(',' if j+1<len(g['rows']) else ''))
 lines.append(']}'+(',' if i+1<len(groups) else ''))
lines.append('],"reference_species_groups":[')
for i,g in enumerate(refgroups):
 lines.append('{"pokemon_file":'+json.dumps(g['pokemon_file'])+',"reverse_field":'+json.dumps(g['reverse_field'])+',"species_order":[')
 a=g['species_order']
 for j in range(0,len(a),15):lines.append(','.join(json.dumps(s) for s in a[j:j+15])+(',' if j+15<len(a) else ''))
 lines.append(']}'+(',' if i+1<len(refgroups) else ''))
lines.append(']}');view='\n'.join(lines)+'\n';json.loads(view);out=P/'facility-reference-complete-exact-components-view.json';out.write_text(view)
m={'begin_utc':begin,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'source_index':53,'source_sha256':r['sha256'],'output':out.name,'bytes':len(view.encode()),'lines':len(lines),'sha256':hashlib.sha256(view.encode()).hexdigest(),'all_current_fields_exact_reconstruction':True,'pools':{k:len(v) for k,v in pools.items()},'trainer_groups':len(groups),'trainer_rows':len(rebuilt),'reverse_rows':sum(len(x) for x in refrebuilt.values()),'generation_reading_credit':0,'source_credit':0,'business':'NOT_EXECUTED'}
(P/'facility-reference-components-generation.json').write_text(json.dumps(m,indent=2)+'\n');print(json.dumps(m))
