"""Own inert, exact current-field component aid. Generation is not reading."""
import datetime,hashlib,json,re
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent.parent;begin=datetime.datetime.now(datetime.timezone.utc).isoformat();l=json.loads((P/'reading-ledger.json').read_text());r=l['snapshot_payloads'][173];raw=(B/r['snapshot']).read_bytes();assert hashlib.sha256(raw).hexdigest()==r['sha256'];d=json.loads(raw)
def canon(x):return json.dumps(x,ensure_ascii=False,separators=(',',':'))
def intern(v,pool):
 if v not in pool:pool.append(v)
 return pool.index(v)
def runs(nums):
 out=[]
 for n in nums:
  if out and n==out[-1][-1]+1:
   if len(out[-1])==1:out[-1].append(n)
   else:out[-1][-1]=n
  else:out.append([n])
 return out
def expand(rs):return [n for z in rs for n in (range(z[0],z[1]+1) if len(z)==2 else z)]
assert set(d)=={'schema','reviewer','source_units','trainer_records','tower_records','cup_peer_records','dispositions','behavior'}
a=d['trainer_records'];fkeys=list(a[0]['fields']);pools={k:[] for k in fkeys};layouts=[];groups=[];bindings=[];units={k:a[0]['fields'][k]['semantic_unit'] for k in fkeys};header={k:a[0][k] for k in ['formal','pool_certificate','status']}
for i,x in enumerate(a):
 assert set(x)=={'id','path','record_order','source_section','source_start','fields','formal','pool_certificate','status'}
 assert x['id']==f'PBF-TRAINER-{i:04d}' and x['record_order']==i and {k:x[k] for k in header}==header
 if not groups or groups[-1]['path']!=x['path']:groups.append({'path':x['path'],'start':i,'count':0,'source_start_formula':'3+8*positionWithinGroup','section':'literalTrainer' if x['source_section']=='Trainer' else 'positionWithinGroup3digits'})
 g=groups[-1];pos=g['count'];g['count']+=1;assert x['source_start']==3+8*pos;assert x['source_section']==('Trainer' if g['section']=='literalTrainer' else f'{pos:03d}')
 layout=[[k,v['line']-x['source_start']] for k,v in x['fields'].items()];li=intern(layout,layouts); assert set(x['fields'])==set(fkeys)
 vals=[]
 for k in fkeys:
  v=x['fields'][k];assert set(v)=={'line','value','semantic_unit'} and v['semantic_unit']==units[k];vals.append(intern(v['value'],pools[k]))
 bindings.append([li,*vals]);back={'id':f'PBF-TRAINER-{i:04d}','path':g['path'],'record_order':i,'source_section':'Trainer' if g['section']=='literalTrainer' else f'{pos:03d}','source_start':3+8*pos,'fields':{k:{'line':3+8*pos+delta,'value':pools[k][vals[fkeys.index(k)]],'semantic_unit':units[k]} for k,delta in layout},**header};assert back==x
poolruns=[]
for s in pools['PokemonNos']:
 assert re.fullmatch('[0-9]+(?:,[0-9]+)*',s);nums=[int(x) for x in s.split(',')];rs=runs(nums);assert ','.join(map(str,expand(rs)))==s;poolruns.append(rs)
view={'qualification':'All current173 JSON fields represented exactly. All literal value dictionaries and ordered bindings require actual reading; numeric candidate runs are inclusive sequences, preserve order/duplicates, not set membership. Source-unit assertions are carrier mappings, not independently checked source definitions/each handler/pool runtime. Generation0reading/source/atomic credit.','source':{k:r[k] for k in ['original_path','snapshot','bytes','sha256','git_blob','captured_utc']},'root_metadata':{k:v for k,v in d.items() if k not in ['source_units','trainer_records','tower_records']},'complete31_source_units':d['source_units'],'trainer_common_header':header,'trainer_groups':groups,'trainer_field_order_in_binding':fkeys,'trainer_complete_field_semantic_units':units,'trainer_complete_line_layouts':layouts,'trainer_value_dictionaries_except_candidate_pool':{k:v for k,v in pools.items() if k!='PokemonNos'},'trainer_candidate_pool_values_inclusive_runs_preserve_order_duplicates':poolruns,'trainer_complete1600_bindings':[b for b in bindings]}
t=d['tower_records'];tk=list(t[0]['source_fields']);tp={k:[] for k in tk};tb=[];th={k:t[0][k] for k in ['path','subassertions','formal','status']}
for i,x in enumerate(t):
 assert set(x)=={'id','path','line','index','source_fields','subassertions','formal','status'} and x['id']==f'PBF-TOWER-{i:03d}' and x['index']==i and x['line']==i+3 and {k:x[k] for k in th}==th and list(x['source_fields'])==tk
 vs=[intern(x['source_fields'][k],tp[k]) for k in tk];tb.append(vs);assert {'id':f'PBF-TOWER-{i:03d}','line':i+3,'index':i,'source_fields':{k:tp[k][vs[j]] for j,k in enumerate(tk)},**th}==x
view.update(tower_common_header=th,tower_encoding='row ordinal i -> id PBF-TOWER-i padded3, indexi,linei+3; exact five field value dictionaries below in field order. No EV/move reordering.',tower_field_order=tk,tower_complete_value_dictionaries=tp,tower_complete882_bindings=tb)
lines=['{'];ks=list(view)
for k in ks:
 v=view[k]
 if isinstance(v,list):
  lines.append(canon(k)+':[')
  for i,x in enumerate(v):lines.append(canon(x)+(',' if i+1<len(v) else ''))
  lines.append(']'+(',' if k!=ks[-1] else ''))
 elif isinstance(v,dict) and k in ['trainer_value_dictionaries_except_candidate_pool','tower_complete_value_dictionaries']:
  lines.append(canon(k)+':{'); sub=list(v)
  for sk in sub:
   lines.append(canon(sk)+':[')
   for i,x in enumerate(v[sk]):lines.append(canon(x)+(',' if i+1<len(v[sk]) else ''))
   lines.append(']'+(',' if sk!=sub[-1] else ''))
  lines.append('}'+(',' if k!=ks[-1] else ''))
 else:lines.append(canon(k)+':'+canon(v)+(',' if k!=ks[-1] else ''))
lines.append('}');data=('\n'.join(lines)+'\n').encode();assert json.loads(data)==view;out=P/'pbs173-complete-exact-components-view.json';out.write_bytes(data);m={'begin_utc':begin,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'source_index':173,'source_sha256':r['sha256'],'output':out.name,'bytes':len(data),'lines':len(lines),'sha256':hashlib.sha256(data).hexdigest(),'source_units':31,'trainers':len(a),'tower_records':len(t),'all_current_objects_exactly_reconstructed':True,'generation_reading_credit':0};(P/'pbs173-complete-components-generation.json').write_text(json.dumps(m,indent=2)+'\n');print(json.dumps(m))
