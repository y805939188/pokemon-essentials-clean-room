#!/usr/bin/env python3
"""Validate only this newly written R-B08 actual report package (Git/JSON/hash/text)."""
import pathlib,json,hashlib,subprocess,re,gzip
ROOT=pathlib.Path('/workspace/r-b08-actual-review');REFROOT=pathlib.Path('/workspace/r-b08-reference')
OUT=ROOT/'review/remediation/20261003-prepare/batches/B08/integration-review-1';ACT='49c21538e72b7a5873972cd00fcae1ee390cce64';REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
checks=[]
def check(v,s):checks.append({'check':s,'pass':bool(v)})
def git(*args,root=ROOT):return subprocess.check_output(['git',*args],cwd=root)
def sha(b):return hashlib.sha256(b).hexdigest()
def load(p):return json.loads(p.read_text())
for p in OUT.glob('*.json'):
 if p.name in ['report-validation.json','artifact-manifest.json']:continue
 load(p);check(True,'valid JSON:'+p.name)
v=load(OUT/'verdict.json');c=load(OUT/'contribution-review.json');f=load(OUT/'fixed-control-bindings.json');s=load(OUT/'source-reading-log.json');d=load(OUT/'document-check-results.json');co=load(OUT/'integrator-comparison-checks.json');di=load(OUT/'input-and-diff-identities.json')
check(v['reviewed_actual']==ACT and v['reviewed_actual_tree']==git('rev-parse',ACT+'^{tree}').decode().strip(),'exact actual/tree verdict')
check(v['verdict']=='PASS_SCOPED' and not v['new_required_findings'] and not v['required_repairs'],'PASS_SCOPED no required repairs')
check(len(c)==17 and [x['id'] for x in c]==v['complete_contribution_IDs']==[x['id'] for x in f['bindings']],'complete17 identical control/independent/verdict memberships')
check(sum(x['B08_primary'] for x in c)==9 and [x['id'] for x in c if x['B08_primary']]==v['primary_IDs'],'exact9 primary')
for x in c:
 check(x['reviewed_actual']==ACT and x['local_verdict']=='PASS_SCOPED' and x['canonical_state']=='OPEN' and x['canonical_closure'] is False,'each exact-actual local PASS without closure:'+x['id'])
 check(all(x[k] for k in ['independent_actual_reasoning','minimal_positive_or_defect_exposing_design','negative_and_reverse_controls','preserved_inputs_and_boundary']),'each actual independent reasoning/control fields:'+x['id'])
 for i in x['fresh_reference_read_event_indices_zero_based']:check(0<=i<len(s['fresh_read_events']),'valid fresh read event index:'+x['id']+':'+str(i))
 for row in x['actual_static_row_identities']:
  b=git('show',ACT+':'+row['path']).splitlines(keepends=True)[row['line']-1];check(sha(b)==row['sha256'] and len(b)==row['bytes'],'actual static row binding:'+x['id']+':'+row['id'])
for r in f['bindings']:
 canon=lambda o:sha(json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
 check(canon(r['complete_original_object'])==r['original_complete_object_sha256'] and canon(r['complete_approved_acceptance'])==r['acceptance_object_sha256'],'fixed full control hashes:'+r['id'])
check(d['checks']==7092 and not d['failed'] and all(r['pass'] for r in d['check_records']),'all7092 independent document records')
check(co['checks']==183 and not co['failed'] and all(r['pass'] for r in co['check_records']),'all183 independent postjudgment comparison records')
check(v['independent_document_assertions']['total']==7092+183,'7275 assertion total is documentary only')
check(len(di['full_predecessor_to_actual_statuses'])==131 and len(di['full_candidate_to_actual_statuses'])==74,'full131/74 report path inventories')
for p in di['unfiltered_actual_diffs']:
 z=(OUT/p['path']).read_bytes();u=gzip.decompress(z);check(sha(z)==p['compressed_sha256'] and len(z)==p['compressed_bytes'] and sha(u)==p['uncompressed_sha256'] and len(u)==p['uncompressed_bytes'],'complete stored gzip full-diff identity:'+p['path'])
check(git('rev-parse','HEAD',root=REFROOT).decode().strip()==REF,'independent reference still exact fixed HEAD')
check(not git('status','--porcelain',root=REFROOT),'independent reference worktree unchanged')
unique={}
for i,r in enumerate(s['fresh_read_events']):
 b=git('show',REF+':'+r['path'],root=REFROOT);check(len(b)==r['bytes'] and sha(b)==r['sha256'] and git('rev-parse',REF+':'+r['path'],root=REFROOT).decode().strip()==r['git_blob'],'fresh text evidence identity:'+str(i))
 for a,e in r['ranges']:
  check(1<=a<=e<=len(b.splitlines()),'fresh bounded range exists:'+str(i)+':'+str(a));unique.setdefault(r['path'],set()).update(range(a,e+1))
check(len(s['fresh_read_events'])==46 and len(unique)==37 and sum(len(z) for z in unique.values())==2923 and s['unique_requested_line_positions']==2925,'fresh46/37/2923 actual and2925 requested denominators')
check(s['inherited_source_limits_verbatim']['retained_source_limits']==['U01–U10','G01–G12','AX01–AX20'],'all unknown families retained')
check(s['inherited_source_limits_verbatim']==json.loads(git('show',ACT+':review/remediation/20261003-prepare/batches/B08/integration-stage-1/scope-and-observation-registration.json'))['source_limits'],'complete inherited named limits retained verbatim')
first=load(OUT/'integrator-comparison.json');check(sha((OUT/first['independent_first_judgment_file']).read_bytes())==first['independent_first_judgment_sha256'],'preserved independent-first-judgment identity')
for r in v['separate_actual_reports_receipts_after_own_judgment']:
 check(git('show','-s','--format=%P',r['commit']).decode().strip()==ACT,'same-actual separate report parent:'+r['role']);h=json.loads(git('show',r['commit']+':'+r['receipt_identity']['path']));check(h['reviewed_actual']==ACT and (h.get('verdict') or h.get('status'))=='PASS_SCOPED','same-actual separate report handoff:'+r['role'])
for p in OUT.glob('*.md'):
 b=p.read_bytes();check(b.endswith(b'\n') and all(x==x.rstrip(b' \t') for x in b.splitlines()),'own Markdown clean:'+p.name)
 for target in re.findall(r'\]\(([^\s)]+)\)',b.decode()):
  if ':' in target or target.startswith('#'):continue
  check((p.parent/target.split('#')[0]).exists(),'own relative link exists:'+p.name+':'+target)
conf=load(OUT/'configuration-and-scope-receipt.json');check(conf['effective_server_configuration']=='UNVERIFIED' and conf['configuration_probes']==0 and conf['authentication_actions']==0 and conf['subagents_spawned']==0,'Plan A/no probes/no subagents')
check(all(conf[k]==0 for k in ['reference_execution','compiler_execution','converter_execution','generator_execution','deserializer_execution','behavior_simulator_execution','behavior_vectors_executed','historical_author_or_reviewer_verifier_execution','runtime_observations','proven_Demo_chains','formal_corrections','original_or_reference_edits','public_or_history_edits','canonical_closures','downstream_dispatch']),'all zero execution/observation/mutation limits')
result={'reviewed_actual':ACT,'scope':'Validation of the newly written report artifacts only; no game/source behavior or inherited program executed','checks':len(checks),'failed':[r for r in checks if not r['pass']],'check_records':checks}
(OUT/'report-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='check_records'},indent=2))
raise SystemExit(bool(result['failed']))
