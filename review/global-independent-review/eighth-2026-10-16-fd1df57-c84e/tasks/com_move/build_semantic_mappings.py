from pathlib import Path
import json,datetime
B=Path(__file__).resolve().parent
N=json.loads((B/'semantic-notes.json').read_text());D=json.loads((B/'dependency-facts.json').read_text())
G=[]
def add(id,formal,location,evidence,assertions,premise='Frozen B8/R, actual normal entry and callbacks unless a different entry or failure prefix is specified.',status='SUPPORTED_SOURCE_STATIC'):
 G.append({'id':id,'formal':formal,'clause':location,'reviewer':'/root/com_move','premise':premise,'status':status,'source_fact_keys':evidence,'subassertions':[{'id':f'{id}.{i+1:02}','assertion':s,'verification':'Read source behavior and compared this finite assertion, including stated entry and failure boundary.'} for i,s in enumerate(assertions)]})
add('M43-INPUT','wp43-types-accuracy-and-damage.md','§§1–2',['R001','R003','Battler001','Battler003','DebugStats'],[
'Combat reads current battle level and five ability values, independently of persistent IV/EV recomputation.',
'Physical/special uses per-move category when enabled, otherwise calculated/base type; missing type is physical, while status classification remains category based.',
'Wonder Room swaps defense getter values, while labels of defense stages and raw writers remain separate.',
'Debug stat submenu snapshots getters, writes the chosen raw field, and updates its cached item only. Defense300 while room active leaves getterDefense200/getterSpDef300; reopening resnapshots. SpDef400 produces getterDefense400/getterSpDef100. No-room controls read/write same names.',
'Current types deduplicate, remove BurnUp Fire, remove Roost Flying and add Normal if empty, then optionally include unique extra type.',
'Display type/damage/category/accuracy delegate persistent move data except Morpeko battle display type; commented dynamic display calculations do not run.',
'Calculated damage, planned per-hit loss, cumulative loss, miss/protection/absorption and actual HP submission are separate state facts.',
'Accuracy calculation can consume Micle marker and invoke item handlers; it is not a pure read, and later failure does not refund earlier PP.' ])
add('M43-FALLBACK','wp43-types-accuracy-and-damage.md','§2.1',['R001','R004','R005'],[
'Factory nil function becomes None; a legal unresolved function implementation produces Unimplemented.',
'Unimplemented status fails at own whole-move gate; valid damaging category continues ordinary damage with no missing special main/additional behavior.',
'Unknown content ID, illegal constant query string, empty string, or plugin registration lies outside the finite nil/valid-name guarantee.',
'Ordinary PP/history precede this gate, so unknown-status failure retains them; None default POUND remains ordinary known behavior.',
'Optional SHADOWSHED RemoveAllScreens has no identically named implementation and fails if validly enabled; the differently named AndSafeguard implementation cannot substitute for its binding.' ])
add('M43-TYPE','wp43-types-accuracy-and-damage.md','§3',['R003','R007','Battler001','TypeData','TypePBS'],[
'Base type and active user modifier precede IonDeluge Normal→Electric and Electrify→Electric; these field/user changes require registered Electric and clear prior ability powerBoost.',
'Nil attack type is neutral and has no STAB; defender data defines each attacking type weakness2/resistance1/2/immunity0, with conflict priority weakness then resistance then immunity.',
'Normal combination multiplies every current complete defender type and includes TarShot Fire×2; empty defender types stay neutral.',
'RingTarget restores any immune single contribution; Scrappy/Foresight restore immune Ghost and MiracleEye immune Dark.',
'StrongWinds neutralizes only super-effective Flying contribution; grounded Flying becomes Ground-neutral.',
'Ground against current Flying with active IronBall returns whole neutral before any other defender type; this differs from ordinary grounded multiplication.',
'Shadow attack uses target shadow identity:1/2 for shadow and2 otherwise, bypasses ordinary types and TarShot.',
'Ordinary damaging type immunity rejects in successful-target gate before core minimum1; status moves do not universally obey ordinary type immunity.',
'FreezeDry Water contribution2, FlyingPress additional Flying base contribution, ThousandArrows Ground/Flying neutral and SkyDrop Flying whole immunity remain distinct overrides.' ])
add('M43-ACC','wp43-types-accuracy-and-damage.md','§4',['R003','R007','Clauses','Battler001','AbilityAccuracy'],[
'Target eligibility/protection/immunity precede per-hit accuracy. Charging, LockOn, move per-hit overrides are distinct earlier returns.',
'NoGuard permits semi-invulnerability at per-hit gate; target NoGuard ordinary accuracy handler remains MoldBreaker gated. SkipAccuracy cannot repair a prior invulnerability failure.',
'Telekinesis, trampled Minimize generation6, and base accuracy0 return before modifier gathering; newly zero accuracy after gathering retains already consumed flags.',
'Gathering order user ability, user allies, target ability unless MoldBreaker, user item, target item, Gravity5/3, Micle1.2 with flagclear, positive evasion removal.',
'Accuracy/evasion stages each clamp±6, each percent separately round after own multipliers, evasion minimum1. Integer base threshold is integer quotient, strict r0..99<threshold, no threshold100 clamp.',
'Affection target-owned internal targetlevel5 nonMega changes comparison to threshold−10 and marks only failures inside the original threshold.',
'Thunder/Hurricane query target effective sunny50/rain0; Blizzard effectiveHail0; UtilityUmbrella can hide sunny/rain weather.',
'OHKO uses its own level-difference threshold and level/Sturdy guards, Ice user exception−10. After default Clauses loading OHKOIce false clause uses parent alias without Ice-target rejection; clause true rejects. AI independent Ice rejection is not actual move entry.',
'NoGuard counterexample MoldBreaker user, active NoGuard target, q70 and no earlyhit guards retains threshold70:69hits,70misses.' ])
add('M43-CRIT','wp43-types-accuracy-and-damage.md','§5',['R001','R003','AbilityCritical'],[
'LuckyChant denies before user/target ability and user/target item stages; negative stage stops later collection and denies.',
'Move override follows denial; then >50 marker/LaserFocus, highcrit1,FocusEnergy,HyperMode with originalShadow type1.',
'New ratios24/8/2/1;old16/8/4/3/2;highstages clamp. Ratio1 directly true without random.',
'Otherwise random0 true; random1 also true only affection enabled/internal/playeruserlevel5 and target notMega; marks affection critical.',
'Each hit recalculates critical after per-hit reset; new damagecrit1.5 vsold2 independent switch; central denial is not bypassed by forced move crit.' ])
add('M43-DAMAGE','wp43-types-accuracy-and-damage.md','§6',['R003','Battler001','R009','R007','R004'],[
'Default physical currentAttack/Defense and specialSpAtk/SpDef with respective stage fractions floor; critical ignores only unfavorable attacknegative/defensepositive.',
'Target Unaware unless MoldBreaker suppresses attack stage; user Unaware suppresses defense stage. Alternate getters replace numeric/stage inputs without changing actual user/target identities.',
'Status skips; Disguise/IceFace normal core sets1 and returns before crit and random.',
'Power/Attack/Defense multiplied independently, each round then minimum1; coefficient floor(2L/5+2); product/divDefense floor,div50floor,+2; final multiplier round minimum1.',
'No per-final-multiplier rounding, maxHP cap or ordinary fixed damagecap is inserted. Valid direct core0 effectiveness can clamp1, ordinary eligibility already rejects immune targets.',
'Aura4/3 orAuraBreak3/4 precedes user ability, userally/target unlessMoldBreaker, nonignorabletarget, targetally unlessMoldBreaker, useritem,targetitem.',
'ParentalBond second power÷4gen7else÷2;MeFirst/help1.5 exceptConfusionhelp,ChargeElectric2;both sport sources independently÷3.',
'Terrain power on affecteduser Electric/Grass/Psychic1.3gen8else1.5, MistyDragon on affectedtarget÷2;badge1.1internalplayer threshold999.',
'Spread target list length>1 final.75 even another target unaffected;user effective sunny/rain type1.5orhalf,SandRock special defense1.5 exceptPsyshock,ShadowSkyShadow1.5.',
'Critical then85..100 variance exceptConfusion,STAB1.5orAdaptability2,typeMod,burnphysicalhalfunlessGuts/moveexception;wall noncrit/noInfiltrator priorityAurora thenReflect/LightScreen and alive-side count2/3orhalf.',
'Minimize trample damage2 has no generation6 gate; move-specific power then final multipliers come last.' ])
add('M43-HP','wp43-types-accuracy-and-damage.md','§7',['R002','R003','R004','R015','Battler003'],[
'Whole-use reset clears cumulative and initial flags; per-hit reset retains already selected effectiveness and whole-use failure state.',
'Other-user unignored Substitute has first absorption priority and clips loss to substitute HP; cumulative loss can include substitute, real HP remains.',
'Normal Disguise/IceFace direct plannedHP0, normalcalc1;Mimikyubust gen8 additionallyfloorTotal/8 andformchange;IceFaceformchange.',
'Lethal normal loss first clipscurrentHP thennonlethal/Endure leave1 regardlessfull;Sturdy/Sash/Band10%/affection allsharefullHP gate.',
'Affection survival probabilities0/0/0/10/15/25 forlevels0..5 requireenabled/internal/player/nonMega. Sashconsumed in subsequent survivalmessage, Bandretained.',
'HP submission onlypositive real loss orSubstitute durability;calculated damage alone neithercommits nor proves animation.',
'Fixeddamage max1 criticalfalse skipsnormalformula butretainseligibilityabsorptionandHPsurvival. Confusiontypelessphysical40 no crit/variance,otheractualcoremodifiersremain. Struggletypelessphysical50,q0,normalstatusentry.',
'ShieldDust additionalchance0 first;positive explicit chance else data;>100preserved;GraceORRainbowdoubleonce withenvironmentgenerationexception;debugCtrl100 after. Extra flinch excludesnativeflinch,ShieldDust then10/20,callerfaint/substgates.' ])
add('M43-DATA','wp43-types-accuracy-and-damage.md','§§8–12',['BattleSettings','MoveData','TypeData','TypePBS'],[
'Default generation8,permove/newcrit/moretypestrue,affectionfalse,badge999 independently configured.',
'Type validnewID defaultsUnnamed/icon0/specialfalse/pseudofalse;Move explicitregisteredNormal omittedNameDescriptionPriorityEffectChanceFlags defaultsUnnamed/???/0/0/empty.',
'Move omittedCategoryPower meansStatus0 subjectcompilercombinationvalidation;typeNone/accuracy100/PP5/targetNone/functionNone defaults remain separate.',
'Currenttypes18normal+QMARKSpseudo neutral;Shadowoptional doesnotnegateexistingShadoweffects. POUND/TACKLE,AuraSphere,Thunder,Toxic stated data samples are fixed dataset facts, not allversionguarantee.',
'TD01–26 are static designs, no runtimeclaim;floatingextremehandlers/plugins/mediaremain excluded and externaldomains retain theirprimary.' ])
add('M44-STATE','wp44-statuses-stat-stages-and-immunities.md','§2',['Battler001','Battler004','Battler002'],[
'Five durablestatuses plusNone,onefield;toxic isPoison+count,notaseparateID;stateseparatecountwritesreflecttopersistentPokemon.',
'Sleep/poison setter doesnotautomaticallyzeroexistingcount;otherstatusesdo. LeavingSleep resetsTruant;poisonToxiccounterconditionsdistinctfromdurabletoxicflag.',
'Confusioncounter,Attractsource−1,Flinchboolean andsevenbattle-onlystages±6excludeHPareseparate domains.',
'ComatoseKomala cancountassleep/anywithrawNone andcannotcureabilitybycuringrawstatus.',
'Queryinputs user/move/self/substitute/status/abilities/item/field/rules/message separate eligibilityfrompresentation.' ])
add('M44-QUERY','wp44-statuses-stat-stages-and-immunities.md','§3.1–3.2',['Battler004','Clauses','AbilityStatuses'],[
'Genericquery order faint/samestatus/otherstatus/substitute/freezeweather/terrain/uproar/type/ability/Safeguard withspecifiedselfreplacementexception.',
'Nilsourceisnotself;selfsourcewithmove canreplaceotherstatus;ignoreStatus bypassesexistingstate butnototherguards.',
'Freeze sunnydenied;affectedElectricdeniesSleep,Mistydeniesstatus;UproarSleep exceptSoundproofonlywhennotMoldBreaker.',
'Poison/Steel immunitycanCorrosionbypass;Fireburn,moretypesElectricparalysis,Icefreeze;noTypeSleepimmunity.',
'Nonignorable abilityhandler queriedfirstwithoutordinaryactivegate;thenactiveown/allyunlessselforMoldBreakerfalse. Safeguardonlynonself+move,Infiltratorbypass.',
'FlowerVeilGrass,Immunity/PastelVeilPoison,Insomnia/SweetVeil/VitalSpiritSleep,LeafGuard sunny,LimberParalysis,MagmaArmorFrozen,WaterVeil/WaterBubbleBurn;nonignorableKomalaComatose/Miniorform<7;alliedFlower/Pastel/Sweet.',
'Synchronizepoison/burn/paralysis requiresrawNone/alive,terrain/types/nonignorable/own/ally/Safeguard,omitsSubstituteandMoldBreakerbypass;reflectcommitnilorigsourcepreventsrecursion,toxicbooleancopied.',
'YawnexpiryrawNone+Electric/Misty+Uproar/Soundproof+abilities+Safeguard,outeralivegate;nosource/Substitute,additionalclauseswrapper.',
'Rest rejectsasleepview,queries selfsleep ignoreexisting then fullHPfail;commitduration3 EarlyBirdhalf. Orbselfnomove bypassesSubstitute/Safeguard butotherguardsremain.',
'Sleep/freeze clauses scanrawsame-sideparty nonEggincludingfaint,onlyspecialwrappers;PsychoShift genericquerydoesnotinherittheseclauses;modifiedSleepalsoappliesself,sleepordinarynotself;evadeclauseonlynondamageDoubleTeam/Minimize.' ])
add('M44-COMMIT','wp44-statuses-stat-stages-and-immunities.md','§3.3',['Battler004','Battler001','R007','AbilityStatuses','ItemStatuses'],[
'Commitdoesnotrequery:state,count,Toxic0,animation/message,form,onstatusability,itemcure,abilitycure,thenifstillSleepcancelOutrage/currentmove.',
'Statusmaybecuredonreturn;ordinarypurestatusqueryearlierthencommit;damagingadditionalexcludesSubstituteandqueriesagain;compositesallowcomponentpartialsuccess.',
'CureviaNONEwriter resetsrelatedcount/flagsanddurablefield;messageusesoldrawstatus;repeatno-statuswritehasno5statuscuremessage.',
'Confusioncureonlycounter0,Attractcureonlysource−1;ordinaryitemcurefaint/activegate,explicititemusesforcedbranch;abilitycureactivegate;immediatecuredoesnoteraseprevioussubmissionreactions.' ])
add('M44-LIFECYCLE','wp44-statuses-stat-stages-and-immunities.md','§4',['Battler004','Battler002','Battler003','EOR','R006'],[
'Sleepdefault2/3/4equalorpositiveexplicit,EarlyBirdfloorhalf;usepoststage decrementfirst,zeroawakeelseifnotusableasleepfail;earlierfailuredoesnotdecrement.',
'ToxiccountpositiveincrementsbattleToxiccountercap16beforePoisonHeal/MagicGuard;ordinaryPoisoncount0doesnotincrement. PoisonfloorH/8,toxicfloorH*counter/16,PoisonHealH/8.',
'Burnnoownactionrandom;gen7damagefloorH/16else/8,Heatproofroundhalf;positivealiveReduceHPminimum1,poisonloopbeforeburn.',
'Paralysis25%atpoststage,speedhalfgen7elsequarterunlessQuickFeet;queuealreadydoneactionsnotreversed.',
'Frozen20%thaworstop,thawsuserflagallowedearlierwithlaterthawcommit;targetfire/gen6thawuserdamagemovescanthawafternormalhitgates.',
'Confusionnew2..5;queryguardsstated;poststage--thenzeroendelse33%gen7/50%oldselfdamage;earlierSleepfailuredoesnotprogress.',
'Attractvalidoppositesexliving/source,own/alliedAroma/ObliviousunderMoldBreakergate;querynoSubstitute/Safeguard;DestinyKnotrequeryreverse,bothcures;action50%.',
'FlinchInnerFocusguardunlessMoldBreaker,actionfailureatflag,tailclear;Yawn2expiresrequeryandstays0onfailure.',
'FocusEnergy2duplicate>=2fail,persistentuntilinit/Baton;LaserFocus2tail--andBatonpositive→2.',
'Charge2build;tailpositive--,actioncleanupclearsexact1beforeInstruct/Dancer regardlessElectric/miss;earlierinterruptionretainsnot-yetwrittenvalue.',
'DefenseCurl/MinimizeflagsandRageonlyestablish;RageopposinghitandlivingeligibleAttack1;attackstartselectotherfunctionclearsRage.',
'NonBatoninitresetseven+namedflags;Batonretainsdeclaredlistnotstatuscopy;Attractcrossrefs,Flinch/Yawn/Toxicnotretained. Faintformal resetsstatusandtemporaryeffects;ordinaryswitchdoesnotcurepermanentstatus.',
'Affectionselfcurebeforepoison/burn requiresenabled/internal/playeralive/rawnonNone/level>=4/nonMega,random>=80;defaultoff.' ])
add('M44-STAGES','wp44-statuses-stat-stages-and-immunities.md','§5',['Battler005','R004','R006'],[
'Raisequeryfaint/ContraryredirectunlessignoredMoldBreaker/max;Lowerqueryfaint/Contrary/MirrorArmorearlytrue/sourceotherguards/min.',
'MirrorArmorquerytrue doesnotguaranteesourcecanlower;reflectionsourcequerynomoveanddisabledreflectionsoSubstituteonrecipientcanreject.',
'BasicchangesContrarythenSimpleunlessMoldBreaker,clipremaining±6,positiveonlywriteactualdirectionflags,downalsoStatsDropped;returnsactualquantity.',
'Ordinary/causecommitdoesnotuniformlyrecheckfaint/Substitute/Mist/immunities,0false/noanimation,successfulchangefeedbackmagnitude1/2/3+thenabilityreaction.',
'Abilitywrappersqueryandoptionalcontact,IntimidateSubstitutebeforeContrary,gen8fourimmunitiesbeforeordinaryquery.',
'Directswap/copy/invert/resetdoesnotnormalboostmultiplierorordinaryprotection/reactions;itsownwritesdirectionflags. Illegalnegative/unknownstatnotpromisedrepair.',
'Multiple-targetdropandVenomDrench ownMirrorArmorprecheckhasnoMoldBreakergate:requiresatleastonetargetnotmin/sourcecanlowerwithreflectdisabled,elseabandonwholegroup.',
'WithMoldBreaker targetMirrorArmorAttack/SpAtk0,sourceboth−6 precheckfailsbothunchanged;source0passesandtarget−1/−1withoutreflection;ordinarysingledropdoesnotprecheck.' ])
add('M44-EFFECTS','wp44-statuses-stat-stages-and-immunities.md','§6',['R007','R006','R004','Clauses'],[
'Status31catalogdirectsleep/poison/burn/paralysis/freeze/confuse/statusadditionalandnotSubstitutequalification verified eachfamily.',
'DarkVoidDarkrai/TransformSpecies gate;RelicSonghits>0,alive,nonTransform,Meloetta,notSheerForcepositiveaddl thenformtoggle.',
'Toxictoxic1andPoisonstatusmoretypesperhitsuccessoverridecannotbypassstatuseligibility;ThunderWavequeriesattackimmunitybeforeparalysis.',
'ToxicThreadpoisonorlowspeedvalid,eachsubmit;fanginternalchance10conditionstatusquerybeforefirstdraw,separateflinchdrawthenInnerFocuscommit,outer101chanceindependent.',
'TriAttackchoosesoneof3noretry;Jealousyreadsroundraisedflagnotcurrentstagepositive.',
'PsychoShiftrawuserstatusrequired,targetgenericqualifier,targetcommitandcuresbeforeusercure,sleepfreshduration,toxicbooleannotcount;SleepTalksimplecallretainsouterSleep/PPanddoesnotspendoriginalPsychoShiftPP.',
'Refreshonlytoxic/burn/paralysisraw;SparklingAriafaint/substitute/rawBurngates.',
'Aromatherapy/HealBellactiveSideandableinactivepartyincludepartner,activeexcludedfrombackup;UserSideeffectdirectactiveiterationvsnormalUserAndAlliestargetqualification.',
'Snoreasleepview,FakeOutturnCount<=1,Twisterspecificskybase2,AttractstatusignoresSubstitutebutadditionalstilldoesnot;Yawnexistingpositivefails.' ])
add('M44-K','wp44-statuses-stat-stages-and-immunities.md','§7–7.1 + coverage §§2.1–2.5',['R006','R004','Battler005'],[
'65ordinaryparametersactualsequencesmatch114identitycoverage;ShiftGearSpeed2→Attack1,VCreateSpeed−1→Defense−1→SpDef−1;ordinarypartialsuccessnotrollback,selfdropopponentallfaintedskip.',
'FellStinger2/3requiresdamageStatefainted;BellyDrumcostmax(floorH/2,1),HPstrictgreater,querythenlossdirectAttack±6andflags,itemheal;ClangorousSoulfivebooststhenfloorH/3cost.',
'K01DefenseCurlflagthenDef1;K02Charge2thenSpDef1;K03Autotomizecomparescurrentweight+storedchange>1thenstored−1000beforeSpeed2;K04MinimizeflagthenEva2,allpurestatusstillordinaryboostfailuregate.',
'K05FocusEnergydirect2;K06Growthstartsunny2else1attackthenSpAtk;K07NoRetreatfiveAttack/Defense/SpAtk/SpDef/Speed1thenflagonlynotalreadytrapped,ownflagpreventsrepeat;K08Rageonlyflagthenlaterattackboost.',
'K09targetAttack1aggregateandtargetqueriesonlystatus,additionalrequeries;K10SpDef1ignoreSubstitute;K11DecorateAttack2thenSpAtk2eachrequery;K12PlayNiceignoreSubstituteonlynotallimmunity.',
'K13GravAppleintegerP*3/2floorbeforemodifiers,81→121;K14Captivategender/Obliviousspecialgatesandordinarydrop,notfullAttract;K15BulldozeGrassyrawP/2round,61→31withoutgroundedgate;K16TarShotnewflagallowsevennodrop,attemptdropthenflag,existingflagordinarygate.',
'K17ShellSmashDef−1,SpDef−1,Attack2,SpAtk2,Speed2eachquery/partial;separatefirstsuccessfulanimationfordown/upgroups.',
'K18CoachingsamesideexcludesU,Attack1thenDefense1;K19PlusMinusAttack1thenSpAtk1;K20PlusMinusDefense1thenSpDef1,canincludeU,activeabilityrequiredandanyboost;UserSidedirectpooliterationwithoutordinarytargetchecks.',
'K21RototillerbothsidesGrassnotairborne/notsemiAttack1→SpAtk1;K22FlowerShieldGrassnotsemiDefense1includingairborne,bothrequireeligiblepoolnotemptyandactualtargetguards.',
'SwapsAttack/SpAtk,Defense/SpDef,allsevenandPsychUpcopydirectdirectionflags;newcritPsychUpcopiesFocus/Laser;SpectralThieftriesreceivepositivethenzeroestargetevenifuserfullbeforecalcdamage.',
'Invertrequiresalteredthennegates;ClearSmogcalc>0/nonsub/alteredreset;Hazeanyalteredelsefailallreset;rawPowerTrick/SpeedSwap/PowerSplit/GuardSplitbelongWP47A,PainSplitWP46,Mist/Tailwind/WonderRoomWP45withoutmiscounting114.' ])
add('M44-BOUNDARY','wp44-statuses-stat-stages-and-immunities.md','§§8–11 + coverage §§3–4',['R006','R007','Battler001','EOR'],[
'Speedstageintegerfirstthenability/item/Tailwind/Swamp/paralysis/badgefinalroundmin1,faintspeed1;escapeusesdifferentrawspeed.',
'Roundraised/loweredflagsaretemporaryandtailclear;HP/statusdurableviawriters,stagesnotdurable. AllEORclaimsrequireactualreachoflocalconsumerandearlierterminalreturnsexcluded.',
'Defaultgeneration8/moretypes/newcrittrueaffectionfalseindependentswitches;SS01–59manualstaticvectorspreserveall statedrandom/partialcommitconditions.',
'Coverage114=106stage-related+3field+4rawstats+1HPmean;status31scopeand21type/ability/airborne/transform+Gravitycrossprimaryexplicit;datasamplessetappropriatefunctionIDs,notproofalloutsideeffectscomplete.' ])
add('M46-ORDER','wp46-damage-multihit-and-healing.md','§2',['R002','R003','R004','R015','Battler003','EOR','BattlerUse'],[
'Ordinaryusequalification/obedience,PP,type/MoldBreaker/twoturn,usage/history,target/Pressure/block,ownfail,startinitialization,lategates/typechange/quickcharge,no-target preserveorderedprefix.',
'Targetwholeusereset/typequalificationbeforeplannedhits;chargingreturnbeforeallordinarygates. Firsthit orperhitsuccessonlychecksaccuracy/semi,badalltargetfailurecrash/item/cancelreturnsfalse.',
'Eachhit resetsperhitstate,rechecksabsorption/calcdamageandplansalltargetloss,animationthenHPalltargets,firsthitselfKO,userfaint,records,dealingeffects,ability/items,survival/allitems/faint/judge,targetmain/general/faint/additionalflinch/berry/SteamEngine/faint.',
'CompletedhitcountseparatefromHPamount;afterhituserfaint/rawSleep/Frozen/alltargetfaintstop,butDisablealonecontinues;allhitsaftercallbacksperoriginaltargetmayrunatnumhits0unlessearlywholeusereturn.',
'Substitutebreaknext-hitrealHPallowed;effectiveness/typeoftenfixedearlierwhileHP/stats/itemsre-read. Fixeddamagekeepsabsorption/survivalbutdoesnotnormalParentalpowerfraction.',
'hpLostperhitincludingSubstitute,totalHPLosttargetcumulative;drainfirst,recoillatter. Reduce/Recover roundclipmin1,canHealindependent;MagicGuardindirectquery,RockHeadordinaryrecoil,notLiquidOoze.',
'CancelclearsTwoTurn/Rollout/Outrage/Uproar/Bide/FuryCutter,notHyperBeam;Outrage1nonfullcancelmayconfuseself. NoautomaticPPrefundandtwousageflagsdistinct.' ])
add('M46-MULTIHIT','wp46-damage-multihit-and-healing.md','§3.1–3.3',['R009','R004','R003','BattlerUse'],[
'Alltwohit/poison/flinchplanned2nativeflinchclassification;TripleKickeachordinarybasequeryaddsP,SkillLinkdisablesperhitaccuracy,formabsorptionskipdoesnotadvancebasecounter.',
'SurgingStrikesplanned3forcedcritstillcentraldenials;2to5distribution7/20,7/20,3/20,3/20drawfirstthenSkillLinkforces5;AshGreninjaform2direct3andbase20withoutBattleBondgate.',
'ScaleShotallhitsafteraffectedDef−1thenSpeed1;BeatUpownteamable/rawNONEincludesU,notpartner,snapshotlength,basequeryshiftfirstremaining,basespeciesAttackfloor/10+5,formabsorptionnotconsume.',
'DragonDartsplanned1/repeattrue,extendoneallycandidateactualconstraints,firsthitchecksallpotentialtargets,firstvalidfirstshot,secondvalidelsefirst;firstshotselectedtargetmustlive/affectedtorecurse,secondnoreaccuracy,userfaintstops;silentimmunityhasnoreward.',
'TwoTurn14identitiesphasefromeffectnil,PowerHerbquickchargeeffects+consumebeforelatergates,failuredonotrestore;SkyDropnoherb. SolarSunbothphasesandnoherb;Noneweatherhasnopowerhalf,othernonSunhas.',
'FreezeShock/IceBurn/SkyAttackattackadditionalonly;Geomancyentryanyof3raisableunlessexistingeffect,attackingSpAtk2→SpDef2→Speed2;SkullBash/MeteorBeamchargebuffsapplyquickcharge.',
'Dig/Dive/Fly/Bouncehalf-invulnerablespecific;SkyDropopponents/substitute/gen6weight2000/semi/holdergates,Flyingtypeimmune,chargeholdandattackaftercallbackreleaseevenunaffected;Forceclearsnamed5personal4sideprotections.',
'HyperBeamgeneral2+currentmove,allinvalidcannotestablish;Uproar3once,wakesrawSleepnotSoundproof;Outrage2/3startthenallhitsafter--andzeroConfuse;RolloutpowersequenceP/2P/4P/8P/16PandDefenseCurldouble,onehit,5then--.',
'Bide3establishthen--,attackwhen1,lastdamagesourceorfallbackrandomnonnearfoe,noaccum/noTargetfailure0;fixed2accumincludesSubstitutedamagerecords.' ])
add('M46-DAMAGE','wp46-damage-multihit-and-healing.md','§4–5.3',['R005','R008-sub','R002','R003','Clauses'],[
'Fixed20/40,roundtargethalf,min1,userlevel,uniformfloorL/2..floor3L/2,min1;EndeavorrequiresU<Tandonehit;OHKOspecificthreshold/guards/defaultClausesbindingpreserved.',
'Counterphysical/specialsourceindexmustopponentaddable,nonnearallowed,nofallback;fixed2loss. MetalBurstlastfoeattacker fixedfloor1.5lastfoeloss. FinalGambitsnapshotHP,notlaterHP.',
'DamagehistoryCounter/Mirroronlynonsub,Bideinclsub,positive-nonsubFocusflag,positiveAssuranceflag,attackerarrayscancontainzero;foespecificrecordsseparateandlegacyHiddenPowerNormalcategorization.',
'SplashesadjacentalivetargetalliesindirectfloorH/16allreducefirstthenmessage/items,nolocalsubguard. FirstImpression/LastResort/Belch/Poltergeist/Synchronoise/FocusPunch/SuckerPunchindividualeligibilityexactread.',
'All22HP/happiness/stage/speed/PP/weightpowerentriesusetheirconcretefloors/thresholds/limits,notgenericlinear;ElectroBallintegerdivision,TrumpCardpost-PP,weightunits0.1kg,Magnitudeoneinitial20-outcomedraw.',
'FuryCutterpreservesoldcountthenreset/incrementcappedbyrepeateddoublingreach>=160notPcap160;EchoedVoiceper-sidefirst-in-roundincrementmax5andtailidleclear.',
'Conditionaldoublefamiliesuser/targetstatus/substitutegates,AcrobaticscurrentemptyorGemConsumed,Pursuit/currentactions/lastRoundfail/lastfoefaint/lastAttackerarray/tookDamage/statslowered alluseactualfieldsnotcommonsensenames.',
'Fusioncapturesotherflagbeforegenericclearandsetsowningeneral;Weather/underwater/underground/sky/electricterrain usecorrectpowerorfinalslot andtarget/usergates,Grassyrawhalvingwithoutgroundgate.',
'FlyingPressnormalizesbothbaseeffectivenessbeforemultiplyanddoesnotreapplysingleexceptionsonFlyingfactor. Photoncomparesuserstage-adjustedAttack>SpAtkelseSpecial,norandom;ShellSideArmfirsttargetratioandrandomties,physicalcontactonly.',
'BodyPressusesuserDefense+stageinattackslot;FoulPlayactualcategorytargetattackinputbutkeepsU/Tidentities;PsyshocktargetDefense+stage. Normalcrit/Unaware/burnandabilityrulesstillapply.' ])
add('M46-RESOURCES','wp46-damage-multihit-and-healing.md','§5.4',['R012-sub','R004','R003','EOR'],[
'Stockpilemax3,incrementfirst,Def1thenSpDef1,recordcountonlyifordinarysubmissiontrue;Simpleactualquantityandrecordcountdiffer.',
'SpitUprequiresstock>0,power100stock;allhitsafteralive/positive/affected,showsloststockthenopposingteamallfaintedearlyreturnretainsallrecords;elseattemptrecordedselfdropsandzero3records.',
'Swallow0fails;cannotHeal andbothrecords0fails;stock1/2/3healH/4,H/2,Hdirectthenrecorddropsandclear. EarlierHealBlockmovequalificationstillapplies.',
'PledgewaitfirsteligibleunmovedUseMoveallyanotherpledge,nonDamage/setupnoanimation,clearselfFirstPledge/setallycodeMoveNext/lastFailedtrue;combinationnotguaranteedlateracted.',
'GrassFireFire/opponentSeaOfFire,FireWaterWater/ownRainbow,WaterGrassGrass/opponentSwamp,eachPdoubleandtypeexistscheck;allhitsaftercombohasnounaffectedgate,onlyzeroeffectsets4,no_refresh. EORSeaOfFiretwoconsumerscan--twice.' ])
add('M46-HEAL','wp46-damage-multihit-and-healing.md','§6.1–6.4',['R010','R006','R004','Battler003','Battler001','EOR','R012-sub'],[
'CommonselfhealSnatch/fullHPfail,earlyHealBlockseparate,noqueryatcentralRecover;Restselfsleep3beforefullmissingheal,weatherhealsnapshotvsShoreUplateread,Roosthealbeforeflag,Purifytargetcurebeforeusergeneralheal.',
'Halfhealround,weatherSun2/3,None/StrongWindshalf,othersquarter,ShoreUpsand2/3;StrengthSapcurrenttargetAttackstagefloorbeforelower,Contrarymax/normalminonlyspecialfailure,LiquidOozedirectuserloss,elsecanHealBigRootfloor1.3.',
'LifeDewfloorH/4sameSidecanHeal;Jungleeitherhealorstatus,healthenrawstatuscure. HealPulsefullHP/canHeal,roundhalf/markedpulseMegaLauncher3/4;FloralrawGrass2/3withoutgrounding.',
'Presentoneinitialr0..99power40/80/120/healwith40/30/10/20weights,healnotdamagingactualquarterandtargetcanHeal;PollenPufffirsttargetsidesnapshotandHealBlocktargettypefoe,allySubstitute/canHealgates,healhalf.',
'DrainperhitpositivehpLostroundhalf/3quarterincludingSubstitute,DreamEaterasleepview,healingflaggen6;LiquidOozeignorefaintedfirstandnotMoldBreakerguard/noMagicGuard,elsemessagecanHealBigRootfloor1.3.',
'Wishposition2/savedrounduserH/2/makerindex,noinitialmissingHPrequired;AquaRing/IngrainflagandEORfloorH/16BigRootfloor,LeechSeedsourcepositionfloorvictimH/8actualdrainafterdeduction,requiresrecipientalive.',
'Nightmareasleepviewandnotexisting,EORrecheckclearsifawake,indirectquarter. FutureSight3position/sourceidentity,setupnodamage;expirycurrenttarget/sourceordummy,extraInitEffectsseatcrossreferencescleanupbeforebind/damage,sourceelsewherepointersuntouched.',
'PainSplitm=floor(sumcurrentHP/2)once,UthenT,independentcaps,nocanHeal/nohealingflag,normalSubstitute/Protectearly;reductionregisterDamagefalsepreservesexistinghistory,Recovercanclearcrosshalf.',
'PainSplitbothitemchecksUthenTevenifnoHPchange,normalwrite-through;51/60and150/200→60/100,1/2→1/1,50/100withORAN→60/60;canloseHPtotal,notconservation.' ])
add('M46-COST','wp46-damage-multihit-and-healing.md','§7–7.1',['R004','R010','R012-sub','Battler003','BattlerUse','Clauses','EOR'],[
'OrdinaryrecoilperoriginaltargettotalHPLostroundquarter/third/half,min1,affected+indirect+notRockHeadthenitemheal;statusadditionindependent;StruggleroundH/4withoutMagicGuard/RockHead.',
'JumpKickcrashonlyperhitalltargetsfailed/nonemptyneededpath,indirecthalfHintegerthenitem/faint,noRockHeadguard;SteelBeamallhitsaftereachoriginaltargetceilH/2,nounaffectedgate,butearlierwholeusereturncanbypass.',
'MindBlownworksnotargets,Dampordinarymoldfalsewholefail,firstselfKOroundH/2ifindirect. Explosiononehit/worksnotargets,HPtargetsubmissionbeforeselfKOallcurrentHPthenformalFaint;Mistybasefloor1.5rawterrain.',
'LoadedExplosionclausesmayearlyfalsebeforebaseDamp;facilityprimaryownsclauseoverride. FinalGambit/targetinvalidbeforeSelfKOcannotguaranteedeath;MementolocalfailfalseallowsnodecreaseyetSelfKO,centralquerieslater.',
'HealingWish/LunarDanceneedsnonactive,SelfKOthenpositionflag,entryconsumerWishthenLunar/gen8nobenefitretainandPPdifference. PerishSongcounter4+source,existingpositivegates;clausesonlytargetgate.',
'DestinyBondgen7Previousreject,actionstartcopyPrevious/clear,opposingdirectKOrecordthenaftallhitsattackerfaint;Grudgeper-hitPPzeroearlierthanDestinyBond,notallindirectdeaths.',
'ShadowHalfallaliveHP<=1fails;elseeachaliveHP>1floorcurrenthalf,allreducebeforemessage/allaliveitemchecks,thenHyperBeam2/currentmove;ShadowEndlivingU+affectedtargetroundcurrenthalfmin1,nobothdefensiveabilityguards.',
'ShadowHPpositiveReduceHPanimfalse/registertruewritesdurableHPthenHPbarandflagsafterdisplay;notallcounterdamagehistoryautomaticallycreated;failurepreservesonlyreachedprefix. OptionalShadowPBSnotautomaticallyenabled.' ])
add('M46-COVER','wp46-damage-healing-coverage.md','all §§1–3',['R004','R005','R006','R007','R009','R010','R008-sub','R012-sub'],[
'Originalunique139 =30multi/22fixedtiming/44power/23healing/4stockpledge/16recoil;eachlistedidentityreadandmatchedconcretebodyrule,notallmovesglobalcount.',
'PainSplit1+ShadowHP2additionalreceivedmakes142withoutchanging139orWP44scope. NaturalGiftremainsWP47AprimarywithWP46multihitconsumer andnotdoublecounted.',
'OtherNone/45WP47A/20WP47B/28field/29status/9typesidentitiesexplicitlycross-owned,theirpresenceisnotcompletionapproval. All sourceeffectsunderthisCOM-MOVEreadsetread,consumerjoinsseparatelyreceived.' ])
add('M47B-SWITCH','wp47-b-switching-control-and-item-changes.md','§§1–2',['R013','R005','Battler002','Battler006','CORE-F030','CORE-F031','CORE-F032','CORE-F034'],[
'Replacementrandomuniformown-teameligibleotherwiseownerAI/playerlooseonly-switchinUIdefaultnocancel;actualrecall/leave/init/displayorder/sendout/speed,entrynotificationseparate,nofullrequalification.',
'PursuitbeforeactualreplacecankillUandstoplaterselection,earlierPP/effectswrittenremain. FleeCanRun+wildernessnoalliesdecision3,nospeedroll.',
'Teleportstatuswildescapeelsebackupwholegateandendchain;damagingpivotlive/hits>0/opponentnotallfainted/notalloriginaltargetsswitched/backup,survivalhpLost0canstillhits1.',
'PartingShotAttack−1thenSpAtk−1,reflectedeffectflagscanchooseswitcherbutouterhits0blocksnormalreflectedcase;Batonwhole/endbackupalivehits/Pursuitthenbatonflag.',
'ForcedstatusSuctionunlessMoldBreaker/Ingrain,wildsolecanRunlevelgateortrainerbackup;wilddecision3,trainerfirsteligibleendphaseonlynonealreadySwitched/useralive/hitspositive. DamagingwildnocopiesstatusfailuregatesandcurrentbrokenSubstitutemayallowdecision3;trainerstilldamageStateSubstituteblocks.',
'AllySwitchrequiresoneadjacentaliveowneralignedally,swapspositionthenpositionentrybothnotfullentry.',
'Batonsevenstages+19namedflagsretained,LaserFocus/LockOnpositive→2,PowerTrickrawnewattack/defenseswap,MegaGengarTelekinesisclear/unstoppableGastroclear;othersresetincludingrawmoveshistory,bindings,noitemorHPmerge.',
'OtherlivingmembersoldseatAttract/JawLock/LockOn/MeanLook/Octolock/SkyDrop/Trappingreferencescleared;BatonownLockOndoesnotpreserveopponentpointingoldseat.' ])
add('M47B-CONTROL','wp47-b-switching-control-and-item-changes.md','§3.1–3.2',['R013','R005','Battler001','R012-sub','CORE-F043','EOR'],[
'Bindingusually5/6orGripClaw8gen5else6,storesmove/user;EOR--thenif0nodamage,gen6H/8elseH/16,sourceBindingBandH/6elseH/8.',
'MeanLookstatusghost/alreadyfail,damageadditionalseparatefaint/substitute/ghost,ThousandWavesmaineffectnativemode;Octolockdamageoverwritewithoutallotherguards,EORDef−1thenSpDef−1nilsource.',
'JawLockbothalive/nonsub,targetghostexclusion,bothlocaltrappedfalse,onepointercausesbothquerytrue;FairyLock2notuniversalall-escape-lock.',
'CurseGhostdynamictargetRandomNearFoegen8elseNearFoe,Substitutebypass,settargetfirstthenfloorH/2cost/registerfalse/itemheal;nonGhostany3changeeligiblethenSpeed−1→Attack1→Defense1noHPcost.',
'Substitutecostmax(floorH/4,1),hpstrictgreater,OnStartdeduct/registerfalse+itemhealbeforemaineffectclearsTrapping/Moveonlyandsetsdurability;oldTrappingUsernotclearedlocally.',
'Pursuitswitchingqtrue/P2;ShellTrapflag+tookPhysicalHitsetbyopposingphysicalrealpositivehitwhilechosenUseMoveunmoved,schedulesMoveNext/Quash0;BeakBlastprepareflagonly,contactburnreactionthenendclear.',
'RoundsideflagP2thenfirstunmovedallysamecodeMoveNexttrue/Quash0;AfterYouUseMove/Shiftunmoved/hasmoveobject/MoveNextfalsethenflagswithoutchangingoriginalmove/PP.',
'Quashmaxpositive/notalreadymaxorordinarylastgates,writeglobalmax+1/clearMoveNext;generation8Quashgroupordinarypriority,olderquashlevelorder. TrickRoomonlyspeedwithinpriority;phaseconsumptionclearflagsbeforeprocessing.' ])
add('M47B-BB','wp47-b-switching-control-and-item-changes.md','§3.2.1',['R005','Battler004','Battler003','BattlerTrigger-sub'],[
'BeakBlastvictimpreparedunmoved,attackerrawNone+ownSubstitute,actualcontactnoPads/LongReach,targetpositivehit:PPandtargetHP/recordsprefixbefore反灼资格wrongcontextignoredSubstitutequeryNoMethodError.',
'NoattackerSubstituteshortcircuitswrongqueryandnormallyburns;existingrawstatusorPads/nocontactearlierguardsavoiderror. TargetSubstituteisnotcause.',
'Uncaughtlocalerrorpreventsnormalremaininghit/endcallbacks,alreadywrittenprefixnotrollback;outerdiagnostic/hostrecoverynotguaranteed,noNaturalGift-specificretryclaim.' ])
add('M47B-INSTRUCT','wp47-b-switching-control-and-item-changes.md','§3.3',['R013','BattlerUse'],[
'InstructignoresSubstitute,lastRegularvalid+known+data/notmultiTurn,currentselectedfocus/shell/beakreject,exact32functionblacklist,lastmatchslotfinitePP0reject;setsflagonly.',
'EndouterbeforeDanceriteratecurrentalive,setflagrequireslastMoveUsednonnull,clearflagbeforelastmatchactualslotlookup,noslotskip;lastMoveUsednotimmutablelastRegularsnapshot.',
'Savemovedround,setInstructed,realchoicequalificationthenreal-slot simpleuse specialfalse:ordinaryPP/status/obedience/accuracy;afterreturnrestoremovedround/judge,positivedecisionmayreturnbeforeclearInstructed.',
'Originalcommandnotreplacedandmovedroundrestored,innerordinaryrecordscanchange;InstructedonlyTormentlocalexceptionnotallrestrictions. Qualificationrejectdoesnotrestoreclearedflag.' ])
add('M47B-RESTRICT','wp47-b-switching-control-and-item-changes.md','§4',['R013','R002','Battler003','Battler001','ItemStatuses'],[
'AromaVeilonlynamedfamilies,self/alliesunlessMoldBreaker. Postwriteitemstatuscurecanimmediatelyclearnewrestriction,countersnotguaranteedpersist.',
'EerieSpelladditionalalive/nonsub,lastRegularcurrentfirstslotPPnonzerofinite,min3;SpiteignoreSub+reflectsameprecheckmin4. PPsyncsameRealMoveID/nonTransformonly.',
'Disableexistingpositive/lastregular/aroma/anyPPeligiblematchingcurrentmove,sets5/IDanditemcure. Tormentimmediateboolean. Encore6always+6gen7blacklist,knownlast/currentPP/ShellTraparoma,sets4/ID,itemcure.',
'Taunt4plusgen6ObliviousunlessMoldBreaker;HealBlock5notignoreSub;ThroatChop3refreshevenoldpositivebutmessageonly0;Imprisonselfboolean,dynamiccurrentenemyknownmoveconsumer.',
'MentalHerbclearsDisablecounteronlynotDisableMove;normalpermissionidentitycomparisoncanstillreject,positiveEORexpirycallbackwouldclearIDbutcounter0doesnotrun,init/Transformclearpair,specialuseonlybypassnamedgate.' ])
add('M47B-ITEM','wp47-b-switching-control-and-item-changes.md','§5.1–5.2',['R011','Battler001','Battler006','ItemData','CORE-F019'],[
'Citemwrite-through,Iinitialbutmutable,Rrecycle,Ppickup+serial,Belchside-party;normalendrestorecurrentIonlyauthorizednormalpath. Noatomictransactionpromise.',
'ItemActivefaint/Embargo/MagicRoom/corrosion/Klutz;ordinarytransfernotuniformactivequery. Unlosablemailfirst/Transformexception/Megadynamic/specific8combosrawArceus/Silvallyability.',
'RemoveChoiceunlessGorilla,olditemUnburden,permanentclearmatchingI;ConsumeR/PthenBelchwhenallowed/permanentremove/optionalSymbiosis;directassignmentdifferent.',
'ThiefnonwildUalive/targetaffectednonsub/Ctarget/Uempty/losableboth/StickyHoldunlessMoldBreaker,targetneednotalive;wildtargetmatchingI+UemptyIpermanentItransferelsetemporarythenUtrigger.',
'BestowUlosableitem/targetemptylosable,gen6ignoreSub,noStickyHold/activegate;wildUmatchinginitial→targetIifempty/permanentremoveelsetemporary,targettrigger.',
'TrickwildUfail,bothnilfail,4unlosablechecks/targetStickyHold;swapcurrentboth,choicelocks/Unburdeneach,onlywildtarget matchingI+UinitialemptywritesU.I,noT.Iclearing/symmetricIexchange;UtriggerthenT.',
'RecycleRexists/Cempty,setC/fromR,wildbattleIemptyfill,clearR/P/serial,trigger,noBag;KnockOffgen6Pround1.5iflosableevenSticky/Substitute,removegatesseparateandtemporary.',
'Incinerateafterdamage nonsub/notberryWeakened,berryorgemgen6,losable/notSticky,permanentremovewithoutordinaryconsumeR/P/Belch/Symbiosis. Corrosionpartyindexedflagpersistsswitch/newitem,nocurrentitemremove.',
'Embargo5doesnotneedcurrentitem;MagicRoomtoggle5/0directcanceldoesnotitemtriggerall,naturalexpiryseparate.' ])
add('M47B-FORCED','wp47-b-switching-control-and-item-changes.md','§5.3–5.4',['R011','Battler006','ItemStatuses','ItemHit','AbilityInnards','R005'],[
'StuffCheeksselectionandactualrequiresberry+itemActivethenDef2eligibility;Unnervenotinthisactivegate,MagicRoomblocks;boostthenconsumeoldberryrecoverable/deferSymbiosis/explicitforcedtrigger.',
'Teatimeanytargetberrynotsemiwholegate,pertargetsamewithoutitemActive,ordinaryability/protectioncaneffectivelyexclude;consumeolditemforced,notallmustconsume.',
'BugBitesuppresseshealingberryduringhitforselectedtargetswithHPHealregistration;afterallhitsbothalive/affected/nonsub/berrylosable/Stickyguard,U.Belch,Tpermanentremove,noT.R/P,UforcedtriggerthenU.Symbiosis.',
'Flingusemessagesnapshotfailure checksheldactive/losable/berryconsumable/Flingprefix;onehit,basecurrentfirstfullynumericflagminimum10,malformedprefixdefault10,nocurrentitembase0.',
'FlingtargeteffectSubstitute/ShieldDustunlessMoldBreakerreturn;barb/orbs/lightball/rockfangstatusorflinch,otherforceditemtriggertrue;thencurrentUitemberryBelch,targetfaintforcedreturndoesnotprotectnilUitempostread.',
'InnardsOuttargetfaint/usernotdummy/indirectpositivecurrentlosscantriggeruserOranordinaryconsume;FlinglatercurrentemptyreadNoMethodErrorbeforetargetBelch/endconsume,priorHP/faint/itemrecordsretain.',
'NormalendFlingifusernotswitchedandstillcurrentitemconsume recoverable/Symbiosis/noBelch evenprotect/miss;RedCardswitcheduser skips,notmerelytargetswitched. ExplicititemtriggerbypassesactivebutrejectsfaintandorderedHP/status/endmove/positiveberry.',
'PayDayplayerownedonly5currentlevelaccum,allmessage;HappyHouronlynonopposingflag,nodeferredlevelrecomputeorbalanceimmediately;actualrewardnormalCOREconsumer.' ])
add('M47B-ABILITY','wp47-b-switching-control-and-item-changes.md','§6',['R007','Battler001','Battler003','Battler006','Clauses'],[
'skillswapclausetargetearlyguard,shortskillswapnotalias. Abilityassignbattle-only,notdurablePokemonability.',
'Simple/Insomniaregistration/targetunstoppable+Truant+samepurpose;assignmessageoldlossnewgain. RolePlayuserunstoppable,targetnonnull/different/gainableandAlchemyReceiverTraceWonderGuardblacklist,ordinaryactive targetnotrequired.',
'Entrainusernonnull/gainable/AlchemyReceiverTraceblacklistnotWonderGuard, targetunstoppable/Truantreject,noequalsguard. SkillSwapbothnonnull/losable/gainable/notWonderGuard,sameidentityonlyold<=5reject,assignboththenUloss/Tloss/Ugain/Tgain.',
'GastroAcidtargetunstoppable/alreadyflagreject,setGastro/Truantfalse/loss(suppressed),nogain. CoreEnforcernonsub/notsuppressed/notunstoppable,UseItemorUseMove/Shiftaftermovedonly.',
'IgnoreAbilityordinaryusageonlysetsMoldBreaker;specialdoesnotownset,userabilityearlierdistinct. MagnetRise5/Telekinesis3do notguaranteeairborneunderIronBall;Gravityunusable,thelatterspecies/MegaGengarblacklist.',
'SkyUppercutpermitsFlyingsemiwithoutdouble/ground;SmackDownGroundFlyingneutral,aliveaffectednonsub/notSkyDrop,actualairborneorFlyBounce,setsground/clearsFlyBouncechoiceifnotmoved,zerosrise/tele.',
'Gravity5repeatfail,clearsnamedFlyBounceSkyDroptwoTurnandunmovedchoice,allrise/tele/heldSkyDrop. Transformuseralreadyfail,targettransform/illusionfail,visualrequestbeforeeffect,copyfive/type/ability/stages/movesPP5withnoHPlevel/durablemovechange/lossoldonly.' ])
add('M47B-DATA','wp47-b-control-items-coverage-data.md','all §§1–5',['R013','R011','ItemData','FlingPBS'],[
'Instruct32/Encore6always+6generation7exactfunctionlistsmatchedallentriesincludingMeteorBeamnotautoadded;identifiersnotsemanticfamilysuper-guard.',
'EightunlosablespeciescombinationsmatchItemdatacompletearraysandArceus/Silvallyidentityconditions;Megarecordquerydynamicnotduplicatedstaticlist.',
'578defaultFlingnumericflagsreadasfullFlagsfieldrecordsandcomparedtoeverygroupinformalorderedbydefaultdata;TM64=250retained,rare25/55/65/75/85groupscorrect,baseclamp10stillapplies.',
'60primaryidentitiesandsharedRapidSpin/Gravity/MagicRoom/TrickRoom/GrassyGlideoutsidesetsarecoverageownership,notexecutionorfulloutside-domainapproval;allbodyanddatawereactuallyread.' ])
# All explicit assertions above are manual semantic normalisations, not split-at-semicolon/line objects.
obj={'schema':'r8-com-move-semantic-reverse-v1','reviewer':'/root/com_move','updated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'groups':G,'assertion_count':sum(len(x['subassertions']) for x in G),'granularity':'Manually normalised finite semantic assertions. Clauses spanning rows/paragraphs grouped by behavior; repeated catalogs retain per-vector reception separately. This number is not an automatically inferred universal requirement count.','unreceived':[],'behavior_execution':'NOT_EXECUTED'}
(B/'reverse-mapping.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
forward={'schema':'r8-com-move-semantic-forward-v1','reviewer':'/root/com_move','facts':N,'dependency_facts':D,'reverse_groups':[x['id'] for x in G],'note':'Each facts array records actually interpreted complete finite source behavior, consumers and owning specification. Raw read logs do not substitute semantics. Child actual reviewer contributions are separately bound on reception.'}
(B/'forward-mapping.json').write_text(json.dumps(forward,ensure_ascii=False,indent=2)+'\n')
print(len(G),obj['assertion_count'])
