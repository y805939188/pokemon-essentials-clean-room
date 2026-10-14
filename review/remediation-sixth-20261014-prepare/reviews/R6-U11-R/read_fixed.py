import sys,json,subprocess,hashlib,datetime,pathlib
root=pathlib.Path(__file__).resolve().parent
commit,path,start,end=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
argv=["git","show",commit+":"+path]
begin=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=subprocess.run(argv,capture_output=True)
finish=datetime.datetime.now(datetime.timezone.utc).isoformat()
if p.returncode:
 out=p.stdout
else:
 rows=p.stdout.decode("utf-8").splitlines(keepends=True)
 out="".join(rows[start-1:end]).encode("utf-8")
record={"reader":"R6-U11-R /root","cwd":str(pathlib.Path.cwd()),"argv":argv,"start_utc":begin,"end_utc":finish,"exit_code":p.returncode,"stderr":p.stderr.decode("utf-8",errors="replace"),"commit":commit,"path":path,"lines":[start,end],"payload_bytes":len(p.stdout),"payload_sha256":hashlib.sha256(p.stdout).hexdigest(),"payload_git_blob":hashlib.sha1(b"blob "+str(len(p.stdout)).encode()+b"\0"+p.stdout).hexdigest(),"stdout_range_bytes":len(out),"stdout_range_sha256":hashlib.sha256(out).hexdigest(),"evidence_level":"SOURCE_STATIC_OR_DOCUMENT_READ","stdout_location":"task tool transcript; source not duplicated into specification"}
with (root/"reading-ledger.jsonl").open("a") as f:f.write(json.dumps(record,ensure_ascii=False)+"\n")
sys.stdout.buffer.write(out)
sys.stderr.buffer.write(p.stderr)
sys.exit(p.returncode)
