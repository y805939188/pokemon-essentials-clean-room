"""Own inert complete field decomposition. Every full original text, explicit
subassertion substring span, metadata dictionary and row binding needs reading.
Exact reconstruction alone grants no reading or semantic/source credit.
"""
from pathlib import Path
import datetime,hashlib,json
P=Path(__file__).resolve().parent;B=P.parent.parent;t=datetime.datetime.now(datetime.timezone.utc).isoformat();r=json.loads((P/'reading-ledger.json').read_text())['snapshot_payloads'][56];raw=(B/r['snapshot']).read_bytes();assert len(raw)==r['bytes'] and hashlib.sha256(raw).hexdigest()==r['sha256'];d=json.loads(raw);q=lambda x:json.dumps(x,ensure_ascii=False,separators=(',',':'));texts=[];tl={};tails=[];ml={};rows=[];rebuilt=[]
for x in d['units']:
 assert x['id']==f"{x['formal_id']}-L{x['line']:04d}"
 ti=-1
 if 'text' in x:
  assert 'subassertion_locators' in x
  s=x['text'];spans=[];pos=0
  for a in x['subassertion_locators']:
   assert set(a)=={'local','text'}
   start=s.find(a['text'],pos);assert start>=0;end=start+len(a['text']);spans.append([a['local'],start,end]);pos=end
  tr={'complete_original_text':s,'subassertion_columns':['original_local','start_unicode0','end_exclusive_unicode0'],'exact_original_subassertion_spans':spans};sig=q(tr)
  if sig not in tl:tl[sig]=len(texts);texts.append(tr)
  ti=tl[sig]
 else:assert 'subassertion_locators' not in x
 tail={k:v for k,v in x.items() if k not in ['id','formal_id','line','text','subassertion_locators']};sig=q(tail)
 if sig not in ml:ml[sig]=len(tails);tails.append(tail)
 mi=ml[sig];rows.append([x['formal_id'],x['line'],ti,mi]);z={'id':f"{x['formal_id']}-L{x['line']:04d}",'formal_id':x['formal_id'],'line':x['line'],**tails[mi]}
 if ti>=0:
  tr=texts[ti];s=tr['complete_original_text'];z.update(text=s,subassertion_locators=[{'local':a,'text':s[b:c]} for a,b,c in tr['exact_original_subassertion_spans']])
 rebuilt.append(z)
assert rebuilt==d['units']
view={'schema':'gr8-fac1156-exact-current-components/v1','qualification':'Exact current carrier fields, not source/fullformal/atomic acceptance. Row ID is original formal_id + -L + original decimal line zero-padded4. Text index -1 preserves original absence of text/subassertions. All text literal, all explicit substring spans, metadata and each binding require reading. Span positions are Unicode string indices, never source lines.','source':{k:r[k] for k in ['original_path','snapshot','bytes','sha256','git_blob','captured_utc']},'complete_other_root_fields':{k:v for k,v in d.items() if k!='units'},'complete_text_and_subassertion_components':texts,'complete_metadata_dictionary':tails,'row_columns':['formal_id','original_formal_line','text_components_index_minus1_absent','metadata_index'],'ordered_rows':rows}
lines=['{']
for i,(k,v) in enumerate(view.items()):
 suffix=',' if i<len(view)-1 else ''
 if isinstance(v,list) and v and isinstance(v[0],(list,dict)):
  lines.append(' '+q(k)+': [');lines.extend('  '+q(x)+(',' if j<len(v)-1 else '') for j,x in enumerate(v));lines.append(' ]'+suffix)
 else:lines.append(' '+q(k)+': '+q(v)+suffix)
lines.append('}');blob=('\n'.join(lines)+'\n').encode();assert json.loads(blob)==view;name='facility1156-reverse-complete-exact-components-view.json';assert not(P/name).exists();(P/name).write_bytes(blob);g={'begin_utc':t,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'source_index':56,'source_sha256':r['sha256'],'output':name,'bytes':len(blob),'lines':len(lines),'sha256':hashlib.sha256(blob).hexdigest(),'all_current_fields_exact_reconstruction':True,'generation_reading_credit':0,'source_credit':0,'business':'NOT_EXECUTED'};(P/'facility1156-reverse-complete-exact-components-generation.json').write_text(json.dumps(g,indent=2)+'\n');print(json.dumps(g))
