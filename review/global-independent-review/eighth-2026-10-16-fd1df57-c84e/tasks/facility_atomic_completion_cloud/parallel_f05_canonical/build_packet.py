from pathlib import Path
import json, hashlib, subprocess, datetime

B = Path('/workspace/pokemon-essentials-clean-room')
R = Path('/workspace/pokemon-essentials')
RR = B / 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
V = RR / 'tasks/facility_atomic_completion_cloud/v2'
OUT = RR / 'tasks/facility_atomic_completion_cloud/parallel_f05_canonical'
ME = '/root/facility_atomic_completion_cloud/f05_canonical_tail'
BC = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
RC = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
FORMAL = 'deliverables/final-specification-set/combat-requirements/wp58-battle-recording-and-playback.md'
UTC = datetime.datetime.now(datetime.timezone.utc).isoformat()

def digest(data): return hashlib.sha256(data).hexdigest()
def dump(name, data):
    (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def identity(repo, path, commit):
    p=repo/path; data=p.read_bytes()
    blob=subprocess.check_output(['git','-C',str(repo),'rev-parse',commit+':'+path],text=True).strip()
    fixed=subprocess.check_output(['git','-C',str(repo),'show',commit+':'+path])
    assert data==fixed, path
    return dict(repo=str(repo),commit=commit,tree=subprocess.check_output(['git','-C',str(repo),'rev-parse',commit+'^{tree}'],text=True).strip(),path=path,bytes=len(data),sha256=digest(data),blob=blob,mode='100644')
def packet_id(name):
    data=(V/name).read_bytes()
    return dict(path='tasks/facility_atomic_completion_cloud/v2/'+name,bytes=len(data),sha256=digest(data))
def aa(*nums): return ['FAC-A%04d'%n for n in nums]
def nn(*nums): return ['FAC-F05-CN-S%02d'%n for n in nums]
rows=[]
lines=(B/FORMAL).read_text().splitlines()
common='Fixed B8/R default definitions and load order, no later overrides. Each adopted fact keeps its exact own premise, valid actual receiver/registered-data/serializer shape, prior dependency normal-return and explicit failure-prefix qualifications. SOURCE_STATIC/NOT_EXECUTED. No future Ruby helper/API mandate, arbitrary plugin claim, native roundtrip, full battle success or whole-domain approval. Definition audit and ordinary default wiring remain separate.'

def row(line, kind, *components):
    cs=[]
    for i,c in enumerate(components,1):
        meaning, refs, *qual = c
        cs.append(dict(id=f'FAC-F05-CN-L{line:04d}-C{i:02d}',meaning=meaning,support_fact_ids=refs,qualification=qual[0] if qual else common,status='FINITE_STATIC_MEANING_SUPPORTED' if refs else 'FORMAL_PROVENANCE_LAYOUT_OR_SCOPE_DISPOSITION'))
    rows.append(dict(id=f'F05-L{line:04d}',line=line,kind=kind,complete_original_structure=lines[line-1],formal_line_sha256=digest(lines[line-1].encode()),children=cs,status='COMPLETE_MEANING_DISPOSITION_WITH_NAMED_PENDING_FACET' if line==105 else 'COMPLETE_FINITE_STATIC_MEANING_DISPOSITION'))

row(3,'PROVENANCE',('The document classifies recording/playback primarily as combat, with serialization/persistence and replay presentation boundaries; it describes implementation-independent requirements.',[]))
row(5,'PROVENANCE_AND_SCOPE',
    ('This is the current sanitized WP58 text; provenance and the audit-traceability destination are document navigation, not new source behavior.',[]),
    ('A–F enumerate the lifecycle/persistence, eighteen initial keys/five components, actual-action versus recording versus playback, random/switch sequences, array/layout limits, mode differences and ending boundaries addressed below.',[]),
    ('The scope excludes universal arbitrary-battle, version/implementation equivalence, runtime confirmation and a replay sandbox guarantee; own review performs zero Ruby/game/native/record/save/model executions.',[]),
    ('The stated WP06 dependency is the finite sequence boundary, not evidence that a seed or a recorded array alone guarantees complete reproduction.',aa(1458,1459,1480,1489)))
row(9,'SCOPE',
    ('WP58 owns what is recorded, its promotion and replay consumption; battle rules, facility session and save system have their separate primary contracts.',[]),
    ('Neither equal seed nor equal record arrays establishes cross-version or cross-implementation reproduction.',aa(1459,1481,1486,1504)))
row(11,'BEHAVIOR',
    ('Challenge factories select recordable Tower/Palace/Arena forms with recorded type 0/1/2.',aa(1409,1410,1411)),
    ('The facility wrapper constructs, sets internalBattle false and performs world preparation before recording start captures current initial fields.',aa(163,164,165,1456,2193,2200)),
    ('Every reached command phase starts a four-slot round; registrations and random/replacement inquiries append or replace at their own actual times.',aa(1460,1462,1465,1468,1470,1472,1473,1475,1476,1479)),
    ('After normal cleanup the wrapper first clears temp and retains a dump for result 1/2/5 only; earlier exceptions are not full cleanup guarantees.',aa(172,173,174,175,184,185,2206)),
    ('Promotion assigns temp to global lastbattle then clears temp; the global object is a saved value, conditional on normal serialization and load.',aa(225,226)+nn(8)),
    ('Replay restores a nonabsent record, dispatches type, runs its battle; debug number/file helpers use Battles/Battle%03d.dat.',aa(227,228,229,230,231,232,2128,2129)+nn(12)))
row(13,'BEHAVIOR_AND_SCOPE',
    ('No ordinary script caller of event-facing pbRecordLastBattle/pbPlayLastBattle/pbDebugPlayBattle was found in the complete fixed Data/Scripts name search; calls among playback helpers remain explicit.',nn(12)),
    ('Event reachability requires unavailable maps/events; debug replay is an independent callable definition.',nn(12),'SOURCE_STATIC name census; no event reachability or absence of arbitrary dynamic calls inferred.'),
    ('Playback classes use the playback module and have no record-production hooks; they do not assign the recorder arrays or global/temp record fields.',aa(1504,1505,234)))
row(17,'LAYOUT',('Introduces the two storage locations, whose semantics are carried by the following two rows.',[]))
row(19,'LAYOUT',('Table columns distinguish storage location, persistence character, and write/clear timing; the heading adds no third location or behavior.',[]))
row(21,'BEHAVIOR',
    ('The temporary record is the Game_Temp field and is absent from the default saved-value registrations.',nn(8)),
    ('At the normal wrapper tail old temp is cleared and only 1/2/5 replaces it with opaque dump bytes.',aa(172,173,174,175,2206)),
    ('Debug skip clears before its normal true return, after the three messages and before MEStop; a message failure can preserve the previous record and MEStop failure keeps nil.',aa(158,159,2201,2286,2287),'Root FAC-W04 bounded NO_REQUIRED scope retained exactly; this row does not reverse the source message-before-clear order.'))
row(22,'BEHAVIOR',
    ('The global lastbattle field defaults nil and belongs to the whole saved global-metadata object.',nn(8)),
    ('Promotion copies the current temp value to it, then clears temp; omitting promotion leaves this particular temp record unpromoted.',aa(225,226)),
    ('No successful native save/reload follows merely from field inclusion.',nn(8)))
row(24,'BEHAVIOR_AND_ABSTRACTION',
    ('Lifecycle names abstract no recorder object, active recorder arrays/properties, exported temp value, and promoted global value.',aa(1400,1401,1402,1404,1456,1458,172,225,226)),
    ('The normal temporary lifetime ends at a later normally completed wrapper clear/promotion; it is not exception-safe unconditional expiry.',aa(184,185,2286,2206)),
    ('Playback exits through its ordinary end or abort path without exporting or promoting a new record.',aa(1504,1505,1526,234),'Does not mean replay is globally read-only; live Bag/Dex effects below remain operative.'))
row(26,'LAYOUT',('Introduces normal wrapper-result retention rows; the header does not classify an exception as a normally returned decision.',[]))
row(28,'LAYOUT',('Decision, outcome meaning, temp effect and note columns separate result codes from wrapper return booleans.',[]))
row(30,'BEHAVIOR',('Decisions 1/2/5 each permit dump retention, including draw.',aa(173,174,175)))
row(31,'BEHAVIOR',
    ('A normal result 3 clears rather than retains the record.',aa(2206)),
    ('In a facility trainer battle internalBattle false permits the ordinary accepted-forfeit path; rejection/cancellation returns 0 from the attempt rather than a successful forfeit.',aa(164,2202,2203,2205)))
row(32,'BEHAVIOR',
    ('Result 4 is excluded from normal wrapper retention.',aa(172,173,174,175)),
    ('Normal facility trainer input rejects the item menu and has no ordinary capture route; the helper capture mechanics are not a broad replay sandbox.',nn(11),'No claim that arbitrary injected Snag Ball/Shadow state, direct internal helper or modified recording is impossible.'))
row(33,'BEHAVIOR',
    ('A normally returned decision 0 is excluded from retention.',aa(172,173,174,175)),
    ('Debug skip is a separate early true return with messages before clearing and no battle construction, rather than a constructed battle assigned decision 0.',aa(159,2201,2286,2287),'The table is lifecycle grouping, not a promise that debug skip writes a battle decision; root W04 finite interpretation retained.'))
row(35,'BEHAVIOR_AND_LIMIT',
    ('Dump requests one opaque runtime-serialized byte string and adds no explicit format version.',aa(1458,1459)),
    ('Party/start/item/rule snapshots and trainer fields retain runtime class/registry/object compatibility premises.',aa(1426,1428,1430,1432,1444,1454,1485,1515,1516,1517)),
    ('Native format/graph compatibility remains unexecuted, not a new validated portable interchange format.',[]))
row(39,'BEHAVIOR',('The five ordered components are battle type, initial properties, rounds, random results, and replacement selections.',aa(1458)))
row(41,'BEHAVIOR',
    ('Properties are replaced at recorder start and captured sequentially before ordinary start; earlier property writes can survive later capture failure.',aa(1419,1456)),
    ('Names/badges use clone; party/start/item/rules use serialization; speech/weather and remaining scalar values are assigned directly.',aa(237,238,1415,1426,1428,1430,1432,1434,1436,1438,1440,1442,1444,1446,1448,1450,1452,1454)),
    ('Trainer metadata and party byte snapshots remove the original live trainer/party references from the normal replay reconstruction; this is field-specific rather than a universal deep-copy or sandbox claim.',aa(1423,1425,1427,1429,1485,1510,1511,1512,1513),'Normal normalized trainer-array inputs; root FAC001 bare-helper defect remains audited and NO_REQUIRED only within its exact product-surface scope.'))
row(43,'LAYOUT',('Keys, captured content and qualifications are separate columns; composite labels party1/party2 etc represent separate keys in the eighteen-key count.',[]))
row(45,'BEHAVIOR',
    ('Records current internalBattle; normal facility wrapper sets it false before preparation/start.',aa(164,1420)),
    ('False internalBattle blocks the ordinary item menu while permitting confirmed trainer forfeit.',nn(11)+aa(2202,2203)))
row(46,'BEHAVIOR',
    ('Nonnil normal player trainers are normalized to an array; each metadata tuple contains trainer type, cloned name, full id and cloned badges.',aa(236,237,238,1412,1413,1417)),
    ('Absent trainer stays nil, and an empty trainer array stays empty; this does not approve the separate direct bare-trainer helper.',aa(235,236),'Root FAC001 retained; no new public metadata helper requirement.'))
row(47,'BEHAVIOR',
    ('Opponent array entries contain current type, cloned name, id, lose speech and win speech in order.',aa(236,1414,1415,1416)),
    ('Missing/false speech uses ellipsis; speech itself is assigned rather than cloned.',aa(239,240),'Normal NPC array entries; a failing getter can stop later capture without rollback.'))
row(48,'BEHAVIOR',('Both party object graphs are snapshotted separately and restored into replay battle parties, so replay mutates those copies under the normal serializer premise.',aa(1426,1427,1428,1429,1485)))
row(49,'BEHAVIOR',
    ('Both party-start index arrays are serialized and restored.',aa(1430,1431,1432,1433)),
    ('The facility wrapper does not supply encounter-generated owner offsets; fresh defaults remain [0] for each side.',nn(1)+aa(2193),'Ordinary encounter contrast is provenance to that separate primary; no all encounter-route acceptance.'))
row(50,'BEHAVIOR',('Weather and weather duration are the current field values and are restored directly to the replay field.',aa(1434,1435,1436,1437)))
row(51,'BEHAVIOR',('Current canRun permission is captured and restored directly.',aa(1438,1439)))
row(52,'BEHAVIOR',('Current switchStyle option is captured and restored directly.',aa(1440,1441)))
row(53,'BEHAVIOR',('Current showAnims option is captured and restored directly.',aa(1442,1443)))
row(54,'BEHAVIOR',
    ('Opponent-owner item collection is serialized/restored; the separate ally_items collection is not.',aa(1444,1445)),
    ('The normal facility wrapper supplies no items collection; the base default is nil, rather than a newly populated inventory.',nn(1)+aa(2193)))
row(55,'BEHAVIOR',
    ('Captures and restores the current prepared backdrop and base values.',aa(1446,1447,1448,1449,2200)),
    ('Preparation uses explicit/next/world/map background priority and indoor1 fallback; base can remain nil when no valid base is assigned.',aa(2194,2195,2196,2197)))
row(56,'BEHAVIOR',
    ('Time and environment are the captured prepared values, restored without real-time preparation.',aa(1450,1451,1452,1453,2200)),
    ('Map Cave forces time 2 independently of explicit chosen environment; non-Cave uses enabled time shading or retains its prior time.',aa(2198,2199)),
    ('Environment is explicit nonnil override or the actual world resolver using map and current/facing terrain with fishing context.',aa(2196)+nn(3)))
row(57,'BEHAVIOR',('The current rules dictionary is serialized and restored; this records rule flags rather than every facility modifier or layout.',aa(1454,1455,2158)))
row(59,'BEHAVIOR',
    ('Construction precedes world preparation and recorder capture; constructor empty/nil/0/None values are not the normal snapshot contract.',aa(2192,2193,2200)),
    ('Backdrop priority is explicit nonnil override, next backdrop, surfing water, nonempty map backdrop, fallback indoor1; explicit empty string remains truthy and suppresses fallback.',aa(2194)),
    ('Base uses explicit nonnil value or chosen environment configuration, and writes only a truthy result.',aa(2196,2197)),
    ('Environment resolver includes map/terrain/fishing, with explicit override taking priority.',aa(2196)+nn(3)),
    ('Map Cave time2 is independent of environment override; otherwise enabled shading maps one current-time value to day/evening/night 0/1/2, while disabled shading can retain0.',aa(2198,2199)),
    ('Replay restores recorded values without another world prepare; debug skip never reaches capture, and prepare errors do not promise capture or rollback.',aa(2193,2200,2201)))
row(61,'BEHAVIOR',
    ('The eighteen recorded keys omit both side sizes; fresh ordinary playback defaults to 1v1.',aa(1456,2157)),
    ('Double modifier calls the layout setter without persisting a layout rule key, and replay does not reapply the facility factory.',aa(2158)),
    ('Valid ordinary double record replay can therefore reach absent battlers at nonempty Fight positions2/3; this is instruction-family-specific and conditioned on normal earlier startup.',aa(2157,2158,1503)),
    ('Party-order arrays and the listed switch/lose/control/EXP/money/ball/box/Mega options remain newly constructed defaults rather than restored complete state.',nn(1)+aa(2152)))
row(63,'BEHAVIOR',
    ('Each reached recording command phase begins one round with four independent empty slots; normal single selections use positions0/1.',aa(1475,1476,2133)),
    ('Assignments to higher valid battler indices can extend the recorded round, while the replay loop visits only indices0..3.',aa(1462,1494),'Array indexed-assignment language semantics; no actual larger-layout game execution.'))
row(65,'BEHAVIOR',
    ('Random and inquiry results append to separate ordered arrays; no explicit capacity limit or per-entry validation appears in these wrappers.',aa(1400,1402,1460,1461,1479,1481)),
    ('Replay likewise reads raw next entries rather than repairing their types or bounds.',aa(1487,1488,1489,1490)))
row(67,'BEHAVIOR',
    ('Recording omits Mega state but does not cancel original manual/AI registration or a reached qualified Mega executor.',aa(2143,2144,2146,2147,2148,2149,2150,2151,2152)),
    ('Normal Palace player automatic Fight and AI AutoFight return before ordinary Mega registration; qualification alone adds none, pending nonnegative entries reset each command phase, external/debug injection is outside that contrast.',aa(2145,2146,2147,2153,1297)),
    ('Replay starts with new Mega pending state and does not reconstruct an omitted toggle.',aa(2152)),
    ('Shift/Call mutate actual choices but have no recorder hooks; an originally empty slot stays empty, whereas a previously recorded successful choice survives cancel/reselect until another recording write replaces it.',aa(2131,2132,1464,1476,1504)),
    ('Ally item collection, AI scoring state, live Bag/money, RNG seed and presentation state are absent from the eighteen keys/five-component record; live replay dependencies remain separate.',aa(1444,1456,1458,1481,2223)),
    ('Only the promotion helper moves these temp bytes into global persistence; ordinary record storage override is empty and facility capture input remains unavailable.',aa(225,226,1478)+nn(8,11),'CD003 optional attribution limited to WP26 is retained; playback has no empty-store override.'))
row(71,'BEHAVIOR',('Each command phase increments round index and initializes the round before ordinary command work; every later successful recording registration replaces that slot rather than appending a selection history.',aa(1462,1464,1472,1473,1475,1476,1477)))
row(73,'LAYOUT',('Command kind, recorded slot and registration/failure timing are separate columns; the numeric command tag is distinct from a battle decision.',[]))
row(75,'BEHAVIOR',
    ('Successful normal move registration records tag0 and its move index; failed registration preserves the old slot.',aa(1392,1462,1463)),
    ('A reached later target registration writes element2.',aa(1465)))
row(76,'BEHAVIOR',
    ('Automatic entry returns from inherited logic then replaces the whole slot with [0,-1].',aa(1470)),
    ('A target written by nested automatic logic is lost by that whole-slot replacement.',aa(1471)),
    ('The inherited Encore/no-usable-move decision is conditional on its normal gates.',nn(2)))
row(77,'BEHAVIOR',
    ('Palace category selection registers an actual selected move index or -2 when no category move exists.',aa(1256,1264,2153)),
    ('The -2 choice carries the Struggle object but fails the incapable check before ordinary attack hit processing, once earlier checks pass.',aa(2153,2154)),
    ('Playback passes -2 through Palace inherited ordinary registration and retains the same incapable sentinel rather than converting it to a successful Struggle.',aa(1498,2155)),
    ('Palace registration does not repeat the ordinary full move-eligibility check.',aa(1254,1255,1256,1257,1264)))
row(78,'BEHAVIOR',
    ('A successful item registration stores tag1,item,target,move index after base registration returns.',aa(1393,1473)),
    ('Base registration writes actual choice before consuming a consumed player-owned item from the current Bag; unused-item return is a separate cancel/end path.',aa(2142), 'CAR-FAC-BIND-05 full fact and normal-prefix conditions also apply; not atomic registration/refund.'),
    ('Normal facility internalBattle false blocks menu entry, without validating arbitrary replay BAG data.',nn(11)+aa(1501,2142)))
row(79,'BEHAVIOR',('A successful inherited switch registration records tag2 and party index; falsy failure preserves the prior recorded slot.',aa(1394,1472)))
row(80,'BEHAVIOR',
    ('A normally returned run attempt records tag3 and the then-current decision independently of its method return value.',aa(1395,1468,1469,2204)),
    ('Actual failed fleeing gives decision0/return-1 and stops later choices; successful escape/accepted forfeit gives decision3/return1, which normal facility cleanup excludes from saved temp.',aa(2202,2205,2206)),
    ('Unavailable/declined forfeit returns0 and can continue selection despite the same initial recorded [3,0]; debug outcomes retain their separate actual return/decision distinctions.',aa(2203,2204,2205,2207)))
row(81,'BEHAVIOR',
    ('Normal target selection cancellation returns before target registration, leaving its previous recorded target unchanged.',aa(2130)),
    ('A confirmed target writes element2 after actual target choice; direct target write without a prior command can create [nil,nil,target].',aa(1465,1466,1467)),
    ('That incomplete nonempty slot clears its actual choice on replay but matches no command tag.',aa(1497,1504)))
row(83,'BEHAVIOR',
    ('There are four recorded command families and the -1 automatic/-2 Palace move sentinels; a forced/unselected unwritten position stays an empty array.',aa(1392,1393,1394,1395,1470,1476,2153)),
    ('Actual Shift/Call have no corresponding recording hooks, so initial empty and previously recorded slots have different results.',aa(2131,2132,1476)),
    ('Cancel/back does not clear a recorder slot; only a later reached recording write replaces it, and a failed registration can leave old content.',aa(1463,1472,1473,2131)))
row(85,'BEHAVIOR',
    ('Ordinary recording uses the base player/AI command loops and their common registration calls.',aa(2130,2133),'CAR-REC-CMD-01/02 received in full; AI choice quality is outside this recording claim.'),
    ('Recording defines no cancel/back override, so actual cancellation and recorded data are distinct.',aa(2131,2132)))
row(91,'BEHAVIOR',
    ('Ordinary Battle random delegates global rand; the recorder appends the result only after inherited return.',aa(1522,1479,2208,2209,2210)),
    ('Replay takes the next stored entry and increments without resampling or applying the supplied bound.',aa(1489,1490,2210)))
row(93,'SCOPE',('The following rows are categories of actual calls reaching the recorder entry; a domain name alone does not force a draw or certify all members of that subsystem.',aa(1480),'Domain rows are conditional mechanism coverage, not an all-CORE audit or fixed call-count guarantee.'))
row(95,'LAYOUT',('Domain and recording-boundary columns distinguish a caller family from the actual dispatch point.',[]))
row(97,'BEHAVIOR',('Full priority calculation shuffles through Battle.pbRandom before equal-priority/subpriority/speed ties consume its stored order; partial recalculation reuses it.',aa(2211)))
row(98,'BEHAVIOR',
    ('Reached ordinary accuracy and additional-effect calls use the battle entry, with earlier skip/always-hit/chance guards preserved.',aa(2212,2213,2214,2215)),
    ('Concrete sleep/confusion-duration and variable-multihit definitions use the same battle entry; positive explicit durations or fixed-hit branches need not draw.',nn(9)),
    ('Candidate target selection and named calculation branches route through battle random when their actual finite guards reach that call.',nn(9)+aa(2213,2220),'This row lists mechanism domains; it does not claim every move or candidate calculation always draws or has been approved as a whole domain.'))
row(99,'BEHAVIOR',
    ('Random ally/foe target helpers sample eligible candidates through battle random only for nonempty candidate sets.',nn(9)),
    ('Random replacement selects eligible team index through battle random and bypasses inquiry/switch sequence.',aa(2171,2172)+nn(5)))
row(100,'BEHAVIOR',
    ('Actual ability/item handler calls using Battle.pbRandom enter the stream; concrete contact-effect, Quick Claw and EOR Harvest bodies demonstrate these named families.',nn(10)),
    ('Conditional guards, deterministic sunny Harvest and other earlier exits do not invent random calls; only the actual wrapper traffic is covered.',aa(1480,2210)+nn(10)))
row(101,'BEHAVIOR_AND_SCOPE',
    ('Normal capture shake calculation uses the battle entry for reached critical/shake trials, and its successful branch feeds capture reception.',nn(11)),
    ('Normal facility item/menu gates make capture unavailable here; detailed capture/receiver correctness is owned by WP38/62 rather than newly approved by this domain label.',nn(11)+aa(1478)))
row(103,'BEHAVIOR',('Safari has its own direct global-rand implementation rather than this RecordedBattle wrapper/Playback cursor.',aa(1567)))
row(105,'BEHAVIOR_WITH_PENDING_ATTRIBUTION',
    ('AI random delegates global rand, so actual AI weighted/switch/move-selection draws and Palace sampling bypass recorder RNG; final successful commands still record.',aa(2216,2217,2218,2219)),
    ('The AI-scoring-noise phrase describes any actual AI-domain draws and does not establish an extra random-noise operation in the complete central scoring body, which has none.',aa(2218),'Full central GetMoveScore bodies received; no conclusion about all score-handler semantics or a universal noise step.'),
    ('Escape-chance calculation is an explicit mechanics-facing AI-random counterexample; reached rate<256 draws are outside recorder RNG.',aa(2224)),
    ('A tied Shell Side Arm category calculation uses global rand while command_phase is true and the battle entry outside it.',aa(2220,2221,2222)),
    ('Ordinary animation/global random is outside the recorder entry; no realized pixel/native rendering result follows.',aa(1480)),
    ('The exact statement that debug-scene random is merely presentation is pending bounded independent/root scope disposition: its complete definitions can return command, target and party selections, while normal facility/replay uses Scene and the sole default generator caller sets controlPlayer true. Current WP76§7.2 already explicitly preserves both direct-helper behavior and normal AI bypass.',aa(1782,1783,1784,1785,1786,1810,1811,1812,1813)+['UNIT:normal_scene_factory','FORMAL:WP76:167-168'],'PENDING_PARENT_AND_DIFFERENT_CONTEXT_COUNTERREVIEW; proposed scope/attribution candidate only, required/optional classification unassigned. Existing facts reused, zero new debug-scene source atoms.'),
    ('Normal end world Pokerus propagation uses direct global random and is gated internalBattle; normal facilities have it false.',aa(164),'CAR-FAC-BIND-01 full received normal-end fact; exact normal_end unit405–512 remains source support, no whole world/contagion approval.'))
rows[-1]['children'][5]['status']='PENDING_INDEPENDENT_SCOPE_DISPOSITION'
row(109,'BEHAVIOR',
    ('Both sides share an ordered inquiry-result sequence; normally returned party indices and cancellation -1 are appended after the inherited inquiry returns.',aa(1460,1461,2166)),
    ('The replay inquiry consumes the next raw entry and advances its own cursor without invoking selection UI.',aa(1487,1488,2166)))
row(111,'LAYOUT',('The source, timing/owner/qualification, and recording/playback columns distinguish inquiry origin and its actual consumer time.',[]))
row(113,'BEHAVIOR',
    ('Reached ordinary EOR opponent or partner trainer replacement uses that owner inquiry; wild opponents do not replace.',nn(7)),
    ('Recording appends the returned index and replay consumes at the same reached replacement point.',aa(1460,1487,2166)))
row(114,'BEHAVIOR',
    ('Ordinary facility trainer player replacement requires an in-bounds present healthy non-egg nonactive same-owner party member.',aa(2162)+nn(7)),
    ('Reached owner inquiry appends the selected index and replay returns the stored entry without a current party dialog.',aa(2165,2166)))
row(115,'BEHAVIOR',
    ('Default TELEPORT/UTURN/FLIPTURN/VOLTSWITCH/PARTINGSHOT/BATONPASS map to the fully read self-switch families; reflected Parting Shot chooses its actual reflected switcher.',nn(4)+aa(2160,2161,2163,2164)),
    ('After-move target item/ability and user after-use processing can reach EJECTBUTTON/EJECTPACK/EMERGENCYEXIT/WIMPOUT owner-choice replacement under their distinct living/hit/bench/trap/earlier-switch/Pursuit/ability/item guards.',nn(4,5,6)+aa(2163,2164,2167,2182,2186,2187)),
    ('The inquiry path has no internalBattle=true requirement; it records a switch result, not a random candidate result, at the reached attack-after-use consumer.',aa(2165,2166)+nn(4,5,6)),
    ('Reached attack replacement clears the actual choice and does not edit the original recorded action; the replacement has no ordinary additional action that round.',aa(2164,2169)+nn(4,5,6)),
    ('That mid-round choice clearing is not a ban on the first later command after initial entry.',aa(2178,2191)))
row(116,'BEHAVIOR',
    ('Opening and ordinary entry run effects first, then in speed order each battler item-on-stat-drop before ability-on-damage, stopping the scan on its first truthy result.',aa(2179)+nn(6)),
    ('Eject Pack requires actual recorded stat loss and effective held item; emergency abilities require effective ability and the strict integer-half crossing flag, not arbitrary HP loss.',aa(2180,2181,2182,2183)+nn(6)),
    ('Their distinct Sky Drop, opposing survival, leave eligibility and same-owner healthy non-egg bench gates still apply.',aa(2162,2186)+nn(6)),
    ('Initial properties are captured before entry, so initial replacement selection can append before the first command round; replay consumes at the analogous entry point.',aa(2178,2179,2166)),
    ('Cleared old choice does not prevent the qualifying replacement participating in the subsequent first command phase; ordinary entry follows its actual reached timing.',aa(2169,2191)))
row(117,'BEHAVIOR',
    ('Reached EOR Eject Pack consumes then recalls/leaves; emergency ability EOR recalls/leaves after its own gates without immediately choosing a replacement.',aa(2190)+nn(6)),
    ('The later actual EOR replacement consumer performs selection and hence appends/consumes the inquiry sequence; this is distinct from immediate attack replacement.',nn(7)+aa(1460,1487)))
row(118,'BEHAVIOR',
    ('Default Roar/Whirlwind/Dragon Tail/Circle Throw use the full forced-random switching families with their distinct gates.',aa(2160,2161,2170,2171)+nn(4)),
    ('Red Card calls random replacement candidate selection; it may have already selected/consumed before a later immunity prevents replacement.',nn(5),'Source request/prefix preserved; table does not guarantee a successful switch merely because a random candidate was drawn.'),
    ('These random candidate routes use the random stream and never the owner-choice inquiry/switch sequence.',aa(2172,2166)+nn(5)))
row(119,'BEHAVIOR',
    ('Optional player switch-style confirmation additionally needs internalBattle, single player side, trainer/opposing replacement, healthy current player, candidate and Outrage gates.',aa(2156,2176)+nn(7)),
    ('False internalBattle excludes only this optional question and its extra player inquiry, not earlier opponent inquiry or attack self-switch paths.',aa(164,2156,2165,2176)))
row(120,'BEHAVIOR',
    ('Arena overrides candidate CanSwitchIn false, so ordinary candidate existence is false and Baton Pass cannot reach its inquiry.',aa(2173,2162,2163)),
    ('Arena fainted replacement advances its sequential party index and directly replaces/enters without owner/random inquiry.',aa(2174,2175)))
row(122,'BEHAVIOR',
    ('Eject Pack consumption precedes its non-EOR selection; a returned negative index still appends and returns false before replacement, with item absent and no restore.',aa(2166,2187,2188)),
    ('Emergency ability negative selection likewise returns false before replacement, but has no Eject Pack item-consumption prefix.',nn(6)),
    ('Returned cancellation, consumed state and successful replacement are separate observations, and exceptions retain their earlier prefixes.',aa(1461,2187,2189)+nn(6)))
row(124,'CATALOGUE_REFERENCE',
    ('W24 has the qualified supplied Baton Pass move/bench/normal attack fixture, appends1 and replays1 after the move.',aa(2159,2160,2161,2162,2163,2164,2166),'All original W24 fixture fields and FAC-RC-W24 children received; no constructor-default move retention inference.'),
    ('W25 contrasts qualified random forced replacement, Arena candidate rejection and internalBattle switch-style confirmation.',aa(2170,2171,2172,2173,2174,2176)),
    ('W26 qualifies real stat-loss/effective Eject Pack initial-entry selection before first command and preserves negative/guard/EOR alternatives.',aa(2177,2178,2179,2180,2181,2182,2183,2186,2187,2189,2190,2191)),
    ('None of the case names guarantees every state of a named move/item/ability succeeds.',[]))
row(128,'LAYOUT',('The aspect-by-mode table compares Tower, Palace and Arena definitions; it adds no fourth mode or automatic equality guarantee.',[]))
row(130,'BEHAVIOR',
    ('Tower and Arena use ordinary registration eligibility; failure itself makes no recording write.',aa(1462,1463,1472,1473,1411)),
    ('Palace automatic result is recorded, including -2 carrier, without ordinary full eligibility retest.',aa(1256,1257,1264,2153)))
row(131,'BEHAVIOR',
    ('Tower execution calls only enter the random stream when they dispatch through the recorder; AI/evaluation draws retain their independent global entry.',aa(1480,2216,2220,2223)),
    ('Palace automatic category/move and HP-dependent switch sampling are global AI random, while selected commands form recorded snapshots.',aa(2219,2153)),
    ('Arena judging and direct sequential replacement do not themselves add RNG; ordinary reached move execution calls retain the recorder boundary.',aa(2174),'CAR-FAC-BIND-03/04 complete finite meanings received; no whole move/ability-domain approval.'))
row(132,'BEHAVIOR',
    ('Tower replay uses its ordinary registration; Palace passes -2 through and later fails incapable rather than performing Struggle.',aa(1498,2154,2155)),
    ('Arena startup resets its judge state, while ordinary sequential entry calls Participated, not the AsActive reset definition.',aa(2175),'CAR-FAC-BIND-03/04 fully received; exact WP56 primary retains count/skill/baseline/changed states.'),
    ('After count reaches3, no reached ordinary replacement reset implies possible consecutive third/fourth/fifth-round judging under the stated living/decision gates.',aa(2174,2175),'CAR-FAC-BIND-03 count increment/judge and CAR-FAC-BIND-04 call binding, conditional on normal prior EOR and no terminal gate.'))
row(136,'BEHAVIOR_AND_LIMIT',
    ('Replay random/switch cursors consume one raw entry then increment; exhausted arrays yield nil and retain the increment.',aa(1487,1488,1489,1490)),
    ('A missing round or nil slot fails earlier at indexing/length; it is not the same immediate behavior as random/switch exhaustion.',aa(1496)),
    ('Later use of nil can fail or diverge where its actual consumer uses it; no uniform downstream failure is invented.',aa(1488,1490,1504)),
    ('Changing random quantity/order/domain across versions or implementations can change replay; no explicit version or seed guarantee exists.',aa(1459,1480,1489,2220)))
row(142,'BEHAVIOR',
    ('Absent nil/false record returns before scene creation; a truthy empty string is not covered by this absence guard.',aa(227)),
    ('For a present record, scene creation and abortable marking precede deserialization and type0/1/2 dispatch.',aa(228,229,230,231,232)),
    ('BGM is resolved from reconstructed opponents and live resolver dependencies, and battle runs in the animation/standby wrapper.',aa(1507,1508,1519,1520,1521)+nn(12)),
    ('Unknown type leaves nil battleplayer and fails at startup only after normal earlier metadata/BGM/animation dependencies.',aa(233,2129)),
    ('Debug number range0..500/cancel-1 selects a formatted file and binary open; missing Battles directory and maps are material limits rather than observed replay execution.',aa(2128)+nn(12)))
row(146,'BEHAVIOR',
    ('Replay restores party graphs and constructs new ordered trainer metadata objects before ordinary battle construction.',aa(1423,1425,1427,1429,1485,1510,1511,1512,1513)),
    ('Start restores all recorded initial fields; it omits layout and does not rerun world preparation.',aa(1421,1431,1433,1435,1437,1439,1441,1443,1445,1447,1449,1451,1453,1455,1486,2157,2200)),
    ('Player badges/NPC speech fields follow their actual constructor/metadata semantics; trainer.party does not automatically alias the restored Battle party arrays and Player type getter retains current-metadata dependency.',aa(1511,1512,1514,1515,1516,1517,1518)),
    ('Copies are not global isolation, as the explicit live Bag and Dex consumers below show.',aa(2142,2136,2137)))
row(148,'BEHAVIOR',('Normal replay trainer/party object mutations use newly constructed/restored objects and do not write those fields back to the original live trainer/party; this does not isolate callbacks/global dependencies.',aa(1423,1425,1427,1429,1485,2136)))
row(149,'BEHAVIOR',
    ('Playback BAG dispatch directly re-registers item/target/move through base registration.',aa(1501,2142)),
    ('Nil or nonconsumed item skips removal; a consumed player-owned item removes from current live Bag and raises if unavailable after the choice was already written.',aa(2139,2140,2141,2142)),
    ('Player ownership is side/owner index routing, not equality of reconstructed trainer object and original player.',aa(2142),'CAR-FAC-BIND-05 base ownership route received; no inventory snapshot restore or arbitrary item-effect success.'))
row(150,'BEHAVIOR',
    ('Normal replay end invokes the ordinary Peer leaving callback on copied party members with actual party-index flags and endBattle true.',aa(2135,2136),'CAR-FAC-BIND-01 normal terminal ordering/receivers retained.'),
    ('Qualified form commit directly registers current global player Pokedex with no internalBattle gate; copied Pokemon state can therefore cause a global Dex write.',aa(2136,2137,2138)),
    ('BURMY party index0 initially in slot0 has true written/read flag; endBattle plus Cave plus oldform0 yields form1 and preserves the default noncollapsed form1 Dex identity.',aa(2134,2135,2136,2137,2138)),
    ('Party index1 only entering slot0 writes flag0, while the terminal read uses flag1 false; actual participation alone is insufficient and form0 remains.',aa(2134,2135,2136)))
row(152,'BEHAVIOR',('Facility item menu restriction is an input gate; direct replay BAG data is not rejected by that menu and has live Bag effects.',nn(11)+aa(1501,2142)))
row(156,'BEHAVIOR',
    ('Only player replay loop advances round; it visits four slots0..3, skips empty arrays, clears nonempty actual choices and ignores higher recorded positions.',aa(1492,1493,1494,1495,1497)),
    ('FIGHT -1 invokes automatic false-message entry; other indices including -2 use ordinary registration, with optional recorded target afterwards and unchecked registration return.',aa(1498,1499,1500,2154,2155)),
    ('BAG directly calls base registration and can remove/fail against current consumed-item Bag state; nil/nonconsumed items skip.',aa(1501,2142)),
    ('POKEMON invokes inherited switch registration; RUN merely assigns the recorded decision.',aa(1502,1503)),
    ('Missing default1v1 positions2/3 fail in commands reading a missing battler such as Fight; RUN itself does not require that battler, so first failure differs by command family.',aa(2157,2158,1503)),
    ('AI loop returns, since both sides already came from slots; malformed/short arrays retain exact earlier failure/prefix rules.',aa(1492,1496,1504,2223)))
row(160,'BEHAVIOR',
    ('Playback regular messages auto-progress and paused-display delegates regular display; exact frame/input results remain unexecuted.',aa(1491,1528,1529,1530,1531,1532)),
    ('The -1 automatic inherited Encore branch can still call scene target selection when non-single and player-owned, even with showMessages=false; normal lost-layout1v1 usually makes that condition false.',nn(2)+aa(2157)),
    ('BACK with abortable/unaborted state marks scene aborted and raises dedicated battle abort; its core rescue sets decision0 and ends scene.',aa(1523,1524,1525,1526,1527)),
    ('Caught abort bypasses ordinary terminal gameplay; ordinary normal completion separately performs scene end, unused choice return, ability switch-out, party0 Peer/form and initial-item writes with prefixes preserved.',aa(1526,2136,2142),'CAR-CRE-F13 and CAR-FAC-BIND-01/05 full meanings received; arbitrary errors/pre-core startup lie outside the dedicated rescue.'),
    ('Neither ordinary replay completion nor abort invokes the facility wrapper restoration/stats/dump/promotion tail, or changes the original party graph.',aa(234,1504,1505,1427,1429),'Global Bag/Dex writes described above remain possible; no universal read-only or rollback inference.'))
row(164,'BEHAVIOR',('Level unadjustment, both-party healing/Mega/Primal/item restoration, facility win/loss counters and temp export are in the organized wrapper; replay does not call that wrapper.',aa(166,167,168,169,170,171,172,173,174,175,176,177,178,179,234)))
row(168,'CATALOGUE_AND_SCOPE',
    ('The referenced RC section contains W01–W28 plus W22b, twenty-nine rows with original IDs distinct from WS W-numbers.',[]),
    ('The whole enumerated topic list is an index into the fully read29 original RC rows and139 individually received finite children, retaining every row fixture and negative alternative.',['RC29-139-COMPLETE-CHILD-RECEPTION'],'The finite packet registry below gives exact source packet refs/child IDs; an overview label does not replace those gates.'),
    ('Failed flee is ret-1, not ret0 cancellation; execution-random-all means actual named wrapper calls, Mega and layout are mode/command qualified, and debug clear-before-return preserves messages-before-clear.',aa(2202,2203,2204,2205,2210,2152,2158,2201,2286,2287)),
    ('All examples remain static/manual, with no actual replay/Marshal/game or simulator run.',[]))
row(172,'CROSSREFERENCE',
    ('Primary dependencies are WP06 random-sequence boundary, WP42 outcome/abort, WP55 wrapper retention and WP56 mode behavior.',[]),
    ('Capture/Dex consumers WP38/62, saved metadata WP09 and unproven video-file producer WP76 are separate finite interfaces.',aa(1478,2136,2142)+nn(8,11,12),'This dependency list is not automatic completion/acceptance of those whole primary files.'))
row(174,'BEHAVIOR_AND_CENSUS',
    ('One five-component record, eighteen property keys, four command families with two move sentinels and types0/1/2 are explicit finite static sets.',aa(1458,1456,1392,1393,1394,1395,1409,1410,1411,1470,2153)),
    ('Replacement scope follows actual behavior/timing rather than direct-text caller count; event-facing promotion/last-play helpers have no ordinary script callers in the fixed census.',aa(2166,2178)+nn(12)))
row(178,'LIMIT_AND_SCOPE',
    ('Versionless runtime-object serialization and changing consumer assumptions do not establish version/implementation equivalence.',aa(1459,1481,1486,1515,1516,1517)),
    ('The exact-file census finds no supplied Battles/*.dat output; generator/replay filename alone does not identify a producer or prove a real video file roundtrip.',nn(12)))
row(179,'EVIDENCE_LIMIT',('Abort key, message progress and frame-by-frame presentation are statically described calls; zero host/UI/native runs were performed, so no realized timing/key/pixel outcome is certified.',aa(1524,1529,1530,1531,1532)))
row(180,'SCOPE_AND_HISTORY',
    ('Facility reception events, Demo/host/media/plugin/outlet coverage are reserved outside this finite recording text; maps/event resources are unavailable here.',[]),
    ('The quoted status language and references to other WPs are document scope/history labels, not a current claim that this child verified their completion or excluded them from the parent full FAC contract.',[]),
    ('Safari/Contest behavior belongs to WP53 rather than RecordedBattle, while their finite random distinction above remains explicitly supported.',aa(1567)))
row(181,'PROVENANCE_AND_SCOPE',('This document submits only its own recording/playback scope, does not approve the whole facility or self-mark Reviewed, and does not claim runtime availability; this child likewise adds no global/FAC PASS.',[]))

assert len(rows)==92
dispatch=json.loads((V/'next-dispatch.json').read_text())
seeds=[x for x in dispatch['unmet_formal_seed_structures'] if x['old_locator_id'].startswith('F05-')]
assert {x['id'] for x in rows}=={x['old_locator_id'] for x in seeds}
rows.sort(key=lambda x:x['line'])

# Each unit below was actually read as the complete named method/class/record,
# or as a complete file. Source text remains a recoverable fixed-Git locator.
units=[]
def unit(key,path,lo,hi,kind='COMPLETE_NAMED_UNIT'):
    ident=identity(R,path,RC); text='\n'.join((R/path).read_text().splitlines()[lo-1:hi])
    units.append(dict(id=key,identity=ident,range=[lo,hi],reading=kind,slice_bytes=len(text.encode()),slice_sha256=digest(text.encode()),recovery='git show '+RC+':'+path+'; select exact inclusive line range; join with LF, no final LF'))

unit('constructor','Data/Scripts/011_Battle/001_Battle/001_Battle.rb',98,174)
unit('auto_and_registration','Data/Scripts/011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb',5,78,'FOUR_COMPLETE_NAMED_METHODS')
unit('environment','Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb',91,108)
unit('switch_move_families','Data/Scripts/011_Battle/003_Move/013_MoveEffects_SwitchingActing.rb',4,255,'SEVEN_COMPLETE_CLASSES')
unit('ejectbutton_redcard','Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb',1525,1573,'TWO_COMPLETE_REGISTRATIONS')
unit('emergency','Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb',367,408,'COMPLETE_REGISTRATION_AND_COPY')
unit('damage_ability_trigger','Data/Scripts/011_Battle/002_Battler/006_Battler_AbilityAndItem.rb',45,49)
unit('hp_change','Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb',5,35,'TWO_COMPLETE_METHODS')
unit('entry','Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb',303,374,'TWO_COMPLETE_METHODS')
unit('eor_switch','Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb',142,217,'TWO_COMPLETE_METHODS')
unit('after_move','Data/Scripts/011_Battle/002_Battler/010_Battler_UseMoveTriggerEffects.rb',1,218,'FULL_FILE_READ')
unit('ability_trigger','Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb',69,73)
unit('ability_hp_trigger','Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb',86,88)
unit('item_target_trigger','Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb',140,142)
unit('handler_symbol','Data/Scripts/003_Game processing/005_Event_Handlers.rb',148,197,'COMPLETE_CLASS')
unit('metadata','Data/Scripts/012_Overworld/002_Overworld_Metadata.rb',1,183,'FULL_FILE_READ')
unit('savevalues','Data/Scripts/002_Save data/004_Game_SaveValues.rb',1,127,'FULL_FILE_READ')
unit('sleep_duration','Data/Scripts/011_Battle/002_Battler/004_Battler_Statuses.rb',321,325)
unit('confuse','Data/Scripts/011_Battle/002_Battler/004_Battler_Statuses.rb',483,497,'TWO_COMPLETE_METHODS')
unit('multihit','Data/Scripts/011_Battle/003_Move/009_MoveEffects_MultiHit.rb',101,115,'COMPLETE_CLASS')
unit('find_targets','Data/Scripts/011_Battle/002_Battler/008_Battler_UseMoveTargeting.rb',36,91)
unit('target_helpers','Data/Scripts/011_Battle/002_Battler/008_Battler_UseMoveTargeting.rb',173,202,'THREE_COMPLETE_METHODS')
unit('effectspore','Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb',1768,1814,'COMPLETE_REGISTRATION')
unit('quickclaw','Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb',648,652,'COMPLETE_REGISTRATION')
unit('harvest','Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb',2497,2512,'COMPLETE_REGISTRATION')
unit('eor','Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb',597,780)
unit('throw_capture','Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb',112,201)
unit('capture_calc','Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb',206,263)
unit('command','Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb',1,265,'FULL_FILE_READ')
unit('recorded','Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb',1,287,'FULL_FILE_READ')
unit('facility_wrapper','Data/Scripts/018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb',1,144,'FULL_FILE_READ')
unit('normal_scene_factory','Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb',204,206)
unit('debug_scene','Data/Scripts/011_Battle/004_Scene/009_Battle_DebugScene.rb',1,106,'FULL_FILE_READ')
unit('ruled_battle','Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/004_ChallengeGenerator_BattleSim.rb',377,438)

primary_records=[]
for path,names in [('PBS/moves.txt',['TELEPORT','UTURN','FLIPTURN','VOLTSWITCH','PARTINGSHOT','WHIRLWIND','DRAGONTAIL','CIRCLETHROW']),('PBS/items.txt',['EJECTBUTTON','REDCARD']),('PBS/abilities.txt',['EMERGENCYEXIT','WIMPOUT'])]:
    ls=(R/path).read_text().splitlines()
    for name in names:
        lo=ls.index('['+name+']'); hi=next((i for i in range(lo+1,len(ls)) if ls[i].startswith('[')),len(ls))
        unit('PRIMARY-'+name,path,lo+1,hi,'COMPLETE_PRIMARY_RECORD')
        primary_records.append('PRIMARY-'+name)

newfacts=[]
def fact(num,meaning,unitids,receivers,qualification=common):
    newfacts.append(dict(id=nn(num)[0],meaning=meaning,complete_source_unit_ids=unitids,formal_receivers=receivers,premise=qualification,evidence='SOURCE_STATIC',execution='NOT_EXECUTED',reader=ME,kind='NECESSARY_NEW_CANONICAL_MEANING_NOT_NEW_PRODUCT_API'))
fact(1,'Fresh playback initializes sideSizes1/1, owner-normalized trainers, items/ally_items nil, order arrays by party length, starts[0], canSwitch true/canLose false/controlPlayer false/EXP-money true/balls enabled/sendToBoxes1 and per-owner Mega pending -1. Recorder restores only its eighteen selected fields, so all other named options remain defaults unless a separate ordinary startup consumer changes them.',['constructor','recorded','facility_wrapper'],[49,54,61])
fact(2,'Inherited automatic move checks fainted/Encore eligibility first. A valid Encore choice returns immediately for single battle; otherwise a player-owned receiver calls target selection regardless of showMessages, which controls the prompt only. Target cancellation returns false before recording a target. Playback -1 passes false to this method.',['auto_and_registration','command','recorded'],[76,160])
fact(3,'World environment resolver starts None, adopts map environment, selects facing terrain only for fishing encounter type and current terrain otherwise, combines Forest with Grass/TallGrass to ForestGrass, else uses a truthy tile environment. Explicit environment override is applied by the already received preparation contract.',['environment'],[56,59])
fact(4,'Complete named default move records route Teleport, U-turn/FlipTurn/VoltSwitch, PartingShot, Whirlwind and DragonTail/CircleThrow to the read self/forced-switch classes. Self-switch handlers reach owner selection after their distinct wild/bench/hit/earlier-switch/Pursuit gates; reflected PartingShot selects the reflected actual switcher. Forced targets use random=true. Normal callback completion is required and no internalBattle gate wraps these owner helpers.',['switch_move_families']+[x for x in primary_records if x.startswith('PRIMARY-') and x not in ['PRIMARY-EJECTBUTTON','PRIMARY-REDCARD','PRIMARY-EMERGENCYEXIT','PRIMARY-WIMPOUT']],[115,118])
fact(5,'Actual after-move target consumers require affected positive damage and active item before EjectButton/RedCard dispatch, with SheerForce/earlier-switch gates. EjectButton consumes then owner-selects, retaining consumption on negative choice. RedCard samples random=true before consumption/late SuctionCups/Ingrain checks; failed late checks need not mean no RNG or no consumption. Neither uses the other sequence channel.',['after_move','ejectbutton_redcard','item_target_trigger','handler_symbol','PRIMARY-EJECTBUTTON','PRIMARY-REDCARD'],[99,115,118])
fact(6,'HP reduction marks droppedBelowHalfHP only after positive registered damage crosses from at-least integer(totalHP/2) to strictly below it; recovery to at-least that threshold clears it. Effective ability and this flag gate the copied EmergencyExit/WimpOut handler. Trainer handler additionally rejects SkyDrop/opponent-all-fainted/cannot-leave/no-bench. Non-EOR selects owner replacement and negative returns false before replacement; EOR only recalls/leaves and returns true. Entry scans item then ability per speed-ordered battler, breaks on first true and clears flags. After-move target/user consumers preserve SheerForce/damage/earlier-switch gates.',['hp_change','damage_ability_trigger','emergency','ability_trigger','ability_hp_trigger','handler_symbol','entry','after_move','PRIMARY-EMERGENCYEXIT','PRIMARY-WIMPOUT'],[115,116,117,122])
fact(7,'Complete ordinary EOR replacement first judges and checks result gates, then loops fainted battlers with legal bench. Nonplayer trainer route calls SwitchInBetween and skips wild; player trainer route calls nonrandom GetReplacement. The optional player style prompt has all listed internal/single/trainer/opposes/health/bench/Outrage gates, and entry follows actual replacements. Inquiry wrappers therefore record/consume at the later reached EOR point.',['eor_switch','recorded'],[113,114,117,119])
fact(8,'Global metadata declares lastbattle and normally initializes it nil; default saved values supply/restore the entire global object, not a projection of that field. The complete default17 registration file has no Game_Temp registration; temporary record field is not this persistent root. Promotion assignment/clear and the received FAC-SAVE02/03/05 conditional graph/restore facts support persistence requests, not a native disk roundtrip.',['metadata','savevalues','facility_wrapper'],[11,21,22,67,172])
fact(9,'Complete sleep/confusion duration helpers draw via actual battle receiver only for unspecified/nonpositive duration; HitTwoToFiveTimes draws through it before the SkillLink override. Full target finder routes relevant random ally/foe categories to nonempty eligible candidate arrays selected through Battle.pbRandom. These establish the listed conditional domain categories without approving every status/move/target algorithm.',['sleep_duration','confuse','multihit','find_targets','target_helpers'],[98,99])
fact(10,'Complete concrete contact EffectSpore and priority QuickClaw handlers call the actual battle RNG after their own guards; EOR calls active-ability GainItem and reached Harvest uses battle RNG only outside Sun/HarshSun after empty-held-item/recycle-berry guards. The complete reached definitions/callers establish ability/item/EOR RNG categories and exact no-draw alternatives, not all handler outcomes.',['effectspore','quickclaw','harvest','after_move','eor'],[100])
fact(11,'Complete capture calculation uses Battle.pbRandom for reached critical capture/shake trials, while definite/debug/unconditional branches skip these draws. Full throw helper calls that calculation only after target/Trainer-block gates, with Snag+Shadow exception explicit; success later queues caught Pokemon. In normal facility flow internalBattle false blocks item menu, so this input gate, not playback validation or empty store override, excludes capture.',['capture_calc','throw_capture','command','facility_wrapper'],[32,45,67,78,101,152])
fact(12,'Full facility helper definitions promote last temp, play global-last, reject absent input before scene, set abortable before restore, dispatch0/1/2, resolve BGM, run animation/standby; debug number0..500/cancel-1 selects binary-read Battles/Battle%03d.dat. Exact fixed Data/Scripts name search finds no ordinary call of event-facing RecordLast/PlayLast/DebugPlay except their definitions; helper-to-helper calls are retained. No supplied root Battles/*.dat files exist; actual maps/CommonEvents are not supplied.',['facility_wrapper'],[11,13,142,174,178],'Bounded fixed-source name and supplied-tree census; dynamic event/plugin/expression calls and runtime binary IO remain unknown, not absent by universal proof.')

parent_names=['forward-mapping.json','recorded-properties-flow-atomic-increment.v2.json','RC14-selected-row-complete-child-reception.v2.json','RC-terminal-Bag-three-row-reception.v2.json','RC-Mega-Palace-layout-five-row-reception.v2.json','RC-replacement-entry-world-prepare-four-row-reception.v2.json','RC-running-random-two-row-reception.v2.json','RC-W04-root-scope-complete-child-reception.v2.json','core-command-ending-reception.v2.json','core-terminal-skill-playback-reception.v2.json','root-recorded-scalar-reception.exact.json','root-recorded-debug-skip-scope-no-required.exact.v2.json','root-cd003-recording-attribution-reception.exact.json','mandatory-running-random-complete-unit-supplement.v2.json','mandatory-prepare-caller-locator-clarification.v2.json']
parent_bindings=[packet_id(n) for n in parent_names]
parent_forward=json.loads((V/'forward-mapping.json').read_text())
atoms={x['id']:x for x in parent_forward['atoms']}
refs=sorted({a for x in rows for c in x['children'] for a in c['support_fact_ids'] if a.startswith('FAC-A')})
assert all(x in atoms for x in refs), [x for x in refs if x not in atoms]
wp76='deliverables/final-specification-set/demo-dx/wp76-facility-content-generation-and-simulation.md'
wp76lines=(B/wp76).read_text().splitlines()
wp76context=dict(identity=identity(B,wp76,BC),range=[158,169],content='\n'.join(wp76lines[157:169]),own_actual_read=[145,175],qualification='Only this exact complete7.1/7.2 dependency context; no whole WP76 semantic grant. Its direct-helper and AI-bypass distinction is the strongest existing current-formal counterargument.')
allowed_refs=set(atoms)|set(nn(*range(1,13)))|{'RC29-139-COMPLETE-CHILD-RECEPTION','UNIT:normal_scene_factory','FORMAL:WP76:167-168'}
assert all(ref in allowed_refs for x in rows for c in x['children'] for ref in c['support_fact_ids'])

rcfiles=['RC14-selected-row-complete-child-reception.v2.json','RC-terminal-Bag-three-row-reception.v2.json','RC-Mega-Palace-layout-five-row-reception.v2.json','RC-replacement-entry-world-prepare-four-row-reception.v2.json','RC-running-random-two-row-reception.v2.json','RC-W04-root-scope-complete-child-reception.v2.json']
rcchildren=[];rcrows=[]
for n in rcfiles:
    p=json.loads((V/n).read_text()); cc=p.get('explicit_children',p.get('explicit_case_children',[]))
    rcchildren.extend(x['id'] for x in cc);rcrows.extend(x['case'] for x in cc)
assert len(rcchildren)==139 and len(set(rcrows))==29

packet=dict(schema='gr8-f05-all92-complete-current-meaning-dispositions/v1',utc=UTC,reader=ME,fixed_B8=BC,fixed_R=RC,formal_identity=identity(B,FORMAL,BC),scope='ONLY F05 current canonical tail, original92 structures. Parent owns full FAC denominator and adoption. No writes to v2/source/formal/main/old/other tasks.',actual_read='All applicable contract/readset text, all current181 WP58 lines and whole29 RC rows; all281 F05/RC selected parent source facts in lossless factored shared fields with an explicitly repaired truncation, all139 RC child meanings/common premises, CORE5 terminal/6 command-ending facts, FAC-SAVE01–13 fields, bounded rootFAC001/W04/CD003. Direct complete source/primary units enumerated below. No old FULL grant or identity check is treated as semantic reading.',common_premise=common,rows=rows,existing_fact_references=refs,parent_fact_binding=parent_bindings,new_source_assertions=newfacts,complete_own_source_unit_locators=units,finite_RC_reception=dict(id='RC29-139-COMPLETE-CHILD-RECEPTION',formal_path='deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md',formal_range=[156,190],cases=sorted(set(rcrows)),child_ids=rcchildren,packets=[packet_id(n) for n in rcfiles],scope='Actual full finite meaning reception only; no historical/global/whole FAC PASS.'),pending_facets=[dict(row='F05-L0105',child='FAC-F05-CN-L0105-C06',candidate='FAC-F05-L105-DEBUG-RANDOM-ATTRIBUTION-CANDIDATE',status='PENDING_DIFFERENT_CONTEXT_COUNTER_AND_ROOT_SCOPE_CLASSIFICATION',packet='L105-debug-random-attribution-candidate.v1.json')],counts=dict(original_structures=92,manual_meaning_components=sum(len(x['children']) for x in rows),fully_disposed_structures=91,structures_with_one_pending_facet=1,new_source_facts=len(newfacts),RC_rows=29,RC_children=139),classification=dict(new_required=0,new_optional=0,new_votes=0,candidate_count=1,root_classification='UNASSIGNED'),requested=dict(model='gpt-6.1-sol',effort='ultra',tier='default normal',Fast='off'),actual={k:'UNVERIFIED' for k in ['model','effort','tier','speed','Fast','opaque_id']},actual_new_contexts=1,business='NOT_EXECUTED',whole_FAC_complete=False,whole_global_complete=False,UPDATE_NOT_STARTED=True)
dump('F05-all92-canonical-meaning-dispositions.v1.json',packet)
dump('identities.json',dict(schema='gr8-f05-child-identities/v1',utc=UTC,B8=BC,R=RC,formal=packet['formal_identity'],source_identities={x['source']:parent_forward['source_identities'].get(x['source']) for x in [atoms[a] for a in refs]},parent_packets=parent_bindings,own_units=units,requested=packet['requested'],actual=packet['actual'],reader=ME,actual_new_contexts=1,new_votes=0,UPDATE_NOT_STARTED=True))
dump('reading-ledger.json',dict(schema='gr8-f05-child-reading-ledger/v1',utc=UTC,reader=ME,contract=dict(AGENTS='/workspace/pokemon-essentials-clean-room/AGENTS.md',global_prompt='inputs/eighth-global-review-prompt.md:1-241',local_skill='inputs/review-SKILL.md:1-51',skill_application='Audit output is explicitly outside this revision skill; read only, not applied.',delegation='delegation/prompts/facility_atomic_completion_cloud.md:complete',readset='delegation/readsets/facility_atomic_completion_cloud.complete.json:1-1130',truncation='Initial combined output was truncated; all global/readset segments subsequently continuously received. No whole credit from truncated output.'),formal=dict(path=FORMAL,range=[1,181],structures=92,RC_range=[156,190],RC_rows=29),parent_reception=dict(selected_F05_RC_source_atoms=281,additional_reference_atoms=refs,method='Repeated fields were displayed once as indexed dictionaries and every unique atom field was displayed; atoms2179–2186 from a middle truncation explicitly reread in full. Additional1256/1264/1297/2128–2133/support atoms are separately verified in supplementary reception before publication.',RC_children=139,CORE_terminal_facts=5,CORE_command_ending_facts=6,save_provider_facts=13,root_dispositions=['FAC001','W04','CD003'],no_inherited_FULL=True),own_complete_units=units,limitations=['Actual native serializer/RNG/Array.sample/UI/game/save/replay not executed.','All supplier/receiver validity, callback normal-return and failure-prefix premises remain explicit.','Only L105 debug merely-presentation attribution facet awaits distinct counter/root; other domains remain parent scope.'],failed_locator_attempts=['Two rg paths for AbilityEffects/ItemEffects initially absent; corrected to 007_Other battle code.','An obsolete SaveValues candidate path absent; corrected to 002_Save data/004_Game_SaveValues.rb.','A combined source print requested past EOF218 in UseMoveTriggerEffects and exited before later reads; completed method tail204–218 actually read, remaining requested material separately read. No extra semantic credit from failed suffix.'],UPDATE_NOT_STARTED=True))

candidate_units=[]
for key in ['debug_scene','normal_scene_factory','ruled_battle','command','recorded','facility_wrapper']:
    u=next(x for x in units if x['id']==key); lo,hi=u['range'];p=R/u['identity']['path']
    candidate_units.append(dict(**u,content='\n'.join(p.read_text().splitlines()[lo-1:hi])))
candidate=dict(schema='gr8-f05-eight-section-bounded-attribution-candidate/v1',id='FAC-F05-L105-DEBUG-RANDOM-ATTRIBUTION-CANDIDATE',utc=UTC,proposer=ME,classification='UNASSIGNED_PENDING_ROOT',required_added=0,optional_added=0,sections={
 '1_identity_and_scope':dict(WP='WP58',formal_clause='F05-L0105',root_key='recording-rng-debug-scene-presentation-attribution',canonical='PROVISIONAL_BOUNDED_CANDIDATE_ONLY',severity='UNASSIGNED; only possible attribution/scope issue, no missing ordinary recording behavior established',historical_relation='Distinct from bare-trainer FAC001, debug-skip message ordering W04, and recording/store attribution CD003; those accepted limited decisions remain unchanged.'),
 '2_bidirectional_evidence':dict(B8=BC,R=RC,formal=identity(B,FORMAL,BC),formal_range=[91,105],exact_sentence=lines[104],complete_source_units=candidate_units,source_facts=[atoms[x] for x in aa(1782,1783,1784,1785,1786,1810,1811,1812,1813)],new_source_atoms=0,current_formal_strongest_counter=wp76context,negative_search=dict(command='rg -n DebugSceneNoVisuals Data/Scripts',scope='All fixed reference Data/Scripts text',result='One definition in DebugScene file and one construction at BattleSim404; no other literal construction found.',qualification='Name search is locator/negative evidence only; complete definitions and actual caller above were read. No all dynamic expressions/plugins/events exclusion.'),forward='Debug scene random return values can feed command/target/party consumers if called; they do not pass through recorder Battle.pbRandom. Default current facility/replay constructs normal Scene. Generator uses debug scene but controlPlayer routes its ordinary command phase to AI.',reverse='WP58 L105 labels excluded animation and debug-scene random merely presentation. The excluded-stream portion remains correct; the debug merely-presentation qualifier is source-wide inaccurate if read to characterize all available definitions, but may be bounded out by ordinary-facility scope and WP76 already explicitly has the correct direct-helper contract.'),
 '3_premises_controls_and_prefixes':dict(finite_input_domain='Fixed definitions/no overrides. Direct valid DebugSceneNoVisuals command-menu diagnostic, or a valid Battle scene receiver passed to the complete base menu helper. No actual RNG outcome is asserted. Other selection helpers retain their exact dependencies, including battler.move in Fight and Array.sample native behavior.',ordinary_control='Normal pbOrganizedBattleEx and pbPlayBattle call create_battle_scene→Battle::Scene; default generator pbRuledBattle sets debug/controlPlayer/internalBattle before start, so the main command loop reaches AI before scene command selection.',minimal_counterexample='On a direct normally returned DebugSceneNoVisuals.pbCommandMenu call, the first rand(15)==0 branch returns Bag tag1; otherwise a reached rand(10)==0 branch returns Call tag4, else Fight tag0. A conditional command value is a decision/input result, not merely pixels. No public support requirement or default reachability follows.',expected_reference='A returned command tag can select the corresponding base command branch for a consumer that actually uses this scene; generator defaults normally bypass these particular helpers.',spec_difference='Only potential overbroad attribution of debug-scene random as presentation; recording stream exclusion and ordinary facility behavior remain supported.',normal_failure_cancel_partial='Menu RNG exception returns no tag and does not prove choice mutation. Downstream Bag gate can refuse in internalfalse facility. Fight depends on battler.move and a block; target no-candidate returns-1; party no-candidate returnsnil and has own yield/50-attempt behavior. Preserve those prefixes rather than infer all helpers succeed. No cancellation/transaction or game execution is invented.',evidence='SOURCE_STATIC / NOT_EXECUTED',impact='Potential implementation reader misunderstanding of a debug utility category, with no demonstrated missing required normal product flow.'),
 '4_minimal_revision_contract_if_adopted':dict(correct_final_behavior='Preserve actual recorder-entry boundary. If any wording change is warranted, distinguish presentation animation RNG from conditional debug-scene selection-return definitions, while retaining that normal facility/replay uses Scene and generator controlPlayer bypasses menu selection.',must_preserve=['All eighteen/five-component and actual-random-call boundaries.','Normal facility and replay scene wiring.','Default generator AI routing and the complete callable definitions audit.','No future public helper/API, new debug scene feature or new test requirement.','FAC001/W04/CD003 bounded dispositions unchanged.'],potential_write_set=[FORMAL+':105'],synchronization='Only if root finds another genuinely contradictory current clause after exact reading; none pre-authorized by this child.',read_set='Complete units in section2, fullWP58 own181lines, referenced RC-W11 and exact current parent finite source facts. No fullCORE re-audit is required by this candidate.'),
 '5_acceptance_and_regression':dict(conditions=['A real different nonauthor context reads the complete candidate, exact current WP58 and necessary complete units, and tests the strongest ordinary-scope counterargument.','Root separately decides required/optional/no-required/policy/limit; author does not self-classify.','If adopted, wording must retain exact RNG exclusion and actual default wiring and not imply debug helpers are normal product APIs.','Static source interpretation and zero native/game/model executions remain separate.'],ordinary_boundary_vectors='Normal facility/replay uses Scene; generator controlPlayer true routes AI; direct called debug command helper has random tag-return branches. These are static controls, not newly mandated tests.',history_regression='Preserve FAC001 array normalization scope, W04 message-before-clear prefix, CD003 recording-vs-playback store attribution.'),
 '6_independent_adjudication':dict(proposer=ME,counterreviewer='/root (parent reports root will act as the actual different context; no counter result yet received)',counter_status='PENDING_REAL_DIFFERENT_CONTEXT',strongest_no_required='WP58 explicitly limits ordinary facility recording, both normal entrypoints use Scene, and the sole supplied debug scene caller sets controlPlayer. Current WP76§7.2 lines167–168 already clearly preserves the direct-helper outputs, singular-move failure and actual AI-path bypass, so the current full product contract already contains correct behavior. A public source helper definition does not by itself create a future supported API. The whole required recording mechanism may therefore already be complete despite imprecise example attribution.',strongest_change_argument='The exact current sentence names debug scene as a source category, and complete definitions have meaningful random selection outputs. Readable definitions must be audited even without a normal caller. Scope and correct WP76 may justify no product revision but must preserve actual source meanings rather than turn them into presentation.',root_decision='UNASSIGNED; this candidate adds0required/0optional/0votes.'),
 '7_dependencies_and_reception':dict(direct=['Exact currentWP58 clause105','Complete DebugScene definitions','Complete normal scene factory/facility wrapper','Complete generator real-battle caller','Complete ordinary command routing','Existing parent recording RNG facts'],blocking='Only this F05-L0105 child06 attribution facet awaits counter/root classification. Other91 structures and other6 children of L105 have explicit dispositions; wholeFAC/global completion remains parent-owned.',file_conflict='No mutations outside child directory. Any future formal amendment belongs root assigned sole writer.',batch='UNASSIGNED; remediation has not started.',closure='Parent actually full-receives this new packet, then root arranges actual distinct counter and classification; no administrative wholebody approval layer or automatic whole FAC approval.'),
 '8_execution_identity_and_authorization':dict(reader=ME,requested=dict(model='gpt-6.1-sol',effort='ultra',tier='default normal',Fast='off'),actual={k:'UNVERIFIED' for k in ['model','effort','tier','speed','Fast','opaque_id']},actual_new_contexts=1,new_votes=0,business='NOT_EXECUTED',source_formal_changed=False,write_scope=str(OUT),UPDATE_NOT_STARTED=True)
},whole_FAC_complete=False,UPDATE_NOT_STARTED=True)
dump('L105-debug-random-attribution-candidate.v1.json',candidate)

dump('progress.json',dict(schema='gr8-f05-child-progress/v1',utc=UTC,task=ME,status='COMPLETED_FINITE_F05_DELIVERY_PENDING_PARENT_RECEPTION_AND_ONE_COUNTER_FACET',B8=BC,R=RC,counts=packet['counts'],pending_facets=packet['pending_facets'],source_formal_modified=False,actual_new_contexts=1,new_votes=0,business='NOT_EXECUTED',wholeFAC_complete=False,UPDATE_NOT_STARTED=True))
dump('validation.json',dict(schema='gr8-f05-child-validation/v1',utc=UTC,checks=dict(exact_original92_ids=True,all181_formal_lines_read=True,all29_RC_rows_and139_children_read=True,fixed_git_source_identity_checks=True,unique_child_source_ids=True,parent_FAC_A_not_reallocated=True,all_component_refs_resolve=True),counts=packet['counts'],pending='Only exact L105 debug merely-presentation facet; candidate has complete8sections, no independent counter/root classification yet.',business='NOT_EXECUTED',UPDATE_NOT_STARTED=True))
(OUT/'review.md').write_text('F05 current canonical tail: all 92 original structures have complete manual meaning dispositions ('+str(packet['counts']['manual_meaning_components'])+' components). 91 structures are finitely reconciled; L105 retains one exact debug-scene attribution facet for a real different context and root classification. The other L105 components are separately supported.\n\nThe complete29 RC rows and139 finite child meanings are actually received. Existing FAC001/W04/CD003 bounded dispositions remain unchanged. Twelve new uniquely named source facts bind necessary new canonical joins, with complete source-unit fixed-Git recovery locators. The debug attribution candidate reuses existing source facts and includes current WP76§7.2 as the strongest formal scope counterargument, adding zero duplicate debug source atoms. No whole FAC/global PASS, source/formal changes, new required/optional votes, Ruby/game/native/model execution, commit or push occurred. UPDATE_NOT_STARTED.\n')

manifest=[]
for p in sorted(OUT.iterdir()):
    if p.is_file() and p.name!='artifact-manifest.json':
        data=p.read_bytes();manifest.append(dict(path=str(p.relative_to(RR)),bytes=len(data),sha256=digest(data)))
dump('artifact-manifest.json',dict(schema='gr8-f05-child-artifact-manifest/v1',utc=UTC,artifacts=manifest,scope='Child output only; manifest excludes itself, no recursive hash.',UPDATE_NOT_STARTED=True))
for p in sorted(OUT.iterdir()):
    if p.is_file():print(p.name,p.stat().st_size,digest(p.read_bytes()))
