"""Own native scalar supplement; opaque string primitives never change native type."""
import completion_read as R
import json
idx=R.gzload('completion-reading-index.json.gz');lookup={c['value_sha256']:i for i,c in enumerate(idx['claims'])};old=len(idx['claims']);occ=[]
for di,d in enumerate(idx['documents']):
 b=R.git(d['commit'],d['path']);assert R.h(b)==d['sha256']
 try:o=json.loads(b)
 except ValueError:o={'literal_lines':b.decode().splitlines(keepends=True)}
 if d['selection'] is not None:o={s:R.at(o,R.parts(s)) for s in d['selection']}
 for ptr,a in R.scalars(o):
  for steps,v in R.semantic_derivations(a):
   k=R.vh(v);ref={'document':di,'selector':ptr,'steps':steps,'native_type':type(a).__name__,'native_value_sha256':R.vh(a)}
   if k not in lookup:lookup[k]=len(idx['claims']);idx['claims'].append({'value_sha256':k,'type':type(v).__name__,'first':ref,'metadata_only':R.pure(v,ptr,set()),'prior_consumed':None,'length':len(str(v)),'native_scalar_supplement':True})
   occ.append([lookup[k],di,ptr,steps,type(a).__name__,R.vh(a)])
idx['native_scalar_supplement_occurrences']=occ
idx['nested_JSON_policy']='Only whole JSON containers or complete property lines are decoded; native string/hash/number-like scalar types stay distinct. Earlier derived views retain exact outer native type/hash/context and are not native behavior evidence.'
R.save('completion-reading-index.json.gz',idx)
q=json.loads((R.OUT/'completion-pending-claims.json').read_text());q.extend(i for i in range(old,len(idx['claims'])) if not idx['claims'][i]['metadata_only']);R.save('completion-pending-claims.json',q)
R.save('completion-native-scalar-correction.json',{'correction':'Restrict embedded JSON decoding to full containers/property lines; retain opaque native string scalar type and exact identity. Earlier transform views preserved, not rewritten into native assertions.','new_native_values':len(idx['claims'])-old,'native_scalar_occurrences':len(occ),'native_types_and_all_relationships_retained':True,'semantic_completion_not_implied':True})
print('new native values',len(idx['claims'])-old,'added semantic queue',len(q)-8458,'queue',len(q))
