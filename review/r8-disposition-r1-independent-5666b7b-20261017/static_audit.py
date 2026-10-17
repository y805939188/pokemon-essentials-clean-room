#!/usr/bin/env python3
"""Independent fixed Git/JSON/Markdown reconciliation; no route generation."""
from pathlib import Path
import collections,copy,datetime,hashlib,importlib.util,json,re,subprocess,sys,unicodedata
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1];E=OUT/'evidence'
SRC=ROOT/'planning/implementation-routing/r8-20261017'
OLD='d62b41f4d620e50bb04c80a7505374bd284d8210';NEW='5666b7b912e2fb79b5119283ee6a37401a7071db'
REVIEW='a0352c7fba38391afc535525988245701d5ce202';BASE='fd1df570cad987dc3852a3b958f03916e317f7fe';DELIVERY='4575e80d041ab0c74a42e2e36399d05791dbaa5b'
CURRENT='908273093e1f6b27fc58249417675dd62d146224';RECEIPT='861f7a44a6f763c265a11761ab17a8ec3b55f304';ACTUAL='548d6bb9a21d0967680445c013e66d9d5661d2d6'
FORMAL='deliverables/final-specification-set';PRIOR='review/r8-disposition-independent-d62b41f-20261017'
R8='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
E.mkdir(exist_ok=True)
def save(n,d):(E/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def run(argv):
 p=subprocess.run(argv,cwd=ROOT,capture_output=True);r={'argv':argv,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':p.returncode,'stdout':p.stdout.decode(errors='replace'),'stderr':p.stderr.decode(errors='replace')}
 with (E/'commands.jsonl').open('a')as f:f.write(json.dumps(r,ensure_ascii=False)+'\n')
 return r
def git(*a):
 r=run(['git',*a]);assert r['exit_code']==0,r;return r['stdout']
def blob(c,p):return subprocess.check_output(['git','show',c+':'+p],cwd=ROOT)
def digest(b):return hashlib.sha256(b).hexdigest()
def jblob(c,p):return json.loads(blob(c,p))
def load(p):return json.loads(p.read_text())
def ident(c,p):
 b=blob(c,p);return {'commit':c,'path':p,'bytes':len(b),'sha256':digest(b),'git_blob':git('rev-parse',c+':'+p).strip()}
def parse(b):
 lines=b.decode().splitlines(keepends=True);out=[];fence=None;used=set()
 for i,line in enumerate(lines,1):
  raw=line.rstrip('\r\n');f=re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$',raw)
  if fence:
   if re.fullmatch(r' {0,3}'+re.escape(fence[0])+r'{'+str(fence[1])+r',}\s*',raw):fence=None
   continue
  if f:fence=(f[1][0],len(f[1]));continue
  mt=re.match(r'^ {0,3}(#{1,6})(?:[ \t]+(.*?)|[ \t]*)$',raw)
  if mt:level=len(mt[1]);title=re.sub(r'[ \t]+#+[ \t]*$','',mt[2] or '').strip();start=i
  elif i>1 and re.fullmatch(r' {0,3}(?:=+|-+)[ \t]*',raw)and lines[i-2].strip()and not lines[i-2].lstrip().startswith(('#','|','>','-','*','`')):level=1 if '='in raw else 2;title=lines[i-2].strip();start=i-1
  else:continue
  t=re.sub(r'<[^>]*>','',title);t=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',t).lower();s=''.join(c for c in t if c in' -_'or unicodedata.category(c)[0]in'LN').replace(' ','-');u=s;k=1
  while u in used:u=f'{s}-{k}';k+=1
  used.add(u);out.append({'level':level,'title':title,'anchor':u,'line_start':start,'heading_sha256':digest(lines[start-1].encode())})
 for n,h in enumerate(out):h['line_end']=next((x['line_start']-1 for x in out[n+1:]if x['level']<=h['level']),len(lines))
 return out,lines
m=load(SRC/'routing-manifest.json');c=load(SRC/'section-coverage.json');old=jblob(OLD,'planning/implementation-routing/r8-20261017/routing-manifest.json')
oldrows={x['feature_id']:x for x in old['features']};active={x['feature_id']:x for x in m['features']};retired={x['feature_id']:x for x in m['retired_features']};metadata={x['metadata_id']:x for x in m['metadata_records']}
objects=[]
for s in [NEW,OLD,REVIEW,CURRENT,RECEIPT,ACTUAL,BASE,DELIVERY]:objects.append({'sha':s,'type':git('cat-file','-t',s).strip(),'tree':git('rev-parse',s+'^{tree}').strip(),'formal_tree':git('rev-parse',s+':'+FORMAL).strip()})
save('fixed-objects.json',objects)
assert len(active)==len(m['features'])and len(retired)==len(m['retired_features'])and not set(active)&set(retired)
assert set(oldrows)<=set(active)|set(retired)
history=[];deltas=[]
prior_results=jblob(REVIEW,PRIOR+'/feature-results.json')['features'];prior_by_id={x['feature_id']:x for x in prior_results}
for fid,f in oldrows.items():
 n=active.get(fid,retired.get(fid));preserved=n['source']==f['source'];full=( {k:v for k,v in n.items()if k!='retirement'}==f)if fid in retired else None
 assert preserved and full is not False,fid
 history.append({'feature_id':fid,'prior_verdict':prior_by_id[fid]['verdict'],'new_state':'active'if fid in active else'retired','source_object_equal':preserved,'complete_retired_object_equal':full})
 if fid in active:
  changed=[k for k in set(f)|set(n)if f.get(k)!=n.get(k)];planfields=[k for k in set(f['future_plan'])|set(n['future_plan'])if f['future_plan'].get(k)!=n['future_plan'].get(k)]
  deltas.append({'feature_id':fid,'prior_verdict':prior_by_id[fid]['verdict'],'changed_top_fields':sorted(changed),'changed_plan_fields':sorted(planfields),'destination_changed':f['future_plan']['destination']!=n['future_plan']['destination'],'source_ranges_equal_effective':f['source']['line_ranges']==n['functional_scope']['line_ranges'],'semantic_inheritance_not_assigned_by_script':True})
newids=set(active)-set(oldrows);assert len(newids)==47 and not newids&set(retired)
save('old-id-preservation.json',{'rows':history,'old_count':len(history),'old_verdict_counts':dict(collections.Counter(x['prior_verdict']for x in history)),'active':len(active),'retired':len(retired),'metadata':len(metadata),'new_ids':sorted(newids),'new_max_id':max(newids)})
save('old-row-field-deltas.json',{'rows':deltas,'note':'Diff evidence only. Changed/unchanged fields do not grant semantic PASS or inherited credit.'})
files=git('ls-tree','-r','--name-only',BASE,'--',FORMAL).splitlines();currentfiles=git('ls-tree','-r','--name-only',CURRENT,'--',FORMAL).splitlines()
index=jblob(DELIVERY,R8+'/tasks/inventory_denominator/formal-inventory.json');assert set(files)=={x['path']for x in index}=={x['source']['path']for x in m['documents']}==set(currentfiles)
proof=[];sections=[];current_sections=[];differences=[];coverage_by_path=collections.defaultdict(list)
for x in c['sections']:coverage_by_path[x['path']].append(x)
for path in files:
 b=blob(BASE,path);cur=blob(CURRENT,path);hs,lines=parse(b);chs,clines=parse(cur)
 keys=['level','title','anchor','line_start','line_end','heading_sha256'];decl=[{k:x[k]for k in keys}for x in coverage_by_path[path]]
 assert hs==decl,path
 doc=next(x for x in m['documents']if x['source']['path']==path);assert doc['source']==ident(BASE,path)and doc['current_applicability']['identity']==ident(CURRENT,path),path
 prior_read=next(x for x in jblob(REVIEW,PRIOR+'/reading-coverage.json')['documents']if x['path']==path)
 assert prior_read['sha256']==digest(b),path
 proof.append({'path':path,'source':ident(BASE,path),'current':ident(CURRENT,path),'worktree_is_B8':(ROOT/path).read_bytes()==b,'source_headings':len(hs),'current_headings':len(chs),'source_lines':len(lines),'current_lines':len(clines),'prior_full_reading_identity_matches':True,'prior_reading_evidence':prior_read['reader_evidence'],'current_changed':b!=cur})
 sections.extend({'path':path,**h}for h in hs);current_sections.extend({'path':path,**h}for h in chs)
 if b!=cur:differences.append(path)
save('formal-coverage.json',{'documents':proof,'source_headings':sections,'current_headings':current_sections,'documents_count':len(proof),'source_heading_count':len(sections),'current_heading_count':len(current_sections),'changed_current_documents':differences,'all_source_identity_credit_eligible':True,'semantic_credit_must_be_assigned_by_domain_review':True})
scope=[];occupied=collections.defaultdict(set);currentocc=collections.defaultdict(set)
for fid,f in active.items():
 source_lines={n for a,b in f['source']['line_ranges']for n in range(a,b+1)};ranges=f['functional_scope']['line_ranges'];nums={n for a,b in ranges for n in range(a,b+1)}
 excluded=set()
 for child_id in f['functional_scope']['excluded_child_refs']:
  child=active[child_id];assert child['document_id']==f['document_id'];excluded|={n for a,b in child['source']['line_ranges']for n in range(a,b+1)}
 assert nums==source_lines-excluded and nums and not nums&occupied[f['source']['document']],fid;occupied[f['source']['document']]|=nums
 current=f['current_applicability'];assert current['snapshot_commit']==CURRENT and current['document']==f['source']['document'];loc=current['locator'];ch,cl=parse(blob(CURRENT,current['document']));heading=next(x for x in ch if x['anchor']==loc['anchor'])
 assert all(loc[a]==heading[b]for a,b in [('heading','title'),('heading_level','level'),('heading_sha256','heading_sha256')]);assert all(heading['line_start']<=a<=b<=heading['line_end']for a,b in loc['line_ranges'])
 unit=''.join(''.join(cl[a-1:b])for a,b in loc['line_ranges']).encode();actual=ident(CURRENT,current['document']);assert digest(unit)==loc['unit_sha256']and actual['sha256']==loc['file_sha256']and actual['git_blob']==loc['file_git_blob']
 cn={n for a,b in loc['line_ranges']for n in range(a,b+1)};assert not cn&currentocc[current['document']],fid;currentocc[current['document']]|=cn
 scope.append({'feature_id':fid,'document':current['document'],'source_ranges':f['source']['line_ranges'],'functional_ranges':ranges,'excluded_child_refs':f['functional_scope']['excluded_child_refs'],'current_ranges':loc['line_ranges'],'partition_and_no_overlap':'PASS','current_locator_identity':'PASS'})
save('functional-and-current-locators.json',{'features':scope,'active_count':len(scope)})
# Verify author file identity inventory and all 97 old-review input identities.
author_inventory=load(SRC/'candidate-file-manifest.json');inventory_checks=[]
for x in author_inventory['files']:
 actual=ident(NEW,x['path']);mode=git('ls-tree',NEW,'--',x['path']).split()[0];assert all(actual[k]==x[k]for k in ['bytes','sha256']);assert(ROOT/x['path']).read_bytes()==blob(NEW,x['path'])
 if 'git_blob'in x:assert actual['git_blob']==x['git_blob']
 if 'git_mode'in x:assert mode==x['git_mode']
 if 'lines'in x:assert len(blob(NEW,x['path']).decode().splitlines())==x['lines']
 inventory_checks.append(actual|{'git_mode':mode})
save('candidate-files.json',{'files':inventory_checks,'self_identity':ident(NEW,'planning/implementation-routing/r8-20261017/candidate-file-manifest.json')})
oldledger=load(SRC/'revisions/r1/tools/review-input-ledger.json');oldchecks=[]
for x in oldledger['files']:
 actual=ident(REVIEW,x['path']);assert all(actual[k]==x[k]for k in ['bytes','sha256']);oldchecks.append(actual)
save('prior-review-input-identity.json',{'files':oldchecks,'count':len(oldchecks),'credit':'Identity of all prior 97 inputs checked. Semantic prior reports/results are read by attributed root/domain contexts; no source reading credit comes from this mechanical check.'})
receipt=jblob(RECEIPT,'review/remediation-eighth-20261016-prepare/acceptance/U02-U03/receipt.json');checks=[]
for r in receipt['records']:
 assert r['ACCEPTED']is True and r['CLOSED']is False and r['actual_artifact_commit']==CURRENT and r['actual_independent_report_commit']==ACTUAL
 p=r['actual_target_identity']['path'];act=ident(CURRENT,p);rec=r['actual_target_identity'];assert act['sha256']==rec['sha256']and act['bytes']==rec['bytes']and act['git_blob']==rec['blob']
 checks.append({'batch':r['batch'],'accepted':True,'closed':False,'actual_identity':act,'receipt_record_identity_match':True})
bound=[f for f in active.values()if f['upstream']['batches']];accepted=[f for f in bound if f['upstream']['accepted_events']];pending=[f for f in bound if not f['upstream']['accepted_events']]
assert len(accepted)==17 and len(pending)==174 and len(bound)==191
assert {f['source']['document']for f in accepted}==set(differences)
for f in pending:assert f['upstream']['status']=='待整改后核对'and f['current_applicability']['status']=='待整改后核对'
changed_units=[]
for f in accepted:
 loc=f['current_applicability']['locator'];_,sl=parse(blob(BASE,f['source']['document']));_,cl=parse(blob(CURRENT,f['source']['document']));a=''.join(''.join(sl[x-1:y])for x,y in f['functional_scope']['line_ranges']);b=''.join(''.join(cl[x-1:y])for x,y in loc['line_ranges'])
 if a!=b:changed_units.append(f['feature_id'])
assert set(changed_units)=={'FR-000403','FR-000588'}
save('accepted-backfill-independent.json',{'receipt':{'commit':RECEIPT,'path':'review/remediation-eighth-20261016-prepare/acceptance/U02-U03/receipt.json'},'actual_report':{'commit':ACTUAL,'path':'review/remediation-eighth-20261016-prepare/reviews/actual-U02-U03/r1/report.md'},'current_payload':CURRENT,'receipt_records':checks,'known_bound_count':len(bound),'accepted_feature_ids':[f['feature_id']for f in accepted],'pending_feature_ids':[f['feature_id']for f in pending],'changed_current_function_units':changed_units,'qualification':'U02/U03 source-spec ACCEPTED only; CLOSED false and routing/implementation/target compatibility not accepted.'})
save('isolation.json',{'new_candidate':NEW,'base_to_new_formal_diff':git('diff','--name-status',BASE,NEW,'--',FORMAL),'old_to_new_changed_paths':git('diff','--name-status',OLD,NEW),'remote_refs_before':run(['git','ls-remote','origin','refs/heads/main','refs/heads/codex/r8-disposition-tagging-20261017','refs/heads/codex/r8-disposition-review-d62b41f-20261017'])})
for command in ['validate','check-generated']:run(['python',str((SRC/'routing.py').relative_to(ROOT)),command])
run(['python',str((SRC/'routing.py').relative_to(ROOT)),'assess-current','--commit',CURRENT])
run(['python',str((SRC/'revisions/r1/tools/validator-regressions.py').relative_to(ROOT)),'--output',str((E/'author-27-regressions.json').relative_to(ROOT))])
print(json.dumps({'documents':len(proof),'source_headings':len(sections),'current_headings':len(current_sections),'active':len(active),'retired':len(retired),'metadata':len(metadata),'new':len(newids),'accepted':len(accepted),'pending':len(pending),'changed_current_units':changed_units,'prior_review_inputs':len(oldchecks)},ensure_ascii=False))
