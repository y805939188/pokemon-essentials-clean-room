"""Assemble C01 audit documents; JSON/text processing only, no behavior execution."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
R = '/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials'
B5 = '9366d9d17aaeac3b4414236468affa650fb3dd27'
RC = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
RT = '7589c800b61ba13a13040ed0d686979b80a84fd0'
F = 'deliverables/final-specification-set/'
K = F + 'generic-kernel/'
C = F + 'creature-rpg/'
P = F + 'pokemon-rules/'
U = F + 'user-interface/'
D = F + 'demo-dx/'
T = F + 'test-catalog/'
WP03 = 'wp03-content-identity-and-schema.md'
WP04 = 'wp04-pbs-lifecycle.md'
WP08 = 'wp08-localization.md'
WP18 = 'wp18-creature-identity-species-ownership.md'
WP19 = 'wp19-attributes-ability-and-stats.md'
WP24 = 'wp24-player-trainers-partners.md'
WP25 = 'wp25-party-and-storage.md'
WP73 = 'wp73-a-content-editors.md'
WP66 = 'wp66-b-storage-and-pokedex-ui.md'
KT = 'generic-kernel-wp02-03-04.md'
LT = 'generic-kernel-wp05-06-07-08-09-10.md'
CT = 'creature-rpg-wp18-20-24-25-26.md'
ST = 'pokemon-rules-wp19-21-22-23-34.md'
DT = 'demo-dx-wp72-73-74-75-76-77.md'
UT = 'user-interface-wp17-63-65-66-67-68-69-70-71.md'
COMP = 'Data/Scripts/021_Compiler/001_Compiler.rb'
CPBS = 'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb'
WRITE = 'Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb'
INTL = 'Data/Scripts/001_Technical/003_Intl_Messages.rb'
SPECIES = 'Data/Scripts/010_Data/002_PBS data/008_Species.rb'
TRAINER = 'Data/Scripts/010_Data/002_PBS data/015_Trainer.rb'
POKEMON = 'Data/Scripts/014_Pokemon/001_Pokemon.rb'
STORAGE = 'Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb'
DEBUG = 'Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb'

def src(path, ranges, scope):
    return dict(path=path, absolute_path=R+'/'+path, ranges=ranges, semantic_scope=scope,
                revision=RC, read_mode='direct_static_source_or_literal_data')

def spec(path, ranges, section):
    return dict(path=path, ranges=ranges, section_or_vector=section, revision=B5,
                read_mode='direct_current_text')

def item(n, severity, disposition, source, specs, challenge, evidence, conclusion,
         expected, minimal, normal, boundaries, math, accepted, corrections, excluded,
         required, optional, preserve, history, unknowns, classification):
    return dict(id=f'GR5-M01-{n:03}', reviewer='C01',
                disposition=disposition, severity=severity,
                recommendation_only=True, source_directly_read=source, spec_directly_read=specs,
                rebuttal=dict(challenge=challenge, counterevidence=evidence, conclusion=conclusion),
                corrected_expected_behavior=expected, minimal_counterexample=minimal,
                normal_case=normal, boundary_cases=boundaries, state_order_math=math,
                accepted_claims=accepted, facts_needing_correction=corrections,
                excluded_claims=excluded,
                acceptance_adjustments=dict(required=required, optional=optional,
                                            preserve=preserve, must_execute=[]),
                history_relation=history,
                execution_status='SOURCE_STATIC / SPEC_STATIC / DERIVED_VECTOR; C01 reference, model, host and generator execution count = 0',
                confidence=dict(source_behavior='high_static', contract_assessment='high_for_bounded_claim', severity='reviewer_judgment'),
                unknowns=unknowns, classification=classification,
                independent_rebuttal_complete=True)

records = []
records.append(item(1, 'P3', 'required',
 [src(COMP, [[72,76],[95,135],[255,293],[343,435],[690,737],[742,842]], '行预处理、当前分词/数值转换/记录入口、Unused 对照与写出'),
  src(CPBS, [[4,68],[283,330],[388,470]], '普通物种和形态调用；尺寸转换先于记录构造/形态继承'),
  src(SPECIES, [[52,111],[113,143],[175,221],[391,451]], 'Height/Weight 模式、编辑器另一路、默认单位与反写'),
  src('PBS/pokemon.txt', [[3,26]], '默认普通十进制尺寸样本')],
 [spec(K+WP03, [[89,117],[160,205],[214,240]], '§4.3、§5.1、字段责任及未知'),
  spec(K+WP04, [[58,92],[153,177],[212,227]], '§4.2、§5.5 与测试/边界'),
  spec(C+WP18, [[47,98],[271,309]], '§3.2 默认表；§7.3/7.4 储存单位与毫米辅助'),
  spec(D+WP73, [[36,46],[63,75],[103,108]], '数值编辑边界、尺寸编辑'),
  spec(U+WP66, [[198,204]], '§7.1 单位显示与筛选消费'),
  spec(P+'wp62-pokedex-records-regions-and-content.md', [[140,155]], '§6 显示消费，不是 PBS 输入语法'),
  spec(T+KT, [[16,81]], 'KR09/10；KL01–36'),
  spec('specs/kernel/'+WP03, [[119,163],[231,270]], '§5.1/5.2、数值场景'),
  spec('specs/kernel/'+WP04, [[79,111],[157,166],[217,242]], '活跃入口与原稿场景'),
  spec('specs/creature-rpg/'+WP18, [[57,99],[255,262]], '默认尺寸与读取'),
  spec('specs/demo/'+WP73, [[52,61],[119,125]], '有界数字与尺寸编辑'),
  spec('specs/ui/'+WP66, [[194,198]], '十分之一单位显示')],
 '“浮点”是否已允许常规解析自由？尺寸最小值、编辑器非零输入或原稿未知项能否排除反例？',
 'WP18 已给十分之一单位与缺省 1，WP73-A 已给有界整数编辑；它们都不规定手工 PBS 文本的接受集合。WP03 将完整解析交 WP04，而 WP04 只回指类型名。Unused 数值辅助不是当前字段调用。B16-C121 是已储存数值的显示换算，也不能消除词法差异。',
 '存在作者文本入口的具体事实缺口；从原 P2 降为 P3。给定反例是窄输入兼容边界，未证明普通随附尺寸数据失效或整个数值系统有错。',
 ['合法单行基础物种输入的 Height 或 Weight 为单个 ASCII 小数点时，当前入口转换为 0，随后乘 10、最近整数取整并至少取 1，登记为十分之一单位 1。',
  '独立的 -1.0、+1.0、1e2 在当前浮点识别阶段拒绝；1.0 登记 10。省略基础物种字段使用记录默认 1；省略形态字段继承基础记录，并不都等于 1。',
  '仅描述固定参考事实；不要求未来采用特定语言、正则或异常输入政策。'],
 '合法基础物种节仅把 Height 改为“.”：局部登记值 1。其余字段/依赖合法且无更早失败；不是完整工程编译成功断言。',
 '同入口 Height=1.0 得 10；默认 BULBASAUR 的 0.7 与 6.9 属普通十进制数据。',
 ['-1.0 / +1.0 / 1e2 分别拒绝。', '字段完全省略、显式空文本、低层空字符串转换不是同一输入；本项不以低层空串接受推导空属性合法。', '已存在基础高度 H 的形态省略高度时继承 H。'],
 '顺序：行预处理 → 分词 → 浮点接受门 → 数值转换 → 尺寸整数化 h=max(1,round(10x)) → 登记；缺省/继承走各自路径。',
 ['单点接受及三个具名文本拒绝成立。', '当前正文没有等价的具名浮点接受边界。', '储存单位、默认值及 UI 换算的现有正确范围保留。'],
 ['原候选“省略走类默认”只可用于其基础物种夹具；形态省略须改述继承。', '原文“取整”应明确为最近整数取整，不能误读为截断。', '严重度由 P2 降 P3。'],
 ['不把所有浮点或多行/Unicode/溢出组合列为已审。', '不要求未来公开低层转换 API；必修锚定实际 PBS 字段。', '不新增默认数据受损、宿主错误画面或完整编译结论。'],
 ['WP04 给出当前单行浮点边界及“.”、1.0、带符号/指数对照，连接尺寸整数化。', '省略基础字段与省略形态字段分开；保持现有引号/q/预处理顺序。', '新增少量静态向量即可；WP03 可只准确交叉引用，无须重复整套表。'],
 ['扩展到全部数值词法/任意异常输入不作为本项验收。'],
 ['WP18 默认表、WP73 数字编辑、WP66-B/B16-C121 显示单位、GR3-M01-003 的井号先行边界。'],
 dict(relation='new_bounded_input_consumer_scope', retained=['GR3-M01-003','B16-C121'],
      explanation='井号预处理与尺寸显示的旧结论不重开；本 ID 只补预处理后 f 字段的接受事实。GR3-M09-001 DEFERRED 和 GR3-M02-003 NO_REQUIRED_REVISION 不相关且保持。'),
 ['未执行 Ruby 转换、编译、写回或错误 UI；精度极端输入未审。'],
 ['Generic Kernel','Demo / Developer Experience','Creature-RPG']))

records.append(item(2, 'P2', 'required',
 [src(INTL, [[7,189],[244,372],[478,670],[710,759]], '收集实际调用、默认/目标语言材料、过滤与替换/追加、导出选择及运行层隔离'),
  src(CPBS, [[202,231],[366,380],[525,538],[931,946]], '招式/基础物种替换收集、形态追加收集、训练家终检'),
  src(COMP, [[1020,1040]], '编译末段收集后保存，调试门'),
  src('Data/Scripts/015_Trainers and player/002_Trainer_LoadAndNew.rb', [[62,68]], '编辑工具也替换训练家类型名称材料'),
  src(DEBUG, [[1423,1455]], '导出目标语言来自作者选择，而不是当前玩家语言')],
 [spec(K+WP08, [[1,191]], '全文，尤其§2/§5/§6.1–6.4'),
  spec(K+WP04, [[193,227]], '收集归 WP08；失败边界'),
  spec(T+LT, [[110,153]], 'LZ01–35；运行、导入归并与导出是不同合同'),
  spec(D+'wp72-debug-contexts-and-controls.md', [[265,274]], '调试提取/编译入口'),
  spec(D+'wp75-project-conversion-and-authoring-tools.md', [[18,20],[33,44]], '§1/§3 明确委托本地化'),
  spec('specs/kernel/'+WP08, [[1,195]], '全文，尤其默认分层/收集/导出/原稿场景'),
  spec('specs/demo/wp72-debug-contexts-and-controls.md', [[281,294]], '作者入口'),
  spec('specs/demo/wp75-project-conversion-and-authoring-tools.md', [[20,34],[43,48],[59,64]], '边界与调用顺序')],
 '现有“从默认消息导出”、game/core 优先级及 GR4 同域逐项合并能否已经覆盖全部候选？是否错误要求将每个公开低层方法都写成未来 API？',
 '“从默认消息导出”已经确定默认材料是原文集合，不宜把语言独有键不导出单独算必修。GR4-M01-001/LZ26–30 处理翻译导入后的归并，不能替代编译/收集生成默认 game 材料的过滤。源有普通招式名称替换、形态文本追加、脚本追加与公共事件/地图桶替换的实际调用。数组 set/add 只定位定义和转发，没有普通静态收集调用者。',
 '保留 required/P2，但必修只落在实际作者默认哈希材料的过滤、替换/追加和地图同桶范围。导出集合部分主要是既有合同的澄清；数组低层分支事实可作补充，不单凭 API 存在升级为必修。',
 ['以默认 core 的同域规范键集合过滤收集输入；比较键是否存在，而非原文值是否相等。替换式重建该默认 game 域，追加式保留旧域再写新候选。',
  '追加遇到与 core 重复而被跳过的输入时，不删除旧 game 的同键值；也不清理未再收集的旧独有键。地图 m 只以默认 core 的 m 桶过滤，不借用运行查找的共享桶 0。',
  '数组分支按同索引原文是否相等决定写入，并跳过 nil/空串；哈希分支仅跳过 nil，空串可以形成键，但导出会跳过空原文值。两者不能统称为“均只收非空文本”。',
  '导出使用作者选定目标语言的译文材料，输出条目由所选默认 core/game 的非空原文条目决定。外层检查范围可能包含语言材料较长的域号，不能说根本不遍历语言独有域；也不能据此承诺任意损坏/缺失地图域都会安全跳过。'],
 '合法默认 core 哈希有 A，旧 game 有 Z；替换式收集 A/B 后 game 只有 B。普通招式终检存在这种替换调用。',
 'core 无 B，收集非空 B 后 game 含 B；追加同一输入保留旧 Z 并加入 B。',
 ['旧 game 同时有 A→Old 与 Z，追加 A/B：A→Old、Z 保留，B 新增；替换则仅 B。', 'core 仅桶0有 A、桶4无 A，收集地图4的 A 仍进入 game[4]。', '选定目标语言独有 X、默认域无 X，不新增 X 输出；该项不算独立缺陷。', '数组收集与哈希收集的差异为已读事实，但无普通数组收集调用者证明。'],
 '明确四层材料身份；默认集合更新发生在保存之前。set 是指定域/桶重建，add 是保留旧值再按过滤写入，跳过并非删除。导入同域归并和运行查找不介入这一步。',
 ['哈希 core 键过滤及替换/追加差异成立。', '具名最小输入可改变最终默认 game 材料，普通作者路径可到达。', '导出默认条目主导事实成立；既有正文已给同义基础。'],
 ['不能说 add 必然让 game 与 core 无重叠；旧 game 同键会保留。', '将“当前语言”精确为导出时选定目标语言材料。', '“只遍历默认域”改为“输出条目由默认域决定”。', '哈希空串与数组空串规则不同。'],
 ['不把所有31域/18份语料全部逐记录重审列作本项前提。', '不以所有低层数组方法存在为未来 API 或普通游戏能力承诺。', '不要求重写已有正确的运行 game/core 回退和 GR4 导入归并规则。'],
 ['集中补实际作者收集的哈希过滤、替换/追加、旧同键保留、地图同桶规则。', '静态对照给出更新前后集合；分别绑定替换/追加普通调用者，不能只画抽象低层 API。', '语言导出示例标明目标语言材料，并保留先删后写和稀疏桶既有边界。'],
 ['数组收集入口可登记为可得但未定位普通调用者的补充事实。', '语言独有键不导出的示例可作为澄清；不另计 required。'],
 ['WP08§5 的回退；§6.2 已有从默认消息导出；LZ18–25 预处理/稀疏桶；LZ26–30 同域导入归并。'],
 dict(relation='new_author_default_generation_stage', retained=['GR4-M01-001','GR3-M01-001','GR3-M01-002','GR3-M01-004'],
      explanation='不同入口和状态集合：旧项分别是翻译导入归并、输入行过滤、稀疏导出和电话记录重复。电话终检取最终候选的原 scope 保留；本轮用 GR5-M01-002 说明候选进入默认材料时的过滤，不重开旧项。'),
 ['真实收集、保存、导出及 I/O 失败未执行；不确认任意既有工程中的旧材料状态。'],
 ['Generic Kernel','Demo / Developer Experience']))

records.append(item(3, 'P2', 'required',
 [src(INTL, [[191,239],[397,472],[481,490],[563,587],[600,631],[644,669],[764,823]], '字面收集、转义/导入、规范键与查找/值分离'),
  src('Data/Scripts/016_UI/001_Non-interactive UI/002_UI_Controls.rb', [[8,47]], '实际两段帮助文本传入本地化入口'),
  src('Text_english_core/SCRIPT_TEXTS.txt', [[4085,4093]], '实际导出文本对：键一个换行标记、值两个'),
  src('Data/Scripts/007_Objects and windows/002_MessageConfig.rb', [[787,814]], '备用定义有主入口未定义条件；正常主入口不被它替换')],
 [spec(K+WP08, [[21,32],[42,79],[81,148]], '§3.2/§5/§6；键归一、值转义与导入过滤分层'),
  spec(T+LT, [[110,153]], 'LZ21/22/26/27 及全部邻近向量'),
  spec(U+'wp65-controls-help-appendix.md', [[1,59]], '正文/页面表/本地化依赖/实际调用者未知'),
  spec(T+UT, [[175,183],[602,602]], 'CH01–05、B16-C114'),
  spec('specs/kernel/'+WP08, [[48,53],[63,112],[154,195]], '原稿同义合同及场景'),
  spec('specs/ui/wp65-controls-help-appendix.md', [[19,32]], '帮助内容表，不定义规范键算法'),
  spec(D+'wp75-project-conversion-and-authoring-tools.md', [[18,20],[33,37]], '事件文本规范化与本地化入口责任区分')],
 '“去首尾空白、压缩连续空白”能否自然包含逐行规则？导入行修剪或帮助页内容表能否消除歧义？是否只是排版？',
 '按整串端部修剪再折叠连续空白，会把 A+两个LF+B 变为 A空格B；固定源先处理行边空白，该输入留下一个LF。已读帮助调用和文本对直接支持这一差异。导入内容行修剪在逆转义前，不能替代逆转义后的规范键处理。B16-C114 只限定帮助时序，不给键变换。',
 'required/P2。差异决定命中哪一个翻译键，普通文本身份合同不能只靠一般“空白归一”唯一重建；不是美化或要求保留源控制结构。',
 ['当前语言有效哈希有 A+LF+B→T 与 A空格B→U，正常主入口查询 A+LF+LF+B 得 T。单个内部 LF 保留；两个内部 ASCII 空格归一为一个空格，得 U。',
  '行边空白处理先于剩余连续空白折叠；行边的空白段可跨相邻空行，不能等价改写成逐行 split/trim 后统一 join。用具名结果说明，不复制正则。',
  '键的规范化与值不同：查找不将已存译文的双 LF 折叠；无占位参数的该值按原样交出。'],
 '两个可区分键同时存在，查询 A+LF+LF+B。固定结果 T，整串压缩实现会误取 U。观察在窗口之前，未执行。',
 'A+两个ASCII空格+B 归一为 A空格B；只有单 LF 的键仍可独立命中。',
 ['存储译文值包含两个 LF，查找后仍有两个 LF；不与后续窗口换行处理混同。', '实际帮助文本源含双 LF，随附文本键单 LF/值双 LF；不由此声称该帮助已在 Demo 运行。'],
 '比较对象是逆转义后的键字符串；先行边空白处理，再剩余长度至少二的空白段折叠，最后按规范键查当前语言 game/core。值不走同一键转换。',
 ['最小反例、ASCII 空格正常对照和实际文本证据成立。', '现行 LZ27 只约束双空格碰撞，不能决定 LF 情形。'],
 ['“逐行修剪”仍需解释能跨空行的空白段，否则也是不充分的替代算法。', 'C01 没有独立解码 messages_core.dat，不接收候选对二进制内容的独立验证表述；实际文本和调用已足以支持本结论。'],
 ['不声称全部 Unicode 空白/CRLF/控制字符组合已穷尽。', '不复制实际帮助文案到新规格；用 A/B/T/U 向量和路径追溯即可。', '不把帮助场景源码存在升级为真实 Demo 可达或像素表现。'],
 ['WP08 以行为说明行边处理优先及单 LF 保留；补双LF/单LF/双空格的成对查找结果。', '明确键与译文值两条路径，保留导入预处理和占位替换的既有边界。'],
 ['二进制数据复核可另做，但不是本项静态审查的必需执行。'],
 ['GR4-M01-001 的已碰撞键后值覆盖、LZ27 双空格；GR4-M01-002 占位参数；GR3-M01-001 的导入行过滤；Controls 帮助时序。'],
 dict(relation='new_identity_rule_scope_on_shared_normalizer', retained=['GR4-M01-001','GR4-M01-002','GR3-M01-001','B16-C114'],
      explanation='与 GR4-M01-001 共用规范键阶段，但旧验收只给 ASCII 空格碰撞及碰撞后的后值覆盖；本 ID 增加 LF 身份/运行查找与收集消费者，不否定旧输入结果，也不扩大其历史接受。'),
 ['参考函数与模型未执行；二进制未独立解码；真实帮助调用点和宿主呈现未知。'],
 ['Generic Kernel','User Interface','Demo / Developer Experience']))

records.append(item(4, 'P2', 'required',
 [src('Data/Scripts/010_Data/001_Hardcoded data/008_Stat.rb', [[1,119]], '固定主能力集合及 PBS 位置，和定义顺序区分'),
  src(SPECIES, [[52,111],[175,221],[391,451]], 'BaseStats 数值模式、EVs 具名对、构造与反写'),
  src(TRAINER, [[18,43],[86,101],[129,175],[192,211]], 'IV/EV 可省尾字段、装载与反写'),
  src(CPBS, [[283,330],[388,470],[791,929]], '物种/形态/训练家编译归名和补项/上限'),
  src(WRITE, [[174,283],[454,506]], '反写调用使用字段投影和当前 schema'),
  src(COMP, [[690,737],[742,842]], '可选尾项与写出值序'),
  src('Data/Scripts/020_Debug/002_Editor_DataTypes.rb', [[607,690]], 'IV/EV 编辑顺序与补0，另一输入入口'),
  src('PBS/pokemon.txt', [[3,26]], '默认 BULBASAUR 不等列样本')],
 [spec(K+WP03, [[99,117],[160,195]], '六项复合模式与领域责任'),
  spec(K+WP04, [[58,92],[153,177]], '通用解析与反写'),
  spec(C+WP18, [[47,98],[192,202]], '物种字段/默认、NPC上下文'),
  spec(P+WP19, [[13,28],[77,115],[128,198]], '能力名录、公式向量与个性环序'),
  spec(P+'wp22-transformation-data.md', [[1,77]], '全附表：只限定本表六项数据顺序'),
  spec(D+WP73, [[63,75],[86,108]], '§3.5 “按PBS顺序”、缺省和编辑补0'),
  spec(U+'wp66-a-party-and-summary-ui.md', [[146,159]], '个性描述专用环序'),
  spec(T+ST, [[1,83]], 'ST01–67，尤其 ST60–66'),
  spec(T+DT, [[48,67],[261,261]], 'CE-M09/M11/M20 与 B19-C021'),
  spec(T+UT, [[610,610]], 'B16-C124'),
  spec('specs/creature-rpg/'+WP18, [[48,99],[187,197]], '原稿数据与上下文'),
  spec('specs/pokemon-rules/'+WP19, [[35,213],[274,330],[376,417]], '原稿公式/数值向量/范围'),
  spec('specs/pokemon-rules/wp22-transformation-data.md', [[1,79]], '原稿全附表'),
  spec('specs/demo/'+WP73, [[79,91],[102,125],[196,219]], '原稿复合编辑与场景')],
 'WP22 附表和个性/觉醒力量的顺序是否足以反证“缺列序”？合法等值数据是否根本不受影响？编辑补0是否已决定 PBS 省略尾项？',
 'WP22 的同序表确实正确，且明确说“在本表”；WP19/WP66-A/B16-C124 的同序环是个性消费者。它们不把该序列绑定到通用 BaseStats 或 Trainer IV/EV 文本语法。WP73-A 的“按PBS顺序”没有进一步定义；其补0是编辑返回规则，而源 PBS 尾项缺省重复首项。全部等值确实不会暴露列序错误。',
 'required/P2，收窄为作者数据边界的字段到列映射与 PBS 尾项语义。不能要求重写已正确的 Mega、公式或个性表，也不能把它们称为矛盾。训练家不等列输入是独立决定性消费者。',
 ['BaseStats 和普通训练家 IV/EV 六数值从左到右为 HP、攻击、防御、速度、特攻、特防。',
  '训练家 IV/EV 首值必需；后五项可缺省，缺项取首值，显式 0 保留为 0；整个 IV/EV 字段省略另走装载等级默认。BaseStats 的文本六项均为必需正整数，不能套同一补首值规则。',
  'Species EVs 为具名能力/正数对；编译归入相应能力，输出仍为具名对，不是训练家六列。反写按各自格式，不承诺任意非常规键/坏输入无损。',
  '编辑器未指定字段打开后 BACK 补0仍保持，不能把 PBS 的补首值推广到编辑器。'],
 '原候选 BaseStats=1,2,3,4,5,6 保留：HP1/攻2/防3/速4/特攻5/特防6。另以 Trainer IV 同输入独立复核，不能借 Mega 附表直接推出它。',
 '六项均为 1 时结果均为 1，顺序误用不可见；正常不等列 BULBASAUR 数据对应速度45、特攻65、特防65。',
 ['Trainer IV=1,2：HP1/攻击2，其余四项1；IV=1,0 则攻击0而其它缺项仍1。', 'Species EVs=速度1 为具名产出，不读为六个位置。', 'IV/EV 全字段省略与显式全0及编辑子页补0三者分列；现有 L20 默认10/30保留。'],
 '先按 PBS 列位映射到具名能力，再核 IV 单项31、EV 单项252/合计510；反写恢复相同数值列序。计算公式的展示向量仍使用它自己已声明的序列，不要求内部储存采用任何排列。',
 ['固定列序与训练家补首值成立。', '缺少通用作者输入与具体序列的明确绑定。', 'WP22 与个性表已有正确的同序数据，是必须保留的反证。'],
 ['原候选不得概括成“全套规格没有该顺序”。', '“尾项省略”属于 Trainer IV/EV；不推广到 BaseStats，且编辑缺项补0已正确。', '受影响文件无需机械扩为全部消费者：集中作者输入表加引用即可。'],
 ['不以能力名录列法不同就判公式或展示顺序错误。', '不按参考登记容器设计未来类/数组；仅外部文本顺序有兼容意义。', '不合并到006：004是编译输入归名，006是成员生成后的覆盖。'],
 ['在作者数据主责位置给 BaseStats/Trainer IV/EV 列位绑定及 Species EVs 区别，WP73-A 可引用。', '至少一个六项不等、一个省略尾项、一个显式0与一个全字段省略静态对照。', '保留现有公式向量、Mega表、个性环和编辑BACK补0；不需要改它们的正确数值。'],
 ['等值负控可保留为说明顺序错误为何不总显现，无须扩展全量公式测试。'],
 ['WP22全附表；ST60–67；B16-C124；B17-PA040 的设施EV例外；B19-C021 编辑返回语义。'],
 dict(relation='new_PBS_consumer_of_known_stat_identity', retained=['B16-C124','B17-PA040','GR-016'],
      explanation='已有顺序在个性/形态表消费者接受，不构成通用 PBS/训练家列映射的接受。用 GR5-M01-004 标记新消费者，保留旧scope，不重开已正确表。'),
 ['未运行编译/编辑器/反写；新增主能力、插件和任意坏字段不在结论内。'],
 ['Demo / Developer Experience','Creature-RPG','Pokémon Rules']))

records.append(item(5, 'P3', 'required',
 [src(STORAGE, [[1,77],[120,264],[269,370],[387,400]], '容量、寻址、首空位、实际扫描消费者、地区代理'),
  src('Data/Scripts/001_Settings.rb', [[215,225]], '队伍6、盒40、默认治疗关闭'),
  src('Data/Scripts/016_UI/017_UI_PokemonStorage.rb', [[1705,1755],[1964,2021]], '实际 UI 取出/存入和特殊负位置选择，区分正常到达能力')],
 [spec(C+WP25, [[1,218]], '全文，尤其§3.1–3.2、§4.1、§7–8'),
  spec(U+WP66, [[1,110],[219,235],[250,271]], '选择模式−2寻址、领域委托与未决范围'),
  spec(T+CT, [[162,208]], 'PS01–42，负目标格不等于负盒号'),
  spec('specs/creature-rpg/'+WP25, [[1,97],[140,161],[197,250]], '容量函数、自动找位和场景'),
  spec('specs/ui/'+WP66, [[28,42],[250,301]], '§2.2 与 B36 原正确范围')],
 '是否只是未承诺的低层非法参数？WP66-B 对−2真实盒的正向例外能否消除 WP25 的全部矛盾？普通 UI 是否会扫描该负盒号？',
 'WP25§3.1 已对容量查询给“≥盒数→0、−1→6、否则当前长度”的分段合同，§3.2又把盒子首空位概括为全长度，未排除其他负盒号。WP66-B只解释寻址，不解释容量，因此不能修正该分段。另一方面，已读普通存入选择要求目标盒非负，选择模式的特殊负位置取出也不等于对负源盒调用首空位；没有证明普通 UI 触发候选扫描。',
 '从 P2 降为 required/P3：只修正已存在的过宽容量/扫描陈述及一个局部例。不能以公开方法可调用为由强制未来新增负索引接口或完整负参数行为族。',
 ['基础储存容量查询：盒号≥盒数返回0；其余负盒号返回队伍上限；非负有效盒号取该盒当前长度。它不因此验证负盒号实际可寻址。',
  '成员寻址只把−1当队伍；−2在40盒中寻址零基38盒。首空位查询仅−1走队伍长度分支，其余按容量查询结果扫描该地址。',
  '盒38长30，零基格0–5占用、格6为空：以−2查询首空位得到−1；以38查询得到6。单独读取[-2,-1]仍指盒38格29，不受容量6截断。'],
 '默认40盒×30格、上限6，直接查询容量−2得6；原候选成立，但仅是局部接口观察。',
 '容量38得30，容量−1得6；无空洞队伍长度2时−1首空位为2。',
 ['−2扫描与38扫描面对同一盒可返回−1/6。', '盒号40容量0，首空位−1。', '更小负号可得到容量6却没有可寻址盒；不因此承诺首空位成功返回。'],
 '先容量上界判断，再负号分支；首空位−1特例早于该扫描。容量、容器长度、成员寻址和负格索引是四个不同观察点。',
 ['源的6/30差异和前六格反例成立。', 'WP25 现有明确“否则”分段与该输入不同。', 'WP66-B 负位置寻址事实本身正确。'],
 ['严重度降P3；没有普通存入误行为的证据。', 'M01将 WP25§7–8锚到138–153行不准确；当前对应167–187行。此是锚点校正，不另立必修。'],
 ['不认定正常 UI 必然使用−2作为自动存入目标。', '不要求未来提供同名公开 API 或所有负号兼容；修订可明确局部入口与作用域。', '不把全部负盒号统一改作队伍，也不抹掉 WP66-B 已接受寻址异常。'],
 ['修正容量表与自动首空位的适用分支；给−2/38/−1的最小成对观察。', '明确这一局部事实不证明普通 UI 可达，不扩大选择模式后续消费者的既有未决。'],
 ['非法负盒号全集不作验收；若未来架构不暴露该接口，不要求创造它。'],
 ['正常非负盒当前长度、清空语义、PS01–42、WP66-B B36的−2寻址、地区代理原scope。'],
 dict(relation='new_capacity_consumer_scope_adjacent_to_negative_addressing', retained=['WP66-B/B36','B16-C120'],
      explanation='旧 B36 仅证明寻址与位置返回；本轮容量/扫描不否定该事实。墙纸负数/旧文本问题是另一输入，保持旧接受。'),
 ['未执行容器或 UI；实际事件/插件传入负目标盒的可达性未知。'],
 ['Creature-RPG','Demo / Developer Experience']))

records.append(item(6, 'P2', 'required',
 [src(TRAINER, [[18,43],[86,101],[113,178]], '输入可省字段、记录构造不填这些值、装载覆盖完整顺序'),
  src('Data/Scripts/010_Data/002_PBS data/014_TrainerType.rb', [[18,30],[101,123]], '类型性别解析和男性谓词'),
  src('Data/Scripts/010_Data/001_GameData.rb', [[78,145]], '登记键序列/枚举/计数'),
  src('Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb', [[1,173]], '固定25身份顺序'),
  src('Data/Scripts/010_Data/001_Hardcoded data/002_GenderRatio.rb', [[1,83]], '混合/固定性别门'),
  src(POKEMON, [[1,28],[340,383],[389,464],[496,522],[1099,1127],[1153,1227]], '普通创建缓存、性别/特性/异色/性格设置门与重算'),
  src('Data/Scripts/015_Trainers and player/001_Trainer.rb', [[25,53]], '训练家男性查询确实来自类型'),
  src('Data/Scripts/015_Trainers and player/002_Trainer_LoadAndNew.rb', [[1,10]], '普通装载包装'),
  src('Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb', [[531,590]], '战斗装载调用及之后的装载钩子'),
  src('Data/Scripts/012_Overworld/002_Battle triggering/004_Overworld_EncounterModifiers.rb', [[62,73]], '本固定源装载钩子模板为注释，不冒充已启用'),
  src('PBS/trainers.txt', [[74,83]], 'COOLCOUPLE两成员省略字段'),
  src('PBS/trainer_types.txt', [[269,274]], 'COOLCOUPLE Unknown'),
  src('PBS/pokemon.txt', [[10226,10249],[10301,10325]], '两个成员均为比例性别物种，无固定性别守卫')],
 [spec(C+WP18, [[158,202]], '§4.1–4.3普通创建与NPC覆盖'),
  spec(C+WP24, [[45,54],[81,85],[141,164]], '身份性别、装载委托'),
  spec(P+WP19, [[39,115],[140,174],[217,268]], '所有相关派生/设置/固定Nature/训练家IV EV及未知'),
  spec(D+WP73, [[63,75],[86,108]], '编辑省略/显式0，不是装载默认'),
  spec(T+CT, [[1,37],[88,119]], 'CI01–28；PT装载/身份原向量'),
  spec(T+ST, [[31,43],[49,83]], '普通派生与缓存向量，不是NPC最终值'),
  spec(T+DT, [[261,261]], 'B19-C021 IV/EV旧范围'),
  spec(D+'wp77-demo-evidence-and-capability-coverage.md', [[100,106]], '实际训练家数据目录，只列显式全字段样本'),
  spec('specs/creature-rpg/'+WP18, [[153,197],[334,361]], '原稿创建、覆盖与场景'),
  spec('specs/creature-rpg/'+WP24, [[136,159],[286,318]], '原稿装载及场景'),
  spec('specs/pokemon-rules/'+WP19, [[61,140],[175,185],[313,330],[376,410]], '原稿默认派生及上下文'),
  spec('specs/demo/'+WP73, [[79,91],[102,110]], '原稿编辑缺省语义')],
 '按数据覆盖是否暗含这些省略默认？普通创建派生、训练家性别字段与完整Nature表能否补齐？SuperShiny/Shadow顺序会否反驳一般最终值？',
 '记录构造并未把省略的性别/特性槽/异色字段填成候选值，它们在普通个体创建之后才确定写入；因此“按数据覆盖”无法推出缺省也会覆盖。固定 Nature表只给选中索引到身份，不给物种/类型索引来源。WP19 已正确给单性别守卫与超级异色写入联动，应直接保留。源还在后段对 Shadow 写普通异色假。',
 'required/P2；普通默认 NPC 数据确实受影响。收窄到装载返回、无后续钩子覆写的结果；补默认覆盖，不重写普通创建与既有IV/EV数学。',
 ['普通记录转成NPC成员时先创建个体；随后缺省 AbilityIndex 写0，再应用显式 Ability（省略则清除显式特性缓存）。因此槽0不排斥另有显式特性覆盖。',
  '省略 Gender：男性训练家类型尝试设男，非男性类型尝试设女；比例物种生效，固定性别/无性别物种设置被忽略。COOLCOUPLE 的 Unknown 仍为训练家类型2，不被改成女；其两个比例性别成员最终为女。',
  '先写普通异色为给定真值/否则假，再写超级异色为给定真值/否则假。超级真会把普通置真；若后段 Shadow 为真，又把普通异色置假。两字段都省略时均为假。',
  '省略 Nature：取基物种身份在当前完整物种登记键序列中的零基位置 iS、训练家类型在其登记键序列中的零基位置 iT；按 (iS+iT) mod N 选择当前 Nature登记序位置（固定N=25）。不是全国编号，也不把物种表先过滤为仅基础形态再编号。',
  '现有默认 IV=min(floor(L/2),31)、EV=min(floor(3L/2),85)及最终重算保持。'],
 '实际 COOLCOUPLE/Alice & Bob、TURTWIG与CHIMCHAR，成员未写Gender；普通装载正常返回且无改写时，两只均为女。未执行实际创建。',
 '同一比例物种显式Gender=Male得男；男性训练家省略Gender也得男；原训练家类型性别保持自己的值。',
 ['固定无性别物种不接受缺省女覆盖。', '合法双自然特性物种、没有显式Ability、缺省AbilityIndex，即使普通创建PID为奇数，覆盖后槽仍0。', 'Shiny省略而SuperShiny真且非Shadow：普通/超级均真；再令Shadow真则普通假，不能无条件说超级真蕴含最终普通真。', '给定合法登记位置iS=0、iT=1，N=25，缺省Nature选第1项LONELY；这是明确的人工位置夹具，不冒充默认随附NPC的实际性格。'],
 '普通随机创建 → 可选形态/招式 → 特性槽再特性 → 性别 → 普通异色再超级异色 → Nature（会重算）→ IV/EV → 可选Shadow及普通异色覆盖 → 球 → 最终重算；只保留对最终值有意义的顺序。',
 ['缺省槽0、非男类型成员尝试女、双异色缺省假及登记位置Nature公式成立。', '实际COOLCOUPLE材料和比例性别前提成立。', 'WP19设置守卫、固定Nature身份及既有IV/EV公式正确。'],
 ['默认槽不等于无条件最终自然特性；显式Ability可覆盖。', '“SuperShiny真可影响普通异色”要补后段Shadow例外和观测时点。', 'Nature位置来自当前完整键序列，不规定未来内部容器。', '原 M01 的WP24锚点应落§5的141–164行，而非较早金钱结算范围。'],
 ['不改变训练家类型Unknown身份。', '不把不经普通数据装载的外部预建NPC/设施模板全部纳入。', '不要求追踪运行随机抽样、宿主可达性或任意扩展重排结果。', '不把IV/EV已有默认重新报为缺失。'],
 ['WP18 NPC上下文给省略/显式字段/最终覆盖的有界表，WP24只需引用。', 'Nature注明两个零基登记位置与取余，沿用WP19固定身份表。', '向量覆盖实际Unknown类型、男性/显式Male、固定性别守卫、缺省槽、双异色与Shadow先后。', '保持IV/EV、普通创建缓存、装载钩子可覆写以及失败不回滚的原边界。'],
 ['无需把全部成员字段复制成新的具体API，也不要求所有默认训练家逐一生成验证。'],
 ['WP19普通创建派生和单性别守卫；Nature表；B19-C021未打开/打开BACK区别；B17设施模板分配；B21 CHAIN-1/5。'],
 dict(relation='new_NPC_post_creation_consumer_scope', retained=['WP18创建缓存旧scope','B19-C021','B17-PA040','B21/CHAIN-1','B21/CHAIN-5'],
      explanation='普通创建、编辑补0、设施均分和伙伴/Shadow链均保留，只补普通NPC装载的后续覆盖。与004共用Trainer文件但状态阶段和修复条款不同，不机械合并。'),
 ['未执行随机创建、战斗装载或宿主；具体默认NPC性格数值未计算/执行；外部钩子覆写不在保证内。'],
 ['Creature-RPG','Pokémon Rules','Demo / Developer Experience']))

records.append(item(7, 'P3', 'optional',
 [src(DEBUG, [[1423,1455]], '语言存在门、作者选择、取消在导出器之前'),
  src(INTL, [[244,290],[291,372],[492,529]], '独立目标语言材料读取，不修改运行消息实例')],
 [spec('analysis/inventory/wp02_build_appendix.py', [[1,44],[135,158],[175,191]], '辅助生成器默认目标、固定语言行与写出'),
  spec('analysis/inventory/out/wp02-settings-inventory-appendix.md', [[193,201]], '旧输出§7.3'),
  spec('specs/kernel/wp02-settings-inventory-appendix.md', [[193,201]], '有效附表§7.3已正确'),
  spec(K+'wp02-rule-configuration-and-data-variants.md', [[238,244]], '正式§6.3'),
  spec(K+WP08, [[34,40],[90,108]], '正式语言选择和作者导出'),
  spec(T+KT, [[13,14]], 'KC05/06'),
  spec(T+LT, [[126,129]], 'LZ13–16 玩家切换/取消/成功导出对照'),
  spec('specs/kernel/wp02-rule-configuration-and-data-variants.md', [[283,290]], '原稿§6.3已正确'),
  spec('specs/kernel/'+WP08, [[55,61],[99,112]], '有效原稿已明确作者目标'),
  spec(D+'wp72-debug-contexts-and-controls.md', [[265,274]], '调试导出入口')],
 '材料是否有效？旧输出是否仍能反证正式规格？是否应自动从optional升required？未来重生成风险是否被当成当前事实？',
 '固定辅助脚本和 analysis/out 确实仍含错误角色说明；有效 specs附表及正式WP02/WP08、KC06/LZ15–16都已正确。C00将旧输出归 superseded_generated_inventory、脚本归 audit_generation_utility。脚本默认输出还指向Desktop原稿位置，但本任务未运行；不能把未来误运行风险改写为当前正文已经回归。',
 '保持 optional/P3；正式规格 no_required_revision。可维护辅助固定说明，但不要求改历史旧输出或重新生成，也不重开已正确语言合同。',
 ['作者候选存在且当前运行语言A，选择导出B后取消core/game：未到导出器，玩家语言/运行消息仍A，无导出写入。',
  '成功导出时只用B作为目标目录/译文材料选择，运行语言A保持。默认LANGUAGES为空时，入口先提示并返回，不能假设固定默认配置本身可选择B。',
  '若辅助生成器执行并成功到写出，现有固定行仍会称该调试入口为语言切换；本次只证明文本漂移，不证明曾重新生成或覆盖过有效附表。'],
 '静态比较生成器第156行/旧输出第200行与有效附表第200行，角色不同；没有生成执行。',
 '有效正式WP02§6.3、WP08§4/§6.2及KC06/LZ15–16均与参考作者导出路径一致。',
 ['LANGUAGES为空早返回。', 'A/B候选存在时选B再取消，与成功导出B、玩家载入菜单切换B分开。'],
 '作者选择 → 可取消类别/地图分组 → 新的目标语言材料读取 → 输出；运行消息集与玩家语言均不是这条路径的写入目标。',
 ['辅助固定行与旧输出有真实语义漂移。', '现行正式正文及有效附表正确，旧生成物不是同字节副本。'],
 ['辅助旧输出应按其被替代身份看待；不把维护同步当作正式必修。', '可选维护应优先改将来仍使用的生成说明；历史生成物可留原样并由已有身份分类隔离。'],
 ['不升required；不修改已正确正式条款。', '不启动生成器或update，不更改全局配置。', '不因本项要求改写历史审计包或恢复原稿中的旧错误。'],
 [],
 ['维护者继续使用该辅助生成器时，可同步第156行的作者导出角色说明；如需新输出，另在授权目录生成并与有效附表核对。'],
 ['WP02/WP08有效语言合同、KC06/LZ15–16、C00的材料有效性分类。'],
 dict(relation='auxiliary_drift_only_no_reopening', retained=['WP02§6.3','WP08§4/§6.2','KC06','LZ15–16','C00 supplemental-scope'],
      explanation='旧纠正已在有效正文和附表生效；本轮仅可选维护辅助材料，不再计为正式语言能力缺口。'),
 ['是否继续维护该生成器由维护者决定；未重生成、未执行UI；不认证未来运行会成功。'],
 ['Demo / Developer Experience']))

candidate_path = HERE.parent/'M01'/'findings.json'
candidate_bytes = candidate_path.read_bytes()
candidates = json.loads(candidate_bytes)['findings']
by_id = {x['id']: x for x in candidates}
for rec in records:
    old = by_id[rec['id']]
    rec['original_candidate'] = {
        'path': '../M01/findings.json',
        'json_pointer': '/findings/'+str(candidates.index(old)),
        'file_sha256': hashlib.sha256(candidate_bytes).hexdigest(),
        'object_sha256': hashlib.sha256(json.dumps(old,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
        'title': old['title'], 'disposition': old['disposition'], 'severity': old['severity'],
        'expected_reference_behavior': old['expected_reference_behavior'],
        'minimal_counterexample': old['minimal_counterexample'],
        'mutation': 'NONE; original candidate retained and not silently rewritten'
    }

base = dict(schema_version='gr5.c01.counterevidence.v1',
    reviewer={'id':'C01','role':'fifth-round targeted independent counterevidence reviewer',
              'independent_of':'M01 proposer','task':'逐项独立反证 GR5-M01-001–007'},
    task_identity='fifth-2026-10-13-9366d9d-c7d3/modules/C01',
    specification_baseline={'commit':B5,'formal_root':F},
    source_baseline={'root':R,'commit':RC,'tree':RT,'access':'read_only'},
    model_request={'model':'gpt-6-astra','reasoning_effort':'ultra','service_tier':'default','fast':False,
                   'actual_echo':'UNVERIFIED','verification':'No quota/authentication/private-session/backend audit and no global configuration change'},
    authority='C01 recommendations only; parent final adjudication remains separate',
    execution_status={'reference':0,'behavior_model':0,'host_or_demo':0,'generator':0,
                      'performed':'read-only text/JSON/git-object inspection and C01 artifact structural checks only'},
    original_candidates_preserved=True, independent_rebuttal_rounds=1,
    global_feature_matrix='NOT_MODIFIED; classification and bounded findings are handed off locally',
    recommendations=records)

supp = [
 dict(path='../C00/supplemental-scope.json', pointers=['/rules','/explicit_current_case_files','/explicit_audit_navigation','/fixed_effective_files'], role='effective-material routing, not inherited PASS'),
 dict(path='../M01/parent-note.md',ranges=[[1,1]],role='parent execution notice read; no C01 execution claim or dependence on its PASS'),
 dict(path='review/remediation/20261003-prepare/batches/B16/author-draft-1/traceability.json',
      pointers=[f'/trace/{i}/{k}' for i in [12,16,17,20] for k in ['current_qualified_controls_full','catalog']],
      relevant_ids=['B16-C114','B16-C120','B16-C121','B16-C124'],
      assessment='实际约束分别为帮助时序、墙纸显示写入、尺寸显示与个性环；均不补本轮的键语法/容量/浮点/PBS列位绑定。'),
 dict(path='review/remediation/20261003-prepare/batches/B17/author-draft-1/static-cases.json',
      pointers=['/records/'+str(i) for i in [0,1,6,7,8]],
      assessment='架构中立保留可观察身份；设施模板255/170分配不能替代普通Trainer六列输入及缺省覆盖。'),
 dict(path='review/remediation/20261003-prepare/batches/B21/author-draft-1/static-cases.json',
      revision='e58486178e746273fb6fab55df00722807f1dc44',pointers=['/cases'],
      assessment='14项实际前提/预期已读；输入类别分派、设置附表审计归属和旧批准边界不补上述行为缺口。'),
 dict(path='review/remediation/20261003-prepare/batches/B21/author-draft-1/eight-chains.json',
      revision='e58486178e746273fb6fab55df00722807f1dc44',
      pointers=[f'/chains/{i}/{k}' for i in [0,4,5] for k in ['current_accepted_sequence_and_conditions','neighboring_contrast_and_partial_failure']],
      assessment='只读相关伙伴、形态/Shadow、编辑/编译/登记/缓存链限定；不递归历史整包，不继承整链PASS。'),
 dict(path='review/remediation-fourth-20261012-prepare/tasks/R4-U01/findings-input.json',
      pointers=[f'/canonical_root_records/{i}/{k}' for i in [0,1] for k in ['id','title','preconditions','minimal_counterexample','acceptance_criteria','excluded_claims']],
      assessment='GR4-M01-001/002的实际输入和验收读取，分别保留导入归并和占位参数scope。'),
 dict(path='review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/M01/report.md',
      revision='df5887f244fa4a5e7200f36a722357bb063f2395',ranges=[[1,85]],
      assessment='该固定报告新增2项GR4；其“四项CLOSED”明确指GR3-M01-001–004。保持两组原scope，不能按模糊称谓扩大历史接受。'),
 dict(path='review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/M01/findings.json',
      pointers=[f'/{i}/{k}' for i in range(4) for k in ['id','premises','scenarios']],
      assessment='行过滤、稀疏导出、PBS井号、电话默认重复的具体输入/对照已读，原结论保留。'),
 dict(path='review/remediation-fourth-20261012-prepare/tasks/R4-U01/legacy-navigation.json',
      pointers=['/historical_optional','/historical_no_revision','/affected_regression_contract/0','/affected_regression_contract/1'],
      assessment='GR3-M09-001 DEFERRED、GR3-M02-003 NO_REQUIRED_REVISION；旧原始candidate标签不覆盖后续限定。')
]

def aggregate(field):
    out = {}
    for rec in records:
        for entry in rec[field]:
            key=(entry['path'],entry['revision'])
            if key not in out:
                out[key]=dict(entry, ranges=[], finding_ids=[], scope_descriptions=[])
            row=out[key]
            row['finding_ids'].append(rec['id'])
            row['ranges'].extend(entry['ranges'])
            row['scope_descriptions'].append(entry.get('semantic_scope',entry.get('section_or_vector')))
    for row in out.values():
        merged=[]
        for a,b in sorted(row['ranges']):
            if merged and a<=merged[-1][1]+1: merged[-1][1]=max(b,merged[-1][1])
            else: merged.append([a,b])
        row['ranges']=merged
        row['finding_ids']=sorted(set(row['finding_ids']))
        row['scope_descriptions']=list(dict.fromkeys(row['scope_descriptions']))
    return list(out.values())

coverage=dict(schema_version='gr5.c01.reading-coverage.v1',reviewer='C01',
    specification_baseline=base['specification_baseline'],source_baseline=base['source_baseline'],
    coverage_unit='actual relevant semantic ranges; not whole-module or whole-repository PASS',
    source_directly_read=aggregate('source_directly_read'),
    spec_directly_read=aggregate('spec_directly_read'),supplements_and_history_directly_read=supp,
    candidate_read={'path':'../M01/findings.json','pointers':['/findings/'+str(i) for i in range(7)],'all_seven_read':True},
    search_assessment=[
      {'scope':'fixed R Data/Scripts','topics':['primary/fallback localization definitions','numeric converter/validator definitions','storage capacity and regional forwarders','trainer load and hooks','message collection callers'],'result':'Located definitions and necessary callers were directly read; conditional fallback and regional forwarding distinguished; no blanket dynamic-override absence claim.'},
      {'scope':'deliverables/final-specification-set + specs','topics':['float/Height/Weight/尺寸','BaseStats/PBS顺序/六项/个性','default/core/game/规范键/翻译','负盒号/容量/寻址','NPC省略/性格/性别/特性'],'result':'Search used only for navigation; contract conclusions depend on the listed body/table/vector/original ranges and effective supplemental clauses.'}],
    exclusions=['No full corpus of 31 message domains/18 text files was re-audited.','No binary messages_core.dat decoding by C01.','No recursive historical package review; only bounded accepted controls/cases listed.','No behavior execution or source/model probes.','Source and spec ranges denote reading, not runtime verification.'],
    request_log_limit='read-log.jsonl is a mechanical requested-range log; early combined outputs were truncated and relevant missing spans were reread. The curated per-finding ranges in this file and resolution.json are the authoritative semantic coverage. Original WP03/WP04 comparisons also used exact equal-text spans against already-read formal text; distinct original spans were read.',
    completed_ids=[r['id'] for r in records],complete=True)

counts={k:sum(r['disposition']==k for r in records) for k in ['required','optional','no_required_revision','unresolved']}
base['counts']=dict(counts,required_P2=sum(r['disposition']=='required' and r['severity']=='P2' for r in records),required_P3=sum(r['disposition']=='required' and r['severity']=='P3' for r in records))
base['supplemental_scope_assessment']=supp
base['completion']='all 7 candidates directly read and independently rebutted; one bounded integration completed'

def dump(path,obj):
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

dump(HERE/'resolution.json',base)
dump(HERE/'reading-coverage.json',coverage)

lines=['# C01 定点独立反证报告','',
 '7/7 候选已完成一次独立反证与有限整合。以下为 C01 建议，父会话最终裁决另行进行；没有修改 M01 候选或正式规格。', '',
 '| 原 ID | 建议 | 本轮收窄／排除 |','| --- | --- | --- |',
 '| GR5-M01-001 | required / P3 | 从P2降级；仅活跃PBS浮点边界；基础缺省与形态继承分开 |',
 '| GR5-M01-002 | required / P2 | 必修限定默认哈希材料生成；导出集合已有同义基础，数组低层收集不单独强制 |',
 '| GR5-M01-003 | required / P2 | LF键身份差异成立；不泛化全部空白，不继承二进制或宿主验证 |',
 '| GR5-M01-004 | required / P2 | 补通用PBS列位与尾项；Mega表、公式和个性表本身正确 |',
 '| GR5-M01-005 | required / P3 | 从P2降级；只纠正已写容量合同，不证明普通UI会触发负盒扫描 |',
 '| GR5-M01-006 | required / P2 | 补NPC装载后覆盖；保留单性别、显式特性、SuperShiny后Shadow例外 |',
 '| GR5-M01-007 | optional / P3 | 辅助材料漂移成立；正式正文与有效附表 no_required_revision |','',
 '**身份和执行边界。** B5为`'+B5+'`，正式根`'+F+'`。只读R根`'+R+'`，commit`'+RC+'`、tree`'+RT+'`。身份沿用任务给定，不重复行政审计。请求gpt-6-astra / ultra / default / 非Fast；实际参数回显 **UNVERIFIED**。未查额度、认证、私有会话或后端，未改全局配置，未启动其他agent/会话，未提交、推送、安装、update。', '',
 '本次只进行了源/规格静态阅读、JSON与Git对象只读解析以及本目录产物结构检查；参考、行为模型、宿主/Demo、生成器执行数均为0。M01父注中的执行告知仅作范围信息，不冒充C01亲自执行，也不以其PASS代替独立反证。', '',
 '**材料与历史。** 已按C00识别读取B16的相关限定控制与当前测试、B17相关静态前提，以及固定Git对象中的B21实际案例和相关链条。没有递归历史整包。第四轮M01固定报告新增2项GR4，并在回归表保留GR3-M01的四项；这里按精确ID保留两组原scope。GR3-M09-001仍DEFERRED，GR3-M02-003仍NO_REQUIRED_REVISION。详细已读范围和关系分别见[reading-coverage.json](reading-coverage.json)、[resolution.json](resolution.json)。','']
for rec in records:
    lines += ['## '+rec['id']+' — '+rec['original_candidate']['title'],'',
              '**建议：'+rec['disposition']+' / '+rec['severity']+'。** '+rec['rebuttal']['conclusion'],'',
              '**反证问题。** '+rec['rebuttal']['challenge'],'',
              '**实际反证材料。** '+rec['rebuttal']['counterevidence'],'',
              '**最小反例。** '+rec['minimal_counterexample'],'',
              '**正常对照。** '+rec['normal_case'],'',
              '**状态／顺序／数学。** '+rec['state_order_math'],'',
              '**需纠正的候选表述。** '+' '.join(rec['facts_needing_correction']),'',
              '**保留与排除。** '+' '.join(rec['excluded_claims'])+' 已正确范围：'+'；'.join(rec['acceptance_adjustments']['preserve'])+'。','',
              '**验收收窄。** '+(' '.join(rec['acceptance_adjustments']['required']) if rec['acceptance_adjustments']['required'] else '没有正式必修验收项。')+' '+ ' '.join(rec['acceptance_adjustments']['optional']),'',
              '**历史关系。** '+rec['history_relation']['explanation'],'',
              '**证据限制。** '+' '.join(rec['unknowns'])+' 源事实为高置信静态结论；严重度为审者判断。','']
lines += ['## 交付与检查','',
          '产物：[逐项裁定](resolution.json)、[实读覆盖](reading-coverage.json)、[进度](progress.json)。原候选标题、建议前状态、原预期和最小反例保存在逐项original_candidate中，附原对象摘要身份；修正另列，没有静默替换。', '',
          '结构检查只确认7个原ID一一对应、所需字段齐全、源与规格锚点非空、限定目录输出及JSON可解析；不计为行为测试。全局Feature Matrix未写，分类与必修范围由本目录交父会话汇总。']
(HERE/'report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

# This is artifact consistency validation, not a reference implementation/model.
assert len(records)==7 and len(by_id)==7
assert {x['id'] for x in records}==set(by_id)
for rec in records:
    assert rec['source_directly_read'] and rec['spec_directly_read']
    assert rec['independent_rebuttal_complete']
    assert rec['disposition'] in {'required','optional','no_required_revision','unresolved'}
    for key in ['rebuttal','corrected_expected_behavior','accepted_claims','excluded_claims',
                'acceptance_adjustments','history_relation','execution_status','confidence','unknowns']:
        assert key in rec
for name in ['resolution.json','reading-coverage.json']:
    json.loads((HERE/name).read_text())
dump(HERE/'progress.json',dict(schema_version='gr5.c01.progress.v1', reviewer='C01',
    task_identity=base['task_identity'],complete=True,completed_ids=[r['id'] for r in records],
    counts=base['counts'],model_request=base['model_request'],
    execution_status=base['execution_status'],
    stage='all_seven_rebuttals_and_bounded_integration_complete',
    remaining_required_work=[],parent_adjudication='pending; this artifact is not a global acceptance',
    artifacts=['report.md','resolution.json','reading-coverage.json','progress.json'],
    structural_checks='PASS: JSON parse, seven exact IDs, required fields, nonempty direct anchors; no behavioral PASS claimed'))
print(json.dumps({'written':['report.md','resolution.json','reading-coverage.json','progress.json'],'counts':base['counts'],'complete':True},ensure_ascii=False))
