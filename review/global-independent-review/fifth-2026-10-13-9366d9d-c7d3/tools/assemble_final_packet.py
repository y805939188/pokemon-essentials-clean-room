#!/usr/bin/env python3
"""Review artifact assembly. Source/reference/formal trees are only read."""
import assemble_review as a
import json,copy,re,collections,hashlib,argparse
O=a.O;W=a.W
FIELDS=('purpose','caller_override','preconditions','configuration_host','dependencies','unknowns','reviewed_scope','status_reason')
def canonical_target(fid,byid):
 f=byid.get(fid)
 if not f:return fid
 dup=f.get('duplicate_of')
 if dup:return dup
 # These no-required rows are explicit duplicate projections, not corrected formal text.
 return {'GR5-M01-019':'GR5-M05-006','GR5-M01-020':'GR5-JXN-001','GR5-M05-005':'GR5-M12-101','GR5-M04-003':'GR5-M08-001'}.get(fid,fid)
def gates():
 assert a.read('modules/C01F/progress.json')['complete'] is True
 assert a.read('modules/ASM/progress.json')['complete'] is True
 assert a.read('modules/ASM/field-gaps.json')['count']==0,'finite matrix fields still open'
 assert a.read('modules/JXN/progress.json')['complete'] is True
 assert a.read('modules/JXN/shared-contracts.json')['complete'] is True
 assert a.read('modules/C00/C01F-final-reception.json')['complete'] is True
 assert a.read('modules/C00/ASM-final-reception.json')['complete'] is True
 assert a.read('modules/C00/JXN-final-reception.json')['complete'] is True
 for x in a.read('modules/C00/JXN-final-reception.json')['input_identities']:
  assert (O/x['path']).stat().st_size==x['bytes'] and a.sha(O/x['path'])==x['sha256'],('JXN changed after actual root reception',x['path'])

def coverages(fs):
 byid={f['id']:f for f in fs};rows=[]
 for sh in a.read('modules/ASM/matrix-draft.json')['scope_shards']:rows+=a.read(sh['path'])['rows']
 assert len(rows)==1460
 m01={r['capability_id']:(n,r)for n,r in enumerate(a.read('modules/M01/followup-partial-dispositions.json')['records'])}
 m02={r['id']:(n,r)for n,r in enumerate(a.read('modules/M02/followup-partial-dispositions.json')['records'])}
 overlays={(r['module'],r['local_capability_id']):r for r in a.read('coverage-adjudications.json')['rows']}
 alias=a.read('modules/C00/shared-finding-routing-draft.json')['rows'];fcontracts=collections.defaultdict(set)
 for r in alias:fcontracts[r['finding_id']].add(r['canonical_contract_id'])
 shared_index=a.read('shared-contracts.json');shared_aliases=collections.defaultdict(set)
 for c in shared_index['contracts']:
  for name in [c['id']]+c.get('aliases',[]):
   if isinstance(name,str):shared_aliases[name].add(c['id'])
 for route in shared_index['domain_interface_join']:
  shared_aliases[route['domain_interface_id']].add(route['canonical_id'])
 for route in shared_index.get('resource_interface_join',[]):
  shared_aliases[route['domain_interface_id']].add(route['canonical_id'])
  shared_aliases[route['domain_interface_id']].update(route.get('consumer_projection_ids',[]))
 for r in rows:
  key=(r['module'],r['local_id']);r['primary_snapshot_status']=r['status'];r['root_integrator']='root'
  linked=set(re.findall(r'GR5-[A-Z0-9]+-\d{3}',json.dumps(r.get('findings',[]))))
  for f in fs:
   if r['local_id'] in f.get('related_capabilities',[]):linked.add(f['id'])
  if key in overlays:
   q=overlays[key];linked.update(q['canonical_finding_ids']);r['root_qualified_disposition']=q
   if q['final_bounded_disposition'].startswith('partial'):r['status']='partial'
   elif q['final_bounded_disposition'].startswith('supported'):r['status']='supported'
  if r['module']=='M01' and r['local_id']in m01:
   n,q=m01[r['local_id']];linked.update(q['existing_finding_ids']+q['new_finding_ids'])
   r['finite_subscope_disposition']={'ref':a.input_ref('modules/M01/followup-partial-dispositions.json',f'/records/{n}'),'subscopes':copy.deepcopy(q['subscope_dispositions']),'reason':q['status_reason'],'reading_complete':True,'independent_resolution':'所有候选已由root定稿裁决；本字段原候选用词是提出时点，当前以canonical_finding_links为准。'}
   r['specification_anchors']['finite_effective_anchors']=q['effective_spec_anchors']
   hasreq=any(byid[canonical_target(x,byid)]['disposition']=='required'for x in linked if canonical_target(x,byid)in byid)
   r['status']='partial' if hasreq else 'supported'
  if r['module']=='M02' and r['local_id']in m02:
   n,q=m02[r['local_id']];r['finite_subscope_disposition']={'ref':a.input_ref('modules/M02/followup-partial-dispositions.json',f'/records/{n}'),'subscopes':q['subranges'],'fact_review_complete':q['complete'],'policy_does_not_mean_unread':True}
   for s in q['subranges']:
    if isinstance(s.get('final_finding'),str):linked.add(s['final_finding'])
   linked.update(x if isinstance(x,str)else x.get('id','')for x in q.get('new_findings',[]))
   if any(byid.get(x,{}).get('disposition')=='required'for x in linked):r['status']='partial'
   elif any(s['status']=='unresolved_policy'for s in q['subranges']):r['status']='unresolved'
   else:r['status']='supported'
  if r['module']=='M10' and r['local_id']=='M10-C-DEX-SHARED':
   r['status']='supported';r['root_qualified_disposition']={'reason':'M10外域原签名not_reviewed不转成全局未读；图鉴的主审由M11全量来源/正文/条件和JXN消费链承接。','primary_module':'M11','refs':[a.input_ref('modules/M11/source-to-spec.json'),a.input_ref('modules/C00/REG-final-reception.json')],'scope':'仅此责任投影；具体图鉴问题仍由M11各行和规范发现记录，不签整个图鉴无缺陷。'}
  linked={x for x in linked if x in byid}
  r['canonical_finding_links']=[{'reported_id':x,'canonical_id':canonical_target(x,byid),'disposition':byid[canonical_target(x,byid)]['disposition'],'severity':byid[canonical_target(x,byid)]['severity'],'canonical_ref':{'path':'findings.json','finding_id':canonical_target(x,byid)}}for x in sorted(linked)]
  if any(x['disposition']=='required'for x in r['canonical_finding_links']) and r['status']=='supported':
   r['status']='partial';r['root_status_reason']='领域已审；本行范围含已独立确认的有限缺口，按具体规范发现前提收窄，未修订B5。'
  exact_labels=[r['local_id']]+[x for x in r['ownership_and_alias'].get('shared_aliases',[])if isinstance(x,str)]
  r['shared_contract_links']=sorted({p for x in linked for p in fcontracts[x]}|{p for x in exact_labels for p in shared_aliases[x]})
  r['shared_link_basis']='exact domain capability/alias identity or qualified canonical finding projection; same file alone never transfers a shared contract'
  r['ownership_and_alias']['JXN_join_state']='current_global_shared_contracts_received';r['pending_final_delta']=[]
  r['semantic_reading_completion']='complete_within_recorded_finite_scope_and_explicit_material_dispositions'
  r['capability_id']=r['scope_id'];r['local_capability_id']=r['local_id']
  r['reviewer']=r['reviewer_and_evidence']['primary']
  absent=[s['path']for s in r['source_anchors']if s.get('material_availability')=='missing_material']
  r['material_availability']={'state':'missing_named_materials'if absent else 'available_fixed_source_for_named_static_scope','missing':absent,'runtime_or_native_selection':'not established by availability; see configuration_host and unknowns'}
  r['review_extent']={'scope':'completed named finite audit scope or evidence-backed material disposition','actual_range_record':'actual_reviewed_scope','field_evidence':'reviewed_scope','whole_file_or_native_behavior_not_inferred':True}
  r['evidence_level']=['TOOL_VALIDATION','SPEC_STATIC']if absent else ['SOURCE_STATIC','SPEC_STATIC']
  r['support_evidence_status']='supported_static'if r['status']=='supported'else r['status']+'_static_disposition'
  r['global_product_feature_count_credit']=False
  for fld in FIELDS:assert fld in r,(r['scope_id'],fld)
  assert not r.get('missing_field_dispositions'),(r['scope_id'],'field gap')
 projection=a.read('modules/ASM/projection-draft.json')
 a.write('source-to-spec-coverage.json',{'schema_version':'gr5.root-source-to-spec.v2','complete':True,'source_baseline':a.RC,'specification_baseline':a.B5,'meaning':'全量已发现有限审计范围和条件化投影的当前去向；status说明B5支持程度，不是阅读状态或运行PASS。','audit_scope_count':len(rows),'unique_product_feature_count':None,'count_warning':'1460审计scope可交叠，1295投影不另计产品能力；同源不同条件也不机械合并。','rows':rows,'finding_scope_overlays':[{'id':f['id'],'record_kind':'canonical_rule_overlay_not_additional_product_feature','status':('partial' if byid[canonical_target(f['id'],byid)]['disposition']in ['required','optional'] else 'unresolved' if f['disposition']=='unresolved' else 'supported'),'disposition':f['disposition'],'source_anchors':f['source_anchors'],'spec_anchors':f['spec_anchors'],'purpose':f['title'],'preconditions':f['preconditions'],'reference_facts':f['expected_reference_behavior'],'current_spec_facts':f['current_spec_behavior'],'status_reason':f['gap'],'reading_completion':'targeted primary plus completed nonproposer/root adjudication','review_resolution_ref':{'path':'findings.json','finding_id':f['id'],'field':'review_resolution'},'related_scope_labels':f.get('related_capabilities',[]),'unknowns':f['unknowns'],'execution_status':f['execution_status']}for f in fs],'projection_index':a.input_ref('modules/ASM/projection-draft.json'),'projection_count':projection['count'],'field_value_store':a.input_ref('modules/ASM/evidence-fields.json'),'field_completion':a.input_ref('modules/ASM/field-completion.json'),'normalization_corrections':[a.input_ref('normalization-corrections.json'),a.input_ref('modules/C00/BIN-projection-join.json')],'final_canonical_authority':'findings.json；primary冻结候选/旧pending用语不覆盖定稿裁决。','shared_primary_identity_index':'shared-contracts.json','status_counts':dict(collections.Counter(r['status']for r in rows))})
 inv=a.read('modules/ASM/inverse-index.json')
 inv.update(schema_version='gr5.root-spec-to-source.v2',complete=True,specification_baseline=a.B5,source_baseline=a.RC,field_value_store=a.input_ref('modules/ASM/evidence-fields.json'),reference_base='review_root',main_capability_index='source-to-spec-coverage.json',canonical_findings_index='findings.json',semantic_records_index=a.input_ref('modules/ASM/semantic-index.json'),late_source_and_clause_corrections=[a.input_ref('normalization-corrections.json'),a.input_ref('modules/C00/M01-followup-reception.json'),a.input_ref('modules/C00/C01F-final-reception.json')],M05_pointer_relocations=a.input_ref('modules/ASM/M05-pointer-relocations.json'))
 inv['canonical_clause_overlays']=[{'finding_id':f['id'],'disposition':f['disposition'],'source_anchors':f['source_anchors'],'spec_anchors':f['spec_anchors'],'comparison':f['gap'],'reference_facts':f['expected_reference_behavior'],'independent_resolution_ref':{'path':'findings.json','finding_id':f['id'],'field':'review_resolution'}}for f in fs]
 scope_shared={r['scope_id']:r['shared_contract_links']for r in rows}
 for unit in inv['units']:
  unit['related_shared_contracts']=sorted({c for sid in unit['canonical_root_ids']for c in scope_shared.get(sid,[])})
 inv['shared_contract_index']='shared-contracts.json: exact primary/consumer projections; empty local links do not negate separately recorded interface joins'
 inv['root_additional_premise_units']=a.read('modules/C00/residual-premise-join.json')['records']
 inv['count_semantics']='25704原逆向审计单位身份保留；新增13段前提及规范裁决覆盖层单列，不把单位数当独立功能数。'
 a.write('spec-to-source-coverage.json',inv)
 files=a.read('modules/ASM/file-dispositions.json');prem=a.read('modules/C00/residual-premise-join.json')['records'];pmap=collections.defaultdict(list)
 for q in prem:pmap[q['path']].append(q)
 for f in files['files']:
  if f['path']in pmap:
   f['root_premise_completion']=pmap[f['path']];covered={n for q in pmap[f['path']]for n in range(q['lines'][0],q['lines'][1]+1)}
   left=[n for x,y in f['remaining_semantic_or_context_ranges']for n in range(x,y+1)if n not in covered];assert not left,(f['path'],left)
   f['remaining_semantic_or_context_ranges']=[];f['remaining_is_available_material_not_missing_host']=False
   if f['disposition']=='available_text_has_precise_remaining_semantic_or_context_ranges':f['disposition']='semantic_ranges_joined_with_root_premise_closure'
  f['authority']='root accepted finite domain semantic scopes plus precise reception overlays'
 assert not any(f['remaining_semantic_or_context_ranges']for f in files['files'])
 files.update(schema_version='gr5.root-reading-coverage.v2',complete=True,available_readable_semantic_ranges_pending=[],native_or_host_unknowns='limits-and-missing-materials.md',status='FULL_FINITE_STATIC_COMPARISON_WITH_NAMED_LIMITS',meaning='完成的是可得且可审有限材料的具名语义及处置；full不外推机器码全控制流/未编码字形/原生渲染/完整Demo。',primary_semantic_index=a.input_ref('modules/ASM/semantic-index.json'),source_matrix='source-to-spec-coverage.json',inverse_matrix='spec-to-source-coverage.json',new_behavior_execution='See execution-evidence.json only; this merge is TOOL_VALIDATION, not execution.')
 files['current_disposition_counts']=dict(collections.Counter(f['disposition']for f in files['files']));a.write('inventory-and-reading-coverage.json',files)
 corpus=a.read('corpus-inventory.json');index={(f['version'],f['path']):(n,f)for n,f in enumerate(files['files'])}
 for family in ('references','specification_repository'):
  for x in corpus[family]:
   key=(x.get('baseline'),x['path'])
   if key in index:
    n,f=index[key];x.setdefault('initial_inventory_review_extent',x.get('review_extent'));x['review_extent']='complete_named_semantic_disposition';x['semantic_disposition']=f['disposition'];x['reading_coverage_ref']={'path':'inventory-and-reading-coverage.json','pointer':f'/files/{n}'};x['remaining_available_semantic_scope']=[]
   elif family=='specification_repository':
    x.setdefault('initial_inventory_review_extent',x.get('review_extent'));x['review_extent']='classified_not_current_independent_behavior_contract';x['semantic_completion_boundary']=x.get('disposition_reason',x.get('classification_basis','modules/C00/supplemental-scope.json'))
 corpus['warning']='完整盘点及当前/历史分类已完成；语义完成依具名阅读账，历史行政身份不自动转为本轮行为支持。'
 corpus['final_semantic_disposition']={'complete':True,'reading_index':'inventory-and-reading-coverage.json','all_current_formal_count':131,'reference_files':432,'original_files':113,'supplement_and_context_files':47,'effective_attachment_join':a.input_ref('modules/C00/effective-attachment-join.json'),'historical_files_preserved':True,'native_execution_or_whole_machine_code_not_claimed':True}
 corpus['classification_summary']['current_counts']=dict(collections.Counter(x.get('currentness','none')for x in corpus['specification_repository']));a.write('corpus-inventory.json',corpus)
 return rows,files

def shared_contracts(fs):
 j=a.read('modules/JXN/shared-contracts.json');chain=a.read('modules/JXN/junction-review.json');routing=a.read('modules/C00/shared-finding-routing-draft.json')
 assert not routing['unresolved_labels'];d=copy.deepcopy(j);d['schema_version']='gr5.root-shared-contracts.v2';d['complete']=True;d['canonical_input']=a.input_ref('modules/JXN/shared-contracts.json')
 special={'CREATURE-PLANT-PERSISTENCE':'M03','CREATURE-ATTRIBUTE-DERIVATION':'M04','KERNEL-EXTERNAL-LOADER':'M12','HOST-READABLE-MATH':'BIN','DEMO-EVIDENCE-BOUNDARY':'M12','SHARED-SAVE-NAVIGATION':'M10'}
 for c in d['contracts']:
  c['original_primary_owner_statement']=c['primary_owner'];m=re.search(r'M\d{2}(?:B)?',c['primary_owner']);c['primary_review_owner']=special.get(c['id'],m.group()if m else 'BIN'if 'BIN'in c['primary_owner']else None);assert c['primary_review_owner'],c['id']
  c['ownership_boundary']='此为主合同的唯一审计归属；各条件化消费投影仍保留，不规定未来模块/接口/继承结构。'
  c['finding_scope_projections']=[r for r in routing['rows']if r['canonical_contract_id']==c['id']]
  c['canonical_findings']=sorted({r['finding_id']for r in c['finding_scope_projections']})
  if any(f['id']in c['canonical_findings']and f['disposition']=='required'for f in fs):
   c['root_support_disposition']='partial: finite required gaps only; existing supported clauses remain'
  else:c['root_support_disposition']='see independent named JXN comparison and material boundary'
 if not any(c['id']=='AUTHOR-CONVERSION-OUTPUT'for c in d['contracts']):
  ff=[f for f in fs if f['id']in ['GR5-M12-002','GR5-M12-003','GR5-M12-004','GR5-M12-005','GR5-M12-006','GR5-M12-007']]
  d['contracts'].append({'id':'AUTHOR-CONVERSION-OUTPUT','primary_review_owner':'M12','primary_owner':'root/M12 primary, M12B independent counterevidence','producer':'作者已有地图/公共事件/旧注记/文件名；各输入资格依具名转换条款。','write':'事件命令与条件转换先形成结果；匹配门、布尔累积、音效/朝向/等待/色调输出及单图/全批保存顺序逐项在M12规范发现及现行WP75分开。','consumer':'事件解释器、战斗启动、地图转移、生成文件再读取；脚本装载器独立归KERNEL-EXTERNAL-LOADER。','display':'仅静态生成的显示/音乐/过渡请求参数；无媒体/宿主像素证明。','persistence':'内存事件更改与按转换入口写档不同；已有CommonEvent排除/训练家空分支插入及未回滚前缀按既有合同保持。','changes':'不同转换规则不同根因：单行匹配边界、生成门/门参数、布尔true锁存、文件名替换；不合并为通用字段CSV转换。','chains':['JXN-C13'],'status':'partial','review_extent':'full_named_conversion_source_scope_and_targeted_counterevidence','source_anchors':[s for f in ff for s in f['source_anchors']],'spec_anchors':[s for f in ff for s in f['spec_anchors']],'normal_failure_boundary_cases':[{'finding_id':f['id'],'normal':f['normal_case'],'counterexample':f['minimal_counterexample'],'failure':f['failure_or_boundary_case'],'exclusions':f['excluded_claims']}for f in ff],'canonical_findings':[f['id']for f in ff],'finding_scope_projections':[r for r in routing['rows']if r['canonical_contract_id']=='AUTHOR-CONVERSION-OUTPUT'],'evidence':['modules/M12/reading-coverage.json','counterevidence/root-M12/canonical-findings.json','modules/M12B/counterevidence.json'],'ownership_boundary':'独立审计主身份，非未来架构建议；事实已由既有主审和非提出者反证接收，本次仅补唯一连接。'})
 assert len({c['id']for c in d['contracts']})==len(d['contracts'])
 d['primary_identity_count']=len(d['contracts']);d['domain_route_count']=len(d['domain_interface_join']);d['finding_label_routes']=routing['rows'];d['labels_are_not_additional_features']=True;d['final_canonical_findings_authority']='findings.json';d['root_independent_reception']='modules/C00/JXN-final-reception.json'
 a.write('shared-contracts.json',d)
 if 'additional_primary_identity_needed'in routing:routing['historical_additional_primary_identity_requests']=routing.pop('additional_primary_identity_needed')
 routing.update(complete=True,pending=[],canonical_contract_count=len(d['contracts']),final_index='shared-contracts.json',all_requested_primary_identities_received=True);a.write('shared-contract-routing.json',routing)
 chain.update(schema_version='gr5.root-junction-review.v2',complete=True,canonical_input=a.input_ref('modules/JXN/junction-review.json'),unique_shared_primary_index='shared-contracts.json',root_reception='modules/C00/JXN-final-reception.json',root_additional_contract='AUTHOR-CONVERSION-OUTPUT',canonical_findings_authority='findings.json')
 a.write('junction-review.json',chain)
 txt=(O/'modules/JXN/report.md').read_text();(O/'junction-review.md').write_text('# 第五轮跨域接收\n\n'+txt+'\n\nroot已接收具名跨域事实与完整限定比较，JXN001/002有CJXN非提出者反证和root定向复读，JXN003有root非提出者直接源/规格反证。最终共享主身份共'+str(len(d['contracts']))+'项，182个领域原始交接路由保留；AUTHOR-CONVERSION-OUTPUT承接已审项目转换事实的唯一审计归属。局部标签和消费投影不算新产品功能。主身份的唯一审计owner、源/规格锚点、生产/写入/消费/显示/持久与边界见shared-contracts.json；不作为未来架构模板。\n')
 return d,chain

def decisions_and_findings(fs,shared):
 routes=collections.defaultdict(set)
 for r in shared['finding_label_routes']:routes[r['finding_id']].add(r['canonical_contract_id'])
 for f in fs:f['normalized_shared_contracts']=sorted(routes[f['id']])
 counts=dict(collections.Counter(f['disposition']for f in fs));sev=dict(collections.Counter(f['severity']for f in fs if f['disposition']=='required'))
 result={'schema_version':'gr5.canonical-findings.v2','complete':True,'source_baseline':a.read('baseline.json')['reference_baseline'],'specification_baseline':a.read('baseline.json')['formal_baseline'],'counts':{'total':len(fs),**counts,'unresolved':counts.get('unresolved',0),'required_severity':{'P1':sev.get('P1',0),'P2':sev.get('P2',0),'P3':sev.get('P3',0)},'optional_severity':dict(collections.Counter(f['severity']for f in fs if f['disposition']=='optional')),'named_policy_decisions':6},'finding_state':'B5未修订；required为下一轮有限修订输入，不是已关闭。','canonical_authority':'主汇总已完成去重与每条必修非提出者反证；模块冻结候选状态/旧严重度由本文件覆盖，不改写原报告。','findings':fs}
 a.write('findings.json',result)
 a.write('counterevidence-resolution.json',{'schema_version':'gr5.counterevidence-root.v2','complete':True,'all_required_have_nonproposer_review':True,'counts':result['counts'],'records':[{'id':f['id'],'disposition':f['disposition'],'severity':f['severity'],'root_cause_group':f['root_cause_group'],'review_resolution':f['review_resolution'],'canonical_input':f['canonical_input'],'duplicate_target':canonical_target(f['id'],{x['id']:x for x in fs})if canonical_target(f['id'],{x['id']:x for x in fs})!=f['id']else f.get('duplicate_of'),'boundary':'只确认本条明确事实、前提、输入/输出与限定修改；不签全域运行通过。'}for f in fs]})
 lines=['# 第五轮发现清单','',f"{len(fs)}条规范记录；{counts['required']}必修（P1 0、P2 {sev['P2']}、P3 {sev['P3']}），{counts['optional']}可选P3，{counts['no_required_revision']}无需另修，事实争议未决0。另6个政策选择单列，不是必修。",'','| ID | 等级 | 处置 | 主责批次 | 结论 |','| --- | --- | --- | --- | --- |']
 for f in fs:lines.append('| '+ ' | '.join([f['id'],f['severity']or'—',f['disposition'],f.get('batch_owner')or'—',f['title'].replace('|','／')])+' |')
 lines+=['','逐项源/规格锚点、全部前提/反例、独立反证、验收和历史资格保留在findings.json，并在完整handoff中展开。所有required仍为待修；本轮未更改正式规格。']
 (O/'findings-summary.md').write_text('\n'.join(lines)+'\n');return result

def plans(fs):
 p,s=a.batch_plan(fs);p['complete_plan']=True;p['authorized_findings']=[f['id']for f in fs if f['disposition']=='required'];p['not_authorized']={'optional':[f['id']for f in fs if f['disposition']=='optional'],'no_required_revision':[f['id']for f in fs if f['disposition']=='no_required_revision'],'policy_decisions':'unresolved-decisions.json','engine_implementation':False}
 admin=['deliverables/final-specification-set/README.md','deliverables/final-specification-set/scope-statement.md','deliverables/final-specification-set/test-catalog/README.md'];support=['planning/feature-matrix.md','planning/coverage.md','audit/source-traceability.md']
 u=p['batches'][-1];u['allowed_formal_files']=admin;u['direct_writer_files']=admin;u['allowed_support_files']=support;u['allowed_new_remediation_artifacts']='新建本轮独立整改目录内的候选、复审、精确字节清单和接受/依赖/回归登记；不回写旧登记。'
 u['scope_limit']='只同步本轮已实际接受限定贡献的导航、Feature Matrix、追溯与状态，保留历史时点；不能据此扩张实质整改或覆盖旧报告。'
 for path in admin+support:
  assert(W/path).exists(),path
  existing=next((r for r in s['files']if r['path']==path),None)
  if existing:
   existing['writer']='R5-I';existing['contributing_batches']=sorted(set(existing['contributing_batches']+['R5-U08']))
  else:s['files'].append({'path':path,'writer':'R5-U08','contributing_batches':['R5-U08'],'findings':[],'historical_files_writable':False,'allowed_scope':u['scope_limit']})
 p['semantic_writer_vs_integration']='批次作者对非共享候选负责；共享正式内容只由R5-I接片段写入，实际整合统一按独立批准的精确字节进行。机械应用不得自行改语义，改了须重作定向复审。'
 p['regression_obligations']={'R4':'regression-fourth-17.json（17控制/76标准）','R3':'regression-third-23.json（23控制/76标准）','R2':'regression-legacy-scope.json（229控制/341贡献）','current_findings':'findings.json全部92必修及每条原来正确的行为','shared':'shared-contracts.json及junction-review.json；每批按其受影响producer/consumer反查','acceptance_scope':'旧资格只按精确owner/scope复用；新字节必须新审，不因文件相同转签。'}
 s['complete']=True;a.write('proposed-update-batches.json',p);a.write('shared-file-owners.json',s);return p,s

def reports(result,rows,files,shared,chain,plan):
 fs=result['findings'];req=[f for f in fs if f['disposition']=='required'];groups=collections.defaultdict(collections.Counter)
 limits_path=O/'limits-and-missing-materials.md';limits_text=limits_path.read_text();limits_text=limits_text.replace('审查进行中的可得材料另见进度，不把它们列成缺失资源。','可得且可审的有限材料已完成静态对照；以下具名边界没有被冒充缺失文件或运行通过。');limits_path.write_text(limits_text)
 for f in fs:groups[f['module']][f['disposition']]+=1
 coverage=f'''# 覆盖结论与计数口径

本轮已完成可得且可审有限材料的全量静态双向对照，具名不能解析/不能运行或缺材料的范围保留于limits-and-missing-materials.md。可读但尚未审的语义范围为0；不是全部机器码控制流、原生宿主、完整Demo或无界动态输入通过。

固定R盘点432个tracked文件；B5全部131份正式文件、113份现行原稿/有效附表及47份补充与审计上下文文件进入逐文件接收，共723个文件身份。47份中含有资格的正文/附表及导航，不能全计为独立规范；32项有效补充的分层处置以C00/effective-attachment-join和supplemental-scope为准。B5的全部37779个tracked路径也已分类，冻结历史、重复/生成清单、行政回执与现行事实分开；原62未跟踪准备材料完整保留。432与131不是语义通过率。

主矩阵含1460个稳定审计scope、1295个投影、25704个逆向条款/数据/向量单位和3849个语义记录身份；106条最终规范规则裁决覆盖层另列，避免最后增量被旧模块快照漏接。它们不是可相加的产品功能数，唯一产品功能数量不作虚假估计。每个范围保留源/规格锚点、caller/override、前提、配置/宿主、已审范围、标准status及理由、证据、发现、依赖和未知。字段引用可在ASM/evidence-fields精确解析；最后431个未单独定位的字段已逐项补上，13段共同前提另有root实读证据。

status统计：{json.dumps(dict(collections.Counter(r['status']for r in rows)),ensure_ascii=False)}。supported只覆盖所列条件，partial/missing是B5合同结果，unresolved保留政策或材料/宿主边界；这些不等于阅读未完成。本次未修改B5。

主领域各自负责完整有限源和当前合同一次；共享/反证只重读必要交界。106条规范记录及92必修均完成非提出者反证、root去重与定向裁决。原提出报告中的候选/旧严重度/待接收文字是冻结过程记录，以根findings及接收层为当前权威。

共享合同有{shared['primary_identity_count']}个唯一审计主身份，182个领域交接路由和{len(shared['finding_label_routes'])}个发现局部标签映射；同一事实的别名与消费投影不新增功能。JXN具名链检查与历史54条交界记录、8条组合链、GR3新增18条链、GR4旧14条链及具名案例/异常表的实际连接按最终账逐项保留，不继承历史PASS。

GR4：17控制/76标准实际复查，16控制/75标准在原限定范围支持，Summary残留对应GR5-M04-002。GR3：23控制/76标准限定支持；原OPTIONAL/U08未启动与NO_REQUIRED保持。第二轮229控制/341贡献保持精确owner/scope，各当前关联已逐项审读。新发现不是因旧控制关闭而忽略，也不凭主题相似重开旧控制。

R5新增4条隔离参考执行记录，其他静态向量不是执行；R4历史4条分开。原生宿主、完整Demo和独立行为模型均新增0。解析、hash、JSON、链接与远端完整字节读回仅属TOOL_VALIDATION。
'''
 (O/'coverage-summary.md').write_text(coverage)
 lines=['# 第五轮全局独立审查报告','',f"完成可得且可审有限材料的全量静态双向对照。当前B5为独立实现提供了广泛且细致的行为基础，但仍有 **92项必修（51 P2、41 P3，无P1）**，不能把现有规格视为无需猜测即可完整实现的最终合同。另有7项可选、7项无需另修、事实争议未决0；6项兼容政策选择另列，当前无需用户决定。",'',
 '主要风险集中在作者内容的接受/拒绝与反写损失、数据默认和查询副作用、世界/界面同轮输入与时间顺序、个体/道具部分提交、战斗异常后的继续路径与共享状态、AI消费实际规则，以及资源选择和工具编辑保存边界。每项都给出具体前提、反例和最小修订，不因风格偏好立必修，也不将一个源方法机械视为新接口。','',
 '## 固定输入与完成范围','',f'B5 `{a.B5}`，tree `594e65edcb192a19110540245fc1663bae2de007`，正式131子树 `d5a462b4c6f8b78c3264a25d6b5495230fa265e2`；R `{a.RC}`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。未发现新的资源叠加包。', '',coverage.split('\n\n',1)[1],
 '## 领域结果','', '| 领域 | 必修 | 可选 | 无需另修 |','| --- | ---: | ---: | ---: |']
 for m,c in sorted(groups.items()):lines.append(f"| {m} | {c['required']} | {c['optional']} | {c['no_required_revision']} |")
 lines+=['','所有106项标题和处置见[findings-summary.md](findings-summary.md)，逐项完整证据见[findings.json](findings.json)；完整交接正文将全部必修展开，不仅列标题或要求下一轮自行猜测。','',
 '## 独立性与裁决','', '主审、反证审者和跨域审查均请求gpt-6-astra、ultra、普通default、禁Fast。请求已接纳，实际运行参数回显UNVERIFIED；未进行额度、计费、认证或后端审计。真实任务ID、输出和CLI日志见task-register.json。root亲审与非提出者反证角色分别登记；没有虚构独立签名。','',
 '每项必修完成一次有效的非提出者直接源/规格反证，再由root定向整合。收窄的条件、已有正确合同、合并重复和降级理由保留；例如道具四项默认由M05唯一主责，M01-016只保留余下默认子表；M01-019/020为重复投影。旧报告保持冻结，用后继裁决解释，不回写历史。','',
 '## 材料、运行与政策限制','',(O/'limits-and-missing-materials.md').read_text(),'',
 '六项具名兼容政策在unresolved-decisions.json展开：旧背包false输入、旧文本/数值便利输入、数组对称差、常量便利入口、隐式回调上下文、温度转换舍入。固定源事实已读；是否将这些旧便利入口/怪异输入作为未来兼容承诺另由用户决定，下一轮不自动实现或扩成必修。一般参考缺陷也如实记录，修订事实不代表决定永久兼容。','',
 '## 下一轮有限修订与授权','', 'proposed-update-batches.json安排7个实质批次及1个最终整合批次，92必修各有唯一主责，共享文件唯一写者及DAG已列。可并行准备，依赖未满足不得整合/接受/关闭。每批需作者候选、真正独立候选复审、精确实际字节复审和唯一登记；旧PASS与候选PASS均不能转签。', '',
 '下一轮仍只修订规格、测试/附表和必要追溯，作者/登记请求gpt-6.1-sol xhigh、独立review请求gpt-6.1-sol ultra，均default禁Fast。本轮只生成完整中文handoff；必须由用户以后交回并要求执行才启动，未发送或启动整改。','',
 '## 发布与保护','', f'只提交并普通push独立报告分支 `{a.BRANCH}`。本语义报告的commit/tree由后继manifest和publication-receipt精确绑定；最终远端验证从新建隔离裸仓库普通fetch，完整读取本轮所有artifact blob并核bytes/SHA256/Git blob，不能用HTTP状态或本地hash冒认远端证明。', '',
 '正式集、固定R、既有历史证据和用户原内容未作修订；原62个未跟踪文件、stash与其他12个worktree受保护。最终实际核验结果以publication-receipt为准。main没有合并或推送，本轮未实现新引擎。']
 (O/'final-report.md').write_text('\n'.join(lines)+'\n')
 return coverage

CORE_ARTIFACTS=['final-report.md','findings.json','counterevidence-resolution.json','corpus-inventory.json','inventory-and-reading-coverage.json','source-to-spec-coverage.json','spec-to-source-coverage.json','shared-contracts.json','junction-review.json','regression-fourth-17.json','regression-third-23.json','regression-legacy-scope.json','proposed-update-batches.json','shared-file-owners.json','execution-evidence.json','limits-and-missing-materials.md','unresolved-decisions.json','task-register.json']
def file_identity(p):
 data=(O/p).read_bytes();return{'path':a.PREFIX+'/'+p,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}
def handoff(result,plan,owners,shared,report_commit=None,report_tree=None):
 # Called only after finite semantic closure. The second pass binds navigation to the frozen semantic commit.
 head=['# 第五次云端规格 update 完整任务书','',a.HANDOFF_RULES,'','## 固定审查结果与交接身份','',
 f'仓库：{a.REPO}。正式输入B5：`{a.B5}`，tree `594e65edcb192a19110540245fc1663bae2de007`，正式131子树 `d5a462b4c6f8b78c3264a25d6b5495230fa265e2`。不可变正式交付标签为`delivery/fourth-round-clean-final-20261012`。R：`{a.RC}`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，仓库`Maruno17/pokemon-essentials`；无新资源包叠加。', '',
 f'报告分支：`{a.BRANCH}`。冻结语义报告commit：`{report_commit or "SEMANTIC_COMMIT_BOUND_BY_PUBLICATION_SUCCESSOR"}`；tree：`{report_tree or "SEMANTIC_TREE_BOUND_BY_PUBLICATION_SUCCESSOR"}`。本任务书的实质内容随语义报告冻结，后继仅补这些提交导航及manifest/发布回执。禁止因此重做全局审查。', '',
 '规范记录106：required92（P1 0、P2 51、P3 41）、optional7（P3）、no_required_revision7（不分必修严重度）、unresolved事实0。另6项兼容政策不计事实缺陷。原提出者候选旧等级/待反证用词不覆盖根findings.json的最终裁决。全部必修均通过非提出者反证和root定向裁决；B5当前仍未整改。','',
 '本轮可得且可审有限材料已静态审完：432固定R文件、131正式、113原稿和47补充/上下文逐项处置；1460审计scope、1295投影、25704逆向单位、3849语义记录不是独立功能总数。全部当前正式正文/附表/案例/测试与有效补充都有逆向去向。具名宿主/媒体/机器码边界见下文，不把这些未知写成运行通过。', '',
 '### 必需产物固定路径及身份','',
 '下表绑定冻结语义报告内的完整文件。其他必需审者证据的完整清单在cloud-fifth-update-handoff-manifest.json；后继publication-receipt提供其最终commit/tree及精确身份，终局交付也提供固定链接与自身SHA。读取后核完整bytes、SHA256和Git blob；不能只查HTTP状态。', '',
 '| 固定文件 | bytes | SHA256 | Git blob |','| --- | ---: | --- | --- |']
 for p in CORE_ARTIFACTS:
  i=file_identity(p);url=f'{a.REPO}/blob/{report_commit}/{i["path"]}'if report_commit else i['path'];head.append(f'| [{p}]({url}) | {i["bytes"]} | {i["sha256"]} | {i["git_blob"]} |')
 head+=['','### 有限批次与唯一写者','',a.markdown_value(plan),'',a.markdown_value(owners),'','### 共享主合同与整合顺序','',f'{shared["primary_identity_count"]}个唯一主身份；182个领域交接及{len(shared["finding_label_routes"])}个发现局部标签映射。每个合同的输入/写入/消费/显示/持久/失败前缀在固定shared-contracts逐项列明。下列是唯一审计owner和本次受影响发现，不要求照此建未来代码模块：','', '| 主合同 | 唯一审计主责 | 本次发现 |','| --- | --- | --- |']
 for c in shared['contracts']:head.append('| '+c['id']+' | '+c['primary_review_owner']+' | '+', '.join(c.get('canonical_findings',[]))+' |')
 for c in shared['contracts']:
  if c.get('canonical_findings'):
   head+=['', '#### 受影响共享合同 '+c['id'], '', a.markdown_value({{'producer':'生产者及输入','write':'写入与提交','consumer':'消费者与反向复查','display':'显示边界','persistence':'持久与清理','changes':'变化顺序','failure':'拒绝、取消、异常与部分提交','review_boundary':'限定范围'}.get(k,k):c[k] for k in ['producer','write','consumer','display','persistence','changes','failure','review_boundary'] if k in c})]
 head+=['','## 全部必修：完整事实、前提、反例、最小修订与逐项验收','', '以下每项的B5/R统一使用上面的固定身份；路径用于证据定位，事实正文不要求复制原实现组织。所有列出的正常/边界与排除条件必须一并承接。仅做最小接收文件中的必要改动，不能把可选projection文件视为已授权必须改写。']
 for f in result['findings']:
  if f['disposition']=='required':head+=['',a.render_finding(f)]
 head+=['','## 可选、无需另修和政策事项','', '下列7项optional及每条必修内明确排除的optional facets不自动授权；7项no_required_revision保留事实/去重理由。不得为凑关闭数改动它们，也不把重复接收项当作B5已修。']
 for f in result['findings']:
  if f['disposition']!='required':head+=['',a.render_finding(f)]
 head+=['','### 六项兼容政策及一般设计边界','',a.markdown_value(a.read('unresolved-decisions.json')),'','## 材料和运行的完整限定','',(O/'limits-and-missing-materials.md').read_text(),'','## 交接启动门','',
 '用户以后明确要求开始，才核固定输入、保护工作区并启动R5-U01；其他批次可依DAG并行只读准备。持续推进已具备条件的后继批次，不以阶段结束提前停工。实际接受完成后只普通push整改分支，不合并或push main。发生真正阻塞时保留成果并指出具体范围和最小恢复条件，不能用重复全局review替代已授权整改。']
 (O/'cloud-fifth-update-handoff-prompt.md').write_text('\n'.join(head)+'\n')

def current_navigation(result):
 c=a.read('modules/C00/progress.json');c.setdefault('prior_complete_flag',c.get('complete'));c.update(complete=True,status='root_scope_and_global_finite_reception_complete',final_authority='inventory-and-reading-coverage.json; findings.json; shared-contracts.json',available_unreviewed_scope=[],native_and_policy_limits='limits-and-missing-materials.md; unresolved-decisions.json');a.write('modules/C00/progress.json',c)
 m=a.read('modules/M11/progress.json');m.setdefault('prior_phase_status',m.get('status'));m.update(status='root_primary_and_nonproposer_counterevidence_received',final_canonical_findings='counterevidence/root-M11/canonical-findings.json');a.write('modules/M11/progress.json',m)
 d=a.read('task-register.json')
 for t in d['tasks']:
  t.setdefault('historical_progress_status',t.get('status'));t['status']='complete_assigned_scope_root_received';t['completion_basis']='具名module/counterevidence和root reception；完成所分配有限范围，不由状态标签代替语义证据。'
  progress_path=O/'modules'/t['module']/'progress.json'
  if progress_path.exists() and a.read(str(progress_path.relative_to(O))).get('complete') is True:
   if 'reviewer_reported_complete'in t:t.setdefault('historical_reviewer_reported_complete',t['reviewer_reported_complete'])
   t['reviewer_reported_complete']=True;t['reviewer_completion_source']=str(progress_path.relative_to(O))
 for t in d.get('queued_scopes',[]):t['status']='completed_assigned_scope'
 d['current_open_work']=[];d['semantic_review_complete']=True;d['publication_evidence']='publication-receipt.json';a.write('task-register.json',d)
 previous=a.read('progress.json')
 if not(O/'modules/C00/progress-before-semantic-freeze.json').exists():a.write('modules/C00/progress-before-semantic-freeze.json',previous)
 a.write('progress.json',{'schema_version':'gr5.progress.final.v2','updated_at':a.now(),'status':'FINITE_STATIC_REVIEW_COMPLETE','complete':True,'formal_baseline':a.B5,'reference_baseline':a.RC,'counts':result['counts'],'coverage':'inventory-and-reading-coverage.json','available_readable_unreviewed_scope':[],'limits':'limits-and-missing-materials.md','all_required_nonproposer_counterevidence_complete':True,'global_shared_and_bidirectional_joins_complete':True,'task_register':'task-register.json','execution':'execution-evidence.json','publication_status_source':'publication-receipt.json（后继发布回执绑定实际remote字节，不回写语义报告）','protected_inputs_not_modified':True,'next_update_started':False})
 (O/'progress.md').write_text('# 第五轮审查完成\n\n可得且可审有限材料的全量静态双向对照、全部必修独立反证、跨域整合与历史限定回归已完成。106条规范记录：92必修（51P2、41P3）、7可选、7无需另修，事实争议未决0；另6项政策选择。\n\n可读未审范围0；具名缺材料/不透明内部/宿主与动态边界见limits-and-missing-materials.md。运行证据按R4与R5分期保留。\n\n当前发布状态、commit/tree和全量远端字节证据由后继publication-receipt.json提供。正式集、R、历史和用户内容未修订；main未合并或推送，下一轮未启动。实际任务入口见task-register.json。\n')
 (O/'README.md').write_text(f'''# 第五轮全局独立审查

固定B5 `{a.B5}`；固定R `{a.RC}`。本目录只含审查、证据、报告和下一轮交接，正式集与参考未修订。

可得且可审有限材料的全量静态双向对照完成；106条规范记录：92必修（51P2、41P3）、7可选、7无需另修，事实争议未决0。6项兼容政策另列。运行与不透明/缺资料范围严格分开。

- [完整报告](final-report.md)、[发现摘要](findings-summary.md)、[全部规范发现](findings.json)、[独立反证](counterevidence-resolution.json)
- [覆盖说明](coverage-summary.md)、[源→规格](source-to-spec-coverage.json)、[规格→源](spec-to-source-coverage.json)、[逐文件阅读](inventory-and-reading-coverage.json)、[全语料盘点](corpus-inventory.json)
- [跨域链](junction-review.md)、[共享唯一主合同](shared-contracts.json)、[发现局部标签路由](shared-contract-routing.json)
- [GR4 17项](regression-fourth-17.json)、[GR3 23项](regression-third-23.json)、[旧229/341限定范围](regression-legacy-scope.json)
- [执行](execution-evidence.json)、[材料/宿主限制](limits-and-missing-materials.md)、[政策边界](unresolved-decisions.json)
- [完整中文下一轮任务书](cloud-fifth-update-handoff-prompt.md)、[机器manifest](cloud-fifth-update-handoff-manifest.json)、[批次DAG](proposed-update-batches.json)、[唯一文件写者](shared-file-owners.json)
- [发布回执](publication-receipt.md)、[发布机器证据](publication-receipt.json)、[进度](progress.md)、[实际任务入口](task-register.json)

实际子任务ID、角色、范围、模型请求及CLI日志均登记在task-register.json；root亲审另列。全部请求gpt-6-astra/ultra/default/禁Fast，实际参数回显UNVERIFIED。没有虚构独立会话或运行证据。

报告分支 `{a.BRANCH}`，仅本目录可写。模块原始候选与历史过程记录保留，当前裁决以根findings/覆盖接收层为准；完整语义报告提交与后继导航/发布提交分别由manifest和publication-receipt绑定。用户之后交回任务书并要求开始，才启动update。
''')

def manifest(report_commit,report_tree):
 paths=[]
 for p in sorted(O.rglob('*')):
  if not p.is_file()or'__pycache__'in p.parts or p.suffix=='.pyc'or p.name=='.DS_Store':continue
  rel=str(p.relative_to(O))
  if rel in ['cloud-fifth-update-handoff-manifest.json','publication-receipt.json','publication-receipt.md']:continue
  ident=file_identity(rel);assert ident['bytes']<100_000_000,(rel,ident['bytes']);paths.append(ident)
 result=a.read('findings.json');base=a.read('baseline.json');plan=a.read('proposed-update-batches.json');owners=a.read('shared-file-owners.json')
 d={'schema_version':'gr5.handoff-manifest.v2','repository':'y805939188/pokemon-essentials-clean-room','formal_baseline':base['formal_baseline'],'reference_baseline':base['reference_baseline'],'resource_scope':base['resource_overlay'],'review_snapshot':{'commit':report_commit,'tree':report_tree,'branch':a.BRANCH,'report_root':a.PREFIX,'semantic_report_is_immutable':True,'navigation_binding_is_successor_only':True},'corpus_scope':{'reference_files':432,'formal_files':131,'original_files':113,'supplement_context_files':47,'fixed_file_identities_in_reading_index':723,'tracked_B5_inventory':37779,'original_untracked_preserved':62,'scope_records':1460,'projections':1295,'inverse_units':25704,'semantic_records':3849,'unique_product_capability_count':None},'coverage_completion':{'finite_readable_static_complete':True,'available_readable_not_reviewed':[],'native_whole_machine_code_or_host_not_claimed':True,'limits_path':a.PREFIX+'/limits-and-missing-materials.md','status_is_not_execution_or_reading_extent':True},'report_artifacts':paths,'artifact_count_excluding_manifest_and_successor_receipts':len(paths),'artifact_identity_rule':'Each listed bytes/SHA256/Git blob binds complete artifact bytes. This manifest and successor publication receipts have external identities in final delivery/remote proof, avoiding self-hash recursion. Frozen semantic files live at review_snapshot; navigation-only successor artifacts are resolved by publication receipt.','canonical_findings':[{'id':f['id'],'module':f['module'],'severity':f['severity'],'disposition':f['disposition'],'batch_owner':f.get('batch_owner'),'root_cause_group':f['root_cause_group'],'full_record':{'path':a.PREFIX+'/findings.json','pointer':f'/findings/{n}'}}for n,f in enumerate(result['findings'])],'dispositions':result['counts'],'batch_plan':plan,'dependency_edges':plan['dependency_edges'],'shared_owners':owners,'legacy_scope_links':{'fourth':file_identity('regression-fourth-17.json'),'third':file_identity('regression-third-23.json'),'legacy':file_identity('regression-legacy-scope.json'),'historical_approvals_not_transferred':True},'acceptance_rules':{'all_required_nonproposer_counterevidence_complete':True,'next_update_requires_author_candidate_independent_review_actual_bytes_review_and_unique_registration':True,'no_early_dependency_closure':True,'historical_qualification_preserved':True,'static_and_runtime_separate':True,'full_handoff':file_identity('cloud-fifth-update-handoff-prompt.md')},'execution_summary':a.read('execution-evidence.json'),'unresolved_decisions':a.read('unresolved-decisions.json'),'authorized_scope':{'this_desktop_turn':'review/evidence/report/handoff, local isolated verification and report-branch commit/normal push/readback only','future_update_start':'only after human later returns this handoff and explicitly instructs execution','future_required_scope':plan['authorized_findings'],'future_author_model':'gpt-6.1-sol/xhigh/default','future_independent_review_model':'gpt-6.1-sol/ultra/default','Fast':'forbidden'},'excluded_scope':['modify R in this review','modify formal specifications in this review','overwrite historical evidence or user work','implement new framework','merge or push main','force push','start or message next cloud update','automatically implement optional or unresolved policies'],'publication_evidence':{'successor_receipt_path':a.PREFIX+'/publication-receipt.json','remote_validation_method':'fresh separate bare git fetch and complete blob streaming; full bytes/SHA256/Git blob comparison','manifest_self_identity':'Final response and successor receipt bind this file; not recursively embedded.'}}
 a.write('cloud-fifth-update-handoff-manifest.json',d);return d

def assemble():
 gates();fs=a.findings();assert len(fs)==106 and sum(f['disposition']=='required'for f in fs)==92
 shared,chain=shared_contracts(fs);result=decisions_and_findings(fs,shared);a.assemble_regressions(fs);plan,owners=plans(fs);rows,files=coverages(fs)
 adj=a.read('coverage-adjudications.json');adj.update(complete=True,pending=[],final_root_authority='findings.json and source-to-spec-coverage.json',final_receptions=['modules/C00/M01-followup-reception.json','modules/C00/C01F-final-reception.json','modules/C00/M02-followup-reception.json','modules/C00/REG-final-reception.json','modules/C00/JXN-final-reception.json','modules/C00/ASM-final-reception.json']);a.write('coverage-adjudications.json',adj)
 current_navigation(result);reports(result,rows,files,shared,chain,plan);handoff(result,plan,owners,shared)
 a.write('modules/C00/semantic-assembly-receipt.json',{'schema_version':'gr5.semantic-assembly.v1','complete':True,'created_at':a.now(),'finding_counts':result['counts'],'scope_rows':len(rows),'shared_contracts':shared['primary_identity_count'],'full_static_complete_with_named_limits':True,'publication_not_claimed_here':True})
 print(json.dumps({'assembled':True,'findings':result['counts'],'scope_rows':len(rows),'shared_contracts':shared['primary_identity_count']},ensure_ascii=False))

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('action',choices=['assemble','bind']);ap.add_argument('--report-commit');ap.add_argument('--report-tree');args=ap.parse_args()
 if args.action=='assemble':assemble()
 else:
  assert args.report_commit and args.report_tree
  assert a.git('rev-parse',args.report_commit+'^{tree}')==args.report_tree
  result=a.read('findings.json');plan=a.read('proposed-update-batches.json');owners=a.read('shared-file-owners.json');shared=a.read('shared-contracts.json')
  handoff(result,plan,owners,shared,args.report_commit,args.report_tree);m=manifest(args.report_commit,args.report_tree);print(json.dumps({'bound':True,'artifact_count':m['artifact_count_excluding_manifest_and_successor_receipts'],'handoff':file_identity('cloud-fifth-update-handoff-prompt.md'),'manifest':file_identity('cloud-fifth-update-handoff-manifest.json')},ensure_ascii=False))
