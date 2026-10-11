# B20 NEW2 电话/CN 有界 affected 再审

结论：**PASS_BOUNDED_STATIC_REPAIR_C028_CN_NO_NEW_BLOCKER**。AF-02（B15/C028）与 AF-03（B04/B19/C003，关联 B06）在本范围满足上一轮验收条件；17 个子例的静态预期有支持，均为 NOT_EXECUTED。未发现本范围剩余问题。该结论不签 actual、正式 C 或其它三组修复，也不重新认证旧308贡献。

- NEW2：commit `3f521e6dea0b442e4bb174a9715c458416386b37`，tree `49f406a6de8ca2786e5dda27abada19780fdfa05`。
- entry：commit `81d3be653e87e6424d0d8cd38dab14a9aafc97a1`，tree `a9d5db33399fee31780ea6cb6ffa3b5225b927ce`。
- readback_packet：commit `dbfa219547690f06eac9180f3ecd9dd1091eb49f`，tree `59529b00d2a3704251f6622f3b1d7b55a186dfdc`。
- prior_report：commit `680e3988c4144db269e063971991134b8e0bd678`，tree `4e2858fe6d52e9b36ede5a54a9ad730c05764108`。
- reference：commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。

固定入口为 `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-2/affected.md`；导航仅用于定位。正式正文、原稿、目录、后继fixture逐项读回后再对照源文本和原 qualified 合同；scope 准许不计入质量证据。

## 修复与增量判断

C028 的正式 WP77:113–121、原稿:137–145、共享目录:277，以及固定后继 JSON `/static_cases/2` 一致：TP 用联系人训练家 max(current,start) 版本，缺记录空文字；TE 用联系人地图与全局遭遇版本，请求版缺回退0，双版缺或三表空才空文字。合法队伍成员均匀且保留重复次数，合法遭遇表首最多4槽均匀、不按槽权重、不去重、第五槽不参加。开始消息先于 TP/TE 求值，TP→TE→地图名各一次，所有分段复用；文本无占位也不跳过。存在空队伍、非法参数及非法物种保留未保护失败，按 TP/TE 阶段区分前缀副作用与后续未达。

CN 在共享目录:270 与固定后继 JSON `/static_cases/0` 改为玩家 coins 代币窗；G 为独立 money 金钱窗。coins=37/money=1200 和 coins=0/money不变两个合法对照支持所读数值；具体千位分隔/币符号仍继承 WP17，未新增字面显示格式保证。旧 CV-M14 的兼容前缀、尾空白与反向门逐字保留。midi/mid、CommonEvent 真可达块、b/pg 和标题实体等未变部分继承上一轮 B19 固定有界证据。

## 逐项静态子例

| ID | 独立核验结果（均 NOT_EXECUTED） |
| --- | --- |
| coin-money-windows | CN读37个coins；G独立读1200 money；数值语义，格式化显示继承WP17；静态预期有支持 |
| coins-zero-money-retained | coins改0只改变CN读值，money不改仍1200；静态预期有支持 |
| resource-and-common-boundaries-preserved | 新增CN不改变既审midi/mid、CommonEvent可达块、b/pg及标题实体边界；旧B19行字节保持，沿旧固定静态证据继承；静态预期有支持 |
| normal-contact-and-encounter-versions | 联系人训练家版本max取2与遭遇全局版3独立；一次计算供全段复用；静态预期有支持 |
| trainer-record-absent | 缺版训练家记录正常空文字；不是存在的空队伍；静态预期有支持 |
| requested-version-absent-zero-present | 请求版2缺、版本0非空Land则读版本0；不先返回空文字；静态预期有支持 |
| both-versions-absent | 请求版与0版都缺才无记录空文字；静态预期有支持 |
| three-tables-empty | 三种表全空时无候选，空文字；静态预期有支持 |
| land-empty-cave-present | 合法Cave候选先于Water；静态预期有支持 |
| only-water-present | 前两种表缺/空才用合法Water；静态预期有支持 |
| party-duplicate-slots | 成员均匀；A/A/B保留A两次机会；静态预期有支持 |
| encounter-prefix-and-weights | 首4槽均匀；A/A/B/C，D及权重不参与；静态预期有支持 |
| nontrainer | 非训练家在两种候选查询前返回空文字；不等同整个呼出流程成功；静态预期有支持 |
| no-placeholder-still-computes | 分段和替换前无条件计算两个候选一次；静态预期有支持 |
| empty-party-not-missing-record | 存在记录与空成员抽样失败分开；TP异常后TE未到，无播放收尾保证；静态预期有支持 |
| invalid-encounter-parameters | 类型校验异常未保护；TP已算且start已到，不保证后续段/end；静态预期有支持 |
| invalid-species | 严格物种名查询失败按TP/TE阶段传播，不等同缺记录空文字；静态预期有支持 |

完整对象/子例 pointer、案例 ID 所在行、canonical 子例哈希和支持 evidence key 在同目录 JSON；没有复制源代码或旧证据正文。

## owner 影响边界

| owner | 增量 affected 与保留判断 |
| --- | --- |
| B15 | 新增WP77与C028为WP63候选/播放reader；电话登记仍有独立前置与未保护缺陷，没有证明Demo注册/通话 |
| B04 | 新增C003 CN/G为WP17消息窗口reader；读取与后续清理不增加异常恢复保证 |
| B06 | CN读取WP24 coins、G读取money；两个字段独立且旧资源域/写者保持 |
| B19 | 共享目录C003消费者修复；旧CV-M14及17个B19行、3个PA040行保留 |
| B08 | TE读GameData遭遇全局请求版本与版本0回退；电话首4槽均匀独立于普通遭遇权重；旧WP36/目录同blob |

B15 的联系人注册/呼出/公共事件与消息生成门保持独立：这里只审 playback/候选静态合同，非训练家 TP/TE 早退不证明整个呼出成功。正式 WP75 训练家转换 §5 在 NEW1→NEW2 逐字相同；新 ASCII 前缀校正的整体门由对应再审范围判定，不由本报告越权认证。B04 的 start 消息可能先发生，而后 TP/TE 失败不保证收尾；新段没有把正常回退推广为统一异常恢复。

WP63、WP17、WP24、WP36、UI目录（含 PL16/PL17）和遭遇目录在 C→NEW1→NEW2 均同 blob/字节；本次仅核身份以继承旧有界判定。旧报告五个相关文件在报告 commit→其既有发布读回包 be3363e8711bdf17b0f08e22517ec3bb00f9ef55 同字节；作者候选树并不包含独立报告分支，不能把该树的缺路径误判为旧报告删除。旧 CV-M14、17 个 B19 行和3个 PA040 行 C→NEW2 同字节，并记录逐行带 LF 哈希；全195顺序/重数与308全贡献另由汇总保存核验处理。

## 固定证据身份

| key | commit / path / 行或pointer | blob / SHA256 / bytes |
| --- | --- | --- |
| NEW2_phone_formal | `3f521e6dea0b442e4bb174a9715c458416386b37` / `deliverables/final-specification-set/demo-dx/wp77-demo-evidence-and-capability-coverage.md:113–121` | `e792348b0a7f35145736f7d595e86ec290b420b8` / `d1ba7c694f41ee5c3763a725467996632264e504563be74036c20d6ad5021ca6` / 29209 |
| NEW2_phone_original | `3f521e6dea0b442e4bb174a9715c458416386b37` / `specs/demo/wp77-demo-evidence-and-capability-coverage.md:137–145` | `64fc5fcf9ace768deaa640cc7f9a4190473785ea` / `46a5e1883baa6c524779f080feb7bec0602f14c3b62b0ff7c2ae41bb4cbb7180` / 47756 |
| NEW2_phone_catalog | `3f521e6dea0b442e4bb174a9715c458416386b37` / `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:277–277` | `d77a72b65a44f8d91b62dd06f0b324e7bfac774a` / `603ee184ceaed66dc6d5f6010542fb84e6a7f4da5d326e61b1227c6ad8ca9eb1` / 102307 |
| NEW2_coins_catalog | `3f521e6dea0b442e4bb174a9715c458416386b37` / `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md:270–270` | `d77a72b65a44f8d91b62dd06f0b324e7bfac774a` / `603ee184ceaed66dc6d5f6010542fb84e6a7f4da5d326e61b1227c6ad8ca9eb1` / 102307 |
| active_cases | `bfc6264bf47478bd174412289de2e31f4da2d9a6` / `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-fix-1/five-group-static-cases.json` | `1bcabfa4982655b6ccf971dba508e5ea690efc3b` / `14e51d538294bbbe8bfdd10dfd78b1091a99fa5f5ea39d7771dcfacae7196515` / 34659 |
| active_cases_at_NEW2 | `3f521e6dea0b442e4bb174a9715c458416386b37` / `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-fix-1/five-group-static-cases.json` | `1bcabfa4982655b6ccf971dba508e5ea690efc3b` / `14e51d538294bbbe8bfdd10dfd78b1091a99fa5f5ea39d7771dcfacae7196515` / 34659 |
| entry_navigation | `81d3be653e87e6424d0d8cd38dab14a9aafc97a1` / `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-2/repair-navigation.json` | `d1a11c235f8c832a13f6ceaa2dbcb2b2cb0781fa` / `fc0b453bb39c609a03e68147aa59070765754a5223f945163a075c5db1d17f65` / 18162 |
| entry_affected | `81d3be653e87e6424d0d8cd38dab14a9aafc97a1` / `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-2/affected.md` | `0780366dc4e6b28c59c5556f1a8c5eebb2425fd8` / `da9049393c0197c409a1e62fe9804b0be6465793d3edd61c6d1ca5fe753f9470` / 4077 |
| qualified_original | `41fffb540c6483f5296ea0d33b789b75180d27ed` / `review/remediation-20261003-prepare/finding-acceptance.json#/GIR-FD82-C028/minimum_revision` | `e178e5706771f5f7465bcf3351b5c632a5d68bab` / `54e4c86be3db493a5463ce4bcdef81c7184f1a1d89e6b3bbea358f14cc347225` / 2329113 |
| prior_findings | `680e3988c4144db269e063971991134b8e0bd678` / `review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-1/findings.json` | `a44f098eb421e5b91d3c59e623bd1a507a22fbb5` / `2be1300a3f1efe2eed88def32d8ef80e7afbd22337f4c3a4737ea0a7d5c09a4f` / 17158 |
| prior_owner_B15 | `680e3988c4144db269e063971991134b8e0bd678` / `review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-1/b20-owners-b13-b18.md:24–50` | `33e0b4737fb4416a65dca03f6a0e672f8ce9c493` / `a6c0c5040c83b935bcf17d5e2f5667641cf414439848cb84047a043855270e04` / 15874 |
| prior_owner_B04_B06 | `680e3988c4144db269e063971991134b8e0bd678` / `review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-1/b20-owners-b01-b06.md:14–24` | `d4fae090616c828789060aea7261c0d0008df29d` / `a6367f1c567b5b0f90e0acca4c949b5f71c974a2d36553a5f6d980c307220e5c` / 6175 |
| prior_owner_B19 | `680e3988c4144db269e063971991134b8e0bd678` / `review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-1/b20-owner-b19.md:23–41` | `0967b3258b7ab69b9b7798e69159fa16405990b0` / `163434c401442991e883df726636a65b41ef2363da1f1477d795bd78f30b91d7` / 11330 |
| prior_owner_B08 | `680e3988c4144db269e063971991134b8e0bd678` / `review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-1/b20-owners-b07-b12.md:20–20` | `578c2b7e2753bd0ccb8e6510cd3faaba62396700` / `78852360415090216f799d55bd79305ee687b823551e6fa19e5d5e8b685168e1` / 15406 |
| phone_flow | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/013_Items/004_Item_Phone.rb:414–438` | `f98163636a7d6082c2e1a8875ecd6e3b9b8fb007` / `81519d2fb0b6926ac2ca08f693e2f08e3800878628ba90f5a7d2a314ff1c60f4` / 25386 |
| phone_TP | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/013_Items/004_Item_Phone.rb:506–512` | `f98163636a7d6082c2e1a8875ecd6e3b9b8fb007` / `81519d2fb0b6926ac2ca08f693e2f08e3800878628ba90f5a7d2a314ff1c60f4` / 25386 |
| phone_TE | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/013_Items/004_Item_Phone.rb:515–535` | `f98163636a7d6082c2e1a8875ecd6e3b9b8fb007` / `81519d2fb0b6926ac2ca08f693e2f08e3800878628ba90f5a7d2a314ff1c60f4` / 25386 |
| phone_registration | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/013_Items/004_Item_Phone.rb:172–184` | `f98163636a7d6082c2e1a8875ecd6e3b9b8fb007` / `81519d2fb0b6926ac2ca08f693e2f08e3800878628ba90f5a7d2a314ff1c60f4` / 25386 |
| encounter_version | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/010_Data/002_PBS data/013_Encounter.rb:30–35` | `e69d300dd0e21690e5970452017e4c2bd457021a` / `d7ebeb1d00434f5da96165ad407101a14d007bce03fa0d0e267c5ee293c183f7` / 2267 |
| trainer_lookup | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/010_Data/002_PBS data/015_Trainer.rb:75–83` | `d6a875e6f96a6e14f06644214d0824ec8b504790` / `fe0533a71e62244b5169fa1948ef06832a92cd59fa69fadae75ad05667d506b1` / 8177 |
| species_binding | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/010_Data/002_PBS data/008_Species.rb:45–50` | `1ce450615687be8ecba5dde48474dd745acda29d` / `0a2bbc80b607c9bb69708a0cd6da9c81489b3b09424388c0d5c0a38d450d3f5c` / 20284 |
| species_lookup | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/010_Data/001_GameData.rb:97–105` | `ccfd971a29b3bab107e2da6865ac0050ed3256b0` / `577359664875c9e2ae78fc1b979409d28b4be932f6b5e8297de76a7df604db26` / 9010 |
| messages_money | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/007_Objects and windows/011_Messages.rb:310–327` | `91c985bd0fda9a2368c894dee0ebbc9a476e9886` / `88e72c557c53da5a72e4d5b4de7431bbfbd03f4f8f27bcf44ac231a5141b8536` / 25224 |
| messages_coins | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/007_Objects and windows/011_Messages.rb:330–343` | `91c985bd0fda9a2368c894dee0ebbc9a476e9886` / `88e72c557c53da5a72e4d5b4de7431bbfbd03f4f8f27bcf44ac231a5141b8536` / 25224 |
| messages_dispatch | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/007_Objects and windows/011_Messages.rb:584–592` | `91c985bd0fda9a2368c894dee0ebbc9a476e9886` / `88e72c557c53da5a72e4d5b4de7431bbfbd03f4f8f27bcf44ac231a5141b8536` / 25224 |
| player_resources | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/015_Trainers and player/004_Player.rb:11–16` | `3a2f3b83a6050831a6fe881b0ccb0ab6ac6e8fd6` / `9b9daa93633906e50430f4d94b3a4ae821d0b0cd568148714f9d3c23952521a3` / 4132 |
| player_resource_setters | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/015_Trainers and player/004_Player.rb:76–87` | `3a2f3b83a6050831a6fe881b0ccb0ab6ac6e8fd6` / `9b9daa93633906e50430f4d94b3a4ae821d0b0cd568148714f9d3c23952521a3` / 4132 |
| C_catalog | `de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f` / `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md` | `17ea088afe9e3fb67e4cbeaf5a7e6faa2eff940d` / `ffd8992eef39f39892709d5dd591780669c97a0bd59dda9cc0f55818fee2e9f1` / 90084 |
| NEW1_catalog | `1abaefb1db5818ff9404392143c476979d34c21a` / `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md` | `a4a5279c9826d87e9663780c6e35a92cc733ffef` / `6e9e463d4f6b7d7591d0d30e457787b759c56c4a3638080a15e92e63eb84cc45` / 100779 |
| NEW2_catalog | `3f521e6dea0b442e4bb174a9715c458416386b37` / `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md` | `d77a72b65a44f8d91b62dd06f0b324e7bfac774a` / `603ee184ceaed66dc6d5f6010542fb84e6a7f4da5d326e61b1227c6ad8ca9eb1` / 102307 |

以上均由独立 Git 对象读取重新计算，并核定 NEW2/tree 和固定参考/tree。工作只读取静态文字和运行本人新写 Git/JSON/hash/text 元数据代码；参考 checkout 保持干净。无运行观察、随机实际取样、Demo链、编译/转换/反序列化或行为向量执行，未修改 repo/正文/原稿/参考/main，未提交或推送。
