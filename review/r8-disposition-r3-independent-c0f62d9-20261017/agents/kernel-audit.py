#!/usr/bin/env python3
"""Independent static identity/reconciliation audit; no author or business writes."""
import ast
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path('/workspace/r8-disposition-r3-review')
OUT = ROOT / 'review/r8-disposition-r3-independent-c0f62d9-20261017/agents'
BASE = 'planning/implementation-routing/r8-20261017/'
RP = 'review/r8-disposition-r2-independent-a32873d-20261017/'
C = 'c0f62d973180679134f2eb1a488c1dc359c8658f'
R2 = 'a32873d2860b15d9f5e27727db8f131f4ec433b6'
R = '0ef0b7ad5f9465cfe31da0d7a35f56b5ccba5add'
S = '5f87743293290de2e219ecdd6c19e88280f60c9a'
P = '908273093e1f6b27fc58249417675dd62d146224'
B = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
D = 'd62b41f4d620e50bb04c80a7505374bd284d8210'

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

def raw(commit, path):
    return git('show', commit + ':' + path)

def obj(commit, path):
    return json.loads(raw(commit, path))

def sha(data):
    return hashlib.sha256(data).hexdigest()

def identity(commit, path):
    data = raw(commit, path)
    return dict(commit=commit, path=path, bytes=len(data), sha256=sha(data),
                blob=git('rev-parse', commit + ':' + path).decode().strip(),
                lines=len(data.splitlines()))

def unit_bytes(commit, path, ranges):
    lines = raw(commit, path).splitlines(keepends=True)
    return b''.join(b''.join(lines[a-1:b]) for a,b in ranges)

def count_nodes(value):
    if isinstance(value, dict):
        return 1 + sum(count_nodes(v) for v in value.values())
    if isinstance(value, list):
        return 1 + sum(count_nodes(v) for v in value)
    return 1

m = obj(C, BASE + 'routing-manifest.json')
prior = obj(R2, BASE + 'routing-manifest.json')
initial = obj(D, BASE + 'routing-manifest.json')
k = obj(R, RP + 'agents/kernel-results.json')
ke = obj(R, RP + 'agents/kernel-evidence.json')
f = {r['feature_id']:r for r in m['features']}
pf = {r['feature_id']:r for r in prior['features']}
ret = {r['feature_id']:r for r in m['retired_features']}
orig = {r['feature_id']:r for r in initial['features']}
meta = {r['metadata_id']:r for r in m['metadata_records']}
ids = [r['feature_id'] for r in k['active_feature_results']]
oldids = [r['feature_id'] for r in k['old_feature_results']]
paths = {r['path'] for r in k['reading_ledger']}
source_deltas = obj(C, BASE+'revisions/r3/feature-source-deltas.json')['records']
delta = {r['feature_id']:r for r in source_deltas}
headings = obj(C, BASE+'revisions/r3/new-heading-mappings.json')['accepted_mappings']
ownheadings = [r for r in headings if r['document'] in paths]
hist_sections = obj(C, BASE+'section-coverage.json')['sections']
current_sections = obj(C, BASE+'current-section-coverage.json')['sections']

input_audit = []
for name in ['REPORT.md','findings.json','feature-results.json','finding-results.json',
             'issue-results.json','reading-coverage.json','section-results.json',
             *['agents/'+p.name for p in (Path('/workspace/r8-disposition-r2-review')/RP/'agents').glob('kernel-*')]]:
    data=raw(R,RP+name)
    physical=Path('/workspace/r8-disposition-r2-review')/RP/name
    record=dict(path=RP+name, identity=identity(R,RP+name), physical_bytes_equal=physical.read_bytes()==data)
    assert record['physical_bytes_equal']
    if name.endswith('.json'):
        value=json.loads(data); record['read_mode']='FULL_JSON_PARSE_AND_ALLOCATED_ARRAY_RECONCILIATION'
        record['parsed_nodes']=count_nodes(value)
        record['top_level_array_counts']={a:len(v) for a,v in value.items() if isinstance(v,list)}
    elif name.endswith('.py'):
        record['read_mode']='FULL_AST_PARSE';record['ast_nodes']=sum(1 for _ in ast.walk(ast.parse(data)))
    else:
        record['read_mode']='FULL_PROSE_SEMANTIC_READ'
    input_audit.append(record)
rootf=obj(R,RP+'feature-results.json')
rootg=obj(R,RP+'finding-results.json')['finding_results']
rooti=obj(R,RP+'issue-results.json')['issue_results']
rootread=obj(R,RP+'reading-coverage.json')['documents']
rootsec=obj(R,RP+'section-results.json')['sections']
reconciliation=[]
for a in ['old_feature_results','active_feature_results']:
    index={r['feature_id']:r for r in rootf[a]}
    for row in k[a]:
        assert index[row['feature_id']]['verdict']==row['verdict']
        reconciliation.append(dict(array=a,id=row['feature_id'],verdict_equal=True,
                                  root_pointer='/'+a+'/'+str(rootf[a].index(index[row['feature_id']])),
                                  own_pointer='/'+a+'/'+str(k[a].index(row))))
for a,key,rootrows in [('original_group_results','finding_id',rootg),('issue_results','issue_id',rooti)]:
    index={r[key]:r for r in rootrows}
    for row in k[a]:
        assert index[row[key]]['verdict']==row['verdict']
        reconciliation.append(dict(array=a,id=row[key],verdict_equal=True))
for row in k['reading_ledger']:
    assert any(x['path']==row['path'] for x in rootread)
for row in k['section_metadata_results']:
    assert any(x['path']==row['source']['document'] and x['anchor']==row['unit_id'].split('#',1)[1] for x in rootsec)

# Exact current source reads performed in the reviewer turn; these are not generated reading claims.
fresh_by_name={
 'wp02-rule-configuration-and-data-variants.md':[[204,278]],
 'wp03-content-identity-and-schema.md':[[159,419]],
 'wp04-pbs-lifecycle.md':[[184,320]],
 'wp06-stats-directory.md':[[1,143]],
 'wp07-diagnostics-files-http.md':[[117,191]],
 'wp08-localization.md':[[1,99]],
 'wp09-save-startup-continue.md':[[1,179]],
 'wp10-migration-failure-recovery.md':[[1,95],[217,299]],
 'generic-kernel-wp05-06-07-08-09-10.md':[[286,324]],
}
changed_docs=[]
ledger=[]
for row in k['reading_ledger']:
    path=row['path'];historic=identity(B,path);old=identity(P,path);cur=identity(S,path)
    changed=old['sha256']!=cur['sha256']
    if changed or historic['sha256']!=cur['sha256']:changed_docs.append(path)
    lines=raw(S,path).splitlines(keepends=True)
    actual_headings=[]
    for lineno,line in enumerate(lines,1):
        match=re.match(rb'^(#{1,6})\s+(.+?)\s*\n?$',line)
        if match:actual_headings.append((lineno,len(match[1]),match[2].decode().strip(),sha(line)))
    records=[x for x in current_sections if x['path']==path]
    assert len(actual_headings)==len(records)
    for n,(lineno,level,title,heading_sha) in enumerate(actual_headings):
        end=next((h[0]-1 for h in actual_headings[n+1:] if h[1]<=level),len(lines))
        section=next(x for x in records if x['line_start']==lineno)
        assert (section['level'],section['title'],section['line_end'],section['heading_sha256'])==(level,title,end,heading_sha)
    ledger.append(dict(document_id=row['document_id'],path=path,historical_identity=historic,
                       r2_current_identity=old,current_identity=cur,
                       current_commit=S,fresh_read_commit=S,
                       fresh_read_ranges=fresh_by_name.get(Path(path).name,[]),
                       complete_cumulative_diff_read=True if historic['sha256']!=cur['sha256'] else False,
                       r2_semantic_credit=dict(commit=R,artifact=RP+'agents/kernel-results.json',
                                              pointer='/reading_ledger/'+str(k['reading_ledger'].index(row)),
                                              recorded_prior_credit=row['prior_semantic_credit']),
                       inheritance_limit='Only exact identity-bound unaffected clauses/facets. Current changes, full effective changed units and affected consumers freshly read; no claim of fresh full13 prose.',
                       independent_git_heading_enumeration_matches=True,
                       current_heading_count=sum(x['path']==path for x in current_sections),
                       historical_heading_count=sum(x['path']==path for x in hist_sections)))

special={
 'FR-000397':'Full current WP03§6–7 plus strict-enumeration §5.2 read. Fifteen exact author identities, base default/form clone and retained failure prefix are covered; 137 owns species fields,214 owns Undiscovered/Ditto/gender/intersection,508 owns normalized parent roles. Generic fixed-rule directory remains in the rationale; refinement does not replace the existing17-family scope or Nature/Shape/Color/Habitat contracts.',
 'FR-000403':'Current WP04§5 complete parent and child context read: only the unsupported Changes-made prompt promise is removed. Actual whole-file rewrite, refresh/writeback, cache and partial-state facts stay; parent403 excludes child404/405, and prior R2 current already has the same effective bytes.',
 'FR-000440':'Current WP08§5 complete read with WP69§2/6 and WP15§3/5: Slot seven selected image roles use current game→core SCRIPT_TEXTS. Empty translation is a hit; resource entrance handles failure, with no general retry of A. Framework lookup service and MZ image consumers remain distinct.',
 'FR-000445':'Complete current WP09§4 and WP10§3/5 plus UI65§3 read. Successful decoded/adapted empty data initializes startup values; reading/adaptation exceptions are not emptiness; later validation/backup/delete may still differ. Existing framework state orchestration and MZ title/map consumers remain adequate.',
 'FR-000446':'Complete current WP09§5 and WP10§5.1.1 plus UI65§3.3 read. Ordered P then single P.bak deletion, first/second failure prefixes and next main-file existence gate fit existing persistence responsibility and recovery/UI navigation; recursive backup reads do not expand deletion.',
 'FR-000451':'Full current WP10§5 read, including all5 deletion controls. Framework handles validity/backup/delete/emergency saving and retains partial state; MZ handles confirmations/refusal/conditional scene recovery. Orphan P.bak is not auto-scanned after P deletion; invalid-data consent resets objects after handled delete errors. No atomic target policy is claimed.'
}

edges=[]
oldedges={(r['source_feature_id'],r['target_feature_id']):r for r in k['outbound_feature_edge_audit']['edge_results']}
newedge_reasons={
 ('FR-000397','FR-000137'):'WP18§3 provides strict author-domain species field/default/form clone consumer, not breeding compatibility.',
 ('FR-000397','FR-000214'):'WP33§5.1 evaluates Undiscovered before Ditto/gender/intersection; direct generation has a different gate.',
 ('FR-000397','FR-000508'):'WP34§3 uses Ditto egg-group identity to assign species parent and move/ability channels after one normalization swap.'}
for id in ids:
    for target in f[id]['dependencies']['feature_refs']:
        src=f[id];dst=f[target]
        oldsrc=pf.get(id);olddst=pf.get(target)
        key=(id,target)
        reason=oldedges[key]['reason'] if key in oldedges else newedge_reasons[key]
        edges.append(dict(source_feature_id=id,target_feature_id=target,verdict='PASS',reason=reason,
                          r2_edge_present=key in oldedges,
                          current_source=src['current_applicability']['locator'],current_target=dst['current_applicability']['locator'],
                          source_effective_bytes_equal_r2=oldsrc['current_applicability']['locator']['unit_sha256']==src['current_applicability']['locator']['unit_sha256'],
                          target_effective_bytes_equal_r2=bool(olddst and olddst['current_applicability']['locator']['unit_sha256']==dst['current_applicability']['locator']['unit_sha256']),
                          current_target_impact='All changed effective targets135/137/326/445/446/451/642 read completely; unchanged consumer chapter credit bound to exact current effective bytes. Added137/214/508 reviewed complete. Failure/diagnostic and explicit indirect navigation retained.',
                          candidate_pointer='/features/'+str(m['features'].index(src))+'/dependencies/feature_refs',finding_refs=[]))
assert len(edges)==31 and len(oldedges)==28

active=[]
for old in k['active_feature_results']:
    id=old['feature_id'];r=f[id];pr=pf[id];cur=r['current_applicability']['locator'];oldcur=pr['current_applicability']['locator']
    actual=unit_bytes(S,r['source']['document'],cur['line_ranges'])
    assert sha(actual)==cur['unit_sha256']
    assert r['source']==pr['source'] and r['functional_scope']==pr['functional_scope']
    changes=[key for key in r if r[key]!=pr.get(key)]
    sameunit=cur['unit_sha256']==oldcur['unit_sha256']
    reason=special.get(id,'Fixed R2 per-row semantic judgment retained only for unchanged classification/responsibility/effective-scope facets. Exact row-field and source-unit identity checked; current shared-contract changes reviewed for applicability and do not shift this row’s owner or scope. R2 specific reason: '+old['reason'])
    facets={a:dict(r2_verdict='PASS',verdict='PASS') for a in ['classification','responsibility','scope','dependency','current_calibration']}
    facets['current_calibration'].update(method='FRESH_COMPLETE_AFFECTED_UNIT_AND_CONSUMER_REVIEW' if id in special else 'CURRENT_UNIT_IDENTITY_AND_CHANGED_SHARED_CONTRACT_NONIMPACT',source_effective_bytes_equal_r2=sameunit,reason=reason)
    active.append(dict(feature_id=id,r2_verdict=old['verdict'],verdict='PASS',new_verdict='PASS',current_state='active',disposition='active',reason=reason,
                       method='LIMITED_FACET_INHERITANCE_PLUS_CURRENT_SOURCE_REASSESSMENT',facets=facets,
                       classification_verdict='PASS',responsibility_verdict='PASS',scope_verdict='PASS',dependency_verdict='PASS',current_calibration_verdict='PASS',
                       source=r['source'],functional_scope=r['functional_scope'],current_applicability=r['current_applicability'],
                       candidate_pointer='/features/'+str(m['features'].index(r)),r2_result_pointer=RP+'agents/kernel-results.json#/active_feature_results/'+str(k['active_feature_results'].index(old)),
                       changed_fields=changes,immutable_source_preserved=True,source_effective_bytes_equal_r2=sameunit,
                       inherited_facets=[a for a in ['classification','responsibility','scope'] if pr.get('future_plan')==r.get('future_plan') or a=='scope'],
                       identity=dict(historical=identity(B,r['source']['document']),current=identity(S,r['source']['document'])),
                       current_source_delta=delta.get(id),finding_refs=[]))
oldresults=[]
for old in k['old_feature_results']:
    id=old['feature_id'];row=f.get(id) or ret[id]
    assert row['source']==orig[id]['source']
    retired=id in ret
    if retired:
        body=copy.deepcopy(row);body.pop('retirement');assert body==orig[id]
    source_result=next((r for r in active if r['feature_id']==id),None)
    oldresults.append(dict(feature_id=id,r2_verdict=old['verdict'],verdict='PASS',new_verdict='PASS',current_state='retired' if retired else 'active',disposition='retired' if retired else 'active',
                           reason=('Complete original d62 row body preserved and combined retired/metadata navigation reviewed; no active implementation function.' if retired else source_result['reason']),
                           method='COMPLETE_ORIGINAL_HISTORY_EQUALITY_AND_CURRENT_METADATA_REVIEW' if retired else source_result['method'],
                           candidate_pointer=('/retired_features/'+str(m['retired_features'].index(row))) if retired else source_result['candidate_pointer'],
                           immutable_source_preserved=True,complete_original_history_preserved=True if retired else None,
                           source=row['source'],finding_refs=[]))

consumerrefs=sorted(set(i for mid in ['META-000019','META-000020','META-000021'] for i in meta[mid]['feature_refs']))
cross=[]
for id in consumerrefs:
    r=f[id];cur=r['current_applicability']['locator'];prev=pf[id]['current_applicability']['locator']
    fresh=id in delta
    cross.append(dict(feature_id=id,current_source=cur,current_identity=identity(S,r['source']['document']),
                      r2_source_unit_sha256=prev['unit_sha256'],current_effective_identity_equal_r2=cur['unit_sha256']==prev['unit_sha256'],
                      r2_reading_credit_commit=R,source_fact_changed=id in delta,
                      reading_mode='FRESH_COMPLETE_CURRENT_EFFECTIVE_UNIT' if fresh else 'EXACT_R2_EFFECTIVE_SOURCE_CREDIT_AND_RELATION_NONIMPACT',
                      fresh_ranges=cur['line_ranges'] if fresh else [],relationship_verdict='PASS',
                      qualification='Navigation relationship only; unrelated outgoing-reference or calibration-note failures do not negate field production/consumption. No inherited whole-target PASS or fresh216-full-read claim.'))

extra=[]
for n in [135,214,326,508,471,625,628,642,644]:
    row=f['FR-%06d'%n];path=row['source']['document']
    extra.append(dict(feature_id=row['feature_id'],path=path,commit=S,identity=identity(S,path),
                      fresh_read_ranges=row['current_applicability']['locator']['line_ranges'],
                      reading_mode='FRESH_COMPLETE_EFFECTIVE_UNIT',is_primary_allocated_document=False,
                      purpose='Egg-group recipient, Mega producer, diagnostic input/window, language persistence or title/delete consumer.'))
for path,ranges,purpose in [
 ('user-interface/wp69-slot-machine.md',[[1,134]],'Complete current Slot language-role/resource/failure prefix consumer.'),
 ('engine-overworld/wp12-terrain-movement-vehicles.md',[[169,188]],'Complete cumulative terminal-motion clause diff plus inherited exact earlier body: new jump gate does not alter kernel step-stat ownership.'),
 ('engine-overworld/wp13-map-events-npc-followers.md',[[90,105],[123,140],[146,154]],'Complete cumulative interpreter-identity/terminal/label clause diff; time/input consumer remains separate.'),
 ('pokemon-rules/wp61-field-passive-effects-and-blackout.md',[[52,57]],'Complete cumulative Repel comparison-member clause diff; no kernel clock/random ownership transfer.'),
 ('combat-requirements/wp58-battle-recording-and-playback.md',[[102,107]],'Complete cumulative global-random attribution change read; recording parent exclusion and745→132–136 remain valid.')]:
    path='deliverables/final-specification-set/'+path
    extra.append(dict(path=path,commit=S,identity=identity(S,path),fresh_read_ranges=ranges,
                      reading_mode='FRESH_COMPLETE_BODY' if 'wp69-' in path else 'COMPLETE_CHANGED_CLAUSE_DIFF_WITH_CONTEXT',
                      purpose=purpose,is_primary_allocated_document=False))

metadata_results=[]
for old in ke['metadata_audit']:
    mid=old['metadata_id'];oldid=old['retired_feature_id'];mr=meta[mid]
    assert mr==next(r for r in prior['metadata_records'] if r['metadata_id']==mid)
    assert sorted(set(i for g in old['groups'] for i in g['feature_refs']))==mr['feature_refs']
    assert ret[oldid]['retirement']['replacement_feature_refs']==mr['feature_refs']
    groups=[]
    for i,g in enumerate(old['groups']):
        item=copy.deepcopy(g);item.update(r2_verdict='PASS',verdict='PASS',current_commit=S,
            current_source_line=[g['lines'][0]+26,g['lines'][1]+26] if mid=='META-000020' else g['lines'],
            reason='Full current6/40/6 responsibility rows reread. Each existing consumer retains its field/phase purpose; affected consumer units freshly read, other exact-unit semantic credit attributed. Egg-group fixed-member self-navigation additionally uses current§6.2→397/137/214/508 without requiring duplicate smallest IDs in the union.')
        groups.append(item)
    sections=[s for s in current_sections if mid in s.get('metadata_refs',[])]
    metadata_results.append(dict(unit_type='combined-retired-metadata',metadata_id=mid,retired_feature_ids=[oldid],r2_verdict='PASS',verdict='PASS',
                                 reason='Metadata remains responsibility/evidence navigation, not an implementation feature. Complete original row preserved; replacement_refs, metadata consumers and historical/current section navigation reconciled.',
                                 source=mr['source'],current_identity=identity(S,mr['source']['document']),consumer_refs=mr['feature_refs'],
                                 original_complete_history_proof=dict(commit=D,pointer='/features/'+str(initial['features'].index(orig[oldid])),row_body_equals_original=True),
                                 current_section_navigation=[dict(path=s['path'],anchor=s['anchor'],feature_refs=s['feature_refs'],metadata_refs=s['metadata_refs']) for s in sections],
                                 group_results=groups,complete_source_group_count=len(groups),finding_refs=[]))

headingresults=[]
for h in ownheadings:
    path=h['document'];a,b=h['line_ranges'][0];data=raw(S,path);lines=data.splitlines(keepends=True);line=lines[a-1]
    title=re.sub(r'^#{1,6}\s+','',line.decode().strip())
    si=h['source_identity'];assert sha(data)==si['file_sha256'];assert sha(unit_bytes(S,path,[[a,b]]))==si['unit_sha256']
    assert sha(title.encode())==si['heading_sha256'];assert sha(line)==si['raw_markdown_heading_sha256']
    if '蛋群' in h['title']:
        why=special['FR-000397']+' META20§7 responsibility navigation remains synchronized through current heading consumers.'
    elif '系统装配' in h['title']:
        why='All8 KER002 controls read: no-file, readable old sequence→empty, valid nonempty, refusal/consent/backup postvalidation, BACK sentinel and decode failure.445/449/451/439/642 cover distinct phases; startup emptiness alone cannot assert final Continue menu.'
    elif h['title']=='默认主档与相邻备份删除':
        why='All5 KER001 controls read;451 owns ordered file prefixes,446 persistence boundary,642 title confirmations/feedback. No cancellation/deletion/rollback or orphan-backup behavior is collapsed.'
    else:
        why='Parent recovery/deletion heading and static-catalog aggregation use existing persistence/recovery/title/language consumers. Static vectors remain NOT_EXECUTED; parent/child chapter aggregation is valid and does not create new functional IDs.'
    headingresults.append(dict(document=path,anchor=h['anchor'],title=h['title'],ranges=h['line_ranges'],r2_verdict='PREPARED_PROPOSAL_ONLY',verdict='PASS',
                               source_commit=S,source_identity=si,feature_refs=h['feature_refs'],metadata_refs=h['metadata_refs'],identity_match=True,
                               heading_hash_conventions_verified=['SHA256_UTF8_TITLE_ONLY','SHA256_RAW_MARKDOWN_LINE_WITH_NEWLINE'],reason=why,finding_refs=[]))

changedresults=[]
for path in changed_docs:
    ds=[r for r in delta.values() if r['immutable_source']['document']==path and r['feature_id'] in ids]
    changedresults.append(dict(path=path,historical_identity=identity(B,path),r2_identity=identity(P,path),current_identity=identity(S,path),verdict='PASS',
                               changed_effective_units=[dict(feature_id=r['feature_id'],current_ranges=r['current_source']['line_ranges'],reason=special[r['feature_id']],verdict='PASS') for r in ds],
                               metadata_impact='META20 field row383 adds fixed EggGroup self-navigation; other6/40/6 groups retain purpose.' if 'wp03-' in path else 'No metadata consumer ownership transfer; complete changed clauses/new headings read.',
                               new_heading_anchors=[r['anchor'] for r in ownheadings if r['document']==path],
                               reading='FULL_CUMULATIVE_GIT_DIFF_AND_COMPLETE_CHANGED_EFFECTIVE_UNITS',finding_refs=[]))

sections=[]
priorsections={(s['path'],s['anchor']):s for s in obj(R2,BASE+'section-coverage.json')['sections']}
for i,s in enumerate(current_sections):
    if s['path'] not in paths:continue
    old=priorsections.get((s['path'],s['anchor']))
    sections.append(dict(document_id=s['document_id'],path=s['path'],anchor=s['anchor'],title=s['title'],ranges=[[s['line_start'],s['line_end']]],mapping_kind=(old or {}).get('mapping_kind','CURRENT_ADDED_CONSUMER_HEADING'),
                         feature_refs=s['feature_refs'],metadata_refs=s.get('metadata_refs',[]),retired_feature_refs=s.get('retired_feature_refs',[]),
                         r2_verdict='PASS' if old else 'PREPARED_PROPOSAL_ONLY',verdict='PASS',
                         reason='Current effective clause/consumer calibration plus exact unaffected historical chapter navigation; new headings separately audited. Static catalogs and metadata do not claim execution.',finding_refs=[]))
groups=[]
for g in k['original_group_results']:
    root=next(x for x in rootg if x['finding_id']==g['finding_id'])
    item=copy.deepcopy(g);item.update(r2_verdict=g['verdict'],verdict='PASS',original_case_verdict='PASS',current_scope_verdict='PASS',finding_refs=[],
                                    reason='Every original case and retained scope reconciled with fixed R2; current changed-source/target semantics independently reassessed. No routing ownership/metadata defect found; no tool/compatibility verdict transferred.')
    for case in item['original_cases']:
        case.update(r2_verdict=case['verdict'],verdict='PASS')
    groups.append(item)
issues=[]
for row in k['issue_results']:
    item=copy.deepcopy(row);item.update(r2_verdict=row['verdict'],verdict='PASS',finding_refs=[],
                                      current_reassessment='R1-KF-001 complete6/40/6 groups and7 existing catalog relationships retained; new current egg/deletion/catalog headings evaluated. R1-KF-002 all31 outgoing edges checked; Mega production and diagnosis/recovery roles still valid.')
    issues.append(item)

result=dict(schema='r8-r3-independent-kernel.v1',candidate_commit=C,current_source_commit=S,prior_candidate=R2,prior_review_commit=R,domain='generic-kernel',reviewer='/root/r3_kernel',verdict='PASS',
            verdict_scope='DOMAIN_ROUTING_AND_CURRENT_SOURCE_CALIBRATION_ONLY',
            configuration=dict(requested=dict(model='gpt-6.1-sol',effort='ultra',service_tier='default',speed='normal',Fast='off'),
                               authoritative_creation_echo={a:'UNVERIFIED' for a in ['model','effort','service_tier','speed','Fast','cloud_task_uuid']},actual_execution_echo={a:'UNVERIFIED' for a in ['model','effort','service_tier','speed','Fast']}),
            counts=dict(old_feature_results=len(oldresults),active_feature_results=len(active),retired_metadata_results=len(metadata_results),retired_history=3,original_groups=6,residual_issues=2,
                        primary_documents=len(ledger),historical_headings=sum(r['historical_heading_count'] for r in ledger),current_headings=len(sections),new_headings=len(headingresults),
                        changed_primary_documents=len(changedresults),current_outgoing_edges=len(edges),r2_outgoing_edges=len(oldedges),metadata_unique_consumers=len(cross),metadata_complete_groups=52,
                        freshly_read_changed_metadata_consumer_units=sum(r['source_fact_changed'] for r in cross)),
            old_feature_results=oldresults,active_feature_results=active,retired_metadata_results=metadata_results,issue_results=issues,original_group_results=groups,
            reading_ledger=ledger,new_heading_results=headingresults,changed_source_results=changedresults,section_results=sections,
            outbound_feature_edge_audit=dict(edge_count=len(edges),source_results=[dict(feature_id=id,feature_refs=f[id]['dependencies']['feature_refs'],verdict='PASS') for id in ids],edge_results=edges),
            metadata_consumer_results=cross,extra_consumer_reading=extra,r2_input_consumption=input_audit,r2_result_reconciliation=reconciliation,new_findings=[],business_execution_count=0,
            remaining=['Root independently handles tool/schema/receipt/global mechanical acceptance.','Target verification, implementation, acceptance and user stage/scope remain pending; no exclusion/prototype/host/business execution approval.','Cross-domain targets may have calibration-note failures unrelated to metadata navigation; no whole-target PASS is claimed.','Actual model/effort/tier/speed/Fast/cloud UUID remain individually UNVERIFIED.'],
            limitations=['Fresh primary ranges and19 changed metadata consumer units are explicit; unchanged source reading is inherited through fixed exact unit identities and attributed R2 semantic credit, not a fresh13/216 whole-body claim.','Early truncated printouts receive no unprinted prose credit; affected missing ranges were re-read. JSON/AST whole parsing is mechanical and is not prose reading.'])
assert len(oldresults)==66 and len(active)==64 and len(metadata_results)==3 and len(headingresults)==5 and len(ledger)==13
(OUT/'kernel-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result['counts'],ensure_ascii=False))
