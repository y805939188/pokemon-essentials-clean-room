# B15 逐 finding 作者修订

当前增量状态：独立FULL报告e08998ab5d208f7607a4750ab57beb6a4b985bf6已审cc08a9150131b7e9fae8424fb0ede890169dd64f，15项局部PASS、唯一P2 R-B15-C1-001/C122。PD32/PD33已补nil/空串前提与反向；原稿W32/W33已获父精确两行范围批准并应用，before/after全字段匹配；当前为完整四行作者修复待同FULL增量复核。此前完整候选/发布与三原稿应用作为准确版本历史保留，不冒称当前修订已全PASS。

正式输入 `0cfe99094b76f8d75fded0d638694677855a5f0c`；派发管理包 `4cb51a33402ec6559a396226239afe308a4b8849`。16 本地贡献／10 主责；所有项目均为作者候选，非独立批准。三份原 spec 已按父批准的完整精确补丁应用，before/after 核验见 ../author-draft-1/original-sync-application.json；六正式文件字节保持旧草案，现为完整有界可复审作者候选。

| Finding | 本地修订与静态正反设计 | 位置/测试 |
| --- | --- | --- |
| GIR-FD82-003 | 菜单排序/出现条件和联系人持久顺序改为行为事实；记录输入、标识输入的真实失败分叉保留；必要ASCII18旧输入身份单独隔离为兼容合同。 同等领域表示无源类/数组也满足行为；反向仍须满足排序、共享记录、参数顺序与局部异常。 | wp63-pokegear-map-music-and-phone.md §2.2,§4.1–§4.5,§6/§10；P47,P31,P32 |
| GIR-FD82-A054 | 普通登记查展示形态名称，最近见到查原形态名称；基种键、性别差异、刷新与首写保持。 ALCREMIE8普通7→最近0；反向有名原形态映射无名P则普通0/最近P。 | wp62-pokedex-records-regions-and-content.md §3.4,§4；PD26,PD27 |
| GIR-FD82-A055 | Start写排序先于过滤；只退出已有结果态复位0；未Start取消/无结果取消不产生或不回撤本次模式写。 合法默认0区域、有图鉴、仅见BULBASAUR无拥有、最重4空→取消→非结果态退出保持4；非空→结果态BACK才0。 | wp62-pokedex-records-regions-and-content.md §6 主列表搜索；PD28,PD29,B25,B26,B35 |
| GIR-FD82-A056 | 可见区域名/见过/拥有两数字；长度仅参与完成比较。 两区域均可访问各见1拥有0，无第三数字；全见成员时完成标记点亮仍不显示长度。 | wp62-pokedex-records-regions-and-content.md §6 区域选择菜单；PD30 |
| GIR-FD82-A057 | Receive成功个体与管理会话共享；后续Edit先写来源，命名取消不回滚玩家个体；主文件与新建别名缺陷分开。 ID7/PICHU/无蛋/队伍有位/无提示/在线空：Receive→Edit Faraway place→取消，队伍变、[7]标记、主文件不变；未Receive不共享对照队伍不变。 | wp64-mail-and-mystery-gift.md §7,§8；MG-29,MG-31,MG-32,MG-30 |
| GIR-FD82-C003 | 本地测试迁移等价恢复采用命令后/换图后双观察点，归C113同一修订；不重复增根因或扩大到FS/FP/编辑器其他owner。 命令higher真→新图两旗标假；反向Custom覆盖跨图保持但旗标仍清。 | wp63-pokegear-map-music-and-phone.md §6,测试P29；P29,P44 |
| GIR-FD82-C007 | 完整18旧公开入口逐项输入/默认/行为/返回/失败已在最终允许集合内；0版本数误置/Reset参数求值优先保留。 每入口成对夹具在PL表；pbPhoneRegisterBattle版本3→版本数1起始3，对照预检/确认拒绝；pbPhoneReset先未定义参数错误、正确记录重置单列。 | wp63-pokegear-map-music-and-phone.md 新增§4.6；PL01–PL18,P45,P46 |
| GIR-FD82-C020 | Custom缺目录先于枚举/子列表/清覆盖，与存在空列表USE/BACK分开。 覆盖A、前置UI正常；缺目录保A/旗标；空USE清覆盖旗标；空BACK保持。 | wp63-pokegear-map-music-and-phone.md §8 Custom；P43 |
| GIR-FD82-C107 | 合法文本类型被规范化并新增，普通反馈用原输入查找失败；静默/规范身份/未知身份四+拒绝门分列。 CAMPER/Jeff/合法事件/同键无可见/缺省版本；文本普通新增后失败，静默true，规范两入口true，未知false无新增。 | wp63-pokegear-map-music-and-phone.md §4.3；P39,PL01,PL02 |
| GIR-FD82-C108 | 只有正公共事件ID才分派；NPC0/省略会在训练家消息类型校验失败；正缺事件的全局助手false不与解释器同名成员混用。 有信号、现有NPC记录：0失败且记录保留；正缺事件提示、正存在进入事件；无信号更早拒绝。 | wp63-pokegear-map-music-and-phone.md §5.1,§8；P40,PL03 |
| GIR-FD82-C109 | 请求参数存在性门与实际区域严格查询分开；无定位优先0、有定位未知请求回当前。 当前0有效请求99回0；请求已登记不同1到左上；实际当前99或回退0缺失严格失败，P33保留。 | wp63-pokegear-map-music-and-phone.md §3.1,§8；P34,P33 |
| GIR-FD82-C110 | 正宽门、ceil长度/宽高度、两轴floor整数偏移、轴维1不偏移、仅字符串长度语义。 (13,12),20×20,w3,S10000,(19,19)→h2偏移2/1终15/13；同长11111相同、w1长度1无偏移。 | wp63-pokegear-map-music-and-phone.md §3.1 子格；P35,P36 |
| GIR-FD82-C111 | 内容顺序首同格记录决定；隐藏/缺字段不补后项，图标与USE同治疗查询；CTRL只豁免访问。 首条开关51关且后条完整→三查询空；首条可见缺治疗→名称A但治疗空；反向交换/补完整首条生效。 | wp63-pokegear-map-music-and-phone.md §3.2,§3.4；P37,P38 |
| GIR-FD82-C112 | 每通TP/TE各一次；队伍成员等概率；首非空Land/Cave/Water表前至多四槽均匀，不权重/不去重，第五不参加；缺表/记录空回退明确。 四槽权重97/1/1/1电话每槽1/4；A/A/B/C→A1/2；多段重复固定；Land空到Cave、再Water、皆空或无记录TE空；普通遭遇合同不改。 | wp63-pokegear-map-music-and-phone.md §5.3,§4.6；P41,P42,PL15,PL16,PL17 |
| GIR-FD82-C113 | 拆命令后/新图设置后旗标；全局覆盖独立保持，音乐请求与实际宿主输出边界明确。 无覆盖March后false/true，新图false/false；Custom A对照跨图保A但旗标仍清；无事件插件再写前提。 | wp63-pokegear-map-music-and-phone.md §6,§7,测试P29；P29,P44,P30 |
| GIR-FD82-C122 | 正确§6.1保持；R-B15-C1-001定点补PD32/33原始/本地化nil前提与空串反向。PD32/33合法RATTATA基础FormName省略使原始/本地化标签均nil；显式空文本且本地化仍空串对照：异图两项空标签、同图结构多形态一雄档空标签；nil异图Male/Female、nil同图结构多形态One Form，去结构多形态清空。结构门/排序/首轮写回保留。 W32/W33两行已按父批准精确应用，不签新SHA独立PASS。 | WP62 §6.1；PD31–34/W31–34、既有B31/B38 |

完整来源范围、前后身份、控制绑定、验收动作与限制见 finding-revisions.json。C003/P29 与 C113 共用一处修订但保留两个贡献记录；C007 的67树果数据条件性范围未升级。A056 的 WP66-B 交界由 B16 后继贡献解决。

C1-001当前应用见 `../author-draft-1/label-nil-original-sync-application.json`；旧FULL候选→新候选九路径/精确四行及未变15贡献/正确正文证据见 `C1-001-delta-and-protection.json`，完整未过滤增量与正式基线diff由新publication receipt绑定。父已取消此前3任务上限，作者仍不派重复任务。
