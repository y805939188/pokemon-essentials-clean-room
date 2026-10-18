"""Own strict locator-metadata purpose component display, no source reading.
All rule-bearing root/manual fields remain literal. Only 64hex text identities
are kept in an exact recovery sidecar and explicitly NOT personally read.
Nonhash locator classifications, scopes, manual bindings and locations are shown
as exact consecutive runs; complete decode equals original. No coverage credit.
"""
import json,hashlib,datetime,re
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent.parent;start=datetime.datetime.now(datetime.timezone.utc).isoformat();r=json.loads((P/'reading-ledger.json').read_text())['snapshot_payloads'][167];raw=(B/r['snapshot']).read_bytes();assert len(raw)==r['bytes'] and hashlib.sha256(raw).hexdigest()==r['sha256'];j=json.loads(raw);rows=j['structural_locators'];keys={'path','line','text_sha256','classification','applicable_manual_units','scope_status','no_line_count_as_semantic_proof'};assert len(rows)==1064 and all(set(x)==keys for x in rows);assert all(re.fullmatch('[a-f0-9]{64}',x['text_sha256']) and x['no_line_count_as_semantic_proof'] is True and isinstance(x['line'],int) for x in rows);manual={x['id'] for x in j['manual_semantic_subassertion_units']};assert all(set(x['applicable_manual_units'])<=manual for x in rows)
paths=[];runs=[];hashes=[]
for i,x in enumerate(rows):
 if x['path'] not in paths:paths.append(x['path'])
 signature=[paths.index(x['path']),x['classification'],x['applicable_manual_units'],x['scope_status']];hashes.append(x['text_sha256'])
 if runs and runs[-1][4]==signature and runs[-1][1]+1==i and runs[-1][3]+1==x['line']:runs[-1][1]=i;runs[-1][3]=x['line']
 else:runs.append([i,i,x['line'],x['line'],signature])
rebuilt=[]
for a,b,c,d,s in runs:
 assert b-a==d-c
 pi,classification,units,scope=s
 for i,n in zip(range(a,b+1),range(c,d+1)):rebuilt.append({'path':paths[pi],'line':n,'text_sha256':hashes[i],'classification':classification,'applicable_manual_units':units,'scope_status':scope,'no_line_count_as_semantic_proof':True})
assert rebuilt==rows
hname='pbs-battle-locator-hash-recovery-only.json';assert not(P/hname).exists();hraw=(json.dumps(hashes,separators=(',',':'))+'\n').encode();(P/hname).write_bytes(hraw)
v={'schema':'gr8-mixed-operative-full-and-strict-locator-purpose/v1','source':{k:r[k] for k in ['original_path','snapshot','bytes','sha256','git_blob','captured_utc']},'qualification':'All operative/manual/root fields literal below. Locator rows contain no source body, clause body, premise or positive semantic assertion: only location/64hex text identity/classification/scope/manual routing and explicit true no-line-count proof flag. Every nonhash locator field represented below and requires actual reading.1064 unique hash literal strings NOT personally read; exact recovery only. No underlying source/formal/atomic/locator-row reading credit.','all_nonlocator_root_and_operative_fields':{k:v for k,v in j.items() if k!='structural_locators'},'strict_all1064_keyset':sorted(keys),'constant_every_locator_no_line_count_as_semantic_proof':True,'path_dictionary':paths,'run_columns':['first_original_row_inclusive','last_original_row_inclusive','first_line_inclusive','last_line_inclusive','signature'],'signature_columns':['path_index','classification','applicable_manual_units_in_original_order','scope_status'],'exact_ordered_runs':runs,'typed_hash_recovery':{'file':hname,'bytes':len(hraw),'sha256':hashlib.sha256(hraw).hexdigest(),'count':len(hashes),'strict_each_type':'lowercase64hex','literal_read':False,'source_read_credit':0}}
lines=['{']
for i,(k,x) in enumerate(v.items()):
 suffix=',' if i<len(v)-1 else ''
 if k=='exact_ordered_runs':lines+=[' '+json.dumps(k)+': [']+['  '+json.dumps(row,ensure_ascii=False,separators=(',',':'))+(',' if q<len(x)-1 else '') for q,row in enumerate(x)]+[' ]'+suffix]
 else:lines+=[' '+json.dumps(k)+': '+json.dumps(x,ensure_ascii=False,indent=1)+suffix]
lines+=['}'];data=('\n'.join(lines)+'\n').encode();assert json.loads(data)==v;name='pbs-battle-reverse-complete-operative-locator-purpose-view.json';assert not(P/name).exists();(P/name).write_bytes(data);proof={'begin_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'source_index':167,'source_sha256':r['sha256'],'output':name,'bytes':len(data),'lines':len(data.splitlines()),'sha256':hashlib.sha256(data).hexdigest(),'all1064_rows_exact_reconstruction_with_hash_sidecar':True,'run_count':len(runs),'hashes_personally_literal_read':False,'generation_reading_credit':0,'source_credit':0,'business':'NOT_EXECUTED'};(P/'pbs-battle-reverse-operative-locator-purpose-generation.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof))
