#!/usr/bin/env python3
"""Capture ordinary Git publication and full fixed-commit remote byte readback."""
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import urllib.parse
import urllib.request

OWN=Path(__file__).resolve().parent
ROOT=OWN.parents[3]
REL=OWN.relative_to(ROOT).as_posix()
BRANCH="codex/remediation-sixth-r6-u02-review-20261014"
AUTHOR="bc570b4e84bc9ef1510228dd69e25a9958e23545"
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def identity(b):return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest(),"git_blob":hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()}
def git(*args):return subprocess.check_output(["git",*args],cwd=ROOT)
def write(name,x):(OWN/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n")
mode=sys.argv[1]
if mode=="manifest":
    files=[]
    for p in sorted(OWN.iterdir()):
        if p.is_file() and p.name!="package-manifest.json":
            files.append({"path":p.relative_to(ROOT).as_posix(),"mode":"100644","git_type":"blob",**identity(p.read_bytes())})
    write("package-manifest.json",{"schema":"R6-U02-R-finite-core-manifest-v1","created_UTC":now(),"candidate_commit":AUTHOR,"entry":REL+"/REPORT.md","files":files,"exclusions":["package-manifest.json (itself)","later publication receipts/attempts are successor payloads, verified at their own fixed commit"],"core_commit_tree":"Bound externally after commit; no self-reference"})
    print(json.dumps({"manifest_entries":len(files)}))
elif mode=="push":
    number=sys.argv[2];start=now();argv=["git","push","-u","origin","HEAD:refs/heads/"+BRANCH]
    p=subprocess.run(argv,cwd=ROOT,capture_output=True,text=True)
    record={"argv":argv,"cwd":str(ROOT),"UTC_start":start,"UTC_end":now(),"stdout":p.stdout,"stderr":p.stderr,"exit":p.returncode,"commit":git("rev-parse","HEAD").decode().strip(),"force":False,"deletion":False}
    write("push-attempt-"+number+".json",record);print(json.dumps(record,ensure_ascii=False));sys.exit(p.returncode)
elif mode=="readback":
    commit,output=sys.argv[2:4];start=now()
    paths=git("diff","--name-only",AUTHOR,commit).decode().splitlines()
    assert paths and all(p.startswith(REL+"/") for p in paths)
    tree=git("rev-parse",commit+"^{tree}").decode().strip()
    directory_tree=git("rev-parse",commit+":"+REL).decode().strip()
    listing=git("ls-tree","-r",commit,"--",REL).decode().splitlines()
    objects={}
    for line in listing:
        meta,path=line.split("\t",1);md,typ,blob=meta.split();objects[path]=(md,typ,blob)
    assert set(paths)==set(objects),"unexpected or omitted reviewer payload"
    def fetch(path):
        begin=now();md,typ,blob=objects[path]
        local=git("show",commit+":"+path)
        url="https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/"+commit+"/"+urllib.parse.quote(path,safe="/")
        with urllib.request.urlopen(url,timeout=45) as response:
            remote=response.read();status=response.status
        row={"path":path,"commit":commit,"mode":md,"git_type":typ,"UTC_start":begin,"UTC_end":now(),"url":url,"http_status":status,"local":identity(local),"remote_full_byte_readback":identity(remote),"exact_bytes_equal":local==remote}
        assert md=="100644" and typ=="blob" and identity(remote)["git_blob"]==blob and local==remote,row
        return row
    rows=[];errors=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futures={pool.submit(fetch,path):path for path in paths}
        for future in concurrent.futures.as_completed(futures):
            try:rows.append(future.result())
            except Exception as e:errors.append({"path":futures[future],"error":repr(e)})
    advertised=git("ls-remote","origin","refs/heads/"+BRANCH).decode().strip()
    receipt={"schema":"R6-U02-R-finite-publication-readback-v1","argv":sys.argv,"cwd":str(ROOT),"UTC_start":start,"UTC_end":now(),"fixed_commit":commit,"workspace_tree":tree,"report_directory_tree":directory_tree,"remote_branch":BRANCH,"advertised_remote_head":advertised,"payload_count":len(paths),"complete_byte_readback_count":len(rows),"rows":sorted(rows,key=lambda x:x['path']),"errors":errors,"scope":"Every new reviewer payload relative to frozen author; full bytes, path/mode/type/blob/SHA and exact finite directory listing. This receipt cannot bind its own future commit.","result":"PASS" if not errors and len(rows)==len(paths) and advertised.startswith(commit+"\t") else "FAIL"}
    write(output,receipt)
    print(json.dumps({k:receipt[k] for k in ["result","fixed_commit","workspace_tree","report_directory_tree","payload_count","complete_byte_readback_count","errors"]},ensure_ascii=False))
    sys.exit(0 if receipt['result']=="PASS" else 1)
else:raise ValueError(mode)
