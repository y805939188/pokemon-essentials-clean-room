# 给原提取会话：WP61 revision-v3，仅四项剩余修订

工作目录 `/Users/dingshinn/Desktop/pokemon-framework-reference`。先读 `review/wp61-review-2026-10-02/recheck-v2/report.md`、`findings.json`、`registration-checks.json`、`review-source-verification.json`。本轮结论 **REQUEST_CHANGES：7项CLOSED、4项PARTIAL（R02/R03/R06/R08）**，无新增ID。只修这四项及其直接交叉引用；完成停止送有限复审，**不要进入WP72**。

## 固定前态与保护

- 主稿 `specs/pokemon-rules/wp61-field-passive-effects-and-blackout.md`：SHA256 `d68f2ae6929bafecee81c3dade3a99ba9e8df7ea3ac03e92271eff3facff9aa7`，63,559字节。
- v2附表 `review/wp61-delivery-2026-10-02/revision-v2/entry-coverage-table.md`：SHA256 `a42b706385aae7557c0c81807316a1d6d8a0ec5048a329412b30516bb91fbdc0`，15,278字节。
- 唯一差分前态是本次 `review/wp61-review-2026-10-02/recheck-v2/input-snapshot/` 内对应两份文件，不再使用首审v1前态。
- 当前manifest/TSV/matrix的完整身份见本轮 `registration-checks.json`；修订前manifest§1为1,229条完整身份＋2旧无哈希行，TSV v82为1,134条。最终数量按实际登记新增项计算。
- reference固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，Git清洁。继承33依赖、15批准、全部已登记来源并从磁盘复测。全部v1/v2交付、首审和本次复审原件/快照保持不变。

## 最小改动清单

- **WP61-R02**（主稿55、57；v2附表14、25；source-identities的Event_Handlers阅读声明）：将队伍成员计数门与净化室对象存在门分列，可拆行或同格明确两个独立分支。队伍门用非零，实际量表变化仍引用WP23；净化室在成员循环结束后按对象是否存在调用，自身组级效果门仍引用WP23。补队伍无Shadow但净化室存在的对照。若保留电话新增取值细节，随机重置为20至39整分钟（40不含），也可删除该非本包主责的数值细节，仅保留次序和门。source-identities中Event_Handlers仍标未重读，与回应24/checks固定输入所称重读66–90不一致，按实际读取同步范围。
- **WP61-R03**（主稿193；v2回应94和checks的semantic_residuals_checked）：只需将§10对应条目同步为§5.2的有界合同或明确引用；保留没有显式循环中止，不再保证后续伤害。同步新回应/自检的残留核对声明。已通过的M06/M08和附表内容保持。
- **WP61-R06**（主稿38、139、195；v2回应94和checks的semantic_residuals_checked）：原位同步38/139/195，统一为到达普通末尾才清点，缺失家图和捕虫分流不经此步骤；无家不是提前返回。其余消息/统计/治疗/转移状态引用已正确§7.2即可。不得只在尾注新增更正而保留现行相反条款。同步新自检。
- **WP61-R08**（主稿38；v2回应67、94和checks的semantic_residuals_checked）：将§2相应概念说明同步为公开入口及已有事件识别证据，并保留实际事件编排U01；已有正确细节不重写。同步新回应及残留核对。泛指编译阶段或历史说明本身不作为新问题，关键是删除当前正面的构造能力断言。

R01/R04/R05/R07/R09/R10/R11已经CLOSED，不重提取、不重写其数学或场景。R11正文§6.3可顺带换成三动作概括或只引用§8.2，不需要新增独立测试/问题。R02表行拆分与否自行选择，数据行数按最终内容实测，不能继续写43作为固定值。为净化室独立更新补静态对照即可，不重开WP23。

## 交付与登记

1. 在 `review/wp61-delivery-2026-10-02/revision-v3/` 新建四项逐条回应、checks、摘要、新版附表、来源身份、两份完整统一差分与diff-bindings；v1/v2材料不覆盖。主稿原位修改剩余错误，不能只加尾注而保留相反现行条款。
2. 主稿diff从本次冻结v2主稿到修改后主稿；附表diff从本次冻结v2附表到新建v3附表。显式绑定before/after路径、完整SHA256、字节和hunk数，逐hunk可机械重建after。不得省略未改上下文或拿旧v1当基线。
3. 保持M01–M31身份与已通过场景；新增场景编号唯一。如仅在M24扩展净化室对照，标清此处修改；不要为消除旧表述大量新增重复段落。
4. 来源读取范围按实际记录：R02的队伍/净化室循环位置、原始量表非零门、电话整数区间；Event_Handlers实际阅读状态须与回应/checks一致。新读文件登记实测完整身份；不能把身份核验当成实际阅读。
5. 主稿、v3附表、新回应和摘要全文检查。对旧毒伤保证、无条件逃脱清理、构造能力断言给出实际命中位置及处理结果；区分肯定、否定和历史材料。不要笼统填写“全部已清空”而漏掉§2/§10。不复写已删除的源码调用，R10保持关闭。
6. Feature Matrix仅更新F14-05修订待审注记，不自行Reviewed。TSV与manifest§1按磁盘实测改主稿及新增交付；manifest轮次/标题与§2.2/§3/§4只追加本轮叙述，旧记录不改写。
7. 全量复核短标签、完整哈希、字节、重复路径、历史插入、旧材料保护；末检单独保存、注明阶段、不自指哈希。复核脚本/末检不登记延用既有约定。

静态规格工作范围不变：不运行参考代码/模型/游戏/战斗/UI/编译器/反序列化，不改reference，不实现框架，不操作真实存档；不创建任务/Agent，不自动发送消息，不提交推送。完成后报告实际身份、四项回应和登记结果，停止复审；不自行关闭四项或推进WP72/整体double review。此前WP53、WP37、WP67-A/B、WP65、GR与WP23-N01等结论保持。
