"""Audit metadata only. Reads literal data; never imports or executes the reference."""
import collections
import review_state as s
import review_ops as o

meanings = [
    'MegaRing flags enumerate permitted ring item identities when the battle is created; the flag is not a mega-stone species/form binding.',
    'Thirteen case-insensitive move predicates consume the corresponding flags. Substitute bypass independently requires generation >=6 and Sound or active Infiltrator. CannotMetronome is a separate candidate filter.',
    'Natural Gift power uses the first matching parameter flag with minimum10; end-of-use consumes a still-held item. The previously read type reader and eligibility gates remain separate.',
    'Fling power is0 without an item, first matching parameter flag with minimum10, otherwise10. Item-specific target effects have their own gates.',
    'Mirror Move requires an existing last regular move carrying CanMirrorMove; successful call uses that move and target.',
    'Metronome samples at most1000 candidates, rejecting blacklist effects, CannotMetronome and Shadow type; no accepted candidate is failure.',
    'AI Mirror Move substitution uses the same existing-record/flag prerequisite and changes only the evaluated move.',
    'AI immunity approximation explicitly reads Bomb for Bulletproof and Sound for Soundproof; other listed abilities use types, with active-ability gate for battler wrappers.',
    'AI authored flags are copied before skill-derived additions; wild rarity sets skill32 only under its setting.',
    'AI AntiX removes X through exact membership, retains AntiX, and does not change numeric skill thresholds32/48/100.',
    'AI held-item ranking reads first Fling parameter, adds1 at80 and another at100, then an independent item-identity effect bonus.',
    'AI Mirror Move failure checks no last move, missing record, then absent CanMirrorMove.',
    'UltraBeast species flag bypasses ordinary ball modifier and divides catch rate by10 unless the ball is Beast Ball.',
    'Beast Ball uses x5 for UltraBeast and division by10 otherwise.',
    'Repel flag builds the repeat-use selection pool after a non-ice step exhausts the counter; possession, confirmation and selection are separate gates.',
    'NoPhoneSignal map flag blocks call permission before contact-specific checks.',
    'Giratina dynamic form is1 with Griseous Orb or DistortionWorld map flag, otherwise0; this is separate from static DefaultForm.',
    'NoName trainer-type flag omits the type prefix from the displayed full trainer name.',
    'DisableBoxLink map flag joins possession and global switch gates at party-screen entry.',
    'Bug contest/reception configuration accepts literal map IDs or string flags expanded over all map metadata; lists are appended and off-limits checks use both lists.',
]
for e, meaning in zip(s.read('flag-consumer-unread-contexts.json')['contexts'], meanings):
    o.source(e['path'], [e['lines']], [dict(lines=e['lines'], entry_or_rule='Flag consumer projection', comparison=meaning)], pending=['Other domain behavior outside the recorded M01 field-consumer projection is not certified.'])
for path, ranges, meaning in [
    ('Data/Scripts/013_Items/001_Item_Utilities.rb', [[636,669],[857,895]], 'EvolutionStone selects per-party eligibility annotations. Apricorn/Fossil wrappers filter the bag, return the selection or nil, and write selected ID or NONE only for a positive variable ID.'),
    ('Data/Scripts/013_Items/002_Item_Effects.rb', [[380,403]], 'EvolutionStone selects the generic item-evolution handler; Shadow rejects before evolution eligibility and UI.'),
    ('Data/Scripts/013_Items/006_Item_Mail.rb', [[32,67]], 'IconMail independently permits up to three stored creature-image entries; plain Mail classification does not imply these images.'),
    ('Data/Scripts/011_Battle/005_AI/009_AITrainer.rb', [[1,39],[64,73],[97,100]], 'Full AI trainer skill and flag lifecycle completed; initialization0, type skill or configured wild rarity32, positive/medium/best additions, Anti filtering and32/48/100 thresholds.'),
]:
    o.source(path, ranges, [dict(lines=ranges[0], entry_or_rule='Indirect flag consumer', comparison=meaning)])

definitions = {
 'abilities': {'FasterEggHatching': ('WP35', 'Party ability scan accelerates the hatch-step decrement; it is not a species hatch-step default.')},
 'pokemon': {
  'Legendary': ('WP36/WP51', 'Configured wild creation guarantees three maximum IVs; configured wild AI rarity selects skill32.'),
  'Mythical': ('WP36/WP51', 'Same two separately gated wild-only projections as Legendary.'),
  'UltraBeast': ('WP36/WP38/WP51', 'Wild IV and AI rarity projections plus the special ball catch-rate branch.'),
  'InheritFormFromMother': ('WP34', 'Inheritance chooses the species-determining parent form before later form rules.'),
  'InheritFormWithEverStone': ('WP34', 'Everstone form inheritance uses eligible parent and offspring-family checks; spelling is case insensitive.'),
 },
 'map_metadata': {
  'BugContest': ('WP54', 'Actual flag used by string-based contest map registration.'),
  'BugContestReception': ('WP54', 'Actual flag used by string-based reception registration; not interchangeable with contest map membership.'),
  'DisableBoxLink': ('WP66A', 'Blocks remote storage permission when party screen opens.'),
  'DistortionWorld': ('WP21', 'Giratina dynamic-form input.'),
  'IceRock': ('WP31/WP32', 'LocationFlag evolution parameter matched against current map metadata.'),
  'Magnetic': ('WP31/WP32', 'LocationFlag evolution parameter matched against current map metadata.'),
  'MossRock': ('WP31/WP32', 'LocationFlag evolution parameter matched against current map metadata.'),
  'ScaleWildEncounterLevels': ('WP36', 'Optional wild-created callback scales the generated level; not the raw encounter table value.'),
 },
 'items': {
  'Apricorn': ('WP27/WP66C', 'Category predicate and filtered bag-choice wrapper; does not itself implement crafting.'),
  'Berry': ('WP27/WP28/WP47/WP50/WP60', 'Category predicate consumed by eligibility and berry interactions; a berry name alone does not supply an effect handler.'),
  'EvolutionStone': ('WP28/WP31', 'Generic evolution-item handler and party eligibility annotation.'),
  'Fossil': ('WP27/WP66C', 'Category predicate and filtered choice wrapper; does not itself create a revived species.'),
  'IconMail': ('WP64', 'Counts as mail and enables stored creature icons in mail display.'),
  'KeyItem': ('WP27/WP28/WP66C', 'Important-item classification affects holdability, consumability, and quantity semantics.'),
  'MegaRing': ('WP22', 'Enumerated as a ring item at battle construction; stone binding is separate species data.'),
  'MegaStone': ('WP22/WP27', 'Exposes a category predicate; the only located same-name predicate call outside its declaration is in a disabled display block. Active mega eligibility uses species stone/move requirements.'),
  'Mulch': ('WP60', 'Berry-plant selection and application category gate.'),
  'PokeBall': ('WP38', 'Ball classification; Snag state additionally depends on player equipment or explicit SnagBall flag.'),
  'Repel': ('WP28/WP36', 'Builds the repeated-use selection pool after repel expiry.'),
  'TypeGem': ('WP43/WP50', 'Gem category used by battle modifiers and consumption; elemental effect handlers are separately registered.'),
 },
 'moves': {k: v for k,v in [
  ('Biting',('WP48','Strong Jaw power factor1.5.')), ('Bomb',('WP48/WP51','Bulletproof immunity and AI absorption approximation.')),
  ('CanMirrorMove',('WP47A/WP51/WP52C','Eligibility of target last regular move for actual and predicted Mirror Move.')),
  ('CanProtect',('WP40/WP47A','Permission for relevant protect barriers to stop the move.')),
  ('CannotMetronome',('WP47A','Exclusion from Metronome sampled candidates.')),
  ('Contact',('WP48/WP50','Raw contact metadata; actual contact may separately be disabled by Long Reach, while Tough Claws reads the raw flag.')),
  ('Dance',('WP49','Dancer trigger classification.')), ('HighCriticalHitRate',('WP43','Adds one critical-hit stage after prior forced/prohibited critical checks.')),
  ('Powder',('WP40/WP48','Powder immunity consumers; grass setting and generation>=6 Overcoat/Goggles are distinct gates.')),
  ('Pulse',('WP48','Mega Launcher power factor1.5.')), ('Punching',('WP48','Iron Fist power factor1.2.')),
  ('Sound',('WP40/WP47A/WP48','Soundproof, sound-based move rules, and generation>=6 substitute bypass.')),
  ('ThawsUser',('WP40/WP46','User thaw eligibility; target thaw and AI prediction retain their own generation gates.')),
  ('TramplesMinimize',('WP43/WP52','Minimize damage bonus and generation>=6 perfect accuracy; AI projection separately recorded.')),
 ]},
}
records = {}
for file in s.read('pbs-data-inspection.json')['files']:
    d=s.read(file['record_review_artifact'])
    for r in d['records']:
        for prop in r.get('properties', []):
            if prop['key']!='Flags': continue
            for flag in [x.strip() for x in prop.get('data_value','').split(',') if x.strip()]:
                key=(d['family'],flag)
                records.setdefault(key, []).append(dict(path=d['path'], record_key=r['record_key'], line=prop['line']))
rows=[]
for (family,flag),occ in sorted(records.items()):
    domain=family if family!='pokemon_forms' else 'pokemon'
    if flag.startswith('NaturalGift_'):
        owner,rule='WP47A', 'First matching parameter flag supplies registered type and numeric power; type validation retains captured case, power minimum10. All actual profile atoms and the current67-row appendix were compared.'
    elif flag.startswith('Fling_'):
        owner,rule='WP47B/WP51', 'First matching flag supplies power with minimum10; AI ranking separately uses raw thresholds80/100. All actual profile atoms and the current578-row appendix were compared.'
    elif flag.startswith('DefaultForm_'):
        owner,rule='WP18/WP21', 'First matching numeric flag determines base/default form. A corresponding explicit form record is not required; form lookup can fall back to base.'
    else:
        match=next((v for k,v in definitions[domain].items() if k.lower()==flag.lower()),None)
        assert match, (family,flag)
        owner,rule=match
    rows.append(dict(family=family,flag=flag,consumer_owner=owner,consumer_semantics=rule,occurrences=occ,
                     semantic_review='reviewed_actual_flag_consumer_projection',evidence_level='supported_static',
                     boundary='No independent full-domain or runtime certification. Precise setting-cutoff gaps remain in configuration-branch-reviews.json.'))
s.write('flag-consumer-contracts.json',dict(schema_version='gr5.review.v1',module='M01',source_baseline=s.R,
    classification='Shared field contract; rows are flag values, not additional capabilities.',
    discovery='All has_flag? and flag collection/predicate references searched in fixed Scripts; indirect item category callers inspected. No plugin/demo absence inferred.',
    rows=rows))
o.progress('完成全部实际Flags值的消费者归属表；补读20组直接上下文及物品分类间接调用。MegaStone分类在已定位核心调用中仅见停用显示分支，未冒充实际Mega资格规则。','收束主责编译/翻译能力的逐条现行合同映射及残余边界候选')
print('Actual flag values mapped:',len(rows))
