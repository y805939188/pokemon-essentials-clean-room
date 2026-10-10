# B17 affected candidate：B12

结论：**NOT_AFFECTED_SUPPORTED**。AI评分/效果/控制评价规则与目录保持；B17 明确正常模拟使用 AI、直接调试菜单另有失败，不改变 AI 的真实评分或随机分布。

固定 reviewedSHA：`86bcafffbb2127c66b8636d10943cf702c18a557`；tree：`8626342ceeba125603aca6cac5b86b4e454a8ba0`。正式 FIX_BASE：`f66366b2bbe5c3e1cdd39459f80be672173e7f94`；封套：`d0effbf6e7cddb88482658f8c1b7616a9d5b4091`。

本报告由同一独立受派 reviewer 按 owner 影响范围给出；不代签历史 owner、FULL、actual、C 或 canonical closure。请求 gpt-6.1-sol / ultra / Standard(default) 已由父线程 cloud create 准入，可信有效运行回显缺失，记 **UNVERIFIED**，无新增认证阻塞。

已逐项对照以下真实 caller/data/condition 交界：

- controlled-player battle main commands → AI evaluation：既有主路仍AI代选；B17辅助菜单Bag/Call条件概率不是AI评价权重或全局随机分布。
- direct debug target/helper → actual action registration：缺访问错误与只筛对方活者的辅助入口不替代AI目标评价和正式执行合法性；不能拿direct失败推主AI不可用。
- WP52A/B/C accepted inputs and pokemon catalog：全部整体保持；生命周期呈现和返回透传未改变评价函数输入、分数或执行条件。

静态判读见证（均未执行）：

- 输入：正常设施controlPlayer=true，前置合法。核对：进入AI代选，旁路辅助菜单；不由此保证完整模拟成功。
- 输入：直接辅助出招标准Battler无插件单数访问。核对：consumer前失败；与WP52评价分数无新对应。
- 输入：既有AI item/calling/target evaluation目录行。核对：原行字节相同，Call7/75只属于debug辅助，不套正式AI。

本 owner 无新增阻塞；有界 PASS 或 NOT_AFFECTED 不构成整个候选通过。B06 的训练家名字回归须返修；WP76 固定算术输入 `R1500` 删除另交作者与 FULL，不能代签其数学门。

[review.json](review.json) 给出本 owner 独立分结论、不可变 accepted/control 身份及见证。[共享核验](../B04/shared-verification.json) 只存一次；完整 diff 仅引用封套不可变 commit/path/blob/SHA256，已独立重建比对，不复制旧大型流。

保护检查：demo 175 旧行中174保持、仅GN-M19改；UI 484旧行中480保持、仅K08/K11/K42/L09改。所有旧ID顺序/重复保持、其余旧行及B16新24行逐字节保持；264旧贡献/统计文件保持。两原稿完整after与exact grant匹配，范围许可不是质量证明。40例为未执行静态设计。

U01–U10 / G01–G12 / AX01–AX20、条件树果67、具名未读源范围/样本、插件动态调用、真实地图/Demo、媒体/字体/宿主/配置/容量限制均保留。没有运行 reference、game、Ruby、行为向量或旧作者/reviewer脚本。
