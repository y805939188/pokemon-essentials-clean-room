import json, subprocess, re
from pathlib import Path
from collections import Counter
P=Path(__file__).parent
R=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
B='1f36475d22120a0d1175967d5b17d71fe8311d88'; RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
reviewer='M12 / thread 01a12ffe-6148-76d0-8038-a1eb8e8bf390'
F=Path('deliverables/final-specification-set')
S={}
for code,pattern in [('72','demo-dx/wp72-*.md'),('73a','demo-dx/wp73-a-*.md'),('73b','demo-dx/wp73-b-*.md'),('74','demo-dx/wp74-*.md'),('75','demo-dx/wp75-*.md'),('76','demo-dx/wp76-*.md'),('77','demo-dx/wp77-*.md'),('04','generic-kernel/wp04-*.md'),('09','generic-kernel/wp09-*.md'),('36','creature-rpg/wp36-*.md'),('43','pokemon-rules/wp43-*.md'),('45','combat-requirements/wp45-*.md'),('65','user-interface/wp65-title-*.md')]:
 S[code]=str(next(F.glob(pattern)))
S.update({'tests':str(F/'test-catalog/demo-dx-wp72-73-74-75-76-77.md'),'readme':str(F/'README.md'),'scope':str(F/'scope-statement.md'),'testreadme':str(F/'test-catalog/README.md')})
A={
 'menu':'Data/Scripts/020_Debug/003_Debug menus/001_Debug_Menus.rb',
 'cmd':'Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb',
 'extra':'Data/Scripts/020_Debug/003_Debug menus/003_Debug_MenuExtraCode.rb',
 'effects':'Data/Scripts/020_Debug/003_Debug menus/006_Debug_BattleExtraCode.rb',
 'rename':'Data/Scripts/020_Debug/003_Debug menus/008_Debug_FilenameUpdater.rb',
 'edit':'Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb',
 'terrain':'Data/Scripts/020_Debug/001_Editor screens/002_EditorScreens_TerrainTags.rb',
 'connect':'Data/Scripts/020_Debug/001_Editor screens/003_EditorScreens_MapConnections.rb',
 'sprite':'Data/Scripts/020_Debug/001_Editor screens/004_EditorScreens_SpritePositioning.rb',
 'util':'Data/Scripts/020_Debug/001_Editor_Utilities.rb',
 'animscene':'Data/Scripts/020_Debug/002_Animation editor/001_AnimEditor_SceneElements.rb',
 'animio':'Data/Scripts/020_Debug/002_Animation editor/004_AnimEditor_ExportImport.rb',
 'animfunc':'Data/Scripts/020_Debug/002_Animation editor/005_AnimEditor_Functions.rb',
 'player':'Data/Scripts/011_Battle/007_Other battle code/007_BattleAnimationPlayer.rb',
 'play':'Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb',
 'compiler':'Data/Scripts/021_Compiler/001_Compiler.rb',
 'compile':'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb',
 'write':'Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb',
 'convert':'Data/Scripts/021_Compiler/004_Compiler_MapsAndEvents.rb',
 'gen':'Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/001_ChallengeGenerator_Data.rb',
 'genpk':'Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/002_ChallengeGenerator_Pokemon.rb',
 'gentr':'Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/003_ChallengeGenerator_Trainers.rb',
 'gensim':'Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/004_ChallengeGenerator_BattleSim.rb',
 'challenge':'Data/Scripts/018_Alternate battle modes/001_Battle Frontier/001_Challenge_BattleChallenge.rb',
 'btdata':'Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb',
 'load':'Data/Scripts/016_UI/013_UI_Load.rb',
 'saveui':'Data/Scripts/016_UI/014_UI_Save.rb',
 'start':'Data/Scripts/003_Game processing/001_StartGame.rb',
 'save':'Data/Scripts/002_Save data/001_SaveData.rb',
 'main':'Data/Scripts/999_Main/999_Main.rb',
 'scene':'Data/Scripts/003_Game processing/002_Scene_Map.rb',
 'pause':'Data/Scripts/016_UI/001_UI_PauseMenu.rb',
 'enc':'Data/Scripts/010_Data/002_PBS data/013_Encounter.rb',
 'metrics':'Data/Scripts/010_Data/002_PBS data/010_SpeciesMetrics.rb',
 'misc':'Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb',
 'town':'Data/Scripts/010_Data/002_PBS data/002_TownMap.rb',
 'type':'Data/Scripts/010_Data/002_PBS data/003_Type.rb',
 'trainer':'Data/Scripts/015_Trainers and player/002_Trainer_LoadAndNew.rb',
 'encuse':'Data/Scripts/012_Overworld/002_Battle triggering/003_Overworld_WildEncounters.rb',
 'meta':'Data/Scripts/012_Overworld/002_Overworld_Metadata.rb',
 'file':'Data/Scripts/001_Technical/002_Files/001_FileTests.rb',
 'rubyutil':'Data/Scripts/001_Technical/002_RubyUtilities.rb',
 'gamedata':'Data/Scripts/010_Data/001_GameData.rb',
 'damage':'Data/Scripts/011_Battle/003_Move/003_Move_UsageCalculations.rb',
 'sports':'Data/Scripts/011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb',
 'settings':'Data/Scripts/001_Settings.rb'
}
def src(k,l,f): return {'path':A.get(k,k),'commit':RC,'lines_or_symbol':l,'fact':f}
def spec(k,l,f='本次核对条款'): return {'path':S.get(k,k),'commit':B,'lines_or_symbol':l,'fact':f}
def dump(name,data): (P/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
caps=[]
def cap(n,desc,source,formal,entry,branches,reason,not_checked,status='supported',evidence='SOURCE_STATIC',history=None,classification=None,owner='M12'):
 caps.append({'capability_id':f'GR4-CAP-M12-{n:03d}','module':'M12','description':desc,'source_anchors':source,'spec_anchors':formal,'entry_and_preconditions':entry,'configuration_data_host_limits':'固定R；默认机制世代8。未补地图/Graphics/Audio/宿主；人工夹具与当前PBS样本分开，详见material-availability.json。','reviewer':reviewer,'checked_branches_boundaries':branches,'evidence_level':evidence,'material_availability':{'reference_source':'available','configuration_and_PBS':'available; selected semantic samples only','host_and_complete_demo':'unavailable','details':'material-availability.json'},'status':status,'reason':reason,'related_findings':['GR4-M12-001'] if n==5 else [],'history_links':history or [],'not_checked':not_checked,'classification':classification or ['Demo / Developer Experience'],'primary_owner':owner,'projection':'本域作者工具/完整流程投影；不重新裁决相邻域完整合同'})
cap(1,'调试入口、受限可见性、层级返回与描述求值', [src('menu','69–146;152–178;184–258;346–405','受限只排显式false，父菜单可达性与usage筛选独立；描述只在构造清单求值'),src('load','281–309;344–345','跳继续三门与Debug出现单一调试门分开'),src('scene','190–209','F9请求受调试及地图请求门约束'),src('pause','290–302','暂停Debug条件为调试')],[spec('72','§3.1–3.2'),spec('65','§3.2/§6.1'),spec('tests','DG-M01–M04/DG-M24')],'已进入合法菜单上下文；无额外插件条件', ['调试真/假','受限父级删除而工具三组保留','根退出与返回父级','普通效果返回值与warp/个体关闭区别'],'supported_static，仅具名入口与筛选链；没有证明玩家Demo入口。',['队伍/存储所有调用点未逐项复读','全部调试命令效果未穷尽'])
cap(2,'高级测试战斗构造先生成/加载，取消不撤回先行副作用',[src('cmd','276–477','普通野生等级取消0；高级加入时已生成/加载并触发训练家加载事件；开战前三拒绝门')],[spec('72','§7.1–7.2/§10'),spec('tests','DG-M18')],'具备玩家、正常生成/训练家数据与战斗环境',['普通等级0/正数','空集合','2训练家1席/1家1成员2席拒绝','加入后BACK'],'supported_static；测试入口调用正常战斗，不构成沙盒。',['完整生成钩子和战斗结算','未知/超3人数消费失败的全部路径'])
cap(3,'战斗效果编辑的数值/引用边界与世代标记消费',[src('effects','60–178;215–245;252–452','成员/场字段独立登记，-2显示归一-1，成员列表跳空与RIGHT搜索无尾界'),src('sports','696–744','正常玩泥巴/玩水按世代6分界写成员布尔或场计时'),src('damage','353–369','两个来源独立除3，不在伤害读取再互斥'),src('settings','17','默认世代8')],[spec('72','§7.5/§13 E046/E081/E088/E114/E117'),spec('43','§5 威力侧水火抑制（line123）'),spec('45','§5 MudSportField/WaterSportField')],'合法在场/场效果记录；尾空洞为人工边界',['默认8与5/6正常写入差异','人工两来源同时置位叠乘','-2与-1显示','空引用与候选列表不是同一守卫'],'supported_static；反证查得WP43已承接双来源叠乘，不新开缺项。',['120项逐项与所有战斗消费者全核','实际UI颜色/卡住运行'])
cap(4,'内容编辑的即时与退出保存及嵌套类型反写',[src('edit','345–442;478–598','类型即时登记/存档/反写；训练家改键先覆盖后删，外层No重载；嵌套新类型立即写PBS'),src('trainer','12–68;98–105','交互首只必选；新建save_changes=false；转换同时写两训练家PBS')],[spec('73a','§2/§4.1–4.2/§6'),spec('tests','CE-M03–M08')],'已有合法训练家；比较只用已有类型与嵌套新建类型',['改键撞已有目标','外层取消但PBS已有前缀','版本0–255满','首只取消强制重选与后续取消可跳该次'],'supported_static，已读保存/反写链与冲突门。',['全部属性类型与复合别名','物种/图鉴编辑器全部分支','新训练家图像与命名宿主'])
cap(5,'遭遇整集复制与空类型的结构差异',[src('edit','69–99;139–154;187–234;256–339','整集复制全部步数率但跳过空类型；单类型复制始终建立目标类型；正常新类型可零槽返回'),src('enc','62–68','初始化直接接收概率和类型，不补回遗漏键'),src('gamedata','78–85','登记只建立记录')],[spec('73b','§6.1 line73/§6.2 line80'),spec('tests','WE-M11 line85')],'有合法地图列表、目标图版本空闲；正常UI新增Land后不加槽返回再Copy',['非空槽独立复制正例','零槽Land整体复制丢类型但概率21保留','同集空Land复制到另一类型保留空类型','当前快照/文件保存另门'],'partial：正常复制与独立性准确，零槽类型过滤与概率残留没有明确承接，WE-M11深拷贝预期过宽。',['实际UI及文件执行'],'partial')
cap(6,'遭遇编辑到档案/PBS再编译及当前地图快照',[src('edit','111–120;281–286','保存档案再反写/取消重载；允许率0'),src('write','403–442','只输出非空类型；零率省略第二字段'),src('compile','658–741','省略率使用默认'),src('encuse','7–35','setup拷贝表且仅重置宽限'),src('meta','114–119','同版本早退，异版且上下文存在才setup')],[spec('73b','§6.4–6.5'),spec('04','§5.5 line164 遭遇概率往返'),spec('tests','WE-M12–M13')],'Land/OldRod各有合法非空槽，成功写出/重编译；初始快照21',['Land0→档案0→PBS省略→编译21','OldRod0→0','Land70保留','同版本不刷新，异版重装宽限4→0/累加210保持'],'supported_static，三层和快照边界均有承接。',['触发概率整套算法','真实切图、编译与文件故障'])
cap(7,'连接编辑的单轴邻接、0/1图早退与取消重载对象',[src('connect','193–285;470–578','0/1图保留旧边；至少2图删除触及画布旧边后重建；孤点回退；取消只Encounter.load')],[spec('73b','§3.2–3.3'),spec('tests','WE-M03–M06')],'地图尺寸和画布精灵合法',['错轴邻接(0,0)/(40,400)','两对有邻居不跨组','删至一图旧边全留','连接不保存不撤销已保存地图元数据'],'supported_static；不把连接生成当通行证明。',['缩略图/拖拽视觉','连接实际跨图消费全路径'])
cap(8,'地形标签整组、稀疏编号与保存后的共享运行数据',[src('terrain','1–74;158–169;190–263','自动图块48整组；比较序号与旧ID；保存后运行数据共享会话')],[spec('73b','§5'),spec('tests','WE-M08–M09')],'可加载Tilesets；默认标签连续，0/2/5为人工配置',['384分界','稀疏旧2选序号2(值5)被跳过','首次No不写','保存B后改C再No：档案B运行C'],'supported_static；素材与宿主恢复未知。',['实际宿主关闭/重新打开','坏Tilesets形状、全部导航'])
cap(9,'指标自动定位与输出路径取保存时非零形态后缀',[src('sprite','4–41;91–165;167–221;338–411','透明图底0、缺图全量跳位置但仍重置其它值；单体直接取高；浏览可查询建态'),src('metrics','32–80','非零形态惰性复制基础且后缀默认空，布局偏移乘2'),src('write','291–347','非零形态决定输出路径，等值形态省行')],[spec('73b','§7.1–7.5'),spec('tests','WE-M18–M20/B19-C016')],'合法物种、明确指标记录集合和图像可得性',['32高底24→背3/正7，全透明→15/19','仅基础记录无路径','非零等值选择路径但省节','档案已保存后PBS失败不回滚'],'supported_static，仅所列编辑/写出合同。',['全量pokemon_metrics内容样本','所有显示者与已布局精灵的重定位入口'])
cap(10,'动画集合缓存、临时新建与组织器保存0项',[src('misc','39–52','动画缓存优先/映射缓存分开'),src('animfunc','996–1002;1157–1170','保存与退出双门；缺首槽临时建集合'),src('edit','1252–1324','组织器拒空首槽，删除无最少1项门，Yes保存清缓存/No不清'),src('player','334–390','容量缩短后游标可等于新长度')],[spec('74','§3.1–3.2/§7.1/§12/§16'),spec('tests','AN-M01/AN-M26/AN-M33')],'明确缓存nil/首槽空/有效三态',['首次保存后另读与编辑对象分离','空首槽缓存保存前后仍复用旧缓存','组织器一项删至0','不保存退出和No继续分开'],'supported_static，缓存失效只影响后续读者。',['实际窗口索引导航与完整列表操作','异常清理/屏幕恢复'])
cap(11,'动画帧复制的独立性与区间清除守卫',[src('animscene','47–63;566–694','剪贴快照；插入帧浅副本；区间copy只0–59；删除守卫读当前帧'),src('player','450–471;592–665;767–842','新帧双个体、常规渲染0–59、可见标志')],[spec('74','§4.4–4.5/§6.1–6.3/§8.1–8.2'),spec('tests','AN-M07/AN-M13–M14')],'多帧动画及具名当前帧/目标帧',['Insert属性联动但槽删独立','Copy/Paste属性独立','当前空槽允许清除目标锁定槽','第60槽可存但渲染跳过'],'supported_static；不把复制/插入/清除混成统一深拷贝。',['补间和曲线完整数学','鼠标命中、颜色预览、全部控件'])
cap(12,'单项/批量动画交换、资源复制先后与分配截断',[src('animio','11–145','单项压缩文本解码/类型检查/缺图警告/旧焦点转换'),src('extra','553–663','导出整体保护与无确认覆盖；导入资源先拷贝再解码，仅解码局部保护'),src('util','16–61','安全复制比较与固定长度10分配'),src('file','195–242;262–272','文件解析及当前仅项目路径')],[spec('74','§11–§14/§16'),spec('73a','§5'),spec('tests','AN-M24–M28')],'合法本地交换目录/动画与失败时点明确',['无目录不写','坏anm仍可能已复制资源','.midi末三字筛选不命中','12非空项分配截10返回12','A-B/A+B导出重名覆盖'],'supported_static；未执行反序列化/交换；多RTP非当前默认。',['真实.anm样本兼容/解码安全','其它扩展名与第三方宿主资源路径'])
cap(13,'预览时序的共享旧值、实际帧访问与渐变坐标',[src('player','474–586;753–842','先活动渐变再起始项；同层共享旧值；时间×20跳帧不补发；位置原点反向'),src('animscene','451–510','预览交给同一播放器，临时精灵/视角')],[spec('74','§10.1–10.3'),spec('tests','AN-M23/B20-C026')],'合法动画长度、时序参数和指定帧访问',['X10到目标20中点25/终点40','d0只捕获无活动帧','后启动项覆写同层旧值','跳过起始帧不补捕获'],'supported_static；数值为手工推导，非屏幕观察。',['渲染像素量化','音频播放','未访问起点后所有异常组合'])
cap(14,'动画命名供应、映射重编译与播放精确消费',[src('compile','1274–1321','每轮空映射；有效名则写，零有效保留旧文件；同侧后槽覆盖'),src('play','418–455;492–518','对手映射回退，Common直接拼接精确比较')],[spec('74','§15'),spec('tests','AN-M29')],'合法招式ID及既有映射',['Move冒号后前导空白消耗/尾随保留','同名后槽覆盖','最后有效名删除后旧映射仍在','Common:X和Common: X不同'],'supported_static，名称兼容不是未来API要求。',['完整按类型默认动画表','实际战斗素材播放'])
cap(15,'工程转换的调试触发、训练家注释词法和部分写出',[src('convert','45–82;441–635;771–844;1683–1751','Map999跳过；CommonEvent收集/解析不对称；道具球重命名；门先重注册；逐图保存/公共事件阶段'),src('compiler','967–1037','顶层PBS发现、编译动画后转换再文本收集')],[spec('75','§3–§7.2/§10'),spec('tests','CV-M01/CV-M05–M06/CV-M09/CV-M24')],'合法工程宿主数据；未执行地图转换',['非调试不导入','有效Battle必要；独立CommonEvent不被收集','道具未知不转换','门结构失败前可能已有开关变化','后图异常不撤回前图'],'supported_static，仅所读家族/阶段；无地图实际事件证据。',['旧战斗六族/文本分页/柜台合并完整重审','所有生成页与事件解释器联合运行'])
cap(16,'脚本归档提取/合并数量门、非互逆内容和破坏性步骤',[src('scripts_extract.rb','12–67;76–179;182–183','9/10/11方向门；先清树，后备份再装载器；正文CR丢失、空正文不写；合并重新聚合'),src('scripts_combine.rb','182–183;其余与extract比较相同','仅激活方向不同'),src('README.md','15–30','散文件加载与往返使用文档')],[spec('75','§3.3/§12'),spec('tests','CV-M26–M27')],'合法归档或目录；数量门不是状态标签',['提取9拒10/11过，合并9/10过11拒','清树后输出失败未到备份','字面实体与非ASCII不保证还原','文件在前再子目录，递归无上限'],'supported_static；脚本未运行/装载器未解包。',['真实归档解析与合并/提取执行','编码/大小写宿主差异'])
cap(17,'区域地图文本工具及两个标记文件实录',[src('townmapgen.html','1–77;150–249;251–414','文本格尺寸无钳制；坏行先清数组且无回滚；输出到文本框；两个BMP相对引用'),src('knownpoint.bmp','BMP header / 246 bytes','可得8×8，身份见material-availability'),src('selpoint.bmp','BMP header / 246 bytes','可得8×8，身份见material-availability')],[spec('75','§13/§16-8'),spec('tests','CV-M28/CV-M30')],'页面输入和原相对路径；不运行浏览器',['格32下(100,36)→(3,1)','CSV引号停用','坏行保留已载前缀','BMP存在与底图缺失分开'],'supported_static及文件头TOOL_VALIDATION，未证明加载/渲染。',['浏览器兼容','所有数值异常和CSV往返','实际底图'],history=['GR3-M12-001'])
cap(18,'外围制作可执行文件的文档能力边界',[src('animmaker.txt','1–26','文档声明XML sprites转RMXP动画，矩形≤96×96并放大2倍'),src('extendtext.txt','1–4','文档声明放大Show Text/Script对话框')],[spec('74','§18'),spec('75','§14')],'文档可读、exe存在；无源码/可用Windows宿主',['文档输入与实际产物区分','不能由exe存在宣称成功'],'supported_static仅文档陈述；实现/产物/宿主结果unresolved。',['exe执行/反编译','XML和.anm衔接'])
cap(19,'设施设置生成门、复用列表和检查点时序',[src('challenge','18–25','设施set后调用写杯'),src('gen','171–338','外层调试门，复用迁移非默认ID，双检查点和11轮/600补齐/五次最后抽样')],[spec('76','§3–§4/§6.4/§9.3'),spec('tests','GN-M01–M03/GN-M14/GN-M20')],'规则可用，生成数据合法；检查点读取失败回落空',['非调试不询问','选默认列表不追加ID','删除游标前进可留601','每次五抽只用第五','先写池再队伍、不是事务恢复'],'supported_static；生成长任务与checkpoint I/O未运行。',['所有cup规则建议等级组合','崩溃后真实恢复与终止耗时'])
cap(20,'设施候选的加权招式、拒绝采样及共享缓存',[src('genpk','1–359','首来源去重、必中剪枝自删除、物种奇偶拒绝、物理/特殊EV可重复、Sketch就地改缓存'),src('btdata','113–163;196–217','空标识转换/EV重复分母/Return替换/IV31构造')],[spec('76','§5.2–§5.7/§6.1–§6.3'),spec('tests','GN-M04–M13')],'已加载当前物种、招式、道具数据；无插件',['两总威力门共享随机量','梦话鼾声独立20%门','不满4招不经过围巾门','重复EV[HP,攻击,攻击]各170','等级变化清合法招式缓存'],'supported_static；没有实测随机分布/构造完整个体。',['全种/全道具/全机器样本正确性','备用Gen5–8全数据'])
cap(21,'设施估算与活动评级、结算累计',[src('gensim','1–438','估算独立类型分，Glicko变体；历史快照、清后计数增量；真实战后治疗与恢复持物'),src('type','73–139','calculate返回归一乘数'),src('gen','196–215;247–252','80/250消费者先后与结算后检查点')],[spec('76','§7.1–§7.4a/§6.4'),spec('tests','GN-M14–M20')],'人工合法评级对象；规则构造/战斗未运行',['70+12→82/0','238+12→250/0','第二12→94','空历史累计70不增/偏差383.3328553','单平/单胜正常更新','退休还须更早支不命中'],'supported_static；额外仅执行原评级结算6条输出记录，见M12-EXEC-001，未提升生成器/战斗/Demo。',['真实1%分支','Elo异常执行','部分失败注入','检查点读写'],evidence='EXECUTED_REFERENCE',history=['GR3-M12-002'])
cap(22,'设施训练家来源、分配重复与反写失败边界',[src('gentr','14–211','普通随机训练家循环无成功退出；编号/成员去重不对称；默认标志按先前事实取反'),src('write','511–619','dat后总PBS/子表交错；性格严格查，道具可空'),src('compile','951–1022','无总表创建默认；缺键报错，缺引用文件空表'),src('btdata','21–32;113–138','先非默认ID后首默认；成员分号格式及无招兜首键')],[spec('76','§8.1–§8.4'),spec('tests','GN-M23–M24')],'已有/空训练家表分别比较；合法文件路径',['普通生成无出口与全YOUNGSTER快捷路径','双类型初轮成员可重复','已选编号长度可先达表长','默认可多/可无','性格缺失与道具缺失不同'],'supported_static；生产器与编译/运行消费界限已承接。',['全部cup/battle_tower条目范围/索引有效性','完整生产结果对局质量'])
cap(23,'格式供应与消费路径及备份不自动启用',[src('compiler','967–1017','仅PBS顶层.txt发现并按基名归属，不递归backup'),src('town','14–19','Point八字段要求与可选项'),src('townmapgen.html','312–324','文本输出需人工补节复制'),src('btdata','113–138','设施分号/逗号解析'),src('write','573–615','设施五组分号及四招式字段输出')],[spec('75','§2/§13'),spec('76','§8.4'),spec('04','PBS发现/编译与反写合同')],'格式本身与具体数据完整性分开',['顶层根PBS实际供应，Gen5–8目录只是可得','TownMap文本无自动文件保存/输入校验','设施文本合法和缺分隔两前提'],'supported_static，只审具名格式两端，不宣称全部格式供应完整。',['每种PBS字段全集','翻译18文件解析','二进制格式完整兼容验证'])
cap(24,'可得Demo配置的入口候选而非事件链',[src('PBS/metadata.txt','1–33','StartMoney3000/PC伤药/Home3,7,5,8与两个角色'),src('PBS/town_map.txt','1–36','两区27点、六飞行记录/五目的地与两开关'),src('PBS/map_connections.txt','1–40','19连接含69↔2'),src('PBS/map_metadata.txt','1–90;239–398','Home/设施地图/旗标与Cedolan治疗点原文'),src('PBS/battle_facility_lists.txt','1–25','默认+四杯赛；fancy用single'),src('PBS/encounters.txt','1–52;221–311','版本变体/Safari重复槽/Tiall形态'),src('PBS/trainers.txt','1–118','Brock/Shadow/再战配置'),src('PBS/phone.txt','1–48','两联系人文本')],[spec('77','§3–§6.3/§8–§9'),spec('tests','DM-M01–M05/DM-M14/DM-M16')],'仅源PBS文本样本与路径清单',['Home≠新游戏起点','Cedolan两个目的地不相同','重复槽/物种数分开','设施名单引用≠已可挑战'],'supported_static，所读样本一致；地图缺失保持事件链0。',['地图元数据91–238/遭遇53–220逐项语义','电话/Giratina/平衡等级全消费者','八杯赛样本全文'])
cap(25,'开始—保存—继续的静态链与实际Demo缺口',[src('main','25–41','插件/编译→初始化→启动设置→标题'),src('start','4–125','系统起点、初始化、load地图分支、保存IO仅减计数'),src('load','281–349','新游戏/继续菜单与跳过三门'),src('saveui','100–139','覆盖二次确认与结果反馈'),src('save','7–61','保存目录与编译值先于打开覆盖')],[spec('09','§4–§5/§7'),spec('65','§3–§4'),spec('77','§3/§4.1/§9 G01'),spec('scope','§2 U01')],'需系统/地图/图块/公共事件/媒体及宿主；当前不具备',['新游戏起点取System，非Home','保存失败不总回滚','Continue按已读非空','当前地图集合空值与零条目有别'],'unresolved：静态供应/消费链可定位且条款一致，当前材料不能实际开始、保存、继续到Demo地图。',['真实启动/存档/退出/恢复','地图事件和完整Demo','存档转换备份全路径'],'unresolved')
cap(26,'正式README/scope/test README的净室与证据使用边界',[src('README.md','32–42','参考仓本不含完整工程媒体'),src('AGENTS.md','用户给定workspace指令','参考只读与独立行为输出要求')],[spec('readme','1–18;84–106;114–139'),spec('scope','§2–§5'),spec('testreadme','1–53;107–109'),spec('75','§8.1 精确兼容文本身份限定')],'按正式B阅读；历史层按其时点解释',['明确静态向量非执行','未以旧批准转授当前字节','兼容身份不充当未来API/类结构','历史管理噪声不自动构成代码复制'],'supported_static，仅本域净室/证据边界；未见把Ruby类层级要求为未来结构的本域实质问题。',['131全篇净室逐字查重','全部历史管理链接有效性与重审'],'supported','SPEC_STATIC',classification=['Generic Kernel','Demo / Developer Experience'])
# AGENTS is a workspace instruction, not a reference file.
caps[25]['source_anchors'][-1].update({'path':'AGENTS.md','commit':B,'repository':'workspace'})
cap(27,'旧树果图形文件更名与事件引用同步的失败先后',[src('rename','17–89','目录缺失阶段1不改；文件更名在前、地图引用逐图写在后'),src('rubyutil','146–169','本地移动先读源/删除旧目标/写目标，再删源')],[spec('75','§11/§16-5'),spec('tests','CV-M25')],'合法图形目录与地图工程；目标已存在/写失败为边界',['已新名与四阶段名跳过','目标已存在无比较覆盖','阶段1异常阻断阶段2','文件新名不保证引用或资源存在'],'supported_static；地图更改记录决定后续RMXP总警告，阶段1有独立更名消息。',['真实文件故障/地图保存异常','宿主大小写路径行为'])
dump('capabilities.json',caps)

finding={
 'id':'GR4-M12-001','title':'遭遇整集复制未承接空类型被丢弃而步数率保留的边界','module':'M12','severity':'P3','disposition':'REQUIRED','status':'OPEN','reviewer':reviewer,'category':'数据或资源契约缺口','classification':['Demo / Developer Experience','Creature-RPG','Generic Kernel'],
 'source_baseline':{'commit':RC,'tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','path':str(R)},'source_anchors':caps[4]['source_anchors']+[src('Data/Scripts/010_Data/001_Hardcoded data/013_EncounterType.rb','29–33','Land默认率21'),src('cmd','1163–1169','调试菜单直接调用遭遇编辑器，未另加数据清理'),src('write','423–438','空槽类型在后续PBS写出也会省略，但这是另一步')],
 'specification_baseline':{'commit':B,'tree':'d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a','formal_identity_navigation':'delivery/2026-10-12/formal-identities.json'},'spec_anchors':caps[4]['spec_anchors']+[spec('73b','§6.4 line91','空槽类型不输出限定PBS往返，未覆盖编辑器Copy')],
 'expected_reference_behavior':'正常作者流程新增遭遇类型后可不加槽直接返回，源集仍显示该类型(x0)。整集Copy逐项复制所有步数率，但不为零槽类型建立目标类型条目；目标只剩该率而无该类型，原集不变。单类型Copy不同：即使源零槽也先建目标空类型。',
 'current_spec_behavior':'WP73-B§6.1只说明复制步数率和各槽内容、保持编辑独立及后缀；WE-M11无输入限制地称深拷贝。没有说明空类型不复制和步数率残留；§6.4的空槽省略专指随后PBS写出。',
 'gap':'一个可由正常编辑流程到达的结构过滤分支未明确，独立实现通常会保留空类型，从而与参考的目标编辑列表/可新增类型集合不同。',
 'preconditions':['固定R、调试菜单或合法直接编辑入口，合法地图列表和窗口宿主','原集地图5版本0，Land已注册且步数率21，槽数0（新增类型后立即BACK可达）','目标地图7版本1未占用；Copy成功，尚未退出总保存门；无插件/外部修改'],
 'minimal_counterexample':{'input':'原集仅含Land类型(0槽)、Land率21，整集复制至空闲(7,1)','reference_output':'原集保留Land(0槽)；目标类型列表没有Land，而步数率仍有Land=21，后缀保留。打开目标可再次新增Land。','naive_spec_output':'按WE-M11无条件深拷贝，目标也显示Land(0槽)，新增类型列表排除Land。','evidence_level':'DERIVED_VECTOR','execution_status':'NOT_EXECUTED'},
 'normal_case':'Land含一个合法非空槽时复制保留类型和独立槽副本；同图同版本冲突仍拒绝。',
 'failure_or_boundary_case':'这是合法空槽边界而非异常。反向对照：在同一集把空Land类型复制到未用Cave类型，参考保留Cave空类型及复制率。复制本身仅登记，退出No仍按原档案重载；不声称产生真实遇敌差异。',
 'impact_on_independent_implementation':'编辑器复制结果、类型(x0)显示、可再次新增类型的集合以及保存的登记结构可不同；不影响已有非空槽复制正常结论，限P3。',
 'negative_evidence_search':{'artifact':'negative-evidence-search.json','scope':'全部131正式Markdown含正文/附表/测试','terms':['遭遇集|encounter set|pbEncountersEditor|WE-M11','空槽类型|空类型|空遭遇|empty encounter|empty.{0,20}slots?','复制.{0,25}(遭遇|步数率)|遭遇.{0,25}(复制|拷贝)|Copy.{0,25}encounter'],'contexts_reviewed':['WP73-B§6.1–6.5/§10–11','WE-M11–13','WP04遭遇概率往返','WP36空表/编译/快照合同'],'result':'没有条款说明整集Copy丢空类型但留概率；查得空槽省略只在PBS输出。源端检查唯一编辑定义、菜单caller、登记构造及单类型Copy，未发现补回空键的路径。'},
 'proposed_spec_change':'在WP73-B整集Copy条款补充零槽类型不建立目标条目、概率照复制；显式区分单类型Copy。限定WE-M11非空正例并补一条空类型与概率残留静态对照。保持参考事实，未来保留或修正该行为由后续政策选择，不修参考。',
 'acceptance_criteria':[{'kind':'static','criterion':'整集空Land21复制后原集不变、目标无Land类型而Land率21存在；保留后缀和未保存状态层次。'},{'kind':'static','criterion':'给出非空Land独立复制和单类型空Land→Cave仍保留空类型的反向对照。'},{'kind':'static','criterion':'不把PBS写出时省空类型当成本次编辑Copy行为，不扩大为运行/遇敌差异。'},{'kind':'runtime','criterion':'本修订验收不要求宿主运行；若后来执行必须独立记宿主/素材/夹具，不冒用本轮证据。'}],
 'affected_files':[S['73b'],S['tests']],'shared_contracts':['WP04 PBS反写与WP36当前地图快照只作相邻消费；无需修改其正确规则'],'dependencies':['WP73-A通用选择器','GameData遭遇登记','WP72编辑器入口'],'related_capabilities':['GR4-CAP-M12-005'],'related_findings':[], 'root_cause_group':'M12-encounter-set-copy-empty-type-filter',
 'history_links':{'relation':'new','gr3_related_ids':[],'second_round_relation':None,'note':'GR3-M12-001/002为BMP与结算累计，不同根因；不重开历史CLOSED。第二轮关联未追认。'},'evidence_level':'SOURCE_STATIC','execution_status':'NOT_EXECUTED','confidence':'high on source branch; bounded P3 documentation sufficiency judgment','unknowns':['当前完整编辑器宿主表现未运行','是否有下游自定义插件补回类型未知'],'excluded_claims':['不宣称参考必须修bug','不宣称所有Copy错误或会丢非空槽','不宣称当前地图遇敌率立即改变','不把当前缺完整Demo归为本发现缺能力'],'user_decision_needed':False,'review_resolution':'本独立审者建议P3有限必修；待主汇总者安排一次针对性反证/去重；未修改正式规格或关闭状态。'}
dump('findings.json',{'schema_version':'1.0','findings':[finding]})

# Per-file coverage, never a whole-file PASS implied by having read it.
coverage=[]
for key,ids,unchecked in [
 ('72',[1,2,3],['大部分个体/玩家命令以及120效果参数逐项未复核；本次源核仅具名样本']),
 ('73a',[4],['全文规格已读；属性类型、列表器、物种/图鉴细节没有本次全源验证']),
 ('73b',[5,6,7,8,9],['全部世界UI按键/图块修复算法及普通战斗显示消费者未穷尽']),
 ('74',[10,11,12,13,14,18],['全文规格已读；补间/曲线路径/控件全部分支未源核；真实anm/媒体缺']),
 ('75',[15,16,17,18,23,27],['全文规格已读；35替换仅表审，六族旧战斗/文字组合/柜台算法未完整重审']),
 ('76',[19,20,21,22,23],['四生成源文件全文语义阅读；全规则/PBS样本/对局质量未核；仅评级局部执行']),
 ('77',[24,25],['全文规格已读；九表不是本次全读；电话/动态形态/平衡等级等所有具名跨表结论未重证']),
 ('tests',list(range(1,26)),['仅cap明确关联行进行双向深核；其余行与B批长表为库存/导航；静态案例未整族执行']),
 ('readme',[26],['历史管理层不作本轮当前状态裁决，全部历史链接未核']),
 ('scope',[25,26],['保留全部具名未知，不复核全球历史分母；全部131文件净室查重未做']),
 ('testreadme',[26],['17族全量计数和历史验收链接未重审']),
 ('04',[6,15,22,23],['只读命中上下文/引用合同，不重新覆盖全编译器']),
 ('09',[25],['只核启动/新游戏/继续/保存顺序；17登记与迁移全路径非本域']),
 ('36',[6],['只核空表、注册与快照/概率相邻语义；完整遭遇非本域']),
 ('43',[3],['只核玩泥巴/玩水双来源叠乘行123']),
 ('45',[3],['只核新旧Sport状态投影行106']),
 ('65',[1,25],['只核§3/§4/§6入口与保存消费，其他UI非本域'])]:
  cc=[caps[i-1] for i in ids]
  coverage.append({'path':S[key],'baseline_commit':B,'contracts_checked':[{'capability_id':c['capability_id'],'contract':c['description']} for c in cc],'source_anchors':[a for c in cc for a in c['source_anchors']],'status':'partial' if key not in ['readme','scope','testreadme','43','45'] else 'supported','support_evidence':[{'evidence_level':c['evidence_level'],'capability_id':c['capability_id'],'meaning':c['reason']} for c in cc],'dependencies':sorted({a['path'] for c in cc for a in c['spec_anchors'] if a['path']!=S[key]}),'unsupported_assertions':['WE-M11未限定零槽来源的深拷贝预期；GR4-M12-001'] if key in ['73b','tests'] else [],'not_checked':unchecked,'interpretation':'supported仅上述supported_static条款；partial不等于全文件错误。所有未点名合同不获新PASS。'})
dump('spec-coverage.json',coverage)

# Read ledger is explicit, ranges not present were inventoried only, not semantically reviewed.
ranges={
 'menu':['1–425'],'cmd':['276–477','1148–1169','1266–1347'],'extra':['1–210','553–720'],'effects':['60–178','200–452'],'rename':['1–89'],
 'edit':['1–448','478–604','926–987','1099–1203','1252–1324'],'terrain':['1–74','158–169','190–263'],'connect':['193–285','470–578'],
 'sprite':['4–46','91–221','338–411'],'util':['1–64'],'animscene':['43–66','409–520','539–730'],'animio':['1–147'],'animfunc':['990–1045','1132–1170'],
 'player':['334–665','749–844'],'play':['418–455','486–550'],'compiler':['967–1038'],'compile':['658–745','951–1050','1274–1321'],'write':['291–347','403–457','511–619'],
 'convert':['1–86','441–635','771–852','1683–1751'],'gen':['1–338'],'genpk':['1–359'],'gentr':['1–211'],'gensim':['1–438'],
 'challenge':['1–30'],'btdata':['1–219'],'load':['245–354'],'saveui':['75–139'],'start':['1–126'],'save':['1–82'],'main':['1–52'],'scene':['188–213'],'pause':['265–310'],
 'enc':['1–71'],'metrics':['1–101'],'misc':['20–63'],'town':['1–43'],'type':['73–141'],'trainer':['1–114'],'encuse':['1–40'],'meta':['110–127'],'file':['181–273'],'rubyutil':['140–175'],'gamedata':['78–108'],'damage':['348–376'],'sports':['690–746'],
 'scripts_extract.rb':['1–183;装载器字符串仅形状，未解包'],'scripts_combine.rb':['182–183;其余由字节比较辅助与extract相同'],'townmapgen.html':['1–414'],
 'README.md':['1–42'],'animmaker.txt':['1–26'],'extendtext.txt':['1–4'],
 'Data/Scripts/010_Data/001_Hardcoded data/013_EncounterType.rb':['1–90','142–146'],'Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb':['155–182','205–222'],'PBS/metadata.txt':['1–33'],'PBS/town_map.txt':['1–36'],'PBS/map_connections.txt':['1–40'],'PBS/battle_facility_lists.txt':['1–25'],'PBS/dungeon_parameters.txt':['1–30'],
 'PBS/map_metadata.txt':['1–90','239–398'],'PBS/encounters.txt':['1–52','221–311'],'PBS/trainers.txt':['1–118'],'PBS/phone.txt':['1–48']}
ranges={A.get(k,k):v for k,v in ranges.items()}
tracked=subprocess.check_output(['git','-C',str(R),'ls-files','-z']).decode().split('\0')[:-1]
source_inventory=[]
for path in tracked:
 primary=(path.startswith('Data/Scripts/020_Debug/') or path.startswith('Data/Scripts/021_Compiler/') or '003_Battle Frontier generator/' in path or path in ['townmapgen.html','scripts_extract.rb','scripts_combine.rb','animmaker.txt','extendtext.txt','animmaker.exe','extendtext.exe','knownpoint.bmp','selpoint.bmp','README.md'])
 related=primary or path in ranges or path.startswith('Data/Scripts/001_Technical/001_Debugging/') or path in A.values() or path.startswith(('PBS/','Fonts/','Text_english_core/')) or path in ['mkxp.json','Data/Scripts.rxdata','Data/messages_core.dat']
 group='outside_M12_inventory' if not related else 'tool_sources' if primary else 'content_supply' if path.startswith('PBS/') else 'translation_font_host_binary' if path.startswith(('Fonts/','Text_english_core/')) or path in ['mkxp.json','Data/Scripts.rxdata','Data/messages_core.dat'] else 'caller_consumer_dependency'
 status='read_semantically' if path in ranges else 'inventoried_only' if related else 'not_reviewed'
 source_inventory.append({'path':path,'group':group,'M12_relevance':'primary' if primary else 'related' if related else 'outside_domain','review_status':status,'read_ranges':ranges.get(path,[]),'not_reviewed':'除read_ranges外均未逐段语义审查；名称/搜索命中不算读过' if status=='read_semantically' else '可得但本次未逐段语义审查' if related else '仅为全参考清单完备而登记，非本域语义范围'})
dump('source-scope.json',{'schema_version':'1.0','reference_baseline':RC,'inventory_basis':'shared baseline432 tracked identity; local git ls-files names only; no whole-repository rehash','counts':dict(Counter(x['review_status'] for x in source_inventory)),'files':source_inventory,'overlays':[{'path':'.DS_Store','status':'not_reviewed'},{'path':'PBS/.DS_Store','status':'not_reviewed'}],'limitations':['setting/constants and other search-only files remain inventoried_only except named anchors','所有backup、八cup名单及完整pokemon_metrics只盘点未全文阅读','翻译18/字体8/二进制只材料可得性；无解析、渲染、执行','不可用地图/事件/媒体不是可读未读；另见material-availability']})
primary_formal={S[k] for k in ['72','73a','73b','74','75','76','77','tests','readme','scope','testreadme']}
covered={c['path'] for c in coverage}
dump('formal-inventory.json',{'baseline':B,'count':131,'primary_M12_count':len(primary_formal),'files':[{'path':str(p),'role':'primary_M12' if str(p) in primary_formal else 'scoped_dependency' if str(p) in covered else 'alias_search_only','semantic_coverage':'spec-coverage.json' if str(p) in covered else 'not_reviewed; negative-evidence-search only'} for p in sorted(F.rglob('*.md'))]})

history_base={'gr3_findings_commit':'d5b6af3ebbabc57ed7fbdc2e1fb2c4736dbf9a65','gr3_findings_path':'review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/findings.json','accepted_actual_commit':'266539d5db6d84116a355f503df8830d309c7937','independent_acceptance_commit':'b8dcb984bdc5ef044f77c3db5d3b83edc2908f10','independent_acceptance_path':'review/remediation-third-20261012-prepare/U06/actual-integration/independent-review/attempt-01/per-id-verdicts.json','formal_acceptance_commit':'c2eb74c7cbcf8a190d5e902d871fbce44904efd6','formal_acceptance_path':'review/remediation-third-20261012-prepare/registration/U06-formal-acceptance.json'}
reg=[]
for id_,n,criteria,limits in [('GR3-M12-001',17,['WP75§13.3两个BMP路径/尺寸/SHA与当前只读头部检查一致','§16-8/CV-M30分开已有标记与缺Graphics/底图','浏览器/解码/外观/完整Demo未提升'],['TOOL_VALIDATION只核字节与文件头，不是图片解码或页面运行']),('GR3-M12-002',21,['WP76§2/§6.4/§7.4/§7.4a与GN-M14/M20保留C+h定义','正常70+12=82/0、238+12=250/0；跨轮94/0；空历史不增','80/250的评分、成员、位置更早门静态核对；异常不承诺评级全回滚'],['M12-EXEC-001仅隔离评级6记录；五支更替/异常/检查点仍SOURCE_STATIC','不给历史静态回执反向增加运行证明'])]:
  c=caps[n-1]
  reg.append({'id':id_,'reviewer':reviewer,'historical_status':'CLOSED (共享导航保持；不改旧身份)','current_spec_anchors':c['spec_anchors'],'source_anchors':c['source_anchors'],'old_acceptance_fixed_reference':history_base,'criteria_actually_checked':criteria,'consumer_checked':'WP75页面/BMP/CV-M30' if n==17 else 'WP76下一轮五支更替+GN-M14/M20；未执行更替','result':'supported','meaning':'本次有界回归未见回退；历史CLOSED保持，不重开','limits':limits,'evidence_level':'TOOL_VALIDATION' if n==17 else 'EXECUTED_REFERENCE','execution_status':'EXECUTED_SCOPED_ONLY'})
dump('regression.json',reg)
execs=[json.loads((P/'rating-execution.json').read_text()),json.loads((P/'material-execution.json').read_text())]
dump('execution.json',{'actual_executions':execs,'not_executed':[{'scope':'完整参考游戏/Windows exe/mkxp/真实Demo开始保存继续','reason':'无宿主，地图/系统/公共事件/图块及媒体缺；没有尝试读取真实用户存档'},{'scope':'遭遇复制反例/全部GUI编辑/编译转换/动画交换/脚本提取合并','reason':'只有SOURCE_STATIC与DERIVED_VECTOR；未构造宿主替身，不写参考或工程'},{'scope':'设施候选/600队11轮模拟/真实1%对局/检查点文件I/O','reason':'仅隔离原评级结算，不扩称生成测试通过'},{'scope':'Fonts/音视频/BMP解码/翻译二进制/实际anm、地图归档解析','reason':'文件名/头部/格式定义不等于解析或播放成功'}]})
print(json.dumps({'capabilities':len(caps),'coverage_files':len(coverage),'findings':len([finding]),'source_inventory':dict(Counter(x['review_status'] for x in source_inventory)),'primary_formal_files':len(primary_formal)},ensure_ascii=False))
