"""Assemble the root's signed scoped review, reading distinctions and report."""
import gzip
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

OUT=Path(__file__).resolve().parent
ROOT=Path(__file__).resolve().parents[5]
BASE=ROOT/'review/remediation-eighth-20261016-prepare'

def read(name):
    p=OUT/name
    if not p.exists():
        return json.loads(gzip.decompress(Path(str(p)+'.gz').read_bytes()))
    return json.loads(p.read_text())

def write(name,o):
    (OUT/name).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')

def main():
    ids=read('per-id.json'); joins=read('root-cross-batch.json')
    p=read('final-protection-facts.json'); l=read('final-current-locator-facts.json')
    assert p['all_mechanical_comparisons_matched'] and l['all_mechanical_comparisons_matched']
    m=read('final-sync-mapping-result.json')
    assert not m['unresolved_mechanical_differences']
    assert all(x['actual_integrated_verdict']=='PASS' for x in ids['records'])
    assert len(ids['records'])==39 and len(joins['records'])==10
    now=datetime.now(timezone.utc).isoformat()
    progress=read('root-progress.json'); fm=read('final-formal-reading-map.json')
    current=set(progress['complete_direct_new_formal_paths'])
    formal=[]
    for v in fm['complete_changed_formal38']:
        ident=v['final_identity']; path=ident['path']; direct=path in current
        assert direct or v['old_final_full_bytes_equal']
        formal.append({'identity':ident,'root_credit':'CURRENT_DIRECT_WHOLE_FILE' if direct else 'OWN_PRIOR_SAME_PURPOSE_WHOLE_FILE_REUSED',
            'original_reader':'same root01a14a49-64c1-764e-b294-c70bb87680fd',
            'own_prior_reading':None if direct else v['old_reading_declaration'],
            'root_current_reception':'PASS: manual cumulative behavior/consumer review; all ten joins separately signed',
            'foreign_reader_FULL_transferred':False})
    assert len(formal)==38 and sum(v['root_credit']=='CURRENT_DIRECT_WHOLE_FILE' for v in formal)==25
    reading={'schema':'r8-final-root-reading-and-qualified-reuse/v1','recorded_utc':now,
        'reader_context':'01a14a49-64c1-764e-b294-c70bb87680fd','current_turn':'01a14c51-69d1-76ee-ae14-d19ff7c3bc83',
        'configuration':'configuration-and-startup.json; explicit parent create default/ultra and continuation admission, all runtime echoes UNVERIFIED',
        'formal_whole38':formal,
        'canonical_contract_reception':{'records':39,'unique_typed_values':2900,'all_uses':34492,'unicode_received':[0,237761],'prompt_unique_shell_paragraphs':109,'shell_unicode_received':[0,85502],
            'method':'Complete exact original typed values and complete original unique prompt shells received; all structure/order/purpose indices losslessly retained. Repeated exact values deduplicated,13 exact terminal metadata keys excluded only when every use has such a key.',
            'credit':'COMPLETE_EXACT_CONTRACT_CONTENT_RECEPTION; not literal FULL all33 carriers or source units they reference','raw_first_two_contracts':'KER00124288 andKER00229057 Unicode each directly whole record received'},
        'common_reads':'AGENTS, complete final protocol/manifest, originalDELIVERY/final-report/review-SKILL/fullhandoff prompt/manifest; applicable accepted/history/policy companion own-prior same bytes plus current complete unique content reception; original provenance preserved.',
        'provenance_reception':{'whole_reports':'All9 candidate independent reports, actual six/U02-U03/U04r2 report families plus own U06 actual report/results, U07 complete overlay, named creation/reception records and all nine ACCEPTED semantic objects received.',
            'data_reception':'Per-ID results received whole or complete required object projection; identity/transport arrays fully mechanically checked. Original candidate source ledgers qualify named existing readers, never root newly reading their sources.',
            'navigation_only':'provenance380 files/4395 parsed documents/3,151,490-char narrative and545149-char shell are complete retained navigation. Root does not claim entire huge streams freshly read; no helper FULL or semantic transfer.'},
        'routing_reception':{'whole_reports':'Final root/result/issue results, prior R3 root/result and all6 domain reports,3 recovery reports and review contract received. All7 final narrative deltas,7 unit/6 file source facts/future boundaries and7 patch after-values received directly.',
            'qualified_prior_credit':'Exact1baee final and342 prior complete artifacts175+75+111 received. Per736/2704 large matrices retain named original reviewers, individual source/purpose/nonimpact qualifications and original FAIL history; root does not restart a global tagging audit.',
            'fresh_current_check':'38 final changed whole files, all39 issue deltas and10 joins,51 changed-unit source bindings/21 new headings/2704 current locators mechanically compared to final5f; source/consumer meanings received from named final cumulative review and root current final-file assessment.',
            'navigation_only':'tagging28,132,054-char narrative/361 files sidecars are mechanically complete, not root semantic FULL of that stream.'},
        'roadmap':'All3 final files whole, originalFAIL and successorPASS reports, exact original-source diff and one-line repair read. Scope limited faithful persistence; no architecture/prototype/implementation approval.',
        'source':'root-source-reception.json + earlier root-progress source ranges; own prior44 direct source paths/ranges in exact U06 ledger, not all143 candidate units or563global files.',
        'mechanical_helpers':{'names':['/root/mechanical_inventory','/root/final_reading_navigation','/root/mechanical_inventory/final_navigation_only'],'semantic_FULL_configuration_credit':0,'new_independent_votes':0},
        'truncation_and_failed_navigation':'root-progress.json retains path/ref guesses and oversized partial displays; necessary gaps were repaired. Mechanical identities do not upgrade unprinted text. U05 identity arrays and all large navigation streams not claimed ownFULL.',
        'business_execution':'NOT_EXECUTED'}
    write('reading-and-reuse.json',reading)
    prov=read('provenance-reading-sources.json')['batch_reader_config_create_report_entries']
    batches=[]
    for b in prov:
        rows=[x for x in ids['records'] if x['batch']==b['batch']]
        batches.append({'batch':b['batch'],'actual_integrated_verdict':'PASS','required_ids':[v['id'] for v in rows if v['classification']=='required'],
            'selected_optional_ids':[v['id'] for v in rows if v['classification']=='optional'],
            'candidate':b['candidate_entry'],'candidate_independent':b['candidate_independent_entry'],'actual_independent':b['actual_independent_entry'],'accepted_receipt':b['accepted_entry'],
            'root_current_nonimpact':'Final affected whole files and all necessary joins received; byte correspondence is supporting evidence. Historical UI65U01 contribution is preserved under authorized U04 final receiver repair.',
            'blocking_dependencies':[],'new_ACCEPTED_or_CLOSED_registration':False})
    write('batches.json',{'schema':'r8-final-root-nine-actual-batches/v1','batches':batches,'actual_PASS':9,'actual_FAIL':0,'actual_BLOCKED':0})
    result={'schema':'r8-final-independent-overall-review/v1','signed_utc':now,
        'input_binding':ids['input_binding'],'artifact':ids['artifact'],'formal_source':'5f87743293290de2e219ecdd6c19e88280f60c9a','formal_tree':'93dc967b4cdb653359afc123d3b8b318d6475fdd',
        'overall_verdict':'PASS','scope':'Final R8 bounded actual integration, selected optionals, received cumulative routing and handoff/protection; not R9/global source rereview',
        'reviewer_is_author_or_integrator':False,'same_context_continuation_additional_votes':0,
        'configuration_evidence':'configuration-and-startup.json; original parent creation correction supersedes initial undefined-admission assertion; runtime fields UNVERIFIED_NOT_EXPOSED',
        'counts':{'required':29,'required_P2':2,'required_P3':27,'selected_optional':10,'per_ID_actual_PASS':39,'batches_actual_PASS':9,'cross_batch_PASS':10,'changed_formal_whole_received':38,'current_direct_whole':25,'own_prior_whole_reused':13},
        'gates':{'frozen_input':'PASS','39_limited_actual_semantics':'PASS','nine_candidate_actual_acceptance_chains':'PASS','ten_cumulative_joins':'PASS','cumulative_tagging_received_and_final_synchronized':'PASS','roadmap_faithful_persistence_reception':'PASS','development_handoff_limits':'PASS','protection_and_own_write_scope':'PASS'},
        'tagging':{'candidate':'7ed3e0554ac24339a7e61cab152f628037111644','independent_PASS':'1baee5d7346592478b72d8983b0109e1b2a5e2d9','retained_prior_FAIL':'34202eb7accfee48bb8761db88b340bd77f54a42','files_received':[175,75,111],
            'documents':131,'bodies':111,'catalogs':17,'shared':3,'WP_rows':87,'content_WP_rows':84,'phase_WP_rows':3,'current_headings':2704,'historical_headings':2683,'new_headings':21,'active':736,'retired':33,'metadata':33,'accepted_source_batches':9,'accepted_events':9,'bound_active':230,'event_uses':238,'target_contributions':40,'formal_contributions':39,'unique_changed_formal_paths':38,'pending_bound':0,'partial_bound':0,
            'destinations':{'framework':307,'Showdown':74,'collaboration':130,'MZ':225,'excluded':0},'all736_destination_verification':'PENDING','all736_phase_implementation_acceptance':'UNAPPROVED_UNIMPLEMENTED_NOT_ACCEPTED','new_full_tagging_global_audit':False},
        'blocking_findings':[],'unresolved_blocking_dependencies':[],
        'nonblocking_qualifications':[
            {'scope':'Old six-actual KER002 evidence prose','qualification':'Old all17bootup/BACKdefault wording overbroad; direct final source and final WP09/UI65/catalog correctly say fivebootup registrations and BACK0 wait. Preserve old report, do not propagate its prose into this verdict.'},
            {'scope':'U01 prior recheck entry','qualification':'Short old locator has3 matches33/61/102, not2; actual unique fixed locator and8reverification correct. Original qualified nonblocking note retained.'},
            {'scope':'U08 N01','qualification':'投入提示只在实际请求L365查找，位于内层loop前；final wording每次到达请求 does not require every-frame lookup. Original nonblocking precision retained.'},
            {'scope':'U09 author reading','qualification':'Original author AGENTS event/MG236–428FULL unproved; original independent reviewer supplementary FULL does not retroactively fill author credit. Current root qualified reception grants no author process certification.'}],
        'remaining_downstream_dependencies':[
            {'owner':'R8-INTEGRATOR','action':'Receive this independent PASS then register final ACCEPTED/CLOSED; reviewer does neither.','blocks_this_content_PASS':False},
            {'owner':'Integrator publication','action':'After exact report reception, refresh remote drift/protected rules/required reviews and CI; normal main merge only when all conditions met, then recoverable cleanup from refreshed exact retained refs.','blocks_this_content_PASS':False,'performed_here':False},
            {'owner':'Parent separate local task','action':'Preserve user local changes, later verify real local synchronization SHA/status against published main. Cloud workspace is not user local.','blocks_this_content_PASS':False,'performed_here':False},
            {'owner':'Implementation stage','action':'Fix target versions, four collaboration prototypes, scope/stage decisions, host/native/media/save/replay and implementation tests; all existing L01–L14 and historical limits retained.','blocks_this_content_PASS':False,'performed_here':False}],
        'business_execution':{'Ruby':0,'reference_game':0,'business_vectors':0,'host_media':0,'save_replay':0,'Showdown_framework_prototype':0,'qualification':'SOURCE_STATIC/DERIVED_VECTOR_NOT_EXECUTED and separate document/Git/Python TOOL_VALIDATION only'},
        'publication':'Content PASS signed now; ordinary own branch push and complete fresh remote readback must be bound by successor publication-readback.json and final external fullSHA. No future selfhash or main-merge claim.',
        'ACCEPTED_registered':False,'CLOSED_registered':False,'main_merged':False,'cleanup_performed':False,'user_local_sync_verified':False}
    write('result.json',result)
    req=[]; opt=[]
    for v in ids['records']:
        row=f"| {v['id']} | {v['batch']} | PASS | {v['final_locations']} |"
        (req if v['classification']=='required' else opt).append(row)
    report='''# R8 最终实际整合独立验收

**整体结论：PASS，限本次冻结的R8内容。** 29必改（2 P2/27 P3）、10个实际选入可选、9批actual integrated、10组跨批接合均PASS；本轮有限静态正确性阻塞0。没有替协调者登记ACCEPTED/CLOSED，没有合并main、清理分支或认证用户本地同步。审查自身发布/全包远端回读由后继回执及外部最终40位SHA绑定。

输入绑定 `8ab43a609e60430492b219f0dce14ef4fdb8e47f`，manifest `review/remediation-eighth-20261016-prepare/final/independent-review-input.json`，状态FROZEN_READY_FOR_INDEPENDENT_REVIEW；artifact `fd414a2c6ec0a0f746b48e0924e5692221ea5d5a`。最终正式源 `5f87743293290de2e219ecdd6c19e88280f60c9a`，formal tree `93dc967b4cdb653359afc123d3b8b318d6475fdd`。不以移动分支替代这些输入。

## 审者与阅读资格

当前审者context `01a14a49-64c1-764e-b294-c70bb87680fd`，续turn `01a14c51-69d1-76ee-ae14-d19ff7c3bc83`；是非作者/非整合者，曾独立验U06，未创作正式内容。原cloud创建参数gpt-6.1-sol/ultra/service_tier default及started回执、当前显式ultra续审/继承default由父任务实际创建回执证明。初期父缓存缺失所述undefined保留，后继原started回执已明确纠正。运行时model/effort/tier/speed/Fast无权威echo，全部UNVERIFIED，不用任务UUID或工具priority广告冒充。辅助context只做机械身份/解析/导航，语义、FULL、配置和新增独立票信用均0。见[配置](configuration-and-startup.json)。

完整接收AGENTS、原DELIVERY/final-report/review-SKILL、完整handoff prompt/manifest、最终协议/manifest，九批prompt和39合同的全部唯一原typed内容及原非JSON外壳；重复精确身份/值按用途去重。237761字符合同投影和85502字符外壳全部实际收到，保留原结构、顺序及全部用途。这不登记为所有载体或引用源的literal FULL。clean-document-revision仅用于判断正式修订的最终规范语气，不用它改写审计报告。

受影响最终正式文件38份整篇接收：25份当前直接全文、12份本人前次U06整篇及1份本人WP61整篇按相同字节/目的复用；各自原阅读账、当前身份及本次接合理由见[阅读分账](reading-and-reuse.json)、[直接读账](root-reading-ledger.jsonl)、[源范围](root-source-reception.json)。并非重新全读563源或全部131正式篇。共享世界目录822行、Creature目录183行及其它改变共享文件按整篇接收。全部9候选独立报告、实际报告及后继、9个ACCEPTED语义对象已经接收，FULL只归其实际原reader，不转授作者或当前root。

361打标及复审载体完整字节接收；final/prior root、6领域、3恢复报告整篇接收，7最终差异及7单元/6文件事实与未来边界、补丁after值直接核。大736/2704矩阵及380/361无损导航流只保机械/具名既有审查信用，不冒称root逐字新读全部工具stdout或重做全量打标。参见[全部来源导航](provenance-reading-sources.json)、[标签交付索引](tagging-reading-deliverables.json)。

## 逐项actual integrated结论

各项的完整合同、候选/独立报告、实际报告、原ACCEPTED精确commit/path/pointer、区分场景、前缀及未决依赖见[39项结构化裁决](per-id.json)。以下逐项不抽样。

| 必改ID | 主批次 | actual | 最终位置 |
| --- | --- | --- | --- |
'''+ '\n'.join(req)+'''

| 已选optional | 主批次 | actual | 最终位置 |
| --- | --- | --- | --- |
'''+ '\n'.join(opt)+'''

十项逐个具有有限理解/验证收益，归属U01一、U06三、U07一、U09五；本次实际全部被选入且有候选和actual独立范围，不从最初UNSELECTED倒推出最新仍禁止。UI003旧alias、计数/导航修词和未知数据有限入口均保。独立视觉policy仍UNSELECTED、单列，不并入39项。正文没有新增框架、转译源码或无关架构。

## 九批接收及跨批必要门

[九批链](batches.json)逐批均actual PASS。U02/U03为真实change-record入口，没有虚构manifest。U01原LOC失败与c877定位返修原样保留；U04六批r1中WORLD003实际FAIL原样保留，5f的UI65 L152/L210修复及40f428后继actual PASS才接最终两行。U01历史UI65接受只覆盖其启动/保存/No贡献，不冒领U04后继修复。U06原f791 BLOCKED及六批固定证据保持，原创建证明与实际完整阅读由同context续审8f71解决，续turn+0。九批ACCEPTED在累计打标前已实际存在，未推迟初次actual复核。审者本人不替owner登记。

[十组接合](root-cross-batch.json)全部PASS：X01保存/驻留/预览，X02Repel与战斗集合，X03faint音频与Slot图像，X04蛋群/Gift与EV，X05共享127ID，X06记录/回放/helper，X07No前共享名，X08历史overlay，X09整个WP67-A各阶段，X10旧alias/EXP与BR23。零语义编辑DAG边不使这些接收门为空。

两P2保留缺失计数而非0、原输入顺序、真实0/1/3席位与配置0/1动作集合；AI登记不自动补调度。玩家skip/NPC/蛋/伙伴/2v1/3v1/反序/双健康分别按前提。未推自动胜利、完整UI或未来Showdown健康队列。Creature目录127既有ID＝EG20/EN32/FC17/TT26/MG32，全部保留顺序与别名前缀，Factory/Triad/E贡献保持；MG32是子节，不能当全文件分母。

## 最终打标同步、交接与保护

固定打标7ed3e05的175文件、独立1baee5d7的75文件和前继34202eb7的111文件全部精确保留。接收其合格累计独立报告；不重开736功能全局打标。真实当前源从5f取，候选分支所保B8正式树不导入。7最终注记正确区分：173记录存储/回放，227负概率向下整除，596默认含濒死Repel，29/204/456总510但单项255越252的首HP门，32外层动画/预锁复位。原两P3七case FAIL不改写，后继对应PASS有界接收。

131路径＝111正文/17catalog/3shared；87WP＝84内容/3阶段，是不同分母。当前2704标题＝历史2683+新增21，736active/33完整retired/33metadata不混计；9接受事件、39issue、40贡献（39formal贡献/38唯一路径+U07 metadata1）、230boundactive/238event用途，pending/partial0。所有当前定位、引用和新heading消费者精确回接最终源；语义消费者依具名累计报告与root正式整篇/接合接收，不由hash单独授予。见[当前定位机械事实](final-current-locator-facts.json.gz)、[九批绑定](final-sync-mapping-result.json.gz)。去向框架307、Showdown74、协作130、MZ225、排除0；全部736去向待验证、阶段未批准、未实现/未验收。

三份framework-roadmap整篇及固定67d0候选、574bc独立忠实性PASS、前继FAIL和唯一恢复原句的修复均接收。详版“先分类再修改对应内容”与简版“就修正规格”是源原有措辞，忠实保存不代替实质架构裁定。live routing README、开发交接、known-limits保留规格/标签入口、L01–L14/native/宿主等具名限制与未来验证入口。

真实保护核验：远端main及第七轮delivery tag仍fd1df570；本地相应refs缺席按VERIFY_IF_PRESENT，不伪建。参考R8c591/tree7589保持clean；原global-review子树034734保持；正式树在prepared/artifact/binding/HEAD/worktree全为93dc967，131路径完整。1008输入载体逐字节绑定，1006非exception输入在artifact/binding/worktree完全一致，另4后继行政文件仅按声明差异接收。原报告、各批候选/actual/ACCEPTED和历史关闭回执保持。当前新增/修改严格限本目录；[保护事实](final-protection-facts.json)、[核心机械事实](final-mechanical.json.gz)不替代上面语义判断。未重跑只适用于作者B8工作树的scope guard来错误否决真实整合树。

## 非阻断资格及后继责任

旧六批actual KER002两处说明过宽：启动不是全部17默认，BACK哨兵0不返回默认选项；本审直接源及最终WP09/UI65/catalog已核为五bootup/等待正确，不传播旧说明。U01旧短locator三命中而说明写二、U08投入图实际L365请求而非内层每帧、U09作者未证FULL等原限定继续保留，不倒填原读者资格，不形成R9。

本次Ruby、参考游戏、业务向量、宿主音画、真实保存/回放、Showdown/框架原型新增执行均0；SOURCE_STATIC、DERIVED_VECTOR/NOT_EXECUTED、TOOL_VALIDATION分别记账。工具通过不授像素/发声/墙钟或兼容执行信用。

本次内容PASS后由协调01a14a04-b178-7567-a4eb-0f0bfac9a0d9接收并登记最终接受/CLOSED。最终正常合并前另核实时远端漂移、精确通过内容、分支保护/必需review和CI；清理须刷新精确refs和恢复来源。用户本地保全/同步由父另设本地任务，需真实最终SHA/status；云工作区不作本地同步证明。四协作原型、目标版本、用户首版/阶段决策及历史native/media/save等限制留实现阶段，不阻本有限内容PASS。当前无必须回修。
'''
    (OUT/'report.zh.md').write_text(report)
    progress['overall_verdict']='PASS_CONTENT_SIGNED_PUBLICATION_PENDING'
    progress['remaining_major_gates']=['ordinary own branch commit/push and complete fresh remote output readback','integrator-only final registration/merge/cleanup and separate parent-local sync, outside reviewer scope']
    progress['recorded_utc']=now
    write('root-progress.json',progress)
    print(json.dumps({'result':'PASS_CONTENT','required':29,'optional':10,'batches':9,'joins':10,'report_bytes':len(report.encode())}))

if __name__=='__main__':main()
