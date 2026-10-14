"""Own finite Markdown/JSON receipt formatter; no reference code or behavior model."""
import copy
import datetime
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path('/workspace/pokemon-essentials-clean-room')
BASE = ROOT/'review/remediation-sixth-20261014-prepare/actual-reviews/group-D/peers/u10'
OUT = BASE/'final-increment'
FINAL = '86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
PRIOR = '9d5b4e99b617828690e6529b77a1e555d7c9eb1b'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
prior = json.loads((BASE/'peer-review.json').read_text())
validation = json.loads((OUT/'identity-validation.json').read_text())
ledger = [json.loads(x) for x in (OUT/'reading-ledger.jsonl').read_text().splitlines()]

def save(name, value):
    (OUT/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')

def merge(intervals):
    result = []
    for a, b in sorted(intervals):
        if result and a <= result[-1][1]+1:
            result[-1][1] = max(b, result[-1][1])
        else:
            result.append([a,b])
    return result

payloads = {}
semantic_delivery_exceptions = {
    0:{'qualification':'Outer output truncated; full U13 scope semantics are supplied by standalone delivery1, not this delivery.', 'numeric':[], 'pointers':[]},
    27:{'qualification':'Last source output outer-truncated;275–304 visible in this delivery and224–274 subsequently reread in delivery28.', 'numeric':[[275,304]], 'pointers':[]},
}
for i, entry in enumerate(ledger):
    key = (entry['kind'], entry['commit'], entry['path'], entry['sha256'])
    if key not in payloads:
        payloads[key] = {k:entry[k] for k in ['kind','commit','path','bytes','lines','sha256','git_blob','git_entry']}
        payloads[key].update(delivery_indexes=[], delivered_numeric_intervals=[], delivered_json_pointers=[], semantic_numeric_intervals=[], semantic_json_pointers=[], UTC_first=entry['utc_start'], UTC_last=entry['utc_end'])
    p = payloads[key]
    p['delivery_indexes'].append(i)
    p['UTC_last'] = entry['utc_end']
    for selector in entry['selectors']:
        if re.fullmatch(r'\d+:\d+', selector):
            p['delivered_numeric_intervals'].append(list(map(int,selector.split(':'))))
        else:
            p['delivered_json_pointers'].append(selector)
    exception = semantic_delivery_exceptions.get(i)
    if exception:
        p['semantic_numeric_intervals'].extend(exception['numeric'])
        p['semantic_json_pointers'].extend(exception['pointers'])
    else:
        for selector in entry['selectors']:
            if re.fullmatch(r'\d+:\d+', selector):
                p['semantic_numeric_intervals'].append(list(map(int,selector.split(':'))))
            else:
                p['semantic_json_pointers'].append(selector)
for p in payloads.values():
    p['delivered_numeric_intervals'] = merge(p['delivered_numeric_intervals'])
    p['delivered_json_pointers'] = sorted(set(p['delivered_json_pointers']))
    p['semantic_numeric_intervals'] = merge(p['semantic_numeric_intervals'])
    p['semantic_json_pointers'] = sorted(set(p['semantic_json_pointers']))
    p['own_semantic_full'] = p['semantic_numeric_intervals']==[[1,p['lines']]] or '' in p['semantic_json_pointers']
    p['qualification'] = 'Direct semantic intervals/pointers only. Full-byte/hash computation is separate from semantic coverage.'

coverage = {
    'schema':'R6_ACTUAL_FINAL_INCREMENT_DIRECT_READING_V1',
    'logical_identity':'/root/storage_review', 'UTC_written':now,
    'delivery_records':len(ledger), 'direct_payloads':len(payloads),
    'UTC_first':ledger[0]['utc_start'], 'UTC_last':ledger[-1]['utc_end'],
    'full_new_actual_formal_direct':['WP66-A 1–267','WP54 1–156','WP55 1–150','facility catalog 1–177','WP53 1–288'],
    'final_other_actual_direct':['WP67-A 224–232 / 302–305','UI catalog 224–242 / 947–1011'],
    'payloads':list(payloads.values()),
    'all_deliveries':ledger,
    'semantic_delivery_exceptions':semantic_delivery_exceptions,
    'identity_only_evidence':'identity-validation.json; no semantic verdict follows solely from identity equality',
    'reused_prior_own_semantic_receipt':{
        'actual_commit':PRIOR,
        'report':{'path':str((BASE/'report.md').relative_to(ROOT)), 'bytes':16221,'sha256':'126f395a779c3a0792331c47bd3c935843c94767d737ebf47d4a6c015c00f3a5'},
        'ledger':{'path':str((BASE/'reading-ledger.jsonl').relative_to(ROOT)), 'bytes':93068,'sha256':'184abbb955f674d5605dc05391a4ebcf75887bbe8e4c5859f91aa03c063f2d4b'},
        'coverage':{'path':str((BASE/'reading-coverage.json').relative_to(ROOT)), 'bytes':115906,'sha256':'491c0d6c0a4f9dbd900759e7962a6127313e6635b65a3181109fa19e551cd580'},
        'qualification':'Same logical reviewer; exact same R and unaffected formal blobs. Old direct full WP18/WP30/WP67-A, all four U10 complete seven-group contracts/originals/counterentries and exact qualified R1–R5 reused. New producer/receiver joins separately fresh-reviewed. Old exclusion and snapshot are not rewritten.',
        'shared_UI_own_prior_spans':[[208,358],[566,938],[947,1011]],
        'historical_qualification':prior['historical_qualification'],
        'original_counterevidence_direct':prior['original_counterevidence_direct'],
    },
    'team_reading_not_claimed_as_own':{
        'shared_UI_remainder':'Old root/evidence coverage belongs to their own receipts; final UI is identical and current root has team coverage. This peer claims only direct spans stated above.',
        'other_groups':'No claim to complete semantic reading or signing of all fourteen batches, all 53 changed files, all U13 IDs, or all 3243 input lines.'
    },
    'new_executions':{'source':0,'Ruby':0,'author_scripts':0,'independent_behavior_model':0,'host':0,'Demo':0,'real_save':0},
}
save('reading-coverage.json',coverage)

common = '合法非 nil 参赛对象、可正常显示/选择，规则及资源正常，无插件/竞争；以下是静态推导，不执行。除特别注明外，各最终成员/队伍/子集规则均通过。'
cases = [
    {'case':'J01-raw-zero', 'premises':common+' 原始 ruleset 默认 minimum=1、number/max=0，A/B 两名可用，未加队伍规则。', 'actions':'选择 A、B，再确认；空确认单列对照。', 'derived':'资格预检 true；选人不施加 UI 上限也不自动 focus；A/B 标注 FIRST/SECOND。两人确认先过 minimum，随后因 maximum=0 返回上限首错误；空确认先报 minimum=1。BACK 返回 nil。', 'source':['Rulesets5–8/31–34/176–223','Party1065–1124'], 'formal':['WP54:19/35–45','WP66-A:132/238','facility:58(Q48)']},
    {'case':'J02-explicit-one', 'premises':common+' explicit setNumber(1)，minimum=maximum=1，两名可用。', 'actions':'Entry A，再试 Entry B，确认。', 'derived':'A 新加入后人数等于1，focus转 CONFIRM；B 在已有一人时被正数 cap 拦，保留 NOT ENTERED；确认返回原 A 对象的列表。', 'source':['Rulesets70–78','Party1090–1124'], 'formal':['WP54:45','WP66-A:132','facility:58(Q48)']},
    {'case':'J03-explicit-three', 'premises':common+' explicit setNumber(3)，minimum=maximum=3，四名合法可用 A/B/C/D。', 'actions':'依次 Entry A/B/C，再试 D，确认；另以仅 A/B 确认为对照。', 'derived':'仅新第三名触发 focus；D 被 cap 拦；确认返回 A/B/C 原对象按 Entry 顺序；两人确认先报 minimum=3。', 'source':['Rulesets70–78/194–223','Party1074–1124'], 'formal':['WP54:39/45','WP66-A:132/238','facility:58(Q48)']},
    {'case':'J04-raw-negative', 'premises':common+' 原始构造 number=-1、minimum=1，六名可用，MAX_PARTY_SIZE=6。', 'actions':'Entry 六人，确认。', 'derived':'原始 number 读取归一化 maximum=6；第六名新增触发 focus；正数 cap 生效；六人可最终通过。工具七人列表先因最终 maximum=6 失败，并不声称默认 UI 可选七人。', 'source':['Rulesets31–34/176–223','Party1090–1124'], 'formal':['WP54:19/45','WP66-A:132','facility:59(Q49)']},
    {'case':'J05-Standard-negative', 'premises':common+' StandardRules(-1)，minimum=1、最终 maximum=6，六名分别满足 StandardRestriction/等级/SpeciesClause/ItemClause，无重复种类或物品。', 'actions':'Entry 六人，确认；工具七人列表另列。', 'derived':'Standard number getter 仍是原值 -1；UI 没有正数 cap，也不会在第六次因 equality 转 focus；最终六人上限仍为6且可通过。七人工具列表先报 maximum 错误；默认 UI 七人可达性未宣称。', 'source':['Rulesets31–34/194–239','Party1090–1124'], 'formal':['WP54:19/45','WP66-A:132','facility:59(Q49)']},
    {'case':'J06-explicit-negative', 'premises':common+' 使用 setNumber(-1)，不是负数构造。', 'actions':'观察 explicit setter 后 Entry/最终范围。', 'derived':'setter 向1截断；minimum=maximum=1，与 J04/J05 构造负数行为分离。', 'source':['Rulesets70–78'], 'formal':['WP54:19/35','facility:15(Q05)/58–59']},
    {'case':'J07-first-error', 'premises':common+' 构造列表分别同时违反多类条件，错误数组初始空。', 'actions':'一次最终 isValid，观测第一个错误与短路。', 'derived':'严格 minimum→maximum→成员规则→队伍规则→子集规则；先命中的失败只追加该首错误并返回 false。预检通过不保证最终人数/最终队伍通过。', 'source':['Rulesets176–223','Party1099–1104'], 'formal':['WP54:35–41','WP66-A:238','facility:41(Q31)']},
    {'case':'J08-order-and-focus', 'premises':common+' 明确 Entry 上限3，A/B/C 已进入。', 'actions':'No Entry B，再 Entry D。', 'derived':'删除后 ordinals 重排 A FIRST/C SECOND；D 第三并刚新加入时 focus；只是当前人数等于 cap 或 Summary 返回不会自动提交或每帧强制 focus。', 'source':['Party1074–1095/1121–1124'], 'formal':['WP54:45','WP66-A:132']},
    {'case':'J09-nil-cancel', 'premises':common+' 已有报名 P；正常返回 nil 的取消。活动 live party 是否为 P 按夹具固定。', 'actions':'调用公共报名包装，EntryScreen 返回 nil。', 'derived':'不调用 setParty，不覆盖 P 或 live party；包装也返回 nil。这不是 false；不触发会话 cancel/end 或全局登记回收。', 'source':['Challenge_Data38–50','BattleChallenge135–136/200–203'], 'formal':['WP54:47','WP66-A:132','WP55:40/48/52–57','facility:94–102(WSW28–30/35–36)']},
    {'case':'J10-empty-tool-return', 'premises':common+' 工具边界/替代场景返回 []，已有报名 P，inProgress=true；不宣称普通最少人数菜单可确认空数组。', 'actions':'调用公共报名包装，返回 []。', 'derived':'[] truthy 因而 setParty([]) 覆盖报名，活动会话立即使 player party=[]；包装 false，因为长度0。不活动时只存报名，后来 start 中 [] 仍 truthy 可替换 party。普通默认 minimum≥1 的空确认失败，不会产生正常成功空列表。', 'source':['Challenge_Data38–50','BattleChallenge200–228','Rulesets194–203'], 'formal':['WP54:47','WP66-A:132','WP55:40/48/52–54','facility:94–96/101']},
    {'case':'J11-normal-range-control', 'premises':common+' explicit range1..3，三可用一不合格，选两人。', 'actions':'Entry 两人后确认；无任何合格成员和 fixed3/只有两合格为对照。', 'derived':'range 内两人可通过并按原对象返回；无合格/最低3但只有两合格在预检返回 nil。range 1..3 与 fixed3 不合并。', 'source':['Rulesets70–78/176–223','Party1065–1139'], 'formal':['WP54:35–45','WP66-A:132/238','UI:227–228(A26/A27)','facility:11(Q01)']},
    {'case':'J12-session-layer-control', 'premises':common+' 报名界面正常取消，与已有正常活动/历史保存状态的 inner cancel/end 分开。', 'actions':'另调用 inner cancel / end，再按 outer end 观察。', 'derived':'inner cancel 可在 oldParty 存在时恢复并 reset；inner end 先赋 oldParty，再判断 inProgress，活动结算才 reset；outer end 另保存挑战累计并 currentChallenge=-1。这些层不能从 nil 返回推成已运行。', 'source':['BattleChallenge79–95/270–304/345–362'], 'formal':['WP55:55–57','facility:102(WSW36)'], 'qualification':'只核与 Entry nil/[] 及取消层接合；不是 GR6-F-001 全域签名。'},
    {'case':'J13-stale-command-negative', 'premises':'固定方法中的 command 是 loop do 块内局部；完整旧反证分别在 Ruby2.6.10 的隔离方法/内存 scene执行，未在本轮执行。', 'actions':'历史重复 Species 的确认拒绝→BACK，与正常成功/空确认失败控制，静态检查每次 loop 局部生命周期。', 'derived':'不支持将上次 Entry command 跨 loop 迭代沿用到拒绝后的 Summary6。旧负证据 Summarycalls=[]、未自动 crash。保存 generator 静态误推及 Ruby/宿主范围限制；不据此新增运行证明或要求复制源结构。', 'source':['Party1073–1139','counterchecks-root-findings.json /counterchecks/1 完整原反例','countercheck-ui-entry-stale-command.json 全文','isolated-entry-rejection-counter.json 全文'], 'formal':['WP54:39/45','WP66-A:132/238']},
]
for case in cases:
    case['classification']='DERIVED_STATIC_NOT_EXECUTED'
    case['verdict']='PASS_SCOPED_STATIC'
save('joint-static-cases.json',{'schema':'R6_F002_JOINT_STATIC_CASES_V1','written_utc':now,'source_commit':R,'actual_commit':FINAL,'default_context':common,'cases':cases,'new_execution':0,'host_validation':'UNVERIFIED'})

results = copy.deepcopy(prior['per_ID_results'])
new_notes = {
    'R6-UI-001':{
        'bidirectional_evidence':'final WP67-A224–232 与 CP01–09 新读；R 及 WP38具名消费者沿精确同身份旧独读复用。消息前删除/消息后记忆与回填仍一致。',
        'acceptance_and_regression':'final UI947–1011完整新读中 CP01–09，正常0/成功目标2、仅N送盒、BACK/禁取消和两个消息局部异常前缀保持；原R1–R5资格按原精确载荷复用，不把未变散列作为实测。',
        'dependencies_and_receivers':'final WP67-A 与原 WP38 控制链保持；新 WP54/WP55 不改变捕获提示或旧成员/记忆观察点。WP38伙伴集合错配仍属另具前提，终局还原不被本项承诺。',
    },
    'R6-UI-002':{
        'bidirectional_evidence':'final WP67-A302–305新读，WP53全1–288新读，双满门79、球消费85、接收90均核；其 final 新存档取消层15/239–247/276不替换球门。',
        'acceptance_and_regression':'final UI947–1011中 SF01–05新读，party1/allboxesfull、party6/allfull、party6/freebox正反控制与扣球后异常前缀保持。WP53 savingdelta有新全文/153行producerdiff检查，未声称重验全GR6-S-001真实存档。',
        'dependencies_and_receivers':'新 WP53消费者全文加入本轮接合，capacity/receive规则没有丢失或被取消的可保存行为推广改变。局部Ball签名不代签其 Bug Contest、saving所有运行资格或 U13其它ID。',
    },
    'R6-UI-PARTY-001':{
        'bidirectional_evidence':'final WP66-A全1–267新读并核182/184；WP18全386沿精确相同 blob旧本人全文复用，UI947–1011中MK01–09新读。新设施 receiver132接合同一UI而不扩Mark入口。',
        'acceptance_and_regression':'MK01–09新读保持缺槽独立ACTION失败、六零正常、组合键优先、编辑副本BACK弃稿及OK写回；U01 Owner/U14Happiness旧组合事实复用，未补齐marks[]。R5动态读取/三行确认资格保持。',
        'dependencies_and_receivers':'新设施 receiver 132已按WP54/WP55/设施177及完整Partyunit联合新审，本轮有界通过，旧9d PENDING_EXCLUDED仍是旧快照事实。该通过不把设施取消传播为Mark取消，也不签其它U13 IDs。',
    },
    'R6-UI-PARTY-002':{
        'bidirectional_evidence':'final WP66-A全新读218/220，WP30旧全文286沿相同 blob复用，UI947–1011中RL01–09新读；设施ordinals与重学Move窗口的顺序消费者分开。',
        'acceptance_and_regression':'RL01–09新读保留overlap[GROWL]不搬移、only[CURSE]前置、重复/已会/配置关闭、取消短确认与教学后统计；A048空候选早失败及C0033/2/来源26、A044双入口原资格精确复用。',
        'dependencies_and_receivers':'WP30/U14友好度相邻组合没有变字；新的设施资格/报名写入不能改重学排序或其true/false。F002的nil[]仅属于具名EntryScreen wrapper，不推广到MoveRelearner取消。',
    },
}
for result in results:
    result['actual_commit']=FINAL
    result['review_phase']='FINAL_INCREMENT_WITH_EXACT_PRIOR_FACT_REUSE_AND_NEW_JOINT_REVIEW'
    result['actual_verdict']='ACTUAL_PASS_SCOPED_STATIC'
    for name, group in result['seven_groups'].items():
        if name in new_notes[result['id']]:
            group['reason']=new_notes[result['id']][name]
        else:
            group['reason']='原同身份七组独审事实复用；最终载荷与9d字节相同，受影响消费者另新审。'+group['reason']
        group['basis']='EXACT_PRIOR_OWN_READING_PLUS_NEW_FINAL_SPANS_AND_CONTEXT'
    result['seven_groups']['independent_adjudication']['reason']='同一非作者身份，四ID全部原提案/反证/消费者及R1–R5在旧9d独审已直接完整按资格读；本轮以精确同R/同blob绑定复用其读事实，新增消费者/接口另直接读。未重跑源/作者模型；未把原SUPPORT、候选PASS、字节相同或团队读集当成当前本人新全文。'

joint_groups = {
    'identity_and_verdict':'GR6-F-002唯一U13/P2 required，本审只签其WP66-A接收器与WP54资格、设施Q/WS条目、WP55取消/登记接合；本轮具名静态范围ACTUAL_PASS_SCOPED_STATIC。原9d pending不重写。',
    'bidirectional_evidence':'完整scope_contracts/1原七组/原提案/反证直接新读，R Rulesets1–323、Party1051–1139完整unit、Challenge_Data1–100、BattleChallenge具名范围。新实际WP54全156/WP66-A全267/设施全177/WP55全150，新行及首错误与源逆向互查。',
    'premises_and_counterexample':'见joint-static-cases.json 13个明确控制：raw0、explicit1/3、raw−1、Standard−1、setter−1、final首错误、ordinal/newEntry focus、nil/[]包装、range和会话层及旧stale反证。默认UI最大6，七人为工具列表反向；所有资源/规则/无插件前提明确。',
    'minimum_revision_contract':'WP54:19/35–47、WP66-A:132/238、facility:Q31/Q48/Q49/WSW28–30/35–36与WP55:40/48/52–57已共同对齐。必要正文修订0；接收器既有单句在新producer加入后重新全文/联合实审，不以stable免接合。',
    'acceptance_and_regression':'0/1/3不混成通用正数上限；raw负数getter=6而Standard getter=-1、两者finalmax6；focus仅人数等于且刚新增；minimum→maximum→member→team→subset firsterror；nil不setParty并nil返回，[]工具边界写报名且false/活动队伍可清空。UIA26/A27和旧R1 fixed3/仅2可用预检资格保持。',
    'independent_adjudication':'新读9971精确candidate对应411b独审全文74，WP54/QC/WP55/WP53实际与其mirror完整字节相同。生产者PASS是候选入口绑定，实际结论仍来自本文新context审；保留旧3ef全局FAIL/局部F002资格及两份反对stale-command证据，Ruby历史未重跑也不作为宿主证明。',
    'dependencies_and_receivers':'新WP54定义提供最终约束/firsterror，WP66-A提供UI cap/focus/order与包装，WP55提供提交/活动party/取消层，facility为所有控制的可审目录；彼此相容。未签U13其它7IDs、WP56/58、完整保存执行或公共行政registry。',
}

failures = [
    {'attempt':'Initial final commit/tree/path lookup before root restoration', 'results':['git rev-parse86bbc^{tree} exit128 unknown revision','git rev-parse86bbc:deliverables/final-specification-set exit128 unavailable path because object missing','git ls-tree86bbc exit128 not a tree','final input absent in then-worktree'], 'resolution':'Parent restored exact final/9971/411b refs, then fixed final tuples read; no source execution/git mutation by this peer.', 'UTC':'NOT_CAPTURED_DO_NOT_BACKFILL'},
    {'attempt':'Initial combined input reconstruction and /scope_contracts/1 delivery','result':'Outer output truncated; full U13 scope pointer reread alone. No claim of full all3243input semantics.', 'UTC_context':'2026-10-14T16:47:03 UTC corrected full scope'},
    {'attempt':'WP55 and old U13 report locator searches','result':'Output truncated; locator is not semantic coverage, exact oldreport1–30/49–61 and finalWP55full1–150 subsequently read.', 'UTC':'NOT_CAPTURED_DO_NOT_BACKFILL'},
    {'attempt':'Initial producer-delta.diff printing','result':'Outer output truncated; complete153 lines reread at16:53:36. First tool delivery not claimed as semantic full.', 'UTC_context':'2026-10-14T16:53:36 UTC corrected complete diff'},
    {'attempt':'Combined WP66-A tail + WP55 full + BattleChallenge224–304','result':'Final source portion outer-truncated;224–274 reread,275–304 previously visible. WP66-A and WP55 full deliveries visible; source union224–304 covered.', 'UTC_context':'2026-10-14T16:53:36 UTC source supplement'},
]

report = {
    'schema':'R6_GROUP_D_FINAL_INCREMENT_NON_AUTHOR_U10_V1','written_utc':now,
    'logical_identity':'/root/storage_review','role':'Independent non-author group-D U10 final increment peer','author_of_candidate':False,
    'only_write_directory':str(OUT.relative_to(ROOT)),
    'requested_configuration':{'model':'gpt-6.1-sol','reasoning_effort':'ultra','service_tier':'default','speed':'default','Fast':False},
    'effective_configuration':{'model':'UNVERIFIED','reasoning_effort':'UNVERIFIED','service_tier':'UNVERIFIED','speed':'UNVERIFIED','Fast':'UNVERIFIED','platform_UUID':'UNVERIFIED','reason':'No effective platform echo; no CLI/config/authentication probes or silent switch.'},
    'actual':{'commit':FINAL,'workspace_tree':'67e8c55d520fa8cad2928cb4b95e24c3ed602d5a','formal_tree':'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c','input':validation['input'],'R_commit':R,'R_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','prior_actual':PRIOR,'fixed_main':'8ea169fbd0f33f378b5d732fd6bea59e854e04a6'},
    'per_ID_results':results,
    'joint_interface':{'id':'GR6-F-002','primary_batch':'R6-U13','classification':'required','severity':'P2','actual_verdict':'ACTUAL_PASS_SCOPED_STATIC','bounded_scope':'WP66-A/WP54/facility test catalog plus WP55 registration/cancel join; not all U13 IDs','seven_groups':{k:{'verdict':'PASS_SCOPED_STATIC','reason':v} for k,v in joint_groups.items()},'cases':'joint-static-cases.json','required_repairs':[], 'prior_snapshot_state':'PENDING_EXCLUDED_IMMUTABLE_AT_9d','current_state':'BOUNDED_CURRENT_FINAL_JOIN_REVIEWED_STATIC_PASS','formal_acceptance':False,'CLOSED_registered_by_this_peer':False},
    'producer_binding':{'candidate':'9971fe84896786645cdcda3ab45e5caf7785cabc','candidate_tree':'93ebe95d038954fd0dfb14fd07ac2f95a2485baf','mirror_tree':'13d502e4131ace3e8fe2e59ce07a338b98ff7967','independent_review':'411b563309a4e642e628dcf8289e36c6fe3fd37f','review_tree':'c34fc75d13828a49322203455073d475431395bc','review_directory_tree':'9c654f8b8cd59c427989bea23958bdd360dcee1c','report_path':'review/remediation-sixth-20261014-prepare/reviews/R6-U13-R/repair-01/review-report.md','report_bytes':11273,'report_sha256':'1445036698ffb92561fd87c121310ee65dac157f038b7ab098e5ccb21710970a','report_blob':'04df5bf6c83056ed44697f379a306ed5f3476d32','report_new_direct_full':'1–74','qualification':'Exact repaired-candidate PASS only; original global FAIL remains. Own actual joint review is separate; author/reviewer reported thread IDs are provenance and not this peer effective UUID.'},
    'necessary_repairs':[], 'cross_file_result':'PASS_SCOPED_STATIC_ON_NAMED_U10_AND_F002_JOIN',
    'source_and_semantic_limits':{'source_objects_read_only':True,'no_source_checkout':True,'full_input_all3243_lines_claimed':False,'new_full_actual_formal':coverage['full_new_actual_formal_direct'],'source_Runtime_host':False,'stale_command_negative':'Historical Ruby2.6.10 isolated method evidence directly read and kept with environment limitations. Generator stale-local assertion contradicted; no runtime this turn; source-local lifecycle reasoning not a future architecture requirement.'},
    'prior_qualification_reused':coverage['reused_prior_own_semantic_receipt'],
    'old_snapshot_exclusion':'Old9d report and its F002 PENDING_EXCLUDED never rewritten; this supplement signs final86bbc bounded interface after new producer and full/joint review.',
    'excluded_scope':['U13 other seven primary IDs/all56 whole-result','full behavior/host/Demo/real save execution','media/fonts/physical input/clock save conversions','administrative public registry syncing and exact registry review','formal acceptance/CLOSED'],
    'administrative_sync':'R6-I retains deferred public planning/audit synchronization; input state and null acceptance not mutated.',
    'formal_acceptance':False,'CLOSED':False,'new_executions':coverage['new_executions'],
    'read_failures_and_truncation':failures,
    'future_revision_boundary':['Any change to WP66-A/WP54/facility catalog requires exact new tuple full-file joint review; same filename/candidatePASS/file stable does not transfer.', 'WP55 registration/active party/cancel/end changes require new wrapper and lifecycle joins; nil versus empty and truthiness/final minimum must remain distinguished.', 'WP53 or WP67-A Safari capacity/receive/settlement change requires renewed U10 Safari source/consumer/counter/control review; new saving scope does not automatically inherit.', 'WP18/WP30/WP66-A Mark/Relearn changes require affected normal/negative/vector and exact qualified R1–R5 checks. Unchanged exact blobs may reuse direct facts, but new combination is separately reviewed.'],
    'reading_evidence':{'ledger':'reading-ledger.jsonl','coverage':'reading-coverage.json','identity_validation':'identity-validation.json','producer_delta':'producer-delta.diff','records':len(ledger),'payloads':len(payloads),'UTC_first':coverage['UTC_first'],'UTC_last':coverage['UTC_last'],'direct_vs_reused_vs_team_explicit':True},
    'AGENTS':{'path':'AGENTS.md','prior_direct_full':'1–297','bytes':6328,'sha256':'41cea9c6aa439dc70eaca2c26ce1f7967a887538c1aef25b9297c07b0437ff40','blob':'07b3655388c7405ec32aeb12e143db10a5e28c81','current_same_hash_verified':True,'nested_applicable':'none found','local_skills':'.agents absent; no related local skill','writes':'only final-increment; no old peer/candidate/formal/public/git writes'},
}
save('peer-review.json',report)

md = [
    '# group-D / U10 最终快照增量非作者复审',
    '',
    '四项 U10 及具名 **GR6-F-002 联合接口均为 ACTUAL_PASS_SCOPED_STATIC**；必要正文修订 **0**。只签最终快照 `'+FINAL+'` 的静态范围。旧 9d 报告和 F002 的 PENDING_EXCLUDED 保留原样；本补充是在修订生产者加入后的新实际全文与联合复审，不能迁签旧报告。',
    '',
    '审者 `/root/storage_review`，独立非作者，未撰写被审候选正文。请求 gpt-6.1-sol / ultra / default tier / default speed / Fast=false；有效 model、effort、tier、speed、Fast、平台 UUID 无回显，全部 **UNVERIFIED**。未运行 CLI/config/auth 探测或另开代理。',
    '',
    '## 固定对象、增量和生产者',
    '',
    '- final commit `'+FINAL+'`，workspace tree `67e8c55d520fa8cad2928cb4b95e24c3ed602d5a`，formal tree `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`。',
    '- prior actual `'+PRIOR+'`，tree `faae3b9a22c37a2e2e994553f59e7099c6394db0` / formal tree `74dccc64506d008d50cf1cdfd906f701931020cc`；固定 main `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`。',
    '- R `'+R+'` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`；全部以 git show 固定对象只读，没有源 checkout、修改或执行。',
    '- final input `integration/U01-U14-final-composite-20261014/actual-review-input.json`：152860 bytes，3243 行，SHA256 `4671c1c31f18858a7719e88533029d746c62dfb77d4239cbb0cae633e79863da`，blob `ccf79b03165573f27070a417a2e3d986907f6623`。完整读取本组/U13批、具名文件节点、完整 delta_from_prior_actual、receiver/根编辑、状态/要求/排除/行政节点；不宣称全部其它批或全3243行语义阅读。',
    '- U13 repaired candidate `9971fe84896786645cdcda3ab45e5caf7785cabc`，candidate tree `93ebe95d038954fd0dfb14fd07ac2f95a2485baf`，mirror tree `13d502e4131ace3e8fe2e59ce07a338b98ff7967`；独立 PASS 审 `411b563309a4e642e628dcf8289e36c6fe3fd37f` 的 repair-01/review-report.md **1–74全文新读**，11273 bytes，SHA256 `1445036698ffb92561fd87c121310ee65dac157f038b7ab098e5ccb21710970a`，blob `04df5bf6c83056ed44697f379a306ed5f3476d32`。精确 PASS 仅绑定修订候选；旧 3ef 原始全局 FAIL/局部 F002 接收依赖仍保留，本人新读该报告1–30及49–61。',
    '',
    'WP54、WP55、设施目录、WP53实际完整字节与上述 PASS 候选镜像一致。生产者 PASS 是入口资格，实际裁决来自本次新全文、固定源和控制接合。五个 U10贡献文件与9d完全同字节，原replace/insert保留事实按旧精确receipt复用；WP66-A虽同blob仍按根要求重新全文读267行。机器核验不等于语义 PASS。',
    '',
    '## 直接新读与准确复用',
    '',
    '| final 正式文件（deliverables/final-specification-set/ 下） | 本人本轮直接语义读 | bytes | SHA256 | blob |',
    '| --- | --- | ---: | --- | --- |',
]
for suffix in ['wp54-entry-eligibility-level-adjustment-and-clauses.md','wp55-facility-session-and-restoration.md','combat-requirements-wp54-55-56-58.md','wp53-safari-and-bug-catching-contest.md','wp66-a-party-and-summary-ui.md','wp67-a-battle-interaction-and-presentation.md','user-interface-wp17-63-65-66-67-68-69-70-71.md']:
    p = next(p for p in payloads.values() if p['commit']==FINAL and p['path'].endswith('/'+suffix))
    spans='全文1–'+str(p['lines']) if p['own_semantic_full'] else ' / '.join(str(a)+'–'+str(b) for a,b in p['delivered_numeric_intervals'])
    md.append('| '+p['path'].split('final-specification-set/')[1]+' | '+spans+' | '+str(p['bytes'])+' | '+p['sha256']+' | '+p['git_blob']+' |')
md += [
    '',
    'WP18全1–386与WP30全1–286沿本人旧9d语义全文、同一R/同blob准确复用：分别37612 bytes / SHA256 `a6410f5d3bcdedef2d682bddaeff4d49facef22e297f19b9a908d855893d346c` / blob `63048ab21f8fa5db77df11316f285db13e162594`；32271 bytes / SHA256 `f622dee4cd0fb1bbf89e47ef2c47bcf3c98f16dd12b5dfa48c006d39aec39fc3` / blob `1d6957846328bc5ad228932334c4fa32b02a47e5`。WP67-A旧全348保留，当前关键段另新读。共享UI本人旧208–358/566–938/947–1011复用，当前224–242/947–1011另新读；其余属于root/evidence团队receipt，未虚报本人全1026。',
    '',
    '原 U10 合同四个完整七组/原提案/原反证、完整捕获/Safari原反证、party results0/1及精确R1–R5资格是本人上一轮直接语义读集，原合同120055 bytes / SHA256 `eb86301b11ef040f4a98365b93d8a6649409f32fe095a13974e697fe160d64f0` / blob `c33b84a0308bdd6776bee11dea7ee4243ba301f4`。本轮仅复用这些同身份固定事实，新增消费者与接口重新核。旧 report.md 16221 bytes / SHA256 `126f395a779c3a0792331c47bd3c935843c94767d737ebf47d4a6c015c00f3a5`；旧完整ledger/coverage身份在本轮reading-coverage.json，七份旧载荷完整字节未变核验在identity-validation.json。',
    '',
    '新读 U13 合同完整 `/scope_contracts/1`（全部七组和原提案），文件370944 bytes / SHA256 `f202a22b1faf72a80edd2d663b9326bf4a9b9be4409fe88780835de909b08473` / blob `8c05e33d56064ff5a79ea25545f696b6156f4543`；不称整个6947行合同均语义已读。完整F002原countercheck项及完整两个stale-command负证据也直接新读。工作树合同/证据与final固定对象完整同字节另绑定。新producer字节diff全文153行已读。',
    '',
    'R 本轮新读：Rulesets **1–323全文**；Party **1051–1139完整多选unit**；Challenge_Data **1–100**；BattleChallenge **1–45、79–95、118–143、181–304、345–362**。源payload完整bytes/hash/blob/模式、逐段UTC/cwd/argv/exit、JSON指针和语义区间均在新ledger/coverage，范围外源全文不虚报。',
    '',
    '根AGENTS.md上轮1–297全文（6328 bytes / SHA256 `41cea9c6aa439dc70eaca2c26ce1f7967a887538c1aef25b9297c07b0437ff40` / blob `07b3655388c7405ec32aeb12e143db10a5e28c81`）本轮相同hash核验；未发现适用nested AGENTS，`.agents`缺失。仅写final-increment，不改旧peer、formal、candidate、public或git。',
    '',
    '## 四项 U10 逐 ID 七组裁决',
]
for result in results:
    md += ['', '### '+result['id']+' — '+result['actual_verdict'], '']
    for i,(name,group) in enumerate(result['seven_groups'].items(),1):
        md.append(str(i)+'. **'+name+'**：'+group['reason'])
md += ['', '## GR6-F-002 的新联合接口七组', '']
for i,(name,reason) in enumerate(joint_groups.items(),1):
    md.append(str(i)+'. **'+name+'**：'+reason)
md += [
    '',
    '### 正常、反例与组合控制',
    '',
    '| 静态控制 | 前提与可观察结果 |',
    '| --- | --- |',
    '| raw 默认0 | min1/max0、A/B合法、无队伍规则：预检可true；Entry不封顶，不自动focus；确认2人先max失败，空确认先min失败。不是最终无上限。 |',
    '| explicit1/3 | setter同时固定min/max；新第一/第三人才focus；再选超限成员被Entry门挡；确认返回原对象按Entry順序。fixed3选2最终min失败。 |',
    '| raw−1 / Standard−1 | raw读取归一化6，sixth新Entry可focus且cap生效；Standard读取原−1，无正cap/该focus。最终max都6；七人仅工具反向，不能声称默认6槽UI可选七人。setter−1另截断1。 |',
    '| first error | 最终min→max→member→team→subset；先命中短路只追加首错。预检eligible并未替代最终资格。 |',
    '| ordinals/focus | No Entry中间项后紧缩FIRST/SECOND；加入第三才focus；Summary或仅count相等不自动确认。 |',
    '| nil取消 / []工具返回 | nil不setParty并nil返回，旧报名不改；[]为truthy，覆盖报名且包装false，活动live party立即[]。正常min≥1空确认失败，不宣称菜单能提交正常空列表。 |',
    '| 1..3范围/不可用 | A26三合法一BANNED选2可成功；A27全不合法、R1 fixed3仅2可用预检nil。范围与固定人数分开。 |',
    '| 会话层 | 普通菜单nil取消不调用session cancel/end。WP55 inner cancel可还原oldParty后reset；inner end先赋oldParty再检查inProgress；outer end才另保存累计/currentChallenge=-1。不能混同。 |',
    '',
    '所有正常成员身份、显示、注册、资源、资格规则、默认MAX_PARTY_SIZE=6和无插件/竞争前提，以及各工具边界/受控失败范围，写入joint-static-cases.json。它是人工静态控制记录，13项均 DERIVED_STATIC_NOT_EXECUTED，未执行模型或Ruby。',
    '',
    '### 原反证中的矛盾与历史资格',
    '',
    '原 generator counterchecks-root-findings.json 的F002完整项（文件42012 bytes / SHA256 `0f8df84ee410cfefeed9b64b4a57e7521d709a8aacf39ff2522c9feff704878e` / blob `3a9934a081e66a1d85d0bcb9c523ae4f58778ac3`）正确指出UI cap只在number>0，但第五静态反例把loop块内command误推为跨迭代残留。完整负证据 countercheck-ui-entry-stale-command.json（2442 bytes / SHA256 `320b742ad5bd6f804610535ee08e8de2747a524799ba2bcf98647feaf2b990c0` / blob `6a2ecc27f138a1471e768d128363d6c6f097d7b5`）与isolated-entry-rejection-counter.json（2919 bytes / SHA256 `3f066179f97e0c2ab3974219c395c982944931035f7dfdaae8bea4b748701e71` / blob `fd828c7d156245c4ec5a50da727e7c1e6b810f19`）保留Ruby2.6.10隔离方法/内存scene的正常成功、重复Species拒绝→BACK、空确认失败控制，Summarycalls=[]，支持撤回该stale推断。',
    '',
    '本轮只读其历史载荷并按固定方法块局部生命周期核对，没有重跑历史Ruby或宿主；隔离负证据不证明全部真实UI/宿主版本，也不要求未来保留源结构。首错误失败后保留选择、ret=nil与正常BACK退出相容。',
    '',
    'R1–R5准确历史五元组/静态范围/正常反向及局部失败前缀沿旧独读coverage复用：R1初始CONTINUE_WITH_DEFERRED_FINDINGS和v3具名A–G；R2 B16 candidate356b46b/actual29b21fe/review191e669c（A044/A048 B16主责、C003 B21主责/B16局部）；R3 accepted341 records244/245/250及失败前驱；R4 U03actual-v1的17/76不混成B5的16/75；R5精确13fddb closing、12df activation的92 CLOSED/51 P2/41 P3，不重签全部92行为。',
    '',
    '本轮final WP66-A全文再次核动态形态227、三行确认244、Mark182/184与Relearn218/220；共享UI836–840沿相同blob旧直接读。设施默认min预检/final首错与多选A26/A27不改变原R1资格；U10新RL02重叠顺序仍保旧C0033/2数量、来源26、A048空候选首绘早失败及A044背包/Party双入口；nil/[]的设施返回不会推广到普通Mark/教学返回。媒体/字体/真实时钟/宿主/save/Demo原未知保留。',
    '',
    '## 修订、失败记录与复验边界',
    '',
    '必要正文修订0。输入的根receiver依赖文字仍描述生成时的pending；本审不改该输入，而以此最终receipt限定解决当前86bbc的具名联合静态接口。public planning/audit行政同步和其精确字节审由R6-I后续办理；本文不办理正式接受、CLOSED或所有56项的整体签名。全文阅读设施其它向量/新WP55取消条款不等于代签其它U13七个ID。',
    '',
    '最初final对象/路径不可解析和工作树input缺失保留为对象未恢复时的失败，不能提前定性规范或路径缺陷；根恢复后读取准确tuple。第一次combined scope/input、locator、diff和最后源段输出截断已分段补足；未捕获首失败UTC不倒补，详见peer-review.json。',
    '',
    '本轮有限Git/UTF-8/JSON/diff/receipt工具为本人已知静态读写；源、Ruby、作者脚本、独立完整行为模型、宿主、Demo、真实save执行均0。当前新送达 '+str(len(ledger))+' 次/'+str(len(payloads))+' 个载荷，UTC '+coverage['UTC_first']+' 至 '+coverage['UTC_last']+'；每载荷模式/完整身份/区间/指针/cwd/argv/exit和读集身份全列新coverage。机器同字节与直接语义、原同身份复用、团队阅读明确分列。',
    '',
    '未来WP66-A/WP54/设施目录任一blob改变需准确新tuple和新全文联合核；WP55报名、活动party、cancel/end变更需重验nil/[]与层级；WP53/WP67-A门/接收/结算变更需重验SF；WP18/WP30/Mark/Relearn变更需重验对应正常反例/向量和精确历史资格。未变同blob可复用已读事实，新增组合不能凭文件stable、相同名字或候选PASS继承。',
    '',
    '交付：report.md、peer-review.json、joint-static-cases.json、reading-ledger.jsonl、reading-coverage.json、identity-validation.json、producer-delta.diff，以及本人有限reader/formatter；delivery-validation.json记录包身份。旧9d七份已知载荷完整字节未改。',
]
(OUT/'report.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'UTC':now,'new_deliveries':len(ledger),'payloads':len(payloads),'per_ID':[x['id'] for x in results],'joint':'ACTUAL_PASS_SCOPED_STATIC','required_repairs':0,'source_execution':0},ensure_ascii=False))
