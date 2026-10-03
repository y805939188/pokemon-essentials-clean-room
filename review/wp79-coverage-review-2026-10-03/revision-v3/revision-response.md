# WP79 v3 逐项修订回应（R01/R02/R03；R04 已关闭）

2026-10-03；规格提取方。依据 [report.md](../../wp79-stage-review-2026-10-03/recheck-v2/report.md)（v2 复审：**REQUIRES_REVISION——R04 本次关闭，R01/R02/R03 仍 OPEN（3 项 P2），无新增编号**）与 [revision-prompt.md](../../wp79-stage-review-2026-10-03/recheck-v2/revision-prompt.md)：3 项按原编号原位修订；R04 保持关闭、不重开；WP78 的 11 项关闭与既有具名限定批准保持；v1/v2 材料、独立审查与冻结快照全部留史未改写。作者状态：**REVISED_PENDING_REVIEW**——不自行 CLOSED、不自行 Reviewed。

## R01（P2）训练家卡开场表残留「水平垂直居中」（已修）

- **残留**：[specs/ui/wp65-trainer-card-appendix.md](../../../specs/ui/wp65-trainer-card-appendix.md) §3 开场表仍写「水平垂直居中」，与已更正的 §4 相反。
- **修订位置**：§3 开场表训练家正面图条目——同步为「**横向对齐到 128 宽区域、底边保持 240**（放置规则见 §4）」。§4 已接受的更正（横向对齐、底边 240、装扮编号消费）与 TC01/06/07/08 已接受的向量全部保持，未从头改写。

## R02（P2）引用清单之后的覆盖判断（已修）

- **残留**：v2 的 290 行仅凭规格文件名命中标为已覆盖，缺少实际行为范围、章节和阅读证据。
- **修订**：建立 [source-judgments.json](source-judgments.json)（312 行，逐路径：实际行为/数据子范围、承担规格章节、批准依据、覆盖判断、剩余处置）——
  - **分布**：已覆盖（行为合同在案）**270**／部分覆盖（身份与评估合同在案）**20**／已补提取（场景/机制合同在案，待复审）**3**／行为层已覆盖（文件级仅定位）**2**／不适用（具名理由）**17**／**仅定位 0**／**未引用 0**（grep 逐路径复核＋短名复核修正后，全部 312 个路径均有覆盖判断）。
  - **分层示例（按复审点名）**：`001_Settings.rb`/`002_BattleSettings.rb` → WP02 §4 词典＋附表检索索引（各消费者实际消费范围按各领域包批准分层）；`abilities.txt`（PBS）→ WP34/WP35 孵化加速三个特性样本（abilities.txt:162,199,976——FastEggHatching 三特性）＋WP48 §B–E（能力计算与阶段触发）＋WP19 §4（特性派生）＋WP44（异常/阶级状态交界）——**分层在案，不标「数据内容已读全覆盖」**；`001_Transitions.rb` → WP16 §4.2/§6（过渡调用与时序守卫在案；**引擎内部算法为实现细节，不逐行提取**）；`009_Scenes/002_EventScene.rb` → WP13 §B＋WP65-controls-help-appendix（父级输入分发与生命周期在案）；AI 评估系列（`005_AI/`×7＋`006_AI MoveEffects/`×9）→ WP51/WP52 行动选择链与效果身份/评估合同在案（**内部评分算术/实现细节为实现细节**）。
  - **命名口径**：字符串匹配统计（grep 命中）＝**候选引用证据**（仅证明被提及）；阅读统计（全文/定点/行为层/仅定位/未读）；行为覆盖统计（责任规格合同与场景在案）——三列分别命名，不把 grep 命中生成「已覆盖」、不把表格数字生成「未读 0」。
  - **配置维**：[config-details.json](config-details.json)（33 顶层 PBS 逐文件：机制/schema 覆盖、数据样本已读、只有存在性、实际启用/组合未证分开；abilities.txt 分层在案；ribbons.txt 行为层仅定位——不标数据内容已读全覆盖；备份目录存在性登记；未引用 fancy 文件如实登记）。
  - **UI 维**：[ui-scenario-relations.json](ui-scenario-relations.json)（13 个入口连到可定位场景 ID 或现有入口表：T01–T10 及 T24（暂停项条件）、TC01–TC08、CH01–CH05、DP01–DP05、WP66-A §F、WP66-B §B/§D–F、WP66-C §B–E、WP67-A α–η、WP67-B A–F、WP63 §10、WP68–71 各族、WP72–76 静态场景节——**不只以「静态场景节」或全库行数作证明**）。
  - **Feature 维**：[feature-details.json](../revision-v2/feature-details.json)（v2 沿用——矩阵子范围直接引用并保留其限定；3 个补充范围以 ReviewPending 单列，不并入旧批准）。

## R03（P2）补提取质量与来源分离（已修）

### 控制帮助

- **过渡单位**：`fadetoblack` 的时长按 **1/20 秒单位**解释（`009_Scenes/001_Transitions.rb:18–35`（「duration is in 1/20ths of a second」注释与主入口）＋`001_Transitions.rb:44–95`（`judge_special_transition` 将时长除以 20.0 转为秒）＋`001_Transitions.rb:440–447`（FadeToBlack 的 `update_anim` 按 timer/@duration 衰减））——**8 对应目标 0.4 秒**，不是 8 个渲染帧。修订位置：[specs/ui/wp65-controls-help-appendix.md](../../../specs/ui/wp65-controls-help-appendix.md) §2（末页过渡退出）、§4（当前页 ≥ 最大页号）、CH02——均改为「**目标 0.4 秒——8 个 1/20 秒单位**」；保留实际调度/素材未运行的限制。
- **BACK 实际规则**：`002_EventScene.rb:155–171`（BACK 输入 → 触发 `onBTrigger` 事件）＋`003_Game processing/005_Event_Handlers.rb:4–48`（Event 的回调表 set/+/-/clear/trigger——**空回调表触发即无事发生**）——**标准初始化且本文件未挂接额外回调时，BACK 不产生退出动作**（场景继续）。修订位置：§4（BACK 触发）、§5（退出路径）——均改为上述实际规则，不泛称「按父级默认」。
- **调用点措辞**：§6 调用点改为「脚本内无调用者（全 Scripts 检索无命中）；**实际调用者未定位**（待证——不推成「已经确定来自事件/宿主」）；「脚本内无调用」不等于「不存在」」。
- **源码表达清理**：§3 页面组建（删 `Graphics.freeze`/`addImage(...)`/`addImageForScreen(...)`/`addLabelForScreen(...)`/`set_up_screen(...)` 的具体调用）、§4 当前页 ≥ 最大页号（删 `$game_temp.background_bitmap = ...` 全局赋值、`Graphics.transition(8, "fadetoblack")` 具体调用、`scene.dispose`）、否则分支（删 `@current_screen += 1` 实例页号自增、`set_up_screen(@current_screen)` 具体调用）——全部改为独立的页面/输入/等待/过渡/退出合同；入口名（`onCTrigger`/`onBTrigger`/`onUpdate`/`pictureWait`/`pbEventScreen`/`fadetoblack`）、文件路径/行号保留作审计定位（`009_Scenes/002_EventScene.rb:71–72, 84–86, 166–170`、`009_Scenes/001_Transitions.rb:18–35, 44–95, 440–447`、`003_Game processing/005_Event_Handlers.rb:4–48`）。**重扫结果：0 命中**（含全局赋值、实例变量赋值、带参方法调用、Ruby 条件返回等扩展模式——见 [checks.json](checks.json)，不沿用旧的「零命中」声明，已对当前有效文件重新实测）。

### 弃用告警

- **首行必需/可选统一**：`Deprecation.warn_method` **首行（方法名）必有**；**移除版本与替代建议两个部分分别可选**——正文、表格、向量与不变量已统一（`005_Deprecation.rb:10–19`）。
- **直接调用者与别名构造器分开**：**直接调用者**——方法体**直接发告警并继续检查**（不经别名构造器登记）：`001_FileTests.rb:78–85`（`safeIsDirectory?(f)`/`safeExists?(f)`：先 `Deprecation.warn_method(...)` 再 `FileTest.directory?(f)`/`FileTest.exist?(f)`）；`005_Move.rb:61`、`004_Pokemon_Move.rb:68`、`001_Pokemon.rb:319/325`、`010_DrawText.rb:44/50/56/62/68`、`001_Compiler.rb:517`（各自直接调用 `Deprecation.warn_method(...)`）。**别名构造器（`deprecated_method_alias`）**：**当前核心脚本未找到其登记调用**（全 Scripts 检索无命中——**不推成扩展永不调用**）。修订位置：[specs/kernel/wp07-deprecation-appendix.md](../../../specs/kernel/wp07-deprecation-appendix.md) §5（消费者行）。
- **转发限定**：别名行为与效果改为「按位置参数与关键字参数调用原方法并返回其结果——**仅显式转发位置/关键字参数，未显式转发块回调**；**目标自身失败等边界按原方法合同，不被「透明兼容」抹掉**」；「兼容不阻断调用、不改变返回值（**限实际参数通道与正常返回**）；不产生静默失败」。修订位置：§4（别名行为与效果）、§6（兼容边界）、DP03（向量同步加限定）。

## 已关闭项保持

R04（计数、保护对象、版本时点与多包关系分类）**保持关闭**；WP78 的 11 项关闭与 WP01–WP77、WP68–70 整合、WP77 的既有具名限定批准全部保持，不重开；R01/R02/R03 的已接受修订（训练家卡 §4/TC 向量、Feature 导航、来源集合、Feature/包一一对应、Feature 状态保留）全部保持。

## 总体自检结果

- 训练家卡 §3 残留句已同步（横向对齐＋底边 240，与 §4 一致）。
- 312 行覆盖判断：270 已覆盖＋20 部分覆盖＋3 补提取＋2 行为层＋17 不适用＋0 仅定位＋0 未引用；分层示例与复审点名逐项相符。
- 控制帮助过渡改为目标 0.4 秒（8 个 1/20 秒单位）；BACK 改为实际规则（标准初始化且无额外回调时不产生退出动作）；调用点改为未定位待证；源码表达清理后扩展模式重扫 **0 命中**（重新实测，不沿用旧声明）。
- 弃用告警首行必需/可选统一；直接调用者与别名构造器分开（`deprecated_method_alias` 在当前核心脚本未找到登记调用，如实登记）；转发限定到实际参数通道与正常返回。
- v3 新材料净化扩展模式扫描 **0 命中**；全部本地链接按文件目录复验可解析（见 [checks.json](checks.json)）。
- U01＋G01–G12 保留；③已证事件链＝0、④运行观察＝0；20 项 AX 异常事实保持。
- 状态：**REVISED_PENDING_REVIEW**——3 项均不自行 CLOSED；送 WP79 v3 有界复审。
