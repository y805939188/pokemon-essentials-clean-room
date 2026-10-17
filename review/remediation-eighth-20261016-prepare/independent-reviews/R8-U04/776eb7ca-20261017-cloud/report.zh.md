# R8-U04 独立完整候选复审

候选结论：**PASS**，六项 required 逐项 PASS，候选阻断缺陷0。实际整合输入未提供，本次不登记 actual integrated PASS、ACCEPTED 或 CLOSED。业务执行为 **NOT_EXECUTED**。

本报告只接收固定候选的静态修订。结论来自实际非作者完整阅读、直接源证据和反方检查；independent-review-entry、issue-dispositions 与 tagging-handoff 只用于导航和关联核对，不作为行为结论证据。

## 固定输入与角色

- 仓库：`y805939188/pokemon-essentials-clean-room`。候选提交 `776eb7caf28d2dd5b1f3ffdc1fc8ddaaeea5fe17`，tree `4c1129350a7014fba2380bc18ee7ccbb5163c925`；作者分支 `revise/r8-u04-20261017`。
- 输入基线 `4575e80d041ab0c74a42e2e36399d05791dbaa5b`，tree `e8fb0884694afee309c57504babf9f849a5f1498`。固定参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，只读。
- C35语义core `2460370f1e410bd49cc29e377b89662838aed2b3` 与C36原handoff发布 `802cef65d44772504304016b8ecbe9be558009a0` 分别保留；原合同5caff来源及C35恢复身份未合并。
- 完整实读主审为本次新建非作者context `/root/full_review`；root负责额外独立工具复核、合并审查证据与发布。`/root/crosscheck` 和 `/root/contract_audit` 的辅助范围单列，不替代主审全文阅读，也不另造全局接受票。
- 请求 `gpt-6.1-sol / ultra / default / normal / Fast off`。缺乏权威运行回显，actual model、effort、tier、speed、Fast均为 `UNVERIFIED`。

## 完整覆盖与证据分型

主审完整接收40固定源/规格单位：28参考源/PBS、12固定规格，共1,005,029字节、17,265物理行；并完整接收六候选镜像，共328,560字节、1,999物理行。六份原目标采用最终候选全文与逐行精确LCS映射接合，全部17个被替换原行另行实读，覆盖所有原文内容；其他六份消费者规格和28源单位逐片全文阅读。具体行界、方法、合同及历史资格见 reading-ledger.json 和 primary-review.md。没有把抓取成功、身份相同或作者FULL当作本人实读。

六条完整合同、AGENTS、review-SKILL、最终作者/审者prompt、readset、manifest、accepted-facts/history/policy及适用原提案/反证/根裁决均已接收。继承读集64 root-input＋8 companion逐项路由；精确重复值按typed-purpose去重，其他批body不授新FULL信用，当前U04唯一适用语义无漏读。见 historical-readset-routing.md。

root另外从远端完整回读并重算34候选文件578,400字节、40源/规格、16当前合同输入2,887,833字节、72继承报告载荷8,091,914字节的SHA256/Git blob，全部匹配；候选九个树节点也独立重建核SHA。各分组是不同证据类型，不相加冒充统一行为atom分母。哈希/目录/引用检查仅记TOOL_VALIDATION，源阅读记SOURCE_STATIC，30向量仅记DERIVED_VECTOR；业务仍NOT_EXECUTED。

## 六项裁决

| 必修ID | 范围 | 判定 | 新静态向量 |
| --- | --- | --- | --- |
| GR8-PBSW-002 | PBS051地牢标记 | **PASS** | R8-PBS01 |
| GR8-WORLD-001 | 邻图摆放异常后继 | **PASS** | R8-NP01、R8-NP02、R8-NP03、R8-NP04、R8-NP05 |
| GR8-WORLD-002 | 当前图范围修剪 | **PASS** | R8-RP01、R8-RP02、R8-RP03、R8-RP04、R8-RP05、R8-RP06、R8-RP07、R8-RP08 |
| GR8-WORLD-003 | 跳跃末端登记与消费门 | **PASS** | R8-JT01、R8-JT02、R8-JT03、R8-JT04、R8-JT05、R8-JT06 |
| GR8-WORLD-INT-001 | 117父子绑定 | **PASS** | R8-CE01、R8-CE02、R8-CE03、R8-CE04、R8-CE05 |
| GR8-WORLD-INT-002 | 119缺标签继续 | **PASS** | R8-LB01、R8-LB02、R8-LB03、R8-LB04、R8-LB05 |

### GR8-PBSW-002 — PASS

随附[051]明确Dungeon=true，字段模式和条件消费者可读；编译登记装载、Map051实体/绑定、进入查询与Demo可达是不同证据层。三处最终文字同步。

最强反方为实际Map051资源缺失可使生成不可达；它不使可读PBS标记变未知。候选保留运行/材料未知，未把文本配置升级成已成功生成。

证据：候选 wp11-map-topology-transfer.md L37–37；wp14-random-dungeons.md L48–48；wp14-random-dungeons.md L284–284；engine-overworld-wp11-15-59-60.md L748–753。固定R直接证据 E0087 L255–262；E0035 L31–62；E0080 L4–67；E0080 L1173–1194；E0065 L1063–1107，完整身份见 input-integrity.json。

累计保留：J01三类复合身份、显式0、别名重复；L01/L11材料与无界配置限制；DG25、GR3-DQ种子与失败前缀。仍未证：实际Map051、tileset/area/event绑定；编译/装载/进入与Demo运行未证。

### GR8-WORLD-001 — PASS

已经进入摆放、首次异常传播而正常收尾未到时，明确外层捕获继续后，同实例后继请求受抑制；合法重建与帮助缓存清理不独立复位。新容器仅在其建立及依赖正常时不继承旧实例抑制。

最强反方为外层默认并未吞异常，或重建可能另有变化。候选明确要求捕获继续，保留重建本身可改图/事件及通知；进入前、收尾后失败另判，不称永久软锁或无条件恢复。

证据：候选 wp11-map-topology-transfer.md L110–115；engine-overworld-wp11-15-59-60.md L755–766。固定R直接证据 E0019 L7–27；E0019 L114–140；E0018 L322–341；E0031 L11–23；E0010 L76–104；E0015 L42–65，完整身份见 input-integrity.json。

累计保留：首有效连接、正常实例复用、六格范围；通知首次异常传播；成功地图加入/偏移前缀与失败地图加入前边界；同实例读档重建既有入口条件。仍未证：宿主画面与保存恢复未运行。

### GR8-WORLD-002 — PASS

有连接分支最终过滤包含当前图；显式speed0、20×20两图与512×384、单轮100格得到12800/10240，均≥3328而空表，global仍旧A。26格为3328/768，删A留B。修剪正常返回与后继取图报错分开。

最强反方为默认speed4含微更新、moving/snap/无连接/第二轮可能改终态。候选逐项保留，snap夹具A钳512；保存须先于任何取图或额外生命周期分叉且其余依赖正常。读档/继续预览先取图的失败先于恢复UI，不承诺真实回放或永久空表。

证据：候选 wp11-map-topology-transfer.md L99–108；wp11-map-topology-transfer.md L143–144；engine-overworld-wp11-15-59-60.md L21–21；engine-overworld-wp11-15-59-60.md L768–782。固定R直接证据 E0019 L30–39；E0019 L361–375；E0019 L475–493；E0018 L497–518；E0008 L63–67；E0010 L76–104；E0072 L310–313，完整身份见 input-integrity.json。

累计保留：小偏移、moving、snap、无连接单项/多项；global与容器引用分立；第二轮可能新建A与旧global实例差异；WP09类型保存与装载顺序、UI65继续预读、WP16相机；MP13原位必修外其余537旧向量不改。仍未证：真实保存/序列化/读回与UI时机NOT_EXECUTED。

### GR8-WORLD-003 — PASS

普通移动/碰撞计时与跳跃计时独立。合法活动零跳且无普通移动计时时，合格普通更新中ACTION/SPECIAL可分别登记并消费；新登记门与已有请求消费门分层，消息公共早退和微更新边界保留。

最强反方为角色新命令另读跳跃门，或解释器/冰滑/上下瀑会阻登记。候选没有把这些门合并；已有debug在消费条件满足时仍可消费。后继异常仅保请求清除/菜单中等已达前缀，不保证完整UI或跳跃清除/暂停/恢复。

证据：候选 wp12-terrain-movement-vehicles.md L174–185；wp13-map-events-npc-followers.md L131–131；engine-overworld-wp11-15-59-60.md L784–796。固定R直接证据 E0011 L165–229；E0011 L103–119；E0020 L348–354；E0020 L767–787；E0020 L893–991；E0022 L416–458，完整身份见 input-integrity.json。

累计保留：USE→ACTION→SPECIAL→F9首检测链及菜单→调试→快捷→互动消费优先；F9按住与moving可登记；消息早退、微更新无末端、路线WAIT；MV68–77、R5-JP、R7-BP、GR3-CS11–13。仍未证：键盘/声音/菜单呈现与宿主后继NOT_EXECUTED。

### GR8-WORLD-INT-001 — PASS

117携父当时事件编号，子绑定建立时当前图，父保原绑定。连接A/7父、当前B得子[B,7]=child、父[A,7]=parent；同图后写覆盖；失联更新仅先清编号0，子[B,0]与父[A,0]分立。

最强反方为普通角色查询/111/123/主结束解锁使用当前图，且失联会清编号。候选分别说明这些消费者与私有键，并给同图/连接/失联控制；缺记录不建子且继续，深度101仍提示退出，异常只保已完成写入。

证据：候选 wp13-map-events-npc-followers.md L94–99；wp13-interpreter-command-matrix.md L40–40；engine-overworld-wp11-15-59-60.md L798–809。固定R直接证据 E0013 L514–521；E0012 L27–52；E0012 L84–135；E0012 L323–382；E0021 L274–291；E0008 L76–81，完整身份见 input-integrity.json。

累计保留：R5-ID及普通角色/自开关/解锁各自当前图规则；独立event0公共事件助手入口与返回差异；深度>100非普通false；全局元数据保存资格不冒实体保存回放。仍未证：默认Demo与实体存档往返NOT_EXECUTED。

### GR8-WORLD-INT-002 — PASS

直接119从列表头找首同名118且不搜最后保留项；缺目标时不改当前位置、返回继续，外层到物理下一项。有限对照命中A OFF/B ON，缺目标A/B ON。

最强反方为最后入口先结束或101预读只向前。候选把已分派119、末尾入口、101辅助和有限回跳分开；损坏结构/后继异常只保已达前缀，不推任意安全恢复、无界终止或未来作者校验政策。

证据：候选 wp13-interpreter-command-matrix.md L42–42；wp13-interpreter-command-matrix.md L144–153；wp13-map-events-npc-followers.md L149–150；wp13-map-events-npc-followers.md L218–218；engine-overworld-wp11-15-59-60.md L811–822。固定R直接证据 E0013 L533–547；E0013 L11–19；E0012 L84–136；E0013 L552–562；E0012 L205–267，完整身份见 input-integrity.json。

累计保留：96命令逐ID及28/2/66分类；IM13–15/16–25/36–41、R6-EV；首同名、有限向后、末尾先结束；已成功A写入不因后继B失败回滚。仍未证：真实宿主/媒体表现NOT_EXECUTED。

## 累计保留、引用与写集

目录由742行/538向量变为822行/568向量，新增恰30（PBS1、NP5、RP8、JT6、CE5、LB5），无丢失/重号。旧742行前缀仅L21 MP13作必需的当前图过滤修正；其余537条旧向量原文完全不变。96命令ID及每条分类保持28空操作、2标记、66有实现；仅117 L40与119 L42正文变化，101预读、分支/循环与旧IM/R6-EV控制保持。

35处证据引用的编号、identity_ref、path、commit和范围全部一致；30新ID、16打标贡献、12显式锚点及行号准确。新增119跨镜像锚点可达，13个镜像外Markdown目标在基线存在。完整数据见 preservation-and-protection.json；辅助独立复核见 auxiliary-crosscheck.md。

六候选全文中的MP/MV/EV/FW/IM/MR/DG/RS/WT/FS、B04、GR3、GR4、R5/R6/R7及地牢参数补充均纳入累计保留接收，没有将旧关闭范围扩大，也未抹去原NOT_EXECUTED资格。

候选相对基线仅新增本批candidate目录34文件（两提交）；正式规格tree仍为 `f292698cdd4a8e725525a9be6dc34b75faaf151e`，deliverables、planning、audit等保护树均与基线相同。所有本次新增写入仅限本报告独占目录，作者候选、正式规格、main、原报告和历史接受/关闭回执均未改。本批optional分配为空，没有越权采纳或新增全局拒选。规格保持实现无关，未复制/转译源结构，未开发框架。

## 未决依赖和执行限制

本候选不存在语义前置批次或未决候选缺陷。剩余门为：R8-INTEGRATOR唯一正式整合；接收WP05通知、WP09保存/元数据/恢复、WP16相机/渲染、UI65继续预览及菜单/快捷/debug、WP11/13/14与世界公共目录的共享贡献；对真实整合结果重新冻结并全文复审累计保留；随后分别登记actual integrated PASS、ACCEPTED、CLOSED。候选PASS不能替代这些门。

实际Map051资源/绑定、编译装载、Demo可达、真实保存往返、宿主键/画面/声音仍未证；它们不阻止这六项有限静态修订。本审没有运行Ruby、游戏、编译、行为模型、宿主UI或作者会改写candidate证据的validate.py。

所选执行环境在container_creation阶段失败；远端固定SHA/blob读取与functions V8文档校验完成审查，未使用本地shell。发布通过GitHub Git Data API新建独立分支、普通提交及非force快进更新完成；不声称执行过shell git push。

继承输入观察：原冻结U04作者prompt尾部启动样例仍指U06，是基线模板问题；本审使用明确U04委托和六条合同，没有执行该样例，不作为本候选缺陷。

## 输出绑定

独立分支 `review/r8-u04-776eb7ca-20261017-independent`；只写 `review/remediation-eighth-20261016-prepare/independent-reviews/R8-U04/776eb7ca-20261017-cloud/`。内容提交、发布操作和完整远端字节回读绑定见后继publication回执；本报告不填自身未来hash。最终输出commit/tree由外部最终交付绑定，业务执行与四门状态不因发布变化。
