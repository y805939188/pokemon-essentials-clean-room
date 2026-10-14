"""Read inert fixed Git bytes; record selected complete UTF-8 fragment. No project code import/evaluation."""
import sys,subprocess,hashlib,json,datetime
from pathlib import Path
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
commit,path,lo,hi=sys.argv[1:];lo=int(lo);hi=int(hi)
run=subprocess.run(['git','show',commit+':'+path],capture_output=True)
if run.returncode:
    sys.stderr.buffer.write(run.stderr);sys.exit(run.returncode)
b=run.stdout;lines=b.splitlines(keepends=True)
assert 1<=lo<=hi<=len(lines)
selected=b''.join(lines[lo-1:hi]);selected.decode('utf-8')
entry=subprocess.check_output(['git','ls-tree',commit,'--',path]).decode().strip()
rec={'commit':commit,'path':path,'tree':subprocess.check_output(['git','rev-parse',commit+'^{tree}']).decode().strip(),'entry':entry,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'total_lines':len(lines),'semantic_read_range':[lo,hi],'selected_bytes':len(selected),'selected_sha256':hashlib.sha256(selected).hexdigest(),'argv':sys.argv,'git_argv':['git','show',commit+':'+path],'cwd':str(Path.cwd()),'utc_start':start,'utc_end':datetime.datetime.now(datetime.timezone.utc).isoformat(),'git_exit':run.returncode,'git_stderr':run.stderr.decode(),'runtime':sys.version,'evidence_level':'SOURCE_STATIC_READ_OR_FORMAL_READ_NO_EXECUTION','scope':'Complete selected fragment emitted in current tool transcript; hash is not semantic PASS.'}
with (Path(__file__).parent/'read-ledger.jsonl').open('a') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
print(f'{path} @ {commit} : lines {lo}–{hi}')
sys.stdout.buffer.write(selected)
