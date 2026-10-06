"""Own complete relevant PLAN/control supplement, retaining native object/row structure."""
import completion_read as R
import json,csv,io
idx=R.gzload('completion-reading-index.json.gz');lookup={c['value_sha256']:i for i,c in enumerate(idx['claims'])};old=len(idx['claims']);added=[]
B='review/remediation-20261003-prepare/'
def add(path,sel=None):
 b=R.git(R.PLAN,B+path)
 try:full=json.loads(b);kind='JSON'
 except ValueError:full={'literal_lines':b.decode().splitlines(keepends=True)};kind='TEXT_LINES_KEEPENDS'
 o={s:R.at(full,R.parts(s)) for s in sel} if sel is not None else full;di=len(idx['documents']);ident={'commit':R.PLAN,'path':B+path,'sha256':R.h(b),'bytes':len(b),'kind':kind,'selection':sel,'supplement':'Direct frozen PLAN acceptance/owner/dependency/conflict control meaning; no authorization-to-quality transfer.'};idx['documents'].append(ident);added.append(ident)
 for ptr,a in R.scalars(o):
  for steps,v in R.semantic_derivations(a):
   k=R.vh(v);ref={'document':di,'selector':ptr,'steps':steps,'native_type':type(a).__name__,'native_value_sha256':R.vh(a)}
   if k not in lookup:lookup[k]=len(idx['claims']);idx['claims'].append({'value_sha256':k,'type':type(v).__name__,'first':ref,'metadata_only':False,'prior_consumed':None,'length':len(str(v))})
   idx['occurrences'].append([lookup[k],di,ptr,steps,type(a).__name__,R.vh(a)])
for path in ['stage-b-contract.md','batches/B03.md','batches/B14.md','cross-chain-acceptance.md','reported-navigation-limits.json']:add(path)
o=json.loads(R.git(R.PLAN,B+'batches.json'));add('batches.json',['/'+str(n) for n,x in enumerate(o) if x['id'] in ['B03','B14']])
for path in ['semantic-dependencies.tsv','physical-conflicts.tsv','shared-premise-conflicts.tsv','finding-coverage.tsv']:
 lines=R.git(R.PLAN,B+path).decode().splitlines(keepends=True);sel=['/literal_lines/0']
 for n,l in enumerate(lines[1:],1):
  cells=next(csv.reader(io.StringIO(l),delimiter='\t'))
  if any('B03' in x or 'B14' in x for x in cells):sel.append('/literal_lines/'+str(n))
 add(path,sel)
R.save('completion-reading-index.json.gz',idx);R.save('completion-plan-native-controls.json',{'commit':R.PLAN,'documents':added,'complete_selected_native_objects_and_rows_retained':True,'semantic_completion_not_implied':True})
q=json.loads((R.OUT/'completion-pending-claims.json').read_text());q.extend(range(old,len(idx['claims'])));R.save('completion-pending-claims.json',q);print('new plan native unique values',len(idx['claims'])-old,'queue',len(q))
