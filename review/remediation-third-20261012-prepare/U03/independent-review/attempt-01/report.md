# GR3-U03 独立候选复审 attempt-01

**结论：3 项 PASS，GR3-M04-001 有限 REQUEST_CHANGES；本批候选整体尚未合格。** 这是对冻结候选的独立静态复审；运行、参考执行、行为案例、真实 Demo、像素／动画宿主观察均为 0，所有设计仍 NOT_EXECUTED。没有正式接受或 CLOSED。

受审作者提交 `5450e35caae225cad69d3f754200b4e7062989e9` / tree `b5e51359cd8e1efabd98a41ac1fdc7d9ca9fdaee`，作者分支 `codex/gr3-u03-author-20261012`。管理输入 `d0371f693f4a0dc713ee5cc6e43a20ff465269a8` / tree `0e217b059c1350b6c4ca93b29ad86fae75b48a54`；H `d5b6af3ebbabc57ed7fbdc2e1fb2c4736dbf9a65` / tree `c8a523150d75c8d1bede346857263ddd00ef0035`；正式 D `86b4d7e1d8645e75af91a215240f8786a5bb4ca8` / tree `42c29efb5422772a1d90f657f25983600f500f28`。

只读参考是 `Maruno17/pokemon-essentials` 的 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。本复审在当前执行器自行从该仓库 fetch 精确提交并 detached checkout 于 `/workspace/pokemon-essentials-reference-fixed`，实际核树及必要源文件字节；没有假设准备任务的目录存在。参考工作树保持干净。根 AGENTS 已读；适用目录无本地 AGENTS/skills 补充。遵守净室规则，仅记行为、数学、前提与证据定位，不复制源代码或设计框架。

复审主角色是本次独立委派的 `/root`，细项由新建 `/root/spinda_review`、`/root/size_review`、`/root/finder_review`、`/root/experience_review`，资格承接由 `/root/qualification_review` 审读，探测依赖还由可见辅助 `/root/finder_review/finder_dependencies` 核查；均只做独立审查，不兼本批作者或唯一整合登记员。作者可见身份为固定提交、分支、`model-request-receipt.json` 的 U03 author only 与 source_thread；其不透明运行任务 ID 不在可见输入中，记 UNVERIFIED，不猜测、不查隐藏接口。复审 `gpt-6.1-sol/ultra/default` 请求接纳有效，执行配置回显 UNVERIFIED；无额度／后台模型审计或隐藏模型 CLI。

## 逐项验收

| ID | 裁决 | 冻结候选位置 | 实质依据 |
| --- | --- | --- | --- |
| GR3-M04-001 | REQUEST_CHANGES | WP21 §3.2-R03，131–159；SP01–SP09，251–265 | 八 nibble、四形状、两倍尺度、两 RGB 偏移／夹限、共享 2×2 左上采样与重叠再调色均吻合；无条件动画逐帧保证超出固定源可证范围，见下述唯一阻塞 |
| GR3-M05-001 | PASS | WP18 §7.4，280–310；WP24 54；SZ01–05／B01–15，250–282 | 原始 IV 低四位、PID 低两 byte、物种高度 0.1m 与两整数阶段可唯一推出 203／209／210mm 及全部 15 段端点；默认 65410…65535 使用 T=65510 的规则保留 |
| GR3-M05-002 | PASS | WP28 §3.3-R01，87–107；IF01–11，224–240 | 名字大小写不敏感子串、当前地图／A 过滤、±7／±5 矩形、Manhattan、枚举平局与方向平局自足；三路计数／音效／等待／消息／效果真和不主动拾取明确 |
| GR3-M06-001 | PASS | WP30 §5.2，136–142，§9 236；WP28 204；EX01–05，242–252 | 钳制后目标比较，三组提示，非零差量先提示后经验写入；同级上升维生素友好、下降无友好，重算／刷新后等级门以及道具前向一致 |

表中位置均相对冻结作者提交下的 `review/remediation-third-20261012-prepare/U03/candidate/deliverables/final-specification-set/`，完整 path/blob/SHA256/bytes 见 [input-snapshot.json](input-snapshot.json)。每项原始完整前提、反例、验收原文与逐条独立结果见 [per-id-verdicts.json](per-id-verdicts.json)。PASS 只覆盖这些字节与明示前提，不能用于后来修订或运行结论。

尺寸独立反例：H=7、零 IV、P=0／2304／2560，s=0／9／10，q=290／299／300，输出 203／209／210mm；s=113 时先 q=401 再得 280mm，合并整数阶段会误得 281mm。每段端点及默认段 65410／65535、内部 65509／65510 均可从候选推导。能力计算的强化 IV、EV、Nature、等级和 PID 高 16 位不是该规则输入。仅定位静态定义不推出动态调用不存在；默认玩家用途、Demo、未来产品范围继续未知。

探测独立对照：玩家 (5,5)，(7,5) 与 (5,7) 都距 2 时取枚举先者；(7,7) 的方向平局取垂直；(12,10) 虽 Manhattan=12 仍在矩形内，(13,5)/(5,11) 被排除。统计在音效／搜索前 +1；无目标是四次 0.5s 文本等待与无响应、脚下四次先等 0.2s 后右转再等 0.3s、邻近先转向后等 0.3s 再两消息；这些是请求合同，未证实际时长。默认 KeyItem 不消费，别名可达和消费按登记内容限定。进入效果前取消不产生该探测效果；进入后的故障可能留下计数，无恢复／回滚签名。方向锁及回调状态改变按明示前提排除或保留未知，不要求真实地图。

经验独立对照：普通非蛋非 Shadow、Medium 曲线 CATERPIE，合法场景、无插件、提示／刷新正常返回。E27→28 先获得1提示（此时仍27），随后写28、维生素友好、重算刷新、L3早退；E28→27 先失去1（仍28），随后写27、重算刷新、L3早退且不改友好；E27→27 提示未变化，直接早退。上下限输入均按钳制目标决定差量。目录的 h80→85 附有软上限／取得地图／球／道具前提。糖果的 qty−1 次友好在设置辅助提示前是原先独立步骤，未改成整条糖果流先提示；战斗零份额静默与原始调试写入路径不扩成此辅助的新签名。

## 唯一必修阻塞 U03-M04-R01

位置：[WP21:101](https://github.com/y805939188/pokemon-essentials-clean-room/blob/5450e35caae225cad69d3f754200b4e7062989e9/review/remediation-third-20261012-prepare/U03/candidate/deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md#L101)、[WP21:157](https://github.com/y805939188/pokemon-essentials-clean-room/blob/5450e35caae225cad69d3f754200b4e7062989e9/review/remediation-third-20261012-prepare/U03/candidate/deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md#L157) 与 [U03-SP07:263](https://github.com/y805939188/pokemon-essentials-clean-room/blob/5450e35caae225cad69d3f754200b4e7062989e9/review/remediation-third-20261012-prepare/U03/candidate/deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md#L263)；`traceability-proposal.json /entries/0/source_evidence/1/note` 的“逐帧”说明有同一限定问题，不另立全局 ID。

前提与最小反例：合法非蛋 SPINDA，指定合法编号／异色，有效正背面资源，尺寸覆盖访问点且无插件；把两帧资源从可枚举分帧 PNG 改为宿主原生两帧 GIF/bitmap，仍满足候选 SP07 当前共同前提。候选却无条件保证两个帧各自处理一次及两个独立颜色终值。

固定源证据：`009_Species_files.rb:92–109` 只能证明资源副本的枚举项被修饰；其直接依赖 `007_Objects and windows/008_AnimatedBitmap.rb:14–18,25` 区分资源消费模式，`105–106` 对可枚举分帧逐一交付，`171–172` 对宿主原生模式仅交付一个 bitmap。`119–123,202–205` 支持各自副本；没有此处逐个切换原生帧的证据。因而不能从源码推出原生每帧独立 get/set 结果；也不能反向声称原生只改第一帧或必然显示失败。该缺口直接由候选新加的帧断言引入，属于 GR3-M04-001 动画边界验收，未扩为资源系统全审。

有限修复验收：

1. WP21 概述及 §3.2-R03 将“每帧各一次／不串色”保证限定到可枚举独立帧的分帧 PNG；其它原生动画只记录一次宿主 bitmap 修饰请求，原生内部帧像素覆盖、显示与时序保留未知。
2. SP07 明示上述分帧 PNG 两帧前提，保留现有数学预期；补一条宿主原生动画反向静态记录，不能签两个原生帧终色。无需创建、修素材或运行宿主。
3. 同步候选源追踪提案的帧说明；更新受影响完整镜像、identities、patch 后交新固定作者 commit/tree 定点复审。编号、形状、颜色、重叠及蛋／朝向／按物种入口合同不得被此限定改坏。

详完整问题对象见 [findings.json](findings.json)。复审者未替作者修候选。

## 完整性、旧控制和承接

八份候选是完整镜像，实际完整 bytes/SHA256/blob 全部等于候选 identities；每一 base 在 H/D 均一致，作者提交内正式文件仍是 D 字节。`candidate.patch` 为 45867 bytes、SHA256 `590cec97110959e74d24ad9f72a2349ce5a5b251149a1e8edb33abaacf1ac1c0`；在仅临时副本执行 `git apply --check --whitespace=error` 及 apply，八结果逐字等于完整候选。实际作者相对管理提交仅有指定 U03 下的 15 个路径变更。作者 45 条新设计与 625 条旧行数字未作为语义通过证据；旧行逐字保留只是保全检查。

必要的 18 个旧控制、39 个局部贡献，其完整 qualified scope、身份 joins、exact 五元组与固定 H 最终 manifest 对齐；完整前提／反例和当前正文保留的有限结果在 snapshot/per-ID 中。A022 明确排除历史“withMoves=false 跳创建形态回调”错句，当前 WP18/CI03 的独立复检门保留；A059 明确排除历史“无记忆 Q 设 timer”错句，当前 WP24/PT58 的取消已有 timer 保留。Nature/IV/HP、TR/学习/PP/取消、经验战斗份额与零值、伙伴持物、煤灰、墙纸等未受本次变更的控制字节保留，不重审全 229/341、不重开旧关闭、不转移历史 PASS 给新字节。

WP28 仍由 U03 唯一候选作者负责。此次一个必修阻塞使候选整体待修；即使所有候选后来 PASS，仍须唯一整合登记员提交实际整合字节，再冻结真实 actual commit/tree/changed-path identities，由另行派发独立角色复审实际字节及公共承接。U03 实际整合独立接受后才以精确新 WP28 commit/blob 顺序交 U04；U05 消费 U03/U04 接受后的冻结结果。U08 未启动，M02-003 未重开。公共 Feature Matrix/source-traceability/approval/junction/status 台账未写。

资源、越界像素、原生动画、实际地图/Demo、消息／输入／音效宿主、异常会话及恢复仍未知；未来 bug 政策、尺寸产品范围、默认艺术／视觉重设计保留用户未来决定，不增列为本次必修阻塞。六个新增报告文件只在派发指定 `U03/independent-review/attempt-01/`，报告精确 commit/tree 由最终外部交付及远端读回提供，避免递归自嵌 SHA。
