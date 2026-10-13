"""Synchronize completed static comparisons and remove obsolete work placeholders."""
import re
import review_state as s
import review_ops as o
F='deliverables/final-specification-set/'
d=s.read('source-to-spec.json')
for c in d['capabilities']:
    identity=c['capability_id']
    if identity.startswith(('M01-ID-','M01-EVO-REG-')) or identity in {
        'M01-PBS-WORLD-MAP-MASK','M01-RIBBON-REGISTRY-CONSUMPTION','M01-ABILITY-FLAG-HATCHING',
        'M01-LZ-CORPUS-SEMANTICS','M01-PBS-CONNECTION-DATA','M01-FIXED-GrowthRate','M01-FIXED-GenderRatio','M01-FIXED-EggGroup'}:
        c.update(semantic_comparison_complete=True,pending=[])
    if identity.startswith('M01-EVO-REG-'):
        c['shared_capability_id']='M01-FIXED-Evolution'
        c['unit_kind']='bounded evidence partition of one shared Evolution registry; not another feature count'
    if identity.startswith('M01-DATA-'):
        c['shared_capability_id']=re.sub(r'-\d+$','',identity)
        c['unit_kind']='record behavior evidence partition; not another content class'
    if identity=='M01-TEXT-CORPUS-DATA-INTEGRITY':
        c.update(status='supported',semantic_comparison_complete=True,pending=[],
                 supported_boundary='supported_static content consistency, conjoined with M01-LZ-CORPUS-SEMANTICS; never count-only semantic proof.',
                 current_contract_comparison='All18 text domains and10697 primitive key/value records match the safely decoded fixed binary. Domain/key/placeholder/producer semantics were independently reviewed in the corpus ledger; event buckets contain no nonempty map text. No reference deserialization or importer execution.')
    if identity=='M01-PBS-DEX-DATA':
        c.update(status='supported',semantic_comparison_complete=True,pending=[],
                 supported_boundary='supported_static for actual151/256 ordered members and their identity/numbering projections.',
                 current_contract_comparison='Full actual lists, uniqueness and profile identity checks completed. Sparse hypothetical sections and writer textual regrouping belong to separate partial M01-PBS-DEX/M01-WRITE-DEX-RIBBON contracts, not unread actual members.')
    if identity=='M01-FACILITY-DEFAULT-DATA-BOUNDARIES':
        c.update(status='supported',semantic_comparison_complete=True,pending=[],
                 supported_boundary='supported_static for all2770 individual rows and1600 trainer records, current-profile tolerant references and listed consumer interfaces.',
                 current_contract_comparison='All special record fields reviewed. STICK and VICEGRIP are absent in the current item/move identity sets but present in older profiles; tolerant nil/drop behavior is already explicit in WP76. Duplicate pool indices remain positions. No unproven data migration or automatic aliases inferred.')
    if identity=='M01-PBS-GENERATION-PROFILES':
        c.update(semantic_comparison_complete=True,pending=[],
                 current_contract_comparison='All36 backup files and every actual per-record field delta were reviewed, including changing compound-form meaning and old-only identities. WP02 explicitly leaves cross-generation combinations unverified; this partial status is a compatibility scope limitation, not a claim that all variants fail or that a required new compatibility policy is missing.',
                 supported_boundary='supported_static for literal data/profile relationships only; no automatic switching, compile success, save conversion or official-generation equivalence.')
    if c.get('semantic_comparison_complete'):c['open_consumer_or_data_review']=None
s.write('source-to-spec.json',d)

family_caps={
 'town_map':'TownMap','types':'Type','abilities':'Ability','moves':'Move','items':'Item','berry_plants':'BerryPlant',
 'pokemon':'Species','pokemon_forms':'Species','pokemon_metrics':'SpeciesMetrics','shadow_pokemon':'ShadowPokemon',
 'ribbons':'Ribbon','trainer_types':'TrainerType','trainers':'Trainer','metadata':'Metadata','player_metadata':'PlayerMetadata',
 'map_metadata':'MapMetadata','dungeon_tilesets':'DungeonTileset','dungeon_parameters':'DungeonParameters','phone':'PhoneMessage',
}
fields=s.read('schema-field-contracts.json')
fields['status_scope']='Field status is the stated meaning/input/actual-data projection. Complete constructor/export/primitive grammar coverage is separately governed by linked source-to-spec capabilities; supported here never overrides a partial shared contract.'
fields['shared_primitive_contracts']=['M01-CSV-CAST','M01-CSV-ENUM','M01-CSV-RECORD','M01-CSV-WRITE']
upgrade_species={'GenderRatio','GrowthRate','BaseExp','CatchRate','Happiness','Flags'}
upgrade_trainers={'Form','Name','Moves','Item','Happiness','Ball','Shadow'}
for f in fields['fields']:
    fam=f['family'];key=f['field'];base=family_caps[fam]
    linked=[c for c in d['capabilities'] if c['capability_id'].startswith('M01-DATA-'+base+'-')]
    assert linked,(fam,key)
    f['capability_refs']=[c['capability_id'] for c in linked]
    f['semantic_comparison_complete']=True
    f['pending']=[]
    if (fam in ('pokemon','pokemon_forms') and key in upgrade_species) or \
       (fam=='trainers' and key in upgrade_trainers) or \
       fam=='player_metadata' or \
       (fam=='map_metadata' and key!='Name') or \
       (fam=='dungeon_tilesets' and key not in ('Autotile','Tile','Flags')):
        f['status']='supported'
    if key=='Flags':f['actual_value_consumer_ledger']='flag-consumer-contracts.json'
    if fam=='trainers' and key in ('Ability','AbilityIndex','Gender','Shiny','SuperShiny','Nature'):
        f.update(status='partial',related_findings=['GR5-M01-006'],coverage_limit='NPC absent-field overlay is not the generic creature default; see candidate006 and M01-DATA-Trainer-3.')
    elif key=='BaseStats' or (fam=='trainers' and key in ('IV','EV')):
        f.update(status='partial',related_findings=['GR5-M01-004'],coverage_limit='Generic PBS six-column input/output order remains candidate004; editor/default/stat-formula orders must remain separate.')
    elif key in ('Height','Weight') and fam in ('pokemon','pokemon_forms'):
        f.update(status='partial',related_findings=['GR5-M01-001'],coverage_limit='Restricted active float grammar remains candidate001; stored tenth-unit semantics are supported separately.')
    elif f['status']=='partial':
        # Preserve precise source-derived field semantics; the limitation is in
        # present-contract coverage, not an assertion this field was not read.
        f['coverage_limit']='Complete current-contract limitation is recorded by the linked partial capabilities; field declaration, construction default and actual values were reviewed. No pending reading task is hidden by this status.'
    else:
        f['coverage_limit']='Shared primitive/constructor/export limitations may still apply; see linked capabilities. No full consumer-domain or runtime claim.'
s.write('schema-field-contracts.json',fields)
statuses={f['field_id']:f['status'] for f in fields['fields']}
# Synchronize references only. Does not parse/execute PBS behavior or re-label
# data based on counts; the prior per-record semantic acceptance remains intact.
for file in s.read('pbs-data-inspection.json')['files']:
    data=s.read(file['record_review_artifact']);changed=False
    for record in data['records']:
        for prop in record.get('properties',[]):
            key=prop.get('field_contract_ref')
            if key in statuses:prop['capability_status']=statuses[key];changed=True
    if changed:s.write(file['record_review_artifact'],data)
for path in sorted(s.OUT.glob('pbs-typed-*.json')):
    data=s.read(path.name)
    for record in data.get('records',[]):
        for f in record.get('fields',[]):
            if f.get('field_contract_ref') in statuses:f['consumer_semantic_status']=statuses[f['field_contract_ref']]
    s.write(path.name,data)

o.spec('analysis/repository-overview.md',[[149,149]],'E25 reference/demo availability boundary read; this closes the overview text gap, not old evidence approval.')
o.spec('specs/demo/wp75-project-conversion-and-authoring-tools.md',[[1,65]],'Current original translation scope/dependencies and compiler call boundary explicitly delegate the authoring algorithm to WP08.')

findings=s.read('findings.json')
for f in findings['findings']:
    f['execution_status']='NOT_EXECUTED; static source and safe literal data inspection only'
    f['status']='candidate_pending_independent_counterevidence'
    if f['id']=='GR5-M01-001':
        f['negative_evidence_search'] += [
          dict(path=F+'creature-rpg/wp18-creature-identity-species-ownership.md',read_ranges=[[1,363]],result='Whole current default/dimension contract read; stored units and individual size math do not define accepted PBS float lexemes.'),
          dict(path='specs/creature-rpg/wp18-creature-identity-species-ownership.md',read_ranges=[[1,384]],result='Whole effective original likewise has stored units/defaults, not this decimal recognizer boundary.'),
          dict(path=F+'demo-dx/wp73-a-content-editors.md',read_ranges=[[1,174]],result='Numeric editor bounds/decimeter conversion are a different entry, not a text-parser acceptance contract.'),
          dict(path=F+'user-interface/wp66-b-storage-and-pokedex-ui.md',read_ranges=[[1,271]],result='Metric/imperial presentation consumes stored units; no countervailing float input rule.')]
        f['unknowns']=['Reference/compiler/error UI not executed','Independent counterevidence and future invalid-input compatibility decision remain pending']
    if f['id'] in ('GR5-M01-002','GR5-M01-003'):
        f['negative_evidence_search'] += [
          dict(path=F+'demo-dx/wp75-project-conversion-and-authoring-tools.md',read_ranges=[[1,394]],result='Whole current tool contract read; translation algorithm delegated to WP08, event-text command rewriting is a different stage.'),
          dict(path='specs/demo/wp75-project-conversion-and-authoring-tools.md',read_ranges=[[1,65]],result='Effective original scope/dependency/call clauses likewise delegate translation to WP08.'),
          dict(path='specs and deliverables/final-specification-set and analysis',method='exact symbol and reasonable synonym navigation, followed by the above whole current relevant contracts',result='stringToKey/setMessagesAsHash/addMessagesAsHash/default-message/core-default/line-whitespace searches found no additional concrete rule that resolves the named gap. Search hits alone were not treated as negative semantic evidence.')]
        f['unknowns']=['Real import/export and host/plugin/event execution not performed','Independent counterevidence remains pending; no self-final required disposition']
    if f['id']=='GR5-M01-004':
        f['negative_evidence_search'] += [
          dict(path='specs/pokemon-rules/wp19-attributes-ability-and-stats.md',read_ranges=[[1,417]],result='Whole original read; formula columns and character-description ring are separate from generic authored PBS mapping.'),
          dict(path='specs/creature-rpg/wp18-creature-identity-species-ownership.md',read_ranges=[[1,384]],result='Whole original data/NPC clauses read; no explicit generic six-column input mapping.'),
          dict(path=F+'demo-dx/wp73-a-content-editors.md',read_ranges=[[1,174]],result='Full current editor contract says PBS order without expanding it; absent-IV/EV zero editor behavior is already explicit and is not this candidate.'),
          dict(path='specs/demo/wp73-a-content-editors.md',read_ranges=[[65,109]],result='Original compound-property clauses retain the same PBS-order shorthand.'),
          dict(path=F+'pokemon-rules/wp22-transformation-data.md',read_ranges=[[1,77]],result='Counterevidence: this48-row table explicitly uses HP/Attack/Defense/Speed/SpAtk/SpDef. Its wording limits the order to this table; it does not explicitly define the generic BaseStats or Trainer IV/EV grammar. Independent reviewer should assess whether cross-reference already suffices.'),
          dict(path=F+'test-catalog/pokemon-rules-wp19-21-22-23-34.md',read_ranges=[[1,88]],result='ST64 uses the same characteristic ring but identifies a different operation. Keep as counterevidence context, not ignore it.')]
        f['unknowns']=['Independent reviewer may judge the transformation-table order sufficient by reference; candidate remains unresolved','No compiler or writer executed']
    # Every initial candidate remains provisional; completion of this static
    # review is not independent counterevidence resolution.
    f['review_resolution']='本轮所列源与现行合同比较已记录，状态保持候选待独立反证；未自签最终必修，未执行参考/模型。'
s.write('findings.json',findings)
o.progress('字段和数据记录状态已同步，旧“待检查全部语料/世代文件”等占位已清除。六条候选补入本轮新增反证范围；004明确保留WP22表序作为反证，不忽略已有具体材料。','共享交界聚合、阅读范围结算及产物一致性检查')
print('Synchronized field and candidate comparison state')
