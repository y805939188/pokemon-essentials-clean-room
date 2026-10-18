from pathlib import Path
import subprocess,sys,json,datetime,hashlib
root=Path(__file__).resolve().parents[1]
name=sys.argv[1]
if not name.replace('_','').isalnum(): raise SystemExit('invalid logical task ID')
prompt=root/'delegation/prompts'/f'{name}.md'
task=root/'tasks'/name
task.mkdir(parents=True,exist_ok=True)
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
command=['codex','exec','--strict-config','--ephemeral','--json','--color','never','--skip-git-repo-check','-C',str(task),'-s','workspace-write','-m','gpt-6.1-sol','-c','model_reasoning_effort="ultra"','-c','service_tier="default"','-o',str(task/'final-message.md'),'-']
record={'logical_id':name,'status':'STARTING','started_utc':now(),'command':command,'prompt_path':str(prompt),'prompt_bytes':prompt.stat().st_size,'prompt_sha256':hashlib.sha256(prompt.read_bytes()).hexdigest(),'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'Fast off'},'actual':dict.fromkeys(['model','effort','tier','speed'],'UNVERIFIED'),'update_started':False}
def save(): (task/'launcher-status.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
save()
with prompt.open('rb') as inp,(task/'events.jsonl').open('wb') as out,(task/'launcher.stderr').open('wb') as err:
 child=subprocess.Popen(command,stdin=inp,stdout=out,stderr=err)
 record.update(status='RUNNING',pid=child.pid,updated_utc=now());save()
 code=child.wait()
record.update(status='EXITED' if code==0 else 'FAILED',exit_code=code,ended_utc=now());save()
print(json.dumps({'logical_id':name,'pid':child.pid,'exit_code':code,'semantic_acceptance':'NOT_IMPLIED_BY_EXIT'},ensure_ascii=False))
