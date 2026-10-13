"""Close the assigned static-review scope; retain bounded foreign-domain gaps."""
from pathlib import Path
import collections
import datetime
import review_state as s

def primary(path):
    return path in ('Data/Scripts/001_Settings.rb','Data/Scripts/002_BattleSettings.rb','Data/Scripts/001_Technical/003_Intl_Messages.rb') or \
      path.startswith('Data/Scripts/010_Data/') or \
      (path.startswith('Data/Scripts/021_Compiler/') and Path(path).name.startswith(('001_','002_','003_')))

caps=s.read('source-to-spec.json')['capabilities']
assert all(c.get('semantic_comparison_complete') for c in caps)
fields=s.read('schema-field-contracts.json')['fields']
assert len(fields)==247 and all(f.get('semantic_comparison_complete') for f in fields)
cfg=s.read('configuration-branch-reviews.json')['branches']
assert len(cfg)==140 and all(b.get('semantic_comparison_complete') for b in cfg)
cov=s.read('reading-coverage.json')
owned=[e for e in cov['sources'] if primary(e['path'])]
assert len(owned)==45
for e in owned:
    assert e.get('read_ranges')==[[1,e['line_count']]],e['path']
    linked=[c for c in caps if any(a['path']==e['path'] for a in c.get('source_anchors',[]))]
    assert linked,e['path']
    e.update(review_extent='full',reading_extent='full',semantic_review_complete=True,
             review_completion_scope='Complete assigned source file: declarations, registrations, callable branches/defaults/errors and necessary data/config consumers compared to current contracts. Full review does not mean complete specification support.',
             unreviewed_ranges=[],unreviewed_semantic_obligations=[],
             capability_refs=[c['capability_id'] for c in linked],
             comparison_results=[dict(capability_id=c['capability_id'],status=c['status'],evidence_level=c.get('evidence_level','supported_static'),
                                      comparison=c.get('current_contract_comparison',c.get('comparison'))) for c in linked])
    for part in e.get('semantic_ranges',[]):
        old=part.get('comparison')
        if old:part['initial_comparison_note']=old
        part['comparison']='Completed current-contract comparison; see this file comparison_results and linked per-field/consumer ledgers. Earlier pending remarks are superseded, not additional unreviewed work.'
    if e['path'].endswith('001_GrowthRate.rb'):
        e['unexecuted_verification']='All606 literal cells were read; no independent600-positive-level recomputation or behavior-model execution. Historical arithmetic results were not used as this review evidence.'

data_paths=set(x['path'] for x in s.read('pbs-data-inspection.json')['files'])
assert len(data_paths)==73
for e in cov['sources']:
    if primary(e['path']):continue
    if e['path'] in data_paths or e['path'].startswith('Text_english_core/') or e['path']=='Data/messages_core.dat':
        assert e['review_extent']=='full',e['path']
        e['semantic_review_complete']=True
        e['review_completion_scope']='Every supplied record/key/field under the M01 data/localization projection, using complete inert inspection plus independently read schema/consumer semantics. Not every associated combat/UI effect and not linguistic translation-quality certification.'
        e['semantic_review_warning']='Counts and hashes alone are not semantic proof; current completed record-level consumer evidence is in the linked PBS/text/field/corpus ledgers. Runtime import/export and host deserialization were not executed.'
        e['unreviewed_semantic_obligations']=[]
    else:
        e['review_extent']='partial'
        e['review_completion_scope']='Necessary M01 consumer/caller projection only; actual read and semantic ranges below are authoritative. Remaining whole-file lines belong to other domains and are not certified.'
        e['m01_projection_complete']=True
        e['unreviewed_semantic_obligations']=['Whole consumer-domain behavior outside the recorded M01 interface ranges is outside this assigned review.']

main_prefix='deliverables/final-specification-set/generic-kernel/'
main_names={'wp02-rule-configuration-and-data-variants.md','wp03-content-identity-and-schema.md','wp04-pbs-lifecycle.md','wp08-localization.md'}
for e in cov['specifications']:
    name=Path(e['path']).name
    is_main=(e['path'].startswith(main_prefix) or e['path'].startswith('specs/kernel/')) and name in main_names
    is_inventory=e['path'].startswith('analysis/inventory/') or e['path']=='specs/kernel/wp02-settings-inventory-appendix.md'
    if is_main or is_inventory:
        assert e.get('read_ranges')==[[1,e['line_count']]],e['path']
        e.update(review_extent='full',semantic_review_complete=True,unreviewed_semantic_obligations=[],
                 review_completion_scope='Complete current M01 primary/effective original/inventory material; clause/table/vector mappings compare current text, not historical approval.')
    else:
        e['review_extent']='partial'
        e['m01_projection_complete']=True
        e['review_completion_scope']='Only the named M01 data/config/current-counterevidence projection. Reading a whole foreign-domain document is not whole-domain source certification.'
        e['unreviewed_semantic_obligations']=['Other-domain source behavior outside the recorded M01 projection is not certified.']
cov['notes']=[
 'Complete means the assigned available static review is finished, not that all specifications are sufficient or all inputs are compatible.',
 '45 primary source files and73 PBS +18 text files +1 safely decoded message binary are complete for M01. Foreign-domain sources/specifications retain actual partial ranges.',
 'Every primary clause/table/definition and all93 primary vectors have reverse mappings. Responsibility-table names are not counted as concrete behavior coverage.',
 'No reference/Ruby/game/behavior-model/vector execution; only inert file/container parsing, literal/identity relations and static control-flow comparison.',
 'Historical PASS and the prior isolated execution receipts were not reused as new evidence. Candidate findings require independent counterevidence.'
]
s.write('reading-coverage.json',cov)

shared=s.read('shared-interfaces.json')
for e in shared['interfaces']:
    key=e['capability_id']
    e['evidence_level']='static_semantic_comparison'
    e['execution_status']='NOT_EXECUTED'
    if key=='M01-LZ-DEFAULT-BUILD':
        e.update(status='partial',related_findings=['GR5-M01-002'],handoff='Default-build and exporter entry-set contract remains candidate002; runtime lookup is a different shared operation. All18 corpora and compiler callers were reviewed.')
    elif key=='M01-PBS-FACILITY':
        e.update(status='supported',contract='One shared facility data lifecycle:13 actual files (list plus6 trainer and6 individual pools); ten current referenced children and two unreferenced fancy files. All2770 individual rows and1600 trainer records reviewed.',handoff='Current STICK→nil item and VICEGRIP→discarded move are already covered by WP76; older profiles contain those identities. Duplicate index positions are retained. No new required finding for these samples.')
    elif key=='M01-CSV-CAST':
        e.update(status='partial',related_findings=['GR5-M01-001'],handoff='Current main/original schema, dimension and editor contracts compared; candidate001 remains pending independent counterevidence. Shared parser gaps are not replicated as separate field findings.')
    elif key=='M01-CONFIG-CONSUMER-HANDOFF':
        e.update(status='partial',contract='One declaration/consumer contract:118 Settings constants,3 callable content settings and3 Essentials metadata entries;140 bounded consumer groups have current comparisons (117 supported_static,23 partial).',
                 consumer_projections=[dict(consumer=b['consumer_projection'],source=dict(path=b['path'],version=s.R,lines=b['lines']),branch_ref=b['id'],status=b['status'],comparison=b['current_contract_comparison']) for b in cfg],
                 handoff='Use configuration-branch-reviews.json for precise direct-generation cutoffs, caller conditions and current-contract limits. Group counts are evidence partitions, not feature counts.')
    elif key=='M01-GENDER-RATIO':
        e.update(capability_id='M01-FIXED-GenderRatio',aliases=['M01-GENDER-RATIO'],status='supported',handoff='WP19 ordinary PID-derived gender is distinct from the NPC missing-field override, candidate006.')
    elif key=='M01-PBS-MOVE-EFFECT-IDENTITY':
        e.update(status='unresolved',contract='All3351 actual move records have an effect-identity link. Optional SHADOWSHED uses the well-formed unresolved RemoveAllScreens identity. The compiler accepts text; the battle factory has an unimplemented fallback, whose Status branch fails locally while damaging moves keep the ordinary base path.',
                 handoff='WP23 data table correctly warns against binding this to RemoveAllScreensAndSafeguard. Source fallback fact is established; sufficiency of the cross-owner effect contract remains unresolved. No activation/runtime claim or final required revision.')
    elif key=='M01-MAP-NAME-SHARED-TEXT':
        e.update(status='unresolved',contract='The inspected map-name getter and basic-map wrapper replace PN in the returned shared string. A language hit can mutate the stored translation; a miss can mutate raw map-name data, so later rename reads may retain the first name until reload.',
                 handoff='Keep this source-derived shared-text observation separate from ordinary display substitution. No blanket claim that all text getters mutate; cross-owner scope/compatibility adjudication remains unresolved, not a self-final required finding.')

for identity,owner,contract,consumers,finding_ids,status in [
 ('M01-FIXED-Stat','M01 data identity / WP18/WP19/WP73A','PBS six-column order HP/Attack/Defense/Speed/SpAtk/SpDef differs from registration/formula order; Species named EV pairs are a separate format.',['WP18 BaseStats','WP19 numeric interpretation','WP73A six-dimensional editors'],['GR5-M01-004'],'partial'),
 ('M01-DATA-Trainer-3','M01 schema / WP18 and WP24 generation','NPC absent fields deterministically override ordinary creature defaults; actual Unknown trainer type with mixed-sex species yields female members.',['WP18 NPC context','WP24 trainer load','WP73A missing versus explicit fields'],['GR5-M01-006'],'partial'),
 ('M01-CONFIG-STORAGE-CAPACITY','M01 MAX_PARTY_SIZE / WP25 storage','All-negative capacity uses party limit; only−1 addresses party. Other negative indices address actual boxes and may scan only the first party-limit cells.',['WP25 capacity/empty-slot search','WP66B special negative selection position'],['GR5-M01-005'],'partial'),
 ('M01-DATA-DungeonTileset','M01 registry / WP14 dungeon inputs','Nonempty missing-ID fallback chooses first record. Empty registry and absent Autotile/Tile lists can fail; valid two supplied records and all four wall-layout tables were reviewed.',['WP14 data construction/fallback','WP73B authoring'],[],'partial'),
 ('M01-LZ-CORPUS-SEMANTICS','M01 localization','All10697 records in18 corpora linked by domain/key/consumer semantics, with five differing payloads, formatted-argument consumers, legacy labels and qualified producer unknowns retained.',['All18 corpus domains','All hash text getters','Script/formatted/phone consumers'],['GR5-M01-002','GR5-M01-003'],'supported'),
]:
    shared['interfaces'].append(dict(capability_id=identity,owner=owner,contract=contract,status=status,
      consumer_projections=[dict(consumer=x,status=status) for x in consumers],related_findings=finding_ids,
      handoff='Bounded static shared contract; no whole consumer-domain certification and no reference/model execution.',evidence_level='supported_static' if status=='supported' else 'static_semantic_comparison'))
shared['interfaces']=list({e['capability_id']:e for e in shared['interfaces']}.values())
shared['identity_policy']='One canonical shared capability with consumer projections; source partitions/fields/records are not inflated into independent feature counts.'
s.write('shared-interfaces.json',shared)

for filename in ('pbs-data-inspection.json','message-data-inspection.json'):
    x=s.read(filename)
    x['warning']='Counts/hashes/literal parsing alone are not semantic review. Completed M01 acceptance is recorded in the per-record, field, corpus and consumer ledgers; no reference/importer/model execution.'
    s.write(filename,x)

summary=dict(schema_version='gr5.review.v1',module='M01',primary_source_files=45,pbs_files=73,translation_files=18,
 safely_decoded_binary_files=1,primary_source_and_data_files=137,bounded_dependency_source_files=len(cov['sources'])-137,
 source_paths_total=len(cov['sources']),specification_paths_total=len(cov['specifications']),
 schema_fields=247,configuration_definitions=124,configuration_consumer_groups=140,
 configuration_comparison=dict(collections.Counter(b['status'] for b in cfg)),
 primary_vectors=93,translation_records=10697,candidate_findings=len(s.read('findings.json')['findings']),
 final_required_findings=0,execution='NOT_EXECUTED',complete=False,phase='final artifact validation')
s.write('review-summary.json',summary)
# The task explicitly forbids writing the shared Feature Matrix. This local
# projection records classifications/status without claiming that file changed.
s.write('feature-matrix-projection.json',dict(schema_version='gr5.review.v1',module='M01',
 shared_matrix_modified=False,scope='Local review projection only, per explicit task write boundary.',
 groups=[
  dict(classification='Generic Kernel',capabilities=['configuration declarations','content identities and registries','PBS parsing/compiling/export','localization'],status='reviewed_static_with_partial_contracts'),
  dict(classification='Creature-RPG',capabilities=['species/trainer/party/storage/inventory/encounter data interfaces'],status='bounded_consumer_projection'),
  dict(classification='Pokémon Rules',capabilities=['fixed stats/Nature/gender/growth/evolution/type and profile data'],status='reviewed_static_data_and_named_consumers'),
  dict(classification='Combat Requirements',capabilities=['settings, targets, move/item effect identity interfaces'],status='bounded_consumer_projection'),
  dict(classification='Engine / Overworld Integration',capabilities=['map/terrain/weather/dungeon/resource interfaces'],status='bounded_consumer_projection'),
  dict(classification='User Interface',capabilities=['configuration, name, icon, region and authoring data consumers'],status='bounded_consumer_projection'),
  dict(classification='Demo / Developer Experience',capabilities=['all73 PBS profiles and18 translation corpora; editors/facilities/tooling interfaces'],status='reviewed_static_data_with_missing_host_demo_assets'),
 ]))
print(summary)
