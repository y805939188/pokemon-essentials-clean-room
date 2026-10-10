# B17 affected candidate：B16

结论：**PASS_SCOPED**。最新 B16-C 的三种队伍模式、空详情/重学首绘失败与 BGS记忆音量合同被正确承接；新24行及全部旧贡献字节保持。

固定 reviewedSHA：`86bcafffbb2127c66b8636d10943cf702c18a557`；tree：`8626342ceeba125603aca6cac5b86b4e454a8ba0`。正式 FIX_BASE：`f66366b2bbe5c3e1cdd39459f80be672173e7f94`；封套：`d0effbf6e7cddb88482658f8c1b7616a9d5b4091`。

本报告由同一独立受派 reviewer 按 owner 影响范围给出；不代签历史 owner、FULL、actual、C 或 canonical closure。请求 gpt-6.1-sol / ultra / Standard(default) 已由父线程 cloud create 准入，可信有效运行回显缺失，记 **UNVERIFIED**，无新增认证阻塞。

已逐项对照以下真实 caller/data/condition 交界：

- WP66A normal MOVES → detail/forget/event/relearn → WP67A battle learning：零招普通MOVES可四空位；详情/直接遗忘/事件选招在BACK前缺首招字段失败，空重学首绘严格ID ArgumentError；不足4战斗学招直接加，满槽遗忘已有旧招前提。不能把所有空列表写成可取消。
- WP66A main/menuSwitch/shortcut → party/Box Link：三个会话的ACTION/SPECIAL权限与旧source index保留；BoxLink缩队[A,B]→[A]后旧1换位可[nil,A]并失败，BACK保留盒修改，B17未添加同步或回滚。
- WP65 SE edit/BGS alias → WP15 memory247/restore248：A059谈BGM曲目选择，不覆盖BGS/SE共享对象后置音量重播合同；C058连续链24行保护。
- C003 B16 accepted PT-A23/A31/A33 vs B17 L09：hp50/120→30/120实际24、上限50反例20；重学初始项合并去重与健康蛋无合格选择仍开UI等限定保持；不代重签B16接受。

静态判读见证（均未执行）：

- 输入：零已知招式普通MOVES，另直接详情/遗忘/事件选招；空重学独立。核对：普通四空位；缺首招读在BACK前失败，无事件结果写入；重学ArgumentError亦早于选择循环；非空取消照旧。
- 输入：主选择/菜单Switch目标/快捷目标三独立模式，BoxLink三门成立。核对：ACTION分别[1,index]/无效果/取消，SPECIAL允许/允许/禁；旧盒修改取消不回滚。
- 输入：BGS80、SE100先247记忆再SE50再248；独立查询副本。核对：当前及记忆50、请求25；副本改动不影响记录，无BGS或同音量不套重播。
- 输入：24个B16新增目录行和264旧贡献记录。核对：整行顺序/字节及统计文件整体保持；只有B17的K08/K11/K42/L09四旧行改，绝不以“scope许可”代质量。

本 owner 无新增阻塞；有界 PASS 或 NOT_AFFECTED 不构成整个候选通过。B06 的训练家名字回归须返修；WP76 固定算术输入 `R1500` 删除另交作者与 FULL，不能代签其数学门。

[review.json](review.json) 给出本 owner 独立分结论、不可变 accepted/control 身份及见证。[共享核验](../B04/shared-verification.json) 只存一次；完整 diff 仅引用封套不可变 commit/path/blob/SHA256，已独立重建比对，不复制旧大型流。

保护检查：demo 175 旧行中174保持、仅GN-M19改；UI 484旧行中480保持、仅K08/K11/K42/L09改。所有旧ID顺序/重复保持、其余旧行及B16新24行逐字节保持；264旧贡献/统计文件保持。两原稿完整after与exact grant匹配，范围许可不是质量证明。40例为未执行静态设计。

U01–U10 / G01–G12 / AX01–AX20、条件树果67、具名未读源范围/样本、插件动态调用、真实地图/Demo、媒体/字体/宿主/配置/容量限制均保留。没有运行 reference、game、Ruby、行为向量或旧作者/reviewer脚本。
