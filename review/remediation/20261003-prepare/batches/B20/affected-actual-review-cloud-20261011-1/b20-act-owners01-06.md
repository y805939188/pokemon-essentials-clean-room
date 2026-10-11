# B20 ACT：B01–B06 独立有界 affected actual 复审

结论：**PASS_SCOPED_AFFECTED_ACTUAL_B01_B06**；本范围剩余阻塞 **0**。此为固定 ACT 的独立有界 actual 判定，不转签 candidate、不签 FULL、正式 C 或 canonical 关闭。

- ACT：commit `6babcf657aef559dbf101aeb093a1beb730ab507`，tree `7f511347be10a55ed1341f4132e198ac6bdedede`。
- management_packet：commit `66ba31f7895067c9d925aba20ce3de046fbf60e7`，tree `2f30f3ae648c593a32c52e2598a968bf677317ea`。
- reviewed_NEW2：commit `3f521e6dea0b442e4bb174a9715c458416386b37`，tree `49f406a6de8ca2786e5dda27abada19780fdfa05`。
- accepted_C：commit `de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f`，tree `88a400af08253bea8d97ee2ef2fa6636f0900f92`。
- prior_independent_candidate_package：commit `7c5309763a6cf2e31564a1fe42786ebcbfecbef5`，tree `e15b4d6548b9e22975a38fa9b61f9056d585e04d`。

入口：管理包 `66ba31f7895067c9d925aba20ce3de046fbf60e7` 的 `review/remediation/20261003-prepare/batches/B20/actual-freeze-1/affected-actual-dispatch.json` 及同目录 `affected-owner-entrypoints.json`。入口、scope、作者完成标记、candidate PASS 只用于定位及控制，均未作为本判定的质量通过依据。

七个 ACT 正式/原稿/目录 payload 逐字与固定已审 NEW2 相同；NEW2→ACT 规格差异为0。身份相同只支持归因复用已审语义，本审另按每个 owner 的实际条款、调用者、数据、条件、间接 route 和原完整 qualified 限定作 actual 判断。所有固定 commit/path/blob/SHA256/bytes、具名条款范围哈希与指针见同名 JSON；完整流由根报告统一独立重建核对并引用，此处不复制。

| owner | 旧贡献/主责 | ACT 的实际受影响接口和有界判定 |
| --- | --- | --- |
| B01 | 14/7 | WP75工具提取/合并阶段与编译主驱动、WP74动画映射写回、共享目录的逆向reader。C024首个文件失败发生在清树之后且备份之前，后续工具IO可部分写出；数量门、独立工具入口和编译调用入口各自保留。 **PASS_SCOPED_AFFECTED_ACTUAL**，阻塞0。 |
| B02 | 12/9 | WP74选择器先进入目录和枚举再构造窗口，文件加载占位/nil与目录传播分开；WP75文本转换、消息提取与C024阶段失败为实际接点。先前路径有文件不能绕过后续缺目录；空列表三类选择器仍不同。 **PASS_SCOPED_AFFECTED_ACTUAL**，阻塞0。 |
| B03 | 27/19 | WP75四前缀item/hiddenitem/Battle/Type的ASCII冒号和局部大小写不敏感收集；独立注册、合法页、有效Battle门仍须满足。生成页继承启用条件、末页优先且全条件合取；门改写保留开关22及结构门。转移201/等待210、跟随者快照/持久隐藏/累计路线和路线45求值后准确前缀均作为实际运行reader判定。 **PASS_SCOPED_AFFECTED_ACTUAL**，阻塞0。 |
| B04 | 35/23 | WP74资源匹配/缺目录/具名图保护与消息生命周期；ACT新C003明确CN读取coins、G读取money且保留原CV-M14。电话开始消息可能先于TP/TE候选失败；工具C024部分写出不增加音画收尾保证。 **PASS_SCOPED_AFFECTED_ACTUAL**，阻塞0。 |
| B05 | 16/10 | ACT WP77普通getter实际消费WP21/WP18：forced存在含0优先；无forced时battle/storage真直接取stored；仅两状态均假才调用动态处理器。GIRATINA的指定宝珠/DistortionWorld仅在实际handler调用时产0/1，候选不同才按主规格提交；form_simple不调handler。原稿正确handler-local审计保留。 **PASS_SCOPED_AFFECTED_ACTUAL**，阻塞0。 |
| B06 | 10/7 | ACT新C003的CN→WP24 coins、G→money为真实间接route，即使原map没有直接route仍判定。WP75旧背包/玩家/队伍名是35行文本兼容而非新对象API；WP77平衡等级输入含蛋/濒死全party，不改变WP25容量/占位、接收或库存写者。 **PASS_SCOPED_AFFECTED_ACTUAL**，阻塞0。 |

## 旧限定与未受本增量影响的范围

- **B01**：原WP01–05配置、PBS整秒新鲜度、内容身份、插件假值/顺序与批次2残留等限定继续绑定；新工具IO不形成全PBS新鲜度、持久事务、插件正常执行或回滚保证。
- **B02**：原WP06–10单位/帧率/零值回退、目录删除与异常层次、本地化、读档/新游戏及无存档门保持；正常释放和主窗口/BGM恢复只支持正常返回，不新增宿主异常显示/恢复观察。
- **B03**：原WP11–14双端通行、连接跨界、取消/输入竞争、解释器矩阵、ASCII兼容字面、地牢固定图样/退化/失败限制保持；不把词法转换变成语义等价接受，也不将单个前缀识别变成整转换或战斗成功。
- **B04**：原WP15–17资源匹配/失败、音频包装/记忆、图片计时器灯光34场景、文本/命名/动画静态时序以及媒体宿主未知保持。CN格式细节继承WP17，不新增金银铜面额或异常必清理。
- **B05**：原WP18–23默认字段、25性格、形态招式、ROTOM唯一招删除、Mega石、h255和可选Shadow/参考异常等16贡献限定保留；其它物种归各自主规格，不由本条重新判定。地图进入/Demo实际变形未证，读getter不证明升级/进化/更新链已运行。
- **B06**：原WP24–27雷达钩子/伙伴门、检查入口例外、追加和早盒优先、静默接收/非蛋前提、对象身份、容量及bag/party部分失败边界保持；CN只读独立字段，不撤销旧资源域或重新签旧库存完整合同。

上述六批 **114 项旧贡献、75 项主责**与原 PLAN 的 ID/primary 准确一致；ACT 全部历史 receipt 字段保持。70 个已接受正式路径元数据条目（67个唯一路径）C=NEW2=ACT，六批旧证据目录 tree 完全相同，545 个旧证据文件逐 mode/path/blob 元数据保持；六个 acceptance 容器与 C 同 blob。114 个公共 ledger 旧行的字段与重复次数保持。原完整根/扩展、前提、最低修订、确定复查、effective case、非局部义务与证据限制继续绑定固定已审全对象指针和 hash，未以局部示例或五组 successor 代替。

B05 与 B06 的原 declared route 为空仍有实际 reader：WP77 普通 getter 消费 WP21/WP18，CN 消费 WP24 coins。故本报告不将“未改 owner 正文”或空路线标记当成不受影响证据。相反，实际 route 逐条件核定；其它不变内容由完整对象身份、旧固定 consumer/source 判断及保留限定共同支持。

ACT 整合登记与外部有效案例绑定保持可审：管理包明确绑定 NEW2 的 five-group-static-cases、full19-active-case-map、all19-author-map 以及整套 qualified effective-case aggregate。candidate 临时目录不在 ACT 中，不意味着外部已固定有效案例被撤销；本审核验其指定 blob/hash。登记仍为待 exact actual/FULL/C、下游 held，未凭整合文字制造运行证明或已接受 C。整合全308/全目录及 scope 链由根报告统一核验，本报告限定自己六批114项。

## 独立相邻静态对照

| 对照 | 前提与唯一预期 |
| --- | --- |
| ACT-B01-IO-STAGE | 合法11节归档，清树已成功，首个非空文件打开失败 → 旧散文件已清；备份未到，既有B0或原无备份状态不变；原归档未改，不保证全局回滚或UI收尾；**NOT_EXECUTED**。 |
| ACT-B02-DIR-VS-FILE | 资源前一路径已有文件，随后目标目录缺失 → 目录枚举阶段在窗口构造前传播；文件占位保护不能救该目录失败；**NOT_EXECUTED**。 |
| ACT-B03-ASCII-INDEPENDENT-GATES | item/ITEM或Battle/battle带ASCII冒号，对照仅换全角冒号，登记/页/其它块前提分开 → 局部前缀大小写不敏感，全角不匹配；通过前缀不保证登记、页、完整转换或战斗成功；**NOT_EXECUTED**。 |
| ACT-B03-ROUTE-FAILURE | 路线45脚本有准确move_random前缀，但求值抛异常；另前导空白的正常脚本 → 异常不推进索引；正常脚本才检查原文本，前导空白不命中提前结束门；**NOT_EXECUTED**。 |
| ACT-B04-B06-CN-G | 合法CN/G，coins37/money1200；coins改0但money不变 → CN读coins37后0；G仍读money1200，格式化继承WP17，无金银铜分层；**NOT_EXECUTED**。 |
| ACT-B05-STORAGE | 无forced，stored0，指定宝珠或旗标真，storage真 → 普通读取仍0，不调用动态handler；未证Demo形态变化；**NOT_EXECUTED**。 |
| ACT-B05-BATTLE-AND-FORCED0 | 无forced/stored1/宝珠旗标皆无/battle真；另forced0/stored1/宝珠旗标真 → 前者返回stored1；后者forced0优先，不调用handler或提交；**NOT_EXECUTED**。 |
| ACT-B06-PARTY-MATH | 合法队伍包含蛋或濒死成员，其等级用于WP36平衡级 → 全队伍成员参加数学输入，不过滤可战斗队伍；仍不改变存储容量/接收/背包写入合同；**NOT_EXECUTED**。 |

## 固定已审证据归因

| 用途 | commit / path / pointer | blob / SHA256 |
| --- | --- |
| prior_owner01_06 | `680e3988c4144db269e063971991134b8e0bd678` / `review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-1/b20-owners-b01-b06.json` | `4c1c87dfe2b3e73bc2b9edb5e18b1ec97ad4abbe` / `04f06aadbe1ebd87e14f6c120052f54fad2ebd6e834e086bdb56dc8f97e36c36` |
| prior_qualified_preservation | `680e3988c4144db269e063971991134b8e0bd678` / `review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-1/b20-preservation.json` | `3f53b569f69097421a1302df3c66d0388cd0eba2` / `5612de987509aebf71f432f69fc27a9c30c354adfeec5860a33442265d81da42` |
| r2_io_ascii | `7c5309763a6cf2e31564a1fe42786ebcbfecbef5` / `review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-2/b20-r2-io-ascii.json` | `53b70270cab06b8d6c3b2ab4223fe0decbf2ee58` / `2168903987c5a923be9fe57fa14944e4028430bca7ab6a4cb43940c5421e34ed` |
| r2_forms | `7c5309763a6cf2e31564a1fe42786ebcbfecbef5` / `review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-2/b20-r2-forms.json` | `9a8b5bbbe7ebd246d9abc7f11a080e27b35ef2d5` / `8a9c96543212db6b25c3f1cce1e582c97ed2b8c9c088a9bd055e7fc202ddf53c` |
| r2_phone_coins | `7c5309763a6cf2e31564a1fe42786ebcbfecbef5` / `review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-2/b20-r2-phone-coins.json` | `ccfa3096abcb072e05cec9af54f88b4a08fec2c0` / `b2759b7676bfb91fc8599a0ec8a3ceef71ca328d58d810771b136c729f16b580` |
| r2_preservation | `7c5309763a6cf2e31564a1fe42786ebcbfecbef5` / `review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-2/b20-r2-preservation.json` | `5524083b0bf8e6b0a7aeb485ebbc28c99f520549` / `85ff5a7e8cbacbcadec2c88d2dc1f406d72800f97271b1d7471df93c5eead174` |
| original_PLAN | `41fffb540c6483f5296ea0d33b789b75180d27ed` / `review/remediation-20261003-prepare/batches.json` | `9dd98a6b96d49294d214f7e9a53eac8738c1484c` / `3758c04581500a29c0fa8dd727d8d6026a4ed2934c42b1778b1ff18e6fdbb02f` |
| whole_approved_acceptance | `41fffb540c6483f5296ea0d33b789b75180d27ed` / `review/remediation-20261003-prepare/finding-acceptance.json` | `e178e5706771f5f7465bcf3351b5c632a5d68bab` / `54e4c86be3db493a5463ce4bcdef81c7184f1a1d89e6b3bbea358f14cc347225` |
| accepted_interface_map | `924c7c3a7a5029b07ad18085cf2dadb594512186` / `review/remediation/20261003-prepare/batches/B20/refreeze-after-B19-C-1/accepted-interface-map.json` | `265041e0830bd47130492e314c67520bb738f562` / `80dde444746b204e6d2a1985da7d41e5bb51e8ae3e2557b9847e8c91055ee28c` |
| actual_dispatch | `66ba31f7895067c9d925aba20ce3de046fbf60e7` / `review/remediation/20261003-prepare/batches/B20/actual-freeze-1/affected-actual-dispatch.json` | `07dd910c0cde97e16a793707500329f16f7b6267` / `1c149a9fe3a455dfa033418c85fc9d9f13e660dea383bd61ac6fcc2aa27b657a` |
| all_complete_effective_case_aggregates | `924c7c3a7a5029b07ad18085cf2dadb594512186` / `review/remediation/20261003-prepare/batches/B20/refreeze-after-B19-C-1/control-and-acceptance-overlay.json` / `/complete_case_aggregates` | `3040e2649bd0ba4571c8bf13db5c9c54f8ff18ee` / `33bcdd915476faa5c721712961e4c979f5433b8c614eb282800ee94c0ba944e9` |

B01–B04 的来源/调用门沿旧 b20-owners-b01-b06.json `/owners/0..3` 和 `/evidence/SRC_*` 归因，修订IO与四前缀沿 R2 io-ascii；B05 新 getter/提交边界沿 R2 forms，旧正确 handler 审计保持；B04/B06 CN/G 与消息前缀失败沿 R2 phone-coins。源码固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，只核固定来源/范围身份，不虚称本轮全文重读。旧未知 U01–U10、G01–G12、AX01–AX20，以及正常返回/部分失败前提继续保留。

所有新/旧静态案例均未执行；运行观察0、已证 Demo 链0。仅运行本人新写 Git/JSON/hash/text 元数据，不执行参考程序、Ruby、编译器、转换器、反序列化器、生成器、行为向量或旧执行脚本。子审只写 `/tmp` 两个报告，没有修改 repo/正文/原稿/参考/main/旧报告，也没有提交或推送。无剩余输入或工具阻塞；最终普通发布及全部输出独立远端读回由根报告完成。
