import json,pathlib,subprocess,hashlib,datetime
V=pathlib.Path(__file__).resolve().parent;R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';B='fd1df570cad987dc3852a3b958f03916e317f7fe';NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
F=json.loads((V/'forward-mapping.json').read_text());REV=json.loads((V/'reverse-mapping.json').read_text());assert len(F['atoms'])==2122
rows=[
 ('B17-BATTLE','Battle469–472/Battler696–699','allOtherSideBattlers selects nonnil/nonfainted oppositeparitybattlers, acceptingindex-likeargument; NoVisualstargethelperthenonlysamplesindices, withnosuppliedtarget_datafilter.'),
 ('B17-BATTLE','Battle387–404','eachInTeamFromBattlerIndex yields nonnilpartyentrieswithinthecurrenttrainerstart/endrange; itdoesnotitselfexcludeeggs/faintedpartyentries.'),
 ('B17-BATTLE','Battle458–461,642–645','pbFindBattler onlyfindsnonfaintedsame-sidecurrentbattlerswithmatchingpokemonIndex, elsereturnsnil; NoVisualsreplacementpopulationusesitsabsence.'),
 ('B17-SWITCH','BattleSwitch113–128','PartyScreenconsumer passesproposedindexandscene to pbCanSwitchIn? forlaxcase orpbCanSwitch? otherwise, retriesfailingcandidate, optionallyregisters, thenacceptsretindex. Debugsceneonlyproposescandidates.'),
 ('B17-SWITCH','BattleSwitch9–34,76–90','Switchvalidation includesentry/owner/egg/fainted/currentbattler/duplicatependingchoice checks beforeoutgoing-switch predicate; item/ability/trappingcallbacksremainconditionalnamedsubcalls, notwholeeffectdomainapproval.')]
paths={'B17-BATTLE':'Data/Scripts/011_Battle/001_Battle/001_Battle.rb','B17-SWITCH':'Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb','B17-BATTLER':'Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb'}
def get(repo,c,p):return subprocess.check_output(['git','show',c+':'+p],cwd=repo)
def sid(repo,c,p):
 b=get(repo,c,p);return {'repo':repo,'commit':c,'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'blob':subprocess.check_output(['git','rev-parse',c+':'+p],cwd=repo,text=True).strip()}
for k,p in paths.items():F['source_identities'][k]=sid('/workspace/pokemon-essentials',R,p)
premise='FixeddefaultR/B8/noextraoverride; explicitdirecthelperorordinarymaincommandentryaslisted. Validinitializedbattlers/parties/trainerboundaryobjects/scene andnormalcalledprimitives; absentcanrequirevalidpositionsonlyforstatedbranch. No random/UI/native/battle execution. Callbackvalidation isnotallability/itemeffectsourceapproval.'
new=[]
for num,(source,unit,meaning) in enumerate(rows,2123):
 a={'id':f'FAC-A{num:04}','source':source,'unit_locator':unit,'assertion':meaning,'formal_receivers':['B17-PB034-other'],'premise':premise,'pending_dependencies':[],'status':'FINITE_STATIC_B17_HELPER_CONSUMER_RECEIVED','evidence':'SOURCE_STATIC','execution':'NOT_EXECUTED','reader':'/root/facility_atomic_completion_cloud'};new.append(a)
F['atoms'].extend(new);F['bounded_denominator']=len(F['atoms']);F['v2_increments'].append({'path':'B17-PB034-complete-child-reception.v2.json','count':5,'ids':[new[0]['id'],new[-1]['id']],'utc':NOW})
children=[
 ('direct','missing','Singularbattler.move readfails beforefirstcandidate rand/yield forvalidstandardBattler, absentaddedgetter.',[1811]),
 ('direct','consumer','Acceptingconsumerneverreceivesacandidateindexfromthatcall.',[1811]),
 ('direct','boundary','No randomlegalresult/wholegameexit/rollbackpromise followsfromthishelperfailure.',[1811,1789]),
 ('main','AI','Normalrealbranch controlPlayertrue dispatchesAIandbypassesthisdirecthelper.',[1784,1786]),
 ('main','scope','Directhelperfailuredoesnotproveordinarymainsimulationfailureoranygeneralsuccessguarantee.',[1789,1784]),
 ('other','bag','Uniformlegalrand15offset0 givesBag1/15.',[1810]),
 ('other','call','OnlynonBagbranchdrawsrand10; conditionalCall1/10 andoverall(14/15)*(1/10)=7/75.',[1810]),
 ('other','target','Targethelperignoresmove-specifictarget_data/visibleSprites andsamplesaliveoppositesideindices.',[1812,2123]),
 ('other','no-target','Emptytargetarrayreturns−1 before sample.',[1812]),
 ('other','party-population','Nonactivecandidatepositionscomefromtrainer-ownednonnilteamrangeandpbFindBattlerabsence; scenehasnogenerallegal-switchfilter.',[1813,2124,2125]),
 ('other','party-consumer','Callerchecksproposedcandidatewithswitchvalidators; rejectionallowsanotherproposal, up to50sceneattempts.',[1813,2126,2127]),
 ('other','no-party','No replacementcandidatesreturnsnilwithoutyield; BattlePartyScreenretremains−1.',[1813,2126])]
byid={a['id']:a for a in F['atoms']};cc=[]
for case,name,meaning,nums in children:
 refs=[f'FAC-A{i:04}' for i in nums];assert all(x in byid for x in refs);cid=f'FAC-B17-PB034-{case}-{name}';cc.append({'id':cid,'row':'B17-PB034-'+case,'meaning':meaning,'source_assertions':refs,'premise':premise,'status':'FINITE_STATIC_CHILD_RECEIVED'})
 for aid in refs:
  a=byid[aid];REV['mappings'].append({'formal_clause':cid,'atomic_assertion':aid,'meaning':meaning,'source':a['source'],'source_unit':a['unit_locator'],'premise':premise,'status':'FINITE_STATIC_CHILD_RECEIVED','pending_dependencies':[],'relation':'FINITE_COMPLETE_B17_PB034_CHILD'})
REV['true_bounded_assertions']=len(F['atoms']);REV['v2_new_exact_child_bindings']=len(REV['mappings'])-992
p='deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md';form=sid('/workspace/pokemon-essentials-clean-room',B,p);F['source_identities']['F17']=form;b=get(form['repo'],B,p).decode().splitlines();assert b[679].startswith('| B17-PB034-direct |') and b[681].startswith('| B17-PB034-other |')
units=[]
for key,ranges in [('B17-BATTLE',[(387,404),(458,472),(642,645)]),('B17-SWITCH',[(9,34),(38,70),(76,90),(113,135)]),('B17-BATTLER',[(696,699)])]:
 s=F['source_identities'][key];ss=get(s['repo'],R,s['path']).decode().splitlines(keepends=True)
 for lo,hi in ranges:units.append({'identity':s,'range':[lo,hi],'content':''.join(ss[lo-1:hi]),'actual_read':['3a23fe','70ad14','d6004c'],'qualification':'Complete namedunits only, no sourceFILE/domainFULL. Callbackpredicates retaintheir explicitconditionalpremises.'})
packet={'schema':'facility-B17-PB034-three-row-complete-finite-child-reception/v2','utc':NOW,'actual_reader':'/root/facility_atomic_completion_cloud','formal_identity':form,'full_three_rows':{'range':[680,682],'content':'\n'.join(b[679:682])+'\n','actual_full_read':'222e64 all3complete'},'source_assertions':new,'complete_necessary_supplemental_units':units,'explicit_children':cc,'summary':{'complete_finite_rows':3,'children':len(cc),'new_manual_source_assertions':5,'all_source_assertions':len(F['atoms']),'finite_bindings':len(REV['mappings'])},'actual_source_basis':['OwnwholeNoVisuals106 read34cb86 plus3a23fe repeated77–106','R22realbranchcompleteandCORE5commandfacts/3completeunitsactuallyreceived','DefaultBattlerpluralmovesdeclaration andfixedscript no-singulargetter/overridecensus previouslyactuallyread inR22increment','3a23fe/70ad14/d6004c namedfullhelpers'],'qualification':'Onlythese3completeB17rowsandnecessaryfinitehelpers. No allB17/wholeUI/AI/ability/item/domainapproval, sourceFILEFULLoractualsimulation/nativeexecution. Fractionsconditionaluniformoffsets, notmeasuredrandomquality. Thissupplementalcatalogdoesnotreducetheoriginal964seedcount.','OPEN':['RemainingSF/RC/PA/QC/WS964seeds/202externaljoins and453species649classes2732provenances/eligibilityproofqualification.','AllotherB17rows belongonlytheirnecessaryfinitecross-domaincontacts; thispacketdoesnotassertallB17coverage.'],'new_required':0,'new_optional':0,'new_contexts':0,'new_votes':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True,'wholeFAC_complete':False}
def save(n,x):(V/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
save('B17-PB034-complete-child-reception.v2.json',packet);save('forward-mapping.json',F);save('reverse-mapping.json',REV)
p=json.loads((V/'progress.json').read_text());p.update(updated_utc=NOW,manually_authored_finite_source_assertions=len(F['atoms']),source_to_formal_bindings=len(REV['mappings']),finite_new_child_bindings=len(REV['mappings'])-992,B17_PB034_finite={'rows':3,'children':len(cc)});save('progress.json',p)
a=json.loads((V/'atomic-denominator.json').read_text());a['updated_utc']=NOW;a['manual_bounded_source_assertions'].update(count=len(F['atoms']),id_end=new[-1]['id']);a['finite_reverse_bindings'].update(count=len(REV['mappings']),qualification=f"992historicalregion+{len(REV['mappings'])-992}explicitfinite source/audit/casechildroutes; notfullformaldenominator.");a['B17_PB034_finite']=packet['summary'];save('atomic-denominator.json',a)
l=json.loads((V/'reading-ledger.json').read_text());l['updated_utc']=NOW;l['v2_exact_receptions'].append({'utc':NOW,'path':'B17-PB034-complete-child-reception.v2.json','actual_reads':['222e64 all3formalrows','3a23fe','70ad14','d6004c'],'qualification':packet['qualification']});save('reading-ledger.json',l)
b=(V/'B17-PB034-complete-child-reception.v2.json').read_bytes();print('source',len(F['atoms']),'routes',len(REV['mappings']),'children',len(cc),'bytes',len(b),'sha',hashlib.sha256(b).hexdigest())
