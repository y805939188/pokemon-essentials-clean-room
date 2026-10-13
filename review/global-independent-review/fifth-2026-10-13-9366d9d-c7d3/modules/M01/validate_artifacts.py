"""Validate audit artifacts only. Never executes reference or behavior vectors."""
import hashlib
import json
from pathlib import Path
import review_state as s

errors=[]
warnings=[]
documents={}
for path in sorted(s.OUT.glob('*.json')):
    try: data=json.loads(path.read_text())
    except Exception as exc:errors.append(f'{path.name}: JSON {exc}');continue
    documents[path.name]=data
    if data.get('schema_version')!='gr5.review.v1':errors.append(f'{path.name}: schema_version')

def filepath(path):
    if path.startswith(('Data/','PBS/','Text_english_core/')):return s.REF/path
    if path.startswith(('deliverables/','specs/','analysis/','planning/','review/','audit/')):return s.ROOT/path
    return None
lengths={}
def check_path_ranges(obj,where):
    path=obj.get('path')
    if not isinstance(path,str):return
    p=filepath(path)
    if p is None:return
    if not p.is_file():errors.append(f'{where}: missing path {path}');return
    ranges=obj.get('lines')
    if ranges is None and isinstance(obj.get('line'),int):ranges=[obj['line'],obj['line']]
    if ranges is None:return
    if not isinstance(ranges,list):return
    if len(ranges)==2 and all(isinstance(x,int) for x in ranges):ranges=[ranges]
    if not all(isinstance(x,list) and len(x)==2 and all(isinstance(n,int) for n in x) for x in ranges):return
    if path not in lengths:
        try:lengths[path]=len(p.read_text().splitlines())
        except UnicodeError:return
    for a,b in ranges:
        if not 1<=a<=b<=lengths[path]:errors.append(f'{where}: invalid range {path}:{a}-{b}/{lengths[path]}')
def walk(obj,where):
    if isinstance(obj,dict):
        check_path_ranges(obj,where)
        for k,v in obj.items():walk(v,where+'.'+k)
    elif isinstance(obj,list):
        for i,v in enumerate(obj):walk(v,where+f'[{i}]')
for name,data in documents.items():walk(data,name)

cov=documents['reading-coverage.json']
for kind in ('sources','specifications'):
    seen=set()
    for e in cov[kind]:
        if e['path'] in seen:errors.append(f'duplicate {kind} path {e["path"]}')
        seen.add(e['path']);p=filepath(e['path'])
        if p is None or not p.is_file():errors.append(f'coverage missing {e["path"]}');continue
        digest=hashlib.sha256(p.read_bytes()).hexdigest()
        if digest!=e.get('sha256'):errors.append(f'coverage changed bytes {e["path"]}')
        if e.get('line_count') is not None:
            n=len(p.read_text().splitlines())
            if n!=e['line_count']:errors.append(f'coverage line_count {e["path"]}: {e["line_count"]}!={n}')
            for a,b in e.get('read_ranges',[]):
                if not 1<=a<=b<=n:errors.append(f'coverage range {e["path"]}:{a}-{b}')

caps=documents['source-to-spec.json']['capabilities']
ids=[x['capability_id'] for x in caps]
if len(ids)!=len(set(ids)):errors.append('duplicate capability IDs')
for c in caps:
    if c['status'] not in {'supported','partial','missing','unresolved','not_reviewed'}:errors.append('cap status '+c['capability_id'])
    if not c.get('semantic_comparison_complete'):errors.append('cap comparison incomplete '+c['capability_id'])
for e in documents['spec-to-source.json']['clauses']:
    for identity in e.get('capability_refs',[]):
        if identity not in ids:errors.append('unresolved reverse capability '+identity)
vectors=[e for e in documents['spec-to-source.json']['clauses'] if e.get('clause','').startswith('vector ')]
if len(vectors)!=93 or len({e['clause'] for e in vectors})!=93:errors.append('primary93 vector identity mismatch')
if any(e['status']!='supported' for e in vectors):errors.append('primary vector unclosed')

required='id title module severity disposition status reviewer category source_baseline specification_baseline source_anchors spec_anchors expected_reference_behavior current_spec_behavior gap preconditions minimal_counterexample normal_case failure_or_boundary_case impact_on_independent_implementation negative_evidence_search proposed_spec_change affected_files shared_contracts acceptance_criteria dependencies related_capabilities related_findings root_cause_group priority batch_owner history_links evidence_level execution_status confidence unknowns excluded_claims user_decision_needed review_resolution'.split()
findings=documents['findings.json']['findings']
for f in findings:
    for key in required:
        if key not in f:errors.append(f'{f.get("id")}: missing {key}')
    if f['status']!='candidate_pending_independent_counterevidence':errors.append('candidate status '+f['id'])
    if f['disposition']=='required':errors.append('unapproved final required '+f['id'])

field_ids={f['field_id'] for f in documents['schema-field-contracts.json']['fields']}
if len(field_ids)!=247:errors.append('field247 identity mismatch')
pbs=documents['pbs-data-inspection.json']['files']
if len(pbs)!=73 or len({x['path'] for x in pbs})!=73:errors.append('PBS73 path mismatch')
for file in pbs:
    if not file.get('semantic_review_complete') or file.get('review_extent')!='full':errors.append('PBS incomplete '+file['path'])
    data=documents[file['record_review_artifact']]
    for r in data['records']:
        for prop in r.get('properties',[]):
            identity=prop.get('field_contract_ref')
            if identity and identity not in field_ids:errors.append('unknown field '+identity)
definitions=documents['configuration-consumer-ledger.json']['definitions']
if len(definitions)!=124:errors.append('configuration124 mismatch')
for d in definitions:
    if not d.get('semantic_review_complete') or not d.get('spec_anchors'):errors.append('config unmapped '+d['key'])
    for h in d['occurrences']:
        if h.get('semantic_review') not in {'current_contract_compared','reviewed_not_an_active_consumer'}:errors.append('config occurrence unclosed '+str(h))
if len(documents['configuration-branch-reviews.json']['branches'])!=140:errors.append('branch140 mismatch')

result=dict(schema_version='gr5.review.v1',module='M01',check_scope='Audit artifact syntax, anchors, hashes, references and declared coverage consistency only; not reference/model/vector execution.',
 json_files=len(documents),coverage_source_paths=len(cov['sources']),coverage_spec_paths=len(cov['specifications']),
 primary_vectors=len(vectors),findings=len(findings),errors=errors,warnings=warnings,
 result='PASS' if not errors else 'FAIL')
s.write('artifact-validation.json',result)
print(json.dumps(result,ensure_ascii=False))
raise SystemExit(1 if errors else 0)
