#!/usr/bin/env python3
"""Independent document/JSON/Git audit only. Never execute author or business code."""
import collections, datetime, hashlib, json, re, subprocess
from pathlib import Path

C = 'a32873d2860b15d9f5e27727db8f131f4ec433b6'
R1C = '5666b7b912e2fb79b5119283ee6a37401a7071db'
R1 = '8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8'
ORIG = 'd62b41f4d620e50bb04c80a7505374bd284d8210'
B = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
P = '908273093e1f6b27fc58249417675dd62d146224'
BASE = 'planning/implementation-routing/r8-20261017/'
RP = 'review/r8-disposition-r1-independent-5666b7b-20261017/'
OUT = Path('review/r8-disposition-r2-independent-a32873d-20261017/agents')
commands = []
cache = {}
def sha(b): return hashlib.sha256(b).hexdigest()
def git(*args):
    r = subprocess.run(['git', *args], capture_output=True)
    commands.append({'argv': ['git', *args], 'exit_code': r.returncode,
                     'stdout_bytes': len(r.stdout), 'stdout_sha256': sha(r.stdout),
                     'stderr': r.stderr.decode()})
    r.check_returncode()
    return r.stdout
def blob(c, p):
    if (c,p) not in cache: cache[c,p] = git('show', c+':'+p)
    return cache[c,p]
def obj(c,p): return json.loads(blob(c,p))
def write(name, data):
    (OUT/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

m = obj(C, BASE+'routing-manifest.json')
r1m = obj(R1C, BASE+'routing-manifest.json')
orig = obj(ORIG, BASE+'routing-manifest.json')
k = obj(R1, RP+'agents/kernel-results.json')
ids = [r['feature_id'] for r in k['old_feature_results']]
f = {r['feature_id']: r for r in m['features']}
ret = {r['feature_id']: r for r in m['retired_features']}
prior = {r['feature_id']: r for r in r1m['features']+r1m['retired_features']}
initial = {r['feature_id']: r for r in orig['features']}
meta = {r['metadata_id']: r for r in m['metadata_records']}
prior_meta = {r['metadata_id']: r for r in r1m['metadata_records']}
active = [r for r in m['features'] if '/generic-kernel/' in r['source']['document']]
sections = obj(C, BASE+'section-coverage.json')['sections']
prior_sections = obj(R1C, BASE+'section-coverage.json')['sections']
paths = {r['path'] for r in k['reading_ledger']}

# Entire fixed JSON artifacts are parsed and all allocated representations reconciled.
inputs = []
parsed = {}
for name in ['REPORT.md','REVIEW-CONTRACT.md','findings.json','finding-results.json',
             'feature-results.json','reading-coverage.json','agents/kernel-report.md',
             'agents/kernel-results.json']:
    b = blob(R1, RP+name)
    disk = Path('/workspace/r8-disposition-r1-review')/RP/name
    rec = {'path': RP+name, 'commit': R1, 'bytes': len(b), 'sha256': sha(b),
           'physical_prior_tree_equals_git': disk.read_bytes()==b,
           'method': 'FULL_TEXT_READ' if name.endswith('.md') else 'FULL_JSON_PARSE_AND_ALLOCATED_STRUCTURAL_RECONCILIATION'}
    if name.endswith('.json'): parsed[name] = json.loads(b)
    inputs.append(rec)
root_features = parsed['feature-results.json']
reconciled = {}
for key in ['old_feature_results','active_feature_results']:
    root = {r['feature_id']:r for r in root_features[key]}
    reconciled[key] = [{'feature_id': r['feature_id'],
                        'verdict_equal': root[r['feature_id']]['verdict']==r['verdict'],
                        'reason_equal': root[r['feature_id']]['reason']==r['reason']}
                       for r in k[key]]
root_meta = {r['metadata_id']:r for r in root_features['retired_metadata_results']}
reconciled['metadata'] = [{'metadata_id': r['unit_id'],
                          'verdict_equal': root_meta[r['unit_id']]['verdict']==r['verdict'],
                          'source_equal': root_meta[r['unit_id']]['source']==r['source']}
                         for r in k['retired_metadata_results'] if r['unit_type']=='metadata_record']
root_groups = {r['finding_id']:r for r in parsed['finding-results.json']['finding_results']}
reconciled['groups'] = [{'finding_id':r['finding_id'], 'verdict_equal':root_groups[r['finding_id']]['verdict']==r['verdict']}
                        for r in k['finding_results']]
root_findings = parsed['findings.json']['findings']
assert {x.get('finding_id',x['id']) for x in root_findings if x.get('finding_id',x['id']).startswith('R1-KF-')} == {'R1-KF-001','R1-KF-002'}

fresh = {
 'wp02-rule-configuration-and-data-variants.md': [[204,278]],
 'wp03-content-identity-and-schema.md': [[313,393]],
 'wp04-pbs-lifecycle.md': [[184,320]],
 'wp05-events-extensions-plugins.md': [[109,147]],
 'wp06-stats-directory.md': [[70,143]],
 'wp06-time-random-steps-stats.md': [],
 'wp07-deprecation-appendix.md': [[35,54]],
 'wp07-diagnostics-files-http.md': [[117,191]],
 'wp08-localization.md': [[24,199]],
 'wp09-save-startup-continue.md': [[23,119],[121,179]],
 'wp10-migration-failure-recovery.md': [[217,281]],
 'generic-kernel-wp02-03-04.md': [[1,236]],
 'generic-kernel-wp05-06-07-08-09-10.md': [[1,288]],
}
ledger = []
for old in k['reading_ledger']:
    p=old['path']; bb=blob(B,p); cur=blob(P,p)
    name=p.split('/')[-1]
    ledger.append({'document_id':old['document_id'],'path':p,'historical_commit':B,
                   'historical_blob':git('rev-parse',B+':'+p).decode().strip(),
                   'historical_bytes':len(bb),'historical_sha256':sha(bb),
                   'current_commit':P,'current_blob':git('rev-parse',P+':'+p).decode().strip(),
                   'current_bytes':len(cur),'current_sha256':sha(cur),'lines':len(cur.splitlines()),
                   'candidate_worktree_is_historical':Path(p).read_bytes()==bb and blob(C,p)==bb,
                   'r1_current_identity_equal':old['current_sha256']==sha(cur),
                   'r1_historical_identity_equal':old['historical_sha256']==sha(bb),
                   'fresh_read_commit':P,'fresh_read_ranges':fresh[name],
                   'prior_semantic_credit':{'commit':R1,'artifact':RP+'agents/kernel-results.json',
                       'pointer':'/reading_ledger/'+str(k['reading_ledger'].index(old)),
                       'r1_fresh_ranges':old['new_read_ranges'],
                       'r1_inherited_full_source_credit':old['source_full_read_credit_inherited_from']},
                   'inheritance_basis':'Exact current and historical file identity with fixed independent R1; unchanged PASS row fields are exact-equal. R2 affected complete tables/chapters reread separately; no all-text fresh claim.'})

rows=[];locators=[]
for id in ids:
    r=f.get(id) or ret[id]
    changed=sorted(x for x in set(r)|set(prior[id]) if r.get(x)!=prior[id].get(x))
    rows.append({'feature_id':id,'active':id in f,'retired':id in ret,
                 'disposition_unique':int(id in f)+int(id in ret)==1,
                 'changed_top_fields':changed,'r1_record_equal':r==prior[id],
                 'immutable_source_equal_original':r['source']==initial[id]['source'],
                 'retired_body_equal_original':{a:b for a,b in r.items() if a!='retirement'}==initial[id] if id in ret else None})
for r in active:
    cur=r['current_applicability'];loc=cur['locator'];b=blob(cur['snapshot_commit'],cur['document']);ls=b.splitlines(keepends=True)
    unit=b''.join(b''.join(ls[a-1:z]) for a,z in loc['line_ranges'])
    locators.append({'feature_id':r['feature_id'],'snapshot_commit':cur['snapshot_commit'],
                     'file_sha_equal':sha(b)==loc['file_sha256'],
                     'file_blob_equal':git('rev-parse',cur['snapshot_commit']+':'+cur['document']).decode().strip()==loc['file_git_blob'],
                     'unit_sha_equal':sha(unit)==loc['unit_sha256'],
                     'heading_sha_equal':sha(ls[loc['line_ranges'][0][0]-1])==loc['heading_sha256'],
                     'applicability_status':cur['status'],'upstream':r['upstream'],
                     'destination_verification':r['destination_verification']['status'],
                     'implementation_status':r['implementation']['status'],
                     'acceptance_status':r['implementation']['acceptance_status']})
scope_overlaps=[]
for i,r in enumerate(active):
    for s in active[i+1:]:
        if r['source']['document']!=s['source']['document']:continue
        for a,b in r['functional_scope']['line_ranges']:
            for x,y in s['functional_scope']['line_ranges']:
                if max(a,x)<=min(b,y):scope_overlaps.append([r['feature_id'],s['feature_id'],max(a,x),min(b,y)])
section_diffs=[]
for i,r in enumerate(sections):
    if r['path'] in paths:
        delta={a:{'r1':prior_sections[i].get(a),'r2':r.get(a)} for a in set(r)|set(prior_sections[i]) if r.get(a)!=prior_sections[i].get(a)}
        if delta:section_diffs.append({'pointer':'/sections/'+str(i),'document_id':r['document_id'],'title':r['title'],'delta':delta})
metadata_audit=[]
mapping=obj(C,BASE+'revisions/r2/consumer-mappings.json')
for id,old_id in [('META-000019','FR-000392'),('META-000020','FR-000398'),('META-000021','FR-000407')]:
    r=meta[id];groups=[x for x in mapping['relationships'] if x.get('metadata_id')==id]
    union=sorted(set().union(*(set(x['feature_refs']) for x in groups)))
    source_sections=[(i,s) for i,s in enumerate(sections) if id in s['metadata_refs']]
    metadata_audit.append({'metadata_id':id,'retired_feature_id':old_id,'source_equal_r1':r['source']==prior_meta[id]['source'],
          'group_count':len(groups),'groups':groups,'group_union_equals_metadata_refs':union==r['feature_refs'],
          'retirement_refs_equal_metadata':ret[old_id]['retirement']['replacement_feature_refs']==r['feature_refs'],
          'section_propagation':[{'pointer':'/sections/'+str(i),'feature_refs_equal_metadata':s['feature_refs']==r['feature_refs'],'retired_feature_refs':s['retired_feature_refs']} for i,s in source_sections]})
summary={'old_count':len(ids),'active_count':len(active),'retired_count':len(set(ids)&ret.keys()),
         'metadata_count':len(metadata_audit),'r1_old_pass_exact_row_count':sum(r['r1_record_equal'] for r in rows if next(x for x in k['old_feature_results'] if x['feature_id']==r['feature_id'])['verdict']=='PASS'),
         'r1_active_pass_exact_row_count':sum(f[r['feature_id']]==prior[r['feature_id']] for r in k['active_feature_results'] if r['verdict']=='PASS'),
         'changed_old_rows':[x['feature_id'] for x in rows if x['changed_top_fields']],
         'all_immutable_sources_preserved':all(r['immutable_source_equal_original'] for r in rows),
         'all_retired_complete_bodies_preserved':all(r['retired_body_equal_original'] for r in rows if r['retired']),
         'all_locators_valid':all(all(v for k,v in r.items() if k.endswith('_equal')) for r in locators),
         'active_scopes_disjoint':not scope_overlaps,'primary_documents':len(ledger),
         'headings':sum(1 for r in sections if r['path'] in paths),
         'mapping_counts':dict(collections.Counter(r['mapping_kind'] for r in sections if r['path'] in paths)),
         'changed_sections':len(section_diffs),
         'metadata_navigation_consistent':all(r['group_union_equals_metadata_refs'] and r['retirement_refs_equal_metadata'] and all(s['feature_refs_equal_metadata'] for s in r['section_propagation']) for r in metadata_audit),
         'accepted_u02_active_ids':[x['feature_id'] for x in locators if 'R8-U02-ACCEPTED-861f7a44' in x['upstream']['accepted_events']]}
write('kernel-evidence.json',{'candidate':C,'prior_candidate':R1C,'prior_review':R1,'current_payload':P,
 'fixed_input_identities':inputs,'r1_full_json_structural_reconciliation':reconciled,
 'reading_ledger':ledger,'old_row_identity':rows,'active_locators':locators,'scope_overlaps':scope_overlaps,
 'metadata_audit':metadata_audit,'section_diffs':section_diffs,'summary':summary,
 'commands':commands,'business_execution_count':0,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
print(json.dumps(summary,ensure_ascii=False,indent=2))
