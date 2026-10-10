# B19 候选 affected 独立复审

结论：**PASS_SCOPED**。没有阻塞本次候选 affected 门的发现。范围为全部 B01–B18 的有证据支持的局部接口判定及旧接受材料保护；不代替 FULL 作者复审，不签整合后的 actual，不作正式接受。

审查对象固定为 NEW `dfe8e726669a83c751d02e923cf290bdafc82bd7`，tree `b830a49ad76369d19ebaae227aaf190ca5542069`。正式 before 为 B18 C `52f24036d09503144c6ec89960029db4ed370734`，tree `3b20f8f2c0dab0ef3e2867aa2bac0fa98497c44b`。发布包 `393ec2680af6e118c1fc959fd0c6290d0cb7c82f`，tree `fa5b613f5296f67dd4ac4eca301b3fe6bcddc118`。下文 N/C/P 分别仅指这三个固定 commit，不使用移动 tip。

固定派发入口为 P 的 `review/remediation/20261003-prepare/batches/B19/author-draft-2/full-candidate-1/publication-1/affected-independent-dispatch.md`，blob `44647c3fc2c599601d15b0e13408ed6b7ea35833`，SHA-256 `704fbe207081fa91c04cb68d2404f820597e6adaf44fd3922994c306c9a378c8`，4253 bytes。先读该入口及原合同；管理包 `a2806c3e30391dca7a804294b8221f857449f847` 下 `review/remediation/20261003-prepare/batches/B19/refreeze-after-B18-C-1/author-contract.json`，blob `c4213c00068fa04e8bfadebf437762163547a494`，SHA-256 `cd36fa966985261b0001f878c6a0f531794089fd4c4a8be22fa93d819edc0618`，13838 bytes。管理包不替代 C。

## 独立差异与证据身份

从固定 C/N 重建整个仓库的无路径过滤差异：`git diff --no-ext-diff --no-color --binary --full-index C N`，1802585 bytes，SHA-256 `07fff7e0391c6bde1bc233a336423e89a6618809231ea04c6e74e6a44d466dd6`。实际为七个既存 payload 修改、27 个新增 B19 作者证据文件，无删除、无七 payload 外的旧文件修改。逐项列表及前后完整 blob 见 [independent-verification.json](independent-verification.json)，不是作者 status 的转录。36778 个 C 已跟踪路径在七 payload 之外全部保持。

再按已独立核对的七个 manifest 路径、原顺序重建完整 payload diff，逐字节等于 N 中唯一发布流：`review/remediation/20261003-prepare/batches/B19/author-draft-2/full-candidate-1/full-unfiltered-C-to-NEW-payload.diff`，blob `c542891696660d5dac52dd19fed00bc947dc6391`，382948 bytes，SHA-256 `61b58208423530ed62fa4fe7a4868bb7cb06ca03e750914fc22f77f3b573df64`。本报告不再复制 diff 正文。整个仓库差异与七 payload 流是两个明确对象，不将后者冒充整个仓库差异。

72 项冻结输入的 before/review 共144次身份比对全部匹配；24个完整 original/approved control 对象按固定 JSON pointer 与 canonical JSON SHA-256 独立复核全部匹配。完整对象绑定与字段控制来自原报告 `93e10babe0b9c9ef8b3f5277754541b447beeeb4` 的 `review/global-independent-review/2026-10-03-fd82a639/findings.json`（SHA-256 `7c2f0b9159f7be21d8ae9d647399521017500fe4c40ffed042c004492c6a242d`）及批准计划 `41fffb540c6483f5296ea0d33b789b75180d27ed` 的 `review/remediation-20261003-prepare/finding-acceptance.json`（SHA-256 `54e4c86be3db493a5463ce4bcdef81c7184f1a1d89e6b3bbea358f14cc347225`）。使用 current qualifications/root/extension 的有效约束，不以旧 checkpoint 或作者局部例子替代。

grant-2 `4ceec8e78604d13bcf884b013300e1beb3e200d0` 的获准完整 after 与 N 的 WP72/73-A 原稿全字节一致，分别17/16条、92128/56632 bytes。许可只证明范围，质量另外按实际接口判断；没有据此扩大正确原稿的003清理范围。WP73-B既有应用与其他未改材料保留。

## 全部 accepted owner 的范围判断

每行有独立事实、确定再检条件及实际静态读取 L 编号；完整判定见 [owner-judgments.json](owner-judgments.json)，L编号的固定 commit/path/blob/SHA-256/bytes/范围见 [source-reading-log.json](source-reading-log.json)。BOUNDARY_PRESERVED 表示接口保护检查通过，不是免审或整个 owner 新验收；B18 的非影响结论只覆盖下面固定案例。

| Owner | 旧接受数 | 判定与实际范围 |
| --- | ---: | --- |
| B01 | 14 | AFFECTED_INTERFACE_PASS；遭遇与指标 archive→PBS→compile；物种旧进化编辑和编译重建的时序。 |
| B02 | 12 | BOUNDARY_PRESERVED_PASS；共享数值/文本消费边界；时间、统计、保存、迁移及语言系统的接受内容未改。 |
| B03 | 27 | AFFECTED_INTERFACE_PASS；连接生成、元数据取消隔离、地形标签、事件变量刷新、ASCII事件名/注释解析保护。 |
| B04 | 35 | AFFECTED_INTERFACE_PASS；数值/消息解析、资源预览/目录与动画名称/音乐兼容、指标显示消费边界。 |
| B05 | 16 | AFFECTED_INTERFACE_PASS；实际HP/状态/能力/招式/Shadow数据消费者；空route表不能免审。 |
| B06 | 10 | AFFECTED_INTERFACE_PASS；玩家角色延后效果、训练家编辑默认IV/EV、demo队伍构造与PC/storage容量交界；空route表不能免审。 |
| B07 | 19 | AFFECTED_INTERFACE_PASS；通用教学、EV随机重置、编辑与自然成长/培养的边界。 |
| B08 | 17 | AFFECTED_INTERFACE_PASS；遭遇登记vs当前地图快照、版本赋值与setup、Day Care选择变量及漫游/育种条件保护。 |
| B09 | 20 | AFFECTED_INTERFACE_PASS；测试战斗入口与场上/持久写回；实际DG-M18数量反例。 |
| B10 | 7 | AFFECTED_INTERFACE_PASS；Wonder Room有效查询vs原始能力赋值、120调试效果范围与正常天气/场地/伤害生产者边界。 |
| B11 | 6 | AFFECTED_INTERFACE_PASS；可编辑效果与普通招式/特性/道具触发的消费边界；空route表不能免审。 |
| B12 | 9 | BOUNDARY_PRESERVED_PASS；AI对战斗字段/空间状态的消费；算法与Safari/Contest接受内容未改。 |
| B13 | 8 | BOUNDARY_PRESERVED_PASS；Palace行为标记、设施资格与录像入口保护。 |
| B14 | 24 | BOUNDARY_PRESERVED_PASS；24小时四通道完整表、字段刷新与条件berry67保护。 |
| B15 | 16 | AFFECTED_INTERFACE_PASS；音乐文件/目录、电话18旧接口全集与UI正常入口保护。 |
| B16 | 24 | AFFECTED_INTERFACE_PASS；普通PC服务与直接boxes、选择器写回、Shadow普通教学和取消。 |
| B17 | 12 | SHARED_CATALOG_AFFECTED_PASS；共享demo目录旧178行/29项完整行修订与设施PA040三行、演出交界。 |
| B18 | 8 | NO_CHANGED_ACCEPTED_BEHAVIOR_SUPPORTED；真实三目录与Tile原稿/已接受T01/T18前提的保护核查；无实际B19调用进入Tile。 |

B05/B06/B11 的 route 输入为空仍实际核对了 Shadow Teach、训练家默认/储存及效果消费者；B09 的数量反例也按真实 C003 控制检查，未机械继承 route 的共有 ID 集。其他 owner 的未变正文哈希只作保护证据，具体影响仍取决于调用者、数据与条件。

## 关键跨系统核查

**B01/B08 PBS 与快照。** Land 概率0在登记/档案为0，PBS头省略第二字段，成功重编译成为默认21；OldRod0与Land70分别仍为0/70。保存、取消或调试Compile不等于当前地图快照setup；同版本早退，异版本有地图/遭遇上下文时才装配，宽限4→0、累积210保留。指标非0形态查询可懒建记录；路径依据保存时非0形态后缀，即使五组与基形态相等可选路径但省行；仅基形态不导出路径。档案先成功后PBS失败没有整体回滚保证；既有战斗显示无自动布局广播。旧进化编辑删除源的旧后继，父Yes仅保存当前对象；反向前驱记录在fullcompile才按前向关系重建；PBS单项旧参数转换是另一时刻。L001–L010、L055、L068、L071、L087–L089支持这些边界。

**C003 相邻前提。** 普通UInt/有界数值BACK回夹限旧默认，与可空型−1清空、普通确认与三态布尔分开；Pocket列表序号+1写身份、取消保旧0。DG-M18的一名/两名训练家与两席对照保留，首家仅1个体不独立构成拒绝门。.mid/.wav与.midi末三字符筛选保留；CommonEvent独立注记不收集，接在Battle、EndSpeech、EndBattle块时按实际收集/更早分支顺序区分。B/pg/CN及`&bs;`/`&fs;`斜杠实体保持准确，不能概括成一般文本标签。Move:/OppMove:/Common:/item:/hiddenitem:/SellItem(...)/Trainer(N)的ASCII冒号、括号、逗号和大小写/空白条件与全角负例都保留，Common:X与Common: X是不同精确公共名。L011/L018/L034–L038/L059–L061/L067/L069/L075/L076/L079/L082/L083以及共有目录的完整修订行支持；未变非本地 encounter/育种/FS/消息/Tile 前提没有被局部属性例子覆盖。

**真实调用者。** Field Use PC进入正常服务选择，另一个入口直接整理boxes。Day Care chooser包括BACK仍写选择变量1/名称变量3及刷新请求，业务提交另门。battle Teach绕通用Shadow拒绝，只做无个体/已会/满容量门，取消和成功追加两层列表分开；战斗外使用普通教学，即使debug仍拒Shadow。Wonder Room有效防/特防查询交换而赋值写原始数值，本菜单缓存与重开回读不同；没有回合推进、整体退出清空或持久能力重算保证。L011–L025、L039–L048、L062–L069、L077/L080/L081支持；据此只限定接口，不改写普通战斗、学习、Shadow、AI或设施接受合同。

**C007 完整集合。** 120个调试效果的行为标签实际读源，完整按顺序比较每项类型、登记默认、合法范围和ACTION复位，83成员/22阵营/13全场/2席位全部匹配，详见 [effects-parameter-verification.json](effects-parameter-verification.json)。E088登记−2、整数编辑/复位−1，不是成员引用；当前引用空位首次显示失败、选择候选空位跳过，人工空尾RIGHT可持续循环，均未修成正常成功。既有24小时四通道表（L027）、18旧电话接口全文表（L028/L029）逐项读并保持原字节。35有序字符串转换对及两条治疗循环字面规则实际从L035源读，不缩为示例；它们所属的完整WP75/B20责任保持，CV-M18没有被本次评为完整35项交付。条件berry67与未读样本继续留名，不改成无条件完整内容兼容。

**C020 目录与异常。** Graphics/Music列表直接Dir.chdir；缺目录失败在“无文件”与正常释放之前。存在的空目录才正常空列表/返回。训练家图形预览有局部保护、普通Graphics预览无对应保护；正常BACK/空列表释放不等于任意异常都会清理。L037直接核对实际分支；音乐/资源非本地case及宿主结果未获升级。

## 旧接受材料与目录保护

284项接受记录的固定路径为 C 的 `review/remediation/20261003-prepare/batches/B18/acceptance-stage-1/completion-statistics-successor.json`，blob `e7579392696cf24b86f8a35169a2afdb2d739107`，534331 bytes，SHA-256 `336a267b23b941ab9b14dceab0ceead26d351eb0ae68906cf4b8215d7504cbac`。N字节相同，逐owner数合计284。没有新署这些回执或将局部候选结论登记为新accepted贡献。

共有demo目录 C→N：178旧ID全部存在，次序和重复次数相同；29个完整旧行修订与声明修复集合一致，但比较从独立旧/新字节开始；149个未分配旧行逐字节相同，新增17，现195行。三项B17-PA040保持原字节，255+255=510设施样本与普通培养252上限分开，重复HP/ATK/ATK仍分母3、170+170=340，未受debug随机EV清零/目标规则污染。旧行哈希与行号列在verification中，不复制整个旧目录。

B18的三个真实目录全部与C字节相同：`creature-rpg-wp35-36-57-64-68.md` SHA-256 `80fa89a5218128818921cba2a8ef8235162d9462b158c20010795e798c79b235`；`pokemon-rules-wp53-60-61-62-69-70.md` SHA-256 `64dedc58ba566e10f20856efe7492364702207a01cdeb6dae9283b25a134d159`；`user-interface-wp17-63-65-66-67-68-69-70-71.md` SHA-256 `a3ac311fcd9dc89e4ebad2df39cfc737d41c5fbb3b0a054f3e8a744ddba30abd`（均在`deliverables/final-specification-set/test-catalog/`）。Tile原稿 `specs/ui/wp71-tile-puzzles.md` SHA-256 `6983c79f864ac928e88c3984ebb6bf7cb7d083f8c1198a60f42c61727e4ef06e`也相同。L051/L052实际读取了T01空手/格0空、T18合法完成态及三反向案例，且B19没有进入其动作域的实际新调用。哈希保护与条件判断同时支持局部非影响结论。

非阻塞文字记录：N净化WP72第72行“取消服务选择返后续处理试流程”有错词。PC源及同目录B19-C008明确支持取消后返回调试流程，未形成互相冲突的服务/写入条件；本报告记录原字节，未改正文。若再修正文，应重新冻结实际目标，不从本报告推导许可。

## 限制与后续门

只进行了固定参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0` 的真实静态文字读取和新写Git/JSON/hash/text操作。未执行game、Ruby、编译器、转换器、生成器、反序列化器、旧程序、随机模型或行为向量；运行观察/已证Demo链均0。metadata读取/哈希匹配不冒充完整72篇或各owner整包语义复审；本报告逐项列明实际有界接口。

全部 U01–U10、G01–G12、AX01–AX20 与具名未读/条件限制保留，包括地图/事件与序列化二进制、实际媒体/字体/宿主/插件组合/配置容量、8杯赛名单、pokemon_metrics样本、backup/gen、动态阴影/EventScene/deprecated未穷尽及条件树果67。没有执行或补读这些保留材料来制造运行/内容证明。模型参数接纳按派发有效；无额度/认证/回参探测，无CLI模型回退，遵守合同未创建额外或嵌套任务。

canonical仍229 OPEN/0 CLOSED。本次PASS_SCOPED仅绑定上述N/tree；之后唯一registrar的G/ACT整合、固定ACT/tree上的独立FULL和supported affected actual门、正式C接受都未由此完成，也不因blob相同而免除。除本目录复审报告及自己的支持元数据，未修改正文、main、原稿、参考或旧证据。
