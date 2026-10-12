# 第四轮云端事实规格 update：完整执行任务书

本文由用户在第四次Desktop独立review完成后，另行交给dot并明确要求执行时生效。仅从仓库读取本文不构成启动授权；原Desktop会话没有发送、调度或开始本update。人类启动后，不必为本任务已授权的常规读取、隔离工作树、规格修订、独立审查、合格接受、整改分支提交与普通push重复索取许可。遇到真实权限/材料阻塞、固定对象冲突或必须由用户决定的政策，再提出具体问题并继续不受影响工作。

## 1. 长期目标与净室边界

项目要从参考Pokémon Essentials完整提取能力、规则、外部行为、输入输出、数据/资源契约、数学、状态/时序、边界/失败、玩家与开发者流程，作为以后从零使用TypeScript和现代工具独立设计实现高质量引擎的输入。本轮是事实规格整改，不是新引擎实现。不得复制源代码、逐行翻译Ruby、照搬源类层级/容器/调用组织、把RGSS/RPG Maker宿主限制变成未来架构。必要内容身份、数值、协议与可观察兼容事实可准确描述，源符号只作审计。

参考及所有旧报告/接受字节只读。只改下文28个授权正式路径内的具名事实合同/附表/静态向量及必要引用；新证据/进度/注册在新的 `review/remediation-fourth-.../` 目录。禁止改写本第四轮报告、旧229/341/GR3关闭记录、历史审查或归档；不为统一旧OPEN/PENDING数字重写冻结文本。不得创建TypeScript包、战斗/引擎适配器或生产框架代码，不合并或push main，不force，不移动交付/归档标签，不自动扩大可选或未决政策。

## 2. 固定输入、身份与获取

- repository：`y805939188/pokemon-essentials-clean-room`，origin `https://github.com/y805939188/pokemon-essentials-clean-room.git`。
- 正式输入B commit `1f36475d22120a0d1175967d5b17d71fe8311d88`，tree `d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a`，delivery tag `delivery/third-round-clean-20261012`。从[固定CURRENT-DELIVERY](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1f36475d22120a0d1175967d5b17d71fe8311d88/CURRENT-DELIVERY.md)读取交付语境，再按[正式131身份](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1f36475d22120a0d1175967d5b17d71fe8311d88/delivery/2026-10-12/formal-identities.json)逐字核验；目录 `deliverables/final-specification-set/`。
- 参考R repository `Maruno17/pokemon-essentials`，commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`；[固定参考入口](https://github.com/Maruno17/pokemon-essentials/tree/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b)。本机审查源曾位于 `/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials`；云端自行定位只读副本并核固定身份，不能把本地绝对路径当云端必存在。
- 最终实质review报告快照 commit **`417e99d4eab78c512b6b002db2a67eadefbee7e7`**，tree **`90dd96e8dfb95e367feed824735db2749cc720b7`**。报告根 **`review/global-independent-review/fourth-2026-10-12-1f36475-c92e/`**；独立报告分支 `codex/review-fourth-20261012-1f36475-c92e`。固定[最终报告](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/final-report.md)、[完整规范findings](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/findings.json)。该快照已完成语义/反证/去重，后继只绑定handoff与发布身份，不能把导航补充当新全量语义门。
- 本prompt自身与后继manifest不自嵌自己的commit/hash。`cloud-fourth-update-handoff-manifest.json`在后继提交准确绑定本prompt冻结commit及下面报告身份，publication-receipt再绑定manifest和远端读回。用户终局消息提供两者固定SHA链接；接手应核这些外部绑定。若只拿到本prompt，可从唯一报告分支的该路径读取后继manifest，要求其review_snapshot严格等于上面的 `417e99d4eab78c512b6b002db2a67eadefbee7e7/90dd96e8dfb95e367feed824735db2749cc720b7`，核本prompt和所有输入bytes/SHA/blob后冻结所读manifest身份；出现内容或对象漂移则报告差异，不能静默用浮动main替代B。

### 必要报告材料的完整身份（路径相对报告根；链接固定报告快照）

|材料|bytes|SHA256|Git blob|
|---|---:|---|---|
|[README.md](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/README.md)|3535|`09a860bdc30ef2f15caeaea0b93739128941b5f406ce3fc323b78f55ae7c4714`|`928da794bcbb34edf586ad2e2a011c6e9edc21a4`|
|[final-report.md](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/final-report.md)|13494|`c6ce78c1f0b06ee4ffcc08c3157caf96ebe948c3e6628454999bc6a7b848107d`|`62a64291308a4c9a2e2c22ca5726818d43c5aebd`|
|[findings.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/findings.json)|296265|`3fb1368243bd942a58a3ad156228c3bbf41e5bf245520204ece90e3981cb9487`|`b376bf1264e09abdbe8bfd39f5f34f18dac164c2`|
|[findings.schema.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/findings.schema.json)|3072|`e8cd72ec70bf6d2996db74df2bbc103972ca951938221405420b4f4eab78e7cc`|`aa7e8c01bf1334169bdc4551225c14bcf1797ac2`|
|[schema.md](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/schema.md)|2686|`01b1da0a99d22411c22bcd8dc51c1d3c8794babc754d5a07c49e450d2290a3d7`|`f0f383bbce42170a3fb79e5d4f07ae343b1c1fe9`|
|[source-to-spec-coverage.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/source-to-spec-coverage.json)|2427540|`047f8e899bd47c48345ad003c761808bca919d0530cbdab3132469db1e60e47e`|`dfbc93d936078a931713b769616392f3568370bc`|
|[spec-to-source-coverage.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/spec-to-source-coverage.json)|1225457|`1cd201670f191f3fad845836cb0b49b52b0f9fbdafeb45cb2d86809be8deb4cc`|`8546db663dad0642a23e7fad50f7e97c3df3e1c1`|
|[coverage-summary.md](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/coverage-summary.md)|2889|`aa07268e7a20f149f140f27bf9b1e381b142c01161429a7467ac96a94d2f2f49`|`3b44934d04f1072397d8bf439c0f0fa62b7df680`|
|[baseline.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/baseline.json)|6632|`37ab51d160cb9309bc8c6066fd270063c5ef143e1da4bc1bb7ee74808c30f179`|`811f8232a86b4704e3c62d78b36541ab4e82e5b2`|
|[readiness.md](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/readiness.md)|1706|`22701e7a831e45e862d1294e8896adb5bfa24e8baa5c7198d5af27af6656b35d`|`d9b49080a5043bb103efdf7bff1039eea8241ece`|
|[progress.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/progress.json)|12033|`9f79f468cfc4bbd6c4b8d393d5bbb32d779ee4e668faae1600f1693e069d743b`|`a26c78682de7b843f286be3b323ac8ac414a5e22`|
|[regression-third-23.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/regression-third-23.json)|225473|`81ad7922fef001299d578e92eec3fc645a279649f8fda2614dc5e382b73e196a`|`2c50d5071ae86e2eac062d510c68637d45d6c9c5`|
|[regression-legacy-scope.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/regression-legacy-scope.json)|2046691|`c7103c598d10482e3b265596bbc0765e4356bac86c127941eb9cd7cfe2586265`|`c8a6453d65c91512b7df457bce1e586d04d70185`|
|[junction-review.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/junction-review.json)|306707|`982e7ba342247573b04204baf22c774d394e885f25c7059f14fc7cfabfa07183`|`529b6a6f2e6c26e76e4fa643da09f2a37c07e11a`|
|[execution-evidence.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/execution-evidence.json)|84823|`7eda349e04c761adbe5e434da67de0da91bdcecd393e4f897a16bc9d39614eb6`|`54afd5808b36ad4dd4566f46be9ec07e45144afa`|
|[limits-and-missing-materials.md](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/limits-and-missing-materials.md)|4203|`a65f40a1b9c35a8ddc407b19c64f2bb29b4ed5a1c079b5eac66904e29109a4c5`|`4cd53f756d772526bfddca825933bf7e2e670753`|
|[proposed-update-batches.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/proposed-update-batches.json)|34174|`b02584d1231c00c115e153a6dc41a028d38da4a90fac651f08b95022666b3af1`|`ba131b6cd044639de7a42b7c319815e5e1a7209f`|
|[shared-file-owners.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/shared-file-owners.json)|12494|`bef6625655a3d6d3c6d6334e22a0bc18d6543374dea9a0c7ae3cb051175be41a`|`ff85057e544627470dd696d772a25715f19629d8`|
|[counterreview-and-dedup.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/counterreview-and-dedup.json)|29058|`f415abcf1ac71fa617c19642c8afd849355c6a94314caf9956951c6b57a77493`|`64893a3498687760422f03dea75c893b2864c7ca`|
|[modules/CA/verdicts.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/CA/verdicts.json)|107323|`99de01142327d9650d681e45e3db8075be3dcd5e8c09e153e52b752dca6a7633`|`1363dd4ad2f520c98ff467cd51eb463e4b217f7e`|
|[modules/CB/verdicts.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/CB/verdicts.json)|74219|`79541a1e4998bfc51595d25f142f97783d88b10232b51bf4c372b84319bf3a6e`|`24cdd86ebda7ad511181feeba7c020f5cb7091ea`|
|[modules/J/junctions.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/J/junctions.json)|253002|`daca51f898c95acc6598b032089c98496672a929e7b7d5fac9b274766e0ee772`|`e927a03306b8ae2bc439a1c366a6b46a737c10f7`|
|[modules/J/shared-capabilities.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/J/shared-capabilities.json)|37322|`46ea2559e1bd7967ee6e805f08b405e76b0058d841f56e316d75aeb2eb0aeb10`|`d93f1fc8454f597e2cc940c0a0da4bfdef25992e`|
|[evidence/formal-identity-check.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/evidence/formal-identity-check.json)|95229|`12ab3a732411e49a5a8a8b4a161bb6b3a243a433d1821fdd712d50fff8d22f7e`|`1b2977ef532bcac8f16f5e7b6759a0ecaca60a26`|
|[evidence/reference-inventory.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/evidence/reference-inventory.json)|125004|`9952b8b94ab72f5511fc3e25b4d9d97d15839b971b0a15c1f6c2fae946984f30`|`bf952aabaafc6f277b469c5a461484d546ff7d82`|
|[evidence/junction-navigation.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/evidence/junction-navigation.json)|128008|`71902eebabfcdccd20523ecd3ec0876d45ae1fa12167712ab1fd460eb9f9f57e`|`f8b49224f49a0aede45c50d975bcb031f396bbe9`|
|[evidence/legacy-projection-links.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/417e99d4eab78c512b6b002db2a67eadefbee7e7/review/global-independent-review/fourth-2026-10-12-1f36475-c92e/evidence/legacy-projection-links.json)|26115|`59042cd4ccb1cba6fa2ffb0056a4ebf5cc7ad12935b7b4f1ddd5e28119dbb098`|`27d2303158d067818c47990a1da38fdece22311a`|

完整333份已冻结报告产物的逐文件身份由后继manifest列出；不递归复制旧全部历史。正式B的131身份和参考R的432 tracked身份分别在固定清单内，来源/字节与语义正确性不能混为一谈。

资源范围：R是独立嵌套Git仓库，432 tracked字节匹配；两个根BMP实际存在、均8×8/24位/246字节，属于R，非额外资源包。312脚本、73 PBS、18翻译、8字体、SoundFont及若干Windows二进制可读；没有Graphics/Audio、地图/事件/System/Tilesets/CommonEvents、动画数据库/映射和完整Demo。仅两份.DS_Store属本地额外元数据，不应搬入云端；无完整资源包叠加。R/LICENSE身份在参考清单中，原许可和分发范围保持，不把代码或资源整包提交到整改分支。文件存在、头部可解析、完整可用、运行成功四层分别记录。

## 3. 规范数量、历史状态与审查结论

本轮规范ID共17：REQUIRED=17（P1=0/P2=11/P3=6），OPTIONAL=0，UNRESOLVED=0，NO_REQUIRED_REVISION=0；无重复合并后的额外ID或别名。CA独立质疑11项，CB质疑6项；9项直接确认、8项精确化确认。M02-002从初审P2收窄为P3。原模块原稿保留其生成字节，根findings.json/最终报告是规范结论；不能拿原稿未精确的句子覆盖以下限定。

不是“全能力通过”：12域给出300个可交叠范围记录（260 supported_static/34 partial/3 missing/3 unresolved），131文件均有责任和局部核对，不等于全部条款通过。25项共享契约单主责，J直接查14链（6 supported_static/8 partial）。历史54交界+8链+18新链共80条导航已核，47条接本轮有限投影，其余33仅历史范围复用。完整未审、资料与运行未知继续保留。

GR3必修23项原CLOSED/6主题接受/U07complete保持，当前激活回执仍是固定 `98e49a592c9e82b1e53d3f1fd403ba2ad0935983:review/remediation-third-20261012-prepare/registration/final-closure-acceptance.json`。本轮逐23映射当前文件/源/criteria/消费者，所核范围未见回归，不把76历史标准自动转签成已执行。GR3-M03-004的116生产端、GR3-M10-002的普通命令/逐位数字为新增scope；旧关闭身份不改。GR3-M09-001 OPTIONAL继续暂缓/U08未启动；GR3-M02-003 NO_REQUIRED_REVISION不重开。

旧229和341 exact scoped contributions在regression-legacy-scope.json逐记录有去向和资格/owner/候选/actual/独立报告固定身份。默认historical_qualified_evidence_reused/not_reexecuted；7具名旧控制静态投影与J04/A053孵化投影另列。341不是功能数；同一ID一个owner通过不能关闭其它owner责任，旧签名不能转到新字节或条件。未被改变/未新审部分继续有限复用，勿重跑整包旧行政审计。

## 4. 全部必修任务（完整条件、反例、修订与验收）

以下源锚点均是R，规格锚点均是B；完整文件身份见共同清单和每项JSON的identity。辅助证据若写相对路径，均相对该项artifact_origin；全量机器格式为固定findings.json。这里完整列出核心任务，不能只读标题自行补政策。

### GR4-M01-001 · P2 · REQUIRED — 翻译同域重复键与重复节的逐项合并规则缺失

领域 M01；分类 数据或资源契约缺口；独立审者 thread `01a12fc9-8425-7c80-b000-3fcaa86b76f1`；辅助证据目录 `modules/M01/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/001_Technical/003_Intl_Messages.rb` · 437–466,481–489：节内后键替换，归一键碰撞，节间同位置合并；并非整节替换。（固定R；blob `f6c27e5d6efacfa696cfcad018007e9ff1c0a072`）
- `Data/Scripts/001_Technical/003_Intl_Messages.rb` · 376–384：所有输入累计到同一消息集合。（固定R；blob `f6c27e5d6efacfa696cfcad018007e9ff1c0a072`）
- `Data/Scripts/021_Compiler/001_Compiler.rb` · 154–181：按文件顺序逐节送入导入；重复节头未拒绝。（固定R；blob `1dd5f374734935f15502f973e07d2a603a1477dd`）
- `Data/Scripts/001_Technical/002_Files/001_FileTests.rb` · 6–14：完整导入的文件枚举结果排序；单文件向量不依赖跨文件排序。（固定R；blob `d753bdae844e8ab44c858718fdc1bc175216ddd6`）
- `Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb` · 1457–1475：作者编译菜单实际调用完整导入。（固定R；blob `6dd0c35a31040174efadefa2ba24a1c85a2499f9`）

**现规格依据**

- `deliverables/final-specification-set/generic-kernel/wp08-localization.md` · §3.2,§6.3;30,98–105：已列归一/形态，没有同域冲突解决规则。（固定B；blob `ef337ff445c701874e9728af118e33fcea33b99b`）
- `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` · LZ17,LZ21：显式无合并冲突前提，没有对照向量。（固定B；blob `3c7daba49da60cca2f6051839e408fc0426978a5`）
- `deliverables/final-specification-set/generic-kernel/wp08-localization.md` · 52：语言game覆盖core是查找优先级，不能代证同域导入冲突处理。（固定B；blob `ef337ff445c701874e9728af118e33fcea33b99b`）

**参考实际行为**

同一合法文本域内的重复规范键取最后译文；后续同域同形态节逐项合入已积累域，覆盖同键但保留先前独有键。按索引节同样只覆盖后节实际提供的索引，不删除稀疏遗漏位置。

**现规格的说法**

WP08描述键归一、数组/哈希判别、节号、失败及运行层game/core优先；未规定同域重复输入的覆盖与保留结果。LZ17/21用无冲突前提规避该分支。

**差异/缺口**

独立实现可合理选择重复拒绝、先值优先或整节替换；三者都不符合固定参考的合并结果。

**必要前提**

- 单一普通可读翻译文件，非地图24号域；所有内容非空、非注释且段落形态合法。
- 同域多节按文本出现顺序；不更换被测入口，不假定默认语料本身含重复。

**最小反例**

```json
{
  "input": "一个24号哈希节按顺序含K→First、K→Last。",
  "reference_result": "成功，K仅取Last。",
  "distinguishes": "重复拒绝/首值优先均不同。"
}
```

**正常对照**

不同键K→First、L→Other均保留；同域后节K→Last、M→New合入后，K=Last、L=Other、M=New。

**失败/边界对照**

A双空格B与A单空格B先规范成同一键后取后值；数组先入再以非数字哈希键向同域合入的探针抛TypeError，前节内存数据保留，不能把所有混合形态都说成安全合并。按索引0/2先入、后节仅0时，2保留。

**独立实现影响**

拆分翻译文件、重复修订或空白规范碰撞时，最终消息集合和运行查找可能不同；这是有效导入数据合同而非风格要求。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-search.json#N01",
    "scope": "全部131正式Markdown（含scope、正文、附表、测试）",
    "terms": [
      "重复",
      "同键",
      "合并",
      "覆盖",
      "冲突",
      "duplicate",
      "collision",
      "merge",
      "翻译",
      "译文",
      "本地化",
      "SCRIPT_TEXTS",
      "compile_text",
      "Translation",
      "文本域"
    ],
    "reviewed_contexts": [
      "deliverables/final-specification-set/generic-kernel/wp08-localization.md §3.2/§5.1/§6.2–6.4",
      "deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md LZ01–LZ25",
      "deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md:20",
      "deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md:13"
    ],
    "result": "未找到同域导入的重复键/节合并规则；命中是game/core查找、导出目录覆盖或地图文件分组，语义不同。"
  },
  "primary_relative_paths_base": "modules/M01",
  "independent_counterevidence": {
    "search_ids": [
      "M01-merge",
      "M01-definition",
      "CA-shared-alias-supplement"
    ],
    "words": [
      "重复键|重复节|同域|同键|文本.{0,18}(合并|冲突)|翻译.{0,25}(合并|冲突|覆盖)|译文|localiz|compile_text|stringToKey",
      "过渡坐标|冲浪基点|冲浪.{0,8}清|动态形态查询|资源消费.{0,15}形态|形态.{0,15}副作用|计时.{0,10}变量|变量.{0,10}计时|PP.{0,20}(补给|补充|活体|存活)|翻译.{0,10}(重复|合并)|文本域.{0,10}(覆盖|冲突)"
    ],
    "scope": {
      "baseline": "1f36475d22120a0d1175967d5b17d71fe8311d88",
      "root": "deliverables/final-specification-set/",
      "files": 131,
      "includes": "正文、共享条款、数据附表及静态测试目录；并非131篇逐篇重新验收"
    },
    "source_countersearch": [
      {
        "id": "M01-definition",
        "pattern": "def (compile_text|compile_text_from_file|pbEachSection|_INTL|_ISPRINTF|_MAPINTL|_MAPISPRINTF)|compile_text\\(",
        "files": 312
      }
    ],
    "contexts_read_and_assessed": [
      "WP08 §3.2/§5.1/§6.3，LZ17/LZ21",
      "WP03 §5.2同键注册、WP05 §3.1处理器同键替换均有各自入口范围，不是翻译编译",
      "WP17 §3.1为显示预处理"
    ],
    "conclusion": "未找到同域翻译逐项覆盖/保留合同。game/core查找顺序、PBS重复注册及导出删除均不能代替导入冲突规则。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CA"
}
```

**下一轮最小修订**

WP08作者导入补节内规范键后值覆盖、同形态重复节按键/索引合并及早节独有项保留；明确混合形态不保证兼容。补最小正常与冲突向量，不要求新框架采用原容器结构。

**验收标准**

```json
[
  {
    "kind": "static_required",
    "criterion": "正文与LZ补同键、规范碰撞、重复同域节独有键保留及稀疏索引保留的准确结果。"
  },
  {
    "kind": "static_required",
    "criterion": "分开同域编译合并与game/core运行查找优先；保留完整入口先截断副作用及Map形态门。"
  },
  {
    "kind": "execution_optional",
    "criterion": "若执行，记录独立同文件夹具和所用参考入口；不得把本次隔离执行升级为宿主/完整导入通过。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/generic-kernel/wp08-localization.md
- deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md

**共享合同**

- WP08 §3.2 文本身份
- WP08 §6.3 作者导入
- WP04末段消息产物交界（无需复制重复规则）

**依赖**

- 文本预处理与消息查找
- 作者翻译工具；实际文件系统/宿主不在执行证明内

**能力范围引用**

- GR4-CAP-M01-015

**关联新问题**

无。

**根因身份**

GR4-M01-TRANSLATION-SAME-DOMAIN-MERGE

**旧GR3/229/341关系**

```json
{
  "relationship": "new",
  "third_round_ids": [],
  "second_round_id": null,
  "note": "不重开GR3-M01-001–004；第三轮为行过滤、稀疏导出、PBS井号、电话默认身份，本项不同根因。",
  "independent_scope_assessment": {
    "relation": "adjacent_import_header_contract",
    "ids": [
      "GIR-FD82-A013"
    ],
    "assessment": "已读绑定qualified_scope和B WP08/LZ17。A013解决节名非零前缀/零例外；本项固定合法头24后比较同域内容归并，属相邻阶段，不是旧项重开或同一反例。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- EXECUTED_REFERENCE

**执行状态**

Original selected functions executed with minimal ancillary stubs on Ruby 2.6.10; NOT_EXECUTED_HOST_OR_DEMO; full compile/export not executed.

**置信限定**

high within stated inputs and fixed baseline

**未知**

- 实际全部语料中的碰撞数量、完整菜单/二进制保存、所有混合域形态组合未执行。
- 未证明默认语料含重复；所有混合形态及完整宿主作者流程未运行。

**排除的主张**

- 不声称导入过程应拒绝重复或应被修复。
- 不声称默认18份语料当前存在这些重复。
- 不以本项重开第三轮行过滤问题。

**用户政策边界**

记录固定参考事实无需新增决策；未来是否兼容异常可另决，不修改参考。

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CA",
    "thread_id": "01a1301e-5efe-77a2-9450-fc09ff6830c1",
    "path": "modules/CA/verdicts.json",
    "pointer": "/records/0",
    "decision": "CONFIRM",
    "reason": "原R在节内规范化键后写入、在后节只覆盖实际有值项；B只规定形态/身份和运行回退，未决定冲突结果。单键与双节反例共同使缺口有确定可观测差异。",
    "required_refinements": [],
    "execution_evidence_assessment": {
      "ca_rerun": false,
      "receipt": "../M01/validation/reference-probe.rb + reference-probe-result.json",
      "kind": "REUSED_ISOLATED_REFERENCE_EVIDENCE",
      "version": "Ruby 2.6.10p210",
      "assessment": "加载原分节器和单文件导入器，未替换合并核心。常量辅助替身不影响数值节头24；nil/empty替身虽不等于原函数全部类型语义，但本组全为有效字符串，结果一致。未跨500行刷新门，未跑完整菜单、输出截断或跨文件导入。",
      "host_or_demo": "NOT_EXECUTED / bundled Ruby 3.1 host UNVERIFIED",
      "new_execution_claim": false
    },
    "historical_relation_assessment": {
      "relation": "adjacent_import_header_contract",
      "ids": [
        "GIR-FD82-A013"
      ],
      "assessment": "已读绑定qualified_scope和B WP08/LZ17。A013解决节名非零前缀/零例外；本项固定合法头24后比较同域内容归并，属相邻阶段，不是旧项重开或同一反例。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M01-002 · P3 · REQUIRED — 普通本地化占位参数并非完全字面插入

领域 M01；分类 事实错误；独立审者 thread `01a12fc9-8425-7c80-b000-3fcaa86b76f1`；辅助证据目录 `modules/M01/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/001_Technical/003_Intl_Messages.rb` · 774–823：普通与地图占位使用替换字符串，格式化入口以格式计算结果插入。（固定R；blob `f6c27e5d6efacfa696cfcad018007e9ff1c0a072`）
- `Data/Scripts/007_Objects and windows/002_MessageConfig.rb` · 790–814：备用定义有条件，不覆盖正常已定义本地化入口。（固定R；blob `47813fd34df588b24a5cc84f9928d9a55f4bcfc6`）

**现规格依据**

- `deliverables/final-specification-set/generic-kernel/wp08-localization.md` · §5.3;67 / §8;142：字面替换概括缺少反斜线参数例外。（固定B；blob `ef337ff445c701874e9728af118e33fcea33b99b`）
- `deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md` · 13–30：显示控制符属于后续窗口层，未解决本地化插入阶段。（固定B；blob `81b14a0b09327bc030e5d9ef9f907089bd68cb82`）

**参考实际行为**

普通脚本和地图占位入口会解释参数中的替换特殊组合：两个真实字符反斜线和&恢复被匹配的占位文本；反斜线和数字1在本例中变为空。字符串格式化入口对照保留反斜线和&。

**现规格的说法**

WP08 §5.3将普通占位概括为字面替换，未限定参数字符串中反斜线的解释。

**差异/缺口**

依完全字面插入实现，输入参数反斜线&将输出该两字符；固定参考却保留原占位标记，返回文本不同。

**必要前提**

- 正常本地化主入口已定义，未被插件覆写。
- 当前语言两层无命中，故取原文X{1}Y；本例在进入任何消息窗口之前观察返回字符串。
- 参数为U+005C与U+0026两个字符，或U+005C与U+0031两个字符；不是字符U+0001。

**最小反例**

```json
{
  "input": "原文X{1}Y，参数为两个真实字符U+005C/U+0026。",
  "reference_result": "X{1}Y",
  "literal_result": "X后接U+005C/U+0026再接Y"
}
```

**正常对照**

普通参数Q返回XQY；格式化字符串入口原文X{1:s}Y、同反斜线&参数返回包含这两个字符的X\&Y。

**失败/边界对照**

普通参数U+005C/U+0031返回XY；地图5的普通入口和脚本普通入口对反斜线&均返回X{1}Y。没有异常，不涉及WP17之后的暂停控制符转换。

**独立实现影响**

含反斜线的作者参数或动态名称的返回文本可能改变；影响范围有限，但“字面”合同会指导出不同字符串结果。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-search.json#N02",
    "scope": "全部131正式Markdown",
    "terms": [
      "字面替换",
      "占位",
      "后向引用",
      "反向引用",
      "backreference",
      "替换表达式",
      "replacement",
      "INTL",
      "参数"
    ],
    "reviewed_contexts": [
      "deliverables/final-specification-set/generic-kernel/wp08-localization.md §5.3/§8",
      "deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md:13–30",
      "deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md LZ04"
    ],
    "result": "未找到参数反斜线的本地化阶段例外；WP17的反斜线1是显示控制层，不能解释本次返回前已消失的参数。"
  },
  "primary_relative_paths_base": "modules/M01",
  "independent_counterevidence": {
    "search_ids": [
      "M01-placeholder",
      "M01-definition"
    ],
    "words": [
      "字面替换|后向引用|反向引用|backreference|replacement|占位|反斜线|_INTL|_MAPINTL"
    ],
    "scope": {
      "baseline": "1f36475d22120a0d1175967d5b17d71fe8311d88",
      "root": "deliverables/final-specification-set/",
      "files": 131,
      "includes": "正文、共享条款、数据附表及静态测试目录；并非131篇逐篇重新验收"
    },
    "source_countersearch": [
      {
        "id": "M01-definition",
        "pattern": "def (compile_text|compile_text_from_file|pbEachSection|_INTL|_ISPRINTF|_MAPINTL|_MAPISPRINTF)|compile_text\\(",
        "files": 312
      }
    ],
    "contexts_read_and_assessed": [
      "WP08 §5.3/§8；LZ04",
      "WP17 §3.1 U+005C显示控制阶段"
    ],
    "conclusion": "“字面替换”无参数反斜线例外；WP17的显示控制不能反证发生在返回文本之前的替换。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CA"
}
```

**下一轮最小修订**

将“字面替换”限定为常规参数，不承诺任意参数逐字保留；用字符码明确两项参考边界和格式化入口对照，保留未来兼容选择。无需规定未来语言的替换API。

**验收标准**

```json
[
  {
    "kind": "static_required",
    "criterion": "正文给出X{1}Y加反斜线&返回X{1}Y、加反斜线1返回XY，以及Q正常对照。"
  },
  {
    "kind": "static_required",
    "criterion": "图区普通占位同样适用，格式化字符串对照保留反斜线&；明确观察在消息窗口前，勿混同U+0001。"
  },
  {
    "kind": "execution_optional",
    "criterion": "任何重跑使用准确输入字符并记录参考入口、解释器版本及宿主未执行界限。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/generic-kernel/wp08-localization.md
- deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md

**共享合同**

- WP08 §5.3 占位参数
- WP17消息输入（仅依赖引用）

**依赖**

- 文本预处理与消息查找
- 作者翻译工具；实际文件系统/宿主不在执行证明内

**能力范围引用**

- GR4-CAP-M01-016

**关联新问题**

无。

**根因身份**

GR4-M01-PLACEHOLDER-REPLACEMENT-ESCAPES

**旧GR3/229/341关系**

```json
{
  "relationship": "new",
  "third_round_ids": [],
  "second_round_id": null,
  "note": "不重开GR3-M01-001–004；第三轮为行过滤、稀疏导出、PBS井号、电话默认身份，本项不同根因。",
  "independent_scope_assessment": {
    "relation": "new_bounded_scope",
    "assessment": "本项在固定B/R独立成立；未把原模块历史PASS当证据，未重开旧关闭项，未扩审229。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- EXECUTED_REFERENCE

**执行状态**

Original selected functions executed with minimal ancillary stubs on Ruby 2.6.10; NOT_EXECUTED_HOST_OR_DEMO; full compile/export not executed.

**置信限定**

high within stated inputs and fixed baseline

**未知**

- 所有反斜线组合、占位嵌套和游戏UI实际效果未穷尽。
- Ruby2.6隔离结果不是随附3.1宿主执行。
- Ruby3.1随附宿主未实测；更多反斜线组合和窗口最终呈现未审。

**排除的主张**

- 不将参数字符称为已发生的安全漏洞。
- 不推断用户实际游戏文本出现该输入。
- 不要求未来保留异常；必修只针对参考事实表述。

**用户政策边界**

记录固定参考事实无需新增决策；未来是否兼容异常可另决，不修改参考。

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CA",
    "thread_id": "01a1301e-5efe-77a2-9450-fc09ff6830c1",
    "path": "modules/CA/verdicts.json",
    "pointer": "/records/1",
    "decision": "CONFIRM",
    "reason": "这是有限的返回文本合同不准确，P3恰当。源码使用会解释替换参数的路径，而格式化入口的对照路径不同；不是本地化模块不存在，也不是安全漏洞。未来选择字面插入仍须另列兼容政策。",
    "required_refinements": [],
    "execution_evidence_assessment": {
      "ca_rerun": false,
      "receipt": "../M01/validation/reference-probe.rb + reference-probe-result.json",
      "kind": "REUSED_ISOLATED_REFERENCE_EVIDENCE",
      "version": "Ruby 2.6.10p210",
      "assessment": "字符由码点构造避免字面转义混淆；查找两层缺失回原文的源链已读。普通/格式化入口均保留原函数；备用定义有条件，不覆盖已存在主入口。支持所列返回字符串，不支持游戏显示或所有转义组合。",
      "host_or_demo": "NOT_EXECUTED / bundled Ruby 3.1 host UNVERIFIED",
      "new_execution_claim": false
    },
    "historical_relation_assessment": {
      "relation": "new_bounded_scope",
      "assessment": "本项在固定B/R独立成立；未把原模块历史PASS当证据，未重开旧关闭项，未扩审229。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M02-001 · P2 · REQUIRED — 游戏变量墙钟计时能力及查询清零/天数边界未进入正式规格

领域 M02；分类 缺能力；独立审者 thread `01a12fc9-af72-7672-b6bf-1c6e0d86f1e3`；辅助证据目录 `modules/M02/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/019_Utilities/001_Utilities.rb` · 157-191 / pbTimeEvent,pbTimeEventDays,pbTimeEventValid：设置与查询均可由脚本调用；未到期返回false且清变量；天数入口与通常日历倒计时不同（固定R；blob `39df7ce43a848625a8596e6bf52692024140af7c`）
- `Data/Scripts/004_Game classes/001_Switches and Variables/003_Game_Variables.rb` · 12-24：变量槽默认0且仅<=5000写入（固定R；blob `20528bd0cd146fe271dc741c1b522a277015e5ff`）
- `Data/Scripts/002_Save data/004_Game_SaveValues.rb` · 42-47：游戏变量整体持久化（固定R；blob `30d41c45ed3b37aeb2e8d8d368ba750c741006c8`）
- `Data/Scripts/004_Game classes/007_Game_Event.rb` · 88-126：私有事件时间/冷却不写游戏变量槽，不等价（固定R；blob `aca6d0992927e1d6ce37f08c2cb75e73ebcb7374`）
- `Data/Scripts/003_Game processing/003_Interpreter.rb` · 373-382：设置事件时间写事件私有记录并置自开关（固定R；blob `21666002e7f4038dd3763b632538becaae5f8d7d`）

**现规格依据**

- `deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md` · §3.1-3.3 L25-50：本轮核对的合同定位（固定B；blob `f293da252a3c344ca6b9c6059bc6e56cd51a5b48`）
- `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` · TM01-14 L37-54：本轮核对的合同定位（固定B；blob `3c7daba49da60cca2f6051839e408fc0426978a5`）
- `deliverables/final-specification-set/engine-overworld/wp13-map-events-npc-followers.md` · §3.1 L26-31：事件页/私有冷却近邻（固定B；blob `6c8046fb3691e6208b588c9090fb85dc7ea4ead4`）
- `deliverables/final-specification-set/engine-overworld/wp13-interpreter-command-matrix.md` · 命令124 L44；计时统一说明L138：游戏累计时间定时器近邻（固定B；blob `bfff8453529890f2ea6e7d00ed9b7e1033da0130`）
- `deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md` · L26,95：墙钟消费者枚举未含本变量计时合同（固定B；blob `a2bda5c3e0d5b967d8ef050bc36b4cac8ed8c420`）

**参考实际行为**

对合法游戏变量槽，秒数设置记录当前墙钟和非负持续时间并刷新地图。查询只有经过时间严格大于正持续时间才为真且保留记录；未到期、恰到期或非正期限返回假并把变量清成0、刷新地图。天数设置按参考日内余数与epoch计算期限，不能替换成通常的次日零点语义。 一般天数输入在d<0时先取0；若设置时Unix墙钟秒为t，保存持续量D=(t mod 86400)+86400×max(d,0)−t。该量不是下一午夜相对时长。

**现规格的说法**

WP06仅列时钟类别及部分消费者；WP13的事件私有冷却/命令计时器、WP59墙钟引用不提供上述游戏变量设置/查询合同。TM目录没有其正常、等阈值、提前查询清零、天数异常对照。

**差异/缺口**

缺少一个可直接调用的持久变量计时能力，并遗漏会销毁尚未到期记录的状态变化。

**必要前提**

- 固定R无覆写，游戏变量对象存在、槽1可写
- 秒数例受控墙钟1000、持续100、地图refresh正常
- 各子例独立；无读取前改变槽值；不是实际Demo事件
- 刷新替身仅计调用；若解释真实地图刷新，假定刷新正常返回且不回写该变量。探针中的刷新次数只指替身调用，不是事件页已执行次数。

**最小反例**

```json
{
  "input": "时间1000设置槽1持续100；时间1050查询一次；1101再查询",
  "reference": "首次false并清0；第二次仍false，原计时已消失",
  "spec": "仅凭正式集合无法确定该状态变化"
}
```

**正常对照**

独立设置1000/100，首次查询1101：true、原记录保留；设置时刷新一次，成功查询不再刷新。

**失败/边界对照**

独立查询1099或1100：false、变量0、设置及查询共两次刷新。持续0/-5均最终false。天数例epoch=1728000100、days=1，存储期限=-1727913600，查询false并清0。

**独立实现影响**

实现方可能遗漏入口，或把查询写成无副作用的>=到期判定、把天数入口修成日历语义，从而改变作者事件的等待与重置行为。

**已完成的反证**

```json
{
  "primary_review": {
    "record": "evidence/negative-search.json",
    "search_ids": [
      "timers_identity",
      "timers_alias"
    ],
    "scope": "全131正式文件",
    "result": "精确/概念同义词0；别名33行12文件，命中为形态时间戳/电话/消息等待/树果/事件私有冷却，不含变量计时清0规则。另读WP13命令124与WP59 L26/95近邻。",
    "source_countercheck": "全Data/Scripts搜pbTimeEvent族仅三个定义；未找到覆写/固定调用；不推成能力不存在。"
  },
  "primary_relative_paths_base": "modules/M02",
  "independent_counterevidence": {
    "search_ids": [
      "M02-timer",
      "M02-callers-overrides",
      "CA-shared-alias-supplement"
    ],
    "words": [
      "pbTimeEvent|墙钟|计时.{0,15}(清零|变量)|变量.{0,15}(计时|时间戳|倒计时)|提前查询|到期|过期|cooldown|expired",
      "过渡坐标|冲浪基点|冲浪.{0,8}清|动态形态查询|资源消费.{0,15}形态|形态.{0,15}副作用|计时.{0,10}变量|变量.{0,10}计时|PP.{0,20}(补给|补充|活体|存活)|翻译.{0,10}(重复|合并)|文本域.{0,10}(覆盖|冲突)"
    ],
    "scope": {
      "baseline": "1f36475d22120a0d1175967d5b17d71fe8311d88",
      "root": "deliverables/final-specification-set/",
      "files": 131,
      "includes": "正文、共享条款、数据附表及静态测试目录；并非131篇逐篇重新验收"
    },
    "source_countersearch": [
      {
        "id": "M02-callers-overrides",
        "pattern": "pbTimeEvent|AntiRandom|pbPostData|pbPostToString|pbPostToFile|def pbGetTimeNow|def rand\\b|def self.rand\\b",
        "files": 312
      }
    ],
    "contexts_read_and_assessed": [
      "WP06 §3及TM01–14",
      "WP09持久变量条目；WP13事件私有冷却及124累计游戏时间",
      "WP59墙钟消费者；WP53比赛计时及24小时查询"
    ],
    "conclusion": "这些共享合同证明时间/存储存在，但没有槽位计时查询销毁未到期记录的规则；未定位pbTimeEvent族默认调用或覆写，只保留可调用脚本工具能力。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CA"
}
```

**下一轮最小修订**

在WP06增加架构中立的游戏变量墙钟计时合同和源事实异常，说明两设置入口、查询副作用、变量持久化、无默认调用证据；在目录增加独立正常/边界/失败向量。源异常是否未来修正另列政策。

**验收标准**

```json
{
  "static": [
    "无需读源码可确定1000/100的1099、1100、1101三个独立结果",
    "提前查询再迟查询明确均false及状态0",
    "天数具体数值和非正期限不伪称标准日历倒计时",
    "与WP13事件私有冷却及累计游戏时间计时器分开，附WP09变量持久化依赖",
    "给出一般天数公式D=(t mod 86400)+86400×max(d,0)−t、默认/负期限和严格大于门；保持无默认caller证据的限定。"
  ],
  "runtime": "本次隔离执行有回执；修订可静态验收，不要求游戏宿主/真实事件或真实存档执行。"
}
```

**受影响正式文件**

- deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md
- deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md

**共享合同**

- WP09游戏变量持久化
- WP13事件脚本输入
- WP59墙钟

**依赖**

- 游戏变量
- 墙钟
- 地图刷新请求

**能力范围引用**

- GR4-CAP-M02-021

**关联新问题**

无。

**根因身份**

M02-unextracted-variable-clock-timers

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "GR3": [],
  "second_round": null,
  "note": "未猜测第二轮ID；不是GR3两已关闭问题的重开。",
  "independent_scope_assessment": {
    "relation": "new_bounded_scope",
    "assessment": "本项在固定B/R独立成立；未把原模块历史PASS当证据，未重开旧关闭项，未扩审229。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- EXECUTED_REFERENCE

**执行状态**

原始函数在Ruby2.6隔离替身环境执行；非EXECUTED_HOST_OR_DEMO；evidence/probe-result-v2.json

**置信限定**

HIGH within stated scope

**未知**

- 真实事件/插件使用方式
- 宿主游戏运行
- 畸形数组与所有编号边界
- 畸形槽值、所有变量编号、真实事件使用、完整宿主刷新/存取未证。

**排除的主张**

- 不认为功能有默认Demo调用
- 不修改参考
- 不要求未来重现天数错误或查询销毁策略

**用户政策边界**

本轮只需记录参考事实；未来是否修正源异常/保留兼容性留后续用户政策决定，不要求复刻代码。

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CA",
    "thread_id": "01a1301e-5efe-77a2-9450-fc09ff6830c1",
    "path": "modules/CA/verdicts.json",
    "pointer": "/records/2",
    "decision": "CONFIRM_WITH_REFINEMENT",
    "reason": "源端可调用能力真实存在：源定义公开于脚本环境，解释器具脚本执行入口。缺默认caller不能抹除能力。提前查询销毁状态、严格大于门和非正期限行为没有正式承接；ROOT一般数学与R一致，应补入而不只留异常数字。",
    "required_refinements": [
      "明确一般天数公式D=(t mod 86400)+86400×max(d,0)−t，t为设置时墙钟Unix秒；不可替换成下一午夜。",
      "把refresh回执称为替身调用次数；实际刷新无异常/无回写为向量前提。",
      "保留无默认调用证据和未来兼容政策待定。"
    ],
    "execution_evidence_assessment": {
      "ca_rerun": false,
      "receipt": "../M02/evidence/probe.rb + probe-v1.rb + probe-result-v2.json",
      "kind": "REUSED_ISOLATED_REFERENCE_EVIDENCE",
      "version": "Ruby 2.6.10p210",
      "assessment": "原变量类与三个原函数被加载；时钟替身提供固定输入，地图替身只计refresh次数，未运行事件页刷新，因此仅支持无刷新回写的有界状态和调用次数。变量持久化来自SaveValues静态证据，未运行存档。",
      "host_or_demo": "NOT_EXECUTED / bundled Ruby 3.1 host UNVERIFIED",
      "new_execution_claim": false
    },
    "historical_relation_assessment": {
      "relation": "new_bounded_scope",
      "assessment": "本项在固定B/R独立成立；未把原模块历史PASS当证据，未重开旧关闭项，未扩审229。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M02-002 · P3 · REQUIRED — POST请求前表单构造失败与便利包装吞没缺少输入边界

领域 M02；分类 实现信息不足；独立审者 thread `01a12fc9-af72-7672-b6bf-1c6e0d86f1e3`；辅助证据目录 `modules/M02/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/001_Technical/002_Files/003_HTTP_Utilities.rb` · 4-35：键值字符串构造早于宿主调用；仅宿主调用有局部rescue（固定R；blob `70282ef270195b43797e7fd50f0405168e66f56b`）
- `Data/Scripts/001_Technical/002_Files/003_HTTP_Utilities.rb` · 69-83：便利POST捕获整个基础调用的普通异常（固定R；blob `70282ef270195b43797e7fd50f0405168e66f56b`）

**现规格依据**

- `deliverables/final-specification-set/generic-kernel/wp07-diagnostics-files-http.md` · §4.1 L58-65；§6 L95-96：本轮核对的合同定位（固定B；blob `0c86892e62805b19731090eb1dc9bd6a7e4058d8`）
- `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` · IO01-05 L60-64：本轮核对的合同定位（固定B；blob `3c7daba49da60cca2f6051839e408fc0426978a5`）
- `deliverables/final-specification-set/creature-rpg/wp64-mail-and-mystery-gift.md` · §5 L80-82：GET下载解码边界不能覆盖POST请求前构造（固定B；blob `5443a594e4151a268297465206185002fac3d420`）

**参考实际行为**

在已验证Ruby2.6语义下，普通字符串散列表键在原地处理前已冻结，基础POST抛FrozenError且宿主调用0次。使用符号键可隔离该问题：安全ASCII值正常构造并调用宿主；值含空格则编码数值转换抛ArgumentError，仍为0次宿主调用。便利到字符串入口捕获并返回空字符串。HTTPS在上述构造前被前缀门挡下。 源静态事实是构造阶段位于宿主调用的局部捕获之外；FrozenError/ArgumentError等精确异常和返回值只按Ruby2.6隔离回执确认，随附3.1宿主仍未执行。

**现规格的说法**

已有GET/POST×基础/便利表描述协议过滤、响应状态与写文件错误，但没有表单构造过程及其可接受输入/请求前失败。普通异常捕获位置的泛述不能唯一推出哪些正常键值不会发起请求。

**差异/缺口**

部分POST输入失败在网络之前发生，基础异常与便利空串/未发送未被对应到具体前提。

**必要前提**

- 固定原始HTTP文件在Ruby2.6.10p210加载，无网络方法覆写之外的改变
- http://example.invalid/，HTTPLite假方法仅记录参数并返回200/OK
- 字符串键或符号键的普通表单输入；无文件目标

**最小反例**

```json
{
  "input": "http地址，符号键k，值a b；基础POST/便利到字符串分别调用",
  "reference": "基础ArgumentError、HTTP调用0；便利空字符串、HTTP调用0",
  "normal_control": "符号键k，值a_b.-9：正文k=a_b.-9，HTTP调用1，返回OK"
}
```

**正常对照**

符号键与安全ASCII值触达假宿主，Content-Length为8；真实服务器可达性未测。

**失败/边界对照**

字符串键k即使安全值也FrozenError；空格值在符号键对照中ArgumentError；两种便利输入均空串。https地址即使含空格也直接空串，不走构造或网络。

**独立实现影响**

未来实现可能默认所有普通表单都成功发送，或将请求前本地错误当作宿主网络失败，丢失可复查的参考兼容事实与错误传播差别。 影响限定于已定位的工具输入边界；没有默认业务caller证据，不推断所有默认游戏POST均不可用。

**已完成的反证**

```json
{
  "primary_review": {
    "record": "evidence/negative-search.json",
    "search_ids": [
      "post_identity",
      "post_alias"
    ],
    "scope": "全131正式文件",
    "result": "API/媒体类型/表单键词0；宽HTTP/POST搜索63行26文件，POST实质合同只有WP07和IO02，另有IMPOSTER/NO_SIGNPOSTS及引用等假命中。WP64为GET下载/解码，不是POST输入构造。已读这些实质上下文。",
    "source_countercheck": "全脚本pbPost族仅定义及便利转发；未找到覆写或核心默认POST业务。HTTPLite实现不在可读脚本，但失败发生于调用前，不依赖真实网络。"
  },
  "primary_relative_paths_base": "modules/M02",
  "independent_counterevidence": {
    "search_ids": [
      "M02-post",
      "M02-callers-overrides",
      "CA-boundary-supplement"
    ],
    "words": [
      "\\bPOST\\b|pbPost|post_body|表单|FrozenError|冻结.{0,12}键|form-urlencoded|HTTP"
    ],
    "scope": {
      "baseline": "1f36475d22120a0d1175967d5b17d71fe8311d88",
      "root": "deliverables/final-specification-set/",
      "files": 131,
      "includes": "正文、共享条款、数据附表及静态测试目录；并非131篇逐篇重新验收"
    },
    "source_countersearch": [
      {
        "id": "M02-callers-overrides",
        "pattern": "pbTimeEvent|AntiRandom|pbPostData|pbPostToString|pbPostToFile|def pbGetTimeNow|def rand\\b|def self.rand\\b",
        "files": 312
      },
      {
        "id": "CA-boundary-supplement",
        "pattern": "def nil_or_empty\\?|def refresh\\b|def getFacingCoords|def pbGetSeason|on_leave_tile|def gsub!?|def to_s|def sprintf",
        "files": 312
      }
    ],
    "contexts_read_and_assessed": [
      "WP07 §4.1/§6/§7；IO01–05",
      "WP64下载是GET/解码；WP10诊断传播引用不提供POST输入构造"
    ],
    "conclusion": "基础宿主调用局部捕获和便利全调用捕获已承接，但没有请求前表单构造及具体输入边界。不得重复报一个“便利捕获不存在”的问题。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CA"
}
```

**下一轮最小修订**

WP07增列请求前构造阶段、普通输入反例、基础传播与便利空串的差别；明确证据仅Ruby2.6隔离执行且准确游戏宿主未证；不把源码缺陷自动转为未来必须复刻的政策。

**验收标准**

```json
{
  "static": [
    "明确安全对照、字符串键冻结、符号键空格三类输入及宿主调用次数",
    "便利包装的空串不能证明已发出HTTP请求",
    "保留HTTPS提前拒绝和GET既有合同",
    "清楚区分SOURCE_STATIC、隔离EXECUTED_REFERENCE和未执行游戏宿主"
  ],
  "runtime": "不要求联网；可用只记录调用的假宿主复核隔离向量。不得用Ruby2.6回执声称目标宿主实测。"
}
```

**受影响正式文件**

- deliverables/final-specification-set/generic-kernel/wp07-diagnostics-files-http.md
- deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md

**共享合同**

- HTTP基础/便利错误传播
- 诊断边界

**依赖**

- 运行时字符串/键语义
- 表单构造
- 宿主HTTP入口

**能力范围引用**

- GR4-CAP-M02-014

**关联新问题**

无。

**根因身份**

M02-post-pretransport-construction

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "GR3": [],
  "second_round": null,
  "note": "未猜测第二轮ID；不是GR3两已关闭问题的重开。",
  "independent_scope_assessment": {
    "relation": "new_bounded_scope",
    "assessment": "本项在固定B/R独立成立；未把原模块历史PASS当证据，未重开旧关闭项，未扩审229。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- EXECUTED_REFERENCE

**执行状态**

两次隔离运行；evidence/probe-result.json与probe-result-v2.json；无网络/写盘POST/真实宿主

**置信限定**

HIGH for Ruby2.6 isolated result; target host UNVERIFIED

**未知**

- 目标游戏宿主运行时的实测
- 非ASCII全部编码路径
- 调用方是否采用被冻结的字符串键
- 没有默认POST消费者样本
- 随附3.1宿主结果UNVERIFIED；原生HTTP实现、实际服务器、非ASCII、实际POST调用数据形态未证。

**排除的主张**

- 不声称真实线上POST全部不可用
- 不声称GET受相同问题影响
- 不要求新实现保留该缺陷

**用户政策边界**

本轮只需记录参考事实；未来是否修正源异常/保留兼容性留后续用户政策决定，不要求复刻代码。

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CA",
    "thread_id": "01a1301e-5efe-77a2-9450-fc09ff6830c1",
    "path": "modules/CA/verdicts.json",
    "pointer": "/records/3",
    "decision": "CONFIRM_WITH_REFINEMENT",
    "reason": "确认有界输入/失败阶段应补，但降为P3：当前强证是无默认业务caller的工具路径和Ruby2.6隔离结果，不能据此宣称默认宿主POST普遍不可用。现有通用异常分层部分正确；整改应补输入边界并限定版本，而不是重写全部HTTP合同。",
    "required_refinements": [
      "severity由P2收窄为P3。",
      "把请求前构造阶段的SOURCE_STATIC与Ruby2.6精确FrozenError/ArgumentError回执分列；随附3.1运行保持未证。",
      "不把前置构造异常混入已捕获的宿主请求异常；不把空串当已发送证明；不强制未来采用可变字符串或复刻缺陷。"
    ],
    "execution_evidence_assessment": {
      "ca_rerun": false,
      "receipt": "../M02/evidence/probe.rb + probe-v1.rb + probe-result-v2.json",
      "kind": "REUSED_ISOLATED_REFERENCE_EVIDENCE",
      "version": "Ruby 2.6.10p210",
      "assessment": "HTTPLite替身只在构造之后收参数，不能造成零调用的前置失败；原表单构造/便利捕获未改写。精确异常类型仅按回执归Ruby2.6，不提升为随附3.1宿主实测；源码独立支持构造在局部捕获之前。",
      "host_or_demo": "NOT_EXECUTED / bundled Ruby 3.1 host UNVERIFIED",
      "new_execution_claim": false
    },
    "historical_relation_assessment": {
      "relation": "new_bounded_scope",
      "assessment": "本项在固定B/R独立成立；未把原模块历史PASS当证据，未重开旧关闭项，未扩审229。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": {
    "from": "P2",
    "to": "P3",
    "reason": "确认有界输入/失败阶段应补，但降为P3：当前强证是无默认业务caller的工具路径和Ruby2.6隔离结果，不能据此宣称默认宿主POST普遍不可用。现有通用异常分层部分正确；整改应补输入边界并限定版本，而不是重写全部HTTP合同。"
  },
  "formal_revision_applied": false
}
```

### GR4-M02-003 · P3 · REQUIRED — 有状态的偏向未出现值随机选择能力缺少正式合同

领域 M02；分类 缺能力；独立审者 thread `01a12fc9-af72-7672-b6bf-1c6e0d86f1e3`；辅助证据目录 `modules/M02/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/019_Utilities/001_Utilities.rb` · 73-98 / AntiRandom#initialize,#get：公开可调用的有状态整数选择；旧值1/7门与剩余值轮转（固定R；blob `39df7ce43a848625a8596e6bf52692024140af7c`）

**现规格依据**

- `deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md` · §5.1-5.3 L81-107：本轮核对的合同定位（固定B；blob `f293da252a3c344ca6b9c6059bc6e56cd51a5b48`）
- `deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md` · TM05-07 L45-47：本轮核对的合同定位（固定B；blob `3c7daba49da60cca2f6051839e408fc0426978a5`）

**参考实际行为**

正整数规模n建立0至n−1的候选轮次，优先选择本轮尚未出现值。已经出现的值非空时，有1/7分支从这些值再次选择；否则从本轮尚未出现者均匀选择并记为出现。全部出现后，下次选择开始新轮，首抽不走重复门。

**现规格的说法**

WP06只有普通随机、抽样/乱序、显式种子、战斗随机记录；全正式集中的无放回/重复抽样/洗牌均是其他领域规则，没有上述带跨次记忆的1/7重复门。

**差异/缺口**

遗漏一个可由作者或插件直接调用的随机能力；核心未有消费者不构成不存在的证据。

**必要前提**

- 正整数n=2
- 未覆写原始选择能力
- 首抽选择0；第二次重复门命中且旧集合仅0
- 仅静态推导，无实际随机运行

**最小反例**

```json
{
  "input": "正整数n=2；首次返回0后，已见仅0、未见仅1。",
  "reference_conditional_probabilities": {
    "next_0": "1/7",
    "next_1": "6/7"
  },
  "without_replacement_next_0": "0",
  "independent_uniform_next_0": "1/2",
  "reason": "0,0单条允许序列只排除无放回，不能排除独立均匀随机；差异由条件分布说明。",
  "evidence_level": "DERIVED_VECTOR",
  "execution_status": "NOT_EXECUTED"
}
```

**正常对照**

重复门未命中且仍有未出现值时选择未出现者；n=1每轮只可能返回0。

**失败/边界对照**

一轮全部候选出现后，下次以新轮开始；不承诺每n次请求必遍历全集，因为中间可以重复。零/负规模未作为本项验收事实。

**独立实现影响**

仅依据正式规格会丢失作者可使用的防连续偏置能力，或以洗牌/普通均匀抽样替代而改变跨次输出分布。

**已完成的反证**

```json
{
  "primary_review": {
    "record": "evidence/negative-search.json",
    "search_ids": [
      "anti_identity",
      "anti_alias"
    ],
    "scope": "全131正式文件",
    "result": "精确/概念名称0；1/7/七分之一/重复抽样/无放回/洗牌等38行20文件已读，命中为宫殿权重、漫游1/32、遗传无放回、小游戏洗牌、设施重抽，均无此轮次和1/7重复机制。",
    "source_countercheck": "全Data/Scripts搜索AntiRandom仅类定义，无默认消费者或覆写；能力定义仍可直接调用。"
  },
  "primary_relative_paths_base": "modules/M02",
  "independent_counterevidence": {
    "search_ids": [
      "M02-random",
      "M02-callers-overrides"
    ],
    "words": [
      "AntiRandom|防重复|未出现|七分之一|1/7|1／7|随机.{0,12}(轮次|状态|偏向)|无放回|洗牌|重复抽样"
    ],
    "scope": {
      "baseline": "1f36475d22120a0d1175967d5b17d71fe8311d88",
      "root": "deliverables/final-specification-set/",
      "files": 131,
      "includes": "正文、共享条款、数据附表及静态测试目录；并非131篇逐篇重新验收"
    },
    "source_countersearch": [
      {
        "id": "M02-callers-overrides",
        "pattern": "pbTimeEvent|AntiRandom|pbPostData|pbPostToString|pbPostToFile|def pbGetTimeNow|def rand\\b|def self.rand\\b",
        "files": 312
      }
    ],
    "contexts_read_and_assessed": [
      "WP06 §5.1–5.3与TM05–07",
      "WP34无放回继承、拼图/雷板洗牌、设施重复采样、战斗记录/平局洗牌的实质命中均为其它规则"
    ],
    "conclusion": "全131未找到有跨次记忆的1/7重复门。源码只有定义、无默认静态消费者/覆写；可实例化并调用get，不能称默认全局随机服务。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CA"
}
```

**下一轮最小修订**

在WP06以输入整数范围、跨次状态、重复概率、轮次重置和具体向量补一个有界能力条目，注明默认调用未定位；不提出类/容器/API结构。

**验收标准**

```json
{
  "static": [
    "n=2首0后可以再次0且保留未出现1",
    "重复门不命中选择未出现者",
    "耗尽后重开一轮、n=1边界",
    "不把它误写为无放回、每n次全覆盖或默认系统统一使用",
    "用首抽0后P(0)=1/7、P(1)=6/7与无放回0、均匀1/2作条件概率对照；不把一条重复序列当统计证明。"
  ],
  "runtime": "静态验收即可；不要求统计性随机测试或安装动态插件。"
}
```

**受影响正式文件**

- deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md
- deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md

**共享合同**

- 普通随机输入
- 动态作者/插件可调用能力

**依赖**

- 普通整数随机

**能力范围引用**

- GR4-CAP-M02-022

**关联新问题**

无。

**根因身份**

M02-unextracted-stateful-random-selection

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "GR3": [],
  "second_round": null,
  "note": "未猜测第二轮ID；不是GR3两已关闭问题的重开。",
  "independent_scope_assessment": {
    "relation": "new_bounded_scope",
    "assessment": "本项在固定B/R独立成立；未把原模块历史PASS当证据，未重开旧关闭项，未扩审229。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- DERIVED_VECTOR

**执行状态**

NOT_EXECUTED

**置信限定**

HIGH for scoped static algorithm

**未知**

- 实际业务采用情况
- 任意规模/非法输入与宿主分布统计
- 非法规模、真实作者/插件使用、原生随机实现与跨语言序列未证。

**排除的主张**

- 不声称默认游戏已用此能力
- 不要求未来采用参考类组织
- 不证明跨语言随机序列一致

**用户政策边界**

本轮只需记录参考事实；未来是否修正源异常/保留兼容性留后续用户政策决定，不要求复刻代码。

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CA",
    "thread_id": "01a1301e-5efe-77a2-9450-fc09ff6830c1",
    "path": "modules/CA/verdicts.json",
    "pointer": "/records/4",
    "decision": "CONFIRM_WITH_REFINEMENT",
    "reason": "原R中轮次记忆、重复分支与重置构成确实独立的可调用能力，B普通随机/洗牌标题并未承接它；P3合理。确认遗漏，但拒绝用一个允许重复的序列证明与无记忆均匀抽样不同。",
    "required_refinements": [
      "用上列条件概率对照替换不足以区分均匀随机的单序列断言；这是静态数学推导，不是统计测试。",
      "保留正整数n范围、无默认消费者、无跨语言随机序列一致性承诺。"
    ],
    "execution_evidence_assessment": {
      "ca_rerun": false,
      "receipt": "../M02/execution.json",
      "kind": "SOURCE_STATIC / SPEC_STATIC / DERIVED_VECTOR",
      "assessment": "原模块记录的Python清点/JSON/路径校验仅为TOOL_VALIDATION，不支持行为运行通过；CA未执行该脚本或参考函数。",
      "host_or_demo": "NOT_EXECUTED"
    },
    "historical_relation_assessment": {
      "relation": "new_bounded_scope",
      "assessment": "本项在固定B/R独立成立；未把原模块历史PASS当证据，未重开旧关闭项，未扩审229。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M03-001 · P2 · REQUIRED — 范围随机移动只承接了路线让出时机，未承接原始位置边界与单轴规则

领域 M03；分类 缺能力；独立审者 thread `01a12fc9-af72-7402-a6d1-0e3abf8b16e8`；辅助证据目录 `modules/M03/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/004_Game classes/006_Game_Character.rb` · 669–700：范围随机选择有负/零/正三态、原始锚点及UD/LR变体。（固定R；blob `9de49c288ec6c5d8c962b14f1b959ad90ae3d662`）
- `Data/Scripts/004_Game classes/006_Game_Character.rb` · 376–385,539–548,553–565：落位不改原始锚点；脚本调用后按字面让出；选向后普通移动可受阻。（固定R；blob `9de49c288ec6c5d8c962b14f1b959ad90ae3d662`）
- `Data/Scripts/004_Game classes/007_Game_Event.rb` · 9–18：事件原始锚点取地图事件数据。（固定R；blob `aca6d0992927e1d6ce37f08c2cb75e73ebcb7374`）

**现规格依据**

- `deliverables/final-specification-set/engine-overworld/wp12-terrain-movement-vehicles.md` · §4.3 L146–148：只有四正向随机、接近/远离和自主策略。（固定B；blob `177f675ec04ae3d5124dfec69693845e3c0162cc`）
- `deliverables/final-specification-set/engine-overworld/wp13-move-route-matrix.md` · §1 L18；§2 9/45行：只定义三前缀调度，没有两个范围输入的行为。（固定B；blob `b79888af1ce084dc0441b0688661b5c4511f029c`）
- `deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md` · MR08、MR10–15、MR18–21：只测试求值/前缀/推进。（固定B；blob `18382cf43e137a671b245a1dd8d836694e6754ee`）
- `deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md` · L235：跨域命中也只承接同一前缀语义。（固定B；blob `f87c6edf5b09c2ee43b51a514bb7ef81e55e4062`）

**参考实际行为**

以事件建立时的原始位置作锚点。每轴负范围允许该轴两方向，零禁该轴，正范围依当前位置相对原始边界筛方向。对候选等概率只抽一次并尝试普通移动；碰撞不重抽。无候选直接返回。两个单轴变体禁用另一轴；之后移位不自动重定锚点。 对正横界r，左当x>x0−r、右当x<x0+r；对正纵界s，下当y<y0+s、上当y>y0−s。固定参考候选序是左、右、下、上，保留满足门的方向后仅作一次均匀索引选择；此序用于解释固定参考抽样，不规定未来容器或跨语言随机序列。方向选择不预转向，移动成功后的转向沿WP12。

**现规格的说法**

已明确普通四向随机和三种脚本文本前缀的同帧/下帧区别；没有说明这些辅助实际如何限制移动范围。

**差异/缺口**

兼容字面被保留，但实现者仍不能从正式行为合同决定其方向候选、锚点与零/负值语义。

**必要前提**

- 1×1普通地图事件，原始锚点(5,5)，当前(7,5)，无方向固定/强制外部写入；地图内普通地面、所有方向通行。
- 执行范围随机能力，横范围2、纵范围0；固定R无额外覆写。

**最小反例**

```json
{
  "input": "上述状态调用一次范围随机移动。",
  "reference": "唯一候选为左，尝试到(6,5)；右移到(8,5)不会被选。",
  "formal_gap": "四向等概率规则会容许向右/纵移；三前缀条款只能决定何时让出，无法排除这些错误结果。",
  "evidence": "DERIVED_VECTOR; NOT_EXECUTED"
}
```

**正常对照**

从原始(5,5)且当前位置同点，横2/纵0，两横向候选各半；普通通过后位移一格。

**失败/边界对照**

横纵0：没有随机抽取/移动；横2纵0位于右界且左格阻挡：只尝试左、不重抽其它方向；负横范围为不限制该轴。另给事件被落位到范围外的输入，锚点仍原值，不承诺自动钳回。

**独立实现影响**

会把受限游走实现成四向漫游、以当前位置不断重定边界，或受阻后重抽；改变NPC活动范围和随机消费。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-evidence.json",
    "key": "GR4-M03-001",
    "scope_file_count": 131,
    "context_results": [
      "全部131文件按原标识和中文范围/随机/单轴/原始位置别名搜索。",
      "相关命中仅WP13路线§1、MR08/10–15/18–21、WP75 L235；逐读均是调度/求值合同。WP12§4.3普通随机并不定义有界族。",
      "原始位置的其它命中属玩家元数据/储存位置，随机漫游命中属游走宝可梦等别域，不补本规则。",
      "源端仅此一组定义，原始坐标赋值见角色初始化及事件初始化；未定位默认Demo调用，调用能力可由路线45到达。"
    ],
    "source_followup": "固定R所有脚本检索定义、同名覆写及所涉状态读写；追踪下述source anchors的实际入口/消费者；不把缺Demo当不存在。"
  },
  "primary_relative_paths_base": "modules/M03",
  "independent_counterevidence": {
    "search_ids": [
      "M03-range",
      "M03-definitions"
    ],
    "words": [
      "move_random|范围.{0,10}(随机|移动)|随机.{0,15}(范围|单轴|边界)|原始.{0,10}(位置|坐标)|左.{0,5}右.{0,5}下.{0,5}上"
    ],
    "scope": {
      "baseline": "1f36475d22120a0d1175967d5b17d71fe8311d88",
      "root": "deliverables/final-specification-set/",
      "files": 131,
      "includes": "正文、共享条款、数据附表及静态测试目录；并非131篇逐篇重新验收"
    },
    "source_countersearch": [
      {
        "id": "M03-definitions",
        "pattern": "move_random_range|move_random_UD|move_random_LR|original_x|original_y|surf_base_coords|ending_surf|def command_116|def pbEraseThisEvent|def addErasedEvent|def pbCancelVehicles|def transfer_player",
        "files": 312
      }
    ],
    "contexts_read_and_assessed": [
      "WP12 §4.3已给普通随机不预转向/成功后转向",
      "路线§1/45、MR08/10–22、WP75 §8.6均只给脚本文本调度；不是范围候选算法"
    ],
    "conclusion": "候选过滤/原始锚点/单轴能力未承接；阻挡时不预转向和通用移动应引用现有合同，不另计缺失。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CA"
}
```

**下一轮最小修订**

在WP12或WP13正文补实现无关的范围随机规则，路线矩阵引用该合同；加边界/空候选/受阻/落位后锚点对照。不得把源方法或类结构当未来API。

**验收标准**

```json
[
  "静态：分别列横纵负/零/正语义、原始锚点生命周期、候选等概率及一次尝试不重抽。",
  "静态：区分UD/LR单轴与普通四向；保留既有前缀调度，不把移动成败当推进门。",
  "静态向量：原始(5,5)/当前(7,5)/横2纵0、双0、左阻挡、当前位置移出原范围；均标NOT_EXECUTED。",
  "运行：本修订不以宿主执行为前置；将来动态验证需要合法地图夹具与真实随机控制，不能以文档/JSON校验充数。",
  {
    "kind": "SPEC_STATIC",
    "criterion": "写出严格比较式和固定参考候选序，并区分方向过滤/越界钳回；受阻不重抽、不预转向的行为引用已有WP12合同。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/engine-overworld/wp12-terrain-movement-vehicles.md
- deliverables/final-specification-set/engine-overworld/wp13-move-route-matrix.md
- deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md
- deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md

**共享合同**

- WP11地图状态/转移
- WP12运动与通行
- WP13事件/路线及测试目录

**依赖**

- 有效地图/事件夹具
- 固定参考默认定义，无插件覆写
- 普通调用和指定更新机会

**能力范围引用**

- GR4-CAP-M03-011
- GR4-CAP-M03-012

**关联新问题**

无。

**根因身份**

GR4-M03-001

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "third_round": null,
  "second_round": null,
  "note": "未知第二轮关联不猜ID；旧CLOSED身份不修改。",
  "independent_scope_assessment": {
    "relation": "new_bounded_scope",
    "assessment": "本项在固定B/R独立成立；未把原模块历史PASS当证据，未重开旧关闭项，未扩审229。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- DERIVED_VECTOR

**执行状态**

NOT_EXECUTED

**置信限定**

HIGH_STATIC_WITH_STATED_PRECONDITIONS

**未知**

- 实际Demo使用/事件可达性未知；宿主和媒体结果未执行。
- 默认Demo调用未证；源路线45可调用不等于真实NPC素材/事件链已运行；任意非整数/非法范围未穷尽。

**排除的主张**

- 不要求修参考、不实现框架或保留源API/结构。
- 不宣称全部本域或全套规格均已审。

**用户政策边界**

无需决定是否补事实；若未来实现选择不同兼容政策，应另阶段明确，不由本审者代定。

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CA",
    "thread_id": "01a1301e-5efe-77a2-9450-fc09ff6830c1",
    "path": "modules/CA/verdicts.json",
    "pointer": "/records/5",
    "decision": "CONFIRM_WITH_REFINEMENT",
    "reason": "ROOT候选序及严格比较经原函数独立核对正确。源选向后调用普通不预转向移动，受阻不重抽；原始锚点独立于当前位置。既有路线前缀只决定让出，不足以决定范围边界。",
    "required_refinements": [
      "补一般比较式、负/零/正三态、UD/LR禁用另一轴；说明是方向过滤而非越界自动钳回。",
      "候选序只用于固定参考抽样索引解释，不要求未来保留源容器结构或跨语言随机序列。",
      "将不预转向/成功转向引用WP12既有规则，不新增重复根因；WP75的正确调度无需重写。"
    ],
    "execution_evidence_assessment": {
      "ca_rerun": false,
      "receipt": "../M03/execution.json",
      "kind": "SOURCE_STATIC / SPEC_STATIC / DERIVED_VECTOR",
      "assessment": "原模块记录的Python清点/JSON/路径校验仅为TOOL_VALIDATION，不支持行为运行通过；CA未执行该脚本或参考函数。",
      "host_or_demo": "NOT_EXECUTED"
    },
    "historical_relation_assessment": {
      "relation": "new_bounded_scope",
      "assessment": "本项在固定B/R独立成立；未把原模块历史PASS当证据，未重开旧关闭项，未扩审229。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M03-002 · P2 · REQUIRED — WP59声称转移重置冲浪临时残留，但转移链没有该清理

领域 M03；分类 状态或时序错误；独立审者 thread `01a12fc9-af72-7402-a6d1-0e3abf8b16e8`；辅助证据目录 `modules/M03/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb` · 705–751：上水先写底座后前跳；清理位于有底座的玩家步后通知。（固定R；blob `841e0c66cce7bbb34c07d4991f952d31a27cc469`）
- `Data/Scripts/004_Game classes/006_Game_Character.rb` · 767–799：跳跃落点拒绝不启动运动，前跳返回false。（固定R；blob `9de49c288ec6c5d8c962b14f1b959ad90ae3d662`）
- `Data/Scripts/003_Game processing/002_Scene_Map.rb` · 72–101,121–133,165–175：转移及正常201消费者；没有两个临时字段写入。（固定R；blob `8be1640f36b293f44329a3bbe6ccf3e13fb0d825`）
- `Data/Scripts/004_Game classes/008_Game_Player.rb` · 64–100,262–266,575–592：实际覆写/载具更新也不清底座或结束标志。（固定R；blob `8f49870b94fdda6dbb53cbaeebfaf458498cd02d`）
- `Data/Scripts/005_Sprites/005_Sprite_SurfBase.rb` · 44–79：保游泳且底座非空时，显示输入仍取底座。（固定R；blob `323f35ce4438cd140f34bb669c0bb8cf91a80858`）
- `Data/Scripts/003_Game processing/003_Interpreter.rb` · 116–123：结束冲浪标志另为解释器等待门。（固定R；blob `21666002e7f4038dd3763b632538becaae5f8d7d`）

**现规格依据**

- `deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md` · §7 L296：明确写中断（如转移）时残留按转移流程重置。（固定B；blob `a2bda5c3e0d5b967d8ef050bc36b4cac8ed8c420`）
- `deliverables/final-specification-set/engine-overworld/wp12-terrain-movement-vehicles.md` · §5.2 L169–171：上水失败无回滚、步后清理三门已有准确限定。（固定B；blob `177f675ec04ae3d5124dfec69693845e3c0162cc`）
- `deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md` · §4 L59–71：列明取消载具/落位流程，无补充临时残留清理。（固定B；blob `7482ac4dc1bdf3720a3d6d5c5c1c8b2a38e12f0d`）
- `deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md` · MV05、WT19及MP显式传送族：没有失败上水后无步通知转移的对照。（固定B；blob `18382cf43e137a671b245a1dd8d836694e6754ee`）

**参考实际行为**

默认转移入口和载具取消都不清surf_base_coords/ending_surf；这些临时量不能由转移本身保证重置。清底座需地图场景、玩家通知、有底座；结束标志又要为真才清。无此通知前的转移返回可保留残留。

**现规格的说法**

WP59§7给了转移重置保证，同时WP12/WP61把清理正确绑定玩家步后通知；WP11被引用但无此重置。

**差异/缺口**

把后续有条件的收尾写成转移本身的无条件保证。

**必要前提**

- 合法20×20同图，玩家初始静止(5,5)、向右，无冰瀑/强制移动/跟随者；无其它字段改写。
- 直接上水入口前跳(6,5)因具名非through阻挡事件拒绝；相关资源调用正常，故surfing=true、底座(6,5)，未启动跳跃。
- 随后正常201转同图(10,10)、方向右，由场景按false保游泳；没有完成步或额外步后通知、无执行移动的其它事件/公共事件；所有宿主调用正常。
- 玩家through=false，无调试Ctrl穿透；ending_surf初始false。失败跳跃不启动运动计时，初始无未完成运动/步后通知。

**最小反例**

```json
{
  "input": "上述失败上水后的同图201保游泳传送，观察转移正常返回。",
  "reference": "玩家到(10,10)，surfing仍真，底座仍(6,5)；显示选择仍读旧底座，不自动跟玩家新位置。",
  "formal": "按WP59残留重置一句会预期底座已清、显示跟随玩家。",
  "evidence": "DERIVED_VECTOR; NOT_EXECUTED；只断言状态和显示输入，不声称可见像素"
}
```

**正常对照**

成功上水跳跃完成，满足玩家步后通知三门时清底座；成功上岸且结束标记真才额外取消载具/重置遭遇/音乐并清标记。

**失败/边界对照**

取消游泳参数true只清冲浪/潜水标志，未独立清临时底座/结束字段；后继合格步通知仍可能清理。人为ending_surf=true只用于直接转移与等待门的条件事实：正常事件201会先受解释器等待门阻止，不能用它证明该人工状态可越门，也不宣称默认流程必软锁。

**独立实现影响**

独立实现可能在每次传送额外清临时量，掩盖失败上水残留，并错误解除结束冲浪等待；状态与显示输入、继续时机可能与R不同。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-evidence.json",
    "key": "GR4-M03-002",
    "scope_file_count": 131,
    "context_results": [
      "全部131文件检索两个字段、底座/基点、残留/中断、载具取消/取消游泳。",
      "WP12§5.2和WP61§3.2只给步后门；WP11显式/边缘入口无临时量清理。测试MV05/WT19只正常收尾，不能证明转移重置。",
      "源端全脚本检索：底座清空只在field 743，结束标志清假为临时状态初始化与field 749；转移、玩家moveto覆写、载具类型设置、同图显示重建均未清。",
      "正常上岸后可能后续步后通知清理，所以反例明确无完成步通知；不把所有转移都说成一定永远残留。"
    ],
    "source_followup": "固定R所有脚本检索定义、同名覆写及所涉状态读写；追踪下述source anchors的实际入口/消费者；不把缺Demo当不存在。"
  },
  "primary_relative_paths_base": "modules/M03",
  "independent_counterevidence": {
    "search_ids": [
      "M03-surf",
      "M03-definitions",
      "CA-shared-alias-supplement",
      "CA-boundary-supplement"
    ],
    "words": [
      "surf_base_coords|ending_surf|冲浪.{0,20}(残留|中断|重置|收尾)|底座|基底|取消游泳|玩家步后",
      "过渡坐标|冲浪基点|冲浪.{0,8}清|动态形态查询|资源消费.{0,15}形态|形态.{0,15}副作用|计时.{0,10}变量|变量.{0,10}计时|PP.{0,20}(补给|补充|活体|存活)|翻译.{0,10}(重复|合并)|文本域.{0,10}(覆盖|冲突)"
    ],
    "scope": {
      "baseline": "1f36475d22120a0d1175967d5b17d71fe8311d88",
      "root": "deliverables/final-specification-set/",
      "files": 131,
      "includes": "正文、共享条款、数据附表及静态测试目录；并非131篇逐篇重新验收"
    },
    "source_countersearch": [
      {
        "id": "M03-definitions",
        "pattern": "move_random_range|move_random_UD|move_random_LR|original_x|original_y|surf_base_coords|ending_surf|def command_116|def pbEraseThisEvent|def addErasedEvent|def pbCancelVehicles|def transfer_player",
        "files": 312
      },
      {
        "id": "CA-boundary-supplement",
        "pattern": "def nil_or_empty\\?|def refresh\\b|def getFacingCoords|def pbGetSeason|on_leave_tile|def gsub!?|def to_s|def sprintf",
        "files": 312
      }
    ],
    "contexts_read_and_assessed": [
      "WP59 §7转移重置保证",
      "WP12 §5.2/ WP61 §3.2只保证玩家步后通知清理",
      "WP11同图转移、MP20/21与WP16 §4.3/B04-W07分别是车辆标记与显示消费，不提供临时坐标清理"
    ],
    "conclusion": "固定源字段写点没有转移独立清理；已有正确步后/显示合同不能使WP59的无条件转移重置句成立。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CA"
}
```

**下一轮最小修订**

将WP59保证更正为入口/消费者分层，明确传送不提供两临时量的独立清理保证；WP11/12引用统一；补失败上水→同图保游泳转移及正常步后清理对照。固定异常事实与未来是否主动清理的政策分开。

**验收标准**

```json
[
  "静态：分别说明surfing/diving、底座和结束标志，不把载具取消等同全部临时状态重置。",
  "静态：给出无步通知转移返回的观察点与后续步后门，不能声称永久卡死或默认Demo可达。",
  "静态向量：上述(5,5)失败跳→(10,10)转移保底座；对照成功完成步清底座；标NOT_EXECUTED。",
  "运行：真实可视位置/继续时机需宿主地图及资源；不要求本轮补造运行证据。",
  {
    "kind": "SPEC_STATIC",
    "criterion": "反例明确through=false、无Ctrl穿透、ending_surf=false、未启动运动计时；直接转移、正常201与步后清理分层。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md
- deliverables/final-specification-set/engine-overworld/wp12-terrain-movement-vehicles.md
- deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md
- deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md

**共享合同**

- WP11转移
- WP12冲浪提交/步后收尾
- WP61步后通知
- WP16/M10冲浪显示输入

**依赖**

- 有效地图/事件夹具
- 固定参考默认定义，无插件覆写
- 普通调用和指定更新机会

**能力范围引用**

- GR4-CAP-M03-002
- GR4-CAP-M03-003
- GR4-CAP-M03-007

**关联新问题**

无。

**根因身份**

GR4-M03-002

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "third_round": null,
  "second_round": null,
  "note": "未知第二轮关联不猜ID；旧CLOSED身份不修改。",
  "independent_scope_assessment": {
    "relation": "producer_cleanup_vs_existing_display_consumer",
    "ids": [
      "GIR-FD82-C064"
    ],
    "assessment": "已读旧qualified_scope及B WP16/B04-W07。C064的基点已清稳定冲浪/visible与opacity是显示消费者；新项质疑临时量何时清，不改旧显示合同，关系准确。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- DERIVED_VECTOR

**执行状态**

NOT_EXECUTED

**置信限定**

HIGH_STATIC_WITH_STATED_PRECONDITIONS

**未知**

- 实际Demo使用/事件可达性未知；宿主和媒体结果未执行。
- 完整宿主像素、真实Demo上水/转移链、外部脚本改写和所有转移组合未运行。

**排除的主张**

- 不要求修参考、不实现框架或保留源API/结构。
- 不宣称全部本域或全套规格均已审。

**用户政策边界**

无需决定是否补事实；若未来实现选择不同兼容政策，应另阶段明确，不由本审者代定。

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CA",
    "thread_id": "01a1301e-5efe-77a2-9450-fc09ff6830c1",
    "path": "modules/CA/verdicts.json",
    "pointer": "/records/6",
    "decision": "CONFIRM_WITH_REFINEMENT",
    "reason": "源码追至玩家jump覆写、普通更新、转移moveto、显示重建与步后通知，失败跳跃没有进入update_move，转移也不单独生成清理通知。WP59多给了一项保证；报告需保持有界条件与观察点，不能推广成默认软锁。",
    "required_refinements": [
      "将玩家through=false、无调试Ctrl穿透、ending_surf=false及未启动运动计时写成反例前提。",
      "区分正常201保游泳、直接默认转移取消游泳及步后通知清理；保留显示输入与真实像素未证的区别。",
      "人工ending_surf=true仅作直接转移/等待门的条件事实，不能称正常201可穿过该等待门。"
    ],
    "execution_evidence_assessment": {
      "ca_rerun": false,
      "receipt": "../M03/execution.json",
      "kind": "SOURCE_STATIC / SPEC_STATIC / DERIVED_VECTOR",
      "assessment": "原模块记录的Python清点/JSON/路径校验仅为TOOL_VALIDATION，不支持行为运行通过；CA未执行该脚本或参考函数。",
      "host_or_demo": "NOT_EXECUTED"
    },
    "historical_relation_assessment": {
      "relation": "producer_cleanup_vs_existing_display_consumer",
      "ids": [
        "GIR-FD82-C064"
      ],
      "assessment": "已读旧qualified_scope及B WP16/B04-W07。C064的基点已清稳定冲浪/visible与opacity是显示消费者；新项质疑临时量何时清，不改旧显示合同，关系准确。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M03-003 · P2 · REQUIRED — 事件命令116的消去记录写入及让出规则未承接，三入口对照含混

领域 M03；分类 实现信息不足；独立审者 thread `01a12fc9-af72-7402-a6d1-0e3abf8b16e8`；辅助证据目录 `modules/M03/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/003_Game processing/004_Interpreter_Commands.rb` · 11–35,502–509：分派116：正事件ID先安全消去再登记；即使缺实例仍登记；本条索引+1、false让出。（固定R；blob `58167231199f1cb8bdc499a61f5ada544d3f7616`）
- `Data/Scripts/004_Game classes/007_Game_Event.rb` · 46–49：普通erase只改实例/刷新。（固定R；blob `aca6d0992927e1d6ce37f08c2cb75e73ebcb7374`）
- `Data/Scripts/003_Game processing/003_Interpreter.rb` · 84–135,292–300：false中断本轮；记录式辅助另有事件存在门。（固定R；blob `21666002e7f4038dd3763b632538becaae5f8d7d`）
- `Data/Scripts/012_Overworld/002_Overworld_Metadata.rb` · 154–168：登记取当前地图，不检查实例存在。（固定R；blob `148211a6c6f94ed0219134f52dcfff817e6bd0fd`）

**现规格依据**

- `deliverables/final-specification-set/engine-overworld/wp13-interpreter-command-matrix.md` · 116行 L37：只描述当前事件被删除和刷新，没有控制结果/局部记录门。（固定B；blob `bfff8453529890f2ea6e7d00ed9b7e1033da0130`）
- `deliverables/final-specification-set/engine-overworld/wp13-map-events-npc-followers.md` · §3.3 L50：辅助有存在门后，将一般实例消去/116并列为不能自动视为同一记录操作。（固定B；blob `6c8046fb3691e6208b588c9090fb85dc7ea4ead4`）
- `deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md` · GR3-MR12 L490：输入将普通实例消去/116并列，预期只有普通实例不登记，没有116明确输出。（固定B；blob `18382cf43e137a671b245a1dd8d836694e6754ee`）
- `deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md` · §6.2 L120：记录式入口概要引用WP13，不补116差别。（固定B；blob `7482ac4dc1bdf3720a3d6d5c5c1c8b2a38e12f0d`）

**参考实际行为**

三个入口有不同合同：普通实例消去不记录；记录式脚本辅助只在当前事件存在时消去并记录；命令116只以事件ID>0为登记门，缺实例可安全跳过消去但仍登记当前图/ID真。116无论ID是否正都推进一项并停止本轮，后条待下一解释器更新机会。

**现规格的说法**

记录式辅助与普通实例的区别已覆盖，但116仅一行粗述，并与一般实例消去在正文/向量中并列；未明确其正ID登记、缺实例登记以及推进让出。

**差异/缺口**

这不是断言规格逐字写了“116绝不登记”；问题是正式三入口对照无法独立推导116的真实生产端和继续时机。 通用“假结果停止当前更新”的调度合同已经存在；只缺116本身选择这一控制结果并在内部推进一项的具名绑定，不另报通用解释器算法缺失。

**必要前提**

- 当前图B、局部记录对象存在，记录表空；解释器绑定事件ID7；合法命令列表中116后还有一条可观察全局开关命令；无其它写入。
- 正常例B中有事件7；边界例只改为B中没有事件7，解释器ID仍正。
- 主解释器记录的地图与当前地图相同，无消息/移动/冲浪等等待门；116不是终止项，后续全局开关命令之后还有正常终止项。

**最小反例**

```json
{
  "input": "边界例在一次解释器更新机会执行116。",
  "reference": "实例消去安全跳过，但(B,7)消去记录为真；索引指向后条且本次不执行后条开关。",
  "formal_gap": "若套记录式辅助缺事件不登记或普通实例不登记，将得到空记录；矩阵没有后条延后判据。",
  "evidence": "DERIVED_VECTOR; NOT_EXECUTED"
}
```

**正常对照**

B中事件7存在：消去/刷新实例，登记(B,7)真，然后推进一项并本轮停止。与直接实例消去不登记作对照。

**失败/边界对照**

ID0：不消去、不登记，仍推进/停止本轮。正ID缺实例：仍登记；局部记录对象为空时安全跳过登记。不借此承诺正常读档还原旧表，进入通知先清记录仍成立。

**独立实现影响**

独立事件兼容实现可能漏记录、把缺实例门套错，或立即连跑116后的全局命令；影响局部状态和当次更新顺序。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-evidence.json",
    "key": "GR4-M03-003",
    "scope_file_count": 131,
    "context_results": [
      "全131文件检索116/删除事件/消去记录/erasedEvents/pbEraseThisEvent及消去-登记别名。",
      "只有WP13矩阵116、WP13§3.3、WP11§6.2和GR3-MR12相关。另116为战斗评分数值和调试目录E116，不是事件命令。",
      "逐读上述及恢复端MR01–13：说明正常读档清表和辅助恢复，不能代替116生产端。",
      "源端command_116仅一处定义且直接主分派可达；addErasedEvent无实例门；Game_Event.erase和脚本辅助的门分别追踪。"
    ],
    "source_followup": "固定R所有脚本检索定义、同名覆写及所涉状态读写；追踪下述source anchors的实际入口/消费者；不把缺Demo当不存在。"
  },
  "primary_relative_paths_base": "modules/M03",
  "independent_counterevidence": {
    "search_ids": [
      "M03-erase",
      "M03-definitions"
    ],
    "words": [
      "\\b116\\b|pbEraseThisEvent|erasedEvents|消去|删除事件|本轮停止"
    ],
    "scope": {
      "baseline": "1f36475d22120a0d1175967d5b17d71fe8311d88",
      "root": "deliverables/final-specification-set/",
      "files": 131,
      "includes": "正文、共享条款、数据附表及静态测试目录；并非131篇逐篇重新验收"
    },
    "source_countersearch": [
      {
        "id": "M03-definitions",
        "pattern": "move_random_range|move_random_UD|move_random_LR|original_x|original_y|surf_base_coords|ending_surf|def command_116|def pbEraseThisEvent|def addErasedEvent|def pbCancelVehicles|def transfer_player",
        "files": 312
      }
    ],
    "contexts_read_and_assessed": [
      "WP13 §4.1和矩阵§2已有false本轮停止规则",
      "矩阵116缺其具体返回/推进；WP13 §3.3及GR3-MR12只确定辅助与普通实例两者区别",
      "WP11/09恢复端不提供116登记门"
    ],
    "conclusion": "不能把已有通用停止/推进说成全局缺失；缺的是116与这条规则的绑定，以及正ID而非实例存在的登记门。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CA"
}
```

**下一轮最小修订**

明确三入口表，修116矩阵的状态/缺事件/推进列，拆分GR3-MR12中的普通实例和116预期，并补正ID缺实例/ID0反向向量；保留读档先清表及历史CLOSED身份。

**验收标准**

```json
[
  "静态：三入口分别写是否登记及门；116正ID缺实例仍登记。",
  "静态：116索引推进一项并停止本轮，下一更新才尝试后条；不把返回false写成业务失败。",
  "静态向量：有实例、缺实例、ID0；局部记录为空可单独限定；后条开关作观察点，全部NOT_EXECUTED。",
  "历史：GR3-M03-004已关闭记录不改；按新增116消费者审查范围登记new_scope_same_root，不给旧全项重新签名。",
  {
    "kind": "SPEC_STATIC",
    "criterion": "只补116的具名推进/让出结果，复用已有通用调度；后条在下一次解释器更新机会尝试，不硬说下一渲染帧。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/engine-overworld/wp13-interpreter-command-matrix.md
- deliverables/final-specification-set/engine-overworld/wp13-map-events-npc-followers.md
- deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md
- deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md

**共享合同**

- WP11地图状态/转移
- WP12运动与通行
- WP13事件/路线及测试目录

**依赖**

- 有效地图/事件夹具
- 固定参考默认定义，无插件覆写
- 普通调用和指定更新机会

**能力范围引用**

- GR4-CAP-M03-009
- GR4-CAP-M03-010
- GR4-CAP-M03-024

**关联新问题**

无。

**根因身份**

GR4-M03-003

**旧GR3/229/341关系**

```json
{
  "relation": "new_scope_same_root",
  "third_round": "GR3-M03-004",
  "second_round": null,
  "note": "未知第二轮关联不猜ID；旧CLOSED身份不修改。",
  "independent_scope_assessment": {
    "relation": "new_scope_same_root",
    "ids": [
      "GR3-M03-004"
    ],
    "assessment": "B当前已标该历史条款并承接辅助/恢复部分；本项补主分派116生产端。保留旧关闭身份，不宣称旧全项重验，不与它简单MERGE而丢失新入口缺口。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- DERIVED_VECTOR

**执行状态**

NOT_EXECUTED

**置信限定**

HIGH_STATIC_WITH_STATED_PRECONDITIONS

**未知**

- 实际Demo使用/事件可达性未知；宿主和媒体结果未执行。
- 真实Demo安排、并行解释器销毁后的继续、宿主更新时机未运行；本例限定主解释器。

**排除的主张**

- 不要求修参考、不实现框架或保留源API/结构。
- 不宣称全部本域或全套规格均已审。

**用户政策边界**

无需决定是否补事实；若未来实现选择不同兼容政策，应另阶段明确，不由本审者代定。

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CA",
    "thread_id": "01a1301e-5efe-77a2-9450-fc09ff6830c1",
    "path": "modules/CA/verdicts.json",
    "pointer": "/records/7",
    "decision": "CONFIRM_WITH_REFINEMENT",
    "reason": "116的真实分派、实例安全消去和记录函数分别核实；当前正式三入口对照无法唯一推出其结果。通用false停止规则存在但116行没有给出它返回false及命令体自推进，所以仍需有界修正。",
    "required_refinements": [
      "明确解释器地图=当前图、无等待门及116不在终止项位置的夹具。",
      "以通用推进合同已有为前提，只补116具体控制结果，不重复报通用算法缺失。",
      "三入口分别列门；保持旧恢复清表合同与历史关闭状态。"
    ],
    "execution_evidence_assessment": {
      "ca_rerun": false,
      "receipt": "../M03/execution.json",
      "kind": "SOURCE_STATIC / SPEC_STATIC / DERIVED_VECTOR",
      "assessment": "原模块记录的Python清点/JSON/路径校验仅为TOOL_VALIDATION，不支持行为运行通过；CA未执行该脚本或参考函数。",
      "host_or_demo": "NOT_EXECUTED"
    },
    "historical_relation_assessment": {
      "relation": "new_scope_same_root",
      "ids": [
        "GR3-M03-004"
      ],
      "assessment": "B当前已标该历史条款并承接辅助/恢复部分；本项补主分派116生产端。保留旧关闭身份，不宣称旧全项重验，不与它简单MERGE而丢失新入口缺口。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M04-001 · P2 · REQUIRED — 按个体取图会求值动态形态，WP18却将图像归为简化形态读取

领域 M04；分类 状态或时序错误；独立审者 thread `01a12fdc-618e-7ea1-be11-c267b26fdb3d`；辅助证据目录 `modules/M04/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/010_Data/002_PBS data/009_Species_files.rb` · 92–109;123–124：个体正/背精灵及图标在选择资源前读取动态形态（固定R；blob `2a2e2fb92e7c05ec3b2f586edfda64cd4eeeaba3`）
- `Data/Scripts/014_Pokemon/001_Pokemon.rb` · 113–115;147–165：物种记录用简化读取；动态读取则可提交变化（固定R；blob `55e7e42c93cc8c0ae91f8594e7a7b9560eb9c22f`）
- `Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb` · 422–431：FURFROU超5天或缺时间戳回0，提交0清时间戳（固定R；blob `d643bcc5fc09d233880174bb2b7004c843d224ac`）
- `Data/Scripts/014_Pokemon/001_Pokemon-related/003_Pokemon_Sprites.rb` · 49–60;124–134：精灵和图标入口调用上述个体取图（固定R；blob `12da4a054e9cd244039c75e3b427153a676d4c0c`）
- `Data/Scripts/016_UI/006_UI_Summary.rb` · 117–134：摘要构造包含该精灵/图标调用链（固定R；blob `8a7dff8b8b0d41a4fb9a405ea726fa06365b6e9b`）
- `PBS/pokemon_forms.txt` · 1635–1661;FURFROU,1…9：默认剪毛形态数据存在；不证明图像资源存在（固定R；blob `08ae264e420484e31a81087eb3125d6f0c7fdaf6`）

**现规格依据**

- `deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md` · §3.4;149–151：普通form/简化form差异正确，但把图像列为简化读取例子（固定B；blob `cb30c0f4a1199b78b860ed513956eedd40c2c970`）
- `deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md` · §4.1;48–50：只说按个体形态取图，未指定动态/简化入口（固定B；blob `23c487115d8b01638ed2db062546ef2a58abdc9f`）
- `deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md` · §3.2-R03;157–163;§3.4;179–180：图像读取副作用一般声明与限时条件分别存在（固定B；blob `a11179facf0ff7822386945aca30aa8a9767528c`）
- `deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md` · FM07;U03-SP07–10：未连接到期形态与个体取图边界（固定B；blob `50086b77a48a2714af17cd8c86174d271397a942`）
- `deliverables/final-specification-set/creature-rpg/wp35-eggs-and-hatching.md` · §5.2/§9；99–122,158–169：已准确承接孵化核心与演出动态读取，必须保留的强反证。（固定B；blob `64308f9d5b6f13f71ac9d2fa408a143e0db8b6ca`）
- `deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md` · EG-13/EG-20；21–32,75：动态孵化对照已有承接，不重新报缺失。（固定B；blob `bb775bf94bd77dd3ff88d587ea093a6ec00076d5`）

**参考实际行为**

按个体取得精灵/图标时先求值普通动态形态；有forced则用forced，战斗/仓库中用存储值，否则动态候选不同会经完整形态提交，再以所得形态选资源。物种记录的基础能力读取用简化形态，两者不能合并。

**现规格的说法**

WP18 §3.4把“图像”列为简化形态读取消费者，属于明确的过宽分类。WP21已有动态读取/提交与守卫；WP35 §5.2/§9及EG-13/20还明确承接孵化演出先读动态形态的副作用。这些是实质反证和已正确部分，但不能消解WP18相反泛称；本项限于入口归属及跨文档一致性。

**差异/缺口**

混淆内容记录读取与按个体取图。会遗漏取图触发的限时形态回退、时间戳清理和完整提交副作用；不仅影响所选图像，也影响个体状态。

**必要前提**

- 合法非蛋FURFROU，存储形态1，forced为空，time_form_set=t
- 普通世界状态in_battle=false、in_storage=false；当前时刻t+432001秒，期间未先读动态形态
- 有效物种/形态和运行状态对象、无插件改写；直接按个体取图到达形态求值；若讨论摘要入口，前序界面资源/构造正常
- 若比较画面，另需不同形态资源存在；状态差异本身不依赖真实位图已显示
- 时间戳t为整数秒；物种资料、能力重算和图鉴依赖正常。显式参数对照先给定数值，不能以低层纯消费反推整条调用链纯读。

**最小反例**

```json
{
  "input": "同上，仅调用一次按个体取正面精灵入口。",
  "reference_static_result": "在资源查找前形态从1提交到0，time_form_set清空；清特性缓存、重算并条件图鉴登记，然后按形态0查图。",
  "result_if_following_incorrect_clause": "简化读取返回1；不触发到期判断/提交，时间戳仍t，按形态1查图。",
  "evidence_level": "DERIVED_VECTOR",
  "execution_status": "NOT_EXECUTED"
}
```

**正常对照**

整数t恰加432000秒不回退。低层按显式物种/形态取图只消费已求值的数值参数；若上游为获得参数先读个体动态形态，调用链仍可能有副作用，孵化即有已承接对照。

**失败/边界对照**

战斗/仓库为真或forced=1时，个体取图同样先走普通形态读取，但其守卫阻止动态回退；forced=0则返回0而不改存储1。无匹配资源时可取不到位图，之前已发生的形态求值/提交不因此成为简化读取或回滚。实际宿主失败和像素未知。

**独立实现影响**

按WP18实现无副作用的图像形态快照，会延迟或遗漏到期回退，并与普通形态查询、图鉴登记、后续能力/界面状态不一致。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-evidence-search.json",
    "corpus": "deliverables/final-specification-set",
    "file_count": 131,
    "queries": [
      "form_simple|简化形态",
      "取图|图像.*读取|个体.*图像|按个体",
      "FURFROU|HOOPA|限时形态|5 天|五天",
      "动态形态|读取副作用"
    ],
    "source_rebuttal": "全Scripts检索def form/def form_simple及个体取图定义；个体实现仅主Pokemon文件，Sprite里的form=是另一个类而非个体覆写。确认普通精灵、图标及摘要调用。",
    "conclusion": "不是缺少动态形态模块；是已存在的具体消费者分类错误。SPINDA纯像素数学与本项独立。"
  },
  "primary_relative_paths_base": "modules/M04",
  "independent_counterevidence": {
    "search_ids": [
      "M04-form",
      "M04-form-overrides",
      "CA-shared-alias-supplement"
    ],
    "words": [
      "form_simple|简化形态|取图|图像.{0,12}(读取|形态|副作用)|FURFROU|限时形态|五天|5 天",
      "过渡坐标|冲浪基点|冲浪.{0,8}清|动态形态查询|资源消费.{0,15}形态|形态.{0,15}副作用|计时.{0,10}变量|变量.{0,10}计时|PP.{0,20}(补给|补充|活体|存活)|翻译.{0,10}(重复|合并)|文本域.{0,10}(覆盖|冲突)"
    ],
    "scope": {
      "baseline": "1f36475d22120a0d1175967d5b17d71fe8311d88",
      "root": "deliverables/final-specification-set/",
      "files": 131,
      "includes": "正文、共享条款、数据附表及静态测试目录；并非131篇逐篇重新验收"
    },
    "source_countersearch": [
      {
        "id": "M04-form-overrides",
        "pattern": "def (self\\.)?(form\\b|form_simple\\b|sprite_bitmap_from_pokemon|icon_filename_from_pokemon|icon_bitmap_from_pokemon)|FURFROU|DEERLING|def pbHatch",
        "files": 312
      }
    ],
    "contexts_read_and_assessed": [
      "WP18 §3.4明确把图像归简化读取",
      "WP21 §3.2-R03已保留读取副作用、FM07/08已给限时回退",
      "强反证：WP35 §5.2/§9和EG-13/20已有孵化资源动态读写的明确合同"
    ],
    "conclusion": "不能声称正式集完全没有图像动态读取副作用；WP35已有具体承接。它与WP18泛称形成矛盾，仍不能让按个体正背精灵/图标的入口归属无歧义。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CA"
}
```

**下一轮最小修订**

最低修订是纠正WP18的图像泛称，并明确按个体精灵/图标入口继承普通动态读取合同；WP15/21按需要对齐引用，复用已正确的WP21/35提交与守卫。增具名静态对照，不重建动态形态整域，不修改WP35正确规则。

**验收标准**

```json
[
  {
    "kind": "STATIC",
    "criterion": "只凭正式集可区分物种内容记录读取与按个体精灵/图标取图；不再声称图像统一用简化形态。"
  },
  {
    "kind": "STATIC",
    "criterion": "给定t+432001反例推出形态0/时间戳空；t+432000仍1；守卫和强制形态对照准确。"
  },
  {
    "kind": "STATIC",
    "criterion": "说明状态求值先于图像匹配；不把无素材当作静态入口不可分析，不宣称真实像素/游戏通过。"
  },
  {
    "kind": "RUNTIME",
    "criterion": "本轮不要求运行参考/宿主；如以后执行，须独立记录输入/工具/输出与素材前提。"
  },
  {
    "kind": "SPEC_STATIC",
    "criterion": "保留WP35/EG-13/20已正确的动态孵化合同；显式物种资源接口仅在输入形态已求值时为纯消费，不外推调用者。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md
- deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md
- deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md
- deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md

**共享合同**

- 个体形态读取与资源消费交界
- 形态提交→时间戳/特性缓存/能力/图鉴

**依赖**

- M03资源匹配
- M10摘要/图标呈现
- WP21动态形态

**能力范围引用**

- GR4-CAP-M04-016

**关联新问题**

无。

**根因身份**

M04-image-consumer-form-read-dispatch

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "third_round": "GR3-M04-001 remains CLOSED; adjacent image consumer, different rule (dynamic form dispatch versus SPINDA pixel mathematics)",
  "second_round": null,
  "note": "没有据未知第二轮ID猜关联；不重开旧SPINDA整改。",
  "independent_scope_assessment": {
    "relation": "adjacent_dynamic_form_consumer_with_existing_shared_contract",
    "ids": [
      "GIR-FD82-A053",
      "GR3-M04-001"
    ],
    "assessment": "已读A053限定scope、孵化源链和B EG-13/20。A053是孵化核心与演出查询分层；M04是通用按个体取图/摘要入口及WP18上游分类。二者共享动态查询机制但不同消费范围，邻接关系准确；不重开A053，也不混SPINDA像素旧项。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- DERIVED_VECTOR

**执行状态**

NOT_EXECUTED

**置信限定**

HIGH (fixed-source static dispatch and explicit spec claim)

**未知**

- 真实形态图是否存在、像素显示及宿主错误
- 插件/地图动态改写
- 实际资源和宿主像素未证；图鉴/能力重算只按依赖正常的静态调用链判定，插件改写未证。

**排除的主张**

- 不认定所有图像消费者均动态求值
- 不声称真实摘要成功运行
- 不要求保留源API或实现图形模块
- 不把SPINDA历史关闭改为未解决

**用户政策边界**

```json
false
```

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CA",
    "thread_id": "01a1301e-5efe-77a2-9450-fc09ff6830c1",
    "path": "modules/CA/verdicts.json",
    "pointer": "/records/8",
    "decision": "CONFIRM_WITH_REFINEMENT",
    "reason": "原R正背精灵/图标入口读取普通形态，形态提交链与FURFROU严格超5天条件均有明确源证。WP35是必须承认的已覆盖部分，但不能消除WP18直接相反的泛称；整改应收窄为入口归属/跨文档一致性，不重建整个动态形态规格。",
    "required_refinements": [
      "将WP35 §5.2/§9和EG-13/20作为已承接的强反证加入结论。",
      "最低整改是纠正WP18图像泛称，并明确个体入口继承动态读取合同；复用WP21/35既有提交/守卫，不重复扩成全域必修。",
      "显式物种/形态对照须提供已求值的数值参数；上游可能先读取个体，不能笼统称所有物种入口调用链无副作用。"
    ],
    "execution_evidence_assessment": {
      "ca_rerun": false,
      "receipt": "../M04/execution.json",
      "kind": "SOURCE_STATIC / SPEC_STATIC / DERIVED_VECTOR",
      "assessment": "原模块记录的Python清点/JSON/路径校验仅为TOOL_VALIDATION，不支持行为运行通过；CA未执行该脚本或参考函数。",
      "host_or_demo": "NOT_EXECUTED"
    },
    "historical_relation_assessment": {
      "relation": "adjacent_dynamic_form_consumer_with_existing_shared_contract",
      "ids": [
        "GIR-FD82-A053",
        "GR3-M04-001"
      ],
      "assessment": "已读A053限定scope、孵化源链和B EG-13/20。A053是孵化核心与演出查询分层；M04是通用按个体取图/摘要入口及WP18上游分类。二者共享动态查询机制但不同消费范围，邻接关系准确；不重开A053，也不混SPINDA像素旧项。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M05-001 · P2 · REQUIRED — PP补给未区分战斗中的濒死拒绝与非战斗可恢复

领域 M05；分类 实现信息不足；独立审者 thread `01a12fdc-b1dc-7f62-8311-aa6a002b9432`；辅助证据目录 `modules/M05/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/013_Items/003_Item_BattleEffects.rb` · 155–186,501–533：战斗ETHER族和ELIXIR族先要求目标可战斗，别名同门。（固定R；blob `4c522dd209fd27bc5b36f807961e69b3405f6cba`）
- `Data/Scripts/013_Items/002_Item_Effects.rb` · 632–684：非战斗恢复只看招式PP条件，无存活门。（固定R；blob `cad2fc8d57960b79088eb19e92ff97ae9203e6df`）
- `Data/Scripts/013_Items/001_Item_Utilities.rb` · 367–382,644–686,710–775：恢复PP封顶、外层成功扣减；非战斗通用门不拒濒死。（固定R；blob `0ff6f88feb9e1b375027d907e03976d17b10d617`）
- `Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb` · 100–137：战斗资格失败不登记不消费。（固定R；blob `9f38551f88dfb95dc6c1a4e31e2ed968019032b6`）
- `Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb` · 239–285：非蛋目标可进入招式选择，拒绝回成员循环。（固定R；blob `3b61c5afac5ab50c42026ff5bcafa4f3e03ca2ce`）
- `Data/Scripts/014_Pokemon/001_Pokemon.rb` · 264–270：可战斗要求非蛋且HP>0。（固定R；blob `55e7e42c93cc8c0ae91f8594e7a7b9560eb9c22f`）
- `PBS/items.txt` · 3294–3333;5242–5250：默认五种PP恢复道具的场外/战斗用途。（固定R；blob `f0d40d5e111b85a606185101c326e24c832348d9`）
- `PBS/moves.txt` · [TACKLE]5326–5336：总PP35。（固定R；blob `fa5dbaf2739b6b6f55ba5cc5d7d599b4a15b68ca`）
- `Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb` · 163–178：非Hyper普通目标不改变通用资格返回；不抵消PP家族存活门。（固定R；blob `51fd0f689ffac0cbe84168eac90c28b7ac7c16a9`）
- `Data/Scripts/010_Data/002_PBS data/006_Item.rb` · 119–138,171–198：五物品非重要、默认消费；LEPPA此处只审主动入口。（固定R；blob `94ac69921fb4a3c22c730d5155d3a559a3d6afb5`）

**现规格依据**

- `deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md` · §5.2,202–206/§3.5：仅给PP门与同步，未给战斗存活门。（固定B；blob `f6bbfa697f8e3441820f2a72027164ce62557f18`）
- `deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md` · IU-07,51：向量未分濒死上下文。（固定B；blob `93902eba147650543c2f7a3dadbcd1f2aa4eb3cb`）
- `deliverables/final-specification-set/combat-requirements/wp51-ai-action-selection-and-skill.md` · §4,104–108：AI缺索引异常不是人手PP资格表。（固定B；blob `9741e2ada560dfc8012b1ec7068735b1fcd5ba22`）
- `deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md` · §5.2–5.3,126–139：目标选择及通用资格框架，具体道具门引用WP28。（固定B；blob `f4167d75f73bb10ac7729ee96dea6aa6de780ffe`）
- `deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md` · §5.4–5.5,159–165：PP恢复辅助及战斗同步存在，但不承接战斗道具的存活前提。（固定B；blob `b8b953375034a8977abab199f2e1c715dec75e71`）
- `deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md` · §4.2,99–104：通用资格框架回指WP28。（固定B；blob `4e28fadf640afd128e19e6afbb3f61f0fa738fe4`）

**参考实际行为**

ETHER/MAXETHER/主动LEPPABERRY以及ELIXIR/MAXELIXIR的战斗资格先要求目标非蛋且HP>0；濒死者即使PP有缺口仍拒绝，不登记、不扣背包。非战斗对同一非蛋非Hyper濒死者可恢复PP：ETHER/LEPPA所选招+10封顶，MAXETHER回满；ELIXIR逐招+10、MAXELIXIR逐招回满，至少有恢复才成功并由外层扣1。HP保持0。

**现规格的说法**

WP28§5.2列ETHER选招、总PP>0、当前未满和ELIXIR总增量门，并单列战斗同步；§3.5只给通用资格家族调用。未写这五种PP补给战斗额外存活门。IU-07未指明上下文和HP状态。WP51的存活AI/缺索引异常不是这份人手使用资格合同。

**差异/缺口**

独立实现者不能由正式合同唯一判断对濒死成员的战斗PP使用应拒绝、但场外应成功；沿用一套PP缺口条件会在战斗中错误恢复并消费，沿用统一存活门又会错误拒绝场外使用。

**必要前提**

- 默认Gen8、默认五物品和TACKLE数据，正常内部战斗，玩家有可行动使用者A与非场上濒死B，避免全队濒死无法进入战斗。
- B为普通非蛋非Shadow非Hyper合法个体，HP0/100，TACKLE当前0/总35、PP提升0，无额外效果或插件；ETHER库存1，背包/场景正常。
- 场外对照独立重置同一字段，不从战斗结算恢复后取状态；目标/招式选择正常确认，无取消、重入或宿主异常。

**最小反例**

```json
{
  "input": "普通内部战斗，A发起使用ETHER，选择濒死后备B，再选TACKLE0/35。",
  "expected": "显示无效果并留成员选择循环；尚未登记UseItem，ETHER仍1，B仍HP0、PP0/35。",
  "nonbattle_reverse": "相同独立初态从普通背包对B选同招：恢复到10/35，HP仍0，效果成功后ETHER1→0。"
}
```

**正常对照**

仅把B改为HP1/100且仍后备、PP0/35：两上下文均可恢复到10/35；战斗在登记扣1、执行前资格保持时完成效果。

**失败/边界对照**

- HP0且PP有缺口：战斗五种均拒；场外五种按各自量值可恢复。
- 目标存活但全部PP已满则仍按既有无效果规则不消费；ETHER取消招式选择不消费。
- MAXETHER和MAXELIXIR回满35；ETHER/LEPPA/ELIXIR在唯一TACKLE槽的例子为10；这些数值是未执行静态向量。

**独立实现影响**

影响普通合法战斗中的可选择动作、目标PP和背包库存；属于有界事实合同缺口，不是要求实现某个源类或特定API。

**已完成的反证**

```json
{
  "primary_review": {
    "searches": [
      {
        "name": "pp_identities",
        "query": "ETHER|ELIXIR|LEPPABERRY",
        "scope": "deliverables/final-specification-set/",
        "files_searched": 131,
        "method": "全目录逐行不区分大小写正则；与本次rg检索互证",
        "hits": [
          {
            "path": "deliverables/final-specification-set/combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md",
            "lines": [
              223,
              225
            ]
          },
          {
            "path": "deliverables/final-specification-set/combat-requirements/wp47-a-attributes-targeting-calling-data.md",
            "lines": [
              137
            ]
          },
          {
            "path": "deliverables/final-specification-set/combat-requirements/wp47-b-control-items-coverage-data.md",
            "lines": [
              72,
              75
            ]
          },
          {
            "path": "deliverables/final-specification-set/combat-requirements/wp51-ai-action-selection-and-skill.md",
            "lines": [
              106,
              108
            ]
          },
          {
            "path": "deliverables/final-specification-set/combat-requirements/wp52-c-item-control-coverage-and-data.md",
            "lines": [
              103
            ]
          },
          {
            "path": "deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md",
            "lines": [
              145,
              204
            ]
          },
          {
            "path": "deliverables/final-specification-set/pokemon-rules/wp50-held-item-effect-coverage.md",
            "lines": [
              28
            ]
          },
          {
            "path": "deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md",
            "lines": [
              90
            ]
          },
          {
            "path": "deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md",
            "lines": [
              74,
              75
            ]
          },
          {
            "path": "deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md",
            "lines": [
              51
            ]
          }
        ]
      },
      {
        "name": "pp_aliases",
        "query": "以太|回复.?PP|恢复.?PP|PP.?回复|PP.?恢复|活力块|活力碎片|苹野|LEPPA",
        "scope": "deliverables/final-specification-set/",
        "files_searched": 131,
        "method": "全目录逐行不区分大小写正则；与本次rg检索互证",
        "hits": [
          {
            "path": "deliverables/final-specification-set/combat-requirements/wp47-a-attributes-targeting-calling-data.md",
            "lines": [
              137
            ]
          },
          {
            "path": "deliverables/final-specification-set/combat-requirements/wp47-b-control-items-coverage-data.md",
            "lines": [
              72
            ]
          },
          {
            "path": "deliverables/final-specification-set/combat-requirements/wp51-ai-action-selection-and-skill.md",
            "lines": [
              106,
              108
            ]
          },
          {
            "path": "deliverables/final-specification-set/combat-requirements/wp52-b-field-damage-healing-and-target-evaluation.md",
            "lines": [
              134
            ]
          },
          {
            "path": "deliverables/final-specification-set/combat-requirements/wp52-c-item-control-coverage-and-data.md",
            "lines": [
              103
            ]
          },
          {
            "path": "deliverables/final-specification-set/combat-requirements/wp52-c-items-calling-and-control-evaluation.md",
            "lines": [
              77,
              203
            ]
          },
          {
            "path": "deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md",
            "lines": [
              159,
              220
            ]
          },
          {
            "path": "deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md",
            "lines": [
              145,
              206,
              315
            ]
          },
          {
            "path": "deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md",
            "lines": [
              267
            ]
          },
          {
            "path": "deliverables/final-specification-set/pokemon-rules/wp50-held-item-effect-coverage.md",
            "lines": [
              28
            ]
          },
          {
            "path": "deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md",
            "lines": [
              21,
              90,
              171,
              178
            ]
          },
          {
            "path": "deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md",
            "lines": [
              45
            ]
          },
          {
            "path": "deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md",
            "lines": [
              99,
              148
            ]
          },
          {
            "path": "deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md",
            "lines": [
              75,
              232
            ]
          },
          {
            "path": "deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md",
            "lines": [
              182
            ]
          },
          {
            "path": "deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md",
            "lines": [
              96,
              106
            ]
          },
          {
            "path": "deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md",
            "lines": [
              128
            ]
          }
        ]
      },
      {
        "name": "pp_fainted",
        "query": "PP.{0,30}(濒死|失能|不可行动|可行动|可战斗)|(濒死|失能|不可行动|可行动|可战斗).{0,30}PP",
        "scope": "deliverables/final-specification-set/",
        "files_searched": 131,
        "method": "全目录逐行不区分大小写正则；与本次rg检索互证",
        "hits": [
          {
            "path": "deliverables/final-specification-set/combat-requirements/wp39-battle-context-and-participants.md",
            "lines": [
              215
            ]
          },
          {
            "path": "deliverables/final-specification-set/combat-requirements/wp45-weather-terrain-side-and-position-effects.md",
            "lines": [
              187
            ]
          },
          {
            "path": "deliverables/final-specification-set/combat-requirements/wp47-a-move-attributes-targeting-and-calling.md",
            "lines": [
              59
            ]
          },
          {
            "path": "deliverables/final-specification-set/combat-requirements/wp52-c-items-calling-and-control-evaluation.md",
            "lines": [
              150
            ]
          },
          {
            "path": "deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md",
            "lines": [
              64
            ]
          },
          {
            "path": "deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md",
            "lines": [
              285
            ]
          },
          {
            "path": "deliverables/final-specification-set/pokemon-rules/wp22-mega-and-primal-reversion.md",
            "lines": [
              23
            ]
          },
          {
            "path": "deliverables/final-specification-set/pokemon-rules/wp31-basic-evolution.md",
            "lines": [
              11
            ]
          },
          {
            "path": "deliverables/final-specification-set/test-catalog/combat-requirements-wp47-ab.md",
            "lines": [
              89,
              91,
              100
            ]
          },
          {
            "path": "deliverables/final-specification-set/test-catalog/pokemon-rules-wp43-44-46-48-50.md",
            "lines": [
              82,
              128,
              220
            ]
          },
          {
            "path": "deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md",
            "lines": [
              704
            ]
          }
        ]
      }
    ],
    "contexts_read": [
      {
        "path": "deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md",
        "commit": "1f36475d22120a0d1175967d5b17d71fe8311d88",
        "lines_or_symbol": "§3.2–3.5/§5.2/§7",
        "fact": "通用门未拒所有濒死；PP段只列PP条件。"
      },
      {
        "path": "deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md",
        "commit": "1f36475d22120a0d1175967d5b17d71fe8311d88",
        "lines_or_symbol": "§3.2/§5.4–5.5",
        "fact": "恢复底层/同步不替代使用资格。"
      },
      {
        "path": "deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md",
        "commit": "1f36475d22120a0d1175967d5b17d71fe8311d88",
        "lines_or_symbol": "§4.2",
        "fact": "资格家族框架和引用，不列PP存活门。"
      },
      {
        "path": "deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md",
        "commit": "1f36475d22120a0d1175967d5b17d71fe8311d88",
        "lines_or_symbol": "§5.2–5.3",
        "fact": "非蛋目标和资格回调，不自动过滤全部濒死。"
      },
      {
        "path": "deliverables/final-specification-set/combat-requirements/wp51-ai-action-selection-and-skill.md",
        "commit": "1f36475d22120a0d1175967d5b17d71fe8311d88",
        "lines_or_symbol": "§4,104–108",
        "fact": "AI存活示例及缺索引异常不定义人工选目标的反向资格，也未给ELIXIR族门。"
      },
      {
        "path": "deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md",
        "commit": "1f36475d22120a0d1175967d5b17d71fe8311d88",
        "lines_or_symbol": "§4 LEPPABERRY,90",
        "fact": "持有触发是不同消费者，不能替代主动资格。"
      },
      {
        "path": "deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md",
        "commit": "1f36475d22120a0d1175967d5b17d71fe8311d88",
        "lines_or_symbol": "IU-07/26–28",
        "fact": "PP正常向量和POTION复检不提供PP濒死场景。"
      }
    ],
    "result": "未找到五种主动PP道具的战斗HP>0门及场外濒死可恢复对照；保留已有通用资格、同步、被动果与AI条款，不以无英文词命中单独判缺失。",
    "source_countersearch": {
      "scope": "固定参考全部312脚本",
      "queries": [
        ":ETHER|:MAXETHER|:ELIXIR|:MAXELIXIR|:LEPPABERRY",
        "pbCanUseItemOnPokemon|triggerCanUseInBattle|pbItemMenu"
      ],
      "result": "资格注册/复制集中Item_BattleEffects155–186；非战斗632–684；其它命中为被动持物、AI估值、迁移身份与拾取表，不覆写该资格。Shadow覆写163–178对本例非Hyper成员不增加或撤销此门。"
    }
  },
  "primary_relative_paths_base": "modules/M05",
  "independent_counterevidence": {
    "search_ids": [
      "M05-pp",
      "M05-pp-overrides",
      "CA-shared-alias-supplement"
    ],
    "words": [
      "ETHER|ELIXIR|LEPPABERRY|以太|苹野|PP.{0,16}(恢复|回复|濒死|失能|可战斗)|恢复.{0,10}PP|濒死.{0,25}(道具|物品|PP)",
      "过渡坐标|冲浪基点|冲浪.{0,8}清|动态形态查询|资源消费.{0,15}形态|形态.{0,15}副作用|计时.{0,10}变量|变量.{0,10}计时|PP.{0,20}(补给|补充|活体|存活)|翻译.{0,10}(重复|合并)|文本域.{0,10}(覆盖|冲突)"
    ],
    "scope": {
      "baseline": "1f36475d22120a0d1175967d5b17d71fe8311d88",
      "root": "deliverables/final-specification-set/",
      "files": 131,
      "includes": "正文、共享条款、数据附表及静态测试目录；并非131篇逐篇重新验收"
    },
    "source_countersearch": [
      {
        "id": "M05-pp-overrides",
        "pattern": ":ETHER|:MAXETHER|:ELIXIR|:MAXELIXIR|:LEPPABERRY|def pbCanUseItemOnPokemon|def pbCheckUseOnPokemon|def triggerCanUseInBattle|def self.triggerCanUseInBattle|def pbRegisterItem|def pbChoosePokemon",
        "files": 312
      }
    ],
    "contexts_read_and_assessed": [
      "WP28 §3.2/§3.5/§5.2；IU-07/26–28",
      "WP20恢复辅助、WP40通用资格、WP67-A非蛋目标/拒绝循环",
      "WP51 I06/I07缺索引与WP50持有LEPPA不是人工带有效索引主动恢复"
    ],
    "conclusion": "已有通用资格/非蛋条件没有战斗PP族HP>0门。AI“存活”前提只是异常例限制，不能反推出场外或战斗全部资格；附表评级/投掷也不承接此门。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CA"
}
```

**下一轮最小修订**

在WP28§5.2以战斗/非战斗两列补五物品的资格差异和别名集合，明确战斗拒绝位于登记扣减之前；保留原恢复量、同步与退款规则。为IU目录增HP0战斗拒、HP0场外成功、HP>0正常及满PP/取消反向向量；WP40/WP67-A可引用，不必复制成多条根因。

**验收标准**

```json
[
  {
    "kind": "static",
    "criterion": "正文独立给出五种主动PP补给的战斗非蛋且HP>0门，并明确场外无该存活门；不扩大为所有道具统一门。"
  },
  {
    "kind": "static",
    "criterion": "按上述夹具可唯一推出战斗库存1/PP0/HP0、场外库存0/PP10/HP0，且MAX两种和别名量值明确。"
  },
  {
    "kind": "static",
    "criterion": "补存活、PP满、取消对照；引用WP20恢复/同步、WP40登记与WP67-A拒绝返回层不冲突；AI/被动LEPPA不混入。"
  },
  {
    "kind": "runtime",
    "criterion": "本轮不要求运行；静态向量标NOT_EXECUTED。未来如做宿主验证须另记录工具/输入/输出/副作用，不以本次审查签运行通过。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md
- deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md

**共享合同**

```json
[
  {
    "path": "deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md",
    "role": "PP状态和恢复量/同步，保持既有合同"
  },
  {
    "path": "deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md",
    "role": "登记前资格门/扣减"
  },
  {
    "path": "deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md",
    "role": "拒绝回成员选择"
  },
  {
    "path": "deliverables/final-specification-set/combat-requirements/wp51-ai-action-selection-and-skill.md",
    "role": "AI消费者区分，非本问题修复目标"
  },
  {
    "path": "deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md",
    "role": "被动LEPPA区别"
  }
]
```

**依赖**

- WP20 非蛋/HP和PP定义
- WP27库存
- WP28主动使用
- WP40战斗登记
- WP67-A目标选择

**能力范围引用**

- GR4-CAP-M05-017

**关联新问题**

无。

**根因身份**

PP_RECOVERY_CONTEXT_ELIGIBILITY

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "third_round": null,
  "second_round": null,
  "note": "不是GR3-M05-001/002或GR3-M07-001。第二轮同根ID未作猜测；本轮只判当前固定正式材料缺口。",
  "independent_scope_assessment": {
    "relation": "new_bounded_scope",
    "assessment": "本项在固定B/R独立成立；未把原模块历史PASS当证据，未重开旧关闭项，未扩审229。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- DERIVED_VECTOR

**执行状态**

NOT_EXECUTED

**置信限定**

HIGH

**未知**

- 真实媒体、按键、宿主UI运行未证。
- 未穷举插件覆写与全部世代数据替换；缺口在固定默认数据已成立。
- 宿主菜单/消息演出未运行；第三方覆盖与全部数据变体不在本项。

**排除的主张**

- 不认为底层PP恢复本身拒绝濒死。
- 不声称全部战斗道具不能对濒死使用，复活道具另有相反资格。
- 不将AI缺索引异常、被动树果或执行退款残留算成本问题。
- 不要求修改参考，也不提供框架实现。

**用户政策边界**

```json
false
```

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CA",
    "thread_id": "01a1301e-5efe-77a2-9450-fc09ff6830c1",
    "path": "modules/CA/verdicts.json",
    "pointer": "/records/9",
    "decision": "CONFIRM",
    "reason": "默认数据与真实人工菜单→通用资格→PP家族→登记扣减链均独立检查。场外通用门不拒濒死、恢复辅助不改HP。反例比较同一有效成员和招式，能排除错误地统一两上下文资格的实现；P2合理。",
    "required_refinements": [],
    "execution_evidence_assessment": {
      "ca_rerun": false,
      "receipt": "../M05/execution.json",
      "kind": "SOURCE_STATIC / SPEC_STATIC / DERIVED_VECTOR",
      "assessment": "原模块记录的Python清点/JSON/路径校验仅为TOOL_VALIDATION，不支持行为运行通过；CA未执行该脚本或参考函数。",
      "host_or_demo": "NOT_EXECUTED"
    },
    "historical_relation_assessment": {
      "relation": "new_bounded_scope",
      "assessment": "本项在固定B/R独立成立；未把原模块历史PASS当证据，未重开旧关闭项，未扩审229。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M06-001 · P3 · REQUIRED — BR18 在双不同力量道具前提下错误保留五项 IV 继承分支

领域 M06；分类 事实错误；独立审者 thread `01a12fe0-a4a3-75a0-87bd-03c04ac176c8`；辅助证据目录 `modules/M06/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/012_Overworld/007_Overworld_DayCare.rb` · 21–45,173–212：先3项，gen≥6且亲本持DESTINYKNOT才5；每个力量属性扣一次，其余不同属性抽样。（固定R；blob `302921c96ecfc4767d9ab9515d8d1e7820aa858c`）
- `Data/Scripts/014_Pokemon/001_Pokemon.rb` · 551–577：每个亲本持物读取/比较来自单一规范身份。（固定R；blob `55e7e42c93cc8c0ae91f8594e7a7b9560eb9c22f`）
- `PBS/items.txt` · 766–774,1423–1439：DESTINYKNOT、POWERWEIGHT、POWERBRACER是不同登记项。（固定R；blob `f0d40d5e111b85a606185101c326e24c832348d9`）

**现规格依据**

- `deliverables/final-specification-set/pokemon-rules/wp34-inheritance-and-offspring.md` · §7，128–134：正文的3/5数量及力量属性扣减是正确规则。（固定B；blob `be4e24a8a3941af83514c9837afc71c7a1e64262`）
- `deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md` · BR16–19，239–242：BR18错误地给双不同力量道具列5−2分支。（固定B；blob `50086b77a48a2714af17cd8c86174d271397a942`）
- `deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md` · §6.1–6.2：本轮仅核此合同／向量，不签全文件通过（固定B；blob `b8b953375034a8977abab199f2e1c715dec75e71`）

**参考实际行为**

普通单持物亲本各持不同力量道具时，均不持羁绊之绳，基础继承数恒3；两种不同属性各固定1项，只再从其余4属性无放回选1项。世代≥6不会单独把3变5。

**现规格的说法**

WP34 §7正文正确，但BR18明列固定2项后剩余采样1（3−2）或3（5−2）；后者在该行前提下不可达。

**差异/缺口**

静态测试接受了一个需要第三件亲本持物的预期，违反同集单持物与羁绊之绳必要条件。不是正文算法缺失。

**必要前提**

- 参考默认普通亲本、每个体一项持物、无插件或自定义多持物覆写；世代8。
- 两亲本可用合法♂/♀PIKACHU，分别持POWERWEIGHT和POWERBRACER；合法数据/场景/玩家。
- 只观察IV继承通道，不要求随机具体输出、孵化或领取。

**最小反例**

```json
{
  "input": "母POWERWEIGHT、父POWERBRACER；母HP31、父ATTACK31；其余亲本IV均0；蛋创建六IV均1（合法条件化随机输入）。",
  "expected": "HP31、ATTACK31；其余4属性中恰1项被继承为0、3项保创建值1。总继承属性3。",
  "incorrect_allowed_result": "若按BR18的5−2分支，再写3项为0，仅1项保创建值1，总继承属性5。",
  "evidence_level": "DERIVED_VECTOR",
  "execution_status": "NOT_EXECUTED"
}
```

**正常对照**

无Knot/无Power继承3项；双不同Power固定2+随机1；双相同Power固定同项一次+随机2。

**失败/边界对照**

合法五项对照应为一方DESTINYKNOT、另一方POWERWEIGHT（gen≥6）：固定HP1项、再选4项；gen5下同一配对仅3项（固定1+随机2）。

**独立实现影响**

照BR18构建验收会允许或要求不可能的5项组合，使正确3项实现的测试预期不唯一；正文已有正确规则，影响局限于向量质量，定P3。

**已完成的反证**

```json
{
  "primary_review": {
    "search_id": "M06-NEG-IV-01",
    "universe": {
      "root": "deliverables/final-specification-set/",
      "count": 131,
      "baseline": "1f36475d22120a0d1175967d5b17d71fe8311d88"
    },
    "query": "BR18|5−2|5-2|DESTINYKNOT|羁绊之绳|红线|力量道具|Power (?:Weight|Bracer|items?)",
    "method": "全套正式Markdown合理别名搜索；命中上下文按繁育主规则、静态向量、持物共享合同与纯物品目录区分。",
    "hits": [
      {
        "path": "deliverables/final-specification-set/combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md",
        "line_numbers": [
          225,
          227,
          245
        ]
      },
      {
        "path": "deliverables/final-specification-set/combat-requirements/wp47-b-control-items-coverage-data.md",
        "line_numbers": [
          72
        ]
      },
      {
        "path": "deliverables/final-specification-set/combat-requirements/wp52-a-generic-numerical-and-status-evaluation.md",
        "line_numbers": [
          205
        ]
      },
      {
        "path": "deliverables/final-specification-set/combat-requirements/wp52-c-item-control-coverage-and-data.md",
        "line_numbers": [
          105
        ]
      },
      {
        "path": "deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md",
        "line_numbers": [
          345
        ]
      },
      {
        "path": "deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md",
        "line_numbers": [
          241
        ]
      },
      {
        "path": "deliverables/final-specification-set/creature-rpg/wp24-player-trainers-partners.md",
        "line_numbers": [
          272
        ]
      },
      {
        "path": "deliverables/final-specification-set/creature-rpg/wp25-party-and-storage.md",
        "line_numbers": [
          203
        ]
      },
      {
        "path": "deliverables/final-specification-set/creature-rpg/wp26-acquisition-gifts-and-script-trade.md",
        "line_numbers": [
          192
        ]
      },
      {
        "path": "deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md",
        "line_numbers": [
          252
        ]
      },
      {
        "path": "deliverables/final-specification-set/generic-kernel/wp02-rule-configuration-and-data-variants.md",
        "line_numbers": [
          197
        ]
      },
      {
        "path": "deliverables/final-specification-set/pokemon-rules/wp34-inheritance-and-offspring.md",
        "line_numbers": [
          128,
          130,
          131,
          160,
          175,
          188,
          202
        ]
      },
      {
        "path": "deliverables/final-specification-set/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md",
        "line_numbers": [
          74
        ]
      },
      {
        "path": "deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md",
        "line_numbers": [
          163
        ]
      },
      {
        "path": "deliverables/final-specification-set/test-catalog/README.md",
        "line_numbers": [
          38
        ]
      },
      {
        "path": "deliverables/final-specification-set/test-catalog/combat-requirements-wp39-40-41-42-45.md",
        "line_numbers": [
          160
        ]
      },
      {
        "path": "deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md",
        "line_numbers": [
          129
        ]
      },
      {
        "path": "deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md",
        "line_numbers": [
          239,
          240,
          241
        ]
      }
    ],
    "contexts_read": [
      "WP34 §7, §9, §10, §11；BR16–19；WP20 §6.1–6.3",
      "WP30/WP02配置EV项；WP42 Pickup稀有池；WP44/WP50/WP52A及相应测试的迷恋效果；WP47B/WP52C纯物品身份行",
      "其余WP18/24/25/26及测试README命中来自文件名中的5-2，已读命中上下文，为导航而非IV规则"
    ],
    "result": "仅BR18含双不同力量物品仍可5−2的预期；WP34明确五项必须亲本持DESTINYKNOT，WP20单持物合同并未豁免；其它命中为战斗/EV或物品目录，不改变遗传持物门。",
    "source_countercheck": {
      "query": "inherit_IVs|DESTINYKNOT|POWERWEIGHT|POWERBRACER (all Data/Scripts)",
      "result": "仅DayCare生成链定义并调用inherit_IVs；其它命中是战斗/AI/物品效果。生成入口不接收独立继承数量或多持物参数；Pokemon持物单一身份，默认PBS三物品互异。"
    },
    "evidence_level": [
      "SOURCE_STATIC",
      "SPEC_STATIC"
    ],
    "execution_status": "NOT_EXECUTED"
  },
  "primary_relative_paths_base": "modules/M06",
  "independent_counterevidence": {
    "search_ids": [
      "M06-power",
      "M06-iv-overrides"
    ],
    "words": [
      "BR18|5−2|DESTINYKNOT|羁绊之绳|红线|力量道具|POWERWEIGHT|POWERBRACER"
    ],
    "scope": {
      "baseline": "1f36475d22120a0d1175967d5b17d71fe8311d88",
      "root": "deliverables/final-specification-set/",
      "files": 131,
      "includes": "正文、共享条款、数据附表及静态测试目录；并非131篇逐篇重新验收"
    },
    "source_countersearch": [
      {
        "id": "M06-iv-overrides",
        "pattern": "inherit_IVs|def hasItem\\?|DESTINYKNOT|POWERWEIGHT|POWERBRACER",
        "files": 312
      }
    ],
    "contexts_read_and_assessed": [
      "WP34 §7数量规则正确；BR16/17/19与BR18对照",
      "WP20单一持物及同一身份比较",
      "力量EV/速度、红线迷恋/拾取、AI评级附表均不提供第三持物或额外继承数量"
    ],
    "conclusion": "BR18的5−2分支没有满足羁绊之绳门的普通输入；正确正文不能让错误验收分支成立。不是整个遗传算法缺失。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CA"
}
```

**下一轮最小修订**

仅修BR18为固定2+随机1；可补单Knot+单Power的合法5项及gen5对照。保留WP34正确数量规则和持物合同，不改参考或发明多持物能力。

**验收标准**

```json
[
  {
    "kind": "static",
    "criterion": "双不同Power向量只允许3个不同继承属性，两个固定、一个其余属性。"
  },
  {
    "kind": "static",
    "criterion": "若保留5项对照，前提明确gen≥6、一个Knot持有者和至多一个Power持有者；固定1+其余4。"
  },
  {
    "kind": "static",
    "criterion": "正文与测试不暗含每亲本多件持物，且同Power重复属性只计一次。"
  },
  {
    "kind": "runtime",
    "criterion": "本轮不要求宿主或参考运行；任何后续执行须另立隔离记录，不能把本推导升格为执行。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md

**共享合同**

- deliverables/final-specification-set/pokemon-rules/wp34-inheritance-and-offspring.md §7
- deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md §6

**依赖**

- WP33两槽生成入口
- WP20单持物身份
- 世代配置

**能力范围引用**

- GR4-CAP-M06-015

**关联新问题**

无。

**根因身份**

M06_IV_VECTOR_UNSATISFIABLE_HELD_ITEM_COMBINATION

**旧GR3/229/341关系**

```json
{
  "relationship": "new",
  "third_round_related_id": null,
  "second_round_related_id": null,
  "note": "未猜第二轮ID；与GR3-M06-001经验提示时点根因不同，不重开旧CLOSED。",
  "independent_scope_assessment": {
    "relation": "new_bounded_scope",
    "assessment": "本项在固定B/R独立成立；未把原模块历史PASS当证据，未重开旧关闭项，未扩审229。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- DERIVED_VECTOR

**执行状态**

NOT_EXECUTED

**置信限定**

high_static

**未知**

- 第三方多持物插件可改行为，但无此材料且不在该向量前提。
- 第三方多持物/重写比较可改变前提，但无该材料且不属于普通BR18输入；未运行繁育。

**排除的主张**

- 不认定WP34正文继承算法错误
- 不认定官方游戏规则是证据
- 不声称运行捕获/繁育/宿主
- 不把随机数值恰等于亲本值视作该属性实际继承

**用户政策边界**

```json
false
```

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CA",
    "thread_id": "01a1301e-5efe-77a2-9450-fc09ff6830c1",
    "path": "modules/CA/verdicts.json",
    "pointer": "/records/10",
    "decision": "CONFIRM",
    "reason": "源数量门要求Knot，两个普通持物槽已被不同Power占满且三身份确实不同；B正文正确而BR18接受不可能分支。最小反例条件可满足，P3局部测试纠错合适。",
    "required_refinements": [],
    "execution_evidence_assessment": {
      "ca_rerun": false,
      "receipt": "../M06/execution.json",
      "kind": "SOURCE_STATIC / SPEC_STATIC / DERIVED_VECTOR",
      "assessment": "原模块记录的Python清点/JSON/路径校验仅为TOOL_VALIDATION，不支持行为运行通过；CA未执行该脚本或参考函数。",
      "host_or_demo": "NOT_EXECUTED"
    },
    "historical_relation_assessment": {
      "relation": "new_bounded_scope",
      "assessment": "本项在固定B/R独立成立；未把原模块历史PASS当证据，未重开旧关闭项，未扩审229。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M10-001 · P2 · REQUIRED — 通用命令选择与逐位数字输入的同轮优先序仍缺少合同

领域 M10；分类 状态或时序错误；独立审者 thread `01a12ff1-a1b1-7212-84b3-c3fdcd6552a9`；辅助证据目录 `modules/M10/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/007_Objects and windows/011_Messages.rb` · 166–205;721–801：数字先组件更新，再USE/elif BACK；普通及帮助命令先BACK，取消无效时仍可USE。（固定R；blob `91c985bd0fda9a2368c894dee0ebbc9a476e9886`）
- `Data/Scripts/007_Objects and windows/005_SpriteWindow_text.rb` · 687–729;862–923：数字/列表方向处理均在确认出口之前，故可同轮改值/改索引并返回。（固定R；blob `e8be64d69b3bcb02def7a0cc09c0a5d4027cc628`）
- `Data/Scripts/003_Game processing/004_Interpreter_Commands.rb` · 325–334：事件数字输入调用同一逐位数字入口，结果写变量。（固定R；blob `58167231199f1cb8bdc499a61f5ada544d3f7616`）
- `Data/Scripts/016_UI/019_UI_PC.rb` · 4–16;116–153：正常PC菜单消费者使用普通/帮助命令入口。（固定R；blob `254fd995a55ad17bd82a341d1b13eb7cb6fc212b`）

**现规格依据**

- `deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md` · §4 L92–99、§5.2–5.3 L114–121、§7.2：仅定义单键结果和更新机会，没有各入口竞争结果。（固定B；blob `81b14a0b09327bc030e5d9ef9f907089bd68cb82`）
- `deliverables/final-specification-set/user-interface/wp66-c-bag-item-storage-and-shop-ui.md` · §5.1 L88–108：旧同轮表明确是共享物品数量/两商店。（固定B；blob `f49d1e3a64e64fb61e1351372f34302a7b925e78`）
- `deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md` · MG12–MG20、B04-M07–09、U05-QN01–04：分别覆盖单键、光标命名、物品数量，不覆盖普通命令和逐位数字竞争。（固定B；blob `5dbb1fbed36800c39844a549939b5123c4b3c1c5`）

**参考实际行为**

命令/带帮助命令：允许取消时同轮BACK+USE返回取消编码；取消项0时BACK无效但本轮USE仍返回当前索引。逐位数字：先编辑方向再USE；合法值当轮确认，USE与BACK同时成立仍确认；越界USE只蜂鸣继续，BACK不被处理。

**现规格的说法**

命令与数字各有确认/取消条款，但未给竞争裁决。已有明确同轮表的“共享数量”是按件数增减窗口，不能泛用于逐位数字；命名的优先序同样是另一入口。

**差异/缺口**

缺少两个实际默认消费者的同轮返回/继续判据；从单键规则无法唯一推出确认还是取消，以及方向能否与确认同轮发生。

**必要前提**

- 无插件，窗口已正常进入循环；列出的输入查询同采样轮为真，其余假。
- 命令为两项、默认索引0；取消项分别2与0。数字范围[0,9]、初值1、显式取消值−1。
- 方向值由正常组件更新产生；数字越界对照采用范围[3,3]初值3同轮UP。
- 无传入块改写值或输入；USE/BACK是给定按下沿，方向是给定repeat查询，不是已实测物理按键。事件103的默认取消值为初值；显式取消−1只是独立通用数字夹具。

**最小反例**

```json
{
  "input": "普通命令取消项2/索引0，USE+BACK；独立数字范围[0,9]/当前1/取消−1，USE+BACK。",
  "reference_output": "前者返回1；后者返回1作为确认，绝非取消−1。",
  "distinguishing_alternative": "全局“取消优先”会使数字返回−1；全局“确认优先”会使命令返回0。"
}
```

**正常对照**

两项命令单独USE返回0、单独BACK在取消项2时返回1；数字单独USE返回1、单独BACK返回−1。

**失败/边界对照**

- 数字当前1，UP+USE→先变2再立即返回2；它不遵守物品数量一轮只执行首个动作。
- 数字范围[3,3]初值3，UP+USE+BACK→先变4，确认越界蜂鸣，留循环；同轮BACK不会救出。
- 命令取消项0，USE+BACK→BACK无效后仍返回当前索引0；带帮助入口相同。

**独立实现影响**

独立实现若采用统一按钮裁决会产生不同的选择/事件变量值，或在参考仍等待的越界场景提前取消。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-searches.json",
    "search_ids": [
      "selector_competition",
      "selector_priority_exact"
    ],
    "scope": "全部131正式文件",
    "relevant_contexts_read": [
      "deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md §4/5/6.2.1/7.2",
      "deliverables/final-specification-set/user-interface/wp66-c-bag-item-storage-and-shop-ui.md §5.1",
      "deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md MG/B04-M/U05-QN",
      "deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md §7"
    ],
    "result": "确认已存在的光标命名与物品数量竞争规则均不同入口；未找到普通命令/帮助命令或逐位数字的上述裁决。其它命中为录像/转换的同轮概念，不能承接此行为。"
  },
  "primary_relative_paths_base": "modules/M10",
  "independent_counterevidence": {
    "search_ids": [
      "CB-N01"
    ],
    "terms": [
      "同轮|同一轮|同时.{0,20}(USE|BACK|确认|取消)|竞争|取消优先|确认优先|逐位|命令选择|MG1[2-9]|MG20|U05-QN"
    ],
    "scope": "B 固定正式131篇，正文、scope、共享合同、附表和测试全部纳入；各检索文件字节与 git show B 相等",
    "contexts_actually_read": [
      "WP17 §4/§5/§6.2.1/§6.4/§7.2",
      "WP66-C §5.1 与 U05-QN01–04",
      "WP67-A §9.1 与 U05-TX01–04",
      "WP65 §7.2；WP13命令103"
    ],
    "conclusion": "命名、共享件数、商店与战斗列表确有局部规则，但均不能推出普通命令和逐位数字的不同竞争结果。MG12的不可取消及MG18的越界只给单独输入；没有全局确认/取消优先规则可补此缺口。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CB"
}
```

**下一轮最小修订**

在WP17按入口增加一个简短竞争表：命令的可取消/不可取消分流；数字先编辑再确认、USE优先及越界仍压过BACK。给定静态查询前提，不规定输入调度实现。

**验收标准**

```json
[
  {
    "kind": "SPEC_STATIC",
    "criterion": "仅凭正式集可唯一推出上述命令2/0与数字合法/越界四分支。"
  },
  {
    "kind": "DERIVED_VECTOR",
    "criterion": "增加单键对照、UP+USE与越界UP+USE+BACK案例，标NOT_EXECUTED。"
  },
  {
    "kind": "SPEC_STATIC",
    "criterion": "保留U05物品数量/商店与光标命名合同，不把其顺序统一化。"
  },
  {
    "kind": "EXECUTED_HOST_OR_DEMO",
    "criterion": "如未来声称物理键可达/真实UI通过，须另供宿主证据；本修订不要求先运行。"
  },
  {
    "kind": "SPEC_STATIC",
    "criterion": "事件数字消费者另用默认取消等于初值的夹具；例如初1同轮UP+USE+BACK确认2，不能把通用取消−1称为该事件默认。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md
- deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md

**共享合同**

- WP65 PC命令
- WP13事件数字输入
- WP66-C数量窗口分界

**依赖**

- WP17通用UI
- WP15资源访问
- 宿主输入/字体或媒体接口的条件前提

**能力范围引用**

- GR4-CAP-M10-002

**关联新问题**

无。

**根因身份**

```json
{
  "id": "GR4-M10-001-ROOT",
  "description": "缺少两个实际默认消费者的同轮返回/继续判据；从单键规则无法唯一推出确认还是取消，以及方向能否与确认同轮发生。"
}
```

**旧GR3/229/341关系**

```json
{
  "relation": "new_scope_same_root",
  "third_round": "GR3-M10-002",
  "second_round": null,
  "note": "GR3-M10-002对物品数量/钱店/BP的修订仍满足，当前新增普通命令与逐位数字入口，非旧项未解决或回归。",
  "independent_scope_assessment": {
    "relation": "new_scope_same_root",
    "related_ids": [
      "GR3-M10-002"
    ],
    "assessment": "B中U05件数/商店条款已存在且范围明确；本项是同类问题的新增消费者范围，不是该旧范围回归，不重开或补签旧关闭。M01–M06十一候选无同根；M03路线时序不同。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- DERIVED_VECTOR

**执行状态**

NOT_EXECUTED

**置信限定**

HIGH_STATIC

**未知**

- 真实宿主/媒体/输入未运行；未推断完整Demo可达。
- 真实宿主、媒体、物理输入与完整Demo未执行；外部插件不在固定R证明范围。

**排除的主张**

- 不要求采用源类/方法/容器组织。
- 不修改参考或决定未来产品必须保留该兼容细节。

**用户政策边界**

```json
false
```

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CB",
    "thread_id": "01a13036-2ee9-7e43-8d09-4699ed1b03f4",
    "path": "modules/CB/verdicts.json",
    "pointer": "/records/0",
    "decision": "CONFIRM",
    "reason": "确认有实际调用与清楚的最小差异。先更新组件与之后两个出口的相对次序决定返回值或继续等待，现有各入口单键规则不能唯一决定它。范围限通用命令/帮助命令及逐位数字，不推广为全部UI；P2针对可改变有效选择和事件变量的行为合同。",
    "required_refinements": [],
    "execution_evidence_assessment": "该候选没有参考行为执行。原模块工具校验只证明产物结构/锚点等，不能证明本候选行为；CB未运行参考函数、行为模型、UI、输入或宿主。以下结果为源码/规格静态核对及条件化推导。",
    "historical_relation_assessment": {
      "relation": "new_scope_same_root",
      "related_ids": [
        "GR3-M10-002"
      ],
      "assessment": "B中U05件数/商店条款已存在且范围明确；本项是同类问题的新增消费者范围，不是该旧范围回归，不重开或补签旧关闭。M01–M06十一候选无同根；M03路线时序不同。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M10-002 · P3 · REQUIRED — 默认皮肤冷读取的回退链与显式设置空结果未进入资源合同

领域 M10；分类 数据或资源契约缺口；独立审者 thread `01a12ff1-a1b1-7212-84b3-c3fdcd6552a9`；辅助证据目录 `modules/M10/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/007_Objects and windows/002_MessageConfig.rb` · 35–85：冷读取先选项皮肤，后系统名、System/Window、001-Blue01；显式设置只解析一次并保留空结果。（固定R；blob `47813fd34df588b24a5cc84f9928d9a55f4bcfc6`）
- `Data/Scripts/007_Objects and windows/004_SpriteWindow.rb` · 818–868：窗口默认皮肤消费缓存；显式setSkin解析失败提前返回，不自动使用默认链。（固定R；blob `c579631b93f6f9fe160bfebaeea3543233706021`）
- `Data/Scripts/007_Objects and windows/011_Messages.rb` · 380–394;444–450：普通消息采用speech默认；空w标签直接清windowskin，属不同操作。（固定R；blob `91c985bd0fda9a2368c894dee0ebbc9a476e9886`）
- `Data/Scripts/016_UI/015_UI_Options.rb` · 492–519：选项值先写再显式设置皮肤缓存及预览。（固定R；blob `cb4a2285bf3c7c3dc4464e36f0769b3d1835321f`）

**现规格依据**

- `deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md` · §3.1 L35、§3.4 L86–87、§7.3 L229：提供空w清皮肤与按选项选肤；资源缺失转引WP15。（固定B；blob `81b14a0b09327bc030e5d9ef9f907089bd68cb82`）
- `deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md` · §3.1、§5.1、§7：有通用图像解析/包装失败，没有窗口默认候选链。（固定B；blob `23c487115d8b01638ed2db062546ef2a58abdc9f`）
- `deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md` · §5.2 L123–124：Speech/Menu Frame正常预览，但缺专属回退条件。（固定B；blob `5a4a629a56ef240de1c34b7e71d428def08a4737`）
- `deliverables/final-specification-set/generic-kernel/wp02-rule-configuration-and-data-variants.md` · 配置目录 SPEECH_WINDOWSKINS/MENU_WINDOWSKINS：仅表数量/角色，不提供回退选择。（固定B；blob `f0fed00b433c0e169b5e75f70f54d944009486a0`）

**参考实际行为**

未初始化的菜单/消息皮肤分别先解析选项指向的资源；未命中才解析系统登记名，再通用Graphics/System/Window，再Graphics/Windowskins/001-Blue01，最终为空。显式设置解析失败后记录空值，后续读取把它当已设置结果，不重新走冷读取回退。

**现规格的说法**

正式集从选项皮肤直接转引通用解析失败规则；未给这一专用搜索链，也未区分“尚未求默认”与“明确设置为空”。

**差异/缺口**

缺少可以独立决定备用皮肤身份的资源选择规则；即便准备相同可用素材，也无法由正式集确定结果。

**必要前提**

- 皮肤配置索引在范围内；初取的缓存未初始化；无插件。
- 所选皮肤缺失，系统登记名Custom有效，Custom与两个通用候选均可解析；图像加载正常。
- 显式设置对照独立开始，输入一个无法解析的皮肤名，后续只检查逻辑解析结果；不承诺已释放图像的实际画面。
- 显式设置对照指定完整逻辑资源位置，不假设任意裸名自动加目录；未提供选项对象时从配置首项开始。

**最小反例**

```json
{
  "input": "初取消息皮肤：选项资源Missing不存在、系统windowskin名Custom存在、System/Window和001-Blue01也存在。",
  "reference_output": "选择Custom；不返回nil，也不直接采用通用Window。",
  "distinguishing_alternative": "正式仅有通用“解析未命中nil”不足以确定这一身份选择。"
}
```

**正常对照**

所选皮肤能解析时直接使用，不尝试系统/通用备用。

**失败/边界对照**

- 系统名也不存在→System/Window；再缺→001-Blue01；全缺→空逻辑皮肤。
- 相同备用资源存在，显式设置Missing后读取仍为空；不再冷回退Custom。
- 消息中的空w标签直接清除皮肤，不应与显式设置不存在名称等同。

**独立实现影响**

默认UI在缺少一个皮肤资源时可能错误地选空白或选错备用；设置项的后续读取也可能错误恢复默认。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-searches.json",
    "search_ids": [
      "font_skin",
      "skin_fallback_exact"
    ],
    "scope": "全部131正式文件",
    "relevant_contexts_read": [
      "deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md §3.1/3.4/7.3",
      "deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md §3/5/7",
      "deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md §5.2",
      "deliverables/final-specification-set/generic-kernel/wp02-rule-configuration-and-data-variants.md 配置表",
      "deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md §失败边界"
    ],
    "result": "字体Arial、形态皮肤、编辑器Windowskins目录异常、w空标签及普通资源解析均不是本回退链；未见001-Blue01/System/Window或冷取与显式设置分层合同。"
  },
  "primary_relative_paths_base": "modules/M10",
  "independent_counterevidence": {
    "search_ids": [
      "CB-N02"
    ],
    "terms": [
      "皮肤|windowskin|001-Blue01|System/Window|Speech Frame|Menu Frame"
    ],
    "scope": "B 固定正式131篇，正文、scope、共享合同、附表和测试全部纳入；各检索文件字节与 git show B 相等",
    "contexts_actually_read": [
      "WP17 §3.1/3.4/7.3",
      "WP15 §3.1/5.1",
      "WP65 §5.1/5.2",
      "WP02配置表",
      "WP73-A §9/CE-M18；WP13命令131；MG05"
    ],
    "conclusion": "未发现默认候选身份链或未初始化与显式空结果的区别。通用解析nil、空文件名空白图、空w、未匹配配置名和编辑器目录失败都有各自前提，不能替代冷取。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CB"
}
```

**下一轮最小修订**

补默认菜单/消息皮肤候选优先级、每步存在性门、最终空结果与显式设置的区别；限定逻辑结果，不补造缺图后的像素恢复或新类结构。

**验收标准**

```json
[
  {
    "kind": "SPEC_STATIC",
    "criterion": "给出选项命中、系统命中、两个通用备用依次命中及全缺的结果。"
  },
  {
    "kind": "DERIVED_VECTOR",
    "criterion": "相同素材条件下，冷读取Missing得到Custom而显式设置Missing后读取为空，标未执行。"
  },
  {
    "kind": "SPEC_STATIC",
    "criterion": "空w标签保持原直接清空合同；不把逻辑空值等于所有既有窗口统一无皮肤。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md
- deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md
- deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md

**共享合同**

- WP02皮肤列表
- WP65皮肤预览

**依赖**

- WP17通用UI
- WP15资源访问
- 宿主输入/字体或媒体接口的条件前提

**能力范围引用**

- GR4-CAP-M10-004
- GR4-CAP-M10-015

**关联新问题**

无。

**根因身份**

```json
{
  "id": "GR4-M10-002-ROOT",
  "description": "缺少可以独立决定备用皮肤身份的资源选择规则；即便准备相同可用素材，也无法由正式集确定结果。"
}
```

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "third_round": null,
  "second_round": null,
  "note": "不猜第二轮ID，不据旧PASS判定本轮支持。",
  "independent_scope_assessment": {
    "relation": "new_within_reviewed_scope",
    "related_ids": [],
    "assessment": "未见与M01–M06同根。没有据历史PASS或旧政策确定完整性；不追认未知第二轮ID。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- DERIVED_VECTOR

**执行状态**

NOT_EXECUTED

**置信限定**

HIGH_STATIC

**未知**

- 所有皮肤图像缺失；无真实窗口验证。
- 显式换肤失败时先释放旧定制资源后的具体宿主画面未验证，未据此声称保持原画面或崩溃。
- 皮肤媒体和真实窗口未取得/未运行；空名称后既有窗口的实际呈现、旧资源释放效果不在本结论。
- 未来是否采用相同候选身份属于兼容政策，事实修订不预先决定。

**排除的主张**

- 不要求采用源类/方法/容器组织。
- 不修改参考或决定未来产品必须保留该兼容细节。
- 逻辑空资源名称不等于既有窗口必定清皮肤、保持旧图或必崩溃；这些真实像素与对象失效结果未证。

**用户政策边界**

```json
false
```

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CB",
    "thread_id": "01a13036-2ee9-7e43-8d09-4699ed1b03f4",
    "path": "modules/CB/verdicts.json",
    "pointer": "/records/1",
    "decision": "CONFIRM",
    "reason": "候选补的是按同一资源集合如何选择备用身份，而不是一般资源缺失标题。原报告已正确排除了空w与单窗设置的画面推论。P3限于缺资源时的默认选择及后续读取，非整个资源系统缺失。",
    "required_refinements": [],
    "execution_evidence_assessment": "该候选没有参考行为执行。原模块工具校验只证明产物结构/锚点等，不能证明本候选行为；CB未运行参考函数、行为模型、UI、输入或宿主。以下结果为源码/规格静态核对及条件化推导。",
    "historical_relation_assessment": {
      "relation": "new_within_reviewed_scope",
      "related_ids": [],
      "assessment": "未见与M01–M06同根。没有据历史PASS或旧政策确定完整性；不追认未知第二轮ID。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M10-003 · P2 · REQUIRED — 长无空格文本的超宽不逐字折行边界未被规格承接

领域 M10；分类 实现信息不足；独立审者 thread `01a12ff1-a1b1-7212-84b3-c3fdcd6552a9`；辅助证据目录 `modules/M10/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/007_Objects and windows/010_DrawText.rb` · 128–205;611–658;1035–1040：两格式化路径都需要非行首词边界才把整词移至下一行；无空格行首长串不会按字符拆行。（固定R；blob `2d6b723b705cc8ecabc6015e13d96359c3b16d81`）
- `Data/Scripts/007_Objects and windows/005_SpriteWindow_text.rb` · 316–347：普通消息将内容宽度传给格式化，依据生成的换行插暂停。（固定R；blob `e8be64d69b3bcb02def7a0cc09c0a5d4027cc628`）
- `Data/Scripts/016_UI/006_UI_Summary.rb` · 519–537;560–587;637：获得文本/地名进入宽268的格式化备忘录，源端不是专用长词换行器。（固定R；blob `8a7dff8b8b0d41a4fb9a405ea726fa06365b6e9b`）

**现规格依据**

- `deliverables/final-specification-set/user-interface/wp17-draw-text-tags.md` · §3、§6 L93：只描述显式对齐/换行，完整排版改为以绘制函数为准。（固定B；blob `0e643fe2440bc78ac6095d9e6fb4d15fca3994b0`）
- `deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md` · §3.3 L82：自动行满暂停示例含显式换行，未给自动宽度换行规则。（固定B；blob `81b14a0b09327bc030e5d9ef9f907089bd68cb82`）
- `deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md` · §5.2 L143–160：列长文本消费者字段，未给超宽词结果。（固定B；blob `04ecf28f8e63958ff848abce99e082736fdbf4c0`）

**参考实际行为**

在正常测量下，行首的一段连续非空白文本即使超过请求行宽，仍在同一逻辑行产生绘制项；不会按字符硬折行。有此前词边界的下一词超宽时可整词移到下一行；显式换行仍生效。这同时存在于无标记快路径和带格式标记的一般路径。 固定参考的换行宽度判定还预留额外2个同单位的测量量；需非行首词边界及对应内容条件成立才移词，不能概括为裸文字宽大于请求行宽。

**现规格的说法**

正式给出标签、行数/行满暂停和摘要字段；排版正文把完整换行算法留在参考绘制函数，没有实现无关的长词边界或案例。

**差异/缺口**

文本可见行为依赖未移交的分词/折行条件，独立实现无法区分自动逐字折行与保持超宽单行。

**必要前提**

- 有效位图/字体测量接口；默认允许自动折行；高度不限制行；无插件和图像/等待控制符。
- 静态测量夹具：A/B各宽8、空格宽4，请求行宽12；不声称真实Power Green有这些度量。
- 比较直接AB与A B；再以已识别无动作pg标签使同一文字走一般路径。
- 普通样式、起点x=0、非斜体、无额外描边，自动与显式换行均开启；高度不限制。<pg>只用于路径对照，比较逻辑行归属，不要求两个路径绝对纵坐标相同。

**最小反例**

```json
{
  "input": "行宽12、测量A=B=8，文本AB；独立对照A B（空格4）。",
  "reference_output": "AB仍只有一个文字行，B横向起点8；A B把B移至下一文字行。带pg标记仍有同样行归属差异。",
  "distinguishing_alternative": "常规逐字折行会把AB中的B移到下一行，改变消息后续行满暂停位置与摘要布局。"
}
```

**正常对照**

短文字在宽内保持一行；显式A换行B形成两行。

**失败/边界对照**

- 长无空格词/连续无空白本地化文本不硬拆行；只承诺生成的布局请求，不宣称屏外字形最终如何裁切。
- 有词边界的A B可整词移行；不能据此泛化任何长词都能装入宽度。
- 摘要备忘录固定宽度输入不增加额外滚动或长词策略；最终像素仍依赖字体和宿主。
- 同一度量A=8、B=8、ASCII空格=4，A B在行宽22保持一行、行宽21时B移下一行；此边界体现额外2单位，不是字体实测或裸宽比较。

**独立实现影响**

语言较长或无空格的文本可能产生不同的可见行数、被遮挡内容和暂停时点；仅凭现集需重新读源才能保持参考行为。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-searches.json",
    "search_ids": [
      "summary_particles",
      "long_text_wrap"
    ],
    "scope": "全部131正式文件",
    "relevant_contexts_read": [
      "deliverables/final-specification-set/user-interface/wp17-draw-text-tags.md §3/6",
      "deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md §3.3/6.3",
      "deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md §5.2",
      "deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md DT04/B04-M14",
      "deliverables/final-specification-set/generic-kernel/wp08-localization.md 非目标"
    ],
    "result": "命中的是显式换行、命令文本转换或编辑长度限制；DT04是对齐触发换行，B04-M14依赖显式换行。未见无空白长词/自动折行边界；§6明确留空不等于有可用净室合同。"
  },
  "primary_relative_paths_base": "modules/M10",
  "independent_counterevidence": {
    "search_ids": [
      "CB-N03",
      "CB-N03b"
    ],
    "terms": [
      "无空[格白]|长词|超宽|折行|自动换行|word.?wrap|wrap.?word|分词|行首|文本.{0,12}换行|换行.{0,12}文本|getFormattedText|B04-M14|DT04",
      "排版|折行|自动换行|word.?wrap|无空格|无空白|超宽|长文本|长词"
    ],
    "scope": "B 固定正式131篇，正文、scope、共享合同、附表和测试全部纳入；各检索文件字节与 git show B 相等",
    "contexts_actually_read": [
      "WP17绘制附表§3/§6；主文§3.3/§6.3",
      "WP66-A §5.2",
      "DT04、DT08、B04-M14",
      "WP08非目标；WP73-A文本长度；scope媒体限制"
    ],
    "conclusion": "未找到无空白串不硬折行或普通自动宽度换行的行为规则。显式换行、对齐换行、输入字数上限及文本转换是不同条件。附表转回参考绘制函数并不能让净室实现者推出AB/A B结果。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CB"
}
```

**下一轮最小修订**

补一个最小行为规则与两条测量夹具：基于词边界的自动折行、行首超宽连续串不硬拆、显式换行优先；说明消息/摘要消费，保留最终像素与未来改善策略自由。无需复写排版函数。

**验收标准**

```json
[
  {
    "kind": "SPEC_STATIC",
    "criterion": "说明无空白长串与含词边界文本的不同结果，不以参考函数名代替规则。"
  },
  {
    "kind": "DERIVED_VECTOR",
    "criterion": "AB、A B、显式换行、带pg四组独立夹具给行归属；注明测量是假定输入、未运行字体。"
  },
  {
    "kind": "SPEC_STATIC",
    "criterion": "不会把消息行满暂停/摘要坐标说明扩成保证所有长文本可见，也不要求逐像素复刻。"
  },
  {
    "kind": "SPEC_STATIC",
    "criterion": "明确额外2个测量单位及适用的词边界/内容门；补A B宽22不换、21换的独立对照，并限定普通样式和起点0。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md
- deliverables/final-specification-set/user-interface/wp17-draw-text-tags.md
- deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md
- deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md

**共享合同**

- WP08本地化后的文本消费
- 消息行满暂停
- 摘要备忘录

**依赖**

- WP17通用UI
- WP15资源访问
- 宿主输入/字体或媒体接口的条件前提

**能力范围引用**

- GR4-CAP-M10-006
- GR4-CAP-M10-020

**关联新问题**

无。

**根因身份**

```json
{
  "id": "GR4-M10-003-ROOT",
  "description": "文本可见行为依赖未移交的分词/折行条件，独立实现无法区分自动逐字折行与保持超宽单行。"
}
```

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "third_round": null,
  "second_round": null,
  "note": "不猜第二轮ID，不据旧PASS判定本轮支持。",
  "independent_scope_assessment": {
    "relation": "new_within_reviewed_scope",
    "related_ids": [],
    "assessment": "M01的本地化参数替换发生在上游文本结果层；本项固定AB输入后的布局，互不合并。没有把旧行满暂停已承接合同重开。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- DERIVED_VECTOR

**执行状态**

NOT_EXECUTED

**置信限定**

HIGH_STATIC

**未知**

- 真实宿主/媒体/输入未运行；未推断完整Demo可达。
- 真实宿主、媒体、物理输入与完整Demo未执行；外部插件不在固定R证明范围。

**排除的主张**

- 不要求全字符排版算法逐行翻译。
- 不声称默认中文文本、所有长字符串都会实际丢字；字体测量和宿主裁切未运行。
- 不把固定摘要坐标要求成未来框架布局架构。

**用户政策边界**

```json
false
```

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CB",
    "thread_id": "01a13036-2ee9-7e43-8d09-4699ed1b03f4",
    "path": "modules/CB/verdicts.json",
    "pointer": "/records/2",
    "decision": "CONFIRM_WITH_REFINEMENT",
    "reason": "原AB/A B最小反例成立，且消息消费者会依据布局换行插入暂停，故不是要求逐像素复刻。须收紧拟补规则的宽度阈值；只写“超过请求行宽”可能漏掉刚好容纳文字却仍换行的边界。保持P2，精确化并不推翻原缺口，也不另立根因。",
    "required_refinements": [
      "拟补自动折行规则须注明固定参考会预留额外2个测量单位，只有非行首词边界及相应内容条件成立时移词；不得概括为裸文本宽大于行宽才折行。",
      "向量明确普通样式、起点0、自动折行开启和测量夹具；<pg>对照比较逻辑行归属，不宣称两个内部路径绝对像素相同。",
      "正文仅登记固定参考的不硬拆长词行为；未来改善无空格语言排版属于独立兼容政策。"
    ],
    "execution_evidence_assessment": "该候选没有参考行为执行。原模块工具校验只证明产物结构/锚点等，不能证明本候选行为；CB未运行参考函数、行为模型、UI、输入或宿主。以下结果为源码/规格静态核对及条件化推导。",
    "historical_relation_assessment": {
      "relation": "new_within_reviewed_scope",
      "related_ids": [],
      "assessment": "M01的本地化参数替换发生在上游文本结果层；本项固定AB输入后的布局，互不合并。没有把旧行满暂停已承接合同重开。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M10-004 · P2 · REQUIRED — 战斗动画的类型默认映射只有表名和查找顺序，缺少可消费数据

领域 M10；分类 数据或资源契约缺口；独立审者 thread `01a12ff1-a1b1-7212-84b3-c3fdcd6552a9`；辅助证据目录 `modules/M10/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb` · 412–485：18类型×6槽明确指定默认招式身份，未映射按本格/对应单目标/变化/TACKLE回退。（固定R；blob `5df4c2c08d2bcca3063ad9fd104d33df37e75cb7`）
- `Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb` · 492–518：普通动画调用真实消费查找结果；有动画才进入播放。（固定R；blob `5df4c2c08d2bcca3063ad9fd104d33df37e75cb7`）
- `Data/Scripts/011_Battle/001_Battle/001_Battle.rb` · 838–843：正常战斗域包装在showAnims为真调用场景播放。（固定R；blob `ce89d430743e1c1a27e8aab603fdc3be60288fed`）
- `Data/Scripts/010_Data/002_PBS data/005_Move.rb` · 22–55;79–96：登记type/category/target决定分格；raw category与世代physical?/special?不同入口。（固定R；blob `47949c4ca821c591957cbf4ecea370fa6c7f41f6`）
- `Data/Scripts/010_Data/001_Hardcoded data/017_Target.rb` · 26–33;136–141：NearOther目标数1；目标数量/敌侧属性参与分格。（固定R；blob `b00c9a22be53f3cacffaf1d11c4c15e02550a769`）
- `Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb` · 39–53：映射与数据库加载分层，可用缓存为条件。（固定R；blob `b6bddb6730dfa407e3691653a1e7ffa7d50c1812`）
- `PBS/moves.txt` · FLAMETHROWER2603–2613;EMBER2782–2792;SUNNYDAY2819–2827;TACKLE5326–5336：默认数据支持火系特殊单目标样本及回退身份存在。（固定R；blob `fa5dbaf2739b6b6f55ba5cc5d7d599b4a15b68ca`）

**现规格依据**

- `deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md` · §9.4 L251–254：称类型默认表并定义六槽/回退骨架，没有表内容。（固定B；blob `f4167d75f73bb10ac7729ee96dea6aa6de780ffe`）
- `deliverables/final-specification-set/demo-dx/wp74-battle-animation-authoring-and-exchange.md` · §15 L396–399：关联编译与播放侧再次引用同一缺表。（固定B；blob `42b214af3267436755339815ced7d67f67a3add1`）
- `deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md` · BT K36：只给全部缺失的结果，无法确定正常默认命中的身份。（固定B；blob `5dbb1fbed36800c39844a549939b5123c4b3c1c5`）
- `deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md` · §非注册表产物 L67：move2anim产物身份不能替代脚本内的类型默认映射。（固定B；blob `c6623b3200cd2a7ee16af96dd02f628076f423e0`）

**参考实际行为**

例：FLAMETHROWER无精确映射时按其火系特殊单目标格选择EMBER映射；EMBER亦无映射时再尝试火系变化默认SUNNYDAY，最后TACKLE。各被选默认身份在对方侧也优先OppMove再普通映射。默认表含18类型、每类六槽及空槽。

**现规格的说法**

给出“查类型默认表”和查找链，但全正式集未提供该表的身份数据；WP74只是回指，不能确定火系特殊对应EMBER。

**差异/缺口**

缺少决定最终资源身份的固定默认内容；算法名和六槽结构不能代替数据。

**必要前提**

- 普通战斗动画开启，无插件，合法FLAMETHROWER/默认type-category-target记录。
- 已正常得到双方映射与动画集合（条件夹具），FLAMETHROWER无精确映射；EMBER、SUNNYDAY、TACKLE映射指向不同有效动画槽。
- hitNum=0；实际媒体存在/内容不用于证明查找结果，未加载二进制动画。
- 映射10/20/30及对方11均为条件夹具中的有效槽，不是默认媒体真实编号；双方映射容器均有效，排除容器异常的局部救援空结果。

**最小反例**

```json
{
  "input": "己方FLAMETHROWER精确映射空；EMBER→10、SUNNYDAY→20、TACKLE→30；三槽均有效。",
  "reference_output": "选择槽10（EMBER）；删EMBER映射则槽20；再删SUNNYDAY则槽30；全部删才空。",
  "distinguishing_alternative": "只凭当前正式集无法在火系的EMBER、FIREPUNCH或其他默认身份中作出唯一选择。"
}
```

**正常对照**

FLAMETHROWER精确映射存在时直接使用它；这一骨架已有正文支持。

**失败/边界对照**

- 对方侧EMBER存在OppMove→11且普通→10时选11；对方项空才选10。
- 默认身份未登记或该候选无映射时继续；不把资源/数据库存在性与映射选择合并。
- 世代物理/特殊机制变化不自动重写raw类别的动画分格；无需假定全部世代运行已验证。

**独立实现影响**

实现者即使拥有相同动画库和招式数据也无法按正式规格选择相同默认动画，作者为新招式省略专用动画时表现不确定。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-searches.json",
    "search_ids": [
      "animation_defaults"
    ],
    "scope": "全部131正式文件",
    "relevant_contexts_read": [
      "deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md §9.4",
      "deliverables/final-specification-set/demo-dx/wp74-battle-animation-authoring-and-exchange.md §15/16",
      "deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md L67",
      "deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md K35–36"
    ],
    "result": "语义相关命中只有WP67-A表名/骨架、WP74前向引用、加载产物说明和缺失测试；FIREPUNCH/EMBER等表成对标识搜索无映射表。钓鱼公共事件回退和Safari数据是其他功能。"
  },
  "primary_relative_paths_base": "modules/M10",
  "independent_counterevidence": {
    "search_ids": [
      "CB-N04",
      "CB-N04b"
    ],
    "terms": [
      "类型默认|默认.{0,16}动画|动画.{0,16}(默认|回退)|move2anim|EMBER|FIREPUNCH|SUNNYDAY|OppMove|K36",
      "火花|火焰拳|喷射火焰|类型.{0,15}动画|动画.{0,15}(火系|物理|特殊|变化)|单目标物理|多目标特殊|typeDefaultAnim"
    ],
    "scope": "B 固定正式131篇，正文、scope、共享合同、附表和测试全部纳入；各检索文件字节与 git show B 相等",
    "contexts_actually_read": [
      "WP67-A §9.4",
      "WP74 §15/§16",
      "WP03非类产物/交界表；WP04 §5.1",
      "K35/K36；中英文火系身份别名及类型/动画交叉匹配"
    ],
    "conclusion": "实质动画命中只有表名/查找骨架、作者命名编译和全落空测试；英文身份或中文别名的其它命中属于招式效果、天气、钓鱼或演出目录，没有默认类型到身份的可用附表。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CB"
}
```

**下一轮最小修订**

以实现无关附表补18类型×六种用途到默认招式身份/空值的映射，说明原始类别/目标分格与候选存在性门；增加正常默认命中和逐级落空对照。不要复制Ruby表表达式或设计播放类。

**验收标准**

```json
[
  {
    "kind": "SPEC_STATIC",
    "criterion": "正式交付包含完整默认类型映射数据及六槽含义，能独立解析身份。"
  },
  {
    "kind": "DERIVED_VECTOR",
    "criterion": "火系特殊10→20→30→空及OppMove11优先案例给明确输入/输出且NOT_EXECUTED。"
  },
  {
    "kind": "SPEC_STATIC",
    "criterion": "保持精确映射hitNum、默认候选查找、动画数据库/媒体缺失分层；不把结构校验称播放测试。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md
- deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md

**共享合同**

- WP74动画命名编译
- WP03动画产物
- 战斗showAnims开关

**依赖**

- WP17通用UI
- WP15资源访问
- 宿主输入/字体或媒体接口的条件前提

**能力范围引用**

- GR4-CAP-M10-027

**关联新问题**

无。

**根因身份**

```json
{
  "id": "GR4-M10-004-ROOT",
  "description": "缺少决定最终资源身份的固定默认内容；算法名和六槽结构不能代替数据。"
}
```

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "third_round": null,
  "second_round": null,
  "note": "不猜第二轮ID，不据旧PASS判定本轮支持。",
  "independent_scope_assessment": {
    "relation": "new_within_reviewed_scope",
    "related_ids": [],
    "assessment": "M01–M06无同根。M12动画作者域没有相同候选；WP74命名编译是共享前置，不与默认选择数据合并。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- DERIVED_VECTOR

**执行状态**

NOT_EXECUTED

**置信限定**

HIGH_STATIC

**未知**

- Data/move2anim.dat与PkmnAnimations.rxdata在参考材料中不可用；未反序列化。
- 本文映射号10/20/30/11是条件静态夹具，不代表默认素材库实际编号。
- 参考材料缺可用move2anim/动画集合及媒体；映射槽号为静态夹具，未加载二进制或播放。
- 未来是否采用相同默认身份是政策问题，不由本事实审计决定。

**排除的主张**

- 不要求采用源类/方法/容器组织。
- 不修改参考或决定未来产品必须保留该兼容细节。

**用户政策边界**

```json
false
```

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CB",
    "thread_id": "01a13036-2ee9-7e43-8d09-4699ed1b03f4",
    "path": "modules/CB/verdicts.json",
    "pointer": "/records/3",
    "decision": "CONFIRM",
    "reason": "六槽的名字不能唯一决定火系特殊单目标采用EMBER；没有别处数据可推出这一身份。默认缺专用映射是明示支持的普通查找分支，补完整固定映射是数据合同修订，不是抄写源表表达式或规定新播放架构。P2维持。",
    "required_refinements": [],
    "execution_evidence_assessment": "该候选没有参考行为执行。原模块工具校验只证明产物结构/锚点等，不能证明本候选行为；CB未运行参考函数、行为模型、UI、输入或宿主。以下结果为源码/规格静态核对及条件化推导。",
    "historical_relation_assessment": {
      "relation": "new_within_reviewed_scope",
      "related_ids": [],
      "assessment": "M01–M06无同根。M12动画作者域没有相同候选；WP74命名编译是共享前置，不与默认选择数据合并。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M11-001 · P2 · REQUIRED — 图鉴预览和条目固定请求普通外观的消费规则未进入正式合同

领域 M11；分类 实现信息不足；独立审者 thread `01a13017-c27c-7020-a9f8-9bb66eb74f64`；辅助证据目录 `modules/M11/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb` · 195–227：首次登记和最近见到均可保留异色true（固定R；blob `fb3afe4df6443fd2704958a4ed4664f793c6299f`）
- `Data/Scripts/016_UI/003_UI_Pokedex_Main.rb` · 264–295、417–448、766–768：选中物种预览读取性别/形态，固定普通外观（固定R；blob `536002291f1eb837ab5173933b87c5ea31a5c3a0`）
- `Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb` · 5–67、71–116、139–151、582–617：完整、摘要单种及简略入口均复用固定普通外观刷新；Info、Forms前/后/图标请求false（固定R；blob `c2b43b0ed024526681dc0ecd5d56dbaa8affd972`）
- `Data/Scripts/014_Pokemon/001_Pokemon-related/003_Pokemon_Sprites.rb` · 64–68、253–258：外观参数透传至资源选择（固定R；blob `12da4a054e9cd244039c75e3b427153a676d4c0c`）
- `Data/Scripts/010_Data/002_PBS data/009_Species_files.rb` · 3–34、47–52、86–89、118–120：普通请求不尝试异色目录（固定R；blob `2a2e2fb92e7c05ec3b2f586edfda64cd4eeeaba3`）

**现规格依据**

- `deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md` · ：本次读取的对应行为条款（固定B；blob `664778d344a13628f2f313d9ee62f6bacf020bc7`）
- `deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md` · ：本次读取的对应行为条款（固定B；blob `6054d7b6e30812d922af092fc55bbb0a5e88e509`）
- `deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md` · ：本次读取的对应行为条款（固定B；blob `23c487115d8b01638ed2db062546ef2a58abdc9f`）
- `deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md` · ：本次读取的对应行为条款（固定B；blob `5dbb1fbed36800c39844a549939b5123c4b3c1c5`）
- `deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md` · ：本次读取的对应行为条款（固定B；blob `9561dc1abc078cc26b98caf4480a3cbea5a70847`）

**参考实际行为**

图鉴保留seen-form及末次形态中的异色记录，但主列表选中物种预览与条目刷新只消费保存的性别/形态，图像选择固定为普通外观。完整Info/Forms前图、背图、Forms物种图标及获得后的简略Info同样处理；没有异色浏览切换。普通刷新本身不把末次记录的true改false，进入形态选择器的首轮写入是另一条已经记载的副作用。

**现规格的说法**

WP62描述异色维度与末次三元组、展示消费者；WP66-B说明图像/形态展示及选择器三参写入导致异色默认false，但没有规定选择器以外的图像请求固定false。WP15只给按已提供属性的资源选择与回退。

**差异/缺口**

仅依正式集合不能确定末次异色true时应请求普通还是异色图像；现有通用资源合同允许两种调用方输入，无法唯一复现参考。

**必要前提**

- 固定R，无插件或临时外部改写；合法已见/已拥有BULBASAUR雄性形态0，末次形态为[0,0,true]。可由合法异色个体登记/最近见到形成，不要求执行真实事件。
- 普通图鉴入口资格、地区/物种/metrics/消息/输入/宿主成立；用于区分视觉的假设资源同时提供相互不同的普通和异色前图/背图/图标。本轮这些媒体实际不可得。
- 先检查普通预览和Info，未进入Forms选择器；以直接符合条件的简略条目入口作另一个独立夹具。
- 最小BULBASAUR夹具先不进入形态选择器；若验证首轮另写异色false，另设>1可列形态的独立夹具，不能用单项个体证明该分支。

**最小反例**

```json
{
  "input": "上述末次异色true，打开主列表选中BULBASAUR，随后打开完整Info；不调用形态选择器。",
  "reference": "两处请求普通前图；保存末次异色仍true。独立简略Info同样请求普通前图。",
  "alternative_allowed_by_current_spec": "实现方把末次三元组完整传给通用资源服务，从而显示异色；数据/资格/形式切换描述都可满足，视觉仍偏离R。",
  "evidence_level": "DERIVED_VECTOR",
  "execution_status": "NOT_EXECUTED"
}
```

**正常对照**

相同输入只有末次异色false：仍请求普通外观；读取性别、形态和已见/拥有资格不变。

**失败/边界对照**

仅异色见过可满足形态资格，图像仍普通；若没有普通/通用图而只有异色图，普通请求不据保存true改查异色，最终依WP15普通请求回退/无图合同，不臆测宿主崩溃。进入多项形态选择器后首轮会另将末次异色写false，此已有合同不可冒充进入前的消费规则。

**独立实现影响**

玩家仅见到/获得异色后首次打开图鉴，就可能看到与参考不同的外观；错误会贯穿列表预览、完整条目和简略条目，并可能把正确的异色记录误清除来达到普通显示。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-evidence.json",
    "scope": "all 131 formal Markdown files including appendices, tests and scope",
    "queries": [
      "(图鉴|Pokédex|Pokedex).{0,80}(普通|异色|闪光|shiny)",
      "(异色|闪光|shiny).{0,80}(图鉴|Pokédex|Pokedex)",
      "(忽略|丢弃|固定|强制|不显示|不展示).{0,40}(异色|闪光|shiny)",
      "(普通外观|普通配色|非闪光|non.?shiny)",
      "(last_form_seen|pbUpdateDummyPokemon|setIconBitmap)"
    ],
    "result": "未找到图鉴选中预览/条目图像固定普通外观的承接。命中记录写入、调试登记、摘要红编号、邮件个体快照及通用资源回退，均不补足本调用方的固定参数。",
    "source_counter_search": {
      "scope": "R/Data/Scripts 全部脚本",
      "terms": [
        "class PokemonPokedexInfo_Scene",
        "def pbUpdateDummyPokemon",
        "def setIconBitmap",
        "shiny",
        "DEX_SHOWS_ALL_FORMS"
      ],
      "result": "本固定脚本集只定位这两处图鉴消费者定义；直接读取入口调用和取图透传，未见后续覆写或配置改为采用保存的异色字段。插件未取得、不推断不存在。"
    }
  },
  "primary_relative_paths_base": "modules/M11",
  "independent_counterevidence": {
    "search_ids": [
      "CB-N05",
      "CB-N05b"
    ],
    "terms": [
      "(图鉴|Pokédex|Pokedex).{0,100}(普通|异色|闪光|shiny)|(异色|闪光|shiny).{0,100}(图鉴|Pokédex|Pokedex)|普通外观|普通配色|非闪光|non.?shiny|last_form_seen|pbUpdateDummyPokemon|setIconBitmap",
      "异色|闪光|shiny|末次形态|最近形态|最近见到|最后.*形态"
    ],
    "scope": "B 固定正式131篇，正文、scope、共享合同、附表和测试全部纳入；各检索文件字节与 git show B 相等",
    "contexts_actually_read": [
      "WP62 §2/§3/§4/§6 与 PD03–05/PD19/PD31–34",
      "WP66-B §6/§7，B30/B33/B38",
      "WP15 §4.1；WP17共享图标",
      "WP66-A邮件/摘要；WP21形态提交"
    ],
    "conclusion": "记录异色、通用资源闪光参数、摘要红编号、邮件快照以及Forms选择器首轮写false都有明文；均不能推出未进入选择器的主预览/Info固定请求普通且保持末次true。跨行异色/末次别名补检也未找到该调用方规则。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CB"
}
```

**下一轮最小修订**

在WP62记录→展示交界及WP66-B列明哪些图像请求固定普通外观，保留性别/形态选择和异色记录；明确普通刷新不清记录、Forms选择器才有既有写入。补true/false成对静态向量，并为完整/简略入口交叉引用。只补参考事实，不要求未来沿用同名方法/对象，不自行决定是否改进异色浏览政策。

**验收标准**

```json
[
  {
    "kind": "STATIC",
    "criterion": "仅读正式集合即可判定末次异色true时主列表选中预览、完整Info/Forms前后图及图标、简略Info均请求普通外观。"
  },
  {
    "kind": "STATIC",
    "criterion": "普通预览/Info刷新不改变保存的异色true；与进入Forms选择器首轮写false的已有合同明确分开。"
  },
  {
    "kind": "STATIC",
    "criterion": "有同性别/形态的末次true/false成对向量，及仅异色已见的形态资格对照；不将资源回退误作固定普通选择的原因。"
  },
  {
    "kind": "STATIC",
    "criterion": "不改WP15通用按属性取图合同，不把规则推广到队伍/摘要/战斗个体外观；新向量标记未执行。"
  },
  {
    "kind": "RUNTIME_OPTIONAL",
    "criterion": "不以当前无媒体/宿主阻止事实修订；如后来运行，应另提供正常/异色相异资源、命令输入及实际输出记录，不能把本轮静态推导标成执行。"
  },
  {
    "kind": "SPEC_STATIC",
    "criterion": "普通刷新保留true/false原记录与多项Forms选择器首轮写false分开；多项选择器反向例需独立合法多项夹具。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md
- deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md
- deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md
- deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md

**共享合同**

- WP62记录消费
- WP66-B图鉴UI
- WP15通用物种图像参数与回退；不要求修改通用规则

**依赖**

- 图鉴普通登记/最近见到
- 物种图像与图标资源选择
- 完整/简略条目入口

**能力范围引用**

- GR4-CAP-M11-006

**关联新问题**

无。

**根因身份**

M11-pokedex-record-versus-image-variant

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "third_round": null,
  "second_round": null,
  "note": "GR3-M11-001仅栖息地掩码，独立回归仍支持CLOSED；本项不是重开。未知第二轮关联不猜ID。",
  "independent_scope_assessment": {
    "relation": "new_within_reviewed_scope",
    "related_ids": [
      "GR3-M11-001"
    ],
    "assessment": "旧栖息地格规则与本次资源请求无同根。M04个体取图动态形态与本项共享资源文件，但前者读取个体并可能提交形态，后者只消费记录的性别/形态且固定异色假；不合并。M10未另报同项，WP66-B只是投影。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- DERIVED_VECTOR

**执行状态**

NOT_EXECUTED

**置信限定**

HIGH_STATIC

**未知**

- 实际图像像素、媒体/宿主效果
- 未来产品是否主动提供异色浏览的政策取舍
- 外部插件行为
- 真实宿主、媒体、物理输入与完整Demo未执行；外部插件不在固定R证明范围。

**排除的主张**

- 不声称图鉴不记录异色
- 不声称普通刷新清除末次异色
- 不把主列表预览误称每行拥有标记图标
- 不声称真实地图/事件已可达或运行成功
- 不判定参考固定普通外观是应修复的游戏bug

**用户政策边界**

```json
false
```

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CB",
    "thread_id": "01a13036-2ee9-7e43-8d09-4699ed1b03f4",
    "path": "modules/CB/verdicts.json",
    "pointer": "/records/4",
    "decision": "CONFIRM",
    "reason": "独立确认的是记录→资源请求交界缺口。通用按属性资源规则可接受true/false两种输入；现有记录与选择器条款没有规定选择器以外传入固定false。不是图鉴不记录异色，也不是每行拥有标记图标的颜色问题。P2针对多正常入口的可见外观差异。",
    "required_refinements": [],
    "execution_evidence_assessment": "该候选没有参考行为执行。原模块工具校验只证明产物结构/锚点等，不能证明本候选行为；CB未运行参考函数、行为模型、UI、输入或宿主。以下结果为源码/规格静态核对及条件化推导。",
    "historical_relation_assessment": {
      "relation": "new_within_reviewed_scope",
      "related_ids": [
        "GR3-M11-001"
      ],
      "assessment": "旧栖息地格规则与本次资源请求无同根。M04个体取图动态形态与本项共享资源文件，但前者读取个体并可能提交形态，后者只消费记录的性别/形态且固定异色假；不合并。M10未另报同项，WP66-B只是投影。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M12-001 · P3 · REQUIRED — 遭遇整集复制未承接空类型被丢弃而步数率保留的边界

领域 M12；分类 数据或资源契约缺口；独立审者 thread `01a12ffe-6148-76d0-8038-a1eb8e8bf390`；辅助证据目录 `modules/M12/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb` · 69–99;139–154;187–234;256–339：整集复制全部步数率但跳过空类型；单类型复制始终建立目标类型；正常新类型可零槽返回（固定R；blob `97c7f39247411587d204a432eb5f7c99b76769e5`）
- `Data/Scripts/010_Data/002_PBS data/013_Encounter.rb` · 62–68：初始化直接接收概率和类型，不补回遗漏键（固定R；blob `e69d300dd0e21690e5970452017e4c2bd457021a`）
- `Data/Scripts/010_Data/001_GameData.rb` · 78–85：登记只建立记录（固定R；blob `ccfd971a29b3bab107e2da6865ac0050ed3256b0`）
- `Data/Scripts/010_Data/001_Hardcoded data/013_EncounterType.rb` · 29–33：Land默认率21（固定R；blob `79cbafb8bd3e5e827cd09b6ca070a13bb70d94aa`）
- `Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb` · 1163–1169：调试菜单直接调用遭遇编辑器，未另加数据清理（固定R；blob `6dd0c35a31040174efadefa2ba24a1c85a2499f9`）
- `Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb` · 423–438：空槽类型在后续PBS写出也会省略，但这是另一步（固定R；blob `be1b3de320d0635d7eca1e24332973344188b53c`）

**现规格依据**

- `deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md` · §6.1 line73/§6.2 line80：本次核对条款（固定B；blob `f75fa5a23f157f434e3e57da69757e4a429a0edc`）
- `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md` · WE-M11 line85：本次核对条款（固定B；blob `255464a58f8e45e30ca1807250926aa47e0791a6`）
- `deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md` · §6.4 line91：空槽类型不输出限定PBS往返，未覆盖编辑器Copy（固定B；blob `f75fa5a23f157f434e3e57da69757e4a429a0edc`）

**参考实际行为**

正常作者流程新增遭遇类型后可不加槽直接返回，源集仍显示该类型(x0)。整集Copy逐项复制所有步数率，但不为零槽类型建立目标类型条目；目标只剩该率而无该类型，原集不变。单类型Copy不同：即使源零槽也先建目标空类型。

**现规格的说法**

WP73-B§6.1只说明复制步数率和各槽内容、保持编辑独立及后缀；WE-M11无输入限制地称深拷贝。没有说明空类型不复制和步数率残留；§6.4的空槽省略专指随后PBS写出。

**差异/缺口**

一个可由正常编辑流程到达的结构过滤分支未明确，独立实现通常会保留空类型，从而与参考的目标编辑列表/可新增类型集合不同。

**必要前提**

- 固定R、调试菜单或合法直接编辑入口，合法地图列表和窗口宿主
- 原集地图5版本0，Land已注册且步数率21，槽数0（新增类型后立即BACK可达）
- 目标地图7版本1未占用；Copy成功，尚未退出总保存门；无插件/外部修改

**最小反例**

```json
{
  "input": "原集仅含Land类型(0槽)、Land率21，整集复制至空闲(7,1)",
  "reference_output": "原集保留Land(0槽)；目标类型列表没有Land，而步数率仍有Land=21，后缀保留。打开目标可再次新增Land。",
  "naive_spec_output": "按WE-M11无条件深拷贝，目标也显示Land(0槽)，新增类型列表排除Land。",
  "evidence_level": "DERIVED_VECTOR",
  "execution_status": "NOT_EXECUTED"
}
```

**正常对照**

Land含一个合法非空槽时复制保留类型和独立槽副本；同图同版本冲突仍拒绝。

**失败/边界对照**

这是合法空槽边界而非异常。反向对照：在同一集把空Land类型复制到未用Cave类型，参考保留Cave空类型及复制率。复制本身仅登记，退出No仍按原档案重载；不声称产生真实遇敌差异。

**独立实现影响**

编辑器复制结果、类型(x0)显示、可再次新增类型的集合以及保存的登记结构可不同；不影响已有非空槽复制正常结论，限P3。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-evidence-search.json",
    "scope": "全部131正式Markdown含正文/附表/测试",
    "terms": [
      "遭遇集|encounter set|pbEncountersEditor|WE-M11",
      "空槽类型|空类型|空遭遇|empty encounter|empty.{0,20}slots?",
      "复制.{0,25}(遭遇|步数率)|遭遇.{0,25}(复制|拷贝)|Copy.{0,25}encounter"
    ],
    "contexts_reviewed": [
      "WP73-B§6.1–6.5/§10–11",
      "WE-M11–13",
      "WP04遭遇概率往返",
      "WP36空表/编译/快照合同"
    ],
    "result": "没有条款说明整集Copy丢空类型但留概率；查得空槽省略只在PBS输出。源端检查唯一编辑定义、菜单caller、登记构造及单类型Copy，未发现补回空键的路径。"
  },
  "primary_relative_paths_base": "modules/M12",
  "independent_counterevidence": {
    "search_ids": [
      "CB-N06",
      "CB-N06b"
    ],
    "terms": [
      "遭遇集|encounter set|pbEncountersEditor|WE-M11|空槽类型|空类型|空遭遇|empty.{0,20}(encounter|slot)|复制.{0,25}(遭遇|步数率)|遭遇.{0,25}(复制|拷贝)|Copy.{0,25}encounter",
      "(遭遇|类型|步数率|触发概率).{0,30}(空|复制|拷贝|过滤)|(空|复制|拷贝|过滤).{0,30}(遭遇|类型|步数率|触发概率)|WE-M1[123]"
    ],
    "scope": "B 固定正式131篇，正文、scope、共享合同、附表和测试全部纳入；各检索文件字节与 git show B 相等",
    "contexts_actually_read": [
      "WP73-B §6.1–6.5/§10–11",
      "WE-M10–14",
      "WP04 §5.5",
      "WP36 §3.1–3.2.1/§9",
      "WP73-A空集合与校验分界"
    ],
    "conclusion": "未找到整集Copy滤空类型但保留率的条款。WP04/WP73-B省空类型明确是PBS输出，WP36空表是运行消费者。WE-M11无非空前提的深拷贝表述无法唯一得出目标列表无Land。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CB"
}
```

**下一轮最小修订**

在WP73-B整集Copy条款补充零槽类型不建立目标条目、概率照复制；显式区分单类型Copy。限定WE-M11非空正例并补一条空类型与概率残留静态对照。保持参考事实，未来保留或修正该行为由后续政策选择，不修参考。

**验收标准**

```json
[
  {
    "kind": "static",
    "criterion": "整集空Land21复制后原集不变、目标无Land类型而Land率21存在；保留后缀和未保存状态层次。"
  },
  {
    "kind": "static",
    "criterion": "给出非空Land独立复制和单类型空Land→Cave仍保留空类型的反向对照。"
  },
  {
    "kind": "static",
    "criterion": "不把PBS写出时省空类型当成本次编辑Copy行为，不扩大为运行/遇敌差异。"
  },
  {
    "kind": "runtime",
    "criterion": "本修订验收不要求宿主运行；若后来执行必须独立记宿主/素材/夹具，不冒用本轮证据。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md
- deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md

**共享合同**

- WP04 PBS反写与WP36当前地图快照只作相邻消费；无需修改其正确规则

**依赖**

- WP73-A通用选择器
- GameData遭遇登记
- WP72编辑器入口

**能力范围引用**

- GR4-CAP-M12-005

**关联新问题**

无。

**根因身份**

M12-encounter-set-copy-empty-type-filter

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "gr3_related_ids": [],
  "second_round_relation": null,
  "note": "GR3-M12-001/002为BMP与结算累计，不同根因；不重开历史CLOSED。第二轮关联未追认。",
  "independent_scope_assessment": {
    "relation": "new_within_reviewed_scope",
    "related_ids": [
      "GR3-M12-001",
      "GR3-M12-002"
    ],
    "assessment": "BMP材料与评级累计是不同根因。M01–M06无编辑器整集筛空候选，不与翻译逐项合并、遗传或运行遭遇规则合并；不重做旧回归签署。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- DERIVED_VECTOR

**执行状态**

NOT_EXECUTED

**置信限定**

high on source branch; bounded P3 documentation sufficiency judgment

**未知**

- 当前完整编辑器宿主表现未运行
- 是否有下游自定义插件补回类型未知
- 真实宿主、媒体、物理输入与完整Demo未执行；外部插件不在固定R证明范围。

**排除的主张**

- 不宣称参考必须修bug
- 不宣称所有Copy错误或会丢非空槽
- 不宣称当前地图遇敌率立即改变
- 不把当前缺完整Demo归为本发现缺能力

**用户政策边界**

```json
false
```

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CB",
    "thread_id": "01a13036-2ee9-7e43-8d09-4699ed1b03f4",
    "path": "modules/CB/verdicts.json",
    "pointer": "/records/5",
    "decision": "CONFIRM",
    "reason": "原报告的有效输入可通过编辑器正常新增/立即返回得到；没有登记构造或caller补回被滤掉类型。缺口有限且不影响非空复制正确规则，P3维持；无需把参考过滤当作未来引擎永久要求。",
    "required_refinements": [],
    "execution_evidence_assessment": "本候选为SOURCE_STATIC/SPEC_STATIC/DERIVED_VECTOR，未执行。另读M12 rating-probe.rb及rating-execution.json：回执是Ruby2.6.10隔离评级/结算，绕过队伍构造，无编辑器调用，不支持本候选也不是随附Ruby3.1宿主实测。CB只评价该回执可支持范围，不重跑或重新认证其数值。",
    "historical_relation_assessment": {
      "relation": "new_within_reviewed_scope",
      "related_ids": [
        "GR3-M12-001",
        "GR3-M12-002"
      ],
      "assessment": "BMP材料与评级累计是不同根因。M01–M06无编辑器整集筛空候选，不与翻译逐项合并、遗传或运行遭遇规则合并；不重做旧回归签署。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

## 5. 有限批次、唯一写者与依赖

五个作者批的正式写集合两两不交，可以在同一固定输入上并行。每批仅一个正式写者；额外协作者只能做独立只读准备并在自己的证据目录写建议。R4-U03合并了共享WP15与两测试目录的7项，避免跨作者争写。源R和所有旧接受材料共享只读，不按源文件目录设计未来类/包。

实际整合与登记由唯一ROOT串行执行U01→U02→U03→U04→U05。候选审查、真实整合、实际复审和接受是不同状态；后续只读准备可以并行，不得提前关闭具有未满足依赖的ID。任何当前文件漂移都要绑定具体后继SHA和差异，不能偷换B。

### R4-U01 内容文本与通用辅助

唯一作者 `R4-U01-author`；主责ID：GR4-M01-001、GR4-M01-002、GR4-M02-001、GR4-M02-002、GR4-M02-003。

**允许写的正式路径**

- deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md
- deliverables/final-specification-set/generic-kernel/wp07-diagnostics-files-http.md
- deliverables/final-specification-set/generic-kernel/wp08-localization.md
- deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md

**开始门**：核验最终handoff绑定、固定B/R与当前漂移；保护既有修改；独立分支/工作树；读取本批完整finding及关联旧范围。

**写入边界**：只修具名finding条款/数据/向量及必要交叉引用，不整篇重写、不改已正确规则。新增正文文件须先说明为何现承接文件不足，不能以整理风格扩范围。

**独立候选审查门**：作者提交精确commit/tree、完整文件身份及逐finding验收映射；新独立reviewer实际读source/整批差异和必要消费者，禁止作者自签。

**精确实际整合复审门**：唯一登记员串行合入已通过候选，冻结实际commit/tree；原独立reviewer核实际差异、精确字节和已进入分支的共享消费者，给限定实际PASS。候选PASS不等于实际接受。

**登记接受**：实际PASS及完整证据后可登记ACCEPTED_SCOPED；全部CLOSED须再满足R4-U06有限整合门。

**执行边界**：本批以事实静态验收为必需；没有新执行就明确NOT_EXECUTED。可复用本轮隔离原函数回执的限定事实，不把其变为新宿主/行为PASS。

### R4-U02 世界移动与事件状态

唯一作者 `R4-U02-author`；主责ID：GR4-M03-001、GR4-M03-002、GR4-M03-003。

**允许写的正式路径**

- deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md
- deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md
- deliverables/final-specification-set/engine-overworld/wp12-terrain-movement-vehicles.md
- deliverables/final-specification-set/engine-overworld/wp13-interpreter-command-matrix.md
- deliverables/final-specification-set/engine-overworld/wp13-map-events-npc-followers.md
- deliverables/final-specification-set/engine-overworld/wp13-move-route-matrix.md
- deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md
- deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md

**开始门**：核验最终handoff绑定、固定B/R与当前漂移；保护既有修改；独立分支/工作树；读取本批完整finding及关联旧范围。

**写入边界**：只修具名finding条款/数据/向量及必要交叉引用，不整篇重写、不改已正确规则。新增正文文件须先说明为何现承接文件不足，不能以整理风格扩范围。

**独立候选审查门**：作者提交精确commit/tree、完整文件身份及逐finding验收映射；新独立reviewer实际读source/整批差异和必要消费者，禁止作者自签。

**精确实际整合复审门**：唯一登记员串行合入已通过候选，冻结实际commit/tree；原独立reviewer核实际差异、精确字节和已进入分支的共享消费者，给限定实际PASS。候选PASS不等于实际接受。

**登记接受**：实际PASS及完整证据后可登记ACCEPTED_SCOPED；全部CLOSED须再满足R4-U06有限整合门。

**执行边界**：本批以事实静态验收为必需；没有新执行就明确NOT_EXECUTED。可复用本轮隔离原函数回执的限定事实，不把其变为新宿主/行为PASS。

### R4-U03 个体、遗传与界面消费

唯一作者 `R4-U03-author`；主责ID：GR4-M04-001、GR4-M06-001、GR4-M10-001、GR4-M10-002、GR4-M10-003、GR4-M10-004、GR4-M11-001。

**允许写的正式路径**

- deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md
- deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md
- deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md
- deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md
- deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md
- deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md
- deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md
- deliverables/final-specification-set/user-interface/wp17-draw-text-tags.md
- deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md
- deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md
- deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md
- deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md

**开始门**：核验最终handoff绑定、固定B/R与当前漂移；保护既有修改；独立分支/工作树；读取本批完整finding及关联旧范围。

**写入边界**：只修具名finding条款/数据/向量及必要交叉引用，不整篇重写、不改已正确规则。新增正文文件须先说明为何现承接文件不足，不能以整理风格扩范围。

**独立候选审查门**：作者提交精确commit/tree、完整文件身份及逐finding验收映射；新独立reviewer实际读source/整批差异和必要消费者，禁止作者自签。

**精确实际整合复审门**：唯一登记员串行合入已通过候选，冻结实际commit/tree；原独立reviewer核实际差异、精确字节和已进入分支的共享消费者，给限定实际PASS。候选PASS不等于实际接受。

**登记接受**：实际PASS及完整证据后可登记ACCEPTED_SCOPED；全部CLOSED须再满足R4-U06有限整合门。

**执行边界**：本批以事实静态验收为必需；没有新执行就明确NOT_EXECUTED。可复用本轮隔离原函数回执的限定事实，不把其变为新宿主/行为PASS。

**专有限定**：- WP18是图像分类最低必改点；WP15/21仅必要入口引用对齐，不重建动态形态全域。
- BR18局部纠错；WP34正确主规则只读回归。
- 共享UI测试目录、WP15和个体/繁育测试目录使这7项合为一个写者批；可并行只读准备，不可拆成互相抢写的作者。
- WP35及EG-13/20正确孵化内容不得因低层显式参数入口而被改成整链纯读。

### R4-U04 主动PP道具资格

唯一作者 `R4-U04-author`；主责ID：GR4-M05-001。

**允许写的正式路径**

- deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md
- deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md

**开始门**：核验最终handoff绑定、固定B/R与当前漂移；保护既有修改；独立分支/工作树；读取本批完整finding及关联旧范围。

**写入边界**：只修具名finding条款/数据/向量及必要交叉引用，不整篇重写、不改已正确规则。新增正文文件须先说明为何现承接文件不足，不能以整理风格扩范围。

**独立候选审查门**：作者提交精确commit/tree、完整文件身份及逐finding验收映射；新独立reviewer实际读source/整批差异和必要消费者，禁止作者自签。

**精确实际整合复审门**：唯一登记员串行合入已通过候选，冻结实际commit/tree；原独立reviewer核实际差异、精确字节和已进入分支的共享消费者，给限定实际PASS。候选PASS不等于实际接受。

**登记接受**：实际PASS及完整证据后可登记ACCEPTED_SCOPED；全部CLOSED须再满足R4-U06有限整合门。

**执行边界**：本批以事实静态验收为必需；没有新执行就明确NOT_EXECUTED。可复用本轮隔离原函数回执的限定事实，不把其变为新宿主/行为PASS。

### R4-U05 遭遇编辑整集复制

唯一作者 `R4-U05-author`；主责ID：GR4-M12-001。

**允许写的正式路径**

- deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md
- deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md

**开始门**：核验最终handoff绑定、固定B/R与当前漂移；保护既有修改；独立分支/工作树；读取本批完整finding及关联旧范围。

**写入边界**：只修具名finding条款/数据/向量及必要交叉引用，不整篇重写、不改已正确规则。新增正文文件须先说明为何现承接文件不足，不能以整理风格扩范围。

**独立候选审查门**：作者提交精确commit/tree、完整文件身份及逐finding验收映射；新独立reviewer实际读source/整批差异和必要消费者，禁止作者自签。

**精确实际整合复审门**：唯一登记员串行合入已通过候选，冻结实际commit/tree；原独立reviewer核实际差异、精确字节和已进入分支的共享消费者，给限定实际PASS。候选PASS不等于实际接受。

**登记接受**：实际PASS及完整证据后可登记ACCEPTED_SCOPED；全部CLOSED须再满足R4-U06有限整合门。

**执行边界**：本批以事实静态验收为必需；没有新执行就明确NOT_EXECUTED。可复用本轮隔离原函数回执的限定事实，不把其变为新宿主/行为PASS。

### R4-U06 有限整合与唯一关闭

依赖U01–U05全部实际ACCEPTED_SCOPED及其完整证据；不并入任何新引擎工作。逐17验收（含本轮反证精确化）、受影响GR3、旧229/341 qualified scopes、14有限链和正确正常/失败行为全部有去向。共享文件只由其主题作者写，全球进度、问题账、接受、冻结与交付回执只由ROOT写。

若实际整合需要新增事实修补，先列原因/范围，冻结新字节并由与作者独立的审者仅复核受影响范围；不得以旧PASS、候选PASS、相同文件名或作者自述宣告实际接受。所有贡献与最终ID闭合必须绑定真实commit/tree、路径、bytes、SHA256/blob和限定条件。完整依赖边：五主题actual acceptance→U06；U06满足后唯一登记员才将17项CLOSED。未满足则保持OPEN/PENDING，不能伪造终局PASS。

跨批有限握手：U01文本结果→U03布局/输入，保留替换和显示阶段；U02世界状态→U03显示/等待，不补总事务；U04道具资格→U03确认/取消，普通数字与件数窗口分开；U05编辑登记→U02运行快照，复制不自动刷新当前图。U06核这些交界，不把它们扩为全能力回归。

只读正确合同尤其包括WP34三/五IV主规则、WP35/EG-13/20动态孵化、GR3 23已正确范围、全部历史报告/回执。不要为了BR18修改正确正文，不把M04低层参数纯消费扩成孵化整链纯读。28个写路径之外的改动如无具名必要依据一律不作；也不擅自把旧可选导航问题纳入。

## 6. 角色、模型与审查真实性

下一轮与本轮astra review分开：作者/修订/唯一登记任务请求 **gpt-6.1-sol、reasoning_effort=xhigh**；独立候选/实际复审请求 **gpt-6.1-sol、reasoning_effort=ultra**。两者均普通速度/service_tier=default，禁Fast。请求被接纳即可继续，实际回显不可得记UNVERIFIED；不探查额度、计费、凭据、私有会话或后台配置，不改全局配置来自证。请求被拒绝或不支持应报告受影响任务和真实可选方式，不能静默换模型/降effort/Fast。

作者不能自签独立review；独立审者必须实际阅读输入差异、R证据、必要caller/override/data及全规格反证。作者的自查可作辅助，不是验收。每批记录真实任务/thread ID、角色、固定输入、状态、已审范围和日志/产物入口；优先可见Desktop机制，CLI须先给父入口、实际ID/PID、日志和查看方法。缺单独侧栏链接不成为无谓阻塞，不编造链接。

一个报告/共享文件只由明确写者更新。更换停滞任务时保留已有取证与范围，不全部重启。只需一次有效独立质疑和一次实际整合检查；无新证据不要建立无限“审查审查报告”循环，身份未变可复用核验缓存。

## 7. 验收、回归和执行证据

最低逐项验收就是第4节的全部准确前提/数学/状态序列/数据/正反例。所有更新须同时处理正文、必要附表、静态向量和共享消费关系；标题不同不等于缺能力，已准确事实保留。源bug先写R事实，再单列未来政策，不默默替R修好，也不要求未来永远保留缺陷。

受影响GR3逐ID记录本次检查/有限复用，不重写旧CLOSED。旧229/341从固定ledger指向原qualified范围和exact tuple，重点检查实际改变的消费者与本轮具名反例；其余写historical_qualified_evidence_reused/not_reexecuted。不得把341当341功能、把一个贡献PASS当整ID责任、把同blob旧签名扩到新owner/前提/运行。

历史54/8/18与本轮14链均保留原前提、未审与资料限制。对新修订影响的旧消费者作有界反向检查；例如A053孵化、C064持续基底、插件顺序/翻译节头、TR记录、经验整数阶段、传送保游泳及对角顺序。未变且未审部分明确复用，不重读所有旧报告或恢复全部退休分支。固定历史入口优先B的evidence-navigation.json；分支别名退休不等于证据删除。

本轮仅4次EXECUTED_REFERENCE：M01本地化原函数1次、M02 HTTP/墙钟原函数2次、M12评级结算1次，均Ruby2.6.10隔离并明确时钟/网络替身或绕过组队初始化。它们没有真实网络、真实存档、完整编译/转换/反序列化、600队模拟或宿主/Demo；精确回执在execution-evidence.json。CA/CB/J没有新增行为执行，只静态回源和结构核验。随附3.1宿主未执行，不把Ruby2.6结果抬成原游戏实测。旧交付运行0保持历史事实。

证据必须使用SOURCE_STATIC、SPEC_STATIC、DERIVED_VECTOR（未执行）、TOOL_VALIDATION、EXECUTED_MODEL、EXECUTED_REFERENCE、EXECUTED_HOST_OR_DEMO分列。hash/JSON/路径/BMP头/名单比较不算行为测试。新的安全隔离执行须先写目的、输入/版本、命令、预期区分、输出目录和副作用，再记实际时间、退出码、输出；不伪造通过。仅当确有必要且已有安全条件时执行，不安装未知软件/改安全设置/取得新凭据/下载未授权资源，不碰reference、真实存档、生产账户或外部状态。

## 8. 未审、额外材料和用户政策

保留全部源文件/配置/数据组合、逐效果笛卡尔积、动态插件重入、全语料/备份启用、精细图案/粒子/字体、所有地图/事件/完整Demo和宿主输入渲染音频的未审范围。300范围记录与逐文件not_checked是边界，不是全部功能证明。缺资料单列material_availability，不计作规范missing。

需要用户后续决定的是新引擎的长期兼容政策：是否保留计时查询销毁与异常天数、POST前失败、传送残留/等待、部分提交/重复退款、无空白长词不硬折行、图鉴普通外观等；是否提供完整资源/地图/宿主做新执行验证；是否另启旧OPTIONAL导航工作。本次事实整改无需先替用户选择这些政策，不能擅自加“改进”行为或启动U08。规范UNRESOLVED=0不代表以上材料/设计/运行未知已解决。

## 9. 启动次序、停止边界与交付

1. 核本handoff外部manifest/发布回执的固定身份、报告快照、B/R和必要文件完整bytes/SHA/blob；保护现有tracked/staged/untracked/ignored、stash和其它worktree。原Mac62候选只是受保护输入，不要求清掉；云端也不reset/clean/自动stash。漂移报具体差异，不静默换基线。
2. 建新的整改工作分支/隔离目录，登记五主题唯一写者和审者，先做独立可并行准备；据第5节限定启动候选修订。不要重跑第四轮全球review代替整改，不恢复全部旧工作分支，不重复归档清理。
3. 每批作者候选→独立候选审查→唯一登记员实际整合→与作者独立的精确actual复审→有界接受；按依赖进入U06，所有门满足才唯一关闭17项。失败/争议保留证据并修本批，不修改已签原报告。
4. 完成后交付新的正式文件身份、逐项接受与旧资格保持、完整未执行/资料限制、简明中文总结和整改分支。仅显式stage授权路径，普通push整改分支；远端按真实commit/tree读回完整产物bytes/SHA/blob，至少完整读取规范文件/接受/交付入口并据全量清单核其余。push不确定先读状态，不盲重试、不force、不推main。
5. 发布受权限/网络阻塞则保全本地完整成果，明确失败动作和未远端可达文件及最小补救。只有真实必要信息/权限或政策阻塞才问用户，继续可独立工作。

授权止于这里：不合并main，不实现新框架/引擎，不变更安全设置，不删除搬迁旧证据，不替用户发送其它消息，不把可选/未决政策范围作为必修启动。依赖尚未满足的实际接受和关闭不得提前。
