"""Serialize manually adjudicated world/UI review and independently checked identities."""
exec(compile((__import__('pathlib').Path(__file__).with_name('world-ui-audit.py')).read_text(),
             'world-ui-audit.py', 'exec'))

def fid(n): return f'FR-{n:06d}'

# These are manual semantic decisions after the source readings recorded below.
reasons = {
326:'WP11 §6完整恢复/记录表已重读；direct_refs现明确WP09恢复门，原WP03/WP05规划索引保留而不再冒称完整依赖。',
345:'仅路线取证口径与通行主责引用，已完整退役为META-000018；343/344仍承接实际路线行为。',
346:'框架明确拥有参数双键回退、三级种子/无条件清待播和全局重播；MZ拥有建立地图及临时查询/正式转移的接入，源§3全部前缀相符。',
348:'框架明确拥有符号、每格随机、墙偏移及256邻接变体；MZ消费确定图块写三层地图，未把图像可见性等同通行。',
349:'房间尺寸/占格间距、1000次单事件和100轮整体尝试归框架；事件失败抛错与玩家失败保留旧暂存均明确，MZ写坐标并接转移。',
358:'特殊注册表仍只覆盖§2；新增726完整承接原遗漏§1包装/四预置清理/正常恢复，并有358→726明确依赖。',
372:'框架拥有真实转移的概率重掷与类型意图；MZ按类型差异和duration路径显示，正时长不当秒数，源§4.2–4.6已重读。',
373:'框架天气身份/类别与MZ Snow扰动、Storm闪屏、Sun逐帧更新明确分责；可保同一粗行，不须每个粒子新ID。',
374:'框架拥有十二族资格和目的地/开关/统计提交；MZ负责选择、动画、地图/载具/事件操作，徽章/摇树算术父子范围不重叠。',
381:'鱼竿/特性阈值和已到达随机消费归框架；MZ等待/反应采样和更新顺序明确，成功等待不等于实际开战。',
384:'WP60 §7已完整重读；direct_refs具名WP38球倍率、WP39战斗环境及WP42结果，三级请求/候选/开战不混同。',
634:'联系人/版本/双倒计时与持久顺序归框架；MZ列表、实时拖动和消息消费明确，普通/移动模式不同输入顺序保留。',
656:'框架拥有奶招HP及持物/邮件实际提交，MZ处理选择和消息；移位发起旧身份及嵌套取回不回滚的具体前缀已登记。',
659:'direct_refs新增WP30学习/重学和统计主责；完整§7已重读，背包TR与队伍Use不同包装以及重学空候选失败没有改写。',
664:'WP25执行存取/拿起/交换/释放及治疗/最后可战门；MZ负责盒/队伍/暂持显示、动画/确认，退出保留已完成写入。',
666:'框架记录Start先写持久模式和结果BACK归零；MZ维护焦点/本地子页/外层草稿/已接受参数/当前列表，空结果不回滚模式。',
667:'WP62拥有末次性别/形态/异色记录；MZ普通刷新不写，选择器首轮/移动三参写false且取消不回滚，职责与全§7相符。',
673:'框架提交PC存取/丢弃库存先后及部分前缀；MZ数量/确认/取消/消息不撤库存，源§5两种丢弃提示时点保留。',
674:'框架按WP29执行资源、库存过滤/回退和数量提交；MZ商店输入/相机/消息，取消只停止尚未到达提交。',
677:'三方协作明确框架队伍/库存/退出包装，Showdown逃跑尝试/选择登记撤销/阶段决定，MZ输入反馈；PROTO-ESCAPE和具体领域refs齐全。',
678:'三方协作明确Mega身份/席位输入、目标合法查询及登记复检、Fight/Target导航；高亮不等于许可，未冒称固定目标版本支持。',
679:'三方协作明确实时背包扣退、持久效果、登记复检/残留/终局二退和MZ对象选择反馈；PROTO-BATTLE-ITEM接到187/731实际链。',
680:'框架队伍/属主映射，Showdown换入换出及二次登记资格，MZ替补循环分别登记；替补拒绝的逃跑路径绑定PROTO-ESCAPE。',
681:'经验/等级/持久学习归框架，战中收益/暂停及场上招式同步归Showdown，MZ显示/遗忘/放弃；PROTO-IN-BATTLE-GROWTH与739/735双提交相符。',
682:'框架拥有球/图鉴/队伍/盒子及记忆回填，Showdown拥有投球/敌队移除/队列，MZ捕获命名及满队选择；PROTO-CAPTURE区分成功决定与真正接收。',
684:'Safari预算/容量、捕虫暂存、Palace/Arena、回放和调试覆写按三方明确分责，四原型与DEC-SPECIAL-AND-HOST-SCOPE均具名，仍待目标验证。',
687:'框架拥有物种/能力/HP/持物/额外个体/图鉴/学习有序提交，MZ提供演出取消和正常后继；成功消息先于物种写入未丢失。',
688:'WP35孵化前后字段与命名归框架，MZ动画/文本输入/消息生命周期明确；命名拒绝不回滚孵化。',
690:'净化室容器/引用及成长/净化/存放/清中心归框架，MZ组编辑/选择器/窗口更新；跨级与双满前缀未抹平，特殊范围门已传递。',
691:'新增744拥有§7.1克隆/编号/裁剪/PC门持久规则；691范围精确扣139–147，保留登记/浏览呈现；目录→691→excluded_child_refs744为显式间接导航。',
695:'16格固定损伤、特殊资格和生命提交归框架；不按常规生物等级/命中/随机伤害处理，特殊范围仍待决策。',
696:'框架拥有3/13等权重动作与随后台词抽样；MZ先显示台词再询问玩家，包装身份随机和胜负随机没有混并。',
697:'框架拥有10/10会话、玩家零优先终局及特殊资格；MZ不可取消选择和地图速度/朝向请求明确分责。',
699:'框架拥有初始索引及停止滑移抽样，MZ依H/v/t更新已提交顶部且先更新后输入；重玩消费样本后强制0未漏。',
700:'有效线/奖项顺序仍归框架，705有序转轮数据现在同归框架并具名连接；无最终中奖率或首版批准声称。',
701:'场景信用/下注/重玩和取消规则归框架，MZ按DOWN/重玩及状态门采样、等待和显示；不会每次下注写持久余额。',
702:'框架拥有待付/场景信用/上限及正常离场持久净差；MZ逐更新或USE/满额支付，20枚/秒注释不冒称实测。',
703:'入口拒绝及场景异常仍作MZ接入验收；728/702已分别承接准入与余额提交，未许诺异常必结算。',
704:'冻结依赖/配置/未决已退役为META-000030，不再计独立实现功能；保699–705及728实际消费者。',
705:'三轮各22项顺序/频次归框架，沿顶部两个循环前驱消费；不能以频次当最终中奖率，MZ转轮显示在699。',
706:'13项等权/重复不去重铁形状归框架；730另补61主候选表，与铁表范围没有重叠。',
707:'48身份/口袋来源资格完整退役META-000031；不再冒充61候选主表，730补齐真实行为数据。',
708:'候选权重/身份去重及化石/石板互斥仍由框架拥有；730直接引用708/709为主表消费者，61行没有被48身份吞掉。',
709:'框架拥有累计权重、占格/去重、位置内层无上限、铁500次及130层厚抽样顺序；MZ仅初始显示。',
710:'框架拥有工具矩阵、中心铁门、损耗/调试和揭露/待领；41–48时间门已精确扣到767，目录→710→excluded_child_refs767可解释。',
711:'框架拥有坍塌优先/逐件入袋/整批部分成功/裸领取非幂等；MZ确认及逐件反馈，已揭物不被坍塌没收。',
712:'闪光中断/领取部分提交作为接入失败合同保留；709/710/711已明确框架规则权威，不再单凭MZ吞掉结算。',
713:'冻结依赖/配置/不终止及宿主未知完整退役META-000032，关联真实挖矿规则/表现。',
714:'框架拥有模式/尺寸默认、排列/角度/暂持和完成谓词；MZ切图/光标消费，排列仍为唯一局面权威。',
715:'七模式合法动作及完成条件归框架，MZ预渲染或精灵旋转不改变规则；旋转−1 mod4保持。',
716:'框架执行有界合法动作，MZ按具体trigger/repeat/press和独有方向优先序采样；越界也抑制低优先BACK。',
717:'洗牌、实际parity复检/末格漏扫及6/7五步构造归框架，未声称全尺寸可解/均匀或运行重播。',
718:'框架完成/取消/不持久局面与MZ动画/确认已明确，106–119抽出768且父范围扣除；目录→718→excluded_child_refs768可解释。',
719:'资源回退/箭头显示门/切图/音效仍归MZ，714–718框架权威分明，特殊范围待用户决定。',
720:'排列权威、完成范围、尺寸限制和固定奇偶不变量归框架；固定证明不当求解器或运行覆盖。',
721:'框架表外模式/默认尺寸/非方形缺陷/初始完成和空槽规则，MZ资源失败/动画输入阻塞明确分责。',
726:'追加独立战前包装单元，完整覆盖§1 L5–21；框架预置/音乐备忘状态与MZ包装/恢复分别负责，异常不保证恢复。',
727:'追加Duel概念章实际行为：10/10临时生命、布尔胜负/无平局和准入归框架，MZ不可取消输入/角色呈现。',
728:'追加Slot入口三拒/难度单元；框架币盒/余额/上限规则与MZ拒绝反馈/只在准入后建场景分明。',
729:'追加Mining无实参/无额外准入守卫单元；框架会话/库存与MZ场景入口分明，不补不存在的币盒守卫。',
730:'新增范围L9–75完整包含61候选有序身份/权重/矩形/占格及去重；框架拥有并连接706/708/709，无主表遗漏或铁表混计。',
744:'新增§7.1完整持久规则，框架克隆/编号/容量裁剪和PC门，MZ记录提交后演出及BGM失败前缀分责；随存档而非登记即落盘。',
767:'新增§4.1独立MZ输入/工具时间门；框架已提交损耗/挖层/终局，MZ档10忙/档11解锁和清忙先终局、闪光重叠均具体。',
768:'新增§6.1独立MZ动画读回/完成等待；框架离散角度/排列提交与异常保留前缀明确，Input更新不等于受理正常动作。',
}

new_ranges = {
'wp11-map-topology-transfer.md':[[121,159]],
'wp13-move-route-matrix.md':[[80,84]],
'wp14-random-dungeons.md':[[23,105],[220,302]],
'wp16-pre-battle-transitions.md':[[1,147]],
'wp59-world-time-weather-field-moves.md':[[102,283]],
'wp60-fishing.md':[[37,102]],
'wp63-pokegear-map-music-and-phone.md':[[68,134]],
'wp66-a-party-and-summary-ui.md':[[66,133],[196,221]],
'wp66-b-storage-and-pokedex-ui.md':[[88,134],[153,258]],
'wp66-c-bag-item-storage-and-shop-ui.md':[[71,165]],
'wp67-a-battle-interaction-and-presentation.md':[[1,335]],
'wp67-b-lifecycle-presentations-and-history.md':[[1,213]],
'wp68-duel.md':[[1,103]],
'wp69-slot-machine.md':[[1,110]],
'wp69-slot-reels.md':[[1,49]],
'wp70-mining.md':[[1,84]],
'wp70-mining-data.md':[[1,101]],
'wp71-tile-puzzles.md':[[1,190]],
'engine-overworld-wp11-15-59-60.md':[[119,135]],
'user-interface-wp17-63-65-66-67-68-69-70-71.md':[[428,467],[694,746],[899,942],[951,1015]],
}
# Whole-document reads above are clamped to the independently measured file length.
full_reads = {'wp16-pre-battle-transitions.md','wp67-a-battle-interaction-and-presentation.md',
 'wp67-b-lifecycle-presentations-and-history.md','wp68-duel.md','wp69-slot-machine.md',
 'wp69-slot-reels.md','wp70-mining.md','wp70-mining-data.md','wp71-tile-puzzles.md'}
read_ledger=[]
for item in identities:
    path=item['path']; name=Path(path).name; n=item['identities'][2]['line_count']
    ranges=[[1,n]] if name in full_reads else new_ranges.get(name,[])
    read_ledger.append(dict(path=path, fixed_commit=NEW, current_commit=CURRENT,
        full_identities=item['identities'], candidate_and_current_bytes_equal=item['all_four_equal'],
        newly_read_ranges=ranges, inherited_full_read_ranges=[[1,n]],
        inherited_evidence_commit=REVIEW,
        inherited_evidence_path=PREV+'agents/'+('world-catalog-full-results.json' if path in catalog_paths else 'world-ui-results.json'),
        inheritance_basis='旧独立报告逐文完整阅读；本次Git对象/字节身份一致。变化和同根因单元按本账区间重读，未把旧PASS或作者映射自动转授。其余未变源事实信用与本次字段差分合用。',
        limits='本轮只对列明区间新增语义阅读信用；空区间表示本轮未重读正文。未执行业务。'))

consumer_ids=[11,22,31,49,187,206,528,529,530,531,554,555,577,581,596,731,735,739]
consumer_docs={}
for n in consumer_ids:
    f=active_by[fid(n)]; p=f['source']['document']
    consumer_docs.setdefault(p,[]).extend(f['source']['line_ranges'])
for p,ranges in consumer_docs.items():
    read_ledger.append(dict(path=p,fixed_commit=CURRENT,full_identity=identity(CURRENT,p),
        newly_read_ranges=sorted(ranges), inherited_full_read_ranges=[],
        purpose='WP67四原型及目录F02具名跨域消费者；按实际完整source单元读取，不推成全篇复读。'))
extra='deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md'
read_ledger.append(dict(path=extra,fixed_commit=NEW,full_identity=identity(NEW,extra),
    newly_read_ranges=[[1,6],[199,242]], inherited_full_read_ranges=[],
    purpose='跨域F01反向串域复核；其余源全文审阅由pokemon分工负责，本分工只独立读以上区间并核2277–2292全部映射。'))

old_results=[];active_results=[]
old_review_by={f['feature_id']:f for f in previous['feature_results']}
for old in previous['feature_results']:
    key=old['feature_id']; n=int(key[-6:]); f=active_by.get(key,retired_by.get(key)); retired_flag=key in retired_by
    own_reason=reasons.get(n)
    if own_reason is None:
        own_reason='本次逐字段差分确认固定source、功能有效范围及原去向未改变，新增责任/直接合同未否定原粗标；'+old['reason']
    scope=f['source']['document']; rr=next(x['newly_read_ranges'] for x in read_ledger if x['path']==scope)
    source_lines={line for a,z in f['source']['line_ranges'] for line in range(a,z+1)}
    read_lines={line for a,z in rr for line in range(a,z+1)}
    method='NEW_FULL_SOURCE_UNIT_READ' if source_lines <= read_lines else ('INHERITED_FULL_READ_WITH_TARGETED_REREAD' if source_lines & read_lines else 'INHERITED_FIXED_FULL_READ_PLUS_NEW_FIELD_DIFF')
    old_results.append(dict(feature_id=key,old_verdict=old['status'],verdict='PASS',disposition='retired' if retired_flag else 'active',
        reason=own_reason,review_method=method,source_document=scope,source_ranges=f['source']['line_ranges'],
        finding_refs=old['finding_ids'],immutable_source_preserved=True,
        changed_fields=[k for k in f if k!='retirement' and f[k]!=old_by[key].get(k)]))
for index,f in enumerate(manifest['features']):
    if f['source']['document'] not in scope_paths:continue
    key=f['feature_id']; n=int(key[-6:])
    reason=reasons.get(n) or next(x['reason'] for x in old_results if x['feature_id']==key)
    active_results.append(dict(feature_id=key,verdict='PASS',reason=reason,
        is_new=key not in old_by,manifest_pointer=f'/features/{index}',
        source_document=f['source']['document'],functional_scope=f['functional_scope'],
        destination=f['future_plan']['destination'],prototype_refs=f['future_plan']['prototype_refs'],
        downstream_mapping_findings=[]))

metadata_results=[]
for f in metadata:
    metadata_results.append(dict(metadata_id=f['metadata_id'],retired_feature_ids=f['retired_feature_ids'],
        verdict='PASS',source=f['source'],feature_refs=f['feature_refs'],reason=f['reason']+' 原完整旧行及source身份已独立比对，真实行为消费者仍存在；该单元不另计实现功能。'))

cases01=[dict(section_index=x['section_index'],path=x['path'],ranges=x['line_ranges'],verdict='PASS',
    reason='原active Berry/Lottery错误子体系refs已实际移除；源文身份与旧完整语义信用不变，主消费者仍在。')
    for x in catalog_checks if x['section_index'] in list(range(2183,2212))+list(range(2293,2345))]
cases02=[]
for idx,ids,why in [
 (2186,[596],'完整R7-BP01–08及WP61源单元重读，计步/友好/Repel框架链已加入。'),
 (2317,[187,11,31,49,554,555,577],'U05完整RF01–03/NG01及七个主消费者已核：退款原型和自然之恩持久写穿均可导航。'),
 (2337,[581],'Safari双容量SF01–05及完整WP53 §4已核，581为PROTO-CAPTURE消费者。'),
 (2339,[206],'U10-RL01–09与完整WP30学习/重学单元已核，206规则消费者已加入。')]:
    cases02.append(dict(section_index=idx,verdict='PASS',required_feature_refs=[fid(n) for n in ids],reason=why))

new_findings=[
 dict(finding_id='WU-R1-N01',severity='P3',related_original_finding='WORLD-CATALOG-F01',
      title='WP编号碰撞修正未传播到反向Pokemon目录',
      candidate_path=BASE+'section-coverage.json',json_pointers=[f'/sections/{i}/feature_refs' for i in range(2277,2293)],
      source_path=extra,source_ranges=[[1,6],[199,242]],
      feature_ids=[fid(n) for n in list(range(380,388))+[699,700,701,702,703,705,706,708,709,710,711,712,728,730]],
      explanation='该目录明确列Berry/Voltorb/Lottery正文，16节仍泛连Fishing/Slot/Mining，包括新增728/730；不是因宽导航本身失败，而是同号不同体系被当成静态验收来源。',
      required_correction='按实际正文/具名后继限定反向目录消费者；保真正跨域交界，不沿同WP编号广播。与pokemon分工同根合并，不重复计根。')]

indirect_navigation_observation=dict(
      related_original_finding='WORLD-CATALOG-F02',verdict='PASS',
      title='新增独立子单元未传播到具名验收消费者',candidate_path=BASE+'section-coverage.json',
      json_pointers=['/sections/2307/feature_refs','/sections/2331/feature_refs','/sections/2333/feature_refs'],
      source_path='deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md',
      source_ranges=[[428,467],[899,915],[925,942]],feature_ids=[fid(n) for n in [691,710,718,744,767,768]],
      cases=[dict(section_index=2307,source_cases=['L22','L24','L33','L35'],missing_feature_refs=[fid(744)],reason='克隆、编号、裁剪/PC门属于744，691范围已排除139–147。'),
             dict(section_indices=[2331,2333],source_cases=['U06-M11-003-A','U06-M11-005-MIN10','MIN11','MINT','MINF','MINL'],missing_feature_refs=[fid(767)],reason='独有输入优先/工具档10与11/闪光重叠属于767，710范围已扣41–48。'),
             dict(section_index=2333,source_cases=['U06-M11-005-TILE','U06-M11-005-TILEEND'],missing_feature_refs=[fid(768)],reason='动画读回/离散提交/完成确认属于768，718范围已扣106–119。')],
      explanation='744/767/768未直接列入catalog feature_refs，但目录具名父691/710/718且各自excluded_child_refs正确指向子行，可合成为显式、可解释的机器导航。分类/责任/父子扣除均成立，不要求重复登记dependencies.feature_refs。',
      readable_view_limit='子行完整出现在source-domain可读视图；父视图是否应额外展示子ID由root统一可读性复核，不作为本域语义FAIL。')

finding_results=[]
wu_old=j(REVIEW,PREV+'agents/world-ui-findings.json')['findings']
for x in wu_old:
    related=[r for r in old_results if x['finding_id'] in r['finding_refs']]
    finding_results.append(dict(finding_id=x['finding_id'],verdict='PASS',
      original_cases=x['source_locations'],original_feature_results=[r['feature_id'] for r in related],
      reason='全部原具名源范围和对应改动已复核；具体逐旧ID判定见old_feature_results。',
      related_new_feature_refs={
       'WU-01':[fid(n) for n in range(726,731)],'WU-02':[fid(767),fid(768)],
       'WU-04':[fid(744)]}.get(x['finding_id'],[]),
      evidence=[r['reason'] for r in related]))
finding_results += [
 dict(finding_id='WORLD-CATALOG-F01',verdict='FAIL',original_cases=cases01,
      original_case_verdict='PASS',same_root_propagation_verdict='FAIL',
      propagation_section_indices=list(range(2277,2293)),new_finding_refs=['WU-R1-N01'],
      reason='本域81个原active错误关系已修；反向Pokemon目录16节仍同WP跨体系广播，根因传播未完成。52节retired618历史导航另记录，未单凭其判active关系仍错。'),
 dict(finding_id='WORLD-CATALOG-F02',verdict='PASS',original_cases=cases02,
      original_case_verdict='PASS',same_root_propagation_verdict='PASS',new_finding_refs=[],
      reason='四个原具名跨领域缺项全部修正；追加子744/767/768可经目录→父→excluded_child_refs导航，未因deps未重复而强判遗漏。')]

catalog_results=[]
for x in catalog_checks:
    idx=x['section_index']; indirect=idx in [2307,2331,2333]
    catalog_results.append(dict(**x,verdict='PASS',
       reason='744/767/768通过已列父691/710/718的excluded_child_refs可解释导航；父子scope准确且不重计。' if indirect else
       '固定源和旧完整阅读信用保留；本轮逐节差分确认原错误active子体系已移除、实际主消费者仍在；静态未执行不升级。',
       finding_refs=[]))

result=dict(schema='r8-r1-independent-world-ui-review.v1',reviewer='/root/r1_world_ui',
    candidate_commit=NEW,old_candidate_commit=OLD,old_review_commit=REVIEW,
    source_commit=SOURCE,current_snapshot_commit=CURRENT,formal_trees=evidence['formal_trees'],
    configuration=dict(requested=dict(model='gpt-6.1-sol',thinking='ultra',service_tier='default',fast=False),
       actual=dict(model='UNVERIFIED',thinking='UNVERIFIED',service_tier='UNVERIFIED',speed='UNVERIFIED',fast='UNVERIFIED',cloud_task_uuid='UNVERIFIED'),
       visible_task_name='/root/r1_world_ui',qualification='请求与实际执行分列；原生priority工具广告不是default执行资格。'),
    counts=dict(**evidence['scope_counts'],old_verdicts=dict(Counter(x['status'] for x in previous['feature_results'])),
      old_new_verdicts=dict(Counter(x['verdict'] for x in old_results)),
      active_verdicts=dict(Counter(x['verdict'] for x in active_results)),
      finding_verdicts=dict(Counter(x['verdict'] for x in finding_results))),
    old_feature_results=old_results,active_feature_results=active_results,
    retired_metadata_results=metadata_results,finding_results=finding_results,
    catalog_section_results=catalog_results,reading_ledger=read_ledger,new_findings=new_findings,
    indirect_child_navigation=indirect_navigation_observation,
    static_evidence='world-ui-static-evidence.json',
    historical_navigation_observation=dict(section_indices=list(range(2293,2345)),retired_feature_ref='FR-000618',
      source='Lottery冻结依赖/旧批准/开放问题',replacement_refs=[fid(n) for n in [615,616,617,725]],
      conclusion='仅保旧ID可行，但当前目录未声明该错误历史关系已撤销；建议删除错误导航或明确其只记录旧错误，不把它当当前消费者。未单独计新FAIL。'),
    limits=['仅固定5666b7b候选的规划分类/元数据审查；不是最终整改或原型通过。',
      '没有执行Ruby/游戏/宿主/业务向量/Showdown/框架。',
      '本域131观察快照中的28正文和3catalog字节均未因908接受而改变；本域所有已知批次继续待整改后核对，未扩U02/U03接受到其它批次。',
      '全局schema/生成器/保护/接受回执整体验收由root负责。'],conclusion='FAIL_CATALOG_PROPAGATION; world/UI functional disposition corrections are substantively accepted within this static scope')
(OUT/'world-ui-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result['counts'],ensure_ascii=False))
