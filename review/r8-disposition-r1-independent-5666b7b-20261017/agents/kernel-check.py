#!/usr/bin/env python3
"""Independent JSON/Markdown/Git checks; no business code or author tool invocation."""
import collections,datetime,hashlib,json,re,subprocess
from pathlib import Path
BASE=Path('planning/implementation-routing/r8-20261017')
OUT=Path('review/r8-disposition-r1-independent-5666b7b-20261017/agents')
C='5666b7b912e2fb79b5119283ee6a37401a7071db'; O='d62b41f4d620e50bb04c80a7505374bd284d8210'; R='a0352c7fba38391afc535525988245701d5ce202'; B='fd1df570cad987dc3852a3b958f03916e317f7fe'; P='908273093e1f6b27fc58249417675dd62d146224'
commands=[]
def git(*args):
 p=subprocess.run(['git',*args],capture_output=True);commands.append({'argv':['git',*args],'exit_code':p.returncode,'stdout_bytes':len(p.stdout),'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr':p.stderr.decode()});p.check_returncode();return p.stdout
def blob(c,p):return git('show',f'{c}:{p}')
def sha(b):return hashlib.sha256(b).hexdigest()
def write(n,x): (OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
m=json.loads(blob(C,str(BASE/'routing-manifest.json')));old=json.loads(blob(O,str(BASE/'routing-manifest.json')))
prior=json.loads(blob(R,'review/r8-disposition-independent-d62b41f-20261017/agents/kernel-full-results.json'))
ids={x['feature_id'] for x in prior['features']}; a={x['feature_id']:x for x in m['features']};ret={x['feature_id']:x for x in m['retired_features']};ob={x['feature_id']:x for x in old['features']}
objects={c:git('cat-file','-t',c).decode().strip() for c in [C,O,R,B,'4575e80d041ab0c74a42e2e36399d05791dbaa5b',P,'861f7a44a6f763c265a11761ab17a8ec3b55f304','548d6bb9a21d0967680445c013e66d9d5661d2d6']}
docs=[]
for r in prior['reading_ledger']:
 p=r['path']; bb=blob(B,p);cur=blob(P,p)
 docs.append({'document_id':r['document_id'],'path':p,'historical_commit':B,'historical_bytes':len(bb),'historical_sha256':sha(bb),'historical_blob':git('rev-parse',f'{B}:{p}').decode().strip(),'prior_identity_equal':len(bb)==r['bytes'] and sha(bb)==r['sha256'],'candidate_and_workspace_equal_historical':blob(C,p)==bb and Path(p).read_bytes()==bb,'current_commit':P,'current_bytes':len(cur),'current_sha256':sha(cur),'current_blob':git('rev-parse',f'{P}:{p}').decode().strip(),'current_equal_historical':cur==bb,'lines':len(bb.splitlines())})
rows=[]
for fid in sorted(ids):
 f=a.get(fid) or ret[fid]; retired=fid in ret
 rows.append({'feature_id':fid,'active_count':int(fid in a),'retired_count':int(retired),'disposition_unique':int(fid in a)+int(retired)==1,'source_complete_object_equal':f['source']==ob[fid]['source'],'retired_complete_old_row_equal':({k:v for k,v in f.items() if k!='retirement'}==ob[fid]) if retired else None,'changed_top_fields':[k for k in f if ob[fid].get(k)!=f[k]],'source':f['source']})
active=[x for x in m['features'] if '/generic-kernel/' in x['source']['document']]
locator=[]
for f in active:
 s=f['current_applicability'];loc=s['locator']; bb=blob(s['snapshot_commit'],s['document']);ls=bb.splitlines(keepends=True)
 unit=b''.join(b''.join(ls[lo-1:hi]) for lo,hi in loc['line_ranges'])
 heading=ls[loc['line_ranges'][0][0]-1]
 locator.append({'feature_id':f['feature_id'],'pointer':f'/features/{m["features"].index(f)}/current_applicability/locator','file_sha_ok':sha(bb)==loc['file_sha256'],'file_blob_ok':git('rev-parse',f'{s["snapshot_commit"]}:{s["document"]}').decode().strip()==loc['file_git_blob'],'unit_sha_ok':sha(unit)==loc['unit_sha256'],'heading_sha_ok':sha(heading)==loc['heading_sha256'],'snapshot':s['snapshot_commit'],'locator':loc,'applicability_status':s['status'],'upstream_status':f['upstream']['status'],'accepted_events':f['upstream']['accepted_events'],'verification':f['destination_verification']['status'],'implementation':f['implementation']['status'],'acceptance':f['implementation']['acceptance_status']})
overlap=[]
for i,f in enumerate(active):
 for g in active[i+1:]:
  if f['source']['document']!=g['source']['document']:continue
  for lo,hi in f['functional_scope']['line_ranges']:
   for gl,gh in g['functional_scope']['line_ranges']:
    if max(lo,gl)<=min(hi,gh):overlap.append([f['feature_id'],g['feature_id'],max(lo,gl),min(hi,gh)])
s=json.loads(blob(C,str(BASE/'section-coverage.json')))['sections'];paths={x['path'] for x in docs};sections=[dict(x,pointer=f'/sections/{i}') for i,x in enumerate(s) if x['path'] in paths]
view=(BASE/'views/generic-kernel.md').read_text();vl=view.splitlines();vrows=[]
for f in active:
 lines=[(i,l) for i,l in enumerate(vl,1) if l.startswith('| '+f['feature_id']+' /')]
 r={'feature_id':f['feature_id'],'row_count':len(lines)}
 if lines:
  i,l=lines[0];r.update({'line':i,'row_sha256':sha(l.encode()),'destination_shown':f['future_plan']['destination'] in l,'responsibilities_shown':all(x['scope'] in l for x in f['future_plan']['responsibilities']),'snapshot_shown':f['current_applicability']['snapshot_commit'] in l,'verification_and_phase_shown':'待验证' in l and '待定（未批准） / 未实现 / 未验收' in l})
 vrows.append(r)
receipt=json.loads(blob('861f7a44a6f763c265a11761ab17a8ec3b55f304','review/remediation-eighth-20261016-prepare/acceptance/U02-U03/receipt.json'))
actual=json.loads(blob('548d6bb9a21d0967680445c013e66d9d5661d2d6','review/remediation-eighth-20261016-prepare/reviews/actual-U02-U03/r1/review-result.json'))
res={'schema':'kernel-r1-independent-mechanical.v1','candidate':C,'objects':objects,'formal_trees':{c:git('rev-parse',f'{c}:deliverables/final-specification-set').decode().strip() for c in [C,B,P]},'documents':docs,'old_row_identity_results':rows,'active_locator_results':locator,'active_scope_overlaps':overlap,'sections':sections,'view':{'path':str(BASE/'views/generic-kernel.md'),'lines':len(vl),'sha256':sha(view.encode()),'rows':vrows,'literal_full_view_semantic_read_claimed':False,'method':'All 64 machine rows and de-duplicated view-field projections reviewed; whole-view regeneration owned by root.'},'U02_receipt':receipt['records'][0],'actual_U02_result':actual['batches'][0],'summary':{'old_rows':len(rows),'old_unique_dispositions':all(x['disposition_unique'] for x in rows),'old_source_objects_preserved':all(x['source_complete_object_equal'] for x in rows),'retired_exact_old_rows':all(x['retired_complete_old_row_equal'] for x in rows if x['retired_complete_old_row_equal'] is not None),'active_rows':len(active),'new_ids':[x['feature_id'] for x in active if x['feature_id'] not in ids],'retired_ids':sorted(ids & ret.keys()),'all_locator_checks':all(all(x[k] for k in ['file_sha_ok','file_blob_ok','unit_sha_ok','heading_sha_ok']) for x in locator),'source_scope_disjoint':not overlap,'section_count':len(sections),'mapping_counts':dict(collections.Counter(x['mapping_kind'] for x in sections))}}
write('kernel-mechanical.json',res);write('kernel-command.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'entry_command':['python','review/r8-disposition-r1-independent-5666b7b-20261017/agents/kernel-check.py'],'scope':'Markdown/JSON/Git only','git_commands':commands,'python_completion':'normal; exit code reported by calling exec tool','business_execution_count':0})
print(json.dumps(res['summary'],ensure_ascii=False));print('object and tree checks:',res['formal_trees'])
