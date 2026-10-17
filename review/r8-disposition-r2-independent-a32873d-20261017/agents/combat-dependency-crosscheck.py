"""Independent full edge-set semantic crosscheck; author Python is AST-read only."""
import ast
import hashlib
import json
import subprocess
from pathlib import Path

ROOT=Path('/workspace/r8-disposition-r2-review')
BASE=Path('planning/implementation-routing/r8-20261017')
OUT=ROOT/'review/r8-disposition-r2-independent-a32873d-20261017/agents'
CAND='a32873d2860b15d9f5e27727db8f131f4ec433b6'
R1='5666b7b912e2fb79b5119283ee6a37401a7071db'
CURRENT='908273093e1f6b27fc58249417675dd62d146224'
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*a):return subprocess.check_output(['git',*a],cwd=ROOT)
def read(p):return json.loads((ROOT/p).read_text())
def fixed(c,p):return json.loads(git('show',c+':'+str(p)))
def fid(n):return f'FR-{n:06d}'
m=fixed(CAND,BASE/'routing-manifest.json');r1=fixed(R1,BASE/'routing-manifest.json')
f={x['feature_id']:x for x in m['features']}
sources=[x for x in m['features'] if '/combat-requirements/' in x['source']['document'] and x['dependencies']['feature_refs']]
purpose={
4:{29:'成长后的等级/HP/能力回读与新招同步消费本初始化/写穿模型。',31:'正常终局逐成员形态/持物记录与撤选择清理消费同一场上—持久分层。',145:'HP赋值钳制、真实失能与治疗的持久主规则。',146:'异常与计数的持久设置/清理主规则。',739:'本初始化明确招式包装和真实PP同步，739定义其三层写回边界。',740:'持物入口写穿与可更新终局还原记录的主边界。'},
20:{22:'野生玩家拒用下一只时调用替补逃跑入口并消费决定3。',31:'补位检查点和决定3最终由正常终局消费。',32:'终局后世界善后/包装结果与补位真值分开。',734:'业主队伍选择的强制/取消许可与资格/登记层交接。'},
58:{20:'中途退出与回合末延后补位的主流程共享。',22:'逃离类实际可逃/决定3主规则。',23:'本章退出/随机拖出/接力效果由WP41有界族共同定义。',31:'逃离决定和未执行选择等交正常终局消费。',734:'真实属主替补请求等待/返回，不能用资格真代替选择完成。'},
61:{4:'物品入口写穿持久个体而直接局部id赋值不同。',31:'临时/永久持物变化由正常终局读取当时还原记录。',739:'FAIL:本源仅C/I/R/P/Belch、物权/金钱标记；739仅招式/PP包装与写回，没有本源的使用或具名排除用途。',740:'C/I临时与永久变化、野生转移和终局还原记录的真实主合同。'},
66:{4:'局部离场HP0与真正濒死状态/持久HP的分层模型。',31:'REGENERATOR战斗结束标志与正常终局调用范围在此定义。',739:'FAIL:离场/濒死源范围只有HP/真实状态/友好/形态/能力链，739的PP同步不被使用，未声明排除性对照。',740:'紧张感结束调用持物触发可消费树果，持物写穿/还原记录按此主边界。'},
68:{4:'每击中央HP/状态写穿、形态/濒死与局部字段按初始化职责分层。',31:'各检查点不等于所有回调立即退出；物权及结束选择由正常终局消费。',739:'CURSEDBODY读取当前槽PP/有限总PP，后段保留已扣PP前缀；包装/持久身份三层合同可作共享边界，不说能力本身扣PP。',740:'MAGICIAN/PICKPOCKET当前物与双方还原记录变动的主合同。'},
69:{4:'回合末HP/真实异常/形态的场上与持久字段入口。',31:'当前还原记录最终消费及正决定只在显式检查点结束的终局交界。',739:'FAIL:完整回合末四族为天气HP、异常治疗、阶级与取物，不涉及招式PP同步；739不承接其中任何具名字段。',740:'BALLFETCH/HARVEST/PICKUP对当前物、回收/拾取与可更新还原记录的真实交界。'},
71:{4:'直接形态、HP差值保护、IMPOSTER临时复制/持久不改的初始化模型。',31:'直接形态与共生后的正常终局/还原消费不同于本局部回调。',739:'DANCER不额外扣原槽PP及IMPOSTER场上PP/总PP5明确需要临时/持久招式身份边界。',740:'SYMBIOSIS转物不更新双方还原记录，CHEEKPOUCH/消费链按本持物交界。'},
75:{11:'AI最终登记UseItem沿同一资源分层/执行复检退款路径。',177:'玩家被AI控制可走玩家背包消费；与业主items列表分开，源L128明确资源不匹配异常。',186:'逐件真实可用性/战斗资格查询与实际效果的上下文主合同。',187:'AI登记后的执行退款残留/终局消费者仍受同一主合同，而非选择偏好保证。'},
121:{114:'固定人数/限制参数由资格组合和最终选择判断消费。',115:'固定物种/特性/禁物/禁招集合的实际资格消费者。',736:'报名界面使用这些成员/整队条件，数据不是新增UI实现。'},
124:{125:'会话与单场治疗/经验物品还原以及胜负布尔明确分工。',162:'队伍容量/容器成员引用作为报名、整体替换和恢复所操作的领域上下文，不能借其界面守卫证明整体引用安全。',324:'仅地图场景显式设置开始位置并执行转移，目标4章真实显式转移消费者。',444:'global_metadata包含会话持久对象，整体保存/读取配置与会话字段语义分开。',446:'开始/暂停/继续/结束的安全保存真实入口，IO假与传播异常分层。',449:'限定为旧存档转换/版本与持久恢复的对照前置；候选direct_ref明确旧格式迁移不能由单场成功推出，非宣称会话保存调用转换。',451:'限定为读档/地图恢复/紧急保存失败的另一层对照，候选direct_ref明确恢复失败不可从单场成功推断；不替代446保存本体。'},
126:{116:'单场调整/经验还原不同阶段失败保留的部分写入。',124:'开始已置位、队伍引用恢复、名单不终止及暂停保存位置的实际状态来源。',125:'单场已调用后的战斗/经验/物品善后失败前缀与会话分工。',446:'源L131明确保存本体IO错误返回假、其它异常传播，目标L127–131有真实对应。',451:'失败层对照限定：启动坏档/超时紧急保存/地图恢复不是本会话的通用兜底；本源保存假仍以446为准，未宣称自动恢复。'},
128:{9:'玩家Fight/AI自动菜单的截获点及登记后进入攻击阶段。',13:'自动选招结果仍由通常行动排序/执行消费，性格随机不替代该排序合同。',73:'普通AI换人/用物后自动菜单截获明确指向Palace，作为被覆写流程对照。',74:'Palace专用换人替换普通意愿/否决/后备评分；对照而非把普通策略套用。',134:'Palace自动槽与无力-2的实际记录钩子。',135:'Palace自动随机不进记录随机序列，而结果按槽位回放。'},
129:{4:'成功状态机初始化及裁判直接HP0写穿/真正濒死。',20:'普通业主选择补位的排除对照：Arena禁止该选择、改顺序补位，不能把20当Arena调用。',30:'先常规回合末，再累计技/计数/裁判的真实共用阶段。',31:'无后备裁判终局与正常收尾，直接裁判HP0不等同普通伤害。',737:'父已扣102–104，逐项心技体比较及裁判UI交给子单元。'},
130:{128:'差异表的Palace性格/自动选择/专用换人主规则。',129:'差异表Arena成功槽/连续裁判/顺序补位主规则。',134:'模式差异中的命令登记内容/时点。',135:'模式差异中的随机域/换人序列及回放限定。'},
731:{11:'失败退款的选择期扣物/执行期复检与身份生产点。',31:'正常终局读取残留身份再次退款的实际消费者。',177:'每次退款当时可加入容量及实际背包变更。',186:'登记/执行/退款各家族的同一使用主合同。',187:'同轮终局退款及独立命令/失能对照主合同。'},
732:{3:'UI下标与业主/席位身份、邻近关系映射。',51:'登记允许/初选/实际执行目标解析分开，异常选远端不使执行成功。',678:'目标窗口的初选、文本、光标、USE/BACK及取消返回真实呈现。'},
733:{155:'六入口曲目选择和引子记忆先于交付的生产合同。',355:'音量/参数/默认覆盖/暂停恢复的实际播放请求入口。',683:'捕获成功ME及3.5秒等待、胜负音频后的消息等待消费者。',726:'WP16§1包装实际暂停/播放/正常恢复/清音乐备忘和下一战预置。'},
734:{655:'共享队伍画面的成员面板、导航、选择/取消基本合同。',680:'战斗下标映射、SwitchIn/摘要、分层取消和替补包装。'},
735:{147:'持久招式列表/PP对象及新槽初始化的主数据边界。',207:'明确排除对照：本源L209说明全局学习/遗忘不能替代两个复制效果，207是战斗升级学习；不赋写生摘要菜单或取消流程。'},
736:{115:'成员/整队约束是资格注解和最终选择的实际输入。',654:'设施报名多选入口模式及按位次成员数组返回。',655:'多选面板、CONFIRM/CANCEL、位次注解和选择基础呈现。'},
737:{684:'Arena特殊裁判窗与心技体逐项总结的实际呈现消费。'},
738:{135:'回放按记录消费随机/换人并保留序列不足边界，不凭种子保证。',677:'通常记录驱动命令循环覆写及场景中止决定0的外层消费；不调用普通命令UI。',678:'非单打、安可且玩家侧的残余选靶例外实际窗口。',683:'普通/暂停消息自动等待差异与BACK触发中止。'},
769:{20:'回合末仅召回，实际后段补位由此消费者负责。',22:'野生可逃查询及决定3的规则归属。',31:'决定3正常终局共同收尾。',32:'世界善后/返回/统计的消费与能力真值分开。',734:'非回合末等待业主选择、取消/负下标与摘要返回的交互合同。'}
}
edges=[]
for x in sources:
    n=int(x['feature_id'][3:]);assert set(x['dependencies']['feature_refs'])=={fid(i) for i in purpose[n]}
    for target in x['dependencies']['feature_refs']:
        y=f[target];why=purpose[n][int(target[3:])];bad=why.startswith('FAIL:')
        edges.append(dict(source_feature_id=x['feature_id'],target_feature_id=target,verdict='FAIL' if bad else 'PASS',
                          reason=why,relationship='WRONG_PURPOSE' if bad else ('EXPLICIT_CONTRAST' if '对照' in why else 'SHARED_CONTRACT_OR_CONSUMER'),
                          source_document=x['source']['document'],source_effective_scope=x['functional_scope']['line_ranges'],
                          target_document=y['source']['document'],target_effective_scope=y['functional_scope']['line_ranges'],
                          target_heading=y['source']['heading'],classification_facet_verdict='PASS',
                          r1_edge_preserved=target in next((r['dependencies']['feature_refs'] for r in r1['features'] if r['feature_id']==x['feature_id']),[])))
assert len(sources)==24 and len(edges)==98 and sum(x['verdict']=='FAIL' for x in edges)==3
units={x['feature_id']:x for x in sources}
units.update({i:f[i] for x in sources for i in x['dependencies']['feature_refs']})
ledger=[]
for i,x in sorted(units.items()):
    p=x['source']['document'];data=git('show',CURRENT+':'+p);lines=data.decode().splitlines(keepends=True)
    effective=''.join(''.join(lines[a-1:b]) for a,b in x['functional_scope']['line_ranges']).encode()
    ledger.append(dict(feature_id=i,commit=CURRENT,document=p,fresh_read_ranges=x['functional_scope']['line_ranges'],
                       file_sha256=sha(data),effective_scope_sha256=sha(effective),
                       method='FULL_EFFECTIVE_SCOPE_FRESH_SEMANTIC_CROSSCHECK',
                       role='SOURCE_AND_TARGET' if i in {x['feature_id'] for x in sources} and i in {x['target_feature_id'] for x in edges} else 'SOURCE' if i in {x['feature_id'] for x in sources} else 'TARGET'))
finding=dict(id='COMBAT-R2-DEP-001',severity='P3',verdict='FAIL',title='持物/离场/回合末能力共享模板误挂招式PP同步单元739',
             feature_ids=[fid(i) for i in [61,66,69]],target_not_failed='FR-000739',
             candidate_pointers={fid(i):'/features/'+str(m['features'].index(f[fid(i)]))+'/dependencies/feature_refs' for i in [61,66,69]},
             source=[dict(path=f[fid(i)]['source']['document'],ranges=f[fid(i)]['functional_scope']['line_ranges']) for i in [61,66,69]],
             target_source=dict(path=f[fid(739)]['source']['document'],ranges=[[162,171]]),
             why='三源完整有效范围不消费招式/PP同步，且无具名排除用途；739只管招式包装三层、学招与首招记录。整行从R1保持不能证明这些出站边语义正确。740持物还原边依然正确，不能混为同一个WP20行为。',
             necessary_fix='移除61/66/69→739无用途边；保留740及其它真实共享合同。68的PP门、71的DANCER/IMPOSTER确有739语境，不批量删除。若作者主张其它用途须给真实源章依据并相应明确关系，不补造原规则。',
             classification_facet_verdict='PASS',overall_feature_verdict='FAIL',old_group_propagation='COMBAT-05 dependency facet; COMBAT-02 ownership/classification repairs remain credited.')
cross=dict(schema='r8-combat-full-dependency-crosscheck.v1',candidate_commit=CAND,current_snapshot=CURRENT,
           scope='All nonempty active combat dependencies.feature_refs outbound edges; source/target complete effective scopes.',
           counts=dict(source_features=24,outbound_edges=98,distinct_targets=len({x['target_feature_id'] for x in edges}),pass_edges=95,fail_edges=3),
           edge_results=edges,reading_ledger=ledger,new_findings=[finding],
           qualification='分类facet与依赖overall分开；不因外域入站错误反授目标FAIL。排除对照必须由明确源/候选用途支持，不能把所有无关引用都解释成对照。')
(OUT/'combat-dependency-crosscheck.json').write_text(json.dumps(cross,ensure_ascii=False,indent=2)+'\n')

# Read both entire author files as text/AST; never import or execute them.
scripts=[]
asts={}
for name,count in [('revise-data.py',358),('write-evidence.py',204)]:
    path=BASE/'revisions/r2'/name;data=git('show',CAND+':'+str(path));tree=ast.parse(data.decode());asts[name]=tree
    assert len(data.decode().splitlines())==count
    scripts.append(dict(path=str(path),commit=CAND,bytes=len(data),lines=count,sha256=sha(data),
                        actual_fresh_read_ranges=[[1,count]],ast_parsed=True,imported=False,executed=False))
dec=read(BASE/'revisions/r2/explicit-decisions.json');data_diff=read(BASE/'revisions/r2/data-diff.json')
script_decisions={ast.literal_eval(x.args[0]):dict(description=ast.literal_eval(x.args[1]),operations=ast.literal_eval(x.args[4]),line=x.lineno)
                  for x in ast.walk(asts['revise-data.py']) if isinstance(x,ast.Call) and isinstance(x.func,ast.Name) and x.func.id=='decision'}
assert len(script_decisions)==len(dec['items'])==11
for d in dec['items']:
    s=script_decisions[d['finding_id']];assert s['description']==d['description'] and s['operations']==d['operations']
def delta(old,new,key):
    a={x[key]:x for x in old};b={x[key]:x for x in new}
    return dict(added=sorted(b.keys()-a.keys()),removed=sorted(a.keys()-b.keys()),changed=[dict(id=k,fields=[field for field in sorted(a[k].keys()|b[k].keys()) if a[k].get(field)!=b[k].get(field)]) for k in sorted(a.keys()&b.keys()) if a[k]!=b[k]])
actual_deltas={k:delta(r1[mk],m[mk],idkey) for k,mk,idkey in [('features','features','feature_id'),('retired','retired_features','feature_id'),('metadata','metadata_records','metadata_id')]}
assert all(data_diff[k]==v for k,v in actual_deltas.items())
cv=read(BASE/'section-coverage.json')['sections'];oldcv=fixed(R1,BASE/'section-coverage.json')['sections']
actualcv=[dict(path=a['path'],anchor=a['anchor'],fields=[k for k in a if a[k]!=b[k]]) for a,b in zip(oldcv,cv) if a!=b]
assert data_diff['coverage_changed']==actualcv
links=read(BASE/'revisions/r2/consumer-mappings.json')['relationships']
meta={x['metadata_id']:x for x in m['metadata_records']};ret={x['feature_id']:x for x in m['retired_features']}
for mid in [f'META-{n:06d}' for n in [11,12,13,14,15,16,17,19,20,21]]:
    union=sorted({v for x in links if x['metadata_id']==mid for v in x['feature_refs']});assert union==meta[mid]['feature_refs']
    for rid in meta[mid]['retired_feature_ids']:assert ret[rid]['retirement']['replacement_feature_refs']==union
    for s in cv:
        if mid in s['metadata_refs']:assert set(union)<=set(s['feature_refs'])
expected_changed={fid(n) for n in [67,76,88,89,98,99,111,155,157,158,186,190,191,192,261,420,436]}
assert {x['id'] for x in actual_deltas['features']['changed']}==expected_changed
declared_feature_refs={i for d in dec['items'] for i in d['affected_refs'] if i.startswith('FR-')}
assert expected_changed|{fid(86),fid(769)}<=declared_feature_refs
transform=dict(schema='r8-r2-author-transform-consistency.v1',candidate_commit=CAND,r1_input=R1,
               conclusion='PASS_SCOPED_STATIC_EXPLICIT_TRANSFORM_CONSISTENCY_NOT_SEMANTIC_ACCEPTANCE',
               scripts=scripts,explicit_decisions=dec['items'],explicit_decision_script_call_map=script_decisions,
               actual_deltas=actual_deltas,actual_coverage_delta=actualcv,
               checks=dict(all_11_explicit_decision_descriptions_and_operations_match_AST=True,
                           all_actual_feature_retired_metadata_and_coverage_deltas_match_published_diff=True,
                           changed_active_fields_confined_to_17_declared_features=True,
                           metadata_consumer_union_retirement_and_coverage_synchronized=True,
                           fixed_semantic_snapshot_hash_matches_evidence_guard=sha(git('show',CAND+':'+str(BASE/'routing-manifest.json')))=='f7e6ee69c5f58c3f5dab89d39a0df7e4c5f1041ba4998dabe9a19879cdd428fc',
                           no_author_script_import_or_execution=True),
               code_review=['revise-data top level loads fixed5666 and refuses changed bytes before mutation; actions are explicit numbered data decisions, no keyword/heading destination seeding.',
                            '67 split/769 append and86 exact-d62 retirement are explicit; metadata loops consume explicit source-group lists; collision loop removes only named fixed source document identities.',
                            'source/current/decisions/prototypes/archive assertions precede saves; evidence script requires exact f7e6 snapshot and retains pre-calibration binding.',
                            'write-evidence derives author dispositions/preservation statements from fixedR1 rows, does not claim independentPASS. Same-row preservation is not semantic proof; new739 edge finding demonstrates its limit.'],
               limits=['未执行或重建作者输出，AST与实际diff一致只证明显式处置可追溯。',
                       '其他领域每条依赖/metadata语义由相应owner和root负责；本记录不给这些源章未新读部分语义PASS。',
                       '源接受门、U04、目标兼容与业务运行均无新批准。'])
(OUT/'combat-author-transform-consistency.json').write_text(json.dumps(transform,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(cross['counts'],ensure_ascii=False));print('AUTHOR STATIC DIFF/AST CONSISTENCY ASSERTIONS PASSED')
