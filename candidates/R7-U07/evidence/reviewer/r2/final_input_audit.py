"""Finish exact immutable input receipt; no model or reference execution."""
import datetime,hashlib,json,os,shutil,subprocess
from pathlib import Path
E=Path(__file__).resolve().parent;root=Path('/workspace/r7-u07-reviewer-r2');F=Path('/workspace/r7-review-bootstrap/R7-U07-r2');R=Path('/workspace/r7-context/R7-U07-reviewer');C=Path('/workspace/r7-review-input/R7-U07-r2-2649ed2bd2cc3afdfa636cd643fc1975de5eae32')
def ident(d):return {'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest()}
def git(*args):return subprocess.check_output(['git',*args],cwd=root)
def copy(src,dst):
 dst=E/dst;dst.parent.mkdir(parents=True,exist_ok=True)
 if dst.exists():assert dst.read_bytes()==src.read_bytes()
 else:shutil.copyfile(src,dst)
 return {'path':str(dst.relative_to(root)),**ident(dst.read_bytes())}
freeze=json.loads((F/'candidate-input.json').read_bytes());readback=json.loads((F/'remote-readback.json').read_bytes())
assert readback['candidate_commit']==freeze['candidate_commit'] and readback['candidate_tree']==freeze['candidate_tree']
expected={r['path']:r for r in freeze['candidate_and_author_evidence_file_identities']}
assert set(expected)=={r['path'] for r in readback['files']}
for row in readback['files']:
 for k in ['bytes','sha256','git_blob','git_mode']:assert row[k]==expected[row['path']][k]
assert git('rev-parse','c651d5599badf5fb9f99c05d307f1d7d70374ab7^{tree}').decode().strip()=='515114b8ea1fdf7154ed47d812c88cb0eed5716c'
for p in (E/'prior-r1').glob('*'):
 assert p.read_bytes()==git('show','c651d5599badf5fb9f99c05d307f1d7d70374ab7:candidates/R7-U07/evidence/reviewer/r1/'+p.name)
paths=[]
for name in ['reviewer-dispatch.md','candidate-input.json','candidate-restore/R7-U07.json','mirror-diffs.patch','remote-readback.json']:paths.append(copy(F/name,'inputs/'+name))
paths.append(copy(Path('/workspace/r7-bootstrap/R7-U07-reviewer/tools/restore_container_context.py'),'inputs/restore_container_context.py'))
paths.append(copy(Path('/workspace/r7-bootstrap/R7-U07-reviewer/recovery/batches/R7-U07.json'),'inputs/original-recovery-plan.json'))
paths.append(copy(R/'dispatch/delegation/contracts/R7-U07.json','inputs/original-contract.json'))
paths.append(copy(R/'evidence/tasks/R7-C17/limits-and-alias-reception.json','inputs/limits-and-alias-reception.json'))
for base,label in [(R,'original'),(C,'candidate')]:
 for p in base.glob('recovery-receipt-*.json'):paths.append(copy(p,'receipts/'+label+'-'+p.name))
ledger=[]
for p in sorted((E/'logs').glob('*.json')):
 log=json.loads(p.read_bytes())
 if any(a.endswith('/inspect_inputs.py') for a in log['argv']) and 'file' in log['argv']:
  metadata=json.loads(log['stdout'].splitlines()[0])
  lo,hi=metadata['read_lines']
  if lo>metadata['lines']:continue
  metadata['requested_read_lines']=[lo,hi]
  metadata['read_lines']=[lo,min(hi,metadata['lines'])]
  ledger.append({**metadata,'log':str(p.relative_to(E)),'qualification':'Actual displayed scoped/full text read; static only'})
ledger.extend(json.loads((E/'supplemental-input-receipt.json').read_bytes())['files'][:3])
(E/'read-ledger.json').write_text(json.dumps({'entries':ledger,'other_full_inputs':['inputs/reviewer-dispatch.md','inputs/original-contract.json','original role prompts: logs/035-original-role-prompts.json','normalized /records/14 all seven groups: logs/021-normalized-identity.json and logs/022-normalized-*.json','original/root /records/14: logs/004-original.json','nonauthor /challenges/3: logs/003-counter.json'],'limits':'Not all 3.9 MB normalized records, source whole tree, historical entire corpus, unrelated current catalog behaviors, arbitrary plugins or host combinations semantically certified.'},ensure_ascii=False,indent=2)+'\n')
result={'schema':'r7.u07.r2.additional-input-validation.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'root_full_readback_all_32_files_match':True,'prior_r1_fixed_tree_and_all_four_blobs_match':True,'copied_exact_inputs_and_receipts':paths,'skills_probe':[{ 'path':str(p),'exists':p.exists()} for p in [Path('/workspace/.agents/skills'),root/'.agents/skills',Path('/workspace/pokemon-essentials-clean-room/.agents/skills'),Path.home()/'.agents/skills']],'git_dispatch_agents_paths':git('ls-tree','-r','--name-only','c64774c60d91e522cb515ef71e3e9d4ea6b4712c','.agents').decode(),'base_top_tree':git('rev-parse','e646432c644dec04d306842cc5a559a29c718fbc^{tree}').decode().strip(),'base_formal_tree':git('rev-parse','e646432c644dec04d306842cc5a559a29c718fbc:deliverables/final-specification-set').decode().strip(),'qualification':'TOOL_VALIDATION only; prior r1 final WAIT remains; no configuration/behavior certification'}
(E/'additional-input-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
