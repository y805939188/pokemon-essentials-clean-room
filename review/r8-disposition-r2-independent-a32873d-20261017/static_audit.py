#!/usr/bin/env python3
"""Independent fixed Git/JSON/Markdown reconciliation, not semantic acceptance."""
from pathlib import Path
import collections,datetime,gzip,hashlib,json,re,subprocess,unicodedata
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1];E=OUT/'evidence'
NEW='a32873d2860b15d9f5e27727db8f131f4ec433b6';R1='5666b7b912e2fb79b5119283ee6a37401a7071db';REVIEW='8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8'
D62='d62b41f4d620e50bb04c80a7505374bd284d8210';A035='a0352c7fba38391afc535525988245701d5ce202';B8='fd1df570cad987dc3852a3b958f03916e317f7fe';DELIVERY='4575e80d041ab0c74a42e2e36399d05791dbaa5b'
CURRENT='908273093e1f6b27fc58249417675dd62d146224';RECEIPT='861f7a44a6f763c265a11761ab17a8ec3b55f304';ACTUAL='548d6bb9a21d0967680445c013e66d9d5661d2d6'
EXTRA=['e042c2f061eb2951a8d662a5987804e3314cb6b4','3157ef455fdac41f0bf5485b281ef2e1699c8599','834888e29f939d0a5ed9478d763deb86eb021211','8f71c18480a847348b8450c9df1e7e8194c03985','49a558f7d5498680ba88d532f3815e07d7844459','0eee6d141f33758eda34bd8ebad94a3e2b617f5a']
SRC='planning/implementation-routing/r8-20261017';FORMAL='deliverables/final-specification-set';PRIOR='review/r8-disposition-r1-independent-5666b7b-20261017';R8='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
def save(n,v):(E/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def run(argv,cwd=ROOT):
 p=subprocess.run(argv,cwd=cwd,capture_output=True);r={'argv':argv,'cwd':str(cwd),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':p.returncode,'stdout':p.stdout.decode(errors='replace'),'stderr':p.stderr.decode(errors='replace')}
 with gzip.open(E/'static-commands.jsonl.gz','at')as f:f.write(json.dumps(r,ensure_ascii=False)+'\n')
 assert p.returncode==0,r
 return p.stdout
def git(*a):return run(['git',*a]).decode()
def blob(c,p):return run(['git','show',c+':'+p])
def sha(b):return hashlib.sha256(b).hexdigest()
def jb(c,p):return json.loads(blob(c,p))
def load(p):return json.loads(p.read_bytes())
def ident(c,p):
 b=blob(c,p);return {'commit':c,'path':p,'bytes':len(b),'sha256':sha(b),'git_blob':git('rev-parse',c+':'+p).strip()}
def parse(b):
 lines=b.decode().splitlines(keepends=True);out=[];fence=None;used=set()
 for i,line in enumerate(lines,1):
  raw=line.rstrip('\r\n');f=re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$',raw)
  if fence:
   if re.fullmatch(r' {0,3}'+re.escape(fence[0])+r'{'+str(fence[1])+r',}\s*',raw):fence=None
   continue
  if f:fence=(f[1][0],len(f[1]));continue
  mt=re.match(r'^ {0,3}(#{1,6})(?:[ \t]+(.*?)|[ \t]*)$',raw)
  if mt:level=len(mt[1]);title=re.sub(r'[ \t]+#+[ \t]*$','',mt[2]or'').strip();start=i
  elif i>1 and re.fullmatch(r' {0,3}(?:=+|-+)[ \t]*',raw)and lines[i-2].strip()and not lines[i-2].lstrip().startswith(('#','|','>','-','*','`')):level=1 if'='in raw else 2;title=lines[i-2].strip();start=i-1
  else:continue
  t=re.sub(r'<[^>]*>','',title);t=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',t).lower();s=''.join(c for c in t if c in' -_'or unicodedata.category(c)[0]in'LN').replace(' ','-');u=s;k=1
  while u in used:u=f'{s}-{k}';k+=1
  used.add(u);out.append({'level':level,'title':title,'anchor':u,'line_start':start,'heading_sha256':sha(lines[start-1].encode())})
 for n,h in enumerate(out):h['line_end']=next((x['line_start']-1 for x in out[n+1:]if x['level']<=h['level']),len(lines))
 return out,lines
objects=[]
for c in [NEW,R1,REVIEW,D62,A035,B8,DELIVERY,CURRENT,RECEIPT,ACTUAL,*EXTRA]:
 assert git('cat-file','-t',c).strip()=='commit';objects.append({'commit':c,'tree':git('rev-parse',c+'^{tree}').strip(),'formal_tree':git('rev-parse',c+':'+FORMAL).strip()})
save('fixed-objects.json',objects)
m=load(ROOT/SRC/'routing-manifest.json');cov=load(ROOT/SRC/'section-coverage.json');before=jb(R1,SRC+'/routing-manifest.json');initial=jb(D62,SRC+'/routing-manifest.json');prior=jb(REVIEW,PRIOR+'/feature-results.json')
active={f['feature_id']:f for f in m['features']};retired={f['feature_id']:f for f in m['retired_features']};combined=active|retired;metas={x['metadata_id']:x for x in m['metadata_records']};oldactive={f['feature_id']:f for f in before['features']};oldretired={f['feature_id']:f for f in before['retired_features']};oldcombined=oldactive|oldretired
assert len(active)==len(m['features'])and len(retired)==len(m['retired_features'])and not set(active)&set(retired)
assert set(combined)==set(oldcombined)|{'FR-000769'} and set(oldactive)-set(active)=={'FR-000086'} and set(retired)-set(oldretired)=={'FR-000086'}
for f in initial['features']:
 fid=f['feature_id'];assert combined[fid]['source']==f['source']
 if fid in retired:assert {k:v for k,v in retired[fid].items()if k!='retirement'}==f
for fid,f in oldcombined.items():assert combined[fid]['source']==f['source']
for fid,f in oldretired.items():assert {k:v for k,v in combined[fid].items()if k!='retirement'}=={k:v for k,v in f.items()if k!='retirement'}
old_pass_ids={f['feature_id']for f in prior['old_feature_results']if f['verdict']=='PASS'};new47={f['feature_id']for f in prior['active_feature_results']if f['is_new']};meta22={x['metadata_id']for x in prior['retired_metadata_results']if x['verdict']=='PASS'};oldmetas={x['metadata_id']:x for x in before['metadata_records']}
assert len(old_pass_ids)==693 and len(new47)==47 and len(meta22)==22
passproof=[{'feature_id':fid,'whole_object_equal':combined[fid]==oldcombined[fid],'original_R1_state':'active'if fid in oldactive else'retired'}for fid in sorted(old_pass_ids)];assert all(x['whole_object_equal']for x in passproof)
newproof=[{'feature_id':fid,'whole_object_equal':active[fid]==oldactive[fid]}for fid in sorted(new47)];assert all(x['whole_object_equal']for x in newproof)
metaproof=[{'metadata_id':mid,'whole_object_equal':metas[mid]==oldmetas[mid]}for mid in sorted(meta22)];assert all(x['whole_object_equal']for x in metaproof)
deltas=[{'feature_id':fid,'changed_fields':[k for k in sorted(set(oldcombined[fid])|set(combined[fid]))if oldcombined[fid].get(k)!=combined[fid].get(k)],'now_retired':fid in retired}for fid in sorted(oldcombined)if oldcombined[fid]!=combined[fid]]
save('stable-ids-and-preservation.json',{'old721':len(initial['features']),'current_active':len(active),'current_retired':len(retired),'current_metadata':len(metas),'surviving_active':len(set(oldactive)&set(active)),'new_active':['FR-000769'],'new_retired':['FR-000086'],'all_old_source_objects_equal':True,'all33_retired_bodies_equal_d62':True,'old693_pass_whole_objects':passproof,'r1_new47_whole_objects':newproof,'old22_pass_metadata_whole_objects':metaproof,'changed_existing_objects':deltas,'retirement_navigation_revisions':[fid for fid in oldretired if oldretired[fid]['retirement']!=retired[fid]['retirement']],'semantic_inheritance':'Identity/equality proves nonmutation only; domains independently check incoming and same-root semantic impact.'})
decl=load(ROOT/SRC/'candidate-file-manifest.json');file_checks=[]
for d in decl['files']:
 i=ident(NEW,d['path']);assert i['bytes']==d['bytes']and i['sha256']==d['sha256'];b=blob(NEW,d['path']);assert(ROOT/d['path']).read_bytes()==b
 if d.get('lines') is not None:assert len(b.decode().splitlines())==d['lines']
 file_checks.append(i|{'git_mode':git('ls-tree',NEW,'--',d['path']).split()[0]})
allactual=git('ls-tree','-r','--name-only',NEW,'--',SRC).splitlines();assert set(allactual)=={x['path']for x in decl['files']}|{SRC+'/candidate-file-manifest.json'}
save('candidate-file-identities.json',{'files':file_checks,'manifest':ident(NEW,SRC+'/candidate-file-manifest.json'),'actual_file_count':len(allactual)})
ledger=load(ROOT/SRC/'revisions/r2/tools/review-input-ledger.json');previous_files=[]
for d in ledger['files']:
 i=ident(REVIEW,d['path']);assert i['bytes']==d['bytes']and i['sha256']==d['sha256'];previous_files.append(i)
actualprev=git('ls-tree','-r','--name-only',REVIEW,'--',PRIOR).splitlines();assert set(actualprev)=={x['path']for x in previous_files}and len(previous_files)==73
save('r1-73-input-identities.json',{'files':previous_files,'count':len(previous_files),'credit':'Machine identity check plus attributed full prior reports/results and source reading; not automatic semantic acceptance.'})
paths=git('ls-tree','-r','--name-only',B8,'--',FORMAL).splitlines();index=jb(DELIVERY,R8+'/tasks/inventory_denominator/formal-inventory.json');assert set(paths)=={x['path']for x in index}=={d['source']['path']for d in m['documents']}
assert set(paths)==set(git('ls-tree','-r','--name-only',CURRENT,'--',FORMAL).splitlines());assert m['current_snapshot']==before['current_snapshot']and m['current_snapshot']['commit']==CURRENT
bycov=collections.defaultdict(list)
for h in cov['sections']:bycov[h['path']].append(h)
docs=[];sections=[];parsed={};current_parsed={}
for p in paths:
 b=blob(B8,p);hs,ls=parse(b);cur=blob(CURRENT,p);chs,cls=parse(cur);parsed[p]=(hs,ls);current_parsed[p]=(chs,cls)
 fields=['level','title','anchor','line_start','line_end','heading_sha256'];assert hs==[{k:h[k]for k in fields}for h in bycov[p]],p
 doc=next(d for d in m['documents']if d['source']['path']==p);old_doc=next(d for d in before['documents']if d['source']['path']==p)
 assert doc['source']==ident(B8,p)and doc['current_applicability']['identity']==ident(CURRENT,p)and doc['current_applicability']==old_doc['current_applicability']
 docs.append({'path':p,'source':ident(B8,p),'current':ident(CURRENT,p),'source_lines':len(ls),'current_lines':len(cls),'headings':len(hs),'source_and_current_equal':b==cur,'current_same_as_R1':True,'worktree_equals_B8':(ROOT/p).read_bytes()==b})
 sections.extend({'path':p,**h}for h in hs)
save('formal-coverage.json',{'documents':docs,'sections':sections,'documents_count':len(docs),'historical_headings':len(sections),'current908_headings':sum(len(x[0])for x in current_parsed.values()),'no_prepared_heading_credit':True,'source_bytes':sum(x['source']['bytes']for x in docs),'current_bytes':sum(x['current']['bytes']for x in docs)})
occupied=collections.defaultdict(set);currentoccupied=collections.defaultdict(set);locators=[]
for fid,f in active.items():
 p=f['source']['document'];hs,ls=parsed[p];h=next(x for x in hs if x['anchor']==f['source']['anchor']);s=f['source'];assert(s['heading'],s['heading_level'],s['heading_sha256'])==(h['title'],h['level'],h['heading_sha256'])
 assert sha(''.join(''.join(ls[a-1:b])for a,b in s['line_ranges']).encode())==s['unit_sha256'];srcnums={i for a,b in s['line_ranges']for i in range(a,b+1)};nums={i for a,b in f['functional_scope']['line_ranges']for i in range(a,b+1)};exc=set()
 for child in f['functional_scope']['excluded_child_refs']:
  assert active[child]['document_id']==f['document_id'];exc|={i for a,b in active[child]['source']['line_ranges']for i in range(a,b+1)}
 assert nums==srcnums-exc and nums and not nums&occupied[p],fid;occupied[p]|=nums
 cur=f['current_applicability'];assert cur['snapshot_commit']==CURRENT and cur['document']==p;loc=cur['locator'];chs,cls=current_parsed[p];h=next(x for x in chs if x['anchor']==loc['anchor']);assert(loc['heading'],loc['heading_level'],loc['heading_sha256'])==(h['title'],h['level'],h['heading_sha256']);assert all(h['line_start']<=a<=b<=h['line_end']for a,b in loc['line_ranges'])
 assert sha(''.join(''.join(cls[a-1:b])for a,b in loc['line_ranges']).encode())==loc['unit_sha256'];actual=next(d['current']for d in docs if d['path']==p);assert loc['file_sha256']==actual['sha256']and loc['file_git_blob']==actual['git_blob']
 cn={i for a,b in loc['line_ranges']for i in range(a,b+1)};assert not cn&currentoccupied[p],fid;currentoccupied[p]|=cn
 locators.append({'feature_id':fid,'source_identity':'PASS','functional_scope_partition':'PASS','current908_locator':'PASS','excluded_children':f['functional_scope']['excluded_child_refs']})
save('active-locator-and-scope-checks.json',{'rows':locators,'count':len(locators)})
events=load(ROOT/SRC/'accepted-source-updates.json');assert events==jb(R1,SRC+'/accepted-source-updates.json')and len(events['events'])==2
bound=[f for f in active.values()if f['upstream']['batches']];accepted=[f for f in bound if f['upstream']['accepted_events']];pending=[f for f in bound if not f['upstream']['accepted_events']]
assert len(bound)==191 and len(accepted)==17 and len(pending)==174
assert all(f['upstream']['status']=='待整改后核对'and f['current_applicability']['status']=='待整改后核对'for f in pending)
save('current-applied-state.json',{'current_snapshot':m['current_snapshot'],'accepted_events':events,'accepted_active_ids':[f['feature_id']for f in accepted],'pending_active_ids':[f['feature_id']for f in pending],'current_is_908_not_prepared':True,'unapplied_receipts_and_headings':'Independently assessed in agents/source-*; no final cumulative coverage/acceptance credit granted.'})
save('isolation.json',{'R1_to_R2_paths':git('diff','--name-status',R1,NEW),'formal_diff':git('diff',B8,NEW,'--',FORMAL),'reference_head':run(['git','rev-parse','HEAD'],Path('/workspace/pokemon-essentials')).decode().strip(),'reference_diff':run(['git','diff','--exit-code'],Path('/workspace/pokemon-essentials')).decode(),'remote_refs':git('ls-remote','origin','refs/heads/main','refs/heads/codex/r8-disposition-tagging-20261017','refs/heads/codex/r8-disposition-r1-review-5666b7b-20261017')})
print(json.dumps({'documents':len(docs),'headings':len(sections),'active':len(active),'retired':len(retired),'metadata':len(metas),'preserved_old_PASS':len(passproof),'preserved_R1new':len(newproof),'preserved_PASSmeta':len(metaproof),'bound':len(bound),'accepted':len(accepted),'pending':len(pending)},ensure_ascii=False))
