# Newly written review metadata collector. Reads Git/text/JSON only; never loads reference behavior.
import subprocess,json,hashlib,pathlib,re,datetime
R=pathlib.Path('/workspace/b14-affected-b04-review-2'); A=pathlib.Path('/tmp/b14-b04-round2-audit')
B='1e6b11a47370f1c7c4659a32443fc1afda597bac';C1='47f7514765f8569ae9172bb06a2cd615e2b83b8a';C2='af39efbf32549be964cb083bd49bed6d1d5c0d2a';G='93e10babe0b9c9ef8b3f5277754541b447beeeb4';P='41fffb540c6483f5296ea0d33b789b75180d27ed'
Q='review/remediation/20261003-prepare/batches/'
def git(*a): return subprocess.check_output(['git','-C',str(R),*a])
def data(c,p):return git('show',c+':'+p)
def sha(b):return hashlib.sha256(b).hexdigest()
def ident(c,p):
 b=data(c,p);return dict(commit=c,path=p,git_blob=git('rev-parse',c+':'+p).decode().strip(),sha256=sha(b),bytes=len(b))
def write(n,d): (A/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def patch_result(before,patch):
 lines=before.splitlines(keepends=True);pp=patch.splitlines(keepends=True);out=[];pos=0;i=2
 while i<len(pp):
  m=re.match(rb'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',pp[i]);assert m
  start=int(m[1])-1;assert start>=pos;out+=lines[pos:start];pos=start;i+=1;oldn=newn=0
  while i<len(pp) and not pp[i].startswith(b'@@'):
   line=pp[i];op=line[:1];body=line[1:]
   if op in [b' ',b'-']:assert lines[pos]==body;pos+=1;oldn+=1
   if op in [b' ',b'+']:out.append(body);newn+=1
   assert op in [b' ',b'-',b'+'];i+=1
  assert oldn==int(m[2] or b'1') and newn==int(m[4] or b'1')
 out+=lines[pos:];return b''.join(out)
def obj(c,p):return json.loads(data(c,p))
checks=[]
def check(n,v,details=None):checks.append(dict(check=n,passed=bool(v),details=details))
changes={};artifacts=[]
for label,start in [('B-to-C2',B),('C1-to-C2',C1)]:
 opts=['diff','--no-ext-diff','--no-textconv','--no-color','--no-renames','--binary','--full-index','--unified=3',start,C2]
 raw=git(*opts);(A/(label+'.diff')).write_bytes(raw)
 formal=git(*opts,'--','deliverables','specs');(A/(label+'-formal.diff')).write_bytes(formal)
 ns=git('diff','--no-renames','--name-status',start,C2).decode().splitlines();entries=[]
 for l in ns:
  status,p=l.split('\t');entries.append(dict(status=status,path=p,before=None if status=='A' else ident(start,p),after=ident(C2,p),formal=p.startswith(('deliverables/','specs/'))))
 changes[label]=entries;artifacts.extend([dict(path=label+'.diff',bytes=len(raw),sha256=sha(raw),unfiltered=True),dict(path=label+'-formal.diff',bytes=len(formal),sha256=sha(formal),unfiltered=False)])
 check(label+' every path reviewed by explicit classification',all(x['formal'] or x['path'].startswith(Q+'B14/') for x in entries))
check('cumulative formal12',sum(e['formal'] for e in changes['B-to-C2'])==12)
check('successor formal8',sum(e['formal'] for e in changes['C1-to-C2'])==8)
check('successor records14 all additions',sum(not e['formal'] for e in changes['C1-to-C2'])==14 and all(e['status']=='A' for e in changes['C1-to-C2'] if not e['formal']))
check('old B14 author/candidate/scope evidence unchanged',git('diff','--name-only',C1,C2,'--',Q+'B14/author-stage-1',Q+'B14/candidate-1',Q+'B14/scope-proposal-1')==b'')
write('complete-change-manifest.json',dict(diffs=artifacts,changes=changes))
rev=obj(C2,Q+'B14/candidate-2/revised-identities.json')
for d in rev['documents']:
 p=d['path']
 for c,k in [(B,'accepted_B09_before'),(C1,'candidate1_before'),(C2,'after')]:
  actual=ident(c,p);check('revised identity '+k+' '+p,all(actual[t]==d[k][t] for t in ['git_blob','sha256','bytes']))
 check('revised changed flag '+p,d['changed_in_candidate2']==(data(C1,p)!=data(C2,p)))
bounded=obj(C2,Q+'B14/candidate-2/bounded-amendment-1.json')
for d in bounded['documents']:
 p=d['path'];check('bounded before '+p,all(ident(C1,p)[t]==d['before'][t] for t in ['git_blob','sha256','bytes']))
 check('bounded after '+p,all(ident(C2,p)[t]==d['intended_after'][t] for t in ['git_blob','sha256','bytes']))
 patch=data(C2,Q+'B14/candidate-2/'+d['patch']);check('bounded exact patch '+p,sha(patch)==d['patch_sha256'] and patch_result(data(C1,p),patch)==data(C2,p))
# Fresh full control object/field binding checks, separate from scoped semantic judgment.
contract=obj(B,Q+'B09/acceptance-stage-1/B14-downstream-contract.json');fg='review/global-independent-review/2026-10-03-fd82a639/findings.json';fp='review/remediation-20261003-prepare/finding-acceptance.json'
gl=obj(G,fg);gm={x['id']:x for x in gl};pm=obj(P,fp);canon=lambda x:sha(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
controls=[]
for c in contract['contribution_controls']:
 i=c['id'];g=gm[i];p=pm[i];bad=[]
 for k,v in c['complete_current_control_fields'].items():
  if g.get(k)!=v:bad.append('G.'+k)
 for k,v in c['complete_minimum_acceptance_fields'].items():
  if p.get(k)!=v:bad.append('P.'+k)
 check('G whole qualified control '+i,canon(g)==c['whole_original_object_sha256']);check('P whole acceptance '+i,canon(p)==c['whole_acceptance_object_sha256']);check('current qualified fields '+i,not bad)
 controls.append(dict(id=i,primary=c['primary'],G_object_sha256=canon(g),P_object_sha256=canon(p),mismatches=bad,current_controls=c['complete_current_control_fields'],acceptance=c['complete_minimum_acceptance_fields']))
write('qualified-controls.json',dict(fixed_inputs=[ident(G,fg),ident(P,fp)],control_count=len(controls),controls=controls,semantic_approval='B04 affected scope only, not all24/19 R14'))
ref=obj(C2,Q+'B14/author-stage-1/input-refreeze.json');bindings=[]
for k in ['planned_reads','write_inputs','current_extra_inputs','fixed_controls']:
 for d in ref[k]:
  c=d.get('commit',B);actual=ident(c,d['path']);ok=all(actual[t]==d[t] for t in ['git_blob','sha256','bytes']);check('fresh input binding '+k+' '+d['path'],ok)
  bindings.append(dict(group=k,identity=actual,matched=ok,changed_at_C2=(data(c,d['path'])!=data(C2,d['path'])) if c==B else None))
check('current B09 contract unchanged',data(B,Q+'B09/acceptance-stage-1/B14-downstream-contract.json')==data(C2,Q+'B09/acceptance-stage-1/B14-downstream-contract.json'))
write('refrozen-input-verification.json',dict(identity_checks_only_not_72_semantic_rereads=True,bindings=bindings,reverse_B04_gate=[x for x in contract['accepted_reverse_review_gates'] if x['accepted_batch']=='B04'],formal_serialization=contract['formal_serialization']))
# Entire catalog rows, including multiplicity and order; no execution of designs.
catalogs=[]
for p in [x['path'] for x in contract['whole_catalog_locks']]:
 def rows(c):return [l for l in data(c,p).decode().splitlines(keepends=True) if re.match(r'^\|\s*[A-Z][A-Z0-9-]*\d+\s*\|',l)]
 def ids(rr):return [l.split('|')[1].strip() for l in rr]
 old,one,two=rows(B),rows(C1),rows(C2);oi,ii,ti=ids(old),ids(one),ids(two);mm=[]
 for prior,lab in [(old,'B'),(one,'C1')]:
  after=[l for l in two if l.split('|')[1].strip() in ids(prior)]
  check(lab+' catalog ID/order/multiplicity '+p,ids(after)==ids(prior))
  modified=[l.split('|')[1].strip() for l,n in zip(prior,after) if l!=n];mm.append(dict(from_commit=B if lab=='B' else C1,modified_old_ids=modified,unchanged_old_rows=len(prior)-len(modified)))
 modified_c1=mm[1]['modified_old_ids'];allowed=['WT28'] if 'engine-overworld' in p else ['BP18'];check('C1 only authorized catalog rows '+p,modified_c1==allowed)
 added=[i for i in ti if i not in ii];check('only WT39/40 added '+p,added==(['WT39','WT40'] if 'engine-overworld' in p else []))
 catalogs.append(dict(path=p,B_rows=len(old),C1_rows=len(one),C2_rows=len(two),row_comparisons=mm,added_C1_to_C2=added,identities=[ident(c,p) for c in [B,C1,C2]]))
check('503 preserved plus2 equals505',sum(x['C1_rows'] for x in catalogs)==503 and sum(x['C2_rows'] for x in catalogs)==505)
write('catalog-comparison.json',catalogs)
# B04 13 path list learned from fixed own historical report; all identities freshly read.
prior=obj('3aa4c41de2f58bd65405bc0855a7f45155a878c2',Q+'B14/affected-B04-review-1/B04-formal-preservation.json');owned=[]
for d in prior:
 p=d['path'];ids=[ident(c,p) for c in ['9e2dadfa650e2111b77f9eae1f834cc00b8805d5',B,C1,C2]]
 changed=data(B,p)!=data(C2,p);owned.append(dict(path=p,identities=ids,changed=changed));check('accepted B04 equals B '+p,ids[0]['git_blob']==ids[1]['git_blob'])
check('B04 only3 authorized paths changed',sum(d['changed'] for d in owned)==3);write('B04-formal-preservation.json',owned)
for p in ['specs/overworld/wp16-world-rendering-and-visual-transitions.md','deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md']:
 a=data(C1,p).decode().splitlines();b=data(C2,p).decode().splitlines();check('WP16 exactly one changed full line '+p,len(a)==len(b) and sum(x!=y for x,y in zip(a,b))==1)
for p in ['specs/pokemon-rules/wp60-berry-plants.md','deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md']:
 a=data(C1,p);b=data(C2,p)
 pre=lambda t:t.split(b'### 5.2')[0];post=lambda t:t.split(b'### 5.3',1)[1]
 check('berry outside5.2 preserved '+p,pre(a)==pre(b) and post(a)==post(b))
protected=[]
p=contract['whole_catalog_locks'][0]['path']
a=data(B,p);b=data(C2,p)
for label,aa,bb in [('all preceding engine/RS sections',a.split(b'## I.')[0],b.split(b'## I.')[0]),('entire B04-R family',a[a.index('## 使用说明'.encode()):],b[b.index('## 使用说明'.encode()):])]:
 check('protected '+label,aa==bb);protected.append(dict(label=label,path=p,before_sha256=sha(aa),after_sha256=sha(bb),bytes=len(aa),equal=aa==bb))
for p in [x['path'] for x in owned if 'test-catalog' in x['path'] and x['path']!=contract['whole_catalog_locks'][0]['path']]:
 check('whole B04 unaffected catalog '+p,data(B,p)==data(C2,p))
write('protected-sections.json',protected)
# Strict UTF8 decode of all formal C2 text; ASCII resource grammar literal preserved.
for d in rev['documents']:data(C2,d['path']).decode('utf8',errors='strict');check('valid UTF8 '+d['path'],True)
for p in ['specs/overworld/wp59-world-time-weather-field-moves.md','deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md']:
 check('ASCII Weather separator '+p,b'Weather = <' in data(C2,p))
check('candidate single parent C1',git('rev-list','--parents','-n','1',C2).decode().strip().split()==[C2,C1])
write('identity-checks.json',dict(kind='fresh Git/hash/text/JSON bookkeeping, not behavioral tests',checks=checks,passed=sum(x['passed'] for x in checks),failed=sum(not x['passed'] for x in checks)))
print(json.dumps(dict(checks=len(checks),failed=[x for x in checks if not x['passed']],diffs=artifacts,catalogs=[(x['B_rows'],x['C1_rows'],x['C2_rows']) for x in catalogs]),ensure_ascii=False,indent=2))
