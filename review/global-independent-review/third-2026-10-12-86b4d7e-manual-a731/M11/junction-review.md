# M11 交界审查（第三轮）

身份 /root/m11_world_activities_v3；固定正式 167296dbe9e2384627b0ed696e87aeb01f211252 / 33598d8a2a3acdd093cc4fe23f48eea8666100f3；参考 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b / 7589c800b61ba13a13040ed0d686979b80a84fd0。正常、失败、边界均为未执行静态判断。其它模块消费者保持具名；下面只给本模块侧支持，不代替root最终跨域裁决。

## 从源码独立得到的交界差异

- GR3-M11-001：图鉴Area按形状掩码和全部可见点的并集生成点集；Pokégear地图的游标只用形状长度，名称/详情/治疗首同格决定。M10独立读同一入口支持差异，未提同根ID；source/spec完整身份在finding中。
- 分配导航G2-5将显式播种写成挖矿：当前Mining全文仅普通随机；WP06§4和Lottery入口才有日期播种/无参重播种。不把旧导航变成正式finding。
- 分配导航G6-5的qty8/10/12→2/3/3计数不采纳：当前单株采摘成功总计+1，达到该果max才最大产量采摘计数+1；容量/取消都不加。Stats是独立累加字段，不是产量分档。
- SURF局部“面向可通行”曾列候选；WP12§5.2的“当前位置”及§3.2判定格合同已使正式集合可唯一推导当前出边，无新必修ID。

## 分配交界逐项判定

### G1-4 注册表默认契约与按类例外

判定：PARTIAL（M11消费侧静态支持；其它所有者 M01|M05|M06|M11 的全合同由其主责/root最终协调）。

正常：通用身份查询默认与Encounter版本回退、Trainer三元身份和Phone三入口各自例外分列。

失败/边界：遭遇缺请求表与缺步进表不同，不能把某类回退泛化到所有注册表。

本轮来源与当前条款：
- M11-C56；Data/Scripts/013_Items/004_Item_Phone.rb|Data/Scripts/016_UI/010_UI_Phone.rb；phone 17–113,172–190,215–316; phoneui全文 → deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md §4.1–4.3。 预检持机非强制；隐藏重注册另建；版本位置查重缺陷；文本普通新增后反馈失败，无回滚。
- M11-C58；Data/Scripts/013_Items/004_Item_Phone.rb；322–408;543–560 → deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md §5.1–5.2。 同图/异区/无信号分层；来电同名也排；NPC ID0转训练家对话失败；按标识缺公开查询先失败。
- M11-C60；Data/Scripts/013_Items/004_Item_Phone.rb；566–706 → deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md §4.5–4.6。 旧注册参数错位、reset未定义参数先失败、query0、NPC可由旧入口隐藏；不是未来API建议。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G2-1 计时来源

判定：PARTIAL（M11消费侧静态支持；其它所有者 M02|M11 的全合同由其主责/root最终协调）。

正常：宿主日期钟、累计游戏时间与运行时长分别消费；读档后的离线时间按消费者定义。

失败/边界：日期变化不等于帧循环推进；动画相位不得统一重置为场景打开时零。

本轮来源与当前条款：
- M11-C01；Data/Scripts/012_Overworld/003_Overworld_Time.rb；1–106 → deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md §3.1–3.2。 5/10/14/17/20为时段界；可传时间，缺省取宿主，不按帧推进。
- M11-C04；Data/Scripts/012_Overworld/003_Overworld_Time.rb；11–128 → deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md §3.5–3.6。 关闭返回已有缓存；非地图不写，地图室内写零；缓存钟与日历钟不同。
- M11-C25；Data/Scripts/012_Overworld/005_Overworld_Fishing.rb；74–110 → deliverables/final-specification-set/engine-overworld/wp60-fishing.md §4/§5。 期限等号继续，同轮晚输入先于超时；自动仍等输入且不抽hook。
- M11-C28；Data/Scripts/012_Overworld/006_Overworld_BerryPlants.rb；97–168 → deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md §5.1–5.2。 同秒/倒退不写；先循环扣寿命再算阶段；9重植耗尽清地，旧常规显示不推进。
- M11-C44；Data/Scripts/018_Alternate battle modes/002_BugContest.rb；28–38;237–265;301–331 → deliverables/final-specification-set/pokemon-rules/wp53-safari-and-bug-catching-contest.md §5.3–5.4。 期限≤0不expired、负仍显示00:00；单调≥门，帧推迟路线/解释器/消息；暂停微更新跨M10。
- M11-C57；Data/Scripts/013_Items/004_Item_Phone.rb；118–148;289–314;543–560 → deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md §4.4。 每墙钟变化减1，不离线追全秒；≤0重随机20–39分当次仍减1，旗标>0停；版本min上限。
- M11-C79；Data/Scripts/017_Minigames/005_Minigame_Lottery.rb|Data/Scripts/019_Utilities/001_Utilities.rb|Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb；lottery全文; utils516–522; storage388–397 → deliverables/final-specification-set/pokemon-rules/wp70-lottery.md §2–§5。 日期播种后重新播种不恢复旧序列；先队再含队储存扫描、并列保先，三变量顺序非原子。
- M11-C82；Data/Scripts/017_Minigames/006_Minigame_Mining.rb；392–527 → deliverables/final-specification-set/user-interface/wp70-mining.md §4。 损耗先加，镐/锤1/2；中心铁且≤2只削中心；占用全0才闪后登记，动画期不输入。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G2-2 离线追赶语义

判定：PARTIAL（M11消费侧静态支持；其它所有者 M02|M11 的全合同由其主责/root最终协调）。

正常：树果按小时追赶生长/耗水/重植；电话按刷新秒去重，期限到零重设20–39分钟且当次仍减一。

失败/边界：单株六小时与多株采摘统计不混同；电话菜单暂停和离线重设不同。

本轮来源与当前条款：
- M11-C28；Data/Scripts/012_Overworld/006_Overworld_BerryPlants.rb；97–168 → deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md §5.1–5.2。 同秒/倒退不写；先循环扣寿命再算阶段；9重植耗尽清地，旧常规显示不推进。
- M11-C29；Data/Scripts/012_Overworld/006_Overworld_BerryPlants.rb|Data/Scripts/010_Data/002_PBS data/007_BerryPlant.rb|PBS/berry_plants.txt；berry 83–95,147–167; berrydata 全文; PBS全文件 → deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md §3.3/§5.2–5.3/§7。 水可负、次小时才罚；新机制整数商下限；旧机制水次计数与随机域。
- M11-C57；Data/Scripts/013_Items/004_Item_Phone.rb；118–148;289–314;543–560 → deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md §4.4。 每墙钟变化减1，不离线追全秒；≤0重随机20–39分当次仍减1，旗标>0停；版本min上限。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G2-3 步进入口与计数

判定：PARTIAL（M11消费侧静态支持；其它所有者 M02|M06|M11 的全合同由其主责/root最终协调）。

正常：普通玩家、强制玩家、NPC及主动请求分入口；全局计步31位回绕，寄养256与友好128各有周期。

失败/边界：强制玩家一步的通用通知两次不能套给NPC/普通玩家；主动遭遇不等于步进机会检查。

本轮来源与当前条款：
- M11-C33；Data/Scripts/012_Overworld/001_Overworld.rb|Data/Scripts/004_Game classes/006_Game_Character.rb|Data/Scripts/004_Game classes/008_Game_Player.rb；world 169–229; character 967–989; player 539–553 → deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md §3.1–3.2。 强制实际一步完整前提两次一般通知，无全局周期；普通一次一般+31位计数，转向不计。
- M11-C34；Data/Scripts/012_Overworld/001_Overworld.rb；72–84 → deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md §4。 128及以上当次逐成员1/2，不共门；空集合仍归0；Shadow门归主责。
- M11-C35；Data/Scripts/012_Overworld/001_Overworld.rb；87–124 → deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md §5。 默认不开毒；批次一次音画，HP1清毒/HP0 faint，handled不显式终止快照。
- M11-C40；Data/Scripts/018_Alternate battle modes/001_SafariZone.rb；1–107;168–196 → deliverables/final-specification-set/pokemon-rules/wp53-safari-and-bug-catching-contest.md §3/§8.3。 重复start不清captures/decision；接待图也区域内；步负首步结束，0不计；回起点朝下不清会话。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G2-4 行走友好度

判定：PARTIAL（M11消费侧静态支持；其它所有者 M06|M11 的全合同由其主责/root最终协调）。

正常：普通步进累计达到或超过128周期→按队伍顺序逐个非空/非蛋/未濒死成员独立1/2抽样（0..1为0命中）→命中才消费成长规则基础2/2/1、正修正/封顶与Shadow阶段门→循环后计数归0。

失败/边界：127到128、两名合格成员独立抽样0/1仅第一名变化，1/0仅第二名变化；不采用共同概率门。空/全不合资格仍归0；Shadow阶段≥4即使命中也不增友好。

本轮来源与当前条款：
- M11-C34；Data/Scripts/012_Overworld/001_Overworld.rb；72–84 → deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md §4。 128及以上当次逐成员1/2，不共门；空集合仍归0；Shadow门归主责。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G2-5 显式种子与有限可重现

判定：PARTIAL（M11消费侧静态支持；其它所有者 M02|M03|M09|M11 的全合同由其主责/root最终协调）。

正常：普通随机由Mining/Tile消费；显式日期种子由Lottery生成消费，取号后重新播种。

失败/边界：Lottery无参重播种不恢复调用前序列；Mining没有显式播种。跨实现具体随机序列未证。

本轮来源与当前条款：
- M11-C79；Data/Scripts/017_Minigames/005_Minigame_Lottery.rb|Data/Scripts/019_Utilities/001_Utilities.rb|Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb；lottery全文; utils516–522; storage388–397 → deliverables/final-specification-set/pokemon-rules/wp70-lottery.md §2–§5。 日期播种后重新播种不恢复旧序列；先队再含队储存扫描、并列保先，三变量顺序非原子。
- M11-C81；Data/Scripts/017_Minigames/006_Minigame_Mining.rb；233–390 → deliverables/final-specification-set/user-interface/wp70-mining.md §3。 普通随机，无播种；物品外500含拒绝、坐标内无上限，铁外500；130格独立厚度分布。
- M11-C85；Data/Scripts/017_Minigames/007_Minigame_TilePuzzles.rb；189–238;363–479 → deliverables/final-specification-set/user-interface/wp71-tile-puzzles.md §5/§8/§9。 3末空漏扫，偶宽奇高反转；6非方形坏列端点；默认6五个4循环奇，7固定奇交数非完成。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G2-6 读档/暂停推进

判定：PARTIAL（M11消费侧静态支持；其它所有者 M02|M11 的全合同由其主责/root最终协调）。

正常：帧消费者须实际得到更新机会；菜单/战斗/消息/强制路线/解释器的电话守卫分别暂停倒计时。

失败/边界：宿主日期继续变化不自动推进所有帧驱动业务；捕虫期限独立。

本轮来源与当前条款：
- M11-C44；Data/Scripts/018_Alternate battle modes/002_BugContest.rb；28–38;237–265;301–331 → deliverables/final-specification-set/pokemon-rules/wp53-safari-and-bug-catching-contest.md §5.3–5.4。 期限≤0不expired、负仍显示00:00；单调≥门，帧推迟路线/解释器/消息；暂停微更新跨M10。
- M11-C57；Data/Scripts/013_Items/004_Item_Phone.rb；118–148;289–314;543–560 → deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md §4.4。 每墙钟变化减1，不离线追全秒；≤0重随机20–39分当次仍减1，旗标>0停；版本min上限。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G2-8 世界天气显示管线

判定：PARTIAL（M11消费侧静态支持；其它所有者 M03|M11 的全合同由其主责/root最终协调）。

正常：世界天气意图、显示粒子/渐变/色调/闪光与战斗天气身份分层；进入通知先要求旧图存在且异图→按元数据/概率求新类型（缺字段/失败为None）→同类型跳过、仅类型改变局部写power9/duration0。合法连接边缘在进入通知后独立写duration20；显式转移重建无此连接后写。

失败/边界：Rain/duration7异图又得Rain：显式重建保留7，合法连接才后写20；同图/旧图0不重掷。类型变更无连接局部0，有连接最终20；正在渐变守卫不打断，类型同仅强度改不刷新。20是名义单位、正值只选择固定渐变，不是20秒；TIME_SHADING/户外门不扩到outdoorlight。

本轮来源与当前条款：
- M11-C06；Data/Scripts/012_Overworld/001_Overworld.rb|Data/Scripts/004_Game classes/005_Game_MapFactory.rb|Data/Scripts/010_Data/002_PBS data/018_MapMetadata.rb|Data/Scripts/021_Compiler/001_Compiler.rb；world 253–265; factory 95–111; schema 41; syntax 95–149 → deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md §4.2–4.3。 同图/旧图0不重掷；同类型不写；连接最后20不是20秒。
- M11-C07；Data/Scripts/012_Overworld/001_Overworld visuals/001_Overworld_Weather.rb|Data/Scripts/005_Sprites/006_Spriteset_Global.rb|Data/Scripts/004_Game classes/001_Game_Screen.rb；weather 54–113,329–506; globaldisplay 33–55; screen 66–70 → deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md §4.4–4.5。 正时长只选固定渐变；在途不打断，意图单改强度不触发显示刷新。
- M11-C08；Data/Scripts/012_Overworld/001_Overworld visuals/001_Overworld_Weather.rb；210–315;404–430;488–506 → deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md §4.1特殊显示参数。 水花重置可见后隐藏再显示；风暴稳定才闪；太阳允许相位越界。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G3-1 捕获唯一主规格

判定：PARTIAL（M11消费侧静态支持；其它所有者 M04|M05|M06|M11 的全合同由其主责/root最终协调）。

正常：投球登记扣减先于动作；捕获成功更新图鉴/拥有/接收；满队选择替换和送盒分别处理。

失败/边界：登记后失败不退球；全满兜底在消息缺陷处失败，不保证撤销已提交字段。

本轮来源与当前条款：
- M11-C42；Data/Scripts/011_Battle/008_Other battle types/001_SafariBattle.rb|Data/Scripts/018_Alternate battle modes/001_SafariZone.rb；safbattle 344–364,420–453; safstate 118–160 → deliverables/final-specification-set/pokemon-rules/wp53-safari-and-bug-catching-contest.md §4.1/4.5–4.6。 会话→战斗预算后再回写；返回整数；无internalBattle包装不登记，但Mixin独立拥有写入跨M05。
- M11-C48；Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb；1–275 → deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md §2–§4。 守卫未知不写、登记未知失败；首写/最近覆盖、原形态与展示名门不同；形态计数只0/1。
- M11-C64；Data/Scripts/016_UI/024_UI_MysteryGift.rb；361–428 → deliverables/final-specification-set/creature-rpg/wp64-mail-and-mystery-gift.md §6。 个体先改PID/时间来源等再收编，失败保队列已改值；物品预检后消息再[id]；图鉴提示后追加。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G3-4 图鉴写入门与公开清理

判定：PARTIAL（M11消费侧静态支持；其它所有者 M05|M06|M09|M11 的全合同由其主责/root最终协调）。

正常：战斗侧仅捕获写拥有，获得侧九入口分别写；静默入队可只写拥有。整体清理清记录后刷新，保留区域解锁。

失败/边界：击倒不写拥有；最近见到覆盖与禁止刷新参数是独立入口。

本轮来源与当前条款：
- M11-C48；Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb；1–275 → deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md §2–§4。 守卫未知不写、登记未知失败；首写/最近覆盖、原形态与展示名门不同；形态计数只0/1。
- M11-C49；Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb|Data/Scripts/019_Utilities/001_Utilities.rb|Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb|Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb|PBS/regional_dexes.txt；dex 279–361; utils 380–422; misc 28–35; compiler 593–633; PBS全文件 → deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md §5.1–5.2。 全国短路、当前区域模式不查锁；成员nil导致数据遍历失败，UI独立回退；两区顺序全文结构读。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G3-5 给予链部分提交

判定：PARTIAL（M11消费侧静态支持；其它所有者 M05|M10|M11 的全合同由其主责/root最终协调）。

正常：持物/邮件给予先完成对应容量检查及已提交入库/清空，再进入后续选择。

失败/边界：后续取消/失败不回滚先前邮件入库和清空；交换取消保持各自先写的实际结果。

本轮来源与当前条款：
- M11-C61；Data/Scripts/013_Items/006_Item_Mail.rb；全文 → deliverables/final-specification-set/creature-rpg/wp64-mail-and-mystery-gift.md §2–§3。 250字空重问；快照后2/后1/本人；信箱10，不复制已有信；下游给予取消部分提交M05/M10。
- M11-C64；Data/Scripts/016_UI/024_UI_MysteryGift.rb；361–428 → deliverables/final-specification-set/creature-rpg/wp64-mail-and-mystery-gift.md §6。 个体先改PID/时间来源等再收编，失败保队列已改值；物品预检后消息再[id]；图鉴提示后追加。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G4-4 Shadow 状态

判定：PARTIAL（M11消费侧静态支持；其它所有者 M04|M06|M11 的全合同由其主责/root最终协调）。

正常：Shadow标志、量表、Hyper和暂存状态独立；量表0仍Shadow，HP到0清Hyper，净化按入口恢复。

失败/边界：再次建立Shadow不是幂等；可选Shadow备份启用仍U06，不能变成默认行为。

本轮来源与当前条款：
- M11-C36；Data/Scripts/012_Overworld/001_Overworld.rb；5–29 → deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md §6。 首门原队含蛋；内部扣非蛋感染期，跨多天只一次，未来日期也扣；个体编码/传播跨M04/M09未全重审。
- M11-C48；Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb；1–275 → deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md §2–§4。 守卫未知不写、登记未知失败；首写/最近覆盖、原形态与展示名门不同；形态计数只0/1。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G4-8 形态提交副作用链

判定：PARTIAL（M11消费侧静态支持；其它所有者 M04|M06|M11 的全合同由其主责/root最终协调）。

正常：正常形态提交写形态→清缓存→处理器→重算→有玩家登记；带提示入口在写入后让出；简单写入省略处理器/缓存/登记。

失败/边界：学习放弃/蛋或Shadow拒绝不回滚形态；同形态ROTOM已有唯一目标招仍可能删到0；战斗专招PP按新总PP夹限。

本轮来源与当前条款：
- M11-C48；Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb；1–275 → deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md §2–§4。 守卫未知不写、登记未知失败；首写/最近覆盖、原形态与展示名门不同；形态计数只0/1。
- M11-C51；Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb|PBS/pokemon_forms.txt；dexentry154–200,446–484; PBS2058–2066样本 → deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md §6.1。 非0无名/重定向拒，全部显示不绕结构门；同图性别折叠、nil/空串标签不同；BACK不恢复。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G5-3 进化提交主流程

判定：PARTIAL（M11消费侧静态支持；其它所有者 M05|M06|M10|M11 的全合同由其主责/root最终协调）。

正常：阻止、取消、成功三路；成功按统计及身份/能力/图鉴/招式/收尾固定序列交接呈现。

失败/边界：呈现失败不自动把先前提交改成事务；兼容物种/道具身份不能净化成泛称。

本轮来源与当前条款：
- M11-C48；Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb；1–275 → deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md §2–§4。 守卫未知不写、登记未知失败；首写/最近覆盖、原形态与展示名门不同；形态计数只0/1。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G5-4 孵化提交

判定：PARTIAL（M11消费侧静态支持；其它所有者 M06|M10|M11 的全合同由其主责/root最终协调）。

正常：队伍孵化先核心写入后演出；图鉴写入及动态形态读取各有门，多蛋按队伍顺序。

失败/边界：演出动态形态读取可有提交副作用；未执行演出不意味着核心孵化未发生。

本轮来源与当前条款：
- M11-C48；Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb；1–275 → deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md §2–§4。 守卫未知不写、登记未知失败；首写/最近覆盖、原形态与展示名门不同；形态计数只0/1。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G6-4 小游戏支付/结算与代币

判定：PARTIAL（M11消费侧静态支持；其它所有者 M02|M05|M11 的全合同由其主责/root最终协调）。

正常：卡片买先余额/容量/添加后扣款，卖先加钱后删卡；老虎机场景信用额到结算写回；挖矿逐件入包；拼图返回布尔。

失败/边界：加钱夹满仍删卡；挖矿工具不扣背包；拼图奖励属于缺失外部事件，不能推有奖励。

本轮来源与当前条款：
- M11-C68；Data/Scripts/017_Minigames/002_Minigame_TripleTriad.rb；634–645;725–758;974–1041;1294–1300 → deliverables/final-specification-set/creature-rpg/wp68-triple-triad.md §3–§4。 每槽999跨槽；预检不写，直接添加可部分；对局重填副本不是原样槽复制，永久不改。
- M11-C71；Data/Scripts/017_Minigames/002_Minigame_TripleTriad.rb；869–944 → deliverables/final-specification-set/creature-rpg/wp68-triple-triad.md §6。 prize胜覆盖noprize，direct败反复扣随机候选末身份/预设nil；忽略部分返回不回滚。
- M11-C72；Data/Scripts/017_Minigames/002_Minigame_TripleTriad.rb；1048–1290 → deliverables/final-specification-set/creature-rpg/wp68-triple-triad.md §7。 买预检添加后扣钱，卖先加钱再删，钱满仍删；不至少留5，正常视野回滚不异常保证。
- M11-C75；Data/Scripts/017_Minigames/003_Minigame_SlotMachine.rb；198–273;313–326;404–414;442–456 → deliverables/final-specification-set/user-interface/wp69-slot-machine.md §1/§5–§6。 全局0检查非本地0；支付tick未更新每帧最多1，满/USE清；离场才写净差，不事务。
- M11-C78；Data/Scripts/017_Minigames/004_Minigame_VoltorbFlip.rb；390–525;695–705 → deliverables/final-specification-set/pokemon-rules/wp69-voltorb-flip.md §1/§4–§6。 免费0币可入，实际增量coins_won；2–8级倒置clamp在展示后清分前失败；已奖不撤回。
- M11-C83；Data/Scripts/017_Minigames/006_Minigame_Mining.rb；529–620 → deliverables/final-specification-set/user-interface/wp70-mining.md §5–§6。 临界击先登记后坍塌；放弃也领已揭，逐件入包失败继续；列表不清重复直接领可重复。
- M11-C86；Data/Scripts/017_Minigames/007_Minigame_TilePuzzles.rb；242–490;503–608 → deliverables/final-specification-set/user-interface/wp71-tile-puzzles.md §3–§4/§6/§9。 方向repeat按优先Up覆盖等，未完成BACKfalse，完成等新USE/BACKtrue；表外也消费公共完成；不发奖励。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G6-5 树果产量与背包容积

判定：PARTIAL（M11消费侧静态支持；其它所有者 M02|M05|M11 的全合同由其主责/root最终协调）。

正常：单株采摘确认且整量容量过后，总采摘+1；qty≥该果最大产量时最大产量采摘另+1。

失败/边界：拒绝/容量不足均不加；直接产量查询不加统计；一株qty8/10/12各只使总采摘+1，不按产量分档累计。

本轮来源与当前条款：
- M11-C29；Data/Scripts/012_Overworld/006_Overworld_BerryPlants.rb|Data/Scripts/010_Data/002_PBS data/007_BerryPlant.rb|PBS/berry_plants.txt；berry 83–95,147–167; berrydata 全文; PBS全文件 → deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md §3.3/§5.2–5.3/§7。 水可负、次小时才罚；新机制整数商下限；旧机制水次计数与随机域。
- M11-C32；Data/Scripts/012_Overworld/006_Overworld_BerryPlants.rb|Data/Scripts/004_Game classes/012_Game_Stats.rb；berry 437–471; stats 21,92–93 → deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md §6.4。 确认和整量容量过才总采摘+1；达到该果max另+1；先A再外层reset，直接工具不清植物。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G7-1 交互合同主责任与消费者处置（v4 收尾）

判定：PARTIAL（M11消费侧静态支持；其它所有者 M03|M05|M10|M11 的全合同由其主责/root最终协调）。

正常：消息/选项/数量/按键由主规格定义，集合内4及外5消费者分别引用；取消负值/零/正数各有含义。

失败/边界：空数组与nil不同；源方法标识只作审计，取消不能统一为false，暂停符与本地化占位符不同。

本轮来源与当前条款：
- M11-C25；Data/Scripts/012_Overworld/005_Overworld_Fishing.rb；74–110 → deliverables/final-specification-set/engine-overworld/wp60-fishing.md §4/§5。 期限等号继续，同轮晚输入先于超时；自动仍等输入且不抽hook。
- M11-C44；Data/Scripts/018_Alternate battle modes/002_BugContest.rb；28–38;237–265;301–331 → deliverables/final-specification-set/pokemon-rules/wp53-safari-and-bug-catching-contest.md §5.3–5.4。 期限≤0不expired、负仍显示00:00；单调≥门，帧推迟路线/解释器/消息；暂停微更新跨M10。
- M11-C56；Data/Scripts/013_Items/004_Item_Phone.rb|Data/Scripts/016_UI/010_UI_Phone.rb；phone 17–113,172–190,215–316; phoneui全文 → deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md §4.1–4.3。 预检持机非强制；隐藏重注册另建；版本位置查重缺陷；文本普通新增后反馈失败，无回滚。
- M11-C66；Data/Scripts/017_Minigames/001_Minigame_Duel.rb；全文 → deliverables/final-specification-set/user-interface/wp68-duel.md §2–§6。 10命、特殊各一次、3:4:4:2权重，玩家0优先判负；BACK无退出，速度正常恢复方向固定不恢复旧值。
- M11-C86；Data/Scripts/017_Minigames/007_Minigame_TilePuzzles.rb；242–490;503–608 → deliverables/final-specification-set/user-interface/wp71-tile-puzzles.md §3–§4/§6/§9。 方向repeat按优先Up覆盖等，未完成BACKfalse，完成等新USE/BACKtrue；表外也消费公共完成；不发奖励。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G7-4 错误阶段与失败分层

判定：PARTIAL（M11消费侧静态支持；其它所有者 M01|M02|M03|M11|M12 的全合同由其主责/root最终协调）。

正常：下载、文件、编辑器校验、资源选择、编译、插件及转换按入口各自定义异常阶段。

失败/边界：阶段1失败阻止阶段2，但不撤销已写文件；没有执行下载/编译/转换或宿主异常画面。 整个路线脚本求值异常先于任何行首判定/索引推进；其它行有前缀不抵消异常。

本轮来源与当前条款：
- M11-C55；Data/Scripts/016_UI/011_UI_Jukebox.rb|Data/Scripts/012_Overworld/001_Overworld.rb；music全文; world238–250 → deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md §6/§8。 Custom缺目录失败、空USE清覆盖；March不清覆盖；跨图率旗标清而覆盖保留。
- M11-C62；Data/Scripts/016_UI/024_UI_MysteryGift.rb；1–121;331–350 → deliverables/final-specification-set/creature-rpg/wp64-mail-and-mystery-gift.md §4–§5。 编码序列化压缩base64；空输入[]，非空错误无本地保护；不下载或反序列化载荷。
- M11-C65；Data/Scripts/016_UI/024_UI_MysteryGift.rb；17–237 → deliverables/final-specification-set/creature-rpg/wp64-mail-and-mystery-gift.md §7。 Create主文件、Export导出，Edit/Delete不主文件；Receive后编辑取消可改已入队对象；未发生在线上传。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G8-1 插件/扩展机制主责任与消费者处置（v4 收尾）

判定：PARTIAL（M11消费侧静态支持；其它所有者 M01|M02|M04|M06|M10|M11|M12 的全合同由其主责/root最终协调）。

正常：插件早于编译检查；编译检查调试门不阻止发布消费预编译插件。候选物种通知与生成完成通知分开。

失败/边界：普通步进候选通知早于允许遭遇门；主动请求通知后仍可空候选退出。WP21自身形态登记不当作WP05事件消费；真实插件组合仍未知。

本轮来源与当前条款：
- M11-C33；Data/Scripts/012_Overworld/001_Overworld.rb|Data/Scripts/004_Game classes/006_Game_Character.rb|Data/Scripts/004_Game classes/008_Game_Player.rb；world 169–229; character 967–989; player 539–553 → deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md §3.1–3.2。 强制实际一步完整前提两次一般通知，无全局周期；普通一次一般+31位计数，转向不计。
- M11-C53；Data/Scripts/016_UI/008_UI_Pokegear.rb；全文 → deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md §2。 三按钮按可用项，BACK-1，Map有目的地整体结束；Phone/Jukebox假留循环，扩展实际组合未证。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G8-4 调试直接写入 vs 领域所有权

判定：PARTIAL（M11消费侧静态支持；其它所有者 M02|M11|M12 的全合同由其主责/root最终协调）。

正常：调试直接写入按非默认入口描述；原状态、即时刷新请求与持久保存的先后保留。

失败/边界：表达式语法失败可能发生在翻槽后/刷新前；不把调试行为当普通领域守卫或推宿主最终收口。

本轮来源与当前条款：
- M11-C37；Data/Scripts/012_Overworld/001_Overworld.rb；38–59;128–149 → deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md §3.2。 放电≤600秒或≤15%；菜单抑制不锁存；NPC/无袋也擦第一煤灰层，资源受门与夹限。
- M11-C44；Data/Scripts/018_Alternate battle modes/002_BugContest.rb；28–38;237–265;301–331 → deliverables/final-specification-set/pokemon-rules/wp53-safari-and-bug-catching-contest.md §5.3–5.4。 期限≤0不expired、负仍显示00:00；单调≥门，帧推迟路线/解释器/消息；暂停微更新跨M10。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G9-2 WP77 引用合同 vs WP11–17/WP36/WP61/WP63/WP64 当前声明

判定：PARTIAL（M11消费侧静态支持；其它所有者 M03|M06|M11|M12 的全合同由其主责/root最终协调）。

正常：Demo配置引用当前主合同；Home是失败回程而非系统起始点；开关51/52读取已存在，置位事件未知。

失败/边界：平衡等级消费有界先求平衡级再−4加0–4夹限；配置样本不证明实际地图事件启用。

本轮来源与当前条款：
- M11-C39；Data/Scripts/012_Overworld/001_Overworld.rb|Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb|Data/Scripts/012_Overworld/001_Overworld visuals/003_Overworld_MapTransitionAnims.rb；world 238–250,602–634; field 251–289,853–885; cave 67–76 → deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md|deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md §7.1;§5.8。 中心记录/healingSpot/escapePoint不可合并；前者正常事件实际调用缺失。
- M11-C55；Data/Scripts/016_UI/011_UI_Jukebox.rb|Data/Scripts/012_Overworld/001_Overworld.rb；music全文; world238–250 → deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md §6/§8。 Custom缺目录失败、空USE清覆盖；March不清覆盖；跨图率旗标清而覆盖保留。
- M11-C58；Data/Scripts/013_Items/004_Item_Phone.rb；322–408;543–560 → deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md §5.1–5.2。 同图/异区/无信号分层；来电同名也排；NPC ID0转训练家对话失败；按标识缺公开查询先失败。
- M11-C65；Data/Scripts/016_UI/024_UI_MysteryGift.rb；17–237 → deliverables/final-specification-set/creature-rpg/wp64-mail-and-mystery-gift.md §7。 Create主文件、Export导出，Edit/Delete不主文件；Receive后编辑取消可改已入队对象；未发生在线上传。
- M11-C87；Data/Scripts/001_Settings.rb|PBS/map_metadata.txt|PBS/encounters.txt|PBS/town_map.txt|PBS/phone.txt；设置/配置样本；缺地图/Audio/Graphics/Plugins/Game.ini → deliverables/final-specification-set/pokemon-rules/wp53-safari-and-bug-catching-contest.md|deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md|deliverables/final-specification-set/engine-overworld/wp60-fishing.md|deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md|deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md|deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md|deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md|deliverables/final-specification-set/creature-rpg/wp64-mail-and-mystery-gift.md|deliverables/final-specification-set/creature-rpg/wp68-triple-triad.md|deliverables/final-specification-set/user-interface/wp68-duel.md|deliverables/final-specification-set/pokemon-rules/wp69-voltorb-flip.md|deliverables/final-specification-set/user-interface/wp69-slot-machine.md|deliverables/final-specification-set/pokemon-rules/wp70-lottery.md|deliverables/final-specification-set/user-interface/wp70-mining.md|deliverables/final-specification-set/user-interface/wp71-tile-puzzles.md 各末节未知与scope。 配置证明参数/旗标/引用，不证明授予、接待、费用、奖励、电话登记或媒体/插件运行；须补素材和宿主。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### G9-5 场地能力资格 vs 地形/通行

判定：PARTIAL（M11消费侧静态支持；其它所有者 M03|M04|M05|M11 的全合同由其主责/root最终协调）。

正常：场地技能徽章/功能/队伍招式及朝向/地形/载具资格分门，效果与取消各自定义。

失败/边界：FLY成功前提和SPLASH句保留；直接FLASH效果与外层资格不同，不泛化所有地形行为。

本轮来源与当前条款：
- M11-C09；Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb；4–65 → deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md §5.1–5.2。 12可用族需资格与效果；只有DIG/TELEPORT另有分派确认，DEBUG不放宽快捷收集。
- M11-C18；Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb；685–786 → deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md §5.3 SURF行;§5.4–5.8。 菜单当前位置出边与目标水标签；状态/计数先于前跳，无跳失败回滚；步后清底座。
- M11-C21；Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb；890–969 → deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md §5.3 WATERFALL行;§5.4–5.8。 向上且瀑布/瀑顶才启用；右向菜单效果true仍不启动；下瀑/离开步后恢复。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### CHAIN-2 生命周期/时间/步进

判定：PARTIAL（M11消费侧静态支持；其它所有者 M02|M06|M10|M11 的全合同由其主责/root最终协调）。

正常：交换计数先于校验；寄养周期/领取生成/队伍孵化分入口；强制玩家一步通用通知两次，各周期/概率由消费者定义；单株果实量更新统计。；行走友好达128后逐可战成员独立1/2抽样，命中再消费成长/Shadow门，循环后计数归0；不采用共同概率门。

失败/边界：NPC及普通玩家不一律两次；多株不替代单株qty；核心孵化与演出动态形态读取可见提交分开。

本轮来源与当前条款：
- M11-C25；Data/Scripts/012_Overworld/005_Overworld_Fishing.rb；74–110 → deliverables/final-specification-set/engine-overworld/wp60-fishing.md §4/§5。 期限等号继续，同轮晚输入先于超时；自动仍等输入且不抽hook。
- M11-C28；Data/Scripts/012_Overworld/006_Overworld_BerryPlants.rb；97–168 → deliverables/final-specification-set/pokemon-rules/wp60-berry-plants.md §5.1–5.2。 同秒/倒退不写；先循环扣寿命再算阶段；9重植耗尽清地，旧常规显示不推进。
- M11-C33；Data/Scripts/012_Overworld/001_Overworld.rb|Data/Scripts/004_Game classes/006_Game_Character.rb|Data/Scripts/004_Game classes/008_Game_Player.rb；world 169–229; character 967–989; player 539–553 → deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md §3.1–3.2。 强制实际一步完整前提两次一般通知，无全局周期；普通一次一般+31位计数，转向不计。
- M11-C34；Data/Scripts/012_Overworld/001_Overworld.rb；72–84 → deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md §4。 128及以上当次逐成员1/2，不共门；空集合仍归0；Shadow门归主责。
- M11-C36；Data/Scripts/012_Overworld/001_Overworld.rb；5–29 → deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md §6。 首门原队含蛋；内部扣非蛋感染期，跨多天只一次，未来日期也扣；个体编码/传播跨M04/M09未全重审。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### CHAIN-3 道具/库存/UI

判定：PARTIAL（M11消费侧静态支持；其它所有者 M05|M06|M10|M11 的全合同由其主责/root最终协调）。

正常：有限两槽P999/997买3失败回退只恢复总量，槽分布可变997/999；邮件先取下入包后取消保留先写；BoxLink缩队后旧索引写入再局部失败；空重学初绘失败。

失败/边界：默认无限不冒充两槽向量；交换后仍持Y；失败不改成全事务回滚；BP显示与实际值同步门保留。

本轮来源与当前条款：
- M11-C61；Data/Scripts/013_Items/006_Item_Mail.rb；全文 → deliverables/final-specification-set/creature-rpg/wp64-mail-and-mystery-gift.md §2–§3。 250字空重问；快照后2/后1/本人；信箱10，不复制已有信；下游给予取消部分提交M05/M10。
- M11-C64；Data/Scripts/016_UI/024_UI_MysteryGift.rb；361–428 → deliverables/final-specification-set/creature-rpg/wp64-mail-and-mystery-gift.md §6。 个体先改PID/时间来源等再收编，失败保队列已改值；物品预检后消息再[id]；图鉴提示后追加。
- M11-C83；Data/Scripts/017_Minigames/006_Minigame_Mining.rb；529–620 → deliverables/final-specification-set/user-interface/wp70-mining.md §5–§6。 临界击先登记后坍塌；放弃也领已揭，逐件入包失败继续；列表不清重复直接领可重复。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### CHAIN-5 形态/Shadow/成长

判定：PARTIAL（M11消费侧静态支持；其它所有者 M04|M05|M06|M10|M11 的全合同由其主责/root最终协调）。

正常：形态写入先于交互学习，学习拒绝不回滚；ROTOM同形态且唯一目标招仍可能删到0；Shadow量表0仍Shadow，香门friendship255，储存HARDY90/LONELY130分列。；Shadow四文本已读样本字段/131量表与招式样本全集由WP23附表§3承接，U06实际启用未知；Gen5–8未读备份仍仅存在性。

失败/边界：默认普通经验消息关闭，直接helper显式消息可先提示后被阶段门拒绝；可选备份U06未证，不把G0或friendship与阶段概念混用。

本轮来源与当前条款：
- M11-C36；Data/Scripts/012_Overworld/001_Overworld.rb；5–29 → deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md §6。 首门原队含蛋；内部扣非蛋感染期，跨多天只一次，未来日期也扣；个体编码/传播跨M04/M09未全重审。
- M11-C48；Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb；1–275 → deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md §2–§4。 守卫未知不写、登记未知失败；首写/最近覆盖、原形态与展示名门不同；形态计数只0/1。
- M11-C51；Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb|PBS/pokemon_forms.txt；dexentry154–200,446–484; PBS2058–2066样本 → deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md §6.1。 非0无名/重定向拒，全部显示不绕结构门；同图性别折叠、nil/空串标签不同；BACK不恢复。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

### CHAIN-8 世界显示/时序/目标几何

判定：PARTIAL（M11消费侧静态支持；其它所有者 M03|M05|M07|M10|M11 的全合同由其主责/root最终协调）。

正常：34世界场景分族保留；飞行先于消息/outdoorlight不受TIME_SHADING户外门/计时负业务值显示0；暂停初显0后全局相位，预览两个周期；选曲与播放/等待/返回清预置分工。；天气先旧图存在/异图门和类型不同门才局部0，合法连接独立后写20；同类型显式重建保持旧duration，同图不重掷，正在渐变/强度单改守卫保留。

失败/边界：零时长即时插值不取消在途任务；99998计时/动画排序各自独立。NearAlly正常三席存活远位可初选登记但执行拒绝；无存活非自身同侧才回自身。

本轮来源与当前条款：
- M11-C06；Data/Scripts/012_Overworld/001_Overworld.rb|Data/Scripts/004_Game classes/005_Game_MapFactory.rb|Data/Scripts/010_Data/002_PBS data/018_MapMetadata.rb|Data/Scripts/021_Compiler/001_Compiler.rb；world 253–265; factory 95–111; schema 41; syntax 95–149 → deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md §4.2–4.3。 同图/旧图0不重掷；同类型不写；连接最后20不是20秒。
- M11-C07；Data/Scripts/012_Overworld/001_Overworld visuals/001_Overworld_Weather.rb|Data/Scripts/005_Sprites/006_Spriteset_Global.rb|Data/Scripts/004_Game classes/001_Game_Screen.rb；weather 54–113,329–506; globaldisplay 33–55; screen 66–70 → deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md §4.4–4.5。 正时长只选固定渐变；在途不打断，意图单改强度不触发显示刷新。
- M11-C08；Data/Scripts/012_Overworld/001_Overworld visuals/001_Overworld_Weather.rb；210–315;404–430;488–506 → deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md §4.1特殊显示参数。 水花重置可见后隐藏再显示；风暴稳定才闪；太阳允许相位越界。
- M11-C14；Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb；457–513 → deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md §5.3 FLY行;§5.4–5.8。 目的地空拒绝；内部无个体清D false被外层忽略；回调异常保留已转移和未清E/D。
- M11-C22；Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb|Data/Scripts/012_Overworld/001_Overworld visuals/003_Overworld_MapTransitionAnims.rb|Data/Scripts/012_Overworld/001_Overworld.rb；field 69–172; cave 1–76; world 602–626 → deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md §5.6/5.8。 共同演出无个体false，洞穴先写/清点；15层延迟，恢复请求不保证完成。
- M11-C33；Data/Scripts/012_Overworld/001_Overworld.rb|Data/Scripts/004_Game classes/006_Game_Character.rb|Data/Scripts/004_Game classes/008_Game_Player.rb；world 169–229; character 967–989; player 539–553 → deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md §3.1–3.2。 强制实际一步完整前提两次一般通知，无全局周期；普通一次一般+31位计数，转向不计。

限制：素材/地图/真实事件/宿主执行0；其它域的深层算法未由本模块重新全读，不沿历史标题或PASS裁全链。

