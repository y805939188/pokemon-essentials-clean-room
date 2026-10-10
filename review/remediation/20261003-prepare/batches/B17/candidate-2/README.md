# B17 NEW：原两位 Ultra 增量入口

NEW审查候选commit：`19095065e39481e408b40a2ca01e5a4660a320c9`

NEW审查候选tree：`d9ca0072aaaa6773983bcd09bbb7d1886ab1fb0f`

OLD审查候选：`86bcafffbb2127c66b8636d10943cf702c18a557`，tree `8626342ceeba125603aca6cac5b86b4e454a8ba0`。

此次只恢复正式WP76 §7.2的 `PLAYER1/PLAYER2` 与 §7.4固定算例 `双方 R1500/D350、σ＝0.9`。正文两行增9字节，所有其它旧路径mode/blob保持。新增两个作者返修证据文件说明两P2、有界52处匹配及完整保护；公式、数值结果、目录、原稿、40静态设计不变。没有执行行为或旧程序。

`OLD-to-NEW.full.diff` 为以上端点完整未过滤3文件delta，唯一保存一次，身份/字节/库存见 `diff-manifest.json`；前后输出身份见 `output-manifest.json`。旧完整C→OLD流、完整控制与源证据以及报告只作不可变引用，不在此复制。NEW从OLD直接分支，避免把旧发布封套和其中完整流再次嵌进delta。本四文件封套位于NEW的后继发布commit，独立审查固定NEW SHA。

原FULL Ultra入口：报告 `15585b2c2b2d05a9689ff494c4bdac94b23fe1fc` 的 `candidate-review-1/findings.json`，对照 `author-draft-2/repair-and-protection.json`、NEW正文两行及完整delta，复核B17-R1/R2和003必要身份/前提回归。

原affected Ultra入口：沿自身对精确OLD的独立结论读取相同NEW/delta，判断真实影响和保护；当前作者未收到其新增发现或报告，不猜测通过。其余旧证据可按精确scope复用，不能把旧报告的局部满足或本作者修复当作NEW PASS。全部原控制、source limits及非局部义务继续绑定，G/ACT/C及后续separate actual gates未签。
