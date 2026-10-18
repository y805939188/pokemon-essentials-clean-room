import pathlib,json,datetime,hashlib,subprocess
P=pathlib.Path(__file__).resolve().parent
R=pathlib.Path('/workspace/pokemon-essentials')
C='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
old=json.loads((P/'sourcefact-consumer-receptions.json').read_text())
by={x['id']:x for x in old['facts']}
d=json.loads((P/'manual_batch_11n.json').read_text())['source_dictionary']
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
records=[]
def consumer(name,keys,meaning,remaining):
    return dict(consumer=name,actual_definitions=keys,complete_finite_join=meaning,remaining=remaining)
def rec(n,children,cs,remaining):
    ident=f'CORE-F{n:03d}'; orig=by[ident]['original_complete_record']
    assert [x['consumer'] for x in cs]==orig['consumers']
    records.append(dict(id='CAR-SFB-'+ident,original_complete_record=orig,
        original_fact_reader='/root/combat_review',independent_actual_receiver='/root/core_atomic_reception',
        original_record_reception='All fields of these ten complete original objects actually read earlier and separately reread in current output 704541; sourceFULL is not inherited from original author.',
        complete_meaning_children=children,consumer_bindings=cs,
        premise='Fixed R, registered valid objects and supported layout unless the explicit countercase says otherwise; no concurrent/plugin mutation. Static derivation only.',
        failure='Each early return, cancel and exception preserves exactly the reached writes. No rollback or target execution follows from helper exit0, source identity or ordinary diagnostic return.',
        persistence='Battle runtime counters/copies and referenced persistent Pokemon/Player/Bag are distinguished. Actual finite save/load contribution establishes only its stated writer/reader contract, not a game save/reload run.',
        remaining=remaining,all_named_finite_interfaces_received=True,all_recursive_domain_callbacks_received=False,
        business='NOT_EXECUTED',update='UPDATE_NOT_STARTED'))
rec(11,[
 'nextPickupUse increments the battle-owned counter before returning its new integer; Battle initializer begins it at0, so reached calls return1,2,... without reuse or reset by consumption.',
 'pbConsumeItem logs before mutation; recoverable=true writes Recycle item ID and PickupItem before requesting/storing the new sequence. recoverable=false bypasses these three writes.',
 'Belch query/write follows the recoverable prefix, then permanent removal and optional Symbiosis. Nil/invalid held-item failure can therefore leave the recoverable prefix committed; no blanket transactional consumption.',
 'Pickup end-round handler refuses an already-held item, searches other living battlers for strictly greatest PickupUse, and only afterward rejects nil foundItem. It does not first filter sources to nonnil PickupItem.',
 'On the selected valid source it shows ability, assigns holder item, clears source PickupItem/Use and matching Recycle, conditionally transfers initialItem only in wild battle with holder initialnil/source initialmatching, then message/hide/held-item-trigger.'
],[consumer('Battler item consumption',['battlefull','consume_complete'],'Same battle counter reference is called only in the recoverable branch after PickupItem assignment; reached later removal/initialItem and Symbiosis effects stay distinct. Exact consumption/common gates already hand-bound in item lifecycle and ERR09 vectors.','Every independent item handler/berry attempt and Symbiosis family remains separately bound; no all-item callback closure.'),
consumer('Pickup ability',['pickup_complete','ability_item','eor'],'pbEOREndRound invokes living active end-round ability handlers in its actual priority stage; Pickup uses the monotonic maximum selection and actual item receiver above. A latest sequence with nil item can block an earlier usable item in this invocation.','Specific retry/native display/Pickup item IDs and every other end-round ability are not inferred from this finite handler.')],
['WP49/50 full family recursion is separate from complete Pickup/consumption interface reception; old WAIT_ABILITY_ITEM is retained inside immutable original record only.'])
rec(12,[
 'defaultWeather= directly stores default/current and duration-1. pbWeather returnsNone for any living active CloudNine/AirLock without changing stored weather or duration.',
 'pbStartWeather returns for same raw current value, otherwise raw value changes before extender callback; fixed duration5 or permanent-1, only positive duration with active held item asks WeatherExtender; matching four rocks return8.',
 'Duration write precedes animation, hide, weather-specific message, all living weather-form callbacks and primordial-source check. Exceptions retain the precise earlier raw/duration/message prefix.',
 'Primordial-source check returns immediately when current==default; otherwise only HarshSun/HeavyRain/StrongWinds without corresponding active global source becomeNone. Only an actual change then checks forms and restarts a nonNone default.',
 'Ability wrapper refuses ordinary overwrite of stored primordial weather unless ignore_primal, and refuses same stored value before splash. FIXED_DURATION_WEATHER_FROM_ABILITY applies only non-primal requested weather; explicit primal handlers passignoretrue.',
 'End-round positive duration decrements first; reaching0 ends raw weather, notifies/forms and may restart default. Effective suppression and holder UtilityUmbrella are separate layers; local Umbrella masks Sun/Rain pairs only.'
],[consumer('prepare_battle',['prepare','weather_core_complete','worldweather_full'],'Explicit battle weather rule assigns default directly; otherwise map weather is converted through its battle_weather metadata under actual prepare gates. This does not dispatch ability weather or extender and duration is permanent.','Every map/host weather resource execution and plugin rule producer stays separate; selected full WorldWeather metadata definition is source only.'),
consumer('weather moves/abilities',['weather_move_parent','weather_terrain_moves','weather_abilities_complete','weather_extenders_complete','ability_item'],'Weather move parent checks stored primal/same-weather before ordinary effect, then requests fixed duration; ordinary Drizzle/Drought/SandStream/SnowWarning use guarded ability wrapper, three primal handlers pass ignoretrue. Active OnSwitchIn caller, global source query and four matching rocks supply the actual gates.','All downstream damage/accuracy/form handlers and raw move/ability records require their own family bindings; selected producers do not grant all weather effects.'),
consumer('EOR weather',['eor','weather_core_complete','eor_weather_handlers'],'Actual EOR weather stage decrements stored timed duration before effective-weather effects, distinguishes current/default from suppression, and invokes its named living ability/item callbacks. Complete W/T manual controls preserve rawRain versus effectiveNone and Umbrella.','Every independent weather damage/heal/forecast form handler retains its bounded record or OPEN; native messages/animation and target persistence unexecuted.'),
consumer('Battler effectiveWeather',['battlerfull','ability_item','weather_core_complete'],'Battler first asks battle.pbWeather, then active UtilityUmbrella maps only Sun/HarshSun/Rain/HeavyRain toNone for that holder. CloudNine/AirLock suppress for all living holders without raw write.','This query receives all ordinary layers but not all callers of each effectiveWeather result.')],
['Shared raw/default/effective/member weather interfaces are received; recursive weather function families remain explicit separate obligations.'])
rec(13,[
 'defaultTerrain= stores default/current and duration-1 directly. Same-current pbStartTerrain returns without refreshing duration or callbacks.',
 'A changed raw terrain precedes extender; duration5 or-1, active positive-duration TerrainExtender makes8, then duration/animation/hide/message happen.',
 'Complete living ability pass precedes complete living item pass. Active MIMICRY onTerrainChange maps four valid terrain types or resets onNone; seed handlers require actual matching raw terrain plus CanRaise and successful Raise before item-trigger/consumption.',
 'Four Surge OnSwitchIn registrations first reject same raw terrain, show splash then request terrain; default change does not directly run this producer loop.',
 'EOR only positive terrainDuration decrements; at0 it ends terrain and performs source-defined callbacks, and restarts only nonNone default with fixedDurationfalse. DirectNone can retain an old duration; no forced default restoration from a nonexistent expiry event.'
],[consumer('prepare_battle',['prepare','weather_core_complete'],'Explicit rule assigns defaultTerrain directly; environment/terrain configuration is read under prepare source gates. Constructor defaultNone and start messages do not imply a 5-turn activation.','Dynamic rule and map environment resource producers remain separate; no implicit Surge/seed call for plain setter.'),
consumer('terrain moves/abilities',['weather_terrain_moves','terrain_abilities_complete','terrain_items_complete','terrain_mimicry_complete','terrain_receivers_complete','stages'],'Four move classes request the same core with fixed duration, four Surge producers use active OnSwitchIn, TerrainExtender and four seeds are exact matching handlers, and MIMICRY has active caller/registered type gates. Raise/animation/message can fail before consumption; all ability pass completes before item pass begins.','Other terrain users including damage/priority/status/immunity families retain independently bound or OPEN callbacks; this is not all-terrain PASS.'),
consumer('pbEOREndTerrain',['eor','weather_core_complete','terrain_receivers_complete'],'Complete timer and restore caller uses same raw fields. Existing T01 heal-cap companion and T02–T04 directNone/default controls remain authoritative; terrain change callbacks and healing tick are separate stages.','Every terrain healing/filter/source-specific downstream effect needs its own finite binding; shared expiry interface received.')],
['Complete default/current/duration and named producer/receiver interfaces received; whole field/effect recursion remains open.'])
rec(14,[
 'Display forwards block/brief/paused/confirm/command arguments to corresponding Scene methods; confirm/commands return Scene return value, and cancel behavior belongs to receiver defaultValue.',
 'showAnims gates only these Battle move/common animation wrappers. Text, HP/EXP, ability UI or direct Scene calls have their own gates rather than a universal showAnims suppression.',
 'Ability show logs name before USE_ABILITY_SPLASH early return; enabled receiver show happens before optional one-second System.uptime loop continuously callingScene.pbUpdate.',
 'Hide/replace separately check USE_ABILITY_SPLASH; Scene receiver same-side visible replacement, animation/missing-asset search, message/Input waits and exceptions keep their own exact contract.'
],[consumer('all battle callers',['battlefull','ui_display_finite','ui_animation_finite'],'For each actual invocation the wrapper contract above is complete, and named battle callbacks in manual atoms bind reached display/animation stages. This label is a generic per-invocation interface; it is not evidence that every callback caller/effect family was recursively enumerated.','All individual unbound caller families remain OPEN. Generic forwarding cannot close an arbitrary effect or prove asset/native execution.'),
consumer('Battle::Scene receivers',['ui_display_finite','ui_animation_finite'],'Actually received complete UI67-U003/U004/U012/U014/U016 original records and common premises; U014 and U016 independently untruncated reread after combined-output truncation. Scene lookup may find no animation, defaults/hit offsets and normal-only coordinate restoration are preserved. SourceFULL remains UI original reader.','Native Input/Graphics/Audio completion, assets existence and every independent Scene path remain unexecuted/open.')],
['Generic all-callers wording is accepted only as the precise per-invocation forwarding interface, never universal recursive closure.'])
rec(15,[
 'BattleAbortedException is dedicated Exception path; public pbStartBattle logs then ensures participants and starting forms before entering the core begin/rescue boundary.',
 'More than two trainers on either side is rejected before later participant counting. Wild able count drives side adjustment, and sparse owner counts/missing entries keep distinct invalid-owner/nil comparison failures.',
 'Zero-able wild nil.times failure and dead-first wild extra-slot mismatch retain root COM002/003 exact scope; correct reverse order/normal positive cases and existing NPC skip coverage113 stay intact.'
],[consumer('pbStartBattle',['ensure','startendfull','b_init','teams'],'Actual public call reaches validation before per-Pokemon starting hooks, and neither is protected by the later dedicated core-abort rescue. Validation failure therefore is not clean decision0 return from that rescue.','All individual starting form and target host exception paths retain their specific units; no broad rescue guarantee.')],
['All validation/common public boundary interfaces received; malformed data behavior only as exact rooted COM002/003, not reopening correct normal ranges.'])
rec(16,[
 'pbCreateBattler creates Battler, same-index Position/choice/successState and initializes shared Pokemon binding; setup wild iterates every party2 entry rather than slicing declared size.',
 'Trainer required counts are per owner but destination display rank uses whole-side battlerNumber, permitting later-owner rank hole; no normalization or implicit repaired mapping.',
 'Start messages/sendouts choose opponent side before player, use actual existing battler arrays and per-owner last/rank/name queries. Wild extra-member Peer callbacks and initial sendout hooks are distinct.'
],[consumer('pbStartBattleCore',['startendfull','b_init','activefield_full'],'Core calls setup sides first, then AI objects, Scene startup and sendout. Thus actual extant battlers/positions shape is observable by AI/Scene; later priority may traverse only declared field slots.','All downstream individual AI handler/Scene asset paths remain separately bounded; shape presence does not imply no holes.'),
consumer('pbLastInTeam',['teams','startendfull'],'Reads post-setup display ranks and actual owner segment; later-owner malformed rank can cause comparison failure at its real consumer, while valid reverse/no-partner controls retain correct behavior. Original F016 legacy originlabel GR8-COM-002:MIXED_ORDER is historical metadata; canonical root COM003 is not merged or double-counted.','No all-Illusion effect family or record inference from this query.'),
consumer('Scene startup',['startendfull','ui_startup_finite'],'Actual Scene intro and sendout receive constructed battler indices/owner arrays, then begin entry ability/item events. Received UI67-U001/U002/U013 complete finite startup objects retain source reader UI and native limits.','No full Scene source credit or proof every animation resource exists/host accepts malformed slots.')],
['Constructor/setup/actual named startup receiver interfaces received, while arbitrary AI/UI and species-form callbacks stay separate.'])
rec(17,[
 'Public validation and full party starting-form hooks precede protected core call; dedicated core abort is caught and maps decision0, while ordinary StandardError stage diagnostics return to their enclosing loop only if diagnostic returns normally.',
 'Core setup order is sides→AI→Scene→initial sends→initial weather/terrain messages→priority/entry callbacks→battle loop. Loop command, attack, endround each have actual decision checks and logonerr wrappers.',
 'Debug >=100 rounds stores pbDecisionOnTime result and then aborts; outer dedicated rescue overwrites it0. Ordinary stage failure after prefix is neither automatic abort0 nor rollback/restart of every phase.'
],[consumer('world core callers',['wild','trainer','prepare','startendfull','after'],'Wild/Trainer core wrappers supply actual battle defaults/prepare state, invoke start under actual animation/standby callbacks, and perform reached after_battle only after return. Public pre-core failure and standard error propagation retain their distinct boundaries.','All world EventHandlers/map/partner dynamic callbacks are independently scoped; no game execution/wholeWORLD acceptance.'),
consumer('PBDebug.logonerr',['pbdebug','startendfull'],'Rescues StandardError only, calls pbPrintException and returnsnil when diagnostics return normally. BattleAbortedException inherits Exception and escapes it to dedicated public rescue; diagnostics may fail and propagate. ERR09 replay control keeps unmoved choice/PP prefix distinct from wrapper implementation.','File/console/native diagnostic success and every caller of logonerr remain unexecuted; current interface is complete.')],
['Precise normal/abort/ordinary diagnostic source interface received; target execution and recursive world callback closure remain open.'])
rec(18,[
 'Gain requires internalBattle && moneyGain; sums each opponent owner maximum level*TrainerType base_money, doubles for AmuletCoin then HappyHour, and message/stats use actual capped positive balance delta.',
 'PayDay is a separate second stage including field multipliers and actual capped delta, so one stage can cap the second to0/no prompt.',
 'Lose checks internal/moneyGain and no-money-loss switch, then owner0 maximum level*badge bracket capped to current funds. canLose suppresses black-out wording, not this monetary loss.',
 'Player.money= clamps valid numeric input to0..Settings::MAX_MONEY. Stat writes are reached only after persistent balance assignment, not a transactional pair.'
],[consumer('pbEndOfBattle',['startendfull','money_exact'],'OldDecision dispatch determines victory/loss branch, but current decision4 suppresses early gain and triggers common post-capture gain; internal loss/draw both reach Lose before optional black-out text. No reward for externally ended states merely by numeric decision.','Concrete trainer type/raw party levels and all capture capacity callbacks require their separate valid data scopes.'),
consumer('Player.money writer',['playerfull','money_cap_config','config'],'Exact setter clamping makes before/after delta authoritative for statistics and messages; highest own owner0 segment excludes partner, and configured no-loss switch read is a runtime switch ID rather than a constant boolean. Kernel config/save finite contributions preserve actual producer and serialization limits.','Native save/reload not performed; all other money mutation callers are outside this finite join.')],
['Complete reward/loss and actual balance receiver interface received, including zero/cap/partner controls; no target save execution.'])
rec(19,[
 'Save oldDecision first; wild win with caught queue changes current4 but dispatches old1. Common record/store can mutate currentparty before later restoration, and current4 triggers later money stage.',
 'Internal Pokerus snapshots current $player.party stage1 source indices, checks adjacent current party0 recipients and each33% draw; newly infected recipients are not added to snapshot.',
 'SceneEnd precedes each actual battler CancelChoice and active OnSwitchOut end=true; then participating party0 loop invokes Peer before Pokemon.item=initialItems[0][i].',
 'Shared original/merged partner array and capture-removal identity determine which Pokemon receives each index restoration; normal return is not a universal each-original-item restore guarantee.',
 'Pokemon.item= acceptsnil clearing, storesfalse, truthy unknown ID leaves old value; end receiver is persistent Pokemon setter, not Battler setter. All later cleanup can be unreached after a prior failure.'
],[consumer('CatchAndStoreMixin',['catch_full','startendfull','capture'],'Record/store actual queue follows dispatch and precedes Pokerus/Scene/cleanup. Selected original CAA F08/F09/F10 plus own fullCatch271 supply finite acquire/store identity and cancel prefixes; exact handlers/storage remain bounded.','Every ball rate/OnCatch/raw data/native storage and save/reload remains separate or OPEN.'),
consumer('pbCancelChoice',['command','items','bag','startendfull'],'Each actual slot refunds still-registered item choice then clears choice, unlike eligible next-command direct clear/formal faint direct clear. Full-capacity add may fail while choice handling follows its actual code; old repeated-refund control conditions are preserved.','Each item handler and Bag native presentation is not granted; actual Bag data helper/source scope separately read.'),
consumer('Peer.pbOnLeavingBattle',['peer','burmy_leave','pokemon_item_exact','startendfull'],'Peer runs before restoring current indexed Pokemon item, with usedInBattle[0][i] indexed as stored; BURMY and primal/form resetting are separate exact hooks and their reached exceptions preserve prefix.','All MultipleForms registrations/raw form records remain independently bounded; known finite CRE C transformation package does not close every species.'),
consumer('world after_battle',['after','partner_producer','pokemon_heal','event_registry','startendfull'],'Only after battle return do reached world cleanup/reorder/registered-partner healing/poison-counter and end events execute. Registered partner healing differs from actual participation; status==POISON needs no count>0. COM005 straighten only animation reset, with mandatory F054 clarification and victory BGM/capture ME correction applying to all relevant joins.','All world callbacks/persistent native map reload and every dynamic event remain separately scoped; mandatory clarifications are required companions.')],
['Normal terminal interfaces received with identity/partial commit detail. No blanket cleanup, original-item restoration, whole form registry or save/reload success.'])
rec(20,[
 'Base pbJudgeCheckpoint is empty and returnsnil; loaded clause override is an actual replacement, not evidence base performs an automatic generic judgement.',
 'Default pbDecisionOnTime counts nonnil able individuals on both complete side parties, compares counts first and summed raw HP second, returns1/2/5. Partner is included by party side; eggs/fainted excluded by able?.',
 'Unused pbDecisionOnTime2 is a separate percentage-average implementation and must not be substituted for the called default.',
 'Debug loop result is an intermediate @decision immediately followed by abort; public dedicated rescue maps0. Clause checkpoint has its own current decision/rules/user/move gates and does not override time comparator.'
],[consumer('debug turn limit',['time_exact','battle_loop_complete','abort_raise'],'Actual debug>=100 path calls pbDecisionOnTime, writes result, calls pbAbort; dedicated public rescue writes0 before world return. Nondebug ordinary phases do not call comparator from this guard.','Host debug flag/input and target execution remain unexecuted; no operational timeout claim.'),
consumer('clauses override',['clauses','time_exact'],'Loaded Battle override pbJudgeCheckpoint changes only declared clause checkpoint semantics using current user/move/side/rule gates, and pbDecisionOnDraw override is separate. Complete clauses306 already personally read; no override of default pbDecisionOnTime found in that full defined file.','Other plugin reopenings/external patches excluded by fixed R premise; every move checkpoint caller retains separate binding.')],
['Precise finite base/loaded clause/time-debug interfaces received; no all-clause or all checkpoint-caller domain acceptance.'])
extra={
 'consume_complete':dict(path=d['ability_item']['path'],complete_units=[[226,243]],reading='OwnFULL476 reused; complete Remove/Consume methods actually freshly reread.'),
 'pickup_complete':dict(path=d['abilityeffects']['path'],complete_units=[[2514,2541]],reading='OwnFULL3208 reused; complete Pickup registration freshly reread.'),
 'weather_abilities_complete':dict(path=d['abilityeffects']['path'],complete_units=[[2685,2695],[2709,2719],[2958,2962],[2973,2977],[3030,3034]],reading='OwnFULL3208 reused; complete seven weather registrations freshly reread.'),
 'weather_extenders_complete':dict(path=d['item']['path'],complete_units=[[1752,1774]],reading='OwnFULL1948 reused; four complete weather-rock registrations actually read.'),
 'terrain_abilities_complete':dict(path=d['abilityeffects']['path'],complete_units=[[2721,2728],[2811,2818],[2883,2890],[2964,2971]],reading='OwnFULL3208 reused; complete four Surge registrations, fresh closing delimiters explicitly read.'),
 'terrain_mimicry_complete':dict(path=d['abilityeffects']['path'],complete_units=[[3156,3187]],reading='OwnFULL3208 reused; complete MIMICRY registration actually read.'),
 'terrain_items_complete':dict(path=d['item']['path'],complete_units=[[1780,1784],[1790,1828]],reading='OwnFULL1948 reused; complete TerrainExtender/four seeds actually read.'),
 'terrain_receivers_complete':dict(path=d['ability_item']['path'],complete_units=[[51,54],[367,372]],reading='OwnFULL476 reused; both complete active-gated receiver methods freshly read.'),
 'ui_display_finite':dict(contribution='ui67-complete-units.ndjson',receipt='ui67-reception.v1.json',unit_ids=['UI67-U003','UI67-U004','UI67-U012','UI67-U014'],original_reader='/root/ui_full',reading='Actual complete original records/common premises received earlier; U014 separately fully reread after combined truncation. No receiver Scene sourceFULL.'),
 'ui_animation_finite':dict(contribution='ui67-complete-units.ndjson',receipt='ui67-reception.v1.json',unit_ids=['UI67-U016'],original_reader='/root/ui_full',reading='Actual complete original record including all31 facts and108 exact type/category cells separately untruncated reread; no sourceFULL or asset execution.'),
 'ui_startup_finite':dict(contribution='ui67-complete-units.ndjson',receipt='ui67-reception.v1.json',unit_ids=['UI67-U001','UI67-U002','UI67-U013'],original_reader='/root/ui_full',reading='Actual complete original finite records/common premises received earlier; sourceFULL remains original reader.'),
 'money_exact':dict(path=d['startendfull']['path'],complete_units=[[352,380],[382,402]],reading='OwnFULL568 reused; exact complete Gain/Lose method bodies; declaration/closing identity checked below.'),
 'time_exact':dict(path=d['startendfull']['path'],complete_units=[[517,517],[519,534],[537,553]],reading='OwnFULL568 reused; default and distinct unused method freshly read to own closing end.'),
}
# Method ranges for money are selected below from actual current source boundaries,
# not inferred from old broad range metadata.
moneylines=(R/d['startendfull']['path']).read_text().splitlines()
starts=[i+1 for i,s in enumerate(moneylines) if s.startswith('  def pbGainMoney') or s.startswith('  def pbLoseMoney') or s.startswith('  def pbEndOfBattle')]
assert len(starts)==3
extra['money_exact']['complete_units']=[[starts[0],starts[1]-2],[starts[1],starts[2]-2]]
extra['money_exact']['reading']='OwnFULL568 reused; full methods up to next sibling method, including own closing end and intervening comments; not new sourceFULL.'
keys={k for x in records for c in x['consumer_bindings'] for k in c['actual_definitions']}
dictionary={k:(extra[k] if k in extra else d[k]) for k in sorted(keys)}
identities={};embedded=[]
for key,x in dictionary.items():
    if 'path' not in x:continue
    path=x['path'];b=(R/path).read_bytes()
    assert b==subprocess.run(['git','show',C+':'+path],cwd=R,capture_output=True,check=True).stdout
    identities[path]=dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=subprocess.run(['git','rev-parse',C+':'+path],cwd=R,capture_output=True,text=True,check=True).stdout.strip(),commit=C)
    if key in extra:
        lines=b.decode().splitlines(keepends=True)
        for a,z in x.get('complete_units',[]):
            assert 1<=a<=z<=len(lines)
            embedded.append(dict(id=key+':'+str(a),path=path,range=[a,z],text=''.join(lines[a-1:z]),original_reader='/root/core_atomic_reception',actual_read='Reuse actual ownFULL plus specified fresh complete-unit reread; byte comparison is not new FULL credit.'))
packet=dict(schema='car-original-sourcefacts-manual-consumer-bindings/v1',utc=now,reader='/root/core_atomic_reception',fixed_R=C,
    records=records,source_dictionary=dictionary,source_parent_identities=identities,embedded_complete_necessary_units=embedded,
    mandatory_companions=[],
    all63_semantically_closed=False,all_CORE_complete=False,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED')
for name in ['core-f054-mandatory-straighten-clarification.v1.json','media-reception.mandatory-audio-caller-correction.v1.json','media-audio-correction-delivery-manifest.v1.json']:
    b=(P/name).read_bytes()
    packet['mandatory_companions'].append(dict(path=name,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),reception='Actually full received/authored earlier; exact original bytes retained, no fresh semantic credit from this identity check.'))
out=P/'sourcefact-consumer-bindings-11-20.v1.json'
out.write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n')
for x in records:
    t=by[x['original_complete_record']['id']]
    t['consumer_receptions']=[dict(consumer=c['consumer'],status='ACTUAL_COMPLETE_FINITE_INTERFACE_RECEIVED',binding_packet=out.name,record_id=x['id'],recursive_callbacks='SEPARATELY_BOUND_OR_EXACT_OPEN') for c in x['consumer_bindings']]
    t['acceptance']='COMPLETE_ORIGINAL_FACT_AND_NAMED_FINITE_INTERFACE_ACTUALLY_RECEIVED; recursive callbacks separately bounded'
    t['formal_mapping']='MANUAL_ATOMIC_CLAUSES_PRESENT; no final all-domain denominator'
old['updated_utc']=now
if out.name not in old.setdefault('manual_original_fact_binding_packets',[]):old['manual_original_fact_binding_packets'].append(out.name)
old['all63_semantically_closed']=False
(P/'sourcefact-consumer-receptions.json').write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
b=out.read_bytes();print(out.name,len(b),hashlib.sha256(b).hexdigest(),'facts',len(records),'namedconsumerjoins',sum(len(x['consumer_bindings']) for x in records),'embeddedunits',len(embedded))
