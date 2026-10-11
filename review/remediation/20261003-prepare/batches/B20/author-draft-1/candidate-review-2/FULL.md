# B20 独立FULL19/15后继候选再审入口

固定审查对象是NEW2 `3f521e6dea0b442e4bb174a9715c458416386b37` / tree `49f406a6de8ca2786e5dda27abada19780fdfa05`，不是后继移动分支tip。基线C `de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f`；先前审查NEW `1abaefb1db5818ff9404392143c476979d34c21a`；repair_BASE `272885cca76c36cd04dde27b6be2c654759ec4c2`。作者应用凭据、许可、哈希和数量仅是导航，不构成质量PASS。所有案例NOT_EXECUTED，运行观察、Demo证明均0。

完整差异采用一次存储的固定链：旧C→OLD_NEW流保持原固定身份；OLD_NEW→BASE的三次证据发布提交只引用；本轮BASE→NEW2完整无过滤流固定D `a9323ee064a4931fa8c218cfe24a060acc4c2e86`，path `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-2/stream/BASE-to-NEW2.full.diff`，blob `355aca2a456562a5e0799cf36957262ff84c88d9`，SHA-256 `0096cacd3fefe3dcb85857300114224b6195deb3f536c22952c75a75845abc1c`，451455 bytes/33路径。无路径筛选、无外部diff/textconv、无忽略空白、binary/full-index/no-renames。独立仓库重建本轮流已逐字节一致。审查者可直接在内存比较完整C和NEW2对象，勿再存/复制旧流或递归大包。

完整19/15的原qualified root/extension、有效case、最低修订、反例、确定再检、其它owner和最终全局义务保持，入口为[full19作者图](https://github.com/y805939188/pokemon-essentials-clean-room/blob/3f521e6dea0b442e4bb174a9715c458416386b37/review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-fix-1/completion/full19-author-map.json)及[全部5组修复导航](repair-navigation.json)。51个子例只用于本轮5组修复，不替代其余14项完整合同。旧195ID次序/重数、193原C旧行及两处已assigned修订、B19/PA040、两份WP74与68旧作者输出保留；原稿仅精确许可2文件3hunk写入。

本门须独立给NEW2完整19贡献/15主责结论。复查聚焦两份原独立报告的5组去重缺口及相关契约，并确认其余14项和不变证据保全；旧16项scoped静态结论或作者完成标记不自动成为NEW2 PASS。不重签既往actual或B01–B19整个包。

1. **C024**：WP75§3.3/§12.1、原稿§12.1、B20-C024及12静态子例一致。9/10/11两方向门保留；正常顺序数量门→建/清树→逐节目录/脚本→备份→loader；编号仅是布局。清树成功、首脚本打开失败时已有备份B0不变/无备份仍无、原归档不变，无loader；其余阶段已发生写入及未到阶段逐项有界，不保证回滚。
2. **WP80-INTAKE-R01**：WP75概念中的四个正向前缀均U+003A；item/hiddenitem与Battle/Type收集/解析前缀大小写不敏感，登记身份与其它门独立。只换U+FF1A的道具/训练家门对照准确；原CV-M07历史字节保留，由当前B20对照明确活跃前缀门。Move/OppMove空白、Common精确拼接、Trainer/SellItem/s:其它准确边界保持；10子例不是单一示例修正。
3. **C029（合并FULL-F03/AF-01）**：普通form强制值存在含0优先，其次战斗/仓庫返回存储值，两状态均假才调用GIRATINA动态处理器。宝珠/旗标0/1仅在处理器调用门内；form_simple不动态。WP21§6第2条及WP18链接有效，原稿局部handler审计句保持；12子例覆盖正常、forced0、战斗和仓库分别短路、其它物种与简单读取。地图进入/实际变形未证。
4. **C028**：两份WP77§5.4、目录和14子例区分无训练家资料空文字、请求遭遇版缺时回退0、双版缺、三表空；队伍空/非法参数/非法物种不承诺同等保护。训练家版本max与全局遭遇版本独立，联系人地图、每次TP/TE一次且所有段复用、队伍成员次数、Land→Cave→Water及合法首最多4槽均匀、不加权不去重均保留；开始消息与失败阶段顺序有界，WP63/旧PL16/PL17只读。
5. **C003**：只改新B20-C003及后继3子例中的CN代币窗/玩家coins，G金钱窗独立读money；旧CV-M14正确字节及.midi不复制/.mid先复制、CommonEvent真实可达块、b/pg、ASCII与标题实体全部保留。

逐条原finding及最低验收以repair-navigation.json的固定报告whole对象/JSON pointer为准，不能把本页概述缩成合同。5组修复的原稿after与许可一致只说明scope合规，质量仍由本门独立判断。输出须绑定准确NEW2/tree、独立源/正文/反向静态核验及残余P2；不签actual、正式接受、G/ACT/C或canonical关闭。父任务协调另一路affected与后续唯一登记流程。
