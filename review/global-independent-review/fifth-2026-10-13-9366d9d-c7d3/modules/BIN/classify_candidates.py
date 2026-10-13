"""Finite string-pool classification and data parsing. No reference execution."""
import bisect,collections,hashlib,json,pathlib,re,struct
O=pathlib.Path(__file__).parent;P=O.parent/'RES';R=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Game.exe');r=R.read_bytes()
blocks=json.loads((O/'block-inventory.json').read_text())['blocks'];shader=json.loads((O/'shader-behavior.json').read_text());res=json.loads((P/'binary-interface-audit.json').read_text())['records'][0]
source=[json.loads(v) for v in pathlib.Path('/tmp/gr5-bin-readable/strings.jsonl').read_text().splitlines()]
byoff={v['offset']:v for v in source if v['encoding']=='ascii'}
# The size-indexed dictionary layout is read from the executable itself, not an external library.
bits=list(r[12051584:12051616]);offs=list(struct.unpack_from('<32I',r,12051616));base=12051776;dcells=[];dg=[]
for n in range(4,25):
 a,b=offs[n:n+2];assert b-a==n*(2**bits[n]);invalid=[]
 for idx,k in enumerate(range(a,b,n)):
  d=r[base+k:base+k+n]
  try:d.decode('utf8');valid=True
  except UnicodeDecodeError:valid=False;invalid.append(idx)
  dcells.append({'width':n,'index':idx,'offset':base+k,'size':n,'sha256':hashlib.sha256(d).hexdigest(),'valid_utf8':valid})
 dg.append({'width':n,'count':2**bits[n],'start':base+a,'end':base+b,'invalid_utf8_indices':invalid})
assert len(dcells)==13504
# Additional built-in controller rows are outside the inherited multiline database.
old=res['embedded_readable']['controller_records'];controllers=[];cb=collections.Counter()
for v in source:
 s=v['text']
 if v['block']=='B00' or not re.match(r'^(?:[0-9a-fA-F]{32}|xinput),',s):continue
 p=s.split(',');bd=[]
 for field in p[2:]:
  if not field:continue
  key,val=field.split(':',1);q={'target':key,'binding':val}
  if val=='':q['meaning']='有键而绑定值为空；不假定宿主忽略、解除或拒绝。'
  else:
   m=re.fullmatch(r'([+-]?)([abh])(\d+)(?:\.(\d+))?(~?)',val);assert m,(v['offset'],val)
   q.update({'source_kind':{'a':'轴','b':'按钮','h':'方向帽'}[m[2]],'source_index':int(m[3]),'source_half':{'+':'正半轴','-':'负半轴','':'完整/未限定'}[m[1]],'hat_mask':int(m[4]) if m[4] else None,'axis_inverted_marker':bool(m[5])})
   q['meaning']='按该记录绑定目标逻辑控制；符号/索引只作数据语法解码，触发阈值、死区、版本覆盖及实际输入不由文字证明。'
  bd.append(q)
 matches=[w for w in old if w['guid']==p[0]]
 exact=[w for w in matches if w['name']==p[1] and [(a['control'],a['binding']) for a in w['mapping'] if a['control']!='platform']==[(a['target'],a['binding']) for a in bd]]
 relation='exact_excluding_platform' if exact else ('same_guid_different_name_or_bindings' if matches else 'new_guid');cb[relation]+=1
 controllers.append({'id':f'CM{len(controllers)+1:03}','candidate_id':v['id'],'offset':v['offset'],'size':v['size'],'sha256':v['sha256'],'guid':p[0],'name':p[1],'mapping':bd,'inherited_relation':relation,'matching_RES_lines':[w['line'] for w in exact or matches],'review_extent':'full','review_detail':'full_static_data','runtime_selection':'UNVERIFIED'})
assert len(controllers)==256
(O/'additional-controller-data.json').write_text(json.dumps({'schema_version':'gr5.review.v1','count':len(controllers),'comparison':dict(cb),'inherited_scope':{'offset':9774912,'size':442647,'records':1666,'source':'../RES/binary-interface-audit.json#/records/0/embedded_readable/controller_records'},'records':controllers},ensure_ascii=False,indent=2)+'\n')
# Byte-accurate disposition for each original long block; no embedded program text is stored.
long=[]
for b in blocks:
 q=dict(b);bid=b['id'];d=r[b['offset']:b['offset']+b['size']]
 if bid=='B00':q.update(classification='controller_database',review_extent='full_inherited',disposition='复用RES的1678物理行、1666映射记录和完整块哈希；不重复全文；平台/宿主选择仍未知。')
 elif bid in ('B11','B12','B13'):q.update(classification='readable_compatibility_program',review_extent='full',disposition='逐函数、字段、分支及常量见script-behavior.json；音频尾部有准确继承范围。')
 elif bid in [x['id'] for x in shader['records']]:q.update(classification='readable_shader_program',review_extent='full',disposition='逐函数/接口/常量见shader-behavior.json。')
 elif 32<=int(bid[1:])<=55:
  assert base<=b['offset'] and b['offset']+b['size']<=base+offs[25]
  ints=[{'width':g['width'],'overlap_start':max(b['offset'],g['start']),'overlap_end':min(b['offset']+b['size'],g['end'])} for g in dg if max(b['offset'],g['start'])<min(b['offset']+b['size'],g['end'])]
  q.update(classification='size_indexed_dictionary_fragment',review_extent='full_data_disposition',dictionary_intersections=ints,disposition='完整跨度属于同一按字节宽度分组的词条数据；组偏移和2的幂计数由邻接表核对。HTML/脚本字样是有限长度词条片段，不是独立脚本。全部字节已按词条覆盖；无需为每个自然语言词、标签或残缺语法创造游戏功能。B52的uniform命中是初筛误报。库名称和原生解压调用关系不在这里推定。')
 elif bid in ('B56','B57'):
  assert d==b'\t'*256+b'\n'*512
  q.update(classification='whitespace_only_numeric_table',review_extent='full_data_disposition',byte_counts={'9':256,'10':512},disposition='完整768字节仅为两个常值段：256个数值9后接512个数值10；以文本看是TAB/LF，无名称、函数或独立用户行为；不把512个换行当脚本行。原生查表用途未证明。')
 elif bid=='B58':q.update(classification='library_diagnostic_explanation',review_extent='full_text_disposition',disposition='完整说明压缩库内部错误1007的可能硬件/可重复缺陷原因及诊断建议；是诊断文案，不是当前故障、恢复算法或必须执行的测试。没有执行其中建议，也不根据文案新增游戏要求。')
 elif bid=='B59':q.update(classification='manifest',review_extent='full_inherited_and_checked',disposition='应用manifest声明DPI aware为true、dpiAwareness为PerMonitorV2；与RES资源树解码相同，不证明系统采纳或像素缩放结果。')
 else:raise ValueError(bid)
 q['review_detail']=q['review_extent'];q['review_extent']='full'
 long.append(q)
(O/'data-block-disposition.json').write_text(json.dumps({'schema_version':'gr5.review.v1','records':long,'dictionary_layout':{'offsets_table_offset':12051616,'bits_table_offset':12051584,'data_offset':base,'size':offs[25],'sha256':hashlib.sha256(r[base:base+offs[25]]).hexdigest(),'groups':dg,'cell_count':len(dcells),'invalid_utf8_cell_count':sum(not c['valid_utf8'] for c in dcells),'interpretation':'内容由字节片段组成，并非所有词条都是完整UTF-8；对13个不完整UTF-8单元保留事实，不推解码失败。词条文本不复制进报告。'},'dictionary_cells':dcells},ensure_ascii=False,separators=(',',':'))+'\n')
# An additional short, executable-looking Ruby string is explicitly not classed as a diagnostic.
z=byoff[10694728]
short_script={'id':'RB01','offset':z['offset'],'size':z['size'],'sha256':z['sha256'],'review_extent':'full','inputs':['当前常量环境','zlib加载设施'],'behavior':'检查Kernel可见常量中是否已定义Zlib；已定义则不请求加载，未定义才请求加载名称zlib的库。文字自身没有局部异常救援；其外围报错、调用顺序、是否实际求值由原生入口决定，未证明。','branches':['已有常量：无加载请求','无常量：一次加载请求'],'constants':['Zlib','zlib'],'resource_interface':'库加载请求，不是读取SoundFont或音轨。','evidence_level':'supported_static_string_program_only'}
(O/'additional-script-behavior.json').write_text(json.dumps({'schema_version':'gr5.review.v1','records':[short_script]},ensure_ascii=False,indent=2)+'\n')
# Full pool: each original candidate has one disposition and a concrete record/rule.
known=shader['records']+shader['prefix_fragments']+[short_script]
ctrl={v['candidate_id']:v['id'] for v in controllers};lmap={v['id']:v for v in long};selected={(v['offset'],v['encoding']) for v in res['string_scan']['selected']}
counts=collections.Counter();records=[]
for v in source:
 q={k:x for k,x in v.items() if k!='text'};s=v['text'];off=v['offset'];category=None;ref=None
 hit=next((w for w in known if w['offset']<=off<w['offset']+w['size']),None)
 if hit:category='program_or_prefix';ref=hit['id']
 elif v['block']:category=lmap[v['block']]['classification'];ref=v['block']
 elif v['id'] in ctrl:category='additional_controller_mapping';ref=ctrl[v['id']]
 elif 10217888<=off<10568088:category='embedded_font_names_or_binary_fragments';ref='SFNT19'
 elif base<=off<base+offs[25]:category='size_indexed_dictionary_fragment';ref='dictionary_layout'
 elif v['section']=='.text':category='native_text_section_literal_or_incidental_bytes';ref='C_NATIVE'
 elif v['section'] in ('.edata','.idata'):category='PE_linkage_metadata';ref='C_LINK'
 elif v['section'] in ('.rsrc','outside_sections','.CRT','.pdata'):category='PE_resource_header_or_incidental_bytes';ref='C_PE'
 elif re.search(r'copyright|license|CRYPTOGAMS|All rights reserved|\bversion\b',s,re.I):category='attribution_or_version_literal';ref='C_META'
 elif re.match(r'^[_?]Z|^\.?[0-9]+[A-Za-z_]|^N[0-9]|^St[0-9]|^typeinfo |vtable ',s):category='symbol_or_type_label';ref='C_SYMBOL'
 elif re.fullmatch(r'[A-Za-z_][A-Za-z0-9_.:?=/<>+\-!]*',s):category='identifier_path_or_format_atom';ref='C_ATOM'
 elif re.search(r'(?i)error|fail|invalid|unsupported|out of|not supported|warning|assert|too (?:many|few|large|small)|could(?:n.t| not)|cannot|can.t|unable|missing|expected|corrupt|truncat|[Ee][Oo][Ff]|[Bb]ad\b|[Dd]isposed|\[ALSOFT\]|Unknown|not found',s):category='diagnostic_literal';ref='C_DIAG'
 elif re.search(r'%(?:[-+ #0]*\d*(?:\.\d+)?[a-zA-Z]|\*)',s):category='formatted_output_template';ref='C_FORMAT'
 elif re.search(r'^(?:\^|\(\?[:=(]|\\)|https?://|HTTP/|Content-|\b(?:GET|POST|PUT|HEAD)\b|</?|xmlns',s):category='protocol_regex_or_markup_fragment';ref='C_FORMAT'
 elif re.search(r'(?:\w\s*(?:==|!=|<=|>=|->)|sizeof\()',s):category='assertion_or_expression_label';ref='C_DIAG'
 elif len(s)<16 or len(re.findall('[A-Za-z]{3,}',s))<1:category='short_or_numeric_binary_fragment';ref='C_FRAGMENT'
 else:category='nonprogram_literal_or_encoded_data_fragment';ref='C_LITERAL'
 q.update({'classification':category,'disposition_ref':ref,'was_RES_selected':(off,v['encoding']) in selected})
 counts[category]+=1;records.append(q)
assert len(records)==161104 and sum(v['was_RES_selected'] for v in records)==284
rules={
'C_NATIVE':'已枚举.text内全部可打印命中；较长自然语言为汇编库归属信息，其余短指令字节偶合不组成独立明文程序。未解释机器指令，不声称该节行为已审。',
'C_LINK':'PE导入/导出及DLL/符号名字；内容身份按RES接口清单复用，名字不证明实现或ABI。',
'C_PE':'PE头/资源/版本及少量数值偶合。DPI manifest另外有独立记录；不启动图标/程序或宿主。',
'C_META':'版权、版本或许可身份字面量；不自动成为用户能力或法律结论。',
'C_SYMBOL':'链接/异常类型/名称字符串；不从名称推原生函数行为或未来类结构。',
'C_ATOM':'单个接口名、路径、格式代号、选项或标识符；无独立控制流。与消费者有直接关系者在shared-interfaces另列；其余只具存在性证据。',
'C_DIAG':'错误/状态/断言表达式文字；含if/return/比较表达式的文字已在宽词法疑似池复查，不把印刷断言当实际执行分支。',
'C_FORMAT':'输出占位符、协议行、正则或标记片段；本身没有可证明的游戏状态转移。现有文件/网络/宿主合同边界仍成立；不扩审第三方网络/压缩/密码库实现。',
'C_FRAGMENT':'短串或数值编码的可打印投影，全文逐条分类而非按可打印性假定代码；不解释相邻机器码。',
'C_LITERAL':'其它完整可打印候选：自然语言标签/帮助/诊断，或编码查表的字符投影。已经过全池程序词法、所有换行跨度和人工疑似池复核；没有独立可读函数。此处完成的是内容类型处置，不是原生消费者语义认证。'}
(O/'string-inventory.json').write_text(json.dumps({'schema_version':'gr5.review.v1','source':'R/Game.exe','source_sha256':hashlib.sha256(r).hexdigest(),'scan':'与RES完全相同的ASCII可打印≥4及UTF16LE ASCII字符≥4两种字节匹配；允许其在字节层相互重叠。另全文件枚举允许TAB/CR/LF的≥16字节跨度以查短/单行程序。','count':len(records),'review_extent':'full','review_detail':'每条候选的类型处置；程序正文见独立账本，不证明native可达或执行','previously_selected':284,'previously_unselected':len(records)-284,'classification_counts':dict(counts),'rules':rules,'records':records},ensure_ascii=False,separators=(',',':'))+'\n')
# Store the entire additional multiline and code-suspicion inventories by offset/hash and disposition.
queries={}
ascii_records=sorted((q for q in records if q['encoding']=='ascii'),key=lambda q:q['offset'])
ascii_offsets=[q['offset'] for q in ascii_records]
for fname in ('multiline-short','code-suspects','broad-code-suspects'):
 vals=json.load(open('/tmp/gr5-bin-readable/'+fname+'.json'));out=[]
 for i,z in enumerate(vals):
  off=z['offset'];n=z['size'];matches=ascii_records[bisect.bisect_left(ascii_offsets,off):bisect.bisect_left(ascii_offsets,off+n)];cats=sorted(set(q['classification'] for q in matches))
  out.append({'index':i,'offset':off,'size':n,'sha256':hashlib.sha256(r[off:off+n]).hexdigest(),'classification':cats,'candidate_ids':[q['id'] for q in matches],'disposition':'已核可读类型；程序、控制器、词典分别逐项转入具名账本；诊断/名称/数值投影按字符串规则处置。'})
 queries[fname]={'count':len(out),'records':out}
(O/'candidate-search-audit.json').write_text(json.dumps({'schema_version':'gr5.review.v1','queries':queries,'font_container':{'offset':10217888,'size':350200,'table_count':19,'disposition':'可打印名字/字形索引/字节码或轮廓中的偶合串处置。SFNT头和表界限已核；字体执行/渲染/完整表语义不属于明文程序任务。'},'no_unclassified_finite_candidates':True,'finite_scope_not_all_machine_behavior':True},ensure_ascii=False,separators=(',',':'))+'\n')
print('counts',dict(counts));print('additional_controllers',dict(cb));print('long categories',dict(collections.Counter(v['classification'] for v in long)))
