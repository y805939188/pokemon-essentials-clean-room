# Pokémon／世界／UI R3 独立复核：FAIL，仅两行当前源校准注记

固定候选 `c0f62d973180679134f2eb1a488c1dc359c8658f`，当前正式源 `5f87743293290de2e219ecdd6c19e88280f60c9a`。工作树正式正文仍为 B8，全部当前定位和正文均从固定 Git 对象读取。

本域 **353 行分类、职责、有效范围和依赖 facet 全部 PASS**；FR456、FR596 的新增当前源差异注记 FAIL，故总体为 **351 PASS／2 FAIL**。R2 的 `POK-WORLD-R2-DEP-001` 全20行及相同 scope 的额外5条错边均已修复。没有将这两处注记错误倒扣为分类失败，也没有重开已修的目录问题。

逐项结果见 [pokemon-world-results.json](pokemon-world-results.json)，固定身份和独立哈希核验见 [pokemon-world-evidence.json](pokemon-world-evidence.json)，可复现静态审计见 [pokemon-world-audit.py](pokemon-world-audit.py)。具体最小修正文集仅作为审查建议保存于 [pokemon-world-calibration-corrections.json](pokemon-world-calibration-corrections.json)，未应用到作者文件。

## 范围、身份与阅读信用

完整解析并与固定 R2 全局结果对齐：333 原始ID、353 active、12完整退役及12 metadata、17原组、62主文档。原333 ID为331 PASS／2 FAIL；12退役体去掉 retirement 后逐字段等于初 d62 完整旧体。12 metadata 与 R2 整对象相同，真实直接及父→excluded_child_refs→子消费者导航保留。

R2 REPORT、findings、feature/finding/issue/reading/section JSON、完整本域报告／结果均按 `0ef0b7ad5f9465cfe31da0d7a35f56b5ccba5add` 读取或完整结构解析并逐本域对象核对。R2 源分工的21新标题完整正文阅读信用，只有正文与最终5f精确相等且本域消费者重估后才复用；不能将其当作当时已经接受或应用。

累计源中18个主文档改变，全部完整 B8→5f 差异已读；28个直接改变的有效功能单元逐一对照最终正文。主文档及额外消费者的新读范围、旧全文信用、当前／B8／R2身份和复用限制逐篇保存，未声称本轮重新全文阅读62篇。截断输出的缺段已由后续完整区间补读；未读部分不计新读信用。

独立重算本域当前1204标题，其中149目录标题；历史目录141标题加本域新增目录8标题。13个主文档新增标题与7个外域新标题的本域消费者分别给结果。前者包括原 U04 待应用的地图修剪、摆放失败后继、117／119、活动跳跃、地图目录等范围；本轮按最终5f实际正文重估，保持静态 `NOT_EXECUTED` 和既有承载分工。未凭新增标题要求新功能ID。

353个 current locator 的单元／文件 SHA256、Git blob、固定 snapshot 和原 source 均独立重算。83个非空出站 feature_refs 行共329条边全部枚举；3724条 direct_refs 的 B8真实锚点另作结构核对。结构存在性不代替真实用途。13个受源／目标变化影响的外域入站生产者给出真实当前源和目标范围，生产者依赖语义由对应领域结果汇总，未从 incoming 关系扩张本域职责。

## R2 依赖问题：20行限定 PASS

348改由364消费地牢三层图块，372／373指366世界天气显示；487／681／754／755接真实成长与持物边界；608指665–667图鉴界面；664／682／749接容量、储存操作和守卫；751／760指365世界角色／临时动画；756／764保持地图转移及地图状态交界；757／759接暂停微更新、保存退出和模式会话；761／762指普通道具／过滤背包；766清除异体系Slot转轮边而保留消息确认。

逐行结果保存删除、替代及保留的完整ID、候选JSON指针、最终有效源和目标范围、独立理由。664额外删除159／160／161的训练家／伙伴／钱包／配置混用；751／760额外清355音频族直接错边。动画内部可交SE定时，不等于751自身直接消费整个音频族。

对照保留：744名人堂确实显示训练家数据卡；681的735为具名“复制槽位与正常教学不同”的排除性对照；753作者校验／诊断／语言经真实合同导航；741→579→excluded755的间接消费者仍合法。没有把未重复最细ID或存在父子导航当成失败。

两个继承的 R1 目录 issue 继续 PASS：724仍消费 WP43 未实现效果回退；16反向目录节移除352错边的修复完整保留。17原组原具体case均PASS；当前扩大scope中仅POK-S05因596的新增注记错误FAIL，WU-06的R2依赖范围已恢复PASS。

## 当前源职责精化：限定 PASS

645／647分别读完 UI65 L148–176、L206–233及WP12 L92–186。静止只排普通移动／碰撞计时，活动跳跃独立；消息早退、新请求门、已有请求消费优先级、微更新不分派，以及失败前缀没有被合并成全UI跳跃暂停／恢复保证。330是真实运动合同，新增 direct_ref 指向B8已有父锚点。

699／703分别覆盖七个SCRIPT_TEXTS图像角色、逐请求game→core、缺译与空译、固定资源例外、实际位图高度参与转轮时间分区；提示空译清图与转轮空名早失败、普通捕获／空白创建／帧前缀路径，以及对象／随机／奖额／音效／财务尾前缀均分立。440、352、354、699／702的引用有实际用途。

397属于kernel正式分配，本域只提供额外交界结果、不计入353：15个精确蛋群作者身份及合法扩展接受域，与WP18基础默认／形态克隆、WP33 Undiscovered先行门及Ditto／性别／交集、WP34亲本／生成角色正确分工。

## 新增当前源校准错误

### R3-EV-BOUNDARY-001：本域case FR456，P3

位置：`routing-manifest.json#/features/433/differences/1`。新注记把“设施255/255”称为“超总量EV”。最终 WP19 L164–180 明确HP与攻击各255、其余0、总量510；越额的是单项252门。该样本进入普通分配时，第一项HP余量252−255=−3先失败；总量夹限及本接收者EV／经验写入未到，不能用“总量超限”解释。重算保留存储值、默认非内部设施更早成长返回的限定均保留。

同步错误：`feature-source-deltas.json#/records/35/source_fact_delta`、`source-file-reassessment.json#/records/22/source_fact_reassessment`、`source-refinement-patch.json#/records/39/field_changes/0/after/1`及派生Pokémon视图。最小修正为准确表述“单项越额、总量510”，并限定该样本的先失败位置；不改正式源、分类、职责、范围或依赖。根报告将本域456与战斗域29／32的同根边界注记合并，不能重复计问题票。

### R3-SOURCE-ATTRIBUTION-001：本域case FR596，P3

位置：`routing-manifest.json#/features/566/differences/1`。新注记称WP61新增步骤概率／累加器向下取整和负值语义。完整B8→5f的WP61差异只有L56：Repel比较对象默认首个非蛋成员（允许濒死），替代配置才取首位可战成员。596的最终有效范围为L22–26、37–40、42–44、46–49、51–54、56–57，没有所述概率／累加器条款。

可区分例：Repel活动、首个非蛋濒死L50、下一健康L10、野生L20，其余门正常；默认比较L50会拒绝，首可战替代比较L10则放行。概率取整不能表达这个已接受修正。现有WP36直接合同、父行计数／通知次序及762的确认选择分工无需修改。

同步错误：`feature-source-deltas.json#/records/40/source_fact_delta`、`source-file-reassessment.json#/records/27/source_fact_reassessment`、`source-refinement-patch.json#/records/44/field_changes/0/after/1`及派生视图。最小修正为替换错抄的当前差异说明；根报告合并其它领域173／227的同根源归属case。

两case还需同步当前证据生成器的对应字符串、重建统一补丁的after值及派生视图，并重算受影响最终身份／摘要。R1／R2历史、接受源、归档实际应用回执均保留。精确before／proposed_after和路径／JSON pointer已作为可复核建议单列。

## 验证与资格

仅执行静态JSON／Markdown／Git／Python审计，全部身份／对象／标题断言通过。没有运行Ruby、参考游戏、业务场景、宿主、Showdown或未来框架。根分工负责全局9接受事件／230绑定、来源工具负例、保护和最终合并；本域不另授源接受或上游CLOSED。

全部去向仍待验证、阶段待定／未批准、实现／验收未完成，排除0。捕获、战斗用物、逃跑和战中成长的协作候选不因未跑原型而自动FAIL，也未获得兼容通过。model／effort／tier／speed／Fast／云UUID缺权威echo，逐字段UNVERIFIED。仅写本新review目录的pokemon-world前缀输出，没有修改作者、正式源、参考或旧报告，没有提交。
