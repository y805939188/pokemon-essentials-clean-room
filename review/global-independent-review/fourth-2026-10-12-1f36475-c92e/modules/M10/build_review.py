"""Generate this bounded review's records; does not run or modify the reference."""
import json
import re
import subprocess
from pathlib import Path
from collections import Counter

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
REF = Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
B = '1f36475d22120a0d1175967d5b17d71fe8311d88'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REVIEWER = 'M10 / thread 01a12ff1-a1b1-7212-84b3-c3fdcd6552a9'
F = 'deliverables/final-specification-set/'
U = F + 'user-interface/'
E = F + 'engine-overworld/'
T = F + 'test-catalog/'
UI_TEST = T + 'user-interface-wp17-63-65-66-67-68-69-70-71.md'
S = {
 'msg':'Data/Scripts/007_Objects and windows/011_Messages.rb',
 'text':'Data/Scripts/007_Objects and windows/005_SpriteWindow_text.rb',
 'draw':'Data/Scripts/007_Objects and windows/010_DrawText.rb',
 'cfg':'Data/Scripts/007_Objects and windows/002_MessageConfig.rb',
 'window':'Data/Scripts/007_Objects and windows/004_SpriteWindow.rb',
 'cache':'Data/Scripts/007_Objects and windows/001_RPG_Cache.rb',
 'bitmap':'Data/Scripts/007_Objects and windows/008_AnimatedBitmap.rb',
 'files':'Data/Scripts/001_Technical/002_Files/001_FileTests.rb',
 'speciesfiles':'Data/Scripts/010_Data/002_PBS data/009_Species_files.rb',
 'metrics':'Data/Scripts/010_Data/002_PBS data/010_SpeciesMetrics.rb',
 'pkmsprite':'Data/Scripts/014_Pokemon/001_Pokemon-related/003_Pokemon_Sprites.rb',
 'move':'Data/Scripts/010_Data/002_PBS data/005_Move.rb',
 'target':'Data/Scripts/010_Data/001_Hardcoded data/017_Target.rb',
 'gamedata':'Data/Scripts/010_Data/001_GameData.rb',
 'miscdat':'Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb',
 'audio':'Data/Scripts/008_Audio/002_Audio_Play.rb',
 'system':'Data/Scripts/004_Game classes/002_Game_System.rb',
 'trans':'Data/Scripts/009_Scenes/001_Transitions.rb',
 'eventscene':'Data/Scripts/009_Scenes/002_EventScene.rb',
 'intro':'Data/Scripts/012_Overworld/002_Battle triggering/002_Overworld_BattleIntroAnim.rb',
 'title':'Data/Scripts/016_UI/001_Non-interactive UI/001_UI_SplashesAndTitleScreen.rb',
 'controls':'Data/Scripts/016_UI/001_Non-interactive UI/002_UI_Controls.rb',
 'hatch':'Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb',
 'evolve':'Data/Scripts/016_UI/001_Non-interactive UI/004_UI_Evolution.rb',
 'trade':'Data/Scripts/016_UI/001_Non-interactive UI/005_UI_Trading.rb',
 'hof':'Data/Scripts/016_UI/001_Non-interactive UI/006_UI_HallOfFame.rb',
 'credits':'Data/Scripts/016_UI/001_Non-interactive UI/007_UI_Credits.rb',
 'load':'Data/Scripts/016_UI/013_UI_Load.rb',
 'pause':'Data/Scripts/016_UI/001_UI_PauseMenu.rb',
 'pc':'Data/Scripts/016_UI/019_UI_PC.rb',
 'options':'Data/Scripts/016_UI/015_UI_Options.rb',
 'card':'Data/Scripts/016_UI/012_UI_TrainerCard.rb',
 'ready':'Data/Scripts/016_UI/016_UI_ReadyMenu.rb',
 'party':'Data/Scripts/016_UI/005_UI_Party.rb',
 'summary':'Data/Scripts/016_UI/006_UI_Summary.rb',
 'storage':'Data/Scripts/016_UI/017_UI_PokemonStorage.rb',
 'bag':'Data/Scripts/016_UI/007_UI_Bag.rb',
 'itemstorage':'Data/Scripts/016_UI/018_UI_ItemStorage.rb',
 'mart':'Data/Scripts/016_UI/020_UI_PokeMart.rb',
 'bp':'Data/Scripts/016_UI/021_UI_BattlePointShop.rb',
 'dexentry':'Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb',
 'scene':'Data/Scripts/011_Battle/004_Scene/001_Battle_Scene.rb',
 'commands':'Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb',
 'play':'Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb',
 'objects':'Data/Scripts/011_Battle/004_Scene/006_Battle_Scene_Objects.rb',
 'baseanim':'Data/Scripts/011_Battle/004_Scene/007_Battle_Scene_BaseAnimation.rb',
 'anims':'Data/Scripts/011_Battle/004_Scene/008_Battle_Scene_Animations.rb',
 'player':'Data/Scripts/011_Battle/007_Other battle code/007_BattleAnimationPlayer.rb',
 'arena':'Data/Scripts/011_Battle/008_Other battle types/004_BattleArenaBattle.rb',
 'battle':'Data/Scripts/011_Battle/001_Battle/001_Battle.rb',
 'interpreter':'Data/Scripts/003_Game processing/004_Interpreter_Commands.rb',
}
P = {
 '17':U+'wp17-messages-windows-input.md', 'tags':U+'wp17-draw-text-tags.md',
 '15':E+'wp15-resource-matching-and-audio.md',
 '16':E+'wp16-world-rendering-and-visual-transitions.md',
 'pre':E+'wp16-pre-battle-transitions.md',
 '65':U+'wp65-title-load-options-pause-and-pc.md',
 'card':U+'wp65-trainer-card-appendix.md', 'controls':U+'wp65-controls-help-appendix.md',
 '66a':U+'wp66-a-party-and-summary-ui.md', '66b':U+'wp66-b-storage-and-pokedex-ui.md',
 '66c':U+'wp66-c-bag-item-storage-and-shop-ui.md',
 '67a':U+'wp67-a-battle-interaction-and-presentation.md',
 '67b':U+'wp67-b-lifecycle-presentations-and-history.md',
 '74':F+'demo-dx/wp74-battle-animation-authoring-and-exchange.md',
 '56':F+'combat-requirements/wp56-palace-and-arena-variants.md',
 '02':F+'generic-kernel/wp02-rule-configuration-and-data-variants.md',
 '03':F+'generic-kernel/wp03-content-identity-and-schema.md',
}

def dump(name, data):
    (OUT/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

def sa(key, loc, fact):
    return {'path':S.get(key,key), 'commit':R, 'lines_or_symbol':loc, 'fact':fact}

def pa(key, loc, fact='仅审所列条款；无全文件通过主张。'):
    return {'path':P.get(key,key), 'commit':B, 'lines_or_symbol':loc, 'fact':fact}

MATERIAL = {'source_text':'AVAILABLE_READ_ONLY', 'formal_text':'AVAILABLE_131_SHARED_IDENTITY',
            'graphics':'ABSENT', 'audio':'ABSENT', 'fonts':'8_FILES_PRESENT_NOT_HOST_VERIFIED',
            'maps_and_complete_demo':'ABSENT', 'game_host':'NOT_ESTABLISHED'}
caps = []
def cap(n, desc, src, spec, branches, reason, status='supported', findings=(), history=(),
        entry='合法输入与正常调用上下文；无插件改写。', limits='正常宿主接口为条件；真实媒体、输入及逐帧输出未运行。',
        not_checked='所列锚点外的组合与宿主表现未穷尽。', owner='M10', projection=None, classification=None):
    caps.append({'capability_id':f'GR4-CAP-M10-{n:03d}', 'module':'M10', 'description':desc,
       'classification':classification or ['User Interface','Engine / Overworld Integration'],
       'source_anchors':src, 'spec_anchors':spec, 'entry_and_preconditions':entry,
       'configuration_data_host_limits':limits, 'reviewer':REVIEWER,
       'checked_branches_boundaries':branches, 'evidence_level':['SOURCE_STATIC','SPEC_STATIC'],
       'execution_status':'NOT_EXECUTED', 'material_availability':MATERIAL, 'status':status,
       'reason':reason, 'related_findings':list(findings), 'history_links':list(history),
       'not_checked':[not_checked], 'primary_owner':owner, 'projection':projection})

cap(1,'消息预处理、暂停/等待与正常出口',
 [sa('msg','405–681','先做文本替换/控制位置计算；非暂停忙状态按键只恢复；命令在消息结束后执行；临时窗口正常末尾释放。'),sa('text','290–418','自动行满暂停插入与resume/skipAhead语义不同。')],
 [pa('17','§3.1–3.3、§7.1–7.3','替换顺序、四态、正常与异常清理分列。')],
 ['文首SE与正文SE','显式暂停、计时等待、全显出口','空换肤标记','调用中抛错不保证末尾清理'],
 '所选条款supported_static；未把普通消息按键解释为全文快进。')
cap(2,'普通命令/帮助命令与逐位数字输入的同轮竞争',
 [sa('msg','166–205;721–801','命令先BACK后USE，禁取消时仍可继续USE；逐位数字更新后先USE、elif BACK。'),sa('text','687–729;862–923','方向更新先于外层确认；数字和普通列表方向优先序不同。')],
 [pa('17','§4、§5.2–5.3、§7.2','有单键结果及更新机会，缺这两个入口的竞争裁决。'),pa('66c','§5.1','既有同轮表仅为物品数量与商店，不是逐位数字控件。')],
 ['USE+BACK','取消项0与2','UP+USE修改并当轮返回','越界USE+BACK仅蜂鸣继续'],
 '单键已有；同轮返回、同轮修改后确认及越界确认抑制取消未承接。','partial',['GR4-M10-001'],['GR3-M10-002：新范围同根，不改旧限定关闭'])
cap(3,'字体配置选择、字体标签回退与字体文件可得性',
 [sa('cfg','13–21;116–172;414–433','三档字体配置；配置候选按存在性取首个，无命中为空；设置失败重试默认候选。'),sa('draw','128–148;345–416','绘制入口另外对不可用字体选择Arial。')],
 [pa('17','§3.4、§8','列三档名/字号及笼统候选回退。'),pa('tags','§2、DT03/B04-D04','字体标记不可用时Arial。')],
 ['默认27/21/27','配置候选空与绘制Arial层分开','字体资源8文件存在不等于Font.exist或字形可用'],
 '字号和绘制回退有支持；配置候选的完整输入空间、字体内部名称与字形度量尚未形成/验证完整合同。','partial',not_checked='8个字体的内部字形/kerning、各平台注册、CJK与输入法、字形实际度量未审。')
cap(4,'窗口默认皮肤的冷读取回退与显式换肤',
 [sa('cfg','35–85','初取默认皮肤逐级回退；显式设置解析空结果后不再自动走初取回退。'),sa('window','835–868','窗口布局按资源尺寸分流，setSkin解析失败提前返回。'),sa('options','492–519','选项先写选择字段，再设置全局逻辑皮肤及预览。')],
 [pa('17','§3.4、§7.3','仅选项皮肤与通用资源边界。'),pa('65','§5.2 Speech/Menu Frame','描述正常即时预览；无初取与显式设置的回退区别。'),pa('15','§3、§5.1','通用图像解析/空白包装不能推出皮肤专属搜索链。')],
 ['所选资源存在','所选缺失但系统/通用备用存在','显式设置缺失','\u005cw[]直接清空另一路径'],
 '资源专属默认链与显式设置状态区别缺少正式承接。','partial',['GR4-M10-002'])
cap(5,'绘制标签识别、实体替换、图像消费边界',
 [sa('draw','75–125;345–468;621–658;940–1040','有标记走一般路径、无标记走快路径；文尾无字符不消费图像；直接绘图加载未由此兜底。')],
 [pa('tags','§1、§4.1、§5、§6.1','c/c3区别、图像尾部与有无标记实体解码差异均登记。')],
 ['无标记A&lt;B与带pg','仅img和文尾img/后接A','c覆盖阴影、c3空分量继承'],
 '所读识别/消费边界supported_static；不是所有21个标签的全部嵌套组合通过。',not_checked='字号、对齐、嵌套非法闭合、图形与字体混排所有组合未穷尽。')
cap(6,'普通/格式化文本长词折行及摘要备忘录消费',
 [sa('draw','128–241;611–658;1035–1040','两路径按词边界换行；行首无空格长串超宽不会逐字折行。'),sa('text','316–347','消息显示消费者传入内容宽度并使用格式化结果。'),sa('summary','481–539;542–638','蛋/普通备忘录在固定区域调用格式化文本；无自身滚动合同。')],
 [pa('tags','§6 L93','完整排版仅指向绘制函数，不给行为边界。'),pa('17','§3.3 自动行满暂停','只给显式换行后的行满暂停。'),pa('66a','§5.2','列备忘录字段，没有长串的折行/超宽规则。')],
 ['AB无空白超宽','A B在词边界换行','A换行B显式折行','有/无格式标记两路径'],
 '缺少会改变可见文本布局与暂停点的长词边界，不能由行满暂停推得。','partial',['GR4-M10-003'])
cap(7,'缓存与动画位图分入口资源失败',
 [sa('cache','31–65;89–91;116–144','有效缓存复用；非空直接加载无本地普通错误捕获；空名32方图；副本内容隔离。'),sa('bitmap','5–18;43–69;126–131;140–205','nil明确错误；前缀条带校验/时间片；非前缀普通加载错误变32方空白。')],
 [pa('15','§5、§5.1–5.2','直接缓存、包装、nil、条带与内嵌图像分列。')],
 ['nil/空名/非空缺失','前缀[0]帧数失败','条带宽不可整除','副本与共享命中'],
 '所选失败前提与内容共享supported_static；损坏媒体实际加载未证。',classification=['Generic Kernel','Engine / Overworld Integration'])
cap(8,'物种图像候选与路径后缀解析',
 [sa('speciesfiles','3–108;113–151','闪光/暗影/性别/形态/物种组合依次降格，蛋通用资源仍解析，个体回调复制后改图。'),sa('files','109–135','SE候选与图像png/gif解析分开。')],
 [pa('15','§3.1、§4.1','同级shiny目录、形态数据前提按入口分列。')],
 ['带变体命中','全部图像候选落空','蛋000仍需存在','Front/Back不先要求形态记录'],
 '已读路径候选supported_static；并未复查所有道具、训练家、脚印/影子/叫声分支。',not_checked='物种全数据集、全部媒体变体组合及alterBitmap扩展回调未穷尽。')
cap(9,'BGM/BGS暂停、记忆及选项音量消费',
 [sa('system','44–149;170–232','BGM零时长暂停只记位置；BGS暂停会停；恢复门为已暂停；记忆不复制播放记录。'),sa('audio','1–39;52–88;152–188;202–233','字符串与已解析记录的参数覆盖不同。'),sa('options','384–419','SE音量改写当前BGS请求量后再次缩放。')],
 [pa('15','§6.1–6.2','逻辑登记、请求与实际发声分开。'),pa('65','§5.2 音量两行','记录80经选项50变记录50、交付25的案例。')],
 ['BGM0暂停与BGS0暂停','正时长暂停','同记录记忆后音量更改','未暂停恢复无操作'],
 '该状态链supported_static，不将所有停止入口都推成有相同帧重置。',not_checked='音频时长解析器、地图自动播放、备用宿主音频类、轨道扩展及真实发声未全面复查。')
cap(10,'全部具名Transitions路由、单位与失败边界',
 [sa('trans','18–165','路由忽略大小写但保留扩展名；初始化前非正时长早退；中断先于旧过渡处置；宿主重试范围受限。')],
 [pa('16','§6.1','完整名称表与通用40/8单位。'),pa('pre','§5、§7.1','固定时长、实例化异常与宿主重试分开。')],
 ['ScrollLeft与SCROLLLEFT','ScrollLeft.png普通路径','正时长/零时长','中断旗标/在途旧过渡','共享资源加载失败不触发备用重试'],
 '全部名称逐一与路由对照；supported_static仅到列明的路由/时长/失败条件。')
cap(11,'通用碎片、条纹、缩放、八方向卷屏、马赛克与淡黑效果',
 [sa('trans','177–453','碎片下落/缩小与旋转，散射、随机条纹、中心放大、八方向移出、后段马赛克淡出及淡黑/淡显。')],
 [pa('16','§6.1名称表','覆盖各可见类别与调用方时长，明确不规定分块算法/逐像素图案。')],
 ['Rotating与Shrinking不同','Random Stripe V/H','八方向符号','Mosaic最后20%淡出'],
 '能力身份与类别有支持；随机分布、8×6/16×12分片、倍率/轨迹等源参数未在正式集承接，属于明示精细图案边界。','partial',not_checked='未把所有分片/随机参数逐项转为合同，也未执行任一效果。')
cap(12,'HGSS普通战前九类效果与四角变体资源消费',
 [sa('trans','458–1235','Snake/Diagonal固定1.25；水浪、各球效果固定时间及专属遮罩/球/浪图加载。')],
 [pa('16','§6.1'),pa('pre','§5–§7','默认选择与固定时长、共享资源异常已有合同；像素参数具名排除。')],
 ['Diagonal四角起点','ThreeBallDown2秒','四球0.9秒','水域昼夜分别效果','黑遮罩不是资源存在守卫的保证'],
 '选择/时长支持；逐效果图集尺寸、切分与各阶段参数仍只有源端可读，不声称完整重现合同。','partial',not_checked='不穷尽非常规屏幕/位图尺寸、每个阶段跳时、随机值或像素呈现。')
cap(13,'四组具名训练家转场与专用数据消费',
 [sa('trans','1244–1929','VSTrainer/EliteFour/Grunt/Admin分别4/3.5/1.6/3.1秒；类型/名字/玩家图上下文与各共享图消费。')],
 [pa('pre','§3、§5、§7','临时数据、资格、VSTrainer关键时间点与未取证像素边界。')],
 ['VS训练家3.8至4渐黑','EliteFour玩家图不在早退检查中','队员六个标志/干部条纹背景','类型图可解析不代表共享图成功加载'],
 '四具体效果全部源端语义阅读；正式合同只覆盖已承诺阶段/选择，详细资源布局和非VSTrainer时线保留partial。','partial')
cap(14,'标题、开场与载入菜单导航',
 [sa('title','1–129','开场停留可跳过；标题离开叫声等待1秒；删除组合与正常离开共用淡出。'),sa('eventscene','134–178','等待仍更新，先更新回调再输入分发。'),sa('load','281–356','可见项、调试跳过、载入选项回菜单、语言整体选项直写。')],
 [pa('65','§3.1–3.3','各可见条件/离开时序/语言写入分列。')],
 ['普通/调试','USE仅停留跳图','载入选项正常返回','语言有档/无档分叉'],
 '选定入口及正常退出supported_static；不把存档反序列化异常和素材存在性纳入通过。')
cap(15,'选项即时应用、关闭再应用与持久边界',
 [sa('options','327–362;384–447;492–519','本轮变更先应用再检查关闭；关闭再应用全部；音量和战斗开关/皮肤各自写入。'),sa('load','334–343','语言支路写回整个选项记录。')],
 [pa('65','§5.1–5.4','三层变化、预览与整体落盘分开。')],
 ['BACK保留已改值','未改项关闭再应用','载入背景音乐不预览','皮肤缺失另列CAP004'],
 '正常选项和持久层交界supported_static；不对缺失皮肤即时预览作无条件保证。',findings=['GR4-M10-002'])
cap(16,'暂停/PC/快捷主导航与子层取消',
 [sa('pause','48–127;239–321','暂停保存失败重显；退出先确认后忽略保存返回；游标确认才记。'),sa('pc','4–53;110–153;163–237','普通PC默认0重开，玩家/储存子层保局部索引；存入/取出入口门。'),sa('ready','245–331','快捷菜单候选、FLY取消重显、道具确认/返回门。')],
 [pa('65','§4.3、§6.1–6.2、§7–8','导航、写入与取消回哪层已分列。')],
 ['保存false留菜单','同意退出保存false仍退出','PC主层与子层记忆','队伍满取出/最后可用存入','快捷FLY取消重显/空候选不开菜单'],
 '所选链supported_static；菜单注册表和所有特殊模式组合不获全面通过。')
cap(17,'训练家卡画像、徽章与开始日期副作用',
 [sa('card','9–111','女性两资源独立回退；画像底边240；首次显示懒写开始时间；BACK退出。')],
 [pa('card','§3–§6、TC01–TC08','仅正面、底边定位、日期副作用和正常释放。')],
 ['女性背景/卡面独立','128×128与128×256底边相同','开始时间空','USE不退出'],
 '本次卡面消费样本supported_static，实际像素/字体未证。')
cap(18,'按键帮助事件场景的换页与取消',
 [sa('controls','8–83','4页，换页清USE回调，末页8单位淡黑；没有挂接BACK回调。'),sa('eventscene','155–178','BACK在USE之前分发；空回调无动作。')],
 [pa('controls','§3–§5','先淡出再淡入、无BACK退出、末页0.4秒。')],
 ['普通换页','换页期间重复USE','末页退出','BACK无响应'],
 '入口级supported_static；未证明默认Demo可达。',not_checked='实际调用者/默认地图事件可达性未定位；完整宿主物理绑定未审。')
cap(19,'队伍Box Link桥与旧持物快照的连续写入',
 [sa('party','746–800;1204–1218;1432–1484','三门允许桥；移位保留旧物品，回来不重读。'),sa('storage','1500–1569;1902–1934','盒队伍面板可取回，先入袋再清持物。')],
 [pa('66a','§2、§4.4.1 U05-MV01–03','重复计数与取消保留前序写入。'),pa('66b','§4.2 L107','反向消费者完整承接。')],
 ['A持POTION/袋0取回再给B→袋1/A空/B持物','取回后BACK','不嵌套正常移动'],
 'GR3-M10-001当前仍supported_static；未以旧PASS替代本次源/消费者读取。',history=['GR3-M10-001'])
cap(20,'摘要五页/蛋页、备忘录坐标与可修改子流程边界',
 [sa('summary','117–215;481–638','主图中心(104,206)、备忘录绘制区域(232,86)/宽268；蛋与普通页面字段/个性决胜。'),sa('metrics','71–86','战斗/孵化指标的双倍偏移属于其他消费路径，不能给摘要擅加。'),sa('pkmsprite','23–77','通用显示设置位图与锚点，不应用战斗指标偏移。')],
 [pa('66a','§5.1–5.3、§6','页面内容、首发/返回索引与具名写入。')],
 ['蛋阈值四档','Shadow心阶段>3隐藏性格/个性','IV并列个人ID循环决胜','长获得地点文本'],
 '页面/字段样本有支持；固定布局、长文本与屏幕变体不完整，长词边界另列finding。','partial',['GR4-M10-003'],not_checked='摘要全部招式/缎带/标记导航、零招式已知异常和所有图鉴号分支仅盘点未全面重审。')
cap(21,'储存整理：暂持退出门、道具与取消不回滚',
 [sa('storage','1500–1569;1902–1934','暂持不能退出；无暂持按两类确认；物品添加成功才清持物。')],
 [pa('66b','§3.2、§4.1–4.4','暂持与先前写入保留，Item和各退出反馈。')],
 ['暂持+BACK/Close','无暂持Continue/Exit两问','取回满包拒绝','取回后退回队伍不回滚'],
 '所选正常/拒绝/取消入口supported_static；储存位置所有负值、移动/释放全域未重审。')
cap(22,'背包排序取消与选择器恢复浏览状态',
 [sa('bag','337–452;591–600','拖动立即写顺序和保存索引；BACK回顺序但不回保存索引；借用选择器正常返回恢复旧浏览状态。')],
 [pa('66c','§2–§3.3','正常/过滤模式和排序三种状态分列。')],
 ['0拖2再BACK→顺序/当前0但保存2','自动排序口袋禁手排','过滤选择模式','借用选择正常返回恢复'],
 '该有界状态链supported_static；不承诺异常路径恢复。')
cap(23,'共享物品数量与钱/BP商店的同轮顺序',
 [sa('itemstorage','276–338','BACK/USE先于方向。'),sa('mart','477–539','左右上下先于USE/BACK。'),sa('bp','332–394','与钱店同顺序。')],
 [pa('66c','§5.1 U05-QN01–04','三入口顺序及方向钳位仍耗轮。'),pa(UI_TEST,'U05-QN01–04','四组独立静态设计。')],
 ['USE+BACK=0/1/1','RIGHT+USE=立即1/11等待/11等待','极限方向不变仍压过操作'],
 'GR3-M10-002原范围supported_static；本轮另发现的逐位数字不属于此表。',history=['GR3-M10-002'])
cap(24,'PC物品存取丢弃的画面与执行时点',
 [sa('bag','604–704','存取先预检容量再删除/添加，丢弃确认后删除；存入复用可排序的正常包。'),sa('pc','4–53','空储存不进入取出/丢弃。')],
 [pa('66c','§5','界面入口、数量门、预检/失败、连续操作。')],
 ['空储存','重要物品整叠存取','数量取消0','预检失败无转移','丢弃无目标容量预检'],
 'UI触发时点supported_static；底层容量算法归M05，本轮未重新证明。',owner='M10',projection={'shared_domain':'M05','boundary':'仅UI调用与正常/失败消息顺序'})
cap(25,'战斗命令、队伍与背包的返回/隐藏恢复',
 [sa('commands','6–190;196–324','Run/Cancel/Call入口；队伍子菜单取消与整屏取消权限分层；战斗背包独立游标保存/恢复。')],
 [pa('67a','§3.3、§5、§6.1','命令模式、目标取消回包、正常出口恢复世界背包游标。')],
 ['首行动BACK无效','不可取消选人但可退成员子菜单','类型4目标取消重显包','正常离开保存战斗游标并恢复外部游标'],
 '所列UI生命周期supported_static；未把注册/消耗/退款全业务等价纳入通过。',not_checked='全部命令撤销/退款路径、每个物品handler和全部目标布局未穷尽。')
cap(26,'战斗消息快进与确认列表仅恢复',
 [sa('scene','184–307','普通/暂停skipAhead；确认列表busy只resume；全显后才返回。'),sa('text','368–418','恢复与立即推进的差别。')],
 [pa('67a','§9.1 L223–227','当前已按消费者区分。'),pa(UI_TEST,'U05-TX01–04','正常、暂停、不可取消、全显对照。')],
 ['正字速busy非暂停USE不改字数','中间暂停只解除','普通消息快进','全显Yes初选与BACKNo'],
 'GR3-M10-003原验收继续supported_static；不冒充真实键盘/时间实验。',history=['GR3-M10-003'])
cap(27,'招式动画查找的类型默认数据与回退',
 [sa('play','412–485;492–518','精确侧映射、18类型六格默认身份、TACKLE与静默失败。'),sa('move','22–55;79–96','动画分格消费登记category，不调用世代物理/特殊查询。'),sa('miscdat','39–53','动画集合及映射为不同加载缓存。')],
 [pa('67a','§9.4 L251–254','引用类型默认表但不提供其内容。'),pa('74','§15 L398','再次前向引用，仍无表。')],
 ['FLAMETHROWER无精确→EMBER','EMBER无映射→SUNNYDAY→TACKLE','对方默认候选优先OppMove','精确命中hitNum与默认分支不混'],
 '选择骨架supported_static，兼容映射数据缺失使默认呈现不能唯一确定。','partial',['GR4-M10-004'])
cap(28,'球的条带、开闭、颜色与两份粒子参数表',
 [sa('baseanim','71–244;259–794','16球种burst/capture数据、默认POKEBALL参数、Master/Dusk/Net/Premier/Nest/Dive/Cherish特例；条带宽高判断与回收阶段。')],
 [pa('67a','§8.1、§9.3–9.4','投球/吸收/摇动/爆出骨架；逐帧坐标/轨迹未转录。')],
 ['未知粒子参数身份回POKEBALL但球图片路径仍按原球ID','条带与单帧','MASTER捕获半径192 vs通常144','NET额外网/CHERISH色序','回收5粒子与捕获9组不同'],
 '源端表与消费者已读；正式只承诺演出骨架，精确粒子数据未覆盖。此明示精细呈现边界不当作已完整支持，也不要求复制演出实现。','partial',not_checked='所有随机角/每个tone/缩放轨迹的数值重建和像素效果未穷尽；没有读取实际球素材。')
cap(29,'动画开关、并行完成、20fps播放器与正常恢复',
 [sa('play','93–170;331–405;521–578','派出错峰同推，各框等各球；投球阻塞；公共球动画入队；位置/影子正常返回恢复。'),sa('player','675–843','按运行时间20fps选帧，目标焦点和结束判据。'),sa('battle','pbAnimation/pbCommonAnimation L838–843','领域包装受showAnims门。')],
 [pa('67a','§9.3–9.4、K35/K50','开关不跳硬编码派出收回；公共/招式动画门及并行等待。')],
 ['Effects Off硬编码派出保留','双派出各自完成','播放正常恢复影子/位置','加载或播放抛错无本地ensure'],
 '所列时序supported_static；逐帧timing的跳帧副作用及编辑器全部格式不在本次通过范围。')
cap(30,'Arena首次提示与3/4/5连续裁判UI',
 [sa('arena','43–94;111–200','开场复位；普通补位不调用孤立复位；count>=3逐轮判并沿提示标志。')],
 [pa('67a','§10 L263–267','对阵窗只首开，后续4/5连续判。'),pa('56','§3.3 L108–110、§4 L122','领域与UI一致。'),pa(UI_TEST,'K40、U05-AR01–02','旧局部与新增完整连续场景一致。')],
 ['首次1/2不判3首判','补位保计数/基线/提示','第4/5无新提示且判决'],
 'GR3-M10-004保持supported_static；未重审整套设施资格、命中/AI/录像。',history=['GR3-M10-004'],projection={'shared_domain':'M09','boundary':'Arena UI消费投影；原评分领域资格不扩签'})
cap(31,'进化动画末轮取消与成功提交次序',
 [sa('evolve','52–134;195–275','最后动画更新后先BACK再检查结束；成功消息/叫声先于物种写入；无待学的图鉴页可能提前收尾。')],
 [pa('67b','§3.1–3.3','可取消权限、末轮竞争、轮廓、提交及条件页重复释放边界。')],
 ['最后一轮BACK可取消','不可取消入口同轮成功','进化消息先于物种写','待学非空不提前收尾'],
 '所选演出/提交边界supported_static；未来是否修复参考异常未代决。')
cap(32,'孵化/交换演出、命名与外层替换',
 [sa('hatch','52–139;192–246','孵化前序提交、演出恒true、图鉴后命名；命名分支免重复淡出。'),sa('trade','157–243','卡片等50单位可提前推进；交换不可取消；进化完成后外层换队伍槽。')],
 [pa('67b','§4–§5','直接孵化与仅演出、纯消息回退不可达、前置取消与演出推进分开。')],
 ['仅演出不写孵化前序','空昵称提交','卡片BACK推进非撤交换','交换条件图鉴页多处收尾风险'],
 '所选生命周期supported_static；默认真实Demo调用、可播放裂纹图和重复释放宿主结果未证。')
cap(33,'名人堂与片尾正常结束/跳过/音频恢复',
 [sa('hof','67–92;120–130;178–209;320–341;403–445','先存记录再演出；0容量空历史后PC取空失败；浏览跨届。'),sa('credits','179–233','已播才USE跳过；收尾标记和BGM恢复在正常末尾。')],
 [pa('67b','§7–§8','记录与落盘分离、0容量分支、首次片尾不可跳过、正常恢复。')],
 ['0容量空历史与已有历史','无取消登记演出','首次/再次片尾','音频恢复不是回滚保证'],
 '所选合同supported_static；局部8帧称谓依WP16统一为8个1/20秒单位，不据此另造宿主8帧保证。')
cap(34,'战前包装的选择、预置清理与音画恢复',
 [sa('intro','17–188;198–267;423–432','优先级选择、地点日夜默认表、各资格资源、临时数据、正常结束恢复/清理。'),sa('cfg','559–641','普通淡出ensure与带音乐包装的正常恢复不是同一保证。')],
 [pa('pre','§1–§7','选择表/包装/正常返回边界。'),pa('15','§6','音频位置与登记。')],
 ['野生昼/夜水域','类别0不误作训练家','同优先级不补稳定性','共享图失败不落默认','战斗执行体异常不保证复原'],
 '所列包装supported_static；alternate自编排仅盘点，完整阶段图案未深查。')
cap(35,'图鉴Area与其他城镇地图消费者的交界投影',
 [sa('dexentry','313–351','可见点取并集，正宽按ceil高度消费已有非零格，隐藏/区域门分别检查。')],
 [pa('66b','§7.1 L200','转引WP62并保留10000/11111/同格第二可见点例。')],
 ['10000与11111','第二Point可见','缺尾格不补'],
 'M10本地消费投影supported_static；不代签M11全部遭遇版本与城镇名/飞行规则。',owner='M11',projection={'module':'M10','boundary':'Area显示消费'},history=['GR3-M11-001：U05共享投影，非本域主责回归'])
cap(36,'资源/宿主与可读未审边界',
 [sa('metrics','17–86','坐标/影子指标可读；只读了三个PBS样本。')],
 [pa(F+'scope-statement.md','当前范围及§限制','运行/字体/素材/地图/动态插件限制。')],
 ['图像/音频目录缺失','字体8文件存在','pokemon_metrics三个样本','无地图/完整Demo'],
 '材料可得性沿共享baseline；未运行、不把来源存在当作支持。','unresolved',not_checked='真实宿主、全部PBS/翻译、渲染像素、完整Demo与动态插件组合。')

# Source-reading index: ranges are the semantic material actually inspected, not whole-file approval.
READ = {
 'msg':'56–255;290–859', 'text':'1–185;260–430;620–734;855–928',
 'draw':'1–125;128–243;345–710;926–1043',
 'cfg':'1–210;390–659', 'window':'1–90;317–417;800–925', 'cache':'1–144',
 'bitmap':'1–228', 'files':'1–135', 'speciesfiles':'1–158', 'metrics':'1–101',
 'move':'1–127', 'target':'1–143', 'gamedata':'80–129', 'miscdat':'27–68', 'pkmsprite':'1–97',
 'audio':'1–278', 'system':'1–255', 'trans':'1–1929 (完整具体效果)', 'eventscene':'1–192',
 'intro':'1–278;423–432', 'title':'1–129', 'controls':'1–83', 'hatch':'52–139;192–246',
 'evolve':'52–276', 'trade':'157–243', 'hof':'48–96;120–134;178–215;310–342;403–452',
 'credits':'109–233', 'load':'84–177;248–356', 'pause':'1–170;210–321', 'pc':'1–120;116–237',
 'options':'327–362;384–447;490–540', 'card':'1–111', 'ready':'223–331',
 'party':'685–800;1180–1222;1416–1504', 'summary':'117–215;481–641',
 'storage':'1490–1569;1890–1938', 'bag':'145–164;337–452;591–704',
 'itemstorage':'276–340', 'mart':'477–539', 'bp':'332–394', 'dexentry':'303–357',
 'scene':'180–307', 'commands':'1–392', 'play':'90–172;293–579',
 'baseanim':'1–244;259–794', 'player':'1–148;207–275;675–843', 'arena':'1–212',
 'interpreter':'325–337', 'battle':'838–843 (全文检索定位及定义读取)',
}

def build_inventory():
    # Inventory all scripts, then retain full domain families and named dependency consumers.
    all_files = subprocess.check_output(['rg','--files',str(REF)],text=True).splitlines()
    families = ['Data/Scripts/007_Objects and windows/','Data/Scripts/008_Audio/',
      'Data/Scripts/009_Scenes/','Data/Scripts/016_UI/','Data/Scripts/005_Sprites/',
      'Data/Scripts/011_Battle/004_Scene/']
    consumer_pattern=r'MessageConfig|pbResolveBitmap|AnimatedBitmap|RPG::Cache|Graphics\.transition|pbFadeOutIn|pbShowCommands|pbMessageChooseNumber|pbChooseNumber'
    consumer_files=subprocess.check_output(['rg','-l',consumer_pattern,str(REF/'Data/Scripts')],text=True).splitlines()
    consumers={str(Path(p).relative_to(REF)) for p in consumer_files}
    rows=[]
    direct={S[k]:v for k,v in READ.items()}
    deps=['Data/Scripts/001_Settings.rb','Data/Scripts/002_BattleSettings.rb',
      'Data/Scripts/001_Technical/001_MKXP_Compatibility.rb',
      'Data/Scripts/001_Technical/004_Input.rb',
      'Data/Scripts/001_Technical/002_Files/002_FileMixins.rb',
      'Data/Scripts/001_Technical/006_RPG_Sprite.rb',
      'Data/Scripts/003_Game processing/002_Scene_Map.rb',
      'Data/Scripts/004_Game classes/001_Game_Screen.rb',
      'Data/Scripts/004_Game classes/003_Game_Picture.rb',
      'Data/Scripts/013_Items/007_Item_Sprites.rb',
      'Data/Scripts/014_Pokemon/001_Pokemon-related/003_Pokemon_Sprites.rb',
      'Data/Scripts/015_Trainers and player/003_Trainer_Sprites.rb',
      'Data/Scripts/019_Utilities/003_Utilities_BattleAudio.rb',
      'Data/Scripts/012_Overworld/001_Overworld visuals/003_Overworld_MapTransitionAnims.rb']
    for full in sorted(all_files):
        rel=str(Path(full).relative_to(REF))
        family=any(rel.startswith(x) for x in families)
        context=rel in direct or rel in deps or rel in consumers or 'Animation editor/' in rel
        data=(rel.startswith('Fonts/') or rel.startswith('Text_english_core/') or
              rel in ['PBS/pokemon_metrics.txt','PBS/moves.txt','PBS/items.txt','PBS/types.txt','PBS/trainertypes.txt',
                      'PBS/metadata.txt','PBS/map_metadata.txt','PBS/trainer_types.txt','mkxp.json','Data/Scripts.rxdata','Data/messages_core.dat',
                      'knownpoint.bmp','selpoint.bmp'])
        if not (family or context or data):continue
        group='script' if rel.startswith('Data/Scripts/') else 'font' if rel.startswith('Fonts/') else 'translation' if rel.startswith('Text_english_core/') else 'data_or_host_material'
        state='read_semantically' if rel in direct else 'inventoried_only'
        detail=direct.get(rel,'路径/定义/相关调用检索盘点；本轮未逐分支语义审查。')
        if rel=='PBS/moves.txt':state='read_semantically';detail='FLAMETHROWER2603–2613;FIREPUNCH2680–2690;EMBER2782–2792;SUNNYDAY2819–2827;TACKLE5326–5336。其余未审。'
        if rel=='PBS/pokemon_metrics.txt':state='read_semantically';detail='BULBASAUR3–7;CHARIZARD33–37;PIKACHU147–151。全表其余未审。'
        if rel in ['Data/Scripts.rxdata','Data/messages_core.dat','knownpoint.bmp','selpoint.bmp','mkxp.json'] or group in ['font','translation']:
            state='not_reviewed';detail='沿共享readiness确认材料存在；未解析/运行/语义审核内容。'
        if rel in ['Data/Scripts/001_Settings.rb','Data/Scripts/002_BattleSettings.rb']:
            state='read_semantically';detail='MECHANICS_GENERATION、SUPER_SHINY、MOVE_CATEGORY_PER_MOVE、NEW_CAPTURE_CAN_REPLACE_PARTY_MEMBER检索命中；未全文件审查。'
        rows.append({'path':rel,'commit':R,'group':group,'review_depth':state,'read_scope':detail,
            'resource_or_ui_consumer_search_hit':rel in consumers,
            'material_availability':'PRESENT_SHARED_BASELINE','not_checked':'read_scope之外全部内容与真实运行。'})
    return {'schema_version':'1.0','reviewer':REVIEWER,'reference_root':str(REF),'reference_commit':R,
       'discovery_method':['rg --files参考全目录','核心UI/窗口/音频/场景/精灵/战斗Scene全族路径盘点',
                           '相关caller/override/handler全文检索','PBS/翻译/字体和宿主边界独立盘点'],
       'counts':dict(Counter(x['review_depth'] for x in rows)),
       'consumer_discovery':{'pattern':consumer_pattern,'matching_files':len(consumers),'scope':'全部312散脚本'},
       'qualification':'相关来源候选盘点，不是完整全游戏能力分母；read_semantically仅代表所列范围，非全文件通过。',
       'missing_materials':['Graphics/','Audio/','地图与完整Demo','可用游戏宿主'], 'files':rows}

dump('capabilities.json',caps)
dump('source-scope.json',build_inventory())

findings=[]
def finding(n,title,severity,category,src,spec,expected,current,gap,pre,minimal,normal,boundary,impact,
            searches,change,criteria,files,capids,shared=(),history=None,unknowns=None,excluded=None):
    fid=f'GR4-M10-{n:03d}'
    findings.append({'id':fid,'title':title,'module':'M10','severity':severity,
      'disposition':'REQUIRED','status':'missing','reviewer':REVIEWER,'category':category,
      'classification':['User Interface','Engine / Overworld Integration'],
      'source_baseline':{'commit':R,'tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','root':str(REF)},
      'source_anchors':src,
      'specification_baseline':{'commit':B,'tree':'d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a',
         'formal_set':'deliverables/final-specification-set/','identity_navigation':'delivery/2026-10-12/formal-identities.json'},
      'spec_anchors':spec,'expected_reference_behavior':expected,'current_spec_behavior':current,'gap':gap,
      'preconditions':pre,'minimal_counterexample':minimal,'normal_case':normal,'failure_or_boundary_case':boundary,
      'impact_on_independent_implementation':impact,'negative_evidence_search':searches,
      'proposed_spec_change':change,'acceptance_criteria':criteria,'affected_files':files,
      'shared_contracts':list(shared),'dependencies':['WP17通用UI','WP15资源访问','宿主输入/字体或媒体接口的条件前提'],
      'related_capabilities':[f'GR4-CAP-M10-{x:03d}' for x in capids], 'related_findings':[],
      'root_cause_group':{'id':fid+'-ROOT','description':gap},
      'history_links':history or {'relation':'new','third_round':None,'second_round':None,'note':'不猜第二轮ID，不据旧PASS判定本轮支持。'},
      'evidence_level':['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR'],'execution_status':'NOT_EXECUTED',
      'confidence':'HIGH_STATIC',
      'unknowns':unknowns or ['真实宿主/媒体/输入未运行；未推断完整Demo可达。'],
      'excluded_claims':excluded or ['不要求采用源类/方法/容器组织。','不修改参考或决定未来产品必须保留该兼容细节。'],
      'user_decision_needed':False,
      'review_resolution':'本审者完成源端与全131正式集反证后保留；待主汇总者安排一次独立针对性反证/去重。'})

finding(1,'通用命令选择与逐位数字输入的同轮优先序仍缺少合同','P2','状态或时序错误',
 [sa('msg','166–205;721–801','数字先组件更新，再USE/elif BACK；普通及帮助命令先BACK，取消无效时仍可USE。'),
  sa('text','687–729;862–923','数字/列表方向处理均在确认出口之前，故可同轮改值/改索引并返回。'),
  sa('interpreter','325–334','事件数字输入调用同一逐位数字入口，结果写变量。'),
  sa('pc','4–16;116–153','正常PC菜单消费者使用普通/帮助命令入口。')],
 [pa('17','§4 L92–99、§5.2–5.3 L114–121、§7.2','仅定义单键结果和更新机会，没有各入口竞争结果。'),
  pa('66c','§5.1 L88–108','旧同轮表明确是共享物品数量/两商店。'),
  pa(UI_TEST,'MG12–MG20、B04-M07–09、U05-QN01–04','分别覆盖单键、光标命名、物品数量，不覆盖普通命令和逐位数字竞争。')],
 '命令/带帮助命令：允许取消时同轮BACK+USE返回取消编码；取消项0时BACK无效但本轮USE仍返回当前索引。逐位数字：先编辑方向再USE；合法值当轮确认，USE与BACK同时成立仍确认；越界USE只蜂鸣继续，BACK不被处理。',
 '命令与数字各有确认/取消条款，但未给竞争裁决。已有明确同轮表的“共享数量”是按件数增减窗口，不能泛用于逐位数字；命名的优先序同样是另一入口。',
 '缺少两个实际默认消费者的同轮返回/继续判据；从单键规则无法唯一推出确认还是取消，以及方向能否与确认同轮发生。',
 ['无插件，窗口已正常进入循环；列出的输入查询同采样轮为真，其余假。',
  '命令为两项、默认索引0；取消项分别2与0。数字范围[0,9]、初值1、显式取消值−1。',
  '方向值由正常组件更新产生；数字越界对照采用范围[3,3]初值3同轮UP。'],
 {'input':'普通命令取消项2/索引0，USE+BACK；独立数字范围[0,9]/当前1/取消−1，USE+BACK。',
  'reference_output':'前者返回1；后者返回1作为确认，绝非取消−1。',
  'distinguishing_alternative':'全局“取消优先”会使数字返回−1；全局“确认优先”会使命令返回0。'},
 '两项命令单独USE返回0、单独BACK在取消项2时返回1；数字单独USE返回1、单独BACK返回−1。',
 ['数字当前1，UP+USE→先变2再立即返回2；它不遵守物品数量一轮只执行首个动作。',
  '数字范围[3,3]初值3，UP+USE+BACK→先变4，确认越界蜂鸣，留循环；同轮BACK不会救出。',
  '命令取消项0，USE+BACK→BACK无效后仍返回当前索引0；带帮助入口相同。'],
 '独立实现若采用统一按钮裁决会产生不同的选择/事件变量值，或在参考仍等待的越界场景提前取消。',
 {'artifact':'negative-searches.json','search_ids':['selector_competition','selector_priority_exact'],
  'scope':'全部131正式文件','relevant_contexts_read':[P['17']+' §4/5/6.2.1/7.2',P['66c']+' §5.1',UI_TEST+' MG/B04-M/U05-QN',P['65']+' §7'],
  'result':'确认已存在的光标命名与物品数量竞争规则均不同入口；未找到普通命令/帮助命令或逐位数字的上述裁决。其它命中为录像/转换的同轮概念，不能承接此行为。'},
 '在WP17按入口增加一个简短竞争表：命令的可取消/不可取消分流；数字先编辑再确认、USE优先及越界仍压过BACK。给定静态查询前提，不规定输入调度实现。',
 [{'kind':'SPEC_STATIC','criterion':'仅凭正式集可唯一推出上述命令2/0与数字合法/越界四分支。'},
  {'kind':'DERIVED_VECTOR','criterion':'增加单键对照、UP+USE与越界UP+USE+BACK案例，标NOT_EXECUTED。'},
  {'kind':'SPEC_STATIC','criterion':'保留U05物品数量/商店与光标命名合同，不把其顺序统一化。'},
  {'kind':'EXECUTED_HOST_OR_DEMO','criterion':'如未来声称物理键可达/真实UI通过，须另供宿主证据；本修订不要求先运行。'}],
 [P['17'],UI_TEST],[2],shared=['WP65 PC命令','WP13事件数字输入','WP66-C数量窗口分界'],
 history={'relation':'new_scope_same_root','third_round':'GR3-M10-002','second_round':None,
          'note':'GR3-M10-002对物品数量/钱店/BP的修订仍满足，当前新增普通命令与逐位数字入口，非旧项未解决或回归。'})

finding(2,'默认皮肤冷读取的回退链与显式设置空结果未进入资源合同','P3','数据或资源契约缺口',
 [sa('cfg','35–85','冷读取先选项皮肤，后系统名、System/Window、001-Blue01；显式设置只解析一次并保留空结果。'),
  sa('window','818–868','窗口默认皮肤消费缓存；显式setSkin解析失败提前返回，不自动使用默认链。'),
  sa('msg','380–394;444–450','普通消息采用speech默认；空w标签直接清windowskin，属不同操作。'),
  sa('options','492–519','选项值先写再显式设置皮肤缓存及预览。')],
 [pa('17','§3.1 L35、§3.4 L86–87、§7.3 L229','提供空w清皮肤与按选项选肤；资源缺失转引WP15。'),
  pa('15','§3.1、§5.1、§7','有通用图像解析/包装失败，没有窗口默认候选链。'),
  pa('65','§5.2 L123–124','Speech/Menu Frame正常预览，但缺专属回退条件。'),
  pa('02','配置目录 SPEECH_WINDOWSKINS/MENU_WINDOWSKINS','仅表数量/角色，不提供回退选择。')],
 '未初始化的菜单/消息皮肤分别先解析选项指向的资源；未命中才解析系统登记名，再通用System/Window，再Windowskins/001-Blue01，最终为空。显式设置解析失败后记录空值，后续读取把它当已设置结果，不重新走冷读取回退。',
 '正式集从选项皮肤直接转引通用解析失败规则；未给这一专用搜索链，也未区分“尚未求默认”与“明确设置为空”。',
 '缺少可以独立决定备用皮肤身份的资源选择规则；即便准备相同可用素材，也无法由正式集确定结果。',
 ['皮肤配置索引在范围内；初取的缓存未初始化；无插件。',
  '所选皮肤缺失，系统登记名Custom有效，Custom与两个通用候选均可解析；图像加载正常。',
  '显式设置对照独立开始，输入一个无法解析的皮肤名，后续只检查逻辑解析结果；不承诺已释放图像的实际画面。'],
 {'input':'初取消息皮肤：选项资源Missing不存在、系统windowskin名Custom存在、System/Window和001-Blue01也存在。',
  'reference_output':'选择Custom；不返回nil，也不直接采用通用Window。',
  'distinguishing_alternative':'正式仅有通用“解析未命中nil”不足以确定这一身份选择。'},
 '所选皮肤能解析时直接使用，不尝试系统/通用备用。',
 ['系统名也不存在→System/Window；再缺→001-Blue01；全缺→空逻辑皮肤。',
  '相同备用资源存在，显式设置Missing后读取仍为空；不再冷回退Custom。',
  '消息中的空w标签直接清除皮肤，不应与显式设置不存在名称等同。'],
 '默认UI在缺少一个皮肤资源时可能错误地选空白或选错备用；设置项的后续读取也可能错误恢复默认。',
 {'artifact':'negative-searches.json','search_ids':['font_skin','skin_fallback_exact'],
  'scope':'全部131正式文件','relevant_contexts_read':[P['17']+' §3.1/3.4/7.3',P['15']+' §3/5/7',P['65']+' §5.2',P['02']+' 配置表',F+'demo-dx/wp73-a-content-editors.md §失败边界'],
  'result':'字体Arial、形态皮肤、编辑器Windowskins目录异常、w空标签及普通资源解析均不是本回退链；未见001-Blue01/System/Window或冷取与显式设置分层合同。'},
 '补默认菜单/消息皮肤候选优先级、每步存在性门、最终空结果与显式设置的区别；限定逻辑结果，不补造缺图后的像素恢复或新类结构。',
 [{'kind':'SPEC_STATIC','criterion':'给出选项命中、系统命中、两个通用备用依次命中及全缺的结果。'},
  {'kind':'DERIVED_VECTOR','criterion':'相同素材条件下，冷读取Missing得到Custom而显式设置Missing后读取为空，标未执行。'},
  {'kind':'SPEC_STATIC','criterion':'空w标签保持原直接清空合同；不把逻辑空值等于所有既有窗口统一无皮肤。'}],
 [P['17'],P['15'],UI_TEST],[4,15],shared=['WP02皮肤列表','WP65皮肤预览'],
 unknowns=['所有皮肤图像缺失；无真实窗口验证。','显式换肤失败时先释放旧定制资源后的具体宿主画面未验证，未据此声称保持原画面或崩溃。'])

finding(3,'长无空格文本的超宽不逐字折行边界未被规格承接','P2','实现信息不足',
 [sa('draw','128–205;611–658;1035–1040','两格式化路径都需要非行首词边界才把整词移至下一行；无空格行首长串不会按字符拆行。'),
  sa('text','316–347','普通消息将内容宽度传给格式化，依据生成的换行插暂停。'),
  sa('summary','519–537;560–587;637','获得文本/地名进入宽268的格式化备忘录，源端不是专用长词换行器。')],
 [pa('tags','§3、§6 L93','只描述显式对齐/换行，完整排版改为以绘制函数为准。'),
  pa('17','§3.3 L82','自动行满暂停示例含显式换行，未给自动宽度换行规则。'),
  pa('66a','§5.2 L143–160','列长文本消费者字段，未给超宽词结果。')],
 '在正常测量下，行首的一段连续非空白文本即使超过请求行宽，仍在同一逻辑行产生绘制项；不会按字符硬折行。有此前词边界的下一词超宽时可整词移到下一行；显式换行仍生效。这同时存在于无标记快路径和带格式标记的一般路径。',
 '正式给出标签、行数/行满暂停和摘要字段；排版正文把完整换行算法留在参考绘制函数，没有实现无关的长词边界或案例。',
 '文本可见行为依赖未移交的分词/折行条件，独立实现无法区分自动逐字折行与保持超宽单行。',
 ['有效位图/字体测量接口；默认允许自动折行；高度不限制行；无插件和图像/等待控制符。',
  '静态测量夹具：A/B各宽8、空格宽4，请求行宽12；不声称真实Power Green有这些度量。',
  '比较直接AB与A B；再以已识别无动作pg标签使同一文字走一般路径。'],
 {'input':'行宽12、测量A=B=8，文本AB；独立对照A B（空格4）。',
  'reference_output':'AB仍只有一个文字行，B横向起点8；A B把B移至下一文字行。带pg标记仍有同样行归属差异。',
  'distinguishing_alternative':'常规逐字折行会把AB中的B移到下一行，改变消息后续行满暂停位置与摘要布局。'},
 '短文字在宽内保持一行；显式A换行B形成两行。',
 ['长无空格词/连续无空白本地化文本不硬拆行；只承诺生成的布局请求，不宣称屏外字形最终如何裁切。',
  '有词边界的A B可整词移行；不能据此泛化任何长词都能装入宽度。',
  '摘要备忘录固定宽度输入不增加额外滚动或长词策略；最终像素仍依赖字体和宿主。'],
 '语言较长或无空格的文本可能产生不同的可见行数、被遮挡内容和暂停时点；仅凭现集需重新读源才能保持参考行为。',
 {'artifact':'negative-searches.json','search_ids':['summary_particles','long_text_wrap'],
  'scope':'全部131正式文件','relevant_contexts_read':[P['tags']+' §3/6',P['17']+' §3.3/6.3',P['66a']+' §5.2',UI_TEST+' DT04/B04-M14',F+'generic-kernel/wp08-localization.md 非目标'],
  'result':'命中的是显式换行、命令文本转换或编辑长度限制；DT04是对齐触发换行，B04-M14依赖显式换行。未见无空白长词/自动折行边界；§6明确留空不等于有可用净室合同。'},
 '补一个最小行为规则与两条测量夹具：基于词边界的自动折行、行首超宽连续串不硬拆、显式换行优先；说明消息/摘要消费，保留最终像素与未来改善策略自由。无需复写排版函数。',
 [{'kind':'SPEC_STATIC','criterion':'说明无空白长串与含词边界文本的不同结果，不以参考函数名代替规则。'},
  {'kind':'DERIVED_VECTOR','criterion':'AB、A B、显式换行、带pg四组独立夹具给行归属；注明测量是假定输入、未运行字体。'},
  {'kind':'SPEC_STATIC','criterion':'不会把消息行满暂停/摘要坐标说明扩成保证所有长文本可见，也不要求逐像素复刻。'}],
 [P['17'],P['tags'],P['66a'],UI_TEST],[6,20],shared=['WP08本地化后的文本消费','消息行满暂停','摘要备忘录'],
 excluded=['不要求全字符排版算法逐行翻译。','不声称默认中文文本、所有长字符串都会实际丢字；字体测量和宿主裁切未运行。','不把固定摘要坐标要求成未来框架布局架构。'])

finding(4,'战斗动画的类型默认映射只有表名和查找顺序，缺少可消费数据','P2','数据或资源契约缺口',
 [sa('play','412–485','18类型×6槽明确指定默认招式身份，未映射按本格/对应单目标/变化/TACKLE回退。'),
  sa('play','492–518','普通动画调用真实消费查找结果；有动画才进入播放。'),
  sa('battle','838–843','正常战斗域包装在showAnims为真调用场景播放。'),
  sa('move','22–55;79–96','登记type/category/target决定分格；raw category与世代physical?/special?不同入口。'),
  sa('target','26–33;136–141','NearOther目标数1；目标数量/敌侧属性参与分格。'),
  sa('miscdat','39–53','映射与数据库加载分层，可用缓存为条件。'),
  sa('PBS/moves.txt','FLAMETHROWER2603–2613;EMBER2782–2792;SUNNYDAY2819–2827;TACKLE5326–5336','默认数据支持火系特殊单目标样本及回退身份存在。')],
 [pa('67a','§9.4 L251–254','称类型默认表并定义六槽/回退骨架，没有表内容。'),
  pa('74','§15 L396–399','关联编译与播放侧再次引用同一缺表。'),
  pa(UI_TEST,'BT K36','只给全部缺失的结果，无法确定正常默认命中的身份。'),
  pa('03','§非注册表产物 L67','move2anim产物身份不能替代脚本内的类型默认映射。')],
 '例：FLAMETHROWER无精确映射时按其火系特殊单目标格选择EMBER映射；EMBER亦无映射时再尝试火系变化默认SUNNYDAY，最后TACKLE。各被选默认身份在对方侧也优先OppMove再普通映射。默认表含18类型、每类六槽及空槽。',
 '给出“查类型默认表”和查找链，但全正式集未提供该表的身份数据；WP74只是回指，不能确定火系特殊对应EMBER。',
 '缺少决定最终资源身份的固定默认内容；算法名和六槽结构不能代替数据。',
 ['普通战斗动画开启，无插件，合法FLAMETHROWER/默认type-category-target记录。',
  '已正常得到双方映射与动画集合（条件夹具），FLAMETHROWER无精确映射；EMBER、SUNNYDAY、TACKLE映射指向不同有效动画槽。',
  'hitNum=0；实际媒体存在/内容不用于证明查找结果，未加载二进制动画。'],
 {'input':'己方FLAMETHROWER精确映射空；EMBER→10、SUNNYDAY→20、TACKLE→30；三槽均有效。',
  'reference_output':'选择槽10（EMBER）；删EMBER映射则槽20；再删SUNNYDAY则槽30；全部删才空。',
  'distinguishing_alternative':'只凭当前正式集无法在火系的EMBER、FIREPUNCH或其他默认身份中作出唯一选择。'},
 'FLAMETHROWER精确映射存在时直接使用它；这一骨架已有正文支持。',
 ['对方侧EMBER存在OppMove→11且普通→10时选11；对方项空才选10。',
  '默认身份未登记或该候选无映射时继续；不把资源/数据库存在性与映射选择合并。',
  '世代物理/特殊机制变化不自动重写raw类别的动画分格；无需假定全部世代运行已验证。'],
 '实现者即使拥有相同动画库和招式数据也无法按正式规格选择相同默认动画，作者为新招式省略专用动画时表现不确定。',
 {'artifact':'negative-searches.json','search_ids':['animation_defaults'],
  'scope':'全部131正式文件','relevant_contexts_read':[P['67a']+' §9.4',P['74']+' §15/16',P['03']+' L67',UI_TEST+' K35–36'],
  'result':'语义相关命中只有WP67-A表名/骨架、WP74前向引用、加载产物说明和缺失测试；FIREPUNCH/EMBER等表成对标识搜索无映射表。钓鱼公共事件回退和Safari数据是其他功能。'},
 '以实现无关附表补18类型×六种用途到默认招式身份/空值的映射，说明原始类别/目标分格与候选存在性门；增加正常默认命中和逐级落空对照。不要复制Ruby表表达式或设计播放类。',
 [{'kind':'SPEC_STATIC','criterion':'正式交付包含完整默认类型映射数据及六槽含义，能独立解析身份。'},
  {'kind':'DERIVED_VECTOR','criterion':'火系特殊10→20→30→空及OppMove11优先案例给明确输入/输出且NOT_EXECUTED。'},
  {'kind':'SPEC_STATIC','criterion':'保持精确映射hitNum、默认候选查找、动画数据库/媒体缺失分层；不把结构校验称播放测试。'}],
 [P['67a'],UI_TEST],[27],shared=['WP74动画命名编译','WP03动画产物','战斗showAnims开关'],
 unknowns=['Data/move2anim.dat与PkmnAnimations.rxdata在参考材料中不可用；未反序列化。','本文映射号10/20/30/11是条件静态夹具，不代表默认素材库实际编号。'])

dump('findings.json',{'schema_version':'1.0','findings':findings})

# Fixed U05 evidence is navigation, not a transferred PASS signature.
OLD_REPORT={'commit':'1cb48da29e9363a2947eb16c75461bc3e76ae726',
 'path':'review/remediation-third-20261012-prepare/U05/actual-integration/independent-review/attempt-01/report.md',
 'lines_or_symbol':'五项新的actual判断表：各GR3-M10行；必要上游与限定段'}
OLD_RECEIPT={'commit':'c2eb74c7cbcf8a190d5e902d871fbce44904efd6',
 'path':'review/remediation-third-20261012-prepare/registration/U05-formal-acceptance.json',
 'lines_or_symbol':'accepted_ids / formal_acceptance / accepted_actual'}
reg=[]
for old_id,capno,checks in [
 ('GR3-M10-001',19,['成功盒侧取回与原来源身份/索引未变','MV01袋1/A空/B持物','MV02 BACK保取回','MV03不嵌套总量1','WP66-B反向Item消费者']),
 ('GR3-M10-002',23,['共享/钱店/BP三个入口实际分支顺序','QN01 USE+BACK','QN02 RIGHT+USE','方向钳位仍消费轮','单键返回仍与旧规则相同']),
 ('GR3-M10-003',26,['resume与skipAhead实际定义','busy非暂停正字速计时未满前提','显式暂停仅解除','全显初始Yes/取消No','普通消息1秒与非战末暂停3秒']),
 ('GR3-M10-004',30,['Arena开场与补位调用链','孤立复位辅助无调用检索','提示标志不复位','K40与AR01/02一致','第3→4→5正常补位仍累计并判'])]:
    c=caps[capno-1]
    reg.append({'id':old_id,'module':'M10','reviewer':REVIEWER,
       'current_file_anchors':c['spec_anchors'],'source_anchors':c['source_anchors'],
       'old_acceptance_fixed_references':[OLD_REPORT,OLD_RECEIPT],
       'criteria_and_consumers_actually_checked':checks,'result':'supported',
       'meaning':'supported_static：本次有界复读未发现该已关闭项回归，不是重签全文件/所有旧输入。',
       'limits':['未运行。','原限定关闭与身份不变；其它模块/数学/真实素材/Demo不扩签。'],
       'historical_status_preserved':'CLOSED','evidence_level':['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR'],
       'execution_status':'NOT_EXECUTED'})
dump('regression.json',reg)

# Every primary formal document/appendix/test family has an explicit bounded row.
specrows=[]
def coverage(path,contracts,capnums,status=None,not_checked=None,deps=None):
    linked=[caps[n-1] for n in capnums]
    sources=[]
    for c in linked:
        for a in c['source_anchors']:
            if a not in sources:sources.append(a)
    relevant=[x['id'] for x in findings if path in x['affected_files']]
    specrows.append({'path':path,'commit':B,'contracts_checked':contracts,'source_anchors':sources,
      'status':status or ('partial' if relevant else 'supported'),
      'support_evidence':{'meaning':'supported_static，仅以下样本，不声明全文件通过。',
                          'capabilities':[c['capability_id'] for c in linked],
                          'evidence_level':['SOURCE_STATIC','SPEC_STATIC'],
                          'execution_status':'NOT_EXECUTED'},
      'dependencies':deps or ['WP15/16/17共享呈现资源与输入','领域写入归属各相应模块'],
      'unsupported_assertions':relevant,
      'not_checked':not_checked or ['除contracts_checked之外的段落/附表/静态案例未逐条重证；宿主、媒体与Demo未运行。']})
coverage(P['15'],['§3.1图像/SE解析','§4.1物种图像组合','§5分入口加载失败','§6.1/6.2音频暂停/缩放/记忆'],[7,8,9,4])
coverage(P['16'],['§6.1所有具名转场身份及通用入口单位','§6场景恢复与战前交界'],[10,11,12,13,34],status='partial',not_checked=['地图图层、自动图块容量、动态阴影、灯光、天气、画面图片/计时器全部条款未重审；这些为M03等主责交界。','具体转场的分块/逐像素/轨迹虽源可读，但未视作完整正式覆盖。'])
coverage(P['pre'],['§1/2包装与注册','§3五组资格表（alternate只读资格/盘点）','§5全部固定时间及宿主异常','§6昼夜地点默认表','§7限制'],[10,12,13,34],status='partial',not_checked=['alternate自编排中段完整阶段未深查；五组运行期插件增删未审。','来源Transitions全读不等于实际像素与所有数据条件通过。'])
coverage(P['17'],['§3预处理/四态/行满暂停','§3.4字体/皮肤','§4命令','§5数字','§6.2.1仅用作反证不同消费者','§7正常/异常边界'],[1,2,3,4,6],not_checked=['两种命名字符全表、自由文本编辑/鼠标/全部物理绑定未新审。','字体的系统候选层/图集布局不完整覆盖，未把整体文件判PASS。'])
coverage(P['tags'],['识别正则/实体替换','c与c3阴影','图像尾部消费','长词折行空白处'],[5,6],not_checked=['所有21标签嵌套/不合法参数和完整对齐/字号测量未穷尽。'])
coverage(P['65'],['§3标题/载入的正常菜单与语言写回','§4.3退出忽略保存结果','§5选项即时/结束应用','§6暂停菜单','§7 PC层游标/资格','§8快捷菜单调用与取消'],[14,15,16,4],not_checked=['存档读取/备份递归核心归M02；读取异常未重新审查。','ReadyMenu核心候选与取消读取，完整所有导航和领域场地招未审。'])
coverage(P['card'],['§3–6全主链','女性资源回退/底边/日期/徽章/BACK'],[17])
coverage(P['controls'],['§3–5时序/清回调/末页0.4秒','BACK空回调'],[18])
coverage(P['66a'],['§2 BoxLink','§4.4.1 U05移物','§5页面/备忘录/长文本','§6与§7仅交界盘点'],[19,20,6],not_checked=['全部学习/遗忘/重学、奶招/邮件、缎带排序/标记/多选准入未重证。'])
coverage(P['66b'],['§2–4整理盒子暂持/Item/正常退出','§7.1 Area显示U05投影'],[19,21,35],not_checked=['图鉴排序/搜索全空间、性别/形态展示、盒子负位置/异常容量与释放全链未新审。'])
coverage(P['66c'],['§2–3背包排序/借用恢复','§5存取丢弃/数量','§5.1 U05竞争','§6钱/BP数量入口投影'],[22,23,24],not_checked=['价格、优惠、赠球、有限槽和事务回退业务本轮只盘点，不重签WP29领域。'])
coverage(P['67a'],['§3.3命令模式','§5–6队伍/背包正常取消恢复','§9消息/粒子/播放/查找','§10 Arena','§11世代开关消费'],[25,26,27,28,29,30],not_checked=['所有招式目标/物品handler/成长数值/捕获计算/退款及回放全域未重审。','粒子数值表可读但正式无详细参数承接，未把省略视作全部通过。'])
coverage(P['67b'],['§3进化末轮取消及成功','§4孵化命名与恒true','§5交换等待/替换/多次收尾','§7名人堂0容量/浏览','§8片尾正常结束'],[31,32,33],not_checked=['§6净化室/遗迹石在本轮仅盘点、未重审；仪式UI与领域失败链由M04等主责。','每个生命周期动画所有帧、图鉴页/学招插入的所有组合未穷尽。'])
coverage(UI_TEST,['MG12–20','DT/长文反证','TC/CH','B04-M14','B16排序/空招式/储存相关边界导航','K35/36/40/45/50','U05-MV/QN/TX/AR'],[1,2,4,5,6,17,18,19,23,26,27,30],not_checked=['共享目录的WP63/68/69/70/71案例不属本轮M10主责；其余全部案例没有逐条验证。','所有案例均未执行；设计行存在不计行为通过。'])
coverage(T+'engine-overworld-wp11-15-59-60.md',['WP15 RS/B04-R音频/资源分入口相关设计导航'],[7,8,9],status='partial',not_checked=['本次仅相关向量导航/检索；未全文重审各RS/B04-R行，也未审WP11/59/60其余设计。'])
coverage(T+'engine-overworld-wp16.md',['BT/具名过渡的身份、时长、资源与异常设计导航'],[10,12,13,34],status='partial',not_checked=['相关设计索引/检索有读，未对全目录每条输入/输出独立重新推导；世界渲染WR/B04-W由相应主责。'])
coverage(F+'scope-statement.md',['现正式身份导航与U01/字体/素材/宿主限制','像素/轨迹等排除的解释边界'],[36],status='partial',not_checked=['各历史生成层身份/计数不重审、不重开；不能把旧pending段当新冻结状态。'])
coverage(F+'README.md',['正式131结构与当前导航、历史层/未运行限定检索'],[36],status='partial',not_checked=['导航/身份沿共享baseline；全文历史登记一致性为其它主责，本轮不重签。'])
coverage(P['02'],['窗口皮肤表数量和配置角色','世代8默认与图形相关开关'],[3,4,29],status='partial')
coverage(P['03'],['非注册表动画产物与加载边界，作为类型默认表反证'],[27],status='partial')
coverage(P['74'],['§15动画命名/默认表前向','§16集合缓存存在性与映射分层'],[27,29],status='partial',not_checked=['动画编辑器全部操作、编译/导入导出/二进制格式本轮未重审；只审M10播放消费交界。'])
coverage(P['56'],['§3.3/§4正常补位不复位，与UI一致'],[30],status='partial')
coverage(T+'combat-requirements-wp54-55-56-58.md',['PA-P28由U05/当前UI完整前提逐项对读；其余仅导航'],[30],status='partial',not_checked=['杯赛/Palace/录像全部测试未重审；PA-P28数学及队伍资格未作新全域证明。'])
dump('spec-coverage.json',specrows)

# All concrete transitions, including names not selected by the default battle table.
trans_lines=(REF/S['trans']).read_text().splitlines()
blocks=[]
starts=[(i,s.strip().split()[1]) for i,s in enumerate(trans_lines,1) if re.match(r'  class \w+',s)]
for j,(start,name) in enumerate(starts):
    if name=='Transition_Base':continue
    end=(starts[j+1][0]-1) if j+1<len(starts) else len(trans_lines)
    txt='\n'.join(trans_lines[start-1:end])
    dur=re.search(r'^\s+DURATION\s*=\s*([\d.]+)',txt,re.M)
    resources=sorted(set(re.findall(r'RPG::Cache\.transition\("([^"\n]+)"\)',txt)))
    # Replace source interpolation syntax with domain placeholders, never output code expressions.
    resources=[re.sub(r'#\{[^}]*\[0\]\}', '<opponent-type>',v) for v in resources]
    resources=[re.sub(r'#\{[^}]*\[2\]\}', '<player-portrait-key>',v) for v in resources]
    names=[]
    for s in trans_lines[:100]:
        m=re.search(r'when "([^"]+)".*Transitions::'+re.escape(name)+r'\.new',s)
        if m:names.append(m.group(1))
    blocks.append({'effect_identity':name,'compatibility_names':names,'source_anchor':sa('trans',f'{start}–{end}','本具体效果的初始化、阶段、更新和处置均已阅读。'),
       'fixed_seconds':float(dur.group(1)) if dur else None,'duration_if_not_fixed':'调用方1/20秒单位换算',
       'resource_keys':resources,'status':'partial','support_scope':'身份/类别/时长/资源消费/异常边界的静态阅读；不代表完整像素参数交付。',
       'not_checked':['实际素材与渲染','所有屏幕尺寸/异常图集尺寸/跳时的数值穷举'],
       'spec_anchors':[pa('16','§6.1'),pa('pre','§5、§7')],
       'evidence_level':['SOURCE_STATIC','SPEC_STATIC'],'execution_status':'NOT_EXECUTED'})
dump('transitions-inventory.json',{'schema_version':'1.0','reviewer':REVIEWER,'effects':blocks,
  'concrete_effect_count':len(blocks),'compatibility_name_count':sum(len(x['compatibility_names']) for x in blocks),
  'shared_base':sa('trans','18–173','公共路由/时间/生命周期另核。')})

dump('execution.json',{'actual_executions':[],
 'not_executed':[
   {'kind':'EXECUTED_REFERENCE','reason':'未执行任何参考Ruby、编译器或二进制反序列化。'},
   {'kind':'EXECUTED_MODEL','reason':'未构造或执行行为模型；所有反例为静态推导。'},
   {'kind':'EXECUTED_HOST_OR_DEMO','reason':'Graphics/Audio/地图/完整Demo缺失且游戏宿主未成立。'},
   {'kind':'DERIVED_VECTOR','reason':'所有新向量及旧U05验收均NOT_EXECUTED，证据类型不与执行状态混用。'}],
 'read_only_activity':'rg、nl/sed与git show用于静态阅读/全正式反证搜索，不作为行为执行证据。',
 'model_identity':{'requested_model':'gpt-6-astra','requested_reasoning_effort':'ultra','requested_service_tier':'default','fast':False,'actual_echo':'UNVERIFIED'},
 'reviewer':REVIEWER,'thread_id':'01a12ff1-a1b1-7212-84b3-c3fdcd6552a9','pid':38287,
 'identity_source':'tasks/M10-launch.json','parent_thread_id':'01a12fc2-e8c0-7e43-a721-ccfe659d75c8',
 'separation':'上述parent仅为启动记录；本审者身份始终为M10/真实CLI thread，不使用内部/root代指父身份。'})

print(json.dumps({'capabilities':len(caps),'capability_statuses':dict(Counter(c['status'] for c in caps)),
  'findings':[x['id'] for x in findings],'regressions':len(reg),'formal_files_with_scope_rows':len(specrows),
  'concrete_transitions':len(blocks),'compatibility_names':sum(len(x['compatibility_names']) for x in blocks)},ensure_ascii=False))
