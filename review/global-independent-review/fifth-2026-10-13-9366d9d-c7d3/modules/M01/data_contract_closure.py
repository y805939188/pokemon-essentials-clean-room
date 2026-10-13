"""Manual registry and record-contract comparisons; audit metadata only."""
import review_state as s
import review_ops as o
F='deliverables/final-specification-set/'
paths={p.name.split('-')[0][2:]:str(p.relative_to(s.ROOT)) for p in (s.ROOT/F).glob('*/*.md') if p.name.startswith('wp')}
def anchor(wp,clause):
    if '/' in wp:return dict(path=F+wp,version=s.B,clause=clause)
    return dict(path=paths[wp],version=s.B,clause=clause)

rows={
 'MiscPBSData-1':('supported',[('73','cache/save boundaries'),('03','§3.3')], 'Four cache invalidations, map helper reset, conditional current-map encounter setup and conditional tileset reload agree with world-editor/encounter cache boundaries; no implicit ordinary map reload.'),
 'MiscPBSData-2':('supported',[('03','§3.3')], 'Lazy non-registry loading and falsey move-mapping fallback agree; file/read failure is not silently upgraded to an empty-map guarantee.'),
 'TownMap-1':('partial',[('63','§3'),('03','§5.1')], 'Point coordinates, labels, optional destination and visibility gate are supported by the three distinct map consumers. Constructor Name ???/filename absence and complete tuple grammar are finer than the domain summary; all actual points were reviewed.'),
 'Type-1':('supported',[('43','§3–4'),('03','§5')], 'Actual18 current type records plus old/Shadow variations, effectiveness lists, nil-attack neutrality and relation precedence were compared. Identity, pseudo/category metadata and list references are separate from battle multipliers.'),
 'Type-2':('supported',[('43','§4')], 'Neutral1, weakness2, resistance0.5, immunity0 and multiplication across supplied defending types match; the helper itself does not deduplicate its arguments.'),
 'Ability-1':('partial',[('08','§3.1–3.2'),('03','§5; §7')], 'Names/descriptions and arbitrary case-insensitive flags have explicit consumer projection. Full raw Unnamed/??? constructor defaults are not a complete authored-data table in the current domain specifications.'),
 'Move-1':('partial',[('43','§2–3'),('03','§4.3; §5.1')], 'All13 keys and every actual profile value reviewed. Type NONE/accuracy100/PP5 examples are explicit; the remaining category/power/target/function defaults and status/power compile normalization are not fully enumerated.'),
 'Move-2':('partial',[('02','MOVE_CATEGORY_PER_MOVE'),('43','§3')], 'Configured move-vs-type category behavior is supported, but the data-reader zero-power prerequisite differs from the battle wrapper and is not explicitly distinguished in current prose.'),
 'Move-3':('supported',[('66','summary move presentation'),('67','battle move presentation')], 'Active display getters return stored values. Both disabled display blocks were read and excluded; dormant effect formulas are not a live preview requirement.'),
 'Move-4':('partial',[('04','§5.5')], 'Zero Power/Priority/EffectChance suppression is a specific serializer normalization beyond the generic non-lossless output contract.'),
 'Item-1':('partial',[('28','item dispatch and item data'),('73','content editor item fields'),('03','§5.1')], 'All16 keys and enumerations read, with editor bounds kept separate. Not every constructor/default or exact enum alias is enumerated in current prose; actual data and consumer dispatch are mapped.'),
 'Item-2':('supported',[('15','§4 resource fallbacks')], 'Direct icon, machine type icon, HM/TR generic machine fallback, nil back image, unknown item fallback, held/mail resources match the current resource chain.'),
 'Item-3':('partial',[('03','§4.3'),('08','§3.1–3.2'),('29','prices')], 'Five message domains, sell-price floor-half and BP1 match. Nil-only portion-name fallback versus valid empty string and all remaining raw defaults are finer than the published item catalog.'),
 'Item-4':('partial',[('28','importance and consumption'),('38','ball categories'),('66','bag quantity display')], 'TM/HM versus TR importance, holdability, consumability and species/ability-specific unlosable checks were compared. ShowQuantity true OR nonimportant remains an explicit coverage gap; current UI names the predicate without its full Boolean rule.'),
 'Item-5':('partial',[('04','§5.5')], 'Suppression of half-price/BP1/use0 and false Consumable emission only for nonimportant items is not a complete explicit serializer contract in current prose.'),
 'BerryPlant-1':('supported',[('pokemon-rules/wp60-berry-plants.md','§3.3'),('04','§4.3')], 'All67 modern and64 old triples, swapped yield bounds,3/15/2–5 defaults and growth/replant/ripe constants match; ordinary symbol identity has no compiler Item foreign key.'),
 'Species-1':('partial',[('18','§3.1–3.2'),('04','§5.5')], 'Base/form schema distinction and all data were compared. Float and six-column order candidates001/004 persist; singular/plural evolution keys share a destination and have ordered precedence not fully expressed by general fields.'),
 'Species-2':('supported',[('demo-dx/wp73-a-content-editors.md','§2–3.5; §6'),('04','§5.5')], 'All editor property entries read; numeric editor limits are not PBS limits. Plural evolution editor read versus singular output mutation is explicitly distinguished.'),
 'Species-3':('supported',[('18','§3.1–3.2 default table'),('03','§3.2'),('08','§3.1–3.2')], 'Full constructor table and compound/base fallback match current WP18, including unregistered default-form fallback and missing/nonpositive stats normalized to1; all four text domains mapped.'),
 'Species-4':('partial',[('18','§3.2; §3.4'),('31','family and predecessor rules'),('34','offspring and form inheritance')], 'DefaultForm, metrics registration, baby/incense recursion and family consumers were read. Fine traversal order, multiple predecessor choice and every derived convenience predicate are more detailed than the consolidated domain rules; no unused feature inferred absent.'),
 'Species-5':('partial',[('04','§5.5'),('18','§3.2')], 'Evolution string mutation is explicitly covered. Exact zero/empty/default omission, base-form comparison and grouped held-item inheritance remain partial output detail; stats/float candidates separately linked.'),
 'Species_files-1':('supported',[('15','§4.1')], 'All bitmap fallbacks, per-axis discard priority, egg/base/000 and altered-bitmap lifecycle match the current resource contract; real media not available/loaded.'),
 'Species_files-2':('supported',[('15','§4.1'),('demo-dx/wp73-b-world-editors.md','metrics query and save')], 'Icons, footprints and shadow form/base/metric fallback match; a metric query may register content before a later save.'),
 'Species_files-3':('supported',[('15','cry resources and duration')], 'Form/base/suffix selection, egg suppression, swallowed playback exception and duration/pitch boundaries agree; this is not audio playback verification.'),
 'SpeciesMetrics-1':('supported',[('03','§3.2; §4.4'),('04','§5.5')], 'Species identity validation, base default registration, form clone registration and nonpositive-form base query agree with explicit query side-effect and export-path contracts.'),
 'SpeciesMetrics-2':('supported',[('demo-dx/wp73-b-world-editors.md','metrics fields'),('user-interface/wp67-a-battle-interaction-and-presentation.md','battle sprite metrics')], 'Coordinate defaults, default shadow size2, offsets scaled2, player/foe parity and foe-only shadow horizontal shift match the inspected presentation/editor projections; all674 records per profile checked.'),
 'ShadowPokemon-1':('supported',[('03','§4.2'),('pokemon-rules/wp23-shadow-data-and-vectors.md','complete131-row table'),('pokemon-rules/wp23-shadow-hyper-and-purification.md','data input')], 'Optional absence retains existing table, positive gauge/default4000, move list and base/form fallback match the current data contract; optional items lack Scent flag and do not automatically bypass Hyper gates.'),
 'Ribbon-1':('partial',[('08','§3.1'),('21','ribbons/display attributes')], 'Identity/name/icon/description consumers mapped and all actual records read. Raw constructor fallbacks and unused arbitrary flags are not a full current catalog; no award workflow inferred from the names.'),
 'Encounter-1':('supported',[('03','§3.2'),('62','§5.3')], 'Exact existence vs fallback query and version enumeration defect are explicitly covered. Negative-version export is a separate partial lifecycle capability.'),
 'TrainerType-1':('partial',[('24','§5.1'),('51','§2')], 'Gender aliases, BaseMoney and SkillLevel schema all read; numeric AI bands are explicit. Exact spelling/case aliases and absent SkillLevel=BaseMoney are more specific than a generic gender/skill field name.'),
 'TrainerType-2':('supported',[('15','trainer resources')], 'Outfit-before-base resources, trainer front/back/map icon and brief charset rules match the resource consumer contract; unknown identity returns no resource.'),
 'TrainerType-3':('partial',[('24','§5.1; §5.4'),('51','§2'),('08','§3.1')], 'Gender2/money30/skill-from-money, no raw audio defaults and skill-equal-base suppression were reviewed. Full constructor/output defaults remain finer than current prose; battle audio empty/nil differences are explicitly covered elsewhere.'),
 'Trainer-1':('partial',[('03','§3.2; §5.2'),('18','§4.3'),('24','§5')], 'Triple identity, member fields, overwrite and constraints reviewed. Six-column IV/EV order remains004; complete exact schema/alias description is not supplied by the responsibility list.'),
 'Trainer-2':('supported',[('03','§3.2'),('08','§3.1–3.2')], 'Typed type/name, exact triple, strict unknown failure and name/lose-text hash linkage match; direct record construction zero-fill is kept separate from compiler repeat-first and NPC level-based defaults.'),
 'Trainer-3':('partial',[('18','§4.3'),('24','§5'),('19','ordinary derivation versus overrides')], 'GR5-M01-006 retains absent slot/gender/shiny/Nature-overlay gap. First matching rival string and named IV/EV formulas are supported; no blanket PID-default claim.'),
 'Trainer-4':('partial',[('04','§5.5'),('demo-dx/wp73-a-content-editors.md','§6')], 'Exact false/nil/empty omissions, gender labels and ordinary-Shiny suppression under SuperShiny remain serializer details; six-column order linked to004.'),
 'Metadata-1':('partial',[('24','§3–5'),('27','PC initialization'),('61','blackout return destination'),('08','§3.1')], 'All13 fields and source defaults reviewed. Start money is copied directly, PC entries add one each, Home and localized storage author have explicit consumers; not every missing/empty default or specialized compile check is in the published field catalog.'),
 'PlayerMetadata-1':('supported',[('24','§3.3'),('61','blackout return destination'),('03','§3.2')], 'Unknown identity→1 and all seven charset fallback links match the explicit current table; empty strings do not activate absence fallback. Player Home takes priority in the inspected return consumer.'),
 'MapMetadata-1':('supported',[('12','terrain/vehicle consumers'),('14','§3'),('59','time/weather/field moves'),('63','§3'),('62','§5.3')], 'All24 authored fields and every actual69-record value mapped to bounded consumers, including map shape length vs occupied-mask and point first-vs-union differences. Geometry/assets and complete map-event behavior are not certified.'),
 'MapMetadata-2':('partial',[('08','§5.1'),('11','map names'),('65','continue preview')], 'Localized/raw name fallback is supported; in-place PN substitution can mutate shared translation/raw map name and affect later renaming reads. Current display prose does not define the repeated-read mutation boundary; retained as unresolved shared observation.'),
 'DungeonTileset-1':('partial',[('03','§3.2'),('14','§3.2; §8')], 'Nonempty registry first-record fallback matches. Empty registry instead reaches strict nil validation; current unqualified fallback/no-error wording needs a nonempty prerequisite.'),
 'DungeonTileset-2':('partial',[('14','§3.4; §5.1')], 'All four wall offset matrices were compared cell by cell and match. Autotile and Tile arrays are both required by construction although no dedicated schema validation enforces their presence; omission can fail before a usable record.'),
 'DungeonTileset-3':('supported',[('14','§5.1–5.2')], 'Missing layout type0, random registered tile, autotile adjacency, large-tile parity and thin-north adjustment match the current independent tables/rules.'),
 'DungeonTileset-4':('partial',[('04','§5.5'),('14','§5.1')], 'Original-origin-only serialization and autotile/normal inverse numeric projection read; current authoring contract does not fully enumerate these export filters.'),
 'DungeonParameters-1':('supported',[('03','§3.2'),('14','§3.2–3.3')], 'All16 fields and unknown area/version unregistered-default fallback match; positive schema fields do not imply percentage<=100 or geometrically valid layouts.'),
 'DungeonParameters-2':('supported',[('14','§3.3; §4.2')], 'Every default, min/max room behavior, inclusive random interval and center offset match the current table. No random generator executed.'),
 'DungeonParameters-3':('partial',[('04','§5.5'),('14','§3.3')], 'Grouped output and nonpositive-version omission are reviewed but finer than general export prose; field semantics/defaults themselves match.'),
 'PhoneMessage-1':('supported',[('03','§3.2; §5.2'),('04','§4.2'),('63','§5.3')], 'Ten repeatable categories, string Default identity and symbol/triple existence mismatch agree with the detailed current duplicate contract.'),
 'PhoneMessage-2':('supported',[('03','§3.2'),('63','§5.3')], 'Separate contact queries and current-version→initial-version→direct default record fallback match; nil category default is handled by the consumer, not a new record.'),
 'PhoneMessage-3':('partial',[('04','§5.5'),('63','§5.3')], 'Default header versus contact raw type/name/positive-version joining reviewed. Embedded comma or nonpositive-version serialization is not completely specified by the general writer summary.'),
}
# Disambiguate every shared domain path rather than relying on glob ordering.
paths.update({'16':F+'engine-overworld/wp16-world-rendering-and-visual-transitions.md','21':F+'pokemon-rules/wp21-dynamic-forms-and-display.md','51':F+'combat-requirements/wp51-ai-action-selection-and-skill.md',
              '66':F+'user-interface/wp66-c-bag-item-storage-and-shop-ui.md','67':F+'user-interface/wp67-a-battle-interaction-and-presentation.md',
              '73':F+'demo-dx/wp73-b-world-editors.md'})
rows['Move-3'][1][0]=('user-interface/wp66-a-party-and-summary-ui.md','move presentation')
rows['Item-1'][1][1]=('demo-dx/wp73-a-content-editors.md','item fields and properties')

d=s.read('source-to-spec.json')
for c in d['capabilities']:
    suffix=c['capability_id'].removeprefix('M01-DATA-')
    if suffix not in rows:continue
    status,refs,comparison=rows[suffix]
    c.update(status=status,spec_anchors=[anchor(*x) for x in refs],current_contract_comparison=comparison,
             semantic_comparison_complete=True,pending=[],open_consumer_or_data_review=None,
             supported_boundary='supported_static only for the named data/field/consumer projection; no full consumer-domain, assets, host or runtime certification.',
             evidence_level='supported_static' if status=='supported' else 'static_semantic_comparison')

fixed={
 'BodyShape':('partial',[('user-interface/wp66-b-storage-and-pokedex-ui.md','§7–9')], 'All14 identities and icon0–13 registration plus actual filter consumer read. Current search behavior does not supply the complete identity/icon catalog; not inferred from the word shape.'),
 'BodyColor':('partial',[('user-interface/wp66-b-storage-and-pokedex-ui.md','§7–9')], 'All10 identities and order read; current search describes color filtering but not the full ordered data catalog.'),
 'Habitat':('partial',[('18','§3.2'),('03','§6–7')], 'All10 identities/default None and export omission read. This species habitat enum is not the Pokedex Area encounter-map computation; no located ordinary dedicated gameplay consumer was inferred from the category name.'),
 'Stat':('partial',[('19','§2; §3.5'),('demo-dx/wp73-a-content-editors.md','§3.5')], 'Eight identities and three enumerator subsets read; PBS position differs from declaration/formula order. Candidate004; characteristic and Hidden Power orders are correctly separate consumers.'),
 'Nature':('supported',[('19','§3.5 complete tableN; §5.4–5.5')], 'All25 ordered identities, five neutral cases, all20 raised/lowered pairs and persistent/stat-override consumers match; language display remains WP08.'),
 'Status':('supported',[('44','major status contract'),('user-interface/wp66-a-party-and-summary-ui.md','status icons')], 'Six identities and all icon/animation fields reviewed; fainting/Pokerus asset-tail icons are not additional registered status identities.'),
 'TerrainTag':('supported',[('12','complete terrain table'),('03','§3.2'),('36','terrain encounter predicates')], 'All18 numeric/symbol identities and every Boolean/environment field match; None and NoEffect differ in resolution despite their false fields, and surf-free excludes falls/crest.'),
 'Weather':('supported',[('16','§5.1.1'),('59','weather gameplay categories')], 'All9 identities, category groups, graphic lists, velocity numbers and tone formulas match the complete current weather table; nil/no-procedure behavior is neutral tone.'),
 'EncounterType':('supported',[('36','§3.3')], 'All26 identities/default probabilities and land/cave/water flags match; actual data overrides and nonpositive writer omission are separate projections.'),
 'Environment':('supported',[('combat-requirements/wp47-a-attributes-targeting-calling-data.md','environment mappings'),('user-interface/wp67-a-battle-interaction-and-presentation.md','environment base resources')], 'All19 identities and seven graphic-suffix choices read and compared to the calling/presentation mappings; environment does not imply weather or terrain.'),
 'BattleWeather':('supported',[('45','weather states'),('user-interface/wp67-a-battle-interaction-and-presentation.md','weather animation presentation')], 'All9 identities and named animations reviewed; None has no animation. Duration/suppression rules belong to independent combat consumers.'),
 'BattleTerrain':('supported',[('45','terrain states'),('user-interface/wp67-a-battle-interaction-and-presentation.md','terrain presentation')], 'All5 identities and four animation identities match; registry itself does not establish grounding or duration.'),
 'Target':('supported',[('combat-requirements/wp47-a-move-attributes-targeting-and-calling.md','§5.1'),('40','target selection and PP/Pressure')], 'All18 records, target count and all Boolean metadata compared. UserAndAllies num2/range differs from affects-all metadata; None/User/side records do not automatically create per-target lists.'),
}
for c in d['capabilities']:
    suffix=c['capability_id'].removeprefix('M01-FIXED-')
    if suffix not in fixed:continue
    status,refs,comparison=fixed[suffix]
    c.update(status=status,spec_anchors=[anchor(*x) for x in refs],current_contract_comparison=comparison,
             semantic_comparison_complete=True,pending=[],open_consumer_or_data_review=None,
             supported_boundary='supported_static for fixed registry and named consumer projection; no reference/model execution.',
             evidence_level='supported_static' if status=='supported' else 'static_semantic_comparison')
s.write('source-to-spec.json',d)

for name,path,n,comparison,refs,status in [
 ('GrowthRate','001_GrowthRate.rb',188,'All6 registrations and606 table cells including six index0 sentinels were read, together with all6 outside-table formulas. Maximum clamp precedes table-vs-formula choice; invalid level returns an error value, invalid exp fails while constructing diagnostics. All current WP30 clauses were compared. The600 positive-level cells were NOT independently recomputed by a behavior model; historical arithmetic PASS was not reused. This is a literal-table/algorithm static review, not a new600-vector execution.', [('30','§3.1–3.2')],'supported'),
 ('GenderRatio','002_GenderRatio.rb',83,'All8 registrations read. Three fixed-sex/genderless identities have nil female probability; five mixed thresholds32/64/128/192/224 match the actual PID-low-byte consumer and WP19. Nil probability defines single-gendered; no independent random roll inferred from comments.', [('19','§3.2')],'supported'),
 ('EggGroup','003_EggGroup.rb',101,'All15 ordered identities and defaults read. Undiscovered and Ditto have dedicated breeding eligibility/parent-selection semantics; ordinary groups use intersection. Species lists and current breeding contracts were compared, including same-gender/Ditto and no-hatch eligibility gates.', [('33','compatibility'),('34','parent/species selection')],'supported'),
]:
    o.cap('M01-FIXED-'+name,'Data/Scripts/010_Data/001_Hardcoded data/'+path,[[1,n]],comparison,[anchor(*r) for r in refs],status)

o.progress('完成50组数据记录方法与13组已登记固定规则的逐项合同比较，并补齐成长率/性别比例/蛋组的独立映射。成长表606个字面单元均已读；未执行600项重算，也不沿用历史算术PASS。','配置余部、主规格反向映射和字段级状态同步')
print('Data decisions:',len(rows),'existing fixed decisions:',len(fixed),'additional fixed registries:3')
