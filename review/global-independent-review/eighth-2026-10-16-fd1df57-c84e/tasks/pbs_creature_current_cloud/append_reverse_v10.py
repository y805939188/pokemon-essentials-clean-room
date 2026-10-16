from pathlib import Path
import json,datetime,hashlib,subprocess
P=Path(__file__).resolve().parent;R=Path('/workspace/pokemon-essentials');C='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';UTC=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
F='deliverables/final-specification-set/'
WP18=F+'creature-rpg/wp18-creature-identity-species-ownership.md'
WP19=F+'pokemon-rules/wp19-attributes-ability-and-stats.md'
WP29=F+'creature-rpg/wp29-shops-and-exchanges.md'
CI=F+'test-catalog/creature-rpg-wp18-20-24-25-26.md'
PK='Data/Scripts/014_Pokemon/001_Pokemon.rb'
SP='Data/Scripts/010_Data/002_PBS data/008_Species.rb'
OW='Data/Scripts/014_Pokemon/005_Pokemon_Owner.rb'
TR='Data/Scripts/010_Data/002_PBS data/015_Trainer.rb'
GR='Data/Scripts/010_Data/001_Hardcoded data/001_GrowthRate.rb'
VA='Data/Scripts/001_Technical/001_Debugging/004_Validation.rb'
sets={
 'species':[(PK,123,138),(SP,243,265)],
 'form':[(PK,147,184)],
 'create':[(PK,1159,1226),(PK,1099,1127),(OW,19,42)],
 'moves':[(PK,625,660)],
 'npc':[(TR,115,178),(PK,123,184),(PK,341,418),(PK,428,490)],
 'clone':[(PK,1135,1151)],
 'owner':[(OW,19,71),(PK,840,849),(VA,12,30)],
 'name':[(PK,878,905)],
 'time':[(PK,852,871)],
 'shiny':[(PK,390,418)],
 'level':[(PK,191,237),(GR,23,71)],
 'calc':[(PK,1066,1127),(PK,246,250),(PK,497,545)],
 'dex':[(PK,159,179),('Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb',157,196)],
 'shop':[],
}
def unit(path,a,z):
 b=(R/path).read_bytes();assert b==subprocess.check_output(['git','show',C+':'+path],cwd=R)
 assert 1<=a<=z<=len(b.splitlines())
 return {'repo':str(R),'commit':C,'tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','path':path,'lines':[a,z],'full_source_bytes':len(b),'full_source_sha256':hashlib.sha256(b).hexdigest(),'git_blob':subprocess.check_output(['git','rev-parse',C+':'+path],cwd=R,text=True).strip(),'reading':'Own full source already recorded, or exact contained method re-read in the named actual I/O; this mechanical identity check creates no reading credit.'}
units={k:[unit(*s) for s in v] for k,v in sets.items()}
# Every row below is a manually assessed finite assertion. Loops only serialize it.
rows=[]
def add(id,doc,line,assertion,key,facts=()):rows.append((id,doc,line,assertion,key,list(facts)))
for id,line,assertion in [
 ('LOOKUP-FIRST',139,'Target lookup is strict and occurs before the same-base equality return.'),
 ('SAME-BASE',139,'Same base species returns without changing form, even if the requested registered target is another form.'),
 ('DEFAULT-FIRST',140,'On a different base, a nonnegative DefaultForm_N result takes priority over the target record form.'),
 ('POSITIVE-FORM',140,'Without a default flag, positive target form is stored; a zero/nonpositive target form leaves the old stored form.'),
 ('FORCED-CLEAR',141,'Different-base assignment clears forced_form before later recomputation.'),
 ('GENDER-GUARD',141,'Gender cache is cleared only when the newly selected effective species data is single-gendered.'),
 ('LEVEL-CLEAR',141,'Level cache is cleared so later reads use the new growth curve with unchanged experience.'),
 ('ABILITY-CLEAR',141,'Resolved ability cache is cleared while ability_index storage is retained.'),
 ('INPUTS-RETAINED',142,'Experience, moves, owner, nickname and happiness are not assigned by species=; later callbacks are separately qualified.'),
]:add('PCR-ID-SPECIES-'+id,WP18,line,assertion,'species',['PC-F023'])
for id,line,assertion in [
 ('COMMIT',148,'form= stores the requested form and clears ability, then onSetForm, stats, and optional player Pokedex registration in this order.'),
 ('YIELD',149,'setForm stores form and clears ability before its optional yield; callback/stats/registration follow only if that yield returns.'),
 ('SIMPLE',150,'form_simple= stores and recalculates without onSetForm, ability clearing or Pokedex registration in that setter.'),
 ('FORCED',154,'Ordinary form reads return nonnil forced_form before accessing battle/storage guards.'),
 ('GUARDS',154,'Without a forced value, battle or storage context returns the stored form and skips dynamic getForm.'),
 ('CHANGE',154,'Otherwise a truthy dynamic result is committed only if unequal to the stored form.'),
 ('SIMPLE-READ',155,'form_simple reads forced_form || stored form and does not call a dynamic handler; species_data uses this result.'),
 ('EQUAL-COMMIT',349,'Explicit form= and creation recheck commits have no equality short circuit; ordinary dynamic reads do.'),
]:add('PCR-ID-FORM-'+id,WP18,line,assertion,'form',['PC-F024'])
for id,line,assertion in [
 ('ENTRY',166,'Creation defaults to current player owner, withMoves=true and recheck_form=true; successful completion requires all actually invoked dependencies.'),
 ('BASE',171,'Creation resolves strict Species data, stores its base species and base_form, and initializes forced_form/time_form_set to nil.'),
 ('LEVEL',172,'The level setter runs before later initialization and stores the selected curve minimum experience plus level cache.'),
 ('NON-EGG',173,'steps_to_hatch is initialized to zero before heal_status, so ordinary creation is not an egg.'),
 ('STATUS',174,'Reached heal_status writes NONE and count0 while the object is not an egg.'),
 ('EMPTY-CACHES',175,'Gender, ordinary shiny, ability index, resolved ability and calculation nature are assigned nil during initialization; later reads may fill selected caches.'),
 ('NATURE-FINAL',176,'The unconditional final stats calculation reads nature_for_stats and therefore fills displayed nature when no calculation override exists.'),
 ('ITEM-MAIL',177,'Item and mail storage are nil in ordinary construction before caller-specific changes.'),
 ('MOVES',178,'Default moves are initialized only when withMoves is truthy; first_moves starts empty independently.'),
 ('CONTAINERS',179,'Ribbons and markings each start as empty arrays; contest fields and Pokerus start0. Empty markings does not mean six explicit zero entries.'),
 ('NAME',180,'Nickname storage starts nil, causing ordinary name reads to use current species display name.'),
 ('HAPPINESS',181,'Constructor copies record happiness directly without an extra 255 clamp; valid authored256 remains256 on successful return without later writer.'),
 ('BALL',182,'Ordinary construction stores POKEBALL, independently from later capture/egg/caller assignment.'),
 ('IV-EV',183,'Each registered main stat gets an independent rand(32) stored IV and EV0; ivMaxed remains an empty hash.'),
 ('OWNER',184,'Existing Owner is retained by reference; Player/NPCTrainer converts current fields; other owner values create an empty Owner(0,"",2,2).'),
 ('SOURCE',185,'Creation writes obtain0 or4 from current fateful switch, current map or0, nil obtain_text, passed level, hatched_map0 and current integer-second time; later switch changes do not rewrite these fields.'),
 ('HP',186,'HP and totalHP start1 before stats; with valid positive data this final adjustment produces the freshly computed full HP.'),
 ('RECHECK-GUARD',188,'Creation recheck is entered only when stored initial form is0 and recheck_form is truthy.'),
 ('RECHECK-ZERO',188,'Truthy getFormOnCreation result includes numeric0, so zero is still explicitly committed with the full form= chain.'),
 ('RECHECK-MOVES',188,'Only withMoves=true causes another reset_moves after a returned creation-form commit; withMoves=false does not reset there.'),
]:add('PCR-ID-CREATE-'+id,WP18,line,assertion,'create',['PC-F025'])
for id,line,assertion in [
 ('START',211,'Normal GameData trainer conversion creates an owned member with automatic moves disabled and appends it to trainer.party before later field writes.'),
 ('FORM',211,'A supplied form including0 triggers form_simple=, preserving that setter’s limited side effects.'),
 ('MOVES',211,'A supplied nonempty move list is learned in its order; absent or empty list instead resets level-eligible moves after any form write.'),
 ('ABILITY',215,'Missing ability_index writes0, then explicit ability field is assigned; missing ability clears resolved cache rather than restoring PID-selected index.'),
 ('GENDER',216,'Missing gender attempts male only for male trainer type, otherwise female; fixed-gender species can reject this attempt through their guard.'),
 ('SHINY',217,'Ordinary shiny then super-shiny booleans are assigned in that order; later Shadow construction writes ordinary shiny false without clearing the super-shiny marker.'),
 ('NATURE',218,'Missing nature uses the zero-based complete Species-key position plus TrainerType-key position modulo Nature count, then registry key at that index; it is not a National-Dex number.'),
 ('IV-EV',219,'Missing IV writes min(level/2,31); missing EV writes min(level*3/2,510/6) per stat using integer arithmetic; explicit per-stat maps take precedence.'),
 ('TAIL',221,'Optional happiness/nickname/Shadow/ball follow those assignments, then stats; partial earlier member/field writes have no general rollback on later failure.'),
]:add('PCR-ID-NPC-'+id,WP18,line,assertion,'npc',['PC-F018','PC-F031'])
for id,line,assertion in [
 ('REBUILT',231,'clone rebuilds IV/ivMaxed/EV hashes, move array and each move object, first_moves array, owner object and ribbons array.'),
 ('SHARED',232,'Unreplaced markings/fused/mail references remain from shallow super clone; no blanket recursive deep copy is performed.'),
 ('IDENTITY',233,'PID and cached values are copied; cloning does not resample PID/IV or clear already cached gender/shiny/ability/nature.'),
 ('NO-NOTICE',239,'The clone method contains no Pokedex registration or form-handler call.'),
]:add('PCR-ID-CLONE-'+id,WP18,line,assertion,'clone')
for id,line,assertion in [
 ('TRAINER',250,'new_from_trainer uses the trainer current id/name/gender/language values, not a fresh host-language lookup.'),
 ('FOREIGN-DEFAULT',251,'new_foreign language default is2; current player supplies a different ID; this helper’s gender default is2, distinct from gift wrappers.'),
 ('COLLISION',254,'For ordinary equal integer/text values the validation hash retains the last condition for a duplicate key; Owner(0,0,0,2) and(1,0,0,2) can bypass the name String condition before all four assignments.'),
 ('NONCOLLISION',254,'Owner(1,0,1,2) retains a String condition for key0 and fails before any of its four field assignments.'),
 ('SINGLE-NAME',255,'Single name=0 independently validates String and fails before replacing an existing valid name.'),
 ('PUBLIC',257,'public_id is id & 0xFFFF; 0x12345678 gives0x5678=22136 by ordinary integer arithmetic.'),
 ('SETTER',262,'Pokemon owner= validates only that the new object is an Owner and assigns it; it does not clear shiny caches or recursively revalidate fields.'),
 ('FOREIGN',288,'foreign? compares only owner id and name with the supplied/default trainer using OR of differences; gender and language do not participate.'),
]:add('PCR-ID-OWNER-'+id,WP18,line,assertion,'owner')
for id,line,assertion in [
 ('FALLBACK',294,'Name returns nickname when nonempty, otherwise current effective species display name.'),
 ('CLEAR',295,'Assigning nil, empty string or current species name clears nickname; this setter does not truncate a longer string.'),
 ('SIZE',297,'height and weight directly read the effective species_data values, in tenths; this is separate from the millimeter helper.'),
]:add('PCR-ID-DISPLAY-'+id,WP18,line,assertion,'name')
add('PCR-ID-TIME-INTEGER',WP18,281,'timeReceived/timeEggHatched setters store value.to_i; reads wrap Time.at, and hatch time reads nil unless obtain_method==1. A method1 nil timestamp is not silently repaired.','time')
for id,line,assertion in [
 ('XOR',53,'Ordinary shiny starts with PID XOR complete owner.id, then XORs the two masked16-bit halves.'),
 ('THRESHOLD',56,'Ordinary shiny caches d < configured threshold; equality with threshold is false. Default/era threshold is separately read from Settings.'),
 ('SUPER',57,'Super shiny independently recomputes and caches d==0; ordinary shiny reading does not initialize the super cache.'),
 ('SUPER-TRUE',58,'Setting truthy super_shiny sets ordinary shiny true; setting false does not clear ordinary shiny.'),
 ('SEPARATE',59,'Changing PID or owner does not clear either cached result here; explicit clearing of one cache does not clear the other.'),
]:add('PCR-ST-SHINY-'+id,WP19,line,assertion,'shiny')
for id,line,assertion in [
 ('CACHE',119,'Level computes and caches curve.level_from_exp only when level cache is absent.'),
 ('SET-VALIDATE',121,'Level setter checks <1 or >max before writing exp/level; rejected ordinary out-of-range numbers leave those fields unchanged.'),
 ('SET-WRITES',121,'A reached valid level set writes curve minimum experience then the requested level cache; no stats recalculation occurs in that setter.'),
 ('EXP',122,'Experience setter stores the supplied value without a clamp and clears level cache; it does not call stats.'),
 ('FRACTION',123,'Experience fraction is0.0 at maximum level; otherwise it divides float earned-in-current-level by that level interval.'),
 ('BAD-LEVEL',124,'minimum_exp_for_level(nil or<=0) returns an ArgumentError object rather than raising it immediately.'),
 ('BAD-EXP',124,'level_from_exp(nil ornegative) attempts a diagnostic interpolation of undefined level and fails during name resolution; it does not return the intended error object.'),
]:add('PCR-ST-LEVEL-'+id,WP19,line,assertion,'level')
for id,line,assertion in [
 ('BASE-COPY',132,'baseStats builds a new main-stat hash from current effective species_data base_stats; it does not normalize absent values there.'),
 ('IV-HYPER',144,'calcIV returns31 for each truthy ivMaxed marker, otherwise the raw stored IV; it does not overwrite the raw IV hash.'),
 ('IV-DISABLE',144,'DISABLE_IVS_AND_EVS replaces local arithmetic IV and EV with0 in calcHP/calcStat, retaining the stored values.'),
 ('EV-QUARTERS',166,'For ordinary integer input each formula consumes integer EV/4; sub-four residues do not produce a stat contribution.'),
 ('HP-ONE',183,'Base HP exactly1 returns1 before the disable-IV/EV arithmetic branch.'),
 ('HP-FORMULA',184,'Other HP uses floor(((2B+IV+floor(EV/4))*L)/100)+L+10 for valid integer inputs.'),
 ('OTHER-INNER',190,'Other stats first divide the multiplied base/IV/EV sum by100 and floor, then add5.'),
 ('OTHER-NATURE',191,'That inner result is multiplied by the per-stat Nature multiplier and divided/floored by100; rounding order is not interchangeable.'),
 ('NATURE-SUM',194,'Each main-stat Nature multiplier starts100, then each registered change is added; the ordinary25 mapped records supply0 or±10 changes.'),
 ('WRITE-ORDER',207,'calc_stats computes all stats first, derives HP difference, stores new totalHP, conditionally calls HP setter, then assigns five other stat caches.'),
 ('LIVE-HP',209,'For a previously live object reached HP adjustment uses max(oldHP+delta,1) then the HP setter clamp.'),
 ('FAINTED-HP',210,'For oldHP0 adjustment occurs only when delta>0, reviving to positive delta under valid values; otherwise HP0 remains untouched.'),
 ('CLAMP',211,'The invoked HP setter clamps to[0,newTotalHP]; reached zero additionally heals status and clears ready_to_evolve.'),
 ('CACHE-FILL',213,'Stats reads current level and calculation nature, potentially filling their caches; it does not overwrite raw exp/IV/EV/owner/moves/happiness inputs.'),
 ('MISSING',248,'Missing required IV/EV/base stat values are not repaired by these read/calculation methods and can fail arithmetic after earlier cache reads.'),
]:add('PCR-ST-CALC-'+id,WP19,line,assertion,'calc',['PC-F028'])
for id,line,assertion in [
 ('PRICE-DEFAULT',112,'Item default SellPrice uses integer half of supplied/default Price and BPPrice defaults1; no extra runtime shop cap is applied to these record values.'),
 ('BUY-OVERRIDE',120,'Normal shop buy uses a positive temporary buy slot, otherwise Item Price.'),
 ('SELL-OVERRIDE',120,'Normal shop sell uses a nonnegative temporary sell slot; zero is effective and makes the item unsellable.'),
 ('BP-OVERRIDE',122,'BP shop shares the positive buy slot, otherwise Item BPPrice; the same overlay slot can affect both currency shops.'),
 ('SELL-GUARD',114,'Nonimportant and effective sell price>0 are required before the ordinary sell quantity flow.'),
 ('ALIAS',49,'Ordinary entry filters already-owned important entries from the supplied array itself. The complete entry has no element-normalization assignment.'),
 ('BP-EXIT',88,'After normal BP screen return, the wrapper requests both farewell messages before clearing prices; failure during either request can prevent clear.'),
 ('BP-HALF',101,'BP quantity window uses quantity*floor(unitPrice/2), while confirmation and spend continue using full price.'),
 ('BP-ODD',174,'With integer unitPrice21 and quantity3 the displayed subtotal is30, not31; confirmation and actual cost are63.'),
 ('BP-ONE',174,'With BP unitPrice1, any displayed quantity subtotal is0, while actual full unit cost remains1.'),
 ('BUY-COMMIT',61,'Complete item additions precede purchase statistics, wallet setter, important-stock filtering, purchase feedback and any bonus.'),
 ('BUY-PARTIAL',62,'A failed all-items add loop removes only its successful prefix, one by one; removal failure raises and there is no universal transaction rollback.'),
 ('SELL-COMMIT',79,'Sale wallet setter precedes actual-increase statistics and unchecked per-item removals; later removal failure is not repaired by a sale rollback.'),
 ('BP-COMMIT',103,'BP successful additions precede BP-spent and shared-item statistics, then BP setter and filtering/feedback.'),
 ('BP-PARTIAL',104,'BP incomplete additions use the same explicit successful-prefix removal loop and no BP/spend-stat change in that branch.'),
]:add('PCR-SHADOW-SHOP-'+id,WP29,line,assertion,'shop')

old=json.loads((P/'reverse-mapping.json').read_text());assert len(old['clauses'])==1634
prior=P/'reverse-mapping.v9.frozen.json';assert not prior.exists();prior.write_bytes((P/'reverse-mapping.json').read_bytes())
existing={x['id'] for x in old['clauses']};atoms=[]
for id,doc,line,assertion,key,facts in rows:
 assert id not in existing;existing.add(id)
 atoms.append({'id':id,'formal':{'path':doc,'lines':[line,line]},'assertion':assertion,'sourcefact_ids':facts,'source_units':units[key],'actual_reader':'/root/pbs_creature_current_cloud','status':'FINITE_ASSERTION_MATCHED_SOURCE_STATIC','premises':['Fixed R/B8, valid specified ordinary inputs and normal prior invoked calls; no plugin override or unstated callback mutation.','Only the complete named assertion is accepted. The surrounding paragraph and all additional children/host effects remain separately OPEN.'],'qualification':'Actual source/formal reading and manual semantic join; no executed testcase. Identity validation only binds already read content.'})
 if key=='shop':
  atoms[-1]['received_complete_fact_basis']={'path':'shadow-item-shop-price-reception.v1.json','original_reader':'/root/creature_b','mandatory_companion':'mandatory-shop-reception-correction.v2.json','scope':'All10objects actually received, with two false fragments expressly rejected. Corrected BP/stock propositions are own complete contained-unit readings, not inherited provider FULL.'}
  atoms[-1]['own_definitions']='Own Item270,Player123,Bag301 as recorded; source price fields below require explicit installation of the optional Shadow records and applicable stock/override premises.'
old['clauses']+=atoms;old['schema']='gr8-pbs-current-reverse/v10';old['utc']=UTC;old['supersedes']='reverse-mapping.v9.frozen.json retained';old['atom_denominator_frozen_so_far']=len(old['clauses']);old['identity_stats_shop_addendum']={'atoms':len(atoms),'previous':1634,'new':len(old['clauses']),'actual_read_io':['0431da','d00d52','e12321','1407af','da0c21','e95e36','7668c8','0ca1f1','e24047','0de579','9d6dea','9c71cc','e0bc20'],'qualification':'WP18/19/29 necessary individual clauses only. Prior raw/default tables are not reread-credit inflated. No all WP18/19/29, all CI or all callbacks acceptance.'};old['whole_scope_status']='OPEN';(P/'reverse-mapping.json').write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
packet={'schema':'gr8-pbs-current-identity-stats-shop-finite-reverse/v1','utc':UTC,'actual_reader':'/root/pbs_creature_current_cloud','complete_atoms':atoms,'common_premises':'Every listed assertion retains its own premise and exact source/receipt identity. Complete own source readings predate this manual binding; scripts do not establish reading.','remaining':'EggGroup15 directory adjudication OPEN; WP18 individual millimeter helper, all gift wrapper/normal UI/unknown plugin surfaces and WP19 transitive battle/facility callbacks beyond received finite facts remain OPEN. No complete-domain PASS.','business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'}
out=P/'identity-stats-shop-reverse-addendum.v1.json';assert not out.exists();out.write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n')
ledger=json.loads((P/'reading-ledger.json').read_text());ledger['formal_partial_read'] += [{'path':CI,'lines':[1,47],'actual_read_chunk':'e0bc20','complete_units':['all CI01–31 original fullobjects with shared premises; only individually source-bound predicates accepted, no wholecatalog credit']},{'path':CI,'lines':[320,329],'actual_read_chunk':'e0bc20','complete_units':['whole R6-U14-CI commonpremises and4completevectors; manual actor sourcebinding separately bounded']}];ledger['updated_utc']=UTC;(P/'reading-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'utc':UTC,'path':str(out),'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'new_atoms':len(atoms),'reverse_atoms':len(old['clauses'])},ensure_ascii=False))
