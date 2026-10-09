# B12 FULL 独立候选复审 1

结论：**PASS_SCOPED**。精确候选的 9 项局部贡献、6 项 B12 主责满足当前 qualified 控制和最低验收；未发现需要作者返修的候选质量阻塞。`blocking_findings=[]`，最小作者修复范围为空。本结论仅覆盖本次 FULL 候选，必要 affected 候选门仍须独立完成；不批准 actual、G、C、main 或任何 canonical 关闭。

| 身份 | 精确值 |
| --- | --- |
| 角色 | R-B12-FULL-CANDIDATE-1；作者外独立复审；额外子任务 0 |
| reviewed candidate SHA | `8ddba850af71f24e7bd77a80b7605c456c31dc7a` |
| reviewed candidate tree | `c8af1998818447f0e8969bada0b23fc83dfd24fd` |
| 作者导航分支 | `codex/cloud-dot-B12-author-1-20261009`；判定绑定 SHA，不随 branch tip 漂移 |
| FIX_BASE / tree | `1d06c45cc0a744fca181ac80ee573cc9ebb9b862` / `5c99f51ec4cc084bc1c2b081306f1b55370744df`（B15-C） |
| 下游管理包 | `9ad5539f38544fef6037356018015fe418021514`；不替代 FIX_BASE |
| 原 review / 批准 PLAN | `93e10babe0b9c9ef8b3f5277754541b447beeeb4` / `41fffb540c6483f5296ea0d33b789b75180d27ed` |
| 参考 SHA / tree | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `7589c800b61ba13a13040ed0d686979b80a84fd0`；静态只读 |
| 独立报告分支 | `codex/cloud-dot-B12-full-review-1-20261009`；从精确候选创建，普通提交/推送 |
| 本角色唯一写入范围 | `review/remediation/20261003-prepare/batches/B12/candidate-review-1/` |

requested 为 **gpt-6.1-sol / ultra / Standard(default)**。本选定云端委托已运行；可见工具没有可信 effective 参数回显，所以 admission/effective 按已批准 Plan A 分记 **UNVERIFIED_NO_AUDIT / UNVERIFIED**。没有主动换模型、降 effort、CLI/native 替代或启动子任务；未发现明确不支持或降级证据，也没有把缺少回显写成有效参数已认证。见 [configuration.json](configuration.json)。

## 完整输入、差异和范围

先读候选 `AGENTS.md`、`handoff/cloud-dot-20261009/original-contract.md` 和精确派发入口，再读冻结管理包及本角色链接输入。未找到适用的 B12 本地技能。原控制、批准验收及所有 current/root/extension/effective 限定按 9 项完整 logical object 核查，未用作者局部摘要替代。原始历史材料只作固定对象/证据复用，没有递归恢复旧 review 证明树；作者声明和 scope-amendment 只作待核证据。

完整流由以下精确命令取得并独立重建核对：

```text
git diff --binary --no-ext-diff --no-textconv 1d06c45cc0a744fca181ac80ee573cc9ebb9b862 8ddba850af71f24e7bd77a80b7605c456c31dc7a
```

[FIX_BASE-to-candidate.full.diff](FIX_BASE-to-candidate.full.diff)：**633,351 bytes**，SHA-256 **`4d7661e673d56cf534438cb51779bb92521073d55d2da60954f52ba52ff67e2a`**。共 43 个路径，11 正式输出、5 原稿、27 作者/候选证据；没有过滤证据、提案、scope 或原稿，也没有意外路径。正文/原稿变化、声明和同步关系做静态语义审阅；重复的大型控制/注册数组以自写 Git/JSON/hash/text 程序逐对象、逐元组穷尽核对，未声称对 57 个作者日志条目重新全文语义复审。

[metadata-verification.json](metadata-verification.json) 独立证明：

- candidate SHA/tree 正确；全部 11＋5 before/output blob、SHA-256、bytes 匹配精确声明。
- 原 findings 全文件 blob `6f3d96fd99b5a026bb88e463b3ad6e46658e3c01`，批准 acceptance 全文件 blob `e178e5706771f5f7465bcf3351b5c632a5d68bab`；9 项逻辑对象完整匹配指定 pointer、sorted/compact JSON 对象 hash 和管理包对象。
- 管理包控制 blob `b7013fc5d031d3b72ce1da33e0366c70565df307`；9 项 complete current control fields 与包内对象相等，6 primary 标记正确。身份相等本身不构成语义通过，逐项结论另见下文。
- 5 个原稿 patch 与父批准 `b452594ca55a9b9e39d073794684c13ec9fa18d9` 的精确 patch 字节/blob/hash 相等；各 before 身份和 after hash/blob/bytes 匹配。proposal 4 的 §3→§4 是标签订正，内容及 patch 身份不变。
- 57 个作者阅读记录、19 个作者源记录只独立验证精确身份。新语义阅读范围在本角色 [reading-log.json](reading-log.json) 单列，不能混同。
- combat 目录旧 230 行→244 行，WP53–70 目录旧 157 行→158 行；所有旧编号行字节、出现次数和顺序保留。前者新增 14 行，后者只新增 SF35，未吞掉已接受 AB/SF/BP/FP/PD 行。

## 九项独立结论

以下全部为 **PASS_SCOPED 的局部贡献**，canonical 均保持 OPEN。完整控制身份、条款、静态设计、判断和消费者边界在 [review.json](review.json)；原/净/附表/目录/追溯相互一致，不以 scope 获批代替质量检查。

| 控制 | 责任 | 最低验收及精确静态核查 |
| --- | --- | --- |
| GIR-FD82-003 | B12 局部；主责 B21 | 指定 A§6、B 主文§1/附表§1、§2.4、C§5.1 的源行号/加载定位历史迁入审计证据。保留族＋身份、复制缺源默认、最终覆盖行为和真实输入异常；CE/C59 比较不同内部表示的同一观察合同，错误叠加重复分或跨族动态别名不等价。未扩成禁止所有必要身份名或重审整个 003。 |
| GIR-FD82-A046 | B12 局部；主责 B07 | WP51 默认附表明确 AI SITRUS 估量 1；WP28 主动量 floor(H/4) 和 WP50 持物门各自保留。AI/I08 合法 H101/105、h1 请求 25/26，实际 HP26/27；`SITURUSBERRY` 不命中真实身份。旧 I02 保持，未以 AI 表覆盖实际恢复。 |
| GIR-FD82-B017 | B12 局部；主责 B10 | WP52-B§4 评分显式接 WP46§6.4。BE/B63 的 U51/60、T150/200 执行一次 m100，用户/目标分别至 60/100，再依序物品检查；AI 比例仍 100.5/51，未夹限。HealBlock 不拒均分，普通替身为独立前门拒绝。旧 B28、MH39–44、原 139＋1 身份保留。 |
| GIR-FD82-B020 | B12 primary | WP51§4 的完整列表先通用及 CanUse 资格再分类；nil 所选索引、首行动假、AI 上下文、场景及消息关闭准确。资格假只跳件，异常退出整段；普通报告返回后继续自动菜单/Mega/选招。AI/I06 的 POTION 先入候选、ETHER 后异常，最终无 UseItem/两物无消费；I07 移除 ETHER 后 POTION 登记消费一次。MAXETHER/主动 LEPPA、先行通用拒绝和需真 battle 的 flute/doll/ball 查询均作边界核查。 |
| GIR-FD82-B021 | B12 primary | WP51§3.3 每项取整/最低 1 后带符号合成。核对全部天气/能力身份、治疗/间伤资格、根倍率和耐热顺序、种子他端 H/h、毒计数、束缚来源、BadDreams 多成员、StickyBarb；Wish 保存量例外及 Perish 直接 999999 不被统一最低量覆盖。AI/S08、S09、AE/G13 正反向与源消费者一致，未写真实 HP。 |
| GIR-FD82-B022 | B12 primary | 完整 A/B/C 族＋身份＋copy-source 集合独立比较；Assurance 恢复 TargetLost，OHKOIce 失败为独立冰门，HelpingHand 无整体分，Imprison 恢复目标分。清理 Morpeko 整体分/青草治目标失败的假直接项、保留真 copy；AbilityRanking 20 add＋5 copy＝25，A334 不变。正确原表/算法不改。BE/B02b/B61、CE/C56/C57 均满足。 |
| GIR-FD82-B023 | B12 primary | 默认 PBS GEOMANCY User→目标数量 0→整体失败/整体分，无所属目标处理器消费；target 本地算法和族保持。BE/B62 合法 XERNEAS L55/H203、GEOMANCY＋AURORABEAM、零阶/清醒/默认 FAIRYAURA/无其它通用改分：h203/50×无物/PowerHerb 四组合候选 100；三项全＋6 得 20，部分封顶仍 100。不推最终选中或真实效果。 |
| GIR-FD82-B024 | B12 primary | 合并两原控制义务；宝石基础 6，比较 MECHANICS_GENERATION≤5。18 宝石类型映射、直接键优先与条件组顺序保持。CE/C58 中等 FIREGEM＋PP 正 EMBER、无后置 Fling/Acrobatics/外部直键：机制 5 得 8、8 得 6；无对应可用火伤害两配置都 0。原主文/附表精确 patch 3/4 与净化稿一致，实际增幅/消费/誓约例外仍归 WP50。 |
| GIR-FD82-B026 | B12 primary | WP53§6.1 串联缩队、步进第二候选、公共单敌/允许覆盖、普通伙伴准备和大会预算/保留/通知。SF35 有效 20 球/K、NaturalPark BugContest、非 Safari、force-single 假、可战伙伴、无其它接管/规则残留、正常返回前未到期：普通 2v2、玩家＋伙伴，无大会菜单或预算传入/回写/K 覆写，正常胜利伙伴善后治两队、无单敌 wild-end。无伙伴、force-single 真及覆盖假分别反向核查。 |

### 重点消费者和反向核查

**B020**：静态源链为通用资格→完整业主列表逐件资格→候选分类→扫描完成后的选择→登记/消费。ETHER 的 nil 索引异常发生在候选选择与注册之前，先前收集 POTION 不会形成临时 UseItem；AI 外层异常包装 normal reporter 返回后继续后续阶段。POKEFLUTE 的 allBattlers、玩偶的 wildBattle?/canRun? 和球的容量/禁球/首行动查询不能因不在偏好表先过滤。通用拒绝则不会到达依赖查询。保留人工 PP 索引、持有 LEPPA、设施/插件/报告器自身异常的分层和未证限制。

**B021**：H11/h9 雨期限 2 的 RAINDISH 恢复 1、Curse 损失 2，d1；技能 32 的普通愿换门 h/2=4、H/4=2 均假。这里只证明该门，不宣称最终不换；高技能额外 Curse/毒/种子分支仍独立。清 Curse 给 d−1。H11/h2 的增/降阶 helper d≥h 假，移除 RainDish 给 d2 真；whole 可返回 60、非whole保持，不推整体最终分。H11 的 BigRoot 先商/倍率/最低量、Heatproof 先商/半数向上最近取整/最低量、Wish0 不套最低量、Perish999999 覆盖累计的邻近对照与正文一致。

**B022/003 注册**：[registration-comparison.json](registration-comparison.json) 比较原提取与最终全集的 `(family, identity, copy-source)` 多重集合。A334 与 C167 字面出现全等；B 原270、最终列表字面269，显式补记一次 `MoveEffectScore/PowerHigherWithConsecutiveUse` 的重复 add 来源后出现数270，无缺项/多项。此调整透明记录，**不代表两个有效分**。该整体分最终读 EchoedVoice 侧计数，基数仍读 FuryCutter；OnUserSide 没有整体分。RemoveProtections 的缺源 copy 不改变 +7，Parting Shot 的跨族缺源 copy 不改变目标降阶分，Sketch 的缺源整体 copy 未创建键。共同默认保持输入，不补造未来动态别名。

Assurance 的目标 +8 依可动且不更快的盟友，Revenge/Avalanche 使用另一整体敌方循环。同级冰目标 OHKOIce 失败；普通 OHKO 同夹具不失败，非冰再落普通等级/坚硬门；WP46 loaded 条款的真实许可区别不由 AI 改写。HelpingHand 整体输入100保持、目标 +5；Imprison 默认 User 普通候选100，直接目标评分遇首个共享敌即停 +8，输入100得108而非116。

**B023**：核查 Target 数据、PBS 招式、基础 pbTarget 和 Geomancy/TwoTurn 类无 pbTarget 覆盖、AI 候选 num_targets=0 分支、整体失败预测及目标两回合处理器。原 patch 2 纠正的是默认入口可达性，未把正确局部 target 算法删掉或移到 whole；评分不执行升阶、扣 HP 或香草消费。

**B024**：核查基础宝石评级 6、中等技能修正门、直接键优先及首个条件组、MECHANICS_GENERATION≤5 的 +2、18 身份→类型映射和 PP 可用伤害类型门。输入已排除后置 Fling/Acrobatics/外部直键，8/6/0 的静态结果唯一。旧 C05 原样保留；57 条条件身份与 786 出现/783 键/782 有效键、完整839口径分开；条件性67树果不是这57身份的替代口径。

**B026**：静态核查大会 start 缩为选员且未注销 partner；步进按 force-single、Safari、partner、成员数量顺序判断，partner 真早于一员假门；双候选传公开包装即不派发大会 override。正常核心收 partner 队伍并设双打，ordinary after-battle 治两队；大会 20/K 未被该路径接收/回写/储存，双敌 public wrapper 没有单敌 wild-end。无伙伴及 force-single 真只产生单候选，仍需 can_override、进行中和无更早 handled；can_override 假不接管。直接大会入口的预算初始化、强制单打在接管后、返回预算回写和 wild-end 次序保留。未读取实际 Demo 事件，不宣称游戏中已出现此组合。

## 五个原稿质量与已接受成果

父范围批准只证明允许这五项精确变更；本次独立判断另核对其语义质量：

| 原稿 patch | 质量结论 |
| --- | --- |
| 1：WP51§3.3/§4 | 残余全分量规则、两个消费者门和完整物品资格异常/无消费链与参考一致；与两个正式 WP51 输出/静态目录一致。 |
| 2：WP52-B§3 | 默认 Geomancy 无目标候选和局部 target 合同准确分层；保留原 target 算法。 |
| 3：WP52-C 主文§2.1 | 比较参数为机制世代；基础6和类型门均保持。 |
| 4：WP52-C 附表§4 | 与主文相同参数订正；原正确18类型映射和全部身份行未变；§4标签正确。 |
| 5：WP53§6.1 | 取消“一员保证接管”的错误保证，补公共基数/覆盖及伙伴优先链；预算、保留、通知、未到期前提和旧 SF01–34保持。 |

[accepted-interface-preservation.json](accepted-interface-preservation.json) 独立记录 23 个 receiving/原稿/目录文件 FIX_BASE→candidate 整文件同字节，另记录两个变化目录的全旧行保护。WP28、WP36、WP37、WP39/40/42、WP46、WP50、WP59–61、WP62/63/64 正确已接受条款保持。B15 的 C122 对应 WP62§6.1 和 PD31–34/W31–34 的 nil/空串分层；C109 对应 WP63 最终选定 ID 查询及 P33/P34 两失败/两成功反向。finding ID 没有被误当测试行 ID，原稿/净化文字和全部旧设计保持。

## 必要 affected 路由和后续门

[affected-routing.json](affected-routing.json) 对全部10个 potential owner 独立绑定精确导航版本并判断接口。下表是 **FULL 的必要范围判断**，没有签署任何 affected owner 的候选/actual receipt：

| owner | FULL 路由 | 有界依据 |
| --- | --- | --- |
| B07 | 必需独立 affected candidate | WP28 主动 SITRUS 量和人工 PP 选择 vs WP51 AI 估量/缺索引全列表异常；纳入新原稿。 |
| B08 | 必需独立 affected candidate | WP36 优先序/步进第二候选、WP37 handled/通知 vs WP53 公共基数/覆盖、普通伙伴及大会预算/保留链。 |
| B10 | 必需独立 affected candidate | WP46 真实均分接收与 AI 比例、loaded OHKOIce 与 AI 独立冰失败；保护139＋1/MH39–44。 |
| B11 | 必需独立 affected candidate | WP50 held LEPPA/SITRUS/宝石执行 vs active/AI入口；保护共享目录所有旧 AB 行。 |
| B02/B03 | FULL 未识别真实新接口变化 | 唯一交集是 WP53–70 reader；SF35 新增属于 B12，全部旧行同字节同序同次数，C109 接收文字/P33/P34未变。 |
| B04 | FULL 未识别真实新接口变化 | 指定003源定位迁出，族/最终行为/默认保持；B04 专属 caller/sanitization 行为义务未改。共享 ID/文件不自动要求全 owner 重审。 |
| B09 | FULL 未识别真实新接口变化 | WP39/40/42 整文件未改；新 d 明确为 AI 近似，未改变真实时序、资源、HP 写入或原最终 binding/default。 |
| B14 | FULL 未识别真实新接口变化 | WP59–61 同字节；SF35 正常返回前未到期，旧时间/步进/blackout、SF/BP/FP行保持。 |
| B15 | FULL 未识别真实新接口变化 | WP62/63/64 两套正文同字节，C122 nil/空串、C109 最终查询和旧目录行保持；新增仅 SF35。 |

四项必要 affected 门应由父任务交独立角色，在其授权目录发表精确 reviewed SHA 结论。其余 FULL 路由证据可供父任务决定准确有界处置，不冒充其他角色报告。本报告通过不使 B13、B16、B21 或全部共享根因通过。

候选 FULL＋真正必要 affected candidate 门齐全后，sole A-REG 才可 G。actual 必须另冻结完整 SHA，并取“当前已接受前驱→actual”和“本 candidate→actual”两份完整未过滤流；独立 Ultra FULL/必要 affected actual 完成后 root 才可 C。B16 私有只读准备已完成、无并发正式写；B12 C 后父任务重新冻结五个已变化正式 reader，并重算实际新增原稿/caller 输入，不能复用已变化的旧输入身份。

## 限制、报告发布和复核方法

[source-limits.json](source-limits.json) 保留 U01–U10/G01–G12/AX01–AX20、条件性67树果、全部具名未读、B15-C 接受限制及所有非局部职责。参考仅以 `git show` 读取固定源文本；未运行参考/游戏/Ruby/编译/转换/生成/反序列化/行为模拟/向量或历史 author/reviewer 程序。**执行行为向量、运行观察、已证 Demo 链全部为0**。新执行程序仅为本目录自写 Git/JSON/hash/text 元数据核验；上述100/20/8/6/0及HP算术均为静态设计结论。

未读/未证仍包括 Data/Scripts.rxdata及二进制/序列化数据、可执行文件/宿主DLL/mkxp.json、真实地图事件、媒体/图像/音频/字体/soundfont及宿主容量输出、八个杯赛名单引用文件/pokemon_metrics.txt样本、backup/gen目录、实际插件组合/动态调用/deprecated别名/EventScene/动态阴影可达性和真实Demo链。未列源路径/范围不宣称本轮语义重审。

本角色仅新增本目录报告/证据/自写元数据程序。正式材料、公共登记、作者证据、main 和参考均未修改。独立分支普通 commit/push 后以远端 branch 完整 SHA 和 fetch/readback 的 tree、报告目录字节、candidate→report 的唯一写入范围验证发布；最终交付在目录外给出完整 **report SHA**，避免报告自身 SHA 无限回填。无候选质量阻塞位置或修复请求；尚缺门是上文四 affected 和后续实际整合门。

JSON 解析及全部身份/集合/计数断言通过。新报告文本格式检查通过；归档 `.full.diff` 的空上下文行含必要 diff 前缀空格，普通 staged whitespace check 会将它们报告为尾空白。此文件保留要求的完整原始流，未为格式检查改写其字节；其精确长度/hash和Git重建相等另已核验。
