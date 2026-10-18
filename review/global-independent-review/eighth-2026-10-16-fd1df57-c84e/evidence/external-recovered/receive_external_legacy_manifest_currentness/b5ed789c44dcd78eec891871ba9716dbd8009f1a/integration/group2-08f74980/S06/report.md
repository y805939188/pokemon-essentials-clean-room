# S06 旧清单有限接收报告

结论：INCOMPLETE。主责 LM-E083, LM-E084, LM-E085, LM-E086, LM-E087, LM-E088 的全部原文和完成元数据已读，6 个事件／42 个完整目的段／66 个物理行／30,434 字节正文均已完成版本用途判定；尚不能签全部当前源—规格—消费者接合。新增 required 0，不作全组 NO_REQUIRED_UPDATE 或全局 PASS。UPDATE_NOT_STARTED。

实际审者 01a1448d-facd-707d-b7b9-bd92fb685010，不同于原作者 01a143c7-a558-738e-9580-11a8f12d903f 和父接收者 01a1447a-0548-77cb-b3bc-af8857847031；未 spawn。执行分支 codex/r8-legacy-reception-group-2-20261016。合同 2d44dafe215842de6355f46de7d4d273d8b4c264；原目标 93d7df7f66adcaa25811fd6ff09352b754577af0，tree dd8105c747b6f66663d9f63254a686594791cae8；原任务 tree e4e557611f94473568b69b7f1a6608896f700128。B8 fd1df570cad987dc3852a3b958f03916e317f7fe、R 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b 保持冻结。

共同前提、实际阅读片段的固定 path/blob/bytes/SHA/行区间、逐事实 producer/consumer 和开放清单只保存一次：[共同证据](evidence/common-review.json)。33 个旧输入复用精确缓存且与目标 C 对象逐字节核对，共 3,736,917 字节；恢复、哈希和视图生成均不算实读。每个原段的字节身份由冻结同名 complete.json 精确引用，[原文阅读视图](evidence/manifest-full.txt) 保留全部原始语义，包括摘要、详细版、错误和纠正。

历史阶段批准、ReviewPending、WAIT、旧表数量与文件hash均保留其原时点。当前实施断言由B8主文与固定R承担；本组没有改写manifest、正式规格或原作者文件。clean-document-revision已全文读取；技能明确不用于review报告/审计，因此这里保留完整修订链。模型、effort、tier、speed、Fast实际权威配置逐项UNVERIFIED；只记录真实线程身份。

## 逐事件判断

### LM-E083

GR-004分别处理移动者自身through和被碰撞玩家through，边界与地图层没有因此删除。GR-005事件是否更新沿用上次成功update的许可，更新中先重算再清理；普通菜单抑制的是地图调用边界，不能推广为所有公开事件入口。GR-006大网格奇数修正写只读参数时先失败，种子消费、地图改写尚未到达。

旧错误与后继：保留旧Reviewed与新ReviewPending两个阶段，不把局部复审当全局关闭；LM-E087补普通移动与直接跳跃的入口。后继E129/E156不在本组签收。

最强 NO_REQUIRED / 已有覆盖：B8 WP12已分五层写清两个through对象与边界；WP13保留缓存许可；WP14已有构造失败前缀。旧阶段语句没有要求重写manifest。缺少外域完整接合不能反向推导新增必修。

已逐事实核对的接口：I-MOVE, I-EVENT, I-DUNGEON；每项具体源/当前条款/完整实际读片及正常、取消、失败前缀见 interfaces.json 指向的共同证据。原段：LM-L1961, LM-L3452, LM-L3453, LM-L3454, LM-L3455, LM-L3456, LM-L3457。

仍需接合：G-WORLD, G-SUCCESSORS。本事件原文/元数据/版本用途已全读全判；整事件当前接口状态保持 INCOMPLETE。

### LM-E084

GR-007的目标BGS自动播放且名字不同分支实际调用BGM淡出，影响BGM登记而非BGS。GR-008初始招式记录先清空后按当前招式顺序复制，保留重复；单独添加只阻止新增重复。GR-009训练家构造取宿主两字符映射，ja1/en2/fr3/it4/de5/es7/ko8/其它2；UI消息索引不是该编号。

旧错误与后继：本事件仍留007/009残余，必须连读E085而不能把v1长段当最终规则。Owner由训练家复制当时字段，非追读宿主。

最强 NO_REQUIRED / 已有覆盖：当前WP15/WP20/WP24已分别承担规则，普通同名音频、空/重复招式和已改写语言字段都由现条款区分；宿主实际音频/语言未运行不等于应改规则。

已逐事实核对的接口：I-AUDIO, I-FIRSTMOVES, I-LANGUAGE；每项具体源/当前条款/完整实际读片及正常、取消、失败前缀见 interfaces.json 指向的共同证据。原段：LM-L1963, LM-L3461, LM-L3462, LM-L3463, LM-L3464, LM-L3465, LM-L3466。

仍需接合：G-WORLD, G-EXECUTION, G-SUCCESSORS。本事件原文/元数据/版本用途已全读全判；整事件当前接口状态保持 INCOMPLETE。

### LM-E085

007需同时满足播放登记存在、目标通道允许自动播放和名称差异；BGM/BGS判断独立，不是互斥选择。009区分Owner直接参数、new_from_trainer复制当前语言、new_foreign默认2以及后续显式setter。

旧错误与后继：这是对E084残余REQUEST_CHANGES的限定，不删除v1失败记录。旧owner语言身份与UI语言切换的来源/时刻始终分列。

最强 NO_REQUIRED / 已有覆盖：当前WP24§3.1/3.4和完整Owner定义支持分列；WP15与Scene_Map/Game_System的完整有关方法支持错误通道的实际前缀。不能因为未来希望修参考而制造本轮规格整改。

已逐事实核对的接口：I-AUDIO, I-LANGUAGE；每项具体源/当前条款/完整实际读片及正常、取消、失败前缀见 interfaces.json 指向的共同证据。原段：LM-L1965, LM-L3470, LM-L3471, LM-L3472, LM-L3473, LM-L3474。

仍需接合：G-EXECUTION, G-SUCCESSORS。本事件原文/元数据/版本用途已全读全判；整事件当前接口状态保持 INCOMPLETE。

### LM-E086

GR-010按物种生成蛋时构造对象尚非蛋，form重查（含0）可先登记已见/形态，之后才设置蛋状态；现成对象及满队早退不等价。GR-011普通移动先查临时遭遇标记，通行后提交前再查、结尾清；直接主动开战包装不是这个标记的写入者。GR-012 DAMP下CHERI每阶段13500秒、每小时整数干燥7；15小时例到成熟、含最后扣水到-5且惩罚0、产量5。

旧错误与后继：E087进一步区别直接jump和普通移动内岩架跳跃；旧berry update/yield不能被读成已采摘统计。

最强 NO_REQUIRED / 已有覆盖：B8 WP26原长段、WP12/WP36、WP60已经给出这些前缀与整数时刻。采摘统计只在容量/确认成功路径；现有条款覆盖的界面无新增必修证据。

已逐事实核对的接口：I-EGG, I-MOVE, I-BERRY；每项具体源/当前条款/完整实际读片及正常、取消、失败前缀见 interfaces.json 指向的共同证据。原段：LM-L1967, LM-L3478, LM-L3479, LM-L3480, LM-L3481, LM-L3482, LM-L3483。

仍需接合：G-CRE-D, G-WORLD, G-SUCCESSORS。本事件原文/元数据/版本用途已全读全判；整事件当前接口状态保持 INCOMPLETE。

### LM-E087

直接jump不经过普通move_generic的遭遇标记两道门；普通移动触发岩架跳跃仍在外层门内。BerryPlantData.update/berry_yield只是推进/查询；pbPickBerry先展示/确认/检查背包，成功加入后才计采摘统计并重置事件。

旧错误与后继：本轮是对E086泛化的收口，不能把直接跳跃例外扩成所有移动都绕门，也不能把读产量视为成功拾取。

最强 NO_REQUIRED / 已有覆盖：WP12、WP60现条款和已完整有关函数相合。取消、容量不足及单纯yield查询分别是正常反证，均不能产生采摘成功统计。

已逐事实核对的接口：I-MOVE, I-BERRY；每项具体源/当前条款/完整实际读片及正常、取消、失败前缀见 interfaces.json 指向的共同证据。原段：LM-L1969, LM-L3487, LM-L3488, LM-L3489, LM-L3490, LM-L3491, LM-L3492。

仍需接合：G-WORLD, G-SUCCESSORS。本事件原文/元数据/版本用途已全读全判；整事件当前接口状态保持 INCOMPLETE。

### LM-E088

GR-013写参战标记用侧与侧内场上位置，终局却按队伍下标读，不保证个体身份。GR-014 Fling命中后INNARDSOUT可使使用者扣血触发ORAN消耗，后继取当时空持物在berry查询失败，既有伤害/回血/消费前缀保留。GR-015旧会心分母16/8/4/3/2；负索引旧分支取2、新分支钳1；rough AI阶段≤2仍用其会心近似，Focus评分旧115/新60不能当算法已变。GR-016设施EV按510除以有效分配数整数分配，2项255、3项170。

旧错误与后继：E089补BURMY别名并修设施4项各127、总508、余2不分配；原E07病毒/E08调试/E09中止ID不能被后补形态记录覆写。

最强 NO_REQUIRED / 已有覆盖：WP42已明确两端索引不一致；WP47B保留当前物品和异常前缀；WP52A/B写明世代/AI口径；WP19已有设施不套252钳制。全称身份一致或事务回滚都不是现主合同。

已逐事实核对的接口：I-USED, I-FLING, I-CRIT, I-FACILITY；每项具体源/当前条款/完整实际读片及正常、取消、失败前缀见 interfaces.json 指向的共同证据。原段：LM-L1971, LM-L3496, LM-L3497, LM-L3498, LM-L3499, LM-L3500, LM-L3501, LM-L3502。

仍需接合：G-BATTLE, G-FACILITY, G-SUCCESSORS。本事件原文/元数据/版本用途已全读全判；整事件当前接口状态保持 INCOMPLETE。

## 精确剩余

- G-BATTLE（READABLE_NOT_FULLY_RECEIVED）：MOVE/ABILITY-ITEM/AI当前贡献的完整资格；实际会心完整战斗计算及AI所有必要外域消费者；Fling全部物品可用/活动门与回调调度定义；伙伴参与集合和接收左移后的完整身份链。已做到：完整pbUseMove/pbProcessMoveHit及相关Fling/ORAN/INNARDSOUT和粗略AI定义已读。后续：按本组明确事实补全必要定义，不将未全读提供者记为本审FULL_READ
- G-CRE-D（FROZEN_PROVIDER_CONTRIBUTION_NOT_RECEIVED）：CRE-D在固定carrier30cfed0996003b6ebf4b5c51cc04f31ca9255440中只有readset、没有可转授的完整贡献接收。已做到：提供者对象完整字段及readset路由已读，直接源事实按已列范围补读。后续：由父取得实际CRE-D有限贡献或自行完整必要接合；不虚造提供者FULL_READ
- G-EXECUTION（NOT_EXECUTED_BOUNDARY）：参考游戏/独立数值模型/宿主/原生音频输入/真实媒体/存档回放/Demo可达性均执行0。已做到：静态定义与数学表达已读；未声称真实观察。后续：若根目标需要运行证明，另由相应执行范围处理；本review不运行旧脚本/游戏
- G-FACILITY（READABLE_NOT_FULLY_RECEIVED）：FACILITY当前贡献完整资格；设施模板有效统计项/数据与实际比赛入口及后继计算消费者。已做到：createPokemon整数分配与B8 WP19相关段直接核对。后续：父接收FACILITY有限接口后再签整事件全部当前接合
- G-SUCCESSORS（OTHER_SHARD_DEPENDENCY_NOT_ADOPTED）：LM-E129；LM-E156；LM-E158；LM-E162；LM-E164；LM-E165；LM-E166；LM-E167；LM-E168。已做到：本组内各后继E083–108已全文实读；组外仅准确路由及资格读取。后续：父接相应主责shard正文和其输出，不重复派本组身份/正文；本组不采用组外批准结论
- G-WORLD（READABLE_NOT_FULLY_RECEIVED）：CORE/WORLD/WORLD-INTERPRETER/WORLD-RESOURCES固定提供者完整贡献；地图层通行producer及临时地图查询创建者；背包/地图/渲染对berry结果的完整消费者。已做到：本组有关R函数和B8条款已逐事实接合；不能从这些片段签整个外域。后续：父接收者接合相应primary完整源/条款/回调资格；不要求重复本组原文

旧catalog的E-V2-WP11声明166–194，但实际EOF190；不存在的4行不授阅读信用，166–190已完整补读。登记QUAL-G2-001供S23资格接合，未立规格required。

## 覆盖与执行资格

读取255行的组总数不等于255个新事实；本shard只按本分母计数。逐物理行已读、逐内容段用途、逐事件接收与完整当前接口接收分别记账。当前六篇主文的全文实读也不自动授予所有外域producer贡献或向量表接收。可得未读对象在上方具名；旧输入没有物料遗失。

全部业务、参考、独立数值模型、宿主、原生媒体、真实存档回放和Demo可达性执行均为0／NOT_EXECUTED。未运行任何恢复的旧脚本或游戏。源片段只用于阅读与身份，报告不复制Ruby实现。root的canonical和task-final签字仍独占。

交付包含 frozen-denominator.json、reading-ledger.json、reception-ledger.json、interfaces.json、proposal-counters.json、此报告及必要证据。后继发布回执在S06绑定实际core commit/tree及仅自身增量的远端完整读回；传输成功不改变这里的INCOMPLETE资格。

UPDATE_NOT_STARTED
