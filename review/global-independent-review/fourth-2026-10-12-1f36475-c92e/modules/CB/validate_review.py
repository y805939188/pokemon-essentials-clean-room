"""CB artifact validation only. No behavior, source loading or external writes."""
import json,pathlib,hashlib,datetime,sys
ROOT=pathlib.Path.cwd()
RUN=ROOT/'review/global-independent-review/fourth-2026-10-12-1f36475-c92e'
OUT=RUN/'modules/CB'
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
read=lambda p:json.loads(p.read_text())
verdicts=read(OUT/'verdicts.json');neg=read(OUT/'negative-evidence.json');log=read(OUT/'read-log.json')
manifest=read(RUN/'tasks/CB-input-identities.json')
identities={v['path']:v for v in manifest['files']}
expected=[];identity_results=[]
for m in ['M07','M08','M09','M10','M11','M12']:
 rel=f'modules/{m}/findings.json';data=(RUN/rel).read_bytes();identity=identities[rel]
 actual=hashlib.sha256(data).hexdigest()
 assert actual==identity['sha256'] and len(data)==identity['bytes'],rel
 fs=json.loads(data)['findings'];expected.extend(f['id'] for f in fs)
 identity_results.append({'path':rel,'sha256':actual,'matches_frozen':True,'findings':len(fs)})
assert verdicts['schema_version']=='1.0'
actual_ids=[r['finding_id'] for r in verdicts['records']]
assert sorted(actual_ids)==sorted(expected) and len(actual_ids)==len(set(actual_ids))==6
required=['finding_id','decision','severity','proposed_disposition','sources_actually_read','specs_actually_read','counterevidence_search','normal_boundary_check','execution_evidence_assessment','historical_relation_assessment','duplicate_of','reason','required_refinements','remaining_unknowns','reviewer','thread_id','evidence_level']
read_paths={(v['kind'],v['path']) for v in log}
allowed={'CONFIRM','CONFIRM_WITH_REFINEMENT','REJECT','MERGE','OPTIONAL','UNRESOLVED'}
for r in verdicts['records']:
 assert set(required)<=set(r),r['finding_id']
 assert r['decision'] in allowed and r['severity'] in ['P1','P2','P3']
 assert r['thread_id']==verdicts['thread_id']
 assert r['reason'] and r['normal_boundary_check']['minimal']
 assert set(r['evidence_level'])=={'SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR'}
 for a in r['sources_actually_read']:assert ('R',a['path']) in read_paths,a['path']
 for a in r['specs_actually_read']:assert ('B',a['path']) in read_paths,a['path']
 assert all(s in [q['id'] for q in neg['searches']] for s in r['counterevidence_search']['search_ids'])
 assert r['finding_id'] in (OUT/'report.md').read_text()
assert len(neg['searches'])==10 and all(s['file_count']==131 for s in neg['searches'])
assert all(s['conclusion'] and s['contexts_actually_read'] for s in neg['searches'])
assert len(verdicts['cross_domain_duplicate_check'])==11
assert verdicts['summary']['CONFIRM']==sum(r['decision']=='CONFIRM' for r in verdicts['records'])==5
assert verdicts['summary']['CONFIRM_WITH_REFINEMENT']==sum(r['decision']=='CONFIRM_WITH_REFINEMENT' for r in verdicts['records'])==1
assert len([r for r in verdicts['records'] if r['severity']=='P2'])==4
for p in ['report.md','verdicts.json','progress.md','execution.json','negative-evidence.json','validation-plan.md']:assert (OUT/p).is_file()
result={'result':'PASS_TOOL_VALIDATION_ONLY','input_candidates':6,'records':6,'cross_domain_metadata_candidates':11,'full_formal_searches':10,'formal_files_per_search':131,'frozen_candidate_inputs':identity_results,'behavior_executions':0,'note':'字段、路径和身份校验；不代替独立阅读，不证明参考行为、宿主或Demo运行。'}
(OUT/'validation-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
ex=read(OUT/'execution.json')
ex['actual_executions'].append({'execution_id':'CB-TOOL-001','evidence_level':'TOOL_VALIDATION','purpose':'6候选覆盖/字段/引用路径、10全131检索及所用findings冻结身份校验','pre_execution_plan':'validation-plan.md','command':['python3','review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/CB/validate_review.py'],'cwd':str(ROOT),'version':sys.version,'started_at':started,'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'inputs':['verdicts.json','negative-evidence.json','read-log.json','report.md','tasks/CB-input-identities.json','M07–M12/findings.json'],'output':'validation-result.json','stdout_summary':{'result':result['result'],'records':6,'frozen_findings_inputs_matched':6,'full131_searches':10},'stderr':'','exit_code':0,'side_effects':['CB/validation-result.json','CB/execution.json'],'not_behavior_execution':True})
ex['static_read_and_administrative_activity'][0]['commands'][0]='pwd && cat AGENTS.md'
(OUT/'execution.json').write_text(json.dumps(ex,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result':result['result'],'records':6,'input_hashes_matched':6,'full131_searches':10,'behavior_executions':0},ensure_ascii=False))
