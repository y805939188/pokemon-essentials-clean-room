# B17 affected candidate 增量复核：B07

NEW结论：**PASS_SCOPED**。WP28训练/增量、WP30成长与WP31进化caller以及WP67A/B/两原稿均同版。提前糖/经验写入不回滚、净化室跨级部分写入失败与遗迹石空刷新、同轮最终取消窗口保持；名字和评分输入不成为成长或进化新条件。

reviewedSHA：`19095065e39481e408b40a2ca01e5a4660a320c9`；tree：`d9ca0072aaaa6773983bcd09bbb7d1886ab1fb0f`；OLD：`86bcafffbb2127c66b8636d10943cf702c18a557`；封套：`c52d727da6ab7ae3f519f0040a26eb2f305527cf`；正式FIX_BASE仍`f66366b2bbe5c3e1cdd39459f80be672173e7f94`。

上一轮报告固定为 `8610526b5079f06f7ea9701f0f5bbd24dfec317f` 的 `affected-candidate-review-1/B07/review.json`，当时结论 `PASS_SCOPED` 只对应OLD。此次独立查看完整delta、核实原caller/data/condition同版，并判定两处恢复对本owner的具体影响；旧报告不改，也不自动转签。

公共核验一次：完整OLD→NEW未过滤3文件、589行、39479字节流与独立Git重建完全相同；只有WP76第165/185行字面恢复、+9字节，外加两个作者返修证据。36613个其它旧路径mode/blob保持，无删除。NEW从OLD直接分支，四文件发布封套是NEW后继。

WP76除两精确替换外整文件保持；其它四formal、两原稿、两目录、40静态设计及旧作者证据同版。264旧贡献统计与C/OLD/NEW整体相同；B16新24行再次逐字节、顺序核验。只复用精确有效证据，不重新阅读全部历史。

B17-AFF-01的名字在NEW恢复，与固定静态caller两名NPC构造相符，B06有界阻塞解除。B17-AFF-02的固定`双方 R1500/D350、σ＝0.9`输入已恢复，公式/数字输出/当前σ限定不变；只核验返修事实，FULL数学门未签。

本owner无剩余影响阻塞或额外最小返修。NEW结论范围仅affected candidate；FULL、actual、G/ACT/C、canonical closure及正式接受未签，不发起后续任务。

[review.json](review.json) 记录精确上一轮证据身份及本轮独立理由；[公共核验](../B04/shared-verification.json)仅写一次。完整diff只引用已有封套commit/path/blob/SHA256，不复制增量流或旧大型流。

请求gpt-6.1-sol/ultra/Standard(default)，Plan A继续，有效配置UNVERIFIED，无新增认证门。40例仍为未执行静态设计；reference/game/Ruby/行为向量/旧程序/真实Demo证据均未运行。U01–U10/G01–G12/AX01–AX20、条件树果67及具名未读源/样本/媒体/宿主/插件/地图/Demo限制完整继承。
