# A-B03 author-v3 完整候选返修交接

状态：第一轮三项作者修订完成，**待同一 R-B03 Ultra 问题与回归复审**。第一轮整批 REQUEST_CHANGES 仍是旧候选结论，作者文档/Git 审计通过不构成语义验收、integration、B06 依赖许可或 CLOSED。

- 完整 payload：`3c5728a47142c57abfdf3d55033768bc44a1f627`；tree `69338441a6c8fac3a97b122b405fcdde3b6494c9`。
- 追加父 SHA：`76b6f6c6f14f1d676f370be72b61cb2f0a069633`；完整比较基线（已接受 B02）`9576f00e7d3aeb96f7ca8c42caccfba8f808505e`；第一轮报告 `4706be652a4d9e70656d1e2db1cbc0be9a9194c6`。
- 普通分支：`remediation/20261003-prepare/batch-B03`。本 README、冻结清单和完整 diff 由随后仅证据追加 commit 承载；13 份正式文件与 payload 相同，实际 push/远端 HEAD 以最终执行交付为准。

| 问题 | 本轮修订 | 新静态对照 |
| --- | --- | --- |
| R-B03-001 / P2 | WP12 两稿明确 F9 按住、移动中登记、静止后消费；ACTION/SPECIAL 的登记门单列，检测成立但资格失败不落到后键。 | MV68–71、75–77 |
| R-B03-002 / P2 | WP12 两稿及两份路线矩阵区分主解释器/三个自动移动标记与角色强制路线；WAIT 期间 ACTION 仍可登记；旧队列消费另门。 | MV72–76 |
| R-B03-003 / C053 / P2 | 两份解释器矩阵及 WP13 两稿同列取消/确认的可见→原映射与缺项 raw 回退；隐藏 A 的后组取消1进 C。 | IM36–41：无隐藏、正常确认、101 合入、403 回退、一次性变换清空 |

27 原贡献/19 主责逐项见 [finding-responses.json](finding-responses.json)；3 个第一轮完整独立反例及作者回应见 [review-responses.json](review-responses.json)，条款与向量见 [traceability.tsv](traceability.tsv)。26 项第一轮局部通过的测试及其原贡献合同继续保护；C053 与三项问题均待同一审查者裁定，R-B03-001/002 不由 C054 局部通过消除。公共登记只有 [registry-proposals.json](registry-proposals.json) 建议，唯一 A-REG 串行处理。R-B03-003 归既有 C053、不增加第三个新根因；原229整体计数未改。

[完整冻结清单](candidate-freeze.json) 列所有 53 个候选差异路径（13 正式＋40 作者证据）及 blob/SHA256；[完整 diff](candidate-full.diff) 为已接受 B02 到新完整 payload 的零上下文/full-index diff，**5,215,961 bytes**，SHA256 `cb1a1cdadd0f904eed2b045a348569d8e1d6d353a475f158b0f3c93e8676a56d`。其中包含旧作者/上一候选全部证据，不只交 76b6→新修订增量。冻结候选与证据 HEAD 分开；复审时应核证据 commit 的 parent 与13正式文件身份。

正式总范围仍13条，本轮仅9条/17处精确修改，见 [scope-and-review-inputs.json](scope-and-review-inputs.json) 和 [formal-edit-ledger.json](formal-edit-ledger.json)。57 阶段＋1历史输入、B01/B02 前提不变，未消费 B05；WP36/C081 属 B08 待修，WP65 属 B16 待修。旧 author 的16文件、author-v2 的12文件及独立审查输入12文件保持字节；原稿历史批准/未决尾部、公共登记、上游和共享目录 WP15/59/60 不改。

[文档/Git 身份审计](self-check-result.json) 通过2099项检查：235旧静态行原字节保留，追加16条，现251条全部未执行；96解释器行、46路线行、B01首次奇数写回失败、ASCII及三路线字面保持；42相对链接和58表格结构通过。正文、附表、组合/反向对照及作用范围见 [verification.md](verification.md)。参考在主仓库外，固定 SHA `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，clean、只读；新13次原文本读/搜索，旧51次读不改，没有参考/游戏/Ruby/编译/生成/反序列化/模拟器/求解器执行。

U01–10/G01–12/AX01–20 及地图、媒体、宿主、插件具名未知保留：运行观察0、已证明 Demo 链0、静态向量执行0。请求 gpt-6.1-sol / Max / Standard(default)，方案 A，实际生效配置 UNVERIFIED；无 Max 不支持推断、无降档/加速、无派生。无环境/权限阻塞。普通 push 后停止等同一 R-B03 Ultra，不自行整合或消费为 B06 前提。
