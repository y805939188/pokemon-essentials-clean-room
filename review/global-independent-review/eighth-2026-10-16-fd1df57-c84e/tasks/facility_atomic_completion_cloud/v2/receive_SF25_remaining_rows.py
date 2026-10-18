import pathlib,json,hashlib,subprocess,datetime,copy
V=pathlib.Path(__file__).resolve().parent
RR=V.parents[2]
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
UTC=datetime.datetime.now(datetime.timezone.utc).isoformat()
def load(n):return json.loads((V/n).read_text())
def save(n,o):(V/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def sha(b):return hashlib.sha256(b).hexdigest()
F=load('forward-mapping.json');REV=load('reverse-mapping.json');N=load('next-dispatch.json')
assert len(F['atoms'])==2287
provider=RR/'tasks/kernel_atomic_reception/maptransition-contest-micro-contribution.v1.json'
raw=provider.read_bytes();assert len(raw)==47166 and sha(raw)=='6ddb1bcf9cd5a9a888d87bdfdade167f53620622a85d309eb1999ef0be82f19f'
D=json.loads(raw)
selected_units=copy.deepcopy(D['source_units'][1:8])
selected_paths={u['path'] for u in selected_units}
identities=[copy.deepcopy(i) for i in D['source_identities'] if i['path'] in selected_paths]
checks=[]
def blob(p):return subprocess.check_output(['git','-C','/workspace/pokemon-essentials','show',R+':'+p])
for i in identities:
 b=blob(i['path']);gb=subprocess.check_output(['git','-C','/workspace/pokemon-essentials','rev-parse',R+':'+i['path']]).decode().strip()
 assert len(b)==i['bytes'] and sha(b)==i['sha256'] and gb==i['git_blob'] and i['fixed_R']==R
 checks.append({'path':i['path'],'parent_bytes_sha_blob_exact':True})
for u in selected_units:
 b=blob(u['path']);lo,hi=u['range'];t='\n'.join(b.decode().splitlines()[lo-1:hi])
 assert u['text'] in [t,t+'\n'] and sha(b)==u['source_sha256']
 checks.append({'path':u['path'],'range':u['range'],'complete_unit_text_exact_allow_container_final_LF':True})
selected={'schema':'FAC-actual-finite-provider-selection/v2','utc':UTC,'original':{'path':str(provider.relative_to(RR)),'bytes':len(raw),'sha256':sha(raw)},'original_reader':D['actual_reader'],'receiving_reader':'/root/facility_atomic_completion_cloud','common_premise':D['manual_package']['common_premise'],'facts':D['manual_package']['facts'][1:7],'source_identities':identities,'source_units':selected_units,'persistence':D['manual_package']['persistence'],'business_execution':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED','unadopted':['KAR-MC-F01','source_units/0 whole MapTransition138','source_units/8 Settings372–379','all source FULL ownership belonging to original reader; no whole messages/events/Settings domain transfer']}
save('kernel-contest-micro-selected-source.v2.json',selected)
sb=(V/'kernel-contest-micro-selected-source.v2.json').read_bytes()
receipt={'schema':'FAC-finite-complete-provider-reception/v2','utc':UTC,'actual_reader':'/root/facility_atomic_completion_cloud','selection_bytes':len(sb),'selection_sha256':sha(sb),'original':selected['original'],'facts_received':[f['id'] for f in selected['facts']],'whole_selected_facts_units_envelope_received':True,'actual_reads':['19e2ca complete original envelope and all7facts, onlyF02–07adopted','c13499 all8identities and completeunits2–7','2389a1 allunits2–7 fresh repeat','11ea60/f6dc96 own whole Contest441 identical unit1; no inheritance of sourceFULL'],'identity_unit_checks':checks,'unadopted':selected['unadopted'],'qualification':'Only named six complete facts and seven complete units with common premises/failure/open fields. Actual pause caller independently read5eedee. Native clock/graphics/messages/UI behavior and general event domain remain OPEN. No whole original47166 package or MapTransition reception.','new_required_optional_contexts_votes':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
save('kernel-contest-micro-reception.v2.json',receipt)

premise=('Fixed R/B8/no override. SOURCE_STATIC and DERIVED_VECTOR only; valid typed player/global/session/registry/storage/scene objects, valid judge-map configuration and normal dependencies returning without unrelated mutation unless a named case explicitly tests failure. '
 'Positive bounded integer RNG produces legal offset as explicitly assumed by WP06; distinct-opponent loop completion is conditional, not a bounded termination or native distribution proof. '
 'Normal successful nickname/store and rendering are conditional source paths, not executed UI/native/file behavior. Each child retains earlier effects on failure and has no rollback guarantee. '
 'Changing Settings in a configuration case means that configuration is in force when its actual consumer reads it: Safari runtime Start versus Contest class-load TIME_ALLOWED capture. '
 'No inner save compatibility, Demo reachability, whole external domain or native Ruby/Array/clock/graphics behavior acceptance.')
unit_specs=[
 ('S21',None,48,72,'Complete pause command loop'),
 ('S21',None,254,272,'Complete dedicated Save menu registration'),
 ('S14',None,306,348,'Complete after_battle and set_outcome methods'),
 ('SF-STEP','Data/Scripts/012_Overworld/001_Overworld.rb',172,187,'Complete ordinary player-step dispatcher'),
 ('SF-CAPACITY',None,4,43,'Complete joint capacity, nickname and final-store helpers'),
 ('SF-STORAGE','Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb',1,53,'Whole PokemonBox class'),
 ('SF-STORAGE',None,120,146,'Complete party/max/full methods'),
 ('SF-STORAGE',None,159,176,'Complete storage accessors'),
 ('SF-STORAGE',None,231,252,'Complete storage caught acceptance'),
 ('REC-TRAINER',None,65,83,'Complete party-count and capacity methods'),
 ('SF-POKEMON','Data/Scripts/014_Pokemon/001_Pokemon.rb',682,685,'Complete first-move recording'),
 ('SF-POKEMON',None,702,704,'Complete first-move clear'),
 ('SF-POKEMON',None,89,89,'IV limit declaration'),
 ('R12',None,1,196,'Whole Safari state/callers'),
 ('R18',None,1,441,'Whole Contest state/callers'),
 ('R02',None,1,83,'Whole Contest battle class/scene extensions'),
 ('S26',None,68,141,'Complete Safari/Contest debug registration'),
]
units=[]
for sid,p,lo,hi,name in unit_specs:
 if p is None:p=F['source_identities'][sid]['path']
 b=blob(p);identity={'repo':'/workspace/pokemon-essentials','commit':R,'path':p,'bytes':len(b),'sha256':sha(b),'blob':subprocess.check_output(['git','-C','/workspace/pokemon-essentials','rev-parse',R+':'+p]).decode().strip()}
 if sid in F['source_identities']:assert F['source_identities'][sid]['sha256']==identity['sha256']
 else:F['source_identities'][sid]=identity
 units.append({'source':sid,'identity':identity,'range':[lo,hi],'name':name,'text':'\n'.join(b.decode().splitlines()[lo-1:hi]),'qualification':'Complete named units/declaration. Only R12/R18/R02 already own whole source; no whole Storage/Utilities/World/Pokemon domain credit.'})
micro_sources={}
for i in identities:
 sid='SF-MICRO-'+str(len(micro_sources)+1)
 F['source_identities'][sid]={'repo':'/workspace/pokemon-essentials','commit':R,'path':i['path'],'bytes':i['bytes'],'sha256':i['sha256'],'blob':i['git_blob']}
 micro_sources[i['path']]=sid
new=[];labels={}
def add(label,sid,unit,text,receiver='F06/F08SF'):
 aid=f'FAC-A{len(F["atoms"])+len(new)+1:04}'
 a={'id':aid,'source':sid,'unit_locator':unit,'assertion':text,'formal_receivers':[receiver],'premise':premise,'pending_dependencies':[],'status':'FINITE_STATIC_SF_SOURCE_MEANING_RECEIVED','evidence':'SOURCE_STATIC','execution':'NOT_EXECUTED','reader':'/root/facility_atomic_completion_cloud'}
 new.append(a);labels[label]=aid
 REV['mappings'].append({'formal_clause':receiver+':'+label,'atomic_assertion':aid,'meaning':text,'source':sid,'source_unit':unit,'premise':premise,'status':a['status'],'pending_dependencies':[],'relation':'NEW_COMPLETE_UNIT_FINITE_SF_SOURCE_ASSERTION'})
add('pause','S21','pbShowCommands48–72','Each normally reached pause command iteration updates commandwindow/Graphics/Input, then calls pbUpdateSceneMap before testing Back/Action/Use. No menu flag suppresses this call. Exceptions skip subsequent input/return; loop is not every UI.')
add('save-condition','S21','Dedicated Save254–272','Dedicated Save requires game_system, save not disabled, outside Safari and outside active BugContest. Active eligible Safari/Contest therefore hides this item. This registration does not remove ordinary Quit Game or invoke mode End/Judge; those independent complete registrations retain their own receivers.')
add('step','SF-STEP','pbOnStepTaken172–187','After eligible step counters/on_player_step notification, dispatcher creates handled[nil], dispatches transfer-capable handlers and returns on truthy handled[0], before ordinary step encounter call. A handler exception prevents this tail; it is not silently continued.')
add('after-cleanup','S14','after_battle306–329','After ordinary battle, each current player party member has poison statusCount reset if poisoned then is unmega/unprimal. A registered partner causes heal of player and partner parties plus partner unmega/unprimal. These are ordered nontransactional calls, not source-wide healing implementation approval.')
add('after-loss','S14','after_battle320–329','A loss/draw outcome2/5 with can_lose true calls heal on each current player party member, requests uptime/Graphics loop until elapsed0.25, then end-battle handlers and player.straighten. It does not itself call ordinary blackout or Contest judging; native elapsed/termination is conditional.')
add('outcome','S14','set_outcome338–348','Won/caught1/4 increments wild_won for trainer_battlefalse; lost/fled/draw2/3/5 increments wild_lost; other outcomes increment neither. All normally returning cases then pbSet outcome_variable, with no rollback if variable assignment fails.')
add('final-gate','SF-CAPACITY','pbNicknameAndStore33–43','Final global receiver first checks live joint party-full AND Storage-full. True requests two messages then returns before this call seen/owned/nickname/store; false writes Dex seen then owned, then nickname then store. It does not undo prior battle recording; message/earlier write failures skip later work.')
add('nickname','SF-CAPACITY','pbNickname8–15','Nickname helper returns unless givenicknames equals0. Enabled path reads species name and asks confirmation; only true confirmation enters name UI and writes name. It runs after final capacity acceptance and Dex writes, before store.')
add('store-party','SF-CAPACITY','pbStorePokemon17–31','Store repeats joint capacity check with two-message early return, then records first moves. If current player party is not full it appends same Pokemon reference at current party length, irrespective of box-full state; no healing call in this branch.')
add('store-box','SF-CAPACITY','pbStorePokemon23–29','When party is full after accepted capacity gate, Store requests Storage.pbStoreCaught, then reads returned box.name and requests sent-to-box message. Stored object is not duplicated. A store/box/name/message error preserves earlier Dex/nickname/firstmoves/storage prefix.')
add('storage-full','SF-STORAGE','PokemonBox1–53/Storage132–146','Box.full? compares its nonnil item count to array length; Storage.full? returnsfalse upon first nonfull box, otherwise true. Trainer.party_full? uses raw party.length >= MAX_PARTY_SIZE, not only usable/nonEgg members. Normal default-class receiver and no concurrent changes are stated premises.')
add('storage-caught','SF-STORAGE','Storage231–252/accessors159–176','Caught storage optionally heals when HEAL_STORED_POKEMON && currentBox>=0, restoring old ready_to_evolve; then searches current box, else all boxes for firstnil, assigns same object, updates currentBox on fallback and returns box index. If none returns−1; no rollback of heal/earlier assignment. Final box success assumes space remains after gate.')
add('firstmoves','SF-POKEMON','record_first_moves682–685/clear_first_moves702–704','First-move recording clears existing first_moves then pushes each current move.id in current order. A later bad move/array failure leaves already cleared/partially pushed prefix; no independent move compatibility or battle legality claim.')
add('contest-notify','R18','pbBugContestBattle361–379','Contest direct wrapper emits on_start_battle before optional nonPokemon wild generation, then passes live current player party and singleton foe to BugContestBattle; copies outer ballcount into battle before setsingle and prepare. Existing Pokemon bypasses generation. No start-notification rollback.')
add('contest-after','R18','pbBugContestBattle381–390','Inside battle animation, core result is assigned before after_battle(result,true). Only results2/5 then unpause BGM/BGS and call BugContestStartOver, whose current-party heal/unmega/unprimal precedes StartJudging. It does not overwrite core result; normal calls may already heal twice through two distinct paths.')
add('contest-writeback','R18','pbBugContestBattle391–397','After animation and Input.update, outer budget is copied from battle. Exactly zero then requests contest-over message and StartJudging, even after defeat already judged; negative budget doesnot meet this equality gate. Judge appends3 each successful call; no once-only guard here.')
add('contest-return','R18','pbBugContestBattle398–403','After any zero-budget judging, set_outcome writes variable1/stats, then wild-end notification, then Boolean result !=2 && !=5. Core0/1/3/4 returntrue on normal tail;2/5 returnfalse. Earlier callback failures may prevent return; integer Safari return is a different wrapper.')
add('score','R18','pbBugContestScore266–277','Score sums level×4, floor(100×sum(eachIV.to_f/31)), floor(100×hp/totalhp), and rarity60 plus20ifcatch_rate<=120 plus20if<=60. It does not floor each IV quotient separately. Six31IVs yield600; positive totalhp and valid species data are premises.')
for fact in selected['facts']:
 path='Data/Scripts/018_Alternate battle modes/002_BugContest.rb'
 if fact['id']=='KAR-MC-F02':path='Data/Scripts/003_Game processing/002_Scene_Map.rb'
 if fact['id']=='KAR-MC-F03':path='Data/Scripts/003_Game processing/006_Event_HandlerCollections.rb'
 add(fact['id'],micro_sources[path],'Complete selected provider '+fact['id']+' / seven exact units','Received complete provider fact: '+fact['meaning']+' CONTROL: '+fact['control']+' FAILURE: '+fact['failure_prefix']+' OPEN: '+fact['open'])
F['atoms'].extend(new);F['bounded_denominator']=len(F['atoms']);by={a['id']:a for a in F['atoms']}
def ids(*xs):return [labels[x] if x in labels else x for x in xs]
cases=[]
def case(cid,line):
 z={'case':cid,'old_locator_id':f'F08-L{line:04}','line':line,'premise':premise,'children':[],'status':'FINITE_STATIC_COMPLETE_ROW_MEANINGS_RECEIVED','business':'NOT_EXECUTED'};cases.append(z);return z
def child(z,name,meaning,support,proof):
 aids=ids(*support);assert aids and all(a in by for a in aids)
 cid='FAC-SF-'+z['case']+'-'+name
 z['children'].append({'id':cid,'meaning':meaning,'source_assertion_ids':aids,'manual_static_justification':proof,'status':'FINITE_STATIC_CHILD_RECONCILED'})
 for aid in aids:by[aid].setdefault('formal_case_receivers',[]).append(cid)
 a=by[aids[0]]
 REV['mappings'].append({'formal_clause':f'F08{z["case"]}L{z["line"]}:{name}','formal_child_id':cid,'atomic_assertion':aids[0],'support_assertion_ids':aids,'meaning':meaning,'source':a['source'],'source_unit':a['unit_locator'],'premise':premise,'status':'FINITE_STATIC_CHILD_RECONCILED','pending_dependencies':[],'relation':'COMPLETE_SF_CASE_CHILD_WITH_NAMED_SUPPORT'})

z=case('SF01',11)
child(z,'origin','New-session Start stores current map/x/y/direction.',['FAC-A0248'],'Fresh state and normally returning Start42–47.')
child(z,'budget','Supplied example30 is copied, not a hardcoded default.',['FAC-A0249'],'Parameter assignment.')
child(z,'steps','Fixed default runtime Settings600 becomes stored steps.',['FAC-A0251'],'Settings88 complete declaration selected micro unit7.')
child(z,'active','Start sets inProgress true.',['FAC-A0250'],'Before steps assignment.')
child(z,'decision','Fresh initialized decision remains0.',['FAC-A0247','FAC-A0253'],'Start doesnot reset but fresh value0.')
child(z,'captures','Fresh initialized captures remains0.',['FAC-A0244','FAC-A0252'],'No capture reset in Start; initial0.')
child(z,'persistent','Live state belongs to persistent outer global metadata; native serialization/reload behavior remains separate.',['FAC-A0260','FAC-A0358','FAC-A0362','FAC-A0367'],'Whole-object registered global supplier with no inner validation.')
child(z,'save','Dedicated Save is hidden; ordinary Quit path remains under independently received SF36–40.',['save-condition'],'Complete Pause254–272; save-vector-reception.v1.json includes fullPause321 and exact shared-Quit cases. No claim Quit equals modeQuit.')
z=case('SF02',12)
child(z,'rewrite','Repeated Start overwrites origin/budget/steps and writes active true.',['FAC-A0248','FAC-A0249','FAC-A0250','FAC-A0251'],'No inactive guard.')
child(z,'captures','Existing captures2 remains2.',['FAC-A0252'],'No assignment in Start.')
child(z,'decision','Existing decision1 remains1.',['FAC-A0253'],'No assignment in Start.')
child(z,'stepguard','Nonzero decision prevents eligible step decrement.',['FAC-A0269'],'Counter guard before subtraction.')
z=case('SF03',13)
child(z,'selected','Index1 picks original second member and eventual party is singleton same object.',['FAC-A0316','FAC-A0324'],'Start direct indexed reference and array replacement.')
child(z,'spares','Otherparty contains indices0/2/3 in original order.',['FAC-A0321'],'Index exclusion loop, not object identity exclusion.')
child(z,'noheal','Start doesnot call heal on selected or spared members.',['FAC-A0316','FAC-A0324'],'Whole Start171–196 source has no heal; calls are named sequence only.')
child(z,'opponents','Five retained opponent indices are distinct.',['FAC-A0322','FAC-A0323'],'Duplicate rejection; loop eventualcompletion is an explicit static path premise, no bound.')
child(z,'timer','Uptime origin is written before selection.',['FAC-A0318','KAR-MC-F04'],'No wallclock substitution.')
child(z,'clears','Stock/places/lastContest are cleared during Start.',['FAC-A0317','FAC-A0318'],'Freshnil/array assignments.')
child(z,'count','Successful tail increments contest count once.',['FAC-A0326'],'After singleton/resetwrites.')
z=case('SF04',14)
child(z,'reception','Active saved reception map is in Safari without needing flag.',['FAC-A0262','FAC-A0263'],'Region OR branch.')
child(z,'flag','Active flagged map is accepted.',['FAC-A0262','FAC-A0264'],'Metadata flag OR branch.')
child(z,'third','Entering unrelated unflagged map ends and clears session.',['FAC-A0265','FAC-A0256','FAC-A0257','FAC-A0258','FAC-A0259'],'Enter-handler false region -> End; transfer caller normally returns.')
child(z,'inactive','Inactive ordinary-map enter still invokes lazy getter/End and refresh.',['FAC-A0260','FAC-A0265','FAC-A0259'],'No active precondition in enter handler.')
z=case('SF05',15)
child(z,'two','Stored2 decrements to1 and positive check returns without expiry messages.',['FAC-A0270'],'88–102 full handler.')
child(z,'one','Stored1 decrements0; two messages precede decision1 and return request.',['FAC-A0270','FAC-A0272','FAC-A0273'],'Order preserved, no hypothetical prior decisionwrite.')
child(z,'handled','After successful return request handler writes handledtrue.',['FAC-A0274'],'Failure of transfer/request doesnot guarantee this tail.')
child(z,'noencounter','Truthy handled makes step dispatcher return before ordinary encounter.',['step','FAC-A0274'],'Complete dispatcher172–187, not inferred from handler name.')
child(z,'occupied','Already handled transfer slot bypasses counter without decrement.',['FAC-A0266'],'Truthy explicit fixture; not nil-only battleoverride gate.')
z=case('SF06',16)
child(z,'zero','Exactly0 config skips all decrement and shows balls-only pause info.',['FAC-A0267','FAC-A0448'],'Two independent consumers: Settings==0 and Settings<=0.')
child(z,'negative','Start stores−5; first eligible step decrements−6 and follows expiry.',['FAC-A0251','FAC-A0270','FAC-A0271'],'Not zero, remaining<=0.')
child(z,'displaynegative','Negative config still displays balls only, without making counter infinite.',['FAC-A0448','FAC-A0271'],'UI and counter comparison differ.')
z=case('SF08',18)
child(z,'caughtcore','Last-ball capture keeps core4 after caught record/store.',['FAC-A1622','FAC-A1624','FAC-A1631'],'Decision4 skips unresolved-round corebudget2 branch.')
child(z,'caughtouter','Budget0 with core4 copies out, emits outer exhausted message, writes session1/return and variable1=4, returns integer4.',['FAC-A0287','FAC-A0288','FAC-A0289','FAC-A0290','FAC-A0294','FAC-A0296'],'Core!=2 permits outer message; no decision normalization.')
child(z,'failedcore','Uncaptured last ball leaves core0 until round-end budget0 sets2 after message.',['FAC-A1622','FAC-A1631'],'Budget branch before escape random.')
child(z,'failedouter','Core2 suppresses duplicate outer message but still ends session and writes/returns2.',['FAC-A0289','FAC-A0290','FAC-A0294','FAC-A0296'],'Message suppression only, not skipping exhaustion.')
z=case('SF10',20)
child(z,'run','Run writes3 after safe escape feedback; normal positive-budget outer session remains0, var1/return integer3.',['FAC-A1628','FAC-A0288','FAC-A0294','FAC-A0296'],'No run gate; named continuing premise.')
child(z,'wildescape','Unresolved positive-budget round random pass writes3 and wild escape message.',['FAC-A1632','FAC-A1635'],'Core flee; no sessionend unless outer budget<=0.')
child(z,'abortmenu','Own abort rescue before consumption yields core0 and unchanged positive budget/sessiondecision0.',['FAC-A1636','FAC-A0287','FAC-A0288'],'Dedicated rescue resets core only.')
child(z,'abort2','From2 consume1 then abort: core0, budget1 copiedout, no exhausted branch, variable/return0.',['FAC-A1622','FAC-A1636','FAC-A0287','FAC-A0288','FAC-A0294','FAC-A0296'],'No consumption rollback.')
child(z,'abort1','From1 consume1 then abort: core0, budget0, outer message/session1/returnstart but variable/return remain0.',['FAC-A1622','FAC-A1636','FAC-A0288','FAC-A0290','FAC-A0294','FAC-A0296'],'Outer exhaustion independent of core0 rescue.')
z=case('SF14',24)
child(z,'order','End appends spares to selected singleton, producing [selected,original0,original2,original3].',['FAC-A0321','FAC-A0324','FAC-A0328'],'Objectreferences original; no sorting to originalparty order.')
child(z,'noheal','Restoring selected+spares has no healing operation.',['FAC-A0328'],'Whole End205–224; distinct retained-Pokemon box-heal policy is outside restoredparty claim.')
child(z,'clear','Successful end clears temporary otherparty.',['FAC-A0333'],'After storage/place prefix normally completes.')
for cid,line in [('SF15',25),('SF22',32)]:
 z=case(cid,line)
 child(z,'postjoin','Final joint capacity is evaluated after current party has been joined with spares.',['FAC-A0328','FAC-A0330','final-gate'],'Ordered End call site; no prematchparty substitution.')
 child(z,'party','Partyroom/boxfull still passes AND gate and appends retained sameobject to party.',['final-gate','store-party','FAC-A1654'],'False partyfull short-circuits Storage, then raw append.')
 child(z,'box','Partyfull/boxroom passes gate and stores in a realbox, then reads/displays boxname.',['final-gate','store-box','storage-caught'],'Valid defaultstorage, free slot remains, normal callbacks.')
 child(z,'full','Bothfull requests exactlytwo messages and returns before newseen/owned/nickname/store in finalhelper.',['final-gate'],'No universal totalDexnochange: priorbattlewrites persist.')
 child(z,'nickname','Capacity accepted -> Dexseen/owned -> enabled nickname confirmation/UI -> store.',['final-gate','nickname'],'Enabled means givenicknames==0; decline still proceeds tostore.')
 child(z,'preservebattle','Rejected finalreceive doesnot rollback battle phase caught/Dex/stat records.',['FAC-A1677','FAC-A1678','final-gate'],'No rollback code in rejection; earlier completed writes remain.')
 child(z,'endtail','Normalreturn of rejection or store still allows endedtrue, clear stock/activity fields and timestamp.',['FAC-A0330','FAC-A0333','FAC-A0335'],'End ignores helper return; normal judge/place prerequisites required.')
z=case('SF16',26)
child(z,'interrupted','Active offlimits leave invokes End(true), appends spares, sets endedfalse and skips finalstockstore.',['FAC-A0356','FAC-A0328','FAC-A0329'],'Complete leave registration and End.')
child(z,'judgedtail','If places valid, interrupted end querieswin then clearsactivity/timestamp.',['FAC-A0331','FAC-A0333','FAC-A0335'],'Judge prefix already completed in input.')
child(z,'unjudged','Without judge places, partyappend precedes place-read failure, before stateclear/timestamp.',['FAC-A0328','FAC-A0331','FAC-A0332'],'No rollback; not a precondition check at entry.')
child(z,'repeat','Inactive repeated End returns without effects.',['FAC-A0327'],'Entry guard beforepartyappend.')
z=case('SF17',27)
child(z,'expiry','Captured1200 limit and uptimeelapsed>=1200 satisfy expired onlywhen active undecided.',['KAR-MC-F04','FAC-A0306','FAC-A0308'],'Raw predicate; no nativeclockrate promise.')
child(z,'gates','Forcedroute/interpreter/messagewindow each defer reached frame handler without timer reset.',['KAR-MC-F05','FAC-A0354'],'Allguards precede messages.')
child(z,'messages','With allthreefalse, two messages then StartJudging.',['KAR-MC-F05','FAC-A0347'],'Messagefailure precedesdecisionwrite; judgingfailure leavesdecision1.')
child(z,'pausecaller','Open normal pause commandloop calls pbUpdateSceneMap before inputaction checks.',['pause'],'Complete actualUIcaller48–72, not allmenus.')
child(z,'micro','Nonfaded Scene_Map helper reaches miniupdate->updateSpritesets->on_frame_update and sequential Contestcallback.',['KAR-MC-F02','KAR-MC-F03'],'All earlier update/callback dependencies normally return.')
child(z,'menunotguard','There is no menu/miniflagguard in Contest timeout handler, so next reached qualifying microdispatch can judge without closing pause first.',['KAR-MC-F05','pause','KAR-MC-F02'],'Not eventual delivery or nativecadence assertion.')
child(z,'fadecontrast','Faded helper performs no miniupdate; true postponeguards defer handler evenif dispatch occurs.',['KAR-MC-F02','KAR-MC-F05'],'Two separate barriers, no generalized allUI behavior.')
z=case('SF18',28)
child(z,'zero','Classcaptured0 disables expiration and timercreation.',['FAC-A0307','FAC-A0352','KAR-MC-F04'],'Expiry<=0, display!=0 fails.')
child(z,'negative','Classcaptured−60 disablesexpiration but permits timercreation and clamps displayed time to00:00.',['FAC-A0307','FAC-A0350','FAC-A0352','FAC-A0353','KAR-MC-F07'],'No equality ofnegative/zeroUI; valid uptimeelapsed>=0 in derivedfixture.')
z=case('SF19',29)
child(z,'unresolved','Last failedthrow reaches baseEOR then localbudget<=0&&decision0 ->core3.',['FAC-A1645','FAC-A1652'],'BaseEOR normalreturn andstillundecided explicitinput.')
child(z,'zerojudge','After normalanimation/cleanup, budget0 writeback requestsmessage+judge.',['contest-after','contest-writeback'],'Exactlyzerooutergate.')
child(z,'fledtail','Core3 increments wildlost, writesvar1=3 and returnsBooleantrue.',['outcome','contest-return'],'Wild trainerflagfalse;3!=2&&3!=5.')
child(z,'caught','Last successfulcapture core4 is preserved by localEOR; budget0 stilljudges; var1=4/wildwon andtrue.',['FAC-A1653','contest-writeback','outcome','contest-return'],'Not3/lost; decisionnotrewrittenbyjudging.')
child(z,'lossdraw','Existing2/5 survivesEOR and takes defeatjudging branch; core remains2/5.',['FAC-A1653','contest-after'],'No overwrite byzero-budgetEOR whenalreadydecided.')
z=case('SF20',30)
child(z,'heal','Core2 after_battle(true) heals currentparty before later Contestdefeat fallback.',['after-loss','contest-after'],'Distinct complete sourcecalls; nativequartersecondloopnormalcompletion premise.')
child(z,'firstjudge','Defeatunpausesaudio then ContestStartOver heals/unmega/unprimal and judgesonce, appending3.',['contest-after','FAC-A0346'],'Noordinaryblackoutdomainclaim.')
child(z,'secondjudge','Afteranimation, outerbudget0 causes message+secondStartJudging; placesappend another3 ->6.',['contest-writeback','FAC-A0346'],'No decision==0guard or clearbetween calls.')
child(z,'tail','Core2 remains2, wildlost+1, var1=2, Booleanfalse.',['outcome','contest-return'],'Twojudges do not mutate localcoredecision.')
z=case('SF23',33)
child(z,'level','Level14 contributes56.',['score'],'14×4 manually evaluated, no modelrun.')
child(z,'iv','SixIV31 eachquotient1; sum6 then×100/floor ->600.',['score'],'Singlefloorafter sum, correct31declaration; sixstatinputexplicit.')
child(z,'fullhp','Fullhp contributes100; catch45 rarity100; total56+600+100+100=856.',['score'],'Both <=120and<=60 bonuses apply.')
child(z,'onehp','HP1/200 termfloor0; total56+600+0+100=756.',['score'],'100/200=0.5floor0.')
child(z,'raritybounds','Catch60->100,61->80,120->80,121->60.',['score'],'Inclusive <=60/<=120 comparisons, independentbonuses.')
z=case('SF25',35)
child(z,'nomaps','NoBugContestorLandeligiblemap raises beforeopponentconstruction; decision1 alreadywritten, transfernotreached.',['FAC-A0338','FAC-A0339','FAC-A0347','FAC-A0348'],'StartJudgingprefix beforejudge.')
child(z,'emptytable','Nil encounterresult raises beforePokemon.new forselectedmap.',['FAC-A0341','FAC-A0342'],'Earlieropponentgeneration maypersist; nomadeupfallback.')
child(z,'few','Artificialemptycontestants+nostock givesfewerthan3 andraisesbeforeappend.',['FAC-A0337','FAC-A0344'],'Normalfiveopponents isdifferentvalidinput; no global cardinality assumption.')
z=case('SF26',36)
child(z,'nocatch','Nostock yieldsfiveopponents; validfirst3containno negativeindex, playerplace3.',['FAC-A0337','FAC-A0311','FAC-A0312'],'Successfulnormalfivegenerationpremise.')
child(z,'first','Playerhighestscore isfrontnegativeindex, place0 andnormalEndwinsincrement.',['FAC-A0345','FAC-A0311','FAC-A0331'],'Noequal-scoretie inthissubcase.')
child(z,'tie','Equal scores have no explicit secondarysortkey or promisedstability.',['FAC-A0345'],'Nativeactualtieorder leftunproved, not fabricated.')
child(z,'rejudge','Twosuccessfuljudgesappend6; playerplace stillonlyscansfirst3.',['FAC-A0346','FAC-A0311'],'Queries havedifferentbounds.')
child(z,'info3','Informationindex3 accessesfourthentry(secondbatchfirst), resolvesname/speciesname/score andwritesvars1/2/3.',['FAC-A0313','FAC-A0314'],'No first3limit inthisquery; demoactualcallerreachabilityunclaimed.')
child(z,'info6','Index6withlength6 yieldsmissingentry andfailsatread.',['FAC-A0315'],'Sourcefailureprefix; notfallbackplayerplace3.')
z=case('SF27',37)
child(z,'safariyes','AcceptedSafariQuit endsmenuscenefirst, writesdecision1 thenrequestsreturn; fieldsawaitleaveclear.',['FAC-A0451','FAC-A0265'],'NotimmediateEndcall.')
child(z,'safarino','Refusalrefreshes/reopens menu andreturnsfalse withoutmodewrite.',['FAC-A0452'],'NormalmenuUIreturnpremise.')
child(z,'contestyes','AcceptedContestQuit endsmenuscenethenStartJudging, notEnd(true).',['FAC-A0457','FAC-A0347'],'Activeexit==judging, notinterruption.')
z=case('SF28',38)
child(z,'balls','DebugcanwriteSafari0budget; reachednextbattleaction/outerwritebacktakesnormalbudgetbranches.',['FAC-A0545','FAC-A1631','FAC-A0288'],'Budgetwriteitselfdoesnotend/judge; artificialzeroallowsnegativeonthrow.')
child(z,'steps','Nonpositiveconfiguredstepsareuneditable/infinitedebugtext whileballseditorremains0..99999.',['FAC-A0542','FAC-A0543','FAC-A0545'],'Debugconditionstrictpositive, separateSafari stepcounternegativebehavior.')
child(z,'timeinput','PositiveconfiguredContesttimecomputesclampedremainingminute/second andallows0..99999wholeminutes.',['FAC-A0546','FAC-A0548','FAC-A0549'],'DebugreadsSettings, timerpredicatecapturesconstant separately.')
child(z,'timerwrite','Editoraddsdeltaminutes×60totimer_start andupdatesthefirstcurrentTimerDisplay.start_time.',['FAC-A0550','FAC-A0551'],'Noall-spritessynchronizationclaim.')
child(z,'nonpositive','Zero/negativeconfiguredContesttime displaysinfiniteanddoesnotentertimeeditor.',['FAC-A0547'],'Notmaptimernegative00:00contract.')
child(z,'noreset','Debugwritesdonotstart/end/judge/resetwholemode.',['FAC-A0555'],'Noimplicitlifecycletransition.')
z=case('SF31',41)
child(z,'nil','Nilchosenindex failsatpartylookupafterbudget/active/timer/stock/placesprefix; noopponents/singletonreplacement.',['FAC-A0316','FAC-A0317','FAC-A0318','FAC-A0319'],'ExactStartorder; notearlyvalidation.')
child(z,'index4','Index4oflength4yieldsnil; all4membersgoothers, successfulsamplerthenparty[nil],resets/count.',['FAC-A0320','FAC-A0321','FAC-A0324','FAC-A0325','FAC-A0326'],'Laternilconsumersdonotmovefailuretoentry.')
child(z,'negative','Index−1selectslastbutdoesnotmatchnonnegativeeach_with_index, all4aresparedandEndappendsduplicatesameobject.',['FAC-A0321','FAC-A0324','FAC-A0328'],'Rubynormalnegativearrayindexbehaviorisexistingformalstaticlanguagepremise, no nativeexecution.')
child(z,'index2','Validindex2producesselectedthird/others0,1,3.',['FAC-A0321','FAC-A0324'],'SuccessfulStarttail.')
z=case('SF32',42)
child(z,'afterend','Inactiveandawayjudgingmap enterClearIfEnded invokesclear.',['FAC-A0357'],'Noextrawas-activeprecondition.')
child(z,'timestamp','ClearpreserveslastContest, sorecentqueryat0<=elapsed<24hremainstrue.',['FAC-A0303','FAC-A0305'],'Strictboundwallclockcomparison; no guaranteeclockmonotonic.')
child(z,'runtime','Clearpreserveschosenindex/timerorigin.',['FAC-A0303'],'Notidenticalnewobject.')
child(z,'neverstarted','Inactivewithniljudgestartstillmeetsclearguardandrewritesemptyfields.',['FAC-A0357','FAC-A0298','FAC-A0299','FAC-A0302'],'Idempotentfieldvaluesdonotmeanhandlernotcalled.')
child(z,'activeallowed','ActivemovingbetweenallowedmapsdoesnotinterruptedEndanddoesnotClearIfEnded.',['FAC-A0356','FAC-A0357'],'Bothspecificguardschecked.')
z=case('SF33',43)
child(z,'preconsume','Menuabortbeforeconsumption givescore0,unchangedpositivebudget,session0.',['FAC-A1636','FAC-A0287','FAC-A0288'],'Noexhaustionunderexplicitcontinuinginput.')
child(z,'two','2->consume1->abortpreservesbudget1/core0;noclear,variable/return0.',['FAC-A1622','FAC-A1636','FAC-A0288','FAC-A0294','FAC-A0296'],'Dedicatedrescueisnottransaction.')
child(z,'one','1->consume0->abortpreservesbudget0/core0,outerexhausts/session1/returnstart,variable/return0.',['FAC-A1622','FAC-A1636','FAC-A0290','FAC-A0294','FAC-A0296'],'Sessionendingdoesnotrewritelocalcore.')
z=case('SF34',44)
child(z,'safariin','NewSafaribattlebudget0thenouter20copiedin;outerremains20duringconstruction.',['FAC-A1592','FAC-A0284'],'Session->battleassignmentdirection.')
child(z,'safariout','Afteroneconsumptionbattle19,outercopied19onlyafterbattleanimation/Inputnormallyreturn.',['FAC-A1622','FAC-A0287'],'Nosharednumericfieldalias.')
child(z,'contestin','NewContestbattlebudget0thenouter20copiedinbeforeprepare.',['FAC-A1642','contest-notify'],'Outerbudgetnotassignedfromnew0.')
child(z,'contestout','Positivebudget20oneconsume->19;afteranimation/Inputouterwriteback19.',['FAC-A1645','contest-writeback'],'Budgetdecrementguards>0;normalreturnpremise.')

assert len(cases)==25
packet={'schema':'FAC-25-additional-SF-rows-complete-child-reception/v2','utc':UTC,'reader':'/root/facility_atomic_completion_cloud','premise':premise,'new_source_assertions':new,'complete_own_source_units':units,'received_provider':'kernel-contest-micro-reception.v2.json','cases':cases,'case_child_count':sum(len(z['children']) for z in cases),'source_reads':['f1ef6b wholeSafari196','11ea60/f6dc96 wholeContest441','5eedee completePause/after_battle/set_outcome/Trainercapacity','d73957 wholeStep172–187/recordmoves','c46468 wholeBox/storagefinite/finalreceive/Contestwrapper','earlier2e074c/71ced6/6e3b55/be925e/b8c030/050f2d finiteproducerreads','0fec0b/8f0938/f92a8c currentfacttextreview'], 'remaining_SF':['SF13 roaming/generation override necessary contacts','SF24 encounter028 wholeliteral and complete finite selector/version consumer','SF29 radar/roaming registration and end-notification consumers','SF35 partnerdouble source route/complete consumers'], 'qualification':'Exact25row meaning children received within conditional static premises; execution0. No whole original atomic census; allsourcefacts mayaggregate necessary assumptions. Other originalSFrows have separate receipts. SF13/24/29/35 deliberately unclosed. Fullstorage/world/UI/native domains not received.','new_required_optional_contexts_votes':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
save('SF25-additional-case-child-reception.v2.json',packet)
closing={z['old_locator_id'] for z in cases};before=len(N['unmet_formal_seed_structures'])
N['unmet_formal_seed_structures']=[z for z in N['unmet_formal_seed_structures'] if z['old_locator_id'] not in closing]
assert before-len(N['unmet_formal_seed_structures'])==25
for z in cases:N['closed_finite_formal_seed_structures'].append({'old_locator_id':z['old_locator_id'],'path':F['source_identities']['F08']['path'],'line':z['line'],'case':z['case'],'children':[c['id'] for c in z['children']],'status':'FINITE_STATIC_CHILD_RECEPTION_COMPLETE','external_catalog_primary':False,'receipt':'SF25-additional-case-child-reception.v2.json'})
N['updated_utc']=UTC
save('forward-mapping.json',F);REV['v2_new_exact_child_bindings']=len(REV['mappings'])-992;save('reverse-mapping.json',REV);save('next-dispatch.json',N)
P=load('progress.json');P.update(updated_utc=UTC,manually_authored_finite_source_assertions=len(F['atoms']),source_to_formal_bindings=len(REV['mappings']),finite_new_child_bindings=len(REV['mappings'])-992,original_formal_seed_locators_still_unexhausted=len(N['unmet_formal_seed_structures']),new_SF_exact_rows=30,new_SF_exact_case_children=62+packet['case_child_count']);save('progress.json',P)
A=load('atomic-denominator.json');A['updated_utc']=UTC;A['full_original_atomic_denominator']['unmet_original_paragraph_table_locators']=len(N['unmet_formal_seed_structures']);A['finite_reverse_bindings'].update(count=len(REV['mappings']),qualification=f'992historical+{len(REV["mappings"])-992}explicitfinite routes; not wholecanonicaldenominator');A['finite_SF_exact_case_children']={'rows':30,'children':62+packet['case_child_count'],'memberships':['sf07-09-11-12-full-child-reception.v2.json','sf21-stock-full-child-reception.v2.json','SF25-additional-case-child-reception.v2.json'],'source_overlap':'Casechildren reuse prior/new finite source IDs. Not new source atoms or complete global denominator.'};save('atomic-denominator.json',A)
L=load('reading-ledger.json');L['updated_utc']=UTC;L.setdefault('v2_additional_source_reads',[]).append({'utc':UTC,'packet':'SF25-additional-case-child-reception.v2.json','complete_units':len(units),'actual_receipts':packet['source_reads'],'qualification':packet['qualification']});L.setdefault('v2_exact_receptions',[]).append({'utc':UTC,'packet':'kernel-contest-micro-reception.v2.json','original_bytes':len(raw),'original_sha256':sha(raw),'actual_selected_facts':[f['id'] for f in selected['facts']],'unadopted':selected['unadopted']});save('reading-ledger.json',L)
for name in ['kernel-contest-micro-selected-source.v2.json','kernel-contest-micro-reception.v2.json','SF25-additional-case-child-reception.v2.json']:
 b=(V/name).read_bytes();print(name,len(b),sha(b))
print('newfacts',len(new),'assertions',len(F['atoms']),'bindings',len(REV['mappings']),'SFnewchildren',packet['case_child_count'],'remaining',len(N['unmet_formal_seed_structures']))
