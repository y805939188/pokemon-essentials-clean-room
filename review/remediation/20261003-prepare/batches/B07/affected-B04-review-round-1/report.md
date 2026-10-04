# B07 候选的独立受影响 R-B04 复审

结论：**PASS_SCOPED**。仅对 B07 候选引起的 WP15–17 资源／音频／视觉／文本／输入交界及冻结读取身份给出限定结论，未发现新的本范围必修缺陷。不是 R-B07 的 19 贡献／12 主责全批验收；不接受 B07，不整合、不登记、不关闭 ID。实际 integration 尚未提供和复审，本报告不能提前批准实际版本。

精确被审候选 `a22df6b1d9465b68e45558c57bc69c61939baeaf`，唯一父／已接受 B04-C 后继 `219cc3c182750155e9dbf2cb619f420b3922de27`，候选 tree `336fc0f3693d20b733d40f60d42d3bbe6323e52f`。候选同时包含正式 payload 与 11 份作者交接证据，本次检查绑定其完整 Git 对象；报告是独立分支上的后继提交，报告 SHA 在普通 push 回读后由外部最终交付提供，不自引用。分支为 `remediation/20261003-prepare/review-B07-affected-B04-1`。

已接受 B04 实际对象 `9e2dadfa650e2111b77f9eae1f834cc00b8805d5`、独立报告 `acda1abc811cc07ea83c6a0930872e9a8cea174e`及父后继219的 acceptance-stage-1/downstream-handshake共同确定反向门。WP28/WP30两份消费者发生变化，必须重查；不能把旧批准自动转授新字节。B04历史35局部贡献／23主责仍以原局部范围有效，完整35行承接见 [B04-conclusion-dispositions.json](B04-conclusion-dispositions.json)。未受影响来源族没有重新做全批语义审查。

请求 gpt-6.1-sol／Ultra／Standard(default)，实际模型、推理及服务无可信回显，均 **UNVERIFIED**。遵用户方案A继续独立限定审查，不新增确认或配置认证门，不自行降档／加速，未派生子任务；见 [configuration-receipt.json](configuration-receipt.json)。历史R1/R2旧门文字不可变保留，不控制本轮已授权方案A。

## 固定依据与独立顺序

读取根 AGENTS.md 的干净室、只读参考、行为规格与证据分层规则；适用范围没有另一个局部AGENTS或本地SKILL。报告明确写入仓库专用新目录，不调用 Library／Pages，不改忽略项或跟踪参考。原全局对象固定 `93e10babe0b9c9ef8b3f5277754541b447beeeb4` 的 `review/global-independent-review/2026-10-03-fd82a639/findings.json`，计划和 acceptance 固定 `41fffb540c6483f5296ea0d33b789b75180d27ed`。执行 current_qualifications、effective_case_constraints、最终root_adjudications及每条extensions.root_review优先规则，不能按历史/raw扩大资格。

先读冻结合同、原问题／反例／验收、完整14正式差分、修订正文和相关消费者，独立读固定参考与正反分支；作者报告和review-request用作范围输入。形成 [独立首判断](independent-first-judgment.json)后才读取详细self-checks并比较。首判断285文档检查通过，追加作者身份／范围记账核对后 [496文档检查](independent-validation.json)全部通过，另有 [340项报告一致性核验](report-validation.json)全部通过。检查只操作Git对象、哈希、JSON、文本／行与链接；未执行参考或静态行为向量。[作者对照](author-comparison.json)不能代替独立判断。

参考由本审者在同一容器R1独立准备于 `/tmp/rb04-reference`，本轮重新验证真实commit类型、HEAD `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree `7589c800b61ba13a13040ed0d686979b80a84fd0`、Maruno17/pokemon-essentials origin及干净工作区；此后仅Git／文本读取。新鲜读取30路径、61范围、3310去重行，精确hash／范围／未读补集见 [source-reading-log.json](source-reading-log.json)。作者56路径仅另核字节与范围记账，不计为本审者语义阅读。未运行Ruby／游戏／编译／转换／生成／反序列化／媒体读取器／参考模拟器；运行观察、参考执行、行为向量执行、已证demo链全部0。

## 精确差分与读取身份

完整父→候选25路径：14修改（8最终正文／附表／目录＋6必要原稿）和11新增B07作者证据，无公共／历史修改。完整未过滤 [complete.diff](complete.diff) 为503874 bytes、SHA256 `4350df38e45fe7b09d87b1e0f56d03af4bb1a456a78d99fbb883a4dbdb7d98e2`；[formal.diff](formal.diff) 为110289 bytes、SHA256 `351110bc2ebf227a89051dc318637931630f922bb2c1be8c39fde280b2a7e855`。逐路径新旧blob／SHA256／bytes及116冻结输入见 [input-identity-manifest.json](input-identity-manifest.json)。哈希完整不代表语义全读。

| 反向消费者 | before blob / SHA256 / bytes | candidate blob / SHA256 / bytes |
| --- | --- | --- |
| final creature-rpg/wp28-item-use-and-training.md | 048b8ecc193fccaacf0f6f6e8bf1d887f3856076 / 6aba982f3fff5a053030d0bfff71b3866b9c4f5ac55aa6f21a2df4ed176e2feb / 32079 | bb7c344cfbb24b8f8eb3e8ed8bfea0be6e426580 / 63d6b9d244b1700f88e311edae37306aad9831358256c1c8ed60f63a11a5737a / 39277 |
| final creature-rpg/wp30-growth-learning-and-friendship.md | 72578036b0cc9d1268d3be5250a3737195082df9 / 24ad1e4513a5e2ac0458895851d32a6969c1cc2ffe8ee38728260ea98257d610 / 25396 | ea4ebda45c4827d31a4d0af9bcf4332313b64104 / 97145b9f2bb6c5109f011c61514455558ac4bf62254a701258facd786f042e38 / 28837 |

以上路径前缀为 `deliverables/final-specification-set/`。反向完整差分见 [reverse.diff](reverse.diff)。B04正式13全部从旧actual→接受父→B07候选原字节保持；五读取输入是engine-overworld的资源目录、WP16目录、UI综合目录、final WP17消息正文、original WP17消息正文，全部核对实际blob／SHA256／bytes。追加其余8份B04正文／原稿也逐字节核验。三份综合目录只能按B04原局部贡献解释，整个文件不自动全批准。

两个B07目录新增28行：IU-49–59、SH-27–28、GR-45–53、BE36–37、CX39–42；旧修正仅SH-08、GR-15、GR-30–34、CX22，共8。原ID顺序与重复出现数保持，BG／DC／RM／CP完整章节原字节保持，既有BE13及正确WP31取消段落保持。六原稿必要同步的全部文本hunk和各old/new/diff哈希核验一致；作者使用文本unified格式（无Git index header、空context行省前导空格、文件间空行），独立重新构造后验证，不能仅用作者成功摘要。

## 受影响语义和正反证据

所有源路径／数值行固定于上述参考commit，完整正反输入及caller/callee定位见 [affected-interfaces-and-counterexamples.json](affected-interfaces-and-counterexamples.json)。以下只报告对B04的影响，静态预期均未执行。

| 交界与候选条款 | 独立证据及正反结果 | 对B04结论 |
| --- | --- | --- |
| WP28 §3.2/5.3、WP29 §3.4/8；IU49、SH08/27/28 | Item Utilities644–752、UI ItemStorage240–338、PokeMart477–538、BPShop332–394/446–480：专用数量窗初值1，持5只给上限；显式5售750、默认1售150；BACK0在效果前跳过。BP显示先半单价再乘量；21×3显示30，确认全价63。 | C071–73的通用数字、命名网格、非正上限和部分失败规则不变，专用窗不被误当通用数字入口。未批准WP66C全部UI。 |
| WP28 §5.3/6.2/7、WP31取消；IU54/BE13，原A045 | Item Effects918–947、Evolution84–134/195–250、Item Utilities674–694/733–752：满级合法糖果动画内BACK只取消进化成功序列，正常演出返回true后扣1；选择前取消／关配置／无目标不消费。 | 通用取消不等于效果false，领域写入不变为全局回滚。取消SE/取消消息与成功ME分支分开。音乐包装只在yield正常返回后恢复；异常不保证消费或恢复。 |
| WP28治疗/教学、WP30 §6、WP31 §5；C055–57/59/60 | Audio Play1–38/52–118/202–277、Game System60–244、Messages405–451/617–629：普通音频字符串与消息SE/ME预解析不同；缺文件与叫声时长各守原门；正常取消请求取消SE、成功才请求成功ME。 | WP15音频/资源语义保持。不得从使用true、可见属性或静态时长反推真实发声/像素。UIHelper消息与普通pbMessage控制解释保持入口差异。 |
| WP30 §6.3；GR49/50与GR30–34，原A048 | MoveRelearner19–108/150–199、GameData97–114、Validation12–29：CATERPIE1两初始招全会／最初空得到[]，首绘selected move严格nil校验失败，尚未到BACK/USE或正常EndScene；MAGIKARP1同支。 | 空领域值不等于安全空画面；前序资源、字体、世界、类型构造成功才能隔离该失败。非空且首绘成功才适用取消循环，外部预检另列。外层fade ensure不替内层统一清理。 |
| WP28 §5.4、WP30 §6.1–6.3；IU58、GR51–53、共享C003 | 两遗忘包装：Battle Scene447–455、Item Utilities630–637、Summary1232–1268/1355–1365；均单个体4旧＋1新，BACK/新槽−1、非调试HM拒。Tutor452–486/Item Utilities710–752区分TR记录。Party1258–1287/1504–1530恢复目标上限与非蛋谓词；重学150–164去重。 | 学习层重新确认与B04普通列表、命名输入分开；满槽业务提交差异不合并。目标30/max40只+10，记录重叠只2、蛋不合格。C003全根8扩展保留，B04历史仅C04，B16仍须改专业UI。 |
| WP31 §5.1、BE36/37，原A050 | Evolution22–81/99–134/152–193、PictureEx362–414/483–508：准备隐藏→首更可见白覆盖/zoom0→2秒放大/2.6秒大轮廓→成功闪白后正常色；之后取消最终还原旧图，先前白影已出现。 | 动画自身20单位/秒，不能套战前过渡总时长；有效非透明资源和正常计时是前提。C061/C062两修复原字节保持；未测素材、实际像素、Bitmap容量或宿主失败。 |
| WP28 §3.5/5.1/6.5、WP30 §4.2；IU51–55/GR45–48 | Battle Command100–137／ActionUseItem34–59/87–148、Battle item effects119–143/426–452、ExpAndMoveLearning83–191：5类缺效果默认资格真，登记消费后效果空仍清选择；1/3缺效果守卫拒。全治混乱战斗/非战斗分叉；基础经验0在消息/写入前早退，先写EV保留。 | 消息和取消未变为通用退款/回滚；数量、战斗资格与效果分开。完整治疗数值、AI/持物/战斗19贡献正确性归R-B07，不由本报告批准。 |
| WP32和B06逻辑音乐接口 | BattleAudio1–149、BattleIntro59–176；WP24正文实际／接受父／候选原字节同一blob bb181b68d143f2a8bd09ba4e447a9867ed791336、SHA256 74ae842aed64fbb8a683ab8263c69113bdf89ceb0f3384855089dcbd24f224e2、29351 bytes。 | 六逻辑请求及引子Q/0、已有R/r、末空/FromType差异、选择不清预置仍有效；正常战前包装返回才恢复/清记忆和四预置。WP32队伍/持物更动不获得额外音乐/伙伴/雷达批准。 |

## 保留、来源关系和后续门

本范围新缺陷0，未新计根因。现存跨批不一致有明确来源关系：原GIR-FD82-A048的WP66A正文181/202及综合UI目录A32（191）仍写空画面正常打开，原C003的A23/A31/A33（182/190/192）仍缺关键前提；它们原属B16，B04旧局部批准从未覆盖这些业务条款。B07域内GR50及IU59/GR52/GR53已给必要前提，不自动替B16关闭。D023的WP66C显示同步、B013的捕获／伙伴／终局／CP20等也保留原责任批；本报告没有把这些历史待修项伪报为B07新增缺陷，也不因综合目录字节保持批准其错误断言。

其余B07业务规则只读完整正式差分并检查是否扩大B04语义；未独立批准全部Nature／EV／形态映射、成长／进化家族、捕获／伙伴错配、专用UI或19项全批贡献。作者19/12映射、完整原controls／acceptance哈希、全部C003最终扩展均核对，但这项身份检查不等于业务验收。U01–10／G01–12／AX01–20、具名8杯赛名单和pokemon_metrics.txt未读、backup/gen未全文、二进制、mkxp、媒体／字体／宿主／soundfont／容量、插件／动态调用、EventScene／动态阴影／deprecated别名及实际地图demo限制全部保留。

仍需独立R-B07全批候选审查。AREG实际整合后，必须提供精确actual／tree／父对象、未过滤predecessor→actual和candidate→actual、五读取字节、B04其余8正文和B06 WP24身份，以及公共登记／历史／资格变化；本R-B04再做精确actual受影响复审。候选PASS不得跳过实际门，B04→B07串行和后续WP28/WP30反向门继续有效。父任务C接受、公共唯一写者AREG与229 OPEN／0 CLOSED保持，本报告未完成这些后续动作。交接见 [handoff.json](handoff.json)。
