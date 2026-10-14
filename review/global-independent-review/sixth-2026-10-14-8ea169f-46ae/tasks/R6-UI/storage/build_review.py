import json, re, subprocess, hashlib
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT=ROOT/'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-UI/storage'
MAIN='8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
SPEC='deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md'
TEST='deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md'
PREFIX='reference/pokemon-essentials/Data/Scripts/'
FILES={
'M':PREFIX+'016_UI/002_UI_Pokedex_Menu.rb',
'L':PREFIX+'016_UI/003_UI_Pokedex_Main.rb',
'E':PREFIX+'016_UI/004_UI_Pokedex_Entry.rb',
'S':PREFIX+'016_UI/017_UI_PokemonStorage.rb',
'D':PREFIX+'014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb',
'PC':PREFIX+'016_UI/019_UI_PC.rb',
'PAUSE':PREFIX+'016_UI/001_UI_PauseMenu.rb',
'PARTY':PREFIX+'016_UI/005_UI_Party.rb',
'SUM':PREFIX+'016_UI/006_UI_Summary.rb',
'BAG':PREFIX+'016_UI/007_UI_Bag.rb',
'PURIFY':PREFIX+'016_UI/023_UI_PurifyChamber.rb',
'PD':PREFIX+'015_Trainers and player/005_Player_Pokedex.rb',
'P':PREFIX+'014_Pokemon/001_Pokemon.rb',
'IU':PREFIX+'013_Items/001_Item_Utilities.rb',
'MAIL':PREFIX+'013_Items/006_Item_Mail.rb',
'U':PREFIX+'019_Utilities/001_Utilities.rb',
'ENC':PREFIX+'010_Data/002_PBS data/013_Encounter.rb',
'ITEM':PREFIX+'010_Data/002_PBS data/006_Item.rb',
'SHAPE':PREFIX+'010_Data/001_Hardcoded data/004_BodyShape.rb',
'COLOR':PREFIX+'010_Data/001_Hardcoded data/005_BodyColor.rb',
'GLOBAL':PREFIX+'012_Overworld/002_Overworld_Metadata.rb',
'SET':PREFIX+'001_Settings.rb'}

def get(path):
    repo=ROOT/'reference/pokemon-essentials' if path.startswith('reference/pokemon-essentials/') else ROOT
    rel=path.removeprefix('reference/pokemon-essentials/') if repo!=ROOT else path
    rev=REF if repo!=ROOT else MAIN
    return subprocess.check_output(['git','-C',str(repo),'show',rev+':'+rel]).decode()

def refs(text):
    ans=[]
    for token in text.split(';'):
        key, span=token.split(':'); a,b=(span.split('-')+[None])[:2]
        ans.append({'path':FILES.get(key,key),'start_line':int(a),'end_line':int(b or a),'commit':REF if key in FILES else MAIN})
    return ans

def dump_jsonl(name, rows):
    (OUT/name).write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))

# Each row below is authored after semantic reading, never inferred from delivery or syntax alone.
# Fields: start line | behavior fact | formal line anchors | scope disposition.
raw={
'M':'''8|区域命令绘制使用独立见过/拥有计数字段；字体/窗口皮肤仅呈现|136|PRESENTATION_RESERVED
17|区域行分别展示见过数与拥有数，完成标记分别比较对应计数和长度|136|SUPPORTED_STATIC
42|更新区域菜单的呈现对象，不提交玩家集合|136|PRESENTATION_RESERVED
46|区域菜单初始化背景、见过/拥有标题和命令窗口后显示|136|SUPPORTED_STATIC
66|BACK优先于USE；BACK返回负取消值，确认末行Exit与区域条目走不同关闭/打开声音请求|136|SUPPORTED_STATIC
84|正常退出淡出并释放菜单呈现资源，无区域字段回滚|136|SUPPORTED_STATIC
95|记录区域菜单场景用于后续流程|136|STRUCTURAL_ONLY
99|可访问区域按当前缓存顺序生成名字及见/拥有/长度；区域选择先写观看区域，主列表关闭后回菜单|128,136|SUPPORTED_STATIC''',
'L':'''5|列表初始化见过与拥有两种状态标记及列表光标；媒体实际未证|150|PRESENTATION_RESERVED
16|替换当前列表内容并立即重绘，不提交图鉴记录|146,221|SUPPORTED_STATIC
21|列表关闭释放状态图标资源；不提交记录|152|PRESENTATION_RESERVED
27|空列表的当前物种查询给空身份占位；正常列表返回当前行物种|146,150|SUPPORTED_STATIC
31|列表数量取当前命中/区域列表长度|146,188|SUPPORTED_STATIC
35|行编号按偏移设置调整；已见显示名和拥有/见过标记，未见显示姓名占位|148,150|SUPPORTED_STATIC
59|仅重绘可见列表行及游标，未单独提交索引|140,150|PRESENTATION_RESERVED
72|常规更新继承选择行为，同时隐藏通用上下箭头|150|PRESENTATION_RESERVED
87|搜索焦点图形初始在主画面模式、索引0；呈现未知|156|PRESENTATION_RESERVED
96|关闭搜索焦点图形释放图像|156|PRESENTATION_RESERVED
101|改变搜索焦点后刷新焦点图形，与已选参数分层|196|SUPPORTED_STATIC
106|排序/名字/类型/颜色/形状逻辑列数分别为2/7/4/3/5；大小页用双端标尺|194,198|SUPPORTED_STATIC
147|主/子搜索焦点分别区分候选、未选、OK/Cancel及双端；布局细节不作为未来约束|165,196|PRESENTATION_RESERVED
260|更新图鉴呈现对象，不在此提交记录|140|PRESENTATION_RESERVED
264|场景建立时接受参数初始化为持久模式和空过滤；初始非搜索态，按区域保存索引恢复列表|140,156|SUPPORTED_STATIC
300|正常关闭场景淡出并释放图鉴资源；不恢复持久排序或索引|221,276|SUPPORTED_STATIC
317|按配置取当前地图区域或观看区域，当前地图区域超出地区目录映射为全国|130,140|SUPPORTED_STATIC
330|全国保存索引使用区域数组最后一项，其它区域按区域号|140|SUPPORTED_STATIC
338|字母模式只纳入已见，四体型模式只纳入拥有，数值模式不按已见过滤|146|SUPPORTED_STATIC
348|区域表缺/空回退基础物种全集；各行保持原区域编号，名字与筛选字段用末次形态|146|SUPPORTED_STATIC
378|非搜索列表数值修剪首个偏移未见行/尾连续未见；常规排序含编号平局规则，刷新背景与索引|148|SUPPORTED_STATIC
417|普通列表显示区域见/拥有计数；结果态显示命中数；预览仅已见物种且读取普通外观|150,152,188|SUPPORTED_STATIC
479|主搜索呈现十参数，未选/表长端点映射不同；US体重除0.254而非信息页的0.45359|156,231,265|SUPPORTED_STATIC
551|子搜索展示候选与本地选择；高度/重量大小页与主搜索同一异常US换算；不提交外层参数|165,196,231|SUPPORTED_STATIC
766|预览取末次性别/形态，固定普通外观；不覆盖已存异色值|152|SUPPORTED_STATIC
771|搜索先写持久模式，再建立和过滤列表；按名字首字符/属性/闭含大小/颜色形状过滤并最终剔未见；搜索排序没有独立编号平局比较|188|SUPPORTED_STATIC
851|退出结果态清标志、模式复位数值、会话参数复位；先恢复保存位置，再按旧物种找回，写索引|221|SUPPORTED_STATIC
868|条目使用区域配置映射；返回结果态按接受参数重跑且夹索引，普通态重建并写返回索引|221|SUPPORTED_STATIC
896|子页克隆已选参数；大小先焦点上界；方向和按钮两阶段，类型禁重复、填空及轮转；取消不提交|165,186,194,196,198,211,215|SUPPORTED_STATIC
1092|进入搜索克隆会话；各子页OK写草稿，Reset只改草稿；主画面互斥输入；命中接受参数/列表，零命中保留旧结果和会话但模式已写|156,188,190,217|SUPPORTED_STATIC
1255|列表更新导航后非结果态写观看索引；ACTION先于BACK先于USE；只有已见物种可开条目|140,150,221|SUPPORTED_STATIC
1293|记录主图鉴场景引用|128|STRUCTURAL_ONLY
1297|完整主列表正常生命周期依序建立、输入、收尾，无新增事务回滚|128,276|SUPPORTED_STATIC''',
'E':'''5|完整条目先设置第一页及身高体重展示；负区域用当前地图区域或0，建立地图、信息和形态资源并算可列形态|229,231|SUPPORTED_STATIC
71|简略入口仅信息页；全国解锁优先编号，否则逐已解锁区域遇缺继续；初始不打开地图/Forms|244|SUPPORTED_STATIC
119|正常关闭条目淡出释放图鉴资源，不恢复末次形态|239|SUPPORTED_STATIC
126|Area高亮按时间变化更新，其它页面常规呈现更新；实际像素/时序未证|231|PRESENTATION_RESERVED
139|所有完整/简略前图和Forms前背图/图标都读取末次性别形态并固定普通外观|233,246|SUPPORTED_STATIC
154|形态结构门先于已见门、多形态结构标志早于已见；单一性别、同图基形折雄、具名停止、缺标签补名及排序不同|237|SUPPORTED_STATIC
202|按当前页选择信息/地图/形态并调整可见资源，普通刷新不提交末次记录|229,233|SUPPORTED_STATIC
221|信息编号非正为问号；拥有门控制类别/身高体重/文本/足迹/拥有/属性；战斗过查询不由拥有门隐藏；US与非US单位差异|231|SUPPORTED_STATIC
302|遭遇资格在任一槽位基础物种与目标相符时成立；无遭遇集合为假|231|SUPPORTED_STATIC
313|可见地图点取无门或开门并集；合法遭遇/地图/区域/非隐藏门；宽正按已有非零字符，缺省/零宽一格|231|SUPPORTED_STATIC
354|Area按要点画高亮，空要点显示未知，显示地区与物种名；图像/逐帧未知|231|SUPPORTED_STATIC
403|Forms名称取可列列表中当前性别形态匹配标签；不匹配则空标签，不提交末次|237|SUPPORTED_STATIC
424|前一物种查询跳过未见，首端夹停|229|SUPPORTED_STATIC
435|后一物种查询跳过未见，末端夹停|229|SUPPORTED_STATIC
446|形态选择先匹配末次，否则首项；首轮及每次变动先写记录，上下在首末回绕；BACK/USE退出保留写入|239|COVERAGE_GAP_PENDING
485|完整条目ACTION/BACK/USE/UP/DOWN/LEFT/RIGHT互斥；翻页夹1..3、物种跳未见、USE信息切换/Forms多项进入，进入播叫声|229,231|SUPPORTED_STATIC
557|简略信息ACTION停音再叫声，BACK或USE关；不提供完整页导航|244|SUPPORTED_STATIC
578|记录条目场景引用|243,244|STRUCTURAL_ONLY
582|完整条目返回最后物种索引，正常收尾不回滚浏览写入|229,239|SUPPORTED_STATIC
590|摘要独立入口取当前/观看图鉴编号并构造单物种完整三页；自身不登记最近见到，调用方先登记|243|SUPPORTED_STATIC
614|简略条目生命周期，编号和内容由简略场景生成|244|SUPPORTED_STATIC''',
'S':'''5|盒格个体图标关联目标并初始化释放状态；素材未知|47,150|PRESENTATION_RESERVED
12|释放演出活动状态与领域删除分层|47,102|PRESENTATION_RESERVED
16|释放演出调整图标中心并开始淡出缩放计时，无集合删除|47,102|PRESENTATION_RESERVED
24|盒格个体图标请求个体素材并只选首方格，不套HP动画|150|SUPPORTED_STATIC
30|释放图标在演出中缩小淡出到结束释放图形；集合后续由操作方提交|47,102|PRESENTATION_RESERVED
52|初始化预览像素化缓存与初始强度|47|PRESENTATION_RESERVED
61|预览关闭清掉临时图像缓存|47|PRESENTATION_RESERVED
69|预览换图会重绘像素化图，不写玩家集合|47,264|PRESENTATION_RESERVED
74|像素化强度负值归0、重绘预览|47|PRESENTATION_RESERVED
80|像素化重绘防再入；强度0或无图恢复原图，其它缩放到至少1像素|47|PRESENTATION_RESERVED
115|自动像素化记录开始强度，负强度归0|47|PRESENTATION_RESERVED
121|自动像素化时长负值归0，正时长启计时|47|PRESENTATION_RESERVED
127|自动像素化从起始强度到0，结束清计时状态；实际宿主/图像未证|47|PRESENTATION_RESERVED
152|盒游标初始化无暂持、无快捷交换及手型图形|65,71|SUPPORTED_STATIC
172|游标关闭释放手形和暂持图标；领域成员处理另属屏幕|47,71|PRESENTATION_RESERVED
178|游标横向变更同步手型及暂持图标位置|71,264|PRESENTATION_RESERVED
185|游标纵向变更同步手型及暂持图标位置|71,264|PRESENTATION_RESERVED
192|游标层级同步手型层级|47|PRESENTATION_RESERVED
197|游标显隐同步手型和暂持图标|47|PRESENTATION_RESERVED
204|游标着色同步手型和暂持图标|47|PRESENTATION_RESERVED
211|已经释放/缺失的暂持图标使呈现暂持状态清空；与屏幕暂持对象分层|71|PRESENTATION_RESERVED
217|呈现暂持要求图标存在且持有状态成立，不等价直接领域成员对象|71|PRESENTATION_RESERVED
221|取成员演出活动标记，用于等待演出结束|47,99|PRESENTATION_RESERVED
225|放成员演出活动标记，用于等待演出结束|47,100|PRESENTATION_RESERVED
229|呈现交换可替换暂持图标，空图标清呈现暂持|71,101|PRESENTATION_RESERVED
239|清呈现暂持并释放其图标，不单独提交集合|71|PRESENTATION_RESERVED
247|拿起图标启动抓取演出并设暂持图标；领域源稍后删|47,99|PRESENTATION_RESERVED
255|放置图标启动演出计时，不单独提交集合|47,100|PRESENTATION_RESERVED
259|暂持图标释放演出，与屏幕暂持清空分层|47,102|PRESENTATION_RESERVED
263|游标抓/放/持/闲置图形与计时转换，快捷交换改变皮肤，媒体时序未证|47,65|PRESENTATION_RESERVED
315|盒初始化按固定默认网格建图标并立即读取背景，可能触发背景记录归一|254|SUPPORTED_STATIC
334|盒关闭释放成员图标及背景，成员集合不回滚|122|PRESENTATION_RESERVED
346|盒移动更新图形位置，刷新标志决定背景是否重读|47,254|PRESENTATION_RESERVED
351|盒移动更新图形位置，刷新标志决定背景是否重读|47,254|PRESENTATION_RESERVED
356|盒着色可避成员图标刷新，用于墙纸切换|47,105|PRESENTATION_RESERVED
368|盒显隐同步个体图标|47|PRESENTATION_RESERVED
378|背景初读/与缓存不同时重读；空值仅默认显示；匹配旧文本写整数；不可用写默认；缓存同不重验可用性|254|SUPPORTED_STATIC
399|盒呈现图标按格读取，不压缩空格|111|PRESENTATION_RESERVED
403|盒格替换呈现图标并刷新，无直接集合提交|100,101|PRESENTATION_RESERVED
409|呈现拿起后盒图标源位置留空，屏幕随后删除实际源|99|PRESENTATION_RESERVED
418|呈现删除释放该格图标，盒格不压缩|102|PRESENTATION_RESERVED
424|按标志刷新盒名/背景后清标志，并将图标布到6列5行|59,254|SUPPORTED_STATIC
453|盒图标逐格更新，不直接读写集合|47|PRESENTATION_RESERVED
467|队伍面板按配置上限建现有成员图标，空位置不画|65,260|SUPPORTED_STATIC
485|面板关闭释放成员和背景图形|47|PRESENTATION_RESERVED
494|面板横向移动后重绘|75|PRESENTATION_RESERVED
499|面板纵向移动后重绘|75|PRESENTATION_RESERVED
504|面板着色同步非空图标|47|PRESENTATION_RESERVED
513|面板显隐同步非空图标|75|PRESENTATION_RESERVED
522|队伍呈现按序号取图标|75,111|PRESENTATION_RESERVED
526|队伍替换图标后压缩空图标；领域队伍压缩在屏幕/领域层|100|PRESENTATION_RESERVED
532|拿起队伍图标删除该呈现序号并压缩|99|PRESENTATION_RESERVED
541|释放队伍图标删除并压缩|102|PRESENTATION_RESERVED
548|队伍面板显示返回按钮；按双列布局刷新图标，弃已释放图标|65,75|SUPPORTED_STATIC
572|面板更新现有非空图标|47|PRESENTATION_RESERVED
589|场景保存默认命令状态，真正入口覆盖为传入模式|34,35,36|STRUCTURAL_ONLY
593|进入重置游标0/快捷交换关/面板来源假；模式2常驻队伍，其它隐藏队伍；初读背景可能写记录|34,35,36,65,254|SUPPORTED_STATIC
649|关闭盒界面正常淡出资源释放，领域集合不回滚；宿主释放结果未知|122|PRESENTATION_RESERVED
658|盒消息窗口直接显示全文，BACK或USE任一关闭；正常结束刷新输入|287|SUPPORTED_STATIC
679|操作命令默认首项或调用者指定项；BACK先于USE返回负取消，USE返回焦点|83,85,86,87,118,120|COVERAGE_GAP_PENDING
716|盒特殊焦点与成员焦点分别定位游标，不提交状态|59,60,61,62|PRESENTATION_RESERVED
733|盒网格上下6格、顶到盒名、底分队伍/关闭；左右在同一行回绕，盒名左右为瞬态切盒|65|SUPPORTED_STATIC
793|队伍焦点按配置生成双列坐标，末项为返回按钮；负焦点不更新|65|PRESENTATION_RESERVED
811|队伍成员左右依连续序列回绕，上下2格越界到末按钮；末按钮UP到最后成员、DOWN到首成员|65|COVERAGE_GAP_PENDING
837|盒方向repeat先按UP/LEFT/RIGHT/DOWN优先，再独立JUMPUP/JUMPDOWN/SPECIAL/ACTION可用/BACK/USE；切盒即写，回传特殊位置|63,65,67|COVERAGE_GAP_PENDING
912|模式1只盒选择器；其它在队伍按钮打开面板，队伍取消收起并恢复盒按钮，成员返回队伍位置|35,39,75|SUPPORTED_STATIC
938|队伍方向repeat先处理再ACTION可用/BACK/USE；末按钮存入返回关闭编码，整理返回面板取消|65,75|COVERAGE_GAP_PENDING
987|存入选择器调用队伍选择并允许末按钮关闭界面|36,65|SUPPORTED_STATIC
991|墙纸切换先淡出，实际新背景值在换入阶段写入，之后显示；异常不承诺回滚|105|SUPPORTED_STATIC
1020|切右盒先创建目标盒，初始化可写目标背景，再滑动替换盒图形；当前盒字段由调用方稍后写|63,67,254|SUPPORTED_STATIC
1037|切左盒先创建目标盒，初始化可写目标背景，再滑动替换盒图形；当前盒字段由调用方稍后写|63,67,254|SUPPORTED_STATIC
1054|Jump到同盒无操作，否则按前后切盒后写当前盒|105|SUPPORTED_STATIC
1064|暂持时导航不重新开始像素化；非暂持时当前盒/焦点改变才启动效果|264|OVERBROAD_CLAUSE_PENDING
1072|快捷交换值同时更新场景状态及游标皮肤|65|SUPPORTED_STATIC
1077|显示队伍面板保留暂持；未暂持时清预览并启动过渡|75,264|SUPPORTED_STATIC
1097|隐藏队伍面板保留暂持；未暂持时清预览并启动过渡|75,264|SUPPORTED_STATIC
1117|拿起先搬呈现图标并等待抓取完成，实际删源由屏幕随后执行|99|SUPPORTED_STATIC
1131|交换图标后显式重启像素化预览，随后屏幕将持有对象换成原目标|101,264|OVERBROAD_CLAUSE_PENDING
1151|放下演出结束后目标格取得图标，领域写入稍后发生|100|SUPPORTED_STATIC
1169|取出先拿起图标/展队伍/放到队末/收队伍，再返回领域提交|97|SUPPORTED_STATIC
1177|存入呈现将持有/队伍图标移至当前盒或删除异盒源图标；实际成员由屏幕提交|98|SUPPORTED_STATIC
1197|释放选暂持/队伍/盒图标并等待释放动画；实际删除后续发生|102|SUPPORTED_STATIC
1217|盒选择列表依序显示名称与占用/容量，初焦点当前盒，BACK负取消|98,105|SUPPORTED_STATIC
1228|盒名输入返回非空才写名，返回后刷新并恢复原呈现可见集|105|SUPPORTED_STATIC
1237|背包选择过滤仅可携带，独立场景正常返回；背包浏览位置恢复由背包消费者实现|103|SUPPORTED_STATIC
1247|暂持摘要用单项/0，队伍用完整队伍、盒用完整盒容器；返回游标写回，无容器重排|111|SUPPORTED_STATIC
1265|标记焦点定位六位及OK/Cancel按钮，具体像素未证|104|PRESENTATION_RESERVED
1278|标记导航六位3列两行，左右同行回绕，上下连OK/Cancel；无领域提交|104|SUPPORTED_STATIC
1314|克隆标记作草稿，初焦点0；方向repeat后BACK优先USE；USE标记循环变体，OK一次提交，取消弃稿|104|SUPPORTED_STATIC
1394|普通刷新盒/队伍图形，不重建容器|111|PRESENTATION_RESERVED
1399|硬刷新重建盒及队伍图形，保留队伍面板纵向位置；盒初始化可写背景|111,254|SUPPORTED_STATIC
1408|标记绘制按图集尺寸计数变体/位数，过大显示值夹最后变体；不提交标记|104|PRESENTATION_RESERVED
1418|预览优先当前暂持对象，其次当前位置；空隐藏；非蛋显示性别/等级/特性/持物/类型/异色标记/标记，更新个体图像|264|OVERBROAD_CLAUSE_PENDING
1481|更新盒呈现对象，不单独提交集合|47|PRESENTATION_RESERVED
1494|储存屏幕绑定场景和容器，实际暂持字段在入口清空|30,71|STRUCTURAL_ONLY
1500|普通模式置临时储存标记真、暂持空；模式0拿/放/交换菜单或快捷，1/2专门菜单；BACK与关闭确认分流，模式3开即关；正常末尾标记假|30,34,35,36,37,83,84,85,86,118,120,122|SUPPORTED_STATIC
1662|调试更新钩子只转呈现更新，不对正常模式作新领域规则|83|DEMO_DX_REFERRED
1667|调试硬刷新钩子重建盒/队伍图形|83|DEMO_DX_REFERRED
1672|调试单项刷新选择对应容器预览再硬刷新|83|DEMO_DX_REFERRED
1677|消息包装转交盒消息显示|287|STRUCTURAL_ONLY
1681|盒通用确认命令Yes在首项、No次项，只有索引0为真，取消为假；释放另用No/Yes|118,120,103,102|COVERAGE_GAP_PENDING
1685|命令包装默认焦点0转交场景，与调用方显式焦点分层|83,105|COVERAGE_GAP_PENDING
1689|可用成员为存在且非蛋且HP正|23,93,263|SUPPORTED_STATIC
1693|可用数只统计当前容器队伍，不计暂持|23,93,263|SUPPORTED_STATIC
1701|实际暂持查询返回屏幕成员对象，不取呈现图标|71|SUPPORTED_STATIC
1705|取出队伍位置报错；满队拒；先演出后持有捕获入队并清持有或普通源移动；正常刷新|97|SUPPORTED_STATIC
1724|存入非队伍位置报错；逐目标最后可用/邮件/禁止存守卫；盒满重试、取消不治不移；治疗保进化准备后演出再领域移|98|SUPPORTED_STATIC
1770|拿起队伍最后可用拒；先演出，随后赋暂持再删实际源并刷新|99,71|SUPPORTED_STATIC
1784|放非空报错；非队伍容量/邮件/禁止存守卫；非负盒按配置治疗保进化准备；演出后写格、队伍压缩、刷新再清暂持|100|SUPPORTED_STATIC
1813|交换空报错；禁止存/最后可用/邮件各条件拒；治疗保进化准备后演出、目标写持有、暂持变原目标、刷新|101|SUPPORTED_STATIC
1845|释放蛋/邮件/不可释放拒；未持队伍最后可用拒且无确认；确认默认No，Yes先演出后删/清暂持再两消息|102|SUPPORTED_STATIC
1882|调试选招将各已知招式显示当前/总PP或无总PP占位；取消返回命令负值|83|DEMO_DX_REFERRED
1894|摘要包装转交场景，持有/容器输入分层|111|STRUCTURAL_ONLY
1898|标记包装转交场景，输入草稿/提交由场景管理|104|STRUCTURAL_ONLY
1902|道具拒蛋/邮件；取物确认成功先入袋、提示后清物；给物正常选择后先写持物再袋删除、提示、硬刷新|103,107|SUPPORTED_STATIC
1936|盒命令依Jump/Wallpaper/Name/Cancel，默认首项；Jump选择初焦点当前盒；墙纸初焦点当前背景在可用列表的匹配否则首项；取消无命令写入|105|SUPPORTED_STATIC
1964|选择模式置储存标记真、模式1进入；无取出模式队伍按钮拦截，负位置寻址后选可返回原位置，操作可改集合；正常收尾标记假|30,39,41,87|SUPPORTED_STATIC'''}

forward=[]
for k in 'MLES':
    text=get(FILES[k]); lines=text.splitlines()
    defs=[n for n,l in enumerate(lines,1) if re.match(r'\s*def ',l)]
    authored={}
    for line in raw[k].splitlines():
        start,fact,anchors,disp=line.split('|')
        authored[int(start)]=(fact,[int(a) for a in anchors.split(',')],disp)
    assert set(defs)==set(authored),(k,set(defs)^set(authored))
    for j,start in enumerate(defs):
        end=(defs[j+1]-1 if j+1<len(defs) else len(lines))
        fact,anchors,disp=authored[start]
        fid=f'UI-ST-{k}-{start:04d}'
        forward.append({'id':fid,'source_unit':{'path':FILES[k],'start_line':start,'end_line':end,'unit_boundary':'definition start through line before next definition; includes trailing separators/declared context','commit':REF},'inventory_status':'INVENTORIED','structural_status':'INSPECTED','semantic_status':'SEMANTIC_READ_AND_ANALYZED','fact':fact,'necessary_consumers':[],'formal_links':[{'path':SPEC,'line':a} for a in anchors],'disposition':disp,'evidence_type':'STATIC_SOURCE_REASONING','actual_reference_execution':'NOT_EXECUTED','independent_model_execution':'NOT_EXECUTED','host_demo_media_observation':'UNKNOWN'})

# Named consumers are audit dependencies, not architecture recommendations.
for f in forward:
    id=f['id']
    consumers={
    'UI-ST-M-0099':'PAUSE:133-163;PD:315-332;PD:351-358;U:401-418;L:264-298',
    'UI-ST-L-0264':'GLOBAL:75-82;L:378-415',
    'UI-ST-L-0317':'U:380-383;PD:315-332',
    'UI-ST-L-0348':'U:401-405;PD:129-132',
    'UI-ST-L-0766':'PD:129-132',
    'UI-ST-L-0771':'L:348-375;L:1224-1235',
    'UI-ST-L-0851':'L:378-415;L:1266-1283',
    'UI-ST-L-0868':'E:582-587;L:771-848',
    'UI-ST-L-0896':'L:1182-1218;SHAPE:34-116;COLOR:30-78',
    'UI-ST-E-0071':'U:389-398',
    'UI-ST-E-0139':'PD:129-132',
    'UI-ST-E-0154':'PD:61-69;E:507-511',
    'UI-ST-E-0313':'ENC:53-60;E:302-308',
    'UI-ST-E-0446':'PD:138-140;E:507-511;L:868-894',
    'UI-ST-E-0590':'SUM:1218-1225',
    'UI-ST-S-0378':'D:101-106;S:424-435',
    'UI-ST-S-0593':'PC:163-218;PARTY:774-781;D:65-76',
    'UI-ST-S-0679':'S:1681-1687;S:1865-1866;S:1217-1226;S:1950-1958',
    'UI-ST-S-0811':'S:938-985',
    'UI-ST-S-0837':'S:912-936;S:1507-1526;S:1967-1985',
    'UI-ST-S-0912':'S:1592-1605;S:1967-1985;D:159-167',
    'UI-ST-S-0938':'S:1626-1650',
    'UI-ST-S-1064':'S:837-841;S:1131-1149;S:1418-1479',
    'UI-ST-S-1131':'S:1813-1842;S:1418-1479',
    'UI-ST-S-1237':'BAG:591-600;ITEM:189-194',
    'UI-ST-S-1247':'SUM:1215-1225;MAIL:100-125;IU:781-822',
    'UI-ST-S-1500':'PC:163-218;PARTY:774-781;P:147-152',
    'UI-ST-S-1681':'S:679-714;S:1508-1524;S:1913-1923;S:1971-1980',
    'UI-ST-S-1705':'D:189-192;D:206-215;S:1169-1175',
    'UI-ST-S-1724':'D:178-209;D:217-228;P:300-306;S:1177-1195',
    'UI-ST-S-1770':'D:254-259;S:1117-1129',
    'UI-ST-S-1784':'D:136-139;D:170-175;P:300-306;S:1151-1167',
    'UI-ST-S-1813':'D:170-175;P:300-306;S:1131-1149',
    'UI-ST-S-1845':'D:254-259;S:1197-1215;S:679-714',
    'UI-ST-S-1902':'BAG:591-600;PARTY:1434-1484;S:1237-1245',
    'UI-ST-S-1936':'D:108-118;S:1217-1235;S:1054-1062',
    'UI-ST-S-1964':'PURIFY:1273-1281;D:159-167;S:912-914;S:1592-1595'}
    if id in consumers:f['necessary_consumers']=refs(consumers[id])

dump_jsonl('forward-matrix.jsonl',forward)
print(json.dumps({'forward_units':len(forward),'all_authored_units_match_inventory':True}))

# Reverse evidence is authored clause-by-clause. Formatting blocks receive STRUCTURAL_ONLY,
# and historical/scope assertions never receive a source-behavior PASS merely by being read.
reverse_rules={}
def rr(lines,summary,sources,premise='合法默认无插件，调用链正常返回；静态行为推导，不证明实体输入、素材或Demo。',status='SUPPORTED_STATIC'):
    for line in lines: reverse_rules[line]=(summary,sources,premise,status)
rr([17],'PC创始人显示门与四命令菜单','PC:156-180','元数据/玩家标记存在；创始人事件写入者未验证。')
rr([21],'整理无额外PC前置进入模式0','PC:182-188')
rr([22],'整队满队拦取出入口','PC:189-198')
rr([23],'PC存入入口按整队非蛋且HP正计数≤1拦截','PC:199-212')
rr([24,26],'返回/取消PC层，区分入口门和逐目标门','PC:170-217;S:1724-1738','帮助命令取消契约引用WP17；当前审只确认调用值与退出分支。')
rr([30],'普通/选择入口置储存临时标记真，正常收尾置假；动态形态查询短路','S:1500-1503;S:1654-1659;S:1964-1968;S:2018-2020;P:147-152','正常返回；异常无ensure回写，不证明外层恢复。强制形态先于储存标记，形态本体WP21。')
rr([34],'整理双层选择器及队伍SPECIAL普通桥','S:593-647;S:912-936;PARTY:774-781;PC:183-188','Box Link许可与非快捷目标门成立；完整队伍界面归WP66-A。')
rr([35],'取出模式只内部盒选择器','S:912-914;S:1584-1622')
rr([36],'存入常驻队伍面板且队伍选择器','S:621-625;S:637-642;S:1623-1653')
rr([37,277],'模式3开即关，正常调用者搜索未命中','S:1654-1658','四个指定源全文及全Data/Scripts调用名搜索；不证明事件或插件无调用。', 'SUPPORTED_WITH_NEGATIVE_SEARCH_LIMIT')
rr([39,41],'选择模式画面1、位置返回、内含修改；队伍按钮负地址泄漏','S:1964-2020;S:912-914;S:903-906;S:1592-1595;D:159-167;PURIFY:1273-1281','默认基础40盒×30格；负索引语义只用于该局部读取和Select，不穷尽负地址Withdraw/Store后续。')
rr([45,47,48,49],'呈现、选择守卫与分散提交为行为职责；呈现效果与领域写入分层','S:1117-1215;S:1705-1879;S:1902-1962;S:837-910','像素、音效、逐帧输出未执行；呈现初始化读取背景另由254限定。')
rr([55,59],'普通盒网格0..29位置编码','S:899-900;D:9-17','默认6×5网格；自定义容量不把显示网格推成动态容器不变量。')
rr([60],'盒名位置返回盒命令编码','S:901-902;S:1525-1526')
rr([61],'队伍按钮整理开面板、取出提示','S:903-904;S:917-929;S:1592-1595')
rr([62],'关闭位置返回退出编码','S:905-906;S:1515-1524')
rr([63,67],'盒名左右瞬态及JUMP切盒持久写当前盒，捕获当前盒优先','S:855-864;S:869-882;D:231-249','默认40盒；切盒动画/目标背景初始化先于当前盒字段提交，异常不保证目标字段提交。')
rr([65],'单方向盒导航大致覆盖，但队伍Close上下例外遗漏；储存两阶段输入顺序未覆盖','S:733-790;S:811-834;S:837-910;S:938-985','默认队伍上限6；输入服务快照，实体组合可达unknown。','PENDING_FINDINGS_UI_ST_001_UI_ST_005')
rr([71],'拿起删源、暂持守卫退出，交换更新暂持而放/释/存清暂持','S:1507-1524;S:1531-1576;S:1770-1781;S:1784-1842;S:1845-1878','正常模式0、合法成员与目标；动作并非事务。')
rr([75],'整理队伍面板返回队伍位置，取消收回恢复队伍按钮','S:912-936;S:938-985')
rr([83,84],'整理操作菜单顺序/持有分支/Debug和快捷交换分流','S:1530-1579','默认命令焦点首项另缺，提出UI-ST-004。')
rr([85],'取出菜单固定顺序，队伍按钮仅提示','S:1592-1619')
rr([86],'存入菜单固定顺序，仅队伍成员','S:1626-1650')
rr([87],'选择菜单固定顺序，返回位置，不含释放','S:1984-2014')
rr([89],'未持空格无菜单，操作菜单取消没有本操作写入','S:1530-1531;S:1560-1579;S:1606-1619;S:1637-1650;S:1984-2014','不包括先前写入、浏览背景写入或异常返回。')
rr([93],'守卫引用WP25但源逐操作检查不同','S:1689-1699;S:1705-1879')
rr([97],'取出满队拒，先演出后队末移动，持有入队清持有','S:1705-1721;S:1169-1175;D:189-215')
rr([98],'存入守卫、选择取消/满盒重试、治疗保进化准备再移动','S:1724-1767;D:178-209;D:217-228;P:300-306','最后可用仅未持且目标可用；取消路径没有治疗/移动；正常返回不承诺异常事务恢复。')
rr([99],'拿起最后可用拒，演出后持有并删源','S:1770-1781;D:254-259')
rr([100],'放置非空报错、仅盒容量/邮件/不能存、治疗写格清持有及队伍压缩','S:1784-1810;D:136-139;D:170-175','正常非负盒/队伍空格；特殊负选择后续仍保留。')
rr([101],'交换空报错，目标盒及队伍最后可用守卫、治疗后换位','S:1813-1842')
rr([102],'释放前置拒绝、未持队伍最后可用拒无确认；No首项，Yes删并两消息','S:1845-1879;S:679-714','合法成员；BACK返回负值因此分支结果等价No，取消编码不是索引0。')
rr([103],'道具蛋/邮件拒；取物先加袋，成功消息后清持物；给物先成员后袋','S:1902-1933;S:1237-1245;BAG:591-600;ITEM:189-194','正常背包添加/删除，后置消息正常返回；中途异常无事务保证；通用确认默认Yes遗漏在UI-ST-004。')
rr([104],'标记副本编辑，OK提交、BACK/Cancel丢弃','S:1314-1392')
rr([105],'盒菜单Jump/Wallpaper/Name取消和写入分支','S:1936-1962;S:1217-1235;S:1054-1062;S:991-1018;D:108-118','默认选择盒焦点当前盒，墙纸为当前匹配/首项，名称返回文本合法。')
rr([107],'队伍物品移动SPECIAL嵌套取回先提交袋/成员，后原移动保旧身份，可取消保取回','PARTY:1434-1484;PARTY:774-781;S:1902-1923;S:1508-1524','A/B索引不变、不存成员、袋可加、非蛋非Shadow无邮件；Box Link三门/媒体/前序依赖按正式共同前提。')
rr([111],'摘要完整容器/持有单项、返回索引；摘要写信快照仍来自玩家队伍k+2/k+1，盒直接Item不写信','S:1247-1263;SUM:1200-1228;IU:781-822;MAIL:100-125;S:1705-1721;S:1902-1933','摘要与邮件本体归WP66-A/WP64；实际Mail→Read下游全文非本域，此审确认传入位置及写信快照与取出链。')
rr([117,119],'暂持退出被拦且保集合','S:1508-1519')
rr([118,120],'BACK无持确认继续、关闭无持确认退出；默认Yes未明示','S:1508-1524;S:1588-1601;S:1627-1635;S:1681-1687;S:679-714;S:1971-1980','正常无暂持；BACK负取消在关闭确认也为否、应留循环。','PENDING_FINDING_UI_ST_004')
rr([122],'正常退出清储存标志，已完成操作不回滚','S:1500-1659;S:2018-2020')
rr([128,130,131,132],'暂停图鉴显示门与当前区域/单区域/多区域三分流','PAUSE:133-163;L:317-335;PD:315-332')
rr([136],'区域菜单名字/见拥有计数及完成阈值，选择写观看区域后主列表回菜单','M:17-32;M:99-128;PD:351-358;U:401-418','可访问区域缓存和名字表有效；空/缺区域成员查询nil导致计数失败，UI不补保护。')
rr([140],'三观看字段及默认值；场景恢复索引，非结果态移动提交','GLOBAL:25-27;GLOBAL:75-82;L:264-298;L:330-335;L:1255-1285','随存档保存引用WP62/WP09，本域未复审整个保存序列；局部读写已核对。')
rr([146],'区域行来源与回退、模式资格、末次形态行字段','L:338-375;U:401-405;PD:129-132')
rr([148],'常规列表数值首/尾修剪与三类排序平局编号规则','L:378-403;L:35-56','常规列表排序；搜索独立排序840-846未显式平局编号，不将常规规则自动推广。')
rr([150],'见/拥有/未见行标记，偏移编号及USE已见门，盒图标首方格与物种动画分层','L:35-56;L:1278-1282;S:24-28','物种动画本体WP66-C；此审仅盒格首方格和图鉴行标记，实际素材未知。')
rr([152],'主列表预览普通外观，保存异色值不改','L:766-769;PD:129-132')
rr([156],'场景四状态分层、主搜索克隆会话、参数子页克隆/OK接纳/取消丢弃','L:293-295;L:917-928;L:1048-1089;L:1092-1094;L:1181-1240')
rr([158,162,163],'37档离散身高/体重候选，显示单位不改变筛选原值','L:1110-1117;L:804-822;L:518-538')
rr([165],'大小参数初焦点上界，未选-1/37表长不同','L:917-926;L:939-1000')
for line,source in [(169,'L:940-943'),(170,'L:944-947'),(171,'L:952-956'),(172,'L:957-960'),(173,'L:965-968'),(174,'L:969-970'),(175,'L:971-972'),(176,'L:973-974'),(177,'L:982-985'),(178,'L:986-987'),(179,'L:988-989'),(180,'L:990-992'),(181,'L:1048-1050'),(182,'L:1051-1063')]:
    rr([line],'大小子页该输入分支与焦点/端点变化','L:917-928;'+source,'该行指定焦点/端点条件；37档、两阶段输入，不将方向改值等同外层提交。')
rr([184],'大小方向直接改本地端点，ACTION仅焦点OK；主ACTION仅Start，需后续USE','L:965-1000;L:1048-1081;L:1173-1240')
rr([186],'类型双槽空位先填、满后轮转、禁止另一槽重复；空白按后槽/前槽清并翻槽','L:927-928;L:1064-1081','默认18类初轮转0；实际候选数量决定轮转初值。')
rr([188],'Start先持久模式后过滤；零命中保结果/会话/草稿并留搜索，取消不还模式；命中接纳并索引0','L:771-848;L:1224-1251','名字字符按当前本地化候选文本逐字符比较大小写；媒体/实体输入未知。')
rr([190],'Reset只改草稿；搜索Cancel/BACK丢本次编辑不回滚Start模式','L:1176-1178;L:1219-1240')
rr([194],'排序/名字/类型/颜色/形状候选与默认列数、定义次序','L:897-899;L:1095-1121;SHAPE:34-116;COLOR:30-78','默认类型18的PBS目录未本域全文核验；候选规则非伪类型与正文一致，默认数量继承输入。')
rr([196],'非排序有空白；焦点≠选值≠外层草稿；USE选值OK提交，BACK弃','L:917-928;L:1001-1089;L:1182-1218')
rr([198],'普通参数导航用候选数量及列数定义末行','L:897-899;L:1001-1046')
for line,source in [(202,'L:1011-1013'),(203,'L:1002-1010'),(204,'L:1015-1020'),(205,'L:1021-1022'),(206,'L:1023-1024'),(207,'L:1015-1017'),(208,'L:1028-1035'),(209,'L:1037-1044')]:
    rr([line],'普通参数页该单方向焦点转移','L:897-899;'+source,'当前候选数N及列数c有效；末候选/特殊按钮按指定例外，不写选值。')
rr([211],'默认名字/排序/颜色/类型/形状焦点向量与本地值提交对照','L:1001-1081;L:1095-1121','各轮独立单键；默认候选序列、名字单字母；仅静态推导，未运行独立模型。')
rr([215],'参数子页方向优先UP/DOWN/LEFT/RIGHT，再ACTION/BACK/USE；大小横向repeat其余trigger','L:939-1082')
rr([217],'搜索主画面方向/ACTION/BACK/USE一条互斥链，Start UP只移体重','L:1139-1241','输入服务条件快照，不证明物理组合键可达。')
rr([221],'结果态BACK复位模式参数且按物种找回写索引；条目返回结果重跑并夹索引','L:851-894')
rr([223],'体型/体色按固定注册次序和图标位置，Area按遭遇点掩码','L:1118-1121;SHAPE:34-116;COLOR:30-78;E:313-351','Habitat完整目录属于WP03，不由Area使用；本审未检查真实图集。')
rr([229],'完整条目页夹限、物种跳未见、ACTION按页叫声及退出返回索引','E:424-444;E:485-555')
rr([231],'信息拥有门、Area无USE且掩码集合、Forms多项门；信息与两个搜索US转换差异','E:221-300;E:302-400;E:498-512;L:518-538;L:631-664;ENC:53-60','地图资格/有限ASCII域/局部US语言字符串条件；WP63消费者差异引用其主域，未复审该地图整链。')
rr([233],'普通刷新读取末次、固定普通外观，只有进入多项选择器才另写记录','E:139-152;E:446-483;E:507-511;PD:61-69;PD:129-140','资源回退本体WP15；普通/异色媒体实际未知。')
rr([237],'可列形态结构/已见/性别/标签/排序全部分层','E:154-199;PD:61-69','素材解析结果相等包括nil相等，不证明存在；本地化命名结果以当前数据有效为前提。')
rr([239],'形态首轮/移动写记录和BACK不回滚成立，但首末回绕未指定','E:446-483;PD:138-140;L:348-373;L:766-769','可列项>1，合法当前项或不匹配；普通刷新不清异色。','PENDING_FINDING_UI_ST_003')
rr([243],'摘要先最近见到再完整单种条目','SUM:1218-1225;E:590-611','摘要DexNo首区即停与完整单种编号属于不同计算；本审未重审摘要DexNo字段。')
rr([244],'捕获获得简略Info入口与编号逐区域查，USE/BACK关','E:71-117;E:557-571;E:614-618','捕获/获得调用方门与前序写入引用WP62，未本域穷尽各调用方。')
rr([246],'摘要/简略普通图像请求与选择器首轮另写false分离，单项不进选择','E:139-152;E:446-483;E:507-511;SUM:1218-1225;PD:138-140','BULBASAUR/RATTATA数据有效性沿正式夹具，本域未逐条核对PBS/媒体。')
rr([250,251,252,253,254,255,256],'全域不变量复核：逐入口守卫、暂持删源/禁退、已完成写入保留、搜索/索引/形态/背景读写边界','S:1500-1659;S:1705-1879;S:1964-2020;S:378-397;D:101-106;L:771-894;L:1255-1285;E:446-483','每个编号不变量单独由下方atomic_subclaims定位；scope及异常限定保留。')
rr([260],'空位置无菜单，空队伍选择仍可到末按钮','S:811-834;S:1530-1531;S:1606-1607;S:1637-1638')
rr([261],'盒满在存入循环重选，不自动改盒','S:1740-1765;S:1217-1226','捕获全满策略引用WP25/WP38，非存入选择UI保证。')
rr([262],'PC整队满队前置与整理逐次满队拒','PC:189-198;S:1705-1712')
rr([263],'蛋/濒死可存取，最后可用守卫按目标可用性','S:1689-1699;S:1705-1767','释放蛋仍拒，存入PC整队前置仍独立。')
rr([264],'跨盒/队伍暂持保留成立；无条件预览不更新过宽，交换有显式重启并换预览对象','S:1064-1070;S:1131-1149;S:1418-1479;S:1813-1842','正常合法X/Y成功交换；只推导请求身份和效果重启，真实像素未知。','PENDING_FINDING_UI_ST_002')
rr([265,267,268,269,270,271,272,274],'大小未选/具体/表长映射及可达极端区间','L:804-822;L:917-1000','具体37档；表长哨兵不是无界，正高度/重量资格与拥有门成立。')
rr([275],'缺/空区域主列表回全国；条目负区域落当前/0；未拥有文本占位','L:348-355;E:20-24;E:247-295;U:401-405','无地图对象本身非保证；地图存在但无位置元数据时0。')
rr([276],'观看字段持久、搜索参数仅场景内、重新打开按保存值','GLOBAL:25-27;GLOBAL:75-82;L:264-298;L:1092-1094','全局存档序列引用WP62/WP09，本审确认字段及局部读取，不重审保存整个系统。')
rr([281],'39条BX目录及补充覆盖索引存在且对应局部源','S:1500-2020;L:264-1285;E:154-571','目录是静态设计；具体测试条款下方独立逐行映射，不是运行通过。','TEST_CATALOG_INDEX_REVIEWED')
rr([285],'容量/伪位置/治疗/守卫依赖域登记，不推广地区代理','D:9-17;D:65-76;D:136-175;D:178-259;S:1705-1879;SET:220-225','地区代理缺陷保持WP25既有范围，本域主UI绑定基础全局容器；不验证地区化UI。')
rr([286],'图鉴字段/可访问/nil/形态/遭遇版本/编号依赖登记','PD:61-69;PD:129-140;PD:315-358;ENC:53-60;E:71-117;E:154-199','形态计数既有缺陷引用WP62，不据UI扩大修复。')
rr([287],'消息命令/输入/文字接口依赖，盒名0..12，不用数字控件','S:658-714;S:1228-1235;S:1960-1960','通用WP17不决定储存自有确认的具体命令顺序；UI-ST-004/005仍需补。')
rr([288],'配置依赖声明符合本域源；真实媒体缺失结果保留','SET:220-225;SET:303-315;S:1748-1755;L:317-324;E:166-177','当前世代8默认值继承配置主域；媒体/宿主/插件未执行。')
rr([289],'前向领域及Demo不纳入本审行为证明','PARTY:774-781;SUM:1218-1225;BAG:591-600;PURIFY:1273-1281','前向归属声明，仅本域必要consumer接口检查。','SCOPE_BOUNDARY_REVIEWED')
rr([293,294,295,296,297,298,300],'未决与历史接受状态保留，不用旧结论替代新字节语义审读','S:1654-1658;S:1964-2020;PURIFY:1273-1281','历史审查/报告与所有保留编号未独立重审；当前局部负位置事实重新核对，媒体/宿主/Demo unknown。','SCOPE_HISTORY_NOT_RUNTIME_PROOF')

# Independent atomic locations for long paragraphs/invariant blocks.
atomic={
65:[{'claim':'队伍末按钮UP到5/DOWN到0缺少例外','sources':refs('S:819-829'),'status':'PENDING_UI-ST-001'},
    {'claim':'普通盒左右在同一行首尾回绕','sources':refs('S:765-788'),'status':'SUPPORTED_STATIC'},
    {'claim':'方向阶段和按钮阶段为两次独立决策','sources':refs('S:845-908'),'status':'PENDING_UI-ST-005'}],
107:[{'claim':'移动物品身份发起时缓存','sources':refs('PARTY:1437-1446'),'status':'SUPPORTED_STATIC'},
     {'claim':'SPECIAL正常桥开整理并重建队伍图形','sources':refs('PARTY:774-781'),'status':'SUPPORTED_STATIC'},
     {'claim':'取回先袋写入、提示后清成员','sources':refs('S:1913-1919'),'status':'SUPPORTED_STATIC'},
     {'claim':'之后确认目标仍交发起时物品，BACK不提交旧物品','sources':refs('PARTY:1445-1460'),'status':'SUPPORTED_STATIC'}],
111:[{'claim':'暂持单项/0、队伍/盒完整容器及返回游标','sources':refs('S:1247-1263'),'status':'SUPPORTED_STATIC'},
     {'claim':'摘要传当前容器位置给通用给予/写信','sources':refs('SUM:1208-1215;IU:816-819;MAIL:100-120'),'status':'SUPPORTED_STATIC'},
     {'claim':'快照前两项仍玩家队伍k+2/k+1','sources':refs('MAIL:107-120'),'status':'SUPPORTED_STATIC'},
     {'claim':'盒直接Item没有写信调用','sources':refs('S:1902-1933'),'status':'SUPPORTED_STATIC'}],
231:[{'claim':'Info拥有门与战斗计数切换','sources':refs('E:240-295;E:500-503'),'status':'SUPPORTED_STATIC'},
     {'claim':'Area资格、可见并集及宽/形状已有格','sources':refs('E:313-351'),'status':'SUPPORTED_STATIC'},
     {'claim':'v>0枚举同图v0泄漏','sources':refs('ENC:53-60;E:325-347'),'status':'SUPPORTED_STATIC'},
     {'claim':'Area无输入动作，Forms多项才开','sources':refs('E:504-511'),'status':'SUPPORTED_STATIC'},
     {'claim':'Info US体重0.45359；两搜索US体重0.254，哨兵先映射','sources':refs('E:251-262;L:518-538;L:631-664'),'status':'SUPPORTED_STATIC'},
     {'claim':'WP63三消费者差异仅引用接口契约，未本域重新全文审读','sources':refs('E:313-351'),'status':'CROSS_DOMAIN_REFERRED_UNKNOWN'}],
250:[{'claim':'入口和选择负地址','sources':refs('PC:183-212;S:1964-2020;D:159-167'),'status':'SUPPORTED_STATIC'}],
251:[{'claim':'当前盒即写，持有禁退，拿起删源','sources':refs('S:855-882;S:1508-1519;S:1778-1781'),'status':'SUPPORTED_STATIC'}],
252:[{'claim':'操作取消无此次提交而先前完成值保留','sources':refs('S:1740-1767;S:1865-1879;S:1314-1392'),'status':'SUPPORTED_STATIC'}],
253:[{'claim':'图鉴领域归WP62，本域只写触发/会话/索引','sources':refs('L:293-295;L:771-894;E:446-483'),'status':'SCOPE_BOUNDARY_REVIEWED'}],
254:[{'claim':'非搜索移动索引写入','sources':refs('L:1260-1264'),'status':'SUPPORTED_STATIC'},
     {'claim':'Start先模式写，零命中不回滚，命中才会话接受','sources':refs('L:771-773;L:1224-1239'),'status':'SUPPORTED_STATIC'},
     {'claim':'Forms首次及移动写','sources':refs('E:446-479;PD:138-140'),'status':'SUPPORTED_STATIC'},
     {'claim':'首次/缓存不等读背景；空不写、完整行兼容转整数、不合法文本数值比较前失败','sources':refs('S:378-397;D:101-106;S:424-435'),'status':'SUPPORTED_STATIC'},
     {'claim':'负整数-1可用并请求对应素材，素材结果unknown','sources':refs('D:101-106;S:390-396'),'status':'SUPPORTED_STATIC_MEDIA_UNKNOWN'}],
255:[{'claim':'空搜索有消息，不改结果；未见行不开，条目跳未见','sources':refs('L:1224-1235;L:1278-1282;E:424-444'),'status':'SUPPORTED_STATIC'}],
256:[{'claim':'放非空/交换空抛错，正常菜单和quick分支按目标有无分流','sources':refs('S:1531-1548;S:1561-1565;S:1787-1789;S:1816-1818'),'status':'SUPPORTED_STATIC'}]}

blocks=json.loads((ROOT/'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/inventory/formal-block-denominator.json').read_text())
spec_lines=get(SPEC).splitlines()
reverse=[]
for b in blocks:
    if b['path']!=SPEC: continue
    line=b['start_line']; content=spec_lines[line-1]
    isstruct=content.startswith('#') or (content.startswith('|') and (set(content.replace('|','').replace(' ','').replace(':',''))=={'-'} or line in [19,32,57,81,95,115,160,167,200]))
    if line in reverse_rules:
        summary,source,premise,status=reverse_rules[line]
        evidence=refs(source)
    elif isstruct:
        summary='标题或表头/分隔符；结构已审，非独立行为命题'; premise='不计为源行为PASS'; status='STRUCTURAL_ONLY'; evidence=[]
    elif line in [1,3,5,9,11]:
        summary='分类/目的/范围与静态证据声明'; premise='按本次读集可核对局部边界；历史批准状态与运行状态不得由文件读取产生'; status='SCOPE_BOUNDARY_REVIEWED'; evidence=[]
    else:
        raise AssertionError(('unmapped formal block',b,content))
    reverse.append({'id':b['id'],'formal_clause':{k:v for k,v in b.items() if k!='status'},'claim_summary':summary,'inventory_status':'INVENTORIED','structural_status':'INSPECTED','semantic_status':'CLAUSE_SEMANTICALLY_READ','source_evidence':evidence,'source_preconditions':premise,'disposition':status,'atomic_subclaims':atomic.get(line,[]),'actual_reference_execution':'NOT_EXECUTED','independent_model_execution':'NOT_EXECUTED','host_demo_media_observation':'UNKNOWN'})

dump_jsonl('reverse-matrix.jsonl',reverse)
print(json.dumps({'reverse_formal_blocks':len(reverse),'no_unmapped_formal_blocks':True}))

# Formal test rows in the storage/Pokedex scope, plus the exact cross-domain rows
# explicitly consumed by this formal module. Domain-only PD cases stay outside this subtask.
test_rules={
248:('PC满队入口拦','PC:189-198'),249:('PC存入可用数前置','PC:199-212'),
250:('持有阻止BACK与关闭','S:1508-1519'),251:('BACK确认Yes继续/No退出保完成值','S:1508-1514'),
252:('盒名LEFT瞬态写当前盒','S:765-768;S:855-864'),253:('JUMPDOWN回绕并写','S:876-882;SET:220-222'),
254:('快捷交换直接拿起/放/换仍逐守卫','S:891-893;S:1531-1536;S:1770-1842'),
255:('整理内取出满队无移动','S:1705-1712'),256:('存入BACK无写/盒满重试','S:1740-1767'),
257:('最后可用拿起拒','S:1770-1777'),258:('非空放下异常非正常菜单路径','S:1784-1789;S:1531-1548'),
259:('释放蛋/邮件/禁止释无确认','S:1845-1859'),260:('未持队伍最后可用释放拒；持有不套','S:1860-1864'),
261:('释放默认No，Yes删除消息','S:1865-1877;S:679-714'),262:('取物背包失败保物','S:1913-1923'),
263:('给物取消无提交，选中先持物后袋删','S:1924-1932;BAG:591-600'),264:('标记BACK丢副本/OK提交','S:1335-1338;S:1372-1385'),
265:('盒名空不覆/12字','S:1228-1235;S:1960-1960'),266:('换背景后退出保写入','S:991-1018;S:1957-1958'),
267:('图鉴暂停可见门','PAUSE:133-163'),268:('两区域菜单写区域回菜单','PAUSE:154-160;M:99-128'),
269:('数值首偏移未见/尾未见裁去/中间保留USE无效','L:378-403;L:35-56;L:1278-1282'),
270:('常规字母/体重资格及平局编号','L:338-345;L:394-403'),271:('类型双槽禁重复和清槽','L:1064-1075'),
272:('搜索空先写持久模式保搜索草稿','L:771-773;L:1224-1235'),273:('结果BACK复位并物种恢复索引','L:851-865'),
274:('结果态导航不写索引','L:1260-1264'),275:('条目页边界夹限无音','E:533-550'),276:('条目物种跳未见末端停','E:435-444;E:523-532'),
277:('形态移动写、BACK保写、预览用末次','E:446-483;L:766-769'),278:('全形态设置不解除结构门','E:154-181'),
279:('Area版本枚举缺陷和空态','ENC:53-60;E:313-400'),280:('摘要先登记最近见到再完整页','SUM:1218-1225;E:590-611'),
281:('结果条目返回重跑、索引夹','L:868-894'),282:('失败搜索四状态和重开初始化','L:293-295;L:771-773;L:1092-1094;L:1224-1251'),
283:('选择队伍按钮负盒末格','S:903-904;S:912-914;S:1984-2001;D:159-167'),
284:('上界表长对应0','L:971-972;L:804-812'),285:('Forms首轮写与不匹配首项','E:446-479;E:507-511;PD:138-140'),286:('ACTION按Info/Area/Forms不同叫声','E:492-494'),
591:('交换持有链与退出拦','S:1770-1842;S:1508-1519'),596:('失败搜索模式保4、结果BACK复0','L:771-773;L:1224-1240;L:851-865'),
597:('区域计数显示和完成标记','M:17-32;M:99-115'),605:('盒格仅首方格；其它动画本体前向','S:24-28'),
606:('背景首次/改变读写及缓存相同门','S:378-397;S:424-435;D:101-106'),607:('US信息/搜索不同体重转换和哨兵','E:251-262;L:518-538;L:631-664'),
608:('可列基形同图折雄与结构多形态标签','E:154-199'),609:('37档及大小焦点/端点/提交','L:917-1000;L:1048-1081;L:1110-1117;L:1173-1240'),
667:('嵌套取回后旧物转交B','PARTY:1434-1484;PARTY:774-781;S:1913-1919'),
668:('嵌套取回后BACK保袋1/A空/B空','PARTY:1434-1484;S:1913-1919'),669:('无嵌套普通移物','PARTY:1434-1484'),
781:('普通主列表预览保异色记录','L:766-769;PD:129-132'),782:('完整Info/Forms刷新普通请求但不清记录','E:139-152'),
783:('简略普通请求；摘要先最近见到','E:139-152;SUM:1218-1225;E:590-611'),784:('仅异色可列但普通请求、真实资源unknown','PD:61-69;E:154-181;E:139-152'),
785:('多项首轮写false、不回滚；单项不开选择','E:446-483;E:507-511;PD:138-140'),
858:('名字普通焦点方向六轮不写选值','L:1001-1046;L:1064-1081'),859:('名字方向/选值/提交与BACK丢本地','L:1001-1089'),
860:('排序DOWN三次至OK/CancelUP末项','L:1002-1025;L:1037-1044'),861:('普通候选不整末行转移','L:1002-1025;L:897-899;L:1095-1121'),
862:('普通左右边界与特殊焦点','L:1002-1046'),873:('子页UP+USE本地选U，主UP+USE只移焦点','L:1002-1081;L:1139-1241'),
877:('主/子页ACTION+USE与大小方向+BACK阶段','L:939-1082;L:1139-1241')}

def test_records(path,rules):
    lines=get(path).splitlines(); out=[]
    denom={b['start_line']:b for b in blocks if b['path']==path}
    for line,(summary,source) in sorted(rules.items()):
        assert lines[line-1].startswith('|'), (line,lines[line-1])
        tid=lines[line-1].split('|')[1].strip()
        out.append({'id':denom[line]['id'] if line in denom else 'LOCAL-TEST-'+tid,
            'test_id':tid,'formal_clause':{'path':path,'start_line':line,'end_line':line,'commit':MAIN},
            'claim_summary':summary,'inventory_status':'INVENTORIED','structural_status':'INSPECTED','semantic_status':'CLAUSE_SEMANTICALLY_READ',
            'source_evidence':refs(source),'source_preconditions':'原正式表该行及共同前提全部继承；合法依赖/无插件；只核对本域所列状态、请求及取消/失败链。',
            'disposition':'STATIC_VECTOR_SUPPORTED_NOT_EXECUTED' if line!=605 else 'PARTIAL_COMPONENT_SUPPORTED_OTHER_UI_REFERRED',
            'actual_reference_execution':'NOT_EXECUTED','independent_model_execution':'NOT_EXECUTED','host_demo_media_observation':'UNKNOWN'})
    return out
reverse+=test_records(TEST,test_rules)
PDTEST='deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md'
pd_rules={
124:('仅全国观看默认-1及缓存','GLOBAL:75-82;PD:323-332'),125:('当前地区列表门/全国回退','PD:315-332;L:317-324'),
126:('空缺表查询失败但主列表回退','U:401-418;PD:351-358;L:348-355'),128:('普通模式及过滤门','L:338-375;L:771-848'),
129:('拥有门及战斗计数展示','E:221-300;E:500-503'),130:('形态结构/已见门','E:154-199;PD:61-69'),
131:('Area版本并列缺陷、资格、空态','ENC:53-60;E:313-400'),134:('浏览写末次形态保留','E:446-483;PD:138-140'),
140:('摘要字段首区与简略继续是领域引用，只复核简略','E:71-117'),143:('零命中四状态与同场景旧会话','L:293-295;L:771-773;L:1092-1094;L:1224-1251'),
144:('无Start无模式写/结果BACK复0','L:1176-1240;L:851-865'),145:('区域菜单两计数与完成标记','M:17-32;M:99-128'),
146:('具名非0首合格性别停止','E:154-199'),147:('基形nil/空串同图异图性别标签分界','E:154-199'),148:('基形结构多形态早于已见且nil/空串标签差异','E:154-199'),149:('首轮写首项vs单项不开','E:446-483;E:507-511'),
203:('10000仅基格、缺尾不补；WP63引用','E:313-351'),204:('11111五格','E:313-351'),205:('缺省/零宽1格与资格/可见门','E:313-351;E:390-395'),206:('可见点并集同格仍亮；WP63首条引用','E:317-351'),
216:('主列表普通预览保三元组','L:766-769;PD:129-132'),217:('完整/简略普通请求与摘要前置写分层','E:139-152;SUM:1218-1225'),218:('任一异色已见资格普通请求','PD:61-69;E:154-199;E:139-152'),219:('普通请求不依据true切异色，媒体unknown','L:766-769;E:139-152'),220:('多项首轮false写和单项对照','E:446-483;E:507-511;PD:138-140'),
232:('有限ASCII2为占位','E:337-347'),233:('ASCII1占位','E:337-347'),234:('ASCII0不占位','E:337-347'),235:('ASCIIx不占位','E:337-347'),236:('ASCII9占位','E:337-347'),237:('资格/可见门阻止已有字符点亮','E:317-347'),238:('已有多字符/缺尾/默认/并集回归','E:313-351')}
reverse+=test_records(PDTEST,pd_rules)
for row in reverse:
    if row.get('test_id')=='PD25': row['disposition']='PARTIAL_COMPONENT_SUPPORTED_SUMMARY_FIELD_REFERRED'
    if row.get('test_id') in ['U05-HAB01','U05-HAB04','U06-M11-001-G']:
        row['disposition']='AREA_COMPONENT_SUPPORTED_WP63_COMPONENT_REFERRED'
dump_jsonl('reverse-matrix.jsonl',reverse)
print(json.dumps({'reverse_total':len(reverse),'test_rows':len(test_rules)+len(pd_rules)}))

# Explicitly considered and rejected as a standalone finding: storage confirmation
# defaults are consistent with the ordinary Yes/No dependency, unlike release No/Yes.
for f in forward:
    if f['id'] in ['UI-ST-S-0679','UI-ST-S-1681','UI-ST-S-1685']:
        f['disposition']='SUPPORTED_STATIC_WITH_GENERIC_CONFIRMATION_DEPENDENCY'
        f['dependency_note']='已检查本地Yes/No与默认索引0；WP17普通确认支持该语义。默认文字是否加清晰度为编辑建议，未提出独立缺陷。'
for r in reverse:
    if r['formal_clause']['path']==SPEC and r['formal_clause']['start_line'] in [118,120]:
        r['disposition']='SUPPORTED_STATIC_WITH_GENERIC_CONFIRMATION_DEPENDENCY'
        r['claim_summary']='退出/继续确认分流正确；本地Yes首项、初焦点0，通用普通确认依赖为间接支持。'
        r['source_preconditions']='正常无暂持；本地命令确认BACK为负值且包装返回false；初USE选择Yes。已检查WP17 111–117，未将可选清晰化提出为缺陷。'
    elif r['formal_clause']['path']==SPEC and r['formal_clause']['start_line'] in [83,103,287]:
        r['source_preconditions']=r['source_preconditions'].replace('默认命令焦点首项另缺，提出UI-ST-004。','本地菜单初焦点0；表项顺序与通用确认依赖一致，未提出默认项缺陷。').replace('通用确认默认Yes遗漏在UI-ST-004。','通用确认Yes首项、初焦点0；该依赖一致。').replace('UI-ST-004/005仍需补。','储存自有导航阶段顺序UI-ST-005另列，通用确认默认项未提出独立缺陷。')

# Context/constant units are separated from callable inventory.
context_facts=[
('M',1,7,'区域菜单文件/绘制窗口结构上下文','STRUCTURAL_ONLY',[136]),
('L',1,4,'主列表绘制窗口结构上下文','STRUCTURAL_ONLY',[146]),
('L',253,258,'六模式身份依数值、字母、最高、最矮、最重、最轻排序','SUPPORTED_STATIC',[194]),
('E',1,4,'条目场景结构上下文','STRUCTURAL_ONLY',[229]),
('S',1,4,'盒格图标结构上下文','STRUCTURAL_ONLY',[47]),
('S',150,150,'抓/放呈现名义周期0.4秒，仅图形时序未执行','PRESENTATION_RESERVED',[47]),
('S',586,587,'标记素材每位参考单元16×16；未来布局不受限','PRESENTATION_RESERVED',[104])]
for k,a,b,fact,disp,anchor in context_facts:
    forward.append({'id':f'UI-ST-{k}-CONTEXT-{a:04d}', 'source_unit':{'path':FILES[k],'start_line':a,'end_line':b,'commit':REF,'unit_boundary':'context/constant declaration'},'inventory_status':'INVENTORIED','structural_status':'INSPECTED','semantic_status':'CONTEXT_REVIEWED_SEPARATELY_FROM_CALLABLES','fact':fact,'necessary_consumers':[],'formal_links':[{'path':SPEC,'line':v} for v in anchor],'disposition':disp,'actual_reference_execution':'NOT_EXECUTED','independent_model_execution':'NOT_EXECUTED','host_demo_media_observation':'UNKNOWN'})

PENDING='PENDING_NON_PROPOSER_COUNTERREVIEW_AND_ROOT_ADJUDICATION'
def finding(id,title,kind,severity,formal,source,pre,control,counter,cancel,negative,consumers,impact,revision,sync,accept,regress,counterreview):
    return {'id':id,'title':title,'kind':kind,'severity':severity,'status':PENDING,
        'reference_commit':REF,'formal_commit':MAIN,'formal_locations':[{'path':SPEC,'line':x[0],'clause':x[1]} for x in formal],
        'source_locations':refs(source),'source_preconditions':pre,'ordinary_control':control,
        'minimal_counterexample':counter,'cancel_exception_partial_commit':cancel,
        'negative_evidence_scope':negative,'necessary_consumers':refs(consumers),
        'impact':impact,'minimum_revision':revision,'scope_preservation':'只补本域静态行为；不改参考、不设计新实现、不修参考缺陷；不扩张宿主/媒体/插件/真实存档/Demo已证边界。',
        'synchronized_files':sync,'acceptance_criteria':accept,'regression_dependencies':regress,
        'non_proposer_counterreview_required':counterreview,
        'evidence_level':{'static_reasoning':'SOURCE_AND_NECESSARY_CONSUMER_READ','actual_reference_execution':'NOT_EXECUTED','independent_model_execution':'NOT_EXECUTED','host_demo_media_observation':'UNKNOWN'},
        'author_counterreview':'NOT_PERFORMED_AS_NON_PROPOSER','root_adjudication':'PENDING'}

sync_basic=[SPEC,TEST,'audit/source-traceability.md (root决定是否同步，本子任务不改)','全局Feature Matrix对应UI行（root同步，不把读取改成执行PASS）']
findings=[
finding('UI-ST-001','队伍面板关闭按钮上下导航缺少专门转移', 'INCOMPLETE_OR_MISLEADING_STATE_TRANSITION','MEDIUM',[(65,'§3.1，队伍面板方向转移')],
'S:811-834;S:938-985',
['默认MAX_PARTY_SIZE=6，合法队伍面板已打开，焦点可为末项6；单个UP或DOWN repeat成立，其余输入假。','整理/存入均消费同一方向转移；整理末按钮USE只收面板，存入末按钮USE发关闭确认。'],
{'initial_focus':2,'input':'UP','expected_focus':0,'domain_write':'none'},
[{'initial_focus':6,'input':'UP','source_expected_focus':5,'generic_plus_minus_2_reading':4}, {'initial_focus':6,'input':'DOWN','source_expected_focus':0,'generic_plus_minus_2_clamp_reading':6}],
'该单方向只改焦点、不提交集合；后续BACK仍收面板/进入继续确认，已完成集合写入不回滚；本反例不需异常或部分提交。',
{'read_formal':[SPEC+':1-300',TEST+':244-286,584-610,661-685,775-787,858-880'], 'absence':'本域导航段只给上下±2及越界到6，未给末按钮UP→5/DOWN→0；BX目录未有该末按钮方向向量。','limit':'未宣称其它所有正式文件没有这条信息；WP17仅输入服务/通用窗口，不能决定自有队伍几何。'},
'S:938-985;S:912-936;S:1626-1650;SET:220-222',
'按正文概括实现队伍导航会在Close按钮向上选择4而非5，向下留6而非回0，导致正常单键流程不同。',
'在§3.1明示成员位置与末按钮两种转移：默认6上到5、下到0，左右按既有连续序列回绕；配置上限用最后成员/首成员表达。同时补两个独立单键测试，保留普通成员±2规则。',sync_basic,
['正文明确末按钮两个方向结果且不把它们等同成员±2。','两反例在默认6成员上限均有唯一静态预期；整理/存入返回按钮USE差别保持。'],
['BX B03/B04/B07','§3.3整理队伍BACK收起与游标−2','模式2末项返回−3','动态配置队伍上限的既有范围，不据此保证任意非默认布局可用'],
'非提出者需尝试以§3.1现有文字、WP17或其它已批准本域条款反证已覆盖末按钮两个转移；若已覆盖应合并/撤销候选，不能把本作者说明作反证。'),
finding('UI-ST-002','暂持时预览不更新的无条件表述覆盖了成功交换', 'OVERGENERALIZED_OBSERVABLE_BEHAVIOR','MEDIUM',[(264,'§9，暂持跨页/预览')],
'S:1064-1070;S:1131-1149;S:1418-1479;S:1813-1842;S:837-841',
['普通整理模式，盒P=X/Q=Y，X与Y具有不同预览身份且合法可移动，无邮件/禁止存；拿起X，Q有Y。','交换成功、呈现调用与刷新正常返回；资源仅作为条件依赖，不声称真实像素通过。'],
{'flow':'持X后仅移动游标/切盒，不交换','expected':'屏幕继续以X为预览对象；导航用的自动像素化设置被暂持守卫跳过。'},
{'flow':'P拿X → Q成功Shift/快捷交换 → 下一次选择器刷新','source_expected':'P空/Q=X/持Y；成功交换显式重新开始预览像素化效果，下一刷新请求Y的个体预览。','conflicting_reading':'暂持存在时冻结先前X预览、不更新。'},
'交换已经提交Q=X、暂持=Y；随后BACK提示正在持有并保这些值，也不会把预览身份或集合自动回滚。若媒体/消息/宿主失败，具体像素/异常恢复unknown。',
{'read_source':'指定储存文件全2022行，特别导航像素化/交换/预览选择三个必要分支。','read_formal':SPEC+':1-300及B16-004/BX持有操作行','absence_or_conflict':'§9以无条件“暂持时马赛克预览不更新”概括；源仅导航启动效果有持有早返，交换另有明确效果重启、预览优先当前持有成员。','limit':'未推导逐帧图、素材加载结果或动画必须在多久完成。'},
'S:1813-1842;S:1131-1149;S:1418-1479;S:837-841',
'后续规格消费者可能把持有期间所有预览更新都禁止，成功交换后仍展示旧暂持X，和当前持有Y不一致。',
'将§9句子限定为“暂持期间单纯导航不重新触发预览像素化；预览仍取当前暂持对象，成功交换会重启效果并在后续刷新改为新暂持对象”。只要求逻辑请求和触发身份，不增加媒体运行保证。',sync_basic,
['单纯导航仍取X且不重启导航像素化。','成功交换后持Y，后续预览请求Y，交换有独立重启效果。','保留暂持BACK禁退及已经提交交换不回滚，不添加真实像素/逐帧PASS。'],
['B16-004 P=X/Q=Y held链','BX B03/B07','§3.2/§4.2交换守卫及治疗配置','§9媒体未证边界'],
'非提出者需尝试解释§9句子是否仅指导航触发、并回读交换与预览消费者反证；若其本身可无歧义限定导航，可下调为澄清而非冲突。'),
finding('UI-ST-003','形态选择器首末上下回绕未进入本域合同', 'SOURCE_FEATURE_COVERAGE_GAP','MEDIUM',[(239,'§7.2，形态移动与写入'),(229,'§7.1相邻但不同的物种边界夹限')],
'E:446-483;E:507-511;PD:138-140;L:868-894',
['可列项>1，合法多项形态夹具、首项为雄形态0、末项为雄具名形态1，末次当前项匹配；显示全部关但两项已见。','每个输入在独立采样轮，呈现/记录依赖正常；不以单项BULBASAUR推可达。'],
{'initial_current':'首项','input':'DOWN','expected':'到次项，下一循环写末次性别/形态并固定false。'},
[{'initial_current':'首项','input':'UP','expected':'回绕末项，下一循环覆盖末次记录'}, {'initial_current':'末项','input':'DOWN','expected':'回绕首项，下一循环覆盖末次记录'}],
'随后独立BACK/USE都退出，不恢复首轮或回绕移动已写值；这不是§7.1物种导航的边界停住，也不是LEFT/RIGHT页夹限。异常媒体/宿主结果unknown。',
{'read_source':'条目文件全619行；形态选择器446-483及其多项USE门507-511；写记录consumer138-140。','read_formal':SPEC+':1-300及BX B28-B31/B38、R4-DX05、PD31-34','absence':'正文只说明每次上下移动写入，未给首末移动结果；已有静态用例没有形态首端UP/末端DOWN边界向量。','limit':'缺项为本域功能覆盖，不声称现有文字明确要求夹限，也不要求改领域形态资格规则。'},
'E:507-511;PD:138-140;L:868-894',
'后续实现可按相邻条目物种导航夹限处理形态列表，端点UP/DOWN不回绕、不产生对应末次写入，行为和保存形态不同。',
'§7.2补一句可列形态上下首末循环回绕，并加首项UP、末项DOWN两个独立向量及BACK保移动写入对照；明确与物种导航/页导航分开。',sync_basic+['deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md §6.1仅交叉引用（若root认为需同步）','deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md（若新增领域对应ID）'],
['形态首UP→末/末DOWN→首且移动后记录写入有唯一预期。','BACK仍不回滚；单项Forms不开选择器。','条目物种UP/DOWN仍边界停住、LEFT/RIGHT仍页夹限。'],
['BX B28/B29/B30/B31/B38','R4-DX05/PD34：多项首轮false与单项不开分界','WP62末次形态直接写字段默认false/不刷新门','§6.3返回主列表重跑读取新末次形态'],
'非提出者需搜索固定正式正文及对应目录的形态首末行为，尝试证明已覆盖或scope排除；必须区别物种、页面、形态三种导航。'),
finding('UI-ST-005','储存自有选择循环的输入阶段与优先级未规格化', 'SOURCE_FEATURE_COVERAGE_GAP','MEDIUM',[(65,'§3.1导航与USE/BACK'),(215,'§6.2.2图鉴子页已有顺序，未推广其它UI'),(217,'§6.2.2图鉴主页已有顺序，未推广其它UI')],
'S:837-910;S:938-985;S:1314-1392;S:679-714;S:733-790;S:811-834',
['普通盒/队伍选择器正常处于网格成员焦点，没有方向导致的切盒动画或额外输入更新；按各阶段查询时的服务布尔条件为前提。','方向均repeat；盒/队伍/标记方向采用覆盖式优先UP>LEFT>RIGHT>DOWN，之后独立动作阶段；不声称实体键组合可达。','若方向阶段切盒，切盒辅助正常结束会再次更新输入，第二阶段查询不保证保留第一阶段快照，必须保留该限定。'],
{'initial':'盒当前0/格0与格1各有合法不同成员','input':'仅USE trigger','expected':'返回格0并显示其操作菜单；不改当前盒/集合。'},
[{'initial':'盒0/格0和格1各有合法不同成员','input':'RIGHT repeat和USE trigger在对应阶段均成立，其余假','source_expected':'先焦点到格1，当轮USE返回格1并菜单其成员','under_specified_alternative':'只处理方向等待下一轮、或先USE选择格0'},
 {'initial':'盒0合法焦点，没有方向','input':'JUMPDOWN与BACK在按钮阶段均成立','source_expected':'JUMPDOWN分支优先并切盒写当前盒1；本轮不发退出确认','under_specified_alternative':'BACK先退出确认/忽略切盒'}],
'方向+USE可先改变局部焦点再选择；JUMP+BACK优先切盒的当前盒写入保留，后续独立BACK才发确认且退出不回滚。持有时退出仍被上层阻止；不据同轮输入证明宿主异常恢复。',
{'read_source':'储存全2022行，盒选择837-910、队伍938-985、标记1314-1392、操作命令679-714。','read_formal':SPEC+':1-300、BX B01-B39与本域补充及U06-M11-002/003-F/J；WP17:106-122。','absence':'盒子段给各键单独结果而没有两阶段/方向优先；现有图鉴阶段条款明确不推广其它UI。WP17通用命令出口竞争不能代替储存自有JUMP/SPECIAL/ACTION阶段。','limit':'只提未覆盖输入服务顺序，不声称游戏/键盘运行缺陷；不推广到所有UI，也不扩张切盒阶段Input.update后的条件。'},
'S:912-936;S:1507-1526;S:1592-1619;S:1626-1650;S:1967-2014',
'同轮条件符合时，先方向再USE可选择另一成员；JUMP与BACK竞争可直接写当前盒。无该合同则不同可接受实现会产生不同选择和持久状态。',
'补储存选择器的局部两阶段合同：方向repeat覆盖优先UP>LEFT>RIGHT>DOWN；盒动作依JUMPUP>JUMPDOWN>SPECIAL>ACTION（仅整理）>BACK>USE，队伍动作ACTION（仅整理）>BACK>USE。标记方向后BACK>USE如纳入同补；普通操作命令BACK>USE已有通用依赖保持。注明会产生额外输入更新的切盒阶段不能视作不变单快照。新增普通网格RIGHT+USE、无方向JUMPDOWN+BACK独立静态向量。',sync_basic,
['两个最小向量各有唯一局部焦点/选择/当前盒预期，标清repeat/trigger及其它查询假。','任何新增步骤不得把切盒内输入更新抹掉，不声称实体键/媒体/真实Demo通过。','单键及持有禁退/后续退出保切盒写入回归不变。'],
['BX B03/B05/B06/B07','§6.2.2图鉴主/子循环相异顺序','WP17普通命令BACK>USE','标记副本OK/BACK','切盒辅助1020-1062末尾输入刷新'],
'非提出者需尝试用现有§3.1、WP17和测试目录反证两阶段已经覆盖；再回读方向切盒的额外Input.update，核查本候选前提是否足够排除快照变化。')]

links={'UI-ST-001':['UI-ST-S-0811'], 'UI-ST-002':['UI-ST-S-1064','UI-ST-S-1131','UI-ST-S-1418'], 'UI-ST-003':['UI-ST-E-0446'], 'UI-ST-005':['UI-ST-S-0837','UI-ST-S-0938']}
for f in forward:
    f['finding_ids']=[id for id,uids in links.items() if f['id'] in uids]
dump_jsonl('forward-matrix.jsonl',forward)
dump_jsonl('reverse-matrix.jsonl',reverse)
(OUT/'findings.json').write_text(json.dumps({'status':PENDING,'findings':findings,'discarded_hypotheses':[{'id':'H-DEFAULT-CONFIRM','reason':'本地普通确认Yes/No默认0、BACK为false，与WP17普通确认依赖一致；源默认已记入forward。可选明示不作为独立缺陷。'}]},ensure_ascii=False,indent=2)+'\n')

# Semantic ledger entries are manually authored at range granularity.
# Hashes identify input identity only; delivery-ledger does not confer semantic review.
manual_reads=[
('M',1,129,'全文审读：区域名字/两计数/完成阈值；BACK/USE返回值，写观看区域后主列表返回区域菜单。','FULL_ASSIGNED_SOURCE_REVIEW'),
('L',1,400,'全文连续首段：列表标记/未见占位；焦点呈现；场景四状态初始化；区域映射及索引；行来源/末次形态/普通列表修剪排序首段。','FULL_ASSIGNED_SOURCE_REVIEW'),
('L',401,800,'连续第二段：普通列表排序尾与刷新；普通/结果计数；搜索主/子呈现与US异常体重/哨兵；普通预览与过滤前段。','FULL_ASSIGNED_SOURCE_REVIEW'),
('L',801,1200,'连续第三段：过滤拥有/已见门、搜索排序；结果BACK复位/条目返回重跑；大小及普通参数两阶段/双槽；主搜索候选和输入/参数接受前段。','FULL_ASSIGNED_SOURCE_REVIEW'),
('L',1201,1302,'连续末段：外层草稿提交；Reset、零命中/非空接受分流，四状态保留；主列表索引与ACTION/BACK/USE顺序及正常收尾。','FULL_ASSIGNED_SOURCE_REVIEW'),
('E',1,400,'条目首段全文：完整/简略初始化与编号；普通请求；可列结构/性别/名字规则；信息拥有门/计数/单位；遭遇资格/占位掩码/可见并集/未知区域。','FULL_ASSIGNED_SOURCE_REVIEW'),
('E',401,619,'条目末段：标签；物种边界停住/跳未见；Forms首轮及回绕移动写记录、BACK保值；完整页互斥输入/页夹限；摘要单种与简略生命周期。','FULL_ASSIGNED_SOURCE_REVIEW'),
('S',1,400,'储存首段：盒格仅首方格；释放、像素化、暂持图标演出与领域分层；盒初始化背景缓存/兼容文本/不可用回写/非匹配与负数边界。','FULL_ASSIGNED_SOURCE_REVIEW'),
('S',401,800,'储存第二段：盒图标源留格；队伍图标压缩与默认显示；模式/初始状态；消息/命令默认与取消；盒网格导航。','FULL_ASSIGNED_SOURCE_REVIEW'),
('S',801,1200,'储存第三段：队伍末按钮特殊上下；盒/队伍方向和动作两阶段；模式1不进队伍；背景/切盒写入与输入刷新；暂持导航抑制效果但交换重启；拿/放/取/存呈现链。','FULL_ASSIGNED_SOURCE_REVIEW'),
('S',1201,1600,'储存第四段：释放演出尾；选盒当前焦点；命名取消/写入；摘要完整容器/暂持单项与游标；标记副本；预览取当前暂持；模式0菜单/退出及模式1前段。','FULL_ASSIGNED_SOURCE_REVIEW'),
('S',1601,2000,'储存第五段：取出/存入/模式3生命周期与临时标志；本地Yes首项默认/取消；逐操作守卫和治疗/提交次序；Item部分提交；盒命令焦点；选择负位置及Select前段。','FULL_ASSIGNED_SOURCE_REVIEW'),
('S',2001,2022,'储存末段：选择模式各实际修改分支与正常关闭/临时标志清；只返回位置，既有集合操作保留。','FULL_ASSIGNED_SOURCE_REVIEW'),
(SPEC,1,149,'正式上半逐条审读：scope、入口门、选择负位置、导航、暂持、菜单顺序、逐操作写序、摘要/嵌套Item、退出、图鉴入口与普通列表；导航末按钮与输入阶段列候选。','FULL_ASSIGNED_FORMAL_REVIEW'),
(SPEC,150,225,'正式中段逐条审读：普通预览，十参数四状态，37档/哨兵、类型槽、普通焦点全转移、主/子输入分层及结果退出；字段缓存/未命中保留来源对照。','FULL_ASSIGNED_FORMAL_REVIEW'),
(SPEC,226,300,'正式末段逐条审读：三页/信息/Area/单位/形态资格和首轮写；摘要简略；各不变量/背景兼容边界/保留和目录，预览过宽及形态回绕缺项列候选。','FULL_ASSIGNED_FORMAL_REVIEW'),
(TEST,244,289,'BX39行逐条对照源与前提/取消/守卫；跨页和持有写入、失败搜索四状态、特殊负位置、形态首轮静态预期；不把目录当已执行。','ASSIGNED_TEST_SCOPE_REVIEW'),
(TEST,584,610,'补充表全文阅读，本域B16-004/A055/A056/C118盒格部分/C120-C123逐行复核；其余行只是相邻上下文未纳入本域PASS。','ASSIGNED_TEST_ROWS_AND_CONTEXT'),
(TEST,661,685,'本域共享持物前提与U05-MV01–03三对照逐条复核；数量/战斗文本行是邻近上下文，不宣称本域全审。','ASSIGNED_TEST_ROWS_AND_CONTEXT'),
(TEST,775,787,'R4-DX01–05共同前提及五条普通请求/保异色/首轮另写false/单项对照逐条复核；资源结果unknown。','ASSIGNED_TEST_SCOPE_REVIEW'),
(TEST,858,880,'U06-M11-002 A–E及003-F/J逐条焦点/选值/提交/阶段对照；其它UI003行只读上下文，未替其主责宣告PASS。','ASSIGNED_TEST_ROWS_AND_CONTEXT'),
(PDTEST,112,149,'PD全表读取；UI实际引用PD09–11、13–16、19、25、28–34仅相应组件对照，领域独有登记/编译/接收未纳本域PASS。','CROSS_DOMAIN_TEST_ROWS_AND_CONTEXT'),
(PDTEST,195,238,'栖息地共同前提/四掩码向量；R4-PD五条及M11-001 A–G逐条对照Area/普通请求/有限ASCII；WP63消费者明确引用非重审。','CROSS_DOMAIN_TEST_ROWS_AND_CONTEXT'),
('D',1,266,'必要领域消费者：默认网格/容量/伪位置、背景可用、直接寻址、同对象移动/捕获/删源压缩及治疗；未审地区代理末段。','NECESSARY_CONSUMER_REVIEW'),
('PC',149,225,'必要入口消费者：创始人显示与四命令；默认整理0；PC整队取出/存入前置与取消。','NECESSARY_CONSUMER_REVIEW'),
('PAUSE',125,164,'必要入口消费者：图鉴可见门/当前区域直接/单区域写/多区域菜单。','NECESSARY_CONSUMER_REVIEW'),
('P',130,185,'必要临时标志消费者：形态读取强制形态先行，再战斗/储存短路；正常动态处理及登记写另归WP21。','NECESSARY_CONSUMER_REVIEW'),
('P',298,312,'治疗消费者：蛋无作用、完整治愈清准备标记，UI保存/恢复该标记。','NECESSARY_CONSUMER_REVIEW'),
('PARTY',742,794,'必要SPECIAL消费者：许可能存储且非快捷目标时打开整理，返回硬重建；本域不全审队伍本体。','NECESSARY_CONSUMER_REVIEW'),
('PARTY',1434,1494,'必要嵌套ItemMove消费者：旧物身份缓存、选择取消/目标门/给空目标或交换；嵌套取回部分提交后旧身份仍用。','NECESSARY_CONSUMER_REVIEW'),
('PURIFY',1260,1291,'选择模式必要调用者：编成层打开储存通用选择，原位置直接返回；不穷尽净化室后续。','NECESSARY_CONSUMER_REVIEW'),
('PD',45,88,'已见形态任一异色查询/缺记录初始化，已见守卫未知返回false；形态资格直接消费。','NECESSARY_CONSUMER_REVIEW'),
('PD',90,178,'区域计数接点、末次读默认/缺记录初始化、直接三参写默认false、拥有守卫；不把查询名当全纯。','NECESSARY_CONSUMER_REVIEW'),
('PD',315,361,'可访问缓存/当前区域映射与区域计数nil失败；UI不额外保护；仅全国默认缓存资格。','NECESSARY_CONSUMER_REVIEW'),
('SUM',1190,1231,'摘要必要消费者：给予通用物品传当前位置、ViewDex先最近见到写再完整单种；本体其它页未全审。','NECESSARY_CONSUMER_REVIEW'),
('BAG',590,617,'袋选择必要消费者：保存浏览口袋/索引，过滤选择正常收尾恢复，不保证异常恢复。','NECESSARY_CONSUMER_REVIEW'),
('IU',781,857,'摘要给予及取回必要消费者：蛋/邮件/换物、写信、袋前缀与失败；直接盒Item不调用它。','NECESSARY_CONSUMER_REVIEW'),
('MAIL',100,125,'写信必要消费者：前两字段快照仍玩家队伍k+2/k+1，第三实际收信对象，文本取消重试；不等同盒邻格。','NECESSARY_CONSUMER_REVIEW'),
('U',380,425,'图鉴区域/序号/成员/长度必要消费者：缺表0或nil，成员克隆、全国长度；回退与计数失败分层。','NECESSARY_CONSUMER_REVIEW'),
('ENC',1,71,'Area必要消费者全文：版本注册键/单取回退与版本枚举v0同时纳入缺陷，不据注释改语义。','NECESSARY_CONSUMER_REVIEW'),
('ITEM',180,195,'可携带筛选必要定义：非重要物可持；盒直接给物不自动写邮件字段。','NECESSARY_CONSUMER_REVIEW'),
('SHAPE',1,116,'14种体型注册次序/图标身份；HeadArms索引3；只读文本不证图集。','NECESSARY_CONSUMER_REVIEW'),
('COLOR',1,78,'10种体色次序/名称；Gray索引7；本地化名字不变身份。','NECESSARY_CONSUMER_REVIEW'),
('GLOBAL',21,29,'图鉴观看区域/索引/模式字段声明，持久消费者归全局保存域。','NECESSARY_CONSUMER_REVIEW'),
('GLOBAL',71,83,'观看默认区域/模式0/各索引0；仅全国区域默认-1，场景参数从持久字段初始化。','NECESSARY_CONSUMER_REVIEW'),
('SET',210,227,'6队/40盒默认及存入治疗世代门，目录值是默认不是全域容量不变量。','NECESSARY_CONSUMER_REVIEW'),
('SET',301,316,'当前地区/显示全部/偏移配置默认，与UI消费路径分别对照。','NECESSARY_CONSUMER_REVIEW'),
('deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md',106,122,'必要正式依赖普通/严肃确认与初始索引/取消、BACK先USE；确认默认假设未提出独立缺陷。','NECESSARY_FORMAL_DEPENDENCY_REVIEW')]
ledger=[]
for k,a,b,semantic,stage in manual_reads:
    path=FILES.get(k,k); data=get(path).encode()
    ledger.append({'path':path,'start_line':a,'end_line':b,'commit':REF if path.startswith('reference/pokemon-essentials/') else MAIN,
        'sha256':hashlib.sha256(data).hexdigest(),'delivery_status':'DELIVERED','semantic_status':stage,
        'semantic_review_record':semantic,'source_to_formal_fact_records':'forward-matrix.jsonl' if k in 'MLES' and len(k)==1 else None,
        'clause_to_source_records':'reverse-matrix.jsonl' if path.startswith('deliverables/') else None,
        'review_basis':'实际阅读工具输出后作者语义记录；非delivery日志自动PASS','actual_reference_execution':'NOT_EXECUTED','independent_model_execution':'NOT_EXECUTED','host_demo_media_observation':'UNKNOWN'})
ledger.insert(0,{'path':'AGENTS.md','start_line':1,'end_line':184,'semantic_status':'INSTRUCTIONS_FULLY_READ','semantic_review_record':'参考只读、净化行为输出、无新框架、按增量与独立双向覆盖审计；实际文件全文已cat，行数为下方validation实测更新。'})
ledger[0]['end_line']=len((ROOT/'AGENTS.md').read_text().splitlines())
ledger.append({'path':SPEC,'range':[1,300],'semantic_status':'INITIAL_DELIVERY_TRUNCATED_REPLACED_NOT_USED_AS_FULL_READ_PROOF','semantic_review_record':'首次1–300输出发生截断；后续分别1–149、150–225、226–300完整输出和审读覆盖其全量，不据首条交付日志给PASS。'})
dump_jsonl('reading-ledger.jsonl',ledger)

from collections import Counter
status={
 'task':'R6-UI/storage','status':'FULL_ASSIGNED_SEMANTIC_REVIEW_COMPLETE_PENDING_COUNTERREVIEW_AND_ROOT_ADJUDICATION',
 'required_outputs_complete':True,'missing_semantic_reads':[], 'blocked':False,
 'fixed_inputs':{'main_commit':MAIN,'main_tree':'6ab3429170d2762607fbc2237014c3a160449fa1','formal_tree':'1046fbb657882e84b3dfc6d017943a9edf7782e5','reference_commit':REF,'reference_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0'},
 'model_metadata':{'model':'UNVERIFIED','model_uuid':'UNVERIFIED','effort':'UNVERIFIED','tier':'UNVERIFIED','speed':'UNVERIFIED','session_uuid':'UNVERIFIED'},
 'coverage':{'assigned_source_files':4,'assigned_source_lines':4072,'source_methods_inventoried':179,'source_methods_semantically_reviewed':179,'source_context_or_constants_separately_reviewed':7,'formal_primary_file_lines':300,'formal_primary_denominator_blocks':181,'formal_primary_blocks_reviewed':181,'formal_test_rows_reviewed_in_scope':94,'reverse_total_records':275,'forward_total_records':186,'reading_ledger_records':len(ledger)},
 'coverage_status_counts':dict(Counter(x['disposition'] for x in forward)),
 'findings':{'count':4,'ids':[f['id'] for f in findings],'status':PENDING,'adjudicated_findings':0},
 'counterreview_additional_task':{'file':'counterreview-R6-UI-001.json','role':'NON_PROPOSER','verdict':'CONFIRM_STATIC_LOCAL_ORDER_CONFLICT','adjudication':'PENDING_GLOBAL_ROOT_ADJUDICATION'},
 'validation_modes':{'static_reasoning':'FULL_ASSIGNED_TEXT_AND_NECESSARY_CONSUMERS_READ','delivery_tools':'EXECUTED_READ_ONLY_NOT_SEMANTIC_PASS','actual_reference_execution':'NOT_EXECUTED','independent_model_execution':'NOT_EXECUTED','host_demo_media_observation':'UNKNOWN'},
 'permissions_and_mutations':{'write_scope':str(OUT.relative_to(ROOT)),'formal_or_reference_modified':False,'git_switch_commit_push':False,'downloads_or_installation':False,'external_services_security_or_real_saves_changed':False,'update_started':False},
 'operational_notes':['首次正式全量交付截断，已用三段修复；范围工具几次路径/长度错误均未给semantic credit，后续指定全量读集已覆盖。','reading-ledger与delivery-ledger严格分离；结构/表头非语义PASS；域外历史/媒体/资源/input/Demo均保留。','必要域外消费者仅按实际读取区间核对，不声称那些文件全量审计。']}
(OUT/'task-status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
report='''# R6-UI/storage 独立双向审读

固定输入：main `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`／tree `6ab3429170d2762607fbc2237014c3a160449fa1`；formal tree `1046fbb657882e84b3dfc6d017943a9edf7782e5`；参考 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`／tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。以上身份只读核验。模型 UUID、effort、tier、speed 与实际 session UUID 无可验证回显，均为 UNVERIFIED。

本子域全量语义审读已完成，发现尚未裁决。4 个指定源码文件共 4072 行，逐个 179 callable unit 记录事实、必要消费者和正文接点，另 7 个结构／常量上下文单列。正式 WP66-B 全 300 行、公共分母 181 block 全量逆向记录；相关目录 94 行逐 ID 核对。`forward-matrix.jsonl` 186 行、`reverse-matrix.jsonl` 275 行。结构／表头、仅交付日志与域外上下文不计为源行为 PASS。没有缺读阻塞。

所有结论属于静态源与必要消费者推导，未运行参考游戏、独立模型或真实 Demo。源读取工具确实执行，只证明输入交付和身份；不证明语义正确、实体输入可达、素材存在、绘图、发声或异常外层恢复。首次正式文件1–300交付截断，已以1–149、150–225、226–300三个完整输出补齐。几次工具路径／长度错误没有计入覆盖。语义记录见 `reading-ledger.jsonl`，原始交付与范围日志分别见 `delivery-ledger.jsonl`／`read-logs/`。

## 待非提出者反证的候选

| ID | 精确正文接点 | 类型／影响 | 必要反例 |
| --- | --- | --- | --- |
| UI-ST-001 | WP66-B:65，§3.1队伍导航 | 状态转移缺少例外，MEDIUM | 默认末按钮6：UP→5、DOWN→0，不能按成员上下±2／越界6概括。 |
| UI-ST-002 | WP66-B:264，§9暂持预览 | 无条件表述过宽，MEDIUM | 拿X后成功交换Y：持有已成Y，交换重启像素化，后续预览请求Y；只有单纯导航的触发受暂持早返。 |
| UI-ST-003 | WP66-B:239，§7.2形态选择 | 功能边界覆盖缺项，MEDIUM | 可列项>1时首项UP→末项、末项DOWN→首项，下一循环覆盖末次，BACK保写；物种和页导航仍各自夹限。 |
| UI-ST-005 | WP66-B:65，§3.1选择循环 | 输入阶段覆盖缺项，MEDIUM | 普通盒格RIGHT repeat+USE trigger先移再选；无方向JUMPDOWN+BACK优先切盒写当前盒、不当轮退出。 |

以上全部为 `PENDING_NON_PROPOSER_COUNTERREVIEW_AND_ROOT_ADJUDICATION`，不是最终缺陷裁决。每项在 `findings.json` 记录精确源／规格、完整前提、普通对照、最小反例、取消／异常／部分提交、负证据范围、必要消费者、最小修订、同步文件、验收与回归，以及非提出者须主动尝试的反证。编号004未作为提案：本地确认Yes/No与默认0、取消false已检查，与WP17普通确认依赖一致；仅可选文字清晰化不足以独立提出缺陷。

## 已核对的状态与边界

- 输入：盒、队伍、标记方向为repeat；按查询次序形成UP>LEFT>RIGHT>DOWN优先，之后独立按钮阶段。盒按钮JUMPUP>JUMPDOWN>SPECIAL>ACTION（仅整理）>BACK>USE；队伍ACTION（仅整理）>BACK>USE；标记BACK>USE。方向切盒的内部辅助会刷新Input，不能将两个阶段强行视作一个不变服务快照；最小组合反例已限定没有该更新。图鉴主搜索与子页的两种顺序原文支持，未推广其它UI。
- 默认与取消：普通储存确认Yes首项／初焦点0，释放确认No首项；操作菜单默认首项，选盒默认当前盒，墙纸为当前背景匹配项否则首项。盒消息USE/BACK关闭；菜单BACK返回负值。存入选盒BACK不治疗不移动，标记BACK弃副本。背包过滤选择正常返回恢复浏览口袋和索引，异常不保证恢复。
- 暂持与部分提交：拿起演出返回后赋持有再删源；队伍压缩，盒留空格。交换后新目标与暂持立即改变；暂持BACK/Close不得退出。放／存／取／释／Item分别提交，正常退出不回滚。Item取回先加袋、成功消息返回才清持物；给予先成员写再袋删除，未追加事务承诺。
- mutable／cache：场景搜索接受参数、本地草稿、当前列表和持久模式分列；失败Start写模式但不替换其它三量，Cancel保模式。结果BACK复位模式／参数并找旧物种，条目返回重跑接受参数。末次形态读取对缺记录可初始化空记录，三参选择器写false与普通图像请求false分开。背景缓存相同不重新核对可用性；初始化／缓存不同时可能转旧文本或写默认；空值仅默认显示、非匹配文本数值比较可先失败、负整数−1不自动回写。均保媒体unknown。
- 守卫与必要消费者：PC整队门和内部逐目标门分开；治疗只在指定条件保进化准备；基本容器成员寻址只有−1为队伍，其余负盒号仍末端寻址。选择模式队伍按钮的负位置已按40×30重新核对，保留未穷尽后续Withdraw/Store边界。摘要完整容器／持有单项、写信快照玩家队伍k+2/k+1、ItemMove嵌套旧物身份和三对照已按必要源核对。
- 图鉴：区域两计数／完成标记与nil计数失败、普通列表过滤／数值修剪／平局、37档大小／哨兵／双类型、普通焦点邻接、图像固定普通而记录保异色、结构先于已见的形态列表、首轮浏览写入、Area有限ASCII占位／可见并集／v0版本泄漏，均逐源反查。真实资源、任意Unicode／损坏输入、WP63完整地图消费者、所有获得／捕获调用方、完整保存链及历史接受记录未扩大本域证明。

## 非提出者追加反证

`counterreview-R6-UI-001.json` 对 root 提出的WP67-A:228满队Add to party消息／队伍删除次序进行了新读源码、实际储存消费者和正式K32/K33核对，结论为 `CONFIRM_STATIC_LOCAL_ORDER_CONFLICT`，最终仍待global root裁决。成功送盒后队伍删除先于旧成员送盒暂停，记忆左移和新成员入队在暂停正常返回后；报告主动检查默认可达性、选人取消、单Send控制、全满失败及消息内前缀，并没有更新提案或正式文件。

本子任务未改参考／正式／旧报告，未git切换、提交或push，未安装／下载／外服配置／真实存档操作，未启动update。全局Feature Matrix与追溯同步只作为以后经非提出者反证和root裁决后所需工作登记，不在此写入。
'''
(OUT/'report.md').write_text(report)
print(json.dumps({'final_forward':len(forward),'final_reverse':len(reverse),'semantic_ledger':len(ledger),'findings':len(findings),'missing_reads':[]}))

# Final precision pass: all atomic claims inside grouped denominator blocks, and
# freshly read default-data prerequisites, remain separate from runtime proof.
for row in reverse:
    c=row['formal_clause']
    if c['path']==SPEC:
        atoms=[]
        for line in range(c['start_line'],c['end_line']+1):
            for item in atomic.get(line,[]):
                atoms.append({'formal_line':line,**item})
        row['atomic_subclaims']=atoms
        if c['start_line']==194:
            row['source_preconditions']='默认PBS/types.txt共19身份，其中QMARKS为伪类型；正常按定义注册且筛掉伪类型时为18。类型构造缺省pseudo=false、遍历定义次序已读；未执行编译或验证真实加载注册。'
            row['source_evidence'] += [
                {'path':'reference/pokemon-essentials/PBS/types.txt','start_line':1,'end_line':129,'commit':REF},
                {'path':PREFIX+'010_Data/002_PBS data/003_Type.rb','start_line':18,'end_line':46,'commit':REF},
                {'path':PREFIX+'010_Data/001_GameData.rb','start_line':123,'end_line':126,'commit':REF}]
        elif c['start_line']==246:
            row['source_preconditions']='默认BULBASAUR基形及RATTATA基形/具名Alolan1 PBS已按必要区间新读；形态展示缺省等于自身、性别双性数据有效。实际已见记录、编译注册与媒体属于正式条件夹具，未执行。'
extra_reads=[
('reference/pokemon-essentials/PBS/types.txt',1,129,'完整类型默认作者数据19条，QMARKS伪类型排除后18；正常编译注册条件不等于真实dat/运行。'),
('reference/pokemon-essentials/PBS/pokemon.txt',3,29,'BULBASAUR基形作者数据为双性；各字段原始数据有效，普通预览夹具身份条件核对。'),
('reference/pokemon-essentials/PBS/pokemon.txt',469,496,'RATTATA基础形态双性、没有基础FormName字段；合法多项夹具基础身份核对。'),
('reference/pokemon-essentials/PBS/pokemon_forms.txt',74,88,'RATTATA形态1原始具名Alolan，省略PokedexForm，结合构造缺省可展示自身；多项首轮/回绕夹具来源。'),
(PREFIX+'010_Data/002_PBS data/003_Type.rb',1,66,'类型Schema映射伪类型，缺省false；UI枚举由正常数据注册前提决定。'),
(PREFIX+'010_Data/001_GameData.rb',78,134,'按定义注册和按定义次序遍历；身份查找类型/未知边界与UI候选次序的必要消费者。'),
(PREFIX+'010_Data/002_PBS data/008_Species.rb',175,198,'物种/形态/原始名称/展示形态/性别构造缺省，具名Alolan自身展示的必要消费者。'),
(PREFIX+'010_Data/002_PBS data/008_Species.rb',225,231,'形态名本地化接点；真实语言目录不在本域证明。'),
(PREFIX+'001_Settings.rb',12,18,'当前固定机制世代8源值，原存入治疗默认关闭所需配置条件。')]
for path,a,b,fact in extra_reads:
    ledger.append({'path':path,'start_line':a,'end_line':b,'commit':REF,'sha256':hashlib.sha256(get(path).encode()).hexdigest(),'delivery_status':'DELIVERED','semantic_status':'NECESSARY_DATA_OR_CONSUMER_REVIEW','semantic_review_record':fact,'review_basis':'作者读取新增范围后写语义记录，不由数据解析或delivery产生PASS','actual_reference_execution':'NOT_EXECUTED','independent_model_execution':'NOT_EXECUTED','host_demo_media_observation':'UNKNOWN'})
for f in forward:
    if f['id'] in ['UI-ST-L-0896','UI-ST-L-1092']:
        f['necessary_consumers'] += [{'path':'reference/pokemon-essentials/PBS/types.txt','start_line':1,'end_line':129,'commit':REF},{'path':PREFIX+'010_Data/001_GameData.rb','start_line':123,'end_line':126,'commit':REF}]
    if f['id']=='UI-ST-E-0446':
        f['necessary_consumers'] += [{'path':'reference/pokemon-essentials/PBS/pokemon.txt','start_line':469,'end_line':496,'commit':REF},{'path':'reference/pokemon-essentials/PBS/pokemon_forms.txt','start_line':74,'end_line':88,'commit':REF},{'path':PREFIX+'010_Data/002_PBS data/008_Species.rb','start_line':175,'end_line':193,'commit':REF}]
status['coverage']['reading_ledger_records']=len(ledger)
dump_jsonl('forward-matrix.jsonl',forward)
dump_jsonl('reverse-matrix.jsonl',reverse)
dump_jsonl('reading-ledger.jsonl',ledger)
(OUT/'task-status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
report=report.replace('BULBASAUR/RATTATA数据有效性沿正式夹具，本域未逐条核对PBS/媒体。','BULBASAUR/RATTATA必要PBS字段已核对，真实编译注册/媒体仍未知。')
report=report.replace('真实资源、任意Unicode／损坏输入、WP63完整地图消费者、所有获得／捕获调用方、完整保存链及历史接受记录未扩大本域证明。','默认类型19身份去除QMARKS伪类型为18，BULBASAUR基形和RATTATA基形／具名Alolan1的必要PBS字段及展示形态缺省已新读；编译／真实加载注册与媒体未执行。真实资源、任意Unicode／损坏输入、WP63完整地图消费者、所有获得／捕获调用方、完整保存链及历史接受记录未扩大本域证明。')
(OUT/'report.md').write_text(report)
print(json.dumps({'final_semantic_ledger':len(ledger),'atomic_claims_in_grouped_blocks':'complete','default_data':'bounded_read_not_runtime'}))
