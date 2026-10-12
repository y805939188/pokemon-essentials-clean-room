# R4-U03 精确 actual 独立复审

**ACTUAL_PASS_SCOPED：七项 finding、30条原验收标准均通过；本批无必修问题。** 判定绑定实际整合 `5dd6789b22e03b85bb81ae73b9c65a1fab585186` / tree `e563ea5f34ba8e0315eee46934deb566ed98a924`，任务发布 `d305ba47f31ecfde747b763682e87f32abe54888` / tree `4d7c193d4cbe4cb707edce30d2ce4cb56d6102ee`。只判断U03修订与现有消费者交界，不登记接受或关闭。

| finding | 实际裁决 | 原标准 | 当前检查要点 |
| --- | --- | --- | --- |
| GR4-M04-001 动态形态取图 | ACTUAL_PASS_SCOPED | 5/5 | 个体先求形态再取图；严格五日界、强制/战斗/仓库、缺图先提交；WP06与孵化分层 |
| GR4-M06-001 遗传向量 | ACTUAL_PASS_SCOPED | 4/4 | 双不同Power总3；gen≥6 Knot+至多一Power总5；gen5总3；同属性一次，单持物 |
| GR4-M10-001 同轮输入 | ACTUAL_PASS_SCOPED | 5/5 | 命令/逐位数字/数量/命名分别排序；WP13返回后映射，事件取消默认初值1，PC负取消 |
| GR4-M10-002 皮肤回退 | ACTUAL_PASS_SCOPED | 3/3 | 冷链首命中/全缺；显式Missing暖读空与冷Custom分开；空w单窗清理 |
| GR4-M10-003 长词排版 | ACTUAL_PASS_SCOPED | 4/4 | 不硬拆/+2严格大于/已有内容门；WP08先返回文本，pg与消息暂停/摘要268分层 |
| GR4-M10-004 动画默认表 | ACTUAL_PASS_SCOPED | 3/3 | 18×6身份表；命名编译与默认查找、8→5→2回退；精确hit偏移/默认无偏移/OppMove/媒体分层 |
| GR4-M11-001 图鉴普通外观 | ACTUAL_PASS_SCOPED | 6/6 | 普通图请求false而保末次true；合法多项RATTATA双male已见/首轮false；不匹配与单项反向保持 |

完整原 finding/验收及每条实际依据见 [findings.json](findings.json)、[criteria-results.json](criteria-results.json)，当前源码/规格范围与有限复用指针见 [read-ledger.json](read-ledger.json)。原候选v1 M11第6条REQUIRES_CHANGES历史原字节保留；候选v2 `d7875398e130b5bfa621c55d6c016ee0f8965cf7` 与独立报告 `4c89f30285f55f017b021f5d6b5a538a02c4bc41` 的收窄前提在actual两处精确落地。没有把候选PASS自动转成actual。

131正式文件全部以完整bytes比较：12 U03＝v2（552,465 bytes），12已接受U01/U02保持（424,200 bytes），107＝B（2,800,559 bytes）。parent→actual 66路径精确分为12正式、51冻结证据、3registration；task后继正式不变。51证据是19作者、19 v1、13 v2，逐个与原提交完整字节相等。13当前消费者身份匹配且相关内容已亲读；身份检查不是整文件语义签名。详见 [identity.json](identity.json) 及 [身份子审](subreviews/identity-integration.json)。

当前整合的有效有限核对包括：WP06墙钟输入与游戏变量清槽/个体time_form_set分开；正确遗传/孵化与A053原限定保持；WP13隐藏选择的原始cancel1须经映射到C，数字103及101合入消费者默认取消初值1；WP65正常显式预览不承诺冷链回退；WP08参数替换先返回A B再按给定宽22/21一/两行，反斜线1先被本地化删除时不再造暂停；WP74尾随空白身份落空与零合法项保旧映射正确消费新默认表。

U02世界→新UI交界另给本次限定判断：地图微更新有Scene_Map/非淡出条件，且与normal update入口不同；消息或皮肤/排版变化没有独立清冲浪临时字段。无合格通知时基点可保留；有合格玩家步通知可清，ending_surf真才额外收尾。人工ending_surf真先阻止解释器到达正常命令，不能扩作事件可达夹具。消息窗与低电量警告仍按各自门，不声称每次微更新必触发帧通知。详见 [世界/UI子审](subreviews/world-audit.json)。U02原WP59六项握手只保旧实际消费者签名。

四项公共提案独立核对均无需额外正式编辑：audit旧索引保持冻结时点身份，新来源见本报告；WP65预览与PC/WP13引用没有行为冲突；WP74现有播放引用已解析到108默认表，可选锚点不构成必修。判断依据与反向完整前提在 [validation-result.json](validation-result.json) 和各子审。

新增参考/行为模型/宿主或Demo执行全部 **0 / NOT_EXECUTED_THIS_UPDATE**；历史第四review4次（M01×1、M02×2、M12×1）独立保留、未重跑，不计本次运行通过。46静态设计及旧108格/84默认PBS身份/18目标资格只作精确限定证据复用；原GR3/229/341资格不扩签。Runtime类标准通过指证据边界合规，媒体、字体、物理输入、像素、播放、地图/真实Demo、宿主、插件仍未证；未代选未来兼容政策。

U04实际PP/物品资格与确认数量、U05编辑/PBS/runtime快照、U06最终依赖门保持。U03本范围无阻断；唯一登记员可据本报告另行办理接受。本reviewer只写 `review/remediation-fourth-20261012-prepare/batches/R4-U03/review/actual-v1/`，不改正式/作者/参考/真实数据/公共台账/main，不登记ACCEPTED_SCOPED/CLOSED，不合并、清理或删除。

请求gpt-6.1-sol / ultra / default / Fast=false、普通速度；实际配置回显 **UNVERIFIED**。根任务 `/root`，真实thread `01a130de-2480-707d-a4fe-c7056c71c02e`；子审真实thread在各JSON。独立分支 `review/r4-u03-independent-actual-20261012` 普通推送；[后继publication.json](publication.json)绑定冻结报告commit/tree与新远端对象库完整字节读回，最终后继commit/tree由返回值提供，避免自引用。
