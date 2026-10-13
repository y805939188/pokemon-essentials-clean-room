from record import *
from build_maps import A,anchors
S='Data/Scripts/'
def add(f,a,b,e,r,m,res='supported_static within this caller projection; other domain behavior not signed'):
 addsource(S+f,[(a,b,e,r,m,res)])
# These entries were read directly in this review; no inferred reading from search inventories.
add('999_Main/999_Main.rb',1,60,'all main entrypoints','debug关键段包装与非debug直调；插件/编译/初始/系统/标题；超时仅非debug先打印，两模式紧急保存后重抛；包装普通返回后主入口恒1','wp09 §4.1; wp10 §5.3; wp07 §5; GR5-M02-005')
add('016_UI/013_UI_Load.rb',204,356,'load controller lifecycle','存在主档才读取；有效性假递归bak；缺备份可删除，拒绝exit；删除失败系统/选项仍重建；三跳屏门；语言直写默认主档','wp09 §4–5; wp10 §5; wp65 §3')
add('016_UI/014_UI_Save.rb',1,139,'emergency and save UI','紧急场景置空无玩家早退；旧档才复制；成功恒两提示；保存询问及新游戏覆盖确认，先清begun_new_game再保存；显示读取playtime','wp10 §5.2; wp65 §4; GR3-M02-003 NO_REQUIRED')
add('003_Game processing/002_Scene_Map.rb',155,196,'map updates/title entry','通知在图更新后；回标题标记非启动/强制新游戏重置项未加载，再换标题','wp09 §3.1/4.1; wp05 §3.3')
add('003_Game processing/002_Scene_Map.rb',220,252,'main termination/title','场景变更后冻结释放；回标题才清游戏时间锚点','wp06 §3.1/TM04')
add('012_Overworld/001_Overworld.rb',1,215,'frame/step handlers','已读pokerus日期降次/低电量门/延迟BGM，步效果顺序、soot净增长；普通stepcount按2^31回绕且先于通知，强制/解释器早退不加','wp05 §3.3/EP26–27; wp06 §4.1/TM12; WP61/WP15消费者边界')
add('012_Overworld/001_Overworld.rb',222,238,'setup_new_map','进入首消费可记治疗点，再清局部记录、重设遭遇、记已访问','wp09 §4.1; WP11 §6/U02-SV-WORLD01–02')
add('012_Overworld/002_Overworld_Metadata.rb',1,183,'global/map metadata','global初值与遭遇版本change只变值才setup；map clear与updateMap门分层、through在图门外','wp09 table; wp06 §6; WP11 §6')
add('012_Overworld/003_Overworld_Time.rb',1,309,'clock/calendar/tone all entries','时段半开区间；30秒uptime缓存与墙钟分钟插值；星期月季节写变量；季节mod4；月相实际小时×60及负相位；星座7/21–22默认0','wp06 §3.1–3.3/TM01,14; wp59 §3.1–3.6')
add('013_Items/004_Item_Phone.rb',1,308,'phone storage/add/timing/contacts','global持久电话；refresh同秒去重每次-1；启动默认不再战；类包装指运行global；隐形联系人跳过查重；缺Phone.get由现行WP63已承接','wp06 §3.2/TM02–03; wp10 phone row; wp63 §4')
add('013_Items/004_Item_Phone.rb',516,560,'phone frame consumer','有工具且不在菜单/战斗/消息/强制路线/解释器才调用再战刷新并扣Graphics.delta来电','wp06 §3.2/TM02–03')
add('013_Items/004_Item_Phone.rb',562,706,'deprecated phone functions','18入口每次先warn(v22)，再转发各原目标；缺操作或参数失配不被告警兼容承诺消除','wp07 deprecation §5; wp63 §4.6; no whole-phone signoff')
add('012_Overworld/008_Overworld_RandomDungeons.rb',415,454,'seed selection/generate','参数种子优先待播种子，再newseed；无条件清待播；播种先于负尺寸早退','wp06 §5.2/TM06')
add('017_Minigames/005_Minigame_Lottery.rb',1,46,'lottery','日+32月+512年播种，抽0..65535后重新播种不恢复旧随机；变量写入和直接结果写的区别','wp06 §5.1/TM05; wp70 §2/5')
add('011_Battle/008_Other battle types/005_RecordedBattle.rb',1,287,'record/playback','五元组与18属性；真实取样后追加，回放索引取既有值无界限重抽；记录属性/重建依赖来源','wp06 §5.3/TM07; wp58 §3/5/6')
add('004_Game classes/005_Game_MapFactory.rb',1,46,'initialize/setup/map','setup清集合，新图初始0，旧图非0触离开；setup+邻图后进入；当前索引回退首图或无图错误','wp09 §4.1; WP11 §6')
add('004_Game classes/005_Game_MapFactory.rb',125,153,'map enter/leave notify','enter通知正常才mapChanged=true；同ID重建仍经过离开门；mapChanged只投影显示通知','wp09 §4.1; WP11 §6/U02-SV-WORLD')
add('004_Game classes/004_Game_Map.rb',1,64,'initial map identity/setup','新地图map_id=0；设置时载入地图，通知先于事件集合创建','wp09 load_map recovery; WP11')
add('016_UI/015_UI_Options.rb',1,34,'PokemonSystem defaults','13选项默认：文字1、动画/风格/送箱/昵称/框/皮肤/语言/跑步/输入0，音乐80/音效100，窗口floor(scale×2)-1','wp09 pokemon_system; wp65 §5.2')
add('012_Overworld/006_Overworld_BerryPlants.rb',1,74,'berry state initialization','reset基准水100及零字段/空身份；提供迁移新对象未填字段默认','wp10 berry conversions; wp60 §3')
add('012_Overworld/007_Overworld_DayCare.rb',259,342,'daycare slot defaults','两个槽；默认空、初始级0；filled仅非nil；等级差当前减初始，迁移直接设置不走deposit治疗','wp10 daycare conversion; MG09; wp33')
add('004_Game classes/011_Game_FollowerFactory.rb',1,60,'FollowerData and legacy field','映射位置/图/朝向/外观，默认可见；deprecated old field仍可读供迁移，followers懒建','wp10 follower conversion; WP13 boundary')
add('018_Alternate battle modes/002_Battle Frontier rules/002_Challenge_Rulesets.rb',110,191,'combination consumers','多个存在性查询使用指定大小索引组合，首合法即返回；短列表零产出','wp54 §2.2; general utility combination')
add('021_Compiler/001_Compiler.rb',72,91,'prepline','行尾#及外侧空白清理，插件metadata调用者采用该预处理','wp05 §5.1; WP04 parser M01')
add('021_Compiler/001_Compiler.rb',195,250,'line preparation helpers','初行BOM检测、UTF8标记、去注释空白再逐非空行输出位置；短行宿主取字符异常不被plugin元数据error改写','wp05 meta input projection; WP04')
add('021_Compiler/001_Compiler.rb',503,528,'deprecated csv prefix','调用旧csv入口先弃用告警；其余完整parser归M01','wp07 deprecation audit')
add('021_Compiler/001_Compiler.rb',1084,1117,'compiler failure propagation','reset/exit重抛；其他诊断后尝试清缓存，超时转reset否则新通用错','wp07 §5.1/IO11; WP04 §3.2')
add('001_Technical/003_Intl_Messages.rb',524,545,'message default read','只签pbRgssOpen文件接口消费者；数组校验/错误复位在消息层，WP08 M01不全签','wp07 file shared interface; WP08 boundary')
for f,a,b,n,r in [
('014_Pokemon/001_Pokemon.rb',308,329,'type1/type2','每次warn后返回首类型/次类型或首类型'),('014_Pokemon/004_Pokemon_Move.rb',58,75,'base_damage','warn后返回存储power，不据名字等同动态数据委托'),('010_Data/002_PBS data/005_Move.rb',51,66,'base_damage','warn后power'),('011_Battle/003_Move/001_Battle_Move.rb',19,34,'baseDamage','warn后power'),('007_Objects and windows/010_DrawText.rb',39,72,'5 color wrappers','分别warn(v22)后原颜色转换；完整颜色渲染不签'),('020_Debug/001_Editor screens/003_EditorScreens_MapConnections.rb',554,578,'pbConnectionsEditor','关键段包装场景/尺寸更改；失败时后段尺寸恢复不保证，wrapper结果可返回'),('009_Scenes/002_EventScene.rb',177,192,'pbEventScreen','普通异常报告正常后局部包装外viewport.dispose可继续；非StandardError或诊断失败不保证')]:add(f,a,b,n,r,'wp07 diagnostics/deprecation; bounded owner projection')
add('001_Settings.rb',1,20,'versions/generation','游戏1.0.0，规则代8','wp09/wp10 version output')
add('001_Settings.rb',67,75,'time setting','TIME_SHADING true','wp06 §3')
add('001_Settings.rb',235,248,'flute migration setting','等级笛子开关由gen>=6（当前真）','wp10 flute conversion')
add('001_Settings.rb',343,353,'phone settings','再战默认false','wp06 phone timing')
add('001_Settings.rb',418,444,'languages/scale','默认语言空列表；屏幕512×384，scale1.0','wp09 startup; wp65 screen settings')
add('001_Settings.rb',509,524,'debug skip/version constants','跳continue默认false；Essentials21.1、ERROR_TEXT空、宿主版本2.4.2/c9378cf','wp05/wp07/wp09/wp10')
# Explicitly inventory adjacent domain files; never claim full utility-directory audit.
for f,why in [('019_Utilities/002_Utilities_Pokemon.rb','Only function inventory: acquisition/naming/storage/egg/balanced-level/size/species breeding, owned by creature reviewers.'),('019_Utilities/003_Utilities_BattleAudio.rb','Only function inventory: battle BGM/victory/capture/intro selectors, owned by audio/combat reviewer.')]:
 p=R/S/f;n=len(p.read_text().splitlines());source(S+f,[],'inventory_only',[[1,n]],why)
# Source-only reviews are complete as reviews, not claims that every behavior is specified.
p=P/'reading-coverage.json';d=json.loads(p.read_text())
main_prefixes=['Data/Scripts/001_Technical/001_Debugging/','Data/Scripts/001_Technical/002_Files/','Data/Scripts/002_Save data/','Data/Scripts/004_Game classes/001_Switches and Variables/']
full_paths=[S+'001_Technical/005_PluginManager.rb',S+'003_Game processing/001_StartGame.rb',S+'003_Game processing/005_Event_Handlers.rb',S+'003_Game processing/006_Event_HandlerCollections.rb',S+'004_Game classes/012_Game_Stats.rb']
scoped_primary={S+'001_Technical/002_RubyUtilities.rb':[[1,34],[54,129],[141,171],[335,406]],S+'001_Technical/001_MKXP_Compatibility.rb':[[1,10],[30,48]],S+'004_Game classes/002_Game_System.rb':[[1,40],[274,287]],S+'019_Utilities/001_Utilities.rb':[[1,47],[63,192],[281,283],[429,520]]}
for x in d['sources']:
 path=x['path'];n=x['line_count']
 if any(path.startswith(t) for t in main_prefixes) or path in full_paths:
  x['review_extent']='full';x['owned_ranges']=[[1,n]];x['unreviewed_intervals']=[];x['review_scope_kind']='primary'
 elif path in scoped_primary:
  x['owned_ranges']=scoped_primary[path];x['review_scope_kind']='primary_mixed_file';x['review_extent']='partial'
  in_scope=set(i for a,b in x['owned_ranges'] for i in range(a,b+1));missing=[i for i in range(1,n+1) if i not in in_scope];rr=[]
  for i in missing:
   if rr and rr[-1][1]==i-1:rr[-1][1]=i
   else:rr.append([i,i])
  x['unreviewed_intervals']=rr;x['unreviewed_reason']='outside M02 primary semantic ownership; source-read/domain projections may exist but not full foreign-domain signoff'
 else:
  x['review_scope_kind']='necessary_caller_projection' if x['segments'] else 'outside_assignment_inventory'
 x['source_read_intervals']=[s['lines'] for s in x['segments']]
 x['evidence_level']='static_semantic_comparison' if x['review_scope_kind'] in ['primary','primary_mixed_file'] else x['evidence_level']
 x['semantic_comparison_complete_for_owned_ranges']=x['review_scope_kind'] in ['primary','primary_mixed_file']
 for seg in x['segments']:
  old=seg['comparison_result']
  if 'pending' in old:
   seg['comparison_result']='completed_source_and_current_contract_comparison; see final capability mapping for supported_static/partial/unresolved distinction; no runtime conclusion'
  if '002_Save data/005_Game_SaveConversions.rb' in path and seg['lines'][0]<142:seg['comparison_result']='partial contract: GR5-M02-004 candidate; other registration/version gates supported_static'
  if path.endswith('001_FileTests.rb') and seg['lines'][0]>=363:seg['comparison_result']='source semantics complete; current contract gap candidate GR5-M02-003'
  if path.endswith('005_Event_Handlers.rb') and seg['lines'][0]==143:seg['comparison_result']='query and copy supported_static by WP05/WP28/WP21; removal/clear gap candidate GR5-M02-002'
  if path.endswith('003_Errors.rb') and seg['lines'][0]==76:seg['comparison_result']='signals supported_static; completion/caller gap candidate GR5-M02-005'
 d['primary_scope_definition']='All available M02 generic-kernel source text in discovered primary files/ranges. Mixed-file non-kernel and WP08 portions explicitly excluded, not signed. full means substantive review completed, not perfect specification coverage.'
d['material_gaps']=[]
for f in ['Plugins','Game.rgssad','Game.rxdata','Game.ini','Data/System.rxdata','Data/CommonEvents.rxdata','Data/MapInfos.rxdata','Data/Tilesets.rxdata','Data/Animations.rxdata','Data/Scripts.rxdata']:
 q=R/f;d['material_gaps'].append({'path':f,'version':RV,'material_availability':'available_binary' if q.is_file() else 'absent','review_extent':'unread' if q.is_file() else 'unreadable','evidence_level':'availability_only','unreviewed_intervals':'all binary content or absent material','reason':'No binary deserialization/reference/model/host execution authorized; readable script conditional behavior reviewed separately.'})
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('Source records:',len(d['sources']),'primary files:',sum(x['review_scope_kind'] in ['primary','primary_mixed_file'] for x in d['sources']))
