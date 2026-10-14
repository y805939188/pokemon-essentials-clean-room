#!/usr/bin/env python3
"""Read every candidate payload at a published immutable commit; no mutations."""
from pathlib import Path
import argparse,subprocess,datetime,json,hashlib,urllib.request,urllib.parse,concurrent.futures
p=argparse.ArgumentParser();p.add_argument('commit');p.add_argument('output');a=p.parse_args()
root=Path.cwd();scope='review/remediation-sixth-20261014-prepare/candidates/R6-U04';branch='codex/remediation-sixth-r6-u04-author-20261014'
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
start=now();argv=['git','ls-remote','--heads','origin',branch];remote=subprocess.run(argv,capture_output=True,text=True)
assert remote.returncode==0,remote.stderr
assert remote.stdout.split()[0]==a.commit,remote.stdout
entries=subprocess.check_output(['git','ls-tree','-r',a.commit,'--',scope],text=True).splitlines()
def read_one(line):
    fields,path=line.split('\t',1);mode,kind,sha=fields.split();assert kind=='blob'
    expected=subprocess.check_output(['git','cat-file','blob',a.commit+':'+path]);attempts=[]
    url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+a.commit+'/'+urllib.parse.quote(path,safe='/')
    for number in range(1,4):
        t=now()
        try:
            with urllib.request.urlopen(url,timeout=30) as res:b=res.read();status=res.status
            actual={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
            ok=b==expected and actual['git_blob']==sha
            attempts.append({'attempt':number,'utc_start':t,'utc_end':now(),'http_status':status,'actual':actual,'byte_equal':ok})
            return {'path':path,'commit':a.commit,'mode':mode,'type':kind,'git_blob':sha,'result':'PASS_FULL_REMOTE_PAYLOAD' if ok else 'FAIL','attempts':attempts}
        except Exception as e:attempts.append({'attempt':number,'utc_start':t,'utc_end':now(),'error':str(e)})
    return {'path':path,'commit':a.commit,'mode':mode,'type':kind,'git_blob':sha,'result':'FAIL','attempts':attempts}
rows=list(concurrent.futures.ThreadPoolExecutor(max_workers=6).map(read_one,entries))
result={'schema':'R6-U04.full-remote-payload-readback.v1','argv':['python3',__file__,a.commit,a.output],'cwd':str(root),'utc_start':start,'utc_end':now(),'commit':a.commit,'workspace_tree':subprocess.check_output(['git','rev-parse',a.commit+'^{tree}'],text=True).strip(),'candidate_directory_tree':subprocess.check_output(['git','rev-parse',a.commit+':'+scope],text=True).strip(),'remote_branch_check':{'argv':argv,'exit':remote.returncode,'stdout':remote.stdout,'stderr':remote.stderr},'identity_method':'Remote branch SHA equals immutable local commit/tree; mode/type/path from that content-addressed tree; every blob independently fully downloaded at fixed remote raw URL and byte/hash/blob compared. No remote metadata API success claimed.','payload_count':len(rows),'payloads':rows,'all_payloads_equal':all(r['result']=='PASS_FULL_REMOTE_PAYLOAD' for r in rows),'reference_or_model_execution':False,'independent_review':False}
Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['payloads','remote_branch_check']},ensure_ascii=False))
raise SystemExit(0 if result['all_payloads_equal'] else 1)
