# 第四轮全局独立审查：M10 UI 与演出资源消费

本次有界双向语义审查完成。保留 **4 项必修建议：3 项 P2、1 项 P3**，详见 [findings.json](findings.json)。GR3-M10-001～004 经本次源码、当前正文及消费者复读，均未发现原限定范围回归；历史 CLOSED 不变。本报告没有修改正式规格或参考，也没有运行游戏、参考程序或行为模型。

## 身份、基线与口径

- 审者：**M10 / thread `01a12ff1-a1b1-7212-84b3-c3fdcd6552a9`**；CLI PID `38287`，来自只读 `tasks/M10-launch.json`。这是父会话启动的独立 CLI 审者；不以内部 `/root` 标签代指父会话。
- 正式 B：`1f36475d22120a0d1175967d5b17d71fe8311d88`，tree `d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a`。全套 131 文件的字节身份/readiness 沿共享 `baseline.json`，导航为 `delivery/2026-10-12/formal-identities.json`。
- 参考 R：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。实际只读目录：`/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials`。
- 模型请求为 gpt-6-astra / ultra / default / 非 Fast；**实际配置回显 UNVERIFIED**。未探查配置、账户或凭据，未再启动 agent。
- `supported` 只表示 **supported_static**：列明前提下的源码/规格支持。材料存在、全文搜索命中、JSON 可解析均不等于行为运行通过。未执行信息独立写在 `execution_status`。

## 实际范围与来源发现

先盘点脚本和资源，再从消息/窗口入口、选项/PC/队伍/背包场景、战斗场景、图像与音频访问、转场定义发现能力；之后反向核对正文、附表、测试族及共享合同。对四个候选在全 131 正式文件做别名/语义反证检索，读取相关命中上下文，不只检查 WP 标题或 GR3 修订。

[source-scope.json](source-scope.json) 收录 **183 个相关来源候选**：53 项有明确语义阅读范围，99 项仅盘点，31 项内容未审（包括字体、翻译、二进制/宿主材料）。其中全脚本的 UI/资源消费者检索命中 107 文件；这个数字是检索分母，不是完整功能分母。每个文件分别记录实际阅读行段，**不因读过某段就标全文件通过**。

核心正式范围为 WP15、WP16 两正文、WP17 两正文、WP65 正文及两个附页、WP66 A/B/C、WP67 A/B；另盘点三个相关共享测试族、README/scope，并针对 WP02/03/56/74 和 Arena 测试交界留覆盖记录。[spec-coverage.json](spec-coverage.json) 共 23 个文件条目，明确 `contracts_checked` 与 `not_checked`。

能力样本为 **36 项：25 supported、10 partial、1 unresolved**。这是本次有界样本，不用于声称整个 M10 完整率。完整锚点、条件与结论见 [capabilities.json](capabilities.json)。

| 范围 | 本次关键正常/边界/异常核查 | 结论与限制 |
| --- | --- | --- |
| 消息、窗口、标签 | 替换顺序、忙/暂停/计时等待/全显、文尾图像、pg 实体路径、数量与命令竞争 | 四态及标签样本支持；普通选择器竞争、长词换行另列问题 |
| 字体、皮肤、长文本 | 三档字体、配置候选与绘制 Arial 层；皮肤冷取与显式设置；有无空格超宽文本 | 字体字形/平台注册未证；皮肤与折行存在有限合同缺口 |
| 标题/载入/选项/暂停/PC | 开场可跳阶段、标题离开等待、选项正常返回、语言整体选项落盘、保存失败重显、退出忽略保存结果、PC 各层游标 | 列明链支持；存档解析、备份与地图输入总调度不扩签 |
| 队伍/摘要/盒子 | Box Link 三门、旧持物快照、取回成功/取消；摘要蛋/普通备忘录、IV 并列决胜；暂持退出门 | U05 原范围支持；摘要所有交互/盒子所有负位置未全审 |
| 背包/PC 物品/商店 | 排序立即写、BACK 的三状态差别、借用浏览恢复、容量预检、共享/钱店/BP 同轮区别 | 所列 UI 时点支持；交易经济、所有 handler 不扩签 |
| 战斗 UI/动画 | 命令模式、成员子菜单与不可取消选人分层、目标取消回背包、浏览记忆恢复、消息列表、动画开关/并行派出/查找 | 原消息/Arena 修订支持；类型默认动画表缺数据 |
| 生命周期演出 | 进化最后更新轮 BACK 优先、成功消息先于物种写入、孵化恒真包装、交换卡片推进非取消、名人堂零容量、片尾首次不可跳 | 正常/取消/失败边界支持；全部逐帧与净化室完整链未新审 |
| 资源与音频 | nil/空名/直接缓存/包装加载错误分层；物种候选；BGM/BGS 零暂停差别、记忆别名、SE 选项二次缩放 | 逻辑请求与静态状态支持；实际加载/发声/暂停精度未证 |

### 全部具体 Transitions 与参数阅读

`Data/Scripts/009_Scenes/001_Transitions.rb:1–1929` 已完整阅读：**23 个具体效果定义、35 个兼容名称**，另审公共基类/入口。逐项身份、行段、固定时长、资源键见 [transitions-inventory.json](transitions-inventory.json)。

包括 BreakingGlass、Rotating/Shrinking、Splash、横/竖随机条纹、ZoomIn、八方向 Scroll、Mosaic、两种 Fade；SnakeSquares、四角 DiagonalBubble、水浪、全部单双三四球变体；VSTrainer、VSEliteFour、RocketGrunt、VSRocketAdmin。检查了大小写/保留扩展名、非正时长、旧过渡/中断顺序、固定时长覆盖、初始化异常与底层宿主重试的不同捕获范围。战前包装另读 `012_Overworld/002_Battle triggering/002_Overworld_BattleIntroAnim.rb:17–278,423–432` 的注册、地点/日夜选择、临时上下文和正常返回清理。

源端可读的分块、遮罩尺寸、波幅、缩放、随机运动、各阶段时间并未全部进入正式细节合同；WP16 §6.1 和战前 §7 明示精细图案/轨迹边界。对此保留 **partial**，没有把“存在完整名称表”当作所有演出参数已覆盖，也不据此要求复制原实现结构。alternate 自编排中段本轮仅盘点、未深查。

球动画另读 `011_Battle/004_Scene/007_Battle_Scene_BaseAnimation.rb:71–244,259–794`：两份 16 球种参数表、条带/开闭、颜色、默认粒子配置及 Master/Dusk/Net/Premier/Nest/Dive/Cherish 特例。确认“未知参数身份回 POKEBALL”**不等于球图片路径也回 POKEBALL**。捕获半径、色调、粒子组/时序等正式未完整承接；本轮登记 partial，不把“公共球动画非阻塞”套到整个投球链。

摘要固定主图中心 `(104,206)`、备忘录输入区域 `(232,86)`/宽 `268` 已追到消费者；指标文件读取了 BULBASAUR、CHARIZARD、PIKACHU 三个样本及指标应用定义。该阅读不等于整个 `pokemon_metrics` 或固定布局已验收。球/摘要精细数值与真正影响文本折行的规则分别裁定：后者另列 GR4-M10-003。

## 本轮问题与最小区分例

详细字段、源与 B 锚点、正常/异常对照、建议和验收要求均在 [findings.json](findings.json)；所有例子都是 **DERIVED_VECTOR / NOT_EXECUTED**。

| ID | 等级 / 类别 | 源端可确定的区分例 | 与当前正式集的差距 |
| --- | --- | --- | --- |
| GR4-M10-001 | P2 / 状态或时序错误 | 两项普通命令索引0、取消项2：USE+BACK返回1。逐位数字当前1、取消−1：同轮仍确认1；UP+USE可先改2再返回。范围[3,3]当前3，UP+USE+BACK改4后蜂鸣继续 | WP17仅单键/更新次序；U05数量表是其他控件，不能推出这两个入口的竞争裁决 |
| GR4-M10-002 | P3 / 数据或资源契约缺口 | 冷取所选缺图、系统 Custom 图存在：取 Custom；再缺才依次通用 Window/001-Blue01。相同素材条件下显式设置缺图后，逻辑结果为空而不再冷回退 | WP17转引WP15通用解析，未给皮肤专属候选与“未初始化/已设置为空”的差别 |
| GR4-M10-003 | P2 / 实现信息不足 | 假定 A/B宽8、空格宽4、请求宽12：AB仍同一行；A B把B移到下一行；带无动作pg标记也同样分流 | 标签附表把完整排版留在源函数，行满暂停例只有显式换行；缺不按字符硬拆长词的规则 |
| GR4-M10-004 | P2 / 数据或资源契约缺口 | FLAMETHROWER无精确映射；EMBER→10、SUNNYDAY→20、TACKLE→30时取10；逐级删除分别20/30/空。对方EMBER的OppMove→11优先 | WP67-A引用18类型六槽默认表，WP74继续回指，但整个正式集没有表内容 |

GR4-M10-001 与 GR3-M10-002 为 **new_scope_same_root**：旧物品数量/钱店/BP顺序仍正确，本轮新增普通命令与逐位数字入口。其余为 new；第二轮关联未知明确为 null，不猜 ID。没有把旧问题重新标 OPEN。

皮肤问题只要求逻辑候选合同，不声称失败后已释放旧定制图一定仍显示或必崩溃。长词问题只要求最小行为边界，不要求逐像素复刻或逐行翻译排版器。类型动画映射是资源身份数据，不是类层级/编排架构。未来产品是否改善参考异常仍由未来阶段决定，本次不代决。

## 全集反证与候选排除

[negative-searches.json](negative-searches.json) 保存所有搜索表达式、命中文件/行和结果。范围始终为 131 正式 Markdown，包含附表、测试、scope 和其他域共享合同；搜索结果本身不充当语义证明。

- 输入：读 WP17 §4/5/6.2.1/7.2、WP66-C §5.1、MG/B04-M/U05-QN、PC 消费者。已有光标命名和按件数数量优先序是明确反证材料，但适用入口不同；故仅保留普通命令/逐位数字新范围。
- 皮肤：读 WP17 §3.1/3.4/7.3、WP15 §3/5/7、WP65皮肤选项、WP02皮肤列表与编辑器目录缺失条款。Arial、空w、编辑器目录不存在均不能替代默认皮肤回退链。
- 长文本：读格式标签附表 §3/6、WP17自动行满暂停与多行输入、WP66-A备忘录、DT04/B04-M14及WP08非目标。命令转换的“换行”、编辑长度上限、显式换行均不补足自动折行。
- 动画：读 WP67-A §9.4、WP74 §15/16、WP03动画产物和 K35/K36。前向引用/编译映射身份/全缺失案例没有提供类型默认身份表。

没有新增必修的观察：具名转场身份没有缺项；VSEliteFour玩家图未在早退检查内已被战前 §7记录；进化末轮取消当前正文已正确；片尾局部“8帧”称谓按 WP16 统一单位可以解析为 8 个1/20秒单位，本次不把它扩成独立运行差异。球粒子/精细转场图案/完整字体字形未覆盖明确记为 partial/未审，不作为隐含已完成。

## 历史回归

固定导航：原 GR3 findings 为 `d5b6af3ebbabc57ed7fbdc2e1fb2c4736dbf9a65:review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/findings.json`；U05 actual 复审为 `1cb48da29e9363a2947eb16c75461bc3e76ae726:review/remediation-third-20261012-prepare/U05/actual-integration/independent-review/attempt-01/report.md`；正式接受记录为 `c2eb74c7cbcf8a190d5e902d871fbce44904efd6:review/remediation-third-20261012-prepare/registration/U05-formal-acceptance.json`。

| 原ID | 本次检查 | 结果 |
| --- | --- | --- |
| GR3-M10-001 | Party旧持物/BoxLink调用、Storage队伍取回、WP66-A/B与MV01–03 | supported_static；袋1/A空/B持物重复、BACK保取回、未嵌套正常三对照一致 |
| GR3-M10-002 | 共享/钱店/BP三段实际输入分支，QN01–04 | supported_static；原范围顺序及极限方向压过操作保持 |
| GR3-M10-003 | 战斗列表resume、普通消息skipAhead、窗口定义与TX01–04 | supported_static；原busy/暂停/全显前提保持 |
| GR3-M10-004 | Arena开场/补位/孤立复位调用搜索，当前WP56、WP67-A、K40/AR01–02 | supported_static；首开提示、3/4/5连续裁判一致 |

逐项源锚点和限制见 [regression.json](regression.json)。GR3-M11-001只检查Area显示的本域投影，不代签M11全域。GR3-M02-003保留 NO_REQUIRED_REVISION；没有重开紧急保存提示。GR3-M09-001 OPTIONAL 不在本次必修中。

## 材料、执行与未审范围

共享 readiness 为 PARTIAL_READY。无 Graphics/Audio/地图/完整Demo；字体8文件、18翻译文本和根BMP存在，但本轮没有解析字形、全面审读语料或运行这些资源。二进制动画库/映射没有被制造或加载；示例槽号是条件夹具。

明确可读未深审：世界地图图层/自动图块/灯光/动态阴影全域；所有文字输入模式与物理键绑定；摘要招式/缎带/标记/重学完整业务；盒子全部负位置/容量；图鉴搜索全空间；净化室与遗迹石完整UI；商店价格/赠品/库存算法；所有战斗目标/物品handler/退款与捕获领域；音频时长解析器；动画编辑器；所有PBS和翻译；动态插件与默认地图调用可达性。文件级清单及阅读范围在 source-scope.json，不用旧 PASS 填补。

[execution.json](execution.json) 单列实际工具结构校验和未执行类型；结构校验不构成行为验证。[progress.md](progress.md) 标记本域已完成。仅在本 M10 目录生成审查材料；未修改全局 Feature Matrix、正式文件、参考、历史报告或 Git 配置，未提交/push。

最终工具校验为 **PASS_TOOL_VALIDATION_ONLY**：8个JSON解析、必需字段/枚举/交叉ID、381个锚点路径及35兼容名称唯一性检查通过；正式文件tracked diff为0。实际命令、Python版本、UTC起止、输入/输出与exit code见 [validation-result.json](validation-result.json)。

本域产物已就绪，交主汇总者接收并对四项建议做一次独立针对性反证/去重；不请求提前修改正式规格或改变任何历史关闭记录。
