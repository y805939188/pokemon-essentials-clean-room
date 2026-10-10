# B17 affected candidate：B04

结论：**PASS_SCOPED**。音频逻辑请求、Intro 记忆交付与正常收尾，以及绘制/输入取消次序的 B04 接口符合当前限定；媒体和宿主结果仍未证。

固定 reviewedSHA：`86bcafffbb2127c66b8636d10943cf702c18a557`；tree：`8626342ceeba125603aca6cac5b86b4e454a8ba0`。正式 FIX_BASE：`f66366b2bbe5c3e1cdd39459f80be672173e7f94`；封套：`d0effbf6e7cddb88482658f8c1b7616a9d5b4091`。

本报告由同一独立受派 reviewer 按 owner 影响范围给出；不代签历史 owner、FULL、actual、C 或 canonical closure。请求 gpt-6.1-sol / ultra / Standard(default) 已由父线程 cloud create 准入，可信有效运行回显缺失，记 **UNVERIFIED**，无新增认证阻塞。

已逐项对照以下真实 caller/data/condition 交界：

- WP24 audio selection → WP15 request/playback → WP16 prebattle wrapper：六入口选择与实际播放分开；FromType 的非 nil 空串/规格化差异保留；选择不清下一战预置，正常外层收尾才清，异常无全局回滚。
- Intro → remembered BGM/timer → battle request：已有记忆时位置/队列不重写；无记忆且 Q 队列时记 Q/0、取消队列后请求 I；否则当前曲目/位置失败取 0。
- evolution update → input → cancel → completion：输入前先完成本轮动画更新，允许 BACK 在最后更新轮自然结束检查前取消；白闪阶段不再消费该取消。首更新白覆盖下双全白 scale0 → 约2s长大 → 约2.6s先白剪影，非“首帧已彩色”或全段白色。
- GIR-FD82-003 local scene neutralization：对象组织/基类/执行器证明改为可见行为；保留九布局、返回未知、暂停与并行更新、Safari/Palace/Arena 独立门。

静态判读见证（均未执行）：

- 输入：训练家数组保存曲目依次 A、空串；地图 M；无预置。核对：最后非 nil 是空串，普通训练家入口回退 M，不能保留 A；FromType 独立非 nil 空串不套普通规格化。
- 输入：Intro I 非空，无记忆且排队 Q；另已有记忆 A/位置 p。核对：前者记 Q/0并取消队列再请求 I；后者保持 A/p 和既有队列，只请求 I。
- 输入：正常战斗返回；对照执行抛错。核对：前者 WP16 清记忆/四类预置并恢复请求；后者不保证收尾到达，不造事务回滚。
- 输入：有效非透明 CATERPIE→METAPOD演出，最后动画更新同轮BACK，可取消与禁止取消分别。核对：可取消先走取消，禁止取消继续成功；后段白闪BACK不取消。未运行像素或帧输入。
- 输入：B16 SE100、记 BGS80→改SE50→恢复248。核对：当前/记忆登记50、播放请求25仍由 BGS/SE独立合同确定，不能套 BGM暂停位置规则。

本 owner 无新增阻塞；有界 PASS 或 NOT_AFFECTED 不构成整个候选通过。B06 的训练家名字回归须返修；WP76 固定算术输入 `R1500` 删除另交作者与 FULL，不能代签其数学门。

[review.json](review.json) 给出本 owner 独立分结论、不可变 accepted/control 身份及见证。[共享核验](../B04/shared-verification.json) 只存一次；完整 diff 仅引用封套不可变 commit/path/blob/SHA256，已独立重建比对，不复制旧大型流。

保护检查：demo 175 旧行中174保持、仅GN-M19改；UI 484旧行中480保持、仅K08/K11/K42/L09改。所有旧ID顺序/重复保持、其余旧行及B16新24行逐字节保持；264旧贡献/统计文件保持。两原稿完整after与exact grant匹配，范围许可不是质量证明。40例为未执行静态设计。

U01–U10 / G01–G12 / AX01–AX20、条件树果67、具名未读源范围/样本、插件动态调用、真实地图/Demo、媒体/字体/宿主/配置/容量限制均保留。没有运行 reference、game、Ruby、行为向量或旧作者/reviewer脚本。
