# WP68–70 整合批次管理收尾 v2 回应（B-INTEGRATION-R01／R02，均 P3）

2026-10-03；单一整合者。依据 [report.md](../../wp68-wp70-integration-review-2026-10-03/report.md) 与 [next-task-prompt.md](../../wp68-wp70-integration-review-2026-10-03/next-task-prompt.md)：**仅两项管理同步收尾**，无行为返工。整合 v1 报告、回填表、自检、映射、管理 diff、本 review 原件与快照全部留史原字节；25 项导入、12 份原件、48 份快照、7 份路径重映射版规格与全部已批准行为产物**不重新导入、不改字节**。reference 固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、Git 清洁。

## R01（P3）回填数量重复计数（已修）

- **v1 残留**：整合报告 v1 第 25 行与末检把回填写为「46 处标注＋5 处规格链接附注」——已含 5 处旧附注的 46 又加了 5。
- **修订**：按单位分列并落到新材料——**状态标注回填 41 处**（B 活动 6＋主线包/N01/WP76 共 16＋GR 状态附注 19）＋**已有规格链接状态附注同步 5 处**＝**合计 46 处**；另有 **6 条 B 新增规格链接**——Notes 列合计 **11 行**变化、矩阵状态列 **40 行**变化（F04-03 一行含 GR-004 与 GR-011 两项回填）。修订版整合报告 [report-v2.md](report-v2.md)、按单位列出的回填依据 [backfill-register-v2.md](backfill-register-v2.md) 与 [checks.json](checks.json) 一致。
- **历史处理**：第 129 轮登记叙述中的旧计数**不回写历史**，由第一百三十轮登记追加勘误说明纠正（见本轮 manifest §2.2 与 §4）。
- **保持**：矩阵已正确的 40 行状态/Notes 变更不重做。

## R02（P3）manifest「当前有效版本」状态没有同步收口（已修）

- **v1 残留**：manifest §1 共 **35 条当前规格记录**仍写待复审注记（如 WP19/GR-016、WP65、WP76 行），与同节矩阵汇总行及已通过报告冲突。
- **修订**：按 [current-index-status-residuals.json](../../wp68-wp70-integration-review-2026-10-03/current-index-status-residuals.json) 的 35 条范围与 [approval-authorities.json](../../wp68-wp70-integration-review-2026-10-03/approval-authorities.json) 的批准入口逐项核对，**manifest §1 该 35 条注记已同步为「当前：Reviewed（限定静态范围，<最新具名批准>——批准依据 <报告路径>）；历史提交状态：<原送审说明>」**——**规格文件、完整哈希、字节与历史审计原件全部保持**（35 份规格身份实测未变，见 [current-index-sync-35.json](current-index-sync-35.json)）；不是批量重写已批准主稿，也不是全局删除历史 ReviewPending（两处旧交付材料行的旧注记按提示不在 35 条规格范围、保持原样）。
- **F17-07／F18-06／F18-07 收紧**：报告 v2、回填依据 v2 与 manifest §1 矩阵汇总行统一为——**F17-07 的 WP71 A～F 静态范围已于 2026-10-01 闭合并回填保持，保留未确认的是事件奖励、媒体、全尺寸可解性/分布等未验证子范围**；**F18-06 Provisional、F18-07 Demo 验证范围 Provisional 保持实际状态**，不笼统改成全部 Inventoried 或全部 Reviewed。矩阵本身已正确，本次未再改其状态或行为。
- **严格管理 diff**：[management-diffs/review-manifest-2026-09-19.diff](management-diffs/review-manifest-2026-09-19.diff)——基线为本 review `input-snapshot/` 冻结 manifest（`ab1c41b7…`／1,113,174，round-129 最终），patch 精确重建 R02 同步后的 manifest 字节（35 条注记同步＋矩阵汇总行 F17-07 收紧）；第一百三十轮登记（标题、TSV 行、新材料行、§2.2/§3/§4 追加）在该 diff 之后按惯例另行登记。

## 总体自检

- 35 份规格身份实测未变（current-index-sync-35.json 逐行含当前 SHA-256/字节）；35 条新注记与 Feature Matrix 同行状态一致（矩阵 `f4e4d472`／72,052 未再改动）。
- 计数口径：41＋5＝46（状态/Notes 分列；40 状态行＋11 Notes 行）——v2 全部材料与第一百三十轮登记摘要一致。
- 链接：v2 材料全部本地链接经脚本解析存在（见 [checks.json](checks.json)）。
- 保持：整合 v1 与本 review 原件、快照、25 项导入、12 份原件、48 份快照、9 份 B 规格（含 7 份重映射版）、WP76 及全部已批准行为产物原字节；WP68/69/70 原 PASS_SCOPED、WP76 20/20 及所有既有具名批准保持。
- 状态：本批 **ReviewPending（管理收尾 v2，待两项短复核）**——不自行标通过、不启动 WP77。
