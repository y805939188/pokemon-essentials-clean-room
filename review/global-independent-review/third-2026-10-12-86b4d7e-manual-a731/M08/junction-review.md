# M08 交界审查

角色 `/root/m08_effects_items_v3`；运行=0。以下保留本模块独立证据与未决，跨模块最终裁判由主角色负责。固定参考/正式提交和精确 blob 见 report 与 file-coverage；所有案例 NOT_EXECUTED。

## G4-9：数值输入与效果修正管道

判定 **SUPPORTED_STATIC_LOCAL / 全局主公式 PARTIAL**。正常：当前速度/重量在对应查询消费；气场→U能力→模式破坏门内U盟友/普通T→T不可忽略→门内T盟友→U物→T物→通用后置。P/A/D/F量值及指定取整位置不能互换；ChoiceBand/Specs在参考为P，ChoiceScarf速度与讲究锁是两条合同。反向：模式破坏者可跳重量能力而不跳FLOATSTONE；无处理器的当前层回退不是未知整能力无效果；非法型相性优先与类型主域由M07保留。

证据：`Data/Scripts/011_Battle/003_Move/003_Move_UsageCalculations.rb`（blob `342abdfb68fb2faec2e25ce803aca3dafbb07b4e`，239–469）；`Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb`（blob `dfea2bb1c97725d8c01ec40fb34549539de04e23`，277–290）；`Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb`（blob `6deff3758f06a7fce8190b6a05c25a3ac69a4936`，1197–1593）；`Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb`（blob `240046fc93ac5221b2684601338a83603173eaab`，725–1234）。正式 `deliverables/final-specification-set/pokemon-rules/wp48-ability-calculation-modifiers.md`（blob `bc6d6c0ba4bfc4589b533acdde5736dbc15b9d71`，§2–§5）、`deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md`（blob `c00e9aaa1bd80b3ace7bc05261e5a7d68c16504d`，§2–§3）、`deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md`（blob `86da3961aba6375142252e8fb3ade847e68f9115`，§5）。

消费者：M04个体当前值、M07命中/伤害/排序、M06沉重球、M09预测。固定1180→590与2360→1180→590及能力/物品分门已支持；本轮未全读捕获公式/世界基值/AI消费，不独自关闭整条全局交界。

## G6-3：持物消费与终局还原

判定 **SUPPORTED_STATIC_LOCAL / FULL_CHAIN_PARTIAL**。正常：当前C写穿个体；I可被真实消费/野生转移更新；R/P与Belch按入口差异；普通终局接收发生后，仅对届时战斗玩家侧队伍列表做一次I还原。反向：AIRBALLOON不可回收不新写R/P；按钮/包禁共生；红牌先消费后吸盘/扎根可阻换；负选择不保证退款；异常未到正常终局不保证还原。

证据：`Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb`（blob `dfea2bb1c97725d8c01ec40fb34549539de04e23`，81–89,664–691）；`Data/Scripts/011_Battle/002_Battler/006_Battler_AbilityAndItem.rb`（blob `3e5005b540e7657e15e77133aaf4a551eac57835`，226–311）；`Data/Scripts/011_Battle/003_Move/011_MoveEffects_Items.rb`（blob `92fa820e0f97a6ad3a5c98e29a249ed4cb8d88ac`，5–130,136–204）；`Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb`（blob `240046fc93ac5221b2684601338a83603173eaab`，447–471,1525–1573）；`Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb`（blob `54d4f8d6a10df57937838b36ec145a96fdc7b91e`，477–511：先捕获接收、后当前队伍一次还原）。正式 `deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md`（blob `c00e9aaa1bd80b3ace7bc05261e5a7d68c16504d`，§1–§2,§5）、`deliverables/final-specification-set/combat-requirements/wp47-b-switching-control-and-item-changes.md`（blob `3eb34eb5d94ce84903fd203788e5f4f15fe10785`，§5.1–§5.3）。

消费者：M05持久个体/队伍，M06捕获接收/存储，M07终局，M09设施，M10呈现。伙伴2v1、满队有盒位/正常接收后 boxed A=Y/live B空 的历史完整前提已作为导航保留；本轮没有重读完整接收/移位/储存链，不能声称运行或独自重证这一最终对象关系，也不得增设移位玩家第二次恢复遍历。

## CHAIN-1：伙伴捕获/持物/存储

判定 **PARTIAL**。与G6-3共享一次还原局部证据；正常链必须保留普通2v1、伙伴参战、玩家满队、盒位可用、正常接收、接收使玩家列表移位但参与记录仍旧对象的全部有效前提。不能以单打/无伙伴简化夹具替代；无需KnockOff，自然打落空物子例未证。

历史定位：`c2bc1a341ba6acdf7c8c111dc88d39a162a093d6:review/remediation/20261003-prepare/FINAL-1/independent-review-cloud-20261011-1/junction-chain-review.json#/per_chain_results/0`。此处只复用具名前提和局部主规则，非旧PASS迁移。M05/M06/M07/M10及主角色应合并本轮各自消费者证据后定最终链状态。

## M07新增提示：GULPMISSILE每击读写顺序

判定 **SUPPORTED_STATIC**，没有新finding。M07向主角色提示的 14–34 行链由M08独立回源。先形态请求0，后读取当前形态决定1降防/2麻痹；通用形态请求拒倒下/变身/已同型。存活非变身T提交0后无这两额外分支；倒下T拒提交而保留1/2时可继续到对应中央请求。U仍须实际间伤/状态/阶级资格，不能保证最终一定降防/麻痹。

证据：`Data/Scripts/011_Battle/002_Battler/010_Battler_UseMoveTriggerEffects.rb`（blob `f35de8ff5fd94e46279a59e4355a8db26e0502b2`，14–34）；`Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb`（blob `a3c00d47e159924e49f83aad5485718381ebae33`，156–169）。正式 `deliverables/final-specification-set/combat-requirements/wp49-ability-phase-triggers.md`（blob `06f36f3f8aec39fa944ac0946dda132d054c92bd`，§9.2吐导弹段）；测试WP49 AB-D08明确存活/倒下反向，属于静态设计。未通过用户决定把参考异常改成常见游戏规则。

## 新交界：自然之恩续击与持物反应

判定 **PARTIAL / GR3-M08-001 REQUIRED_REVISION**。M08-C25 覆盖正常自然之恩，但源首击后U当前物可能被HP恢复物自耗；续击不重跑起用树果门。H160/h81、ORAN、有亲子爱；目标JABO且首击后存活；首击反伤20→61、恢复10→71并空物；第二击基底先访问空当前物品身份而失败，已提交状态保留。高HP101对照→81>80不自耗，单击对照无第二次访问。

证据：`Data/Scripts/011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb`（blob `2f6f5db5298d8c7ee8cd046d9b9124f895b41ab1`，1338–1379，尤其1364–1369）；`Data/Scripts/011_Battle/003_Move/002_Move_Usage.rb`（blob `10b06a44eabef9cd87291712141e938872acff1c`，45–54）；`Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb`（blob `b6aa0c7f4aafc8b99d80508978f5704bc51a5867`，404–432,583–646）；`Data/Scripts/011_Battle/002_Battler/010_Battler_UseMoveTriggerEffects.rb`（blob `f35de8ff5fd94e46279a59e4355a8db26e0502b2`，40–45）；`Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb`（blob `240046fc93ac5221b2684601338a83603173eaab`，364–387,1311–1331）；`Data/Scripts/011_Battle/002_Battler/006_Battler_AbilityAndItem.rb`（blob `3e5005b540e7657e15e77133aaf4a551eac57835`，212–243,315–323）；`Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb`（blob `dfea2bb1c97725d8c01ec40fb34549539de04e23`，81–89）；`Data/Scripts/010_Data/001_GameData.rb`（blob `ccfd971a29b3bab107e2da6865ac0050ed3256b0`，99–116）。

正式 `deliverables/final-specification-set/combat-requirements/wp47-a-move-attributes-targeting-and-calling.md`（blob `977839d20748e302813f6fe55bf1ba6a08a01225`，§3.1 line45） 与 `deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md`（blob `86da3961aba6375142252e8fb3ade847e68f9115`，§2.1,§3.1亲子爱） 未补该当前空物威力失败。失败在物品数据get之前，不能写成get空ID回退；没有游戏运行，宿主诊断/恢复未证。与已有GR-014投掷空物异常有关但不同失败位置/招式/前提。M07应核一般动作异常边界；M09预测仅为后续消费待验。补写异常与三组可验设计是规格任务；未来是否兼容bug由用户选择。
