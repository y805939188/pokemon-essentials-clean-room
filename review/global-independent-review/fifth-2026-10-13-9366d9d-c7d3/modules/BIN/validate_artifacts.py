"""Structural evidence validation only. Never executes reference or behavior vectors."""
import ast,collections,hashlib,json,pathlib,re
O=pathlib.Path(__file__).parent;W=O.parents[4];R=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials');checks=[]
def ok(name,condition,detail=''):
 if not condition:raise AssertionError((name,detail))
 checks.append({'check':name,'result':'PASS','scope':detail})
def read(name):return json.loads((O/name).read_text())
r=(R/'Game.exe').read_bytes();base=read('block-inventory.json');scripts=read('script-behavior.json');shader=read('shader-behavior.json');strings=read('string-inventory.json');data=read('data-block-disposition.json');mapping=read('source-to-spec.json');reverse=read('spec-to-source.json');coverage=read('reading-coverage.json');findings=read('findings.json');ctrl=read('additional-controller-data.json')
res=json.loads((O.parent/'RES/binary-interface-audit.json').read_text())['records'][0]
ok('fixed_R_Game_exe_hash',hashlib.sha256(r).hexdigest()==res['sha256']==coverage['game_exe']['sha256'],'数据身份与继承RES对照，不执行程序')
for b,z in zip(base['blocks'],res['embedded_readable']['blocks']):
 ok('block_'+b['id'],all(b[k]==z[k] for k in ('offset','size','sha256','kind','lines')) and hashlib.sha256(r[b['offset']:b['offset']+b['size']]).hexdigest()==b['sha256'],'提取offset/size/hash及初始标签一致；重分类另列')
ok('long_block_inventory_60',len(base['blocks'])==len(data['records'])==60)
expected=[]
for enc,p in [('ascii',rb'[\x20-\x7e]{4,}'),('utf-16-le',rb'(?:[\x20-\x7e]\x00){4,}')]:
 for m in re.finditer(p,r):expected.append((m.start(),len(m.group()),enc,hashlib.sha256(m.group()).hexdigest()))
actual=[(z['offset'],z['size'],z['encoding'],z['sha256']) for z in strings['records']]
ok('every_string_span_matches_independent_regex_rescan',actual==expected and len(actual)==161104,'逐条核范围/编码/哈希；不测试字符串消费者行为')
ok('string_ids_and_classification',all(z['id']==i and z['classification'] and z['disposition_ref'] for i,z in enumerate(strings['records'])) and dict(collections.Counter(z['classification'] for z in strings['records']))==strings['classification_counts'])
ok('inherited_selected_284',sum(z['was_RES_selected'] for z in strings['records'])==284)
# Independently count source declarations, then verify every recorded function location.
bmap={b['id']:b for b in base['blocks']};decls=[];accessors=0
for bid in ['B11','B12','B13']:
 b=bmap[bid];text=r[b['offset']:b['offset']+b['size']].decode();lines=text.splitlines();accessors+=len(re.findall(r'^\s*attr_(?:accessor|reader)\b',text,re.M))
 for i,l in enumerate(lines,1):
  m=re.match(r'\s*def\s+([^\s(]+)',l)
  if m:decls.append((bid,i,m[1]))
actualdecls=[(v['block'],v['lines'][0],v['function']) for v in scripts['records']]
ok('all_225_functions_accounted',actualdecls==decls and len(decls)==225)
ok('all_988_accessor_declarations_accounted',len(scripts['accessors'])==accessors==988)
ok('inherited_audio_31',sum(z.get('review_origin')=='inherited' for z in scripts['records'])==31)
for v in scripts['records']:
 b=bmap[v['block']];a,e=v['byte_range'];ok('function_span_'+v['id'],b['offset']<=a<e<=b['offset']+b['size'] and r[a:e].lstrip().startswith(('def '+v['function']).encode()),'只核定义定位和范围，不执行函数')
ok('shader_program_count',len(shader['records'])==55 and sum(len(z['functions']) for z in shader['records'])==66 and len(shader['prefix_fragments'])==5)
for z in shader['records']+shader['prefix_fragments']:
 d=r[z['offset']:z['offset']+z['size']];ok('shader_bytes_'+z['id'],hashlib.sha256(d).hexdigest()==z['sha256'])
 if 'functions' in z:
  ok('shader_function_ledger_'+z['id'],len(re.findall(rb'\b(?:void|float|vec[234])\s+\w+\s*\([^)]*\)\s*\{',d))==len(z['functions']) and all(v['behavior'] for v in z['functions']),'函数名单/解释非空；不声称GLSL编译成功')
ok('B52_not_shader',next(v for v in data['records'] if v['id']=='B52')['classification']=='size_indexed_dictionary_fragment')
cells=data['dictionary_cells'];ok('dictionary_all_13504_cells_partition',len(cells)==13504 and cells[0]['offset']==12051776 and cells[-1]['offset']+cells[-1]['size']==12174560 and all(a['offset']+a['size']==b['offset'] for a,b in zip(cells,cells[1:])) and all(hashlib.sha256(r[c['offset']:c['offset']+c['size']]).hexdigest()==c['sha256'] for c in cells),'固定数据界限和无缺口分组，不运行解压算法')
ok('dictionary_13_non_utf8_fragments',sum(not z['valid_utf8'] for z in cells)==13)
ok('extra_256_controller_rows',len(ctrl['records'])==256 and sum(ctrl['comparison'].values())==256 and sum(not z['binding'] for v in ctrl['records'] for z in v['mapping'])==4)
for v in ctrl['records']:
 z=strings['records'][v['candidate_id']];ok('controller_identity_'+v['id'],v['offset']==z['offset'] and v['sha256']==z['sha256'] and z['classification']=='additional_controller_mapping')
capids={c['id'] for c in mapping['capabilities']};ok('forward_capability_targets',len(capids)==15 and all(z['capability'] in capids for z in mapping['function_mappings']))
ok('every_program_forward_mapped',{v['source_record'] for v in mapping['function_mappings']}=={z['id'] for z in scripts['records']}|{z['id'] for z in shader['records']}|{z['id'] for z in shader['prefix_fragments']}|{'RB01'})
ok('all_long_blocks_forward_mapped',{v['block'] for v in mapping['long_block_mappings']}==set(bmap) and all(v['capabilities'] for v in mapping['long_block_mappings']))
ok('reverse_capability_targets',len(reverse['records'])==34 and all(z['capability'] in capids and z['source_ids'] for z in reverse['records']))
for v in coverage['external_source_records']+coverage['specification_records']:
 p=(R/v['path']) if v['path'].startswith('Data/') or v['path']=='mkxp.json' else (W/v['path']);d=p.read_bytes();n=len(d.splitlines());ok('coverage_identity_'+v['path'],hashlib.sha256(d).hexdigest()==v['sha256'] and all(1<=a<=b<=n for a,b in v['semantic_ranges']),'只验证报告声明的阅读范围可定位，全文hash不替代语义阅读')
for v in reverse['records']:
 n=len((W/v['path']).read_bytes().splitlines());ok('reverse_range_'+v['capability']+'_'+v['section_or_vector'],1<=v['lines'][0]<=v['lines'][1]<=n)
required='id title module severity disposition status reviewer category source_baseline specification_baseline source_anchors spec_anchors expected_reference_behavior current_spec_behavior gap preconditions minimal_counterexample normal_case failure_or_boundary_case impact_on_independent_implementation negative_evidence_search proposed_spec_change affected_files shared_contracts acceptance_criteria dependencies related_capabilities related_findings root_cause_group priority batch_owner history_links evidence_level execution_status confidence unknowns excluded_claims user_decision_needed review_resolution order_and_mathematics'.split()
ok('full_candidate_schema',len(findings['findings'])==1 and all(set(required)<=set(v) for v in findings['findings']))
ok('no_self_mandatory_signoff',all(v['disposition']=='optional' and v['status']=='candidate_pending_independent_counterevidence' and v['review_resolution']['final_required_signoff'] is False for v in findings['findings']))
for p in O.glob('*.json'):
 if p.name=='artifact-validation.json':continue
 json.loads(p.read_text())
ok('all_json_parse',True)
for p in O.glob('*.py'):ast.parse(p.read_text())
ok('authored_parser_syntax',True,'只解析本目录作者工具的语法，未编译/执行R代码或shader')
for p in list(O.glob('*.json'))+[O/'report.md']:
 if p.name=='artifact-validation.json':continue
 s=p.read_text();ok('sanitized_no_raw_program_block_'+p.name,re.search(r'(?m)^\s*(?:module RPG|class [A-Z]\w*|def self\.|uniform \w+|gl_FragColor\s*=)',s) is None,'结构性排查辅助人工净室复核；不把名称/数值数据当复制源代码')
for target in re.findall(r'\]\(([^)]+)\)',(O/'report.md').read_text()):
 if target=='artifact-validation.json':continue
 ok('report_link_'+target,(O/target).exists())
ok('complete_type_present',isinstance(read('progress.json').get('complete'),bool))
result={'schema_version':'gr5.review.v1','module':'BIN','status':'PASS_TOOL_VALIDATION','check_count':len(checks),'checks':checks,'execution_accounting':{'reference':0,'behavior_model':0,'host_or_demo':0,'shader_compilation':0,'type':'authored_static_parser_and_report_validation_only'},'not_proved':['原生入口/后端选择','GPU或媒体实际输出','所有原生机器码语义','数学例已在引擎运行'],'artifacts':[{ 'path':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(O.iterdir()) if p.is_file() and p.name not in ('artifact-validation.json','progress.json')]}
(O/'artifact-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('PASS_TOOL_VALIDATION',len(checks),'checks; no reference/model/host execution.')
