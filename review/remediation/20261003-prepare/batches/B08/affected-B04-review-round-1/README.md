# R-B04：B08 候选对 WP15–17 的限定复审（第一轮）

结论 **PASS_SCOPED**。固定候选 `0f35a393d9de467cd5f7e695b6072687bb582186` 相对接受基线 `759eee80ce7856570fde2de12d5dcf98ce7e6017`，仅核下列两组新调用条件对 B04 的影响；本范围内未发现新增缺陷，无本轮修复项。这不是完整 R-B08、B04 35 贡献／23 主责的重新验收，也不批准实际整合或关闭规范 ID。

## 版本与审查方法

候选唯一父为 WIP `d6367692610c83fd24bd1ab8d2ab0cfa6757314d`，WIP 唯一父为上述接受基线。候选树 `8fdbde0a7654c65b6efc7b7d71bcff6b63d5794e`，基线树 `8e6b6f5f15b6572a6ab69d6fe7da147ce20872e9`。报告分支 `remediation/20261003-prepare/review-B08-affected-B04-1` 从候选建立，只增加本目录；报告 commit 的完整 SHA 由提交后的普通 push／远端回读回执给出，不能把报告 HEAD 当被审候选。

冻结门来自基线的 B07 acceptance-stage-1/downstream-handshake.json，blob `38a405898d78d7bbe2f6731fefba284a7cd6a4bc`，SHA-256 `aa6a89bf6b6d6d6d3ef2bda437aa0de9fc014be99e5a282793ff683f4f4b62be`，880299 字节。读取固定 R-B07 报告 `7fd9271bc77b534e0eba5b47c77034e2453dd560` 的报告及 B04-affected-gate.json 后，我独立回读参考、反例及修订正文，不以其 PASS 替代本轮判断。

原问题与有效裁决绑定 GIR `93e10babe0b9c9ef8b3f5277754541b447beeeb4` 的 findings.json；计划／finding-acceptance 绑定 `41fffb540c6483f5296ea0d33b789b75180d27ed`。采用 current_qualifications 与最终逐项裁决优先规则，历史／raw 表述不扩大范围。A053 的 core／scene 区分、B026 的 a/b/c 公开候选基数门，以及 C003 的 C05 EN-16 强制单打前提得到本轮接口核对；不据此完成这些根的全部贡献。C003 的 EN-01/15/16 原稿不足与净化丢失按既有裁决区分，不新增重复根。

已读根 AGENTS.md 和有效冻结规范；相关目录未发现额外本地 AGENTS.md／SKILL.md。独立准备的参考 `/tmp/rb04-reference` 真实 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，树 `7589c800b61ba13a13040ed0d686979b80a84fd0`，origin Maruno17/pokemon-essentials；本轮复核 HEAD、真实 commit 类型与干净状态，之后只读。没有将参考加入主 Git，没有更改 ignore，没有向参考 push。

本轮登记新读 21 个参考文本文件、37 次范围读取、1726 个唯一行；精确已读／未读补集及文件 blob／SHA-256 在 [source-reading-log.json](source-reading-log.json)。范围行数不是分支覆盖。先冻结 [first-judgment.json](first-judgment.json)，后读取作者详细自检并比较；此前已读固定 R-B07 门、作者身份和原稿授权元数据，因此不声称完全盲审。之后补读大会选员入口及消息正常收尾，首判未变。

## 孵化：动态形态、资源、消息与恢复

范围：WP35 §5.2／9、EG-13／20 与原稿对应条款，接 WP15 的蛋／裂纹／前图／叫声，WP16 淡出边界和 WP17 实际消息。参考 EggHatching 13–40、52–137、202–268；Pokemon 147–178；FormHandlers 322–328；Time 201–203；Species_files 1–115、183–244；Pokedex 195–218。所有定位都固定在 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，详见 [affected-boundaries.json](affected-boundaries.json)。

| 静态前提 | 按调用顺序确定的结果与边界 |
| --- | --- |
| 普通非 Shadow DEERLING 蛋，存储形态0，无强制形态，steps1，月2，非战斗／非储存；有效玩家、地图、图鉴；无其它改写，媒体／消息正常，跳过命名 | 步数先归0，统计／名称／owner／来源／首招等 core 写入完成；场景读动态形态得1，提交存储形态、重算及已见形态。蛋图参数与裂纹选择在此后使用形态；前图／叫声也读取动态形态。通常 owned／seen-egg 在孵化消息之后。 |
| 同前提改月1；或有效非 nil 强制形态 | 月1仍0，无此次季节 setter；强制形态在处理器之前返回。战斗／储存短路也保留，不推广 EG-20 到这些状态。 |
| 更早 Huh／背景阶段抛错，未到首个场景形态读取 | core 写入已发生，但不保证季节形态已提交，不保证后续 owned／seen-egg。此处以实际抛错为条件，不把“背景文件缺失”一概判为异常。 |
| 已到月2形态提交，裂纹候选全部不可解析 | 裂纹解析可 nil；AnimatedBitmap 4–19 明确拒绝 nil，普通图像回退不能覆盖此入口。已提交 core／形态不回滚，未到 owned／seen-egg；异常不是演出正常返回 false，不进入文本替代分支。 |

蛋／裂纹按形态→物种→通用候选，前图按 WP15 独立降格，叫声按形态→物种；候选请求不证明素材存在或实际显示／发声。前图 nil 与裂纹 nil 后继错误不同；叫声缺文件可为时长0／无播放请求，播放自身有捕获，不能把所有媒体缺失写成同一失败。

实际消息链是 core 后 `Huh?` 暂停，再进 with-music fade，演出后清名称、发送空 SE 前缀的孵化文本及 wt80（逻辑等待4秒，不是墙钟实测），再通常图鉴写入；可选图鉴及昵称交互保持原入口。没有改富文本、兼容字符、命名或数字输入规则。MessageConfig 629–641 在 inner block 正常返回后才恢复位置／BGM／BGS；559–590 的确保只处理淡出／视口边界，不替它补造音乐恢复、领域回滚或场景资源清理。

候选正文与 EG-20 明确“媒体和消息正常返回”；EG-13 将“core 不显式改形态”与“演出查询可提交”分开。原稿 §5.2／9／已提交字段场景同步，未发现受影响 B04 接口的新增不一致。

## 遭遇：伙伴、单／双敌、选曲、消息与正常返回

范围：WP36 §3.3／4.1／4.4／7、EN-16／32 与原稿相关同步，接 WP16 的 foe 数／类别／位置／清理、WP15 BGM 和 WP17 实际调用消息。参考 WildEncounters 47–98、211–217、249–263；Overworld 172–217；BattleStarting 171–201、306–345、354–408；BugContest 171–196、350–404；BattleIntroAnim 59–151；BattleAudio 1–20。

| 静态前提 | 调用及后果 |
| --- | --- |
| 活动大会，已选一名可战玩家，Sport20／保留K，时限足，合法草地与 BugContest 表，概率／允许门通过，非 Safari，无雷达／漫游／其它覆盖／插件／布局残留；合法伙伴，force-single假，正常击败并返回 | 伙伴真门先于“一员假门”，取双候选；公开 start 只有单敌才派发覆盖，所以走普通 core／伙伴准备。包装传两敌数组、类别2；未传／回写大会预算，K未由大会存储改写，不发单敌 wild-end。普通 after_battle 因全局伙伴存在治疗玩家与伙伴队伍。 |
| 同夹具取消伙伴；或保留伙伴但 force-single真 | 一敌；允许覆盖且大会处理器未被先行接管时才走大会入口、类别0，预算20传入，正常包装返回后才回写预算。耗尽预算的公告／judging 是该单敌路径条件分支。不能只审大会 helper 就证明公开入口必选它。 |
| 早退／允许拒绝／正常返回 false／包装异常 | 各阶段合同分别成立；步进在开战调用正常返回后才清类型、置 trigger、复位 force-single。不能把这些步骤、治疗或预算回写推广为异常保证。 |

移动陆地汇总含 land／contest，普通陆地查询只含 land；仅大会表的合法地形可提供调用前提，仍须过后续概率／允许门。WP36 计数回绕改动在孵化事件链之前，但它没有改变形态月份、消息控制、音乐优先级或本轮两组 receiver 的规则。

类别2与位置2是不同输入。位置依次按 surf／dive→fishing→cave→indoor→outdoor 判定；伙伴／大会不会自行变成训练家类别。默认过渡对类别0／2走同一野生选择族，但自定义资格仍接收实际类别与 foe 数。正常包装返回才恢复 BGM／BGS、清记忆与位置、四类下一战预置、重置遭遇计步、请求0.4秒目标淡入并清 in_battle；其后步进调用者再清自己的字段。治疗发生在包装 body 内，不能等同异常清理。

Wild BGM 优先级仍是 nextBattleBGM→非空地图 wild→非空全局 wild→默认。入口忽略 foe 内容／数目／等级，所以 RM35 的48／52级不产生新音乐选择键。请求、宿主默认曲覆盖、音量与素材门沿 WP15；记忆交付与正常消费沿已接受 WP24，未扩大 B06 的引子／选曲接口。

实际野生入场文本由 Battle StartAndEnd 170–209 按一／二敌取占位文本，经 Battle 824–825 到 Scene 230–265。该场景暂停／skipAhead 不是通用 pbMessage 的 resume 合同；大会预算公告不能套给普通双敌。EN-16 给了 force-single 与伙伴的一正一反，EN-32 明确正常返回和20/K前提。原稿既有正确优先序及清理分层保持，双打场景同步了前提与 EN-32 指针。本门不验收完整战斗 UI、捕虫会话或伙伴捕获结算。

## 身份、同步和回归控制

独立 [340项身份／差异检查](independent-input-validation.json) 全部通过。基线→候选共57路径：12个修改输出（8正式＋4授权原稿），45个新增 B08 作者证据；无删改公共登记／其它历史，未扩大正式写入集合。79计划读身份（77基线、2固定报告）按合同复核，其中10个候选输入变化重新列出；其余2个输出也固定 before／WIP／candidate。这里只是身份审计，不宣称79全文语义已审。

四原稿的31346字节 v2 patch，SHA-256 `05b75bcafcb1fd9359e9a35e935e8b7cbb7dd038a0f3349a1172d1fe3ba88f25`，以及四份 before／expected-after 与候选字节精确一致。WP35／WP36 做相关语义核对；WP33／WP37 只核授权 footprint 和身份，不接管其业务验收。授权／先准备后写入的历史时序及跨容器锁没有独立追认，仍是 AUTHOR_SELF_REPORT_ONLY。

B04 的13个产物与本轮基线字节一致；WP24／28／30／34 的8份原／最终正文也未变。旧 B04／B07 复审有效范围保持：A048／C003／D023 的 B16 残余、B013 的伙伴捕获还原贡献不由本门批准。其它 owner 目录行精确保留；15新静态行与5旧行修订是整个 B08 差异统计，本门仅评 EG-13／20 与 EN-16／32 的 receiver 后果，全部向量执行数0。

| 保留差异证据 | 字节／SHA-256 |
| --- | --- |
| [完整无过滤仓库差异](complete-baseline-to-candidate.diff) | 2129917／913f8286c5ee1f56162aaed74777dd958e82ae219dafe45711d0645940d4d9e2 |
| [12输出完整差异](all12-output.diff) | 116226／3b753d70ecbbaea6b0b521749806db8337242effbab193adb676011f68152970 |
| [5受影响路径差异](affected-output.diff) | 53208／765aae13b7b9288f56ec2ec728eabc273e9eb0eb445c5e5c461f7013bf0f38c2 |

三个差异均由固定 SHA 独立生成（no-ext-diff／no-textconv／no-renames／binary／full-index／unified3），包括完整 evidence 足迹。作者短 index 的输出差异也按同参数形式另行复核；header 长度不同不当作正文不一致。独立首判和作者对照见 [author-comparison.json](author-comparison.json)。

## 仍保留的限制及交接

请求 gpt-6.1-sol／Ultra／Standard(default)，没有可信运行配置回显，实际 model／reasoning／tier 均 **UNVERIFIED**，继续已接受 Plan A。未新增认证、配额查询或配置确认门，未派生子任务。

U01–U10／G01–G12／AX01–AX20 与固定 scope-statement、先前 source-reading-log 的具名未读继续保留：二进制档案／真实地图事件、8个杯赛名单、pokemon_metrics 样本、宿主／mkxp配置、字体／素材／声字体、损坏媒体／真实容量、备份全文、动态／deprecated／插件组合、EventScene／动态阴影可达性与 Demo 链未证。容量1024／2048及宿主普通加载错误仍只是条件夹具。每个已开文件的本轮未读行补集明确登记；未把其它参考文件算成已读。

参考／游戏／编译／转换／反序列化／媒体读取／参考模拟器执行0，静态行为向量执行0，运行观察0，已证 Demo 链0。所运行 Python 仅审计 Git、JSON、字节身份和报告，不执行参考或重建行为模型。

仅本候选这两组 B04 接口可以给 PASS_SCOPED。完整 R-B08 仍由独立任务完成；将来准确 actual SHA 须再次核同两组、最终 caller／receiver 输入身份、实际整合差异与公共／追溯界面，不能移用本候选 PASS。B04→B07 串行条件和未来 WP28／30 或共享条件变化的 B04 复核门保留，父 C 最后决定，规范登记仍229 OPEN／0 CLOSED。等待父任务。
