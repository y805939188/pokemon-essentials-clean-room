"""Manual future batch launcher; current review never calls --launch.

This is a small argv/stdio/PID receipt wrapper, not an automation or scheduler.
Without --launch it only prints the exact resolved request. It never changes Git.
"""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import subprocess

B='e646432c644dec04d306842cc5a559a29c718fbc'
FT='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--project',required=True);ap.add_argument('--package',required=True)
    ap.add_argument('--entry',required=True);ap.add_argument('--launch',action='store_true')
    ap.add_argument('--status',action='store_true');a=ap.parse_args()
    project=Path(a.project).resolve(); package=Path(a.package).resolve()
    requests=json.loads((package/'cli-invocations.json').read_bytes())
    matches=[v for v in requests if v['entry_id']==a.entry]
    if len(matches)!=1:raise ValueError('unknown or duplicate exact entry ID')
    row=matches[0];role=row['role'];batch=a.entry[:-2]
    expected_logroot=(project/'candidates'/batch/'execution'/role).resolve()
    logs={k:(project/v).resolve() for k,v in row['logs'].items()}
    if any(p.parent!=expected_logroot for p in logs.values()):raise ValueError('log path escapes exact candidate execution directory')
    if a.status:
        entry=json.loads(logs['entry'].read_bytes()) if logs['entry'].exists() else None
        complete=json.loads(logs['completion'].read_bytes()) if logs['completion'].exists() else None
        ids=[]
        if logs['stdout'].exists():
            for line in logs['stdout'].read_bytes().splitlines():
                try:v=json.loads(line)
                except ValueError:continue
                if v.get('type')=='thread.started':ids.append(v.get('thread_id'))
        print(json.dumps({'entry':entry,'completion':complete,'actual_thread_ids':sorted(set(ids)),
                          'semantic_status':'NOT_INFERRED_FROM_PROCESS_EXIT'},ensure_ascii=False,indent=2));return
    prompt=package/'prompts'/(batch+'-'+role+'.md'); data=prompt.read_bytes()
    effort='xhigh' if role=='author' else 'ultra'
    argv=['codex','exec','--model','gpt-6.1-sol','--config','model_reasoning_effort="'+effort+'"',
          '--config','service_tier="default"','--sandbox','workspace-write','--json','--cd',str(project),
          '--output-last-message',str(logs['entry'].parent/'last-message.txt'),'-']
    request={'entry_id':a.entry,'argv':argv,'cwd':str(project),'stdin_prompt':str(prompt),
             'prompt_identity':{'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()},
             'requested':{'model':'gpt-6.1-sol','effort':effort,'tier':'default','speed':'normal; Fast forbidden'},
             'actual':{k:'UNVERIFIED' for k in ('model','effort','tier','speed')},
             **{k:str(v) for k,v in logs.items()},'status':'NOT_STARTED'}
    if not a.launch:print(json.dumps(request,ensure_ascii=False,indent=2));return
    members=json.loads((package/'package-members.json').read_bytes())['members']
    matches=[v for v in members if v['path']=='prompts/'+prompt.name]
    if len(matches)!=1 or matches[0]['bytes']!=len(data) or matches[0]['sha256']!=request['prompt_identity']['sha256']:
        raise ValueError('prompt bytes differ from frozen package member identity')
    def git(*args):return subprocess.check_output(['git','-C',str(project),*args]).decode().strip()
    if git('rev-parse',B+':deliverables/final-specification-set')!=FT:raise ValueError('fixed formal tree mismatch')
    if git('branch','--show-current') in ('main','codex/review-seventh-2026-10-14-e646432-7a91',''):
        raise ValueError('future update must already have its own authorized branch')
    if any(p.exists() for p in logs.values()):raise FileExistsError('existing entry/logs must be preserved')
    ref=project/'reference/pokemon-essentials'
    if subprocess.check_output(['git','-C',str(ref),'rev-parse','HEAD']).decode().strip()!='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b':
        raise ValueError('actual reference material identity mismatch')
    logs['entry'].parent.mkdir(parents=True,exist_ok=True)
    request.update(start_utc=utc(),status='STARTING')
    with logs['stdout'].open('xb') as stdout,logs['stderr'].open('xb') as stderr:
        child=subprocess.Popen(argv,cwd=project,stdin=subprocess.PIPE,stdout=stdout,stderr=stderr)
        request.update(pid=child.pid,status='RUNNING');dump(logs['entry'],request)
        print(json.dumps({'entry_id':a.entry,'actual_pid':child.pid,'entry':str(logs['entry'])}),flush=True)
        child.communicate(input=data)
        code=child.returncode
    dump(logs['completion'],{'end_utc':utc(),'exit_code':code,'status':'PROCESS_EXITED',
                              'semantic_status':'PENDING_ACTUAL_RECEPTION','update_entry':a.entry})
    raise SystemExit(code)
if __name__=='__main__':main()
