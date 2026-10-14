import datetime, hashlib, json, pathlib
OUT=pathlib.Path(__file__).resolve().parent
PREFIX='review/remediation-sixth-20261014-prepare/'
final=json.loads((OUT/'final-validation.json').read_text())
prior=json.loads((OUT/'fixed-validation.json').read_text())
GROUP_KEYS=['identity_and_verdict','bidirectional_evidence','premises_and_counterexample',
            'minimum_revision_contract','acceptance_and_regression','independent_adjudication','dependencies_and_receivers']
peers=[('R6-U10','u10','peer-review.json','per_ID_results','seven_groups'),
       ('R6-U11','u11','peer-review.json','per_id','groups'),
       ('R6-U12','u12','report.json','per_id','seven_groups')]
unique_facts={
'R6-UI-001':('送盒暂停内A已盒存/已从party删除，记忆与N接收未到；正常消息返回才移记忆/收N。','CP01–09，含两层BACK、sendToBoxes2、送N盒与两个消息异常和更早双满失败。','WP38接收、默认Peer/Storage currentBox、WP67-A；最终U13录制空存储操作与普通捕获域分列。'),
'R6-UI-002':('Safari party_full AND boxes_full才拒绝；party1/全盒满放行，party6/全盒满拒绝。','SF01–05，三容量态、扣球/刷新/投掷请求、Run/末球及失败前缀；放行不等于捕获成功。','最终WP53全文与domain286新读，SF30及SF36–40共享保存不改变容量门/模式接收；专用Save隐藏不同于普通Quit。'),
'R6-UI-PARTY-001':('构造markings=[]，显示0不补齐；Summary缺槽ACTION失败、未提交；Storage直接Mark无ACTION清零。','MK01–09，显式六零、缺槽、局部编辑、BACK/ACTION及USE/ACTION优先、OK/Cancel及Storage对照。','WP18/U14邻接初值、Party/Storage Summary委托、WP66-A；最终设施多选另由具名联合接口审覆盖，非统一回滚。'),
'R6-UI-PARTY-002':('只有未会且不在等级候选的initial记录前置；重叠GROWL仍保等级位置。','RL01–09，空/重叠/独有/重复诊断/已会/混合/配置关；取消、教学结果、统计次序及B16/HM控制。','WP30/U14、MoveRelearner列表窗口、WP66-A；新设施规则不改重学/配置/教学入口。'),
'UI-ST-001':('Storage末按钮6的UP→5、DOWN→0与成员±2分列；mode0整理与mode2存入消费者区别。','R6-BX01–04，左右/普通成员/模式消费者；暂持/交换/已提交写入及旧导航保持。','最终WP66-B/UI两blob不变且必要接点明确复核；domain新全文和保存接口并置不变按钮域。'),
'UI-ST-003':('Forms已生成序列首尾trigger回绕，下一轮开头先写last再刷新/处理新输入；单项不开放。','R6-DX01–04/R6-PD01–03，false首写、多项/单项、BACK分层、媒体失败只保前缀及旧结构/性别/标签控制。','WP62 U01登记与U09磁盘/同会话缓存接合；最终domain新blob13eb3ec4...全文，PD/R4-PD/R6-PD原块保持；最终WP53保存不自动恢复last。'),
'UI-ST-005':('Storage先方向覆盖UP>LEFT>RIGHT>DOWN，后动作互斥；切盒正常后段/Input刷新才完成当前盒写入。','R6-BX05–11，方向+USE、JUMP+BACK、模式ACTION、SPECIAL消费、暂持与标记BACK/USE、刷新后新查询。','图鉴主/子页及Summary/普通命令独立优先级，当前盒保存与捕获消费者保持；最终共享保存前缀不作浏览回滚。'),
'GR6-UI-BAG-001':('BP nil默认两介绍、普通自定义一条替换；同stock首问候前过滤，正常共同两告别/清覆盖。','BP01–04，省略/自定、同列表过滤、首问候/购买异常不保证尾部；价格/资源/退款统计旧控制保留。','WP29/WP66-C/WP17、GameTemp与请求消费，最终四U12blob同9d但已明确核新8路径无相关行为覆盖。'),
'GR6-UI-BAG-002':('Bag成功提示入口仍5，正常返回删1三次到2再刷新；PC整批checked删3/刷新后提示已2。','TS01–05，正常同终态、提示异常不同前缀、qty0/No/重要守卫、三行真实LF+最终两行busy未知宿主。','WP27/U14名称配置、WP66-C、共享消息/AdvancedText更新/partial容器；最终活动保存不回滚库存阶段，局部消息恢复门不统一。')}
records=[]
for batch,u,file,ids_key,groups_key in peers:
    peer_path=OUT/'peers'/u/file
    peer=json.loads(peer_path.read_text())
    b=next(b for b in final['batches'] if b['batch']==batch)
    for idx,item in enumerate(peer[ids_key]):
        groups=item[groups_key];assert list(groups)==GROUP_KEYS
        i=item['id'];fact,controls,dependency=unique_facts[i]
        contract_root=PREFIX+'contracts/'+batch+'.json'
        seven={}
        for key in GROUP_KEYS:
            judgment={
              'identity_and_verdict': 'Final ACTUAL_PASS_SCOPED_STATIC, required/'+item['severity']+'; canonical/primary/aliases unchanged; generated old pending is historical.',
              'bidirectional_evidence': fact+' 固定源R不变，真实actual路径与逐文件三指纹在final-validation绑定，详尽双向位置见旧peer和final-increment。',
              'premises_and_counterexample': controls+' 仅合法具名初态、资源/消息等正常依赖与排除插件/外部改写；异常保实际前缀，不保证外层恢复。',
              'minimum_revision_contract': '原合同最小规则、正确正常控制、源行为范围和历史隔离保持，最终相关候选新增/替换块完整存在，必要正文再修订0。',
              'acceptance_and_regression': controls+' 已就最终未变blob/新全文/接口重新作明确裁决；历史R1–R5精确scope按各peer限定，不将旧整轮PASS或计数迁签。',
              'independent_adjudication': '非作者团队直接/反向复核原提案、原证据、原反证，根汇合新实际全文与final-increment；SOURCE_STATIC/DERIVED_VECTOR，源码/模型/宿主运行0，配置UNVERIFIED。',
              'dependencies_and_receivers': dependency+' 本组D仍9项，F002接收接口另列不加分母；正式/行政/CLOSED独立，未来变blob或接口须增量复审。'
            }[key]
            seven[key]={'root_final_result':'PASS_SCOPED_STATIC','contract_path':contract_root,
                        'contract_pointer':f'/scope_contracts/{idx}/{key}','contract_identity':b['contract_identity'],
                        'prior_actual_evidence':{'path':str(peer_path.relative_to(OUT)),
                         'pointer':f'/{ids_key}/{idx}/{groups_key}/{key}','frozen_actual_commit':prior['actual_commit'],
                         'role':'Exact prior evidence, not automatic transfer of verdict'},
                        'final_increment_report':f'peers/{u}/final-increment/report.md','root_final_adjudication':judgment}
        records.append({'id':i,'classification':'required','severity':item['severity'],'primary_batch':batch,
                        'actual_commit':final['actual_commit'],'actual_verdict':'ACTUAL_PASS_SCOPED_STATIC',
                        'required_repairs':0,'seven_groups':seven})
assert [r['id'] for r in records]==final['group_ids']
result={'schema':'r6.actual.group-d.final-per-id.v1','recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'actual_commit':final['actual_commit'],'workspace_tree':final['workspace_tree'],'formal_tree':final['formal_tree'],
        'scope_ids':final['group_ids'],'per_id':records,'required_repairs':0,
        'separate_receiver_interface':'joint-interface-review.json','entire56_INTEGRATED_PASS':None,
        'formal_acceptance':None,'CLOSED':False,'effective_configuration':'UNVERIFIED','behavior_execution':0}
(OUT/'per-id-review.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
mapping=[]
owner={
'wp18':'/root/storage_review','wp30':'/root/storage_review','wp66-a':'/root/storage_review','wp67-a':'/root/storage_review',
'wp62':'/root/pokedex_review','wp66-b':'/root/pokedex_review','pokemon-rules-wp53':'/root/pokedex_review',
'wp27':'/root/evidence_audit','wp29':'/root/evidence_audit','wp66-c':'/root/evidence_audit',
'wp54':'/root/storage_review','wp55':'/root/storage_review','wp53':'/root/pokedex_review',
'combat-requirements-wp54':'/root/storage_review'}
for f in final['files']:
    name=pathlib.Path(f['path']).name
    if name.startswith('user-interface-wp17'):
        credit={'mode':'New full team reading at9d and exact final unchanged-byte/interface supplement',
                'team_ranges':[{'reader':'/root/evidence_audit','lines':[1,243]},
                               {'reader':'/root/storage_review','lines':[244,358]},
                               {'reader':'/root','lines':[359,565]},
                               {'reader':'/root/storage_review','lines':[566,938]},
                               {'reader':'/root','lines':[939,1026]}],
                'root_personal_full':False,'physical_lines':1026,'coverage':'No gaps; overlaps additionally in peer relevant spans'}
    else:
        key=next(k for k in owner if name.startswith(k))
        new_final=not f['unchanged_from_9d'] or name.startswith(('wp66-a','wp54','wp55'))
        credit={'reader':owner[key],'range':[1,f['physical_lines']],
                'mode':'Final full newly read' if new_final else 'Prior9d full newly read, exact unchanged final bytes and explicit interface supplement',
                'root_personal_full':False}
    mapping.append({'path':f['path'],'final_identity':f['actual'],'prior_identity':f['prior'],
                    'unchanged_from_9d':f['unchanged_from_9d'],'semantic_credit':credit})
readmap={'schema':'r6.actual.group-d.final-semantic-readmap.v1','actual_commit':final['actual_commit'],'files':mapping,
         'root_fresh_reference_and_doc_reads':'reading-ledger.jsonl; selected F002 complete scope joint-contract-read-receipt.json',
         'root_peer_reports_read':'Old U10/U12 complete MD, U11 omitted middle re-read27–65 after combined output truncation; final incremental MD all read before freeze.',
         'full_input_qualification':'Old2661 whole semantic read plus every final changed/new record structurally read and reconstructed exactly; no claim of new3243 line-by-line read.',
         'previous_source_reads':'Precise same-reader/fixed-identity prior receipts identified in each peer; no automatic fresh full-source credit.',
         'timestamps':'Per-read UTC where captured in ledgers; inventory timestamp is not substituted for uncaptured semantic read time.',
         'old_u11_UI_reader_correction':'Old peer claim root personal fullUI corrected by final-increment to team ranges; no old report rewritten.',
         'behavior_execution':0}
(OUT/'semantic-readmap.json').write_text(json.dumps(readmap,ensure_ascii=False,indent=2)+'\n')
limits={'schema':'r6.actual.group-d.execution-limits.v1','requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'default'},
        'effective_configuration':'UNVERIFIED','configuration_cli_probe':False,
        'counts':{'reference_execution':0,'author_scripts':0,'independent_behavior_model':0,'host_Demo':0,'real_save_load':0,'Mac':0},
        'allowed_tool_execution':'Own Git/UTF8/JSON/hash/table/diff document validation only',
        'actual_final_content_scope':final['group_ids'],'additional_interface_scope':'GR6-F-002 WP66-A/WP54/QC/WS receiver; not full U13 adjudication',
        'excluded':'Other47 required items; full host/native media/input; unbounded plugin/config; future edited blobs/interfaces; administrative/public sync; formal acceptance/CLOSED',
        'old_failures':'Preserved attempts, old U13 FAIL and historical nonpassing/advisory states; recovered objects/new successful reads separately recorded',
        'only_write_directory':PREFIX+'actual-reviews/group-D/','no_force_merge_main_delete':True}
(OUT/'execution-limits.json').write_text(json.dumps(limits,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'ids':len(records),'semantic_files':len(mapping),'scope':'9 plus explicit F002 receiver interface','actual':final['actual_commit']}))
