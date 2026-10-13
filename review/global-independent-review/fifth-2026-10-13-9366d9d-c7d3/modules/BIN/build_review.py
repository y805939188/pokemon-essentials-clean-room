"""Generate bounded, implementation-independent review reports from audit evidence."""
import hashlib,json,pathlib,re,collections
O=pathlib.Path(__file__).parent;W=O.parents[4];R=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials');F=W/'deliverables/final-specification-set'
# O = workspace/review/global-independent-review/fifth/modules/BIN
assert (W/'AGENTS.md').is_file(),W
B5='9366d9d17aaeac3b4414236468affa650fb3dd27';RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';RT='7589c800b61ba13a13040ed0d686979b80a84fd0';FT='d5a462b4c6f8b78c3264a25d6b5495230fa265e2'
I={'schema_version':'gr5.review.v1','module':'BIN','source_baseline':{'root':str(R),'commit':RC,'tree':RT},'specification_baseline':{'commit':B5,'formal_root':'deliverables/final-specification-set','formal_tree':FT,'formal_file_count_inherited':131},'runtime_parameters':{'requested_model':'gpt-6-astra','requested_reasoning_effort':'ultra','requested_service_tier':'default','Fast':False,'actual_echo':'UNVERIFIED'},'execution_status':{'reference':0,'behavior_model':0,'host_or_demo':0,'shader_compilation':0,'authored_static_parsers':'TOOL_VALIDATION_ONLY'},'reviewer':'BIN有限独立审查；未创建其它会话/agent；沿用母任务身份'}
def emit(name,x): (O/name).write_text(json.dumps(dict(I,**x),ensure_ascii=False,indent=2)+'\n')
def ref(name):return 'deliverables/final-specification-set/'+name
wp13=ref('engine-overworld/wp13-map-events-npc-followers.md');im=ref('engine-overworld/wp13-interpreter-command-matrix.md');mr=ref('engine-overworld/wp13-move-route-matrix.md');wp15=ref('engine-overworld/wp15-resource-matching-and-audio.md');wp16=ref('engine-overworld/wp16-world-rendering-and-visual-transitions.md');bt=ref('engine-overworld/wp16-pre-battle-transitions.md');wp17=ref('user-interface/wp17-messages-windows-input.md');dt=ref('user-interface/wp17-draw-text-tags.md');scope=ref('scope-statement.md');wp02=ref('generic-kernel/wp02-rule-configuration-and-data-variants.md')
t16=ref('test-catalog/engine-overworld-wp16.md');teng=ref('test-catalog/engine-overworld-wp11-15-59-60.md');tui=ref('test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md')
def a(path,section,lines):return {'path':path,'version':B5,'section_or_vector':section,'lines':lines}
# Only scopes actually semantically examined are listed; reads for hash are not full-review claims.
cons=[]
def source(path,ranges,review,meaning,functions=None):
 p=R/path;data=p.read_bytes();n=len(data.splitlines());assert all(1<=x<=y<=n for x,y in ranges),(path,n,ranges)
 covered=set(i for x,y in ranges for i in range(x,y+1));gaps=[];start=None
 for i in range(1,n+2):
  if i<=n and i not in covered:
   if start is None:start=i
  elif start is not None:gaps.append([start,i-1]);start=None
 rec={'id':f'EXT{len(cons)+1:02}','path':path,'version':RC,'sha256':hashlib.sha256(data).hexdigest(),'total_lines':n,'semantic_ranges':ranges,'review_extent':review,'material_availability':'readable','evidence_level':'supported_static_bounded_consumer','semantic_review':meaning,'entry_points':functions or [],'outside_review_ranges':gaps,'outside_review_reason':'本BIN任务只审与内嵌明文的连接；其余可读区间不宣称不可得或已全审。','execution_status':'NOT_EXECUTED'}
 cons.append(rec);return rec['id']
S='Data/Scripts/'
srcsprite=source(S+'001_Technical/006_RPG_Sprite.rb',[[1,103]],'full','外部重开RPG精灵：替换构造/处置/位置赋值/普通与循环动画入口/活动查询/更新；构造建立普通和循环列表。播放建立独立SpriteAnimation并复用首个不活动槽或追加；位置先通知子动画再交宿主；每个父更新末清共享动画身份。未覆盖旧白化/伤害/闪烁等定义，不能称删除，但此文件更新不推进那些旧计数。FloatSprite保存浮点逻辑坐标再交原生setter。',['RPG::Sprite','FloatSprite'])
srccache=source(S+'007_Objects and windows/001_RPG_Cache.rb',[[1,144]],'full','覆盖内嵌加载/切图，保留内嵌目录转发与clear及定义期缓存。有效命中增加使用计数；非零色相复制并变色；空名32×32，非空加载不捕获。切图支持width/height，来源上边以图块所在行减height再加1；在复制后释放源用量。retain只对hue>0查色相键，否则保留基础图；处置计数到0且未保留才交宿主，copy重置计数。debug是显式文件输出入口，本次未调用。',['Cache.load_bitmap','Cache.tileEx','Cache.retain','BitmapWrapper'])
srcanim=source(S+'005_Sprites/008_Sprite_AnimationSprite.rb',[[1,331]],'full','当前动画按运行时间和默认20fps推进，末尾[N]改帧率，同帧只定位、跳帧不补定时；0/1/2位置改为顶/中/底。SE经pbSEPlay而非旧直接Audio请求。循环初始化读空普通动画的失败已在WP16。重复position3的空槽和坐标传播仍有局部失败，见已有M10-013；不新编号。临时格每次更新先算坐标，普通角色顺序不同。',['SpriteAnimation','AnimationContainerSprite','Spriteset_Map.addUserAnimation'])
srcweather=source(S+'012_Overworld/001_Overworld visuals/001_Overworld_Weather.rb',[[1,528]],'full','覆盖内嵌天气的全部7个方法与构造，类型改为注册身份，60粒子、独立叠层、阶段式渐变。淡入在途先拒绝；类型相同且上限相同再拒绝，正时长为阶段开关；立即分支调用新type/max。资源来自Graphics/Weather；寿命/Graphics.delta运动、雨滴与水花、雪扰动、Sun色调和Storm闪光均在新体内，旧39槽/每更新固定位移不投射当前天气。',['RPG::Weather'])
srcglobal=source(S+'005_Sprites/006_Spriteset_Global.rb',[[1,56]],'full','建立当前天气并在类型不同才调用fade_in；跨图累计/归零偏移，按显示坐标设置ox/oy，再更新天气。图片1–100与玩家/跟随/计时器独立。证明当前消费者没有调用旧数值type方案。',['Spriteset_Global.initialize','Spriteset_Global.update'])
srcaudio=source(S+'008_Audio/002_Audio_Play.rb',[[1,278]],'full','四类请求先解析AudioFile；有系统走系统分支，缺系统才检测RPG包装存在及play能力，最后直达Audio。stop的局部救援各异；ME现有系统缺相应stop时可能落包装/原生路径，现有M10候选不重报。字符串未显式覆盖项用100，预解析记录保留；UI默认SE只按登记名/文件存在条件选。',['pbResolveAudioFile','pbBGMPlay','pbMEPlay','pbBGSPlay','pbSEPlay','四类停止辅助'])
srcsys=source(S+'004_Game classes/002_Game_System.rb',[[1,255]],'partial','系统音频主路径与内嵌包装不同：记录克隆、文件存在门、音乐/SE选项缩放、暂停和位置、轨道、默认覆盖、恢复与记忆有自己状态。BGM参数错误重试一次位置0；SE无名停止。本文读取到battle_bgm入口，未重审后续系统更新。',['bgm_play_internal','me_play','bgs_play','se_play'])
srcev=source(S+'004_Game classes/007_Game_Event.rb',[[1,54],[185,259]],'partial','事件消费者从输入记录读取id/坐标/名称/页；按末页优先和开关/变量/自开关选择页，图形消费character_hue/opacity/blend_type/always_on_top这些B13字段。新空路线用于已擦路线；正常页建立自己的解释器状态。默认数据不是全部命令分派的证明。',['initialize','start','erase_route','refresh'])
srcfollower=source(S+'004_Game classes/010_Game_Follower.rb',[[1,29]],'partial','创建RPG事件并覆盖id/name；可选公共事件覆盖默认第0页列表，继而实例化跟随事件并设置外观/方向。因此默认第0页和空终止命令在构造消费链中有实质用途；移动其余域不扩审。',['initialize'])
srcroute=source(S+'012_Overworld/001_Overworld.rb',[[488,526]],'partial','pbMoveRoute创建兼容路线后显式改为不重复、可跳过，清默认列表；加穿透开、逐命令转换、异步脚本后插等待0、穿透关及终止0；waitComplete未使用。默认repeat=true不能覆盖此实际包装。',['pbMoveRoute'])
srccomp=source(S+'021_Compiler/004_Compiler_MapsAndEvents.rb',[[65,145],[220,250]],'partial','编译辅助消费MapInfo、MoveRoute/MoveCommand、EventCommand和Page默认记录；生成路线明确替换repeat/skippable/list；209/509与210是列表生成请求，代码0为终止。门页覆写条件/图形/trigger/列表。未执行编译或写数据。',['generate_move_route','push_move_route','push_event','add_passage_list'])
srcconvert=source(S+'011_Battle/007_Other battle code/007_BattleAnimationPlayer.rb',[[170,232]],'partial','RPG动画辅助新建Animation/Frame/Timing/AudioFile，复制动画身份、五列图集相关单元8列、位置偏移和定时；与PB动画播放器不同。只审默认记录的消费者，不把此片段当战斗播放器全审。',['RPG::Animation.fromOther','addSound','addAnimation'])
srctrans=source(S+'009_Scenes/001_Transitions.rb',[[1,170]],'partial','脚本transition先选具名特殊效果；未命中则调用保留的原生transition(duration换帧,filename,vague)，vague缺省20原样传。异常首次在此捕获；非空文件名才空名重试。普通过渡与B08/S14只有资源/参数角色关系，未证原生绑定或归一化。',['Graphics.transition','judge_special_transition','Transition_Base'])
srcscene=source(S+'003_Game processing/002_Scene_Map.rb',[[1,31],[72,104]],'partial','场景创建TilemapRenderer；传送在地图更新、逐图呈现处置之后调用继承Cache.clear，再建呈现；可证明清缓存调用点，不能由GC请求保证所有旧位图同步释放。',['createSpritesets','transfer_player'])
srcchar=source(S+'005_Sprites/003_Sprite_Character.rb',[[62,187]],'partial','普通角色继承外部改写RPG精灵，先super推进动画，后设置坐标、不透明/混合及动画ID；图块走扩展切图、字符走4×4图集。当前灌木由专用位图组成，并不证明使用B10的bush uniform。',['Sprite_Character.initialize','refresh_graphic','update'])
srcset=source(S+'005_Sprites/007_Spriteset_Map.rb',[[1,131]],'full','地图集添加图块资源并使用脚本地图渲染器；雾色相/不透明/混合/色调和视口tone/color都有明确赋值；这只证明原生图像属性需求，未能直接连到特定shader uniform。开头ClippableSprite为定义级裁切辅助，未作为当前初始化选择。',['Spriteset_Map.initialize','Spriteset_Map.update'])
srctile=source(S+'006_Map renderer/001_TilemapRenderer.rb',[[1,89],[524,545]],'partial','当前地图渲染常量为32格、8含空自动图块、48布局、5/20秒，色调/颜色变化转给各呈现单元；不等于B02原生七自动元件动画函数就是当前地图算法。',['TilemapRenderer constants','TilesetBitmaps.add','update tone/color'])
srcpic=source(S+'005_Sprites/001_Sprite_Picture.rb',[[1,58]],'full','图片请求按名称建立/销毁图形，原点/位置/编号z/缩放/opacity/blend/angle/tone传给精灵；单独tone与不透明赋值不定义颜色合成顺序，shader新增证据只在定义层补充。',['Sprite_Picture.update'])
srcinput=source(S+'001_Technical/004_Input.rb',[[1,31]],'full','只定义八个逻辑别名、底层刷新后F8截图以及鼠标窗内/强制捕获门；没有从两组控制器记录到逻辑按钮的原生选择/死区/重复延迟实现。',['Input.update','Mouse.getMousePos'])
srcfiles=source(S+'001_Technical/002_Files/001_FileTests.rb',[[109,143]],'partial','专用SE有空输入门和四后缀；图像去五种已知后缀但仅尝试png/gif，另一入口未命中返原输入。与宿主位图解码、内嵌缓存直读分开。',['pbResolveAudioSE','pbResolveBitmap','pbBitmapName'])
srcfont=source(S+'007_Objects and windows/002_MessageConfig.rb',[[1,25],[158,173],[411,435]],'partial','当前正文/小/窄字体27/21/27并带文字y偏移8；候选逐项调用Font.exist?，系统字体写入仍由宿主绘制。内嵌字体名字/TTF表或旧damage指定Arial Black均不能覆盖这些消费者。',['pbTryFonts','pbSetSystemFont','pbSetSmallFont','pbSetNarrowFont'])
srcdraw=source(S+'007_Objects and windows/010_DrawText.rb',[[396,425],[489,500]],'partial','字体默认值可为候选数组；按Font.exist?找到首个或回Arial。fn开标记先裁尾空白再检查存在，不存在用Arial；关闭弹栈恢复。颜色标记与图像shader是不同处理层。',['formatted text font default','fn tag'])
srcconf=source('mkxp.json',[[1,159]],'full','当前活动项为标题、512×384、八输入标签、SoundFont、pathCache=false、subImageFix/vsync/syncToRefreshrate=true；Lanczos3、smooth/integer/fullscreen等只为注释。该文件未指定rgssVersion；不从注释或EXE字面量猜默认选择。',['configuration fields'])
# Read two small actually-followed scene ranges not previously displayed is caught by explicit reading step before generation.
unknowns=[
 {'id':'BIN-U01','status':'UNKNOWN_NOT_BLOCKER','subject':'兼容脚本版本选择','detail':'三块定义均可读且全审；没有证明原生启动选择和加载顺序。当前可读消费者结构对应B13的字段，属于条件性兼容需求；不能据此声称三个变体都运行。Game.ini缺失为现有范围声明，不是三块明文不可读。'},
 {'id':'BIN-U02','status':'UNKNOWN_NOT_BLOCKER','subject':'着色器实际选择和拼接','detail':'55份正文与5个前缀已审。原生入口、源码长度、前缀组合、图形API/硬件路径、uniform归一化与纹理绑定未知；S11后邻I不自行判编译失败。'},
 {'id':'BIN-U03','status':'UNKNOWN_NOT_BLOCKER','subject':'实际图像/声音/字体输出','detail':'未执行GPU/Bitmap/Font/Audio；采样边界、钳制、精度、调度、图像解码与缺资源异常仍按当前条件合同。没有把词条/位图/字体的可打印投影当全部原生行为。'},
 {'id':'BIN-U04','status':'UNKNOWN_NOT_BLOCKER','subject':'两组控制器映射的选择','detail':'1666条复用加256条新解码，二者内容有差异；优先顺序、平台选择、空绑定解释、阈值/重复延迟/真实物理事件未证。'},
 {'id':'BIN-U05','status':'OUTSIDE_FINITE_SCOPE','subject':'其余原生/第三方/字节码','detail':'不扩审Game机器码、CRT、第三方完整库、内嵌字体字节码；并非材料不可得，也不把本次complete当它们全审。'},
 {'id':'BIN-U06','status':'UNVERIFIED','subject':'实际运行参数回显','detail':'仅记录用户请求astra/ultra/default，Fast禁用；未调查配置、额度、认证、私有会话或后端。'}]
# Current formal clauses are used directly; other module review claims are context only.
caps=[]
def cap(cid,title,classification,status,sources,anchors,relation,note,shared=[]):
 caps.append({'id':cid,'title':title,'classification':classification,'status':status,'evidence_level':'supported_static_bounded' if status=='supported' else 'static_definition_or_interface_only','source_ids':sources,'spec_anchors':anchors,'relationship':relation,'conclusion':note,'shared_contracts':shared,'runtime_evidence':'NOT_EXECUTED'})
cap('BIN-C01','兼容地图、事件、路线、动画和系统记录','Engine / Overworld Integration','supported',['B13',srcev,srcfollower,srcroute,srccomp,srcconvert],[a(wp13,'§2–3/§6；默认记录消费者边界',[13,65]),a(im,'§2及§3命令参数角色',[11,114]),a(mr,'§1–2路线容器与终止项',[5,73])],'supports_static_data_interface','B13构造提供当前消费者所需的页/图形/路线/音频/动画字段；字段默认值见逐函数账本。只支持这些数据接口，不把构造定义当全部事件分派或宝可梦战斗规则；载入的序列化记录不必运行构造器，默认值不证明实际数据样本内容。')
cap('BIN-C02','兼容变体及未见当前调用数据库域的默认值、公式和条件','Engine / Overworld Integration','unresolved',['B11','B12','B13 dormant RPG database types'],[a(wp13,'§1非标准RMXP全兼容承诺',[5,11]),a(scope,'§2–3证据限制',[93,111])],'definition_only_unselected','四层/三层地图、八参数/六参数、范围编号、公式求值和装备评分均已逐函数解释；当前启用未证，不能把它们作为新框架类层级或宝可梦规则移植。')
cap('BIN-C03','共享缓存与切图的有效覆盖','Generic Kernel','supported',['B13',srccache,srcscene,srcfiles],[a(wp15,'§5–5.1',[86,114]),a(teng,'B04-R13/14/21/27/28',[418,433]),a(wp17,'§7.3资源交界',[246,251])],'effective_external_override_plus_inherited_methods','外部加载/切图替换旧体；继承目录转发与clear仍可被调用。当前规格准确区分空名、缺失异常与包装回退；不要求复制引用计数实现。',['SHARED-BITMAP-LIFECYCLE','SHARED-RESOURCE-SELECTION'])
cap('BIN-C04','内嵌精灵演出与当前世界动画的差异','Engine / Overworld Integration','partial',['B13',srcsprite,srcanim,srcchar],[a(wp16,'§4.5',[155,168]),a(t16,'B04-W20/21',[80,81])],'effective_override_existing_candidate','内嵌偶数帧计数/单个动画替换/固定z不可冒充现行20fps与并存合同；外部仍存在的屏幕重复/坐标问题已有M10-012/013，本次只证据关联。未覆盖的旧白化/伤害等定义已审，但无静态当前调用证据。',['SHARED-MAP-VISUALS'])
cap('BIN-C05','旧天气与60粒子当前实现','Engine / Overworld Integration','supported',['B13',srcweather,srcglobal],[a(wp16,'§5.1–5.1.1',[171,199]),a(t16,'WR07–11/B04-W12/13',[15,19])],'superseded_definition','旧40槽创建/1起点循环只得到39有效槽；当前所有同名方法被外部覆盖，60粒子合同有当前消费者，旧异常不构成现行天气修订。',['SHARED-MAP-VISUALS'])
cap('BIN-C06','音频数据及分支请求边界','Engine / Overworld Integration','supported',['B11 audio inherited','B12 audio inherited','B13 audio inherited',srcaudio,srcsys],[a(wp15,'§6及§8',[116,178]),a(im,'241–251',[77,85]),a(wp17,'SE/ME与交互调用',[45,59])],'conditional_fallback','AudioFile的名称/音量/音高为共同接口；系统存在时走其选项/登记/存在性门，缺系统才有RPG包装或直达Audio路径。RES音频尾部精确复用，不将包装默认值改写为系统音频规则。',['SHARED-AUDIO-REQUESTS'])
cap('BIN-C07','明文颜色/灰度/透明度与图案的次序','Engine / Overworld Integration','partial',['B03','B05','B06','B10','S02','S04','S05','S06','S07','S08','S09','S10','S11','S12',srcset,srcpic,srctile],[a(wp16,'§3.3/§4.4/§5.3；宿主结果边界',[99,101]),a(wp16,'§5.3',[206,212]),a(wp17,'颜色标记不是shader规则',[24,42])],'new_definition_scope_extension','当前规格给逻辑色调与颜色属性，没有给这些可读程序的归一化数学次序；候选BIN-001仅建议独立宿主静态附录，原生接线未证，不自签必修。',['SHARED-MAP-VISUALS','BIN-HOST-READABLE'])
cap('BIN-C08','位图混合、色相、模糊和缩放','Engine / Overworld Integration','partial',['B04','B07','B09','S00','S01','S03','S13',srccache,srcconf],[a(wp15,'§5色相/复制',[86,114]),a(wp02,'§8宿主配置',[257,263]),a(scope,'素材与媒体边界',[98,100])],'new_definition_scope_extension','RGBA混合零alpha分支、HSV变换、三点模糊、六乘六Lanczos正文均已审；未据配置注释宣称已启用，也不规定未来GPU架构。',['SHARED-BITMAP-LIFECYCLE','BIN-HOST-READABLE'])
cap('BIN-C09','原生兼容自动元件着色器','Engine / Overworld Integration','unresolved',['B01','B02',srcscene,srcset,srctile],[a(wp16,'§3.1–3.2.1',[23,97])],'unselected_native_path','读懂动画区域、顺序及索引/除零边界；当前脚本自行建地图图块和相位，不能由原生七元件表改写WP16的八含空布局或容量折叠合同。')
cap('BIN-C10','普通宿主过渡与脚本具名过渡','Engine / Overworld Integration','partial',['B08','S14',srctrans],[a(wp16,'§6.1',[251,270]),a(bt,'§5/§7',[59,111]),a(t16,'BT11/14/15',[39,43])],'host_boundary_refinement','宿主普通过渡的混合/遮罩程序可读；脚本具名转场及fallback次序已有合同。vague=0程序除零不直接推出外部transition失败，因为原生守卫/归一化未证。',['BIN-HOST-READABLE'])
cap('BIN-C11','多种图形后端的YUV与通道转换','Engine / Overworld Integration','unresolved',[f'B{i:02}' for i in range(14,32)]+[f'S{i:02}' for i in range(15,27)]+['P01','P02','P03','P04','P05'],[a(scope,'宿主输出不声明',[98,111])],'definition_only_backend_variants','Y/U/V的平面/交错顺序、三组系数、矩形坐标前缀、RGB交换和顶点转换逐份有事实记录；外部当前脚本不直接绑定这些后端程序，非新游戏域功能。')
cap('BIN-C12','两组控制器映射与输入消费者','User Interface','unresolved',['B00','CM001–CM256',srcinput,srcconf],[a(wp17,'§2/§6.1/§6.4',[15,22]),a(wp17,'§6.1',[145,151]),a(wp17,'§6.4',[212,218])],'data_present_selection_unknown','1666条复用，另256条解析；忽略platform后的逐序比较102相同、151同GUID但内容不同、3新GUID。不能据数据决定物理键/死区或默认平台优先。')
cap('BIN-C13','词典/格式/错误/符号字符串的处置','Generic Kernel','supported',['B32–B58 data','all 161104 string candidates'],[a(scope,'§3字符串匹配不等于覆盖',[107,111])],'no_independent_game_requirement','24词典片段属于固定宽度13504词条字节数据，两块纯9/10数值段，一块库诊断。其余每条字符串已登记类型和理由；没有以错误文字推出实际故障/恢复或执行其中建议。')
cap('BIN-C14','短zlib加载程序','Generic Kernel','unresolved',['RB01'],[a(scope,'静态定义/宿主边界',[93,111])],'definition_only_unselected','可读短脚本已有常量则跳过、否则加载zlib；没有原生调用或外围救援证明。新增取证事实，不宣称启动流程现有条款矛盾。')
cap('BIN-C15','字体投影与DPI元数据','User Interface','unresolved',['SFNT19','B59',srcfont,srcdraw,srcconf],[a(wp17,'§3.4字体及未验证',[93,98]),a(dt,'§2字体',[46,59]),a(dt,'§6.1与宿主',[108,117])],'metadata_does_not_close_host','内嵌字形名/轮廓投影不是可读脚本；manifest声明DPI值。当前字体链调用原生exist/测量，不由内嵌字体存在补实际命中、字宽或窗口效果。',['SHARED-FONT-MEASUREMENT'])
# Every actual function and original long block has a bounded forward mapping.
scripts=json.loads((O/'script-behavior.json').read_text());sh=json.loads((O/'shader-behavior.json').read_text());data=json.loads((O/'data-block-disposition.json').read_text());strings=json.loads((O/'string-inventory.json').read_text())
functions=[]
for z in scripts['records']:
 c='BIN-C06' if z.get('review_origin')=='inherited' else ('BIN-C02' if z['block'] in ('B11','B12') or re.match(r'RPG::(?:Actor|Class|Skill|Item|Weapon|Armor|Enemy|Troop|State)(?:::|$)',z['source_scope_for_trace_only']) else ('BIN-C03' if '::Cache' in z['source_scope_for_trace_only'] else 'BIN-C04' if z['source_scope_for_trace_only']=='RPG::Sprite' else 'BIN-C05' if z['source_scope_for_trace_only']=='RPG::Weather' else 'BIN-C01'))
 functions.append({'source_record':z['id'],'source_ledger':'script-behavior.json','lines':z['lines'],'capability':c})
for z in sh['records']:
 c=next(c['id'] for c in caps if z['id'] in c['source_ids']);functions.append({'source_record':z['id'],'source_ledger':'shader-behavior.json','capability':c,'all_functions':[f['name_for_trace'] for f in z['functions']]})
for z in sh['prefix_fragments']:functions.append({'source_record':z['id'],'source_ledger':'shader-behavior.json#/prefix_fragments','capability':'BIN-C11'})
functions.append({'source_record':'RB01','source_ledger':'additional-script-behavior.json','capability':'BIN-C14'})
blockmaps=[]
for z in data['records']:
 bid=z['id'];cs=[c['id'] for c in caps if bid in c['source_ids']]
 if bid=='B13':cs=['BIN-C01','BIN-C02','BIN-C03','BIN-C04','BIN-C05','BIN-C06']
 if bid in ('B11','B12'):cs=['BIN-C02','BIN-C06']
 if z['classification'] in ['size_indexed_dictionary_fragment','whitespace_only_numeric_table','library_diagnostic_explanation']:cs=['BIN-C13']
 blockmaps.append({'block':bid,'offset':z['offset'],'size':z['size'],'classification':z['classification'],'capabilities':cs})
assert all(z['capabilities'] for z in blockmaps)
emit('source-to-spec.json',{'bounded_scope':'仅RES-L05明文定义、候选类型及具名外部消费者；不认证这些规格整域或原生机器码。','capabilities':caps,'function_mappings':functions,'long_block_mappings':blockmaps,'candidate_family_mappings':[{'classification':k,'count':v,'ledger':'string-inventory.json','capability':'BIN-C13' if k not in ['program_or_prefix','readable_compatibility_program','additional_controller_mapping','controller_database','embedded_font_names_or_binary_fragments','manifest'] else '按具体source_record转对应BIN-C01–C15','scope':'每条候选有offset/size/hash/类型/处置引用；不是数量替代函数阅读。'} for k,v in strings['classification_counts'].items()],'global_feature_matrix':'遵守只写BIN；本文件capabilities为本地Feature Matrix投影，不改共享矩阵、不新增全局功能统计。'})
reverse=[]
for c in caps:
 for anchor in c['spec_anchors']:
  reverse.append(dict(anchor,capability=c['id'],source_ids=c['source_ids'],status=c['status'],relationship=c['relationship'],support_boundary=c['conclusion']))
emit('spec-to-source.json',{'scope':'对已实际读完的8份WP13/15/16/17正文/附表和关联测试作有界反查；仅列与BIN证据有关的条款，不把未映射领域说成缺来源。','records':reverse,'effective_supplements':[{'path':t16,'semantic_ranges':[[1,153]],'extent':'full','purpose':'WR/BT/B04-W/XC/GR3-CAM均为现行静态向量，未含shader数学'},{'path':teng,'semantic_ranges':[[118,248],[297,321],[400,435]],'extent':'partial','purpose':'EV/FW/IM/MR及RS/B04-R资源音频、事件数据、缓存失败/共享有效期'},{'path':tui,'semantic_ranges':[[1,52],[535,583],[712,761]],'extent':'partial','purpose':'MG/DT/B04-M/I/D/R4-CM/NM/SK/WR不构成物理输入或像素认证'},{'path':'../M12/host-config-contracts.json','pointer':'#/records','purpose':'mkxp159行全部字段活动/注释状态；本次直接重读R配置交叉核对'},{'path':'../M10/shared-interfaces.json','pointer':'#/interfaces selected shared identities','purpose':'资源/位图/音频/字体/地图共享接口边界；不承接其它域PASS'},{'path':'../M10/findings.json','pointer':'#/findings id=GR5-M10-013','purpose':'已存在屏幕重复动画空槽失败，不重复编号'}],'unmapped_statement':'构造器不证明全部事件分派；着色器不证明原生入口；字体和按钮字符串不证明宿主行为。其余章节与其它131正式文件不作BIN全量再审。'})
# Coverage: exact source and specification reading, plus every finite program/data range.
spec_read=[]
for path in [wp13,im,mr,wp15,wp16,bt,wp17,dt,t16]:
 p=W/path;d=p.read_bytes();spec_read.append({'path':path,'version':B5,'sha256':hashlib.sha256(d).hexdigest(),'semantic_ranges':[[1,len(d.splitlines())]],'review_extent':'full','comparison_scope':'full_text_read_bounded_comparison','material_availability':'readable','evidence_level':'static_current_contract_read','purpose':'逐节/表/当前向量反查内嵌定义与外部覆盖，非重新认证全域。'})
for path,rs in [(wp02,[[246,278]]),(scope,[[1,16],[86,125]]),(teng,[[118,248],[297,321],[400,435]]),(tui,[[1,52],[535,583],[712,761]])]:
 d=(W/path).read_bytes();spec_read.append({'path':path,'version':B5,'sha256':hashlib.sha256(d).hexdigest(),'semantic_ranges':rs,'review_extent':'partial','material_availability':'readable','evidence_level':'static_current_contract_read','outside_ranges':'其余范围不属于本次BIN映射；不是缺资料。'})
emit('reading-coverage.json',{'complete_for_assigned_plaintext':True,'not_a_claim':'不签Game.exe全机器码/第三方库/字体字节码/宿主运行全审。','method':'先复现RES有限候选；源正文逐函数审读，简单默认值/访问器以安全解析生成事实表并人工核读；词典按相邻长度/偏移表完整分组，诊断/格式/数值投影逐候选分类；所有code-shaped/span候选复查，不用grep数量代替程序语义。','baseline_materials':[{'path':'../RES/report.md','extent':'full'},{'path':'../RES/limits.json','extent':'full'},{'path':'../RES/binary-interface-audit.json','pointer':'#/records/0/embedded_readable','extent':'60块元数据全读；1666映射精确复用，不重复全文'}],'game_exe':{'path':'Game.exe','version':RC,'size':len((R/'Game.exe').read_bytes()),'sha256':strings['source_sha256'],'material_availability':'binary_with_readable_programs_and_data','review_extent':'partial','assigned_plaintext_extent':'full','original_long_blocks':data['records'],'script_functions':{'total':225,'new_read':194,'inherited_audio':31,'accessor_declarations':988,'ledger':'script-behavior.json'},'shaders':{'original_labelled':29,'actual_long':28,'reclassified_dictionary':['B52'],'additional_short_or_single_line':27,'actual_total':55,'functions':66,'prefixes':5,'ledger':'shader-behavior.json'},'additional_script':{'records':1,'ledger':'additional-script-behavior.json'},'candidates':{'count':161104,'previously_unselected':160820,'unclassified':0,'ledger':'string-inventory.json','supplemental_queries':'candidate-search-audit.json'},'other_long_data':{'original_labelled':26,'actual_including_B52':27,'dictionary_spans':24,'whitespace_tables':2,'diagnostic_blocks':1,'ledger':'data-block-disposition.json'},'controller_data':{'inherited':1666,'additional':256,'not_unique_controller_count':True,'ledger':'additional-controller-data.json'},'unreviewed_assigned_plaintext':[],'excluded_file_semantics':unknowns},'external_source_records':cons,'specification_records':spec_read,'blockers':[],'unknowns':unknowns})
# Shared identities, not separate duplicate findings per consumer.
shared=[]
for sid,title,cc,lim in [
 ('SHARED-RESOURCE-SELECTION','资源匹配与空名/缺名',['BIN-C03'],'覆盖的是当前脚本解析与加载接口；内嵌旧目录转发不扩成所有媒体可用。'),
 ('SHARED-BITMAP-LIFECYCLE','位图缓存与复制',['BIN-C03','BIN-C08'],'旧clear只丢索引并请求GC；当前使用计数覆盖已核，最终销毁/像素未知。'),
 ('SHARED-AUDIO-REQUESTS','音频登记/包装/宿主请求',['BIN-C06'],'复用RES音频定义；按系统是否存在区分实际脚本分支，未证明真实发声。'),
 ('SHARED-MAP-VISUALS','世界图像、天气与动画',['BIN-C01','BIN-C04','BIN-C05','BIN-C07','BIN-C09','BIN-C10'],'当前外部覆盖优先；M10-012/013仍为原候选，本次不签其必修结论。'),
 ('SHARED-FONT-MEASUREMENT','字体选择/测量',['BIN-C15'],'内嵌字体数据和名字不能补出Font.exist?或字宽/最终UI。'),
 ('BIN-HOST-READABLE','可读宿主程序的条件性数学事实',['BIN-C07','BIN-C08','BIN-C10','BIN-C11'],'新本地审查身份；若后续接纳附录再由母任务并入共享合同，未改共享目录或全局矩阵。'),
 ('BIN-INPUT-MAPPING-DATA','控制器两组数据与逻辑输入',['BIN-C12'],'只做数据解码/与外部八别名连接；未推定实际表优先级。')]:
 shared.append({'id':sid,'unique_capability_identity':sid,'title':title,'capabilities':cc,'consumer_modules':['M10','M12','M03'],'consumer_projection':lim,'source_to_spec_ref':'source-to-spec.json#/capabilities','status':'partial','support_boundary':'supported_static_interface_with_named_unknowns','execution_status':'NOT_EXECUTED','counting_rule':'一份接口身份，多消费者投影；不按函数/字符串/纹理变体重复计功能。'})
emit('shared-interfaces.json',{'interfaces':shared,'unknowns':unknowns,'existing_candidates_evidence_only':['GR5-M10-012','GR5-M10-013'],'feature_matrix_write':'仅BIN本地投影；没有改共享总表。'})
print('consumers',len(cons),'capabilities',len(caps),'forward records',len(functions),'reverse anchors',len(reverse))
