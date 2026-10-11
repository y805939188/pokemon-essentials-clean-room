# M09 本轮交界审查

独立任务 `/root/m09_ai_facilities_v3`；正式输入 `167296dbe9e2384627b0ed696e87aeb01f211252`，交付 `86b4d7e1d8645e75af91a215240f8786a5bb4ca8`，参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。只读静态审查；参考执行、案例执行、录像反序列化、运行观察均为 0。下面是 M09 的判断，跨模块最终裁决交独立主角色；不覆写公共登记或其它 reviewer 的异议。

## 已分配交界

| ID / 消费者 | 正常静态合同 | 反向、失败、边界及本次证据 | M09 判定 |
| --- | --- | --- | --- |
| G1-3 / M01、M12 | 设施文本名单通过显式 Trainers/Pokemon/Challenges 字段编译，挑战首非默认匹配、否则首默认。 | `021_Compiler/002_Compiler_CompilePBS.rb:951–1063` 与 `018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb:21–33`；`PBS/battle_facility_lists.txt` 全字段实读。当前默认塔+四杯对；非 single Fancy 两文件只存在、当前列表无引用。缺编译物时读取回空。 | SUPPORTED_STATIC（机制）；PARTIAL（数据全内容/实际启用）；编译物 MISSING_MATERIAL。 |
| G1-5 / M01、M06、M12 | 普通 PBS 自动发现与设施专用名单入口不同；未知属性不自动成为消费者。 | 同编译段按 schema 忽略未知键、缺实际文件置相应数组空；设置已有规则不重建。生成写文件/失败后保留问题由 M12 WP76 覆盖，M09 未执行生成。 | SUPPORTED_STATIC（设施入口）；PARTIAL（M12生成及M06遭遇部分不代签）。 |
| G2-5 / M02、M03、M11 | 普通全局随机、显式种子和录制的执行随机序列分层；回放逐项取记录值。 | `005_AI/008_AI_Utilities.rb:5`；`008_Other battle types/005_RecordedBattle.rb:129–132,188–192`。AI/Palace选招随机不进执行随机记录；记录不存种子，序列不足取空后递增，无跨实现等价保证。 | SUPPORTED_STATIC（M09）；其它播种消费者保持本模块边界。 |
| G3-3 / M05 | Factory 全候选以空训练家创建，得到有效默认拥有者记录；NPC分配/交换不转移拥有者。 | `002_Challenge_Data.rb:201–217`；`001_Challenge_BattleChallenge.rb:373–423`；`014_Pokemon/001_Pokemon.rb:1198–1204`；`005_Pokemon_Owner.rb:19–32`。默认0/空名/2/2；交换仅确认加数，取消无条件再提交R；若活动P≠R可见队伍改为R。 | SUPPORTED_STATIC；永久获得不因租借提交自动成立。 |
| G3-4 / M05、M06、M11 | 租借创建/交换自身没有永久接收的 owned 登记；战斗入场看到与形态登记是不同写入。 | Factory UI/创建全行为与 `001_Battle/005_Battle_ActionSwitching.rb:287–296`、`014_Pokemon/001_Pokemon.rb:159–178`。回放副本 BURMY 形态提交可写实时图鉴，不能称副本隔离。其它九获得入口及整体清理由对应模块核。 | SUPPORTED_STATIC（租借/回放本地）；PARTIAL（其它获得/清理）。 |
| G3-6 / M04、M05、M06 | Factory 默认拥有者四字段是真实记录；不以包装对象是否存在推外来资格。 | 同 G3-3 创建与Owner字段；普通设施对手传NPC、Factory全候选空训练家；后续只交换引用。玩家ID/宿主语言与界面语言在其它模块有不同角色。 | SUPPORTED_STATIC（M09）；外来比较全域不代签。 |
| G4-1 / M09 | 单场先治疗玩家、保存两侧完整EXP、调整返后才记持物；正常按届时位置恢复。 | `004_Challenge_LevelAdjustment.rb:28–79`、`004_Challenge_Battles.rb:40–97`；WP54 §4、QC-Q25/Q45/Q46。同级保留级内经验；重排会错配；旧EXP缺跳、旧物缺置空；异常部分写，无统一回滚。 | SUPPORTED_STATIC。 |
| G4-2 / M09 | 原队伍仅开始按引用快照；活动报名/租借、开始、取消、结束有不同玩家队伍写入门。 | `001_Challenge_BattleChallenge.rb:200–229,258–318` 与 `002_Challenge_Data.rb:38–49`；WP55 §2.2–2.4、WS-W28/W29/W30/W35。[]写并包装false，nil不提交并返nil；开始/暂停/继续决定0仍保存；结束先无条件恢复、非活动止于此。 | SUPPORTED_STATIC；默认UI确认空列表 NOT_REVIEWED（运行），不作可达宣称。 |
| G4-3 / M04、M06、M07 | 设施单场正常恢复逐成员治疗、解除Mega/Primal、按位置复持物；裸回放不调用设施包装。 | `004_Challenge_Battles.rb:69–88,111–128`；`005_RecordedBattle.rb:164–179`；WP54 §4.2、WP55 §3、WP58 §6.5。中止不走正常终局；本包装治疗不是旧HP/PP快照恢复。普通换下/裸终局/世界返回解除分工由其它模块。 | SUPPORTED_STATIC（设施/回放）；PARTIAL（其它入口）。 |
| G4-5 / M07 | 派出记录按侧内席位，终局读取按队伍下标；回放保留来源口径异常。 | `005_Battle_ActionSwitching.rb:287–296`；`002_Battle_StartAndEnd.rb:506–509`；`001_FormHandlers.rb:178–200`；WP58 §6.2、RC-W22/W22b。位0首发传真→Cave形1；位1仅换入席0终局读假→保持形0；不能用实际参战代替标志。 | SUPPORTED_STATIC；未来是否修复口径由用户决定，审查不提出框架实现。 |
| G6-3 / M05、M06、M07、M08 | 设施记录当前持物身份并在正常善后按届时队伍位置恢复；普通终局另有初始物记录消费者。 | `004_Challenge_Battles.rb:53–82`、`002_Battle_StartAndEnd.rb:506–509`；WP54/55/58 当前合同实读。伙伴捕获送盒的A得Y/B空主夹具属于非设施实际接收链，本轮不从位置恢复推第二次全队恢复。 | SUPPORTED_STATIC（M09）；PARTIAL（捕获/伙伴消费者由M05–08对接，保留已有限定）。 |
| CHAIN-4 / M07、M10、M12 | 报名提交→会话开始快照→单场EXP/持物处理→正常恢复→显式计数/结束，各层时点明确。 | 上述 G4-1/G4-2 源段；`005_UI_BattleSwap.rb:168–246`；WP54/55/57与QC/WS/FC全测试设计逐行核。UI nil取消与[]工具边界不同；Factory取消可再次提交；异常不保证外层地图/资源清理。 | SUPPORTED_STATIC（M09链）；事件实际可达/宿主/写文件前后状态 PARTIAL/MISSING_MATERIAL，M10/M12独立判断保留。 |
| CHAIN-7 / M07、M10、M12 | Arena首发复位后第3/4/5轮连续裁判，记录按原动作/执行随机/询问替补分流，回放按其实际消费者重取。 | `004_BattleArenaBattle.rb:58–94,111–200`；全Scripts孤立复位只定义；`005_RecordedBattle.rb:74–132,182–222`；替补辅助 `005_Battle_ActionSwitching.rb:132–217,365–373`；真实控制 `013_MoveEffects_SwitchingActing.rb:23–145`；物品/能力的具名退出段。WP56 §3、PA-P28、WP58 §5.2、RC-W16/W24/W25/W26均核。Roar/REDCARD只随机；EJECTPACK首命令前先耗再询问、负值亦记不替换；EOR退出留后补位。 | SUPPORTED_STATIC（M09本地）；WP67-A现行残留见GR3-M10-004，跨面未闭合；真实录制回放/演出未运行。B030有效非必修裁决保持。 |

路径未展开的 Battle Frontier、AI 和 Other battle types 源路径均相对 `Data/Scripts/`；精确完整路径与 Git blob 在 `file-coverage.tsv`。未将搜索次数、登记数或旧签名当作上表语义证据。

## 新增交界

- **Natural Gift 实际续击与预测（GR3-M08-001）**：本轮实读 AI `004_AI_MoveEffects_MoveAttributes.rb:1423–1435`、粗伤 `011_AIMove.rb:81–92,223–230` 与真实 `008_MoveEffects_MoveAttributes.rb:1338–1379`。PredictMoveFailure 开且当时无果会先得到整失败候选20；当时持有效ORAN则预测基底来自该果，亲子爱只近似乘P。AI没有逐首击JABO反伤→ORAN自耗→第二击空持物查询的模拟。M08的新实际失败证据不改变这份预测合同，也不把参考异常当未来默认实现义务。M08最小主夹具及其实际多击后段由该 reviewer 裁决；M09明确预测/实际的边界，未新增同根ID。
- **WP76模拟消费者**：本轮实读 `004_ChallengeGenerator_BattleSim.rb:377–430`，真实1%分支以双方AI接管、非内部战斗开战，正常只治/复持物；它不等设施包装的完整经验恢复、Mega/Primal解除与录像提升。近似99%评分不证明AI执行或回放。M12通知累计场次差的 `GR3-M12-002`，保持M12归属和独立裁决，M09不覆盖。
- **WP51录像责任定位（GR3-M09-001）**：P3 OPTIONAL；WP51 §7 L155将录像定位写WP57/76，实际记录主合同WP58，WP57是Factory。仅文档责任指向，现有机制仍受支持。

- **Arena呈现消费者异议（GR3-M10-004）**：M10登记P2新证据，随后M09独立补读冻结WP67-A§10 L253，确见“成员更替时先显示对阵窗/每3回合裁判”。实际源与WP56/58/PA-P28是首发提示、正常替补不复位、3/4/5连续裁判。这项当前消费者矛盾保留M10归属，不重复计新ID、不改旧B028关闭；本地SUPPORTED与历史FINAL1复用均不覆盖它。跨模块最终裁决交主角色。

## B030有限复核

完整有效限定、原反例、最低修订建议及确定复核已读；其最低修订在有效裁决下是可选澄清，不能自动成为必修。当前 WP54准备顺序、WP58穷举快照/恢复字段和WP45默认合同联合可推出：准备Misty使首轮Yawn计数0、回放缺地形可到2；录制默认Rain经晴5轮到期恢复Rain、回放无默认天气回None；准备后的背景/环境/时段并非裸构造默认。没有发现与联合合同相反的新保证，本轮维持 `NOT_REQUIRED_AS_REPORTED`，不增记录字段、不重开旧ID、不执行这些案例。
