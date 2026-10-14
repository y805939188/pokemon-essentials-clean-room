"""Assemble human static-review judgments and payload coverage, without game execution."""
import datetime, hashlib, json, pathlib, re, subprocess
ROOT=pathlib.Path('/workspace/pokemon-essentials-clean-room')
OWN=pathlib.Path(__file__).resolve().parent
ACTUAL='86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
PRE='review/remediation-sixth-20261014-prepare/'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def digest(d):return dict(bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest())
def load(p):return json.loads((OWN/p).read_text())
def save(p,j):(OWN/p).write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
def canon(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
reports=(OWN/'report.md').read_text()
groups=['identity_and_verdict','bidirectional_evidence','premises_and_counterexample','minimum_revision_contract','acceptance_and_regression','independent_adjudication','dependencies_and_receivers']
rows=[]
for b in ['R6-U02','R6-U04','R6-U05']:
 p=PRE+'contracts/'+b+'.json';raw=git('show',ACTUAL+':'+p);j=json.loads(raw)
 for n,r in enumerate(j['scope_contracts']):
  marker='**'+r['id']+' — PASS。**'
  assert marker in reports
  paragraph=reports.split(marker,1)[1].split('\n\n',1)[0].strip()
  rows.append(dict(id=r['id'],batch=b,actual_commit=ACTUAL,verdict='ACTUAL_INTEGRATED_PASS_SCOPED_STATIC',necessary_repairs=[],contract=dict(path=p,identity=digest(raw),scope_pointer='/scope_contracts/'+str(n)),
                   seven_groups=[dict(group=k,json_pointer='/scope_contracts/'+str(n)+'/'+k,canonical_value_sha256=canon(r[k]),verdict='PASS_UNDER_FROZEN_SCOPE',evidence='Report per-ID paragraph; exact actual formal full reading and fixed source/rebuttal ledger, not merely tool exit') for k in groups],
                   exact_acceptance_and_regression=r['acceptance_and_regression'],reasoning=paragraph,evidence_level=['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR'],execution='NOT_EXECUTED'))
assert len(rows)==9
save('criteria-results.json',dict(actual_commit=ACTUAL,result='ACTUAL_INTEGRATED_PASS_SCOPED_STATIC',required_count=9,passed=9,failed=0,ids=rows,additional_interface=dict(batch='R6-U13',scope='GR6-F-V004 alias GR6-F-007 WP40 Arena cancellation vs recharge; no other U13 signoff',verdict='PASS_SCOPED_STATIC'),formal_acceptance=False,CLOSED=False))
catalogs={
 'deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md':{'GR6-C-001':[f'S{i:02}' for i in range(10,17)],'GR6-CA-EB-001':[f'B{i}' for i in range(72,77)],'GR6-CA-EB-002':[f'B{i}' for i in range(77,83)]},
 'deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md':{'GR6-C-002':['HI10'+x for x in 'abcdef'],'R6-CM-SE-001':[f'SS{i}' for i in range(43,48)],'R6-CM-SE-002':[f'SS{i}' for i in range(48,53)],'R6-CM-SE-003':[f'SS{i}' for i in range(53,60)]},
 'deliverables/final-specification-set/test-catalog/combat-requirements-wp47-ab.md':{'R6-CM-CALL-01':[f'MA-T{i}' for i in range(11,17)]}}
vectors=[]
for p,want in catalogs.items():
 raw=git('show',ACTUAL+':'+p);lines=raw.decode().splitlines()
 for owner,ids in want.items():
  for case in ids:
   found=[];section=''
   for i,l in enumerate(lines,1):
    if l.startswith('## '):section=l
    if l.startswith('| '+case+' |') and (owner!='GR6-C-001' or section.startswith('## AI：')):found.append((i,l))
   assert len(found)==1,(case,found)
   number,line=found[0]
   vectors.append(dict(required_id=owner,case=case,actual_commit=ACTUAL,path=p,line=number,identity=digest(raw),actual_row=line,human_assessment='PASS_DERIVED_UNDER_ROW_AND_COMMON_PREMISES',execution='NOT_EXECUTED',method='Human independent source/contract reasoning in report; extraction here only binds the exact row. No game simulation or assertion execution.'))
assert len(vectors)==47
save('derived-vector-assessment.json',dict(new_case_rows=len(vectors),vectors=vectors,navigation_only=dict(id='R6-CA-EA-P001',result='PASS_exact_hazards_5.2_weather_5.1'),other_regressions=['Life Dew B64–B71','HI10 original local result','MA-T07–10 type-stable controls','Arena P30–P32 interface only'],new_behavior_execution=0))
ledger=[json.loads(l) for l in (OWN/'reading-ledger.jsonl').read_text().splitlines()]
bindings=load('input-bindings.json');full=[]
for p in bindings['formal_paths']:
 total=len(git('show',ACTUAL+':'+p).splitlines());cover=set()
 rr=[]
 for i,r in enumerate(ledger,1):
  if r['commit']==ACTUAL and r['path']==p and r['json_key'] is None:
   cover.update(range(r['start'],r['end']+1));rr.append(i)
 missing=sorted(set(range(1,total+1))-cover)
 assert not missing,(p,missing)
 full.append(dict(path=p,lines=total,recorded_full_range_coverage=True,ledger_rows=rr,human_semantic_reading='COMPLETE_FULL_ACTUAL_DOCUMENT_NEW_READ',identity=digest(git('show',ACTUAL+':'+p))))
save('reading-coverage.json',dict(actual_commit=ACTUAL,new_ledger_rows=len(ledger),group_formal_files=full,additional_scope='WP56 full; WP42 relevant tail; Arena P30–P32 and full relevant source/caller/status/PP/item chains. Exact ranges/JSON keys in ledger.',
       same_session_reuse='71 earlier U04 rows reverified at exact immutable identity, recorded separately; old verdict/runtime not reused.',
       limitations=['Full source/input bytes fetched or parsed do not establish semantic reading of every byte. JSON projections mean only the displayed fields. Formal 14 full reads and WP56 full read were semantically inspected.',
                    'Early global actual input cat truncated; relevant metadata/batches/files later read and mechanically bound. No complete 56-item semantic input claim.',
                    'Some early lookups were outside run.py and have platform outputs but no per-process local UTC record; no later timestamp is substituted for them.',
                    'Earlier output aggregation exceeded token budget for R5 findings4/5; each reread separately fully. U13 bidirectional output similarly reread bounded.'],
       lookup_and_descriptor_issues=['Copy from current old-review path absent: recovered tools from exact prior review commit.',
       'U05 report absent at actual snapshot: reread exact review commit 77681de.',
       'Wrong formal_paths key corrected to all_candidate_allowlist_paths; list-shaped historical JSON not dict; oversized accidental list display excluded from full-reading claim.',
       'Selected-historical-scopes belongs to candidate evidence, not reviewer path; corrected fixed pointer.',
       'Arena guessed Other battle code path absent: corrected ledger path 008_Other battle types/004_BattleArenaBattle.rb and read185–220.',
       'Initial raw-ID checker and vector row assembler collapsed AI and AE series; corrected section-qualified IDs. Initial history preservation demanded entire old dream-talk line; exact old sentences and ordering retained with bounded insertion. Failed process logs retained.']))
save('execution-and-limitations.json',dict(requested=dict(model='gpt-6.1-sol',reasoning_effort='ultra',service_tier='default',speed='default/non-Fast'),effective=dict(model='UNVERIFIED',reasoning_effort='UNVERIFIED',service_tier='UNVERIFIED',speed='UNVERIFIED',platform_task_UUID='UNVERIFIED'),
      no_extra_CLI_agent_config_probe=True,independence='Direct non-author reviewer; same-session prior U04 reviewer, not an author of reviewed candidates. No separate-agent certification claimed.',
      new_execution=dict(isolated_reference=0,reference_with_surrogates=0,independent_behavior_model=0,full_host_demo=0,real_save=0,production_service=0),
      tool_validation=dict(new_payload_checks=131,result='131/131 PASS; only text/Git/JSON identity and finite structural assertions',historical_bound_projections=41,historical_preserved_spans=56,continuous_preserved_spans=49),
      prior_U04_evidence=dict(review_commit='4be1e586fcbe2416c33ede333430e5f2918f3cae',reproduced_author_tool_checks=337,additional_independent_tool_checks=55,derived_case_rows=11,reference_model_host_execution=0,transfer_boundary='Prior same-session verification at exact U04 candidate; not rerun on actual or promoted to runtime'),
      author_tools_read='U02 final static process exit0 (finite payload/history validation); U05 validation-04 exit0/429. Input process evidence only; not a new independent behavioral reproduction.',
      unresolved=['Actual effective configuration and platform UUID lack echo.', 'Runtime, host resources/diagnostics recovery, actual menus/save/service behavior not executed.', 'Future compatibility of historical exceptions is separate policy, not a required current content fix.', 'R6-I administrative sync, other scopes, formal acceptance and CLOSED remain pending.'],necessary_content_repairs=[]))
print(json.dumps(dict(required=9,passed=9,derived_not_executed=47,formal_full_reads=len(full),ledger_rows=len(ledger),reference_model_host_execution=0)))
