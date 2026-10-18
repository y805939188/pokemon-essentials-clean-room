import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_10f.json').read_text());d=base['source_dictionary'];rows=[]
d['trainer_loader']={'path':'Data/Scripts/015_Trainers and player/002_Trainer_LoadAndNew.rb','range':[4,10],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete pbLoadTrainer actually read; Trainer.to_trainer/content constructors remain their separately bounded inputs'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
def layout(n,why):rows.append(dict(number=n,layout_reason=why))
layout(768,'Catalog scope and NOT_EXECUTED declaration. Each ID/input/premise/expected result is a static vector, not an executed test or host/media success report. Actual payload meanings are decomposed individually below.')
layout(769,'BC table column heading only; not a behavior or source-coverage atom.')
row(770,[
 'BC01 is conditional ordinary legal registered PIKACHU level5 input, one foe, can_override true, no callback mutation outside the specified nonintercepting hook, and normal earlier dependencies.',
 'WildBattle.start generates foes before invoking the optional calling-wild-battle hook.',
 'For separated legal species/level, that generation invokes Pokemon.new once and on_wild_pokemon_created once along the normally returned generation path.',
 'The single-foe override receives that same Pokemon and a mutable handled array; in this vector it may alter Pokemon but leaves handled nil.',
 'The subsequent start_core receives the existing Pokemon, so generate_foes reuses it rather than constructing another.',
 'The first creation/hook precedes the later core skip and on_start_battle record; actual same-object mutation survives into core.',
 'This is a conditional legal-object/source-order vector, not proof current compiled default registration or a real Demo encounter ran.'
],['wild','wild_generate','event_registry','event_dispatch'],'legal generation -> created hook -> optional nonintercepting override -> same Pokemon core argument -> skip/start record, with no implicit clone.')
row(771,[
 'BC02 array argument [registered species, legal level] uses GameData::Species.get and pbGenerateWildPokemon once in wrapper.',
 'An existing Pokemon argument is pushed by identity and is not reconstructed by generate_foes.',
 'Array branch does not apply the separated-argument Integer/range check before calling generator.',
 'The conditional legal array vector must not be extended to malformed array levels succeeding; downstream constructor/data can reject or fail.',
 'Core receives existing wrapper-generated object and also reuses it; no second creation in these ordinary wrapper paths.'
],['wild','wild_generate'],'argument case Array/Pokemon/separated -> branch-specific validation/generation -> same-object core reuse.')
row(772,[
 'BC03 requires first Trainer wrapper to enter the candidate probe, load A from trainer data, satisfy the one-trainer/party-size condition and save A as waiting_trainer.',
 'That first data-load branch triggers on_trainer_load for A before saving; callback changes remain on saved object.',
 'The second call with B data appends the saved NPCTrainer A object to its new args.',
 'The second core data branch loads B and triggers its load hook, while the NPCTrainer argument branch directly reuses A with its existing party/items/changes.',
 'Thus the successful saved-A merge path does not data-load or load-hook A twice; B is separately loaded.',
 'These counts require normally resolved data and no extra callback-triggered loads; they are not all-branch global load-count guarantees.'
],['trainer','trainer_loader','event_registry','event_dispatch'],'first data A -> hook -> save A -> second data B + same NPC A -> load/hook B and reuse A.')
row(773,[
 'BC04 first probe may data-load a trainer and trigger its hook before the waiting-save condition is found false.',
 'With no saved waiting object and this core not skipped, Trainer.start_core receives the original data arguments.',
 'Core generate_foes may then load the same author data again and trigger another load hook.',
 'The saved-A successful merge single-load conclusion does not apply when probing did not save the generated object.',
 'A dependency/callback failure can stop before the second load; earlier created objects/changes are not automatically rolled back.'
],['trainer','trainer_loader','event_registry','event_dispatch'],'probe data conversion without save -> original args core -> second conversion if reached; explicit branch distinction.')
row(774,[
 'BC05 wrapper with species/level generates before override and core; given nonintercepting override it reaches debug Ctrl core skip with that Pokemon already generated.',
 'Direct WildBattle.start_core with raw species/level checks skip before its generation, so the same Ctrl gate returns before creating a foe.',
 'Both reject normal battle construction/on_start processing through skip, but their earlier generation prefixes differ.',
 'No claim that Ctrl undoes wrapper generation or hook mutations; no extra source execution was performed.'
],['wild','outer','wild_generate'],'wrapper pre-generation vs direct core pre-generation skip; same guard, different earlier prefix.')
row(775,[
 'BC06 single generated foe plus can_override permits the calling-wild-battle hook.',
 'When handled[0] is any nonnil value, wrapper returns that exact value before core.',
 'Even false is nonnil and intercepts; ordinary wrapper outcome-to-boolean mapping is bypassed in this branch.',
 'Earlier Pokemon generation and hook mutations remain; no battle core or ordinary wild-end callback from the bypassed tail.'
],['wild','wild_generate','event_registry','event_dispatch'],'single + can_override -> mutable handled -> nonnil early exact return, no core.')
row(776,[
 'BC07 normally returned Wild core outcome2 makes wrapper false.',
 'Outcome5 also makes false.', 'Outcome1 makes true.', 'Outcome3 makes true.', 'Outcome4 makes true.',
 'These return mappings apply after any normally reached wild-end callback, not to the earlier override exact-return branch.'
],['wild'],'normal core raw outcome -> optional end hook -> outcome!=2 && outcome!=5.')
row(777,[
 'BC08 raw3 yields Wild wrapper true but Trainer wrapper false.',
 'Raw5 yields both wrappers false.',
 'Trainer wrapper uses outcome==1, distinct from the Wild exclusion of only2/5; wrapper boolean is not the raw result variable.'
],['wild','trainer'],'raw result3/5 -> distinct wrapper boolean conversions, result-variable logic independent.')
row(778,[
 'BC09 means player able count0 at the public core skip guard, not an all-fainted wild-foe participant fixture.',
 'Wild skip result is1; Trainer skip with player zero-able is0.',
 'Skip helper messages are conditional by trainer/wild/debug and pokemon_count/able_count, rather than one unconditional shared message.',
 'Normally completed helper clears battle rules/music overrides and resets encounter step count before writing the result.',
 'This current vector and WP39:113 are correct; COM004 only repairs the separate skip-parenthesis line, not this BC09.'
],['outer','wild','trainer','playerfull','root_set'],'player-zero-able guard -> army-specific skip helper -> cleanup/reset -> raw result write; preserve root-correct BC09.')
row(779,[
 'BC10 with DEBUG+Ctrl and earlier zero-able check otherwise satisfied takes the public core skip branch.',
 'No Battle.new occurs in the skipped core.',
 'No on_start_battle record event occurs in that core.',
 'Earlier wrapper generation/probe loads can still exist as their own prefixes; skipping core does not imply global no earlier work.'
],['outer','wild','trainer'],'public core early guard -> skip helper, before start record/generation/Battle.new.')
row(780,[
 'BC11 assumes an existing registered partner, no noPartner prohibition, one foe and no explicit battle-size rule.',
 'Partner participation returns false for one foe without explicit larger size, so core player setup contains only player.',
 'Partner existence alone does not force participation; later normal-end partner healing has a separate partner-existence condition.'
],['partner','partner_array_producer','prepare','normal_end'],'partner registered -> foe count1/no size -> participation false, separate terminal registered-partner effects.')
row(781,[
 'BC12 requires valid existing partner and noPartner=false; two foes then permit partner participation before the explicit-size branch.',
 'Player setup adds the partner trainer/party segment and item source and writes default double only when size rule was nil.',
 'Changing only partner existence to absent returns false before foe-count approval.',
 'Changing only noPartner true likewise returns false before foe-count approval.',
 'Two foes do not construct/register a missing partner or negate noPartner.'
],['partner','partner_array_producer','prepare','rules'],'existing partner/noPartner gate -> foe count>1 -> merged own-party setup + default double; guards precede count.')
row(782,[
 'BC13 ordinary Trainer battle has one trainer per side, declared2v2, player one able, opposing at least two.',
 'Player requirement2 exceeds count1, so validation requests lowering before full setup.',
 'Trainer reduction takes max side size2 minus1 and reduces both eligible sides to1.',
 'The resulting1v1 passes the stated able-count condition; this differs from wild fixed opposing count.'
],['ensure','startendfull','owners','teams'],'trainer requirement2/count1 -> lower max to1 -> both side sizes1, no wild fixed-side exemption.')
row(783,[
 'BC14 has two able wild Pokemon, player one able, no partner, original2v2.',
 'Wild side able count2 is fixed by the wild-size branch and is skipped during later ordinary side-size reduction.',
 'Player shortage lowers only player side from2 to1; stated complete valid fixture yields1v2.',
 'Do not replace opposing wild count with trainer-style simultaneous reduction.'
],['ensure','startendfull','teams'],'wild count2 fixed -> own shortage -> own2->1 only ->1v2.')
row(784,[
 'BC15 requires Trainer battle, more than one trainer on both sides, and at least one side size>2.',
 'EnsureParticipants raises at its first multi-trainer-size guard before able-count construction.',
 'The word immediate is local to this validator; earlier public-core records/construction/presentation may already have happened.',
 'Single-trainer side or both sizes<=2 does not trigger this particular guard.'
],['ensure','startendfull'],'validator entry both multi-owner + too-large side -> first guard failure, preserve earlier outer prefix.')
row(785,[
 'BC16 explicitly concerns the validator moment when wild able count2 differs from declared opposing1.',
 'If both old side sizes equal1, wild-count repair assigns both2 at that step.',
 'If old side sizes unequal, that step assigns only opposing wild size2.',
 'Later own-side able-count reductions still run and may further reduce own side; the intermediate repair is not unconditional final2v2 success.',
 'This count2 legal-control vector does not normalize nil wild count0 or fix the separate COM002/003 scopes.'
],['ensure','startendfull','teams'],'wild count differs -> equality-dependent intermediate assignment -> later independent participant loop; existing root scopes preserved.')
row(786,[
 'BC17 with two trainers on a side of three slots uses owner mapping [0,0,1] indexed by global battler index/2.',
 'Own global0 mapsowner0.', 'Own global2 mapsowner0.', 'Own global4 mapsowner1.',
 'With side size2, mapping is global index/2, giving owners0/1 for own0/2.',
 'This mapping depends on actual side-size/trainer-count context; it is not always one owner per interleaved slot.'
],['owners','battlefull','startendfull'],'actual side/trainer counts -> explicit3-slot owner map vsordinary2-slot arithmetic.')
row(787,[
 'BC18 specifies a3v2 configuration and global battler index1.',
 'Its opposing index ordering is [2,4,0] in the fixed battle geometry table.',
 'This is ordered slot geometry, not sorted current living battlers; caller filters must be evaluated separately.'
],['query','battlefull'],'3v2 + index1 -> geometry lookup [2,4,0], actual caller decides occupancy/liveness.')
row(788,[
 'BC19 valid existing nonempty NPC party but all members fainted passes Battle constructor nonempty-party guard.',
 'Normal Trainer core with player one able/debugfalse/no partner/default1v1 establishes start records and clears creation rules before EnsureParticipants.',
 'Opposing pbAbleTeamCounts builds no positive count entries, producing length0 rather than [0].',
 'Required owner range has length1; required-length>counts-length fails first with invalid-owner error, before the later no-able message.',
 'Changing one same-object NPC member to able constructs count[1] and avoids this particular failure.',
 'Earlier records/rules/objects are not rolled back. This is a currently correct old-NPC fixture, not a new COM002/003 finding.'
],['trainer','constructor','record_start','ensure','teams','startendfull'],'existing nonempty NPC -> zero positive count range -> requiredlength1/countlength0 -> earlier invalid-owner guard, preserve root-correct NPC history.')
row(789,[
 'BC20 valid2v2 fixture has one player owner with two able members and opposing two owners, first segment all fainted and later segment able.',
 'Opposing count array contains missing first entry and positive later count; its length is2.',
 'Owner requirements are [1,1], so required-length guard passes.',
 'At first comparison the missing count is not normalized to0; numeric <= missing fails before a promised no-able message.',
 'Changing first segment to one able supplies [positive,positive] and passes this count comparison under the stated requirements.',
 'The fixture is static object-domain evidence, not an executed failing game or a new old-NPC correction.'
],['trainer','constructor','teams','owners','ensure'],'sparse two-owner counts [missing,positive] +[1,1] -> length okay -> first numeric comparison fails; legal first-able control.')
row(790,[
 'BC21 assumes clause overrides loaded, an otherwise sleep-eligible target and current source/recipient status conditions allowing sleep.',
 'Setting only literal rules[sleep]=true does not enable the consumer keyed sleepclause.',
 'Setting sleepclause=true with an existing qualifying clause-asleep own-side member rejects at that clause gate.',
 'All14 exact rule spellings and three consumer-only clauses retain WP39 scope; absence of a facility setter wrapper does not erase a readable consumer.',
 'skillswapclause=true still blocks its actual SkillSwap target consumer; the local command table does not disable that clause.',
 'These named interface controls do not approve every future clause/mode combination or assert actual sleep was executed.'
],['clauses','wrappers','statuses_full','use'],'exact rule string -> loaded clause override -> ordinary status qualification -> clause rejection; preserve distinct consumer-only keys.')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_11a.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows),'layout',sum('layout_reason'in x for x in rows))
