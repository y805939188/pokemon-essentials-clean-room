#!/usr/bin/env python3
"""Fixed Git/document inventory only; never execute source or static designs."""
import collections,csv,hashlib,io,json,re,subprocess
from pathlib import Path
P=Path('/workspace/b14-affected-b03');R=Path('/workspace/reference-b03');D=Path(__file__).resolve().parent
B='1e6b11a47370f1c7c4659a32443fc1afda597bac';C='47f7514765f8569ae9172bb06a2cd615e2b83b8a';S='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
G='93e10babe0b9c9ef8b3f5277754541b447beeeb4';PLAN='41fffb540c6483f5296ea0d33b789b75180d27ed';OLD='dea9d118d7ed3b7ddb57b1c4e7bd40db8dd06497'
AP='review/remediation/20261003-prepare/';BP=AP+'batches/B14/';CON=AP+'batches/B09/acceptance-stage-1/B14-downstream-contract.json';CP=BP+'candidate-1/'
E='deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md';Q='deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md'
checks=[]
def need(c,label):
 checks.append({'check':label,'pass':bool(c)})
 if not c:raise AssertionError(label)
def git(*args,repo=P):return subprocess.check_output(['git','-C',str(repo),*args])
def read(rev,path,repo=P):return git('show',rev+':'+path,repo=repo)
def obj(rev,path):return json.loads(read(rev,path))
def sha(data):return hashlib.sha256(data).hexdigest()
def stable(data):return sha(json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
def identity(rev,path,repo=P):
 data=read(rev,path,repo)
 return {'commit':rev,'path':path,'git_blob':git('rev-parse',rev+':'+path,repo=repo).decode().strip(),'sha256':sha(data),'bytes':len(data)}
def dump(name,value):(D/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def tsv(rev,path):return list(csv.DictReader(io.StringIO(read(rev,path).decode()),delimiter='\t'))

contract=obj(B,CON);request=obj(C,CP+'reverse-impact-packages.json')
package=next(x for x in request['accepted_owner_packages'] if x['accepted_owner']=='B03')
gate=next(x for x in contract['accepted_reverse_review_gates'] if x['accepted_batch']=='B03')
need(package['contract_gate']==gate,'exact B03 package matches accepted B09-C contract gate')
need(request['baseline']==B and not package['author_NOT_AFFECTED_assertion'],'candidate package fixed baseline no authored NOT_AFFECTED receipt')
need(git('merge-base',B,C).decode().strip()==B,'accepted predecessor ancestor of complete candidate')
need(git('branch','--show-current').decode().strip()=='remediation/20261003-prepare/review-B14-affected-B03-1','isolated requested review branch')
need(git('rev-parse','HEAD').decode().strip()==C,'review starts at fixed complete candidate')
delta=git('diff','--binary','--full-index','--no-renames','--no-ext-diff','--no-textconv','--no-color',B,C)
paths=git('diff','--name-status',B,C).decode().splitlines()
finals=contract['allowed_formal_write_paths'];originals=['specs/overworld/wp59-world-time-weather-field-moves.md','specs/overworld/wp60-fishing.md','specs/pokemon-rules/wp60-berry-plants.md','specs/pokemon-rules/wp61-field-passive-effects-and-blackout.md']
need(len(paths)==30,'complete unfiltered predecessor-to-candidate30paths')
need({x.split('\t')[1] for x in paths if x.startswith('M\t')}==set(finals+originals),'six final plus four originals only modified paths')
need(all(x.startswith('M\t') or x.startswith('A\t'+BP) for x in paths),'all20 additions are local B14 evidence')
changed=[]
for line in paths:
 status,path=line.split('\t');row={'status':status,'path':path,'candidate':identity(C,path)}
 if status=='M':row['accepted_predecessor']=identity(B,path)
 changed.append(row)
frozen_reads=[]
for row in gate['changed_planned_reverse_readers']:
 path=row['path'];current=identity(B,path)
 need(all(current[k]==row['current_baseline'][k] for k in ['git_blob','sha256','bytes']),'B03 stale reader baseline identity '+path)
 frozen_reads.append({'baseline':current,'candidate':identity(C,path),'changed':read(B,path)!=read(C,path)})
owner=obj(OLD,AP+'batches/B03/integration-review-1/finding-dispositions.json')
owner_paths=sorted({e['path'] for x in owner['dispositions'] for e in x['actual_project_evidence']} | {x['path'] for x in obj(OLD,AP+'batches/B03/integration-review-1/complete-diff-manifest.json')['formal_payload']})
for path in owner_paths:
 if path!=E:need(read(B,path)==read(C,path),'unchanged B03 owner prose/matrices original/final '+path)
approval=[x for x in tsv(B,AP+'approval-ledger.tsv') if x['candidate_commit']=='3c5728a47142c57abfdf3d55033768bc44a1f627']
need(len(approval)==27 and all(x['integration_review_commit']==OLD and x['reviewed_integration_commit']=='e24f2ac6f43642ea0e68bd9aa21fb2c313d6ebdf' and x['integration_verdict']=='PASS_SCOPED' for x in approval),'accepted B03 exact27 actual receipt records not candidate labels')
need(not git('diff','--name-only',B,C,'--',AP+'batches/B03/',AP+'batches/B09/acceptance-stage-1/',AP+'finding-ledger.tsv',AP+'approval-ledger.tsv',AP+'traceability-successor.tsv').strip(),'prior owner/B09-C/public registries immutable')
ledger=tsv(C,AP+'finding-ledger.tsv');need(len(ledger)==229 and all(x['canonical_state']=='OPEN' for x in ledger),'229 original canonical required OPEN')
for row in obj(C,CP+'validation.json')['checkpoint_files_preserved']:
 need(read('b37533ef1cfc7808ed41d64215647a78d165ada4',row['path'])==read(C,row['path']),'immutable scope checkpoint '+row['path'])
application=obj(C,BP+'author-stage-1/original-application.json')
for row in application['application']:
 path=row['path'];before=identity(B,path);after=identity(C,path)
 need(all(before[k]==row['before'][k] and after[k]==row['actual_after'][k] for k in ['git_blob','sha256','bytes']),'original application exact before/after '+path)
 patch=BP+'scope-proposal-1/original-patches/'+path.replace('/','__')+'.patch'
 need(sha(read(C,patch))==row['approved_patch_sha256'],'approved original patch frozen identity '+path)

original={x['id']:x for x in obj(G,'review/global-independent-review/2026-10-03-fd82a639/findings.json')};acceptance=obj(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json')
control_ids=gate['shared_control_ids'];adjacent=['GIR-FD82-C103','GIR-FD82-C104','GIR-FD82-C088']
controls={x['id']:x for x in contract['contribution_controls']}
bound=[]
for fid in control_ids+adjacent:
 o=original[fid];a=acceptance[fid];k=controls[fid]
 need(stable(o)==k['whole_original_object_sha256'] and stable(a)==k['whole_acceptance_object_sha256'],'complete original/acceptance binding '+fid)
 for field,value in k['complete_current_control_fields'].items():need(value==o.get(field),'complete current qualification field '+fid+' '+field)
 need(k['complete_minimum_acceptance_fields']['acceptance_gate']==a['acceptance_gate'],'original effective acceptance gate '+fid)
 bound.append({'id':fid,'scope':'B03 shared owner control' if fid in control_ids else 'Adjacent qualified interface only; no full B14 owner approval',
 'original_object_sha256':stable(o),'acceptance_object_sha256':stable(a),'complete_contract_control':k})
catalogs=[]
rowexpr=rb'^\| ([A-Z]+[A-Z0-9-]*\d+) \|'
def rows(data):return [(m[1].decode(),line) for line in data.splitlines(keepends=True) if (m:=re.match(rowexpr,line))]
for path in [E,Q]:
 old,new=rows(read(B,path)),rows(read(C,path));od=dict(old);nd=dict(new)
 need(len(od)==len(old) and len(nd)==len(new),'static row IDs unique '+path)
 need([k for k,line in new if k in od]==[k for k,line in old],'all old row ID order/multiplicity '+path)
 changed_ids=[k for k,line in old if nd[k]!=line];added=[k for k,line in new if k not in od]
 allowed=['WT03','WT07','WT09','WT14','WT15','WT17','WT18','WT20','WT23','WT25','FS02','FS03','FS06'] if path==E else ['FP01','FP02','FP06','FP12','FP14','FP15']
 need(changed_ids==allowed,'only19 named changed old rows '+path)
 preserved=[]
 for k,line in old:
  if k not in allowed:need(nd[k]==line,'old static row bytes '+k);preserved.append(k)
 if path==E:
  families=['MP','MV','EV','FW','IM','MR','DG'];b03=[k for k,line in old if re.sub(r'\d+$','',k) in families]
  need(len(b03)==251 and all(od[k]==nd[k] for k in b03),'all251 B03 row bytes preserved')
  need(read(B,path).split(b'## H.',1)[0]==read(C,path).split(b'## H.',1)[0],'full shared engine prefix before H preserved')
  b04=[k for k,line in old if k.startswith('B04-R')];need(len(b04)==28 and all(od[k]==nd[k] for k in b04),'all28 B04-R supplements preserved without B04 reapproval')
 else:need(all(od['BP'+str(i).zfill(2)]==nd['BP'+str(i).zfill(2)] for i in range(1,18)),'allBP01–17 preserved including GR012')
 catalogs.append({'path':path,'old_rows':len(old),'candidate_rows':len(new),'changed_old_ids':changed_ids,'new_ids':added,'preserved_old_ids':preserved,
 'family_counts':dict(collections.Counter(re.sub(r'\d+$','',k) for k,line in new)),'all_vectors_executed':False})
need(sum(x['old_rows'] for x in catalogs)==480 and sum(x['candidate_rows'] for x in catalogs)==503,'two whole catalog480→503 static designs')
source_reads=[
 ('Data/Scripts/004_Game classes/005_Game_MapFactory.rb','75–128;138–182','Connected crossing, enter callback dispatch and valid target/through/edge guard'),
 ('Data/Scripts/003_Game processing/002_Scene_Map.rb','1–29;35–104;120–180','Explicit rebuilt transfer, display update order, scene construction'),
 ('Data/Scripts/012_Overworld/001_Overworld.rb','120–210;220–255;297–316;540–552','Soot and double notifications; auto movement/ice; enter weather; location announcement'),
 ('Data/Scripts/004_Game classes/001_Game_Screen.rb','60–75','Weather intent type/power/duration storage'),
 ('Data/Scripts/005_Sprites/006_Spriteset_Global.rb','1–49','Intent type comparison and display fade consumer'),
 ('Data/Scripts/012_Overworld/001_Overworld visuals/001_Overworld_Weather.rb','66–99','Positive fade selection and in-flight guard only, no full renderer approval'),
 ('Data/Scripts/004_Game classes/006_Game_Character.rb','427–486;516–552;867–998','Route forcing/WAIT/terminal state, three literal prefixes, completed movement notification'),
 ('Data/Scripts/004_Game classes/008_Game_Player.rb','394–432;450–585','Player update and post-step/automatic-state gates'),
 ('Data/Scripts/012_Overworld/002_Overworld_Metadata.rb','112–128','forced_movement flag set distinct from route forcing'),
 ('Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb','414–516;875–990','FLY direct helper/callback/public consumer; waterfall start/traversal/direct/menu/interaction'),
 ('Data/Scripts/004_Game classes/004_Game_Map.rb','419–430','Soot erasure single selected layer'),
 ('Data/Scripts/015_Trainers and player/004_Player.rb','88–108','Soot clamp and actual resource delta'),
 ('Data/Scripts/001_Settings.rb','55','MAX_SOOT9999 constant'),
 ('Data/Scripts/012_Overworld/001_Overworld visuals/002_Overworld_Overlays.rb','1–58','Location delayed flag and FLY/message/map guard order only'),
 ('Data/Scripts/021_Compiler/001_Compiler.rb','95–149','ASCII field separator recognition, text read not compiler execution'),
 ('Data/Scripts/010_Data/002_PBS data/018_MapMetadata.rb','26–45','Weather data identity/schema boundary'),
 ('Data/Scripts/004_Game classes/007_Game_Event.rb','8–22;74–86;170–181','ASCII size/s:/sight/trainer/counter input markers'),
 ('Data/Scripts/012_Overworld/006_Overworld_BerryPlants.rb','150–163','Existing rain-category reader only, no full berry approval'),
 ('Data/Scripts/010_Data/001_Hardcoded data/012_Weather.rb','65–101','Rain/Storm category identities only'),
 ('Data/Scripts/007_Objects and windows/002_MessageConfig.rb','559–611','Fade wrapper cleanup propagates callback failure; no FLY destination cleanup')]
source=[]
for path,ranges,purpose in source_reads:
 i=identity(S,path,R);need(read(S,path,R)==(R/path).read_bytes(),'literal reference worktree fixed bytes '+path)
 source.append({**i,'literal_read_ranges':ranges,'purpose':purpose,'ranges_are_branch_coverage':False,'execution':False})
need(git('rev-parse','HEAD',repo=R).decode().strip()==S and git('rev-parse','HEAD^{tree}',repo=R).decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0' and not git('status','--porcelain',repo=R).strip(),'independent reference SHA/tree/clean')
need(git('remote','get-url','origin',repo=R).decode().strip()=='https://github.com/Maruno17/pokemon-essentials.git','independently obtained reference remote provenance')
white=subprocess.run(['git','-C',str(P),'diff','--check',B,C],capture_output=True,text=True)
white_rows=[x for x in white.stdout.splitlines() if re.search(r':\d+: ',x)]
need(white.returncode==2 and all(x.startswith(BP+'scope-proposal-1/original-patches/') and '.patch:' in x for x in white_rows),'raw whitespace warnings confined to literal approved original patches')
git('diff','--check',B,C,'--',':(exclude)*.patch');need(True,'all actual nonpatch formal/evidence whitespace check')
manifest={'reviewed_candidate':C,'candidate_tree':git('rev-parse',C+'^{tree}').decode().strip(),'accepted_predecessor':B,'predecessor_tree':git('rev-parse',B+'^{tree}').decode().strip(),
 'full_unfiltered_diff':{'method':'git diff --binary --full-index --no-renames --no-ext-diff --no-textconv --no-color predecessor candidate; no exclusions','bytes':len(delta),'sha256':sha(delta),'path_count':len(paths),'paths':changed},
 'B03_owner_package':package,'accepted_B09_contract':identity(B,CON),'declared_changed_readers_refrozen':frozen_reads,
 'accepted_B03_disposition_source':identity(OLD,AP+'batches/B03/integration-review-1/finding-dispositions.json'),
 'B03_formal_owner_paths':[{ 'baseline':identity(B,p),'candidate':identity(C,p),'unchanged':read(B,p)==read(C,p)} for p in owner_paths],
 'original_findings':identity(G,'review/global-independent-review/2026-10-03-fd82a639/findings.json'),'approved_acceptance':identity(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json'),
 'first_judgment_sha256':sha((D/'independent-first-judgment.json').read_bytes()),'full_delta_inventory_does_not_mean_unrelated_domain_approval':True}
dump('input-identity-manifest.json',manifest);dump('qualified-control-bindings.json',bound);dump('catalog-preservation.json',{'reviewed_candidate':C,'catalogs':catalogs,'B03_rows_preserved':251,'B04_supplement_rows_preserved':28,'behavior_execution':0})
dump('source-reading-log.json',{'reference_directory':str(R),'independent_reference_reused_from_own_prior_acquisition':True,'fresh_clone_claimed':False,'fixed_commit':S,'fixed_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','literal_reads':source,
 'FLY_callsite_search':'Fixed Scripts contains the helper definition and FieldMoves/Item_Effects/PauseMenu callers. No ordinary caller passing the optional block located; proposed exception fixture is a direct-helper supported-parameter static case, not default menu/runtime/plugin reachability.',
 'reference_execution':0,'helpers_executed':0,'historical_verifiers_executed':0,'static_vectors_executed':0,'runtime_observations':0,'proven_demo_chains':0})
dump('independent-validation.json',{'result':'PASS_FIXED_GIT_AND_DOCUMENT_INVENTORY_ONLY','semantic_review_verdict_separate':True,'reviewed_candidate':C,'check_count':len(checks),'checks':checks,'raw_diffcheck':{'returncode':white.returncode,'warnings':len(white_rows),'scope':'literal approved original patches only; nonpatch files pass separately'},'reference_execution':0,'behavior_execution':0,'canonical_closed':0})
print(json.dumps({'checks':len(checks),'paths':len(paths),'B03_rows':251,'catalogs':[x['candidate_rows'] for x in catalogs],'source_records':len(source),'result':'PASS_DOCUMENT_INVENTORY_NOT_SEMANTIC_VERDICT'},ensure_ascii=False))
