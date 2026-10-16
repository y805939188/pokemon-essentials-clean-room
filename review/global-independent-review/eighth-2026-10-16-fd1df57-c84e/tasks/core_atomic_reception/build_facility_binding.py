import datetime, hashlib, json, pathlib, subprocess
P = pathlib.Path(__file__).resolve().parent
R = '/workspace/pokemon-essentials'
C = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
B = 'Data/Scripts/011_Battle/'
units = []
def unit(ident, path, start, end, whole=False):
    raw = subprocess.check_output(['git', '-C', R, 'show', C + ':' + path])
    blob = subprocess.check_output(['git', '-C', R, 'rev-parse', C + ':' + path], text=True).strip()
    lines = raw.decode().splitlines(keepends=True)
    assert 1 <= start <= end <= len(lines)
    text = ''.join(lines[start-1:end])
    units.append(dict(id=ident, repo=R, commit=C, path=path, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest(), git_blob=blob, range=[start,end], content=text, original_reader='/root/core_atomic_reception', original_read_scope='FULL_FILE_READ previously completed; this payload embeds the named complete unit' if whole else 'PARTIAL_FILE_READ; only named complete unit, no whole-file credit'))
    return ident
unit('normal_end',B+'001_Battle/002_Battle_StartAndEnd.rb',405,512,True)
unit('peer_leave',B+'007_Other battle code/004_Battle_Peers.rb',53,59,True)
unit('burmy','Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb',178,200)
unit('success_state',B+'008_Other battle types/004_BattleArenaBattle.rb',4,36,True)
unit('arena_entry',B+'008_Other battle types/004_BattleArenaBattle.rb',42,94,True)
unit('arena_eor',B+'008_Other battle types/004_BattleArenaBattle.rb',127,200,True)
unit('attack_phase',B+'001_Battle/010_Battle_AttackPhase.rb',176,201,True)
unit('use_move',B+'002_Battler/007_Battler_UseMove.rb',154,578,True)
unit('cancel_moves',B+'002_Battler/007_Battler_UseMove.rb',80,95,True)
unit('hp_setter',B+'002_Battler/001_Battle_Battler.rb',107,112,True)
unit('faint',B+'002_Battler/003_Battler_ChangeSelf.rb',64,99,True)
unit('base_entry',B+'001_Battle/005_Battle_ActionSwitching.rb',316,391,True)
unit('send_out',B+'001_Battle/005_Battle_ActionSwitching.rb',289,297,True)
unit('playback_init_start',B+'008_Other battle types/005_RecordedBattle.rb',147,180,True)
unit('playback_commands',B+'008_Other battle types/005_RecordedBattle.rb',198,222,True)
unit('playback_classes',B+'008_Other battle types/005_RecordedBattle.rb',246,256,True)
unit('item_register_consume_return',B+'001_Battle/006_Battle_ActionUseItem.rb',34,75,True)
unit('choice_clear_cancel',B+'001_Battle/009_Battle_CommandPhase.rb',5,23,True)

facts = [
 dict(id='CAR-FAC-BIND-01',units=['normal_end','peer_leave','burmy'], meaning=[
 'At normal pbEndOfBattle entry oldDecision is copied; wild win with caughtPokemon changes current decision to4, while the win/loss/capture presentation branch uses oldDecision. RecordAndStoreCaught precedes capture PayDay, internal global $player.party Pokerus, scene end, per-battler CancelChoice/active OnSwitchOut(true), then current pbParty(0) per-Pokemon Peer leaving and initial-item assignment.',
 'The battle-end Peer call receives usedInBattle[0][party index], true. This read index is not universally the same as the slot/2 index written by ordinary participation. This package preserves that distinction and does not equate merged pbParty(0) with global $player.party or give party1 a matching item-restore loop.',
 'Peer skips nil Pokemon; calls getFormOnLeavingBattle with actual used/end arguments; a truthy differing result sets Pokemon.form; current HP is capped to totalhp if greater; then changePokemonOnLeavingBattle runs. Ruby integer0 is truthy, so returned form0 can be applied.',
 'The complete BURMY registration returns no leaving form unless endBattle AND usedInBattle are truthy. On that qualified path battle.environment Rock/Sand/Cave yields1, None yields2, other yields0. Ordinary switch/faint Peer calls omit endBattle and therefore cannot trigger this BURMY leaving-form change merely because the used flag is true.'
 ], failure='Any reached callback/scene/form setter/item assignment may raise; earlier stored captures, money, Pokerus, choice cancellation, earlier forms/items remain committed. No rollback or ensure continuation is promised. Pokemon.item= is the normal-end assignment receiver, not Battler.item=.', remaining=['Precise usedInBattle producer defect/correct party identity is retained from the independently scoped original root finding; this packet does not reopen or globally deduplicate it.','All other MultipleForms registrations, save/native reload and successful runtime remain OPEN outside explicitly received facts.']),
 dict(id='CAR-FAC-BIND-02',units=['success_state','attack_phase','use_move'], meaning=[
 'AttackPhase clears each nonnil battler slot successState, including currently fainted slots. Full clear sets normal type multiplier/useState0/protectedfalse/skill0. updateSkill sets failed-use skill−2 only if not protected; successful-use super/normal/notvery/ineffective maps2/1/−1/−2; useState0 retains prior skill. Its clear(false) resets type/use/protected while preserving the resulting or retained skill.',
 'UseMove initially marks useState1 after its actual earlier gates; the completed real-hit loop path with numHits>0 marks useState2 and sums non-unaffected target type modifiers if targets exist. Reaching the normal common tail updates successStates for all current living allBattlers.',
 'An ordinary late move failure may return before the common updateSkill call. Thus initial failed state does not prove every failed action immediately writes skill−2. Protected failed use may also retain prior skill. This finite fact preserves source control flow rather than applying a universal failed-use scoring convention.'
 ],failure='Early return before common-tail updateSkill preserves the earlier state prefix; exceptions in attack/move/target callbacks likewise do not imply completed scoring. No battle execution was performed.',remaining=['Specific status/move/Protect producer families not explicitly joined by this packet retain their independent bounded facts or OPEN state.']),
]
facts.extend([
 dict(id='CAR-FAC-BIND-03',units=['arena_eor','cancel_moves','hp_setter','faint'], meaning=[
 'Arena EndOfRound first calls super and returns on any nonzero decision. Otherwise it adds each current slot successState.skill to the accumulated skill, increments count, and returns while count<3. At judgment both battlers CancelMoves(true), suppressing the final-turn Outrage confusion branch; TwoTurnAttack/Rollout/Outrage/Uproar/Bide/FuryCutter reset, and currentMove clears only if HyperBeam==0. HyperBeam is not cancelled.',
 'Mind/skill comparison gives each side1 for ties, or the winner2 and loser0. Body is floor(currentHP*100/max(starthp,1)); its comparison uses the same ratings. Judgment UI gets cloned rating arrays. Rating sums decide tie/both or one loser. Each affected battler receives hp=0, then Faint(false); GainExp and Arena EORSwitch follow.',
 'Battler hp= writes both local integer HP and attached persistent Pokemon.hp. Faint(false) still runs scene faint, opposing defeated marking, runtime reset/statusNONE/count0, qualified happiness change, Peer leaving with default endBattlefalse, unmega/unprimal, choice clear, side last-faint stamp, direct-damage ledger reset, faint ability callbacks and primordial weather check. The source comment about not really losing HP does not suppress the real write-through.'
 ],failure='If the first tie branch battler HP/faint callback raises, the later battler and GainExp/EORSwitch need not run; prior HP/status/form/callback writes survive. Judgment scene can fail before HP writes. No general successful cleanup or transaction is assumed.',remaining=['Individual OnFainting/ability/final save consumers remain their separate bounded obligations.']),
 dict(id='CAR-FAC-BIND-04',units=['arena_entry','base_entry','send_out'], meaning=[
 'Arena startup OnAllBattlersEntering sets changedtrue, both mind/skill0, both startHP to their current battler HP, count0, then super. Arena defines an AsActive-named method with the same resets then super.',
 'SendOut writes usedInBattle[slot&1][slot/2] after Peer entering, scene sendout and menu reset/SetSeen. The separate complete ordinary base entry method calls pbRecordBattlerAsParticipated; that implementation sets the raw nonopposing AmuletCoin flag and asks each current living battler to update participants. This actual entry call name is not pbRecordBattlerAsActive, so these ordinary call sites do not dispatch the Arena AsActive reset override merely because both concern entry.',
 'Arena EORSwitch uses current decision/favorDraw gates then Judge; for each of two sides a fainted slot with a next sequential party index increments its own index, messages, directly Replace, then Entry. It does not call RecallAndReplace or generic eligible-bench enumeration. This packet does not infer all external arbitrary code can never call the AsActive-named method.'
 ],failure='Entry callbacks may mutate state or fail between replacement and remaining entry operations. The existence of an unused-by-these-calls override is not proof its body was executed. This is a finite call-binding fact, not a new formal finding.',remaining=['The FAC reviewer must compare these precise calls with the full WP54/WP58 contract before proposing a document correction; no required/optional count is added here.']),
 dict(id='CAR-FAC-BIND-05',units=['playback_init_start','playback_commands','playback_classes','item_register_consume_return','choice_clear_cancel'],meaning=[
 'Playback initializer takes the recorded arrays/properties and restores parties/trainers for super; Start restores party-start arrays, internal flag, weather/duration, canRun, style/anims, backdrop/base/time/environment, owner items and rules before super. Neither complete initializer nor Start restores a global player Bag snapshot.',
 'PlaybackBattle, PalacePlaybackBattle and ArenaPlaybackBattle include RecordedBattlePlaybackModule and inherit their live Battle classes; these shown playback classes do not include RecordedBattleModule. Playback CommandPhaseLoop returns for non-player phase, increments round, loops exact four indices, skips empty recorded rows, clears each nonempty slot choice, and BAG calls pbRegisterItem with stored item/target/move.',
 'Base RegisterItem writes UseItem plus all three item/target/move values before ConsumeItemInBag. Nil item or registered nonconsumed item returns without removal. A consumed player-owned item calls current global $bag.remove and raises if false; a nonplayer item uses current owner items and delete_at(index) if the collection exists. Thus replayed BAG input can consume or fail against current live Bag, and the choice is already written if removal fails.',
 'ReturnUnusedItem uses current $bag.can_add?/add for player-owned consumed item, or pushes into current nonplayer owner items; failure to return to player Bag raises. CancelChoice attempts this return before unregisterMega/ClearChoice. Playback nonempty rows use ClearChoice directly, not CancelChoice, so their command-load clear itself does not promise an unused prior item refund.'
 ], failure='Malformed or short recorded arrays can fail after roundindex/earlier choices advance. Missing current player item can raise after choice writes; a nonplayer missing index can error. This packet proves the explicit calls and committed prefix, not successful native playback or every Bag internal mutation failure case.', remaining=['Whole serialized-record validation, native Marshal compatibility, full player inventory save/reload, and every item effect/AI suitability policy remain outside this finite contribution.'])
])
packet = dict(schema='r8-core-facility-terminal-skill-playback-finite-binding-v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),original_reader='/root/core_atomic_reception',fixed_R=C,R_tree='7589c800b61ba13a13040ed0d686979b80a84fd0',facts=facts,source_units=units,
 common_premises=['Fixed default source definitions and the qualified normal call paths shown; current objects, arrays, indices and registered data satisfy each stated precondition. Explicit negative/false/return/error cases are retained.', 'Source FULL_FILE_READ credit stays with the named original reader; a receiver must actually read each adopted complete fact and all its named units/common premises. No whole CORE/FAC/Pokemon/forms/Bag approval follows.', 'This packet is static source interpretation; no Ruby/game/native execution, source/formal modification, save/reload or dynamic UI result is claimed.'],
 persistence_reload='Attached Pokemon HP/form/item mutations are persistent-object writes; proving an actual save/reload result requires separately received save-field contracts and remains OPEN here. Runtime choices/successStates/Arena accumulators do not become saved merely because their source was read.',
 mandatory_prior_clarifications=[dict(path='tasks/core_atomic_reception/core-f054-mandatory-straighten-clarification.v1.json',bytes=12899,sha256='d8b8307f27cade1b67c98fb98d78c448fff02399dcdc9766614fdd9bb5f8b3f2'),dict(path='tasks/core_atomic_reception/media-reception.mandatory-audio-caller-correction.v1.json',bytes=3905,sha256='38544141edab159a2f388fd1abd6cfab54deab98a09cdc5263142ae9089d0e41'),dict(path='tasks/core_atomic_reception/media-audio-correction-delivery-manifest.v1.json',bytes=7007,sha256='cdaccb47cc5dbd3a1d508b42a1839ec32d220e807fa236fb2d128b0bc4798018')],
 correction_scope='Mandatory earlier F054 animation-not-direction and normal-victory-BGM/capture-ME corrections remain authoritative; this package adds no contrary audio/direction assertion. FAC reported actually reading those prior packets; that report is not used as our own source reading.',
 new_required=0,new_optional=0,new_context=0,new_vote=0,business_execution='NOT_EXECUTED',UPDATE_NOT_STARTED=True)
packet['prepublication_draft_correction']={'path':str(P/'facility-terminal-skill-playback-binding.v1.json'),'bytes':62998,'sha256':'95fafee0f0e7100a6e9a8c7f7473e8e08bf3fcb1a6d76492ede89b568163b325','adoption':'NOT_PUBLISHED_TO_ANY_RECEIVER; original preserved','correction':'Draft base_entry selected range ended at an unrelated method declaration394; complete combined entry/participation/message unit ends391. Draft F04 incorrectly attributed usedInBattle write to Participated. Actual writer is SendOut289–297, now embedded separately and correctly bound. Manifest navigation filename corrected. No formal finding is created.'}
out=P/'facility-terminal-skill-playback-binding.v2.json'
encoded=(json.dumps(packet,ensure_ascii=False,indent=2)+'\n').encode()
out.write_bytes(encoded)
print(json.dumps(dict(path=str(out),bytes=len(encoded),sha256=hashlib.sha256(encoded).hexdigest(),facts=len(facts),units=len(units),utc=packet['utc'])))
