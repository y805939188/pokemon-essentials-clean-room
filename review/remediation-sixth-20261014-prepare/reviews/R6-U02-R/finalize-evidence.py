#!/usr/bin/env python3
"""Freeze reviewer evidence; only this directory is writable."""
import datetime
import difflib
import hashlib
import json
from pathlib import Path
import subprocess
import sys

OWN=Path(__file__).resolve().parent
ROOT=OWN.parents[3]
PRE="review/remediation-sixth-20261014-prepare/"
PUB="bc570b4e84bc9ef1510228dd69e25a9958e23545"
CORE="5210b009db5191f307301115845e31475cd798ef"
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
commands=[]
def run(argv):
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    p=subprocess.run(argv,cwd=ROOT,capture_output=True)
    commands.append({"argv":argv,"cwd":str(ROOT),"UTC_start":start,"UTC_end":datetime.datetime.now(datetime.timezone.utc).isoformat(),"exit":p.returncode,"stdout_bytes":len(p.stdout),"stdout_sha256":hashlib.sha256(p.stdout).hexdigest(),"stderr":p.stderr.decode()})
    if p.returncode:raise RuntimeError((argv,p.stderr.decode()))
    return p.stdout
def show(commit,path):return run(["git","show",commit+":"+path])
def identity(b):return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest(),"git_blob":hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()}
def write(name,x):(OWN/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n")
def canonical(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
v=json.loads((OWN/"verification.json").read_text())
assert v['candidate_commit']==PUB
reads=[json.loads(x) for x in (OWN/"reading-receipts.jsonl").read_text().splitlines()]
groups={}
for x in reads:
    key=(x['input'],x.get('role','source'))
    y=groups.setdefault(key,{"input":key[0],"role":key[1],"total_lines":x['total_lines'],"sha256":x['sha256'],"ranges":[]})
    assert y['sha256']==x['sha256']
    y['ranges'].append(x['range'])
for x in groups.values():
    covered=set()
    for a,b in x['ranges']:covered.update(range(a,b+1))
    x['covered_lines']=len(covered);x['full_line_coverage']=len(covered)==x['total_lines']
coverage={"created_UTC":NOW,"line_receipts":list(groups.values()),"full_text_method":"Paired complete payloads: shared exact lines expanded with both coordinates, changed baseline/candidate sides separately. WP51 candidate entire 1-160 and complete old/new patch jointly cover baseline 1-156.","WP51_baseline_full_text":{"lines":[1,156],"method":"exact shared candidate bytes plus all baseline-only patch lines; initial read UTC not separately captured"},"initial_semantic_reads_without_separate_UTC":["AGENTS.md","complete prompts/R6-U02-R.md with full contract JSON and lossless common-field expansion of all115 recovery entries","complete contracts/R6-U02.json all fields","seven specified counterevidence packets","author-report.md; complete candidate-changes.patch; manifests; execution-snapshot and integration-handoff","complete relevant R2/R3/R5 qualification records expanded from fixed R6-H JSON objects; final packet two-ID records","complete limit-records and execution-phases JSON; U02 graph edges","CA original probe-inputs/result/validation JSON"],"structural_only":"Remaining unrelated evidence cache leaves and generated administrative payloads: identities/structure, not new full-game semantic credit","early_truncation":"Initial oversized output is not full-text credit; complete contract lossless views and patch/R6-H/B022 retries replace it for read coverage only, not original execution metadata"}
write("reading-coverage.json",coverage)
history={"created_UTC":NOW,"level":"HISTORICAL_QUALIFICATION_AND_TOOL_VALIDATION","new_game_verdict_transfer":False,"fixed_inputs":[],"selected":[]}
closure_path="review/remediation-fifth-20261013-prepare/registration/successors/20261014-final-closure-candidate/closure-candidate.json"
activation_path="review/remediation-fifth-20261013-prepare/registration/successors/20261014-final-activation/activation-receipt.json"
closure_b=show("13fddb0a217b36974c75657aa68da0caf104ee48",closure_path);closure=json.loads(closure_b)
activation_b=show("12df95a8e81061a606d50d3f0a0528793b2e6b2c",activation_path);activation=json.loads(activation_b)
history['fixed_inputs']=[{"commit":"13fddb0a217b36974c75657aa68da0caf104ee48","path":closure_path,**identity(closure_b)},{"commit":"12df95a8e81061a606d50d3f0a0528793b2e6b2c","path":activation_path,**identity(activation_b)}]
for s in activation['state_resolution']['selection']:
    if s['id'] not in ['GR5-JXN-002','GR5-M07-001','GR5-M07-002','GR5-M08-003','GR5-M09-001']:continue
    r=closure['records'][s['record_index']]
    assert r['id']==s['id'] and canonical(r)==s['scope_record_sha256']
    assert canonical(r['proposed_only_after_valid_activation'])==s['selected_state_record_sha256']
    history['selected'].append({**s,"state":r['proposed_only_after_valid_activation'],"canonical_identity_result":"MATCH","span_rows":[x for x in v['historical_spans'] if x['id']==s['id']]})
assert len(history['selected'])==5
history['preserved_counts']=activation['effective_counts'];history['history_preserved']=activation['history_preserved'];history['scope']=activation['closure_scope']
write("historical-bindings.json",history)
ids=json.loads((ROOT/(PRE+"contracts/R6-U02.json")).read_text())['scope_contracts']
write("dispositions.json",{"reviewer":"R6-U02-R","verdict":"PASS","evidence_scope":"FINITE_STATIC_CANDIDATE_CONTRACT","candidate_commit":PUB,"candidate_workspace_tree":"e7667bb80c89444708348e619c3feea0d315954a","candidate_mirrors":v['candidate_mirrors'],"required_ids":[{"id":x['id'],"classification":"required","severity":"P2","root_cause_key":x['id'],"aggregation_aliases":[],"verdict":"PASS","seven_groups":"REPORT.md corresponding seven sections","minimum_necessary_revisions":[]} for x in ids],"effective_configuration":"UNVERIFIED","new_reference_execution":0,"integrated_PASS":False,"formal_acceptance":False,"CLOSED":False,"public_ledger_write":False,"new_task_requirements":0})
write("execution-context.json",{"created_UTC":NOW,"actual_cwd":str(ROOT),"task_path":"/root","logical_id":"R6-U02-R","delegation_source_thread_id":"01a10d94-84b9-759e-aa1d-edb0d9b6d0e2","task_UUID":"UNVERIFIED","requested":{"model":"gpt-6.1-sol","effort":"ultra","tier":"default","speed":"default","fast":False},"effective":{"model":"UNVERIFIED","effort":"UNVERIFIED","tier":"UNVERIFIED","speed":"UNVERIFIED"},"CLI_configuration_probe":False,"subagents":0,"runtime_for_text_tools":sys.version,"early_command_UTC":"NOT_SEPARATELY_CAPTURED; platform tool echoes retained; no retrofill","independent_reference_or_surrogate_observation":0,"independent_model":0,"complete_host_Demo":0,"real_save_production":0})
write("limitations-and-attempts.json",{"created_UTC":NOW,"first_commands_UTC":"NOT_SEPARATELY_CAPTURED","preserved_from_tool_transcript":[{"action":"initial prepare directory search","result":"not yet checked out at initial8ea HEAD; fetch and independent branch corrected"},{"action":"oversized original contract/prompt-index/author aggregate/R6-H aggregate/B022 display","result":"truncation retained; full contract lossless expansion, complete patch, full55-line R6-H and fullB022 follow-up read; initial output not claimed complete"},{"action":"Ruby capability read","stdout":"","stderr":"/bin/bash: line 1: ruby: command not found","result":"Ruby absent; no original definition loaded or executed; no installation attempted"},{"action":"wc guessed WP42 filename","result":"No such file; rg located wp42-growth-end-of-round-and-battle-outcomes.md, then full1-285 read"},{"action":"git fetch four commits including shortened199dee3","exit":128,"stderr":"fatal: couldn't find remote ref 199dee3","result":"Known full R6core/R5core/activation commits fetched normally; fixed complete R3 qualification projection used, no claimed successful fetch of short ref"},{"action":"guessed001_Battler.rb source path","result":"path absent at fixedR; ls-tree resolved001_Battle_Battler.rb; actual required methods independently read"},{"action":"independent verification attempt01","exit":1,"result":"collapsed untracked-directory allowlist assertion; retained attempt-01.json; --untracked-files=all correction then new captured attempt02exit0"}],"remaining_limits":["actual model/effort/tier/speed/platformUUID lack valid echo","Ruby absent, new original execution0; no full host/Demo/resources/save observation","legacy execution UTC or underlying exit gaps retained, not filled by present text validation","candidate-only verdict, receiving/shared integration and closure gates outstanding"],"minimum_semantic_revision_blockers":[]})
write("finalization-commands.json",commands)
print(json.dumps({"history_selected":len(history['selected']),"history_spans":len(v['historical_spans']),"recorded_input_groups":len(groups),"verdict":"PASS","new_behavior_execution":0},ensure_ascii=False))
