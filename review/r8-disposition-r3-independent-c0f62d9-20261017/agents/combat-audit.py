#!/usr/bin/env python3
"""Independent static Git/JSON reconciliation. No author/game code imported."""
import copy, hashlib, json, re, subprocess
from pathlib import Path
from collections import Counter

REPO=Path('/workspace/r8-disposition-r3-review')
OUT=REPO/'review/r8-disposition-r3-independent-c0f62d9-20261017/agents'
BASE='planning/implementation-routing/r8-20261017/'
C='c0f62d973180679134f2eb1a488c1dc359c8658f'
R2='a32873d2860b15d9f5e27727db8f131f4ec433b6'
RP='0ef0b7ad5f9465cfe31da0d7a35f56b5ccba5add'
RB='review/r8-disposition-r2-independent-a32873d-20261017/'
OLD='d62b41f4d620e50bb04c80a7505374bd284d8210'
B8='fd1df570cad987dc3852a3b958f03916e317f7fe'
CUR='5f87743293290de2e219ecdd6c19e88280f60c9a'
R2CUR='908273093e1f6b27fc58249417675dd62d146224'
def git(*args): return subprocess.check_output(['git','-C',str(REPO),*args])
cache={}
def raw(c,p):
    if (c,p) not in cache: cache[c,p]=git('show',c+':'+p)
    return cache[c,p]
def j(c,p): return json.loads(raw(c,p))
def sha(b): return hashlib.sha256(b).hexdigest()
def canonical(o): return sha(json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
def ident(c,p):
    b=raw(c,p)
    return dict(commit=c,path=p,bytes=len(b),sha256=sha(b),git_blob=git('rev-parse',c+':'+p).decode().strip(),lines=len(b.splitlines()))
def union(rs):
    out=[]
    for a,b in sorted(rs):
        if out and a<=out[-1][1]+1: out[-1][1]=max(out[-1][1],b)
        else: out.append([a,b])
    return out
def unit(c,p,ranges):
    ls=raw(c,p).splitlines(keepends=True)
    return b''.join(b''.join(ls[a-1:b]) for a,b in ranges)
def fid(n): return f'FR-{n:06d}'
def write(n,d): (OUT/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')

m=j(C,BASE+'routing-manifest.json'); prev=j(R2,BASE+'routing-manifest.json'); initial=j(OLD,BASE+'routing-manifest.json')
f={x['feature_id']:x for x in m['features']}; pf={x['feature_id']:x for x in prev['features']}; inf={x['feature_id']:x for x in initial['features']}
ret={x['feature_id']:x for x in m['retired_features']}; p_ret={x['feature_id']:x for x in prev['retired_features']}
met={x['metadata_id']:x for x in m['metadata_records']}; pmet={x['metadata_id']:x for x in prev['metadata_records']}
prior=j(RP,RB+'agents/combat-results.json'); graph=j(RP,RB+'agents/combat-dependency-crosscheck.json')
ids={x['feature_id'] for x in prior['active_feature_results']}; oldids={x['feature_id'] for x in prior['old_feature_results']}
docs={x['path'] for x in prior['reading_ledger']}; mids={x['metadata_id'] for x in prior['retired_metadata_results']}
assert (len(ids),len(oldids),len(docs),len(mids))==(134,136,27,11)
prior_active={x['feature_id']:x for x in prior['active_feature_results']}; prior_old={x['feature_id']:x for x in prior['old_feature_results']}
required=['REPORT.md','findings.json','feature-results.json','finding-results.json','issue-results.json','reading-coverage.json','section-results.json','agents/combat-report.md','agents/combat-results.json','agents/combat-dependency-crosscheck.json','agents/combat-author-transform-consistency.json','agents/combat-static-evidence.json']
consumption=[]; parsed={}
for p in required:
    b=raw(RP,RB+p)
    if p.endswith('.json'): parsed[p]=json.loads(b)
    consumption.append(dict(commit=RP,path=RB+p,bytes=len(b),sha256=sha(b),mode='COMPLETE_STRUCTURED_PARSE_AND_RECONCILIATION' if p.endswith('.json') else 'COMPLETE_PROSE_READ'))
rootfeatures=parsed['feature-results.json']
for key in ['old_feature_results','active_feature_results']:
    rr={x['feature_id']:x for x in rootfeatures[key]}
    for x in prior[key]: assert all(rr[x['feature_id']].get(k)==v for k,v in x.items()),(key,x['feature_id'])
for file,key,ownkey,idkey in [('finding-results.json','finding_results','original_group_results','finding_id'),('issue-results.json','issue_results','issue_results','issue_id')]:
    rr={x[idkey]:x for x in parsed[file][key]}
    for x in prior[ownkey]: assert all(rr[x[idkey]].get(k)==v for k,v in x.items()),x[idkey]
rr={x['metadata_id']:x for x in rootfeatures['retired_metadata_results']}
for x in prior['retired_metadata_results']:
    if x['unit_type']=='metadata-record': assert all(rr[x['metadata_id']].get(k)==v for k,v in x.items())
rootreading={x['path']:x for x in parsed['reading-coverage.json']['documents']}
for x in prior['reading_ledger']:
    ri=rootreading[x['path']]['current_identity']
    assert (ri['sha256'],ri['git_blob'],ri['bytes'])==(x['sha256'],x['git_blob'],x['bytes'])
assert len(rootfeatures['old_feature_results'])==721 and len(rootfeatures['active_feature_results'])==736
assert len(parsed['finding-results.json']['finding_results'])==44 and len(parsed['issue-results.json']['issue_results'])==12
assert len(parsed['findings.json']['findings'])==7 and len(parsed['reading-coverage.json']['documents'])==131 and len(parsed['section-results.json']['sections'])==2683

fixed=[C,R2,RP,OLD,B8,CUR,'5666b7b912e2fb79b5119283ee6a37401a7071db','8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8','a0352c7fba38391afc535525988245701d5ce202','4575e80d041ab0c74a42e2e36399d05791dbaa5b','8336249c78b4698cd77445653d3b05ff6a76ce94','a974eb133bdb280ac46f2684df4b309a18fc6cc1','40f428ef33d9b09ba9cc584ef4794779cc9869cb','861f7a44a6f763c265a11761ab17a8ec3b55f304','548d6bb9a21d0967680445c013e66d9d5661d2d6','e042c2f061eb2951a8d662a5987804e3314cb6b4','834888e29f939d0a5ed9478d763deb86eb021211','3157ef455fdac41f0bf5485b281ef2e1699c8599','8f71c18480a847348b8450c9df1e7e8194c03985']
fixed_results=[]
for c in fixed:
    assert git('cat-file','-t',c).strip()==b'commit'
    fixed_results.append(dict(commit=c,type='commit',tree=git('rev-parse',c+'^{tree}').decode().strip()))
assert git('rev-parse',CUR+':deliverables/final-specification-set').decode().strip()=='93dc967b4cdb653359afc123d3b8b318d6475fdd'
assert git('rev-parse',C+':deliverables/final-specification-set').decode().strip()=='f292698cdd4a8e725525a9be6dc34b75faaf151e'

FRESH={fid(n) for n in [1,2,4,5,7,9,11,12,13,17,18,19,20,22,24,29,31,32,58,61,66,67,68,69,71,76,88,89,92,98,99,111,124,126,128,130,135,186,187,204,446,451,456,525,677,683,686,731,733,734,738,739,740,769]}
fresh={}; supplements=[]
for i in sorted(FRESH):
    x=f[i]; a=x['current_applicability']; p=a['document']; ranges=a['locator']['line_ranges']
    fresh.setdefault(p,[]).extend(ranges)
    supplements.append(dict(feature_id=i,identity=ident(CUR,p),line_ranges=ranges,unit_sha256=sha(unit(CUR,p,ranges)),mode='FRESH_COMPLETE_EFFECTIVE_UNIT_SEMANTIC_READ'))
for mid in ['META-000003','META-000004','META-000005','META-000006','META-000007','META-000010','META-000033']:
    x=met[mid]; fresh.setdefault(x['source']['document'],[]).extend(x['source']['line_ranges'])
fresh.setdefault('deliverables/final-specification-set/test-catalog/combat-requirements-wp39-40-41-42-45.md',[]).extend([[299,317]])
fresh.setdefault('deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md',[]).extend([[116,195],[351,363]])
fresh.setdefault('deliverables/final-specification-set/demo-dx/wp76-facility-content-generation-and-simulation.md',[]).append([164,170])

changed_docs=[p for p in sorted(docs) if raw(B8,p)!=raw(CUR,p)]
assert len(changed_docs)==8
delta=j(C,BASE+'revisions/r3/feature-source-deltas.json')
direct_changed={x['feature_id'] for x in delta['records'] if x['feature_id'] in ids}
assert direct_changed=={fid(n) for n in [1,2,5,7,12,13,17,24,29,32,92,135]}
locator_checks=[]
for i in sorted(ids):
    x=f[i]; a=x['current_applicability']; p=a['document']; loc=a['locator']; b=raw(CUR,p); ranges=loc['line_ranges']; h=ident(CUR,p)
    assert a['snapshot_commit']==CUR
    assert sha(unit(CUR,p,ranges))==loc['unit_sha256'],i
    assert h['sha256']==loc['file_sha256'] and h['git_blob']==loc['file_git_blob'],i
    assert x['source']==pf[i]['source'],i
    locator_checks.append(dict(feature_id=i,verdict='PASS',current_locator=loc,current_commit=CUR,immutable_source_preserved=True))

old_edges={(x['source_feature_id'],x['target_feature_id']):x for x in graph['edge_results']}
edges={(i,t) for i in ids for t in f[i]['dependencies']['feature_refs']}
removed=set(old_edges)-edges; added=edges-set(old_edges)
assert removed=={(fid(n),fid(739)) for n in [61,66,69]}
assert added=={(fid(92),fid(76))}
assert len(edges)==96
edge_results=[]
for s,t in sorted(edges):
    sx,tx=f[s],f[t]; psx,ptx=pf[s],pf[t]
    s_same=sx['current_applicability']['locator']['unit_sha256']==psx['current_applicability']['locator']['unit_sha256']
    t_same=tx['current_applicability']['locator']['unit_sha256']==ptx['current_applicability']['locator']['unit_sha256']
    oldedge=old_edges.get((s,t)); changed=(not s_same or not t_same)
    assert not changed or s in FRESH and t in FRESH,(s,t)
    reason=oldedge['reason'] if oldedge else 'FR92的直调贡献与普通User/0不消费路径均由FR76的逐槽、目标数、共享准备与评分后原槽登记协调；不增设默认消费。'
    if t==fid(29): impact='WP42新增EV负余量先失败界限；初始化/写穿关系仍真实，不能由输入存在推出成长成功或完整刷新。'
    elif t==fid(32): impact='WP42末端改为行走动画/转向预锁记录复位，未改决定3之后外层善后、统计及包装返回的消费者关系。'
    elif t==fid(13): impact='排序现在明确配置最大席位范围，与Palace自动登记后的通常排序共用；不是把所有实际对象自动加入队列。'
    elif t==fid(135): impact='WP58仅澄清debug辅助随机与AI主路径；Palace不记录AI随机、回放序列消费及不足边界保持。'
    elif t==fid(446): impact='新增有序删档导航不改变正常安全保存的IO假/未捕获异常层次，设施真实调用仍落5.1。'
    elif t==fid(451): impact='新增删档前缀与下一次主档门属于已有恢复层对照，不给设施保存补造自动恢复或迁移调用。'
    elif t==fid(677): impact='混合野生及debug辅助扩展不改变回放命令循环覆写/中止决定0的真实消费；全部有效目标范围已重读。'
    elif t==fid(683): impact='新增倒下音频排期/动画回退不改捕获ME3.5秒、消息等待与BACK中止；不是音频请求证明实际发声。'
    elif s==fid(92): impact='新增依赖仅连接既有候选/目标数调度；原始类型候选无PP门、计算类型匹配仅PP门、一次+14和普通User0不消费逐项保留。'
    else: impact='源/目标有效正文精确相等；R2逐边真实用途仍成立。累计改动只影响此二单元之外的创建/EV/纹理/恢复/UI细化，未改变本边具名字段、资格、提交或排除对照。目标依赖的更正不替代本边的直接用途。'
    edge_results.append(dict(source_feature_id=s,target_feature_id=t,r2_verdict=oldedge['verdict'] if oldedge else 'NEW',verdict='PASS',reason=reason,nonimpact_or_current_reassessment=impact,method='FRESH_COMPLETE_SOURCE_TARGET_EFFECTIVE_UNITS' if changed or s in {fid(n) for n in [61,66,68,69,71]} else 'IDENTITY_BOUND_R2_EDGE_SEMANTIC_CREDIT_WITH_EXPLICIT_NONIMPACT',source_unit_equal_r2=s_same,target_unit_equal_r2=t_same,source_record_equal_r2=sx==psx,target_record_equal_r2=tx==ptx,source_current_identity=dict(commit=CUR,document=sx['current_applicability']['document'],locator=sx['current_applicability']['locator']),target_current_identity=dict(commit=CUR,document=tx['current_applicability']['document'],locator=tx['current_applicability']['locator']),r2_evidence=RB+'agents/combat-dependency-crosscheck.json'))

semantic={
1:'已有个体输入复用、不预治疗/过滤；缺失计数和更早skip/前缀分开，框架持久输入与战斗创建候选职责成立。',
2:'配置人数、实际对象、存活集、priority与UI遍历分开；零计数缺失先失败与正计数原序异常均由当前范围承担，不新增承载方。',
5:'善后复位行走动画，不保证转向；领域善后与MZ音频子733职责仍分开。',
7:'不统一承诺缩零错误；缺失计数/原序首失败、前序写入与未到清理均留在现行失败合同。',
12:'火药火招失败与自损门分开，有效雨/大雨及间伤资格由规则查询；不重定向持久HP责任。',
13:'全量只扫描配置上限，增量不插入实际Q；STALL/QUICKDRAW与排序规则仍为战斗侧候选，输入配置由框架。',
17:'配置世代对照明确王者盾牌，未新增实际功能或用户阶段决定。',
24:'可选重算换人席位在完整速度序入场之前，仍有召回/绑定/派出/入场边界，无统一回滚。',
29:'EV255首项负上界失败早于此接收者EV/EXP及清参与记录；非内部早门与已处理成员前缀保留。成长/PP回读、逐级UI及真实持久提交仍协作。',
32:'世界正常核心返回尾部复位行走动画/转向预锁记录；未变进化/拾取/结果统计责任，不保证改朝向。',
92:'直调原始类型发现不查PP、计算类型伤害匹配只过滤有限PP0、仅一次+14；普通User/0不消费贡献且不推总分100。框架策略与战斗查询分责充分，92→76真实。',
135:'记录随机入口与AI/无视觉debug辅助全局随机分开；直接helper访问失败不推出真实AI模拟失败，不扩成跨版本回放保证。',
61:'移去无用途739；4初始化、31正常终局、740持物写穿/可更新还原记录有真实用途。',
66:'离场HP0/真正濒死/状态治疗及气体/紧张感链不消费PP；739移除，740吃果接点保留。',
69:'回合末天气HP/治疗/阶级/取物不消费PP；739移除，740对C/I/R/P与野生转移仍真实。'
}
for n in [76,88,89,98,99,111]: semantic[n]='完整重读共享准备源与候选责任：框架拥有策略/逐目标对象重建及顺序，战斗侧候选拥有具名准备写入/正常清理；NaturalGift/BeatUp等异常前缀不保证统一回滚。'
for n in [67,769]: semantic[n]='父67精确扣除L106，769独占L106；野生人数/可逃/决定3、训练家等待/负选择与回合末只召回的粗责任及20/22/31/32/734真实。'
active=[]
for i in sorted(ids):
    x=f[i]; p=pf[i]; oldr=prior_active[i]; n=int(i.split('-')[1]); same=x['current_applicability']['locator']['unit_sha256']==p['current_applicability']['locator']['unit_sha256']
    why=semantic.get(n,('本行完整有效源新读；' if i in FRESH else '本行未变有效源保留固定R2限定语义信用；')+oldr['reason'])
    outgoing=[e for e in edge_results if e['source_feature_id']==i]
    changedfields=[k for k in x if x[k]!=p.get(k)]
    active.append(dict(feature_id=i,r2_verdict=oldr['verdict'],verdict='PASS',current_state='active',candidate_pointer='/features/'+str(m['features'].index(x)),reason=why,method='FRESH_AFFECTED_EFFECTIVE_UNIT_REASSESSMENT' if i in FRESH else 'IDENTITY_BOUND_R2_UNAFFECTED_FACET_CREDIT_AFTER_CUMULATIVE_DIFF_AND_EDGE_NONIMPACT',classification_facet_verdict='PASS',responsibility_facet_verdict='PASS',scope_facet_verdict='PASS',dependency_facet_verdict='PASS',current_calibration_facet_verdict='PASS_SOURCE_TO_ROUTING_ONLY',facets=dict(classification='PASS',responsibility='PASS',scope='PASS',dependency='PASS',current_calibration='PASS_SOURCE_TO_ROUTING_ONLY'),identity=dict(immutable_source=x['source'],r2_record_sha256=canonical(p),candidate_record_sha256=canonical(x),effective_unit_equal_r2=same,changed_top_fields=changedfields,current_snapshot=CUR,current_locator=x['current_applicability']['locator']),inheritance=dict(r2_evidence=RP+':'+RB+'agents/combat-results.json#/active_feature_results/'+str(prior['active_feature_results'].index(oldr)),retained_credit='R2原分类/责任/scope判断仅在未改变或新读证实的facet保留；R2 FAIL不自动继承。',affected_source_evidence='combat-results.json#/changed_source_results' if i in direct_changed else None,outgoing_edge_count=len(outgoing),outgoing_edge_reassessment='combat-dependency-crosscheck.json',nonimpact='累计8文件完整diff与本行有效单元身份核对；同源其它条款变化不自动扩大此scope。所有新/变目标边已完整新读，未变边有逐边真实用途。'),future_destination=x['future_plan']['destination'],destination_verification=x['destination_verification'],implementation=x['implementation'],phase=dict(stage=x['future_plan']['stage'],approval=x['future_plan']['stage_approval']),finding_refs=[]))

oldresults=[]
for i in sorted(oldids):
    x=f.get(i,ret.get(i)); assert x['source']==inf[i]['source']
    oldresults.append(dict(feature_id=i,r2_verdict=prior_old[i]['verdict'],verdict='PASS',current_state='active' if i in f else 'retired',disposition='active' if i in f else 'retired',reason=(next(a['reason'] for a in active if a['feature_id']==i) if i in f else '完整d62原对象去retirement后逐字段相等，退役ID未复用；metadata及真实消费者导航保持。'),method='PER_ID_CURRENT_FACETS_OR_COMPLETE_ORIGINAL_HISTORY_RECONCILIATION',immutable_source_preserved=True,source=inf[i]['source'],finding_refs=[]))

metresults=[]
for mid in sorted(mids):
    x=met[mid]; assert x==pmet[mid]
    histories=[]
    for i in x['retired_feature_ids']:
        r=copy.deepcopy(ret[i]); retirement=r.pop('retirement'); assert r==inf[i] and ret[i]==p_ret[i]
        assert retirement['metadata_record_id']==mid and set(retirement['replacement_feature_refs'])==set(x['feature_refs'])
        histories.append(dict(feature_id=i,complete_d62_body_preserved=True,original_body_sha256=canonical(inf[i]),archived_body_sha256=canonical(r),original_source=inf[i]['source'],retirement=retirement))
    changedtargets=[i for i in x['feature_refs'] if f[i]['current_applicability']['locator']['unit_sha256']!=pf[i]['current_applicability']['locator']['unit_sha256']]
    assert all(i in FRESH for i in changedtargets)
    metresults.append(dict(unit_type='retired-metadata-combined',metadata_id=mid,r2_verdict='PASS',verdict='PASS',retired_old_ids=x['retired_feature_ids'],retired_feature_ids=x['retired_feature_ids'],source=x['source'],complete_history_proofs=histories,consumer_refs=x['feature_refs'],changed_consumer_units=changedtargets,consumer_navigation_verdict='PASS',reason='源索引为历史责任/共享目录，不计实现；完整metadata及退休replacement原对象相等，真实消费者按章节聚合或显式父→excluded_child_refs→子可达。'+('改变消费者正文已完整新读：'+','.join(changedtargets)+'，仍承担同一历史组的实际行为。' if changedtargets else '消费者有效正文未变；61的错误PP出站删除不改变持物主合同作为本索引消费者。'),method='COMPLETE_ORIGINAL_HISTORY_IDENTITY_PLUS_CURRENT_CONSUMER_NONIMPACT',finding_refs=[]))

groups=[]
for g in prior['original_group_results']:
    out=copy.deepcopy(g);out['r2_verdict']=g['verdict'];out['r2_current_scope_verdict']=g.get('current_scope_verdict');out['verdict']='PASS';out['current_scope_verdict']='PASS';out['original_case_verdict']='PASS';out['method']='ALL_ORIGINAL_CASES_RECONCILED_WITH_R2_PLUS_AFFECTED_CURRENT_SOURCE_AND96_EDGES'
    for case in out['original_cases']:
        case['r2_case_verdict']=case['verdict'];case['verdict']='PASS';case['current_overall_feature_verdict']='PASS';case['r3_nonimpact']='保留原case修正facet；12当前变源、六AI、67/769、11metadata及全部96出站边另行新审；COMBAT05当前PP错边已修复。'
    for case in out['propagation_cases']:
        case['r2_verdict']=case['verdict']
        if case.get('feature_id') in {fid(61),fid(66),fid(69)}:
            case['r2_reason']=case['reason'];case['verdict']='PASS';case['reason']=semantic[int(case['feature_id'].split('-')[1])];case['finding_refs']=[]
    out['r3_scope_reason']='原case与当前扩大scope均逐项复核；COMBAT-R2-DEP-001已修，正向68/71 PP对照未删，当前源累计细化不改变本组已接受粗标边界。'
    groups.append(out)
issues=[]
for issue in prior['issue_results']:
    x=copy.deepcopy(issue);x['r2_verdict']=issue['verdict'];x['verdict']='PASS';x['r3_reassessment']='固定5f完整有效源重读；原scope/共享准备/历史索引与现行责任相合，逐case保留独立限定PASS。';issues.append(x)
issues.append(dict(issue_id='COMBAT-R2-DEP-001',finding_id='COMBAT-R2-DEP-001',r2_verdict='FAIL',verdict='PASS',severity='P3',cases=[dict(feature_id=fid(n),r2_verdict='FAIL',verdict='PASS',removed_target=fid(739),retained_targets=f[fid(n)]['dependencies']['feature_refs'],source=f[fid(n)]['current_applicability'],reason=semantic[n]) for n in [61,66,69]],positive_controls=[dict(feature_id=fid(n),verdict='PASS',retained_target=fid(739),reason='当前槽PP资格/已扣PP前缀' if n==68 else 'DANCER原槽PP不消费及IMPOSTER场上PP/总PP5') for n in [68,71]],same_root_propagation=dict(all_outgoing_edges=96,all_sources=25,all_targets=53,additional_failure=0),qualification='目标739不因入站误用被判FAIL；740与真实世界/终局边未盲删。'))

reading=[]
for p in sorted(docs):
    oldledger=next(x for x in prior['reading_ledger'] if x['path']==p); b=ident(B8,p);r2i=ident(R2CUR,p);cur=ident(CUR,p)
    assert b['sha256']==oldledger['sha256'] and r2i['sha256']==oldledger['sha256']
    reading.append(dict(path=p,historical_identity=b,r2_identity=r2i,current_identity=cur,candidate_formal_identity=ident(C,p),fresh_source_commit=CUR,fresh_ranges=union(fresh.get(p,[])),complete_cumulative_diff_read=p in changed_docs,complete_diff_sha256=sha(git('diff',B8,CUR,'--',p)) if p in changed_docs else None,prior_full_semantic_credit=dict(report_commit=RP,record=RB+'agents/combat-results.json#/reading_ledger/'+str(prior['reading_ledger'].index(oldledger)),r2_ledger=oldledger),method='CURRENT_COMPLETE_CHANGED_UNITS_AND_IDENTITY_BOUND_UNCHANGED_UNITS' if p in changed_docs else 'IDENTITY_BOUND_PRIOR_FULL_READ_PLUS_LISTED_FRESH_UNITS',inheritance_limits='仅未改变有效单元/未受新消费者边界影响的facet继承；完整diff、JSON/标题枚举不算本轮全文。所有listed fresh ranges实际从fixed5f读。',verdict='PASS'))

headings=[]
for x in j(C,BASE+'revisions/r3/new-heading-mappings.json')['accepted_mappings']:
    if x['document'] not in docs:continue
    p=x['document'];si=x['source_identity'];ls=raw(CUR,p).splitlines(keepends=True);a,b=x['line_ranges'][0]
    assert sha(unit(CUR,p,x['line_ranges']))==si['unit_sha256'];assert sha(raw(CUR,p))==si['file_sha256']
    assert sha(x['title'].encode())==si['heading_sha256'];assert sha(ls[a-1])==si['raw_markdown_heading_sha256']
    reason=('零计数首失败、配置/实际/存活/priority/UI集合差均为2/7/9/13及677/686的现有责任，不新增承载边界。' if 'wp39-' in p else 'Z/M输入的同一现有入口/命令/排序消费者，加EV模板456、分配204与成长29；静态NOT_EXECUTED，无普通设施成长失败泛化。' if 'wp39-40' in p else '现存纹理直调查询由92承载，候选普通User0调度由76承载；T02与CV共同保留不消费、不推总分100，静态NOT_EXECUTED。')
    headings.append(dict(document=p,anchor=x['anchor'],title=x['title'],level=x['heading_level'],line_ranges=x['line_ranges'],current_identity=si,heading_title_hash_verdict='PASS',raw_heading_hash_verdict='PASS',feature_refs=x['feature_refs'],metadata_refs=x['metadata_refs'],consumer_results=[dict(feature_id=i,verdict='PASS_NAVIGATION_AND_BEHAVIOR_RESPONSIBILITY',current_locator=f[i]['current_applicability']['locator'],source_commit=CUR,fresh_complete_effective_unit_read=i in FRESH,qualification='FR29的EV概括注记另有R3-EV-BOUNDARY-001；该错字不否定此heading映射到真实成长消费者。' if i==fid(29) else '本新增heading与现有消费者的输入/调度/结果责任相符。') for i in x['feature_refs']],r2_verdict='PREPARED_PROPOSAL_NOT_CURRENT',verdict='PASS',reason=reason,current_calibration_verdict='PASS_HEADING_TO_CONSUMER_MAPPING',method='FRESH_FULL_NEW_HEADING_BODY_AND_ALL_AFFECTED_CONSUMER_UNITS',finding_refs=[]))
assert len(headings)==3

clauses=[
('wp39-battle-context-and-participants.md',[[96,96]],[1,2],'已有对象不先治疗/过滤；零计数和原序边界分别交现有初始化。'),
('wp39-battle-context-and-participants.md',[[109,113]],[1],'skip消息与结果差异保留，不把返回真当战胜。'),
('wp39-battle-context-and-participants.md',[[165,181]],[2,7,9,13,677,686],'野生同步可增配置，缺失计数不能转0；实际Q可被命令登记而不在priority，不推自动胜利或UI成功。'),
('wp39-battle-context-and-participants.md',[[271,271]],[5,32],'善后只复位行走动画；未保留错误转向保证。'),
('wp39-battle-context-and-participants.md',[[314,314]],[7,2],'缺失计数/原序的更早异常与缩零消息分开。'),
('wp40-commands-obedience-and-action-order.md',[[167,167]],[12],'火药先失败，自损另受有效雨/大雨和可间伤门；战斗临时查询与持久HP提交分责。'),
('wp40-commands-obedience-and-action-order.md',[[255,259]],[13,2,9],'配置范围与实际集合分开，增量不插入；STALL/QUICKDRAW字面身份校准不新增功能。'),
('wp40-commands-obedience-and-action-order.md',[[337,337]],[17],'世代配置对应王者盾牌，分类与职责仍充分。'),
('wp41-switching-positioning-and-escape.md',[[201,201]],[24,19,20,58],'配置重算该换人席位在完整速度序入场之前，不把所有换人入口写成同一资格。'),
('wp42-growth-end-of-round-and-battle-outcomes.md',[[73,73]],[29,204,456],'普通EV负余量首失败及非内部早门保留，持久接收者无新提交与早先前缀不回滚分开。'),
('wp42-growth-end-of-round-and-battle-outcomes.md',[[207,207]],[32,5],'行走动画和转向预锁记录复位，不保证玩家朝向恢复。'),
('wp52-a-generic-numerical-and-status-evaluation.md',[[215,215]],[92,76],'普通User0不进入目标贡献，不推完整候选100。'),
('wp52-a-generic-numerical-and-status-evaluation.md',[[217,221]],[92,76],'原始候选发现无PP门，计算类型伤害匹配仅PP门，首次匹配+14一次；直接查询不新增默认接线。'),
('wp52-a-generic-numerical-and-status-evaluation.md',[[225,225]],[92],'20直接登记+5复制目标为25身份计数，保留固定表/未知0，不改策略算法。'),
('wp58-battle-recording-and-playback.md',[[105,105]],[135,128,130,738],'debug helper随机不入记录，与真实AI控制路径分开；不承诺直接helper成功或整体模拟失败。'),
('combat-requirements-wp39-40-41-42-45.md',[[299,317]],[2,7,9,13,456,204,29],'Z/M/EV为独立静态向量，源集合/首失败/余量门和现有消费者完整对应，无引擎运行信用。'),
('combat-requirements-wp49-51-52.md',[[170,170]],[92,76],'T02从未来未知算法改为现有有限直调贡献，普通User0路径不改接。'),
('combat-requirements-wp49-51-52.md',[[351,363]],[92,76],'CV01–05覆盖候选/PP/原始与计算类型/一次加分和非消费对照，全部NOT_EXECUTED。')]
changes=[]
for name,ranges,cons,reason in clauses:
    p=next(p for p in docs if p.endswith('/'+name)); changes.append(dict(document=p,current_commit=CUR,current_effective_ranges=ranges,current_clause_sha256=sha(unit(CUR,p,ranges)),consumer_refs=[fid(n) for n in cons],verdict='PASS',classification_facet_verdict='PASS',responsibility_facet_verdict='PASS',scope_facet_verdict='PASS',dependency_facet_verdict='PASS',current_calibration_facet_verdict='PASS_SOURCE_TO_ROUTING_ONLY',reason=reason,method='COMPLETE_CUMULATIVE_DIFF_PLUS_FRESH_EFFECTIVE_UNIT_AND_CONSUMER_READ',finding_refs=[]))

histcov=j(C,BASE+'section-coverage.json'); curcov=j(C,BASE+'current-section-coverage.json')
domain_hist=[x for x in histcov['sections'] if x['path'] in docs];domain_cur=[x for x in curcov['sections'] if x['path'] in docs]
assert len(domain_cur)==len(domain_hist)+3
catalog_prior=prior['catalog_consumer_results']; catresults=[]
for x in catalog_prior:
    y=copy.deepcopy(x); y['r2_verdict']=x.get('verdict','PASS');y['verdict']='PASS';y['r3_reassessment']='旧目录章节按相同身份/未改消费者用途保留；AE T02与新增Z/M/EV、CV按完整当前源章及现有消费者新审。';catresults.append(y)

write('combat-dependency-crosscheck.json',dict(schema='r8-combat-r3-full-dependency-crosscheck.v1',candidate_commit=C,current_snapshot=CUR,r2_candidate_commit=R2,r2_report_commit=RP,counts=dict(source_features=25,outbound_edges=96,distinct_targets=53,pass_edges=96,fail_edges=0,removed_wrong_edges=3,new_true_edges=1),edge_results=edge_results,removed_edge_results=[dict(source_feature_id=s,target_feature_id=t,r2_verdict='FAIL',verdict='PASS_REMOVAL',reason=semantic[int(s.split('-')[1])]) for s,t in sorted(removed)],reading_ledger=supplements))
results=dict(schema='r8-disposition-r3-combat-independent.v1',candidate_commit=C,r2_candidate_commit=R2,r2_report_commit=RP,current_snapshot=CUR,conclusion='PASS_SCOPED_SEMANTIC_ROUTING_AND_CURRENT_CALIBRATION',configuration={k:'UNVERIFIED' for k in ['actual_model','actual_effort','actual_service_tier','actual_speed','actual_Fast','cloud_task_UUID']},counts=dict(primary_body_documents=23,primary_catalog_documents=4,primary_documents=27,old_ids=136,old_verdicts=dict(PASS=136,FAIL=0),active=134,active_verdicts=dict(PASS=134,FAIL=0),retired=11,metadata=11,original_groups=9,r1_residual_issues=3,r2_issues=1,changed_documents=8,direct_changed_effective_units=12,changed_clause_results=len(changes),new_headings=3,historical_domain_sections=len(domain_hist),current_domain_sections=len(domain_cur),catalog_original_sections=len(catresults),dependency_edges=96),old_feature_results=oldresults,active_feature_results=active,retired_metadata_results=metresults,issue_results=issues,original_group_results=groups,reading_ledger=reading,new_heading_results=headings,changed_source_results=changes,changed_active_unit_results=[dict(feature_id=i,verdict='PASS',current_source=f[i]['current_applicability'],reason=semantic[int(i.split('-')[1])]) for i in sorted(direct_changed)],catalog_consumer_results=catresults,dependency_crosscheck='combat-dependency-crosscheck.json',supplemental_reading_ledger=supplements,input_consumption_ledger=consumption,fixed_objects=fixed_results,structural_checks=dict(root_domain_rows_exactly_reconciled=True,root_44group_domain9_exactly_reconciled=True,root_12residual_domain3_exactly_reconciled=True,all134_current_locators_recomputed=True,all136_original_source_objects_preserved=True,all11_complete_retired_bodies_equal_d62=True,all11_metadata_and_replacement_navigation_preserved=True,historical_coverage_bytes_equal_r2=raw(C,BASE+'section-coverage.json')==raw(R2,BASE+'section-coverage.json'),shared_ai_contract_bytes_equal_r2=raw(C,BASE+'revisions/r2/shared-ai-preparation.json')==raw(R2,BASE+'revisions/r2/shared-ai-preparation.json')),shared_ai_contract=j(C,BASE+'revisions/r2/shared-ai-preparation.json'),new_findings=[],limits=['仅固定candidate和final5f的静态粗标/责任/范围/依赖/来源校准；不是目标兼容、行为已实现、验收完成、用户范围或阶段批准。','全部四协作原型未运行，目标Showdown版本/格式未固定；未因这些待办否决合理粗标。','9接受事件/39来源事项/230绑定和来源门工具的全局资格由root/source owner核；本域不把作者ACCEPTED标签当独立目标兼容证明。','只有列出的fresh ranges及八完整diff是本轮新读；其余按固定R2与早期全文记录的精确身份及逐facet非影响继承，不声称27全文新读。','没有Ruby、参考游戏、业务/宿主/Showdown/框架执行；未执行作者业务代码，未修改作者/正式/reference/旧报告，未提交。'])
finding=dict(finding_id='R3-EV-BOUNDARY-001',severity='P3',verdict='FAIL',title='当前EV校准摘要把单项越额错误概括为总量越额先在单项门失败',domain_cases=[fid(29),fid(32)],same_root_parent_merge='root合并world FR456；本域仅承担29/32，不计额外接受票。',failed_facet='current_calibration_only',preserved_facets=['classification','responsibility','scope','dependency'],candidate_commit=C,candidate_path=BASE+'routing-manifest.json',candidate_pointers=['/features/28/differences/1','/features/31/differences/1'],other_candidate_pointers=[dict(path=BASE+'revisions/r3/feature-source-deltas.json',pointer='/records/8/source_fact_delta'),dict(path=BASE+'revisions/r3/feature-source-deltas.json',pointer='/records/9/source_fact_delta'),dict(path=BASE+'revisions/r3/source-file-reassessment.json',pointer='/records/3/source_fact_reassessment')],source_evidence=[dict(commit=CUR,document=f[fid(29)]['current_applicability']['document'],line_ranges=[[59,96]],exact_decisive_ranges=[[73,73]],fact='最终WP42只把HP EV255普通模板的首项反向区间失败与原有EV/经验分配、内部成长门对齐。'),dict(commit=CUR,document=f[fid(456)]['current_applicability']['document'],line_ranges=[[162,180]],exact_decisive_ranges=[[174,180]],fact='HP255/ATK255合计510等于总上限；HP先处理且单项252−255=−3，首项失败，非总量超限。'),dict(commit=CUR,document=f[fid(204)]['current_applicability']['document'],line_ranges=[[116,123]],fact='普通分配先查单项余量，再查总量余量；已有越额不自动修复。')],candidate_claim='超总量EV受领者先在单项负上界夹取失败',distinguishing_counterexamples=[dict(input='固定正常模板HP255/ATK255，其余0',static_arithmetic='255+255=510，不大于总上限510；HP单项255>252。',result='HP单项上界−3先失败；支持源事实，却不能称超总量。'),dict(input='独立普通非Shadow分配输入HP/ATK/DEF/SPA/SPD各100、SPE20，无物品/病毒等副作用，首先处理HP',static_arithmetic='总量520>510，各项≤252；HP单项余量252−100=152非负，总余量510−520=−10。',result='单项门不因总量越额失败；随后总量门才非法，故候选概括的首失败归因不成立。')],minimum_fix='只修上述当前来源摘要与同步叙述：明确“HP EV255等单项越额模板在HP首项反向区间失败”；若保留总量越额泛称，按实际第一个非法余量门分开，不宣称必先单项。保留源正文、去向类别、职责、范围、依赖、未验证与未批准状态。',qualification='源正文接受与行为合同未失败；该finding只否定源到routing注记的校准精度。未运行业务向量。')
for a in results['active_feature_results']:
    if a['feature_id'] in {fid(29),fid(32)}:
        a['verdict']='FAIL';a['current_calibration_facet_verdict']='FAIL';a['facets']['current_calibration']='FAIL';a['finding_refs']=[finding['finding_id']]
        a['reason']+=' 但differences[1]的“超总量EV先单项失败”把单项与总量额度混同；当前校准facet FAIL，详见R3-EV-BOUNDARY-001。'
for a in results['old_feature_results']:
    if a['feature_id'] in {fid(29),fid(32)}:
        a['verdict']='FAIL';a['finding_refs']=[finding['finding_id']];a['reason']+=' 当前源摘要的单项/总量越额概括错误，只有current-calibration facet失败。'
for g in results['original_group_results']:
    if g['finding_id']=='COMBAT-05':
        g['verdict']='FAIL';g['current_scope_verdict']='FAIL';g['original_case_verdict']='PASS';g['finding_refs']=[finding['finding_id']]
        g['r3_scope_reason']='原6case依赖修正和COMBAT-R2-DEP-001已修PASS；扩大当前scope中29的来源摘要精度因R3-EV-BOUNDARY-001 FAIL，不重开原修正facet。'
    for case in g['original_cases']:
        if case['feature_id'] in {fid(29),fid(32)}:case['current_overall_feature_verdict']='FAIL';case['original_case_verdict']='PASS';case['finding_refs']=[finding['finding_id']]
for a in results['changed_active_unit_results']:
    if a['feature_id'] in {fid(29),fid(32)}:a['verdict']='FAIL_CURRENT_CALIBRATION_ONLY';a['finding_refs']=[finding['finding_id']]
for a in results['changed_source_results']:
    a['source_fact_verdict']='PASS'
    if a['document'].endswith('wp42-growth-end-of-round-and-battle-outcomes.md'):
        a['verdict']='FAIL_CURRENT_CALIBRATION_ONLY';a['current_calibration_facet_verdict']='FAIL';a['finding_refs']=[finding['finding_id']];a['reason']+=' 实际源事实正确；对应29/32的source_delta/differences“超总量先单项失败”叙述错误，须修注记。'
results['new_findings']=[finding]
results['conclusion']='FAIL_CURRENT_CALIBRATION_ONLY_WITH_ROUTING_REPAIRS_PRESERVED'
results['counts']['old_verdicts']=dict(PASS=134,FAIL=2)
results['counts']['active_verdicts']=dict(PASS=132,FAIL=2)
results['counts']['classification_facet_verdicts']=dict(PASS=134,FAIL=0)
results['counts']['responsibility_facet_verdicts']=dict(PASS=134,FAIL=0)
results['counts']['scope_facet_verdicts']=dict(PASS=134,FAIL=0)
results['counts']['dependency_facet_verdicts']=dict(PASS=134,FAIL=0)
results['counts']['current_calibration_facet_verdicts']=dict(PASS=132,FAIL=2)
results['extra_consumer_reading_ledger']=[dict(path=p,current_identity=ident(CUR,p),fresh_source_commit=CUR,fresh_ranges=union(rs),method='FRESH_COMPLETE_LISTED_CURRENT_CONSUMER_UNITS',qualification='Extra consumer evidence; not counted again among27 primary documents.') for p,rs in sorted(fresh.items()) if p not in docs]
write('combat-results.json',results)
write('combat-findings.json',dict(candidate_commit=C,current_snapshot=CUR,findings=[finding],count=1,qualification='R3-EV-BOUNDARY-001与world456由root合并；本域仅29/32，单一独立review分工。'))
write('combat-static-evidence.json',dict(candidate_commit=C,command='python agents/combat-audit.py (static Git/JSON only)',status='PASS',counts=results['counts'],input_consumption=consumption,locator_checks=locator_checks,changed_document_diffs=[dict(path=p,bytes=len(git('diff',B8,CUR,'--',p)),sha256=sha(git('diff',B8,CUR,'--',p)),complete_semantic_diff_read=True) for p in changed_docs],root_reconciliation_counts=dict(old=721,active=736,metadata=33,groups=44,residuals=12,findings=7,reading=131,historical_sections=2683),configuration=results['configuration']))
write('combat-audit-run-history.json',dict(candidate_commit=C,qualification='Review script executions only; no author or business code. Static assertion PASS is separate from semantic review FAIL.',runs=[dict(run='initial',argv=['python','review/r8-disposition-r3-independent-c0f62d9-20261017/agents/combat-audit.py'],exit_code=1,stdout='',stderr='AssertionError at complete-history navigation comparison: retirement replacement_feature_refs list order differed from metadata feature_refs for META-000005/META-000007.',cause='Reviewer incorrectly required ordering equality for navigation reference sets; complete candidate and historical records were unchanged.',correction='Compare same consumer set while separately asserting each exact candidate record is preserved; no author/candidate edits.'),dict(run='final_static_assertions',argv=['python','review/r8-disposition-r3-independent-c0f62d9-20261017/agents/combat-audit.py'],exit_code=0,stdout=results['counts'],stderr='',utc='UNRECORDED_BY_PER_COMMAND_CAPTURE',semantic_conclusion=results['conclusion'])]))
print(json.dumps(results['counts'],ensure_ascii=False))
