# B20 独立云端 FULL 候选复审（19项贡献／15项主责）

结论：**REQUEST_CHANGES，3项P2阻断问题**。行为方向及多数新增条文可静态核对；C024提取写出顺序、INTAKE当前ASCII定义、C029形态求值门尚未满足合同。16项贡献在本地范围为PASS_SCOPED_STATIC，3项需修订；主责13/15满足、2/15需修订，共享3/4满足、1/4需修订。旧内容保全通过，scope许可未被当成质量证据。

## 固定审查身份

| 对象 | commit | tree |
| --- | --- | --- |
| 审查NEW | `1abaefb1db5818ff9404392143c476979d34c21a` | `2e40f9ad0e8fa40377d39e5a19eaa74cc2e05e85` |
| B19 C | `de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f` | `88a400af08253bea8d97ee2ef2fa6636f0900f92` |
| 入口包 | `9a46a131ba2f7ea82b6eed823aa892cb57b0fba7` | `3397ef849f652c47506b492dabc32c51f5a12c76` |
| 最终入口读回包 | `272885cca76c36cd04dde27b6be2c654759ec4c2` | `46969272b7387645bc97b91d227734e89a5f8a80` |
| 只读参考 | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` | `7589c800b61ba13a13040ed0d686979b80a84fd0` |

审查入口：`review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-1/FULL.md`。本报告写在分支 `codex/cloud-B20-independent-full-review-20261011`，起于最终入口读回包；只新增自己的复审文件，不修改正文、main、参考或旧证据。该分支提交身份见`publication-readback.json`；最终附加读回记录的远端身份在交付回覆中给出。

完整控制以原findings `93e10babe0b9c9ef8b3f5277754541b447beeeb4`、批准acceptance/PLAN `41fffb540c6483f5296ea0d33b789b75180d27ed`及B19后完整派发 `669997ac28258f26d0bafc81b1d081abb407a3a1`为准。19个完整对象的原/批准指针、独立重算对象哈希及全部必要资格字段在`per-ID-review.json`，文件身份在`source-reading-log.json`。其root、extensions、前提、最小修订、determinate与案例边界一并审查，不缩成先前六项切片。原稿scope grant `d54fba72a75a3324d7a3daf8e02bc1ecf6c8beeb`仅允许三份固定after应用；不证明语义正确。

## 方法与完整差异

独立获取固定Git对象与参考文本，读取正文及相关调用者/状态/失败门，手工追踪静态案例。只执行Git、文本读取和新写的JSON/哈希/目录身份比较。未执行参考游戏、Ruby、编译器、转换器、反序列化器、行为向量、旧执行脚本；没有构造/加载参考实例。所有数值/事件例均**NOT_EXECUTED**，不是运行测试。素材、宿主、插件、备份遭遇表及具体Demo事件前提继续保留；U01–U10、G01–G12、AX01–AX20、条件树果67等既有范围不扩为可玩证明。模型参数接纳即有效，未做模型/额度审计或CLI替代。按原合同禁止额外/嵌套任务，独立完成本派发。

以 `git diff --no-ext-diff --no-textconv --binary --full-index C NEW` 独立重建未过滤差异，在内存逐字节比对唯一已发布流，完全一致：

- 固定流commit：`f325f625f879105f7811713d9a38cc58da875de2`。
- 路径：`review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-1/stream/C-to-NEW.full.diff`。
- blob：`54c4dcf3be88f175fcceaca5c3642c29c532adfe`。
- SHA256：`0889ed6d2a4d300325c0fa5d319d9fd89b72bdaeec8e8a0401c7185a25f9eccb`；字节数：**1,189,663**。

本报告只引用该固定SHA/路径/哈希，没有重新发布差异、复制参考源码或递归复制控制包。71个输入均独立核对blob/SHA256/字节数（69个C、2个immutable）；此身份核验不冒充71篇全文语义重读。新鲜参考阅读的文件身份与精确范围单列，旧已接受依赖只在固定身份和资格下复用。

## 问题与验收条件

以下位置均指审查NEW `1abaefb1db5818ff9404392143c476979d34c21a`；源位置指固定参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。完整blob/SHA256/字节数与静态前提在`findings.json`。编号仅为本报告局部发现，不创建canonical ID。

### F01／P2／GIR-FD82-C024：提取备份顺序错误

WP75:48写成“先备份原归档、输出散文件/索引、再写单节装载器”，目录B20-C024:273及每ID案例:70重复此顺序。参考`scripts_extract.rb:12–66`实际为数量门、创建/清树、逐节散文件/目录写出、备份、loader。当前WP75:278–281及原稿§12.1已正确把备份列为收尾。另未见独立索引文件写出；编号布局不能暗示新增产物。

静态反例：11节可读归档，清旧散文件树成功，首个非空正文的文件打开失败。源到失败点已清树，但备份未到、Scripts归档未换；既有备份B0不变（若原无备份则仍无）。候选“先备份”却错误推出已有新备份。正常全成功对照仍是全部散文件后备份再loader；combine同一11节输入在门处拒绝。

验收：同步§3.3、目录案例和每ID有序变化，补这个已发生清树而未备份的失败边界，准确限定编号布局；保留原正确方向/收尾及9/10/11矩阵、无回滚承诺。新固定NEW复查这三处及后继身份，不能以scope许可通过。

### F02／P2／WP80-INTAKE-R01：当前概念定义仍全角化

WP75:26仍把`item：X`、`hiddenitem：X`、`Battle：`、`Type：`定义为可展开事件简写（U+FF1A）。同文件:63及:99、B20-INTAKE-R01:287正确ASCII，因而当前合同自相矛盾。参考Compiler MapsAndEvents:487/524/527及:780/785只按U+003A识别；该位置属于已裁决C02扩展，不能以作者只列部分正例排除。

静态反例：POTION注册且事件页合法，`item:POTION`转换两页，只有冒号换成`item：POTION`就不命中；hiddenitem同理。Battle全角块不能满足Battle收集/解析门，Type全角块不提供所写类型。另`ITEM:POTION`/`HiddenItem:POTION`前缀仍可命中大小写不敏感门；注册标识大小写另判。目录CV-M07:150的“小写必要”来自C、在NEW字节不变；它是当前说明需解释的历史冲突旁证，不另开跨批次关闭项。

验收：将四个当前正向定义改成ASCII，只把全角留作明确不匹配负例；补异码点的道具/注释静态对照，在当前说明或新增案例明确前缀大小写不敏感，保留B19锁定行历史字节。对本批实际活跃正文/目录逐字符复查，保留Move/OppMove/Common空白区别、Trainer/SellItem/s:及其它owner扩展资格。共享INTAKE主责仍B21，本报告只判B20贡献。

### F03／P2／GIR-FD82-C029：getter读取消费不足以通过求值门

WP77:139、B20-C029:278和每ID案例:133只给“无外层强制覆盖、getter实际被消费者取用”，随后直接承诺orb/DistortionWorld→1，否则0。参考Pokemon:147–157在forced门后还会因in_battle或in_storage提前返回存储形态；只有两者都假才调GIRATINA getForm（FormHandlers:267–273）。form_simple从不重算。已接受WP21:246、WP18:150已明确这个门，候选却未链接。C029 minimum_revision明确要求与形态主规格求值门链接，root亦保留外层资格。

静态反例：GIRATINA存储0、持GRISEOUSORB、forced为空，在战斗（或独立仓库）状态读form，满足候选写明的前提却返回0且不调处理器。相邻正常例：两个状态都假才按orb/旗标得1/否则0。逆向：存储1、无orb/旗标、在战斗/仓库仍得1，不能推出否则0。forced及非目标物种仍按各自门。

验收：明确0/1是动态处理器**实际执行**的结果，说明form的forced与战斗/仓库提前返回、简化读取区别；链接只读WP21§6第2条及必要WP18，不改其它owner正文；同步正文、目录和每ID案例，加入战斗/仓库存储形态对照。物种/道具身份、地图进入未证、③④=0保持。

## 完整19项判定

PASS_SCOPED_STATIC只表示对应本批贡献在固定输入和静态前提下可核对，不代表执行通过、canonical关闭、affected gate、ACT或正式接受。每项完整控制绑定及异常/反向/保全说明见`per-ID-review.json`。

| 贡献 | 主责归属 | 候选静态结论 | 核验要点 |
| --- | --- | --- | --- |
| GIR-FD82-003 | B21（共享） | PASS_SCOPED_STATIC | 复制快照后改源、两次粘贴各独立；Insert属性联动而槽删除/交换不联动。必要.anm持久格式及35兼容文本保留；实现可采用独立表示，不要求照搬类/方法/序列化快照的内部实现。原稿未获架构清理的额外许可，不凭净化行删去必要行为。 |
| GIR-FD82-C003 | B21（共享） | PASS_SCOPED_STATIC | 核对.midi不复制而.mid复制先于坏anm判定；CommonEvent独立块无收集、Battle先支吞续行、EndSpeech末CommonEvent:5才可达；b男性/pg玩家性别/CN钱窗；bs/fs实体往返分开。四个B19修复行未改。 |
| GIR-FD82-C007 | B21（共享） | PASS_SCOPED_STATIC | 35条按顺序、大小写敏感全出现文本替换，2条正则独立；每项精确输入/产物已逐项比源。无边界/引号保护，前项产物可被后项匹配。治疗首字符门先于去空白，精确i和99999包装；三路线前缀在脚本正常求值后才控制帧结束。 |
| GIR-FD82-C020 | B20（本批主责） | PASS_SCOPED_STATIC | 目录chdir枚举在子窗口前，缺目录未捕获；空sheet在刷新取空选项失败，空SE仍有cry、空BG仍有erase。文件保护占位/nil与目录异常分开。 |
| GIR-FD82-C024 | B20（本批主责） | REQUIRES_REVISION | extract 9拒、10/11允；combine 9/10允、11拒正确。新增先备份顺序错误，详F01；当前原稿及§12正确方向/收尾不能被新增条文反转。 |
| GIR-FD82-C025 | B20（本批主责） | PASS_SCOPED_STATIC | 整帧与Insert复制所有实际槽包括60；区间/PasteLast/Clear/旧格式检测修正仅0–59；目标60不清。TAB遍历实际长度可编辑60、常规精灵仍0–59；换回2恢复显示资格。 |
| GIR-FD82-C026 | B20（本批主责） | PASS_SCOPED_STATIC | 活动阶段先于同帧start捕获；每层一份旧位置/opacity/RGBA，后捕获含零时长重置全份。图形P(q)=P0+(T+P0)q；完整RGBA含未参与旧值，后项覆盖。 |
| GIR-FD82-C027 | B20（本批主责） | PASS_SCOPED_STATIC | 9行分页改5/9命令类型却保留旧计数9；断句只拼1–4却删1–9。后续重访使Following重新升首行；Tail只合一次L2。最终序列与源码游标/短行/分页顺序一致。 |
| GIR-FD82-C028 | B20（本批主责） | PASS_SCOPED_STATIC | TN联系人、PN玩家、TP取max(current/start)的联系人版本队伍、TE该联系人图Land前四否则Cave否则Water、TM该地图；引用WP63且维持登记缺口。 |
| GIR-FD82-C029 | B20（本批主责） | REQUIRES_REVISION | GIRATINA与GRISEOUSORB身份及处理器0/1分支恢复正确；getter读取消费前提不足，缺战斗/仓库求值门及主规格链接，详F03。 |
| GIR-FD82-C030 | B20（本批主责） | PASS_SCOPED_STATIC | 克隆原条件/移动属性；首页selfC保留、结束A/再战B；EndIf/Vanish清self，原switch1启用→覆盖switch2=N，否则启用switch1=N而保留switch2；变量门不删。 |
| GIR-FD82-C031 | B20（本批主责） | PASS_SCOPED_STATIC | organiser初始选0 Yes，BACK取消映射3−1=2；直接USE正常写盘清缓存离开、BACK继续、不写。No独立不写离开；0项仍可保存。 |
| GIR-FD82-C032 | B20（本批主责） | PASS_SCOPED_STATIC | 路径保存窗口坐标不减64；curve拖钳X0..512/Y0..384、hand不共用钳制；写回画布统一+64。 |
| GIR-FD82-C033 | B20（本批主责） | PASS_SCOPED_STATIC | ALT像素命中逆中心、源区、zoom、mirror，但不逆角度；渲染仍施角度。静态不对称192图146,96及指针350,300在0/90检查同像素。 |
| GIR-FD82-C034 | B20（本批主责） | PASS_SCOPED_STATIC | 六族整体旧形、括号非空，没有固定元数门；逐个存在的尾位按文本条件消费，中间必需成员前占位不能删。18例核心/显式默认/可败非默认位置和插入序均比源。 |
| GIR-FD82-C051 | B20（本批主责） | PASS_SCOPED_STATIC | 源码门模板确实调用follow_into_door/hide/put；分派前快照全体、横优先一步prepend累计。P5,3/F1 5,4/F2 5,5得上1/上2再opacity0。 |
| GIR-FD82-C083 | B20（本批主责） | PASS_SCOPED_STATIC | 唯一完整数学入口保留人口σ、权重分支/边界/归一、正半向上、下限1→加2→capM；含蛋/濒死，不取可战斗队伍均值。缩放−4+0..4再钳、重算/重置。 |
| GIR-FD82-D024 | B20（本批主责） | PASS_SCOPED_STATIC | 曲线N点参数grid含两端、Catmull-Rom端点重复；hand/改帧数弧长递推1/N共N+2候选、只写前N。hand近整数半远0，改帧数实数。 |
| WP80-INTAKE-R01 | B21（共享） | REQUIRES_REVISION | Move/OppMove空白、Common直接拼名、Trainer/SellItem/s:正确；WP75概念正向定义仍有四个全角冒号，详F02。全文本地兼容义务不由新示例代替。 |

## 旧内容保全与独立实现边界

C→NEW共42条路径变化：7个获准payload修改、35个本次作者证据新增，无删除。C的36,856个旧跟踪文件中，除这7个payload外的36,849个路径、类型/模式/blob全部相同；AGENTS、参考/旧证据、公共登记、旧接受记录和其它owner正文没有既有修改。七个payload的C/NEW commit/path/blob/SHA256/字节数逐项见`identity-and-preservation.json`，三原稿还独立等于scope grant的exact complete-after及已发布proposal after。

目录旧195 ID顺序/重复次数完整保留，新增19为214；193个旧行逐字节相同。改动仅AN-M23（以精确渐变合同替换错误“仅参与项”，其余事实保留）与CV-M18（补完整35＋2合同链接，其余五个旧对照不变）。两改行前后整行SHA256见身份报告。B19/PA040及非本批owner行逐字节不变；308条既有接受、19个accepted batches、229 OPEN/0 CLOSED记录未变。此结论由旧树及行比较取得，不依作者布尔声明。

独立实现可决定60槽与实际存储、复制隔离/联动、共享渐变状态、文本转换順序与精确词法、坐标与采样、页面合取/优先、跟随快照/路线异步等行为，无需照搬参考类/方法/容器架构。必要兼容字符、物种/持物身份、持久文件格式、异常及部分写入语义仍保留；F01/F02/F03使当前版本在各自边界不能得到唯一正确实现，因此本候选不通过。

WP77仍限配置①与静态消费者②，③已证事件链=0、④运行观察=0；主稿材料未证、缺口及依赖资格不因本次静态案例增加。全部源阅读是文本；压缩loader不解包，旧执行脚本不运行。

## 后续门与交付

本报告对固定NEW给候选FULL结论。作者需处理上述有限3项并发布新的固定候选；当前branch的后继不能沿用此NEW结论。父级的独立affected审查及后续精确ACT门另行完成。没有自签actual、注册G/ACT/C、正式接受、main合并或推进B21；canonical及原主责全部保留。

输出：`REPORT.md`、`findings.json`、`per-ID-review.json`、`identity-and-preservation.json`、`source-reading-log.json`、`output-manifest.json`，随后附`publication-readback.json`。普通push后，在独立无本地对象共享的bare仓库从远端获取报告分支，逐个读回上述输出并比较blob、SHA256、字节数；最终receipt自身也由第二次远端读回验证，身份在最终交付回覆中给出，不制造递归receipt。
