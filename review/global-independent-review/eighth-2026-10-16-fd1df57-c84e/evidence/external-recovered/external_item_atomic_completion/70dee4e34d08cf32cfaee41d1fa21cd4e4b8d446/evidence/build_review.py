"""Package manually authored semantic judgments; static enumeration is bookkeeping.

Never execute or translate reference behavior. The lists below are the reviewer's
behavioral assertions, rather than token/statement/semicolon-based atoms.
"""
from pathlib import Path
import collections, datetime, gzip, hashlib, json, re, subprocess

ROOT=Path('/workspace/pokemon-essentials-clean-room')
REF=Path('/workspace/pokemon-essentials')
REPORT='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
OUT=ROOT/REPORT/'tasks/external_item_atomic_completion'
CONTRACT='40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232'
B8='fd1df570cad987dc3852a3b958f03916e317f7fe'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
PRIMARY='Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb'
MAIN='deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md'
COVER='deliverables/final-specification-set/pokemon-rules/wp50-held-item-effect-coverage.md'
CAT1='deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md'
CAT2='deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md'
HELPER='Data/Scripts/011_Battle/002_Battler/006_Battler_AbilityAndItem.rb'
BATTLER='Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb'
STAGE='Data/Scripts/011_Battle/002_Battler/005_Battler_StatStages.rb'
TRIGGER='Data/Scripts/011_Battle/002_Battler/010_Battler_UseMoveTriggerEffects.rb'
CALC='Data/Scripts/011_Battle/003_Move/003_Move_UsageCalculations.rb'
def dump(name,x):
    (OUT/name).parent.mkdir(parents=True,exist_ok=True)
    (OUT/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def git(repo,*args,input=None):return subprocess.check_output(['git','-C',str(repo),*args],input=input).decode().strip()
def ident(repo,path,commit):
    raw=(repo/path).read_bytes()
    return dict(repo=str(repo),commit=commit,tree=git(repo,'rev-parse',commit+'^{tree}'),path=path,mode=git(repo,'ls-tree',commit,'--',path).split()[0],bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),blob=git(repo,'hash-object','--stdin',input=raw),lines=len(raw.decode('utf-8-sig').splitlines()))
spec_lines=(ROOT/MAIN).read_text().splitlines()
atoms=[]; groups=[]; units=[]
def group(gid,path,ranges,lines,rules,normal,boundary,consumers,disposition='SUPPORTED_SOURCE_STATIC'):
    aid=[]
    for i,rule in enumerate(rules,1):
        a=f'{gid}-A{i:02d}';aid.append(a)
        atoms.append(dict(id=a,meaning=rule,source=dict(path=path,ranges=ranges),operative=[dict(path=MAIN,line=n,text=spec_lines[n-1]) for n in lines],premises=['EIA-P01','EIA-P02','EIA-P03'],consumers=consumers,judgment=disposition,execution='NOT_EXECUTED'))
    groups.append(dict(id=gid,assertions=aid,ordinary_control=normal,minimal_branch_or_boundary=boundary,cancellation='No local menu cancellation in this definition; upstream non-entry does not create writes. Interactive replacement exceptions are stated per handler.',failure_prefix='Preserve only writes already reached. Calls/feedback/data errors propagate from this unit; no inferred rollback or host recovery.',consumers=consumers))
    return aid

# Manually decomposed common premises, helper contracts and consumer joins.
group('G-ACTIVE',BATTLER,[[344,357],[421,435]],[11],[
 'Ordinary active-item queries reject fainted holders; the explicit ignore-fainted argument removes this one guard.',
 'A positive Embargo counter disables held effects.', 'A positive Magic Room counter disables held effects.',
 'Corrosive Gas reads the current side and party index, rather than the field seat alone.',
 'Active Klutz disables items, using the same ignore-fainted argument for its ability test.',
 'Ability activity independently rejects Gastro Acid and applicable Neutralizing Gas; allowing a fainted item does not activate ordinary Ripen.',
 'An active-item predicate does not itself require a current item identity; the subsequent identity/registry query decides whether an effect exists.'
], 'Live, registered item, all suppressors absent.', 'Independently change fainted/Embargo/MagicRoom/corrosion/Klutz; allow-fainted affects only its own guard.', ['I-CORE','I-DATA'])
group('G-REGISTRY','Data/Scripts/003_Game processing/005_Event_Handlers.rb',[[148,197],[294,295]],[169],[
 'Lookup converts an object exposing an identity to that identity, but does not automatically normalize arbitrary strings into symbols.',
 'An exact stored handler takes precedence over conditional handlers.',
 'With no exact handler the first matching conditional registration supplies the handler.',
 'Same-key registration replaces the current handler after handler-shape validation.',
 'Copy resolves its source at copy time and stores the same resolved handler for each destination.',
 'A missing copy source adds nothing; a later source replacement does not dynamically retarget old destinations.',
 'Only the named family is copied, rather than every effect associated with an item.',
 'A trigger forwards the normalized key as its first argument and preserves the callback return.',
 'No handler yields nil; invalid handler shape is rejected before registration.',
 'Single removal deletes an exact key; clearing removes exact and conditional groups.'
], 'Exact registered symbol reaches its handler.', 'Exact/condition collision, missing copy source, later replacement, nil identity and invalid handler all remain distinct.', ['I-KERNEL'], 'SUPPORTED_FINITE_KERNEL_CONTRACT')
group('G-PINCH',HELPER,[[212,222]],[74],[
 'Opposing active Unnerve or either As One variant rejects ordinary berry permission.',
 'Pinch qualification always checks berry permission before HP thresholds.',
 'HP at or below floor(H/4) qualifies in either pinch mode.',
 'Between floor(H/4) and floor(H/2), mode false requires no Gluttony.',
 'The same interval in the default mode requires active Gluttony.',
 'Neither mode permits ordinary triggering above floor(H/2).'
], 'H100 h25 passes either mode without Gluttony.', 'H100 h50 versus51; mode false versus true; independently add Unnerve.', ['I-CORE'])
group('G-CONSUME',HELPER,[[224,286]],[29,31],[
 'A recoverable consumption first records the current identity as the recycle item.',
 'It then records the current pickup item and obtains a new monotonically increasing pickup-use sequence.',
 'Eligible berry consumption sets the party-linked Belch record before removal.',
 'Removal clears Choice lock unless Gorilla Tactics is currently active.',
 'Removal sets Unburden only when a held item exists and Unburden is currently active.',
 'Permanent removal clears the current restoration record only when it equals the removed current item.',
 'Clearing the battle current item writes through to the associated persistent creature.',
 'The optional Symbiosis phase occurs after removal, not before the consumption records.',
 'Nonrecoverable consumption leaves prior recycle/pickup records intact rather than erasing them.',
 'The generic triggered suffix checks active Cheek Pouch, berry identity and canHeal before requesting floor(H/3).',
 'Cheek Pouch healing and its feedback precede the own-item consumption phase.',
 'A foreign explicit item does not clear the receiver current item; non-Fling foreign use can request Symbiosis.',
 'Symbiosis requires the receiver alive and empty, then chooses the first eligible same-side active donor in cached speed order.',
 'The donor must have an item losable by both donor and receiver.',
 'Symbiosis transfers current possession, clears the donor, may set donor Unburden and rechecks the recipient held item.',
 'Symbiosis does not transfer the restoration record as a general operation.',
 'No once-per-round latch prevents a newly received item from triggering recursively.'
], 'Own ORAN C=I, old recycle empty, no donor: records then removal.', 'Foreign berry/Fling, nonrecoverable AIRBALLOON, unequal I, no donor and eligible donor are independent branches.', ['I-CORE','I-DATA'])
group('G-ENTRY',HELPER,[[297,394]],[21,26,29],[
 'The complete held-item check rejects a fainted receiver even with an explicit forced identity.',
 'Ordinary complete entry also requires item activity; explicit forced identity bypasses this ordinary item gate.',
 'The full entry orders HP, status, end-of-move checks, then forced positive-hit berry handling.',
 'The direct HP helper has no preliminary faint guard, unlike direct status/end-of-move helpers.',
 'Only a successful HP callback reaches the generic triggered suffix.',
 'An unsuccessful ordinary HP callback falls through to terrain-seed checking; forced HP failure does not.',
 'End-of-move checks try Leppa first and White Herb only if the first callback was unsuccessful.',
 'Terrain and Intimidate helpers consume only after the respective callback returns true.',
 'Stat-loss entry requires the dropped flag and item activity before calling Eject Pack.',
 'Ending Unnerve can ask every cached-speed berry holder to recheck current eligibility.'
], 'Ordinary ORAN success and LEPPA empty PP.', 'Explicit forced vs normal, fainted direct HP vs complete entry, HP callback false triggering a seed.', ['I-CORE'])
group('G-CONFUSION',HELPER,[[399,432]],[80],[
 'Nonforced confusion berries require canHeal before pinch qualification.',
 'Generation 6 or earlier passes pinch mode false; generation 7 or later passes true.',
 'Generation 6 or earlier requests floor(H/8).',
 'Generation 7 requests floor(H/2).', 'Generation 8 or later requests floor(H/3).',
 'Active Ripen doubles the already integer-divided request.',
 'The ordinary eating animation is requested only for nonforced use.',
 'The central recovery operation runs before the nature check.',
 'A recovery message is requested only when the central recovery reports a positive amount.',
 'Dislike tests the actual nature stat changes, rather than a mint-adjusted nature used solely for stat calculation.',
 'A negative change for the berry-specific stat requests the taste feedback.',
 'Self-confusion is committed only when the separate self-confusion eligibility query permits it.',
 'Forced use skips both canHeal and pinch gates, and can return true after zero healing at full HP.',
 'When all reached operations return normally, this helper returns true even if confusion was ineligible.'
], 'Gen8 H100 h25, Figy and a nature lowering Attack: request33 then eligible confusion.', 'Gen6/7/8; H101; Gluttony; forced full HP; Own Tempo; mint-only nature alteration; HealBlock.', ['I-CORE','I-DATA'])
group('G-STATBERRY',HELPER,[[434,449]],[81,82],[
 'Nonforced stat berries require default pinch permission.',
 'Forced use bypasses pinch but still requires the central stat-increase query.',
 'Ripen doubles the requested increment before central stage transformations and clamping.',
 'Ordinary use requests cause-specific stage feedback; forced use requests the ordinary stage commit.',
 'The returned success is the central commit result; false does not reach generic consumption.'
], 'Stage0, ordinary legal pinch, request1.', 'Stage cap, Contrary, Simple, forced high HP, Ripen and truncated positive delta.', ['I-CORE'])
group('G-RESIST',HELPER,[[451,464]],[70],[
 'The registered berry type must match this move calculation type.',
 'A non-Normal match additionally requires super-effective current typeMod.',
 'A qualifying berry halves the final-damage multiplier.',
 'It records berryWeakened immediately, before animation and later item consumption.',
 'Active Ripen halves the multiplier a second time.',
 'This helper does not query ordinary eating permission or Unnerve.',
 'The animation occurs during calculation; actual removal belongs to the later per-hit consumer.'
], 'Matching super-effective Fire with OCCA and neutral multiplier.', 'Nonmatch, neutral Fire, Normal CHILAN neutral, Ripen and Unnerve independently.', ['I-MOVE','I-CORE'])
group('G-GEM',HELPER,[[466,475]],[66],[
 'Every PledgeMove subclass is excluded from the gem helper.',
 'A gem must match this move calculation type.',
 'Qualification records the current held identity as GemConsumed before applying its multiplier.',
 'Generation 6 or later multiplies power by1.3; earlier generations by1.5.',
 'The query does not remove the held item.',
 'The first-hit consumer requests gem feedback after move animation; the after-move consumer removes the then-current item.',
 'Intervening item changes and failures preserve already reached marker and multiplier writes.'
], 'Gen8 matching FIREGEM, ordinary nonpledge move.', 'Gen5; wrong type; pledge; multiple hits before removal; abort between marker/feedback/removal.', ['I-MOVE','I-CORE'])
group('G-HP','Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb',[[5,35],[54,62]],[9,31,88,92,119,123,131,144,145],[
 'Central HP requests round before clamping to current HP or missing HP.',
 'A sub-one heal request becomes one only while below maximum HP; a full-HP direct recovery can report zero.',
 'Recovery itself does not query canHeal or HealBlock.',
 'The HP write precedes bounds validation and scene feedback.',
 'Recovery reaching floor(H/2) clears the cross-half flag only after reached feedback.',
 'The effect-damage helper orders damage, its supplied feedback, immediate HP-item check, damage-triggered ability and fainting.',
 'Only completed prefixes survive; failure before a later flag write does not imply that flag was set or cleared.'
], 'H15 h14 Leftovers request0 centrally heals1.', 'Full HP forced confusion fruit, HealBlock direct recovery, and failure after HP assignment before feedback returns.', ['I-CORE'])
group('G-STAGE',STAGE,[[5,99],[119,237]],[81,88,104,107,111,140,142,143],[
 'Stage qualification rejects fainted receivers.',
 'Ordinary qualification can redirect through Contrary unless ignored or Mold Breaker applies.',
 'Central commits apply Simple to the request before limiting to remaining stage capacity.',
 'A nonpositive actual delta reports false without stage feedback.',
 'A positive delta writes stages and the appropriate raised/lowered/dropped flags before feedback and ability notifications.',
 'Multi-stat callers may commit one eligible stat while another is capped; there is no group rollback.',
 'White Herb direct assignment does not inherit the central Contrary/Simple transformations.'
], 'Neutral stage request1 commits1.', 'Stage+5 request2 commits1; cap reports false; Simple/Contrary independently; White Herb keeps positive stages.', ['I-CORE'])
group('G-MOVE-HIT',TRIGGER,[[5,82],[87,217]],[22,23,24,100,105,107,117,119,128,129,130,131],[
 'Per-hit target items require positive calcDamage and no substitute.',
 'The target item activity query explicitly permits fainted holders.',
 'Target ability, Gulp Missile and user hit-ability reactions precede the target-item read.',
 'If the target-item reaction lowers user HP, user HP items are checked immediately before the next hit.',
 'After-move target items use the original target set, affected flag, positive calcDamage and ordinary active-item gate.',
 'Target items are processed in cached speed order.',
 'The user item runs only when the user has not been switched out and its current item is active.',
 'Active user Sheer Force plus positive additional-effect data suppresses the named after-move second and third stages.',
 'The Sheer Force gate does not suppress the separate per-hit positive berry callbacks.',
 'The remaining after-move chain, including each reached item check, is not an atomic transaction.'
], 'Ordinary hit, both alive, positive damage, no substitute or suppressor.', 'Fainted target Helmet, substitute, earlier transfer, Sheer Force with positive/zero addlEffect, user already switched.', ['I-MOVE','I-CORE'])
group('G-PRIORITY','Data/Scripts/011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb',[[136,279]],[48,49,50],[
 'Full initial ordering computes item brackets only for UseMove or Shift choices.',
 'Item bracket calculation follows the ability bracket calculation.',
 'A fast item bracket can override a slow ability bracket.',
 'Partial recalculation updates speed and move priority without redrawing the item bracket.',
 'The attack-phase notice rechecks the saved responsible source and current item activity before dispatch.',
 'The cached speed-only order does not itself recalculate speed or apply Trick Room reversal.'
], 'QUICKCLAW r19 gives+1.', 'r20 gives0; partial recalculation; disable item after ordering; ability bracket wins.', ['I-CORE'])
group('G-REWARD','Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb',[[59,224]],[27,150,151],[
 'Experience checks the persistent current item first and consults the restoration record only when the result is negative.',
 'An EV registry hit reports handled regardless of the callback return; no hit alone permits restoration-record fallback.',
 'Field item suppression is not checked in either reward modifier path.',
 'EV item changes precede Pokerus multiplication and per-stat/total limits.',
 'The experience item receives the already split/scaled/outsider/charm-adjusted amount, before affection and growth limits.',
 'Current and restoration-record modifiers do not stack on this path.'
], 'LuckyEgg input101 gives151; power Speed yield1 plus8 then virus gives18.', 'Unknown current with valid I; same C/I; MagicRoom or fainted field holder.', ['I-CORE','I-DATA'])
group('G-FIELD','Data/Scripts/011_Battle/001_Battle/001_Battle.rb',[[707,733],[786,811]],[138,139,140],[
 'A same stored weather or terrain request exits without refreshing its duration.',
 'Weather extension is queried only for a positive finite duration, a source and an active current item.',
 'Terrain extension uses the same finite-source activity conditions.',
 'Indefinite weather or terrain is not converted to eight by these ordinary extenders.',
 'Terrain change notifies all abilities before notifying all item holders.',
 'Field identity assignment precedes the duration query and later feedback, so a later failure need not roll it back.'
], 'Finite Rain with DampRock becomes8.', 'Indefinite weather, no source, wrong rock, same terrain and floating seed holder.', ['I-CORE'])
group('G-EOR','Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb',[[436,505],[597,781]],[25,144,145,146,147],[
 'The round-end phase recalculates speed once before obtaining its cached speed order.',
 'Within each member healing sequence, terrain healing precedes ability healing and item healing.',
 'The later member sequence orders self timers, ability effects, item effects and item-acquiring abilities.',
 'Each item step rechecks current activity rather than relying on one phase-wide snapshot.',
 'A positive battle decision is checked only at explicit phase checkpoints, not after every callback.',
 'MagicRoom expiry requests item checks in cached speed order without an additional autonomous speed recalculation.'
], 'Live Leftovers holder reaches healing phase.', 'Earlier phase changes HP/item/activity; decision written inside callback; MagicRoom expires.', ['I-CORE'])

# Exact direct handler meanings, independently derived from the complete file.
rules={}
def put(f,item,line,*meanings,shared=()):rules[(f,item)]=(line,list(meanings),list(shared))
put('SpeedCalc','CHOICESCARF',39,'Multiply incoming speed multiplier by1.5.')
for item in ['IRONBALL','MACHOBRACE']:put('SpeedCalc',item,40,'Divide incoming speed multiplier by2.')
put('SpeedCalc','QUICKPOWDER',41,'Require the underlying creature to be Ditto.','Require it not currently transformed.','Multiply speed multiplier by2 only when both conditions hold.')
put('WeightCalc','FLOATSTONE',42,'Use integer half of the incoming weight in0.1kg.','Clamp this item result to at least1.')
confusion={'AGUAVBERRY':'SPECIAL_DEFENSE','FIGYBERRY':'ATTACK','IAPAPABERRY':'DEFENSE','MAGOBERRY':'SPEED','WIKIBERRY':'SPECIAL_ATTACK'}
for item,stat in confusion.items():put('HPHeal',item,80,f'This berry selects the actual nature lowering {stat} as its disliked taste.',shared=['G-CONFUSION','G-PINCH','G-CONSUME','G-HP'])
statberries={'APICOTBERRY':'SPECIAL_DEFENSE','GANLONBERRY':'DEFENSE','LIECHIBERRY':'ATTACK','PETAYABERRY':'SPECIAL_ATTACK','SALACBERRY':'SPEED'}
for item,stat in statberries.items():put('HPHeal',item,81,f'Request an increase of1 in {stat} through the stat-berry helper.',shared=['G-STATBERRY','G-PINCH','G-STAGE','G-CONSUME'])
put('HPHeal','BERRYJUICE',78,'Require canHeal even when forced.','Require HP no greater than floor(H/2) unless forced.','Request20 HP without a Ripen branch in this handler.','A normally returned recovery and feedback reports true.',shared=['G-HP','G-CONSUME'])
for item,amount in [('ORANBERRY','10'),('SITRUSBERRY','floor(H/4)')]:put('HPHeal',item,79,'Require canHeal even when forced.','Nonforced use requires pinch mode false.',f'The base healing request is {amount}.','Active Ripen doubles the already evaluated integer request.','Forced use omits the ordinary eating animation.','After central recovery and feedback the handler returns true.',shared=['G-PINCH','G-CONSUME','G-HP'])
put('HPHeal','LANSATBERRY',83,'Nonforced use requires default pinch qualification.','Existing FocusEnergy at least2 rejects.','Set FocusEnergy directly to2 rather than adding2.','This direct write is not doubled by Ripen.','Write the marker before the success feedback and true return.',shared=['G-PINCH','G-CONSUME'])
put('HPHeal','MICLEBERRY',84,'Nonforced use requires default pinch qualification.','A false existing MicleBerry marker rejects.','An existing true marker remains true, then feedback and true return permit consumption.','The later ordinary accuracy modifier consumes the stored marker, multiplying accuracy by1.2.',shared=['G-PINCH','G-CONSUME'])
put('HPHeal','STARFBERRY',82,'Build the five-main-battle-stat pool using central eligibility.','An empty legal pool returns false without drawing.','Uniformly choose one legal entry before the pinch helper can reject.','Request2 for the selected stat; Ripen changes that request to4.',shared=['G-STATBERRY','G-STAGE','G-CONSUME'])
for item,status in {'ASPEARBERRY':'FROZEN','CHERIBERRY':'PARALYSIS','CHESTOBERRY':'SLEEP','PECHABERRY':'POISON','RAWSTBERRY':'BURN'}.items():put('StatusCure',item,86,'Nonforced use requires berry permission.',f'Require raw status {status}, rather than a viewed or assumed status.','Cure status through its state writer before any later success feedback.','Forced mode changes feedback routing and bypasses eating permission, but does not bypass the status match.','Return true only after the reached cure/feedback completes.',shared=['G-PINCH','G-CONSUME'])
put('StatusCure','PERSIMBERRY',86,'Nonforced use requires berry permission.','Require nonzero confusion count.','Clear confusion before the ordinary or forced feedback.','Report true after the reached feedback completes.',shared=['G-CONSUME'])
put('StatusCure','LUMBERRY',86,'Nonforced use requires berry permission.','Reject only when raw status is NONE and confusion count is0.','Save the old status/confusion before clearing both.','Cure status before clearing confusion, so an intervening failure can leave only the status cured.','Choose feedback from the saved values and forced mode.','Report true only after reached feedback.',shared=['G-CONSUME'])
put('StatusCure','MENTALHERB',88,'Require at least one of Attract, Taunt, Encore, Torment, Disable or HealBlock.','This nonberry handler has no eating-permission guard.','Cure Attract when present.','Clear Taunt count.','Clear Encore count and its move identity.','Clear Torment.','Clear Disable count while retaining DisableMove.','Clear HealBlock count.','The ordered individual clears and intervening feedback can leave partial prefixes.','Report true after all reached operations; generic consumption follows.',shared=['G-CONSUME'])
put('OnStatLoss','EJECTPACK',127,'Reject a SkyDrop target or the matching carrying two-turn attack.','Reject when the opposing team has all fainted.','Reject a wild holder.','Require full canSwitchOut qualification.','Require an available nonactive replacement.','Request animation/feedback before consumption.','Consume recoverably with Symbiosis disabled before selecting a replacement.','At round end recall if alive, invoke switch-out effects and return true without selecting now.','Outside round end a negative selection returns false while retaining consumption.','A valid selection replaces the holder and clears its choice.','Clear MoldBreaker when the holder is the move user, then process entry and return true.',shared=['G-CONSUME','G-ENTRY'])
put('PriorityBracketChange','CUSTAPBERRY',48,'Default pinch qualification yields bracket+1.','This query does not consume the berry.',shared=['G-PINCH','G-PRIORITY'])
put('PriorityBracketChange','LAGGINGTAIL',49,'Return bracket-1.',shared=['G-PRIORITY'])
put('PriorityBracketChange','QUICKCLAW',50,'Draw an integer in0..99.','Return+1 only for a value below20; nil otherwise becomes the wrapper fallback0.',shared=['G-PRIORITY'])
put('PriorityBracketUse','CUSTAPBERRY',48,'After the eating animation and priority feedback, consume directly.','Direct consumption does not enter the generic Cheek Pouch suffix.',shared=['G-CONSUME','G-PRIORITY'])
put('PriorityBracketUse','QUICKCLAW',50,'Request the use animation and priority feedback.','This notification does not consume.',shared=['G-PRIORITY'])
put('OnMissingTarget','BLUNDERPOLICY',51,'Reject a hit index greater than0.','Reject the target invulnerable miss flag.','Reject OHKO, OHKOIce and OHKOHitsUndergroundTarget effect codes.','Require central Speed-increase eligibility.','Request Speed+2 before the used-up feedback.','Then invoke the generic triggered suffix.',shared=['G-STAGE','G-CONSUME'])
put('AccuracyCalcFromUser','WIDELENS',43,'Multiply the shared accuracy multiplier by1.1.')
put('AccuracyCalcFromUser','ZOOMLENS',44,'A target choice other than UseMove/Shift qualifies, including None.','A target already moved this round also qualifies.','Qualifying cases multiply accuracy by1.2 once.','Do not replace this with a speed comparison.')
put('AccuracyCalcFromTarget','BRIGHTPOWDER',45,'Multiply the shared user accuracy multiplier by0.9.','Do not change the target evasion stage.')
boosters={'BLACKBELT':'FIGHTING','BLACKGLASSES':'DARK','CHARCOAL':'FIRE','DRAGONFANG':'DRAGON','HARDSTONE':'ROCK','MAGNET':'ELECTRIC','METALCOAT':'STEEL','MIRACLESEED':'GRASS','MYSTICWATER':'WATER','NEVERMELTICE':'ICE','PIXIEPLATE':'FAIRY','POISONBARB':'POISON','SHARPBEAK':'FLYING','SILKSCARF':'NORMAL','SILVERPOWDER':'BUG','SOFTSAND':'GROUND','SPELLTAG':'GHOST','TWISTEDSPOON':'PSYCHIC'}
for item,typ in boosters.items():put('DamageCalcFromUser',item,59,f'Require calculation type {typ}.','Multiply the power slot by1.2; a nonmatch leaves it unchanged.')
for item,sp,types in [('ADAMANTORB','DIALGA','DRAGON/STEEL'),('GRISEOUSORB','GIRATINA','DRAGON/GHOST'),('LUSTROUSORB','PALKIA','DRAGON/WATER')]:put('DamageCalcFromUser',item,60,f'Require underlying species {sp}.',f'Require calculation type in {types}.','Multiply the power slot by1.2 when both predicates hold.')
for item,cat,factor in [('CHOICEBAND','physical','1.5'),('CHOICESPECS','special','1.5'),('MUSCLEBAND','physical','1.1'),('WISEGLASSES','special','1.1')]:put('DamageCalcFromUser',item,61,f'Require the move current {cat} classification.',f'Multiply the power slot by{factor}, rather than the attack slot.')
for typ in ['BUG','DARK','DRAGON','ELECTRIC','FAIRY','FIGHTING','FIRE','FLYING','GHOST','GRASS','GROUND','ICE','NORMAL','POISON','PSYCHIC','ROCK','STEEL','WATER']:put('DamageCalcFromUser',typ+'GEM',66,f'This registration supplies gem type {typ} to the shared helper.',shared=['G-GEM'])
for item,sp,cat in [('DEEPSEATOOTH','CLAMPERL','special'),('LIGHTBALL','PIKACHU','either physical or special'),('THICKCLUB','CUBONE or MAROWAK','physical')]:put('DamageCalcFromUser',item,62,f'Require underlying species {sp}.',f'The applicable category is {cat}.','Double the attack slot on qualification.')
put('DamageCalcFromUser','EXPERTBELT',63,'Require super-effective stored target typeMod.','Multiply final damage by1.2.','AI uses a separate calculated-type effectiveness test rather than proving the real stored-state input.')
put('DamageCalcFromUser','LIFEORB',63,'Exclude the dedicated confusion self-hit move.','Multiply final damage by1.3.','Damage increase does not itself perform or guarantee after-move HP recoil.')
put('DamageCalcFromUser','METRONOME',64,'Use1+0.2 times the lesser of the consecutive counter and5.','Multiply the final-damage slot.','This handler does not clamp a negative counter to0.')
put('DamageCalcFromUser','SOULDEW',65,'Require underlying Latias or Latios.','With the type-power setting true, Dragon/Psychic calculation type multiplies final damage by1.2.','With that setting false, require a special move and no souldewclause, then multiply attack by1.5.','Do not apply both alternatives.')
for item,typ in {'BABIRIBERRY':'STEEL','CHARTIBERRY':'ROCK','CHILANBERRY':'NORMAL','CHOPLEBERRY':'FIGHTING','COBABERRY':'FLYING','COLBURBERRY':'DARK','HABANBERRY':'DRAGON','KASIBBERRY':'GHOST','KEBIABERRY':'POISON','OCCABERRY':'FIRE','PASSHOBERRY':'WATER','PAYAPABERRY':'PSYCHIC','RINDOBERRY':'GRASS','ROSELIBERRY':'FAIRY','SHUCABERRY':'GROUND','TANGABERRY':'BUG','WACANBERRY':'ELECTRIC','YACHEBERRY':'ICE'}.items():put('DamageCalcFromTarget',item,70,f'This registration supplies weakening type {typ} to the shared helper.',shared=['G-RESIST'])
put('DamageCalcFromTarget','ASSAULTVEST',68,'Require special classification.','Multiply the defense slot by1.5.')
put('DamageCalcFromTarget','DEEPSEASCALE',68,'Require underlying Clamperl.','Require special classification.','Double the defense slot.')
put('DamageCalcFromTarget','EVIOLITE',68,'Read the persistent creature current-form species data.','Require a nonempty evolution list excluding prevolutions and method None.','Multiply defense by1.5 without checking whether a listed evolution can presently occur.')
put('DamageCalcFromTarget','METALPOWDER',68,'Require underlying Ditto and no current Transform flag.','Multiply defense by1.5 for either move category.')
put('DamageCalcFromTarget','SOULDEW',68,'Reject when the type-power setting is true.','Require underlying Latias or Latios.','For a special move and absent souldewclause multiply defense by1.5.')
put('CriticalCalcFromUser','LUCKYPUNCH',46,'Only underlying Chansey adds2 to the incoming critical stage.')
put('CriticalCalcFromUser','RAZORCLAW',47,'Add1 to the incoming critical stage.')
put('CriticalCalcFromUser','LEEK',46,'Only underlying Farfetchd or Sirfetchd adds2 to the incoming critical stage.')
for item,typ,stat in [('ABSORBBULB','WATER','SPECIAL_ATTACK'),('CELLBATTERY','ELECTRIC','ATTACK'),('LUMINOUSMOSS','WATER','SPECIAL_DEFENSE'),('SNOWBALL','ICE','ATTACK')]:put('OnBeingHit',item,104,f'Require current move calculation type {typ}.',f'Require central {stat} increase eligibility.',f'Request {stat}+1 before invoking generic triggered consumption.',shared=['G-MOVE-HIT','G-STAGE','G-CONSUME'])
put('OnBeingHit','AIRBALLOON',105,'Request popped feedback before removal.','Consume nonrecoverably while allowing ordinary Symbiosis.','Then explicitly request Symbiosis again.','There is no additional hpLost-positive guard in this callback.',shared=['G-MOVE-HIT','G-CONSUME'])
put('OnBeingHit','ENIGMABERRY',106,'Reject substitute, Disguise or Ice Face flags.','Require super-effective typeMod.','Invoke positive-hit berry handling with forced false.','A true helper result enters generic triggered consumption.',shared=['G-MOVE-HIT','G-CONSUME'])
for item,cat in [('KEEBERRY','physical'),('MARANGABERRY','special')]:put('OnBeingHit',item,107,f'Require {cat} classification.','Invoke the matching positive-hit berry handler with forced false.','Consume via the generic suffix only when that helper reports true.','No local Sheer Force guard is added here.',shared=['G-MOVE-HIT','G-CONSUME'])
for item,cat in [('JABOCABERRY','physical'),('ROWAPBERRY','special')]:put('OnBeingHit',item,108,'Require holder berry permission.',f'Require {cat} classification.','Require the attacker to take indirect damage.','Use floor(attacker H/8) as the damage request.','Active holder Ripen doubles the already integer-divided amount.','Request damage animation before central HP loss.','After damage and feedback invoke holder generic consumption.','The outer caller immediately checks attacker HP items if its HP fell.',shared=['G-MOVE-HIT','G-PINCH','G-HP','G-CONSUME'])
put('OnBeingHit','ROCKYHELMET',109,'Require actual contact and attacker contact-effect permission.','Require attacker indirect-damage eligibility.','Request floor(attacker H/6) damage before feedback.','Do not consume the helmet.',shared=['G-MOVE-HIT','G-HP'])
put('OnBeingHit','STICKYBARB',110,'Require actual contact and attacker contact-effect permission.','Require attacker alive and without an item.','Assign the target current item to the attacker before clearing target possession.','Set target Unburden only when its ability is active.','In a wild battle only a player-side attacker with empty I and item equal to target I transfers those I records.','This transfer does not write recycle/pickup records or invoke generic triggered consumption.','Feedback follows the transfer; there is no universal immediate check of the received barb.',shared=['G-MOVE-HIT','G-CONSUME'])
put('OnBeingHit','WEAKNESSPOLICY',111,'Reject Disguise or Ice Face flags.','Require super-effective typeMod.','Require at least one of Attack/SpecialAttack centrally raisable.','Query and request Attack+2 first.','Then independently query and request SpecialAttack+2.','The second eligible stat omits a duplicate stage animation when the first qualified.','After the used-up feedback invoke generic consumption.',shared=['G-MOVE-HIT','G-STAGE','G-CONSUME'])
put('OnBeingHitPositiveBerry','ENIGMABERRY',106,'Require canHeal even when forced.','Nonforced use requires berry permission.','Request floor(H/4), doubled after division by active Ripen.','Return true after central recovery and mode-specific feedback.',shared=['G-HP','G-CONSUME'])
for item,stat in [('KEEBERRY','DEFENSE'),('MARANGABERRY','SPECIAL_DEFENSE')]:put('OnBeingHitPositiveBerry',item,107,'Nonforced use requires berry permission.',f'Require central increase eligibility for {stat}.',f'Request {stat}+1 or+2 with active Ripen.','Ordinary mode uses cause feedback; forced mode uses ordinary stage commit.','Return the central commit result.','Forced positive entry bypasses the outer physical/special trigger condition, but not this central eligibility.',shared=['G-STAGE','G-CONSUME'])
put('AfterMoveUseFromTarget','EJECTBUTTON',128,'Require the switched set empty.','Require at least one opposing team survivor.','Require an available nonactive replacement, without full canSwitchOut.','After animation/feedback consume recoverably with Symbiosis disabled.','A negative owner replacement selection leaves this consumption committed.','A valid selection replaces the holder, clears its choice and records the switched seat.','Clear MoldBreaker if the holder was the user, then run entry effects.',shared=['G-MOVE-HIT','G-CONSUME'])
put('AfterMoveUseFromTarget','REDCARD',129,'Require the switched set empty and attacker alive.','Choose an eligible random attacker replacement before consuming.','No replacement returns before any consumption.','After animation/feedback perform ordinary consumption including possible Symbiosis.','Active Suction Cups blocks only when MoldBreaker is false, after consumption.','Ingrain independently blocks after consumption.','A successful forced replacement clears the attacker choice and records its switched seat.','Then clear MoldBreaker and run entry effects.',shared=['G-MOVE-HIT','G-CONSUME'])
put('AfterMoveUseFromUser','LIFEORB',130,'Require indirect-damage eligibility.','Require a dynamically damaging move and a positive successful-hit count.','Require at least one original target not unaffected and not substitute.','Request floor(user H/10) HP loss.','Then request user HP-item healing and fainting if necessary.','Do not consume Life Orb.',shared=['G-MOVE-HIT','G-HP'])
put('AfterMoveUseFromUser','SHELLBELL',131,'Require canHeal.','Sum target totalHPLost across all supplied targets.','Reject a nonpositive sum.','Request floor(sum/8) recovery, including accumulated substitute losses.','Do not consume Shell Bell.','Reaching half HP can clear the later Emergency Exit event; the official-game exception is absent.',shared=['G-MOVE-HIT','G-HP'])
put('AfterMoveUseFromUser','THROATSPRAY',132,'Reject if either participant team has all fainted.','Require a sound move and nonzero successful-hit count.','Require central SpecialAttack increase eligibility.','Request SpecialAttack+1, then direct consumption.','Do not add a damaging-category or positive-HP-loss requirement.',shared=['G-MOVE-HIT','G-STAGE','G-CONSUME'])
put('OnEndOfUsingMove','LEPPABERRY',92,'Nonforced use requires berry permission.','Enumerate persistent creature moves, ignoring totalPP<=0 and full-PP slots.','Prefer the first zero-PP slot in persistent order.','Only forced use may fall back to the first partially depleted slot when there is no empty slot.','No eligible slot returns false.','Request10 PP or20 with active Ripen.','Write persistent PP then clamp it to that persistent slot maximum.','Directly write the same-index battle slot to the resulting PP even if its move identity differs.','The two PP writes are sequential, not an atomic sync operation.','Return true only after the reached name lookup and feedback.',shared=['G-CONSUME'])
put('OnEndOfUsingMoveStatRestore','WHITEHERB',88,'Visit all seven battle-stage entries.','Every negative stage is directly assigned0 and sets the raised flag.','Positive and zero stages remain unchanged.','No negatives reports false.','All stage writes occur before item-name lookup, animation and success feedback.','Do not apply Simple/Contrary or per-stat central notifications.','A normal completion returns true for generic consumption.',shared=['G-CONSUME'])
put('ExpGainModifier','LUCKYEGG',150,'Return integer floor(incoming experience times3/2).',shared=['G-REWARD'])
put('EVGainModifier','MACHOBRACE',151,'Double every entry in the passed EV-yield container.',shared=['G-REWARD'])
for item,stat in {'POWERANKLET':'SPEED','POWERBAND':'SPECIAL_DEFENSE','POWERBELT':'DEFENSE','POWERBRACER':'ATTACK','POWERLENS':'SPECIAL_ATTACK','POWERWEIGHT':'HP'}.items():put('EVGainModifier',item,151,f'Add8 to {stat} when MORE_EVS_FROM_POWER_ITEMS is true; otherwise add4.','Leave the other stat yields unchanged.',shared=['G-REWARD'])
for item,weather in {'DAMPROCK':'Rain','HEATROCK':'Sun','ICYROCK':'Hail','SMOOTHROCK':'Sandstorm'}.items():put('WeatherExtender',item,138,f'Return8 only for passed weather {weather}; otherwise the wrapper preserves its duration input.',shared=['G-FIELD'])
put('TerrainExtender','TERRAINEXTENDER',139,'Return8 for any supplied terrain; the actual consumer imposes finite-source eligibility.','Do not consume.',shared=['G-FIELD'])
for item,terrain,stat in [('ELECTRICSEED','Electric','DEFENSE'),('GRASSYSEED','Grassy','DEFENSE'),('MISTYSEED','Misty','SPECIAL_DEFENSE'),('PSYCHICSEED','Psychic','SPECIAL_DEFENSE')]:put('TerrainStatBoost',item,140,f'Require stored current terrain {terrain}.',f'Require central increase eligibility for {stat}.',f'Return the cause-specific {stat}+1 commit result.','There is no grounding requirement in this handler.',shared=['G-FIELD','G-STAGE','G-CONSUME'])
put('EndOfRoundHealing','BLACKSLUDGE',144,'Poison current type chooses the healing branch.','Poison holders require canHeal and request floor(H/16) recovery.','A full Poison holder exits this branch without falling through to harm.','Only a non-Poison holder with indirect-damage eligibility takes floor(H/8) effect damage.','Do not consume.',shared=['G-EOR','G-HP'])
put('EndOfRoundHealing','LEFTOVERS',145,'Require canHeal.','Request floor(H/16) recovery, with the central minimum1 rule.','Do not consume.',shared=['G-EOR','G-HP'])
for item,status in [('FLAMEORB','burn'),('TOXICORB','bad poison')]:put('EndOfRoundEffect',item,146,f'Query whether the holder can receive {status} using itself as source.',f'Submit {status} without a source argument after qualification.','A status-cure reaction can change the final status again.','Do not consume.',shared=['G-EOR'])
put('EndOfRoundEffect','STICKYBARB',147,'Require indirect-damage eligibility.','Request the damage animation then floor(H/8) effect damage with separate feedback.','Do not consume.',shared=['G-EOR','G-HP'])
put('CertainSwitching','SHEDSHELL',148,'Return true without switching or consuming; callers decide subsequent action.')
put('OnSwitchIn','AIRBALLOON',141,'Request the floating notice only.','Do not create a permanent airborne flag or consume.')
put('OnSwitchIn','ROOMSERVICE',142,'Require a nonzero TrickRoom counter.','Require the central Speed-lowering query with no source.','After the use animation request Speed-1 and then direct consumption.','The after-TrickRoom-move all-holder path is an additional actual consumer.',shared=['G-STAGE','G-CONSUME'])
put('OnIntimidated','ADRENALINEORB',143,'Require central Speed-increase eligibility.','After use animation return the cause-specific Speed+1 commit result.','The caller uses true to invoke generic consumption; its precomputed permission does not require Intimidate actually lowered Attack.',shared=['G-STAGE','G-CONSUME'])
put('CertainEscapeFromBattle','SMOKEBALL',149,'Return true without changing the battle decision or consuming.','Actual run consumers still impose trainer/canRun and normal-versus-duringBattle entry conditions.')

# Register complete bodies and resolved copies, with exact provenance. No evaluation.
src=(REF/PRIMARY).read_text(); ls=src.splitlines()
starts=[(i+1,re.match(r'Battle::ItemEffects::(\w+)\.(add|copy)\(',l)) for i,l in enumerate(ls) if re.match(r'Battle::ItemEffects::(\w+)\.(add|copy)\(',l)]
for start,m in starts:
    f,op=m.groups()
    if op=='add':
        end=next(i+1 for i in range(start,len(ls)) if ls[i]==')')
    else:
        end=start
        while not ls[end-1].rstrip().endswith(')'):end+=1
    names=re.findall(r':([A-Z][A-Z0-9_]*)','\n'.join(ls[start-1:end]).split('(',1)[1].split('proc')[0])
    if op=='add':
        item=names[0];line,meaning,shared=rules.pop((f,item));uid=f'H-{f}-{item}'
        aa=group(uid,PRIMARY,[[start,end]],[line],meaning,
                 f'Actual caller qualifies; {item} identity and all listed local conditions hold.',
                 'Independently negate each stated predicate; numeric/category/type boundaries use the listed assertion and shared group controls.',
                 shared)
        units.append(dict(id=uid,family=f,item=item,operation=op,range=[start,end],atom_ids=aa,shared_semantic_groups=shared,operative_line=line,read_status='FRESH_FULL_BODY_READ',copy_source=None))
    else:
        for item in names[1:]:
            source=next(u for u in units if u['family']==f and u['item']==names[0])
            uid=f'H-{f}-{item}'
            aa=group(uid,PRIMARY,[[start,end]],[source['operative_line']],
                     [f'This exact copy binds {item} to the already resolved {names[0]} effect in {f} at this registration point.'],
                     f'Immediately after this copy, {item} shares the resolved effect.',
                     'Later replacement of the source key does not retarget this alias; other families are independent.', ['G-REGISTRY'])
            units.append(dict(id=uid,family=f,item=item,operation=op,range=[start,end],atom_ids=aa,shared_semantic_groups=source['shared_semantic_groups'],operative_line=source['operative_line'],read_status='FRESH_FULL_COPY_READ',copy_source=source['id'],resolved_atom_ids=source['atom_ids']))
assert not rules, sorted(rules)
assert len(units)==196
assert sum(u['operation']=='add' for u in units)==165
assert sum(u['operation']=='copy' for u in units)==31

# Explicit wrapper defaults, empty families, query/container distinctions.
fallback={'SpeedCalc':'incoming multiplier','WeightCalc':'incoming weight','PriorityBracketChange':'0','CriticalCalcFromUser':'incoming critical stage','CriticalCalcFromTarget':'incoming critical stage','ExpGainModifier':'-1','WeatherExtender':'incoming duration','TerrainExtender':'incoming duration'}
notification={'PriorityBracketUse','OnMissingTarget','AccuracyCalcFromUser','AccuracyCalcFromTarget','DamageCalcFromUser','DamageCalcFromTarget','OnBeingHit','AfterMoveUseFromTarget','AfterMoveUseFromUser','EndOfRoundHealing','EndOfRoundEffect','OnSwitchIn'}
families=[]
for i,l in enumerate(ls[:50],1):
    match=re.match(r'\s*(\w+)\s*= ItemHandlerHash.new',l)
    if not match:continue
    f=match[1]; families.append(f)
    method=re.search(r'^  def self.trigger'+f+r'\(.*?^  end',src,re.M|re.S)
    a=src[:method.start()].count('\n')+1;b=src[:method.end()].count('\n')+1
    msg=[]
    if f=='EVGainModifier':msg=['An absent resolved handler reports false without mutating EV yield.','A present resolved handler is invoked, then the wrapper reports true independently of the callback result.']
    elif f in notification:msg=['No handler yields nil from the notification dispatcher.','Mutated parameter containers or reached state changes, rather than this return, carry the effect.','The dispatcher does not automatically consume an item.']
    else:msg=[f'A nil callback result or no handler produces {fallback.get(f,"false")}.','A nonnil callback result, including false or0, is preserved rather than replaced with the fallback.']
    line=17 if f in ['SpeedCalc','WeightCalc'] else 18 if 'Accuracy' in f else 19 if 'DamageCalc' in f else 20 if 'Critical' in f else 27 if f in ['ExpGainModifier','EVGainModifier'] else 169 if f=='TrappingByTarget' else 21 if f in ['HPHeal','StatusCure','OnEndOfUsingMove','OnEndOfUsingMoveStatRestore'] else 26 if f in ['TerrainStatBoost','OnSwitchIn','OnIntimidated'] else 24 if f=='OnStatLoss' else 25 if f.startswith('EndOfRound') else 23 if f.startswith('AfterMove') else 22 if f.startswith('OnBeingHit') else 50 if f.startswith('Priority') else 51 if f=='OnMissingTarget' else 138 if f=='WeatherExtender' else 139 if f=='TerrainExtender' else 148 if f=='CertainSwitching' else 149
    group('D-'+f,PRIMARY,[[i,i],[a,b]],[line],msg,'A registered handler returns its ordinary value.','Missing key; handler nil; handler false; handler0; mutation before a thrown error.', ['G-REGISTRY'])
assert len(families)==32
for f,line in [('CriticalCalcFromTarget',20),('TrappingByTarget',169)]:
    group('E-'+f,PRIMARY,[[1262,1266] if f=='CriticalCalcFromTarget' else [1900,1904]],[line],[f'The complete fixed registry defines no {f} handlers, while the real caller and its neutral fallback still exist.'],'No fixed handler.', 'Explicit future registration is outside this fixed snapshot; do not infer absence of a caller.', ['G-REGISTRY'])

premises=[dict(id='EIA-P01',meaning='All claims are SOURCE_STATIC or explicitly hand-derived finite vectors at fixed B8/R. No Ruby/reference/model/native/game/save execution.'),dict(id='EIA-P02',meaning='Registered identity, data-loaded identity, current possession and active-item eligibility are separate. Apply the actual caller before local predicates; explicit conditional definitions remain reviewed even without a default data record.'),dict(id='EIA-P03',meaning='Normal feedback/data/helper calls must return for later steps to occur. On exception retain only reached prefixes. Exact message wording, host pixels/audio, arbitrary plugins and all cross-domain combinations are outside this finite approval.')]
group('G-U04','Data/Scripts/011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb',[[1338,1380]],[117,119,121,123],[
 'Natural Gift first requires an actual current berry, active held item and at least one NaturalGift_ prefix; the move gate does not query ordinary berry eating permission.',
 'Its base type starts Normal and stops at the first fully matching type/power flag, accepting the type only when registered.',
 'Each damage query dereferences current user.item.id before it can reach item lookup or the fallback1; no retained starting item protects a later hit.',
 'When an item remains but no full power flag matches, the query returns1; a matching numeric flag instead returns at least10.',
 'The finite ordinary fixture uses active Natural Gift/Parental Bond, H160/h81 and current ORAN against an eligible surviving JABO target with all listed suppressors absent.',
 'After first target HP loss, eligible JABO requests160//8=20 from the user, committing81to61 before the immediate user item-heal query.',
 'At61 the ordinary ORAN half-HP gate passes, its10 request reaches71, then successful berry consumption removes the current item and commits the recorded prefixes.',
 'A planned second hit then encounters nil at the current item dereference; first target loss, user71 and both consumptions remain reached prefixes.',
 'Changing only starting HP to101 gives81 after JABO, above80; ORAN returns false, remains current and the second query can still read its80 power flag.',
 'Natural Gift normal end checks current item existence and directly consumes with arguments true,true,false; the high-HP control therefore consumes ORAN only at normal end and does not newly set Belch.',
 'Removing only active Parental Bond leaves a single planned hit, so the low-HP control reaches no next-hit nil access and normal-end current-item guard skips its already absent ORAN.',
 'These are hand-derived finite paths with all stated legal type/PP/feedback premises, not executed traces or a promise of generic terminal restoration, rollback or AI simulation.'
], 'Ordinary low-HP two-hit fixture from the complete current operative clauses.', 'Independently change only starting HP81to101 or planned hit count2to1; distinguish missing item from present malformed power flags.', ['I-CORE','I-MOVE','I-AI'])
family_callers={
 'SpeedCalc':[(BATTLER,248,275)],'WeightCalc':[(BATTLER,277,288)],
 'HPHeal':[(HELPER,297,323)],'StatusCure':[(HELPER,297,311),(HELPER,329,336)],
 'OnStatLoss':[(HELPER,384,388),(TRIGGER,177,217)],
 'PriorityBracketChange':[('Data/Scripts/011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb',136,262)],
 'PriorityBracketUse':[('Data/Scripts/011_Battle/001_Battle/010_Battle_AttackPhase.rb',6,14)],
 'OnMissingTarget':[('Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb',583,660)],
 'AccuracyCalcFromUser':[(CALC,126,166)],'AccuracyCalcFromTarget':[(CALC,126,166)],
 'DamageCalcFromUser':[(CALC,283,484)],'DamageCalcFromTarget':[(CALC,283,484)],
 'CriticalCalcFromUser':[(CALC,178,220)],'CriticalCalcFromTarget':[(CALC,178,220)],
 'OnBeingHit':[(TRIGGER,5,82)],'OnBeingHitPositiveBerry':[(HELPER,297,311)],
 'AfterMoveUseFromTarget':[(TRIGGER,87,205)],'AfterMoveUseFromUser':[(TRIGGER,87,205)],
 'OnEndOfUsingMove':[(HELPER,341,350)],'OnEndOfUsingMoveStatRestore':[(HELPER,341,364)],
 'ExpGainModifier':[('Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb',92,224)],
 'EVGainModifier':[('Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb',59,90)],
 'WeatherExtender':[('Data/Scripts/011_Battle/001_Battle/001_Battle.rb',707,732)],
 'TerrainExtender':[('Data/Scripts/011_Battle/001_Battle/001_Battle.rb',786,811)],
 'TerrainStatBoost':[(HELPER,315,323),(HELPER,367,372),('Data/Scripts/011_Battle/001_Battle/001_Battle.rb',786,811)],
 'EndOfRoundHealing':[('Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb',597,623)],
 'EndOfRoundEffect':[('Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb',684,701)],
 'CertainSwitching':[('Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb',38,71)],
 'TrappingByTarget':[('Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb',38,71),('Data/Scripts/011_Battle/001_Battle/007_Battle_ActionRunning.rb',5,159)],
 'OnSwitchIn':[('Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb',316,374)],
 'OnIntimidated':[(HELPER,376,381),('Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb',2851,2868)],
 'CertainEscapeFromBattle':[('Data/Scripts/011_Battle/001_Battle/007_Battle_ActionRunning.rb',5,159)]}
for u in units:
    u['mandatory_common_groups']=['G-ACTIVE','G-REGISTRY','D-'+u['family']]
    if u['family'] in ['ExpGainModifier','EVGainModifier']:u['mandatory_common_groups'].remove('G-ACTIVE')
    u['actual_callers']=[dict(path=p,range=[a,b]) for p,a,b in family_callers[u['family']]]
    u['consumer_reception']=['I-CORE','I-MOVE'] if u['family'] in ['OnMissingTarget','OnBeingHit','AfterMoveUseFromTarget','AfterMoveUseFromUser','DamageCalcFromUser','DamageCalcFromTarget','AccuracyCalcFromUser','AccuracyCalcFromTarget','CriticalCalcFromUser'] else ['I-CORE']
    u['ordinary_scope']='Apply the actual caller gates first; local callback definitions remain conditional when invoked directly.'
    u['failure_prefix']='The assertion order is the dependency of writes, not a simulated trace. See the complete source range and shared group; early predicates reject before local writes, later callback/feedback errors retain reached writes without a transaction.'
for a in atoms:
    if a['id'].startswith('G-REGISTRY'):
        a['additional_operative']=[dict(path='deliverables/final-specification-set/generic-kernel/wp05-events-extensions-plugins.md',range=[30,38],role='Finite full registry contract read; no whole WP05 approval')]
    if a['id'].startswith('G-STAGE'):
        a['additional_operative']=[dict(path='deliverables/final-specification-set/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md',range=[85,105],role='Finite full stage query/commit contract read')]
    if a['id'].startswith(('H-Damage','D-Damage','D-Accuracy','D-Critical','G-RESIST')):
        a['additional_operative']=[dict(path='deliverables/final-specification-set/pokemon-rules/wp43-types-accuracy-and-damage.md',range=[67,157],role='Finite calculation clauses read, not entire WP43 acceptance')]
dump('evidence/semantic-atoms.json',dict(schema='gr8-manual-item-meaning-atoms/v1',premises=premises,assertions=atoms,groups=groups,handler_units=units,denominator_rule='Manually separated observable predicates, quantities, returns, writes and ordering obligations. Statement/line/semicolon/registration counts are never taken as semantic completeness proof.',frozen_input=dict(B8=B8,R=R,contract=CONTRACT)))
dump('forward-mapping.json',dict(schema='gr8-item-forward/v1',reference=PRIMARY,formal=[MAIN,COVER],assertions=atoms,handler_bindings=units,empty_families=['CriticalCalcFromTarget','TrappingByTarget'],unmapped_primary_handlers=0,unread_primary_source_ranges=[],qualification='Every assertion retains its actual operative body clause. Registration table rows are identity corroboration only; shared helper assertions are mandatory dependencies, not inferred from a family label.',execution='NOT_EXECUTED'))
dump('evidence/denominator.json',dict(schema='gr8-item-frozen-denominator/v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),primary_reference_files=1,primary_source_lines=1948,formal_files=2,formal_lines=252,shared_catalog_files=2,shared_catalog_lines=669,families=32,direct_bodies=165,copy_statements=21,copy_destination_bindings=31,expanded_handler_pairs=196,unique_registry_item_names=len({u['item'] for u in units}),manual_assertions=len(atoms),manual_groups=len(groups),root_acceptance='PENDING_ACTUAL_INDEPENDENT_RECEPTION',not_a_global_requirement_denominator=True))
print(json.dumps(dict(assertions=len(atoms),groups=len(groups),handlers=len(units),families=len(families))))
