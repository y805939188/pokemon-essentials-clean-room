# WP64 — 邮件与神秘礼物（保存／转移／候选／重复与领取）

状态：**Drafted（提取与自检完成，2026-10-01；待统一 review）**。具名范围 A～F：邮件数据与信箱（模型、快照次序、容量）；邮件流转（写信、阅读、取下、PC 信箱、给予链的部分提交事实）；神秘礼物的定义与载体（四元组、主文件／导出文件、加解密）；下载与候选（载入画面入口、去重、接收入队）；领取（配送员接口、宝可梦／物品写入序列、容量失败）；调试 authoring（编辑、创建、管理、导出）。依据 extraction-plan 的 WP64 行（邮件独立流程；礼物下载/候选/领取/重复和容量要求；WP07、WP26、WP27、WP62、WP09 为依赖）。真实下载不执行（HTTP 仅登记合同与失败语义）、示例 URL 的可访问性不作结论前提、demo 配送员事件与解锁事件属 U01／WP77。F15-04、F15-05 子范围。分类 Creature-RPG（主）、User Interface（画面）、Generic Kernel（HTTP／文件载体接点）。固定只读 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。全部为静态读取；未运行游戏、UI、网络或参考表达式。

**非目标**：不定义物品使用与给予资格（WP28）、背包容器与容量（WP27）、收编与蛋入口规则（WP26，含已确认 GR-010，本包只登记调用点）、图鉴登记规则（WP62）、HTTP 层实现（WP07，仅登记下载合同）、存档与载入画面本体（WP09）、队伍侧邮件命令与给予画面（WP66-A，WP66A-R01／C02 交界本包已采用查明行为，旧稿待统一修订）、PBS 生命周期（WP04）。

## 1. 目的、边界与可见流程

邮件是附在个体上的可写消息物品：写信时把消息与三只成员快照封存进邮件对象，可随个体持有、被取下存入 PC 信箱、从信箱取回背包或再给予成员。神秘礼物是外部分发的领取凭证：作者侧用调试功能维护主文件并导出上传；玩家侧在载入画面下载候选、选择接收后由商店配送员交付宝可梦或物品。两套产物**分开建模、互不复用状态**：邮件没有下载/领取链，神秘礼物没有信箱与写信链。

## 2. 邮件数据与信箱（A）

### 2.1 邮件对象

字段：邮件物品（决定卡片图）、消息文本、发件人名、三只快照成员 poke1／poke2／poke3。快照在**写信成功时**从队伍现场截取，每项为 `[物种, 性别, 闪光, 形态, Shadow, 蛋?]`（蛋标记仅在是蛋时追加）：**poke1＝持有者在队伍中之后第二名成员（存在时）、poke2＝之后第一名成员（存在时）、poke3＝持有者本人**（采用 WP66A-C02 纠正后的次序；WP66-A 旧稿顺序表述待统一修订）。图鉴邮件（is_icon_mail?）在阅读时按快照绘出对应图标。

### 2.2 写信

给予邮件物品时触发（WP28 给予链）：自由文本输入（至多 250 字）；**留空并确认「停止给予？」则放弃本次给予**（返回 false）；写入成功才把邮件对象挂到成员（前提：成员当前无邮件，否则为防御性异常）。快照按 §2.1 截取。写信的取消路径不产生邮件对象，但**不保证回滚调用链上已完成的其它写入**（§3.3）。

### 2.3 信箱

`$PokemonGlobal.mailbox` 懒建立（初始 nil，首次存入时建为空表）；**容量 10**：存入已满时失败（调用方显示「PC's Mailbox is full.」）。信箱保存邮件对象本身（含消息与快照），不是邮件物品。

## 3. 邮件流转（B）

### 3.1 阅读

队伍侧 Mail→Read 与 PC 信箱 Read 都打开同一阅读画面：卡片图、正文与发件人（按背景明暗配色）、图鉴邮件附加快照图标；USE／BACK 关闭，无任何写入（WP66-A 已登记画面行为，此处登记两处打开点）。

### 3.2 取下与 PC 信箱

- 队伍取下（WP66-A Mail→Take／物品 Take）：先询问「存到 PC？」——信箱未满则邮件入信箱、清空成员邮件与持物；信箱满失败保持原状；拒绝存 PC 再确认「消息将丢失」——邮件物品入背包、成员邮件与持物清空。
- PC 信箱画面（PC「Mailbox」项）：空信箱只提示「There's no Mail here.」。对每封邮件的命令：
  | 命令 | 门 | 写入 |
  | --- | --- | --- |
  | Read | 无 | 打开阅读画面（§3.1） |
  | Move to Bag | 先确认「The message will be lost. Is that OK?」 | 邮件**物品**入背包（背包满则「The Bag is full.」失败保持原状）、信箱删除该封；消息与快照随邮件对象一并丢弃 |
  | Give | 无 | 打开队伍给予画面（WP66-A）：成员已有持物或邮件→「持物中不能持邮件」；蛋→「蛋不能持邮件」；否则邮件写入成员、成员持物设为邮件物品、信箱删除该封 |
- 信箱进件唯一入口是队伍取下的「存到 PC？」分支；没有从背包直接入信的入口。

### 3.3 给予链的部分提交事实（WP66A-R01 查明行为，WP66-A 旧稿「失败保持原状」概括待统一修订）

邮件／持物给予链**不是全有全无事务**；取消写作时，调用链上已完成的写入不回滚：

1. **交换给予邮件**：成员已持普通物品 X、背包有邮件 M。给予 M → 确认交换两件 → 背包先减 M、X 入背包 → 进入写信 → 留空并确认放弃。结果：给予返回 false，**成员仍持 X，M 已回背包，而入包的 X 不回撤**——背包 X 计数净 +1（防御异常仅在 M 无法回包时）。
2. **先取邮件再给予**：成员原持邮件，给予新物品时链上先把原邮件成功存入 PC 信箱（成员邮件与持物清空）；随后新物品的写入（或新邮件的写作）被取消／失败时，**先前的信箱入库与成员清空不回滚**。

后续统一修订与 WP64 的流程描述均按此真实结果记录，不补造事务保证。

## 4. 神秘礼物：定义与载体（C）

- 礼物为四元组 `[id, type, item, giftname]`：`type==0` 为宝可梦（item 为宝可梦对象），`type>0` 为物品数量（item 为物品 ID）；id 为唯一整数（创建时 0–99,999，重复拒绝）；giftname 为显示名（至多 250 字）。
- 载体：主文件 `MysteryGiftMaster.txt`（作者侧全量）与导出文件 `MysteryGift.txt`（选中在线项导出，用于上传）。编码为 Marshal 序列化 → Zlib 压缩 → base64；**解密时物品条目经 GameData 归一化为内部 ID**（宝可梦对象原样）。配置常量 `MysteryGift::URL` 是下载地址（默认示例地址为占位；**不以示例 URL 可访问性作为任何结论前提**，WP07 的 HTTP 层另行负责）。
- 玩家侧持久：`$player.mystery_gifts`（默认空表），元素为未领取礼物（四元组）或已领取标记 `[id]`；`mystery_gift_unlocked`（默认 false）控制载入画面入口（事件解锁，U01）。

## 5. 神秘礼物：下载与候选（D）

- 入口：继续／新游戏载入画面在存档玩家 `mystery_gift_unlocked` 为真时提供「Mystery Gift」命令（WP09 画面侧），调用下载流程。
- 下载：`pbDownloadToString(URL)`——HTTP 状态 200 才取 body，异常／非 200／空一律按空串处理（WP07 合同）；空则提示「No new gifts are available.」并结束。
- 候选：解密后按 **ID 去重**——玩家 `mystery_gifts` 中已存在同 ID（无论未领取还是已领取标记）的礼物不进入候选；候选为空同样提示无新礼物。**下载成功不等于领取**：候选只进选择列表。
- 接收：逐件选择（可随时 Cancel）：宝可梦／物品图掉落动画、提示「The gift has been received!」与「Please pick up your gift from the deliveryman in any Poké Mart.」，随后**推入玩家未领取队列**（同 ID 已在队列的情形在候选阶段已被排除）；候选耗尽自动结束。

## 6. 神秘礼物：领取（E）

配送员事件接口（demo 事件属 U01）：`pbNextMysteryGiftID` 返回队列中**首个未领取**礼物的 ID（无则 0）；`pbReceiveMysteryGift(id)` 执行领取。

### 6.1 宝可梦领取（type==0）写入序列

1. 重摇 personalID（32 位随机）并重算能力（calc_stats）。
2. `timeReceived`＝当前时间；`obtain_method`＝4（命运相遇）；`record_first_moves`；`obtain_level`＝当前等级；`obtain_map`＝当前地图 ID（无地图为 0）。
3. 记录此前是否已拥有该物种（was_owned）。
4. `pbAddPokemonSilent` 收编（WP26：队伍／盒子放置规则；**失败则礼物保持未领取、返回 false**，前述字段改写留在礼物对象上——该对象仍处未领取队列，其字段在下次领取时再次被改写）。
5. 成功：消息「X received Y!」＋音效；该礼物的队列元素**改写为 `[id]`（已领取标记）**。
6. 图鉴分支（默认配置 SHOW_NEW_SPECIES_POKEDEX_ENTRY_MORE_OFTEN 开，世代 ≥7）：此前未拥有、玩家有图鉴、该物种在已解锁图鉴内——提示数据已加入，登记最近见过（WP62），并打开图鉴条目画面。

### 6.2 物品领取（type>0）写入序列

- 门：`$bag.can_add?(item, qty)`；**背包不能容纳（容量／上限）则失败，礼物保持未领取**（WP27 规则）。
- 写入：按量入背包；消息按物品形态分流：DNASPLICERS 专属格式、机器（含数量与招式名）、数量 >1 复数格式、单件按元音选择 a/an；随后队列元素改写为 `[id]`。

### 6.3 查找失败

按 ID 找不到**未领取**礼物时提示「Couldn't find an unclaimed Mystery Gift with ID X.」并 false（不改任何东西）。重复 ID 在下载候选阶段已被排除；领取阶段的 ID 语义是队列内首个未领取。

## 7. 调试 authoring（F，调试菜单）

- **编辑／创建**：宝可梦礼物先选获得地短语（Mystery Gift／Faraway place／当前 obtain_text／自定义 30 字）；物品礼物改数量（1–99,999，取消为 0 视为放弃）；ID 为 0 时分配新 ID（与主文件现有 ID 查重，重复拒绝）；再命名（≤250 字）。各步留空／取消都会询问「Stop editing this gift?」，确认则放弃返回 nil；异常兜底「Couldn't edit the gift.」。创建把礼物追加到主文件（不存在则新建）并加密写盘；取消则「Didn't create a gift.」。
- **管理**：读取主文件（无文件或空 →「There are no Mystery Gifts defined.」）＋**联网下载在线列表**（搜索提示；无在线礼物按空表）。列表逐项显示 `[X]/[ ] 在线标记、ID、名称、内容`；操作：Toggle on/offline（改在线标记集合）、Edit（§7 编辑）、Receive（有存档时把礼物替换／追加进玩家队列并立即按 §6 领取——无存档提示不能领取）、Delete（确认后从主文件删除）、Export selected to file（把在线标记的礼物导出 `MysteryGift.txt` 并提示上传）。编辑主文件的改动只在导出后影响线上。

## 8. 规则与不变量

- 邮件与神秘礼物状态不交叉：信箱只存邮件对象；神秘礼物队列只存四元组与已领取标记。
- 邮件对象只在写信成功、给予邮件入队（信箱／成员）时产生；阅读永不写入；取下两分支分别对应「保留邮件入信箱」与「销毁消息物品回包」。
- 信箱容量 10 恒成立（存入方检查）；PC 信箱 Move to Bag 受背包容量门。
- 神秘礼物按 ID 去重贯穿下载候选与领取；领取成功才改写为 `[id]`；领取失败保持未领取可重试。
- 给予邮件链的取消**不产生邮件对象但也不回滚既有写入**（§3.3 两条事实）。
- 调试 authoring 只改作者侧文件与（Receive 时）玩家队列，不影响线上数据；导出不自动上传。

## 9. 边界与失败

- 信箱满（10）：队伍取下存 PC 失败保持原状。
- 背包满：PC 信箱 Move to Bag 失败保持原状；神秘礼物物品领取失败保持未领取。
- 收编失败（pbAddPokemonSilent false，如队伍与盒子均无位）：宝可梦礼物保持未领取。
- 空信箱、无可下载（网络失败／空响应／全部已收）、候选选完、配送员按 ID 查无未领取：各有确定消息与返回。
- 无 Pokégear／无关：邮件功能与 Pokégear 无关；神秘礼物入口只看解锁标志。
- 主文件缺失／为空／解密失败（管理）：提示无已定义礼物；编辑异常兜底消息。
- 蛋：不能持邮件（给予链与信箱 Give 同门）。

## 10. 依赖与配置

- 规则引用：WP28（给予链与写信触发点）、WP27（背包 can_add? 与上限）、WP26（pbAddPokemonSilent 收编；GR-010 已确认、本包只登记调用点）、WP62（图鉴登记与条目）、WP07（pbDownloadToString／HTTP 合同）、WP09（载入画面与存档）、WP66-A（队伍邮件命令与给予画面；WP66A-R01／C02 已采用）、WP04（PBS 与文件生命周期）、WP17（消息输入）。
- 配置：`MysteryGift::URL`（占位示例地址）；`SHOW_NEW_SPECIES_POKEDEX_ENTRY_MORE_OFTEN` 默认开（世代 ≥7）；信箱容量 10；写信 250 字、获得地短语 30 字、命名 250 字、ID 0–99,999、数量 1–99,999。
- 数据：PBS `items.txt` 含 12 个邮件物品（GRASSMAIL 等，is_mail?／is_icon_mail? 数据驱动）；主文件与导出文件为 Marshal+Zlib+base64 载体。
- 持久：`$PokemonGlobal.mailbox`（懒建立）、`$player.mystery_gifts`、`mystery_gift_unlocked`。

## 11. 静态场景（输入 → 推导预期；均未运行）

| ID | 输入／前提 | 期望 |
| --- | --- | --- |
| M01 | 写信：输入 250 字内文本并确认 | 邮件对象挂到成员；快照为后第二名、后第一名、本人（存在时截取） |
| M02 | 写信：留空并确认停止 | 无邮件对象；给予返回 false；链上既有写入不回滚（§3.3） |
| M03 | 成员已有邮件再写信 | 防御性异常（前提破坏），不是正常可达路径 |
| M04 | 队伍取下邮件，信箱 9 封，确认存 PC | 邮件入信箱（10 封）、成员邮件与持物清空 |
| M05 | 同 M04 但信箱已满 10 | 「PC's Mailbox is full.」，成员邮件与持物不变 |
| M06 | 队伍取下邮件，拒绝存 PC 并确认销毁 | 邮件物品入背包、成员邮件与持物清空；信箱不变 |
| M07 | 交换给予邮件：成员持 X、背包有 M，确认交换后写作放弃 | 成员仍持 X；M 回背包；入包的 X 不回撤（背包 X 净 +1） |
| M08 | 先取邮件入 PC 成功后，新给予被取消 | 信箱入库与成员清空不回滚；后续写入未发生 |
| M09 | PC 信箱空 | 只提示「There's no Mail here.」 |
| M10 | PC 信箱 Move to Bag，背包满 | 「The Bag is full.」，邮件仍在信箱 |
| M11 | PC 信箱 Move to Bag，背包可容 | 确认后物品入包、信箱删除该封、消息与快照丢弃 |
| M12 | PC 信箱 Give 给无持物非蛋成员 | 邮件写入成员、持物设为邮件物品、信箱删除该封 |
| M13 | PC 信箱 Give 给已有持物的成员 | 「持物中不能持邮件」，信箱不变 |
| M14 | 载入画面：mystery_gift_unlocked false | 无 Mystery Gift 命令 |
| M15 | 下载：HTTP 非 200／异常／空响应 | 按「No new gifts are available.」结束，无任何写入 |
| M16 | 在线礼物 3 件，玩家队列已有同 ID 已领取标记 | 该件不进候选；其余 2 件可选 |
| M17 | 接收一件物品礼物 | 动画后两条提示；礼物推入未领取队列；未交付背包 |
| M18 | 配送员领取物品：背包 can_add? 失败 | 礼物保持未领取，false；无消息改写队列 |
| M19 | 配送员领取物品：POTION x3 | 背包 +3；复数获得消息；队列元素改写为 [id] |
| M20 | 配送员领取宝可梦 | personalID 重摇并重算；timeReceived=当前、obtain_method=4、record_first_moves、obtain_level=当前等级、obtain_map=当前地图；收编成功消息＋[id] 标记 |
| M21 | M20 中收编失败（无空位） | 礼物保持未领取、false；已改写字段留在队列中的对象上，下次领取再改写 |
| M22 | M20 且此前未拥有、有图鉴、物种在已解锁图鉴（默认配置） | 追加图鉴登记最近见过并打开条目画面 |
| M23 | pbNextMysteryGiftID：队列 [id1 已领取, gift2 未领取] | 返回 gift2 的 ID；全已领取或空队列返回 0 |
| M24 | pbReceiveMysteryGift(不存在的 ID) | 「Couldn't find an unclaimed Mystery Gift with ID X.」，false，无写入 |
| M25 | 创建礼物：ID 与主文件现有重复 | 「That ID is already used by a Mystery Gift.」，留在输入循环 |
| M26 | 管理：主文件不存在 | 「There are no Mystery Gifts defined.」，不进入管理循环 |

## 12. 未决与保留

- **WP66A-R01／C02 交界**：本包 §2.1／§3.3／M02／M07／M08 已采用查明行为（快照次序：后第二名、后第一名、本人；给予链取消不回滚既有写入）；WP66-A 旧稿相应表述待统一修订，本包不先改旧稿。
- **WP26 交界（GR-010）**：宝可梦礼物收编走 pbAddPokemonSilent；WP26 规则归属上游，GR-010 已确认待统一修订，本包不复制其旧合同。
- **网络与示例 URL**：真实下载未执行；HTTP 合同只登记到「200 取 body、其余按空」；示例地址的可访问性与线上内容不作结论。
- **demo 事件**：配送员事件、解锁事件、信箱 PC 事件属 U01／WP77；「任何 Poké Mart」提示与 demo 实际配送点未核对。
- **调试 authoring**：管理界面的在线下载同样不执行；导出文件的上传是人工步骤。
- **媒体**：卡片图、掉落动画时长、图标资源存在性未核对。

## 13. 来源与审计（traceability）

只读静态读取；行为化描述，未复制源码结构。固定 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。

- `Data/Scripts/013_Items/006_Item_Mail.rb`：全文 1–125（模型 1–17、信箱 20–32、阅读 34–97、写信 99–125，含末段放弃返回）。
- `Data/Scripts/016_UI/024_UI_MysteryGift.rb`：全文 1–428（编辑创建 17–120、管理 126–235、下载 241–326、加解密 331–349、领取 354–428）。
- `Data/Scripts/016_UI/019_UI_PC.rb:57–100,113–128`（PC 信箱画面与 PC 菜单）；`016_UI/013_UI_Load.rb:295–327`（载入画面入口与解锁门）；`013_Items/001_Item_Utilities.rb:781–860`（给予／取回链与部分提交事实复核，WP66A-R01）；`016_UI/005_UI_Party.rb:938–956`（信箱 Give 画面门）。
- `Data/Scripts/001_Technical/002_Files/003_HTTP_Utilities.rb:40–58`（下载合同）；`015_Trainers and player/004_Player.rb:34–36,54–55`（mystery_gift_unlocked 默认 false、mystery_gifts 默认空）；`012_Overworld/002_Overworld_Metadata.rb:18,71`（mailbox 懒建立）。
- 配置：`001_Settings.rb:319`（SHOW_NEW_SPECIES_POKEDEX_ENTRY_MORE_OFTEN）；PBS `items.txt` 邮件物品计数与 GRASSMAIL 样本。
- 交界登记：WP66-A 进度复审 `review/wp66a-progress-review-2026-10-01/report.md`（WP66A-R01、WP66A-C02、WP66A-C03——C03 的本文件审计范围已按全文 1–125 记录）；WP66-A 主稿队伍邮件命令与给予画面；全局 findings GR-010（WP26）。

---

本包为 **Drafted（提取与自检完成，2026-10-01；待统一 review）**；静态自检不授权把缺陷修成理想行为，也不等于独立 review 或运行通过。

### 当前依赖身份（审计绑定）

| 包 | 文件 | 完整SHA-256 | 字节 |
| --- | --- | --- | ---: |
| WP27 | `specs/creature-rpg/wp27-bag-and-item-storage.md` | `6ac234e466918123fe0382cef95829d20456522b4e17d377df31e079649a908d` | 27,602 |
| WP28 | `specs/creature-rpg/wp28-item-use-and-training.md` | `a4ccb38365521eeb130b30d9e04a281812cd03ccc76ca5443393f5fbc352d95a` | 44,159 |
| WP26 | `specs/creature-rpg/wp26-acquisition-gifts-and-script-trade.md` | `c87101adc78d2bf5d6c51fd6bb2f608fec0b2536da19d855f12cdaca79520f18` | 35,738 |
| WP62 | `specs/pokemon-rules/wp62-pokedex-records-regions-and-content.md` | `272d928378cd269e8922e975032bf651006512b328979d7e4626837dad4a2a3e` | 32,871 |
| WP07 | `specs/kernel/wp07-diagnostics-files-http.md` | `2cd5408ae9dbb1d96281057829c6bff125fdf471b2afc0e96020d105801cdbd2` | 17,398 |
| WP09 | `specs/kernel/wp09-save-startup-continue.md` | `76450356b03f11abc59808e84c7c07e0f69c3f6543aaafc9b1856b3cdf2de4e6` | 18,087 |
| WP66-A | `specs/ui/wp66-a-party-and-summary-ui.md` | `332c5d8b7dd59d8fd78b563031c13f27bbadb361da4dd6cb54b4408344038478` | 36,649 |
