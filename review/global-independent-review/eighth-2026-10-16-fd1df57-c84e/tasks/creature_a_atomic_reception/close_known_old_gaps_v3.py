import pathlib,json,datetime,hashlib,subprocess,collections
P=pathlib.Path(__file__).parent;NOW=datetime.datetime.now(datetime.timezone.utc).isoformat();R=pathlib.Path('/workspace/pokemon-essentials');C='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
def save(n,d):(P/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
l=json.loads((P/'reading-ledger.json').read_text())
# Correct only locator bounds; original commands really rendered these entire units.
for x in l.get('own_partial_read_spans',[]):
 if x['path'].endswith('/001_Compiler.rb') and x['range']==[968,991]:x['range']=[967,991]
 if x['path'].endswith('/003_Overworld_MapTransitionAnims.rb') and x['range']==[80,139]:x['range']=[80,138]
 a,b=x['range'];raw=(R/x['path']).read_text(encoding='utf-8-sig').splitlines();norm=('\n'.join(raw[a-1:b])+'\n').encode();x['normalized_span_bytes']=len(norm);x['normalized_span_sha256']=hashlib.sha256(norm).hexdigest()
path='Data/Scripts/001_Settings.rb'
if path not in {x['path'] for x in l['own_full_reads']}:
 b=(R/path).read_bytes();assert b==subprocess.check_output(['git','show',C+':'+path],cwd=R);l['own_full_reads'].append(dict(repo='R',commit=C,tree='7589c800b61ba13a13040ed0d686979b80a84fd0',path=path,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),blob=subprocess.check_output(['git','rev-parse',C+':'+path],cwd=R,text=True).strip(),lines=len(b.splitlines()),status='FULL_READ_BY_SELF',reader='/root/creature_a_atomic_reception',extent=[1,len(b.splitlines())],source_of_read='1–160,154–205,205–332,333–524 actual contiguous read through EOF',recorded_utc=NOW,semantic_time_utc='UNRECORDED_PER_CALL',primary=False,qualification='Settings definitions only; actual required consumer meanings separately joined, no KERNEL whole-domain transfer'))
path='Data/Scripts/002_BattleSettings.rb';b=(R/path).read_bytes();norm=('\n'.join(b.decode('utf-8-sig').splitlines()[:92])+'\n').encode();l['own_partial_read_spans'].append(dict(repo='R',commit=C,path=path,range=[1,92],named_units='Default turnorder/obedience/affection constants and immediate related definitions, not whole Settings module',status='PARTIAL_FILE_ACTUAL_READ_SPAN',reader='/root/creature_a_atomic_reception',bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),lines=len(b.splitlines()),normalized_span_bytes=len(norm),normalized_span_sha256=hashlib.sha256(norm).hexdigest(),recorded_utc=NOW,semantic_time_utc='UNRECORDED_PER_CALL'))
save('reading-ledger.json',l)
s=json.loads((P/'sourcefact-consumer-receptions.json').read_text());fs={f['id']:f for f in s['facts']}
A=json.loads((P/'manual-atomic-clauses.json').read_text());D=json.loads((P/'old-locator-disposition.json').read_text());byid={a['id']:a for a in A['atoms']}
for a in A['atoms']:
 if a.get('parent_original_fact') in fs:
  f=fs[a['parent_original_fact']];a['consumer_reception_initial']=a.get('consumer_reception_initial',a.get('consumer_reception'));a['consumer_reception']=f['consumers'];a['current_sourcefact_reassessment_ref']='sourcefact-consumer-receptions.json#/facts/'+f['id']+'/manual_consumer_reassessment_v2';a['support']='SUPPORTED_LOCAL_STATIC_MEANING; ALL_SUPPLIED_OLD_PARENTS_DECOMPOSED_BUT_GLOBAL_DENOMINATOR_UNFROZEN'
# Specific new complete evidence reception, never a blanket PASS for vectors or parents.
closures={
'CAA-W20-L071-A01':('CORE F16完整after_battle+own pbStartOver80–138','败/平局canlose特定治疗与不canlose进入StartOver区分；后者BugContest先早分流，普通先stats.blackout+1再playerheal，后转移失败保已治。'),
'CAA-W20-L071-A02':('own pbStartOver80–138 / pbBugContestStartOver301–308 / Trainer.heal_party完整','BugContest分支逐party heal→unmega→unprimal再StartJudging；普通blackout先heal。其它未具名竞赛实现不从此两caller推全家族。'),
'CAA-W20-L071-A03':('UI facility-lifecycle complete facts63','organized normal-end才还原等级后逐索引heal/unmega/unprimal/item，任何提前异常无ensure，不能把一次胜利推广所有设施。'),
'CAA-W20-L071-A05':('CAA-LIFE-D02/D03完整','deposit先slot引用赋值再heal，withdraw不heal；wrapper先stats写，失败前缀保持。'),
'CAA-W20-L071-A06':('own Interpretercommand3141099–1109','参数0==0才执行；HEAL_STORED=true只playerheal，false pbEachPokemon遍历party/boxes；默认gen8为false。'),
'CAA-W20-L111-A02':('CAA-LIFE-DBG05 / own Debug1151L','status editor先拒蛋/濒死，再status=后count=，Sleep非正选值取消；cure heal_status。'),
'CAA-W20-L131-A11':('CAA-LIFE-DBG01','忘招菜单明确moveindex>=0才读取并调用forget_move_at_index，负选择取消；底层-1删除末项不变。'),
'CAA-W20-L160-A06':('own ChangeSelf104–124 and Battler627–635','usingMultiTurnAttack?依TwoTurnAttack或HyperBeam/Rollout/Outrage/Uproar/Bide>0；pbReducePP先该谓词返true，再pp<0/totalpp<=0返true，pp0返false，其余pbSetPP。'),
'CAA-W19-L143-A07':('own DebugPokemonCommands1151L CAA-LIFE-DBG04','rawIV/EV编辑后calc，PID重掷后calc但不清派生缓存；不把编辑器目标菜单列表/原生数值输入全域签过。'),
'CAA-W62-L068-A07':('own DebugMenuCommands555–705 complete6handlers','fillboxes先按Species逐seen forms和owned(refreshfalse)，再capacity装baseform，最后refresh；partyDemo先清party再逐造/登记/学招，cancel不替既有前缀回滚。'),
'CAA-CATSHARED-L119-A05':('own HandlerHash97–139完整','copy取当时handler引用加入新key；之后源add替换不重绑副本key，原Hash对象in-place修改仍共享；不是每次动态重新解析源key。')}
for id,(ev,meaning) in closures.items():
 a=byid[id];a['initial_assertion_before_later_read']=a.get('initial_assertion_before_later_read',a['assertion']);a['assertion']=meaning;a['later_complete_reception']=dict(utc=NOW,reader='/root/creature_a_atomic_reception',evidence=ev,meaning=meaning,parent_auto_acceptance=False)
# Precise previously stale buckets: replace only each exact known old placeholder, preserve original and bounded outstanding details.
replacement={
'exact complete debug Owner/source/cannot_* tools and obedience consumers not yet read; source definitions/normal acquire/hatch/trade are independently read':[],
'Data/Scripts/016_UI/024_UI_MysteryGift.rb complete reward mutation/claim caller still to read':[],
'Actual TM57 PBS full record and pbMoveTutorChoose complete producer still to read; Party nonappend and machine dispatcher read':[]}
for a in A['atoms']:
 co=a.get('complete_contract')
 if not co:continue
 old=co.get('open_exact',[])
 hit=[v for v in old if v in replacement]
 if hit:
  co['initial_open_exact_before_v3']=co.get('initial_open_exact_before_v3',old[:]);co['open_exact']=[v for v in old if v not in replacement]
  co['later_reception_v3']=dict(utc=NOW,reader='/root/creature_a_atomic_reception',evidence=['DebugPokemonCommands1151L','Obedience107–181完整','MysteryGift428L完整','TutorChoose452–487完整','actual-pbs-record-reception TM57/MAGNEMITE'],meaning='Own exact full sources/units and finite complete records actually read; earlier not-read label removed only for named finite evidence. Other callbacks/PBS/native not silently accepted.')
  if a.get('source_support')=='PARTIAL_EXACT_SOURCE_PENDING':a['source_support']='SUPPORTED_BOUNDED_STATIC_AFTER_NAMED_V3_RECEPTION'
# Explicit identities for the removed MysteryGift gap.
A['later_complete_contracts_v3']={'MG_RECEIVE':dict(source='MysteryGift361–428 complete; full428L ownread',normal='Findfirst unclaimedid; Pokemon gift rerollPID→calc→timeReceived Time.now.to_i→method4→firstmoves→level/map→wasowned→pbAddSilent(existing object); onlysuccess message thenclaim[id], optionalDexpromptmessage→lastseen→Entry. Item canadd→add→message→claim. No Owner reset.',failure='Pre-add mutation persists whenfullparty/storage rejects; message failure afterstore butbeforeclaim can leave gift unclaimed and sameobject stored; afterclaim entry failure retainsclaim. Exactsource, no newformalfinding.',premise='Valid storedgift shape/registered records, normal preceding dependencies, no plugins; time/native not executed.'),'ITEM_TRANSFER':dict(source='MoveEffects_Items1–163 complete4classes, CORE consume/remove F12/F13, ownPokemon/initialItem setter receivers',normal='Thief nonwildlivinguser, targetaffected/noSub, targetitem/userempty, no unlosable/StickyHold+mold gate; useritem first, wildtarget && !user.initialItem && item==target.initialItem then user.initialItem=stolen and permanenttarget.remove else temporaryremove; messages thenheldcheck. Bestow andTrick exact separate initialrecord gates; Recycle restores recycleitem and onlywildbattle+missinginitial updatesinitial.',failure='Modelwrites precede messages/heldtriggers; no inferredrollback; defaultfullItem/Move dispatcher families not autoapproved.',premise='Actualeffectmethod reached after ordinarydispatcher checks; validbattle ownership/index/records. Only four complete classes adopted.'),'PBS_COMPILE_DISCOVERY':dict(source='Compiler967–991 complete',meaning='PBS/*.txt nonrecursive, longest basefilenamefirst, exact/base_ match; backups in subdirectories not automatic defaultload. Alternative complete record receipts explicit.')}
A['warning']='1430 supplied oldlocators each manually decomposed or bounded typed; 6939 semantic records are not a frozen fullglobal atomic denominator. Sourcefact261 children never substitute fullformal parents. No heading/line/semicolon count or source FULL_READ grants consumer/global PASS.';A['recorded_utc']=NOW
# Copy latest finite evidence to each relevant exact parent without changing its independent acceptance flag.
for r in D['rows']:
 cs=[byid[i] for i in r.get('manual_children',[]) if i in byid]
 later=[x.get('later_complete_reception') for x in cs if x.get('later_complete_reception')]
 if later:r['later_named_receptions_v3']=later
 if cs and all(x.get('source_support')=='SUPPORTED_BOUNDED_STATIC_AFTER_NAMED_V3_RECEPTION' for x in cs):r['source_support']='SUPPORTED_BOUNDED_STATIC_AFTER_NAMED_V3_RECEPTION'
save('manual-atomic-clauses.json',A);save('old-locator-disposition.json',D)
# Preserve old receipt bytes and record later actual source inspection honestly.
save('core-money-reception.scope-clarification.v1.json',dict(schema='gr8-cre-a-later-source-clarification/v1',utc=NOW,original_unchanged='core-money-reception.v1.json',meaning='Original full two CORE money objects were actually received; own pbMaxLevelInTeam432–439 source inspection occurred afterward. This later record is the own complete source join; it doesnot backdate it to originalreceipt recorded_utc.',source='Battle001432–439 complete; player-team maxlevel behavior verified',business='NOT_EXECUTED',update='UPDATE_NOT_STARTED'))
F=json.loads((P/'io/recent-read-failures.json').read_text());F['recorded_utc']=NOW
for chunk,code,err in [('774df5',1,'Own metadatahelper asserted nonexistent spelling003_Overworld_FieldMoves beforewriting; corrected to actual004 then succeeded.'),('db0772',1,'Own102 mapping coverage assertion found omitted62/99; noartifactwrites beforeassertion, correctedboth then succeeded.'),('7645dd',2,'formal sed from R cwd nonexistent; precedingBattleSettings source andrgvalid, formalcorrectcwdsubsequentlyread.')]:
 if chunk not in {x['tool_chunk'] for x in F['errors']}:F['errors'].append(dict(tool_chunk=chunk,exit_code=code,stderr=err,execution_utc='UNRECORDED_PER_CALL',credit='No semantic credit for failed intended path or uncompleted metadata write. Other actually rendered valid outputs remain separate.'))
save('io/recent-read-failures.json',F)
print(json.dumps(dict(utc=NOW,old_pending_named_atoms_corrected=len(closures),stale_bucket_values_removed=list(replacement),full_R=sum(x['repo']=='R' for x in l['own_full_reads']),allparent_acceptances_unchanged=True)))
