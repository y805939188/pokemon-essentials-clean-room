import pathlib,json
P=pathlib.Path(__file__).resolve().parent;base=json.loads((P/'manual_batch_07a.json').read_text());d=base['source_dictionary'];rows=[]
d['usagefull']={'path':'Data/Scripts/011_Battle/003_Move/002_Move_Usage.rb','range':[1,405],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(312,[
 'First-target check calls actual ShowFailMessages and CalcTypeMod, writes target.damageState.typeMod before charging TwoTurnAttack earlytrue.',
 'After charging gate, actual move targetfailure callbacktrue refuses before Psychic/guards/reflect/immunity; concrete targetcallback can mutate/raise first.',
 'Psychic requires fieldPsychic, targetaffectedByTerrain, opposinguser and savedchoicepriority>0; feedback thenfalse, no generic fullmove priority recalculation.',
 'CraftyShield targetsideflag, user!=target, status and !targetdata.targets_all marks target/userSuccess protected and false.',
 'ActiveUnseenFist plus raw contactMove? bypasses following Wide/Quick/Protect/King/Spiky/Baneful/Obstruct/Mat block, not prior Crafty/Psychic or later immunities.',
 'WideGuard nonself,targetnum>1 and(current>=7 or damaging) refuses/protected; QuickGuard additionallycanProtect flag and savedprioritypositive.',
 'Protect flag undercanProtect rejects; KingsShield/Obstruct require damaging; Spiky/Baneful do not adddamaging requirement.',
 'Kings contact reaction actualpbContactMove and affectedByContact plus lowerAtk eligibility, requestcurrent>=8 −1 else−2.',
 'Spiky actualcontact/affectedContact/indirect eligible requests totalHP/8 integer, thenfeedback andHPitemcheck; Baneful actualcontact/affectedContact/poisoneligibility requests ordinarypoison.',
 'Obstruct actualcontact/affectedContact/lowerDef eligibility requests−2; central stat/status predicates can refuse reactions separately from already protected move.',
 'MatBlock sideflag plusdamaging undercanProtect setsprotectedfalse return without own commonanimation; not inferred contactreaction.',
 'Then status/canMagicCoat/nonsemiInvul/opposingtarget: MagicCoat recordsdamageflag and consumes targetflag beforefalse; activeMagicBounce requires !moldBreaker and !alreadyBounce, writesbothflags thenfalse.',
 'Actual ability-immunity method runs before type-immunity; default returnsnoimmunity ifmoldBreaker, elseactive target handler decides. Targetstate gain from such handlers can precede any eventual type refusal.',
 'Dynamic damagingMove? plus ineffective typeMod rejects; current>=7 Prankster flag with targetDark/opposing rejects next.',
 'Ground damaging and airborne/nonhitsFlying checks activeLevitate&&!moldBreaker, activeBalloon, MagnetRise, Telekinesis individually with ownmessage; not allairborne automaticallysamefeedback.',
 'Powderflag: targetGrass&&MORE_TYPE_EFFECTS firstrefuses; current>=6 activeOvercoat&&!moldBreaker thenSafetyGoggles refuse withdistinctfeedback.',
 'Last Substitute positive/status/nonignoresSub/user!=target refuses; reachingendtrue means only this checkstage passed, not perhit accuracy or damage succeeded.'
],['checksfull','usagefull','battlerfull','abilityeffects','ability_item','calculations','typefull','targetdata','damage_state','priority','config'],'typeprecalculation→charging→targetcallback→terrain→Crafty→contact-abilityguardbypass→otherguards/reactions→reflect→ability→type→Prankster→ground→powder→substitute. Each first-return gate retains earlier writes.',open=['Complete concrete targetcallback/immunity/protect/position producers beyond named read classes and received limited source facts remain exactOPEN; no all Move/Ability approval.'])
row(313,[
 'Perhit success firstreturns true for usercharging TwoTurnAttack; next LockOn counterpositive and recordedtargetindexmatch true.',
 'Then actual move.pbOverrideSuccessCheckPerHit can earlytrue; defaultfalse, concreteoverrides haveownscope.',
 'Active userORtarget NOGUARD, battlefutureSight or functionPowerUpAllyMove only sets hitsInvul=true to bypass invulnerability/SkyDrop block; no unconditional accuracytrue here.',
 'Without exemption, matching targetTwoTurn function Sky/Dig/Dive checks corresponding moveflags, protection-removalinvulnerability alwaysmiss; targetSkyDrop holder!=user and nothitsFlying also miss.',
 'Miss writes targetinvulnerable and log, thenfalse before skipAccuracy. If notmiss, skipflagtrue returns true; else actual AccuracyCheck true returns true, false logs/refuses.',
 'Missmessage uses affection_missed first; multiple-targetdata or targetTwoTurn givesavoidtext; otherwise actual customMissMessage returntruthy suppresses generic missedtext.',
 'Earlier first-target immunity/guards stillapply; perhit exemption doesnot rewind those checks or guarantee all special accuracyfamilies.'
],['checksfull','usagefull','calculations','battlerfull','movebase'],'perhit charging/lock/override→invulnerabilityexemption→skipflag→actualaccuracy→message; two layers distinct.',open=['Complete specific successOverride and special Counter/Mirror/OHKO accuracy classes not all personallyreceived by this source-stage proof; exactOPEN.'])
row(314,[
 'N01 ordinary accuracy handler UserNOGUARD and TargetNOGUARD each set base_accuracy0 when called; calleronlytarget ability handler guarded !battle.moldBreaker.',
 'Perhit targetNOGUARD may bypass invulnerability even underMoldBreaker, but later ordinary accuracycalculator skips its targethandler; no universal targetNoGuardguarantee.',
 'Ordinary notspecial, rawbase70, zerostages and nomodifiers/userNoGuard, userMoldBreaker and active targetNoGuard: resultingthreshold70, rand69<70true/rand70<70false.',
 'RemovingMoldBreaker permits targethandler base0 then ordinary accuracyearlytrue after modifiers; doesnot generalize special overriddenaccuracyfamilies.',
 'Historical2026-09-27 N01 text marks bounded priorrevision/review closure; retain existing twoflag/PP contracts and old12 closure. This read is no new candidate/count or reconstructionofhistoricexecution.'
],['checksfull','calculations','abilityeffects','battlerfull','ability_item'],'savedMoldBreaker/currentactive target→modifierscallgate→base0 ornormal70threshold→source-static designed comparison; historical scope not reopened.')
row(315,['First precheck actual ChooseMove false explicitly sets currentfailuretrue, returnsfalse; all later stagegates skipped and ordinaryPPnotdeducted.'],['checksfull','use'],'ordered precheck1→failureBoolean versusaction refusal.')
row(316,['Afterchoose pass user SkyDrop marker>=0 returnsfalse with no user-facing move-failure message in this branch; debuglog possible; currentfailure not explicitly settrue.'],['checksfull','use','debuglog'],'ordered precheck2→silent-normal-refusal with qualified initialfalse.')
row(317,[
 'Next positiveHyperBeam logs andmustrecharge display, before ordinaryTruantgate.',
 'If actualactiveTRUANT toggles its flag even thoughreturnfalse; no uniformfailuretrue assignment. PPdeduction notyetreached.'
],['checksfull','use','ability_item'],'ordered precheck3 recharge→Truanttoggle→refusal; notREST.')
row(318,[
 'Next choiceindex−2 is Palace incapacity marker, displays incapable andfalse before skip/ordinarystatus/PP.',
 'Actual Palace category selection noallowedmoves registers−2/struggleobject; rawordinary valid move index−2 is not normalplayer menu selection.'
],['checksfull','palace','use'],'actualspecialproducer−2→precheck4 feedback/refusal; no defaultordinary choice alias.')
row(319,[
 'After firstfour gates passed, originalentry skipAccuracyChecktrue immediately returnsTryUse true before laterstatus/obedience.',
 'False for normal/Struggle/ordinary-entrycontinuedmultiTurn meansorderedlatergates eligible. Effective specialUsage changes aftercapture do not rewrite skip.',
 'This scope bypasses TryUse steps6–12; targetlevelsuccess/ordinaryaccuracyhas its separate skip/invulnerability order.'
],['checksfull','use'],'entry twoflags→firstgates→skip gate→laterstatechecks.')
row(320,[
 'Sleep reached decrementscount then curesif<=0 elsecontinuesstatus andrefusesif!usableWhenAsleep.',
 'Frozen reached nonthaw-user move draws100<20 cure elsecontinues/refuses; thawsUser moves do not drawthiscure andlaterthaw branch handles.',
 'Sleep/frozenrefusal explicitly setsfailuretrue; source callbackfailures beforewrite retainprefix.'
],['checksfull','use','b_change'],'precheck6statuscount/random/cure→explicitrefusal; savedPPstillunchanged.')
row(321,['Obedience invoked afterstatus and beforeTruant; full badge/config/foreign/Shadow/probability and disobey branch detailed in C328–336 and earlier exactBoolean cases, not implied by menu orAI eligibility.'],['checksfull','shadowother','use'],'precheck7→mayreplacechoice/continue ORrefuse withoutautomaticfailuretrue.')
row(322,[
 'ActiveTRUANT reached flips currentflag; ifnewfalse showsability/loaftext, setsfailuretrue/hides/logs thenfalse.',
 'Othernewflag passes; rechargeearliercouldalreadytoggle andreturn beforethisgate. No STALL/slow-priority conflation.'
],['checksfull','ability_item','use'],'precheck8actualactive ability state→toggle→specificrefusal.')
row(323,[
 'Flinchflag reached displays/logs; active OnFlinch handler executes before failuretrue/false.',
 'Steadfastcentralstage effects or handlerfailprefix are distinct from action cancellation; not every feedback call guarantees finalfieldwrite.'
],['checksfull','abilityeffects','ability_item'],'precheck9feedback→activehandler→failurewrite/refusal.')
row(324,[
 'Confusionpositive decrements; zero cures+snapoutfeedback andcontinues.',
 'Stillpositive anim/message then thresholdcurrent>=7 33 else50, randomselfdamagebranch calls confusiondamage before failuretrue/refusal.',
 'No selfdamage branch letslaterparalysis/attraction run; ordinaryconfusioncurrentfailure rulesdistinct fromdisobedience selfdamage.'
],['checksfull','use','config'],'precheck10counter→cure ORrandomdamage→fieldwrite; no universaldamageeachconfusionturn.')
row(325,['Reached PARALYSIS and rand100<25 continuesstatus/logs, setsfailuretrue andfalse; otherroll proceeds. Requirespriorstatus/obedience/Truant/flinch/confusion notterminated.'],['checksfull','use'],'precheck11randomblock→noPPyet.')
row(326,[
 'Attractrecordnonnegative animates/displaysreferencedbattler, draws100<50 blockmessage/log/failuretrue/false.',
 'NonblockreturnsTryUse true; invalidstale referencedslot couldfail earlier, so validcurrenttargetandnormalcallbacks arepremises, not guaranteed by oldnumericmark.'
],['checksfull','use','battlerfull'],'precheck12targetreference/feedback→randomblockorqualificationtrue; no effectcallbacksuccessguarantee.')
base['source_dictionary']=d;base['rows']=rows
(P/'manual_batch_07b.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n');print({'rows':len(rows),'children':sum(len(x['children']) for x in rows)})
