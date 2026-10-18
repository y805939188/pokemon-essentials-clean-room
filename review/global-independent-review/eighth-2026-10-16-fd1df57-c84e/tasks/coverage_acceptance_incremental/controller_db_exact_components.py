"""Own inert exact component aid for controller DB evidence carrier.

Only raw-row SHA256 values are separately retained as recovery identities.
Every nonhash metadata field and ordered GUID/name/mapping/pattern/offset binding
is represented for actual reading. Checks restore every original current object;
this is not native registration/selector/program semantic evidence.
"""
import datetime,hashlib,json,re
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent.parent
start=datetime.datetime.now(datetime.timezone.utc).isoformat();l=json.loads((P/'reading-ledger.json').read_text());r=l['snapshot_payloads'][205];raw=(B/r['snapshot']).read_bytes();assert hashlib.sha256(raw).hexdigest()==r['sha256'];d=json.loads(raw)
assert set(d)=={'source_commit','source_path','source_bytes','source_sha256','offset','length','end_exclusive','region_sha256','decoder','record_count','line_count','pattern_count','platform_counts','rows','qualification'}
pools=[];lookup={};rows=[];hashes=[];rebuilt=[]
basekeys={'line','start','end_exclusive','raw_bytes','sha256','text','reading_status','kind'}
for i,x in enumerate(d['rows']):
 assert x['line']==i+1 and re.fullmatch('[0-9a-f]{64}',x['sha256']);hashes.append({'row':i,'sha256':x['sha256'],'purpose':'RAW_LINE_RECOVERY_IDENTITY_ONLY_NOT_PERSONALLY_LITERAL_READ'})
 assert x['reading_status']=='UNREAD_FOR_NEW_READER'
 if x['kind']=='mapping':
  assert set(x)==basekeys|{'record_index','guid','name','mapping','pattern_group'}
  parts=x['text'].split(',');assert parts[:2]==[x['guid'],x['name']]
  suffix=','.join(parts[2:]);mapping=[v.split(':',1) for v in parts[2:] if v];assert mapping==x['mapping']
  key=json.dumps([suffix,mapping,x['pattern_group']],separators=(',',':'))
  if key not in lookup:lookup[key]=len(pools);pools.append([suffix,mapping,x['pattern_group']])
  j=lookup[key];row=[x['start'],x['end_exclusive'],x['raw_bytes'],x['record_index'],x['guid'],x['name'],j];rows.append(row)
  z={'line':i+1,'start':row[0],'end_exclusive':row[1],'raw_bytes':row[2],'sha256':x['sha256'],'text':row[4]+','+row[5]+','+pools[j][0],'reading_status':'UNREAD_FOR_NEW_READER','kind':'mapping','record_index':row[3],'guid':row[4],'name':row[5],'mapping':pools[j][1],'pattern_group':pools[j][2]}
 else:
  assert x['kind']=='comment_or_empty' and set(x)==basekeys
  row=[x['start'],x['end_exclusive'],x['raw_bytes'],-1,x['text']];rows.append(row);z={'line':i+1,'start':row[0],'end_exclusive':row[1],'raw_bytes':row[2],'sha256':x['sha256'],'text':row[4],'reading_status':'UNREAD_FOR_NEW_READER','kind':'comment_or_empty'}
 assert z==x;rebuilt.append(z)
assert rebuilt==d['rows'];assert len(pools)==d['pattern_count']
side=P/'controller-db-row-sha-recovery-only.json';side.write_text(json.dumps(hashes,indent=2)+'\n');sraw=side.read_bytes()
lines=['{"complete_nonrow_metadata":'+json.dumps({k:v for k,v in d.items() if k!='rows'},ensure_ascii=False,separators=(',',':'))+',','"encoding":"All pools zero based. mapping_patterns rows=[complete literal suffix,complete ordered mapping pair array,original pattern_group]. Record rows=[start,endExclusive,rawBytes,recordIndex,literalGUID,literalName,patternIdx]; comment/empty rows=[start,endExclusive,rawBytes,-1,fullText]. Row ordinal+1 is original line. All rows retain original reading_status UNREAD_FOR_NEW_READER. text=GUID+comma+name+comma+suffix. Raw row SHA retained separately recovery-only, not literal read or semantic proof.",','"row_sha_recovery_identity":'+json.dumps({'path':side.name,'bytes':len(sraw),'sha256':hashlib.sha256(sraw).hexdigest(),'rows':len(hashes),'all_values_strict_lowercase64hex':True,'literal_values_read':False},separators=(',',':'))+',','"mapping_patterns":[']
for i,p in enumerate(pools):lines.append(json.dumps(p,ensure_ascii=False,separators=(',',':'))+(',' if i+1<len(pools) else ''))
lines.append('],"ordered_rows":[')
for i,row in enumerate(rows):lines.append(json.dumps(row,ensure_ascii=False,separators=(',',':'))+(',' if i+1<len(rows) else ''))
lines.append(']}');view='\n'.join(lines)+'\n';json.loads(view);out=P/'controller-db-complete-nonhash-components-view.json';out.write_text(view)
m={'begin_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'source_index':205,'source_sha256':r['sha256'],'output':out.name,'bytes':len(view.encode()),'lines':len(lines),'sha256':hashlib.sha256(view.encode()).hexdigest(),'all_current_objects_exact_reconstruction':True,'nonhash_fields_for_reading':True,'mapping_patterns':len(pools),'rows':len(rows),'row_sha_purpose_only':len(hashes),'generation_reading_credit':0,'source_credit':0,'business':'NOT_EXECUTED'}
(P/'controller-db-components-generation.json').write_text(json.dumps(m,indent=2)+'\n');print(json.dumps(m))
