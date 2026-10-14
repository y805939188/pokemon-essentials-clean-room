"""Render exact-clause reverse matrix and manually checked vector inventory.

Reads the bound formal text and our own annotations, not reference executable
code. Parsing is structural only; semantic determinations are the manual data.
"""
import json
import re
from pathlib import Path

ROOT=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT=Path(__file__).resolve().parent
review=json.loads((OUT/'forward-matrix.json').read_text())
main='deliverables/final-specification-set/combat-requirements/wp52-b-field-damage-healing-and-target-evaluation.md'
coverage='deliverables/final-specification-set/combat-requirements/wp52-b-effect-coverage.md'
catalog='deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md'
all_text={p:(ROOT/p).read_text().splitlines() for p in [main,coverage,catalog]}

def locators(clause):
    result=set()
    for span in re.findall(r'L([0-9,\-]+)',clause):
        for part in span.split(','):
            if '-' in part:
                a,b=map(int,part.split('-'))
                result.update(range(a,b+1))
            else:
                result.add(int(part))
    return result

reverse=[]
local_lines=sorted(set().union(*(locators(r['formal_clause']) for r in review)))
for line in local_lines:
    if line>len(all_text[main]) or not all_text[main][line-1].strip():
        continue
    mapped=[r for r in review if line in locators(r['formal_clause'])]
    reverse.append(dict(formal=main,line=line,clause=all_text[main][line-1],
                        source_units=[dict(id=r['id'],path=r['path'],start=r['start'],end=r['end'],family=r['family']) for r in mapped],
                        preconditions=sorted(set(r['upstream_precondition'] for r in mapped)),
                        verdict='LOCAL_PRIMARY_SCOPE_CHECKED; see individual source row; any clauses concerning other effect files remain parent-owned',
                        qualifications=sorted(set(r['boundary'] for r in mapped))))

# Shared prerequisites are supported by newly read common consumers, not by an
# inherited PASS or an inference from registration existence.
for line,fact,source in [
 (11,'Five output families stay separate. Actual HP commits are separate scope.','005_AI/001_Battle_AI.rb:85-118;005_AI/005_AI_ChooseMove.rb:38-82,232-323'),
 (13,'Independent PredictMoveFailure and ScoreMoves gates; medium base gate; local60 can be modified later; common missing-family defaults.','005_AI/009_AITrainer.rb:55-87;005_AI/005_AI_ChooseMove.rb:273-310;005_AI/011_AIMove.rb:81-92;005_AI/001_Battle_AI.rb:97-118'),
 (15,'Integer/floating distinctions were checked per individual formula; check_for_move excludes finitePP0, direct slot loops do not.','005_AI/010_AIBattler.rb:292-313;005_AI/005_AI_ChooseMove.rb:283-285'),
 (27,'Actual base-value calls are consumers of the real receiver; rough formula is a different stage.','005_AI/011_AIMove.rb:81-106,367-374;003_Move/008_MoveEffects_MoveAttributes.rb:1-635'),
 (61,'No dedicated base-power registration for turn-lostHP/acted/fusion families is not proof of absent real base changes.','006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb:382-431;005_AI/011_AIMove.rb:81-87'),
 (79,'Multi-hit representative combines planned total base once; formula+2/rounding are not per-hit accumulation.','005_AI/011_AIMove.rb:367-374;006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb:1-185'),
 (109,'canHeal is queried for prediction and some local scoring guards; concrete gates differ by handler.','002_Battler/001_Battle_Battler.rb:596-600;006_AI MoveEffects/006_AI_MoveEffects_Healing.rb:1-322'),
 (240,'Generic exception statement does not supply specific omitted legal-input boundaries; two proposals preserve this scope.','005_AI/005_AI_ChooseMove.rb:54-82;001_Technical/001_Debugging/001_PBDebug.rb:4-17'),
]:
    reverse.append(dict(formal=main,line=line,clause=all_text[main][line-1],fact=fact,source=source,
                        preconditions=['Normal internal battle context; exact flags and individual local entry prerequisites retained.'],
                        verdict='SHARED_PREREQUISITE_STATIC_CHECK'))

for line,ids,fact in [
 (11,['004:220','004:238','004:1190'],'Final override and same-family missing-copy behavior separately checked.'),
 (40,[r['id'] for r in review if r['id'].startswith('004:') and r['family']=='MoveBasePower'],'Every local base-power occurrence checked; receiver-dependent copies preserve actual receiver.'),
 (42,[r['id'] for r in review if r['id'].startswith('004:') and r['family']=='MoveFailureAgainstTargetCheck'],'Distinct OHKOIce failure retained, other target-failure families exact.'),
 (44,[r['id'] for r in review if r['id'].startswith('004:') and r['family']=='MoveEffectAgainstTargetScore'],'Target preference occurrences, overwritten-copy no-write and PoisonTarget dependency separated.'),
 (46,[r['id'] for r in review if r['id'].startswith('004:') and r['family']=='MoveEffectScore'],'Both FuryCutter overall occurrences counted; only final one consumable.'),
 (48,[r['id'] for r in review if r['id'].startswith('004:') and r['family']=='MoveFailureCheck'],'Whole-failure distinct gates, not automatically imported into score bodies.'),
 (50,['004:1461'],'AuraWheel copied from RaiseUserSpeed1 overall family, with same current receiver.'),
 (54,[r['id'] for r in review if r['id'].startswith('005:') and r['family']=='MoveBasePower'],'All13 multi-hit/charge base registrations inventoried and semantically assessed.'),
 (56,[r['id'] for r in review if r['id'].startswith('005:') and r['family']=='MoveEffectAgainstTargetScore'],'All target-score occurrences checked, including defaultGeomancy NOT_ENTERED and BeatUp n0 concern.'),
 (58,['005:151','005:322'],'BeatUp eligibility and Geomancy multi-stat copied failure differ.'),
 (60,['005:450'],'SkyDrop target-failure gate inspected independently of copied Fly score.'),
 (62,['005:190','005:512'],'Recharge and Bide whole-score entries inspected individually.'),
 (66,[r['id'] for r in review if r['id'].startswith('006:') and r['family']=='MoveFailureCheck'],'All healing/sacrifice whole-failure originals and copies checked.'),
 (68,[r['id'] for r in review if r['id'].startswith('006:') and r['family']=='MoveEffectScore'],'All healing/sacrifice whole-score originals and copies checked; no PP value added to LunarDance.'),
 (70,[r['id'] for r in review if r['id'].startswith('006:') and r['family']=='MoveFailureAgainstTargetCheck'],'All healing/seed/perish target failures checked separately from scores.'),
 (72,[r['id'] for r in review if r['id'].startswith('006:') and r['family']=='MoveEffectAgainstTargetScore'],'All healing target scores checked, especially LifeDew independent guard and JungleHealing wrong-family default.'),
 (74,['006:495','006:507'],'MistyExplosion multiplier and FinalGambit fixed value separately checked.'),
 (111,[r['id'] for r in review],'Preserved default/nohandler, medium-base and scoring-flag gates; other formal effect files are parent scope.'),
]:
    reverse.append(dict(formal=coverage,line=line,clause=all_text[coverage][line-1],source_units=ids,
                        fact=fact,verdict='LOCAL_REGISTRATION_COVERAGE_NOT_RUNTIME_PASS',
                        preconditions=['Registration order and same-family source availability; common consumer route is per forward row.']))

vectors=[]
def v(id,line,ids,derivation,kind='DERIVED_VECTOR'):
    vectors.append(dict(id='BE-'+id,formal=catalog,line=line,source_units=ids.split(),
                        derivation=derivation,evidence=kind,execution='NOT_EXECUTED',
                        prerequisite='Exact catalog local-stage fixture plus forward-row flag/receiver gates; not final action guarantee.'))
v('B01',148,'004:22 004:40','round(41/2)=21;round(1/2)=1; random-level representative41.')
v('B02',149,'004:63 004:70','Higher-level fails;equal-level noSturdy gives currentHP60,notH100; accuracy separate.')
v('B03',150,'004:140','n1<2→200;n2<5→150; remaining four thresholds inspected.')
v('B04',151,'004:188','FinitePP0 excluded at actual-choice eligibility; reached medium basePP0 queries missing totalpp before power return.','STATIC_EXCEPTION_ROUTE')
v('B04b',152,'004:188','After expected deduction,PP1 index0→200,PP2 index1→80.')
v('B04c',153,'004:188','PP−1 short-circuitsPP0 guard; index−2 picks50, not a new normal-choice guarantee.')
v('B05',154,'004:215 004:220 004:238','40×2²=160;finalscore dependsEchoedVoice0/1→0/+10;oldFuryCutter score overwritten.','STATIC_OVERRIDE_ROUTE')
v('B06',155,'004:233','40×(5+1)=240; no overall score for EchoedVoice key.','APPROXIMATION_PRESERVED')
v('B07',156,'004:251','71×2=142;Grassy142/2=71;representative mean of20 actual magnitudes is71.','APPROXIMATION_PRESERVED')
v('B08',157,'004:330','ActiveFlyingGem doubles;inactiveFlyingGem with still-held item does not.')
v('B09',158,'004:276 004:278','Real sleepcount2/nonwanted−10;count1 no target-score adjustment; base query is independent.')
v('B12',161,'004:441','LuckyChant makes potentialnegative→60;ordinary nonforced damage plus normal critical stage→+15.')
v('B12b',162,'004:441','1+1+3=5;oldcapindex4 denominator2→115;newcapindex3 denominator1→60.','CONFIGURATION_VECTOR')
v('B13',163,'005:9','80×1/2=40;sub39<40 true;+10;sub40 equality false.')
v('B14',164,'005:97 005:103','25×5=125;25×31//10=77;substitute counts5/3, not3.1.','APPROXIMATION_PRESERVED')
v('B15',165,'005:119 005:128','AshGreninja20×3=60;ordinary15×31//10=46;copied target count3 absentSkillLink.','APPROXIMATION_PRESERVED')
v('B16',166,'005:151 005:162 005:171','(5+100//10)+(5+75//10)=27;empty whole-failure true if prediction on;new off-prediction/substitute boundary proposed.','STATIC_GATE_WITH_PROPOSED_GAP')
v('B17',167,'005:203','NoHerb:−10−10−20=−40;activeHerb returns input before all three branches.')
v('B18',168,'005:256 005:261','EffectiveSun skips charge;Rain retains penalties and half base;None no base halving.')
v('B19',169,'005:371','After non60 common charge,one foe hitsDig−10/without+8;known usable slots only.')
v('B20',170,'005:450','Generation6+:weight1999 passes localweight gate;2000 fails;oldgen gate absent.')
v('B21',171,'005:507 005:512','H100:h25→60;h26≤50 and≤75 gives−23;h51≤75 gives−8;fixed representative40.')
v('B22',172,'006:42','h50≥50→−10;h49→30×51//100=15.')
v('B23',173,'006:58 006:94','Sun/HarshSun+5;Rain−10 after selfheal;Roost no type-loss adjustment.')
v('B24',174,'006:166','d80 half40>30;missing60 gives20×60//100=12 and20×40//100=8;d60 half30 notstrictly>30.')
v('B25',175,'006:166 006:204','LiquidOoze targetHP40:rough39<40 penalty20;40<40false,no penalty.')
v('B26',176,'006:259','Wrong overall family LifeDew call defaultsinput;noStatus adds0,status nonwanted+10.','WRONG_FAMILY_DEFAULT')
v('B27',177,'006:280','Missing75:20×75//100=15;MegaLauncherPulseestimate75 gives15;ordinaryestimate50 gives10;foe60.')
v('B30',180,'006:470','h20/H100:base−20+lowHP20,thenownReserve0+30 orown>0/foe0+20.')
v('B32',182,'006:597','Medium1ally1highHPfoe:−15−15+20+10=0;zero affectedallies refunds15.')
v('B33',183,'006:642 006:665','Onefasterfoe,h10%:−25+7+20+10+15=27;h41%:−25+7=−18;zero fasterfoes stops−25.')
v('B43',193,'004:751','Rate3:eligiblefoe7−(3−1)×15=−23;rate4 early60.','APPROXIMATION_PRESERVED')
v('B44',194,'004:795','Independentpoisonresult15 integerhalf7; no nearest-half rounding.')
v('B45',195,'004:1084 004:1089','Knownbasepriority>0/protectable may score despite own last action;failure does not rebuild actual order.','PREDICTION_EXECUTION_SEPARATION')
v('B46',196,'004:1134','Generation6 current statusguard fails wrong currentmove-damaging gate;generation7 short-circuits that gate.','PREDICTION_APPROXIMATION')
v('B47',197,'004:1175 004:1190','Missing copy source leaves prior Feint+7 intact;BypassSubstitute target family remains absent.','STATIC_COPY_NO_WRITE')
v('B48',198,'004:1212','d100//4=25≥U25 andownReserves<=enemy→60;activeRockHead/indirectimmune returnsinput.')
v('B50',200,'004:1482 004:1487','Benefit/cost1/1 holdsinput afterpositive tie;0/1→60;slowerU predictedtargetfailure.','APPROXIMATION_PRESERVED')
v('B51',201,'006:327 006:332','ExistingpositionWishpositive→failure;withoutWish/fullHP→local−10,notfailed.')
v('B52',202,'006:349 006:354 006:365 006:370','Existingmarker→failure;AquaRing15+root5=20;earlyIngrain8+15+5=28.')
v('B53',203,'006:397 006:404','Earlymediumnodamagemove/noreserves15+10+10+8=43;activeOoze subtract20.')
v('B54',204,'006:382 006:387','Sleepcount1→60;count2→8×2=16;notviewedsleep predictsfailed.')
v('B58',208,'004:481','Allowncritpotentialnegative→60;onevulnerable permitsfoepotentialscan;safeown iterator.','STATIC_GATE')
v('B59',209,'004:611','Nofirefoe→60 discards priorpenalty;onepurefirefoe15+7=22 when ownfireabsent.')
v('B60',210,'004:1337','DirectPP0accuracy50slot adds5+8=13;not OHKOextra8 unless identityOHKO.','ENUMERATION_FILTER_DIFFERENCE')
v('B02b',211,'004:91','OwnIcefailure differs from ordinaryOHKO;nonIce delegates ordinarycondition.','STATIC_FAMILY_DIFFERENCE')
v('B61',212,'004:382 004:396','TargetAssurance+8 fromeligibleally;Revenge/Avalancheonly overall foe loop;wrong-family target call would default.','STATIC_FAMILY_DIFFERENCE')
v('B62',213,'005:322 005:324','DefaultGeomancyUser target0 excludes targethandler in all fourHP/herb fixtures;wholedefault100 exceptallstatscapped predictive20.','DEFAULT_ROUTE_NOT_ENTERED')
v('B64',220,'006:236','Predictionoff/fullHP:independentcanHealguard hold100; not95.')
v('B65',221,'006:236','h50:100+15×50//100=107;noHPcommit.')
v('B66',222,'006:236','h75:equal0.75H→100−5=95.')
v('B67',223,'006:236','LivingallyHealBlock:targetenumerationstilllegal,canHealfalse→hold100;userunblocked.')
v('B68',224,'006:231','Predictionon/fullHP→target−1 beforelocaltargetscore;wholevalidtargethandlingseparate.','NOT_ENTERED_SCORE')
v('B69',225,'006:236','Predictionoff/ScoreMovesoff→targetbodyNOT_ENTERED;100isupstreambenchmark.','NOT_ENTERED_SCORE')
v('B70',226,'006:236','h50/canHealtrue/HPAwareoff→input100;not107.')
v('B71',227,'006:231 006:236','UserHealBlockpositive→actualmovehealingeligibilityrejectsBEFOREcandidate;faintedtargetsremovedbylegalenumeration.','NOT_ENTERED_CANDIDATE')

for row in vectors:
    reverse.append(dict(formal=catalog,line=row['line'],clause=all_text[catalog][row['line']-1],
                        source_units=row['source_units'],preconditions=[row['prerequisite']],
                        fact=row['derivation'],verdict=row['evidence']))
(OUT/'vector-matrix.json').write_text(json.dumps(vectors,ensure_ascii=False,indent=2)+'\n')
(OUT/'reverse-matrix.json').write_text(json.dumps(reverse,ensure_ascii=False,indent=2)+'\n')
md=['# Reverse formal-clause matrix','',
    'Every included line is a freshly read formal clause or vector with exact source units and entry prerequisites. Main clauses whose other identities are in Misc/Stats/BattlerOther/ChangeMoveEffect remain parent-owned; this file does not approve those source bodies. Structural headings/ownership/provenance text are not runtime assertions.','',
    '| Formal line / clause | Source / unit | Preconditions / qualification | Assessment |','|---|---|---|---|']
for r in reverse:
    source=r.get('source',r.get('source_units',[]))
    if isinstance(source,list):
        source=', '.join(s['id']+f":{s['start']}-{s['end']}" if isinstance(s,dict) else s for s in source)
    fact=r.get('fact','; '.join(r.get('qualifications',[])))
    md.append(f"| {Path(r['formal']).name}:{r['line']} | {source} | {'; '.join(r['preconditions'])} {fact} | {r['verdict']} |")
(OUT/'reverse-matrix.md').write_text('\n'.join(md)+'\n')
print(f'{len(reverse)} reverse rows; {len(vectors)} individually checked local BE vectors.')
