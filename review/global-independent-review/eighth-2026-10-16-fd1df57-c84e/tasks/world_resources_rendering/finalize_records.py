import json,datetime,hashlib,subprocess,collections
from pathlib import Path
D=Path(__file__).parent; R=Path('/workspace/pokemon-essentials'); C=Path('/workspace/pokemon-essentials-clean-room')
N=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text())
def write(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
base=read(D/'identities.json'); F=read(D/'forward-mapping.json'); V=read(D/'reverse-mapping.json')
files=base['files']; primary=[x['path'] for x in files[:33]]
full=set(primary)
full.update(['Data/Scripts/003_Game processing/001_StartGame.rb','Data/Scripts/003_Game processing/002_Scene_Map.rb','Data/Scripts/004_Game classes/005_Game_MapFactory.rb','Data/Scripts/012_Overworld/001_Overworld.rb'])
full_extra=['001_Technical/002_Files/001_FileTests.rb','001_Technical/006_RPG_Sprite.rb','002_Save data/004_Game_SaveValues.rb','007_Objects and windows/001_RPG_Cache.rb','007_Objects and windows/002_MessageConfig.rb','007_Objects and windows/004_SpriteWindow.rb','007_Objects and windows/008_AnimatedBitmap.rb','007_Objects and windows/009_Planes.rb','010_Data/001_Hardcoded data/012_Weather.rb','010_Data/002_PBS data/009_Species_files.rb','010_Data/002_PBS data/010_SpeciesMetrics.rb','010_Data/002_PBS data/014_TrainerType.rb','010_Data/002_PBS data/018_MapMetadata.rb','018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb','018_Alternate battle modes/001_SafariZone.rb','016_UI/001_Non-interactive UI/002_UI_Controls.rb','016_UI/012_UI_TrainerCard.rb']
full.update('Data/Scripts/'+x for x in full_extra)
full.add('Data/Scripts/011_Battle/007_Other battle code/007_BattleAnimationPlayer.rb')
full.add('Data/Scripts/004_Game classes/007_Game_Event.rb')
full.update(['Data/Scripts/002_Save data/001_SaveData.rb','Data/Scripts/002_Save data/002_SaveData_Value.rb','Data/Scripts/010_Data/001_GameData.rb'])
partial={
'Data/Scripts/004_Game classes/004_Game_Map.rb':[[104,181]],
'Data/Scripts/012_Overworld/003_Overworld_Time.rb':[[1,124]],
'Data/Scripts/011_Battle/001_Battle/001_Battle.rb':[[824,854]],
'Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb':[[360,579]],
'Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb':[[20,61]],
'Data/Scripts/019_Utilities/001_Utilities.rb':[[1,265]],
'Data/Scripts/010_Data/002_PBS data/006_Item.rb':[[1,235]],
'Data/Scripts/010_Data/002_PBS data/008_Species.rb':[[145,178]],
'Data/Scripts/014_Pokemon/001_Pokemon.rb':[[130,201]],
'Data/Scripts/010_Data/001_GameData.rb':[[1,250]],
'Data/Scripts/003_Game processing/004_Interpreter_Commands.rb':[[876,1075]],
'Data/Scripts/020_Debug/002_Editor_DataTypes.rb':[[820,895],[1620,1706]],
'Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb':[[1,115],[775,825]],
'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb':[[1,135],[1165,1200]],
'Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb':[[1,104],[681,740]],
'Data/Scripts/021_Compiler/001_Compiler.rb':[[220,310],[348,570],[640,681],[690,842]],
'Data/Scripts/016_UI/015_UI_Options.rb':[[1,48],[380,432]],
'Data/Scripts/011_Battle/004_Scene/002_Scene_Initialize.rb':[[1,185]],
'Data/Scripts/011_Battle/004_Scene/001_Battle_Scene.rb':[[285,338]],
'Data/Scripts/007_Objects and windows/007_BitmapSprite.rb':[[130,220]],
'Data/Scripts/007_Objects and windows/011_Messages.rb':[[211,243],[380,705]],
'Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb':[[110,184]],
'Data/Scripts/012_Overworld/006_Overworld_BerryPlants.rb':[[1,180]],
'Data/Scripts/012_Overworld/003_Overworld_WildEncounters.rb':[[72,183]],
'Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb':[[198,308],[355,431],[453,552]],
'Data/Scripts/002_Save data/005_Game_SaveConversions.rb':[[267,287]],
'Data/Scripts/018_Alternate battle modes/002_BugContest.rb':[[335,420]],
'Data/Scripts/016_UI/020_UI_PokeMart.rb':[[225,370]],
'Data/Scripts/001_Technical/002_RubyUtilities.rb':[[55,82],[390,406]],
'Data/Scripts/001_Technical/003_Intl_Messages.rb':[[478,552],[589,643],[675,823]],
'Data/Scripts/011_Battle/004_Scene/005_Battle_Scene_Menus.rb':[[1,159],[198,304]],
'Data/Scripts/017_Minigames/004_Minigame_VoltorbFlip.rb':[[1,22],[257,318]],
'deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md':[[1,180],[270,330]],
'deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md':[[1,115],[285,319]],
'deliverables/final-specification-set/generic-kernel/wp08-localization.md':[[38,105]]}
# Resolve locator mistakes only by unique current basename; record resolution.
allr=list(R.rglob('*.rb')); resolutions=[]
for path in list(partial):
 if not (R/path).exists() and not (C/path).exists():
  matches=[x for x in allr if x.name==Path(path).name]
  if len(matches)==1:
   actual=str(matches[0].relative_to(R));partial[actual]=partial.pop(path);resolutions.append({'requested':path,'resolved':actual})
extra_paths=set(full)|set(partial)
extra_paths.update(x['source']['path'] for x in F['units'])
extra_paths.update(x['path'] for x in read(D/'weather-shared-facts.json')['source_identities'])
aliases={'Data/Scripts/002_Save data/003_Save_Conversions.rb':'Data/Scripts/002_Save data/005_Game_SaveConversions.rb','Data/Scripts/010_Data/001_Hardcoded data/016_Evolution.rb':'Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb','Data/Scripts/020_Debug/001_Editor_DataTypes.rb':'Data/Scripts/020_Debug/002_Editor_DataTypes.rb','Data/Scripts/020_Debug/002_Editor_Screens.rb':'Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb'}
existing={x['path']:x for x in files if x['path'] not in aliases}
resolutions.extend({'requested':a,'resolved':b,'qualification':'prior own locator corrected, not actual missing material'} for a,b in aliases.items())
for path in sorted(extra_paths):
 if path not in existing:
  repo=C if path.startswith('deliverables/') else R
  existing[path]={'repo':str(repo),'path':path,'commit':base['B8'] if repo==C else base['R'],'scope':'named_additional_dependency','evidence_level':'UNREAD','semantic_status':'UNREAD'}
ledger=[]; problems=[]
for path,x in existing.items():
 repo=Path(x['repo']); fp=repo/path
 if not fp.exists():problems.append({'path':path,'reason':'PATH_MISSING_NOT_CREDITED'});continue
 b=fp.read_bytes(); ln=len(b.splitlines()); digest=hashlib.sha256(b).hexdigest();blob=subprocess.check_output(['git','hash-object','--stdin'],input=b,cwd=repo).decode().strip()
 frozen=x.get('git_blob')
 status='FULL_READ' if path in full else ('PARTIAL' if path in partial else 'UNREAD')
 rr=[[1,ln]] if status=='FULL_READ' else partial.get(path,[])
 x.update(bytes=len(b),sha256=digest,actual_blob=blob,actual_lines=ln,identity_checked_utc=N,matches_git_blob=(blob==frozen) if frozen else None,semantic_status=status,read_range=rr,evidence_level='SOURCE_STATIC_READ' if rr else 'INVENTORY_ONLY')
 if not frozen:
  cp=base['B8'] if repo==C else base['R']
  q=subprocess.run(['git','rev-parse',cp+':'+path],cwd=repo,capture_output=True,text=True)
  if q.returncode==0:x['git_blob']=q.stdout.strip();x['matches_git_blob']=blob==q.stdout.strip()
  else:problems.append({'path':path,'reason':'FROZEN_BLOB_LOOKUP_FAILED','exit':q.returncode,'stderr':q.stderr})
 un=[u['unit_id'] for u in F['units'] if u['source']['path']==path]
 ledger.append({'path':path,'repo':str(repo),'status':status,'continuous_read_ranges':rr,'complete_file_lines':ln,'source_units':un,'reader':'/root/world_resources_rendering','source_identity_ref':'identities.json#'+path,'kind':'PERSONAL_SOURCE_READ' if rr else 'NO_PERSONAL_SEMANTIC_CREDIT','limits':'Available unread text remains UNREAD; host/media execution is separately NOT_EXECUTED.','io':'read-io/index.jsonl and named exact stdout; initial unlogged reads remain platform-tool evidence only, never backdated local I/O.'})
base['files']=list(existing.values());base['updated_utc']=N;base['path_resolutions']=resolutions;base['identity_problems']=problems;write('identities.json',base)
stats=collections.Counter(x['status'] for x in ledger)
write('reading-ledger.json',{'schema':'gr8-personal-reading-ledger/v1','reader':'/root/world_resources_rendering','utc':N,'primary_reference_full':28,'primary_formal_full':4,'main_catalog_full':1,'primary_partial':0,'primary_unread':0,'all_inventory_status_counts':dict(stats),'files':ledger,'note':'Mechanical line/hash verification is identity only. Personal FULL_READ assignments are explicit manual semantic attestations carried across context; exact dependency partial ranges remain partial. Shared packets never change personal source statuses.','identity_problems':problems})

def snap(name,source,selector,key):
 obj=read(source); arr=obj[key]; picked=[x for x in arr if selector(x)]
 payload={'source':str(source),'source_sha256':hashlib.sha256(Path(source).read_bytes()).hexdigest(),'received_by':'/root/world_resources_rendering','utc':N,'qualification':'Complete selected fact objects read; finite source-static receipt only, never personal source FULL_READ or whole-domain acceptance.','objects':picked}
 write(name,payload);return payload
world=snap('world-facts.received.json',D.parent/'world_full/forward-mapping.json',lambda x:x['unit_id'] in [f'WFS-{i:03}' for i in list(range(12,24))+list(range(24,29))+list(range(36,49))+list(range(70,74))],'units')
ui=snap('ui-facts.received.json',D.parent/'ui_full/forward-mapping.json',lambda x:x['id'] in [f'UI17-U{i:03}' for i in [26,27,28,29,30,52]],'semantic_units')
kernel=snap('kernel-facts.received.json',D.parent/'kernel_review/file-unit-fact-consumer-spec-matrix.json',lambda x:x['fact_id'] in [f'KER-F{i}' for i in range(109,121)],'rows')
interfaces=[
{'id':'WRR-I01','status':'RECEIVED_BOUNDED','peer':'/root/world_interpreter','direction':'source receiver offered; peer read and accepted','units':['WRR-S01','WRR-X01'],'peer_units':['WIC223–251','IM26–35'],'boundary':'screen intent/game-clock/zero-duration old jobs; receiver requests only'},
{'id':'WRR-I02','status':'RECEIVED_BOUNDED','peer':'/root/world_interpreter','units':['WRR-P01','WRR-P02','WRR-P03'],'boundary':'picture slots/battle+50, erase/show clocks, timer'},
{'id':'WRR-I03','status':'RECEIVED_BOUNDED_TYPE_GUARD_ONLY','peer':'/root/world_interpreter','units':['WRR-C01'],'boundary':'type/active-fade gate only; peer has not received all176 weather atoms'},
{'id':'WRR-I04','status':'RECEIVED_BOUNDED','peer':'/root/world_interpreter','units':['WRR-A01','WRR-A02','WRR-A03'],'boundary':'logical records, memory aliases, scaling, request/failure; no actual sound'},
{'id':'WRR-I05','status':'RECEIVED_BOUNDED','peer':'/root/world_full','packet':'world-facts.received.json','boundary':'complete selected Map/Player/Time/FieldMoves/BattleStarting facts; source ownership remains world_full'},
{'id':'WRR-I06','status':'RECEIVED_BOUNDED_BY_PEER','peer':'/root/world_full','packet':'weather-shared-facts.json','peer_receipt':'WORLD-RCP-WEATHER-001','boundary':'176 WD/WS/WX atoms; no source-file personal credit for receiver'},
{'id':'WRR-I07','status':'RECEIVED_BOUNDED_BY_PEER','peer':'/root/ui_full','units':['WRR-P02','WRR-D07','WRR-D08','WRR-D09'],'peer_receipt':'tasks/ui_full/wrr-bounded-reception.json','boundary':'34 authored atoms; platform naming/load prefix/local rescue only'},
{'id':'WRR-I08','status':'RECEIVED_BOUNDED','peer':'/root/ui_full','packet':'ui-facts.received.json','boundary':'DrawText full selected payloads, especially U05218 image atoms; direct Bitmap requests differ from Cache/AnimatedBitmap'},
{'id':'WRR-I09','status':'RECEIVED_BOUNDED','peer':'/root/kernel_review','packet':'kernel-facts.received.json','boundary':'KER109–112 only; own complete resource consumer units D20–24 newly read; entire kernel reverse pending'},
{'id':'WRR-I10','status':'OPEN','peer':'root native/resource successors','boundary':'preflight report text partly received; 751 source facts/55 shaders/5 preludes/659 C/3 profiles not personally or wholly packet-read; no native backend/CFG/global-domain approval'},
{'id':'WRR-I11','status':'OPEN','peer':'resource_media_serialized','boundary':'8 fonts/SF2/messages full semantic reception absent; structure parsing not media approval; task launch not inferred'},
{'id':'WRR-I12','status':'RECEIVED_BOUNDED','peer':'/root/ui_full + own combat source read','boundary':'Evolution complete UI-EVO-LAST-BACK-01 received; normal Move/Common chain and full PBAnimationPlayer844 personally read, D27/D28; no whole battle-domain approval'},
{'id':'WRR-I13','status':'RECEIVED_BOUNDED_LOCAL_SAVE_AND_PBS','peer':'kernel SaveData/PBS writers','boundary':'supplement-v1.json41 newly read source atoms; complete SaveData82/Value284 + selected complete CSV writer/PBS path/metadata units; entire save/migration/native and unrelated PBS domains remain outside this receipt'}]
write('interfaces.json',{'schema':'gr8-resources-interfaces/v1','utc':N,'reader':'/root/world_resources_rendering','interfaces':interfaces,'counts':dict(collections.Counter(x['status'] for x in interfaces)),'execution':'NOT_EXECUTED','update_status':'UPDATE_NOT_STARTED'})
write('proposals.json',{'schema':'gr8-resources-proposals/v1','reader':'/root/world_resources_rendering','utc':N,'proposals':[],'candidate_count':0,'required_count':'ROOT_ADJUDICATION_ONLY','whole_domain_no_required_update':False,'counterreview':[{'id':'GR8-UI-002','file':'counter-ui002.json','role':'actual different nonproposer','recommendation':'reject nil-& exception rationale; no automatic replacement required claim','frozen_ui_v1_preserved':True}],'triage':[{'id':'WRR-TRIAGE-WEATHER-CAP','claim':'60 means per group/steady intensity; old and new groups can overlap above60','source':'Weather11,163–192,425–478','formal':'WP16§5.1/5.1.1 together with WP59§4.5 line169','ordinary_control':'stable one group max60','bounded_counterexample':'old Snow60 all visible with remaining lives beyond1.2s, fade to Blizzard60 with shift1; at1.2 new floor(60*.2/2) may be5 due floating value; old count not immediately hidden, hence >60 possible. Exact numerical runtime not executed.','status':'FINITE_WORDING_TRIAGE_NO_FORMAL_REVISION_PROPOSED','root_cause':'ambiguous aggregate reading; current joint formal already preserves natural death and stable s0–60','preserve':'existing type/fade guards and steady cap; do not create new mandatory by wording alone'}],'update_status':'UPDATE_NOT_STARTED'})
p=read(D/'progress.json');p.update(updated_utc=N,status='RUNNING_MAPPING_RECONCILIATION',semantic_primary_full=32,semantic_primary_partial=0,semantic_primary_unread=0,main_catalog_full=1,all_personal_counts=dict(stats),source_fact_atoms=F['manual_atom_count'],reverse_vector_rows=V['catalog_vectors_total'],reverse_vector_atomized=V['catalog_vectors_atomized'],reverse_vector_atoms=V['explicit_vector_atoms'],interfaces_open=2,interfaces_received=11,body_atomic_denominator=read(D/'body-reverse-mapping.json')['explicit_body_atoms'] if (D/'body-reverse-mapping.json').exists() else 'PENDING',identity_problems=problems,business_execution='NOT_EXECUTED',update_status='UPDATE_NOT_STARTED');write('progress.json',p)
print(json.dumps({'files':len(ledger),'counts':dict(stats),'identity_problems':problems,'path_resolutions':resolutions},ensure_ascii=False))
