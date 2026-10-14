"""One local audit reviewer; real JSONL output, PID, exit and timestamps."""
import datetime,json,pathlib,subprocess,sys,time
root=pathlib.Path(__file__).resolve().parents[1];task=sys.argv[1];out=root/'tasks'/task;out.mkdir(exist_ok=True)
argv=['codex','exec','-C',str(root.parents[2]),'-m','gpt-6.1-sol','-c','model_reasoning_effort="ultra"','-c','service_tier="default"','--json','--color','never','-o',str(out/'last-message.md'),'-']
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
status={'logical_id':task,'argv':argv,'started_at':now(),'state':'RUNNING','requested_model':'gpt-6.1-sol','requested_effort':'ultra','requested_tier':'default','requested_speed':'default','actual_model_effort_tier_speed':'UNVERIFIED','update_started':False}
with (out/'prompt.md').open('rb') as inp,(out/'stdout.jsonl').open('wb') as stdout,(out/'stderr.log').open('wb') as stderr:
    p=subprocess.Popen(argv,stdin=inp,stdout=stdout,stderr=stderr,cwd=root.parents[2]);status['pid']=p.pid
    (out/'launcher-status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n');print(json.dumps(status,ensure_ascii=False),flush=True)
    code=p.wait()
status.update(state='COMPLETED' if code==0 else 'FAILED',exit_code=code,ended_at=now())
(out/'launcher-status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(status,ensure_ascii=False),flush=True)
sys.exit(code)
