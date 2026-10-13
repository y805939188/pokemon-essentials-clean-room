import json,pathlib,hashlib,subprocess,datetime
O=pathlib.Path(__file__).parent
B='9366d9d17aaeac3b4414236468affa650fb3dd27';R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
snapshot=(O/'candidate-initial.json').read_bytes(); original=json.loads(snapshot); initial_hash=hashlib.sha256(snapshot).hexdigest()
S={
'SW':'Data/Scripts/004_Game classes/001_Switches and Variables/002_Game_Switches.rb','SSW':'Data/Scripts/004_Game classes/001_Switches and Variables/004_Game_SelfSwitches.rb','I':'Data/Scripts/003_Game processing/003_Interpreter.rb','IC':'Data/Scripts/003_Game processing/004_Interpreter_Commands.rb','H':'Data/Scripts/003_Game processing/005_Event_Handlers.rb','SC':'Data/Scripts/003_Game processing/002_Scene_Map.rb',
'E':'Data/Scripts/004_Game classes/007_Game_Event.rb','C':'Data/Scripts/004_Game classes/006_Game_Character.rb','P':'Data/Scripts/004_Game classes/008_Game_Player.rb','M':'Data/Scripts/004_Game classes/004_Game_Map.rb','MF':'Data/Scripts/004_Game classes/005_Game_MapFactory.rb','CE':'Data/Scripts/004_Game classes/009_Game_CommonEvent.rb','F':'Data/Scripts/004_Game classes/010_Game_Follower.rb','FF':'Data/Scripts/004_Game classes/011_Game_FollowerFactory.rb',
'FI':'Data/Scripts/012_Overworld/005_Overworld_Fishing.rb','BERRY':'Data/Scripts/012_Overworld/006_Overworld_BerryPlants.rb','META':'Data/Scripts/012_Overworld/002_Overworld_Metadata.rb','FIELD':'Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb','TIME':'Data/Scripts/012_Overworld/003_Overworld_Time.rb','ITEM':'Data/Scripts/013_Items/002_Item_Effects.rb','IU':'Data/Scripts/013_Items/001_Item_Utilities.rb','UTIL':'Data/Scripts/019_Utilities/001_Utilities.rb','MSG':'Data/Scripts/007_Objects and windows/011_Messages.rb','SPR':'Data/Scripts/005_Sprites/008_Sprite_AnimationSprite.rb','SET':'Data/Scripts/001_Settings.rb','BD':'Data/Scripts/010_Data/002_PBS data/007_BerryPlant.rb','BPBS':'PBS/berry_plants.txt'}
F={
'EV':'engine-overworld/wp13-map-events-npc-followers.md','MR':'engine-overworld/wp13-move-route-matrix.md','IM':'engine-overworld/wp13-interpreter-command-matrix.md','MV':'engine-overworld/wp12-terrain-movement-vehicles.md','MAP':'engine-overworld/wp11-map-topology-transfer.md','WT':'engine-overworld/wp59-world-time-weather-field-moves.md','FS':'engine-overworld/wp60-fishing.md','BP':'pokemon-rules/wp60-berry-plants.md','T':'test-catalog/engine-overworld-wp11-15-59-60.md','BT':'test-catalog/pokemon-rules-wp53-60-61-62-69-70.md','TIME':'generic-kernel/wp06-time-random-steps-stats.md','STATS':'generic-kernel/wp06-stats-directory.md','UI':'user-interface/wp17-messages-windows-input.md','DX':'demo-dx/wp72-debug-contexts-and-controls.md','RENDER':'engine-overworld/wp16-world-rendering-and-visual-transitions.md'}
F={k:'deliverables/final-specification-set/'+v for k,v in F.items()}
F.update({'OEV':'specs/overworld/wp13-map-events-npc-followers.md','OMR':'specs/overworld/wp13-move-route-matrix.md','OIM':'specs/overworld/wp13-interpreter-command-matrix.md','OMV':'specs/overworld/wp12-terrain-movement-vehicles.md','OMAP':'specs/overworld/wp11-map-topology-transfer.md','OWT':'specs/overworld/wp59-world-time-weather-field-moves.md','OFS':'specs/overworld/wp60-fishing.md','OBP':'specs/pokemon-rules/wp60-berry-plants.md','OTIME':'specs/kernel/wp06-time-random-steps-stats.md','OUI':'specs/ui/wp17-messages-windows-input.md'})
logs=[json.loads(x) for x in (O/'direct-read-log.jsonl').read_text().splitlines()]
def refs(domain, specs):
 out=[]
 for key,ranges,why in specs:
  p=(S if domain=='R' else F)[key]
  found=[x for x in logs if x['root']==domain and x['path']==p]
  assert found,(domain,p)
  # Structural check only: cited ranges must be within one of the read requests.
  covered={i for x in found for a,z in x.get('ranges',[]) for i in range(a,min(z,x.get('line_count',z))+1)}
  for a,z in ranges:assert all(i in covered for i in range(a,z+1)),(key,a,z)
  out.append({'path':p,'version':R if domain=='R' else B,'sha256':found[0]['sha256'],'read_ranges':ranges,'supports':why,'reading_kind':'direct_text_read'})
 return out
records=[]
def add(n,src,spec,rebuttal,expected,accepted,excluded,adjust,normal,minimal,boundary,history,already=None,optional=None,unknowns=None):
 f=next(x for x in original['findings'] if x['id']==f'GR5-M03-{n:03}')
 records.append({'id':f['id'],'original_candidate':f,'original_candidate_canonical_sha256':hashlib.sha256(json.dumps(f,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest(),'original_candidate_snapshot_sha256':initial_hash,
 'source_directly_read':refs('R',src),'spec_directly_read':refs('B5',spec),
 'independent_challenge':rebuttal,'rebuttal':rebuttal,'recommended_disposition':'required','recommended_severity':'P2','disposition':'required','severity':'P2',
 'corrected_expected_behavior':expected,'accepted_claims':accepted,'excluded_claims':excluded,
 'no_required_revision_claims':already or [],'optional_claims':optional or [],'unresolved_claims':[],
 'acceptance_adjustments':adjust,'normal_case_review':normal,'minimal_counterexample_review':minimal,'failure_or_boundary_review':boundary,
 'history_relation':history,'unknowns':unknowns or ['真实地图/事件/公共事件数据与媒体未提供；不宣称默认Demo可达或实际运行复现。','无参考、行为模型或宿主执行；只静态解释固定R，未来是否保留异常另属政策。'],
 'confidence':'high_static_with_stated_preconditions','execution_status':{'reference':'NOT_EXECUTED','model':'NOT_EXECUTED','host_or_demo':'NOT_EXECUTED','structural_checks':'JSON/text/hash/range processing only'},'review_status':'completed_independent_counterevidence_bounded_integration','final_global_adjudication':'parent_only'})
add(1,
 [('E',[[197,258]],'刷新选择/相同页早退/两项原值门'),('C',[[521,535],[815,826]],'路线41直接写入与普通转向守卫分离'),('M',[[429,437]],'地图刷新调用者')],
 [('EV',[[24,31],[98,106]],'页描述及现有同页/页变承接'),('MR',[[5,19],[62,68]],'路线41及方向固定合同'),('T',[[123,124],[225,241],[467,467]],'EV/MR/CS09'),('OEV',[[48,53]],'原稿同一概述'),('OMR',[[8,18],[61,67]],'原稿路线表'),('RENDER',[[116,124]],'显示只消费方向/图案')],
 '尝试用页决定外观、方向固定开关及GR3-CS09同页保留启动规则消解。均不能推出“参数与保存原值相同则不改当前值”；方向固定只挡普通转向，两个直接写入点不查它。相同页早退已有局部承接，不应单独再立必修。',
 '选中同一页时刷新提前返回；选中另一有效页或处理路线41时，方向与图案各自比较保存的原始值。相同则保留当前值；不同时才把当前和原始对应值一同改为新值。方向这一步还清预锁方向；该直接赋值不受普通方向固定守卫拦截。',
 ['方向和图案两个独立条件覆盖门缺失，影响后继朝向及表现。','路线41与有效页切换均须明确该条件。'],
 ['不把“同一页”扩大成任意内容相同但不同页。','不把观察点延长为后续动画更新永远保持当前图案。'],
 ['只补条件写入及成对向量；同页早退可引用/明确既有规则，不重复计新缺陷。','向量固定原方向下、当前右，参数下/上成对；图案另独立成对；观察点在调用返回且无后续动画写入。'],
 '新参数上不同于原始下时，当前/原始均变上，清预锁方向；方向固定真仍不否定这一直接写入。',
 '原始下、当前右；路线41方向下则仍右。另一有效新页方向仍下也保留右。反证有效。',
 '无满足页走单独清图/列表分支，不套用有效页赋值；同一已选页早退。',
 '与B5 GR3-CS09页刷新范围相邻；该例已承接同页不清启动，未交付方向/图案门。不改旧接受身份。',
 ['同页不重新套页的既有局部事实；方向固定作为普通转向守卫。'])
add(2,
 [('I',[[45,78],[84,135],[183,205],[323,383]],'绑定身份、失联清ID、当前图角色解析及绑定私有键'),('IC',[[128,135],[413,417],[632,642],[752,779],[833,842],[856,865]],'解锁、自开关、202和跟随路线覆盖'),('E',[[274,291]],'邻图并行解释器建立/更新'),('SC',[[121,151]],'各驻留图更新'),('FF',[[38,45],[274,286]],'跟随互动锁定/启动'),('F',[[7,31]],'跟随ID及实例地图来源'),('MF',[[221,224]],'连接判定'),('C',[[165,185]],'锁/解锁效果')],
 [('EV',[[55,60],[68,90],[98,106],[133,148]],'已知当前图消去及绑定自开关例外、未给通用投影'),('IM',[[31,43],[57,65]],'各命令消费者与跟随覆盖'),('MAP',[[88,93],[119,136]],'邻图实例/恢复异图同ID，非解释器目标解析'),('T',[[135,143],[152,161],[459,471],[482,490]],'已有向量入口限定'),('OEV',[[72,94],[118,133]],'原稿解释器及跟随'),('OMAP',[[98,104]],'原稿邻图')],
 '最强既有承接是WP13§4.3绑定地图写A、§3.3当前图消去以及WP11异图through恢复。它们已说明若干不同身份，但没有为202/111/123/结束解锁提供统一可推得的目标规则；不能用“邻图事件按各自实例更新”推成角色查询也在绑定图。跟随路线覆盖确实是反例，故排除“所有角色命令一律当前图”的过宽说法。',
 '解释器保留绑定图和事件编号；相连异图不会清编号。通常角色选择-1为玩家，0为当前图该编号事件，指定编号也查当前图。私有变量和缺省脚本自开关用绑定图；111自开关子型、123及有效主解释器结束解锁用当前图。跟随互动锁跟随实例，但不自动把普通本事件查询重定向到它；207/209显式跟随覆盖另列。',
 ['相连A/B同ID映射在当前文本中缺少足够消费者约定。','跟随互动的锁对象与普通目标/结束解锁对象不必相同。'],
 ['不宣称所有事件上下文都查当前图。','不排除207/209具名跟随覆盖。','不宣称跟随实例永久不能移动或默认软锁。'],
 ['最小例固定两图均驻留且连接判定真、B稳定为当前图、A/7并行有更新机会、无等待门/转移/额外改写，B宽高>8。','补绑定私有键/当前角色键对照，并明确主解释器结束及跟随覆盖例外；不要求全局改造事件身份架构。'],
 '绑定图等于当前图时通常角色与私有键一致；显式跟随覆盖可选择跟随实例。',
 'A/7的202本事件落位(8,8)实际改B/7；同解释器私有值写A/7。直接调用链支持反证。',
 'B缺7则202跳过；失联先把解释器编号清0。跟随结束只请求当前图同编号事件解锁，不自动解锁跟随实例。',
 '扩展现有GR3过场绑定自开关/记录恢复的相邻身份事实，非重开其范围；只新增普通解释器目标投影。',
 ['过场跳过缺省脚本自开关绑定图已在§4.3明确。','消去/恢复当前图键与失联只清ID已承接。'])
add(3,
 [('E',[[56,127],[283,290]],'私有记录、日秒门、临时A及失败刷新消费'),('I',[[323,330],[350,383]],'登记与刷新顺序'),('TIME',[[1,6]],'宿主墙钟来源'),('SSW',[[7,23]],'持久自开关读严格true，与临时表独立')],
 [('EV',[[28,31],[98,102]],'冷却和写持久A刷新概述'),('WT',[[24,27],[85,98]],'时间消费者'),('TIME',[[52,72]],'游戏变量计时明确不同入口'),('T',[[322,369]],'WT无私有冷却算式'),('OEV',[[48,53]],'原稿冷却'),('OWT',[[44,51],[106,122]],'原稿秒默认值已有但无完整算法')],
 'WP06§3.4虽已有严格秒截止及天数数学，却是会清游戏变量的另一能力，文本明确与事件私有冷却不同，不能借来闭合。WP13已承接冷却失败刷新和临时A，原稿WP59亦已有秒默认86400；不应把这些都声称全无。剩余缺口仍是私有秒/日算法、空记录差异与批量登记顺序。',
 '整数记录t、当前取整墙钟n：秒式默认86400，只有记录存在且n>t+s才真。日式默认1，空记录按0；令Δ=n−t，q=⌊Δ/86400⌋，r为对应0…86399余数，h为当前本地日内秒；计数=q加上“r>h”时的1，再以计数≥请求天数判定。冷却查询还要求临时A关闭，否则只请求该事件刷新并返回假。登记仅取一次当前整数墙钟，按自身再各给定事件，先置绑定图的持久A，再写对应私有时间；A值变化且地图已加载才请求地图刷新。',
 ['严格大于秒边界、日式固定86400秒/本地日内修正、空记录不对称必须可测。','一次时钟样本与持久A/私有时间的按事件登记合同缺失。'],
 ['不把日式改写为任意时区/DST下严格自然日数。','不移植WP06游戏变量查询失败清0的副作用。','不把过期查询默认参数误写成冷却包装也可省略参数。'],
 ['提供1010/1011秒式对照；日式以明确本地分量和Unix差值列向量，保留余数比较严格大于。','区分持久A与临时A；登记写入顺序和正常刷新条件可交叉引用现有合同。'],
 '稳定时区下昨天23:59到今天00:00，Δ=60、日内秒0，日式1日通过，秒式86400不通过。',
 't=1000,s=10,n=1010：冷却假且刷新请求；n=1011且临时A假：真。有效。',
 '无记录秒式为空/不成立，冷却包装仍返回假并请求刷新；日式以0计算。时间倒退照算式，不补归零策略。',
 '与第四轮WP06游戏变量墙钟计时相邻但不同入口；其限定回执不覆盖事件私有冷却。',
 ['临时A门、失败请求刷新、临时开关重建丢失已承接。','宿主时间来源与秒默认86400已有局部承接。'])
add(4,
 [('C',[[145,158],[362,374],[427,552],[893,933],[994,997]],'安装同步处理/覆盖保存/自主延迟/遍历边界'),('IC',[[856,873]],'209调用与210等待'),('E',[[197,258]],'有效新页和空页分开'),('P',[[431,458]],'玩家自主输入不采用NPC频率算法')],
 [('MR',[[5,21],[54,57]],'剩余命令说法与原路线恢复'),('IM',[[64,65]],'立即继续只是不等完成'),('EV',[[28,31],[73,82],[126,129]],'页与调度'),('MV',[[144,148]],'自主策略频率门未量化'),('T',[[102,103],[135,135],[225,241]],'已知等待/结束/空路线'),('OEV',[[48,53],[72,86]],'原稿'),('OMR',[[8,20],[55,56]],'原稿同缺口'),('OMV',[[163,167]],'原稿频率引用')],
 '“设置后立即继续”及MR07只保证事件不等待路线完成、单次处理可连跑，不能判定209返回前是否已跑路线首项。MR05已有结束恢复，也不能推出覆盖进行中路线保留哪一层。候选“新页会清强制状态”过宽：只有选中不同且非空的有效页才走该写入，变无满足页提前返回。',
 '安装强制路线清旧等待并立刻尝试路线处理；运动/跳跃中提前返回，静止且列表非空时可在209返回前提交首项。首次接管前原路线存在且已保存时，覆盖另一强制路线不替换该保存值。选中不同有效页重置路线/索引/强制标记并更换并行解释器；同页早退及无满足页另列。普通NPC自主频率1…6停止延迟为4.75、3.6、2.55、1.6、0.75、0秒，强制路线不受此门。单次处理的迭代上限为列表总长减1，仍受运动项/等待项/终止等提前退出。',
 ['同步安装效应与自主频率定量门未交付。','重复路线跨尾回绕的总长减1上限与正文“剩余”不一致。','覆盖保存和有效新页接管边界应明确。'],
 ['不称所有页变化或消去都清forcing。','不将NPC频率延迟套给玩家输入。','不将同步尝试表述为路线总在安装时完成。'],
 ['保留仅终止项空路线的既有悬置行为。','有效新页/同页/无页分别设前提，覆盖例明确已保存原路线非空。','频率向量指本次调度前停止计数0.74/0.75，实际更新需非菜单且增量≤0.25；不保证固定帧。'],
 '正在运动时安装先改路线标记，首次动作待后续静止机会；非空原路线R0被R1再R2覆盖，R2正常终止恢复R0。',
 '静止角色，209装[开关S ON,终止]，返回前S已真；紧后111读真。首项虽已运行，终止可能留待下一机会。',
 '重复路线从靠末尾索引开始仍可绕回处理总长减1次；不同有效页中断forcing，无页分支没有该清写。',
 '不重审GR4范围随机字面让出、MR空路线/WAIT既有结论；本项补安装和自主调度。',
 ['209不置等待、210等待、结束恢复和空路线不恢复已有充分合同。'])
add(5,
 [('C',[[260,303],[397,400],[451,469],[553,638],[981,991]],'对角许可与直接提交、保留一般步通知'),('P',[[130,193],[238,251],[543,554]],'距离只在四向/跳跃覆写，后续步事件另行'),('IC',[[856,865]],'玩家强制路线入口')],
 [('MV',[[94,111],[144,148],[223,225]],'普通步统计与固定L许可不能补对角副作用'),('MR',[[11,15],[28,35]],'对角与索引'),('TIME',[[76,87]],'距离概述与全局计步分离'),('T',[[58,64],[97,103],[225,233]],'已有运动/对角/碰撞向量'),('OMV',[[115,130],[163,167]],'原稿同缺口'),('OMR',[[27,34]],'原稿'),('OTIME',[[75,84]],'原稿距离概述')],
 '固定L分解只规定许可，不等于实际执行两次普通移动；WP12已分离一般计步与全局步数。直接追玩家覆写确认没有对角距离累计，但一般离格和步完成链仍存在。因此接受入口差异，排除“对角不产生任何移动副作用/通知”的扩张。',
 '四对角入口按各自规则在通行前直接调整朝向（方向固定则不改），按固定两段/多格许可后一次提交两轴坐标和运动计时，并重置停止计时、条件性通知离格。它们不调用玩家四向入口的距离累计、岩架/上岸/碰撞处理或转向通知；运动完成仍经过一般步完成和玩家步后链，按其各自守卫处理。',
 ['玩家对角位移不增加行走/骑行/冲浪距离，现有“按实际距离”摘要需限定入口。','失败对角不触发四向碰撞计数/接触尝试；可能已调整方向。'],
 ['不删除一般离格与步完成通知。','不从距离未增推出全局步计数一定不变；该计数由路线/解释器守卫决定。'],
 ['主反例明确步行、surf/dive/bicycle/ice_sliding皆假；观察逻辑提交后，无其它统计写入。','另列失败、方向固定和普通四向/非零跳跃对照。'],
 '普通向右成功距离+1；非零直接跳跃坐标变化时按两轴绝对位移和累计。',
 '玩家(5,5)路线6成功至(6,6)，distance_walked仍N。把对角实现成两次普通步会得N+2；有效。',
 '任一固定分段不许则无位移/碰撞计数；例如原朝左请求右下可先变右。一般后续通知不得混同四向入口副作用。',
 '与既有GR-011普通移动遭遇门、WP06计步分层相邻，新增对角入口范围，不撤销原四向/直接跳跃合同。',
 ['固定L许可顺序、多格前缘及一般计步/全局计步分离已承接。'])
add(6,
 [('C',[[348,354],[397,400],[451,469],[767,813],[948,985]],'零偏移直接跳/包装零距离/完成通知'),('P',[[188,193]],'坐标未变不加距离')],
 [('MV',[[98,109]],'无条件占格门误述'),('MR',[[11,13],[41,41]],'跳跃门及状态推进'),('T',[[63,64],[225,229]],'非零失败和运动状态门'),('OMV',[[120,130]],'原稿'),('OMR',[[12,17],[40,40]],'原稿')],
 'MR的“按运动状态推进”已足够解释一旦原地跳进入jumping为何推进，不能另立索引缺口。问题在WP12/路线14无条件要求占格许可；源的转向和落点许可都只针对非零偏移。候选“峰值按最小1”须说明1是距离下限，不是峰高1。',
 '直接跳跃偏移(0,0)跳过转向与占格许可，仍开始原地跳跃并调用一般计步；名义时间距离取1、跳峰按该距离乘每格高度的3/8，坐标不变故玩家距离不增。前跳/后跳包装距离0则直接false、不创建跳跃。',
 ['零偏移是现有无条件跳跃许可描述的可观察反例。'],
 ['不声称原地跳峰等于1像素。','不要求原地跳必增全局步数或产生离格通知。'],
 ['阻挡格原地跳与非零阻挡跳成对；前/后包装0独立对照。','索引推进引用现有运动状态规则；不新改该规则。'],
 '非零目标阻挡时拒绝，无成功跳跃提交；现有MV24在许可实际被检查的前提下保留。',
 '静止普通事件位于全向阻挡格，路线14(0,0)仍jumping=true；不可跳过路线也推进。有效。',
 '逻辑坐标不变、一般计步只重置停止/条件性离格；跳跃完成才通知一般步，前后包装0不进入这些过程。',
 '零偏移是WP12既有直接跳跃合同的新边界；无需撤销GR-011或MR按状态推进规则。',
 ['不可跳过路线在jumping为真时推进已有充分承接。'])
add(7,
 [('I',[[138,145],[304,320]],'事件脚本接收上下文及局部公共事件助手返回'),('IC',[[1168,1179]],'脚本执行调用链'),('FI',[[1,70]],'开始/结束无显式接收者调用'),('UTIL',[[524,539]],'全局助手负ID门和true返回'),('ITEM',[[276,316]],'三竿闭包注册'),('IU',[[4,14],[74,81],[755,762]],'物品消费者'),('H',[[148,168],[192,197],[294,295]],'直接调用闭包、不切换为解释器上下文'),('SET',[[78,86]],'默认公共事件-1')],
 [('FS',[[21,30],[67,80],[104,144]],'一般替代与直接调用描述'),('EV',[[68,90]],'公共事件运行概述'),('T',[[371,392]],'FS14/16及正常入口'),('OFS',[[43,52],[89,102],[125,149],[193,195]],'原稿同样统一处理')],
 '首先核三竿处理器是否仍可能以解释器为接收上下文：注册闭包被直接调用，保留定义上下文，故正常物品路径使用全局公共事件助手。解释器脚本直接无显式接收者调用钓鱼则不同，其内部同名调用落到解释器助手。B21-CASE-DISPATCH只处理OldRod主动遭遇与步进表，不覆盖公共事件助手；不能据其既有接受消解。',
 '在非战斗解释器脚本上下文直接请求钓鱼时，存在的开始/结束公共事件正常执行完后，本地助手返回空值，钓鱼因此继续对应内置表现；正常物品回调的全局助手成功返回真，跳过该内置段。开始先置钓鱼标志；结束在正常表现/随附消息后仍作共同清理。解释器助手没有全局助手的负ID拒绝门，负ID按实际数组索引；无记录则空返回并用内置。',
 ['调用上下文改变同名助手返回值及内置段是否执行，需限定现有统一替代条款。','开始和结束均需按入口分列，不能只修开始。'],
 ['不称所有从事件触发的物品调用都使用解释器助手；关键是直接无显式接收者调用链。','不宣称默认-1一定存在末项公共事件。','不将正常清理扩大到中途异常/场景中断。'],
 ['使用正ID合法立即结束公共事件、非战斗、正常资源/时钟/更新、无插件/状态改写作最小成对例。','为FS14/16加普通物品路径前提，并新增解释器直接调用对照。','负ID只写条件性索引规则，缺公共事件数组内容时不虚构默认演示结果。'],
 '三竿正常物品路径，正ID事件存在并完成：只跑公共事件，不跑对应内置段；正常结束共同清理保持。',
 '解释器直接开始：fishing先真→有效公共事件完成→仍设钓鱼类型/锁图案并请求3,2,1,0序列。与物品入口相反；有效。',
 '公共事件缺失回退；负ID在解释器助手中可能取得倒数记录，取决于数组，不能一律判无效。异常未承诺清理。',
 'B21-CASE-DISPATCH已直接读取，内容不是该分派差异。FS14/16历史正常物品合同保留；本项为直接脚本入口增补。',
 ['直接入口不重查鱼竿资格已承接。','全局助手正常返回true的物品替代及正常结束清理已承接。'])
add(8,
 [('I',[[183,205],[385,417]],'推动调用、严格预检、计数/移动/记录/等待顺序'),('C',[[237,303],[553,581],[165,185]],'严格双端前缘与普通移动再检查/锁'),('M',[[249,268]],'全向通行位门'),('META',[[144,163]],'力量状态初值及条件记录')],
 [('WT',[[181,230]],'力量激活/直接工具而无推石消费者合同'),('MV',[[70,90],[94,109]],'普通/严格能力，无法推得调用选择'),('EV',[[55,60]],'移动快照已定义'),('MAP',[[119,132]],'快照条件/恢复'),('STATS',[[20,33]],'计数摘要'),('T',[[51,57],[338,353],[491,491]],'方向位及力量标记/快照既有例'),('OWT',[[218,241]],'原稿激活层'),('OMV',[[93,120]],'原稿严格通行')],
 '严格通行和快照结构并非完全未提取；已在WP12及WP13/WP11承接。缺的是实际推动消费者选择严格预检以及统计/移动/记录/锁等待顺序。进一步反证候选正常路径：双端全向通行不必使普通移动通过（例如普通NPC冰面限制），因此不得把strict通过写成必定推动成功。',
 '力量巨石包装仅力量状态真才请求推动，正常返回true并不表示发生位移。有效当前事件的推动入口先做严格双端/前缘/碰撞预检；通过后计数+1，再按玩家方向尝试普通一步，之后在记录对象和有效事件条件下登记当前快照。只有逻辑位置确变才按可选参数请求音效、锁玩家、等待事件运动结束并解锁；自身through仍只在有效目标边界之后可提前放行。',
 ['从力量激活到推石的消费者合同缺失。','计数在尝试位移之前，记录在尝试之后，位移条件才控制音效/等待。'],
 ['不把严格预检通过当普通位移一定成功。','不将默认无推声参数解释为不记strength_push_count。','不把记录对象缺失说成仍必写快照。','不推默认Demo巨石实际配置。'],
 ['最小反例固定普通非冰/非水/非岩架地形、有效边界及无其它碰撞；仅目标非进入方向通行位被禁。','正常成功例还需普通移动许可；增加strict通过但普通移动拒绝时计数/记录和等待的分离说明，可复用现有普通通行合同。','准确引用已交付严格能力及记录结构，不复制整套规则。'],
 '普通地面双端所有门通过：计数+1→一步逻辑位移→快照→可选音效→玩家锁定/正常等待/解锁。',
 '右推目标左入边允许、另一方向被禁；普通右移可通过，strict预检拒绝，位置/计数/快照保持。有效。',
 '力量假：包装true但不推动；记录对象空：跳记录；strict通过而普通移动未变：计数已增，可记未变快照，不锁玩家等待。',
 '既有WP12 strict与GR3-MR13快照为充分子合同；本项只接消费者和时序，不重新认领这两项。',
 ['全向严格通行概念、移动记录字段及有效整数ID/事件门已有充分承接。'])
add(9,
 [('IC',[[752,779]],'202全部位置模式/缺对象/转向'),('I',[[183,205]],'角色选择'),('C',[[376,395],[815,826]],'落位取模/离格/方向固定'),('P',[[262,275]],'玩家落位有额外既有副作用')],
 [('IM',[[56,65]],'202仅事件/坐标概括'),('EV',[[112,122]],'命令兼容层说明不足以决定参数效果'),('MAP',[[71,72],[125,132]],'通用落位及恢复转向不是202交换语义'),('T',[[179,219]],'无202三模式向量'),('OIM',[[56,65]],'原稿同样概述'),('OEV',[[96,107]],'原稿兼容界限')],
 'WP11已有落位取模与转向顺序，但它的主体是传送/记录恢复；从这些不能推出202有坐标变量模式和双对象交换。命令矩阵“不保证所有参数语义”是范围说明，不会使已经列为可用的202能由实现者唯一解释。',
 '非战斗且主角色存在时，202支持直接坐标、变量值坐标及交换两角色坐标；交换先保存主坐标、先落主再落副，后只向主角色请求有效2/4/6/8方向，方向固定仍阻止转向。缺副对象只省交换，后续主转向仍可发生；缺主或战斗态整体继续而无此次效果。各目标落位副作用按对象所属入口，非碰撞移动。',
 ['三种输入模式与主/副缺失、转向后处理属于缺失的可观察兼容语义。'],
 ['不规定未来必须保存源参数槽/类组织。','不把玩家目标简化为只有普通事件的落位副作用。'],
 ['交换例限定两个不同普通有效事件、同图宽高足够、方向固定假、无离格处理器额外写入。','变量模式与直接模式、缺副但仍转向、缺主/战斗跳过及固定方向对照须可推出。','对象身份复用002规则，不重复立同ID投影缺陷。'],
 '直接/变量得到相同坐标输入时，按各对象落位规则并在后处理主方向。',
 '7=(5,5)、8=(9,9)，交换后向左：7=(9,9,左)，8=(5,5,原方向)。有效。',
 '副8不存在则7不位移但可向左；主7不存在或战斗中整体无效继续；非法/未指定朝向不请求转身。',
 '新提取202参数/目标分支；不改WP11已有落位合同，不与002目标身份重复计数。',
 ['通用落位坐标取模与条件性离格通知已有承接。'])
add(10,
 [('E',[[78,86],[197,213]],'页s:原结果按真值'),('CE',[[30,55]],'公共并行s:求值门/刷新'),('I',[[54,78]],'公共自动运行只看原始槽'),('IC',[[392,453]],'111开关严格相等与脚本原值/Else门'),('M',[[429,437]],'刷新传播'),('SW',[[7,24]],'原始槽读取不求值名称')],
 [('EV',[[26,31],[41,46],[80,90],[119,122]],'s:支持、公共事件概述'),('IM',[[31,32]],'类型列/脚本nil但未写开关归比较结果'),('T',[[140,143],[194,196]],'脚本nil/false既有向量'),('DX',[[62,66]],'调试表达式不提供这些事件消费规则'),('OEV',[[48,53],[68,94],[107,116]],'原稿'),('OIM',[[31,32]],'原稿同一描述')],
 '111/411已有nil与false细分，但111的开关子型先形成严格比较后的布尔值，不能把“脚本原值保留”直接套给s:开关。调试开关页也有独立求值规则，不是公共自动运行的消费者。用纯常数s:1排除接收上下文差异后，候选四入口反例成立。',
 '页条件和公共并行对s:表达式按真值使用；111开关子型把表达式结果与目标布尔值严格比较，所以非布尔真值1对ON/OFF都不满足，条件结果false会走Else。111脚本子型保留原值：1进Then、nil两支都跳。公共自动运行直接读取普通槽，不对名称脚本求值。',
 ['同一脚本开关在四类消费端判据不同，现有“支持s:”不足以交付此差异。'],
 ['不把公共并行解释为每次update无条件重新求表达式；启停在refresh。','不把111开关表达式nil直接保存在分支表。','不移入调试资格过滤/异常救援规则。'],
 ['固定s:1且原始槽OFF：刷新页/公共并行、111 ON/OFF比较、公共自动运行选择机会分别观察。','s:nil的开关ON/OFF结果都false且走Else；与脚本nil两支都跳成对。','补true/false正常二值对照，保留IM16–18。'],
 '表达式true且普通槽ON时，各ON判据可一致；111目标OFF仍按其比较。',
 's:1、槽OFF：页/并行启用，111开关ON和OFF各false，脚本1进Then，公共自动运行不启动。有效。',
 'nil表达式并非严格false：111开关OFF仍比较不成立（最终false，Else可进入）；普通脚本nil则Then/Else均跳。',
 '扩展B03/IM16–18已接受脚本原值范围到开关子型和公共事件消费者，非推翻旧nil合同。',
 ['111脚本nil/false和Else严格false已充分承接。','s:兼容字面及调试专用资格已有各自合同。'])
add(11,
 [('BERRY',[[21,50],[83,160],[221,303],[308,321],[437,471]],'数量预取、生命周期、显示订阅、采摘/外层reset'),('MSG',[[18,20],[633,650],[687,754]],'非淡出地图微更新门、输入出口先于微更新'),('SC',[[121,163]],'迷你更新仍更新精灵'),('SPR',[[300,331]],'用户精灵更新'),('SET',[[16,17],[75,77]],'默认新机制'),('BD',[[20,33]],'4+4周期/9次重植/数据'),('BPBS',[[3,6]],'正确内容ID和3h参数')],
 [('BP',[[13,17],[36,82],[100,132],[143,168]],'每帧/重植规则已给而取消后保持成熟过宽'),('BT',[[47,70]],'BP13/14及重植/图形向量'),('UI',[[233,251]],'微更新门和顺序已有充分承接'),('EV',[[68,90]],'解释器等待非暂停全部世界'),('OBP',[[92,113],[149,185],[235,248]],'原稿同样存在过宽终态'),('OUI',[[235,246]],'原稿微更新')],
 '最强反证是WP60§5已有加载每帧追赶、WP17§7.2已有非淡出地图微更新及输入后顺序；两者联合确可推出等待中可能更新。因此不是缺一套新时间机制。但§6.4及§9明确承诺拒摘/满包保持成熟/惩罚保持，与这些规则组合冲突，仍需有界修订。候选最小例还必须明确无覆盖物、正确ID CHERIBERRY，且至少一轮无出口输入的正常微更新先于拒摘。',
 '新机制已加载植物在可用的地图微更新中按墙钟继续结算，采摘提示前已锁定该次树果身份和数量。拒摘或容量失败不主动reset、不撤销等待中重植/清零/干涸；不能承诺最终仍成熟。正常确认并加入仍使用提示前数量，所有成功尾部正常返回后外层reset当前持有的该植物状态。',
 ['取消/满包“保持成熟及惩罚”的无条件终态应改为无采摘重置，保留独立时间推进。','提示前数量取样与成功后外层reset之间的时序应能验证。'],
 ['不新增“消息等待冻结植物”的未来政策。','不说每次越秒后的确认/取消轮都先更新植物；实际出口检查先行。','不把24h周期套给带覆盖物或后续生命周期。','不把CHERI当作固定数据ID。'],
 ['反例设同图有效berryplant事件、主解释器和私有植物一致、场景为地图且未淡出、用户精灵未销毁、新机制、CHERIBERRY、无覆盖物、首周期、replant_count=0。','初time_alive=86399/阶段8、last=T；确认窗口至少一轮不退出，在T+1微更新后再拒摘，保证没有其它状态写入。','增加同秒快速拒摘、已跨周期拒摘/满包、跨周期确认仍用旧数量三类观察点；只需引用既有更新数学。'],
 '未发生普通时间推进的快速拒摘：不加物品、不增采摘统计、不reset，原成熟状态可保留。',
 '3h×(4+4)=86400秒；86399+1触及首周期，重植一次、剩余0、阶段2。先完成该次微更新再拒摘，最终阶段2。有效但原前提须补齐。',
 '按键出口本轮先于地图微更新；满包后的消息还可继续推进时间。确认成功沿旧数量提交，正常尾部之后才reset；非地图/淡出/旧机制不套本例。',
 '新增跨WP17微更新与WP60采摘的组合限定；GR-012取整、BP18公共写入、BP20闪光及旧机制不更新均保持。',
 ['新机制每帧结算、生命周期算式、微更新资格与按键出口顺序已有充分承接；不要求重写。','工具true后才外层reset及失败不由采摘主动清植物已承接。'])
add(12,
 [('I',[[84,145],[292,301],[419,424]],'辅助自身推进与外层推进'),('IC',[[11,35],[128,135],[502,509],[1168,1179]],'脚本预合并/true与116 false'),('FIELD',[[213,227]],'碎除正常返回前的等待/消去'),('E',[[46,49],[197,258]],'消去刷新'),('META',[[154,157]],'消去记录')],
 [('EV',[[48,64],[68,89],[119,122]],'三入口表尚未写辅助自增'),('IM',[[10,17],[37,38],[118,118]],'355和116不同外层行为'),('T',[[138,139],[189,189],[490,491],[526,540]],'GR3-MR12/GR4-ER06只有存在门而无自增事实'),('MAP',[[119,136]],'恢复范围不覆盖辅助推进'),('OEV',[[72,107]],'原稿外层推进'),('OIM',[[10,17],[118,118]],'原稿355')],
 '强力消解尝试是B5§3.3“调用推进沿既有入口规则”及GR4-ER06“不得套116让出”。然而现有规则只给355合并后true/外层+1，没有给这两个脚本辅助自身+1；不能从“不是116”推出跳过下一命令。GR3/GR4旧例也只测消去/记录存在门，故未充分承接。',
 '记录式消去或碎除辅助在正常返回路径各额外推进解释器索引1，缺当前事件也如此，随后返回true。独立355（无后续355/655合并）调用一次辅助后，355正常true使外层再推进1，紧邻非脚本后命令被跳过。相邻脚本先整体合并，须从合并后的索引计算；116自身+1后false只让出，不发生这次外层再增。',
 ['辅助额外推进与355组合的可观察跳过缺失。','两个辅助缺当前事件仍推进，应与实例/记录存在门分开。'],
 ['不说任意包含该辅助的脚本都恰跳物理下一行；多次调用/合并/额外索引写入另有结果。','不把辅助结果true当成116一样停止解释器更新。','不撤销旧消去与记录恢复结论。'],
 ['固定主解释器、同图有效ID、355独立一调用→121 S ON→终止，S初OFF，无等待/其它启动项/输入跳过/额外写入且所有操作正常返回。','分别列缺事件、碎除正常返回及116成对例；碎除等待期间无额外改变本解释器的输入/状态。','不要求保留源内部索引结构，只要求相同命令序列的可观察跳过结果。'],
 '116→121→终止：第一次更新让出，后续合格机会执行121；原GR4-ER合同保持。',
 '355单次记录式消去→121→0：辅助额外推进再加外层推进，直接到终止，S保持OFF。有效。',
 '缺当前实例不消去/登记但仍跳邻条；相邻355/655先合并执行。中途异常不承诺完成推进或清理。',
 'new_scope_same_root：GR3-M03-004的实例/记录与GR4-M03-003的116生产端均保留；本项新增355组合，不重签旧CLOSED。',
 ['116自身推进并false让出、辅助存在门、355合并及普通false不等待已有充分承接。'])

# Additional direct supplemental anchors, explicitly selected fields rather than whole-file claims.
def supplemental(p,pointer=None,fields=None,rows=None,root='B5',why=''):
 xs=[x for x in logs if x['path']==p and x['root']==root]
 assert xs,p
 return {'path':p,'version':B if root=='B5' else root,'sha256':xs[0]['sha256'],'pointer':pointer,'rows':rows,'fields':fields,'supports':why,'reading_kind':'direct_selected_semantic_fields'}
jp='review/remediation/20261003-prepare/wp78-junction-successor.tsv';fs=['junction_id','theme','current_interface','ordered_failure_and_neighboring_contrast']
for i in [2,3,4,5,6,7,8,9,10,11,12]:
 rows={2:[51],3:[7,8,12],4:[9,12],5:[9],6:[9],7:[7,12,41,51],8:[54],9:[51],10:[49,51],11:[7,8,12,40,41],12:[51]}[i]
 records[i-1]['spec_directly_read'].append(supplemental(jp,fields=fs,rows=rows,why='共享交界仅提供来源/消费者/既有范围；不补本候选缺失的具体分支。'))
sp='review/remediation/20261003-prepare/batches/B21/author-draft-1/static-cases.json'
records[6]['spec_directly_read'].append(supplemental(sp,'/cases/6',root='e58486178e746273fb6fab55df00722807f1dc44',why='B21-CASE-DISPATCH实际仅OldRod主动请求与步进表，非同名公共事件助手。'))
ep='review/remediation/20261003-prepare/batches/B21/author-draft-1/eight-chains.json'
for i in [4,5,6,11]:records[i-1]['spec_directly_read'].append(supplemental(ep,'/chains/'+str(5 if i==4 else 1),fields=['id','title','current_accepted_sequence_and_conditions','neighboring_contrast_and_partial_failure'],root='e58486178e746273fb6fab55df00722807f1dc44',why='保留路线字面/一般步/树果统计既有合同；不补本项。'))
records[10]['spec_directly_read'].append(supplemental('review/wp78-consistency-review-2026-10-03/revision-v3/anomaly-register.json','/facts/19',fields=['id','fact','junction','evidence'],why='AX20仅水分/干小时惩罚，不规定采摘等待期间冻结。'))

# Final candidate comparison, structural only; do not silently substitute later candidates.
current=(O.parent/'M03/findings.json').read_bytes(); cur=json.loads(current); oldby={x['id']:x for x in original['findings']}; newby={x['id']:x for x in cur['findings']}
changes=[]
for fid in sorted(set(oldby)|set(newby)):
 if oldby.get(fid)!=newby.get(fid):
  changes.append({'id':fid,'changed_fields':[k for k in set(oldby.get(fid,{}))|set(newby.get(fid,{})) if oldby.get(fid,{}).get(k)!=newby.get(fid,{}).get(k)],'before':oldby.get(fid),'after':newby.get(fid)})
assert not [x for x in changes if x['id'] in {r['id'] for r in records}], 'Scoped candidate changed: read delta before completion'
change_info={'initial_sha256':initial_hash,'final_sha256':hashlib.sha256(current).hexdigest(),'changed':bool(changes),'changes':changes,'out_of_scope':[x for x in newby if x not in {r['id'] for r in records}],'policy':'Only GR5-M03-001…012 assigned. New IDs referred to parent, not reviewed.'}
(O/'candidate-change-check.json').write_text(json.dumps(change_info,ensure_ascii=False,indent=2)+'\n')
res={'schema_version':'gr5.c03.independent-counterevidence.v1','reviewer':'C03 independent counterevidence reviewer, distinct from M03 proposer','complete':True,'scope':[r['id'] for r in records],
'baselines':{'specification_commit':B,'formal_root':'deliverables/final-specification-set/','reference_commit':R,'reference_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','reference_root':'/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials','identity_audit':'parent-established; not repeated'},
'parameters':{'requested':{'model':'gpt-6-astra','reasoning_effort':'ultra','service_tier':'default','Fast':'forbidden'},'actual_echo':'UNVERIFIED','actual_model':'UNVERIFIED','actual_reasoning_effort':'UNVERIFIED','actual_service_tier':'UNVERIFIED','actual_speed_mode':'UNVERIFIED','global_configuration_changed':False},
'candidate_versions':change_info,'disposition_groups':{'required':[r['id'] for r in records],'optional':[],'no_required_revision':[],'unresolved':[],'out_of_scope':change_info['out_of_scope']},
'counts':{'assigned':12,'reviewed':12,'required':12,'optional':0,'no_required_revision':0,'unresolved':0,'out_of_scope':len(change_info['out_of_scope'])},
'classification_note':'Whole-ID recommendations all required/P2, but accepted/excluded/no_required_revision/optional/unresolved subclaims are separate. This is not unconditional acceptance of every proposer sentence. Final global aggregation belongs to parent.',
'operational_limits':{'writes':'C03 only','other_agents_created':0,'commits_or_pushes':0,'installs_or_update_launches':0,'reference_execution':0,'model_execution':0,'host_or_demo_execution':0,'feature_matrix':'not modified: user narrowed write scope; parent owns global aggregation'},
'resolutions':records}
(O/'resolution.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
# Coverage counts exact cited ranges/pointers only. Avoid pretending truncated broad requests were full reads.
cov={}
for r in records:
 for typ in ['source_directly_read','spec_directly_read']:
  for a in r[typ]:
   key=(a['version'],a['path']);ent=cov.setdefault(key,{'version':a['version'],'path':a['path'],'sha256':a['sha256'],'kind':'reference_source' if typ=='source_directly_read' else 'specification_or_effective_supplement','ranges':[],'selectors':[],'finding_ids':[]})
   ent['ranges'].extend(a.get('read_ranges',[]))
   if a.get('pointer') or a.get('rows'):ent['selectors'].append({k:a[k] for k in ['pointer','rows','fields'] if a.get(k) is not None})
   ent['finding_ids'].append(r['id'])
for e in cov.values():
 merged=[]
 for a,z in sorted(set(tuple(x) for x in e['ranges'])):
  if merged and a<=merged[-1][1]+1:merged[-1][1]=max(merged[-1][1],z)
  else:merged.append([a,z])
 e['ranges']=merged;e['finding_ids']=sorted(set(e['finding_ids']))
coverage={'schema_version':'gr5.c03.reading-coverage.v1','complete':True,'scope':res['scope'],'source_baseline':R,'specification_baseline':B,'formal_root':'deliverables/final-specification-set/','entries':list(cov.values()),
'coverage_policy':'Per-ID resolution records are the authoritative semantic coverage. This ledger unions their exact directly read ranges and selected JSON/TSV fields. Search hits, hash operations, prior PASS and read-request size do not count as full semantic reading.',
'raw_read_log':'direct-read-log.jsonl records requested ranges, with some oversize or beyond-EOF requests; not itself a full-read certification.',
'capture_limit_adjustments':['Broad wp78 TSV request was truncated; no full TSV read claimed. Only explicitly selected semantic fields/rows are cited.','Formal README broad request was truncated and is not used as behavioral evidence.','WP11 broad output had a truncated line69; that line is not in cited coverage.','Original interpreter matrix output had a truncated unrelated choices paragraph; only fully visible pertinent sections are cited.','Source ranges beyond EOF are clipped; no absent lines claimed.','Fishing/berry portions lost in an earlier aggregate output were reread in bounded ranges before completion.'],
'negative_evidence':{'search_artifact':'negative-search.txt','scope':'fixed B5 formal set and originals plus current junction text; then direct clause/row reading','effective_supplements':'Read selected relevant WP78 rows, B21 /cases/6 and /chains/1,/chains/5 plus AX20 directly. B09 43 catalog/18 designs and B17 40 records structurally filtered for these topics; no relevant candidates selected, no full semantic read claimed.','new_SI_names':'M03 SI labels are current review navigation, not a B5 independently sufficient behavior contract; actual B5 consumers and retained junction clauses inspected.'},
'execution_status':'STATIC_ONLY; reference/model/host/demo NOT_EXECUTED','unread_or_unknown':['Outside assigned12: GR5-M03-013 not source-reviewed.','Unrelated source modules, whole repository/global coverage, real binary map/common-event data and media not claimed.','No execution/real Demo reachability; malformed inputs and arbitrary plugins not exhausted.'],
'per_id_completion':[{'id':r['id'],'complete':True,'source_entries':len(r['source_directly_read']),'spec_entries':len(r['spec_directly_read']),'disposition':r['disposition']} for r in records]}
(O/'reading-coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
# Report is clean-room prose, no reference source fragments.
lines=['# C03 定点独立反证报告','', '已完成 GR5-M03-001–012 的一次独立质疑及有界整合。推荐 **12 条 required / P2**；整条 optional、no_required_revision、unresolved 均为0。不是原候选全部措辞照收：每条已分别记录接受、排除及已有充分承接的子主张。父会话唯一汇总，本目录不签全局关闭。','',f'固定 B5：`{B}`；正式根 `deliverables/final-specification-set/`。固定 R：`{R}`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，从用户指定桌面只读根直接读取。身份沿父会话既有核验，不重复行政审计。','',f'候选首次及收尾 SHA-256 均为 `{initial_hash}`，范围内无差异。首次读取已有 **GR5-M03-013**，列为 **out_of_scope** 交父，未扩审。原12条候选完整保存在 `resolution.json` 各条的 `original_candidate`，也保留原始字节快照 `candidate-initial.json`。','', '请求参数：gpt-6-astra / ultra / default / 禁Fast；实际参数回显不可得，全部记 **UNVERIFIED**。未检查额度、认证、私有会话或后端，未改全局配置，未创建其他会话/agent。','', '| ID | 推荐 | 独立反证后的范围 |','| --- | --- | --- |']
shorts=[
'保留方向/图案原值门；同页早退已有局部承接，不重复立项。',
'保留绑定私有键与当前图角色投影；排除207/209显式跟随覆盖，已有过场绑定A规则无需重修。',
'补事件私有秒/日数学、空记录差异及登记；不能套WP06会清槽的公开计时。',
'补同步安装、覆盖、自主延迟和总长上限；清forcing只限不同有效页，无页另列。',
'补对角不累计玩家距离及四向专属副作用；保留一般离格/步完成通知。',
'补直接零偏移跳跃例外；1是名义距离下限，非峰高1；索引推进已有承接。',
'按物品回调/解释器直接脚本分公共事件返回和内置段；负ID结果依实际数组。',
'补严格预检→计数→普通尝试→记录→条件等待；strict通过不等于必位移。',
'补202直接/变量/交换及缺主/缺副/方向后处理；复用通用落位和002身份规则。',
'分列页、公共并行、111开关子型、111脚本子型、公共自动运行；nil比较结果不能混用。',
'取消/满包只是不主动采摘重置，不能冻结时间；反例补非淡出、无覆盖物、先微更新等前提。',
'补两个辅助在独立355中的额外推进；保留116让出及脚本先合并规则。']
for r,s in zip(records,shorts):lines.append(f"| {r['id']} | required / P2 | {s} |")
lines += ['', '独立质疑采用最强现有承接优先：逐条直接阅读源定义及必要调用者、处理器、配置，再读固定B5正文、附表、向量、原稿与相关有效补充。WP06公开墙钟计时、WP17微更新顺序、WP11/13身份与记录规则、GR3/GR4既有向量均作为反证尝试；没有凭旧PASS或提出者摘要裁决。具体路径、行段、字段选择和文件哈希见 `resolution.json` 与 `reading-coverage.json`。','', '关键收窄及验收观察点：','']
for r in records:
 lines.extend([f"- **{r['id']}**：{r['rebuttal']} 最小对照：{r['minimal_counterexample_review']}"])
lines += ['', '这些修订只要求准确交付固定参考的可观察事实，不要求修复参考、复制源内部结构、设计未来API或预先选择异常兼容政策。已有充分承接的子规则在JSON中单列为 `no_required_revision_claims`；没有将纯文风或未来政策列入必修。','', '本轮参考执行0、行为模型执行0、宿主/Demo执行0。只做文件读取、Git固定对象读取、搜索、JSON/TSV解析、哈希和产物结构检查；数学及状态结果是静态推导，不是执行回执。真实地图/公共事件/素材、实际可达性及异常宿主收口继续未知。','', '仅写C03目录；未改正式、参考、原稿、历史、共享或M03文件，未提交/推送、安装或启动update。未修改全局Feature Matrix，由父会话接收本目录后统一汇总。','']
(O/'report.md').write_text('\n'.join(lines))
print(json.dumps({'resolutions':len(records),'required':12,'coverage_entries':len(cov),'candidate_sha256':initial_hash,'out_of_scope':change_info['out_of_scope']},ensure_ascii=False))
