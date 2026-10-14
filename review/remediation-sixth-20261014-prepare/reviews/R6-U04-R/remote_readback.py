"""Read every published reviewer blob in full at one immutable remote commit."""
import concurrent.futures, datetime, hashlib, json, pathlib, subprocess, sys, urllib.parse, urllib.request
ROOT = pathlib.Path('/workspace/pokemon-essentials-clean-room')
SCOPE = 'review/remediation-sixth-20261014-prepare/reviews/R6-U04-R'
BRANCH = 'codex/remediation-sixth-r6-u04-review-20261014'
COMMIT, OUTPUT = sys.argv[1:3]
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*args): return subprocess.check_output(['git','-C',str(ROOT),*args])
started=now()
argv=['git','-C',str(ROOT),'ls-remote','--heads','origin','refs/heads/'+BRANCH]
ref=subprocess.run(argv,capture_output=True)
assert ref.returncode==0,ref.stderr.decode()
assert ref.stdout.decode().split()[0]==COMMIT,ref.stdout.decode()
entries=git('ls-tree','-r',COMMIT,'--',SCOPE).decode().splitlines()
def fetch(entry):
    meta,path=entry.split('\t',1);mode,kind,blob=meta.split()
    assert kind=='blob'
    local=git('cat-file','blob',blob)
    url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+COMMIT+'/'+urllib.parse.quote(path,safe='/')
    attempts=[]
    for number in range(1,4):
        begin=now()
        try:
            with urllib.request.urlopen(url,timeout=30) as response:
                remote=response.read();http_status=response.status
            actual=dict(bytes=len(remote),sha256=hashlib.sha256(remote).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(remote)).encode()+b'\0'+remote).hexdigest())
            equal=remote==local and actual['git_blob']==blob
            attempts.append(dict(number=number,utc_start=begin,utc_end=now(),http_status=http_status,actual=actual,full_byte_equal=equal))
            return dict(path=path,mode=mode,type=kind,commit=COMMIT,url=url,result='PASS_FULL_REMOTE_BYTES' if equal else 'FAIL',attempts=attempts)
        except Exception as error:
            attempts.append(dict(number=number,utc_start=begin,utc_end=now(),error=str(error)))
    return dict(path=path,mode=mode,type=kind,commit=COMMIT,url=url,result='FAIL',attempts=attempts)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: rows=list(pool.map(fetch,entries))
result=dict(schema='R6-U04-R.full-remote-readback.v1',utc_start=started,utc_end=now(),cwd=str(ROOT),argv=sys.argv,
            commit=COMMIT,workspace_tree=git('rev-parse',COMMIT+'^{tree}').decode().strip(),review_directory_tree=git('rev-parse',COMMIT+':'+SCOPE).decode().strip(),
            branch=BRANCH,branch_ref_process=dict(argv=argv,exit=ref.returncode,stdout=ref.stdout.decode(),stderr=ref.stderr.decode()),
            identity_method='Remote Git ref equals immutable commit. That content-addressed commit fixes local tree/path/mode/type. Every listed blob independently downloaded fully from its fixed remote raw URL; bytes/SHA256/Git blob compared. No metadata API or behavior execution claim.',
            payload_count=len(rows),payloads=rows,all_payloads_full_byte_equal=all(r['result']=='PASS_FULL_REMOTE_BYTES' for r in rows),
            reference_execution=0,behavior_model_execution=0,host_demo_execution=0)
path=ROOT/OUTPUT
assert path.is_relative_to(ROOT/SCOPE)
path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['payloads','branch_ref_process']},ensure_ascii=False))
sys.exit(0 if result['all_payloads_full_byte_equal'] else 1)
