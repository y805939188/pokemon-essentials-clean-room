"""Bounded declarative identity checks; no target behavior execution."""
from pathlib import Path
import json,hashlib,subprocess,os,datetime
r=Path('/workspace/r7-ir-R7-U10-wave3');repo=r/'result-checkout';out=repo/'review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U10/r1/evidence'
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def git(*a):return subprocess.check_output(['git','-C',str(repo),*a])
contract=json.loads((r/'original/dispatch/delegation/contracts/R7-U10.json').read_text())
raws={hashlib.sha256(p.read_bytes()).hexdigest():p for root in [r/'original/evidence',r/'supplement'] for p in root.rglob('*') if p.is_file()}
refs={}
def visit(x):
 if isinstance(x,dict):
  if all(k in x for k in ['input_sha256','raw_member_byte_offsets','raw_member_sha256']):refs[(x['input_sha256'],tuple(x['raw_member_byte_offsets']))]=x
  for v in x.values():visit(v)
 elif isinstance(x,list):
  for v in x:visit(v)
visit(contract)
checks=[]
for (sha,(lo,hi)),ref in sorted(refs.items()):
 p=raws.get(sha)
 if not p:checks.append({'input_sha256':sha,'status':'MISSING'});continue
 b=p.read_bytes()[lo:hi]
 checks.append({'input_sha256':sha,'pointer':ref.get('json_pointer'),'offsets':[lo,hi],**ident(b),'expected_sha256':ref['raw_member_sha256'],'match':hashlib.sha256(b).hexdigest()==ref['raw_member_sha256'] and len(b)==ref['raw_member_bytes']})
nav='review/remediation-seventh-20261015-prepare/current-navigation-errata.json';mi='e54f54a2cb32e546eabd46aaf53ed45b30a8af89'
j=json.loads((r/'actual-input/integration/applied-clauses.json').read_text());f=next(f for f in j['cumulative_files'] if f['path']==nav)
c=json.loads(f['hunks'][0]['added_text']);a=json.loads(git('show',mi+':'+nav));d=[]
def compare(c,a,p=''):
 if isinstance(c,dict) and isinstance(a,dict):
  for k in sorted(c.keys()|a.keys()):compare(c.get(k),a.get(k),p+'/'+k)
 elif c!=a:d.append({'pointer':p,'candidate':c,'actual':a})
compare(c,a)
expected={'/status','/reception/candidate_review','/reception/shared_integration'}
assert set(x['pointer'] for x in d)==expected
nav_bytes=git('show',mi+':'+nav);prior_bytes=git('show','45c80832a41c1b56dcd7e9d93497758cbb7721de:'+nav)
# Existing stage annotation: no new wave3 delta; keep raw strict failure in byte-audit.
nav_result={'path':nav,'current':ident(nav_bytes),'previous_actual':ident(prior_bytes),'unchanged_from_previous_MI':nav_bytes==prior_bytes,'exact_JSON_differences_against_candidate':d,'interpretation':'Three prior receiver-stage strings; no added behavioral field. Strict textual journal mismatch retained, not silently waived as a full byte match. Outside U10 target set.'}
cil=(r/'bootstrap/current-cil.txt').read_text();methods=[line for line in cil.splitlines() if line.startswith('METHOD ')];eh=[line for line in cil.splitlines() if line.startswith('EH_CLAUSE')];branches=[line for line in cil.splitlines() if line.startswith('BRANCH_TARGETS_VALID')]
ci={'input':ident((r/'original/inputs/reference/animmaker.exe').read_bytes()),'decoder_source':{'commit':'d7337be83dae5aa7b848cd6a603c2aa7048ffa0c','path':'candidates/R7-U10/evidence/reviewer/r2/inspect_cil_static.py','read_before_use':True,'change':'Only input path rebased; no target evaluation'},'decoder_actual':ident((r/'bootstrap/inspect_cil_read_and_rebased.py').read_bytes()),'output_identity':ident(cil.encode()),'methods':methods,'EH_count':len(eh),'validated_branch_counts':[int(x.split()[-1]) for x in branches],'execution_class':'STATIC_DECODER_TOOL_ONLY','target_programs_executed':0,'library_host_pixels_files_certified':False}
# The actual decoded clauses are not republished as source code; original output stays local.
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pid':os.getpid(),'CODEX_THREAD_ID':os.environ.get('CODEX_THREAD_ID'),'CODEX_SESSION_ID':os.environ.get('CODEX_SESSION_ID'),'identity_provenance':'Exact named environment fields; no process/role/request inference','original_contract_member_spans':checks,'strict_member_span_failures':[x for x in checks if not x.get('match')],'prior_navigation_annotation':nav_result,'current_static_decoder':ci,'no_auth_or_quota_query':True,'auxiliary_AI_tasks_created':0,'model_configuration':'UNVERIFIED','semantic_or_runtime_PASS':False}
(out/'supplemental-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'member_spans':len(checks),'failures':len(result['strict_member_span_failures']),'thread':result['CODEX_THREAD_ID'],'methods':len(methods),'EH':len(eh),'prior_nav_unchanged':nav_result['unchanged_from_previous_MI']}))
