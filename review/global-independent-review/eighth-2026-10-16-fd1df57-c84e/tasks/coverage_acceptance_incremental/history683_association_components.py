"""Own partial137 static association aid; raw canonical SHA values recovery-only.

Literal pointer templates plus original decimal digit strings reconstruct each
from/to verbatim. No associated target semantic value is supplied by this aid.
"""
import datetime,hashlib,json,re
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent.parent;begin=datetime.datetime.now(datetime.timezone.utc).isoformat();l=json.loads((P/'reading-ledger.json').read_text());r=l['snapshot_payloads'][137];raw=(B/r['snapshot']).read_bytes();assert hashlib.sha256(raw).hexdigest()==r['sha256'];d=json.loads(raw);templates=[];credits=[];facts=[];lookup={};rows=[];sha=[];full=[]
def pointer(s):
 parts=re.split(r'(\d+)',s);template='{}'.join(parts[::2]);digits=parts[1::2]
 if template not in templates:templates.append(template)
 idx=templates.index(template);z=templates[idx]
 for q in digits:z=z.replace('{}',q,1)
 assert z==s
 return [idx,digits]
for ri,rec in enumerate(d['records']):
 bind=[];rebuilt=[]
 for ai,x in enumerate(rec.get('current_same_value_associations',[])):
  assert set(x)=={'from','to','canonical_bytes','canonical_sha256','credit'} and re.fullmatch('[0-9a-f]{64}',x['canonical_sha256'])
  if x['credit'] not in credits:credits.append(x['credit'])
  f=[*pointer(x['from']),*pointer(x['to']),x['canonical_bytes'],credits.index(x['credit'])];sig=json.dumps(f,separators=(',',':'))
  if sig not in lookup:lookup[sig]=len(facts);facts.append(f)
  bind.append(lookup[sig]);sha.append({'record':ri,'association':ai,'canonical_sha256':x['canonical_sha256'],'purpose':'CANONICAL_VALUE_RECOVERY_IDENTITY_ONLY_NO_LITERAL_READ'})
  def undo(i,ds):
   s=templates[i]
   for q in ds:s=s.replace('{}',q,1)
   return s
  rebuilt.append({'from':undo(f[0],f[1]),'to':undo(f[2],f[3]),'canonical_bytes':f[4],'canonical_sha256':x['canonical_sha256'],'credit':credits[f[5]]})
 assert rebuilt==rec.get('current_same_value_associations',[]);rows.append(bind)
side=P/'h137-association-sha-recovery-only.json';side.write_text(json.dumps(sha,indent=2)+'\n');sraw=side.read_bytes();lines=['{"qualification":"PARTIAL137 associations only;683 canonicalSHA values separately strict recovery identity, not personally literal read. Complete from/to pointer templates retain exact literal names; replace each{} left-to-right with ordered original decimal digit strings. All indices zero-based. Each fact=[fromTemplate,fromDigits,toTemplate,toDigits,canonicalBytes,creditIdx]. Every243 ordered binding list required. Targets are referenced, not actually read from this carrier.",','"recovery":'+json.dumps({'path':side.name,'rows':len(sha),'bytes':len(sraw),'sha256':hashlib.sha256(sraw).hexdigest(),'literal_hex_read':False},separators=(',',':'))+',','"pointer_templates":[']
for i,x in enumerate(templates):lines.append(json.dumps(x)+(',' if i+1<len(templates) else ''))
lines.append('],"credits":'+json.dumps(credits,ensure_ascii=False,separators=(',',':'))+',"association_facts":[')
for i,x in enumerate(facts):lines.append(json.dumps(x,separators=(',',':'))+(',' if i+1<len(facts) else ''))
lines.append('],"ordered243association_bindings":[')
for i,x in enumerate(rows):lines.append(json.dumps(x,separators=(',',':'))+(',' if i+1<len(rows) else ''))
lines.append(']}');data=('\n'.join(lines)+'\n').encode();json.loads(data);out=P/'h137-association-complete-nonhash-components-view.json';out.write_bytes(data);m={'begin_utc':begin,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'source_index':137,'source_sha256':r['sha256'],'output':out.name,'bytes':len(data),'lines':len(lines),'sha256':hashlib.sha256(data).hexdigest(),'templates':len(templates),'unique_nonhash_association_facts':len(facts),'binding_records':len(rows),'total_associations':len(sha),'all_current_association_objects_exact_reconstruction':True,'generation_reading_credit':0,'whole137_complete':False};(P/'h137-association-components-generation.json').write_text(json.dumps(m,indent=2)+'\n');print(json.dumps(m))
