# WP65 附：控制帮助（Controls help）四页场景合同（WP79-R03 补提取）

2026-10-03；规格提取方。WP79 覆盖审查 v2 发现：`016_UI/001_Non-interactive UI/002_UI_Controls.rb`（83 行）被误列为「不适用（绘制原语）」——实际为**四页可交互控制帮助场景**（确认键推进、页面内容/显示、末页过渡退出），从未提取。本附页作有界补提取。**本场景无菜单注册项**（WP65-D 的 12 项注册中无 Controls 条目；实际调用点为事件侧 `pbEventScreen`，U01 待证）——本附页不冒充 WP65 被审内容。分类：User Interface（主）、Generic Kernel（输入/场景机制接点）、Demo / Developer Experience（作者帮助内容）。

| 项目 | 内容 |
| --- | --- |
| 关联功能 | F16-02（菜单/界面导航子范围——控制帮助场景） |
| 前置依赖 | WP17（输入/消息与窗口语义，已 Reviewed）、WP15（资源匹配，已 Reviewed）、WP08（本地化文本，已 Reviewed）、WP16（图形过渡，已 Reviewed） |
| 输入 | `016_UI/001_Non-interactive UI/002_UI_Controls.rb`（**83 行全文阅读**）；`009_Scenes/002_EventScene.rb`（66–100, 166–170 行——父级输入分发与生命周期定点） |
| 证据等级 | 全部为静态证据：已定位 / 静态确认；**无运行确认**（未运行游戏、UI 或参考表达式；媒体资源存在性未核验） |

## 1. 目的与可见流程

控制帮助是展示键盘控制说明的**四页帮助场景**：玩家打开后逐页查看各键用途，按确认键翻页，末页再按一次即过渡退出。可见流程：打开（冻结图形→背景→首页内容）→ 逐页（确认键 → 下一页内容淡入）→ 末页（确认键 → 快照背景→黑屏过渡→场景释放）→ 回到调用方。

**非目标**：不定义键位绑定的实际宿主映射（`Graphics/UI/Controls help/` 素材与帮助文字描述只是内容展示，**帮助文字的键位描述不能冒充实际宿主绑定验证**）；不定义 EventScene 父类全部机制（仅定点其输入分发与生命周期）；不提取 demo 实际调用点（U01 待证）。

## 2. 领域概念

- **页面（screen）**：逻辑页号 `@current_screen`（初值 1）；每页由**键图**（key image）与**说明标签**（label）组成，未激活页的不透明度为 0（§3）。
- **确认键推进（onCTrigger）**：父级 EventScene 在 USE 输入时触发 `onCTrigger`——本场景挂接为「翻页或退出」（`009_Scenes/002_EventScene.rb:71–72, 84–86, 166–170`：逐帧 `onUpdate` 触发、BACK 触发 `onBTrigger`、USE 触发 `onCTrigger`）。
- **末页过渡退出**：当前页 ≥ 最大页号时，快照当前画面→冻结→`fadetoblack`（8 帧）过渡→释放背景位图与场景（§4）。

## 3. 页面内容（`002_UI_Controls.rb:12–37, 43–53`）

| 页 | 键图（文件名） | 说明标签内容（本地化文本） |
| --- | --- | --- |
| 1 | `help_f1`、`help_f8` | F1：打开键位绑定窗口（可选择各控制使用的键盘键）；F8：截图（存入与存档同一文件夹） |
| 2 | `help_arrows` | 方向键：移动主角；也可用于选择条目与菜单导航 |
| 3 | `help_usekey`、`help_backkey` | 使用键：确认选择、与人和物交互、推进文本（默认 C）；返回键：退出、取消选择、取消模式；移动中按住以不同速度移动（默认 X） |
| 4 | `help_actionkey`、`help_specialkey` | 动作键：打开暂停菜单，另有随上下文变化的功能（默认 Z）；特殊键：打开快捷菜单（Ready Menu），使用已登记物品与可用场地招式（默认 D） |

- **页面组建**：`Graphics.freeze` → `addImage(0, 0, "Graphics/UI/Controls help/bg")` 背景 → 逐页 `addImageForScreen`（键图，不透明度 0）与 `addLabelForScreen`（标签，不透明度 0）→ `set_up_screen(@current_screen)` 把当前页内容淡入 → `Graphics.transition` 过渡显示。
- **换页（`set_up_screen`）**：对全部键图/标签按页号匹配设置目标不透明度（当前页 255、其余 0）并 `pictureWait` 应用变化（55–63 行）。

## 4. 翻页与退出（`pbOnScreenEnd`，65–81 行）

- **最大页号**：取键图与标签页号的最大值（本文件为 4）。
- **当前页 ≥ 最大页号**：`$game_temp.background_bitmap = Graphics.snap_to_bitmap` 快照当前画面 → `Graphics.freeze` → 视口置黑 → `Graphics.transition(8, "fadetoblack")` → 释放背景位图 → `scene.dispose`（退出场景、回到调用方）。
- **否则**：`@current_screen += 1` → 清除旧触发 → `set_up_screen(@current_screen)` 淡入新页 → 重新挂接 `onCTrigger`。
- **BACK 触发**：父级 EventScene 提供 `onBTrigger`（009_Scenes/002_EventScene.rb:71–72, 84–86, 166–170）——本文件未挂接自定义 `onBTrigger` 行为，不推断其退出路径（不补造）。
- **每帧**：父级逐帧触发 `onUpdate`（同行）——场景内容除换页外无动态刷新。

## 5. 输入、退出与边界

- **确认推进**：USE 输入 → 翻页（§4）；无 ACTION 分支、无方向键选择（帮助内容只读）。
- **退出路径**：末页确认 → 快照→黑屏过渡→释放（§4）；**BACK 的退出行为按父级默认**（本文件未挂接，不补造）。
- **素材缺失**：`Graphics/UI/Controls help/` 的 bg、help_f1/f8/arrows/usekey/backkey/actionkey/specialkey——按资源解析与回退规则处理（WP15 引用）；当前快照 Graphics/ 缺失（WP01 §4.2），存在性不验证。
- **帮助文字 ≠ 宿主绑定**：说明标签中的「默认 C/X/Z/D」只是内容文本；实际键位绑定与键位绑定窗口的行为归属输入/选项主规格（WP17/WP65 引用），本附页不据帮助文字断言宿主绑定已验证。
- **不变量**：场景只读（除页号与透明度状态外不写玩家数据）；退出后背景位图与场景释放；页号从 1 起、单调递增到末页。

## 6. 依赖与配置

- 消费 WP17（USE/BACK 输入语义与键位绑定窗口的归属）、WP15（bg 与键图的资源解析）、WP08（说明标签的本地化文本）、WP16（`fadetoblack` 过渡语义）、EventScene 父级（`onUpdate`/`onBTrigger`/`onCTrigger` 输入分发与场景生命周期——`009_Scenes/002_EventScene.rb:66–100, 166–170`）。
- 调用点：`pbEventScreen(ButtonEventScene)`——**脚本内无调用者**（全 Scripts 检索无命中），实际调用为事件/宿主侧（U01 待证）；「脚本内无调用」不等于「不存在」。

## 7. 静态场景（输入 → 推导预期；均未运行）

| 编号 | 场景（前提） | 预期（静态推导） |
| --- | --- | --- |
| CH01 默认翻页链 | 打开 → 连续按确认键 | 页 1（F1/F8）→ 页 2（方向键）→ 页 3（使用/返回）→ 页 4（动作/特殊）依次淡入；每页其余内容不透明度为 0 |
| CH02 末页退出 | 当前页 4 时再按确认键 | 快照当前画面 → 冻结 → 视口置黑 → `fadetoblack`（8 帧）→ 释放背景位图与场景 |
| CH03 帮助文字边界 | 说明标签含「默认 C/X/Z/D」 | 仅作内容展示登记；不据其断言实际键位绑定已验证（绑定与键位绑定窗口归 WP17/WP65） |
| CH04 素材缺失 | `help_f8` 文件不存在 | 按资源解析与回退规则处理（WP15）；不推断缺失素材的运行表现 |
| CH05 无 ACTION 分支 | 循环中按 ACTION 或方向键 | 无翻页/无响应（无分支）；仅确认键推进与末页退出 |

## 8. 未决问题

1. 实际调用点（`pbEventScreen` 的事件/宿主侧调用者）待证（U01）；demo 中是否可达未知。
2. 素材内容与存在性未验证（Graphics/ 缺失）。
3. 帮助场景的宿主表现（淡入、过渡、音效）未运行验证。
4. 帮助文字与键位绑定窗口的关系：绑定窗口的行为归属 WP17/WP65 引用，本附页不展开。

## 9. 证据与来源（traceability）

- **全文阅读**：`016_UI/001_Non-interactive UI/002_UI_Controls.rb`（83 行——本附页全部条款的直接来源）。
- **定点阅读**：`009_Scenes/002_EventScene.rb`（66–100 行——EventScene 类与触发事件定义；166–170 行——逐帧 update/BACK/USE 触发分发）。
- **引用（既有批准文本）**：WP15（资源解析与回退）、WP08（本地化文本）、WP16（图形过渡）、WP17（输入语义）、WP65（键位绑定窗口与选项归属）。
- 未运行游戏、UI、编译器、生成器、反序列化或参考行为模拟器；reference 固定 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 只读。

## 10. 状态与后续

- 状态：**ReviewPending（WP79-R03 补提取，待独立复审）**；WP65 已批准范围不变；本附页为 WP79 覆盖审查 v2 中「不适用误列」的有界补提取，复审通过后随 WP79 登记并入 UI 场景覆盖关系。
