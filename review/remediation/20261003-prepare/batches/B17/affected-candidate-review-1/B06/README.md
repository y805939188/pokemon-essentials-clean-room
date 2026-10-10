# B17 affected candidate：B06

结论：**FAIL_SCOPED**。A059 六入口曲目/空值/Intro 接口符合已接受 WP24，但完整差异额外发现设施 caller 的训练家名字被错误删除，阻断本 owner 的 candidate gate。

固定 reviewedSHA：`86bcafffbb2127c66b8636d10943cf702c18a557`；tree：`8626342ceeba125603aca6cac5b86b4e454a8ba0`。正式 FIX_BASE：`f66366b2bbe5c3e1cdd39459f80be672173e7f94`；封套：`d0effbf6e7cddb88482658f8c1b7616a9d5b4091`。

本报告由同一独立受派 reviewer 按 owner 影响范围给出；不代签历史 owner、FULL、actual、C 或 canonical closure。请求 gpt-6.1-sol / ultra / Standard(default) 已由父线程 cloud create 准入，可信有效运行回显缺失，记 **UNVERIFIED**，无新增认证阻塞。

已逐项对照以下真实 caller/data/condition 交界：

- WP67A §3.7 → WP24 §5.4 trainer/wild audio：wildbattle/victory/capture 各独立预置→地图→全局→默认；trainer battle/victory 最后非 nil，包括空串覆盖早先值后回退；FromType保留独立空串与返回形式。普通选择不清预置。
- WP76 real-simulation constructor → WP24 §3.1 trainer name → battle creation：候选 PLAYER1/PLAYER2→PLAYE/PLAYE 改变两个确切 caller 数据身份，固定源380–383明确为原值。影响不因作者建议或反向读表没有列 WP76 而忽略。
- WP24 normal outer cleanup → WP39/WP16：选择入口和收尾分开，所有动态插件调用、真正媒体、伙伴/多目标/捕获失败仍保留其独立门。

静态判读见证（均未执行）：

- 输入：训练家数组前项A后项空、地图M，无预置；直接FromType空独立。核对：普通取M；直接保留非nil空/独立规范化，不误述所有空均等。
- 输入：合法真实设施模拟，两队可构造，无插件，读取进入规则创建战斗前两训练家名字。核对：固定静态调用应PLAYER1和PLAYER2，候选要求PLAYE和PLAYE，失败；不声称运行已观察。
- 输入：类型表首项与等级/成员有效性照C。核对：名字修复不改变类型表首项、等级归一、队伍规则或 AI控制路线。

阻塞及最小返修：将 WP76 §7.2 的 `PLAYE/PLAYE` 恢复为 `PLAYER1/PLAYER2`（B17-AFF-01）。固定源构造范围 380–383 和当前/候选完整文件身份见 [review.json](review.json)。下一精确冻结候选静态复核两个数据身份及其它模拟条件保持。

[review.json](review.json) 给出本 owner 独立分结论、不可变 accepted/control 身份及见证。[共享核验](../B04/shared-verification.json) 只存一次；完整 diff 仅引用封套不可变 commit/path/blob/SHA256，已独立重建比对，不复制旧大型流。

保护检查：demo 175 旧行中174保持、仅GN-M19改；UI 484旧行中480保持、仅K08/K11/K42/L09改。所有旧ID顺序/重复保持、其余旧行及B16新24行逐字节保持；264旧贡献/统计文件保持。两原稿完整after与exact grant匹配，范围许可不是质量证明。40例为未执行静态设计。

U01–U10 / G01–G12 / AX01–AX20、条件树果67、具名未读源范围/样本、插件动态调用、真实地图/Demo、媒体/字体/宿主/配置/容量限制均保留。没有运行 reference、game、Ruby、行为向量或旧作者/reviewer脚本。
