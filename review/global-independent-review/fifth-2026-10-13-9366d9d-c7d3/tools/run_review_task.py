"""Foreground task runner for this review only; no scheduler, publishing, or source writes."""
import argparse, hashlib, json, os, pathlib, subprocess, sys, datetime
parser=argparse.ArgumentParser()
parser.add_argument("module")
parser.add_argument("--resume")
a=parser.parse_args()
work=pathlib.Path("/Users/dingshinn/.codex/worktrees/review-fifth-9366d9d/pokemon-framework-reference")
report=work/"review/global-independent-review/fifth-2026-10-13-9366d9d-c7d3"
module=report/"modules"/a.module
runtime=pathlib.Path("/tmp/pokemon-gr5-c7d3")/a.module
runtime.mkdir(exist_ok=True)
cli="/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex"
thread=a.resume
prior=None
stalled=0
step=0
status={"module":a.module,"runner_pid":os.getpid(),"thread_id":thread,"status":"starting","config_request":{"model":"gpt-6-astra","reasoning_effort":"ultra","service_tier":"default","fast":False,"actual_echo":"UNVERIFIED"},"turns":[]}
def save():
    q=runtime/"runner-status.json"
    q.write_text(json.dumps(status,ensure_ascii=False,indent=2)+"\n")
def fingerprint():
    h=hashlib.sha256()
    for name in ["reading-coverage.json","source-to-spec.json","spec-to-source.json","findings.json"]:
        f=module/name
        if f.exists():h.update(name.encode()+f.read_bytes())
    return h.hexdigest()
save()
while True:
    if (runtime.parent/"STOP").exists():
        status["status"]="stopped_by_parent_marker";save();break
    step+=1
    stem="runner-turn-"+str(step).zfill(3)
    log=runtime/(stem+".jsonl")
    err=runtime/(stem+".stderr.log")
    final=runtime/(stem+".final.md")
    if log.exists():
        status["status"]="output_collision_needs_parent";save();break
    config=["-m","gpt-6-astra","-c",'model_reasoning_effort="ultra"',"-c",'service_tier="default"',"--json","-o",str(final)]
    if thread:
        command=[cli,"exec","resume"]+config+[thread,"-"]
        prompt="继续同一第五轮全量独立审查任务。固定B5/R、模型请求和只写自己模块目录的限制保持。读取自己的progress与reading-coverage检查点，从未审范围继续；不要重做已完成语义范围或全仓身份审计，不因阶段结束/输出预算自定抽样终点。完成全部分配可得可审源、当前正文、测试、附表和有效补充才在progress.json置complete=true；已审出的partial/missing/unresolved是审查结果，和可读但尚未审分开。若仅剩跨域合同依赖，请明确仍需的精确路径/范围，不要重复已审范围。若真实工具/模型/权限拒绝立即记blocked并停止，不换模型、不改Fast、不查额度/认证/后端。更新逐条双向映射和候选的完整反证。母任务会做独立反证与整合，你不能自签最终必修。首任务要求见本模块task-prompt.md。检查本轮evidence/initial-owner-map.json仅辅助责任定位，完整源发现仍独立完成。额外父提示如本模块存在parent-note.md请读。任何缺宿主不阻止可得源/数据的静态审查。不要建立其他agent或会话。"
    else:
        command=[cli,"exec"]+config+["-C",str(work),"-"]
        prompt=(module/"task-prompt.md").read_text()
    request={"step":step,"started_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"command":command,"event_log":str(log),"stderr_log":str(err),"last_message":str(final)}
    status["turns"].append(request);status["status"]="running";save()
    print(json.dumps({"module":a.module,"step":step,"thread_id":thread,"log":str(log),"status":"running"}),flush=True)
    with log.open("w") as stdout,err.open("w") as stderr:
        process=subprocess.run(command,input=prompt,text=True,cwd=work,stdout=stdout,stderr=stderr)
    request["exit_code"]=process.returncode
    request["ended_utc"]=datetime.datetime.now(datetime.timezone.utc).isoformat()
    events=[]
    for line in log.read_text().splitlines():
        try:events.append(json.loads(line))
        except json.JSONDecodeError:pass
    for event in events:
        if event.get("type")=="thread.started":thread=event["thread_id"]
    status["thread_id"]=thread
    errors=[x for x in events if x.get("type") in ["error","turn.failed"]]
    if process.returncode or errors:
        status["status"]="runtime_error_needs_parent";status["errors"]=errors;save();break
    try:progress=json.loads((module/"progress.json").read_text())
    except Exception as error:
        status["status"]="progress_unreadable_needs_parent";status["error"]=str(error);save();break
    request["progress_status"]=progress.get("status")
    if progress.get("complete") is True:
        status["status"]="reviewer_reported_complete_pending_parent_validation";save();break
    if str(progress.get("status","")).lower() in ["blocked","blocked_on_dependency","needs_parent"]:
        status["status"]="dependency_or_blocker_needs_parent";save();break
    current=fingerprint()
    stalled=stalled+1 if current==prior else 0
    prior=current
    if stalled>=2:
        status["status"]="no_semantic_ledger_change_needs_parent";save();break
    if not thread:
        status["status"]="missing_thread_id_needs_parent";save();break
    save()
print(json.dumps({"module":a.module,"thread_id":thread,"status":status["status"]}),flush=True)
