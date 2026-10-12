import pathlib,json,collections,datetime,sys
D=pathlib.Path(__file__).resolve().parent;root=D.parent.parent
v=json.loads((D/'verdicts.json').read_text());n=json.loads((D/'negative-evidence.json').read_text())
required=['finding_id','decision','severity','proposed_disposition','sources_actually_read','specs_actually_read','counterevidence_search','normal_boundary_check','execution_evidence_assessment','historical_relation_assessment','duplicate_of','reason','required_refinements','remaining_unknowns','reviewer','thread_id','evidence_level']
allowed={'CONFIRM','CONFIRM_WITH_REFINEMENT','REJECT','MERGE','OPTIONAL','UNRESOLVED'}
ids=[r['finding_id'] for r in v['records']];inputs=[]
for m in ['M01','M02','M03','M04','M05','M06']:inputs.extend(x['id'] for x in json.loads((root/'modules'/m/'findings.json').read_text())['findings'])
assert v['schema_version']=='1.0';assert len(ids)==len(set(ids))==11;assert sorted(ids)==sorted(inputs)
for r in v['records']:
 assert all(k in r for k in required);assert r['decision'] in allowed;assert r['sources_actually_read'] and r['specs_actually_read']
 assert r['counterevidence_search']['scope']['files']==131
 assert r['thread_id']=='01a1301e-5efe-77a2-9450-fc09ff6830c1'
 assert r['ca_behavior_execution']=='NOT_EXECUTED'
 assert r['decision']!='CONFIRM_WITH_REFINEMENT' or r['required_refinements']
for s in n['searches']:assert s['files_searched']==(131 if s['kind']=='B' else 312)
assert sorted(x['finding_id'] for x in n['records'])==sorted(ids)
for name in ['report.md','verdicts.json','negative-evidence.json','progress.md','execution.json']:assert (D/name).stat().st_size>0
counts=collections.Counter(r['decision'] for r in v['records']);sev=collections.Counter(r['severity'] for r in v['records'])
assert counts=={'CONFIRM':4,'CONFIRM_WITH_REFINEMENT':7};assert sev=={'P2':7,'P3':4}
result={'schema_version':'1.0','result':'PASS_ARTIFACT_STRUCTURE_ONLY','time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'python':sys.version,'input_candidates':len(inputs),'unique_verdict_records':len(ids),'decision_counts':dict(counts),'severity_counts':dict(sev),'formal_search_groups':sum(s['kind']=='B' for s in n['searches']),'all_formal_searches_cover_131':True,'behavior_execution':False,'semantic_self_rereview':False,'side_effects':'Only CA/validation-result.json'}
(D/'validation-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
