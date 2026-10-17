#!/usr/bin/env python3
"""Run inspected document-only author checks on exact bytes in an isolated clone."""
from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,sys,tempfile
sys.dont_write_bytecode=True
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1];E=OUT/'evidence';PREFIX='planning/implementation-routing/r8-20261017'
CANDIDATE='a32873d2860b15d9f5e27727db8f131f4ec433b6';records=[]
def save(n,v):(E/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def run(argv,cwd):
 started=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(argv,cwd=cwd,capture_output=True,text=True)
 rec={'argv':list(map(str,argv)),'cwd':str(cwd),'started_utc':started,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr};records.append(rec);save('tool-replay-io.json',records)
 assert r.returncode==0,rec
 return r.stdout
fixture=Path(tempfile.mkdtemp(prefix='r2-static-clean-'))/'clone'
run(['git','clone','--shared','--no-checkout','--no-hardlinks',str(ROOT),str(fixture)],ROOT)
run(['git','sparse-checkout','set','--cone',PREFIX],fixture)
run(['git','checkout','--detach',CANDIDATE],fixture)
assert not run(['git','status','--porcelain'],fixture)
src=fixture/PREFIX
inventory=[]
for p in sorted((ROOT/PREFIX).rglob('*')):
 if p.is_file():
  rel=p.relative_to(ROOT/PREFIX);assert (src/rel).read_bytes()==p.read_bytes(),rel
  inventory.append({'path':str(rel),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
save('isolated-tool-inputs.json',{'candidate':CANDIDATE,'fixture':str(fixture),'mode':'LOCAL_SHARED_OBJECT_STATIC_FIXTURE_NOT_FRESH_REMOTE_PROOF','all_author_files_byte_identical':inventory,'reason':'preservation-check scans all untracked paths; a clean isolated clone avoids treating reviewer-owned reports as author mutations. No author check is weakened.'})
run([sys.executable,str(src/'revisions/r2/tools/run-author-checks.py'),'--phase','r2-fixed-source'],fixture)
names=['revisions/r2/tools/actual-command-io.json','revisions/r2/tools/actual-results.json','revisions/r2/tools/navigation-results.json','revisions/r2/tools/preservation-results.json','validator-negative-checks.json']
for name in names:shutil.copyfile(src/name,E/('replay-'+Path(name).name))
io=json.loads((src/'revisions/r2/tools/actual-command-io.json').read_bytes());assert io['all_commands_exit_zero']and io['all_input_hashes_stable']and len(io['commands'])==7
for name,sha in io['initial_input_sha256'].items():assert hashlib.sha256((ROOT/PREFIX/name).read_bytes()).hexdigest()==sha,name
generated=[]
for p in sorted((src/'views').glob('*.md')):
 rel=p.relative_to(src);generated.append({'path':str(rel),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'equal_candidate':p.read_bytes()==(ROOT/PREFIX/rel).read_bytes()})
for name in ['coverage.md','coverage-summary.json','validation-result.json']:
 p=src/name;generated.append({'path':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'equal_candidate':p.read_bytes()==(ROOT/PREFIX/name).read_bytes()})
assert len(generated)==11 and all(x['equal_candidate']for x in generated)
save('tool-replay-summary.json',{'candidate':CANDIDATE,'commands':7,'all_exit_zero':True,'all13_input_hashes_stable_and_equal_candidate':True,'author27':'PASS_REPLAY_ONLY','self_test9':'PASS_REPLAY_ONLY','navigation2':'PASS_REPLAY_ONLY','preservation12':'PASS_REPLAY_ONLY','rendered_files':generated,'future5_accepted_fixtures_and_cumulative_current_coverage':'NOT_EXECUTED_AWAITING_U04; no PASS','fixture':str(fixture),'author_candidate_not_modified':True,'scope':'Document/Git static tests only; domain semantics independent.'})
print(json.dumps({'fixture':str(fixture),'commands':7,'inputs':len(io['initial_input_sha256']),'all_passed':True,'generated_equal':11}))
