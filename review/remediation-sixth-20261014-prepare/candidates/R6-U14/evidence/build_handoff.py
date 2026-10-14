"""Bind the six author results to frozen contracts and actual candidate bytes."""
from pathlib import Path
import datetime,hashlib,json,re,subprocess
ROOT=Path(__file__).resolve().parents[5];OUT=Path(__file__).resolve().parent;BATCH=OUT.parent
C=json.loads((ROOT/'review/remediation-sixth-20261014-prepare/contracts/R6-U14.json').read_text())
manifest=json.loads((OUT/'candidate-manifest.json').read_text())
tool=json.loads((OUT/'author-tool-validation.json').read_text())
specroot='deliverables/final-specification-set/'
def vec(prefix,n):return [prefix+str(i).zfill(2) for i in range(1,n+1)]
vectors={'R6-D-LZ-001':['LZ36','LZ37','LZ38'],'R6-D-LZ-002':['LZ39','LZ40','LZ41'],'R6-D-PBS-C05':vec('R6-U14-C05-',5),'R6-D-PBS-C06':vec('R6-U14-C06-',3),'R6-D-PBS-C07':vec('R6-U14-CI',4)+vec('R6-U14-GR',5),'R6-D-DATA-C01':vec('R6-U14-FLAGS-',4)}
reason={
'R6-D-LZ-001':'完整新读收集、键规范化、运行回退、源681及生成1154/1162/1321锚、先添加物品后口袋消息与窗口换行处理；两个键的分隔字符不同。非提出者反证没有推翻收集次序；仅补运行消费后果。字节成员复核不当作加载器或真实查找执行。',
'R6-D-LZ-002':'完整新读控制帮助、图形战斗菜单、训练家卡和翻牌小游戏消费者：指定身份先查当前语言再传给资源入口；背景/标签各自独立。女性卡译后身份另过存在性门，失败可能走该调用者既有普通卡分支，不能据此给所有译后资源通用重试A。原48行图像矩阵全文已读；只新回源指定代表链，不给其它63调用位置冒签新全链验证。',
'R6-D-PBS-C05':'Type/Move/Item构造、省略编译路径与终检已新读：缺字段采用有限默认，Item复数独立。原反证认可新建编辑器既有Unnamed/???合同，未重复申报该入口；正文仅新增混合显式单数/省略复数及Type/Move有限原值。普通语言查找、价格/用途/消费与类别×威力旧门均保留。',
'R6-D-PBS-C06':'SpeciesMetrics及普通编译登记、查询命中/缺整条分支已新读。作者部分形态节先形成自身五组默认，查询不会逐字段继承；整条身份缺席才克隆基础并给空后缀。数据记录、档案/PBS和已布局精灵不同观察点，WP73-B §7.5和WP04 §5.5原保存门保留。',
'R6-D-PBS-C07':'物种Happiness非负格式、基础校验、形态仅缺值继承、个体初始化直接字段复制及后续变化末端夹限已新读。256夹具在成功创建返回前没有255上限；255/省略70/0分别保留。此新例排除创建复检与招式初始化，不误用NPC成员255门，也不扩张当前友好方法三档到任意大整数。',
'R6-D-DATA-C01':'CSV没有首值、重复字符串仍求首组、零数组过滤不清理单缺值元素、特性登记与字符串比较消费者已新读。省略/显式空/Other三个输入结果不同；安全导航只保护不存在的特性对象，不能清理内部缺值。条件蛋步回调在首次减步后查询，2→1后失败，无额外减步/夹0/孵化；只针对所列二成员队伍。'}
history={
'R6-D-LZ-001':['GIR-FD82-A006 (B01/B02 exact contributions)','GIR-FD82-A013','GIR-FD82-A018','GR3-M01-001','GR3-M01-002','GR4-M01-001','GR4-M01-002','GR5-M01-002','GR5-M01-003','GR5-M01-008','GR5-M01-009'],
'R6-D-LZ-002':['GIR-FD82-C061','GIR-FD82-C114','GR4-M01-002','GR5-M01-003','GR5-M10-011'],
'R6-D-PBS-C05':['GR5-M01-013','GR5-M01-016','GR5-M05-006','GR5-M12-101'],
'R6-D-PBS-C06':['GIR-FD82-C016','GR5-M01-017 (adjacent form export; not metrics field inheritance)'],
'R6-D-PBS-C07':['GIR-FD82-A021','GIR-FD82-A022','GR5-M01-006','GR5-M04-002','CI-01–CI-28','GR-35–GR-42'],
'R6-D-DATA-C01':['GIR-FD82-A001','GR3-M01-003','GR5-M01-012','GR5-M01-016/C01F-016-01']}
rows=[]
for s in C['scope_contracts']:
    fid=s['id'];paths=s['minimum_revision_contract']['candidate_formal_write_set']
    actual=[x for x in manifest['files'] if x['formal_path'] in paths]
    found=[]
    for x in actual:
        text=(ROOT/x['candidate_path']).read_text().splitlines()
        for v in vectors[fid]:
            hits=[i for i,l in enumerate(text,1) if l.startswith('| '+v+' |')]
            found.extend(dict(id=v,path=x['candidate_path'],line=i,status='DERIVED_VECTOR/NOT_EXECUTED_THIS_UPDATE') for i in hits)
    assert sorted(x['id'] for x in found)==sorted(vectors[fid]),fid
    source=s['bidirectional_evidence']['source']
    normal=s['premises_and_counterexample']
    rows.append(dict(id=fid,
      identity_and_verdict=dict(frozen=C['frozen_main'],reference=C['frozen_reference'],contract_id=fid,original_root_classification=s['identity_and_verdict']['classification'],severity=s['identity_and_verdict']['severity'],aggregation_aliases=s['aggregation_aliases'],author_state='REVISED_PENDING_NONAUTHOR_REVIEW',formal_accepted=False,CLOSED=False),
      bidirectional_evidence=dict(source=source,formal_before=s['bidirectional_evidence']['formal'],candidate_actual_bytes=actual,original_full_proposal_locator='contracts/R6-U14.json#/scope_contracts/'+str(C['scope_contracts'].index(s))+'/original_full_proposal',non_proposer=s['independent_adjudication']['non_proposer_records'],author_source_reasoning=reason[fid],traceability='input-snapshot.json + reading-receipts.jsonl + packet-validation.json; fixed identities, no source fragments copied into mirror'),
      premises_and_counterexample=normal,
      minimum_revision_contract=dict(original_rule=s['minimum_revision_contract']['rule'],preserved_scope=s['minimum_revision_contract']['preserve_correct_scope'],actual_changed_files=actual,document_operations='edit-receipt.json 29 exact edits + refinement-receipt.json 8 clarification edits',bounded_author_result=reason[fid]),
      acceptance_and_regression=dict(original_conditions=s['acceptance_and_regression']['conditions_and_vectors'],actual_vector_rows=found,author_result='SOURCE_STATIC_DERIVATION_DOCUMENTED; TOOL_CHECKS_COMPLETE; no reviewer PASS',tool_validation='author-tool-validation.json',historical_controls=history[fid],historical_qualification_material=['historical-qualified-spans.json','historical-case-premises.json'],manual_regression='Original14 baseline files fully read; specified original qualifications, criteria and case premises newly read; each new clause compared with unchanged relevant clauses/source branches. Old catalog rows byte-identical; h=0–255 normal method values unchanged. No old verdict transferred.',reference_execution='NOT_EXECUTED',independent_behavior_model='NOT_EXECUTED',host='NOT_EXECUTED',real_save='NOT_EXECUTED'),
      independent_adjudication=dict(frozen_root=s['independent_adjudication'],new_nonauthor_review='PENDING_PARENT_ASSIGNED_ULTRA_DEFAULT_REVIEWER',author_self_review_signed=False),
      dependencies_and_receivers=s['dependencies_and_receivers']))
out=dict(schema='r6.u14.author-handoff.v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),author='R6-U14-A',provenance=dict(source_thread_id='01a10d94-84b9-759e-aa1d-edb0d9b6d0e2',requested_model='gpt-6.1-sol',requested_effort='xhigh',requested_tier='default',requested_speed='普速',requested_fast=False,effective_echo='UNVERIFIED',actual_task_UUID='UNVERIFIED',CLI_or_extra_agent_probe=False,historical_not_started_fields_immutable=True),prepare=manifest['prepare'],branch='codex/remediation-sixth-r6-u14-author-20261014',per_id=rows,execution=dict(reference_functions=0,independent_gameplay_model=0,host=0,Demo=0,real_save=0,media=0,new_static_catalog_rows=27,vector_count_boundary='27 named rows; CI/GR contain four overlapping creation observations, not27unique gameplay executions'),review_and_integration=dict(candidate_non_author='PENDING',integration_writer='R6-I',actual_integration='NOT_PERFORMED_BY_AUTHOR',shared_full_file_review='PENDING_AFTER_RECEIPT',formal_acceptance='NOT_GRANTED',CLOSED='NOT_REGISTERED'),historical_boundaries='R1 originalWP only; R2 229/21/341; R3 23/76 and optionalM09/U08-notstarted/M02-no-required; R4 current17/76 versus B5 16/75; R5 exact92CLOSED/0OPEN51P2/41P3 retained, optional7/no-required7/policy6/limits13 separate; native410/schema568/extra158/shared21/deps18/solewriter85 remain separate. R6 policies7/limits14 and Float facet unchanged.',author_blockers=[],remaining_gates=['Parent-appointed nonauthor candidate review at published SHA','R6-I unique integration including shared intersections with U01/U09/U10/U12','New integrated full-file/source/interface review and exact affected history acceptance','Formal acceptance and later CLOSED registration'],limits=['No new Marshal decode/loader execution; whole binary identity and bounded member checks only','18 designated text files completely displayed/read; this is not all18catalog-domain translation quality or global semantic closure','Two additional consumer files read only the required message-processing/egg-callback ranges; four resource helper files fully read','Original image matrix48 and three diagnostic anchors read; other unassigned UI call chains not new author acceptance','Some early tool/read attempts have only platform stdout and no separately captured UTC/stderr/process metadata; no backfill','Requested model/effort/speed effective echo unverified; no repeated probe or extra agents'])
(OUT/'per-id-author-handoff.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
requests=dict(writer='R6-I only',actual_public_mutation_by_author=False,formal_file_receivers=json.loads((OUT/'packet-validation.json').read_text())['handoff']['handoff/file-conflict-graph.json']['selected_original_records']['file_receivers'],administrative_sync_requests=[])
for s in C['scope_contracts']:
    requests['administrative_sync_requests'].append(dict(id=s['id'],original_request=s['minimum_revision_contract'].get('synchronization_original_contract'),candidate_files=s['minimum_revision_contract']['candidate_formal_write_set'],action='After independent candidate and integrated acceptance, resolve actual audit/source-traceability and planning relevant rows. No author edits to public records.',new_source_trace='Fixed source/path/ranges and generated key anchors in per-id-author-handoff.json + input-snapshot.json + reading-receipts.jsonl + newline-byte-validation.json'))
(OUT/'integration-request.json').write_text(json.dumps(requests,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(handoff_ids=len(rows),vector_rows=sum(len(x['acceptance_and_regression']['actual_vector_rows']) for x in rows),status='READY_FOR_INDEPENDENT_REVIEW; no acceptance or CLOSED')))
