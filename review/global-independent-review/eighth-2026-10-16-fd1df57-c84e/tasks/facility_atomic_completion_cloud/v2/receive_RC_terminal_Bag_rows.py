import pathlib,json,hashlib,subprocess,datetime,re
V=pathlib.Path(__file__).resolve().parent;R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';B='fd1df570cad987dc3852a3b958f03916e317f7fe';NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
F=json.loads((V/'forward-mapping.json').read_text());REV=json.loads((V/'reverse-mapping.json').read_text());N=json.loads((V/'next-dispatch.json').read_text());assert len(F['atoms'])==2133
provider=json.loads((V/'core-terminal-skill-playback-binding.source.exact.json').read_text());facts=[x for x in provider['facts'] if x['id'] in ['CAR-FAC-BIND-01','CAR-FAC-BIND-04','CAR-FAC-BIND-05']];wanted=set(x for f in facts for x in f['units']);provided_units=[u for u in provider['source_units'] if u['id'] in wanted]
def get(p):return subprocess.check_output(['git','show',R+':'+p],cwd='/workspace/pokemon-essentials')
def sid(p):
 b=get(p);return {'repo':'/workspace/pokemon-essentials','commit':R,'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'blob':subprocess.check_output(['git','rev-parse',R+':'+p],cwd='/workspace/pokemon-essentials',text=True).strip()}
for k,p in [('RC-BAG','Data/Scripts/013_Items/008_PokemonBag.rb'),('RC-DEX','Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb'),('RC-FORMHANDLERS','Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb')]:F['source_identities'][k]=sid(p)
prim=[]
for p,keys in [('PBS/pokemon.txt',['BURMY']),('PBS/pokemon_forms.txt',['BURMY,1','BURMY,2']),('PBS/items.txt',['POTION'])]:
 b=get(p);ss=b.decode('utf-8-sig').splitlines(keepends=True);ix=[i for i,t in enumerate(ss) if re.fullmatch(r'\[.+\]\s*',t)];rr=[]
 for i,n in enumerate(ix):
  name=ss[n].strip()[1:-1]
  if name in keys:
   z=ix[i+1] if i+1<len(ix) else len(ss);rr.append({'id':name,'ordinal':i+1,'range':[n+1,z],'complete_raw_body':''.join(ss[n:z]),'actual_full_read':'c504d4' if p!='PBS/items.txt' else '236fe8'})
 assert len(rr)==len(keys);prim.append({'identity':sid(p),'complete_records':rr})
F['source_identities']['RC-BURMY-PBS']=prim[0]['identity'];F['source_identities']['RC-BURMY-FORMS']=prim[1]['identity'];F['source_identities']['RC-POTION-PBS']=prim[2]['identity']
manual=[
 ('RC-FORMHANDLERS','CAR-FAC-BIND-01/BURMYcompletehandler','BURMYgetFormOnLeavingBattle returnsnil unlessendBattle&&used; qualifiedCave/Rock/Sand→1,None→2,else0. Mereordinaryswitch/faintdoesnotpassendBattle.'),
 ('B17-BATTLE','CAR-FAC-BIND-04/send_out','NormalSendOut writesusedInBattle[slot&1][slot/2], whereasnormalEndPeerreadsusedInBattle[0][partyindex]. Partyindex1onlyswappedintoslot0doesnotwriteflag1.'),
 ('S01','Pokemon159–166/COREnormal_end+peer_leave','NormalterminalPeer onplayerpartyPokemon receivesactualparty-indexflag,endBattletrue; differingtruthyform setsPokemon.form, capsHPifneeded, thenleavingcallback. Formsetterwritesstoredform/clearsabilityvalue/callback/calcstats thenregisterscurrentglobalplayerPokedex.'),
 ('RC-DEX','Pokedex195–219','Pokedex.register(Pokemon) resolvescurrentSpeciesdata/gender/shiny, canonicalPokedexForm andnonemptyFormName beforewritingseen/seen_forms andoptionalinitiallastseen, thenrefresh. Priorseenwritesarenotrolledbackiflaterrefreshfails.'),
 ('RC-BURMY-FORMS','BURMY1/2completePBS+formvalidator448–485+Speciesconstructor175–221','DefaultBURMYforms1/2haveSandyCloak/TrashCloak names; normalformcompilerassignsIDsBURMY_1/2andform1/2, inheritsmissingbasefields, andabsentPokedexFormdefaultsform. Form1thereforedoesnotcollapseform0atDexregistration.'),
 ('RC-BAG','PokemonBag103–109','CurrentPokemonBag.remove(item,qty1) resolvesItem.try_get, returnsfalseifunknown, thenusesitscurrentpocketarrayandcanonicalID inItemStorageHelper.remove.'),
 ('RC-BAG','ItemStorageHelper.remove283–300','Helperremove1decrementsmatchingpocketquantityby1, deletesemptyzero-slotandcompacts, returnstrueif1removed; withnoitemreturnsfalsewithoutquantitydecrement. Partialdeletionsforlargerrequestsarenottransactional.'),
 ('RC-POTION-PBS','POTION2942–2951/Itemconstructor+consumed_after_use','POTIONcompleteprimaryrecordhasFieldUse/BattleUseOnPokemon,pocket2,FlagsFling_30, andnoConsumable/key/machineflag. NormalItemconstructor givesconsumabletrue andconsumed_after_use?true; descriptiondoesnotproveallbattlehealinghandlers.'),
 ('R05','CAR-FAC-BIND-05/PlaybackBAG→BaseRegisterItem','PlaybackBAGcallsbaseRegisterItem: actualUseItemchoiceiswrittenbeforeconsumebag. Player-ownedconsumeditemusescurrent$bag.remove; falsecausesraiseafterchoicewrite. Nil/registerednonconsumeditemskipremoval; noplayerBagrestoreexistsinrecordproperties.')]
premise='FixeddefaultR/B8/nooverride; actualfullrowfixture, validdefaultBURMYformrecords/noforcedformoverride/current$playerandPokedex/currentBagpockets/itemregistry, normalprecedingbattle/Peer/form/calcstats/callbacks whereoutputspecified. Slot0/party0vs1 flagsasstated, noconfoundingentry/flagmutation. Playbackpartycopyisvalidserializerpremise; noactualMarshal/playback/save/nativeexecution. COREoriginalFULLreaderpreserved; onlycompletefacts/unitsreceived.'
new=[]
for num,(s,u,m) in enumerate(manual,2134):
 a={'id':f'FAC-A{num:04}','source':s,'unit_locator':u,'assertion':m,'formal_receivers':['RC-W22/W22b/W23'],'premise':premise,'pending_dependencies':[],'status':'FINITE_STATIC_TERMINAL_BAG_PRODUCER_RECEIVED','evidence':'SOURCE_STATIC_PLUS_COMPLETE_CORE_FINITE_FACTS','execution':'NOT_EXECUTED','reader':'/root/facility_atomic_completion_cloud','original_provider_reader':'/root/core_atomic_reception'};new.append(a)
F['atoms'].extend(new);F['bounded_denominator']=len(F['atoms']);F['v2_increments'].append({'path':'RC-terminal-Bag-three-row-reception.v2.json','count':9,'ids':[new[0]['id'],new[-1]['id']],'utc':NOW})
children=[]
def c(case,name,meaning,nums):children.append({'id':f'FAC-RC-{case}-{name}','case':case,'meaning':meaning,'source_assertions':[f'FAC-A{i:04}' for i in nums],'premise':premise,'status':'FINITE_STATIC_CHILD_RECEIVED'})
c('W22','copy','RestoredpartygraphisindependentoforiginalpartyundernormalMarshalfixture; globalplayerDexisnotisolated.',[1427,1429,2136])
c('W22','flag','Partyindex0inslot0sendoutwritesflag0true, terminalreadsflag0true.',[2135])
c('W22','gates','endBattletrue+actualusedflagtruepassesBURMYleavinggate.',[2134])
c('W22','cave','Cavehandlerreturns1whichdiffersfromold0, soPeerappliesform1.',[2134,2136])
c('W22','dex','Formsetterdirectlyregistersto liveglobalplayerDex; defaultform1name/PokedexFormkeepseenform1.',[2136,2137,2138])
c('W22b','write-index','Partyindex1onlyenteredslot0writespositionflag0, notflag1.',[2135])
c('W22b','read-index','Terminalpartyiterationreadsindex1flagfalse, despiteactualparticipation.',[2135])
c('W22b','no-change','BURMYusedgatefails; noform1assignment, oldform0remains.',[2134,2136])
c('W22b','no-dex1','Thisfailedgateaddsnoform1Pokedexregistration; actualparticipationcannotreplaceflagprecondition.',[2134,2136,2137])
c('W23','dispatch','Player-ownedrecordedBAGslotpassesrecorditem/target/moveintobaseRegisterItem.',[1501,2142])
c('W23','potion','NormalPOTIONregistereddataisconsumed_after_use?true, independentofEnglishdescription.',[2141])
c('W23','present','CurrentBagcontaining≥1ofthisitemloses1uponregistration.',[2139,2140,2142])
c('W23','absent','CurrentBagwithoutitemreturnsfalseandbaseconsumptionraisesafteractualchoicewrite.',[2139,2140,2142])
c('W23','nil','NilitemshortcircuitsbeforeBagremoval.',[2142])
c('W23','nonconsumed','RegisterednonconsumeditemshortcircuitsbeforeBagremoval.',[2142])
c('W23','menu','FacilityitemmenurejectiondoesnotrevalidateorrejectdirectplaybackBAGcommand.',[1421,1501,2142])
byid={a['id']:a for a in F['atoms']}
for ch in children:
 assert all(x in byid for x in ch['source_assertions'])
 for aid in ch['source_assertions']:
  a=byid[aid];REV['mappings'].append({'formal_clause':ch['id'],'atomic_assertion':aid,'meaning':ch['meaning'],'source':a['source'],'source_unit':a['unit_locator'],'premise':premise,'status':ch['status'],'pending_dependencies':[],'relation':'COMPLETE_RC_TERMINAL_BAG_CHILD'})
REV['true_bounded_assertions']=len(F['atoms']);REV['v2_new_exact_child_bindings']=len(REV['mappings'])-992
s=F['source_identities']['F07'];bb=subprocess.check_output(['git','show',B+':'+s['path']],cwd=s['repo']).decode().splitlines();groups=[]
for case in ['W22','W22b','W23']:
 hit=[(i,t) for i,t in enumerate(bb,1) if i>=156 and t.startswith('| '+case+' |')];assert len(hit)==1;line,text=hit[0];old=f'F07-L{line:04}';h=[x for x in N['unmet_formal_seed_structures'] if x['old_locator_id']==old];assert len(h)==1;N['unmet_formal_seed_structures'].remove(h[0]);child=[x['id'] for x in children if x['case']==case];N['closed_finite_formal_seed_structures'].append(dict(h[0],case='RC-'+case,children=child,status='FINITE_STATIC_CHILD_RECEPTION_COMPLETE',receipt='RC-terminal-Bag-three-row-reception.v2.json'));groups.append({'case':case,'old_locator_id':old,'line':line,'complete_original_row':text,'children':child})
assert len(N['unmet_formal_seed_structures'])==947
units=[]
for key,ranges in [('RC-BAG',[(103,109),(237,301)]),('RC-DEX',[(195,219)]),('S01',[(113,115),(147,166)]),('GEN-COMPILE',[(292,330),(448,485)]),('RC-FORMHANDLERS',[(4,35)])]:
 st=F['source_identities'][key];ss=get(st['path']).decode().splitlines(keepends=True)
 for lo,hi in ranges:units.append({'identity':st,'range':[lo,hi],'content':''.join(ss[lo-1:hi]),'actual_read':['35b995','217de0','c504d4','0712e8','e07358','1d2b35','075252'],'qualification':'Namedcompleteunitonly; nowholeBag/Dex/FormHandlers/Compiler/Pokemondomaincredit. Runtimecurrentreceiverandnormalcallbackpremisesretained.'})
packet={'schema':'facility-RC-terminal-Bag-three-row-complete-finite-reception/v2','utc':NOW,'actual_reader':'/root/facility_atomic_completion_cloud','formal_identity':s,'common_premise':premise,'rows':groups,'explicit_children':children,'new_source_assertions':new,'complete_primary_records':prim,'complete_additional_units':units,'original_CORE_finite_contribution':{'path':'core-terminal-skill-playback-binding.source.exact.json','bytes':64730,'sha256':'ffca5443085544fcd4b07eb27c6778008db67ddaded4aa6abe3bb1acbac9f156','complete_selected_facts':facts,'complete_selected_source_units':provided_units,'complete_common_premises':provider['common_premises'],'actual_full_fact_and_units_read':'Priorwhole64730Breceptionb65a21/228508/074d57; e34274repeatedwholeF01/F04/F05. OriginalreaderCORE; sourceFULLnottransferred.'},'counts':{'new_complete_RC_rows':3,'new_case_children':len(children),'total_RC_complete_rows':17,'total_RC_children':55,'all_manual_source_assertions':len(F['atoms']),'finite_reverse_bindings':len(REV['mappings']),'remaining_original_seed_structures':947},'qualification':'Complete3rowinput/expectedchildmeaningsreceivedwithcurrentliveglobalDex/Bagandactualflagindexdistinctions. ValidBURMYbase+2forms/POTIONallrawfieldssourceactuallyread; compiledefinitionsstaticonly. DoesnotinferallDex/Bag/item/MultipleForms/formcallbacks orproofallnativeplaybacksafe.','OPEN':['Other12RCrows andallremainingSF/PA/QC/WS947seedstructures/202external','453species649classes2732provenance/completeeligibilityproofqualification/allmachineItemprimaryinputs'],'new_required':0,'new_optional':0,'new_contexts':0,'new_votes':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True,'wholeFAC_complete':False}
def save(n,d):(V/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
save('RC-terminal-Bag-three-row-reception.v2.json',packet);save('forward-mapping.json',F);save('reverse-mapping.json',REV);N['updated_utc']=NOW;save('next-dispatch.json',N)
p=json.loads((V/'progress.json').read_text());p.update(updated_utc=NOW,manually_authored_finite_source_assertions=len(F['atoms']),source_to_formal_bindings=len(REV['mappings']),finite_new_child_bindings=len(REV['mappings'])-992,original_formal_seed_locators_still_unexhausted=947,new_RC_exact_case_children=55,new_RC_exact_rows=17);save('progress.json',p)
a=json.loads((V/'atomic-denominator.json').read_text());a['updated_utc']=NOW;a['manual_bounded_source_assertions'].update(count=len(F['atoms']),id_end=new[-1]['id']);a['finite_reverse_bindings'].update(count=len(REV['mappings']));a['full_original_atomic_denominator']['unmet_original_paragraph_table_locators']=947;a['RC_terminal_Bag_finite']=packet['counts'];save('atomic-denominator.json',a)
l=json.loads((V/'reading-ledger.json').read_text());l['updated_utc']=NOW;l['v2_exact_receptions'].append({'utc':NOW,'path':'RC-terminal-Bag-three-row-reception.v2.json','actual_read':['e34274','0712e8','c504d4','e07358','1d2b35','236fe8','35b995','217de0','075252'],'qualification':packet['qualification']});save('reading-ledger.json',l)
b=(V/'RC-terminal-Bag-three-row-reception.v2.json').read_bytes();print('source',len(F['atoms']),'routes',len(REV['mappings']),'rows',3,'children',len(children),'remainingseeds',947,'bytes',len(b),'sha',hashlib.sha256(b).hexdigest())
