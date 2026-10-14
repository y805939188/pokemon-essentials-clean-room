"""Review evidence joins; pending semantic work is never promoted to PASS."""
import audit as a, relations as r
from collections import Counter, defaultdict
from pathlib import Path
import json,re,gzip

def read(name):
    x=json.loads((a.OUT/name).read_text())
    return json.loads(gzip.decompress((a.OUT/x['artifact']).read_bytes())) if isinstance(x,dict) and x.get('artifact_encoding')=='gzip_json' else x
def L(path,start,end=None):return {'path':path,'start_line':start,'end_line':end or start}
SPEC='deliverables/final-specification-set/'
SRC='reference/pokemon-essentials/Data/Scripts/'
CORE=SRC+'014_Pokemon/001_Pokemon.rb'
SHADOW=SRC+'014_Pokemon/003_Pokemon_ShadowPokemon.rb'
BERRY=SRC+'012_Overworld/006_Overworld_BerryPlants.rb'
MV=SRC+'011_Battle/003_Move/001_Battle_Move.rb'
TYPE=SRC+'010_Data/002_PBS data/003_Type.rb'
CP=r.COMPILER
WP03=SPEC+'generic-kernel/wp03-content-identity-and-schema.md'
WP04=SPEC+'generic-kernel/wp04-pbs-lifecycle.md'
WP02=SPEC+'generic-kernel/wp02-rule-configuration-and-data-variants.md'
WP23=SPEC+'pokemon-rules/wp23-shadow-data-and-vectors.md'
WP43=SPEC+'pokemon-rules/wp43-types-accuracy-and-damage.md'
WP60=SPEC+'pokemon-rules/wp60-berry-plants.md'
WP27=SPEC+'creature-rpg/wp27-bag-and-item-storage.md'
TEST=SPEC+'test-catalog/generic-kernel-wp02-03-04.md'

def fact(fid,behavior,source,consumer,spec,preconditions,extent='REVIEWED_LIMITED_STATIC_CONTRACT'):
    return {'fact_id':fid,'behavior':behavior,'source':source,'necessary_consumers':consumer,'formal_clauses':spec,'preconditions':preconditions,'status':extent,'preserved_scope':'Fixed reference behavior only; not architecture, execution evidence, official game guarantees, or variant support certification.'}

FACTS=[
 fact('D01','Type matchup entries belong to defending types. A listed weakness contributes 2, resistance 1/2, immunity 0, otherwise 1. Conflicting authored memberships use weakness before resistance before immunity.',[L(TYPE,18,27),L(TYPE,61,67)],[L(TYPE,130,139)],[L(WP43,43,47)],'Registered type identities and ordinary base matchup evaluation; battle-specific overrides are separate.'),
 fact('D02','Type list duplicates are removed per record; undefined listed counterpart types fail whole-table validation after records have been registered.',[L(CP,149,171)],[L(CP,143,146),L(CP,54,67)],[L(WP03,170,176)],'Generic Type compiler reached normally; no automatic transaction rollback claimed.'),
 fact('D03','Ability names/descriptions have omission defaults; flags are data strings and flag comparisons ignore letter case.',[L(r.SCHEMA_DIR+'004_Ability.rb',16,28),L(r.SCHEMA_DIR+'004_Ability.rb',31,43)],[L(CP,190,199)],[L(WP03,95,100),L(TEST,113)],'Valid unique identity and ordinary dependencies; raw values and localized output are separate.'),
 fact('D04','FasterEggHatching is consumed by the step callback: after the first decrement, scan current non-egg party members, apply one extra decrement at the first matching active ability flag, then stop.',[L(r.SCHEMA_DIR+'004_Ability.rb',41,43)],[L(SRC+'016_UI/001_Non-interactive UI/003_UI_EggHatching.rb',252,268)],[L(SPEC+'creature-rpg/wp35-eggs-and-hatching.md',75,80)],'Normal step event, current player/party and ability access successful; callbacks and hatch presentation normal.'),
 fact('D05','A move Status category with positive power is rejected. Physical/Special with zero or omitted power warns and becomes Status; valid positive damage values survive this check.',[L(CP,211,218)],[L(CP,54,67)],[L(WP04,137,146),L(TEST,106,108)],'New unique move, lexical fields and enum references valid, warning returns normally; no full-table save until normal completion.'),
 fact('D06','Move effect names are text identities. Missing named runtime effect uses generic fallback rather than enum parse rejection: Status fails at the move gate, damaging categories retain ordinary damage without a special effect.',[L(r.SCHEMA_DIR+'005_Move.rb',22,35)],[L(MV,57,68),L(SRC+'011_Battle/003_Move/004_Move_BaseEffects.rb',10,17)],[L(WP43,29,35),L(WP23,225,228)],'Valid move already registered and ordinary action gates reached; no added matching implementation or plugin; caller-specific PP remains separate.'),
 fact('D07','Battle move construction reads type, category, power, accuracy, target, priority, flags and additional-effect chance from move data.',[L(r.SCHEMA_DIR+'005_Move.rb',22,35)],[L(MV,34,49)],[L(WP03,102),L(WP04,139,146)],'Valid move instance and battle construction; later effective-value overrides and move-specific effects remain unreviewed here.'),
 fact('D08','Data effect chance 101 is a legal nonnegative integer. The additional-effect chance consumer preserves values above 100 before doubling or debug override, after the Shield Dust gate.',[L(r.SCHEMA_DIR+'005_Move.rb',34)],[L(SRC+'011_Battle/003_Move/003_Move_UsageCalculations.rb',489,498)],[L(WP43,157)],'This exact chance calculation reached with effective target ability/mold-breaker state; later invocation and actual application remain separate.'),
 fact('D09','Item omission defaults include pocket 1, price 0, sell price integer half of purchase price, BP price 1, no field/battle use. Importance means KeyItem/TM/HM, and effective consumption requires a non-important item.',[L(r.SCHEMA_DIR+'006_Item.rb',119,137),L(r.SCHEMA_DIR+'006_Item.rb',171,201)],[L(r.SCHEMA_DIR+'006_Item.rb',196,201)],[L(WP27,45,67)],'Valid registered item and relevant direct query; use eligibility, action execution, bag bounds and UI drawing are separate.'),
 fact('D10','Portion names omitted from an item fall back separately to ordinary singular and plural names. Their localization remains distinct.',[L(r.SCHEMA_DIR+'006_Item.rb',140,164)],[L(r.SCHEMA_DIR+'006_Item.rb',151,159)],[L(WP03,108),L(TEST,116)],'Raw portion field missing, or present nonempty localization lookup as stated; PBS empty field is not assumed to be a stored empty string.'),
 fact('D11','Berry numeric schema: positive hours, nonnegative drying, nonnegative first yield and positive second yield. Construction supplies 3/15/2,5 when missing, and reverses yields if the second is smaller.',[L(r.SCHEMA_DIR+'007_BerryPlant.rb',13,18),L(r.SCHEMA_DIR+'007_BerryPlant.rb',28,42)],[L(BERRY,83,105)],[L(WP60,43,49)],'A registered berry record; a missing whole record is a different strict lookup failure.'),
 fact('D12','Berry record identity is a symbolic section key; no Item enum exists in its schema and both berry validators are empty. Runtime interaction associates the identity with item content.',[L(r.SCHEMA_DIR+'007_BerryPlant.rb',13,18),L(CP,268,278)],[L(BERRY,83,105)],[L(WP04,118),L(WP60,49)],'Compiler/runtime stages separated; item existence and berry flag eligibility do not establish berry data existence.'),
 fact('D13','Berry stage duration is hours times 3600. New-mechanic yield uses the integer quotient of maximum times (5-penalty) over 5, bounded below by minimum; old watering yield uses the configured range.',[L(r.SCHEMA_DIR+'007_BerryPlant.rb',37,42)],[L(BERRY,83,92),L(BERRY,97,159)],[L(WP60,74,82),L(WP60,136,143)],'Planted state and forward time for update, no mulch unless explicitly chosen; random/sample calculations do not execute the game.'),
 fact('D14','Base species and form author schemas differ. Fields absent in forms inherit from base in named groups, while any explicit wild-item family prevents inheriting all three wild-item groups.',[L(r.SCHEMA_DIR+'008_Species.rb',52,109)],[L(CP,448,484)],[L(WP03,120),L(WP04,112,113)],'Valid base species already registered; form identity conversion and prior validation normal. Detailed runtime form handlers remain separate.'),
 fact('D15','Species base-stat author columns map HP, attack, defense, speed, special attack, special defense; EV output uses stat-name/positive-value pairs, and repeated stat keys retain the later value during hash construction.',[L(r.SCHEMA_DIR+'008_Species.rb',69,75)],[L(CP,292,306)],[L(WP03,180,188)],'Six positive authored base stats; hardcoded main stat PBS order and legal stat identities required. Battle/stat formulas are separate.'),
 fact('D16','Species height and weight are converted to tenths, rounded, and bounded below by one; omitted forms inherit base values.',[L(r.SCHEMA_DIR+'008_Species.rb',91,92)],[L(CP,308,310),L(CP,462,465)],[L(WP04,96,98),L(TEST,89,92)],'Prior lexical float acceptance; this review instrument does not reproduce all malformed input parsing.'),
 fact('D17','Evolution target/parameter and offspring references include deferred validation. Required evolution parameters are checked before registration; base finalization converts parameter kinds and builds first-found reverse ancestry.',[L(r.SCHEMA_DIR+'008_Species.rb',85,108)],[L(CP,311,324),L(CP,332,365)],[L(WP03,174,176),L(WP04,152),L(TEST,141,147)],'Registry phase and record order matter; absence-free literal relation joins do not certify all temporal prerequisites or callbacks.'),
 fact('D18','Level-up move reset filters by current level in authored order, retains the last occurrence of duplicate moves, and takes the final maximum-move-count entries.',[L(r.SCHEMA_DIR+'008_Species.rb',80)],[L(CORE,620,641)],[L(SPEC+'creature-rpg/wp30-growth-learning-and-friendship.md',1)],'Valid current species data and level; full WP30 contract has not been read, so the destination is only a scope pointer.','SOURCE_REVIEWED_FORMAL_DESTINATION_PENDING'),
 fact('D19','Tutor move compatibility uses membership. Duplicate TutorMoves atoms do not create an extra affirmative compatibility result.',[L(r.SCHEMA_DIR+'008_Species.rb',81)],[L(CORE,708,714)],[L(SPEC+'creature-rpg/wp30-growth-learning-and-friendship.md',1)],'Valid registered queried move; this only resolves the membership result, not all tutoring workflows.','SOURCE_REVIEWED_FORMAL_DESTINATION_PENDING'),
 fact('D20','Metrics section identity references a species and optional positive form. Missing metric lookup for a valid species registers defaults or a cloned base metric, and sprite adjustment doubles configured offsets.',[L(r.SCHEMA_DIR+'010_SpeciesMetrics.rb',17,23)],[L(r.SCHEMA_DIR+'010_SpeciesMetrics.rb',32,56),L(r.SCHEMA_DIR+'010_SpeciesMetrics.rb',59,80)],[L(WP03,112,114),L(TEST,24)],'Valid existing species; record mutation and source suffix of generated data remain observable; full metric rendering/export clauses pending.'),
 fact('D21','Shadow input is optional. Gauge is positive, default 4000; ordered move IDs are filtered by runtime existence and capped at MAX_MOVES during conversion. Missing per-form record falls back to base; missing all data retains default gauge and may use SHADOWRUSH if registered.',[L(r.SCHEMA_DIR+'011_ShadowPokemon.rb',11,22),L(r.SCHEMA_DIR+'011_ShadowPokemon.rb',35,53)],[L(SHADOW,32,43),L(SHADOW,114,139)],[L(WP23,61,67)],'Conditional valid loading of the optional overlay; no automatic activation or reference compilation performed.'),
 fact('D22','Current active bulk families exactly match their Gen 8 backup bytes. Metrics are identical in all five profiles; modern berry/type files have additional exact-byte duplicates. This proves data identity only.',[],[],[L(WP02,227,236)],'44 individually Git-blob-checked files at fixed snapshot. Other backup content and settings cannot be certified by these byte matches.','REVIEWED_FIXED_INPUT_IDENTITY_ONLY'),
]

def run():
    a.bind();records=r.readrecords();domains=read('field-value-domains.json');files=read('file-inventory.json')
    a.save('behavior-facts.json',FACTS)
    # Shared schema declarations can bind every occurrence without pretending that
    # uninspected runtime methods were semantically reviewed.
    bindings=[];attrs=set()
    for domain in domains:
        fam=domain['family'];key=domain['field'];p=r.SCHEMA_DIR+r.SOURCE_FILE[fam]
        hits=[];attribute=None
        for n,line in enumerate((a.ROOT/p).read_text().splitlines(),1):
            m=re.search(r'"'+re.escape(key)+r'"\s*\]?\s*(?:=>|=)\s*\[:(\w+)',line)
            if not m:m=re.search(r'"'+re.escape(key)+r'"\s*=>\s*\[:(\w+)',line)
            if m:hits.append(L(p,n));attribute=m[1]
        if attribute:attrs.add(attribute)
        factids=['D14'] if fam.startswith('pokemon') else []
        groups={'types':['D01','D02'],'abilities':['D03'],'moves':['D05','D06','D07'],'items':['D09','D10'],'berry_plants':['D11','D12','D13'],'pokemon_metrics':['D20'],'shadow_pokemon':['D21']}
        if fam in groups:factids=groups[fam]
        if fam in {'pokemon','pokemon_forms'}:
            if key in {'BaseStats','EVs'}:factids+=['D15']
            if key in {'Height','Weight'}:factids+=['D16']
            if key in {'Offspring','Evolution','Evolutions'}:factids+=['D17']
            if key=='Moves':factids+=['D18']
            if key=='TutorMoves':factids+=['D19']
        bindings.append({'field_fact_id':'FIELD.'+fam+'.'+key,'family':fam,'field':key,'shape':r.SCHEMAS[fam].get(key),'schema_locations':hits,'source_attribute_for_audit_only':attribute,'data_occurrences':domain['occurrences'],'reviewed_limited_fact_ids':factids,'status':'SCHEMA_BOUND; full per-field runtime consumer and formal closure NOT_COMPLETE'})
    a.save('field-contract-matrix.json',bindings)
    # Broad location-only search, output intentionally omits source expressions.
    candidates=defaultdict(list)
    pat=re.compile(r'\.('+('|'.join(sorted(attrs,key=len,reverse=True)))+r')\b')
    for p in sorted((a.REF/'Data/Scripts').rglob('*.rb')):
        for n,line in enumerate(p.read_text().splitlines(),1):
            for attribute in set(pat.findall(line)):
                candidates[attribute].append({'path':str(p.relative_to(a.ROOT)),'line':n,'status':'lexical_candidate_receiver_domain_NOT_PROVEN; context_unread_unless_in_reading_ledger'})
    a.save('runtime-consumer-candidates.json',dict(candidates))
    fb={(b['family'],b['field']):b for b in bindings}
    fmap={f['fact_id']:f for f in FACTS}
    forward=[]
    for rec in records:
        ids=sorted({fid for f in rec['fields'] for fid in fb[(rec['family'],f['key'])]['reviewed_limited_fact_ids']})
        forward.append({**r.loc(rec),'unit_id':rec['path']+':'+str(rec['start_line'])+':'+rec['identity'],'field_facts':[fb[(rec['family'],f['key'])]['field_fact_id'] for f in rec['fields']],'limited_behavior_facts':ids,'consumer_locations':[x for fid in ids for x in fmap[fid]['necessary_consumers']],'formal_clause_locations':[x for fid in ids for x in fmap[fid]['formal_clauses']],'status':'PARTIAL_FORWARD_JOIN; NOT_FULL_RECORD_SEMANTIC_PASS','precondition':'Data profile and actual source/schema/consumer premises must hold; literal resolution is not semantic compatibility.'})
    a.save('source-to-spec-matrix.json',forward)
    reverse=[]
    for f in FACTS:
        for clause in f['formal_clauses']:
            reverse.append({'formal_clause':clause,'fact_id':f['fact_id'],'source':f['source'],'necessary_consumers':f['necessary_consumers'],'preconditions':f['preconditions'],'status':f['status'],'missing_extent':'Full formal domain clauses and dependent test vectors are not all read; this is a finite reviewed join, not exhaustive reverse coverage.'})
    # Independent table equality, preserving ordered move identities.
    lines=(a.ROOT/WP23).read_text().splitlines();table={};effecttable={};itemtable={}
    for n,line in enumerate(lines,1):
        cells=[x.strip() for x in line.strip().strip('|').split('|')]
        if 71<=n<=201 and len(cells)==3:table[cells[0]]={'gauge':int(cells[1]),'moves':cells[2].split('／'),'line':n}
        if 209<=n<=226 and len(cells)==2:effecttable[cells[0]]={'effect':cells[1],'line':n}
        if 232<=n<=235 and len(cells)==5:itemtable[cells[0]]={'field_use':cells[1],'battle_use':cells[2],'price':int(cells[3]),'line':n}
    comparisons=[]
    for rec in records:
        if rec['profile']!='Shadow Pokémon backup':continue
        fields=r.effective(rec);fam=rec['family'];entry=None
        if fam=='shadow_pokemon':
            t=table.get(rec['identity']);ok=bool(t) and int(fields['GaugeSize']['value'])==t['gauge'] and r.atoms(fields['Moves']['value'])==t['moves'];entry={'table':t,'matches_gauge_and_ordered_moves':ok,'consumer_fact':'D21'}
        elif fam=='moves':
            t=effecttable.get(rec['identity']);ok=bool(t) and fields['FunctionCode']['value']==t['effect'];entry={'table':t,'matches_bound_effect_identity':ok,'all_shadow_type':fields['Type']['value']=='SHADOW','consumer_fact':'D06'}
        elif fam=='items':
            t=itemtable.get(rec['identity']);ok=bool(t) and fields['FieldUse']['value']==t['field_use'] and fields.get('BattleUse',{}).get('value','无')==t['battle_use'] and int(fields['Price']['value'])==t['price'] and 'Flags' not in fields;entry={'table':t,'matches_use_price_and_no_flags':ok,'consumer_fact':'D09'}
        if entry:
            comparisons.append({**r.loc(rec),**entry,'status':'LIMITED_LITERAL_TABLE_COMPARISON_NOT_FULL_GAMEPLAY_APPROVAL'})
            reverse.append({'formal_clause':L(WP23,entry['table']['line']),'data_unit':r.loc(rec),'necessary_consumer_fact':entry['consumer_fact'],'status':'LIMITED_LITERAL_EQUALITY','preconditions':'Optional overlay validly loaded; no claim that effect handlers or item uses succeed.'})
    a.save('shadow-formal-table-comparison.json',comparisons)
    a.save('spec-to-source-matrix.json',reverse)
    # Track every pending record directly. A model-visible read only proves data
    # bytes/context were inspected; it cannot close unrelated consumers.
    semantic=[]
    for rec in records:
        semantic.append({**r.loc(rec),'status':'PENDING_FULL_SEMANTIC_REVIEW','completed':['full byte/record/field inventory','authored scalar-shape check','conditional registry identity relation check','field-schema binding','profile delta or overlay identity binding'],'pending':['all actual runtime consumers and dependent configuration premises','exact full formal contract plus all relevant test vectors','negative/control and cancellation/exception prefixes for each effective rule'],'full_semantic_pass':False})
    a.save('semantic-pending-records.json',semantic)
    # Exact duplicate evidence remains path-specific; it is never a prior PASS.
    a.save('deduplication-proof.json',{'method':'independently read complete file bytes and compare Git blob plus SHA256 at fixed tree','files':[{'path':f['path'],'sha256':f['sha256'],'git_blob':f['git_blob'],'equal_to':f['same_blob_as']} for f in files if f['same_blob_as']],'reusable_extent':'Data byte identity only. No old review result reused and no current unreviewed semantics closed.'})
    print(json.dumps({'field_bindings':len(bindings),'unlocated_schema_fields':[x['field_fact_id'] for x in bindings if not x['schema_locations']],'behavior_facts':len(FACTS),'forward_record_joins':len(forward),'reverse_limited_joins':len(reverse),'shadow_table_rows':len(comparisons),'shadow_table_mismatches':[x for x in comparisons if any(v is False for k,v in x.items() if k.startswith('matches'))],'semantic_pending_records':len(semantic)},ensure_ascii=False,indent=2))

if __name__=='__main__':
    a.append('command-log.jsonl',{'time':a.now(),'script':'build_mappings.py','script_sha256':a.sha(Path(__file__).read_bytes()),'purpose':'limited facts, source/consumer/formal joins, explicit pending semantic coverage'})
    run()
