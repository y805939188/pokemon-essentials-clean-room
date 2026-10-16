from pathlib import Path
import json,re,datetime,hashlib,subprocess

P=Path(__file__).resolve().parent
W=Path('/workspace/pokemon-essentials-clean-room')
R=Path('/workspace/pokemon-essentials')
T=P.parents[1]
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
def load(p):return json.loads(p.read_text())
def save(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def merged(iv):
 out=[]
 for a,b in sorted(iv):
  if out and a<=out[-1][1]+1:out[-1][1]=max(out[-1][1],b)
  else:out.append([a,b])
 return out
def complement(iv,n):
 out=[];cursor=1
 for a,b in merged(iv):
  if cursor<a:out.append([cursor,a-1])
  cursor=max(cursor,b+1)
 if cursor<=n:out.append([cursor,n])
 return out
rs=load(T/'delegation/readsets/com_move.json')
logs=[(p,load(p)) for p in sorted((P/'io').glob('read-*.json'))]
cl=load(P/'subreviews/attributes_calling/reading-ledger.json')
cf=load(P/'subreviews/attributes_calling/forward-mapping.json')
cr=load(P/'subreviews/attributes_calling/reverse-mapping.json')
D=load(P/'dependency-facts.json');N=load(P/'semantic-notes.json')
full_new=[('AbilityEffects','008_Battle_AbilityEffects.rb',3208),('ItemEffects','009_Battle_ItemEffects.rb',1948)]
for key,name,total in full_new:
 path='Data/Scripts/011_Battle/007_Other battle code/'+name
 D[key]={'path':path,'intervals':[[1,total]],'status':'FULL_READ_DEPENDENCY','reviewer':'/root/com_move','formal_boundary':'Source contribution only. Does not accept all WP48/49/50 formal clauses, or combinations beyond actual inputs.','facts':[]}
D['AbilityEffects']['facts']=[
 'Read every registry wrapper and all add/copy handler bodies through line3208. Speed/weight/status/accuracy/critical facts are separately detailed in AbilitySpeedWeight/Statuses/Accuracy/Critical and all damage/trigger phases below.',
 'Priority: Gale Wings raw Flying and full HP current; Prankster status sets its marker and addsone; Triage healing adds three. Quick Draw draws<30 bracketone, Stall minusone; display/use phase separate. Steadfast requests Speedone on flinch. Dazzling/Queenly Majesty use saved positive priority plus actual opposing target and opposing bearer; empty targets false.',
 'Move immunity: Bulletproof bomb; Flash Fire nonself Fire returns true even silent and writes boost only visible; Lightning Rod/Motor Drive/Sap Sipper/Storm Drain use the matching stat helper; Soundproof sound, current gen self exemption; Telepathy only damaging nonself ally; Volt/Water Absorb and Dry Skin use healing helper; Wonder Guard rejects damaging typed nonsupereffective, not typeless/status.',
 'User damage fields were read per entry: power conversion1.2; Analytic last-in-round1.3power; Blaze/Overgrow/Swarm/Torrent at <=H/3 matchingtype1.5attack; Defeatist<=half halvesattack; DragonsMaw Dragon1.5attack; FlareBoost burnspecial1.5power; FlashFire flag Fire1.5attack; FlowerGift sunnyphysical1.5attack; Gorilla physical1.5attack; Guts statusphysical1.5attack; Huge/PurePower physical2attack; Hustlephysical1.5attack; IronFist punch1.2power; MegaLauncher pulse1.5power; Minus/Plus special with eligibleally1.5attack; Neuroforce supereffective1.25final; PunkRock sound1.3attack; Reckless recoil1.2power; Rivalry known genders same1.25/opposite.75power; SandForce matchingthree types/weather1.3power; SheerForce positiveaddlEffect1.3power; SlowStart positivephysicalhalfattack; Snipercritical1.5final; SolarPower sunnyspecial1.5attack; Stakeout selectedSwitchOut2attack; Steelworker Steel1.5attack; SteelySpirit Steel1.5final; StrongJaw bite1.5power; Technician nonself/nonstruggle currentpowerproduct<=60 then1.5power; TintedLens resistant2final; ToughClaws rawcontact4/3power; ToxicBoost poisonphysical1.5power; Transistor Electric1.5attack; WaterBubble Water2attack.',
 'Ally Battery special1.3final, sunnyphysical FlowerGift1.5attack, PowerSpot1.3final, Steel SteelySpirit1.5final. Target DrySkin Fire1.25power; Filter/SolidRock supereffective.75final; FlowerGift sunnyspecial1.5defense; Fluffy actualFire2final then actualcontacthalf; FurCoat physical/Psyshock2defense; GrassPelt storedGrassy1.5defense no grounding/category guard; Heatproof Firehalvespower; IceScales specialhalffinal; MarvelScale statusphysical1.5defense; Multiscale fullHPhalffinal; PunkRock soundhalffinal; ThickFat Fire/Icehalvespower; WaterBubble Firehalffinal. Nonignorable PrismArmor .75supereffective and ShadowShieldhalf-fullHP still require active ability. Targetally FlowerGift and FriendGuard affect defense/final separately.',
 'On-hit handlers read completely: Aftermath faint/contact then Damp gate and source indirect/contact permission beforequarter; AngerPoint crit+canraise then directAttackmax; CottonDown allotherlegalSpeed losses; CursedBody living source/noexistingDisable/lastregularslotfinitePP then30%/AromaVeil beforeDisable3+ID and itemcure; CuteCharm live target/contact then30% thensourceAttract/contactpermission; EffectSpore contact30% draw then uniformsleep/poison/paralysis, no retry, powder/contact gates; FlameBody/PoisonPoint/Static already matchingstatus shortcircuits draw then30%/query/contact; Gooey/TanglingHair sourceSpeedlosscontact; Illusion clears disguise without splash. Innards/IronBarbs separately detailed.',
 'Remaining on-hit: Justified actualDark Attackone; Mummy actualcontact/living source/no unstoppable/same ability then contactpermission assignment, followed even when no assignment by loss/gain callbacks using old=nil; PerishBody contact/living/source-and-target countersnotpositive thencontactpermission setsboth4/sourcepointertarget; Rattled Bug/Dark/Ghost Speedone; SandSpit weather; StaminaDefenseone; WanderingSpirit raw gainability/Receiver/WonderGuard exclusions, actualcontact thenpermission assignments, thenbothloss/gaincallbacks; WaterCompaction WaterDefense2; WeakArmor physical anyDefense-loss/Speed-rise thenDefense-1,Speedcurrent2old1. PoisonTouch uses rawcontact, draws30 before ShieldDust/query and submits poison.',
 'End-use: BeastBoost counts damageState.fainted, skips allopponentsfainted, selects highest raw five-stat first in enum and canraise; Chilling/GrimNeigh use anyfaint but requestone and temporarily change ability identity without ensure; Moxie requests numFainted; Magician futureSight/nondamaging/currentitem/wild guards then first eligible target with no StickyHold, current+wildinitial transfer and held trigger. Berserk reads droppedBelowHalfHP; ColorChange reads calcDamage/nonSub/nonpseudo currenttype; Pickpocket checks source not switched/rawcontact/bothsubstitutes/currentitems/unlosable/StickyHold then wildinitial transfer and held trigger.',
 'EOR weather DrySkin sunindirectH/8 or rainycanHealH/8; IceBody hailH/16; IceFace restored only its form/canRestore flag; RainDish rainyH/16; SolarPower sunindirectH/8. Healer drawsone30% then cures all rawstatus allies; Hydration effective rain; ShedSkin rawstatus then30%. BadDreams nearother-side viewedSleep/indirectH/8; Moody currentfive/oldseven prequalified independentup/down pools, +2 draw then deletechosenfromdown, -1 draw and itemchecks; SpeedBoost positive turncount and notRun. BallFetch firstfailedball; Harvest storedRecycleBerry/sunnyordraw50%; Pickup highestpositive sequence excludingself, clear donorPickup andmatchingRecycle, wildinitial conditionaltransfer, heldtrigger.',
 'Trapping ArenaTrap notairborne, MagnetPull Steel, ShadowTag targetwithoutactiveShadowTag; CertainSwitching empty. Switchin fullbody read: AirLock/CloudNine notices; Anticipation ownedplayer fullopponentmoves with actual type/conditionalHiddenPower and OHKO; AsOne temporaryUnnerve identity withoutensure; AuraBreak/Comatose/DarkAura/FairyAura/Pressure/MoldBreaker/Teravolt/Turboblaze/Unnerve notices; CuriousMedicine alliesstageReset; shields/swordDefense/Attackone; primordial andordinaryweather wrappers; Download sums opponent getter defenses choosesAttack onlystrictDef<SpDef; fourSurges only when storedterrain differs; Forewarn explicit syntheticpowers and uniformhighest-list; Frisk current all/oldone heldfoe; IceFace Eiscueform1/hail; Imposter switch_in only and directopposing form/sub/sky/semiguards then Transform; Intimidate nearfoes with separate ability/item checks; Mimicry delegates terrain change; NeutralizingGas clearsall SlowStart/Truant, noChoiceitems clearsChoiceBand, Illusion clears unlessTransformdisplay, temporarily removesownability to detect Unnerve ending; PastelVeil allyrawpoison cure; ScreenCleaner six wallcounts only. Switchout rawmatching statuscures, NaturalCureall, Regenerator non-endbattleH/3 with no ordinarycanHeal; faintReceiver/Alchemy same-side and exact exclusions assignmentonly, SoulHeartSpAtk1; Mimicry None resettypes, fourterrain registeredtype conversion; RattledonIntimidate currentSpeed1; RunAway returns true with caller battlekind gates.'
]
D['ItemEffects']['facts']=[
 'Read complete1948 lines, every registry wrapper and all direct/copy bodies. Speed/Weight, all16HPHeal, all8StatusCure, OnStatLoss and every OnBeingHit/AfterMove/Leppa/WhiteHerb concrete behavior are detailed in ItemStatuses and ItemHit.',
 'Priority Custap canConsumePinchBerry returnone, LaggingTail/FullIncense minusone, QuickClaw draw<20; usephase consumes Custap only, QuickClaw displayonly. BlunderPolicy hit_numzero/noninvulnerable/nonOHKO andlegalSpeed2, thentrigger. WideLens1.1accuracy, ZoomLens1.2 if targetnonmove/nonShift or acted; BrightPowder/LaxIncense .9accuracy.',
 'All71 userdamage identities/aliases read. Matchingordinary type boosters/plates/incenses multiplypower1.2;18gems callmatchingtypehelper. Adamant DialgaDragon/Steel, GriseousGiratinaDragon/Ghost, LustrousPalkiaDragon/Water usepower1.2. ChoiceBand physical/ChoiceSpecs special usepower1.5. DeepSeaTooth Clamperlspecial, LightBallPikachu, ThickClubCubone/Marowakphysical doubleattack. ExpertBelt supereffective1.2final; LifeOrb nonConfusion1.3final; Metronome1+.2*min(counter,5)final; MuscleBandphysical/WiseGlassesspecial1.1power. SoulDew Latias/Latios currentsetting matchingDragon/Psychic1.2final, oldsettingspecialnotclause1.5attack.',
 'All23 targetdamage entries read. AssaultVestspecial1.5defense;18resistberries exactmatchingtype helper; DeepSeaScaleClamperlspecial2defense; Eviolite currentindividualform anyreal evolution1.5defense; MetalPowder nontransformedDitto1.5defense; SoulDew oldsettingLatias/Latiosspecialwithoutclause1.5defense. User critical LuckyPunchChansey+2, RazorClaw/ScopeLens+1, Leek/StickFarfetchd/Sirfetchd+2; targetcriticalfamilyempty.',
 'Rewards LuckyEgg integerexp*3/2; MachoBrace allEVdouble; sixPoweritems addcurrent8old4 to specifiedstat. Fourweatherrocks return8 only matchingordinaryweather, TerrainExtender returns8 forany passedterrain. Fourterrainseeds requirestoredmatchingterrain and canraise DefenseorSpDef1, no grounding. BlackSludgePoisoncanHealH/16 withoutfallthroughwhenfull, else nonPoisonindirectH/8; LeftoverscanHealH/16. FlameOrb/ToxicOrb queryself thencommitburn/toxic; StickyBarbindirectH/8. ShedShell trueCertainSwitching; TrappingByTarget empty; AirBalloon entrynotice; RoomService positiveTrickRoom/canlowerSpeed thenloss1+consume; AdrenalineOrb legalSpeed1 returnscommit forcallerconsume; SmokeBall trueCertainEscape.'
]
D['Catch']={'path':'Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb','intervals':[[1,271]],'status':'FULL_READ_DEPENDENCY','reviewer':'/root/com_move','facts':['Full271 lines read: nickname/storage choice and party-removal records, capture throw gates and outcomes, actual capture formula. Explicit catch_rate is modified unless UltraBeast nonBeastBall; fullHP/noStatus x=floor(rate/3), clampminone; critical andfourshake randomness later. Storage and loss callbacks retain prefix semantics, not transaction. HeavyBall completehandler125–148 takes current pbWeight in0.1kg and new thresholds<1000:-20,2000:+20,3000:+30, clamp1..255.']}
D['Rewards']={'path':'Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb','intervals':[[59,224]],'status':'COMPLETE_METHODS_READ','reviewer':'/root/com_move','facts':['Full pbGainEVsOne and pbGainExpOne read. Currentpersistentitem then initialfallback registry calls precede PokerusdoubledEV thenperstat/totalcaps. No field itemActive gate. Exp split/trainer/scaled/outsider/ExpCharm precede currentitem/initialfallback, thenaffection/growthclamp/message/actualExp+levelup/statrefresh/movelearn. Input101 at LuckyEgg stage yields151, not an assertion of full reward pipeline input101.']}
D['ActiveSitrus']={'path':'Data/Scripts/013_Items/001_Item_Utilities.rb','intervals':[[333,362],[710,753]],'other_complete_units':[{'path':'Data/Scripts/013_Items/002_Item_Effects.rb','range':[451,453]},{'path':'Data/Scripts/013_Items/003_Item_BattleEffects.rb','range':[372,374]},{'path':'Data/Scripts/011_Battle/001_Battle/006_Battle_ActionUseItem.rb','range':[1,149]}],'status':'COMPLETE_RELEVANT_UNITS_READ','reviewer':'/root/com_move','facts':['Active Sitrus requests integer totalHP/4; field helper requiresable/nonfull then clips persistentHP; battle helper delegatesactualBattlerrecovery ifpresent. Field use resolves qty then handlertrue andconsumable removeqty; battle registration consumesbag first, executionvalidates andcallsactualhandler/clearschoice, refusalreturnstheunuseditem. Active use doesnot manipulateheldC/I/R/P; normalheldhalfthreshold andrecordconsumerremainseparate.']}
D['Running']={'path':'Data/Scripts/011_Battle/001_Battle/007_Battle_ActionRunning.rb','intervals':[[1,160]],'status':'FULL_READ_DEPENDENCY','reviewer':'/root/com_move','facts':['pbCanRun rejects trainerfirst and blockedplayercanRun beforeGhost/certainability/item, thenlocalbinding/trapping. Ordinaryrunopposingwild onlyregisters; playerdebug/trainer/canRun precedecertainescaping. duringBattle skipsGhost/certain/trapgroup. NormalcalculationusesrawfieldSpeed, incrementattemptonlynormal andAIrandom. RunAwayregistrytruealone doesnot implyallscenariosescape.']}
save('dependency-facts.json',D)

# These are textual registry and table checks after the real semantic reads.
# No recovered Ruby or game/model behavior is evaluated by this script.
def registry(path,kind):
 s=path.read_text();rows=[];adds={};copies={}
 for m in re.finditer(r'Battle::'+kind+r'Effects::(\w+)\.(add|copy)\(([^)]*)\)',s):
  fam,op,args=m.groups();ids=re.findall(r':([A-Z][A-Z0-9_]*)',args)
  if not ids:continue
  line=s.count('\n',0,m.start())+1
  rows.append({'family':fam,'op':op,'ids':ids,'line':line})
  adds.setdefault(fam,[]);copies.setdefault(fam,[])
  (adds if op=='add' else copies)[fam].extend(ids[:1] if op=='add' else ids[1:])
 return rows,adds,copies
ar,aa,ac=registry(R/'Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb','Ability')
ir,ia,ic=registry(R/'Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb','Item')
def formal_registry(p,start,end):
 out={}
 for l in p.read_text().splitlines()[start-1:end]:
  if not l.startswith('|'):continue
  cells=[v.strip() for v in l.split('|')[1:-1]]
  if not cells or not re.match(r'\w+（\d+）',cells[0]):continue
  fam=cells[0].split('（')[0];out[fam]=re.findall(r'\b[A-Z][A-Z0-9_]+\b',cells[1])
 return out
af=formal_registry(W/'deliverables/final-specification-set/pokemon-rules/wp48-ability-calculation-modifiers.md',202,227);af['CertainSwitching']=[]
it=formal_registry(W/'deliverables/final-specification-set/pokemon-rules/wp50-held-item-effect-coverage.md',11,40);it['CriticalCalcFromTarget']=[];it['TrappingByTarget']=[]
def compare(f,a,c,rows):
 out=[]
 for fam,ids in f.items():
  src=a.get(fam,[])+c.get(fam,[])
  out.append({'family':fam,'formal':ids,'source_direct':a.get(fam,[]),'source_new_aliases':c.get(fam,[]),'literal_set_equal':set(src)==set(ids),'direct':len(a.get(fam,[])),'new_aliases':len(c.get(fam,[])),'pairs':len(src)})
 return {'rows':out,'families':len(f),'direct':sum(x['direct'] for x in out),'new_aliases':sum(x['new_aliases'] for x in out),'expanded_pairs':sum(x['pairs'] for x in out),'copy_statements':sum(r['op']=='copy' and r['family'] in f for r in rows),'all_literal_sets_equal':all(x['literal_set_equal'] for x in out)}
registries={'kind':'TOOL_VALIDATION_AFTER_SOURCE_STATIC_READ','behavior_execution':'NOT_EXECUTED','ability_calculation':compare(af,aa,ac,ar),'item':compare(it,ia,ic,ir),'not_semantic_denominator':'These literal counts only check the two specific catalog vectors AB25/HI36; actual every-handler facts reside in dependency-facts.'}
save('registry-validation.json',registries)

# Match Fling fields to the already read complete formal table.
fpath=W/'deliverables/final-specification-set/combat-requirements/wp47-b-control-items-coverage-data.md'
formalfling={}
for no,l in enumerate(fpath.read_text().splitlines(),1):
 if 72<=no<=92 and re.match(r'^\| \d+ \|',l):
  cells=[c.strip() for c in l.split('|')[1:-1]]
  for item in re.findall(r'[A-Z][A-Z0-9_]+',cells[1]):formalfling[item]={'power':int(cells[0]),'line':no}
fling=[]
for l in (P/'pbs-fling-projection.txt').read_text().splitlines():
 m=re.match(r'(\d+) \[([^\]]+)\] Flags=(.*)',l)
 if not m:continue
 line,item,flags=m.groups();powers=[int(x.split('_')[1]) for x in flags.split(',') if re.fullmatch(r'Fling_\d+',x,re.I)]
 got=formalfling.get(item)
 fling.append({'id':item,'pbs_section_start':int(line),'complete_flags':flags.split(','),'source_power':powers[0] if powers else None,'formal':got,'status':'SUPPORTED_SOURCE_STATIC' if got and got['power']==powers[0] else 'MISMATCH','consumer_fact':'R011','premise':'Only this registered default field; ordinary active/losable/prefix/berry-use/target/after-use gates still apply.'})
save('fling-data-reception.json',{'rows':fling,'source_fields':len(fling),'formal_fields':len(formalfling),'all_equal':len(fling)==len(formalfling) and all(x['status']=='SUPPORTED_SOURCE_STATIC' for x in fling),'field_projection_scope':load(P/'pbs-fling-projection.json'),'behavior_execution':'NOT_EXECUTED'})

payloads=[]
for kind in ['reference','formal']:
 for row in rs[kind]:
  ap=Path(row['repo'])/row['path'];n=len(ap.read_text().splitlines());own=[(p,d) for p,d in logs if d['path']==str(ap)]
  iv=merged([(d['start_line'],d['end_line']) for p,d in own]);gaps=complement(iv,n)
  ch=next((r for r in cl['payloads'] if r['payload'].split(':',1)[-1]==row['path'] and r['status'] in ['FULL_READ','FULL_READ_DEPENDENCY']),None)
  reviewer='/root/com_move'
  evidence=[str(p.relative_to(P)) for p,d in own]
  if gaps and ch:
   reviewer='/root/com_move/attributes_calling';iv=ch['continuous_intervals'];gaps=complement(iv,n);evidence=['subreviews/attributes_calling/reading-ledger.json','subreviews/attributes_calling/evidence/commands.jsonl','subreviews/attributes_calling/evidence/io-location-resolution.json']
  payloads.append({'kind':kind,'payload':row['path'],'frozen_commit':row['commit'],'sha256':sha(ap),'bytes':ap.stat().st_size,'identity_matches':sha(ap)==row['sha256'],'total_lines':n,'reviewer':reviewer,'received_by':'/root/com_move','status':'FULL_READ' if not gaps else 'UNREAD_GAP','continuous_intervals':iv,'unread_intervals':gaps,'original_read_io':evidence,'semantic_evidence':['semantic-notes.json','forward-mapping.json','reverse-mapping.json'] if reviewer=='/root/com_move' else ['subreviews/attributes_calling/unit-facts.tsv','subreviews/attributes_calling/main-breakdown.tsv','subreviews/attributes_calling/forward-mapping.json','subreviews/attributes_calling/reverse-mapping.json']})
deps=[]
for path in sorted({d['path'] for p,d in logs if d['path'].startswith(str(R)+'/')}):
 if any(row['kind']=='reference' and str(R/row['payload'])==path for row in payloads):continue
 ap=Path(path);n=len(ap.read_text().splitlines());ls=[(p,d) for p,d in logs if d['path']==path];iv=merged([(d['start_line'],d['end_line']) for p,d in ls]);gaps=complement(iv,n)
 deps.append({'payload':str(ap.relative_to(R)),'reviewer':'/root/com_move','sha256':sha(ap),'bytes':ap.stat().st_size,'total_lines':n,'continuous_intervals':iv,'unread_intervals':gaps,'status':'FULL_READ_DEPENDENCY' if not gaps else 'RELEVANT_COMPLETE_UNITS_OR_FIELDS_READ','boundary':'Partial entries grant only the actual complete definitions/fields documented in dependency-facts; no whole-file credit.','original_io':[str(p.relative_to(P)) for p,d in ls]})
ledger={'schema':'r8-com-move-reading-ledger-v2','reviewer':'/root/com_move','updated_utc':now(),'primary_readset':'../../delegation/readsets/com_move.json','primary_payloads':payloads,'primary_full_reference':sum(r['kind']=='reference' and not r['unread_intervals'] for r in payloads),'primary_full_formal':sum(r['kind']=='formal' and not r['unread_intervals'] for r in payloads),'primary_unread_files':sum(bool(r['unread_intervals']) for r in payloads),'dependencies':deps,'named_child_ledger':'subreviews/attributes_calling/reading-ledger.json','semantic_credit':'All primary actual contents read and interpreted. Intervals, regexes and counts locate/validate evidence only; they do not themselves grant semantic credit. 13R/9formal own continuous reads, 2R/2formal named child full reads received via complete actual fact/compound/vector artifacts.','body_assertion_groups':'reverse-mapping.json','vectors':'vector-review.json','data_fields':['fling-data-reception.json','subreviews/attributes_calling/reverse-mapping.json','subreviews/attributes_calling/stage-table-reception.json'],'not_global_domain_completion':'Whole COM-BATTLER and COM-ABILITY-ITEM formal-domain reverse reception, root history/public tasks, remain separately owned.','execution':'NOT_EXECUTED','behavior_runs':0}
save('reading-ledger.json',ledger)

# Bind all ten exact Battler source files to actual named human/model readings.
br=load(T/'delegation/readsets/com_battler.json');brows=[]
for r in br['reference']:
 ap=Path(r['repo'])/r['path'];name=ap.name;idx=int(name[:3]);k='Battler%03d'%idx if idx<=6 else {7:'BattlerUse',8:'BattlerTarget',9:'BattlerSuccess',10:'BattlerTrigger-sub'}[idx]
 entry=D[k];brows.append({'path':r['path'],'sha256':sha(ap),'expected_sha256':r['sha256'],'bytes':ap.stat().st_size,'identity_matches':sha(ap)==r['sha256'],'full_source_read':True,'continuous_interval':[1,len(ap.read_text().splitlines())],'reviewer':entry.get('reviewer','/root/com_move'),'receiver':'/root/com_move','source_fact_key':k,'facts':entry['facts'],'boundary':'Exact source full read and these actual facts accepted. No implied acceptance of every formal clause in com_battler readset.'})
save('battler-reception.json',{'schema':'r8-com-move-battler-source-contribution-v1','readset':'../../delegation/readsets/com_battler.json','reference_commit':rs['reference'][0]['commit'],'rows':brows,'source_full_read':10,'source_unread':0,'formal_domain_reverse_reception':'OPEN_NOT_CLAIMED','update_status':'UPDATE_NOT_STARTED','behavior_execution':'NOT_EXECUTED'})
save('ability-item-source-reception.json',{'reviewer':'/root/com_move','reference_commit':rs['reference'][0]['commit'],'source_entries':[r for r in deps if r['payload'].endswith(('008_Battle_AbilityEffects.rb','009_Battle_ItemEffects.rb'))],'facts':{k:D[k] for k in ['AbilityEffects','ItemEffects','AbilitySpeedWeight','AbilityStatuses','AbilityAccuracy','AbilityCritical','AbilityInnards','ItemStatuses','ItemHit','Battler006','Rewards','ActiveSitrus','Catch','Running']},'finite_catalog_reception':'All AB01–25 and HI01–36/HI10a–f shared catalog rows read and specifically checked in vector-review. WP48§9 full unit and WP50coverage full read added for identity counts.','formal_domain_reverse_reception':'OPEN: does not claim full WP48/WP49/WP50 formal body acceptance.','behavior_execution':'NOT_EXECUTED'})

# Each catalog row receives an actual per-vector proof written by the reader,
# or the named child exact full input/expectation/proof. No proof is inferred
# from a line, delimiter, effect name, or a generated identifier.
notes={l.split('\t',1)[0]:l.split('\t',1)[1] for l in (P/'vector_notes.tsv').read_text().splitlines() if '\t' in l}
byline={r['catalog_line']:r for r in cr['vectors']}
vectors=[];missing=[]
for filename in ['combat-requirements-wp47-ab.md','pokemon-rules-wp43-44-46-48-50.md']:
 path=W/'deliverables/final-specification-set/test-catalog'/filename
 for no,l in enumerate(path.read_text().splitlines(),1):
  if not l.startswith('|'):continue
  cols=[v.strip() for v in l.split('|')[1:-1]]
  if not re.match(r'(?:[A-Z]+|C01|R[57]|U04)[A-Za-z0-9-]*\d',cols[0]):continue
  raw=cols[0];ch=byline.get(no) if filename=='combat-requirements-wp47-ab.md' else None
  if ch and ch['primary']:
   vectors.append({'catalog':str(path.relative_to(W)),'line':no,'catalog_id':raw,'canonical_id':ch['id'],'full_input':cols[1],'full_expected':cols[2],'reviewer':ch['reviewer'],'receiver':'/root/com_move','actual_semantic_check':ch['check'],'source_facts':ch['source_facts'],'status':'SUPPORTED_DERIVED_VECTOR','execution':'NOT_EXECUTED','evidence':'subreviews/attributes_calling/reverse-mapping.json'})
  else:
   proof=notes.get(raw)
   if not proof:missing.append([filename,no,raw])
   family='AB/HI shared finite source reception' if raw.startswith(('AB','HI')) else 'COM-MOVE primary'
   vectors.append({'catalog':str(path.relative_to(W)),'line':no,'catalog_id':raw,'canonical_id':ch['id'] if ch else raw,'full_input':cols[1],'full_expected':cols[2],'reviewer':'/root/com_move','actual_semantic_check':proof,'status':'SUPPORTED_DERIVED_VECTOR' if proof else 'MISSING_SEMANTIC_PROOF','scope':family,'premise':'Entire common fixture immediately preceding this row plus this independent variation, not silently assuming a tested failure gate passed. Source facts preserve exact phase/prefix/current-value consumers; unrelated callbacks and host continuation excluded only where fixture says so.','source_evidence':['semantic-notes.json','dependency-facts.json','registry-validation.json' if raw in ['AB25','HI36'] else 'reverse-mapping.json'],'execution':'NOT_EXECUTED'})
save('vector-review.json',{'schema':'r8-com-move-actual-vector-reception-v1','updated_utc':now(),'rows':vectors,'catalog_rows':len(vectors),'actual_semantic_proof_missing':missing,'named_child_primary':sum(v['reviewer']=='/root/com_move/attributes_calling' for v in vectors),'own_actual_checks':sum(v['reviewer']=='/root/com_move' for v in vectors),'behavior_runs':0,'execution':'NOT_EXECUTED','boundary':'Every row is the actual source-static / independent arithmetic judgment of its full stated premise. No Ruby/game/model/simulator vector was run. Full AB/HI formal-domain review remains with its own primary.'})
print(json.dumps({'primary':{'R':ledger['primary_full_reference'],'formal':ledger['primary_full_formal'],'unread':ledger['primary_unread_files']},'vectors':len(vectors),'missing_vector_proofs':missing,'registry_counts':{'ability':{k:v for k,v in registries['ability_calculation'].items() if k!='rows'},'item':{k:v for k,v in registries['item'].items() if k!='rows'}},'fling':{'source':len(fling),'formal':len(formalfling),'all_equal':all(x['status']=='SUPPORTED_SOURCE_STATIC' for x in fling)}},ensure_ascii=False))
