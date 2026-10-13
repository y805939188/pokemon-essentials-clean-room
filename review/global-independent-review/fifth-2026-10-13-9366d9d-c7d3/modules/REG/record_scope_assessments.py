"""Persist manually reasoned REG scope comparisons; no inference from historical verdicts."""
from reg_io import *
OUT=HERE/'scope-assessments.json'
def add(batch, text, boundary, primary_modules):
 d=json.loads(OUT.read_text()) if OUT.exists() else {**BASE,'complete':False,'method':'Manually reasoned qualified scope comparisons against actual fresh semantic records; evidence addresses and pending gates are joined separately.','records':{}}
 for line in text.strip().splitlines():
  if not line.strip():continue
  ident,reason=line.split('|',1);key=batch+'/'+ident.strip()
  d['records'][key]={'record_key':key,'status':'supported','evidence_level':'supported_static','current_behavior_comparison':reason.strip(),'qualified_scope_boundary':boundary,'primary_modules':primary_modules,'scope_review_complete':True,'evidence_join_complete':False,'no_historical_verdict_transfer':True,'execution_status':'NOT_EXECUTED','final_required_signature':False}
 save('scope-assessments.json',d)
if __name__=='__main__':
 raise SystemExit('Final manual341 assessments reside in scope-assessments.json; import add only for an explicitly reviewed amendment.')
 add('B01','''
GIR-FD82-A001|耗尽奇数引号合并时保留尚未到达后续剥离步骤的文本，不能套正常闭合引号结果；M01 active splitter 与 KL10 当前例匹配。
GIR-FD82-A002|新鲜度比较使用最大整数秒时间；相等仍触发，非直接浮点mtime比较；M01 trigger/failure分段已保留。
GIR-FD82-A003|缺失/假值Scripts与已给空列表分开，空列表仍走自动发现；M02插件metadata具体比较支持当前§5.1。
GIR-FD82-A004|完整路径含.rb子串的递归候选与显式列表在前、文本去重/顺序分开；编译/执行阶段沿各自守卫，不是统一按扩展名筛选。
GIR-FD82-A006|此B01贡献仅WP02的作者翻译导出目标与玩家当前语言分离；不能以选择导出语言推游戏切换。
GIR-FD82-A009|依赖/版本错误消息中的Link仅在元数据提供时使用；EP08具名Link前提保留，不把所有插件错误强制带链接。
GIR-FD82-A020|此贡献为WP03对固定Nature目录的交付指引；25身份、20升降配对/5中性由当前WP19及M01固定Nature记录承接，不把此处算成另一性格能力。
GIR-FD82-C004|只在WP04反写边界登记非正遭遇率省略及成功再编译按类型默认恢复；完整编辑/当前地图快照职责仍由B08/B19范围承担。
GIR-FD82-C016|非零形态决定指标输出文件路径，先基础记录写入不保证该文件发生反写；M01 metrics query与writer的当前比较一致。
GIR-FD82-C022|复数编辑读取与单数导出字段的差异及导出参数字符串化时点被分列；此处不替代B19编辑对话的完整状态合同。
GIR-FD82-C080|专用遭遇解析不套通用重复拒绝：同类型槽覆盖/概率缺省保留、严格正槽数值与宽松map/version/chance转换分别承接。
WP80-B02-R01|WP02 §7将来源结构统计/审计身份定位与独立配置行为分开；M01当前配置声明/消费者记录不把统计数量当新运行保证。
''','B01具名主文/原稿同步或入口导航局部贡献；原接受引用和其他批次责任不扩大。',['M01','M02'])
 add('B02','''
GIR-FD82-A006|作者导出选择/取消不切换当前游戏语言或消息；真实启动、载入选择和直接保存仍为不同入口。当前WP08与M01实际导出/加载比较支持。
GIR-FD82-A010|采摘最大产量统计按单株采得果实数量与既有最大值比较，不是种植株数；74字段及直接写入者当前核对支持。
GIR-FD82-A011|交易统计在演出之前增加，不以完整交换最终成功为门；当前M02 stats与M10 trade顺序相互匹配。
GIR-FD82-A012|递归删除含目标目录本身；导出覆盖消费者保留删除时机和失败前缀，不变成仅清内容的入口。
GIR-FD82-A013|导入节头使用非零整数前缀再常量识别；数字0不能当合法编号入口，域目录含0并不改变节头算法。
GIR-FD82-A014|旧地图恢复的分支条件是事件集合缺失，空集合不是同一条件；当前startup/map-restore/失败合同有此分流。
GIR-FD82-A015|SV02仅在无存档等具名前提下预测New Game；有效存档与跳过标题配置另判，不扩大为固定启动画面。
GIR-FD82-A016|旧帧统计迁移保留给定帧率除数与零/假回退，存在stats键（即便nil）阻止补建；不把迁移证明外推真实旧档全链成功。
GIR-FD82-A018|LZ08–10以具名非地图节为输入才适用数组形态/第一保留值规则；地图域的独立拒绝顺序不混入。
GIR-FD82-C003|只保留B02时间/月/季节辅助的具体数值和布尔输入族，区分查询值域/取消子型；其他CE-M02消费者不由该贡献闭合。
GIR-FD82-C081|普通玩家计步在2^31边界回绕，强制/解释器移动仅通用通知且不计该累计；与距离统计不同。
''','B02有限核心/本地化/统计范围；source能力的其他partial子范围及新M02候选不继承此结论。',['M01','M02','M10'])
 add('B05','''
GIR-FD82-A020|25性格完整顺序与升降数据及分步取整已在M04.nature/M01-Nature逐项对照；表现性格与计算覆盖分层保留。
GIR-FD82-A021|WP18物种构造默认表不统一为空；缺/非正基本能力归1等当前字段与M04/M01构造比较吻合。
GIR-FD82-A022|创建回调可能增加随机/派生读取与同值提交；不能把PID/IV两类随机来源说成无例外全集，当前创建和形态记录明确分层。
GIR-FD82-A023|四槽学习入口与直接整表写入不同，合法零/五槽状态保留，不能把容量当所有写入者共同不变量。
GIR-FD82-A024|重学使用已记录最初招式而不是即时全部蛋招式目录；通用查询与更多候选配置的UI消费分开。
GIR-FD82-A025|按索引遗忘的负索引从末尾计数，越界不删；当前招式状态源比较与HP38/39资格吻合。
GIR-FD82-A026|六族具名形态/招式与记录存在门由当前WP21映射表承接；提交/战斗进入离开时序分列，不推额外道具消费者均已审。
GIR-FD82-A027|ROTOM目标招已会时删旧特殊招，压缩/空招边界与新对象PP不同于直接改身份；当前形态commit比较支持。
GIR-FD82-A028|BANETTE目标Mega石为固定默认对应，48资格数据与主文一致；不凭译名创造另一物品身份。
GIR-FD82-A029|香的无效门包括友好度255及心量表等入口条件，不能换为心阶段5；field/battle及Hyper各门分开。
GIR-FD82-A030|可选131个体配置、18招/4物品按固定输入逐记录核对；GROWLITHE/SNORUNT首招正确。只签内容身份，不用该表替代Shadow战斗效果执行合同。
GIR-FD82-A031|SH06的90下降需给定存储性格；计算覆盖不改变该系数，附表25×4与Scent乘数分别保留。
GIR-FD82-A040|普通培养的252/510不约束所有直接写入，设施255反例和重算存储分层保留；不把源异常合理化。
GIR-FD82-A044|背包TR成功额外写最初招记录/教学统计，队伍Item→Use没有这套包装；当前通用学习记录及双入口例一致。
GIR-FD82-C124|IV并列先按PID模6起点沿HP/攻/防/速/特攻/特防取首最高，再余5选文意；不混PBS数字列顺序。
GIR-FD82-C126|零已知招普通页可画空槽，详情/遗忘入口先于BACK循环失败；正常不足四招教学直接成功，有限合同与M04/M10交界一致。
''','B05个体/形态/默认与可选数据的具名局部范围；新三自然特性候选、摘要只读矛盾与专用Shadow执行缺口分别归现有GR5候选，不据旧表级接受扩大签名。',['M04','M01','M10'])
 add('B08','''
GIR-FD82-003|WP36/37已把观察状态、索引身份和副作用从源对象组织中分离；必要当前遭遇快照/漫游持久身份仍保留。
GIR-FD82-A034|伙伴排除位于雷达遭遇钩子；通用战斗启动许可本身没有同一门，当前M06雷达与M07入口交界分开。
GIR-FD82-A052|不可繁殖等先行资格先于Ditto例外；原PICHU对照仍拒。WP34保留只读、直接产蛋工具不自动复用该前门；新无性别绝对句问题是另一个默认配对范围。
GIR-FD82-A053|孵化核心提交与演出读取动态形态分层，演出可以在形态查询时提交变化；EG13/20保持，不将此等同所有图像都动态。
GIR-FD82-B026|捕虫缩队不清伙伴；步行候选生成/单敌覆盖/伙伴普通准备次序分别存在，不能从单员队伍推出必然捕虫战斗。
GIR-FD82-C003|仅B08具名遭遇/孵化/漫游目录的条件与返回子型；当前正常/取消/后置失败各条前提保留，非所有CE控制总签名。
GIR-FD82-C004|Land零率写出省略、成功compile恢复21；原默认零的OldRod对照仍0，注册/反写/再编译与当前快照分开。
GIR-FD82-C005|编辑登记、落盘、文本反写、编译及当前地图setup为不同状态层；无相应setup不自动替换正在使用的表。
GIR-FD82-C007|漫游专属邻接表与条件由当前WP37承接；这是C007所分配的漫游输入能力，不是战斗120效果或全域目录签名。
GIR-FD82-C079|等级修正实际能力身份和先物品后能力顺序保留，当前固定来源与WP36修正目录吻合。
GIR-FD82-C080|遭遇专用重复类型和数值边界已由WP36与WP04双向承接；不沿用通用重复拒绝来覆盖该解析器。
GIR-FD82-C081|WP36周期入口与M02普通计步2^31回绕一致；强制通知/距离计数不混同。
GIR-FD82-C082|普通陆地机会的表口径含BugContest；地形、时间型选择与主动钓鱼接口资格分开。
GIR-FD82-C083|队伍平衡等级的权重、均值/偏移和界限可由当前独立公式计算；不是只提供源辅助名。
GIR-FD82-C084|普通临时野生生成先发生，漫游持久生成/重用随后；两次路径的随机/通知副作用及终态标记不合并。
GIR-FD82-C085|漫游覆盖同时需要当前候选身份和临时下标存在，不能只凭某个全局旗标接管。
GIR-FD82-C096|写入相同遭遇版本提前返回，不重装表/清步数；异版本且上下文存在才setup，累加器保留。
''','B08只签其批准局部条款/案例；WP34等READ_ONLY/NOT_AFFECTED依赖资格原样保留。整体主审partial/unresolved只用于对应新范围，不自动转为旧PASS。',['M06','M01','M02','M07','M09'])
 add('B18','''
GIR-FD82-C003|T01必须暂持空且目标0空，抓放替换与已有U对照不同；T18完成后等待新BACK真，与未完成假分开。其他CE/其它小游戏消费者没有继承签名。
GIR-FD82-C127|正常库存槽可形成[A1,A1,B3]，对局副本依序合并为[A2,B3]，首抽A为1/2；保留满999槽时仍三槽且2/3，不能总按物种去重。
GIR-FD82-C128|openhand后手玩家5/对手4时查看导航有索引4空高亮；不能当不存在牌的提交。关闭openhand及5/5对照保留。
GIR-FD82-C129|默认4×4模式6五次四循环奇置换、模式7五次W交数奇偶不变量保证初始化非完成；不推广其它尺寸或玩家无法完成，也不执行枚举模型。
GIR-FD82-C130|暂持加红还需目标非空；模式4/5/6箭头受USE持续门，模式3与1/2/7分别对照；状态不写与显示请求分开。
GIR-FD82-C131|模式0的1×1完成检查先于输入，等待后新确认可真；2×1未完成新BACK假，表外模式不统一拒绝。源M11完成/包装比较支持。
''','B18有限手牌/拼图默认夹具；新同轮输入、普通图鉴网格、老虎机时间索引与资源参数不由这些既有单键/逻辑局面合同代签。导航/旧批准身份两控制交ROOT/C00当前对应记录。',['M11'])
 print('Manual scope assessments persisted; mappings remain independently gated.')
