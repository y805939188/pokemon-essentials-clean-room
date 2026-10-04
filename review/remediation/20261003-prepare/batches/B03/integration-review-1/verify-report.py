#!/usr/bin/env python3
"""Final review-document consistency audit, never executes reference behavior."""
import hashlib, json, re, subprocess
from pathlib import Path

P=Path('/workspace/pokemon-essentials-clean-room')
R=Path('/workspace/reference-b03')
D=Path(__file__).resolve().parent
I='e24f2ac6f43642ea0e68bd9aa21fb2c313d6ebdf'
R2='a69d6e057723cc8f8aec8cac0f868da4e456d0eb'
G='93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN='41fffb540c6483f5296ea0d33b789b75180d27ed'
S='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
BP='review/remediation/20261003-prepare/batches/B03/'
checks=[]
def need(condition,label):
    checks.append({'check':label,'pass':bool(condition)})
    if not condition: raise AssertionError(label)
def git(*args,repo=P):return subprocess.check_output(['git','-C',str(repo),*args])
def raw(rev,path,repo=P):return git('show',rev+':'+path,repo=repo)
def fixed(rev,path):return json.loads(raw(rev,path))
def stable(obj):return hashlib.sha256(json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def local(name):return json.loads((D/name).read_text())

need(git('branch','--show-current').decode().strip()=='remediation/20261003-prepare/review-B03-integration-1','isolated intended review branch')
need(git('merge-base',I,'HEAD').decode().strip()==I,'review is based on exact actual integration')
for p in D.glob('*.json'):
    if p.name=='review-document-validation.json':continue
    json.loads(p.read_text());need(True,'valid JSON '+p.name)
report=(D/'report.md').read_text()
for p in D.glob('*.md'):
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)',p.read_text()):
        if '://' not in link:need((p.parent/link.split('#')[0]).is_file(),'relative review link '+p.name+' '+link)
r=local('finding-dispositions.json');old=fixed(R2,BP+'review-round-2/finding-dispositions.json')
need(r['overall_verdict']=='PASS_SCOPED' and r['reviewed_integration_commit']==I,'actual verdict identity')
need(len(r['dispositions'])==27 and sum(x['primary_in_B03'] for x in r['dispositions'])==19,'27/19 review disposition inventory')
need(len(r['prior_observation_dispositions'])==3 and not r['new_findings'],'three prior P2 repairs and no new hidden findings')
need(not r['canonical_edited'] and not r['parent_serial_acceptance_performed'] and not r['B06_full_dependency_integration_accepted'] and not r['B04_B06_parallelism_verified'],'bounded reviewer verdict no closure/unlock')
for row,prior in zip(r['dispositions'],old['dispositions']):
    fid=row['id']
    need(row['candidate_disposition_immutable']==prior and row['priority']=='P2','immutable independent candidate disposition '+fid)
    need(row['verdict']=='PASS_SCOPED' and row['canonical_state']=='OPEN' and not row['canonical_edited'],'actual scoped pass no closure '+fid)
    need(row['actual_static_case_evidence']['executed'] is False and row['actual_static_case_evidence']['commit']==I,'unexecuted current static evidence '+fid)
    for ev in row['actual_project_evidence']:
        need(ev['commit']==I and raw(I,ev['path'])==raw(R2,ev['path']),'current actual formal identity '+fid+' '+ev['path'])
    need('| '+fid+' / P2 / ' in report,'report full-ID/severity row '+fid)
for row,prior in zip(r['prior_observation_dispositions'],old['prior_observation_dispositions']):
    need(row['original_and_candidate_repair_disposition_immutable']==prior,'original P2 and independent repair object '+row['id'])
    need(row['actual_integration_verdict']=='PASS_SCOPED' and row['priority']=='P2' and not row['canonical_closed'],'actual P2 repair no closure '+row['id'])

original={x['id']:x for x in fixed(G,'review/global-independent-review/2026-10-03-fd82a639/findings.json')}
acceptance=fixed(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json')
semantic=local('interface-semantic-review.json')
for row in semantic['qualified_original_and_acceptance_objects_verified']:
    fid=row['interface']['id'];o=original[fid];a=acceptance[fid]
    need(row['original_binding']==stable(o) and row['acceptance_binding']==stable(a),'interface complete original/acceptance object '+fid)
    need(row['effective_case_constraints']==o.get('effective_case_constraints') and row['minimum_revision']==o['minimum_revision'] and row['determinate_recheck']==o['determinate_recheck'],'interface effective constraints and original gates '+fid)
need(not semantic['dispatch_performed'] and not semantic['unlock_performed'] and not semantic['global_gate_passed'],'interface no dispatch/unlock/global pass')
for row in local('source-reading-log.json')['fresh_actual_integration_literal_reads']:
    data=raw(S,row['path'],R)
    need(row['sha256']==hashlib.sha256(data).hexdigest() and row['bytes']==len(data) and row['git_blob']==git('rev-parse',S+':'+row['path'],repo=R).decode().strip(),'fresh source full byte binding '+row['path'])
need(git('rev-parse','HEAD',repo=R).decode().strip()==S and not git('status','--porcelain',repo=R).strip(),'reference fixed SHA and clean after review')
stats=local('primary-completion-review.json')
need(stats['independent_specific_obligation_counts']=={'satisfied_scoped':25,'missing_specific_consumer':1,'insufficient_evidence':0},'specific obligation 25/1/0')
need(stats['strict_all_contributor_acceptance_counts']=={'all_contributor_batches_accepted':23,'still_has_unaccepted_contributor':3},'strict all-contributor 23/3 distinction')
need(set(stats['strict_pending_ids'])=={'WP80-B02-R02','GIR-FD82-A017','GIR-FD82-A024'},'three strict pending identities')
receipt=local('execution-request-receipt.json')
need(receipt['effective_model']==receipt['effective_reasoning_effort']==receipt['effective_speed']=='UNVERIFIED','effective configuration remains unverified')
need(not receipt['capacity_failure']['failed_run_is_pass_evidence'] and receipt['subagents_spawned']==0,'failed capacity run not pass no derivation')
need('1377机械检查全通过' in report and local('independent-validation.json')['check_count']==1377,'report count binds own independent metadata audit')
need('1340空白警告' in report and local('independent-validation.json')['nested_patch_diffcheck']['raw_returncode']==2,'raw patch whitespace limitation visible')
out={'result':'PASS_REVIEW_DOCUMENT_CONSISTENCY','reviewed_integration_commit':I,'check_count':len(checks),'checks':checks,
     'reference_execution':0,'behavior_vector_execution':0,'canonical_closed':0,'future_self_commit_embedded':False}
(D/'review-document-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='checks'},ensure_ascii=False,indent=2))
