"""Read every frozen payload from raw GitHub at an immutable commit and hash it.

This verifies transport only. It neither executes downloaded content nor grants
semantic reading credit. Output is written only to an explicit caller path.
"""
import argparse, concurrent.futures, datetime, hashlib, json, pathlib, subprocess, tempfile, urllib.parse
p=argparse.ArgumentParser()
p.add_argument('commit')
p.add_argument('manifest')
p.add_argument('output')
a=p.parse_args()
assert len(a.commit)==40 and all(c in '0123456789abcdef' for c in a.commit)
manifest=json.loads(pathlib.Path(a.manifest).read_text())
repo='y805939188/pokemon-essentials-clean-room'
def check(row):
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    url='https://raw.githubusercontent.com/'+repo+'/'+a.commit+'/'+urllib.parse.quote(row['path'],safe='/')
    with tempfile.NamedTemporaryFile(prefix='r8-ability-remote-',dir='/tmp') as f:
        r=subprocess.run(['curl','--fail','--silent','--show-error','--location','--connect-timeout','10','--max-time','45',url,'-o',f.name],capture_output=True)
        raw=pathlib.Path(f.name).read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    sha=hashlib.sha256(raw).hexdigest()
    ok=r.returncode==0 and len(raw)==row['bytes'] and sha==row['sha256'] and blob==row['git_blob']
    return {'path':row['path'],'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'transport':'full raw HTTPS GET at fixed commit; complete response read_bytes, no range limit','curl_exit':r.returncode,'stderr':r.stderr.decode(errors='replace'),'bytes':len(raw),'sha256':sha,'git_blob':blob,'expected_git_mode':row.get('mode'),'match':ok,'semantic_credit':0}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
    results=list(ex.map(check,manifest['files']))
result={'schema':'gr8-ability-full-remote-readback/v1','commit':a.commit,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':results,'all_match':all(x['match'] for x in results),'qualification':'Full file bytes remotely read. Git modes/directory tree are bound by separately verified same immutable commit, not inferred from raw HTTP headers. No semantic or business credit.'}
pathlib.Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'commit':a.commit,'files':len(results),'all_match':result['all_match'],'output':a.output}))
raise SystemExit(0 if result['all_match'] else 1)
