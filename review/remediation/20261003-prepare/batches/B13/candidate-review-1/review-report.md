# B13 candidate FULL 独立复审：NEEDS_REVISION

本次独立静态复审完成全部 **8 贡献／5 主责／11 输出**。精确 reviewed candidate 是 `5845e8084ced280e51c51a4081ec8583a9c2ca39`，tree `23f92a9c446f5f0fbcee44df2f57d85df4dd0e3c`。结论 **NEEDS_REVISION**：GIR-FD82-B027 的新增结构化验收证据把取消返回的 `nil` 写成 `false`，尚不能据此给 candidate FULL PASS。

这是 R-B13 的 candidate FULL 结论，不是 affected、G、actual 或 C 签署。全部静态向量均未执行。B030 非必修、计数 0；WP67-A 扩展继续归 B16，不因本地复审关闭或解除其正式工作保留。

正式 FIX_BASE 为 B12-C `8e67f780c204d593d89f364f585d2c6c2fe74631`，tree `ae2f491294eb4f97be6b75f75706c16279f9bf46`。`1dc5cc80854e02965b9bb7a02c00a7c40d392f89` 仅作为当前派发 publication 导航。管理许可 `2b23c82947bcecec4ab059d63048f9b67586575b` 没有取代 FIX_BASE，四份原稿的精确范围许可也不是质量 PASS。

## 阻塞 B13-R01：取消返回值的身份丢失

当前新增证据存在一个同根局部问题：

- `author-draft-1/static-transition-traces.json:14–18` 的 `/entry_submission/1/return` 是 JSON `false`，输入却明确为 `nil`。
- 净化 combat 目录 `WS-W35`（99 行）把空列表和 nil 取消的包装返回均写成“假”。
- 当前 `scope-applied-1/finding-dispositions-successor.json:1092` 的 B027 处置也写“nil 保留两者且返假”。单独的“假”可以被理解为条件真值，但与明确的 JSON false 合读并未保留精确返回身份。

固定参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 的 `002_Challenge_Data.rb:38–50` 包装，在正常界面返回后用该结果与“长度大于零”的合取值覆盖返回变量。取消界面返回 nil 时，该合取值及包装最终返回均为 nil；初始 false 并不会留下。界面取消的 nil 由 `005_UI_Party.rb:1051–1138` 独立定点回读确认。报名写入的活动队伍分支由 `001_Challenge_BattleChallenge.rb:200–203` 确认。

| 正常返回的输入 | 提交 | 已有报名 P | 进行中的活动队伍 P | 精确返回 |
| --- | --- | --- | --- | --- |
| nil 取消 | 不提交 | 保留 P | 保留 P | nil |
| 空列表对象（工具／替换 UI） | 提交该列表 | 覆盖为空列表 | 立即覆盖为空列表 | false |
| 非空列表对象 | 提交该列表 | 覆盖为该列表 | 立即覆盖为该列表 | true |

nil 与 false 同为 falsey，不能以相同条件分支结果替代精确返回值。现有新增 oracle 会漏掉将取消返回错误转换为 false 的实现。本项批准的 determinate recheck 明确要求空列表与取消各自的提交、返回和活动队伍状态一致；因此这是 GIR-FD82-B027 的返修，优先级 P3，不增加 canonical 根因计数。

最小返修是：仅把新增 WS-W35 的 nil 返回明确为取消空值；把 nil 轨迹写为 JSON null 并补显式 nil 身份；同步当前 B027 处置文字。若冻结作者证据按流程不可覆写，可以新增明确替代该轨迹的后继证据并更新当前派发导航。保持 WP55、旧 WS-W28/W29、进行中／未进行中提交差别和默认 UI 人数下限限定。无需改变参考、运行向量、扩大 B16 范围或修改四份已精确授权原稿；另增原稿改动仍须自己的精确范围许可。

## 全部 qualified 控制与局部结论

完整证据见 [control-coverage.json](control-coverage.json)。每项记录当前控制优先级、完整 root 裁决、扩展裁决、minimum_revision、determinate_recheck、反例／逆向条件和独立身份检查。原始 raw／历史状态没有替代当前 qualified/root/extension 决定。

| canonical 控制 | 主责 | 独立静态核对与结果 |
| --- | --- | --- |
| GIR-FD82-003 | 否，B21 | 本地 WP54/56/58 源继承、类组织、调用统计和历史定位已迁审计；必要席位／索引、五元组、18 键、−1/−2、BURMY 标志与共享图鉴／Bag 副作用保留。本地要求满足，其它扩展／共同根因不关闭。 |
| GIR-FD82-B003 | 否，B11 | 14 个精确键、11 设置包装／3 仅消费者、suddendeath 原字面与 sleep/sleepclause 成对条件一致；共享 skillswapclause 门没有被局部表取消。本地要求满足。 |
| GIR-FD82-B010 | 是 | 默认固定加载且无后续覆盖；条款假不因冰目标本身拒绝，真时先拒绝。非冰用户 SHEERCOLD q30、双方 L50、排其它防御后阈值 20，r19/r20 成对；原定义与 AI 独立预测差别保留。资格不扩大为必中／必倒。本地要求满足。 |
| GIR-FD82-B018 | 否，B11 | 旧 RC 实际 24、总 127，新 47+35+28+26=136；W22b 存在且保留。数字标签不推导行为缺失、语义通过或关闭 B016/B017/INTAKE-C01。其它域 65/139/148/196 限定保留。本地要求满足。 |
| GIR-FD82-B025 | 是 | 本次收到使用者与保存灭亡歌来源区别正确；合法双 Lapras 保存源 0、最后动作 1／0 两例均为决定 2，倒下前收源、正决定退出与非内部早退保持。普通 selfKO 最后使用者方向及爆炸返回假异常不改。本地要求满足。 |
| GIR-FD82-B027 | 是 | nil 不提交、空列表提交及活动队伍后态正确，旧 W28/W29 保留；新增精确返回 oracle 不正确，B13-R01 阻塞。 |
| GIR-FD82-B028 | 是 | 开场初始化与普通补位分离，补位不重置 count/mind/skill/starthp/开始标志。合法三员 HP100/115/105、固定成功 Growl 在 3/4/5 轮累计裁判、双方当前持久 HP 归零并顺序补位，最终决定 5；首次三轮控制保留。WP56/58 本地满足，WP67-A/B16 未关闭。 |
| GIR-FD82-B029 | 是 | 完整非随机 helper 闭包覆盖回合末及攻击阶段招式／物品／能力属主选择，逐门核 phase/owner/候选/生存/追打/失败。BatonPass 记录追加 1／回放同点消费 1；Roar/RedCard 随机不写询问，Arena 不进询问，旧 W16 内部战斗不可达限定保留。本地要求满足。 |

Arena 的全 Scripts “复位入口只有定义”的既定有限事实采用同一固定参考版本的完整 root 裁决及冻结导航证据，实际开场、普通补位和参与登记链本轮独立定点回读。没有把继承的全域搜索记录说成本轮重新搜索或语义全读。B029 同样以完整 fixed qualified 控制导航全部列举消费者，再独立回读对应入口与记录／回放链；3 处直接文字调用统计没有代替行为闭包。

## 完整差异、十一输出与旧贡献保护

新复审 metadata 程序独立产生无路径过滤的 FIX_BASE→candidate 差异 [FIX_BASE-to-candidate.full.patch](FIX_BASE-to-candidate.full.patch)：**4,623,310 字节，69 路径，SHA256 `443b607310bdd6556c0c923f0209804fcc86aa6b66cf5ae52fb4b0513f5316f2`**。逐路径／前后树对象分类、所有正式变更语义、当前控制与报告绑定均核对；哈希相等没有冒充语义或运行验证。69 路径由 11 正式输出及 58 作者／候选证据组成，无范围外变更。publication 相对 candidate 只增加三份派发／收据文件，没有正式稿字节变化。

十一输出的 before/after Git blob、SHA256、bytes 与作者记录全部独立相等，publication 相同；见 [independent-metadata.json](independent-metadata.json) 的 `all11_outputs`。覆盖方式如下：

| 输出 | 复审内容 |
| --- | --- |
| 净化 WP54 eligibility/clauses | 完整正文；报名、EXP／恢复、精确键、OHKO、收到源判定及 Q 控制。 |
| 净化 WP54 entry-rules/cup-data | 完整附表；键／策略／模式身份与正文一致，八个杯赛名单未读限制保留。 |
| 净化 WP55 session/restoration | 完整正文；活动报名、会话统计、单场正常顺序及异常部分提交窗口。 |
| 净化 WP56 Palace/Arena | 完整正文；概率、开场与累计状态、体分／表格／向量一致。 |
| 净化 WP58 recording/playback | 完整正文；外部格式、共享副作用、全消费者来源域与 Arena 回指。 |
| combat catalog | 全部 136 行与旧 127 行独立分组／身份比较，改动／新增行逐项语义核对。 |
| creature catalog | 全部旧 125 身份顺序／次数和前后字节比较；唯一变动 FC-10 的对象／默认属主／活动计数及报名区别核对，其余既有行为复用相同字节。 |
| 原稿 WP54 | 完整 before/after 身份及精确许可补丁，局部 §2.3 B027 同步核对；其余固定原稿字节复用。 |
| 原稿 WP55 | 完整 before/after 身份及精确许可补丁，单场恢复补充核对；canonical 增量 0，其余原稿保留。 |
| 原稿 WP56 | 完整 before/after 身份及精确许可补丁，Arena 生命周期／体分／P19/P20/P28／摘要一致。 |
| 原稿 WP58 | 完整 before/after 身份及精确许可补丁，完整消费者、Arena 回放／W24/W25／审计统计一致。 |

四份原稿 after 与 `2b23c8…` 所绑定 proposed-after 全字节相等；依批准 patch 序列化重建的 whole.patch 为 22,738 字节、SHA256 `11bfdbd21211dce18016569c7bb5dd9447b90531475f70920e737ae77df0e769`，全字节相等。其许可、固定补丁及质量判断分别记录。Git 原生 diff 与 difflib patch 的不同序列化没有被误报为原稿范围问题。

52 输入身份全数独立核验。全部 8 控制的 whole original 和 whole approved acceptance JSON 对象与各固定原报告／批准 PLAN pointer 相等，完整当前字段一致。要求链接的 `refreeze-after-B12-C-1` 管理路径在 publication 中缺席，但在精确管理 SHA `e8caada4ab919e48e3dc817f0638ce595fde449c` 可读，作者控制副本全字节相等；没有以失效导航跳过控制。

所有既有 accepted contributors 按当前控制登记核对：003 的 B04/B08/B09/B10/B12/B14/B15，B003 的 B09/B11，B010 的 B10，B018 的 B10/B11，B025 的 B09；B027/B028/B029 没有此前 accepted contributors。未变接受材料以精确字节复用，本地会影响的当前 B09 received-source/终局、B10 loaded-Ice、B11 keys/attack replacement/count、B12 prediction 与最终 52 输入边界核对，不将作者 affected assessment 当作独立 affected 签署。

36,073 个既有受保护路径（十一许可输出及 B13 本批证据范围之外）前后 mode/type/blob 均未变；其它域 formal/public/review、AGENTS 等没有被改写。旧 combat 全 127 ID 的分组内顺序及出现次数保留，creature 全 125 ID 同样保留，非 FC 行逐字一致。旧 combat 仅 Q32/Q36/Q37/Q38/Q40/Q41、P19/P20/P22、RC-W22b 十行改变，均在当前控制核对；新增九项如 coverage 所列。旧 WS-W28/W29、PA-P16 与 RC-W16 不变。不能把这些保护结果扩大为其余 owner 全域重新质量接受。

## 独立性、配置、来源与后续门

首先读取 AGENTS.md；冻结 baseline/publication 的 AGENTS 身份一致。环境 `.agents/skills`／相关 SKILL.md 未发现适用本仓库技能，遵循仓库规格／架构中立和 reference 只读要求。独立 worktree/分支为 `codex/cloud-dot-B13-review-1-20261010`，仅新增本 `candidate-review-1/` 报告目录，没有改变正式稿、public、main、reference 或作者证据。没有创建额外／嵌套任务。

请求配置记录为 **gpt-6.1-sol / ultra / Standard / service_tier=default**。有效后端没有可信回显，记 **UNVERIFIED**，不声称已认证。完整 B13 contract 明确允许已批准 Plan A 的 requested admission，且不要求新的 backend/quota probe。本复审没有请求配置变更、使用另行模型 fallback 或创建认证门；无回显本身不构成质量阻塞。详见 [model-and-limits.json](model-and-limits.json)。

固定参考 commit 的 20 个文本文件通过不可变 raw URL 重新取得，Git blob/SHA256/bytes 全部独立匹配。语义仅阅读 [source-reading-log.json](source-reading-log.json) 列明的准确行段；完整文件哈希不是完整语义阅读。参考 tree 的固定身份继承当前 qualified trace，未声称本轮重新核验完整 reference tree。作者声明的范围与本轮实际范围分列，特别是 StartAndEnd 仅到实际 EOF 568，ItemEffects 本轮延伸至 1582；不把越过 EOF 的作者定位当作本轮读数。

reference／Ruby／游戏／编译器／转换器／生成器／反序列化器／历史作者与复审脚本／行为向量执行均 0，runtime observations 和已证明 Demo chains 均 0。只运行本轮新 Git/JSON/hash/text metadata 与报告读回程序。U01–U10、G01–G12、AX01–AX20、树果条件 67 及全部继承具名限制完整保留；未读杯赛名单/pokemon_metrics、二进制/序列化、地图事件、素材媒体/字体/音频、Game/DLL/mkxp/宿主容量、备份/gen、动态调用／插件／别名／EventScene／动态阴影与真实 Demo 链均不以静态设计作运行确认。完整限制原文保存在 source log，不递归重读历史。

candidate 必须先局部修正 B13-R01 并冻结新的精确 SHA，再完成所需独立 FULL 及有限 affected 门。潜在 affected 导航为 B02/B03/B04/B07/B08/B09/B10/B11/B12/B14/B15，必要性与真实有限范围由各独立角色判定，不由本报告代签 PASS_SCOPED 或 NOT_AFFECTED。没有 G 登记授权、actual 审核或 C 接受。actual 阶段仍须当时接受前驱→actual 和 candidate→actual 两条完整未过滤流，及独立 FULL／分别必要 affected；candidate 字节或局部结论不能替代。

普通 commit/push 与远端 ref/tree/全部报告读回记录另见 publication receipt；报告发布 SHA 与 reviewed candidate SHA 分别返回。任何报告发布管理后继均不改变本次实际 reviewed candidate。
