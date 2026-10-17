"""Static supplementary semantic edge review; no author/game code is executed."""
import collections
import hashlib
import json
import pathlib
import subprocess

C='a32873d2860b15d9f5e27727db8f131f4ec433b6'
A='908273093e1f6b27fc58249417675dd62d146224'
P='planning/implementation-routing/r8-20261017/'
OUT=pathlib.Path(__file__).parent

def fid(n): return f'FR-{n:06d}'
def read(path,commit=C): return subprocess.check_output(['git','show',commit+':'+path])
def sha(b): return hashlib.sha256(b).hexdigest()
m=json.loads(read(P+'routing-manifest.json'))
features={x['feature_id']:x for x in m['features']}
rows=[x for x in m['features'] if '/creature-rpg/' in x['source']['document'] and x['dependencies']['feature_refs']]

# Each entry records the limited actual use checked in fixed source text, not a
# transfer of the R1 verdict because the row happened to be unchanged.
judgments=[
(153,330,'PASS','NOTIFICATION_AND_PERMISSION','WP24§4.1 L106的迈步/通知资格及§4.3跑鞋，实际由WP12§4 L101–110通知阶段、L118–125跑步门消费；不把通行或全局步数当煤灰采集资格。'),
(153,596,'PASS','SHARED_STATE_AND_STAGE','WP61有效范围L48明列任意事件擦首煤烟层及持袋玩家按实际增量写资源/统计；L26给普通玩家步进入口。排除给子项的通知演出不被偷算为596本体。'),
(153,741,'PASS','EXPLICIT_PARENT_CHILD_NAVIGATION','153有效范围已扣出WP24§4.4；feature_ref741提供钱包写入者目录到独立战斗结算子项的显式导航，不重新拥有子行为。'),
(154,742,'PASS','EXPLICIT_PARENT_CHILD_NAVIGATION','正常装载§5.2 L157明确由调用者处理缺失§5.3；742持有L160–172缺失/调试新建，154有效范围已扣出，属真实正常/缺失分流导航。'),
(155,355,'PASS','ACTUAL_CONSUMER','WP24§5.4 L196把播放/音量/默认覆盖/暂停恢复交WP15§6；355有效范围L129–190正承这些合同。'),
(155,682,'PASS','ACTUAL_CONSUMER','682的WP67-A§8 L215承野生捕获成功ME和3.5秒等待；不将训练家捕获误套同音乐。'),
(155,726,'PASS','ACTUAL_CONSUMER','726的WP16§1 L8承战前暂停、备忘位置、正常返回恢复及清四份下一战预置。'),
(155,733,'PASS','SHARED_REQUEST_BOUNDARY','733的WP39§7.5 L262–275把同一选择表交过渡/胜利/捕获入口，并保引子记忆早写和异常边界。'),
(157,1,'PASS','ACTUAL_CONSUMER','WP39§3.5 L118–121正消费伙伴参与谓词、第二训练家及独立伙伴道具列表。'),
(157,2,'PASS','ACTUAL_CONSUMER','WP39§4 L129–165消费参与数组、布局尺寸、业主必需席位与缩减；不是伙伴储存迁移。'),
(157,3,'PASS','ACTUAL_CONSUMER','WP39§5 L186–189承玩家/伙伴的侧内业主、队伍段和席位归属，不是原个体Owner字段。'),
(158,32,'PASS','ACTUAL_CONSUMER','WP42§7.1 L207承伙伴存在时治疗玩家与伙伴并解除伙伴变身，以及可败2/5的独立玩家治疗。'),
(158,464,'PASS','ACTUAL_CONSUMER','WP21§4.3 L240–247给普通成员含伙伴的开始/入场/离场/终战形态触发参数。'),
(158,473,'PASS','ACTUAL_CONSUMER','WP22§6 L85给世界战斗返回时有伙伴治疗/解除MegaPrimal，普通换下和裸终局另分。'),
(186,11,'PASS','ACTUAL_CONSUMER','WP40§4.2 L99–104承1–5使用家族、登记预扣、分家族执行复检、库存/捕获交界。'),
(186,32,'FAIL','WRONG_STAGE_TARGET','FR32有效范围仅WP42§7 L203–250外层世界善后；作者direct reason称“战后退款”，实际退款在§6 L177及§6.0 L183–191/FR31。'),
(186,525,'PASS','ACTUAL_CONSUMER','WP28§3.5 L117–118球分流实际交WP38§2 L21–29，登记消费与专用球执行/捕获失败不退款明确分开。'),
(186,679,'PASS','ACTUAL_CONSUMER','WP67-A§5 L138–154承过滤、目标/招式、取消层级、提交与登记/执行，是战斗上下文真实UI消费。'),
(190,11,'PASS','ACTUAL_CONSUMER','治疗/复活战斗主动入口沿WP28§3.5，共享WP40§4.2登记预扣、执行资格复检和退款；不将场外成功后扣减搬入战斗。'),
(190,32,'FAIL','WRONG_EFFECT_AND_STAGE_TARGET','WP42§7伙伴/可败全队治疗不是WP28§5.1主动药品/复活效果；direct reason另称退款但该范围不退款。真实正常终局退款属于FR31。'),
(190,145,'PASS','SHARED_STATE','WP20§3 L52及L69给持久HP钳制、道具部分回复与复活清状态，是主动HP表实际调用状态合同。'),
(190,576,'PASS','EXPLICIT_CONTRAST','WP28 L204明确持物触发另有合同；WP50§4 L78–94区分主动SITRUS与自动持物半血/食果/RIPEN/消费，正确对照而非把被动触发套主动入口。'),
(190,656,'PASS','ACTUAL_CONSUMER','WP28 L206明确奶招来源先扣HP与目标封顶，完整UI由WP66-A负责；656§4.2 L82给实际奶招选择循环/拒绝/刷新。'),
(190,679,'PASS','ACTUAL_CONSUMER','679§5提供战斗治疗目标选择、提交拒绝留层和取消，主动HP表不自行定义这些UI。'),
(191,11,'PASS','ACTUAL_CONSUMER','WP28 L220明确战斗PP道具在登记前拒绝濒死/满PP，不扣库存；WP40§4.2承登记与执行分层。'),
(191,147,'PASS','SHARED_STATE_WITH_EXPLICIT_CHILD','147有效§5.4 L154–160承总PP/钳制/恢复；PP同步子范围由显式147→739到L162–171，不把父已扣范围当仍有直接职责。'),
(191,576,'PASS','EXPLICIT_CONTRAST','WP28 L210/222明确主动LEPPA与持物不同；576有效WP50§4 L92给持久槽优先、RIPEN和无身份/变身检查的持物PP例外，故是准确失败/语义对照。'),
(191,679,'PASS','ACTUAL_CONSUMER','679§5 L143–145/151承招式选择、取消回成员选择、拒绝不登记，对应WP28 L220–222。'),
(192,11,'PASS','ACTUAL_CONSUMER','X/GuardSpec/娃娃/笛/球沿WP28§3.5家族登记/预扣与执行，WP40§4.2承真实命令分层。'),
(192,22,'PASS','ACTUAL_CONSUMER','WP28 L281娃娃受野生/可逃门，WP41§7 L156–173给逃跑查询/决定3及正常终局边界；不套玩家速度概率为娃娃必经。'),
(192,40,'FAIL','WRONG_EFFECT_TARGET','FR40有效WP45§7 L147–177仅火海、侧保护、侧交换/清屏障；作者direct reason为GuardSpec Mist建立/期限，真实同种正值拒绝和5回合侧期限在§6.2 L127/FR39。'),
(192,463,'PASS','ACTUAL_CONSUMER','WP28§5.5 L285显式指形态/融合道具§5.6与WP21提交；463有效§4 L189–234承形态写入后缓存/招式/HP/图鉴副作用，不是教学或香。'),
(192,525,'PASS','ACTUAL_CONSUMER','WP28 L284球资格与投球归WP38/WP40；525§2承菜单许可、登记及专用球执行。'),
(192,546,'PASS','SHARED_RULE','X各项/蘑菇的可升/升阶用WP44§5 L88–103资格与中央提交，不能只看请求档数保证实际升阶。'),
(192,679,'PASS','ACTUAL_CONSUMER','679§5 L143/147/151给X目标、GuardSpec/娃娃无目标与拒绝返回，不是邮件给予UI。'),
(204,487,'PASS','ACTUAL_BRANCH','WP30§4 L106/120实际分流Shadow暂存经验/EV；487有效WP23§6 L78/82给阶段≤3及暂存表门、普通EV回落，不把净化恢复当每次收益。'),
(207,735,'PASS','EXPLICIT_CONTRAST','WP30§6.1学招写持久及场上同槽；WP47-A§6.3 L205–209给模仿临时/写生持久、无真实菜单、失败不回滚。两者同槽状态的受限对照，未强称写生调用通用学习入口。'),
(244,241,'PASS','SHARED_DATA','WP64§7编辑/导出/管理读写的四元组及Master/Export载体由同文§4 L86–88定义，真实数据合同。'),
(244,243,'PASS','ACTUAL_CALLEE','WP64§7 L128管理Receive实际替换/追加玩家队列后立即按§6领取，L132共享P前缀例依赖该实际入队。'),
(244,263,'FAIL','WRONG_TOOL_FAMILY','263有效WP73-A§4 L77–169仅训练家类型/训练家/道具/物种/metadata/dex六类PBS编辑器；244是WP64§7独立MysteryGiftMaster/Export编辑器，未用该六类保存链，WP64§10也未列WP73。共同作者工具身份不构成这条功能依赖。'),
(244,265,'FAIL','WRONG_CANCELLATION_CONTRACT','265有效WP73-A§6 L177–192仅汇总上述六类及属性子结构的登记/.dat/PBS确认/重载；244的GiftMaster/会话/Export/线上四层及共享P取消行为由WP64§7自有合同，不能从PBS编辑取消汇总转授。未给明示对照用途。'),
(723,177,'PASS','SHARED_STATE_AND_CONTRAST','WP27§2.2 L71明确每槽显示2/3而数量查询5；177§3 L79/98给跨槽累计和槽位操作，连接正确但不把累计查询值当每行显示。'),
(723,722,'PASS','SHARED_DATA','722§2.1 L57–60定义Consumable和ShowQuantity独立三态/重要门，723消费该定义而不反授数量显示为消耗属性。'),
(739,29,'PASS','ACTUAL_CONSUMER','WP42§4 L89–91逐级学习先换持久及场上对应槽；与739的持久/临时PP及新学习槽交界一致。'),
(739,191,'PASS','ACTUAL_CONSUMER','WP28§5.2 L222/225主动PP按身份相同/非变身同步，消费739专门关联规则，和576持物例外不同。'),
(739,204,'PASS','ACTUAL_CONSUMER','WP30§4.3 L113逐升级学习和L114招式变更形态复检属于739 L166战中学招同步的真实触发者，不将纯EV分配当PP写入。'),
(739,207,'PASS','ACTUAL_CONSUMER','WP30§6.1 L156–157新增/替换后上场对象同步及新PP，正是739 L166对应槽更新。'),
(740,31,'PASS','ACTUAL_CONSUMER','WP42§6 L177–181正常终局读取更新后I且按真实玩家参与集合/索引还原，含伙伴捕获错配，符合740 L196–201。'),
(740,61,'PASS','SHARED_STATE_AND_PRODUCER','WP47-B§5 L120/124及L130–150给C写穿、I永久清除/取得、暂时打落保留和转移/消费操作，是740 L194–195还原记录真实生产。'),
(740,528,'PASS','STAGE_AND_IDENTITY_CONTRAST','WP38§5 L102明确捕获时持物不改、满队按当前持物送盒，是否退出还原依集合是否同步；对应740捕获对象/旧成员身份边界。'),
(740,529,'PASS','ACTUAL_CONSUMER','WP38§6 L111–115实际送盒/移出/记录左移与入队回填I，伙伴参与集合错配直接消费740规则。'),
(740,577,'PASS','ACTUAL_PRODUCER','WP50§5有效L110 STICKYBARB转移可写I；L119 JABO/ORAN消费示例分别更新C/I/R/P/Belch。571等中央消费合同另在其它节，但本目标确有真实更新点，不凭整篇名接受。'),
(741,31,'PASS','ACTUAL_CONSUMER','WP42§6/§6.1 L172–177/195–197给胜/败金额及捕获两阶段实际余额统计，真实调用WP24§4.4。'),
(741,421,'FAIL','WRONG_STATISTICS_GROUP','FR421有效WP06 stats§7 L88–103为商店金额/件数、币、BP、煤灰11字段；741的battle_money_gained/lost实际在§6 L82–83/FR420。货币标题不能替代实际字段。'),
(741,579,'PASS','EXPLICIT_PARENT_CHILD_NAVIGATION','579有效范围排除L167，但显式excluded_child_refs755精确拥有该行EXP.SHARE/AMULETCOIN/LUCKINCENSE及世界持物输入；741经579→755可达奖金标记，按合同允许该间接导航。'),
(742,263,'PASS','SHARED_TRAINER_CREATION','WP73-A§4.1/4.2 L84/91含同一训练家类型/交互新建：版本0–255、首只必录、嵌套类型即时落盘。742 WP24§5.3 L164–169真实走这些新建入口，区别于Gift工具。'),
(742,265,'PASS','SHARED_SAVE_CANCEL_BOUNDARY','WP73-A§6 L181–182/190限定训练家类型即时保存、训练家外层确认及不回滚已写PBS；742新建同构作者训练家及可选保存，需此具体分层，不推广所有取消。'),
]
expected={(x['feature_id'],t) for x in rows for t in x['dependencies']['feature_refs']}
observed={(fid(s),fid(t)) for s,t,_,_,_ in judgments}
assert expected==observed and len(judgments)==len(expected)==57

texts={}
def document(path):
    if path not in texts: texts[path]=read(path,A)
    return texts[path]

edges=[]
for s,t,v,kind,reason in judgments:
    sf=features[fid(s)];tf=features[fid(t)]
    child_ids=tf['functional_scope']['excluded_child_refs']
    target_identity=dict(commit=A,document=tf['source']['document'],
                         file_sha256=sha(document(tf['source']['document'])),
                         effective_ranges=tf['functional_scope']['line_ranges'],
                         explicitly_excluded_child_refs=child_ids)
    edges.append(dict(source_feature_id=fid(s),target_feature_id=fid(t),verdict=v,
                      candidate_pointer='/features/'+str(m['features'].index(sf))+'/dependencies/feature_refs/'+str(sf['dependencies']['feature_refs'].index(fid(t))),
                      relationship=kind,limited_actual_use=reason,
                      source_effective_scope=sf['functional_scope'],target_effective_scope=target_identity,
                      explicit_child_targets=[dict(feature_id=i,document=features[i]['source']['document'],effective_ranges=features[i]['functional_scope']['line_ranges']) for i in child_ids],
                      unchanged_R1_row_is_not_semantic_proof=True))

new_affected=[fid(244),fid(741)]
fresh_ranges={
'creature-rpg/wp24-player-trainers-partners.md':[[89,172]],
'creature-rpg/wp20-hp-status-moves-helditem.md':[[172,205]],
'creature-rpg/wp27-bag-and-item-storage.md':[[45,105]],
'creature-rpg/wp30-growth-learning-and-friendship.md':[[79,125],[154,158]],
'creature-rpg/wp64-mail-and-mystery-gift.md':[[84,133],[157,174]],
'engine-overworld/wp12-terrain-movement-vehicles.md':[[92,181]],
'pokemon-rules/wp61-field-passive-effects-and-blackout.md':[[22,57]],
'pokemon-rules/wp23-shadow-hyper-and-purification.md':[[74,85]],
'combat-requirements/wp47-a-move-attributes-targeting-and-calling.md':[[203,212]],
'combat-requirements/wp47-b-switching-control-and-item-changes.md':[[116,159]],
'combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md':[[59,96]],
'pokemon-rules/wp38-capture-and-receiving.md':[[81,119]],
'pokemon-rules/wp50-held-item-triggers-and-consumption.md':[[8,32],[122,170]],
'generic-kernel/wp06-stats-directory.md':[[55,103]],
'demo-dx/wp73-a-content-editors.md':[[1,17],[77,169],[177,192]],
}
fresh_ledger=[]
for short,ranges in fresh_ranges.items():
    path='deliverables/final-specification-set/'+short
    b=document(path)
    fresh_ledger.append(dict(path=path,commit=A,bytes=len(b),sha256=sha(b),new_semantic_read_ranges=ranges,
                             limitation='仅此处区间为本次补核新读，其余沿首份结果的有身份信用或先前新读。'))
supplement=dict(candidate_commit=C,current_source_commit=A,status='FROZEN_AFTER_COMPLETE_57_EDGE_REVIEW',
                scope=dict(active_rows=122,rows_with_feature_refs=17,edges=57,rows_without_feature_refs=105),
                verdict_counts=dict(PASS=sum(x['verdict']=='PASS' for x in edges),FAIL=sum(x['verdict']=='FAIL' for x in edges)),
                failed_outgoing_feature_ids=sorted({x['source_feature_id'] for x in edges if x['verdict']=='FAIL'}),
                new_same_root_affected_ids=new_affected,
                edges=edges,
                target_identity_ledger=[dict(document=p,commit=A,sha256=sha(b),bytes=len(b)) for p,b in sorted(texts.items())],
                supplemental_reading_ledger=fresh_ledger,
                reading_method='固定Git当前908正文；七变更行与此前consumer新读信用加本次完整源节/目标有效范围定向阅读。新增阅读含WP24§4–5、WP20§6.4、WP27§2.1–3、WP30§4/§6.1、WP64§4/§6/§7/§10，WP12§4、WP61§3、WP23§6、WP47-A§6.3、WP47-B§5、WP38§5–6、WP50§2/§5/§7、stats§6–7、WP73-A§1/§4/§6。没有宣称其它131全文本轮新读。',
                qualification='57边逐边实际用途判断，与115个R1 PASS整行保全不同。允许实际共享、明确对照、父→excluded_child_refs导航；外域错出站不反授目标失败。业务/参考/宿主执行0。',
                supplemental_read_error='一次只读探索误将WP61放engine-overworld路径，git show拒绝；随后以固定pokemon-rules正确路径读取。无错误阅读信用。')

result_path=OUT/'creature-results.json'
r=json.loads(result_path.read_text())
new_reasons={fid(244):'同根因全57边补核：礼物数据241和管理Receive→领取243真实；但263/265仅六类PBS内容编辑器及其取消/.dat/PBS链，WP64§7的GiftMaster/会话/Export/线上四层不在其有效scope。旧PASS整行未变不能证明这两条功能依赖。',fid(741):'同根因全57边补核：正常终局31与579→excluded755奖金标记导航真实；421有效scope仅商店/币/BP/煤灰11字段，战斗battle_money_gained/lost在420的stats§6 L82–83，故421为错统计组。'}
for key in ['active_feature_results','old_feature_results']:
    for x in r[key]:
        i=x['feature_id']
        if i not in new_reasons: continue
        x['reason']=new_reasons[i];x['review_mode']='ALL_FEATURE_REF_EDGES_SEMANTICALLY_REREAD_SAME_ROOT_PROPAGATION'
        if key=='active_feature_results': x['verdict']='FAIL';x['dependency_semantics']='FAIL'
        else: x['new_verdict']='FAIL'
        x['finding_refs']=['R2-CRE-DEP-002']

new_cases=[]
for s,t in [(244,263),(244,265),(741,421)]:
    edge=next(x for x in edges if x['source_feature_id']==fid(s) and x['target_feature_id']==fid(t))
    new_cases.append(dict(feature_id=fid(s),wrong_target_feature_id=fid(t),candidate_pointer=edge['candidate_pointer'],
                          source_document=features[fid(s)]['source']['document'],source_lines=features[fid(s)]['functional_scope']['line_ranges'],
                          target_document=features[fid(t)]['source']['document'],target_effective_ranges=features[fid(t)]['functional_scope']['line_ranges'],
                          reason=edge['limited_actual_use'],necessary_fix='更换统计目标为FR420（WP06 stats§6）；保留正常终局和显式奖金标记子导航。' if s==741 else '删除不相干263/265；确需共享输入/列表能力时指向其真正拥有者并说明实际调用，不把六类PBS编辑器保存/取消语义转授礼物工具。'))
r['new_findings']=[x for x in r['new_findings'] if x['finding_id']!='R2-CRE-DEP-002']
r['new_findings'].append(dict(finding_id='R2-CRE-DEP-002',severity='P3',verdict='FAIL',original_issue_id='R1-CRE-DEP-001',
                              title='未变PASS行仍含礼物工具族和战斗统计组的错误功能引用',candidate_commit=C,
                              candidate_path=P+'routing-manifest.json',feature_ids=new_affected,cases=new_cases,
                              required_fix='按真实有效scope修复244的263/265及741的421出站引用；分类、稳定ID、source和父子范围不需改。'))
r['summary'].update(old_PASS=112,old_FAIL=4,active_PASS=117,active_FAIL=5,r1_new_PASS=5,r1_new_FAIL=1,
                     r1_PASS_rows_inherited_exactly=113,r1_PASS_rows_byte_preserved=115,r1_PASS_same_root_reopened=2,
                     feature_ref_rows_checked=17,feature_ref_edges_checked=57,feature_ref_edges_PASS=51,feature_ref_edges_FAIL=6)
r['issue_results'][0]['same_root_affected_PASS_cases']=[dict(feature_id=i,r1_verdict='PASS',verdict='FAIL',reason=new_reasons[i],finding_refs=['R2-CRE-DEP-002']) for i in new_affected]
r['issue_results'][0]['finding_refs']=['R2-CRE-DEP-001','R2-CRE-DEP-002']
r['same_root_propagation']['additional_failed_ids']=new_affected
r['same_root_propagation']['all_nonempty_feature_ref_edges_crosschecked']=True
r['same_root_propagation']['crosscheck_file']='creature-dependency-crosscheck.json'
r['dependency_crosscheck']='creature-dependency-crosscheck.json'
r['supplemental_reading_ledger']=fresh_ledger
r['scope_qualification']='原组CK-TOOLS的工具分责/用户范围门facet仍PASS；244新增依赖facet FAIL单列R2-CRE-DEP-002。原CK-DEP仍FAIL并记录同根传播244/741，不重计原组。'
(OUT/'creature-dependency-crosscheck.json').write_text(json.dumps(supplement,ensure_ascii=False,indent=2)+'\n')
result_path.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')

report_path=OUT/'creature-report.md'
report=report_path.read_text()
report=report.split('\n## 补充全边语义复核：R2-CRE-DEP-002')[0].rstrip()+'\n'
report=report.replace('**122 active：119 PASS / 3 FAIL / 0待查；116原ID：113 PASS / 3 FAIL。6个R1新增全部PASS。','**122 active：117 PASS / 5 FAIL / 0待查；116原ID：112 PASS / 4 FAIL。6个R1新增5 PASS / 1 FAIL（741）。')
report=report.replace('三条失败均限依赖用途，全部122行分类、历史source和有效范围继续PASS。','五条失败均限依赖用途，全部122行分类、历史source和有效范围继续PASS。')
report=report.replace('六个R1新增722/723/739/740/741/742全部整行相同且源不变，按原源范围、职责、父子排除关系及本轮影响分析继承PASS。','六个R1新增722/723/739/740/741/742全部整行相同且源不变；逐边语义补核后741依赖FAIL，其余五项PASS。')
for i,reason in new_reasons.items():
    prefix='| '+i+' | '
    lines=report.splitlines()
    for n,line in enumerate(lines):
        if line.startswith(prefix) and ('| 是 |' in line or '| R1新增 |' in line):
            member='是' if i==fid(244) else 'R1新增'
            lines[n]=f'| {i} | {member} | PASS → FAIL | 全边新读 | {reason} |'
    report='\n'.join(lines)+'\n'
addition='''
## 补充全边语义复核：R2-CRE-DEP-002 · P3

本域非空feature_refs实际为17行/57边，全部逐边对照目标**有效scope**，不是以115个R1 PASS整行保全代替语义。51条边PASS、6条边FAIL，落在186/190/192及新增受影响244/741共5行。

- **FR244→263/265 FAIL**：WP64§7是神秘礼物自有编辑/管理/导出，四层为GiftMaster、当前会话、Export和线上；WP73-A§4 L77–169及§6 L177–192仅训练家类型/训练家/物品/物种/metadata/dex六类PBS编辑器与其登记/.dat/PBS保存和取消。WP64§10 L157未列WP73。仅同为工具、同有取消不构成实际功能依赖。241礼物载体和243管理Receive调用领取的边正确。
- **FR741→421 FAIL**：WP24§4.4的战斗金钱累计字段是WP06 stats§6 L82–83 `battle_money_gained/lost`，属于FR420；421§7 L88–103只有商店金额/件数、币、BP与煤灰11字段。需改真实统计组。
- **FR741→579 PASS（显式间接）**：579本体排除L167，但579.excluded_child_refs明确指755，755精确拥有该行AMULETCOIN/LUCKINCENSE世界持物输入。此导航按合同允许，不要求重复直连或再造ID。
- **FR742→263/265 PASS**：缺失训练家新建实际共享训练家类型/训练家交互建队与保存链；WP73-A L84/91及L181–182/190有具体入口和嵌套写盘前缀，与Gift工具的错族区别明确。

其余739的成长/主动PP/学习四边、740的终局/物品生产/捕获五边、723的逐槽数量对跨槽累计对照、153煤灰/跑鞋/结算导航、204 Shadow分支、207模仿/写生槽位对照均有逐边限定用途。完整57边指针、理由、目标实际范围、显式子导航及固定文件身份见[creature-dependency-crosscheck.json](creature-dependency-crosscheck.json)。

最终计数以本节和results更新为准：117/5 active，112/4原ID，R1新增5/1。115个旧PASS完整字节仍保全，其中113语义继承，244/741因同根传播重开；没有把错误外域出站引用反授为其目标失败。原7组仍6PASS/CKDEP FAIL：CK-TOOLS原分责/范围门facet保留，新增244依赖问题单列。仅补跑文档/Git/JSON静态边集核对，无业务执行。
'''
report_path.write_text(report+'\n'+addition+'\n复现顺序为先creature-audit.py的初始源身份/行差分收集，再creature-dependency-crosscheck.py的完整57边语义补核；最终裁定以补核后的creature-results.json和本报告为准。\n')
print(json.dumps(dict(edge_counts=supplement['verdict_counts'],failed_rows=supplement['failed_outgoing_feature_ids'],summary=r['summary']),ensure_ascii=False))
