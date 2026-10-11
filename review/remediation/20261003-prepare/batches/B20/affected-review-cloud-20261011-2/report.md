# B20 NEW2 独立 affected 有界再审

结论：**PASS_SCOPED_AFFECTED_CANDIDATE；本门剩余阻塞0**。上一轮 AF-01、AF-02、AF-03 在 NEW2 满足原验收条件；同一 C029 与 FULL-F03 重叠只计一组，另对 C024 和四个 ASCII 前缀修复的实际 owner 交界做了独立有界核验。五组修复与 B01–B19 支持接口未发现增量回归。此结论只绑定本次固定 NEW2，不签 FULL、actual、正式接受或 canonical 关闭，不重新批准旧308贡献。

## 固定身份及工作边界

| 对象 | commit | tree |
| --- | --- | --- |
| 本次 NEW2 | `3f521e6dea0b442e4bb174a9715c458416386b37` | `49f406a6de8ca2786e5dda27abada19780fdfa05` |
| 入口 E2 | `81d3be653e87e6424d0d8cd38dab14a9aafc97a1` | `a9d5db33399fee31780ea6cb6ffa3b5225b927ce` |
| 作者最终读回 P2、报告分支基点 | `dbfa219547690f06eac9180f3ecd9dd1091eb49f` | `59529b00d2a3704251f6622f3b1d7b55a186dfdc` |
| 上轮审查 NEW1 | `1abaefb1db5818ff9404392143c476979d34c21a` | `2e40f9ad0e8fa40377d39e5a19eaa74cc2e05e85` |
| repair BASE | `272885cca76c36cd04dde27b6be2c654759ec4c2` | `46969272b7387645bc97b91d227734e89a5f8a80` |
| B19 接受基线 C | `de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f` | `88a400af08253bea8d97ee2ef2fa6636f0900f92` |
| 旧独立 affected 报告 R1 | `680e3988c4144db269e063971991134b8e0bd678` | `4e2858fe6d52e9b36ede5a54a9ad730c05764108` |
| 静态参考 S | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` | `7589c800b61ba13a13040ed0d686979b80a84fd0` |

入口为 E2 的 [candidate-review-2/affected.md](https://github.com/y805939188/pokemon-essentials-clean-room/blob/81d3be653e87e6424d0d8cd38dab14a9aafc97a1/review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-2/affected.md) 和同目录 [repair-navigation.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/81d3be653e87e6424d0d8cd38dab14a9aafc97a1/review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-2/repair-navigation.json)。报告分支为 `review/b20-affected-cloud-20261011-2`，只新增本目录。报告自身 commit/tree 在普通发布后由后继 publication 凭据绑定，最终包由第二次独立远端读回及最终回复给出准确身份。

原报告及证据保留在既有固定 R1 和最终包 `be3363e8711bdf17b0f08e22517ec3bb00f9ef55`；它们位于独立报告分支，不因作者 NEW2 树没有该目录而算作删除。本次没有复制它们的正文。未变内容继承 R1 的固定 commit/path/blob/SHA256/范围证据，并核对增量身份和真实消费者条件，不无变化整库重读，也不把文件无交集当作未受影响理由。

原派发 `669997ac28258f26d0bafc81b1d081abb407a3a1`、原 qualified PLAN/acceptance `41fffb540c6483f5296ea0d33b789b75180d27ed` 及 finding `93e10babe0b9c9ef8b3f5277754541b447beeeb4` 的 root/extension、有效 case、最低修订、前提、确定再检、其它 owner 与最终全局义务继续绑定。scope `924c7c3a7a5029b07ad18085cf2dadb594512186` 的两份原稿三 hunk 仅核允许写入及精确应用；许可、作者 completion、导航路线和数量均不计为质量通过。

## 完整差异及有效案例

无 pathspec、无外部 diff/textconv、binary/full-index/no-renames、无忽略空白地在内存重建完整 BASE→NEW2，与已发布流逐字节一致：**451,455 bytes、33路径、SHA256 `0096cacd3fefe3dcb85857300114224b6195deb3f536c22952c75a75845abc1c`**。唯一发布引用：commit `a9323ee064a4931fa8c218cfe24a060acc4c2e86`，path `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-2/stream/BASE-to-NEW2.full.diff`，blob `355aca2a456562a5e0799cf36957262ff84c88d9`。没有再次保存或发布差异流。

旧 C→NEW1 流独立重建仍匹配原固定 `f325f625f879105f7811713d9a38cc58da875de2` 的 `candidate-review-1/stream/C-to-NEW.full.diff`，blob `54c4dcf3be88f175fcceaca5c3642c29c532adfe`，SHA256 `0889ed6d2a4d300325c0fa5d319d9fd89b72bdaeec8e8a0401c7185a25f9eccb`。NEW1→BASE 三个提交只有作者证据新增。完整 C→NEW2 也在内存核对，**3,052,784 bytes、82路径、SHA256 `35175e1a164b62c4c190617609a0a940b90f35a801a26d4be32d340b85fa16c7`**；不另发递归大包。

相对 NEW1，实际正文/目录只有五个修改路径：正式 WP75、正式 WP77、共享目录、原稿 WP75、原稿 WP77；两份 WP74 全文件不变。NEW2→作者最终 P2 只有13个作者证据新增，既有正文及对象不变。详见 [metadata-verification.json](metadata-verification.json)。

固定 active successor 为 `bfc6264bf47478bd174412289de2e31f4da2d9a6` 的 `author-draft-1/candidate-fix-1/five-group-static-cases.json`，blob `1bcabfa4982655b6ccf971dba508e5ea690efc3b`，SHA256 `14e51d538294bbbe8bfdd10dfd78b1091a99fa5f5ea39d7771dcfacae7196515`，34,659 bytes；NEW2 中同字节。五组分别3/12/14/12/10，共51个子例逐项静态核验，均 NOT_EXECUTED、observation=null、quality_verdict=null。full19-active-case-map 的19个 contribution/pointer 绑定均核对；其余14项旧 case/限定不由51子例替代。历史 per-ID 的旧错误预期仍作为冻结证据引用，本轮按明确绑定的 successor 判断，没有要求改写旧证据。

## 五组修复与旧反例

完整固定证据身份、行范围、静态反向和验收判断见 [findings.json](findings.json) 及各子报告。本节的路径行号指固定 NEW2，源码指 S；所有反例均未执行。

| 修复 | 本次独立支持与验收判断 |
| --- | --- |
| C029：AF-01 / FULL-F03 | 正式WP77:145–146、原稿新增:174–176、目录:278和active `/static_cases/3` 明确 forced存在含0先返回；否则战斗/仓库各短路返回stored；两状态均假才到动态处理器。指定物种/宝珠/旗标的0/1、不同候选提交及form_simple不求动态，与WP21/WP18和源Pokemon:147–166/FormHandlers:267–272一致。stored0+宝珠/旗标在战斗或仓库仍0，stored1+无两条件仍1；原AF-01反例已排除。正确原稿局部handler审计只移行，字节保持。 |
| C028：AF-02 | 正式WP77:113–121、原稿:137–145、目录:277和active `/static_cases/2` 准确区分：缺训练家记录空文字；TE全局请求遭遇版缺回地图0版；双版缺及三表空为空文字。训练家max版本与TE版本独立，成员次数/首最多4槽均匀/不去重/不按野生权重保持。消息开始→TP一次→TE一次→地图名→全段复用→收尾；无占位符仍计算，空party/非法参数/非法物种失败按阶段限定。源Phone:414–438/506–535、Encounter:30–35及旧WP63支持，未增加非空替代、异常保护或注册成功保证。 |
| C003：AF-03 | 目录:270和active `/static_cases/0` 改为CN读玩家coins、G读money，合法coins37/money1200及coins0对照支持数值语义；显示格式继承WP17。源Messages:310–343/584–592与Player字段支持，无金银铜分层。旧CV-M14、B19/PA040行及midi/CommonEvent/b/pg/标题边界保持。 |
| C024：FULL-F01的affected交界 | 正式WP75:48/282、原稿:304、目录:273和active `/static_cases/1` 顺序为数量门→建/清树→逐节目录/脚本输出→备份→loader，无独立索引文件。清树成功后首文件打开失败时旧树已删、备份未到且原值/不存在状态保持、原归档不变、无loader；清树/后续文件/备份/loader失败分别保留已发生前缀、可能截断/部分写入，无全局回滚。9/10/11两入口数量门保持，源scripts_extract:12–66/71–73/154–179及combine门支持。 |
| INTAKE-R01：FULL-F02的affected交界 | 正式WP75:26、目录:287和active `/static_cases/4` 四前缀正向冒号均为U+003A，U+FF1A只为负例；item/hiddenitem/Battle/Type前缀大小写不敏感，登记身份、有效页和Battle门独立。全角Type只排除其提供的类型，不能说其它合法Name/Battle也被清空。源Compiler_MapsAndEvents:473–529/556–570/771–807支持；未扩展到Common精确拼接、SellItem、治疗或其它括号/逗号/大小写门。 |

前三个局部 AF 编号只在本门被标为“对 NEW2 已解决”，不改 canonical finding。另两组只判断实际 affected 交界及增量，不签 FULL 原19/15总审。独立挑战检查没有找到仍成立的反例，见 [b20-r2-challenge.md](b20-r2-challenge.md)。

## B01–B19 影响与保留范围

每行保留结论由固定旧接口/条款身份及实际消费条件共同支持；不是旧整包重签。完整身份与未变范围哈希在对应 JSON 中。

| owner | 本次有界影响与增量判断 |
| --- | --- |
| B01 | WP75提取/合并阶段IO、WP74映射写回、共享目录reader；C024纠正部分写入顺序，不扩成PBS新鲜度、配置/插件或持久事务保证。 |
| B02 | 目录进入/文件加载局部失败与WP75工具交界；五组不改变文件占位≠目录捕获、正常释放≠异常必达的旧门。 |
| B03 | 四前缀ASCII/大小写修复只影响具体收集/解析门；训练家、道具登记/页/Battle门及门事件开关22、转移、跟随快照/路线/等待等真实条件保持。 |
| B04 | CN/G及电话消息开始后候选失败、C024文件阶段交界；不增加窗口/BGM异常恢复或全局回滚，AF-03修复有支持。 |
| B05 | 实际WP77 getter→WP21/WP18门和提交条件；AF-01修复有支持，其它物种/形态旧资格保持。 |
| B06 | CN→WP24 coins而G→money；两字段及旧库存/容量保持，前缀识别不重新定义资源域或35行旧词法表。 |
| B07 | 公共动画名消费与成长阶段仍分开；WP74和旧成长接口不变，未把CN/前缀或形态读取变为经验、库存、进化成功。 |
| B08 | 电话资料均匀首4槽与WP36实时遇敌/加权装配分开；平衡级完整数学及缩放条款未变，不从联系人版本/地图推出实时遇敌或生成成功。 |
| B09 | 保留WP75六族输出→WP39创建规则的实际路由；整节不变，前缀不敏感不扩大到六族脚本名/元数/尾参，战斗演出不替代参战/结果。 |
| B10 | WP74和每击伤害/HP/恢复先后接口不变；五组没有数值输入，动画帧/槽不能成为HP。 |
| B11 | 保留WP47-A动态类型/环境借用/Ghost→动画映射/偏移的间接route；B11不是电话owner。旧目标/PP/能力持物/未决保持，前缀不敏感不传到动画登记身份。 |
| B12 | AI评分/效果绑定与演出仍分开；WP74及旧查询限定不变，不推出纯查询、统一回滚或完整AI质量通过。 |
| B13 | Copy/Paste独立、Insert联动与记录/回放仍分开；WP74、WP77设施段及旧记录条款不变，形态修复不证明设施/回放实际执行。 |
| B14 | WP75治疗词法→WP61 Recover All成员/存储设置接口保持，精确词法与残留/持续插入边界不变；前缀校正不扩大到治疗/SellItem/中心构造，C024不增加全局恢复保证。 |
| B15 | 电话候选/播放reader的AF-02修复有支持；联系人登记、CommonEvent、呼出和消息生成仍独立，图鉴/邮件/礼物旧范围保持。 |
| B16 | WP74屏幕倍率/缓存/临时集合/首槽空/正常生命周期及旧WP65不变；新增IO/电话失败不保证所有UI清理或改变BoxLink/物品/BP/槽规则。 |
| B17 | 实际WP67-A动画播放reader保持；Move/OppMove与Common各自匹配、缓存/槽号/重编译门不由四前缀大小写修复替代，PA040及入口限制保持。 |
| B18 | Game Corner只读能力reader、素材及各游戏自身状态/资源/完成门保持；形态补充不使场所登记成为可玩或奖励成功证明。 |
| B19 | 六个真实输入及旧120效果、取消/PBS写回/缓存/快照/资源复制/CommonEvent/ASCII边界按旧固定证据保留；仅新增CN、C024、前缀消费者修复，不回写旧17行或PA040。 |

“无直接声明route”未用于排除B05/B06/B11；B09创建规则及B17实际播放reader继续纳入。十个其它owner的82个PLAN路径出现/71个不同路径保持，五个相关整节与三个单行保持；B05/B07/B08另核31条旧身份。实际未变接口的固定对象比较和限定分别见 [forms](b20-r2-forms.md)、[phone/CN](b20-r2-phone-coins.md)、[IO/ASCII](b20-r2-io-ascii.md)、[其它owner](b20-r2-other-owners.md)。

## 接受贡献、目录和输出保护

固定旧独立保留 proof 的身份再次核定，结合增量 Git 绑定保留 **308个(owner,ID)、205主责、216触及ID**及原 qualified 控制；**2,757个旧owner证据文件全同**，既往actual不重跑/重签。两份WP74不变，68个旧作者输出在完整固定发布基点Q `cd714a3cba8319402ddd81d2bebd8fe1d215003a`（tree `99e32a4bd4d0c1a095216aa5ae515be6a8e335d5`）保留；没有把较早P只含65个文件的计数当作丢失。

完整共享目录 C→NEW2：旧195 ID顺序/重数保持；193原C旧行逐字相同；AN-M23/CV-M18仍为上一候选已经assigned的原值修订，没有二次修改；17个B19行、3个PA040行不变。NEW1→NEW2全部214 ID顺序/重数保持，209行逐字相同，恰五个新B20行修复。scope两原稿3 hunk逐范围重建与完整after一致，未越允许写入；质量仍由上述源条件/反例独立判断。详见 [b20-r2-preservation.md](b20-r2-preservation.md) / [JSON](b20-r2-preservation.json)。

root亲读五正文增量、51个静态子例及关键源条件，合并六个独立有界子审并读其最终报告；导航/旧报告清单身份、有效case绑定与新增输出另作元数据核验。六个子审的250个唯一固定引用对象、126个数值行范围哈希和21个pointer再核通过，均为有限引用的身份/文本元数据核验，不重读未变整库语义。源仅静态阅读，未执行参考游戏、Ruby、编译器、转换器、反序列化器、行为向量或旧执行脚本。仅运行自己新写的Git/JSON/hash/text元数据代码；所有静态案例不是运行测试，运行观察/已证明Demo链均0。U01–U10/G01–G12/AX01–AX20及宿主、插件、媒体、未读、conditional等旧限制继续绑定。

剩余问题清单为空；本门没有输入、工具或已知发布阻塞。下一正式步骤仍须另一路FULL candidate独立结论，再由唯一登记者G固定ACT并按原合同完成独立两路actual、登记及发布读回；本报告不代做这些步骤、不合main、不改canonical状态。

## 支持文件

- [问题处置与验收](findings.json)、[完整差异/固定输入/有效绑定](metadata-verification.json)、[证据身份及输出核验](evidence-identities.json)、[输出清单](output-manifest.json)
- [形态](b20-r2-forms.md) / [结构证据](b20-r2-forms.json)
- [电话/CN](b20-r2-phone-coins.md) / [结构证据](b20-r2-phone-coins.json)
- [阶段IO/ASCII](b20-r2-io-ascii.md) / [结构证据](b20-r2-io-ascii.json)
- [其它owner](b20-r2-other-owners.md) / [结构证据](b20-r2-other-owners.json)
- [保留](b20-r2-preservation.md) / [结构证据](b20-r2-preservation.json)
- [挑战检查](b20-r2-challenge.md) / [结构证据](b20-r2-challenge.json)

报告文件不预填自身commit/tree。普通推送后的全部输出独立读回凭据见后继 `publication/report-readback.json`；最终发布包身份与第二次全部输出读回由最终回复绑定。
