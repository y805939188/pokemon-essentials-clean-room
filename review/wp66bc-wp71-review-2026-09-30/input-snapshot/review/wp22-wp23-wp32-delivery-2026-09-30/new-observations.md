# 本批具名观察与首审处理记录（提取方）

2026-09-30首审后同步。WP22／WP32已获限定PASS_SCOPED并管理回填；WP23按R01～R03修订v2经有限复审PASS_SCOPED并管理回填。本文件记录独立报告§3的判定与提取方实际处理，不自行批准修订。首稿观察文件 `6646dde258a08f030e0a91274dedeb94906e6a9706ceb321f1f0179138aeb1bf`（4,620字节）保存在本轮input-snapshot；旧声明留史，当前适用结论如下。

## WP32-N01：要害计数不限制敌方目标

- 旧稿：`specs/pokemon-rules/wp31-basic-evolution.md`，完整SHA-256 `0b40917c3a0c9b942f004dd5fb6bc75addf749d154e162e75e06a2f001806d91`，39,554字节，第114行条件摘要写“该成员对对方造成的要害打击次数”。
- 新证据：`Data/Scripts/011_Battle/003_Move/002_Move_Usage.rb:294–304`只检查使用者属玩家、记录槽存在和本击critical；没有目标阵营门；替身路径不早退，画皮／结冻头才早退。直接调用者`011_Battle/002_Battler/007_Battler_UseMove.rb:669–675`逐非unaffected目标调用，也没有敌方限制。
- 影响：限定为敌方会漏记对友方／替身的要害；本场多击／多目标不是一招一次。新稿WP32§3.2与W10／W11按实际写入域描述。
- **CONFIRMED，已按授权实际同步**：只改WP31§3.4旧第114行目标范围摘要并加单点维护尾注，当前完整身份 `8ea81dcefff940ff6232db1268cc908a8dd6f1d344070786ec8e411dd74ac155`（40,087字节）。基础阈值、进化提交／取消及旧关闭编号不变；真正引用其完整身份的WP23／WP32及活动绑定已级联。上条旧完整身份与原句是同步前历史。

## WP32-N02：交换图鉴页和外层包装均调用收尾

- 旧交界：`specs/creature-rpg/wp26-acquisition-gifts-and-script-trade.md`，完整SHA-256 `c87101adc78d2bf5d6c51fd6bb2f608fec0b2536da19d855f12cdaca79520f18`，35,738字节，第108–117行描述交换演出后检查／替换；未对两收尾点作完整承诺，本观察是补充而非重判已审规则。
- 新证据：Trading:157–168收尾含交换进化检查；199–209的条件图鉴展示在页内调用收尾；236–242外层仍再次调用。MessageConfig:514–519释放并清空精灵表；第二次无消息窗口，但Trading:161再次直接释放viewport。
- 影响：两个业务检查调用位置没有一次性标记。宿主允许重复释放并继续时，第二次检查读已经变化的收到者，可对自定义连续交换条目再次命中；第二次能否抵达及实际结果未经运行验证。
- **CONFIRMED_STATIC／RETAIN_RUNTIME**：保持WP32§6.3和W35的条件化结论；第二次viewport释放能否继续仍为宿主未决。未改WP26，不宣称必然双进化、必然异常或运行确认。

## WP23-O01～O06：本包新范围内的非理想结果

这些是原来前向范围的新增提取，不是旧规则已获批准的修订。位置和输入场景已在WP23主稿列明。

| 编号 | 观察 | 源定位（均相对Data/Scripts） | 场景 |
| --- | --- | --- | --- |
| WP23-O01 | TIMEFLUTE非零量表门与统一净化零量表门不相交；符合普通用物门时可消费但不净化 | `014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb:17–18,277–284`；`013_Items/001_Item_Utilities.rb:674–686,743–747` | W25／W26 |
| WP23-O02 | 可选香数据没有Scent旗标，有效Hyper时常规前门拒；处理器自身可清Hyper不代表可达 | 同上Shadow辅助:170–176、248–324；ActionUseItem:18–22；Item:131–134,187；`PBS/Shadow Pokémon backup/items_shadow_pkmn.txt` | W27 |
| WP23-O03 | 取出时盒全满但队伍有位，双满门不拦；直接入盒失败后仍清源；最终净化领取在**确实到达存放**后双满拒绝仍清中心；跨级恢复可能按R01更早失败而保留中心 | `016_UI/023_UI_PurifyChamber.rb:474–487,570–584`；Storage:231–251；UtilitiesPokemon:4–5,17–30 | W37／W38 |
| WP23-O04 | 替换比较Shadow查询**原始返回值相等**（nil与false不相等），没有普通放置的蛋／最后可战斗成员门；蛋例要求原始返回值匹配 | Chamber:361–405,497–507；UIStorage:1964–2023 | W33／W34 |
| WP23-O05 | 捕获左移等级／K／D但不左移战前心量表，战后提示可能错配 | Catch:47–59；Shadow辅助:419–435 | W40；WP32§5 |
| WP23-O06 | 个体复制的暂存EV表没有新建容器，可共享改动；招式标识记录列表另外复制 | ShadowPokemon:212–220；Pokemon:1133–1150 | W41 |

## WP22-O01：默认METAGROSS形态数据的HP差异

`PBS/pokemon_forms.txt:1004–1009`与`PBS/pokemon.txt:9943–9954`给出Mega HP基础值95、基础形态80。50级IV／EV0时最大HP140→155，当前70→85，解除后140／70。它符合WP19已审重算合同，没有发现旧规则冲突。仅作为固定数据观察，不能用官方系列常识覆盖，也不授权修正参考数据。

独立判定：WP22-O01、WP23-O01／O02／O05／O06与WP32-N01为CONFIRMED；O03为CONFIRMED但保留到达前提；O04原为PARTIALLY_CONFIRMED，现按R02修为原始结果相等（修订已经有限复审通过）；N02为CONFIRMED_STATIC／RETAIN_RUNTIME。R01新增净化室跨级失败、R03默认G0写标志／提示已同步主稿与场景；不是再增加旧观察编号或重开旧关闭项。统一有限复审材料由用户转交，未发送reviewer消息。
