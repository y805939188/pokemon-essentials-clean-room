import datetime, hashlib, json, pathlib, subprocess
ROOT = pathlib.Path(__file__).parent
R = pathlib.Path('/workspace/pokemon-essentials')
B = pathlib.Path('/workspace/pokemon-essentials-clean-room')
SOURCE = 'Data/Scripts/010_Data/001_Hardcoded data/012_Weather.rb'
DISPLAY = 'Data/Scripts/012_Overworld/001_Overworld visuals/001_Overworld_Weather.rb'
SCREEN = 'Data/Scripts/004_Game classes/001_Game_Screen.rb'
GLOBAL = 'Data/Scripts/005_Sprites/006_Spriteset_Global.rb'
WP59 = 'deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md'
WP16 = 'deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md'
facts = []
def add(key, assertion, path, lines, spec, consumer, premises='固定R默认脚本、无外部覆写；宿主请求正常的有限静态前提'):
    facts.append(dict(id=key, assertion=assertion, source=dict(path=path, lines=lines), spec=spec,
                      consumers=consumer, premises=premises, evidence='SOURCE_STATIC', execution='NOT_EXECUTED'))
records = [
 ('None',0,'None',[],[],[0,0,0],[0,0],[0,0,0,0],[65,68]),
 ('Rain',1,'Rain',['rain_1','rain_2','rain_3','rain_4'],[],[-600,2400,0],[0,0],['−s/2','−s/2','−s/2',10],[70,80]),
 ('Storm',2,'Rain',['storm_1','storm_2','storm_3','storm_4'],[],[-3600,3600,0],[0,0],['−3s/4','−3s/4','−3s/4',10],[83,93]),
 ('Snow',3,'Hail',['hail_1','hail_2','hail_3'],[],[-240,240,0],[0,0],['s/2','s/2','s/2',0],[96,106]),
 ('Blizzard',4,'Hail',['blizzard_1','blizzard_2','blizzard_3','blizzard_4'],['blizzard_tile'],[-720,240,0],[-1200,600],['3s/4','3s/4','3s/4',0],[108,120]),
 ('Sandstorm',5,'Sandstorm',['sandstorm_1','sandstorm_2','sandstorm_3','sandstorm_4'],['sandstorm_tile'],[-1200,640,0],[-800,400],['s/2',0,'−s/2',0],[122,134]),
 ('HeavyRain',6,'Rain',['storm_1','storm_2','storm_3','storm_4'],[],[-3600,3600,0],[0,0],['−3s/4','−3s/4','−3s/4',10],[136,146]),
 ('Sun',7,'Sun',[],[],[0,0,0],[0,0],[64,64,32,0],[149,156]),
 ('Fog',8,'Fog',[],['fog_tile'],[0,0,0],[-32,0],[0,0,0,0],[158,165]),
]
for name,num,cat,particles,tiles,particle_speed,tile_speed,tone,lines in records:
    props={'numeric_id':num,'category':cat,'ordered_particle_resources':particles,'ordered_tile_resources':tiles,
           'particle_x_per_second':particle_speed[0],'particle_y_per_second':particle_speed[1],
           'particle_opacity_per_second':particle_speed[2], 'tile_x_per_second':tile_speed[0],
           'tile_y_per_second':tile_speed[1], 'tone_R':tone[0],'tone_G':tone[1],'tone_B':tone[2],'tone_gray':tone[3]}
    for field,value in props.items():
        add(f'WRR-WD-{name}-{field}', {'weather':name,'field':field,'value':value}, SOURCE, lines,
            [WP59+' §4.1 table/default table',WP16+' §5.1.1'],
            [DISPLAY+' prepare_bitmaps/get_weather_tone/particle and tile update'],
            '内置登记；未明示速度/色调按定义缺省；色调s为被传入的强度。负整数除法向下取整，非整数保留分数；媒体内容与像素未执行')
manual = [
 ('01','默认屏幕天气意图为None，强度0，duration0',SCREEN,[17,35],'§4.3','Spriteset_Global.update'),
 ('02','天气设置先以登记表验证身份并规范成符号；失败在后续强度/时长写入之前',SCREEN,[65,70],'§4.4','Interpreter.command_236'),
 ('03','power映射意图强度为(power+1)×60/10；合法整数0/9分别6/60',SCREEN,[65,70],'§4.4','Spriteset_Global.update'),
 ('04','时长原值保存在意图，设置入口本身没有天气过期计时',SCREEN,[65,70],'§4.3/4.4','Spriteset_Global.update'),
 ('05','整体显示更新仅比较天气类型，类型相同不交付上限或时长变化',GLOBAL,[33,38],'§4.3/4.5','RPG::Weather.fade_in'),
 ('06','淡入入口首先拒绝任何在途渐变的新请求',DISPLAY,[66,70],'§4.5','Spriteset_Global.update'),
 ('07','通过在途门后，天气身份验证发生在目标None上限归0之前',DISPLAY,[66,70],'§4.4','RPG::Weather.fade_in'),
 ('08','None目标上限归0；当前类型及上限同时不变才在入口内提前返回',DISPLAY,[66,70],'§4.5','RPG::Weather.fade_in'),
 ('09','仅正duration选择固定渐变，正值数值不参与阶段计时',DISPLAY,[71,95],'§4.4/4.5','RPG::Weather.update_fading'),
 ('10','duration非正且守卫已通过时依次设置类型和上限',DISPLAY,[92,95],'§4.4/4.5','RPG::Weather.type=/max='),
 ('11','显示上限setter将输入夹到0至60',DISPLAY,[121,128],'§4.5','ensureSprites'),
 ('12','旧类型None的阶段偏移为2',DISPLAY,[82,86],'§4.5','update_fading/update_screen_tone'),
 ('13','旧天气非None且无平铺的阶段偏移为1',DISPLAY,[82,86],'§4.5','update_fading/update_screen_tone'),
 ('14','旧平铺、旧色调、旧粒子阶段分别0–1、0–2、1–3',DISPLAY,[11,23],'§4.5','RPG::Weather.update_*'),
 ('15','新粒子、新色调、新平铺阶段分别2–4、3–5、4–5',DISPLAY,[11,23],'§4.5','RPG::Weather.update_*'),
 ('16','渐变累计Graphics.delta，独立于调用duration的大小',DISPLAY,[425,428],'§4.5','RPG::Weather.update'),
 ('17','更换平铺发生在旧色调阈值扣除阶段偏移并夹到0之后的跨越',DISPLAY,[429,445],'§4.5','update_fading'),
 ('18','旧粒子数衰减不立即强制各粒子隐藏，等待其自然重置时按新上限决定',DISPLAY,[446,452],'§4.5','reset_sprite_position'),
 ('19','新粒子数随阶段比例向下取整，并更新其可见资格',DISPLAY,[453,458],'§4.5','update_sprite_position'),
 ('20','完成同时要求名义阈值到达且旧粒子全部不可见',DISPLAY,[459,478],'§4.5','Spriteset_Global.update后续再次比较意图'),
 ('21','None→非None名义阈值5−2=3秒，仍受实际更新机会和旧粒子门约束',DISPLAY,[82,86,459,478],'§4.4/4.5','update_fading'),
 ('22','渐变完成后显示类型及上限采用目标值，清在途状态并换成新粒子集合',DISPLAY,[459,478],'§4.5','Spriteset_Global.update'),
 ('23','雨类别奇数索引用末位水花资源，偶数索引循环其它资源',DISPLAY,[210,227],'§4.1','reset/update_sprite_position'),
 ('24','水花重置寿命离散抽0.30至0.49秒，步长0.01',DISPLAY,[239,252],'§4.1','update_sprite_position'),
 ('25','重置重新选屏幕范围位置并将透明度设255',DISPLAY,[249,252,271,272],'§4.1','update_sprite_position'),
 ('26','寿命本次到期先重置并返回，不执行同次普通隐藏判断',DISPLAY,[274,283],'§4.1','RPG::Weather.update'),
 ('27','非到期水花剩余寿命严格小于.2秒时255，否则0',DISPLAY,[285,290],'§4.1','RPG::Weather.update'),
 ('28','水花普通分支不执行普通粒子漂移',DISPLAY,[285,311],'§4.1','RPG::Weather.update'),
 ('29','普通粒子按数据每秒速率乘delta移动，透明度也按每秒速率推进',DISPLAY,[290,310],'§4.1/4.5','RPG::Weather.update'),
 ('30','Snow横向另加基础横移×相对纵坐标/(屏高×3)',DISPLAY,[295,298],'§4.1','RPG::Weather.update'),
 ('31','Snow横向扰动从2,1,0,−1均匀抽取后乘基础横移/8',DISPLAY,[295,298],'§4.1','RPG::Weather.update'),
 ('32','Snow纵向另按索引mod6取2,1,1,0,0,−1并乘基础纵移/10',DISPLAY,[295,298],'§4.1','RPG::Weather.update'),
 ('33','粒子低透明度、越左边或越底部会重置；其它方向先按屏宽高回绕',DISPLAY,[300,310],'§4.5','RPG::Weather.update'),
 ('34','仅稳定Storm进入随机白闪分支，HeavyRain和渐变期不进入',DISPLAY,[481,495],'§4.1','viewport.flash请求'),
 ('35','Storm下次间隔离散0.5至6秒，步长.5',DISPLAY,[492,494],'§4.1','viewport.flash请求'),
 ('36','Storm白闪请求RGBA255,255,255,230，持续参数40/60/80',DISPLAY,[485,490],'§4.1','viewport.flash请求；非最终像素'),
 ('37','Sun附加量每次按±s×delta/.8推进',DISPLAY,[411,419],'§4.1','weather viewport tone请求'),
 ('38','Sun只在旧附加量已超过上界或低于0后翻向，允许越界',DISPLAY,[411,419],'§4.1','weather viewport tone请求'),
 ('39','Sun附加强度分别加到R/G、其一半加到B',DISPLAY,[411,419],'§4.1','weather viewport tone请求'),
 ('40','跨图显示按相对位置累加以图块宽高换算的天气偏移',GLOBAL,[39,49],'§4.5','ox=/oy='),
 ('41','相对位置为0,0时偏移归0，当前显示原点按地图子像素量化为整数像素',GLOBAL,[39,51],'§4.5','ox=/oy='),
 ('42','平铺随delta和数据速率移动，并按贴图宽高回绕覆盖屏幕',DISPLAY,[314,358],'§4.5','RPG::Weather.update'),
 ('43','类型变化时预加载目标资源；直接缓存加载异常可发生在随后状态建立之前',DISPLAY,[66,95,150,160],'§4.5 boundary','RPG::Cache.load_bitmap'),
]
for num,text,path,lines,clause,consumer in manual:
    add('WRR-WS-'+num,text,path,lines,[WP59+' '+clause,WP16+' §5'],[consumer])
extra = [
 ('ENTER1','旧图ID为0或与当前相同时不重掷','Data/Scripts/012_Overworld/001_Overworld.rb',[240,253],'§4.3'),
 ('ENTER2','有效不同图通知默认新天气None；字段存在时取0–99样本严格小于概率才选登记天气','Data/Scripts/012_Overworld/001_Overworld.rb',[240,253],'§4.2/4.3'),
 ('ENTER3','结果与当前意图同类型时跳过；异类型写power9/duration0','Data/Scripts/012_Overworld/001_Overworld.rb',[240,253],'§4.3'),
 ('ENTER4','连接边缘先进入通知，正常返回后独立覆写duration20','Data/Scripts/004_Game classes/005_Game_MapFactory.rb',[93,112],'§4.3'),
 ('ENTER5','显式转移正常路径不执行连接边缘的duration20赋值','Data/Scripts/003_Game processing/002_Scene_Map.rb',[72,101],'§4.3'),
 ('DATA1','地图PBS天气格式是天气登记枚举加非负整数概率；该专属校验无概率上限','Data/Scripts/010_Data/002_PBS data/018_MapMetadata.rb',[33,58],'§4.2'),
 ('EDIT1','属性选择取消或选None均返回nil，不返回原值','Data/Scripts/020_Debug/002_Editor_DataTypes.rb',[860,883],'§4.2'),
 ('EDIT2','属性数值选择范围0–100；格式化nil显示短横','Data/Scripts/020_Debug/002_Editor_DataTypes.rb',[860,883],'§4.2'),
 ('EDIT3','属性设置返回值先写编辑缓冲，外层保存Yes才重建登记、存dat、写PBS','Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb',[787,817],'§4.2'),
 ('SAVE1','普通存档登记game_screen整个状态，读档重新赋全局screen；天气显示对象由新地图场景另建','Data/Scripts/002_Save data/004_Game_SaveValues.rb',[56,61],'§4.3 boundary'),
 ('SAVE2','v20天气转换仅在旧screen.weather_type整数0时改None','Data/Scripts/002_Save data/005_Game_SaveConversions.rb',[274,282],'§4.3 boundary'),
 ('CONS1','NoWeather进化读取具体None；Sun/Rain/Hail/Sandstorm进化读取类别，其中Rain接受Fog','Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb',[133,175],'§4.6'),
 ('CONS2','旧树果机制在有效正时间更新尾部按Rain类别浇水；新机制分支不执行这条浇水','Data/Scripts/012_Overworld/006_Overworld_BerryPlants.rb',[97,160],'§4.6'),
 ('CONS3','SnowCloak在Hail类别减半遇敌率并加倍最小步；SandVeil对Sandstorm同理，特定持物分支优先','Data/Scripts/012_Overworld/002_Battle triggering/003_Overworld_WildEncounters.rb',[102,182],'§4.6'),
 ('CONS4','battle规则未指定defaultWeather时按世界类别设置独立battle天气；指定时用指定规则','Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb',[249,263],'§4.6'),
 ('CONS5','defaultTerrain未指定且配置允许时Storm映Electric、Fog映Misty；这不是同名天气身份传递','Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb',[236,248],'§4.6'),
]
for key,text,path,lines,clause in extra:
    add('WRR-WX-'+key,text,path,lines,[WP59+' '+clause],['数据/进入/显示/保存/后续业务链，具体入口如assertion'])
paths = sorted({f['source']['path'] for f in facts})
ids=[]
for path in paths:
    raw=(R/path).read_bytes()
    ids.append(dict(repo=str(R),commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',tree='7589c800b61ba13a13040ed0d686979b80a84fd0',path=path,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),blob=subprocess.check_output(['git','hash-object',str(R/path)]).decode().strip()))
doc={'schema':'gr8-world-weather-shared-facts/v1','reviewer':'/root/world_resources_rendering','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'evidence_level':'SOURCE_STATIC / DERIVED_VECTOR','business_execution':'NOT_EXECUTED','atomic_fact_count':len(facts),'atomization':'Explicit behavioral/data fields and hand-written assertions. No method, semicolon or line-count denominator. Ordered resource lists are each one list-valued contract, not a media approval.','facts':facts,'source_identities':ids,'status':'OFFERED_FOR_WORLD_FULL_RECEPTION','open':['Compiler generic full parse helper reception','FieldMoves SweetScent owner reception','SaveData serializer/boot conversion owner reception','All receiving owners must explicitly acknowledge scope'],'excluded_claims':['full native host','pixels/audio/video observed','all scene consumers read by this agent','all WP59 outside shared weather subsection approved'],'update_status':'UPDATE_NOT_STARTED'}
(ROOT/'weather-shared-facts.json').write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
print(len(facts))
