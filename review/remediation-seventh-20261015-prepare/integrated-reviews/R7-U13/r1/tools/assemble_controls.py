"""Archive real receipts, fixed controls, and actual environment identifiers."""
from pathlib import Path
import os,json,datetime,subprocess,shutil,re
from run_logged import identity
W=Path('/workspace/r7-ir-R7-U13');T=Path(__file__).resolve().parent
dispatch='c64774c60d91e522cb515ef71e3e9d4ea6b4712c';dp='review/remediation-seventh-20261015-prepare/integration/wave2/v1/dispatch/R7-U13-R7IR.md'
data=subprocess.check_output(['git','-C',str(W/'checkout'),'show',dispatch+':'+dp]);controls=T/'input-controls';controls.mkdir(exist_ok=True)
(controls/'dispatch.md').write_bytes(data)
copies=[(W/'original/dispatch/delegation/contracts/R7-U13.json',controls/'original-seven-group-contract.json'),(W/'original-plans/R7-U13.json',controls/'original-restore-plan.json'),(W/'actual-plans/R7-U13.json',controls/'actual-restore-plan.json'),(W/'actual-input/integration/integrated-input.json',controls/'integrated-input.json'),(W/'actual-input/freeze/candidate-input.json',controls/'candidate-input.json'),(W/'bootstrap/restore_container_context.py',controls/'fixed-restore-tool.py'),(W/'bootstrap/independent-containers.md',controls/'independent-containers.md')]
for folder in ['original','actual-input']:
    for p in (W/folder).glob('recovery-receipt-*.json'):copies.append((p,T/'recovery'/folder/p.name))
inventory=[]
for src,dst in copies:
    dst.parent.mkdir(parents=True,exist_ok=True)
    if dst.exists():assert dst.read_bytes()==src.read_bytes()
    else:shutil.copyfile(src,dst)
    inventory.append({'source':str(src),'archived':str(dst.relative_to(T.parent)),'identity':identity(dst.read_bytes())})
source_io=W/'local-reference-source-io';source_io.mkdir(exist_ok=True);relocations=[]
for name in ['read-reference-0.stdout','read-reference-1.stdout','read-reference-2.stdout','read-reference-3.stdout','read-reference-gamesystem-gap.stdout']:
    src=T/name;dst=source_io/name
    if src.exists():
        if dst.exists():assert src.read_bytes()==dst.read_bytes();src.unlink()
        else:shutil.move(str(src),str(dst))
    relocations.append({'original_log_label':name,'actual_full_stdout_local_path':str(dst),'identity':identity(dst.read_bytes()),'publication':'Reference program text retained only in container/platform I/O; public commands ledger retains exact stream identity. No transcript replacement or retroactive redaction claim.'})
(T/'evidence-relocations.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'relocations':relocations,'reason':'Keep reference program source out of public clean-room review evidence; all actual stream bytes remain locally available.'},ensure_ascii=False,indent=2)+'\n')
thread=os.environ.get('CODEX_THREAD_ID');session=os.environ.get('CODEX_SESSION_ID');assert thread and thread==session
excluded=sorted(set(re.findall(r'01[a-f0-9]{6}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}',data.decode())))
assert len(excluded)==19 and thread not in excluded
ctx={'schema':'r7.u13.fresh-actual-ir-context.v1','observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'actual_CODEX_THREAD_ID':thread,'actual_CODEX_SESSION_ID':session,'separate_opaque_platform_task_id':'NOT_EXPOSED_UNVERIFIED','separate_opaque_context_id':'NOT_EXPOSED_UNVERIFIED','selected_environment_id':'NOT_EXPOSED_UNVERIFIED','model_process_pid':'NOT_EXPOSED_UNVERIFIED','evidence_process_pid':os.getpid(),'evidence_process_parent_pid':os.getppid(),'pid_qualification':'Actual ordinary Python evidence process only, never a model/platform identity','parent_source_thread_id':'01a13f49-a154-7054-9b04-ce31f924d01c','excluded_actual_visible_identifiers':excluded,'actual_thread_differs_from_all_excluded':True,'subtasks_or_AI_helpers_created':0,'requested_configuration':{'model':'gpt-6.1-sol','reasoning_effort':'ultra','service_tier':'default','speed':'ordinary','Fast':'forbidden'},'effective_configuration':dict.fromkeys(['model','reasoning_effort','service_tier','speed'],'UNVERIFIED'),'configuration_qualification':'No valid model configuration response exposed. No quota/auth inspection or separate model CLI. Requested settings, environment IDs, PIDs and tool exit0 are not configuration attestation.','workspace_rules':'Full actual MI AGENTS.md read in controls-corrected stdout; no tracked .agents at MI/B and empty /workspace/.agents; no relevant .agents/skills available.','independence':'Current real thread is distinct from all 19 dispatch exclusions. No author/candidate-review/integration work performed in this context; opaque prior author IDs remain qualified.'}
(T/'execution-context.json').write_text(json.dumps(ctx,ensure_ascii=False,indent=2)+'\n');(T/'control-and-receipt-inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'real_thread':thread,'excluded_visible_identifiers':len(excluded),'fixed_controls_and_receipts':len(inventory),'reference_source_streams_local_only':len(relocations)}))
