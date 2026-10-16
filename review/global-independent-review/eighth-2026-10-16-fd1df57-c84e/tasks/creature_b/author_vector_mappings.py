"""Serialize individually reviewed catalog rows. Text is reviewer authored, no generated facts."""
import json,pathlib
p=pathlib.Path(__file__).resolve().parent
body='''BG-01|BG02,BG05|900+200→999+101, aggregate1100; slot limit not total cap
BG-02|BG02,BG05|empty infinite reserves length+1 slot only;1500 precheckfalse/no write
BG-03|BG02,BG05|same input directadd writes999 thenfalse; no transaction
BG-04|BG02,BG05|finite capacity exhaustion retains earlier additions
BG-05|BG02,BG05|all-or-none precheck prevents all writes on failed capacity
BG-06|BG02,BG05|999+101 remove1000→100 remaining; true+compact
BG-07|BG02,BG05|five remove10→false but all5 removed; all-or-none differs
BG-08|BG03|replace both old slots in old pocket, same new ID but no merge
BG-09|BG01,BG03|clear items/cursor0 retains last pocket4/registrations
BG-10|BG02|configured fourth pocket sort by item definition insertion order
BG-11|BG02,BG05|unlimited means oldlength+1 scan; empty new999 yes1000 no
BG-12|BG02|unknown query0, normal has/add/canadd false; has nonpositive is rawcomparison
BG-13|BG05|negative helper quantity raises before operation
BG-14|BG04,METADATA|constructor defaultempty vs actual metadata POTION; each valid seed1
BG-15|BG02,BG05,OVERWORLD|three receipt wrappers directadd1500 partial999/false; distinct message timing
BG-16|BG02,PC-UI|gift precheck and PC capacity precheck prevent direct partial operation
BG-17|BG04,PC-UI|withdraw selected qty, source removal before destinationadd
BG-18|PC-UI|withdraw bag capacityfailure no storage change
BG-19|PC-UI|deposit storage capacityfailure no bag change
BG-20|PC-UI,ITEM-DATA|important toss rejection no delete
BG-21|PC-UI|important stack moves whole stack, skips quantity, singular display1
BG-22|U01,BG03,BAG-UI,READY-UI|unqualified ordinary no register; directregistered exposesunregister; Readycollect only held
BG-23|U01,BG03,BAG-UI|fieldhandler important register dedup and two qualified icons
BG-24|BG03,READY-UI|removed item stillregistered but absent Readycollection
BG-25|READY-UI|noitem/nohiddenmove yields message before menu
BG-26|READY-UI|3 registered1held→only1 item collected
BG-27|U14,BAG-UI|filter resets on entry; wrapper restores original cursors on normal return/cancel
BG-28|BG01|pocket0/9 throws, upper invalid index ignored, negative index allowed
BG-29|SAVE|conversion old registered field to list and Readyselection state; static reload only
BG-30|BAG-UI|egg-only count0 suppressesGive; no selection-state externalmutation
BG-31|BAG-UI|fainted nonEgg adds eligibility; menu build itself no inventorywrite
IU-01|U04,E05|fullHP Potion false/no consume
IU-02|U04,E05|HP0 Potion false/no consume
IU-03|U04,E05,U11|missing30/request20 actual20, true thenconsume1
IU-04|E06|Revive101 max→50 floor; status cleared
IU-05|E06|RevivalHerb101→101 then friendship loss
IU-06|E06,U11|Awakening only living rawSleep, otherstatusfalse
IU-07|U05,E07,B02|validpositivePP partial+10 cap; fieldfainted vs battleable gated separately
IU-08|E07|PPUP2→3;>=3 or total<=1 reject
IU-09|U06,E08|gen8 vitamin100→110 restrictedordinary252/510 premise
IU-10|U06,E08|cap100 enabled100→no effect
IU-11|U06,E08|feather252→zero/happinessunchanged
IU-12|U06,E08,U11|250EV qty2→252, h80→86 default bonusesabsent; stock5→3; configoff1
IU-13|E08,U01|WING copied quantity+effect aliases only if valid record supplied
IU-14|U07,E11|PomegEV15→5,h80→90 with no bonuses; consume1
IU-15|U07,E11|EV0+h255 both eligibilityfalse/no consume
IU-16|U06,U11|explicit bypassedqty3 with room20, first2success thirdstop; true consumes requested3
IU-17|U06,U01|gen8remainingmin252/510 ceil10, configofffixed1
IU-18|U03,E10|XSqty2 combined200EXP once; happiness vitamin twice
IU-19|U03,E10|maxlevel candy rejects/no consume
IU-20|U10,E01,ITEM-DATA|compatibleTM free slot learn, important no consume; bag wrapperstat1
IU-21|U10,E01,ITEM-DATA|TR learn true then consumable1
IU-22|U10,U12|known machine rejected filter or learning, no consume
IU-23|U10|fullmoves cancel forgetting returnsfalse before consume
IU-24|E05,U11|stone eligibility then noncancellable evolution callback; species/screen caller in IF-EVOLUTION
IU-25|E05|no stone target false/no consume
IU-26|B02,U01,COMMAND,ATTACK|registration writes itemchoice then removesbag1
IU-27|B02,COMMAND,ATTACK,ENDING|postregistrationfullHP execution recheck refunds, leaveschoice identity
IU-28|B05,COMMAND,ATTACK|qualificationpassed; handlernormalreturn clears identity regardless boolean
IU-29|B01,B04,ATTACK|ball branch no generic failurecatchrefund; capture consumer separate
IU-30|B02,B06|battleRevivefloorhalf min1+statusclear
IU-31|B01,COMMAND|ballallactions flag; multiopponent/other guard before registration
IU-32|B03,B08|XAttack2/1config, fixed3; stat eligibility and battlehappiness
IU-33|B03,B08|onlySpeedlegal mushroom five-main-stat loop→speed1 and happiness
IU-34|B01,B04|Mist existingreject else5 turns, not Safeguard
IU-35|E03,FIELD-MOVES|Honeytrue after SweetScent weather/noencounter no-op, consume by data
IU-36|B01,COMMAND|doll trainer refusal beforeregistration
IU-37|E02,OVERWORLD|Repel100, rejects existing>0; step snapshot beforedecrement/reuse
IU-38|E02,E03|rope missingescape/follower rejects before consume
IU-39|E03|Ash nofaintednonEgg rejects
IU-40|U11|eggonlyparty rejects even boxednonEggexists
IU-41|U11|successonce then targetcancel retfalse; prior effect/removal retained
IU-42|U12|directhelperstock0 noindependentrefusal; default UIpresence premise differs
IU-43|U11,U12,COMMAND|field quantityminstock; battle registered removefalse raises afterchoice write
IU-44|E12,FORMS|nightGracidea false; day plusother gates requests1; getter mayresetwhenfainted/frozen/night
IU-45|E13|secondpartyselectioncancel beforelink/form/toolwrite
IU-46|E13,FORMS|ordinary no nestedmutation Kyurem+Zekrom2/samefused reference/toolreplace
IU-47|E13|split partyfull rejects beforewrites
IU-48|E13,FORMS|free split requests0, append samefused then clear/toolrevert, callbacks canintervene
IU-49|U07,E11,U11|PomegEV250+h255 qty25→EV0/stock0; offqty1→240/stock24
IU-50|U06,E08|legaltemplateHP/ATK255 store510 floor63; no normalization; existingboundedreverse retained
IU-51|B02,B06,E06,COMMAND|battlefullheal/fullrestore accepts confusiononly/fullHP but fieldrefuses; neitherissue rejects
IU-52|U04,E05,B05|active Sitrusfloor101/4=25 and105/4=26; HP1→26/27, heldpassivesseparate
IU-53|E05,E06,B05,B06|each identity request table actuallychecked config20/60:50/120:200/full/30:50/50:60/70:80/100/10; capactualgain
IU-54|E10|maxlevel Candy eligibleevolutionBACK effectstilltrue consumes; animation/evolutionrecord IF-EVOLUTION
IU-55|U01,COMMAND,ATTACK|Direct5 missingfamilies visible/defaultCanUseTrue→consume and no effect; types1/3 absentfamilyreject
IU-56|U08,E09,NATURE|Lonelyattack+/defense-, Braveattack+/speed-, calculated override only; vectorbase/rounding CRE-A receiver
IU-57|E13,FORMS,U10|Necrozma1 appendsSunsteelStrikePP5 via callback, no nestedmutation; species/move data receiver
IU-58|E01,U10,U12,ITEM-DATA|defaultTM57TRChargeBeam bagaddsfirstmoves/stat, Party directdoesnot; bothconsume
IU-59|PARTY-UI,U04|source120request24, HP50→26; target30/54 gains24 vs30/40 gains10
SH-01|SHOP-BUY,RESOURCE|200*3=600 from1000→400; spendstat600 count3
SH-02|SHOP-BUY|150<200 firstguard beforequantity/no writes
SH-03|SHOP-BUY,RESOURCE|free999; ordinarywallet0..M unchanged after money-0 setter; alladdsuccesspremise
SH-04|SHOP-BUY|999999price1 qtymax999
SH-05|SHOP-BUY|partial2 of3 removes2/no money/stat; rollbackremovefailure raises
SH-06|SHOP-BUY,SHOP-ENTRY|importantqty1 confirmation and postpurchasealiasedstockdelete
SH-07|SHOP-ENTRY|owned important removed from callerarray on entry and notrestored
SH-08|SHOP-SELL|explicitqty5 *150→750 resourceandactualgainstat, item0
SH-09|SHOP-SELL,RESOURCE|999950+100clamps999999 actualstat49
SH-10|SHOP-DATA,SHOP-SELL|important or sell0 refusesbeforewrite
SH-11|SHOP-BUY,SHOP-SELL|qty0/refusal no transactionwrites
SH-12|PRICE-WRITER,SHOP-DATA,BP-DATA|buyoverlay250positive valid in both money/BPsharedslot
SH-13|PRICE-WRITER,SHOP-DATA|[-1,0] sell0 validoverride→cannotSell
SH-14|PRICE-WRITER,SHOP-DATA|sellarg60 stored120/effective120
SH-15|PRICE-WRITER|firstnonpositivebuy initializes[-1,-1], missingwrites datafallback
SH-16|PRICE-WRITER|nonpositive updates preserve prior250/120; missingcommand2arg raises
SH-17|ITEM-DATA,RESOURCE|textprice1000000 unboundedbyMAX; resourceaffordability separate
SH-18|SHOP-BONUS|gen8qty25 anyball attemptsPremier2; actualsuccessfulcount stat
SH-19|SHOP-BONUS|legacyPokeballqty10 one bonus only
SH-20|BP-BUY,RESOURCE|100-20*3→40 spend60 commoncount3
SH-21|BP-BUY|50/20 floor2; chosen2→10 spend40 count2
SH-22|BP-BUY|50<60 firstguard/no writes
SH-23|BP-BUY|explicit overmax input reachingsecondguard rejected; normalUIcannotchooseit
SH-24|BP-BUY|free999, price0 and ordinaryBPsetterdomain preservesBP
SH-25|BP-DATA,BP-SCENE,BP-BUY|price20qty3 display30 vs confirm/deduct60
SH-26|SHOP-ENTRY,BP-ENTRY,PRICE-WRITER|normal exit clearsalloverlay; exceptionsnoensureguarantee
SH-27|SHOP-SELL,SHOP-SCENE|holding5 defaultquantity1→150/item4; explicit5 requiredSH08
SH-28|BP-DATA,BP-SCENE|20qty1/2/3 display10/20/30 deduct20/40/60;21qty3 display30 deduct63
R4-U04-PP01|B02,COMMAND|fieldfainted baseline but battleHP0fails eligibility fiveitems stock1
R4-U04-PP02|E07,U05,U11|fieldHP0 PP0→10or35 byfamily, consumes1, HPremains0
R4-U04-PP03|E07,B02,B07,COMMAND|HP1 bothcontexts restore10/full, consume1 atdifferentstages
R4-U04-PP04|E07,B02|fullPP allfamilies reject stock1/no actionregistration
R4-U04-PP05|E07,COMMAND|selectedmovecancel noPPwrite/no consume; battlereturnsselectionlayer
R4-U04-PP06|U05,E07,B07|PP30/35 actual5 notrequest10/full; consume1
R4-U04-PP07|E07,B07|duplicateIDs slots35/0/30→35/10/35 or all35; battleHP0entirebefore-registerrefusal
'''
rows=[]
for line in body.strip().splitlines():
    i,s,f=line.split('|',2);rows.append(dict(id=i,source_facts=s.split(','),judgement=f,premise='Exact per-row fixed B8 input and shared fixture, no unmentioned mutation/cancel; explicit counterexamples keep their own finite premises.',evidence='DERIVED_VECTOR / NOT_EXECUTED',consumer_qualification='interfaces.json'))
assert len(rows)==125,len(rows)
out={'schema':'gr8-creb-individual-vector-mapping/v1','reviewer':'/root/creature_b','formal':'deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md','primary_named_rows':118,'additional_PP_rows':7,'vectors':rows,'other_shared_groups':'All IF11/EX5, R5U03 groups and GR53/DC20/R6GR5 fully read; finite atomic groups in reverse-mapping.json. GR/DC full-domain numerical acceptance remains its actual primary owner; no full-domain credit from this catalog read.','warning':'These are reviewer-authored row judgments after actual source/formal reading, not a script-generated expected-value test or executed result.'}
(p/'vector-mapping.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('individual rows authored',len(rows))
