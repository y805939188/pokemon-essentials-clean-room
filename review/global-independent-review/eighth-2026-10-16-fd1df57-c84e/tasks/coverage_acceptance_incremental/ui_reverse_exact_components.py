"""Own static complete UI reverse component representation; generation is not reading.
All literal compound texts, every complete bounded assertion, dictionaries and all
ordered bindings must be actually read. Exact reconstruction preserves absence.
"""
from pathlib import Path
import datetime,hashlib,json
P=Path(__file__).resolve().parent;B=P.parent.parent;t=datetime.datetime.now(datetime.timezone.utc).isoformat();r=json.loads((P/'reading-ledger.json').read_text())['snapshot_payloads'][232];raw=(B/r['snapshot']).read_bytes();assert len(raw)==r['bytes'] and hashlib.sha256(raw).hexdigest()==r['sha256'];d=json.loads(raw);rows=d['records'];keys=['line_unit_id','path','line','compound_text','linked_source_fact_ids','disposition','atomic_denominator_final','remaining','bounded_assertions'];assert all(set(x)==set(keys) for x in rows)
q=lambda x:json.dumps(x,ensure_ascii=False,separators=(',',':'))
pools={k:[] for k in ['path','compound_text','linked_source_fact_ids','disposition','remaining']};lookup={k:{} for k in pools};facts=[];fl={};factsets=[];fsl={};out=[];common={'atomic_denominator_final':False};rebuilt=[]
for n,x in enumerate(rows,1):
 assert x['line_unit_id']==f'UI65-C{n:04d}' and x['atomic_denominator_final'] is False
 rr=[]
 for k in pools:
  sig=q(x[k])
  if sig not in lookup[k]:lookup[k][sig]=len(pools[k]);pools[k].append(x[k])
  rr.append(lookup[k][sig])
 fs=[]
 for f in x['bounded_assertions']:
  sig=q(f)
  if sig not in fl:fl[sig]=len(facts);facts.append(f)
  fs.append(fl[sig])
 sig=q(fs)
 if sig not in fsl:fsl[sig]=len(factsets);factsets.append(fs)
 ix=fsl[sig];out.append([rr[0],x['line'],rr[1],rr[2],rr[3],rr[4],ix]);rebuilt.append({'line_unit_id':f'UI65-C{n:04d}','path':pools['path'][rr[0]],'line':x['line'],'compound_text':pools['compound_text'][rr[1]],'linked_source_fact_ids':pools['linked_source_fact_ids'][rr[2]],'disposition':pools['disposition'][rr[3]],'atomic_denominator_final':False,'remaining':pools['remaining'][rr[4]],'bounded_assertions':[facts[z] for z in factsets[ix]]})
assert rebuilt==rows
view={'schema':'gr8-ui1127-exact-current-components/v1','qualification':'All current carrier fields retained. Every literal and all ordered bindings require actual reading; generation0/source0/atomic0. Row n=1..1127 has exact original id UI65-C plus decimal n padded to4digits. No implicit acceptance of unlinked child claims.','source':{k:r[k] for k in ['original_path','snapshot','bytes','sha256','git_blob','captured_utc']},'all_other_root_fields':{k:v for k,v in d.items() if k!='records'},'row_common_fields':common,'complete_field_dictionaries':pools,'complete_bounded_assertion_objects':facts,'bounded_assertion_set_dictionary':factsets,'row_columns':['path_index','original_line','compound_text_index','linked_source_fact_list_index','disposition_index','remaining_index','bounded_assertion_set_index'],'ordered_rows':out}
lines=['{']
for i,(k,v) in enumerate(view.items()):
 suffix=',' if i<len(view)-1 else ''
 if isinstance(v,list) and v and isinstance(v[0],(list,dict)):
  lines.append(' '+q(k)+': [');lines.extend('  '+q(x)+(',' if j<len(v)-1 else '') for j,x in enumerate(v));lines.append(' ]'+suffix)
 elif k=='complete_field_dictionaries':
  lines.append(' '+q(k)+': {')
  for j,(f,a) in enumerate(v.items()):
   lines.append('  '+q(f)+': [');lines.extend('   '+q(x)+(',' if z<len(a)-1 else '') for z,x in enumerate(a));lines.append('  ]'+(',' if j<len(v)-1 else ''))
  lines.append(' }'+suffix)
 else:lines.append(' '+q(k)+': '+q(v)+suffix)
lines.append('}');blob=('\n'.join(lines)+'\n').encode();assert json.loads(blob)==view;name='ui1127-reverse-complete-exact-components-view.json';assert not(P/name).exists();(P/name).write_bytes(blob);g={'begin_utc':t,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'source_index':232,'source_sha256':r['sha256'],'output':name,'bytes':len(blob),'lines':len(lines),'sha256':hashlib.sha256(blob).hexdigest(),'all_current_fields_exact_reconstruction':True,'generation_reading_credit':0,'source_credit':0,'business':'NOT_EXECUTED'};(P/'ui1127-reverse-complete-exact-components-generation.json').write_text(json.dumps(g,indent=2)+'\n');print(json.dumps(g))
