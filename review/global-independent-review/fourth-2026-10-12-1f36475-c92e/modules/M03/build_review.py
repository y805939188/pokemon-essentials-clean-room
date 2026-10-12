"""Generate M03 review records only; never loads or executes reference programs."""
from pathlib import Path
import json
import subprocess

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
REF = Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
B = '1f36475d22120a0d1175967d5b17d71fe8311d88'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REVIEWER = '/root (M03 independent reviewer; actual model/reasoning/service-tier echo UNVERIFIED)'
FORM = 'deliverables/final-specification-set/'
S = 'Data/Scripts/'
FILES = {
 'map': S+'004_Game classes/004_Game_Map.rb',
 'factory': S+'004_Game classes/005_Game_MapFactory.rb',
 'character': S+'004_Game classes/006_Game_Character.rb',
 'event': S+'004_Game classes/007_Game_Event.rb',
 'player': S+'004_Game classes/008_Game_Player.rb',
 'common': S+'004_Game classes/009_Game_CommonEvent.rb',
 'follower': S+'004_Game classes/010_Game_Follower.rb',
 'followers': S+'004_Game classes/011_Game_FollowerFactory.rb',
 'system': S+'004_Game classes/002_Game_System.rb',
 'screen': S+'004_Game classes/001_Game_Screen.rb',
 'temp': S+'004_Game classes/001_Switches and Variables/001_Game_Temp.rb',
 'scene': S+'003_Game processing/002_Scene_Map.rb',
 'start': S+'003_Game processing/001_StartGame.rb',
 'interpreter': S+'003_Game processing/003_Interpreter.rb',
 'commands': S+'003_Game processing/004_Interpreter_Commands.rb',
 'world': S+'012_Overworld/001_Overworld.rb',
 'metadata': S+'012_Overworld/002_Overworld_Metadata.rb',
 'time': S+'012_Overworld/003_Overworld_Time.rb',
 'field': S+'012_Overworld/004_Overworld_FieldMoves.rb',
 'fish': S+'012_Overworld/005_Overworld_Fishing.rb',
 'berry': S+'012_Overworld/006_Overworld_BerryPlants.rb',
 'dungeon': S+'012_Overworld/008_Overworld_RandomDungeons.rb',
 'weather': S+'012_Overworld/001_Overworld visuals/001_Overworld_Weather.rb',
 'transition': S+'012_Overworld/001_Overworld visuals/003_Overworld_MapTransitionAnims.rb',
 'surf_sprite': S+'005_Sprites/005_Sprite_SurfBase.rb',
 'global_sprite': S+'005_Sprites/006_Spriteset_Global.rb',
 'items': S+'013_Items/002_Item_Effects.rb',
 'settings': S+'001_Settings.rb',
 'mapdata': S+'010_Data/002_PBS data/018_MapMetadata.rb',
 'dungeondata': S+'010_Data/002_PBS data/020_DungeonParameters.rb',
 'berrydata': S+'010_Data/002_PBS data/007_BerryPlant.rb',
 'utilities': S+'019_Utilities/001_Utilities.rb',
 'messages': S+'007_Objects and windows/011_Messages.rb',
 'mart': S+'016_UI/020_UI_PokeMart.rb',
}
SPEC = {
 'wp11': 'engine-overworld/wp11-map-topology-transfer.md',
 'wp12': 'engine-overworld/wp12-terrain-movement-vehicles.md',
 'wp13': 'engine-overworld/wp13-map-events-npc-followers.md',
 'im': 'engine-overworld/wp13-interpreter-command-matrix.md',
 'mr': 'engine-overworld/wp13-move-route-matrix.md',
 'wp14': 'engine-overworld/wp14-random-dungeons.md',
 'wp59': 'engine-overworld/wp59-world-time-weather-field-moves.md',
 'fish': 'engine-overworld/wp60-fishing.md',
 'berry': 'pokemon-rules/wp60-berry-plants.md',
 'wp61': 'pokemon-rules/wp61-field-passive-effects-and-blackout.md',
 'wp16': 'engine-overworld/wp16-world-rendering-and-visual-transitions.md',
 'tests': 'test-catalog/engine-overworld-wp11-15-59-60.md',
 'ptests': 'test-catalog/pokemon-rules-wp53-60-61-62-69-70.md',
 'vtests': 'test-catalog/engine-overworld-wp16.md',
 'save': 'generic-kernel/wp09-save-startup-continue.md',
 'ktests': 'test-catalog/generic-kernel-wp05-06-07-08-09-10.md',
 'scope': 'scope-statement.md',
 'wp75': 'demo-dx/wp75-project-conversion-and-authoring-tools.md',
}

def write(name, data):
    (OUT/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

def src(key, loc, fact):
    return {'path':FILES.get(key,key), 'commit':R, 'lines_or_symbol':loc, 'fact':fact}

def spec(key, loc, fact='本次只核指定条款/向量，不作整文件通过'): 
    return {'path':FORM+SPEC.get(key,key), 'commit':B, 'lines_or_symbol':loc, 'fact':fact}

CAPS=[]
def cap(n, desc, sources, specs, checks, reason, entry, limits, status='supported', findings=(), history=(), owner='M03', projection=None):
    CAPS.append({'capability_id':f'GR4-CAP-M03-{n:03}', 'module':'M03', 'description':desc,
      'source_anchors':sources, 'spec_anchors':specs, 'entry_and_preconditions':entry,
      'configuration_data_host_limits':limits, 'reviewer':REVIEWER,
      'checked_branches_boundaries':checks, 'evidence_level':['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR'],
      'material_availability':{'source_text':'AVAILABLE','formal_text':'AVAILABLE', 'maps_demo_media':'MISSING_MATERIAL','host_execution':'NOT_ESTABLISHED'},
      'status':status, 'reason':reason, 'related_findings':list(findings), 'history_links':list(history),
      'not_checked':['未执行参考、仿制模型或游戏宿主；未证明实际地图/事件可达。',limits],
      'primary_owner':owner,'projection':projection,
      'status_semantics':'supported 仅指所列分支 supported_static；本数组是有界能力样本，非全功能分母。'})

cap(1,'地图连接锚点、跨缘坐标与驻留裁剪',
 [src('factory','68–112,114–140,226–243,307–327,361–375,392–493','方向连接归一为锚点；首个有效目标生效；移动中不切图/裁剪。'),src('PBS/map_connections.txt','4–40','连接文本提供带偏移的双端方向样本；不证明地图尺寸。')],
 [spec('wp11','§3.2、§4、§5.2'),spec('tests','MP01–03、MP22–24')],
 ['A锚点(10,3)、B锚点(0,5)，A(10,4)换到B(0,6)，B须有效。','无连接拒绝；源/目标方向位阻挡与目标全向阻挡区分；玩家移动中不切图。'],
 '支持锚点偏移、首匹配及有效范围门；真实路线未确认。','尺寸/连接数据有效，无插件改写。','地图文件缺失；未逐条验证PBS所有连接，未审自连接/重复连接全部组合。')
cap(2,'显式转移的排队、游泳参数与失败前缀',
 [src('commands','722–747','201排队、推进一项并本轮停止。'),src('scene','56–101,121–133,165–175','两个消费者传false保游泳；有音频时先读目标图。'),src('player','262–266,575–597','落位、载具取消与骑行目的地门分开。')],
 [spec('wp11','§4、§8'),spec('im','201行'),spec('wp12','§5.1')],
 ['同图不重建/不发进入；跨图重建内进入早于玩家落位。','BGM/BGS非空导致缺图早失败；均空时才到重建失败前缀。','取消游泳false仍单独判断骑行。'],
 '所列转移合同支持；临时底座清理承诺另列CAP003。','201资格门通过，或显式直接调用；必要宿主操作正常返回。','未运行资源异常；转场演出主责M10。')
cap(3,'冲浪临时底座/结束标记与转移的生命周期',
 [src('field','705–751','开始先写底座后跳；只有有底座的玩家步后消费者清底座并条件清结束标记。'),src('scene','72–101','转移本身无上述两字段清理。'),src('player','575–592','载具取消只处理游泳/骑行标志与外观。'),src('surf_sprite','44–79','游泳显示优先使用非空底座坐标。')],
 [spec('wp59','§7 L296'),spec('wp12','§5.2 L169–171'),spec('wp61','§3.2'),spec('wp16','§4.3 L130','有过渡坐标时按它定位，未承诺转移清理；此条支持显示输入差异'),spec('vtests','B04-W07','仅已清过渡坐标的正常显示对照')],
 ['失败上水跳跃留下底座；同图保游泳转移没有完成步时底座仍在。','后续满足场景/玩家/底座三门的步后通知才清理；非玩家/无底座反例。'],
 'WP59额外承诺转移重置，与已读转移/覆写/消费者不符。','有效场景、同图正常转移、非冰瀑状态、无额外相关写入或步后通知。','只证明状态和显示输入选择，不证明缺失素材的可见像素。','partial',['GR4-M03-002'],projection='WP11转移、WP12运动、WP61通知、M10显示输入')
cap(4,'镜头卷动速度、SnapEdges、包装等待与数值状态',
 [src('map','323–394,439–458,497–565','镜头时长/钳边、直接与等待包装、居中整数/浮点商。'),src('commands','784–789','203已有任务等待，新任务立即继续。'),src('mart','242–244,299–320,345–362','共用买卖画面和背包卖出分支调用不同。')],
 [spec('wp16','§3.1.1'),spec('im','203行'),spec('vtests','GR3-CAM01、03、05–09、14–15、18')],
 ['速度4右1格：.1秒64、.2秒128子像素；小地图钳0。','512×384目标(10,8)：整数起点0终点384/384，浮点0.0终点320/320。','包装0即时与203速度0区分；背包存在卖出无共用卷动。'],
 '本轮定点重读支持原GR3验收核心和具体消费者分支。','无旧任务、无其它镜头写入、有效地图/更新机会。','未穷尽中途覆写/换图；实际镜头画面未审。',history=['GR3-M03-001'],projection='M10共用显示/商店；M03负责镜头输入生成')
cap(5,'同图双端通行、跨图单目标门和多格对角',
 [src('map','142–267','图块事件提前许可；玩家/非玩家/严格入口不同。'),src('character','237–303','同图双端、事件/玩家碰撞及对角固定分解。'),src('player','238–250','宽松边界先于调试门。'),src('factory','157–200','跨缘目标方向0，不追加源格方向位。')],
 [spec('wp12','§3.2、§4.3'),spec('wp11','§4跨界通行'),spec('tests','MV15、17、26、40')],
 ['非玩家陆→水由目标反向检查拒绝，水→陆由源格拒绝。','优先级0图块事件提前通过可绕地图层骑行冰禁，外层碰撞仍查。','多格向上对角先横后上；调试也不越过无有效邻图门。'],
 '所选组合及层次支持；未把所有角色通行合成单一规则。','无插件；人工有效图层、占格和阻挡前提明确。','18地形数据未逐条重比；全部形状×地形组合未审。')
cap(6,'普通移动遭遇门、跳跃失败和步前/步后状态',
 [src('player','130–193,431–554','普通移动两次遭遇门、岩架两格跳、距离开始即写、步后通知在完成后。'),src('character','767–799,893–989','跳跃落点失败无运动/计步；运动插值与通知次序。')],
 [spec('wp12','§4.1–4.3'),spec('tests','MV03、MV68、MV72、MV75')],
 ['遭遇标记真不通行/位移/碰撞；直接跳跃无同一普通移动门。','强制路线WAIT不自动阻止场景末端菜单登记；消息门阻止消费。','失败跳跃与玩家撞墙运动标记不同。'],
 '选定运动与输入分层支持。','给定遭遇处理正常返回、合法运动输入、明确本次输入。','不重审遭遇概率或实际帧手感；快速多输入竞态未审。')
cap(7,'载具、上水提交和瀑布启动守卫',
 [src('player','38–100,575–609','骑乘跟随门、运行速度与载具取消。'),src('field','685–785,891–969','上水先提交；上瀑朝上/地形门区别于菜单资格。')],
 [spec('wp12','§4.2、§5'),spec('wp59','§5.3、§5.7'),spec('tests','MV42、MV05、WT19')],
 ['无跑鞋潜水可跑判据、冰不禁跑但禁骑行。','上水前跳失败仍置冲浪/统计/底座。','向右面向瀑布：菜单可过，效果true，但不启动攀瀑；朝上瀑顶菜单拒/直接可启。'],
 '正常提交与守卫差异支持；转移残留问题另报。','徽章/个体/媒体正常；明确调用入口和朝向。','未审十二族所有组合或冰瀑同时标记；音频/图形仅请求。')
cap(8,'事件页、触发与更新资格',
 [src('event','9–44,133–291','末页优先、同位/触碰/感知门、更新持续许可。'),src('player','284–385','玩家同位/面前/柜台与感知选择。'),src('map','460–465','菜单抑制地图事件但公共事件继续。'),src('common','30–55','并行公共事件开关门与独立解释器。')],
 [spec('wp13','§3.1–3.2'),spec('tests','EV01、EV06、EV24')],
 ['具名非through与hiddenitem不可越格触发；页变化清starting。','一旦成功更新的同实例持续获得调用，离屏不自行停。','菜单地图事件停调用/公共事件继续；trainer与counter感知入口不等价。'],
 '样本规则支持。','可读事件页夹具、更新调用有效；无外部改字段。','真实事件页缺失；并行跨图所有身份碰撞未审。')
cap(9,'解释器上下文、等待、公共事件与命令推进',
 [src('interpreter','11–18,45–135,183–202','失联只归零事件ID、子解释器先行、路线等待仅显式标记门。'),src('commands','371–386,514–520,856–873','105双推进、106单调秒数、117子调用、209与210等待区分。')],
 [spec('wp13','§4.1–4.2'),spec('im','105、106、117、209、210行'),spec('tests','EV17、IM05')],
 ['失联仍可继续全局命令；超过100层拒。','209设置强制路线不置解释器等待；210才查玩家/当前图事件/跟随者。','105内外各推进一次；106 n/20秒。'],
 '所查命令支持；96分派总数及全部参数未重新核算。','命令列表合法、调用正常，无外部覆盖。','未逐条审96命令、消息合并/表达式全分支和宿主错误呈现。')
cap(10,'事件消去的三个入口与局部记录',
 [src('commands','11–35,502–509','116为正事件ID记录消去，即使事件不存在；索引+1并停止本轮。'),src('event','46–49','单纯实例消去只改变实例及刷新。'),src('interpreter','292–300','记录式脚本辅助先查事件存在。'),src('metadata','154–168','记录按当前图/ID登记，恢复辅助只在匹配图执行。')],
 [spec('wp13','§3.3 L50'),spec('im','116行 L37'),spec('tests','GR3-MR12 L490')],
 ['正常116消去并记录；正ID但事件缺失仍记录；ID0无记录但推进停止本轮。','普通实例消去不记录；辅助缺实例不记录。'],
 '现有文字未明确承接116，并在对照中把它与一般实例消去并列。','当前图和局部记录存在、解释器事件ID给定、命令合法。','不承诺普通读档还原记录；恢复仍先清记录。','partial',['GR4-M03-003'],['GR3-M03-004'],projection='M02保存字段消费者；新增116生产端边界')
cap(11,'移动路线执行、空路线、等待与脚本前缀',
 [src('character','348–374,427–550,912–923','空路线早退，状态/转向/移动的推进机会与三前缀分开。'),src('player','121–128','玩家碰撞有运动计时。')],
 [spec('mr','§1–2'),spec('tests','MR01–02、04–05、07–08、10–15、18–21'),spec('wp75','L235')],
 ['仅终止项强制路线不恢复且210等待可持续。','非跳过NPC受阻留索引；玩家碰撞按运动标记推进。','任一行行首前缀匹配，空白/接收者不匹配，异常先于推进。'],
 '路线调度合同支持；三种范围随机辅助的实际移动语义另列CAP012。','合法路线、实际更新机会，脚本前缀案例以正常求值为前提。','没有求值用户脚本；系统包装waitComplete/门编译仅盘点未独立深查。')
cap(12,'围绕事件原始位置的有界随机移动与单轴变体',
 [src('character','669–700,553–565,376–385','先按原始位置及两个范围构造方向候选，再等概率尝试一次；落位不改原始锚点。'),src('event','9–18','事件原始位置来自数据位置。')],
 [spec('wp12','§4.3 L146–148'),spec('mr','§1 L18、代码9/45'),spec('tests','MR08、MR10–15、MR18–21'),spec('wp75','L235')],
 ['原始(5,5)、当前(7,5)、横2纵0仅向左；横纵均0不抽随机/不移动。','负范围不限该轴，0禁该轴；正范围依据原始锚点，非每次当前位置重置。','抽选方向被阻挡不重抽；UD/LR只是轴限制变体。'],
 '全131文件命中仅承接前缀调度与普通四向随机，缺有界移动能力规则。','正常非玩家事件、有效原始锚点、整数范围、无方向固定和外部写入。','Demo是否使用这三种辅助缺事件材料；不要求保留函数API。','partial',['GR4-M03-001'])
cap(13,'事件跟随的位移、持久状态和传送隐藏',
 [src('follower','36–168,174–214','一/两格条件位移，其余非重合直接定位；实际通行独立于严格入口。'),src('followers','89–137,155–190,242–287','去重、领队链、传送及可见性/互动门。')],
 [spec('wp13','§6.2'),spec('wp12','§3.2层5'),spec('tests','FW01–07')],
 ['中格可通走两步，不能保证第二步通过；中格阻而落点/起点可通尝试跳。','同轴三格及(1,1)直接定位；强制路线跳过跟随。','传送写数据和隐藏标记，开始移动才清；有跟随不阻普通传送。'],
 '所选分支支持。','领队和地图有效；无外部跟随数据变更。','门事件编译/移除后的原事件复现、动态公共事件覆盖完整流程未审。')
cap(14,'未驻留地图查询触发地牢建立副作用',
 [src('factory','54–92,157–169,203–206,307–309','不加入集合仍实际建立。'),src('map','45–74','建立通知早于运行时事件。'),src('dungeon','428–450,1063–1106','消费种子、生成改图、成功写暂存，无传送标记门。')],
 [spec('wp11','§3.1.1'),spec('wp14','§3.1.1'),spec('tests','GR3-DQ01–03、06、09')],
 ['未驻留两次查询可两次生成；驻留且无重建不生成。','非地牢仍通知但不走本消费者；种子清空/重播不等于保证某空抽样耗随机。','后继通知异常保留已写暂存。'],
 '本轮支持原GR3有界整改；不证明Demo默认查询链。','B可读、地牢标记、参数和摆放按各案例限定。','未运行生成；空集合原生抽样消费量、插件订阅者未审。',history=['GR3-M03-002'],projection='M02随机和通知；M01地图装载')
cap(15,'地牢布局输入与事件/玩家摆放失败分流',
 [src('dungeon','120–215,428–475,510–555,982–1106','空节点先失败；零房间退化无候选；摆放次数与玩家失败标志分开。'),src('dungeondata','33–117','区域/版本回退、默认参数和正整数/非负数据字段。'),src('PBS/dungeon_parameters.txt','3–30','cave/forest参数样本。')],
 [spec('wp14','§3.2–3.5、§4.2、§6、§8'),spec('tests','DG01–02、DG27、DG34、GR3-DQ06')],
 ['N25概率70取17；N1概率200只1；N0仍0。','2×2 antiring无起点，早于房间退化。','事件最终失败抛错；仅玩家100轮失败正常返回且暂存旧值。','摆放1×1相邻对角拒；间隔两格许可，底行左锚点。'],
 '选定输入和异常阶段支持。','有效图块映射、明确各前序阶段通过；不证明终止性。','256墙掩码、自动图块、装饰全表和大网格奇数构造的引入模块未复核；均可读未审。')
cap(16,'日夜、季节、缓存与应用门',
 [src('time','4–124,129–224','宿主时间、五谓词、整数明暗/色调插值、单调缓存及月模4季节。'),src('settings','72','TIME_SHADING默认真。')],
 [spec('wp59','§3.1–3.3、§3.5'),spec('tests','WT04、WT30')],
 ['5/10/14/17/20小时边界；10–13仅day。','06:30明暗138；关闭配置返回既有非零缓存，非地图应用不清对象。','候选不匹配仍可写星期名并刷新。'],
 '选定时间合同支持。','宿主时间分量和单调时间有效；对象/地图有效。','月相/星座整公式仅读规格未反向核源；备份与插件时间源未审。')
cap(17,'世界天气意图、进入重掷与显示触发门',
 [src('world','241–252','旧ID0/同ID不重掷、同类型不写新天气。'),src('screen','66–70','power映射和持续输入保存。'),src('global_sprite','36–52','只有天气类型差异才调用显示更新。'),src('weather','11–18,66–95','渐变进行时拒绝新请求；正持续数值只选渐变分支。'),src('mapdata','33–48','Weather schema天气身份和非负整数概率。')],
 [spec('wp59','§4.2–4.5'),spec('wp11','§4天气观察点'),spec('tests','WT08、WT10、MP22–24')],
 ['概率0/100/>100；同图不重掷、无字段可清旧天气。','边缘进入后持续输入20；显式无该后写。','同类型只改power不会由显示集合入口刷新；进行中拒新请求。'],
 '意图与触发门支持；固定渐变全部阶段未重审。','天气身份有效；区分意图状态和呈现。','天气9项参数全表、粒子随机/结束旧粒子条件可读未审；交M10演出。')
cap(18,'场地能力入口差异：徽章、潜水、回程与上瀑',
 [src('field','4–64,319–420,837–969','资格/确认/执行分层，潜水音乐入口差异，Teleport解析和瀑布朝向门。'),src('settings','110–124','徽章计数默认和1–8阈值。')],
 [spec('wp59','§5.1–5.4、§5.7'),spec('tests','WT26、WT28')],
 ['徽章负数/debug绕过；默认计数vs指定徽章。','直接上浮与菜单上浮同位置/状态、不增计数，但音乐末请求不同。','Teleport优先healingSpot→角色家→全局家并朝下。'],
 '所选四族/共用门支持，未对12族全部执行正文背书。','合法目标/资源，明确界面资格已查或直接工具入口。','CUT/DIG/FLY/HEADBUTT/ROCKSMASH/STRENGTH/SWEETSCENT完整效果链本轮未深查；共用演出及洞穴动画主责M10。')
cap(19,'钓鱼资格、概率、输入截止与公共事件替代',
 [src('fish','1–110','提前取消、加速抽取、严格超时门、输入优先和正常收尾。'),src('items','49–56,276–315','三竿资格检查当前出边；成功才请求遭遇。'),src('utilities','524–538','有效公共事件才返回替代成功。'),src('settings','80–86','自动关闭、公共事件ID -1。')],
 [spec('fish','§3–6、§8–10'),spec('tests','FS03–04、06、09、15–18')],
 ['OldRod加速67.5接受0–67共68%；无表仍等待且不咬。','窗口.5：.500无输入继续，.510有输入先成功，无输入失败；自动仍待输入。','有效开始公共事件替代移动类型/锁定/动画整体；无效回退。'],
 '选定规则支持。','首非蛋成员口径沿队伍合同，必要宿主调用正常。','未重审钓鱼战斗环境/捕球倍率/候选过滤；未量测手感。')
cap(20,'树果两机制、结算时点、干涸与交互提交',
 [src('berry','21–160,221–233,245–320,357–470','冻结机制、旧显示不结算、水分和重植、施肥取消与采摘提交。'),src('berrydata','13–43','数据默认、Yield对调、常量和水壶列表。'),src('settings','77','世代4以上新机制默认。'),src('PBS/berry_plants.txt','3–6,28–31,43–56','3h/15、LEPPA/LUM/FIGY样本。')],
 [spec('berry','§3–9'),spec('ptests','BP01、03、05、07、10、12、16、18、20')],
 ['新机制10h：阶段4、水分-5、惩罚3；旧显式结算雨浇，常规显示不推进。','DAMPMULCH 15整数折半7；重植只按剩余周期扣水。','施肥后取消保留消耗；满包拒不清植物；工具与外层reset分开。'],
 '所选新/旧世代和取消边界支持。','合法BerryPlant数据/事件、背包调用正常；机制冻结与当前UI配置分开。','Gen5–8备份全数据差异、完整种植Demo会话未审。')
cap(21,'步进通知、友好周期、煤烟和世代毒伤',
 [src('world','70–187','普通计步/强制早退、煤烟、毒伤门及逐成员处理。'),src('character','967–985','运动完成先一般通知。'),src('player','543–553','玩家完成后再进入步后链。'),src('settings','17,99–102','默认世代8不毒伤，<=4毒伤、<=3可濒死。')],
 [spec('wp61','§3–5'),spec('ptests','FP01–02、06–08、FP33')],
 ['普通平移一次一般通知再计步；强制/解释器保持时可两次一般通知而不计步。','128友好周期即使无可战成员仍归零。','Gen8毒伤关；Gen4 HP1清毒；Gen3 HP1倒下；两独立开关四组合。','煤烟非玩家也擦；资源统计仅玩家持袋正增量。'],
 '限定入口组合支持。','非冰瀑自动/无中断转移、明示路线保持、合法可战成员；注入回调不混入默认。','寄养/孵化/Shadow/Repel/Safari后继各域完整效果未重审。',projection='M02计步通知；M04成员口径；M03步进世界投影')
cap(22,'病毒日期门与失败回程的目的地/清理分流',
 [src('world','5–25,115–123,224–237','日期不同只扣一次、首门含感染蛋；失能交接及healingSpot写入。'),src('transition','80–138','捕虫优先、统计治疗先行、家图缺失早退、普通末尾清逃点。')],
 [spec('wp61','§6.2、§7.1–7.2'),spec('ptests','FP14、FP17–18、FP35')],
 ['跨多日/回拨均只一次，last为空不进；感染蛋可过首门但不被扣。','中心有效优先；家图缺失统计/治疗已发生却保留逃点；无家仍末尾清逃点。','非地图场景不传送但参数/刷新请求可发生。'],
 '所选日期和回程分支支持。','Player成员筛选及lowerPokerusCount沿领域合同；资源存在门仅存在性。','病毒编码方法本轮未重读；捕虫内部回程/战后款项及完整治疗覆写未重审。',projection='M04个体病毒；M09捕虫；M10淡出视觉')
cap(23,'SPECIAL具名过场跳过与重新启动请求',
 [src('system','279–285','SPECIAL按写A→结束→启动顺序。'),src('messages','26–50','108/408全文相等；空数组和空值区分。'),src('interpreter','54–82,94–96,183–202,323–330','上下文、刷新与重新选择。'),src('commands','128–135','结束列表/覆盖/有效主事件解锁。'),src('scene','121–133,165–214','正常/迷你系统更新先于正常末端输入。')],
 [spec('wp13','§4.3'),spec('wp12','§4.3末段'),spec('tests','GR3-CS01–13')],
 ['准确Cut Scene/大小写尾空格反例；匹配末端空数组通过。','A已真不另请求刷新但仍结束/请求启动；列表一项不设starting。','页切换可清starting，不保证立即A页；不承诺SPECIAL独占。'],
 '原GR3验收指定门与顺序支持。','主解释器运行、当前事件可解析；动作正常返回。','实际页/消息/快捷同轮宿主表现未运行。',history=['GR3-M03-003'])
cap(24,'正常读档记录先清空与条件恢复的字段门',
 [src('start','63–104','两恢复分支与图更新→恢复辅助顺序。'),src('factory','17–27,142–153','同ID实际重建仍比较新实例0而发离开。'),src('world','224–237','进入清局部记录。'),src('metadata','144–182','异图真through仍写；假不清、异图缺事件失败。')],
 [spec('wp11','§6.1–6.2'),spec('save','§4.1 L94–96'),spec('tests','GR3-MR01–11、13'),spec('ktests','U02-SV-WORLD01–02')],
 ['复用实例可留状态但表已清；同ID重建与同图显式传送不可混用。','A记录/B事件同ID：位置朝向不改而真through写入；假保持。','异图缺事件真值失败、同图缺事件跳整条；无整体回滚。'],
 '原GR3恢复端核心支持；生产端116新增缺口单列CAP010，不转移旧PASS。','合法正常读档，或明示记录仍存的直接辅助夹具。','未读真实存档；异常宿主恢复、额外动态记录生产者未审。',history=['GR3-M03-004'],projection='M02保存/加载共享投影')

write('capabilities.json', CAPS)

# Full formal-set counterevidence search. Store locations, never source fragments.
queries = {
 'GR4-M03-001':[
  r'move_random_(range|UD|LR)|xrange|yrange',
  r'限定.{0,8}(随机|移动)|范围.{0,6}随机移动|随机.{0,6}(漫游|游走|活动范围)|原始位置|初始位置',
  r'随机移动|随机方向|单轴|游走|漫游范围|出生点'],
 'GR4-M03-002':[
  r'surf_base_coords|ending_surf',
  r'冲浪.*(残留|中断|重置)|上岸.*(残留|中断|传送)|中断.*转移',
  r'底座|基点|载具取消|取消游泳'],
 'GR4-M03-003':[
  r'116|删除事件|记录式消去|消去记录|erasedEvents|pbEraseThisEvent',
  r'消去.*(登记|记录)|记录.*消去|实例消去'],
}
negative={}
for fid, patterns in queries.items():
    entries=[]
    for pattern in patterns:
        cmd=['rg','--json','-n',pattern,FORM,'--glob','*.md']
        result=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
        hits=[]
        for line in result.stdout.splitlines():
            msg=json.loads(line)
            if msg['type']=='match':
                d=msg['data'];hits.append({'path':d['path']['text'],'line':d['line_number']})
        entries.append({'command':cmd,'pattern':pattern,'exit_code':result.returncode,'hits':hits,'hit_count':len(hits)})
    negative[fid]={'formal_baseline':B,'scope':'全部131正式Markdown，正文/附表/测试/shared/scope均包含','searches':entries,
                  'semantics':'搜索命中不等于语义覆盖；关键命中上下文和排除理由见findings.json。'}
write('negative-evidence.json',negative)

def finding(fid,title,category,sources,specs,expected,current,gap,premises,counter,normal,boundary,impact,neg,change,criteria,caps,history=None,relation='new'):
    return {'id':fid,'title':title,'module':'M03','severity':'P2','disposition':'REQUIRED','status':'OPEN_REVIEWER_CONFIRMED_STATIC',
     'reviewer':REVIEWER,'category':category,
     'source_baseline':{'commit':R,'tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','root':str(REF)},'source_anchors':sources,
     'specification_baseline':{'commit':B,'tree':'d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a','root':FORM},'spec_anchors':specs,
     'expected_reference_behavior':expected,'current_spec_behavior':current,'gap':gap,'preconditions':premises,
     'minimal_counterexample':counter,'normal_case':normal,'failure_or_boundary_case':boundary,
     'impact_on_independent_implementation':impact,
     'negative_evidence_search':{'artifact':'negative-evidence.json','key':fid,'scope_file_count':131,'context_results':neg,
        'source_followup':'固定R所有脚本检索定义、同名覆写及所涉状态读写；追踪下述source anchors的实际入口/消费者；不把缺Demo当不存在。'},
     'proposed_spec_change':change,'acceptance_criteria':criteria,
     'affected_files':list(dict.fromkeys(a['path'] for a in specs)),
     'shared_contracts':['WP11地图状态/转移','WP12运动与通行','WP13事件/路线及测试目录'] if fid!='GR4-M03-002' else ['WP11转移','WP12冲浪提交/步后收尾','WP61步后通知','WP16/M10冲浪显示输入'],
     'dependencies':['有效地图/事件夹具','固定参考默认定义，无插件覆写','普通调用和指定更新机会'],
     'related_capabilities':[f'GR4-CAP-M03-{c:03}' for c in caps], 'related_findings':[],
     'root_cause_group':fid,'history_links':{'relation':relation,'third_round':history,'second_round':None,'note':'未知第二轮关联不猜ID；旧CLOSED身份不修改。'},
     'evidence_level':['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR'],'execution_status':'NOT_EXECUTED',
     'confidence':'HIGH_STATIC_WITH_STATED_PRECONDITIONS',
     'unknowns':['实际Demo使用/事件可达性未知；宿主和媒体结果未执行。'],
     'excluded_claims':['不要求修参考、不实现框架或保留源API/结构。','不宣称全部本域或全套规格均已审。'],
     'user_decision_needed':'无需决定是否补事实；若未来实现选择不同兼容政策，应另阶段明确，不由本审者代定。',
     'review_resolution':{'decision':'REQUIRED_FACT_CONTRACT_REVISION','independent_counter_review':'PENDING_MAIN_COORDINATOR','formal_files_modified':False}}

F=[]
F.append(finding('GR4-M03-001','范围随机移动只承接了路线让出时机，未承接原始位置边界与单轴规则','missing_behavior_family',
 [src('character','669–700','范围随机选择有负/零/正三态、原始锚点及UD/LR变体。'),src('character','376–385,539–548,553–565','落位不改原始锚点；脚本调用后按字面让出；选向后普通移动可受阻。'),src('event','9–18','事件原始锚点取地图事件数据。')],
 [spec('wp12','§4.3 L146–148','只有四正向随机、接近/远离和自主策略。'),spec('mr','§1 L18；§2 9/45行','只定义三前缀调度，没有两个范围输入的行为。'),spec('tests','MR08、MR10–15、MR18–21','只测试求值/前缀/推进。'),spec('wp75','L235','跨域命中也只承接同一前缀语义。')],
 '以事件建立时的原始位置作锚点。每轴负范围允许该轴两方向，零禁该轴，正范围依当前位置相对原始边界筛方向。对候选等概率只抽一次并尝试普通移动；碰撞不重抽。无候选直接返回。两个单轴变体禁用另一轴；之后移位不自动重定锚点。',
 '已明确普通四向随机和三种脚本文本前缀的同帧/下帧区别；没有说明这些辅助实际如何限制移动范围。',
 '兼容字面被保留，但实现者仍不能从正式行为合同决定其方向候选、锚点与零/负值语义。',
 ['1×1普通地图事件，原始锚点(5,5)，当前(7,5)，无方向固定/强制外部写入；地图内普通地面、所有方向通行。','执行范围随机能力，横范围2、纵范围0；固定R无额外覆写。'],
 {'input':'上述状态调用一次范围随机移动。','reference':'唯一候选为左，尝试到(6,5)；右移到(8,5)不会被选。','formal_gap':'四向等概率规则会容许向右/纵移；三前缀条款只能决定何时让出，无法排除这些错误结果。','evidence':'DERIVED_VECTOR; NOT_EXECUTED'},
 '从原始(5,5)且当前位置同点，横2/纵0，两横向候选各半；普通通过后位移一格。',
 '横纵0：没有随机抽取/移动；横2纵0位于右界且左格阻挡：只尝试左、不重抽其它方向；负横范围为不限制该轴。另给事件被落位到范围外的输入，锚点仍原值，不承诺自动钳回。',
 '会把受限游走实现成四向漫游、以当前位置不断重定边界，或受阻后重抽；改变NPC活动范围和随机消费。',
 ['全部131文件按原标识和中文范围/随机/单轴/原始位置别名搜索。','相关命中仅WP13路线§1、MR08/10–15/18–21、WP75 L235；逐读均是调度/求值合同。WP12§4.3普通随机并不定义有界族。','原始位置的其它命中属玩家元数据/储存位置，随机漫游命中属游走宝可梦等别域，不补本规则。','源端仅此一组定义，原始坐标赋值见角色初始化及事件初始化；未定位默认Demo调用，调用能力可由路线45到达。'],
 '在WP12或WP13正文补实现无关的范围随机规则，路线矩阵引用该合同；加边界/空候选/受阻/落位后锚点对照。不得把源方法或类结构当未来API。',
 ['静态：分别列横纵负/零/正语义、原始锚点生命周期、候选等概率及一次尝试不重抽。','静态：区分UD/LR单轴与普通四向；保留既有前缀调度，不把移动成败当推进门。','静态向量：原始(5,5)/当前(7,5)/横2纵0、双0、左阻挡、当前位置移出原范围；均标NOT_EXECUTED。','运行：本修订不以宿主执行为前置；将来动态验证需要合法地图夹具与真实随机控制，不能以文档/JSON校验充数。'],[11,12]))

F.append(finding('GR4-M03-002','WP59声称转移重置冲浪临时残留，但转移链没有该清理','contradiction',
 [src('field','705–751','上水先写底座后前跳；清理位于有底座的玩家步后通知。'),src('character','767–799','跳跃落点拒绝不启动运动，前跳返回false。'),src('scene','72–101,121–133,165–175','转移及正常201消费者；没有两个临时字段写入。'),src('player','64–100,262–266,575–592','实际覆写/载具更新也不清底座或结束标志。'),src('surf_sprite','44–79','保游泳且底座非空时，显示输入仍取底座。'),src('interpreter','116–123','结束冲浪标志另为解释器等待门。')],
 [spec('wp59','§7 L296','明确写中断（如转移）时残留按转移流程重置。'),spec('wp12','§5.2 L169–171','上水失败无回滚、步后清理三门已有准确限定。'),spec('wp11','§4 L59–71','列明取消载具/落位流程，无补充临时残留清理。'),spec('tests','MV05、WT19及MP显式传送族','没有失败上水后无步通知转移的对照。')],
 '默认转移入口和载具取消都不清surf_base_coords/ending_surf；这些临时量不能由转移本身保证重置。清底座需地图场景、玩家通知、有底座；结束标志又要为真才清。无此通知前的转移返回可保留残留。',
 'WP59§7给了转移重置保证，同时WP12/WP61把清理正确绑定玩家步后通知；WP11被引用但无此重置。',
 '把后续有条件的收尾写成转移本身的无条件保证。',
 ['合法20×20同图，玩家初始静止(5,5)、向右，无冰瀑/强制移动/跟随者；无其它字段改写。','直接上水入口前跳(6,5)因具名非through阻挡事件拒绝；相关资源调用正常，故surfing=true、底座(6,5)，未启动跳跃。','随后正常201转同图(10,10)、方向右，由场景按false保游泳；没有完成步或额外步后通知、无执行移动的其它事件/公共事件；所有宿主调用正常。'],
 {'input':'上述失败上水后的同图201保游泳传送，观察转移正常返回。','reference':'玩家到(10,10)，surfing仍真，底座仍(6,5)；显示选择仍读旧底座，不自动跟玩家新位置。','formal':'按WP59残留重置一句会预期底座已清、显示跟随玩家。','evidence':'DERIVED_VECTOR; NOT_EXECUTED；只断言状态和显示输入，不声称可见像素'},
 '成功上水跳跃完成，满足玩家步后通知三门时清底座；成功上岸且结束标记真才额外取消载具/重置遭遇/音乐并清标记。',
 '取消游泳true可清surfing/diving但仍不清临时底座；用人为已有ending_surf=true输入时，仅转移不能保证解除解释器等待。后者只作条件读者事实，不宣称默认流程必软锁。',
 '独立实现可能在每次传送额外清临时量，掩盖失败上水残留，并错误解除结束冲浪等待；状态与显示输入、继续时机可能与R不同。',
 ['全部131文件检索两个字段、底座/基点、残留/中断、载具取消/取消游泳。','WP12§5.2和WP61§3.2只给步后门；WP11显式/边缘入口无临时量清理。测试MV05/WT19只正常收尾，不能证明转移重置。','源端全脚本检索：底座清空只在field 743，结束标志清假为临时状态初始化与field 749；转移、玩家moveto覆写、载具类型设置、同图显示重建均未清。','正常上岸后可能后续步后通知清理，所以反例明确无完成步通知；不把所有转移都说成一定永远残留。'],
 '将WP59保证更正为入口/消费者分层，明确传送不提供两临时量的独立清理保证；WP11/12引用统一；补失败上水→同图保游泳转移及正常步后清理对照。固定异常事实与未来是否主动清理的政策分开。',
 ['静态：分别说明surfing/diving、底座和结束标志，不把载具取消等同全部临时状态重置。','静态：给出无步通知转移返回的观察点与后续步后门，不能声称永久卡死或默认Demo可达。','静态向量：上述(5,5)失败跳→(10,10)转移保底座；对照成功完成步清底座；标NOT_EXECUTED。','运行：真实可视位置/继续时机需宿主地图及资源；不要求本轮补造运行证据。'],[2,3,7]))

F.append(finding('GR4-M03-003','事件命令116的消去记录写入及让出规则未承接，三入口对照含混','partial_missing_consumer_contract',
 [src('commands','11–35,502–509','分派116：正事件ID先安全消去再登记；即使缺实例仍登记；本条索引+1、false让出。'),src('event','46–49','普通erase只改实例/刷新。'),src('interpreter','84–135,292–300','false中断本轮；记录式辅助另有事件存在门。'),src('metadata','154–168','登记取当前地图，不检查实例存在。')],
 [spec('im','116行 L37','只描述当前事件被删除和刷新，没有控制结果/局部记录门。'),spec('wp13','§3.3 L50','辅助有存在门后，将一般实例消去/116并列为不能自动视为同一记录操作。'),spec('tests','GR3-MR12 L490','输入将普通实例消去/116并列，预期只有普通实例不登记，没有116明确输出。'),spec('wp11','§6.2 L120','记录式入口概要引用WP13，不补116差别。')],
 '三个入口有不同合同：普通实例消去不记录；记录式脚本辅助只在当前事件存在时消去并记录；命令116只以事件ID>0为登记门，缺实例可安全跳过消去但仍登记当前图/ID真。116无论ID是否正都推进一项并停止本轮，后条待下一解释器更新机会。',
 '记录式辅助与普通实例的区别已覆盖，但116仅一行粗述，并与一般实例消去在正文/向量中并列；未明确其正ID登记、缺实例登记以及推进让出。',
 '这不是断言规格逐字写了“116绝不登记”；问题是正式三入口对照无法独立推导116的真实生产端和继续时机。',
 ['当前图B、局部记录对象存在，记录表空；解释器绑定事件ID7；合法命令列表中116后还有一条可观察全局开关命令；无其它写入。','正常例B中有事件7；边界例只改为B中没有事件7，解释器ID仍正。'],
 {'input':'边界例在一次解释器更新机会执行116。','reference':'实例消去安全跳过，但(B,7)消去记录为真；索引指向后条且本次不执行后条开关。','formal_gap':'若套记录式辅助缺事件不登记或普通实例不登记，将得到空记录；矩阵没有后条延后判据。','evidence':'DERIVED_VECTOR; NOT_EXECUTED'},
 'B中事件7存在：消去/刷新实例，登记(B,7)真，然后推进一项并本轮停止。与直接实例消去不登记作对照。',
 'ID0：不消去、不登记，仍推进/停止本轮。正ID缺实例：仍登记；局部记录对象为空时安全跳过登记。不借此承诺正常读档还原旧表，进入通知先清记录仍成立。',
 '独立事件兼容实现可能漏记录、把缺实例门套错，或立即连跑116后的全局命令；影响局部状态和当次更新顺序。',
 ['全131文件检索116/删除事件/消去记录/erasedEvents/pbEraseThisEvent及消去-登记别名。','只有WP13矩阵116、WP13§3.3、WP11§6.2和GR3-MR12相关。另116为战斗评分数值和调试目录E116，不是事件命令。','逐读上述及恢复端MR01–13：说明正常读档清表和辅助恢复，不能代替116生产端。','源端command_116仅一处定义且直接主分派可达；addErasedEvent无实例门；Game_Event.erase和脚本辅助的门分别追踪。'],
 '明确三入口表，修116矩阵的状态/缺事件/推进列，拆分GR3-MR12中的普通实例和116预期，并补正ID缺实例/ID0反向向量；保留读档先清表及历史CLOSED身份。',
 ['静态：三入口分别写是否登记及门；116正ID缺实例仍登记。','静态：116索引推进一项并停止本轮，下一更新才尝试后条；不把返回false写成业务失败。','静态向量：有实例、缺实例、ID0；局部记录为空可单独限定；后条开关作观察点，全部NOT_EXECUTED。','历史：GR3-M03-004已关闭记录不改；按新增116消费者审查范围登记new_scope_same_root，不给旧全项重新签名。'],[9,10,24],history='GR3-M03-004',relation='new_scope_same_root'))
write('findings.json',{'schema_version':'1.0','findings':F})

# Per-formal-file bounded reverse coverage; include all owned body/appendix/test files.
coverage=[]
for key in SPEC:
    rel=FORM+SPEC[key]
    relevant=[c for c in CAPS if any(a['path']==rel for a in c['spec_anchors'])]
    refs=[]
    for c in relevant:
        for a in c['source_anchors']:
            if a not in refs:refs.append(a)
    # Correct shared projections are supporting evidence, not unsupported assertions.
    assertion_owners={
      'GR4-M03-001':['wp12','mr','tests'],
      'GR4-M03-002':['wp59','tests'],
      'GR4-M03-003':['wp13','im','tests'],
    }
    related=[fid for fid, keys in assertion_owners.items() if key in keys]
    checked=[a['lines_or_symbol'] for c in relevant for a in c['spec_anchors'] if a['path']==rel]
    if key=='scope':checked=['§2–4：缺地图/Demo/素材、静态案例与运行证据分层；历史层不作为本轮完成度']
    coverage.append({'path':rel,'specification_baseline':B,'contracts_checked':list(dict.fromkeys(checked)),
      'source_anchors':refs,'status':'partial' if related else ('supported' if checked else 'not_reviewed'),
      'support_evidence':{'kind':['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR'] if refs else ['SPEC_STATIC'],
        'capabilities':[c['capability_id'] for c in relevant], 'meaning':'仅所列条款/样本supported_static；不是整文件PASS或已运行'},
      'dependencies':list(dict.fromkeys(c['primary_owner'] for c in relevant))+['共享来源身份/readiness见../../baseline.json'],
      'unsupported_assertions':[{'finding_id':fid,'kind':'contradiction' if fid=='GR4-M03-002' and key=='wp59' else 'missing_or_ambiguous_contract_or_vector','details':'参见finding同ID的current_spec_behavior与gap；不能由此推本文件其它条款错误。'} for fid in related],
      'not_checked':['文件其它断言/向量未获本轮逐项源支持；仅全文浏览或搜索不计逐项审查。',
        '源端具体未审段见source-scope.json；该文件跨域内容归其owner。'],
      'read_extent':'十份主责正文/附表已阅读其正文；语义对照仅contracts_checked' if key in ['wp11','wp12','wp13','im','mr','wp14','wp59','fish','berry','wp61'] else '指定章节/命中上下文/指定向量定点读取'})
extra_specs=['README.md','test-catalog/README.md','generic-kernel/wp02-rule-configuration-and-data-variants.md',
 'generic-kernel/wp03-content-identity-and-schema.md','generic-kernel/wp04-pbs-lifecycle.md','generic-kernel/wp05-events-extensions-plugins.md',
 'generic-kernel/wp06-time-random-steps-stats.md','generic-kernel/wp06-stats-directory.md',
 'creature-rpg/wp36-wild-encounters-and-modifiers.md','creature-rpg/wp28-item-use-and-training.md',
 'pokemon-rules/wp53-safari-and-bug-catching-contest.md','user-interface/wp17-messages-windows-input.md',
 'user-interface/wp63-pokegear-map-music-and-phone.md','demo-dx/wp73-b-world-editors.md','demo-dx/wp77-demo-evidence-and-capability-coverage.md']
for path in extra_specs:
    coverage.append({'path':FORM+path,'specification_baseline':B,'contracts_checked':[], 'source_anchors':[],
      'status':'not_reviewed','support_evidence':'盘点/别名反证搜索或调用边界导航，不构成本轮该文件独立语义审查。',
      'dependencies':['由对应域审查；M03只使用capabilities中明确交界前提'], 'unsupported_assertions':[],
      'not_checked':['该文件主责合同及向量未逐项源对照。']})
write('spec-coverage.json',coverage)

# The old formal acceptance is navigation only; every result below uses the new bounded read.
accept=json.loads((ROOT/'review/remediation-third-20261012-prepare/registration/U02-formal-acceptance.json').read_text())
receipt_path='review/remediation-third-20261012-prepare/U02/actual-integration/independent-review/attempt-01/per-id-verdicts.json'
reg=[]
for old, cn, checks, limits in [
 ('GR3-M03-001',4,['镜头速度1–6、每轴时长与双轴结束','SnapEdges普通/小地图','203等待与包装0/非0、居中整数/浮点','商店共用/背包卖出两分支'], '未穷尽在途卷动覆写或完整UI；画面未执行'),
 ('GR3-M03-002',14,['未驻留建立vs驻留复用','重复临时查询、种子/暂存而不置传送请求','非地牢反向门','构造/生成/事件及仅玩家失败阶段'], '奇数构造引入模块、全生成表未重读；不核宿主空抽样精确消费'),
 ('GR3-M03-003',23,['108/408严格全文/空数组门','写A→结束→请求重启；已真/长度门/页变化','正常与mini系统更新vs末端输入','失联上下文不等于命令终止'], '真实事件页/同轮UI和输入宿主未执行'),
 ('GR3-M03-004',24,['两读档分支进入清记录→图更新→辅助','同ID实际重建离开与复用不离开','条件异图真through、假保持、缺事件异常','实例状态与记录状态区分、前缀无回滚'], '原恢复端核心支持；新读到命令116生产端缺口见GR4-M03-003，未修改旧CLOSED'),
]:
    c=next(c for c in CAPS if c['capability_id'].endswith(f'{cn:03}'))
    reg.append({'id':old,'historical_status':'CLOSED (preserved; shared delivery baseline)',
      'current_file_anchors':c['spec_anchors'],'source_anchors':c['source_anchors'],
      'old_acceptance_fixed_reference':{'accepted_actual':accept['accepted_actual'], 'independent_review_commit':'3a707500031bf164ac7fdfb74f3a2cfad128bf28',
        'path':receipt_path,'selector':'per_id[id='+old+']','git_blob':'b6a852cb93b069ae7f479cc7e10e8ba79fbaf5bd','old_verdict':'PASS',
        'registration_path':'review/remediation-third-20261012-prepare/registration/U02-formal-acceptance.json'},
      'actually_checked_criteria_and_consumers':checks,
      'result':'supported_static_in_bounded_recheck','limits':limits,'signature_transfer':False,'behavior_execution':'NOT_EXECUTED',
      'new_scope_finding':'GR4-M03-003' if old.endswith('004') else None})
write('regression.json',reg)

# Inventory all owned source families, related call sites, relevant PBS including backups,
# and translation files. Line ranges express semantic reads, not whole-file passes.
read_ranges={
 'map':'45–83,140–474,497–565','factory':'1–506','character':'237–307,348–403,427–565,660–747,767–799,830–999',
 'event':'1–302','player':'1–124,129–207,223–390,420–609','common':'1–56','follower':'1–215','followers':'1–294',
 'system':'271–287','screen':'66–70 (weather检索上下文)','temp':'21–22,67 (字段全仓读写检索)',
 'scene':'1–104,119–219','start':'63–104','interpreter':'1–220,286–337','commands':'11–40,128–139,369–390,502–524,716–802,849–878',
 'world':'1–190,224–278；入口符号目录检索','metadata':'123–183','time':'1–224','field':'1–91,319–468,685–790,837–978',
 'fish':'1–110','berry':'1–233,244–470','dungeon':'75–219,280–348,404–555,942–1107',
 'weather':'1–18,64–98,178–243','transition':'80–138','surf_sprite':'44–84','global_sprite':'36–52 (类型消费检索上下文)',
 'items':'49–57,276–318','settings':'17,72–124 (相关配置检索上下文)','mapdata':'1–116','dungeondata':'1–135','berrydata':'1–45',
 'utilities':'524–540','messages':'26–53','mart':'236–248,299–322,345–366',
 'PBS/map_connections.txt':'1–40','PBS/dungeon_parameters.txt':'1–30','PBS/berry_plants.txt':'3–6,28–31,43–56',
 'PBS/map_metadata.txt':'Weather/DiveMap及[051]命中（字段检索，未读全表）'}
read_ranges={FILES.get(k,k):v for k,v in read_ranges.items()}
tracked=subprocess.check_output(['git','-C',str(REF),'ls-files'],text=True).splitlines()
discovery=r'PokemonMapFactory|MapFactoryHelper|can_map_transfer_with_follower|can_ride_vehicle_with_follower|on_enter_map|on_leave_map|on_game_map_setup|on_step_taken|on_player_step_taken|pbStartOver|pbSetEscapePoint|pbEraseEscapePoint|HiddenMoveHandlers|pbFishing|BerryPlant|DungeonParameters|DungeonTileset|move_random_range|surf_base_coords|ending_surf'
res=subprocess.run(['rg','-l',discovery,str(REF/'Data/Scripts')],text=True,capture_output=True)
xrefs={str(Path(x).relative_to(REF)) for x in res.stdout.splitlines()}
scope=[]
for path in tracked:
    direct=(path.startswith(S+'004_Game classes/') or path.startswith(S+'012_Overworld/') or
      path in [FILES[k] for k in ['scene','start','interpreter','commands','settings','mapdata','dungeondata','berrydata']] or
      any(t in path for t in ['011_TerrainTag.rb','012_Weather.rb','019_DungeonTileset.rb']))
    pbs=(path.startswith('PBS/') and Path(path).name in ['map_connections.txt','map_metadata.txt','metadata.txt','town_map.txt','dungeon_parameters.txt','dungeon_tilesets.txt','berry_plants.txt','items.txt','moves.txt','abilities.txt','encounters.txt'])
    media=(path.startswith('Text_english_core/') or path in ['Data/Scripts.rxdata','Data/messages_core.dat','mkxp.json'])
    shared_visual=(path.startswith(S+'006_Map renderer/') or path.startswith(S+'009_Scenes/') or path.startswith(S+'005_Sprites/'))
    if not(direct or pbs or media or shared_visual or path in xrefs or path in read_ranges):continue
    scope.append({'path':path,'reference_commit':R,'group':'primary_world' if direct else ('configuration_or_data' if pbs else 'translation_or_binary' if media else 'shared_visual_M10' if shared_visual else 'caller_or_cross_domain'),
      'review_state':'read_semantically' if path in read_ranges else ('not_reviewed' if path in ['Data/Scripts.rxdata','Data/messages_core.dat','mkxp.json'] else 'inventoried_only'),
      'read_loci':read_ranges.get(path,[]),
      'limits':'仅列出范围的语义阅读；文件其它内容不视为通过' if path in read_ranges else '本轮仅来源目录/符号命中盘点，未作此文件行为结论',
      'material_availability':'AVAILABLE_NOT_PARSED_OR_EXECUTED' if path in ['Data/Scripts.rxdata','Data/messages_core.dat'] else 'AVAILABLE_TEXT'})
write('source-scope.json',{'schema_version':'1.0','source_baseline':R,'reference_root':str(REF),
 'inventory_method':'固定参考tracked路径盘点；004/012世界族、003入口、010定义、全部本域PBS及Gen备份、18翻译、M10视觉交界；再全312脚本按入口/状态/通知反向检索。隐式eval、外部插件与缺失地图不能据此枚举。',
 'discovery_pattern':discovery,'tracked_count_shared_baseline':432,'entries':scope,
 'availability_absences_from_shared_baseline':['真实Data/Map*.rxdata及完整Demo数据库','Graphics/Audio','已成立的游戏宿主运行'],
 'not_executed':['未解析Scripts.rxdata/messages_core.dat','未编译PBS、运行地牢或游戏','未运行历史脚本、模型或行为测试'],
 'counts':{s:sum(x['review_state']==s for x in scope) for s in ['read_semantically','inventoried_only','not_reviewed']}})
formal_paths=sorted(str(p.relative_to(ROOT)) for p in (ROOT/FORM).rglob('*.md'))
write('formal-inventory.json',{'baseline':B,'count':len(formal_paths),'all_formal_paths':formal_paths,
 'scope_entries':[x['path'] for x in coverage], 'negative_search_scope':'所有131份；全文别名搜索不等于全文语义阅读'})
write('execution.json',{'actual_executions':[], 'not_executed':[
 {'kind':'EXECUTED_REFERENCE','status':'NOT_EXECUTED','reason':'未加载/执行任何参考Ruby、PBS编译、地牢生成或二进制。'},
 {'kind':'EXECUTED_MODEL','status':'NOT_EXECUTED','reason':'向量为静态推导，没有仿制模拟器。'},
 {'kind':'EXECUTED_HOST_OR_DEMO','status':'NOT_EXECUTED','reason':'共享readiness无地图/媒体/完整Demo，未成立游戏宿主。'}],
 'static_work':'rg/nl/sed/git show/Python读取和生成审查JSON只用于SOURCE_STATIC/SPEC_STATIC及文件工具验证，非行为执行。',
 'model_request':{'requested_from_task':'gpt-6-astra / ultra / default / Fast禁用','actual_echo':'UNVERIFIED','config_changed':False,'external_model_cli_executed':False}})
print(json.dumps({'capabilities':len(CAPS),'findings':[f['id'] for f in F], 'spec_files':len(coverage),'source_inventory':len(scope),'formal_files':len(formal_paths)},ensure_ascii=False))
