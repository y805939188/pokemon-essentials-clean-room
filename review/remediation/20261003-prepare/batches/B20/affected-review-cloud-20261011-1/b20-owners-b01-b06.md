# B20：B01–B06 已接受 owner 有界影响复审

审查 NEW `1abaefb1db5818ff9404392143c476979d34c21a` / tree `2e40f9ad0e8fa40377d39e5a19eaa74cc2e05e85`，基线 C `de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f`。入口包 `9a46a131ba2f7ea82b6eed823aa892cb57b0fba7`，入口 `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-1/affected.md`；最终读回包 `272885cca76c36cd04dde27b6be2c654759ec4c2`。固定派发 `669997ac28258f26d0bafc81b1d081abb407a3a1` 的 accepted-interface-map 与原 PLAN/完整批准限定只作控制，实际条款、参数状态、逆向 reader 和源文本决定影响。

结论：本范围 REQUEST_CHANGES。AF-01 为 B05 新 getter 合同缺门；AF-03 为 B04/B06/B19 新 CN 消费者预期错误。B01/B02/B03 有界新增 reader 检查未发现阻塞冲突。保留六批原 114 项接受贡献，70 个正式路径元数据条目在 C/NEW 全部同 blob/SHA256；B01–B06 旧证据目录树全部同一 tree。此处不重新签这些 actual，不把局部复审扩大为旧308项重审。

仅静态读取；参考、Ruby、编译器、转换器、反序列化器、行为向量、旧执行脚本均未执行。所有案例 NOT_EXECUTED；运行观察与已证真实 demo 链均0。参考固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。

| owner | 旧主责/贡献 | 有界实际接点与结论 |
| --- | --- | --- |
| B01 | 7/14 | WP75编译阶段、WP74动画映射写回与Demo目录逆向reader；编译顺序/部分写回不改PBS新鲜度、配置/插件资格，未发现阻塞冲突。 |
| B02 | 9/12 | WP74目录进入先于窗口、空表/文件占位、正常返回清理及WP75文本转换；文件捕获与目录传播分开，未发现阻塞冲突。原PLAN的WP75读路径也已检查。 |
| B03 | 19/27 | WP75继承条件/末向前全门选页、原201参数、210等待、跟随者可见/隐藏状态与路线45词法；NEW WP75:89–95/111–124/233–245，与C WP11:49–61、WP13:28–31/55–60/112–119及路线矩阵:9–18/71对应，未发现阻塞冲突。不是全地图/地牢再接受。 |
| B04 | 23/35 | WP74:59–75资源失败边界与C WP15:85–98一致；格式码新增案例违反C/NEW WP17:47，AF-03阻塞。 |
| B05 | 10/16 | 作者空route不能豁免实际WP77→WP21形态消费者；AF-01阻塞，原稿正确handler事实保护。 |
| B06 | 7/10 | WP75:143–190是兼容文本而非新对象API；WP77:149–155消费完整party数学输入，不改变WP25容量/占位。新增CN实际读WP24 coins字段，关联AF-03；不标无实际影响。旧party/bag部分失败资格保持。 |

AF-01 / P2：NEW `deliverables/final-specification-set/demo-dx/wp77-demo-evidence-and-capability-coverage.md:139` 声称 getter 被消费、无 forced override 时即可按宝珠/旗标求形态，NEW Demo catalog:278 和 per-ID JSON:130–137重复缺门。固定源 `Data/Scripts/014_Pokemon/001_Pokemon.rb:147–152` 在调用handler之前，先取forced_form，再在battle或storage中直接返回stored form。源 `001_FormHandlers.rb:267–272` 的GIRATINA handler局部0/1事实正确。C/NEW已接受 WP21:246明确战斗/仓库不调用handler。

静态正常：无forced且不在battle/storage，GIRATINA有GRISEOUSORB或DistortionWorld→1，皆无→0。反例：stored=0、forced=nil、storage=true且orb/flag真→getter仍0；反向：stored=1、forced=nil、battle=true、orb/flag皆无→getter仍1。forced=2优先返回2。验收需在新增正式getter条款及C029案例补明确实际到达handler和两外层门，给上述相邻静态对照，保留其它物种与运行未验证限制。NEW `specs/demo/wp77-demo-evidence-and-capability-coverage.md:163` 只描述handler局部、引用FormHandlers:267–271，原稿正确，不请求修改。

AF-03 / P2：NEW Demo catalog:270 与 per-ID JSON:32把CN写为“金银铜钱”。固定源 `Data/Scripts/007_Objects and windows/011_Messages.rb:330–343/587–589` 的cn分支消费 `$player.coins` 单一代币字段。C/NEW WP17:47、旧CV-M14:157均正确为代币窗；B06 C/NEW `creature-rpg/wp24-player-trainers-partners.md:63/91–98` 区分money与游戏币，源 `015_Trainers and player/004_Player.rb:11–16/78–87` 明确不同reader/整数钳位入口。

静态对照：money=100、coins=7，合法CN请求coins窗取7；另G请求money窗。没有金/银/铜面额换算分支。验收只纠正新增案例为CN代币窗/游戏币字段，保留旧CV-M14字节、必要尾随空白与反向识别边界；B04/B06旧资源域、库存/party资格不撤销、不整体重审。

B03/B04 源核查包含：Compiler_MapsAndEvents:1–38/473–579/633–645/727–760/815–902/951–974/1135–1191/1683–1748；Game_Event:197–211逆向全门选页；Game_Character:539–548路线45先eval后准确前缀；Interpreter_Commands:722–746/871–874/1099–1107区分201参数/210等待/全体治疗；FollowerFactory:193–237/252–257累计路线与持久hidden；Overworld:489–524 wrapper未消费waitComplete。资源源核查分别定位AnimEditor_Functions:29–65/504–593/1157–1170、SceneElements:409–421/947–964、ExportImport:7–16、AnimatedBitmap:4–19/137–151与FileTests:216–242。路径/固定SHA/全文件及具名范围SHA256在同名JSON evidence中。

不递归复制完整差异或旧证据。唯一已发布C→NEW完整差异只引用 `f325f625f879105f7811713d9a38cc58da875de2:review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-1/stream/C-to-NEW.full.diff`，blob `54c4dcf3be88f175fcceaca5c3642c29c532adfe`，SHA256 `0889ed6d2a4d300325c0fa5d319d9fd89b72bdaeec8e8a0401c7185a25f9eccb`，1189663 bytes。完整差异独立重建与195旧Demo行顺序/重复保护由root总报告集中记录；本子报告已独立核六批旧目录整文件身份及旧证据目录tree。

同名JSON为逐owner scope/evidence/decision、固定对象哈希、问题与验收条件的自写结构化报告。U01–U10/G01–G12/AX01–AX20、具名未知和正常返回/部分失败边界保留；未自签actual或正式接受，未写正文/main/reference/旧证据。
