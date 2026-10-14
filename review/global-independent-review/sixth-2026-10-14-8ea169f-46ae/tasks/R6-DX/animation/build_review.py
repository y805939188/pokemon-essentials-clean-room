from pathlib import Path
import json,hashlib
r=Path(__file__).parent
base='reference/pokemon-essentials/Data/Scripts/'
spec='deliverables/final-specification-set/demo-dx/wp74-battle-animation-authoring-and-exchange.md'
cat='deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md'
S=base+'020_Debug/002_Animation editor/001_AnimEditor_SceneElements.rb'
C=base+'020_Debug/002_Animation editor/002_AnimEditor_ControlsButtons.rb'
I=base+'020_Debug/002_Animation editor/003_AnimEditor_Interpolation.rb'
E=base+'020_Debug/002_Animation editor/004_AnimEditor_ExportImport.rb'
F=base+'020_Debug/002_Animation editor/005_AnimEditor_Functions.rb'
P=base+'011_Battle/007_Other battle code/007_BattleAnimationPlayer.rb'
U=base+'020_Debug/001_Editor_Utilities.rb'
B=base+'020_Debug/003_Debug menus/003_Debug_MenuExtraCode.rb'
O=base+'020_Debug/001_Editor screens/001_EditorScreens.rb'
K=base+'010_Data/002_PBS data/001_MiscPBSData.rb'
Q=base+'021_Compiler/002_Compiler_CompilePBS.rb'
BC=base+'011_Battle/004_Scene/004_Scene_PlayAnimations.rb'
BT=base+'007_Objects and windows/008_AnimatedBitmap.rb'
RTP=base+'001_Technical/002_Files/001_FileTests.rb'
W=base+'007_Objects and windows/005_SpriteWindow_text.rb'
def loc(path,a,b,clause=None):
 d={'path':path,'lines':[a,b]}
 if clause:d['clause']=clause
 return d
findings=[]
def finding(n,title,severity,source,formal,preconditions,normal,counterexample,cancel_exception,negative_scope,impact,proposal,sync,acceptance,dependencies):
 findings.append({'id':f'R6-DX-AN-{n:03d}','status':'PROPOSED_PENDING_NON_AUTHOR_COUNTEREVIDENCE_AND_ROOT_RULING','title':title,'severity':severity,'evidence_level':'STATIC_SOURCE_REASONING_NOT_EXECUTED','source':source,'formal':formal,'preconditions':preconditions,'ordinary_control':normal,'minimal_counterexample':counterexample,'cancel_exception_partial_commit':cancel_exception,'negative_evidence_scope':negative_scope,'impact':impact,'minimal_revision_scope':proposal,'synchronization_files':sync,'acceptance':acceptance,'dependencies':dependencies})
finding(1,'最后个体删除门的计数只覆盖0–59；槽60不计入', 'P2',
 [loc(S,678,694,'deletable?'),loc(S,652,658,'deleteCel'),loc(S,810,834,'TAB与DELETE'),loc(F,1069,1074,'重编号入口')],
 [loc(spec,118,123,'§4.4第三/四支'),loc(spec,188,200,'§6.3范围表'),loc(cat,116,116,'AN-M05'),loc(cat,282,282,'B20-C025')],
 '正常编辑器、有效帧；两使用者图案分别存于槽0和槽60；要删除的槽0未锁。槽60可由复制槽0→粘贴至2→重编号到60正常形成，无插件/损坏数据。',
 '两使用者位于槽0和2且都未锁：计数2，DELETE槽0允许。只有常规槽0一个使用者时，计数1拒绝。',
 '把第二使用者从2交换到60后，帧仍存两个使用者，但常规计数只有1；解锁并DELETE槽0被拒绝。正文按“当前帧同图案单元数”及AN-M05未限定范围会推导允许。',
 '拒删不改变任何槽。重编号取消不产生60状态。Clear入口也调用同一计数门，拒删会重置目标而非清除；未保存对象的缓存可见性仍按§3.2。',
 '完整读取SceneElements1–1012、Functions1–1170和Player1–844；检查TAB实际存储长度、重编号消费者、普通删除/键盘DELETE/Clear。没有另一个包含60的计数补偿。',
 '参考删除保护与实际存储项数不等价；当前槽60参与存在/锁定/图案判断，但它以及其它60以后槽不进入保护计数。',
 '仅把§4.4计数定义改为当前帧0–59中该图案次数；§6.3加删除保护计数范围。不要改现有60的存储、键盘可达或复制合同。',
 [spec,cat,'specs/demo/wp74-battle-animation-authoring-and-exchange.md','对应追溯/覆盖记录（root裁决后同步）'],
 '非提出者回读678–691并沿普通可达的复制/粘贴/重编号验证上述正反例；保留既有常规最后个体保护和槽60回换恢复。',
 ['§4.4','§4.5','§6.3','私有剪贴快照','未执行宿主'])
finding(2,'槽替换后Cel Focus仍写集合成员，不写画布持有的旧动画','P2',
 [loc(F,168,173,'列表Delete替换'),loc(F,1106,1120,'Cel Focus读写集合选中槽'),loc(S,717,727,'新增单元读画布动画焦点'),loc(E,27,45,'导出集合选中槽')],
 [loc(spec,56,56,'§3.2画布脱离'),loc(spec,209,210,'§7.1 Delete/BACK'),loc(spec,222,224,'§7.4焦点'),loc(cat,120,123,'AN-M09/AN-M12')],
 '集合选中槽0原成员A有效且默认焦点4、画布持A；列表Delete确认把该槽替换为新B，随后列表BACK，不重新Load。A有可用图样位图，允许正常新增单元。',
 '画布与集合选中槽仍为同一A时，Cel Focus选择Target使A默认1，后续新增单元焦点1。取消焦点选择不写。',
 '已替换成B但画布仍A时，选择Target：B默认焦点变1，A仍4；在画布新增单元仍用4。保存/单项导出取B，故焦点变1落入这些产物；A的新单元仍不进入集合保存。',
 '列表Delete取消保持同一对象；Focus取消保持A/B各值。无异常即产生分裂的内存改动；BACK不保存并退出清缓存仍不回滚已发出的A/B引用。缩容形成空选中槽时同一Focus读取还有未保护空值失败，不能承诺安全刷新。',
 '五个编辑器文件全文及缓存/集合定义全文已读；分别追读Cel Focus、addSprite、属性焦点默认、batch焦点默认、import/export/save目标。没有Focus操作后把canvas绑回成员的步骤。',
 '正文现有画布脱离说明不足以唯一预测此控件；“该默认用于新建单元”仅在集合成员与画布对象一致时成立。',
 '在§3.2/§7.4补充写入目标分支：Focus及单项交换取集合选中成员；画布编辑/新单元/批改取画布持有动画。取消与重新Load保留原合同。',
 [spec,cat,'specs/demo/wp74-battle-animation-authoring-and-exchange.md','对应追溯/覆盖记录（root裁决后同步）'],
 '非提出者按Delete→BACK→Focus Target→add cel→save/export路径反证；普通同对象与Focus取消对照必须保留。',
 ['§3.2缓存别名','§7.1','§7.4','§11.1','§16'])
finding(3,'使用者/目标焦点锚点在播放器建立时捕获，不随逐帧中心变化','P2',
 [loc(P,675,697,'播放器创建捕获原始中心'),loc(P,818,840,'逐帧焦点重定位'),loc(S,451,488,'编辑器预览建立'),loc(BC,521,564,'战斗动画核心')],
 [loc(spec,314,314,'§10.2焦点定位“当前中心”'),loc(cat,134,134,'AN-M23')],
 '有效立绘/正常播放器；开始时使用者中心(128,224)，帧内槽0为使用者、X200/Y224、focus2；槽2普通图案X128/Y224、focus2。按槽顺序访问正常帧；所有依赖有效，无外部覆盖。',
 '使用者不移动时，开始中心与应用后中心相同，当前/捕获措辞数值一致；Screen焦点不使用锚点。',
 '槽0先显示到X200，随后槽2依建立时捕获的X128，仍显示X128（编辑预览统一加64后两者为264和192）。如果依正文“当前中心”在应用槽2时重新读取，会错误得到X200（预览264）。',
 '预览不改动画数据；正常结束恢复编辑件。中途异常并无保证恢复的边。球爆开辅助有显式目标锚点覆盖，是另一入口，不构成每帧读取当前中心。',
 'Player1–844、SceneElements1–1012、Battle consumers390–579完整相关单元已读；userOrig/targetOrig仅初始化捕获，另仅set_target_origin显式覆盖。未见update每帧重新捕获或跟随立绘中心。',
 '现文字可诱导粒子追随本动画移动后的立绘，改变同帧/后续帧的轨迹。',
 '§10.2把“当前中心”限定为播放器建立时捕获的中心，显式覆盖目标锚点另列依赖；双方源/目标线段也按已建立变换。保留20fps、固定边框、时序合同。',
 [spec,cat,'specs/demo/wp74-battle-animation-authoring-and-exchange.md','user-interface/wp67-a-battle-interaction-and-presentation.md（仅一致性核查，不必改若无当前措辞）'],
 '非提出者核查捕获时点与后续写入者，逐槽静态推导普通移动粒子对照；不得当作实际截图或运行观察。',
 ['WP67-A动画核心','§10.1','§10.2','focus常量'])
finding(4,'Cel Batch数值初值和渐变可选参数范围未写成完整作者输入合同','P2',
 [loc(F,831,894,'Cel Batch全部11参数'),loc(F,624,677,'渐变全部可选参数'),loc(C,388,420,'赋值即时钳制')],
 [loc(spec,251,253,'§8.4'),loc(spec,296,298,'§9.3'),loc(cat,127,127,'AN-M16'),loc(cat,133,133,'AN-M22')],
 '正常已存在单元Opacity17；进入新的Cel Batch，未修改数值，只勾Opacity；正常渐变对话框，已有参与X550（兼容数据夹具），不点箭头。',
 '所有项不勾时不改；仅当前属性窗口的现值默认不等于批改默认。合法渐变X20打开/确认仍20。',
 'Cel Batch勾Opacity直接OK会写255，不是现值17或0；勾Zoom写100、Priority写Front1。正文只列全不勾，未给选中后的11个数值/枚举初值。渐变X550在构造即钳到500，正文没有给其范围。',
 'Batch Cancel/BACK不提交；Gradient Cancel不写原时序；Gradient全不勾OK返回假不写；只勾X确认才提交已钳500。依共享属性别名可能影响区间外共享单元，已有§6.1仍保留。',
 'Functions1–1170及Controls1–942全文；检查§5/§8/§9/§17全文：§5现值表不能推导Batch独立默认，§9.3未明确引用§9.2继承范围。',
 '后续实现/测试无法从净化正文确定勾项直接确认的值与所有作者输入边界。',
 '§8.4增11项范围/初值（Pattern[-2,1000]/0；X[-64,576]/0；Y[-64,448]/0；Zoom[5,1000]/100；Angle[0,359]/0；Opacity[0,255]/255；Blending[0,2]/0；Flip False；Priority Front；Focus动画默认经兼容映射）。§9.3补X/Y[-500,500]、其余[0,255]及未参与数值初始0、现值优先。',
 [spec,cat,'specs/demo/wp74-battle-animation-authoring-and-exchange.md','对应作者控件覆盖记录（root裁决后同步）'],
 '非提出者逐项对照构造参数与消费，验证未勾/Cancel和勾默认的相邻对照；不得把属性现值默认替代Batch默认。',
 ['§5','§8.4','§9.3','§17即时钳制'])
finding(5,'单项导入的类型门不保证内部结构可渲染；替换后失败不回滚槽','P2',
 [loc(E,47,84,'单项导入保护范围'),loc(E,89,126,'转换跳过空帧'),loc(S,409,427,'载入动画'),loc(S,696,705,'setBitmap消费者'),loc(S,907,919,'正常帧更新'),loc(F,1129,1135,'返回主循环')],
 [loc(spec,343,343,'§11.2成功/坏数据分型'),loc(spec,453,453,'§19第11项'),loc(cat,136,136,'AN-M25')],
 '人工外部兼容输入：可正常解码为动画对象，长度1，帧0为空值，图样名空串，时序表有效空；原集合槽为有效A。仅对象类型有效，内部帧结构不满足常规作者产物。文件/列表/消息宿主有效。',
 '有效1帧动画正常替换并载入；解码失败/非动画对象在局部保护中提示回列表，旧槽保持。',
 '转换扫描跳过空帧，因此到达集合槽替换。载入空图样名正常回nil位图、帧号0；回到主循环时更新同号帧单元会读取空帧并产生未保护局部失败。集合槽已替换为该输入，旧A未被回滚。',
 '失败前本次未调用集合保存，缓存集合有效时坏成员已可见；未到正常释放/退出清缓存/环境恢复。仅知失败步骤与已提交槽，实际宿主错误展示/进程结局未知。列表BACK在无导入成功时不替换，但不能回滚此前已完成的输入提交。',
 '五编辑器文件及Player数据定义/缓存读取全文已读；类型门内无结构验证，canvas更新不在该局部rescue内。此反例不声称正常UI能造空帧。',
 '解码/对象类型、旧格式转换、槽替换、画布更新是不同门；把所有坏输入归“消息并回列表”会错误承诺事务回滚。',
 '§11.2将合法/成功前提明确为内部帧/单元结构可用；补类型正确但结构损坏的阶段边界、可能替换后传播、无回滚和未证宿主恢复。保留坏编码/错类型正常拒绝。',
 [spec,cat,'specs/demo/wp74-battle-animation-authoring-and-exchange.md','对应输入失败追溯记录（root裁决后同步）'],
 '非提出者回读解码保护范围与转换跳空帧/画布消费者，确认给定类型正确输入确实越过替换点；允许反证应列具体更早守卫。',
 ['§11.2','§3.3/§3.4异常恢复边界','集合缓存别名','外部兼容数据'])
finding(6,'已有路径后重开Smooth Curve并提前BACK会保留旧路径但清掉可视采点','P2',
 [loc(I,229,263,'路径局部状态'),loc(I,263,353,'Smooth Curve重定义与条件写回'),loc(I,354,405,'Freehand取消不同支'),loc(I,406,425,'OK和外层取消')],
 [loc(spec,261,269,'§8.6定义/取消/OK门'),loc(cat,129,129,'AN-M18')],
 '同一次Define Path窗口中已经生成非空路径P，尚未OK写动画；再次点击Define Smooth Curve，在未放齐端点、未显示曲线前按BACK。',
 '第一次定义曲线且提前BACK：path仍未定义，OK不提交；已显示曲线后BACK：产生新曲线路径。外层Cancel/BACK仍不写动画。',
 '重开曲线首先移除旧路径可视点，但只在showline成立时替换path；提前BACK后path仍旧P，面板回显时没有旧路径点标记。随后OK会按旧P写入动画，必要时先扩帧。',
 '外层取消不写；内部曲线BACK不总是抛弃已有路径。相邻Freehand首次等待阶段ESC会把旧P换成空路径，随后OK先扩帧再失败，原已接受空路径部分提交合同仍成立。',
 'Interpolation1–436全文；全路径状态赋值与控制分支/OK消费均已追读。没有在Curve提前BACK时清空path的步骤；清空的是显示点集合。',
 '取消/重新定义的状态机欠一条历史状态前提，可能使无可视点的OK写出旧轨迹。',
 '仅补§8.6“无此前路径/已有此前路径”对照和可视点与可提交路径分离；不改初次曲线BACK、手绘两个ESC阶段或三套取样规则。',
 [spec,cat,'specs/demo/wp74-battle-animation-authoring-and-exchange.md','对应路径状态机追溯记录（root裁决后同步）'],
 '非提出者按同窗P→重开Curve→未显示线BACK→OK的状态变量逐步反证，另保留首次Curve BACK和Freehand ESC对照；不执行参考。',
 ['§8.6路径局部状态','取消前提','空路径扩帧失败'])
finding(7,'曲线默认中间控制点和参数递推被正文理想化为精确分数','P3',
 [loc(I,216,227,'曲线参数递推'),loc(I,310,333,'自动控制点与30点显示参数')],
 [loc(spec,263,267,'§8.6中间点/初次曲线'),loc(spec,272,276,'B20-D024精确定义'),loc(cat,294,294,'B20-D024')],
 '正常曲线两端点X0和300、Y相同；观察中间控制点赋给宿主之前的数值；另初次曲线N一般值，未要求宿主像素量化。',
 '已拖到明确控制点0/1/8/11且N5的既有精确向量步长1/4可精确表示，原向量不需改。',
 '自动赋给中间控制点的X为99.99、199.98，非精确1/3、2/3的100、200；初次曲线参数也是从0逐次加1/(N−1)，不是每次以j重新除N。一般浮点N的末项不承诺逐位等于1。宿主位置量化未运行，不能声称具体像素差。',
 '控制点定义阶段仍未写动画；外层取消不写。参数末点误差不等于错误退出；已经接受的手绘/改帧数递推、曲线成功后BACK仍提交路径等不变。',
 'Interpolation1–436全文、formal§8.6全文以及B20-D024；未见自动点用精确分数、初次曲线末参数钳1或索引重新计算。',
 '“精确定义”用理想等式会在精确兼容/浮点边界测试中产生过强要求；可视量化的差异尚未知。',
 '把自动默认点限定为近似三等分（数值比例0.3333/0.6666，宿主量化未知）；初次曲线补递推而非索引重新除数、一般N端点容差边界。保留N5明确点向量与数学概念。若root裁决净化合同只要求容差等价，可降为记录而非缺陷。',
 [spec,cat,'specs/demo/wp74-battle-animation-authoring-and-exchange.md','对应数值精度追溯记录（root裁决后同步）'],
 '非提出者确认源码参数递推与控制点常量，并裁定本项目数值兼容是否要求这一级精度；若允许统一容差，明确反证边界后可驳回。',
 ['§8.6','B20-D024','宿主量化未知','全局数值兼容裁决'])
(r/'findings.json').write_text(json.dumps({'scope':'R6-DX/animation','finding_count':len(findings),'all_findings_are_proposals':True,'findings':findings},ensure_ascii=False,indent=2)+'\n')
# Behavioral audit units partition all five mandatory source files. Grouping is for reading audit only.
units=[]
def unit(path,a,b,fact,consumers,clauses,status='SUPPORTED_WITH_FINDINGS'):
 units.append({'unit_id':f'AN-U{len(units)+1:03d}','source':loc(path,a,b),'fact':fact,'necessary_consumers':consumers,'formal_clauses':clauses,'review_status':status,'semantic_review':True})
for args in [
(S,1,95,'弹出菜单定位、鼠标/USE选择及BACK返回-1；私有帧/单元剪贴每次取独立快照',['Functions帧/单元菜单'],'§2剪贴板; §4.3; §6.1; §17'),
(S,96,247,'5格条带、192源区/96缩略、滚动速率/边界、选中改变',['主循环canvas.pattern赋值'],'§2图样表; §7.5'),
(S,248,353,'当前/上一帧角标、锁定与选中颜色、标脏刷新',['AnimationCanvas逐帧设置'],'§4; §17'),
(S,354,448,'建立60常规精灵；load绑定动画、空名nil、图形保护、重置游标/图案；资源释放',['属性、列表Load、import、主循环'],'§3.1; §3.3; §4; §7.1; §11.2'),
(S,449,511,'双立绘预览、Opp互换、固定边框、隐藏恢复编辑件并释放',['Player完整实现'],'§10.1; §10.3'),
(S,512,576,'帧切换/当前帧边界、残影位置；滑动守卫读当前帧',['Functions区间滑动'],'§4; §6.2; §8.5'),
(S,577,626,'Clear0–59用当前守卫；Insert浅帧容器；Copy0–59单元克隆；剪贴全帧替换；最后帧拒删',['帧菜单/区间复制/PasteLast'],'§4.4; §6.1–6.3; §8.1–8.2'),
(S,627,727,'单元粘贴坐标原值/解锁、删除/交换；锁定和删除守卫；正常新增从首空槽',['菜单、键盘、区间Clear、重编号'],'§4.1; §4.3–4.5; §6.3; finding001/002'),
(S,728,891,'非ALT盒/ALT像素(不逆角度)、拖拽偏移、TAB实际槽数、DELETE/锁/旋转/缩放/方向键',['主循环、属性窗口'],'§4.1–4.2; §4.6; §6.3'),
(S,892,931,'播放状态与脏槽重绘；只渲染0–59；渲染消费者要求存在的帧槽序列',['单项import后主循环、Player应用'],'§4; §6.3; §10.2; finding005'),
(S,932,983,'图形预览按名/色相刷新，空名值拼接未保护，按窗口比例缩略',['图样表选择器'],'§7.3; §3.4'),
(S,984,1012,'动画名窗消费画布持有动画并按名变化刷新',['主循环列表/导入返回'],'§7.1画布脱离; §7.2'),
(C,1,115,'文本绘制/控件失效基础，不新增游戏状态',['控件族'],'§17（实现细节不转未来架构）'),
(C,116,233,'按钮按下捕获、框内释放触发；复选翻转',['全部作者确认/取消/可选项'],'§17按钮/复选'),
(C,234,377,'文本输入字符/左右/退格删除、0.35秒光标、无此控件独立长度上限',['重命名窗口'],'§7.2; §17文本框'),
(C,378,491,'数值滑杆构造/赋值即时钳制，重复1/5/10步进，箭头后floor',['全部数字作者参数'],'§5; §6.2; §17'),
(C,492,584,'可选滑杆未勾nil/禁用，勾后取内部数值；setter名字无正常入口消费',['CelBatch/Gradient构造+checked赋值'],'§8.4; §9.3; §17'),
(C,585,630,'ArrayCountSlider失效定义无消费者；帧滑杆动态上界/帧数按钮标签',['主循环帧导航'],'§6.2; §14.3'),
(C,631,746,'枚举滑杆索引钳制、相同步进时序、宽度缓存，不执行数字floor',['属性Priority/Focus/Flip'],'§5; §17'),
(C,747,839,'可选枚举未勾nil，Focus/Flip/Priority默认与消费',['Cel Batch'],'§8.4; §17; finding004'),
(C,840,942,'控件添加索引、窗口逐项更新/value/changed、hittest被帧菜单0消费',['全部对话框+主循环'],'§17; §4帧菜单'),
(I,1,74,'控制点拖拽钳0–512/0–384，未显示点可命中；采点显示',['Smooth Curve循环'],'§8.6; B20-C032'),
(I,75,180,'点列克隆、弧长累计/零段跳过、平滑N+2递推候选、空路径与定义域',['手绘/改帧数/OK'],'§8.6; B20-D024'),
(I,181,228,'三段Catmull-Rom、重复端控制点、初次N点参数递推',['Smooth Curve生成'],'§8.6; finding007'),
(I,229,353,'路径窗口帧2–500、改帧数实数重采样；曲线放置/旧路径清显示但不总清数据',['OK/外层Cancel'],'§8.6; finding006/007'),
(I,354,436,'手绘两阶段ESC、记录重复点剔除、首次取整；OK先扩帧再逐槽写X/Y；空路径失败',['动画resize/pbCreateCel'],'§8.6; finding006'),
(E,1,26,'目录枚举chdir无保护；数据辅助保护；单动画交换编码/解码互逆边界',['单项与批量交换'],'§3.4; §11; §13'),
(E,27,45,'文件名32空名取消；当前集合选中成员导出；写失败消息',['主循环Export'],'§11.1; §16'),
(E,46,84,'单项导入类型门/转换/替换在局部保护，缺图检查与canvas绑定在保护后',['loadAnimation+主循环更新'],'§11.2; finding005'),
(E,85,127,'旧格式检测和修正常规0–59；缺FOCUS触发全动画修正',['单/批量导入'],'§14.1; §6.3'),
(E,128,147,'全量转换入口首槽门、转换计数、仅改动写盘清缓存，无调用者',['全脚本检索'],'§14.2; §16'),
(F,1,25,'占位战斗成员无pokemon，因此叫声静音',['预览Player时序'],'§10.2'),
(F,26,67,'PNG目录选择、hue0–359默认0、预览先于输入、USE写表并绑定',['BitmapDisplayWindow/AnimatedBitmap'],'§7.3; §3.4'),
(F,68,90,'总帧数1–1000、OK resize、Cancel/BACK不改',['主循环当前帧钳制'],'§6.2'),
(F,91,116,'改名现值、文字模式、OK/Return写，Cancel/ESC弃',['AnimationList/编译/公共名查找'],'§7.2; §15'),
(F,117,184,'列表先填nil；Resize立即改集合/越界游标；Load绑定、Delete替换不绑定',['集合resize/窗口索引/Focus/Save'],'§7.1; §3.2; finding002'),
(F,185,212,'重编号2–60、Cancel=-1、由调用者交换',['swapCels'],'§4.5; §6.3'),
(F,213,242,'Tone RGB±255/gray255、即时tone预览、OK克隆提交',['属性父窗'],'§5'),
(F,243,272,'混色RGBA255但子预览tone；OK写混色，Cancel不写',['属性父窗color应用'],'§5'),
(F,273,372,'属性克隆11参数及2子入口、固定预览坐标/z、OK原位覆盖保留共享别名',['pbSpriteSetAnimFrame/Insert共享单元'],'§5; §6.1'),
(F,373,503,'时序5 Add、Set Frame/Delete索引更新，子确认追加，既有修改即内存',['时序子窗口/Player playTiming'],'§9'),
(F,504,561,'SE扩展列表/叫声特殊项、Volume/Pitch、USE才选文件、试听/停止/确认/取消',['声音系统/时序播放'],'§9.1'),
(F,562,623,'BG/FG列表排序抹除索引错位，X/Y±500、Opacity/RGBA255默认0，OK提交',['playTiming/批量import'],'§9.2'),
(F,624,678,'Gradient duration0–50，7可选项范围/现值，至少一项才提交',['playTiming共享快照'],'§9.3; finding004'),
(F,679,725,'复制包含端点、重叠方向、越尾copyFrame逐项跳过，不扩帧',['Canvas copy0–59'],'§8.1'),
(F,726,753,'Clear升序区间，Cancel不写',['Canvas当前守卫'],'§8.2'),
(F,754,830,'Tween起>=终不写，缺端点跳列，中间空槽pbCreateCel默认focus4，强制3组，数值类型插值',['pbCreateCel/reset'],'§8.3'),
(F,831,895,'Batch11可选范围/独立初值、已存在槽、Focus逆映射，USE/OK提交',['Optional Slider/别名单元'],'§8.4; finding004'),
(F,896,927,'EntireSlide帧区间/偏移±500默认0，OK消费当前守卫',['Canvas offsetFrame'],'§8.5'),
(F,928,947,'Help ALT2文案与实际1不一致；BACK或USE退出',['键盘实际行为'],'§4.2; §19'),
(F,948,1032,'主画布+13侧栏按钮、帧条带、双确认与帧菜单；保存集合退出才清缓存',['缓存/持久化/Canvas'],'§3.2; §6; §17'),
(F,1033,1082,'Q/右键属性剪切复制粘贴删除/重编号/路径实际前提与消费',['Clipboard/Canvas/Path'],'§4.2–4.5; §8.6'),
(F,1083,1143,'各按钮dispatch目标；帧数钳制；Focus写集合成员而画布工具写canvas对象',['Load/import/export/Focus/Save'],'§6.2; §7.4; §11; finding002'),
(F,1144,1153,'正常循环返回后才释放窗口/viewport与图像缓存',['入口环境恢复'],'§3.3–3.4'),
(F,1154,1170,'BGM停止/缓存读取，空首槽临时集合不写缓存；扩屏因子1/正常返回恢复',['缓存+主循环'],'§3.1–3.2; §19')]:unit(*args)
# Additional consumers, each relevant unit read in full.
for args in [
(P,1,112,'25语义属性、默认cel/reset、中心/坐标数学',['Canvas/属性/路径/Player'],'§2; §4.4; §10.2'),
(P,113,232,'旧宿主转换定义与兼容拼接，无活动编译调用',['注释块全脚本检索'],'§14.3'),
(P,233,333,'五类时序数据默认与文本显示',['时序编辑/播放'],'§2; §9.4'),
(P,334,395,'集合构造下限、resize游标置新长度、容器写入/插删/首名查找',['AnimationList/organiser/allocate/import'],'§2; §7.1; §12; §13.4'),
(P,396,473,'动画默认、帧扩缩/双个体、speed仅getter',['主编辑器/全部帧工具'],'§2; §6.2; §10.2'),
(P,474,591,'活动渐变先处理再起始时序、共享oldbg/oldfo、位置符号、RGBA全写、d0捕获',['Player每次访问帧'],'§10.2a'),
(P,592,670,'逐单元渲染/可见==1/比例/源图/优先级，闪烁兼容字段未活动消费',['Canvas/属性/Player'],'§5; §10.2'),
(P,671,844,'固定20fps跳帧/末帧、60精灵、捕获焦点锚点、Opp/边框/完整时序',['编辑器preview/战斗core/ball辅助'],'§10.1–10.3; finding003'),
(U,16,62,'文件安全复制比较y但可写z；动画空槽分配1起无空调整10',['批量import/export'],'§13.3–13.4'),
(U,284,336,'组织器ACTION+方向/USE/BACK命令返回',['organiser'],'§12'),
(B,553,663,'批量输出有兜底/覆写/资源安全复制；批量输入无整体兜底/资源先于校验/分配先于转换/音频核名所有时序',['codec/allocate/converter/RTP/缓存'],'§13; §16; §19'),
(O,1252,1324,'organiser首槽门、方向交换/插删/0项/YesNoCancel保存语义',['Commands3/cache/collection'],'§12; §16'),
(K,1,64,'动画和映射懒缓存、全局清理、磁盘读取前提',['editor/organiser/batch/战斗查找'],'§3.1–3.2; §16'),
(Q,1274,1321,'编译直接读磁盘，前导空白匹配/重复后槽覆盖、有效条目写门',['Move exists/get/播放lookup'],'§15; §16'),
(BC,390,579,'招式/公共名查找/回退与core创建、恢复；ball显式目标锚点',['Player/cache/映射'],'§15引用交界; finding003'),
(BT,1,228,'普通图位图保护占位，帧前缀解析可抛，deanimate给单帧',['Canvas/选择器/Player'],'§3.3–3.4'),
(RTP,181,286,'RTP实际当前路径枚举/文件/图像/音频扩展与存在性',['directory选择器/batch复制与核名'],'§3.4; §13; §19范围保留'),
(W,753,1248,'选择窗口索引不钳制，常规方向取模，刷新不修index',['AnimationList/Timing/organiser'],'§7.1; §17'),
('reference/pokemon-essentials/animmaker.txt',1,26,'文档XML图块≤96且精灵加倍；没有本工具运行证据',['文档陈述边界'],'§18'),
(base+'007_Objects and windows/009_Planes.rb',1,76,'图形层置图先清旧位图，nil退纯色，普通保护由AnimatedBitmap提供',['playTiming'],'§10.2a'),
(base+'020_Debug/003_Debug menus/002_Debug_MenuCommands.rb',1272,1306,'四动画菜单注册与淡出/直接批量入口',['editor/organiser/batch'],'§3.1')]:unit(*args)
(r/'forward-matrix.json').write_text(json.dumps({'direction':'unit -> behavioral fact -> necessary consumer -> formal clause','grouping':'Behavioral units, not future architecture; primary 3707 source lines partitioned without gaps','units':units},ensure_ascii=False,indent=2)+'\n')
rev=[]
def reverse(clause,a,b,sources,review='SUPPORTED_WITH_SCOPED_FINDINGS',obligations=None):
 rev.append({'clause':clause,'formal':loc(spec,a,b),'source':sources,'precondition_review':review,'obligations':obligations or ['静态合同，不升级为运行验证']})
for args in [
('§1 purpose/scope',7,19,[loc(F,951,1170),loc(B,553,663),loc(O,1252,1324)]),
('§2 concepts/defaults',21,32,[loc(P,4,30),loc(P,75,108),loc(P,233,472),loc(S,47,64)]),
('§3.1 entry',34,40,[loc(F,1157,1170),loc(K,39,45)]),
('§3.2 save/cache/alias',42,57,[loc(F,994,1001),loc(F,117,183),loc(K,39,45),loc(P,334,391)]),
('§3.3 normal cleanup/bitmap branches',59,67,[loc(F,1144,1170),loc(S,409,448),loc(BT,4,207)]),
('§3.4 directory failure vs loader failure',69,75,[loc(E,7,9),loc(F,29,66),loc(F,504,677),loc(RTP,181,286)]),
('§4.1 mouse',77,87,[loc(S,729,828),loc(S,717,727)]),
('§4.2 keyboard',89,104,[loc(S,810,890),loc(F,928,947),loc(F,1033,1038)]),
('§4.3 clipboard',106,110,[loc(S,47,64),loc(S,608,613),loc(S,634,650),loc(F,1058,1066)]),
('§4.4 delete/reset',112,123,[loc(S,579,590),loc(S,678,694),loc(P,86,108)]),
('§4.5 renumber',125,129,[loc(F,188,211),loc(F,1069,1074),loc(S,660,669),loc(P,802,806)]),
('§4.6 ALT rotation',131,133,[loc(S,729,779)]),
('§5 properties',135,158,[loc(F,213,371),loc(C,388,461),loc(P,592,665)]),
('§6.1 frame/alias',160,176,[loc(S,592,626),loc(S,47,64),loc(F,346,360)]),
('§6.2 count/navigation',178,182,[loc(C,603,625),loc(F,68,89),loc(F,1083,1093),loc(P,450,472)]),
('§6.3 slot60',184,200,[loc(S,579,669),loc(S,810,890),loc(P,802,806),loc(E,89,126),loc(I,414,422)]),
('§7.1 animation list',202,210,[loc(F,117,183),loc(P,334,391),loc(W,753,976),loc(W,1163,1248)]),
('§7.2 rename',212,214,[loc(F,91,115),loc(C,238,377)]),
('§7.3 sheet/hue',216,220,[loc(F,29,66),loc(S,936,983)]),
('§7.4 Focus',222,224,[loc(F,1106,1120),loc(S,717,727),loc(F,295,297),loc(F,853,855)]),
('§7.5 sheet strip',226,228,[loc(S,100,247)]),
('§8 common ranges/cancel',230,232,[loc(F,679,927)]),
('§8.1 interval copy',234,236,[loc(F,679,724),loc(S,598,606)]),
('§8.2 interval clear',238,240,[loc(F,726,752),loc(S,579,590),loc(S,678,694)]),
('§8.3 tween',242,249,[loc(F,754,829),loc(P,75,108)]),
('§8.4 batch',251,253,[loc(F,831,894),loc(C,496,584),loc(C,751,839)]),
('§8.5 slide',255,257,[loc(F,896,926),loc(S,566,576),loc(S,671,676)]),
('§8.6 path',259,276,[loc(I,1,436),loc(P,450,472),loc(P,75,108)]),
('§9 timing list',278,286,[loc(F,376,502)]),
('§9.1 sound',288,290,[loc(F,504,560),loc(P,233,268)]),
('§9.2 graphics',292,294,[loc(F,562,622),loc(P,532,571)]),
('§9.3 gradient',296,298,[loc(F,624,676),loc(C,496,584)]),
('§9.4 text',300,302,[loc(P,278,328)]),
('§10.1 preview',304,308,[loc(S,451,511),loc(F,7,24)]),
('§10.2 shared frame',310,315,[loc(P,592,844),loc(P,474,586)]),
('§10.2a timings exact',317,329,[loc(P,474,586),loc(P,767,843)]),
('§10.3 preview no data write',331,333,[loc(S,451,511),loc(P,474,844)]),
('§11.1 single export',335,339,[loc(E,19,45)]),
('§11.2 single import',341,343,[loc(E,47,84),loc(S,409,427),loc(S,696,705),loc(S,907,919)]),
('§12 organiser',345,350,[loc(O,1252,1324),loc(U,284,336),loc(K,39,45)]),
('§13.1 bulk export',352,361,[loc(B,553,595),loc(U,16,44)]),
('§13.2 bulk import',363,370,[loc(B,597,663),loc(U,46,62)]),
('§13.3 safe copy',372,374,[loc(U,16,44)]),
('§13.4 allocation',376,378,[loc(U,46,62),loc(P,381,390)]),
('§14.1 conversion',380,384,[loc(E,89,126)]),
('§14.2 unused whole conversion',386,388,[loc(E,128,147)]),
('§14.3 inactive definitions',390,392,[loc(P,113,165),loc(Q,1283,1294),loc(C,589,598)]),
('§15 names/compiler/lookup',394,399,[loc(Q,1274,1321),loc(BC,412,579),loc(K,47,53)]),
('§16 persistence/cache matrix',401,421,[loc(F,994,1001),loc(O,1306,1324),loc(B,553,663),loc(E,128,147),loc(Q,1315,1319),loc(K,11,53)]),
('§17 controls',423,433,[loc(C,1,942),loc(W,753,1248)]),
('§18 doc boundary',435,439,[loc('reference/pokemon-essentials/animmaker.txt',1,26)]),
('§19 edge/unknown summary',441,460,[x['source'] for x in units if x['source']['path'] in [S,C,I,E,F,P,B,O,K,Q]]),
('§20 examples',462,464,[loc(cat,106,144),loc(cat,277,295)]),
('§21 dependency/unknown/neutrality',466,472,[loc(spec,19,19),loc(spec,470,472)])]:reverse(*args)
# Catalog AN clause coverage linked to matching formal unit, and supplementary animation vectors.
for i in range(1,34):
 line=111+i
 rev.append({'clause':f'AN-M{i:02d}','formal':loc(cat,line,line),'source_relation':'对应以上WP74条款的源链；非自动测试通过','evidence_level':'DERIVED_VECTOR_NOT_EXECUTED','review_status':'SCOPED', 'findings':[x['id'] for x in findings if any(y['path']==cat and y['lines'][0]<=line<=y['lines'][1] for y in x['formal'])]})
for line,cid in [(277,'B20-003'),(278,'B20-C003 animation portion'),(280,'B20-C020'),(282,'B20-C025'),(283,'B20-C026'),(288,'B20-C031'),(289,'B20-C032'),(290,'B20-C033'),(294,'B20-D024'),(295,'B20-INTAKE-R01 animation portion')]:
 rev.append({'clause':cid,'formal':loc(cat,line,line),'source_relation':'以上对应源链已语义回读','evidence_level':'DERIVED_VECTOR_NOT_EXECUTED','review_status':'SCOPED','findings':[x['id'] for x in findings if any(y['path']==cat and y['lines'][0]<=line<=y['lines'][1] for y in x['formal'])]})
(r/'reverse-matrix.json').write_text(json.dumps({'direction':'formal clause -> source -> preconditions','wp74_full_text_read':True,'catalog_full_text_read':True,'catalog_semantic_review_scope':'Animation clauses; other domains full text read as required, not source-audited here','clauses':rev},ensure_ascii=False,indent=2)+'\n')
# Manual semantic passes, explicitly separate from display/read mechanics.
primary=[S,C,I,E,F]
for p in primary+[spec,cat,P,BT]:
 relevant=[x for x in units if x['source']['path']==p]
 notes=[x['fact'] for x in relevant] if relevant else ['Formal clauses manually compared to source chain; other-domain catalog prose only read, not audited here']
 with (r/'logs/reading-ledger.jsonl').open('a') as fp:
  fp.write(json.dumps({'phase':'manual_semantic_pass','path':p,'start':1,'end':len(Path(p).read_text().splitlines()),'sha256':hashlib.sha256(Path(p).read_bytes()).hexdigest(),'semantic_pass':True,'automatic_read_is_not_semantic_pass':True,'reviewed_by':'animation subagent; actual runtime identity UNVERIFIED','facts':notes},ensure_ascii=False)+'\n')
for x in units:
 p=x['source']['path']
 if p in primary+[spec,cat,P,BT]:continue
 with (r/'logs/reading-ledger.jsonl').open('a') as fp:
  fp.write(json.dumps({'phase':'manual_semantic_pass','path':p,'start':x['source']['lines'][0],'end':x['source']['lines'][1],'sha256':hashlib.sha256(Path(p).read_bytes()).hexdigest(),'semantic_pass':True,'automatic_read_is_not_semantic_pass':True,'fact':x['fact']},ensure_ascii=False)+'\n')
# Mechanical completeness check is only interval accounting, never evidence of semantic correctness.
coverage=[]
for p in primary:
 n=len(Path(p).read_text().splitlines());covered=set()
 for x in units:
  if x['source']['path']==p:covered.update(range(x['source']['lines'][0],x['source']['lines'][1]+1))
 missing=sorted(set(range(1,n+1))-covered)
 assert not missing,(p,missing)
 coverage.append({'path':p,'total_lines':n,'semantic_audit_lines':n,'unread_lines':0,'sha256':hashlib.sha256(Path(p).read_bytes()).hexdigest()})
status={'logical_id':'R6-DX-animation','state':'REVIEW_COMPLETE_PROPOSALS_AWAIT_COUNTEREVIDENCE','baseline':{'main_commit':'8ea169fbd0f33f378b5d732fd6bea59e854e04a6','main_tree':'6ab3429170d2762607fbc2237014c3a160449fa1','formal_tree':'1046fbb657882e84b3dfc6d017943a9edf7782e5','reference_commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','reference_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0'},'required_source_files':5,'required_source_lines':3707,'read_source_lines':3707,'unread_source_lines':0,'required_formal_lines':472,'read_formal_lines':472,'required_catalog_lines':327,'read_catalog_lines':327,'semantic_pass_is_manual':True,'proposals':len(findings),'approved_findings':0,'root_ruling':'PENDING','counterevidence_by_non_proposer':'PENDING','update_started':False,'reference_executed':False,'unknown_scripts_executed':False,'downloaded_or_installed':False,'actual_model':'UNVERIFIED','actual_effort':'UNVERIFIED','actual_service_tier':'UNVERIFIED','actual_speed':'UNVERIFIED','actual_agent_uuid':'UNVERIFIED','writes_restricted_to':str(r),'primary_coverage':coverage,'blocked':False,'limitations':['全部为静态语义审查，不声称游戏/编辑器/播放器/参考实例执行','animmaker仅文档；本子域未依赖R6-B报告','数值精度候选需root裁定兼容容差','全部发现仅提案，等待非提出者反证与全局root裁决']}
(r/'task-status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
