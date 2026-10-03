# WP73-B 规格：世界编辑器（地图连接/地图元数据/地形标签/遭遇/指标）

| 字段 | 内容 |
| --- | --- |
| 工作包 | WP73-B（世界编辑器） |
| 关联功能 | F18-02（数据和世界编辑器，D18——与 WP73-A 分治：本包为世界/资源内容编辑部分） |
| 分类 | Demo/Developer Experience（主）；Engine/Overworld Integration（地图/图块组/连接/小地图）、Generic Kernel（GameData 持久/编译反写交界）、User Interface（可视化画布/选择器）分别注明；类名/方法名是参考侧取证记录，不是未来框架 API |
| 参考基线 | `reference/pokemon-essentials/` @ commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（WP01 固定） |
| 输入 | 三份世界编辑器文件分段全文（`020_Debug/001_Editor screens/003_EditorScreens_MapConnections.rb` 578 行、`…/002_EditorScreens_TerrainTags.rb` 263 行、`…/004_EditorScreens_SpritePositioning.rb` 411 行，共 1,252 行）；遭遇编辑器与地图元数据编辑器（`001_EditorScreens.rb:6–340, 779–817`——WP73-A 已全文阅读，同基线复用）；无效图块修复（`003_Debug_MenuExtraCode.rb:668–739`——WP72 已全文阅读，同基线复用）；指标持久常量、MapFactoryHelper 连接存取、小地图/临界段辅助定点 |
| 前置依赖 | WP04（PBS 生命周期/编译反写，必需）、WP11（地图拓扑/连接，必需）、WP12（地形/移动，必需）、WP15（资源匹配/素材，必需）、WP36（遭遇数据语义，必需）五份必需；边界引用 WP02/WP03/WP05/WP07/WP09/WP13/WP16/WP17/WP18/WP19/WP21/WP59/WP72/WP73-A（各自具名通过范围，以独立报告为准） |
| 规格状态 | **ReviewPending（WP73-B 具名静态范围，待统一 review）**：地图连接可视化编辑器、地图元数据编辑器、地形标签编辑器、遭遇编辑器（集/类型/槽三层）、指标编辑器与全量自动定位、无效图块修复的输入、校验、取消、保存与反写合同；资源关联核验与无资源边界。内容编辑器（WP73-A）、动画工具（WP74）、编译与转换（WP75）不在本状态内 |
| 证据等级 | 全部为静态证据：已定位 / 静态确认 / 数据样本确认；**无运行确认**（未运行编辑器/游戏/UI、未执行编译器或反序列化、未写 PBS/.dat/地图/图块组文件、未播放音频、未操作真实存档、未调整宿主界面） |

## 1. 目的、范围与非目标

**目的**：固定世界编辑器的规则合同——**每个世界/资源编辑器读什么输入、坐标/地形/遭遇/指标如何校验、取消时是否仍写入、编辑何时生效（内存/`.dat`/PBS 三层）、数据与地图/图块组资源的关联如何核验、无资源时哪些操作不可确认**。后续包据此判断"某次世界编辑实际落到了哪一层、改了哪份文件"。编辑器实现是作者行为要求的参考，不作为未来编辑器的布局或交互设计模板。

**范围**（WP73-B 自身声明范围）：

1. 地图连接可视化编辑器（`pbConnectionsEditor`/`MapScreenScene`）：画布与邻居递归摆放、增删图、拖拽、连接数据生成（邻接判定与对称去重）、保存与取消。
2. 地图元数据编辑器（`pbMapMetadataScreen`/`pbEditMapMetadata`——同 `001_EditorScreens.rb`，WP73-A 已读全文）：属性框架复用与即时落盘。
3. 地形标签编辑器（`pbTilesetScreen`/`PokemonTilesetScene`）：图块组载入、标签设置（含自动图块整组语义）、保存与宿主提示。
4. 遭遇编辑器（`pbEncountersEditor`/`pbEncounterMapVersionEditor`/`pbEncounterTypeEditor`——同 `001_EditorScreens.rb`，WP73-A 已读全文）：集/类型/槽三层编辑与退出确认。
5. 指标编辑器（`SpritePositioner`/`SpritePositionerScreen`）与全量自动定位（`pbAutoPositionAll`）：单项定位/阴影尺寸/单体自动定位/全量自动定位的算法与落盘。
6. 无效图块修复（`pbDebugFixInvalidTiles`——WP72 已读全文，本包主责其合同）：全地图扫描、有效性判定、写 0 与地图文件保存。

**非目标**：

- 不提取内容编辑器（WP73-A 主责：训练家类型/训练家战斗/道具/物种/全局与玩家元数据/地区图鉴——本包复用其属性框架与列表器合同并引用）；不提取动画工具（WP74）、编译器全集与文件更名/转换（WP75）；不展开遭遇/地图/地形/指标的**数据语义**（WP36/WP11/WP12/WP15/WP16 主责——本包只固定编辑行为与文件层）。
- 不重提取已通过规则：属性框架与列表器（WP73-A §3/§5）、GameData 三层持久（WP73-A §2）、调试入口（WP72 §8.3——含归属更正：本包为其 WP73-B 归属的主体）、PBS 编译/反写（WP04）。
- 不运行编辑器/编译器/反序列化、不写 PBS/.dat/地图/图块组文件、不操作真实存档、不调整宿主界面、不设计未来编辑器布局或 API。

## 2. 概念与术语

- **三层持久模型（继承 WP73-A §2）**：内存 `DATA`/运行缓存层 → `.dat` 保存层 → `Compiler.write_*` PBS 反写层。本包各编辑器的落点：**连接**＝退出确认时 `save_data` 写 `Data/map_connections.dat`＋`Compiler.write_connections`＋清工厂缓存；**地图元数据**＝确认即 `register`＋`save`＋`Compiler.write_map_metadata`；**地形标签**＝退出确认时 `save_data` 写 `Data/Tilesets.rxdata`＋替换运行 `$data_tilesets`＋**重启 RMXP 提示**；**遭遇**＝退出确认时 `GameData::Encounter.save`＋`Compiler.write_encounters`，否则 `load` 丢弃；**指标**＝退出确认时 `GameData::SpeciesMetrics.save`＋`Compiler.write_pokemon_metrics`，否则 `load` 丢弃；**修复图块**＝逐图立即保存（无总确认）。
- **小地图与画布**：`createMinimap`（`006_Map renderer/004_TileDrawingHelper.rb:164`——WP16 引用）生成每格 4 像素的地图缩略图；连接编辑器以**网格对齐（坐标向下取整到 4 的倍数）**摆放缩略图；**画布上的图只是编辑会话内的摆放**——删掉画布上的图不删连接数据本身，连接数据由**生成算法**按当前画布重算（§3.3）。
- **连接数据形态**：原始连接为**边＋坐标**形式（`[图1, 边1, 坐标1, 图2, 边2, 坐标2]`——N/S/E/W 边经 `MapFactoryHelper.getMapConnections` 惰性装载时换算为坐标对并**过滤尺寸为 0 的无效图**——`004_Game classes/005_Game_MapFactory.rb:383–420`）；编辑器生成的连接为**相对坐标差**形式（`[参照图, 0, 0, 目标图, dx, dy]`，dx/dy 为缩略图坐标差除以 4——即地图格数差）。
- **邻接判定**：两图**直接连接**当且仅当缩略图在某轴对齐且另一轴的坐标差等于其中一图的对应尺寸（边贴边——§3.3 公式）；**画布上无任何直接连接的图**回退为与（非自身的）第一个画布图建立连接——**保证连通**（`003:241–246`）。
- **对称去重**：新连接与既有连接**完全相同**或**镜像对称**（两端互换且坐标差取负）时不重复添加（`003:200–219`）。
- **地形标签的自动图块语义**：图块 ID < 384（每行 8、每自动图块 48）时**设置整组 48 个标签**；≥384 时设置单个标签（`002:163–169`）。**TILESET_START_ID = 384**。
- **指标（metrics）**：每物种×形态的显示参数——**back_sprite [x,y]**（我方背后位）、**front_sprite [x,y]**（对方正面位）、**front_sprite_altitude**、**shadow_x**、**shadow_size**（0＝无，编号对应 `Graphics/Pokemon/Shadow/<编号>` 图形）；**自有阴影图形**（`Graphics/Pokemon/Shadow/<物种>_<形态>` 或 `<物种>`）存在时 **shadow_size 不可编辑**（§6.3）。持久于 `species_metrics.dat`（`010_SpeciesMetrics.rb:14`）。
- **底部探测（自动定位算法）**：从位图底行向上找到**首个 alpha>0 像素**所在行——bottom；**y = (位图高 − (bottom+1)) / 2**（正面位再 +4）；自动定位同时把 **x 写 0、front_sprite_altitude 写 0**（全量时另把 shadow_x 写 0、shadow_size 写 2）（`004:4–41, 138–155`）。
- **资源关联核验**：**有资源才能确认的操作**——地形标签编辑要求 `Data/Tilesets.rxdata` 可装载（编辑器直接 `load_data`，WP04/WP10 边界）；指标编辑的预览要求对应物种/形态图形存在（缺失时预览为空，编辑仍可改数值）；**自有阴影图形存在时阴影尺寸编辑被拒绝**；**无资源时**小地图/预览仅显示层回落，**不阻止数值编辑**（除上述具名拒绝）。
- **已通过边界（必须继承，不重开）**：WP73-A（属性框架/列表器/三层持久/选择器——当前字节 `4c3e591c`）、WP72（调试入口与工具归属——当前字节 `49731474`）、WP04、WP11、WP12、WP15、WP36、WP16、WP59、WP61（`d84dff78`）、WP53（`75fc4db7`）、WP37（`d032f5b7`）、WP65、WP67-A/B、GR-001～016、WP23-N01。

## 3. 地图连接可视化编辑器（`003_EditorScreens_MapConnections.rb` 全文）

### 3.1 打开与画布（`003:567–578, 308–344`）

- **打开**：屏幕尺寸**宽高各 +288**（临界段 `pbCriticalCode`——`003_Errors.rb:76` 引用），结束后恢复原尺寸与缩放因子；初始图：当前图（无当前图取系统编辑图 ID，再缺省 1）居中摆放并**递归摆放全部邻居**（按既有连接偏移 ×4 递归——`003:165–191`）。
- **画布元素**：每图一个缩略图精灵（网格对齐）；选中框（红色描边跟随选中图）；底部"D: Help"提示行；帮助窗（D 键——按键清单）。
- **既有连接装载**：`MapFactoryHelper.getMapConnections`（惰性、含坐标换算与无效图过滤——§2）；**克隆入会话数组**（去两端完全重复项——`003:332–337`）。

### 3.2 编辑操作（`003:384–544`）

- **A 键（Add map）**：地图列表（MapLister——WP73-A 引用）选图 → 居中放入画布（网格对齐）＋置顶 → **立即重算连接数据**（§3.3）。
- **S 键（Go to map）**：选图 → **先重算当前画布连接数据**（保存当前成果入会话数组）→ 清画布 → 以新图为根重新摆放（含邻居递归）。
- **DEL 键（Delete map from canvas）**：画布图数 >1 且有选中 → 从画布移除该图（**只移出画布——连接数据不因此删除**；下次重算时被移出的图不再参与）。
- **单击**：选中（红框、置顶、标题行显示图名）＋开始拖拽（**拖拽落点同样网格对齐**）；**双击（0.5 秒内）**：打开该图的**地图元数据编辑**（§4——WP73-A 属性框架复用）。
- **拖动画布空白**：记录各图位置后整体平移（网格对齐）；**方向键**：全画布 4 像素步进平移。
- **D 键**：帮助窗（USE/BACK 关闭）。

### 3.3 连接数据生成与保存（`003:221–285, 546–562`）

- **生成算法**：克隆会话连接数组 → **删除所有触及画布图的旧连接** → 对每个画布图求**直接连接集**（对画布内每个其它图：缩略图坐标差 ÷4 后，**x 差等于对方图宽或己方图宽取负，或 y 差等于对方图高或己方图高取负**即邻接；**一个都没有时回退连接画布首个其它图**）→ 逐对生成 `[参照图, 0, 0, 本图, dx, dy]`，**经对称去重**后追加。
- **保存**：BACK → **"Save changes?" 确认** → `save_data` 把生成结果写入 `Data/map_connections.dat`＋`Compiler.write_connections`＋**MapFactoryHelper.clear（清工厂连接缓存）**＋会话数组替换为生成结果；**不确认 → `GameData::Encounter.load`（遭遇数据整体重载——跨编辑器状态恢复的如实登记：本编辑器经由双击进入的地图元数据/遭遇编辑若未各自保存，其内存改动随此重载丢弃；连接会话数组本身不序列化）**；随后 **"Exit from the editor?"** 确认才退出（否则回到画布）。
- **边界**：生成只覆盖**画布上的图**——不在画布上的既有连接原样保留（克隆里未触及部分）；**不校验生成连接的图是否存在/有资源**（装载期过滤由 MapFactoryHelper 负责，WP11 引用）。

## 4. 地图元数据编辑器（`001_EditorScreens.rb:779–817`；WP73-A 已读全文，本包主责合同）

- **顶层**：`pbMapMetadataScreen`（实参为起始地图 ID）——地图列表（MapLister，默认传入图/默认图）循环；**选 0 → 编辑全局元数据**（WP73-A §4.5）；**选图 → `pbEditMapMetadata`（实参为该图 ID）**。
- **编辑**：图名取自 mapinfos；元数据不存在则**先以 `{:id => map_id}` 实例化**；editor_properties → `pbPropertyList`（saveprompt——WP73-A §3.1）→ **确认保存**：schema 组哈希＋保留 `pbs_file_suffix` → **register＋save＋`Compiler.write_map_metadata`**（即时生效，无退出确认）。
- **从连接编辑器双击进入**时同此合同（保存即时；未保存的内存改动可能随后被连接编辑器的取消分支重载——§3.3 如实登记）。

## 5. 地形标签编辑器（`002_EditorScreens_TerrainTags.rb` 全文）

- **打开**：屏幕**高 ×2**（结束后恢复）；**载入 `Data/Tilesets.rxdata` 全量**（`load_data`——反序列化边界，WP04/WP10 引用）；初始图块组 1。
- **显示**：每行 8 块 ×32 像素；**首行为自动图块行**（每自动图块 48 块）；覆盖层显示**非 0 标签数字**；右侧 400% 放大当前块＋标签名（`GameData::TerrainTag` 存在则显示 `编号: 名称`，否则只显示编号）；品红衬底。
- **导航**：方向键（repeat）逐块、**JUMPUP/JUMPDOWN 半页**、ACTION 菜单（**Go to bottom／Go to top／Change tileset**——图块组列表切换）。
- **编辑**：USE → 标签列表（全部 `GameData::TerrainTag`，**当前标签预选**）→ 选定且不同才写——**自动图块（ID<384）整组 48 个同写；普通块单写**；随后刷新覆盖层。
- **保存**：BACK → **"Save changes?" 确认** → **`save_data` 把图块组数据写回 `Data/Tilesets.rxdata`＋运行侧 `$data_tilesets` 整体替换**＋消息 **"为确保更改保留，请关闭并重新打开 RPG Maker XP"**（宿主数据双份语义——WP10/WP75 边界如实登记）；**"Exit from the editor?"** 确认才退出。
- **关闭**：恢复地图工厂装配、玩家居中、地图场景精灵组重建（`002:44–52`）。
- **资源关联**：图块组数据来自 RMXP 工程文件（Tilesets.rxdata）——**不是 PBS/.dat 游戏数据**；标签 ID 与 `GameData::TerrainTag`（PBS `terrain_tags.txt`——WP04/WP12 引用）的关联**只在显示层核验**（存在才显示名称）；**无名称数据的标签值仍可写入**。

## 6. 遭遇编辑器（`001_EditorScreens.rb:6–340`；WP73-A 已读全文，本包主责合同）

### 6.1 集列表（`pbEncountersEditor`）

- **列表**：全部遭遇集（`GameData::Encounter.each`）——显示 `地图ID[(v.版本)][: 图名]`（图名缺失省略）；**[Add new encounter set]** 在首。
- **新建**：地图列表（MapLister 默认图）＋版本（LimitProperty2 0–999，取消 → 放弃）→ **已存在检查**（同图同版本 → 消息拒绝）→ 注册空集（step_chances/types 空）并定位光标。
- **已有项**：**Edit**（进 §6.2）／**Copy**（目标图＋新版本——已存在检查；**深拷贝 step_chances 与 types（槽数组逐项克隆）＋保留 `pbs_file_suffix`**）／**Delete**（确认 → `DATA` 删除）。
- **保存**：BACK → **"Save changes?" 确认** → `GameData::Encounter.save`＋`Compiler.write_encounters`；**否则 `GameData::Encounter.load`（整体重载丢弃——含删除）**（`001:115–120`）。

### 6.2 集内编辑（`pbEncounterMapVersionEditor`）

- **图 ID 行／版本行**：改图或改版本——**目标（图,版本）已存在检查**（冲突 → 消息）；通过则**删旧键、改字段、按新键重新登记**。
- **类型列表**：每个遭遇类型显示 `类型 (x槽数)`；**[Add new encounter type]**——未用类型列表（全用 → 消息）；新增时**步数率默认取该类型 trigger_chance**（WP36 引用）并进 §6.3。
- **类型项**：**Edit**（§6.3）／**Copy**（目标未用类型——克隆步数率与槽数组）／**Delete**（确认 → 步数率与类型槽同删）。

### 6.3 类型内编辑（`pbEncounterTypeEditor`）

- **步数率行**：LimitProperty 0–255（默认当前）。
- **类型行**：改为另一类型（**已被本集使用的类型排除**；当前预选）——步数率与槽**整体迁移**（旧键删除）。
- **槽列表**：每槽 `EncounterSlotProperty.format`（`概率, 名字[_形态] (Lv.a[-b])`——WP73-A §3.5 引用）；**[Add new slot]**（缺省 `[20, 首个物种, 5, 5]`）；槽项 **Edit**（属性子编辑——**最低>最高交换**）／**Copy**（克隆插入其后）／**Delete**（确认）。
- **无总确认**：§6.2/§6.3 的改动**即时写入内存 `enc_data`**——最终落盘与否由 §6.1 的退出确认决定（**不确认则全部丢弃**）。

## 7. 指标编辑器与自动定位（`004_EditorScreens_SpritePositioning.rb` 全文）

### 7.1 编辑器框架（`004:46–136, 389–411`）

- **打开**：战斗背景/双方底座/消息框位图＋双方宝可梦精灵位（`Battle::Scene.pbBattlerPosition` 引用——WP40/WP16）；物种未选时精灵隐藏。
- **物种选择**：全物种×形态列表（0 形态显示名、非 0 形态 `名字 (form N)`、字母序）；**浏览即预览**（切换即时重设精灵位图与阴影）；**BACK 取消**（清选择）、**USE 选定**。
- **主菜单**（五选项循环——确认后 **(当前+1) mod 3 循环前进**到下一参数项）：**Set Ally Position／Set Enemy Position／Set Shadow Size／Set Shadow Position／Auto-Position Sprites**（**前进模数为 3**——如实登记：五项菜单按 3 循环）。
- **保存**：退出（pbClose）——**`metricsChanged` 且 "Some metrics have been edited. Save changes?" 确认** → `GameData::SpeciesMetrics.save`＋`Compiler.write_pokemon_metrics`；**否则 `GameData::SpeciesMetrics.load`（整体重载丢弃全部指标改动）**（`004:91–101`）。

### 7.2 单项定位（`pbSetParameter`，param 0/1/3；`004:224–305`）

- 选中精灵**闪烁**；信息行显示当前坐标；**LEFT/RIGHT 调 x**（三个参数均可）；**UP/DOWN 调 y**（param 3 不可调 y——阴影只有 x）；**USE 确认**（有变化才置 metricsChanged）；**ACTION 确认并前进下一项**；**BACK 恢复旧值**（放弃）。

### 7.3 阴影尺寸（`pbShadowSize`；`004:167–222`）

- **自有阴影图形检查**：`Graphics/Pokemon/Shadow/<物种>_<形态>` 或 `<物种>` 任一存在 → **"该物种有自有阴影图形，shadow_size 不可编辑"消息并返回**（拒绝）。
- 否则列出可选尺寸：**0（None）＋按编号递增探测 `Graphics/Pokemon/Shadow/<编号>` 存在的项**（当前预选）；**浏览即改并预览**；**USE 确认／ACTION 确认并前进／BACK 恢复旧值**。

### 7.4 单体与全量自动定位（`pbAutoPosition`/`pbAutoPositionAll`；`004:4–41, 138–155`）

- **单体（菜单 Auto-Position Sprites）**：按 §2 底部探测算法计算 back/front 的 y（front 再 +4）；**仅当有变化或 front_sprite_altitude 非 0 才写入**（back y、front y、altitude=0）并置 metricsChanged＋刷新；**x 不改、阴影不改**。
- **全量（调试菜单 Auto-set pokemon_metrics——确认"确定要重定位全部精灵？"后执行）**：**遍历全部物种×形态**（每 5 秒保活界面）；每对象：背后位图存在 → **back_sprite = [0, 算法 y]**；正面位图存在 → **front_sprite = [0, 算法 y+4]**；**front_sprite_altitude = 0、shadow_x = 0、shadow_size = 2**（**无差别覆写**——含手工调过的值）；完成后 **`GameData::SpeciesMetrics.save`＋`Compiler.write_pokemon_metrics`**（立即落盘，无二次确认；等待消息窗随执行显示）。
- **资源关联**：位图缺失的对象**对应项不写入**（保持原值）；`findBottom` 对全透明位图返回 0（y 退化为 (高−1)/2——如实登记，不虚构资源校验）。

## 8. 无效图块修复（`003_Debug_MenuExtraCode.rb:668–739`；WP72 已读全文，本包主责合同）

- **范围**：**全部地图**（`Compiler::MapData`——WP75 引用）的**全部图块层**与**全部事件页图形**。
- **有效性判定**：图块 ID <384 → 对应**自动图块名非空**才有效；≥384 → **图块组通行表存在该 ID** 才有效（`pbCheckTileValidity`——tilesets 数据引用，WP04/WP12 边界）。
- **修复**：无效图块 **写 0**（事件页图形 tile_id 同）；每图计数；**有改动的图立即 `mapData.saveMap(id)`（逐图保存——无总确认）**；控制台逐图列出（图 ID/名称/错误数）。
- **完成反馈**：无错误 → "No invalid tiles were found."；有错误 → 控制台汇总＋**"RMXP data was altered. Close RMXP now to ensure changes are applied."**＋消息"N error(s) were found across M map(s) and fixed."＋"关闭 RPG Maker XP 以应用更改"（**宿主双份语义**——WP10/WP75 边界如实登记；执行期每 5 秒保活界面）。

## 9. 默认行为与配置变体

- **配置值（WP02 引用）**：`SCREEN_WIDTH/SCREEN_HEIGHT`（连接编辑器 +288、地形编辑器 ×2）、`GrowthRate.max_level`（遭遇槽等级范围）。
- **数据文件层**：`Data/map_connections.dat`、`Data/map_metadata.dat`（经 GameData）、`Data/Tilesets.rxdata`（**RMXP 工程文件**——WP10/WP75 边界）、`Data/species_metrics.dat`、`Data/encounters.dat`（经 GameData）、地图 `Data/MapNNN.rxdata`（修复图块——WP75 边界）。
- **宿主重启语义**：地形标签与无效图块修复均提示**关闭/重开 RMXP 以应用更改**（工程文件与运行数据双份——如实登记，不虚构热同步）。
- **未验证组合**：编辑器实际运行表现、小地图/预览/战斗背景素材存在（WP15/WP16/U01）、demo 中入口默认可达性（WP77/U01）、连接生成后的实际通行表现（WP11 主责）。

## 10. 边界、失败与未知

- **取消语义汇总**：连接——BACK 确认才序列化＋清缓存（否则**遭遇重载**——§3.3 如实登记）；地图元数据——确认即落盘；地形——BACK 确认才写 Tilesets.rxdata（否则内存数据随关闭丢弃）；遭遇——BACK 确认才 save＋反写（否则 load 丢弃全部含删除）；指标——退出确认才 save＋反写（否则 load 丢弃）；修复图块——**逐图立即保存**（无取消路径）。
- **拒绝/回退**：连接——无邻接回退连首图（保证连通）；遭遇——同（图,版本) 存在检查（新建/复制/改图/改版/改类型）、类型全用消息；指标——自有阴影图形拒绝 shadow_size 编辑；修复——无错误只提示。
- **不校验项（如实登记）**：生成连接不验证图存在性（装载层过滤）；地形标签可写入无名称数据的值；指标编辑不要求图形存在（除 §7.3 具名拒绝）；自动定位对全透明位图退化计算。
- **异常路径**：图形装载失败仅显示层回落（精灵位图为空）；`pbCriticalCode` 包裹连接编辑器的屏幕尺寸变更（恢复在临界段内）；**不虚构事务回滚**——逐图保存与逐对象覆写按实际登记。
- **未知/未证**：编辑器运行表现与宿主窗口行为；素材存在（WP15/U01）；demo 入口可达性（WP77/U01）；`Compiler::MapData` 读写地图的完整合同（WP75 主责——本包只引用调用点）；连接数据的运行时消费细节（WP11 主责）。

## 11. 可复核性与静态场景

### 11.1 复核方式

| 事实 | 复核方式 |
| --- | --- |
| 地图连接编辑器（画布/生成/保存） | 阅读 `S/020_Debug/001_Editor screens/003_EditorScreens_MapConnections.rb`（578 行全文） |
| 地形标签编辑器 | 阅读 `S/020_Debug/001_Editor screens/002_EditorScreens_TerrainTags.rb`（263 行全文） |
| 指标编辑器与自动定位 | 阅读 `S/020_Debug/001_Editor screens/004_EditorScreens_SpritePositioning.rb`（411 行全文） |
| 遭遇编辑器与地图元数据编辑器 | `S/020_Debug/001_Editor screens/001_EditorScreens.rb:6–340, 779–817`（WP73-A 同基线全文阅读复用） |
| 无效图块修复 | `S/020_Debug/003_Debug menus/003_Debug_MenuExtraCode.rb:668–739`（WP72 同基线全文阅读复用） |
| 连接装载与缓存 | `S/004_Game classes/005_Game_MapFactory.rb:383–420`；`S/010_Data/002_PBS data/001_MiscPBSData.rb:14–26` |
| 指标持久与小地图/临界段 | `S/010_Data/002_PBS data/010_SpeciesMetrics.rb:14, 71`；`S/006_Map renderer/004_TileDrawingHelper.rb:164`；`S/001_Technical/001_Debugging/003_Errors.rb:76` |
| 属性框架/列表器/选择器 | WP73-A 主稿 §3/§5（同基线继承） |

### 11.2 静态推导场景（未运行，待运行验证）

| 场景 | 输入 | 推导预期 |
| --- | --- | --- |
| M01 连接编辑器打开（人工夹具） | 当前图有若干既有连接 | 屏幕 +288；当前图居中＋**邻居按偏移 ×4 递归摆放**；会话数组为克隆（去两端重复） |
| M02 增图与重算（人工夹具） | A 键加入一张与画布图边贴边的图 | 网格对齐放入＋置顶；**立即重算**：触及画布图的旧连接删除，新邻接按 §3.3 生成（坐标差 ÷4） |
| M03 邻接判定与回退（人工夹具） | a) 两图 x 差 = 对方图宽；b) 两图对角放置（无邻接） | a) 直接连接生成；b) **回退与画布首个其它图连接**（保证连通） |
| M04 对称去重（人工夹具） | 已生成 [A,0,0,B,dx,dy] 后再评估 [B,0,0,A,−dx,−dy] | **不重复添加**（镜像对称） |
| M05 画布删除与保存（人工夹具） | a) DEL 移除一张图后保存确认；b) BACK 不确认 | a) 被移图不参与重算（其旧连接已删、不重建）；确认 → 写 `map_connections.dat`＋write_connections＋清工厂缓存；b) **`GameData::Encounter.load` 重载遭遇**＋连接不序列化；随后 Exit 确认才退出 |
| M06 双击编辑元数据（人工夹具） | 0.5 秒内两次单击某图 | 打开该图元数据编辑（pbPropertyList——确认即 register＋save＋write_map_metadata；**随后若连接编辑器取消保存，遭遇/元数据内存改动可能被重载丢弃**） |
| M07 地形编辑器显示（人工夹具） | 打开并移动到某非 0 标签块 | 覆盖层显示标签数字；右侧 400% 放大＋`编号: 名称`（无名称数据只显示编号） |
| M08 自动图块整组（人工夹具） | 对 ID<384 的自动图块设标签 | **该自动图块全部 48 个标签同写**；普通块只写单块 |
| M09 地形保存（人工夹具） | BACK 确认／不确认 | 确认 → 写 `Data/Tilesets.rxdata`＋`$data_tilesets` 替换＋**重启 RMXP 提示**；不确认 → 无写入；Exit 确认才退出并恢复地图工厂/精灵组 |
| M10 遭遇集新建与冲突（人工夹具） | a) 新建（图 5, 版本 0）不存在；b) 同（图,版本) 已存在 | a) 注册空集（step_chances/types 空）并定位；b) "已存在"消息、不建 |
| M11 遭遇集复制（人工夹具） | 复制到（图 7, 版本 1） | **深拷贝**（step_chances 逐项、槽数组逐槽克隆）＋保留 suffix＋注册；冲突同样拒绝 |
| M12 遭遇集保存与丢弃（人工夹具） | a) 删除一个集后退出确认；b) 同样删除但退出不确认 | a) save＋write_encounters（删除落盘）；b) **load 重载——删除被撤销** |
| M13 遭遇类型编辑（人工夹具） | a) 新增类型；b) 改类型为已被本集使用者；c) 改步数率 | a) 未用列表选择＋**步数率默认 trigger_chance**＋进槽编辑；b) 该类型不在可选列表（排除）；c) 0–255 写入（即时内存） |
| M14 遭遇槽编辑（人工夹具） | a) 新增槽；b) 编辑槽使最低级 > 最高级；c) 删除槽 | a) 缺省 [20, 首个物种, 5, 5] 追加；b) **两值交换**；c) 确认后删除（均即时内存——最终由集列表退出确认决定落盘） |
| M15 指标编辑循环（人工夹具） | 选物种 → 菜单五项确认某项 | 浏览即预览；确认后 **(当前+1) mod 3** 前进到下一参数项（模数 3 如实登记） |
| M16 单项定位（人工夹具） | a) Set Enemy Position 调 x/y 后 USE；b) 同样操作后 BACK；c) Set Shadow Position 调 y | a) 写入＋metricsChanged；b) **恢复旧值**；c) **y 不可调**（阴影只有 x——UP/DOWN 无效果） |
| M17 阴影尺寸（人工夹具） | a) 物种有自有阴影图形；b) 无：浏览尺寸列表后 BACK；c) USE 确认 | a) "不可编辑"消息拒绝；b) **恢复旧值**；c) 写入＋metricsChanged（ACTION 则并前进） |
| M18 单体自动定位（人工夹具） | 某物种当前 back y 与算法值相同且 altitude 为 0／不同 | 相同且 altitude 0 → **不写**（无 metricsChanged）；不同 → 写 back/front y＋altitude=0（**x 与阴影不动**） |
| M19 全量自动定位（人工夹具） | 调试菜单确认执行 | **遍历全部物种×形态**：位图存在才写 back/front（算法 y，front +4）；**front_altitude=0、shadow_x=0、shadow_size=2 无差别覆写**；完成即 save＋write_pokemon_metrics（无二次确认） |
| M20 指标保存与丢弃（人工夹具） | a) 有改动退出确认；b) 有改动退出不确认 | a) save＋write_pokemon_metrics；b) **load 重载——全部指标改动丢弃** |
| M21 无效图块修复（人工夹具） | a) 全地图扫描（某图有 3 个无效图块＋1 个事件页无效图形）；b) 全部有效 | a) 4 处写 0＋**该图立即 saveMap**＋控制台逐图列出＋RMXP 警告消息；b) "No invalid tiles were found."（无写入） |
| M22 有效性判定（静态核对） | a) ID<384 且自动图块名为空；b) ID≥384 通行表无该 ID | a) 无效（写 0 候选）；b) 无效（写 0 候选）——其余有效保留 |

## 12. 证据与来源（traceability）

- **本轮复核（2026-10-02，首版）**：三份世界编辑器文件**分段全文阅读**（`003_EditorScreens_MapConnections.rb` 1–578；`002_EditorScreens_TerrainTags.rb` 1–263；`004_EditorScreens_SpritePositioning.rb` 1–411，共 1,252 行）。
- **同基线复用（WP73-A／WP72 已全文阅读，字节不变）**：`001_Editor screens/001_EditorScreens.rb:6–340, 779–817`（遭遇/地图元数据编辑器）；`003_Debug menus/003_Debug_MenuExtraCode.rb:668–739`（无效图块修复）。
- **定点阅读**：`004_Game classes/005_Game_MapFactory.rb:383–420`；`010_Data/002_PBS data/001_MiscPBSData.rb:14–26`；`010_Data/002_PBS data/010_SpeciesMetrics.rb:14, 71`；`006_Map renderer/004_TileDrawingHelper.rb:164`；`001_Technical/001_Debugging/003_Errors.rb:76`。
- **继承同基线既有记录**：WP73-A（属性框架/列表器/持久/选择器——`4c3e591c`）；WP72（调试入口与工具归属——`49731474`）；WP04（PBS 编译/反写）；WP11（地图拓扑/连接语义）；WP12（地形/移动语义）；WP15（资源匹配/素材）；WP36（遭遇数据语义——trigger_chance/槽结构引用）；WP16（小地图/战斗背景引用）；WP59/WP61（`d84dff78`）、WP53（`75fc4db7`）、WP37（`d032f5b7`）、WP65、WP67-A/B、GR-001～016、WP23-N01（各自具名通过范围）。
- 全部静态证据；**无运行确认**（未运行编辑器/游戏/UI、未执行编译器或反序列化、未写 PBS/.dat/地图/图块组文件、未播放音频、未操作真实存档、未调整宿主界面、未访问网络）。

## 13. 未决问题

1. 编辑器实际运行表现与宿主窗口/素材行为（小地图、战斗背景、阴影图形——WP15/WP16/U01）。
2. `Compiler::MapData` 的地图读写完整合同与 `Compiler.write_connections/write_map_metadata/write_encounters/write_pokemon_metrics` 的诊断输出（WP75/WP04 主责——本包只引用调用点）。
3. 连接数据运行时消费（地图拼接显示/跨图事件——WP11 主责）；生成连接与实际通行的一致性验证需运行（保留）。
4. demo 中各编辑器入口的默认可达性与真实使用编排（WP77/U01）。

## 14. 状态与后续

- WP73-B 自身范围（第 1 节六项）已提取并自检，2026-10-02 首版登记 **ReviewPending（具名静态范围，待统一 review）**；不自行标 Reviewed、不宣称通过。依据用户批次授权（WP72＋WP73-A＋WP73-B）与 `planning/extraction-plan.md` 的 WP73-B 任务定义执行；三份世界编辑器文件分段全文阅读、同基线复用 WP73-A/WP72 证据、持久层与连接存取定点核对并建立覆盖映射（见交付目录附表）。
- **已通过边界原样继承**：WP73-A（`4c3e591c`）、WP72（`49731474`）、WP04、WP11、WP12、WP15、WP36、WP16、WP59、WP61（`d84dff78`）、WP53（`75fc4db7`）、WP37（`d032f5b7`）、WP65、WP67-A/B、GR-001～016、WP23-N01——本包只引用其合同，不重开、不修改 reference。
- **WP73-B 完成 ≠ F18-02 完成**：编辑器运行验证、素材、demo 编排保留；Feature Matrix 按聚合规则分别显示，不将整个 D18 标完成。
- 后续包引用本文的世界编辑器合同（连接生成算法、取消语义表、自动图块整组、自动定位算法、修复图块逐图保存）时，不得把参考侧类/方法组织当作未来框架的 API；发现与本文冲突的新证据时，先修订本文并通知受影响包。批次完成后统一 review（WP72／WP73-A／WP73-B）与整体 double review（WP78/79）、WP80 净化交付按 extraction-plan 执行，本包完成不自动推进。
