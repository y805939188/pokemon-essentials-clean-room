# 内嵌字体完整有限语义贡献

作者为实际新上下文 `/root/media_font_programs`；接收者 `/root/resource_media_serialized_cloud`。本贡献在 B8 `fd1df570cad987dc3852a3b958f03916e317f7fe`、R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 上新读。原委派 JSON 的 `PROPOSED_NOT_APPLIED_0START` 是先前历史，未被本任务改写。当前仅完成有限静态读取，尚待接收者实际内容审查；不表示全局 PASS、已整合或已整改。UPDATE_NOT_STARTED。

## 完整单位与证据意义

Game.exe 的 `[10217888,10568088)` 为 350200 字节字体；SHA256 `e5b0af421ea2bfbc1ac8d251d647268087ae82786234c57f757d1f0b90fa8b49`。13 个独占完整单位是 fpgm、prep、cvt、glyf、loca、hmtx、maxp、head、hhea、GPOS、GSUB、kern、GDEF。`identities.json` 绑定原始文件和 fixed B8/R 字节，`structure-ledger.json` 逐表、逐 glyph 绑定原始跨度和散列，`program-ledger.json` 逐完整程序绑定指令、push 来源和实际读证据。表数不是语义需求分母。

2587 个 glyph 全范围 `[0,2587)`：1497 simple、1075 composite、15 empty；2347 个有自身指令，225 个非空但无自身指令，15 个空项。所有 2347 glyph 程序和 fpgm/prep 总计 2349 个程序、121793 字节、52297 条解码指令，均实际完整审读，未以重复 blob、共享模板、抽样或脚本成功替代。71 个 FDEF ID 稀疏分布于 0..91；maxp.maxFunctionDefs=92 不是已有定义数量。

`decoded-programs.json` 保留每个 opcode、flag、PC、push 字节/字编码和全部原值。`glyphs.read.txt` 每一完整 glyph 独占一行；只压缩本行立即重复序列，缩写在 `glyph-spelling-glossary.json`，不跨 glyph 复用阅读信用。原序列、完整数值和消费者 PC 同时保留在 `static-push-roles.json`。八个 glyph-read 原始 stdout 连续覆盖 2347 行，全部读完。控制值另读 `delta-controls-short-read-001-100/101-300/301-568.stdout`，568 个含 DELTAP 的 glyph、5927 个 packed 参数全部实际值已读；首次较长 delta-controls-read 输出有平台截断，不作为其未显示部分的阅读依据。完整机器账本保留 point、PC 和原 DELTA 类别的关联。

## 所有 push 的实际类型与用途

glyph 共 65761 个推入值，每值都有原 push PC/序号、消费者 PC、角色和值。点号、轮廓号、CVT 号、度量、坐标、font-unit 修正属于有精确范围的数值几何/地址数据，按照各指令的 point/contour/CVT 使用方式全范围处置，未逐一声称眼读坐标。点号还可指向 composite 展开的点或 phantom point；地址本身不等于像素结果。轮廓号被 SHC 使用，实际 SHC 变体均保留。

其它值全部按实际数值和意义逐读：3578 个函数 ID 与所有实参；663 个 SLOOP 计数；411 个 SDB；315 个 SDS；240 个 SMD（F26Dot6）；3703 个 DELTAP pair 数；5927 个 packed DELTA ppem/位移选择器；F72/F73/F77 的 ppem 边界和模式参数。不存在 glyph 内联 IF/ELSE、相对跳转偏移、动态函数 ID、storage index、zone 指针或额外 rounding 参数的遗漏；这些指令根本不在 glyph 程序中，RTG/RTHG、SVTCA/SDPVTL、MDRP flag 则实际存在并逐条保留。glyph 的所有 CALL 前 loop=1；SLOOP 后相应 IP/SHP 消耗该批点并复位。glyph 不通过共享模板豁免实际控制参数。

glyph 调用的全部接口为：F91(ref,point,cvt) 109 次；F89(ref,point,cvt) 1972 次；F72(point,shift,lowerPpem,upperPpem) 176 次；F77(point,shift,ppem,mode) 3 次；F73(point,shift,ppem) 2 次；F37(fontUnitCorrection,point,point,point,point) 723 次；F38(point,cvt) 593 次。每次参数均保留且已读；几何部分按上述 type/use 处理。F72 在 lower<=ppem<=upper 时 SHPIX；F73 精确 ppem 相等时 SHPIX；F77 先比较 storage[2] 模式再调用 F73。

对 packed 参数 q：ppem 选择为当前 deltaBase + 类别偏移(0/16/32) + (q>>4)；低四位 n 的带符号步数为 n<8 时 n-8、否则 n-7，除以 2^deltaShift。所有实际 q、有效 base、shift 分母均已逐全读，不只执行配对器。`delta-controls-decoded.json` 保留每个原始 q、point、pc、最终 ppem/分数位移；没有执行任何点移动。DELTAC 同规则，prep 全部原值在 `prep-actions.txt` 实际全读。

## fpgm：全部定义、分支与调用

`function-semantics.json` 逐一给出 71 个完整定义的原 PC/字节范围、全部指令/值、stack 接口和用途。`functions-01.stdout` 的完整定义逐一实际读完；`function-signatures-check.json` 为之后的辅助交叉核验，不替代阅读。检查器不解释数学谓词、不执行字体状态，只遍历两条 IF 臂检查抽象栈；首次错误参数摘要和失败输出保留，修正后的 lexical-03 为最终角色账本。

F0 为双 CVT 与当前坐标偏差组合后的 SCFS；F1 对单 CVT RTG/ROUND 后回写。F2/F3 是正/负方向的两点 SCFS，偏移 32/70/38；F4/F5 对应 64/102/38。F6 依 X/Y 两轴 ALIGNRP。F7 分段以 205、141、77、13 写 CVT，比较 346、237 和调用者阈值。F8 把相邻 CVT 经 RTG、SROUND70 组合回写。F9/F10 从 storage10/11 建 projection/freedom vector；F11 用 scratch CVT40 和两点构向量并返回 GFV。F13 当两 CVT 差绝对值<=80 时复制；F14 把 MD 写 CVT14；F15 加 storage0 后回写；F16 从 storage6/7 建 projection vector。

F17 消耗一个输入并返回一个结果。其唯一 computed CALL 是 `44 + DIV(min(max(ROUND[1](d)-64,0),192),4096)`，按固定点 DIV 的 64 倍尺度，目标闭合于 44..47；这不是未解析无限调用。所选分支仍依赖图形 round/projection 状态。GPV 两分量绝对值相等时结果再减3。F20 消耗4参，经 SDPVTL1、F17 得校正 CVT41，ROFF/MIRP4 后恢复 RTG。F24 把一 CVT 取负写44，另一写43。

F31 在 threshold>ppem 时复制 source CVT 到 dest；F33 在 threshold<=ppem 时复制。F34/F35 按 X/Y 分别用 MIRP21/13/12，邻点索引分别+1/-1；F36 是6参版本。F37 在 storage2>1 时仅丢弃5参，否则由四点坐标和 font-unit 修正经 CVT12 缩放、DIV(-128)，负值先减1再max(-70)、非负min(70)，再加16并 ROUND，X 向 MSIRP。F38 在 CVT>point 当前坐标或 ppem<=19 时 MIAP/SHPIX 补偿，否则 SRP1；F39 是 CVT<point 的对应分支，无 ppem<=19 附加门。F40 从 storage7/6 建 freedom vector。

F44 丢两参，由 GPV 最大绝对分量/16384 返回数；F45/F46 依输入<=128/192 直接算相应8192/5461分母，否则调 F47，之后加2。F47 将向量校正加到输入后返回。F48 在 caller threshold>=ppem 时计算间距/CVT14、MIRP22，否则设参考点 IP/MDAP1。F49 同样以 threshold>=ppem 分两臂；前臂完整消耗8个 caller 参数，后臂消耗5个，均净返回0。不存在现有 glyph/prep 或其它定义调用 F49，不能把这个源事实直接升格为当前正式规格缺陷；也不能用固定5参摘要掩去其前臂。

F53 将4个 CVT 相加、按 caller SROUND 设定舍入，除128并返回两份结果；F54 完整转调F72。F55 在目标 CVT=0 时置64，并把另一 CVT 减64；否则丢参。F56 把 CVT48-CVT47 加到输入 CVT，+1后 ROUND1 回写。F57 在 threshold<=ppem 时 WCVTF47、WS20；否则丢参。F58 在 threshold<=ppem 且输入值>=ROUND1(CVT) 时写 CVT。F59 将 CVT 与 storage20 的比例相乘、+1、ROUND1 后回写。F60 复制 CVT47；F61 把 source CVT 加到 dest 原值；F62 将两个 source CVT 和写 dest。F63 在 ppem<=threshold 时写 CVT51=-32、52=32，否则两者为0。

F64 受 storage22 门控：按 caller 符号/舍入选项把 CVT 宽度规整为非零整数格附近值，以 scratch CVT41/MIRP0 约束点；否则丢5参。F65 先比较 storage2 的模式，再在闭 ppem 区间 SHPIX。F66 在 storage22 门内用8参建立两段自由向量、临时保存在 caller 指定 storage 及下一格的坐标、ALIGNRP、正负 CVT41 约束，再 RS/SCFS 复原投影坐标；外臂丢8参。F67 在 caller storage 格保存点坐标并沿指定向量以 CVT 定位；F68 从 caller storage 格 SCFS 恢复。它们的 caller storage/point/vector 是未实例化形参，实际 glyph/prep 无这些函数的调用，不伪造运行输入。F69 将 source CVT 的符号保留且至少一像素的 RTG 结果加到 dest。

F70 在 lower<=ppem<=upper 时给 CVT 加修正；F71 在精确 ppem 时加修正；F72/F73 为同条件的 SHPIX，F73 的 `PUSH0 POP` 也保留。F74/F75/F76/F77 先比较 storage2 模式，再分别完整调用 F70/F71/F72/F73，否则平衡丢参。F78 先按两点 SFVTL 定 freedom vector，再在闭 ppem 区间 SHPIX。F79 Y向测两点 MD，非负则把点 SHPIX64并置 SRP1；负则丢参。F80 以3点坐标及 font-unit 修正(CVT64)求居中量，ROUND 后 X向 MSIRP。F81 在量化阈值条件下 ALIGNRP，否则丢点。F82 在 caller threshold>ppem 时 RDTG，否则 ROFF。

F83 比较 Y/X ppem 写 storage18。F84 完整按 GETINFO selector1 的版本35..64门、selector32/64/128/256/512/1024/2048 的结果位构 storage2（加1/2/4/8/16/32/64/128），含 version36 的 X/Y ppem 比较和 version>=38 的高位门。最后按 mode0、mode1、128>mode、其它分支写 storage5/8/9/12/13。实际常量组合为 mode0=[64,64,64,2,2]；mode1=[64,256,256,1,1]；其余mode<128=[64,384,64,0,1]；其余mode>=128=[64,384,320,0,1]。最后嵌套 GETINFO 的两条臂均给[0,1]，未擅自简化掉源码分支。F85 读 source、RTG/ROUND0；threshold<=ppem 时再加 dest 原值的舍入结果，绝对值<64 时先 RUTG，最后回写 dest。

F88 临时 SZPS0，用 twilight 点1/2、MIAP0 和 MIAP1 建两组向量，分别写 storage10/11 和6/7，再 SZPS1、X向结束；所有 zone/point/storage 常量已实际读。F89 在 mode>128 或 mode=1 时舍弃 CVT，用 SMD32、MDRP9；否则参考点+MIRP13。F90 完整别名调用F89。F91 参考点+MIRP5。MIRP/MDRP 每一 variant 的原5-bit值保留，不能概括为统一“吸附”。所有函数原 IF 条件、CINDEX/MINDEX/ROLL 深度、scratch CVT/storage 位置均在完整 code 对象中；未发现 JMPR/JROT/JROF、LOOPCALL、IDEF，动态分支是结构化 IF，动态调用仅上述 F17 的有限集合。没有执行这些定义，也没有把未选中的函数删除。

## prep：完整初始栈、控制门与真实调用参数

835 字节全部解码并实际读。前608字节将全部后续参数预装栈，随后 CALL83、84；参数顺序与消费者不是简单“最近 PUSH”。`prep-roles.json` 把所有线性参数配对；610..646、653..683 的自含条件 prologue 另逐条人工读，完整原码在 decoded-programs。最终参数栈耗尽；没有在两段 prologue 中误消费预装栈。

当 ppem>2047、ppem<7，或 GETINFO version 在37..64且 selector6结果非0，INSTCTRL(1,1)请求禁用指令。随后 SCANCTRL400、SCANTYPE1再5、Y向、storage22=1、SCVTCI128。ppem>=50 将 cut-in 改96，>=100 改64，>=128 改16且 storage22=0。所有阈值/selector/位值实际读完；不声称目标 rasterizer 必定采纳。

prep 的全部65次 CALL 是83/84各1次、31共36次、85共22次、70共5次；每次真实参数、轴切换、DELTAC1/2/3 的全部 CVT/packed参数在 `prep-actions.txt` 逐项完整实际读。F31/F85 的 threshold、F70 的 ppem上下界没有按“几何数字”豁免。SDB 依次在相关位置改8、64、11、10，最后恢复9；没有 SDS，沿默认 deltaShift3。末尾 RTG。完整写 CVT 是随后 glyph 可读取的状态；原 CVT 数组不是永久不变像素度量。源内指令语义和目标宿主是否执行分别登记。

## 轮廓、度量与数值全范围

`decoded-glyphs.json` 对全部2587项保存 loca 段、空/simple/composite 类型、bbox、hmetric、自身程序位置和 padding。1497 simple 的全部 contour endPoints、重复 flag、34342 点的 x/y/oncurve/overlap 数值完整安全解码并按二次轮廓数值用途处置；不把这些坐标声称为视觉验收。1075 composite 的2130个 component 全部保留 child/flags/args；实际均 XY font-unit translation，无 F2Dot14 变换矩阵。全部8种 flags=4102/4358/4134/4135/4359/4646/4614/4103，分别含 byte/word signed offsets、MORE_COMPONENTS、WE_HAVE_INSTRUCTIONS、USE_MY_METRICS、UNSCALED_COMPONENT_OFFSET 等实际位；不能把 component child 当函数。未有点对点 attachment。

loca 为2588个 uint32，完整对应 glyf `[0,267132)` 单调边界；hmtx 为2587组 u16 advance/s16 lsb，实际 advance 0..2740、lsb -1114..725。324个 CVT s16 全数组实际读完，按2048 units/em的设计单位，运行后可能变为scaled/CVT写入值。head 整54字节、hhea整36、maxp整32逐字段读；完整值保存在 decoded-tables.json。head flag=0x21f、macStyle0、longloca1、字形格式0；时间戳原64位数值不伪造实际UTC。hhea ascent1854/descent-434/gap67；maxp points338/contours84/compositePoints92/compositeContours6/zones2/twilight16/storage47/functionDefs92/instructionDefs0/stack676/maxInstructions516/componentElements4/depth1。这些是声明界限而不是运行覆盖率，也不是已成功分配内存的证据。

## GDEF、GSUB、GPOS、kern 的全部规则

`decoded-layout.json` 保存全部原覆盖集合、规则、顺序、值、anchor、offset 与 lookup flags。`layout.read.txt` 仅去掉重复字段键并列出全值；全部100行均实际完整读，三个大 pair 列表另分为完整无截断输出，未用“同kern”替代第二份读取。coverage展开数据有原二进制 offset 可回查；规则中的 glyph ID 不被混作 Unicode。原 Coverage/ClassDef 编码格式和区间在 structure-ledger 的 raw_layout_structures 保留。

GDEF v1.0 的 class/attach/ligCaret/markAttach 偏移为14/0/120/128。class fmt2 的17个原区间完整覆盖0..2586；class1一般基字，class3 mark区间1225..1269、1271、1273..1277、1279、2247、2583..2585；class2为2291、2578..2580。AttachList不存在，LigCaretList有表但实际为空；markAttachClassDef fmt1 start0/count1/value0，不能误写为不存在。无 MarkGlyphSets。

GSUB v1.0：6 lookup、6 subtable。脚本 cyrl 只有MKD/SRB语言的locl→L0，没有默认语言；grek/latn默认ccmp→L4；hebr默认ccmp→L2,L3及dlig→L1；全部 requiredFeature=65535。L0单替换994→2586（delta1592）；L1 1280,1292→2291；L2全37条希伯来连字含3输入顺序；L3完整 fmt3 backtrack/input/lookahead 覆盖条件在 input位置0调用L5；L4全140条由679..683组成的2/3输入序列映到2361..2500；L5全6条上下文连字。共184条连字规则，既保留每个输入次序也保留输出；没有将范围补成笛卡尔积。Lookup flags的 RTL、忽略base/ligature/mark逐实值处理，不自行反转输入/输出。

GPOS v1.0：26 lookup、58 subtable；cyrl（default/MKD/SRB）、grek/latn default用kern→L17；hebr default用kern→L0和mark→L1..16，requiredFeature均65535。L0 1107 pair，flag9，ValueFormat1=5(xPlacement+xAdvance)，ValueFormat2=0，全部实值完整读。L17另908 pair，flag8，ValueFormat1=4(xAdvance)，ValueFormat2=0；L25一个1244/1245 pair，两个 ValueFormat=1，xPlacement分别+200/-200。共2016个pair记录。L1、3、4、5、6、11、12、13、19、20、21、22为 mark-to-base fmt1，所有 mark-class/anchor/base覆盖完整读；L5/6两类，其余单类，anchor均fmt1设计单位xy，无device/pointanchor。空anchor保持null，不能补成(0,0)。

GPOS chain fmt3 的 L2 调L18，L7→19、L8→20、L9→21、L10→22；L14→23、L15→24、L16→25；每个 subtable 的 backtrack/input/lookahead 顺序及应用位置都完整保留并读。L18对1265作xPlacement25/xAdvance10；L23对1234/1253作xPlacement320；L24对其六个覆盖glyph作xPlacement-540（1269为-400）。所有 lookup均无mark-filter-set位0x10；原flags仍决定是否忽略某glyph类。这些是可选排版引擎按脚本/feature上下文应用的规则，不能由存在表推定每次 Bitmap.text_size/draw_text 已应用全部。

kern v0 单一 format0 子表，coverage1 horizontal，完整908个有符号kerning pair全部独立读，search字段只是排序/检索数据。与 GPOS17 相同数值仍是两个独立原表；不推断宿主双重应用、取其中之一或完全忽略。全部1816个pair的两份源码阅读保留，不把同字节/同值算一次阅读后虚增范围。

## fixed B8 正反映射与正式结论

`wp17-messages-windows-input.md` 全319行、`wp17-draw-text-tags.md` 全117行按身份验证与 B8 完全相等后完整读。仅针对字体及其消费者接口作本任务的语义接收，不声称我独自批准其全部窗口/输入/消息内容。消息§3.4 的字体候选请求是 Power Green27、Power Green Small21、Power Green Narrow27，offset8；并未保证任何宿主实际安装或选中内嵌字体。来源 MessageConfig 完整文本已读：recursive候选数组依 Font.exist? 选首个非空可用名，未知/nil略过，全部失败得空串，getter缓存、setter失败回默认请求、pbSet*写name/size/y_offset。实际 Font.exist? 仍未运行。

Draw-tags§2 的 `<fs>`字号栈、`<fn>`字体栈及不存在回退Arial，与固定 DrawText 的完整 getFormattedTextFast/getFormattedText/getLastParam/getLastColors/drawSingleFormattedChar/drawFormattedChars 单位匹配。fn去尾空白后查询Font.exist?；字符项目携name/size，绘制普通字符前写回bitmap.font；格式化和批绘制正常尾部恢复oldfont，未把正常恢复泛化为异常ensure。源的每字符测量调用与实际宿主对单glyph的hinting结果不同。§3.1 明说夹具不是PowerGreen实测，§6/7与消息未决范围保留无运行确认，均未被字体表证明推翻。

正向：字体全部结构/程序/布局事实进入资源兼容证据和L04/L08边界，不要求未来复制原VM、专有glyph轮廓或native类层级。反向：正式字体请求、回退、参数栈、测量夹具边界由具名R消费者支持；表中的度量不能证明实际像素。表数量、opcode数、数据行数只校验覆盖，不作为正式条款分母。当前没有发现应修改 fixed B8 字体条款的新根因，required/optional/policy新提案均0；此为本有限范围贡献，非未接收的全局 NO_REQUIRED_UPDATE。没有提出缺陷，故无可交非提出者反证的缺陷案；接收者仍应真实检查本完整事实和负证据。

## 原生贡献接合及仍未知部分

父三份 native contribution 与 font-three-metadata contribution JSON均已全文实际接收，精确bytes/SHA见 `receptions.json`。它们的原始 FULL信用仍属于 `/root/resource_media_serialized_cloud`，我只授完整贡献内容接收，不改称我又读了3208条原生指令。6+7+7主函数及4cold、truetype168字节classprefix、20namepatterns和31表指纹、7具体回调全部内容已接合。690a00是driver探测分派；674110正常返回均0；faceinit6a6dc0只是SFNT服务/表/loca/fpgm/prep加载，不是全字体解释器。当前字体cvt长度648与31条指纹长度均不符；这只排除该指纹匹配分支，不排除其它name/selection路径。

L04保留：活动class注册/选择、SFNT service +08/+10实现、faceinit装入的69ace0/69ad40/6997a0/69b0c0/69e1e0回调body、glyph loader及VM执行器/下层CFG尚未完整建立。完整合同允许具名有限静态边界，未扩成无界逆向整Game.exe；也未把字符串或导出当运行证明。

已另完整接收 font-envelope contribution 的原 SFNT 5 header字段/19目录、7段13个zero gap、name 30记录和45个unused zero bytes、post 9 header字段、cmap 127原segment与format6 header。原350200=316(header+dir)+349871(tables)+13(padding)；覆盖算式不替代正文阅读。首次原38k JSON平台显示截断，随后完整无损compact对象在parent-envelope-compact-read.stdout实际全读，无遗漏且不新增原source FULL。

父另外6表的原始完整阅读仍归父：name、post、cmap，以及新FFTM/OS2/gasp三表贡献。后3表的所有字段/bit原值与前提已完整接收：gasp仅声明8→gray/17→gridfit/65535→both的偏好，OS2.fsType0不作法律裁定，Unicode/codepage掩码不代替cmap映射或实际渲染，FFTM原时间整数不伪造实际UTC。我的13表与父6表合19目录；此加法仅是单位覆盖，不增加独立票或全局裁决。

L08保留：准确目标宿主是否找到/选择字体、Font.exist?、text_size字宽、实际glyph hinting/字节码执行、脚本/feature选择、rasterizer实际采用gasp/scan请求、UI视觉均 NOT_EXECUTED。可读 fpgm/prep/glyph/布局此次均完整读完，不再作为“宿主缺失所以未读”的limit。读取完成不证明任何一组像素等价。

## 工具与引用

所有parser为任务内数据恢复/抽象检查，未import或执行fontTools程序，只用其中已全文理解的指令元数据literal；未运行字体VM/目标程序、安装、spawn、commit或push。完整辅助脚本与实际 stdout/stderr/exit/UTC在本目录保留；工具exit0非业务PASS。早期初始化若仅有平台回显而无本地单独UTC，原缺字段保留，不用后继capture冒充原命令。请求gpt-6.1-sol/ultra/default/normal/Fast off；actual逐字段UNVERIFIED。

指令/布局术语核对采用primary技术定义：[TrueType instructions](https://learn.microsoft.com/en-us/typography/opentype/spec/tt_instructions)、[GPOS](https://learn.microsoft.com/en-us/typography/opentype/spec/gpos)、[GSUB](https://learn.microsoft.com/en-us/typography/opentype/spec/gsub)、[GDEF](https://learn.microsoft.com/en-us/typography/opentype/spec/gdef)。这些参考解释数据格式，不替代原字体与完整规则的实际阅读。
