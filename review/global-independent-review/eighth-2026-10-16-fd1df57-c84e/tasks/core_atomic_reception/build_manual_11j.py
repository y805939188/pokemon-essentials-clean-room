import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_11i.json').read_text());d=base['source_dictionary'];rows=[]
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
def head(n,s):rows.append(dict(number=n,layout_reason=s+' column heading only; no independent behavioral denominator.'))
head(916,'Weather')
row(917,[
 'W01 assumes world weather identifierStorm, mapping enabled and no battle rule override, with normal field construction.',
 'Prepare weather mapping uses GameData::Weather category, where Storm has Rain category, and sets default/current Battle Rain with duration-1.',
 'Terrain mapping separately recognizes raw worldStorm and sets default/current Electric with duration-1 when the overworld terrain setting is enabled.',
 'An explicit Misty terrain rule prevents only that terrain mapping and creates default/currentMisty-1; it does not cancel independent Rain mapping.',
 'World weather IDs/categories, battle-weather IDs and battle-terrain IDs are distinct registries and not interchangeable display strings.'
],['prepare','worldweather_full','battleweather_full','battleterrain_full','weather_core_complete','config'],'worldStorm categoryRain -> independent default Rain-1; rawStorm -> Electric-1 unless explicit terrainRuleMisty.')
row(918,[
 'W02 starts current raw Rain duration2 and attempts ordinary Rain setup with no independent earlier effects.',
 'WeatherMove failure checks current raw weather and rejects same Rain.',
 'Direct core StartWeather also returns immediately when current raw weather==requested weather.',
 'Thus neither normal same-kind path resets2 to5 or calls a rain-extending held-item handler to make8.',
 'This is current raw weather equality, not equality after CloudNine/AirLock/Umbrella effective-weather queries.'
],['weather_move_parent','weather_terrain_moves','weather_core_complete','item'],'rawRain2 -> same rawkind movefail/coreearlyreturn -> duration2 unchanged/no extension callback.')
row(919,[
 'W03 sets defaultSun duration-1 with temporaryRain duration1 before EOR weather.',
 'The early weather stage decrements1to0, gives Rain-end feedback and changes current weather toNone.',
 'It then restores nonNone defaultSun through StartWeather with fixedDuration=false, producing currentSun/-1.',
 'The remainder of that weather helper and later weather consumers use current effectiveSun, not the expiredRain.',
 'This default is a separately stored value, not a stack automatically restoring the most recent arbitrary temporary weather.'
],['eor','weather_core_complete','battlerfull'],'Rain1to0/end -> currentNone -> defaultSun core -1 -> subsequent effectiveSun.')
row(920,[
 'W04 has storedSandstorm duration2 and an actual active living CloudNine/AirLock source, with ordinary160HP members.',
 'Stored weather countdown still changes2to1 and current-weather continuation feedback can occur.',
 'Battle.pbWeather returnsNone because the active suppressor is found; member effectiveWeather consequentlyNone.',
 'Sandstorm damage helper therefore does not apply the nominal160/16=10 to those members under this suppression.',
 'When that source loses active eligibility, effectiveSandstorm can resume from the remaining raw weather/duration; no weather setter/refresh is inherently required.',
 'A stored but fainted/suppressed ability does not satisfy the active living source premise.'
],['eor','weather_core_complete','battlerfull','ability_item'],'rawSand2to1 -> active suppressor effectiveNone -> nodamage; source losesactive -> raw remaining weather visible.')
row(921,[
 'W05 has current rawHeavyRain with an active suppressor making effective weatherNone.',
 'The ordinary Sun move parent still tests stored field.weather in the primordial-weather prohibition.',
 'Thus it fails on rawHeavyRain despite effective suppression and does not replace it withSun.',
 'CloudNine suppression is not erasure of raw storage or permission to bypass a setter gate defined on raw weather.'
],['weather_move_parent','weather_terrain_moves','weather_core_complete','battlerfull'],'rawHeavyRain gate -> normal Sunfail even effectiveNone; no raw replacement.')
row(922,[
 'W06 has currentHarshSun different from default and no remaining eligible active DesolateLand source after departure.',
 'EndPrimordialWeather detects that current/default differ, searches living active matching sources and clears current when none qualifies.',
 'With defaultRain it starts that default with indefinite-1; with defaultNone it remainsNone after the end notification/forms.',
 'If HarshSun itself equals the default, the initial current==default return exempts it from this termination, even without a current ability source.',
 'Actual withdrawal/fainting and ability-active conditions determine when that helper observes the source absent; native animations/messages remain unexecuted.'
],['weather_core_complete','ability_item','switching','b_change','battlerfull'],'current!=default +lastactive sourcegone -> clearprimal -> defaultRain-1/None; equalityexemption separate.')
row(923,[
 'W07 has battle effectiveSun with one actual active UtilityUmbrella holder and another ordinary member.',
 'The holder member effectiveWeather returnsNone for Sun/Rain/HarshSun/HeavyRain, while the nonholder still returnsSun.',
 'Battle.pbWeather itself remainsSun; the item does not globally suppress or clear raw weather.',
 'Sandstorm is outside that umbrella mask, so an active umbrella does not make memberSandstormNone by this query.',
 'Item-active guards still matter: merely storing the Umbrella ID under Klutz/Embargo/MagicRoom/etc does not establish this effect.'
],['battlerfull','weather_core_complete','ability_item','item'],'battleSun -> per-member activeUmbrella maskNone vs otherSun; raw/global and Sandstorm unchanged.')
head(924,'Terrain')
row(925,[
 'T01 has current temporaryGrassy duration1 and a living affected healable member with totalHP160 and at least10 missingHP.',
 'The earlier healing phase recovers integer160/16=10, subject to normal HP cap/write-through.',
 'Only later EndTerrain decrements1to0 and ends/restores terrain as applicable.',
 'It does not expire before the current round terrain heal by analogy with the earlier weather phase.',
 'Fainted, airborne/semi-invulnerable or nonhealable members do not meet the stated effect gate.'
],['eor','battlerfull','b_change','weather_core_complete'],'early affected/healableGrassy ->10HP -> later duration1to0; weather timing not substituted.')
row(926,[
 'T02 has defaultGrassy and current temporaryElectric duration1 naturally reaching terrain expiration with normal callbacks.',
 'EndTerrain decrements1to0, emits expiry feedback and sets currentNone before its initial ability wave.',
 'Default restoration StartTerrain(Grassy,fixed=false) writesGrassy/-1 and runs an ability wave then an item wave.',
 'The caller then performs its own remaining ability and item waves, giving three ability batches and two item batches in total.',
 'Each actual ability/item helper still filters active/correct terrain/other prerequisites and a consumed item can cease applying; batch count is not guaranteed repeated effect count.',
 'An exception in an earlier wave can prevent later waves while leaving current/default/duration changes already committed.'
],['eor','weather_core_complete','ability_item','item','abilityeffects'],'naturalElectric1to0/None -> ability1 -> restoreGrassy-1 ability2/item1 -> ability3/item2, actualeffects gated.')
row(927,[
 'T03 sets defaultGrassy/currentElectric duration2 and a successfully reached SteelRoller direct removal.',
 'SteelRoller writes only current terrainNone, retaining duration2 and defaultGrassy.',
 'Subsequent EndTerrain invocations decrement that positive duration2to1to0.',
 'Because current terrain isNone, the nonNone-expiry branch does not execute at0, so there is no default restoration or natural-expiry ability/item wave from that branch.',
 'This direct-removal path is distinct from StartTerrain and natural expiration; other unrelated later producers remain outside the fixture.'
],['misc_full','eor','weather_core_complete'],'SteelRoller currentNone only -> remaining counter2/1/0 -> no nonNone expiry/default chain.')
row(928,[
 'T04 first supplies a Flying-type member with genuinely active IronBall and no separate remaining airborne/semi-invulnerable condition.',
 'airborne? checks activeIronBall before Flying/Levitate/Balloon etc and returnsfalse, permitting terrain qualification if not semi-invulnerable.',
 'The independent grounded but semi-invulnerable member is rejected by the second affectedByTerrain? check.',
 'Type-only Flying/nonFlying classification therefore cannot replace the complete active-item/grounding/semi-invulnerability predicate.',
 'KS-TERRAINQUERY complete definition ends516; the mandatory499–516 closure companion preserves its correct actual source scope.'
],['battlerfull','ability_item','weather_core_complete'],'activeIronBall -> grounded -> !semi gate; independent groundedsemi -> reject terrain.')
head(929,'Global-field')
row(930,[
 'F01 begins Gravity0 and reaches the normal successful Gravity producer.',
 'It sets the global Gravity counter5 and then scans current living battlers.',
 'For the named three sky TwoTurn functions it clears the charge/currentMove and clears that battler choice only when not already moved; unrelated underground/underwater semi-invulnerability is not generically cleared by this sky list.',
 'The producer also clears MagnetRise, Telekinesis and SkyDrop states under their actual conditions, with grounded feedback only for an affected battler.',
 'A repeat while Gravity>0 fails without refreshing5.',
 'Selection predicates, current airborne queries and actual affected battler list remain separate consumers rather than assuming every field object is grounded identically.'
],['gravity_producer','battlerfull','priority','b_init','eor'],'Gravity0 ->5 -> exact sky/levitation/drop state and conditional choice clears; positive-repeat fail/no refresh.')
row(931,[
 'F02 supplies one corresponding TrickRoom/WonderRoom/MagicRoom move while that room counter2.',
 'Each producer toggles its own positive counter directly to0 rather than restarting5.',
 'The independent natural MagicRoom countdown2to1to0 invokes terrain held-item stat checks when it expires.',
 'Its direct toggle-off producer has no identical explicit terrain-item notification at that site; later unrelated normal callbacks may still check items.',
 'TrickRoom ordering, WonderRoom raw defensive getters and MagicRoom itemActive suppression retain their own actual readers and are not three names for one shared effect.'
],['switch_effects_full','wonderroom_producer','magicroom_producer','eor','battlerfull','ability_item'],'roompositive -> direct0; natural MagicRoomcounter expiry includes itemterrain check absent from direct producer.')
row(932,[
 'F03 uses new-style global WaterSport counter5 and then replaces its creator.',
 'Ordinary battler replacement does not clear the global field counter, so it remains5 until its reached EOR decrement.',
 'The old-style member WaterSporttrue is stored on the battler and normal InitEffects clears it during replacement.',
 'Damage multiplier code has separate global/member guards, so clearing the old member does not justify clearing all global sport effects.',
 'The generation configuration chooses which producer scope is used; this control does not assert both producers normally set the same field simultaneously.'
],['sport_ion_producers','b_init','activefield_full','eor','calculations','b_settings'],'generation producer scope -> globalcounter survivescreatorreplacement vs oldmemberflag Initfalse -> independent damage consumers.')
head(933,'Side-effect')
row(934,[
 'S01 compares currentReflect5 repeat, activeLightClay newLightScreen, and already createdAuroraVeil followed by Hail ending.',
 'Reflect producer rejects a positive existing counter without refreshing it.',
 'A successful newLightScreen uses current activeLightClay to establish8 instead of ordinary5.',
 'AuroraVeil requires its actual user effectiveHail for establishment, but later Hail loss does not itself clear the already stored side counter.',
 'Its subsequent duration expires through its own side EOR countdown; no ongoing Hail predicate is added to the stored screen existence.',
 'Actual screen damage reduction still has critical/ignore/activeInfiltrator/move-category/side-count gates separately reviewed.'
],['screens_lucky_producers','eor','calculations','battlerfull'],'positiveReflectfail; activeClay newLightScreen8; establishVeilHailonly -> independent sidecountdown afterward.')
row(935,[
 'S02 starts SeaOfFire4 with an alive nonFire indirect-damage-eligible member totalHP160 and both local phases normally reached.',
 'Early helper decrements4to3 then applies integer160/8=20 effect damage.',
 'Later side-countdown decrements3to2; next complete round repeats2to1/damage20 then1to0/expiry feedback.',
 'Fire typing or activeMagicGuard control prevents damage via actual eligibility while the side counter still advances.',
 'HP floors/caps/healing/faint callbacks can change actual lostHP if fixtureconditions differ; nominal20 is the controlled ordinary result.'
],['eor','battlerfull','b_change','abilityeffects'],'side4->3/20damage->2; next2->1/20->0; damage immunity does not stopcounter.')
row(936,[
 'S03 starts SeaOfFire1 and reaches the early helper, which decrements1to0 then skips damage.',
 'Later side countdown checks<=0 and returns, so it neither decrements again nor emits that later expiry message.',
 'This differs from starting2, whose early decrement1 allows damage and later decrement0 gives the normal end feedback.',
 'No blanket one-tick-per-round or always-end-message contract replaces this ordered source behavior.'
],['eor'],'SeaFire1 -> early0/nodamage -> later<=0return/noendmessage.')
row(937,[
 'S04 supplies ownSpikes2, opposingLightScreen3 and opposingLuckyChant4 before successful CourtChange.',
 'CourtChange swaps its explicit selected effect list between side arrays, including Spikes and LightScreen.',
 'Thus the two supplied values2/3 move across sides exactly as stored, not reset to default layers/durations.',
 'LuckyChant is not in the selected list and its4 remains on the original side.',
 'Other excluded flags/counters likewise are not justified as cleared/swapped merely because they are side effects; per-ID list remains decisive.'
],['misc_full','activefield_full','eor'],'explicit CourtChange list -> swapvalues Spikes2/LightScreen3; excludedLuckyChant4 stays.')
row(938,[
 'S05 begins own EchoedVoiceCounter2 and Usedfalse, then one successful usage-counter update.',
 'The first use increments counter3 subject to cap5 and setsUsedtrue.',
 'A second same-side use while Usedtrue does not increment again, leaving3.',
 'Normal EOR tail preserves the nonzero counter when Usedtrue, then clearsUsedfalse.',
 'A following round with no relevant use reaches tail with Usedfalse and resets counter0.',
 'An early EOR return before that tail does not imply either reset; base-power consumption is a separate actual counter reader.'
],['echo_retaliate_producers','eor','use'],'first update2to3/Usedtrue -> second noinc -> reachedtail keep3/clearUsed -> unusednexttail0.')
row(939,[
 'S06 is generation8 QuickGuard/WideGuard with its side flagfalse, ProtectRate9 and no other eligible unmoved UseMove/Shift even if item/switch choices remain.',
 'The sidedEffect generation>=6 branch skips the consecutive protection random test, so ProtectRate9 does not itself cause a draw.',
 'The independent last-in-round helper still finds no other qualified action and fails.',
 'That failure sets ProtectRate1 and returns before EffectGeneral, leaving the side flagfalse.',
 'Being present in battlers or having any nonmove command is not a substitute for that precise pending UseMove/Shift predicate.'
],['protect_parent_complete','side_protect_producers','usagefull','attack','b_settings'],'sidedgen8 -> no consecutiveRNG -> last-action failure -> rate1/no sideflag.')
row(940,[
 'S07 changes only S06 to have another qualified living unmoved UseMove/Shift and all other front gates passing.',
 'It still skips the sided gen8 consecutive random draw.',
 'The last-action helper now permits normal EffectGeneral, which sets the selected side flagtrue.',
 'ProtectRate is multiplied by gen>=6 factor3, giving9to27 before protection feedback.',
 'A later presentation error can leave flagtrue/rate27; existing-object count alone did not establish eligibility.'
],['protect_parent_complete','side_protect_producers','usagefull','attack','b_settings'],'other qualified pendingaction -> noRNG -> sideflagtrue -> rate9*3=27 -> feedback.')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_11j.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows),'layout',sum('layout_reason'in x for x in rows))
