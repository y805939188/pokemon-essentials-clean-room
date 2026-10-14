# group-D / U10 实际整合非作者复审

四项均为 **ACTUAL_PASS_SCOPED_STATIC**，必要正文修订 **0**。结论只签实际快照 `9d5b4e99b617828690e6529b77a1e555d7c9eb1b` 的 U10 四项静态规则、向量及具名接合，不办理正式接受或 CLOSED。**GR6-F-002 为 PENDING_EXCLUDED**：WP66-A 已含接收器单句不意味着 U13 候选或 WP54/设施目录联合接口通过。

审者 `/root/storage_review`，本次角色 group-D U10 peer；非 U10 候选作者，未撰写本次被审正文，不继承原作者自检或候选 PASS 作为实际裁决。要求配置 gpt-6.1-sol / ultra / default tier / default speed / Fast=false；平台没有提供有效配置回显或可核 UUID，实际 model/effort/tier/speed/UUID 全部 **UNVERIFIED**。没有为此启动 CLI、探测配置或另开代理。

## 固定对象与直接读集

- 实际 commit `9d5b4e99b617828690e6529b77a1e555d7c9eb1b`，workspace tree `faae3b9a22c37a2e2e994553f59e7099c6394db0`，formal tree `74dccc64506d008d50cf1cdfd906f701931020cc`。
- 正式基线 `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`；R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。R 仅读 Git 对象，不检出、不修改、不执行。
- U10 candidate `d3554f9479fadcd1255cf8103b19e4aa88e1825b`；独立候选审 `dc3f0af0017e790c6e7dd32dc3bc280751230368` 的 `review-report.md` 全部 1–89 新读，14709 bytes / SHA256 `b01cf35e18d54b2cd8d63eb61c6c7ac9bb8147dffed77a54b10ba615b88aed3a` / blob `01322c19fd2cd88ac4c409ed771e534b5ea58ca4`。
- 根 AGENTS.md 全部 1–297；未发现适用 nested AGENTS；`.agents` 缺失。原 U10-R 提示执行通则 1–151 全读，截断中段另补 79–116。其原候选 allowlist 由本次明确委派覆盖；只写本 peer 目录。
- `contracts/R6-U10.json` 全部顶层字段及四个完整 `scope_contracts`（七组、原提案、原证据、反证、接收人）新读：120055 bytes / SHA256 `eb86301b11ef040f4a98365b93d8a6649409f32fe095a13974e697fe160d64f0` / blob `c33b84a0308bdd6776bee11dea7ee4243ba301f4`。
- actual-review-input 124082 bytes / SHA256 `7b63483a915792c077b2f8cf84208e9f5a7ac94e55ce93cfc8bbde718bf6d9aa` / blob `f7f220a4ee7c4b2ff6dc94b799fe54b13879b6c8`。直接读本组 batch9、files8/11/41/43/46、冲突/根编辑/receiver、全部状态/要求/排除节点；不把首次全文件输出截断声称为其它所有批的完整语义读。

| 实际文件（deliverables/final-specification-set/ 下） | 本人新语义读 | bytes | SHA256 | blob |
| --- | --- | ---: | --- | --- |
| creature-rpg/wp18-creature-identity-species-ownership.md | 全文 1–386 | 37612 | a6410f5d3bcdedef2d682bddaeff4d49facef22e297f19b9a908d855893d346c | 63048ab21f8fa5db77df11316f285db13e162594 |
| creature-rpg/wp30-growth-learning-and-friendship.md | 全文 1–286 | 32271 | f622dee4cd0fb1bbf89e47ef2c47bcf3c98f16dd12b5dfa48c006d39aec39fc3 | 1d6957846328bc5ad228932334c4fa32b02a47e5 |
| user-interface/wp66-a-party-and-summary-ui.md | 全文 1–267；132 联合接口排除 | 45706 | 2a5ed9d7b30ae7f309381d96ef01d33b21324793e1761d8ef7cea8a90a4dac49 | 00acb05350a3cbd4fce1cc0ecf74cb3c845ae07f |
| user-interface/wp67-a-battle-interaction-and-presentation.md | 全文 1–348 | 78217 | 66153fc4a013bf78743f37b58e9eeab1e7f8f01c139326e4e52f0176cd82553b | 44b915c2149ddc62f008445c309424626816fb55 |
| test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md | 208–358、566–938、947–1011 | 170395 | b4edb87c39ad8f9ec9f0572b55464d3f46f3d1da755ee578d33e2cef4ae546e5 | 4bc6fcda1473e6d31870dff079ba111bee97567b |

UI 1026 行的团队其它分配为 evidence peer 1–243、root 359–565 / 939–946 / 1012–1026；这些不是本人的全文阅读声明，团队完成回执由 root 最终绑定。本人另新读 WP38 103–123 与 WP53 49–99 的实际消费者。全部逐载荷 mode/type、完整 bytes/SHA/blob、直接范围/JSON指针、cwd/argv、UTC、exit 在 `reading-coverage.json` 与 `reading-ledger.jsonl`；87 个读送达记录、58 个载荷，首记录 16:18:10.986620 UTC，末记录 16:34:31.536079 UTC。机器同字节证明与语义阅读分列。

## R6-UI-001 — ACTUAL_PASS_SCOPED_STATIC

1. **identity_and_verdict**：唯一 U10 主责、P2 required，根因是满队替换送盒暂停的删除/记忆次序；不扩为全部接收、伙伴还原或任意存储异常。
2. **bidirectional_evidence**：固定 R `005_Battle_CatchAndStoreMixin.rb` 1–125，默认 `004_Battle_Peers.rb` 1–77、`004_PokemonStorage.rb` 231–259、Battle 97–107 / 815–841、Scene 230–265、ChooseCommands 141–228，形成存盒同一身份→删玩家队伍→阻塞提示→四记忆移位→收编 N→入队提示→初始物品回填的链。反向定位实际 WP67-A226/228、WP38 111/114、UI957–965。
3. **premises_and_counterexample**：满队 [A..F]、合法实际下标0、N待接收、至少一盒空位、sendToBoxes0（成功目标2同）、图鉴/命名/离场/盒名正常、无插件/竞争时，旧成员送盒提示内为盒持同一A、队伍[B..F]、N未入队、记忆未移。提示内受控失败仅保此前前缀，不保证队列清空、N收编、终局或外层恢复。
4. **minimum_revision_contract**：实际226与228同时修好旧成员提示前删除和新成员提示后回填；不是只改附表。其余去向/强制档/显示初始0/BACK99保持。最小必要再修订0。
5. **acceptance_and_regression**：CP01–09逐行新核，含正常移位/清尾、仅送N入盒、选人BACK、档2禁取消、两消息异常前缀及早容量失败。试图以Peer提前删除/非阻塞消息/最终队伍相同消除差异均不成立。全满默认Peer兜底失败在删A之前，CP08没有错误套CP06前缀。原K32/K33、R1 R04取消值与初选分离、R06逐个图鉴→命名→存放保持。
6. **independent_adjudication**：完整新读 storage/counterreview-R6-UI-001.json 并按固定源重新反证；不以其 SUPPORT 字段或旧候选PASS得出本结论。SOURCE_STATIC / DERIVED_VECTOR，零执行。
7. **dependencies_and_receivers**：实际 WP67-A与WP38的业务顺序相容；WP38新增的伙伴参与集合错配另有完整前提，本组共同夹具显式不推出其终局还原。UI消费同一捕获身份，未把显示状态当全局事务。未来 WP38接收/还原或WP67-A/CP字节改变须复验相关链。

## R6-UI-002 — ACTUAL_PASS_SCOPED_STATIC

1. **identity_and_verdict**：唯一U10/P2 required，仅Safari Ball容量拒绝门及扣球前后观察；不扩普通球概率或会话全域。
2. **bidirectional_evidence**：固定 Safari300–345/405–502、UtilitiesPokemon1–16、Trainer57–89、Storage1–40/110–165、SafariZone107–159及默认Peer全77行。玩家真实队伍不被Safari构造填成6；全部盒满判据与队伍满判据独立。反向实际WP67-A304、WP53 79/85/90、UI973–977。
3. **premises_and_counterexample**：合法Safari、单存活目标、球10、默认容量6、正常前门/资源/输入、无竞争。party1且盒全满允许10→9/刷新/投球请求；party6且盒全满拒绝、不扣/投、不进入回末；party6但一盒有位允许。放行不是捕获保证；扣球后异常没有退球/正常收编保证。
4. **minimum_revision_contract**：实际304完整写双满、拒绝重选与扣球→刷新→投球；WP53本来正确的门保留。再修订0。
5. **acceptance_and_regression**：SF01–05新核，尤其拒绝提示正常返回才重新命令、`next`跳过逃逸抽样；最后一球未捕获且决定0先球尽2而非先逃逸。Run3/Bait/Rock因子/caught4、原K17/K37/K49保持。反证“固定球图表示队伍强制六人”“构造独立容量门”“放行必捕获”均失败/被明确排除。
6. **independent_adjudication**：完整新读 bag/counterreview-R6-UI-002.json；从源和实际条款独立确认三容量控制，原报告的Demo未知没有被清零。
7. **dependencies_and_receivers**：WP53实际79/90承接双满门及Safari满队直接送盒；与普通Add-to-party UI明确分列。U13后续可能改WP53其它内容；不得用本次局部SF签名证明其候选已接收或新WP53全文通过，变更相关门/结算须重新join。

## R6-UI-PARTY-001 — ACTUAL_PASS_SCOPED_STATIC

1. **identity_and_verdict**：U10唯一/P2 required，摘要Mark合法缺槽ACTION的局部失败边界；原“非空槽清零”不足以定义缺槽，不把覆盖缺口夸成已有强断言。
2. **bidirectional_evidence**：Pokemon40–45/1159–1227，Summary117–182/290–305/1078–1231/1270–1400，SaveConversions301–312，Party705–713及StorageMark1328–1392。默认创建[]；显示缺槽0不补原值/副本；摘要用编辑副本；正常OK差异写回返回true才触发重绘。实际WP18 179、WP66-A182/184、UI985–993对齐。
3. **premises_and_counterexample**：非战斗INFO正常进入Mark、初槽0、六槽图集且至少2变体、无补齐/插件，独立ACTION对缺失值先数值比较失败，原[]保持，隐藏/返回/摘要收尾未到。显式六零为正常无动作，不和缺失槽混同。先编辑其它槽后失败也未提交标记副本。
4. **minimum_revision_contract**：WP18默认与WP66-A正常/缺槽条款及32向量中的MK01–09共同保留，行为语言没有要求未来复制源结构或永久保持缺陷。再修订0。
5. **acceptance_and_regression**：MK01–09全新核；[]USE→ACTION→BACK副本1→0后丢弃；BACK+ACTION由BACK退出、USE+ACTION只USE；OK写[1]，显式六零直接OK false。Storage直接Mark没有ACTION清零；BACK弃稿、OK提交的B17/A30保持。A35蛋Mark可达仍在；创建[]不被U14 Happiness或U01 Owner修订填齐。
6. **independent_adjudication**：counterreview-party.json完整results0新读；主动试图用显示兜底/迁移/组合键/Storage入口反证摘要失败，均只限制范围而不消除独立ACTION反例。
7. **dependencies_and_receivers**：WP18创建→Summary显示→副本→提交→页面刷新相容；普通取消与此前其它动态形态读取写入分开。R5三行确认忙门与Mark不同入口，未被此次ACTION/取消优先级推广覆盖。WP66-A132设施接收器仍PENDING_EXCLUDED。

## R6-UI-PARTY-002 — ACTUAL_PASS_SCOPED_STATIC

1. **identity_and_verdict**：U10唯一/P2 required，仅最初记录与等级候选重叠的重学排列；不新建全蛋招表/来源法定可达/Demo要求。
2. **bidirectional_evidence**：MoveRelearner全199行，Pokemon610–621/681–704，BULBASAUR PBS完整3–29，Settings147–153，Window_CommandPokemon1163–1210。先取等级≤当前且未会的首现顺序，仅独有且未会记录前置，最后身份去重，窗口保持传入顺序。反向WP30 42/170–176/230、WP66-A218/220及UI1001–1009。
3. **premises_and_counterexample**：合法非蛋非Shadow基形BULBASAUR L2、当前仅AMNESIA、更多候选开、合法记录编辑、注册/首绘正常。记录[GROWL]仍[TACKLE,GROWL]，不能搬成[GROWL,TACKLE]；记录[CURSE]才前置。重复记录仅诊断夹具，不声称正常记录链生成重复。
4. **minimum_revision_contract**：领域概括与UI概括均收窄为未会且不在等级候选；WP30原精确§6.3保持，新UI RL02补旧A31首项重叠无法区分的顺序。再修订0。
5. **acceptance_and_regression**：RL01–09全核：空/重叠/独有/重复/已会/混合/配置关；BACK拒放弃留、后确认false、无教学/统计；USE初项TACKLE成功后才统计+1/true。B16-A048空候选仍首绘严格ID ArgumentError早于输入；A21/A22 HM/满槽放弃保持；B16-A044背包TR记录/机器统计与Party入口不合并；C003旧3/2数量及来源26控制保留。反证后续窗口排序、全部记录先入去重、旧首项重叠已证明顺序均不成立。
6. **independent_adjudication**：counterreview-party.json完整results1与原完整scope新读，按固定源从合法输入重新推导，不依赖作者向量执行。
7. **dependencies_and_receivers**：WP30与U14友好度初值相邻接合没有改动重学候选；候选计算、绘制、教学提交、提醒统计各观察点分列。更多配置关不加入记录、不会自动加入完整蛋招表。U13多选接口不获本项接收签名。

## 组合、历史及排除

`fixed-validation.json` 对五实际载荷完整字节核验，与input实际身份及当前worktree吻合；U10所有原replace/insert块逐块原样存在。`candidate-to-actual.diff` 全177行已读。WP18的U01 Owner同值例外与U14 Happiness直接初值、WP30的U14受控变化范围均未触及Mark[]或重学排序。WP67-A与U10候选字节相同，但本次仍全文新读，没有以相等代替语义审。UI U10 64行完整块连续保留，U11 31行前插与U12尾17行没有丢弃32个U10向量。共享原C12/C36改写属于U12，未认领其全域裁决。

R1直接读WP66-A原139行、GROUP1-C02 22行、v3 45行；原首轮是CONTINUE_WITH_DEFERRED_FINDINGS，后续具名资格不改成全包初始PASS。WP67-A R04–R07原90–154/收尾296–305、v3全38行新读：初始0/BACK99、已拥有/持图鉴/解锁三门、逐个完整接收及普通双满门均保留。v3只签A–G具名静态范围，非媒体/宿主。

R2原B16候选`356b46b…` / 实际`29b21fe…` / 审`191e669c…`精确五元组及完整per_ID_results4/5/10新读。A044/A048为B16主责；C003是B21主责的B16局部UI贡献。R3 accepted341载荷在`469a268…`的records244/245/250完整语义资格、正常/反向/部分前缀与tuple新读；机械carrier/projection数组未声明新全文，不把同ID签成其它owner。当前A044双入口、A048空首绘、C003来源50→26与A31候选3/2均保持；旧30失败前驱仍保留。

R4 U03 actual-v1全29行新读，当前17/76与B5 16/75分开。R5原task-packet U03/findings4与U06/findings0完整新读、closing records52/67完整新读，唯一activation的全部92 selection和限制新读。旧OPEN是关闭候选生成时点；`12df95…`只选`13fddb…`原精确静态资格，92 CLOSED/0 OPEN、51 P2/41 P3不变。本次不重签全部92行为标准。Summary FURFROU严格432000/432001、强制/战斗/仓库门与HOOPA无时间戳首次用瓶0/新时间戳及正常再次1对照，已按相关固定源形态、取图、刷新、item callback链新核；实际WP18/WP66-A全文保留其原限定。三行A/B/C真实换行、最终两行、逐字、无外部恢复的确认不返回，与短文本/普通显示反向由Summary217–265/UIHelper178–274重新核；UI836–840及WP66-A244、RL08短文本门不被本次覆盖。媒体/字体/真实时间/宿主/存档/Demo未知保持。

**PENDING_EXCLUDED 的精确边界**：WP66-A132有245bytes根receiver额外载荷，U13修订`9971fe84896786645cdcda3ab45e5caf7785cabc`尚未接收/独立完成。本报告不签0/1/3人数、raw-negative、Standard-negative、第一错误/focus及nil/[]的WP66-A/WP54/设施测试联合接口；不会以45路径stable或本次WP66-A全文已读消除该pending。设施接口、U13其它路径、公共planning/audit行政同步及最终接受/关闭由root后继具名办理。

## 工具、失败与后续复验

本轮仅自写有限Git/UTF-8/JSON读送达和字节diff工具。源/Ruby/作者脚本/独立完整模型/宿主/Demo/真实save执行均0。已保存失败及截断说明在`peer-review.json`：初actual-input输出截断、旧候选报告工作树路径不存在、对象缺失与历史191e恢复前两次失败、旧helper不存在、报告范围越界、提示/联合输出截断和activation错误JSON指针。它们不算源程序执行或规范缺陷；修正后新读不改写旧失败。没有倒补未捕获原失败UTC或有效配置。

任何相关载荷改变都使受影响结论需要对新blob重验；不能仅沿用文件名、candidate PASS或本报告状态。尤其未来WP66-A单句/设施接口改动需新全文WP66-A、WP54与设施目录联合核验；未来WP53接收/结算改动需重新核Safari消费者。未变的具名blob可按准确身份复用已读事实，但新组合与传递接口不能自动继承。本文不是全group-D INTEGRATED_PASS、正式接受、最终发布或CLOSED。
