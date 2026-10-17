#!/usr/bin/env python3
"""Independent complete fixed-source identities, headings and patch reconciliation."""
from pathlib import Path
from collections import defaultdict,Counter
import copy,datetime,gzip,hashlib,json,re,subprocess,unicodedata
O=Path(__file__).resolve().parent;R=O.parents[1];E=O/'evidence'
C='c0f62d973180679134f2eb1a488c1dc359c8658f';P='a32873d2860b15d9f5e27727db8f131f4ec433b6';REVIEW='0ef0b7ad5f9465cfe31da0d7a35f56b5ccba5add';D='d62b41f4d620e50bb04c80a7505374bd284d8210';B='fd1df570cad987dc3852a3b958f03916e317f7fe';CUR='5f87743293290de2e219ecdd6c19e88280f60c9a';OLD_CUR='908273093e1f6b27fc58249417675dd62d146224';PACKAGE='8336249c78b4698cd77445653d3b05ff6a76ce94'
S='planning/implementation-routing/r8-20261017';F='deliverables/final-specification-set';PR='review/r8-disposition-r2-independent-a32873d-20261017';cache={}
def sha(b):return hashlib.sha256(b).hexdigest()
def save(n,x):(E/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def run(argv,cwd=R):
 t=datetime.datetime.now(datetime.timezone.utc).isoformat();p=subprocess.run(argv,cwd=cwd,capture_output=True);item={'argv':argv,'cwd':str(cwd),'utc':t,'exit':p.returncode,'stdout_bytes':len(p.stdout),'stdout_sha256':sha(p.stdout),'stderr':p.stderr.decode(errors='replace')}
 if len(p.stdout)<2000:item['stdout']=p.stdout.decode(errors='replace')
 with(E/'static-command-log.jsonl').open('a')as log:log.write(json.dumps(item,ensure_ascii=False)+'\n')
 assert p.returncode==0,item;return p.stdout
def git(*a):return run(['git',*a]).decode()
def blob(c,p):
 k=(c,p)
 if k not in cache:cache[k]=run(['git','show',c+':'+p])
 return cache[k]
def jb(c,p):return json.loads(blob(c,p))
def load(n):return json.loads((R/S/n).read_bytes())
def identity(c,p):
 b=blob(c,p);return {'commit':c,'path':p,'bytes':len(b),'sha256':sha(b),'git_blob':sha1_blob(b)}
def sha1_blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
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
fixed=[C,P,REVIEW,'5666b7b912e2fb79b5119283ee6a37401a7071db','8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8',D,'a0352c7fba38391afc535525988245701d5ce202',B,'4575e80d041ab0c74a42e2e36399d05791dbaa5b',CUR,PACKAGE,'a974eb133bdb280ac46f2684df4b309a18fc6cc1','40f428ef33d9b09ba9cc584ef4794779cc9869cb','861f7a44a6f763c265a11761ab17a8ec3b55f304','548d6bb9a21d0967680445c013e66d9d5661d2d6','e042c2f061eb2951a8d662a5987804e3314cb6b4','834888e29f939d0a5ed9478d763deb86eb021211','3157ef455fdac41f0bf5485b281ef2e1699c8599','8f71c18480a847348b8450c9df1e7e8194c03985',OLD_CUR]
objects=[]
for c in fixed:
 assert git('cat-file','-t',c).strip()=='commit';objects.append({'commit':c,'tree':git('rev-parse',c+'^{tree}').strip(),'formal_tree':git('rev-parse',c+':'+F).strip()})
save('fixed-objects.json',objects)
m=load('routing-manifest.json');prev=jb(P,S+'/routing-manifest.json');original=jb(D,S+'/routing-manifest.json');hist=load('section-coverage.json');current=load('current-section-coverage.json');registry=load('accepted-source-updates.json')
assert m==jb(C,S+'/routing-manifest.json') and m['current_snapshot']['commit']==CUR and current['snapshot']==m['current_snapshot']
a={f['feature_id']:f for f in m['features']};ret={f['feature_id']:f for f in m['retired_features']};both=a|ret;pa={f['feature_id']:f for f in prev['features']};pr={f['feature_id']:f for f in prev['retired_features']};meta={f['metadata_id']:f for f in m['metadata_records']}
assert set(a)==set(pa) and set(ret)==set(pr) and not set(a)&set(ret);assert m['metadata_records']==prev['metadata_records'] and m['retired_features']==prev['retired_features']
for f in original['features']:
 n=both[f['feature_id']];assert n['source']==f['source']
 if f['feature_id']in ret:assert {k:v for k,v in n.items()if k!='retirement'}==f
for fid,f in (pa|pr).items():assert f['source']==both[fid]['source']
assert blob(C,S+'/section-coverage.json')==blob(P,S+'/section-coverage.json')
for fid,f in a.items():
 old=pa[fid];assert f['functional_scope']==old['functional_scope']
 for key in ['destination','partners','stage','stage_approval','proposal_status','exclusion_decision']:assert f['future_plan'][key]==old['future_plan'][key]
 for key in ['implementation','destination_verification']:assert f[key]==old[key]
 assert set(old['upstream']['batches'])<=set(f['upstream']['batches']) and set(old['upstream']['required_ids'])<=set(f['upstream']['required_ids'])
 assert f['destination_verification']['status']=='待验证'and f['implementation']['status']=='未实现'and f['implementation']['acceptance_status']=='未验收'and f['future_plan']['stage']=='待定'and f['future_plan']['stage_approval']=='未批准'
history=[]
for p in git('ls-tree','-r','--name-only',P,'--',S).splitlines():
 if '/revisions/r1/'in p or'/revisions/r2/'in p:assert blob(C,p)==blob(P,p);history.append(identity(C,p))
assert len(history)==58
save('preservation.json',{'active':len(a),'retired':len(ret),'metadata':len(meta),'old721_immutable_sources':True,'retired33_complete_d62_bodies':True,'metadata33_exact_R2':True,'history58':history,'source_scope_category_partners_stage_implementation_verification_preserved':True,'semantic_PASS_inheritance':'Not automatic; domain full affected-unit and dependency checks.'})
# Exact explicit patch reconstruction, independent of author replay implementation.
archive=gzip.decompress(blob(C,S+'/revisions/r3/tools/post-source-pre-semantic-35175c7094b0.json.gz'));patch=load('revisions/r3/source-refinement-patch.json');assert sha(archive)==patch['input_manifest_sha256'];reconstructed=json.loads(archive);ra={f['feature_id']:f for f in reconstructed['features']};changes=[];seen=set()
allowed={'/future_plan/rationale','/future_plan/responsibilities','/future_plan/questions','/dependencies/feature_refs','/dependencies/direct_refs','/dependencies/wp_refs','/differences'}
for row in patch['records']:
 fid=row['feature_id']
 for field in row['field_changes']:
  pointer=field['pointer'];assert pointer in allowed and(fid,pointer)not in seen;seen.add((fid,pointer))
  if pointer.startswith('/future_plan/'):assert fid in patch['six_future_dependency_refinement_ids']
  obj=ra[fid];parts=pointer.strip('/').split('/')
  for part in parts[:-1]:obj=obj[part]
  assert obj[parts[-1]]==field['before'];obj[parts[-1]]=copy.deepcopy(field['after']);changes.append({'feature_id':fid,'pointer':pointer})
assert reconstructed==m
serialized=(json.dumps(reconstructed,ensure_ascii=False,indent=2)+'\n').encode();assert serialized==blob(C,S+'/routing-manifest.json')
save('patch-reconstruction.json',{'archive_sha256':sha(archive),'patch_sha256':sha(blob(C,S+'/revisions/r3/source-refinement-patch.json')),'rows':len(patch['records']),'fields':len(changes),'complete_object_and_serialized_bytes_equal':True,'final_manifest_sha256':sha(serialized),'changes':changes,'semantic_validity':'Separate independent domain review; replay does not prove narrative accuracy.'})
# Declared author candidate identities and precise R2 diff, excluding only explicit self identities.
manifest=load('candidate-file-manifest.json');checks=[]
for d in manifest['files']:
 i=identity(C,d['path']);assert all(i[k]==d[k]for k in ['bytes','sha256','git_blob']);b=blob(C,d['path']);assert(R/d['path']).read_bytes()==b
 if d.get('lines')is not None:assert len(b.decode().splitlines())==d['lines']
 checks.append(i|{'mode':git('ls-tree',C,'--',d['path']).split()[0]})
paths=git('ls-tree','-r','--name-only',C,'--',S).splitlines();assert set(paths)=={d['path']for d in manifest['files']}|{S+'/candidate-file-manifest.json'}
save('candidate-identities.json',{'files':checks,'manifest':identity(C,S+'/candidate-file-manifest.json'),'actual_count':len(paths)})
priorchecks=[]
for d in load('revisions/r3/tools/r2-review-input-ledger.json')['files']:
 i=identity(REVIEW,d['path']);assert all(i[k]==d[k]for k in ['bytes','sha256','git_blob']);priorchecks.append(i)
assert len(priorchecks)==94 and {x['path']for x in priorchecks}==set(git('ls-tree','-r','--name-only',REVIEW,'--',PR).splitlines())
save('r2-94-input-identities.json',{'count':94,'files':priorchecks,'consumption':'Identity proof only; full prose/structured domain consumption attributed in ledgers.'})
pack=[]
for d in load('revisions/r3/tools/cumulative-input-ledger.json')['files']:
 i=identity(d['commit'],d['path']);assert all(i[k]==d[k]for k in ['bytes','sha256','git_blob']);pack.append(i)
assert len(pack)==11;save('cumulative11-input-identities.json',{'files':pack,'semantic_reading':'agents/source-* plus root intake; not identity-only acceptance'})
diff=load('revisions/r3/changes-from-r2.json');exclusions=diff['identity_exclusions']['paths'];actualchanges=set(git('diff','--name-only',P,C).splitlines());assert all(p.startswith(S+'/')for p in actualchanges)
for d in diff['files']:
 i=identity(C,d['path']);assert all(i[k]==d['current'][k]for k in ['bytes','sha256','git_blob']);prior=d.get('previous')
 if prior:
  old=identity(P,d['path']);assert all(old[k]==prior[k]for k in ['bytes','sha256','git_blob'])
assert {d['path']for d in diff['files']}|set(exclusions)==actualchanges,(exclusions,actualchanges-{d['path']for d in diff['files']})
save('R2-to-R3-paths.json',{'actual_changes':sorted(actualchanges),'declared_nonself_payload_changes':len(diff['files']),'identity_exclusions':exclusions,'all_only_routing':True})
# Independently parse every formal heading and verify all current/source files.
wp_index=jb('4575e80d041ab0c74a42e2e36399d05791dbaa5b','review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/coverage/wp-final-coverage.json');assert len(wp_index['rows'])==87
formalpaths=git('ls-tree','-r','--name-only',B,'--',F).splitlines();assert set(formalpaths)==set(git('ls-tree','-r','--name-only',CUR,'--',F).splitlines())=={d['source']['path']for d in m['documents']}
byhist=defaultdict(list);bycur=defaultdict(list)
for h in hist['sections']:byhist[h['path']].append(h)
for h in current['sections']:bycur[h['path']].append(h)
parsed={};cparsed={};docs=[];added=[];fields=['level','title','anchor','line_start','line_end','heading_sha256']
for p in formalpaths:
 hs,ls=parse(blob(B,p));chs,cls=parse(blob(CUR,p));parsed[p]=(hs,ls);cparsed[p]=(chs,cls);assert hs==[{k:x[k]for k in fields}for x in byhist[p]];assert chs==[{k:x[k]for k in fields}for x in bycur[p]]
 d=next(d for d in m['documents']if d['source']['path']==p);assert d['source']==identity(B,p);assert d['current_applicability']['snapshot_commit']==CUR and d['current_applicability']['identity']==identity(CUR,p)
 assert(R/p).read_bytes()==blob(B,p)
 docs.append({'path':p,'source':identity(B,p),'current':identity(CUR,p),'source_lines':len(ls),'current_lines':len(cls),'source_headings':len(hs),'current_headings':len(chs),'changed':blob(B,p)!=blob(CUR,p),'same_current_as_R2':blob(OLD_CUR,p)==blob(CUR,p)})
 oldkeys={x['anchor']for x in hs};added.extend({'path':p,**h}for h in chs if h['anchor']not in oldkeys)
 ids={f['feature_id']for f in m['features']};mids=set(meta)
 for h in bycur[p]:assert set(h['feature_refs'])<=ids and set(h['metadata_refs'])<=mids
assert len(docs)==131 and sum(d['source_headings']for d in docs)==2683 and sum(d['current_headings']for d in docs)==2704 and len(added)==21
save('formal-coverage.json',{'documents':docs,'count':len(docs),'historical_headings':2683,'current_headings':2704,'changed_documents':sum(d['changed']for d in docs),'new_headings':added,'source_bytes':sum(d['source']['bytes']for d in docs),'current_bytes':sum(d['current']['bytes']for d in docs)})
occupied=defaultdict(set);coccupied=defaultdict(set);locators=[];changedunits=[]
for fid,f in a.items():
 s=f['source'];p=s['document'];hs,ls=parsed[p];h=next(x for x in hs if x['anchor']==s['anchor']);assert(s['heading'],s['heading_level'],s['heading_sha256'])==(h['title'],h['level'],h['heading_sha256']);assert sha(''.join(''.join(ls[x-1:y])for x,y in s['line_ranges']).encode())==s['unit_sha256']
 nums={i for x,y in f['functional_scope']['line_ranges']for i in range(x,y+1)};srcnums={i for x,y in s['line_ranges']for i in range(x,y+1)};exc=set()
 for child in f['functional_scope']['excluded_child_refs']:assert a[child]['document_id']==f['document_id'];exc|={i for x,y in a[child]['source']['line_ranges']for i in range(x,y+1)}
 assert nums==srcnums-exc and nums and not nums&occupied[p];occupied[p]|=nums
 cur=f['current_applicability'];l=cur['locator'];chs,cls=cparsed[p];h=next(x for x in chs if x['anchor']==l['anchor']);assert cur['snapshot_commit']==CUR and cur['document']==p;assert(l['heading'],l['heading_level'],l['heading_sha256'])==(h['title'],h['level'],h['heading_sha256']);assert all(h['line_start']<=x<=y<=h['line_end']for x,y in l['line_ranges'])
 unit=''.join(''.join(cls[x-1:y])for x,y in l['line_ranges']).encode();assert sha(unit)==l['unit_sha256'];ident=identity(CUR,p);assert l['file_sha256']==ident['sha256']and l['file_git_blob']==ident['git_blob'];cn={i for x,y in l['line_ranges']for i in range(x,y+1)};assert not cn&coccupied[p];coccupied[p]|=cn
 sourceeffective=''.join(ls[i-1]for i in sorted(nums)).encode()
 if sourceeffective!=unit:changedunits.append(fid)
 locators.append({'feature_id':fid,'historical_source_identity':'PASS','source_effective_partition':'PASS','current_locator':'PASS','current_unit_text_changed':sourceeffective!=unit})
 for ref in f['dependencies']['direct_refs']:assert ref['document']in parsed and ref['anchor']in{x['anchor']for x in parsed[ref['document']][0]}
 assert set(f['dependencies']['feature_refs'])<=set(a)
save('all736-locators.json',{'rows':locators,'count':len(locators),'direct_changed_unit_ids':changedunits,'direct_changed_unit_count':len(changedunits),'range_overlap_count':0})
bound=[f for f in a.values()if f['upstream']['batches']];newly=[f['feature_id']for f in bound if not pa[f['feature_id']]['upstream']['batches']];extended=[f['feature_id']for f in bound if set(f['upstream']['batches'])-set(pa[f['feature_id']]['upstream']['batches'])];events={x['event_id']:x for x in registry['events']}
assert len(bound)==230 and len(newly)==39 and len(extended)==47 and len(events)==9
binding=[]
for f in bound:
 u=f['upstream'];actualevents=[events[e]for e in u['accepted_events']];assert set(u['batches'])<=set(b for e in actualevents for b in e['batches']);assert all(f['source']['document']in e['documents']for e in actualevents);assert u['status']=='已回填ACCEPTED源规格；去向待独立复审'
 binding.append({'feature_id':f['feature_id'],'batches':u['batches'],'events':u['accepted_events'],'status':'ALL_BINDINGS_BACKFILLED_STRUCTURE_ONLY'})
save('binding-clearance.json',{'current_snapshot':CUR,'registry':registry,'bound':230,'newly_bound':newly,'new_or_extended':extended,'pending':0,'partial':0,'bindings':binding,'qualification':'All planned obligations retained; semantic source/routing calibration checked independently.'})
assert git('diff',B,C,'--',F)=='';reference=Path('/workspace/pokemon-essentials');assert run(['git','rev-parse','HEAD'],reference).decode().strip()=='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';assert run(['git','status','--porcelain'],reference)==b''
save('isolation.json',{'all_changes':sorted(actualchanges),'formal_diff':'EMPTY','reference_head':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','reference_clean':True,'remote_refs':git('ls-remote','origin','refs/heads/main','refs/heads/codex/r8-disposition-tagging-20261017','refs/heads/codex/r8-disposition-r2-review-a32873d-20261017')})
print(json.dumps({'documents':len(docs),'headings':2704,'new_headings':21,'changed_docs':sum(d['changed']for d in docs),'active':len(a),'retired':len(ret),'metadata':len(meta),'direct_changed_units':len(changedunits),'patch_rows':len(patch['records']),'patch_fields':len(changes),'bound':len(bound),'pending':0,'prior_report_files':len(priorchecks)},ensure_ascii=False))
