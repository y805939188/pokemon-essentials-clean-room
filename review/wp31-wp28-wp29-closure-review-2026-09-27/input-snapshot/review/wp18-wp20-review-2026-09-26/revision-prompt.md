# WP18–WP20 有限修订提示

你是提取/修订模型。工作区 `/Users/dingshinn/Desktop/pokemon-framework-reference/`。先读根及适用 AGENTS.md，完整读 `review/wp18-wp20-review-2026-09-26/report.md`、同目录 `input-manifest.json`、三包当前规格和当前 manifest。参考固定 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，reference 只读。

**本轮只修 WP18–WP20 的 9 个有界问题及直接传播，C01/C02 可同步维护；不执行 WP21 或其他新包。** WP17 管理回填已接受，WP01–WP17 限定 Reviewed 保持，不重做其已关闭行为。三包各自 REQUEST_CHANGES，修订后仍 ReviewPending，不自批 Reviewed。

## 1. 固定输入

| 文件 | 被审完整 SHA-256 | 字节数 |
| --- | --- | ---: |
| `specs/creature-rpg/wp18-creature-identity-species-ownership.md` | `7ab818e21831ef0b1d110c773c80ca3b85f1a40835fc0d67dee937158b18151d` | 34100 |
| `specs/pokemon-rules/wp19-attributes-ability-and-stats.md` | `3cba4bcda26c701a008ccc8352bae059ac15cca988bcca32f67e74c744d17698` | 30963 |
| `specs/creature-rpg/wp20-hp-status-moves-helditem.md` | `84c29af6b5f3c6fb18ae5cc801d7319887d0eb6b34f5139a53f8b6675c557897` | 29018 |
| `planning/feature-matrix.md` | `c7c09d7b01efed477bc4275e3438c689dc0fdb920d9a4c9d08746aafb96730b3` | 38071 |
| `planning/review-manifest-2026-09-19.md` | `cd384fd9b36bc7dd9f9e3b3a9fb3eedc94fbbfa2e232558cfc3dae66490a4025` | 61999 |

先复算实际完整哈希与字节数；若不同，对照本轮 `input-snapshot/`，记录差异再适用意见。保留旧被审版本与全部 review 原件，不覆盖报告/检查/快照。不能将本轮检查文件中的“算术匹配”当作三包已经通过。

## 2. 按稳定编号最小修订

以下源路径均相对 `reference/pokemon-essentials/Data/Scripts/`，准确行号、影响和最小验收以报告为准。

### WP18-R01：创建返回状态与中途赋空分开

查 `014_Pokemon/001_Pokemon.rb:496–534,1099–1108,1168–1177,1215–1224`。创建末尾重算已经求值并缓存表现 Nature；不要把初始化赋空当成最终输出。重算可补齐等级/Nature 缓存，WP19 的“不改变缓存/其它字段”总结同步收窄。创建形态复检后的默认招式重置仍以 `withMoves` 为前提。

补普通创建后 `hasNature?`、更改 personal ID 不重派 Nature 的场景；补 `withMoves=false` 且形态处理器不另外写招式时，不因复检执行默认招式重置。不得以此提前提取 WP21 的所有处理器。

### WP18-R02：外来赠送包装的默认与来源

查 `019_Utilities/002_Utilities_Pokemon.rb:131–136`、`014_Pokemon/005_Pokemon_Owner.rb:40–41`、创建来源段。外来 Owner 构造默认性别2，但赠送包装默认传0；已有个体保留来源方式，新建受命运开关影响。修对应入口表，保留 Owner 本身已正确的规则。

### WP19-R01：两个异色缓存分别求值

查 `014_Pokemon/001_Pokemon.rb:26–28,389–418`。普通异色与超级异色分别首次计算、分别缓存；普通异色置空不清超级异色。限定“超级必为普通”的数学前提，不把它写成所有显式覆盖和缓存状态的不变量。

保留已正确公式，补报告所列读取次序/id变化/单独失效的最小对照。野生重试只清普通异色的事实与上游摘要要一致。

### WP19-R02：非法经验输入的失败阶段

查 `010_Data/001_Hardcoded data/001_GrowthRate.rb:41–46,63–70`。非法等级分支与非法经验分支不能合并：后者诊断字符串引用未定义 level，在返回错误对象前就失败。分别登记 nil/0 等级与 nil/−1 经验的静态结果，保留合法换算。禁止运行参考表达式验证，也不修参考代码。

### WP19-R03：EV 配置默认与暂存额度

查 `001_Settings.rb:17,234–236`、`013_Items/002_Item_Effects.rb:714–727`、`001_Item_Utilities.rb:401–428`、`011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb:59–89`。

区分工具默认形参与默认世代8道具实参：维生素默认不再受100上限限制，仍守单项252/总510；100上限是另一配置。去掉无证据的 Hyper 双倍描述；Shadow 暂存剩余额度包含现有与已暂存值。补EV100默认增加/100上限变体拒绝，以及当前240+暂存10时再收益10最多增加2的静态对照。完整培养道具和 Shadow 流程仍留 WP28/WP23。

### WP19-R04：类型列表长度不是两项硬限制

查 `010_Data/002_PBS data/008_Species.rb:68,184`、`021_Compiler/002_Compiler_CompilePBS.rb:292–329`、`014_Pokemon/001_Pokemon.rb:312–334`。完整列表保存与查询没有两项截断；旧 type1/type2 只是前两项兼容读取。同步 WP18 字段目录的“1–2”表述。

补三个已登记不同类型的静态列表/成员/兼容读取对照。不要把这点扩成多类型战斗机制全部兼容，也不重开 WP03/WP04。

### WP20-R01：可更新的还原记录与持有物入口区别

查 `011_Battle/001_Battle/001_Battle.rb:151–154`、`002_Battler/001_Battle_Battler.rb:85–88,664–671`、`002_Battler/006_Battler_AbilityAndItem.rb:224–242`、`001_Battle/002_Battle_StartAndEnd.rb:506–509`、`003_Move/011_MoveEffects_Items.rb:15–21,179–186`。

修掉“不可变快照/消耗后也恢复”的保证，说明结束用的是可更新记录。补永久消耗不恢复、暂时打落保留原记录则恢复、永久取得可更新记录的对照。个体持有物 setter 未知项忽略，战斗入口未知项会清空，分开描述。

保留已正确的捕获入队登记和直接送箱边界；满队转送、所有效果族仍登记 WP38/WP50 前向引用，不能为了这条提前展开整个战斗包。

### WP20-R02：PP 直接字段、同步入口和 setter 失败时序

查 `011_Battle/003_Move/001_Battle_Move.rb:11,34–45`、`002_Battler/003_Battler_ChangeSelf.rb:104–119`、`014_Pokemon/004_Pokemon_Move.rb:37–46`。

包装对象直接 PP 赋值不是自动写穿；专门同步入口才按原关联/同标识/非变身条件写持久值。负提升计数例修为设置提升计数的调用本身就失败：基础PP20、旧计数0/当前PP20，设−6后计数已改而PP保留20，异常发生在该setter内。同步 WP19:305 及摘要/不变量/场景。总PP数值公式与已核对向量无需重写。

### WP20-R03：HP 清理与复活按前提/入口区分

查 `014_Pokemon/001_Pokemon.rb:246–249,280–283`、`003_Pokemon_ShadowPokemon.rb:22–25`、`019_Utilities/002_Utilities_Pokemon.rb:162–169`、`013_Items/002_Item_Effects.rb:560–587,618–629`。

HP0清异常通过 heal_status，蛋守卫仍适用；已有异常/计数的蛋写HP0时二者保留，进化准备标记清除。不要把非蛋结论提升为全个体恒真。

半血复活明确限定 REVIVE；MAXREVIVE/复活草回满，补上限100时50/100对照。只修本包错误概括，不提取所有道具流程。

## 3. 非阻塞维护可同步

- BATCH-C01：WP19 HP写回最后一行补旧HP上限；WP20:106 的写穿引用改到实际章节。核心HP公式及其余明确输入的算术结果保持。
- BATCH-C02：薄荷注册与设置消费者已经定位，WP19 未决改为“完整流程待WP28”，登记报告提供的来源；不把Hyper等其他未知一起关闭。

## 4. 自检、传播、交付

每项回应说明证据、实际修改位置、静态验收和保留边界。按 WP18→WP19→WP20 更新批内引用，检查反向摘要/不变量/场景和矩阵的直接传播；所有引用使用最终固定版本，注明尚未外审。不要整体重写三包或添加无关范围；报告 §2 已接受部分继承，下一轮只复核原问题及直接回归。

交付修订三包、逐项 `revision-response.md`、相对本轮 `input-snapshot/` 的 diff、完整 SHA-256/字节数、自检与传播记录，更新矩阵/manifest 的版本关系并保留旧被审哈希。回应与 diff 可在本 review 目录新建文件/子目录，但不得覆盖任何 reviewer 原件。未解决的实质问题如实保留，不能只改状态。

完成后统一送复审并停止。新三包保持 ReviewPending，WP01–WP17 限定 Reviewed 不变；不执行 WP21，不创建其他任务/并行 Agent，不发送消息给其他会话，不提交/推送。

全程不运行游戏、参考 Ruby/表达式、解释器/事件脚本、生成器、编译器、转换器、插件、真实网络或宿主输入，不操作地图/存档，不设计实现框架。允许安全自有文本/哈希/集合和独立算术检查，不执行参考代码。Demo、宿主、媒体、插件、U01–U10、WP78→WP79→WP80 出口继续保留；新三包不冒称 sanitized 交付。
