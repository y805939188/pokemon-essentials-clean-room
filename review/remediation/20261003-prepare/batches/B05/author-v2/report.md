# B05 author-v2 候选交接

RUN_ID：`20261003-prepare`；作者：`A-B05`；阶段：`B05-A`。父统筹已明确批准五份原稿最小同步，本后继候选已完成同步，并保留原十份净化稿和旧 `author/` 全部原字节。十个主责、十六项贡献的原／净化／附表／静态目录关系及 A-REG 建议已更新；本批原稿写范围待批项为 0。候选尚待**全新独立 Ultra**及实际 integration 受影响范围 Ultra，所有规范 ID 继续 OPEN。

## 冻结链与范围

- 固定上游：`0a12de641542f9a59909d2a950c1de8df17ca09d`。B01 被审整合 `93d0714ddfdb4900e946c0acd1cc80cf6431f0a0`、Ultra 报告 `8a1fdfb2b582df4cefb408b56eea144a2e53dcfe` 及后继交接的正式正文无变化结论继续保留。B01 只接受 WP03/KR13 依赖，WP19 全表由 B05 交付，WP28 消费贡献仍归 B07。
- 本候选直接父 SHA：`7dc7dd5dfc986788fd6d9ce7b2bdaa6208837b4e`；父 tree：`f0e82350ce11fdf22e015b4eb9c90a0199fec13e`。同一分支 `remediation/20261003-prepare/batch-B05` 追加普通提交，不改写旧候选。
- 后继写范围：批准规划原十个正式文件加父统筹授权的五份原稿；相对旧候选实际只修改五原稿，并新增本批 `scope-amendment/`、`author-v2/` 记录。批准依据与精确条款见 [scope-amendment/approval.md](../scope-amendment/approval.md)、[approval.json](../scope-amendment/approval.json)。规划、历史批准／review、旧作者记录、公共索引／Feature Matrix／coverage／trace／公共哈希和登记状态均未改。
- 固定参考保持主 Git 外、只读：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`；SHA/tree/clean 和原 26 个读取文件的哈希重新核对。没有参考游戏／Ruby／编译／转换／生成／反序列化／模拟器／求解器执行，没有修改 ignore、主仓库跟踪参考或推参考上游。

本候选 SHA/tree 在提交后的远端核验与最终交接提供；本报告不声称文件能够自引用其所属提交 SHA。旧完整 finding、current_qualifications、有效二审／扩展裁决、批准 acceptance 及阅读凭据均通过旧作者 Git blob／哈希冻结继承，详见 [input-freeze.json](input-freeze.json)。

## 五份原稿最小同步

| 原稿路径 | 条款与结果 | Finding（GIR-FD82 前缀） |
| --- | --- | --- |
| `specs/creature-rpg/wp18-creature-identity-species-ownership.md` | §3.2 完整默认值；§4.2 基础初始化与创建形态抽样，保留已有 Nature 缓存限定；§9 区分动态读取同值与显式提交 | A021、A022 |
| `specs/creature-rpg/wp20-hp-status-moves-helditem.md` | §5.1–5.3、§7.5、§9：入口容量／五项与零项、负索引、首招重学开关、背包 TR 与队伍入口及零招式调用边界 | A023、A024、A025、A044、C126 的本批贡献 |
| `specs/pokemon-rules/wp19-attributes-ability-and-stats.md` | 仅 §3.5：完整 25 Nature 序号／身份／升降表及具名取整数值；覆盖、缓存、rawIV、EV 和其它条款保留 | A020 的本批贡献 |
| `specs/pokemon-rules/wp21-dynamic-forms-and-display.md` | §3 C/D、§4.1–4.2：六族具名招式、数据门、ROTOM 删除、PP、次序、拒绝与部分失败 | A026、A027 的本批贡献 |
| `specs/pokemon-rules/wp23-shadow-hyper-and-purification.md` | 仅 W06：HARDY/M4000/G2500/H4/h80/JOY×1 → G2410/H4/h80；LONELY → G2370/H3/h80 | A031 |

已发布 v1 建议把 WP18 同值原句的段号写为 §9，但原句位于 §8。本轮将补丁收窄到实际获准条款：**§8 原字节保留**，在 §9 明确该句仅指动态读取，并列出显式／创建复检同值提交的差异。WP18 §4.2 同时保留原有普通创建限定、`hasNature?` 判定和精确 WP19 引用。实际同步补丁见 [original-delta.patch](original-delta.patch)，不把旧建议附件改写为执行记录。

正确的原 Mega `BANETTITE`、原 h=255 且 G=0 门以及原 GROWLITHE/SNORUNT Shadow 表均保留。原 WP19 的其它数值、原 WP21 的非批准条款、原 WP23 的其它场景也保持父提交字节。未写 WP28/WP30/WP66A/WP76 的跨批正文。

## 自检与逐 ID 后继建议

- [static-validation.json](static-validation.json)：**121 项**静态文本／身份／固定算术检查通过。沿用旧候选完整 Nature、Mega、可选 Shadow、目录与反向对照检查，并新增五原稿按批准条款屏蔽后其它字节一致、原 Nature 表与固定参考一致、原／净化形态映射一致、同值范围收窄、正确原表与旧候选不回归。复现：[verify-static.py](verify-static.py)。
- [evidence-integrity.json](evidence-integrity.json)：**195 项**证据完整性检查通过；包括旧作者 21 个文件不可变、十五份父输入／输出、原 finding／acceptance 完整摘要、有效限定／责任／目录行继承、批准规划与固定参考哈希、原稿范围及模型披露。
- 相对旧候选：五原稿 **98 行新增、18 行删除**。相对固定上游：十五个正式文件 **280 行新增、59 行删除**；完整冻结 diff 见 [formal-diff.patch](formal-diff.patch)，输出哈希与候选路径见 [candidate-manifest.json](candidate-manifest.json)。正文和非补丁记录的 whitespace 检查通过；两个原生 diff 保留空行上下文标记，单独核对精确字节与逆向适用性。
- 旧候选 38 条新增静态目录行及 FM15/FM20/SH06 前提修订保持；v2 未增加目录行。WP24–26 的 PT/PS/AQ、WP34 的 BR（包括文件尾字节）保持原样；整文件冲突仍由统筹串行整合／重冻结／按影响复审。扩围后与 B02 的写集合及双向读写交集均为空，未引入互相前提；本容器外 B02 运行状态未独立核验。
- [finding-dispositions.json](finding-dispositions.json) 更新全部十六个原 ID 的原稿条款、净化条款、附表、测试和静态前后／邻近反例。十个主责仍为 A021–A025、A027–A031；每项有效二审／扩展裁决、原限定和跨批责任完整继承。
- [registrar-proposals.json](registrar-proposals.json) 仅为 A-REG 后继建议，未应用公共登记。只有全新候选 Ultra 和实际 integration 受影响 Ultra 均通过后，才可登记本批有效贡献；B07 的 WP28/WP30、B16 的 WP66A、B17 的 WP76 仍须完成各自贡献，跨域规范 ID 由最终 Ultra 后再交 A-REG 关闭。本作者未自行整合、登记或 CLOSED。

**运行观察 0；demo 链 0；行为静态向量未执行。** 文本比较、哈希及独立固定算术不充当运行验证；U01–U10、G01–G12、AX01–AX20、可选启用与宿主／媒体／插件／运行组合未知继续保留。

模型请求继续为 `gpt-6.1-sol / Max / Standard(default)`；实际 model／reasoning／tier 未独立核验，按用户方案 A 保留 UNVERIFIED 披露。未请求降档／加速，未使用 xhigh fallback，未派生任务。详见 [model-request-receipt.json](model-request-receipt.json)。普通推送本批分支并核远端后停止，等待全新独立 R-B05 Ultra。
