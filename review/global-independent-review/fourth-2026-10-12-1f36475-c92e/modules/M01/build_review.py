from pathlib import Path
import json, subprocess

O=Path(__file__).resolve().parent
B='1f36475d22120a0d1175967d5b17d71fe8311d88'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
P='deliverables/final-specification-set/'
D='Data/Scripts/010_Data/'
C='Data/Scripts/021_Compiler/'
I='Data/Scripts/001_Technical/003_Intl_Messages.rb'
G=D+'001_GameData.rb'
CP=C+'001_Compiler.rb'
CC=C+'002_Compiler_CompilePBS.rb'
CW=C+'003_Compiler_WritePBS.rb'
DATA=D+'002_PBS data/'
W2=P+'generic-kernel/wp02-rule-configuration-and-data-variants.md'
W3=P+'generic-kernel/wp03-content-identity-and-schema.md'
W4=P+'generic-kernel/wp04-pbs-lifecycle.md'
W8=P+'generic-kernel/wp08-localization.md'
T1=P+'test-catalog/generic-kernel-wp02-03-04.md'
T2=P+'test-catalog/generic-kernel-wp05-06-07-08-09-10.md'
W15=P+'engine-overworld/wp15-resource-matching-and-audio.md'
T15=P+'test-catalog/engine-overworld-wp11-15-59-60.md'
WHO='M01 independent reviewer /root; requested gpt-6-astra ultra default; actual model echo UNVERIFIED'

def dump(name,x): (O/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sa(path,locus,fact):return {'path':path,'commit':R,'lines_or_symbol':locus,'fact':fact}
def sp(path,locus,fact):return {'path':path,'commit':B,'lines_or_symbol':locus,'fact':fact}
def cid(n):return 'GR4-CAP-M01-%03d'%n
caps=[]
def cap(n,desc,sources,specs,pre,checks,status='supported',reason='所列合同由 SOURCE_STATIC 与 SPEC_STATIC 一致支持，仅 supported_static；不推全域通过。',notchecked=None,findings=None,history=None,owner='M01',executed=False):
 caps.append({'capability_id':cid(n),'module':'M01','description':desc,'source_anchors':sources,'spec_anchors':specs,'entry_and_preconditions':pre,'configuration_data_host_limits':'R 固定快照、未被插件覆写；共享 readiness=PARTIAL_READY；源码/PBS/翻译可读，完整地图/Graphics/Audio/宿主缺席。具体输入门见 entry_and_preconditions。','reviewer':WHO,'checked_branches_boundaries':checks,'evidence_level':['SOURCE_STATIC','SPEC_STATIC']+(['EXECUTED_REFERENCE'] if executed else ['DERIVED_VECTOR']),'material_availability':'source_and_selected_text_data_available; game_host_and_complete_demo_unavailable','status':status,'reason':reason,'related_findings':findings or [],'history_links':history or [],'not_checked':notchecked or ['真实宿主调用及文件操作失败组合未执行；未列分支不计入本能力支持范围。'],'primary_owner':owner,'projection':'M01 数据/配置主责' if owner=='M01' else 'M01 仅资源身份到候选名称的投影；播放/绘制属于 WP15 归属域'})

cap(1,'规则世代为默认值输入，派生开关与内容数据选择分离',
 [sa('Data/Scripts/001_Settings.rb','7–17,130–169,425–428','机制世代8、派生阈值和空语言清单。'),sa('Data/Scripts/002_BattleSettings.rb','33–45,77–82,102–117','分类开关≥4；经验缩放世代5或≥7；亲密软限跟随独立亲密开关。'),sa(DATA+'005_Move.rb','79–88','损伤招式按开关选择自身分类或类型分类。'),sa('Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb','103–136','经验消费者实际分开使用分配、训练家加成和缩放开关。')],
 [sp(W2,'§3–5; 26–31,182,190–198,204–211','默认派生不是所有消费者的唯一输入。'),sp(T1,'KC01–KC02','世代与软限分离场景。')],
 '读取固定设置；世代5/6/7对照只推默认计算，不推完整战斗。', ['世代5与7缩放为真，6为假；可单独覆盖分类开关；亲密开关与软限的声明依赖。'],notchecked=['118项所有消费者和所有直接世代条件未逐点审查；不认证任何整代兼容。'])
cap(2,'默认兼容数据、备用世代和设施显式输入的发现边界',
 [sa(CP,'967–1017','顶层最长基名匹配与固定内容调度，无备份自动切换。'),sa(CC,'951–1021','设施名单按字段另读两个文件；缺引用文件得到空集合。'),sa('PBS/battle_facility_lists.txt','1–25','5节指定10个不同输入。'),sa('PBS/Gen 5 backup/moves.txt','3637–3641 / TACKLE','样本威力50，与默认40有区分。'),sa('PBS/moves.txt','5326–5330 / TACKLE','默认样本威力40。'),sa('PBS/Gen 5 backup/pokemon.txt','893–895 / CLEFAIRY','NORMAL；第6代备份与默认为FAIRY。')],
 [sp(W2,'§6.1–6.2; 215–236','备份仅候选、显式引用与自动发现区分。'),sp(W4,'§4.1; 51–56','发现不等于可编译。'),sp(T1,'KC04 / KL17','顶层后缀可发现，但固定基名缺失仍可早期失败。')],
 '盘点73个PBS；比较Gen5–8各3个有区别字段样本；其余不作逐记录兼容认证。',['33个顶层、36个世代备份、4个Shadow备份；TACKLE 5/6为50、7/8与默认40；CLEFAIRY类型和STEEL抗性样本。'],status='partial',reason='发现与材料存在支持；20个PBS文件选定行语义抽查，未证明全部默认/备份数据可编译、可组合。',notchecked=['53个PBS文件仅盘点；已抽查20文件的其余记录未审；八杯赛池、完整指标、所有跨代引用未验证。'])
cap(3,'共用身份、查找、枚举及直接注册替换',
 [sa(G,'8–210,217–242','三种身份查询/输入类型/枚举顺序与直接登记；false和空数组导出为缺值。')],
 [sp(W3,'§3.1,§4.1,§5.2; 26–42,75,125','严格/宽容/存在性分开，直接登记覆盖不等于编译拒绝。'),sp(T1,'KR03/KR07','非法类型与重复入口对照。')],
 '未覆写的共用查询；双身份登记无键冲突。',['未知合法键：严格拒绝、宽容空、存在性假；空输入与非法类型区分；未登记同类实例仍可直接返回。'],notchecked=['双身份键冲突、每个固定规则登记、各子类所有覆写未穷尽。'])
cap(4,'专用身份查询的回退与副作用',
 [sa(DATA+'013_Encounter.rb','20–60','精确存在性、版本0回退，以及目标版本枚举仍包含已有版本0。'),sa(DATA+'010_SpeciesMetrics.rb','32–68','缺失形态指标克隆并登记，默认后缀空。'),sa(DATA+'020_DungeonParameters.rb','58–65','未找到返回不登记默认参数。'),sa(DATA+'017_PlayerMetadata.rb','45–48','玩家编号缺失回退1。'),sa(DATA+'008_Species.rb','154–162','形态缺失回退基础记录。')],
 [sp(W3,'§3.2,§4.4; 50–57,93–95','例外按入口表述，不把所有查询视为只读。'),sp(T1,'KR01–KR05','查询、枚举和指标登记样本。')],
 '合法基础物种存在；正常编译的遭遇键表；无插件覆写。',['遭遇0/2均存在与单独存在；缺形态指标使登记集合增长；默认地牢参数不增长。'])
cap(5,'PBS schema求值与属性/身份/引用三级边界',
 [sa(CP,'95–150,384–484,690–737','普通重复属性替换、重复标记累加，正数与非负数、可选值和枚举校验。'),sa(CC,'4–68','按schema消费，未知合法属性忽略，登记前拒绝已存在身份。'),sa(DATA+'008_Species.rb','52–110','基础与形态两组schema；后者引用已知基础物种。')],
 [sp(W3,'§5; 97–144','约束模式及入口特定校验。'),sp(W4,'§4.2;71–92','未知属性不消费，新身份与未知引用不同。'),sp(T1,'KR09–KR10 / KL06,KL11–KL16','数值门与通用属性/身份样本。')],
 '通用入口及合法节语法，必需注册依赖满足；特殊电话默认另计。',['v拒绝0/u接受0；可选空位保留缺值；普通Name覆盖与^Evolution累加；未知引用失败。'],notchecked=['所有浮点/十六进制/枚举异常值及每个schema逐字段语义未穷尽；旧CSV辅助未审。'])
cap(6,'PBS前处理、分词位置条件和文本不保真边界',
 [sa(CP,'72–86,95–129,255–293,690–737,824–834','井号删除先于schema，CSV标记去除依赖位置，q仅保留预处理后值。')],
 [sp(W4,'§4.2,§5.5;62–78,166','普通/q/反写读回及实际反斜线字符区分。'),sp(W3,'108','q输入层限定。'),sp(T1,'KL07–KL10,KL33–KL35','合并耗尽和井号正反例。')],
 '合法基础物种与字段；反写例从其他有效入口已有含井号登记开始。',['Alpha#Beta变Alpha；引号不保护井号；末值包围保留、增加尾值才可能去标记。'],history=['GR3-M01-003'])
cap(7,'调试编译触发、整秒新鲜度、删除与异常部分状态',
 [sa(CP,'924–947,1020–1117','固定PBS改名、仅DEBUG、集合最大整秒≥、预删及分阶段异常处理。'),sa('Data/Scripts/999_Main/999_Main.rb','25–37','提示拒绝不否定后续自动判定。'),sa(C+'004_Compiler_MapsAndEvents.rb','45–81,1683–1751','导入排除999及变更后保存地图/公共事件。')],
 [sp(W4,'§3,§5.2,§6;21–47,139,179–191','不承诺原子性，重置退出跳过清理。'),sp(T1,'KL01–KL05,KL17,KL19–KL21','触发/早期失败/精度场景。')],
 'DEBUG编译检查；隔离新鲜度时其他触发均关闭、文件正常可读。',['1000.1/1000.9同整秒触发；999.9/1000.1不由时间触发；PBS缺失早期清单未建立。'],notchecked=['实际删除、Hangup/Reset宿主类别及恢复未运行；地图转换内部各模板未审。'])
cap(8,'专用PBS重复处理：训练家覆盖、遭遇合并和概率回写',
 [sa(CC,'646–765,809–945','重复地图版本拒绝，同槽合并，重复方式清槽；训练家直接登记并去重招式。'),sa(CW,'403–441','非正遭遇概率省略，非空槽才输出。')],
 [sp(W3,'128–132','三种重复层次分开。'),sp(W4,'§4.4,§5.5;112–125,164','整数前缀和Land概率往返。'),sp(T1,'KR08,KL22,KL30–KL32','异常/覆盖对照。')],
 '合法物种、方式和等级；完整导出成功；不包含当前地图遭遇缓存。',['重复方式省略概率保留旧概率但替换槽；0权重拒绝；训练家后节替换；Land0回写省略。'])
cap(9,'PBS导出按登记后缀分组及指标记录集合条件',
 [sa(CW,'4–65,291–351','通用输出只有实际后缀路径；指标仅非零形态建立路径。'),sa(DATA+'010_SpeciesMetrics.rb','32–68','查询缺失形态可增加后缀为空的记录。')],
 [sp(W4,'§5.5;160–175','无条目无路径、基本指标独自不建路径，等值非零形态省节不省路径。'),sp(T1,'KL18,KL23–KL26','登记、档案、PBS和再编译分层。')],
 '目录可写；实际登记集合和来源后缀已知；五组指标可比较。',['只有基本记录不输出；同后缀形态启用路径；不同后缀不改基础旧路径。'],notchecked=['所有专用导出、进化编辑与写出副作用KL27–KL29未重新逐链审查；宿主文件往返未运行。'])
cap(10,'可选Shadow数据缺席不清空已登记数据',
 [sa(DATA+'011_ShadowPokemon.rb','11–29','唯一声明可选类，缺档案时跳过加载。'),sa(CC,'4–8','可选输入全部不存在时在清表前返回。'),sa('PBS/Shadow Pokémon backup/shadow_pokemon.txt','3–13','备用物种/招式引用样本，默认顶层未发现该文件。')],
 [sp(W3,'§4.2;83–87','缺席与空表分开。'),sp(W2,'§6.2;232–236','备份存在不等于默认启用。'),sp(T1,'KR12','已有记录保留。')],
 '可选类文件缺席；分别从初始空表和已登记状态观察。',['跳过读取与不清表；备用SHADOW类型、Shadow招式与个体数据有跨数据引用。'],notchecked=['Shadow完整捕获/成长/净化消费者及备用数据整体启用未审。'])
cap(11,'电话默认重复的登记/探测/最终消费交界',
 [sa(CC,'54–60,1237–1268','Default转为字符串身份；成功终检收集最终条目。'),sa(DATA+'021_PhoneMessage.rb','15–46,53–69','默认存在性探测为符号键，联系人为三元键。'),sa('Data/Scripts/013_Items/004_Item_Phone.rb','447–461','当前/初始版本缺失才取默认并经当前语言查找。')],
 [sp(W3,'§3.2,§5.2;49,126–134','默认后项整条覆盖，联系人仍拒绝。'),sp(W4,'89','例外明确。'),sp(T1,'KR14–KR16,KL36','完整合法前提和第一项非自动回滚。')],
 '同一输入两个合法Default节或两个相同已知类型/姓名/版本联系人节；无其他覆盖。',['Default A/B最后只有B；普通联系人/道具第二条拒绝；B是候选而非保证显示。'],history=['GR3-M01-004'])
cap(12,'语言选择、消息加载与按域查找回退',
 [sa(I,'481–642,679–710','31域、键归一、game/core查找、空串有效命中及载入异常清空。'),sa('Data/Scripts/003_Game processing/001_StartGame.rb','21–34','无存档且≥2语言才选择；非空候选立即加载。'),sa('Data/Scripts/016_UI/013_UI_Load.rb','300–344','载入语言菜单及有存档直接回写选项。')],
 [sp(W8,'§3–5.2;25–63','数组空串、哈希原文、地图四层链不同。'),sp(T2,'LZ01–LZ04,LZ13–LZ14','空译与加载/保存边界。')],
 '合法外层消息数组，内层符合查找形态；消息路径按语言片段；真实存档不操作。',['game优先core；地图game共享桶先于core专用桶；当前两层缺失不查默认语料。'])
cap(13,'翻译收集与作者导出：目标语言、转义、覆盖及稀疏地图桶',
 [sa(I,'7–240,244–371','收集来源、Hangup部分结果；先确认删除后写；稀疏桶合并预检与逐图不同。'),sa('Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb','1423–1455','作者选B与取消不会改玩家语言。'),sa('Data/Scripts/001_Technical/002_Files/001_FileTests.rb','6–31','导出清理递归文件枚举，目录本身保留。')],
 [sp(W8,'§6.1–6.2.1;71–96','收集/导出与运行语料分层，稀疏桶条件完整。'),sp(T2,'LZ05–LZ06,LZ12,LZ15–LZ16,LZ23–LZ25','数据形态与覆盖/稀疏桶对照。')],
 '默认语料存在、写入/相关宿主可用；缺桶样本不视为默认实际数据。',['空0缺1有效5：合并跳过，逐图可写5；早桶非空合并也继续写5；取消覆盖无写。'],history=['GR3-M01-002'],notchecked=['真实地图收集、默认二进制结构和所有脚本字面量覆盖未验证；提取/写回不执行。'])
cap(14,'翻译导入预处理、节号和首内容形态判别',
 [sa(CP,'154–181','列首注释/空行删除，保留内容修剪。'),sa(I,'214–240,350–471','数字首内容数组、Map数组拒绝、先截断后读入。')],
 [sp(W8,'§6.3–6.3.1;98–119','行过滤先于节号与形态；数字节0拒绝、空译往返失败。'),sp(T2,'LZ07–LZ11,LZ17–LZ22','单文件与完整编译副作用区分。')],
 '合法输入文件；错误例单条非地图哈希K；完整编译截断另要求输出成功打开。',['纯数字首键两行拒绝；空译/列首井号被删，前置空格井号保留；转义制表符恢复。'],history=['GR3-M01-001'])
cap(15,'翻译导入同域重复键、归一冲突及重复节逐项合并',
 [sa(I,'437–466,481–489','节内后键替换，归一键碰撞，节间同位置合并；并非整节替换。'),sa(I,'376–384','所有输入累计到同一消息集合。')],
 [sp(W8,'§3.2,§6.3;30,98–105','已列归一/形态，没有同域冲突解决规则。'),sp(T2,'LZ17,LZ21','显式无合并冲突前提，没有对照向量。')],
 '单一可读文件中非空24号域；同形态段合法；无插件覆写。',['同键后值；双空格/单空格键归一后碰撞；早节独有L保留；重复数组节仅覆盖有值索引。'],status='missing',reason='确定的正常导入合并合同未在全131正式文件反证搜索中找到；GR4-M01-001。',findings=['GR4-M01-001'],executed=True,notchecked=['完整菜单编译、跨操作系统排序和全部混合形态组合；探针异常边界见validation结果，不外推全部情况。'])
cap(16,'普通占位参数的反斜线解释与格式化入口对照',
 [sa(I,'774–823','普通与地图占位使用替换字符串，格式化入口以格式计算结果插入。'),sa('Data/Scripts/007_Objects and windows/002_MessageConfig.rb','790–814','备用定义有条件，不覆盖正常已定义本地化入口。')],
 [sp(W8,'§5.3;67 / §8;142','字面替换概括缺少反斜线参数例外。'),sp(P+'user-interface/wp17-messages-windows-input.md','13–30','显示控制符属于后续窗口层，未解决本地化插入阶段。')],
 '当前消息均未命中，输入原文X{1}Y；参数为真实字符U+005C/U+0026或U+005C/U+0031，不是字符串表示法转义。',['普通Q得XQY；反斜线&得X{1}Y；反斜线1得XY；地图同样；字符串格式化对照保留反斜线&。'],status='partial',reason='正常与异常传播描述支持，但完全字面替换与原参考返回值冲突；GR4-M01-002。',findings=['GR4-M01-002'],executed=True,notchecked=['所有替换特殊组合、递归占位、所有格式说明符、游戏内实际渲染未穷尽。'])
cap(17,'内容身份到资源命名及候选降格',
 [sa(DATA+'009_Species_files.rb','3–68,113–168,183–199','物种图按闪光/暗影/性别/形态/000组合降格，蛋/脚印/影子/叫声先查询基础记录。'),sa(DATA+'014_TrainerType.rb','52–98','类型登记门、装束后缀与基础回退。'),sa(DATA+'006_Item.rb','74–116','空/未知/机器及持有图标路径不同。')],
 [sp(W15,'§3.2–4.3;32–69','候选名称、空格目录、类型门和未知道具兜底。'),sp(T15,'RS01–RS08,RS18,RS20;301–308,318,320','存在性前提成对区分。')],
 '只按资源解析存在/缺席输入静态推导；没有Graphics/Audio，不声称任何候选实存。',['未登记形态但基础存在；图像入口无前置门 vs 蛋等有门；Front shiny同级目录；机器HM双层降格。'],owner='WP15 / Engine-Overworld',notchecked=['低层扩展名解析、缓存、播放、实际像素及损坏媒体未审；不把共享投影统计为资源域整体支持。'])

dump('capabilities.json',caps)

common={'module':'M01','status':'OPEN','reviewer':WHO,'source_baseline':{'commit':R,'tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','path':'/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials'},'specification_baseline':{'commit':B,'tree':'d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a','identity_source':'../../baseline.json; formal131 identities shared'},'disposition':'REQUIRED','evidence_level':['SOURCE_STATIC','SPEC_STATIC','EXECUTED_REFERENCE'],'execution_status':'Original selected functions executed with minimal ancillary stubs on Ruby 2.6.10; NOT_EXECUTED_HOST_OR_DEMO; full compile/export not executed.','confidence':'high within stated inputs and fixed baseline','affected_files':[W8,T2],'dependencies':['文本预处理与消息查找','作者翻译工具；实际文件系统/宿主不在执行证明内'],'related_findings':[],'history_links':{'relationship':'new','third_round_ids':[],'second_round_id':None,'note':'不重开GR3-M01-001–004；第三轮为行过滤、稀疏导出、PBS井号、电话默认身份，本项不同根因。'},'user_decision_needed':'记录固定参考事实无需新增决策；未来是否兼容异常可另决，不修改参考。','review_resolution':'已完成本审者源端/全正式集反证；待主汇总者安排一次独立针对性反证/去重；未修改正式规格。'}
f1={**common,'id':'GR4-M01-001','title':'翻译同域重复键与重复节的逐项合并规则缺失','severity':'P2','category':'missing behavior contract / Generic Kernel / Demo-Developer Experience',
 'source_anchors':caps[14]['source_anchors']+[sa(CP,'154–181','按文件顺序逐节送入导入；重复节头未拒绝。'),sa('Data/Scripts/001_Technical/002_Files/001_FileTests.rb','6–14','完整导入的文件枚举结果排序；单文件向量不依赖跨文件排序。'),sa('Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb','1457–1475','作者编译菜单实际调用完整导入。')],
 'spec_anchors':caps[14]['spec_anchors']+[sp(W8,'52','语言game覆盖core是查找优先级，不能代证同域导入冲突处理。')],
 'expected_reference_behavior':'同一合法文本域内的重复规范键取最后译文；后续同域同形态节逐项合入已积累域，覆盖同键但保留先前独有键。按索引节同样只覆盖后节实际提供的索引，不删除稀疏遗漏位置。',
 'current_spec_behavior':'WP08描述键归一、数组/哈希判别、节号、失败及运行层game/core优先；未规定同域重复输入的覆盖与保留结果。LZ17/21用无冲突前提规避该分支。',
 'gap':'独立实现可合理选择重复拒绝、先值优先或整节替换；三者都不符合固定参考的合并结果。',
 'preconditions':['单一普通可读翻译文件，非地图24号域；所有内容非空、非注释且段落形态合法。','同域多节按文本出现顺序；不更换被测入口，不假定默认语料本身含重复。'],
 'minimal_counterexample':{'input':'一个24号哈希节按顺序含K→First、K→Last。','reference_result':'成功，K仅取Last。','distinguishes':'重复拒绝/首值优先均不同。'},
 'normal_case':'不同键K→First、L→Other均保留；同域后节K→Last、M→New合入后，K=Last、L=Other、M=New。',
 'failure_or_boundary_case':'A双空格B与A单空格B先规范成同一键后取后值；数组先入再以非数字哈希键向同域合入的探针抛TypeError，前节内存数据保留，不能把所有混合形态都说成安全合并。按索引0/2先入、后节仅0时，2保留。',
 'impact_on_independent_implementation':'拆分翻译文件、重复修订或空白规范碰撞时，最终消息集合和运行查找可能不同；这是有效导入数据合同而非风格要求。',
 'negative_evidence_search':{'artifact':'negative-search.json#N01','scope':'全部131正式Markdown（含scope、正文、附表、测试）','terms':['重复','同键','合并','覆盖','冲突','duplicate','collision','merge','翻译','译文','本地化','SCRIPT_TEXTS','compile_text','Translation','文本域'],'reviewed_contexts':[W8+' §3.2/§5.1/§6.2–6.4',T2+' LZ01–LZ25',P+'demo-dx/wp75-project-conversion-and-authoring-tools.md:20',P+'user-interface/wp17-messages-windows-input.md:13'],'result':'未找到同域导入的重复键/节合并规则；命中是game/core查找、导出目录覆盖或地图文件分组，语义不同。'},
 'proposed_spec_change':'WP08作者导入补节内规范键后值覆盖、同形态重复节按键/索引合并及早节独有项保留；明确混合形态不保证兼容。补最小正常与冲突向量，不要求新框架采用原容器结构。',
 'acceptance_criteria':[{'kind':'static_required','criterion':'正文与LZ补同键、规范碰撞、重复同域节独有键保留及稀疏索引保留的准确结果。'},{'kind':'static_required','criterion':'分开同域编译合并与game/core运行查找优先；保留完整入口先截断副作用及Map形态门。'},{'kind':'execution_optional','criterion':'若执行，记录独立同文件夹具和所用参考入口；不得把本次隔离执行升级为宿主/完整导入通过。'}],
 'shared_contracts':['WP08 §3.2 文本身份','WP08 §6.3 作者导入','WP04末段消息产物交界（无需复制重复规则）'],'related_capabilities':[cid(15)],'root_cause_group':'GR4-M01-TRANSLATION-SAME-DOMAIN-MERGE','unknowns':['实际全部语料中的碰撞数量、完整菜单/二进制保存、所有混合域形态组合未执行。'],'excluded_claims':['不声称导入过程应拒绝重复或应被修复。','不声称默认18份语料当前存在这些重复。','不以本项重开第三轮行过滤问题。']}
f2={**common,'id':'GR4-M01-002','title':'普通本地化占位参数并非完全字面插入','severity':'P3','category':'contradiction / Generic Kernel / observable text result',
 'source_anchors':caps[15]['source_anchors'], 'spec_anchors':caps[15]['spec_anchors'],
 'expected_reference_behavior':'普通脚本和地图占位入口会解释参数中的替换特殊组合：两个真实字符反斜线和&恢复被匹配的占位文本；反斜线和数字1在本例中变为空。字符串格式化入口对照保留反斜线和&。',
 'current_spec_behavior':'WP08 §5.3将普通占位概括为字面替换，未限定参数字符串中反斜线的解释。',
 'gap':'依完全字面插入实现，输入参数反斜线&将输出该两字符；固定参考却保留原占位标记，返回文本不同。',
 'preconditions':['正常本地化主入口已定义，未被插件覆写。','当前语言两层无命中，故取原文X{1}Y；本例在进入任何消息窗口之前观察返回字符串。','参数为U+005C与U+0026两个字符，或U+005C与U+0031两个字符；不是字符U+0001。'],
 'minimal_counterexample':{'input':'原文X{1}Y，参数为两个真实字符U+005C/U+0026。','reference_result':'X{1}Y','literal_result':'X后接U+005C/U+0026再接Y'},
 'normal_case':'普通参数Q返回XQY；格式化字符串入口原文X{1:s}Y、同反斜线&参数返回包含这两个字符的X\\&Y。',
 'failure_or_boundary_case':'普通参数U+005C/U+0031返回XY；地图5的普通入口和脚本普通入口对反斜线&均返回X{1}Y。没有异常，不涉及WP17之后的暂停控制符转换。',
 'impact_on_independent_implementation':'含反斜线的作者参数或动态名称的返回文本可能改变；影响范围有限，但“字面”合同会指导出不同字符串结果。',
 'negative_evidence_search':{'artifact':'negative-search.json#N02','scope':'全部131正式Markdown','terms':['字面替换','占位','后向引用','反向引用','backreference','替换表达式','replacement','INTL','参数'],'reviewed_contexts':[W8+' §5.3/§8',P+'user-interface/wp17-messages-windows-input.md:13–30',T2+' LZ04'],'result':'未找到参数反斜线的本地化阶段例外；WP17的反斜线1是显示控制层，不能解释本次返回前已消失的参数。'},
 'proposed_spec_change':'将“字面替换”限定为常规参数，不承诺任意参数逐字保留；用字符码明确两项参考边界和格式化入口对照，保留未来兼容选择。无需规定未来语言的替换API。',
 'acceptance_criteria':[{'kind':'static_required','criterion':'正文给出X{1}Y加反斜线&返回X{1}Y、加反斜线1返回XY，以及Q正常对照。'},{'kind':'static_required','criterion':'图区普通占位同样适用，格式化字符串对照保留反斜线&；明确观察在消息窗口前，勿混同U+0001。'},{'kind':'execution_optional','criterion':'任何重跑使用准确输入字符并记录参考入口、解释器版本及宿主未执行界限。'}],
 'shared_contracts':['WP08 §5.3 占位参数','WP17消息输入（仅依赖引用）'],'related_capabilities':[cid(16)],'root_cause_group':'GR4-M01-PLACEHOLDER-REPLACEMENT-ESCAPES','unknowns':['所有反斜线组合、占位嵌套和游戏UI实际效果未穷尽。','Ruby2.6隔离结果不是随附3.1宿主执行。'],'excluded_claims':['不将参数字符称为已发生的安全漏洞。','不推断用户实际游戏文本出现该输入。','不要求未来保留异常；必修只针对参考事实表述。']}
dump('findings.json',{'schema_version':'1.0','findings':[f1,f2]})

coverage=[]
def cov(path,contracts,nums,status='supported',notchecked=None,unsupported=None):
 sources=[]
 for n in nums:
  for a in caps[n-1]['source_anchors']:
   if a not in sources:sources.append(a)
 coverage.append({'path':path,'specification_baseline':B,'contracts_checked':contracts,'source_anchors':sources,'status':status,'support_evidence':{'capabilities':[cid(n) for n in nums],'meaning':'仅所列条款的 supported_static；文件状态不是整篇PASS。','execution':'仅CAP015/016的自制夹具调用原函数，其余静态。'},'dependencies':list(dict.fromkeys(a['path'] for n in nums for a in caps[n-1]['spec_anchors'] if a['path']!=path)),'unsupported_assertions':unsupported or [],'not_checked':notchecked or ['未列条款及真实运行、组合穷尽未审。']})
cov(W2,['§3计数/世代默认；§4.2选定开关；§5派生边界；§6普通发现/备份/语言；§7–8限定'],[1,2,10,12],status='partial',notchecked=['正文已通读；118设置所有消费者、全部候选内容兼容性、官方各代规则未逐项复核。'])
cov(W3,['§3.1共用身份；§3.2 Encounter/Metadata/Player/Species/Metrics/Phone/Terrain；§4可选/默认；§5类型与重复；§6–7责任目录'],[3,4,5,8,10,11],notchecked=['DungeonTileset特殊回退只定位未逐行复核；完整Nature及其他固定规则表未复核；字段组目录不等于其全部行为已审。'])
cov(W4,['§3触发/异常；§4发现/活跃解析/遭遇例外；§5通用/指标/遭遇导出；§6部分状态'],[5,6,7,8,9,11],status='partial',notchecked=['§5.3地图转换细则、§5.4完整动画映射、§5.5进化编辑/写出KL27–29仅读正式合同，未重新完成源端全链核对。'])
cov(W8,['正文§1–11通读；§3–5消息与参数；§6收集/提取/编译；§8边界；LZ对应'],[12,13,14,15,16],status='partial',unsupported=['GR4-M01-001: §6.3缺同域重复输入合并合同。','GR4-M01-002: §5.3完全字面替换概括不成立。'])
cov(T1,['KC01–KC06；KR01–KR12,KR14–KR16；KL01–KL26,KL30–KL36逐项对照；KR13仅登记目录顺序样本'],[1,2,3,4,5,6,7,8,9,10,11],status='partial',notchecked=['KR13全25性格消费者与KL27–KL29编辑器/进化回写本次不重新认证；所有正式向量均未作为测试执行。'])
cov(T2,['仅LZ01–LZ25，86–114行；正文语言门/查找/导出/导入前提'],[12,13,14,15,16],status='partial',unsupported=['没有同域重复/规范碰撞合并向量；没有普通参数反斜线对照。'],notchecked=['EP/TR/IO/DP/SV/MG等其他模块测试族不属本次M01语义范围；LZ正式向量未执行。'])
cov(W15,['§3.2–4.3,32–69：物种、蛋、影子、训练家装束、机器道具资源命名/回退'],[17],notchecked=['文档其他章节虽作上下文阅读，底层资源解析/缓存/声音状态与宿主结果不作语义认证。'])
cov(T15,['RS01–RS08,RS18,RS20；301–308,318,320'],[17],notchecked=['其余IM/RS/B04-R/地图/音频向量未审；资源文件不存在于当前材料。'])
cov(P+'user-interface/wp17-messages-windows-input.md',['13–30行：本地化与窗口控制符分层，仅GR4-M01-002反证'],[16],status='partial',notchecked=['WP17窗口、格式标签附表、输入/UI其余合同不在M01。'])
cov(P+'scope-statement.md',['1–14行当前保留层及36/52行历史未执行限定，限定本轮不移转旧批准'],[2,13,17],status='partial',notchecked=['未重新审计所有旧批登记数字；当前基线身份取共享baseline与delivery导航，不把历史层当当前状态。'])
dump('spec-coverage.json',coverage)

oldp='review/remediation-third-20261012-prepare/U01/actual-integration/independent-review/attempt-01/per-id-verdicts.json'
old=json.loads(subprocess.check_output(['git','show','68505ac57164e9192cd700431f5634f0aad7242b:'+oldp]))
reg=[]
lookup={1:14,2:13,3:6,4:11}
for i,x in enumerate(old['records']):
 if not x['id'].startswith('GR3-M01'):continue
 number=int(x['id'].split('-')[-1]); current=caps[lookup[number]-1]
 criteria=[]
 for c in x['acceptance_criteria_review']:
  criteria.append({'criterion':c['criterion'],'actual_check':'本次重新阅读固定R与B当前条款及相邻对照；'+c['evidence'],'result':'supported_static; no regression found','consumer':{'1':'作者导出→预处理→单文件导入，与运行空译不同','2':'作者合并/逐图导出及覆盖删除','3':'PBS名称/q图鉴文本及写出再读','4':'电话终检文本收集→联系人默认候选→当前语言查找'}[str(number)]})
 reg.append({'id':x['id'],'historical_state':'CLOSED retained; not reopened','current_file_anchors':current['spec_anchors'],'source_anchors':current['source_anchors'],'old_acceptance_fixed_reference':{'commit':'68505ac57164e9192cd700431f5634f0aad7242b','path':oldp,'pointer':f'/records/{i}/acceptance_criteria_review'},'formal_acceptance_fixed_reference':{'commit':'c2eb74c7cbcf8a190d5e902d871fbce44904efd6','path':'review/remediation-third-20261012-prepare/registration/U01-formal-acceptance.json','note':'Earlier formal acceptance generation; final_CLOSED=false there is not reopened state.'},'closure_fixed_reference':{'commit':'98e49a592c9e82b1e53d3f1fd403ba2ad0935983','path':'review/remediation-third-20261012-prepare/registration/final-closure-acceptance.json','pointer':'/activated_required_ids23','effective_final_CLOSED':23},'criteria_checked':criteria,'result':'supported_static','limits':['本次是固定当前字节的独立静态复核，未借旧PASS替代源读。','这些历史正式向量未运行；本轮新隔离探针不追认旧执行，也不认证默认语料/完整宿主。']})
dump('regression.json',reg)

probe=json.loads((O/'validation/reference-probe-result.json').read_text())
probe['inputs']={'harness':'validation/reference-probe.rb','fixture_files':['validation/'+n+'.txt' for n in ['distinct_keys','duplicate_key','normalized_collision','repeated_hash_section','repeated_array_section','array_then_hash','hash_then_array']],'parameter_inputs':'Plain Q, Unicode code points [92,38] and [92,49], script/map ordinary and formatted controls.','source_commit':R,'loaded_original_files':[CP,I],'pre_execution_plan':'validation-plan.md'}
dump('execution.json',{'actual_executions':[probe],'not_executed':['Full Compiler.main / PBS compilation, PBS rewrite/export, map/event/animation conversion.','Translator.compile_text full workflow, extraction/deletion/export, default binary deserialization and all 18-file import.','Any real save read/write, language switch UI, host/game/Demo/audio/graphics.','Formal KC/KR/KL/LZ/RS vectors, legacy reviewer scripts, all combinations of configuration and backups.'],'static_inspections':{'evidence_level':['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR'],'artifacts':['source-scope.json','negative-search.json','capabilities.json','spec-coverage.json','regression.json'],'note':'rg/nl/Python metadata scans are inspection/tool validation, not reference behavior execution; failed path lookups were corrected and do not prove absent capabilities.'},'model_identity':{'requested':'gpt-6-astra','reasoning_effort':'ultra','service_tier':'default','fast':False,'actual_echo':'UNVERIFIED','request_source':'../../tasks/M01-launch.json; no self-attestation of actual model/tier'},'readiness':'PARTIAL_READY from shared baseline; no whole-repository recheck'})
print(json.dumps({'capabilities':len(caps),'findings':2,'spec_coverage':len(coverage),'regression':len(reg)},ensure_ascii=False))
