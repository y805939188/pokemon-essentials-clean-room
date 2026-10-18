"""Audit metadata correction only. Explicit actor attestation, never status-as-reader fallback."""
import json, hashlib, datetime, subprocess
from pathlib import Path
B=Path(__file__).parent
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
old=(B/'reading-ledger.json').read_bytes()
snapshot=B/'reading-ledger.v1.before-metadata-correction.json'
assert not snapshot.exists()
snapshot.write_bytes(old)
v1=json.loads(old)
# This explicit ordered readset is attested from this context's actual complete
# tool-read sequence, not inferred from a prior null reader or an external PASS.
own_reference=[
'Data/Scripts/007_Objects and windows/001_RPG_Cache.rb',
'Data/Scripts/007_Objects and windows/002_MessageConfig.rb',
'Data/Scripts/007_Objects and windows/003_Window.rb',
'Data/Scripts/007_Objects and windows/004_SpriteWindow.rb',
'Data/Scripts/007_Objects and windows/005_SpriteWindow_text.rb',
'Data/Scripts/007_Objects and windows/006_SpriteWindow_pictures.rb',
'Data/Scripts/007_Objects and windows/007_BitmapSprite.rb',
'Data/Scripts/007_Objects and windows/008_AnimatedBitmap.rb',
'Data/Scripts/007_Objects and windows/009_Planes.rb',
'Data/Scripts/007_Objects and windows/010_DrawText.rb',
'Data/Scripts/007_Objects and windows/011_Messages.rb',
'Data/Scripts/007_Objects and windows/012_TextEntry.rb',
'Data/Scripts/016_UI/001_Non-interactive UI/001_UI_SplashesAndTitleScreen.rb',
'Data/Scripts/016_UI/001_Non-interactive UI/002_UI_Controls.rb',
'Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb',
'Data/Scripts/016_UI/001_Non-interactive UI/004_UI_Evolution.rb',
'Data/Scripts/016_UI/001_Non-interactive UI/005_UI_Trading.rb',
'Data/Scripts/016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb',
'Data/Scripts/016_UI/001_Non-interactive UI/007_UI_Credits.rb',
'Data/Scripts/016_UI/001_UI_PauseMenu.rb',
'Data/Scripts/016_UI/002_UI_Pokedex_Menu.rb',
'Data/Scripts/016_UI/003_UI_Pokedex_Main.rb',
'Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb',
'Data/Scripts/016_UI/005_UI_Party.rb',
'Data/Scripts/016_UI/006_UI_Summary.rb',
'Data/Scripts/016_UI/007_UI_Bag.rb',
'Data/Scripts/016_UI/008_UI_Pokegear.rb',
'Data/Scripts/016_UI/009_UI_RegionMap.rb',
'Data/Scripts/016_UI/010_UI_Phone.rb',
'Data/Scripts/016_UI/011_UI_Jukebox.rb',
'Data/Scripts/016_UI/012_UI_TrainerCard.rb',
'Data/Scripts/016_UI/013_UI_Load.rb',
'Data/Scripts/016_UI/014_UI_Save.rb',
'Data/Scripts/016_UI/015_UI_Options.rb',
'Data/Scripts/016_UI/016_UI_ReadyMenu.rb',
'Data/Scripts/016_UI/017_UI_PokemonStorage.rb',
'Data/Scripts/016_UI/018_UI_ItemStorage.rb',
'Data/Scripts/016_UI/019_UI_PC.rb',
'Data/Scripts/016_UI/020_UI_PokeMart.rb',
'Data/Scripts/016_UI/021_UI_BattlePointShop.rb',
'Data/Scripts/016_UI/022_UI_MoveRelearner.rb',
'Data/Scripts/016_UI/023_UI_PurifyChamber.rb',
'Data/Scripts/016_UI/024_UI_MysteryGift.rb',
'Data/Scripts/016_UI/025_UI_TextEntry.rb']
own_formal=[
'deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md',
'deliverables/final-specification-set/user-interface/wp17-draw-text-tags.md',
'deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md',
'deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md',
'deliverables/final-specification-set/user-interface/wp65-controls-help-appendix.md',
'deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md',
'deliverables/final-specification-set/user-interface/wp65-trainer-card-appendix.md',
'deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md',
'deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md',
'deliverables/final-specification-set/user-interface/wp66-c-bag-item-storage-and-shop-ui.md',
'deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md',
'deliverables/final-specification-set/user-interface/wp67-b-lifecycle-presentations-and-history.md']
assert len(own_reference)==44 and len(own_formal)==12
own=set(own_reference+own_formal)
allids=json.loads((B/'identities.json').read_text())['records']
identities={x['path']:x for x in allids}
records=[]
for prev in v1['records']:
 path=prev['identity_path'];ident=identities[path]
 rec={**prev,'as_of_utc':now,'identity_binding':{'bytes':ident['bytes'],'sha256':ident['sha256'],'git_blob':ident['git_blob'],'commit':ident['commit']},'previous_record_reader':prev.get('reader'),'previous_record_status':prev['status']}
 if path in own:
  rec.update({'status':'FULL_READ','reader':'/root/ui_full','actual_reader':'/root/ui_full','credit':'OWN_ACTUAL_FULL_READ','own_full_read':True,'read_completion_time_exact':'NOT_RECONSTRUCTED_FROM_TRANSCRIPT','attested_complete_by_utc':now,'credit_basis':'Explicit present attestation of this actual context complete source/formal tool reads; not a fallback from missing actor, status, old PASS or peer.','peer_full_read_transferred_to_own':False})
 else:
  rec.update({'status':'PEER_FULL_READ_FACT_MEANING_RECEIVED; OWN_SOURCE_OR_FORMAL_UNREAD','reader':None,'actual_reader':None,'own_full_read':False,'credit':'PEER_FACT_RECEPTION_ONLY','ranges':[],'unread_ranges':[[1,ident['line_count']]],'peer_reader':'/root/ui_minigames','peer_reception':'minigames-reception.json#UI-RCP-MINIGAMES-01','peer_full_read_transferred_to_own':False,'atomic_mapping':'RECEIVED_COMPLETE_PROVIDER_MAPPING_WITH_RETAINED_INTERFACE_AND_HISTORY_OPEN'})
 records.append(rec)
v2={**v1,'schema':'gr8-ui-full-reading-ledger/v2','utc':now,'as_of_utc':now,'records':records,'own_reference_full':44,'own_reference_unread':7,'own_formal_full':12,'own_formal_unread':6,'primary_peer_fact_meaning_received':{'reference':7,'formal':6},'primary_entire_file_own_read_or_provider_fact_meaning_received':{'reference':51,'formal':18},'all_current_clauses_closed':False,'source_structure_denominator':'MANUAL_SEMANTIC_DECOMPOSITION_IN_PROGRESS_NOT_METHOD_COUNT','formal_atomic_denominator':'NOT_FINAL','previous_snapshot':{'path':snapshot.name,'bytes':len(old),'sha256':hashlib.sha256(old).hexdigest()},'older_root_frozen_snapshot':{'root_reported_bytes':30476,'root_reported_lines':1104,'root_reported_record_full_read_reference':41,'root_reported_record_full_read_formal':12,'sha256':'ROOT_OWNED_IDENTITY_NOT_REPORTED_HERE','state':'Unchanged root-owned snapshot; current v2 does not overwrite or retroactively promote its as_of counts.'},'correction':'Old top-level14/3 and37/15 were stale. Old null actor fields were missing metadata, not proof of an actor; this v2 supplies an explicit current actor attestation per exact owned path. Current44/12 does not backfill root frozen41/12.','full_read_is_not_atomic_closure':True,'business_execution_count':0,'execution':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'}
deps=json.loads((B/'dependency-identities.json').read_text())
v2['dependency_full_files']=sum(x['whole_file_read'] for x in deps['records'])
v2['dependency_partial_files']=sum(not x['whole_file_read'] for x in deps['records'])
data=(json.dumps(v2,ensure_ascii=False,indent=2)+'\n').encode()
(B/'reading-ledger.v2.json').write_bytes(data);(B/'reading-ledger.json').write_bytes(data)
receipt={'schema':'gr8-ui-ledger-correction-receipt/v1','id':'UI-AUDIT-LEDGER-CORRECTION-01','utc':now,'reason':'Root independent incremental audit found stale totals and missing actual actor metadata. Audit correction only, no business finding or formal change.','current_payload':{'path':'reading-ledger.v2.json','same_bytes_alias':'reading-ledger.json','bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()},'previous_current_payload':v2['previous_snapshot'],'root_frozen_payload':v2['older_root_frozen_snapshot'],'explicit_own_reference_paths':own_reference,'explicit_own_formal_paths':own_formal,'as_of_counts':{'own_reference':44,'own_formal':12,'peer_fact_received_reference':7,'peer_fact_received_formal':6,'own_unread_reference':7,'own_unread_formal':6},'metadata_only':True,'read_completion_timestamps_not_invented':True,'own_actor_not_inferred_from_null':True,'old_snapshot_not_promoted':True,'all_UI_approval':False,'business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'}
(B/'reading-ledger-correction-receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt['current_payload']));print('correction receipt',len((B/'reading-ledger-correction-receipt.json').read_bytes()),hashlib.sha256((B/'reading-ledger-correction-receipt.json').read_bytes()).hexdigest())
