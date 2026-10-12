# M05：玩家与物品 — 第四次全局独立审查

## 结论与身份

本次完成 WP24/25/26/27/28/29/64 的**有边界双向静态语义审查**。保留 **1 项 P2 REQUIRED：GR4-M05-001**（主动 PP 补给的战斗濒死资格缺口）。29 个能力样本中 28 个在列明分支获 `supported`、1 个 `partial`；`supported` 仅指 **supported_static**，不是本域全能力或整文件通过率。没有给不可读材料或可读未审部分补签。

审者为 **M05 / thread `01a12fdc-b1dc-7f62-8311-aa6a002b9432`，PID 64300**。身份来自只读 `../../tasks/M05-launch.json`；父会话 thread 为 `01a12fc2-e8c0-7e43-a721-ccfe659d75c8`，两者不混同。请求 gpt-6-astra / ultra / default、禁 Fast；实际模型、推理与服务档位回显 **UNVERIFIED**。

- 正式基线 B：`1f36475d22120a0d1175967d5b17d71fe8311d88`，tree `d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a`；正式身份导航为该基线 `delivery/2026-10-12/formal-identities.json`。
- 参考 R：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。参考根 `/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials`，只读。
- 采用共享 `../../baseline.json` 的逐字匹配与 `PARTIAL_READY`，未重核整仓。脚本、PBS、翻译与部分二进制存在，不代表解析或可运行；缺完整 Graphics/Audio/地图/Demo，宿主运行未成立。
- 未改正式规格、参考、历史、全局矩阵或配置；未提交/push、未启动其它 agent、未下载或访问账户。唯一写入为本 M05 目录。

## 方法、盘点与边界

先读 AGENTS.md、共同任务书和共享身份；再以参考文件目录和实际入口发现能力，而后与正式正文、测试和共享合同比较。盘点覆盖参考全部 432 tracked 路径（312 脚本、73 PBS，包含备份）；通过全脚本的背包增删、获得/交换、伙伴、邮件、礼物和储存/价格标识追消费者。其中40文件包含本次具名语义阅读范围，101路径被列为本域候选/消费者或语义样本。此盘点分母不是语义覆盖分母。每个可读文件是否只盘点、具体语义阅读范围，均见 [source-scope.json](source-scope.json)。翻译18文件只盘点，二进制未解码；Gen5–8/Shadow备份只登记与少量身份定位。

完整 131 份正式文件均列在 [spec-coverage.json](spec-coverage.json)，包含七份本域正文、三份合并测试目录以及交界/附表/范围声明。七份本域正文已阅读；正文里未沿源深查的条款、测试目录中的非本域部分与未选向量仍明确列为未审。全套131用于反证搜索，不意味着131均做了语义审查。

实际深查选择正常、边界、异常和世代对照，主要依赖链为：

| 来源/能力组 | 本次主查 | 必要消费交界 |
| --- | --- | --- |
| 训练家、玩家、NPC数据 | 身份、资源、元数据回退、装载失败、伙伴注册 | 伙伴参与/战后治疗、类型/版本数据 |
| 队伍、盒子、获得、脚本交换 | 容量、同引用搬运、治疗、最后可用守卫、获得入口差异 | 仓库UI、图鉴登记、演出收尾/最终替换 |
| 背包与PC道具 | 部分写入/全有全无、替换、游标、登记、PC预检 | 拾取/收到/奖品、快捷菜单、给予菜单 |
| 主动使用与装备 | 上下文分派、HP/状态/PP/EV、机器、野外工具、持物/邮件 | 数量、消费、战斗登记/退款、教学初始记录 |
| 商店与兑换 | 金钱/BP、价格覆盖、数量、部分回退、赠品 | 钱包钳位、库存列表原地过滤、显示与实扣 |
| 邮件与神秘礼物 | 快照、信箱容量、写作取消、下载候选、领取与作者会话 | 存储/背包、载入解锁、共享个体和落盘范围 |

本次没有新增提取或修复正式规格。新发现先完成源端 caller、别名/覆写、默认数据与全正式集反证，再列问题。

## 新问题 GR4-M05-001（P2 / REQUIRED）

**PP补给缺少战斗中的濒死拒绝与非战斗可恢复的区分。**

固定源事实：

- R `Data/Scripts/013_Items/003_Item_BattleEffects.rb` **155–186**：ETHER/MAXETHER/主动 LEPPABERRY、ELIXIR/MAXELIXIR 的战斗资格均先要求目标可战斗。可战斗的定义在 R `Data/Scripts/014_Pokemon/001_Pokemon.rb` **264–270**：非蛋且 HP>0。
- R `Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb` **239–285**：可选择非蛋后备，招式型再选招；没有把所有濒死目标提前排掉。R `.../001_Battle/009_Battle_CommandPhase.rb` **100–137**：资格不通过就在登记和扣库存前返回；拒绝仍留成员选择。
- R `Data/Scripts/013_Items/002_Item_Effects.rb` **632–684** 与 `001_Item_Utilities.rb` **367–382、644–686、710–775**：非战斗相应流程只需通过非蛋/Hyper等前门和PP恢复条件，没有存活要求；恢复成功后消费一件。
- 默认身份可达依据是 R `PBS/items.txt` **3294–3333、5242–5250**，以及 `PBS/moves.txt` 的 **TACKLE，5326–5336（总PP35）**。不是只有自定义处理器才出现的区别。

最小静态对照（全部 `DERIVED_VECTOR`，`execution_status=NOT_EXECUTED`）：

| 独立初态/入口 | 固定参考结果 |
| --- | --- |
| 普通内部战斗；可行动A与濒死后备B；B非蛋非Shadow非Hyper，HP0/100、TACKLE0/35；ETHER1；A选择给B补该招PP | 无效果提示，未登记物品；B仍HP0/PP0，ETHER仍1 |
| 同字段的独立场外初态，从普通背包对B选同招 | B仍HP0，PP变10/35，ETHER变0 |
| 只把B改为HP1/100、PP0/35，保持其它条件 | 两入口均可恢复；战斗先登记扣1，稳定执行后PP10 |
| B存活但PP已满，或取消选招 | 按各自已有失败/取消门不消费 |

正式缺口在 B `creature-rpg/wp28-item-use-and-training.md` **§5.2（202–206）**：只有PP条件、回复量及战斗同步。`§3.5` 给出资格家族框架，未定义本族存活门。测试目录 `creature-rpg-wp27-28-29-30-33.md` **IU-07（51）** 未区分上下文与HP。由此直接实施统一PP缺口规则，会在战斗中恢复濒死者并消耗物品；反过来统一加存活门则会拒绝源端允许的场外使用。

已做全131文件的英文身份和中文别名反证，并读命中上下文：[negative-evidence.json](negative-evidence.json)。WP20 §5.4–5.5是底层恢复/同步，WP40 §4.2和WP67-A §5是通用资格和交互，均回指具体道具。WP51 §4的“存活AI、缺少招式索引导致异常”没有定义人手选招后的濒死反向结果，也未覆盖ELIXIR族；WP50的持有LEPPA是另一消费者。源端 Shadow 覆写 **163–178** 不改变本例普通非Hyper目标的结果。全脚本五身份搜索未找到抵消这些门的覆写。

建议只补参考事实：WP28按上下文列五种PP补给资格，补战斗拒绝/场外成功/存活/满PP/取消向量；保持现有量值、同步与退款条款。无需指定类、接口或修改参考。完整字段、验收条件、影响与排除项见 [findings.json](findings.json)。与第三轮两项及退款残留不同根；第二轮关联ID未知，明确为 null，未猜测。

## 已审支持与反证结果

完整逐样本的前提、分支、固定commit锚点和限制见 [capabilities.json](capabilities.json)。下表用于导航，不能把 `supported` 扩成未列分支也通过。

| 能力样本 | 主题 | 结论 |
| --- | --- | --- |
| GR4-CAP-M05-001 | 训练家标识、玩家资源域及许可初态 | supported |
| GR4-CAP-M05-002 | 玩家元数据按编号回退与字符集后备链 | supported |
| GR4-CAP-M05-003 | NPC 训练家装载、缺失与默认个体数据 | supported |
| GR4-CAP-M05-004 | 伙伴注册、参与谓词及战后资源清理 | supported |
| GR4-CAP-M05-005 | 队伍过滤、移除和最后可用成员 | supported |
| GR4-CAP-M05-006 | 基础盒容器同对象搬运、容量及存入治疗 | supported |
| GR4-CAP-M05-007 | 仓库 UI 的拿起、存入、放下、交换及释放守卫 | supported |
| GR4-CAP-M05-008 | 地区储存的缓存、可得性与代理异常 | supported |
| GR4-CAP-M05-009 | 普通/静默/仅入队/外来/蛋的获得入口 | supported |
| GR4-CAP-M05-010 | 脚本交换准备、演出后替换及选择器 | supported |
| GR4-CAP-M05-011 | 背包与共享容器的部分写入/全有全无及替换 | supported |
| GR4-CAP-M05-012 | PC 道具存取、数量选择与懒初始化 | supported |
| GR4-CAP-M05-013 | 快捷登记、候选过滤与游标恢复 | supported |
| GR4-CAP-M05-014 | 装备给予、取回与邮件取消后的库存状态 | supported |
| GR4-CAP-M05-015 | 主动道具的四入口、返回值与库存扣减时点 | supported |
| GR4-CAP-M05-016 | 主动HP、状态、复活的世代与上下文差异 | supported |
| GR4-CAP-M05-017 | PP 补给按上下文的濒死资格、选招与消费 | partial |
| GR4-CAP-M05-018 | EV培养数量层、100阈值和部分成功消费 | supported |
| GR4-CAP-M05-019 | TM/HM/TR教学入口与最初招式记录 | supported |
| GR4-CAP-M05-020 | 野外喷雾、HONEY和离洞工具消费 | supported |
| GR4-CAP-M05-021 | 金钱商店购买回退、出售钳位和球赠品 | supported |
| GR4-CAP-M05-022 | BP商店、显示半价与会话价格覆盖 | supported |
| GR4-CAP-M05-023 | 邮件快照、信箱容量与同对象流转 | supported |
| GR4-CAP-M05-024 | 神秘礼物解锁、下载候选过滤与重复ID | supported |
| GR4-CAP-M05-025 | 神秘礼物领取的容量与提交先后 | supported |
| GR4-CAP-M05-026 | 礼物作者侧创建、管理会话与共享个体 | supported |
| GR4-CAP-M05-027 | 探测仪的矩形窗口、平局、方向和三路响应 | supported |
| GR4-CAP-M05-028 | 个体毫米尺寸数学辅助 | supported |
| GR4-CAP-M05-029 | 战斗消费登记、失败退款残留与后续清理 | supported |

重点排除的表面差异：

- 邮件替换写作取消时袋中旧物品净增加、先取旧邮件再取消新给予的部分提交，已由WP64 §3.3与MG-07/08承接；不另立问题。
- 个体礼物在容量失败前已改PID/来源/时间但仍未领取，已由WP64 §6.1与MG-21承接。物品礼物先预检，不能套用普通直接入包的部分添加。
- 脚本交换新图鉴页的两处收尾调用及宿主重复释放未证，已由WP67-B §3.3/§5承接；不把WP26的简化流程单独判缺失，也不宣称必定二次进化。
- 地区储存缓存已沿到地图地区查询及缓存更新；地图缺地区返回负值后报错有支持。代理移动只复制、删除和解锁失败亦已在WP25。默认存档创建基础储存，不能声称地区对象已在普通玩家链启用。
- 默认TM57实际数据为TR，背包教学与队伍教学的最初记录/统计差异已写在WP28 §5.4和IU-58，未凭显示名猜不可消费。
- 商店分支先完成商品入袋再扣资源，容量失败逐件撤回；赠品不参与回退；BP数量显示先对单价整除2再乘数量。WP29及SH向量已区分这些次序。

## 历史回归

[regression.json](regression.json)仅对本域GR3两项逐条列当前锚点、旧验收固定引用、本次实际标准及限制：

1. **GR3-M05-001**：重新比尺寸源243–271与当前WP18 §7.4、WP24转引、U03-SZ。确认位输入、15区段、两整数阶段、203/209/210mm和s113反向对照；默认段起点65410但基准65510保留。仅可得辅助，未当作默认玩法。
2. **GR3-M05-002**：重新比候选窗口/Manhattan/平局与三路响应、默认工具数据，再核WP28 §3.3-R01和U03-IF。确认无候选仍计数且真返回、脚下等待/转向及不自动拾取。

两项在本次检查标准内 **supported_static，无回归发现**。旧U03实际审查位于commit `08fc8828229c14ab4a540db417d08194ba194a31` 的具名 per-id-verdicts；U03接受收据 `c2eb74c7cbcf8a190d5e902d871fbce44904efd6` 当时只是实际接受（final_CLOSED=false），不混同最终关闭。最终effective CLOSED23由当前交付导航指向 `98e49a592c9e82b1e53d3f1fd403ba2ad0935983` 的最终激活收据。保持这些历史身份，不重新关闭、不迁移签名。

对GR3-M07-001仅重读物品登记/退款、下轮直接清选择、正常终局取消三个消费交界，当前WP28已承接；没有重审完整毒伤裁判链。GR3-M10的Box Link持物/数量输入仅作相关来源和正式导航，不转签其整链通过。GR3-M09-001 OPTIONAL及GR3-M02-003 NO_REQUIRED_REVISION保持，未重开。

## 限制、可读未审与证据

- 源可读但未穷尽：全部NPC/物品/物种/形态PBS条目，备份整套切换，翻译内容，所有主动道具与别名组合、21薄荷数值、融合工具全部形态提交、被动持物、AI、捕获/寄养/竞赛/净化/挖矿等发放和消费整链。
- WP24的完整战斗奖金/罚金、语言/用户名建议、逻辑音频、煤灰、雷达组合；WP25墙纸读取兼容和全部UI输入；教学遗忘完整循环；真实商店库存/赠品容量变化；HTTP运输与载荷反序列化，均不因本次邻近能力支持而通过。
- 主流程可读不等于宿主可达。未执行任何参考、独立行为模型、测试向量、UI/战斗/真实Demo。未编译PBS、反序列化存档或礼物，未访问示例URL。正常响应前提之外的资源故障、插件重入、异步改状态及中断恢复未穷尽。
- 证据字段只使用 `SOURCE_STATIC`、`SPEC_STATIC`、`DERIVED_VECTOR`；未执行单独写 `execution_status`。最后JSON结构/路径/引用检查只记 `TOOL_VALIDATION`，不能作为行为测试或本域运行能力证据。
- 没有发现要求照搬源架构或源码的新增净室问题；此结论只限所读行为样本，不给全部131文档做自动净化认证。报告只记录路径、符号、事实和静态向量，不复制源码。

## 交付物

必需产物：[report.md](report.md)、[capabilities.json](capabilities.json)、[spec-coverage.json](spec-coverage.json)、[findings.json](findings.json)、[regression.json](regression.json)、[execution.json](execution.json)、[progress.md](progress.md)。补充 [source-scope.json](source-scope.json)、[negative-evidence.json](negative-evidence.json)、[reviewer-identity.json](reviewer-identity.json)。生成与结构验证脚本仅服务本审查产物，不是新框架实现。

最终产物结构验证已通过：8份JSON可解析、能力/问题交叉引用与全部参考清单路径有效，tracked diff为空。参考清单已用NUL分隔处理非ASCII路径；两次结构检查都仅属TOOL_VALIDATION。

本域审查完成，停止扩张范围。新问题等待主汇总者接收及一次独立针对性反证；本审者没有修正式文件或将问题状态写入全局矩阵。
