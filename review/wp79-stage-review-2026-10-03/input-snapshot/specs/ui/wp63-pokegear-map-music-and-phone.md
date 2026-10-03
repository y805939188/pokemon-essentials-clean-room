# WP63 — Pokégear、区域地图、点唱机与电话（工具入口／旅行目标／联系人再战生命周期）

状态：**ReviewPending（修订 v3，2026-10-01；WP63-R01／R05／R07 残留与 GROUP1-C01／C02 同步补修完成，待定点复审）**。具名范围 A～E：Pokégear 与地图工具入口（含飞行链）；区域地图（浏览、点信息、飞行选择、编辑器模式）；点唱机（曲目、默认 BGM 覆盖与遭遇率旗标）；电话数据与联系人生命周期（注册、删除、排序、可见性）；呼叫与再战（呼出门、呼入循环、对话生成、再战就绪与版本推进）。依据 extraction-plan 的 WP63 行（地图选择/旅行入口、音乐操作、联系人/电话/再战；WP24、WP11、WP59、WP17 为依赖）。宿主运行／媒体逐帧／demo 事件可达性与插件组合保留。F15-02、F15-03 子范围。分类 User Interface（主）、Creature-RPG（电话与再战）、Engine / Overworld Integration（地图元数据与事件自开关接点）。固定只读 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。全部为静态读取；未运行游戏、UI 或参考表达式。

**非目标**：不定义训练家版本数据、队伍与语言来源（WP24；语言身份见 GR-009 注明）；不定义地图拓扑／元数据字段与玩家转移（WP11／WP12）；不定义场地招资格、飞行执行与转移（WP59，pbCanFly?／pbFlyToNewLocation 只登记调用点）；不定义遭遇生成与遭遇率旗标消费（WP36）；不定义时间系统与统计字段（WP06）；不定义消息与输入原语（WP17）；不定义公共事件机制（WP13）；不重新定义队伍界面 FLY 调用方行为（WP66-A，含已确认 WP66A-R05，本包 §2.3 采用其查明结果）；不评估媒体资源存在性与 demo 事件内容（U01／WP77）。

## 1. 目的、边界与可见流程

Pokégear 是玩家持有的一件工具入口：打开后给出 Map／Phone／Jukebox 三个功能按钮（默认注册集合，可由插件扩展）。区域地图既从这里打开，也由「Town Map」物品（无 Pokégear 时）与队伍 FLY（WP66-A）打开；地图可以仅浏览，也可以在满足条件时选择飞行目的地。点唱机改写当前背景音乐与遭遇率旗标。电话系统管理联系人（训练家与公共事件 NPC）的登记、可见性、排序与再战就绪，并产生来去电对话。

## 2. Pokégear 与工具入口（A）

### 2.1 入口

| 入口 | 条件 | 行为 |
| --- | --- | --- |
| 暂停菜单「Pokégear」 | 玩家 `has_pokegear`（默认 false，由事件授予，demo 授予点为 U01 范围） | 打开 Pokégear 按钮画面；返回后若有飞行目的地则结束暂停菜单并执行飞行（WP59），否则刷新暂停菜单 |
| 暂停菜单「Town Map」 | **无** Pokégear 且背包含 TOWNMAP（与上一项互斥） | 直接打开区域地图（§3）；选定飞行点后同样经飞行链执行 |
| 脚本助手 | `pbShowMap(region, wallmap)` | 打开区域地图；**wallmap 模式不写飞行目的地**（浏览模式不写，非 wallmap 且选定才写） |

### 2.2 Pokégear 按钮画面

- 按钮由 `:pokegear_menu` 注册表生成（order 排序、condition 求值；默认：Map 10、Phone 20、Jukebox 30）。按钮纵列居中；UP／DOWN 回绕移动（多于一项才播游标音）；BACK 返回 -1 关闭；USE 执行该项效果。
- 效果返回假时回到按钮循环（Phone／Jukebox 均如此）；**Map 效果选定飞行目的地时**：写 `$game_temp.fly_destination`、销毁按钮画面并返回哨兵值结束整个 Pokégear；随后由暂停菜单入口检查目的地并进入飞行链。
- Phone 入口的「需有联系人」条件在注册表中**被注释停用**：按钮总出现；打开后无可见联系人时只提示「There are no phone numbers stored.」并直接返回（§4.1）。
- 按钮与背景按玩家性别选用 `_f` 变体图（资源存在时）。

### 2.3 队伍 FLY 调用方交界（采用 WP66A-R05 查明结果）

队伍界面（WP66-A）对可用 FLY 的成员确认后，关闭队伍界面并以飞行模式打开区域地图（§3.4）：选定治疗点则写飞行目的地并整体返回 `[成员, FLY]` 进入飞行链；**取消（BACK）时不写任何目的地**，但调用方重建队伍界面时**未携带本次的存储访问许可且选中位重置为面板 0**——即本次会话的 Box Link 桥在返回后失效，SPECIAL 提示消失，直至整个队伍界面退出重开才重新按三条件计算（已确认 WP66A-R05；WP66-A 已同步修订为 v3，两稿一致；本包只登记地图侧合同与该交界事实）。飞行处理器的另一面：飞行目的地为空时执行处理器直接失败（「You can't use that here.」）。

## 3. 区域地图（B）

### 3.1 打开与初始定位

打开参数：区域（-1＝跟随当前位置）、wallmap（墙面展示模式）、飞行模式（直接以飞行选择打开）、编辑器（$DEBUG 时启用）。初始定位：当前地图元数据有 `town_map_position` 时定位到该区域的对应格（配置了 `town_map_size` 时按玩家坐标折算子格偏移）；指定区域参数且与当前不同且存在时定位该区域左上角；无定位元数据时回退到区域 0 的左上角。**区域查询是严格的（WP63-R07）**：未定义的区域 ID（含回退目标区域 0 未定义、当前位置指向未定义区域）在进入自定义提示分支前先抛「Unknown ID」错误；「The map data cannot be found.」的友好提示仅在其实际可达前提（定位数据对象为空而非未知 ID）出现，不能当作未知区域的恢复保证。玩家图标仅当显示区域与当前区域一致时按当前位置绘制。

### 3.2 显示合同

- 底栏：区域名、游标处地点名、游标处详情（按点数据；名称与详情文本经消息哈希本地化；编辑器模式显示原始键）。
- 附加图：REGION_MAP_EXTRAS 注册的叠加图（默认 2 项隐藏地点）：wallmap 模式按其「墙面可见」旗标显示；普通模式按其开关号显示。
- 治疗点（飞行点）：浏览全部已访问地图对应点，**图标仅在飞行选择模式（mode 1）显示**；`visitedMaps` 在玩家进入地图时写入（WP11 侧）。
- 点可见性：带开关字段（point[7]）的点在 wallmap 模式一律隐藏名称／详情／治疗点；普通模式须开关置位才可见。

### 3.3 浏览与编辑

- 方向输入按 8 向折算 ±1 格移动，夹到网格边界（0..29 × 0..19），游标平滑滚动；底栏地点／详情随游标即时刷新。
- BACK：普通模式直接关闭返回 nil；编辑器模式**仅在已有改动时**先询问「Save changes?」（确认则保存区域数据并反写 PBS，WP04 侧）再询问「Exit from the map?」——**进入编辑器未作修改就按 BACK 会直接退出、无任何询问**（WP63-C02）。
- 编辑器（$DEBUG 经普通入口开启）：USE 对当前格编辑地点名（自由文本至多 250 字；新点追加、旧点改写），未保存的改动按上述确认写盘。

### 3.4 飞行选择

- 模式进入：飞行模式打开即 mode 1；普通浏览中 ACTION 可切换 mode 0↔1（条件：`CAN_FLY_FROM_TOWN_MAP` 默认 true、非 wallmap、非飞行模式打开、`pbCanFly?` 通过——WP59 规则：徽章、队伍持 FLY（调试豁免）、无跟随者、户外地图）。
- 选择（mode 1 中 USE）：游标位于治疗点且（该点地图已访问 或 调试＋CTRL）时——**飞行模式打开的直接返回该治疗点**（无确认）；浏览中切换进 mode 1 的先确认「Would you like to use Fly to go to X?」再返回。返回值为 `[地图ID, x, y]`；BACK 返回 nil，不写飞行目的地。
- 目的地消费：写入 `$game_temp.fly_destination` 后由 WP59 的飞行执行消费（消息、统计 fly_count、转移、清除逃生点、清空目的地）；无 FLY 成员（非调试）在执行点改为清空目的地并失败。

## 4. 电话：数据与联系人生命周期（D）

### 4.1 电话画面

- 打开前置：存在至少一个可见联系人才进入画面，否则仅提示「There are no phone numbers stored.」。
- 画面：联系人列表（仅可见者）、信号图标（当前地图元数据无 `NoPhoneSignal` 旗标为有信号）、注册数与待再战数统计、联系人头像（训练家按训练家类型行走图、公共事件联系人按 `phoneNNN` 图）、所在地图名、再战就绪图标（仅再战启用时，逐行按 `can_rematch?` 显示）。
- 列表操作：USE 选中打开命令菜单；BACK 关闭。ACTION 进入移动模式后**游标移动即实时重排底层联系人数组**（随游标逐位移动），USE／ACTION 落定，BACK 还原到起始位置。

### 4.2 联系人数据（全局持久，随存档）

两类联系人：**训练家**（地图 ID、事件 ID、训练家类型、名字、版本数、起始版本、当前版本＝最后被击败的版本、就绪倒计时、再战旗标 0／1／2、可选公共事件 ID）与**公共事件 NPC**（地图 ID、名字、公共事件 ID）。所有联系人带可见标志（默认可见）；`rematch_variant`（全局再战版本上限，默认 0）与 `rematches_enabled`（默认由设置给出，默认 false）为电话对象级状态。显示名：训练家为「类型名＋消息名」，NPC 为本地化名字（语言与消息文件相关；训练家语言来源编号属 WP24 已确认事项 GR-009，界面语言与训练家／拥有者语言身份不混同）。

### 4.3 注册、删除与排序

**预检与写入入口分开（WP63-R01）**：`can_add?` 是**可选预检**（须持 Pokégear；训练家类型存在；同键尚无可见联系人）——事件脚本通常先用它决定是否提供注册，但**写入入口 `Phone.add／add_silent` 自身不调用该预检**：脚本不经预检直接注册时，即使玩家未持 Pokégear 也会实际新增可见联系人。**「无强制预检」不等于没有守卫**：两个训练家注册分支仍保留**训练家类型存在性检查**（未知类型返回 false、不新增），NPC 直调则可无 Pokégear 写入。同理，电话画面的打开只检查可见联系人是否为空，没有持工具门；只有正常暂停菜单入口被 `has_pokegear` 挡住（§2.1）。

| 操作 | 门 | 写入与反馈 |
| --- | --- | --- |
| 注册 `Phone.add` | 无强制预检（训练家类型存在性检查仍保留，见上） | 已有**可见**同键联系人：置回可见并移到可见组尾；否则新建（训练家版本＝起始版本、倒计时 0、旗标 0）。成功后可见优先重排，并播注册音效消息「Registered X in the Pokégear!」；`add_silent` 省略显式消息（音效消息在 `Phone.add` 包装内）。**查重只匹配可见联系人（WP63-R02）**：对**已隐藏**的同键联系人再注册，不会恢复旧对象（其版本进度随旧对象保持隐藏），而是**另建一个可见联系人**。另具名参考缺陷：按事件注册的查重调用把「版本数」位置当作起始版本查询，却按真实起始版本创建——用相同「版本数 3、起始版本 0」参数连续直接注册两次，两次都会新增同起始版本联系人 |
| 删除（画面 Delete 命令） | 仅训练家联系人可删（NPC 不可） | 确认后 `visible=false`：训练家联系人同时清倒计时与再战旗标、**将其地图事件的自开关 A 置位**并请求地图刷新（事件回到登记前页，WP13 侧）；随后可见优先重排、提示已删除；删光后提示无联系人并关闭画面 |
| 排序（Sort Contacts） | 画面命令 | 三式：按内部 name、按显示名 display_name、特殊联系人（NPC）优先；每式排序后再做**可见优先稳定重排**（组内保留刚排的相对顺序）并刷新 |
| 重排（列表 ACTION） | 见 §4.1 | 实时移动底层数组；BACK 还原 |

### 4.4 再战就绪与版本推进

- 就绪倒计时（WP63-R05 查明）：再战启用时，每秒（系统秒变化时）对可见训练家联系人处理：旗标 >0 **跳过**；倒计时 ≤0 时**重新随机 20–39 分钟（整数分钟，40 取不到）**并**当次仍减 1**（如随机 20 分钟 → 本次结束为 1199 秒），否则每秒减 1；减到 0 时旗标置 1，并把其地图事件自开关 **A 复位、B 置位**（事件切到再战页）＋请求地图刷新。**旗标变 1 后倒计时停在 0、不再重新随机**（每秒因旗标 >0 跳过），直到胜利重置等外部操作。
- 版本推进：联系人 `next_version = 起始版本 + min(variant+1, 全局 rematch_variant, 版本数-1)`（variant＝当前版本−起始版本）；`Phone.battle` 以 next_version 启动训练家战斗（WP24）；`reset_after_win`（胜利后调用）：当前版本推进到 next_version、再战旗标清 0、倒计时清 0（下轮就绪循环重新随机）。
- **全局上限默认 0**：`rematch_variant` 默认 0，脚本须自行抬高（Phone.rematch_variant=）才允许更高再战版本；本包不声明 demo 中的实际抬升点（U01）。

### 4.5 事件脚本接口与弃用族

可用入口按**调用形态**分列（WP63-R03／R04 查明）：

- **对象级正确路径**：`Phone.can_add?／add／add_silent／battle／reset_after_win`、`Phone::Call.make_incoming`、联系人的 `next_version／increment_version／variant`；`Phone::Call.make_outgoing(联系人对象)`（电话 UI 的用法——直接传入联系人对象，跳过查找，正常走 §5.1 呼出门）。
- **按标识呼出的缺陷路径**：`Phone::Call.make_outgoing(类型, 名字[, 起始版本])` 的分支会调用一个**固定脚本中并不存在的类级 `Phone.get`**——在信号／距离门**之前**即发生未定义方法错误（本地异常，不是 nil 返回）；事件按标识呼出的实际可达性留 WP77。
- **公开版本查询／递增包装的缺陷路径**：`Phone.variant(类型, 名字, 起始版本)` 与 `Phone.increment_version(...)` 把训练家类型传入实例查询的**布尔标志位**，无法匹配任何正常联系人——查询恒返回 0、递增无动作。**编译器生成的再战事件页确实使用 `Phone.variant(...)` 条件**（连同 `Phone.battle(...)`／`Phone.reset_after_win(...)`），即生成事件携带这一缺陷（WP13／WP24 侧的消费关系登记；正确算法是联系人对象级的 `next_version` 与 `increment_version`、`reset_after_win`）。
- 旧 `pbPhoneRegister*`／`pbPhoneDeleteContact`／`pbHasPhoneTrainer?`／`pbPhoneReadyToBattle?`／`pbPhoneBattleCount` 等一族为 v22 弃用包装，**多条指向上述缺失或失配的入口**；本包只登记其转发关系与缺陷边界，不以「转发」暗示功能必然可用。

## 5. 电话：呼叫与对话（E）

### 5.1 信号与呼出门

- 信号：当前地图元数据有 `NoPhoneSignal` 旗标时不能拨打（画面信号图标同步显示无信号）。
- 呼出门（玩家主动）：无信号提示「There is no phone signal here...」；训练家联系人与玩家**同图**时提示「The Trainer is close by. Talk to the Trainer in person!」；联系人所在地图与当前地图**区域不同**（town_map_position 首分量不同，或任一侧缺元数据）时提示「The Trainer is out of range.」；NPC 联系人过信号门即可。

### 5.2 呼入循环

帧更新挂钩（须持 Pokégear；菜单／战斗／消息窗口／强制移动路线／事件解释器运行中暂停——暂停时两套电话倒计时都不更新）：呼入倒计时 ≤0 时**抽样离散整数分钟 20–39（`rand(20...40)`，40 取不到；不取 20.5 等非整数）**，乘 60.0 转为浮点秒后按帧间隔递减（当帧即开始减，如抽 20 分钟本帧再减 delta 秒）；到 0 时发起一次呼入：从**同区域、不同图（且地图名不同）**的可见训练家联系人中随机选一；有公共事件 ID 则调用该公共事件（缺失时提示「messages not defined. Couldn't call common event N.」），否则生成训练家对话并播放。

### 5.3 对话生成与播放

- 消息集选择：`phone.txt` 中按［类型, 名字, 当前版本］查找；缺则退回起始版本；再缺退回 `[Default]` 节。
- 问候：intro 随机一条；按时段以对应**非空**问候替换——替换窗口为**早晨 05:00–09:59（intro_morning）、下午 14:00–16:59（intro_afternoon）、傍晚 17:00–19:59（intro_evening）**；10:00–13:59 与 20:00–04:59（夜间）**不替换**，保留通用 intro（WP63-C03 查明：夜间不使用傍晚问候）。
- 主体：再战启用且旗标 >0 时——旗标 1 选 battle_request 并**就地写旗标为 2**（已告知）；旗标 2 选 battle_remind（缺则回退 battle_request）。否则：body1 与 body2 都存在时以 75% 概率取「body1＋body2」两条拼接（无 body 时恒取），否则取 body 整段；结尾 end 非空才追加。
- 占位符（播放时逐条替换）：`\TN` 联系人名、`\TP` 联系人当前版本队伍中随机一只要宝可梦名、`\TE` 联系人所在地图遭遇表随机一种（Land 前 4 槽，缺则 Cave 前 4 槽，再缺 Water 前 4 槽）、`\TM` 联系人地图名、`\PN` 玩家名（消息系统通用）。训练家类型有性别数据且设置开启（默认开）时，消息按性别加蓝／红着色标签。
- 播放：开省略号、逐段消息、结尾「Click!」。来电与去电共用同一播放路径。

## 6. 点唱机（C）

命令集（固定六项）：Play: Pokémon March／Play: Pokémon Lullaby／Play: Oak／Play: Custom...／Stop／Exit。

| 命令 | 音乐请求与实际播放（WP63-R06 查明） | 遭遇率旗标写入（WP36 消费） |
| --- | --- | --- |
| March | 请求电台曲「Radio - March」并照常更新旗标；**若已有 Custom 默认 BGM 覆盖，实际仍播放覆盖曲**（电台命令不清覆盖；覆盖规则见 WP15） | `lower=false, higher=true` |
| Lullaby | 请求电台曲「Radio - Lullaby」（已有覆盖时同样不实际改播） | `lower=true, higher=false` |
| Oak | 请求电台曲「Radio - Oak」（已有覆盖时同样不实际改播） | 两旗标都清 |
| Custom | 枚举 `Audio/BGM` 下指定扩展名（wav/ogg/mp3/midi/mid/wma）文件，去扩展名去重、按小写排序成子列表；USE 选定后**写默认 BGM 覆盖**（此后各 BGM 请求均被覆盖曲替代，持续跨地图）；BACK 退出子列表回主命令 | 选定后两旗标都清 |
| Stop | **清除默认 BGM 覆盖**并请求重播当前地图自身 BGM（此后电台命令才恢复实际改播） | 两旗标都清 |
| Exit／BACK | 无 | 无 |

旗标挂在地图元数据对象上（$PokemonMap），由遭遇生成侧读取；点唱机本身不消费。

## 7. 规则与不变量

- Pokégear 与 Town Map 入口互斥（持有 Pokégear 时不出 Town Map 项）；Phone 按钮不以联系人为条件，空电话本只提示不开画面。
- 地图选择合同以返回值分层：浏览 BACK→nil；飞行选择→`[地图ID,x,y]`；wallmap 浏览从不写飞行目的地；飞行目的地只由调用方写入 `$game_temp.fly_destination` 并由飞行执行消费后清空。
- 联系人的 UI 操作（删除、排序、移动、注册）都改变持久电话对象；再战旗标与事件自开关（A 登记后／B 再战就绪）保持同步写入。
- 对话生成只读取数据与随机选择；唯一写入是旗标 1→2 的就地推进。
- 点唱机不写地图数据；遭遇率旗标与默认 BGM 覆盖是其全部持久副作用。

## 8. 边界与失败

- 无 Pokégear：正常暂停菜单的 Pokégear 项不出现（入口门）；`can_add?` 预检 false，按预检写法的事件脚本跳过注册；但**直接 `Phone.add／add_silent` 注册仍写入**（写入入口不查预检），电话画面也只按可见联系人是否为空提示（WP63-R01）。
- 区域数据缺失分两种（WP63-R07）：**未定义的区域 ID**（含回退目标区域 0 未定义、当前位置指向未定义区域）在严格查询处先抛「Unknown ID」错误，**不会**进入友好提示分支；「The map data cannot be found.」只在其实际可达前提（定位数据对象为空而非未知 ID）出现。当前地图无 town_map_position 的**定位缺省**回退区域 0 左上角（区域 0 已定义时）。
- 无信号地图：呼出逐项拒绝、信号图标无信号、呼入循环虽计时但发起时被信号门挡下。
- 联系人同图拨打、跨区域拨打：分别提示当面谈／超出范围。
- 飞行模式下游标不在治疗点或该点未访问：USE 无效果（调试＋CTRL 豁免）。
- 公共事件缺失：来去电提示未定义消息。
- 再战版本数 =1 或全局上限 0：next_version 恒为起始版本，版本不推进。
- 点唱机 Custom 目录为空：子列表为空，USE 于空子列表等价于清除默认 BGM 覆盖（防御性保留，正常素材下不可达）。

## 9. 依赖与配置

- 规则引用：WP24（训练家类型／版本数据与战斗启动）、WP11（地图元数据、visitedMaps 写入点、区域定位）、WP59（pbCanFly?、飞行执行、HiddenMove 处理器）、WP36（遭遇率旗标消费）、WP06（时间与 fly_count 统计）、WP17（消息与输入）、WP13（公共事件与事件自开关页）、WP04（town_map.txt／phone.txt 的 PBS 生命周期）、WP08（地点名／详情／训练家名消息哈希；GR-009 语言身份注明）、WP66-A（FLY 调用方，WP66A-R05 交界）。
- 配置：`CAN_FLY_FROM_TOWN_MAP` 默认 true；`BADGE_FOR_FLY`=5；`PHONE_REMATCHES_POSSIBLE_FROM_BEGINNING` 默认 false；`COLOR_PHONE_CALL_MESSAGES_BY_CONTACT_GENDER` 默认 true；`REGION_MAP_EXTRAS` 默认 2 项；`MECHANICS_GENERATION=8`。
- 数据：PBS `town_map.txt`（区域与点：名称、详情、治疗点、开关门）、`phone.txt`（[Default] 与按［类型,名字(,版本)］的消息节）；`GameData::TownMap`、`GameData::PhoneMessage` 编译产物。
- 持久：`$PokemonGlobal.phone`（联系人、rematch_variant、rematches_enabled、双倒计时）、`visitedMaps`、`has_pokegear`、`$game_temp.fly_destination`（会话）。

## 10. 静态场景（输入 → 推导预期；均未运行）

| ID | 输入／前提 | 期望 |
| --- | --- | --- |
| P01 | 玩家有 Pokégear，背包含 TOWNMAP | 暂停菜单只出现 Pokégear 项；Town Map 项不出现 |
| P02 | 无 Pokégear、背包无 TOWNMAP | 两项均不出现 |
| P03 | Pokégear 中按 DOWN／UP（3 项） | 游标回绕；BACK 关闭，无副作用 |
| P04 | Pokégear→Map，浏览后 BACK | 返回 nil；无飞行目的地；Pokégear 回按钮循环 |
| P05 | Pokégear→Map，mode 1 选已访问治疗点并确认 | 写 fly_destination、Pokégear 整体结束，进入飞行链 |
| P06 | `pbShowMap(1, true)`（wallmap）浏览选定治疗点 | 不写飞行目的地（wallmap 浏览合同）；开关字段点一律隐藏 |
| P07 | 当前地图无 town_map_position，区域 0 已定义 | 定位回退区域 0 左上角；无玩家图标（区域不同） |
| P08 | 浏览中 ACTION 切 mode 1（CAN_FLY_FROM_TOWN_MAP 且 pbCanFly? 通过） | 显示已访问治疗点图标与「ACTION: Cancel Fly」提示；再 ACTION 回 mode 0 |
| P09 | mode 1 中 USE 于未访问治疗点（非调试） | 无效果（不发生选择） |
| P10 | 队伍 FLY 确认后打开飞行地图按 BACK | 地图返回 nil、不写目的地；调用方重建队伍：选中位重置 0、本次 Box Link 许可丢失（WP66A-R05 查明行为） |
| P11 | 编辑器模式改名一个点后 BACK 并两次确认；再进编辑器未修改按 BACK | 改动时确认保存并反写 PBS 后退出；未修改时直接退出、无询问（WP63-C02） |
| P12 | 电话画面打开（3 个可见联系人，再战启用，1 个旗标≥1） | 列表 3 项、注册数 3、待再战数 1、对应行再战图标、信号图标按当前地图旗标 |
| P13 | 无可见联系人打开电话 | 只提示「There are no phone numbers stored.」，不进画面 |
| P14 | 注册：无 Pokégear，事件先调用 can_add? 再注册；对照：脚本不经预检直接 add_silent | 预检 false（按预检写法的事件不注册）；**直接注册仍新增可见联系人**（写入入口不查预检）（WP63-R01） |
| P15 | 训练家联系人被删除（隐藏）后按原参数再注册 | 查询跳过隐藏对象：**旧对象保持隐藏（版本进度不恢复），另建一个新可见联系人**（WP63-R02）；对照：相同「版本数 3、起始版本 0」参数连续直接注册两次，两次都新增（查重口径缺陷） |
| P16 | 删除训练家联系人并确认 | visible=false、倒计时与旗标清零、事件自开关 A 置位＋地图刷新；可见优先重排；删光提示并关闭画面 |
| P17 | 删除 NPC 联系人 | 命令不出现（NPC 不可删） |
| P18 | 排序三式各执行一次（含隐藏联系人） | 按所选键排序后可见优先稳定重排；隐藏者沉底且组内顺序保留 |
| P19 | 列表 ACTION 移动第 1 项到下两位再 BACK | 实时重排在 BACK 时还原到原位置；USE／ACTION 则落定新位置 |
| P20 | 再战就绪：旗标 0、倒计时减到 0 | 旗标置 1，事件自开关 A 复位／B 置位，地图刷新；**此后每秒因旗标 >0 跳过、倒计时停在 0 不再随机**（WP63-R05），直到胜利重置 |
| P21 | 旗标 1 时来去电对话 | 主体取 battle_request，**旗标就地写 2**；下通取 battle_remind（缺则 battle_request） |
| P22 | 旗标 0 且 body1/body2 齐备 | 75% 概率取 body1＋body2 拼接；无 body 时恒取拼接；end 非空追加 |
| P23 | 消息集缺当前版本节 | 回退起始版本节；再缺回退 [Default] 节 |
| P24 | 时段问候（intro_morning 非空，06:00 呼入；22:00 对照） | 06:00 以 intro_morning 替换 intro；**22:00（夜间）不替换，保留通用 intro**（WP63-C03） |
| P25 | 呼出：训练家与玩家同图 | 提示当面谈，不拨打；跨区域提示超出范围；无信号提示无信号 |
| P26 | 呼入随机候选：同区域、不同图且地图名不同 | 只从满足三条件的可见训练家联系人抽取；无候选则不发起 |
| P27 | 再战胜利后 reset_after_win | 版本推进到 next_version、旗标清 0、倒计时清 0（下轮重新随机） |
| P28 | 版本数 1、全局 rematch_variant 0 | next_version 恒为起始版本；Phone.battle 以起始版本开战 |
| P29 | 点唱机 March → 换地图（无既有覆盖） | 请求电台曲并实际播放；遭遇率 higher 旗标置位（WP36 消费）；未写默认 BGM 覆盖 |
| P30 | 先 Custom 选曲 A，再选 March，最后 Stop | Custom 写覆盖 A；**March 只更新旗标与请求、实际仍播 A**（WP63-R06）；Stop 清覆盖并请求地图 BGM，此后电台恢复实际改播 |
| P31 | 事件按类型＋名字呼出（无插件补充，联系人有效可见） | 在信号／距离门之前即发生未定义方法错误（类级 `Phone.get` 不存在）；对照：电话 UI 传联系人对象正常走呼出门（WP63-R03） |
| P32 | 公开包装 `Phone.variant`／`Phone.increment_version`（联系人相对版本 1） | 查询恒返回 0、递增无动作（类型落入布尔标志位无法匹配）；对照：联系人对象级 next_version 与 reset_after_win 正确（WP63-R04） |
| P33 | 打开区域地图：区域 0 未定义（或当前位置指向未定义区域） | 严格查询先抛「Unknown ID」错误，**不进入**「The map data cannot be found.」分支（WP63-R07） |

## 11. 未决与保留

- **WP66A-R05 交界**：队伍 FLY 取消返回的调用方重置（选中位 0、Box Link 许可丢失）已在 §2.3／P10 采用查明行为；WP66-A 已同步修订为 v3，两稿一致。
- **公共事件电话材料**：NPC 联系人的公共事件 ID 与对话内容属事件数据（U01）；「公共事件电话如何调用」仅登记 `pbCommonEvent` 调用点与缺失提示，demo 实际公共事件未提取。
- **demo 可达性**：Pokégear 授予点、联系人注册事件、rematch_variant 抬升点、飞行点解锁事件均属 U01／WP77；本包不作可达声明。
- **GR-009（WP24）**：训练家语言来源编号与界面语言的区分是 WP24 已确认事项；本包显示名经消息哈希，未复制其旧合同。
- **插件**：`:pokegear_menu` 可扩展；自定义按钮的组合未穷尽。
- **媒体**：按钮／背景性别变体、头像图、地图图资源存在性未核对；显示合同只到可观察状态层。
- **弃用族与缺陷入口**：v22 弃用包装多条指向缺失或失配的入口（WP63-R03／R04），只登记转发关系与缺陷边界，不以「转发」暗示功能必然可用；编译器生成的再战事件使用公开 `Phone.variant` 查询（携带同缺陷），其修复归 WP13／WP24 侧统一处理。

## 12. 来源与审计（traceability）

只读静态读取；行为化描述，未复制源码结构。固定 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。

- `Data/Scripts/016_UI/008_UI_Pokegear.rb`：全文 1–206（按钮、场景、注册表默认项 160–206）。
- `Data/Scripts/016_UI/009_UI_RegionMap.rb`：全文 1–356（打开定位 70–157、点信息 183–231、飞行模式 233–246、主循环 248–320、屏幕与 pbShowMap 326–356）。
- `Data/Scripts/016_UI/010_UI_Phone.rb`：全文 1–271（画面 31–137、选择与移动 139–189、命令 210–270）。
- `Data/Scripts/016_UI/011_UI_Jukebox.rb`：全文 1–149。
- `Data/Scripts/013_Items/004_Item_Phone.rb`：全文 1–706（电话对象 4–210、联系人 215–313、呼叫 318–538、帧更新挂钩 543–560、弃用族 562–706）。
- `Data/Scripts/010_Data/002_PBS data/021_PhoneMessage.rb`：全文 1–100；PBS `town_map.txt`、`phone.txt` 结构样本（顶层各首 30／40 行）。
- `Data/Scripts/016_UI/001_UI_PauseMenu.rb:166–182,206–236`（Pokégear／Town Map 入口与飞行链）；`016_UI/005_UI_Party.rb:479–526,774–781,1204–1213,1288–1302`（WP66A-R05 交界复核）；`012_Overworld/004_Overworld_FieldMoves.rb:457–500,505–513`（pbCanFly?、pbFlyToNewLocation、FLY 处理器）；`012_Overworld/001_Overworld.rb:236`（visitedMaps 写入点）；`012_Overworld/002_Overworld_Metadata.rb:50,72,105`（电话对象与 visitedMaps 初始化）；`003_Game processing/006_Event_HandlerCollections.rb:80–123`（注册表机制）；`019_Utilities/001_Utilities.rb:524`（pbCommonEvent）；`015_Trainers and player/004_Player.rb:24,49`（has_pokegear 默认 false）。
- 修订补读（WP63-R01～R07、C01～C03）：`021_Compiler/004_Compiler_MapsAndEvents.rb:648–670`（生成再战事件页的 Phone.variant 消费）；`008_Audio/002_Audio_Play.rb:52–67`、`004_Game classes/002_Game_System.rb:44–81`（默认 BGM 覆盖的播放优先）；`010_Data/002_PBS data/002_TownMap.rb:22–30`、`010_Data/001_GameData.rb:171–178`（严格查询抛错）；`012_Overworld/003_Overworld_Time.rb:50–72`（时段窗口）。
- 配置：`001_Settings.rb:121,333–353`（BADGE_FOR_FLY、REGION_MAP_EXTRAS、CAN_FLY_FROM_TOWN_MAP、PHONE_REMATCHES_POSSIBLE_FROM_BEGINNING、COLOR_PHONE_CALL_MESSAGES_BY_CONTACT_GENDER）。
- 交界登记：WP66-A 进度复审 `review/wp66a-progress-review-2026-10-01/report.md`（WP66A-R05）；全局 findings GR-009（WP24 语言身份）。

---

本包为 **ReviewPending（修订 v3，2026-10-01；待定点复审）**；静态自检不授权把缺陷修成理想行为，也不等于独立 review 或运行通过。首版 Drafted 稿 `80cdbff2b9dbb7274a123fb64f3fb3b7f5d3ac2c1545415942ca36a9a23ae859`（26,354字节）为被审 v1 原件留史；修订 v2 `c90a728dd599fa58c702569c2a55bfd5f136927666986d0bdf6512c5fa1c6076`（32,874字节）为被审 v2 原件留史。

### 当前依赖身份（审计绑定）

| 包 | 文件 | 完整SHA-256 | 字节 |
| --- | --- | --- | ---: |
| WP17 | `specs/ui/wp17-messages-windows-input.md` | `bb61f967a91423de675a32f71f2a1efd91efc822a6e5d5a08be63d3af246fc12` | 30,047 |
| WP24 | `specs/creature-rpg/wp24-player-trainers-partners.md` | `325940946f7b120c4e484695dd35c5804c2baf9411798d95c22af2f944a2e7e5` | 29,668 |
| WP11 | `specs/overworld/wp11-map-topology-transfer.md` | `84ca24a5919f05a280e67b0470436cdaf5557800ced19a0fccb218fbf3f38275` | 19,944 |
| WP59 | `specs/overworld/wp59-world-time-weather-field-moves.md` | `46e8010658029a4338a1abc23dd9191ae0cb91f9f05dd0f3815eb0c4318b4094` | 42,401 |
| WP36 | `specs/creature-rpg/wp36-wild-encounters-and-modifiers.md` | `5a05aad72cec624397912038f3fb2f7df920eac220b2e55cbe9ee583c161ac33` | 34,305 |
| WP13 | `specs/overworld/wp13-map-events-npc-followers.md` | `0b9bbd02e9b6032690967549f62d0f5024c0a8bf6ad541e0f7b94b7a09d242d8` | 28,571 |
| WP66-A | `specs/ui/wp66-a-party-and-summary-ui.md` | `49f373e278ace6f78fe810a11382d994931f63960e0b09356fd75898d3023210` | 44,563 |
