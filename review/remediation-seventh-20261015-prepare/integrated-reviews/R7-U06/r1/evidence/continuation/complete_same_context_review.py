import copy, datetime, hashlib, json, os, pathlib, shutil, subprocess

ROOT=pathlib.Path('/workspace/r7-ir-R7-U06')
REPO=ROOT/'result'
PREFIX='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U06/r1/'
OUT=REPO/PREFIX
OLD='84dd2631af9f3496008fa9971c136c43a4b772a7'
HIST=OUT/'history'/OLD
E=OUT/'evidence/continuation'
ADJ='5325e8046f4d625b855e3c216abaa650805fab5e'
THREAD='01a1401c-1527-75c6-9a36-7bc9b3a00007'
MI='45c80832a41c1b56dcd7e9d93497758cbb7721de'
FI='13d76ba61838b13925ba9d41f58a6b047564d926'
utc=datetime.datetime.now(datetime.timezone.utc).isoformat()
assert os.environ.get('CODEX_THREAD_ID')==THREAD

def load(p):return json.loads(p.read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}

decision=load(E/'decision.json')
assert decision['disposition']=='ALLOW_SAME_INDEPENDENT_CONTEXT_TO_COMPLETE_AND_SIGN_EXPLICIT_CONTENT_VERDICTS; RETAIN_PROCESS_NONCOMPLIANCE'
assert decision['actual_reviewer_thread']==THREAD and decision['original_WAIT_commit']==OLD
assert not decision['PASS_granted_by_this_decision'] and not decision['ACCEPTED'] and not decision['CLOSED']
archive=load(E/'old-WAIT-archive-receipt.json')
assert archive['archived_files']==50
for row in archive['files']:
    p=REPO/row['archive_path'];assert ident(p.read_bytes())=={k:row[k] for k in ['bytes','sha256','git_blob']}

oldper=load(HIST/'per-id.json')
per=copy.deepcopy(oldper)
oldreceipt=load(HIST/'review-input-receipt.json')
receipt=copy.deepcopy(oldreceipt)
audit=load(ROOT/'bootstrap-evidence/actual-byte-audit.json')
meta=load(ROOT/'bootstrap-evidence/cumulative-metadata-audit.json')
assert audit['git'][MI]=='6480ffe3df49bd9776c719f3c9be1c13618fdb0a'
assert audit['git'][FI]=='6747a584b91c86acd4771c1a6dee93260602106f'
assert len(meta['complete_required_actual_read_trace'])==14
root_binding={'fixed_publication_commit':ADJ,'decision_path':'review/remediation-seventh-20261015-prepare/process-adjudications/R7-U06-IR-PROC-001/v1/decision.json','decision_identity':ident((E/'decision.json').read_bytes()),'decision_utc':decision['utc'],'finding':decision['finding'],'disposition':decision['disposition'],'root_granted_semantic_PASS':False,'scope':'Only this recorded read-only diagnostic no longer blocks content independence; violation and original UTC/PID gap remain permanently recorded. The independent reviewer signs each new scoped verdict.'}
process={'original_issue':'U06-IR-PROC-001','finding':'VIOLATED_RETAINED_NONCOMPLIANCE','original_violation_record_unchanged':'evidence/initial-provenance-and-deviation.json','original_WAIT_commit':OLD,'original_WAIT_archive':'history/'+OLD+'/','root_adjudication':root_binding,'current_content_independence_blocker_from_this_diagnostic':False,'new_auth_or_quota_queries':0,'new_auxiliary_AI_tasks':0,'original_missing_UTC_PID':'RETAINED_UNAVAILABLE; no retrospective fabrication','fully_procedurally_compliant':False}
separate_gates=[
 {'gate':'root receipt and registration of the newly signed actual result','state':'SEPARATE_POST_REVIEW_ACTION','is_review_unread_or_incomplete_item':False},
 {'gate':'formal ACCEPTED and separately CLOSED','state':'NOT_GRANTED_BY_REVIEWER','is_review_unread_or_incomplete_item':False},
 {'gate':'reference observation / full independent model / host / Demo / native media / real save / replay','state':'NOT_EXECUTED_0_RETAINED','is_review_unread_or_incomplete_item':False},
 {'gate':'effective model / effort / tier / speed attestation','state':'UNVERIFIED_RETAINED','is_review_unread_or_incomplete_item':False},
 {'gate':'global C12/D/H/J coverage, old56/92, other batches and future unmerged contributions','state':'OUTSIDE_THIS_TWO_ID_SCOPED_PASS; historical/domain limits retained','is_review_unread_or_incomplete_item':False}]

common_completion=[
 {'obligation':'original seven groups, actual record identity, original nonauthor counterproof, narrowed minimum and correct preservation','completion':'COMPLETE','basis':'Both original full seven-group contracts and normalized records12/13 read in original phase. All286 referenced input/pointer/canonical/raw-slice bindings reverified. New verdict uses independent content reasons, not the mechanical count.'},
 {'obligation':'four current MI target files in full and every actual U06 hunk','completion':'COMPLETE','basis':'Four complete current targets read in original phase; exact full-file identities and six hunks remain bound to fixed MI. Every clause/vector is described in this per-ID record; no candidate snapshot substitutes for actual MI.'},
 {'obligation':'fourteen full required actual targets/conditional target/consumers/catalogs','completion':'COMPLETE','basis':'Full required fourteen-file actual read trace retained; original truncation gaps were supplemented before original phase ended. All bytes remain immutable and reverified. Conditional WP43 assessed explicitly.'},
 {'obligation':'all thirty actual vectors: common prerequisites, independent variation, normal control, cancellation, failure and committed prefixes','completion':'COMPLETE','basis':'All30 independently reasoned in original phase and actual two catalog sections reread in continuation. Per-vector lines/bytes, premises, independent reasons and NOT_EXECUTED retained. M09 six original groups and M10 C1–C7 mappings complete.'},
 {'obligation':'named direct/transitive consumers and history relevant to these two IDs','completion':'COMPLETE','basis':'Required full WP39/WP41/WP34/WP43/WP44/WP46/WP48/WP49 and full four catalogs, plus named WP40/WP42/WP47-A/WP50/WP52-B and fixed R/history supplements. Specific prefix, stat-stage, suppression, parent-read, AI empty-list, natural-gift and BeakBlast interactions reviewed. No global historical alias/coverage certification inferred.'},
 {'obligation':'shared preservation/current cumulative reception metadata','completion':'COMPLETE','basis':'Own four complete files each have only U06 as contributor; shared_preservation_checks empty and no missing own receiver. All56 journal hunks/24targets reconstruct B→MI, explicit two U01→U02 EOF concatenations and three root metadata adjustments verified. Prior accepted five files byte-preserved and their current intersecting consumers semantically reviewed. Other batches receive no new semantic PASS.'},
 {'obligation':'execution/configuration/limits and clean-room boundary','completion':'COMPLETE_AS_STATIC_REVIEW','basis':'All behavior NOT_EXECUTED; no reference/native/game/model execution; config UNVERIFIED; exact L01–L14 retained. No implementation or reference source copy/translation, no optional/policy adoption.'}]

for record in per['records']:
    key=record['record_id']
    assert record['verdict']=='WAIT' and len(record['vectors'])==15
    record['original_WAIT']={'commit':OLD,'verdict':'WAIT','wait_reason':record.pop('wait_reason'),'archive_per_id':'history/'+OLD+'/per-id.json','preserved_unchanged':True}
    record['verdict']='PASS_SCOPED_ACTUAL_INTEGRATION'
    record['PASS_SCOPED_ACTUAL_INTEGRATION']=True
    record['content_finding']='COMPLETE_SCOPED_STATIC_ACTUAL_INTEGRATION_REVIEW_SUPPORTED'
    record['signed_by_actual_independent_reviewer']=THREAD
    record['signed_at_utc']=utc
    record['process_adjudication']=root_binding
    record['review_completion']={'status':'COMPLETE','original_seven_groups_completed':7,'all_four_current_target_files_fully_read':True,'required_fourteen_actual_files_fully_read':True,'own_actual_vectors_completed':15,'all_batch_actual_vectors_completed':30,'remaining_unread_items':0,'remaining_in_scope_content_review_items':0,'unmet_scoped_review_gates':[],'identified_content_blockers':0,'completed_obligations':common_completion,'qualification':'This is the same reviewer completing and explicitly signing the full original scoped content judgment. The previous WAIT was not PASS, the root decision grants no PASS, and root later administrative reception is not an unread obligation.'}
    record['unmet_gates']=[]
    record['remaining_separate_gates']=separate_gates
    for v in record['vectors']:
        assert v['execution']=='NOT_EXECUTED'
        v['primary_record_verdict']='PASS_SCOPED_ACTUAL_INTEGRATION'
        v['same_context_completion_at_utc']=utc
        v['review_completion']='ACTUAL_PREMISES_AND_STATIC_EXPECTATION_REVIEWED_COMPLETE; NOT_EXECUTED'
    record['shared_receiver']['formal_receiver']='Scoped current-byte semantic compatibility and shared preservation review COMPLETE. Root later receipt/registration, formal acceptance and closure are separate actions; no own unread/incomplete receiver item remains.'
    record['shared_receiver']['scoped_receiver_review_complete']=True
    for collection in [record['direct_and_transitive_receivers'],record['seven_group_review']['dependency_reception']]:
        for dep in collection:
            dep['scoped_consumer_review']='COMPLETE; no identified U06 incompatibility in the stated actual scope'
            dep['root_registration']='SEPARATE_POST_REVIEW_ACTION; not an unread/content-review item'
    if key=='GR7-M09-001':
        record['explicit_signed_basis']='PASS for fixed MI WP46L54/L59 and pokemon catalogL135–157: actual base-evaluation consumption, independent hit counts, all normal/substitute/miss/stop/cancel/fault-prefix cases and preserved WP43/AI/fixed-damage/current-stat scope are fully reviewed. All15 vectors static; conditional WP43 not triggered. No remaining original-scope read/content item.'
    else:
        record['explicit_signed_basis']='PASS for fixed MI WP49L157–164, WP46L23 and combat catalogL43–65: direct per-hit timing/type/actual-target/exclusion/current ordinary ability/central increment-clamp gates, all C1–C7 cases, normal control, canceled/failed/committed-prefix paths and unchanged registry/AI/hatching boundaries fully reviewed. All15 vectors static; no remaining original-scope read/content item.'
    assert not record['ACCEPTED'] and not record['CLOSED']

per['schema']='r7.U06.actual-independent-review.r1.same-context-completion'
per['original_reviewed_at_utc']=per['reviewed_at_utc'];per['reviewed_at_utc']=utc
per['continuation']={'same_actual_thread':THREAD,'root_fixed_commit':ADJ,'original_WAIT_commit':OLD,'original_all50_files_preserved':True,'no_new_reviewer':True,'new_auxiliary_AI_tasks':0,'new_auth_or_quota_queries':0}
per['process_deviation_original_at_WAIT']=per['process_deviation'];per['process_deviation']=process
per['review_completion']={'reviewed_ids':2,'PASS_SCOPED_ACTUAL_INTEGRATION_ids':2,'FAIL_ids':0,'WAIT_ids':0,'unread_items':0,'incomplete_in_scope_content_items':0,'remaining_scoped_review_gates':[],'all30_behavior_vectors':'NOT_EXECUTED','root_formal_acceptance_and_closure_granted':False}
write(OUT/'per-id.json',per)

receipt['schema']='r7.U06.actual-review-input-receipt.r1.same-context-completion'
receipt['original_receipt_utc']=receipt['utc'];receipt['utc']=utc
receipt['identity']['process_eligibility']='Root fixed decision allows same-context completion and explicit content verdicts; original process noncompliance permanently retained. No new reviewer/context.'
receipt['process_deviation_original_at_WAIT']=receipt['process_deviation'];receipt['process_deviation']=process
receipt['root_adjudication']=root_binding
receipt['original_WAIT_archive']={'commit':OLD,'archived_files':50,'bytes':1184638,'receipt':'evidence/continuation/old-WAIT-archive-receipt.json'}
receipt['continuation_reverification']={'source_and_actual_byte_audit':'evidence/continuation/actual-byte-audit.json','metadata_audit':'evidence/continuation/cumulative-metadata-audit.json','read_ledger':'evidence/continuation/read-ledger.jsonl','qualification':'No replacement/shared-directory assumption: original physical input directories persisted in same container and all bounded members/identities reverified. Original full content reading remains valid; continuation rechecks all30 actual vectors and narrow decisive source paths. Mechanical rechecks are corroboration, never the semantic basis.'}
receipt['complete_scope_declaration']={'all_two_original_seven_group_contracts':True,'all_four_current_target_files':True,'conditional_WP43_and_required_fourteen_actual_files':True,'all_thirty_actual_vectors':True,'necessary_named_supplements':True,'direct_transitive_shared_history_relevant_to_two_IDs':True,'remaining_unread_items':0,'remaining_in_scope_content_items':0,'remaining_scoped_review_gates':[],'separate_root_or_runtime_gates':separate_gates}
receipt['publication']['original_completed_readback']={'commit':OLD,'tree':'cc698b55ca67a7970a233c23cf14117f5092eecd','files':50,'bytes':1184638,'scope':'Original WAIT result, fully preserved in history'}
receipt['publication']['continuation']='Ordinary fast-forward commits/push to original sole branch. Full new result tree including archived core/manifest will be read back per file; final readback external receipt avoids a false self-referential future hash.'
receipt['publication']['final_completed_readback_destination']='/workspace/r7-ir-R7-U06/continuation-final-remote-readback.json'
write(OUT/'review-input-receipt.json',receipt)

for source,name in [('actual-byte-audit.json','actual-byte-audit.json'),('cumulative-metadata-audit.json','cumulative-metadata-audit.json'),('read-ledger.jsonl','read-ledger.jsonl')]:shutil.copyfile(ROOT/'bootstrap-evidence'/source,E/name)
for n in ['024-fetch-root-adjudication.json','025-continuation-input-reverification.json','026-continuation-cumulative-metadata.json']:shutil.copyfile(ROOT/'bootstrap-evidence'/n,E/n)
shutil.copyfile(pathlib.Path(__file__),E/'complete_same_context_review.py')
write(E/'scoped-completion-matrix.json',{'utc':utc,'pid':os.getpid(),'signed_by_actual_thread':THREAD,'root_adjudication':root_binding,'original_WAIT_preservation':'history/'+OLD+'/','records':[{'record_id':r['record_id'],'verdict':r['verdict'],'explicit_signed_basis':r['explicit_signed_basis'],'completion':r['review_completion']} for r in per['records']],'limitations':per['runtime'],'effective_configuration':per['effective_configuration'],'process_violation':process,'ACCEPTED':False,'CLOSED':False})

report=f'''# R7-U06 同一独立 context 完成复审

本人在原真实 thread **{THREAD}** 完成原合同全部限定内容复审，于 **{utc}** 分别签发：

| ID | 新结论 | 本范围未读项 | 本范围未完成内容项／未满足审查门 |
| --- | --- | --- | --- |
| GR7-M09-001 | **PASS_SCOPED_ACTUAL_INTEGRATION** | **0** | **0／无** |
| GR7-M10-001 | **PASS_SCOPED_ACTUAL_INTEGRATION** | **0** | **0／无** |

这是本审者对完整限定静态实际整合内容的新明确结论。原 `84dd2631af9f3496008fa9971c136c43a4b772a7` 两项结论仍是 **WAIT**，没有被改写成过去已PASS。原50文件／1,184,638字节（核心四文件、provenance、所有原失败日志和清单）在更新前逐字归档到 [history/{OLD}/](history/{OLD}/report.md)，完整身份见 [归档回执](evidence/continuation/old-WAIT-archive-receipt.json)。

## 根程序裁决与保留违例

完整读取固定提交 **{ADJ}** 的 [same-context-continuation.md](evidence/continuation/same-context-continuation.md) 与 [decision.json](evidence/continuation/decision.json)，并核其Git blob和本地实际字节。根明确允许原同一真实独立context完成内容并签新结论；该裁决自身**没有**签发PASS、ACCEPTED或CLOSED。本审者也不以根的判断替代自己的内容审查。

原一次 `gh auth status` 确实违反“不查额度/认证”，原退出1、未暴露令牌值及初期UTC/PID缺口永久保留。[原始违例记录](evidence/initial-provenance-and-deviation.json) 原样保持，不宣称过去零查询或完全合规。根将该只读程序违例单独接收留档，裁定其不阻断本份内容独立性。因此旧WAIT所列该门由具名根裁决处理，不能继续充当本审者未读门。续审新增辅助AI任务、子会话、模型调用、认证/额度查询均 **0**。

## 固定输入、完成范围与证据性质

- B：`e646432c644dec04d306842cc5a559a29c718fbc`；结果仍从B建立的原唯一分支 `codex/r7-ir-u06-20261015-r1` 延续。
- MI：`{MI}`；workspace tree `6480ffe3df49bd9776c719f3c9be1c13618fdb0a`；正式131文件子树 `8403869aaeb4726518414b409b3808c3c0780e65`。
- FI：`{FI}`；tree `6747a584b91c86acd4771c1a6dee93260602106f`。原派发 `c64774c60d91e522cb515ef71e3e9d4ea6b4712c` 全文要求继续适用；原完整七组合同 `f622356f3beb9e84ea8cff9db07c7fb382565d3f` 不变。
- 固定参考R：`Maruno17/pokemon-essentials@8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，派发给定tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。仅主张有界成员身份与具名源范围已核，不认证整个参考tree。
- 作者、候选freeze、候选独立review与各tree均保持原冻结，精确身份见 [输入回执](review-input-receipt.json)。候选PASS、作者自审和旧“未发现新增阻断”均不作为本次新PASS的替代。

原容器与原目录的 original36成员／7,536,934字节、actual-input123／2,704,432、具名补充11／602,702全部保留并再次核验，不重建替代任务，不假设共享目录。原两项七组、C01/C05原非作者反证、最小合同、正确保留、正常对照和取消/失败/已提交前缀均已读完；286项原始定位/规范JSON/切片绑定无缺项。

四个当前实际目标全文、全部六处U06变更、指定条件WP43，以及合同列出的完整14份实际目标/消费者/目录，在原阶段已全部实际审读；初期大输出截断的中段已逐段补读。本续审确认固定完整字节未变，再读两目录全部30向量和M09基底/循环、M10直接尾部关键源路径。不是把“复核hash/退出0”当作重新内容审查；实际内容理由、逐向量前提/独立变化/静态理由和精确MI行号及字节身份保留在 [per-id.json](per-id.json)。[完成矩阵](evidence/continuation/scoped-completion-matrix.json) 逐项确认所有原合同范围义务完成，本范围未读、未完成内容及未满足审查门均为0。未声称全文重读131份。

实际AGENTS全文及相关技能检查保持；B/MI `.agents`/`.codex` 树和相关本地目录无适用项目技能，不补造应用回执。仅产出干净室行为规格审查证据，无引擎/TS实现、参考程序执行或源码复制/转译。

## GR7-M09-001 明确内容结论

**PASS_SCOPED_ACTUAL_INTEGRATION。** WP46 L54/L59和pokemon目录L135–157完整满足原窄合同：形态吸收在普通基底前返回，不消费围攻参与者、不推进三连踢累计基底；计划和成功击计数独立，吸收仍占击数，不补击。SNEASEL95/MAGIKARP10围攻首吸收后首次普通基底14、非6，普通对照14/6；三连踢首吸收后10/20，普通对照10/20/30。替身仍普通求值推进，基底与最终伤害/HP损失严格区分。

全部15行逐一完成前提及静态理由判断：原6组拆分的吸收/普通对照、两种替身、首失手与续击失手、U倒下/睡眠/冰冻、唯一T倒下，以及额外上游取消和两种前缀故障。独立后段睡冻/倒下是条件化变化，不声称无其它反应的默认夹具会自然产生它们。后续未到的基底/HP不补做，已到PP/形态/HP/求值写点不自动回滚，不承诺宿主恢复或整招完成。

WP43 §6.2 C1早返原已正确，条件同步不触发，未采用可选交叉引用；不把整个核心/TK求值触发写成缺失。原MH02/MH06、AI、身份计数、owner/目标资格、命中与当前攻防、固定伤害覆盖保持。该完整内容判断不是由字节一致性推导；未满足原限定内容审查项为0。

## GR7-M10-001 明确内容结论

**PASS_SCOPED_ACTUAL_INTEGRATION。** WP49 L157–164、WP46 L23及combat目录L43–65完整满足C05窄合同。直接每击尾部位于附效/额外畏缩/减伤果消费之后、后续T/U濒死检查之前；以本次计算类型火/水、实际目标列表和当下状态判门。unaffected、calcDamage0、替身独立排除；当下普通有效STEAMENGINE及中央可升资格通过才由自身来源请求速度+6。普通有效性拒倒下/胃液/有效气体；更早显式允许倒下的OnBeingHit不扩此门。无独立模式破坏者/强行屏蔽门，强行对附效及具名整招后段二/三的门不套到此尾部。

全部SE01–SE15及原C1–C7映射逐条完整判断。合法水枪夹具当前PP5／总PP25，独立常量核算普通基础6、合成倍率3、伤18至82、PP5→4；后继普通速度140而原速度35不重写。增量+6按中央夹限−4→+2、+5→+6、+6不增；+2后继速度70。火例和其它类型/输电例伤害另算，不复制水18。替身、保护/失手、条件入口calcDamage0、两种压制、尾部已倒下、多击逐次重查、模式破坏者、合法DARMANITAN/SHEERFORCE/EMBER、上游取消/早失败和写阶后反馈故障均按实际位置判断，保留已到前缀。

不构造同时蒸汽机/单纯/唱反调夹具。原AB31行及AI/AE/BE/CE条款保持，48族267配对与WP48的27族148配对不增加；AI评级/孵化标记不当作此战斗反应证据。该完整内容判断未借用根语义判断、运行或作者自审，未满足原限定内容审查项为0。

## 共享、直接／传递消费者及历史

本审者的本范围共享/消费者/历史内容审查**已经完成**，没有因等待根未来登记而留下可读未读项。U06四份完整目标各仅有U06贡献，`shared_preservation_checks=[]`；六hunk之外逐字保留B，实际MI与本批批准候选片段一致，未漏接/重复/覆盖其它当前贡献。24目标/56hunk累计重建、两处U01→U02 EOF连接、三处root接收元数据调整及其固定链接/候选读取方式已核。该全局机械核对不对U01/U02 engine/UI、audit/matrix、U11 DX或其它批次授予新语义PASS。

U04/U05先前接受的五份文件逐字保持，其当前全文与本批相交的领域消费者均已读。WP34父代动态读取、WP39/WP41上下游命令/换人上下文、当前WP40 §5.2.3、WP42 §8、WP47-A §3.1.1、WP50 §5.1.1、WP52-B具名段及相应历史/参考补充均完成本范围语义核：自然之恩/JABO-ORAN续击失败与已提交持物/HP/PP、BeakBlast时序、完整新尝试的条件错误重试均不受新两项规则破坏，未补造自动恢复漏击或统一事务。

GR6-CA-EB-001的AI空名单、正替身、预测关/评分开除零是不同消费者/原因，本M09不关闭它。J09有限生产/消费者与逐clause接收、C05登记外直接分支的窄裁决及既有历史资格都保持；没有把无作者排程边解释为全领域无依赖。C12/D/H/J全域覆盖、其它批次、未来未合入贡献的责任仍按原边界，不被本次两个ID的限定PASS替代。U03/U07/U10仍流程WAIT未合入；旧56/92、27项/13批保持，7 optional、2导航facet、1 no-required、2 policy未采用。

根对**新结果**后续接收/登记以及正式ACCEPTED、另行CLOSED是独立后续动作；它们不等于本审者还有未读消费者。本审者未宣布这些动作完成。

## 运行限制与成果发布

30条行为向量全部 **NOT_EXECUTED**。本次及续审参考观察、参考程序、独立完整行为模型、宿主/Demo/native媒体/真实存档回放、行为故障注入新增运行均0。历史H14/UTIL-03的一进程10输入只保留原资格，不回填。原 [L01–L14完整原件](evidence/limits-and-alias-reception.json) 字节不变；有效model/effort/tier/speed始终 **UNVERIFIED**，请求/PID/退出0不认证配置。两项PASS只认证以上完整限定静态实际整合内容。

所有真实旧失败及原一次认证查询仍可在旧提交/归档/原日志核验。只在原唯一分支和原授权r1目录普通提交/推送；MI正文、候选、公共台账、main和tag不改、不force。发布后对包括历史归档和manifest在内的全部新成果文件做固定commit完整远端字节/SHA256/Git blob/mode回读；先将首次续审提交的真实回读纳入证据提交，再将最终提交的完整回读及commit/tree随最终答复返回，避免虚构自含未来提交身份。
'''
(OUT/'report.md').write_text(report)
write(E/'completion-build-receipt.json',{'utc':utc,'pid':os.getpid(),'same_actual_thread':THREAD,'root_fixed_commit':ADJ,'records':[{'id':r['record_id'],'verdict':r['verdict'],'unread':0,'incomplete_scoped_content':0,'unmet_scoped_review_gates':[]} for r in per['records']],'manual_review':'The independent reviewer explicitly completed and signed the stated content findings; this script only serializes findings/evidence. No behavior model or reference program executed.','original_process_violation':'RETAINED','original_WAIT_all50_files':'ARCHIVED_BYTE_EXACT','ACCEPTED':False,'CLOSED':False})
print(json.dumps({'utc':utc,'output':str(OUT),'records':2,'verdicts':[r['verdict'] for r in per['records']],'all30_behavior':'NOT_EXECUTED','remaining_unread':0,'remaining_scoped_content_items':0,'remaining_scoped_review_gates':[],'original_WAIT_preserved_files':50,'root_granted_semantic_PASS':False,'reviewer_signed':True},ensure_ascii=False))
