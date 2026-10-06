"""New own native-control document bookkeeping; no historical helper runs."""
import completion_read as R
import json,re,subprocess
idx=R.gzload('completion-reading-index.json.gz');lookup={c['value_sha256']:i for i,c in enumerate(idx['claims'])};known=set()
for commit in [R.ACT,R.ORIG,R.PLAN,R.PRE]:known.update(subprocess.check_output(['git','ls-tree','-r','--name-only',commit]).decode().splitlines())
ids=set()
for commit,path in [(R.PRE,'review/remediation/20261003-prepare/batches/B03/integration-stage-1/finding-registration.json'),(R.ACT,R.BASE+'integration-stage-1/finding-registration.json')]:
 ids.update(r['id'] for r in json.loads(R.git(commit,path))['dispositions'])
original=json.loads(R.git(R.ORIG,'review/global-independent-review/2026-10-03-fd82a639/findings.json'))
selected=[x for x in original if x['id'] in ids];aliases=set()
for x in selected:
 aliases.update(re.findall(r'RUN-[ABC]-\d{3}',json.dumps(x)))
def add(commit,path,sel=None):
 if any(d['commit']==commit and d['path']==path and d['selection']==sel for d in idx['documents']):return
 b=R.git(commit,path)
 try:full=json.loads(b);kind='JSON'
 except ValueError:full={'literal_lines':b.decode().splitlines(keepends=True)};kind='TEXT_LINES_KEEPENDS'
 o={s:R.at(full,R.parts(s)) for s in sel} if sel is not None else full
 di=len(idx['documents']);idx['documents'].append({'commit':commit,'path':path,'sha256':R.h(b),'bytes':len(b),'kind':kind,'selection':sel,'supplement':'Separate native original second-review/root evidence, preserving external binding and full selected object fields/order/types.'})
 for ptr,a in R.scalars(o):
  for steps,v in R.semantic_derivations(a):
   k=R.vh(v);ref={'document':di,'selector':ptr,'steps':steps,'native_type':type(a).__name__,'native_value_sha256':R.vh(a)}
   if k not in lookup:
    lookup[k]=len(idx['claims']);idx['claims'].append({'value_sha256':k,'type':type(v).__name__,'first':ref,'metadata_only':R.pure(v,ptr,known),'prior_consumed':None,'length':len(str(v))})
   idx['occurrences'].append([lookup[k],di,ptr,steps,type(a).__name__,R.vh(a)])
 print('ADDED',di,path,'selectors',len(sel) if sel else 'whole')
B='review/global-independent-review/2026-10-03-fd82a639/'
for p,key in [('agents/A/X-A-C05-RECHECK/recheck.json','rechecks'),('agents/B/X-B-C06-RECHECK/findings-review.json','items')]:
 o=json.loads(R.git(R.ORIG,B+p));sels=['/'+k for k in o if k!=key]+['/'+key+'/'+str(n) for n,v in enumerate(o[key]) if v['id'] in aliases];add(R.ORIG,B+p,sels)
for p in ['root/fullwidth-syntax-review.json','root/new-findings.json']:
 o=json.loads(R.git(R.ORIG,B+p))
 if isinstance(o,list):sels=['/'+str(n) for n,x in enumerate(o) if any(i in json.dumps(x) for i in ids)]
 else:
  keys=['colon_candidates','equals_candidates','known_grammar_parenthesis_candidates'];sels=['/'+k for k in o if k not in keys]
  for k in keys:sels+=['/'+k+'/'+str(n) for n,x in enumerate(o[k]) if x.get('finding') in ids or re.search(r'/wp1[1-4]-',x.get('path',''))]
 add(R.ORIG,B+p,sels)
for p in ['root/c05-unified-scope.md','root/fullwidth-syntax-review.md','root/language-semantics-correction.md','root/language-semantics-review-note.md','root/reading-range-correction.md','root/process-deviations.md']:
 add(R.ORIG,B+p)
R.save('completion-reading-index.json.gz',idx)
R.save('completion-original-native-supplement.json',{'canonical_membership':sorted(ids),'raw_aliases_from_full_native_findings':sorted(aliases),'documents_added':len(idx['documents'])-287,'all_native_contexts_retained':True,'semantic_completion_not_implied':True})
# Append new semantic values without disturbing the existing queue positions.
q=json.loads((R.OUT/'completion-pending-claims.json').read_text());present=set(q)
q.extend(i for i,c in enumerate(idx['claims']) if not c['metadata_only'] and not c['prior_consumed'] and i not in present)
R.save('completion-pending-claims.json',q);print('pending queue',len(q))
