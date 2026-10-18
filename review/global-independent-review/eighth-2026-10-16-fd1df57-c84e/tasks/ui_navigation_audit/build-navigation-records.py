from pathlib import Path
import json,hashlib,subprocess,re,datetime
P=Path('/workspace/pokemon-essentials-clean-room');R=Path('/workspace/pokemon-essentials');O=P/'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/ui_navigation_audit'
B8='fd1df570cad987dc3852a3b958f03916e317f7fe'; RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'; NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(name,obj): (O/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
ids=json.loads((O/'identities.json').read_text())['inputs'][:28]; initial_paths={x['path'] for x in ids}
alias={}
for x in ids:
 x['read_status']='FULL_READ';x['read_ranges']=[[1,x['lines']]]
 alias[x['path'].split('/')[-1]]=x['path']
extra_full=['Data/Scripts/014_Pokemon/005_Pokemon_Owner.rb','Data/Scripts/015_Trainers and player/001_Trainer.rb','Data/Scripts/005_Sprites/010_PictureEx.rb','Data/Scripts/002_Save data/004_Game_SaveValues.rb','Data/Scripts/015_Trainers and player/003_Trainer_Sprites.rb','Data/Scripts/010_Data/002_PBS data/014_TrainerType.rb','Data/Scripts/002_BattleSettings.rb','Data/Scripts/016_UI/008_UI_Pokegear.rb','Data/Scripts/016_UI/009_UI_RegionMap.rb','Data/Scripts/018_Alternate battle modes/001_SafariZone.rb','Data/Scripts/018_Alternate battle modes/002_BugContest.rb','Data/Scripts/003_Game processing/005_Event_Handlers.rb','Data/Scripts/010_Data/002_PBS data/016_Metadata.rb']
partial={
'Data/Scripts/007_Objects and windows/005_SpriteWindow_text.rb':[[753,1254]],
'Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb':[[1,115],[420,530]],
'Data/Scripts/013_Items/001_Item_Utilities.rb':[[1,112],[730,800]],
'Data/Scripts/013_Items/002_Item_Effects.rb':[[350,375]],
'Data/Scripts/007_Objects and windows/011_Messages.rb':[[1,65],[230,270]],
'Data/Scripts/003_Game processing/004_Interpreter_Commands.rb':[[1110,1165]],
'Data/Scripts/002_Save data/005_Game_SaveConversions.rb':[[180,250]],
'Data/Scripts/016_UI/005_UI_Party.rb':[[908,958],[1204,1488]],
'Data/Scripts/016_UI/007_UI_Bag.rb':[[458,581]],
'Data/Scripts/016_UI/024_UI_MysteryGift.rb':[[241,330]],
'Data/Scripts/016_UI/023_UI_PurifyChamber.rb':[[1260,1310]],
'Data/Scripts/016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb':[[1,142],[435,493]],
'Data/Scripts/016_UI/025_UI_TextEntry.rb':[[1,179],[371,490],[738,787]],
'Data/Scripts/004_Game classes/004_Game_Map.rb':[[90,112]],
'Data/Scripts/010_Data/002_PBS data/018_MapMetadata.rb':[[112,134]],
'Data/Scripts/001_Technical/003_Intl_Messages.rb':[[590,625],[740,780]],
'Data/Scripts/007_Objects and windows/002_MessageConfig.rb':[[1,166],[492,516]],
'Data/Scripts/004_Game classes/008_Game_Player.rb':[[1,83],[560,600]],
'Data/Scripts/019_Utilities/002_Utilities_Pokemon.rb':[[1,35]],
'Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb':[[203,325]],
'Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb':[[48,78]],
'Data/Scripts/012_Overworld/002_Overworld_Metadata.rb':[[110,140]],
'Data/Scripts/015_Trainers and player/004_Player.rb':[[1,96]],
'Data/Scripts/016_UI/017_UI_PokemonStorage.rb':[[1494,1730]]}
for path in extra_full+list(partial):
 b=subprocess.check_output(['git','-C',str(R),'show',RC+':'+path]);assert (R/path).read_bytes()==b
 mode,typ,blob,_=subprocess.check_output(['git','-C',str(R),'ls-tree',RC,'--',path]).decode().split(maxsplit=3)
 n=len(b.splitlines());rr=[[1,n]] if path in extra_full else [[a,min(z,n)] for a,z in partial[path]]
 ids.append(dict(id=f'R{len(ids)+1:03}',kind='reference',repo=str(R),commit=RC,tree='7589c800b61ba13a13040ed0d686979b80a84fd0',path=path,mode=mode,blob=blob,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),lines=n,disk_equals_fixed_blob=True,read_status='FULL_READ' if path in extra_full else 'PARTIAL_READ_NAMED_UNITS_ONLY',read_ranges=rr,units=[{'line':i,'kind':'definition','name':l.strip()} for i,l in enumerate(b.decode().splitlines(),1) if re.match(r'\s*(?:class|module|def)\s+',l)]))
 alias[path.split('/')[-1]]=path
by_path={x['path']:x for x in ids}
save('identities.json',{'schema':'r8-ui-navigation-identities-v2','B8':B8,'R':RC,'updated_utc':NOW,'initial_frozen_paths_retained':True,'additional_reads_explicit':True,'inputs':ids})
M='deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md'; C='deliverables/final-specification-set/user-interface/wp65-controls-help-appendix.md';T='deliverables/final-specification-set/user-interface/wp65-trainer-card-appendix.md';CAT='deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md'
facts=[]
def loc(file,a,z):
 p=alias.get(file,file);x=by_path[p]
 return {'identity_id':x['id'],'path':p,'line_start':a,'line_end':min(z,x['lines']),'full_file_read':x['read_status']=='FULL_READ'}
def group(key,refs,spec,lines,premise,consumer,assertions,status='SUPPORTED_SOURCE_STATIC'):
 for j,assertion in enumerate(assertions,1):
  facts.append(dict(id=f'UIF-{key}-{j:02}',source=refs,spec={'path':spec,'lines':lines},premise=premise,consumer=consumer,assertion=assertion,status=status,reader='/root/ui_navigation_audit',evidence_level='SOURCE_STATIC',execution='NOT_EXECUTED'))
normal='固定R默认脚本与合法正常依赖，无插件/覆写/并发修改；显示/媒体/宿主最终结果不由静态请求保证。'
group('BOOT',[loc('999_Main.rb',1,60),loc('001_StartGame.rb',1,60)],M,[27,33],normal,'标题入口与Game系统装配',[
'核心消息存在时先请求加载默认消息。','调试、非打包且编译提示配置开启才询问完整编译。','正常启动按插件、编译、游戏初始化、系统装配、标题入口顺序继续。','调试标题入口直接调用载入屏，普通入口调用开场标题。','装配对读取结果是否为空分流启动值初始化与载入；这不是文件存在等价门。','装配先应用画面缩放。','语言配置非空才尝试消息文件装载。','已读数据为空且语言候选至少两项才在装配弹出语言选择。','主场景循环只在场景引用非空时继续。','主循环Hangup路径调用紧急保存后重新抛出；不据此认证宿主重启或退出。'])
group('TITLE',[loc('001_UI_SplashesAndTitleScreen.rb',4,129),loc('002_EventScene.rb',130,204)],M,[29,33],normal,'IntroEventScene→载入/删除屏',[
'默认开场图两张，依序播放。','每张淡入与淡出各8个1/20秒单位。','每张淡入后才记录单调时钟起点，停留到相对2秒。','停留阶段挂接USE跳过，淡入淡出时该回调清空。','无输入两张名义总5.6秒，不保证真实墙钟或渲染帧数。','标题确认提示使用名义40个1/20秒单位的透明度循环。','标题图显示后请求标题BGM。','标题确认与隐藏删除组合键都通过同一离开演出。','离开先清更新/确认回调，再选择随机物种叫声请求。','叫声请求后等名义1秒再令两图淡出0.4秒，同时请求BGM按1秒淡出。','标题离开不保证叫声全长播放。','DOWN/BACK/CTRL同时按住的查询成立可进入删除屏。'])
group('LOADGATE',[loc('013_UI_Load.rb',217,318),loc('001_SaveData.rb',1,82),loc('002_SaveData_Value.rb',208,276)],M,[37,50],normal,'PokemonLoadScreen构造与命令构建',[
'构造时有主存档则读取，无主存档以空数据继续。','校验失败且当前读取路径旁有bak则提示并递归读该备份。','校验失败又无备份时进入删除提示；普通读取异常不自动进入备份分支。','无效存档删除提示拒绝触发语言级exit；不是仅把场景引用置空。','同意无效存档删除后新建Game_System/PokemonSystem，按空数据继续。','隐藏删除屏无主存档只提示后回标题。','隐藏删除屏有主存档须两次严肃确认，任一拒绝均不删除。','删除调用的SystemCallError转失败消息；没有此层重试或回滚。','调试、非打包、跳过配置三门全真才不建载入菜单。','跳过后的新游戏/继续按已读数据空/非空决定。','继续项只在存档数据非空时追加。','神秘礼物项另要求存档玩家解锁标记。','新游戏/选项/退出游戏无附加可见门。','语言项只在候选至少两项时追加。','调试项只在DEBUG为真时追加。'])
group('LOADPANEL',[loc('013_UI_Load.rb',13,212),loc('003_Trainer_Sprites.rb',4,69),loc('008_Game_Player.rb',560,573),loc('011_Messages.rb',245,263),loc('018_MapMetadata.rb',121,125)],M,[47,83],normal,'继续面板→地图命名/行走预览/成员图标',[
'继续项使用大面板，非继续项只显示窄命令面板。','继续面板显示徽章数与已见数。','秒数先取整，小时/分钟取整换算，有小时显示h m，无小时只显示分钟。','名字按男/女/其它颜色分支绘制。','先调用地图命名服务，再以存档训练家名展开仍留的大写玩家名占位。','地图服务全局玩家名可先消费占位，面板不能覆盖已经消费的内容。','共享材料可在进入载入菜单且尚未选择命令时已经改变；开新游戏不自动重新加载该材料。','玩家元数据存在时创建行走图；位图为空触发具名行走图缺失错误。','队伍图标按两列排列。','行走4×4图集取首行四格，周期0.5秒，由绝对单调运行相位计算帧号。','行走预览创建不会把绝对相位重置到0。','选择位置变化可滚动面板和相关图标。','载入选择循环只有USE返回，没有BACK取消分支。'])
group('LOADCOMMAND',[loc('013_UI_Load.rb',281,356),loc('004_Game_SaveValues.rb',19,33),loc('002_SaveData_Value.rb',235,276),loc('024_UI_MysteryGift.rb',241,326)],M,[49,65],normal,'载入命令→Game/Options/语言/神秘礼物',[
'继续关闭载入画面后调用Game.load。','新游戏关闭载入画面后调用Game.start_new。','神秘礼物下载正常返回后留在载入菜单循环。','载入选项以in_load_screen=true打开，正常返回后留循环。','语言命令先关闭画面再选择并加载对应消息文件。','有继续项时语言路径把当前系统选项对象写进存档数据再直接序列化整个数据到主存档。','该直写连同此前在载入选项中改动的字段落盘，不限语言字段。','没有继续项的语言路径不直接写存档。','语言命令结束回pbCallTitle选择的标题入口。','调试菜单正常返回后留在载入循环。','退出游戏关闭画面并把场景引用置空；源码可证场景循环结束，宿主进程是否结束未观察。','退出项之外先请求决定音，退出项请求关闭菜单音。'])
group('SAVE',[loc('014_UI_Save.rb',29,139),loc('001_StartGame.rb',107,126)],M,[87,100],normal,'共享保存→暂停保存/退出保存/事件保存',[
'保存信息窗在普通保存确认之前创建并读取当前地图名。','保存信息窗显示地图/姓名/时间/徽章；图鉴计数只在持图鉴时追加。','普通确认拒绝返回false并请求选择音，不调用Game.save。','有现存主存档且begun_new_game为真才显示覆盖三警告及严肃确认。','覆盖确认拒绝返回false，未进入Game.save。','通过保存确认后在调用Game.save之前清begun_new_game。','Game.save返回true才显示成功并返回true。','Game.save返回false显示失败并返回false。','保存UI不统一回滚确认前或持久层失败前已发生的更改。','脚本直接保存包装透传布尔结果。','暂停保存true后显式关闭菜单，false时刷新重显。','退出确认拒绝仅刷新重显菜单。','退出确认通过后保存返回值被忽略，仍关闭菜单并场景置空。','保存确认前的信息读取可原位改共享地图名，所以拒绝不能作全层无副作用保证。'])
group('EVENTSAVE',[loc('004_Interpreter_Commands.rb',1132,1158),loc('002_Scene_Map.rb',103,115)],M,[100,148],normal,'事件命令351/352/354→请求/保存',[
'事件菜单命令生产菜单请求并推进解释器索引；不经过ACTION输入菜单禁用门。','事件保存命令忽略保存UI布尔结果且自身返回true继续事件。','事件返回标题只生产title_screen_calling请求，由地图更新消费。'])
group('EMERGENCY',[loc('014_UI_Save.rb',1,24)],M,[94,94],normal,'Hangup→紧急保存',[
'紧急保存先保存旧场景引用，再把当前场景置空并提示。','无玩家时在提示后立即返回，未到达末尾恢复旧场景。','有玩家且主存档存在时先按字节复制到bak，再调用Game.save。','成功路径依次提示保存与已备份；即便之前无文件，成功后的备份提示仍存在。','持久层false时给失败消息。','只有到达函数尾部的正常有玩家路径才恢复旧场景；异常没有统一ensure恢复。'])
group('OPTIONFRAME',[loc('015_UI_Options.rb',4,379),loc('006_Event_HandlerCollections.rb',80,133)],M,[106,115],normal,'Options值对象/选择窗口/退出应用',[
'枚举左右到端夹住，不回绕。','编号域以零基存值表示，左右跨两端回绕。','滑杆按步长增减，到端夹住。','可见选项按有效排序值排序后逐项条件筛选；缺省顺序用登记序号。','没有额外同序次级键，不能补同序稳定承诺。','列表末尾总有Close。','初始值从每项getter读入，空值按0显示。','选择位置改变时运行选择效果并更新静态或动态说明。','左右输入设置value_changed后调用该项setter，端点输入也可调用setter。','BACK在任意行关闭；USE只有Close行关闭。','正常关闭先淡出，再对全部可见项调用一次setter，随后清理并更新地图。','修改实时写入选项对象；关闭或BACK不还原。','普通关闭选项本身没有存档写调用。'])
options=[
('Music Volume','Slider0..100 step5','80','无附加门','字段变化后若载入标记真或无playing_bgm则不预览；其余暂停并恢复当前BGM','015_UI_Options.rb',384,399),
('SE Volume','Slider0..100 step5','100','无附加门','只有值变才改；有BGS则改当前登记音量并暂停/恢复，然后光标音','015_UI_Options.rb',401,419),
('Text Speed','Slow/Mid/Fast/Inst','1=Mid','无附加门','值变化写字段与消息速度，并重显当前说明作逐字预览','015_UI_Options.rb',421,438),
('Battle Effects','On/Off','0=On','无附加门','写战斗动画字段，战斗准备读取并可被battle rule覆盖','015_UI_Options.rb',440,448),
('Battle Style','Switch/Set','0=Switch','无附加门','写战斗风格字段，战斗准备读取并可被battle rule覆盖','015_UI_Options.rb',450,458),
('Default Movement','Walking/Running','0=Walking','全局玩家有跑鞋','写runstyle；普通跑步资格通过后和BACK按住作异或决定快慢','015_UI_Options.rb',460,469),
('Send to Boxes','Manual/Automatic','0=Manual','NEW_CAPTURE_CAN_REPLACE_PARTY_MEMBER','写sendtoboxes；准备战斗时按配置读取且forceCatchIntoParty可覆盖2','015_UI_Options.rb',471,480),
('Give Nicknames','Give/Don’t give','0=Give','无附加门','写givenicknames；普通命名入口仅0询问昵称','015_UI_Options.rb',482,490),
('Speech Frame','Number1..21；存值0..20','0=Type1/21','无附加门','写textskin并显式设置消息皮肤缓存，当前说明窗换皮肤','015_UI_Options.rb',492,505),
('Menu Frame','Number1..28；存值0..27','0=Type1/28','无附加门','写frame并显式设置菜单皮肤缓存，当前选项窗换皮肤','015_UI_Options.rb',507,520),
('Text Entry','Cursor/Keyboard','0=Cursor','无附加门','写textinput，后继文字输入包装按1选键盘，其余选屏幕光标','015_UI_Options.rb',522,530),
('Screen Size','S/M/L/XL/Full','floor(scale×2)−1；默认1=M','无附加门','getter只min存值与4、不钳负值；setter值变化才写字段并请求缩放','015_UI_Options.rb',532,544)]
for i,(name,domain,default,gate,effect,file,a,z) in enumerate(options):
 group('OPT'+str(i+1).zfill(2),[loc(file,a,z),loc('015_UI_Options.rb',4,34)],M,[119+i,119+i],normal,'系统选项及对应运行消费者',[name+'的候选/值域为'+domain+'。',name+'新建默认值为'+default+'。',name+'可见条件为'+gate+'。',name+'变更合同：'+effect+'。'])
group('OPTIONCONSUMER',[loc('002_Game_System.rb',44,262),loc('002_MessageConfig.rb',34,113),loc('008_Game_Player.rb',51,62),loc('002_Utilities_Pokemon.rb',8,15),loc('001_Overworld_BattleStarting.rb',209,306),loc('025_UI_TextEntry.rb',754,787)],M,[121,144],normal,'设置→音频/文字/移动/命名/战斗/文字输入',[
'BGS记忆保存当前登记的同一记录，查询播放信息返回克隆。','SE改50时先把当前及同一记忆记录改50，恢复播放请求又乘SE百分比得25，未认证真实听感。','音频/截图都是请求；正常调用返回不授予真实外部成功。','文字速度设置映射0/1/2/3至4/80、2/80、1/80、0秒延迟。','语言索引没有选项注册项；只由装配及载入语言命令选择。','系统选项作为bootup值载入并在新游戏不必重建，故载入选项改动可被后续继续保留。','系统选项随正常SaveData登记保存，语言命令有例外直写。','暂停游标属于Game_Temp，默认0且不登记存档。','快捷三元游标属于Bag，默认[0,0,1]且Bag登记保存。'])
group('RESIZE',[loc('001_MKXP_Compatibility.rb',29,43),loc('001_StartGame.rb',21,35),loc('015_UI_Options.rb',532,544)],M,[132,144],normal,'启动/选项→Graphics请求',[
'首次应用且未初始化时请求默认SCREEN_WIDTH/HEIGHT，并设初始化标志。','同会话后续调用不再重复初始化内部尺寸。','0/1/2/3请求关闭全屏、0.5/1/1.5/2倍并居中。','4或负数请求全屏。','启动保存7被读取上界限制为4来请求，但内存字段仍7。','随后打开选项并关闭会把显示值4经setter写回7所在字段。','真实DPI/窗口/全屏效果未执行。'])
group('MAPINPUT',[loc('002_Scene_Map.rb',103,252),loc('001_Game_Temp.rb',1,94),loc('011_Messages.rb',1,20),loc('002_Overworld_Metadata.rb',121,123)],M,[150,158],normal,'常规Scene_Map.update→Pause/Ready/Interact',[
'标题请求在输入之前处理并提前返回。','消息窗显示中在请求生产与消费之前提前返回。','解释器运行或ice_sliding/descending_waterfall/ascending_waterfall任一真时不生成新输入请求。','新输入检测优先USE，其次ACTION，其次SPECIAL，最后F9。','ACTION仅菜单未禁用且玩家不移动时生产菜单请求。','SPECIAL只要求玩家不移动，不经menu_disabled门。','F9仅DEBUG时生产调试请求。','已有请求消费只要求玩家不移动，不重复套新输入生产守卫。','已有请求消费顺序为菜单、调试、快捷、互动，一轮取其一。','菜单调用清请求、设in_menu真、整姿、地图更新后开屏；正常返回再清in_menu。','无玩家的暂停屏入口直接返回，DEBUG下先提示。','miniupdate更新世界与spritesets但没有输入检测/请求分派；已有请求不由它消费。','共享pbUpdateSceneMap只有当前场景为地图且未淡出时调用miniupdate。'])
group('PAUSELOOP',[loc('001_UI_PauseMenu.rb',4,128),loc('006_Event_HandlerCollections.rb',80,133)],M,[151,157],normal,'Pause菜单场景与注册项调用',[
'每次入口先按排序/条件建立一次可见命令及效果列表，普通循环不重建可见集合。','选择窗口每次以Game_Temp.menu_last_choice恢复索引。','BACK或ACTION返回−1且关闭本菜单。','USE返回当前索引并写回临时游标。','正常效果返回false时继续同一选择循环。','效果返回true会停止循环；默认需要退出的handler已各自显式调用场景关闭。','没有通用异常ensure清理，不能把正常回到父级合同延伸到异常退出。'])
pause=[('图鉴','持图鉴且可访问数>0','按当前地区设置/单一图鉴/多区域分流，正常返回false',133,164),('队伍','party_count>0','无隐藏招式结果回菜单；有结果则关闭菜单、in_menu假并转交隐藏招式，返回true',166,184),('背包','不在捕虫大会','无物品结果回菜单；有结果则关闭菜单、in_menu假并转交关键道具，返回true',186,204),('Pokégear','has_pokegear','正常子屏返回后按fly_destination决定关闭或刷新，并调用飞行转交',206,220),('城镇地图','无Pokégear且持TOWNMAP','返回目的地时记录并关闭；随后飞行转交',222,237),('训练家卡','无附加门；名称为玩家名','正常关闭后回菜单false',239,252),('保存','game_system存在且save_disabled假且非Safari且非捕虫','true关菜单，false刷新重显',254,272),('选项','无附加门','以in_load_screen=false打开，正常返回刷新地图与菜单false',274,288),('调试','DEBUG真','正常返回刷新false',290,302),('退出游戏','无附加门','确认退出通过后无论保存返回值均关菜单且scene=nil',304,321)]
for i,(name,gate,effect,a,z) in enumerate(pause):
 group('PAUSE'+str(i+1).zfill(2),[loc('001_UI_PauseMenu.rb',a,z)],M,[161+i,161+i],normal,'Pause注册项→子屏/动作',[name+'可见门：'+gate+'。',name+'执行及返回：'+effect+'。'])
group('SESSIONS',[loc('001_SafariZone.rb',4,200),loc('002_BugContest.rb',4,449)],M,[171,176],normal,'Safari/Bug条件及Pause退出效果',[
'Safari状态正常启动记录当前地图为接待点并设进行中。','pbInSafari还需地图是该接待点或具有Safari标记。','捕虫正常启动设自身进行中并选出队伍成员，不清Safari状态。','同地图两种正常启动可使两个退出项同时可见，不证明默认Demo存在此组合。','保存要求两会话均假；两个退出项分别只要求自己条件真。','四组合00/10/01/11的Save/Safari/Bug可见集合分别100/010/001/011。','Safari退出确认通过后显式关菜单，decision设1并请求回接待点。','Safari退出拒绝刷新重显且false。','捕虫退出确认通过后显式关菜单并启动评审。','捕虫退出拒绝刷新重显且false。','同order60不额外承诺两退出相对次序。','Safari信息窗按步数配置显示球或步数/球，捕虫info后继覆盖为已捕获/等级/球或None/球；内部结算另归WP53。'])
group('PC',[loc('019_UI_PC.rb',1,237),loc('016_Metadata.rb',1,81)],M,[184,212],normal,'PC主循环/玩家PC/物品与邮件分支',[
'普通PC先开机消息再建立一次可见注册集合。','普通PC每次主消息命令默认索引0，没有把上次选择写回该默认位。','普通PC BACK与注销均结束并在正常尾部请求PC close。','储存创建者见过标记决定Someone或作者名PC，作者名从全局metadata本地化并空时回Bill。','储存/玩家PC/净化室/名人堂效果正常返回false回PC主循环。','玩家PC子菜单循环保留自身command值，与主PC游标独立。','储存子菜单循环保留自身command值，与主PC游标独立。','PC取出入口队伍满仅提示并继续储存子菜单，不打开Storage屏。','PC存入入口非蛋且HP>0成员数≤1仅提示并继续储存子菜单。','整理/取出/存入分别传模式0/1/2。','玩家PC菜单为物品储存/信箱/关闭；BACK等同关闭并正常尾音。','物品取出/丢弃对象缺失时先创建，再按empty判是否开屏。','物品存入没有同一空储存守卫，直接开存入屏。','物品子菜单返回退出只回上级玩家PC。','信箱缺失/空时只提示。','信箱列表按sender构造，末尾Cancel；选择一封可读/移包/给队伍/取消。','移包先确认消息丢失，Bag.add成功后显示消息并删除邮箱项。','Bag.add失败给满消息，邮箱项未删除；该分支不存在先清邮件内容再检测的动作。','给予调用Party邮件接收屏；正常返回重建邮箱列表。','Party邮件接收取消不转移；非蛋且未持物/邮件才在提示正常返回后写成员邮件/持物并删除邮箱。','PC真实地图事件调用者尚未取得工程材料；脚本定义和调试入口不能认证Demo可达。'])
group('PCEXTRA',[loc('023_UI_PurifyChamber.rb',1287,1310),loc('006_UI_HallOfFame.rb',120,132),loc('006_UI_HallOfFame.rb',435,493)],M,[191,196],normal,'净化室/名人堂PC项注册→正常子调用返回',[
'净化室PC项仅seen_purify_chamber真可见，入口包装在开屏之前设该标记真。','名人堂PC项仅累计编号>0可见。','登记流程追加记录后递增累计编号，PC浏览入口不写该编号。','这两个PC项正常子调用结束后都返回false。','内部净化/名人堂演出未在本贡献全文审读，不能把已核注册门升级为整屏通过。'])
group('READYBUILD',[loc('016_UI_ReadyMenu.rb',299,331),loc('013_Items/008_PokemonBag.rb',1,32) if '013_Items/008_PokemonBag.rb' in alias else loc('008_PokemonBag.rb',1,32),loc('004_Overworld_FieldMoves.rb',4,64)],M,[216,222],normal,'地图SPECIAL请求→候选集合→快捷场景',[
'固定16个候选招式按标识枚举，再逐成员筛非蛋/已学会/场地资格。','每个合格成员贡献对应招式与队伍下标，重复招式来自不同成员可保留。','道具登记列表只保留当前Bag仍持有的项目。','两类都空只提示登记用途，不打开Ready场景。','候选非空才设in_menu真并更新地图后开屏，正常结束再置假。','候选资格不保证执行成功。'])
group('READYUI',[loc('016_UI_ReadyMenu.rb',4,232)],M,[224,230],normal,'Ready按钮/选择循环→Bag共享三元游标',[
'两列各按本地化名称字符串比较排序。','招式列有成员图标，物品列有物品图标。','重要道具不绘数量，其余>99显示>99，否则xN。','选择侧按钮外凸并高亮。','场景直接使用Bag同一三元数组，正常下标变动直接改该数组。','非空侧只把超过末位的下标改为末位；源码没有统一负数下界夹限。','当前侧空会切到另一非空侧。','LEFT仅在当前右侧且招式非空时切左；RIGHT对称。','输入链LEFT/RIGHT分支先于BACK，再USE，不推广其它UI同轮顺序。','BACK返回−1，USE返回当前侧与窗口下标。','场景更新先把窗口旧索引写到持久数组，再更新选择窗口；最后一轮同轮方向/确认可能留下旧数组值，正常分轮导航向量保持。'])
group('READYUSE',[loc('016_UI_ReadyMenu.rb',236,295),loc('001_Item_Utilities.rb',69,82),loc('001_Item_Utilities.rb',755,765),loc('002_Item_Effects.rb',363,366)],M,[232,241],normal,'Ready确认→领域handler→关闭/继续',[
'FLY先隐藏Ready并开专用飞行选择器；无目的地则重显继续。','FLY有目的地则记录、in_menu假、转交选定成员隐藏招式并结束Ready。','其它招式确认拒绝重新显示，确认通过则转交并结束。','道具使用前确认拒绝不先清in_menu，直接重显。','确认通过道具使用前清in_menu，包装true结束。','道具包装false会恢复in_menu真并重显。','缺handler会包装为false并提示不能使用；handler正常false同样包装false。','使用成功且是消耗品才尝试从Bag移除；成功与消耗独立。','COINCASE显示代币后正常true，数量保持且Ready关闭。','领域handler异常没有本层统一保证标记恢复/资源清理。'])
group('PREVIEW',[loc('003_Trainer_Sprites.rb',4,69),loc('025_UI_TextEntry.rb',77,179),loc('025_UI_TextEntry.rb',371,490)],M,[74,81],normal,'载入/命名两模式→TrainerWalkingCharSprite',[
'玩家/NPC命名两模式均用同一行走预览组件，合法4×4图集仅取首行四格。','盒名两模式用单行四格并把组件周期设0.4秒。','时点0/0.20/0.40/0.50的行走帧为0/1/3/0。','相同时点盒名帧为0/2/0/1。','缺预览位图时命名构建仍读取宽高，可在构建失败；不补统一空态或套载入专有错误文字。'])
group('HELP',[loc('002_UI_Controls.rb',8,83),loc('002_EventScene.rb',66,204),loc('005_Event_Handlers.rb',4,60)],C,[1,61],normal,'Controls→EventScene回调/资源请求',[
'四页顺序为F1/F8、方向、USE/BACK、ACTION/SPECIAL说明。','七个键图分别按_INTL获得请求身份，背景身份固定；标签独立本地化。','F1/F8及默认C/X/Z/D只作为帮助内容，不作真实绑定证据。','开场冻结图形并建所有页，键图/标签初始透明度0。','首页和换页都把旧内容0.5秒淡出与新页延迟0.5后淡入串成名义1秒。','首页冻结期间的透明度变化不直接宣称可见闪烁。','父级先触发onUpdate再判BACK，BACK分支排斥同轮USE。','标准初始化无BACK回调，所以单BACK不翻页、不退出。','BACK+USE在稳定页只分发空BACK回调，页码保持。','非末页USE页码加1，清确认回调、等待图片变化、完成再重挂。','换页等待中的USE更新不触发已清的确认回调。','末页USE先快照并冻结、视口置黑、请求8单位过渡，再释放背景与场景。','场景没有ACTION/方向翻页分支。','场景释放清回调与持有sprites；不写Player字段。','全脚本检索ButtonEventScene/pbEventScreen未定位实际调用者，不推默认事件或Demo已可达。'])
group('CARD',[loc('012_UI_TrainerCard.rb',4,111),loc('014_TrainerType.rb',52,81),loc('001_Utilities.rb',380,384)],T,[1,59],normal,'Pause训练家卡→全局玩家/统计/地区/图像',[
'开场、查看循环、正常收尾顺序调用。','背景女性变体存在且玩家女性才选择，否则默认。','卡面女性变体经本地化身份解析，存在且玩家女性才用；与背景判断独立。','训练家正面图按类型优先当前装扮_N，再回基础身份，装扮0同样先试_0。','画像横向按128宽居中，底边恒240，不是垂直居中。','宽128高256时左上(336,−16)，宽128高128时(336,112)。','姓名/公开号/金钱/图鉴拥有与已见/游戏时间/开始日期六行在开场一次绘制。','公开号用至少五位十进制零补齐；42为00042。','3661秒显示1h1m，未满小时只分钟。','开始时间为空才当场写Time.now，此副作用不由BACK撤回。','地区读取当前地图元数据定位的第0值，缺地图/定位回默认0。','八槽徽章按i+region×8真值绘第i图标，x=72+i×48，图集行也按region。','查看循环没有动态重绘文本与徽章。','循环唯一局部退出输入BACK，正常退出请求关闭音并淡出清理。','ACTION/方向没有选择或翻页分支。','卡面没有正反页分支，不据局部只有正面断言所有作品卡面结构。'])
group('CREDITS',[loc('007_UI_Credits.rb',36,233),loc('001_Settings.rb',23,42)],CAT,[459,461],normal,'Credits调用→标记/音频/场景交接',[
'游戏致谢之后追加插件署名，再追加引擎/宿主/版权内容。','插件作者至少五名时两列配对，末单名补空；较少时逐行。','背景每名义11秒按相对运行钟换，文字每秒40像素滚动。','首次creditsPlayed假时USE不跳过，已播真时USE可以结束。','正常收尾快照并淡出BGM、冻结、黑色8单位过渡、释放、写已播标记、恢复旧BGM，再按是否有地图设新地图场景或nil。','BACK没有独立跳过分支。'])
group('CLOCK',[loc('010_PictureEx.rb',164,204),loc('010_PictureEx.rb',311,317),loc('010_PictureEx.rb',362,485),loc('002_EventScene.rb',131,163)],M,[29,31],normal,'Title/Controls→picture process scheduler',[
'图片过程调度用当前单调时钟减其局部timer_start，再乘20转整单位，不是绝对运行相位帧。',
'过程时间单位delay/duration分别除20得秒；全部过程结束且无旋转后重置timer_start。',
'标题与控制页的相对淡入/延迟来自局部图片过程，不能套行走预览的绝对周期。',
'等待仍调用场景更新；确认回调清空负责抑制推进，Input更新本身不是跳页事实。'])
group('CURSORINPUT',[loc('005_SpriteWindow_text.rb',753,965),loc('016_UI_ReadyMenu.rb',167,232)],M,[220,223],normal,'Ready隐藏命令窗→游标保存时点',[
'单列UP/DOWN首按沿可在端点回绕，持续repeat不一定端点回绕。',
'Ready持久数组在本轮命令窗更新之前取窗口下标；用户连续普通分轮导航后可保留当前索引。',
'负数下标不由通用index setter钳限，而会保留负值并停止方向导航；这仅是诊断额外输入域，不推默认合法游标产生负数。'])
group('LANGUAGE',[loc('001_Trainer.rb',169,176),loc('005_Pokemon_Owner.rb',19,41),loc('001_Utilities.rb',51,63),loc('015_UI_Options.rb',4,34)],M,[135,135],normal,'UI语言索引与训练家/拥有者领域语言',[
'界面语言字段是LANGUAGES候选索引，不是训练家或拥有者语言ID。',
'训练家默认语言由宿主语言前两字符映射，未识别回英语2。',
'拥有者显式构造保存入参语言；从训练家创建复制其当前语言值。',
'外来拥有者构造默认语言2；界面选择语言不直接同步已有拥有者语言。'])
# Make assertion IDs recoverable and source identities complete without copying reference code.
save('forward.json',{'schema':'r8-ui-navigation-forward-v1','reader':'/root/ui_navigation_audit','source_fact_assertion_count':len(facts),'facts':facts,'warning':'These explicit source assertions form a bounded semantic set, not a claim to exhaust every assertion in the shared test catalog. Unmapped source units remain named below.'})
# Full-read and partial read ledger with exact uncovered intervals.
def complement(n,rr):
 s=sorted(rr);m=[]
 for a,z in s:
  if m and a<=m[-1][1]+1:m[-1][1]=max(m[-1][1],z)
  else:m.append([a,z])
 c=[];pos=1
 for a,z in m:
  if a>pos:c.append([pos,a-1])
  pos=max(pos,z+1)
 if pos<=n:c.append([pos,n])
 return c
led=[]
for x in ids:
 units=[]
 for u in x.get('units',[]):
  links=sorted({f['id'] for f in facts for ref in f['source'] if ref['path']==x['path'] and ref['line_start']<=u['line']<=ref['line_end']})
  read=any(a<=u['line']<=z for a,z in x['read_ranges'])
  units.append({**u,'header_read':read,'fact_ids':links,'disposition':'BOUNDED_FACT_MAPPING' if links else ('READ_OTHER_DOMAIN_OR_UNDECOMPOSED_UNIT' if read else 'UNREAD')})
 led.append({'identity_id':x['id'],'path':x['path'],'status':x['read_status'],'reader':'/root/ui_navigation_audit','read_ranges':x['read_ranges'],'unread_ranges':complement(x['lines'],x['read_ranges']),'whole_file_semantic_read':x['read_status']=='FULL_READ','structure_units':units,'source_assertion_exhaustive':False if x['kind']=='reference' else 'formal-unit-matrix-below'})
save('reading-ledger.json',{'schema':'r8-ui-navigation-ledger-v1','updated_utc':NOW,'records':led,'full_formal_files':4,'full_reference_files':sum(x['kind']=='reference' and x['read_status']=='FULL_READ' for x in ids),'partial_reference_files':len(partial),'formal_full_read_ranges':{'WP65-main':[[1,140],[141,263]],'Controls':[[1,61]],'TrainerCard':[[1,59]],'UI-test-catalog':[[1,145],[146,290],[291,435],[436,580],[581,725],[726,855],[856,985],[986,1111]]},'untruncated_recovery':'WP65 main reread in two independent output blocks after initial combined truncation. MessageConfig full-file attempt was truncated and has no FULL_READ credit; only explicit bounded rereads credited. Wrong guessed paths produced errors then exact paths resolved; nonexistent paths receive no identity/read credit.','source_static_only':True,'behaviour_executions':0})
# Reverse entries preserve compound text and distinguish scoped evidence from final atomic closure.
cl=json.loads((O/'clause-denominator.frozen.json').read_text())['clauses'];rev=[]
for c in cl:
 linked=[f['id'] for f in facts if f['spec']['path']==c['path'] and f['spec']['lines'][0]<=c['line']<=f['spec']['lines'][1]]
 is_test=c['path']==CAT
 if is_test:
  # Exact navigation families and explicitly shared navigation rows only.
  l=c['line'];linked=[]
  testgroup=None
  if 132<=l<=174:testgroup='NV'
  elif 179<=l<=183:testgroup='CH'
  elif 189<=l<=196:testgroup='TC'
  elif any(k in c['text'] for k in ['B16-A015','B16-A058','B16-C058','B16-C114','B16-C115','U06-M10-006','JXN-NAME05']):testgroup='NAV_SHARED'
  if testgroup:
   keys={'NV':['BOOT','TITLE','LOADGATE','LOADPANEL','LOADCOMMAND','SAVE','EMERGENCY','OPTIONFRAME','RESIZE','MAPINPUT','PAUSELOOP','PC','READYBUILD','READYUI','READYUSE'],'CH':['HELP'],'TC':['CARD'],'NAV_SHARED':['BOOT','PREVIEW','OPTIONCONSUMER','TITLE','HELP','RESIZE','LOADPANEL']}[testgroup]
   linked=[f['id'] for f in facts if any(f['id'].startswith('UIF-'+k+'-') for k in keys)]
  elif 459<=l<=461:linked=[f['id'] for f in facts if f['id'].startswith('UIF-CREDITS-')]
 if c['path']==M and c['line']==88:state='COUNTEREXAMPLE_PROPOSED_GR8_UI_001'
 elif linked:state='READ_WITH_BOUNDED_FACT_LINKS_NOT_FINAL_ATOMIC_ACCEPTANCE'
 elif is_test:state='FULL_TEXT_READ_SOURCE_RECEPTION_PENDING_OTHER_UI_OWNER'
 else:state='FULL_TEXT_READ_ATOMIC_MAPPING_PENDING_OR_ADMIN_SCOPE'
 rev.append({'line_unit_id':c['id'],'path':c['path'],'line':c['line'],'compound_text':c['text'],'linked_source_fact_ids':linked,'disposition':state,'atomic_denominator_final':False,'remaining':'Every compound clause must still be assigned its exact per-assertion support rather than inherit all fact links of a nearby section. This matrix makes that gap explicit.'})
save('reverse.json',{'schema':'r8-ui-navigation-reverse-v1','frozen_line_unit_count':len(cl),'explicit_source_assertion_count':len(facts),'final_formal_atomic_denominator':'NOT_FROZEN: complete semantic sentence/compound assertion decomposition remains open','records':rev,'coverage_claim':'Full text was read. Broad section links are routing/evidence, never proof that every child assertion is accepted. No whole UI PASS.'})
# Interface contracts are independent of content-owner completion.
interfaces=[
('UI-I01','Scene_Map regular update→Pause/Ready','UIF-MAPINPUT','COMPLETE_LOCAL_REQUEST_PRODUCER_CONSUMER','miniupdate cannot consume pending requests; menu_disabled only ACTION producer.'),
('UI-I02','Pause→Party→HiddenMove','UIF-PAUSE02','CALLER_AND_RECEIVER_ENTRY_RETURN_READ_INTERNAL_PARTIAL','Party pbPokemonScreen full1204–1315; FLY cancel rebuild loses Box Link permission is source fact, other Party internal units not whole-read.'),
('UI-I03','Pause→Bag→KeyItem','UIF-PAUSE03','CALLER_AND_RECEIVER_ENTRY_RETURN_READ_INTERNAL_PARTIAL','Bag pbStartScreen full464–580; return item vs nil examined; inner item domain effects remain outside navigation.'),
('UI-I04','Pause→Pokegear/RegionMap→Fly','UIF-PAUSE04','POKEGEAR_REGIONMAP_FULL_READ_FLY_WRAPPER_READ','Full205/356 sources; follower/badge/outdoor guard at field wrapper read; actual transfer/route/media not executed.'),
('UI-I05','Load→Options→language direct save','UIF-LOADCOMMAND','COMPLETE_LOCAL_NAVIGATION_CHAIN','Whole option object alias and entire stored data serialization examined; boot data empty gate KER002 separately canonical.'),
('UI-I06','Pause/Interpreter→Save→Game.save','UIF-SAVE','COMPLETE_LOCAL_UI_BOOL_AND_FAILURE_PREFIX','Save/Game complete, value registry complete; delete/boot KER scope not duplicated.'),
('UI-I07','PC→Storage(mode0/1/2)','UIF-PC','CALLER_AND_RECEIVER_MAIN_CONTROL_FULL_OTHER_STORAGE_PARTIAL','Storage pbStartScreen1500–1658 full; scene drawing/selection and internal operations not all read; no whole Storage acceptance.'),
('UI-I08','PC→Mailbox→Party give mail','UIF-PC','MAILBOX_AND_GIVE_MAIL_RECEIVER_READ','Party938–956 normal cancel/guard/write/delete order checked; ordinary mail content/display domain pending.'),
('UI-I09','PC→Purify/Hall','UIF-PCEXTRA','REGISTRATION_WRITER_WRAPPER_READ_INTERNAL_PARTIAL','Full PC gates and visible-flag writer/number increment examined; internal lifecycle presentation incomplete.'),
('UI-I10','Controls→EventScene→Event','UIF-HELP','COMPLETE_LOCAL_CALLBACK_CHAIN','Full Controls/EventScene/EventHandler definitions; actual caller absent in scripts, engine event materials unavailable.'),
('UI-I11','TrainerCard→name/portrait/region/time','UIF-CARD','COMPLETE_LOCAL_PRESENTATION_CALL_CHAIN','Full card/type sprite chooser; getters read, player/pokedex/stat producers require creature/kernel owner; pixels not executed.'),
('UI-I12','Options→audio/config/movement/battle/input','UIF-OPTIONCONSUMER','BOUNDED_CONSUMER_UNITS_READ','Game_System full; message config set/get/speed and GamePlayer can_run wrappers read; battle prepare full209–306; wide battle domain not accepted.'),
('UI-I13','Load→MysteryGift download→return','UIF-LOADCOMMAND','FULL_DOWNLOAD_ENTRY_READ_REMAINING_MYSTERY_GIFT_PARTIAL','241–326 reads network/decrypt selection then append gift on normal feedback; external connection and delivery recipient rules not run.'),
('UI-I14','TownMap PBS→RegionMap','UIF-PAUSE05','READ_SOURCE_RECEIVER_PBS_OWNER_REQUESTED','/root/pbs_world_record_audit actual world record reader, full TownMap36/27point; record+source evidence sent, formal WP63 not read here.'),
('UI-I15','Save information→shared map naming→refusal','UIF-SAVE','PROPOSED_GR8_UI_001_WAIT_INDEPENDENT','/root/world_topology_audit actual independent refuter; no global semantic acceptance yet.'),
('UI-I16','Credits→global mark/BGM/scene','UIF-CREDITS','FULL_CREDITS_READ_FORMAL_PRIMARY_NOT_READ','Shared LC tests read, WP67-B primary not yet read; do not assign entire lifecycle acceptance.')]
save('interfaces.json',{'schema':'r8-ui-navigation-interfaces-v1','records':[dict(id=a,chain=b,fact_prefix=c,status=d,boundary=e,actual_local_reader='/root/ui_navigation_audit',execution='NOT_EXECUTED') for a,b,c,d,e in interfaces],'accepted_external_source_scope':[{'reader':'/root/world_topology_audit','scope':'map-name complete getter/lookup chain only','receipt':'collaboration message; exact metadata getter and lookup segments also independently read here','not_accepted':'Save proposal final disposition, all WP11 clauses, any other UI internal screen'}],'pending_external_reception':['full Party/Summary','full Storage/Pokedex','full Bag/ItemStorage/Marts','full MysteryGift/Mail lifecycle','Phone/Jukebox','Hall/Purify internal lifecycle','kernel/creature producer contracts and current historical qualification payloads'],'whole_ui_accepted':False})
counts={'formal_full_files':4,'formal_lines':sum(x['lines'] for x in ids if x['kind']=='formal'),'reference_full_files':sum(x['kind']=='reference' and x['read_status']=='FULL_READ' for x in ids),'reference_full_lines':sum(x['lines'] for x in ids if x['kind']=='reference' and x['read_status']=='FULL_READ'),'reference_partial_files':len(partial),'source_assertions':len(facts),'line_units':len(rev),'final_formal_atomic_denominator':None,'all_navigation_clauses_accepted':False,'whole_ui_pass':False}
save('counts.json',counts)
p=json.loads((O/'progress.json').read_text());p.update(updated_utc=NOW,stage='FACTS_AND_BIDIRECTIONAL_ROUTING_WRITTEN; FINAL_ATOMIC_MAPPING_PENDING',counts=counts,outputs=['identities.json','reading-ledger.json','forward.json','reverse.json','interfaces.json','proposals.json'],formal_atomic_status='NOT_FINAL; broad links never ACCEPTED');save('progress.json',p)
print(json.dumps(counts,ensure_ascii=False))
