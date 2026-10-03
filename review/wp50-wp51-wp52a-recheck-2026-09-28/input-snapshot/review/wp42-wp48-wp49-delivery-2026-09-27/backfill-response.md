# WP44／WP45管理回填与N01关闭回应

日期2026-09-27；提取方材料。依据[独立闭合报告](../wp43-wp45-recheck-2026-09-27/report.md)与[权威执行提示](../wp43-wp45-recheck-2026-09-27/next-batch-prompt.md)，不重新审查已关闭编号，不以自检批准新包。

## 1. 固定预检

八件必检＋WP41／主TSV两件补检均实测完整SHA-256、stat字节，并与本轮input-snapshot逐字节相等；下表为回填前身份，未有漂移。reference保持指定commit只读。

| 对象 | SHA-256 | 字节 | 快照 |
| --- | --- | ---: | --- |
| `specs/combat/wp40-commands-obedience-and-action-order.md` | `ad4718722897ef448623fb2bdcd7e9e8ca9a51538a5015edc331fcae50516654` | 42,476 | MATCH |
| `specs/pokemon-rules/wp43-types-accuracy-and-damage.md` | `0cd9958c256ef2caf7d6f9933127f35e5644131a3a97ed79d46998c6bcc15688` | 30,543 | MATCH |
| `specs/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md` | `85e17c6c15225040eb5dd5f38503bbcac6c8fd96916f40270e3c989e86559311` | 49,950 | MATCH |
| `specs/pokemon-rules/wp44-effect-coverage.md` | `47bd80e20c877e612bb99e6929cf46b2efe7d87d94862760e9871234eecac3ef` | 27,133 | MATCH |
| `specs/combat/wp45-weather-terrain-side-and-position-effects.md` | `f92b0f3cfa807d0c9a069fb586cde3673f878d4762dbede3425b08b86f06f35b` | 35,823 | MATCH |
| `planning/feature-matrix.md` | `b230d1d7840b31923c741d439c2344990c18e00108a45801fdc45b6fd5078cc7` | 47,092 | MATCH |
| `planning/review-manifest-2026-09-19.md` | `8ea63286474328dcb2ca45aa6af3aac385bf7f33ec01bff4e3deda721dc340fe` | 253,979 | MATCH |
| `review/wp43-wp45-delivery-2026-09-27/delivery-summary.md` | `39275cb4291ba561557e2ee014cb5c1d5236836bcd615d981b8a31878d8b2d7d` | 9,790 | MATCH |
| `specs/combat/wp41-switching-positioning-and-escape.md` | `42878fac04b7ba5e195663f183fb484489200bab8ef5dc17333b0c0525b14085` | 31,939 | MATCH |
| `review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv` | `95415831e570e765210686c637f3552e6e9cf5a7595e2cca23eae462186720d7` | 51,044 | MATCH |

## 2. 回填与直接维护

- WP44-R01/R02、WP45-R01、BATCH-N01、C01已由独立复审CLOSED；WP43既有回填被接受。WP44主稿头尾／附表和WP45头尾按授权登记Reviewed（限定静态范围），不新增行为批准。
- WP40／WP43的N01待复核语境改为已关闭，旧发现与实际修订历史留存；沿WP40→WP41→WP43→WP44主稿／附表→WP45重新固定完整身份，只作状态／引用维护。
- 矩阵F12-01/02/03管理回填；F11-06/07与F12-06是本批新提取增量，分别ReviewPending。旧摘要v3同步闭合；旧self／boundary、reviewer原件、快照不修改。
- 限定通过集合＝WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP41、WP43–WP45、WP59–WP60。WP42／48／49首稿没有自批Reviewed。

## 3. 回填后实测身份

本表新字节不是闭合报告原始被审版本；原值见§1及manifest替代链。

| 文件 | SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/combat/wp40-commands-obedience-and-action-order.md` | `13ac33470f375f2a3c5f0af7acddb6b038b98ba058e73397f39babf592d32b42` | 42,751 |
| `specs/combat/wp41-switching-positioning-and-escape.md` | `1b7e395b98727e3aa7272ad73d3873c77f4581d0acd18ac71cc6703736a77ccb` | 31,948 |
| `specs/pokemon-rules/wp43-types-accuracy-and-damage.md` | `b5ac8946316fae5cac765db52d2344767bca2f9e5abed52ebfc331a216040ed7` | 30,921 |
| `specs/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md` | `a4e82ddf09d9d9db4e4d610e8dc074d5ef093136b74290dd83b84f764a6bdf9c` | 50,426 |
| `specs/pokemon-rules/wp44-effect-coverage.md` | `c226232d523b899197590800b8e6f75230de103363eebf6c12a16111a24cb2ad` | 27,346 |
| `specs/combat/wp45-weather-terrain-side-and-position-effects.md` | `7ddb026aa71e8576d54ab2f98df5e78e84066e28eccbada4f551ca5ae58e5d95` | 36,525 |
| `planning/feature-matrix.md` | `4234c91e8b2c3a8153e607709425b7ba89900462d069694e962f21206aa0bed2` | 48,137 |
| `review/wp43-wp45-delivery-2026-09-27/delivery-summary.md` | `4cc8e434e1a7d1feca37dce2290626055fd41fbc8d3dc8215ddc1ef43960e35d` | 10,636 |

## 4. 差异与边界

[backfill-diffs](backfill-diffs/)共8份，均相对有限复审快照；六份旧规格仅状态／身份维护，矩阵差异同时含三行管理回填与三行新批增量，旧摘要差异维护历史／当前语境。差异文本可以从原快照重建回填后文本，不对reference生成补丁。

[新批交付摘要](delivery-summary.md)给WP42→WP48→WP49串行固定及五组交界。完成批末统一送审后停止；不发reviewer消息、不创建其它任务／并行Agent、不提交／推送；所有运行未决及阶段出口保留。
