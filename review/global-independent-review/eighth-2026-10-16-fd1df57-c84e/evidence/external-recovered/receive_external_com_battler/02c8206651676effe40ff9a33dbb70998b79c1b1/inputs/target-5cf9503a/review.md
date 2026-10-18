# R8 COM-BATTLER 独立审查证据（续审完成主读责任）

十个 Battler 主文件的完整正文审读、结构分解和本地双向比较已完成；有限跨域接收、两条提案的不同上下文反证与主审最终接收仍开放，**不宣告全局 PASS**。本次没有整改，`UPDATE_NOT_STARTED`。

固定 B8 `fd1df570cad987dc3852a3b958f03916e317f7fe`，workspace tree `751dfde81048c81390f89a65ca1d1a565ba8e1ca`，正式 tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`；R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。委派 prompt/readset 固定 `30cfed0996003b6ebf4b5c51cc04f31ca9255440`，必要跨域接收合同固定 `ea3359282fe4e27132fa3ceaa2d8f308b0831510`。实际云端规格目录 `/workspace/pokemon-essentials-clean-room`、参考目录 `/workspace/pokemon-essentials`。完整委派、全局 prompt、适用 AGENTS、review-SKILL 已实读；身份以 mode/blob/bytes/SHA256 对照固定对象，读取区间与精确补集见 [identities.json](identities.json)、[reading-ledger.json](reading-ledger.json)。

审者为同一实际外部委派上下文 `/root`，来源线程 `01a13f49-a154-7054-9b04-ce31f924d01c`。用户授权只 commit/普通 push 本目录至 `codex/r8-external-com-battler-20261016`；未 spawn，未改 main/tag/正式规格/参考/公共台账/他人目录。30cf/ea3359 是读取输入，没有把其余报告并入本分支。

主读分母是 **10/10 文件、4,646 行、183,690 bytes，未读 0**。逐文件计数如下；不是搜索命中或旧 PASS 信用。

| 文件序号 | 结构（方法/声明） | 显式子断言 |
|---|---:|---:|
| 001_Battle_Battler.rb | 151 | 236 |
| 002_Battler_Initialize.rb | 9 | 146 |
| 003_Battler_ChangeSelf.rb | 17 | 50 |
| 004_Battler_Statuses.rb | 37 | 76 |
| 005_Battler_StatStages.rb | 17 | 42 |
| 006_Battler_AbilityAndItem.rb | 31 | 77 |
| 007_Battler_UseMove.rb | 8 | 78 |
| 008_Battler_UseMoveTargeting.rb | 8 | 25 |
| 009_Battler_UseMoveSuccessChecks.rb | 7 | 51 |
| 010_Battler_UseMoveTriggerEffects.rb | 4 | 29 |

合计 **289 结构（231 方法、58 声明）、810 条显式子断言、92 个语义族**；另逐文件交代 10 个 class 重开包络与注释/空行/end。810 是完整正文后手工列出的复合规则子断言分母，包含有序守卫序列，不是声称存在唯一数学原子切分。初始化逐字段检查补齐 `ProtectRate=1`；没有把“全文读完”等同于“机械索引证明语义”。

[forward-mapping.json](forward-mapping.json) 保存每个结构的精确源范围、各子断言、前提、条款关系、必要消费者与接口。旧 ECB-F001..088 通过固定源范围接到新复合单元，旧笼统观察已废止为当前事实依据：能力有效不普遍豁免不可失去名单，trapped 原查询不含上层逃脱豁免，离睡清 Truant，濒死标志在 InitEffects 内建立，Reset 不明确清 captured，HP/等级/状态/PP 接收者有独立校验/夹限和部分提交，AfterMove3 只处理用户物品/能力退出。

[reverse-mapping.json](reverse-mapping.json) 对 **58 组必要 B8 条款、160 条显式条款子断言**逐项给主源 facet、前提、具体消费者和处置；其中 23 条还明确列外域 facet。该分母不冒充所有扩展 formal 的全部条款。状态/默认值/别名实现不强制未来提供相同 Ruby API；组合支持也不等于逐名帮助函数必须复刻。根接收仍为 0/810 源子断言、0/160 选定条款子断言。

主审已明确扩展 98 R/43 formal 清单不是本任务全部 primary。个人已读/未读仍按每个文件精确保留，不改成全局已读、全局未读或 material limit。其他 primary 的完整 Move/Ability/Item/Pokemon/AI/变体/展示/数据/历史责任继续归其原实际负责人；本任务交付实际需要的有限接口。

[interfaces.json](interfaces.json) 保持中央四接口 IF-CORE、IF-MOVE、IF-ABILITY-ITEM、IF-POKEMON-PERSISTENCE，附 24 个本上下文直接核过的有限消费者事实，并单列 HISTORY 资格接点。内容包括共享集合/业主/交换/入场/调度/EOR/诊断、HandlerHash 的覆盖/复制/缺省、能力和物品全部 dispatcher 定义及选定倍率族、GameData 查找/相等、完整 Ability/Item schema、持久 HP/状态/等级/形态/能力值/物品/关联 PP、Shadow 覆写、Peer，以及刷新/位图/HP 等待和 Illusion/闪光字段来源。每个事实带精确范围，未读注册体/子方法/原生显示不借完整前缀获得信用。中央合同原始四接口及展示 IF04 的完整 JSON 对象已读，其他入口仅导航；全文件 cat 截断没有登记全文。35 PBS 的 20/8/6/1 归属是有限路由，不是新增 35 个本任务主文件，备份需显式选择/替换，不自动递归激活。

两条疑似提案仍见 [proposals.json](proposals.json)：GR8-ECB-001 是晚期正常失败后模式标志留至 Octolock 的静态条件向量；GR8-ECB-002 是 WonderRoom 下 Transform 从 getter 读取再写原字段的向量。**现有 WP40/42/44 和 WP43/47B/49 的组合可能已经推出结果**，未证明 required 缺项，分类保持 UNDECIDED_NOT_REQUIRED，接受数 0。中央合同已分别路由实际 CORE/CREA 不同上下文反证；需同时判断合法可达状态、原接收者、当前条款可推导性与历史 canonical/optional 资格。作者未自接收、未将自己改名充当独立复核。

直接对面 early-break、BeakBlast 错误接收者、Gulp 生存分支、MentalHerb 身份/计数及 NaturalGift 部分失败已有合同，未重复上报。GR8-COM-001 只有本上下文有限佐证，GR8-COM-002 混合席创建/AI/UI 全链未亲读，均不冒充最终接收。

**行为执行 0，全部向量 NOT_EXECUTED。** Ruby 可用性检查 exit127，未安装。实际 model/effort/tier/Fast、平台会话/完整原始日志导出 ID 分别 UNVERIFIED；请求配置不是实际证明。工具对话保留 stdout/stderr/exit 与 chunk；截断、错误目录/文件名尝试不作负证据。Mac 历史准备与其他工作树未在云端认证。验证仅检查报告 JSON、定位、范围、分母和写集，不代替人工语义比较。

交付缺口是四个中央有限接口与历史资格的主审累计接收、两条提案的实际不同上下文反证及最终签收；不是十主文件尚未读完，也不要求外域全系统重读。主证据 commit `ec1de4d398028ff0504185aced6e451c28adc656` 已普通 push，并从独立 bare 仓库完整读取远端 10 文件、2567898 bytes，逐字节/对象/模式/SHA256 均相等；收据见 publication.json。包含该收据的最终 tip/tree/任务 tree 与最终十文件回读由最终回复和独立 /tmp 凭据绑定，避免文件自哈希循环。
