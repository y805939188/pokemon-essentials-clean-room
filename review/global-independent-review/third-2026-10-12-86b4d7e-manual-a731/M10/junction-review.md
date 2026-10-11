# M10 交界审读

只读固定源码/当前正式文字，全部静态、执行0。以下结论仅签收M10列出的消费片段；其它模块完整链由root独立整合。正常、反向/失败和边界不合并；PARTIAL不会转成全链PASS。

## G3-5：给予链部分提交

- 本地状态：PARTIAL；交界owner：M05|M10|M11。
- 正常合同：持物/邮件给予先完成对应容量检查及已提交入库/清空，再进入后续选择。
- 反向/失败边界：后续取消/失败不回滚先前邮件入库和清空；交换取消保持各自先写的实际结果。
- 本轮证据：Party:926–958/§4.4，PC:58–105及Storage:1902–1934。
- 独立判断与未决：给予邮件放弃保留入包旧物/先清邮件；容量预检与取消不能合并事务。M05领域仍主责。
- 历史定位（不是旧PASS授权）：c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_junction_results/17。

## G5-2：战后进化时序

- 本地状态：PARTIAL；交界owner：M06|M07|M10。
- 正常合同：战后T1–T7及L0/K/D临时记录分别定义；扫描一次，不对新结果连锁重查。
- 反向/失败边界：取消不留下成功记录；NINCADA附加个体不继承该记录。
- 本轮证据：Evolution:84–134/195–250；WP67B§3。
- 独立判断与未决：UI成功/取消及后置提交已读，战后扫描T1–T7和临时进化记录完整生命周期消费M06/M07，未由UI扩成扫描全审。
- 历史定位（不是旧PASS授权）：c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_junction_results/29。

## G5-3：进化提交主流程

- 本地状态：SUPPORTED_STATIC；交界owner：M05|M06|M10|M11。
- 正常合同：阻止、取消、成功三路；成功按统计及身份/能力/图鉴/招式/收尾固定序列交接呈现。
- 反向/失败边界：呈现失败不自动把先前提交改成事务；兼容物种/道具身份不能净化成泛称。
- 本轮证据：Evolution:195–250；WP67B§3.2–3.3。
- 独立判断与未决：成功消息早于物种写入；后置→物种→图鉴→待学→条件页/学习。取消没有该链；后续异常不回滚先写。
- 历史定位（不是旧PASS授权）：c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_junction_results/30。

## G5-4：孵化提交

- 本地状态：SUPPORTED_STATIC；交界owner：M06|M10|M11。
- 正常合同：队伍孵化先核心写入后演出；图鉴写入及动态形态读取各有门，多蛋按队伍顺序。
- 反向/失败边界：演出动态形态读取可有提交副作用；未执行演出不意味着核心孵化未发生。
- 本轮证据：EggHatching:103–138/202–264；WP67B§4。
- 独立判断与未决：迈步核心先演出，直接孵化/仅演出分层；图鉴已写后命名拒绝/空返回不回滚，逐蛋串行。动态形态领域M04主责。
- 历史定位（不是旧PASS授权）：c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_junction_results/31。

## G6-2：扣除与不退

- 本地状态：PARTIAL；交界owner：M05|M06|M10。
- 正常合同：消耗登记/资格/效果/返回分层；道具使用过一件后再取消目标可返回0而保留效果与扣减。
- 反向/失败边界：不能由返回0推成未使用；投球登记即扣减，与普通道具消费门不同。
- 本轮证据：Bag:503–508/591–704；WP66C§4/5；ActionUseItem:34–147。
- 独立判断与未决：野外内层0可已有用物效果；战斗登记先扣、执行失败退款身份保留需同轮终局再核GR3-M07-001。
- 历史定位（不是旧PASS授权）：c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_junction_results/35。

## G7-1：交互合同主责任与消费者处置（v4 收尾）

- 本地状态：PARTIAL；交界owner：M03|M05|M10|M11。
- 正常合同：消息/选项/数量/按键由主规格定义，集合内4及外5消费者分别引用；取消负值/零/正数各有含义。
- 反向/失败边界：空数组与nil不同；源方法标识只作审计，取消不能统一为false，暂停符与本地化占位符不同。
- 本轮证据：Messages:55–205/687–859；Summary:1232–1384；UIHelper:276–338。
- 独立判断与未决：nil/空数组、取消负/零/正哨兵按入口；新GR3-M10-002数量竞争与003战斗列表恢复，各应由正式主合同承接。
- 历史定位（不是旧PASS授权）：c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_junction_results/39。

## G7-2：主导航状态分层

- 本地状态：SUPPORTED_STATIC；交界owner：M10。
- 正常合同：界面即时修改、游戏状态和持久写盘分开；可见候选排序后逐项评估，保存/退出分别处理。
- 反向/失败边界：退出前保存被拒仍可终止；子画面返回父级与回地图不混同，选项取消不恢复即时值。
- 本轮证据：Load:281–356；Options:327–359；Pause:304–321；PC:116–153；Ready:245–331。
- 独立判断与未决：选项即时内存与语言直写/保存分开；退出同意后保存被拒仍终止；子取消回父/回地图不同，PC主重0。
- 历史定位（不是旧PASS授权）：c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_junction_results/40。

## G7-3：领域守卫与 UI 消费

- 本地状态：PARTIAL；交界owner：M05|M10。
- 正常合同：PC整队入口门与界面逐目标门分别检验，容量预检先于实际提交。
- 反向/失败边界：BoxLink缩队后旧索引可部分写入再失败；空重学初绘可失败，不能统一为正常空提示。
- 本轮证据：Party:746–790/1013–1021/1425–1484；Storage:1500–1568/1902–1934。
- 独立判断与未决：C125旧来源索引不重绑保留；新GR3-M10-001持物快照取回后重复与该索引失败不同。PC整队门不等内部逐目标门。
- 历史定位（不是旧PASS授权）：c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_junction_results/41。

## G7-5：战斗命令 UI 与选择期合法性

- 本地状态：PARTIAL；交界owner：M07|M10。
- 正常合同：命令导航/选择/登记/撤销和执行资格分层；登记消耗物品的扣减时点保留。
- 反向/失败边界：NearAlly正常三席：user0/near2濒死无reserve/far4存活可初选登记4，但布局/存活不变到执行拒绝4；无非自身同侧存活才回自身。
- 本轮证据：SceneChoose全选择/取消；CommandPhase:28–140；ActionUseItem:34–147；WP67A§4/5。
- 独立判断与未决：选择/登记/执行分层；NearAlly初选远4可登记而执行拒绝；普通两药水同目标可选择，次份失败后同轮终局二次退款同根GR3-M07-001。
- 历史定位（不是旧PASS授权）：c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_junction_results/43。

## G8-1：插件/扩展机制主责任与消费者处置（v4 收尾）

- 本地状态：PARTIAL；交界owner：M01|M02|M04|M06|M10|M11|M12。
- 正常合同：插件早于编译检查；编译检查调试门不阻止发布消费预编译插件。候选物种通知与生成完成通知分开。
- 反向/失败边界：普通步进候选通知早于允许遭遇门；主动请求通知后仍可空候选退出。WP21自身形态登记不当作WP05事件消费；真实插件组合仍未知。
- 本轮证据：Pause:109–125；PC:137–152；Options:274–282；WP65§2/5/6/7。
- 独立判断与未决：UI候选注册先排序再条件、动态名与效果返回已读；插件装配/编译/事件机制归M01/M02，真实插件组合未知。
- 历史定位（不是旧PASS授权）：c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_junction_results/44。

## G9-6：保存 UI 交接 vs 存档机制

- 本地状态：SUPPORTED_STATIC；交界owner：M02|M10。
- 正常合同：保存UI可用门、确认、反馈与实际存档/迁移机制分工；普通、事件、退出前、紧急入口分别交接。
- 反向/失败边界：无效档/备份与删除双确认不统一；新字节没有继承旧批准，实际签名须绑定actual。
- 本轮证据：Save:1–24/100–128；Pause:254–271/304–321；WP65§4/WP10引用。
- 独立判断与未决：保存UI明确拒绝/失败/覆盖/退出忽略返回。M02-003 DISPUTED/OPTIONAL：存在旧档限定只绑定复制步骤，成功双提示无旧档门，现WP65可推出无旧档仍双提示；无玩家提前返回优先于尾部恢复。root认可NO_REQUIRED_REVISION方向，保留原ID与异议。
- 历史定位（不是旧PASS授权）：c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_junction_results/53。

## CHAIN-1：伙伴捕获/持物/存储

- 本地状态：PARTIAL；交界owner：M05|M06|M07|M08|M10。
- 正常合同：普通2v1、有伙伴参战、玩家满队且盒位可用，接收正常；先接收使玩家队伍移位，战斗参与记录仍持旧对象；仅一次终局持物恢复→boxed A=Y/live B空。
- 反向/失败边界：无伙伴对照保持；无需KnockOff；自然打落空物子例未证；不再追加移位玩家第二次恢复遍历。
- 本轮证据：SceneChoose:148–219；WP67A§8.3；WP20/38/42引用。
- 独立判断与未决：捕获满队选送盒UI与显示下标反查已读；伙伴真实参与的持物终局共享身份领域主责M05/M07，不据UI推全链PASS。
- 历史定位（不是旧PASS授权）：c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_chain_results/0。

## CHAIN-2：生命周期/时间/步进

- 本地状态：PARTIAL；交界owner：M02|M06|M10|M11。
- 正常合同：交换计数先于校验；寄养周期/领取生成/队伍孵化分入口；强制玩家一步通用通知两次，各周期/概率由消费者定义；单株果实量更新统计。；行走友好达128后逐可战成员独立1/2抽样，命中再消费成长/Shadow门，循环后计数归0；不采用共同概率门。
- 反向/失败边界：NPC及普通玩家不一律两次；多株不替代单株qty；核心孵化与演出动态形态读取可见提交分开。
- 本轮证据：Trading:217–243；EggHatching:212–264；WP67B§4/5。
- 独立判断与未决：交换计数先对象校验、 received最终入队在演出/进化后；孵化步/核心/演出分层。世界强制步/植物/钓鱼时间M11/M02主责。
- 历史定位（不是旧PASS授权）：c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_chain_results/1。

## CHAIN-3：道具/库存/UI

- 本地状态：PARTIAL；交界owner：M05|M06|M10|M11。
- 正常合同：有限两槽P999/997买3失败回退只恢复总量，槽分布可变997/999；邮件先取下入包后取消保留先写；BoxLink缩队后旧索引写入再局部失败；空重学初绘失败。
- 反向/失败边界：默认无限不冒充两槽向量；交换后仍持Y；失败不改成全事务回滚；BP显示与实际值同步门保留。
- 本轮证据：Mart:598–748、BP:446–525、Bag:351–458、Party:746–790/1013–1021/1425–1484、Storage:1902–1934、MoveRelearner:19–191。
- 独立判断与未决：有限槽回退只恢复总量，邮件先写不撤回，旧索引交换及空重学初绘失败沿有效控制；新持物快照GR3-M10-001和数量竞争002追加当前UI域缺口，不把全部改成事务。完整容器/领域效果M05主责。
- 历史定位（不是旧PASS授权）：c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_chain_results/2。

## CHAIN-4：设施提交/恢复/异常

- 本地状态：PARTIAL；交界owner：M07|M09|M10|M12。
- 正常合同：nil取消不覆盖原队伍；空列表显式提交false；经验快照在等级调整前、物品在调整后；正常归还等级→治疗→解除→恢复物品。；原队伍快照只开始写；进行中报名/租借显式空列表立即写报名及玩家引用并返回假，nil不提交；玩家引用另有开始/取消/结束写入，保存/重置/刷新门按WP55§2.2–2.4分列。
- 反向/失败边界：正常治疗不是HP/PP快照；正常UI空列表可达未证；异常可能阻止后层清理；文件打开前/后失败的落盘状态分开。
- 本轮证据：Party:1051–1202；WP66A§4.6。
- 独立判断与未决：多选取消nil不提交；普通CONFIRM返回有序成员，显式空数组领域提交false另路。设施开始/恢复全部状态M09主责；没把正常UI空数组可达当已证。
- 历史定位（不是旧PASS授权）：c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_chain_results/3。

## CHAIN-5：形态/Shadow/成长

- 本地状态：PARTIAL；交界owner：M04|M05|M06|M10|M11。
- 正常合同：形态写入先于交互学习，学习拒绝不回滚；ROTOM同形态且唯一目标招仍可能删到0；Shadow量表0仍Shadow，香门friendship255，储存HARDY90/LONELY130分列。；Shadow四文本已读样本字段/131量表与招式样本全集由WP23附表§3承接，U06实际启用未知；Gen5–8未读备份仍仅存在性。
- 反向/失败边界：默认普通经验消息关闭，直接helper显式消息可先提示后被阶段门拒绝；可选备份U06未证，不把G0或friendship与阶段概念混用。
- 本轮证据：Purify:361–628/1232–1280；Evolution:195–250；Summary:929–1384。
- 独立判断与未决：Shadow清除/跨级能力窗失败/清中心与命名分层；SPINDA个体位图消费者实证给root M04-001，非蛋前/背面共同后处理，species-only入口另路。
- 历史定位（不是旧PASS授权）：c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_chain_results/4。

## CHAIN-7：Arena/攻击记录/回放

- 本地状态：PARTIAL；交界owner：M07|M09|M10|M12。
- 正常合同：Arena开局复位，正常补位不调用孤立复位辅助；第3/4/5回合连续裁判，HP/技能基线与提示门保留；回放按录制攻击/随机序列消费。
- 反向/失败边界：替补辅助可进入攻击阶段及回合末；随机Roar不等于业主选择流；非必修B030联合既有合同可推出，不新增记录字段/关闭登记。
- 本轮证据：Arena:43–209；WP67A§10/现行WP56§3.3/PA-P28。
- 独立判断与未决：GR3-M10-004当前UI表两项残留，与M09正确WP56/58不抵消；M09已确认无重复ID，旧B028受限关闭保留。录制随机/属主选择全消费仍M09/M07。
- 历史定位（不是旧PASS授权）：c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_chain_results/6。

## CHAIN-8：世界显示/时序/目标几何

- 本地状态：PARTIAL；交界owner：M03|M05|M07|M10|M11。
- 正常合同：34世界场景分族保留；飞行先于消息/outdoorlight不受TIME_SHADING户外门/计时负业务值显示0；暂停初显0后全局相位，预览两个周期；选曲与播放/等待/返回清预置分工。；天气先旧图存在/异图门和类型不同门才局部0，合法连接独立后写20；同类型显式重建保持旧duration，同图不重掷，正在渐变/强度单改守卫保留。
- 反向/失败边界：零时长即时插值不取消在途任务；99998计时/动画排序各自独立。NearAlly正常三席存活远位可初选登记但执行拒绝；无存活非自身同侧才回自身。
- 本轮证据：TextWindow:421–440；AnimatedSprite:119–135；Preview/Scene animation消费者；WP16采样附表。
- 独立判断与未决：暂停初0再全局相位、Preview两周期与战斗20Hz跳帧时点区分；世界天气/地点条/行走光照M03/M11。播放器取当前帧不补跳过定时已由WP16承接，无新finding。
- 历史定位（不是旧PASS授权）：c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_chain_results/7。

## 两条新嵌套输入证据

GR3-M10-001保持完整队伍[A,B]索引不变：A持POTION、袋0，Item→Move→SPECIAL→整理队伍面板取回A物品成功（袋1/A空），退出盒子再确认B，无再次源物品资格检查，B持POTION，袋仍1。BACK对照只保留取回，未嵌套对照总量1；不能沿旧C125失效来源索引解释。

GR3-M10-003区分普通/暂停战斗消息和确认/列表：前两者推进字符，列表busy非暂停只是恢复并按计时继续。全显USE和BACK取消仍保持K45；有中间暂停则解除暂停，未当自动全文。数量竞争GR3-M10-002按共享/两商店的动作优先序，UI采样夹具可审且宿主组合未观察。

GR3-M07-001 UI可达核验限定：普通内部2v2单玩家两名可输入者，合法非蛋非Shadow伤员缺HP在1..20、正常袋2份POTION，两次Bag均选同一成员，选择阶段尚未施用，第二行动的firstAction=false不禁药水。首份先补满；第二执行复核无效退款但选择物品身份不清。仅在同轮已终局并到正常终局取消选择时再退款；下一轮重置、未终局或终局清理未达不共用此结论。源POTION资格66–72/效果333–335、ItemUse87–101、CancelChoice13–23、End503及SceneChoose列表链一起支持，不添加新编号。

## M11栖息地掩码新增交界

M11已独立提GR3-M11-001/P2候选：UI_Pokedex_Entry313–353在多格图形中按行优先位置读0/1、以宽与形状长度上取整高度，且与可见地图点集合求交/并入结果。M10直接核过此消费者，当前WP66-B§7.1仅引用WP62，未在M10找到完整计算规则；与区域地图定位只长度/同格首条门不同。由M11主责最终finding，M10不新增同根编号；本地C20保持PARTIAL。
