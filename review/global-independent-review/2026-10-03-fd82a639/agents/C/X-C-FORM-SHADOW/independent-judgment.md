# X-C-FORM-SHADOW 独立首判

保存时间：**2026-10-03 19:33:56 UTC**。此文件及同名JSON在保存后冻结；后续比较另写，不追改首判。固定项目`e1e01bb18d824931e54f182dd61af5a9f908ba85`，只读参考`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。已完成C全部主审；此为第二视角，**新增WP主审计数0**。

本次只读中性brief、固定原/净化材料与来源，尚未读本交叉的A/ROOT结论。此前ROOT002/ROOT004授权比较与邻接邮件/净化室段意外暴露已持续披露，尤其CF-04不能称完全盲审。C07的UI_PurifyChamber 1–1308、ShadowPokemon_Other 1–460全文阅读明确复用并定点重读；其它实际范围见JSON和reading-log.tsv，未冒充全模块重审。

## CF-01 · 三种形态提交分层；ROTOM同值普通提交可删唯一招

初判：**SPEC_GAP_CANDIDATE**。

1. 普通提交先写形态/清特性缓存，再执行形态处理，正常返回后重算并登记玩家图鉴；同值并无早退。提示型在清缓存后、处理前执行提示承接者；承接者自己读取可重新填充缓存，不能把清缓存当最终恒为空。简化写入只写形态并重算，不调用处理/清特性缓存/登记。

2. ROTOM没有旧形态招时，普通或提示提交到1会走交互教学；满四槽放弃或有效Shadow被教学拒绝后，形态已写，既有招不变，正常继续重算/登记。若提示承接或后续消息抛错则按已执行阶段保留，不假定回滚。

3. 具名反例：有效非蛋ROTOM存储形态1、唯一OVERHEAT、对应招与THUNDERSHOCK均存在。低层普通提交1后目标OVERHEAT先被选中；已有该招使后续目标被抹空，因保底检查已经过去，唯一旧形招被删除，最终0招。随后仍重算/登记。提示型正常返回时相同；简化写入保留OVERHEAT。

4. 正常ROTOM目录选择当前形态1先提示无效并返回，不调用提交，不删招。不能把低层反例冒充普通目录选当前形态的可达结果。

5. 原/净化WP21有入口分层、拒绝不回滚与无目标保底异常，但未写目标已知发生在保底之后的删除分叉；FM13/14/20不覆盖此合法同值前提。拟与A/ROOT同根发现比较，首判不分配重复RUN编号。

证据：`Data/Scripts/014_Pokemon/001_Pokemon.rb:147-184;612-615;672-674;1099-1127`；`Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb:221-265`；`Data/Scripts/013_Items/001_Item_Utilities.rb:582-627`；`Data/Scripts/013_Items/002_Item_Effects.rb:1232-1261`；`specs/pokemon-rules/wp21-dynamic-forms-and-display.md:101;175-195;323-330`；`deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md:79;151-171`；`deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md:92-99`。

## CF-02 · 七种离场/返回按对象集合和还原次序分开

初判：**ALREADY_COVERED_SCOPED**。

1. 普通换下：旧席位换下能力、一般离场处理与HP上限钳制后，只把战斗副本视为濒死以收尾能力；没有统一Mega/Primal解除，持久HP不因此0。默认特殊形态对象可在换入时保留。

2. 真正濒死：持久HP先经写0清理；濒死效果/状态/友好度后先一般离场，再显式解除持久Mega、Primal。该分支不完整刷新战斗形态副本，默认形态数据下不由解除复活。

3. 捕获成功：对手移出→条件化普通成长→场上对象复位→必要属主改写/球效果/球种→Mega/Primal解除→Shadow招式刷新/首招→读取型物种解除强制形态→一般终战离场→待接收队列；所有权/图鉴/存放时点不合并。

4. 满队换出既有成员：选人取消尚未走下列写入；确认后一般终战离场→剧毒计数0→解除两形态→按当前持物存盒→队伍移除及指定记忆数组移动。该对象不再等待世界当前队伍还原；心量表旧快照不能凭此假定同步。

5. 裸正常终局：先接收捕获队列，随后结束画面/取消选择/逐席位离场能力，逐玩家侧战斗队伍成员做一般终战离场后恢复可更新物品记录；包含该战斗队伍的未实际出场成员，参战标志是传入数据，不是循环过滤。此层没有统一解除特殊形态，不扫描对方整队。

6. 世界正常返回：在裸返回后的善后，当前玩家队伍清剧毒并解除；伙伴存在时治疗玩家和伙伴、解除伙伴；可败负/平再治疗玩家。裸终局的玩家侧物品恢复已在前。并非对方原队伍全体，也不是所有异常都保证返回。

7. 设施正常返回：裸战斗后先恢复双方经验/等级/能力，然后分别双方成员治疗→解除Mega/Primal→恢复包装保存物品；裸层此前只恢复玩家侧可更新记录。回放不借用该设施恢复包。Primal身份依当前宝珠，所以恢复物品前/后不能任意交换。

8. WP22§6、WP38§5/6、WP42§6/7、WP54§4.2及ME17-23已分层，未认定新的统一离场缺陷。表内‘参与个体’按实际战斗队伍数组解释，不能改成仅实际出场者。

证据：`Data/Scripts/011_Battle/002_Battler/006_Battler_AbilityAndItem.rb:5-28`；`Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb:64-99`；`Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb:34-60;165-195`；`Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb:479-511`；`Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb:306-329;399-408;519-528`；`Data/Scripts/018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb:50-97;111-128`；`deliverables/final-specification-set/pokemon-rules/wp22-mega-and-primal-reversion.md:74-87`；`deliverables/final-specification-set/pokemon-rules/wp38-capture-and-receiving.md:83-114`；`deliverables/final-specification-set/combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md:99-101`。

## CF-03 · 重复建立非幂等、完整治疗不清Hyper、暂存EV复制共享

初判：**ALREADY_COVERED_SCOPED**。

1. 重复建立会清Hyper、清暂存经验、重新建立全0暂存EV、量表置最大与步数归0，并重建Shadow记录；有有效Shadow招时恢复目标来自此刻已知招，旧暂存及旧原招记录不保留。无有效Shadow招的默认条件只保留当前招，不凭备份声称启用。

2. 存活G>0且Hyper真者完整治疗只回HP/异常/PP并清进化准备，Hyper仍可真；经HP赋值到0才叠加清Hyper。G降到0仅令有效查询假，旧存储Hyper可仍真，人工升G可再显露。

3. 克隆后当前EV/IV与实际招式状态等基础字段按基础复制分别独立；Shadow招式标识记录列表另复制。暂存EV没有新建容器，改副本V某项可改原体同项；把副本V重新绑定为空只改变副本绑定，原体表与先前修改保留。整数暂存经验/量表等值写入不会像该表的就地修改传播。

4. WP23§2 S01/S03、§5 H03与SH02/15/41已经准确保留；不再新建重复问题，不把引用事实用作未来架构模板。

证据：`Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb:13-26;93-140;212-221`；`Data/Scripts/014_Pokemon/001_Pokemon.rb:246-306;1135-1150`；`deliverables/final-specification-set/pokemon-rules/wp23-shadow-hyper-and-purification.md:26-30;68-70`；`deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md:151;164-165;190`。

## CF-04 · 净化先提交与同级/跨级、命名、双满、下一组四边界

初判：**ALREADY_COVERED_WITH_DISCLOSED_PRIOR_EXPOSURE**。

1. 统一净化先净化统计+1、清Shadow/Hyper、授NATIONAL；再消息/恢复招式/重记首招；受额度恢复EV后清V；若S存在则算floor(4S/5)受最大经验限制并先清S。G、步数、所有者等不统一清空。

2. 同等级：写精确经验并重算后可到命名，拒绝昵称不撤回净化；S0仍走重算，S缺失跳经验和这次重算。不是完整治疗。

3. 跨等级：等级工具先写新等级下限经验、重算、升级友好变化，再进入首个能力窗口更新。净化室传入接收者缺更新方法，且该调用在确认键判断之前；因此失败时前述状态和等级下限已提交，精确目标经验、学招/进化/昵称、存放/清中心未到。

4. 固定RATTATA Medium L10/E1000/S416：恢复请求332、目标1332/L11；净化室停在E1331且中心仍引用已修改对象。遗迹石接收者有空更新方法，在其余呈现正常前提下可越过同点，工具正常返回后写E1332；学习放弃、可取消进化或昵称拒绝不回滚前提交。

5. 只有确实越过统一净化（如S0同等级）的路径才检查后续双满。通用存放双满提示后早退，但净化室仍无条件清中心；此前已净化/命名状态不回滚。第一组正常净化/存放/清中心后拒绝下一组只停止后续组，第一组不撤回。跨级首窗失败不能拿来作双满/下一组拒绝例子。

6. 原/净化WP23§6.2/8.3、WP67-B§6.3/6.4、SH24/38/39/43-45已保留，本次不是新缺陷。先前ROOT004邻接净化室取消段的已披露暴露适用于本项，不能称完全盲审；仍做本次逐源独立状态推导。

证据：`Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:17-58;106-160`；`Data/Scripts/013_Items/001_Item_Utilities.rb:132-221`；`Data/Scripts/016_UI/023_UI_PurifyChamber.rb:348-359;548-594;1072-1079;1123-1127`；`Data/Scripts/019_Utilities/002_Utilities_Pokemon.rb:4-31`；`deliverables/final-specification-set/pokemon-rules/wp23-shadow-hyper-and-purification.md:88-110;176-180`；`deliverables/final-specification-set/user-interface/wp67-b-lifecycle-presentations-and-history.md:122-132`；`deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md:173;187-188;192-194`。

## CF-05 · Shadow经验提示必须保留正常分配与显式开启的单体辅助两层

初判：**CONDITIONAL_HELPER_FACT_NOT_NORMAL_FLOW_DEFECT**。

1. 普通成长分配对参与/分享者把个别消息参数设为‘非Shadow’，故有效Shadow总为关闭；Exp All补发同样明确关闭个别提示。捕获成长也调用同一普通分配，并不会把该参数改真。全体补发的一次泛化提示是另一条消息，可能仍出现。

2. 有效Shadow心阶段0～3且正的受限增量D时暂存和total_exp_gained各+D，当前经验不变；阶段4/5时这两项均不增加。该描述不把高阶段EV普通写入抹掉。

3. 直接调用单体辅助且显式开启消息、当前未到经验上限、正增量D、其它数据有效时，个别获得经验提示先于Shadow心阶段门。因此H4/5也能先提示D再不增经验/暂存/统计；H0～3提示后暂存/统计增加，当前经验仍不变。达到上限或非正实际增量在提示前早退。

4. 全脚本只定位到普通分配的两个调用点；没有已读正常入口把有效Shadow消息参数设真。显式辅助是条件化直接调用，不能称普通战斗或普通捕获会给Shadow错误到账提示。

5. WP30§4.1（原83/净86）已明确正常Shadow抑制；§4.2第11项泛写消息若作完整辅助合同宜补参数，但与上一节合读不能推出正常流程有该提示。此首判不以正常流程缺陷报P2；比较时应保留可达性限定。

证据：`Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb:5-56;92-99;160-185`；`Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb:165-175`；`specs/creature-rpg/wp30-growth-learning-and-friendship.md:78-102`；`deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md:81-105`；`deliverables/final-specification-set/combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md:63-83`；`deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md:146-148`。

## CF-06 · Shadow香资格把h255误写为心阶段H5

初判：**SANITIZATION_CONFLICT_CANDIDATE**。

1. 读取本交叉的WP23分入口表时另见净化第120/121行把原h255改成H5。主规格H是0～5心阶段，而h255是友好度达到255，不能互换。

2. 源共同香工具与战斗资格拒绝的是非Shadow，或友好度255且G0。有效Shadow G0时心阶段为0；因此一个h255/G0的有效非Hyper个体应被拒，按H5且G0却不会命中。

3. 这是原稿→净化的直接条件漂移候选，未见在本代理既有发现中登记。只在直接共同工具/有效具名处理器或明确提供可选物品数据时作向量；不声称默认顶层已启用香。拟请求与A/ROOT同根发现有界比较后再决定去重编号。

证据：`Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:226-244;286-294`；`Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb:93-106`；`specs/pokemon-rules/wp23-shadow-hyper-and-purification.md:120-121`；`deliverables/final-specification-set/pokemon-rules/wp23-shadow-hyper-and-purification.md:120-121`。

## 尚未关闭的边界

U01–U10、G01–G12、AX01–AX20全部保留；真实Demo事件链与运行证据为0。没有执行参考、游戏、编译/载入/生成器、反序列化、模拟器或求解器。没有实现未来框架或给出继承结构。本次来源中的字段共享仅描述可观察状态传播，不作架构模板。CF-01及偶见CF-06需有界比较去重；CF-05只支持显式消息参数的条件化辅助事实，不支持正常战斗/捕获误报。
