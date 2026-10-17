#!/usr/bin/env python3
"""Read-only crosscheck of root aggregation; writes only its own new JSON evidence."""
import ast
import collections
import datetime
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT=Path('/workspace/r8-disposition-r3-review')
OUT=ROOT/'review/r8-disposition-r3-independent-c0f62d9-20261017'
DEST=OUT/'agents/kernel-aggregate-crosscheck.json'
BASE='planning/implementation-routing/r8-20261017/'
C='c0f62d973180679134f2eb1a488c1dc359c8658f'
S='5f87743293290de2e219ecdd6c19e88280f60c9a'
R2='a32873d2860b15d9f5e27727db8f131f4ec433b6'
RR='0ef0b7ad5f9465cfe31da0d7a35f56b5ccba5add'
RP='review/r8-disposition-r2-independent-a32873d-20261017/'
BAD={'FR-000173':'R3-SOURCE-ATTRIBUTION-001','FR-000227':'R3-SOURCE-ATTRIBUTION-001','FR-000596':'R3-SOURCE-ATTRIBUTION-001','FR-000029':'R3-EV-BOUNDARY-001','FR-000032':'R3-EV-BOUNDARY-001','FR-000204':'R3-EV-BOUNDARY-001','FR-000456':'R3-EV-BOUNDARY-001'}
NAMES=['aggregate.py','feature-results.json','finding-results.json','issue-results.json','reading-coverage.json','section-results.json','result.json','findings.json']

def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sh(b):return hashlib.sha256(b).hexdigest()
def raw(c,p):return subprocess.check_output(['git','-C',str(ROOT),'show',c+':'+p])
def jb(c,p):return json.loads(raw(c,p))
def load(p):return json.loads(p.read_text())
def ptr(value,pointer):
    if not pointer:return value
    assert pointer.startswith('/'),pointer
    for key in pointer[1:].split('/'):
        key=key.replace('~1','/').replace('~0','~')
        value=value[int(key)] if isinstance(value,list) else value[key]
    return value

started=now();inputs={n:(OUT/n).read_bytes() for n in NAMES}
docs={n:json.loads(b) for n,b in inputs.items() if n.endswith('.json')}
ast.parse(inputs['aggregate.py'])
m=jb(C,BASE+'routing-manifest.json')
pm=jb(R2,BASE+'routing-manifest.json')
original=jb('d62b41f4d620e50bb04c80a7505374bd284d8210',BASE+'routing-manifest.json')
r2f=jb(RR,RP+'feature-results.json')
r2g=jb(RR,RP+'finding-results.json')['finding_results']
r2i=jb(RR,RP+'issue-results.json')['issue_results']
r2find=jb(RR,RP+'findings.json')['findings']
cv=jb(C,BASE+'current-section-coverage.json')
hc=jb(C,BASE+'section-coverage.json')
checks=[]
def check(name,passed,details=None):checks.append(dict(check=name,verdict='PASS' if passed else 'FAIL',details=details))
def exact(name,rows,key,expected):
    values=[r[key] for r in rows]
    missing=sorted(set(expected)-set(values));extra=sorted(set(values)-set(expected));dups=sorted(k for k,v in collections.Counter(values).items() if v>1)
    check(name,not missing and not extra and not dups,dict(count=len(values),expected=len(expected),missing=missing,extra=extra,duplicate=dups))

old=docs['feature-results.json']['old_feature_results']
active=docs['feature-results.json']['active_feature_results']
meta=docs['feature-results.json']['retired_metadata_results']
groups=docs['finding-results.json']['finding_results']
issues=docs['issue-results.json']
reading=docs['reading-coverage.json']['documents']
sections=docs['section-results.json']['sections']
heads=docs['section-results.json']['new_heading_results']
findings=docs['findings.json']['findings']
result=docs['result.json'];counts=result['counts']
f={r['feature_id']:r for r in m['features']};pf={r['feature_id']:r for r in pm['features']}
ret={r['feature_id']:r for r in m['retired_features']}
r2active={r['feature_id']:r for r in r2f['active_feature_results']}
exact('old721_ID_set',old,'feature_id',{r['feature_id'] for r in original['features']})
exact('active736_ID_set',active,'feature_id',f)
exact('metadata33_ID_set',meta,'metadata_id',{r['metadata_id'] for r in m['metadata_records']})
exact('original44_group_set',groups,'finding_id',{r['finding_id'] for r in r2g})
exact('R2_seven_issue_set',issues['R2_seven_issue_results'],'issue_id',{r['id'] for r in r2find})
exact('R1_twelve_issue_set',issues['R1_twelve_issue_results'],'issue_id',{r['issue_id'] for r in r2i})
exact('primary131_document_set',reading,'path',{r['source']['path'] for r in m['documents']})
exact('current2704_heading_set',[{'key':r['path']+'#'+r['anchor']} for r in sections],'key',{r['path']+'#'+r['anchor'] for r in cv['sections']})
oldkeys={(r['path'],r['anchor']) for r in hc['sections']}
newkeys={(r['path'],r['anchor']) for r in cv['sections']}-oldkeys
normalized_heads=[]
for r in heads:
    anchor=r.get('anchor') or r.get('current_identity',{}).get('anchor')
    if not anchor:
        matches=[s['anchor'] for s in cv['sections'] if s['path']==r['document'] and s['title']==r['title']]
        anchor=matches[0] if len(matches)==1 else 'AMBIGUOUS_TITLE:'+r['title']
    normalized_heads.append({'key':r['document']+'#'+anchor})
exact('new21_heading_set',normalized_heads,'key',{p+'#'+a for p,a in newkeys})

facets=['classification','responsibility','scope','dependency','current_calibration']
badfacets=[]
for r in active:
    expected={k:('FAIL' if k=='current_calibration' and r['feature_id'] in BAD else 'PASS') for k in facets}
    if r.get('normalized_facets')!=expected:badfacets.append(dict(feature_id=r['feature_id'],actual=r.get('normalized_facets'),expected=expected))
    if r['r2_verdict']!=r2active[r['feature_id']]['verdict']:badfacets.append(dict(feature_id=r['feature_id'],error='R2 verdict mismatch'))
check('all736_five_normalized_facets',not badfacets,badfacets)
check('seven_calibration_FAIL_rows_exact', {r['feature_id'] for r in active if r['verdict']=='FAIL'}==set(BAD))
check('all_old721_states_and_pointers_match_fixed_candidate',all(r['current_state']==('active' if r['feature_id'] in f else 'retired') and ptr(m,r['candidate_pointer'])['feature_id']==r['feature_id'] for r in old))
check('all_active_candidate_source_scope_locator_match',all(ptr(m,r['candidate_pointer'])['feature_id']==r['feature_id'] and r['fixed_source']==f[r['feature_id']]['source'] and r['functional_scope']==f[r['feature_id']]['functional_scope'] and r['current_applicability']==f[r['feature_id']]['current_applicability'] for r in active))
check('original44_specific_cases_PASS',all(r['original_case_verdict']=='PASS' for r in groups))
check('original44_classification_dependency_PASS',all(r['current_classification_dependency_scope_verdict']=='PASS' for r in groups))
check('expanded_group_FAIL_exact_COMBAT05_POKS05',{r['finding_id'] for r in groups if r['verdict']=='FAIL'}=={'COMBAT-05','POK-S05'},[(r['finding_id'],r.get('attributed_group_verdict'),r.get('current_scope_verdict'),r['verdict']) for r in groups if r['verdict']=='FAIL'])
check('all19_historical_issues_PASS',all(r['verdict']=='PASS' for a in ['R2_seven_issue_results','R1_twelve_issue_results'] for r in issues[a]))
check('R2_failed28_all_PASS',collections.Counter(r['verdict'] for r in active if r['r2_verdict']=='FAIL')=={'PASS':28})
check('R2_old708_propagates701_PASS7_calibrationFAIL',collections.Counter(r['verdict'] for r in active if r['r2_verdict']=='PASS')=={'PASS':701,'FAIL':7})
check('aggregate_counts_recomputed',counts['old721']==dict(collections.Counter(r['verdict'] for r in old)) and counts['active736']==dict(collections.Counter(r['verdict'] for r in active)) and counts['metadata33']==dict(collections.Counter(r['verdict'] for r in meta)) and counts['facets']=={k:dict(collections.Counter(r['normalized_facets'][k] for r in active)) for k in facets})
check('two_canonical_finding_set',{r['id'] for r in findings}==set(BAD.values()))
cases=[(finding['id'],case) for finding in findings for case in finding['cases']]
check('seven_finding_cases_unique_and_owned',len(cases)==7 and len({r['feature_id'] for _,r in cases})==7 and all(BAD.get(r['feature_id'])==id for id,r in cases))

pointerresults=[]
for fid,c in cases:
    actual=ptr(m,c['candidate_pointer'])
    entries=[]
    for r in c['related_candidate_pointers']:
        try:
            v=ptr(jb(C,r['path']),r['pointer']);entries.append(dict(path=r['path'],pointer=r['pointer'],exists=True,value=v))
        except (KeyError,IndexError,ValueError) as err:entries.append(dict(path=r['path'],pointer=r['pointer'],exists=False,error=repr(err)))
    sr=f[c['feature_id']]['current_applicability']['locator'];lines=raw(S,c['current_source_document']).splitlines(keepends=True)
    unit=b''.join(b''.join(lines[a-1:b]) for a,b in c['current_effective_ranges'])
    sourceok=(c['source_identity']==sr and c['current_source_commit']==S and sh(unit)==sr['unit_sha256'])
    patch=[x for x in entries if 'source-refinement-patch' in x['path']]
    passcase=actual==c['candidate_claim'] and sourceok and all(x['exists'] for x in entries) and patch[0].get('value')==actual
    check('finding_case_pointers_'+c['feature_id'],passcase)
    pointerresults.append(dict(finding_id=fid,feature_id=c['feature_id'],candidate_pointer=c['candidate_pointer'],candidate_value_matches=actual==c['candidate_claim'],current_source_identity_and_unit_matches=sourceok,related_pointers=entries))
check('failed_feature_findings_refs_exact',all(r.get('finding_refs')==[BAD[r['feature_id']]] for r in active if r['feature_id'] in BAD))

# Resolve every aggregate attribution pointer, retaining different agent-level verdict scopes.
reviewptr=[]
def walk(x,where):
    if isinstance(x,dict):
        for k,v in x.items():
            if k=='review_evidence' and isinstance(v,str):reviewptr.append((where+'/'+k,v))
            walk(v,where+'/'+k)
    elif isinstance(x,list):
        for i,v in enumerate(x):walk(v,where+'/'+str(i))
for n in docs:walk(docs[n],n)
broken=[];resolved=0;jsoncache={};contexts=collections.Counter()
for where,target in reviewptr:
    path,_,pointer=target.partition('#');context='R3'
    if '/r1_identity_and_semantic_credit/' in where or '/r1_reading_record/' in where:context='R1'
    elif '/r2_reading_credit/' in where or '/inherited_r2_reading/' in where:context='R2'
    contexts[context]+=1
    try:
        key=(context,path)
        if key not in jsoncache:
            data=(OUT/path).read_bytes() if context=='R3' else raw(RR,RP+path) if context=='R2' else raw('8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8','review/r8-disposition-r1-independent-5666b7b-20261017/'+path)
            jsoncache[key]=json.loads(data) if pointer else None
        if pointer:ptr(jsoncache[key],pointer)
        resolved+=1
    except (OSError,KeyError,IndexError,ValueError,AssertionError) as err:broken.append(dict(location=where,target=target,error=repr(err)))
check('all_root_attribution_pointers_resolve',not broken,dict(total=len(reviewptr),resolved=resolved,by_fixed_review_context=dict(contexts),broken=broken))

cvindex={(r['path'],r['anchor']):r for r in cv['sections']}
check('all2704_section_values_match_candidate',all(all(r[k]==v for k,v in cvindex[(r['path'],r['anchor'])].items()) for r in sections))
headingchecks=[]
for d in reading:
    path=d['path'];lines=raw(S,path).splitlines(keepends=True);actual=[]
    for i,line in enumerate(lines,1):
        match=re.match(rb'^(#{1,6})\s+(.+?)\s*\n?$',line)
        if match:actual.append((i,len(match[1]),match[2].decode().strip(),sh(line)))
    expected=[r for r in sections if r['path']==path]
    ok=len(actual)==len(expected)
    if ok:
        for n,(i,level,title,hsh) in enumerate(actual):
            end=next((h[0]-1 for h in actual[n+1:] if h[1]<=level),len(lines));rec=next((r for r in expected if r['line_start']==i),{})
            ok=ok and (rec.get('level'),rec.get('title'),rec.get('line_end'),rec.get('heading_sha256'))==(level,title,end,hsh)
    headingchecks.append(dict(path=path,current_heading_count=len(actual),verdict='PASS' if ok else 'FAIL'))
check('all131_Git_bodies2704_heading_identity_ranges',all(r['verdict']=='PASS' for r in headingchecks),dict(documents=len(headingchecks),headings=sum(r['current_heading_count'] for r in headingchecks)))

# Neither six responsibility refinements nor accepted source bindings imply compatibility.
rolechanges={r['feature_id'] for r in m['features'] if r['future_plan']!=pf[r['feature_id']]['future_plan']}
check('exact_six_responsibility_refinements',rolechanges=={'FR-000092','FR-000397','FR-000645','FR-000647','FR-000699','FR-000703'},sorted(rolechanges))
bound=[r for r in m['features'] if r['upstream'].get('batches')]
check('all230_bound_rows_accepted_source_only',len(bound)==230 and all(r['upstream']['accepted_events'] and r['upstream']['status']=='已回填ACCEPTED源规格；去向待独立复审' for r in bound),dict(bound=len(bound)))
check('all736_pending_destination_unimplemented_unaccepted_unapproved',all(r['destination_verification']=={'status':'待验证','evidence':[],'source_only_is_compatibility_evidence':False} and r['implementation']=={'status':'未实现','acceptance_status':'未验收','evidence':[]} and r['future_plan']['stage']=='待定' and r['future_plan']['stage_approval']=='未批准' and r['future_plan']['exclusion_decision'] is None for r in m['features']))
check('four_prototypes_unexecuted',len(m['prototypes'])==4 and all(r['status']=='未运行' for r in m['prototypes']))
check('root_compatibility_separate_from_source_and_classification',result['classification_corrections_verdict']=='PASS' and result['final_cumulative_source_calibration_verdict']=='FAIL' and result['overall_verdict']=='FAIL' and result['source_acceptance_identity_and_binding_verdict']=='PASS' and result['target_compatibility']=='UNVERIFIED' and counts['CLOSED']==0)
check('aggregate_script_parsed_not_executed',True,dict(ast_nodes=sum(1 for _ in ast.walk(ast.parse(inputs['aggregate.py']))),root_outputs_written=False))
unchanged=all((OUT/n).read_bytes()==data for n,data in inputs.items());check('root_input_hashes_unchanged_during_read',unchanged)
failures=[r for r in checks if r['verdict']=='FAIL']
prior=load(DEST).get('attempts',[]) if DEST.exists() else [dict(verdict='REVIEWER_HELPER_ERROR',exit_code=1,
    start_utc='UNVERIFIED; original tool output retained in conversation',end_utc='UNVERIFIED',
    stderr="KeyError: 'documents' at the primary131 set lookup: current-section-coverage contains sections, not a document array.",
    correction='Read the complete fixed candidate routing-manifest documents source paths as the expected131 set; root artifacts unchanged.'),
    dict(verdict='REVIEWER_HELPER_ERROR',exit_code=1,start_utc='UNVERIFIED; original tool output retained in conversation',end_utc='UNVERIFIED',
    stderr="KeyError: 'document' in document source identity: document records use source.path, whereas feature records use source.document.",
    correction='Use document source.path after inspecting the actual document identity shape; root artifacts unchanged.')]
attempt=dict(start_utc=started,end_utc=now(),verdict='PASS' if not failures else 'FAIL',failure_checks=[r['check'] for r in failures])
output=dict(schema='r8-r3-kernel-root-aggregate-crosscheck.v1',candidate_commit=C,current_source_commit=S,verdict=attempt['verdict'],checks=checks,
            canonical_case_pointer_results=pointerresults,current_heading_git_checks=headingchecks,
            inputs={n:dict(bytes=len(b),sha256=sh(b)) for n,b in inputs.items()},attempts=prior+[attempt],
            qualification='Independent aggregation/set/facet/pointer/current-heading crosscheck only. Agent-level attributed verdict versus expanded group scope is preserved, not treated as an aggregation defect. No business execution or compatibility approval.',
            writes=[str(DEST.relative_to(ROOT))],root_artifacts_modified=False)
if DEST.exists():
    previous=load(DEST)
    output['prior_failed_check_records']=previous.get('prior_failed_check_records',[])+[r for r in previous.get('checks',[]) if r['verdict']=='FAIL']
    output['checker_corrections']=['Current new-heading records may identify a unique fixed document/title without repeating anchor; resolve against fixed current coverage and still require exact21 set.', 'Nested R2/R1 semantic reading credits retain their fixed historical report context; resolve their attribution pointers at RR/8c8, not at R3. Cache parsed targets without changing checked bytes.']
DEST.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(verdict=output['verdict'],checks=len(checks),failed_checks=[r['check'] for r in failures],pointers=resolved,attempts=len(output['attempts'])),ensure_ascii=False))
raise SystemExit(0 if not failures else 1)
