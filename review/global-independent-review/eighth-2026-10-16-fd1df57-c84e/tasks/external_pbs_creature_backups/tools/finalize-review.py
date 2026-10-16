"""Assemble the final finite contribution around actual prior human/model reads.

Field meaning and assertion text below are reviewer authored. Enumeration, hashing,
and propagation of already reviewed contracts to exact source coordinates are
mechanical; they grant no source reading, engine execution, or main reception.
"""
import collections
import datetime
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
REF = pathlib.Path('/workspace/pokemon-essentials')
UTC = datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(name): return json.loads((ROOT/name).read_text())
def write(name, obj): (ROOT/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')
ids = read('identities.json')['payloads']
ledger = read('reading-ledger.json')
notes = read('semantic-notes.json')
def at(tail, first, last):
    matches = [k for k,v in ids.items() if k.startswith('D') and v['path'].endswith(tail)]
    assert len(matches)==1, (tail,matches)
    return dict(identity_id=matches[0], lines=[first,last])
def method(tail, name):
    k = at(tail,1,1)['identity_id']; obj=ids[k]
    lines=pathlib.Path(obj['cloud_path']).read_text().splitlines()
    hits=[i for i,l in enumerate(lines) if re.match(r'^  def '+re.escape(name)+r'(?:\(|\s|$)',l)]
    assert len(hits)==1,(tail,name,hits)
    start=hits[0]; end=next((i for i in range(start+1,len(lines)) if lines[i].startswith('  def ')),len(lines))
    return dict(identity_id=k,lines=[start+1,end])
S='008_Species.rb'; C='002_Compiler_CompilePBS.rb'; P='001_Pokemon.rb'
WP18='wp18-creature-identity-species-ownership.md'
WP03='wp03-content-identity-and-schema.md'; WP04='wp04-pbs-lifecycle.md'
WP21='wp21-dynamic-forms-and-display.md'; WP36='wp36-wild-encounters-and-modifiers.md'
WP62='wp62-pokedex-records-regions-and-content.md'

# key, grammar, constructor default, form policy, meaning/receiver, owner route.
# The policies distinguish omission, explicit values, and whole-record fallback.
rows=[
('Name','s','Unnamed','SCALAR_BASE','Raw species name; translated Species.name/Pokemon.speciesName; not content identity.','ELR-I03'),
('FormName','q','nil','OWN_DEFAULT','Raw form label; no base-label inheritance. Pokedex receiver-name checks differ from source-name checks.','IF07'),
('PokedexForm','u','record form','OWN_DEFAULT','Display alias only; does not change data, stored form, battle form or resource request.','IF07'),
('MegaStone','e:Item','nil','OWN_DEFAULT','Registered item identity for naked Mega candidate selection, not MegaStone flag or battle permission.','IF02'),
('MegaMove','e:Move','nil','OWN_DEFAULT','Known move identity is alternative to stone, independent of current PP.','IF02'),
('UnmegaForm','u','0','OWN_DEFAULT','Current simplified source form must match for Mega candidate selection; current Mega record defines undo target.','IF02'),
('MegaMessage','u','0','OWN_DEFAULT','Message selector for the selected candidate; does not itself grant battle permission.','IF02'),
('Types','*e:Type','[NORMAL]','CLONE_BASE','Ordered registered type IDs; compilation uniq/compact, no hard two-type limit; Pokemon returns cloned list.','IF02'),
('BaseStats','vvvvvv','six main stats 1','CLONE_BASE','PBS columns HP/ATTACK/DEFENSE/SPEED/SPECIAL_ATTACK/SPECIAL_DEFENSE; Pokemon stat formula consumes named values.','IF08'),
('GenderRatio','e:GenderRatio','Female50Percent','SCALAR_BASE','Fixed ratio ID; nil female chance means single gender; otherwise PID low-byte threshold.','IF02'),
('GrowthRate','e:GrowthRate','Medium','SCALAR_BASE','Fixed six-curve identity for level/experience lookup, table precedes formula fallback.','IF08'),
('BaseExp','v','100','SCALAR_BASE','Positive author base experience; getter feeds foreign combat XP consumer, not actual awarded XP.','IF08'),
('EVs','*ev:Stat','six main yields 0','CLONE_BASE','Named positive yield pairs, repeated named stat last assignment; Pokemon evYield returns six named values.','IF08'),
('CatchRate','u','255','SCALAR_BASE','Raw capture difficulty input; successful capture depends on foreign capture consumer.','IF05'),
('Happiness','u','70','SCALAR_BASE','Raw initial happiness copied by initialize; no PBS255 cap; later normal change clamps0–255.','IF08'),
('Abilities','*e:Ability','[]','CLONE_BASE','Ordered natural ability IDs; PID parity index falls back to first. Effect logic is foreign combat primary.','IF02'),
('HiddenAbilities','*e:Ability','[]','CLONE_BASE','Ordered hidden IDs indexed2+; absent selected hidden entry falls back to natural parity.','IF02'),
('Moves','*ue:Move','[]','NESTED_BASE_IF_EMPTY','Ordered level/move pairs incl level0; retain raw repeats; reset keeps latest duplicate then lastMAX4. Evolution learns0/currentlevel via separate caller.','IF08'),
('TutorMoves','*e:Move','[]','CLONE_BASE','Ordered machine/tutor compatibility IDs; compatibility does not itself teach or consume an item.','IF08'),
('EggMoves','*e:Move','[]','CLONE_BASE','Raw egg list versus get_egg_moves ancestry fallback are different consumers; no automatic relearner full-list admission.','IF08'),
('EggGroups','*e:EggGroup','[Undiscovered]','CLONE_BASE','Exact fixed group identities used by breeding admission/roles; mere list existence does not prove compatible pair.','CD-I01'),
('HatchSteps','v','1','SCALAR_BASE','Positive species hatch count; generated egg steps and later hatching callback are distinct stages.','CD-I01'),
('Incense','e:Item','nil','SCALAR_BASE','Registered item at baby stage gates ancestry recursion; no blanket incense requirement for Pichu.','CD-I01'),
('Offspring','base:*s then final Species enumeration; form:*e:Species','[]','CLONE_BASE','Ordered alternate child identities; duplicate entries retain their sampling multiplicity; generation owned creature_d.','CD-I01'),
('Height','f','1 tenth metre','SCALAR_BASE','Accepted decimal multiplied10, rounded and max1; Pokemon height getter and owned Pokedex presentation consume tenths.','IF07'),
('Weight','f','1 tenth kilogram','SCALAR_BASE','Accepted decimal multiplied10, rounded and max1; Pokemon weight getter and owned Pokedex presentation consume tenths.','IF07'),
('Color','e:BodyColor','Red','SCALAR_BASE','Exact10-ID descriptor, translated label; distinct from encounter-derived Area map.','IF07'),
('Shape','e:BodyShape','Head','SCALAR_BASE','Exact14-ID descriptor/order/icon association; not a guarantee of image availability.','IF07'),
('Habitat','e:Habitat','None','SCALAR_BASE','Exact10-ID descriptive value; Area visibility is computed from encounters/map metadata instead.','IF06'),
('Category','s','???','SCALAR_BASE','Raw category independently translated, then gated by Pokedex ownership.','ELR-I03'),
('Pokedex','q','???','SCALAR_BASE','Full prose retained after line preprocessing; hash/comment stripping can precede q; translated entry not guaranteed literal raw prose.','ELR-I03'),
('Generation','i','0','SCALAR_BASE','Signed descriptive debut number; does not activate backup or select mechanics constants.','IF01'),
('Flags','*s','[]','CLONE_BASE','Case-insensitive exact flags; first DefaultForm_N controls base_form. Mother/EverStone/Legendary flags have distinct foreign consumers.','IF02'),
('WildItemCommon','*e:Item','[]','TRIPLE_BASE_IF_ALL_ABSENT','Common pool; any explicit one of triple suppresses inheritance of all three; equal nonempty pools can guarantee held identity.','IF09'),
('WildItemUncommon','*e:Item','[]','TRIPLE_BASE_IF_ALL_ABSENT','Uncommon pool; ordinary50/5/1 or lead60/20/5 cumulative generator branches, not independent three rolls.','IF09'),
('WildItemRare','*e:Item','[]','TRIPLE_BASE_IF_ALL_ABSENT','Rare pool; empty choice may remainnil, actual assignment validates registered item, not can_hold flag.','IF09'),
('Evolutions','base:*ses; form:*ees','[]','NESTED_BASE_IF_EMPTY','Legacy plural list precedes singular list by schema order; repeated ordinary plural property last-wins.','IF08'),
('Evolution','base:^seS; form:^eeS','[]','NESTED_BASE_IF_EMPTY','Repeated singular triples append in appearance order after plural; method parameter converted by method type; None/predecessor excluded from checks.','IF08'),
('BackSprite','ii','[0,0]','METRICS_OWN','Back x/y multiplied2 for even battler index; Pokedex back UI consumes vertical*2 separately.','IF03'),
('FrontSprite','ii','[0,0]','METRICS_OWN','Front x/y multiplied2 for odd index; hatch/trade direct call passes1.','IF03'),
('FrontSpriteAltitude','i','0','METRICS_OWN','Foe front y subtracts altitude*2; omitted in all2696 primary metric records.','IF03'),
('ShadowX','i','0','METRICS_OWN','Shadow branch only shifts foe x by2*value; not general body offset.','IF03'),
('ShadowSize','u','2','METRICS_OWN','Generic shadow resource size after explicit species/form shadow fallback; custom shadow bypasses editing size.','IF03'),
('ENCOUNTER_TYPE','registered EncounterType + optional to_i chance','type trigger chance','ENCOUNTER','First missing chance uses type default; repeat type replaces slots but omittedchance retains prior chance.','IF05'),
('SLOT','positive weight, Species, min, optional max','max=min','ENCOUNTER','Registered species/form,1..maxlevel andmin<=max; merge identical species/range then descendingweight/species sort; local weighted inclusive choice.','IF05')]
contracts=[]
for i,(key,grammar,default,policy,meaning,route) in enumerate(rows,1):
    ident=f'FC{i:02}'
    metric=policy=='METRICS_OWN'; enc=policy=='ENCOUNTER'
    source=[at('010_SpeciesMetrics.rb',17,101)] if metric else [at(C,658,763),at('013_Encounter.rb',1,71)] if enc else [at(S,52,111),at(S,175,226),at(C,281,541)]
    spec=[at(WP03,135,164),at('wp73-b-world-editors.md',120,168)] if metric else [at(WP36,49,123),at(WP04,148,162)] if enc else [at(WP18,49,102),at(WP04,130,147)]
    if key=='ShadowSize':
        source.append(at('009_Species_files.rb',1,246))
        spec.append(at('wp15-resource-matching-and-audio.md',53,70))
    getter={'Name':'speciesName','Types':'types','BaseStats':'baseStats','EVs':'evYield',
        'GenderRatio':'gender','GrowthRate':'growth_rate','BaseExp':'base_exp','Happiness':'initialize',
        'Abilities':'ability_id','HiddenAbilities':'ability_id','Moves':'reset_moves',
        'TutorMoves':'compatible_with_move?','EggMoves':'compatible_with_move?',
        'Height':'height','Weight':'weight','WildItemCommon':'wildHoldItems',
        'WildItemUncommon':'wildHoldItems','WildItemRare':'wildHoldItems'}.get(key)
    if getter: source.append(method(P,getter))
    if key in {'EggMoves','EggGroups','Incense','Offspring','Evolution','Evolutions'}:
        source.append(at(S,250,415))
    # Finite explicit four-way decomposition, not one physical line == one clause.
    atoms=[('grammar','Accepted author grammar: '+grammar),('default','Omitted base/explicit metric record constructor value: '+default),('form','Omitted form disposition: '+policy),('consumer',meaning)]
    schema_scope='METRICS' if metric else 'ENCOUNTER' if enc else 'BASE_ONLY' if key in {'Name','GenderRatio','GrowthRate','Incense'} else 'FORM_ONLY' if key in {'PokedexForm','MegaStone','MegaMove','UnmegaForm','MegaMessage'} else 'BASE_AND_FORM'
    contracts.append(dict(id=ident,key=key,grammar=grammar,author_schema_scope=schema_scope,default=default,form_policy=policy,meaning=meaning,route=route,
        source=source,spec=spec,atoms=[dict(id=ident+'.'+k,assertion=t,source=source,spec=spec,local_status='SOURCE_STATIC_FINITE_CONTRACT_CHECKED',acceptance='PENDING_MAIN_REVIEWER') for k,t in atoms]))
bykey={x['key']:x for x in contracts}
species_keys=[x[0] for x in rows if x[3] not in ['METRICS_OWN','ENCOUNTER']]
base_schema=set(species_keys)-{'PokedexForm','MegaStone','MegaMove','UnmegaForm','MegaMessage'}
form_schema=set(species_keys)-{'Name','GenderRatio','GrowthRate','Incense'}
metrics_schema={'BackSprite','FrontSprite','FrontSpriteAltitude','ShadowX','ShadowSize'}

# Each exact field instance is bound only AFTER full actual file reading.
assert len(ledger['primary'])==16 and all(f['file_status']=='FULL_READ' for f in ledger['primary'])
records=[]; base_index={}; field_count=0; omitted_count=0; primitive_count=0
for f in ledger['primary']:
    if f['path'].endswith('/pokemon.txt'):
        for s in f['all_sections']:base_index[(f['path'].split('/')[1],s['section'])]=s
for f in ledger['primary']:
    lines=(REF/f['path']).read_text(encoding='utf-8-sig').splitlines()
    kind='BASE' if f['path'].endswith('/pokemon.txt') else 'FORM' if f['path'].endswith('/pokemon_forms.txt') else 'METRICS' if f['path'].endswith('/pokemon_metrics.txt') else 'ENCOUNTER'
    for s in f['all_sections']:
        fields=[]; present=collections.defaultdict(list)
        for n,key in s['fields_line_key']:
            contract=bykey[key]; present[key].append(n)
            raw=lines[n-1]; value=raw.split('=',1)[1].strip() if '=' in raw else raw.strip()
            isprose=key in {'Name','FormName','Category','Pokedex'}
            arity=1 if isprose else len(value.split(','))
            fields.append([n,key,contract['id'],hashlib.sha256(value.encode()).hexdigest(),arity])
            field_count+=1;primitive_count+=arity
        base=None
        if kind=='FORM':
            species=s['section'].split(',')[0].strip()
            base=base_index.get((f['path'].split('/')[1],species));assert base,(f['path'],s['section'])
        eligible=species_keys if kind in ['BASE','FORM'] else sorted(metrics_schema) if kind=='METRICS' else []
        omitted=[]
        for key in eligible:
            if key in present:continue
            c=bykey[key];policy=c['form_policy']; target=None
            if key in {'Evolution','Evolutions'} and any(k in present for k in {'Evolution','Evolutions'}):
                disposition='ALTERNATIVE_SPELLING_ABSENT_LOGICAL_EVOLUTION_EXPLICIT'
            elif kind=='FORM' and policy in {'SCALAR_BASE','CLONE_BASE','NESTED_BASE_IF_EMPTY','TRIPLE_BASE_IF_ALL_ABSENT'}:
                if policy=='TRIPLE_BASE_IF_ALL_ABSENT' and any(k in present for k in ['WildItemCommon','WildItemUncommon','WildItemRare']):
                    disposition='OWN_EMPTY_POOL_AFTER_OTHER_POOL_EXPLICIT'
                else:
                    disposition=policy;target=base['id']
            else:disposition='BASE_CONSTRUCTOR_DEFAULT' if kind=='BASE' else 'EXPLICIT_METRICS_OWN_DEFAULT' if kind=='METRICS' else 'FORM_OWN_CONSTRUCTOR_DEFAULT'
            # Name/GenderRatio/GrowthRate/Incense inherit even though absent from form schema.
            omitted.append([key,c['id'],disposition,target]);omitted_count+=1
        records.append(dict(section_id=s['id'],identity_id=f['identity_id'],kind=kind,source_lines=s['lines'],
            header_contract='HC-'+kind,base_section=(base['id'] if base else None),fields=fields,omitted=omitted,
            local_status='ALL_LITERAL_CONTENT_READ_AND_FINITE_BINDINGS_REVIEWED',acceptance='PENDING_MAIN_REVIEWER'))

# Control-flow assertions manually separated from per-field types/defaults.
global_rows=[
('G01','Ordinary top-level PBS discovery does not recurse into Gen5–8 backups.', '001_Compiler.rb',967,1037,WP04,59,65,'IF01'),
('G02','Mechanics-generation constants and backup data selection are different inputs; no compatibility guarantee from a folder name.','001_Settings.rb',10,17,'wp02-rule-configuration-and-data-variants.md',215,245,'IF01'),
('G03','Base record strict symbol identity and registered positive form section convert to compound identity before duplicate rejection.',C,388,475,WP18,49,58,'IF02'),
('G04','Form scalar omission copies base; collection omission clones; nested moves/evolution empty list inherits member copies.',C,454,497,WP18,49,58,'IF02'),
('G05','Allthree wild pools inherit together only if all absent; oneexplicit suppresses wholetriple inheritance.',C,489,497,WP18,49,58,'IF09'),
('G06','Absent form label remainsnil and Pokedex alias defaults to ownform, distinct from inherited category/prose.',S,175,226,WP18,84,102,'IF07'),
('G07','Species lookup missing requested form falls back base; missing base returnsnil, not a newly created Species.',S,154,162,WP18,49,58,'IF02'),
('G08','Metrics whole missing form lazily copiesbase/default; explicitpartial record usesown defaults, nofield-byfield inheritance.','010_SpeciesMetrics.rb',30,68,WP03,135,164,'IF03'),
('G09','Lazy metricnewform coordinates independentarrays andsuffixempty, not inheritedbasesuffix.','010_SpeciesMetrics.rb',30,68,'wp73-b-world-editors.md',148,168,'IF04'),
('G10','Metrics normal body even/odd index and shadow branch differ; scale2 andaltitude onlyfoe front.','010_SpeciesMetrics.rb',71,87,'wp73-b-world-editors.md',120,168,'IF03'),
('G11','Current fixed shows_shadow? returns true; commented altitude-only alternative is inactive.','010_SpeciesMetrics.rb',89,92,'wp73-b-world-editors.md',120,168,'IF03'),
('G12','Metricsexport paths derive onlynonzeroform suffixes; equal form suppressessection, notselectedpath.','003_Compiler_WritePBS.rb',291,352,'wp73-b-world-editors.md',148,168,'IF04'),
('G13','EditorYes savesbinarybeforePBS, No reloadsbinary; noexisting battlelayout broadcast.','004_EditorScreens_SpritePositioning.rb',92,106,'wp73-b-world-editors.md',148,168,'IF04'),
('G14','Metricwriter laterfailure cannotrollback already savedbinary; directfileopen cantruncate orpartiallywrite.','003_Compiler_WritePBS.rb',291,352,'wp73-b-world-editors.md',148,168,'IF04'),
('G15','Directencounterquery prefersversion then0; exists? onlyexact version.','013_Encounter.rb',20,43,WP36,49,54,'IF05'),
('G16','Normal Symbol-key versioniterator yields v0 aswellas v>0; notsamequery fallback.','013_Encounter.rb',45,59,WP36,49,54,'IF06'),
('G17','Encountercompiler omittedmaximum=min, mergeduplicate slots thenweight/species sort.',C,658,763,WP36,56,67,'IF05'),
('G18','Repeat encountertype replaces slots, omittedchance keeps priorchance; duplicate mapversion rejected afterfirstregistration.',C,658,763,WP04,148,162,'IF05'),
('G19','Setup refreshes independenttables andgracesteps butdoesnotresetaccumulator.','003_Overworld_WildEncounters.rb',1,46,WP36,69,82,'IF05'),
('G20','Version setter samevalueearlyreturns; actualintegerchange writesversionthen conditionallysetupsnapshot.','002_Overworld_Metadata.rb',114,119,'wp73-b-world-editors.md',108,118,'IF05'),
('G21','Wilditem equalnonemptytriple selectscommon; otherbranch cumulative50/5/1 or60/20/5; assignment validatesitemidentity.','003_Overworld_WildEncounters.rb',383,447,WP36,178,206,'IF09'),
('G22','Ordinarydexregister checksaliasreceivername; recentseen checkssourceformname while storingalias.','005_Player_Pokedex.rb',197,236,WP62,84,108,'IF07'),
('G23','Area versioniterator contribution additionally requiresvalidmap metadata, matchingregion, visibilitypointand nothidden.','004_UI_Pokedex_Entry.rb',301,351,WP62,120,167,'IF06'),
('G24','Formslisting excludesaliases/unnamed alternate records and appliesseen/config/gender gates; movement writeslastseen, BACK doesnotrestore.','004_UI_Pokedex_Entry.rb',160,214,WP62,169,183,'IF07'),
('G25','Dynamicform resourcegetter cancommit beforelookup; forced/battle/storage guards andsimplifiedgetter differ.',P,116,195,WP21,177,206,'IF02'),
('G26','Nakedformsetter always writesclearability/handler/recalc/conditionaldex even samevalue; simplifiedsetter onlywrite/recalc.',P,151,195,WP21,187,205,'IF02'),
('G27','Mega candidate firstmatchingregisteredtarget withsourceformmatch andstoneORmove; barequery isnotbattlepermission.','002_Pokemon_MegaEvolution.rb',6,55,'wp22-mega-and-primal-reversion.md',28,45,'IF02'),
('G28','BarePrimal currentidentity dependscurrentitemhandler result; absentorb mayleave stored1withfalseidentity.','002_Pokemon_MegaEvolution.rb',61,83,'wp22-mega-and-primal-reversion.md',66,74,'IF02'),
('G29','Evolution forwardmerge pluralbefore singular; reversepredecessor firstdiscovered withcorrespondingformpriority.',C,330,541,'wp31-basic-evolution.md',113,123,'IF08'),
('G30','Ordered evolutionchecks returnfirsttarget behindegg/Shadow/Everstone/BattleBond guards; None/predecessor notexecutable.',P,974,1080,'wp31-basic-evolution.md',124,150,'IF08'),
('G31','Fullplayer/global/storage savevaluesbindobjects, ordinarycurrentversionload assignsdeserializedvalues ratherthan regeneratePokemonfromPBS.','004_Game_SaveValues.rb',1,127,WP18,1,44,'IF07'),
('G32','Save hashvalidation thenMarshalwrite, conversion callbacks andloadassignment have no allgraph atomicrollbackpromise.','001_SaveData.rb',24,60,WP04,210,258,'IF01')]
assertions=[]
for ident,claim,src,a,z,sp,x,y,route in global_rows:
    assertions.append(dict(id=ident,assertion=claim,source=[at(src,a,z)],spec=[at(sp,x,y)],route=route,
        premises='Fixed B8/R, named valid registered inputs and earlier calls/dependencies successful, no plugin override; actual engine/media/host NOT_EXECUTED.',
        local_status='FINITE_SOURCE_STATIC_CHECKED',acceptance='PENDING_MAIN_REVIEWER'))
    if ident=='G24': assertions[-1]['source'].append(at('004_UI_Pokedex_Entry.rb',460,619))
    if ident in {'G11','G31','G32'}:
        assertions[-1]['spec']=[]
        assertions[-1]['local_status']='SOURCE_PREMISE_ONLY; FOREIGN_FORMAL_RECEPTION_PENDING'
        assertions[-1]['foreign_formal_scope']='IF03 combatpresentation shadowgate' if ident=='G11' else 'IF01/IF07 KERNEL fullsave/migrationformal; not PBSbinarysave'
headers=[dict(id='HC-'+k,assertion=t,source=src,spec=sp) for k,t,src,sp in [
('BASE','Newsymbolidentity m; records stayconditionalbackupauthorinstances.',[at(S,52,62)],[at(WP18,49,58)]),
('FORM','Registeredbase Species pluspositiveform; samegenerationbase anchor mandatory.',[at(S,52,69),at(C,454,475)],[at(WP18,49,58)]),
('METRICS','Speciesenum plusoptionalpositiveform; omittedslot0, explicitnonempty0 rejected.',[at('010_SpeciesMetrics.rb',17,24)],[at(WP03,172,199)]),
('ENCOUNTER','Specialized map/versionto_i header; missingversion0 andduplicatekey separate.',[at(C,658,763)],[at(WP04,148,162)])]]
write('field-contracts.json',dict(schema='r8-xpcb-reviewed-field-contracts/v1',utc=UTC,reviewer='/root',contracts=contracts,headers=headers,
    common_premises='Backupfilesarealternativeauthorinputs, notautomaticallyloaded. All referencedregistries/selecteddataset/hostdependencies mustindependentlysucceed. Fieldmeaningreview doesnotcertifyany wholebackupcompile or actualeffect.',
    explicit_limit='No reference source corpus copied; exact literal values remain recoverable from identities and coordinates. All were actuallyread before hashing.'))
write('forward-mapping.json',dict(schema='r8-xpcb-forward-mapping/v2',utc=UTC,reviewer='/root',status='PRIMARY_FINITE_MAPPING_COMPLETE_PENDING_MAIN',
    field_columns=['line','key','field_contract_id','value_sha256_utf8_after_property_split','primitive_csv_positions_or_prose1'],
    omitted_columns=['key','field_contract_id','default_or_inheritance_disposition','base_section_or_null'],
    records=records,global_assertions=assertions,section_denominator=len(records),physical_field_denominator=field_count,
    omitted_dispositions=omitted_count,primitive_value_positions_mechanical=primitive_count,
    local_semantic_rule='Every literal/list/prose source was read. These enumerations bind reviewer-authored contracts; they add no reading or independent reception.',
    unresolved_local_primary_fields=0,accepted_sections=0,foreign_consumer_reception='central-contract-projection.json; all9 finalinterfaces pending main'))
reverse=[]
for c in contracts:
    for atom in c['atoms']:
        reverse.append(dict(atom,source_field_key=c['key'],source_instances_selector='forward-mapping.json records[].fields key=='+c['key'],
            omission_selector='forward-mapping.json records[].omitted key=='+c['key'],route=c['route'],
            premises='Valid activated compatible authorinput andregisteredreferences; literalvalue doesnotcertify foreigneffect/host.'))
reverse+=assertions
write('reverse-mapping.json',dict(schema='r8-xpcb-reverse-mapping/v2',utc=UTC,status='FINITE_APPLICABLE_ASSERTIONS_COMPLETE_PENDING_MAIN',
    atomic_assertions=reverse,atomic_assertion_denominator=len(reverse),header_assertions=headers,
    complete_formal_global_denominator='NOT_CLAIMED:131formal files are globalmain/primaryresponsibilities; this taskformalprimary0.',
    owned_assertion_scope='All primary fieldtype/default/forminherit/necessarygetter/compile/export/encounter/metrics/localizationproducer joins; unrelated formal clauses in fullyread foreignfiles retain actualprimaryowner.',
    physical_line_inventory='reading-ledger.json; not used as semantic clause count',accepted=0,
    local_discrepancy='No new demonstratedrequiredchange within finiteclaimscope; withdrawnGR8-XPCB-001 retained for independentmain decision.'))

central=read('central-contract-projection.json')
interfaces=[]
for x in central['interfaces']:
    if x['primary']!='pbs_creature_backups':continue
    ident=x['id']; local=[g['id'] for g in assertions if g['route']==ident]
    interfaces.append(dict(id=ident,chain=x['complete_original_interface']['chain'],finite_contract=x['finite_contract'],
        receiver_routes=x['receiving_owner_routes'],local_assertion_ids=local,
        field_contract_ids=[c['id'] for c in contracts if c['route']==ident],
        local_status='NECESSARY_FIELD_AND_DIRECT_RECEIVER_EVIDENCE_DELIVERED',
        status='PENDING_MAIN_CUMULATIVE_RECEPTION',business_execution='NOT_EXECUTED',
        remaining='External actualprimary consumerfacets and finalmain receipt; navigation/ownerassignmentisnotreception.',
        central_contract_commit=central['commit']))
for ident in ['ELR-I03','CD-I01','CD-I06']:
    x=next(v for v in central['interfaces'] if v['id']==ident and v['primary']!='pbs_creature_backups')
    interfaces.append(dict(id=ident,foreign_primary=x['primary'],finite_contract=x['finite_contract'],
        local_status='PRIMARY_RECORD_FIELDS_AND_ACTIVATION_SOURCE_PROVIDED',
        source_selector='forward-mapping.json all8BASE/FORMpaths' if ident=='ELR-I03' else 'forward-mapping.json allapplicableSpecies/Encounters/metrics',
        status='PENDING_MAIN_CUMULATIVE_RECEPTION',acceptance_credit=0))
write('interfaces.json',dict(schema='r8-xpcb-finite-interfaces/v2',utc=UTC,interfaces=interfaces,
    original_nine_interface_count=9,additional_inbound_field_joins=3,accepted_interfaces=0,
    root_receiver=central['final_receiver'],central_contract_commit=central['commit'],
    no_children=True,update_started=False,external_primary_full_file_reassignment=False))

# Preserve original candidate and its complete independent-disproof requirements.
proposal=read('proposals.json'); proposal['utc']=UTC
proposal['reason']='Primary full reading and finite mappings delivered. Main independent disproof and cumulative reception remain pending; no global NO_REQUIRED_UPDATE decision.'
proposal['records'][0]['dependency']['blocking']='Independent main disproof/final reception; foreign finite interfaces owned by exact central routes.'
proposal['records'][0]['dependency']['batch']='NONE; UPDATE_NOT_STARTED'
write('proposals.json',proposal)
route=read('dependency-routing.json')
for e in route['entries']:
    note=notes['dependencies'].get(e['path']);assert note,e['path']
    k=next(k for k,v in ids.items() if k.startswith('D') and v['path']==e['path'])
    dep=next(v for v in ledger['read_dependencies'] if v['identity_id']==k)
    e.update(status=dep['read_status'],read_ranges=dep['read_ranges'],personal_unread_ranges=dep['unread_ranges'],
        local_necessary_scope='Applicable directdefinition/fieldjoin read; foreignremainder retained at actualprimary, not localexhaustiveforeignfilework.',
        unreceived=True,blocking='Final global acceptance only; unreadforeignremainder not auto localprimarygap.',owner_credit='ROUTED_NOT_RECEIVED',identity_id_current=k)
route.update(utc=UTC,metadata_only=False,central_contract_commit=central['commit'],original_discovered_paths=40,
    whole_foreign_file_credit=False,finite_local_evidence='field-contracts/reverse-mapping/interfaces',final_receiver=central['final_receiver'])
write('dependency-routing.json',route)
counts=ledger['counts'];counts['discovered_unread_dependency_files']=0
counts['dependency_files_with_personal_unread_remainder']=sum(bool(x['unread_ranges']) for x in ledger['read_dependencies'])
counts['dependency_personal_unread_line_positions']=sum(b-a+1 for x in ledger['read_dependencies'] for a,b in x['unread_ranges'])
counts['local_atomic_assertions']=len(reverse);counts['primary_omission_dispositions']=omitted_count
ledger['semantic_subassertion_denominator']=dict(primary_sections=6712,physical_fields=field_count,
    omission_dispositions=omitted_count,reviewer_authored_finite_atomic_assertions=len(reverse),header_contracts=4,
    warning='Different denominators; physicalpositions and hashes are not independentsemanticorreadcredit.')
ledger['utc']=UTC
for f in ledger['formal_read_decomposition_status']:
    f['semantic_clause_subassertion_denominator']='Applicable namedatoms in reverse-mapping; foreignwholefile clauses notclaimed'
    f['unmapped_semantic_subassertions']='Foreignprimaryremainder/clauses routed, not granted localsupport'
write('reading-ledger.json',ledger)
write('coverage.json',dict(schema='r8-xpcb-final-coverage/v2',utc=UTC,counts=counts,
    semantic_forward_complete_for_owned_primary=True,semantic_reverse_complete_for_finite_applicable_contracts=True,
    all_formal_global_complete=False,foreign_interfaces_accepted=0,main_primary_sections_accepted=0,
    classification_decisions=dict(required=0,optional=0,no_required_revision=0,policy=0,limit=0),
    local_questions=1,withdrawn_as_already_documented=1,independently_decided_questions=0,
    NO_REQUIRED_UPDATE=False,update_started=False))
write('gaps.json',dict(schema='r8-xpcb-final-gaps/v2',utc=UTC,status='LOCAL_PRIMARY_DELIVERED_MAIN_RECEPTION_PENDING',
    primary_unread=[],primary_unmapped_fields=[],primary_unreceived_sections=6712,
    original40_dependency_routes='dependency-routing.json; all40 at least necessarysource/clausesread, exactforeignremainder preserved',
    all_personal_dependency_unread=[dict(identity_id=x['identity_id'],path=x['path'],ranges=x['unread_ranges'],
        disposition='FOREIGN_PRIMARY_REMAINDER; NOT_PERSONAL_FULL_READ; MAIN_RECEPTION_PENDING') for x in ledger['read_dependencies'] if x['unread_ranges']],
    unreceived=['9originalfiniteinterfaces','3inboundfieldjoins','Main independent disproof of withdrawnGR8-XPCB-001','Main finalclassification/6712sectionreception'],
    execution='All behavior/runtime/compile/writer/game/save/host vectors NOT_EXECUTED; zero.',
    unverified=['actualmodel/effort/tier/Fast/sessionID','complete raw platform transcript export','historical canonical proposal relation beyond fixed supplied contract'],
    real_environment_permission_or_material_blockers=[],material_limit_claim=False,
    boundary='Main exactfinitecrossdomaincontract keeps foreignprimary ownership; this report cannot invent mainreception or NO_REQUIRED_UPDATE.'))
progress=read('progress.json');progress.update(updated_utc=UTC,status='LOCAL_PRIMARY_REVIEW_COMPLETE_PENDING_MAIN',
    semantic_status='OWNED_PRIMARY_AND_FINITE_MAPPING_DELIVERED',failure_reason=None,
    read_complete_files=16,partial_read_files=0,unread_files=0,read_complete_primary_sections=6712,
    unread_or_partial_primary_sections=0,unreceived_primary_sections=6712,
    read_line_positions=102507,primary_fields_read=field_count,local_atomic_assertions=len(reverse),
    process_state='Sameactualrootcontextcontinued; nochildspawn; necessaryforeigninterfacesfiniteboundbyea335928.',
    publication='Final ordinarypush/readback pending; previous962204c incompletecheckpoint superseded onlyafterfinalpublication.',
    semantic_acceptance='PENDING_MAIN_REVIEWER',update_started=False,end_utc='UNVERIFIED_UNTIL_TURN_END')
write('progress.json',progress)
print(json.dumps(dict(sections=len(records),fields=field_count,omissions=omitted_count,atoms=len(reverse),
    dependency_count=len(ledger['read_dependencies']),personal_partial_dependencies=counts['dependency_files_with_personal_unread_remainder'],
    personal_unread_dependency_lines=counts['dependency_personal_unread_line_positions'])))
