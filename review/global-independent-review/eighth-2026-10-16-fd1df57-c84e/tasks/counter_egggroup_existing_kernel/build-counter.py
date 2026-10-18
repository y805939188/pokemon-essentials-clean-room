from pathlib import Path
import datetime,hashlib,json,subprocess
P=Path(__file__).resolve().parent;RR=P.parent.parent;B=Path('/workspace/pokemon-essentials-clean-room');R=Path('/workspace/pokemon-essentials')
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat();B8='fd1df570cad987dc3852a3b958f03916e317f7fe';RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def write(n,o):(P/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
prompt=RR/'delegation/prompts/counter_egggroup_existing_kernel.md';proposal=RR/'evidence/adjudication-inputs/9958b3fab32fd912124bfde83eddcbb6a3c2a8a4a66b6b3a8927c2be335e8110.json'
for p,size,sha in [(prompt,2875,'0308e2e885bc2cf6a9c62abe270b899993c9695ad5e13c88c66893c053a6dabf'),(proposal,17361,'9958b3fab32fd912124bfde83eddcbb6a3c2a8a4a66b6b3a8927c2be335e8110')]:
 raw=p.read_bytes();assert len(raw)==size and hashlib.sha256(raw).hexdigest()==sha;(P/p.name).write_bytes(raw)
lib=json.loads((RR/'tasks/coverage_acceptance_incremental/dispatch/kernel_atomic_reception.readset.json').read_text())['all_fixed_R432_F131_identity_library'];primary=json.loads((RR/'tasks/kernel_atomic_reception/reading-ledger.json').read_text())
rs={
 'egg':'Data/Scripts/010_Data/001_Hardcoded data/003_EggGroup.rb','generic':'Data/Scripts/010_Data/001_GameData.rb','species':'Data/Scripts/010_Data/002_PBS data/008_Species.rb','c1':'Data/Scripts/021_Compiler/001_Compiler.rb','c2':'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb','daycare':'Data/Scripts/012_Overworld/007_Overworld_DayCare.rb','pbs':'PBS/pokemon.txt','pool':'Data/Scripts/020_Debug/002_Editor_DataTypes.rb','chooser':'Data/Scripts/020_Debug/001_Editor_Utilities.rb'}
fs={'wp03':'deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md','wp18':'deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md','wp33':'deliverables/final-specification-set/creature-rpg/wp33-daycare-and-breeding-session.md','wp34':'deliverables/final-specification-set/pokemon-rules/wp34-inheritance-and-offspring.md','scope':'deliverables/final-specification-set/scope-statement.md','readme':'deliverables/final-specification-set/README.md','audit':'audit/source-traceability.md'}
identities={};gitchecks=[]
for repo,root,paths in [('R',R,rs),('F',B,fs)]:
 for key,path in paths.items():
  raw=(root/path).read_bytes();fixed=next((x for x in lib if x['repo']==repo and x['path']==path),None)
  if fixed:assert len(raw)==fixed['bytes'] and hashlib.sha256(raw).hexdigest()==fixed['sha256']
  else:
   assert key=='audit';start=datetime.datetime.now(datetime.timezone.utc).isoformat();a=subprocess.run(['git','show',B8+':'+path],cwd=B,capture_output=True);g=subprocess.run(['git','rev-parse',B8+':'+path],cwd=B,capture_output=True,text=True);end=datetime.datetime.now(datetime.timezone.utc).isoformat();assert a.returncode==0 and g.returncode==0 and a.stdout==raw
   fixed={'repo':'B8 supplemental audit','path':path,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'git_blob':g.stdout.strip(),'lines':len(raw.decode().splitlines())};gitchecks.append({'started_utc':start,'ended_utc':end,'commands':[['git','show',B8+':'+path],['git','rev-parse',B8+':'+path]],'exit_codes':[a.returncode,g.returncode],'stderr':[a.stderr.decode(),g.stderr],'actual_bytes_equal':True,'semantic_credit':'NONE_FROM_IDENTITY'})
  identities[key]={'fixed':fixed,'current_bytes_SHA_equal':True,'semantic_read_credit':'Exact actual full/partial reading separately ledgered; hash/wholeblob does not grant semantic approval.'}
write('input-identities.json',{'utc':NOW,'fixedB8':B8,'formal_tree':'f292698cdd4a8e725525a9be6dc34b75faaf151e','fixedR':RC,'R_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','inputs':identities,'supplemental_git_identity_only':gitchecks,'frozen_contract_and_query':[{'original':str(p.relative_to(RR)),'local_copy':p.name,'bytes':len(p.read_bytes()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [prompt,proposal]]})
unit_specs=[('EGG-ALL','egg',1,101),('GENERIC-SYMBOLS','generic',76,153),('SPECIES-SCHEMA','species',52,111),('SPECIES-INITIALIZE','species',175,223),('ENUM-CAST','c1',384,486),('CSV-RECORD','c1',690,737),('COMPILE-GENERIC','c2',4,67),('COMPILE-SPECIES','c2',283,383),('COMPILE-FORMS','c2',388,538),('DAYCARE-WHOLE','daycare',1,564),('ACTUAL-MRMIME-COMPLETE-RECORD','pbs',3218,3244),('EGG-POOL','pool',1040,1176),('CHOOSE-GAMEDATA','chooser',116,129)]
units=[]
for ident,key,a,z in unit_specs:
 root=R;path=rs[key];lines=(root/path).read_text().splitlines();assert z<=len(lines);units.append({'id':ident,'source_identity_ref':key,'range':[a,z],'text':'\n'.join(lines[a-1:z])+'\n','actual_reader':'/root/kernel_atomic_reception','qualification':'Complete necessary named definition/record or specified whole source; adjacent partial bodies not implicitly complete. Original sourceFULL credit only as explicitly ledgered.'})
write('necessary-source-units.json',{'utc':NOW,'units':units,'no_target_execution':True})
sections=json.loads((P/'sections.manual.json').read_text())
reads=[
 {'input':'complete prompt2875B','scope':'FULL_READ','evidence':['33abb3']},
 {'input':'complete query17361B','scope':'FULL_READ_ALL_FIELDS','evidence':['fc810a']},
 {'input':'WP03 complete393L','scope':'PRIOR_SAME_ACTUAL_CONTEXT_OWN_FULL_READ_RETAINED; current relevant complete sections reread','evidence':['tasks/kernel_atomic_reception/reading-ledger.json by exact path','78a386','ef042c navigation only','50e33d fullsection6']},
 {'input':'WP18 complete386L','scope':'FULL_READ','evidence':['269553 complete no truncation']},
 {'input':'WP33 complete213L','scope':'FULL_READ_AFTER_TRUNCATION_RECOVERY','evidence':['9f5b50 initially truncated no FULL','60fdc1 complete1–120','b08647 complete121–213']},
 {'input':'WP34 complete233L','scope':'FULL_READ','evidence':['c260fe complete']},
 {'input':'scope complete155L','scope':'FULL_READ_AFTER_TRUNCATION_RECOVERY','evidence':['973ae1 initialtruncated noFULL','fc3294 complete1–77','b61c35 complete78–155']},
 {'input':'final README complete169L','scope':'FULL_READ','evidence':['1dc7b9 complete1–110','50e33d complete111–169']},
 {'input':'EggGroup whole101L/Generic whole283L','scope':'OWN_FULL_READ_RECONFIRMED','evidence':['abf0a6','a890c5']},
 {'input':'Species/Compiler1/Compiler2 complete sources','scope':'PRIOR_SAME_ACTUAL_CONTEXT_OWN_FULL_READ; current complete necessary units reread','evidence':['tasks/kernel_atomic_reception/reading-ledger.json exact paths','abf0a6','181e88','99163e schema tail fullyrecovered']},
 {'input':'DayCare complete564L','scope':'OWN_FULL_READ_NEW_SAME_CONTEXT','evidence':['361657 complete1–280','136e9a complete281–564']},
 {'input':'PBS pokemon.txt','scope':'PARTIAL_COMPLETE_MRMIME3218–3244 only; no full898 or whole23115L transferred','evidence':['361657']},
 {'input':'Editor_DataTypes','scope':'PARTIAL complete GameDataPool/EggGroups1040–1176; no whole1706','evidence':['99163e']},
 {'input':'Editor_Utilities','scope':'PARTIAL complete pbChooseFromGameDataList116–129; no wholeUI or calledpbChooseList reception','evidence':['dd7c1c']},
 {'input':'audit1896L','scope':'PARTIAL complete purpose160–176 and four fullresponsibilityentries233–245/554–566/822–834/941–953; no wholeaudit/history','evidence':['78a386','a890c5','dd7c1c','ed6484/63825b truncated searches not negative/full credit']},
]
write('reading-ledger.json',{'utc':NOW,'reader':'/root/kernel_atomic_reception','records':reads,'direct_command_UTC':'Older direct commands captured by platform only, start/end UTC UNVERIFIED_NOT_CAPTURED; read.py I/O carries actual subprocess UTC. No estimated/retrofilled UTC.','negative_navigation_errors':['deliverables/audit/source-traceability.md wrong relative path in5a6577/2d3900; resolved actualaudit/source-traceability.md by79a6d4, zero unavailable-material credit.','Editor path was first queried in B instead ofR inef042c; resolved01e3a5/094646, zero false reading.'],'target_execution':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'})
out={'schema':'eighth-existing-kernel-independent-egggroup-finite-counter/v1','utc':NOW,'query_id':'PC-QUERY-EGGGROUP-DOMAIN-01','counterreviewer':'/root/kernel_atomic_reception','proposer':'/root/pbs_creature_current_cloud','actual_different_context':True,'request':{'model':'gpt-6.1-sol','effort':'ultra','tier':'defaultnormal','Fast':'off'},'actual':{'model':'UNVERIFIED','effort':'UNVERIFIED','tier':'UNVERIFIED','speed':'UNVERIFIED','Fast':'UNVERIFIED','opaque_id':'UNVERIFIED'},'fixedB8':B8,'fixedR':RC,'sections':sections,'source_units':'necessary-source-units.json','identity_ledger':'input-identities.json','reading_ledger':'reading-ledger.json','actual_IO':'io/*.json retains read-only command UTC/output/stderr/exit; first direct prior reads platform only','new_contexts':0,'new_votes':0,'new_required_counted_by_counter':0,'root_is_sole_final_classifier':True,'business_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
write('counterreview.json',out)
manifest=[]
for name in ['counterreview.json','necessary-source-units.json','input-identities.json','reading-ledger.json','sections.manual.json']:
 raw=(P/name).read_bytes();manifest.append({'path':name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
write('manifest.json',{'utc':NOW,'files':manifest,'target_execution':'NOT_EXECUTED','writes':'Onlythisauthorizedcounterdirectory; source/formal/audit/proposer/sharedstate untouched','main_task':'Return to KERNEL primary, responsibility unchanged.'})
print(json.dumps({'utc':NOW,'outputs':manifest,'classification':sections['1_exact_dispute_and_bounded_conclusion']['counter_recommendation'],'new_context_vote_required':0}))
