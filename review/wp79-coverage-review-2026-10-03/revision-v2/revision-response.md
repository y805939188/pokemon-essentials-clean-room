# WP79 v2 逐项修订回应（R01–R04）

2026-10-03；规格提取方。依据 [report.md](../../wp79-stage-review-2026-10-03/report.md)（首版 **REQUIRES_REVISION：原 WP79-R01 保持 OPEN，新增 R02/R03/R04——共 4 项（P2×3、P3×1）**）与 [revision-prompt.md](../../wp79-stage-review-2026-10-03/revision-prompt.md)：4 项按原编号原位修订；WP78 的 11 项关闭与既有具名限定批准保持，不重开；首版材料、独立审查与冻结快照全部留史未改写。作者状态：**REVISED_PENDING_REVIEW**——不自行 CLOSED、不自行 Reviewed。

## R01（P2）训练家卡附表画像对齐、装扮资源输入与徽章向量（已修）

- **残留 1（对齐）**：v1 把画像写成「垂直居中」。实际放置规则（`012_UI_TrainerCard.rb:28–31`）：**横向对齐到 128 宽区域**（x＝336 −（图宽 − 128）/2）＋**底边保持 240**（y＝112 −（图高 − 128），底边＝y＋图高＝240）。固定算术对照：宽 128 高 256 位图 → 左上角 **(336, −16)**（底边 240）；128×128 位图 → 左上角 (336, 112)（底边同为 240）——底边不随图高变化。
- **残留 2（装扮资源输入）**：v1 写「不读取性别差分之外的其它玩家字段」。实际正面画像资源还读取**玩家装扮编号**（`$player.outfit`，缺省 0）：**优先尝试 `_N` 装扮变体**（`Graphics/Trainers/<类型ID>_N`，N＝当前装扮编号），资源解析失败（不存在）则**回退基础图**（`Graphics/Trainers/<类型ID>`）——`010_Data/002_PBS data/014_TrainerType.rb:52–61, 78–81` 定点（WP24 资源主规则引用）。错误排除已删除。
- **残留 3（徽章向量）**：v1 TC01 把「3 枚徽章」误推成固定前三槽。已改为**按真值位**：下标 0/3/7 为真（共 3 枚）→ 图标落在槽位 0（x＝72）、槽位 3（x＝216）、槽位 7（x＝408）三处，**不紧排前三槽**（槽位 1/2/4/5/6 不绘）。TC06 补「下标 11–15 为假」前提（仅期望地区内 0–2 显示时）。新增 **TC07**（不同图高：底边不随图高变化，横向对齐到 128 宽区域）与 **TC08**（装扮编号 2 且变体存在 → 用 `_2`；装扮编号 2 且变体不存在 → 回退基础图；装扮编号 0 → 先试 `_0` 再回退——变体优先规则与编号无关）。
- **修订位置**：[specs/ui/wp65-trainer-card-appendix.md](../../../specs/ui/wp65-trainer-card-appendix.md) §4（放置规则＋装扮消费）、§8（TC01/TC06 更正＋TC07/TC08 新增）、§11（v2 更正记录）。**保持 ReviewPending**；旧 WP65/WP24/WP15 不为迎合新摘要而改写；v1 附表与首版材料留史。

## R02（P2）交付可枚举的五维覆盖明细（已修）

- **残留**：v1 的两个小 JSON 主要是汇总，不足以支持五维闭合；「文件被引用」被直接当作已覆盖。
- **修订**：建立四份可枚举明细（本目录）——
  - **[feature-details.json](feature-details.json)**（113 行＋3 个补充范围）：逐 Feature 列实际承接包、规格文件、状态分类、未验证子范围；补充范围（训练家卡/控制帮助/弃用告警）以 ReviewPending 单列，旧批准范围保持。
  - **[source-details.json](source-details.json)**（312 行）：逐 .rb 路径列处置（已覆盖（规格引用）／已补提取／行为层已覆盖／不适用／未引用待核）、证据与阅读层级。分类法：字符串匹配统计（grep 命中，仅证明被提及）／阅读统计（全文/定点/行为层/仅定位/未读）／行为覆盖统计（责任规格合同与场景在案）——三列分别命名不互相替代。**未引用待核 0 行**（grep 逐路径复核；数字前缀误配 5 行已按短名复核修正）。
  - **[config-details.json](config-details.json)**（36 行）：33 顶层 PBS 逐文件处置＋备份目录（存在性登记，未读/未启用，U03/U06）＋未引用 fancy 文件（如实登记，非遗漏）；机制/schema 覆盖、数据样本已读、只有存在性、实际启用/组合未证分开；`ribbons.txt` 标行为层覆盖（不据此标数据内容已读全覆盖）。
  - **[ui-scenario-relations.json](ui-scenario-relations.json)**（13 行）：入口和关键正常/失败/取消/部分提交/恢复边界连到既有场景 ID 与责任规格；1,731 行只作统计量（非完整性证明）；含 specs 目录与 review 目录附表（WP77 证据表/WP78 已核交界）的关系。
- **边界补记**：根目录两个 Ruby 工具（`scripts_extract.rb`、`scripts_combine.rb`）登记为作者工具（WP01 快照，非游戏行为）——**不把 312 说成全 reference 源码总数**（非 Git 目录全 reference 共 314 个 Ruby 文件）。已读样本、完整目录和未验证组合分开；demo 与配置用同样的明确关系；缺地图/素材/运行时继续保留具名缺证（U01/U03/U05/U06/P05）。
- **未预设「仅一项遗漏」**：逐项核对后实际遗漏为 3 项（R01/R03-1/R03-2），均已补提取（待复审），无新增无归属缺口。

## R03（P2）不适用误列纠正与补提取（已修）

- **反例 1（控制帮助）**：`016_UI/001_Non-interactive UI/002_UI_Controls.rb`（83 行）为**四页可交互控制帮助场景**——页面内容（F1 键位绑定窗口/F8 截图/方向键/使用键 C/返回键 X/动作键 Z/特殊键 D）、确认键推进（`onCTrigger` 挂接翻页）、末页过渡退出（快照→冻结→`fadetoblack`(8)→释放）。父级 EventScene 的输入分发与生命周期已定点核对（`009_Scenes/002_EventScene.rb:66–100, 166–170`：逐帧 `onUpdate`、BACK 触发 `onBTrigger`、USE 触发 `onCTrigger`）。**本场景无菜单注册项**（WP65-D 的 12 项注册中无 Controls 条目；实际调用点为事件侧 `pbEventScreen`，脚本内无调用者——U01 待证）；帮助文字的键位描述不冒充实际宿主绑定验证。已补提取 [specs/ui/wp65-controls-help-appendix.md](../../../specs/ui/wp65-controls-help-appendix.md)（CH01–CH05 场景）。
- **反例 2（弃用告警）**：`001_Technical/001_Debugging/005_Deprecation.rb`（52 行）为**开发者体验合同**——`Deprecation.warn_method`（方法名＋可选移除版本＋可选替代方法→控制台告警，三部分独立可选）与 `deprecated_method_alias`（参数类型校验（WP03 引用）、目标方法缺失抛 `ArgumentError`、别名先告警后按原方法执行并透传返回值——兼容不阻断）。WP07 §3 已述「弃用警告机制归调试面」（控制台输出去向已覆盖），本附页补机制本体：[specs/kernel/wp07-deprecation-appendix.md](../../../specs/kernel/wp07-deprecation-appendix.md)（DP01–DP05 场景）。
- **其余项逐路径核对**：精灵/渲染原语 14 个（可观察行为已由 WP15/WP16 覆盖——给确切归属：WP15 §A–D 资源匹配/缓存/音频、WP16 §3/§4.2/§6 地图绘制/精灵/天气/转场）、Game_Picture（WP13 命令矩阵 231–235 覆盖图片命令）、Utilities_BattleAudio（WP15 §D 音频行为覆盖）、FileMixins（WP07 §A 文件访问层覆盖）——仅内部实现细节，给确切章节后保留不适用；`009_Scenes/001_Transitions.rb` 由不适用改判**行为层已覆盖**（WP16 §4.2 淡入守卫与时序/§6 命令与转场资源）；`009_Scenes/002_EventScene.rb` 已由父级定点引用（WP13/本附页）；AI 效果实现 9＋7 个（WP51/WP52 身份与评估合同层覆盖，WP52-A 覆盖表逐项映射）；数据类文件（WP03/WP18/WP19/WP24 字段责任目录覆盖）。**新确证遗漏 0 项**（除 R01/R03-1/R03-2 外）。

## R04（P3）统计同步（已修）

- **保护对象时点**：相对 WP78 recheck-v6 的 31,693 个——当前为 **31,690 个不变＋manifest/TSV/coverage 三项授权变化**（v1 误把 coverage.md 计入「字节不变」；coverage.md 为 WP79 任务指定填写对象，不计入）。
- **文件/包口径**：规格文件基线 109 → 当前 **112**（新增 3 个补提取附表：wp65-trainer-card-appendix、wp65-controls-help-appendix、wp07-deprecation-appendix）；内容包 ID 仍 **84**（附表归入既有 WP65/WP07 包 ID，不新增包 ID）；后续新增附表按真实文件集合更新。
- **多包关系分类**：10 个多包承接按实际分工分类（配置/管线、并列机制族、同域两册、计算/时序、AI 评估三包系列、会话/变体、储存两域、编辑器两域、基线/证据），不统称 A/B/C 拆分。
- **计数命名**：字符串匹配统计（grep 命中）、阅读统计（全文/定点/行为层/仅定位/未读）、行为覆盖统计（合同与场景在案）——三列分别命名并同步 report、coverage、JSON、自检与末检；**不增加没有验收用途的装饰性总数**。
- **同步范围**：[planning/coverage.md](../../../planning/coverage.md)（v2 主覆盖表）、[feature-details.json](feature-details.json)、[source-details.json](source-details.json)、[config-details.json](config-details.json)、[ui-scenario-relations.json](ui-scenario-relations.json)、本文件、[checks.json](checks.json)、[report.md](report.md)、[delivery-summary.md](delivery-summary.md)。

## 已关闭项保持

WP78 的 11 项（R01–R11）与 WP01–WP77、WP68–70 整合、WP77 的既有具名限定批准**全部保持**，不重开；本阶段仅 WP79 交付层的 4 项修订与 3 份补提取附表。

## 总体自检结果

- R01 附表三处错误已原位更正（对齐/装扮/徽章），新增 TC07/TC08 向量；固定算术对照（128×256 → (336,−16)、128×128 → (336,112)，底边同为 240）与 reference 行（28–31、52–61、78–81）一致。
- 312 行来源明细：未引用待核 **0**（grep 逐路径复核；5 个数字前缀误配已按短名复核修正）；不适用 17 个均给确切章节或理由；行为层 2 个。
- 控制帮助与弃用告警两份补提取均全文阅读（83/52 行）并给场景与未决边界；WP65/WP07 已批准范围不动。
- v2 新材料净化扩展模式扫描 **0 命中**（含 return-false-if 等）；全部本地链接按文件目录复验可解析（见 [checks.json](checks.json)）。
- U01＋G01–G12 保留；③已证事件链＝0、④运行观察＝0；20 项 AX 异常事实保持。
- 状态：**REVISED_PENDING_REVIEW**——4 项均不自行 CLOSED；送 WP79 v2 独立复审。
