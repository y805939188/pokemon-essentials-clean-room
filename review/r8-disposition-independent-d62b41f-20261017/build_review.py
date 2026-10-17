#!/usr/bin/env python3
"""Assemble attributed human review decisions; never assigns routes by keywords."""
from pathlib import Path
import collections, hashlib, json
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
A=OUT/'agents'; E=OUT/'evidence'
def load(p):return json.loads(p.read_text())
def save(name,obj):(OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
manifest=load(ROOT/'planning/implementation-routing/r8-20261017/routing-manifest.json')
independent=load(E/'independent-heading-coverage.json')
locators=load(E/'candidate-feature-locations.json')
feature_sources=[('combat-results.json','feature_results'),('combat-ai-report.json','feature_results'),('creature-kernel-results.json','features'),('world-ui-results.json','feature_results'),('demo-shared-results.json','feature_results'),('pokemon-results.json','results'),('kernel-full-results.json','feature_results')]
rows=[]; findings=[]; attribution=[]
for filename,key in feature_sources:
    d=load(A/filename)
    if key not in d:
        key=next(k for k in ['feature_results','features','results'] if k in d)
    for i,r in enumerate(d[key]):
        verdict=next(r[k] for k in ['verdict','overall_result','status','overall'] if k in r)
        reason=r.get('reason',r.get('semantic_judgment',''))
        refs=r.get('finding_refs',r.get('finding_ids',r.get('findings',[])))
        rows.append({'feature_id':r['feature_id'],'verdict':verdict,'reason':reason,'finding_refs':refs,'review_record':f'agents/{filename}#/{key}/{i}','candidate_locator':locators[r['feature_id']]})
    for f in d.get('findings',[]):
        if f.get('status') in ['OBSERVATION','NONBLOCKING_OBSERVATION'] or f.get('blocking') is False:continue
        ff=dict(f);ff['id']=f.get('id',f.get('finding_id'));ff['review_record_file']='agents/'+filename;findings.append(ff)
    attribution.append({'file':'agents/'+filename,'features':len(d[key])})
for filename in ['world-ui-findings.json','world-catalog-full-results.json','cc-catalog-full-results.json']:
    d=load(A/filename)
    for f in d.get('findings',[]):
        if f.get('blocking') is False or f.get('status') in ['OBSERVATION','NONBLOCKING_OBSERVATION']:continue
        ff=dict(f);ff['id']=f.get('id',f.get('finding_id'));ff['review_record_file']='agents/'+filename;findings.append(ff)
for f in load(OUT/'root-findings.json')['findings']:findings.append({**f,'review_record_file':'root-findings.json'})
ids=[x['feature_id'] for x in rows];expected={x['feature_id'] for x in manifest['features']}
assert len(ids)==len(set(ids)), 'duplicate feature review'
assert set(ids)==expected, f'missing feature decisions: {expected-set(ids)}'
assert all(x['verdict'] in ['PASS','FAIL','待查'] and x['reason'] for x in rows)
assert len({x['id'] for x in findings})==len(findings), 'duplicate finding ID'
findings.sort(key=lambda x:(x.get('severity','P9'),x['id']))
rows.sort(key=lambda x:x['feature_id'])
# Ledgers are explicit declarations of actual body reading by the named contexts.
ledger_inputs=[('combat-results.json','reading_ledger'),('combat-ai-report.json','source_ledger'),('creature-kernel-results.json','documents'),('world-ui-results.json','documents'),('demo-shared-evidence.json','documents'),('pokemon-static-evidence.json','reading_ledger'),('kernel-full-results.json','documents'),('world-catalog-full-results.json','documents'),('cc-catalog-full-results.json','documents')]
ledgers={}
for filename,key in ledger_inputs:
    d=load(A/filename)
    if key not in d:
        key=next(k for k in ['documents','reading_ledger','source_ledger'] if k in d)
    for i,r in enumerate(d[key]):
        path=r.get('path',r.get('source_path'))
        ranges=next((r[k] for k in ['literal_read_ranges','full_body_read_ranges','read_ranges','read_intervals','full_semantic_read_ranges','full_read_ranges','reading_ranges','semantic_read_ranges_inclusive'] if k in r),None)
        if ranges is None and r.get('full_read') is True:ranges=[[1,r.get('line_count',r.get('lines'))]]
        ledgers[path]={'reader_evidence':f'agents/{filename}#/{key}/{i}','read_ranges':ranges,'sha256':r.get('sha256'),'reader_record':{k:v for k,v in r.items() if k not in ['headings','metadata_sections']}}
root_path='deliverables/final-specification-set/test-catalog/README.md'
root_proof=next(x for x in independent['documents'] if x['path']==root_path)
ledgers[root_path]={'reader_evidence':'evidence/root-read-ledger.json','read_ranges':[[1,root_proof['lines']]],'sha256':root_proof['sha256'],'reader_record':{'reader':'/root','method':'actual split reads 1-94 and 95-EOF, including governance and historical layers'}}
documents=[]
for proof in independent['documents']:
    path=proof['path'];r=ledgers.get(path)
    assert r, 'unread document '+path
    assert r['sha256']==proof['sha256'], 'reading identity mismatch '+path
    covered=set()
    for a,b in r['read_ranges'] or []:covered.update(range(a,b+1))
    assert set(range(1,proof['lines']+1)) <= covered, 'body reading range gap '+path
    documents.append({**proof,'body_reading':'FULL_SEMANTIC_READ_BY_ATTRIBUTED_REVIEW_CONTEXT','read_ranges':r['read_ranges'],'reader_evidence':r['reader_evidence']})
assert set(ledgers)>=set(x['path'] for x in independent['documents'])
save('reading-coverage.json',{'candidate_commit':'d62b41f4d620e50bb04c80a7505374bd284d8210','documents':documents,'unread_documents':[],'unread_body_lines':0,'qualification':'Root did not personally reread every delegated body. Every source body was actually read in an attributed context; tools independently verify identity and coverage only. Generated duplicate view text was checked by exact regeneration and per-row projections, not counted as a second full body reading.'})
save('feature-results.json',{'scope':'fixed-baseline coarse routing, including classification, granularity and necessary dependencies; PASS never certifies target behavior','counts':dict(collections.Counter(x['verdict'] for x in rows)),'features':rows})
save('findings.json',{'candidate_commit':'d62b41f4d620e50bb04c80a7505374bd284d8210','findings':findings,'count':len(findings),'counts_by_severity':dict(collections.Counter(x['severity'] for x in findings))})
row_by_id={r['feature_id']:r for r in rows}
doc_by_path={d['path']:d for d in documents}
coverage=load(ROOT/'planning/implementation-routing/r8-20261017/section-coverage.json')
sections=[]
for i,c in enumerate(coverage['sections']):
    sections.append({**{k:c[k] for k in ['document_id','path','line_start','line_end','anchor','title','level','mapping_kind']},'candidate_mapping_pointer':f'/sections/{i}','fixed_identity_and_heading_coverage':'PASS','source_body_reading':doc_by_path[c['path']]['reader_evidence'],'candidate_feature_refs':c['feature_refs'],'reviewed_feature_verdicts':{f:row_by_id[f]['verdict'] for f in c['feature_refs']},'semantic_qualification':'Candidate mapping retained as evidence, including challenged mappings. See findings and attributed source-body review; this is not an automatic semantic PASS for a heading or all its referenced features.'})
save('section-results.json',{'sections':sections,'count':len(sections),'missing_headings':0,'scope':'All headings identity/structural coverage plus body-reading and feature-decision navigation; no keyword-derived route or semantic approval is generated here.'})
roles=collections.defaultdict(lambda:dict(documents=0,bytes=0,lines=0,headings=0))
for d in documents:
    for key in ['bytes','lines','headings']:roles[d['role']][key]+=d[key]
    roles[d['role']]['documents']+=1
counts=dict(collections.Counter(x['verdict'] for x in rows))
checks=[
 {'requirement':1,'result':'FAIL','detail':'131-file/2683-heading identity coverage PASS; semantic behavior omissions and spurious implementation rows are proven.'},
 {'requirement':2,'result':'PASS','detail':'Fixed candidate/source/current bytes and all 721 immutable locators match; seed refuses reseeding. Future accepted-version ID continuity remains to be exercised.'},
 {'requirement':3,'result':'FAIL','detail':'Mixed responsibility/acceptance boundaries omitted; pure metadata inflated into implementation features.'},
 {'requirement':4,'result':'FAIL','detail':'Allowed route labels, excluded=0 and unapproved phases are correct; embedded special-scope decision propagation remains deficient.'},
 {'requirement':5,'result':'FAIL','detail':'Four prototype gates exist and remain unrun honestly; related callers/consumers and persistent-state boundaries are incompletely associated.'},
 {'requirement':6,'result':'FAIL','detail':'All rows separate source/plan/verification/stage/implementation/acceptance correctly; specific ownership and necessary dependency fields remain deficient.'},
 {'requirement':7,'result':'PASS','detail':'Limited to baseline binding: 183 features/32 documents match conservative direct write sets. U07 is navigation outside formal tree. No accepted remediation candidate/receipt received; final calibration pending.'},
 {'requirement':8,'result':'FAIL','detail':'Author validation/fresh generation and original negatives pass; extended static negatives expose locator/reference/acceptance-gate holes.'},
 {'requirement':9,'result':'PASS','detail':'Observed isolation only: delivery->candidate adds 25 routing files; formal tree unchanged; reference clean; review writes isolated. Publication proof is external to enclosing commit.'}
]
result={'schema':'r8-disposition-independent-review.v1','candidate_commit':'d62b41f4d620e50bb04c80a7505374bd284d8210','source_delivery_commit':'4575e80d041ab0c74a42e2e36399d05791dbaa5b','source_formal_commit':'fd1df570cad987dc3852a3b958f03916e317f7fe','formal_tree':'f292698cdd4a8e725525a9be6dc34b75faaf151e','conclusion':'FAIL_FIXED_BASELINE_COARSE_ROUTING','final_remediation_acceptance':'NOT_GRANTED_AWAITING_ACCEPTED_FIXED_BASELINE_AND_REVIEW','configuration_qualification':load(E/'task-qualification.json'),'scope':{'documents':len(documents),'body_lines':sum(d['lines'] for d in documents),'bytes':sum(d['bytes'] for d in documents),'headings':len(sections),'feature_rows':len(rows),'feature_verdict_counts':counts,'unread_documents':0,'roles':dict(roles),'raw_specs_markdown':113,'wp_plan_rows':87,'wp_content_rows':84,'wp_stage_rows':3},'findings_count':len(findings),'findings_by_severity':dict(collections.Counter(x['severity'] for x in findings)),'requirements':checks,'pending':['Author must revise candidate with preserved stable IDs/source facts, then provide a new exact SHA for re-review.','46 reviewed rows may still lack sufficient ownership rationale; use actual feature-results count as authority.','Fix target Showdown commit/generation/format and decide scope; four prototypes remain unrun without blocking a correctly bounded coarse inventory.','Receive coordinator accepted remediation candidate/receipt; backfill current applicability and independently review again.','Cloud task UUID and effective execution configuration lack authoritative echo.'],'reference_game_framework_business_execution':0,'evidence':['reading-coverage.json','feature-results.json','section-results.json','findings.json','evidence/commands.jsonl','evidence/candidate-identities.json','evidence/prescribed-input-identities.json','evidence/extended-validator-negatives.json','evidence/batch-binding-check.json','evidence/isolation-and-scope.json']}
result['pending'][1]=f"{counts.get('待查',0)} reviewed rows still lack sufficient ownership rationale; they are not PASS and are not unread-body gaps."
save('result.json',result)
text=['# 固定候选独立完整复审：FAIL','',f"受审候选 `{result['candidate_commit']}` 的固定基线粗标**不通过，须返修后绑定新 SHA 复核**。全文阅读已覆盖全部131份正式文档；未以标题遍历或结构脚本代替语义阅读。逐项功能结果为 {counts.get('PASS',0)} PASS、{counts.get('FAIL',0)} FAIL、{counts.get('待查',0)} 待查。PASS仅表示本次粗标相应范围可接受；待查行已读，但职责依据不足。当前不授予最终整改验收。",'',
'## 固定输入和任务资格','',
"固定交付 `4575e80d041ab0c74a42e2e36399d05791dbaa5b`，历史正式来源 `fd1df570cad987dc3852a3b958f03916e317f7fe`；来源、交付及候选正式子树均为 `f292698cdd4a8e725525a9be6dc34b75faaf151e`。只读参考提交 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。候选25文件集合、24个非自指文件的bytes/SHA256/blob/mode及manifest本身身份已核对，无差异；完整身份见 [固定输入证据](evidence/candidate-identities.json)。",'',
"用户委派请求为 gpt-6.1-sol / ultra / default。可见本上下文 `/root` 及11个累计审查上下文；真实云任务UUID与平台创建回显未暴露，实际model/effort/tier/speed/Fast逐字段UNVERIFIED。原生工具没有default tier入参且广告为priority，不能据其推造普通档执行资格。各子审仅为同一独立复审的分工，不另计独立验收票；作者原候选没有由本团队改写。[配置资格证据](evidence/task-qualification.json)保留此缺口。",'',
'## 完整覆盖与读取方式','',
'| 口径 | 文档 | 字节 | 正文行 | 标题 |','| --- | ---: | ---: | ---: | ---: |']
for role,v in roles.items():text.append(f"| {role} | {v['documents']} | {v['bytes']} | {v['lines']} | {v['headings']} |")
text += ['',"总计131文档、4,364,108字节、29,956行、2683标题（H1=131/H2=1307/H3=1212/H4=33）；721是候选功能行数，不能代替行为覆盖。原始specs/113份、87WP计划行（84内容+3阶段）另计。文件全集由固定Git树、正式README/测试索引和现行固定索引联合核对；没有硬编码131忽略差异。",'',
"各领域连续分块全文读过正文、表格、历史与限制层，截断区间补读；后继上下文补完kernel和所有未读catalog。每文档实际范围/哈希/归属证据见 [阅读覆盖](reading-coverage.json)，未读文档及正文行均为0。root负责全局协议、schema/577行工具、状态/批次/保护和补充复核；没有冒称root亲自重读所有委派正文。重复生成视图以10文件逐字节重建和721逐行关键字段投影核对，不另算一次全文语义阅读。",'',
"[721项裁定](feature-results.json)保留具体源锚点/行范围、候选JSON pointer/实际行号、生成view行号及每项审查理由；[2683章节导航](section-results.json)保留全部映射及阅读归属。标题结构通过没有被升级为章节分类合理性通过。管理/历史/测试元数据可以关联合适的功能；问题单列出其中吞掉真实行为或制造伪功能的反例。",'',
'## 按严重度列出的问题','',
f"共{len(findings)}组问题，完整可复现源区间、功能ID、候选位置、原因及必要修正在 [findings.json](findings.json) 和各域报告。组内多个ID共享根因；不能把组数当不同新历史根或整改必修分母。",'',
'| ID | 严重度 | 问题 | 详情 |','| --- | --- | --- | --- |']
for f in findings:
    text.append(f"| {f['id']} | {f['severity']} | {f['title'].replace('|','/')} | [{f['review_record_file']}]({f['review_record_file']}) |")
text += ['',
"关键反例已由root额外核实：WP40 §4.2.1 L106–115的退款残留身份仍落FR-000010/Showdown，FR-000011协作范围仅L97–105；§4.2.1实际为同级H3，问题是语义后续消费者遗漏，并非虚构的H4解析错误。WP27 §2.1–2.2 L45–72的缺省/数量显示真实行为、Mining数据附页L9–75的61候选主表却只获泛元数据映射。WP74 §21明确6个必需依赖，清单仅3个。源定位完整和数据一致均不能消除这些语义缺口。",'',
"返修须保留既有stable ID、immutable source和原规格事实。可追加子行/继承或把伪功能保留为历史导航并转元数据关联；不要删旧ID重新seed，也不要修改正式正文来使清单通过。允许章节级粗标以及MZ带框架伙伴处理普通交互提交；本报告不要求逐句/逐向量造ID。纯数值/战斗内部规则可继续保留Showdown候选，未指控Showdown实际不支持；需解决的是具体持久状态/资源/宿主消费者归属及必要依赖。",'',
'## 工具、状态和整改绑定','',
"作者validate、check-generated、assess-current实际exit=0，stdout/stderr/UTC见 [命令日志](evidence/commands.jsonl)。check-generated重建比较10文件无陈旧；隔离运行原CLI self-test/render/check-generated均exit=0，原9负例全拒；seed对已存在清单exit=1拒重建；仅在本review隔离副本追加STALE PROBE后check-generated exit=1拒陈旧view。原工件始终未改。",'',
"扩展14负例3拒绝、11接受；[扩展结果](evidence/extended-validator-negatives.json)与保留脚本可复现。错误当前提交/路径、失真部分身份字段、已知批次删除和未绑定接受事件等结构问题列为必修工具缺口。任意目标证据结构的真实性、分类依据、用户决定及源引用是否等于兼容证据仍须人工审核；没有要求工具自动证明运行行为。",'',
"独立复算确认所有721行去向待验证、阶段待定且未批准、未实现、未验收；排除0。捕获/主动战斗道具/逃跑/战中成长四门均未运行，当前没有固定目标Showdown版本/世代/格式。没有原型本身不阻止合格粗标收尾；遗漏相关调用者、消费关系和具体问题仍是本候选缺陷。",'',
"183行/32文档的整文件保守R8绑定与固定actual_target_write_set一致，保留待整改后核对和空接受事件。此绑定没有声称每个finding都修改每行。U07必修写集仅新导航overlay，正式行不应虚绑；其资格/来源索引后继须单独检查，正式tree不变不能证明U07已校准。[绑定证据](evidence/batch-binding-check.json)、[U07范围](evidence/u07-routing-scope.json)。",'',
"本任务收到整改接受候选/回执0；旧handoff的UPDATE_NOT_STARTED按生成时点保留，不作为协调线程实时状态。修订任务 `01a14a05-405f-7581-9119-73cd53d4a0d2` 返修后须给新40位SHA；协调任务 `01a14a04-b178-7567-a4eb-0f0bfac9a0d9` 提供正式接受固定基线后，还须回填current_applicability、完整受影响差分/消费者/依赖及独立再验收。初版粗标、R8规格整改、实际整合、接受和关闭分别登记。",'',
'## 隔离和交付边界','',
"交付→候选完整差分仅新增25个独立打标文件；正式规格子树未变，历史报告/来源材料不改。只读参考HEAD正确且diff空；远端main在观察时仍为fd1df57。本团队仅在本独占review目录写报告/静态证据；无参考/游戏/Ruby/宿主/Showdown/框架/业务向量执行，无force、删除历史或合并main。",'',
"输出commit由发布回执和父任务转交消息作外部绑定，不在该commit内填未来自指SHA。已发布载荷及完整独立远端字节回读见 [publication-proof.json](publication-proof.json)；该证据只绑定其明确命名的真实提交，包含该证据的最终后继commit再由交接消息绑定。本报告的FAIL不会因推送成功转为通过。后续仍待用户范围决定、目标行为原型、上游正式校准，以及可得的真实云任务/执行配置资格。",'']
labels=['正式全集与章节','固定定位与历史身份','粒度与分类','五类去向及范围决定','协作与行为证据','字段与状态分离','整改绑定及后继校准','工具及生成视图','隔离与保全']
qualifications=['机械全集通过；存在行为漏标/元数据伪功能','仅当前固定身份及seed拒重建；后继续接仍待验','混合职责及独立验收边界未完整表达','枚举/排除0正确；部分特殊范围门缺传播','四门诚实未运行；相关消费者与归属遗漏','状态分栏正确；具体归属/必要依赖/来源分类有缺口','仅基线183行保守绑定；最终校准待办','原校验/生成通过；扩展静态负例暴露缺口','仅本次可观察路径、参考与main保护范围']
idx=text.index('## 按严重度列出的问题')
check_table=['## 复审合同九项裁定','','| 项 | 结果 | 限定理由 |','| --- | --- | --- |']
check_table += [f"| {i+1}. {labels[i]} | {checks[i]['result']} | {qualifications[i]} |" for i in range(9)]
text[idx:idx]=check_table+['']
(OUT/'REPORT.md').write_text('\n'.join(text))
print(json.dumps({'documents':len(documents),'features':len(rows),'headings':len(sections),'verdicts':counts,'findings':len(findings)},ensure_ascii=False))
