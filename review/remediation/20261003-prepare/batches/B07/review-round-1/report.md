# 独立 R-B07 候选复审 — RUN_ID20261003-prepare

**PASS_SCOPED**。完整候选的 B07 本批19项贡献（12主责）通过限定范围静态复审，没有本批要求返工项。这个结论只验收下列精确候选的本批贡献，未批准全局、未关闭任何原ID、未批准实际整合，也未代替单独 R-B04。

| 对象 | 固定身份 |
| --- | --- |
| 候选 | `a22df6b1d9465b68e45558c57bc69c61939baeaf` |
| 单父版本 | `219cc3c182750155e9dbf2cb619f420b3922de27` |
| 候选 tree | `336fc0f3693d20b733d40f60d42d3bbe6323e52f` |
| 被审分支 | `remediation/20261003-prepare/batch-B07`；裁决绑定SHA，不绑定浮动分支 |
| 报告分支 | `remediation/20261003-prepare/review-B07-1`；报告完整commit由提交后交付收据给出 |
| 完整原finding终裁 | `93e10babe0b9c9ef8b3f5277754541b447beeeb4` 的 `review/global-independent-review/2026-10-03-fd82a639/findings.json` |
| 固定计划/验收 | `41fffb540c6483f5296ea0d33b789b75180d27ed` 的 `review/remediation-20261003-prepare/batches/B07.md`、`finding-acceptance.json` |
| 合同 | 父版本 `review/remediation/20261003-prepare/batches/B04/acceptance-stage-1/downstream-handshake.json` |
| 独立参考 | `https://github.com/Maruno17/pokemon-essentials`，精确commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0` |

## 独立证据顺序与边界

先读 AGENTS.md、项目有效规范、固定原终裁的完整19对象、计划验收和父版本合同，再独立准备、核验并只读精确参考。先读参考、caller/consumer、配置/数据及候选完整未过滤差异，建立正向/反向静态对照并写 [independent-first-lock.md](independent-first-lock.md)，之后才读作者报告、自检、验收索引、授权/同步计划、依赖/追溯和复审请求。锁定文件SHA256为 `7862ddc6c2c1cc299e83a8821ce134824c6f72657d443397b449cf0f693091c2`。没有读取或采纳并行 R-B04 的新结论，没有派生子任务。

作者索引不替代完整控制对象。独立比对确认19完整原对象与19计划验收对象的规范化JSON SHA256、当前资格、effective_case_constraints、所有最终 root_adjudications、所有 extensions.root_review、优先级与共责均相同。C003四原root及8扩展全部保留；A048第二root、B008同根两raw以及B013两扩展不省略。完整控制引用和逐项结论见 [finding-dispositions.json](finding-dispositions.json)，身份明细见 [verified-identities.json](verified-identities.json)。跨域原裁决文字已经读作验收控制，不据此声称独立重新读尽其参考源码。

运行观察、行为向量执行、参考执行、已证demo链均 **0**。仅自有文本/JSON/Git/hash/目录记账与手工静态推导；没有运行游戏、Ruby、编译/转换/生成/反序列化器或行为模拟器，没有参考源码复制或逐行伪码。静态向量给待执行设计，表内数值不是运行结果。模型请求 gpt-6.1-sol / ultra / Standard；无可信实际配置回显，实际配置 **UNVERIFIED**，保持已接受方案A，无降档、无新增确认门。见 [model-and-scope-receipt.json](model-and-scope-receipt.json)。

## 逐问题验收

下列ID均带前缀 `GIR-FD82-`。每项的PASS只针对B07候选贡献，原ID仍OPEN。参考简名的精确路径见末表；均为上述固定参考commit。正文定位指候选净化文件，旧正确条款与上游映射不反改。

### GIR-FD82-A020 — PASS_SCOPED

主责B07；定位：WP28 §5.3 → WP19 §3.5完整表N；静态目录：IU-56;ST完整既有目录。

同一 Bulbasaur、L50、IV31、EV0，按 HP/Atk/Def/SpAtk/SpDef/Speed：LONELY 为 [120,75,62,85,85,65]，BRAVE 为 [120,75,69,85,85,58]；WP28 消费已接受 WP19 完整25性格映射，薄荷只改计算性格。

反向/邻近对照：HARDY 中性为 [120,69,69,85,85,65]；相同性格拒绝或确认前取消均不消耗，不新创薄荷使用门。

独立参考：Nature 1-173；Pokemon 508-535;1069-1136；Species 3-31；ItemUtilities 445-488。冻结已接受他批：B01, B05；未完他批：无其他贡献批待项；候选/实际审查门仍适用。

### GIR-FD82-A024 — PASS_SCOPED

主责B05（B07贡献）；定位：WP30 §6.3 最初记录实际消费者；静态目录：GR-49;GR-52。

Bulbasaur L5 已知 TACKLE/GROWL/VINEWHIP，等级候选已覆盖；最初记录为空或 [AMNESIA] × 配置关/开四组，只有实际记录且配置开得到 [AMNESIA]。

反向/邻近对照：物种蛋招表有 AMNESIA 不等于消费者读取整张蛋招表；记录与等级候选重叠须按身份去重。can_relearn 谓词与 UI 配置门分别定位，不能互换。

独立参考：Reminder 1-199；Pokemon 717-724；Settings 148-151；Species 3-31。冻结已接受他批：B05；未完他批：无其他贡献批待项；候选/实际审查门仍适用。

### GIR-FD82-A026 — PASS_SCOPED

主责B07；定位：WP28 §5.6 → WP21 §4.2完整表F；静态目录：IU-57;FM既有目录。

完整复核 Rotom/Kyurem/Necrozma/Zacian/Zamazenta/Calyrex 六组表F。合法 Necrozma form0＋空 NSOLARIZER 融合合法 Solgaleo：form1、SUNSTEELSTRIKE 的 PP5/PP提升0，融合成员退出队伍、工具状态替换；缺招者走普通学习。

反向/邻近对照：第二成员选择取消保留原状态；形态提交后的学习拒绝不倒退既有形态/删招状态。保留缺身份与部分失败原资格，不补普遍事务回滚或额外守卫。

独立参考：Forms 221-265;330-383;562-596;653-697;699-729；ItemUtilities 580-768。冻结已接受他批：B05；未完他批：无其他贡献批待项；候选/实际审查门仍适用。

### GIR-FD82-A039 — PASS_SCOPED

主责B07；定位：WP28 §5.3 原始数量上限三层；静态目录：IU-49;IU-14;IU-15。

降EV树果先给原始请求上限：EV按每10点向上取整、幸福度升至255所需次数取较大者，再分数量配置与库存/UI。幸福255、EV250、库存25：多用开请求25，EV→0/库存→0；关请求1，EV→240/库存→24。

反向/邻近对照：幸福255且对应EV0为无效果失败；幸福未满但EV0仍有幸福作用，不能把EV单项界限当全局可用门。数量请求、选择和实际消耗分别说明。

独立参考：ItemUtilities 89-94;445-484;674-689；ItemEffects 995-1010。冻结已接受他批：无；未完他批：无其他贡献批待项；候选/实际审查门仍适用。

### GIR-FD82-A040 — PASS_SCOPED

主责B07；定位：WP28 §6.6 → WP19 §5.3；静态目录：IU-50;IU-09～17。

样本 Caterpie/FOCUSBAND/QUIRKY、HP与Atk两个不同 effort 身份：设施初值将510平均为各255，能力重算读原始EV并取EV/4整数63。

反向/邻近对照：普通增量入口252单项/510总量不规范化其他写入者；夹具明定两个不同身份，不把重复身份情况擅自推广。B05既有原始重算边界保留。

独立参考：Challenge 197-219；FacilitySample 1-8；Pokemon 1069-1136。冻结已接受他批：B05；未完他批：B17。

### GIR-FD82-A041 — PASS_SCOPED

主责B07；定位：WP28 §5.1 上下文拒绝/效果表；静态目录：IU-51。

战斗中满HP50、NONE、混乱3：Full Heal/Full Restore 可登记，库存1→0，执行清混乱→0，正常效果路径无退款；Heal Powder 同类资格并保留幸福惩罚。

反向/邻近对照：战斗 NONE/混乱0拒绝且库存1；POISON单独可清。非战斗满HP/NONE拒绝，不能套用战斗混乱资格。登记扣除与效果阶段分开。

独立参考：ItemBattle 119-145;426-454;482-521；ItemEffects 495-560；ActionItem 1-149。冻结已接受他批：无；未完他批：无其他贡献批待项；候选/实际审查门仍适用。

### GIR-FD82-A043 — PASS_SCOPED

主责B07；定位：WP29 §3.4及原稿售出·正常；静态目录：SH-08;SH-27。

买价300/卖价150、库存5、钱包/售出统计0且剩余容量750：明确数量5→金额/统计750、库存0；未改默认初值1→150、库存4。SH-08 加明示选5前提。

反向/邻近对照：库存5是最大可选量，数量窗口初值仍1；取消不写金额/统计/库存。上限不足与售出数量不等同。

独立参考：Mart 477-523;677-726。冻结已接受他批：无；未完他批：无其他贡献批待项；候选/实际审查门仍适用。

### GIR-FD82-A044 — PASS_SCOPED

主责B16（B07贡献）；定位：WP28 §5.4、WP30 §6.3；静态目录：IU-58;GR-49。

默认 TM57 为 TR CHARGEBEAM。兼容 Magnemite L5、当前/最初记录只有 TACKLE：背包导师包装入口学习成功，统计+1、最初记录去重追加、外层消耗；队伍直接入口学习消耗但不作该记录/统计写入。

反向/邻近对照：取消/拒绝均不追加或计数。遗忘后且额外最初记录配置开，仅背包入口记录可贡献 CHARGEBEAM；其他等级候选仍在，不能称整个重学集合为空。

独立参考：Items 4654-4665；Species 2125-2156；ItemEffects 75-96；Tutor 452-512；ItemUtilities 580-768；Pokemon 674-698。冻结已接受他批：B05；未完他批：B16。

### GIR-FD82-A045 — PASS_SCOPED

主责B07；定位：WP28 §5.3/§6.2/§7 → WP31 §6；静态目录：IU-54;BE13原行。

合法 Caterpie L100、Shield Dust、无 Everstone、非蛋/Shadow/Hyper、满级糖果开且有升级进化资格：进入进化预演后 BACK 取消，物种/等级保留、进化取消统计+1，处理器成功返回使外层库存1→0。

反向/邻近对照：选择/确认前取消不消费；配置关或无进化条件为失败。WP31 §6 与 BE13 原本正确的取消条款不改；不能把场景取消等同外层效果失败。

独立参考：ItemEffects 913-947；Evolution 84-134；ItemUtilities 674-689；Species 237-264；Settings 243-249。冻结已接受他批：无；未完他批：无其他贡献批待项；候选/实际审查门仍适用。

### GIR-FD82-A046 — PASS_SCOPED

主责B07；定位：WP28 §5.1主动HP请求表；静态目录：IU-52;IU-53。

主动场外与战斗HP表核查固定/配置请求量及截顶：Potion20，Super60/50、Hyper120/200、Max全补、Fresh30/50、Soda50/60、Lemon70/80、Milk100、Oran10、Sitrus取maxHP/4整数、Energy60/50、Root120/200、Full Restore全补。Sitrus HP1/max101→26，HP1/max105→27，各消耗1。

反向/邻近对照：实际增量不超过缺HP；满HP拒绝与状态/混乱资格按上下文。AI中Sitrus估计1与自动持物触发独立，不能覆盖主动请求表；配置开关两组保留。

独立参考：ItemEffects 378-455;582-618；ItemBattle 301-376；ItemUtilities 327-361。冻结已接受他批：无；未完他批：B11, B12。

### GIR-FD82-A047 — PASS_SCOPED

主责B07；定位：WP30 §4.2；静态目录：GR-45～48;GR-15修前提;GR-08～18其它原行。

每份经验先独立截断；非正份额在缩放/+1/后修饰前退出，EV先于经验。Caterpie L2基础39，未加成、recipient L3原EXP27：a78先除5取整15，缩放约12.6236再取整+1得13，总EXP40仍L3；延迟除5取整会错得14/41。兼任参与/共享、a39、有效参与2/共享1且均分开，独立9+19=28而非29，同级缩放取5+1=6。训练家加成开/缩放关、a11、异语言、Charm、Lucky Egg、幸福全部资格开，依次11→16→2→3→4→6→7，EXP27→34仍L3。

反向/邻近对照：首例关缩放得11/38；兼任例均分关得39基础；修饰链关幸福得6、去Charm保留Lucky Egg/幸福得4。合法基础1/L1、两等份各0：无EXP/统计增量而EV仍可得；零份额不能被+1复活。非零改基础2则缩放中间值1，后修饰继续按顺序截断。GR-15指非空参战记录但有效资格数0，不虚构空记录奖励。

独立参考：BattleExp 1-271；LuckyEgg 1693-1702；Species 237-264。冻结已接受他批：无；未完他批：B09。

### GIR-FD82-A048 — PASS_SCOPED

主责B16（B07贡献）；定位：WP30 §6.3；静态目录：GR-50;GR-30～34原ID非空资格。

普通合法 Caterpie L1 已知 TACKLE/STRINGSHOT，或 Magikarp L1 已知 SPLASH，最初记录空：无等级候选。原始重学界面初次详情渲染早于输入循环，缺少有效 Move 身份触发严格查找/校验失败。

反向/邻近对照：明定资源、字体、类型/窗口构造等此前环节成功；非空才适用原GR-30～34循环/取消描述。不是“空集正常false”或宿主崩溃/地图可达的实测结论，外层预检另有边界。A048保留 RUN-C-116 第二根裁决。

独立参考：Reminder 1-199；GameData 88-107；Validation 12-29；Species 237-264;3402-3428。冻结已接受他批：无；未完他批：B16。

### GIR-FD82-A049 — PASS_SCOPED

主责B07；定位：WP30 §6.1/§6.3；静态目录：GR-51;GR-25/26。

战斗和普通学习的遗忘包装都进入单成员 Summary：四个旧槽＋第五新招。选择旧0～3成功替换，返回-1保留旧招；战斗另同步活跃招式PP。

反向/邻近对照：BACK/第五槽为取消，HM非debug拒绝并继续选择、debug另论。机器keepPP只是该入口资格，不把战斗同步、通用学习与机器PP行为混成一次提交。

独立参考：BattleExp 247-270；ChooseScene 447-457；ItemUtilities 630-642；Summary 1232-1296;1348-1370。冻结已接受他批：无；未完他批：B09。

### GIR-FD82-A050 — PASS_SCOPED

主责B07；定位：WP31 §5.1；静态目录：BE36;BE37。

有效非透明目标素材与正常计时前提下：目标预备隐藏，初次更新设可见/白色255但缩放0；40/20=2秒开始放大，52/20=2.6秒已首次大白轮廓，早于约9秒成功揭示。成功闪白结束恢复正常颜色。

反向/邻近对照：后来取消恢复旧种类，却不能抹去先前的目标白轮廓；早取消另有时点。静态属性和时序不等于真实像素/素材输出证明。原稿只补这条错误预演，不改正确取消规则。

独立参考：Evolution 1-136;152-195；Picture 177-185;362-405;453-508。冻结已接受他批：无；未完他批：B17。

### GIR-FD82-A051 — PASS_SCOPED

主责B07；定位：WP32 §5、附表§4；静态目录：CX22原ID;CX39。

队伍容量3且 A/B/C 已满，允许替换、空箱、无伙伴、send0/2并选A：队伍B/C/X，L0=[20,30,nil]、K=[3,0,nil]、D=[49,5,nil]。CX22补明容量/已满前提；当前玩家扫描顺序保留。

反向/邻近对照：默认容量6但只有三成员时直接追加，不是替换分支；不存在的槽为nil而非0，不移上述记录。非满、送箱/拒绝分别保留。

独立参考：CatchStore 1-105；Peer 1-77；Trainer 65-83；Settings 219-220；BattleStart 608-655。冻结已接受他批：无；未完他批：无其他贡献批待项；候选/实际审查门仍适用。

### GIR-FD82-B008 — PASS_SCOPED

主责B09（B07贡献）；定位：WP28 §3.5/§6.5；静态目录：IU-55。

合法自定义 Direct5、可耗非重要非球、资格/效果处理器均缺，普通内部战斗且玩家活：Use可见，缺资格处理器回退true，登记库存1→0；空直接效果清选择后不退款。

反向/邻近对照：类型1/2/3相关效果存在守卫不覆盖Direct5；类型1/3缺效果拒绝于扣库存前。保留原 RUN-A-042/RUN-B-008 同根裁决，不新增ID或推成所有类型都会放行。

独立参考：ChooseScene 196-239;312-331；Command 88-156；ActionItem 1-149；ItemUtilities 38-50;90-105。冻结已接受他批：无；未完他批：B09。

### GIR-FD82-B013 — PASS_SCOPED

主责B09（B07贡献）；定位：WP32 §5持物依赖（§4/T2→当前持物读取）；静态目录：CX40～42。

伙伴真实参战、普通双野生一敌已败另一被捕，玩家满6 A..F，A持X/B持Y、其他与新捕获无物品，空箱且无额外形态/持物回调：旧合并战斗列表与玩家列表分离而成员引用相同。接收移A入箱、玩家变B..F/N，初始物品首6变[Y,nil..]；结束按旧列表恢复，箱A最终Y、B最终nil。

反向/邻近对照：无伙伴同一队伍列表：箱A保持X、B保持Y；伙伴中段C移出且A:X/B:Y/C:Z/D:W，箱C变W、D变nil、A/B不变。伙伴前提不可省。当前持物扫描读实际状态；正确扫描时序/L0/K/D不改，CP20/WP38由B09另改。

独立参考：BattleStart 171-225；Battle 119-159;297-309；CatchStore 1-105；Peer 1-77；Storage 214-252；BattleEnd 479-511。冻结已接受他批：无；未完他批：B09。

### GIR-FD82-C003 — PASS_SCOPED

主责B21（B07贡献）；定位：WP28 §5.1、WP30 §6.3；静态目录：IU-59;GR-52;GR-53。

本批C07/A23：source HP50/max120，转移请求24，source50→26；target30/max54→54实际+24，或max40→40实际+10，两组源均扣24。A31：三条不同候选为3；最初M1与已有M1重叠去重为2。A33：仅蛋无合格者，BACK清选择为-1/名字空；非蛋HP1合格。

反向/邻近对照：转移拒绝自己/蛋/死亡/已满、source≤24，无状态写入；A31配置关只等级2。要求非蛋且HP>0的选择器拒非蛋HP0，只要求非蛋的另一选择器可接受HP0。四个原root和全部8扩展资格保留，未把本批A23/A31/A33改动当全ID验收；A32属A048/B16，LC L09属B21。

独立参考：ItemUtilities 327-361；Reminder 1-199；PartyUI 1141-1180;1258-1288;1504-1531。冻结已接受他批：B02, B03, B04；未完他批：B08, B14, B15, B16, B17, B18, B19, B20, B21。

### GIR-FD82-D023 — PASS_SCOPED

主责B16（B07贡献）；定位：WP29 §4正确表保留、§8显示边界；静态目录：SH-25原行;SH-28。

BP显示先把单位价整数减半再乘数量，实际确认/扣款仍全价：20×数量1/2/3显示10/20/30、实际20/40/60；奇数21×3显示30、实际63。

反向/邻近对照：不能把奇数总价63整体减半取整31当显示值；资格和实际全价规则不变。WP29 §4原正确BP公式/SH-25保留，§8/SH-28仅显示边界；UI主责B16尚待。

独立参考：BPShop 330-345。冻结已接受他批：无；未完他批：B16。

## 完整差异、回归及原稿写入门

未过滤 `219cc3c182750155e9dbf2cb619f420b3922de27 → a22df6b1d9465b68e45558c57bc69c61939baeaf` 共25路径：8正式文件＋6原稿修改，11项B07证据新增。没有删除、改名或其他跟踪文件变化。8正式文件是WP28、WP29、WP30、WP31、WP32主表/附表及两个目录；六原稿与前六正文对应。独立核对14输出的before/after commit、blob、SHA256及bytes；116固定输入按64计划读＋8 B04追加输入＋35冻结证据＋2当前管理＋7固定计划身份核对。读身份与哈希不称全文语义验收。

父合同原本 `original_specs_write_authorized:false`，潜在六路径本身不构成写授权。本轮用户委托明确“8正式文件+6必要原稿，核查原稿写入门授权及范围”；作者记录了“同步错误原稿/净化正文/静态设计及本批追溯，正确原稿不反改；全部本轮修订/报告/commit和普通push已授权”的新指令，并限定覆盖旧read-only门的六个错误原稿。本复审在这个明确的本轮六原稿范围内接受，不扩大授权。

逐一核对 `original-sync-plan.json` 的六路径、原ID、必要错误条款、前后身份和 `original-sync.patch` 的精确内容。独立从固定Git字节重建声明的规范化difflib差异并核对每份diff SHA256，`git apply --check --reverse` 成功且未应用补丁。差异不是跨文件批量替换；原稿新增状态说明只标明本轮后继待审，不改历史批准对象。WP29原正确BP规则、WP31正确取消/BE13、WP32正确当前扫描、WP19/21已接受映射均保留。

授权证据限制：作者“先备计划/差异再写入”以及原父会话新指令的完整上下文未取得独立时间/会话凭据，不能由最终Git树认证历史写入顺序。本结论认证本轮受委托的六路径和精确差异范围，以及候选现存授权记录；不把历史顺序自述认证为平台事实。这个限制保留在配置/范围收据，不另设用户确认门。

全部旧目录ID顺序和重复出现次数保持。新28行是IU-49～59、SH-27～28、GR-45～53、BE36～37、CX39～42；改旧8行仅SH-08、GR-15、GR-30～34、CX22，分别纠正明示数量、有效经验资格数、非空重学资格和已满容量前提。BG/DC、RM/CP完整章节逐字节相同，BE13不变。已有正确BP实际扣款、进化取消、扫描顺序和一般数量选择未反改。新增表与正文、原稿、19项追溯相互定位一致；静态设计没有升级成运行测试。

边邻核查涉及WP19/20的Nature、原始EV与最初记录；WP21六组形态映射及部分失败；WP24伙伴/战斗入口；WP38捕获接收；WP40物品注册/效果；WP41经验；WP42遗忘；WP50持物；WP51 AI估值；WP66相关UI条款。B06 WP24只沿用已接受六逻辑音轨请求和引子前记忆，既有PT41–63身份不改，不扩大至伙伴/雷达/完整BattleAudio。WP38/CP20尚有伙伴条件的全局不变说法、WP66尚有空重学及BP显示表述，均有B09/B16主责待项；本批消费者明确条件、保留冲突追踪，没有倒写受保护章节或批准那些正文。

## 作者自检的对照结果

在独立初步证据锁之后读全11项新增作者证据。作者15项自检只能作作者声明；本审自有14项文档/Git检查全部PASS，见 [document-checks.json](document-checks.json)、[verify_documents.py](verify_documents.py)。比对确认输入、输出、完整控制与共责、精确六原稿差异、28/8目录、保护章节、JSON和19项追溯、固定参考树/干净状态一致。另有11项审者报告结构、链接、证据行范围、零执行和写范围检查全部PASS，见 [report-validation.json](report-validation.json)、[verify_report.py](verify_report.py)，同样只是文档记账。作者56参考文件哈希/bytes/行数与读区间分割独立核对，但不据此声称审者读了所有这些区间，或证明作者历史语义阅读/其另一个工作区历史干净状态。

author-report的行为摘要与独立正向/反向对照相合；acceptance-map/traceability定位是复核索引，结论来自固定原控制、参考及候选正文。areg-proposals是建议，未改公共登记。作者xhigh请求记录与本审ultra请求分开，二者实际配置均未认证；未凭旧Max措辞或作者自述作配置通过依据。暂未发现作者自检掩盖的本批实质错误。

## 必须继续保留的未完范围

1. 单独 R-B04 候选影响审查仍须自身精确报告收据，本报告不认证其完成或结果。WP28/WP30改变引入资源/消息/音效/转场、严格身份验证及异常/正常返回交界，旧B04 actual批准不能自动转移。R-B07已完整审本批，包括相邻依赖的限定行为；这仍不能替R-B04独立链。
2. 实际整合尚未发生于本审对象。父任务后续必须绑定完整actual SHA及实际依赖，检查 predecessor→actual 与 candidate→actual 的未过滤差异，并分别完成R-B07 actual和独立R-B04 actual审查。两个候选链和两个实际链均通过才满足父任务门；当前PASS不会自动带入actual。
3. 跨批责任继续保留：A040/B17；A044/B16；A046/B11/B12；A047/A049/B008/B013/B09；A048/D023/B16；A050/B17。C003的B08、B14、B15、B16、B17、B18、B19、B20、B21仍待各自贡献；已接受B01/B02/B03/B04/B05只是固定输入，不在本审重新全球批准。下游B08/B09/B13/B15/B16/B21不据此自行开放。
4. C003完整八扩展不缩成局部三项：C01选择/确认/空身份；C02音频与事件/文本控制；C03地图跳跃、地牢和天气；C04小地图、绘字、反射与时间缓存；C05遭遇/引子与连接；C06野战入口、毒步与病毒/伙伴；C07重学、HP转移、事件选择及LC；C08格盘目标/持物、反向身份与表头。原root的P2、局部资格P3、同根计数及共享raw收窄照原控制，不因本批PASS关闭C003。
5. U01–10/G01–12/AX01–20及具名未读保持。8个杯赛名单引用文件、pokemon_metrics.txt样本、备份未全文读；二进制、mkxp配置、实际图像/音频/字体/宿主输出、插件组合、动态调用/deprecated别名、EventScene/动态阴影、真实地图可达和demo链未穷尽。1024/2048只为条件夹具；前置媒体/字体/身份失败与后续静态规则不混同。[source-reading-log.json](source-reading-log.json)逐参考文件列实际打开区间、剩余区间和其余跟踪路径；[reading-events.jsonl](reading-events.jsonl)保存文本范围打开记录，不声称截断输出中每行都已语义审查。

公共登记不写，正式文件/原稿不由审者改；229 OPEN、0 CLOSED保持。要求返工项：无。阻塞本批报告提交的事项：无。全局/实际接受所需未完门和证据限制如上。

## 独立参考定位简名

所有路径以固定参考仓为根。各文件commit/blob/SHA256/bytes及实际打开区间在审者source-reading-log内；本表和逐项行范围是追溯定位，不包含源码副本。

| 简名 | 路径 |
| --- | --- |
| Nature | `Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb` |
| Pokemon | `Data/Scripts/014_Pokemon/001_Pokemon.rb` |
| Species | `PBS/pokemon.txt` |
| Settings | `Data/Scripts/001_Settings.rb` |
| Forms | `Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb` |
| ItemUtilities | `Data/Scripts/013_Items/001_Item_Utilities.rb` |
| ItemEffects | `Data/Scripts/013_Items/002_Item_Effects.rb` |
| ItemBattle | `Data/Scripts/013_Items/003_Item_BattleEffects.rb` |
| ActionItem | `Data/Scripts/011_Battle/001_Battle/006_Battle_ActionUseItem.rb` |
| Challenge | `Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb` |
| FacilitySample | `PBS/battle_tower_pokemon.txt` |
| Mart | `Data/Scripts/016_UI/020_UI_PokeMart.rb` |
| Items | `PBS/items.txt` |
| Tutor | `Data/Scripts/019_Utilities/001_Utilities.rb` |
| Evolution | `Data/Scripts/016_UI/001_Non-interactive UI/004_UI_Evolution.rb` |
| BattleExp | `Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb` |
| LuckyEgg | `Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb` |
| Reminder | `Data/Scripts/016_UI/022_UI_MoveRelearner.rb` |
| GameData | `Data/Scripts/010_Data/001_GameData.rb` |
| Validation | `Data/Scripts/001_Technical/001_Debugging/004_Validation.rb` |
| ChooseScene | `Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb` |
| Summary | `Data/Scripts/016_UI/006_UI_Summary.rb` |
| Picture | `Data/Scripts/005_Sprites/010_PictureEx.rb` |
| CatchStore | `Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb` |
| Peer | `Data/Scripts/011_Battle/007_Other battle code/004_Battle_Peers.rb` |
| Trainer | `Data/Scripts/015_Trainers and player/001_Trainer.rb` |
| BattleStart | `Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb` |
| Battle | `Data/Scripts/011_Battle/001_Battle/001_Battle.rb` |
| Storage | `Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb` |
| BattleEnd | `Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb` |
| Command | `Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb` |
| PartyUI | `Data/Scripts/016_UI/005_UI_Party.rb` |
| BPShop | `Data/Scripts/016_UI/021_UI_BattlePointShop.rb` |
