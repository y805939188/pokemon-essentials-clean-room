import json,hashlib,datetime
from pathlib import Path
P=Path(__file__).parent;utc=datetime.datetime.now(datetime.timezone.utc).isoformat();parent=P/'evolution-catalog79-meaning.v1.json';pd=json.loads(parent.read_text());packs={};bindings={};extras=[];byid={u['id'] for u in pd['selected_source_units']};joins={}
names={'W':'wp31-wrappers-commit-meaning.v1.json','R':'wp31-registry-meaning-atoms.v1.json','X':'wp32-context-meaning.v1.json','B':'battle-consumer-delta.v1.json'}
for a,n in names.items():
 raw=(P/n).read_bytes();d=json.loads(raw);us=d.get('whole_source_units',d.get('complete_source_units',d.get('source_units',[])));packs[a]={u['id']:u for u in us};bindings[a]=dict(path=n,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def ref(v):
 if '@' not in v:assert v in byid;return v
 a,n=v.split('@',1);u=packs[a][n];full=names[a]+'/'+n
 if full not in byid:
  d=json.loads((P/names[a]).read_text());row=dict(u,id=full,original_packet=names[a]);key=u.get('source_identity_key');row['original_source_identity']=d.get('source_identities',{}).get(key,u.get('identity'));extras.append(row);byid.add(full)
 return full
def J(v,*refs):joins[v]=[ref(x) for x in refs]
J('BE01','R@C31-REG-Level','W@pokemon:check_evolution_internal','W@utilities:pbChangeLevel','W@ui:pbEvolutionSuccess')
J('BE02','R@C31-REG-Level','W@pokemon:check_evolution_internal')
J('BE03','R@C31-REG-Silcoon');J('BE04','R@C31-REG-Cascoon');J('BE05','R@C31-REG-AttackGreater','R@C31-REG-AtkDefEqual')
J('BE06','R@C31-REG-Item','W@pokemon:check_evolution_on_use_item')
for v in ['BE07','BE10']:J(v,'W@pokemon:check_evolution_internal')
J('BE08','W@pokemon:check_evolution_internal','W@effects:EvolutionStones','W@effects:RareCandy')
J('BE09','W@pokemon:check_evolution_internal','W@effects:EvolutionStones','W@utilities:pbUseItem')
J('BE11','W@ui:pbEvolution','W@utilities:pbChangeLevel','W@utilities:pbLearnMove')
J('BE12','W@effects:EvolutionStones','X@trade:pbEndScreen:0','W@ui:pbEvolution')
for v in ['BE13','BE14']:J(v,'W@effects:RareCandy','W@utilities:pbUseItem','W@utilities:pbUseItemOnPokemon')
J('BE15','R@C31-REG-Happiness','W@effects:RareCandy')
J('BE16','W@ui:pbEvolutionSuccess','W@pokemon:action_after_evolution')
J('BE17','W@ui:pbEvolutionSuccess','pokemon:getMoveList','W@utilities:pbLearnMove')
J('BE18','W@ui:pbEvolutionSuccess','W@utilities:pbLearnMove')
J('BE19','W@pokemon:species=');J('BE20','W@pokemon:species=','pokemon:gender','pokemon:singleGendered?');J('BE21','W@ui:pbEvolution')
for v in ['BE22','BE23','BE24']:J(v,'R@C31-REG-Ninjask','R@C31-REG-Shedinja','W@ui:self.pbDuplicatePokemon','W@pokemon:clone','W@ui:pbEvolutionSuccess')
J('BE25','R@C31-REG-HoldItem','W@pokemon:action_after_evolution')
J('BE26','B@world:pbEvolutionCheck','W@ui:pbEvolutionSuccess','X@pokemon:hp=:0')
J('BE27','B@world:event:evolve_and_black_out','B@world:pbEvolutionCheck')
J('BE28','B@world:pbEvolutionCheck','W@ui:pbEvolution')
J('BE29','R@C31-REG-EventAfterDamageTaken','B@world:pbEvolutionCheck','W@pokemon:trigger_event_evolution','W@ui:pbEvolutionSuccess')
J('BE30','X@evolution:pbEvolutionEvent:0','X@trainer:able_party:0')
J('BE31','X@evolution:pbEvolutionEvent:0','R@C31-REG-Event','W@pokemon:trigger_event_evolution')
J('BE32','W@pokemon:trigger_event_evolution','W@ui:pbEvolution');J('BE33','R@C31-REG-Event','R@C31-REG-EventAfterDamageTaken');J('BE34','W@species:get_evolutions')
J('BE35','R@C31-REG-TradeItem','X@trade:pbEndScreen:0','W@ui:pbEvolutionSuccess')
for v in ['BE36','BE37']:J(v,'W@ui:pbStartScreen','W@ui:set_up_animation','W@ui:pbEvolution','W@ui:pbFlashInOut','picture:WHOLE','ruby:lerp')
J('CX01','X@time:self.isDay?:0','X@time:self.isNight?:0','X@time:self.isMorning?:0','X@time:self.isAfternoon?:0','X@time:self.isEvening?:0')
J('CX02','X@time:pbGetTimeNow:0','W@ui:pbEvolutionSuccess')
J('CX03','X@evolution:REG:LevelRain','X@screen:weather:0');J('CX04','X@evolution:REG:LevelRain','X@evolution:REG:LevelNoWeather');J('CX05','X@evolution:REG:LocationFlag','X@metadata:has_flag?:0')
J('CX06','X@evolution:REG:LocationFlag','X@evolution:REG:Region');J('CX07','X@evolution:REG:Region','X@evolution:REG:Location');J('CX08','X@evolution:REG:LevelDarkInParty','X@trainer:pokemon_party:0')
J('CX09','B@world:event:record_party_status')
J('CX10','B@usage:pbHitEffectivenessMessages','B@usemove:pbProcessMoveHit');J('CX11','B@usage:pbHitEffectivenessMessages')
J('CX12','B@usage:pbRecordDamageLost','B@usemove:pbProcessMoveHit');J('CX13','B@usemove:pbConfusionDamage','B@usage:pbRecordDamageLost');J('CX14','B@usage:pbReduceDamage','B@usage:pbRecordDamageLost','B@change:pbFaint')
J('CX15','B@change:pbFaint','X@pokemon:hp=:0');J('CX16','B@usage:pbRecordDamageLost','X@pokemon:heal:0','B@change:pbFaint');J('CX17','B@world:event:record_party_status','B@world:event:evolve_and_black_out')
for v in ['CX18','CX19']:J(v,'B@world:event:evolve_and_black_out','B@world:pbEvolutionCheck','B@world:after_battle')
J('CX20','B@world:after_battle','B@world:pbEvolutionCheck');J('CX21','B@world:pbEvolutionCheck','W@ui:pbEvolution','B@world:event:evolve_and_black_out')
for v in ['CX22','CX23','CX24','CX39']:J(v,'X@catch:pbStorePokemon:0','X@catch:pbRecordAndStoreCaughtPokemon:0','B@world:pbEvolutionCheck')
J('CX25','W@pokemon:check_evolution_internal','R@C31-REG-EventAfterDamageTaken')
for v in ['CX26','CX27']:J(v,'W@pokemon:trigger_event_evolution','R@C31-REG-EventAfterDamageTaken','W@ui:pbEvolution')
J('CX28','X@evolution:pbEvolutionEvent:0','W@pokemon:trigger_event_evolution');J('CX29','X@evolution:pbEvolutionEvent:0','X@trainer:able_party:0','W@pokemon:trigger_event_evolution','W@pokemon:check_evolution_internal')
J('CX30','R@C31-REG-TradeItem','X@trade:pbStartTrade:0','X@trade:pbEndScreen:0','W@ui:pbEvolutionSuccess')
for v in ['CX31','CX32']:J(v,'R@C31-REG-TradeSpecies','X@trade:pbStartTrade:0','X@trade:pbEndScreen:0')
J('CX33','W@pokemon:check_evolution_internal','X@trade:pbStartTrade:0')
J('CX34','X@party:pbChooseTradablePokemon:1','X@party:pbChoosePokemonForTrade:0','X@trade:pbStartTrade:0','X@trade:pbEndScreen:0')
J('CX35','X@trade:pbTrade:0','X@trade:pbEndScreen:0','X@trade:pbStartTrade:0','X@sprite:pbDisposeSpriteHash:0','X@message:pbDisposeMessageWindow:0')
J('CX36','storage:pbStoreCaught','storage:pbMoveCaughtToBox','storage:pbCopy','X@pokemon:heal:0')
J('CX37','R@C31-REG-Shedinja','W@ui:self.pbDuplicatePokemon','X@evolution:REG:HasInParty','B@world:pbEvolutionCheck')
J('CX38','B@world:pbEvolutionCheck','B@world:event:evolve_and_black_out')
for v in ['CX40','CX41','CX42']:J(v,'B@world:set_up_player_trainers','B@world:partner_can_participate?','X@catch:pbStorePokemon:0','B@startend:pbEndOfBattle','B@world:pbEvolutionCheck')
assert set(joins)=={r['vector'] for r in pd['records']}
parent_indexes={r['vector']:i for i,r in enumerate(pd['records'])}
out=dict(schema='gr8-cre-c-evolution-catalog79-exact-joins/v1',recorded_utc=utc,actual_reader='/root/creature_a_atomic_reception',mandatory_parent=dict(path=parent.name,bytes=len(parent.read_bytes()),sha256=hashlib.sha256(parent.read_bytes()).hexdigest()),meaning_qualification='This companion makes each manualvector producer/caller/receiver whole-unit binding explicit. Parent meanings/claims and exact original bytes unchanged; no new behavioral finding, sourceFULL, atom or vote.',complete_source_packet_bindings=bindings,exact_vector_sourceunit_joins=[dict(vector=v,parent_record_pointer='/records/'+str(parent_indexes[v]),complete_source_unit_ids=joins[v],complete_raw_record_ids=['pbs_species:IVYSAUR','pbs_species:VENUSAUR','pbs_move:PETALBLIZZARD'] if v=='BE17' else [],source_credit='All original units personally read in this same actualcontext; no implicit receiver readback.',remaining='Unstated modifiers/host/wholePBS/currentcatalog neighbors not approved.') for v in joins],additional_complete_source_units=extras,new_atoms=0,new_votes=0,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED')
f=P/'evolution-catalog79-exact-sourceunit-joins.v1.json';assert not f.exists();f.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');raw=f.read_bytes();print(json.dumps(dict(utc=utc,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),vectors=len(joins),additional_source_units=len(extras),new_atoms=0)))
