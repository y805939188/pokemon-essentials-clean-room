import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_11j.json').read_text());d=base['source_dictionary'];rows=[]
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
def head(n,s):rows.append(dict(number=n,layout_reason=s+' column heading only; the stated vectors are separately decomposed.'))
head(941,'Entry hazards')
row(942,[
 'H01 fixes a grounded indirect-damage-eligible member totalHP120 without activeBoots or other hazard immunity and Spikes layers1/2/3 as independent controls.',
 'The exact divisor lookup is[8,6,4][layers-1], producing integer nominal damage15/20/30.',
 'pbReduceHP rounds the passed amount then clips to current remainingHP, so a lower currentHP loses only that remainder.',
 'The bound individual HP setter receives the reached actual decrement; feedback and item HP-heal checks follow.',
 'Layer count is not consumed by damaging a member, and malformed/out-of-domain counts are not assumed clamped by this valid-layer vector.'
],['switching','b_change','battlerfull','item'],'valid Spikeslayer -> /8,/6,/4 ->15/20/30 -> currentHPclip/write-through -> feedback/itemheal.')
row(943,[
 'H02 fixes successful StealthRock eligibility, totalHP101 and actual Rock effectiveness factor2 with no immunity/Boots.',
 'The hazard calls ReduceHP with101*2/8=25.25 from its effectiveness multiplication, rather than an earlier integer Spikes divisor.',
 'ReduceHP rounds25.25 to25 before currentHP clipping and writes the actual loss.',
 'Thus ordinary sufficient-currentHP loss25 differs from forcing an arbitrary floor or using a Spikes-style layer table.',
 'The effect does not inherit all ordinary Move damage multipliers, and later item heal/faint handling remains in its actual entry order.'
],['switching','b_change','typefull','battlerfull','item'],'Rockeffective2 -> float25.25 -> ReduceHPround25 -> remainingHPclip -> later entry handling.')
row(944,[
 'H03 starts ToxicSpikes2 with an actual living grounded Poison member wearing activeBoots.',
 'The ToxicSpikes branch tests Poison absorption before the Boots guard used only in its nonPoison status branch, so it sets layers0.',
 'A grounded nonPoison Boots control keeps layers2 and receives no poison because the item blocks that latter branch.',
 'An airborne Poison control fails the outer grounded gate, so it neither absorbs nor receives poison and layers remain2.',
 'Boots do not generally delete hazards; this ordered Poison absorption is a specific separate operation.'
],['switching','statuses_full','battlerfull','item'],'live/grounded ToxicSpikes -> Poison clear first evenBoots; else poison eligibility+!Boots; airborne outer skip.')
row(945,[
 'H04 supplies existing StickyWeb, a live grounded member without activeBoots, Speedstage0 and ordinary CanLower eligibility.',
 'The entry helper displays web feedback then asks CanLowerSpeed and invokes LowerSpeed1 with nil user.',
 'Ordinary stage semantics give-1; activeContrary redirects actual lowering to raising, giving+1 when its real raise check permits.',
 'No source member exists for this hazard nil-user call, so target/source-specific MirrorArmor logic cannot be invented from ordinary move lowering.',
 'The side StickyWeb flag remains true after the entry effect; its use is not consumption of the hazard.',
 'Stat item checks and caps/abilities are actual later/inner gates, not a universal promise every web invocation changes a stage.'
],['switching','stages','battlerfull','abilityeffects','ability_item'],'Webgate -> message -> CanLower -> Lower1(nil) or Contraryraise1 -> item checks; sideflag stays.')
head(946,'Position effects')
row(947,[
 'P01 creates Wish from a member totalHP101 and later changes the resident at that position to a healable successor.',
 'Producer stores counter2, WishAmount=round(101/2.0)=51 and the maker party index at the source position.',
 'EOR position loop decrements2to1 then1to0 across reached rounds and recovers the current resident, not the original maker identity.',
 'Reduce/recover HP semantics clip nominal51 to current missingHP; the stored amount is not recalculated from successor totalHP.',
 'Maker is read for the later message after the counter is0 and before recovery; a naming/other error there can prevent healing without restoring the counter.',
 'Amount/maker auxiliary fields are not cleared by this ordinary Wish consumer.'
],['position_heal_producers','eor','b_change','battlefull'],'source101 -> stored51/positioncounter2/maker -> successor current at0count -> makername -> caprecover51.')
row(948,[
 'P02 has Wish decrementing to0 with no resident or a resident whose canHeal? is false.',
 'The consumer exits that position after decrement without applying HP recovery.',
 'Counter remains0, so later ordinary Wish ticks skip it rather than deferring and retrying automatically.',
 'WishAmount and WishMaker remain whatever was previously stored because this path has no auxiliary reset.',
 'A new valid Wish producer can overwrite those fields under its own counter check; retained metadata is not evidence a heal is still pending.'
],['eor','position_heal_producers','battlerfull'],'Wish1to0 -> absent/notCanHeal skip ->0/noretry/auxretained.')
row(949,[
 'P03 compares HealingWish and LunarDance position flags for a currently healthy/statusNONE entrant that is missingPP.',
 'At gen>=8 HealingWish requires canHeal OR status!=NONE, so this PP-only deficit gives no effect and retains HealingWishtrue.',
 'LunarDance also checks whether every movePP is full, so the same PP deficit admits its branch.',
 'LunarDance performs animation/message, HP recovery/cure and per-move SetPP(total), then clears its position flag on normal return.',
 'At gen<8 a benefitless HealingWish instead clears its flag in the explicit elsif without a heal.',
 'These are branch-specific position semantics and do not mean HealingWish itself restoresPP or all flags are consumed upon any entry.'
],['switching','b_change','battlerfull','b_settings'],'healthyPPdeficit -> gen8 HealingWishretain; Lunar fullPPfalse -> restore moves/clear; oldgen benefitless flagclear.')
row(950,[
 'P04 reaches FutureSight count1 but either has no living current target or later finds no able stored source.',
 'The timer decrements1to0 before either early-return check.',
 'No target returns before source construction; an off-field source not able returns without a usable source and attack.',
 'The move/source auxiliary metadata may remain because ordinary final reset statements are after the attack path.',
 'Counter0 prevents normal retry on a later occupant/source becoming able; this is not a delayed wait queue.'
],['eor','b_init','pokemon_growth_qual','battlefull'],'Future1to0 -> target/source unavailable return -> metadataretained/zero no retry.')
row(951,[
 'P05 has Wish1 stored at position0 then a legal Shift moving a different resident into0.',
 'SwapBattlers exchanges residents/indices/choices and selected relationship pointers, while the positions array and its Wish counter remain at0.',
 'Shift does not call EffectsOnBattlerEnteringPosition, so no immediate Wish or HealingWish recovery is implied by that move.',
 'When Wish later reaches0, the current resident0 receives the normal conditional recovery.',
 'The independent AllySwitch function, after a successful same-owner nearby swap, explicitly calls EffectsOnBattlerEnteringPosition for both endpoints.',
 'That explicit position callback can immediately consume a benefiting HealingWish there; it does not also imply entry hazards or full ordinary switch-in callbacks.'
],['swap','use','misc_full','switching','eor'],'slotboundWish stays0/Shift no positioncallback -> latercurrent beneficiary; AllySwitch explicit two positioncallbacks separate.')
row(952,[
 'P06 retains R10 sourceA off-field/able, savedsourceindex0/current replacementB0 and a live targetT with the exact five relation pointers0, LockOn2/position0, Trapping3/source0 and saved trapping-move identity; liveC points elsewhere.',
 'After decrement to0 and passing current target/source availability gates, new Battler(saved0) runs full InitEffects before copyingA dummy data.',
 'The current living allBattlers cross-loops set T Attract/JawLock/MeanLook/Octolock/SkyDrop matching0 to-1.',
 'The positive LockOn2 and matching position0 cause both LockOn0 and LockOnPos-1.',
 'Matching TrappingUser0 sets Trapping0/TrappingUser-1 but does not clear that other T TrappingMove field.',
 'C pointers to another saved index are unchanged by these matching checks; fainted objects outside allBattlers are excluded.',
 'B being physically present at0 does not preserve T just-established index-based relationships when the new off-field source uses that same saved index.',
 'Later delayed attack miss/ineffectiveness does not undo those clears; A-still-on-field control avoids constructing the extra Battler and therefore avoids this extra cross-clear.'
],['eor','b_init','battlefull','battlerfull','use'],'saved0 newBattler InitEffects -> live matching fiveptr/positiveLockOn/trapping clears -> dummyA -> attack; unrelated pointers/onfield control preserved.')
row(953,[
 'P07 independently makes the current target unavailable or the off-field sourceA not able while count1 phase is actually reached.',
 'Each early-return case leaves count0 and may retain move/source metadata but does not construct the dummy, so the constructor cross-clears from P06 do not occur.',
 'The independent T LockOn0/oldposition0 control skips the LockOn cross-loop at its first counter==0 guard, retaining that old position number.',
 'On an executable normal delayed-attack completion, caller restores futureSight=false and the source original lastMoveFailed, then formal target fainting as needed and resets count/move/source auxiliaries.',
 'A later error can prevent those restorations/clears; counter0 by itself does not prove all auxiliaries were reset or every temporary state restored.'
],['eor','b_init','use','b_change'],'early availability failure -> no constructor/auxretained; LockOn0 skips oldposclear; normal completion explicit restores/reset only.')
head(954,'Clear-field')
row(955,[
 'C01 supplies gen8 Defog against a target already Evasion-6 but with an explicitly removable wall/hazard or nonNone terrain.',
 'The specialized failure predicate returnsfalse for named removable effects before delegating to the stat-lowering parent, so inability to lower Evasion alone does not fail the whole move.',
 'The effect separately asks CanLowerEvasion and may skip the stage change while still clearing its exact named target-side five protections.',
 'It clears the four named hazards on target side and, gen>=6, the opposite side; values are set0/false according to their actual representations.',
 'Gen>=8 current terrain is directly setNone with its feedback, retaining duration/default and omitting the natural restoration notification chain.',
 'Tailwind and LuckyChant are outside the named clear set and remain; no generic all-side/all-field wipe is inferred.',
 'Earlier target/accuracy/other common gates and subsequent callback failure retain their normal conditions and reached-prefix semantics.'
],['defog_complete','targetstatdown_parent','stages','eor','weather_core_complete','switching'],'removable effect admitsDefog despite minEvasion -> optional stage -> exact5protections/4hazards -> directterrainNone; excluded counters stay.')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_11k.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows),'layout',sum('layout_reason'in x for x in rows))
