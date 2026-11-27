# 跨功能流程的状态与失败顺序

以下八条是参考行为的静态推导。每条依赖所列前提与领域规格。独立实现的兼容模式和修正规则单独适用。

## CHAIN-1 伙伴捕获/持物/存储

普通2v1、有伙伴参战、玩家满队且盒位可用，接收正常；先接收使玩家队伍移位，战斗参与记录仍持旧对象；仅一次终局持物恢复→boxed A=Y/live B空。

无伙伴对照保持；无需KnockOff；自然打落空物子例未证；不再追加移位玩家第二次恢复遍历。

相关规格　[player trainers partners](../spec/creatures/player-trainers-partners.md)、[item use and training](../spec/creatures/item-use-and-training.md)、[capture and receiving](../spec/creatures/capture-and-receiving.md)、[battle context and participants](../spec/battle/battle-context-and-participants.md)、[held item effect coverage](../spec/battle/held-item-effect-coverage.md)、[held item triggers and consumption](../spec/battle/held-item-triggers-and-consumption.md)、[party and summary ui](../spec/ui/party-and-summary-ui.md)、[storage and pokedex ui](../spec/ui/storage-and-pokedex-ui.md)、[bag item storage and shop ui](../spec/ui/bag-item-storage-and-shop-ui.md)

## CHAIN-2 生命周期/时间/步进

交换计数先于校验；寄养周期/领取生成/队伍孵化分入口；强制玩家一步通用通知两次，各周期/概率由消费者定义；单株果实量更新统计。行走友好达128后逐可战成员独立1/2抽样，命中再消费成长/Shadow门，循环后计数归0；不采用共同概率门。

NPC及普通玩家不一律两次；多株不替代单株qty；核心孵化与演出动态形态读取可见提交分开。

相关规格　[stats directory](../spec/core/stats-directory.md)、[time random steps stats](../spec/core/time-random-steps-stats.md)、[growth learning and friendship](../spec/creatures/growth-learning-and-friendship.md)、[eggs and hatching](../spec/creatures/eggs-and-hatching.md)、[wild encounters and modifiers](../spec/world/wild-encounters-and-modifiers.md)、[world time weather field moves](../spec/world/world-time-weather-field-moves.md)、[fishing](../spec/world/fishing.md)、[berry plants](../spec/world/berry-plants.md)、[field passive effects and blackout](../spec/world/field-passive-effects-and-blackout.md)、[battle interaction and presentation](../spec/ui/battle-interaction-and-presentation.md)、[lifecycle presentations and history](../spec/ui/lifecycle-presentations-and-history.md)

## CHAIN-3 道具/库存/UI

有限两槽P999/997买3失败回退只恢复总量，槽分布可变997/999；邮件先取下入包后取消保留先写；BoxLink缩队后旧索引写入再局部失败；空重学初绘失败。

默认无限不冒充两槽向量；交换后仍持Y；失败不改成全事务回滚；BP显示与实际值同步门保留。

相关规格　[player trainers partners](../spec/creatures/player-trainers-partners.md)、[party and storage](../spec/creatures/party-and-storage.md)、[bag and item storage](../spec/creatures/bag-and-item-storage.md)、[item use and training](../spec/creatures/item-use-and-training.md)、[shops and exchanges](../spec/creatures/shops-and-exchanges.md)、[growth learning and friendship](../spec/creatures/growth-learning-and-friendship.md)、[mail and mystery gift](../spec/creatures/mail-and-mystery-gift.md)、[party and summary ui](../spec/ui/party-and-summary-ui.md)、[storage and pokedex ui](../spec/ui/storage-and-pokedex-ui.md)、[bag item storage and shop ui](../spec/ui/bag-item-storage-and-shop-ui.md)

## CHAIN-4 设施提交/恢复/异常

nil取消不覆盖原队伍；空列表显式提交false；经验快照在等级调整前、物品在调整后；正常归还等级→治疗→解除→恢复物品。原队伍快照只开始写；进行中报名/租借显式空列表立即写报名及玩家引用并返回假，nil不提交；玩家引用另有开始/取消/结束写入，保存/重置/刷新门按WP55§2.2–2.4分列。

正常治疗不是HP/PP快照；正常UI空列表可达未证；异常可能阻止后层清理；文件打开前/后失败的落盘状态分开。

相关规格　[battle context and participants](../spec/battle/battle-context-and-participants.md)、[entry eligibility level adjustment and clauses](../spec/battle/entry-eligibility-level-adjustment-and-clauses.md)、[entry rules and cup data](../spec/battle/entry-rules-and-cup-data.md)、[facility session and restoration](../spec/battle/facility-session-and-restoration.md)、[palace and arena variants](../spec/battle/palace-and-arena-variants.md)、[factory rentals and swaps](../spec/battle/factory-rentals-and-swaps.md)、[battle recording and playback](../spec/battle/battle-recording-and-playback.md)、[battle interaction and presentation](../spec/ui/battle-interaction-and-presentation.md)、[lifecycle presentations and history](../spec/ui/lifecycle-presentations-and-history.md)、[facility content generation and simulation](../spec/authoring/facility-content-generation-and-simulation.md)

## CHAIN-5 形态/Shadow/成长

形态写入先于交互学习，学习拒绝不回滚；ROTOM同形态且唯一目标招仍可能删到0；Shadow量表0仍Shadow，香门friendship255，储存HARDY90/LONELY130分列。Shadow四文本已读样本字段/131量表与招式样本全集由WP23附表§3承接，U06实际启用未知；对 Gen5–8 只给目录身份的早期输入不能推出字段值。稍后的采样见[旧世代备份的字段与启用条件](generation-data-compatibility.md)。

默认普通经验消息关闭，直接helper显式消息可先提示后被阶段门拒绝；可选备份U06未证，不把G0或friendship与阶段概念混用。

相关规格　[attributes ability and stats](../spec/creatures/attributes-ability-and-stats.md)、[hp status moves helditem](../spec/creatures/hp-status-moves-helditem.md)、[dynamic forms and display](../spec/creatures/dynamic-forms-and-display.md)、[shadow data and vectors](../spec/creatures/shadow-data-and-vectors.md)、[shadow hyper and purification](../spec/creatures/shadow-hyper-and-purification.md)、[item use and training](../spec/creatures/item-use-and-training.md)、[growth learning and friendship](../spec/creatures/growth-learning-and-friendship.md)、[inheritance and offspring](../spec/creatures/inheritance-and-offspring.md)、[eggs and hatching](../spec/creatures/eggs-and-hatching.md)、[pokedex records regions and content](../spec/creatures/pokedex-records-regions-and-content.md)、[battle interaction and presentation](../spec/ui/battle-interaction-and-presentation.md)、[lifecycle presentations and history](../spec/ui/lifecycle-presentations-and-history.md)

## CHAIN-6 编辑/编译/登记/缓存

编辑登记→archive→PBS→编译→当前地图快照分层；0率archive反写省略，重编译Land21；同版本早退保留；指标写路径由保存时非零形态集决定，已有布局不自动刷新。

复数Evolutions父No不把数值转文本；单数写出共享转换另列；标准非lambda break局部失败，不用已更正return推理；宿主外层收口未知。 仅文本消费的条件边界：整段求值正常后再检任一行；三准确前缀命中则推进/结束帧，无命中则推进/同帧继续；异常先于检查/推进。不是转换自动执行路线或编译链保证。 路线脚本文本的静态反例见 [maps movement events and field actions](../vectors/maps-movement-events-and-field-actions.md) 中的 MR18、MR19、MR20、MR21、MR22。 编辑旧复数 Evolutions 的原字段与清空行为、向 PBS 写出的转换分别检查。

相关规格　[pbs lifecycle](../spec/core/pbs-lifecycle.md)、[wild encounters and modifiers](../spec/world/wild-encounters-and-modifiers.md)、[debug contexts and controls](../spec/authoring/debug-contexts-and-controls.md)、[content editors](../spec/authoring/content-editors.md)、[world editors](../spec/authoring/world-editors.md)、[battle animation authoring and exchange](../spec/authoring/battle-animation-authoring-and-exchange.md)、[project conversion and authoring tools](../spec/authoring/project-conversion-and-authoring-tools.md)、[demo evidence and capability coverage](../spec/authoring/demo-evidence-and-capability-coverage.md)

## CHAIN-7 Arena/攻击记录/回放

Arena开局复位，正常补位不调用孤立复位辅助；第3/4/5回合连续裁判，HP/技能基线与提示门保留；回放按录制攻击/随机序列消费。

替补辅助可进入攻击阶段及回合末；随机Roar不等于业主选择流。随机强制换人不新增独立记录字段。

相关规格　[battle context and participants](../spec/battle/battle-context-and-participants.md)、[commands obedience and action order](../spec/battle/commands-obedience-and-action-order.md)、[switching positioning and escape](../spec/battle/switching-positioning-and-escape.md)、[palace and arena variants](../spec/battle/palace-and-arena-variants.md)、[battle recording and playback](../spec/battle/battle-recording-and-playback.md)、[battle interaction and presentation](../spec/ui/battle-interaction-and-presentation.md)、[lifecycle presentations and history](../spec/ui/lifecycle-presentations-and-history.md)、[facility content generation and simulation](../spec/authoring/facility-content-generation-and-simulation.md)

## CHAIN-8 世界显示/时序/目标几何

34世界场景分族保留；飞行先于消息/outdoorlight不受TIME_SHADING户外门/计时负业务值显示0；暂停初显0后全局相位，预览两个周期；选曲与播放/等待/返回清预置分工。天气先旧图存在/异图门和类型不同门才局部0，合法连接独立后写20；同类型显式重建保持旧duration，同图不重掷，正在渐变/强度单改守卫保留。

零时长即时插值不取消在途任务；99998计时/动画排序各自独立。NearAlly正常三席存活远位可初选登记但执行拒绝；无存活非自身同侧才回自身。 即时图片、编号加 50 和传送记录保留各有自己的条件。计时器业务剩余时间可为负数，显示最低为 00:00。

相关规格　[map topology transfer](../spec/world/map-topology-transfer.md)、[interpreter command matrix](../spec/world/interpreter-command-matrix.md)、[map events npc followers](../spec/world/map-events-npc-followers.md)、[move route matrix](../spec/world/move-route-matrix.md)、[resource matching and audio](../spec/world/resource-matching-and-audio.md)、[pre battle transitions](../spec/world/pre-battle-transitions.md)、[world rendering and visual transitions](../spec/world/world-rendering-and-visual-transitions.md)、[draw text tags](../spec/ui/draw-text-tags.md)、[messages windows input](../spec/ui/messages-windows-input.md)、[player trainers partners](../spec/creatures/player-trainers-partners.md)、[commands obedience and action order](../spec/battle/commands-obedience-and-action-order.md)、[world time weather field moves](../spec/world/world-time-weather-field-moves.md)、[controls help appendix](../spec/ui/controls-help-appendix.md)、[title load options pause and pc](../spec/ui/title-load-options-pause-and-pc.md)、[trainer card appendix](../spec/ui/trainer-card-appendix.md)、[party and summary ui](../spec/ui/party-and-summary-ui.md)、[storage and pokedex ui](../spec/ui/storage-and-pokedex-ui.md)、[bag item storage and shop ui](../spec/ui/bag-item-storage-and-shop-ui.md)、[battle interaction and presentation](../spec/ui/battle-interaction-and-presentation.md)、[lifecycle presentations and history](../spec/ui/lifecycle-presentations-and-history.md)

## 相关验证条件

取消型、索引 0 与返回 0 需由各入口分别验证。交叉检查还包括 MIDI、公共事件 5 的结束消息、CV 格式／翻页／CN／实体、训练家编号、两类跳跃、默认 5×5 地牢的 Y 读取调整后的 X、缺失第 28 项树果、字体标记字母、反射高度／桥／时间门、75 随机与强制单打、午时四通道 138、毒伤配置／感染期、净化有效开始事件、队伍目标上限／候选交集／非蛋、LC09 第三个选项 c、拼图空格／空手与 T18 列。

验证数据含 120 个效果（83／22／13／2，按类型、默认、范围、哨兵检查）、24 小时四通道色调、35 种旧转换与三个路线前缀、资源目录与后缀及登记门、火箭身份与颜色、KYOGRE 四键专属邻接、18 个弃用电话入口。KYOGRE 邻接不构成全局十图规则。67 树果整表的范围有条件。

兼容拼接字面 Common: 保持原空格；名称本身可含空格。默认 4×4 模式 6／7 的五步不可完成证明仅适用给定尺寸和步骤；表外模式 0 的 1×1 输入可先完成并返回真。
