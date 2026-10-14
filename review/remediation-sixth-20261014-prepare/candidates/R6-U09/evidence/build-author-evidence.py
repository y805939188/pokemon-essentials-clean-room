#!/usr/bin/env python3
"""Assemble the author's scoped seven-group review packet from read fixed inputs."""
import json
from pathlib import Path
import re
from datetime import datetime, timezone

e = Path(__file__).resolve().parent
p = e.parents[2]
repo = e.parents[4]
contract = json.loads((p / 'contracts/R6-U09.json').read_text())
inputs = json.loads((e / 'input-manifest.json').read_text())['inputs']
files = json.loads((e / 'candidate-files.json').read_text())['files']
ledger = [json.loads(line) for line in (e / 'reading-ledger.jsonl').read_text().splitlines()]
by_path = {r['identity']['path']: r for r in inputs}
formal_root = 'deliverables/final-specification-set/'

def anchor(path, first, last, fact):
    path = 'Data/Scripts/' + path
    row = by_path[path]
    return {'identity': row['identity'], 'range': [first, last], 'fact': fact,
            'author_read_ranges': [r['range'] for r in ledger if r['path'] == row['local_path']],
            'evidence_level': 'SOURCE_STATIC', 'execution': 'NOT_EXECUTED'}

def formal(path, clauses, identifiers):
    path = formal_root + path
    row = next(r for r in files if r['formal_path'] == path)
    return {'formal_path': path, 'candidate_path': row['candidate_path'],
            'baseline': row['baseline'], 'candidate': row['candidate'],
            'candidate_clauses': clauses, 'new_vectors': identifiers,
            'reverse_join': 'Source anchors in this record and fully read frozen formal input; hashes bind payloads, not semantic PASS.'}

chains = {
 'R6-DX-COMP-001': [
  anchor('020_Debug/003_Debug menus/001_Debug_Menus.rb',69,146,'默认调试入口/菜单分派门与处理器调用；不在分派处增加编译异常清理或缓存刷新。'),
  anchor('020_Debug/003_Debug menus/002_Debug_MenuCommands.rb',1335,1344,'菜单创建消息窗，直接强制内容阶段；完成提示与窗口释放在正常返回之后，无局部确保释放。'),
  anchor('021_Compiler/001_Compiler.rb',993,1037,'PBS发现/兼容改写、内容编译顺序；内容阶段自身无调试判断、启动新地图导入、清单预删除及局部异常转换。'),
  anchor('021_Compiler/001_Compiler.rb',1039,1115,'启动检查的缺目录前缀、导入、整数mtime、强制键、清单删除与异常分类；诊断须正常返回才能到异常后删除。'),
  anchor('021_Compiler/002_Compiler_CompilePBS.rb',4,68,'当前表清空，逐节校验后登记；整表终检与保存在全部节完成之后。'),
  anchor('021_Compiler/002_Compiler_CompilePBS.rb',206,231,'词法合法Status/Power40在条目校验拒绝，先于该条目登记及整表保存。'),
  anchor('021_Compiler/004_Compiler_MapsAndEvents.rb',45,83,'启动导入扫描未登记地图、排除999；有导入才写地图信息并清地图信息缓存。'),
  anchor('021_Compiler/004_Compiler_MapsAndEvents.rb',1683,1751,'事件驱动取得地图信息后只遍历已登记编号；后续公共事件与保存有各自变化门。'),
  anchor('003_Game processing/001_StartGame.rb',1,17,'初始化载入完整宿主数据的必要门与新临时会话数据；不把缺宿主Demo当合法正常对照。')],
 'R6-DX-COMP-002': [
  anchor('010_Data/002_PBS data/001_MiscPBSData.rb',1,64,'区域/动画集合/关联/地图信息惰性读取，存在缓存优先返回；全局具名清理定义包括独立连接清理，未接入编译菜单。'),
  anchor('021_Compiler/001_Compiler.rb',993,1115,'直接内容阶段与启动前缀均没有统一对象缓存失效操作。'),
  anchor('021_Compiler/002_Compiler_CompilePBS.rb',593,629,'区域编译从合法PBS建立新列表并写regional_dexes.dat；不替换已发出的区域缓存。'),
  anchor('021_Compiler/003_Compiler_WritePBS.rb',364,391,'区域反写先取得区域读取对象，随后覆盖目标文本；单项和全量共用该写出入口。'),
  anchor('021_Compiler/003_Compiler_WritePBS.rb',794,819,'全量反写包含区域单项写出，不能通过“全量”绕过区域读取缓存。'),
  anchor('019_Utilities/001_Utilities.rb',389,418,'编号、成员、长度接口都消费区域表读取入口；A缓存的BULBASAUR编号1、IVYSAUR编号0。'),
  anchor('020_Debug/001_Editor screens/001_EditorScreens.rb',1099,1202,'地区图鉴总保存Yes：保存工作表档案、清区域缓存、反写、正常完成；No不执行该保存链，子页编辑副作用分别观察。'),
  anchor('003_Game processing/001_StartGame.rb',1,17,'初始化重建临时会话数据，动画集合在其载入门读取；并无独立连接缓存清空。'),
  anchor('004_Game classes/005_Game_MapFactory.rb',350,506,'独立连接/尺寸缓存及地图消费者；清理与临时会话数据替换不同。'),
  anchor('021_Compiler/002_Compiler_CompilePBS.rb',1274,1321,'动画编译从磁盘读取，空映射重建；存在有效条目即写映射/集合，零有效不写；不清预载两缓存。'),
  anchor('011_Battle/004_Scene/004_Scene_PlayAnimations.rb',412,506,'播放查找消费关联缓存并从动画集合读取编号，成功写磁盘不保证本次可见播放已变。'),
  anchor('020_Debug/003_Debug menus/002_Debug_MenuCommands.rb',1335,1408,'直接编译/区域导出及宿主Reload请求是不同入口，正常完成消息不证明对象广播刷新。'),
  anchor('021_Compiler/004_Compiler_MapsAndEvents.rb',45,83,'新地图导入只显式清地图信息缓存；不扩大为连接/区域/动画全部清空。')],
 'R6-DX-COMP-003': [
  anchor('021_Compiler/001_Compiler.rb',72,77,'行内井号后缀先删除再修剪，不识别引号保护。'),
  anchor('021_Compiler/001_Compiler.rb',95,135,'普通分节先按物理首列井号/纯空白跳过；缩进独立井号预处理为空后没有再次跳过。B节头已交付A，B内容中失败尚未交付B。'),
  anchor('021_Compiler/001_Compiler.rb',232,249,'专用预处理逐行入口先预处理再跳过空结果，同一缩进注释可略过。'),
  anchor('021_Compiler/002_Compiler_CompilePBS.rb',4,68,'普通条目校验、内存登记、终检及整表保存顺序；错误不回滚A。'),
  anchor('021_Compiler/002_Compiler_CompilePBS.rb',791,862,'合法训练家材料的专用入口实际消费预处理逐行读取；需要有效已定义类型/物种等字段。')]
}
changes = {
 'R6-DX-COMP-001': [
  formal('generic-kernel/wp04-pbs-lifecycle.md',['§2','§3.2','新§3.3','§5.1','§5.3','§6','§9'],['KL37','KL38','KL39']),
  formal('demo-dx/wp75-project-conversion-and-authoring-tools.md',['§3.1','§4','§16.1'],['DXCOMP-C01','DXCOMP-C02','DXCOMP-C03']),
  formal('demo-dx/wp72-debug-contexts-and-controls.md',['§8.3 Compile data行'],[]),
  formal('test-catalog/generic-kernel-wp02-03-04.md',['KL02/KL03限定启动','KL37–KL39'],['KL37','KL38','KL39']),
  formal('test-catalog/demo-dx-wp72-73-74-75-76-77.md',['新增编译/缓存对照'],['DXCOMP-C01','DXCOMP-C02','DXCOMP-C03'])],
 'R6-DX-COMP-002': [
  formal('generic-kernel/wp04-pbs-lifecycle.md',['§5.1/§5.4动画写入门与WP74一致','§5.5区域三观察点','新§5.6','§9'],[f'KL{i}' for i in range(40,46)]),
  formal('demo-dx/wp75-project-conversion-and-authoring-tools.md',['§3.1缓存引用'],['DXCOMP-C04','DXCOMP-C05','DXCOMP-C06','DXCOMP-C07','DXCOMP-C08']),
  formal('demo-dx/wp74-battle-animation-authoring-and-exchange.md',['§15编辑/保存/编译到磁盘','§16编译缓存行及读取路径'],['DXCOMP-C06','DXCOMP-C08']),
  formal('demo-dx/wp72-debug-contexts-and-controls.md',['§8.3 Compile data/Create PBS/Reload行'],[]),
  formal('pokemon-rules/wp62-pokedex-records-regions-and-content.md',['§5.1区域查询/反写与记录刷新区分'],['KL40','KL41','KL42']),
  formal('test-catalog/generic-kernel-wp02-03-04.md',['KL40–KL45'],[f'KL{i}' for i in range(40,46)]),
  formal('test-catalog/demo-dx-wp72-73-74-75-76-77.md',['新增编译/缓存对照'],[f'DXCOMP-C{i:02}' for i in range(4,9)])],
 'R6-DX-COMP-003': [
  formal('generic-kernel/wp04-pbs-lifecycle.md',['§4.2物理/预处理空行家族及A/B前缀','§9'],[f'KL{i}' for i in range(46,51)]),
  formal('test-catalog/generic-kernel-wp02-03-04.md',['KL46–KL50'],[f'KL{i}' for i in range(46,51)])]
}
generic = (e.parent/'mirror'/formal_root/'test-catalog/generic-kernel-wp02-03-04.md').read_text()
demo = (e.parent/'mirror'/formal_root/'test-catalog/demo-dx-wp72-73-74-75-76-77.md').read_text()
vector_rows = {}
for text in (generic, demo):
    for line in text.splitlines():
        if re.match(r'^\| (KL\d+|DXCOMP-C\d+) \|',line):
            identifier, premise, expected = [part.strip() for part in line.split('|')[1:4]]
            vector_rows[identifier] = {'id': identifier, 'input_and_premises': premise, 'expected_prefix': expected,
                'author_result': 'SOURCE_STATIC_SUPPORTED_WITH_STATED_PREMISES', 'execution': 'NOT_EXECUTED',
                'independent_candidate_verdict': 'PENDING_NON_AUTHOR_REVIEW'}
partners = {
 'demo-dx/wp72-debug-contexts-and-controls.md': ['R6-U08'],
 'demo-dx/wp74-battle-animation-authoring-and-exchange.md': ['R6-U07'],
 'demo-dx/wp75-project-conversion-and-authoring-tools.md': ['R6-U06'],
 'generic-kernel/wp04-pbs-lifecycle.md': ['R6-U14'],
 'pokemon-rules/wp62-pokedex-records-regions-and-content.md': ['R6-U01','R6-U11'],
 'test-catalog/demo-dx-wp72-73-74-75-76-77.md': ['R6-U06','R6-U07','R6-U08'],
 'test-catalog/generic-kernel-wp02-03-04.md': ['R6-U14']}
history = {
 'R6-DX-COMP-001': ['WP04 §3.1及§3.2原异常表逐字保留；新限定诊断正常返回、不误用于直接入口。KL01–36原结果保留，仅KL02/03前提缩至启动。',
   'WP75 §3.2/§3.3及§5–15逐字保留：B20-C024、事件页转换、门/出口、自开关、数量守卫和脚本往返；运行中直接不导入与Map999排除分别观察。',
   'WP72原调试门、受限菜单及完整效果表保持；原demo目录327行全文保留。'],
 'R6-DX-COMP-002': ['WP74 §1–14、§15命名/写入门/播放回退、§17后全文保留；AN-M29/AN-M30零有效旧磁盘规则另列KL45/C08。WP04旧“有变化才保存”摘要在必要接合处精确改成既有WP74有效条目门。',
   'WP04遭遇输入、快照相关引用、概率21/0/70、指标布局/输出路径、进化反写、电话身份/默认与井号反写段保持；不推广统一刷新。',
   'WP62记录写入/身份及§5.2后解锁、展示/刷新参数保留；WP73-A §5.3保存Yes与CE-M14/CE-M20对子页No副作用独立，不编辑WP73-A。',
   'GR5-M12-001–004原限定（loader、六家族LF/外层空白、门条件、布尔）以及SC-U07-001纠正不变；001–004准则135–360与纠正全文已读，101–103元数据和原表保留，不冒称新增独立回归PASS。'],
 'R6-DX-COMP-003': ['KL07–10分词/模式及KL33–36井号、普通/q文本、反写再读/默认重复原行逐字保留；WP04旧行内井号规则只限定物理过滤前缀，后续语义不变。',
   '本次普通类型A/B与专用训练家注释对照来自新完整Compiler读取；不把局部失败推广到全部解析家族/随附PBS数量或全局dat未变。',
   'history-hash-input-contract.json名字沿用初提取，但其内容实为GR5-M01-002本地化消息默认合同；不是PBS井号旧验收，不用它证明本项。']}
records = []
for original in contract['scope_contracts']:
    identifier = original['id']
    vec = sorted({v for row in changes[identifier] for v in row['new_vectors']}, key=lambda x: (not x.startswith('KL'), int(re.search(r'\d+$',x)[0])))
    record = {
      'identity_and_verdict': {**original['identity_and_verdict'], 'canonical_id': identifier,
          'aggregation_aliases': [], 'author_logical_id': 'R6-U09-A',
          'state': 'REVISED_CANDIDATE_PENDING_NON_AUTHOR_REVIEW',
          'author_state': 'REVISION_COMPLETE_READY_FOR_NON_AUTHOR_REVIEW',
          'formal_acceptance': False, 'CLOSED': False, 'input_state_retained_in_original': original['identity_and_verdict']['state']},
      'bidirectional_evidence': {'source_fact_to_consumer_to_formal': chains[identifier],
          'formal_to_source': changes[identifier], 'formal_inputs_read': 'All seven frozen formal files were read in full; ledger ranges and input-manifest bind them.',
          'readonly_control': 'WP73-A 140–153 explicit Yes invalidation control; not in write set.',
          'negative_evidence': {'new': 'Full four Compiler files and bounded dispatcher/cache/editor/consumer contexts freshly read; current fixed-R literal searches in source-current-call-search.json.',
             'historical': 'counter-B-compiler.json full 1–1075 and counter-call-search.txt read; original call inventory retained separately.',
             'limit': 'Literal inventory is not reflective/dynamic/native absence or all-source semantic read; no shipped-PBS corpus assertion.'}},
      'premises_and_counterexample': {**original['premises_and_counterexample'],
          'author_counterexample_precision': {'R6-DX-COMP-001':'Status/Power40 is lexically legal; prior producers and old dat valid. New unregistered Map007 is independent adjacent case; map999 exclusion unchanged.',
            'R6-DX-COMP-002':'A=[BULBASAUR], B=[IVYSAUR], both registered; all stages succeed. Explicitly separate cache absent, editor Yes/No, fresh Game_Temp, independent connection clear/new process, and zero-effective animation mapping.',
            'R6-DX-COMP-003':'A/B are valid unique ordinary type sections; one ASCII space then standalone # note within B; compare column0, blank, inline Name, before first section and valid Trainer specialized path.'}[identifier],
          'cancellation': 'Direct compile has no added confirmation/cancel branch. Editor Yes/No controls apply only to COMP002; No is not promoted to globally no side effects.',
          'execution_current_author': 'NOT_EXECUTED; new static derivation only; no isolated reference execution.'},
      'minimum_revision_contract': {'original_required_minimum': original['minimum_revision_contract'],
          'actual_changes': changes[identifier], 'clean_room': 'Behavioral prose/tables only, no reference fragments, engine or framework implementation.',
          'preserved_correct_content': history[identifier],
          'future_compatibility_policy': 'Accurate fixed-source behavior does not decide permanent defect compatibility; no optional/policy changes.'},
      'acceptance_and_regression': {'vectors': [vector_rows[v] for v in vec],
          'current_author_static_result': 'SUPPORTED_FOR_SCOPED_FACTS_AND_DERIVED_VECTORS; NOT_AN_INDEPENDENT_PASS',
          'tool_validation': {'record':'static-validation.json', 'checks':198, 'failed':0, 'scope':'identities/allowlist/preserved spans and vectors/33 local link targets, not behavior execution'},
          'precise_history_controls': history[identifier],
          'history_qualification': 'R1 original WP only; R2 229/21/341; R3 23/76 with optional/NO_REQUIRED/historical not-started kept; R4 17/76 distinct from B5 16/75; R5 unique activation 92 CLOSED precise selected scopes only, not whole files or host.',
          'history_current_author_limit': 'Bounded retained clauses and rejoined source controls only; unchanged history input identities and selected qualification records do not count as fresh whole-R1–R5 or independent integrated PASS.',
          'execution_counts': {'reference':0,'independent_complete_behavior_model':0,'host':0,'Demo':0,'real_save':0,'production_services':0},
          'unverified': ['native/host error UI','actual filesystem failure results','visible animation or media playback','hidden System.reload_cache side effects','complete compatible-host execution']},
      'independent_adjudication': {'original_non_proposer_record': original['independent_adjudication'],
          'new_candidate_reviewer': 'R6-U09-R, to be assigned separately by parent',
          'new_candidate_review_state':'PENDING_NON_AUTHOR_ULTRA_REVIEW',
          'actual_reviewer_identity':'UNVERIFIED/NOT_ASSIGNED_BY_AUTHOR',
          'requested_model':'gpt-6.1-sol','requested_effort':'ultra','tier':'default','speed':'default',
          'author_is_not_independent_reviewer':True,'CANDIDATE_PASS':False,'INTEGRATED_PASS':False},
      'dependencies_and_receivers': {'primary_batch':'R6-U09','blocking_author_dependencies':[],
          'nonblocking_domain_dependencies':contract['nonblocking_domain_dependencies'][identifier],
          'sole_formal_writer':'R6-I', 'actual_integrator_thread_from_latest_user':'01a13a93-d1da-71e4-a488-63b8524f503d',
          'parent_source_thread':'01a10d94-84b9-759e-aa1d-edb0d9b6d0e2',
          'shared_paths':[{'path':r['formal_path'],'other_batches':partners[r['formal_path'].removeprefix(formal_root)],'receive_required':True} for r in changes[identifier]],
          'integration_rule':'Receive every relevant batch delta; compare shared full file and joins after integration. Do not replace shared formal with U09 whole-file mirror.',
          'closure_blockers':['new candidate non-author review','unique writer actual integration','shared full-file non-author review','direct/transitive interfaces and precise integrated history regression','formal acceptance','CLOSED registration']}
    }
    records.append({'id':identifier, **record})
metadata = {'logical_id':'R6-U09-A','actual_cwd':str(repo),'branch':'codex/remediation-sixth-r6-u09-author-20261014',
    'fixed_prepare':'469a268b92daed7b4d28d7fd0da75520cbb7228f','fixed_main':contract['frozen_main'],'fixed_reference':contract['frozen_reference'],
    'requested':{'model':'gpt-6.1-sol','effort':'xhigh','tier':'default','speed':'default','Fast':False},
    'effective':{'model':'UNVERIFIED','effort':'UNVERIFIED','tier':'UNVERIFIED','speed':'UNVERIFIED','platform_uuid':'UNVERIFIED'},
    'metadata_limit':'Platform effective configuration/thread UUID not echoed; latest user explicitly says direct author work, no CLI or extra-agent proof. No configuration/credentials probe performed.',
    'initial_start_utc':'UNVERIFIED: initial tool calls did not independently capture UTC locally; not backfilled',
    'first_locally_recorded_activity_utc':'2026-10-14T13:59:30.362520+00:00',
    'snapshot_utc':datetime.now(timezone.utc).isoformat(),
    'source_root_mapping':{'legacy':'/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials',
         'prepared_root_missing_here':'/workspace/pokemon-essentials-reference-r6',
         'raw_payload_cache':'/workspace/r6-input-cache/frozen-payloads/Maruno17/pokemon-essentials/'+contract['frozen_reference'],
         'fresh_readonly_object_cache':'/tmp/r6-u09-reference-objects.git'},
    'formal_root_mapping':{'legacy':'/Users/dingshinn/Desktop/pokemon-framework-reference','actual':str(repo)},
    'original_integration_thread_superseded':'Prep header names old parent /root; latest user assigns actual sole integrator 01a13a93-d1da-71e4-a488-63b8524f503d.'}
(e/'finding-responses.json').write_text(json.dumps({'metadata':metadata,'records':records},ensure_ascii=False,indent=2)+'\n')
readsets = []
for path, row in by_path.items():
    events = [r for r in ledger if r['path']==row['local_path']]
    if not events: continue
    total = events[0]['total_lines']
    covered = set()
    for event in events: covered.update(range(event['range'][0], event['range'][1]+1))
    readsets.append({'path':path,'identity':row['identity'],'total_lines':total,
        'emitted_ranges':[r['range'] for r in events], 'full_range_emitted':len(covered)==total,
        'author_semantic_read':'FULL' if len(covered)==total else 'COMPLETE_NAMED_CONTEXT_ONLY',
        'receipt_is_not_semantic_pass':True})
(e/'author-reading.json').write_text(json.dumps({'prompt':{'path':'prompts/R6-U09-A.md','bytes':227242,
    'sha256':'b21be4d214a9d157f0526122981669ea72fe0c39e534aff8376a00f7538b5c0b',
    'git_blob':'500382c78bf7d13b1383f8ba3b7fe8f1997a9abf','full_author_read_ranges':[[1,155],[156,300],[301,600],[601,900],[901,1200],[1201,1500],[1501,1800],[1801,2100],[2101,2335],[2336,2550],[2551,2950],[2951,3552]],
    'semantic_read':'FULL','standalone_contract':'Fully read embedded JSON parsed equal to standalone contracts/R6-U09.json; no substitute summary.'},
    'readsets':readsets,'counterevidence_full_read':{'path':'inputs/evidence/tasks/R6-DX/debug/counter-B-compiler.json','ranges':[[1,450],[451,800],[801,1075]]},
    'other_reads':'Root AGENTS full; prep README/historical qualification/aliases full; relevant policy/limit records and dependency/conflict entries; counter-call-search full; selected R5 qualification records full, criteria135–360 and SC-U07-001 erratum full.',
    'local_capture_limit':'Early prompt/admin/history tool outputs reside platform transcript, not independently saved raw stdout/UTC. Ledger supports later file/range emissions; truncation in combined output was repaired by smaller reads. No fabricated backfilled metadata.',
    'semantic_pass':False,'execution':False},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'records':len(records),'groups_per_record':7,'new_generic_vectors':14,'new_demo_vectors':8,'state':'READY_FOR_NON_AUTHOR_REVIEW'},ensure_ascii=False))
