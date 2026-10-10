from pathlib import Path
import subprocess,json,hashlib,re
r=Path('/workspace/pokemon-essentials-clean-room');base='8e67f780c204d593d89f364f585d2c6c2fe74631';prev='d4bfb88e461383d689f0e2db5d08c5f143b1e5f5';amend='2b23c82947bcecec4ab059d63048f9b67586575b';branch='codex/cloud-dot-B13-author-1-20261010';aroot='review/remediation/20261003-prepare/batches/B13/author-draft-1/';proot='review/remediation/20261003-prepare/batches/B13/candidate-1/';a=r/(aroot+'scope-applied-1');p=r/(proot+'scope-applied-1');p.mkdir(parents=True,exist_ok=True)
def git(*args):return subprocess.check_output(['git','-C',str(r),*args])
def ident(d):return {'git_blob':subprocess.check_output(['git','hash-object','--stdin'],input=d,cwd=r).decode().strip(),'sha256':hashlib.sha256(d).hexdigest(),'bytes':len(d)}
def write(path,o):path.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
app=json.loads((a/'scope-application-receipt.json').read_text());m=json.loads((a/'scope-amendment.json').read_text());contract=json.loads(git('show',prev+':'+aroot+'B13-downstream-contract.json'));olds=json.loads(git('show',prev+':'+aroot+'finding-dispositions.json'));reviews=json.loads(git('show',prev+':'+aroot+'independent-review-requirements.json'));oldfinal=json.loads(git('show',prev+':'+aroot+'formal-output-identities.json'));allowed=contract['allowed_formal_write_paths']+m['allowed_original_write_paths']
# Reuse already checked exact full controls/read/catalog/source evidence; no new source or old program reading/execution.
for x in oldfinal['records']:assert (r/x['path']).read_bytes()==git('show',prev+':'+x['path']),x['path']
for x in m['records']:assert ident((r/x['path']).read_bytes())=={k:x['after_to_apply'][k] for k in ['git_blob','sha256','bytes']}
changed=git('diff','--name-only',prev).decode().splitlines();assert changed==sorted(m['allowed_original_write_paths'])
# All old authored evidence/candidate payload kept byte-for-byte, not rewritten to erase pending history.
oldoutputs=git('diff','--name-only',base,prev).decode().splitlines();assert len(oldoutputs)==50
for f in oldoutputs:assert (r/f).read_bytes()==git('show',prev+':'+f),f
newoutputs=[]
for f in allowed:
 now=(r/f).read_bytes();old=git('show',base+':'+f);newoutputs.append({'path':f,'kind':'APPROVED_FINAL' if f in contract['allowed_formal_write_paths'] else 'EXACT_AUTHORIZED_ORIGINAL','formal_input':{'commit':base,**ident(old)},'output':ident(now),'changed_from_formal_base':old!=now,'exact_original_scope_amendment':amend if f in m['allowed_original_write_paths'] else None})
write(a/'all-11-output-identities.json',{'status':'AUTHOR_SUBMISSION_NOT_QUALITY_PASS','formal_FIX_BASE':base,'formal_FIX_BASE_tree':m['frozen_formal_base']['tree'],'initial_management_packet':'e8caada4ab919e48e3dc817f0638ce595fde449c','scope_management_commit':amend,'management_not_formal_input':True,'approved_final_count':7,'exact_original_count':4,'total_output_count':11,'records':newoutputs,'no_other_formal_write':True})
# Full per-control author successor keeps required fields verbatim; it supersedes only own pending-scope status.
dis=[]
for x in olds['controls']:
 y=dict(x);y['historical_disposition_source']={'commit':prev,'path':aroot+'finding-dispositions.json','original_status':x['author_only_status'],'original_remaining_gaps':x['remaining_required_gaps']};y['author_only_status']='COMPLETE_LOCAL_AUTHOR_REVISION_SUBMITTED_FOR_INDEPENDENT_REVIEW';y['original_scope_application']=[z for z in app['records'] if x['id'] in z['canonical_finding_ids']];y['supplementary_WP55_application']='Applied exact consistency supplement; not a new B027 minimum obligation/canonical item' if x['id']=='GIR-FD82-B027' else None
 y['remaining_required_gaps']=['Parent-dispatched independent Ultra FULL8/5 and necessary candidate affected scopes; no author quality signoff','Only after candidate gates G; separate exact actual FULL/affected, then sole registrar C; all nonlocal/global canonical obligations retained']
 if x['id']=='GIR-FD82-B028':y['remaining_required_gaps'].append('WP67-A UI extension remains B16-owned; B16 full author hold/bilateral dependency not released here')
 if x['id']=='GIR-FD82-003':y['remaining_required_gaps'].append('B16/B17/B19/B20/B21 pending/nonlocal architecture obligations unchanged; only assigned local slice submitted')
 y['quality_PASS']=None;y['canonical_state']='OPEN';dis.append(y)
write(a/'finding-dispositions-successor.json',{'role':'A-B13_AUTHOR_ONLY','formal_FIX_BASE':base,'previous_frozen_author_publication':prev,'scope_amendment':amend,'complete_original_approved_current_controls_reused':{'commit':prev,'path':aroot+'original-and-acceptance-controls.json',**ident(git('show',prev+':'+aroot+'original-and-acceptance-controls.json'))},'counts':{'contributions':8,'primary':5,'accepted_contributions':0,'B030_required':0,'new_canonical_items':0,'vectors_executed':0},'controls':dis,'scope_blocker_resolved':True,'quality_PASS':None,'independent_review_started_by_author':False})
write(a/'scope-state-successor.json',{'status':'GRANTED_EXACT_SCOPE_APPLIED_AND_IDENTITIES_VERIFIED','supersedes_historical_pending_flags_only_for_fixed_bytes':{'source_publication':prev,'source_paths':[aroot+'original-scope-state.json',proot+'review-dispatch.json'],'historical_files_unchanged':True},'scope_management_commit':amend,'precise_combined_patch_SHA256':m['source_whole_patch']['sha256'],'four_records':app['records'],'original_write_authorized_and_exactly_applied':4,'formal_base_unchanged':base,'author_scope_blockers':[],'quality_or_vector_feasibility_assessed_by_scope_permission':False,'quality_PASS':None,'required_independent_reviews_pending':['Candidate Ultra FULL8/5','Necessary candidate affected finite scopes','After G exact actual Ultra FULL8/5','Separate necessary actual affected finite scopes'],'G':False,'C':False,'B16_release':False,'main_merge':False,'public_registration':False,'canonical_closure':False})
# Narrow new metadata checks: all planned/source proofs inherited; metadata is not rerun semantic validation.
current=git('diff','--name-only',base).decode().splitlines();assert sorted(f for f in current if f in allowed)==sorted(allowed)
assert all(f in allowed or f.startswith(aroot) or f.startswith(proot) for f in current)
protected=git('diff','--name-only',prev).decode().splitlines();assert protected==sorted(m['allowed_original_write_paths'])
check=subprocess.run(['git','-C',str(r),'diff','--check',base,'--',*allowed],capture_output=True,text=True);assert check.returncode==0,check.stdout
catpath=contract['allowed_formal_write_paths'][-2];cat=(r/catpath).read_text();counts={};sec=None
for l in cat.splitlines():
 if l.startswith('## '):sec=l.split('：')[0][3:]
 if re.match(r'^\| (Q\d+|W\d+\w*|P\d+) \|',l):counts[sec]=counts.get(sec,0)+1
assert counts=={'QC':47,'WS':35,'PA':28,'RC':26}
write(a/'new-scope-metadata-verification.json',{'kind':'NEW_METADATA_ONLY_NOT_RUNTIME_OR_INDEPENDENT_REVIEW','fixed_patch_exact':True,'four_before_bindings_verified':True,'four_after_bindings_verified':True,'all_seven_final_outputs_previous_candidate_byte_identical':True,'all50_previous_payload_files_byte_identical':True,'formal_write_scope_11':allowed,'all_other_protected_tracked_paths_unchanged':True,'all11_formal_git_diff_check':'PASS','catalog_static_design_counts':counts,'catalog_static_total':136,'old_catalog_total':127,'catalog_delta':9,'vectors_executed':0,'52_planned_reads_reused_from_exact_prior_verified_evidence':True,'complete8_control_bindings_reused_unchanged':True,'additional_reference_or_historical_semantic_reading':0,'old_programs_executed':0,'scope_approval_is_not_quality_PASS':True,'WP55_supplement_canonical_delta':0,'B030_required':False})
write(a/'affected-interface-scope-successor.json',{'role':'AUTHOR_NAVIGATION_ONLY_NOT_INDEPENDENT_VERDICT','exact_prior_map_and_assessment':[{'commit':prev,'path':aroot+n,**ident(git('show',prev+':'+aroot+n))} for n in ['affected-interface-map.json','affected-interface-author-assessment.json']],'new_original_delta_only':[{'path':x['path'],'canonical_finding_ids':x['canonical_finding_ids'],'allowed_clauses':x['allowed_clauses'],'output':x['applied_after']} for x in app['records']],'scope_change':'No new behavior or final-byte change beyond the approved7-file author revision: exact original synchronization only. Independent roles must still decide all original necessary/real current impacts at candidate and separately at actual.','potential_owner_batches':['B02','B03','B04','B07','B08','B09','B10','B11','B12','B14','B15'],'focus_required_navigation':['B09 received-source checkpoint/positive terminal exit vs selfKO; active submission uses same accepted interfaces','B10 loaded Ice actual qualification/non-Ice threshold; AI independent','B11 exact keys/settings vs consumers and ability/item attack replacement; RC24/127 count successor','B12 all four B12-C inputs refreshed in prior exact full delta; no scoring-to-actual conflation','All other-owner catalog rows unchanged; no automatic whole-owner reapproval'], 'candidate_independent_disposition':'NOT_STARTED; parent dispatches necessary finite scopes','actual_independent_disposition':'NOT_STARTED; separate exact actual mandatory','author_PASS_or_NOT_AFFECTED':False,'B16_WP67A_nonlocal':'Remains B16-owned read-only preparation/bilateral dependency; no release'})
# New review entry explicitly points at current successor; old candidate/pending entry remains frozen history.
review={'status':'COMPLETE_LOCAL_AUTHOR_CANDIDATE_READY_FOR_PARENT_INDEPENDENT_DISPATCH','branch':branch,'formal_FIX_BASE':base,'formal_FIX_BASE_tree':m['frozen_formal_base']['tree'],'prior_author_candidate':'57c79e4a9db6a9b987a8000c3afc5bdcd8dd9aa6','prior_author_publication':prev,'scope_management_commit':amend,'management_not_formal_input':True,'candidate_binding':'New exact candidate SHA/tree and complete unfiltered base->candidate/prior-publication->candidate streams are in following publication-receipt.json','author_role':'A-B13_ONLY','contributions':8,'primary_minimum':5,'formal_outputs':11,'seven_final_plus_four_exact_scoped_original':True,'complete_controls':{'commit':prev,'path':aroot+'original-and-acceptance-controls.json',**ident(git('show',prev+':'+aroot+'original-and-acceptance-controls.json'))},'original_frozen_contract':{'commit':'e8caada4ab919e48e3dc817f0638ce595fde449c','path':'review/remediation/20261003-prepare/batches/B13/refreeze-after-B12-C-1/B13-downstream-contract.json'},'current_author_report':str((a/'author-report-successor.md').relative_to(r)),'current_dispositions':str((a/'finding-dispositions-successor.json').relative_to(r)),'current_scope_receipt':str((a/'scope-application-receipt.json').relative_to(r)),'all11_output_identities':str((a/'all-11-output-identities.json').relative_to(r)),'candidate_FULL':reviews['FULL'],'candidate_affected':reviews['affected'],'actual_full_difference_requirement':reviews['actual_full_difference_requirement'],'scope_blockers':[],'quality_PASS':None,'independent_review_started_by_author':False,'parent_only_dispatch':True,'additional_tasks_spawned':0,'G_C_sole_registrar':True,'candidate_quality_acceptance_pending':True,'actual_quality_acceptance_pending':True,'B16_release':False,'B030_required':False,'canonical_state':'OPEN until all nonlocal/global obligations fulfilled','execution_limits':'All prior U01-U10/G01-G12/AX01-AX20, conditional berry67 and named unread paths retained; reference/Ruby/game/vectors/old programs execution0; no new source/history reads','configuration_requested':contract['configuration'],'configuration_effective':'UNVERIFIED; no CLI/native/quota probe or fallback'}
write(p/'review-dispatch.json',review)
(p/'review-dispatch.md').write_text('''# B13 新完整作者候选：scope-applied-1

这是当前作者派发入口，替代旧 candidate-1 根目录的“原稿范围待确认”状态；旧冻结材料按其当时状态保持原件。新精确candidate SHA/tree与普通publication及完整未过滤差异见本目录后继 `publication-receipt.json`。

正式FIX_BASE仍为 B12-C `8e67f780c204d593d89f364f585d2c6c2fe74631`／tree `ae2f491294eb4f97be6b75f75706c16279f9bf46`。管理许可 `2b23c82947bcecec4ab059d63048f9b67586575b` 没有并入或替代正式输入。作者只应用它绑定的四份固定原稿补丁：WP54 B027、WP55恢复一致性（补充、canonical增量0）、WP56 B028、WP58 B028/B029。before/after与whole.patch `11bfdbd21211dce18016569c7bb5dd9447b90531475f70920e737ae77df0e769` 全部相等。7份正式稿保持先前候选字节，当前正式输出11份。

[当前作者报告](../../../author-draft-1/scope-applied-1/author-report-successor.md)、[全部8项完整作者处置后继](../../../author-draft-1/scope-applied-1/finding-dispositions-successor.json)、[精确应用收据](../../../author-draft-1/scope-applied-1/scope-application-receipt.json)、[全部11份输出身份](../../../author-draft-1/scope-applied-1/all-11-output-identities.json)。52读身份、8项完整原／批准／当前root+扩展控制、来源定位、条件／最小反例、状态轨迹、目录保留与源限制复用先前精确冻结证据，未减少任何义务；未增加额外参考或历史阅读。

**范围阻塞已解除，范围许可不是质量PASS。** 父任务派发独立 `gpt-6.1-sol Ultra` FULL全部8贡献／5主责，并派必要当前affected有限门。完整 [独立要求](../../../author-draft-1/independent-review-requirements.json) 与 [受影响导航后继](../../../author-draft-1/scope-applied-1/affected-interface-scope-successor.json) 为准；作者未自开任务、未签独立PASS／NOT_AFFECTED。

候选所有必要门完成才唯一登记者G；actual仍须独立FULL及分别必要affected，对当时接受前驱→actual和candidate→actual两条完整未过滤流回读，然后父C。canonical全局／非本地义务未完成不能关闭，B16只读增量准备且双向依赖仍在，WP67-A扩展由B16负责。B030非必修、计数0。没有main／公共登记／reference写入。

136项是静态未执行验收设计；新增9项及全部行为均未实测。参考／Ruby／游戏／行为向量／历史程序执行0；全部继承限制、树果条件67与具名未读内容保持。
''')
# Relative link target from candidate-1/scope-applied-1 is ../../author-draft-1/, not ../../../ (B13 parent).
s=(p/'review-dispatch.md').read_text();(p/'review-dispatch.md').write_text(s.replace('../../../author-draft-1/','../../author-draft-1/'))
(a/'author-report-successor.md').write_text('''# B13 scope应用后完整作者交付

正式FIX_BASE保持B12-C `8e67f780c204d593d89f364f585d2c6c2fe74631`／tree `ae2f491294eb4f97be6b75f75706c16279f9bf46`。当前状态：本地完整作者修订可交独立复审，7份批准正式稿＋4份新获准精确原稿，共11份；8贡献／5主责，作者scope阻塞0，独立质量PASS为空，接受贡献0，未G/C登记。

登记者 `2b23c82947bcecec4ab059d63048f9b67586575b` 精确许可已核对并应用：[scope及应用收据](scope-application-receipt.json)逐一绑定 d4bfb88 的proposal／whole.patch及B12-C四份before和精确proposed-after。没有修改补丁、增路径或增条款；WP55只改单场首条摘要，是原恢复焦点的一致性补充，不新增B027最低义务或canonical。WP55正确报名/取消及WS28/29、旧目录其他owner全部保持。旧pending提案／旧候选／旧报告按时间保持原字节，由本目录状态后继覆盖当前状态。

[当前8项作者处置](finding-dispositions-successor.json)完整复用每项原前提、反例、minimum/recheck、批准验收门与当前root/扩展限定，只更新“获准原稿已应用”及后續独立门状态。GIR-FD82-003/B003/B018局部协作；B010/B025/B027/B028/B029五主责。固定加载Ice资格与独立AI、歌声保存来源两例／selfKO最后方、nil和空列表提交／活动队伍、双方完整EXP与物品按位置和异常部分提交、Arena3/4/5轮状态不复位、攻击阶段属主替补记录和随机/Arena反向均沿先前完整静态证据。不能以该范围许可认可向量可行性或源码正确性。

[11份输出身份](all-11-output-identities.json)与[新静态元数据核验](new-scope-metadata-verification.json)确认四份精确after、7份正式稿旧候选字节、先前50份作者输出全不改、全部受保护路径不改，11份正式差异空白检查通过。52读身份、全8控制、原source-reading-log／static-transition-traces／catalog-preservation／source-limits等原证据复用，不重新运行历史作者/reviewer程序、不额外阅读参考或全历史。目录仍47+35+28+26=136；W22b与旧ID顺序/行锁保持，旧127→新增9设计，所有向量未执行；历史RC23/126错误仍只在自有后继解释，公共历史报告不改。

[受影响后继导航](affected-interface-scope-successor.json)保留11批完整接口/原必要条件，由独立角色判断必要候选与actual有限门；不自动要求全部旧owner重批，也不由作者代签NOT_AFFECTED。父派独立Ultra FULL8/5及必要affected candidate；通过后G，再实际FULL和必要affected及完整两流，全部通过才C。B16只读准备/双向依赖及B028 WP67-A非本地扩展未解除，B17/B21及canonical未尽义务继续OPEN，B030非必修。

未合main、未改公共登记/reference/历史报告；参考／Ruby／游戏／向量／历史程序执行0。全部U01–U10/G01–G12/AX01–AX20、树果条件67、具名未读内容与宿主/媒体/事件/插件限制保持。请求配置仍作者xhigh、独立ultra、default/Standard；effective UNVERIFIED，无CLI/native/quota探测或自开子任务。

新候选及ordinary publication的SHA/tree、完整未过滤差异、独立远端ref／FETCH_HEAD及所有输出读回放在当前 [候选入口](../../candidate-1/scope-applied-1/review-dispatch.md) 所在目录后继publication。作者没有替父派发或签复审。
''')
# Current full11 formal diff is an author convenience only; parent still reads whole unfiltered frozen candidate.
patch=git('diff','--binary','--no-ext-diff','--no-textconv',base,'--',*allowed);(p/'all-11-formal.patch').write_bytes(patch)
(a/'new-refreeze-metadata.py').write_bytes(Path('/tmp/B13-refreeze-scope-20261010.py').read_bytes())
# Validate all new markdown relative links without any source read. Existing historical entry remains unchanged.
for f in list(a.glob('*.md'))+list(p.glob('*.md')):
 if f.name=='scope-disposition.md':continue
 for link in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  if '://' not in link:assert (f.parent/link).exists(),(f,link)
newfiles=sorted([f for d in [a,p] for f in d.rglob('*') if f.is_file() and f.name!='output-inventory.json']);newformal=m['allowed_original_write_paths'];allnew=[r/f for f in newformal]+newfiles
inv={'stage':'NEW_SCOPE_COMPLETE_AUTHOR_PRECOMMIT_PAYLOAD','FIX_BASE':base,'previous_publication':prev,'scope_amendment':amend,'11_outputs':newoutputs,'inherited50_output_bindings':'Prior frozen d4bfb88 payload remains exact, old candidate package is history','records':[{'path':str(f.relative_to(r)),**ident(f.read_bytes())} for f in allnew],'self_inventory_excluded_only':True};write(p/'output-inventory.json',inv)
print('REFROZEN author payload:11 outputs / 8 contributions /5 primary; exact4 originals and unchanged7 final; scope blocker0; quality PASS null; new own files',len(newfiles)+1)
