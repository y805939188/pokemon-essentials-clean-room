#!/usr/bin/env python3
"""Independent bounded input identities and protection audit. No author writes."""
from pathlib import Path
import datetime, hashlib, json, subprocess
O=Path(__file__).resolve().parent; R=O.parents[1]; E=O/'evidence'
C='7ed3e0554ac24339a7e61cab152f628037111644'
P='c0f62d973180679134f2eb1a488c1dc359c8658f'
PR='34202eb7accfee48bb8761db88b340bd77f54a42'
S='planning/implementation-routing/r8-20261017/'
OLD='review/r8-disposition-r3-independent-c0f62d9-20261017/'
def git(*a,cwd=R):return subprocess.check_output(['git',*a],cwd=cwd)
def blob(c,p):return git('show',c+':'+p)
def sha(b):return hashlib.sha256(b).hexdigest()
def identity(c,p):
 b=blob(c,p)
 return {'bytes':len(b),'sha256':sha(b),'lines':None if p.endswith('.gz') else len(b.splitlines()),'git_blob':git('rev-parse',c+':'+p).decode().strip()}
def dump(p,d):(E/p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
checks=[]
def check(n,v):
 checks.append({'check':n,'passed':bool(v)})
 assert v,n
check('exact_single_parent',git('rev-list','--parents','-n','1',C).decode().split()==[C,P])
entries=[]
for line in git('ls-tree','-r',C,'--',S).decode().splitlines():
 meta,p=line.split('\t');mode,kind,b=meta.split();check('blob_mode_'+p,kind=='blob' and mode=='100644')
 i=identity(C,p);check('working_bytes_'+p,(R/p).read_bytes()==blob(C,p));entries.append({'path':p,'git_mode':mode,**i})
manifest=json.loads(blob(C,S+'candidate-file-manifest.json'))
by={x['path']:x for x in entries}
check('candidate175_exact_set',len(entries)==175 and set(by)=={x['path']for x in manifest['files']}|{S+'candidate-file-manifest.json'})
check('candidate174_payload',manifest['payload_file_count']==174)
for x in manifest['files']:check('declared_identity_'+x['path'],all(x[k]==by[x['path']][k] for k in ['bytes','sha256','lines','git_blob']))
dump('candidate-identities.json',{'candidate':C,'files':entries,'count':len(entries),'total_bytes':sum(x['bytes']for x in entries),'self_identity_bound_by_fixed_commit':True})
delta=json.loads(blob(C,S+'revisions/r3-calibration-repair/changes-from-c0.json'))
changed=git('diff','--name-only',P,C).decode().splitlines();excluded=delta['identity_exclusions']['paths']; declared=delta['files']
check('changed41_all_routing',len(changed)==41 and all(p.startswith(S)for p in changed))
check('delta38_plus3_exact',len(declared)==38 and len(excluded)==3 and set(changed)=={x['path']for x in declared}|set(excluded))
check('delta_no_overlap',not set(excluded)&{x['path']for x in declared})
for x in declared:
 check('delta_current_'+x['path'],x['current']==identity(C,x['path']))
 check('delta_previous_'+x['path'],x['previous']==(identity(P,x['path']) if x['change']=='MODIFY' else None))
check('delta15_added23_modified',sum(x['change']=='ADD'for x in declared)==15 and sum(x['change']=='MODIFY'for x in declared)==23)
dump('candidate-delta-identities.json',{'candidate':C,'parent':P,'actual_changed_paths':changed,'declared_payloads':declared,'fixed_commit_identity_exclusions':excluded,'actual_added':len(git('diff','--name-only','--diff-filter=A',P,C).decode().splitlines())})
prior=[]
for line in git('ls-tree','-r',PR,'--',OLD).decode().splitlines():
 meta,p=line.split('\t');mode,kind,b=meta.split();data=blob(PR,p)
 check('prior_report_worktree_'+p,(Path('/workspace/r8-disposition-r3-review')/p).read_bytes()==data)
 prior.append({'path':p,'git_mode':mode,**identity(PR,p)})
check('prior_report111',len(prior)==111)
pm=json.loads(blob(PR,OLD+'output-file-manifest.json'));pb={x['path'][len(OLD):]:x for x in prior}
check('prior110_manifest_plus_self',pm['count']==110 and set(pb)=={x['path']for x in pm['files']}|{'output-file-manifest.json'})
for x in pm['files']:check('prior_manifest_identity_'+x['path'],all(x[k]==pb[x['path']][k]for k in ['bytes','sha256']))
dump('prior111-input-identities.json',{'prior_review':PR,'files':prior,'count':len(prior),'total_bytes':sum(x['bytes']for x in prior),'qualification':'Identity of complete fixed prior review; does not create new full-text reading credit.'})
for p in ['review-prompt.md','revisions/r3/review-prompt.md']:
 old=blob(P,S+p).decode();new=blob(C,S+p).decode();addition=new.splitlines(keepends=True)[2:4]
 check('inherited_prompt_byte_preserved_'+p,new==''.join(old.splitlines(keepends=True)[:2]+addition+old.splitlines(keepends=True)[2:]))
fixed=[]
for c in [C,P,PR,'fd1df570cad987dc3852a3b958f03916e317f7fe','4575e80d041ab0c74a42e2e36399d05791dbaa5b','5f87743293290de2e219ecdd6c19e88280f60c9a','8336249c78b4698cd77445653d3b05ff6a76ce94']:
 fixed.append({'commit':c,'type':git('cat-file','-t',c).decode().strip(),'tree':git('rev-parse',c+'^{tree}').decode().strip(),'formal_tree':git('rev-parse',c+':deliverables/final-specification-set').decode().strip()})
check('candidate_formal_B8_exact',fixed[0]['formal_tree']==fixed[1]['formal_tree']==fixed[3]['formal_tree']=='f292698cdd4a8e725525a9be6dc34b75faaf151e')
check('accepted_current_exact',fixed[5]['formal_tree']=='93dc967b4cdb653359afc123d3b8b318d6475fdd')
dump('fixed-objects.json',fixed)
protected=git('diff',P,C,'--','deliverables','reference','AGENTS.md','.agents','.codex')
check('protected_committed_diff_empty',not protected)
check('candidate_all_tracked_worktree_bytes_unchanged',not git('diff',C,'--'))
refhead=git('rev-parse','HEAD',cwd='/workspace/pokemon-essentials').decode().strip();refstatus=git('status','--porcelain',cwd='/workspace/pokemon-essentials').decode()
check('reference_readonly_clean',refhead=='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b' and not refstatus)
refs=git('ls-remote','origin','refs/heads/main','refs/heads/codex/r8-disposition-tagging-20261017','refs/heads/codex/r8-r3-seven-line-recovery-20261017').decode()
expected={'refs/heads/main':'fd1df570cad987dc3852a3b958f03916e317f7fe','refs/heads/codex/r8-disposition-tagging-20261017':P,'refs/heads/codex/r8-r3-seven-line-recovery-20261017':C}
check('protected_remote_refs',dict((l.split()[1],l.split()[0])for l in refs.splitlines())==expected)
dump('protection-precommit.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'candidate':C,'tracked_diff_empty':True,'protected_committed_diff_empty':True,'reference_head':refhead,'reference_status':refstatus,'remote_refs':refs,'review_worktree_status':git('status','--short').decode()})
dump('input-audit-results.json',{'candidate':C,'checks':checks,'all_passed':all(x['passed']for x in checks),'qualification':'Static complete identity/protection checks; seven semantic reviews and prior-credit nonimpact are separate.'})
print(json.dumps({'checks':len(checks),'candidate_files':len(entries),'candidate_bytes':sum(x['bytes']for x in entries),'prior_review_files':len(prior),'changed_paths':len(changed),'all_passed':True}))
