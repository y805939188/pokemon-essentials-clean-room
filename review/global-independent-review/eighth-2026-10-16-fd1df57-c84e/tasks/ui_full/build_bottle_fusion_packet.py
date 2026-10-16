import json,hashlib,subprocess,datetime
from pathlib import Path
T=Path('review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/ui_full'); R=Path('/workspace/pokemon-essentials'); C=Path('/workspace/pokemon-essentials-clean-room')
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
specs=[
('R','Data/Scripts/013_Items/002_Item_Effects.rb',[[1122,1524]]),
('R','Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb',[[1,88],[315,390],[465,496]]),
('R','Data/Scripts/014_Pokemon/001_Pokemon.rb',[[145,250]]),
('R','Data/Scripts/013_Items/008_PokemonBag.rb',[[105,145]]),
('R','Data/Scripts/015_Trainers and player/001_Trainer.rb',[[75,140]]),
('R','Data/Scripts/013_Items/001_Item_Utilities.rb',[[696,780]]),
('R','Data/Scripts/010_Data/002_PBS data/009_Species_files.rb',[[1,140]]),
('R','PBS/pokemon.txt',[[16681,16707],[16755,16783],[18614,18643]]),
('R','PBS/pokemon_forms.txt',[[1460,1500],[1775,1795]]),
('R','PBS/items.txt',[[6400,6445]]),
('B','deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md',[[295,342]])]
sources=[]
for which,path,ranges in specs:
 repo=R if which=='R' else C
 raw=(repo/path).read_bytes(); tree='7589c800b61ba13a13040ed0d686979b80a84fd0' if which=='R' else '751dfde81048c81390f89a65ca1d1a565ba8e1ca'
 commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b' if which=='R' else 'fd1df570cad987dc3852a3b958f03916e317f7fe'
 blob=subprocess.check_output(['git','rev-parse',commit+':'+path],cwd=repo,text=True).strip()
 sources.append(dict(repo=str(repo),commit=commit,tree=tree,path=path,blob=blob,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),mode='100644',lines=len(raw.splitlines()),reader='/root/ui_full',status='PARTIAL_READ_COMPLETE_NAMED_UNITS',ranges=ranges,whole_file_read=False))
texts=[
('FORM-CALL','MultipleForms uses SpeciesHandlerHash; missing function returns nil, existing proc gets the actual pkmn and supplied arguments; it dispatches by pkmn.species.'),
('FORM-GET','Pokemon.form first returns nonnil forced_form including zero; in battle or storage returns stored @form; otherwise calls dynamic getForm and commits via ordinary self.form= only if result truthy and different.'),
('FORM-SET','Ordinary form= first writes stored form and clears cached ability; then onSetForm(value,old), calc_stats, player dex registration. It has no same-value guard.'),
('FORM-YIELD','setForm writes stored form and clears ability, yields caller block, then onSetForm(value,old), calc_stats and dex. The callback argument remains requested value even if nested reads changed stored form.'),
('HOOPA-GET','Hoopa getForm returns 0 when time_form_set nil, or current integer time strictly exceeds prior integer time plus259200; otherwise nil. Equality is not expiry.'),
('HOOPA-SET','Hoopa onSetForm requested form>0 writes current integer time; requested form<=0 clears time. It does not rewrite stored form.'),
('BOTTLE-GATE','PRISONBOTTLE handler rejects nonHoopa or fainted before change, chooses requested1 if current dynamic form0 else0.'),
('BOTTLE-YIELD','Handler setForm yields scene.pbRefresh then scene.pbDisplay(formchanged); normal completion returns true. Neither call is protected by ensure.'),
('SPRITE-READ','Species.sprite_bitmap_from_pokemon normalizes species, tests egg and reads actual pkmn.form before front/back bitmap request; icon_filename_from_pokemon and icon_bitmap_from_pokemon also read pkmn.form.'),
('SPRITE-ALTER','After bitmap request, an alterBitmap function gets a copied bitmap after original disposal, then each bitmap callback; no invented rollback if copy/dispose/alter fails.'),
('SPRITE-RESOLVE','check_graphic_file enumerates combinations: shiny subfolder, shadow, female, positive form and species/000 fallbacks; the generated filename request does not establish actual asset or pixels.'),
('BOTTLE-PRE','Bottles finite witness assumes default no plugin, Hoopa stored0/time nil/no forcedform, healthy/nonEgg/nonShadow/nonHyper/noMail, ordinary Party field context, registered data and required dependencies normal; current time within the subsequent three days.'),
('BOTTLE-FIRST','Initial dynamic form read returns0 equal stored0, so no self.form= commit and no timestamp write.'),
('BOTTLE-OUTER','Outer setForm(1) writes stored1 and abilitynil before yielding to refresh.'),
('BOTTLE-INNER','Refresh actual icon/bitmap form read sees timestamp stillnil; getForm returns0 differing stored1, so ordinary self.form=0 writes0, clearsability, onSetForm0 clearstime, recalculates and registers according to actual surrounding gates.'),
('BOTTLE-AFTER','After normal refresh and message, outer onSetForm still receives1 and writes integer time; it does not restore stored1. Outer remaining stats/dex sees actual stored0.'),
('BOTTLE-PARTY','Party item utility triggers handler, then clearsannotations and hardrefreshes before consumed_after_use deduction; key item bottle is not consumed. Final finite result stored0/newtime/bottlequantity1.'),
('BOTTLE-CONTROL-TIME','Ordinary control stored0 with existing current timestamp: initial getter returnsnil, outer setForm1 callback does not reset it to0; form1 remains and timestamp refreshed.'),
('BOTTLE-CONTROL-AFTER','A second successful use within period from stored0/newtime can remain1; a later request1→0 clears timestamp. Direct ordinary form=1 does not yield between storing1 and onSetForm, so differs from callback path.'),
('BOTTLE-FAILURE','A refresh or display/resource exception propagates with prior storedform/ability/time/stat/dex writes retained; no boolean success or final timestamp can be moved before their actual point.'),
('FUSE-GATE','DNASPLICERS usable requires Kyurem, fusednil and nonfainted. Cancel second choice negative returnsfalse before fusion.'),
('FUSE-SECOND','Second choice resolves current $player.party[chosen], rejects receiveritself, egg, fainted and nonReshiram/nonZekrom. Reshiram requestsform1, Zekrom2.'),
('FUSE-IDENTITY','Receiver pkmn was captured by original Party item session; after Box reentry second choice reads current party. The stored receiver object is not rebound from its original index.'),
('FUSE-CALLBACK','setForm requested value is written before callback; callback assigns pkmn.fused=selected actual object, calls remove_pokemon_at_index(chosen), hardrefresh then message.'),
('FUSE-REMOVE-IGNORED','remove_pokemon_at_index result is not inspected by fusion handler. Fused assignment precedes attempted removal.'),
('REMOVE-BOUNDS','Trainer removal returnsfalse for negative or index>=party_count before mutation.'),
('REMOVE-ABLE','Removal scans other indices for any able? member. With none returnsfalse and leaves party; with one delete_at(index) and true.'),
('FUSE-TOOL','After normal setForm callback/onSetForm/stat/dex return, bag.replace_item(usable,used) runs; its false return is also unchecked, then handlertrue.'),
('REPLACE-GUARDS','Bag.replace_item try_gets old/new identifiers, missing either false. It iterates OLD pocket and changes every matching slot id to new, returns whether any matched.'),
('REPLACE-POCKET','Replacement does not relocate to new item pocket or repair registered list; source declares same-pocket support. These default fusion tools both pocket8.'),
('UNFUSE-GATES','DNASPLICERSUSED requires Kyurem, nonnil fused, nonfainted and not full party; there is no exact current Kyurem form guard.'),
('UNFUSE-CALLBACK','setForm0 callback appends SAME fused object to party end, then clears fused, hardrefreshes and displays; after normal setForm completion used→usable replace runs and handlertrue.'),
('SOLAR','NSOLARIZER usable uses unfused healthy Necrozma and healthy nonEgg nonself Solgaleo partner, requestedform1, same unchecked removal/tool sequence. Used variant also requires receiver.form==1 before unfuse.'),
('LUNAR','NLUNARIZER usable substitutes Lunala/form2; used additionally requires receiver.form==2. Other callback ordering same.'),
('REINS','REINSOFUNITY usable uses unfused healthy Calyrex and Glastrierform1/Spectrierform2; used variant needs fused/nonfainted/notfull but no exact receiver form guard; same identity and unchecked returns.'),
('OTHER-ITEMS','Full1122–1524 also read Gracidea/Shaymin nonfrozen/day/form0, four Nectar Oricorio target0..3, RevealGlass healthy forces toggle0/1, Rotom sixchoices/current/cancel and Zygarde form/ability/cancel. These are separate finite definitions, not proof all callbacks/media succeed.'),
('KYUREM-ENTER','Kyurem onEnteringBattle maps forms1/2 to3/4; onLeavingBattle forms>=3 subtract2. These producers are not executed by ordinary field finite witness.'),
('KYUREM-ZERO','Kyurem onSetForm0 iterates ICEBURN/FREEZESHOCK to GLACIATE and FUSIONFLARE/BOLT to SCARYFACE when target registered; duplicate-known target clears slot, else rewritesid, then compacts.'),
('KYUREM-ONE-TWO','Requestedform1 maps existing GLACIATE→ICEBURN and SCARYFACE→FUSIONFLARE; form2→FREEZESHOCK/FUSIONBOLT, each only registered target and not already known.'),
('DATA-SPECIES','Complete default Reshiram/Kyurem/Hoopa records and Kyurem1–4/Hoopa1 form records were directly read including Moves/Tutor/Pokedex. Appended adjacent partial record has no complete-record credit.'),
('DATA-TOOLS','Complete PRISONBOTTLE/ROTOMCATALOG/ZYGARDECUBE/DNASPLICERS/DNASPLICERSUSED records each pocket8, price0, FieldUseOnPokemon and FlagsKeyItem; next NSOLARIZER header is not complete record credit.'),
('DATA-LEVEL5','Default Kyurem L5 move candidates are level1 DragonBreath/NobleRoar/AncientPower/FreezeDry; no GLACIATE or SCARYFACE. Their absence avoids these onSetForm1 move-mapping interactions in finite witness.'),
('FUSE-PRE','Finite WP28§5.6.2: defaultGen8, baseStorage, party[K,R], healthy unfused nonforced nonMail Kyurem0 and Reshiram0 level5, canstore, BoxLink three permission gates true, no FLY permission loss; usable1/used0 and box0slot0empty.'),
('FUSE-STORE','During second choice SPECIAL opens Storage mode0; store SAME captured K in box0slot0. Two able members permit storage, party compresses to[R]. Return retains old K identity.'),
('FUSE-CHOOSE','USE party0 selects SAME R, passes partner checks, KsetForm1 stores1 then callback sets fused=SAME R.'),
('FUSE-NOREMOVE','removeindex0 sees no other able member in now-singleton[R], returnsfalse; unchecked leaves[R]. Refresh/message/onSetForm finish normally under premises.'),
('FUSE-FINAL','Tool replace transforms usable1→0 and used0→1; handlertrue. SAME K is in boxform1 with fused reference to SAME R that remains actualparty0. No clone or partnerclear occurs.'),
('FUSE-CONTROL-NOREENTRY','Without Box reentry, party[K,R], removalR succeeds due to able K and normal result party[K], fusedR.'),
('FUSE-CONTROL-CANCEL','After storing K, BACK from second selection returnsfalse before fusion and tool replacement; party[R]/boxK side effects stay. BACK does not undo Storage.'),
('FUSE-CONTROL-GATE','With any BoxLink gate false, or FLY field return loses permission, or new Bag item session without permission, this reentry path is unavailable.'),
('FUSE-CONTROL-THIRD','With initial[K,R,A] and able A, after storingK current[R,A], removalR succeeds, current[A]. This is ordinary successful-removal control.'),
('FUSE-FAILURE','If callback message/resources, onSetForm/stats/dex or replace lookup fails, already stored form/fused/storage/party prefixes stay; final handlertrue and tool replacement are not guaranteed. No atomic rollback contract is inferred.'),
('FINITE-NOT-ALL','Reading handlers of other fusion families does not prove all partner-specific nested callbacks, later unfusion, battle ownership or save/reload alias behavior for every family. Those remain separately bounded.'),
('FORMAL-MATCH','WP28§5.6.1/5.6.2 currently state these finite callback/data witnesses and ordinary controls; this is finite support/closure of A10 two requested combinations, not a new discrepancy proposal.'),
('EXECUTION','Every fact is SOURCE_STATIC or derived conditional vector; actual render/native/Ruby/game/persistence execution count0 and UPDATE_NOT_STARTED.')]
facts=[{'id':f'UI-BF-{i:03}', 'topic':k, 'meaning':v} for i,(k,v) in enumerate(texts,1)]
wp66=json.loads((T.parent/'ui_wp66/forward-mapping.json').read_text())
peers=[u for u in wp66['units'] if u['id'] in ['P02','P07','P11','X04','X08','X21']]
d=dict(schema='gr8-ui-bottle-fusion-interface/v1',id='UI-BOTTLE-FUSION-01',reader='/root/ui_full',utc=now,scope='Complete finite WP28§5.6.1 and§5.6.2 callback/identity/defaultdata composition; no allfusionfamilies approval',sources=sources,facts=facts,manual_fact_count=len(facts),received_complete_peer_units=peers,peer_credit='ui_wp66113units446facts already fully received via wp66-reception.json; duplicated units remain peer source credit, not own FULL_READ',source_whole_file_credit=False,formal_read_scope='wp28 partial295–342 only; adjacent section boundary credit not whole WP28',business='NOT_EXECUTED',business_execution_count=0,update='UPDATE_NOT_STARTED',global_approval=False)
(T/'bottle-fusion-interface.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
# Add only current true partial read extents; no earlier ledger/snapshot rewrite.
deps=json.loads((T/'dependency-identities.json').read_text())
for rec in sources:
 if rec['repo']!=str(R):continue
 old=next((a for a in deps['records'] if a['path']==rec['path']),None)
 if old:
  if not old.get('whole_file_read'):
   old['ranges']=sorted({tuple(x) for x in old['ranges']+rec['ranges']})
   old['ranges']=[list(x) for x in old['ranges']]
   old['status']='PARTIAL_READ_COMPLETE_NAMED_UNITS'
 else:deps['records'].append(rec)
deps['utc']=now
(T/'dependency-identities.json').write_text(json.dumps(deps,ensure_ascii=False,indent=2)+'\n')
raw=(T/'bottle-fusion-interface.json').read_bytes();print(json.dumps(dict(path=str(T/'bottle-fusion-interface.json'),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),facts=len(facts),sources=len(sources)),ensure_ascii=False))
