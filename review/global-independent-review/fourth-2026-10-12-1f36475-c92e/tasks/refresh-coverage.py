import pathlib,json,collections,datetime
r=pathlib.Path(__file__).resolve().parent.parent
owners=json.loads((r/'tasks/formal-ownership.json').read_text());sources=json.loads((r/'tasks/source-responsibility.json').read_text());plan=json.loads((r/'tasks/module-plan.json').read_text())
caps=[];projections=collections.defaultdict(list);completed=[];modules=[]
for m in plan:
 launch=r/'tasks'/(m+'-launch.json')
 if not launch.exists():modules.append({'module':m,'status':'not_reviewed','workflow':'PLANNED'});continue
 l=json.loads(launch.read_text())
 if l['status']!='PROCESS_COMPLETED':modules.append({'module':m,'status':'not_reviewed','workflow':l['status'],'qualification':'Review ongoing; incomplete submission not aggregated.'});continue
 completed.append(m)
 cc=json.loads((r/'modules'/m/'capabilities.json').read_text())
 if isinstance(cc,dict):cc=cc.get('capabilities',cc.get('records',[]))
 for c in cc:
  c['submission_artifact']=f'modules/{m}/capabilities.json';c['actual_reviewer_thread_id']=l['thread_id'];c['actual_reviewer_pid']=l['pid'];caps.append(c)
 sc=json.loads((r/'modules'/m/'spec-coverage.json').read_text())
 if isinstance(sc,dict):sc=sc.get('files',sc.get('records',[]))
 for s in sc:
  path=s.get('path',s.get('spec_path'));s['reviewer_module']=m;s['actual_reviewer_thread_id']=l['thread_id'];s['submission_artifact']=f'modules/{m}/spec-coverage.json';projections[path].append(s)
 modules.append({'module':m,'workflow':'SUBMITTED_PENDING_INTEGRATION','status':'partial','record_count':len(cc),'actual_reviewer_thread_id':l['thread_id'],'scope_artifact':f'modules/{m}/source-scope.json','limits':'Submitted finite scope; not whole-module semantic PASS.'})
rev=[]
for o in owners:
 ps=projections[o['path']];ss={p.get('status','not_reviewed') for p in ps}
 real=ss-{'not_reviewed'}
 status='not_reviewed'
 if real:status='partial' if ('partial' in real or 'missing' in real) else ('unresolved' if 'unresolved' in real else 'supported')
 rev.append({**o,'status':status,'status_scope':'Only contracts_checked below; no whole-file or runtime pass. Missing contracts are findings, not absence of material.','current_review_projections':ps,'source_anchors':[a for p in ps for a in p.get('source_anchors',[])],'evidence_level':['SPEC_STATIC','SOURCE_STATIC'] if real else [],'material_availability':'available_verified_bytes','unreviewed_reason':None if real else 'No completed semantic submission yet; file remains assigned.'})
common={'schema_version':'1.0','status':'IN_PROGRESS_PRE_COUNTERREVIEW','updated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'formal_baseline':{'commit':'1f36475d22120a0d1175967d5b17d71fe8311d88','tree':'d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a'},'reference_baseline':{'commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','tree':'7589c800b61ba13a13040ed0d686979b80a84fd0'},'counting_rule':'Finite submitted scoped records, not exhaustive capabilities. Shared projections may overlap; no total-function percentage. supported with static evidence means supported_static only.'}
(r/'source-to-spec-coverage.json').write_text(json.dumps({**common,'module_status':modules,'capabilities':caps,'source_file_responsibility':sources,'shared_identity_resolution':'Pending final cross-domain integration; raw submitted capability IDs retained for traceability.'},ensure_ascii=False,indent=2)+'\n')
(r/'spec-to-source-coverage.json').write_text(json.dumps({**common,'formal_file_count':len(rev),'files':rev},ensure_ascii=False,indent=2)+'\n')
text=['# 覆盖进度（进行中）','', '双向矩阵现已按完成提交汇入；这是有限范围记录，不是全能力通过或全功能百分比。必修仍待独立反证，共享能力身份将在交界阶段归一。','',f"已汇入模块：{', '.join(completed)}。能力范围记录{len(caps)}条；正式文件责任归属{len(rev)}/131，逐文件实际contracts_checked与not_checked见反向矩阵。",'', '| 文件行状态 | 数量 |','|---|---|']
for k,v in collections.Counter(x['status'] for x in rev).items():text.append(f'|{k}|{v}|')
text+=['','所有supported只针对记录的前提/分支和证据类别；文件存在、被列出或有旧PASS不算语义审查。未完成模块仍明确not_reviewed，另有材料可得性和运行限制。','']
(r/'coverage-summary.md').write_text('\n'.join(text))
print(json.dumps({'modules':completed,'capability_scope_records':len(caps),'formal_file_rows':len(rev),'file_status_counts':dict(collections.Counter(x['status'] for x in rev))}))
