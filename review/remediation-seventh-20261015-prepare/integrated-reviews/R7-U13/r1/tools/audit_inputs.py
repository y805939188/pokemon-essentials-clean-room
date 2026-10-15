"""Independent byte audit; no behavior, reference, candidate or native programs run."""
from pathlib import Path
import hashlib,json,subprocess,sys,datetime
root=Path('/workspace/r7-ir-R7-U13');out=Path(__file__).resolve().parent
sys.path.insert(0,str(out));from run_logged import identity
repo=root/'checkout';MI='45c80832a41c1b56dcd7e9d93497758cbb7721de';B='e646432c644dec04d306842cc5a559a29c718fbc';FI='13d76ba61838b13925ba9d41f58a6b047564d926'
def git(*a):return subprocess.check_output(['git','-C',str(repo),*a])
def check(d,e):
 a=identity(d)
 for k,v in a.items():
  ek='git_blob' if k=='git_blob_content_id' and 'git_blob' in e else k
  if ek in e:assert v==e[ek],(k,v,e[ek])
 return a
r={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'plans':{},'git':{},'formal':[],'snapshots':[],'prior_preservation':[],'semantic_credit':False}
for name,dest in [('original-plans','original'),('actual-plans','actual-input')]:
 p=json.loads((root/name/'R7-U13.json').read_bytes());rows=p['artifacts']+p['evidence']+p['fixed_read_inputs']
 checks=[dict(local_path=x['local_path'],**check((root/dest/x['local_path']).read_bytes(),x)) for x in rows]
 r['plans'][name]={'files':len(checks),'bytes':sum(x['bytes'] for x in checks),'checks':checks}
fi=json.loads(git('show',FI+':review/remediation-seventh-20261015-prepare/integration/wave2/v1/integrated-input.json'))
for c in [B,MI,FI]:r['git'][c]=git('show','-s','--format=%H %T %P',c).decode().strip()
assert git('rev-parse',MI+'^{tree}').decode().strip()==fi['actual_MI_tree']
assert git('rev-parse',MI+':deliverables/final-specification-set').decode().strip()==fi['actual_formal_subtree']
paths=git('ls-tree','-r','--name-only',MI,'--','deliverables/final-specification-set').decode().splitlines()
assert len(paths)==131 and set(paths)=={x['path'] for x in fi['all_formal_file_identities']}
for row in fi['all_formal_file_identities']:
 p=row['path'];d=git('show',MI+':'+p);b=git('show',B+':'+p)
 a=check(d,row);check(b,row['base_B_identity']);assert (d!=b)==row['changed_against_B']
 r['formal'].append(dict(path=p,**a,changed_against_B=d!=b))
assert sum(x['changed_against_B'] for x in r['formal'])==26
for row in json.loads((root/'actual-plans/R7-U13.json').read_bytes())['artifacts']:
 if row['local_path'].startswith(('actual/','baseline/')):
  d=(root/'actual-input'/row['local_path']).read_bytes();assert d==git('show',row['commit']+':'+row['path'])
  r['snapshots'].append(dict(path=row['local_path'],git_tree_bytes_match=True))
for p in (root/'actual-input/prior-accepted/actual-at-accepted-MI').rglob('*.md'):
 rel=p.relative_to(root/'actual-input/prior-accepted/actual-at-accepted-MI');a=(root/'actual-input/actual'/rel).read_bytes();assert a==p.read_bytes()
 r['prior_preservation'].append(dict(path=str(rel),**identity(a),mechanical_preservation_only=True))
assert len(r['prior_preservation'])==5
r['summary']={'formal_files':131,'changed_against_B':26,'unchanged_against_B':105,'prior_five_exact':5,'new_targets':len(fi['new_actual_target_files']),'required_ids':len(fi['covered_new_required_ids'])}
(out/'input-byte-audit.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(r['summary']))
