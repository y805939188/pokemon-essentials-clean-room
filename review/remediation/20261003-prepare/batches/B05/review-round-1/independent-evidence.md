# R-B05 独立证据与首判

在阅读 `author/`、`author-v2/` 的自检结论之前写成。被审对象为 `1914cd379bcb7c8b6feb13dc3e872b7ded27d9a4` 的完整 15 正式文件，比较起点 `0a12de641542f9a59909d2a950c1de8df17ca09d`；不是仅审 v1 的后继差异。首判 **PASS_SCOPED**，新增缺陷 0。各项仅批准 B05 贡献，均未关闭原 finding。

以下 S 证据均在独立 Git `/workspace/b05-reference` 的固定提交 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 只读核对。完整输入身份、原对象校验及表比较见 [独立静态核对](independent-static-validation.json)。没有运行参考、模拟回调、装载编译数据或执行行为向量；反例结果是带前提的静态判断。

| 原 ID / 原统一严重度 | 本批范围与验收 | 独立反例及相邻对照 | 真实证据 | 剩余待办 |
| --- | --- | --- | --- | --- |
| GIR-FD82-A020 / P2 | WP19 原 §3.5、净化 §3.5；全 25 Nature 与逐步取整；ST60–63。通过。 | 5 中性、20 修正。BULBASAUR L50、IV31/EV0：中性 120/69/69/85/85/65；LONELY 攻75防62；BRAVE 速58；ADAMANT 特攻76。独立中间值105的正/负修正为115/94，不能四舍五入。 | S01/S02；原稿与净化的25行均逐行一致。 | B07/WP28 扩展消费点；B01贡献保持。 |
| GIR-FD82-A021 / P3 | WP18 原/净化默认字段、CI-25。通过。 | 直接登记物种，form=2且省略 PokédexForm 得2；名称Unnamed，分类/图鉴文本???；unmega/message=0、后缀空字符串、配置数组空。不是全部未知字段统一为空，也不以编译器默认替代直接登记。原六能力标准化条款保留。 | S03；WP18默认表。 | integration身份核验；无本批修订。 |
| GIR-FD82-A022 / P2 | WP18 原 §4.2/§9与净化创建入口；CI-26–28。通过。 | 普通创建有IV/PID随机，UNOWN另取0–27，PUMPKABOO/GOURGEIST另按5/15/45/35%选择。withMoves=false不走该创建回调；已给非零形态不走形态0复检。随机结果0仍可同值提交及图鉴登记。动态读取的同值早退不能推广至裸提交。既有Nature缓存前提保留。 | S04/S05；原§8旧句未改，批准§9明确限定该旧句。 | integration；不新增默认创建随机来源的全域量词。 |
| GIR-FD82-A023 / P2 | WP20 原/净化整表与四槽入口、HP-35–37。通过。 | 直接5项表保持5；新学LEER只删首项一次仍5；已知GROWL移动原对象到末尾，PP7/up1保留；首招记录、复制保持5及重复。reset默认才限最多4；正常交互满槽门另论。旧HP-14/15与共享成长行保留。 | S06。 | integration；不能登记全局列表四项不变量。 |
| GIR-FD82-A024 / P3 | WP20 原/净化重学候选与开关、HP-40/41。通过。 | BULBASAUR L5已知TACKLE/GROWL/VINEWHIP、首招空：AMNESIA虽可兼容且在蛋/教学表，却不因此成为重学候选。记录AMNESIA后，开首招重学得到AMNESIA，关则候选空；有记录时资格查询不据该开关变假。空首招/已无遗漏等级招则资格假。 | S06/S07；PBS BULBASAUR1–20。 | B07/WP30完整重学消费点。 |
| GIR-FD82-A025 / P3 | WP20 原/净化负索引；HP-38/39。通过。 | 两招TACKLE/GROWL：-1删GROWL，-2删TACKLE；-3或2无变化。空表不删。调试选择取消-1在调用者早退，不能据此否定直接负索引的合法删除。 | S06/S08。 | integration；维持直接入口与UI取消区分。 |
| GIR-FD82-A026 / P2 | WP21 原/净化六族具名映射与数据门，FM15/20及FM36–43。通过。 | ROTOM五形态招与THUNDERSHOCK保底顺序；KYUREM目标缺失跳过、已掌握归零目标时删/即时压缩可跳后项；白→黑不直接改白专招。NECROZMA旧/新≥3不改；CALYREX归0按基础等级/教学/蛋表剔除，不设当前等级门。后两族新增解析失败早于蛋/Shadow门，前序形态/删除不回滚。ZACIAN/ZAMAZENTA入战需持物且目标登记；终战反改IRONHEAD不需持物，缺数据失败时该槽原标识保留。普通NECROZMA0→1新SUNSTEELSTRIKE PP5/up0；直改保留up并钳PP。 | S09/S10/S11；默认SUNSTEELSTRIKE TotalPP=5（PBS/moves.txt:8016–8022）。 | B07/WP28完整道具链扩展；不登记全部道具/战斗刷新通过。 |
| GIR-FD82-A027 / P2 | WP21 原/净化同值删除、FM40/41，保留FM13/14的PP对照。通过。 | 普通非蛋非Shadow、形态1且唯一OVERHEAT，裸提交再写1：先有有效目标，随后因已掌握取消新增，删除唯一招，最终形态1/零招，无THUNDERSHOCK。CATALOG同值选择外层拒绝，原招保留。仅“最初无有效目标、找到旧专招且总数1”才走保底。 | S09/S10；原有效二审FS01/CF01限定相同。 | integration；零招不得修成更合理的保底。 |
| GIR-FD82-A028 / P2 | WP22 Mega石身份与附表、ME26。通过。 | BANETTE形态0持BANETTITE对应目标1；无持物/不匹配不触发。此为查询数据，不能代替战斗Mega许可。48条条件/六能力逐项核对；固定参考的METAGROSS异于通常认知的数值仍保留；正确原Mega表字节不改。 | S12/S13；Mega48逐行无差异。 | integration；不扩大为Mega/Primal全部退出链重审。 |
| GIR-FD82-A029 / P2 | WP23正文/附表h255、SH47/48/51。通过。 | 有效可选香、普通非蛋存活Shadow、M4000/G0/h255：H0、有效Hyper假；共用工具失败、野外不消费、战斗资格拒绝；战斗登记后到此状态则执行前拒绝/退还。仅改h254、默认软上限关闭无修正则成功至h255/G0且正常野外消费。G0存储Hyper真也无“先清有效Hyper”绕过。 | S14/S15；正确原h255文字保留。 | integration；可选样本无Scent旗标、默认未启用限制保留。 |
| GIR-FD82-A030 / P2 | WP23可选131配置、18招/4物品、SH50。通过。 | GROWLITHE M4000，SHADOWBLITZ/SHADOWWAVE；SNORUNT M2500，SHADOWWAVE/SHADOWSHED。全部131条量表与有序招式逐项一致；18招效果身份、类型及4物品字段核对；四者没有Flags，不能因描述为香就补Scent旗标。 | S16；正确原131表字节不改。 | 实际安装/编译/运行具名未知保留，不能记默认已启用。 |
| GIR-FD82-A031 / P3 | WP23正文/附表、原W06；SH06/49/52。通过。 | 存储HARDY、M4000/G2500/H4/h80，JOYSCENT倍率1：先H4拦友好，降90→2410/H4/h80。只改LONELY：降130→2370/H3/h80，不跨阶段追补友好；计算性格覆盖不替代存储性格。25行下降表不改。 | S14/S17及独立固定算术。 | integration；不把HARDY当默认100下降。 |
| GIR-FD82-A040 / P2 | WP19合法EV writer边界及设施具体反例；ST67，保留ST56–59。通过。 | CATERPIE设施模板第5行、L50/IV31/E510：HP/ATK各255、总510；能力计算读取各floor(255/4)=63，不把存储改252。药剂/战斗/训练家等合规写者不因此失去既有局部门；4项分摊508不补尾数。 | S18/S02；PBS/battle_tower_pokemon.txt:5。 | B07/WP28局部量词；B17/WP76调试/演示表述；本批不能全域关闭。 |
| GIR-FD82-A044 / P2 | WP20通用教学与记录边界、HP-42/43。通过。 | TM57以真实FieldUse=TR判定（CHARGEBEAM）；MAGNEMITE L5、初始TACKLE/首招TACKLE：包内教学成功追加首招，队伍直接道具教会且消费TR但不追加；忘掉后前者可作为首招重学，后者不可。取消/拒绝不记录，通用教会不自动记录。WP66-A已有正确区别不能说全部缺失。 | S19/S07；PBS/items.txt:4654–4664、pokemon.txt:2125–2153。 | B07/WP30成长消费点；B16/WP66-A边界/统计验收。 |
| GIR-FD82-C124 / P2 | WP19Characteristic数据与算法、ST64–66。通过。 | 固定轮为HP/ATK/DEF/SPEED/SPA/SPD；从PID mod6首位找原始IV最高并列首项，再取所选原始IV mod5。六项31时PID3选速度、PID4选特攻；原始ATK31/SPEED30而Speed最大化旗标真，仍选ATK。完整30语义由正文给出，显示本地化另论。 | S20；原有效case限定已读；全30语义及邻近最大化规则保留。 | B16/WP66-A显示/本地化与UI贡献。 |
| GIR-FD82-C126 / P2 | WP20零招合法状态、HP-44/45。通过。 | withMoves=false、清空或ROTOM同值删除可为零招。摘要MOVES基础四格绘制可成立；USE进入首招详情在读缺对象的display_damage处先失败，早于BACK循环。事件/直接遗忘首招详情同边界。普通通用教学零招能新增TACKLE满PP/up0。不能统一补一招或说一切MOVES操作都失败。 | S21/S11；有效case限定保留。 | B16/WP66-A完整UI入口/失败贡献。 |

## 证据定位

这些路径与行区间用于回查，不复制参考程序。行号均在上述固定参考提交。

- S01 `Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb:30–176`。
- S02 `Data/Scripts/014_Pokemon/001_Pokemon.rb:470–530,1080–1125`；`PBS/pokemon.txt:1–20`。
- S03 `Data/Scripts/010_Data/002_PBS data/008_Species.rb:175–235`。
- S04 `Data/Scripts/014_Pokemon/001_Pokemon.rb:125–200,1138–1228`。
- S05 `Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb:140–155,445–465`。
- S06 `Data/Scripts/014_Pokemon/001_Pokemon.rb:29–52,605–727,1135–1149`。
- S07 `Data/Scripts/016_UI/022_UI_MoveRelearner.rb:150–170`；`Data/Scripts/001_Settings.rb:140–154`。
- S08 `Data/Scripts/020_Debug/003_Debug menus/007_Debug_PokemonCommands.rb:473–483`。
- S09 `Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb:221–270,330–390,562–590,650–735`。
- S10 `Data/Scripts/013_Items/002_Item_Effects.rb:1232–1268`。
- S11 `Data/Scripts/014_Pokemon/004_Pokemon_Move.rb:1–125`；`Data/Scripts/013_Items/001_Item_Utilities.rb:582–630`。
- S12 `Data/Scripts/014_Pokemon/002_Pokemon_MegaEvolution.rb:1–40`。
- S13 `PBS/pokemon_forms.txt` 全部 Mega 条件节；`PBS/items.txt` MegaStone身份集合；BANETTE节955–963、BANETTITE节2798–2806。
- S14 `Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:226–325`。
- S15 `Data/Scripts/011_Battle/001_Battle/006_Battle_ActionUseItem.rb:87–106`；`Data/Scripts/013_Items/001_Item_Utilities.rb:672–688,774–789`。
- S16 `PBS/Shadow Pokémon backup/shadow_pokemon.txt` 全131配置节；`moves_shadow_pkmn.txt` 全18效果字段；`items_shadow_pkmn.txt` 全4物品字段；`types_shadow_pkmn.txt`。
- S17 `Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb:1–180`。
- S18 `Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb:114–140,201–218`；`Data/Scripts/013_Items/001_Item_Utilities.rb:400–425`。
- S19 `Data/Scripts/019_Utilities/002_Utilities_Pokemon.rb:450–490`；`Data/Scripts/013_Items/002_Item_Effects.rb:75–94`；`Data/Scripts/013_Items/001_Item_Utilities.rb:710–756`。
- S20 `Data/Scripts/016_UI/006_UI_Summary.rb:590–641`。
- S21 同摘要文件 `180–208,692–742,814–850,929–942,1280–1291,1380–1410`。

## 有效限定与跨批验收

原16对象、`current_qualifications`、root裁决、二审/扩展、原验收均按原ID保留。独立静态清单逐对象证明准备验收字段与原对象相等；完整原对象的规范化散列保留。A020/A026的WP28扩展、A044的WP30/WP66-A边界、C124/C126的有效case均不缩为标题结论。原二审A的FS01–FS05、C的CF01–CF06限定也读取；其中净化室跨级先失败、Shadow复制共享、普通经验消息关闭等正确现有条款与测试仍保持，不将其重开为新问题。

B07/B16/B17未完成的消费点属于原问题剩余范围，不能靠本批通过关闭。所有ID尚须 actual integration 新SHA的受影响核验，再交唯一登记者；跨域ID还须全部贡献和最终Ultra门。公共登记只能提交建议。U01–U10、G01–G12、AX01–AX20及具名未知保留；运行观察0、demo证明链0、行为向量执行0。
