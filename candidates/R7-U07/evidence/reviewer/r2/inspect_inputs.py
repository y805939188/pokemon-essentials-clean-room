"""Read immutable inputs and record scoped content. No restored code execution."""
import hashlib,json,sys
from pathlib import Path
R=Path('/workspace/r7-context/R7-U07-reviewer')
C=Path('/workspace/r7-review-input/R7-U07-r2-2649ed2bd2cc3afdfa636cd643fc1975de5eae32/candidate/candidates/R7-U07')
def emit(p,start=1,end=None):
 p=Path(p);data=p.read_bytes();lines=data.decode().splitlines()
 print(json.dumps({'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'lines':len(lines),'read_lines':[start,end or len(lines)]},ensure_ascii=False))
 for i,line in enumerate(lines[start-1:end],start):print(f'{i:04}: {line}')
mode=sys.argv[1]
if mode=='counter':
 p=R/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs/bcf3539beb2c1c24c44f3cd426dd4b4a49752b1a39d30925effb32a36b6329d6.raw'
 d=p.read_bytes();v=json.loads(d)['challenges'][3]; print(d[50839:68277].decode());print('raw_sha256='+hashlib.sha256(d[50839:68277]).hexdigest())
elif mode=='original':
 p=R/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs/e0c5ebb227169d6a24ca470630bdc0c22f4ea8f8a70a89951fae64546dde22ae.raw'
 d=p.read_bytes();print(d[416485:450531].decode());print('raw_sha256='+hashlib.sha256(d[416485:450531]).hexdigest())
elif mode=='normalized':
 v=json.loads((R/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/normalized-record-candidates.json').read_bytes())['records'][14]
 print(json.dumps(v if len(sys.argv)==2 else v['groups'][sys.argv[2]],ensure_ascii=False,indent=2))
elif mode=='file':emit(sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 1,int(sys.argv[4]) if len(sys.argv)>4 else None)
elif mode=='limits':emit(R/'evidence/tasks/R7-C17/limits-and-alias-reception.json')
elif mode=='sources':
 for p in sorted((R/'inputs/reference').rglob('*.rb')):
  emit(p)
elif mode=='skills':
 for base in [Path('/workspace/.agents'),Path('/workspace/r7-u07-reviewer-r2/.agents'),Path('/workspace/pokemon-essentials-clean-room/.agents')]:
  print(str(base),'exists=',base.exists())
  if base.exists():
   for p in sorted(base.rglob('SKILL.md')):emit(p)
else:raise SystemExit('unsupported mode')
