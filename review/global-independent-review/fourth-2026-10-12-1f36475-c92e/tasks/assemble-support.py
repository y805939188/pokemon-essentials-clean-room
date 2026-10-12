import pathlib,json,collections,hashlib,datetime,copy
r=pathlib.Path(__file__).resolve().parent.parent
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';B='1f36475d22120a0d1175967d5b17d71fe8311d88'
def save(name,x):(r/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def levels(items):
 if isinstance(items,str):items=[items]
 return list(dict.fromkeys(next((e for e in ['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR','TOOL_VALIDATION','EXECUTED_MODEL','EXECUTED_REFERENCE','EXECUTED_HOST_OR_DEMO'] if str(v).startswith(e)),str(v)) for v in items))
mods=[f'M{x:02d}' for x in range(1,13)];caps=[];sp=collections.defaultdict(list);module_stats=[]
for m in mods:
 launch=json.loads((r/'tasks'/(m+'-launch.json')).read_text());assert launch['status']=='PROCESS_COMPLETED'
 cc=json.loads((r/'modules'/m/'capabilities.json').read_text());cc=cc if isinstance(cc,list) else cc.get('records',cc.get('capabilities'))
 for i,c in enumerate(cc):
  c=copy.deepcopy(c);c['evidence_level']=levels(c.get('evidence_level',[]));c['submission_identity']={'path':f'modules/{m}/capabilities.json','pointer':'/'+str(i),'reviewer_thread_id':launch['thread_id']};c['scope_record_not_independent_function_count']=True;caps.append(c)
 dd=json.loads((r/'modules'/m/'spec-coverage.json').read_text());dd=dd if isinstance(dd,list) else dd.get('files',dd.get('records'))
 for i,s in enumerate(dd):sp[s['path']].append({'reviewer_module':m,'reviewer_thread_id':launch['thread_id'],'artifact':f'modules/{m}/spec-coverage.json','pointer':'/'+str(i),'status':s.get('status','partial'),'contracts_checked':s.get('contracts_checked',[]),'support_evidence':s.get('support_evidence'),'dependencies':s.get('dependencies',[]),'unsupported_assertions':s.get('unsupported_assertions',[]),'not_checked':s.get('not_checked',s.get('limits')),'source_anchors':s.get('source_anchors',[])})
 module_stats.append({'module':m,'name':json.loads((r/'tasks/module-plan.json').read_text())[m]['name'],'reviewer_thread_id':launch['thread_id'],'scope_records':len(cc),'scope_status_counts':dict(collections.Counter(c['status'] for c in cc)),'spec_file_projection_count':len(dd),'source_scope_artifact':f'modules/{m}/source-scope.json','report':f'modules/{m}/report.md','status':'COMPLETED_BOUNDED_SEMANTIC_REVIEW'})
inv=json.loads((r/'evidence/reference-inventory.json').read_text());known={x['path']:x for x in inv};readmap=collections.defaultdict(list)
def walk(o):
 if isinstance(o,dict):
  if o.get('path') in known:yield o
  for v in o.values():yield from walk(v)
 elif isinstance(o,list):
  for v in o:yield from walk(v)
for m in mods:
 data=json.loads((r/'modules'/m/'source-scope.json').read_text())
 for x in walk(data):
  flag=next((x[k] for k in ['inspection','status','review_status','review_state','review_depth','read_status'] if k in x),'not_reviewed')
  readmap[x['path']].append({'module':m,'declared_depth':flag,'declared_scope':{k:v for k,v in x.items() if k in ['checked_range','not_checked','read_extent','limitation','read_loci','limits','read_scope','ranges_read_semantically','semantic_ranges','remainder','scope','semantic_anchors','read_ranges_or_symbols','read_ranges','read_anchors','not_reviewed']},'source_scope_artifact':f'modules/{m}/source-scope.json'})
source_rows=[];respons={x['path']:x['primary_owner'] for x in json.loads((r/'tasks/source-responsibility.json').read_text())}
for p,x in known.items():
 rr=readmap[p];anchored=[c['capability_id'] for c in caps if any(a.get('path')==p for a in c.get('source_anchors',[]))]
 semantic=[q for q in rr if 'semantic' in str(q['declared_depth']).lower() and 'not_' not in str(q['declared_depth']).lower()]
 # Never infer whole-file semantic completeness, including declarations called 'full read'.
 source_rows.append({'path':p,'tracked_reference':x['tracked'],'identity':{k:x[k] for k in ['bytes','sha256','git_blob']},'primary_inventory_owner':respons[p],'status':'partial' if semantic or anchored else 'not_reviewed','status_meaning':'具名片段/事实被审；不表示整文件全部行为通过' if semantic or anchored else '仅身份/资料盘点或本轮无语义依据；不代表缺功能','material_availability':'available_readable' if x['tracked'] else 'local_metadata_nonsemantic','semantic_readers':semantic,'inspection_kind':('semantic_partial' if semantic else 'header_only' if anchored else 'inventory_only'),'other_inventory_projections':[q for q in rr if q not in semantic],'related_scope_record_ids':anchored})
formal=json.loads((r/'tasks/formal-ownership.json').read_text());fr=[]
for f in formal:
 ps=sp[f['path']];actual=[p for p in ps if p['status']!='not_reviewed'];statuses={p['status'] for p in actual};status='not_reviewed'
 if actual:status='partial' if ('partial' in statuses or 'missing' in statuses) else ('unresolved' if 'unresolved' in statuses else 'supported')
 anchors=[];seen=set()
 for p in ps:
  for a in p['source_anchors']:
   k=json.dumps(a,ensure_ascii=False,sort_keys=True)
   if k not in seen:anchors.append(a);seen.add(k)
 # Compact projections: common source anchors appear once in row, precise mapping retained by immutable module pointer.
 concise=[{k:v for k,v in p.items() if k!='source_anchors'} for p in ps]
 fr.append({'path':f['path'],'primary_owner':f['primary_owner'],'contract_reviewers':f['contract_reviewers'],'identity_at_B':{**f['baseline_identity'],'commit':B,'tree':'d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a'},'historical_accepted_identity':f['baseline_identity'],'status':status,'status_scope':'仅下列contracts_checked；整文件剩余条款不自动通过','material_availability':'available_verified_bytes','evidence_level':['SOURCE_STATIC','SPEC_STATIC'] if actual else [],'contracts_and_evidence':concise,'source_anchors':anchors,'unreviewed_remainder':'见各投影not_checked及相应模块source-scope/report；未逐段核对的条款不因文件有记录而通过。'})
shared=json.loads((r/'modules/J/shared-capabilities.json').read_text())
common={'schema_version':'1.0','formal_baseline':{'commit':B,'tree':'d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a'},'reference_baseline':{'commit':R,'tree':'7589c800b61ba13a13040ed0d686979b80a84fd0'},'status':'BOUNDED_DOMAIN_REVIEW_COMPLETE_FINDING_ADJUDICATION_SEPARATE','counting_rule':'300 non-mutually-exclusive scoped review records are not 300 independent functions. Shared contracts have one JSC identity and one primary document; junction consumers are projections, not new feature counts. No full-capability percentage is calculated.','supported_meaning':'supported_static for the exact checked premises/branches when evidence is SOURCE_STATIC/SPEC_STATIC; any isolated execution is separately scoped.'}
save('source-to-spec-coverage.json',{**common,'scope_record_count':len(caps),'module_results':module_stats,'capability_scope_records':caps,'shared_capability_registry':shared,'source_file_coverage':source_rows})
save('spec-to-source-coverage.json',{**common,'formal_file_count':len(fr),'files':fr})
# All GR3 members retain historical identity; new scoped evidence is attributed without copying signatures.
g=json.loads((r/'regression-third-23.json').read_text());targets={x['id']:x for x in g['records']}
for t in targets.values():t['actual_semantic_reviews']=[];t['fourth_status']='not_reviewed'
for m in mods:
 d=json.loads((r/'modules'/m/'regression.json').read_text());rows=d if isinstance(d,list) else d.get('records',d.get('regressions',[]))
 for i,row in enumerate(rows):
  id=row.get('id',row.get('finding_id',row.get('legacy_id')))
  if id not in targets:continue
  t=targets[id];t['fourth_status']='supported_static_scoped';t['actual_semantic_reviews'].append({'module':m,'reviewer_thread_id':json.loads((r/'tasks'/(m+'-launch.json')).read_text())['thread_id'],'path':f'modules/{m}/regression.json','pointer':('/' if isinstance(d,list) else '/records/')+str(i),'record':row});t['limitations']=['仅实际列明criteria/consumer获本轮复查；不等于76条全部执行或所有组合/宿主通过。','历史CLOSED由旧固定回执保持，本轮不重写。']
g['fourth_completion']='COMPLETE_BOUNDED_REGRESSION_MAPPING';g['current_status_counts']=dict(collections.Counter(t['fourth_status'] for t in g['records']));g['new_execution_qualification']='M12 adds isolated original rating-settlement observations for named inputs; this is not full simulation/host execution or retrospective execution of the historical test catalog.';save('regression-third-23.json',g)
# Attributed module records, no execution falsely created by aggregation.
e=json.loads((r/'execution-evidence.json').read_text());rootrecs=[x for x in e['records'] if x.get('id','').startswith('GR4-TOOL-')];records=rootrecs;notrun=[]
for m in mods+['CA','CB','J']:
 p=r/'modules'/m/'execution.json'
 if not p.exists():continue
 d=json.loads(p.read_text());es=d.get('actual_executions',d.get('executions',d.get('records',[])))
 for i,x in enumerate(es):records.append({'origin_module':m,'artifact':f'modules/{m}/execution.json','pointer':'/actual_executions/'+str(i),'evidence_level':x.get('evidence_level',x.get('kind','TOOL_VALIDATION')),'record':x,'aggregation_is_not_a_rerun':True})
 if d.get('not_executed'):notrun.append({'origin_module':m,'records':d['not_executed']})
counts=collections.Counter(x.get('evidence_level') for x in records)
save('execution-evidence.json',{'schema_version':'1.0','status':'ATTRIBUTED_ACTUAL_EXECUTION_RECORDS','historical_execution_claim':e['historical_execution_claim'],'counts_by_record_not_testcase':dict(counts),'behavior_claim_limit':'原参考隔离执行与宿主分开。退出码0可包含按计划捕获的异常，不等于功能全部通过；静态向量/JSON/哈希/格式头不升级成行为执行。','records':records,'module_not_executed':notrun,'reference_probe_runs':[x for x in records if x.get('evidence_level')=='EXECUTED_REFERENCE'],'no_full_host_or_demo_execution':True,'legacy_runtime_states_unchanged':True})
# Independent 14-chain inspection + exact navigation for all historical 80.
j=json.loads((r/'modules/J/junctions.json').read_text());nav=json.loads((r/'evidence/junction-navigation.json').read_text());by={x['id']:[] for x in nav['records']}
for i,x in enumerate(j['records']):
 for old in x.get('historical_junction_ids',[]):
  assert old in by,old;by[old].append({'junction_id':x['id'],'status':x['status'],'artifact':'modules/J/junctions.json','pointer':'/records/'+str(i),'scope':x['title'],'restriction':'Only current named projection, not reapproval of the whole historical junction/chain.'})
for x in nav['records']:
 x['current_semantic_reviews']=by[x['id']];x['fourth_review_status']='partial' if by[x['id']] else 'not_reviewed';x['history_use']='historical_qualified_evidence_reused / not_reexecuted; navigation verified; new scope only if explicitly linked'
save('junction-review.json',{'schema_version':'1.0','independent_reviewer_thread_id':j['thread_id'],'records':j['records'],'status_counts':dict(collections.Counter(x['status'] for x in j['records'])),'historical_navigation_and_projections':nav,'historical_projection_counts':{'with_fresh_scoped_projection':sum(bool(x['current_semantic_reviews']) for x in nav['records']),'navigation_only_not_reaudited':sum(not x['current_semantic_reviews'] for x in nav['records'])},'shared_capability_registry':shared,'retained_controls':j.get('retained_controls'),'independence_limit':'J did not read unsealed M11 submission; J11 concerns record/Area, not acceptance of the new M11 shiny-display finding. CB independently reviews that finding.'})
lines=['# 跨模块整合审查','', '由新独立审者J直接读取固定R与B完成14条有界链，6条supported_static、8条partial；没有新规范问题。主会话核对具体前提、反证和身份后归并，没有把消费者投影再计为新问题。','','|链|结论|范围|','|---|---|---|']
for x in j['records']:lines.append(f"|{x['id']}|{x['status']}|{x['title']}|")
lines += ['',f"历史54交界+8旧链+18新增链共80条，固定导航全部可读；{sum(bool(x['current_semantic_reviews']) for x in nav['records'])}条接到本轮具名有限投影，其余只复用历史限定证据/未新审。不表示这些历史条目完整重新通过。",'', '逐链生产者、状态写入、消费者、条件、正常/失败/取消/重复边界、R/B锚点及未审项见junction-review.json和modules/J/report.md。25项共享契约各有唯一主身份/正文所有者；布局、存储和调用组织不是未来架构建议。','', 'J11图鉴链仅检查记录/Area与可见点，未读取当时未冻结的M11；其supported不能覆盖后来M11提出的普通外观固定请求。该项由CB另作原证据反证。','']
(r/'junction-review.md').write_text('\n'.join(lines))
stats={'capability_scope_records':len(caps),'capability_scope_status_counts':dict(collections.Counter(c['status'] for c in caps)),'formal_file_rows':len(fr),'formal_scope_status_counts':dict(collections.Counter(x['status'] for x in fr)),'tracked_reference_files':sum(x['tracked_reference'] for x in source_rows),'source_file_status_counts':dict(collections.Counter(x['status'] for x in source_rows if x['tracked_reference'])),'source_file_inspection_kind_counts':dict(collections.Counter(x['inspection_kind'] for x in source_rows if x['tracked_reference'])),'shared_contract_identities':len(shared['records']),'execution_record_counts':dict(counts),'GR3':g['current_status_counts'],'junction':{'new_chains':len(j['records']),'status_counts':dict(collections.Counter(x['status'] for x in j['records'])),'historical80_with_scoped_projection':sum(bool(x['current_semantic_reviews']) for x in nav['records'])}}
save('evidence/aggregate-counts.json',stats)
lines=['# 覆盖与证据边界','', '本轮12域均完成独立有界双向审查，正式131文件全部有主责和实际局部核对记录。文件被覆盖不等于整篇每条断言或源端所有变体已通过。','', f"记录{len(caps)}个可交叠的能力范围投影；状态分布："+'，'.join(f'{k} {v}' for k,v in stats['capability_scope_status_counts'].items())+'。它们不是功能全集分母，不计算完整率。', '', f"正式文件行状态：{stats['formal_scope_status_counts']}。这些状态仅约束每行contracts_checked，not_checked与模块报告所列余项继续保留。",'', f"R的432 tracked文件均已盘点；{stats['source_file_status_counts'].get('partial',0)}份有具名范围/能力锚点，{stats['source_file_status_counts'].get('not_reviewed',0)}份仅盘点或无本轮语义依据。前者均记partial，不能从读取范围或文件数推整文件全部语义通过。两个.DS_Store只为保护本地输入，不计参考能力。",'', '共享能力以JSC01–25登记唯一主身份和正文主责；J01–14中的消费者是交界投影，不另计新功能。原模块CAP编号保留为稳定的范围记录身份，引用允许交叠。','','|域|能力范围记录|本域记录状态|独立报告|','|---|---:|---|---|']
for x in module_stats:lines.append(f"|{x['module']} {x['name']}|{x['scope_records']}|{x['scope_status_counts']}|[{x['module']}]({x['report']})|")
lines+=['','未审/部分审查集合以source-to-spec-coverage.json的source_file_coverage、每个CAP的not_checked、反向矩阵的逐契约not_checked及各模块source-scope.json为完整导航。重点仍包括：未抽取的源码子分支/全部效果组合、全PBS/翻译与备份启用、全插件/动态调用、图案/粒子与字体字形、完整地图事件/Demo和真实宿主。','', '材料缺席与规格缺能力分别记录。主图/声音/地图/完整工程及运行宿主未建立；现有字体/根BMP/二进制不能自动推出已解析/可用/执行成功。实际隔离原函数执行另见execution-evidence.json，主机或Demo执行0。','']
(r/'coverage-summary.md').write_text('\n'.join(lines));print(json.dumps(stats,ensure_ascii=False))
