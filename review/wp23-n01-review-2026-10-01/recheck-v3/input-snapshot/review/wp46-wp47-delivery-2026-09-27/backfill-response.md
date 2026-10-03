# WP42／48／49限定Reviewed管理回填回应

日期2026-09-27，提取方。依据[独立复审报告](../wp42-wp48-wp49-recheck-2026-09-27/report.md)与[执行提示](../wp42-wp48-wp49-recheck-2026-09-27/next-batch-prompt.md)，三原编号及C01已CLOSED。此次回填不重做独立review、不修改已接受行为。

## 1. 回填前固定预检

六件必检加self／boundary／主TSV三件补检均用shasum完整SHA-256与stat字节实测、与本轮input-snapshot逐字节一致。

| 文件 | 回填前／被审完整SHA-256 | 字节 | 快照 |
| --- | --- | ---: | --- |
| `specs/combat/wp42-growth-end-of-round-and-battle-outcomes.md` | `6644c77775b1e02481674079c847652dbbf2c566214d3969f1f333f741c22f7d` | 41,329 | MATCH |
| `specs/pokemon-rules/wp48-ability-calculation-modifiers.md` | `87e39127e14eddd10f6e0d10e6d63999e0cb9ff70fa0e2505dc97a195f3b3bb8` | 35,021 | MATCH |
| `specs/combat/wp49-ability-phase-triggers.md` | `7a4ecf931a65931cd8c6255d09b2697f83a5b538da907a016e5712efa32a67d7` | 52,573 | MATCH |
| `planning/feature-matrix.md` | `6d9a28754bd2cfb3622a8a6dbf6b624600fd8c45aa34db570dc111f57c455a20` | 48,271 | MATCH |
| `planning/review-manifest-2026-09-19.md` | `6dfa15eadfa3b40a125741b90192a80b17ae0925e993b7f95a62b8a476ec4631` | 279,090 | MATCH |
| `review/wp42-wp48-wp49-delivery-2026-09-27/delivery-summary.md` | `e41b85316b620dede8ce1b8c30f61cbbdabee155a069ae34bbce19c5258a1e58` | 8,520 | MATCH |
| `review/wp42-wp48-wp49-delivery-2026-09-27/self-checks.json` | `939f7e366b0c75feb45275e5ee340647715499cde96144b22bb78273925864e3` | 102,908 | MATCH |
| `review/wp42-wp48-wp49-delivery-2026-09-27/boundary-checks.json` | `9509999c8dadeba83dfeceb39fd4d45d7d0b1494e1837abed8f01163792a309b` | 14,399 | MATCH |
| `review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv` | `e16fc33168b07694e0791ac96fc81cf367bdd37d9ab70cb6e9a8c9d4f1e9a4b5` | 57,528 | MATCH |

## 2. 授权范围与管理差异

WP42头尾只登记A～E成长／学招等待／场上同步、27阶段与早退／替补、正常终局／世界交接、默认拾取采蜜与异常边界；WP48头尾只登记27族148身份计算／资格／免疫；WP49头尾只登记21族119身份阶段与直接生命周期。均注明2026-09-27 v2有限复审PASS_SCOPED，并链接独立报告。WP49仅再同步WP42／48回填后的完整身份；被审v1／v2都保留。

矩阵F11-06/07、F12-06分别按具名子范围Reviewed＋前向Inventoried，F12-02/03只更新对WP42的状态引用；F12-04/05为另行新批增量，只ReviewPending。旧活动摘要v3记录闭合，旧self／boundary、修订回应／差异、reviewer与快照不倒写。

## 3. 回填后实测版本

新字节是管理回填版本，不能冒充独立复审原始v2对象。

| 文件 | 当前完整SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/combat/wp42-growth-end-of-round-and-battle-outcomes.md` | `8b8149c3b1f6ee7d130802a4fe1638404a5ac76e7927ee4ce77c85ee5127620f` | 41,759 |
| `specs/pokemon-rules/wp48-ability-calculation-modifiers.md` | `457a47b0438a5664fa75e1988251e5aefea2620efec0c006c4f78f7c12a00611` | 35,320 |
| `specs/combat/wp49-ability-phase-triggers.md` | `b5c083209e218dc17d7490cc2f171a653502d05e58ec66b83b403ea6d96b4e25` | 53,127 |
| `planning/feature-matrix.md` | `9b0ac4a232ec2df4855f8ad31b32d9ef2d9511185d4384647f57c515b434efc8` | 48,848 |
| `review/wp42-wp48-wp49-delivery-2026-09-27/delivery-summary.md` | `498dde568f7c77c30c35d28e2ab492622b7c985c0243977683b54d184111f695` | 9,388 |

## 4. 验收与保留

三稿状态／历史身份／尾节之外的主体逐字节保持；WP49另外只更新两上游引用。拾取18／11表与重复位、C06整数96、野生敌方存活计数、MOODY和ICEFACE已闭合文本不改。[backfill-diffs](backfill-diffs/)五份均相对本轮快照；矩阵差异明确混合管理回填和新批F12-04/05增量，不视为旧包行为修改。

限定通过集合为WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP45、WP48–WP49、WP59–WP60，不连续全部完成。新批WP46→WP47-A→WP47-B见[交付摘要](delivery-summary.md)，三包均ReviewPending。新提取中对旧WP40／41摘要的三条具名观察只在新材料登记、待独立review判断，没有静默改旧规格。

完成管理回填与三个新包及批末交界后停止；未执行参考、未发消息、未创建任务／Agent、未提交／推送。运行／Demo／宿主／媒体／插件／U01–U10和WP78→79→80继续保留。
