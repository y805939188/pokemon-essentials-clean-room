"""Assemble CB's independently reached static verdicts. No reference execution."""
import json,pathlib,datetime,sys
ROOT=pathlib.Path.cwd()
RUN=ROOT/'review/global-independent-review/fourth-2026-10-12-1f36475-c92e'
OUT=RUN/'modules/CB'
B='1f36475d22120a0d1175967d5b17d71fe8311d88'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
launch=json.loads((RUN/'tasks/CB-launch.json').read_text())
thread=launch['thread_id']
P='deliverables/final-specification-set/'
def src(path,lines,role):return {'path':path,'commit':R,'lines':lines,'role':role}
def spec(path,lines,role):return {'path':P+path,'commit':B,'lines':lines,'role':role}
neg=json.loads((OUT/'negative-evidence.json').read_text())
searches={v['id']:v for v in neg['searches']}
def counter(ids,contexts,conclusion):
 return {'search_ids':ids,'terms':[searches[x]['pattern'] for x in ids],'scope':'B 固定正式131篇，正文、scope、共享合同、附表和测试全部纳入；各检索文件字节与 git show B 相等','contexts_actually_read':contexts,'conclusion':conclusion,'artifact':'negative-evidence.json'}
records=[]
def add(fid,decision,severity,sources,specs,ce,normal,reason,history,refinements=None,unknowns=None,execution=None):
 records.append({'finding_id':fid,'decision':decision,'severity':severity,
 'proposed_disposition':'REQUIRED：补准确的固定参考事实与有区分力的静态向量；未来兼容/改进行为由后续政策另定。'+('须同时落实下列精确化。' if refinements else ''),
 'sources_actually_read':sources,'specs_actually_read':specs,'counterevidence_search':ce,
 'normal_boundary_check':normal,
 'execution_evidence_assessment':execution or '该候选没有参考行为执行。原模块工具校验只证明产物结构/锚点等，不能证明本候选行为；CB未运行参考函数、行为模型、UI、输入或宿主。以下结果为源码/规格静态核对及条件化推导。',
 'historical_relation_assessment':history,'duplicate_of':None,'reason':reason,
 'required_refinements':refinements or [],'remaining_unknowns':unknowns or ['真实宿主、媒体、物理输入与完整Demo未执行；外部插件不在固定R证明范围。'],
 'reviewer':'CB：本轮新独立反证审者；未编写输入域报告','thread_id':thread,
 'evidence_level':['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR']})
add('GR4-M10-001','CONFIRM','P2',[
 src('Data/Scripts/007_Objects and windows/011_Messages.rb','55–159,166–205,650–801','数字参数、通用命令/帮助命令、消息包装'),
 src('Data/Scripts/007_Objects and windows/005_SpriteWindow_text.rb','624–729,862–923,1253–1254','先组件方向更新；普通扩展命令未覆盖更新'),
 src('Data/Scripts/003_Game processing/004_Interpreter_Commands.rb','325–334','事件103真实消费者'),
 src('Data/Scripts/016_UI/019_UI_PC.rb','4–24,110–153','普通和帮助命令的PC消费者')],[
 spec('user-interface/wp17-messages-windows-input.md','90–130,146–178,191–196,220–229','单键、命名与更新机会分界'),
 spec('user-interface/wp66-c-bag-item-storage-and-shop-ui.md','74–108','共享物品数量/两商店同轮表的明确范围'),
 spec('user-interface/wp65-title-load-options-pause-and-pc.md','188–200','PC菜单消费者'),
 spec('engine-overworld/wp13-interpreter-command-matrix.md','24–30','事件数字入变量不提供竞争判据'),
 spec('user-interface/wp67-a-battle-interaction-and-presentation.md','224–227','战斗列表是不同消息/取消合同'),
 spec('test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md','19–30,540–554,671–687','MG11–20、B04-M、U05-QN/TX')],
 counter(['CB-N01'],['WP17 §4/§5/§6.2.1/§6.4/§7.2','WP66-C §5.1 与 U05-QN01–04','WP67-A §9.1 与 U05-TX01–04','WP65 §7.2；WP13命令103'],
 '命名、共享件数、商店与战斗列表确有局部规则，但均不能推出普通命令和逐位数字的不同竞争结果。MG12的不可取消及MG18的越界只给单独输入；没有全局确认/取消优先规则可补此缺口。'),
 {'preconditions':'窗口已正常进入循环，无插件、无传入块更改值或输入；USE/BACK按下沿及方向repeat为给定同轮查询，非实测物理按键。',
 'minimal':'命令两项、索引0、取消参数2，USE+BACK返回1；数字[0,9]、值1、显式取消−1，同输入返回1。两处虽然都是数字1，但命令的确认对照为0、数字的取消对照为−1，确实分别排除统一确认优先与统一取消优先。',
 'normal':'仅USE：命令0/数字1；仅BACK：命令1/数字−1；命令取消参数0且同轮USE+BACK仍返回0。帮助命令同样。',
 'boundary':'数字值1同轮UP+USE得2；[3,3]初3同轮UP+USE+BACK改4、蜂鸣继续，不取消。事件103默认取消值等于初值，不能把显式−1包装成其默认参数；但事件入口在初1的一位编辑UP+USE+BACK仍确认2而非取消初1。'},
 '确认有实际调用与清楚的最小差异。先更新组件与之后两个出口的相对次序决定返回值或继续等待，现有各入口单键规则不能唯一决定它。范围限通用命令/帮助命令及逐位数字，不推广为全部UI；P2针对可改变有效选择和事件变量的行为合同。',
 {'relation':'new_scope_same_root','related_ids':['GR3-M10-002'],'assessment':'B中U05件数/商店条款已存在且范围明确；本项是同类问题的新增消费者范围，不是该旧范围回归，不重开或补签旧关闭。M01–M06十一候选无同根；M03路线时序不同。'})
add('GR4-M10-002','CONFIRM','P3',[
 src('Data/Scripts/007_Objects and windows/002_MessageConfig.rb','28–85','冷读取、备用链、显式设置为空的独立状态'),
 src('Data/Scripts/007_Objects and windows/004_SpriteWindow.rb','818–874','默认消费者与单窗设置失败的区别'),
 src('Data/Scripts/007_Objects and windows/005_SpriteWindow_text.rb','258–275,1118–1124','文字窗覆盖调用上层设置，不另建回退链'),
 src('Data/Scripts/007_Objects and windows/011_Messages.rb','370–394,444–451','消息冷取与空w直接清除'),
 src('Data/Scripts/016_UI/015_UI_Options.rb','492–519','选项写入和缓存设置'),
 src('Data/Scripts/003_Game processing/004_Interpreter_Commands.rb','671–678','在册皮肤事件设置，未匹配是不同前提'),
 src('Data/Scripts/001_Technical/002_Files/001_FileTests.rb','119–141','单资源解析不提供跨皮肤候选链')],[
 spec('user-interface/wp17-messages-windows-input.md','29–39,84–88,225–236','换肤、样式与资源转引'),
 spec('engine-overworld/wp15-resource-matching-and-audio.md','20–28,71–96','通用解析、缓存与空文件名'),
 spec('user-interface/wp65-title-load-options-pause-and-pc.md','102–124','选项即时/退出应用'),
 spec('generic-kernel/wp02-rule-configuration-and-data-variants.md','160–170,239–244','皮肤配置只有数量及角色'),
 spec('demo-dx/wp73-a-content-editors.md','151–166','编辑器目录缺失/空目录不等于皮肤冷回退'),
 spec('engine-overworld/wp13-interpreter-command-matrix.md','50','未匹配配置名无变化，不是已匹配名对应资源缺失'),
 spec('test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md','15','MG05仅空w')],
 counter(['CB-N02'],['WP17 §3.1/3.4/7.3','WP15 §3.1/5.1','WP65 §5.1/5.2','WP02配置表','WP73-A §9/CE-M18；WP13命令131；MG05'],
 '未发现默认候选身份链或未初始化与显式空结果的区别。通用解析nil、空文件名空白图、空w、未匹配配置名和编辑器目录失败都有各自前提，不能替代冷取。'),
 {'preconditions':'合法选项索引、未初始化的对应默认皮肤状态；候选资源存在性为条件输入。显式设置对照指定完整逻辑资源位置，不假设任意裸名自动加目录。',
 'minimal':'所选Missing缺失，系统登记Custom及两个通用备用均存在：首次读选Custom。独立显式设置Missing失败后再读，返回空资源名称，不重新选Custom。',
 'normal':'所选资源存在时即用它；缺选项对象时采用配置首项开始候选查找。',
 'boundary':'系统名缺失/为空后试Graphics/System/Window，再Graphics/Windowskins/001-Blue01，全部缺才空。空结果不等于既有消息窗必然无皮肤：单窗设置失败可提前返回；不从缓存空名称推出像素、崩溃或旧图保持。'},
 '候选补的是按同一资源集合如何选择备用身份，而不是一般资源缺失标题。原报告已正确排除了空w与单窗设置的画面推论。P3限于缺资源时的默认选择及后续读取，非整个资源系统缺失。',
 {'relation':'new_within_reviewed_scope','related_ids':[],'assessment':'未见与M01–M06同根。没有据历史PASS或旧政策确定完整性；不追认未知第二轮ID。'},
 unknowns=['皮肤媒体和真实窗口未取得/未运行；空名称后既有窗口的实际呈现、旧资源释放效果不在本结论。','未来是否采用相同候选身份属于兼容政策，事实修订不预先决定。'])
add('GR4-M10-003','CONFIRM_WITH_REFINEMENT','P2',[
 src('Data/Scripts/007_Objects and windows/010_DrawText.rb','75,119–240,345–545,563–658,703–783,1035–1040','快/一般格式化、标记分流、行归属及后处理'),
 src('Data/Scripts/007_Objects and windows/005_SpriteWindow_text.rb','316–355','布局生成的换行被消息行满暂停消费'),
 src('Data/Scripts/016_UI/006_UI_Summary.rb','510–587,634–637','获得文本与摘要备忘录的同一格式化消费者')],[
 spec('user-interface/wp17-draw-text-tags.md','1–100','显式标签与§6未展开换行算法'),
 spec('user-interface/wp17-messages-windows-input.md','59–87,185–189','行满暂停与多行编辑不是格式化折行合同'),
 spec('user-interface/wp66-a-party-and-summary-ui.md','132–160','摘要内容未给长词布局结果'),
 spec('test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md','40–51,554','DT04显式标签、B04-M14显式换行'),
 spec('generic-kernel/wp08-localization.md','1–11','本地化明确将呈现交给UI'),
 spec('demo-dx/wp73-a-content-editors.md','47–53','限长输入不是行宽拆分'),
 spec('scope-statement.md','93–117','未运行像素/字体的保留不等于已有逻辑行规则')],
 counter(['CB-N03','CB-N03b'],['WP17绘制附表§3/§6；主文§3.3/§6.3','WP66-A §5.2','DT04、DT08、B04-M14','WP08非目标；WP73-A文本长度；scope媒体限制'],
 '未找到无空白串不硬折行或普通自动宽度换行的行为规则。显式换行、对齐换行、输入字数上限及文本转换是不同条件。附表转回参考绘制函数并不能让净室实现者推出AB/A B结果。'),
 {'preconditions':'有效测量接口、起点x=0、普通非斜体无额外描边、A/B各测量宽8、ASCII空格宽4；自动折行开启、显式换行开启、高度不限制。测量是输入，不是实际字体实测。',
 'minimal':'行宽12：AB的A/B留同一逻辑行，B相对横坐标8；A B的B移到下一逻辑行。加前置<pg>仍保持各自的行归属，不要求快/一般路径绝对纵坐标相等。',
 'normal':'宽内短文本保持一行；显式A换行B为两行；带标签路径和快路径均有真实格式化调用。',
 'boundary':'额外精确化：相同A B在行宽22时仍一行，在行宽21时B换行；因为判定含额外2个测量单位，而非只比较裸累计文字宽。超宽行首词移不出行首；最终裁切和可见像素未证。'},
 '原AB/A B最小反例成立，且消息消费者会依据布局换行插入暂停，故不是要求逐像素复刻。须收紧拟补规则的宽度阈值；只写“超过请求行宽”可能漏掉刚好容纳文字却仍换行的边界。保持P2，精确化并不推翻原缺口，也不另立根因。',
 {'relation':'new_within_reviewed_scope','related_ids':[],'assessment':'M01的本地化参数替换发生在上游文本结果层；本项固定AB输入后的布局，互不合并。没有把旧行满暂停已承接合同重开。'},
 refinements=['拟补自动折行规则须注明固定参考会预留额外2个测量单位，只有非行首词边界及相应内容条件成立时移词；不得概括为裸文本宽大于行宽才折行。','向量明确普通样式、起点0、自动折行开启和测量夹具；<pg>对照比较逻辑行归属，不宣称两个内部路径绝对像素相同。','正文仅登记固定参考的不硬拆长词行为；未来改善无空格语言排版属于独立兼容政策。'])
add('GR4-M10-004','CONFIRM','P2',[
 src('Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb','412–485,492–525','实际默认身份映射、候选链、映射和播放分层'),
 src('Data/Scripts/011_Battle/001_Battle/001_Battle.rb','838–843','动画开关真实包装'),
 src('Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb','228–235','玩家选项和战斗规则设置开关'),
 src('Data/Scripts/010_Data/002_PBS data/005_Move.rb','22–56,79–96','储存类别与世代派生物理/特殊不同'),
 src('Data/Scripts/010_Data/001_Hardcoded data/017_Target.rb','26–33,136–141','目标分格输入'),
 src('Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb','39–53','映射/动画库加载分开'),
 src('Data/Scripts/010_Data/001_GameData.rb','87–92','空候选不存在的守卫'),
 src('PBS/moves.txt','2603–2614,2782–2793,2819–2828,5326–5336','FLAMETHROWER/EMBER/SUNNYDAY/TACKLE默认数据')],[
 spec('user-interface/wp67-a-battle-interaction-and-presentation.md','249–254','六槽名称与骨架不含身份数据'),
 spec('demo-dx/wp74-battle-animation-authoring-and-exchange.md','394–404','作者命名关联、保存与播放交界'),
 spec('generic-kernel/wp03-content-identity-and-schema.md','61–69,200–205','move2anim产物来源不等于类型默认表'),
 spec('generic-kernel/wp04-pbs-lifecycle.md','130–139','动画映射编译产物'),
 spec('test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md','365–369','K35开关/K36全落空'),
 spec('scope-statement.md','93–117','资源身份可作为兼容数据，媒体存在性仍未证')],
 counter(['CB-N04','CB-N04b'],['WP67-A §9.4','WP74 §15/§16','WP03非类产物/交界表；WP04 §5.1','K35/K36；中英文火系身份别名及类型/动画交叉匹配'],
 '实质动画命中只有表名/查找骨架、作者命名编译和全落空测试；英文身份或中文别名的其它命中属于招式效果、天气、钓鱼或演出目录，没有默认类型到身份的可用附表。'),
 {'preconditions':'动画开关真；合法默认FLAMETHROWER记录；映射已正常取得，双方映射容器均有效；动画10/20/30为不同有效条件槽，hitNum=0；无插件。',
 'minimal':'己方FLAMETHROWER无精确映射，EMBER→10、SUNNYDAY→20、TACKLE→30：依次删前一候选可得10→20→30→空。不是默认媒体真实编号。',
 'normal':'精确映射存在先命中；对方EMBER独立映射11存在时优先11，无则普通10。',
 'boundary':'候选身份须登记且有映射；不是以图像文件存在代替映射门。分格消费储存类别及目标数据，不把当前战斗派生物理/特殊直接替换它。映射异常的局部返回空与正常候选缺失不同，夹具排除前者。'},
 '六槽的名字不能唯一决定火系特殊单目标采用EMBER；没有别处数据可推出这一身份。默认缺专用映射是明示支持的普通查找分支，补完整固定映射是数据合同修订，不是抄写源表表达式或规定新播放架构。P2维持。',
 {'relation':'new_within_reviewed_scope','related_ids':[],'assessment':'M01–M06无同根。M12动画作者域没有相同候选；WP74命名编译是共享前置，不与默认选择数据合并。'},
 unknowns=['参考材料缺可用move2anim/动画集合及媒体；映射槽号为静态夹具，未加载二进制或播放。','未来是否采用相同默认身份是政策问题，不由本事实审计决定。'])
add('GR4-M11-001','CONFIRM','P2',[
 src('Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb','61–69,129–140,195–227','异色记录可真、读取不覆盖及选择器写入默认假'),
 src('Data/Scripts/016_UI/003_UI_Pokedex_Main.rb','264–298,417–448,766–768','主列表选中物种预览固定普通'),
 src('Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb','5–116,139–213,446–552,582–617','完整/简略共用刷新、形态资格和选择器单独写入'),
 src('Data/Scripts/014_Pokemon/001_Pokemon-related/003_Pokemon_Sprites.rb','49–68,253–258,289–300','物种图和图标参数透传'),
 src('Data/Scripts/010_Data/002_PBS data/009_Species_files.rb','3–34,47–52,86–124','普通请求不查异色目录；区别个体动态形态入口'),
 src('Data/Scripts/016_UI/006_UI_Summary.rb','1218–1225','摘要先登记最近见到再开完整条目'),
 src('Data/Scripts/019_Utilities/002_Utilities_Pokemon.rb','55–71','获得提示先登记最近见到后开简略条目')],[
 spec('pokemon-rules/wp62-pokedex-records-regions-and-content.md','11–30,34–91,141–164','记录维度、末次值与展示资格'),
 spec('user-interface/wp66-b-storage-and-pokedex-ui.md','143–211','主列表、Info/Forms、首轮写入、独立入口'),
 spec('engine-overworld/wp15-resource-matching-and-audio.md','36–52','请求属性的通用解析不能确定调用者传何属性'),
 spec('user-interface/wp17-messages-windows-input.md','198–210','物种图标按传入属性的通用合同'),
 spec('user-interface/wp66-a-party-and-summary-ui.md','123–145','图鉴邮件快照、摘要异色标志均不同消费者'),
 spec('pokemon-rules/wp21-dynamic-forms-and-display.md','183–194','形态提交登记普通异色是数据写入，不是图鉴固定非异色显示'),
 spec('test-catalog/pokemon-rules-wp53-60-61-62-69-70.md','116–149','PD查询/展示/选择器向量'),
 spec('test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md','267–286','BX B20–B39')],
 counter(['CB-N05','CB-N05b'],['WP62 §2/§3/§4/§6 与 PD03–05/PD19/PD31–34','WP66-B §6/§7，B30/B33/B38','WP15 §4.1；WP17共享图标','WP66-A邮件/摘要；WP21形态提交'],
 '记录异色、通用资源闪光参数、摘要红编号、邮件快照以及Forms选择器首轮写false都有明文；均不能推出未进入选择器的主预览/Info固定请求普通且保持末次true。跨行异色/末次别名补检也未找到该调用方规则。'),
 {'preconditions':'已见/拥有合法雄性BULBASAUR形态0、末次[0,0,true]、正常图鉴入口与媒体宿主依赖；普通/异色资源相互不同。先不进形态选择器。',
 'minimal':'主列表选中预览与完整Info均请求普通前图，末次true保持；独立简略Info同样请求普通。完整传递末次三元组的备选实现会请求异色，故可区分。',
 'normal':'仅将末次异色改false仍请求普通；性别与形态仍消费原记录。',
 'boundary':'仅异色见过仍可通过相应形态已见门；普通资源缺失不会因为保存true而改查异色。只有>1可列项且真正进入选择器，首轮另写末次false。单项BULBASAUR不用于证明这个多项选择器分支，须用独立多项夹具。'},
 '独立确认的是记录→资源请求交界缺口。通用按属性资源规则可接受true/false两种输入；现有记录与选择器条款没有规定选择器以外传入固定false。不是图鉴不记录异色，也不是每行拥有标记图标的颜色问题。P2针对多正常入口的可见外观差异。',
 {'relation':'new_within_reviewed_scope','related_ids':['GR3-M11-001'],'assessment':'旧栖息地格规则与本次资源请求无同根。M04个体取图动态形态与本项共享资源文件，但前者读取个体并可能提交形态，后者只消费记录的性别/形态且固定异色假；不合并。M10未另报同项，WP66-B只是投影。'})
add('GR4-M12-001','CONFIRM','P3',[
 src('Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb','6–124,128–251,256–340','新增零槽可返回、整集筛空/率全复制、单类型复制及保存层'),
 src('Data/Scripts/010_Data/002_PBS data/013_Encounter.rb','20–35,62–68','精确目标查找和构造不补类型'),
 src('Data/Scripts/010_Data/001_GameData.rb','78–85','登记不清理或补键'),
 src('Data/Scripts/010_Data/001_Hardcoded data/013_EncounterType.rb','29–33','Land默认21'),
 src('Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb','1163–1169','公开调试菜单实际调用'),
 src('Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb','403–438','PBS写出过滤是后续不同步骤')],[
 spec('demo-dx/wp73-b-world-editors.md','67–109,179–205','整集Copy、单类型Copy、零率往返与快照'),
 spec('test-catalog/demo-dx-wp72-73-74-75-76-77.md','84–88','WE-M10–14，M11未限定非空'),
 spec('generic-kernel/wp04-pbs-lifecycle.md','153–164','非空槽PBS输出是文件门'),
 spec('creature-rpg/wp36-wild-encounters-and-modifiers.md','49–71,98–107,240–252','数据/快照/候选空表分层'),
 spec('demo-dx/wp73-a-content-editors.md','47–53,158–166','其它空集合清理与保存语义不能补本Copy')],
 counter(['CB-N06','CB-N06b'],['WP73-B §6.1–6.5/§10–11','WE-M10–14','WP04 §5.5','WP36 §3.1–3.2.1/§9','WP73-A空集合与校验分界'],
 '未找到整集Copy滤空类型但保留率的条款。WP04/WP73-B省空类型明确是PBS输出，WP36空表是运行消费者。WE-M11无非空前提的深拷贝表述无法唯一得出目标列表无Land。'),
 {'preconditions':'合法地图5版本0源集：Land已注册、率21、槽0；目标7版本1未占用；调试编辑窗口正常；尚未退出总保存门，无插件。新增类型后不加槽BACK可达该状态，不是假设损坏数据。',
 'minimal':'整集Copy后源仍Land(x0)，目标无Land类型但保留Land率21及来源后缀；目标可再次新增Land。结构保真的普通深拷贝则仍显示Land(x0)并禁止再次新增，确能区分。',
 'normal':'非空Land保持类型及独立槽内容；同图同版冲突拒绝。',
 'boundary':'在同集单类型空Land→未用Cave的Copy仍建立Cave空类型并复制率，是独立反向夹具。取消总保存会重载登记，不能说复制已改真实存档或当前地图遇敌率；PBS稍后省空类型不能解释保存前列表差异。'},
 '原报告的有效输入可通过编辑器正常新增/立即返回得到；没有登记构造或caller补回被滤掉类型。缺口有限且不影响非空复制正确规则，P3维持；无需把参考过滤当作未来引擎永久要求。',
 {'relation':'new_within_reviewed_scope','related_ids':['GR3-M12-001','GR3-M12-002'],'assessment':'BMP材料与评级累计是不同根因。M01–M06无编辑器整集筛空候选，不与翻译逐项合并、遗传或运行遭遇规则合并；不重做旧回归签署。'},
 execution='本候选为SOURCE_STATIC/SPEC_STATIC/DERIVED_VECTOR，未执行。另读M12 rating-probe.rb及rating-execution.json：回执是Ruby2.6.10隔离评级/结算，绕过队伍构造，无编辑器调用，不支持本候选也不是随附Ruby3.1宿主实测。CB只评价该回执可支持范围，不重跑或重新认证其数值。')

cross=[]
for n in range(1,7):
 for f in json.loads((RUN/'modules'/f'M{n:02d}'/'findings.json').read_text())['findings']:
  cross.append({'id':f['id'],'title':f['title'],'source_anchors_read_as_candidate_metadata':f.get('source_anchors',[]),'spec_anchors_read_as_candidate_metadata':f.get('spec_anchors',[]),'verdict':'NO_DUPLICATE_IN_CB_SCOPE; ID/标题/锚点比对，不为本项能力重签'})
result={'schema_version':'1.0','reviewer':'CB','thread_id':thread,'pid_from_launch':launch['pid'],
 'identity_source':'tasks/CB-launch.json','requested_model':launch['requested'],'actual_echo':'UNVERIFIED',
 'formal_baseline':B,'reference_baseline':R,'reference_root':'/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials',
 'input_identity_manifest':'tasks/CB-input-identities.json','scope':['M07','M08','M09','M10','M11','M12'],
 'empty_candidate_modules':['M07','M08','M09'],'scope_limit':'六条输入候选的独立针对性反证；空候选域不做全能力签署；不重做readiness或历史档案审计。',
 'records':records,'cross_domain_duplicate_check':cross,'new_findings':[],
 'summary':{'input_candidates':6,'records':6,'CONFIRM':5,'CONFIRM_WITH_REFINEMENT':1,'REJECT':0,'MERGE':0,'OPTIONAL':0,'UNRESOLVED':0,'P2':4,'P3':2}}
(OUT/'verdicts.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')

for s in neg['searches']:
 matched=[r for r in records if s['id'] in r['counterevidence_search']['search_ids']]
 s['finding_ids']=[r['finding_id'] for r in matched]
 s['contexts_actually_read']=[v for r in matched for v in r['counterevidence_search']['contexts_actually_read']]
 s['conclusion']='；'.join(r['counterevidence_search']['conclusion'] for r in matched)
neg['scope_note']='匹配文本来自B规格，非R源码复制。命中不等于缺失；各记录列实质上下文与结论。全131检索不表示逐段通读131篇。'
neg['source_countersearches']=[
 {'scope':'R/Data/Scripts 全部脚本','queries':['def pbChooseNumber|def pbShowCommands|class Window_InputNumberPokemon|class Window_CommandPokemonEx','pb(Get|Set|Default)(Speech|System)Frame|pbDefaultWindowskin|def setSkin'], 'assessment':'通用选择函数定义唯一；相同名的场景实例入口有各自接收者，不覆盖Kernel通用调用。皮肤缓存设置来自选项/命令131；文字窗setSkin覆盖仍调用基底，不增加备用链。'},
 {'scope':'R/Data/Scripts 全部脚本','queries':['def (getFormattedText|getFormattedTextFast|drawFormattedTextEx)|FORMATREGEXP'],'assessment':'格式化路径和真实消息/摘要消费者已读；pg只有识别无处理动作；未见覆盖本规则的同名活跃定义。'},
 {'scope':'R/Data/Scripts/011_Battle 与012_Overworld','queries':['pbFindMoveAnimation|pbFindMoveAnimDetails|typeDefaultAnim|showAnims|battle_effects'],'assessment':'默认映射仅场景查找处定义；战斗包装受动画选项及规则门控制，正常真值条件可消费；无同域另一个默认表。'},
 {'scope':'R/Data/Scripts 全部脚本','queries':['class PokemonPokedexInfo_Scene|def pbUpdateDummyPokemon|def setIconBitmap|DEX_SHOWS_ALL_FORMS|pbDexEntry|pbStartSceneSingle','def last_form_seen|def set_last_form_seen|def seen_form?'],'assessment':'列表和条目直接固定普通，设置只绕过已见形态门；正常概要/获得caller已核。不声称外部插件不存在。'},
 {'scope':'R/Data/Scripts 全部脚本','queries':['def pbEncountersEditor|def pbEncounterMapVersionEditor|def pbEncounterTypeEditor|class Encounter'],'assessment':'编辑器三层唯一活跃定义及菜单caller；登记/构造没有补空类型，PBS写出是后续独立过滤。'}]
(OUT/'negative-evidence.json').write_text(json.dumps(neg,ensure_ascii=False,indent=2)+'\n')

report=f'''# CB 有界独立反证报告

结论：6条候选全部逐条裁决，**5条 CONFIRM，1条 CONFIRM_WITH_REFINEMENT**；维持4条P2、2条P3。没有驳回、合并、可选项或核心事实 unresolved；没有新增 GR4-CB 问题。结论仅确认固定参考事实需准确进入规格，不决定未来引擎必须保留这些行为。

审者为本轮新独立CB，未编写输入域报告。身份按 `tasks/CB-launch.json`：thread `{thread}`，PID `{launch['pid']}`；请求gpt-6-astra/ultra/default/noFast，实际回显 **UNVERIFIED**。未查询后端、凭据或私有会话。

B=`{B}`；R=`{R}`。源根只读，采用共享baseline的环境限制；没有重做整仓readiness。输入绑定 `tasks/CB-input-identities.json`。先读根AGENTS.md，全部findings已完整读取；M07/M08/M09各0候选，因此本报告不替这些域签全能力通过。

## 逐项理由

### GR4-M10-001 — CONFIRM / P2

独立核对 `011_Messages.rb:166–205,721–801`、数字和列表组件更新以及事件103、PC调用。普通/帮助命令先处理可用取消；取消被禁用时仍可确认。逐位数字先更新当前位，再检查确认；越界确认继续等待且同轮不再处理取消。

反例确有区分力：两项命令索引0、取消参数2时USE+BACK返回1；数字当前1、取消−1时同输入确认1。尽管两个结果碰巧都是1，各自的对照分别为确认0与取消−1，不是无效反例。数字[3,3]初3，UP+USE+BACK得到编辑值4并蜂鸣继续。事件103默认取消为初值，不能把显式−1说成该事件的默认参数；其UP+USE+BACK仍可区分确认新值与取消初值。

全131检索并读取WP17、WP66-C§5.1、WP65、WP13以及WP67-A战斗列表及MG/B04-M/U05-QN/U05-TX：件数、商店、命名和战斗列表合同都有明确入口范围，不能代替本项。保留与GR3-M10-002的新增消费者关联，不重开其已承接旧范围。输入为同轮查询条件，未证明物理按键组合。

### GR4-M10-002 — CONFIRM / P3

`002_MessageConfig.rb:35–85`的正面事实明确：首次默认读取按所选资源→系统登记名→通用Window→Blue01；显式设置解析失败则留下空资源名称，之后读取不重走首次默认链。核对窗口消费、选项处理、消息空w及事件131：它们是不同操作，不能统一成“设置失败自动恢复默认”。

所选Missing不存在、Custom与备用均存在时首次选Custom；独立显式设置Missing再读为空，足以区分。WP15的单资源解析/空文件名、WP17空w、WP65预览、WP02清单、WP73-A目录失败及对应测试未承接该候选链。确认限于逻辑资源选择；缓存空名称不推出已有消息窗无皮肤、保留原像素或崩溃。缺失资源情境下的有限合同，维持P3。

### GR4-M10-003 — CONFIRM_WITH_REFINEMENT / P2

独立读快路径、一般格式化、标记分流、后处理及消息/摘要调用。正常测量A=B=8、空格4、行宽12、起点0时，AB不逐字硬拆；A B的B移到下一逻辑行。前置pg标记可转入一般路径，行归属结论不变。没有把其绝对纵坐标或最终字形裁切说成相同。

WP17附表§6明确将完整排版留给参考绘制函数；DT04是对齐标记换行，B04-M14是已有显式换行后的行满暂停，WP66-A只列内容，WP08将呈现交给UI。它们不能推导AB/A B差异。消息确实消费布局换行来插暂停，所以缺口超出逐像素外观。

**必需精确化**：拟补规则还应保留宽度检查额外2个测量单位，不能简写成裸文字宽大于行宽。相同A B在宽22仍一行、宽21则B移行，是静态边界对照。向量限定普通样式、自动折行开启、高度不限；登记固定参考事实与未来改进无空格语言排版政策分列。不要求移植整段排版算法。

### GR4-M10-004 — CONFIRM / P2

读场景查找412–485及播放/开关caller、招式类别、目标和默认PBS。六槽表名确实不足以决定身份：FLAMETHROWER无精确映射，给定EMBER→10、SUNNYDAY→20、TACKLE→30时选10；逐个删候选得20、30、空。对方专用EMBER→11优先于共用10。槽号是夹具，不是假称默认动画库编号。

WP67-A§9.4提供六槽与回退骨架；WP74提供作者命名关联，WP03/04提供产物边界；K36只测落空。全131中英文相关别名检索未找到可消费默认身份表。应补行为数据表，保留储存类别/目标输入、候选登记与映射门；不把映射选中等同媒体加载或播放。与动画作者命名合同不是重复根因。

### GR4-M11-001 — CONFIRM / P2

读图鉴记录195–227、主列表766–768、条目139–151及完整/简略入口、形态选择器446–480和资源透传。末次异色可以为真；普通预览、Info及Forms资源请求固定普通；普通刷新不回写末次true。只有实际进入多项形态选择器才另有首轮写false，不能用它解释进入选择器之前的显示。

合法雄性BULBASAUR形态0、末次true，给定不同的普通/异色资源时，按整个三元组直接取图的备选实现会不同，反例成立。仅异色已见也能满足对应形态资格。WP62的记录维度、WP66-B的选择器写入、WP15/17通用图标、PD/BX及摘要/邮件合同均不确定这个调用方的固定参数。M04虽然共享资源文件，但审的是按个体取图引发动态形态读取，根因不同。本项不推广到队伍/战斗个体外观，也不把选中物种预览混称每行拥有图标。

### GR4-M12-001 — CONFIRM / P3

读编辑器完整遭遇三层、登记构造、默认率、菜单caller及PBS输出。正常新增Land后立即返回即可留下零槽，不需损坏输入。整集Copy遍历复制全部率，另过滤零槽类型；构造不补回。源Land(x0)/率21复制到空闲目标后，目标不显示Land且可再次新增，但Land率21仍在。普通结构保真的深拷贝会保留Land(x0)，确实不同。

单类型空Land→未用Cave仍建立空Cave，是有效反向对照。WP73-B§6.4和WP04只在后续PBS写出省空类型；WE-M11无非空限定的“深拷贝”未说明Copy自身过滤；WP36运行空表/快照不补此规则。确认只及编辑登记和保存前列表，不推真实遇敌率或落盘；保持P3。评级/BMP旧问题不与它合并。

## 证据、去重及边界

- `negative-evidence.json`记录10次独立全131检索的词、范围、匹配、实质上下文和结论；并列源码caller/override/开关检索。全131检索不等于逐段通读全部正式文件。各记录具体实际阅读的源与规格见 `verdicts.json`；`read-log.json`是辅助读取范围日志。
- M01–M06共11候选均读ID、标题、源/规格锚点，未发现需合并的根因；共享资源源文件已作M04/M11交界核对。没有为其它域重签全部能力，也不把仅共享文件当重复。读取父会话冻结的有限观察未替代本次取证。
- 六项均为 **SOURCE_STATIC + SPEC_STATIC + DERIVED_VECTOR**。CB没有参考函数、行为模型、输入、字体、UI、动画、编辑器或宿主执行。M10/M11的工具校验不是行为测试；M12隔离评级回执只限Ruby2.6.10的所选结算路径，绕过构造，不涉及遭遇编辑器，绝不是随附Ruby3.1宿主实测。本轮未重跑它。
- 旧状态文字按时点保留，没有据OPEN/PASS标题要求翻改历史档案。已读当前B相邻合同用于反证，不签旧关闭重新通过。未确定第二轮关联时不猜ID。
- 所有写入仅CB目录；没有修改参考、原模块报告、正式规格、Feature Matrix或共享聚合，没有提交/push、联网或启动agent。规范聚合留给父会话。本次有效有界复核到此结束。
'''
(OUT/'report.md').write_text(report)
plan='''# CB 执行记录计划\n\n候选事实取证已完成，不追加行为探针。接下来唯一专项执行是本目录产物校验。\n\n- 目的：检查6个输入ID恰有6个裁决、schema及必需字段、证据枚举、10次全131检索、所消费findings冻结身份，以及源码/规格实际阅读路径在读取日志中。不是行为测试。\n- 输入：CB的verdicts.json、negative-evidence.json、read-log.json、report.md；固定CB-input-identities.json及M07–M12 findings.json。\n- 命令：python3 review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/CB/validate_review.py\n- 版本：共享baseline报告Python3.14.0；执行中只回显当前Python解释器版本。\n- 预期输出：PASS_TOOL_VALIDATION_ONLY及计数；若失败仅修CB产物。\n- 副作用：只写CB/validation-result.json及CB/execution.json；不执行或改写R、B，不读取真实存档、不联网。\n'''
(OUT/'validation-plan.md').write_text(plan)
execution={'schema_version':'1.0','reviewer':'CB','thread_id':thread,'pid_from_launch':launch['pid'],'identity_source':'tasks/CB-launch.json','requested':launch['requested'],'actual_echo':'UNVERIFIED',
 'behavior_execution_count':0,'actual_executions':[],
 'static_read_and_administrative_activity':[
  {'tool':'exec_command','commands':['pwd; cat AGENTS.md (read-only)','cat / Python JSON reads of baseline, launch, frozen manifest, six domain findings and bounded cross-domain metadata','git show B:path / git -C R show R:path','rg -n -i pattern <all 131 formal paths>','rg -n pattern <relevant R script scope>','python3 CB/finalize_audit.py (artifact assembly)'],'purpose':'静态阅读/检索及本目录产物装配','outputs':'对话工具输出；CB/read-log.json、negative-evidence.json、verdicts.json、report.md、progress.md和本目录辅助脚本','side_effects':'仅CB写入；git show/rg不改R或正式文件','evidence_level':['SOURCE_STATIC','SPEC_STATIC'],'not_behavior_execution':True}],
 'previous_evidence_assessed':[
  {'path':'modules/M10/execution.json','assessment':'产物校验，非行为执行，不能证明四候选；CB不重跑'},
  {'path':'modules/M11/execution.json','assessment':'小游戏字面数据与产物校验，不证明图鉴消费；CB不重跑'},
  {'paths':['modules/M12/rating-execution.json','modules/M12/rating-probe.rb'],'assessment':'原回执Ruby2.6.10隔离原评级/历史/结算路径，allocate绕过队伍构造；没有遭遇编辑器调用，不支持GR4-M12-001。CB仅读记录与探针范围，未重新认证其数值。不是Ruby3.1宿主实测。'}],
 'not_executed':[
  {'kind':'EXECUTED_REFERENCE','scope':'CB未执行任何参考Ruby函数或脚本'},
  {'kind':'EXECUTED_MODEL','scope':'CB未编写或执行行为模型'},
  {'kind':'EXECUTED_HOST_OR_DEMO','scope':'未启动宿主/地图/图鉴/UI/动画/编辑器；未观察真实输入、字体、媒体'},
  {'kind':'DERIVED_VECTOR','scope':'六项最小、正常及边界向量全部NOT_EXECUTED'},
  {'kind':'OTHER','scope':'未编译、反序列化、联网、读写真实存档、写参考或正式文件、提交/push、启动agent、查后端/凭据/私有会话'}],
 'planned_tool_validation':'validation-plan.md'}
(OUT/'execution.json').write_text(json.dumps(execution,ensure_ascii=False,indent=2)+'\n')
(OUT/'progress.md').write_text('''# CB 进度\n\n六条候选的一次独立针对性复核已完成：5 CONFIRM、1 CONFIRM_WITH_REFINEMENT，P2四条/P3两条。已读R原锚点、调用/覆盖/开关及B正文/合理共享/附表/测试，已做10次全131相关别名检索。M01–M06十一候选仅作ID/标题/锚点跨域去重；M07–M09零候选不补签。\n\nreport.md、verdicts.json、negative-evidence.json、execution.json已形成。仅待按validation-plan.md运行一次产物结构/冻结输入身份校验；不追加行为执行或重审。\n\n写入仅CB，无参考/正式规格/原报告/共享聚合变更，无提交/push/联网/agent。实际模型回显UNVERIFIED。\n''')
print(json.dumps({'written':['report.md','verdicts.json','progress.md','execution.json','negative-evidence.json','validation-plan.md'],'records':len(records),'searches':len(neg['searches']),'cross_domain_candidates':len(cross)},ensure_ascii=False))
