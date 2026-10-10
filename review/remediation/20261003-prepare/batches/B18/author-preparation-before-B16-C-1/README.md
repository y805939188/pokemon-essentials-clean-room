# B18 有限私有准备（B16-C 前）

状态：**有限静态准备已打包；正式作者仍等待 B16-C**。本包不是正式 release、candidate、独立 review、PASS、贡献接受或 canonical 关闭。

固定准备输入为 B13-C `27185563f307e16d2612fa86e83b2c9bd772c79e`，tree `e44ed01586846bb42b03105dcc575d463df4ef49`。从该 C 创建独立分支 `codex/cloud-dot-B18-preparation-1-20261010`。管理派发包 `6d67715253c6789861a2785f1f6c8438bd60caaf` 只提供准备权限与完整控制，未被当成正式输入。

唯一项目写范围为本目录。formal/specs/candidate/public/其他 owner、AGENTS、旧 review 和 reference 均未写；两份原稿提案只保存完整合并 patch 和 proposed-after，未应用。未自开子任务，未代替独立 reviewer。

完整范围仍为 WP68–WP71、8 贡献／5 主责、54 计划读（52 当前 C＋2 immutable original review），原拟正式写 13 路径现写 0。54 项均核身份，语义消费按必要本 WP 条款和准确复用材料记录于 `input-consumption.json`；身份核验不等于全文语义阅读。没有递归全历史审计，也没有为了证明旧作者已读而运行程序。

读取 AGENTS.md 后执行本任务；固定 C 与派发树均没有可用 `.agents/skills` SKILL.md。请求配置 gpt-6.1-sol／xhigh／default Standard，admission 按已派发 Plan A；有效 backend **UNVERIFIED**，未探测配置／额度，未做 CLI/native 降级。

## 文件索引

- `inherited-controls.json`：派发包完整原 findings／approved acceptance／current qualified controls 原字节副本；八项原对象及八项批准对象已与精确原 commit/pointer 核对。它们是继承控制，不是本作者的新结论。
- `frozen-inputs.json`：54 计划读、13 future formal 及10 原稿导航完整固定身份；不增加正式写权限。
- `per-ID-preparation.md`、`per-ID-index.json`：八项当前静态修订需求、完整限定验收绑定、源/caller、已有与缺少证据、案例与一致计划。
- `source-evidence.json`：三个必要固定参考文本文件的实际静态范围、精确 B07 复用范围及已裁决数学证明；不含复制的参考代码。
- `approval-chain-reuse.json`、`historical-corrections.md`：九份 B-v1 原输入的旧限定批准与当前身份对应，以及错误载体的后继勘误建议。
- `original-proposals/manifest.json`：Triple Triad（C127/C128）和 Tile Puzzles（C129/C130/C131）每文件一份完整合并补丁、精确 before/after 身份和完整 proposed-after；T01 原稿、T18 原四列表及已有正确不变量保持。
- `pending-B16.json`：共享 UI catalog、条件性 WP66-A 原稿、真实接受接口及 B17/B18 后续目录锁/reader 门。
- `source-limits.json`、`inherited-source-limits.json`：完整继承限制和本轮精确未读/执行口径。
- `public-registration-proposals.json`：八项公共登记建议，均仅为准备，不接受、不关闭。
- `validation-results.json`、`output-manifest.json`：新的 Git/JSON/hash/text 文件范围与内容验证；不作为独立语义 review。

## 完成与后续

本轮有限准备可带真实 pending 结束。缺少的正式门是 B16 已接受且普通发布读回的真实 C/实际回执，以及父/sole registrar 的最新 C 完整重冻结/派工。UI catalog before blob 为 `9d8aa85ff8e56365b3eba695248cd1b40289e28b`；WP66-A before blob 为 `e2818baa4e33c0547fe3b06efb807f2da0f7332c`。B16-C 后只刷新真实变化的字节、本 WP 行号/案例、接受接口与实际新增条件；未变材料精确复用，不重做全部准备。

未来正式 B17/B18 共享 UI catalog；B18 写而 B17 读的三个 catalog 与 B17 写而 B18 读的 demo/UI catalog 均保留 reader 影响。整文件锁、B16-C 原依赖、sole 串行 G/C、独立 candidate/actual FULL 与真实 affected 门不因本包解除。

所有案例都是**未执行静态设计**。参考/game/Ruby、编译/转换/生成/反序列化、旧 author/reviewer/preparation 程序、行为向量执行均 0；运行观察 0、已证真实 Demo 链 0。U01–U10/G01–G12/AX01–AX20、条件性完整67树果、插件/宿主/媒体/样本非局部限制全部保留。准备打包后仅普通提交、推送此分支并核远端 ref/FETCH_HEAD/tree/全部输出字节，完整 publication SHA 由最终返回外部提供，不在文件内造自指 receipt。
