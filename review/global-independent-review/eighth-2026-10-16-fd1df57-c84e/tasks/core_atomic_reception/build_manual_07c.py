import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_07b.json').read_text());d=base['source_dictionary'];rows=[]
d['playerfull']={'path':'Data/Scripts/015_Trainers and player/004_Player.rb','range':[1,123],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ'}
d['pokemon_hyper']={'path':'Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb','range':[104,106],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE_COMPLETE_GETTER_READ; heart_gauge callee remains separately bounded'}
d['foreign_method']={'path':'Data/Scripts/014_Pokemon/001_Pokemon.rb','range':[847,849],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE_COMPLETE_METHOD_READ'}
d['maxlevel_method']={'path':'Data/Scripts/010_Data/001_Hardcoded data/001_GrowthRate.rb','range':[23,25],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE_COMPLETE_METHOD_READ'}
d['maxlevel_constant']={'path':'Data/Scripts/001_Settings.rb','range':[127,133],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE_CONSTANT_AND_CONTEXT_READ; MAXIMUM_LEVEL100, not wholeSettings'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(327,[
 'Pursuit pre-switch hook sets battle.switching=true before priority iteration; only living opposing and notmoved registered PursueSwitchingFoe actors remain.',
 'Each candidate must satisfy actual current move-target eligibility against switcher and pbCanChooseMove?(index,registeredMoveIndex,false); mere known Pursuit is insufficient.',
 'Sleeping/Frozen, SkyDrop>=0 and activeTRUANT with Truantflagtrue are excluded before Mega and targetwrite. This is TRUANT loafing gate, distinct existingCOM001 STALL naming root.',
 'For nonwild qualifying actor, its owner/side registration equal actorindex invokes Mega before Pursuit; wild actor skips this Mega call.',
 'Then registered targetslot is replaced by switchingindex and pbProcessTurn(choice,false) performs whole ordinary action, including its own later qualification/PP checks.',
 'After normal processreturn, decision>0 OR current switcherfainted breaks; otherwise next qualifying actor may interrupt. Normal tail resets switching=false, no ensure guarantees that reset after callback exception.'
],['attack','priority','checksfull','use','orderproducers','battlefull','other'],'switching marker→ordered actor/target/choice/status gates→conditionalMega→targetrewrite→ordinaryaction→decision/faintbreak→normalmarkerreset.',open=['Full concrete Mega/Pursuit move-effect and target callbacks beyond current actual source/received finite facts remain named OPEN; this is battle interrupt contract, not all Move domain.'])
row(328,[
 'Obedience immediately returns true for usingMultiTurnAttack before checking action/internal/ownership.',
 'NonUseMove then noninternalBattle then !pbOwnedByPlayer? each return true; passing requires all four restrictions, even if Pokemon is foreign or hyper.',
 'Actual owner predicate is Battle player-owned slot logic, not merely supplied Trainer object equality or AI control flag.',
 'Ordinary TryUse reaches obedience after earlier action/status gates; false from obedience refuses before ordinary PP deduction and normal caller cancels/EndTurn. A true result can mean original or substituted move.'
],['checksfull','battlerfull','battlefull','use'],'execution eligibility→four obedience bypasses→check result→PP boundary/actioncompletion; no inferred check on every selected command.')
row(329,[
 'L initially10*(battle.pbPlayer.badge_count+1); actual badge_count counts entries ==true, rather than all truthy badge-array entries.',
 'A fresh player has eightfalse badge entries; with no badge L10. At count>=8 method replaces L with GameData::GrowthRate.max_level, not arithmetic90.',
 'GrowthRate.max_level reads Settings.MAXIMUM_LEVEL, current fixed constant100. For legal levels at most100, level>L is false at eightbadges; hyper-mode check remains separately eligible.',
 'No persistence proof follows from runtime badge_count; real loaded Player identity and finite Kernel top-level class assignment facts do not validate every nested badge or ownership field.'
],['checksfull','playerfull','maxlevel_method','maxlevel_constant'],'current Player.badges exacttruecount→L→level comparison; maxlevel gate excludes highlevel branch only.')
row(330,[
 'Fixed full BattleSettings explicitly ANY_HIGH_LEVEL=false and FOREIGN_HIGH_LEVEL=true; these two assignments are independent of MECHANICS_GENERATION.',
 'Highlevel branch qualification is ANY OR(FOREIGN AND realPokemon.foreign?(battle.pbPlayer)); ANYtrue shortcircuits the foreign call.',
 'foreign? compares realPokemon owner.id OR owner.name difference to trainer; matching id with differentname is foreign, matching both is not. Method has no niltrainer guard despite permissive annotation.',
 'Only qualified level>L draws battle.pbRandom(256), computes floor((level+L)*draw/256), and ORs a>=L into disobedient.',
 'The draw is an integer0..255 from Battle.pbRandom under normal valid bound; threshold equality counts disobedient. No sampling frequency/seed execution asserted.',
 'A prior highlevel refusal does not suppress the subsequent hyper check: boolean |= evaluates the right-hand call and combines it.'
],['checksfull','b_settings','foreign_method','battlefull'],'independent constants→Ownercomparison→level gate→battle random threshold→boolean aggregation; no language/gender comparison implied.')
row(331,[
 'Shadow extension supplies pbHyperModeObedience and returns true when not actually inHyperMode?.',
 'When inHyperMode?, nilmove OR move.type==SHADOW returns true without draw; otherwise global rand(100)<20 returns obedience.',
 'This Shadow predicate uses current move.type and global rand, not calculated move.calcType or battle.pbRandom; 20 is strict cutoff, draw20 refuses.',
 'Battler inHyperMode? rejects fainted then delegates Pokemon.hyper_mode; that getter returns false when heart_gauge==0 OR realHP==0, otherwise rawhyper flag. Ordinary pbHyperMode producer requires Shadow/playerowned/living/notalreadyhyper before setting flag; no fabricated rawflag equivalence or automatic global rate proof.'
],['checksfull','shadowother','battlerfull','b_change','pokemon_hyper'],'Shadow state predicate→nil/rawShadow exemption→globalrand threshold→negated refusal contribution.')
row(332,[
 'Highlevel and !pbHyperModeObedience are accumulated; either true selects pbDisobey, neithertrue returns true without disobedience handling.',
 'pbDisobey starts debuglog then clears Rage before any sleep/alternate/selfharm/refusal branch. If logging raises, that later clear need not happen.',
 'Return true from pbDisobey means substituted move continues, not original order obeyed. False is actionrefusal with no uniform lastMoveFailed=true write here.'
],['checksfull','use','debuglog'],'both refusalproducers→one handler→early Rageclear→branchresult; preserve boolean success versus literal obedience.')
row(333,[
 'In disobey handler, current statusSLEEP AND actual chosenmove.usableWhenAsleep? displays keptsleeping and returns false before b/random alternatemove search.',
 'Snore/SleepTalk illustrate actual predicate; not every sleeping disobedient Pokemon enters this branch, because earlier TryUse/status/predicate gates matter.',
 'Refusal is before ordinary PP deduction; ordinary caller then CancelMoves/EndTurn may mutate counters/Choice/continual checks. No rollback or no-state-change inference.'
],['checksfull','use','usagefull'],'reached disobey→sleepusable check→message/refusal→normal actioncancel/end; ordinaryPP untouched by this branch.')
row(334,[
 'If earlier keptsleeping did not return, b=floor((level+L)*battleRandom256/256); b<L first displays ignoredorders.',
 'Then !pbCanShowFightMenu? refuses, so no alternative collection; menu eligibility here is a method predicate, not actual requirement to render player UI.',
 'Alternatives exclude original choiceindex and require pbCanChooseMove?(actor,index,false). Empty alternatives returnsfalse after ignoredorders message.',
 'Nonempty alternatives uses battleRandom(length), writes choice[1]=newindex then choice[2]=actual @moves[newindex] then targetchoice[3]=−1 and returns true.',
 'Ordinary caller rereads move from mutatedchoice before PP; chosen newmove must pass its actual reducer. NoPP newmove refuses without deducting original move PP; positivePP newmove normally deducts itself.',
 'The alternate selection does not invoke a second full obedience check within this invocation; downstream target resolution uses resettarget and actual newmove data.'
],['checksfull','use','battlefull','priority','command'],'b cutoff→message→menu/candidate legality→random newchoice sequentialwrites→newmove PP/targets; callback exceptions retain earlier prefix.',open=['Actual specific alternative move callbacks beyond current read classes remain OPEN; AI whole selection producer is not needed to assert this player-owned execution branch.'])
row(335,[
 'When b>=L, c=level−L and r=battleRandom256. First r<c AND pbCanSleep?(self,false) invokes selfsleep and returnsfalse.',
 'If sleep condition does not take branch, code subtracts c from the same r, then r<c AND currentstatus!=SLEEP invokes confusiondamage andfalse; this is not a second independent draw.',
 'Selfsleep feasibility can fail despite r<c and then selfharm may still qualify. Existing sleeping status prevents selfharm even if its numeric cutoff matches.',
 'If neither branch returns, one battleRandom4 chooses exactly one of four refusal messages, thenfalse. Text turningaway is feedback, not a direction-field write.',
 'Selfdamage/sleep writer may commit before later display/item/faint callbacks; this handler does not globally assign lastMoveFailedtrue for every disobedience. Normal caller completion remains separately reached.'
],['checksfull','use','b_change','battlerfull','ability_item'],'same-r sequential thresholds→actual sleep feasibility→confusion writer orfourmessage refusal; PPnotyetordinarydeducted.')
row(336,[
 'Base command loop delegates nonplayer or controlPlayer routes to AI command chooser, while obedience is later in actual Battler TryUse path restricted by playerownership/internal/action/multiturn.',
 'AI control of a playerowned actor does not by itself bypass that later owner predicate. AI legality and literal obedience are distinct stage contracts.',
 'Highlevel/disobey draws use Battle.pbRandom; Shadow hyper predicate explicitly uses globalrand. This formal separation does not promise independent streams for all AI or callback randomness.',
 'All AI producers, score/filter branches and specific override paths have not yet been fully received in this current semantic pass; the assertion that AI only produces legalchoices remains a precise dependency OPEN rather than inferred from delegation.'
],['command','checksfull','shadowother','use','battlefull'],'command delegation versus later executor restriction→distinct documenteddraw calls.',support='OPEN_EXACT_FOREIGN_RECEIVER',open=['Complete original AI producer/filter facts and necessary actual caller/receiver closures for AI only-legal selection remain OPEN; large AI payload available but not yet semantically received.'])
base['source_dictionary']=d;base['rows']=rows
(P/'manual_batch_07c.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print({'rows':len(rows),'children':sum(len(x['children']) for x in rows)})
