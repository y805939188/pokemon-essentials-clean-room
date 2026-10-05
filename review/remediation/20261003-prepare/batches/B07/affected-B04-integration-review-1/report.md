# B07 实际整合的独立受影响 R-B04 复审

结论：**PASS_SCOPED**。独立检查精确实际 `adca83d63d18c94429cdb52aef9eaf7b8aa00189` 对已接受 B04 WP15–17 的资源、音频、视觉、文本与输入交界、五读取合同、公共登记及回归，本范围新增必修缺陷0。B04历史35局部贡献／23主责按原限定范围保持；不替代R-B07完整19贡献／12主责实际复审，不执行父任务C接受、不修改登记、不关闭ID。

实际tree `392c60655eff833399e796e081b18ae344cdaa82`，唯一父payload `94aa281d6ff10d5b3e80c7df066d0ccd6d0f0c6f`。管理前驱为 `259a1c158f317c5e32830e04838a76aa82f4d20a`，正式内容基线为 `219cc3c182750155e9dbf2cb619f420b3922de27`，候选为 `a22df6b1d9465b68e45558c57bc69c61939baeaf`。以前的受影响候选报告 `3e88d42b8d9313e1adbbc8944e54faa1b45e71a0` 只是固定历史输入，未自动套用。本轮报告独立分支 `remediation/20261003-prepare/review-B07-affected-B04-integration-1`；包含本目录的精确报告SHA由普通push及远端ref／fetch对象回读后外部交付，避免自引用。[身份](input-identities.json)、[交接](handoff.json)。

读取根AGENTS.md、固定计划B04/B07条款和实际integration-stage-1冻结／差分／下游合同；适用目录无新增局部AGENTS或本地SKILL。输出限用户具名仓库新目录，未调用Library／Pages。请求gpt-6.1-sol／Ultra／Standard(default)，实际模型、推理、服务无可信回显，均 **UNVERIFIED**；继承方案A，无新确认／配置认证门、不主动降档或加速、未派生子任务。保留259a的显式xhigh更正及其来源，历史Max收据按时点保留；[配置收据](configuration-receipt.json)。

## 独立证据与完整差分

原全局对象固定于 `93e10babe0b9c9ef8b3f5277754541b447beeeb4` 的 findings.json，计划／finding-acceptance固定于 `41fffb540c6483f5296ea0d33b789b75180d27ed`。原findings属于独立固定提交，未在actual树内；不把不存在误报成删除，也不使用漂移分支替代原资格。完整原根、current_qualifications、effective_case_constraints、root_adjudications及全部extensions最终裁决按固定对象优先；完整53项B04／B07联合控制绑定与C003全部8扩展见 [fixed-control-bindings.json](fixed-control-bindings.json)。资格身份核对不等于全批业务批准。

逐项独立核原问题与正反前提、actual完整范围、正文／来源／公共和依赖，再冻结 [首判断](first-judgment.json)，随后比对A-REG详细保存断言。[773自有文档检查](independent-validation.json)和另行 [502项报告一致性核验](report-validation.json)全部通过；A-REG1571项成功记录只作比较，未据总数作语义证据、未运行作者／历史审者verifier；[对照](A-REG-comparison.json)。自己的脚本只操作Git／SHA／JSON／文本，不执行参考或静态行为向量。

| 无过滤差分 | 路径数／bytes | SHA256 |
| --- | --- | --- |
| [管理前驱→actual](upstream-to-actual.diff) | 80／11571952 | 3e581bad2503a65bde0cfb4697fea82c292b6921a3ebc8a8f7e243bb43449e49 |
| [候选→actual](candidate-to-actual.diff) | 59／11079157 | 5ef3e314b6ea099b6f83a8b1291ceb315e9595faf898b6c66673331ca5c67c25 |

管理前驱→actual80＝14正式修改＋10公共修改＋11作者证据新增＋32候选报告新增＋13整合冻结新增。实际末提交只有两完整payload patch和diff-and-freeze.json三新增，未再动正式／公共／历史。两原生merge父序／tree、payload父／tree及冻结patch均逐对象复算；据此核结果与图关系，不从Git结果反推过去冲突处理或原稿准备历史。候选→actual没有正式改动，但多出的公共／依赖／冻结与259a四份B04管理更正均独立核查。

57导入来源（14正式＋11作者＋两候选报告32）逐字节等于原候选／报告对象。完整14 [formal.diff](formal.diff) 等于同一独立审者已完整读取的候选正式差分；本轮重新核actual身份、重读关键actual正文与源正反链，另外检查新公共全文及冻结注册／合同结构。完整差分含大量原对象重复存证：逐路径／hunk和字节核验不冒充对未受影响历史业务的重新全文语义审查。[范围清单](diff-scope-manifest.json)、[公共完整差分](public.diff)、[WP28/WP30反向差分](reverse.diff)。

只读参考由本审者同容器R1独立准备于 `/tmp/rb04-reference`，本轮核真实commit/type、HEAD `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree `7589c800b61ba13a13040ed0d686979b80a84fd0`、正确origin和干净状态。本轮新读26路径／45范围／2428去重行；旧候选阅读未计入新读。精确已读／未读补集、源hash见 [source-reading-log.json](source-reading-log.json)。参考只读，不跟踪进主Git、不改ignore、不push参考；游戏／Ruby／编译／转换／生成／反序列化／媒体／模拟／行为向量、运行观察和已证demo链全部0。

## 实际边界与回归

B04十三正式文件（8净化／目录＋5必要原稿）从已接受actual9e2d→219cc→259a→B07候选→本actual全部原字节。五个读取输入为资源／音频综合目录、WP16目录、UI综合目录、final WP17消息正文及original WP17消息正文；另八份B04正文／原稿也核blob／SHA256／bytes。综合目录只按B04局部贡献解释，不批准整个混合文件。B06 WP24原字节，blob `bb181b68d143f2a8bd09ba4e447a9867ed791336`／SHA256 `74ae842aed64fbb8a683ab8263c69113bdf89ceb0f3384855089dcbd24f224e2`／29351 bytes。

实际WP28 blob `bb7c344cfbb24b8f8eb3e8ed8bfea0be6e426580`／SHA256 `63d6b9d244b1700f88e311edae37306aad9831358256c1c8ed60f63a11a5737a`／39277 bytes，WP30 blob `ea4ebda45c4827d31a4d0af9bcf4332313b64104`／SHA256 `97145b9f2bb6c5109f011c61514455558ac4bf62254a701258facd786f042e38`／28837 bytes，均精确候选字节。全部8交界的正反输入、固定源数值行及限定结论见 [affected-boundaries.json](affected-boundaries.json)；以下静态结果均未执行。

| 实际条款／场景 | 独立正反核查及对B04的影响 |
| --- | --- |
| WP28数量／WP29显示；SH08/27/28 | 专用数量初值1，持5只给上限；显式5／默认1分开。取消0在效果前；BP21×3先半价再乘，显示30／确认实扣63。WP17通用数字取消值不夹限、有符号确认、命名网格和非正上限失败不改；C071–73和兼容字符（含精确空格、ΡΚ/ΠΜ身份及同轮优先序）原字节，无替换／归一化。D023专业UI仍待B16。 |
| WP28满级糖果／WP31取消；IU54/BE13 | 正常演出中BACK取消成功序列，物种不改、取消统计+1，效果正常返回true后消费1；选择阶段取消、配置关或无目标不消费。fade外层ensure只覆盖自身淡入／viewport，不保证内层领域／资源事务；音乐恢复赋位置／resume在yield正常返回后，异常不保证恢复或消费。 |
| WP28治疗／教学、WP30消息 | 普通音频字符串参数覆盖100/100，消息SE/ME预解析对象不同；取消请求取消SE，成功才成功ME。UIHelper直接text/确认与完整消息控制解释有入口差异。请求、逻辑登记、可见属性不证明真实发声／像素，C055–57/59–60、富文本与消息四态保持。 |
| WP30空重学；GR50/GR30–34 | CaterpieL1两初招已会、最初空→候选[]；前序构造成功时首绘strict nil校验先失败，尚未BACK/USE或EndScene。合法非空且首绘成功才适用取消循环；外部拦空不入失败。既有WP66A/A32相反断言仍留B16，不自动反向批准。 |
| WP28教学／恢复及WP30学习；IU58/59、GR51–53/C003 | 两遗忘包装为单个体4旧＋1新，BACK/第5槽−1、非调试HM拒；通用旧PP保留与战斗同步分开。TR背包包装记最初招／统计，队伍直接使用不记。HP30/max40只+10但来源仍50→26；候选身份重叠只2，蛋不满足非蛋且HP>0。C003根和8扩展未关闭，B04只承接历史C04局部。 |
| WP31白影；BE36/37 | 准备隐藏→首更白覆盖alpha255／zoom0→约2秒开始放大／2.6秒大白轮廓→成功闪白后正常色；之后取消最终还原旧图，不抹除已出现的白影。本动画20单位/秒，非通用战前过渡时钟；有效非透明素材与正常计时为前提，C061/C062旧修复保持。 |
| WP28战斗消费／WP30经验消息；IU51–55/GR45–48 | 5类缺效果可默认资格真、登记消费、执行空后清选择，1/3登记前有存在守卫。战斗混乱和非战斗NONE有不同治疗资格；基础经验0在消息／写入前早退，已有EV不回滚。未把消息取消或效果空推广为统一退款，完整数值业务归R-B07。 |
| B06逻辑请求／引子记忆、以后消费者 | 六逻辑请求、普通数组末空与FromType空差异、选曲不清预置保持；无记忆且待播Q/计时存在才保存Q/0，已有R/r不覆盖。正常战前包装返回才恢复／清记忆和四预置；WP32队伍／持物不变成音乐快照或伙伴批准。后续WP28/WP30或共享目录改动仍须重冻结并受影响复审。 |

B07十四正式＝8最终／目录＋6具名错误原稿同步，没有新增正式delta。两目录169→191、125→131；新增28未执行静态行（IU49–59、SH27–28、GR45–53、BE36–37、CX39–42），旧只SH08、GR15、GR30–34、CX22共8修前提。旧ID次序／重复次数及BG/DC、RM/CP整节、BE13保持。六原稿old/new/diff与整份文本patch重新复算；“先备差异再写入”仅作者自述，不从最终tree/hash追认时序。其余B07领域规则不因身份相同获得本审者全批批准。

## 公共、历史及后续门

十个公共文件的状态仍为两actual待审；两TSV旧114行含表头按前缀原字节保留，新19候选行／12主责均OPEN、actual未审、父C未做、下游BLOCKED。其locator／静态行／精确文件身份／剩余责任与原controls及固定候选报告匹配；133公共记录不是133已接受贡献。旧六批114已接受／105触及ID、75主责，具体74满足／1缺消费／0不足、严格71／4的历史数据原字节。A024不提前升级，A017/B21、A034/B08、WP80-B02-R02/B21保留；[公共／依赖审计](public-and-dependency-audit.json)。

本范围新根因0。现存B16的A048（WP66A181/202及UI A32）空重学、C003 A23/A31/A33前提、D023 BP显示同步，以及B013其他责任／CP20属于固定原问题与责任，不伪报为B07新缺陷、不以B04局部通过替其关闭；[new-findings.json](new-findings.json)。35逐ID实际保持与原范围见 [B04-conclusion-dispositions.json](B04-conclusion-dispositions.json)，未对无影响来源族重新全审。

B08暂定79读／8写／17贡献／9主责逐路径对固定计划与actual哈希；B07改变它3个计划读者，未来B08反向影响B07五读取者，整文件目录锁保留。WP34正文只读，B07六原稿许可不继承；91对并行材料只为固定元数据有界探查，不证明caller／数据／配置／动态语义独立，任务／并行写许可均0。必须先有同一actual的独立R-B07全批报告与本报告两PASS，再由父任务C串行接受，并在精确接受后继重新冻结79输入；本报告不执行或提前赋予这些后续批准。

U01–10/G01–12/AX01–20、具名未读8杯赛名单／pokemon_metrics.txt、backup/gen未全文、二进制、媒体字体／mkxp／soundfont／容量／宿主、插件／动态调用、EventScene／动态阴影／deprecated别名及真实地图demo限制全部保留。无配置认证门；无本轮报告提交阻塞。只新增本独立报告目录，未改正式产物、公共登记或历史，229 OPEN／0 CLOSED保持。
