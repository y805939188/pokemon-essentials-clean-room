# B17 affected candidate：B09

结论：**PASS_SCOPED**。普通/Encore/物品分层取消、NearAlly初选缺陷与执行期拒绝、Mega首门和回末预收集调位均符合当前最终限定；B06名字回归另列阻塞，不代签整个候选。

固定 reviewedSHA：`86bcafffbb2127c66b8636d10943cf702c18a557`；tree：`8626342ceeba125603aca6cac5b86b4e454a8ba0`。正式 FIX_BASE：`f66366b2bbe5c3e1cdd39459f80be672173e7f94`；封套：`d0effbf6e7cddb88482658f8c1b7616a9d5b4091`。

本报告由同一独立受派 reviewer 按 owner 影响范围给出；不代签历史 owner、FULL、actual、C 或 canonical closure。请求 gpt-6.1-sol / ultra / Standard(default) 已由父线程 cloud create 准入，可信有效运行回显缺失，记 **UNVERIFIED**，无新增认证阻塞。

已逐项对照以下真实 caller/data/condition 交界：

- WP39 living iterators/seat relation → WP67A target UI → move execution：NearAlly按席顺第一个存活非自身同侧，初选错误忽略邻近；3v3 0/死2/活4选4，文本nil仍立绘/框4高亮、无按钮选中，USE登记4退出，执行正常门拒远4不代选。无人活非自身才回自身0，不能用“没有活近邻”提前回退。
- WP40 Encore auto registration vs manual Fight → cancellation：普通手动目标BACK回Fight；生效Encore自动目标BACK回main，候选选择撤销及Mega撤销，PP/Encore不因此变化；物品目标BACK回bag。回放K56循环不继承普通清理。
- reachable Mega variant → ordinary gates → Ctrl：道具或已知MegaMove可达；Rayquaza已知DragonAscent无需持Mega石，但普通ring/quota等门仍有。Ctrl先经过开关/可达/非Transform/非wild门，再可绕SkyDrop/ring/quota；按钮开关不等同攻击期变形。
- WP42 stage23 → collect plans side0 then1 → execute：先收所有计划，遇已有近邻对停止后续收集并保留先前计划；多于一计划抑制2席候选不抑制3席；执行不因第一项后新近邻而取消第二项。端点建立/同属主门保留，不擅加额外存活端点门。手动WP41Shift耗行动与回末移动分开。
- debug helper direct call vs controlled-player AI main path：直接出招辅助缺单数访问在首采样/consumer前失败；正常设施AI路线旁路。目标只对方活者不验招合法，无目标-1；换人consumer验证/空最多50次无返回；Call整体7/75，不当AI权重。

静态判读见证（均未执行）：

- 输入：正常合法3v3，0使用NearAlly，2倒下4活，对方全活。核对：初4/niltext/高亮4/USE登记4，执行拒远；对照双打2倒下无非自身活者，回0后执行拒自身。
- 输入：Encore生效自动招需选目标→BACK，独立手动Fight/物品目标。核对：分别main/Fight/bag；普通撤候选及Mega，PP和Encore不变；不推回放同样退出。
- 输入：Rayquaza知DragonAscent无持石，ring/quota有效；Ctrl但reachable假或Transform/wild。核对：正常允许按钮；首门不通过时Ctrl仍不通过，Ctrl不能造可达Mega。
- 输入：合法3v3六席建立、仅0/1活，中心2/3死无后备，到阶段23、每侧单属主。核对：预收0↔2、1↔3均执行，最终2/3，不按第一项后近邻停第二项。
- 输入：合法3v2同活0/1，到stage23；另合法3v3玩家三属主/对手单属主。核对：3v2多计划抑2席1↔3，最终2/1；属主例只对手1↔3，最终0/3。
- 输入：替补后终局早退未到stage23；直接辅助出招与主AI路独立。核对：不承诺移动反馈；direct先失败而主路旁路，不宣称整个模拟失败/成功。

本 owner 无新增阻塞；有界 PASS 或 NOT_AFFECTED 不构成整个候选通过。B06 的训练家名字回归须返修；WP76 固定算术输入 `R1500` 删除另交作者与 FULL，不能代签其数学门。

[review.json](review.json) 给出本 owner 独立分结论、不可变 accepted/control 身份及见证。[共享核验](../B04/shared-verification.json) 只存一次；完整 diff 仅引用封套不可变 commit/path/blob/SHA256，已独立重建比对，不复制旧大型流。

保护检查：demo 175 旧行中174保持、仅GN-M19改；UI 484旧行中480保持、仅K08/K11/K42/L09改。所有旧ID顺序/重复保持、其余旧行及B16新24行逐字节保持；264旧贡献/统计文件保持。两原稿完整after与exact grant匹配，范围许可不是质量证明。40例为未执行静态设计。

U01–U10 / G01–G12 / AX01–AX20、条件树果67、具名未读源范围/样本、插件动态调用、真实地图/Demo、媒体/字体/宿主/配置/容量限制均保留。没有运行 reference、game、Ruby、行为向量或旧作者/reviewer脚本。
