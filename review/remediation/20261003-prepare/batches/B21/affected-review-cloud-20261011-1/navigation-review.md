# B21 导航、资格及旧批准保全独立静态复核

结论：`NEEDS_REVISION_CURRENT_CONSUMER_NAVIGATION`。完整资格、旧接受贡献及旧行为条款保全在本子范围为 `PASS`；当前导航有一个阻塞 `B21-NAV-01`，含四个具体错配。此结果不签 actual、B21 接受、FINAL-1、关闭或 FINAL-2。

被审 NEW `5c3e19831e1e29450247fa6061f3c2feac2f893e`，tree `98062bf1205669936426ae870913e578528b740c`；C `e9c140dc33de1cb0662521318b051174909e4509`；D `eb1885265fcde2a52767077de3193862036c3a71`；发布冻结入口 P `fa5e1d876c9082797d6eb71f1590f3d8d9a19b0a`。先按 P frozen-NEW → FULL → affected → dispatch 顺序读取，再读 D 原合同及完整 control overlay。

仅用新写只读 Git、文本、JSON/TSV 元数据分析及原始字节哈希。所有源身份均从固定参考 tree 独立重建；未执行参考、Ruby、编译器、转换器、游戏数据反序列化器、行为向量、静态案例或旧脚本。432 路径的身份核对不等于 432 份源码语义通读，案例不报告运行。

## 一项导航阻塞与四个实例

下列错配是当前摘要/消费者入口的定位错误。固定完整批准对象、全部控制限定及正确的旧同 ID scoped 接受证据仍在；不能据错误摘要认定正文条款或资格被删除，也不能以正确旧证据宣称错误当前导航已完整。

### obligation-map /records/9 · GIR-FD82-003 · extension_decisions/4

固定批准对象：`41fffb540c6483f5296ea0d33b789b75180d27ed:review/remediation-20261003-prepare/finding-acceptance.json/GIR-FD82-003/extension_decisions/4`，规范对象 SHA256 `eff4332168b08ac236bcc9449680da1c0ed4a2c0c7fbdad621fb8cee7ffec113`。

原批准控制的 project_locations：`[原对象所记来源]:deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md:17-18;141-143;214;233-240;264`; `[原对象所记来源]:deliverables/final-specification-set/demo-dx/wp76-facility-content-generation-and-simulation.md:36-41;52;122;190;254`。

当前声称域 `WP39, WP76`，应承接 `WP67-A, WP76`。真实当前条款：C WP67-A §§2/6.3/9.3/10; WP76 §§3.2/6.1/7.4; B17 inherited TSV row265。保留的正确旧 scoped 接受行：`265`。

### obligation-map /records/14 · GIR-FD82-003 · extension_decisions/9

固定批准对象：`41fffb540c6483f5296ea0d33b789b75180d27ed:review/remediation-20261003-prepare/finding-acceptance.json/GIR-FD82-003/extension_decisions/9`，规范对象 SHA256 `560c9558ff0bccf86b358ce7a6185d9977c5b4ccc923ac964ca05603c729314c`。

原批准控制的 project_locations：`e1e01bb18d824931e54f182dd61af5a9f908ba85:deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md:17-17;26-26`; `e1e01bb18d824931e54f182dd61af5a9f908ba85:deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md:25-27;69-69;92-95`; `e1e01bb18d824931e54f182dd61af5a9f908ba85:deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md:88-95`; `e1e01bb18d824931e54f182dd61af5a9f908ba85:deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md:13-14;24-40`。

当前声称域 `WP63, WP65, WP66, WP67`，应承接 `WP60, WP61, WP63, WP65`。真实当前条款：C WP60 §2/§3.1; WP61 §2/§3.1; WP63 §§2.2/4.2–4.6; WP65 §5.1/§5.2; B14 row172 and B15 row208。保留的正确旧 scoped 接受行：`172, 208, 241`。

### obligation-map /records/15 · GIR-FD82-003 · extension_decisions/10

固定批准对象：`41fffb540c6483f5296ea0d33b789b75180d27ed:review/remediation-20261003-prepare/finding-acceptance.json/GIR-FD82-003/extension_decisions/10`，规范对象 SHA256 `8665f5ef298dc14ed97c8b7d5ea3d197f3e4c05c2e840aec08285dc81bc3abda`。

原批准控制的 project_locations：`e1e01bb18d824931e54f182dd61af5a9f908ba85:deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md:29;57-62;141;145`; `e1e01bb18d824931e54f182dd61af5a9f908ba85:deliverables/final-specification-set/user-interface/wp67-b-lifecycle-presentations-and-history.md:11;18;126;132`; `e1e01bb18d824931e54f182dd61af5a9f908ba85:deliverables/final-specification-set/README.md:21-25`。

当前声称域 `WP72, WP73, WP74, WP75`，应承接 `WP66-A, WP67-B`。真实当前条款：C WP66-A §§2/3.3/6; WP67-B §2/§6.3/§6.4; B16 row241 and B17 row265。保留的正确旧 scoped 接受行：`241, 265`。

### obligation-map /records/39 · GIR-FD82-C029 · root_adjudications/0

固定批准对象：`41fffb540c6483f5296ea0d33b789b75180d27ed:review/remediation-20261003-prepare/finding-acceptance.json/GIR-FD82-C029/root_adjudications/0`，规范对象 SHA256 `823ff4cb62475fe59b2fc672c9f5c68711d71e2f0bf6c4e34a129f180ab79f4c`。

原批准控制的 project_locations：`e1e01bb18d824931e54f182dd61af5a9f908ba85:specs/demo/wp77-demo-evidence-and-capability-coverage.md:159-160`; `e1e01bb18d824931e54f182dd61af5a9f908ba85:deliverables/final-specification-set/demo-dx/wp77-demo-evidence-and-capability-coverage.md:132-136`; `e1e01bb18d824931e54f182dd61af5a9f908ba85:audit/source-traceability.md:1348`。

当前声称域 `WP21, WP73`，应承接 `WP77, WP21, WP18`。真实当前条款：C WP77 §6.4 lines145–146 and demo test B20-C029 line278; WP21 §6/WP18 form-read gates; B20 row318。保留的正确旧 scoped 接受行：`318`。

003 extensions/4：WP39 的 B09 row151 不能代替 B17 row265 的 WP67-A/WP76；完整 B17 门还保留 WP67-B 局部条件。003 extensions/9：应加入实际 WP60 树果与 WP61 场外效果消费者，不能用 WP66/WP67 摘要代替。003 extensions/10：应定位 WP66-A/WP67-B，而非 WP72–75。C029：NEW traceability `/records/9/current_consumer_nodes` 同样只列 WP21/WP73；应加入 WP77 §6.4 及 demo test B20-C029（当前 C/N 行278），WP21/WP18 为真实形式读取交界，WP73 不能代替 WP77。

修订验收：对四个 records 及相应 current_consumer_nodes/source/central 导航修正精确 owner、条款、测试和匹配旧 receipt 的关联；保持正文、资格对象和所有旧证据不变。对全部 47 对象重建当前关联，不能只修域名字符串。重新冻结新 NEW 并独立复核全部规定 affected 门；本 NEW 的结论不转授新候选。actual/B21 C/FINAL 各门另行协调。

## 资格、源码身份与机制分层：PASS

独立从固定参考 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0` 枚举并逐 blob 校验 432 路径、mode、Git blob、SHA256、bytes；其中 312 Data/Scripts Ruby 和 33 顶层 PBS txt 是导出计数。35 配置行及 17 UI 行逐项验证原证据对象规范哈希，并核对历史字段逐字节承接。111 当前正文消费者的 blob/bytes/SHA256 和全部声明标题行均与固定 C 树相符，C→NEW 同字节。

配置的存在、机制语义、样本内容与启用/实际配置四个层级分别核对，没有以文件存在推出启用，也没有以完整导航推出全源语义覆盖或真实 Demo。全 14 原控制和批准对象、全部限定字段及 47 根/扩展对象规范哈希均重算相符。`complete_original_object` 和 `index_row` 未重复列入 all_qualified_fields；完整原对象/完整批准对象绑定已分别独立验证，这两个冗余元数据不是控制限定的遗漏。

旧 NA 的九个世界/UI/audio 源文件有真实消费者后继，不能沿用旧 NA 作为当前排除理由。静态阅读核实：Picture 游戏时长20单位/秒与旋转运行时钟20度/秒分开；erase 仅清图片名，持续状态和入口矩阵分层。Timer 负业务值、显示0与停止隐藏分开。地点条0.4+1.6+0.4秒、fly 先于消息/地图释放、outdoorlight 名称回退和暗图64/176保留。BitmapSprite 宿主可见更新与容器组织分开。pause 4帧/.15 和导航8帧/.1全局相位、初始帧0与后续update分开。命名行走图4×4首行/.5与箱图单行/.4保留合法资源及各 caller 失败边界。audio last-truthy-including-empty 顺序与 map 后备、FromType helper 空串返回、next-battle 各类别独立及 intro 已排队/当前记忆均保留；静态全 Scripts 文本检索仅作 caller 定位。Scene_Map 堆栈与时间顺序按固定源读回。

C003 全部输入、最小反例、fixture 前提、根/扩展资格保持；C007 的120行为、默认24时段、35转换词法项、3行首路由前缀和旧18电话项分别承接。树果67输入是承诺完整默认兼容时的条件性要求，不能升级为普通样本默认表义务。ASCII 必要字面量与源容器/API要求分开，415/154/18为原候选分类规模，不是缺陷数；各扩展原限定完整保留。U01–U10/G01–G12/AX01–AX20、未读 cup/pokemon_metrics/backup、动态、媒体、宿主、插件和真实运行/Demo 限定保持。

## 九输入与历史保全：PASS（独立子审计）

九原输入独立逐字节重建为2份同字节，7份恰好一次 `delivery/` → `../../review/wp68-wp69-wp70-parallel-b-2026-09-30/` 且各 +41 bytes。九当前最终正文均与固定 B18 ACT `c211767166b18799122c1e39b9f08afce6b0c92b` blob 相同，C→NEW 未变；旧 ReviewPending 与批准范围不转授 B21。原158是历史字段标签，实际138数组位置全部逐位置重算原对象/批准对象哈希及当前 owner receipt，保持原标签并后继勘误。17历史载体、dated manifest 原4112行前缀、正式历史勘误原119行前缀及两个 TSV 原327数据行字节保持。327回执原容器627635 bytes不变，SHA256 `d11d131dc64b399cda50b7518fffe8a812282c1b51436065647c1707c831d303`；327数组规范 SHA256 `ca73d8b68c03e80e40066acb4349683836f8165a4f2daa5935cfef8b852cd9fa`。新增14行仍 OPEN、未接受、无 actual。

独立九输入/历史审计详见 `approval-history-review.md` 及压缩固定引用 JSON；后者只记对象身份与派生检查，不复制整包旧证据。该子项不替代各 owner 全规定条款复审。

## 固定证据身份

原 findings 固定 `93e10babe0b9c9ef8b3f5277754541b447beeeb4:review/global-independent-review/2026-10-03-fd82a639/findings.json`，blob `6f3d96fd99b5a026bb88e463b3ad6e46658e3c01`，SHA256 `7c2f0b9159f7be21d8ae9d647399521017500fe4c40ffed042c004492c6a242d`。完整批准文件固定 `41fffb540c6483f5296ea0d33b789b75180d27ed:review/remediation-20261003-prepare/finding-acceptance.json`，blob `e178e5706771f5f7465bcf3351b5c632a5d68bab`，SHA256 `54e4c86be3db493a5463ce4bcdef81c7184f1a1d89e6b3bbea358f14cc347225`。下列 /records 索引均是0起始 JSON 索引；TSV行数均是1起始数据行。

| 固定 commit:path | Git blob | SHA256 | bytes |
| --- | --- | --- | ---: |
| `5c3e19831e1e29450247fa6061f3c2feac2f893e:review/remediation/20261003-prepare/batches/B21/author-draft-1/obligation-map.json` | `3ac13c2d126acad18022082e855c62358ec14deb` | `a9a20ef588cb9d3e77d502d097d914098250c630dac54bc7a04e1484c16fe252` | 204840 |
| `5c3e19831e1e29450247fa6061f3c2feac2f893e:review/remediation/20261003-prepare/batches/B21/author-draft-1/traceability.json` | `3e83ff6ce3f9e609c81174d27ef9df7f8d56741d` | `ef295f8ab2b7df9298f469dd1f2eae53095fcc859b3b8d48dc7fe7a61521a604` | 660402 |
| `5c3e19831e1e29450247fa6061f3c2feac2f893e:review/remediation/20261003-prepare/batches/B21/author-draft-1/navigation-identities.json` | `eb1f083e91421f3119ec8e78aeeb018ba36f0b0b` | `4c3258dbe806eaf660eb1568f9fb543ef559cdff3e8e75f1459901a83c0d3fde` | 270708 |
| `5c3e19831e1e29450247fa6061f3c2feac2f893e:review/remediation/20261003-prepare/wp79-source-successor.json` | `d5ed465adfe37c0cdde6e060a2f84248facd8dbb` | `ab5b39f35cfbdbdce75d08b69df1b2734a8a9de4c61f99ff43c368ed624496e0` | 601928 |
| `5c3e19831e1e29450247fa6061f3c2feac2f893e:review/remediation/20261003-prepare/wp79-config-successor.tsv` | `8c5929f12aa085bd88aa7df2bec902e17ac87718` | `e631bcf69236db493ed10754fe55afe1d518dfd4389e65f68d2f965b3aadd944` | 46883 |
| `5c3e19831e1e29450247fa6061f3c2feac2f893e:review/remediation/20261003-prepare/wp79-ui-successor.tsv` | `b106f4938413b768c7342d0652c1b1913175cb8d` | `926ce5169faf1591875a4df9946541f211e84fd4f11506b7d060bc428cc1f973` | 23487 |
| `e9c140dc33de1cb0662521318b051174909e4509:deliverables/final-specification-set/demo-dx/wp77-demo-evidence-and-capability-coverage.md` | `e792348b0a7f35145736f7d595e86ec290b420b8` | `d1ba7c694f41ee5c3763a725467996632264e504563be74036c20d6ad5021ca6` | 29209 |
| `e9c140dc33de1cb0662521318b051174909e4509:review/remediation/20261003-prepare/traceability-successor.tsv` | `43d961b027fe73fe14c0d8149b226a9dd283f51d` | `d419ab4bebf9274056914be7ca1b47332fb3354d106fbf0400796c40f1b88d8a` | 985845 |

完整 C→NEW 差异已发布一次，复用 P `review/remediation/20261003-prepare/batches/B21/author-draft-1/freeze-1/complete-C-to-NEW.diff`，SHA256 `7cb43d6e3b3ab252029396234dd5de631ff37b85171270be40f0a239d39dcb8a`，3430268 bytes。根审计负责独立重建；本文件不递归复制差异或完整 approved-controls 阅读缓存。

## 全14完整控制资格裁决

每个控制的原对象与完整批准对象分别从固定 Git 文件重算规范 SHA256；全部规定资格字段的集合与值都核对，不以作者字段数或断言作通过依据。下表 PASS 限于完整资格与旧成果保全；003/C029 的当前导航须按上文修订。所有14当前仍 OPEN，无 actual/接受/关闭签名。

| ID | 原控制对象 SHA256 | 完整批准对象 SHA256 | 资格/旧成果裁决 |
| --- | --- | --- | --- |
| GIR-FD82-001 | `e7622aab86d642f366df81db11509cb306f1ae0ea5b9ba5f49b51f5ffbc72fc5` | `cc74c7752cde4dd7ed70d9d896f1e9896af4437b3e057226d74dd8f13907981d` | PASS（完整资格/旧成果，有界） |
| GIR-FD82-002 | `1044fd3ccd7f911cbabe12538216838a7371d8972fedde0ec917f92d48993bde` | `c2994704567b70dec3b52ffb6c3c53999196bcf6aef1682c17a0c1bf7672546a` | PASS（完整资格/旧成果，有界） |
| GIR-FD82-003 | `7f65b95e57c5894daca39a68fc000f0d25128e6b0ab00a46f40657fab937f0d7` | `87a237bcca488318f1c42793b8b42882167c0f038f17f3e2a1c1f19539263f50` | PASS（完整资格/旧成果，有界）；当前导航见 B21-NAV-01 |
| GIR-FD82-006 | `d35bb618fadf8f067b80a7dbca029b0c717c170e203e9a7c05e1d31aaa695ad7` | `5da187227b36049a84b4445f0e610c0fcf0804aed9a1e7f6c656e8e31fe3ce57` | PASS（完整资格/旧成果，有界） |
| GIR-FD82-A017 | `6ad66dc2c74c38f83668913851358fa6e26dac02762f547ff10b5e326739a7a9` | `72faf567de673708e15b06127b535b991a1622e0aee63e59156fec3fdd3d6840` | PASS（完整资格/旧成果，有界） |
| GIR-FD82-A058 | `5791739a78acb5dff9ed76dd7aa32e41bfb5fbe7db573303e58efe7333fc5751` | `d7cc026d23942cc971285bc645ae98a9679042c411b12453736fae96331541e5` | PASS（完整资格/旧成果，有界） |
| GIR-FD82-A059 | `8e0cff53e71ba3ebd0cf55ea5bc85d18da038ab7b0c5bfef2459dc00979bc32b` | `e9cbda63fd4653f1c808d6b4a95f51277fe62cccd59870416fbf89972ed0e659` | PASS（完整资格/旧成果，有界） |
| GIR-FD82-C003 | `d15815f17cd3774f9f3a71a4344cd7582375e7272a7dba4513eedf336c68d313` | `e9d0142ff20807904c0c9e904ef58cb6dc34c946a96b801d115c9ca5ec36e870` | PASS（完整资格/旧成果，有界） |
| GIR-FD82-C007 | `564aaea01b9d52685912601c7cef335259ad8ccc3fcdefd68d2f840fc7218eff` | `2aaf7910600505747db56be6a214e65a6125afc6be7d39013e69e510b1a81b86` | PASS（完整资格/旧成果，有界） |
| GIR-FD82-C029 | `4f51bc85599330d6cedacc3eabdc765da9f87d1625bf5bd90e3c5e4ad7e81a80` | `b0662d15b2abc507a5cc4595138412a1df8f370d137e80d3ece27824a2c4574f` | PASS（完整资格/旧成果，有界）；当前导航见 B21-NAV-01 |
| WP80-B02-R02 | `a2817040098b716475bcf0ea618feb77ff99d36695a382977731d789be2a9667` | `66dd919c91c53e304d624d31a29652f6b3acfc75dd3d45d1a05cf20ef99e8e25` | PASS（完整资格/旧成果，有界） |
| WP80-INTAKE-C01 | `03b94212980b124c8fcb760e491be6933cb9aaa964713a20391496f809f356af` | `842068fd6d916152a2f35fb273cf7d0c4894d54fcfef02e8e2119123e7421509` | PASS（完整资格/旧成果，有界） |
| WP80-INTAKE-R01 | `c7e7cc0c518e336305b0c0ce5e649013d432561136c00bc04f8cca3c6f525a98` | `84ccd698373558d050de4d4450e075a413227bc2d2b5bce3464a94e5d135d90e` | PASS（完整资格/旧成果，有界） |
| WP80-INTAKE-R02 | `cf4cb7f48995a426b91aa8a2400446c5f1b668b685a252aa2e7654ad5840a736` | `47663429daa26a32931bf8edc48ed1ab13875d229afccd7468e59a017dfde0ec` | PASS（完整资格/旧成果，有界） |

## 全47逐项核验

每项完整批准对象规范 SHA256 已重算相符，完整资格保全 PASS。表中给出当前 owner 真实条款；原 project_locations 全部在同名 JSON 各项 `original_approved_project_locations` 保留原路径/行/已有来源 commit。当前导航其余43项以准确当前条款或精确同 ID 旧 scoped receipt 承接，本表不向旧 receipt 扩大结论。

| record | ID / 批准子对象 | 批准对象 SHA256 | 实际当前 owner 条款 / 当前导航判定 |
| ---: | --- | --- | --- |
| 0 | GIR-FD82-001 / `root_adjudications/0` | `bf61defdd5d79327ecdfcaffbcb5a73716e1f6d0a0fc95b2de83953e5d8ed2d1` | NEW README/scope/current status layer; audit and historical errata distinguish delivered, accepted, candidate, actual, FINAL；PASS（有界） |
| 1 | GIR-FD82-001 / `root_adjudications/1` | `778c40fcbdc01670fd857807455ae6f3dd8604efdd6e2fcb9b3ca6cef9b3b9b8` | C seven named WP68–71 headers: root audit relative link; Voltorb layouts already-correct link retained；PASS（有界） |
| 2 | GIR-FD82-002 / `root_adjudications/0` | `175473f307b758401a0d25aef4b369e7f97d745be8e84208bae07869fafe581c` | C WP16 §§5.4–5.5; WP13 command-entry matrix; WP11 transfer; WP59 FLASH gates；PASS（有界） |
| 3 | GIR-FD82-003 / `root_adjudications/0` | `e4c50ccc89c5e84b35dc8c411b90377b206011853bafe71bf7afb920993053a8` | C WP39 §§2/3.5/4.1 and WP40 §§2/6.1: behavioral seats, command acceptance and sort inputs；PASS（有界） |
| 4 | GIR-FD82-003 / `root_adjudications/1` | `34431bb6311f2f0b559a13d10fbac253d1504594c1bcc6c772154d80c0e79dfa` | C WP73-A §§2/3.2–3.5/4–6: input categories, cancellation and shared-state effects；PASS（有界） |
| 5 | GIR-FD82-003 / `extension_decisions/0` | `ba3cd930db635ce599e4e66eaf88959e9b1f2cad42ac6d2038ceb865d40b310b` | C WP46 damage/healing rules and WP54 §6.1: Ice clause final target gate retained；PASS（有界） |
| 6 | GIR-FD82-003 / `extension_decisions/1` | `6b4f7325509f588d475e7cb11d195252b3820d1a63bf93c92e53f7bffaa8559e` | C WP52 A/B/C bodies and data appendices; historical module/line anchors confined to audit；PASS（有界） |
| 7 | GIR-FD82-003 / `extension_decisions/2` | `c52b5b22a97f4faff1b2fa96099dbffb13e4d52fbf128ff241c6e1cf5e27b8e3` | C WP54 §6.1 and QC data/static rows: final OHKO/Ice target condition；PASS（有界） |
| 8 | GIR-FD82-003 / `extension_decisions/3` | `9f21b38e9237fef16f9ab9f91f83b0c52e263666f688472e145768ddc75bdaf7` | C WP56 §§2–4 and WP58 §§5–6: behavioral variants, random inputs and replay state effects；PASS（有界） |
| 9 | GIR-FD82-003 / `extension_decisions/4` | `eff4332168b08ac236bcc9449680da1c0ed4a2c0c7fbdad621fb8cee7ffec113` | C WP67-A §§2/6.3/9.3/10; WP76 §§3.2/6.1/7.4; B17 inherited TSV row265；**NEEDS_REVISION** |
| 10 | GIR-FD82-003 / `extension_decisions/5` | `fd414a7c7af5ae8c6ac587469bec59eafd62470b217d498267e6813edaf4e941` | C WP73-A §§3.2–3.5/4–6: neutral property/list roles and partial state preservation；PASS（有界） |
| 11 | GIR-FD82-003 / `extension_decisions/6` | `a87a7a45b0de0ddd7eedac4c5cdfe2d63f1ebc71fc7fb8eedf487b2b1dec70e4` | C WP74 §§4.3/6.1/17: independent clipboard pastes, coupled inserted attributes, visible refresh；PASS（有界） |
| 12 | GIR-FD82-003 / `extension_decisions/7` | `b02ef3d944255daab8c97716d75f0be292434c717fe5ffddec73fb817a42a03a` | C WP15 §§5/6.1: observable reuse/lifetime and playback fallback; WP16 neutral lifetime comparison；PASS（有界） |
| 13 | GIR-FD82-003 / `extension_decisions/8` | `7395a149a9e254be2ea05b346dedf830774ab36abc2af70a5415d2742135d7d2` | C WP36 §§3/7; WP37 §§3/8.2; WP59 §§5.1/5.4: state identity and order without source container/API requirement；PASS（有界） |
| 14 | GIR-FD82-003 / `extension_decisions/9` | `560c9558ff0bccf86b358ce7a6185d9977c5b4ccc923ac964ca05603c729314c` | C WP60 §2/§3.1; WP61 §2/§3.1; WP63 §§2.2/4.2–4.6; WP65 §5.1/§5.2; B14 row172 and B15 row208；**NEEDS_REVISION** |
| 15 | GIR-FD82-003 / `extension_decisions/10` | `8665f5ef298dc14ed97c8b7d5ea3d197f3e4c05c2e840aec08285dc81bc3abda` | C WP66-A §§2/3.3/6; WP67-B §2/§6.3/§6.4; B16 row241 and B17 row265；**NEEDS_REVISION** |
| 16 | GIR-FD82-006 / `root_adjudications/0` | `d85f65faf4980c57d62ee345ea6866c08e6f0ef055b0759bebbc135d8137f488` | C WP17 §3.4 (line80) and WP66-C §3.1 (line29): pause/nav frame clocks and initial frame0 distinction；PASS（有界） |
| 17 | GIR-FD82-A017 / `root_adjudications/0` | `646012dc05bb8dd93d3a37af02d7e9a2932c3a052015c234eac61dcafca4e0bb` | NEW audit current A017 erratum; reference 003_Game processing/002_Scene_Map.rb:243–246; old eight path corrections remain in B02 receipt；PASS（有界） |
| 18 | GIR-FD82-A058 / `root_adjudications/0` | `a6ce92361768163d9fbb7b0242db879af2d7b12c2d5ad7a1fda81831ab425dc2` | C WP17 §6.2.3 (line183), WP65 §§3.2/3.4 (lines45/68–77), legitimate walking/box previews and caller-specific failure；PASS（有界） |
| 19 | GIR-FD82-A059 / `root_adjudications/0` | `e8339bd69e17f105d92024d368cf0279bf981be004ada73ef29a4f09c5efbea3` | C WP24 §5.4/PT41–63; WP15 §6 cross-link; WP16 pre-battle §§1/7 normal-return cleanup; helper-only FromType restriction；PASS（有界） |
| 20 | GIR-FD82-C003 / `root_adjudications/0` | `afb73f107150fe326a61b2b6530362c8bb450bd29acbb737766220fb2e2e1566` | C WP73-A §§3.2/3.3; CE-M02 ordinary/nullable numeric and bool cancellation；PASS（有界） |
| 21 | GIR-FD82-C003 / `root_adjudications/1` | `2a883ab04d9b4146e7fe4925d0adb42b5be45a83d17a0cc50e7db86e7a705e62` | C WP36 §§3.4/4/5 and EN-01/15/16: non-surf step-table, active OldRod request and contest gates separated；PASS（有界） |
| 22 | GIR-FD82-C003 / `root_adjudications/2` | `9f26456c2d026ee4e76479c937652322707871f3bdf849a3f3989ba8cbb535b4` | C WP28 §§4/5; PT A23/A31/A33 unique HP, overlap and egg fixtures; B07 row132/B17 row274；PASS（有界） |
| 23 | GIR-FD82-C003 / `root_adjudications/3` | `36677f0f9efcee7c1d18883544e9efdaf71fd33da21c74c2ae3fb52cdf401e0d` | C WP72 §7.2/DG-M18; WP73-A CE-M02; WP74 AN-M28; trainer-count, input-subtype and midi fixtures；PASS（有界） |
| 24 | GIR-FD82-C003 / `extension_decisions/0` | `7409bfecdd96ad8c1e7e032f5a62b9e6807b4a31b9b91f3a3d02787cea0f3b76` | C WP73-A §3.4 and CE-M10: cancel old pocket0 versus confirm visible index0/pocket1；PASS（有界） |
| 25 | GIR-FD82-C003 / `extension_decisions/1` | `1d0c4642c1cc2a2c79f8efe7af93abf909b45e8e869f4eec68fe2a947c8479b2` | C WP74 AN-M28 and WP75 CV-M03/CV-M14/CV-M27 exact CommonEvent5/EndSpeech/&bs; and formatting categories；PASS（有界） |
| 26 | GIR-FD82-C003 / `extension_decisions/2` | `4e8307410d3ebb72f7664255724ff26c012424baa4ed3e8412c4ca57b551547a` | C WP12 MV03; WP14 DG01/DG23; WP11 MP22/23: two tiles, dimensions, ordered X/Y and edge weather20；PASS（有界） |
| 27 | GIR-FD82-C003 / `extension_decisions/3` | `65076f7a39ff7b6f8efff1c9248a0e8b7273174414f373892d784649b45d2696` | C WP17 MG28/DT03 original-scene/no callback/ordinary-character gates; WP16 WR06/WR12 bridge/height/shading/cache time；PASS（有界） |
| 28 | GIR-FD82-C003 / `extension_decisions/4` | `9ced158b8ffae9463355ece32f0534f0bee7ea1336e77503aedfcf92c84307f1` | C WP36 EN-01/15/16/32 and WP59 WT03/WT07: separate original insufficiency, step/active/weather premises；PASS（有界） |
| 29 | GIR-FD82-C003 / `extension_decisions/5` | `5880ee5fdec3b49af40edd273f157518bb4ea770ed38571db579fdf723a9d8a5` | C WP60 fishing §6.1/FS16; WP61 §§5.1/6 FP06/FP12/FP14: common-event fixture, poison configuration and non-egg infection period；PASS（有界） |
| 30 | GIR-FD82-C003 / `extension_decisions/6` | `46e59d1c9fa44e5cdf9d3fff4fe85303684ccc8cdb246b05447dee9bf9ffc498` | C WP28 PT A23/A31/A33; WP70 L09 duplicate-b layout; B07/B15/B17 accepted local traces；PASS（有界） |
| 31 | GIR-FD82-C003 / `extension_decisions/7` | `ffadc441b7ea99698e48e0acfca55926e22fc18f440d1aafdda516d90e5d3bed` | C WP71 §§2/6 and TP T01/T18: empty cell0, empty held tile, three-column result placement; B18 row278；PASS（有界） |
| 32 | GIR-FD82-C007 / `root_adjudications/0` | `24eb5df4a04f4b1908afd3e28a5a1e1d53ae0c69a2c1505c26b9487a240110a5` | C WP72 §13 120 independent behavior rows and allowed scopes; B19 row290；PASS（有界） |
| 33 | GIR-FD82-C007 / `root_adjudications/1` | `80a7ea0cbb424d3774291763543c0a4c37c5ee5d587b8b717bc469a2729bb3da` | C WP59 §3.5/default24 table (line70), brightness/cache clock; B14 row174；PASS（有界） |
| 34 | GIR-FD82-C007 / `extension_decisions/0` | `771aaa877c4cde02458e7dc65ce34dfd0397d9de464b4169dcfe31f1d373d3fd` | C WP75 §8.1 ordered35 old lexical inputs and §8.4 two healing-loop variants; B20 row311；PASS（有界） |
| 35 | GIR-FD82-C007 / `extension_decisions/1` | `d97a3540871e46dd19d5c84cce11509b35358e4bc34cc5dd58f535500cf316db` | C WP13 move-route §1 exact three line-start prefixes after evaluation; MR08/10–16; B03 row45 and B20 row311；PASS（有界） |
| 36 | GIR-FD82-C007 / `extension_decisions/2` | `c78705319c29dcf0fe686dc983f76a7cfe9d21d60138c90ccb20640ac6fee49b` | C WP15 resource compatibility rows; WP16 pre-battle Rocket IDs; WP17 color data; WP59 default24 values; B04 row86/B14 row174；PASS（有界） |
| 37 | GIR-FD82-C007 / `extension_decisions/3` | `69c7728b82d22e9658991c1ba78aa2613044fa76c31a79690d499e1f4b12369c` | C WP37 §3.1 KYOGRE 2/69↔21/31 adjacency and separate optional candidate gate; B08 row142；PASS（有界） |
| 38 | GIR-FD82-C007 / `extension_decisions/4` | `ed1eb17c12a59d0f7d0bbd3d2087406193d7338a32b7b5b971542e3ab7d52234` | C WP63 §4.6 PL01–18 legacy directory; WP60 §3.3/§10 sample-only berry scope unless full67 default compatibility promised；PASS（有界） |
| 39 | GIR-FD82-C029 / `root_adjudications/0` | `823ff4cb62475fe59b2fc672c9f5c68711d71e2f0bf6c4e34a129f180ab79f4c` | C WP77 §6.4 lines145–146 and demo test B20-C029 line278; WP21 §6/WP18 form-read gates; B20 row318；**NEEDS_REVISION** |
| 40 | WP80-B02-R02 / `root_adjudications/0` | `8906812c353ebb7a09ecea9e601df561aef52d32613255a8bfcfecfb4dda1083` | NEW historical-errata B02 rows + historical-carrier-errata; old batch02:14/81 remain immutable; original WP02 §4.3/appendix§7.2 destinations；PASS（有界） |
| 41 | WP80-INTAKE-C01 / `root_adjudications/0` | `7ca52d7d561498edb3f0bf254dbb49b40b0b9692da4b811277fa63d2a2958202` | NEW scope-counts/README current counts with seven-domain paths; historical wp80 completion:8–9/24 by successor only；PASS（有界） |
| 42 | WP80-INTAKE-R01 / `root_adjudications/0` | `25c07b607d03c3bf1c1ac87e8b6325c007d464c9fd6bc6284e523b0937970def` | C WP72 DG-M06 s: lexical contrast; full415/154/18 classification inherited; B19 row308/B20 row327；PASS（有界） |
| 43 | WP80-INTAKE-R01 / `extension_decisions/0` | `525c884d8e49f95a277b3527b10710ee88d8379d74d581da2790fed62b95d0d2` | C WP74 §15 Move:/OppMove:/Common: immediate concatenation; WP75 §§5/6/8 SellItem/item:/hiddenitem:/Trainer(N)/s:；PASS（有界） |
| 44 | WP80-INTAKE-R01 / `extension_decisions/1` | `c3636f3dac33d10692e819178d57f0db8b09adffc384ae58cdc8ad50ca442b83` | C WP13 ASCII counter/sight/trainer and WP14 size(2,1); EV27–29 and DG-M06, oldWP14:39 corrected separately；PASS（有界） |
| 45 | WP80-INTAKE-R01 / `extension_decisions/2` | `0eb38dc4a356062bd6d03c3b62e14abfb8dca4714d2a4625584a14bfa624ab91` | C WP59 §4.2 author PBS Weather= literal and WT38; B14 row194；PASS（有界） |
| 46 | WP80-INTAKE-R02 / `root_adjudications/0` | `1fe9f4e66220c56f481bfb18d8d9cf53c7f789ec256605489e0a10ce1ae26421` | NEW nine-input-approval-successor plus historical errata; exact old/input/current/original/final identities and accepted B18 row284；PASS（有界） |

审计过程说明：批准链子审计整理临时输出时曾因路径变量复用，短暂误写工作树 `review/remediation/20261003-prepare/batches/B01/author/historical-errata.md`；立即用固定 C 原始3003 bytes恢复，SHA256 `bafff7cd954b8150456518ad407b9768559cceeb407bfe619cc1e62088cbf624`，该路径 git status为空，未提交/发布误写。实质核验始终读取固定Git对象。本审计新输出全部写 `/tmp`；不得声称从未触碰历史工作副本。
