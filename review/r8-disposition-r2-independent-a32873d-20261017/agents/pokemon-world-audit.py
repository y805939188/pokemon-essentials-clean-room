"""Independent static Git/document audit. Does not import or execute author code."""
import collections
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path

C = 'a32873d2860b15d9f5e27727db8f131f4ec433b6'
R1 = '5666b7b912e2fb79b5119283ee6a37401a7071db'
RR = '8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8'
OLD = 'd62b41f4d620e50bb04c80a7505374bd284d8210'
OR = 'a0352c7fba38391afc535525988245701d5ce202'
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
CUR = '908273093e1f6b27fc58249417675dd62d146224'
B = 'planning/implementation-routing/r8-20261017/'
RP = 'review/r8-disposition-r1-independent-5666b7b-20261017/'
OP = 'review/r8-disposition-independent-d62b41f-20261017/'
OUT = Path(__file__).parent
PREFIX = 'pokemon-world-'
sha = lambda b: hashlib.sha256(b).hexdigest()
def git(c, p):
    return subprocess.check_output(['git', 'show', c + ':' + p])
def read(c, p):
    return json.loads(git(c, p))
def identity(c, p):
    b = git(c, p)
    return {'commit': c, 'path': p, 'bytes': len(b), 'sha256': sha(b),
            'git_blob': subprocess.check_output(['git', 'rev-parse', c + ':' + p]).decode().strip(),
            'lines': len(b.decode().splitlines())}
def raw_array(c, p, field, key):
    s = git(c, p).decode()
    m = re.search(r'^  "' + field + r'": \[', s, re.M)
    pos = m.end(); decoder = json.JSONDecoder(); result = {}
    while True:
        while s[pos].isspace() or s[pos] == ',': pos += 1
        if s[pos] == ']': return result
        start = pos; obj, pos = decoder.raw_decode(s, pos)
        result[obj[key]] = {'lines': [s.count('\n', 0, start) + 1, s.count('\n', 0, pos) + 1],
                            'sha256': sha(s[start:pos].encode()), 'bytes': len(s[start:pos].encode())}
def owned(x):
    return any('/' + d + '/' in x['source']['document'] for d in ['pokemon-rules', 'engine-overworld', 'user-interface'])
def merge(rs):
    out = []
    for a, b in sorted(rs):
        if out and a <= out[-1][1] + 1: out[-1][1] = max(b, out[-1][1])
        else: out.append([a, b])
    return out

man = read(C, B + 'routing-manifest.json'); prev = read(R1, B + 'routing-manifest.json'); initial = read(OLD, B + 'routing-manifest.json')
mf = {x['feature_id']: x for x in man['features']}; pf = {x['feature_id']: x for x in prev['features']}
of = {x['feature_id']: x for x in initial['features']}
mr = {x['feature_id']: x for x in man['retired_features']}; pr = {x['feature_id']: x for x in prev['retired_features']}
mm = {x['metadata_id']: x for x in man['metadata_records']}; pm = {x['metadata_id']: x for x in prev['metadata_records']}
ids = {i for i, x in mf.items() if owned(x)}; oldids = {i for i, x in of.items() if owned(x)}
metaids = {i for i, x in mm.items() if owned(x)}
domains = {n: read(RR, RP + 'agents/' + n + '-results.json') for n in ['pokemon', 'world-ui']}
rootfiles = {n: read(RR, RP + n) for n in ['findings.json', 'finding-results.json', 'feature-results.json', 'reading-coverage.json']}
prior_global = rootfiles['feature-results.json']
rootold = {x['feature_id']: x for x in prior_global['old_feature_results']}
rootactive = {x['feature_id']: x for x in prior_global['active_feature_results']}
rootmeta = {x['metadata_id']: x for x in prior_global['retired_metadata_results']}
prior_old = {x['feature_id']: x for d in domains.values() for x in d['old_feature_results']}
prior_active = {x['feature_id']: x for d in domains.values() for x in d['active_feature_results']}
prior_meta = {x['metadata_id']: x for d in domains.values() for x in d['retired_metadata_results']}
assert ids == set(prior_active) and oldids == set(prior_old) and metaids == set(prior_meta)
assert all(prior_old[i]['verdict'] == rootold[i]['verdict'] for i in oldids)
assert all(prior_active[i]['verdict'] == rootactive[i]['verdict'] for i in ids)
assert all(prior_meta[i]['verdict'] == rootmeta[i]['verdict'] for i in metaids)
raw = {c: {f: raw_array(c, B + 'routing-manifest.json', f, k) for f, k in [('features', 'feature_id'), ('retired_features', 'feature_id'), ('metadata_records', 'metadata_id')]} for c in [R1, C]}

# Concrete semantic cases established by freshly reading each complete effective source unit
# and the complete cited target unit. Classification and responsibilities are a distinct facet.
casespec = [
 (348, [355], '地牢图块化的布局符号、编号/墙块和自动邻接变体不消费音频播放/暂停/叫声；FR355不是图块资源匹配。'),
 (372, [355,358], '世界天气的元数据采样、屏幕天气意图、固定渐变和列明消费者不消费音频或战前特殊过渡注册；天气显示不能由同WP16的战前过渡承接。'),
 (373, [33,355,358], '九天气类别/粒子/平铺/色调/风暴白闪数据不消费战斗中止/异常、音频或战前特殊过渡。战斗天气映射是另一具名合同，不能用FR33替代。'),
 (487, [25,26], 'Shadow经验/EV暂存、友好与成长拒绝门引用WP42/WP30成长；FR25/26是WP41换人/逃跑失败和配置，不承接这份成长合同。'),
 (608, [670], '图鉴展示/搜索/形态浏览源节明确WP66-B消费者；FR670为WP66-C背包入口/过滤选择，不是图鉴条目/主列表。'),
 (664, [157,158], '盒子操作矩阵和即时移动/释放/持物/标记/退出引用WP25容器/守卫；伙伴参战谓词及伙伴战后治疗不承担这些存取规则。'),
 (681, [25,26], '经验、升级和持久/战斗招式双提交的显示链引用WP42/WP30；WP41换人/逃跑失败/配置并非这份成长提交合同。'),
 (682, [157,158], '捕获队列、图鉴/命名、满队送盒和记忆左移的实际源合同不消费伙伴参战谓词或伙伴战后治疗。'),
 (749, [157,158,172,667], '净化室编成的储存选择器/引用移动/纯交换没有伙伴参战、伙伴战后、NPC脚本交换属主/命名或图鉴Forms浏览；已有源明确是WP25/WP66-B储存选择与WP67-B净化室。'),
 (751, [358], '雷达摇草动画请求→列表写入→0.5秒等待不消费战前过渡注册选择。'),
 (754, [25], 'LUCKYEGG/努力值持物倍率静态目录指WP50§6和WP42/WP30成长，不指WP41换人失败。'),
 (755, [25], 'EXP.SHARE/奖金持物世界输入引用成长/终局/持久物品；WP41换人失败不能承担其成长分配。'),
 (756, [650], 'Safari回起点是地图场景门和转移；训练家卡开场/只读BACK/淡出释放不是地图转移合同。'),
 (757, [650], '捕虫倒计时、帧到期通知、地图微更新和计时器显示不消费独立训练家卡场景。'),
 (759, [650], '活动暂停菜单、专用退出/Save/普通Quit/共享保存与调试不消费训练家卡开场和只读BACK循环。'),
 (760, [358,643], '树果常规地图显示结算、阶段资源及闪光不消费战前特殊过渡注册或WP65保存/退出交接；需要真实地图显示/更新消费者。'),
 (761, [186,650], '施肥/种植/采摘、过滤背包、确认微更新不采用战斗登记预扣/复检退款，也不进入训练家卡场景。'),
 (762, [186], '世界Repel再次使用与移动/警告/通知源单元不是战斗用物登记/复检/退款；实际普通道具入口应精确导航。'),
 (764, [650], '失败回程取消载具/伙伴/设置转移/刷新不经过训练家卡独立场景。'),
 (766, [699], 'Voltorb格翻面、效果、全盘揭露/确认/收牌阶段不消费Slot三轮停止/滑移；同WP69不能证明共享规则。')]
bad = {f'FR-{i:06}': [f'FR-{j:06}' for j in js] for i, js, why in casespec}
FID = 'POK-WORLD-R2-DEP-001'
cases = []
fresh = collections.defaultdict(list)
for i, js, why in casespec:
    fid = f'FR-{i:06}'; x = mf[fid]
    for target in bad[fid]: assert target in x['dependencies']['feature_refs']
    pidx = next(k for k, t in enumerate(man['features']) if t['feature_id'] == fid)
    cases.append({'feature_id': fid, 'source_document': x['source']['document'], 'source_ranges': x['functional_scope']['line_ranges'],
                  'candidate_pointer': f'/features/{pidx}/dependencies/feature_refs', 'wrong_feature_refs': bad[fid],
                  'targets': [{'feature_id': t, 'document': mf[t]['source']['document'], 'heading': mf[t]['source']['heading'], 'ranges': mf[t]['functional_scope']['line_ranges']} for t in bad[fid]],
                  'verdict': 'FAIL', 'classification_verdict': 'PASS', 'reason': why,
                  'r1_record_unchanged': mf[fid] == pf[fid]})
    fresh[x['source']['document']] += x['functional_scope']['line_ranges']
    for t in bad[fid]: fresh[mf[t]['source']['document']] += mf[t]['functional_scope']['line_ranges']

# Additional completed fresh reading; no truncation is credited for a missing range.
for i in [355,726,682,679,463,464,471,473,525,546,576,656,155,158,186,190,191,192,420,157]:
    x=mf[f'FR-{i:06}']; fresh[x['source']['document']] += x['source']['line_ranges']
fresh['deliverables/final-specification-set/pokemon-rules/wp43-types-accuracy-and-damage.md'] += [[1,43]]
fresh['deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md'] += [[253,320]]
fresh['deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md'] += [[1,317]]
fresh['deliverables/final-specification-set/demo-dx/wp77-demo-evidence-and-capability-coverage.md'] += [[49,197]]
fresh['deliverables/final-specification-set/generic-kernel/wp02-rule-configuration-and-data-variants.md'] += [[246,256]]
fresh['deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md'] += [[313,359]]
fresh['deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md'] += [[286,296]]
fresh['deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md'] += [[285,294],[319,344]]
fresh['deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md'] += [[5,91],[97,180],[200,236]]
fresh['deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md'] += [[277,288]]

all_inputs = ['REPORT.md', 'findings.json', 'finding-results.json', 'feature-results.json', 'reading-coverage.json', 'agents/pokemon-report.md', 'agents/pokemon-results.json', 'agents/world-ui-report.md', 'agents/world-ui-results.json']
input_ids=[]
for p in all_inputs:
    x=identity(RR,RP+p); local=Path('/workspace/r8-disposition-r1-review')/(RP+p)
    x['physical_prior_tree_matches_fixed_git']=local.read_bytes()==git(RR,RP+p)
    assert x['physical_prior_tree_matches_fixed_git']; x['consumption']='FULL_REPORT_OR_STRUCTURAL_RECONCILIATION_WITH_ALL_OWN_ROWS_GROUPS_AND_ATTRIBUTED_READING_CREDIT'
    input_ids.append(x)

feature_evidence={}
active=[]; old=[]; metas=[]
for i in sorted(ids):
    x=mf[i]; exact=x==pf[i]; rexact=raw[C]['features'][i]['sha256']==raw[R1]['features'][i]['sha256']
    assert exact and rexact
    b=git(CUR,x['source']['document']); lines=b.splitlines(keepends=True); loc=x['current_applicability']['locator']
    assert loc['unit_sha256']==sha(b''.join(b''.join(lines[a-1:e]) for a,e in loc['line_ranges']))
    assert loc['file_sha256']==sha(b) and loc['line_ranges']==x['functional_scope']['line_ranges']
    assert loc['file_git_blob']==hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    assert x['current_applicability']['snapshot_commit']==CUR
    sourcebytes=git(x['source']['commit'],x['source']['document']); source_lines=sourcebytes.splitlines(keepends=True)
    assert x['source']['unit_sha256']==sha(b''.join(b''.join(source_lines[a-1:e]) for a,e in x['source']['line_ranges']))
    assert x['source']['file_sha256']==sha(sourcebytes)
    scope_lines={n for a,e in x['functional_scope']['line_ranges'] for n in range(a,e+1)}
    source_lineset={n for a,e in x['source']['line_ranges'] for n in range(a,e+1)}
    for child in x['functional_scope']['excluded_child_refs']:
        source_lineset-={n for a,e in mf[child]['source']['line_ranges'] for n in range(a,e+1)}
    assert source_lineset==scope_lines
    evidence={'object_equal':exact,'raw_git_row_bytes_equal':rexact,'r1':raw[R1]['features'][i],'candidate':raw[C]['features'][i],
              'current_locator_unit_and_file_hash_recomputed':True,'immutable_source_git_hash_recomputed':True,'functional_scope_exact_parent_minus_children':True}
    feature_evidence[i]=evidence
    active.append({'feature_id':i,'r1_verdict':prior_active[i]['verdict'],'verdict':'FAIL' if i in bad else 'PASS',
                   'classification_verdict':'PASS','dependency_verdict':'FAIL' if i in bad else 'PASS',
                   'reason':next(c['reason'] for c in cases if c['feature_id']==i) if i in bad else '固定R1行的全部原始Git字节与字段相等；已核R2新增/修改出入站关系及同根目录传播，不改变原功能归属/职责/范围/状态判断。 '+prior_active[i]['reason'],
                   'method':'EXACT_GIT_RAW_ROW_AND_FIELDS_PLUS_SEMANTIC_SAME_ROOT_REASSESSMENT' if i in bad else 'ATTRIBUTED_R1_SEMANTIC_CREDIT_PLUS_EXACT_GIT_RAW_ROW_AND_NONIMPACT',
                   'source_document':x['source']['document'],'functional_scope':x['functional_scope'],'is_r1_new':i not in of,
                   'affected_fields':['dependencies.feature_refs'] if i in bad else [],'finding_refs':[FID] if i in bad else [],
                   'prior_evidence':RP+'agents/'+('pokemon' if '/pokemon-rules/' in x['source']['document'] else 'world-ui')+'-results.json#/active_feature_results',
                   'exact_identity':evidence})
for i in sorted(oldids):
    x=mf.get(i) or mr[i]; retired=i in mr
    if retired: assert {k:v for k,v in x.items() if k!='retirement'}==of[i]
    else: assert x['source']==of[i]['source']
    old.append({'feature_id':i,'r1_verdict':prior_old[i]['verdict'],'verdict':'FAIL' if i in bad else 'PASS',
                'classification_verdict':'PASS','dependency_verdict':'FAIL' if i in bad else 'PASS','disposition':'retired' if retired else 'active',
                'reason':next(c['reason'] for c in cases if c['feature_id']==i) if i in bad else 'R1具体语义理由保留；固定Git整行身份与未受变更影响的facet已核。 '+prior_old[i]['reason'],
                'review_method':'REREAD_COMPLETE_SOURCE_AND_WRONG_TARGET' if i in bad else 'INHERITED_ATTRIBUTED_R1_READING_WITH_EXACT_IDENTITY_AND_NONIMPACT',
                'finding_refs':[FID] if i in bad else [],'source_document':x['source']['document'],'immutable_source_preserved':x['source']==of[i]['source'],
                'complete_retired_history_preserved':True if retired else None})
for i in sorted(metaids):
    x=mm[i]; assert x==pm[i]
    for f in x['retired_feature_ids']: assert {k:v for k,v in mr[f].items() if k!='retirement'}==of[f]
    metas.append({'metadata_id':i,'retired_feature_ids':x['retired_feature_ids'],'r1_verdict':prior_meta[i]['verdict'],'verdict':'PASS',
                  'reason':'整份metadata和retirement导航与R1精确相同；非功能处理及固定原文完整历史保留。原消费者语义信用只保留该metadata facet；消费者自己的错误依赖另列，不由metadata导航转授。 '+prior_meta[i]['reason'],
                  'feature_refs':x['feature_refs'],'consumer_mapping_verdict':'PASS','nonfunctional_treatment':'PASS','complete_history_preserved':True,
                  'raw_git_row_identity':{'r1':raw[R1]['metadata_records'][i],'candidate':raw[C]['metadata_records'][i]}})

sec=read(C,B+'section-coverage.json')['sections']; psec=read(R1,B+'section-coverage.json')['sections']
catalogs=[p for p in subprocess.check_output(['git','ls-tree','-r','--name-only',CUR,'deliverables/final-specification-set/test-catalog']).decode().splitlines() if p.split('/')[-1].startswith(('pokemon-rules-','engine-overworld-','user-interface-'))]
catalog_results=[]
collision_bad={f'FR-{i:06}' for i in list(range(380,388))+[699,700,701,702,703,705,706,708,709,710,711,712,728,730]}
for k,s in enumerate(sec):
    if s['path'] not in catalogs: continue
    added=sorted(set(s['feature_refs'])-set(psec[k]['feature_refs'])); removed=sorted(set(psec[k]['feature_refs'])-set(s['feature_refs']))
    if k in range(2277,2293): assert not (set(s['feature_refs'])&collision_bad) and set(removed)==collision_bad
    if k==2275: assert 'FR-000724' in s['feature_refs'] and added==['FR-000724']
    catalog_results.append({'section_index':k,'path':s['path'],'title':s['title'],'ranges':[[s['line_start'],s['line_end']]],'verdict':'PASS',
                            'review_method':'FRESH_SOURCE_AND_EXACT_MAPPING_DIFF' if added or removed else 'R1_EXACT_SECTION_OBJECT_IDENTITY_PLUS_RETAINED_SEMANTIC_CREDIT',
                            'record_exactly_equal':s==psec[k],'added_feature_refs':added,'removed_feature_refs':removed,
                            'reason':'静态未执行目录身份保持；具名724已可达、16节异体系ID清除；其它目录既有合法宽导航及父→excluded_child_refs间接导航保留。功能依赖闭包新增错误单独列，不把它冒充目录直接feature_refs未修。'})
assert len(catalog_results)==141
groups=[]
for d in domains.values():
    for g in d['finding_results']:
        q=copy.deepcopy(g); q['r1_verdict']=g['verdict']; q['verdict']='PASS'; q['review_method']='R1_ORIGINAL_FACET_EXACT_IDENTITY_AND_ORIGINAL_CASES_RECONCILIATION'
        q['original_case_verdict']='PASS'; q['current_scope_verdict']='FAIL' if g['finding_id']=='WU-06' else 'PASS'
        if g['finding_id']=='WORLD-CATALOG-F01': q['same_root_propagation_verdict']='PASS'
        q['r1_full_result']=g; q['reason']='原问题具体分类/范围/职责/退役facet成立且保持；WORLD-CATALOG-F01的16反向目录传播本轮已修。新增/保留的具体依赖错链另列；WU-06当前扩大依赖检查scope FAIL而原三case PASS。历史R1理由另保留在r1_full_result。'
        q['related_new_finding_refs']=[FID] if g['finding_id'] in ['POK-S02','POK-S04','POK-S05','WU-03','WU-06','WORLD-CATALOG-F01'] else []
        groups.append(q)
assert len(groups)==17

primary=sorted(set(p for p in subprocess.check_output(['git','ls-tree','-r','--name-only',CUR,'deliverables/final-specification-set']).decode().splitlines() if any('/'+d+'/' in p for d in ['pokemon-rules','engine-overworld','user-interface']))|set(catalogs))
assert len(primary)==62
oldcov={x['path']:x for x in read(OR,OP+'reading-coverage.json')['documents']}
r1cov={x['path']:x for x in rootfiles['reading-coverage.json']['documents']}
ledger=[]
for p in primary:
    q=identity(CUR,p); z=r1cov[p]; assert q['sha256']==z['current_identity']['sha256']
    q['candidate_formal_identity']=identity(C,p);q['b8_identity']=identity(B8,p)
    q['prior_semantic_credit']={'r1_report_commit':RR,'r1_reading_record':z,'original_report_commit':OR,'original_reading_record':oldcov[p],
                               'scope':'仅固定未变source与功能facet；incoming改动按完整源表重读、错误feature依赖按完整源/目标新判；不是本轮62份全文重读。'}
    q['fresh_read_ranges']=merge(fresh.get(p,[]));q['fresh_read_commit']=CUR;q['all_current_bytes_equal_r1_current']=True
    ledger.append(q)

# Enumerate every changed external incoming relationship and every own outgoing link to changed rows.
incoming=[]
for x in man['features']:
    y=pf.get(x['feature_id'],{})
    if x==y: continue
    a=set(x['dependencies']['feature_refs']);b=set(y.get('dependencies',{}).get('feature_refs',[]))
    dr=[t for t in x['dependencies']['direct_refs'] if t not in y.get('dependencies',{}).get('direct_refs',[]) and t['document'] in {mf[i]['source']['document'] for i in ids}]
    if (a^b)&ids or dr: incoming.append({'producer_id':x['feature_id'],'added_own_refs':sorted((a-b)&ids),'removed_own_refs':sorted((b-a)&ids),'new_own_direct_refs':dr,'impact':'新增实际音频/战斗用物/形态/Mega统计共享合同不改接收者功能分类；具体源/目标完整单元已读。出站旧错误不因此获PASS。'})
metaincoming=[]
for x in man['metadata_records']:
    y=pm.get(x['metadata_id'],{})
    a=set(x['feature_refs']);b=set(y.get('feature_refs',[]))
    if (a^b)&ids: metaincoming.append({'metadata_id':x['metadata_id'],'source':x['source'],'added_own_refs':sorted((a-b)&ids),'removed_own_refs':sorted((b-a)&ids),'impact':'重新读WP77完整组、WP02组合表、WP03完整字段责任表及WP04完整交界表；消费者为责任/证据导航，不更改接收行去向/范围/状态，也不把Demo变新功能。'})
changed={x['feature_id'] for x in man['features'] if x!=pf.get(x['feature_id'])}|(set(pf)-set(mf))
outgoing=[{'feature_id':i,'changed_target_refs':sorted(set(mf[i]['dependencies']['feature_refs'])&changed),'verdict':'FAIL' if i in bad else 'PASS','finding_refs':[FID] if i in bad else []} for i in sorted(ids) if set(mf[i]['dependencies']['feature_refs'])&changed]
external_catalog_incoming=[]
for k,(a,b) in enumerate(zip(psec,sec)):
    if a==b or '/test-catalog/' not in b['path'] or b['path'] in catalogs: continue
    added=(set(b['feature_refs'])-set(a['feature_refs']))&ids
    removed=(set(a['feature_refs'])-set(b['feature_refs']))&ids
    if added or removed:
        external_catalog_incoming.append({'section_index':k,'path':b['path'],'ranges':[[b['line_start'],b['line_end']]],'added_own_refs':sorted(added),'removed_own_refs':sorted(removed),'verdict':'PASS',
                                          'reason':'完整具名静态源表已读：培养252/510、TP/TE、形态读取门、KC03/05/06、KR13、连接/地牢/指标、语言键图。新增关系有实际既有消费者，不新造功能/运行资格；接收者自身出站错链另计。'})

issues=[{'issue_id':'POK-R1-CATALOG-001','r1_verdict':'FAIL','verdict':'PASS','cases':[{'section_index':2275,'feature_refs_added':['FR-000724'],'source_ranges':[[270,285]],'verdict':'PASS','reason':'FB01–06各前提/PP前缀/变化失败/伤害回退/None/SHADOWSHED边界与WP43§2.1 L29–36真实724一致。'}],'same_root_propagation':'4本域目录47节逐节比较，补漏724外所有R1显式父→子导航保留；未执行保持。'},
 {'issue_id':'R1-CATALOG-WP-COLLISION','r1_verdict':'FAIL','verdict':'PASS','scope':'原16节直接目录feature_refs修复facet','cases':[x for x in catalog_results if x['section_index'] in range(2277,2293)],'original_forward_cases':{'count':81,'all_section_objects_unchanged':all(sec[i]==psec[i] for i in list(range(2183,2212))+list(range(2293,2345))),'verdict':'PASS'},'same_root_propagation_verdict':'FAIL','same_root_propagation_finding_refs':[FID],'reason':'352条错误直接目录边全部删去，六份源正文身份匹配；Voltorb等保留feature_refs的异体系错链仍有，单独报告。'}]
finding={'id':FID,'severity':'P3','verdict':'FAIL','title':'通过行的依赖导航仍保留异体系/错章节feature_refs','candidate_file':B+'routing-manifest.json','cases':cases,
         'related_original_roots':['POK-S02','POK-S04','POK-S05','WU-03','WU-06','WORLD-CATALOG-F01'],'related_residual_roots':['R1-CRE-DEP-001','R1-CATALOG-WP-COLLISION'],
         'why':'精确相等只证明保全，不能证明原依赖正确；实际具名源和目标显示这些稳定ID指向不同消费者。正确direct_refs或另一个正确ID不使多余错误feature_refs变真。',
         'required_change':'保留已通过的去向/职责/范围/source，只删除或替换逐case无实际用途的feature_refs，按源已有真实合同连接相应消费者并核对同根传播；不造新功能、不要求逐句ID或运行原型。'}
result={'schema_version':'r2-independent-pokemon-world.v1','candidate_commit':C,'r1_candidate_commit':R1,'r1_report_commit':RR,'current_snapshot_commit':CUR,
        'configuration':{k:'UNVERIFIED' for k in ['actual_model','actual_effort','actual_service_tier','actual_speed','actual_Fast','cloud_task_UUID']},
        'outcome':'FAIL','counts':{'old_features':len(old),'active_features':len(active),'r1_new_active':sum(x['is_r1_new'] for x in active),'metadata':len(metas),'retired_old':sum(x['disposition']=='retired' for x in old),'original_groups':len(groups),'primary_documents':len(primary),'catalog_sections':len(catalog_results),'dependency_fail_rows':len(cases),'old_verdicts':dict(collections.Counter(x['verdict'] for x in old)),'active_verdicts':dict(collections.Counter(x['verdict'] for x in active))},
        'old_feature_results':old,'active_feature_results':active,'retired_metadata_results':metas,'issue_results':issues,'original_group_results':groups,'reading_ledger':ledger,
        'extra_consumer_reading':[dict(identity(CUR,p),fresh_read_ranges=merge(r)) for p,r in fresh.items() if p not in primary],
        'catalog_section_results':catalog_results,'incoming_dependency_results':incoming,'incoming_metadata_results':metaincoming,'outgoing_to_changed_rows':outgoing,
        'external_catalog_incoming_results':external_catalog_incoming,
        'retained_r1_domain_extra_facets':{n:{k:v for k,v in d.items() if k in ['catalog_consumer_navigation_results','related_finding_results','accepted_backfill_results','indirect_child_navigation','historical_navigation_observation','necessary_consumer_reading','entry_input_identities']} for n,d in domains.items()},
        'all_nonempty_feature_dependency_rows':81,'exact_active_row_preservation_count':len(feature_evidence),'mandatory_r1_inputs':input_ids,'new_findings':[finding],
        'limits':['固定908/U02U03阶段；0eee后继新源范围由另一个分工审查，本结果不授予最终全量校准。','原型/业务/Ruby/宿主/参考/新框架执行均0。','62文档逐篇固定Git身份与归属阅读信用核算；完整源新读仅列明范围，未宣称本轮全文重读。','753诊断/校验可经395的WP08语言合同间接导航；744名人堂有训练家数据卡，未仅凭宽导航判错。']}
(OUT/(PREFIX+'results.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
evidence={'candidate':C,'r1_candidate':R1,'raw_exact_rows':feature_evidence,'metadata_rows_exact':{i:raw[C]['metadata_records'][i]['sha256']==raw[R1]['metadata_records'][i]['sha256'] for i in metaids},'counts':result['counts'],'formal_trees':{c:subprocess.check_output(['git','rev-parse',c+':deliverables/final-specification-set']).decode().strip() for c in [B8,R1,C,CUR]},'all_assertions_passed':True}
(OUT/(PREFIX+'evidence.json')).write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result['counts'],ensure_ascii=False))
