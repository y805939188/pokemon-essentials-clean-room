import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_07c.json').read_text());d=base['source_dictionary'];rows=[]
d['recordedfull']={'path':'Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb','range':[1,287],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ'}
d['pokemon_mega_full']={'path':'Data/Scripts/014_Pokemon/002_Pokemon_MegaEvolution.rb','range':[1,83],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ; data/formcallback callees separately bounded'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(337,[
 'Full calculation iterates0..maxBattlerIndex, skips nilBattler; actor reference and actual pbSpeed are captured with initial priority/bracket0 and tievalue.',
 'Collection is declared maximum slot bound, not an unbounded scan of every unexpectedly created Battler. Existing GR8-COM-003 mixed-order overflow remains its own bounded root; legal declared-layout comparison is supported.',
 'Stored conceptual comparison inputs include identity/speed/abilitybracket/itembracket/combinedbracket/movepriority/tie. Formal intentionally doesnot require source sevenelement representation.',
 'Full table may contain fainted actual Battlers; ordinary pbPriority filters them, while speed-only variant includes them and consumers impose local eligibility.'
],['priority','battlefull','attack'],'declaredbound→presentBattler capture→cached comparison inputs→consumer filtering; no invented wholearray sweep.')
row(338,[
 'For UseMove only, actual move.pbPriority(user) supplies basepriority, then active ability PriorityChange callback may replace it.',
 'Full and incremental calculations both write computed movepriority to cached entry AND choice[4]; Shift computes no movepriority and retains0 in fullentry.',
 'First-target PsychicTerrain and QuickGuard read saved choice[4]>0, not a fresh raw move priority; later ability/state changes need actual recalculation to change this savedvalue.',
 'PriorityChange concrete registry includes current activeability gate and handler defaults. This finite stage doesnot imply every callback family or AI estimate has been semantically closed.'
],['priority','checksfull','abilityeffects','usagefull','ability_item'],'movepriority callback→abilitymodifier→two savedwrites→target protection consumers.',open=['All specific priority-changing move overrides/AI estimates beyond actual read classes and full finite contribution facts remain OPEN.'])
row(339,[
 'Only UseMove OR Shift full-entry choices evaluate bracket modifiers, each separately guarded actual abilityActive? and itemActive?. Other actions keep initialized0.',
 'Ability and item callback results cached separately. Source ability negative bracket here is STALL, not TRUANT; exact formal parenthetical name is existing required/P3 GR8-COM-001 only.',
 'Every calculate call clears both PriorityAbility/PriorityItem flags on every cached entry before merge, including partial calls on an index subset.',
 'If abilitybracket==0&&itembracket!=0 OR abilitybracket<0&&itembracket>=1, final adopts item and PriorityItemtrue.',
 'Otherwise abilitybracket!=0 marks PriorityAbilitytrue and keeps ability value; both0 yields0 and bothflagsfalse. Thus faster positiveitem beats negativeability.',
 'Attack-stage notification reads adopted flag then current activeability/item Use handler; item can be consumed after message. Adopted table flag alone is not guarantee a message/callback occurs.'
],['priority','attack','abilityeffects','item','ability_item'],'two gatedproducer callbacks→cache→merge provenanceflags→active-use notification/conditionalconsumption.',support='EXISTING_ROOT_REQUIRED_BOUNDED',open=['Existing GR8-COM-001 fixes only STALL/TRUANT example naming; other merge/flags clauses supported. Complete additional concrete callback consumer closure remains OPEN.'])
row(340,[
 'Full calculation creates index permutation and iterates i with r=i+pbRandom(length−i), swapping; tievalue for presentactor derives shuffled randomOrder[index].',
 'Every actual fullCalc=true repeats shuffle, clears/rebuilds priority array; repeated pbPriority getters alone draw nothing.',
 'Incremental fullCalc=false retains existing tievalues and actorentries, with optional current speed/priority replacements; no same-round reshuffle in that branch.',
 'All fullcalc calls still use actual Battle.pbRandom implementation; ordinary base rand or RecordedBattle override must be distinguished. No actual seed/replay execution inferred.'
],['priority','battlefull','recordedfull'],'fullshuffle versuscachedincremental→same-round stable comparator tie; no global unique RNG claim.')
row(341,[
 'Rearranging sorts movepriority descending, then combinedbracket descending before considering speed.',
 'TrickRoom snapshottrue sorts speedascending; false sorts speeddescending; equal speed uses cached tie descending in either branch.',
 'The comparator uses cached speed captured by calculation, not immediate actual speed from each priority getter. Zero/negative speed behavior not broadened beyond valid source values.',
 'Earlier stages can force MoveNext or defer Quash outside this ordering; the formal comparison is tableorder, not unconditional final action schedule.'
],['priority','attack'],'cached comparator tuple→tableorder→scheduler forced/deferred/moved eligibility.')
row(342,[
 'Base attackphase after scene/reset bookkeeping calls pbCalculatePriority(true) before priority notifications/Call/Switch/Items/Mega/Moves.',
 'This bullet specifies that phase entry full calculation; it doesnot negate later EOR incremental calculation or public full API callers. Callback/native exceptions may stop before actions.'
],['attack','priority','eor'],'attackphase entry→full priority snapshot→ordered stages; scope is this phase.')
row(343,[
 'Incremental calculation first compares current positiveTrickRoom to cached flag; mismatch updates flag and requiresresort even if no member speed changes.',
 'It traverses existing entries and optionally limits speed/movepriority reread to indexArray members. It doesnot append newly created table entries or rerandomize tie.',
 'Each included entry rewrites speed and flags rearrange on inequality; current UseMove rereads basepriority and activeability modifier, writes entry and choice[4], rearranges on inequality.',
 'Incremental path retains ability/item bracket caches; merge/provenance recomputed from those cached values, not fresh bracket callbacks. Arbitrary ability/item replacement doesnot by itself reroll QuickDraw/Claw.',
 'Base itemphase calls incremental only after completed itempass and RECALCULATE_TURN_ORDER_AFTER_SPEED_CHANGES; earlydecision return skips it.',
 'Ordinary selected actionprocess after normal wrapper/Judge invokes incremental when sameconfigtrue; exact forcednested/currentfailure routes have their own actual call order. API itself doesnot contain this config gate.',
 'Current fullBattleSettings derives speedchanges config from generation>=8; receivedKernel producerMECH8 fixes ittrue. It is a producer fact, not blanket allpriority callback execution.'
],['priority','attack','use','b_settings','config','debuglog'],'callerconfiguration/completion→incremental snapshot comparison→selected entries→cachedbracketmerge→conditionalresort; failedprefix retained.')
row(344,[
 'Normal Mega helper after form/UI/slot/ability callbacks invokes pbCalculatePriority(false,[idxBattler]) only when Mega-order settingtrue.',
 'Setting derives generation>=7 and currentMECH8 true; update remains incremental only actor speed/ability movepriority, retaining allcachedbrackets/ties.',
 'If earlier Mega callback raises before finalcall, source can retain transformed Pokemon, refreshprefix or usedslot without recalculation. No transaction/alwaysresort guarantee.'
],['other','priority','b_settings','config'],'Mega ordered writes→optional singleactorincremental; exact failureprefix and cachedinputs retained.')
row(345,[
 'pbPriority(true) constructs temporary tuples from cached actor/speed/tie; sorts speeddescending regardless of TrickRoom, ignoring movepriority/brackets.',
 'It includes each cached actor without ordinary faintfilter; callers such as redirection perform their own actual liveness/near/opposition/ability gates.',
 'This getter neither rereads actualspeed nor calls calculate. It returns newactor array, leaving cached priority table order unchanged; existing CORE-F049 new-speed shorthand is conditional on prior calculation.'
],['priority','targetresolve','eor','battlerfull'],'cachedspeed/tie getter→temporary order→consumer-specific gates; no implicit freshspeed or snapshot update.')
row(346,[
 'Cached table retains actors after their action. Ordinary pbPriority omits currentfainted but not moved actors.',
 'Move scheduler checks movedThisRound on forcednext, ordinary and generationquash passes; completed actor skipped there even while present in table.',
 'Failure before EndTurn completionwrite can leave actor eligible for a fresh scheduler pass; normal actionrefusal still EndTurn writesmoved. Existing NG01 finite conditional retry remains separate exact vector.'
],['priority','attack','use','battlerfull'],'tablepresence versuslive getter versusactualmovedfilter; no delete-after-action inference.')
row(347,[
 'CanMega checks switchdisable first, then Battler.hasMega?, then wildfalse; only after these three can DEBUG&&Ctrl returntrue.',
 'Battler.hasMega? rejects Transform then delegates realPokemon.hasMegaForm?. Pokemon searches same species and matching unmega form, first accessible stone OR move entry, and requires result>0 differentcurrentform.',
 'After debug shortcut, SkyDrop>=0 refuses, ring predicate required, then owner/side mega slot must be−1. Debug bypass doesnot skip the first three restrictions.',
 'Constructor builds ringIDlist from current GameData Item MegaRing flag. Player-owned check uses Bag.has? for anylistedID; other owner uses traineritems include?, nilitemsfalse.',
 'Menu passes CanMega result to scene and toggles registration via callback; bare registration doesnot callqualification. UI button state actual consumer held by finiteUI contribution, no native Input execution.',
 'GameData species iteration and real form/item/move predicates are separately delegated prerequisites; no complete compiled species/acquisition/reload proof inferred from this full83L helper.'
],['other','battlerfull','pokemon_mega_full','battlefull','bag','itemdata','command','ui_command'], 'switch→realMega accessibility→wild→debug exception→SkyDrop→owner ring→slot−1→menu display, separate bare register.',open=['Complete species record/registry iteration and form/item/move getter lifecycle beyond finite CRE/Media contributions remain OPEN; actual UI menu unit binding remains finite receivedUI, not native run.'])
row(348,[
 'Register computes side/owner and unconditionally writes actorindex; unregister clears only if currently equalactor, preserving anotheractor or−2.',
 'Toggle compares current slot to actorindex: equal→−1 else→actorindex. Registration is owner-shared, not one independent slot perPokemon.',
 'CancelChoice refunds eligible item first, then unregisters Mega, then clearschoice; callback error can leave later unregister/clear unperformed.',
 'Fightmenu Shift unregisters before RegisterShift. New ordinary move registration doesnot itself cancelMega, permitting changing chosenmove aftertoggle.',
 'Commandphase reset clears only nonnegative leftover registrations to−1, retaining consumed−2; initial constructor slots are eachowner−1. This phase is not reset of already-used allowance.'
],['other','command','battlefull','priority'],'bare slotwrites→menu/cancelcommand order→nextphase nonnegativeclear; permanentusedslot preserved.')
row(349,[
 'Attackphase after Switch/Items and each explicit decision return invokes Mega stage, then Moves; currentpriority snapshots and their earlier messages already exist.',
 'Mega stage ordinary pbPriority iteration skips wild, nonUseMove, fainted and owner-slot not equal actor; qualifyinghelper called before move loop.',
 'Inside helper noBattler/noPokemon/noaccessibleMega/alreadyMega return beforecount. Normal successful path writes owner-slot−2 only after transformation/UI/finalMega message.',
 'Usedslot prevents normal later qualification; explicit bare register can overwrite it because API layers are separate. Formal describes normal menu gate, not tamperproof invariant.',
 'Optional singleactorpriority recalculation follows lose/gainability callbacks. Pursuit interrupt can invoke Mega earlier at its own qualifying hook already coveredC327.'
],['attack','other','priority','command','battlerfull','pokemon_mega_full'],'postitem Mega eligibleiteration→helpercommitprefix→usedslot→abilitycallbacks→optionalpriority; no blankethelpercompletion guarantee.')
row(350,[
 'After helperearlyguards, playerowned actor increments Stats.mega_evolution_count before ownername/Illusion/message/form writes; laterfailure doesnot rollback count.',
 'Oldability cached before activeILLUSION OnBeingHit callback invoked with niluser/nilmove; callback may clear illusion before Mega feedback. Whole unrelated handlers not invoked.',
 'Pokemon.megaMessage selects targetMega record mega_message withfallback0; value1 gets ferventwish text, otherwise reacting item/ring names. Source comment Rayquaza describes data mapping, not hardcoded isSpecies gate in messagecase.',
 'Commonanimation then Pokemon.makeMega via realformsetter, Battlerform sync/pbUpdate(true), scenechange/refresh/secondanimation, name/finalmessage precede slot−2.',
 'Only then if Gengar AND actualmega? Telekinesis0, then oldabilitylosing and gainability callbacks; finalpriority optional. Exact form setters/handlers can add own earlier sideeffects.',
 'Transient Battler form/cache and permanentPokemon form are distinct writes; later faint/withdraw/ending undo is separate actual chain, not ensure around this helper. No successful Save/reload/host rendering asserted.'
],['other','battlerfull','b_change','pokemon_mega_full','abilityeffects','ability_item','config'],'earlyStats→Illusion→message→realform→battle/UI→usedslot→Gengarfield→lose/gainability→priority; each callback failure retains priorprefix.',open=['Pokemon formsetter/MultipleForms and precise Species record semantics require actual CRE finite contributions or direct complete reads; not promoted to wholeMega lifecycle here.'])
base['source_dictionary']=d;base['rows']=rows
(P/'manual_batch_07d.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print({'rows':len(rows),'children':sum(len(x['children']) for x in rows)})
