# 第一组交付摘要 — WP66-A／WP63／WP64（覆盖优先阶段）

2026-10-01；规格提取方。阶段策略见 `planning/extraction-plan.md` §2.2（用户指令：先完成剩余 16 个内容包提取，再统一 review、统一修订）。本目录为第一组（WP66-A → WP63 → WP64）交付材料，逐包追加；**第一组三包已全部完成提取与自检**。新包默认 **Drafted（提取与自检完成，待统一 review）**，不送逐包独立首审，不自标 Reviewed。

## 1. 当前完成

| 包 | 文件 | 状态 | 完整SHA-256 | 字节 | 场景 |
| --- | --- | --- | --- | --- | ---: |
| WP66-A [wp66-a-party-and-summary-ui.md](../../specs/ui/wp66-a-party-and-summary-ui.md) | 队伍与摘要界面 | Drafted | `332c5d8b7dd59d8fd78b563031c13f27bbadb361da4dd6cb54b4408344038478` | 36,649 | 35 |
| WP63 [wp63-pokegear-map-music-and-phone.md](../../specs/ui/wp63-pokegear-map-music-and-phone.md) | Pokégear、地图、音乐与电话 | Drafted | `80cdbff2b9dbb7274a123fb64f3fb3b7f5d3ac2c1545415942ca36a9a23ae859` | 26,354 | 30 |
| WP64 [wp64-mail-and-mystery-gift.md](../../specs/creature-rpg/wp64-mail-and-mystery-gift.md) | 邮件与神秘礼物 | Drafted | `51108659c4ec12cbb9e1cd7122aceb3360552e04bdadded52b5c98686a194841` | 20,598 | 26 |

矩阵增量：F16-03 新增 WP66-A Drafted 子范围段；F15-02／F15-03 各新增 WP63 Drafted 子范围段；F15-04／F15-05 各新增 WP64 Drafted 子范围段（F15-03 公共事件缺失材料部分、F15-05 真实下载与 demo 配送点部分保留 Inventoried）。

**WP66-A 进度复审（2026-10-01，`review/wp66a-progress-review-2026-10-01/`）**：CONTINUE_WITH_DEFERRED_FINDINGS——WP66-A 保持 Drafted，9 项 P2（WP66A-R01～R09）与 3 项 P3（C01～C03）进入统一修订清单，不阻止后续提取；WP63 的 FLY 返回交界已采用 WP66A-R05 查明行为（§2.3／P10）；WP64 将带入 R01（邮件取消的部分已提交变化）与 C02（快照次序为后第二名、后第一名、本人）。

## 2. WP66-A 提取范围（A～F 具名）

- A 入口与模式：暂停菜单、脚本直开、背包 Give、PC 邮箱 Give、借用选择（资格／交易／招式）、多选入场、重学；Box Link 桥（开关 35、地图旗标、持有来源）。
- B 面板／导航／选择合同：6 面板＋取消（多选双钮）、空槽跳过与回绕导航、USE／BACK／ACTION／SPECIAL 返回合同、换位置两段写入。
- C 命令菜单与成员操作：注册表构建（order／condition）、默认项与场地招插入位、奶招与秘传招（FLY 特例）、邮件命令、持物子菜单与真实写入（给予／取回／使用／移位）、内嵌背包选择（两过滤）、给予／邮件给予画面、邮件阅读、借用选择器与多选入场。
- D 摘要页面：非蛋五页（页码夹住不回绕）、蛋单页、INFO／MEMO／SKILLS／MOVES／RIBBONS 内容合同、成员切换与叫声。
- E 摘要交互：招式换位（Shadow 禁止）、缎带换位与压紧、标记编辑（变体循环／清零／仅变更才写）、选项菜单（给予／取回／图鉴／标记；蛋子集）、遗忘画面（HM 门、必选模式）。
- F 学习／替换／重学：pbLearnMove 四分支与 PP 合同（默认不保留旧 PP）、机器使用入口、Move Relearner 候选与流程（统计仅成功累加）。

自检见 [self-checks.json](self-checks.json)（来源覆盖、10 组场景定点核对、一致性／交界检查、8 处自纠记录）；固定包信息见 [wp66a-fixed.json](wp66a-fixed.json)。

## 3. WP63 提取范围（A～E 具名）

- A Pokégear 与工具入口：暂停菜单 Pokégear／Town Map 互斥条件、按钮菜单注册表（Map／Phone／Jukebox 默认项）、Map 效果的飞行链哨兵出口、`pbShowMap` 助手（wallmap 不写目的地）。
- B 区域地图：初始定位（town_map_position／区域参数／回退区域 0）、附加图与点可见性（开关门）、浏览导航夹限、编辑器模式（改名、保存确认反写 PBS）、飞行模式（ACTION 切换条件、治疗点选择与确认分层、返回 `[地图ID,x,y]` 或 nil）。
- C 点唱机：三电台曲直接播放、Custom 文件枚举与默认 BGM 覆盖、Stop 恢复地图 BGM、遭遇率旗标写入（March→higher、Lullaby→lower、其余清除）。
- D 电话数据与联系人：两类联系人字段、注册门（须 Pokégear、同键去重、重复注册置回可见并移尾）、删除（仅训练家；自开关 A 置位＋地图刷新）、排序三式＋可见优先稳定重排、列表 ACTION 实时移动与还原。
- E 呼叫与再战：信号门、呼出三门（无信号／同图／跨区）、呼入循环（帧挂钩门、20–40 分钟、同区不同图随机）、对话生成（时段问候、body 75% 拼接、版本与 [Default] 回退、battle_request 旗标 1→2 就地写入、占位符 \TN \TP \TE \TM \PN、性别着色）、再战就绪倒计时与版本推进（next_version 三项取小、reset_after_win）。

自检见 [wp63-self-checks.json](wp63-self-checks.json)（来源覆盖 16 项、10 组场景定点核对、交界检查含 WP66A-R05 复核、1 处自纠）；固定包信息见 [wp63-fixed.json](wp63-fixed.json)。

## 4. WP64 提取范围（A～F 具名）

- A 邮件数据与信箱：邮件对象五字段、快照次序（后第二名、后第一名、本人，WP66A-C02 纠正后）、信箱懒建立与容量 10。
- B 邮件流转：写信（250 字、快照、放弃无邮件对象）、两处阅读（队伍／PC，零写入）、取下两分支（存 PC／销毁）、PC 信箱三命令（Read／Move to Bag 背包满失败／Give 门）、给予链取消不回滚既有写入的部分提交事实（WP66A-R01 两条）。
- C 神秘礼物定义与载体：四元组 [id, type, item, giftname]、主文件与导出文件（Marshal+Zlib+base64、解密归一化）、示例 URL 占位。
- D 下载与候选：载入画面解锁门、HTTP 合同（200 取 body、其余按空）、按 ID 去重（含已领取标记）、接收入队（下载成功不等于领取）。
- E 领取：配送员接口（首个未领取／按 ID 查找失败）、宝可梦写入序列（personalID 重摇、命运相遇、收编失败保持未领取、图鉴分支默认开）、物品容量门与分形消息。
- F 调试 authoring：编辑（获得地／数量／查重 ID／命名与各步放弃）、创建追加、管理（在线对照、切换、编辑、接收、删除、导出）。

自检见 [wp64-self-checks.json](wp64-self-checks.json)（来源覆盖 11 项、10 组场景定点核对、交界检查含 WP66A-R01／C02／C03、1 处自纠）；固定包信息见 [wp64-fixed.json](wp64-fixed.json)。

## 5. 来源与交界

WP66-A：全文精读 `016_UI/005_UI_Party.rb`（1–1560）、`016_UI/006_UI_Summary.rb`（1–1400）、`016_UI/022_UI_MoveRelearner.rb`（1–199）、`013_Items/006_Item_Mail.rb`（1–122）；分段精读 `013_Items/001_Item_Utilities.rb` 使用／学习／给予／取回各段、暂停菜单入口、背包与 PC 的 Give 入口、场地招工具、挑战报名调用、遗迹石借用、菜单注册机制与相关设置。

WP63：全文精读 `016_UI/008_UI_Pokegear.rb`、`016_UI/009_UI_RegionMap.rb`、`016_UI/010_UI_Phone.rb`、`016_UI/011_UI_Jukebox.rb`、`013_Items/004_Item_Phone.rb`（1–706）、`010_Data/002_PBS data/021_PhoneMessage.rb`；分段精读暂停菜单 Pokégear／Town Map 入口、`016_UI/005_UI_Party.rb` FLY 段（WP66A-R05 复核）、`012_Overworld/004_Overworld_FieldMoves.rb` 飞行段、visitedMaps 写入点、电话对象初始化、菜单注册机制、pbCommonEvent、PBS `town_map.txt`／`phone.txt` 结构样本与相关设置。

WP64：全文精读 `013_Items/006_Item_Mail.rb`（1–125，含末段放弃返回）、`016_UI/024_UI_MysteryGift.rb`（1–428）；分段精读 PC 信箱画面、载入画面入口、`013_Items/001_Item_Utilities.rb` 给予／取回链（WP66A-R01 复核）、`016_UI/005_UI_Party.rb` 信箱 Give 门、HTTP 工具下载合同、玩家礼物字段与信箱初始化、图鉴设置、PBS 邮件物品样本。

交界：WP66-B／WP66-C（SPECIAL 桥、给予画面，对方已登记归 WP66-A）、WP25／WP27／WP28／WP30／WP23／WP62（领域规则引用）、WP26（脚本交易选择器与收编；GR-010 已确认待统一修订）、WP55 族（多选入场规则集）、WP24／WP11／WP59／WP36／WP13／WP04／WP08（WP63 规则引用；GR-009 语言身份注明）、WP07／WP09（WP64 的 HTTP 合同与载入画面）、WP17（消息输入原语）；WP63（WP66-A 的飞行画面）、WP64（WP66-A 的邮件模型，承接 WP66A-R01／C02）、WP67-A（战斗衔接）、WP77（demo 可达）为前向。

## 6. 未决与新增观察

- 无新增跨包编号问题；GR-001～016 中 GR-010（WP26）、GR-009（WP24）已按阶段策略读取证据并在新稿注明，不擅改旧包、不重复编号、不宣称关闭。
- WP66A-R01～R09 与 C01～C03 为 WP66-A 统一修订清单（进度复审确认）；WP63 已采用 R05 查明行为；WP64 已带入 R01／C02（并按 C03 把 Item_Mail 审计范围更正为全文 1–125）。
- 具名保留：战斗衔接（WP67-A）、公共事件电话内容与 Pokégear 授予／注册／rematch_variant 抬升等事件数据（U01）、神秘礼物真实下载与 demo 配送／解锁事件（U01／U09／WP77）、插件菜单项组合、媒体逐帧。
- N01 已于 2026-10-01 定点复审 PASS_SCOPED；其管理性回填与 WP23 头尾的 N01 子项状态更新按阶段策略留待集中收尾，本组不执行。

## 7. 登记

manifest 续第七十六轮、主 TSV 续 v51：新增 WP64 主稿、wp64-fixed.json、wp64-self-checks.json 3 行，矩阵 F15-04／F15-05 行就地更新，本摘要同步（第七十四轮登记 WP66-A 4 行、第七十五轮登记 WP63 3 行）；其余登记与历史行不动。阶段最终检查（登记对磁盘复测）按阶段策略独立保存、不登记进其描述的 manifest／TSV。
