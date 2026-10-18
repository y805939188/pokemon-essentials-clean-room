import datetime
import hashlib
import json
import pathlib
import subprocess

V = pathlib.Path(__file__).parent
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
READER = '/root/facility_atomic_completion_cloud'
F = json.loads((V / 'forward-mapping.json').read_text())
REV = json.loads((V / 'reverse-mapping.json').read_text())
assert len(F['atoms']) == 1391

# This is assertion bookkeeping. Every statement and route below was manually
# authored after reading its named complete source unit. No target code runs.
rows = []
def a(unit, meaning, receiver, source='R05', relation=None):
    rows.append((source, unit, meaning, receiver, relation))

for unit, meaning, receiver in [
 ('Commands9', 'Recording FIGHT command tag is0.', 'F05§4L75:record-fight-tag'),
 ('Commands10', 'Recording BAG command tag is1.', 'F05§4L78:record-bag-tag'),
 ('Commands11', 'Recording POKEMON command tag is2.', 'F05§4L79:record-switch-tag'),
 ('Commands12', 'Recording RUN command tag is3.', 'F05§4L80:record-run-tag'),
 ('PlaybackCommands141', 'Playback FIGHT command tag is0.', 'F05§6.3L156:play-fight-tag'),
 ('PlaybackCommands142', 'Playback BAG command tag is1.', 'F05§6.3L156:play-bag-tag'),
 ('PlaybackCommands143', 'Playback POKEMON command tag is2.', 'F05§6.3L156:play-switch-tag'),
 ('PlaybackCommands144', 'Playback RUN command tag is3.', 'F05§6.3L156:play-run-tag'),
 ('initialize16', 'A new recorder initializes the actually appended randomnumbers array empty.', 'F05§3L65:record-random-init'),
 ('initialize17', 'A new recorder initializes rounds empty.', 'F05§3L63:record-rounds-init'),
 ('initialize18', 'A new recorder initializes switches empty.', 'F05§5.2L109:record-switches-init'),
 ('initialize19', 'A new recorder initializes roundindex−1.', 'F05§4L71:record-round-index'),
 ('initialize20', 'A new recorder initializes properties to an empty dictionary.', 'F05§3L41:record-properties-init'),
 ('initialize15–22', 'Recorder field initialization precedes base constructor super; a later constructor error doesnot roll back that prefix.', 'F05§3L41:record-constructor-prefix'),
 ('randomnums5/initialize16/pbRandom129–133', 'The public Recording randomnums reader names @randomnums, whereas its constructor/append/dump use @randomnumbers. Default recorder randomnums therefore reads nil; fixed script census found no caller of this accessor.', 'F05§3L65/§9:audited-unconsumed-accessor'),
 ('rounds6', 'The public Recording rounds reader returns its live rounds array reference.', 'F05§3L63/§9:audited-array-accessor'),
 ('pbGetBattleType24–26', 'The module default battle type is0.', 'F05§3L39:type-module-default'),
 ('RecordedBattle228–232', 'Tower recording inherits ordinary Battle, includes only recording module and reports type0.', 'F05§1L11:tower-record-class'),
 ('PalaceRecorded234–238', 'Palace recording inherits Palace behavior, includes recording module and reports type1.', 'F05§5.3L130–132:palace-record-class'),
 ('ArenaRecorded240–244', 'Arena recording inherits Arena behavior, includes recording module and reports type2.', 'F05§5.3L130–132:arena-record-class'),
 ('pbGetTrainerInfo33–34', 'For a Player member in the normalized array, the recorded type is the actual tr.trainer_type getter result.', 'F05§3L46:player-type-source'),
 ('pbGetTrainerInfo34', 'For a Player array member, the full trainer id value is stored directly.', 'F05§3L46:player-id-source'),
 ('pbGetTrainerInfo36', 'For an NPC array member, type is its trainer_type getter result.', 'F05§3L47:npc-type-source'),
 ('pbGetTrainerInfo36', 'For an NPC array member, its name string is cloned.', 'F05§3L41,47:npc-name-clone'),
 ('pbGetTrainerInfo36', 'For an NPC array member, its full trainer id is stored directly.', 'F05§3L47:npc-id-source'),
 ('pbGetTrainerInfo28–45+baseconstructor', 'Ordinary Battle construction wraps each nonnil scalar trainer in an array before the recording start helper; existing direct-bare helper failure is separate.', 'F05§3L46–47:ordinary-array-premise'),
 ('pbGetTrainerInfo28–45', 'Metadata collection traverses array members in order; a later member error leaves no returned complete metadata array and doesnot roll back earlier start-property writes.', 'F05§3L41:trainer-metadata-failure-prefix'),
 ('pbStartBattle48', 'Every recorder start replaces properties with a fresh dictionary before taking fields.', 'F05§3L41:properties-reset-at-start'),
]:
    a(unit, meaning, receiver)

# Eighteen explicitly reviewed record properties. Restore meaning is authored per
# field, including the different constructor versus start restoration moments.
fields = [
 ('internalBattle',49,'Records the current internalBattle value directly.',167,'Playback start assigns recorded internalBattle directly.','45'),
 ('player',50,'Records player metadata through the normalized-array helper.',159,'Playback construction creates new player-side trainer objects from the metadata.','46'),
 ('opponent',51,'Records opponent metadata through the normalized-array helper.',160,'Playback construction creates new opponent trainer objects from the metadata.','47'),
 ('party1',52,'Records party1 with Marshal.dump before ordinary start.',157,'Playback construction restores party1 bytes into the supplied Battle party1 object graph.','48'),
 ('party2',53,'Records party2 with Marshal.dump before ordinary start.',158,'Playback construction restores party2 bytes into the supplied Battle party2 object graph.','48'),
 ('party1starts',54,'Records party1starts with Marshal.dump.',165,'Playback start restores party1starts bytes.','49'),
 ('party2starts',55,'Records party2starts with Marshal.dump.',166,'Playback start restores party2starts bytes.','49'),
 ('weather',56,'Records current field.weather by direct assignment.',168,'Playback start assigns recorded weather to the new field.','50'),
 ('weatherDuration',57,'Records current field.weatherDuration by direct assignment.',169,'Playback start assigns recorded weatherDuration to the new field.','50'),
 ('canRun',58,'Records current canRun directly.',170,'Playback start assigns recorded canRun.','51'),
 ('switchStyle',59,'Records current switchStyle directly.',171,'Playback start assigns recorded switchStyle.','52'),
 ('showAnims',60,'Records current showAnims directly.',172,'Playback start assigns recorded showAnims.','53'),
 ('items',61,'Records items with Marshal.dump; allyItems is a different unrecorded field.',177,'Playback start restores items bytes; it doesnot restore allyItems.','54'),
 ('backdrop',62,'Records current prepared backdrop directly.',173,'Playback start assigns recorded backdrop.','55'),
 ('backdropBase',63,'Records current prepared backdropBase directly.',174,'Playback start assigns recorded backdropBase.','55'),
 ('time',64,'Records current prepared time directly.',175,'Playback start assigns recorded time.','56'),
 ('environment',65,'Records current prepared environment directly.',176,'Playback start assigns recorded environment.','56'),
 ('rules',66,'Records rules with Marshal.dump.',178,'Playback start restores rules bytes.','57'),
]
for key, ln, record, pn, play, formal_line in fields:
    a(f'pbStartBattle{ln}', record, f'F05§3L{formal_line}:record-{key}')
    a(f'Playback.initialize/start{pn}', play, f'F05§6.2L146/§3L{formal_line}:restore-{key}')

for unit, meaning, receiver in [
 ('pbStartBattle47–68', 'Recorder takes all18 properties before calling ordinary start; sequential failures can leave an earlier property prefix and prevent later capture/core entry.', 'F05§3L41,59:start-order-and-prefix'),
 ('pbStartBattle47–68', 'Starting again doesnot explicitly reset rounds/randomnumbers/switches/roundindex; only properties is replaced there.', 'F05§3/§9:audited-reused-recorder-boundary'),
 ('pbDumpRecord70–72', 'Dump orders exactly five components: type, properties, rounds, randomnumbers, switches.', 'F05§3L39:five-tuple-order'),
 ('pbDumpRecord70–72', 'Dump asks Marshal for one opaque serialized byte string; no explicit version field is added.', 'F05§2L35/§5.4L136:opaque-versionless-dump'),
 ('pbSwitchInBetween74–78', 'Recording replacement inquiry first calls inherited selection, then appends its returned value to switches, then returns that same value.', 'F05§5.2L109:switch-append-order'),
 ('pbSwitchInBetween74–78', 'A negative/cancel selection is appended without a success filter; an inherited exception prevents this append.', 'F05§5.2L109,122:negative-vs-error-switch'),
 ('pbRegisterMove80–86', 'Recording move writes [FIGHT,idxMove] only when inherited move registration returns truthy, and then returns true.', 'F05§4L75:move-success-gate'),
 ('pbRegisterMove80–86', 'Falsy inherited move registration returns false without replacing the prior recorded slot.', 'F05§4L75,83:move-failure-retains'),
 ('pbRegisterMove80–86', 'Successful move registration replaces the entire recorded slot, dropping its previous target/command contents.', 'F05§4L71,75:move-whole-slot-replacement'),
 ('pbRegisterTarget88–91', 'Recording target first calls inherited target registration then assigns element2 of the existing recorded slot; inherited return is not tested.', 'F05§4L81:target-order-no-return-gate'),
 ('pbRegisterTarget88–91', 'On a current empty slot array, direct target registration expands it to [nil,nil,target], which playback doesnot dispatch as a command.', 'F05§4L81:incomplete-target-slot'),
 ('pbRegisterTarget88–91', 'Target record assignment can fail after the inherited actual target choice was already mutated, e.g. absent round/slot; no rollback appears.', 'F05§4L81,85:target-choice-prefix'),
 ('pbRun93–97', 'Run calls inherited behavior then always records [RUN,current decision] when that call returns, independent of its return truthiness.', 'F05§4L80:run-decision-snapshot'),
 ('pbRun93–97', 'The original inherited run return value is returned unchanged; recorded decision and method return are distinct.', 'F05§4L80:run-return-vs-decision'),
 ('pbAutoChooseMove99–103', 'Automatic move first calls inherited logic, then unconditionally replaces this slot with [FIGHT,−1] if inherited logic returns.', 'F05§4L76:auto-post-super-slot'),
 ('pbAutoChooseMove99–103', 'Automatic whole-slot replacement drops any target recorded by nested inherited logic; it returns the inherited result unchanged.', 'F05§4L76:auto-target-loss'),
 ('pbRegisterSwitch105–111', 'Recording switch writes [POKEMON,idxParty] only on truthy inherited success; falsy returns false and preserves its prior recorded slot.', 'F05§4L79:switch-registration-gate'),
 ('pbRegisterItem113–119', 'Recording item writes [BAG,item,idxTarget,idxMove] only after truthy inherited item registration; falsy returns false and preserves prior recording.', 'F05§4L78:item-registration-gate'),
 ('pbRegisterItem113–119', 'Inherited item choice/consumption can already occur before an invalid recording index fails, leaving the actual mutation prefix.', 'F05§4L78/§6.2L149:item-prefix-not-transaction'),
 ('pbCommandPhase121–125', 'Each recording command phase increments roundindex before any inherited phase work.', 'F05§4L71:round-increment-first'),
 ('pbCommandPhase123', 'Each recording round begins as four independently written literal empty slot arrays.', 'F05§3L63:four-empty-slots'),
 ('pbCommandPhase121–125', 'A later base command/scene exception leaves the newly appended current round; no ensure removes it.', 'F05§4L71,85:round-exception-prefix'),
 ('pbStorePokemon127', 'Recording module alone overrides storage as an empty method; it supplies no ordinary capture/store side effect.', 'F05§3L67:recording-empty-store'),
 ('pbRandom129–133', 'Recording random first asks inherited pbRandom(num), appends the returned value once, then returns that value.', 'F05§5.1L91:record-random-order'),
 ('pbRandom129–133', 'Only calls reaching this battle random wrapper are appended; independent globalrand/AI random calls are not intercepted by it.', 'F05§5.1L93–105:random-call-domain'),
 ('Playback.initialize148–152', 'Playback keeps the supplied decoded type/properties/rounds/randomnums/switches components as direct references; it doesnot validate or clone those component arrays here.', 'F05§3L39/§5.4L136:decoded-component-references'),
 ('Playback.initialize153', 'Playback starts roundindex−1.', 'F05§6.3L156:playback-round-index-init'),
 ('Playback.initialize154', 'Playback starts randomindex0.', 'F05§5.4L136:playback-random-index-init'),
 ('Playback.initialize155', 'Playback starts switchindex0.', 'F05§5.4L136:playback-switch-index-init'),
 ('Playback.initialize156–161', 'Playback restores both party graphs and builds trainer metadata objects as arguments before ordinary Battle construction; malformed restoration can prevent that construction.', 'F05§6.2L146:restore-before-base-construction'),
 ('Playback.pbStartBattle164–180', 'Playback restores starts, internal flag, field/config values, then items and rules before ordinary start; partial restore errors preserve prior assignments.', 'F05§6.2L146:playback-start-prefix'),
 ('Playback.pbSwitchInBetween182–186', 'Playback switch inquiry ignores battler/checkLax/cancel parameters and consumes the next shared switch entry without asking selection or rechecking it here.', 'F05§5.2L109:playback-inquiry-consumption'),
 ('Playback.pbSwitchInBetween182–186', 'Playback switchindex increments even when the indexed entry is nil from array exhaustion.', 'F05§5.4L136:switch-exhaustion-increment'),
 ('Playback.pbRandom188–192', 'Playback random ignores the requested bound and returns the next recorded random entry without resampling or range validation here.', 'F05§5.1L91/§5.4L136:playback-random-bound-ignored'),
 ('Playback.pbRandom188–192', 'Playback randomindex increments even when exhaustion returned nil; downstream consumers determine its later failure.', 'F05§5.4L136:random-exhaustion-increment'),
 ('Playback.pbDisplayPaused194–196', 'Playback paused-display requests ordinary pbDisplay instead of the ordinary paused scene method.', 'F05§6.4L160:paused-display-downgrade'),
 ('Playback.pbCommandPhaseLoop199', 'Playback command loop returns immediately for isPlayer false, before advancing its round index.', 'F05§6.3L156:nonplayer-no-loop'),
 ('Playback.pbCommandPhaseLoop200', 'The true/player playback loop advances roundindex once before processing slots.', 'F05§6.3L156:player-advance-round'),
 ('Playback.pbCommandPhaseLoop201', 'The playback loop visits only indices0,1,2,3, independent of recorded larger-round length.', 'F05§3L63/§6.3L156:fixed-four-consumption'),
 ('Playback.pbCommandPhaseLoop202', 'Empty slot arrays skip before any actual-choice clear.', 'F05§6.3L156:empty-slot-skip'),
 ('Playback.pbCommandPhaseLoop202', 'Absent round or absent slot fails while indexing or calling length before a normal command dispatch; this is separate from random/switch exhaustion.', 'F05§5.4L136:missing-round-slot-first-failure'),
 ('Playback.pbCommandPhaseLoop203–204', 'Every nonempty playback slot clears its actual choice before command tag dispatch, including unknown/unrecognized tags.', 'F05§6.3L156:clear-before-tag'),
 ('Playback.pbCommandPhaseLoop205–210', 'FIGHT with index−1 calls automatic move(false); every other index, including−2, calls inherited registerMove.', 'F05§6.3L156:fight-sentinel-routing'),
 ('Playback.pbCommandPhaseLoop211–213', 'A truthy target element triggers registerTarget after fight registration; target0 is truthy in Ruby, nil/false skip.', 'F05§6.3L156:target-truthiness'),
 ('Playback.pbCommandPhaseLoop205–213', 'Playback fight doesnot branch on registerMove/auto return before optional target registration.', 'F05§6.3L156:fight-return-unchecked'),
 ('Playback.pbCommandPhaseLoop214–215', 'BAG passes recorded item, target and move-index arguments to inherited item registration.', 'F05§6.2L149/§6.3L156:bag-base-registration'),
 ('Playback.pbCommandPhaseLoop216–217', 'POKEMON passes its party-index argument to inherited switch registration, retaining that method own qualifications.', 'F05§6.3L156:switch-base-registration'),
 ('Playback.pbCommandPhaseLoop218–219', 'RUN directly assigns recorded decision without re-running escape probability or requiring a battler object in that branch.', 'F05§6.3L156:run-direct-decision'),
 ('Playback.pbCommandPhaseLoop198–222', 'Playback dispatch has no catch-all command correction, malformed-record repair or record-production hook.', 'F05§5.4L136/§6.3L156:unknown-command-boundary'),
 ('PlaybackClasses246–256', 'Playback classes inherit their ordinary Tower/Palace/Arena superclass plus Playback module, not the Recording module.', 'F05§6.2L146/§6.4L160:distinct-playback-inheritance'),
 ('PlaybackClasses246–256/store census', 'Playback defines no empty storage override; a direct store call binds ordinary storage. Ordinary facility capture input limits do not constitute this helper protection.', 'F05§3L67/§6.2L152:playback-store-distinction'),
 ('PlaybackHelper.pbGetOpponent262–264', 'BGM opponent helper independently builds trainers from the decoded opponent metadata.', 'F05§6.1L142:bgm-opponent-rebuild'),
 ('PlaybackHelper.pbGetBattleBGM266–268', 'Playback BGM is requested from ordinary trainer-BGM resolution using reconstructed opponents; it is not saved in the eighteen properties.', 'F05§6.1L142:bgm-not-snapshot'),
 ('PlaybackHelper.pbCreateTrainerInfo271', 'Nil/false trainer metadata returns nil without constructing trainer objects.', 'F05§6.2L146:absent-trainer-rebuild'),
 ('PlaybackHelper.pbCreateTrainerInfo273–275', 'Each metadata entry of exact length4 is classified as Player; any other length takes NPC branch rather than a tag/type validation.', 'F05§6.2L146:tuple-length-discriminator'),
 ('PlaybackHelper.pbCreateTrainerInfo275–276', 'Player reconstruction calls Player.new(recorded name,type), then assigns the recorded badges array directly.', 'F05§6.2L146:player-badges-restoration'),
 ('PlaybackHelper.pbCreateTrainerInfo278–280', 'NPC reconstruction calls NPCTrainer.new(recorded name,type), then assigns lose/win texts with falsey values replaced by ellipsis.', 'F05§6.2L146:npc-text-restoration'),
 ('PlaybackHelper.pbCreateTrainerInfo282–285', 'Every reconstructed trainer receives the recorded id after construction and is appended in input order.', 'F05§6.2L146:id-and-order-restoration'),
 ('PlaybackHelper.pbCreateTrainerInfo270–286', 'No helper here assigns restored battle party arrays to each new trainer.party; ordinary new Trainer.party begins empty.', 'F05§6.2L146:trainer-party-distinct-receiver'),
]:
    a(unit, meaning, receiver)

for unit, meaning, receiver, source in [
 ('Player.initialize38–56/getter72–74', 'New playback Player starts character_ID0; its trainer_type getter reads current PlayerMetadata for character_ID rather than the recorded constructor @trainer_type.', 'F05§6.2L146/§9:audited-player-type-derived-reader', 'REC-PLAYER'),
 ('PlayerMetadata.get45–49', 'PlayerMetadata lookup validates an Integer, uses DATA[player_id] if present and otherwise DATA[1]; absent both yields nil before caller.trainer_type.', 'F05§6.2L146/§9:player-metadata-fallback-premise', 'REC-META'),
 ('PlayerMetadata.get45–49+Player.getter72–74', 'Thus playback Player reported type equals the currently registered ID0 type if present, otherwise ID1 type, conditional on that metadata existing; recorded type alone is not an exact getter-restoration guarantee.', 'F05§6.2L146/§9:conditional-derived-type-not-new-product-API', 'REC-META'),
 ('Trainer.initialize169–175/NPC181–194', 'Base new Trainer validates constructor type through TrainerType registry, assigns name/id/language and empty party; NPC subclass adds version0 by default, an empty items array and nil lose/win texts.', 'F05§6.2L146:trainer-construction-premises', 'REC-TRAINER'),
 ('pbGetTrainerBattleBGM81–82', 'A truthy live nextBattleBGM immediately supplies its clone before trainer lookup, including on playback BGM resolution.', 'F05§6.1L142:live-next-bgm-priority', 'REC-AUDIO'),
 ('pbGetTrainerBattleBGM85–90', 'Without live override, BGM traverses trainers in order and retains the last truthy TrainerType battle_BGM; an empty string is truthy and can replace an earlier value before nonempty check.', 'F05§6.1L142:trainer-bgm-order', 'REC-AUDIO'),
 ('pbGetTrainerBattleBGM91–102', 'If trainer music doesnot yield an audio object, resolution tries current map metadata, then current global metadata, then Battle trainer fallback.', 'F05§6.1L142:live-bgm-fallbacks', 'REC-AUDIO'),
 ('Battle.pbRandom93', 'Ordinary Battle random is rand(x), so recording wrapper captures globalrand only at this object method boundary.', 'F05§5.1L91:base-random-source', 'S08'),
 ('Scene.initialize5–11', 'Normal scene construction starts abortablefalse and abortedfalse; pbPlayBattle explicitly sets abortabletrue afterward.', 'F05§6.1L142/§6.4L160:abortable-setup', 'REC-SCENEINIT'),
 ('Scene.pbInputUpdate103–109', 'Scene input first updates Input, then BACK trigger with abortabletrue and abortedfalse marks abortedtrue before calling battle.pbAbort.', 'F05§6.4L160:abort-trigger-prefix', 'REC-SCENE'),
 ('Battle.pbAbort4–6', 'Ordinary pbAbort raises the dedicated BattleAbortedException.', 'F05§6.4L160:abort-exception', 'C-JUDGE'),
 ('Battle.pbStartBattle247–277', 'Only pbStartBattleCore is inside the dedicated abort rescue: caught abort sets decision0 and calls scene.end; pre-core ensure/starting hooks are outside that rescue.', 'F05§6.4L160:abort-rescue-boundary', 'C-JUDGE'),
 ('Scene.pbEndBattle365–372', 'Scene end first clears abortable, shows blank window, then fades BGM/sprites and disposes sprites; it doesnot itself run normal battle-end gameplay callbacks.', 'F05§6.4L160:scene-end-prefix', 'REC-SCENE'),
 ('Battle.pbDisplay816–826', 'Ordinary Battle display forwards to scene regular-message method; ordinary paused display would forward to the separate paused method, which Playback bypasses.', 'F05§6.4L160:display-forwarding', 'S08'),
 ('Scene.pbUpdate79–83', 'A message update executes graphics update, input/abort update, then frame update in that order.', 'F05§6.4L160:message-update-and-abort-order', 'REC-SCENE'),
 ('Scene.pbWaitMessage169–180', 'Brief-message wait uses elapsed uptime and a1-second constant, repeatedly updates the scene, then clears message text/visibility/brief flag.', 'F05§6.4L160:brief-wait-static-clock', 'REC-SCENE'),
 ('Scene.pbDisplayMessage184–223', 'Regular playback messages skip busy text forward automatically via abortable; once fully shown, regular message closes after1 second rather than requiring command confirmation.', 'F05§6.4L160:regular-message-auto-progress', 'REC-SCENE'),
 ('Scene.pbDisplayMessage184–223', 'Within regular message update, BACK may abort before later text skip/close checks; arbitrary graphics/input/message errors have no rollback guarantee here.', 'F05§6.4L160:message-abort-error-prefix', 'REC-SCENE'),
]:
    a(unit, meaning, receiver, source)

premise = ('FixedR/B8 default methods/load order without later overrides; valid source receiver types and decoded record shapes except where a named malformed/absent case is stated. '
           'Called registry/scene/constructor/Marshal dependencies return normally to the stated observation unless the failure prefix is explicit. '
           'Recording/Playback wrappers, complete CORE5facts and18terminal units, own constructor/Trainer/Player/Catch/Peer and named Scene/audio units are finite joins only. '
           'Native serialization, real replay/UI/resources and complete switch-effect/random-consumer/PBS preconditions remain NOT_EXECUTED/OPEN. '
           'Audited internal accessor/reused-object/type-getter facts are source descriptions; no independent future public API compatibility requirement is inferred.')
new = []
for offset,(source,unit,meaning,receiver,relation) in enumerate(rows,1392):
    atom={'id':f'FAC-A{offset:04}', 'source':source,'unit_locator':unit,'assertion':meaning,
          'formal_receivers':[receiver], 'premise':premise, 'pending_dependencies':[],
          'status':'BOUNDED_SOURCE_FACT_AND_EXPLICIT_FORMAL_CHILD_OR_AUDIT_SCOPE_ROUTING',
          'formal_relation':relation or 'Explicit property/flow child or explicitly scoped source audit detail; not all RC catalog prerequisites or mandatory compatibility surface.',
          'evidence':'SOURCE_STATIC','execution':'NOT_EXECUTED','reader':READER}
    new.append(atom)
    REV['mappings'].append({'formal_clause':receiver,'atomic_assertion':atom['id'],'meaning':meaning,
                            'source':source,'source_unit':unit,'premise':premise,'status':atom['status'],
                            'pending_dependencies':[], 'relation':'EXPLICIT_NAMED_FORMAL_CHILD_OR_DECLARED_INTERNAL_SOURCE_SCOPE'})

source_paths={
 'REC-PLAYER':'Data/Scripts/015_Trainers and player/004_Player.rb',
 'REC-TRAINER':'Data/Scripts/015_Trainers and player/001_Trainer.rb',
 'REC-META':'Data/Scripts/010_Data/002_PBS data/017_PlayerMetadata.rb',
 'REC-AUDIO':'Data/Scripts/019_Utilities/003_Utilities_BattleAudio.rb',
 'REC-SCENE':'Data/Scripts/011_Battle/004_Scene/001_Battle_Scene.rb',
 'REC-SCENEINIT':'Data/Scripts/011_Battle/004_Scene/002_Scene_Initialize.rb',
}
ids={}
buffers={}
for key,path in source_paths.items():
    b=subprocess.check_output(['git','-C','/workspace/pokemon-essentials','show',R+':'+path])
    buffers[key]=b.decode().splitlines()
    ids[key]={'repo':'/workspace/pokemon-essentials','commit':R,'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
              'blob':subprocess.check_output(['git','-C','/workspace/pokemon-essentials','rev-parse',R+':'+path]).decode().strip()}
    F['source_identities'][key]=ids[key]
units=[]
for key,lo,hi,name in [
 ('REC-PLAYER',38,56,'Complete Player constructor'),('REC-PLAYER',72,74,'Complete Player trainer_type getter'),
 ('REC-TRAINER',169,175,'Complete Trainer constructor'),('REC-TRAINER',181,194,'Complete NPC class'),
 ('REC-META',45,49,'Complete PlayerMetadata.get'),('REC-AUDIO',81,103,'Complete trainer BGM resolver'),
 ('REC-SCENEINIT',5,11,'Complete scene constructor'),('REC-SCENE',3,3,'abortable accessor'),
 ('REC-SCENE',8,8,'message pause constant'),('REC-SCENE',79,83,'Complete scene update'),
 ('REC-SCENE',103,109,'Complete scene input/abort update'),('REC-SCENE',169,180,'Complete brief message wait'),
 ('REC-SCENE',184,224,'Complete regular message and alias'),('REC-SCENE',230,265,'Complete paused message'),
 ('REC-SCENE',365,372,'Complete scene end'),
]:
    units.append({'source':key,'identity':ids[key],'range':[lo,hi],'name':name,'content':'\n'.join(buffers[key][lo-1:hi]),
                  'reading':'ACTUAL_COMPLETE_NAMED_UNIT_ONLY','actual_reader':READER})

for atom in F['atoms']:
    if 235 <= int(atom['id'][5:]) <= 241:
        atom['pending_dependencies']=[]
        atom['status']='BOUNDED_SOURCE_AUDIT_ROOT_NO_REQUIRED_RECEIVED'
        atom['root_receipt']='root-recorded-scalar-reception.exact.json'
for item in REV['mappings']:
    if 235 <= int(item['atomic_assertion'][5:]) <= 241:
        item['pending_dependencies']=[]
        item['status']='BOUNDED_SOURCE_AUDIT_ROOT_NO_REQUIRED_RECEIVED'
        item['root_receipt']='root-recorded-scalar-reception.exact.json'

F['atoms'].extend(new)
F['bounded_denominator']=len(F['atoms'])
F.setdefault('v2_increments',[]).append({'path':'recorded-properties-flow-atomic-increment.v2.json','count':len(new),'ids':[new[0]['id'],new[-1]['id']],'utc':NOW})
REV['true_bounded_assertions']=len(F['atoms'])
REV['v2_new_exact_child_bindings']=len(REV['mappings'])-992
packet={'schema':'facility-recorded-manual-property-and-flow-increment/v2','utc':NOW,'reader':READER,
        'explicit_source_assertions':new,'source_identities':{**{k:F['source_identities'][k] for k in ['R05','R10','S08','C-JUDGE']},**ids},
        'complete_supplemental_units':units,
        'source_receipts':['50ec21 complete R05 287L reread','e4f46b complete R10 and Player/Trainer required getters','215fb1 complete PlayerMetadata95L','f1d66d finite complete BGM/Scene/abort units','4985a7 complete display forwarding/update/constants',
                           'core-command-ending-reception.v2.json','core-terminal-skill-playback-reception.v2.json','counter_cd003_existing_fac/source-evidence.json whole named files'],
        'formal_receipts':['e3699f+93784b whole currentWP58','cf037b currentWP58L138–181','original8F fulltext'],
        'qualification':'Finite manual property/flow or declared internal-source audit routing. All18property record/restore meanings individually authored. Not a full normalized RC/source/formal denominator, all switch-effect/AI/PBS closure, or automatic requirement to preserve internal Ruby APIs. Current WP58 already correctly assigns Recording empty store; rootCD003 optional WP26 attribution only. Player getter current-metadata dependency is retained as conditional audited fact, no newfinding classified here.',
        'root_scalar_pending_correction':'Only v2 FAC-A0235–0241 stale adjudication dependency cleared after actual root NO_REQUIRED receipt; frozenv1 retained.',
        'new_required':0,'new_optional':0,'new_contexts':0,'new_votes':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
def dump(name,obj):
    (V/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
dump('recorded-properties-flow-atomic-increment.v2.json',packet)
dump('forward-mapping.json',F)
dump('reverse-mapping.json',REV)
P=json.loads((V/'progress.json').read_text());P.update(updated_utc=NOW,manually_authored_finite_source_assertions=len(F['atoms']),source_to_formal_bindings=len(REV['mappings']),finite_new_child_bindings=len(REV['mappings'])-992,state='RUNNING_SAFARI_CONTEST_GENERATOR_AND_PBS_PROOF_TAILS')
dump('progress.json',P)
D=json.loads((V/'atomic-denominator.json').read_text());D['updated_utc']=NOW;D['manual_bounded_source_assertions'].update(count=len(F['atoms']),id_end=new[-1]['id']);D['finite_reverse_bindings'].update(count=len(REV['mappings']),qualification=f"992historicalregionbindings+{len(REV['mappings'])-992}newexplicitmanualchild/audit routes; not a global independent formalchilddenominator.");D['finite_recorded_properties_flow']={'children':len(new),'membership':'recorded-properties-flow-atomic-increment.v2.json','qualification':packet['qualification']};dump('atomic-denominator.json',D)
L=json.loads((V/'reading-ledger.json').read_text());L['updated_utc']=NOW;L.setdefault('v2_additional_source_reads',[]).append({'utc':NOW,'path':'recorded-properties-flow-atomic-increment.v2.json','complete_supplemental_units':len(units),'actual_receipts':['215fb1','50ec21','e4f46b','f1d66d','4985a7'],'qualification':'Complete finite named UI/audio/metadata/Trainer/Player source units; whole PlayerMetadata95L text ownread, whole otherfile credit only prior actual reader ledger. No allworld/UI/fullBGMmedia/runtime inheritance.'});L['failures'].append({'receipt':'dee868','meaning':'Wrong guessed NPCTrainer filename grep returned no match; recovered actual class in already wholly read Trainer.rb via ba21e6; no failed-path reading credit.'});dump('reading-ledger.json',L)
print('new',len(new),'ids',new[0]['id'],new[-1]['id'],'total',len(F['atoms']),'bindings',len(REV['mappings']))
b=(V/'recorded-properties-flow-atomic-increment.v2.json').read_bytes();print('packet',len(b),hashlib.sha256(b).hexdigest())
