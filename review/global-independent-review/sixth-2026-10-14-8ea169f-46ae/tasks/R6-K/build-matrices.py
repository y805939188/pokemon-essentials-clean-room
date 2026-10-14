"""Administrative expansion of manually authored, freshly read review units.

This does not inspect behavior or decide PASS. Missing bindings stay pending.
All source ranges must have actual own reading or an explicitly imported owner.
"""
from pathlib import Path
import json, re, hashlib, datetime, collections

P = Path(__file__).parent
BASE = P.parent.parent
INV = json.loads((P / 'active-inventory.json').read_text())
LEDGER = [json.loads(x) for x in (P / 'reading-ledger.jsonl').read_text().splitlines()]
SRC = {Path(x['path']).name: x['path'] for x in INV['source']}
SPEC = {Path(x['path']).name: x for x in INV['formal']}
UNITS = []

def refs(*values):
    result=[]
    for value in values:
        name, first, last = value.rsplit(':',2)
        path=SRC.get(name,name)
        if not Path(path).is_file(): raise ValueError('Nonexistent source binding: '+path)
        total=len(Path(path).read_text().splitlines())
        if not (1<=int(first)<=int(last)<=total): raise ValueError('Invalid source binding: '+value)
        result.append({'path':path,'start_line':int(first),'end_line':int(last)})
    return result

def add(doc, start, end, name, fact, sources, consumers=(), prerequisite=None,
        status='SOURCE_STATIC_SUPPORTED', owner=None):
    s=SPEC[doc]
    if isinstance(sources,str): sources=(sources,)
    if isinstance(consumers,str): consumers=(consumers,)
    UNITS.append({'id':f'K-U{len(UNITS)+1:03d}','formal_path':s['path'],
        'start_line':start,'end_line':end,'name':name,'new_fact':fact,
        'source_refs':refs(*sources),'necessary_consumer_refs':refs(*consumers),
        'prerequisites':prerequisite or 'The clause is limited to its stated entry, valid content and dependency objects; completed prefix writes are retained on a later failure. No plugin overwrite is assumed. Host/UI/media behavior is not executed.',
        'status':status,'imported_owner':owner,
        'evidence':'IMPORTED_SOURCE_STATIC' if owner else 'SOURCE_STATIC',
        'execution':'NOT_EXECUTED_THIS_MAPPING','final_required_authority':'ROOT_WITH_NON_PROPOSER_COUNTER'})

def endunits(doc, start, sources, fact='Purpose, dependency, example and unknown clauses preserve the named scope and static-only evidence; they do not turn reading into host validation.', owner=None):
    add(doc,start,SPEC[doc]['lines'],'Scope and limitations',fact,sources,
        status='NAMED_SCOPE_DISPOSITION',owner=owner)

# Generic configuration, identity, notifications, persistence and files.
add('wp02-rule-configuration-and-data-variants.md',1,172,'Main configuration dictionary',
    'The 524-line default setting file defines values and generation-derived switches. Configuration existence does not prove a variant is active or a consumer uses every setting.',('001_Settings.rb:1:524',))
add('wp02-rule-configuration-and-data-variants.md',173,212,'Battle configuration interface',
    'Battle settings are a separate 30-constant input family; the primary combat reviewer must bind this table and its consumers.',(),status='FOREIGN_SOURCE_BINDING_PENDING',owner='R6-C')
add('wp02-rule-configuration-and-data-variants.md',213,237,'Variant discovery interface',
    'Source-side schemas enumerate content identities and author files; compilation/discovery and filesystem candidate inventory require the delegated DX/data evidence.',('001_GameData.rb:1:283',),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-DX/R6-D')
add('wp02-rule-configuration-and-data-variants.md',238,245,'Language choice by parsed data',
    'Language candidates come from settings. Startup uses parsed save-data emptiness, not an unconditional equivalence with file absence; player language tools return an index.',('001_Settings.rb:423:433','001_Utilities.rb:603:610','reference/pokemon-essentials/Data/Scripts/003_Game processing/001_StartGame.rb:1:126'))
endunits('wp02-rule-configuration-and-data-variants.md',246,('001_Settings.rb:1:524',))
add('wp03-content-identity-and-schema.md',1,88,'Registry identity and class exceptions',
    'Three common registry families differ in accepted identifier types and strict/loose lookup; species, encounter, trainer, phone and dungeon override normal matching. Load replaces registered data rather than refreshing all consumers.',('001_GameData.rb:1:283','008_Species.rb:1:158','013_Encounter.rb:1:71','015_Trainer.rb:1:70','021_PhoneMessage.rb:1:100','019_DungeonTileset.rb:1:222','020_DungeonParameters.rb:1:135'))
add('wp03-content-identity-and-schema.md',89,117,'Content defaults and read side effects',
    'Constructors provide per-field defaults and translated display fields; explicit false/zero differ by field. Species evolution extraction has a nested-parameter mutation recorded by KL29; construction defaults are not editor limits.',('006_Item.rb:1:270','008_Species.rb:1:455','017_PlayerMetadata.rb:1:95','018_MapMetadata.rb:1:138','004_Ability.rb:1:45','012_Ribbon.rb:1:48'))
add('wp03-content-identity-and-schema.md',118,194,'Author schema, enums and six columns',
    'Schemas expose field shape and reference identities, while parsing/compile behavior and explicit six-column writer transformations need current DX/data input; schema alone is insufficient proof of accepting a literal.',('001_GameData.rb:1:283','005_Move.rb:1:408','006_Item.rb:1:270','008_Species.rb:1:455','015_Trainer.rb:1:213'),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-DX/R6-D')
add('wp03-content-identity-and-schema.md',195,263,'Fixed hardcoded species descriptors',
    'The full body-shape14/body-color10/habitat10 identity sets are registered hardcoded content; these identifiers do not imply a future architecture.',('004_BodyShape.rb:1:116','005_BodyColor.rb:1:78','006_Habitat.rb:1:76','008_Stat.rb:1:119','009_Nature.rb:1:173'))
add('wp03-content-identity-and-schema.md',264,310,'Content field responsibility directory',
    'All 010_Data definitions have been newly read. Creature/stat/battle/environment/phone/dungeon fields retain the named downstream ownership; constructor/schema/default behavior is distinct from runtime consumer semantics.',tuple(f"{x['path']}:1:{x['lines']}" for x in INV['source'] if '/010_Data/' in x['path']))
endunits('wp03-content-identity-and-schema.md',311,('001_GameData.rb:1:283',))
add('wp05-events-extensions-plugins.md',1,54,'Event arity, identity lookup and interrupted dispatch',
    'Lists deduplicate callback identity; named keys overwrite. Arity<=2 receives sender plus remainder. Direct handlers precede conditional registrations; removing a same-named direct key does not remove a condition. Uncaught callback failure stops later callbacks, retaining earlier writes.',('005_Event_Handlers.rb:1:298','006_Event_HandlerCollections.rb:1:79'))
add('wp05-events-extensions-plugins.md',55,61,'Menu extension dispatch',
    'Menu availability evaluates conditions and order, then callback requests retain passed argument identity; no implicit rollback or host presentation is guaranteed.',('006_Event_HandlerCollections.rb:80:123',))
add('wp05-events-extensions-plugins.md',62,125,'Plugin metadata, dependency and execution stages',
    'Full plugin loader defines required/optional/exact dependency handling, character-position version comparison, cyclic dependency termination, explicit+discovered script order and compiled-product consumption even without source directories.',('005_PluginManager.rb:106:664',),('001_FileTests.rb:4:77','003_Errors.rb:16:94'))
endunits('wp05-events-extensions-plugins.md',126,('005_PluginManager.rb:106:664','005_Event_Handlers.rb:1:298'))
add('wp06-stats-directory.md',1,125,'Declared stats and constructor defaults',
    'All declared stat fields and their initialized defaults are read in the 200-line source. Caller write unit (items, attempts, fruit per plant) remains distinct from field existence and zero initialization.',('012_Game_Stats.rb:1:200','002_Item_Effects.rb:1:1524','004_Item_Phone.rb:1:706'),status='COUNTERPART_WRITER_BINDINGS_PENDING')
endunits('wp06-stats-directory.md',126,('012_Game_Stats.rb:150:200',),'Derived stats query mutable runtime anchors; declarations are not all write sites, and absent writers are named unresolved rather than declared nonexistent.')
add('wp06-time-random-steps-stats.md',1,59,'Clock and runtime play-time queries',
    'Played time accrues only with an existing runtime anchor; average play time preserves integer division for integer stored input. Phone readiness decrements one per distinct eligible wall-clock second; incoming phone counts frame delta.',('012_Game_Stats.rb:161:196','004_Item_Phone.rb:118:144','004_Item_Phone.rb:543:560'),status='PARTIAL_SUPPORTED_WORLD_CLOCK_BINDING_PENDING',owner='R6-O')
add('wp06-time-random-steps-stats.md',60,81,'Destructive wall-clock variable timer',
    'Seconds clamp nonpositive to zero. Days helper stores the historical arithmetic duration, and validation keeps only strictly expired positive timers; any early/zero query destroys the record through the variable-write helper.',('001_Utilities.rb:157:193','001_Utilities.rb:510:523'))
add('wp06-time-random-steps-stats.md',82,108,'General movement/stat writer interface',
    'Stat constructor records the default counters; ordinary step increment and forced/interpreter branch are owned by the world reviewer, including 31-bit wrap before callbacks.',('012_Game_Stats.rb:1:149',),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-O')
add('wp06-time-random-steps-stats.md',109,134,'Ordinary random overloads',
    'Numeric endpoints use an inclusive difference; a Range wins over the second argument, strings are not parsed, and zero numeric underlying random differs from a positive-integer domain.',('002_RubyUtilities.rb:366:388',))
add('wp06-time-random-steps-stats.md',135,152,'Dungeon seed and replay consumers',
    'The generic random overload does not prove replay/dungeon consumers; seed-clear-before-size-check and recorded random order require current world/combat source bindings.',('002_RubyUtilities.rb:366:388',),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-O/R6-C')
add('wp06-time-random-steps-stats.md',153,165,'Biased unseen-value cycle',
    'AntiRandom first chooses from unseen; repeated-value gate can delay coverage. With n2 after0 the seen0 probability is1/7 and unseen1 is6/7; exhausted cycles restart. Invalid sizes remain outside the finite acceptance contract.',('001_Utilities.rb:77:101',))
endunits('wp06-time-random-steps-stats.md',166,('012_Game_Stats.rb:173:196','002_RubyUtilities.rb:366:388'))
add('wp07-deprecation-appendix.md',1,49,'Deprecation warning and alias',
    'Warning first line always emitted; version and alternative lines are optional. Alias construction validates method existence/name, then warning precedes positional/keyword forwarding; an implicit block-forwarding guarantee is absent.',('005_Deprecation.rb:1:52','004_Validation.rb:1:31'))
endunits('wp07-deprecation-appendix.md',50,('005_Deprecation.rb:1:52',))
add('wp07-diagnostics-files-http.md',1,41,'File and directory access entries',
    'Directory recursive deletion removes root only after children; listing and read wrappers catch different errors. Archive content reads do not certify missing-file behavior. A child deletion failure retains completed removals.',('001_FileTests.rb:1:365',))
add('wp07-diagnostics-files-http.md',42,57,'Memory stream state',
    'StringInput preserves historical cursor/EOF/length and close semantics; seeking to end does not immediately set EOF, a read can do so, and double close can replace a block exception.',('001_FileTests.rb:366:484','002_FileMixins.rb:131:149'))
add('wp07-diagnostics-files-http.md',58,70,'Resource candidate and writable surfaces',
    'Bitmap/audio existence and path lookup are candidate requests, not real media observations; file copy/move/save paths have their own ordering and no cross-step atomicity.',('001_FileTests.rb:109:281','002_RubyUtilities.rb:144:174'))
add('wp07-diagnostics-files-http.md',71,87,'Little-endian indexed content protocol',
    '8/16/32-bit reads treat missing bytes as zero at these helpers, writes keep low bytes, signed8 uses two-complement interpretation; indexed offsets/lengths and zero-length content retain precise cursor behavior. Later byte failure retains earlier byte writes.',('002_FileMixins.rb:1:149',))
add('wp07-diagnostics-files-http.md',88,116,'GET/POST transport versus construction',
    'POST alone requires http prefix. Non-Hash responses pass through. Constructing POST keys/escaped data precedes the local host-call rescue, while convenience wrappers rescue the whole call; writing a successful body can fail later.',('003_HTTP_Utilities.rb:1:83',),('002_RubyUtilities.rb:24:61',))
add('wp07-diagnostics-files-http.md',117,168,'Diagnostics, completion marker and Main',
    'Critical wrapper propagates Reset/SystemExit, returns0 after an ordinary error if diagnostic completes, and Main still returns1. Hangup emergency save precedes reset; diagnostic-log write failure is not made harmless. Native UI/clipboard remains unknown.',('003_Errors.rb:1:94','001_PBDebug.rb:1:77','002_DebugConsole.rb:1:233','999_Main.rb:1:60'))
endunits('wp07-diagnostics-files-http.md',169,('003_Errors.rb:1:94','001_FileTests.rb:1:484','003_HTTP_Utilities.rb:1:83'))
add('wp08-localization.md',1,43,'Message domains and language input',
    'MessageTypes registers numeric domains and array/hash/map buckets. Chosen-language game/core files are distinct from default author collection; parsed save-data emptiness controls startup writeback.',('003_Intl_Messages.rb:478:769','001_Utilities.rb:603:610','001_Settings.rb:423:433'),status='PARTIAL_SUPPORTED_UI_WRITEBACK_BINDING_PENDING',owner='R6-UI')
add('wp08-localization.md',44,84,'Lookup precedence, empty values and substitutions',
    'Lookup prefers current game then core, map-specific then bucket0. Empty translated strings are hits. Ordinary placeholder replacement interprets replacement backslashes; formatted replacement follows a separate pathway. No runtime fallback to default author material.',('003_Intl_Messages.rb:589:638','003_Intl_Messages.rb:764:823'))
add('wp08-localization.md',85,108,'Collection and value normalization',
    'Script/event collection uses different string recognition/unescape rules; replace versus append preserve different old materials. Hash keys normalize whitespace separately from output values; source text occurrence does not establish runtime reachability.',('003_Intl_Messages.rb:4:243','003_Intl_Messages.rb:553:588','003_Intl_Messages.rb:644:674'))
add('wp08-localization.md',109,132,'Author extraction and sparse maps',
    'Extraction deletes files before writing but retains directory containers. Combined-map nonempty scan can stop at a missing early bucket; separate mode skips missing/empty buckets and reaches later maps. Export target selection does not change player language.',('003_Intl_Messages.rb:244:375',))
add('wp08-localization.md',133,181,'Import shape, repeated content and destructive output',
    'Import chooses array/hash from first content row, rejects map arrays before divisibility; repeated keys use last value and repeated sparse sections retain unmentioned early entries. Exported empty/hash/comment/bracket/space values can lose representability. Full compile truncates destination before parse, unlike single-file parse.',('003_Intl_Messages.rb:376:477','003_Intl_Messages.rb:214:243','003_Intl_Messages.rb:350:375'))
endunits('wp08-localization.md',182,('003_Intl_Messages.rb:1:823',))
add('wp09-save-startup-continue.md',1,58,'Save value registration and duplicate identity',
    'New value registration appends, even at duplicate identity. Saved hash keeps later value while ordered load can call both callbacks on that same later value. Value type check, loaded flags and boot/newgame filters are distinct.',('001_SaveData.rb:1:82','002_SaveData_Value.rb:1:284'))
add('wp09-save-startup-continue.md',59,82,'Default seventeen save values',
    'Default17 registered values have type constraints and positional old-format extraction; stats reset on new game while settings/system boot values have different reuse gates.',('004_Game_SaveValues.rb:1:127','002_SaveData_Value.rb:195:284'))
add('wp09-save-startup-continue.md',83,94,'Variables and switches external implementation',
    'Saved overall variables/switches objects do not alone prove their raw slot false/nil/zero semantics or numbered limits; current world owner source binding is required.',('004_Game_SaveValues.rb:1:127',),status='FOREIGN_CONSUMER_BINDING_PENDING',owner='R6-O')
add('wp09-save-startup-continue.md',95,120,'Startup and progress split',
    'Main critical path completion differs from host exit. System setup reads parsed save data and prepares language/settings before progress; newgame/continue substantive UI restoration is delegated.',('999_Main.rb:1:60','reference/pokemon-essentials/Data/Scripts/003_Game processing/001_StartGame.rb:1:126','002_SaveData_Value.rb:245:284'),status='PARTIAL_SUPPORTED_UI_BINDING_PENDING',owner='R6-UI')
add('wp09-save-startup-continue.md',121,153,'Save collection and startup recovery callers',
    'Save hash collection validates before file-open, while normal IO/system write rescue and count rollback belong to game save consumer. Generic low-level save does not promise backup/atomic recovery.',('001_SaveData.rb:24:82','002_SaveData_Value.rb:279:284'),status='PARTIAL_SUPPORTED_UI_BINDING_PENDING',owner='R6-UI')
endunits('wp09-save-startup-continue.md',154,('001_SaveData.rb:1:82','002_SaveData_Value.rb:1:284'))
add('wp10-migration-failure-recovery.md',1,77,'Conversion selection, ordering and writeback',
    'Conversion gates compare saved versions, select essentials before game conversions, make backup before applying and only then advance version/write output in full chain. Single-object conversion does not update supplied version context; failures retain completed prefixes.',('003_SaveData_Conversion.rb:1:223','001_SaveData.rb:24:82'))
add('wp10-migration-failure-recovery.md',78,100,'Fourteen named migrations',
    'All420 conversion-registration lines newly read. Bag cursor conversion has a case mismatch: old lastpocket is retained, different-case field cleared, current cursor copied; exact clause88 is GR6-K-001 proposal. Registered-item conversion remains correctly described in WP27.',('005_Game_SaveConversions.rb:1:420','003_SaveData_Conversion.rb:195:223'),status='GR6-K-001_PROPOSAL_COUNTER_SUPPORTED')
add('wp10-migration-failure-recovery.md',101,210,'Old frame stats and plant conversion',
    'Old frames divide by40. Complete64 berry/4mulch lookup identities, six/seven/eight slot conversion ordering and already-written prior entries are preserved; malformed single reconstruction is distinguished from full selective chain.',('005_Game_SaveConversions.rb:1:206','005_Game_SaveConversions.rb:241:420'),status='PARTIAL_SUPPORTED_BERRY_CONSTRUCTOR_BINDING_PENDING',owner='R6-O')
add('wp10-migration-failure-recovery.md',211,259,'Recovery and emergency-save consumers',
    'Conversion failure, load validation, backup recursion, map restore and Hangup emergency-save are separate layers; no uniform rollback, atomicity or host failure outcome is supplied by SaveData.',('003_SaveData_Conversion.rb:195:223','003_Errors.rb:76:94','999_Main.rb:1:60'),status='PARTIAL_SUPPORTED_UI_WORLD_BINDING_PENDING',owner='R6-UI/R6-O')
endunits('wp10-migration-failure-recovery.md',260,('003_SaveData_Conversion.rb:1:223','005_Game_SaveConversions.rb:1:420'))

# Additional units are authored in the companion; they use the same add function.
exec((P/'matrix-creature-units.py').read_text())
exec((P/'matrix-binding-updates.py').read_text())

den=json.loads((BASE/'inventory/formal-block-denominator.json').read_text())
own={v['path'] for v in INV['formal']}
formal_blocks=[v for v in den if v['path'] in own]
reverse=[]
for b in formal_blocks:
    matches=[u for u in UNITS if u['formal_path']==b['path'] and
             u['start_line']<=b['start_line'] and u['end_line']>=b['end_line']]
    line=Path(b['path']).read_text().splitlines()[b['start_line']-1]
    kind='HEADING_OR_TABLE_STRUCTURE' if re.match(r'^(#|---|\|\s*---|```)',line) else 'CLAUSE'
    overlap=[e for e in LEDGER if e.get('path')==b['path'] and
          not(e['end_line']<b['start_line'] or e['start_line']>b['end_line']) and e.get('acquisition_log')]
    read=list(dict.fromkeys(e['acquisition_log'] for e in overlap))
    covered={i for e in overlap for i in range(e['start_line'],e['end_line']+1)}
    reverse.append({**b,'block_kind':kind,'text_sha256':hashlib.sha256(line.encode()).hexdigest(),
        'fresh_read_logs':read,'unit_ids':[u['id'] for u in matches],
        'actual_read_range_union_complete':all(i in covered for i in range(b['start_line'],b['end_line']+1)),
        'status':'NEW_EVIDENCE_OR_NAMED_DISPOSITION' if matches else 'BINDING_NOT_YET_AUTHORED',
        'disposition_statuses':[u['status'] for u in matches],
        'no_pass_inference':True})
forward=[]
foreign=json.loads((P/'foreign-source-dispositions.json').read_text())
for e in LEDGER:
    if not e.get('path','').startswith('reference/'):continue
    uu=[u for u in UNITS if any(s['path']==e['path'] and not(s['end_line']<e['start_line'] or s['start_line']>e['end_line']) for s in u['source_refs']+u['necessary_consumer_refs'])]
    ff=[f for f in foreign if (e['path'] in f.get('paths',[])
        or e['path'] in f.get('additional_paths',[])
        or (e['path'].startswith(f.get('source_prefix','\0')) and
            not e['path'].startswith(f.get('exclude_prefix','\0'))))]
    forward.append({**e,'source_unit':f"{e['path']}:{e['start_line']}-{e['end_line']}",
        'fact':e['semantic_summary'],'consumer_and_formal_unit_ids':[u['id'] for u in uu],
        'foreign_disposition_ids':[f['id'] for f in ff],
        'disposition':'NAMED_UNITS_AVAILABLE' if uu else 'NAMED_FOREIGN_DISPOSITION' if ff else 'FOREIGN_OR_UNBOUND_FACT_PENDING',
        'no_pass_inference':True})
(P/'named-review-units.json').write_text(json.dumps(UNITS,ensure_ascii=False,indent=2)+'\n')
(P/'reverse-formal-matrix.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in reverse))
(P/'forward-source-matrix.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in forward))
summary={'formal_blocks':len(reverse),'mapped_blocks':sum(bool(x['unit_ids']) for x in reverse),
    'unmapped_blocks':sum(not x['unit_ids'] for x in reverse),'named_units':len(UNITS),
    'statuses':dict(collections.Counter(u['status'] for u in UNITS)),
    'source_read_segments':len(forward),'unbound_source_segments':sum(not x['consumer_and_formal_unit_ids'] and not x['foreign_disposition_ids'] for x in forward),
    'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope':'Administrative mapping is not a new behavioral execution or blanket PASS.'}
(P/'matrix-coverage.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False))
