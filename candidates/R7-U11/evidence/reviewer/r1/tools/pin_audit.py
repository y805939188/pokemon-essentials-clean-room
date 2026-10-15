"""Bind all downloaded control files to actual fixed Git objects."""
import hashlib,json,pathlib,subprocess,datetime
out=pathlib.Path(__file__).resolve().parents[1];repo='/workspace/pokemon-essentials-clean-room';boot=pathlib.Path('/workspace/r7-review-bootstrap/R7-U11-r1');orig=pathlib.Path('/workspace/r7-bootstrap/R7-U11-reviewer');prefix='review/remediation-seventh-20261015-prepare/'
def git(*a):return subprocess.check_output(['git','-C',repo,*a])
def identity(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
D='95c260d8f3fb4a171675dde877137fcd4c2f1c8d';F='aa369555b0e8b6c8b077f964b54ed63d3b924f26';T='658488c81f1f3181a488298ab27850c8af951d73';B='e646432c644dec04d306842cc5a559a29c718fbc';C='f151a507bb43e8c936845c7408ab4bc14138caf0'
inputs=[(D,prefix+'candidate-freezes/R7-U11/reviewer-dispatch.md',boot/'reviewer-dispatch.md'),(D,prefix+'delegation/parallel-dispatch/candidate-freeze-requirements.json',boot/'candidate-freeze-requirements.json'),(D,'AGENTS.md',boot/'AGENTS.md')]
for p in ('candidate-input.json','candidate-restore/R7-U11.json','mirror-diffs.patch','remote-readback.json'):inputs.append((F,prefix+'candidate-freezes/R7-U11/'+p,boot/p))
for p in ('tools/restore_container_context.py','recovery/batches/R7-U11.json','recovery/independent-containers.md'):inputs.append((T,prefix+p,orig/p))
rows=[]
for commit,path,local in inputs:
 b=git('show',commit+':'+path);assert b==local.read_bytes();rows.append({'commit':commit,'path':path,'local_path':str(local),**identity(b),'exact_Git_object_match':True})
assert git('rev-parse',F+'^{tree}').decode().strip()=='08bd0f362c74ef7645b5bbd70b557489c122ae29'
skills=[]
for commit in (D,B,C):
 r=git('ls-tree','-r','--name-only',commit,'--','.agents').decode();assert not r;skills.append({'commit':commit,'tracked_dot_agents_paths':[]})
conflict=json.loads(git('show',D+':'+prefix+'delegation/conflict-groups.json'))
selected=[g for g in conflict['groups'] if g['id'] in ('CG01','CG03','CG07')]
assert all('R7-U11' in r['required_batches'] for r in selected)
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'fixed_commits':{c:git('rev-parse',c+'^{tree}').decode().strip() for c in (D,F,B,C)},'B_formal_subtree':git('rev-parse',B+':deliverables/final-specification-set').decode().strip(),'pinned_control_files':rows,'skills_check':{'git_tree_checks':skills,'workspace_dot_agents_visible_entries':[p.name for p in pathlib.Path('/workspace/.agents').iterdir()],'executor_catalog_observed_result':{'skills':[],'warnings':[],'next_cursor':None},'qualification':'No project .agents/skills content exists at these fixed inputs; no skill reading fabricated. Executor catalog observed via skills.list, not a model/configuration proof.'},'conflict_groups':selected,'qualification':'TOOL_VALIDATION_ONLY; no floating branch content substitutes for these fixed inputs.'}
(out/'fixed-pin-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'fixed_control_files':len(rows),'dispatch_tree':result['fixed_commits'][D],'freeze_tree':result['fixed_commits'][F],'skills':'ABSENT','groups':[g['id'] for g in selected]}))
