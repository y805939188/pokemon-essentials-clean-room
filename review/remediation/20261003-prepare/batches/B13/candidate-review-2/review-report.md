# B13 NEW candidate FULL 独立增量复核：PASS

原 R-B13 角色完成当前 **8 贡献／5 主责／11 输出**的独立增量复核，结论 **PASS（仅精确 NEW 的 B13 本地 candidate FULL）**。本轮两个问题的返修满足相应 qualified 控制；未发现新的局部质量阻塞，当前要求作者继续返修的最小范围为空。

Reviewed NEW：`db9e6ed1997efe5bf94dac952aad44fd3b9ebd21`，tree `d7e8953fb0f3eff949c3dbee1f9361b0b8f71804`。Reviewed OLD：`5845e8084ced280e51c51a4081ec8583a9c2ca39`，tree `23f92a9c446f5f0fbcee44df2f57d85df4dd0e3c`。正式 FIX_BASE 仍为 B12-C `8e67f780c204d593d89f364f585d2c6c2fe74631`，tree `ae2f491294eb4f97be6b75f75706c16279f9bf46`。`dbabf68ec00e7e368d594dfb49497ba5a9cbf578` 仅为派发 publication；管理后继没有替代实际被审 candidate。

本 PASS 不是 B09/B11 或其它 affected 签署，不是 G 登记、actual FULL 或 C 接受，不关闭 canonical 或非本地义务。OLD 的 NEEDS_REVISION 报告保持原身份；这里给出经过真实增量检查后的 NEW 结论，不自动转签 OLD。B030 计数 0，B16／WP67-A 仍按原归属和 B13-C 依赖保留。

## 两个返修问题的独立结论

**B13-R01／GIR-FD82-B027：修复满足。** 当前 WS-W35 明确 nil 取消精确返回 nil，空列表返回布尔 false，不能以同为 falsey 替代返回身份。当前 successor 轨迹 `/entry_submission/1/return` 为 JSON null，`return_identity=nil`；活动报名 P／活动队伍 P 均保留且不提交。空列表对象仍提交，进行中覆盖报名和活动队伍为空；未进行中只改变报名。新增非空列表与未进行中 nil 对照分别保持 true／nil。当前 B027 处置及 evidence-index 指向正确后继；旧 nil=false trace 原字节冻结，明确只作旧错误证据。

固定源入口、提交状态和 UI 取消范围重新定点阅读，确认正常回调返回 nil 时包装保留该值，初始 false 被覆盖。WP55、WS-W28/W29、正常 UI 人数确认门和工具／替换 UI 的空列表边界均未变化；B027 没有新增原稿范围。本项原 determinate recheck 的提交／返回／活动队伍四个读数同时满足。

**B13-AFFECTED-F1／GIR-FD82-B029：在 FULL 的本地 B029 控制内修复满足。** 此问题补足原 FULL 未变证据之外的真实入场影响；原 FULL 的旧 B029 局部判断不能压过 affected 发现。当前独立结论以新条款、固定消费者和当前接受接口为依据，仍由原 affected 角色另签其范围。

| 消费者／边界 | 独立静态核对 |
| --- | --- |
| 开场及普通入场最终扫描 | 全场速度序逐成员先真实降阶物品、再跨半 HP 能力；第一项假可继续同成员能力／后续成员，首个真返回才停止本次扫描。当前事件标记及物品／能力有效性门存在，不把任意降阶／扣 HP 当即时选择。 |
| 开场首命令前 | 录制初始属性先于正常入场；轮索引 −1、轮次表尚空时，入场消费者可选择后备 1 并追加 1。回放换人 cursor 在入场前已建为 0，同一入场消费者读取 1 后推进为 1；未读取首命令槽，也不把这个选择改记随机序列。 |
| 清选择与行动 | 入场清旧选择不取消以后首命令；新成员可按普通资格参加随后首命令。攻击后 BATONPASS／具名退出路径的当轮无额外行动限定仍保留，只用于那条攻击后路径。 |
| EJECTPACK 负选择 | 前置门通过后先消费，再询问。返回 −1 仍追加／回放消费；退出返回假、不提交替补，物品已耗且不回滚。假返回不等于成功退出，不要求停止本次扫描。此为条件返回边界，不承诺默认实时 UI 正常可以取消该强制询问。 |
| 退出能力负选择 | 同样不提交替补，保持该处理器的门与反馈；不新增 EJECTPACK 的物品消费。原稿“消费能力”按事件消费／触发理解，不要求移除或消耗能力身份。 |
| 回合末 | EJECTPACK／退出能力只召回、离场；当前退出处理器不即时询问或追加，后段实际补位询问时才追加／同点消费。 |
| 旧反向控制 | RC-W16 的设施 internalBattle=false 不可达确认；RC-W24 攻击 BATONPASS 追加／消费 1；RC-W25 随机 Roar/RedCard 与 Arena 候选恒假／顺序补位不询问，全部原字节保持。 |

逐入口保持天空摔投、对侧存活、训练家／野生分支、能离场、同属主健康非蛋未在场后备等各自门。严格整数半 HP 的定义重用同版本当前 WP49 既有接受合同；本轮独立回读事件标记／有效性／退出处理器，未把能力名字出现当资格通过。首真停止仅指**本次最终扫描**；退出后的递归入场链仍可能产生更多后续效果，RC-W26 已明确排除其后的其它退出或终局。

原／净 WP58 §5.2、未执行 RC-W26、当前 entry_final_scan 轨迹和 WP41／WP49／WP50 消费者导航一致。当前三份主接口定点回读，WP47-B 及原攻击邻近控制按准确版本复用；全部 owner 正式稿／原稿未变。详见 [repair-conclusions.json](repair-conclusions.json)。这些结论是静态推导，不是录制／回放运行成功。

## 完整八项当前处置

完整 [control-coverage.json](control-coverage.json) 逐项记录当前 qualified 字段、root／extension 裁决、最低修订与验收、此前精确语义证据、当前处置及保护检查，两个焦点没有取代 8／5 FULL 范围。

| 控制 | 主责 | 当前本地处置 |
| --- | --- | --- |
| GIR-FD82-003 | 否，B21 | 原本地净化证据复用；WP58 新时点条款仍为行为语言，没有新增源方法／继承组织。必要格式、索引、哨兵、BURMY 与共享副作用保持。PASS_LOCAL。 |
| GIR-FD82-B003 | 否，B11 | 精确 14 键、11 设置／3 消费者、suddendeath、sleep 成对及 skillswapclause 共同门证据完全未变。PASS_LOCAL。 |
| GIR-FD82-B010 | 是 | 加载后冰目标资格、q30/L50/阈值20/r19-r20、条款真前拒和 AI 独立差别的全部正文及反例未变。PASS_LOCAL。 |
| GIR-FD82-B018 | 否，B11 | 重新解析当前目录 47+35+28+27=137，保留旧 136 身份和 W22b；相对原基线 127 新增 10。其它域数字限定及语义／非本地义务不因计数关闭。PASS_LOCAL。 |
| GIR-FD82-B025 | 是 | 收到使用者／保存歌源、双 Lapras 两例决定 2、正终局退出与普通 selfKO 方向／爆炸假返回证据不变，返修不进入判胜语义。PASS_LOCAL。 |
| GIR-FD82-B027 | 是 | nil／false 精确 oracle、提交／活动状态、UI 门及当前后继一致；B13-R01 修复满足。PASS_LOCAL。 |
| GIR-FD82-B028 | 是 | Arena 开场与普通参与登记、累计状态、3/4/5 连续裁判、HP 基线及提示标志、PA-P28/RC-W25均未变，新 WP58 保留 Arena 门。WP67-A/B16不关闭。PASS_LOCAL。 |
| GIR-FD82-B029 | 是 | 完整 helper 闭包保留并补实际入场最终扫描、首命令前 append/consume、攻击行动限定、取消耗物、EOR 延后；原稿精确同步，W26 当前证据满足。PASS_LOCAL。 |

全部此前 accepted contributors 保持原边界：003 的 B04/B08/B09/B10/B12/B14/B15，B003 的 B09/B11，B010 的 B10，B018 的 B10/B11，B025 的 B09；其余三项没有旧 accepted contributors。复用精确未变已审材料，实际改变的返回与入口时点重新核查，不重新递归全部历史，也不按本地满足关闭其它 owner／共同根因。

## 差异、输出、许可与保护证据

本轮新 metadata 程序独立生成完整未过滤 [OLD-to-NEW.full.patch](OLD-to-NEW.full.patch)：**2,008,347 字节／52 路径，SHA256 `0319f0e2a4d4ed0c520724e9eeb67b84ef254f46abdd62ec54ed3f7982be0aff`**，与精确 publication 派发文件全字节一致。逐路径／树对象／新增 JSON／当前控制和绑定核验没有路径过滤。52 路径只有 3 正式变更，其余是 B13 作者／候选报告、历史派发收据及冻结 peer 副本，没有范围外路径。完整 FIX_BASE→NEW 聚合差异也另存；先前 FIX_BASE→OLD 质量和保护证据按 `e03b7c2…` 的准确记录复用。

十一输出的 FIX_BASE／OLD／NEW blob、SHA256、bytes 全部独立登记；当前作者 output 与 publication 全字节匹配。八份输出与 OLD 完全相同，三份改变为净化 WP58、combat catalog、原稿 WP58。净化 WP58 仅新增／限定 §5.2 时点及 §7 数量导航；combat 仅改旧新增 WS-W35、加 RC-W26及相应标题；原稿只改 §5.2。其余十一输出行为由原 FULL 准确字节和控制证据复用，没有把“未变”说成本轮再次全文阅读。

`scope-amendment-2` 精确 SHA `231c9f25df4dd64961fb9290ff52302782a9fdb8` 的四份 scope 输入与作者冻结副本逐字相等；WP58 整文件 before／proposed-after 相等，§5.2 外前缀／后缀逐字相等。独立重建批准序列化的 whole.patch 为 **3,211 字节，SHA256 `8d186d65c9eb2bc0e03a27728bfa0ea8476f4753bb863054b41cdb3b79459b0d`**，全字节相等。范围许可只用于确认可写字节；源正确性与质量来自上述独立检查。旧 scope1 四补丁许可不追溯扩围，B027 原稿、邻域正文和其它条款没有新改动。

36,139 个 OLD 已存在路径（仅排除实际 3 正式变更）在 NEW 的 mode/type/blob 全部不变，包含原作者证据／控制、旧错误 trace、旧 scope1 及其余接受材料。52 输入身份、完整 8 项控制文件、当前 successor 的 whole_control/original_required_fields/current_required_fields/root-extension/approved gate 全部与已审 OLD 相等；当前 evidence-index 的固定绑定、7 份 FULL/affected 原报告副本与原精确提交相等。没有以历史 pending 原稿提案否定当前 scope2 应用，也没有把历史值当当前 oracle。

combat 旧 136 分组 ID 的顺序和次数全部保留，只 WS-W35 行改变；新增 RC-W26 一行，总 137。creature 全 125 行全字节未变。W16/W24/W25、WS-W28/W29、PA-P16/P28等保护行不变。当前 WP41/WP49/WP50/WP47-B 的 binding 与 FIX_BASE／OLD／NEW 全部相等；本报告未给这些 owner 全域重新接受。正式路径的 OLD→NEW diff-check 通过；完整保存 patch 中嵌套 raw patch 上下文空白是准确证据，不以它声称整个未过滤流无空白诊断。

全部对象与差异证据见 [independent-metadata.json](independent-metadata.json)，新程序为 [new-incremental-metadata.py](new-incremental-metadata.py)，没有运行旧 author/reviewer 检查程序。

## 独立性、配置、源限制与发布

已先读 AGENTS.md，并检查环境相关 `.agents/skills`／SKILL.md，未发现本仓库适用技能。独立分支 `codex/cloud-dot-B13-review-2-20261010` 基于精确 publication，只新增 `candidate-review-2/`；不修改正式稿、原稿、旧报告、public/main/reference，也不创建额外／嵌套任务。普通 commit/push 后另作远端 ref/tree/全部报告字节读回，发布收据单独绑定报告提交。

保持请求配置 **gpt-6.1-sol / ultra / Standard / service_tier=default**；有效后端无可信回显，记 **UNVERIFIED**。沿用已批准 Plan A，不新增配置确认／认证门、quota probe 或另行 fallback，也不声称有效配置已认证。精确政策和角色边界见 [model-and-limits.json](model-and-limits.json)。

本轮准确定点重读 10 个固定参考文本文件：8 个由先前相同 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 缓存重校验身份并读列明范围，2 个必要文件新按不可变 raw URL 获取并独立核 blob/hash/bytes。记录范围不冒充完整文件语义阅读，固定 reference tree 身份沿用 qualified trace，未声称重新验证整个参考树。source log 列准确行段及当前接口阅读；临时源缓存不加入报告，不复制源代码片段。

reference／游戏／Ruby／编译器／转换器／生成器／反序列化器／历史程序／行为向量执行全部 0；runtime observations 与已证明 Demo chains 为 0。新 metadata 只作 Git/JSON/hash/text／报告读回，静态轨迹不是模拟或实测。U01–U10、G01–G12、AX01–AX20、树果条件 67、全部具名未读杯赛名单/pokemon_metrics、二进制／序列化、实际地图事件、素材媒体／字体／音频、Game/DLL/mkxp／宿主容量、备份/gen、插件／动态调用／别名／EventScene／动态阴影及真实 Demo 限制完整保留于 [source-reading-log.json](source-reading-log.json)。

本 FULL 门已通过；原 affected B09/B11 仍须各自独立评 NEW，其它有限 affected 当前处置不由作者或本报告自动延展 OLD。G/actual/C 仍按唯一登记者与原合同推进；actual FULL/affected 和两条当时接受前驱→actual、candidate→actual完整未过滤流仍必须独立核验。B16 不因本报告提前释放。
