import pathlib,json,datetime,subprocess,hashlib
V=pathlib.Path(__file__).parent;NOW=datetime.datetime.now(datetime.timezone.utc).isoformat();R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
F=json.loads((V/'forward-mapping.json').read_text());REV=json.loads((V/'reverse-mapping.json').read_text());assert len(F['atoms'])==1841
rows=[]
def a(unit,meaning,receiver,source='R19'):rows.append((source,unit,meaning,receiver))
for unit,meaning,receiver in [
 ('Replenish113–115','Pool replenishment runs only while current pool length<20, requesting random candidate with the currentrule and niltrainer.','F12§6.2L128:replenishment-target'),
 ('Replenish116–122','A candidate is appended only when no existing pool member satisfies the duplicate predicate; first duplicate breaks that scan.','F12§6.2L128:replenishment-duplicate-gate'),
 ('Replenish113–124','Rejected candidates retry indefinitely, with no iteration cap/progresscallback inside this helper; existing pools≥20 are not truncated.','F12§6.2L128/§10L256:replenishment-progress-boundary'),
 ('Duplicate126–127','Different species IDs immediately returnfalse before comparing moves/items/nature/EVs.','F12§6.1L121:species-first'),
 ('Duplicate130–133','Each move list contains exactly MAX_MOVES slots in original order, using nil for absent move positions.','F12§6.1L122:fixed-slot-lists'),
 ('Duplicate134–135','compact.sort results are discarded; source doesnot replace either original move array with those temporary results.','F12§6.1L122:nonmutating-sort-discarded'),
 ('Duplicate137','Equal fixed slot lists returntrue, including equal nil positions; the list length condition is already satisfied by the fixed-length collection loop.','F12§6.1L122:ordered-move-equality'),
 ('Duplicate138–140','If ordered moves differ, every main-stat EV equality is checked, then item_id AND nature_id AND allEV equality supplies the alternative duplicate result.','F12§6.1L123–124:alternative-trait-equality'),
 ('Duplicate126–141','Neither move-set reordering alone nor EV/item/nature disagreement alone excludes duplicate: the two positive criteria are OR after species match.','F12§6.1L124:OR-not-AND'),
 ('RemoveDuplicates143–150','De-duplication traverses input in order and builds a fresh result array retaining selected member identities.','F12§6.2L129:ordered-retention'),
 ('RemoveDuplicates151–154','A duplicate of any retained member is dropped; duplicate scan breaks immediately.','F12§6.2L129:duplicate-drop'),
 ('RemoveDuplicates155–158','For a nonduplicate scan, it counts same-species retained members and remembers their earliest index.','F12§6.2L129:same-species-count'),
 ('RemoveDuplicates160–162','A nonduplicate with at least10 retained members of its species evicts the earliest same-species member, then appends the new member.','F12§6.2L129:FIFO-ten-cap'),
 ('RemoveDuplicates143–166','The same-species10 cap is imposed only by an explicit call to this helper, not continuously by all pool insertions.','F12§6.2L129:cap-stage-scope'),
 ('Generate172–174','Main generation keeps the original rule reference, yields preparing text, then replaces local rule with rule.copy.setNumber(2).','F12§6.4L138:original-vs-copy-rule'),
 ('Generate175–177','It yieldsnil before separately loading pool<tag>.rxdata and teams<tag>_teams.rxdata; default rescue maps each caughtStandardError to its own empty array.','F12§6.4L139/§9.3L248–249:independent-checkpoint-loads'),
 ('Generate178–181','Existing-template seeding occurs only when loaded teams length<10 and selected BTPokemon table is nonnil/nonempty; level comes from the copiedrule.','F12§6.4L140:seed-gates-and-level'),
 ('Generate182–185','Every seed template creates a Pokemon at suggested level with IV31 and niltrainer; only copiedrule singlePokemon-valid members append to currentpool.','F12§6.4L140:seed-creation-and-legality'),
 ('Generate188–190','After optional seeding, it yields, replacespool by explicitdedup result, then yieldsagain.','F12§6.4L140:seed-dedup-order'),
 ('Generate191','Main target maxteams is600.','F12§6.4L141:team-target'),
 ('Generate192','Main cutoffrating is65.','F12§6.4L141:high-cutoff'),
 ('Generate193','Main toolowrating is40.','F12§6.4L141:low-cutoff'),
 ('Generate194–195','Main loop executes11 iterations if all preceding/current operations return normally.','F12§6.4L141:iteration-count'),
 ('Generate196–197','Each iteration first saves currentpool checkpoint, then yields Generating teams progress text.','F12§6.4L144:pool-save-before-progress'),
 ('Generate198–201','Existing-team scan starts index0, yieldsnil at multiplesof10, and replenishespool before evaluating any replacement branch.','F12§6.4L145:scan-pool-and-progress-order'),
 ('Generate202–203','First replacement branch requires team displayrating<65 AND visible totalGames≥80.','F12§6.4L145:first-replacement-gate'),
 ('Generate204–205','Only if first branch fails, membercount<2 replaces the team.','F12§6.4L145:second-replacement-gate'),
 ('Generate206–207','Only after firsttwo failures, index≥600 deletes this team at its current index.','F12§6.4L145:third-delete-gate'),
 ('Generate208–213','Only after earlierbranches fail, visiblegames≥250 retires: append each old team member to pool in team order, then construct replacement from that pool.','F12§6.4L145:fourth-retirement-order'),
 ('Generate214–215','Only after all firstfour fail, rating<40 replaces the team.','F12§6.4L145:fifth-low-gate'),
 ('Generate217','Scan cursor increments even after deletion; the shifted-in member at the deleted index is skipped this iteration.','F12§6.4L145:delete-cursor-skip'),
 ('Generate199–218','600 is not a universal saved-library maximum: excess teams can be replaced by earlierbranches or shifted past a deletion before another index check.','F12§6.4L145:target-not-invariant-cap'),
 ('Generate219–220','After scanning existingteams it saves teamlibrary checkpoint before yielding and before filling missing teams.','F12§6.4L146:pre-fill-team-save'),
 ('Generate221–225','While teamcount<600, it optionally yields at countmultiplesof10, replenishespool, then appends a newly sampled team; no branch truncates an oversized list here.','F12§6.4L146:fill-target'),
 ('Generate226–228','After filling, it savespool, sorts teams by descending displayrating, then yields Simulating battles text.','F12§6.4L147:presimulation-order'),
 ('Generate232–238','Every attacker index draws exactly five opponent indices unconditionally; next inside the five-times block doesnot exit that block or retain an earlier suitable opponent.','F12§6.4L148:five-draw-last-only'),
 ('Generate239','Only the fifth/current opponent value decides whether self-opponent skips the match.','F12§6.4L148:self-after-fifth'),
 ('Generate240–241','A nonself final opponent sets changedtrue then runs pbRuledBattle; changed is not used as a loop termination gate afterward.','F12§6.4L148:unused-changed-marker'),
 ('Generate243–247','After a full attacker pass, loopcounterincrements, sums current history lengths, yields, then compares integer sum/teams.length to12.','F12§6.4L148:global-integer-average'),
 ('Generate247','Average<12 repeats a full pass even if some teams already have12; average≥12 can finish despite other teams still having fewerthan12.','F12§6.4L148:average-not-per-team'),
 ('Generate248–249','At the accepted average, every team rating updates/clears in library order, then the simulation loop breaks.','F12§6.4L148:rating-settlement-before-break'),
 ('Generate251–252','Each completediteration sortsdescending again and saves the teamlibrary checkpoint.','F12§6.4L148:postiteration-team-save'),
 ('Generate254–256','After11 iterations, oldpool is replaced empty, nil progress is yielded, then teams sortascending by displayrating.','F12§6.4L149:final-reset-and-ascending-sort'),
 ('Generate257–261','Final collection skips teams with rating≤65, then appends all members of every >65 team; no early-break assumes sorted prefix suffices.','F12§6.4L149:strict-final-threshold'),
 ('Generate263–267','Local rule restores original before final dedup, Writing results text and tier arrangement; tier eligibility is under originalrule.','F12§6.4L138,149:restore-before-tier'),
 ('Generate268–270','It yieldsnil, invokes trainer allocation with finalpool/tag/originalrule while forwarding nilprogress callbacks, then yieldsnilagain.','F12§8/§6.4L149:allocation-handoff'),
 ('WriteCup276–277','WriteCup nondebug returns before any list load, message, reuse or generation.','F12§3.1L48:debug-gate'),
 ('WriteCup278','Only afterdebug gate, trainer_lists.dat load catches defaultStandardError and uses emptytable on that failure.','F12§3.2L52:initial-list-load'),
 ('WriteCup279–287','Displayoptions follow table order, use trainerfilename with only a final.txt suffix removed, and prefix defaultentries withasterisk.','F12§3.2L52:list-display-names'),
 ('WriteCup289–297','No-list question has YES/NO withcancel selectingNO; returnedYES0 maps to newmode2 andNO1 maps tostop0.','F12§3.2L53:no-list-question-mapping'),
 ('WriteCup299–302','Existing-list question offers NO/use-existing/use-new withcancelNO; command0 returns before any mutations.','F12§3.2L54:existing-question-mapping'),
 ('WriteCup305–306','Reuse list-selection cancel−1 skips the entire mutation/save/write block, then returns.','F12§4L60:reuse-selection-cancel'),
 ('WriteCup307–313','Successfulreuse first displays selected-list message, then removes all occurrences of challengeID from every nondefaultentry, preserving defaultentry ID arrays.','F12§4L61:reuse-ID-removal'),
 ('WriteCup314','Reuse appends challengeID only to selected nondefaultentry; choosingdefault doesnot add it there.','F12§4L61:reuse-default-exception'),
 ('WriteCup315–317','Reuse saves.dat before Graphics.update and full Compiler.write_trainer_lists call.','F12§4L62/§8.4L231:reuse-write-prefix'),
 ('WriteCup308–317','Reuse doesnot change any defaultflag; later writerfailure doesnot undo ID migration or earlier.datsave.','F12§4L61–62/§10L264:reuse-defaultflags-and-prefix'),
 ('WriteCup320–322','New-generation mode asks a second confirmation; false returns before creatingmessagewindow or startinggenerator.','F12§3.2L55:new-confirmation-gate'),
 ('WriteCup322–324','Confirmedgeneration creates the messagewindow then reads uptime before invoking main generation.','F12§3.2L55:progress-window-start'),
 ('WriteCup325–328','At each reached progresscallback, elapsed≥5 increments trackedtime by5 and calls Graphics.update once; it is not a continuous independenttimer.','F12§3.2L55:callback-five-second-gate'),
 ('WriteCup329–333','Any truthy progressmessage displays with letterbyletterfalse, resets trackedtime to currentuptime, then refreshesGraphics.','F12§3.2L55:text-progress-immediate'),
 ('WriteCup324–334','Progresscallback doesnot inspect usercancel; long computation without callback can leave noUIrefresh despite elapsed5seconds.','F12§3.2L55–56:no-intermediate-cancel-or-watchdog'),
 ('WriteCup335–336','Only after main generation returns normally does it dispose the window and request completionmessage, in that order.','F12§3.2L55:normal-completion-ui'),
 ('WriteCup276–338','No ensure rolls back migration/checkpoints/writes or guarantees messagewindowdisposal on arbitrary error.','F12§10L257/§8.4L231:generator-error-prefix'),
]:a(unit,meaning,receiver)

for source,unit,meaning,receiver in [
 ('S01','MAX_MOVES97','Default Pokemon.MAX_MOVES is4, so generator duplicate slot vectors contain four positions even when some are nil.','F12§6.1L122:default-four-slots'),
 ('GEN-STAT','Stat.each_main24–26/register59–105','Main-stat iteration selects main/main_battle types: HP,ATTACK,DEFENSE,SPECIAL_ATTACK,SPECIAL_DEFENSE,SPEED in fixedregistration order, excluding accuracy/evasion.','F12§6.1L123:all-six-EV-comparison'),
]:a(unit,meaning,receiver,source)

premise=('FixeddefaultR/B8 without later overrides; validparty/team/template/rule/input types and numeric fields, successfulcalled allocation/registry/serialization/message callbacks to each stated observation unless explicitly a failureprefix. '
         'Rulecopy/subset differences, individualcreator7facts54units, battle/rating152facts and existingfinite rulewrappers retain their exact ownpremises. '
         'No generator/compile/IO/nativeUI/random/model execution; datafile snapshot absence is not a guarantee after latercompilation. Probabilities assume ordinaryuniformoffsets only, actualsequence/distribution/quality unknown. '
         'Source helpers and progress markers are audit descriptions, not a required futureclass/API design.')
new=[]
for n,(source,unit,meaning,receiver) in enumerate(rows,1842):
    atom={'id':f'FAC-A{n:04}','source':source,'unit_locator':unit,'assertion':meaning,'formal_receivers':[receiver],'premise':premise,'pending_dependencies':[],'status':'BOUNDED_SOURCE_FACT_AND_EXPLICIT_FORMAL_CHILD_OR_AUDIT_SCOPE_ROUTING','evidence':'SOURCE_STATIC','execution':'NOT_EXECUTED','reader':'/root/facility_atomic_completion_cloud'};new.append(atom);REV['mappings'].append({'formal_clause':receiver,'atomic_assertion':atom['id'],'meaning':meaning,'source':source,'source_unit':unit,'premise':premise,'status':atom['status'],'pending_dependencies':[],'relation':'EXPLICIT_NAMED_GENERATOR_POOL_ITERATION_CHILD_OR_AUDIT_SCOPE'})
p='Data/Scripts/010_Data/001_Hardcoded data/008_Stat.rb';b=subprocess.check_output(['git','-C','/workspace/pokemon-essentials','show',R+':'+p]);sid={'repo':'/workspace/pokemon-essentials','commit':R,'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'blob':subprocess.check_output(['git','-C','/workspace/pokemon-essentials','rev-parse',R+':'+p]).decode().strip()};F['source_identities']['GEN-STAT']=sid
F['atoms'].extend(new);F['bounded_denominator']=len(F['atoms']);F.setdefault('v2_increments',[]).append({'path':'generator-pool-iteration-entry-atomic-increment.v2.json','count':len(new),'ids':[new[0]['id'],new[-1]['id']],'utc':NOW});REV['true_bounded_assertions']=len(F['atoms']);REV['v2_new_exact_child_bindings']=len(REV['mappings'])-992
packet={'schema':'facility-generator-pool-iteration-entry-manual-meaning-increment/v2','utc':NOW,'reader':'/root/facility_atomic_completion_cloud','explicit_source_assertions':new,'source_identities':{k:F['source_identities'][k] for k in ['R19','R22','S01','GEN-STAT','F12']},'complete_supplemental_units':[{'identity':sid,'range':[1,119],'content':b.decode(),'actual_reader':'/root/facility_atomic_completion_cloud','qualification':'OwnwholeStat119Ltext; mainstatfiniteuse only, no PBSdomain/runtime inheritance.'},{'identity':F['source_identities']['S01'],'range':[97,97],'content':'  MAX_MOVES     = 4','actual_reader':'/root/facility_atomic_completion_cloud','qualification':'Complete constant declaration only.'}],'actual_source_reads':['a6cabd R19L113–275 completehelpers/mainloop','95df19 R19L276–338 completewriteCup','fad398 wholeStat119/PokemonMAXMOVESconstant','priorR19L1–112fulltier/readset andfinite46childpacket'],'actual_formal_reads':['95df19 WP76L1–62','6276b9 WP76L113–206','priorwholeWP76all279','v1completeMessages/confirm/showcommands namedmethods actualread retained'],'qualification':'All newly listed source facts manually authored, some mechanical antecedents remainaggregated. No fullcanonical originalsource/formaldenominator or allGNvector prerequisiteclosure. Mainloop/nativewrite/callback outcomes remain conditional; fullindividual/rules/sourcefacts are separately bounded receipts. CurrentWP76 already describes unusual branches/limits correctly.','OPEN':['R20 candidate/legalmove/cache/rejection/fullprimarytrait inputs andR21 allocation/write compiler/normalization meanings','453species649classes2732provenances/proofinputqualification andallGN/B17/full964seed/202externalchildreception','ExactData/Compiler/writer andnormalcurrentB8/historylimitedreceipts still separately needed; newsourceFULL not totalacceptance'],'new_required':0,'new_optional':0,'new_contexts':0,'new_votes':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
def dump(n,x):(V/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
dump('generator-pool-iteration-entry-atomic-increment.v2.json',packet);dump('forward-mapping.json',F);dump('reverse-mapping.json',REV)
P=json.loads((V/'progress.json').read_text());P.update(updated_utc=NOW,manually_authored_finite_source_assertions=len(F['atoms']),source_to_formal_bindings=len(REV['mappings']),finite_new_child_bindings=len(REV['mappings'])-992,state='RUNNING_R20_R21_PRIMARY_TRAIT_AND_CATALOG_TAILS');dump('progress.json',P)
D=json.loads((V/'atomic-denominator.json').read_text());D['updated_utc']=NOW;D['manual_bounded_source_assertions'].update(count=len(F['atoms']),id_end=new[-1]['id']);D['finite_reverse_bindings'].update(count=len(REV['mappings']),qualification=f"992historicalregionbindings+{len(REV['mappings'])-992}newexplicit source/audit/case-childroutes; notglobalformaldenominator.");D['finite_generator_pool_iteration_entry']={'source_assertions':len(new),'membership':'generator-pool-iteration-entry-atomic-increment.v2.json','qualification':packet['qualification']};dump('atomic-denominator.json',D)
L=json.loads((V/'reading-ledger.json').read_text());L['updated_utc']=NOW;L.setdefault('v2_additional_source_reads',[]).append({'utc':NOW,'packet':'generator-pool-iteration-entry-atomic-increment.v2.json','actual_reads':packet['actual_source_reads'],'qualification':'WholeStat119source ownread, finite6mainstatconsumer; no primarydataset/normaltraitproof inheritance.'});dump('reading-ledger.json',L)
b=(V/'generator-pool-iteration-entry-atomic-increment.v2.json').read_bytes();print('new',len(new),'range',new[0]['id'],new[-1]['id'],'total',len(F['atoms']),'routes',len(REV['mappings']),'bytes',len(b),'sha',hashlib.sha256(b).hexdigest())
