# WP39／WP40／WP41闭合回填回应（→WP43／WP44／WP45）

2026-09-27，Asia/Shanghai。提取方材料，不是独立review。已完整读取根AGENTS.md与本闭合报告／执行提示，活动子目录未发现另有适用AGENTS.md；reference只读，固定commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。

依据：[闭合报告](../wp39-wp41-closure-review-2026-09-27/report.md)与[回填＋下一批提示](../wp39-wp41-closure-review-2026-09-27/next-batch-prompt.md)。独立结论为三个被审v3均PASS_SCOPED（限定静态范围），原12项及C03全部闭合；本轮无另立C04。允许先管理回填后同轮串行WP43→WP44→WP45。

## 1. 六项固定预检与主TSV补检

逐件使用shasum -a 256和stat -f %z，并与闭合input-snapshot逐字节比较；七件全部MATCH、无漂移，未覆盖快照。

| 文件 | 被审／回填前SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/combat/wp39-battle-context-and-participants.md` | `864dec262b0d7e3f9bdc4944bab07f2c2bcefd459fee2f6a46af9323bf0122f5` | 42,165 |
| `specs/combat/wp40-commands-obedience-and-action-order.md` | `716a244244248bc25d626ed487fc4b47b65cd942942a3d9647821cbfde84ef7d` | 40,100 |
| `specs/combat/wp41-switching-positioning-and-escape.md` | `463cab3c062a366a7b142f66248ea9e5bb5bacb9a12ff8748f930aefd498a2ec` | 31,502 |
| `planning/feature-matrix.md` | `2402cf4281b1aefb0770545d0ff147e56252f5b1ff9f36ceeb97777ac0691c8f` | 46,283 |
| `planning/review-manifest-2026-09-19.md` | `029ace88ec69272796cd6be016d605be5d4e0ebb18b31948a9c52008265ca30d` | 228,722 |
| `review/wp39-wp41-delivery-2026-09-27/delivery-summary.md` | `8360aec47b2bff8d03287fb07e23a96a7dc229cdf305ba071f7a79794d19e841` | 11,292 |
| `review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv` | `4bf6bcf4947aebeae1e46f10ba9ced94c4ed227c2d69435253c5802f56929a97` | 44,821 |

## 2. 管理回填范围与新身份

三稿头部及§15按闭合报告§4限定范围回填Reviewed；仅改状态、范围说明、互相状态引用和上游完整哈希，不改变已接受行为。v1/v2及本轮被审v3保留历史，新哈希不冒充reviewer审查字节。

| 包 | 被审v3 | 当前回填后SHA-256 | 当前字节 | 范围 |
| --- | --- | --- | ---: | --- |
| WP39 | `864dec262b0d7e3f9bdc4944bab07f2c2bcefd459fee2f6a46af9323bf0122f5`／42,165 | `9a3a796f08335bc7d4886c7e2b11f3b273c955e24ba9d6fe966c60103df5719b` | 42,697 | 已述入口／输入／跳过／返回，布局／业主／参与者写回，创建规则／环境／钩子和善后接口 |
| WP40 | `716a244244248bc25d626ed487fc4b47b65cd942942a3d9647821cbfde84ef7d`／40,100 | `07789951f9aaaa7cac82508218a3f58c76caa735e18e4fad9f9a2dcd123a80d3` | 40,547 | 已述命令／控制／登记取消、分族复检／PP与物品消费、服从／排序与特殊动作时机 |
| WP41 | `463cab3c062a366a7b142f66248ea9e5bb5bacb9a12ff8748f930aefd498a2ec`／31,502 | `e6b835af5db676a28b80e7fb1513cf379267b2cdab427c7e9cc916e8e8a4c234` | 31,897 | 已述换人资格分层／替补入场、Shift／重映射、三类逃跑与有界强制换出／形态交界 |

完整绑定按WP39→WP40→WP41重新实测：WP40→WP39，WP41→WP40／WP39。WP39 §11对WP40/41及WP40 §11对WP41的待审状态已同步；尾部把对方已通过子范围与WP42等未决分开。其余旧规格的领域责任／完整组合前向并未因此完成，本轮未修改其行为。WP43新发现的N01反例在新规格与交界中具名登记，没有借管理回填静默改写已审WP40。

## 3. 矩阵与旧摘要

矩阵分两个逻辑增量：F11-01～05仅将对应已审子范围回填Reviewed并保留Inventoried；F12-01～03随后按新批具名范围更新ReviewPending＋Inventoried，未改变F11-06/07或其它Feature。矩阵差异含这两组共8行，读者可按Feature编号区分。为避免多次覆盖，两个增量合并为一次最终文件写入。

旧交付摘要改为v4：追加独立闭合记录与回填后完整身份，v1/v2/v3声明加历史语境；旧self-checks／boundary-checks和所有旧回应／reviewer原件保留。当前限定通过集合仅为 **WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP41、WP59–WP60**。

## 4. 回填差异

以本闭合input-snapshot为基准，五份新差异均独立按差异块在内存重建当前目标，5/5匹配。未向参考或快照应用补丁。

| 差异 | SHA-256 | 字节 |
| --- | --- | ---: |
| `backfill-diffs/wp39-backfill.diff` | `77966eba98c81e8c8d0f00cf505cefcbdde69bfd02057436862e41d368e5f60d` | 5,818 |
| `backfill-diffs/wp40-backfill.diff` | `f8e88efaeb26180262d108e1a4f8bb0f6dc415653ff62c52aacaec732c402373` | 6,623 |
| `backfill-diffs/wp41-backfill.diff` | `5ed55ae0a5e04f0650ce688c29968bd55f7308b9e38fa49eedc2037a05ff3b97` | 5,065 |
| `backfill-diffs/feature-matrix.diff` | `1617019c19041bfe3ff09551871093ea5f30563560254fe3bffd88d716ddcf4a` | 9,702 |
| `backfill-diffs/previous-delivery-summary.diff` | `83297d8191544eed153f4a29567d49fa98851ee95c8224a96cafe98f838ffcdd` | 11,601 |

闭合报告完整身份 `c88d91cf0202e083294870896283fc10264860f608b8bad69ba46b9c622b7f07`（11,892字节）；执行提示 `a712c0fb9c3311bfbade32305cfb000827864d5bb985d07567022c1763f9ed35`（16,208字节）。

## 5. 边界与出口

三新包仅为ReviewPending，不自批Reviewed。完整终局／成长WP42、特性／道具／招式家族、AI、设施、WP22/23、捕获及真实运行均按各自范围保留。未运行游戏、参考Ruby／表达式、解释器／事件脚本、生成器、编译器、转换器、插件或真实网络，未操作真实地图／存档／输入；未创建并行Agent／任务、未发reviewer消息、未提交／推送。仅用自有文本、哈希、集合、JSON、diff和独立算术。管理回填完成后按授权同轮完成WP43→WP44→WP45，批末统一送审后停止。
