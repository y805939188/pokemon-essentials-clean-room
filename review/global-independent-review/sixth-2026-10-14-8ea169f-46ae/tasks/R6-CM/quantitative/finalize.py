from pathlib import Path
import json,hashlib
O=Path(__file__).parent;B='reference/pokemon-essentials/Data/Scripts/011_Battle/'
ledger=O/'reading-ledger.jsonl';records=[json.loads(x) for x in ledger.read_text().splitlines()]
records[0]['end_line']=297;records[0]['note']='AGENTS.md full file read first;297 lines (verified by wc); initial ledger end222 corrected.'
more=[
(B+'002_Battler/002_Battler_Initialize.rb',145,155,'closed the small initial output truncation'),
(B+'003_Move/005_MoveEffects_Misc.rb',598,693,'fresh future-attack and adjacent complete units'),
(B+'002_Battler/001_Battle_Battler.rb',80,122,'persistent HP and item writers;Wonder Room getters'),
(B+'002_Battler/001_Battle_Battler.rb',214,303,'full speed/weight consumers'),
(B+'001_Battle/001_Battle.rb',389,498,'owner-team bounds;living battler iteration;global/opposing abilities'),
(B+'002_Battler/008_Battler_UseMoveTargeting.rb',1,203,'continuous entire actual targeting caller read across1-95,96-175,176-203'),
(B+'007_Other battle code/006_Battle_Clauses.rb',1,60,'draw/recharge wrapper and clauses entry'),
(B+'007_Other battle code/006_Battle_Clauses.rb',190,235,'OHKO loaded-layer definitions;complete OHKOIce unit'),
(B+'007_Other battle code/009_Battle_ItemEffects.rb',364,425,'Oran/Sitrus exact helpers'),
(B+'007_Other battle code/009_Battle_ItemEffects.rb',1300,1337,'Jaboca exact reached-hit handler'),
(B+'002_Battler/004_Battler_Statuses.rb',1,575,'continuous full fresh statuses/helpers'),
(B+'002_Battler/005_Battler_StatStages.rb',1,387,'continuous full fresh stage/helper callers'),
(B+'003_Move/007_MoveEffects_BattlerOther.rb',552,603,'Twister sky multiplier and adjacent flinch/confusion units'),
(B+'003_Move/007_MoveEffects_BattlerOther.rb',100,174,'Toxic Thread and paralysis units'),
(B+'003_Move/007_MoveEffects_BattlerOther.rb',520,551,'full FlinchTarget inherited effect'),
(B+'003_Move/007_MoveEffects_BattlerOther.rb',75,99,'full PoisonTarget inherited effect'),
(B+'003_Move/012_MoveEffects_ChangeMoveEffect.rb',375,430,'full Fusion Bolt/Flare parameter and animation units'),
(B+'003_Move/004_Move_BaseEffects.rb',168,285,'multi-stat target lower preflight and commit'),
(B+'003_Move/001_Battle_Move.rb',1,79,'factory;critical-ratio configuration;inputs;two ranges1-49 and50-79'),
('reference/pokemon-essentials/Data/Scripts/001_Settings.rb',17,38,'default generation declaration'),
('reference/pokemon-essentials/Data/Scripts/002_BattleSettings.rb',1,83,'default damage/status/critical/affection switches'),
(B+'004_Scene/004_Scene_PlayAnimations.rb',215,245,'shared HP display updates and wait;static only'),
(B+'007_Other battle code/008_Battle_AbilityEffects.rb',1,70,'declared family metadata for independent static registry counts'),
(B+'007_Other battle code/008_Battle_AbilityEffects.rb',300,390,'Quick Feet;Surge Surfer;Light Metal;adjacent clauses'),
(B+'007_Other battle code/008_Battle_AbilityEffects.rb',844,872,'Quick Draw threshold and feedback'),
(B+'007_Other battle code/008_Battle_AbilityEffects.rb',1118,1197,'Victory Star and accuracy-target handlers'),
(B+'007_Other battle code/008_Battle_AbilityEffects.rb',1273,1286,'Huge Power exact handler'),
(B+'007_Other battle code/008_Battle_AbilityEffects.rb',1397,1474,'Steely Spirit;Technician;Tough Claws exact handlers'),
(B+'007_Other battle code/008_Battle_AbilityEffects.rb',1491,1505,'ally Steely Spirit exact handler'),
(B+'007_Other battle code/008_Battle_AbilityEffects.rb',1513,1555,'Fluffy;Grass Pelt exact handlers'),
(B+'007_Other battle code/008_Battle_AbilityEffects.rb',1601,1613,'Shadow Shield exact handler'),
(B+'007_Other battle code/008_Battle_AbilityEffects.rb',1625,1657,'Merciless/Battle Armor exact handlers'),
(B+'007_Other battle code/008_Battle_AbilityEffects.rb',2540,2552,'empty CertainSwitching declaration area'),
(B+'007_Other battle code/009_Battle_ItemEffects.rb',1,51,'declared family metadata'),
(B+'007_Other battle code/009_Battle_ItemEffects.rb',253,262,'Float Stone exact handler'),
(B+'007_Other battle code/009_Battle_ItemEffects.rb',346,363,'Micle exact helper'),
(B+'007_Other battle code/009_Battle_ItemEffects.rb',426,476,'Starf and Eject Pack exact helpers'),
(B+'007_Other battle code/009_Battle_ItemEffects.rb',551,585,'Mental Herb exact helper'),
(B+'007_Other battle code/009_Battle_ItemEffects.rb',648,738,'Quick Claw and lenses accuracy handlers'),
(B+'007_Other battle code/009_Battle_ItemEffects.rb',759,774,'Choice Band/Specs exact handlers'),
(B+'007_Other battle code/009_Battle_ItemEffects.rb',1170,1179,'Occa source binding'),
(B+'007_Other battle code/009_Battle_ItemEffects.rb',1371,1454,'Rocky Helmet;Rowap;Weakness Policy exact hit handlers'),
(B+'007_Other battle code/009_Battle_ItemEffects.rb',1525,1578,'Eject Button/Red Card exact after-use handlers'),
(B+'007_Other battle code/009_Battle_ItemEffects.rb',1580,1610,'Life Orb and Shell Bell exact parameters'),
(B+'007_Other battle code/009_Battle_ItemEffects.rb',1612,1750,'Throat Spray;Leppa;White Herb;XP/EV exact parameters'),
(B+'007_Other battle code/009_Battle_ItemEffects.rb',1790,1829,'all four terrain seed handlers'),
(B+'007_Other battle code/009_Battle_ItemEffects.rb',1834,1861,'Black Sludge/Leftovers exact handlers'),
(B+'007_Other battle code/005_Battle_CatchAndStoreMixin.rb',136,269,'capture scalar and random consumer only;not full storage review'),
(B+'007_Other battle code/010_Battle_PokeBallEffects.rb',120,192,'Heavy Ball source threshold including new3000/2000/1000 units'),
(B+'001_Battle/003_Battle_ExpAndMoveLearning.rb',55,82,'item EV then virus then cap consumer'),
(B+'001_Battle/003_Battle_ExpAndMoveLearning.rb',138,164,'persistent XP item consumer'),
('reference/pokemon-essentials/Data/Scripts/013_Items/002_Item_Effects.rb',434,460,'active Sitrus exact amount'),
('reference/pokemon-essentials/Data/Scripts/013_Items/003_Item_BattleEffects.rb',356,382,'active battle Sitrus exact amount'),
('reference/pokemon-essentials/Data/Scripts/013_Items/001_Item_Utilities.rb',333,381,'active HP recovery helpers and persistence cap'),
('deliverables/final-specification-set/pokemon-rules/wp48-ability-calculation-modifiers.md',196,240,'only scoped registry appendix and bounded formula context;not full WP48 semantic reread'),
('deliverables/final-specification-set/test-catalog/combat-requirements-wp47-ab.md',127,139,'supplementary Shadow fixture andSH01–SH09 read;onlySH01–04 checked here'),
]
for path,a,z,note in more:records.append({'path':path,'start_line':a,'end_line':z,'mode':'static_read','note':note})
for name,ids in [('moves.txt','TRIPLEKICK DRAGONDARTS SCALESHOT BEATUP PRESENT POLLENPUFF REST SHEERCOLD FINALGAMBIT MINDBLOWN STEELBEAM SOLARBEAM WATERSHURIKEN DRAININGKISS PAINSPLIT'.split()),('items.txt','ORANBERRY JABOCABERRY'.split())]:
 path='reference/pokemon-essentials/PBS/'+name;a=Path(path).read_text().splitlines()
 for ident in ids:
  start=a.index('['+ident+']');end=next((i for i in range(start+1,len(a)) if a[i].startswith('[')),len(a))
  records.append({'path':path,'start_line':start+1,'end_line':end,'mode':'static_read','note':'Full data section '+ident+';no content enabled or altered.'})
for name in ['008_Battle_AbilityEffects.rb','009_Battle_ItemEffects.rb']:
 path=B+'007_Other battle code/'+name
 records.append({'path':path,'mode':'static_text_registry_scan','note':'Reviewer-authored add/copy lexical expansion across full text for scoped pair counts. This is NOT a full semantic reading of the file.'})
ledger.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in records))
# Freeze hashes of the three primary formal inputs and the two source partitions.
inputs=['AGENTS.md','deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md','deliverables/final-specification-set/pokemon-rules/wp46-damage-healing-coverage.md','deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md',B+'003_Move/009_MoveEffects_MultiHit.rb',B+'003_Move/010_MoveEffects_Healing.rb']
(O/'input-identities.json').write_text(json.dumps({p:{'sha256':hashlib.sha256(Path(p).read_bytes()).hexdigest(),'bytes':len(Path(p).read_bytes()),'lines':len(Path(p).read_text().splitlines())} for p in inputs},indent=2)+'\n')
status=json.loads((O/'task-status.json').read_text())
status.update({'status':'COMPLETE_SCOPED_WITH_CROSS_DOMAIN_DEPENDENCIES','formal_tree':'1046fbb657882e84b3dfc6d017943a9edf7782e5','owned_source_full_continuous_read':{'009_MoveEffects_MultiHit.rb':633,'010_MoveEffects_Healing.rb':695},'primary_owned_class_count':59,'primary_owned_method_count':170,'inspection_metadata_count':4,'forward_records':233,'reverse_records':192,'shared_catalog_records_read_and_derived':185,'independent_constant_assertions':150,'numerical_discrepancies_proposed':0,'findings_proposed':0,'findings_confirmed_by_self':0,'cross_domain_semantic_dependencies':135,'non_proposer_rebuttal_and_root_adjudication':'No proposals submitted; parent retains final integration/adjudication. Cross-domain semantic rows are not marked PASS.'})
(O/'task-status.json').write_text(json.dumps(status,indent=2)+'\n');(O/'findings.json').write_text('[]\n')
print(json.dumps({'ledger_records':len(records),'status':status['status'],'files':len(list(O.iterdir()))},indent=2))
