# B17 affected candidate：B15

结论：**NOT_AFFECTED_SUPPORTED**。Pokégear/点唱机、飞行/图鉴共享目录接受贡献保持；B17 新音轨入口引用既有优先链，不改全局覆盖的写入和跨图寿命。

固定 reviewedSHA：`86bcafffbb2127c66b8636d10943cf702c18a557`；tree：`8626342ceeba125603aca6cac5b86b4e454a8ba0`。正式 FIX_BASE：`f66366b2bbe5c3e1cdd39459f80be672173e7f94`；封套：`d0effbf6e7cddb88482658f8c1b7616a9d5b4091`。

本报告由同一独立受派 reviewer 按 owner 影响范围给出；不代签历史 owner、FULL、actual、C 或 canonical closure。请求 gpt-6.1-sol / ultra / Standard(default) 已由父线程 cloud create 准入，可信有效运行回显缺失，记 **UNVERIFIED**，无新增认证阻塞。

已逐项对照以下真实 caller/data/condition 交界：

- WP63 jukebox writes global default BGM → WP24 battle selector：默认BGM覆盖与地图遭遇lower/higher旗标分开，换图只清旗标；新WP67A表只引用该既有全局来源，不清覆盖或宣称确定地图曲目/实际听感。
- WP63 fly/map/phone → UI/catalog shared whole writer：所有B15旧贡献行及B16有关图鉴行保持，L09只孵化标号；没有飞行目标/图鉴持久状态新写入。
- directory failure vs empty jukebox list：Custom目录缺失早于清覆盖、空列表USE和BACK分支仍原合同；不能从音乐回退文本推出统一安全空态。

静态判读见证（均未执行）：

- 输入：March写higher及全局覆盖A后换图，无其它写入。核对：两遭遇旗标false，覆盖A仍在；战斗选择按既有优先链，不扩成资源/播放保证。
- 输入：Custom目录不可进入，已有覆盖A；另合法空列表BACK。核对：前者在清覆盖前失败，后者保留覆盖；没有被B17空音轨回退门改写。

本 owner 无新增阻塞；有界 PASS 或 NOT_AFFECTED 不构成整个候选通过。B06 的训练家名字回归须返修；WP76 固定算术输入 `R1500` 删除另交作者与 FULL，不能代签其数学门。

[review.json](review.json) 给出本 owner 独立分结论、不可变 accepted/control 身份及见证。[共享核验](../B04/shared-verification.json) 只存一次；完整 diff 仅引用封套不可变 commit/path/blob/SHA256，已独立重建比对，不复制旧大型流。

保护检查：demo 175 旧行中174保持、仅GN-M19改；UI 484旧行中480保持、仅K08/K11/K42/L09改。所有旧ID顺序/重复保持、其余旧行及B16新24行逐字节保持；264旧贡献/统计文件保持。两原稿完整after与exact grant匹配，范围许可不是质量证明。40例为未执行静态设计。

U01–U10 / G01–G12 / AX01–AX20、条件树果67、具名未读源范围/样本、插件动态调用、真实地图/Demo、媒体/字体/宿主/配置/容量限制均保留。没有运行 reference、game、Ruby、行为向量或旧作者/reviewer脚本。
