"""Record explicit reviewer judgments; never infer semantic PASS from generation."""
from pathlib import Path
import json,datetime,hashlib,gzip,os,subprocess
T=Path(__file__).resolve().parent
UTC=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(name,obj): (T/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
reader=os.environ.get('CODEX_THREAD_ID','UNVERIFIED');assert reader!='01a143b2-fc07-7339-ab2f-055dba6bc023'
full={
 'report.md':'作者的整体完成声明及边界已读；不采纳为独立完成事实。',
 'completion-scope.json':'各轮分母与非必修分类按声明接收；实际完整接收另判。',
 'unread.json':'原作者必需未读0与6份未给全文信用的用途已读；不继承为本审者未读0。',
 'purpose-dispositions.json':'10份的用途及行政路由规则已读；业务正文不能由路由标签豁免。',
 'consumer-review.json':'四条接口的全部前提、对照、反例、外推排除已读，有限独立核对见interfaces。',
 'consumer-reads/manifest.json':'20包固定身份/全部声明范围已读；本人实际输出范围另列。',
 'history-current-acceptance-records.json':'12记录的全部字段已读作被接收主张；底层证明未齐，不给12/12完整签收。',
 'semantic-atlas/association-transport.json':'压缩/解码双身份及惰性恢复规则已读。',
 'build_semantic_atlas.py':'完整读懂字典值去重与行政路由；只做工具静态审查。',
 'semantic-atlas/chunk-001.txt':'V00001–V00088精确值已读；未读全部出现上下文，不作这些出现次数的全接收。',
 'inputs/delegation-prompt.md':'原任务全文范围与旧禁止push条款已读；本次用户明确授权专用分支普通push优先。',
 'originals/r5-u03-actual-fail.md':'旧actual FAIL完整正文，原消费false反例与原工具PASS不抵消FAIL保留。',
 'originals/r5-u03-limited.md':'一行新审+59原静态复用及10项原有限复用，非11项新全文复核。',
 'originals/r5-u08-candidate-fail.md':'14门与G03/G09旧FAIL、三处动作措辞完整正文。',
 'originals/r5-u08-actual.md':'14门的限定组合与20旧全文+UI三行上下文复用，不代原21篇新读。',
 'originals/r5-u08-final.md':'CLOSE01–07只签确切关闭候选；唯一激活另需准确回执。',
 'originals/sc-u07-001-erratum.json':'完整错误字段、正确前提、原独立决定、后继clarifier和排除范围已读。',
 'originals/r5-limits-and-missing-materials.md':'L01–L13全文及运行分期/政策边界已读作历史资格，不继承R8实测。',
 'additional-input-bindings.json':'原5份mode/tree未知完整保留；本次独立fetch后身份另行解除。',
 'process-evidence.json':'原失败/截断/脚本中断/anchor补读与发布前清理声明全部保留。',
 'preflight.json':'原作者预检只属其原环境时点。',
 'inputs/AGENTS.md':'与本次先全文读的根AGENTS精确字节关联，一次信用。',
 'inputs/eighth-global-review-prompt.md':'与本次固定合同全文精确字节关联，一次信用。',
 'inputs/review-SKILL.md':'与本次固定合同全文精确字节关联；该skill不用于审计记录正文修订。'
}
readrows=json.loads((T/'input-recovery.json').read_text())['files'];byblob={r['git_blob']:p for p in full for r in readrows if r['relative_to_target_task']==p}
entries=[]
for r in readrows:
 p=r['relative_to_target_task'];alias=byblob.get(r['git_blob'])
 entries.append({'object':p,'identity':{k:r[k]for k in ['mode','git_blob','bytes','sha256','remote_path_at_target_commit']},'reading':'FULL_BODY_READ'if p in full else 'EXACT_BYTE_ALIAS_OF_READ_BODY'if alias else 'NOT_FULLY_READ','purpose':full.get(p,('精确同字节别名，原用途不扩大；共同正文只给一次信用。 alias='+alias)if alias else '文件已恢复核身份；当前有效字段尚未独立逐项接收，不能以行政/历史/生成标签自动豁免。'),'whole_object_reception':'NOT_ACCEPTED_AS_COMPLETE_EFFECTIVE_SEMANTICS'})
receipts=[]
for p in sorted((T/'evidence/presentations').glob('*.json')):
 d=json.loads(p.read_text());d['receipt']=str(p.relative_to(T));receipts.append(d)
# These bodies were actually presented and read in this turn, independently of target ledger labels.
originals=[{'logical_path':p,'reading':'FULL_BODY_READ','qualification':q}for p,q in [
 ('tasks/R7-H12/report.md','原资格/原程序越界事实；不继承6857值的阅读'),
 ('tasks/R7-H12/preserved-special-history.json','完整SC错误/纠正/clarifier和五报告历史身份与范围'),
 ('tasks/R7-H05/execution-qualification.json','全执行家族/失败/重复/退出未知/替身和程序事件'),
 ('tasks/R7-H05/report.md','115索引/41正文/74未全文及原任务分工、不继承其它正文')]]
save('reading-ledger.json',{'schema':'gr8.receive-external-h.reading-ledger/v1','reader_actual_context':reader,'updated_utc':UTC,'target_entries':entries,'original_full_body_reads':originals,'original_full_body_bytes':42590,'original_payloads_purpose_complete':0,'presentation_receipts':receipts,'contract_reading':'完整task prompt、完整global prompt1-EOF、SKILL1-EOF、适用根AGENTS1-EOF；readset全部357行以可逆去共同前缀表1-120/121-240/241-357读完。','early_output_scope':'早期全文及readset只有平台工具日志，无独立本地原始stdout/UTC；没有倒填。后期输出receipt只记真实生成时刻，显式判断由本ledger负责。','atlas_actual_read':{'exact_values':['V%05d'%i for i in range(1,89)],'not_read_exact_values':['V%05d'%i for i in range(89,6858)],'all_occurrence_contexts_received':False,'context_rows_read':0,'schema_binding_rows_fully_received':0,'nested_reason_rows_fully_received':0},'supplemental_actual_text':{'file':'evidence/admin-original-actual-text-check.json','read_unique_long_values':28,'current_source_and_B8_validation':'NOT_COMPLETED','first8':'原始路由检查输出及D4756/D4781上下文全文','remaining20':'单独连续9–28完整输出'},'truncations_retained':[{'attempt':'初次GitHub connector readset/full output','status':'TRUNCATED_NO_FULL_READ_CREDIT','replacement':'本地可逆357行三块全文读取'},{'attempt':'helper+readset1-85批输出','status':'readset部分截断，不给该尝试全文信用','replacement':'同上357行三块'},{'attempt':'EV/U03/SC合批输出','status':'中间U03末段/向量截断','replacement':'U03-receiver252–274、U03-vectors274–300、SC-source997–1133单独完整补读；其余可见完整段按receipt记录'}],'new_behavior_execution':0,'vector_execution':'NOT_EXECUTED','semantic_status':'INCOMPLETE'})
interfaces=[
 {'id':'EH-CONSUMER-SC','current_effective_meaning':'六族按固定先后顺序匹配完整合法旧调用行；普通捕获体不跨LF、外围空白与独立行门分别成立，改写赋给整个字段。不能由旧错误跨LF字面或历史六样本签跨体LF/六族运行。','source':['SC-source951–1134（997–1133完整方法另读；979–995完整分词方法）'],'B8':['SC-receiver202–255（225–242六族表、参数条件与重访条款）'],'ordinary_and_boundary':'合法单行核心调用命中；括号体内LF且无其它合法调用行不命中；另有合法完整独立调用行可整字段丢外围文字。可选尾参逐位置存在再判文本，未规定的额外尾参不添规则。','independent_reason':'固定R六个literal无m/内联选项；全字段赋值已在各完整分支读到。官方Ruby3.1 Character Classes/Anchors/Options另外全文读到相关段；这是静态对照，无表达式运行。','strongest_no_required':'B8六族门已准确写出，未建立需要改B8的矛盾；不要求恢复原错误前提。','remaining':'fix_event_use1135–1582完整driver/caller尚未读；因此同轮/次轮重访与整个producer GR5-M12-002仍未全接收。','status':'FINITE_LINE_GATE_CONFIRMED_WHOLE_INTERFACE_OPEN','documentation':'https://docs.ruby-lang.org/en/3.1/Regexp.html'},
 {'id':'EH-CONSUMER-U03','current_effective_meaning':'六FEATHER及WING效果/上限绑定只证明对应EV增加；有效消费还取决于非重要和消费位。效果成功与库存扣减分开；队伍普通刷新先于外层扣减。','source':['U03-data110–210（相关构造/消费谓词到end）','U03-consumers601–767（644–706与710–753完整方法，补足原摘录缺753结束行）','EV-handlers752–835（六对完整注册/复制762–832）','EV-helper388–449（401–443完整三个辅助）'],'B8':['U03-receiver100–155、212–274；缺失252–274单独补读','U03-vectors274–300，关键294'],'ordinary_and_boundary':'qty1余量足、合法非重要WING省略/true且后段正常：EV+1、扣1。独立改Consumable=false：EV+1、库存保持。取消qty<=0或首份无额度返回假；先有成功再触限保留部分，外层依返回真/qty扣，不推事务。','independent_reason':'数据false保留而重要物消费被谓词再拦；六别名复制handler没有重写数据消费位；helper返回布尔非成功份数；两外层消费守卫独立存在。','strongest_no_required':'当前294行已有准确消费前提；旧FAIL依旧正确，新一行限定修复能同时成立，无需再改当前B8。','remaining':'GR5-M05-004其余参数/战斗等所有schema单元及92 producer人口未全部实读；此接口不签whole finding。','status':'FINITE_CONSUMPTION_FACTS_CONFIRMED_WHOLE_PRODUCER_OPEN'},
 {'id':'EH-CONSUMER-SUMMARY-PARTY','current_effective_meaning':'显示取个体图可在资源匹配前由动态形态读取提交状态；取消换位只无换位动作写入，已提交显示/盒侧前缀不撤销。','source':['form-producer130–215（form147–184完整）','form-time415–443、467–491（两限时handler完整）','form-request80–145（取图/图标完整入口）','form-sprites1–80、112–152（相关setter完整）','summary-consumer96–151、152–183、284–335、336–378（117–182/303–377完整）','party-refresh162–232、269–276、855–899、966–977、1370–1415'],'B8':['form-receiver173–202','summary-receiver214–234','current-ui-cancel-vectors190–250，A05/A06/A41'],'ordinary_and_boundary':'FURFROU1/t恰432000保留，432001动态提交0；战斗/仓库读存储；forced0只返回0而存储1/t保留。无过期读的取消不强制提交；资源失败不回撤此前写入。','independent_reason':'普通form先forced/模式guard，再处理动态返回差异；setter先写/清缓存、handler、重算、条件登记；图像入口先求形态再装图。B8三处动作措辞已经限定，旧candidate FAIL与新actual范围不互相回写。','strongest_no_required':'当前WP66A§8和三向量覆盖该有限反例；不需要把所有取消改成必有形态写入。','remaining':'完整目标选择/BACK控制流及EG-13/20孵化消费者未另全读；历史R4全部17/76及R5完整schema尚欠；明确不签这些范围。','status':'FINITE_DISPLAY_PREFIX_CONFIRMED_WHOLE_RECEPTION_OPEN'},
 {'id':'EH-CONSUMER-BOTTLE','current_effective_meaning':'指定初空timer的正常主队伍链：requested1先写，回调刷新动态读内层0并清timer，外层handler仍收到请求1只写新timer，最终存储0。新鲜timer与无中途读入口是独立对照。','source':['bottle-effect1208–1242（1216–1230完整）','form-producer147–179','form-time475–485','party-refresh完整相关setter/refresh/wrapper/item-use handler','form-stat-context94–130（species_data113–115完整）','form-registration180–238（register195–219完整）','U03-data119–198与U03-consumers710–753'],'B8':['bottle-receiver298–342（321–333完整）','form-receiver177–196','U03-vectors281–287'],'ordinary_and_boundary':'初0/timer空且panel/icon既建未释放，资源消息正常：最终0/新time/瓶1，效果真。初0且fresh timer或没有中途动态读的直接提交：保留1；之后1→0清time。回调资源失败只保留已到达前缀，不保证效果真或最终UI。','independent_reason':'提示式提交把回调置于写入与onSetForm之间；刷新setter重取图标触发动态形态，内层0先完成；外层后段不会重新赋请求形态。登记走species_data的simple形态，并受form_name/pokedex_form归一化；不保证请求1曾登记。','strongest_no_required':'B8§5.6.1给出完整限定顺序和三个对照，未建立当前错误；不能把特例推广为每次瓶子都归0。','remaining':'所有其它形态/工具/完整游戏可达性不在本有限事实信用内；目标原92合同/全部相关字段尚未完整接收。','status':'FINITE_BOTTLE_SEQUENCE_CONFIRMED_WHOLE_RECEPTION_OPEN'}
]
save('interfaces.json',{'schema':'gr8.receive-external-h.interfaces/v1','reader':reader,'utc':UTC,'records':interfaces,'whole_interface_final_acceptance':0,'source_publication':'参考完整文本只在受忽略.transport内及平台读取输出，提交仅身份/范围/行为分析。','producer_unread_blocks_whole_consumer_signature':True})
claims=json.loads((T/'inputs/target/history-current-acceptance-records.json').read_text())['records']
notes={
 'EH-HISTORY-01':'仅原报告/声明及V1–88值已读；R1剩余100/113/83的完整资格字段和5勘误9纠正8合同未全接收。',
 'EH-HISTORY-02':'229/21/341及308/33作为原单位已读；共同字段和逐owner绑定未完整接收。',
 'EH-HISTORY-03':'23/76与两个排除项的摘要已读；原excluded_R3及完整23/76尚未逐值接收。',
 'EH-HISTORY-04':'Summary有限当前形态事实作独立对照；原17/76、B5 16/75和c492 C01–C05所有证据未齐。',
 'EH-HISTORY-05':'激活/分母声明和关闭报告全文已读；92原完整合同/568criteria/570binding/206nested/632context尚未接收，不能签唯一激活的全部逐项语义。',
 'EH-HISTORY-06':'SC完整原erratum+preserved-special+六族完整方法+当前条款已读，支持准确LF更正；driver/整个旧ID尚欠。',
 'EH-HISTORY-07':'两份原FAIL/有限后继完整正文+当前消费数据/效果/helper/outer/向量独立对照，支持一行新审与59复用的限定，不签整11。',
 'EH-HISTORY-08':'candidate FAIL/actual/final三原报告全文，当前3行向量与动态链已读；全部14/7门底层与21共享/18依赖不能据摘要全接收。',
 'EH-HISTORY-09':'H05两原载荷全文接受其历史执行限定意义；原底层18进程未重新恢复审查，不能声称新18次运行或底层全链再验。',
 'EH-HISTORY-10':'14原非必修ID分类声明已读；908独有值、7块与237anchor所需完整上下文未读，不接受14条全部语义。',
 'EH-HISTORY-11':'L01–L13原全文按历史资格读完；六policy具体事实/输入尚未逐项接收，R8各材料/宿主也未重新全证。',
 'EH-HISTORY-12':'20原包全部指定范围已呈现并补必要方法end，另读当前UI3向量上下文；四条有限事实确认，整producer与其它必要caller/consumer仍OPEN。'}
save('reception-ledger.json',{'schema':'gr8.receive-external-h.reception-ledger/v1','reader':reader,'utc':UTC,'status':'INCOMPLETE','all_target_history_records':[{'id':x['id'],'subject':x['subject'],'claim_fields_read':'ALL_FIELDS_AS_CLAIM','independent_reception':'PARTIAL_EXPLICIT_SCOPE_ONLY','decision':notes[x['id']],'whole_record_final_accepted':False,'original_record':'inputs/target/history-current-acceptance-records.json#/records/'+str(i)}for i,x in enumerate(claims)],'whole_history_records_received':0,'source_facts':'interfaces.json逐事实；不把有限对照混成whole producer签名','root_prior_rulings':'未将root已有有限裁决作为本次独立真值；本次仅依据列出的完整原报告/当前R/B8范围。root未实读的其它裁决本次不采用。','remaining_available_not_received':{'atlas_values':'V00089–V06857（6769）；已读V1–88的全部occurrence上下文亦未全接合','schema_context_binding':'570binding、206nested、632context完整行及其指向值尚未完整接收；只打印过表头/首3行，信用0whole','R5':'frozen92全部完整原范围/568检查和producer-to-receiver逐项判定未完成','R1_R3_R4':'除明确片段，原完整资格/历史例外/有限后继未完成','nonmandatory':'14原记录、N0001–N0908、237anchor完整用途接收未完成','policy':'BAG-04、UTIL-03/05/11/12/13全部详细事实尚欠','administrative_routing':'180833leaf不能批量认可；已发现业务文本被original_actual_text规则路由，须逐对象核目的','finite_interfaces':'每条remaining见interfaces；不签未读producer贡献'},'unavailable_material_limits':[],'task_processing_limit':'本次单会话交付容量不足以对余下6769值及其上下文、绑定和定义消费者作真实逐项完整接收；它们实际可得，明确是本任务未完成工作，不是材料/宿主limit，也不豁免验收。','new_behavior_execution':0,'UPDATE_NOT_STARTED':True,'ready_for_root_task_final_acceptance':False})
proposal={'id':'RECEPTION-H-EARLY-EVIDENCE-001','classification':'RECEPTION_EVIDENCE_SCOPE_GAP_NOT_B8_REQUIRED','status':'OPEN_FOR_ROOT_DISPOSITION','target_commit':'11c057d9aed330c16312470f80f13d180f8e1e65','title':'原actual正文被整键归入行政路由，未证明其有效语义已呈现接收','evidence':['inputs/target/build_semantic_atlas.py#ROUTE_KEYS/original_actual_text及ancestor_admin','inputs/target/report.md#原值/当前值/签名原因已读声明','evidence/admin-original-actual-text-check.json','evidence/original-recovery.json'],'ordinary_control':'纯commit/path/hash及只含旧报告locator可按准确身份路由，无需无界重读旧报告。','minimal_counterexample':'D4756/1/original_actual_text包含新建道具口袋BACK返回0放弃、价格BACK返回0继续、描述ESC继续、登记/文件失败前缀等完整业务意义；不是单一locator。D4781/2还包含BP2/显式1省略/份量空值/SellPrice对照。','negative_evidence':'机械检查28个>80字符的不同original_actual_text，均无精确同值V组；对其中3条特定措辞在357文本载荷检索无命中。此结果只针对发布证明，不证明作者私有平台从未读过。','strongest_no_required_or_scope_explanation':'可能被视为旧actual字节证据，且相近行为由其它scope/reason值覆盖；目标不要求重复审旧formal全文。故不将它定为新B8缺陷、不计required，也不推断作者虚报。仍须逐指针说明当前有效意义、exact alias或可接受旧身份用途。','minimal_reception_contract':'由非作者逐对象确认有效业务值，读全原上下文和必要B8接收，不用键名自动行政豁免；如已有完整同值阅读，给准确值/occurrence/呈现凭据。','preserve_scope':'不改原作者目录/旧证据，不重开R5历史92或R7的27，不修改正式，不启动整改。','independent_counterreview':'本context不同于目标作者；此项为本context提出，最终裁决/任何required定性仍由真正非提出者root承担。','current_effect':'完整接收保持OPEN；本context已读这28长值本体，但没有全部当前source/spec验证。'}
save('findings.json',{'schema':'gr8.receive-external-h.findings/v1','B8_new_required_proposals':[],'reception_evidence_gaps':[proposal]})
save('proposal-counters.json',{'schema':'gr8.receive-external-h.counters/v1','B8_required_proposals':0,'B8_required_confirmed':0,'B8_optional_new':0,'reception_evidence_scope_gaps_proposed':1,'reception_evidence_scope_gaps_confirmed_by_nonproposer':0,'whole_task_final_acceptances':0,'whole_history_records_final_received':0,'target_author_context':'01a143b2-fc07-7339-ab2f-055dba6bc023','receiver_actual_context':reader,'context_source':'CODEX_THREAD_ID environment read, not source_thread_id','same_as_target_author':False,'new_contexts_spawned_by_this_task':0,'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'standard','Fast':False},'actual':{'model':'UNVERIFIED','effort':'UNVERIFIED','tier':'UNVERIFIED','speed':'UNVERIFIED','Fast':'UNVERIFIED','UUID':reader},'execution':{'reference':0,'model':0,'host':0,'Demo':0,'native_media':0,'real_save':0,'vectors':'NOT_EXECUTED'},'UPDATE_NOT_STARTED':True})
save('progress.json',{'task':'receive_external_h_early_qualifications','reader':reader,'utc':UTC,'status':'INCOMPLETE_CAPACITY_BOUNDED_DELIVERY','blocking_work':'reception-ledger.json#/remaining_available_not_received','transport':'357/357 identity verified; own publication readback follows','spawned':0,'update_started':False,'root_task_final_signed':False})
print('Recorded explicit partial review; whole task INCOMPLETE, no automatic PASS')
