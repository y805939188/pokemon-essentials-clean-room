"""Single finite continuation of an existing review; unique public logs, no scheduler."""
import sys,os,json,subprocess,datetime,pathlib
module,thread,phase,promptname=sys.argv[1:]
work=pathlib.Path("/Users/dingshinn/.codex/worktrees/review-fifth-9366d9d/pokemon-framework-reference")
report=work/"review/global-independent-review/fifth-2026-10-13-9366d9d-c7d3"
runtime=pathlib.Path("/tmp/pokemon-gr5-c7d3")/module
stem=runtime/phase
if stem.with_suffix(".jsonl").exists(): raise RuntimeError("log collision; choose a unique phase")
cli="/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex"
command=[cli,"exec","resume","-m","gpt-6-astra","-c",'model_reasoning_effort="ultra"',"-c",'service_tier="default"',"--json","-o",str(stem.with_suffix(".final.md")),thread,"-"]
status={"module":module,"task_id":thread,"runner_pid":os.getpid(),"phase":phase,"command":command,"status":"running","started_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"log":str(stem.with_suffix(".jsonl")),"model_echo":"UNVERIFIED"}
def save(): stem.with_suffix(".status.json").write_text(json.dumps(status,ensure_ascii=False,indent=2)+"\n")
save();print(json.dumps(status,ensure_ascii=False),flush=True)
with stem.with_suffix(".jsonl").open("w")as out,stem.with_suffix(".stderr.log").open("w")as err:
 p=subprocess.run(command,input=(report/"modules"/module/promptname).read_text(),text=True,cwd=work,stdout=out,stderr=err)
status.update(status="turn_ended_pending_parent_validation",exit_code=p.returncode,ended_at=datetime.datetime.now(datetime.timezone.utc).isoformat());save();print(json.dumps(status,ensure_ascii=False),flush=True)
