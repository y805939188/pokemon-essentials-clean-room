from pathlib import Path
import json,subprocess,hashlib,difflib,re,datetime
r=Path('/workspace/pokemon-essentials-clean-room');base='8e67f780c204d593d89f364f585d2c6c2fe74631';old='5845e8084ced280e51c51a4081ec8583a9c2ca39';prev='1dc5cc80854e02965b9bb7a02c00a7c40d392f89';affected='4a75ca146e10062e469a42a9610bc3026861a34c';full='e03b7c2824105c5925cb9d64079bf653b03a41f4';ref='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';aroot='review/remediation/20261003-prepare/batches/B13/author-draft-1/';proot='review/remediation/20261003-prepare/batches/B13/candidate-1/';a=r/(aroot+'two-findings-repair-1');p=r/(proot+'two-findings-repair-1');a.mkdir(parents=True,exist_ok=True);p.mkdir(parents=True,exist_ok=True);prop=a/'original-scope-proposal-2';(prop/'proposed-after/specs/combat').mkdir(parents=True,exist_ok=True)
wp='deliverables/final-specification-set/combat-requirements/wp58-battle-recording-and-playback.md';cat='deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md';orig='specs/combat/wp58-battle-recording-and-playback.md'
def git(*args,repo=r):return subprocess.check_output(['git','-C',str(repo),*args])
def ident(d):return {'git_blob':subprocess.check_output(['git','hash-object','--stdin'],input=d,cwd=r).decode().strip(),'sha256':hashlib.sha256(d).hexdigest(),'bytes':len(d)}
def write(f,o):f.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
assert git('rev-parse','HEAD').decode().strip()==prev
# Read full concrete peer findings/reports, preserving their exact frozen bytes as read-only author inputs.
inputs=[]
for commit,path in [(affected,'review/remediation/20261003-prepare/batches/B13/affected-candidate-review-1/B09/report.md'),(affected,'review/remediation/20261003-prepare/batches/B13/affected-candidate-review-1/B09/result.json'),(affected,'review/remediation/20261003-prepare/batches/B13/affected-candidate-review-1/B11/report.md'),(affected,'review/remediation/20261003-prepare/batches/B13/affected-candidate-review-1/B11/result.json'),(affected,'review/remediation/20261003-prepare/batches/B13/affected-candidate-review-1/B11/finding-B029-entry-timing.json'),(full,'review/remediation/20261003-prepare/batches/B13/candidate-review-1/findings.json'),(full,'review/remediation/20261003-prepare/batches/B13/candidate-review-1/review-report.md')]:
 d=git('show',commit+':'+path);name=('affected-'+path.split('/')[-2]+'-' if commit==affected else 'FULL-')+path.split('/')[-1];(a/'review-inputs').mkdir(exist_ok=True);(a/'review-inputs'/name).write_bytes(d);inputs.append({'commit':commit,'path':path,**ident(d),'copy':str((a/'review-inputs'/name).relative_to(r)),'reviewed_OLD':old,'not_new_candidate_verdict':True})
write(a/'review-input-bindings.json',{'mode':'READ_ONLY_FROZEN_PEER_EVIDENCE_NO_REVIEW_SIGNATURE_BY_AUTHOR','inputs':inputs,'same_OLD_candidate':old,'formal_FIX_BASE':base,'public_peer_files_modified':False})
# New exact original proposal: only §5.2, from current already-authorized original bytes. It is not applied.
before=git('show',prev+':'+orig);assert (r/orig).read_bytes()==before
text=before.decode();start=text.index('换人询问返回队伍索引或取消−1',text.index('### 5.2'));end=text.index('\n\n### 5.3',start);oldclause=text[start:end]
newclause='''换人询问返回队伍索引或取消−1，返回即按发生时点追加同一换人序列。回合末对手／玩家补位与攻击阶段属主选择式替补均可达：训练家Teleport、U-turn/Flip Turn/Volt Switch、PartingShot（按实际换出者）、BatonPass、EjectButton，以及在攻击中触发的EjectPack、EmergencyExit/WimpOut，分别通过各自phase／owner／后备／生存／失败及追打等门后经pbGetReplacementPokemonIndex非随机分支到pbSwitchInBetween，回放同一消费者时点取值。对于这条攻击后替补路径，命令仍为原出招，清选择使替补当轮不再行动；不能把这条行动限定套到开场首命令前。

开场或普通换入的效果处理后，另有全场速度序最终退出扫描：逐成员先pbItemOnStatDropped，再pbAbilitiesOnDamageTaken，首个返回真即停止本次退出扫描。真实降阶且物品有效才消费EJECTPACK；真实跨过严格整数半HP且能力有效才消费EMERGENCYEXIT/WIMPOUT，仍须各自天空摔投、对侧未全灭、能换出及健康非蛋同属主未在场后备等门。非回合末时在入场消费者选择并追加，回放同点消费；开场初始属性快照先于正常入场，所以录制时这个选择可在首命令槽建立前追加，回放在首命令消费前从换人序列重取。清旧选择不表示新成员不能参加随后首命令；不是每次降阶或扣HP都立即触发这些退出。

EJECTPACK通过前置门后先消费物品再选择；负选择仍记入换人序列，退出处理返假、物品已耗而不提交替补，不回滚消费。退出能力负选择同样不提交替补，但没有该物品消费。回合末触发这两类退出时只召回／离场并返回真，选择留后段补位消费者，此退出处理器不立即询问／追加，不标作攻击阶段选择。

Roar/Whirlwind/DragonTail/CircleThrow与RedCard走随机分支，只有随机记录、不写询问序列。内部战斗门所限定的对手补位后换人风格确认在设施不可达（W16保持）。Arena正常顺序补位不询问，候选换入资格恒假使普通选择式退出不到询问。'''
proposed=(text[:start]+newclause+text[end:]).encode();target=prop/'proposed-after'/orig;target.write_bytes(proposed);patch=''.join(difflib.unified_diff(before.decode().splitlines(keepends=True),proposed.decode().splitlines(keepends=True),fromfile='a/'+orig,tofile='b/'+orig)).encode();(prop/'whole.patch').write_bytes(patch)
subprocess.run(['git','-C',str(r),'apply','--check','-'],input=patch,check=True,capture_output=True)
bl=text[:start].count('\n')+1;al=newclause.count('\n')+1
proposal={'status':'PENDING_NEW_EXACT_SOLE_REGISTRAR_SCOPE_CONFIRMATION_NOT_APPLIED','formal_FIX_BASE':base,'current_before_publication':prev,'reviewed_OLD':old,'finding_local_id':'B13-AFFECTED-F1','canonical_id':'GIR-FD82-B029','canonical_increment':0,'B030_increment':0,'old_permission':'2b23c82947bcecec4ab059d63048f9b67586575b applies only its fixed old4 patches; no extension reused','whole_patch':{'path':str((prop/'whole.patch').relative_to(r)),**ident(patch)},'records':[{'path':orig,'clause':'§5.2 entire sole paragraph replaced by phase-separated paragraphs; no other clause','before':{'commit':prev,'path':orig,**ident(before)},'before_line_range':[bl,bl+oldclause.count('\n')],'exact_before_clause':oldclause,'proposed_after':{'path':str(target.relative_to(r)),**ident(proposed)},'after_line_range':[bl,bl+al-1],'exact_after_clause':newclause,'write_authorized':False,'applied':False,'quality_PASS':None}],'B027_original_extension':False,'before_and_after_outside_clause_byte_equal':True,'git_apply_check':'PASS; check only','original_current_bytes_unchanged':True}
write(prop/'proposal.json',proposal)
(prop/'README.md').write_text(f'''# B029 入场时点原稿新精确提案 2

待唯一登记者确认，只改 `{orig}` §5.2，不应用。before绑定publication `{prev}` 当前原稿（既有四补丁已获准并应用）；正式FIX_BASE仍B12-C `{base}`。旧许可 `2b23c82947bcecec4ab059d63048f9b67586575b` 不扩展。

[逐条精确before/after及身份](proposal.json)；[whole patch](whole.patch)；[完整proposed-after](proposed-after/{orig})。whole SHA-256 `{hashlib.sha256(patch).hexdigest()}`，Git blob `{ident(patch)['git_blob']}`，{len(patch)}字节。仅同根B029入场时点、攻击行动限定、回合末延后及消费/取消边界；其他条款和W16/W24/W25不改，canonical及B030增量0。B027 nil修正不申请原稿扩围。

新metadata已确认scope段外原字节相同、patch可干净应用、当前原稿仍before；scope许可及质量PASS分别处理。父确认后才能应用固定新字节并重冻结完整候选，再由原独立FULL/B09/B11角色做增量复核。本提案没有质量签字。
''')
# Clear supersession: historical traces/statuses stay frozen; current successor fixes exact nil return identity.
trace=json.loads(git('show',prev+':'+aroot+'static-transition-traces.json'));trace['supersedes']={'commit':prev,'paths':[aroot+'static-transition-traces.json',aroot+'scope-applied-1/finding-dispositions-successor.json'],'scope':'Current nil return identity and item/ability entry timing only; all unaffected prior traces reused'}
for x in trace['entry_submission']:
 x['return_identity']='nil' if x['input']=='nil' else 'false'
 if x['input']=='nil':x['return']=None
 x['condition_truth_value']=False
trace['entry_submission'].append({'state':'active with registration=P and player=P','input':'nonempty list L object','submit':True,'registration':'same L','active_player':'same L','return':True,'return_identity':'true','condition_truth_value':True})
trace['entry_submission'].append({'state':'inactive with registration=P','input':'nil','submit':False,'registration':'P unchanged','active_player':'unchanged','return':None,'return_identity':'nil','condition_truth_value':False})
for x in trace['recording_caller_closure']:
 if x['effect']=='EJECTPACK':x['premises']='Real stat-drop flag and effective item; individual SkyDrop/opponent alive/trainer/leave/reserve gates. Entry or attack non-EOR owner choice; EOR recall/leave defers. Consume before choice; negative choice returns false but item remains consumed.'
 if x['effect']=='EMERGENCYEXIT/WIMPOUT':x['premises']='Strict integer-half crossing flag and effective ability; individual gates. Entry scan or attack non-EOR owner choice; EOR recall/leave defers. Do not generalize to every HP loss.'
trace['entry_final_scan']={'catalog':'RC-W26','mode':'UNEXECUTED_SYMBOLIC_INTERFACE_PRESTATE, not a generated behavior vector','preconditions':['Legal ordinary Tower trainer single, internalBattle=false','Normal opening attributes snapshot complete; no first command slot yet','Alive effective EJECTPACK holder, genuine entry stat-drop flag (qualifying actual opponent Intimidate drop); no SkyDrop, opponent party alive, can leave','Healthy non-egg same-owner off-field reserve index1; no earlier true exit in speed scan','Chosen reserve/entry chain causes no further exit or terminal decision'],'recording_checkpoints':[{'point':'initial attributes captured before startup','roundindex':-1,'rounds':[],'switches':[],'holder_item':'EJECTPACK'},{'point':'entry effects and final speed scan','real_stat_drop':True,'effective_item':True,'consumer_order':['stat-drop item','cross-half ability'],'per_battler_in_speed_order':True,'stop_at_first_true':True},{'point':'item after gates before owner query','holder_item':None,'consumed':True,'switches':[],'first_command_not_started':True},{'point':'owner returns1 during entry','switches':[1],'rounds':[],'roundindex':-1,'replacement_party_index':1,'old_choice_cleared':True},{'point':'after entry then first command','first_command_may_select_replacement_action':True,'not_forbidden_by_old_choice_clear':True}],'playback_checkpoints':[{'point':'initialize from pre-entry properties','holder_item':'EJECTPACK','switch_cursor':0,'roundindex':-1},{'point':'same entry item consumer','item_consumed_before_choice':True,'read_switches_at':0,'value':1,'switch_cursor_after':1,'random_sequence_for_selection':False,'live_owner_UI':False,'first_command_not_started':True},{'point':'first command afterwards','replacement_can_receive_first_command':True}],'nearby_controls':[{'case':'no real stat drop / inactive item / no legal reserve','owner_query':False,'no_query_record':True},{'case':'owner query negative -1 after EJECTPACK passed guards','switches_append':-1,'consumer_return':False,'item_consumed':True,'replacement_submitted':False,'no_consumption_rollback':True},{'case':'EOR item/ability exit','immediate_owner_query':False,'immediate_query_append':False,'recall_leave_now':True,'replacement_choice_consumer':'later actual replacement','append_consume_timing':'at later query'}, {'case':'qualified entry hazard half-crossing effective EmergencyExit/WimpOut','choice_timing':'entry final scan if individual trainer/leave/reserve gates pass','not_all_HP_loss':True}],'retained_existing_controls':['RC-W16 internalBattle false','RC-W24 attack BatonPass index1 and replacement no extra attack','RC-W25 random Roar/RedCard and Arena candidate=false'],'executed':False}
write(a/'static-transition-traces-successor.json',trace)
# Fresh limited source proof, no source body copied, no script execution.
ranges={
'Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb':('30-54','B027: return keeps nil input, empty list false; submit truthy list'),
'Data/Scripts/018_Alternate battle modes/001_Battle Frontier/001_Challenge_BattleChallenge.rb':('196-205','B027 active and inactive submission state'),
'Data/Scripts/016_UI/005_UI_Party.rb':('1051-1074;1103-1141','B027 normal cancellation returns nil; default UI validity remains'),
'Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb':('279-341','All-entry scan precedes first command; no startup attack slot'),
'Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb':('184-218;303-375','Replacement-helper nonrandom branch; entry final speed scan item-before-ability first true break'),
'Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb':('447-478','EJECTPACK guards, consume-before-choice, EOR defer, negative choice and clearing'),
'Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb':('367-409','Exit ability guards, entry/non-EOR choices vs EOR defer'),
'Data/Scripts/011_Battle/002_Battler/006_Battler_AbilityAndItem.rb':('41-55;380-395','Real event flags and current item/ability effectiveness before handler'),
'Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb':('1-91;112-191','Initial properties before normal startup; append every query; first slot command-time; playback cursor0 established before entry'),
'Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb':('1-52','Clear old choice only; future command availability remains governed by normal gates')}
source=[]
for f,(lines,purpose) in ranges.items():
 d=git('show',ref+':'+f,repo='/tmp/B13-reference-full');source.append({'repository':'fixed read-only reference','commit':ref,'path':f,'fresh_bounded_read_ranges':lines,'purpose':purpose,**ident(d),'whole_file_identity_not_full_read':True})
interfaces=[]
for f,lines,owner in [('deliverables/final-specification-set/combat-requirements/wp41-switching-positioning-and-escape.md','87-97','B09'),('deliverables/final-specification-set/combat-requirements/wp49-ability-phase-triggers.md','40-46;102-109','B11'),('deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md','20-26;113-118','B11')]:
 d=git('show',old+':'+f);assert (r/f).read_bytes()==d==git('show',base+':'+f);interfaces.append({'owner':owner,'commit':old,'FIX_BASE_commit':base,'path':f,'bounded_semantic_read_ranges':lines,**ident(d),'unchanged':True})
write(a/'source-and-consumer-navigation-successor.json',{'formal_FIX_BASE':base,'reviewed_OLD':old,'reference_commit':ref,'reference_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','fresh_bounded_records':source,'additional_review_discovered_current_interfaces':interfaces,'previous52_read_plan_and_complete8_controls':'Exact previous frozen bindings reused; these3 new necessary interface bounded reads are additive navigation, not a rewritten frozen plan or author permission to edit owners','B09_B11_attack_navigation_reused':'Current WP47-B exact binding in affected B11 result; unchanged attack W24/W25 proof retained, no full history reread','reference_runtime':0,'Ruby_game_vectors_old_programs_executed':0,'not_whole_source_or_search_coverage':True})
# Current eight-control author successor, preserving full fields; author's response is not a reviewer verdict.
disp=json.loads(git('show',prev+':'+aroot+'scope-applied-1/finding-dispositions-successor.json'));disp['current_repair_publication_parent']=prev;disp['reviewed_OLD']=old;disp['review_findings']=['B13-R01/GIR-FD82-B027','B13-AFFECTED-F1/GIR-FD82-B029'];disp['scope_blocker_resolved']=False;disp['current_original_scope_pending_only']=str((prop/'proposal.json').relative_to(r));disp['quality_PASS']=None
for x in disp['controls']:
 x['historical_current_disposition']={'commit':prev,'path':aroot+'scope-applied-1/finding-dispositions-successor.json','id':x['id'],'local_disposition':x['local_disposition']}
 if x['id']=='GIR-FD82-B027':
  x['local_disposition']='nil不提交、保留报名P与活动P，正常包装精确返回nil（JSON null，return_identity=nil）；空列表提交、立即活动空且返回布尔false；非空列表提交并返回true。falsey不替代返回身份；WS-W35与当前轨迹同改，WP55及旧W28/W29保持，默认UI人数门不扩大。'
  x['current_return_oracle']='static-transition-traces-successor.json replaces old /entry_submission/1/return false with null and explicit nil; no original scope extension'
 if x['id']=='GIR-FD82-B029':
  x['local_disposition']='完整询问域补开场/普通入场最终扫描；按速度逐成员item降阶在先、half能力在后、首个真即停。非EOR在实际入场消费者选择并记录/回放，开场可在首命令槽前；攻击后不再行动限定仅该攻击路径。EOR只召回离场、选择延后；EJECTPACK先消费再选、负选已耗但无替补，-1仍记录。W16/W24/W25与Arena随机/候选门保持，新增未执行W26。'
  x['author_only_status']='FINAL_ENTRY_TIMING_REPAIRED; ORIGINAL_NEW_EXACT_SCOPE_PENDING';x['current_original_scope_proposal']=proposal
 if x['id']=='GIR-FD82-B018':x['local_disposition']+=' 本轮新增未执行RC-W26，现47+35+28+27=137，旧127→新增10；历史136保持当时身份，不改旧报告。'
 for loc in x.get('final_locations',[]):
  if loc['path'] in [wp,cat]:
   loc['previous_output_binding']={'commit':prev,'output':loc['output']};loc['output']=ident((r/loc['path']).read_bytes())
 x['current_trace_entry']=str((a/'static-transition-traces-successor.json').relative_to(r));x['quality_PASS']=None;x.pop('independent_review_started',None);x['new_repair_independent_review_started']=False;x['independent_review_started_by_author']=False;x['OLD_review_status']='Exact OLD reports completed: FULL NEEDS_REVISION / affected B09+B11 REQUEST_CHANGES; no new repair verdict'
write(a/'finding-dispositions-successor.json',disp)
# New metadata verifies strictly limited formal delta and complete old catalog row protection.
def rows(s):
 sec=None;out={}
 for l in s.splitlines():
  if l.startswith('## '):sec=l.split('：')[0][3:]
  if re.match(r'^\| (?:Q\d+|W\d+\w*|P\d+) \|',l):out.setdefault(sec,[]).append(l)
 return out
o=rows(git('show',prev+':'+cat).decode());n=rows((r/cat).read_text());changes=[];adds=[]
for sec,rr in o.items():
 oldids=[l.split('|')[1].strip() for l in rr];newids=[l.split('|')[1].strip() for l in n[sec]];assert [i for i in newids if i in oldids]==oldids
 for l in rr:
  id=l.split('|')[1].strip();newl=next(z for z in n[sec] if z.split('|')[1].strip()==id)
  if l!=newl:changes.append({'series':sec,'id':id,'before':l,'after':newl})
 for l in n[sec]:
  id=l.split('|')[1].strip()
  if id not in oldids:adds.append({'series':sec,'id':id,'row':l,'executed':False})
assert [(x['series'],x['id']) for x in changes]==[('WS','W35')];assert [(x['series'],x['id']) for x in adds]==[('RC','W26')]
assert {k:len(v) for k,v in n.items()}=={'QC':47,'WS':35,'PA':28,'RC':27}
oldwp=git('show',prev+':'+wp).decode();newwp=(r/wp).read_text();assert oldwp[:oldwp.index('### 5.2')]==newwp[:newwp.index('### 5.2')];assert oldwp[oldwp.index('### 5.3'):oldwp.index('## 7.')]==newwp[newwp.index('### 5.3'):newwp.index('## 7.')];assert oldwp[oldwp.index('## 8.'):] ==newwp[newwp.index('## 8.'):]
for f in git('diff','--name-only',base,prev).decode().splitlines():
 if f not in [wp,cat]:assert (r/f).read_bytes()==git('show',prev+':'+f),f
assert (r/orig).read_bytes()==before
actual=git('diff','--name-only',prev).decode().splitlines();assert actual==sorted([wp,cat])
check=subprocess.run(['git','-C',str(r),'diff','--check',prev,'--',wp,cat],capture_output=True,text=True);assert check.returncode==0,check.stdout
write(a/'repair-metadata-verification.json',{'kind':'NEW_TEXT_GIT_JSON_HASH_METADATA_ONLY_NO_BEHAVIOR_EXECUTION','formal_FIX_BASE':base,'OLD':old,'prior_publication':prev,'direct_changed_formal_paths':[wp,cat],'no_original_applied':True,'all_four_existing_originals_previous_bytes':True,'all_other_previous72_output_files_byte_equal':True,'catalog_old_ID_order_and_multiplicity_preserved':True,'changed_existing_rows':changes,'new_unexecuted_rows':adds,'WS_W28_W29_RC_W16_W24_W25_and_all_other_rows_unchanged':True,'counts_previous':{'QC':47,'WS':35,'PA':28,'RC':26,'total':136},'counts_now':{'QC':47,'WS':35,'PA':28,'RC':27,'total':137},'old_frozen_catalog':127,'new_total_delta_from_old':10,'old_complete8_5_controls_retained':True,'11_previous_outputs_scope_retained':True,'original_new_scope_pending':True,'formal_git_diff_check':'PASS','runtime_vectors_reference_Ruby_old_programs':0,'B030_required':False,'canonical_increment':0,'independent_quality_verdict':None})
issues={'B13-R01':{'canonical':'GIR-FD82-B027','review_commit':full,'review_path':'review/remediation/20261003-prepare/batches/B13/candidate-review-1/findings.json','minimum_map':[{'requirement':'WS-W35 exact nil vs false','output':cat,'clause':'WS-W35'},{'requirement':'nil JSON null and explicit identity','output':str((a/'static-transition-traces-successor.json').relative_to(r)),'pointer':'/entry_submission/1/return'},{'requirement':'current B027 disposition','output':str((a/'finding-dispositions-successor.json').relative_to(r)),'id':'GIR-FD82-B027'}],'original_scope_new':False,'author_response':'Applied final-row and current successor corrections; frozen old trace unchanged','quality_PASS':None},'B13-AFFECTED-F1':{'canonical':'GIR-FD82-B029','review_commit':affected,'review_path':'review/remediation/20261003-prepare/batches/B13/affected-candidate-review-1/B11/finding-B029-entry-timing.json','minimum_map':[{'requirement':'phase-separated entry final scan and attack-only no-action condition','output':wp,'clause':'§5.2'},{'requirement':'one unexecuted entry contrast','output':cat,'clause':'RC-W26'},{'requirement':'static transition trace and current consumer navigation','outputs':[str((a/'static-transition-traces-successor.json').relative_to(r)),str((a/'source-and-consumer-navigation-successor.json').relative_to(r))]},{'requirement':'original synchronization only after new exact scope','proposal':str((prop/'proposal.json').relative_to(r)),'status':'PENDING_NOT_APPLIED'}],'author_response':'Final repaired; exact single WP58 original proposal published for sole registrar confirmation','quality_PASS':None}}
write(a/'two-findings-repair-map.json',{'role':'AUTHOR_RESPONSE_NOT_INDEPENDENT_REVIEW','reviewed_OLD':old,'issues':issues,'complete_original8_controls_retained':True,'canonical_increment':0,'B030_increment':0,'old_reviewers_inputs_unchanged':True,'FULL_old_report_does_not_overrule_affected_entry_scope':'FULL B029 local judgment and affected B029 entry omission treated as finite combined revision; neither authored or re-signed here','independent_recheck_after_scope':['Original FULL R-B13 nil oracle and retained8/5','Original affected B09 and B11 entry/record finite interfaces'],'old_other_affected_verdicts':'B10/B12 PASS_SCOPED; B02/B03/B04/B07/B08/B14/B15 NOT_AFFECTED only at OLD; no new candidate re-signature by author','G_actual_C_pending':True,'B16_WP67A_nonlocal_unchanged':True})
# Accurate current input list adds WP41/WP49/WP50 main, with current identities and owner scope.
write(a/'affected-inputs-successor.json',{'role':'AUTHOR_NAVIGATION_ONLY','OLD':old,'preserved_old_finite_map':{'commit':prev,'path':aroot+'scope-applied-1/affected-interface-scope-successor.json'},'new_current_read_only_interfaces':interfaces,'unchanged_WP47B_binding_from_review':{'owner':'B11','commit':old,'path':'deliverables/final-specification-set/combat-requirements/wp47-b-switching-control-and-item-changes.md',**ident(git('show',old+':deliverables/final-specification-set/combat-requirements/wp47-b-switching-control-and-item-changes.md'))},'necessary_incremental_review_navigation':['R-B13 B027 exact return oracle with complete retained8/5','B09 WP41 §4.2 and WP58 entry before command','B11 WP49 final scan and WP50 EJECTPACK effective/consume/EOR/choice','Other old owner results remain exact OLD; parent decides supported reuse/delta needs, author does not sign'],'candidate_and_actual_separate':True,'owner_formal_writes':0,'author_NOT_AFFECTED_or_PASS':False})
write(a/'current-output-identities.json',{'formal_FIX_BASE':base,'OLD':old,'current_before_publication':prev,'direct_repair_outputs':[{'path':f,'before':{'commit':prev,**ident(git('show',prev+':'+f))},'after':ident((r/f).read_bytes())} for f in [wp,cat]],'single_proposed_original':proposal['records'][0],'all_other_previous_outputs_unchanged':True,'original_current_before_still_unchanged':True,'quality_PASS':None})
(a/'author-report.md').write_text('''# B13 两项有限返修及原稿新范围提案

当前仅作者返修／提案，非独立PASS。正式FIX_BASE仍B12-C `8e67f780c204d593d89f364f585d2c6c2fe74631`；两份review均审旧候选 `5845e8084ced280e51c51a4081ec8583a9c2ca39`，其输入未改。父要求把FULL B13-R01/B027及affected B13-AFFECTED-F1/B029一次整理，canonical增量0、B030不计。

B027：源正常回调的nil左值原样返回；空列表对象提交后返回false。仅新增WS-W35及当前轨迹／B027处置返修：JSON null+return_identity=nil，falsey另列，不覆盖历史冻结证据。WP55、旧W28/W29、进行中／未进行中状态与默认UI人数门保留；无B027原稿新扩围。

B029：独立定点核实初始属性快照先于正常入场，入场最终全场速度扫描先真实降阶物品、再跨严格整数半HP能力，首个真停止；非EOR的选择可在首命令槽之前追加／回放同点消费。攻击后清选择不再行动限定仅用于已有攻击；开场清旧选择不取消随后首命令。EOR只召回离场、询问留后段；EJECTPACK先耗后选、负选返假却已耗，负值仍记录。净WP58§5.2分开这些时点，保留随机／Arena／W16，补未执行RC-W26；WP58§7/目录只同步数量和导航，现137静态设计（旧136+1，初始127+10），没有执行向量。

[两问题映射](two-findings-repair-map.json)逐条连到最小返修；[当前轨迹](static-transition-traces-successor.json)明确替代旧nil false oracle及未覆盖的entry timing；[当前8项处置](finding-dispositions-successor.json)保留完整原控制、root/extension、有效反例、最低验收、非本地义务及主责计数，不用两个focus代替8/5。[来源及consumer导航](source-and-consumer-navigation-successor.json)记录准确fresh局部范围、current WP41/WP49/WP50主稿三个必要只读增量，未扩大owner写入或重新阅读全历史。

唯一待许可原稿是 [WP58§5.2新精确提案](original-scope-proposal-2/README.md)，before绑定当前1dc5cc8原稿、完整after和whole.patch逐字绑定。旧四补丁许可仅保留旧字节，不延伸；本轮未在原稿树应用新补丁。父必须先确认这个新scope，随后作者可应用固定字节、重冻结完整候选，原独立FULL及B09/B11做OLD→NEW有限复核。当前净稿／原稿尚未同步，不能给完整验收或G/C。

[新metadata](repair-metadata-verification.json)确认只有2正式路径变化，旧目录全部ID顺序/多重性、W16/W24/W25/W28/W29及他方行保持；仅改新增WS-W35、加RC-W26，其余所有旧输出与四原稿保持。所有已冻结报告/许可/输入原件保留，不向reviewer旧candidate写入。

全部源限制与U01–U10/G01–G12/AX01–AX20、树果条件67、具名未读内容、B16 WP67-A与双向依赖保持；无reference/Ruby/game/行为向量/历史程序执行，只本轮新文本／Git／JSON／SHA元数据。无main／公共登记／reference写入，无自开review任务、无质量签字。新publication及OLD→NEW完整未过滤流与远端ref/FETCH_HEAD/tree/全部输出读回在 [当前返修入口](../../candidate-1/two-findings-repair-1/review-dispatch.md) 后继收据中。
''')
(p/'review-dispatch.md').write_text('''# B13 两问题增量返修入口（待单独原稿scope）

当前返修同时回应旧候选 `5845e8084ced280e51c51a4081ec8583a9c2ca39` 的 FULL `B13-R01/B027` 和 affected `B13-AFFECTED-F1/B029`。完整两问题映射：[author map](../../author-draft-1/two-findings-repair-1/two-findings-repair-map.json)。新精确repair/proposal SHA/tree、publication与OLD→NEW完整未过滤流见本目录后继 `publication-receipt.json`。

先由唯一登记者确认 [WP58原稿§5.2新的精确before／whole patch／after提案](../../author-draft-1/two-findings-repair-1/original-scope-proposal-2/README.md)。旧 `2b23c8` scope不扩展。本次只直接修净WP58时点及新增WS35精确nil返回、RC26未执行入场对照；原稿当前字节未动，所以本发布是有限返修／新scope提案，尚非完整原/净同步可接受候选。

确认后应用固定新补丁并重冻结完整候选，由父协调原 R-B13 FULL 和 affected B09/B11 做增量复核。FULL仍覆盖全部8贡献／5主责与完整原qualified/root/扩展前提、最小反例和验收；新增两问题不是替代整批门。当前 [8项作者处置](../../author-draft-1/two-findings-repair-1/finding-dispositions-successor.json)、[精确nil及入场轨迹](../../author-draft-1/two-findings-repair-1/static-transition-traces-successor.json)、[consumer导航](../../author-draft-1/two-findings-repair-1/source-and-consumer-navigation-successor.json)明确替代旧相应状态与oracle；历史报告原件保持，不是作者PASS。

B09/B11需核WP41、WP49、WP50主稿入场最终扫描／consume-before-choice／EOR延后和首命令前记录消费。W16/W24/W25、随机/Arena、B025终局/其它前8/5保持。旧B10/B12 PASS及其余NOT_AFFECTED仅签旧candidate，由父/独立角色决定精确新增量可复用哪些门，作者不代签。actual独立FULL/分别必要affected及两未过滤流、G/C和canonical非本地全局义务保持，B16不释放、B030计数0。

新增及全部137项设计未执行；fresh阅读只本次具体证据和必要局部源/accepted合同，无全历史复读、无参考/Ruby/游戏/历史程序或向量运行。所有继承限制保持。
''')
write(p/'review-dispatch.json',{'status':'LIMITED_COMBINED_REPAIR_AND_NEW_ORIGINAL_PROPOSAL_PENDING_SOLE_REGISTRAR_SCOPE','formal_FIX_BASE':base,'formal_FIX_BASE_tree':'ae2f491294eb4f97be6b75f75706c16279f9bf46','OLD_candidate':old,'OLD_tree':'23f92a9c446f5f0fbcee44df2f57d85df4dd0e3c','prior_publication':prev,'two_reports':{'FULL':full,'affected':affected},'issues':['B13-R01/B027','B13-AFFECTED-F1/B029'],'two_problem_map':str((a/'two-findings-repair-map.json').relative_to(r)),'original_scope_pending':proposal,'canonical_increment':0,'B030_increment':0,'complete8_contribution5_primary_controls_retained':True,'new_count_static':137,'runtime_vectors':0,'parent_only_original_scope_confirmation_then_apply_and_refreeze':True,'required_incremental_roles':['Original independent R-B13 FULL with complete8/5','Original independent affected B09','Original independent affected B11'],'author_review_signature':False,'extra_tasks_spawned':0,'quality_PASS':None,'G':False,'C':False,'B16_release':False,'publication_binding':'Exact new repair/proposal SHA/tree and full OLD->NEW/prev-publication->NEW/FIX_BASE->NEW stream identities plus independent remote readback in following receipt','effective_configuration':'Requested original xhigh author/ultra independent, default/Standard; effective UNVERIFIED, no CLI/native/quota audit or fallback'})
(a/'new-repair-metadata.py').write_bytes(Path('/tmp/B13-two-findings-repair-20261010.py').read_bytes())
# Only narrow formal convenience diff now. Full unfiltered OLD->NEW stream frozen after commit and published separately.
(p/'two-formal-repair.patch').write_bytes(git('diff','--binary','--no-ext-diff','--no-textconv',prev,'--',wp,cat))
for f in list(a.glob('*.md'))+list(p.glob('*.md'))+[prop/'README.md']:
 for link in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  if '://' not in link:assert (f.parent/link).exists(),(f,link)
new=sorted([r/wp,r/cat]+[f for d in [a,p] for f in d.rglob('*') if f.is_file() and f.name!='output-inventory.json']);write(p/'output-inventory.json',{'kind':'PRECOMMIT_REPAIR_PAYLOAD_IDENTITIES_NO_SELF_HASH','prior_publication':prev,'OLD':old,'records':[{'path':str(f.relative_to(r)),**ident(f.read_bytes())} for f in new],'self_inventory_excluded_only':True,'old72_outputs_except2_formal_unchanged':True})
print('Prepared combined B027/B029 finite repair:2 formal paths; old rows exceptWS35 preserved;RC26 added,total137 unexecuted;single WP58 original proposal PENDING;wholepatch',hashlib.sha256(patch).hexdigest(),'bytes',len(patch),'new payload',len(new)+1)
