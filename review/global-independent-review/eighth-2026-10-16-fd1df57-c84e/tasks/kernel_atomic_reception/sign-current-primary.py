"""Publish only this task's completed, bounded static contribution locally."""
import collections
import datetime
import hashlib
import json
import subprocess
from pathlib import Path
B=Path(__file__).resolve().parent
RR=B.parent.parent
R=Path('/workspace/pokemon-essentials')
PROJECT=Path('/workspace/pokemon-essentials-clean-room')
START=datetime.datetime.now(datetime.timezone.utc).isoformat()
def load(n): return json.loads((B/n).read_text())
def write(n,d): (B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def identity(n):
    raw=(B/n).read_bytes()
    return {'path':n,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
def transport(p): return any(s.endswith('.git') or s.startswith('tmp_pack') for s in p.parts)
atoms=load('manual-atomic-clauses.json');old=load('old-locator-disposition.json')
cons=load('consumer-candidate-dispositions.json');facts=load('sourcefact-consumer-receptions.json');ledger=load('reading-ledger.json')
ids={r['id'] for r in atoms['records']}
refs={v for r in old['records'] for k in ['explicit_manual_child_ids','manual_child_assertions'] for v in r.get(k,[]) if isinstance(v,str) and v.startswith('KAR-')}
assert len(ids)==4792 and len(refs)==4748 and refs<=ids
assert sum(r.get('formal_denominator_role')=='COUNTED_INDEPENDENT_FORMAL_CLAIM_OCCURRENCE' for r in atoms['records'])==4732
assert len(old['records'])==2219 and len(facts['records'])==135
assert collections.Counter(r['status'] for r in cons['records'])=={'RECEIVED_LOCAL_STATIC_DOWNSTREAM_OPEN':476,'RECEIVED_NAMED_BOUNDED_CONTRIBUTION_DOWNSTREAM_OPEN':227,'COMMENT_OR_INACTIVE_DEFINITION_NO_RUNTIME_CONSUMPTION_AT_THIS_LOCATION':10,'ATTRIBUTE_DECLARATION_COMMENT_NOT_VALUE_CONSUMER':1}
assert len(cons.get('additional_discovered_lexical_candidates',[]))==2
fullR={r['path'] for r in ledger['records'] if r.get('repo')=='R' and r.get('status')=='FULL_READ' and not r['path'].startswith('PBS/')}
fullPBS={r['path'] for r in ledger['records'] if r.get('repo')=='R' and r.get('status')=='FULL_READ' and r['path'].startswith('PBS/')}
assert len(fullR)==124 and len(fullPBS)==36
originalR={s['path'] for f in facts['records'] for s in f['original_record'].get('sources',[])}
formal={r['path'] for r in old['records']}
assert len(originalR)==77 and originalR<=fullR and len(formal)==13
gitchecks=[]
for root,commit,paths in [(R,'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',originalR),(PROJECT,'fd1df570cad987dc3852a3b958f03916e317f7fe',formal)]:
    for path in sorted(paths):
        raw=(root/path).read_bytes();fixed=subprocess.run(['git','show',commit+':'+path],cwd=root,capture_output=True,check=True).stdout
        assert raw==fixed
        gitchecks.append({'path':path,'commit':commit,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'fixed_git_bytes_equal':True})
jsonchecked=0
for path in B.rglob('*.json'):
    if not transport(path.relative_to(B)):
        json.loads(path.read_text());jsonchecked+=1
receipts=[
 'received/pcr-bulbasaur-finite-reception.v1.json',
 'received/media-messages-complete-body-finite-reception.v1.json',
 'received/developer-wp75-map-filename-finite-reception.v1.json',
 'received/mg-http-finite-reception.v1.json',
 'received/mg-http-finite-reception.mandatory-load-binding.v1.json',
 'received/ui-shape-color-area-residual-finite-reception.v1.json',
 'received/root-bootstrap-finite-new-joins.v1.json',
 'received/root-bootstrap-finite-new-joins.mandatory-path-clarifier.v1.json',
]
sign={'status':'QUALIFIED_CURRENT_PRIMARY_SOURCE_STATIC_COMPLETE','signed_utc':START,'actual_reader':'/root/kernel_atomic_reception','formal_files':13,'independent_formal_claim_occurrences':4732,'working_records':4792,'noncounting_aliases':16,'noncounting_source_forward_notes':44,'old_locators':2219,'semantic_locator_bindings':1723,'layout_table_purposes':496,'original_sourcefacts':135,'sourcefact_manual_scope_groups':31,'original_lexical_candidates':714,'candidate_dispositions':cons['summary'],'additional_method_locations':8,'additional_discovered_lexical_locations':2,'own_nonPBS_source_FULL':124,'own_PBS_FULL':36,'all_current_necessary_material_received':True,'whole_global_domain_PASS':False,'target_business_execution':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'}
historical={'Timer':'Originalrawprobe UNVERIFIED; completeoldcanonical/counter/actualcriteria read, currentstaticvectors/refreshsubstitute limitretained.','HTTP':'Originalrawprobe/probe-v1/probe-result-v2 UNVERIFIED; currenthelperdefinitions+actualMGcaller+historicalcriteria received, no current/old hostexecutioncredit.','GR3_map_citation':'CurrentcompleteMapFactory/Overworld sourceprojection received; fullGR3-M03-004 historicalqualification not inherited.','dedup':'Onlyactuallyreceivedboundedrootcanonical records adopted; wholeearlyhistory/globalaliasdedup remainsroot scope.'}
p=load('progress.json');p.update(state=sign['status'],updated_utc=START,final_manual_atom_denominator=4732,explicit_manual_atom_subset=4792,own_primary_full_read=13,own_reference_full_read=124,own_reference_full_read_non_PBS=124,own_PBS_full_read_paths=sorted(fullPBS),all_sourcefacts_received='All135completeoriginaloperativeclaims disposed in31specificcurrentmanualscopegroups; F101rejected, F134/135oldnavigationrejected/currentWP75joinclosed; notwhole-domainPASS',current_primary_signature=sign,final_primary_task=True,historical_evidence_qualifications=historical,material_limit=False)
write('progress.json',p)
ledger.update(updated_utc=START,current_primary_signature=sign,current_selected_final_receptions=[identity(n) for n in receipts],source_credit_policy='ActualownFULL only; namedcompletefinitequalifiedfacts retainoriginalreader; no inheritedbinary/PBSliteralFULL.',readset_semantic_qualification='All135completeoriginalfacts and2219operativeoldlocators/currentmeanings read; repeatedadministrativeidentitylibrary notclaimedvisuallyreadinfull. Latestroot explicitlypermitsnecessaryoperativeobjects andno recursiveadministrative reread.')
write('reading-ledger.json',ledger)
g=load('coverage-gaps.json');g.update(updated_utc=START,current_primary_signature=sign,current_primary_required_unread=[],current_primary_required_unreceived=[],material_limit=False,historical_receipts=historical,current_unreceived_lexical_candidate_count=0,current_unreceived_lexical_candidates=[],old_locator_semantic_denominator=4732,partial_old_locator_bindings_not_completed=0,manual_subset_not_denominator='SUPERSEDED:4776earlycountincluded44sourceforwardnotes; currentformaldenominator4732/working4792',PBS_remaining_paths_interpretation='37physicalpathsnotownrawFULL, not37unreadrequiredclaims. Exactnecessaryscope/qualifiedproducer receipt inpbs-necessary-primary-scope.v1.json.',dynamic_consumer_denominator='OPEN_DISCOVERY_NOT_GLOBAL_EXHAUSTION; currentformalclaims bounded andqualified, no allcallbacktheorem required.')
for group in g['primary_formal']:
    path=group['path'];group.update(semantic_exhaustiveness='Allcurrentformalmeaning/qualifiers handdecomposed; finalcount excludesexplicitaliases/sourceforwardnotes; no host/globaldomainPASS',still_without_named_child_binding_old_ids=[],current_claim_occurrences=sum(r['formal']['path']==path and r.get('formal_denominator_role')=='COUNTED_INDEPENDENT_FORMAL_CLAIM_OCCURRENCE' for r in atoms['records']))
write('coverage-gaps.json',g)
i=load('interfaces.json');i['updated_utc']=START;i['current_primary_signature']=sign;i['final_complete_finite_receptions']=[identity(n) for n in receipts]
for row in i['interfaces']:
    row.setdefault('previous_checkpoint_open',row.get('open'))
    if row['id']=='KAR-I-PBS':row.update(status='CURRENT_PRIMARY_NECESSARY_PRODUCER_SCOPE_RECEIVED',accepted='36ownPBSFULL; completeBULBASAURliteral+commonpremise; actualPBS-battlefieldcontracts; priorcompleteworld/berry/encounter/type/ability/Shadow/Regional/Trainerfixtures. Current5facilitylist/10paths+2unreferencedFancy exactexistence received.',open='Whole37additionalrawfilesnotclaimed; currentprimaryonlynecessaryliteral/schema/existence/declaredU03boundary received. No allvariantcompatibility/runtimePASS.')
    elif row['id']=='KAR-I-INTL-MEDIA':row.update(status='COMPLETE_NECESSARY_SERIALIZED_BODY_FACTS_LOADER_AND_FINITE_CONSUMERS_RECEIVED',accepted='Completeoriginalmedia31bucket/85hash/10697pairquantifiedfacts,17semanticfacts+5exactnon_equalpairs+premises/sourceidentity actualreceived; originalmediaFULL retained. Main49 loader+mandatorypathcorrector andIntl/Compiler15producer+Traineridentity finitefacts received.',open='HostMarshal/currentselectedlanguage/runtimepixels/audio/allassets unexecuted; originalcorpusreaderFULL isnotreceiverliteralFULL. No allglobaldynamicconsumers proof.')
    elif row['id']=='KAR-I-CONFIG':row.update(status='ALL_CURRENT_FINITE_CENSUS_MEANINGS_AND_PURPOSES_RECEIVED',open='No original714candidate semanticallyunreceived. Dynamic/transitiveglobalexhaustion notclaimed; currentqualifiedoverview/definitionscope complete.')
    row['current_primary_required_unreceived']=False
    row['whole_domain_approval']=False
write('interfaces.json',i)
inp=load('input-identities.json');inp.update(updated_utc=START,final_primary_signature=sign,final_complete_selected_receptions=[identity(n) for n in receipts],publication_exclude='Every*.gitdirectoryandtmp_pack transport scratch excluded; no deletion/readcredit.')
write('input-identities.json',inp)
nextstep=load('next-dispatch.json');nextstep.update(updated_utc=START,state='NO_REMAINING_REQUIRED_CURRENT_PRIMARY_WORK',current_work='QualifiedSOURCE_STATIC finiteprimarysignature complete. Rootmayactualreceivefinal10+specificfrozencontributions; no newtask/spawn/R9/TS/update authorized.',retained_work=[],current_remaining_consumer_ids=[],current_primary_signature=sign,historical_evidence_qualification=historical,responsibility_transferred=False,proposals='Earlier4shardsremainPROPOSED_NOT_APPLIED_0START; neveractualtransfer ornewcontext/vote.')
write('next-dispatch.json',nextstep)
execution=load('execution-ledger.json');io=[]
for path in sorted((B/'io').glob('*.json')):
    d=json.loads(path.read_text())
    if 'underlying_exit_code' in d:io.append({'path':str(path.relative_to(B)),'started_utc':d.get('started_utc'),'ended_utc':d.get('ended_utc'),'underlying_exit_code':d['underlying_exit_code']})
execution.update(updated_utc=START,current_captured_read_IO=io,target_business_execution='NOT_EXECUTED',update_status='UPDATE_NOT_STARTED',final_primary_signature=sign,all_direct_command_UTC_and_stdout_captured='NO; platformpreservesdirecttooloutputs, older/currentdirectmetadatahelpercommands notallmirroredinIOfiles. No guessedstart/endtimes or fabricatedcompleteI/O claim.',known_failed_helper_operations=[{'operation':'AIhandlernavigationwrongprefix ValueError','clock_after_utc':'2026-10-16 12:57:36 UTC','credit':0},{'operation':'MGLoadbindingselection generatorKeyError','clock_after_utc':'2026-10-16 13:13:18 UTC','credit':0},{'operation':'Sourcefactscopefreeze NameErrornotout','clock_after_utc':'2026-10-16 13:19:02 UTC','credit':0},{'operation':'Finalscopehelper SyntaxErrorandlen','clock_after_utc':'2026-10-16 13:31:01 UTC','credit':0}],failure_time_policy='Theseareactualclockafterreadouts, not operationstart/end. Failedhelpersretained0credit andfixedbeforepersistentsemanticclaims; actualcommands/results remainplatformevidence.')
write('execution-ledger.json',execution)
report=f'''KERNEL 第八轮当前 primary 的有限静态审查已完成。状态：QUALIFIED_CURRENT_PRIMARY_SOURCE_STATIC_COMPLETE。仅签本人已实际接收的固定 13 份正式合同及必要源事实、前提和消费者；不签全局 PASS。实际签署时点 {START}。

固定 B8 为 fd1df570cad987dc3852a3b958f03916e317f7fe，formal tree 为 f292698cdd4a8e725525a9be6dc34b75faaf151e；R 为 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。原 77 个源全部本人全文；扩读后非 PBS 本人 FULL 为 124，PBS 本人 FULL 为 36。完整具名贡献保留实际原 reader，未改成本人 source/PBS/binary FULL 或第二票。请求模型/effort/tier/speed/Fast 与实际未权威回显字段分别保留 UNVERIFIED。

最终分母为 4,732 条独立正式 claim occurrence：4,792 条工作记录中，16 条明确 alias 与 44 条早期 source-forward 摘要不重复计数。74 个统计目录旧复合项各拆为单位/更新类别/责任导航三个独立 facet；原有合法前提、实际写点、取消及异常前缀保留。数字是人工子义处置后的计数，不是行、分号、方法或旧 locator 的替代。详见 [原子记录](manual-atomic-clauses.json)、[facet 差异](atomic-current-joins-and-denominator-refinement.v1.json) 和 [最终分母用途分类](atomic-final-denominator-source-notes.v1.json)。

2,219 个旧定位全部处置：1,723 个绑定完整手工当前子义，496 个为精确 heading/table/layout 用途。4,789 条 locator→child 引用无悬空；重用同一 child 不再增加分母。135 个完整原 fact 逐义在 31 个手工 scope 组处理；F101 原 callsite 记录断言拒收，F134/135 原 WP10 导航拒收而当前 WP75 有限 owner 接合已闭。见 [135 fact 当前契约](sourcefact-current-scope-reconciliation.v1.json)，必须同时使用 [Compiler 行数澄清](sourcefact-current-scope-reconciliation.mandatory-compiler-lines.v1.json)：Compiler001 真实 1–1117，原叙述 1010 错误不产生阅读信用。

原 714 词法候选为 476 本人有限意义、227 具名完整贡献、10 注释用途和 1 属性声明用途，未接收 0；另 8 方法型位置与 2 新发现词法位置分别保留。此为实际收到的有限集合，未声称动态/传递消费者穷尽。调用定义、配置快照、真实写点、正常/失败/取消/部分提交与保存/重载接口按各条原子和完整有限包接合；未知 native/Demo/事件调用者及正文明确 U01/U03/U09 限定不被改成成功或材料缺失。

PBS 按正式实际声明接收必要完整 producer 值及共同前提。BULBASAUR 完整 25 显式字段、12 省略默认和身份已实际接收，支持目录速度45/特攻65/特防65；不授另897条或全文件。其余未本人全文的37物理路径仅在当前所需 schema/字段/候选存在性/显式引用与手动选择限定上处置，不声称全部 literal/变体组合兼容。见 [必要 PBS scope](pbs-necessary-primary-scope.v1.json)。

媒体完整有限贡献已接收31桶/85hash/10697pair/178links的实际原 reader 资格、17完整语义事实、5对实际非等键/body及共同前提；原 body 全文信用留媒体 reader，不冒本人阅读10697 literal。默认语料不等于当前语言、文本效果代码或 native Marshal/图像/音频运行。Main49行完整 loader、必要 Intl/Compiler/实际指定资源消费者分别具名；见 [完整媒体有限回执](received/media-messages-complete-body-finite-reception.v1.json)。

保留既有 root 的 KER001/002/003 狭窄裁决；MapSave 仍 TRIAGE_ONLY_NOT_REQUIRED，不挂 KER003，当前 WP75 已明记吞异常/nil/不报告。Emergency 无新增 required，GR7-M04-001 是紧急保存 optional，不作 Encounter alias。本人非提出者追加 after-all-hits、Slot、EggGroup 和参与者更新点有限反证均交 root；Slot/EggGroup 已有 root 有限 required、其余按实际完整裁决保留。Hash 完整候选与 root NO_REQUIRED_BOUNDED_SCOPE 已接收。此处不新增 required/optional/context/vote、不改正式或参考源。

历史 Timer/HTTP 原 rawprobe 均 UNVERIFIED：原完整 canonical/counter/实际 criteria 已读，不能代原始执行。当前 SOURCE_STATIC/DERIVED_VECTOR 限定签署不继承旧执行，四个精确历史原子另标资格。GR3 地图恢复引用不继承全历史 PASS，当前源投影独立已读。整个历史 alias/dedup 仍由 root 处理。

业务、游戏、宿主与 Demo 全部 NOT_EXECUTED；UPDATE_NOT_STARTED。没有 commit/push/install/spawn 或 R/formal/planning/audit 修改。真实阅读 I/O 与已捕获 UTC/exit 见 [执行账](execution-ledger.json)；直接工具元数据命令未全部另存原始 stdout/完整开始结束时点，保平台证据并明确资格，不倒填或宣称完整镜像。失败 helper 与早期时间文字纠正均保留0信用。所有 *.git/tmp_pack 均为传输 scratch，排除发布清单；原字节不删除。

当前 primary 没有尚需亲读/接收的必要材料。原子、135 fact、2,219 定位及接口的完整具体限定保留在十件交付，root 仍须实际接收后独立作全局裁决。下一步仅 root 审收，不启动 R9/TS/整改。
'''
(B/'review.md').write_text(report)
ten=['review.md','progress.json','input-identities.json','reading-ledger.json','manual-atomic-clauses.json','sourcefact-consumer-receptions.json','old-locator-disposition.json','interfaces.json','coverage-gaps.json','next-dispatch.json']
assert all((B/n).is_file() for n in ten)
validation={'schema':'KAR-final-static-delivery-validation.v1','started_utc':START,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'required_ten_exist':True,'deliverables':[identity(n) for n in ten],'json_files_checked_before_finalwrites':jsonchecked,'counts':sign,'all_locator_child_references_resolve':True,'bound_unique_child_ids':len(refs),'git_checks':gitchecks,'semantic_credit':'Mechanical JSON/identity/reference/count validation only; actual manual meanings and real readers remain in semantic ledgers.','transport_excluded':'All*.gitdirectories/tmp_pack; notpartofdelivery orsemanticcoverage.','business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'}
write('validation.json',validation)
write('final-primary-signature.v1.json',{'schema':'KAR-final-primary-signature.v1','signature':sign,'ten_deliverable_identities':validation['deliverables'],'validation':'validation.json','qualifications':historical,'root_global_acceptance':'PENDING_ACTUAL_ROOT_RECEPTION_NOT_SELF_SIGNED'})
print(json.dumps({'signed_utc':START,'finished_utc':validation['ended_utc'],'signature':sign,'json_validated':jsonchecked,'fixed_git_equal_files':len(gitchecks),'ten':10,'captured_IO':len(io)}))
