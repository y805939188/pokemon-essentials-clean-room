# X-A-CONFIG-UI-COVERAGE：WP79配置与UI覆盖断言核对

结论：**已完成有界知情辅助；旧覆盖断言需按行限缩及链接既有缺口。** 完整实质阅读指定revision-v4配置表35行与revision-v6 UI关系表17行；新增发现0，新增主审WP0。ROOT保留WP79全局主责。本批不修改旧表、规格、公共Feature Matrix或已发表报告。

固定BASE与参考提交、输入路径、逐行原断言、处置和证据见`audit.json`。证据定位中的A-xx表示本轮agents/A/A-xx，B/和C/表示相应agents目录；WPxx final表示本日志所列净化文件。35/17仅是此任务输入集合的枚举，不是完整性或通过率。每个配置行继续分开机制、样本、文件内容、实际启用；UI各行只把场景ID当导航，不视为已执行测试。

本次允许知情比较。最先固定summary本地380ca0b8读取已提交发现索引与报告；后查远端仍为5de947dc，已立即告ROOT。ROOT明确授权继续使用该本地固定且已审计导入提交，无需退回旧远端重读。`audit.json`保留完整身份；没有把380说成已发布，也没有读未提交工作区。初始两个过宽输出均截断，只记为局部曝光/导航；后续按具名范围读取。

## 配置处置

| 行 | 配置族 | 处置 | 关键判断 |
|---|---|---|---|
| CONFIG-01 | abilities.txt | LINK_KNOWN_GAP | 三层战斗机制和三个孵化样本仍是有效入口；不得等同整个特性配置族闭合。非战斗遭遇消费另接WP36，已有HUSTLE/GUTS身份误述；WP48族标签计数问题另按B018。样本标记精确身份为FasterEggHatching，旧表FastEggHatching仅作导航措辞校正，不另开根因。 |
| CONFIG-02 | battle_facility_lists.txt | HOLDS_AS_LIMITED_EVIDENCE | 五节名单及默认/四杯赛、八挑战身份的引用关系成立；两个fancy挑战都消费_single。专用名单发现、会话消费与生成写出合同具名存在；25行不是设施全生命周期通过证据。 |
| CONFIG-03 | battle_tower_pokemon.txt | HOLDS_AS_LIMITED_EVIDENCE | 设施候选个体读取/构建合同成立；头部样本不能推成所有条目正确或已启用。A-03另读双EV与三EV样本，说明该数据与普通培养写入的数值范围必须分层。 |
| CONFIG-04 | battle_tower_trainers.txt | HOLDS_AS_LIMITED_EVIDENCE | 默认训练家池经专用列表消费；旧头部格式阅读限定可保留。NPC普通训练家文件与设施训练家池不混同。 |
| CONFIG-05 | berry_plants.txt | LINK_KNOWN_GAP | 种植/生长/收获机制存在，但不能继续作为机制已闭合判断：显式更新旧机制覆盖物仍生效，浇水反馈与成熟/重植闪光边界有既有缺口。 |
| CONFIG-06 | cup_fancy_pkmn.txt | NARROW_SCOPE | 只保留“当前名单未引用非_single文件”；本次PBS与Scripts精确字面检索仅命中_single字段。删除“无机制消费者/全局未启用”的无条件读法；动态拼接、外部输入、插件与实际档案不在该检索证明内。 |
| CONFIG-07 | cup_fancy_pkmn_single.txt | HOLDS_AS_LIMITED_EVIDENCE | fancycup单双打都显式引用此个体文件；专用读取机制在案，文件名出现不是数据样本阅读。 |
| CONFIG-08 | cup_fancy_trainers.txt | NARROW_SCOPE | 与非_single个体文件同样，只证当前名单及已搜字面形式不引用；不能由此宣称所有可能消费者不存在或实际绝未启用。 |
| CONFIG-09 | cup_fancy_trainers_single.txt | HOLDS_AS_LIMITED_EVIDENCE | fancycup单双打都显式引用此训练家池；机制引用可留，样本未读不得因名单出现而升级。 |
| CONFIG-10 | cup_little_pkmn.txt | HOLDS_AS_LIMITED_EVIDENCE | littlecup单双打共用本个体文件的引用成立；列表/会话/生成机制存在不等同本文件逐条内容已核。 |
| CONFIG-11 | cup_little_trainers.txt | HOLDS_AS_LIMITED_EVIDENCE | littlecup训练家池引用成立，继续分开文件名、数据内容和实际启用。 |
| CONFIG-12 | cup_pika_pkmn.txt | HOLDS_AS_LIMITED_EVIDENCE | pikacup单双打共用本个体文件；专用编译与名单消费者可链接，不能扩大至该文件样本已读。 |
| CONFIG-13 | cup_pika_trainers.txt | HOLDS_AS_LIMITED_EVIDENCE | pikacup训练家池引用成立；本辅助没有读取池内容，不以引用关系关闭样本缺口。 |
| CONFIG-14 | cup_poke_pkmn.txt | HOLDS_AS_LIMITED_EVIDENCE | pokecup单双打共用本个体文件；文件引用与作者输入合同成立，样本未读状态保留。 |
| CONFIG-15 | cup_poke_trainers.txt | HOLDS_AS_LIMITED_EVIDENCE | pokecup训练家池明确被引用；不将该名字所在名单行作为训练家记录内容证据。 |
| CONFIG-16 | dungeon_parameters.txt | LINK_KNOWN_GAP | cave/forest参数事实及区域/版本选择限定仍成立；零密度合法输入的失败阶段、图样/数量/布局确定性缺口使生成机制不能判闭合。 |
| CONFIG-17 | dungeon_tilesets.txt | LINK_KNOWN_GAP | 两种图块集样本不能替代邻接、墙种、自动图块及布局映射的可计算合同；C048已指出明确遗漏。 |
| CONFIG-18 | encounters.txt | LINK_KNOWN_GAP | 遭遇/雷达/编辑器主责关系成立；专用解析覆盖、零率反写再编译、登记表与当前地图快照、同值版本早退均须链接既有缺口，不能以311行全文作为完备性结论。 |
| CONFIG-19 | items.txt | LINK_KNOWN_GAP | 原引用以招式持物/终局为主，不能代表物品全消费面；补导航到WP27/28主动使用、WP29商店、WP50被动物品。已知回复量、EV上限、仅混乱、TR记录、进化取消与效果存在门问题仍开放。 |
| CONFIG-20 | map_connections.txt | LINK_KNOWN_GAP | 连接记录与编辑器合同具名存在；配置边表不证明通行性、几何可达或边缘转换完整。边缘目标单向阻挡的消费者边界接C052。 |
| CONFIG-21 | map_metadata.txt | LINK_KNOWN_GAP | 天气三例与元数据登记仍有效；消费者远多于天气/编辑器。跨连接天气渐变、旅行落位/逃生点、扭曲世界物种/物品身份，以及战斗音频选择均有现存缺口。 |
| CONFIG-22 | metadata.txt | LINK_KNOWN_GAP | 初始资源、Home与两玩家元数据的样本和编辑器入口仍成立；补WP09/WP24真实消费导航。全局战斗音乐/胜利/捕获回退字段的选择合同挂A059。 |
| CONFIG-23 | moves.txt | LINK_KNOWN_GAP | 招式槽、属性、控制与条款的导航有效；“属性/控制合同在案”不能消去动态目标被误当静态目标、HP平均执行合同移交未接收等已知缺口。 |
| CONFIG-24 | phone.txt | LINK_KNOWN_GAP | 数据/联系人/对话机制确有承接；WP77占位符解释、普通注册部分提交失败、零公共事件ID、每通固定抽样粒度分别已报，不能继续以“已覆盖”隐去。 |
| CONFIG-25 | pokemon.txt | LINK_KNOWN_GAP | 应加WP18/19物种默认字段与属性、WP20招式派生导航；进化/繁殖/设施消费者列表仅是选取的交界。默认值、Ditto资格测试、孵化动态形态的已知问题继续挂接。 |
| CONFIG-26 | pokemon_forms.txt | LINK_KNOWN_GAP | Mega/Primal与进化条件引用有效，但动态形态/展示映射还要接WP21/WP62。BANETTE石身份、ALCREMIE原形/展示名判断、孵化动态提交与扭曲世界具名条件已有问题。 |
| CONFIG-27 | pokemon_metrics.txt | LINK_KNOWN_GAP | 旧样本未读限定仍可留；但指标编辑/保存机制本身不能称闭合：只有基础形态记录时档案可更新而PBS不写，且即时预览、登记表与已有布局消费者不同。 |
| CONFIG-28 | regional_dexes.txt | LINK_KNOWN_GAP | 区域有序内容与图鉴机制确有承接；A-08已全文读两区数据，但搜索取消不复位和区域长度误列可见值仍需修订。读完数据不能关闭消费者问题。 |
| CONFIG-29 | ribbons.txt | HOLDS_AS_LIMITED_EVIDENCE | WP21缎带存储/升级/移除及摘要滚动合同可保持；图标字段是裁切位置而非排序规则。A-04额外具名读NATIONAL相关数据，不能把旧文件级定位状态继续误称为本轮完全未读，也不升级全文。 |
| CONFIG-30 | town_map.txt | LINK_KNOWN_GAP | 区域地图/转换/飞行点导航有效；子格定位、同格多点首条优先、区域参数回退与旅行落位已有缺口。配置飞行点不证明解锁事件或真实可飞。 |
| CONFIG-31 | trainer_types.txt | LINK_KNOWN_GAP | 技能/编辑器/设施消费只是部分导航，还应接WP24身份、性别、基础金钱/资源与WP15战斗音频。下一战覆盖、数组末非空/空文本、直接类型辅助差异由A059承接。 |
| CONFIG-32 | trainers.txt | LINK_KNOWN_GAP | 普通训练家版本/队伍/持物/Shadow装载主责应接WP24；设施池是不同文件与消费者。检查入口未知类型并非都报错，编辑器的空槽与取消/省略值边界已有问题。 |
| CONFIG-33 | types.txt | HOLDS_AS_LIMITED_EVIDENCE | 类型schema与相性主责还应显式接WP03/WP43；AI/卡牌/编辑器只是其它消费者。B-02明确读当前types全文，原表更窄的具名读取并不错误；不外推可选SHADOW类型已启用。 |
| CONFIG-34 | Gen 5–8 backup/ (9 texts each) | HOLDS_AS_LIMITED_EVIDENCE | 四个备份目录各九文本的存在性成立；普通发现不递归与固定检索未见自动切换可保留。内容、与世代配置组合及实际启用仍未证；不能把未读当不存在。 |
| CONFIG-35 | Shadow Pokémon backup/ (4 texts) | READING_SCOPE_UPDATED_ACTIVATION_UNCHANGED | 不能把历史“仅存在性/未读”照搬为本轮状态：A-04已实读Shadow数据131条、四物品、SHADOW类型及18招式指定领域字段，并发现净化数据误改A030。只更新真实阅读范围，U06启用/组合与运行缺口保持。 |

## UI关系处置

| 行 | 功能 | 处置 | 关键判断 |
|---|---|---|---|
| UI-01 | 标题/启动/载入/删除画面（含继续面板与游标持久） | LINK_KNOWN_GAP | T01–T10/T35/T36仍能定位启动/载入行为；不能作标题时间线或继续面板动画已闭合的证明。开场2.8秒名义完整链与确认挂接、步行图预览周期分别链接现存缺口。 |
| UI-02 | 选项/语言设置/紧急保存 | LINK_KNOWN_GAP | 选项即时写入、语言独立、紧急保存交界仍有合同；Screen Size具体倍率/全屏映射不能被枚举端点场景替代。无玩家紧急保存不恢复场景已由WP10承接，不新增。 |
| UI-03 | 暂停菜单（12 项注册：图鉴/队伍/背包/Pokégear/地图/训练家卡/选项/调试/保存/退出/Safari-捕虫退出项） | HOLDS_AS_LIMITED_EVIDENCE | 12项注册条件、保存拒绝仍退出、子屏幕返回差别保持为有限入口覆盖；子界面各自缺口见下行，不重复计为暂停菜单独立缺口。不能将T24某一组合当全部可见性组合。 |
| UI-04 | PC 主导航与会话退出/快捷菜单（ReadyMenu） | HOLDS_AS_LIMITED_EVIDENCE | PC存入门、信箱部分提交及快捷菜单返回/消耗边界可保留；普通PC导航与调试Use PC入口分开，后者缺口放第17行。FLY取消与世界实际飞行合同也分层。 |
| UI-05 | 战前过渡（世界画面进入战斗前；WP79-R02 v5 补提取） | NARROW_SCOPE | BT01–BT16是静态推导场景，不能沿用method_note的“实测”措辞或BT01–BT12旧计数。世界战前选择与战斗内开场分开；新A059音频选择是依赖未承接，不能由过渡播放/清理概述补齐。通用具名转场的C069另作WP16依赖，不重开。 |
| UI-06 | 训练家卡场景（WP79-R01） | HOLDS_AS_LIMITED_EVIDENCE | TC01–TC08对应只读展示、BACK退出、性变独立回退、底边定位与开始时间懒写入，源全文与净化附表吻合。此处只读允许已明确的开始时间副作用；不得由资源名断言素材存在。历史“待复审”只属旧审计阶段，不能替本轮ROOT裁决。 |
| UI-07 | 控制帮助场景（WP79-R03-1） | LINK_KNOWN_GAP | CH01–CH05及末页0.4秒退出有合同，但换页旧页0.5秒/新页0.5秒与期间确认禁用未在现附表自足交付。BACK无响应仍是标准无额外回调的限定。 |
| UI-08 | 队伍界面/摘要 | LINK_KNOWN_GAP | A01–A41只能定位场景族。空重学首绘失败、数量夹具、图标周期、并列IV个性排序、Box Link缩队后旧索引部分提交及零招式选择失败分别挂现有根因。C116与A048是同一根因，保留别名不重计。 |
| UI-09 | 盒子/图鉴界面 | LINK_KNOWN_GAP | B01–B39的存放/导航/搜索入口存在；成功交换后手中仍持被换出者、浏览墙纸写回、美制显示两种换算、形态性别选择及搜索标尺均不能被场景数量关闭。图鉴区域长度误列数字保留A056。 |
| UI-10 | 背包/PC 物品/商店界面 | LINK_KNOWN_GAP | C01–C36仍作入口映射，PC取出预检不泛化为所有库存操作原子性。排序取消保存索引、购买部分回退槽分布、BP数量窗乘数量、图标时序，以及主动道具已知问题仍需修订。 |
| UI-11 | 战斗命令/成长/捕获反馈 | LINK_KNOWN_GAP | K01–K59不能推出战斗UI完整：目标BACK按调用者、无石Mega招式资格、NearAlly缺同伴初选、自动出招辅助失败、Arena提示周期、目标次序与音频选择等已有问题。暗影messages=true例按直接辅助入口解释，正常成长传false，按既有FORM补审不新增问题。 |
| UI-12 | 进化/孵化/交换/净化室/名人堂/片尾 | LINK_KNOWN_GAP | L01–L35与成功提交共享链仍有用，但不能关闭进化末帧BACK先行、取消前已见新种剪影、孵化形态读取提交等差异。净化跨级首窗失败、双满存储后清中心及中途取消保留已提交状态已在原合同/FORM补审中确认，不再报新缺陷。 |
| UI-13 | Pokégear/区域地图/电话/点唱机 | LINK_KNOWN_GAP | P01–P33作路线定位成立；电话注册/公共事件/抽样、区域回退/子格/重复点与点唱机跨图旗标已有缺口。静态电话文本及地图点不等于真实事件可达。 |
| UI-14 | 消息/窗口/选项/数量/按键输入 | LINK_KNOWN_GAP | 无字母编号场景就使用具体表位置的做法正确，不能补造ID。但溢出暂停滚动、负数数量、两命名模式、图片裁剪、实体转义/性别色、缺图路径与命名预览周期均有已知缺口；NA BitmapSprite箭头时序余项单独保留，未硬并C118。 |
| UI-15 | Duel/Triple Triad/Slot/Voltorb/Lottery/Mining/拼图 | LINK_KNOWN_GAP | 七活动的各自编号映射仍成立；旧“批次B通过”不能当本轮通过。Triad副本归并/后手空高亮、拼图五步奇偶不可完成/表外完成路径/显示条件与审计相对路径已有新一轮C08发现。Slot/Voltorb/Lottery/Mining具名保持点继续有限保留，不扩大到求解/随机分布/运行。 |
| UI-16 | 弃用告警机制（WP79-R03-2） | HOLDS_AS_LIMITED_EVIDENCE | DP01–DP05和直接告警/别名两入口、首行必有、可选参数、先告警后调用、正常返回与位置/关键字通道限制可保留。A-02的旧原稿待审标签A019不等同机制不成立；本次净化54行已不保留旧待审句。UI关系中的历史待复审标签交ROOT统一解释。 |
| UI-17 | 调试菜单/编辑器/动画工具/转换/生成器（作者入口） | LINK_KNOWN_GAP | 六作者工具包的场景ID关系仍能导航，但“已覆盖”必须降为已提取且有具名缺口：Use PC、白名单交付、编辑保存/缓存、输入语法、取消部分写入、动画/转换等问题均已登记。WP76正常模拟与直接无视觉辅助的B034分开；工具未运行不是遗漏静态合同的豁免。 |

## 读证与边界

- 原断言逐行位置及现存根因链接在两份dispositions.tsv；直接/既有本人阅读和同行阅读分记reading-log.tsv与peer-reading-log.tsv。同行摘要只作现存问题关联，不冒称A再次独立核过每个source。
- 两个非_single fancy文件仅证当前名单/已搜字面形式未引用，不称全局无消费者。Gen5–8备份本批仍仅存在性；Shadow四文件按A-04真实字段范围更新阅读状态，U06和实际启用限制保持。
- 配置表FastEggHatching导航措辞与UI方法说明BT旧范围/实测措辞随逐行处置校准；它们不再另立行为根因或增加运行证据。
- UI消息箭头的NA审计剩余时序问题仍具名开放，未因为已挂C118或A058就自动关闭。既有B030被ROOT列为非必修的结论不得借此次覆盖表重新算P2。
- 未运行参考、Ruby、游戏、编译器、转换器、生成器、反序列化器、模拟器、真实UI或存档；没有框架实现、源码转译或参考写入。U01–U10、G01–G12、20项AX全部保留；运行观察0，已证Demo事件链0。
- 请求模型/推理沿用显式spawn的gpt-6-astra/ultra；运行时独立回显不可用，speed=UNVERIFIED，未更改Fast/Ultrafast设置。未派子agent。

验证：52行原断言与固定输入逐项一致，JSON/TSV均可解析，输入行段可还原对应记录；114个链接均属于已存在发现编号，新增发现仍为0。该校验只证审计文件一致性，不是参考行为验证。Python只用于文本检查、固定数据序列化及审计辅助脚本语法检查，没有加载参考程序。

仅本目录新增审计产物。正常提交/推送前核origin精确身份、A目录白名单、暂存/未暂存/未跟踪与全部相对BASE提交；精确发布提交由Git及交付回执记录，不在包含自身的文件中伪造自引用哈希。
