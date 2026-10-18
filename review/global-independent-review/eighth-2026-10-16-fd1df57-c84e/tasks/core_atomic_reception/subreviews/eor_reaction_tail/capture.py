import subprocess,sys,datetime,json,hashlib,pathlib
p=pathlib.Path(__file__).parent
name=sys.argv[1]
cmd=sys.argv[2:]
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
r=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
end=datetime.datetime.now(datetime.timezone.utc).isoformat()
(p/(name+".stdout")).write_bytes(r.stdout)
(p/(name+".stderr")).write_bytes(r.stderr)
rec={"name":name,"argv":cmd,"start_utc":start,"end_utc":end,"exit_code":r.returncode,"stdout_bytes":len(r.stdout),"stdout_sha256":hashlib.sha256(r.stdout).hexdigest(),"stderr_bytes":len(r.stderr),"stderr_sha256":hashlib.sha256(r.stderr).hexdigest(),"category":"SOURCE_STATIC_OR_TOOL_VALIDATION","business_execution":"NOT_EXECUTED"}
with (p/"io-ledger.jsonl").open("a") as f:f.write(json.dumps(rec,ensure_ascii=False)+"\n")
print(json.dumps(rec,ensure_ascii=False))
sys.stdout.flush()
sys.stdout.buffer.write(r.stdout)
sys.stderr.buffer.write(r.stderr)
sys.exit(r.returncode)
