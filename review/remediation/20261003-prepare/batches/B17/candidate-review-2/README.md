# B17 candidate-review-2：原 FULL 增量复审

结论：**PASS_SCOPED_FULL_CANDIDATE**。原两项 P2 在精确 NEW 解除；当前完整12贡献／7主责的局部最低验收静态满足，剩余FULL阻塞及最小返修均为空。此结论仅签本FULL候选角色，affected、G、actual、C不代签、不假设通过。

| 身份 | 精确值 |
| --- | --- |
| reviewedSHA NEW | `19095065e39481e408b40a2ca01e5a4660a320c9` |
| reviewed tree | `d9ca0072aaaa6773983bcd09bbb7d1886ab1fb0f` |
| OLD | `86bcafffbb2127c66b8636d10943cf702c18a557` |
| 正式FIX_BASE B16-C | `f66366b2bbe5c3e1cdd39459f80be672173e7f94` |
| publication envelope | `c52d727da6ab7ae3f519f0040a26eb2f305527cf` |
| 复用原FULL报告 | `15585b2c2b2d05a9689ff494c4bdac94b23fe1fc` 的 `candidate-review-1/` |
| 独立报告分支 | `codex/cloud-dot-B17-full-review-2-20261010` |

先读AGENTS，确认它在NEW与先前C/报告父树完全相同；无相关本地技能目录。维持请求 gpt-6.1-sol／ultra／default／Standard，Plan A无effective可信回显记UNVERIFIED，未请求降级、fallback或配置审计。

## 两项修复的独立判定

- **B17-R1 已解决**：正式WP76第165行恢复 `PLAYER1/PLAYER2`，重新保留两个区别完整的名字；与先前独立固定参考静态证据及C字面一致。
- **B17-R2 已解决**：第185行恢复 `双方 R1500/D350、σ＝0.9`，该固定算例的评级输入再次明确。公式与旧数值输出未改；未重算或运行向量。

独立整文件检验：NEW WP76精确等于OLD加这两次唯一替换，只有第165/185行变化，增加9字节。作者52处有界匹配被本次独立重建为49个修订标签与3个必要字面（复合标签按一处计）；52个上下文均绑定C正文，NEW保留必要的R1/R2/R1500。该范围内未见其它必要字面误删，不声称全仓重新审计。旧可选标点问题仍为非阻塞。

## 完整增量流与保护

独立重建无路径筛选的OLD→NEW `git diff --no-ext-diff --no-textconv --binary --full-index`：与发布封套唯一流逐字节相同，**39479字节、3文件**（WP76＋两个新作者证据）。完整引用 commit `c52d727da6ab7ae3f519f0040a26eb2f305527cf`，path `review/remediation/20261003-prepare/batches/B17/candidate-2/OLD-to-NEW.full.diff`，blob `483c0925b44a2a8523db056794474a9209429bce`，SHA256 `b696d08a3ab5c7d7f6233a9eea5568f40f10c4505627a6b1dd0ade4ff8d07d1a`。本报告不复制任何完整流或递归历史包。

OLD全部36614个既有路径中，除WP76外**36613个mode/blob完全保持**，无删除；NEW只新增两个作者证据文件。发布封套再新增4个candidate-2文件，不改冻结内容。264旧贡献统计精确保持；两本整目录及B16新增24行、两份获准原稿、40静态设计、原作者完整控制/source/caller/trace证据均保持。完整C→OLD流按 `d0effbf6e7cddb88482658f8c1b7616a9d5b4091` 的 `review/remediation/20261003-prepare/batches/B17/candidate-1/C-to-candidate.full.diff` 不可变身份复用，不重新复制或全历史重读。

## 12／7当前FULL结论

[contribution-review.json](contribution-review.json) 逐项承接原独立完整资格、原始／批准／当前根及扩展、合法正反例与旧回归判断。003因两处必要身份／前提恢复，由旧局部FAIL更新为静态满足；005、A040、A050、A059、B031、B032、B033、B034、C003、C119、D018的完整审阅对象精确未变，原独立结论逐项复用。所有跨包、canonical及非局部义务保留，229 OPEN／0 CLOSED。

原P003-equivalent／P003-identity的正文一致性问题已解除；其余38个设计的静态审阅结论按未变输入复用。[repair-and-case-review.json](repair-and-case-review.json) 明确**40项设计均未执行**，不是运行测试。无新reference读取、reference/game/Ruby、行为向量、旧脚本、运行观察或真实Demo证明。只执行新编写文本／哈希／树／JSON元数据检查。

[增量核验](incremental-verification.json) 给出完整流复建、52处匹配、全树和敏感文件保护证据；[范围与门](source-limits-and-gates.json) 继承U01–U10/G01–G12/AX01–AX20、conditional berry67及宿主／媒体／插件／样本／Demo限制。原affected审查者依据其OLD结论与精确NEW另签增量门；separate actual gates继续必需。B18 FULL按原合同等待B17 C读回。

仅本新目录写入，普通独立分支commit/push后读回远端ref、tree与全部报告字节；最终交接返回实际reportSHA。[report-manifest.json](report-manifest.json) 记录本目录文件身份，排除自身递归哈希。
