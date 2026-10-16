import json,hashlib,pathlib,subprocess,datetime
root=pathlib.Path('/workspace/pokemon-essentials-clean-room')
p=root/'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/pbs_world_record_audit'
r=pathlib.Path('/workspace/pokemon-essentials')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def read(n):return json.loads((p/n).read_text())
def write(n,d):(p/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def identity(repo,commit,path):
 data=subprocess.check_output(['git','show',f'{commit}:{path}'],cwd=repo)
 ls=subprocess.check_output(['git','ls-tree',commit,'--',path],cwd=repo,text=True).split()
 return dict(repo=str(repo),commit=commit,path=path,git_mode=ls[0],git_blob=ls[2],bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),actual_matches_fixed=(repo/path).read_bytes()==data)
a=read('identities.json'); ledger=read('reading-ledger.json');den=read('input-record-denominator.json')
for group in [a['input_files'],den['files']]:
 for row in group:
  row['inventory_received_status']={'evidence_level':row.get('evidence_level'),'semantic_status':row.get('semantic_status'),'responsible_task':row.get('responsible_task')}
  row['evidence_level']='SOURCE_STATIC';row['semantic_status']='FULL_RECORD_SEMANTIC_READ';row['read_range']=[1,len((r/row['path']).read_text(encoding='utf-8-sig').splitlines())];row['semantic_reviewer']='/root/pbs_world_record_audit'
  row['semantic_read_basis']='Actual current full records; Gen6–8 exact-byte identity linked to default, no additional independent reader credit'
extra=[('PBS/battle_facility_lists.txt',[[1,25]]),('Data/Scripts/016_UI/005_UI_Party.rb',[[1204,1215]]),('Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb',[[267,273]]),('Data/Scripts/012_Overworld/002_Battle triggering/004_Overworld_EncounterModifiers.rb',[[47,60]]),('Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb',[[490,497]]),('Data/Scripts/018_Alternate battle modes/002_BugContest.rb',[[67,92]]),('Data/Scripts/012_Overworld/003_Overworld_Time.rb',[[1,82]])]
for path,ranges in extra:
 ident=identity(r,R,path);count=len((r/path).read_text(encoding='utf-8-sig').splitlines());ranges=[[b,min(e,count)] for b,e in ranges]
 row={'path':path,'ranges':ranges,'status':'FULL_READ' if ranges==[[1,count]] else 'PARTIAL_READ','line_count':count,'reviewer':'/root/pbs_world_record_audit','evidence_level':'SOURCE_STATIC','identity':ident,'recorded_utc':now}
 if not any(x['path']==path for x in ledger['dependency_reads']):ledger['dependency_reads'].append(row)
 if not any(x['path']==path for x in a['dependencies']):a['dependencies'].append(ident)
ledger['external_artifact_reads']=[{'path':'../../coverage/root-pbsw-001-counterreview.json','status':'FULL_READ','scope':'GR8-PBSW-001 actual distinct-context refutation, source-static no execution'},{'path':'../world_topology_audit/refutation-pbsw002.json','status':'FULL_READ','scope':'GR8-PBSW-002 actual nonproposer refutation; bounded clauses and records only'},{'path':'../world_topology_audit/interfaces.json','status':'FULL_CURRENT_SNAPSHOT_READ','scope':'IF-W01/W02/W05 reception; other interfaces not accepted wholesale'},{'path':'../world_topology_audit/forward.json','status':'SELECTED_FACT_OBJECTS_READ','scope':'W01–W06,W19–W21,W27–W30 only, no whole forward claim'}]
a['updated_utc']=now;a['status']='COMPLETED_SCOPED_RECORD_CONTRIBUTION_INTERFACES_PARTIAL';a['inventory_provenance_note']='Original INVENTORY_ONLY/UNREAD describes incoming delegation only; current own semantic status is separate and explicit.'
a['instructions_read']=[{'path':str(root/'AGENTS.md'),'bytes':(root/'AGENTS.md').stat().st_size,'sha256':hashlib.sha256((root/'AGENTS.md').read_bytes()).hexdigest(),'status':'FULL_READ'}, {'path':str(p.parent.parent/'inputs/review-SKILL.md'),'bytes':(p.parent.parent/'inputs/review-SKILL.md').stat().st_size,'sha256':hashlib.sha256((p.parent.parent/'inputs/review-SKILL.md').read_bytes()).hexdigest(),'status':'FULL_READ'}]
a['actual_scope_note']='Platform model/effort/tier/speed/opaque agent/session IDs remain UNVERIFIED; logical task path is echoed. Current HEAD is a permitted report successor; fixed objects govern judgments.'
ledger['updated_utc']=now;den['mechanical_only']=False;den['status']='ALL18_RECORD_SEMANTICS_COMPLETE';den['mechanical_validation_note']='Counts and identity checks validate bookkeeping; reading credit comes only from continuous actual source/record reads and declared exact-byte association.'
write('identities.json',a);write('reading-ledger.json',ledger);write('input-record-denominator.json',den)
prop=read('proposals.json');prop['updated_utc']=now
prop['records'][0]['independent_rebuttal']['artifact']='../../coverage/root-pbsw-001-counterreview.json'
prop['records'][0]['independent_rebuttal']['actual_artifact_read']='FULL_READ at '+now
prop['records'][0]['independent_rebuttal']['root_final_decision']='PENDING'
prop['records'][1]['independent_rebuttal']['artifact']='../world_topology_audit/refutation-pbsw002.json'
prop['records'][1]['independent_rebuttal']['actual_artifact_read']='FULL_READ at '+now
prop['records'][1]['independent_rebuttal']['root_final_decision']='PENDING'
write('proposals.json',prop)
interfaces=read('interfaces.json');interfaces['updated_utc']=now
for row in interfaces['interfaces']:
 if row['id']=='PBSW-I03':
  row['status']='BOUNDED_RECEPTION_WITH_NAMED_TAIL_PENDING'
  row['accepted']='Actual world reviewer IF-W01/W02/W05 and W01–W06/W19–W21/W27–W30 received for connection parser, bidirectional anchors and zero dimensions, nonresident map setup/resident reuse, mutable map-name localization and editor/ordinary-save persistence boundary. Shared 19 connection and global/player metadata facts independently read there.'
  row['evidence']='../world_topology_audit/interfaces.json IF-W01/W02/W05; forward.json selected exact W facts; refutation-pbsw002.json'
  row['remaining']='Full map-lifecycle/audio/weather/blackout/transfer and wider engine compound assertions not closed by this bounded producer contribution; actual maps and resources unavailable.'
 if row['id']=='PBSW-I07':row['evidence']='interface-facts.json GEN01–GEN08; full source read and bounded formal assertions, plus world W01/W03/W27 outer setup facts'
write('interfaces.json',interfaces)
genpath='Data/Scripts/012_Overworld/008_Overworld_RandomDungeons.rb'
gen={'schema':'gr8-world-exact-interface-facts/v1','reader':'/root/pbs_world_record_audit','utc':now,'identity':identity(r,R,genpath),'source_read':[[1,1107]],'premises':'Fixed R, standard GameData objects, no plugin overrides or external writes; source-stage reasoning only. Actual Map051 tileset/area/event binding and runtime absent.','facts':[
 {'id':'GEN01','lines':[347,382],'fact':'Dungeon construction precedes generate. Width/height below20 are node counts scaled by cell size plus screen buffer. Snap parameter odd-field writes can fail before generation because standard fields have no writer; no generator seed consumption or original map rewrite reached. All four present parameter×tileset pairs use even10/10/2, so that particular gate is skipped.','formal':['WP14§4.1','WP14§3.1.1 failure prefix']},
 {'id':'GEN02','lines':[428,431],'fact':'Choose parameter rng_seed, else global pending seed S, else system new seed, by Ruby truthiness; then clear S, then reseed global Random. Parameter priority still clears S. No local independent random stream or restoration is introduced. Failure evaluating selection may precede clear; failure in reseed follows clear. Host random implementation/sequence is unverified.','formal':['WP14§3.5','WP11§3.1.1']},
 {'id':'GEN03','lines':[432,450],'fact':'Negative usable drawing width or height returns normally after seed selection/clear/reseed. Otherwise redraw loop clears layout and reruns stages but never reseeds or clears the stored room-rectangle list; random consumption continues from the prior prefix. No retry bound or termination proof.','formal':['WP14§4.1','WP14§4.4/§3.5']},
 {'id':'GEN04','lines':[120,184],'fact':'Maze obtains visitable nodes before random starting-node selection and then reads its x/y. Empty visitable set fails before direction shuffling and subsequent room/decorative draws. No exact positive or zero random-channel consumption is inferred for native empty sample.','formal':['WP14§4.2','WP14§3.1.1 generation failure']},
 {'id':'GEN05','lines':[1063,1076],'fact':'Registered Dungeon flag gates receiver. Tileset/parameter lookup and Dungeon construction precede generate. Only after generate returns does original map receive width then height then data resize then tile writes. Generate-time exception does not reach these original-map writes; prior seed/random prefix remains.','formal':['WP14§3.1.1','WP14§6']},
 {'id':'GEN06','lines':[982,1005],'fact':'Tile conversion traverses x, then y, then layer; ignore retains old value, none writes0, large decoration draws four mapped choices and writes2×2 offsets. Exceptions retain already-written original-map prefix; no rollback/ensure. Tile random draws follow layout-generation draws on global channel.','formal':['WP14§5.1/§5.2','WP14§3.5']},
 {'id':'GEN07','lines':[1011,1039],'fact':'Placement clones stored rectangles, filters inadequate sizes, returns nil if none, else attempts1000 room/x/y choices. Checks occupied spacing only, not current floor terrain; success appends all event cells then returns bottom-left coordinate. Retained prior-redraw rectangles therefore remain conditional candidates; no actual bad seed or placement observed.','formal':['WP14§6.1','WP14§4.4']},
 {'id':'GEN08','lines':[1077,1107],'fact':'Each of100 rounds resets failed=false and occupied cells. Any event failure sets failed and aborts that round, leaving already-moved events. Player failure continues without setting failed. Only final failed=true raises. If all rounds have successful events but failed player, receiver returns normally with last event locations and old player_new_x/y. Successful player placement writes x then y. No transfer flag is set here and no rollback occurs; outer runtime-event creation and later subscriber effects require actual caller receipt.','formal':['WP14§6.2','WP14§3.1.1']}
], 'behavior':'NOT_EXECUTED','behavior_runs':0,'note':'These facts are a named bounded reception surface, not whole generator test/catalog PASS.'}
write('interface-facts.json',gen)
rv=read('review.json');rv['updated_utc']=now;rv['independent_support']['GR8-PBSW-002']='/root/world_topology_audit; tasks/world_topology_audit/refutation-pbsw002.json';rv['forward_field_count']=24980;rv['unresolved_interfaces']=['PBSW-I03 named lifecycle tails','PBSW-I04 full COM-FACILITY primary reception','PBSW-I05 grant/save tails','Explicit tails in PBSW-I06/I07/I08'];write('review.json',rv)
print('Updated only',p,'at',now)
