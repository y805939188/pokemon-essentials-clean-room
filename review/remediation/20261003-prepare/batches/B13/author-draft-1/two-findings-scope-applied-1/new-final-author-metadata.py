import pathlib,subprocess,json,hashlib,copy,re,datetime
repo=pathlib.Path('/workspace/pokemon-essentials-clean-room')
base='8e67f780c204d593d89f364f585d2c6c2fe74631';old='5845e8084ced280e51c51a4081ec8583a9c2ca39';prior='c52c0df80bcba45ac77f8da2cdee264890846327';repair='235c9a599f20346bf82add2fa1d7220f5bfacdb2';scope='231c9f25df4dd64961fb9290ff52302782a9fdb8'
root=pathlib.Path('review/remediation/20261003-prepare/batches/B13')
prev=root/'author-draft-1/two-findings-repair-1';a=root/'author-draft-1/two-findings-scope-applied-1';c=root/'candidate-1/two-findings-scope-applied-1'
(repo/c).mkdir(parents=True,exist_ok=True)
original='specs/combat/wp58-battle-recording-and-playback.md'
net='deliverables/final-specification-set/combat-requirements/wp58-battle-recording-and-playback.md'
catalog='deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md'
def git(*args):return subprocess.run(['git',*args],cwd=repo,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True).stdout
def ident(b):return {'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
def read(p):return (repo/p).read_bytes()
def jread(p):return json.loads(read(p))
def write(p,d):
 out=repo/p;out.parent.mkdir(parents=True,exist_ok=True)
 out.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n' if not isinstance(d,str) else d)
def binding(p,commit=prior):return {'commit':commit,'path':str(p),**ident(git('show',commit+':'+str(p)))}
def names(x,y):return sorted(git('diff','--name-only','-z',x,y).decode().rstrip('\0').split('\0'))
assert git('rev-parse','HEAD').decode().strip()==prior
assert git('diff','--name-only').decode().splitlines()==[original]
receipt=jread(a/'scope-application-receipt.json');assert receipt['applied'] and receipt['entire_file_exact_after_equal']
assert ident(read(original))==receipt['actual_after']
# Read and protect every prior published output, not merely selected formal paths.
previous_outputs=names(base,prior);assert len(previous_outputs)==100
protected=[]
for p in previous_outputs:
 before=git('show',prior+':'+p);after=read(p)
 if p==original:assert ident(before)=={k:receipt['before'][k] for k in ['git_blob','sha256','bytes']};assert ident(after)==receipt['actual_after']
 else:assert before==after,p
 protected.append({'path':p,'before':ident(before),'current':ident(after),'byte_equal':before==after,'authorized_fixed_scope2_original_change':p==original})
# Maintain the full 8 contributions / 5 primary controls, all original/current fields and gates.
previous_dispositions=jread(prev/'finding-dispositions-successor.json')
d=copy.deepcopy(previous_dispositions)
d['historical_scope_amendment']=d['scope_amendment'];d['scope_amendment']=scope
d['historical_previous_frozen_author_publication']=d['previous_frozen_author_publication'];d['previous_frozen_author_publication']=prior
d['current_repair_publication_parent']=prior;d['current_original_scope_pending_only']=None;d['scope_blocker_resolved']=True
d['scope_application_receipt']=str(a/'scope-application-receipt.json')
d['complete_source_controls_and_52_navigation_reused_without_reexecution']=True
d['original_scope_application_fields_are_frozen_scope1_history']=True
d['current_original_and_final_output_identities']=str(a/'all-11-formal-output-identities.json')
for item in d['controls']:
 item['current_disposition_previous_binding']={'commit':prior,'path':str(prev/'finding-dispositions-successor.json'),'id':item['id']}
 item['current_source_trace']=binding(prev/'static-transition-traces-successor.json')
 item['current_source_consumer_navigation']=binding(prev/'source-and-consumer-navigation-successor.json')
 if item['id']=='GIR-FD82-B029':
  item['author_only_status']='COMPLETE_LOCAL_AUTHOR_REPAIR_AND_EXACT_SCOPE2_ORIGINAL_SYNC_SUBMITTED_FOR_INDEPENDENT_RECHECK'
  item['historical_pending_original_proposal']=item.pop('current_original_scope_proposal')
  item['current_original_scope_application']={'scope_commit':scope,'scope_json_path':'review/remediation/20261003-prepare/batches/B13/scope-amendment-2/scope-amendment.json','receipt':str(a/'scope-application-receipt.json'),'original_path':original,'clause':'§5.2','before':receipt['before'],'applied_after':receipt['actual_after'],'whole_patch':receipt['source_whole_patch'],'applied':True,'quality_PASS':None}
  item['final_locations'].append({'path':original,'clauses':'§5.2 exact scope-amendment-2 only','output':receipt['actual_after']})
  item['local_disposition']+=' 原稿§5.2现按scope-amendment-2精确whole.patch同步；before/whole/after全文件身份及条款外字节匹配。历史pending提案保持冻结，仅本successor标应用。'
  item['source_chain_evidence']=str(prev/'static-transition-traces-successor.json')+' and '+str(prev/'source-and-consumer-navigation-successor.json')+'; exact fixed static reads reused, no runtime'
  item['remaining_required_gaps']=['Original independent Ultra FULL complete8/5 and original affected B09/B11 necessary incremental recheck at exact NEW candidate; no author quality verdict','Only after candidate gates G; separate exact actual FULL/affected, then sole registrar C; all nonlocal/global canonical obligations retained']
 assert item['quality_PASS'] is None and item['canonical_state']=='OPEN'
assert len(d['controls'])==8 and sum(x['primary'] for x in d['controls'])==5
for before,after in zip(previous_dispositions['controls'],d['controls']):
 assert before['id']==after['id']
 for k in ['whole_control','original_required_fields','current_required_fields','whole_extensions_and_root_adjudications','approved_acceptance_gate','catalog_series_ids','accepted_B13_contributions']:
  assert before[k]==after[k],(before['id'],k)
write(a/'finding-dispositions-successor.json',d)
# Successor response maps both issues, and the exact original application, with no review signature.
m=jread(prev/'two-findings-repair-map.json');m=copy.deepcopy(m)
m['previous_repair_map']=binding(prev/'two-findings-repair-map.json')
m['issues']['B13-R01']['minimum_map'][2]['output']=str(a/'finding-dispositions-successor.json')
x=m['issues']['B13-AFFECTED-F1'];x['author_response']='Final WP58 entry timing and original §5.2 now synchronized by exact granted fixed patch; submitted for independent incremental review'
x['minimum_map'][3].update({'status':'EXACT_SCOPE2_GRANTED_AND_APPLIED_NOT_QUALITY_PASS','scope_commit':scope,'original_output':original,'application_receipt':str(a/'scope-application-receipt.json')})
m['scope_pending']=False;m['new_original_application_complete']=True;m['quality_PASS']=None
write(a/'two-findings-repair-map-successor.json',m)
# Preserve the completed bounded source analysis rather than run historical author/reviewer programs.
evidence_paths=[prev/'review-input-bindings.json',prev/'static-transition-traces-successor.json',prev/'source-and-consumer-navigation-successor.json',prev/'affected-inputs-successor.json',root/'author-draft-1/original-and-acceptance-controls.json',root/'author-draft-1/bounded-input-navigation.json',root/'author-draft-1/B13-downstream-contract.json',root/'author-draft-1/inherited-source-limits.json',root/'author-draft-1/catalog-preservation.json',root/'author-draft-1/scope-applied-1/affected-interface-scope-successor.json']
evidence={'role':'AUTHOR_EXACT_EVIDENCE_REUSE_INDEX_NO_NEW_EXECUTION_OR_INDEPENDENT_VERDICT','formal_FIX_BASE':base,'reviewed_OLD':old,'previous_repair_commit':repair,'previous_publication':prior,'references':[binding(p) for p in evidence_paths],'current_dispositions':str(a/'finding-dispositions-successor.json'),'supersession':['Historical nil=false trace is frozen evidence only; current exact oracle is corrected successor /entry_submission/1: JSON null, return_identity=nil','Historical scope pending proposal remains immutable; current original application is scope-application-receipt.json'],'full8_5_current_control_objects_preserved':True,'52_read_navigation_reused':True,'reference_commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','reference_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','U01_U10_G01_G12_AX01_AX20_and_unread_domains_retained':True,'execution_count':0,'historical_author_reviewer_programs_run':False,'effective_backend':'UNVERIFIED; requested author xhigh and independent ultra default/Standard; no probing or fallback'}
write(a/'current-evidence-index.json',evidence)
trace=jread(prev/'static-transition-traces-successor.json')
assert trace['entry_submission'][1]['return'] is None and trace['entry_submission'][1]['return_identity']=='nil'
assert trace['entry_submission'][0]['return'] is False and trace['entry_submission'][0]['return_identity']=='false'
assert trace['executed_vectors']==0
# Compare all catalog rows and identities against OLD and preceding repair publication.
def rows(b):
 result=[];series=None
 for line in b.decode().splitlines():
  h=re.match(r'^## (QC|WS|PA|RC)：',line)
  if h:series=h.group(1)
  match=re.match(r'^\| ((?:Q|W|P)\d+b?) \|',line)
  if match:result.append((series,match.group(1),line))
 return result
oldrows=rows(git('show',old+':'+catalog));nowrows=rows(read(catalog));priorrows=rows(git('show',prior+':'+catalog))
assert len(oldrows)==136 and len(nowrows)==137 and priorrows==nowrows
assert len({(s,i) for s,i,_ in nowrows})==137
oldmap={(s,i):line for s,i,line in oldrows};nowmap={(s,i):line for s,i,line in nowrows}
changed=[{'series':s,'id':i,'before':line,'after':nowmap[s,i]} for (s,i),line in oldmap.items() if line!=nowmap[s,i]]
assert [(r['series'],r['id']) for r in changed]==[('WS','W35')]
assert [x[:2] for x in nowrows if x[:2] in oldmap]==[x[:2] for x in oldrows]
added=[{'series':s,'id':i,'row':line,'executed':False} for s,i,line in nowrows if (s,i) not in oldmap]
assert [(r['series'],r['id']) for r in added]==[('RC','W26')]
counts={s:sum(row[0]==s for row in nowrows) for s in ['QC','WS','PA','RC']};assert counts=={'QC':47,'WS':35,'PA':28,'RC':27}
formal_paths=[p for p in previous_outputs if p.startswith(('specs/','deliverables/'))];assert len(formal_paths)==11
all11=[{'path':p,'output':ident(read(p)),'previous_publication_output':ident(git('show',prior+':'+p)),'same_as_previous':read(p)==git('show',prior+':'+p)} for p in formal_paths]
write(a/'all-11-formal-output-identities.json',{'formal_FIX_BASE':base,'previous_publication':prior,'outputs':all11,'only_direct_formal_changed_since_publication':original,'OLD_to_current_formal_changes':[catalog,net,original]})
# Accepted B09/B11 contracts and old source inputs stay byte-identical.
interfaces=jread(prev/'affected-inputs-successor.json');interface_records=[]
for rec in interfaces['new_current_read_only_interfaces']:
 p=rec['path'];actual=read(p);assert actual==git('show',old+':'+p)==git('show',base+':'+p)
 assert ident(actual)=={k:rec[k] for k in ['git_blob','sha256','bytes']}
 interface_records.append({'path':p,'owner':rec['owner'],'identity':ident(actual),'same_as_OLD_FIX_BASE':True,'writes':False})
wp47=interfaces['unchanged_WP47B_binding_from_review'];p=wp47['path'];assert read(p)==git('show',old+':'+p)
interface_records.append({'path':p,'identity':ident(read(p)),'same_as_OLD':True,'writes':False})
write(a/'affected-interface-navigation-successor.json',{'role':'AUTHOR_NAVIGATION_ONLY_NOT_AFFECTED_VERDICT','previous_complete_affected_map':binding(prev/'affected-inputs-successor.json'),'current_read_only_interfaces':interface_records,'necessary_incremental_roles':['Original independent FULL R-B13 complete8/5','Original independent affected reviewer B09','Original independent affected reviewer B11'],'all_other_finite_domains':'Old B10/B12 PASS_SCOPED and B02/B03/B04/B07/B08/B14/B15 NOT_AFFECTED apply only exact OLD; necessary new candidate disposition belongs to original independent affected role','candidate_and_actual_separate':True,'owner_writes':False,'author_quality_signature':False,'B16_WP67A_unchanged':True})
protected_current={'kind':'NEW_GIT_JSON_HASH_TEXT_METADATA_ONLY_NOT_BEHAVIOR_TEST','formal_FIX_BASE':base,'OLD':old,'previous_publication':prior,'scope_commit':scope,'scope2_fixed_patch_applied':True,'current_original_entire_after_identity':receipt['actual_after'],'only_tracked_change_from_prior':original,'all100_previous_outputs_actual_byte_comparison':protected,'99_other_previous_outputs_byte_equal':True,'all11_formal_outputs':all11,'entire_reference_main_public_registration_and_history_outside_own_dirs_unchanged':True,'old_pending_proposal_and_old_review_input_copies_preserved':True,'full8_contributions5_primary_original_current_fields_gates_preserved':True,'current_nil_identity':{'JSON_return':None,'return_identity':'nil','list_empty_return':False,'condition_truth_values_both_false':True},'catalog_total_OLD':136,'catalog_total_current':137,'catalog_counts':counts,'changed_existing_rows_from_OLD':changed,'new_rows_from_OLD':added,'all_other_OLD_row_bytes_and_order_multiplicity_preserved':True,'WS_W28_W29_RC_W16_W24_W25_bytes_preserved':True,'current_catalog_unchanged_from_repair_publication':True,'accepted_interfaces_preserved':interface_records,'behavior_runtime_vectors_executed':0,'reference_Ruby_game_historical_programs_executed':False,'independent_quality_verdict':None,'canonical_increment':0,'B030_increment':0,'G':False,'C':False,'B16_release':False}
write(a/'protection-and-metadata-verification.json',protected_current)
write(a/'author-report.md',f'''# B13 两问题返修最终作者提交\n\n作者角色仅 A-B13；正式 FIX_BASE `{base}` / tree `ae2f491294eb4f97be6b75f75706c16279f9bf46`。管理许可 `{scope}` 仅读取、核对，未合并或作为正式基线。\n\nB13-R01 / GIR-FD82-B027 的 WS-W35 和当前静态轨迹已于 `{repair}` 修正：nil取消返回 JSON null / return_identity=nil，空列表提交返回布尔false，二者条件真值虽假但返回身份不同；活动队伍/报名后态、默认UI人数门及旧WS-W28/W29保持。本次这些返修字节全部保留，无新增B027原稿范围。\n\nB13-AFFECTED-F1 / GIR-FD82-B029 的净稿、未执行RC-W26、入场最终扫描静态轨迹及WP41/WP49/WP50消费者导航已于 `{repair}` 修订。本次在整个before身份匹配后，精确应用固定 whole.patch SHA256 `8d186d65c9eb2bc0e03a27728bfa0ea8476f4753bb863054b41cdb3b79459b0d` 到原稿WP58 §5.2；整文件after为 `0dbd9207664b04d6ea869c5252bb91c8f4559eff0072656ea733f0a4043b5bc4`，其余条款字节保持。许可仅范围，质量仍未裁定。\n\n当前主入口是本目录 finding-dispositions-successor.json / two-findings-repair-map-successor.json / current-evidence-index.json。完整8贡献/5主责的原始、批准、current qualifications、root adjudications、extensions、effective case constraints和验收门精确复用原控制对象；52读导航及源限制保持。历史pending/旧nil假值和旧评审输出均为冻结证据，不是当前预期或新候选质量签署。\n\ncatalog共137静态设计：QC47、WS35、PA28、RC27，全部未执行。相对OLD `{old}` 只改变WS-W35，新增RC-W26，OLD的136个原ID保留，除WS-W35外其它行字节保持；W16/W24/W25与WS-W28/W29保持。相对上一publication的100输出仅原稿WP58改变，其余99全部实际字节比对一致。公开登记、main、reference、B09/B11正文、历史报告未改。\n\n交父任务协调原Ultra FULL complete8/5和原affected B09/B11做精确NEW增量复核；本作者不代签、不新开复审任务。OLD两份结论只绑定OLD；新scope不表示PASS。G/actual FULL+affected/C仍后续独立门，canonical/B030增量0、B16/WP67-A依赖保持。\n\n仅新Git/JSON/hash/补丁文本元数据核验；未运行参考、Ruby、游戏、行为向量或历史作者/reviewer程序。源U01–U10/G01–G12/AX01–AX20及未读素材限制延续，backend有效档位仍UNVERIFIED，无探测或fallback。\n''')
review={'status':'FINAL_COMBINED_TWO_FINDINGS_AUTHOR_CANDIDATE_SCOPE2_APPLIED_AWAITING_ORIGINAL_INDEPENDENT_INCREMENTAL_REVIEW','role':'AUTHOR_DISPATCH_NAVIGATION_ONLY','formal_FIX_BASE':base,'formal_FIX_BASE_tree':'ae2f491294eb4f97be6b75f75706c16279f9bf46','OLD_candidate':old,'OLD_tree':'23f92a9c446f5f0fbcee44df2f57d85df4dd0e3c','prior_repair_candidate':repair,'prior_publication':prior,'scope_amendment2':scope,'scope2_applied':True,'scope_quality_PASS':None,'current_dispositions':str(a/'finding-dispositions-successor.json'),'two_problem_map':str(a/'two-findings-repair-map-successor.json'),'scope_application':str(a/'scope-application-receipt.json'),'complete_evidence_index':str(a/'current-evidence-index.json'),'protections':str(a/'protection-and-metadata-verification.json'),'formal_outputs':str(a/'all-11-formal-output-identities.json'),'finite_affected_interfaces':str(a/'affected-interface-navigation-successor.json'),'original_FULL_report':'e03b7c2824105c5925cb9d64079bf653b03a41f4','original_affected_report':'4a75ca146e10062e469a42a9610bc3026861a34c','required_original_roles':['Ultra FULL R-B13 complete8 contribution5 primary; B13-R01 and all retained gates','Ultra affected role B09/B11; B13-AFFECTED-F1 and necessary finite scopes'],'candidate_SHA_tree_and_full_OLD_NEW_binding':'following publication-receipt.json; commit containing this file is payload candidate, later publication adds only full diff and receipts','OLD_to_NEW_full_diff':'following OLD-to-NEW.full.patch generated without path filters and read back independently','catalog_total':137,'all_behavior_designs_unexecuted':True,'reference_Ruby_game_historical_programs_executed':False,'quality_PASS':None,'author_independent_review_signature':False,'author_new_subtasks':0,'canonical_increment':0,'B030_increment':0,'G':False,'actual_gate':False,'C':False,'B16_release':False,'effective_configuration':'requested author xhigh and original independent ultra, default/Standard; effective UNVERIFIED; no probe/fallback'}
write(c/'review-dispatch.json',review)
write(c/'review-dispatch.md',f'''# B13 原两个 Ultra 增量复核入口\n\n当前状态：两问题作者返修完成，WP58新原稿固定补丁已获scope-amendment-2并精确应用；**等待原独立FULL/affected增量复核，尚无质量PASS、G或C**。\n\n正式FIX_BASE `{base}` / tree `ae2f491294eb4f97be6b75f75706c16279f9bf46`；复审OLD `{old}` / tree `23f92a9c446f5f0fbcee44df2f57d85df4dd0e3c`保持。最终NEW candidate SHA/tree、完整未过滤OLD→NEW diff及远端ref/FETCH_HEAD/全部输出读回见随后同目录 publication-receipt.json / publication-summary.md。\n\n1. 原Ultra FULL角色：以 `{a}/finding-dispositions-successor.json` 及 current-evidence-index.json 核验完整8贡献/5主责及所有原控制/最低验收；B13-R01 的当前 WS-W35、nil null/return_identity=nil、空列表false后态和UI人数门位于保留的 `{prev}/static-transition-traces-successor.json`。历史原trace中的false只作为冻结旧错误证据。\n2. 原Ultra affected角色：B09/B11复核B13-AFFECTED-F1，见新净稿WP58 §5.2、原稿WP58 §5.2、RC-W26及保留的当前entry_final_scan轨迹/consumer导航；WP41/WP49/WP50及WP47-B只读身份和完整既有有限影响范围见 affected-interface-navigation-successor.json。检查逐成员item后ability、首真即停、开场首命令前录制/回放、攻击后行动限定、取消先耗物和EOR延后选择；保留W16/W24/W25/随机/Arena门。\n\n两个问题的完整逐项响应见 `{a}/two-findings-repair-map-successor.json`；许可与精确after见 scope-application-receipt.json。新scope `{scope}`仅许可固定patch `8d186d65c9eb2bc0e03a27728bfa0ea8476f4753bb863054b41cdb3b79459b0d`，不改变OLD评审结论，不扩展B027或邻域作者范围。\n\n保留catalog137未执行设计（QC47/WS35/PA28/RC27）及全部非本次问题正确内容，证据见 protection-and-metadata-verification.json 和 all-11-formal-output-identities.json。历史pending提案及原两位reviewer输出保持原身份；当前successor才表示已应用。旧其他affected verdict只限OLD，不代签NEW。\n\n作者未开子任务、未自签门，未运行参考/Ruby/游戏/行为向量/历史程序。独立candidate门后才可G，actual FULL/affected另复核，C由唯一登记者处理；canonical/B030增量0，B16/WP67-A依赖保持。\n''')
write(c/'scope2-original-only.patch',git('diff','--binary','--no-ext-diff','--no-textconv',prior,'--',original).decode())
# Archive only newly authored metadata tools; these are not reference/behavior programs.
(repo/(a/'new-scope-application-metadata.py')).write_bytes(pathlib.Path('/tmp/B13-scope2-author-apply-20261010.py').read_bytes())
(repo/(a/'new-final-author-metadata.py')).write_bytes(pathlib.Path(__file__).read_bytes())
payload=sorted([original]+[str(p.relative_to(repo)) for directory in [repo/a,repo/c] for p in directory.rglob('*') if p.is_file() and p != repo/(c/'payload-inventory.json')])
write(c/'payload-inventory.json',{'kind':'PRECOMMIT_PAYLOAD_HASH_INVENTORY_EXCLUDES_OWN_INVENTORY_TO_AVOID_RECURSION','formal_FIX_BASE':base,'prior_publication':prior,'only_direct_formal_path':original,'own_directories':[str(a),str(c)],'payload_before_this_inventory_count':len(payload),'records':[{'path':p,**ident(read(p))} for p in payload],'inventory_will_be_included_in_postcommit_all_output_readback':True,'quality_PASS':None})
assert git('diff','--name-only').decode().splitlines()==[original]
subprocess.run(['git','diff','--check','--',original],cwd=repo,check=True)
print(json.dumps({'author_payload_files':len(payload)+1,'scope2_applied':True,'formal_changed_from_prior':[original],'previous_outputs_protected':100,'other_previous_outputs_byte_equal':99,'complete_controls':[len(d['controls']),sum(x['primary'] for x in d['controls'])],'catalog_total':137,'OLD_catalog_changed_rows':[(x['series'],x['id']) for x in changed],'OLD_catalog_added_rows':[(x['series'],x['id']) for x in added],'independent_quality':None,'evidence_dirs':[str(a),str(c)]},ensure_ascii=False))
