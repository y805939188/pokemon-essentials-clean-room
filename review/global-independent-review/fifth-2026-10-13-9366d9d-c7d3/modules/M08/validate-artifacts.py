"""Artifact integrity checks only; no behavior/reference execution."""
import sys,json,datetime,collections
from pathlib import Path
sys.dont_write_bytecode=True
from ledger import read,write,ROOT
names=['reading-coverage.json','source-to-spec.json','spec-to-source.json','findings.json','shared-interfaces.json','progress.json']
objects={n:read(n) for n in names};errors=[]
for n,o in objects.items():
    if o.get('schema_version')!='gr5.review.v1':errors.append('schema '+n)
for n in ['report.md','progress.md']:
    if not (ROOT/n).is_file():errors.append('missing '+n)
cov=objects['reading-coverage.json'];src=objects['source-to-spec.json'];rev=objects['spec-to-source.json'];findings=objects['findings.json'];shared=objects['shared-interfaces.json'];prog=objects['progress.json']
rv=cov['source_baseline']['commit'];bv=cov['specification_baseline']['commit'];R=Path(cov['source_baseline']['root']);source_map={s['path']:s for s in cov['sources']}

def rs(v):
    if not v:return []
    return [v] if isinstance(v[0],int) else v

def anchor_check(a,where):
    if not isinstance(a,dict):errors.append('unstructured source anchor '+where);return
    path=a.get('path')
    if not path:return
    if path in source_map:
        n=source_map[path]['line_count'];expected=rv
    elif Path(path).is_file():
        n=len(Path(path).read_text().splitlines());expected=bv
    else:errors.append('unresolvable path '+where+': '+str(path));return
    if a.get('version')!=expected:errors.append('version '+where+': '+path)
    for pair in rs(a.get('lines',[])):
        if len(pair)!=2 or not all(isinstance(x,int) for x in pair) or not 1<=pair[0]<=pair[1]<=n:errors.append('invalid range '+where+': '+path+' '+str(pair)+' max'+str(n))

for s in cov['sources']:
    if s['version']!=rv:errors.append('source version '+s['path'])
    actual=len((R/s['path']).read_text().splitlines())
    if actual!=s['line_count']:errors.append('linecount '+s['path'])
    if s['M08_scope_review_extent']!='full' or s['within_M08_unreviewed_ranges']:errors.append('incomplete scoped source '+s['path'])
    if s['scope_role']=='primary' and (s['review_extent']!='full' or s['unreviewed_ranges']):errors.append('incomplete primary '+s['path'])
    for r in s['semantic_ranges']:
        if not 1<=r['lines'][0]<=r['lines'][1]<=actual:errors.append('semantic range '+s['path'])
    for r in s.get('data_semantic_ranges',[]):
        for pair in r['lines']:
            if not 1<=pair[0]<=pair[1]<=actual:errors.append('data range '+s['path'])
    for p in s['unreviewed_ranges']:
        if not 1<=p[0]<=p[1]<=actual:errors.append('unreviewed bound '+s['path'])

ids=[c['id'] for c in src['capabilities']]
if len(ids)!=len(set(ids)):errors.append('duplicate canonical capability')
contracts=[c['id'] for c in shared['contracts']]
if len(contracts)!=len(set(contracts)):errors.append('duplicate shared contract')
groups=rev['source_anchor_groups'];used=set()
for s in rev['specifications']:
    if s['version']!=bv:errors.append('specversion '+s['path'])
    n=len(Path(s['path']).read_text().splitlines())
    for c in s['clause_mappings']:
        if c['review_extent']!='full' or c['evidence_level']!='static_semantic_clause_comparison':errors.append('incomplete clause '+s['path']+str(c['lines']))
        gid=c.get('source_anchor_group_ref');used.add(gid)
        if gid not in groups:errors.append('missing group '+str(gid));continue
        g=groups[gid]
        if g['specification_path']!=s['path'] or not g['specification_lines'][0]<=c['lines'][0]<=c['lines'][1]<=g['specification_lines'][1]:errors.append('wrong group scope '+gid)
        if not 1<=c['lines'][0]<=c['lines'][1]<=n:errors.append('invalid clause')
for gid,g in groups.items():
    for a in g['source_anchors']:anchor_check(a,gid)
for c in src['capabilities']:
    for a in c['source_anchors']:anchor_check(a,c['id'])
    if c['capability_status']=='supported' and not str(c.get('supported_boundary','')).startswith('supported_static'):errors.append('missing static boundary '+c['id'])
    for link in c.get('precise_specification_links',[]):
        if link['group_id'] not in groups:errors.append('cap link '+c['id'])
    if not c.get('precise_specification_links') and c['capability_status']=='supported':errors.append('supported cap without precise receiver '+c['id'])
for f in src['source_files']:
    for link in f['precise_comparison_links']:
        if link['comparison_group_id'] not in groups:errors.append('source inverse link '+f['path'])
required='id title module severity disposition status reviewer category source_baseline specification_baseline source_anchors spec_anchors expected_reference_behavior current_spec_behavior gap preconditions minimal_counterexample normal_case failure_or_boundary_case impact_on_independent_implementation negative_evidence_search proposed_spec_change affected_files shared_contracts acceptance_criteria dependencies related_capabilities related_findings root_cause_group priority batch_owner history_links evidence_level execution_status confidence unknowns excluded_claims user_decision_needed review_resolution'.split()
for f in findings['findings']:
    errors.extend(f['id']+' missing '+k for k in required if k not in f)
    if f['status']!='candidate_pending_independent_counterevidence':errors.append('candidate status '+f['id'])
    if f['review_resolution']['required_revision_signed_off']:errors.append('selfsign '+f['id'])
    if f['acceptance_criteria']['must_execute']:errors.append('unauthorized execution request '+f['id'])
    for a in f['source_anchors']:anchor_check(a,f['id'])
    if f['source_baseline']['commit']!=rv or f['specification_baseline']['commit']!=bv:errors.append('finding baseline '+f['id'])
if prog['reference_execution_count'] or prog['behavior_model_execution_count']:errors.append('unexpected execution')
if prog['not_reviewed']['within_assigned_available_static_scope']:errors.append('remaining owned static scope')
result={'schema_version':'gr5.review.v1','kind':'artifact_integrity_only','reference_or_model_executed':False,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'errors':errors,'passed':not errors,'primary_source_bodies':sum(s['scope_role']=='primary' for s in cov['sources']),'primary_specification_files':len(rev['specifications']),'exact_clause_rows':sum(len(s['clause_mappings']) for s in rev['specifications']),'unique_shared_rule_records':len(ids),'counts_are_not_semantic_or_execution_proof':True}
write('artifact-validation.json',result)
print(json.dumps(result,ensure_ascii=False,indent=2))
if errors:sys.exit(1)
