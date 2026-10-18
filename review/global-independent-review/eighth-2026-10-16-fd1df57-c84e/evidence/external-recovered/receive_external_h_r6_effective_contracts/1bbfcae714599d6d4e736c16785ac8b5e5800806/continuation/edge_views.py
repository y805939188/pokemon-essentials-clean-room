"""Reversible display aliases for complete edge fields; generation is reading zero."""
import pathlib,json,re,hashlib
T=pathlib.Path(__file__).resolve().parents[1];O=T/'continuation/edge-reading';O.mkdir(exist_ok=True)
roles=json.loads((T/'decoded-index.json').read_text())['roles'];original=json.loads((T/roles[5]['decoded_path']).read_text())['edges'];claim=json.loads((T/'inputs/interface-and-edge-claims.json').read_text())['edges']
assert len(original)==len(claim)==110
for x,y in zip(original,claim):assert x==y['original'] and all(x[k]==y[k] for k in ['index','from','to','kind'])
ids={};identity_definitions={}
prefix='deliverables/final-specification-set/'
def walk(x,p=''):
 if isinstance(x,dict):
  if set(x)=={'bytes','sha256','git_blob'}:
   assert isinstance(x['bytes'],int) and x['bytes']>=0 and re.fullmatch('[a-f0-9]{64}',x['sha256']) and re.fullmatch('[a-f0-9]{40}',x['git_blob'])
   key=json.dumps(x,sort_keys=True)
   if key not in ids:ids[key]='identity-'+str(len(ids));identity_definitions[ids[key]]=x
   return {'$exact_identity':ids[key]}
  return {k:walk(v,p+'/'+k) for k,v in x.items()}
 if isinstance(x,list):return [walk(v,p+'/'+str(i)) for i,v in enumerate(x)]
 if isinstance(x,str):
  if re.fullmatch('[a-f0-9]{40}',x):
   if x not in ids:ids[x]='oid-'+str(len(ids));identity_definitions[ids[x]]=x
   return {'$exact_identity':ids[x]}
  if prefix in x:return {'$formal_prefix_text':x.replace(prefix,'@FORMAL/')}
 return x
v=walk(original)
def restore(x):
 if isinstance(x,dict):
  if set(x)=={'$exact_identity'}:return identity_definitions[x['$exact_identity']]
  if set(x)=={'$formal_prefix_text'}:return x['$formal_prefix_text'].replace('@FORMAL/',prefix)
  return {k:restore(v) for k,v in x.items()}
 if isinstance(x,list):return [restore(v) for v in x]
 return x
assert restore(v)==original
root_claims={k:sorted({json.dumps(e[k],ensure_ascii=False,sort_keys=True) for e in claim}) for k in ['fresh_read','adjudication','basis','main_reception']}
(O/'exact-identities.json').write_text(json.dumps(dict(purpose='Full exact claimed transport identities only; all pointer/value references preserved. Not original-candidate remote recovery or semantic PASS.',definitions=identity_definitions),ensure_ascii=False,indent=2)+'\n')
(O/'display-legend.json').write_text(json.dumps(dict(formal_prefix=prefix,identity_definitions='exact-identities.json',outer_author_claims=root_claims,reconstruction_equal=True,original_source_role=5,original_source_pointer='/edges',claim_source='inputs/interface-and-edge-claims.json#/edges',reading_credit_from_generation=0),ensure_ascii=False,indent=2)+'\n')
for k,start in enumerate(range(0,110,28)):
 rows=v[start:start+28];(O/('edges-%02d.jsonl'%k)).write_text(''.join(json.dumps(x,ensure_ascii=False,separators=(',',':'))+'\n' for x in rows))
print(json.dumps(dict(edges=110,identity_aliases=len(identity_definitions),display_bytes=sum(p.stat().st_size for p in O.glob('edges-*.jsonl')),roundtrip_equal=True,reading_credit=0)))
