import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_11a.json').read_text());d=base['source_dictionary'];rows=[]
d['triggered_trainer_events']={'path':'Data/Scripts/004_Game classes/008_Game_Player.rb','range':[284,298],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete actual candidate getter; own earlier actual read retained and now reread, no wholeGamePlayer'}
d['event_trigger_producer']={'path':'Data/Scripts/004_Game classes/007_Game_Event.rb','complete_units':[[1,8],[197,258]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE class/trigger accessor and complete refresh; constructor1–16 only partial and not counted complete'}
d['map_interpreter_running']={'path':'Data/Scripts/007_Objects and windows/011_Messages.rb','complete_units':[[4,6],[8,11]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete interpreter/get-running helpers; not wholeMessages'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(791,[
 'BC22 supplies the complete conditional event fixture: no waiting trainer, running map interpreter, double-battle capacity, one distinct trainer candidate, A self-switch off, valid name/distance/reachability and no jumping/over-trigger.',
 'Trainer wrapper requests triggered events with triggers[2], checkIfRunning=false, trainer_only=true.',
 'Game_Player candidate getter explicitly filters event.trigger membership before the trainer-name/reach/jumping/over-trigger tests.',
 'Game_Event refresh assigns trigger from selected page.trigger and stores always_on_top separately; trigger2 is an event trigger value, not a rendered layer comparison.',
 'Keeping all other fixture fields equal, trigger2 passes that filter and trigger0 is excluded.',
 'With exactly one other candidate and own input resolving to one trainer of at most MAX_PARTY_SIZE, wrapper saves [trainer,thisEvent.id] and returns false.',
 'The positive result is a legal static event/page fixture, not a proven Demo chain or a claim every reachability helper/condition ran in a host.'
],['trainer','triggered_trainer_events','event_trigger_producer','map_interpreter_running','double','b_settings'],'page.trigger -> event.trigger -> [2] membership -> other stated guards -> single candidate/party size -> waiting save +false; display layer independent.',open=['Actual Demo/map event execution/native reachability not run; other helper success is explicit fixture premise, not all WORLD completion.'])
row(792,[
 'BC23 assumes valid registered types/metadata and normal audio conversion, no preloaded override, ordinary normal consumers.',
 'Wild battle BGM selects its map W before global fallback; wild victory selects V and capture selects C through independent getters.',
 'Trainer ordered battle fields A then B use the last nonnil field B; later nil leaves A.',
 'Trainer victory fields independently follow last-nonnil order.',
 'When all type fields nil, ordinary trainer getters try nonempty map M, then nonempty global G, then their own fixed default.',
 'Corresponding nextBattleBGM/nextBattleVictoryBGM/nextBattleCaptureME preload X takes precedence and is cloned; the three fields do not alias a shared override.',
 'The selectors do not clear those preloads; normal world animation/skip cleanup may clear them later through separate consumers.',
 'Getter selection is separate from actual playback: accepted correction keeps normal wild/trainer victory on BGM and capture success on ME.',
 'Requests, prefixes and raw-path existence checks do not prove host media output or every native dependency succeeded.'
],['audio','audio_path','wild','trainer','normal_end'],'ordinary caller -> UI67-U020 complete39 facts/source identity -> ordered specific getter -> request; actual caller/audio correction companions mandatory, sourceFULL remains UI reader.',open=['Media/native playback and resources remain NOT_EXECUTED; finite getter/caller/path facts only, no whole UI/MEDIA approval.'])
row(793,[
 'BC24 valid IntroBGM I is strictly resolved from TrainerType; nil/empty intro returns before memory/play request.',
 'With nonempty intro, audio conversion precedes memory handling.',
 'If no memorized BGM and cue delay is truthy, it first clears the delay, then memorizes queued Q and position0.',
 'Only after that memory prefix does it request playing I.',
 'An existing memorized R/r remains unchanged; that branch also does not cancel cue delay.',
 'With no existing memory and no cue delay it memorizes current playing BGM and obtains position; ordinary position-query exception falls back0.',
 'Any later playback/native failure leaves the earlier memory/delay prefix; no general ensure rollback.',
 'This is conditional ordinary intro consumer behavior, not an executed sound cue or proof every event reaches it.'
],['audio','audio_path'],'UI67-U020 full intro facts -> convert -> existing-memory vsdelay/current capture -> BGM request; actual prefix preserved.')
row(794,[
 'BC25 explicitly uses a legal author record storing a later nonnil empty string; it is not an assumption every default parser produces an empty field.',
 'In the ordinary ordered trainer array getter, later empty overwrites prior A because it is nonnil.',
 'The ordinary getter then rejects the empty chosen value as a usable type track and falls back to map M.',
 'The separate direct FromType helper retains a nonnil raw empty field and does not force that branch to an AudioFile.',
 'Its fallback applies only when the direct type field is nil, rather than empty.',
 'Fixed Scripts search locates the direct helper definition, not an ordinary caller; dynamic/plugin callers remain open, so its unusual return does not alter the ordinary battle consumer contract.',
 'Later media/resource handling follows the actual request path, not an automatic original A retry.'
],['audio','audio_path'],'explicit later-empty stored field -> ordinary array overwrite then map fallback OR direct raw empty return; caller scopes distinct.',open=['All dynamic/plugin FromType uses and host treatment of empty requests remain unproved; no new ordinary consumer asserted.'])
row(795,[
 'BC26 supplies valid1v3, user slot0, opposing geometry order[3,5,1], existing fainted3 and live5/1, no mutation during query.',
 'DirectOpposing(true) encounters existing fainted3 and breaks the first loop rather than continuing to search live5.',
 'Its fallback loop returns the first existing object3, so the raw query result is3, not5.',
 'The complete query performs no HP/party/choice writes and no selection input/cancellation; this does not certify later caller behavior.'
],['battlerfull','battlefull','query'],'1v3 geometry -> first loop break at fainted3 -> second loop first existing3; raw result preserved, query only.')
row(796,[
 'BC27 changes only slot3 to live, keeping the same geometry/order.',
 'DirectOpposing(true) now returns3 from the first loop.',
 'A correct live result in this control does not turn the preference option into an all-state guarantee of liveness.'
],['battlerfull','battlefull'],'same order + live3 -> first-loop return3; distinct control from fainted3 fallback.')
row(797,[
 'BC28 changes only slot3 to absent rather than existing fainted.',
 'DirectOpposing skips an absent3, reaches existing live5 and returns5 in its first loop.',
 'Absent and fainted-existing have different branch behavior; no implied occupancy mutation or cleanup.'
],['battlerfull','battlefull'],'absent3 next -> live5 return, unlike break at fainted-existing3.')
row(798,[
 'BC29 passes own-side index0 directly into wild ball resolution with the BC26 state and valid ball/data/normal callbacks.',
 'The resolver calls that own-side battler DirectOpposing(true), yielding raw3.',
 'Because3 is fainted, it substitutes battler.allAllies[0]. That allAllies uses same-side living battlers in global battler-array order, not the old geometry order.',
 'The living allies of3 are global1 then5 in the fixture, so final recovery target is1.',
 'CaptureCalc receives target1 if the subsequent normal item/trainer/use checks and presentation reach it; no assertion of capture success.',
 'This direct internal helper fixture does not claim ordinary menu allows a ball while two opponents survive; menu eligibility remains separate.'
],['catch_full','battlerfull','battlefull','itemdata'],'own index0 -> rawDirectOpposing3 -> fainted fallback allAllies globalorder -> target1 -> conditional CaptureCalc; not menu permit or success.')
row(799,[
 'BC30 supplies explicit opposing index5 to the same direct resolver state.',
 'Because index5 opposes, it uses battlers[5] directly rather than own-side DirectOpposing.',
 'With5 live the fainted-ally fallback is skipped and subsequent capture calculation can receive5.',
 'Ordinary menu may provide explicit opposing targets under its own permission rules; this vector preserves that caller distinction.'
],['catch_full','battlerfull','battlefull'],'explicit opposing5 -> direct current5 -> no own-side geometry/fainted fallback; later capture gates separate.')
row(800,[
 'BC31 has one existing opposing fainted object and no living ally, directly invoking ball resolution with valid item data.',
 'The fainted fallback battler.allAllies[0] is nil in that fixture.',
 'After legal item-name lookup, the next battler.fainted? dereference fails before the ordinary no-target feedback branch can execute.',
 'No refund/rollback or clean false return is promised; earlier external caller/Bag writes are outside this local target lookup.',
 'This is the already documented WP38 boundary, no new required finding or automatic scope expansion from a raw read query.'
],['catch_full','battlerfull','battlefull','itemdata'],'existing fainted -> empty allies -> nil -> next status query failure before no-target text; preserve existing bounded history.')
rows.append(dict(number=801,layout_reason='CM table heading only; obedience/action vectors below require their separate full input and arithmetic decomposition.'))
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_11b.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows),'layout',sum('layout_reason'in x for x in rows))
