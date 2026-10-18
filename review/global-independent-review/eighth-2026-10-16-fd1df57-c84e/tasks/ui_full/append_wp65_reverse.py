import json,datetime
from pathlib import Path
p=Path(__file__).parent;o=json.loads((p/'reverse-mapping.json').read_text());rs=[]
main='wp65-title-load-options-pause-and-pc.md'
def group(file,clause,units,claims,status='SUPPORTED_LOCAL_SOURCE_STATIC'):
 for a in claims:
  rs.append(dict(id=f'UI65-C{len(rs)+1:03}',formal={'file':file,'clause':clause},assertion=a,source_units=[f'UI65-U{i:03}' for i in units],premise='固定默认B8/R、无插件并发；正常具名基础依赖，仅静态行为；异常/未证范围按每断言限定。',status=status,execution='NOT_EXECUTED'))
group(main,'§1–2范围/术语',[12,15,18],[
'导航只规定入口可见与拒绝门。','内容领域规则由相应主规格保留。','注册数量不等于可见数量。','可见集合先排序再评估条件。','order缺省取登记次序。','动态name在构建集合时求值。','界面预览是第一层状态。','系统选项内存是第二层状态。','磁盘写入是第三层状态。','离开选项不推出落盘。','子屏幕返回与退出整个菜单不同。','可见条件不推出执行资格。','暂停下标在临时字段。','快捷三元游标在bag持久字段。','PC主循环每次默认0。','玩家PC子循环保持下标。','储存PC子循环保持下标。'])
group(main,'§3.1启动生产顺序',[22,23],[
'核心默认消息文件存在才先载默认消息。','DEBUG且非打包且PROMPT_TO_COMPILE才询问编译。','编译确认真写full_compile。','插件加载先于Compiler.main。','Compiler.main先于Game.initialize。','Game.initialize先于set_up_system。','装配先于标题入口。','画面缩放在boot数据装配后应用。','语言配置空不载语言。','候选至少2且读后数据空才首启选择。','已有正确WP08空性门保留。','DEBUG标题入口直接Load。','普通标题入口有splash/title。'])
group(main,'§3.1穷尽boot装配二分',[23,24,25],[
'现文有文件等同boot加载遗漏成功读后空数据默认分支。'],status='KNOWN_ROOT_REQUIRED_GR8-KER-002_UI65_LINE27_ONLY')
group(main,'§3.1开场/标题/主循环',[1,22],[
'默认splash两张按顺序。','单图淡入目标0.4秒。','停留最多2秒。','淡出目标0.4秒。','无输入名义总2.8秒。','USE提前仅停留已挂回调窗口。','淡入不挂USE跳过。','淡出不挂USE跳过。','标题start名义40/20秒闪烁。','标题BGM在准备完成后请求。','离开先清update回调。','离开先清confirm回调。','随机物种叫声请求先于1秒等待。','等待结束再淡出两标题图。','淡图目标0.4秒。','并行请求BGM按1秒停。','不保证叫声全长听感。','隐藏删除组合也走离开链。','scene.main反复直到nil。','Hangup调紧急保存后原样raise仅在其正常返回时。'])
group(main,'§3.2读档与跳过',[3,4,24,25],[
'存在文件先read/adapt。','成功读后做全部注册valid?。','valid数据继续使用。','invalid当前路径有.bak先提示。','提示后递归读相邻.bak。','invalid无备份转删除提示。','无文件初始数据空。','读取阶段异常不强制接备份UI。','DEBUG真为跳过必要门。','非打包为跳过必要门。','SKIP_CONTINUE_SCREEN真为跳过必要门。','三门全真才跳过。','跳过空数据新游戏。','跳过非空数据load。','默认skipfalse。','旧可读序列空与无文件是不同前序。','后续17值空数据仍invalid，不越过删除链。'])
group(main,'§3.2命令可见/去向',[4],[
'非空才Continue。','Continue为首项。','非空且gift解锁才MysteryGift。','NewGame总可见。','Options总可见。','语言候选至少2才Language。','默认空语言表不出现Language。','DEBUG才Debug。','Quit总可见。','选择循环无BACK出口。','确认返回当前下标。','非Quit先决定音。','Continue先关闭屏幕。','Continue随后load已读对象。','NewGame先关闭。','NewGame随后start_new。','Gift正常返回留菜单循环。','Options传入load_screen=true。','Options正常返回留循环。','Debug正常返回留循环。','Quit关闭音先于关闭屏幕。','Quit最后scene=nil。','其它下标蜂鸣。'])
group(main,'§3.2继续预览/§3.4附表',[2],[
'大面板显示badge_count。','大面板显示seen_count。','大面板显示player.name。','男性名字蓝色。','女性名字红色。','其它性别默认色。','时间至少1小时显示h+m。','不足1小时只m。','地图命名服务先于存档名PN展开。','全局名已消耗PN不能被面板覆盖。','主Alice例需全局player为空。','共享材料查询成功后可能保展开结果。','预览后新游戏不自动重载命名材料。','查询之前失败不套成功例。','查询之后UI失败不回滚展开。','没有自动内容保存。','继续玩家图集missing具名抛错。','玩家元数据不存在不强制构造预览。','party图标两列。','非Continue只命令窄面板。','合法128x128图集首行四32格。','继续/命名行走周期0.5秒。','t0行走frame0。','t0.20行走frame1。','t0.40行走frame3。','t0.50行走frame0。','盒名128x32单行四格。','盒名周期0.4秒。','t0盒frame0。','t0.20盒frame2。','t0.40盒frame0。','t0.50盒frame1。','绝对uptime相位不因重开归零。','个体命名使用PokemonIcon，不套walking。','命名资源失败不能泛用Continue具名错误。'])
group(main,'§3.3删除',[3,24],[
'无存档提示No save file。','无存档结束回标题。','第一次严肃确认拒绝不删。','第一次同意先不可恢复警告。','第二次严肃确认拒绝不删。','第二次同意先正在删除提示。','提示后才执行delete。','删除正常提示成功。','SystemCallError提示无法全部删除。','部分失败不重试。','部分失败不回滚。','正常结束回标题。','invalid无备份先损坏/不兼容提示。','invalid删除确认拒绝exit。','invalid同意先删除。','删除正常返回后重建Game_System。','随后重建PokemonSystem。','最后返回空数据进入无Continue菜单。'])
group(main,'§4.1共享保存',[5],[
'信息窗显示当前map名。','显示玩家名性别色。','显示游戏时间。','显示badge_count。','has_pokedex才附owned/seen。','普通保存确认先行。','拒绝播放选择音。','拒绝返回false。','No无副作用合理限该分支，不撤销确认前材料更改。','覆盖门exists?且begun_new_game。','覆盖前三警告连续。','覆盖严肃确认拒绝false。','接受清begun_new_game在save之前。','save前播放选择音。','save成功消息正常返回才true。','save失败消息后false。','确认前更改不回滚。','覆盖确认前更改不回滚。','save失败更改不回滚。','底层持久部分提交由WP09。'])
group(main,'§4.2紧急保存',[6,22,23],[
'先换出scene为nil。','先脚本过久提示。','无player直接return。','存在旧档先按字节复制.bak。','备份早于新保存。','保存真提示已保存。','保存真再提示旧档已备份。','保存假提示失败。','恢复oldscene是正常末尾。','早退/异常不按末尾恢复保证。'])
group(main,'§4.3暂停与退出/事件交接',[5,13],[
'暂停保存先hide。','保存true关闭暂停。','保存false刷新并重显。','退出先hide再退出确认。','退出拒绝重显。','退出同意调用共享保存。','退出忽略保存布尔。','保存拒绝仍可退出。','保存false仍可退出。','保存正常返回后end菜单。','再scene=nil。','事件脚本直接取保存布尔，不自带暂停包装。','解释器保存命令忽略布尔继续true为WI有限外接，非本地source全文。'])
# known interpreter command source remains finite received, not own full.
rs[-1]['status']='BOUNDED_WI_MESSAGE_RECEPTION_EVENT_COMMAND_OWNER'
group(main,'§5.1选项类型/循环',[7,8],[
'枚举有序候选。','枚举左端不循环。','枚举右端不循环。','编号整数域。','编号最高后回最低。','编号最低前回最高。','编号显示Type当前/总数。','滑杆按步长。','滑杆最低钳限。','滑杆最高钳限。','可见选项按有效order。','同序无明确次级键，不保证稳定。','最后Close。','总行数可见数+1。','选择变化调用on_select。','说明可静态本地化。','说明Proc按当前状态求值。','左右新值即时写。','BACK任意行关闭。','USE只有Close关闭。','取消不还原改值。','结束再逐项写所有可见项。','未改项也应用。','结束后地图刷新。','中间异常不提供整组选项回滚。'])
group(main,'§5.2默认选项目录',[7,9,10,11],[
'Music域0..100。','Music步长5。','Music默认80。','Music写BGM字段。','load_screen不BGM预览。','无playingBGM不预览。','其它pause/resume当前BGM。','SE域0..100。','SE步5。','SE默认100。','SE先写字段。','SE同值不预览。','有BGS新值先改当前记录volume。','再恢复请求按SE再次缩放取整。','同引用记忆记录同步变。','SE100/记录80改50得到记录50。','该恢复请求音量25。','getPlayingBGS副本改动不改当前/记忆。','cursorSE在变更后请求。','TextSpeed四候选。','默认Mid=1。','写字段与消息速度。','说明重显一次。','说明逐字开启。','BattleEffects On/Off默认On0。','BattleEffects写battlescene。','BattleStyle Switch/Set默认Switch0。','BattleStyle写battlestyle。','Movement只有跑鞋可见。','Movement Walking/Running默认0。','Movement写runstyle。','SendToBoxes由NEW_CAPTURE配置可见。','默认世代8该配置真。','Send Manual/Automatic默认0。','GiveNicknames Give/Dont默认0。','Speech皮肤编号1..N。','默认21项。','存0显示1/21。','Speech即时换说明窗。','Menu皮肤编号1..N。','默认28项。','Menu即时换选项窗。','TextEntry Cursor/Keyboard默认0。','Screen五档。','Screen默认floor(scale*2)-1。','scale1默认M1。','Screen getter仅min4。','负存值不被钳0。','首次请求512x384依默认Settings。','同会话不重复初始化。','Screen0缩0.5。','Screen1缩1。','Screen2缩1.5。','Screen3缩2。','这四档关fullscreen并center。','Screen4请求fullscreen。','负档请求fullscreen。','启动7按4请求但仍存7。','Options读7为4并退出写4。','实际宿主尺寸/DPI未证。'])
group(main,'§5.3–5.4语言/持久',[4,7,8,23],[
'语言不进入options注册。','装配数据空至少2时选语言。','载入Language至少2可见。','默认LANGUAGES空。','UI语言索引与训练家领域语言独立。','训练家/Owner默认构造规则由WP24/18，不在UI泛化。','Load语言有Continue时直写。','直写整体PokemonSystem。','之前LoadOptions其它改值连带落盘。','无Continue不直写。','装配修改不单独落盘。','单关闭Options不落盘。','Options值随正常保存可持久。','语言首次启动值随首次保存。','Pause游标临时不持久。','Ready游标在bag持久。'])
group(main,'§6.1入口与循环',[12,14],[
'常规地图更新message显示提前return。','提前return不生产新请求。','提前return不消费已有请求。','解释器运行不产新请求。','forced movement不产新请求。','USE产互动请求。','ACTION需菜单未禁用。','ACTION需玩家静止。','SPECIAL只需玩家静止。','菜单禁用不门SPECIAL。','F9仅DEBUG产请求。','静止时消费一个。','消费Pause优先Debug。','Debug优先Ready。','Ready优先Interact。','生产守卫不无条件门已有请求。','miniupdate不检测输入。','miniupdate不消费请求。','已有Ready经历mini仍保留。','call_menu先in_menu真。','玩家整姿再地图更新再开菜单。','无player不开菜单。','菜单正常返回in_menu假。','本次集合每次打开构造。','打开读上次临时下标。','BACK/ACTION取消−1。','USE写上次下标。','effect真退出。','effect假继续同列表。','普通子屏幕取消回父菜单。','hiddenmove/item/fly特定结果转交离开。'])
group(main,'§6.2逐项注册',[13],[
'Dex10需持有Dex。','Dex10需accessible>0。','单Dex先设当前。','多Dex开菜单。','当前地区配置走直接画面。','Dex返回false。','Party20需成员>0。','Party无hiddenmove返回false。','Party有hiddenmove关闭并清in_menu再执行。','Bag30不在BugContest。','Bag有item关闭并清in_menu再执行。','Gear40需has_pokegear。','Map40需无pokegear。','Map40另需TOWNMAP。','Gear/Map互斥。','Trainer50总见。','Trainer显示name动态。','Save60需system。','Save60未save_disabled。','Save60非Safari。','Save60非BugContest。','Options70总见。','Options游戏中标记false。','Debug80需DEBUG。','Quit90总见。','SafariQuit60独立Safari条件。','BugQuit60独立Bug条件。','两个会话退出可同时可见。','00可见100。','10可见010。','01可见001。','11可见011。','同order相对顺序未承诺。','会话结算领域由WP53。','Pause游标不随保存。'])
for r in rs[-9:]:
 if any(s in r['assertion'] for s in ['SafariQuit','BugQuit','会话退出','00可见','10可见','01可见','11可见','会话结算']):r['status']='BOUNDED_FACILITY_INTERFACE_RECEIVED'
group(main,'§7.1普通PC',[15,16],[
'PCopen音先开机消息。','可见集合按order/条件。','PC主默认下标每次0。','子菜单返回不记主choice。','BACK关闭菜单音退出。','effecttrue退出。','正常末尾PCclose。','Storage10总见。','见创建者用创建者PC。','未见用SomeonePC。','创建者取全局元数据。','Organize模式0。','Withdraw满队拒绝留子循环。','Withdraw通过模式1。','Deposit非蛋HP>0计数。','count<=1拒绝留子循环。','Deposit通过模式2。','子循环保command。','BACK/SeeYa退出false。','PlayerPC20总见。','PlayerPC名当前玩家。','净化30需seenPurifyChamber。','该seen写在打开前为UILC-U020。','Hall40需hallOfFameLastNumber>0。','登记递增编号为UILC-U011/U014。','HallPC浏览不增编号。','Logoff100总见并true。','子调用false回PC主。','真实地图事件caller未证。'])
for r in rs[-8:]:
 if any(x in r['assertion'] for x in ['净化','Hall','登记递增']):r['source_units']+=['UILC-U011','UILC-U014','UILC-U020']
group(main,'§7.2玩家PC/物品/信箱',[16,17],[
'玩家PCopen消息。','子菜单ItemStorage/Mailbox/Close。','子菜单保持下标。','BACK/Close退出并PCclose。','物品Withdraw缺对象先创建。','Withdraw空拒开。','Withdraw非空打开。','Deposit直接开。','Toss缺对象先建。','Toss空拒开。','Exit回上级。','信箱nil拒开。','信箱空拒开。','非空寄件人列表+Cancel。','Read展示所选。','MoveToBag先将丢消息确认。','bag.add真后成功消息再delete。','bag.add假满包且mail不删。','中间消息失败保加物品前缀，不补全原子。','Give开PartyGiveMailScreen。','内层Cancel回列表。','外列表BACK/Cancel退出。'])
group(main,'§8.1候选与状态',[18,14],[
'Ready请求只常规update消费。','message显示不消费。','miniupdate不消费。','静止且优先轮到才清Ready标记。','整姿后入口。','固定16个hiddenmoves。','每个非蛋且hasMove成员贡献候选。','还需CanUseHiddenMove真。','同招多成员各贡献。','登记items只当前bag.has。','登记但不持有不出现。','两侧空只提示。','非空in_menu真。','再map.update后开Ready。'])
group(main,'§8.2显示/游标',[18,19],[
'招式左列带成员图标。','item右列带item图标。','重要item不显示qty。','qty>99显示>99。','其它xN。','两侧独立名称字母序。','选中高亮外凸。','读bag三元游标。','默认0,0,1。','非空侧越界收末项。','当前侧空换侧。','LEFT/RIGHT只切非空。','BACK关闭音−1。','USE给侧别/下标。','结束保游标在bag。'])
group(main,'§8.3–8.4执行/持久边界',[19],[
'FLY先隐藏开地图。','FLY取消重显继续。','FLY成功先记录目的地。','再in_menu假/执行/关闭。','其它move先confirm。','拒绝重显。','接受清in_menu再执行关闭。','Item先preconfirm。','preconfirm拒绝不清in_menu。','接受清in_menu后use。','use真关闭。','use假恢复in_menu真并重显。','数量不变不等于失败。','COINCASE真不消耗仍关闭。','消耗另由WP28包装。','Ready正常结束清in_menu。','入选资格不推执行成功。','bag游标随保存静态路径。','旧迁移填充字段为WP10外接口。','其它游标写入者未穷尽。'])
group(main,'§9–12保留/目录',[1,3,4,8,14,16,18],[
'默认普通构建有开场。','默认skipfalse。','默认语言表空。','NEW_CAPTURE配置变体影响Send可见。','事件字段可见驱动不证明demo实际。','真实媒体存在性未证。','宿主缩放行为未证。','PC真实事件调用未证。','ACTION/SPECIAL物理映射未运行。','子屏幕异常清理未逐项验证。','参考行为不等于官方预期或未来API。','NV39向量为静态未执行。','WP53前向结算不列继承已批准。','G/U/AX保留边界不由UI补充抹除。'])
ch='wp65-controls-help-appendix.md'
group(ch,'§1–3页面内容/组建',[20],[
'帮助无pause菜单注册。','四页只展示控制文字。','help文字不认证宿主绑定。','页初值1。','page1是help_f1。','page1另help_f8。','page2是help_arrows。','page3是help_usekey。','page3另help_backkey。','page4是help_actionkey。','page4另help_specialkey。','七图分别本地化路径。','背景bg固定身份。','缺译用原身份。','非空译文用译后身份。','译后失败不保证重试原。','标签独立本地化。','图和标签初opacity0。','先freeze再构造背景及全部页。','首页先完成两阶段才transition。','旧页0.5秒淡出。','新页0.5秒淡入。','两阶段总目标1秒。','冻结期不假可见闪烁。','时间单位1/20非固定帧。'])
group(ch,'§4–7退出/输入/保留',[20],[
'maxpage取两页号表max=4。','未末页先页+1。','清确认回调再等待。','完成后重挂。','等待有Input更新不等于回调存在。','末页先snap背景。','再freeze。','viewport置黑。','transition目标8/20=0.4。','再释放snapshot。','再释放scene。','标准BACK回调空表无动作。','稳定页USE前进。','稳定页BACK保持。','同轮BACK+USE先BACK所以保持。','无ACTION分支。','无方向分支。','页号不逆行。','仅页号/透明度等UI状态变化。','实际脚本caller未定位。','无caller不等于不存在。','真实demo可达未证。','媒体存在性未证。','宿主过渡未运行。'])
tc='wp65-trainer-card-appendix.md'
group(tc,'§1–4场景/资源/定位',[21],[
'暂停TrainerCard总见。','正常取消回暂停循环。','三段start→readonlyloop→end。','viewport z99999。','female且bg_f存在才女背景。','其它默认bg。','female且本地化card_f存在才女卡。','其它默认card。','两变体独立。','正面图按player.trainer_type。','装扮编号缺省0。','先尝试类型_N。','解析不存在退基础类型。','x=336−(w−128)/2。','底边y+h=240。','128x256定位336,−16。','128x128定位336,112。','非垂直居中。','trainer z2。','先绘front再淡入。'])
group(tc,'§5–8内容/输入/保留',[21],[
'Name为玩家名。','ID为public_ID不是内部ID。','公开号42格式00042。','Money千分位。','Dexowned/seen。','时间为play_time。','3661秒1h1m。','不足1小时仅分钟。','startTime空当场写Time.now。','Started缩写月/日/年。','已有startTime不重置。','按currentRegion取徽章行。','每地区8枚。','每槽读i+region*8真值。','真槽绘src i*32,region*32。','位置72+i*48,310。','0/3/7真不紧排前三。','只开场一次绘front。','循环不重绘。','BACK唯一退出。','无ACTION/方向分支。','关闭音后退出。','end淡出/disposehash/viewport。','除startTime懒写只读player数据。','短徽章数组不补造额外守卫合同。','素材内容未证。','宿主淡入/声音未运行。','只本场景front，不推整作品无背面。'])
old={x['id'] for x in o['records']};assert not old&{r['id'] for r in rs}
o['records']+=rs;o['manually_authored_assertion_count']=len(o['records']);o['utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();o['scope']='WP17两正文304/WP63全文334/WP65主+两附录全部语义段手工子断言；WP66/67/完整catalog原子分母仍未最终。';(p/'reverse-mapping.json').write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n');print('added',len(rs),'total',len(o['records']))
