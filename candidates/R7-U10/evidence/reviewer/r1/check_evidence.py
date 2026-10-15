"""Check semantic evidence formatting and exact write scope; preserve literal raw logs."""
import hashlib, json, pathlib, subprocess
p=pathlib.Path(__file__).parent
prefix='candidates/R7-U10/evidence/reviewer/r1/'
B='e646432c644dec04d306842cc5a559a29c718fbc'
for f in p.rglob('*.json'):json.loads(f.read_bytes())
paths=[str(f) for f in p.rglob('*') if f.is_file() and f.suffix in ['.md','.json','.py']]
r=subprocess.run(['git','diff','--cached','--check','--',*paths],capture_output=True)
print(r.stdout.decode(),end='');print(r.stderr.decode(),end='');assert r.returncode==0
tracked=subprocess.check_output(['git','diff','--name-only','-z',B]).split(b'\0')
untracked=subprocess.check_output(['git','ls-files','--others','--exclude-standard','-z']).split(b'\0')
assert all(not s or s.decode().startswith(prefix) for s in tracked+untracked)
assert all(not f.is_symlink() for f in p.rglob('*'))
per=json.loads((p/'per-id.json').read_bytes())
assert len(per['records'])==3 and sum(len(r['checks']) for r in per['records'])==38
assert per['overall_workflow_verdict']=='WAIT_INPUT_OR_INDEPENDENCE'
assert all(r['content_verdict']=='PASS_SCOPED_CANDIDATE' and not r['ACCEPTED'] and not r['CLOSED'] for r in per['records'])
print('Structured evidence whitespace/JSON, 38 scoped static assessments and exact write scope OK. Raw stdout and unified patch context whitespace preserved without editing.')
