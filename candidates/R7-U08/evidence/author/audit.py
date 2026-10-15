"""Public command recorder; never invokes restored reference programs."""
import datetime, json, os, pathlib, subprocess, sys
root=pathlib.Path(__file__).resolve().parent
name=sys.argv[1]
argv=sys.argv[2:]
assert name and all(c.isalnum() or c in "-_" for c in name)
prefix=root/"commands"/name
assert not prefix.with_suffix(".json").exists()
utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
start=utc()
p=subprocess.Popen(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err=p.communicate()
prefix.with_suffix(".stdout").write_bytes(out)
prefix.with_suffix(".stderr").write_bytes(err)
record={"argv":argv,"cwd":os.getcwd(),"recorder_pid":os.getpid(),"process_pid":p.pid,"start_utc":start,"end_utc":utc(),"exit_code":p.returncode,"stdout":prefix.with_suffix(".stdout").name,"stderr":prefix.with_suffix(".stderr").name,"qualification":"Real command I/O; exit zero is not semantic acceptance."}
prefix.with_suffix(".json").write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n")
sys.stdout.buffer.write(out);sys.stderr.buffer.write(err)
raise SystemExit(p.returncode)
