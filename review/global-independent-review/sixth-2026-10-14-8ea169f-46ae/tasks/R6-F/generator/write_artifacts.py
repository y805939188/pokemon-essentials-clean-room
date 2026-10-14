"""Assemble explicitly reviewed audit records. Does not evaluate reference behavior."""
import datetime, json, pathlib

ROOT = pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
BASE = ROOT / 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-F'
OUT = BASE / 'generator'
SOURCE = 'reference/pokemon-essentials/Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/'
F = {1: SOURCE + '001_ChallengeGenerator_Data.rb',
     2: SOURCE + '002_ChallengeGenerator_Pokemon.rb',
     3: SOURCE + '003_ChallengeGenerator_Trainers.rb',
     4: SOURCE + '004_ChallengeGenerator_BattleSim.rb'}
SPEC = 'deliverables/final-specification-set/demo-dx/wp76-facility-content-generation-and-simulation.md'
WP54 = 'deliverables/final-specification-set/combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md'
DATA = 'reference/pokemon-essentials/Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb'
FOES = 'reference/pokemon-essentials/Data/Scripts/018_Alternate battle modes/001_Battle Frontier/003_Challenge_ChooseFoes.rb'
COMPILE = 'reference/pokemon-essentials/Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb'
WRITE = 'reference/pokemon-essentials/Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb'

rows = []
def unit(file, name, start, end, fact, consumers, spec_lines, disposition='SUPPORTED_STATIC'):
    rows.append({'unit_id': f'GEN-U{len(rows)+1:03}', 'source_path': F[file], 'source_unit': name,
                 'source_lines': [start, end], 'review': 'FULL_BODY_AND_FIELDS_SEMANTICALLY_READ',
                 'behavior_fact': fact, 'necessary_consumers': consumers,
                 'formal_path': SPEC, 'formal_lines': spec_lines, 'disposition': disposition,
                 'evidence': 'STATIC_SOURCE_REVIEW_NOT_REFERENCE_EXECUTION'})

unit(1,'BaseStatRestriction.initialize',5,8,'Stores the inclusive lower and upper species base-stat-total bounds, without exchanging them.',['withRestr'],[153,156])
unit(1,'BaseStatRestriction.isValid?',10,13,'Eligibility is a species-total inclusive range test.',['pbArrangeByTier'],[153,156])
unit(1,'NonlegendaryRestriction.isValid?',20,24,'Gendered individuals pass; genderless individuals in the Undiscovered egg group fail; remaining genderless individuals pass.',['withRestr','pbArrangeByTier'],[153,154])
unit(1,'InverseRestriction.initialize',31,33,'Retains the input eligibility condition for later inversion.',['withRestr'],[154,154])
unit(1,'InverseRestriction.isValid?',35,37,'Inverts the supplied eligibility result.',['withRestr','pbArrangeByTier'],[154,154])
unit(1,'withRestr',56,65,'Builds each tier using only its base-stat range and optional normal/inverse nonlegendary condition; the incoming challenge rule is unused here.',['pbArrangeByTier'],[153,155])
unit(1,'pbArrangeByTier',67,108,'Nine tiers have the documented bounds. First filters by original single-member eligibility; rejects candidates in no tier. Selects an allowed tier from relative input position, then sorts inside each tier by total and species identity.',['pbGenerateChallenge','pbTrainerInfo'],[151,156])
unit(1,'pbReplenishBattlePokemon',113,124,'Repeatedly obtains rule-eligible candidates and rejects duplicates until the pool reaches 20. It does not truncate larger pools or impose a retry bound.',['pbGenerateChallenge','RuledTeam.initialize'],[126,129])
unit(1,'isBattlePokemonDuplicate',126,141,'Different species cannot duplicate. Otherwise equal ordered four-slot move identities including nil, or equal item/nature/all-main-stat EVs, suffice. The temporary compaction/sort result is discarded.',['pbReplenishBattlePokemon','pbRemoveDuplicates'],[119,124])
unit(1,'pbRemoveDuplicates',143,166,'Keeps input order, omits duplicates, and replaces the earliest same-species entry when admitting an eleventh distinct entry of that species.',['pbGenerateChallenge'],[126,129])
unit(1,'pbGenerateChallenge',171,271,'Two-member rule copy governs construction and simulation; original rule returns for final tiers/allocation. Loads two independently rescued checkpoints, optionally seeds from existing content, runs eleven replacement/simulation cycles, keeps score strictly above 65, then publishes through trainer allocation. Checkpoints persist in multiple stages without a transaction.',['pbWriteCup','pbTrainerInfo','pbGetBTPokemon','RuledTeam','pbRuledBattle'],[136,156])
unit(1,'pbWriteCup',276,338,'Debug-only UI. No-list and existing-list prompts have different options/cancel mappings. Reuse migrates all nondefault challenge IDs and then writes data/PBS. New-generation confirmation precedes window creation; progress only refreshes at callback points; no mid-generation cancel or exception cleanup guarantee.',['BattleChallenge.set','Compiler.write_trainer_lists'],[43,63])

unit(2,'pbBaseStatTotal',9,14,'Adds all base-stat values of the species data.',['baseStatTotal'],[78,78])
unit(2,'baseStatTotal',16,19,'Memoizes the species total by species identity.',['BaseStatRestriction','pbArrangeByTier','pbRandomPokemonFromRule','pbDecideWinnerScore'],[78,78])
unit(2,'babySpecies',21,24,'Memoizes the baby species from the species data.',['pbGetLegalMoves2','pbRandomPokemonFromRule'],[78,78])
unit(2,'minimumLevel',26,29,'Memoizes the species minimum level.',['pbRandomPokemonFromRule'],[77,78])
unit(2,'evolutions',31,34,'Memoizes forward evolution records requested with the true filter parameter.',['pbRandomPokemonFromRule'],[77,78])
unit(2,'pbRandomMove',40,48,'Uniformly samples move keys excluding the Struggle and target-last-move-copy function identities; no retry cap.',['pbRandomPokemonFromRule Sketch branch'],[103,103])
unit(2,'pbGetLegalMoves2',50,103,'Processes level moves, machine-compatible tutor moves, and baby egg moves in order. Weights are first-actual-insertion sensitive. Pruning compares a prebuilt move-data snapshot while deleting from the actively traversed weighted list; self-deletion and order dependence are retained.',['pbRandomPokemonFromRule'],[94,99])
unit(2,'addMove',105,124,'Has two explicit exclusions and ordered weight overrides, with zero-copy insertions allowing a later source to supply the move. Duplicate identities already in the weighted list block additional source weighting.',['pbGetLegalMoves2'],[96,98])
unit(2,'hasMorePowerfulMove',128,139,'For a damaging candidate only, reports any higher-power same-type move in the whole supplied weighted list. It does not require equal function or accuracy.',['pbRandomPokemonFromRule'],[105,105])
unit(2,'pbRandomPokemonFromRule',144,359,'Alternating species rejection bias; random EV emphasis and nature; 41-item list plus special gates; shared level-sensitive legal-move cache and Sketch mutation; short-move-list bypass; four-move combination gates; post-accept emphasis changes and item fixes; materialization at suggested level/IV31; final member eligibility is the only outer success exit.',['pbReplenishBattlePokemon','PBPokemon.createPokemon'],[65,115])

unit(3,'getTypes',4,7,'Returns a copy of the species data type list.',['pbTrainerInfo'],[220,222])
unit(3,'pbTrainerInfo',14,211,'Queries trainer and template tables separately. Empty trainers enter per-trainer shortcuts or a nonterminating ordinary draw. Normal nonempty input candidates are relabeled to original-rule suggested level without explicit stat recomputation. Builds preference weights, independent type trials, asymmetric index/member deduplication and sequential/random supplementation, then serializes all matches or a new list. Captures whether any default existed before scanning, saves data before writing PBS, and retains all earlier side effects on later exceptions.',['pbGenerateChallenge','pbGetBTTrainers','pbGetBTPokemon','PBPokemon.fromPokemon','Compiler.write_trainer_lists','pbGenerateBattleTrainer'],[207,232])

unit(4,'RuledTeam.initialize',7,22,'Consumes a random pool member immediately for each required slot and retries complete construction until final team eligibility. Pool exhaustion is unguarded. Initializes active rating/history and zero cumulative games.',['pbGenerateChallenge'],[131,145])
unit(4,'RuledTeam.[]',24,26,'Returns the team member at the requested position.',['pbGenerateChallenge retirement/final collection','pbRuledBattle'],[145,149])
unit(4,'RuledTeam.length',28,30,'Reports team member count for replacement, retirement and collection.',['pbGenerateChallenge','pbRuledBattle'],[145,149])
unit(4,'RuledTeam.rating',32,34,'Exposes the active rating win-chance display value, not its raw rating.',['pbGenerateChallenge','pbRuledBattle'],[38,39])
unit(4,'RuledTeam.ratingData',36,38,'Exposes the active rating record consumed when creating opponent snapshots.',['MatchHistory.addMatch','RuledTeam.addMatch'],[182,182])
unit(4,'RuledTeam.ratingRaw',40,42,'Diagnostic tuple contains raw rating, deviation, volatility and display win chance; no in-scope normal caller found.',['NONE_FOUND_IN_NORMAL_GENERATOR'],[179,189],'NONCONSUMED_DIAGNOSTIC_NO_NEW_CONTRACT_REQUIRED')
unit(4,'RuledTeam.compare',44,46,'Diagnostic delegates comparison to an active rating operation that is not defined in the reviewed active rating record; no normal generator caller found.',['NONE_FOUND_IN_NORMAL_GENERATOR'],[],'NONCONSUMED_HELPER_NO_NORMAL_FAILURE_CLAIM')
unit(4,'RuledTeam.totalGames',48,50,'Visible game count includes settled cumulative count (missing field treated as zero) plus pending history length.',['pbGenerateChallenge replacement/retirement thresholds'],[38,38])
unit(4,'RuledTeam.addMatch',52,54,'Adds a result using an opponent-rating snapshot.',['pbRuledBattle'],[182,185])
unit(4,'RuledTeam.games',56,58,'Pending game count is current history length.',['pbGenerateChallenge average gate','RuledTeam.totalGames','RuledTeam.updateRating'],[38,38])
unit(4,'RuledTeam.updateRating',60,66,'Successful history settlement increases cumulative count by the number of removed history records. Counts are conserved; failures before clear do not settle the games and need not roll back rating fields.',['pbGenerateChallenge'],[190,205])
unit(4,'RuledTeam.toStr',68,70,'Nonconsumed formatting helper uses conversions/fields that are not guaranteed by the active record; no normal generator caller found.',['NONE_FOUND_IN_NORMAL_GENERATOR'],[],'NONCONSUMED_HELPER_NO_NORMAL_FAILURE_CLAIM')
unit(4,'RuledTeam.load',72,78,'Nonconsumed helper interprets stored members as indices into another pool, unlike normal teams of creature objects; no normal caller found.',['NONE_FOUND_IN_NORMAL_GENERATOR'],[],'NONCONSUMED_HELPER_NO_NORMAL_FAILURE_CLAIM')
unit(4,'SingleMatch.initialize',90,95,'Stores opponent raw rating/deviation, score and K value; draw identity is negative one.',['MatchHistory.addMatch','PlayerRating.update','unused Elo.update'],[182,185])
unit(4,'MatchHistory.initialize',104,107,'Stores empty pending matches and the associated active rating record.',['RuledTeam.initialize'],[134,134])
unit(4,'MatchHistory.[]',109,111,'Returns a pending match record by position.',['PlayerRating.update'],[182,187])
unit(4,'MatchHistory.length',113,115,'Reports pending match count.',['RuledTeam.games','PlayerRating.update'],[38,38])
unit(4,'MatchHistory.each',117,119,'Enumerates pending matches in input order; available diagnostic enumeration has no separate normal caller.',['NO_SEPARATE_GENERATOR_CALLER'],[182,185])
unit(4,'MatchHistory.addMatch',121,124,'Captures raw opponent rating/deviation at result insertion time. Later sequential settlement cannot retroactively change this snapshot.',['RuledTeam.addMatch'],[182,182])
unit(4,'MatchHistory.updateAndClear',126,129,'Updates rating before clearing history. A propagated rating-update failure bypasses clear.',['RuledTeam.updateRating'],[190,191])
unit(4,'PlayerRatingElo.initialize',140,145,'Unused alternative starts raw rating 1600 with zero deviation/volatility and absent display cache.',['NO_NORMAL_GENERATOR_CONSUMER'],[192,192])
unit(4,'PlayerRatingElo.winChancePercent',147,152,'Unused alternative caches the stated logistic value; despite the helper name this is not promoted to a usable active generator percentage algorithm.',['NO_NORMAL_GENERATOR_CONSUMER'],[192,192])
unit(4,'PlayerRatingElo.update',154,163,'Empty input returns; nonempty input fails at acquiring undeclared current-match data. Active generation constructs the other rating record.',['NO_NORMAL_GENERATOR_CONSUMER'],[192,192])
unit(4,'PlayerRating.initialize',174,179,'Active rating starts at raw 1500, deviation350, volatility0.9 and absent display cache.',['RuledTeam.initialize'],[179,179])
unit(4,'PlayerRating.winChancePercent',181,198,'Caches the display value; branches on deviation strictly above100 between the two independently described formulas.',['RuledTeam.rating','pbGenerateChallenge','pbRuledBattle'],[189,189])
unit(4,'PlayerRating.update',200,238,'Empty history inflates only deviation. Nonempty history computes snapshot factors/variance, excludes draws from improvement sum, updates volatility then deviation then rating, and writes rating/deviation/volatility in that sequence.',['MatchHistory.updateAndClear'],[181,191])
unit(4,'PlayerRating.rating2',248,250,'Converts raw rating to centered normalized scale.',['PlayerRating.update'],[181,181])
unit(4,'PlayerRating.deviation2',252,254,'Converts deviation using the same scale factor.',['PlayerRating.update'],[181,181])
unit(4,'PlayerRating.getGFactor',256,260,'Computes the opponent deviation factor from the raw snapshot deviation.',['PlayerRating.update'],[183,183])
unit(4,'PlayerRating.getEFactor',262,267,'Computes expected result from current normalized rating, opponent raw rating and factor.',['PlayerRating.update'],[183,183])
unit(4,'PlayerRating.setVolatility2',269,271,'Assigns updated volatility in its unchanged scale.',['PlayerRating.update'],[181,187])
unit(4,'PlayerRating.setRating2',273,276,'Writes denormalized raw rating and invalidates display cache.',['PlayerRating.update'],[187,189])
unit(4,'PlayerRating.setDeviation2',278,281,'Writes denormalized deviation and invalidates display cache.',['PlayerRating.update'],[187,189])
unit(4,'PlayerRating.getUpdatedVolatility',283,304,'Documented variation starts each update at current log volatility squared, uses system1.2 by default, limits to100 steps, stops on step-size tolerance and returns exponentiated half-final approximation.',['PlayerRating.update'],[186,186])
unit(4,'pbDecideWinnerEffectiveness',310,332,'Status moves score zero. Ground against Levitate stays neutral. Wonder Guard changes non-super-effective component factors to neutral before combining. The six-case discrete score matrix is used; unlisted products return zero.',['pbDecideWinnerScore'],[174,174])
unit(4,'pbDecideWinnerScore',334,359,'For each own move and opposing member adds approximate type score, plus each own species total divided by10 with integer semantics and item bonus10. Adds scaled rating and a separate random0..31 draw for each side.',['pbDecideWinner'],[173,175])
unit(4,'pbDecideWinner',361,372,'Scales and rounds both ratings before scoring; total-score ties compare these rounded values and then return draw5.',['pbRuledBattle'],[173,175])
unit(4,'pbRuledBattle',377,438,'Random1% executes a no-visual AI-controlled noninternal real battle after suggested-level normalization and positional item snapshots; normal return heals and restores items but not normalized levels. Other99% estimates. Result1/2 versus other records win/loss or paired negative-one draws. Exceptions bypass subsequent recovery/result insertion.',['pbGenerateChallenge','rule.createBattle','Battle.pbCommandPhaseLoop','Pokemon.heal'],[160,175])

assert len(rows) == 62
fields = [
 {'source': F[1], 'lines': [4,338], 'fields': ['inclusive tier bounds','wrapped eligibility condition','original challenge rule','two-member rule copy','candidate pool','rated team library','tag/challenge identity','600 target','65 strict final threshold','40 low score threshold','11 iterations','current scan position','five opponent draws','average pending history count','debug flag','display filename','default flag','challenge ID list','message window','refresh time'], 'formal': [[35,41],[43,63],[117,156],[244,265]]},
 {'source': F[2], 'lines': [1,359], 'fields': ['species keyed total/baby/minimum/evolution caches','level keyed move cache generation','cached machine move IDs','suggested level','base form gate','outer parity','species random gate0..19','EV emphasis entries including duplicates','nature increase/decrease relations','41 item identities','short-level berry substitution','Sketch shared-cache flag','move IDs/function/type/power/accuracy/PP','physical/special/normal flags','shared ten-way total-power draw','final rule eligibility'], 'formal': [[65,115],[236,242]]},
 {'source': F[3], 'lines': [4,211], 'fields': ['trainer type/name/intro/win/lose/candidate numbers','template species/type preferences','200 target','one-in-thirty shortcut','original suggested level','member-rule-cleared copy','candidate validity/type caches','rank distance','eight-entry weight table','type counts cap10','candidate numbers','candidate object collection','party capacity','prior default existence','matching list positions','trainer/Pokemon filename','default boolean','serialized species/item/nature/moves/EV emphasis'], 'formal': [[36,36],[207,232]]},
 {'source': F[4], 'lines': [4,438], 'fields': ['team reference/accessor','settled games','rating','history','opponent rating/deviation snapshots','score -1/0/1','stored K16','raw rating1500','deviation350','volatility0.9','display cache','normalized rating/deviation','default system1.2','100-step limit','1e-6 tolerance','six type scores','item presence','two independent jitter draws','trainer type first key','positional item snapshots','debug=true/controlPlayer=true/internalBattle=false','battle decision'], 'formal': [[38,39],[131,134],[158,205]]}
]

presented = [json.loads(line) for line in (BASE / 'reading-ledger-generator.jsonl').read_text().splitlines()]
def coverage(path, required):
    entries = [e for e in presented if e['path'] == path]
    seen = set()
    for e in entries:
        seen.update(range(e['start_line'], e['end_line']+1))
    wanted = set(range(1, required+1))
    return {'path': path, 'required_lines': required, 'presented_unique_lines': len(seen & wanted),
            'readable_unread_lines': sorted(wanted-seen), 'readable_unread': len(wanted-seen),
            'semantic_attestation': 'MANUALLY_READ_ALL_REQUIRED_LINES; presentation ledger alone does not establish this',
            'bindings': [{k:e[k] for k in ['commit','git_blob','sha256']} for e in entries[:1]]}
required = [coverage(F[i], n) for i,n in [(1,338),(2,359),(3,211),(4,438)]]
required += [coverage(SPEC,279), coverage(WP54,156),
             coverage('deliverables/final-specification-set/combat-requirements/wp54-entry-rules-and-cup-data.md',109),
             coverage('deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md',168),
             coverage('deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md',327),
             coverage('AGENTS.md',297)]
assert all(e['readable_unread'] == 0 for e in required)

reverse = []
def clause(label, lines, source_refs, conditions, tested):
    reverse.append({'clause': label, 'formal_path': SPEC, 'formal_lines': lines,
                    'source': [{'path': p, 'lines': [a,b]} for p,a,b in source_refs],
                    'preconditions': conditions, 'test_catalog': tested,
                    'result': 'SUPPORTED_STATIC', 'not_executed': True})
clause('Purpose/scope/evidence demarcation',[1,41],[(F[1],171,338),(F[2],144,359),(F[3],14,211),(F[4],377,438)],'Author tool; wrapper debug gate. This is static text, no actual host/demo observation.','GN-M01..M24')
clause('Embedded facility setup/debug gate',[43,48],[('reference/pokemon-essentials/Data/Scripts/018_Alternate battle modes/001_Battle Frontier/001_Challenge_BattleChallenge.rb',18,25),(F[1],276,278)],'Facility set executes successfully; debug must be true to enter write-cup UI.','GN-M01')
clause('Prompt state/options/cancel/long-task refresh',[50,56],[(F[1],278,338),('reference/pokemon-essentials/Data/Scripts/007_Objects and windows/011_Messages.rb',687,755)],'Readable compatible list data or rescued empty fallback; valid message host. Default command is zero and positive cancel choice is one-based. Refresh requires callback invocation; no later exception.','GN-M01/GN-M03')
clause('Reuse challenge migration/default distinction',[58,63],[(F[1],302,319),(DATA,21,32)],'User selected a valid index rather than cancel; save/write stages succeed for full result.','GN-M02')
clause('Unbounded candidate sampling/form0/species bias',[65,78],[(F[2],144,170)],'Nonempty species catalogs; valid rule methods; feasible candidates required for termination.','GN-M04')
clause('EV/nature probability and later duplicate entries',[80,84],[(F[2],171,191),(F[2],245,250),(F[2],326,333)],'Registered natures/main stats; sequential random gates, not deterministic hard requirements.','GN-M05/B17-PA040-duplicate')
clause('Item list/special restrictions/berries/absence',[86,92],[(F[2],196,258),(DATA,154,163)],'Species and level already selected; item absence becomes nil at intermediate materialization.','GN-M06')
clause('Weighted legal sources/first insertion/pruning',[94,99],[(F[2],50,124),(F[2],193,195)],'Registered move data; comparison snapshot and live list preserve traversal order effects.','GN-M07')
clause('Sketch shared cache/short list/four-slot sampling',[101,105],[(F[2],259,283)],'Cache list first element determines Sketch; fewer than four distinct moves uses short branch.','GN-M09')
clause('Combination/physical/special/power/item consistency',[106,110],[(F[2],284,353)],'Four-distinct-move branch; shared ten-way draw; two sleep-dependent exception gates independent.','GN-M08/GN-M10')
clause('Materialization/EV fraction/reverse threshold',[112,115],[(F[2],354,357),(DATA,141,163),(DATA,196,217)],'Valid species/level; default totalEV510 used in numeric examples; EV values written without training-path caps.','B17-PA040-double/B17-PA040-duplicate')
clause('Slot-sensitive duplicate OR attribute predicate',[117,124],[(F[1],126,141)],'Same species; four-slot comparison includes nil slots; attributes must all equal for the second criterion.','GN-M11')
clause('Replenishment/same-species ten-entry cap',[126,129],[(F[1],113,124),(F[1],143,166)],'The cap acts only in explicit deduplication, not as general pool capacity.','GN-M12')
clause('Pool-consuming team construction',[131,134],[(F[4],7,22)],'Simulation copy requests two; all current team slots must pass final-rule validation. No pool exhaustion protection.','GN-M13')
clause('Rule switch/checkpoints/seeding/constants',[136,142],[(F[1],171,196),(F[4],48,65)],'Normal restored checkpoint records; original rule retained; candidate/template construction valid.','GN-M13/GN-M14/GN-M20')
clause('Priority replacement/delete/retire/skip and checkpoints',[143,147],[(F[1],195,228)],'Each later branch requires preceding branches false. Delete still advances index.','GN-M14')
clause('Five unconditional opponent draws/average history',[148,148],[(F[1],229,252)],'Nonzero team library; only final sampled opponent is used; successful rating settlement for normal exit.','GN-M20')
clause('Final collection and nine tiers',[149,156],[(F[1],4,108),(F[1],254,269)],'Score strictly above65; original eligibility; reject no-tier candidates; integer relative-position placement.','GN-M21/GN-M22')
clause('Simulation split and result identities',[160,162],[(F[4],377,438)],'One hundred-way draw; other decisions are paired negative-one draws.','GN-M15')
clause('Real no-visual AI and recovery boundary',[164,169],[(F[4],377,419),('reference/pokemon-essentials/Data/Scripts/011_Battle/004_Scene/009_Battle_DebugScene.rb',1,106),('reference/pokemon-essentials/Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb',198,217),('reference/pokemon-essentials/Data/Scripts/014_Pokemon/001_Pokemon.rb',274,307)],'Valid battle construction; normal return is necessary for subsequent heal/items. Scene auxiliaries are direct-call contracts, not AI main commands.','GN-M16')
clause('Approximate scoring/Levitate/WonderGuard/tie',[171,175],[(F[4],310,372),('reference/pokemon-essentials/Data/Scripts/010_Data/002_PBS data/003_Type.rb',61,141)],'Legal move/type data; approximation intentionally differs from formal immunity/damage. Integer division applies per creature.','GN-M17')
clause('Active rating initialization/scaling/snapshot factors',[177,183],[(F[4],90,129),(F[4],174,179),(F[4],248,267)],'Active record, finite snapshots; volatility is kept at its original scale.','GN-M18')
clause('Variance/draw exclusion/volatility/deviation/rating',[184,188],[(F[4],200,238),(F[4],283,304)],'Finite valid history and successful arithmetic; current volatility determines starting log value.','GN-M18')
clause('Display formulas/cache',[189,189],[(F[4],181,198),(F[4],273,281)],'Deviation strictly above100 selects first formula; setters invalidate display.','GN-M18')
clause('Cumulative conservation/failure/next-round vectors',[190,205],[(F[4],48,65),(F[4],126,129),(F[1],199,216)],'Effective cumulative count, valid histories; no external mutation or concurrent new game. Failure does not promise rating rollback.','GN-M14/GN-M20')
clause('Unused broken Elo alternative',[192,192],[(F[4],135,163),(F[4],19,21)],'Only direct unused alternative with nonempty history reaches its missing-match failure.','GN-M19')
clause('List lookup/order/default fallback',[209,211],[(DATA,21,32)],'First nondefault challenge match; otherwise first default. Rescue load failure yields empty source.','GN-M02/GN-M24')
clause('Trainer generation/shortcut/nonterminating ordinary loop',[213,216],[(F[3],14,49),('reference/pokemon-essentials/Data/Scripts/019_Utilities/001_Utilities.rb',285,368)],'Empty trainers; YOUNGSTER registered. Every trainer needs shortcut to proceed; existing trainers bypass generation.','GN-M23')
clause('Level relabeling/type bias/rank weight/dual inclusion',[218,222],[(F[3],50,132),('reference/pokemon-essentials/Data/Scripts/014_Pokemon/001_Pokemon.rb',199,205)],'Nonempty candidate input; level assignment has no explicit stat recomputation. Normal species/type lookup succeeds.','GN-M24')
clause('Index/member dedup asymmetry and supplementation',[223,225],[(F[3],132,177)],'Index lengths and member list validation are separate; sequential same-species branch can duplicate index; random supplement ignores cached member validity and can stagnate.','GN-M24')
clause('Publication/default flag/preexisting filenames',[227,230],[(F[3],179,207)],'Prior-default fact captured once; all matching IDs updated; no uniqueness repair.','GN-M24')
clause('Ordered partial publication/failure/nil fields',[231,232],[(F[3],207,211),(WRITE,511,619),(COMPILE,951,1063),(DATA,113,151)],'Data save succeeds before PBS write. Missing filename is an error; absent named file becomes empty. Invalid item can be blank but invalid/nil nature fails direct write lookup.','GN-M02/GN-M24; proposed GR6-F-G001 named compatibility cases')
clause('Cache/name/checkpoint summary',[234,251],[(F[2],1,34),(F[2],50,62),(F[2],193,195),(F[2],259,264),('reference/pokemon-essentials/Data/Scripts/019_Utilities/001_Utilities.rb',285,368),(F[1],196,252)],'Legal names; maxLength12 uppercase call. Cache is process-global and level changes replace legal-move map. Checkpoint timing is not transaction recovery proof.','GN-M03/GN-M09/GN-M20/GN-M23')
clause('Failure/unknown/test/dependency summaries',[253,279],[(F[1],171,338),(F[2],144,359),(F[3],14,211),(F[4],377,438),(COMPILE,951,1063)],'Summaries inherit exact earlier preconditions. Missing demo materials do not prove normal startup empty tables; no runtime or event-chain promotion.','GN-M01..M24/B17-PA040-double/B17-PA040-duplicate')

finding = {
 'id': 'GR6-F-G001', 'state': 'TENTATIVE_PROPOSAL_REQUIRES_PARENT_NONPROPOSER_REBUTTAL',
 'type': 'NAMED_DEFAULT_DATA_COMPATIBILITY_COVERAGE_GAP', 'suggested_severity': 'LOW',
 'title': '默认设施表的两处旧身份在当前目录与 Gen5 目录下产生不同编译结果，尚无具名向量',
 'formal_location': [{'path': SPEC, 'lines': [231,232]}, {'path': SPEC, 'lines': [262,262]},
                     {'path': 'deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md', 'lines': [189,212]}],
 'source_location': [{'path': 'reference/pokemon-essentials/PBS/battle_tower_pokemon.txt', 'lines': [140,140]},
                     {'path': 'reference/pokemon-essentials/PBS/battle_tower_pokemon.txt', 'lines': [252,252]},
                     {'path': DATA, 'lines': [113,138]}, {'path': WRITE, 'lines': [593,615]},
                     {'path': 'reference/pokemon-essentials/PBS/items.txt', 'lines': [2072,2078]},
                     {'path': 'reference/pokemon-essentials/PBS/moves.txt', 'lines': [5153,5163]},
                     {'path': 'reference/pokemon-essentials/PBS/Gen 5 backup/items.txt', 'lines': [1670,1676]},
                     {'path': 'reference/pokemon-essentials/PBS/Gen 5 backup/moves.txt', 'lines': [3613,3623]}],
 'preconditions': ['Frozen default tower PBS and current root item/move identifiers; normal successful item/move compilation and list compilation, or compatible loaded registries with exactly these identities.',
                   'No plugin or supplemental root file defines STICK or VICEGRIP; no author modification of the table; all preceding parse dependencies succeed.',
                   'Gen5 comparison is explicit optional alternate registered catalogs, not automatic backup selection; no files are copied or compiled in this review.',
                   'Rewriting/instantiating results additionally requires successful respective consumer stages.'],
 'normal_control': 'The documented parser tolerates missing item identity as nil and skips missing move identities. With catalogs actually defining STICK/VICEGRIP (the Gen5 backup profile), these two fields survive the parser. Current-root LEEK/VISEGRIP are different identifiers; handlers mentioning both do not register data aliases.',
 'minimal_counterexample': [
   {'input': 'Default template index137 / PBS line140: FARFETCHD with STICK, RELAXED, three EV labels and SLASH/KNOCKOFF/SWORDSDANCE/AGILITY.',
    'current_root_expected': 'Species/nature/moves remain, item becomes nil; successful subsequent materialization has no held item; successful PBS rewrite emits an empty held-item field.',
    'gen5_registered_profile_expected': 'STICK resolves and the held-item identity is retained.'},
   {'input': 'Default template index249 / PBS line252: CRAWDAUNT with PERSIMBERRY, ADAMANT, HP/DEF/SD and BUBBLEBEAM/VICEGRIP/KNOCKOFF/PROTECT.',
    'current_root_expected': 'VICEGRIP is dropped and survivors compact to BUBBLEBEAM/KNOCKOFF/PROTECT. It is not automatically renamed VISEGRIP and no fallback move is inserted because three valid moves remain. Successful rewrite preserves three survivors and an empty fourth slot.',
    'gen5_registered_profile_expected': 'All four listed move identities survive.'}],
 'necessary_consumers': [{'path': COMPILE, 'lines': [951,1020], 'role': 'List child files parsed into data'},
                         {'path': DATA, 'lines': [21,32], 'role': 'Generator and facility consume default table fallback'},
                         {'path': DATA, 'lines': [201,217], 'role': 'Template materialization'},
                         {'path': FOES, 'lines': [39,82], 'role': 'Normal facility opponent generation'},
                         {'path': 'reference/pokemon-essentials/PBS/battle_tower_trainers.txt', 'lines': [147,153], 'role': 'CHEN list actually contains index137'},
                         {'path': 'reference/pokemon-essentials/PBS/battle_tower_trainers.txt', 'lines': [819,825], 'role': 'JAMAL list actually contains index249'},
                         {'path': WRITE, 'lines': [573,619], 'role': 'Successful later rewrite materializes field loss'}],
 'negative_search': {'artifact': 'negative-search.json', 'summary': 'Root PBS section membership and all scripts searched. No STICK or VICEGRIP data alias definition found. VICEGRIP has no script hit. STICK hits are handler compatibility or a move blacklist, not registry entries. Precompile rewriting only covers VictoryME/BaseDamage. Compiler discovery is root PBS/*.txt, not recursive backups. Entire formal set searched for both legacy spellings; no named template/vector exists.'},
 'impact': 'Generic parsing rule is already correct. Gap is concrete compatibility evidence for shipped default inputs: current-root compilation loses an item and a move which an explicitly selected Gen5 registry can retain. A clean-room test corpus may otherwise exercise only synthetic unknown identities and omit shipped cases. No claim that the entire generator/host fails.',
 'minimal_fix': 'Append two implementation-independent named static vectors near WP76 §8.4 or its GN tests. State active-root registry precondition, nil item / compacted three moves, successful later rewrite conditions, and optional Gen5 alternate-ID contrast. Keep paths/lines in audit only. Do not edit reference data or add aliases to future behavior.',
 'proposed_sanitized_text': '当前默认设施候选中的 FARFETCHD／STICK 与 CRAWDAUNT／VICEGRIP 是具名数据兼容对照。仅在采用当前根目录物品和招式目录、无额外身份定义且解析正常时：前者持物转空；后者跳过 VICEGRIP，剩余招式按原相对顺序成为 BUBBLEBEAM、KNOCKOFF、PROTECT，不自动改名为 VISEGRIP。后续创建或反写成功时分别消费该空持物与三招式结果。显式采用含 STICK／VICEGRIP 的 Gen5 身份目录时，两处身份可保留；备份不会因存在而自动进入当前目录。以上为静态推导，未执行编译、创建、对战、反写或完整 Demo。',
 'preserved_scope': 'Preserve §8.4 generic invalid-item/invalid-move rule, source/destination ordering, nil-nature exception, checkpoints/default flag behavior and all existing GN/B17 rows. No future API/class or code requirement.',
 'synchronization': ['If accepted, WP76 §8.4/data-boundary summary', 'Add companion GN rows without deleting old24 rows', 'Audit source traceability', 'Global Feature Matrix/coverage/independent-review finding status by parent'],
 'regression': ['Unknown item still maps nil; invalid move compacts; all-invalid moves still fall back to first registry move',
                'No blanket root alias from handler identity registration', 'Gen5 remains optional, no recursive automatic PBS discovery',
                'Existing GN-M06/M24 and B17 EV vectors unchanged', 'Normal compiler/file failure boundaries are not replaced by rollback promises'],
 'dependencies': ['WP04 registry loading/identifier lookup','WP55 facility template/opponent consumption','WP76 generated content publication','WP75 compiler discovery','WP77 active-vs-backup/demo evidence boundary'],
 'strongest_rebuttal': 'WP76 §8.4 already correctly states the general unknown-identifier outcomes, and §10.8 does not promise lossless default data. Therefore this is a proposed data/test coverage addition rather than a demonstrated incorrect clause. Parent should reject as a material defect if named shipped-data cases are not required for this assigned compatibility slice.',
 'validation': {'static_source': True, 'tools_data_census': True, 'independent_derived_case': True,
                'reference_execution': False, 'isolated_reference_execution': False,
                'independent_behavior_model_execution': False, 'host_execution': False, 'complete_demo_validation': False}
}

negative = {'evidence': 'TOOLS_SEARCH_WITH_MANUAL_HIT_CLASSIFICATION',
 'checks': [
  {'query': 'PBS root item section STICK/LEEK', 'result': 'LEEK at2072; no STICK section; legacy STICK in Gen5 backup1670'},
  {'query': 'PBS root move section VICEGRIP/VISEGRIP', 'result': 'VISEGRIP at5153; no VICEGRIP section; VICEGRIP in Gen5 backup3613'},
  {'query': 'All reference scripts VICEGRIP/VISEGRIP/STICK data aliases', 'result': 'No VICEGRIP hit. STICK appears only in handlers/AI and one move blacklist, not data registration.'},
  {'query': 'Compiler precompile rewrites and registry registration', 'result': 'VictoryME/BaseDamage field-name rewriting only; identifiers registered from section names; no alias normalizer.'},
  {'query': 'PBS discovery and backup selection', 'result': 'Root *.txt enumeration; no recursive Gen5 registration. No dedicated Gen5 facility trainer/template files exist.'},
  {'query': 'Entire frozen formal set STICK/VICEGRIP/VISEGRIP', 'result': 'STICK handler compatibility rows exist outside this generator slice; no named default template case or VICEGRIP/VISEGRIP template case.'},
  {'query': 'Generator entry under020_Debug', 'result': 'No separate pbWriteCup/pbGenerateChallenge menu. Debug file creation menu dispatches writer at1334-1407; facility set embeds generator UI.'},
  {'query': 'RuledTeam.compare/toStr/load/ratingRaw consumers', 'result': 'No normal generator consumers found. Defects or diagnostic assumptions are not promoted to normal-loop failures.'}
 ]}

ledger = {'reader': 'generator', 'scope': 'R6-F generator and immediate consumption/publication slice',
          'model': 'UNVERIFIED', 'reasoning_effort': 'UNVERIFIED', 'tier': 'UNVERIFIED', 'speed': 'UNVERIFIED', 'session_uuid': 'UNVERIFIED',
          'bindings': {'main_commit': '8ea169fbd0f33f378b5d732fd6bea59e854e04a6', 'main_tree': '6ab3429170d2762607fbc2237014c3a160449fa1',
                       'formal_tree': '1046fbb657882e84b3dfc6d017943a9edf7782e5', 'reference_commit': '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',
                       'reference_tree': '7589c800b61ba13a13040ed0d686979b80a84fd0'},
          'required_full_reads': required, 'method_units': rows, 'field_groups': fields,
          'coverage_limit': 'WP54 and shared combat catalog were read in full as contextual dependency text; their full reverse-source validation belongs to parent and sibling owners. Shared DX file read in full, but only GN24 and B17 facility-EV cases reversed here. Neither full131 formal inventory nor entire PBS species/move corpora claimed semantically reviewed.',
          'tool_census': 'compatibility-census.json scans all rows/fields of five active facility tables and identity membership, but is not a semantic-read certificate or compiler execution.',
          'semantic_complete_readable_unread': 0, 'semantic_attestation_date_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()}

report = """# R6-F generator independent review

Frozen main `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`, main tree `6ab3429170d2762607fbc2237014c3a160449fa1`, formal tree `1046fbb657882e84b3dfc6d017943a9edf7782e5`; read-only reference `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`, tree `7589c800b61ba13a13040ed0d686979b80a84fd0`. Bound reads assert unchanged frozen bytes. AGENTS.md was fully read before analysis; its bound transcript was also completed. read_bound.py was fully read before its first use. No git, source, reference, formal, save, security or network mutations occurred.

The four assigned generator files were fully semantically read: 338+359+211+438 = **1,346 lines**, all **62 defined method bodies**, associated fields, accessors, aliases, initializers, constants, disabled commentary and normal/nonconsumed consumers. Required readable-unread=0. WP76 279, WP54 main156/data109, shared combat catalog168 and shared DX catalog327 were fully read. The source-to-fact-to-consumer matrix is `forward-matrix.json`; clause-to-source/precondition mapping is `reverse-matrix.json`; `semantic-ledger.json` states which dependency/cross-owner material was context-read rather than fully reverse-validated. Presented-for-reading logs alone are not semantic certification.

No contradicted generator behavior clause was found. The prior specification already accurately records the current duplicate predicate, EV entry denominator, weighted move pruning/self-deletion and Sketch cache mutation, two-member rule phase, priority of all replacement branches, deletion skip, five unconditional opponent draws, cumulative game conservation, active rating mathematics, estimate-vs-real split, AI main command control, treatment/positional items rather than old injury snapshots, ordinary trainer-loop nontermination, preference/member-index asymmetry, prior-default inversion, and ordered non-atomic publication. Generated results, loaded checkpoints, default flags, type caches, names and field absence were traced to actual consumers. Unused diagnostic helpers were reviewed and classified; they do not establish failure of the normal generator.

One **tentative low-severity named-data coverage proposal**, `GR6-F-G001`, is in `findings.json`, pending the parent reviewer's non-proposer rebuttal. A read-only identifier/field census of all five active facility lists found two root-catalog mismatches in the default tower table: FARFETCHD/STICK and CRAWDAUNT/VICEGRIP. All other inspected identifiers, six trainer fields, EV labels and candidate indices passed that census. STICK and VICEGRIP exist in the Gen5 backup catalogs, while the current root catalogs define LEEK and VISEGRIP. The parser's already-correct generic behavior drops the item/move rather than creating aliases; actual default trainer rows consume both template indices. A successful later writer emits the changed fields. The proposal asks only for named static cases, and explicitly admits the strongest rebuttal: the existing generic contract already entails the result, so this is not a proved incorrect clause. No reference patch or future alias recommendation is proposed.

The census is **TOOLS_ONLY identifier/schema analysis**, not a semantic review of the entire species/item/move corpus, not execution of the compiler, and not a creature legality or battle-quality proof. Gen5 identity membership is an explicitly selected alternate-catalog comparison. No dedicated Gen5 facility lists are present; root discovery does not recurse into backups. Current list counts are 300/882, 200/363, 200/369, 300/284, 300/254 (trainers/templates). Counts and zero shape/index problems do not certify game legality or successful generation. Named source rows and relevant parser/writer/registry consumers were bound-read and semantically evaluated.

Evidence status: static source review and independent derived counterexample **performed**; read-only file/hash/identifier tooling **performed**; reference execution, isolated reference harness, independent executable behavior model, live host/UI, compiled data, checkpoint recovery, generation completion, combat results and complete Demo validation **NOT PERFORMED**. No claim is upgraded to those levels. Host/demo material and actual execution remain blockers to runtime proof, not blockers to this completed static review. Model, reasoning effort, service tier, speed and session UUID remain **UNVERIFIED** because no authoritative metadata echo was available; no quota/auth/config investigation was attempted.

The full R6-F verdict, WP54/55/57 coverage and global Feature Matrix belong to the parent reviewer. This report is the completed generator slice, with a tentative coverage proposal, not a global pass.
"""

status = {'task': 'R6-F/generator', 'status': 'STATIC_REVIEW_COMPLETE_PENDING_PARENT_REBUTTAL',
          'required_readable_unread': 0, 'four_source_files_full_semantic_read': True,
          'source_lines': 1346, 'method_units': 62, 'tentative_findings': 1,
          'confirmed_incorrect_generator_clauses': 0, 'parent_rebuttal_required': ['GR6-F-G001'],
          'model': 'UNVERIFIED', 'effort': 'UNVERIFIED', 'tier': 'UNVERIFIED', 'speed': 'UNVERIFIED', 'uuid': 'UNVERIFIED',
          'source_reference_execution': False, 'isolated_reference_validation': False,
          'independent_model_execution': False, 'host_validation': False, 'complete_demo_validation': False,
          'report': str((OUT/'report.md').relative_to(ROOT)), 'blocked_for_static_completion': False,
          'runtime_blockers': ['No host/demo execution authorized/performed; required original host/media/demo data remain unavailable in this slice.'],
          'modified_scope': 'Only generator audit artifact directory and authorized reader-generator binding logs.'}

OUT.mkdir(parents=True, exist_ok=True)
for filename, value in [('semantic-ledger.json',ledger), ('forward-matrix.json', {'schema':'unit→fact→consumer→spec','units':rows,'field_groups':fields}),
                        ('reverse-matrix.json', {'schema':'formal clause→source/preconditions','clauses':reverse}),
                        ('findings.json', {'tentative':[finding], 'confirmed':[], 'nonproposer_rebuttal':'PENDING_PARENT'}),
                        ('negative-search.json',negative), ('task-status.json',status)]:
    (OUT/filename).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
(OUT/'report.md').write_text(report)
print(json.dumps({'method_units': len(rows), 'reverse_clauses': len(reverse),
                  'required_readable_unread': sum(e['readable_unread'] for e in required), 'tentative': 1}))
