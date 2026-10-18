"""Own inert exact current-field reading aid. No reviewed code is executed.

Changed records retain every literal ID, field, meaning, range and status.
Shared complete dictionaries reduce repeated values only. Every decoded object
is checked against its original. Generating an aid grants no reading credit.
"""
import datetime,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent
B=P.parent.parent
begin=datetime.datetime.now(datetime.timezone.utc).isoformat()
ledger=json.loads((P/'reading-ledger.json').read_text());r=ledger['snapshot_payloads'][160]
raw=(B/r['snapshot']).read_bytes();assert hashlib.sha256(raw).hexdigest()==r['sha256']
d=json.loads(raw);expected={'schema','reviewer','all16_backup_paths','generation_warning','behavior'};assert set(d)==expected
pools={'field_meaning_sets':[],'status':[],'changed_bases':[],'activation':[],'semantic_facts':[],'only_id_lists':[]}
lookup={k:{} for k in pools}
def intern(k,v):
 s=json.dumps(v,ensure_ascii=False,separators=(',',':'))
 if s not in lookup[k]:lookup[k][s]=len(pools[k]);pools[k].append(v)
 return lookup[k][s]
headers=[];bindings=[];rebuilt=[]
for b,x in enumerate(d['all16_backup_paths']):
 assert set(x)=={'path','family','generation','records','default_records','exact_byte_equal','only_backup','only_default','changed_records','activation','semantic_facts'}
 h={k:x[k] for k in ['path','family','generation','records','default_records','exact_byte_equal']}
 h.update(only_backup_idx=intern('only_id_lists',x['only_backup']),only_default_idx=intern('only_id_lists',x['only_default']),activation_idx=intern('activation',x['activation']),semantic_facts_idx=intern('semantic_facts',x['semantic_facts']))
 headers.append(h);rows=[];rchanges=[]
 for c in x['changed_records']:
  assert set(c)=={'id','changed_fields','meanings','default_range','backup_range','status'}
  f=intern('field_meaning_sets',[c['changed_fields'],c['meanings']]);s=intern('status',c['status']);base=intern('changed_bases',[c['id'],f,c['default_range'],s]);row=[base,*c['backup_range']];rows.append(row)
  cb=pools['changed_bases'][base];fm=pools['field_meaning_sets'][cb[1]]
  rchanges.append({'id':cb[0],'changed_fields':fm[0],'meanings':fm[1],'default_range':cb[2],'backup_range':row[1:],'status':pools['status'][cb[3]]})
 bindings.append(rows)
 rx={k:h[k] for k in ['path','family','generation','records','default_records','exact_byte_equal']};rx.update(only_backup=pools['only_id_lists'][h['only_backup_idx']],only_default=pools['only_id_lists'][h['only_default_idx']],changed_records=rchanges,activation=pools['activation'][h['activation_idx']],semantic_facts=pools['semantic_facts'][h['semantic_facts_idx']]);rebuilt.append(rx)
assert rebuilt==d['all16_backup_paths']
metadata={k:v for k,v in d.items() if k!='all16_backup_paths'}
lines=['{"exact_root_metadata":'+json.dumps(metadata,ensure_ascii=False,separators=(',',':'))+',','"encoding":"All pools zero-based. changed_bases=[literalID,fieldMeaningsIdx,completeDefaultRange,statusIdx]; backupRows=[baseIdx,backupStart,backupEnd]. Complete original objects reconstructed exactly; no additional semantic or source reading from generation.",']
for key in ['activation','semantic_facts','status','field_meaning_sets','only_id_lists','changed_bases']:
 lines.append(json.dumps(key)+':[')
 for i,value in enumerate(pools[key]):
  if key=='only_id_lists':
   lines.append('[')
   for j in range(0,len(value),12):lines.append(','.join(json.dumps(s,ensure_ascii=False) for s in value[j:j+12])+(',' if j+12<len(value) else ''))
   lines.append(']'+(',' if i+1<len(pools[key]) else ''))
  else:lines.append(json.dumps(value,ensure_ascii=False,separators=(',',':'))+(',' if i+1<len(pools[key]) else ''))
 lines.append('],')
lines.append('"backup_headers":[')
for i,h in enumerate(headers):lines.append(json.dumps(h,ensure_ascii=False,separators=(',',':'))+(',' if i+1<len(headers) else ''))
lines.append('],"ordered_backup_changed_bindings":[')
for i,rows in enumerate(bindings):
 lines.append('[')
 for j,row in enumerate(rows):lines.append(json.dumps(row,separators=(',',':'))+(',' if j+1<len(rows) else ''))
 lines.append(']'+(',' if i+1<len(bindings) else ''))
lines.append(']}')
view='\n'.join(lines)+'\n';json.loads(view)
out=P/'pbs-alternative-complete-exact-components-view.json';out.write_text(view)
manifest={'begin_utc':begin,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'source_index':160,'source_sha256':r['sha256'],'output':out.name,'bytes':len(view.encode()),'lines':len(lines),'sha256':hashlib.sha256(view.encode()).hexdigest(),'all_current_fields_exact_reconstruction':True,'pool_counts':{k:len(v) for k,v in pools.items()},'backup_bindings':len(bindings),'changed_rows':sum(map(len,bindings)),'generation_reading_credit':0,'source_credit':0,'business':'NOT_EXECUTED'}
(P/'pbs-alternative-components-generation.json').write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps(manifest))
