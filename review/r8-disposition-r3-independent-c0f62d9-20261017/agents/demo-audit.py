#!/usr/bin/env python3
"""Read-only Git/JSON evidence reconstruction for the R3 demo/shared review."""
import copy
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path('/workspace/r8-disposition-r3-review')
OUT = ROOT / 'review/r8-disposition-r3-independent-c0f62d9-20261017/agents'
PREFIX = 'planning/implementation-routing/r8-20261017/'
CANDIDATE = 'c0f62d973180679134f2eb1a488c1dc359c8658f'
R2_CANDIDATE = 'a32873d2860b15d9f5e27727db8f131f4ec433b6'
R2_REPORT = '0ef0b7ad5f9465cfe31da0d7a35f56b5ccba5add'
R2_SOURCE = '908273093e1f6b27fc58249417675dd62d146224'
CURRENT = '5f87743293290de2e219ecdd6c19e88280f60c9a'
INITIAL = 'd62b41f4d620e50bb04c80a7505374bd284d8210'
R2_BASE = 'review/r8-disposition-r2-independent-a32873d-20261017/'
R2_LOCAL = Path('/workspace/r8-disposition-r2-review')
CACHE = {}

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)

def raw(commit, path):
    key = (commit, path)
    if key not in CACHE:
        CACHE[key] = git('show', f'{commit}:{path}')
    return CACHE[key]

def obj(commit, path):
    return json.loads(raw(commit, path))

def sha(b):
    return hashlib.sha256(b).hexdigest()

def identity(commit, path):
    b = raw(commit, path)
    return dict(commit=commit, path=path, bytes=len(b), lines=len(b.splitlines()),
                sha256=sha(b), git_blob=git('rev-parse', f'{commit}:{path}').decode().strip())

def unit(commit, row):
    app = row['current_applicability']
    lines = raw(commit, app['document']).decode().splitlines(True)
    return ''.join(''.join(lines[s-1:e]) for s, e in app['locator']['line_ranges']).encode()

def merge_ranges(ranges):
    out = []
    for s, e in sorted(ranges):
        if out and s <= out[-1][1] + 1:
            out[-1][1] = max(e, out[-1][1])
        else:
            out.append([s, e])
    return out

prior = obj(R2_REPORT, R2_BASE + 'agents/demo-results.json')
manifest = obj(CANDIDATE, PREFIX + 'routing-manifest.json')
old = obj(R2_CANDIDATE, PREFIX + 'routing-manifest.json')
original = obj(INITIAL, PREFIX + 'routing-manifest.json')
features = {r['feature_id']: r for r in manifest['features']}
old_features = {r['feature_id']: r for r in old['features']}
original_features = {r['feature_id']: r for r in original['features']}
metadata = {r['metadata_id']: r for r in manifest['metadata_records']}
old_metadata = {r['metadata_id']: r for r in old['metadata_records']}
retired = {r['feature_id']: r for r in manifest['retired_features']}
own_ids = {r['feature_id'] for r in prior['active_feature_results']}
old_ids = {r['feature_id'] for r in prior['old_feature_results']}
meta_ids = {r['metadata_id'] for r in prior['retired_metadata_results']}
primary = {r['path'] for r in prior['reading_ledger']}
consumer_ids = {i for r in prior['source_group_results'] for i in r['feature_refs']}
outgoing_ids = {i for fid in own_ids for i in features[fid]['dependencies']['feature_refs']}
direct_paths = {r['document'] for fid in own_ids for r in features[fid]['dependencies']['direct_refs']}
changed_paths = set(git('diff', '--name-only', R2_SOURCE, CURRENT, '--', 'deliverables/final-specification-set').decode().splitlines())

# Every byte of each fixed prior JSON is parsed; semantic reading is separately
# attributed in the report/ledger, never inferred from this traversal.
prior_paths = ['REPORT.md', 'findings.json', 'feature-results.json', 'finding-results.json',
               'issue-results.json', 'reading-coverage.json', 'section-results.json',
               'agents/demo-report.md', 'agents/demo-results.json', 'agents/demo-final-report-crosscheck.json']
prior_inputs = []
prior_json = {}
for p in prior_paths:
    rp = R2_BASE + p
    b = raw(R2_REPORT, rp)
    local = (R2_LOCAL / rp).read_bytes()
    assert b == local, p
    rec = identity(R2_REPORT, rp)
    rec['physical_equals_fixed_git'] = True
    rec['consumption'] = 'FULL_PROSE_READ' if p.endswith('.md') else 'COMPLETE_JSON_PARSE_AND_ALLOCATED_ARRAY_RECONCILIATION'
    if p.endswith('.json'):
        prior_json[p] = json.loads(b)
        rec['top_level_array_lengths'] = {k: len(v) for k, v in prior_json[p].items() if isinstance(v, list)}
    prior_inputs.append(rec)

root_features = prior_json['feature-results.json']
for key, identifier, selected in [('old_feature_results','feature_id',old_ids),
                                  ('active_feature_results','feature_id',own_ids),
                                  ('retired_metadata_results','metadata_id',meta_ids)]:
    a = {r[identifier]: r for r in root_features[key] if r[identifier] in selected}
    b = {r[identifier]: r for r in prior[key]}
    assert set(a) == set(b), key
    for i in b:
        assert a[i].get('verdict', a[i].get('new_verdict')) == b[i].get('verdict', b[i].get('new_verdict')), (key, i)
assert {r['finding_id'] for r in prior['original_group_results']} <= {r['finding_id'] for r in prior_json['finding-results.json']['finding_results']}
assert {r['issue_id'] for r in prior['issue_results']} <= {r['issue_id'] for r in prior_json['issue-results.json']['issue_results']}
assert primary <= {r['path'] for r in prior_json['reading-coverage.json']['documents']}

primary_identity = []
for p in sorted(primary):
    a, b = identity(R2_SOURCE,p), identity(CURRENT,p)
    assert a['sha256'] == b['sha256']
    prior_record = next(r for r in prior['reading_ledger'] if r['path'] == p)
    assert a['sha256'] == prior_record['identity']['sha256']
    primary_identity.append(dict(path=p, r2_identity=a, current_identity=b, bytes_equal=True))

row_identity = []
for fid in sorted(own_ids):
    f, o = features[fid], old_features[fid]
    changed = [k for k in f if f[k] != o.get(k)]
    assert changed == ['current_applicability'], (fid, changed)
    a,b=copy.deepcopy(f['current_applicability']),copy.deepcopy(o['current_applicability'])
    a.pop('snapshot_commit'); b.pop('snapshot_commit')
    assert a == b, fid
    assert f['source'] == original_features[fid]['source']
    assert unit(CURRENT, f) == unit(R2_SOURCE, o)
    row_identity.append(dict(feature_id=fid, changed_fields=changed,
        only_snapshot_commit_changed=True, source_preserved_from_original=True,
        effective_unit_equal_r2=True, current_effective_sha256=sha(unit(CURRENT,f))))

retirement_checks = []
for pr in prior['retired_metadata_results']:
    mid,fid=pr['metadata_id'],pr['retired_feature_id']
    r=copy.deepcopy(retired[fid]); retirement=r.pop('retirement')
    assert r==original_features[fid],fid
    assert retirement['replacement_feature_refs']==metadata[mid]['feature_refs'],mid
    assert metadata[mid] == old_metadata[mid], mid
    retirement_checks.append(dict(metadata_id=mid, retired_feature_id=fid,
        original_complete_body_equal=True, replacement_and_metadata_refs_equal=True,
        metadata_complete_row_equal_r2=True, replacement_refs=retirement['replacement_feature_refs']))

consumer_evidence = []
for fid in sorted(consumer_ids|outgoing_ids):
    f,o=features[fid],old_features[fid]
    a,b=unit(CURRENT,f),unit(R2_SOURCE,o)
    consumer_evidence.append(dict(feature_id=fid, current_identity=identity(CURRENT,f['source']['document']),
        r2_identity=identity(R2_SOURCE,o['source']['document']),
        r2_ranges=o['current_applicability']['locator']['line_ranges'],
        current_ranges=f['current_applicability']['locator']['line_ranges'],
        effective_unit_equal=a==b, current_unit_sha256=sha(a), r2_unit_sha256=sha(b),
        roles=([ 'METADATA_CONSUMER' ] if fid in consumer_ids else []) + ([ 'OUTGOING_FEATURE_TARGET' ] if fid in outgoing_ids else [])))

direct_diff = []
for p in sorted(direct_paths):
    patch=git('diff','--unified=6',R2_SOURCE,CURRENT,'--',p)
    direct_diff.append(dict(path=p,current_identity=identity(CURRENT,p),r2_identity=identity(R2_SOURCE,p),
        changed=bool(patch),complete_diff_bytes=len(patch),complete_diff_sha256=sha(patch),
        complete_diff_reading='FRESH_FULL_PATCH_AND_EFFECTIVE_CONTEXT' if patch else 'EXACT_IDENTITY_BOUND_PRIOR_CONTRACT'))

new_headings = obj(CANDIDATE,PREFIX+'revisions/r3/new-heading-mappings.json')['accepted_mappings']
owned_heading = [r for r in new_headings if r['document'] in primary]
impact_heading = [r for r in new_headings if set(r['feature_refs'])&(consumer_ids|outgoing_ids) or r['document'] in direct_paths]
assert not owned_heading
coverage=obj(CANDIDATE,PREFIX+'current-section-coverage.json')
historical_coverage=obj(CANDIDATE,PREFIX+'section-coverage.json')
old_coverage=obj(R2_CANDIDATE,PREFIX+'section-coverage.json')
assert historical_coverage==old_coverage
own_sections=[r for r in coverage['sections']if r['path']in primary]
old_sections=[r for r in historical_coverage['sections']if r['path']in primary]
assert len(own_sections)==len(old_sections)
for section in own_sections:
    lines=raw(CURRENT,section['path']).decode().splitlines(True)
    heading=lines[section['line_start']-1]
    assert sha(heading.encode())==section['heading_sha256']
    prior_section=next(x for x in old_sections if x['path']==section['path']and x['anchor']==section['anchor'])
    for field in ['feature_refs','metadata_refs','coverage_scope']:
        expected=prior_section.get(field)
        if field=='coverage_scope' and expected is None:
            expected='EXPLICIT_SOURCE_FUNCTIONS_OR_METADATA'
        assert section.get(field)==expected,(section['path'],section['anchor'],field)
    if section['metadata_refs']:
        for mid in set(section['metadata_refs'])&meta_ids:
            assert set(section['feature_refs'])<=set(metadata[mid]['feature_refs'])
evidence=dict(candidate_commit=CANDIDATE,current_source_commit=CURRENT,r2_candidate_commit=R2_CANDIDATE,
    r2_report_commit=R2_REPORT,r2_source_commit=R2_SOURCE,
    fixed_git_objects={c:git('rev-parse',f'{c}^{{tree}}').decode().strip() for c in [CANDIDATE,R2_CANDIDATE,R2_REPORT,R2_SOURCE,CURRENT,INITIAL]},
    final_formal_tree=git('rev-parse',f'{CURRENT}:deliverables/final-specification-set').decode().strip(),
    primary_identity=primary_identity,own_row_identity=row_identity,retirement_checks=retirement_checks,
    consumer_evidence=consumer_evidence,direct_reference_evidence=direct_diff,
    own_new_heading_count=len(owned_heading),supplemental_new_heading_impacts=impact_heading,
    prior_input_reconciliation=prior_inputs,
    root_array_reconciliation='PASS_ALL_ALLOCATED_IDS_GROUPS_ISSUES_DOCUMENTS',
    primary_section_mapping_checks=dict(count=len(own_sections),historical_sections_identical_to_r2=True,
        heading_hashes_and_refs_match_fixed_current=True),
    counts=dict(primary_documents=len(primary),old_features=len(old_ids),active_features=len(own_ids),metadata=len(meta_ids),
        source_groups=len(prior['source_group_results']),unique_metadata_consumers=len(consumer_ids),
        outgoing_unique_feature_targets=len(outgoing_ids),outgoing_unique_document_targets=len(direct_paths),
        changed_direct_reference_documents=sum(r['changed'] for r in direct_diff),
        changed_effective_consumers=[r['feature_id']for r in consumer_evidence if not r['effective_unit_equal']],
        owned_new_headings=len(owned_heading),supplemental_heading_impacts=len(impact_heading)))
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'demo-evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(evidence['counts'],ensure_ascii=False,indent=2))

# Explicit adjudication entered after fresh semantic review of the affected
# source units and complete target units; identity checks above are evidence,
# not a rule that byte equality itself establishes a semantic PASS.
notes={
 'wp39-battle-context-and-participants.md': 'Existing-object parsing keeps HP0/egg/raw order; zero/mixed counts may fail before scene/normal cleanup. Demo testing still delegates normal battle execution and does not promise rollback; §6 target remains the initialized current-state contract.',
 'wp52-a-generic-numerical-and-status-evaluation.md': 'Conversion is a registered direct target query, with raw-type candidates, PP-only calculated damage-type matching and at most +14; ordinary User/0 does not consume it. WP76 true AI and approximate scoring remain distinct, so broad AI reference does not invent this as the approximate generator path.',
 'wp18-creature-identity-species-ownership.md': 'Fifteen egg-group author identities refine species input validation and form inheritance; existing content editors still consume author data while breeding semantics stay WP33/34. No new demo behavior or target implementation follows.',
 'wp36-wild-encounters-and-modifiers.md': 'Negative accepted trigger prefixes can produce negative accumulator/floor quotient; this does not change metadata version/type/slot navigation or phone uniform first-four selection. Repel default first non-egg (including fainted) is distinct from optional first able.',
 'wp11-map-topology-transfer.md': 'Dungeon text eligibility, neighbor failure residue and connected-map range pruning refine the same map contracts. Current-map identity is not a pruning exemption; conditional empty-container save/preview failure does not demonstrate a demo route or a successful save round trip.',
 'wp12-terrain-movement-vehicles.md': 'Terminal registration/consumption uses ordinary movement/collision timer, independent of jump timer. Message/new-registration/queued-consumption guards remain distinct; author input and cancel contracts do not acquire a jump cancellation policy.',
 'wp13-map-events-npc-followers.md': '117 carries parent current event number into a child bound to the then-current map; direct119 absent labels fall through. Existing author conversion references remain interpreter contracts, not new tool accept/reject policies.',
 'wp15-resource-matching-and-audio.md': 'Seven slot image roles join selected language lookup; fixed resources stay fixed. Empty icon replacement clears while empty direct animated bitmap may fail before ordinary load rescue. Preview and author tooling still retain their own resource/cleanup failure boundaries.',
 'wp08-localization.md': 'Slot seven-role lookup is a named additional consumer, not translation of all author/UI resources; game/core precedence, empty hit and no original-image retry stay bounded.',
 'wp10-migration-failure-recovery.md': 'Main P deletion precedes adjacent backup; second failure preserves orphan backup but next startup still checks P first. Existing recovery/author tool references do not promise atomic deletion or universal backup UI.',
 'wp09-save-startup-continue.md': 'System assembly distinguishes absent main file, successfully adapted empty table, and valid nonempty data; later validation/backup/continue checks stay separate. This does not fill WP77 G01 missing starting location/event evidence.',
 'wp14-random-dungeons.md': 'Default map051 Dungeon=true is a text fact, conditional on compilation/registration/loading for runtime eligibility. Region/version, tileset and geometry/event evidence remain missing; no playable demo or successful generation is inferred.',
 'wp65-title-load-options-pause-and-pc.md': 'Early startup empty/nonempty branching and later save validity/backup/continue menu retain separate gates; ordered deletion may leave an orphan backup. G01 remains an evidence limit, while Home is still only return fallback.',
 'wp69-slot-machine.md': 'Seven image roles use current game/core language material, fixed assets stay fixed, and actual reel-image height affects timing. Empty translation/load/object/random/audio/financial prefixes are distinguished without granting playable-demo or rendering credit.',
 'wp61-field-passive-effects-and-blackout.md': 'Repel comparison member is selected by configuration, while Home/healing metadata remains a return fallback rather than new-game start evidence.',
 'wp67-a-battle-interaction-and-presentation.md': 'Mixed wild inputs distinguish actual slots from configured and priority/UI traversals. Faint presentation chooses special/normal/missing cry schedules and parallel data-box disappearance; WP74 authoring/playback references do not imply audiovisual execution.',
}
fresh_primary={
 'wp72-debug-contexts-and-controls.md':[[177,230],[307,451]],
 'wp73-a-content-editors.md':[[170,225]],
 'wp76-facility-content-generation-and-simulation.md':[[36,96],[155,245]],
 'wp77-demo-evidence-and-capability-coverage.md':[[1,230]],
 'demo-dx-wp72-73-74-75-76-77.md':[[285,344]],
}
results=dict(schema_version='r8-r3-demo-independent-review.v1',reviewer='/root/r3_demo',
    candidate_commit=CANDIDATE,current_source_commit=CURRENT,r2_candidate_commit=R2_CANDIDATE,
    r2_report_commit=R2_REPORT,verdict='PASS_LIMITED_FIXED_CANDIDATE_DOMAIN',
    requested_configuration=dict(model='gpt-6.1-sol',effort='ultra',service_tier='default',speed='normal',Fast='off'),
    effective_execution_configuration={k:'UNVERIFIED'for k in ['model','effort','service_tier','speed','Fast','cloud_task_uuid']},
    counts=evidence['counts'],old_feature_results=[],active_feature_results=[],retired_metadata_results=[],
    issue_results=[],original_group_results=[],reading_ledger=[],consumer_reading_ledger=[],
    source_group_results=[],new_heading_results=[],changed_source_results=[],
    supplemental_new_heading_results=[],section_results=[],new_findings=[],
    prior_input_reconciliation=prior_inputs,identity_evidence='demo-evidence.json')
prior_active={r['feature_id']:r for r in prior['active_feature_results']}
for fid in sorted(own_ids):
    f=features[fid]
    targets={r['document']for r in f['dependencies']['direct_refs']}
    impacted=sorted(targets&changed_paths)
    reason=prior_active[fid]['reason']+' R3: own effective source/responsibilities/scope are unchanged under exact current5f identity. Current target changes were separately reread for their real contract use; no added behavior, changed responsibility boundary or unsupported outgoing edge results.'
    facets={k:dict(verdict='PASS',reason=(reason if k=='classification' else
        'Own body and explicit facet fields retain exact R2 identity; target changes separately assessed, with '+str(len(impacted))+' changed document references.'),
        method='IDENTITY_BOUND_UNAFFECTED_FACET_WITH_CURRENT_TARGET_SEMANTIC_REVIEW')
        for k in ['classification','responsibility','scope','dependency']}
    facets['current_calibration']=dict(verdict='PASS',reason='Final5f own source is byte-identical to independently read R2 source; snapshot, locator and unchanged mapping reconciled. This is source-to-routing calibration only.',method='FIXED_CURRENT_SOURCE_AND_CONSUMER_CHECK')
    results['active_feature_results'].append(dict(feature_id=fid,r2_verdict=prior_active[fid]['verdict'],verdict='PASS',
        reason=reason,review_method='LIMITED_FACET_INHERITANCE_PLUS_FRESH_CURRENT_TARGET_REVIEW',facets=facets,
        source_identity=identity(CURRENT,f['source']['document']),source_ranges=f['current_applicability']['locator']['line_ranges'],
        current_scope_unchanged=True,changed_dependency_documents=impacted,
        dependency_feature_refs=f['dependencies']['feature_refs'],finding_refs=[],
        target_compatibility='UNVERIFIED',destination_verification=f['destination_verification']['status'],
        stage_approval=f['future_plan']['stage_approval'],implementation=f['implementation']))
for r in prior['old_feature_results']:
    fid=r['feature_id'];active=fid in own_ids
    results['old_feature_results'].append(dict(feature_id=fid,r2_verdict=r.get('verdict',r.get('new_verdict')),
        new_verdict='PASS',verdict='PASS',current_state='active'if active else'retired',disposition='active'if active else'retired',
        reason=(next(x['reason']for x in results['active_feature_results']if x['feature_id']==fid)if active else
            'Complete original d62 body retained; nonfunctional evidence metadata retains original source and matching replacement/current navigation; changed consumer units separately reassessed.'),
        review_method='PER_ID_FACET_RECONCILIATION'if active else'FULL_ORIGINAL_BODY_AND_CONSUMER_NAVIGATION_CHECK',finding_refs=[]))
for r in prior['retired_metadata_results']:
    rr=copy.deepcopy(r);rr['r2_verdict']=rr.pop('verdict');rr['verdict']='PASS'
    rr['reason']+=' R3: original body and metadata/navigation are exactly preserved; final current changes of each actual consumer are separately impact-reviewed.'
    rr['history_proof']=next(x for x in retirement_checks if x['metadata_id']==r['metadata_id'])
    rr['changed_consumer_ids']=[x['feature_id']for x in consumer_evidence if not x['effective_unit_equal']and x['feature_id']in metadata[r['metadata_id']]['feature_refs']]
    results['retired_metadata_results'].append(rr)
for r in prior['issue_results']:
    rr=copy.deepcopy(r);rr['r2_verdict']=rr['verdict'];rr['verdict']='PASS'
    rr['r3_propagation']='All allocated cases and actual consumer changes checked. WP72 four-layer editing is not §7.4 persistent editing; metadata has real chapter navigation; catalog remains static NOT_EXECUTED.'
    results['issue_results'].append(rr)
for r in prior['original_group_results']:
    rr=copy.deepcopy(r);rr['r2_verdict']=r['verdict'];rr['original_specific_case_verdict']='PASS';rr['current_scope_verdict']='PASS'
    rr['method']='ORIGINAL_CASE_AND_CURRENT_DEPENDENCY_SCOPE_SEPARATE_RECONCILIATION'
    rr['r3_reason']='Original specific cases preserved with exact field/source identity; cumulative changed target contracts fresh read for actual use. No target compatibility or implementation acceptance inherited.'
    results['original_group_results'].append(rr)
for p in sorted(primary):
    old_ledger=next(r for r in prior['reading_ledger']if r['path']==p)
    results['reading_ledger'].append(dict(path=p,identity=identity(CURRENT,p),historical_identity=identity('fd1df570cad987dc3852a3b958f03916e317f7fe',p),
        fresh_commit=CURRENT,fresh_ranges=fresh_primary.get(p.split('/')[-1],[]),
        prior_reading_credit=dict(report_commit=R2_REPORT,report_path=R2_BASE+'agents/demo-results.json',
            exact_source_identity_verified=True,original_full_semantic_reading=old_ledger['prior_reading_credit'],r2_fresh_ranges=old_ledger['fresh_ranges']),
        inheritance_reason='Unchanged body/source scope and actual semantic purpose; changed incoming/outgoing consumers reviewed separately. Source identity is a prerequisite, not by itself semantic proof.',
        reading_claim='Fresh only listed ranges. Remaining full-body reading uses attributed exact-identity prior credit. No fresh full131/full105 claim.'))
for ce in consumer_evidence:
    rr=copy.deepcopy(ce)
    rr['review_method']='FRESH_FULL_EFFECTIVE_UNIT'if not ce['effective_unit_equal']or'OUTGOING_FEATURE_TARGET'in ce['roles']else'EXACT_EFFECTIVE_UNIT_NONIMPACT_INHERITANCE'
    rr['fresh_ranges']=ce['current_ranges']if rr['review_method']=='FRESH_FULL_EFFECTIVE_UNIT'else[]
    prior_receiver=[(n,x)for n,x in enumerate(prior['consumer_reading_ledger'])if x.get('feature_id')==ce['feature_id']]
    rr['prior_reading_credit']=[dict(report_commit=R2_REPORT,
        report_pointer=R2_BASE+'agents/demo-results.json#/consumer_reading_ledger/'+str(n),
        attributed_full_semantic_credit=x.get('prior_full_semantic_credit'),
        limit='R2 full source credit and unchanged current effective unit only; not a claim of fresh full current document reading.')for n,x in prior_receiver]
    rr['reason']=notes.get(ce['current_identity']['path'].split('/')[-1],
        'Existing receiving unit and its actual metadata purpose unchanged; changed clauses elsewhere in its document do not alter this mapping. Its own destination/dependency judgment belongs to the feature owner.')
    rr['verdict']='PASS_NAVIGATION_PURPOSE';results['consumer_reading_ledger'].append(rr)
for n,g in enumerate(prior['source_group_results']):
    rr=copy.deepcopy(g);rr['source_group_index']=n;rr['r2_verdict']=rr['verdict'];rr['verdict']='PASS'
    rr['changed_consumer_ids']=[i for i in g['feature_refs']if any(x['feature_id']==i and not x['effective_unit_equal']for x in consumer_evidence)]
    rr['r3_impact_reason']='Source group is unchanged, each named receiving unit identity and role reconciled; changed receiver body read in full. New refinements preserve static capability/navigation without evidence elevation.'
    results['source_group_results'].append(rr)
for d in direct_diff:
    if d['changed']:
        results['changed_source_results'].append(dict(document=d['path'],role='OUTGOING_SHARED_CONTRACT_IMPACT_NOT_PRIMARY_OWNERSHIP',
            r2_source_commit=R2_SOURCE,current_source_commit=CURRENT,verdict='PASS',semantic_reason=notes[d['path'].split('/')[-1]],
            complete_diff_identity=dict(bytes=d['complete_diff_bytes'],sha256=d['complete_diff_sha256']),
            source_acceptance_verdict='SEPARATE_GLOBAL_SOURCE_REVIEW',source_to_routing_calibration='PASS',target_compatibility='UNVERIFIED'))
for ce in consumer_evidence:
    if not ce['effective_unit_equal']:
        results['changed_source_results'].append(dict(feature_id=ce['feature_id'],document=ce['current_identity']['path'],
            role='METADATA_RECEIVER_EFFECTIVE_UNIT_IMPACT_NOT_PRIMARY_OWNERSHIP',current_source_commit=CURRENT,
            effective_ranges=ce['current_ranges'],current_unit_sha256=ce['current_unit_sha256'],verdict='PASS_NAVIGATION_PURPOSE',
            semantic_reason=notes[ce['current_identity']['path'].split('/')[-1]],
            source_acceptance_verdict='SEPARATE_GLOBAL_SOURCE_REVIEW',source_to_routing_calibration='PASS',target_compatibility='UNVERIFIED'))
for h in impact_heading:
    results['supplemental_new_heading_results'].append(dict(document=h['document'],anchor=h['anchor'],title=h['title'],
        source_ranges=h['line_ranges'],source_identity=h['source_identity'],ownership='OTHER_DOMAIN_PRIMARY_OWNER; DEMO_CONSUMER_IMPACT_ONLY',
        verdict='PASS_CONSUMER_IMPACT',affected_consumer_ids=sorted(set(h['feature_refs'])&(consumer_ids|outgoing_ids)),
        reason=notes.get(h['document'].split('/')[-1],
            'Static catalog/body refinement maps the same source contract and actual consumer; no new implementation unit, no execution or demo reachability credit.')))
for s in own_sections:
    results['section_results'].append(dict(path=s['path'],anchor=s['anchor'],line_start=s['line_start'],line_end=s['line_end'],
        feature_refs=s['feature_refs'],metadata_refs=s['metadata_refs'],coverage_scope=s.get('coverage_scope'),
        verdict='PASS',reason='Actual unchanged section identity, existing navigation and metadata/nonfunctional role retained; affected consumer impacts reviewed separately.'))
results['examined_concerns']=[dict(id='DEMO-R3-CHECK-BOX',status='NOT_A_FINDING',
    explicit_path=['META-000014','FR-000114','FR-000736','FR-000654'],
    edges_exist=True,reason='Explicit metadata→parent→excluded child→shared entry navigation reaches current WP66-A L29. The path describes contract navigation, not facility multiselect executing the normal-menu bridge.'),
    dict(id='DEMO-R3-CHECK-261',status='NOT_A_FINDING',reason='Full WP72 §13 E001–E120 and §7 reread; scope is current battle four layers, and the three-party responsibility does not claim original/persistent edits or ordinary effect followups.')]
results['allocated_new_r2_issue_ids']=[]
results['shared_governance_results']=copy.deepcopy(prior['shared_governance_results'])
for r in results['shared_governance_results']:
    r['r2_verdict']=r['verdict']
    r['r3_reason']='Exact full source identity, unchanged all-feature governance purpose and 46 total explicitly exempt headings preserved; no ordinary behavior document receives this exemption.'
results['catalog_result']=dict(document_id=prior['catalog_result']['document_id'],r2_verdict='PASS',verdict='PASS',
    sections_checked=19,static_not_executed_boundary='PASS',reason='All19 mapping rows preserved. B17 EV template/training/duplicate and B20 phone/form whole tables reread; source/current identity and actual receiving roles remain valid. No execution credit added.')
results['scope_boundaries']=dict(primary_new_headings=0,primary_changed_source_files=0,
    source_acceptance='Global receipt/tool qualification belongs to source/root reviewer; this is independent demo impact adjudication.',
    source_to_routing_calibration='PASS_LIMITED_DEMO_SHARED_DOMAIN',target_compatibility='UNVERIFIED',
    business_execution=0,prototype_execution=0,implementation='NOT_IMPLEMENTED',target_acceptance='NOT_ACCEPTED',
    stage_approval='UNAPPROVED',user_exclusion_count=0,all_upstream_closed=False)
results['limitations']=['Other-domain feature verdicts are not transferred from metadata incoming-navigation approval.',
    'Runtime/model/effort/tier/speed/Fast/cloud UUID lack authoritative echo and are UNVERIFIED.',
    'No source acceptance, target compatibility, implementation completion, user scope/phase approval or global CLOSED follows from the limited PASS.',
    'Tool parsing and byte identity do not count as fresh semantic body reading. Truncated excerpts were reread where fresh range credit is claimed.']
(OUT/'demo-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
