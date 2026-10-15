"""Capture current visible identity and fixed extra HTTP input; never execute it."""
import os,json,hashlib,datetime,urllib.request,shutil
from pathlib import Path
ROOT=Path('/workspace/r7-ir-R7-U08');OUT=Path(__file__).parent
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def put(name,j):(OUT/name).write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
dispatch=(ROOT/'bootstrap/R7-U08-R7IR.md').read_text()
import re
excluded=sorted(set(re.findall(r'01a[0-9a-f-]{33}',dispatch)))
thread=os.environ.get('CODEX_THREAD_ID');session=os.environ.get('CODEX_SESSION_ID')
assert thread=='01a1401c-33a5-716e-8f2e-4f96e971b01c' and thread==session and thread not in excluded
put('context.json',{'captured_utc':now(),'capture_tool_pid':os.getpid(),'visible_thread_id':thread,'visible_session_id':session,'source':'actual environment CODEX_THREAD_ID/CODEX_SESSION_ID; current capture is not a creation API receipt','author_context':'01a13f7f-ac68-740b-922a-7bf690ebb024','candidate_reviewer_context':'01a13ff0-a716-77b3-bbda-7ad40ff90032','dispatch_excluded_visible_ids':excluded,'visible_distinctness':'CONFIRMED_AGAINST_ALL_DISPATCH_IDS','internal_opaque_task_or_context_id':'NOT_EXPOSED; qualification retained','role_name_not_used_as_identity':True,'subagents_or_auxiliary_model_calls_created':0,'requested_configuration':{'model':'gpt-6.1-sol','effort':'ultra','service_tier':'default','speed':'normal','Fast':'FORBIDDEN'},'effective_configuration':dict.fromkeys(['model','effort','service_tier','speed'],'UNVERIFIED'),'configuration_authority':'No effective backend response exposed; PID, request and exit status are not configuration evidence.'})
url='https://raw.githubusercontent.com/Maruno17/pokemon-essentials/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/001_Settings.rb'
start=now()
with urllib.request.urlopen(url,timeout=60) as response:
 b=response.read();status=response.status;final_url=response.url
assert b==(ROOT/'bootstrap/001_Settings.rb').read_bytes()
put('extra-fixed-source-input.json',{'utc_start':start,'utc_end':now(),'tool_pid':os.getpid(),'url':url,'final_url':final_url,'http_status':status,**ident(b),'read_scope_lines':[141,151],'purpose':'Independently verify default IV/EV enablement for legal odd-total-HP fixture','execution':'NOT_EXECUTED','reference_git_tree_verified_in':'input-byte-validation.json','earlier_metadata_api_failure':{'transport':'urllib GitHub REST /git/commits at fixed R','outcome':'Tunnel connection failed: 403 Forbidden','platform_output_chunk':'f7bd3b','local_PID_stdout_stderr_receipt':'NOT_CAPTURED; no retroactive receipt invented','resolution':'Readonly exact-commit Git fetch succeeded; 003/004 logs and input-byte-validation bind R tree. This request is a fresh logged re-read of Settings, not a backfilled receipt.'}})
copies=[('bootstrap/R7-U08-R7IR.md','dispatch-read.md'),('original-plans/R7-U08.json','original-restore-plan.json'),('actual-plans/R7-U08.json','actual-restore-plan.json'),('bootstrap/restore_container_context.py','prescribed-restore-tool.py'),('bootstrap/independent-containers.md','prescribed-recovery-guide.md'),('original/evidence/tasks/R7-C17/limits-and-alias-reception.json','retained-L01-L14.json')]
for name in ['original','actual-input']:
 for p in sorted((ROOT/name).glob('recovery-receipt-*.json')):copies.append((str(p.relative_to(ROOT)),name+'-'+p.name))
rows=[]
for src,dest in copies:
 b=(ROOT/src).read_bytes();(OUT/dest).write_bytes(b);rows.append({'source':str(ROOT/src),'output':dest,**ident(b)})
put('transport-evidence-copy-receipt.json',{'utc':now(),'tool_pid':os.getpid(),'copies':rows,'source_programs_executed':False,'qualification':'Only the prescribed restoration tool was executed after full reading. No candidate/reviewer/reference program was executed. Restored snapshots are bounded, not full working trees.'})
print(json.dumps({'thread':thread,'excluded_visible_ids':len(excluded),'fresh_HTTP_status':status,'copied_evidence_files':len(rows),'effective_configuration':'UNVERIFIED','execution':'IDENTITY_AND_TRANSPORT_ONLY'}))
