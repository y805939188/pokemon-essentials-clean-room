"""Finalize concrete discovery scope and report; record limits, never synthesize semantic credit."""
from pathlib import Path
import json,datetime
P=Path(__file__).resolve().parent
load=lambda n:json.loads((P/n).read_text())
def wr(n,x):(P/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
units=load('new-program-and-data-inventory.json')['units']
common={'7_minimum_write_set_and_formal_consumers':'Only own audit directory. Frozen B8 scope, WP15 and WP17 completely read as context; their exact identities remain in formal-context-identities.json. No whole-domain normative no-required finding or formal/catalog revision is issued. Root actual primary receivers must adjudicate media, native and global formal implications.','8_history_synchronization_regression':'Every candidate original ID/line/offset/end/SHA is conserved in full-disposition-ledger.jsonl.gz. Previous191850 inventory types and5135 prior semantic credit are not expanded. All business vectors NOT_EXECUTED, reference/model/host added business execution0; UPDATE_NOT_STARTED. No commit/push/install/target execution.'}
findings=[]
def add(pid,ids,sections):
 findings.append({'id':pid,'kind':'NEW_FINITE_SOURCE_DISCOVERY_STATIC_RECEPTION','units':ids,'proposer':'/root/binary_remaining_texts','independent_nonproposer_reception':'PENDING_ROOT','normative_change_claim':'NONE_ISSUED','eight_sections':{**sections,**common}})
add('GR8-BIN-R8-SFNT-001',['GR8-GAME-SFNT-001'],{
'1_exact_object_identity':'Game[10217888,10568088),350200B SHA e5b0af421ea2bfbc1ac8d251d647268087ae82786234c57f757d1f0b90fa8b49; exact candidate intersections/name records/table directory/glyph and cmap structures in new-program-and-data-inventory.json and embedded-font-structure.json.',
'2_positive_fact':'Complete19table boundaries/checksums/glyph2587/loca/hmtx/cmap structure retained; every30name record and2298post glyph-name identities received. All8 standaloneTTF wholebytes and complete corresponding tables compared, none equal.',
'3_ordinary_vector':'Native209072 passes the exact350200B memory span through3823040 and6817536 memory-stream wrappers. Metadata identifies Liberation Sans Regular2.00.1 and Arimo metric compatibility; metadata strings are retained as statements, not legal conclusions.',
'4_minimum_counterexample':'Single exact wholefont SHA differs from each8 known standalone fonts, and complete corresponding table comparisons also differ. The set of8 standaloneTTF sources is not the complete set of font media embedded in R.',
'5_failure_cancel_partial_commit':'No font decoder/rendering execution. Native load wrappers are statically received; final indirect decoder/failure/rendering effects remain open. No resource replacement or write.',
'6_strongest_rebuttal_correct_preservation':'Presence plus metadata/memory binding does not establish active font selection, glyph visual output, outline/instruction behavior, pixel parity or licensing outcome. Retain these for actual media primary; do not absorb them under numeric subrun type proof.'})
add('GR8-BIN-R8-HRTF-001',['GR8-GAME-HRTF-001'],{
'1_exact_object_identity':'Game[11394336,11474689),80353B SHA162825b9b3a5ff4d93c1fcc9682ee6e7483da89e37ceebeaa6837bdc19eaa974; all111 candidate IDs and exact subranges in new inventory/embedded-hrtf-structure.json.',
'2_positive_fact':'MinPHR03,44100Hz,mono,32taps,one1400mmfield,19elevations,828IR,26496 signed24coefficients and828delaybytes fully structurally recovered. Native bounded window exactly binds begin/end span.',
'3_ordinary_vector':'Static native3447632 displayed window receives the exact80353B span; all elevation counts and coefficient/delay layout conserved for future receiver.',
'4_minimum_counterexample':'The embedded44100Hz/32tap blob differs in whole bytes and header dimensions from installed48000Hz/64tap comparator; the external file is not a byte-identical substitute.',
'5_failure_cancel_partial_commit':'No hearing/convolution/backend execution, no data installation or replacement. Whole3447632 function was not read; only explicitly logged1310–1342 window.',
'6_strongest_rebuttal_correct_preservation':'File signature and numeric layout do not approve spatial perception, delay interpretation quality, selected device/backend or runtime fallback. Numeric type exemption stays within111 exact subruns; future media semantic reception remains open.'})
add('GR8-BIN-R8-CONTROLLER-001',['GR8-GAME-CONTROLLER-001'],{
'1_exact_object_identity':'Complete257 builtin records,256-pointer table[11619560,11621616) includingnull plus hardcodedxinput record; full perrecord bytes/SHA/GUID/name/all ordered fields and257 candidates in builtin-controller-readset.json.',
'2_positive_fact':'All119 ordered patterns/209names received; native3879264 registration,3874736 record priority/update handling,3874224 field materializer and3873328 binding parser complete.15button+6axis NULL-terminated target name tables received.',
'3_ordinary_vector':'Builtin priority0,environment-file priority1,inline priority2. Concrete fields map±aN,bN,hN.mask onto21 finite targets, includingtrigger0..32767 andsource tilde inversion.',
'4_minimum_counterexample':'Record155/P79 and228/P109 have empty guide;record222/P107 has empty shoulders;record149/P75 lacks a. Reading one generic21field pattern would lose these exact meaningful differences. Complete patterns/names preserve them.',
'5_failure_cancel_partial_commit':'Unknown/oversize/malformed field paths signal error and outer loop can continue; realloc failure resets count0. Lowerpriority leaves old mapping, equal/higher replaces and notifies. No physicalcontroller orgame action execution.',
'6_strongest_rebuttal_correct_preservation':'Builtin257 is a second table, not the earlier external1666 record table. Its21 parser targets do not prove platform filtering, attached-device match, runtime mapping choice or gameAction/Use bridge. WP17 finite targets remain context, not universal mapping approval.'})
add('GR8-BIN-R8-GLYPHDICT-001',['GR8-GAME-GLYPHDICT-001'],{
'1_exact_object_identity':'Game[11961024,12017021),55997B SHAb6b6cf98e05fa65c35b1dc84b2fb588203a5babba75ba0236a361b82abb4ff68.284 candidate intersections; exactnodes/entries and complete source bytes identity in glyph-dictionary-structure.json.',
'2_positive_fact':'52rootchildren/5642trienodes/4401name→16bitcodepoint mappings recovered; all55997bytes structurally covered, no cycles/duplicate names/remainder. All4401 mappednames/codepoints actually read; native7396800 entire1009B lookup received.',
'3_ordinary_vector':'Native lookup reads real52root children viaBE16 offsets and followscompressedlabel/terminalcodepoint fields. Independent inert parser preserves the same trie shape and exact mappings.',
'4_minimum_counterexample':'Delta→2206 differs from Deltagreek→0394;Omega→2126 differs from Omegagreek→03A9. Treating names as merely binary gibberish or normalizing aliases loses recoverable dictionary meaning.',
'5_failure_cancel_partial_commit':'Unknown names/empty orsuffix forms have native return branches received, no lookup businessexecution. No font modification, conversion or targetprogram run.',
'6_strongest_rebuttal_correct_preservation':'A glyph-name dictionary is not a font, renderedglyph set, universalUnicode normalization or proof of game input charset. Whole external FreeType initializer equality is bounded type evidence; actual metadata reception derives from the recovered target bytes.'})
dxids=[u['id'] for u in units if u['kind']=='NEW_COMPLETE_COMPILED_SHADER_CONTAINER']
add('GR8-BIN-R8-DXBC-001',dxids,{
'1_exact_object_identity':'12completeDXBC containers at11639456..11655168 with exact individual offset/end/SHA/chunk directories/candidate IDs in new-program-and-data-inventory.json;182 candidate intersections. Total194SHDR+218Aon9 instructions fully recovered.',
'2_positive_fact':'All raw instruction controls/flags/masks/swizzles/floatbits and printableRDEF/ISGN/OSGN metadata received in complete206/230line views. Native3984304 vertex and3984576 pixel creation helpers complete; originalblob pointers/sizes retained.',
'3_ordinary_vector':'Vertex does two4×4 transforms andUV/colorpass-through;9pixels use3YUV coefficient sets with2planeUV/VU or3planes, alpha1 andvertexcolor multiply; plaintexture multiply andsolidcolor programs also present. Aon9 vertex adds viewport adjustment.',
'4_minimum_counterexample':'Exact container[11654592,11655168) contains DCL_INPUT_PS,DCL_OUTPUT,MOV output=inputcolor,RET; its full program is recoverable independently of opaque device/driver behavior. This defeats a blanketallcompiledprogrambytesopaque classification.',
'5_failure_cancel_partial_commit':'Native creation helpers testHRESULT/errorformat branches; completepixel selectorindexes11 pointer-sizepairs withoutown boundscheck. Outerindexpreconditions/devicecaller not proven. NoGPUcompile/render/run orresourcecommit.',
'6_strongest_rebuttal_correct_preservation':'Complete programtoken reading does not verify DXBCchecksum algorithm, everyAon9translation-header field, device/vtable selection, actualcolor-space configuration, shaderoutputpixels or runtime parity. Those remain separate explicit limits.'})
wr('proposals.json',{'schema':'gr8.binary.remaining.proposals/v2','discoveries':findings,'normative_gap_claims':[],'no_required_scope':'No whole-domain normative no-required adjudication. All5 new finite discovery proposals await actual nonproposer reception. Child GR8-RZ-YARB-001 has actual independent parent counterproof in its separate file.'})
p=load('progress.json');p.pop('semantically_received',None);p['content_received_or_exactly_typed_occurrences']=57948;p['full_native_semantic_approval']=False;p['updated_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();wr('progress.json',p)
(P/'review.md').write_text('''R8 剩余 binary 文本有限审读交付，保留开放语义边界。

原分母 57,948 个出处／41,849 条不同完整文本全部守恒。Game 37,041 个出处由本真实上下文审读；Ruby 20,817 与 zlib 90 由实际新上下文 `/root/binary_ruby_zlib_remaining` 完整逐文阅读，并经本上下文正式接收。`full-disposition-ledger.jsonl.gz` 保留每项原 candidate_id、inventory_line、encoding、offset/end、原 bytes SHA、read_id、阅读归属、类型证据及消费者限制。`bidirectional-mapping.json` 保留完整文本和全部出处。可得字面内容未接收为 0；这不是全 binary／native 行为／全 formal PASS。

Game 的 18,436 个出处具精确类型证据：8,501 原结构（SFNT5,438二进制子run、2,298glyph-name身份、764真实重定位指针、1PE节名）、1,283数值查表、154EC参数、111HRTF、603音频窗、6,208完整iconv数值数组、777FluidSynth数值数组、748完整标量数组、14精确数值指令操作数、37完整GUID。仅 active 文件计数，旧INVALID/VALID版本保留历史但不重复计。2,298 glyph-name 与284已解码字典候选另标 metadata实际阅读，不能把有效名称掩为纯binary。每项证明严格局限于原范围，不继承旧191,850项的更宽豁免。

另 182 个候选属于12个新完整 DXBC 容器：194条SHDR与218条Aon9指令、所有打印metadata已实际完整读过，含顶点矩阵、YUV三系数/通道变体、纹理乘色和纯颜色程序。257条第二builtin SDL controller记录通过119顺序pattern、209名称及全部原GUID/bytes接收；四个完整native parser/register函数与15button＋6axis目标表已读。二者仍不证明设备/平台选择或game Action/Use桥。

发现并保存新媒体：Game内350,200B SFNT字体，SHA e5b0af421ea2bfbc1ac8d251d647268087ae82786234c57f757d1f0b90fa8b49；19表、30条name、2,587glyph与cmap结构完整，和8独立TTF的完整bytes及每张完整表均不相同。另80353B MinPHR03 HRTF（44100Hz／mono／32tap／828IR）。字体轮廓指令／像素与HRTF听感／卷积尚未媒体语义接收。`media-handoff.json` 明确后继主责未接收，旧Game PNG/DIB仅结构接收也未偷闭。

55,997B压缩glyph-name字典全部结构恢复为5,642节点／4,401名称→Unicode项，4,401行已实际连续全读，完整1009B native lookup已接收。别名差异、PUA与control名称保留原值；它不等同字体或通用Unicode规范化。

Ruby/zlib 真实子审的全部92项manifest身份和20,907原候选字段均独立核过。本上下文实际完整读了16 YARB的654对象、171 ISEQ参数/keyword/optional/catch/outer和1,002指令，以及536整NUL单元、115 builtin记录、120索引/名称/函数指针接线、16 caller窗口、三个完整loader与cold。已读懂的154行inert decoder安全复制到自己隔离目录重跑，恢复体与子审逐字节一致；独立PE映射还核456指令行原bytes、103RIP位移、74rel32目标。`ruby-child-independent-counterproof.json` 实际非提出者接受 GR8-RZ-YARB-001 的有限发现与静态内容。NilClass两个无native R operand的常量返回程序反驳整块opaque；Marshal/IO/GC等包装器委托115个native叶的事实同时反驳恢复包装器就批准全部native的越界结论。13,574条子literal阅读只归子context，不冒本人的全量literal阅读。

`remaining.json` 精确保留18,166个Game已字面阅读但完整type或native消费者语义未闭的候选ID。它们获得无inventory豁免的逐文阅读状态，不能据字面存在签完整CFG或全formal no-required。全体61,269条RIP引用由独立静态反汇编逐raw-byte/位移验证；其中6,169候选有直接句法引用，完整边在`candidate-native-direct-consumers.jsonl.gz`。机械处理2,419,046条指令不冒人工全native阅读；无直接引用也不证明无消费者。Game PE全部import名称实际已读，确导入独立zlib1.dll四个deflate入口；Ruby自己的Init_zlib builtin扩展与独立DLL不得混同。

自己的完整formal上下文仅冻结B8 scope155行、WP15全部224行、WP17全部319行，身份在`formal-context-identities.json`。其它子审R/formal阅读按精确路径/范围归实际子reader。没有签完整binary／所有program／所有media／全formal no-required；五个新发现八节提案在`proposals.json`，等root安排实际非提出者接收，原四个GR8-BIN裁决仅归root的有限反证。

全部目标业务、模型、参考运行与宿主新增业务执行为0，所有业务向量NOT_EXECUTED；UPDATE_NOT_STARTED。未commit/push/install/spawn，未修改旧任务、R、formal、planning、audit、history或root状态。静态工具退出和字节断言仅TOOL_VALIDATION。请求配置gpt-6.1-sol／ultra／default普速／Fast off；实际model/effort/tier/speed/UUID无权威回显，逐字段UNVERIFIED。

失败与更正历史保留：font cmap6、numeric页目录/错误delta、DXBC DP2、iconv尾零、scalar维度/Latin1等失败未用作当前证明；修正后active结果单计。补充source archives及其matched完整initializer仅提供有界格式/类型证据，未运行、未冒目标版本等价或全源码FULL_READ。大输出截断不授全文信用；连续阅读中的两次截断已逐缺口修复，后续机械清单截断只作导航。
''',encoding='utf-8')
print(json.dumps({'discoveries':len(findings),'review_bytes':(P/'review.md').stat().st_size,'open_semantic_boundaries':18166}))
