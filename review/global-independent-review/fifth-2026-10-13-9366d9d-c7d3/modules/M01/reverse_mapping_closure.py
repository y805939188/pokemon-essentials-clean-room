"""Precise reverse mappings for the four primary specifications and93 vectors."""
import re
import review_state as s
import review_ops as o
F='deliverables/final-specification-set/'
specs={
 '02':F+'generic-kernel/wp02-rule-configuration-and-data-variants.md',
 '03':F+'generic-kernel/wp03-content-identity-and-schema.md',
 '04':F+'generic-kernel/wp04-pbs-lifecycle.md',
 '08':F+'generic-kernel/wp08-localization.md',
}
cfg=s.read('configuration-consumer-ledger.json')
branches=s.read('configuration-branch-reviews.json')['branches']
o.cap('M01-CONFIG-DECLARATIONS','Data/Scripts/001_Settings.rb',[[1,524]],
      'All118 Settings constants,3 callable configuration entries and3 Essentials metadata declarations were read and compared to WP02 and its effective inventory appendix. BattleSettings declarations have independent source anchors. Declaration defaults/derivations are distinct from140 reviewed consumer projections.',
      [dict(path=specs['02'],clause='§3–5 and every dictionary row'),dict(path='specs/kernel/wp02-settings-inventory-appendix.md',clause='complete declaration tables')], 'supported')
caps=s.read('source-to-spec.json')
cc=next(c for c in caps['capabilities'] if c['capability_id']=='M01-CONFIG-DECLARATIONS')
cc['source_anchors'].append(dict(path='Data/Scripts/002_BattleSettings.rb',version=s.R,lines=[1,140]))
cc.update(semantic_comparison_complete=True,definition_ledger='configuration-consumer-ledger.json',consumer_ledger='configuration-branch-reviews.json')
caps['capabilities'].append(dict(capability_id='M01-CONFIG-STORAGE-CAPACITY',
 source_anchors=[dict(path='Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb',version=s.R,lines=[128,176])],
 spec_anchors=[dict(path=F+'creature-rpg/wp25-party-and-storage.md',version=s.B,clause='§3.1–3.2')],status='partial',
 comparison='Negative capacity query uses MAX_PARTY_SIZE for every negative box number, unlike only−1 party addressing. Candidate005; box-count construction and stored count remain distinct.',
 related_findings=['GR5-M01-005'],semantic_comparison_complete=True,evidence_level='static_semantic_comparison',pending=[]))
# Stable upsert if this bookkeeping script is explicitly repeated.
unique={c['capability_id']:c for c in caps['capabilities']};caps['capabilities']=list(unique.values());s.write('source-to-spec.json',caps)
byid=unique

def sources(ids):
    result=[]
    for identity in ids:
        assert identity in byid,identity
        for a in byid[identity].get('source_anchors',[]):
            if a not in result:result.append(a)
    return result
def entry(wp,clause,a,b,ids,status='supported',comparison=None,kind='behavior'):
    return dict(path=specs[wp],version=s.B,clause=clause,lines=[a,b],capability_refs=ids,
       source_anchors=sources(ids),status=status,evidence_level='supported_static' if status=='supported' else 'static_semantic_comparison',
       semantic_comparison_complete=True,claim_kind=kind,
       supported_boundary='Only the statement/rule in this clause and its stated prerequisites; no runtime or complete consumer-domain approval.',
       comparison=comparison or 'Current clause compared to the named independently inspected source capability; see its detailed source-to-spec decision.',
       effective_supplements=['specs/kernel/'+specs[wp].split('/')[-1]])

reverse=s.read('spec-to-source.json')
# Preserve all93 primary vectors and existing nonprimary projected clauses.
clauses=[x for x in reverse['clauses'] if x['path'] not in specs.values()]
for wp,groups in {
 '02':[
  ('§1–2 purpose and dimensions',1,20,['M01-CONFIG-DECLARATIONS'],'supported'),
  ('§3 configuration/declaration/consumer distinction',21,31,['M01-CONFIG-DECLARATIONS'],'supported'),
  ('§4 dictionary reading scope',33,41,['M01-CONFIG-DECLARATIONS'],'supported'),
  ('§5.1–5.4 declared generation and field-badge derivations',204,209,['M01-CONFIG-DECLARATIONS'],'supported'),
  ('§5.5–5.6 direct-generation and combination boundary',210,211,['M01-CONFIG-DECLARATIONS'],'supported'),
  ('§6.1 input discovery and facilities',213,226,['M01-PBS-DISCOVER-SCHEDULE','M01-PBS-FACILITY'],'supported'),
  ('§6.2 generation/Shadow backup candidates',228,235,['M01-PBS-GENERATION-PROFILES','M01-DATA-ShadowPokemon-1'],'supported'),
  ('§6.3 language and authored lists',237,244,['M01-LZ-LOAD','M01-LZ-EXPORT','M01-CONFIG-DECLARATIONS'],'supported'),
  ('§7 unresolved combination table',246,256,['M01-PBS-GENERATION-PROFILES','M01-CONFIG-DECLARATIONS'],'supported'),
  ('§8 invalid/host boundary',258,263,['M01-CONFIG-DECLARATIONS','M01-PBS-TRIGGER-FAIL'],'supported'),
  ('§9–11 tests/dependencies/reservations',265,278,['M01-CONFIG-DECLARATIONS','M01-PBS-DISCOVER-SCHEDULE'],'supported'),
 ],
 '03':[
  ('§1–2 scope and identity dimensions',1,23,['M01-ID-SYMBOL','M01-ID-INTEGER','M01-ID-DUAL'],'supported'),
  ('§3.1 identity/query/equality/default writer table',24,43,['M01-ID-SYMBOL','M01-ID-INTEGER','M01-ID-DUAL','M01-ID-EQUALITY-WRITE'],'supported'),
  ('§3.2 Trainer/PhoneMessage',44,49,['M01-DATA-Trainer-2','M01-DATA-PhoneMessage-1','M01-DATA-PhoneMessage-2'],'supported'),
  ('§3.2 Encounter version identity/enumeration',50,50,['M01-DATA-Encounter-1'],'supported'),
  ('§3.2 Metadata/Player/Terrain',51,53,['M01-DATA-Metadata-1','M01-DATA-PlayerMetadata-1','M01-FIXED-TerrainTag'],'supported'),
  ('§3.2 dungeon fallback',54,55,['M01-DATA-DungeonTileset-1','M01-DATA-DungeonParameters-1'],'partial'),
  ('§3.2 metrics/species query',56,58,['M01-DATA-SpeciesMetrics-1','M01-DATA-Species-3'],'supported'),
  ('§3.3 all classes/nonregistry/suffix',59,70,['M01-ID-BULK-DISCOVERY','M01-PBS-DISCOVER-SCHEDULE','M01-DATA-MiscPBSData-2'],'supported'),
  ('§4.1 registration/loading/startup',71,78,['M01-ID-BULK-DISCOVERY','M01-PBS-COMPILE-ALL'],'supported'),
  ('§4.2 required/optional missing data',79,88,['M01-PBS-TRIGGER-FAIL','M01-DATA-ShadowPokemon-1'],'supported'),
  ('§4.3 stated constructor examples',89,92,['M01-DATA-Species-3','M01-DATA-Item-3','M01-DATA-Move-1','M01-DATA-MapMetadata-1'],'supported'),
  ('§4.4 query side effects',93,96,['M01-DATA-SpeciesMetrics-1','M01-DATA-DungeonParameters-1'],'supported'),
  ('§5.1 structure and scalar modes',97,118,['M01-CSV-CAST','M01-CSV-ENUM','M01-CSV-RECORD'],'partial'),
  ('§5.2 direct/generic/trainer duplicates',119,129,['M01-PBS-GENERIC','M01-PBS-TRAINER','M01-PBS-PHONE'],'supported'),
  ('§5.2 dex/encounter duplicates and phone consumer boundary',130,134,['M01-PBS-DEX','M01-PBS-ENCOUNTER','M01-PBS-PHONE'],'supported'),
  ('§5.2 references and validation stages',136,145,['M01-CSV-ENUM','M01-PBS-GENERIC','M01-PBS-SPECIES'],'supported'),
  ('§6 fixed/authored distinction and full Nature dependency',146,159,['M01-ID-BULK-DISCOVERY','M01-FIXED-Nature','M01-FIXED-GrowthRate'],'supported'),
  ('§8 baseline/candidate distinctions',207,213,['M01-DATA-ShadowPokemon-1','M01-PBS-GENERATION-PROFILES'],'supported'),
  ('§9 failures/unknowns',214,223,['M01-ID-SYMBOL','M01-DATA-SpeciesMetrics-1','M01-PBS-TRIGGER-FAIL'],'supported'),
  ('§10–12 vectors/dependencies/reservations',224,240,['M01-ID-BULK-DISCOVERY','M01-PBS-GENERIC'],'supported'),
 ],
 '04':[
  ('§1–2 lifecycle scope',1,20,['M01-PBS-COMPILE-ALL','M01-PBS-DISCOVER-SCHEDULE'],'supported'),
  ('§3.1 trigger table and whole-second comparison',21,37,['M01-PBS-TRIGGER-FAIL'],'supported'),
  ('§3.2 exception-stage table',38,48,['M01-PBS-TRIGGER-FAIL'],'supported'),
  ('§4.1 ordinary/explicit discovery',49,57,['M01-PBS-DISCOVER-SCHEDULE','M01-PBS-FACILITY'],'supported'),
  ('§4.2 line preprocessing and CSV joining',58,69,['M01-PBS-SECTIONS','M01-CSV-SPLIT'],'supported'),
  ('§4.2 record/scalar/enum conversion',71,80,['M01-CSV-RECORD','M01-CSV-CAST','M01-CSV-ENUM'],'partial'),
  ('§4.2 property/identity/validation rules',82,93,['M01-PBS-GENERIC','M01-PBS-PHONE'],'supported'),
  ('§4.3 dependency-edge table',94,111,['M01-PBS-DISCOVER-SCHEDULE','M01-PBS-SPECIES','M01-PBS-ITEM-BERRY','M01-PBS-METADATA'],'supported'),
  ('§4.4 dedicated encounter parser',112,126,['M01-PBS-ENCOUNTER'],'supported'),
  ('§5.1 data output and animation change condition',127,136,['M01-PBS-COMPILE-ALL','M01-PBS-ANIMATION'],'partial'),
  ('§5.2 fixed textual renames',137,140,['M01-PBS-MIGRATE'],'supported'),
  ('§5.3 map/event conversion call boundary',141,147,['M01-PBS-COMPILE-ALL'],'supported'),
  ('§5.4 animation mapping',148,152,['M01-PBS-ANIMATION'],'partial'),
  ('§5.5 writer callers/grouping/format',153,162,['M01-WRITE-GENERIC','M01-WRITE-CONNECTION','M01-WRITE-DUNGEON-ALL'],'supported'),
  ('§5.5 encounter probability round trip',164,164,['M01-WRITE-ENCOUNTER','M01-PBS-ENCOUNTER','M01-FIXED-EncounterType'],'supported'),
  ('§5.5 hash text loss on reparse',166,166,['M01-CSV-QUOTE','M01-PBS-SECTIONS'],'supported'),
  ('§5.5 metrics output paths and omission table',168,175,['M01-WRITE-METRICS','M01-DATA-SpeciesMetrics-1'],'supported'),
  ('§5.5 evolution getter/editor/write state distinction',177,178,['M01-DATA-Species-2','M01-DATA-Species-5','M01-PBS-SPECIES'],'supported'),
  ('§6 staged mutation/errors',179,192,['M01-PBS-TRIGGER-FAIL','M01-DIAGNOSTIC','M01-PBS-COMPILE-ALL'],'supported'),
  ('§7 interface ownership table',193,203,['M01-PBS-COMPILE-ALL','M01-LZ-COLLECT','M01-WRITE-GENERIC'],'supported'),
  ('§8 defaults/variants/reservations',204,211,['M01-CONFIG-DECLARATIONS','M01-PBS-TRIGGER-FAIL','M01-PBS-GENERATION-PROFILES'],'supported'),
  ('§9–11 vectors/dependencies/reservations',212,227,['M01-PBS-COMPILE-ALL','M01-CSV-RECORD'],'supported'),
 ],
 '08':[
  ('§1–2 domains/default-vs-language purpose',1,19,['M01-LZ-DOMAINS','M01-LZ-LOOKUP'],'supported'),
  ('§3.1 all31 domain identities',21,25,['M01-LZ-DOMAINS'],'supported'),
  ('§3.2 key shape/normalization',27,32,['M01-LZ-KEY','M01-LZ-DOMAINS'],'partial'),
  ('§4 language selection/loading/save',34,40,['M01-LZ-LOAD'],'supported'),
  ('§5.1 lookup table',42,52,['M01-LZ-LOOKUP'],'supported'),
  ('§5.2 exception and empty-hit table',54,63,['M01-LZ-LOOKUP','M01-LZ-LOAD','M01-LZ-INTERPOLATE'],'supported'),
  ('§5.3 parameter substitution and table',65,79,['M01-LZ-INTERPOLATE'],'supported'),
  ('§6.1 collector and default build',81,88,['M01-LZ-COLLECT','M01-LZ-DEFAULT-BUILD'],'partial'),
  ('§6.2 exporter/escaping',90,96,['M01-LZ-EXPORT','M01-LZ-ESCAPE'],'partial'),
  ('§6.2.1 sparse event buckets',98,108,['M01-LZ-EXPORT'],'supported'),
  ('§6.3 import path/shape/truncation',110,117,['M01-LZ-IMPORT','M01-TRANSLATION-SECTIONS'],'supported'),
  ('§6.3.1 empty/hash/whitespace boundaries',119,131,['M01-LZ-IMPORT','M01-LZ-ESCAPE'],'supported'),
  ('§6.3.2 duplicate-key/section table',133,148,['M01-LZ-IMPORT','M01-LZ-KEY'],'supported'),
  ('§6.4 mutation-stage table',150,157,['M01-LZ-COLLECT','M01-LZ-EXPORT','M01-LZ-IMPORT'],'supported'),
  ('§7 defaults/variants',159,165,['M01-LZ-LOAD','M01-LZ-DOMAINS'],'supported'),
  ('§8 boundaries',167,174,['M01-LZ-LOOKUP','M01-LZ-IMPORT','M01-LZ-INTERPOLATE'],'supported'),
  ('§9–11 vectors/dependencies/reservations',176,191,['M01-LZ-DOMAINS','M01-LZ-CORPUS-SEMANTICS'],'supported'),
 ],
}.items():
    for clause,a,b,ids,status in groups:clauses.append(entry(wp,clause,a,b,ids,status))

# Each definition points at the exact grouped dictionary row and the effective
# original inventory row. Values were previously semantically compared; this
# operation records the cross-reference, not a new lexical-pass claim.
text=(s.ROOT/specs['02']).read_text().splitlines()
appendix='specs/kernel/wp02-settings-inventory-appendix.md'
app=(s.ROOT/appendix).read_text().splitlines()
for definition in cfg['definitions']:
    key=re.split(r'::|\.',definition['key'])[-1]
    if definition['key'].startswith('Essentials::'): row=27
    elif key.startswith('BADGE_FOR_'):row=78
    elif key.startswith('NUM_BADGES_BOOST_'):row=185
    elif key.endswith('_ANIMATION_ID'):row=166
    else:
        hits=[i for i,line in enumerate(text,1) if 41<=i<=202 and line.startswith('|') and re.search(r'(?<!\w)'+re.escape(key)+r'(?!\w)',line.split('|')[1])]
        assert len(hits)==1,(key,hits)
        row=hits[0]
    app_rows=[i for i,line in enumerate(app,1) if line.startswith('|') and re.search(r'(?<!\w)'+re.escape(key)+r'(?!\w)',line)]
    assert app_rows,(key,'missing appendix')
    definition.update(spec_anchors=[dict(path=specs['02'],version=s.B,lines=[row,row],clause='dictionary/declaration '+key),
                                   dict(path=appendix,version=s.B,lines=[app_rows[0],app_rows[0]],clause='individual declaration '+key)],
                      declaration_comparison='Default/derivation and declared purpose compared to the complete fixed declaration; runtime projections are separately linked branches.')
    e=entry('02','definition '+definition['key'],row,row,['M01-CONFIG-DECLARATIONS'],
            comparison='Declared default/derivation supported_static. Complete consumer status is '+definition['status']+'; see linked branch decisions, not inferred from this dictionary row.',kind='configuration_dictionary_row')
    e['source_anchors']=[dict(path=definition['definition']['path'],version=s.R,lines=[definition['definition']['line'],definition['definition']['line']])]
    e['consumer_branch_refs']=definition['branch_refs'];e['effective_supplements']=[appendix]
    clauses.append(e)
s.write('configuration-consumer-ledger.json',cfg)

# Responsibility-table rows are certified as routing only; they never count as
# an implementable behavior merely because a field/family name appears.
table=(s.ROOT/specs['03']).read_text().splitlines();family=None
for line_no in range(166,205):
    line=table[line_no-1]
    if not line.startswith('|'):continue
    label=line.split('|')[1].strip()
    if label!='〃':family=label.split('（')[0]
    if family=='固定规则 17 类':ids=[c for c in byid if c.startswith(('M01-FIXED-','M01-EVO-REG-'))]
    elif family=='非类产物与资源':ids=['M01-DATA-MiscPBSData-1','M01-DATA-MiscPBSData-2','M01-PBS-CONNECTION-DATA','M01-PBS-DEX-DATA','M01-PBS-FACILITY','M01-PBS-ANIMATION']
    else:ids=[c for c in byid if c.startswith('M01-DATA-'+family+'-')]
    assert ids,(line_no,family)
    clauses.append(entry('03','§7 responsibility row '+str(line_no),line_no,line_no,ids,
        comparison='Supported only as field ownership/dependency routing. Concrete rules are compared separately in schema-field-contracts.json and source-to-spec.json; this row alone is not behavior coverage.',kind='responsibility_assignment_only'))

vector_decisions={
 'KC02':('Declared affection/soft-cap separation and actual consumers checked; no claim all combinations or battle outcomes are verified.',[]),
 'KC03':('Count>=4 versus badge index4 is supported by the field-move guard, including zero-based fifth badge.',[]),
 'KC04':('Ordinary root discovery and fixed-list explicit trainer file are both inspected; all referenced actual facility children mapped.',[]),
 'KL22':('Conditional successful save/write/recompile has probability0→bare Land→default21; OldRod default0 and positive70 provide distinct controls.',[]),
 'KL23':('Metric path selection derives only from nonzero-form records; no such record means no PBS write despite successful data save.',[]),
 'KL24':('Nonzero same-suffix record selects the path before equal-value form omission; base altitude4 remains written.',[]),
 'KL25':('Only extra suffix gets an output path; section omission does not cancel a selected path.',[]),
 'KL27':('Plural Evolutions getter returns nil, property default is[], parent No skips register/save/write; original relation remains numeric.',
          [('Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb',[926,988]),('Data/Scripts/020_Debug/002_Editor_DataTypes.rb',[1545,1562]),('Data/Scripts/020_Debug/002_Editor_DataTypes.rb',[1624,1706])]),
 'KL28':('Parent Yes constructs/registers the empty list then saves and writes; no global predecessor rebuild occurs until full compilation.',
          [('Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb',[926,988])]),
}
for e in clauses:
    if '/test-catalog/' not in e['path']:continue
    identity=e['clause'].removeprefix('vector ')
    if identity in vector_decisions:
        comparison,extra=vector_decisions[identity]
        e.update(status='supported',evidence_level='supported_static',pending=None,comparison=comparison,
                 supported_boundary='Static conditional vector only; NOT_EXECUTED. No reference/model or host/UI execution.')
        for path,ranges in extra:
            a=dict(path=path,version=s.R,lines=ranges)
            if a not in e['source_anchors']:e['source_anchors'].append(a)
    e['semantic_comparison_complete']=True
    e['execution_status']='NOT_EXECUTED_THIS_REVIEW'
reverse['clauses']=clauses
reverse['method']='Manual clause/table/rule comparisons; exact rows cross-linked after the source and current contracts were read. No support inferred from heading, hit count, or historical PASS.'
reverse['primary_vector_count']=93
s.write('spec-to-source.json',reverse)
for path,ranges,rule in [
 ('Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb',[[926,996]],'Species parent No/Yes construction/register/save/write sequence for KL27/28.'),
 ('Data/Scripts/020_Debug/002_Editor_DataTypes.rb',[[1340,1360],[1545,1562],[1624,1706]],'Evolution default empty list and exact property-list Save/No/Cancel result; not a whole-editor certification.'),
]:o.source(path,ranges,[dict(lines=ranges[0],entry_or_rule='Primary vector necessary caller',comparison=rule)])
o.progress('四份主规格的反向映射已按条款/表重新建立：WP02逐124定义链接当前合并词典行和原始附录，WP03责任行只认证归属、不冒充行为覆盖。93条主责向量均完成静态路径核对，全部未执行。','字段状态、共享交界、候选反证与最终锚点/范围验证')
print('Reverse entries:',len(clauses),'primary vectors:93; declarations:124')
