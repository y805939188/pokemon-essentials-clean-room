#!/usr/bin/env python3
"""Independent payload, diff and historical-span checks. Does not execute R."""
import datetime
import difflib
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
OWN = Path(__file__).resolve().parent
PRE = "review/remediation-sixth-20261014-prepare/"
PUB = "bc570b4e84bc9ef1510228dd69e25a9958e23545"
BASE = "8ea169fbd0f33f378b5d732fd6bea59e854e04a6"
R = "8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b"
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
commands = []
def git(*args):
    argv = ["git", *args]
    begin = datetime.datetime.now(datetime.timezone.utc).isoformat()
    p = subprocess.run(argv, cwd=ROOT, capture_output=True)
    commands.append({"argv":argv,"cwd":str(ROOT),"UTC_start":begin,
                     "UTC_end":datetime.datetime.now(datetime.timezone.utc).isoformat(),
                     "exit":p.returncode,"stdout_bytes":len(p.stdout),
                     "stdout_sha256":hashlib.sha256(p.stdout).hexdigest(),"stderr":p.stderr.decode()})
    if p.returncode: raise RuntimeError((argv,p.stderr.decode()))
    return p.stdout
def ident(b):
    return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest(),
            "git_blob":hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()}
contract = json.loads((ROOT/(PRE+"contracts/R6-U02.json")).read_text())
payloads = {}
def walk(v):
    if isinstance(v,dict):
        if "payload_identity" in v:
            x=v["payload_identity"]; payloads[(x["commit"],x["path"])]=x
        for x in v.values(): walk(x)
    elif isinstance(v,list):
        for x in v: walk(x)
walk(contract)
for x in json.loads((ROOT/(PRE+"candidates/R6-U02/evidence/supplemental-inputs.json")).read_text()):
    payloads[(x["commit"],x["path"])]=x
identities=[]
for (commit,path), expected in sorted(payloads.items()):
    b=git("show",commit+":"+path)
    actual=ident(b)
    for k,val in actual.items(): assert expected[k]==val,(path,k)
    mode,kind,blob,_=git("ls-tree",commit,"--",path).decode().split(maxsplit=3)
    assert mode==expected["mode"] and kind=="blob" and blob==actual["git_blob"]
    identities.append({"commit":commit,"path":path,"mode":mode,"git_type":kind,**actual,"result":"MATCH"})
assert git("rev-parse",PUB+"^{tree}").decode().strip()=="e7667bb80c89444708348e619c3feea0d315954a"
assert git("rev-parse",R+"^{tree}").decode().strip()=="7589c800b61ba13a13040ed0d686979b80a84fd0"
assert git("rev-parse",PUB+":deliverables/final-specification-set")==git("rev-parse",BASE+":deliverables/final-specification-set")
mirror=[]; changes=[]
author_manifest=json.loads((ROOT/(PRE+"candidates/R6-U02/evidence/candidate-mirror-manifest.json")).read_text())
for row in author_manifest:
    path=row["formal_path"]; cp=PRE+"candidates/R6-U02/mirror/"+path
    old=git("show",BASE+":"+path); new=git("show",PUB+":"+cp)
    assert (ROOT/cp).read_bytes()==new
    assert ident(old)==row["baseline"] and ident(new)==row["candidate"]
    mode,kind,blob,_=git("ls-tree",PUB,"--",cp).decode().split(maxsplit=3)
    assert mode=="100644" and kind=="blob" and blob==ident(new)["git_blob"]
    mirror.append({"formal_path":path,"candidate_path":cp,"commit":PUB,"mode":mode,"git_type":kind,"baseline":ident(old),"candidate":ident(new)})
    ops=difflib.SequenceMatcher(None,old.decode().splitlines(),new.decode().splitlines(),autojunk=False).get_opcodes()
    changes.append({"path":path,"changed_spans":[{"kind":k,"baseline":[a+1,b],"candidate":[c+1,d]} for k,a,b,c,d in ops if k!="equal"]})
assert sorted(x["formal_path"] for x in mirror)==sorted(contract["candidate_formal_paths"])
spans=[]
historical=json.loads((ROOT/(PRE+"candidates/R6-U02/evidence/historical-span-validation.json")).read_text())
for row in historical:
    old=git("show",row["commit"]+":"+row["path"]).splitlines(keepends=True)
    new=(ROOT/(PRE+"candidates/R6-U02/mirror/"+row["path"])).read_bytes().splitlines(keepends=True)
    a,b=row["lines"]; c,d=row["candidate_lines"]
    before=b"".join(old[a-1:b]); after=b"".join(new[c-1:d])
    assert before==after and hashlib.sha256(before).hexdigest()==row["span_sha256"],row
    spans.append({"id":row["id"],"path":row["path"],"historical_commit":row["commit"],"historical_lines":[a,b],"candidate_lines":[c,d],"span_sha256":row["span_sha256"],"result":"EXACT_UNCHANGED_BYTES"})
assert len(spans)==23
prompt=(ROOT/(PRE+"prompts/R6-U02-R.md")).read_bytes()
assert ident(prompt)=={"bytes":215630,"sha256":"36b77f3c43a9a0f912cc6a9444c1604b8b099381bb0b79844f0f5902b013b337","git_blob":"5d15fde0102a19600c52c5b83edd2e164c4e5be6"}
blocks=re.findall(r"```json\n(.*?)\n```",prompt.decode(),re.S)
assert json.loads(blocks[0])==contract
evidence=[]
for eid, x in json.loads(blocks[1]).items():
    b=(ROOT/(PRE+"inputs/evidence/"+x["path"])).read_bytes()
    assert all(ident(b)[k]==x[k] for k in ["bytes","sha256","git_blob"]),(eid,x["path"])
    evidence.append({"id":eid,"path":x["path"],**ident(b),"result":"MATCH"})
author_delta=git("diff","--name-only","469a268b92daed7b4d28d7fd0da75520cbb7228f",PUB).decode().splitlines()
assert all(p.startswith(PRE+"candidates/R6-U02/") for p in author_delta)
own_delta=git("status","--porcelain","--untracked-files=all").decode().splitlines()
assert all(PRE+"reviews/R6-U02-R" in p for p in own_delta),own_delta
result={"schema":"R6-U02-R-independent-static-verification-v1","UTC_start":start,
        "UTC_end":datetime.datetime.now(datetime.timezone.utc).isoformat(),"argv":sys.argv,
        "cwd":str(ROOT),"runtime":sys.version,"level":"TOOL_VALIDATION",
        "behavior_execution":False,"candidate_commit":PUB,"candidate_workspace_tree":"e7667bb80c89444708348e619c3feea0d315954a",
        "prompt_identity":ident(prompt),"contract_identity":ident((ROOT/(PRE+"contracts/R6-U02.json")).read_bytes()),
        "fixed_payloads":identities,"candidate_mirrors":mirror,"candidate_changes":changes,
        "historical_spans":spans,"evidence_cache_identities":evidence,
        "candidate_delta_count":len(author_delta),"candidate_delta":author_delta,
        "effective_model_effort_tier_speed_UUID":"UNVERIFIED; no valid platform echo; no CLI probe",
        "ruby_path":shutil.which("ruby"),"new_reference_execution":0,
        "result":"PASS_IDENTITY_DIFF_AND_SPAN_CHECKS_ONLY"}
(OWN/"verification.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
(OWN/"verification-commands.json").write_text(json.dumps(commands,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"result":result["result"],"fixed_payloads":len(identities),"mirror_count":len(mirror),"historical_spans":len(spans),"evidence_cache_count":len(evidence),"author_delta_count":len(author_delta),"ruby_path":result["ruby_path"]},ensure_ascii=False))
