#!/usr/bin/env python3
"""Finite candidate package safety, syntax and scope verification."""
from pathlib import Path
import subprocess,json,hashlib,ast,datetime
E=Path(__file__).resolve().parent; B=E.parents[2];REPO=B.parents[1]
PREP='469a268b92daed7b4d28d7fd0da75520cbb7228f';C=json.loads((B/'contracts/R6-U05.json').read_text())
def git(*a):return subprocess.check_output(['git',*a],cwd=REPO)
mirror={str((E.parent/'mirror'/p).relative_to(REPO)) for p in C['candidate_formal_paths']}
eprefix=str(E.relative_to(REPO))+'/'
tracked=git('diff','--name-only',PREP).decode().splitlines();untracked=git('ls-files','--others','--exclude-standard').decode().splitlines()
assert all(p in mirror or p.startswith(eprefix) for p in tracked+untracked)
assert git('branch','--show-current').decode().strip()=='codex/remediation-sixth-r6-u05-author-20261014'
assert git('merge-base',PREP,'HEAD').decode().strip()==PREP
assert git('diff','--check').strip()==b''
checked=[]
for p in sorted(E.rglob('*')):
 if not p.is_file():continue
 b=p.read_bytes();assert b'\0' not in b
 if p.suffix=='.json':json.loads(b)
 elif p.suffix=='.jsonl':
  for row in b.splitlines():json.loads(row)
 elif p.suffix=='.py':ast.parse(b,filename=str(p))
 checked.append(str(p.relative_to(REPO)))
assert len(json.loads((E/'author-results.json').read_text())['per_id'])==4
assert len(json.loads((E/'historical-verification.json').read_text())['records'])==41
R={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'level':'TOOL_VALIDATION','result':'FINITE_PACKAGE_SCOPE_SYNTAX_PROTECTION_CHECKS_CONFIRMED','tracked_changes':tracked,'untracked_changes':untracked,'evidence_files_checked':checked,'formal_paths_allowed':sorted(mirror),'protected_formal_originals':'No tracked difference outside allowed candidate mirror/evidence relative to PREP; 8 actual formal originals already byte-equal fixed main in validation-results.json','branch_base':'Exact PREP ancestor; no main merge/mutation','reference_model_host_execution':0,'independent_review':'PENDING_NON_AUTHOR'}
(E/'package-check.json').write_text(json.dumps(R,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result':R['result'],'mirrors':len(mirror),'evidence_files_parsed':len(checked),'outside_write_set':0},ensure_ascii=False))
