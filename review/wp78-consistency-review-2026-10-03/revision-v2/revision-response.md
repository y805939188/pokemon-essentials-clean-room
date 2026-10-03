# WP78 v2 逐项修订回应（R01–R08）

2026-10-03；规格提取方。依据 [report.md](../../wp78-stage-review-2026-10-03/report.md)（**REQUIRES_REVISION：8 项 OPEN——P2×6、P3×2**）、[findings.md](../../wp78-stage-review-2026-10-03/findings.md) 与 [revision-prompt.md](../../wp78-stage-review-2026-10-03/revision-prompt.md)：8 项按原编号原位修订；v1 交付材料（`../`）与审查原件全部留史未改写。作者状态：**REVISED_PENDING_REVIEW**——不自行 CLOSED、不自行 Reviewed。

修订对象身份（磁盘程序化实测）：

| 文件 | v1 被审（审查方 input-snapshot 冻结） | v2 当前 |
| --- | --- | --- |
| `specs/kernel/wp10-migration-failure-recovery.md` | `e6e44bfd5fd0eae008821529a4d1552ee48427a5ce914ffd00fafb5823e52dd6`／24,592（v1；更早前态 `07ccae9a`／23,833） | `dc6984a56971855167ee544fb930e7feb75904d205aea190d5c24dc84bcae462`／25,031（225 行） |
| WP78 v1 材料（11 份，`../`） | 见 v1 登记（第 136 轮） | **留史未改写**；v2 全部材料在本目录新建 |

两份新 diff 均对各自前态 patch 精确重建（临时目录验证，冻结件未动）：**增量**（审查方冻结 v1→v2，2 hunks）与**累计**（`07ccae9a` 前态→v2，3 hunks），见 [revision-diffs/](revision-diffs/)。

## R01（P3）WP10 前置依赖仍称 WP09 未外审（已修净）

- **v1 残留**：第 10 行「前置依赖｜WP09（持久状态目录，本批自检版本，未外审）」紧邻已改的第 9 行，同一头部给出相反状态。
- **修订位置**：WP10 第 10 行（注记同步为当前 Reviewed——2026-09-19 WP08–WP10 闭合复审通过，引用不复制）＋修订记录追加 v2 收尾条目（v1 身份 `e6e44bfd`／24,592 留史）。行为正文、场景、转换目录不变。
- **勘误（按提示同步，旧稿留存）**：v1 `../findings.md` 修订记录中前态哈希误写为「13d1379e…」——真实前态为 `07ccae9ab040cd6c85b22ea4a70bd0b1a8dfe72ce735aab68c82cec22fb0c917`（23,833 字节，v1 交付目录 revision-diffs/ 内冻结副本实测一致）；v1 文件不改写，本行为勘误记录。
- **验收对照**：增量 diff（冻结 v1→v2，2 hunks＝第 10 行＋修订记录）与累计 diff（`07ccae9a`→v2，3 hunks）均精确重建；无其他规格引用该注记（specs/** 检索）。

## R02（P3）计数与分母不能由交付表复算（已修）

- **交界数**：v1 矩阵实有 **39 个唯一 ID**（G1×5、G2×6、G3×5、G4×5、G5×4、G6×4、G7×4、G8×3、G9×3——与核验方 independent-counts.json 一致），v1 文本误写「30」。v2 补审与新增后**实际 51 项**（G1×5、G2×8、G3×6、G4×7、G5×5、G6×5、G7×5、G8×4、G9×6），逐 ID 可复算（[junction-inventory.md](junction-inventory.md)）；结论写「已核 51/51」，**不写成「51/51 通过」**。
- **三类计数分列**：异常事实数（具名异常保持的交界 **13 项**）／带异常标签交界行数（同 13，逐项见矩阵）／确证规格错误数（**1**＝WP78-R01）。
- **保护对象**：相对 WP77 v3 保护清单 30,874 个中 **4 个具名授权对象变化、30,870 个不变**（v1 误写 30,871 已更正）；审查开工保护 30,925/30,925 不变（沿核验方 mechanical-checks.json 口径）；授权变化集合本身正确、无越界。
- **文件构成**：109 份＝**88 主规格/合同文档＋21 附表/数据文档**——按文件名与头部角色逐份分类（[reading-log.json](reading-log.json)）；不用 109−84 推算（84 为文件名工作包 ID 数）。
- **阅读分母**：全文 1／定点章节 65／头部＋结构 22／结构骨架＋身份 21＝109，逐文件集合在 reading-log.json；四类不混用。
- **V01 枚举补全**：45 份＝20 份 Reviewed＋滞后 GR/N01 后缀＋25 份整体 ReviewPending；**WP69 族 4 文件**（slot-machine、voltorb-flip 两份主稿＋slot-reels、voltorb-layouts 两份附表），v1「WP69×3」枚举错误已更正（完整枚举见本文件 V01 节）。

## R03（P2）未审交界整体推给 WP79（已修）

- **修订**：建立 [junction-inventory.md](junction-inventory.md)——**51 项适用交界闭合清单**（主题/主责任/消费者/输入与配置/输出·失败·取消·还原/双方章节证据/状态）；状态划分：已核 51、待审 0、证据不足 0（全部归入既有 U01/U03/U05/U06/G01–G12 框架）、不适用 6 类（§2 具名理由，含纯公式所有权引用与两两组合枚举）。v1 的 E05/P08 兜底已删除。
- **补审（v1 证据不足三行）**：**G1-5** 补读 WP36 §3.1/58 行（编译错误与 each_of_version 错键反例）、WP76 §8.4（写出残留与编译往返边界）、WP54 §2（块注释示例不入默认集），与 WP04 §4.2/§5.5 互证一致；**G6-4** 补读 WP68（Triple Triad §T-G/T22 买卖次序）、WP69（§S-A/S-E 信用额与支付时点）、WP70（§M-A/M-E 无准入守卫/逐件入包）、WP71（§9 奖励属外部事件），与 WP24/WP27/WP06 资源·随机所有权互证一致；**G7-4** 补读 WP07 §1/WP07-D（非目标具名）与 WP64 §4、WP73-A §4、WP75 §3 各自失败语义，分层一致。
- **新增 12 项**（依赖/共享状态/消费者推导）：G2-7（WP37 漫游/雷达随机）、G2-8（WP59↔WP16 天气显示管线）、G3-6（WP18 拥有者结构）、G4-6（WP39 参战者初始化与两规则字典）、G4-7（WP44 异常/阶级分层写回）、G5-5（WP34 后代生成时点）、G6-5（WP60 产量与容量门）、G7-5（WP67-A↔WP40 命令合法性）、G8-4（WP72 调试写入路径）、G9-4（WP77 缺失素材↔WP15 缺失归一）、G9-5（WP59 场地资格↔WP12）、G9-6（WP65 保存 UI↔WP09 机制）。
- **全称具名范围核对**：junction-inventory.md §3 对「唯一/全部/无入口/均/不回滚」逐项给出适用范围；发现 v1「无清除入口」为错误全称，已随 R04 废弃更正。

## R04（P2）图鉴写入范围与清理入口（已修）

- **修订位置**：v2 [mappings.md](mappings.md) §1 术语行与 §2 状态行、[consistency-matrix.md](consistency-matrix.md) G3-4、[junction-inventory.md](junction-inventory.md) G3-4。
- **内容**：恢复**战斗侧限定**（「拥有」仅捕获流程写入、击倒不写）；获得侧**九入口**分列（赠送/静默加入/仅入队/仅入队静默/外来赠送/孵化/进化/分裂式复制/交换——WP62 §3.2 52–60 行；仅入队静默 see_form=false 不写见过仍写拥有）；补**公开整体清理 clear**（§3.4 80 行：清全部记录集合——见过/拥有/形态/蛋/末次/暗影/两计数，**保留区域解锁表**，随后刷新）；另记「最近见到」总覆盖入口与 should_refresh=false 不重算边界。
- **对照**：v1「拥有仅捕获写入」扩大战斗侧限定、「无清除入口」与公开清理相反，且与 v1 自身 G3-4 行不一致；WP62 责任规格既有正确描述未改动。
- **独立静态向量（沿用核验方）**：仅入队静默获得 see_form=false 仍写拥有；调用 clear 后记录清空、区域解锁保持。

## R05（P2）Mega/Primal 解除入口（已修）

- **修订位置**：v2 mappings.md §2 状态行、matrix G4-3、inventory G4-3。
- **内容（按 WP22 §6 78–87 行、W17/W23 逐入口）**：普通换下**不统一解除**（再上场保留形态；副本视为濒死仅收尾能力，持久 HP 不归 0）；真正濒死→解除（先 Mega 后 Primal，改持久个体）；捕获成功→解除（WP38 主）；捕获满队换出→本入口自行解除；**正常战斗对象终局（裸战斗/回放）不统一解除**；世界战斗返回→玩家当前全队＋具名伙伴解除（对方原队伍不在该循环）；设施单场包装返回→双方等级恢复→治疗→解除→恢复旧物品（解除在恢复旧物品前）。
- **对照**：v1「换下/濒死/终局/战后包装分入口解除」把不解除的两个入口（普通换下、裸终局）并入解除入口，会得出错误状态转换；WP22 合同保持未改。

## R06（P2）编译/反写拼成自动执行链（已修）

- **修订位置**：v2 mappings.md §1 术语行/§4 时序行、matrix G8-2、inventory G8-2。
- **内容**：拆为**具名入口**——同次调用真实先后（WP75 `compile_all`：编译 PBS→编译动画→`compile_trainer_events`→翻译收集→消息保存/载入；重编译标志吸收 `import_new_maps` 返回值；WP76 生成写出：更新 `.dat`（先记录默认列表存在性）→刷帧→截断总 PBS 交错写）；**可另行调用的往返能力（文字说明非顺序承诺）**：`compile_trainer_lists` 把 PBS 编回 `.dat`；PBS 目录缺失时编译检查先 `load_all` 再 `write_all`（WP04 §3.1/§5.5 150–158 行）；调试菜单主动导出 `write_all`/单个 `write_*`。**否定边界**：WP76 写出在反写及刷帧后结束、没有自动接续编译（reference `003_ChallengeGenerator_Trainers.rb:185–211` 只读核对）；写出成功不证明编译器已重读或校验输出；常规编译完成不固定触发反写。部分落盘保持（WP76 后续失败不撤销先前数据；编译/反写不互逆）。
- **对照**：v1 时序行把「编译总管线之后接 WP04 写回」与 WP76 写出/反写/再编译写成连续链；WP04/WP76 责任规格未改。

## R07（P2）两套证据分类与批准状态混同（已修）

- **修订位置**：v2 mappings.md §1 术语行＋新增 §5 对照表、matrix G9-1/G9-3、findings V01 措辞（v2 新材料统一改为「当前批准状态及批准范围」）。
- **内容**：WP01 **五档证据等级**（已定位/静态确认/数据样本确认/运行确认/待验证——wp01:39）与 WP77 **demo 证据链四档**（①配置事实/②静态能力证据/③事件证据链/④运行观察——wp77:62）分别标明责任规格、含义与使用场景；语义对应（已定位≈①、静态确认≈②、运行确认≈④、待验证＝未取得证据）与**不能一一等同之处**（WP01 数据样本确认在 WP77 四档无对应——WP77③是事件链证据而非数据样本；数据样本确认与③＝0 并存不矛盾；Reviewed 是限定范围审查状态、不是运行确认）。「档位不提升」为共同纪律不等于标签逐字相同。
- **对照**：v1 把四档归于 WP01 并称「逐字相符」、以中央登记定义「行为真值」；WP01/WP77 分类本身未统一重写。

## R08（P2）成长前提混入继续资格（已修）

- **修订位置**：v2 matrix G5-1、inventory G5-1、mappings.md §4 成长分配时序行。
- **内容（WP42 §2 22–23 行、§4.1 55–59 行、§4 44 行）**：**继续战斗资格**（两侧参与队伍可战斗成员计数，非在场席位；伙伴计入玩家侧继续资格）与**成长入口守卫**分开——先查野生胜利音乐条件→**非内部战斗或经验开关关即退出**（不分配 EV/经验、不清参与者记录）→逐对方对象须**非空参与者记录**且当前濒死或临时捕获标记真→接收者须当前可战斗且属**玩家本人队伍段**（伙伴不进经验分配循环）→统计有效参战者核对所有权→每人先 EV 后经验→该对手处理后清参与者记录防重复分配；捕获临时标记的设置/撤除时点（§4 成功捕获流程）。
- **独立静态向量（责任规格既有，未运行）**：经验全体有效、玩家有可战斗成员，但对手参与者记录为空→早期跳过该对手分配；非内部战斗或经验开关关闭→不因双方计数满足而分配。
- **阅读归属更正**：v1 G5-1 仅列 WP42 §6/头部、WP30 友好度定点，不足以支撑成长资格结论；v2 补读 WP42 §2/§4.1/§4 全文段。

## V01（已核·有意管理决策；v2 枚举补全与措辞修订）

**45 份头部滞后全集**（程序化扫描，逐文件可复算）：

- **20 份 Reviewed＋滞后 GR/N01 ReviewPending 后缀**：wp04-pbs-lifecycle（GR-001）、wp08-localization（GR-002）、wp10-migration-failure-recovery（GR-003）、wp12-terrain-movement-vehicles（GR-004＋GR-011）、wp13-map-events-npc-followers（GR-005）、wp14-random-dungeons（GR-006）、wp15-resource-matching-and-audio（GR-007）、wp19-attributes-ability-and-stats（GR-016）、wp20-hp-status-moves-helditem（GR-008）、wp23-shadow-hyper-and-purification（N01 子项）、wp24-player-trainers-partners（GR-009）、wp26-acquisition-gifts-and-script-trade（GR-010）、wp36-wild-encounters-and-modifiers（GR-011）、wp41-switching-positioning-and-escape（GR-013）、wp42-growth-end-of-round-and-battle-outcomes（GR-013）、wp47-b-switching-control-and-item-changes（GR-014）、wp52-a-generic-numerical-and-status-evaluation（GR-015）、wp52-b-field-damage-healing-and-target-evaluation（GR-015）、wp58-battle-recording-and-playback（GR-013）、wp60-berry-plants（GR-012）。
- **25 份整体 ReviewPending**：wp37-roaming-and-poke-radar、wp53-safari-and-bug-catching-contest、wp61-field-passive-effects-and-blackout、wp63-pokegear-map-music-and-phone、wp64-mail-and-mystery-gift、wp65-title-load-options-pause-and-pc、wp66-a-party-and-summary-ui、wp67-a-battle-interaction-and-presentation、wp67-b-lifecycle-presentations-and-history、wp72-debug-contexts-and-controls、wp73-a-content-editors、wp73-b-world-editors、wp74-battle-animation-authoring-and-exchange、wp75-project-conversion-and-authoring-tools、wp76-facility-content-generation-and-simulation、wp77-demo-evidence-and-capability-coverage、wp68-duel、wp68-triple-triad、wp69-voltorb-flip、wp69-voltorb-layouts、wp69-slot-machine、wp69-slot-reels、wp70-lottery、wp70-mining、wp70-mining-data。

- **决策链（不变）**：各通过报告「无须重写主稿字节」、WP68–70 backfill-register「旧头部不当当前结论」、manifest「当前／历史提交状态」分记、第 134/135 轮 WP77 回填。**v2 措辞修订**：中央登记确定的是**当前批准状态及批准范围**，不替代责任规格与来源证据定义行为（R07 同步）；本决策不扩为「所有正文中的旧状态注记均自动免责」——WP10 的 WP09 依赖注记即反例（R01 已修净）。
- **不要求改写 45 份主稿字节**；后续各包新修订时顺带同步其头部。

## E 系（证据不足具名，v2 保留并收窄）

| # | 事项 | 现状 | 补证条件 |
| --- | --- | --- | --- |
| E01 | 备份数据集启用路径与世代组合兼容 | U03/U06 框架内 | 专用读取/切换证据 |
| E02 | 帐篷档（60）登记路径的脚本外调用者 | WP55 具名不可达分支 | 完整 demo 事件材料（U01 系） |
| E03 | 全满兜底失败分支运行表现 | WP38 具名静态登记 | 运行验证阶段 |
| E04 | 插件组合、工具运行与 demo 编排 | 各包 Inventoried 子范围 | 运行/素材证据 |

（v1 E05「矩阵之外关系整体推给 WP79」已随 R03 删除——51 项清单与 §2 不适用清单取而代之。）

## 总体自检结果

- 两份 WP10 diff 精确重建（增量 2 hunks／累计 3 hunks，临时目录验证）；WP10 行为正文/场景/转换目录不变。
- 51 项交界清单逐 ID 可复算；全部「唯一/全部/无入口/均/不回滚」全称带具名范围（inventory §3）。
- v2 新材料净化扩展扫描 **0 命中**；全部本地链接可解析（见 [checks.json](checks.json)）。
- v1 材料与审查原件字节未动；WP22/WP42/WP62/WP04/WP76 等责任规格既有正确描述未为迎合汇总反改。
- U01＋G01–G12 保留；③已证事件链＝0、④运行观察＝0；来源异常保持，未用「待运行」掩盖可由文本确认的错误。
- 状态：**REVISED_PENDING_REVIEW**——8 项均不自行 CLOSED；送 WP78 v2 独立阶段复审。
