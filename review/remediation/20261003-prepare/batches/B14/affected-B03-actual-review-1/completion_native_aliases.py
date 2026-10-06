"""Own exact original raw-alias/native-structure supplement; no reviewed code runs."""
import completion_read as R
import json,re,collections
idx=R.gzload('completion-reading-index.json.gz');lookup={c['value_sha256']:i for i,c in enumerate(idx['claims'])};old_count=len(idx['claims']);aliases=collections.defaultdict(set)
controls=json.loads(R.git(R.ORIG,'review/global-independent-review/2026-10-03-fd82a639/findings.json'))
ids=set(json.loads((R.OUT/'completion-original-native-supplement.json').read_text())['canonical_membership'])
def find_reports(v):
 if isinstance(v,dict):
  if isinstance(v.get('report'),str) and isinstance(v.get('raw_id'),str):aliases[v['report']].add(v['raw_id'])
  for x in v.values():find_reports(x)
 elif isinstance(v,list):
  for x in v:find_reports(x)
for c in controls:
 if c['id'] in ids:find_reports(c)
B='review/global-independent-review/2026-10-03-fd82a639/'
def add(path,sel):
 b=R.git(R.ORIG,B+path)
 try:full=json.loads(b);kind='JSON'
 except ValueError:full={'literal_lines':b.decode().splitlines(keepends=True)};kind='TEXT_LINES_KEEPENDS'
 if any(d['commit']==R.ORIG and d['path']==B+path and d['selection']==sel for d in idx['documents']):return
 o={s:R.at(full,R.parts(s)) for s in sel} if sel is not None else full;di=len(idx['documents'])
 idx['documents'].append({'commit':R.ORIG,'path':B+path,'sha256':R.h(b),'bytes':len(b),'kind':kind,'selection':sel,'supplement':'Complete native raw finding/extension records selected by exact qualified canonical aliases; original keys/order/types and full selected bodies preserved, raw judgments do not override effective qualification.'})
 for ptr,a in R.scalars(o):
  for steps,v in R.semantic_derivations(a):
   k=R.vh(v);ref={'document':di,'selector':ptr,'steps':steps,'native_type':type(a).__name__,'native_value_sha256':R.vh(a)}
   if k not in lookup:lookup[k]=len(idx['claims']);idx['claims'].append({'value_sha256':k,'type':type(v).__name__,'first':ref,'metadata_only':False,'prior_consumed':None,'length':len(str(v))})
   idx['occurrences'].append([lookup[k],di,ptr,steps,type(a).__name__,R.vh(a)])
 print('ADDED',di,path,'native selections',len(sel) if sel is not None else 'whole')
bound=[]
for path,wanted in sorted(aliases.items()):
 if not path.endswith('.json'):continue
 full=json.loads(R.git(R.ORIG,B+path));sels=[]
 def select(v,p=''):
  if isinstance(v,dict):
   # Native extension records also use root_id and other explicitly named
   # ID fields. Keep the complete object at every exact scalar-ID match.
   if any(isinstance(x,str) and x in wanted for x in v.values()):sels.append(p);return
   for k,x in v.items():select(x,p+'/'+k.replace('~','~0').replace('/','~1'))
  elif isinstance(v,list):
   for n,x in enumerate(v):select(x,p+'/'+str(n))
 select(full);assert sels,(path,wanted)
 add(path,sels);bound.append({'path':B+path,'qualified_raw_IDs':sorted(wanted),'native_selected_objects':sels})
for path in ['root/independent-first-judgments.md','root/cross-risk-first-judgments.md']:add(path,None)
R.save('completion-native-alias-bindings.json',{'commit':R.ORIG,'canonical_membership':sorted(ids),'records':bound,'qualification_precedence':'Current qualified global findings/root/extension decisions govern; early raw verdicts are historical relationships only.','no_new_domain_reapproval':True})
R.save('completion-reading-index.json.gz',idx)
q=json.loads((R.OUT/'completion-pending-claims.json').read_text());q.extend(range(old_count,len(idx['claims'])));R.save('completion-pending-claims.json',q);print('new unique values',len(idx['claims'])-old_count,'queue',len(q))
