"""Documentation indexes over already presented/read fixed inputs.
Only writes this task directory. Structural indexing does not establish PASS.
Handwritten assessments remain in semantic-notes and individual findings.
"""
from pathlib import Path
import re, json, hashlib
OUT = Path(__file__).resolve().parent
WORK = OUT.parents[4]
ROUND = OUT.parents[1]
R = WORK/'reference/pokemon-essentials'
FORMAL = 'deliverables/final-specification-set/'
def save(name,obj):
    assert Path(name).name == name
    (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def src(path,start,end):return {'path':path,'lines':[start,end]}
def method_units(path):
    lines=(WORK/path).read_text().splitlines();rows=[]
    for i,l in enumerate(lines):
        m=re.match(r'^(\s*)def\s+(\S+)',l)
        if not m:continue
        indent=m[1]
        if re.search(r';\s*end\s*$',l):end=i+1
        else:
            end=next((j+1 for j in range(i+1,len(lines)) if lines[j]==indent+'end'),len(lines))
        rows.append({'unit':m[2],'source':src(path,i+1,end)})
    return rows
compat=[];field_index=[]
consumer_refs={
 'Map':['Compiler::MapData (Compiler_MapsAndEvents293–435)','map consumers WP13; native serialized-class selection UNKNOWN'],
 'MapInfo':['Compiler.import_new_maps45–83'],
 'Event':['Compiler converters473–807 and generated page consumer WP13'],
 'EventCommand':['Compiler command builders88–249; Interpreter dispatch11–118'],
 'MoveRoute':['Compiler generate_move_route88–118; WP13 route consumer'],
 'MoveCommand':['Compiler generate_move_route88–118; WP13 route consumer'],
 'CommonEvent':['Compiler.pbEachPage281–288; main commonEvent phase1734–1749'],
 'Tileset':['Compiler MapData348–434; resource/terrain owner'],
 'System':['Compiler MapData296–309,415–434 and Game_System audio consumer'],
 'AudioFile':['Audio_Play1–38,52–233; generated Door enter/Exit Door requests'],
 'BGM':['Audio_Play52–89 conditional compatibility fallback'],
 'BGS':['Audio_Play152–189 conditional compatibility fallback'],
 'ME':['Audio_Play102–139 conditional compatibility fallback'],
 'SE':['Audio_Play202–233 conditional compatibility fallback'],
 'Animation':['BattleAnimationPlayer170–228 extension and SpriteAnimation consumer; native selection UNKNOWN'],
 'Cache':['RPG_Cache1–144 overrides load_bitmap/tile; inherited category/clear methods require selected base'],
 'Sprite':['RPG_Sprite1–84 overrides animation/update/position/effect; SpriteAnimation consumer'],
 'Weather':['Overworld_Weather1–528 replaces behavior; no direct current use of old 40-sprite body proved']
}
for bid in ('BIN-0079','BIN-0080','BIN-0081'):
    path=str((ROUND/'evidence/bin-readable'/f'{bid}.txt').relative_to(WORK))
    lines=(WORK/path).read_text().splitlines();classes=[];current=[]
    for i,line in enumerate(lines):
        e=re.match(r'^(\s*)end\s*$',line)
        if e:
            current=[x for x in current if x[0]<len(e[1])]
        c=re.match(r'^(\s*)class\s+(\S+)',line)
        if c:
            n=len(c[1]);current=[x for x in current if x[0]<n];current.append((n,c[2]));cl='::'.join(x[1] for x in current)
            end=next((j+1 for j in range(i+1,len(lines)) if lines[j]==c[1]+'end'),len(lines))
            classes.append({'unit':cl,'line':i+1,'end':end,'root':current[0][1]})
        owner='::'.join(x[1] for x in current)
        fields=re.findall(r'attr_(?:accessor|reader|writer)\s+(.+)',line)
        for spec in fields:
            for name in re.findall(r':([A-Za-z_]\w*)',spec):
                field_index.append({'id':f'{bid}-FIELD-{i+1}-{name}','unit':owner,'source':src(path,i+1,i+1),'field':name,'fact':'对应命名数据属性的读写/只读声明；构造默认和行为分派见本轮手写类组分析','consumer':consumer_refs.get(current[0][1] if current else '',['本套兼容数据定义；未定位当前游戏的显式静态消费者，动态/原生选择UNKNOWN']),'disposition':'CONDITIONAL_COMPATIBILITY_POLICY_NO_ORIGINAL_CLASS_ARCHITECTURE_REQUIRED','assessment_basis':'semantic-notes.md#兼容明文三单元','index_evidence':'STRUCTURE_ONLY_NOT_AUTO_PASS'})
    for j,c in enumerate(classes):
        end=c['end']
        compat.append({'id':f'{bid}-CLASS-{c["line"]}','unit':c['unit'],'source':src(path,c['line'],end),'fact':'该声明及其方法/默认数据已在三单元连续全文中审读；精确方法与字段另索引，嵌套类不误当全部父类范围','consumer':consumer_refs.get(c['root'],['本套数据库兼容定义；未定位当前游戏显式静态消费者，native/dynamic UNKNOWN']),'spec_or_policy':'WP13/WP15/WP16/WP75有对应当前逻辑合同；其它旧RPG数据库仅独立可选兼容policy','semantic_basis':'semantic-notes.md#兼容明文三单元','runtime_selection':'UNKNOWN'})
    for m in method_units(path):
        compat.append({'id':f'{bid}-METHOD-{m["source"]["lines"][0]}',**m,'fact':'全文已人工审读的方法单元；输入保留、默认赋值、谓词集合、运算、缓存和分派详见该类手写分析','consumer':'同类调用/构造或上述外部散文件消费者；实际RGSS选择UNKNOWN','spec_or_policy':'CONDITIONAL_COMPATIBILITY_POLICY','semantic_basis':'semantic-notes.md#兼容明文三单元'})
save('compat-field-index.json',field_index)
save('compat-unit-forward.json',compat)
forward=[]
for name in ('scripts_combine.rb','scripts_extract.rb'):
    path='reference/pokemon-essentials/'+name
    for m in method_units(path):
        start=m['source']['lines'][0]
        clause='WP75§12.1' if start<69 else 'WP75§12.4' if start<76 else 'WP75§12.2' if start<119 else 'WP75§12.3' if start<154 else 'WP75§12.1分阶段失败'
        forward.append({'id':f'{name}-{start}',**m,'fact':clause+'；方向/命名/清树/写出次序和异常前缀已手写核对','consumer':name+':182–183选择的根作者入口；其余为有限内部调用','formal':clause,'status':'SEMANTIC_READ_WITH_HOST_LIMITS','basis':'semantic-notes.md#根作者工具与Formal接合'})
    forward.append({'id':name+'-entry','unit':'root authoring direction','source':src(path,182,183),'fact':'两条末行只启用对应一个方向','consumer':'作者显式启动（本轮未执行）','formal':'WP75§3.2','status':'SEMANTIC_READ'})
path='reference/pokemon-essentials/Data/Scripts/021_Compiler/004_Compiler_MapsAndEvents.rb'
def compiler_clause(start):
    for a,b,c in [(1,44,'§8.1'),(45,87,'§4'),(88,253,'§15.2/§7.3'),(254,269,'§15.3'),(270,280,'§15.5'),(281,439,'§15.1'),(440,472,'§5.3'),(473,764,'§5'),(765,814,'§6'),(815,904,'§7.2'),(905,935,'§7.3'),(936,950,'§7.1'),(951,975,'§8.1'),(976,996,'§15.4'),(997,1134,'§8.2'),(1135,1577,'§8.3–§9'),(1578,1679,'§7.4'),(1680,1751,'§10')]:
        if a<=start<=b:return 'WP75'+c
    raise ValueError(start)
for m in method_units(path):
    start=m['source']['lines'][0]
    forward.append({'id':f'CV-SOURCE-{start}',**m,'fact':compiler_clause(start)+'本轮全文生成/识别/失败/停用/写出合同核对','consumer':'Compiler.compile_trainer_events1683–1750与Compiler.compile_all1020–1037；辅助unit调用关系在源全文核对','formal':compiler_clause(start),'status':'SEMANTIC_READ_WITH_TWO_PROPOSALS','notes':'候选R6-B-001/002为待非提出者反证；非其它unit通过替代','basis':'logs连续1–1751及semantic-notes'})
forward.extend([
 {'id':'CV-REPLACEMENTS','source':src(path,2,38),'unit':'35 ordered compatibility replacements','fact':'35条顺序全出现替换，随后两规则；与WP75逐行表对应','formal':'WP75§8.1:176–217','consumer':src(path,951,974),'status':'SEMANTIC_READ'},
 {'id':'CV-DISABLED','source':src(path,1232,1397),'unit':'disabled transfer block','fact':'整块已读但停用；不得提升其中通道消费者为当前可达','formal':'WP75§8.4/§7.3','consumer':'无活动调用；唯一通道调用位于停用块','status':'SEMANTIC_READ_INACTIVE'},
 {'id':'HTML','source':src('reference/pokemon-essentials/townmapgen.html',1,414),'unit':'all HTML helpers and handlers','fact':'每函数输入/输出/事件和失败前缀见semantic-notes；无文件写入，外部资源与浏览器未知','formal':'WP75§13;CV-M28/M30','consumer':'作者浏览器页面→textarea→手工PBS复制；本轮未浏览器执行','status':'SEMANTIC_READ'},
 {'id':'DOC-ANIM','source':src('reference/pokemon-essentials/animmaker.txt',1,26),'unit':'complete tool usage text','fact':'XML文档及double-size陈述，与CIL定义细节分列','formal':'WP74§18','consumer':'作者命令行输入；无实际衔接.anm证据','status':'SEMANTIC_READ_DOC_ONLY'},
 {'id':'DOC-EXT','source':src('reference/pokemon-essentials/extendtext.txt',1,4),'unit':'complete tool usage text','fact':'RMXP文本/脚本窗放大文档与有限静态请求分列','formal':'WP75§14','consumer':'作者显式启动，不是当前游戏窗口运行链','status':'SEMANTIC_READ_DOC_ONLY'},
 {'id':'LOADER','source':src(str((OUT/'logs/loader-from-current-bytes.txt').relative_to(WORK)),1,49),'unit':'fixed one-section loader plaintext','fact':'同本轮根工具literal和当前archive已证明字节身份；本层.rb先排序、子目录后递归、读文件保护外、ScriptError/普通错误/899/900日志分层，前缀不回滚','formal':'WP75§12.4;U07-L01–03','consumer':'当前归档Main内容入口；实际host未执行','status':'SEMANTIC_READ_DATA_DECODE_ONLY'}
])
metadata=json.loads((ROUND/'evidence/resource-parser/binary-interface-audit.json').read_text())
cli=next(r for r in metadata['records'] if r['path']=='animmaker.exe')['CLI']
cil=[]
for m in cli['methods']:
    n=m['method_token']&0xffffff;p=OUT/'logs'/f'animmaker-il-{n:02d}.txt'
    cil.append({'id':f'ANIM-IL-{n:02d}','method':m['name'],'source':{'path':'reference/pokemon-essentials/animmaker.exe','method_token':hex(m['method_token']),'file_offset':m['file_offset'],'code_size':m['code_size'],'sha256':m['sha256'],'IL_log':str(p.relative_to(OUT)),'log_lines':[1,len(p.read_text().splitlines())]},'instruction_count':m['instruction_count'],'all_instructions_branches_EH_read':True,'fact_basis':'semantic-notes.md#animmaker-全15方法静态审查','consumer': '内部方法14/15或缓存/构造调用；方法10没有本程序集调用者','formal_or_policy':'WP74§18文档边界；可选新静态authoring compatibility附录，非既有必修矛盾','runtime_and_external_libraries':'UNKNOWN_NOT_EXECUTED'})
save('animmaker-method-forward.json',cil)
forward.extend(cil)
native=[]
for a,b,note in [(0x401000,0x401219,'CRT/SEH有限启动及异常展开/信号路径'),(0x401219,0x40129b,'PE入口，CRT args→工作主函数→exit'),(0x40129c,0x40131f,'EnumWindows callback;完整重新对齐解码'),(0x40131f,0x401352,'宿主窗口枚举found门'),(0x401352,0x4013a6,'mutex创建/已存在/失败−1分支'),(0x4013a6,0x4013c2,'非0/非−1清句柄'),(0x4013c2,0x401600,'四窗请求/子控件请求/150ms/Sleep/退出循环'),(0x401600,0x4016cc,'17 IAT trampoline与padding；导入链接不等于执行')]:
    native.append({'id':f'EXT-VA-{a:x}','source':{'path':'reference/pokemon-essentials/extendtext.exe','VA_half_open':[hex(a),hex(b)],'file_half_open':[1024+a-0x401000,1024+b-0x401000]},'fact':note+'，详见手写静态工作体分析','consumer':'仅工具工作循环或CRT局部；宿主调用结果UNKNOWN','formal_or_policy':'WP75§14仍文档边界；可选有限static native请求合同','status':'STATIC_FINITE_BODY_REVIEW_NOT_FULL_NATIVE_CFG_PROOF'})
save('extendtext-forward.json',native);forward.extend(native)
forward.append({'id':'BIN-0708','source':src(str((ROUND/'evidence/bin-readable/BIN-0708.txt').relative_to(WORK)),1,1),'fact':'这是SoundFont load帮助候选；reset默认1、bank offset默认0为文本陈述；不含兼容RPG程序','consumer':'未知native命令帮助消费者，非游戏开放shell证明','formal_or_policy':'WP15音频请求及SF2边界；不可据帮助推运行能力','status':'SEMANTIC_READ_HELP_LITERAL_ONLY'})
save('forward-matrix.json',{'rows':forward,'compat_units':'compat-unit-forward.json','compat_fields':'compat-field-index.json','shader_complete55':'shader-counter/forward-traceability.json','controller_complete1678_and_PE_structures':'controller-meta/forward-matrix.json','not_auto_PASS':'索引由工具生成；语义依据是本轮呈现日志和手写事实，所有宿主未知分列'})
# Every WP75 block gets an exact global clause identity; manually read ranges
# determine the source link. This is not a repository-wide formal acceptance.
blocks=json.loads((ROUND/'inventory/formal-block-denominator.json').read_text())
wp=FORMAL+'demo-dx/wp75-project-conversion-and-authoring-tools.md'
zones=[(1,32,[src(path,1,1751),src('reference/pokemon-essentials/scripts_extract.rb',1,183)],'scope/purpose/domain records'),(33,49,[src('reference/pokemon-essentials/Data/Scripts/021_Compiler/001_Compiler.rb',1020,1117),src('reference/pokemon-essentials/scripts_extract.rb',182,183)],'authoring trigger and directional gate'),(50,57,[src(path,45,83)],'new map registration'),(58,108,[src(path,440,763)],'trainer collection/parsing/pages'),(109,114,[src(path,771,807)],'item event'),(115,139,[src(path,815,903),src(path,415,434)],'door route and switch prefix'),(140,148,[src(path,847,897)],'follower consumer handoff to O/WP13; not complete follower source re-review here'),(149,152,[src(path,1398,1412)],'independent transfer'),(153,158,[src(path,231,249),src(path,919,934),src(path,1232,1397)],'inactive passage definition'),(159,167,[src(path,1583,1678),src(path,325,340)],'counter aliases/shared pages'),(168,217,[src(path,2,38),src(path,951,974)],'ordered 35 replacement rows and2rules'),(218,236,[src(path,979,1133),src(path,1499,1574)],'six family rewrite/revisit'),(237,244,[src(path,1192,1223),src(path,1503,1532)],'sell/order and money; candidate002'),(245,265,[src(path,1135,1191),src(path,1232,1397)],'healing prefix/inactive/route handoff'),(266,283,[src(path,1419,1498)],'message split/merge/revisit'),(284,292,[src(path,1683,1750),src(path,348,434)],'driver/save/failure candidate001'),(293,301,[src('reference/pokemon-essentials/Data/Scripts/020_Debug/003_Debug menus/008_Debug_FilenameUpdater.rb',1,89),src('reference/pokemon-essentials/Data/Scripts/001_Technical/002_RubyUtilities.rb',140,170)],'rename/copy/delete prefix'),(302,336,[src('reference/pokemon-essentials/scripts_extract.rb',1,183),src('reference/pokemon-essentials/scripts_combine.rb',1,183)],'roundtrip two directions'),(337,353,[src(str((OUT/'logs/loader-from-current-bytes.txt').relative_to(WORK)),1,49)],'loader data-decoded and read'),(354,381,[src('reference/pokemon-essentials/townmapgen.html',1,414)],'HTML state/author text/resources'),(382,387,[src('reference/pokemon-essentials/extendtext.txt',1,4)],'documentation policy with newly readable native evidence separate'),(388,414,[src(path,88,468),src('reference/pokemon-essentials/Data/Scripts/003_Game processing/004_Interpreter_Commands.rb',392,443)],'shared builders/queries/parser/condition consumer'),(415,438,[src(path,1,1751),src('reference/pokemon-essentials/scripts_extract.rb',1,183)],'summary/test/dependency/limits; external owners retain proofs')]
reverse=[]
for b in blocks:
    if b['path']!=wp:continue
    line=b['start_line'];z=next(z for z in zones if z[0]<=line<=z[1])
    reverse.append({'clause_id':b['id'],'formal':src(wp,b['start_line'],b['end_line']),'source':z[2],'assessment':z[3],'status':'FULL_TEXT_READ_SOURCE_CROSSCHECK_WITH_RETAINED_OWNER_HANDOFFS','preconditions':'合法数据/相应门与资源；静态定义/生成产物与实际宿主执行分开；明示异常前缀无整体回滚','proposal': 'R6-B-001' if b['start_line']<=289<=b['end_line'] or b['start_line']<=392<=b['end_line'] else 'R6-B-002' if b['start_line']<=241<=b['end_line'] else None})
tests=FORMAL+'test-catalog/demo-dx-wp72-73-74-75-76-77.md'
for b in blocks:
    if b['path']!=tests:continue
    a,c=b['start_line'],b['end_line'];owned=(152<=a<=181 or a in [278,279,281,284,287,291,292,295,303,304,305,306,307,308])
    reverse.append({'clause_id':b['id'],'formal':src(tests,a,c),'read_status':'FULL_DOCUMENT_READ_THIS_ROUND','source_assessment':'CV/new authoring source clauses independently checked' if owned else 'CROSS_MODULE_READ_ONLY_NOT_SOURCE_CERTIFIED_BY_R6_B','source':[src(path,1,1751),src('reference/pokemon-essentials/scripts_extract.rb',1,183),src('reference/pokemon-essentials/townmapgen.html',1,414)] if owned else [],'preconditions':'Each named input remains conditional NOT_EXECUTED; other DG/CE/WE/AN/GN/DM domain owners retain source denominator','proposal':'R6-B-002' if a<=162<=c else None})
save('reverse-matrix.json',{'WP75_all_blocks':sum(r.get('status') is not None for r in reverse),'rows':reverse,'kernel_handoffs':[{'formal':src(FORMAL+'generic-kernel/wp04-pbs-lifecycle.md',231,279),'source':src('reference/pokemon-essentials/Data/Scripts/021_Compiler/001_Compiler.rb',1020,1117),'fact':'converter saves may precede outer compile cleanup; no rollback; rules delegated WP75'}, {'formal':src(FORMAL+'generic-kernel/wp07-diagnostics-files-http.md',119,167),'fact':'local catch boundaries cannot promote root loader/file/native API success or fixed diagnostics; root/K owns whole diagnostic source'}],'shader_reverse':'shader-counter/reverse-traceability.json','controller_meta_reverse':'controller-meta/reverse-matrix.json'})
save('matrix-index-counts.json',{'compat_class_and_method_rows':len(compat),'compat_accessor_field_rows':len(field_index),'root_source_forward_rows':len(forward),'CIL_methods':len(cil),'extendtext_finite_units':len(native),'WP75_global_blocks':sum(b['path']==wp for b in blocks),'reverse_rows':len(reverse),'indexing_is_not_semantic_PASS':True})
print(json.dumps(json.loads((OUT/'matrix-index-counts.json').read_text()),ensure_ascii=False))
