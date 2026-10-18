"""Serialize this reviewer's manually adjudicated facts after actual reading.

Inventory, record bindings and locators generated here are not semantic review.
No reference Ruby, game, compiler, model, or serialized object is executed.
"""
import collections, datetime, hashlib, json, pathlib, re, subprocess

HERE = pathlib.Path(__file__).resolve().parent
REPORT = HERE.parent.parent
B = pathlib.Path('/workspace/pokemon-essentials-clean-room')
R = pathlib.Path('/workspace/pokemon-essentials')
BC = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
RC = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
BT = '751dfde81048c81390f89a65ca1d1a565ba8e1ca'
FT = 'f292698cdd4a8e725525a9be6dc34b75faaf151e'
RT = '7589c800b61ba13a13040ed0d686979b80a84fd0'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
READER = '/root/pbs_battle'

def readj(p): return json.loads(p.read_text())
def dump(n,x): (HERE/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def ident(root, rel, commit=None):
    raw=(root/rel).read_bytes()
    d={'repo':str(root),'path':rel,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
       'blob':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),
       'lines':len(raw.decode('utf-8-sig').splitlines())}
    if commit:
        frozen=subprocess.check_output(['git','show',f'{commit}:{rel}'],cwd=root)
        d.update(commit=commit,workspace_tree=RT if root==R else BT,
                 formal_tree=FT if root==B and rel.startswith('deliverables/final-specification-set/') else None,
                 matches_frozen_bytes=frozen==raw)
        assert frozen==raw,rel
    return d

primary = readj(REPORT/'delegation/readsets/pbs_battle.json')['reference']
rawio=[json.loads(x) for x in (HERE/'read-io/index.jsonl').read_text().splitlines()]
pbsio=[json.loads(x) for x in (HERE/'read-io/pbs-index.jsonl').read_text().splitlines()]
associations={
 'PBS/Gen 8 backup/abilities.txt':'PBS/abilities.txt',
 'PBS/Gen 8 backup/moves.txt':'PBS/moves.txt',
 'PBS/Gen 6 backup/types.txt':'PBS/types.txt',
 'PBS/Gen 7 backup/types.txt':'PBS/types.txt',
 'PBS/Gen 8 backup/types.txt':'PBS/types.txt'}
source_ids={
 'REG':'Data/Scripts/010_Data/001_GameData.rb',
 'TYPE':'Data/Scripts/010_Data/002_PBS data/003_Type.rb',
 'ABILITY':'Data/Scripts/010_Data/002_PBS data/004_Ability.rb',
 'MOVE':'Data/Scripts/010_Data/002_PBS data/005_Move.rb',
 'ITEM':'Data/Scripts/010_Data/002_PBS data/006_Item.rb',
 'TARGET':'Data/Scripts/010_Data/001_Hardcoded data/017_Target.rb',
 'COMPILER':'Data/Scripts/021_Compiler/001_Compiler.rb',
 'COMPILE_PBS':'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb',
 'WRITE_PBS':'Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb',
 'FACILITY':'Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb',
 'START':'Data/Scripts/003_Game processing/001_StartGame.rb',
 'MAIN':'Data/Scripts/999_Main/999_Main.rb',
 'PKMOVE':'Data/Scripts/014_Pokemon/004_Pokemon_Move.rb',
 'BTMOVE':'Data/Scripts/011_Battle/003_Move/001_Battle_Move.rb',
 'AIMOVE':'Data/Scripts/011_Battle/005_AI/011_AIMove.rb',
 'SETTINGS':'Data/Scripts/001_Settings.rb',
 'BSETTINGS':'Data/Scripts/002_BattleSettings.rb'}
formal_ids={
 'WP02':'deliverables/final-specification-set/generic-kernel/wp02-rule-configuration-and-data-variants.md',
 'WP03':'deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md',
 'WP04':'deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md',
 'KCAT':'deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md',
 'WP43':'deliverables/final-specification-set/pokemon-rules/wp43-types-accuracy-and-damage.md'}

# These facts are written by the actual reader. Loops below only bind their
# already adjudicated meanings to individually read records and exact fields.
facts=[
 ('PB01','Discovery and alternative activation',
  'Ordinary discovery scans PBS root *.txt only, matches exact base or base_ suffix after longest-base ordering. Gen5–8 subdirectories are author alternatives, not simultaneous or automatically active registries. Explicit facility Trainers/Pokemon paths bypass generic basename discovery. A copied backup remains subject to current schema, dependencies, code and settings; changing its directory name does not recompute loaded settings constants.',
  ['COMPILER:get_all_PBS_files_to_compile/compile_PBS_files','SETTINGS:17','BSETTINGS:derived declarations'],['WP02 §6','WP04 §4.1','KCAT KC04/KL17']),
 ('PB02','Lexical and schema collection',
  'First-line BOM removal, physical comment/blank skip and subsequent first-# suffix deletion precede ordinary attribute collection. A space followed by # within ordinary section becomes invalid empty attribute, unlike specialized prepped-line loops. Ordinary repeated attributes overwrite; ^ fields accumulate; valid unknown schema attributes are ignored. Fixed schema ignores excess tail, q consumes preprocessed original string. Escaped-quote marker removal is positional; ordinary CSV quotation is not a general unquote guarantee.',
  ['COMPILER:prepline/pbEachFileSectionEx/split_csv_line/pbGetCsvRecord'],['WP03 §5','WP04 §4.2','KCAT KL06–13/KL33–35/KL46–50']),
 ('PB03','Registry identity and incomplete compile',
  'String IDs normalize to Symbol, comparisons and enum membership are exact; no STICK→LEEK or VICEGRIP→VISEGRIP alias is supplied by generic registry. get unknown raises; try_get unknown/nil returns nil, but wrong types fail validation. Direct register replaces same key; ordinary compiler duplicate gate rejects before second registration. Clear and successful prefix registrations occur before whole-table validation/save. Failure does not itself undo earlier in-memory registrations.',
  ['REG:ClassMethodsSymbols','COMPILE_PBS:compile_PBS_file_generic'],['WP03 §3/§5.2','WP04 §4.3','KCAT KR07/KR16/KL14–16/KL36–37']),
 ('PB04','Four schema families and defaults',
  'Each actual author field is parsed by its declared schema. Type references and Move Type/Target and Item Move are validated against the current registered dependency, not the English display label. Missing and explicit zero/false remain distinct. All complete defaults and field interpretations are in field-contracts.json; every present and omitted field of all 7704 primary path-records binds that contract in record-field-ledger.json.',
  ['TYPE:SCHEMA/initialize','ABILITY:SCHEMA/initialize','MOVE:SCHEMA/initialize','ITEM:SCHEMA/initialize','TARGET:all18 records','COMPILE_PBS:compile_types/abilities/moves/items'],['WP03 §4.3/§7','WP04 §4.3–4.5','WP43 §8']),
 ('PB05','Move validation and effect identity',
  'Status with positive power rejects before current record registration; Physical/Special with zero or omitted power warns and becomes Status. FunctionCode is author text and is not validated against a move-effect implementation at compile time. Factory resolves exact function name (digit prefix Effect); lawful absent effect falls back to Unimplemented. Missing/nil function uses None, not arbitrary empty or malformed name. Source and formal lawful missing-effect examples already preserve different status-failure and ordinary-damage branches.',
  ['COMPILE_PBS:validate_compiled_move','BTMOVE:34–69','MOVE:initialize','received COM-MOVE R001/R013 and FB01–06'],['WP04 §4.5','WP43 §2.1','KCAT C01F-013/R6-U14-C05','received FB01–06']),
 ('PB06','Types, generation and combat categories',
  'All default19 and Gen5 18 rows read; Gen6/7/8 equal default. QMARKS is pseudo and neutral in supplied table, not universally unusable. Gen5 lacks FAIRY and retains STEEL resistance to DARK/GHOST. Each defending type checks weaknesses before resistances before immunities; generic Effectiveness.calculate multiplies all supplied defending arguments without deduplication, while ordinary battler type collection supplies its own deduplicated types. Per-move category switch is independent of author backup; old-category mode queries current type special flag. Optional Shadow input is a separate activation condition.',
  ['TYPE:all141','BTMOVE:84–103','BSETTINGS:35–45','received COM-MOVE R001/TypeData'],['WP43 §2/§3/§8','WP02 battle switches']),
 ('PB07','Ability data versus callback behavior',
  'All1122 per-path ability records bind ID/name/description/Flags. Data descriptions are display strings; callback lookup uses effective ability identity at each actual caller. FasterEggHatching is present only on the explicitly read flagged rows (MAGMAARMOR/FLAMEBODY, plus default/Gen8 STEAMENGINE). Neither a plain description nor registration proves handler activation. MERCILESS reads target poison; wording it poisoned is not a source admission rule. Gen5/6/7 availability164/191/233 and current267 do not imply mechanic-generation changes.',
  ['ABILITY:all45','BSETTINGS:all140','received AbilityEffects3208 family facts','received Battler effective-ability queries'],['WP03 ability schema/field responsibility','received WP48/WP49 finite source families and AB vectors']),
 ('PB08','Every move field and dynamic consumers',
  'All3333 per-path move records bind Type/Category/Power/Accuracy/PP/Target/Priority/EffectChance/Flags and exact FunctionCode to the complete named move family contributions. Power1 can be a variable-power marker; accuracy0 has its own bypass; zero total PP is not finite exhaustion. Source target metadata distinguishes num_targets from final list length, User0 from failure, dynamic target replacement, range and foe-side flags. Actual common target/PP/ability/status guards remain before or after family-specific hooks; description order is not execution order.',
  ['MOVE:all408','TARGET:all185','BTMOVE:all201','PKMOVE:all77','received move125 attribute/calling units and15 source families'],['WP03 field responsibility','WP43 §§2/4/8','received WP47-A/B,WP44,WP46 and331 vector meanings']),
 ('PB09','Alternative move differences',
  'All four unique move payloads were actually read. Old VICEGRIP identity becomes default VISEGRIP; Gen5 SheerCold OHKO differs from later OHKOIce; Gen5 DarkVoid SleepTarget differs from later user-Darkrai gate and Gen7+ accuracy50; Gen5 HiddenPower author power1 versus later60 is separate from old-mechanic power function. Gen5–7 Teleport FleeFromBattle differs from default SwitchOutUserStatusMove priority−6. All other exact changed fields and availability bind the same per-field contracts, not a blanket legacy-mechanics claim.',
  ['all primary moves record fields','received exact family facts R001/R008/R012/R013'],['WP02 alternative data contract','WP03 schema','WP43 data-specific scope','received WP47 move contracts']),
 ('PB10','Item receipt and active/passive split',
  'CRE-B actually full-read four unique primary item payloads2457 records and associated Gen8/default693; received3150 primary path-records plus separately Shadow4. Full reception includes prices and explicit sale overrides, BP, use selectors, machine Move IDs, names/plurals/portions/descriptions, flags, consumability and all absent defaults. This context independently read Item270 and compiler units; data receipt is attributed to /root/creature_b. Active field/battle handlers and passive held effects have distinct callers and may use ID without a dedicated flag.',
  ['ITEM:all270','COMPILE_PBS:compile_items','received CRE-B PBS-FIELDS/ACTIVE/PRICE/FLAGS/PATHS and dependency facts','received ItemEffects1948 families'],['WP03 Item schema/default/field responsibility','received WP27/28 and WP50 bounded contracts']),
 ('PB11','Fling and NaturalGift current identity',
  'Current berry and any NaturalGift prefix admit that family; complete type+digits and complete power matching have separate fallbacks. Gen5 raw60/70/80 differs from later80/90/100. Fling requires active losable current item and its own berry-consumption gate, with prefix admission distinct from numeric power. Per-hit current identity and later actual current-item consumption are not frozen at selection. Existing NG self-consumption and Fling InnardsOut→ORAN missing-item failure prefixes, controls, no rollback and unexecuted status were actually received.',
  ['ITEM:has_flag?/unlosable?','received COM-MOVE R011/R008','received U04-NG01–04/U04-MH01–03/U04-HI01–03/SB-I13–15'],['received WP47-A §3.1.1,WP46 §2.1.1,WP50 §5.1.1 and exact static catalogs']),
 ('PB12','Facility list graph and compile behavior',
  'Exactly five list sections. Default references Tower; pokecupsingle/double→Poke, little→Little, pika→Pika, fancycupsingle/double→Fancy_single. The alternative Fancy618 has no current list selector. compile_trainer_lists stores trainer/template arrays, names, filenames and default bit; missing referred files become empty arrays. Challenges on Default are skipped. Loader rescues list load failure to [] and searches matching nondefault then firstdefault. No general all-files/all-items registration or list nonemptiness guarantee.',
  ['PBS/battle_facility_lists.txt:all25','COMPILE_PBS:951–1063','FACILITY:list selectors'],['WP04 explicit producer paths','received WP54/55/57/76 source contracts FAC-I07/I08/I11']),
 ('PB13','Facility template normalization',
  'Template species/item/nature use permissive existence checks. Unknown item becomes nil; unknown moves drop and valid moves compress among first MAX_MOVES; only all-invalid falls back to first Move.keys (default MEGAHORN). EV names are fixed recognized aliases and unrecognized are ignored. Creation uses a new Pokemon without default moves, assigns actual item (no can_hold gate), chosen nature/happiness0, move objects, IV allstats and integer EV_LIMIT/number-of-EV-stats before recalculation. RETURN→FRUSTRATION is conditional on registry existence at creation.',
  ['FACILITY:PBPokemon.fromInspected/initialize/createPokemon','PKMOVE:initialize','received CRE-B FITEM1–4'],['received facility constructor contracts PBF/FAC-I07/I08','WP03 registry distinction']),
 ('PB14','Tower missing literal controls',
  'Named PBF actual reader reports882 Tower templates/1600 trainers and full references: only84 raw item IDs has STICK unknown at physical line140/index137, hence nil under current registry; LEEK is different. Only330 raw move IDs has VICEGRIP unknown line252/index249, leaving BUBBLEBEAM/KNOCKOFF/PROTECT. Every actual Tower row retains at least one valid move, so fallback is unreachable in this finite table. ItemClause ignores nil and compares actual identity; no need to assert all authored literals register. This is a bounded received table fact plus own exact parser, not personal raw Tower reading.',
  ['FACILITY:PBPokemon.fromInspected','REG:exists?/try_get','received PBF-ITEM/PBF-MOVE/PBF trait and CSV contracts'],['WP03 permissive versus strict lookup','received facility contracts; no new required claim']),
 ('PB15','Facility eligibility and consumption boundary',
  'Actual PBF/FAC receipts preserve template pool/trait/party constraints, fancyboth single file selection, infeasible ordinary factory level totals and unbounded rejection loops. Filename/record existence does not prove eligibility or termination. Organized battle item snapshots follow heal/adjustment and normal positional restoration; exceptions do not guarantee restoration. These finite named consumer facts are received, without granting all facility formal/shared catalog/history completion.',
  ['received PBF all8 facts','received FAC-I01/I02/I07/I08/I11'],['received WP54/55/57/76 finite contracts']),
 ('PB16','Compile, save, startup reload and failure',
  'Main loads core messages, plugins, Compiler.main, then Game.initialize. Compiler.main is debug-gated, uses missing required data/full flag/CTRL/import and integer-second maximum text>=maximum data time trigger; deletes listed data before full stage if triggered. Types→abilities→moves→items precede dependent species/trainers/facilities. Direct full-content entry lacks startup discovery decision/predelete/rescue. Reset/SystemExit rethrow; other diagnosed failures attempt listed deletion, not guaranteed transaction. Successful stage saves table/message outputs; ordinary startup GameData.load_all replaces registries. No Ruby/serialized load was run here.',
  ['MAIN:25–41','COMPILER:main/compile_all/compile_PBS_files','REG:load_all/ClassMethodsSymbols.load','START:initialize'],['WP04 §§3/4/5','KCAT KL02–05/KL19–21/KL37–39']),
 ('PB17','Existing objects and save-game reload',
  'Game.load(save_data) applies saved values/maps rather than recompiling or calling GameData.load_all. Pokemon::Move holds ID/PP/PPUp but queries data fields and totalPP live by ID. Battle::Move snapshots name/function/power/type/category/accuracy/target/priority/effectChance and clones flags at construction; its totalPP may delegate to realMove unless positive explicit override. AIMove wraps this existing battle object, sets calcType and moldBreaker during setup and uses skill-dependent own handlers/callbacks. Registry reload cannot be generalized to refresh all existing battle snapshots, caches or old data instances.',
  ['START:Game.load','PKMOVE:all77','BTMOVE:34–100','AIMOVE:all563','REG:load'],['WP04 §5.6','WP03 §4.1','received WP52 AI wrapper/query scope']),
 ('PB18','Writer and language/resource boundaries',
  'Generic writer selects suffix paths from current registry entries, emits BOM/CRLF and schema properties. Type/Ability/Move/Item omissions use constructor/default/property policies; Item false Consumable for nonimportant must be written, sale-half/BP1/use0 may omit. Facility writer exports normalized arrays and strict present move identities. Display names/descriptions use message-domain lookup; icon resolver can fall back and depends on real resource existence. Author text and metadata do not prove translated text, pixels, host availability or byte round-trip.',
  ['WRITE_PBS:1–69/137–164/511–625','TYPE/ABILITY/MOVE/ITEM:name/description/get_property_for_PBS','ITEM:74–117'],['WP03 §4.3/§7','WP04 §5','WP43 §8']),
 ('PB19','AI differences and real combat',
  'AIMove unconditionally substitutes basepower1→60 before its medium-skill gate; only the optional AI basepower handler depends on that gate. Its rough type/priority/damage/accuracy/critical queries can invoke actual callback writes and explicit untriggering, but do not reproduce all true use ordering or RNG. Data Target/Function/PP/flags and current ability/item identity are distinct inputs. AI own OHKOIce ice gate does not restore actual loaded-clause target gate. Conversion User0 generic score path and separately defined target-handler remain distinct; root-owned AI001 is not duplicated.',
  ['AIMOVE:all563','BTMOVE/TARGET','received COM-AI all14 interfaces/sharedAB31','received COM-MOVE331 vector meanings'],['received WP52-A/B/C and GR8-AI-001 owner; no new duplicate']),
 ('PB20','Finite evidence and open responsibility',
  'This task has21R and0 formal primary. Own full text/field review11 primary, exact-byte associations5 after own read, CRE-B named full raw4 and named association1. All primary7704 path-record fields have data/schema/finite consumer meanings, not all execution combinations or all subsystem reverse approval. Shared formal text/read receipts and their unaccepted predicates are explicit. Current global history, all external species/trainer records and complete ordinary-runtime reload assertions remain with named owners, not called host limits.',
  ['reading-ledger.json','external-data-62.json','interfaces.json','reverse-mapping.json'],['original full review contract; scope retained'])]
fact_records=[{'id':a,'title':b,'fact':c,'source_units':d,'formal_receivers':e,
               'reviewer':READER,'evidence':'SOURCE_STATIC_OR_NAMED_SOURCE_RECEPTION','execution':'NOT_EXECUTED'} for a,b,c,d,e in facts]
dump('semantic-facts.json',{'schema':'gr8-pbs-battle-semantic-facts/v1','reviewer':READER,'facts':fact_records})

family_fields={
 'abilities':{
  'SectionName':('m','exact new symbol identity; duplicate compile gate, not callback registration','PB03'),
  'Name':('s','raw Unnamed default; ability message-name domain lookup','PB07'),
  'Description':('q','raw ??? default; ability description display, not callback program','PB07'),
  'Flags':('*s','omitted []; each string exact case-insensitive match; explicit empty can retain nil and fail query; FasterEggHatching consumer','PB07')},
 'moves':{
  'SectionName':('m','exact move identity and insertion order; default fallback firstMEGAHORN','PB03'),
  'Name':('s','Unnamed default; Move name message domain; factory snapshots name','PB18'),
  'Type':('e:Type','current registered Type enum; missing constructorNONE is not author enum approval; dynamic overrides have independent existence gates','PB06'),
  'Category':('e:Physical=0,Special=1,Status=2','defaultStatus; zero-power validator and configuration per-move/type category distinct','PB05'),
  'Power':('u','default0; ordinary versus fixed/variable functions; statuspositive rejects; power1 not finaldamage','PB08'),
  'Accuracy':('u','default100; ordinary0 bypass versus effect-specific query and independent AI roughestimate','PB08'),
  'TotalPP':('u','default5; Pokemon move PPUp integer increments, persistent PP vs temporary special PP−1, finitezeroPP gate','PB08'),
  'Target':('e:Target','defaultNone; all18 exact hardcoded vectors, dynamic replacements, num_targets/list/range/foeside distinguished','PB08'),
  'Priority':('i','default0 signed; modified and saved effectivepriority distinct','PB08'),
  'FunctionCode':('s','defaulttextNone; exact implementation identity/digit-prefix dispatch; lawfulmissingfallback; separate AI handler registry','PB05'),
  'Flags':('*s','default[]; all exact present flags bound to complete move predicates/calling exclusions and aliases, not arbitrary English tag implication','PB08'),
  'EffectChance':('u','default0; extra-effect family uses own gates/random,101 not chanceclamp; fang internal draws separate','PB08'),
  'Description':('q','default???; localized display; generation-specific prose does not choose behavior or request order','PB18')},
 'types':{
  'SectionName':('m','exact type identity; final reference-existence validation','PB03'),
  'Name':('s','Unnamed default and Type name-domain lookup','PB18'),
  'IconPosition':('u','default0; resource layout input, not actual pixels','PB18'),
  'IsSpecialType':('b','defaultfalse; old category mode special/physical','PB06'),
  'IsPseudoType':('b','defaultfalse; HiddenPower and other consumers can exclude; neutral not automatically unusable','PB06'),
  'Weaknesses':('*m','default[]; attacking type symbols giving2; uniqwithinfield and terminal whole-table type-existence validation, weak-first overlap priority','PB06'),
  'Resistances':('*m','default[]; attacking type symbols giving1/2, checkedafterweak; terminal whole-table reference validation','PB06'),
  'Immunities':('*m','default[]; attacking type symbols giving0, checkedafterresist; terminal whole-table reference validation','PB06'),
  'Flags':('*s','default[]; generic flag list; no default file flag authorvalues invented','PB06')},
 'items':{
  'SectionName':('m','exact item identity; named reader full receipt, callback dispatch separate','PB10'),
  'Name':('s','rawUnnamed and item name-domain lookup','PB10'),
  'NamePlural':('s','rawUnnamed independent; no automatic singularplural grammar','PB10'),
  'PortionName':('s','missingnil falls back name; existing translatedempty staysempty','PB10'),
  'PortionNamePlural':('s','missingnil falls back name_plural separately','PB10'),
  'Pocket':('v','positive integer; default1, no schema bound to configuredbagcount','PB10'),
  'Price':('u','nonnegative/default0; own exact purchaseprice, not walletmax editor limit','PB10'),
  'SellPrice':('u','explicit nonnegative including0 wins; missingintegerprice/2','PB10'),
  'BPPrice':('u','default1; independent BPadapter price','PB10'),
  'FieldUse':('e:OnPokemon1,Direct2,TM3,HM4,TR5','missing0; exact context selector and separate registered handler/eligibility','PB10'),
  'BattleUse':('e:OnPokemon1,OnMove2,OnBattler3,OnFoe4,Direct5','missing0; exact active battle request context, not passiveholderactivation','PB10'),
  'Flags':('*s','omitted[]; case-insensitive full exact flags, prefixesFling/NaturalGift independent; MegaStoneexcludesorbs','PB11'),
  'Consumable':('b','missinginverseimportant; importantKey/TM/HM always effectivefalse; active consumption different from heldconsume','PB10'),
  'ShowQuantity':('b','missingnil; effective rawflag OR !important, explicitfalse cannot hideordinaryquantity','PB10'),
  'Move':('e:Move','strict registered Move enum when authorpresent; defaultnil; only machineclassification makes machineconsumer','PB10'),
  'Description':('q','raw??? and item descriptiondomain; names do not dispatch handlers','PB10')},
 'battle_facility_lists':{
  'SectionName':('DefaultTrainerList or TrainerList','specialized exactsection; defaultflag distinct from challenge string','PB12'),
  'Trainers':('s','required field not universal fileexists requirement; file path and specializedtrainerschema','PB12'),
  'Pokemon':('s','required field; specializedtemplate fromInspected, not strictgeneraltrainerparser','PB13'),
  'Challenges':('*s','Default skip/empty; nondefault exactstrings, firstmatch thenfirstdefault','PB12')}}
dump('field-contracts.json',{'schema':'gr8-pbs-battle-field-contracts/v1','manually_authored_after_actual_read':True,
 'reviewer':READER,'families':{fam:{k:{'schema':v[0],'meaning':v[1],'fact':v[2]} for k,v in fs.items()} for fam,fs in family_fields.items()},
 'source_identity_keys':source_ids,'boundary':'Per-field data meaning; no claim every cross-product/game execution or every domain consumer is globally approved.'})

def pbsrecords(path):
    raw=(R/path).read_bytes(); lines=raw.decode('utf-8-sig').splitlines(); out=[]; cur=None
    for ln,s in enumerate(lines,1):
        m=re.match(r'^\s*\[(.+)\]\s*$',s)
        if m:
            if cur:cur['range'][1]=ln-1
            cur={'id':m.group(1),'range':[ln,len(lines)],'fields':[]};out.append(cur)
        elif cur and '=' in s and not s.lstrip().startswith('#'):
            k,v=s.split('=',1);cur['fields'].append({'key':k.strip(),'value':v.strip(),'line':ln})
    return out

primary_ids=[]; ledger=[]; recled=[]; duplicates=[]; unknownfields=[]
items_inventory=readj(REPORT/'tasks/creature_b/pbs-record-inventory.json')
provider_paths={p['identity']['path']:p for p in items_inventory['payloads']}
for x in primary:
    p=x['path']; ii=ident(R,p,RC); assert ii['sha256']==x['sha256']; fam=pathlib.Path(p).stem
    rs=pbsrecords(p); ii['record_count']=len(rs)
    if fam=='items':
        state='RECEIVED_NAMED_SAME_BYTE_ASSOCIATION' if 'Gen 8 backup' in p else 'RECEIVED_NAMED_FULL_RAW_READER'
        actual_reader='/root/creature_b'; support=['../creature_b/pbs-record-reception.json','../creature_b/dependency-semantic-facts.json','../creature_b/facility-item-interface.json']
        provider=provider_paths[p]
        assert provider['record_count']==len(rs)
        assert provider['identity']['sha256']==ii['sha256']
        assert [z['id'] for z in provider['records']]==[z['id'] for z in rs]
    elif p in associations:
        state='OWN_READ_THEN_EXACT_BYTE_PATH_ASSOCIATION';actual_reader=READER
        assert (R/p).read_bytes()==(R/associations[p]).read_bytes()
        support=[z['io'] for z in pbsio+rawio if z['path']==associations[p]]
    else:
        state='OWN_FULL_FIELD_VIEW' if fam in ['abilities','moves'] else 'OWN_FULL_CONTINUOUS_RAW'
        actual_reader=READER;support=[z['io'] for z in pbsio+rawio if z['path']==p]
        assert support,p
    ii.update(primary=True,review_status=state,actual_full_reader=actual_reader)
    primary_ids.append(ii)
    ledger.append({'identity':ii,'status':state,'reviewer':READER,'actual_full_reader':actual_reader,
      'own_read_range':[1,ii['lines']] if state.startswith('OWN_FULL') else None,
      'all_record_field_semantics':'OWN_ACTUAL_READING' if fam!='items' else 'ACTUALLY_RECEIVED_NAMED_READER_FIELD_AND_CONSUMER_FACTS',
      'associate_from':associations.get(p,'PBS/items.txt' if p=='PBS/Gen 8 backup/items.txt' else None),
      'support':support,'records':len(rs),'fact_ids':(['PB10','PB11'] if fam=='items' else ['PB12','PB13','PB14','PB15'] if fam=='battle_facility_lists' else ['PB06'] if fam=='types' else ['PB07'] if fam=='abilities' else ['PB05','PB08','PB09','PB19']),
      'premise':'Correct current active registry and successful applicable entry; backups conditional; no all-requests-register assumption',
      'unread_primary_records':0,'unreceived_primary_field_meanings':0,'execution':'NOT_EXECUTED'})
    for n,z in enumerate(rs,1):
        seen=collections.Counter(f['key'] for f in z['fields'])
        if any(c>1 for c in seen.values()):duplicates.append({'path':p,'record':z['id'],'keys':dict(seen)})
        present=[]
        for f in z['fields']:
            k=f['key'];v=f['value'];present.append(k)
            if k not in family_fields[fam]:unknownfields.append({'path':p,'record':z['id'],'field':k})
            f.update(meaning_ref=f'field-contracts.json#/families/{fam}/{k}',value_sha256=hashlib.sha256(v.encode()).hexdigest())
            if k in ['Description','Name','NamePlural','PortionName','PortionNamePlural']:f.pop('value')
        recled.append({'path':p,'path_record_number':n,'id':z['id'],'range':z['range'],'identity_sha256':ii['sha256'],
          'actual_full_reader':actual_reader,'reading_credit':state,
          'fields':z['fields'],'section_contract':f'field-contracts.json#/families/{fam}/SectionName',
          'omitted_fields':[k for k in family_fields[fam] if k!='SectionName' and k not in present],
          'omission_meaning':'Each omitted field binds the independently specified constructor default; no unparsed numerical value invented.',
          'semantic_acceptance':'Actual own full record reading' if fam!='items' else 'Named CRE-B full record/field receipt, mechanically rebound to exact path/record/field vector; NOT own raw read',
          'consumer_mapping':'forward-mapping.json',
          'global_all_combinations':'NOT_CLAIMED'})

assert not unknownfields,unknownfields
dump('record-field-ledger.json',{'schema':'gr8-pbs-battle-record-field-ledger/v1','reviewer':READER,'path_record_denominator':len(recled),
 'meaning':'Generated only to bind already actually reviewed records to manually adjudicated field meanings. This serialization is not the source of reading credit.',
 'records':recled,'duplicate_attribute_inventory':duplicates,'unknown_field_inventory':unknownfields,'execution':'NOT_EXECUTED'})

supp=[]
grouped=collections.defaultdict(list)
for z in rawio:
    if z['path'] not in {a['path'] for a in primary}: grouped[(z['repo'],z['path'])].append(z)
for (repo,p),zs in grouped.items():
    root=pathlib.Path(repo);ii=ident(root,p,RC if root==R else BC)
    covered=set(i for z in zs for i in range(z['read_range'][0],z['read_range'][1]+1))
    missing=[i for i in range(1,ii['lines']+1) if i not in covered]
    supp.append({'identity':ii,'actual_reader':READER,'status':'OWN_FULL_CONTINUOUS_UNION' if not missing else 'OWN_COMPLETE_NAMED_UNITS_ONLY',
        'actual_ranges':[z['read_range'] for z in zs],'io':[z['io'] for z in zs],
        'unread_line_count':len(missing),'unread_ranges_not_host_limit':missing,
        'scope':'Relevant PBS lifecycle/schema/consumer proof; unrelated text of partial files is not credited.'})

receipt_names=[
 'creature_b/pbs-record-reception.json','creature_b/facility-item-interface.json','creature_b/dependency-semantic-facts.json','creature_b/reading-ledger.json',
 'com_move/ability-item-source-reception.json','com_move/battler-reception.json','com_move/semantic-notes.json','com_move/vector-review.json',
 'com_move/subreviews/attributes_calling/unit-facts.tsv','com_ai/review.md','com_ai/interfaces.json','com_ai/shared-ab-reception.json',
 'com_ai/remaining-reception/prompt.md','com_ai/remaining-reception/readset.json',
 'com_facility/review.md','com_facility/interfaces.json','pbs_creature_facility/interfaces.json','com_ability_item/review.md']
receipts=[]
for p in receipt_names:
    ii=ident(B,str((REPORT/'tasks'/p).relative_to(B)))
    status='ACTUAL_COMPLETE_MEANING_RECEPTION_READ'
    if p=='creature_b/reading-ledger.json':status='RELEVANT_ITEM_IDENTITY_AND_READ_SCOPE_RECEIVED_NOT_WHOLE_LEDGER_PERSONAL_READ'
    if p=='com_move/vector-review.json':status='ALL331_INPUT_EXPECTED_AND_MANUAL_CHECK_RECEIVED; repeated_group_facts_bound_to_prior_full_source_fact_receipts'
    receipts.append({'identity':ii,'receiver':READER,'status':status,'not_own_full_source_credit':True,'behavior':'NOT_EXECUTED'})
inventory_identity=ident(B,str((REPORT/'tasks/creature_b/pbs-record-inventory.json').relative_to(B)))
receipts.append({'identity':inventory_identity,'receiver':READER,'status':'MECHANICAL_PER_RECORD_BINDING_ONLY; not own complete raw artifact display','not_own_full_source_credit':True})

dump('identities.json',{'schema':'gr8-pbs-battle-identities/v1','utc':NOW,'reviewer':READER,
 'frozen':{'B8':BC,'B8_workspace_tree':BT,'B8_formal_tree':FT,'R':RC,'R_workspace_tree':RT},
 'cloud_paths':{'specification':str(B),'reference':str(R),'task':str(HERE)},
 'Mac_historical_paths':'Not resolved or authenticated by this cloud review; no cross-platform identity inferred.',
 'report_base_HEAD_seen_at_start':'adfb0237bdcb3732061d0d23a8d8a17653991c7c',
 'configuration':{'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default normal','Fast':'off'},
 'actual':dict.fromkeys(['model','effort','tier','Fast','opaque_platform_session_id'],'UNVERIFIED'),
 'logical_context':READER,'independence':'Actual new context; failed prior launches did not begin and do not count; no rename/reuse independent-review claim'},
 'primary':primary_ids,'own_supplemental':[z['identity'] for z in supp],'receipt_artifacts':receipts,
 'checks':{'all_primary_bytes_match_frozen':True,'all_own_supplemental_bytes_match_frozen':True,'reference_engine_executed':False}})
dump('reading-ledger.json',{'schema':'gr8-pbs-battle-reading-ledger/v1','utc':NOW,'actual_context':READER,
 'contract_inputs':{'prompt':'inputs/eighth-global-review-prompt.md','bytes':36653,'sha256':'63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b',
 'actual_read':'All241lines in continuous windows at start; AGENTS.md, review-SKILL.md, taskprompt and allreadset also fullyread; original private platform read I/O not mislabeled as public captures.'},
 'credit_policy':'Raw/view output alone does not establish read credit. Credit below is this actual reader declaration after complete visible semantic reading or actually received named facts. Same-byte association only after own source payload read; no independent reader invented.',
 'primary':ledger,'own_supplemental':supp,'named_receipts':receipts,
 'counts':{'primary_paths':21,'primary_formal':0,'own_full_primary_payloads':11,'own_post_read_byte_associated_paths':5,
 'named_full_raw_primary_paths':4,'named_full_reader_associated_primary_paths':1,'primary_path_records':len(recled),
 'primary_unread_or_unreceived_records':0,'primary_unread_or_unreceived_field_meanings':0,
 'own_actual_supplemental_paths':len(supp),'own_full_supplemental':sum(z['status']=='OWN_FULL_CONTINUOUS_UNION' for z in supp),
 'own_partial_supplemental':sum(z['status']!='OWN_FULL_CONTINUOUS_UNION' for z in supp)},
 'formal_primary_clause_denominator':0,'supplemental_clause_scope':'Own全文 reading of WP02/03/04,KCAT,WP43 does not approve all unrelated kernel/runtime clauses; see exact reverse dispositions.',
 'execution':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'})

dump('forward-mapping.json',{'schema':'gr8-pbs-battle-forward/v1','primary_path_denominator':21,'primary_path_record_denominator':len(recled),
 'identity_table':'identities.json#/primary','record_field_bindings':'record-field-ledger.json','field_meanings':'field-contracts.json','facts':fact_records,
 'primary_by_path':[{'path':z['identity']['path'],'records':z['records'],'fact_ids':z['fact_ids'],
 'upstream':['PB01','PB02','PB03','PB04'],'compile_save_load_reload':['PB16','PB17','PB18'],
 'consumers':'Each field/record bound to complete listed own/named source facts; open whole-domain joins retained in interfaces.'} for z in ledger],
 'administrative_disposition':'Wiki comments/separators only give documentation; identity/order/IDs/values are effective rules and receive no administrative waiver.',
 'behavior':'NOT_EXECUTED'})

# All remaining readset identities are actually checked. Their metadata is not
# used to declare outside-ownership record semantics as read.
outer=readj(REPORT/'tasks/com_ai/remaining-reception/readset.json')
outerrows=[]
own_by_path={z['identity']['path']:z for z in supp}
for i,z in enumerate(outer['records']):
    p=z['identity']['path'];ii=ident(R,p,RC);primarymatch=p in {v['path'] for v in primary_ids}
    if primarymatch:status='THIS21_PRIMARY_DATA_AND_FINITE_LIFECYCLE_MEANINGS_RECEIVED'
    elif p in own_by_path:
        status=own_by_path[p]['status']
    elif p=='PBS/Shadow Pokémon backup/items_shadow_pkmn.txt':status='CRE_B_NAMED_FULL_FOUR_RECORD_RECEIPT'
    elif p.endswith('008_Species.rb'):status='CRE_B_FINITE_SCHEMA_FACTS_RECEIVED_WHOLE_EXTERNAL_SOURCE_NOT_OWN_READ'
    elif p.endswith('014_TrainerType.rb'):status='COM_AI_OWN_FULL_SOURCE_PROVIDER_FINITE_QUERY_RECEIPT'
    else:status='EXTERNAL_OWNER_RECORD_OR_SOURCE_SEMANTICS_NOT_RECEIVED_HERE'
    outerrows.append({'number':i,'identity':ii,'owner_readsets':z['upstream_readsets'],'is_this_primary':primarymatch,
       'this_receiver_status':status,'AI_prior_receiver_status':z['current_AI_receiver_status'],
       'meaning':'Input identity proven; semantic status above is deliberately separate from byte check.'})
dump('external-data-62.json',{'schema':'gr8-pbs-battle-ai-outer-readset-disposition/v1','denominator':62,
 'primary_inside':21,'outside_primary':41,'records':outerrows,
 'status_counts':dict(collections.Counter(z['this_receiver_status'] for z in outerrows)),
 'responsibility':'Exact62 union is not62 new primary files; source/creature-current/backups ownership retained. No pending readable data called hostlimit.'})

# Mechanically enumerate alternative differences only after actual full reading.
alts=[]
for fam in ['abilities','moves','types','items']:
    base={z['id']:z for z in pbsrecords(f'PBS/{fam}.txt')}
    for gen in range(5,9):
        p=f'PBS/Gen {gen} backup/{fam}.txt';rs={z['id']:z for z in pbsrecords(p)}
        changes=[]
        for k in sorted(base.keys() & rs.keys()):
            a={f['key']:f['value'] for f in base[k]['fields']};c={f['key']:f['value'] for f in rs[k]['fields']}
            changed=[n for n in a.keys()|c.keys() if a.get(n)!=c.get(n)]
            if changed:changes.append({'id':k,'changed_fields':sorted(changed),'meanings':[f'field-contracts.json#/families/{fam}/{n}' for n in sorted(changed)],
              'default_range':base[k]['range'],'backup_range':rs[k]['range'],'status':'Mechanical difference locator; both complete record meanings already actually read/received, not an additional semantic review.'})
        alts.append({'path':p,'family':fam,'generation':gen,'records':len(rs),'default_records':len(base),'exact_byte_equal':(R/p).read_bytes()==(R/f'PBS/{fam}.txt').read_bytes(),
          'only_backup':sorted(rs.keys()-base.keys()),'only_default':sorted(base.keys()-rs.keys()),'changed_records':changes,
          'activation':'Only if copied/explicitly supplied to current compiler; no recursive discovery, generation constants/callback definitions independently fixed.',
          'semantic_facts':['PB01','PB06' if fam=='types' else 'PB07' if fam=='abilities' else 'PB09' if fam=='moves' else 'PB10','PB17']})
dump('alternative-semantics.json',{'schema':'gr8-pbs-battle-alternative-semantics/v1','reviewer':READER,'all16_backup_paths':alts,
 'generation_warning':'Actual input variant != mechanic generation; no implicit migration/alias/type creation/recompiled constants.',
 'behavior':'NOT_EXECUTED'})

# Semantic atomic units below are manually chosen independent predicates;
# source-line/table locators further below remain locators, not fake atoms.
atomic=[
 ('BPR01','WP02',[213,237],'PB01','PBS discovery, alternative backup and independent settings','LOCAL_PBS_SCOPED_RECONCILED'),
 ('BPR02','WP03',[24,90],'PB03','Exact symbol lookup and directregister/compileduplicate split; other named class exceptions retain owners','LOCAL_PBS_SCOPED_RECONCILED'),
 ('BPR03','WP03',[91,117],'PB04','Four constructor default families versus raw field and finaldisplay','LOCAL_PBS_SCOPED_RECONCILED'),
 ('BPR04','WP03',[138,228],'PB02','Applicable schema primitive/enum/repetition/extra-tail predicates; unrelated composite identities not reapproved','LOCAL_PBS_SCOPED_RECONCILED'),
 ('BPR05','WP03',[313,359],'PB08','Four field family responsibility references; downstream domain assumptions finite received only','BOUNDED_RECEIVER_NOT_WHOLE_ALL_DOMAIN_APPROVAL'),
 ('BPR06','WP04',[21,56],'PB16','Main/start/direct compile gates and nontransactional failure prefixes','LOCAL_PBS_SCOPED_RECONCILED'),
 ('BPR07','WP04',[66,119],'PB02','Lexical pipeline precedes scalar/list schema and field defaults','LOCAL_PBS_SCOPED_RECONCILED'),
 ('BPR08','WP04',[130,183],'PB05','Move category/power validation and dependency order; unrelated specialized validators retain owners','LOCAL_PBS_SCOPED_RECONCILED'),
 ('BPR09','WP04',[210,258],'PB18','Writer omission policy / no byte roundtrip; unrelated class-specific exports retain owners','LOCAL_PBS_SCOPED_RECONCILED'),
 ('BPR10','WP04',[259,270],'PB17','Registry reload versus existing objects and caches; unrelated cacheexamples retain owners','LOCAL_PBS_SCOPED_RECONCILED'),
 ('BPR11','WP04',[194,197],'PB16','Changes made output existing root-accepted KER003 kept with owner; no duplicate new proposal','KNOWN_ROOT_ADJUDICATION_NO_DUPLICATE'),
 ('BPR12','WP43',[29,35],'PB05','Lawful exact missing effect distinct from None/nil/illegal IDs','RECEIVED_SOURCE_PLUS_OWN_FACTORY_RECONCILED'),
 ('BPR13','WP43',[37,64],'PB06','Defending-type source arrays/overlap/order/pseudo/Shadow boundary','RECEIVED_CORE_SOURCE_PLUS_OWN_TYPE_TABLE_RECONCILED'),
 ('BPR14','WP43',[159,165],'PB04','Current data and constructor defaults, localized display and data generation scope','LOCAL_PBS_SCOPED_RECONCILED'),
 ('BPR15','KCAT',[9,14],'PB01','KC01–06 only configurationdata/discovery local; language runtime externally scoped','BOUNDED_SOURCE_NOT_ALL_KERNEL_VECTOR_APPROVAL'),
 ('BPR16','KCAT',[26,35],'PB03','KR07/09/10/11/12/16 PBS and identity finite predicates, phone/other classes outside','LOCAL_PBS_SCOPED_RECONCILED'),
 ('BPR17','KCAT',[41,90],'PB16','KL01–21/33–39/46–50 relevant entry/grammar/vector conditions; unrelated cache/classes preserve ownerstatus','BOUNDED_SOURCE_NOT_ALL_KERNEL_VECTOR_APPROVAL'),
 ('BPR18','KCAT',[111,122],'PB05','Item enum/numeric/default and move power/category ordinary control examples','LOCAL_PBS_SCOPED_RECONCILED'),
 ('BPR19','KCAT',[127,133],'PB04','Ability/Item/Move default predicates local; unrelated metadata/ribbon callers not reapproved','BOUNDED_SOURCE_NOT_ALL_KERNEL_VECTOR_APPROVAL'),
 ('BPR20','KCAT',[173,175],'PB18','ItemConsumablefalse export and important effectiveflag retained','LOCAL_PBS_SCOPED_RECONCILED'),
 ('BPR21','KCAT',[187,198],'PB07','Type/Move defaults and explicit-empty AbilityFlags failure finite; egg consumer named CREreceipt only','BOUNDED_SOURCE_NOT_ALL_KERNEL_VECTOR_APPROVAL')]
ar=[{'id':a,'formal':formal_ids[b],'location_window':c,'fact_id':d,'subassertion':e,'disposition':f,'execution':'NOT_EXECUTED'} for a,b,c,d,e,f in atomic]
formal_locators=[]
for k,p in formal_ids.items():
    for i,line in enumerate((B/p).read_text().splitlines(),1):
        if not line.strip():continue
        matches=[z['id'] for z in ar if z['formal']==p and z['location_window'][0]<=i<=z['location_window'][1]]
        formal_locators.append({'path':p,'line':i,'text_sha256':hashlib.sha256(line.encode()).hexdigest(),
          'classification':'STRUCTURAL' if line.startswith('#') or re.match(r'^\|\s*[-: ]+\|',line) else 'TEXT_OR_TABLE_LOCATOR_NOT_ATOMIC_CLAUSE',
          'applicable_manual_units':matches,'scope_status':'MANUAL_UNITS_ARE_FINITE_NOT_WHOLE_LINE_PASS' if matches else 'OUTSIDE_PRIMARY_SCOPE_OWNER_RECEPTION_NOT_CLAIMED',
          'no_line_count_as_semantic_proof':True})
dump('reverse-mapping.json',{'schema':'gr8-pbs-battle-reverse/v1','primary_formal_paths':0,'primary_formal_clause_denominator':0,
 'supplemental_own_full_text_paths':5,'manual_semantic_subassertion_units':ar,'structural_locators':formal_locators,
 'important':'Location windows are navigation ranges, not assertion that all text inside is accepted. Each manually written subassertion is finite; residual formal clauses retain actual owner. Kernel2219 reverse locators/771missing local links are not inherited as PASS.',
 'named_source_and_catalog_reception':{'com_move':'All331 input/expected/manualchecks actually received, with currentcatalog commonpremise prose read; formal-source domain credit belongs namedactualreaders. See catalog-reception.json.',
 'com_ai':'All14 finite interfaces and31 sharedAB vectors received; no wholeAIprimaryreverse approval by this task.',
 'com_ability_item':'Complete localreport facts read; full fourformal atomicmatrix not rereviewed here. Authority staysactualowner.',
 'com_facility':'All13 finite interfaces received, allknown tails explicitly kept.'},
 'unaccepted_remainder':'All clauses outside stated finite units and named accepted source facts remain external owner/global join work, explicitly enumerated by owner/path in interfaces and external-data-62; no global PASS.'})

# Bind source-backed catalog reception without promoting it to own source read.
v=readj(REPORT/'tasks/com_move/vector-review.json'); catrows=[]; mismatch=[]
for z in v['rows']:
    line=(B/z['catalog']).read_text().splitlines()[z['line']-1]
    if z['full_input'] not in line or z['full_expected'] not in line:mismatch.append(z['canonical_id'])
    catrows.append({'id':z['canonical_id'],'catalog':z['catalog'],'line':z['line'],
        'source_actual_reader':z['reviewer'],'source_evidence':z.get('source_facts'),
        'complete_premises_input_expected_and_manual_check':'ACTUALLY_RECEIVED_THIS_CONTEXT',
        'source_fact_join':'semantic-notes,battler-reception,ability-item-source-reception,attributesunitfacts actual full fact reception, own schema/data/factory/AIwrapper',
        'scope':'Finite source-backed vector; not own source全文 or behavior execution; no approval of unrelated host/history/otherformal domains',
        'execution':'NOT_EXECUTED'})
dump('catalog-reception.json',{'schema':'gr8-pbs-battle-finite-catalog-reception/v1','receiver':READER,
 'provider_artifact':next(z['identity'] for z in receipts if z['identity']['path'].endswith('com_move/vector-review.json')),
 'actual_read_batches':'All331 rows input/expected/manualcheck:0–99,100–199,200–279,280–330. All commonpremise and non-table prose from both currentB8catalogs actually read separately. Repeated source-group facts bound to previously complete meaningreceipts.',
 'mechanical_current_row_binding_mismatch':mismatch,'rows':catrows,
 'shared_AB31':'Complete com_ai/shared-ab-reception.json all31 premises/outcomes/manualfacts/sourcebindings actuallyread; different actual source readers retained.',
 'not_claimed':'No source/model/engine/callback/host/vector execution; no new independent fullsource reader created by receiving.'})

dump('interfaces.json',{'schema':'gr8-pbs-battle-interfaces/v1','utc':NOW,'reviewer':READER,
 'received_and_reconciled':[
  {'id':'PB-I01','boundary':'All21 primary schema/field meanings','facts':['PB01','PB02','PB03','PB04','PB05','PB06','PB07','PB08','PB09','PB10'],'status':'PRIMARY_RECORD_FIELD_REVIEW_COMPLETE','scope':'7704pathrecords; own11+ownassoc5+namedraw4+namedassoc1; all author fields including absent defaults'},
  {'id':'PB-I02','boundary':'CRE-B items→compiler→facility setter/held/activeeffects','facts':['PB10','PB11','PB13','PB14'],'status':'ACTUAL_NAMED_FULL_MEANING_RECEPTION_RECONCILED','scope':'3150primaryitems +Shadow4 separate; Item270/compiler own; not other systemfullscope'},
  {'id':'PB-I03','boundary':'PBS data→Move/Battler/AbilityItem→AIwrapper','facts':['PB05','PB06','PB07','PB08','PB11','PB17','PB19'],'status':'FINITE_SOURCE_MEANINGS_AND331VECTORS_RECEIVED','scope':'all named family source facts actuallyreceived, ownTarget/PokemonMove/BattleMove/AIMove; no universal callbackcomposition'},
  {'id':'PB-I04','boundary':'facility lists→templates/traits/rules/session','facts':['PB12','PB13','PB14','PB15'],'status':'FINITE_PRODUCER_CONSUMER_RECONCILED','scope':'Five sectiongraph own; PBF882+1600 andcup1888 named record/factreceipts; fullallfacilityformal/history remainowner'},
  {'id':'PB-I05','boundary':'parse/register/compile/save/startup-load/reload/existing-object','facts':['PB01','PB02','PB03','PB04','PB05','PB16','PB17','PB18'],'status':'THIS21DOMAIN_FULL_RELEVANT_LIFECYCLE_RECONCILED_STATIC','scope':'Complete actual local chain and failureunits; source/host notrun; all62 unionexternal domains stayseparate'}],
 'open':[
  {'id':'PB-O01','owner':'pbs_creature_current / pbs_creature_backups / root','status':'AVAILABLE_EXTERNAL_RECORD_OR_SOURCE_SEMANTICS_NOT_RECEIVED_HERE','exact_readset':'external-data-62.json','scope':'62 outerpaths contains21thisprimary and41external; perpath actual own/namedreceipt/open classification preserved. Do not close whole AI external interface solely from this21.'},
  {'id':'PB-O02','owner':'kernel_review / root','status':'SUPPLEMENTAL_FORMAL_RESIDUAL_ATOMIC_AND_EXTERNAL_CONSUMER_RECEPTION_OPEN','exact_paths':list(formal_ids.values())[:4],'scope':'Fulltextread here; only manually written local PBS assertions reverseapproved. Kernel2219 locators and771 missinglocalfactlink not inherited. Other classes/map/phone/metrics/language/runtime consumers outsidefinitePBSclaim.'},
  {'id':'PB-O03','owner':'com_move / com_ability_item / com_ai / com_facility / root','status':'WHOLE_EXTERNAL_FORMAL_AND_REMAINING_DEPENDENCY_ACCEPTANCE_NOT_CLAIMED','exact_artifacts':['../com_move/reverse-mapping.json','../com_ability_item/reverse-mapping.json','../com_ai/interfaces.json','../com_facility/interfaces.json'],'scope':'All finite meanings actually received as declared; their wholeformal atomics/historical tails not silently closed by data receipt. Runtimecapability/material gaps separate from readable joins.'},
  {'id':'PB-O04','owner':'root/history owner','status':'CURRENT_EFFECTIVE_HISTORY_AND_FINAL_GLOBAL_ADJUDICATION_OPEN','scope':'No oldPASS orhistoricalCLOSED used as current proof; known KER003/AI001 remain their owners, no duplicateproposal.'}],
 'execution_boundaries':{'behavior':'NOT_EXECUTED','reference_runs':0,'independent_behavior_model_runs':0,'host_runs':0,'actual_dat_loads':0,'actual_save_reload_runs':0,'update':'UPDATE_NOT_STARTED'},
 'zero_is_limited':'Primary unread/unreceived0 does not mean allglobalrecords/formalclauses/consumers/execution closed.'})
dump('proposals.json',{'schema':'gr8-pbs-battle-proposals/v1','reviewer':READER,'new_candidates':[],'new_required':0,
 'disposition':'No new reproducible difference established in the actually completed21primary and finite received chain; this is not global NO_REQUIRED_UPDATE.',
 'considered_not_proposals':[
  {'id':'PB-CONTROL-STICK','reason':'Unknown Tower STICK normalizesnil by actual permissive parser; source does not require everyliteralregistered or aliasLEEK. ItemClause ignoresnone. No currentformal contradiction shown.'},
  {'id':'PB-CONTROL-VICEGRIP','reason':'UnknownTowerVICEGRIP drops; threevalidmovesremain. All-invalidfallbackonlyconditional, actuallyunreachableTowerfinite882. Cannot callthis illegalregistration/requiredrepair.'},
  {'id':'PB-CONTROL-MERCILESS','reason':'Ability description is displaytext; active callbacktarget-poison alreadypreserved. Do not elevate prose display to mechanicalpermission.'},
  {'id':'PB-CONTROL-BACKUPS','reason':'Subdirectorycontents conditional, notautomaticallyregistered; no extra missingFAIRY orSTICK conflict assumed underdefault.'},
  {'id':'PB-KNOWN-KER003','reason':'Root accepted existing generic kernel Changes made outputnotconsumed scope only; no duplicatecandidate.'},
  {'id':'PB-KNOWN-AI001','reason':'CurrentAI separateConversiontargethandlers preserved by ownAIwrapper/targetdataandnamedreceipt; existingownerproposalnotduplicated.'}],
 'independent_counterreview':'No new proposal submitted, so no invented second reviewer/adjudication. Any futurecandidate needs full eight-section evidence and actual distinct nonproposer before rootclassification.',
 'behavior':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'})

counts=dict(collections.Counter(pathlib.Path(x['path']).stem for x in recled))
summary={'path_records':len(recled),'records_by_family':counts,'primary_paths':len(primary_ids),
 'primary_bytes':sum(z['bytes'] for z in primary_ids),'primary_lines':sum(z['lines'] for z in primary_ids),
 'primary_identity_mismatch':0,'same_byte_associations':associations,'duplicate_attributes':duplicates,'unknownfields':unknownfields,
 'catalog_binding_mismatch':mismatch,'behavior':'NOT_EXECUTED','reference_executed':False,
 'meaning':'Static file/hash/JSON/difference/linebinding checks, not compiler/load/run or semanticreading substitute.'}
dump('validation.json',summary)
progress=readj(HERE/'progress.json');progress.update(status='PRIMARY_COMPLETE_FINITE_JOINS_COMPLETE_GLOBAL_EXTERNAL_JOINS_OPEN',
 updated_utc=NOW,delivery_snapshot_utc=NOW,actual_process_end_utc='UNVERIFIED_UNTIL_PLATFORM_TURN_END',
 primary_counts=readj(HERE/'reading-ledger.json')['counts'],new_candidates=0,new_required=0,
 actual_reference_behavior_runs=0,actual_behavior_model_runs=0,actual_host_runs=0,
 open_ids=['PB-O01','PB-O02','PB-O03','PB-O04'],final_global_verdict='NOT_AUTHORIZED_BY_THIS_FINITE_SCOPE',
 tool_failures='One rg invocation used assumed root directories that did not exist (exit2), corrected to actual deliverables path. One oversized metadata output truncated; all relevant62 identities and331 meanings reprinted compactly completely. No truncated output given semanticcredit.',
 no_commit_push_install_spawn=True)
dump('progress.json',progress)
print(json.dumps(summary,ensure_ascii=False))
