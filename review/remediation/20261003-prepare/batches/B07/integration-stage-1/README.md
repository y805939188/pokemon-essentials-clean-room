# B07-G实际整合，等待两份分别Ultra复审

当前管理前驱 `259a1c158f317c5e32830e04838a76aa82f4d20a`；B07正式内容基线 `219cc3c182750155e9dbf2cb619f420b3922de27`；完整候选 `a22df6b1d9465b68e45558c57bc69c61939baeaf`。R-B07 `19e2d5f9de40a9220059a62f785ac0bbc13b2154` 为19贡献／12主责候选 PASS_SCOPED，独立受影响 R-B04 `3e88d42b8d9313e1adbbc8944e54faa1b45e71a0` 仅反向接口候选 PASS_SCOPED。14正式文件＝8净化正文／目录＋6精确原稿同步，原字节整合；实际新SHA的两份分别 Ultra 复审均待办，随后父任务C接受。规范必修229 OPEN／0 CLOSED，B07尚未接受。

[manifest](integration-manifest.json)、[逐ID控制及候选定位](finding-registration.json)、[授权／历史顺序限制](scope-and-authorization-registration.json)、[普通合并／依赖影响](merge-and-dependency-impact.json)、[B08精确合同与有界并行探查](downstream-handshake.json)、[计数](scope-counts.json)、[文档核验](validation-results.json)、[R-B07候选报告](../review-round-1/report.md)、[独立受影响R-B04候选报告](../affected-B04-review-round-1/report.md)。来源57＝14正式＋11作者＋32两份报告，全部候选／报告字节保留。

两实际复审须各自绑定同一最终冻结actual SHA，完整管理前驱→actual及候选→actual无过滤差分；R-B07查完整19／12，独立R-B04查受影响WP15–17反向接口及35／23历史范围。双PASS后才父任务C接受／以精确接受后继重冻结B08；B08当前未解锁、未派发。

六批B01–B06已接受口径保持：114已接受贡献记录／105触及ID，75主责，具体原修订74满足／1缺具体消费／0证据不足，严格全贡献71／4。A024的B07消费者虽候选PASS，尚不升级接受统计；A017/B21、A034/B08、WP80-B02-R02/B21继续待办。当前公共133记录＝114原接受＋19候选，与28新增静态设计分母不同。

六份原稿路径、完整hunks及before/after/patch哈希可核验；作者“先备差异再写入”仅自述，最终Git树不能追认该历史顺序，不补造前置证据。原稿旧批准按旧字节保留，正确既有条款不反改。

28未执行静态行，8旧行前提修订；目录169→191、125→131。BG/DC与RM/CP整节、BE13及其他旧行的字节／次数／顺序保持。B16的A048空重学UI、C003 A23/A31/A33前提、D023 BP显示同步及B09的B013伙伴接收／还原与CP20责任继续待办；既有B04专业业务条款未因此获新批准。U01–U10/G01–G12/AX01–AX20、动态调用／插件／宿主／媒体字体／容量／真实Demo等具名未知保留。

B08为79计划读／8计划写／17贡献／9主责，前置B03/B05/B07；B07改变其3个计划读者（WP28、WP30、creature-rpg-wp27目录）。B08未来写入反向影响B07的5个计划读者，必须检查接口、受影响复审与整文件目录锁；WP34正文只读。安全并行探查仅为固定输入的有界只读候选，未判定写入独立性、未派发或并行写入。 合同为准备材料，不启动任务；矩阵只读固定元数据不足以宣称语义独立，未知依赖不得并行写。B08 WP34正文只读，原稿授权不继承B07。

请求gpt-6.1-sol/xhigh/Standard，分别复审要求Ultra/Standard，实际配置UNVERIFIED；保留259a显式xhigh更正及其来源，历史Max收据按时点保留，Plan A已接受，无新增配置认证门。参考／作者／审者程序不执行，行为向量、运行观察、真实Demo链0。最终actual以普通push及回读外部交付；末提交仅两完整patch及diff-and-freeze.json。
