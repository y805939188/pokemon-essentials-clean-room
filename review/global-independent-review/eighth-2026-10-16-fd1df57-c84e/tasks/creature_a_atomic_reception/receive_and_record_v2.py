import json, pathlib,hashlib,subprocess,datetime
P=pathlib.Path(__file__).parent;BASE=P.parent.parent;R=pathlib.Path('/workspace/pokemon-essentials');NOW=datetime.datetime.now(datetime.timezone.utc).isoformat(); COMMIT='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';TREE='7589c800b61ba13a13040ed0d686979b80a84fd0'
def sha(b):return hashlib.sha256(b).hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def ident(path):
 b=(R/path).read_bytes(); fixed=subprocess.check_output(['git','show',COMMIT+':'+path],cwd=R); assert b==fixed,path
 return dict(repo='R',commit=COMMIT,tree=TREE,path=path,bytes=len(b),sha256=sha(b),blob=subprocess.check_output(['git','rev-parse',COMMIT+':'+path],cwd=R,text=True).strip(),lines=len(b.splitlines()))
l=json.loads((P/'reading-ledger.json').read_text())
for path in ['Data/Scripts/012_Overworld/007_Overworld_DayCare.rb','Data/Scripts/016_UI/001_Non-interactive UI/004_UI_Evolution.rb','Data/Scripts/010_Data/002_PBS data/003_Type.rb','Data/Scripts/010_Data/002_PBS data/004_Ability.rb']:
 if path not in {x['path'] for x in l['own_full_reads']}:
  d=ident(path);d.update(status='FULL_READ_BY_SELF',reader='/root/creature_a_atomic_reception',extent=[1,d['lines']],source_of_read='Actual complete source output, contiguous pieces reaching EOF; Type/Ability complete cat',semantic_time_utc='UNRECORDED_PER_CALL',recorded_utc=NOW,primary=False,qualification='Own source reading only; no whole consumer/domain PASS');l['own_full_reads'].append(d)
spans=[
('Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb',1,117,'pbStartScene and pbStartSceneBrief complete; adjacent comments retained'),
('Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb',134,204,'pbUpdateDummyPokemon, pbGetAvailableForms complete; adjacent fragments excluded'),
('Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb',791,947,'compile_trainers, validate_trainers and validate_all_compiled_data complete'),
('Data/Scripts/019_Utilities/001_Utilities.rb',239,284,'pbChangePlayer, pbTrainerName, pbSuggestTrainerName, pbGetUserName complete'),
('Data/Scripts/004_Game classes/008_Game_Player.rb',560,616,'pbGetPlayerCharset, vehicle-refresh/cancel/bike helpers complete named units'),
('Data/Scripts/012_Overworld/001_Overworld.rb',128,144,'on_player_step_taken soot handler complete'),
('Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb',125,202,'Double/Triple/skip-battle and partner setup complete named units'),
('Data/Scripts/016_UI/020_UI_PokeMart.rb',1,98,'PokemonMartAdapter complete'),
('Data/Scripts/016_UI/020_UI_PokeMart.rb',579,721,'PokemonMartScreen complete'),
('Data/Scripts/016_UI/021_UI_BattlePointShop.rb',1,90,'BattlePointShopAdapter complete'),
('Data/Scripts/016_UI/021_UI_BattlePointShop.rb',427,508,'BattlePointShopScreen complete'),
('Data/Scripts/011_Battle/001_Battle/001_Battle.rb',303,318,'pbParty and pbPartyStarts complete'),
('Data/Scripts/011_Battle/001_Battle/001_Battle.rb',387,414,'team range/team iteration complete named helpers'),
('Data/Scripts/011_Battle/001_Battle/001_Battle.rb',432,439,'pbMaxLevelInTeam complete'),
('Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb',56,65,'pbCheckHiddenMoveBadge complete'),
('Data/Scripts/012_Overworld/002_Battle triggering/005_Overworld_RoamingPokemon.rb',135,185,'on_wild_species_chosen complete roaming handler'),
('Data/Scripts/016_UI/023_UI_PurifyChamber.rb',348,628,'PokemonPurifyChamberScreen complete class'),
('Data/Scripts/016_UI/023_UI_PurifyChamber.rb',1072,1088,'Scene pbUpdate/pbRefresh complete named methods'),
('Data/Scripts/003_Game processing/005_Event_Handlers.rb',97,139,'HandlerHash complete class'),
('Data/Scripts/003_Game processing/004_Interpreter_Commands.rb',1099,1109,'command_314 complete'),
('Data/Scripts/011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb',107,185,'pbObedienceCheck and pbDisobey complete'),
('Data/Scripts/018_Alternate battle modes/002_BugContest.rb',205,230,'pbEnd complete'),
('Data/Scripts/019_Utilities/001_Utilities.rb',452,487,'pbMoveTutorChoose complete'),
('Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb',1,64,'Evolution class/dispatch definition complete'),
('Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb',265,277,'Shedinja registration and complete after_evolution_proc'),
('Data/Scripts/021_Compiler/001_Compiler.rb',384,487,'cast_csv_value and checkEnumField complete'),
('Data/Scripts/021_Compiler/001_Compiler.rb',690,737,'get_csv_record complete')]
# Resolve only path spelling by exact basename inventory. A correction does not create semantic read credit.
files=[str(x.relative_to(R)) for x in (R/'Data/Scripts').rglob('*.rb')]
for path,a,b,u in spans:
 if not (R/path).exists():
  cand=[f for f in files if pathlib.Path(f).name==pathlib.Path(path).name]
  assert len(cand)==1,(path,cand);path=cand[0]
 k=(path,a,b);ex=l.setdefault('own_partial_read_spans',[])
 if k in {(x['path'],*x['range']) for x in ex}:continue
 d=ident(path);raw=(R/path).read_bytes(); norm=('\n'.join(raw.decode('utf-8-sig').splitlines()[a-1:b])+'\n').encode();d.update(range=[a,b],named_units=u,status='PARTIAL_FILE_ACTUAL_READ_SPAN',reader='/root/creature_a_atomic_reception',recorded_utc=NOW,semantic_time_utc='UNRECORDED_PER_CALL',normalized_span_sha256=sha(norm),normalized_span_bytes=len(norm),qualification='Complete named units only; no whole file credit, adjacent fragments carry no separate complete-unit claim');ex.append(d)
save(P/'reading-ledger.json',l)
s=json.loads((P/'sourcefact-consumer-receptions.json').read_text())
for relative,expected in [('tasks/ui_full/facility-entry-interface.json','aacdf54eacbfa6ce650051d45a17102ea580820a133fb09d44ba4fe3123e51e9'),('tasks/ui_full/facility-lifecycle-interface.json','1cf941cf4abb86d4f5c1f8087b0af839b0755ee8988152ca109898df50a04607'),('adjudication/root-chamber-receiver-reception.json','dbb6d3c76c62007ac8face120a2d4b3268bd0d6d6c040581effc51d0b45f50f7')]:
 src=BASE/relative;b=src.read_bytes();assert sha(b)==expected,(relative,sha(b));payload=json.loads(b);dst=P/'received-snapshots'/('received-'+src.name);dst.write_bytes(b)
 if relative not in {x.get('source_path') for x in s['named_contributions']}:
  facts=payload.get('facts',[])
  s['named_contributions'].append(dict(package=src.name,source_path=relative,original_reader=payload.get('reader',payload.get('actual_independent_receiver')),receiver='/root/creature_a_atomic_reception',recorded_utc=NOW,bytes=len(b),sha256=sha(b),snapshot=str(dst.relative_to(P)),complete_payload_actually_read=True,adopted_complete_fact_ids=[x.get('id') for x in facts],fact_count=len(facts),received_complete_semantic_payload=payload,own_source_full_read_granted=False,qualification='Finite complete payload/common premise receipt; exact original reader/source scope preserved. Root receipt adds minimum parameter-receiver qualification, no new finding.'))
s['recorded_utc']=NOW;save(P/'sourcefact-consumer-receptions.json',s)
f=json.loads((P/'io/recent-read-failures.json').read_text());old={x['tool_chunk'] for x in f['errors']}
for chunk,code,err,credit in [('623916',1,'cat PBS/shadow_pokemon.txt absent','Earlier complete ShadowPokemon_Other source read valid; absent PBS path has no read credit.'),('e8687e',1,'report-relative partner path from R cwd absent','Earlier Chamber source read valid; correct partner package subsequently read completely.'),('4ca2aa',2,'invalid Data/Scripts/006_Map* glob','Other valid search results retained; no absence conclusion from invalid glob.'),('f42037',2,'rg wrong Data/Scripts/006_Map objects/001_Game_Player.rb','Compiler fragment/Shedinja/wc/Pokedex search outputs valid; nonexistent Game_Player path no credit; actual earlier complete named methods separately preserved.')]:
 if chunk not in old:f['errors'].append(dict(tool_chunk=chunk,exit_code=code,stderr=err,credit=credit,execution_utc='UNRECORDED_PER_CALL'))
f['recorded_utc']=NOW;save(P/'io/recent-read-failures.json',f)
print(json.dumps(dict(utc=NOW,full_R=sum(x['repo']=='R' for x in l['own_full_reads']),full_F=sum(x['repo']=='B8' for x in l['own_full_reads']),partial_spans=len(l['own_partial_read_spans']),named_packages=len(s['named_contributions'])),ensure_ascii=False))
