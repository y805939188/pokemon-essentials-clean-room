"""Fresh report metadata verification only. Never executes reference/author programs."""
import datetime,hashlib,json,re,subprocess,sys
from pathlib import Path
R=Path('/workspace/b14-affected-b04-review')
D=R/'review/remediation/20261003-prepare/batches/B14/affected-B04-review-1'
SREP=Path('/tmp/b14-b04-reference')
C='47f7514765f8569ae9172bb06a2cd615e2b83b8a'
B='1e6b11a47370f1c7c4659a32443fc1afda597bac'
S='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def git(*a,r=R):return subprocess.check_output(['git',*a],cwd=r)
def read(p):return json.loads((D/p).read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
checks=[]
def check(name,value,detail=None):checks.append(dict(name=name,pass_=bool(value),detail=detail))
for f in sorted(D.glob('*.json')):
 try:json.loads(f.read_text());check('JSON '+f.name,True)
 except Exception as e:check('JSON '+f.name,False,str(e))
f=read('findings.json');h=read('handoff.json');a=read('identity-and-scope-audit.json');q=read('qualified-controls.json');cats=read('catalog-comparison.json');protect=read('protected-sections.json');compare=read('author-comparison.json');ref=read('reference-preparation.json')
check('candidate HEAD exact and report branch exact',git('rev-parse','HEAD').decode().strip()==C and git('branch','--show-current').decode().strip()==h['report_branch'])
check('verdict/request gate coherent',f['verdict']==h['verdict']=='REQUEST_CHANGES' and len(f['blocking_findings'])==1 and h['candidate_gate'].startswith('BLOCKED'))
peer=read('B03-cross-reference-assessment.json')
peer_bytes=git('show',peer['peer_report']['commit']+':'+peer['peer_report']['path'])
check('fixed B03 peer report references same original candidate',json.loads(peer_bytes)['reviewed_candidate']==C and sha(peer_bytes)==peer['peer_report']['sha256'] and len(peer_bytes)==peer['peer_report']['bytes'])
check('existing B03 ID cross-referenced without duplicate local ID',peer['id']=='B14-AFFECTED-B03-001' and f['cross_referenced_findings'][0]['id']==peer['id'] and not peer['source_relation']['new_B04_ID_created'] and f['overall_blockers_count']==2 and h['cross_referenced_blocking_ids']==[peer['id']])
check('pre-peer saved first judgment byte preserved',sha((D/'first-judgment.json').read_bytes())==peer['first_judgment_sha256'])
check('report distinct from actual/candidate',f['actual_integration_commit'] is None and h['actual_commit'] is None and not f['actual_integration_reviewed'])
check('current candidate tree/parent exact',git('rev-parse',C+'^{tree}').decode().strip()==f['reviewed_tree'] and git('show','-s','--format=%P',C).decode().strip()==h['candidate_parent'])
check('full unfiltered predecessor→candidate diff exact',git('diff','--no-ext-diff','--no-textconv','--no-color','--no-renames','--binary','--full-index','--unified=3',B,C)==(D/'complete-predecessor-to-candidate.diff').read_bytes())
check('full diff bound bytes/hash exact',(D/'complete-predecessor-to-candidate.diff').stat().st_size==a['full_diff_bytes'] and sha((D/'complete-predecessor-to-candidate.diff').read_bytes())==a['full_diff_sha256'])
check('30 change identities exact',len(a['changes'])==30 and a['modified_count']==10 and a['added_count']==20 and a['modified_exactly_allowed'] and a['all_additions_under_B14'])
check('all24 complete object/control bindings exact',len(q['all24_object_bindings'])==24 and not any(x['mismatches']for x in q['all24_object_bindings']) and not a['control_mismatches'])
check('input families72/6/14 plus8 exact',a['binding_counts']==dict(planned_reads=72,write_inputs=6,current_extra_inputs=14,fixed_controls=8) and not a['binding_mismatches'])
check('four original scopes exact',len(a['original_scope_checks'])==4 and all(all(x[k]for k in ['before_match','after_match','approved_checkpoint_patch_unchanged','patch_hash_match'])for x in a['original_scope_checks']))
check('protected catalogs and original IDs exact',all(x['old_ids_order_preserved'] and x['old_multiplicity_preserved'] and all(y['byte_equal']for y in x['protected_rows'])for x in cats) and all(x['equal']for x in protect))
check('12/13 owner full paths remain equal',a['B04_formal_count']==13 and a['B04_full_paths_unchanged']==12 and all(x['accepted_baseline_equal']for x in read('B04-formal-preservation.json')))
check('author comparison follows own saved first judgment',datetime.datetime.fromisoformat(compare['compared_at_utc'])>datetime.datetime.fromisoformat(read('first-judgment.json')['saved_at_utc']) and compare['verdict_after_comparison']=='REQUEST_CHANGES')
check('author counts and16 log identities independently match',all(all(x[k]for k in ['counts_equal','changed_ids_equal','added_ids_equal','unchanged_rows_equal'])for x in compare['catalogs']) and all(x['actual_bytes_equal']for x in compare['checkpoint_files']) and len(compare['author_source_log_bindings'])==16 and all(x['identity_match'] and x['ranges_valid']for x in compare['author_source_log_bindings']))
events=[json.loads(s)for s in (D/'reading-events.jsonl').read_text().splitlines()]
for e in events:
 r=SREP if e['repository']=='reference' else R
 b=git('show',e['commit']+':'+e['path'],r=r)
 check('successful text-read identity '+e['path']+' '+str(e['start'])+'-'+str(e['end']),sha(b)==e['sha256'] and len(b)==e['bytes'] and 1<=e['start']<=e['end']<=len(b.decode().splitlines()))
def visited(ev):
 ranges=[(e['start'],e['end'])for e in events if e['commit']==ev['commit'] and e['path']==ev['path']]
 covered=set()
 for lo,hi in ranges:covered.update(range(lo,hi+1))
 return set(range(ev['lines'][0],ev['lines'][1]+1))<=covered
for finding in f['blocking_findings']:
 for e in finding['evidence']:check('finding numeric locus actually read '+e['path'],visited(e),e['lines'])
for e in peer['evidence']:check('peer-correlated locus independently actually read '+e['path'],visited(e),e['lines'])
for d in read('static-designs.json')['cases']:
 check('manual nonexecuted design '+d['id'],d['execution']=='NOT_EXECUTED' and not d['runtime_observation'] and bool(d['premises']) and bool(d['ordered_static_expected']) and bool(d['neighboring_reverse_control']))
 for e in d['source_evidence']:check('design source actually read '+d['id']+' '+e['path'],visited(e),e['lines'])
 check('design project numeric loci valid '+d['id'],all(1<=e['lines'][0]<=e['lines'][1]<=len(git('show',e['commit']+':'+e['path']).decode().splitlines())for e in d['project_evidence']))
check('reference remains exact detached clean without remote',git('rev-parse','HEAD',r=SREP).decode().strip()==S and git('rev-parse','HEAD^{tree}',r=SREP).decode().strip()==ref['tree'] and not git('status','--porcelain',r=SREP).strip() and not git('remote',r=SREP).strip() and subprocess.run(['git','symbolic-ref','-q','HEAD'],cwd=SREP,stdout=subprocess.PIPE).returncode!=0)
check('reference files absent from main tree delta',not any(x['path'].startswith('reference/') or x['path'].endswith('.gitignore')for x in a['changes']))
limits=read('source-limits.json')
check('configuration retained UNVERIFIED/no probes',limits['configuration']['effective_model_reasoning_speed']=='UNVERIFIED' and limits['configuration']['requested_reasoning']=='Ultra' and limits['configuration']['requested_speed']=='Standard(default)' and limits['configuration']['configuration_probes']==limits['configuration']['quota_probes']==0)
check('execution/observation/child/registry counters retained0',all(v==0 for k,v in limits.items()if k in ['reference_execution','game_execution','compiler_execution','converter_execution','generator_execution','deserializer_execution','author_or_historical_reviewer_program_execution','reference_behavior_simulation','behavior_vectors_executed','runtime_observations','proven_Demo_chains','child_tasks','reference_modification','reference_tracking_in_main_Git','ignore_modifications','reference_push']) and f['canonical_registry_writes']==f['canonical_IDs_closed']==f['new_canonical_root_count']==0)
# No report metadata is added outside D. The checks themselves intentionally do not certify semantic correctness.
st=git('status','--porcelain','-uall').decode().splitlines()
check('working tree writes only new report directory',bool(st) and all(s[3:].startswith(str(D.relative_to(R))+'/') and s[:2] in ['??','A '] for s in st),st)
failed=[x for x in checks if not x['pass_']]
result=dict(checked_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),kind='Fresh independent metadata/text/hash/evidence-range verification only; no behavior tests',check_count=len(checks),passed=len(checks)-len(failed),failed=len(failed),checks=checks,reference_or_author_execution=False,candidate_behavior_execution=False,report_SHA_binding='Pending ordinary report commit and remote readback; parent=C will be checked after commit. No self-SHA embedded.')
(D/'verification-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k]for k in ['check_count','passed','failed']},ensure_ascii=False));print(json.dumps(failed,ensure_ascii=False,indent=2))
sys.exit(1 if failed else 0)
