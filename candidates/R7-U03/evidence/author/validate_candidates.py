"""Finite document-scope checks; never execute reference or behavior models."""
import difflib
import json
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
CONTRACT = json.loads(Path('/workspace/r7-bootstrap/R7-U03-author/delegation/contracts/R7-U03.json').read_bytes())
assert subprocess.check_output(['git','branch','--show-current'],cwd=ROOT).decode().strip() == 'codex/r7-u03-author-20261015-wave1'
required = {r['candidate_path'] for r in CONTRACT['paths'] if r['classification']=='required'}
actual = {str(p.relative_to(ROOT)) for p in (ROOT/'candidates/R7-U03/deliverables').rglob('*') if p.is_file()}
assert actual == required
assert not (ROOT/'candidates/R7-U03/deliverables/final-specification-set/generic-kernel').exists()
tracked_changes = subprocess.check_output(['git','diff','--name-only',B],cwd=ROOT).decode().splitlines()
assert all(p.startswith('candidates/R7-U03/') for p in tracked_changes)
untracked = subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=ROOT).decode().splitlines()
assert all(p.startswith('candidates/R7-U03/') for p in untracked)
allowed_original_changes = {
 'wp12-terrain-movement-vehicles.md':[(98,98),(102,102),(104,104),(108,108),(229,229),(238,238)],
 'wp61-field-passive-effects-and-blackout.md':[(15,15),(33,33),(188,188)],
 'engine-overworld-wp11-15-59-60.md':[(41,42),(118,118)],
 'engine-overworld-wp16.md':[(9,9),(26,26)],
 'pokemon-rules-wp53-60-61-62-69-70.md':[(116,116)],
}
diffs=[]; verified=[]
for row in CONTRACT['paths']:
 if row['classification']!='required':continue
 p=ROOT/row['candidate_path']; before=subprocess.check_output(['git','show',B+':'+row['path']],cwd=ROOT).decode(); after=p.read_text()
 changes=[]
 for tag,a,b,c,d in difflib.SequenceMatcher(None,before.splitlines(True),after.splitlines(True),autojunk=False).get_opcodes():
  if tag=='equal':continue
  changes.append(dict(kind=tag,original_lines_zero_based_half_open=[a,b],candidate_lines_zero_based_half_open=[c,d]))
  # Insertions are located immediately before original line a+1.
  assert any(lo<=a+1 and max(a+1,b)<=hi for lo,hi in allowed_original_changes[p.name]), (p.name,tag,a+1,b)
 oldrows=[x for x in before.splitlines() if x.startswith('| ')]
 edited_ids={'wp12-terrain-movement-vehicles.md':{'普通移动','碰撞'},'engine-overworld-wp11-15-59-60.md':{'MV01','MV02'},'engine-overworld-wp16.md':{'WR01'}}.get(p.name,set())
 for oldrow in oldrows:
  id=oldrow.split('|')[1].strip()
  if id not in edited_ids:assert oldrow in after, (p.name,id)
 for link in re.findall(r'\]\(([^)]+)\)',after):
  if link in re.findall(r'\]\(([^)]+)\)',before):continue
  if '://' in link or link.startswith('#'):continue
  target=(p.parent/link.split('#')[0]).resolve()
  logical=str(target.relative_to(ROOT/'candidates/R7-U03'))
  assert target.is_file() or subprocess.run(['git','cat-file','-e',B+':'+logical],cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE).returncode==0, link
 diffs.extend(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='B/'+row['path'],tofile=row['candidate_path']))
 verified.append(dict(path=row['candidate_path'],unchanged_old_table_rows=len(oldrows)-len(edited_ids),changes=changes))
for p in HERE.rglob('*.json'):
 json.loads(p.read_bytes())
(HERE/'candidate.diff').write_text(''.join(diffs))
result=dict(result='FINITE_DOCUMENT_CHECKS_COMPLETE',stage='TOOL_VALIDATION',mirrors=len(verified),files=verified,
    formal_reference_public_ledger_writes=0,conditional_wp06_write=False,
    all_non_target_table_rows_preserved=True,new_link_targets_resolve_in_candidate_plus_B_view=True,
    reference_behavior_execution=0,independent_model_execution=0,host_Demo_native_media_save_replay=0,
    semantic_PASS=False,qualification='Checks file scope, exact preserved text and syntax only; no semantic or independent acceptance.')
(HERE/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
