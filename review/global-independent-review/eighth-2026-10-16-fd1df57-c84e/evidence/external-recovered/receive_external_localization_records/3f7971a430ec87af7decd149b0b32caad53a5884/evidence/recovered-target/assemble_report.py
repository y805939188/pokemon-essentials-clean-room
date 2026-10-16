from pathlib import Path
import datetime, hashlib, json, re, subprocess

ROOT = Path(__file__).resolve().parent
B = Path('/workspace/pokemon-essentials-clean-room')
R = Path('/workspace/pokemon-essentials')
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
RC = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
CC = '30cfed0996003b6ebf4b5c51cc04f31ca9255440'
REPORT = 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/'
REVIEWER = 'Codex /root — external_localization_records; one actual independent delegation context'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
INTL = 'Data/Scripts/001_Technical/003_Intl_Messages.rb'
COMP = 'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb'
SLOT = 'Data/Scripts/017_Minigames/003_Minigame_SlotMachine.rb'
WP08 = 'deliverables/final-specification-set/generic-kernel/wp08-localization.md'
WP15 = 'deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md'
WP69 = 'deliverables/final-specification-set/user-interface/wp69-slot-machine.md'
REELS = 'deliverables/final-specification-set/user-interface/wp69-slot-reels.md'
TEST = 'deliverables/final-specification-set/test-catalog/generic-kernel-wp05-06-07-08-09-10.md'

def dump(path, obj):
    (ROOT / path).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], text=True).strip()

identities = {}
def identity(repo_key, path):
    key = repo_key + ':' + path
    if key not in identities:
        repo, commit = (R, RC) if repo_key == 'R' else (B, B8)
        data = (repo / path).read_bytes()
        tree = git(repo, 'rev-parse', commit + '^{tree}')
        ls = git(repo, 'ls-tree', commit, '--', path).split()
        actual_blob = git(repo, 'hash-object', '--', path)
        identities[key] = {
            'id': key, 'repository': str(repo), 'commit': commit, 'workspace_tree': tree,
            'formal_tree': 'f292698cdd4a8e725525a9be6dc34b75faaf151e' if repo_key == 'B' and path.startswith('deliverables/final-specification-set/') else None,
            'path': path, 'git_mode': ls[0], 'git_blob': ls[2], 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(), 'actual_blob': actual_blob,
            'matches_frozen_blob': actual_blob == ls[2], 'actual_mode': oct((repo/path).stat().st_mode & 0o777),
            'type': 'application/octet-stream' if path.endswith('.dat') else 'text/plain; charset=utf-8',
        }
    return key

def loc(repo, path, start, end):
    return {'identity': identity(repo, path), 'lines': [start, end]}

readset = json.loads((ROOT/'evidence/contracts/localization_records.json').read_text())
mechanical = json.loads((ROOT/'evidence/primary-mechanical-inventory.json').read_text())
inventory = {x['path']: x for x in mechanical['files']}

# The explicit domain arguments and receivers were read, not inferred from filenames.
domains = {
 'ABILITY_NAMES': ('004_Ability.rb', 'name', [31,34], [190,200]),
 'ABILITY_DESCRIPTIONS': ('004_Ability.rb', 'description', [36,39], [190,200]),
 'ITEM_DESCRIPTIONS': ('006_Item.rb', 'description', [162,165], [244,263]),
 'ITEM_NAMES': ('006_Item.rb', 'name', [140,143], [244,263]),
 'ITEM_NAME_PLURALS': ('006_Item.rb', 'name_plural', [145,148], [244,263]),
 'ITEM_PORTION_NAMES': ('006_Item.rb', 'portion_name', [150,154], [244,263]),
 'ITEM_PORTION_NAME_PLURALS': ('006_Item.rb', 'portion_name_plural', [156,160], [244,263]),
 'MOVE_DESCRIPTIONS': ('005_Move.rb', 'description', [70,73], [220,230]),
 'MOVE_NAMES': ('005_Move.rb', 'name', [65,68], [220,230]),
 'POKEDEX_ENTRIES': ('008_Species.rb', 'pokedex_entry', [238,241], [366,380]),
 'RIBBON_DESCRIPTIONS': ('012_Ribbon.rb', 'description', [39,42], [643,653]),
 'RIBBON_NAMES': ('012_Ribbon.rb', 'name', [34,37], [643,653]),
 'SCRIPT_TEXTS': (None, '_INTL/_ISPRINTF', [774,801], [7,212]),
 'SPECIES_CATEGORIES': ('008_Species.rb', 'category', [233,236], [366,380]),
 'SPECIES_FORM_NAMES': ('008_Species.rb', 'form_name', [228,231], [366,380]),
 'SPECIES_NAMES': ('008_Species.rb', 'name', [223,226], [366,380]),
 'TRAINER_TYPE_NAMES': ('014_TrainerType.rb', 'name', [114,117], [779,786]),
 'TYPE_NAMES': ('003_Type.rb', 'name', [49,52], [156,176]),
}
common_assertions = [
 '此记录含一个完整原文键和一个完整译文值；键身份属于本节指定的文本域，不是物种/道具/招式的数值ID。',
 '导入先按分节读取过滤及修剪，再对键和值逆转义，仅键经过规范化；值中的内部空白及换行不套用键规范化。',
 '成功编译的语言载荷经显式语言文件加载才参与game→core运行查找；默认core语料本身不构成运行回退层。',
 '实际同域文本消费者按其原始文本查询；两层缺译返回调用者原输入，空串命中保持；是否到达最终宿主另须对应消费者接收。',
 '此语料描述/名称是可展示数据；其叙述不是战斗、繁殖、图鉴生态或作者工具实际执行的独立证据。',
]
files, units, forwards, facts = [], [], [], []
for row in readset['reference']:
    path = row['path']; domain = Path(path).stem
    meta = inventory[path]; ident = identity('R',path)
    lines = (R/path).read_text(encoding='utf-8-sig').splitlines()
    getter, method, get_range, prod_range = domains[domain]
    fid = 'ELR-F-' + domain
    source = loc('R',INTL,*get_range) if getter is None else loc('R','Data/Scripts/010_Data/002_PBS data/'+getter,*get_range)
    producer = loc('R',INTL,*prod_range) if getter is None else loc('R',COMP,*prod_range)
    fact = {
      'id': fid, 'domain': domain, 'reviewer': REVIEWER,
      'source_identity': ident, 'full_record_range':[1,meta['records']],
      'premises':['固定R的完整现存文本；正常可读UTF-8输入；无插件覆写；运行例另要求有效语言载荷、来源及调用路径。'],
      'assertions':common_assertions, 'producer':producer, 'receiver':source,
      'consumer_entry':method, 'compiler':loc('R',INTL,397,472),
      'loading_and_lookup':loc('R',INTL,478,670),
      'formal_contracts':[loc('B',WP08,27,34),loc('B',WP08,46,78),loc('B',WP08,126,171)],
      'support':'SOURCE_STATIC; all corpus values actually read in lossless full-record views; no runtime equivalence claim',
      'reception':'LOCAL_SOURCE_REVIEW_COMPLETE; ROOT_AND_DOMAIN_RECEPTION_PENDING',
    }
    if domain in ('SPECIES_FORM_NAMES','SPECIES_CATEGORIES','POKEDEX_ENTRIES'):
        fact['alternative_producer']=loc('R',COMP,448,538)
    if domain.startswith('ITEM_PORTION'):
        fact['additional_rule']='原始portion字段不存在时调用名称/复数名称消费者；空译不是字段缺席，不能据空译退到名称域。'
    if domain == 'SCRIPT_TEXTS':
        fact['additional_rule']='普通脚本、插件与事件采集门分列；含占位符、窗口控制码、资源身份和工具诊断，不从语料存在推导所有caller可达。'
    facts.append(fact)
    files.append({'identity':ident,'role':'PRIMARY_REFERENCE','reviewer':REVIEWER,
       'semantic_status':'FULL_READ','read_lines':[[1,meta['lines']]],'unread_lines':[],
       'structures':{'headers':1,'records':meta['records'],'fields':2*meta['records']},
       'record_read_range':[[1,meta['records']]],'fact_group':fid,
       'reading_method':'完整逐记录显示键和值；相等两字段共用完整字面值并显式标等，差异字段分别显示；编号到行号可逆。渲染与哈希本身不授语义信用。',
       'byte_level':'BOM/CRLF/bytes/blob/SHA separately TOOL_VALIDATION; not a semantic substitute'})
    units.append({'id':'ELR-H-'+domain,'identity':ident,'lines':[1,4],
       'status':'FULL_READ','reviewer':REVIEWER,'disposition':'作者翻译说明、BOM/注释及域节头逐项处置；翻译每第二内容行的说明不豁免导入结构门。'})
    for i,(key,value) in enumerate(zip(lines[4::2],lines[5::2]),1):
        uid=f'ELR-{domain}-{i:04d}'
        units.append({'id':uid,'identity':ident,'lines':[2*i+3,2*i+4],
           'record':i,'fields':['source_key','translation_value'],'reviewer':REVIEWER,
           'status':'FULL_READ','fact_group':fid,'key_equals_translation':key==value,
           'key_sha256':hashlib.sha256(key.encode()).hexdigest(),
           'translation_sha256':hashlib.sha256(value.encode()).hexdigest(),
           'premise':'作为本地化数据逐字段阅读；不把名称或描述当作玩法定义。',
           'consumer':fact['consumer_entry'],'disposition':'COVERED_AS_LOCALIZATION_RECORD; downstream reception pending'})
        forwards.append({'unit':uid,'fact':fid,'consumer':fact['receiver'],
           'spec_clauses':['WP08-30','WP08-51','WP08-130','WP08-153','WP08-155'],
           'reception':'WAIT_ROOT','evidence_level':'SOURCE_STATIC'})

invocations=[json.loads(l) for l in (ROOT/'evidence/unit-invocations.jsonl').read_text().splitlines()]
dependency_reads=[]
for x in invocations:
    dependency_reads.append({'identity':identity(x['repo'],x['path']),'lines':x['lines'],
       'total_lines':x['total_lines'],'reviewer':REVIEWER,'reading_status':'ACTUALLY_READ',
       'source_view':x['output'],'observation':'SOURCE_STATIC' if x['repo']=='R' else 'FORMAL_TEXT_READ',
       'claim_scope':'Only named contiguous range. Remaining file text not granted credit.'})
# These complete files were read before the public range renderer existed.
dependency_reads += [
 {'identity':identity('R',INTL),'lines':[1,823],'total_lines':823,'reviewer':REVIEWER,
  'reading_status':'FULL_READ','source_view':'Platform exec chunks ba0625 L1–360; bb565b L350–823 (continuous union). Raw platform transcript export UNVERIFIED.', 'observation':'SOURCE_STATIC'},
 {'identity':identity('B',WP08),'lines':[1,231],'total_lines':231,'reviewer':REVIEWER,
  'reading_status':'FULL_READ','source_view':'Platform exec chunks a9f698 L1–120; f67d85 L121–231. Earlier truncated display not used for credit.', 'observation':'FORMAL_TEXT_READ'},
]

pbs=[]
for p in sorted((R/'PBS').rglob('*.txt')):
    if re.fullmatch(r'(abilities|items|moves|pokemon|pokemon_forms|ribbons|trainer_types|types)(?:_shadow_pkmn)?\.txt',p.name):
        path=str(p.relative_to(R)); pbs.append({'identity':identity('R',path),'semantic_status':'UNREAD','reception':'NOT_RECEIVED','reason':'精确备用/默认数据依赖；由原primary领域审者完整语义审读并向主审接收，本上下文没有借用其结果。'})
dump('evidence/pbs-dependencies.inventory-only.json',pbs)
dump('reading-ledger.json',{'schema':'gr8-external-localization-reading/v1','reviewer':REVIEWER,
   'primary':{'files_denominator':18,'full_read':18,'unread_files':0,'physical_lines':21466,
   'record_denominator':10697,'records_full_read':10697,'records_unread':0,'header_units':18,
   'structure_units':10715,'fields_read':21394,'unread_fields':0,'primary_formal_files':0,
   'outgoing_root_reception_pending_files':18},
   'files':files,'units':units,'dependency_reads':dependency_reads,
   'additional_unread_pbs_files':len(pbs),'unread_pbs_inventory':'evidence/pbs-dependencies.inventory-only.json',
   'qualifications':['三次工具显示截断不是实读；SPECIES_CATEGORIES 150–210、POKEDEX_ENTRIES 30–34及global prompt 125–235均重新完整显示，覆盖缺口。',
      '许可/行政/opaque不替代有效规则阅读：18文件均可读文本，无primary opaque豁免；语料内容不作语言质量或法律审校。',
      '在未接收跨域回执前，不宣称全系统/全部接口闭合；可读未读PBS、UI caller与当前历史资料保持UNREAD/NOT_RECEIVED，不改标宿主limit。']})
dump('forward-mapping.json',{'schema':'gr8-external-localization-forward/v1','fact_groups':facts,
     'records':forwards,'record_denominator':10697,'record_local_mapping_complete':10697,
     'semantic_reception':'WAIT_ROOT; pointers do not establish global acceptance'})

# Clause records carry full original formal text, semantic subassertions, source loci and pending premises.
reverse=[]
for n,line in enumerate((B/WP08).read_text().splitlines(),1):
    if not line.strip() or line.startswith('#') or re.fullmatch(r'[| :\-]+',line):continue
    if n<=25: spans=[(INTL,675,709)];status='SCOPE_OR_DOMAIN_CATALOGUE'
    elif n<=34: spans=[(INTL,481,490),(INTL,600,631)];status='LOCAL_STATIC_SUPPORTED'
    elif n<=42: spans=[('Data/Scripts/003_Game processing/001_StartGame.rb',19,35),('Data/Scripts/016_UI/013_UI_Load.rb',281,355)];status='LOCAL_STATIC_SUPPORTED_SAVE_SERVICE_RECEPTION_PENDING'
    elif n<=55: spans=[(INTL,589,631)];status='LOCAL_STATIC_SUPPORTED'
    elif n<=67: spans=[(INTL,774,801),(SLOT,15,33)];status='PARTIAL_CALLER_RECEPTION_PENDING; ELR_RESOURCE_PROPOSAL'
    elif n<=80: spans=[(INTL,511,545),(INTL,589,631),(INTL,774,823)];status='LOCAL_STATIC_SUPPORTED_MAP_CONSUMER_RECEPTION_PENDING'
    elif n<=96: spans=[(INTL,774,823)];status='SOURCE_STATIC_DERIVATION_ONLY; historical execution not re-certified'
    elif n<=124: spans=[(INTL,7,212),(INTL,553,587),(INTL,644,669),(COMP,220,230),(COMP,487,538)];status='LOCAL_STATIC_SUPPORTED_EVENT_AND_PBS_RECEPTION_PENDING'
    elif n<=148: spans=[(INTL,244,371)];status='LOCAL_STATIC_SUPPORTED_DEFAULT_BINARY_RECEPTION_PENDING'
    elif n<=188: spans=[(INTL,376,472),('Data/Scripts/021_Compiler/001_Compiler.rb',154,182)];status='LOCAL_STATIC_SUPPORTED; derived vectors NOT_EXECUTED'
    elif n<=214: spans=[(INTL,244,472),(INTL,511,631),('Data/Scripts/016_UI/013_UI_Load.rb',334,343)];status='LOCAL_STATIC_SUPPORTED_RECEIVER_RECEPTION_PENDING'
    else: spans=[(INTL,7,823)];status='CROSS_REFERENCE_OR_LIMIT; no runtime/historical acceptance granted'
    parts=[s.strip(' |-*') for s in re.split(r'[；。]|(?<=\|)\s*(?=[^|])',line) if s.strip(' |-*')]
    reverse.append({'id':f'WP08-{n}','identity':identity('B',WP08),'lines':[n,n],
      'text':line,'subassertions':[{'index':i,'assertion':s,'review':'ACTUALLY_READ; disposition and finite premises inherited from this record'} for i,s in enumerate(parts,1)],
      'reviewer':REVIEWER,'reading_status':'FULL_READ','source_facts':[loc('R',*t) for t in spans],
      'premises':'按该条原有有限前提、实际输入与层次核对；未扩大到任意Unicode、完整宿主、任意插件或未接收caller。',
      'status':status})
test_ids=[]
for n,line in enumerate((B/TEST).read_text().splitlines(),1):
    m=re.match(r'\| (LZ\d+) \|',line)
    if m:test_ids.append({'id':m[1],'identity':identity('B',TEST),'lines':[n,n],
        'reading_status':'FULL_ROW_READ','text':line,'evidence_level':'DERIVED_VECTOR','execution':'NOT_EXECUTED',
        'source':loc('R',INTL,7,823),'qualification':'原历史回执未在本上下文重新接受；展示/库存/其它跨域消费者待其primary接收。'})
dump('reverse-mapping.json',{'schema':'gr8-external-localization-reverse/v1',
    'primary_formal_denominator':0,'added_full_formal_files':[identity('B',WP08),identity('B',WP69),identity('B',REELS)],
    'added_partial_formal_files':[identity('B',WP15),identity('B',TEST)],
    'wp08_clause_records':reverse,'wp08_clause_record_count':len(reverse),
    'wp08_subassertion_count':sum(len(x['subassertions']) for x in reverse),'tests':test_ids,
    'test_count':len(test_ids),'qualification':'Clause lexical inventory is mechanical; actual reading and semantic rationale are documented separately. WP69/附表完整读且与Slot完整源对照，财务外部依赖、测试目录SL行及其它WP正文未接收，不认证整WP闭合。'})

interfaces=[
 {'id':'ELR-I01','owner':'kernel_review / 主审','paths':[INTL,WP08],
  'local_evidence':'完整823行服务、完整WP08及LZ01–41已读；默认/语言分层、键/值处理、重复归并、失败前缀已对照。',
  'pending':'全内核任务与本报告的合并接收；一项资源消费者遗漏疑似提案独立反证。'},
 {'id':'ELR-I02','owner':'kernel_review；developer_full及主审协调','paths':['Data/Scripts/021_Compiler/001_Compiler.rb',COMP],
  'local_evidence':'相关完整编译/替换/追加/默认持久化单位已读；PBS获取只匹配顶层数据路径，备用目录不自动参与。',
  'pending':'全PBS生命周期、数据持久化及导出真实主责结论未接收。'},
 {'id':'ELR-I03','owner':'pbs_creature_current / pbs_creature_backups / pbs_battle / pbs_world；主审确认当前路由',
  'paths':[x['identity'] for x in pbs], 'local_evidence':f'{len(pbs)}份默认/备用文件仅核身份及被选择规则，构造器/文本getter已读。',
  'pending':f'{len(pbs)}份PBS全文语义未读、其primary回执未接收；不以18份语料替代全量PBS或完整玩法规则审查。'},
 {'id':'ELR-I04','owner':'resource_media_serialized / binary_remaining_texts；主审',
  'paths':['Data/messages_core.dat','Data/messages_game.dat','Data/Scripts.rxdata'],
  'local_evidence':'语言加载/默认加载完整可读源已读；现存messages_core.dat为963270 bytes，game.dat在此R中不存在。',
  'pending':'messages_core.dat可恢复内容与脚本归档当前独立审读未接收；可读结构缺读不是宿主limit。'},
 {'id':'ELR-I05','owner':'ui_full / combat_presentation / world_activities；主审',
  'paths':['evidence/ui-resource-search.json',WP15,WP69],
  'local_evidence':'63处资源定位命中只是导航；Slot456行及两份WP69完整读，动画包装228行、IconSprite141–207、缓存入口已读。',
  'pending':'其它UI/战斗/图鉴/背包/存储/命名/重学/翻牌的完整caller及正式消费者映射未接收；精确匹配位于locator原始stdout。'},
 {'id':'ELR-I06','owner':'world_full / creature相关主责 / ui_full；主审',
  'paths':['Data/Scripts/016_UI/013_UI_Load.rb','Data/Scripts/003_Game processing/001_StartGame.rb',
           'deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md',
           'deliverables/final-specification-set/generic-kernel/wp09-save-and-startup.md'],
  'local_evidence':'启动语言选择、Load语言直写及默认语言字段相关完整单位已读；地图文本回退已读。',
  'pending':'消息窗口最终控制处理、地图名可变别名、真实保存服务、物品接收后提示及所有下游UI的当前主责接收；未声称运行完成。'},
 {'id':'ELR-I07','owner':'history主责 / 主审',
  'paths':['review/remediation-sixth-20261014-prepare/inputs/limit-records.json',REPORT+'handoff/',
           'review/global-independent-review/seventh-2026-10-14-e646432-7a91/findings.json'],
  'local_evidence':'完整全局合同所列历史资格和L01–L14恢复要求已读，未继承旧PASS。',
  'pending':'原L01–L14全文、R7当前接收、历史canonical/alias/当前有效补充均未在本上下文接收；提案历史去重待核。'},
]
# Do not publish an inferred non-existent filename as a bound formal dependency.
interfaces[5]['paths']=[p for p in interfaces[5]['paths'] if p!='deliverables/final-specification-set/generic-kernel/wp09-save-and-startup.md']
for x in interfaces:
    x.update(status='NOT_RECEIVED',blocking='Blocks global closure/accepted coverage only; does not undo the exact local reading already completed.',receiver='主审独立接收；本任务不改公共队列')
dump('interfaces.json',{'schema':'gr8-external-localization-interfaces/v1','incoming_denominator':len(interfaces),
    'received':0,'not_received':len(interfaces),'interfaces':interfaces,
    'outgoing_primary_files':{'denominator':18,'accepted_by_root':0,'pending':18},
    'independent_counterreview':{'proposal_count':1,'completed':0,'pending':1,'self_counterreview_not_counted':True}})

slot_records=[]
slines=(R/'Text_english_core/SCRIPT_TEXTS.txt').read_text(encoding='utf-8-sig').splitlines()
for i,key in enumerate(slines[4::2],1):
    if key.startswith('Graphics/UI/Slot Machine/'):
        slot_records.append({'record':i,'key':key,'evidence':loc('R','Text_english_core/SCRIPT_TEXTS.txt',2*i+3,2*i+4)})
proposal={
 'id':'GR8-ELR-001','classification':'PROPOSED_GAP','proposed_severity':'P3',
 'severity_reason':'有限非默认语言变体下，指定可见图像身份选择缺失；没有证明默认玩法或实际像素失效。',
 'status':'WAIT_INDEPENDENT_COUNTERREVIEW_AND_ROOT_DECISION','required':False,
 'author':REVIEWER,'actual_independent_counterreviewer':'NOT_RECEIVED',
 'root_cause_key':'localization-resource-receivers-slot-machine-seven-identities',
 'canonical_candidate':True,'aliases':[],'modules':['WP08','WP15','WP69'],
 'title':'老虎机七个图像身份的语言选择接点未列入指定消费者合同',
 'source':{'corpus_records':slot_records,'caller':loc('R',SLOT,1,456),
    'specific_calls':[30,206,209,264,303,327,365,371],
    'translation':loc('R',INTL,600,611),'script_wrapper':loc('R',INTL,774,785),
    'loader':loc('R',INTL,511,529),'image_receiver':loc('R','Data/Scripts/007_Objects and windows/008_AnimatedBitmap.rb',1,207),
    'sprite_receiver':loc('R','Data/Scripts/007_Objects and windows/007_BitmapSprite.rb',141,207)},
 'spec':[loc('B',WP08,56,67),loc('B',WP15,30,34),loc('B',WP69,17,46),loc('B',WP69,94,108),loc('B',TEST,277,288)],
 'finite_premises':['固定B8/R；未覆写实际查找和Slot消费者。',
    '配置并成功加载一个有效当前语言；Data/messages_<片段>_core/game.dat的合法文本哈希，而不是仅把默认文本目录放在工程。',
    '有COINCASE、正且低于上限的余额，正常场景初始化到达目标资源请求；或单独合法调用已读reel初始化。',
    '对照与反例的A/B均为普通非前缀、可加载、布局尺寸合适的位图；不依赖实际仓库缺席的Graphics或完整Demo。'],
 'ordinary_control':{'input':'两语言层均不含老虎机转轮图身份A；其它前提不变。',
    'source_expected':'创建三个转轮时仍交付原身份A。','execution':'NOT_EXECUTED','evidence_level':'DERIVED_VECTOR_FROM_FULL_SOURCE'},
 'minimal_counterexample':{'input':'仅在当前语言game域24把实际转轮图身份A映射为另一个有效非空位图身份B，core缺同键；A仍可用。',
    'steps':['固定正常入口与余额，进入老虎机初始化。','观察第一个转轮图像包装所收到的身份；不把观察点移到最终像素。'],
    'source_expected':'交付B；A是否仍存在不改变选择；三个转轮分别查找。',
    'spec_difference':'WP08§5.1.1表指定控制帮助、图形战斗菜单、训练家卡和翻牌；WP15仅同样列这四组；完整WP69/附表没有老虎机图像语言接点或WP08引用。只遵循当前明确消费者集合的实现可固定A而失去此条件行为。',
    'execution':'NOT_EXECUTED','not_a_claim':'不是宣称参考游戏默认语言已启用、A/B媒体真实存在或官方预期。'},
 'full_observable_rule':'七个角色分别为转轮符号图、中奖、大奖、未中、投入提示、停止提示、按键提示。依状态先查当前语言game再core再原身份，随后交付现有资源入口；背景、遮罩、按钮、线、灯和数字图独立固定。',
 'normal_cancel_failure_partial':{
    'normal':'缺译原A、有译非空B；同键game覆盖core；进入不另行改玩家语言或写存档。',
    'cancel':'没有币盒/零币/已满入口拒绝时不进入这些图像初始化；未下注BACK退出沿原结算合同。',
    'failure':'普通非前缀非空B失败由已读动画包装按其捕获回空白；前缀路径另有异常边界；不重试A。',
    'empty_translation':'空译仍命中；IconSprite清空图像，直接AnimatedBitmap的空输入不能套用IconSprite的清空保证，须按确切入口验收。',
    'partial':'初始化先建场景和若干部件；语言查找/后继失败不保证整体清理。余额/统计提交在正常退出后部，保持WP69已有提交前缀和部分提交规则。'},
 'negative_evidence':{'full_read':[WP08,WP69,REELS],
    'partial_read':[{'path':WP15,'range':[[20,44],[92,127]]}],
    'bounded_search':'WP69两份完整正文对翻译/语言/本地化无命中；全R资源定位63处只是扩展导航；未以检索代替全文。',
    'remaining':'其它正式UI/战斗消费者及原R7根因全文未完整接收；主审应检查是否已有其它主合同覆盖而反证/去重。'},
 'impact':'独立实现可能保持英语/原身份的老虎机图像，即使作者提供有效当前语言位图；不同转轮位图高度还被时间分区消费，但此提案不推定其是否应兼容任意尺寸。',
 'minimal_revision':{
    'rule':'在WP08指定图像消费者合同补齐老虎机七个角色；WP69引用该语言身份选择，并保持图像尺寸、时间分区、转轮顺序、随机输入及支付合同；WP15同步入口导航。',
    'preserve':['现有四组正确指定消费者','game→core→原身份及空译不回退','普通/前缀图像失败分层','原有Slot转轮、滑移、重玩、余额与统计规则','宿主/媒体未知与全部NOT_EXECUTED标记'],
    'read_set':[SLOT,INTL,WP08,WP15,WP69,REELS,TEST,'Data/Scripts/007_Objects and windows/008_AnimatedBitmap.rb','Data/Scripts/007_Objects and windows/007_BitmapSprite.rb'],
    'suggested_write_set':[WP08,WP15,WP69,TEST],
    'actual_write_set':'NONE: 本轮只提出，不整改。附表顺序无此根因必要变化。'},
 'acceptance':[{'id':'ELR-A01','condition':'具名实际非提出者上下文核完整caller、语言层及当前正式覆盖，确认遗漏或具理由撤销/别名。'},
   {'id':'ELR-A02','condition':'静态合同明确七个资源角色，普通缺译A、有译B、game覆盖core及固定背景对照；不扩大到所有图片。'},
   {'id':'ELR-A03','condition':'空译、非空缺资源、初始化/正常退出财务前缀分别验收；不能套通用回滚或重试A。'},
   {'id':'ELR-A04','condition':'回归LZ39–41与WP69时间H/滑移/有效线/重玩/币额/统计；执行与静态分别登记。'}],
 'history':{'C2':'4580645dfbfec4a3c7ccbad56ae293cc619b0d25','related_id':'UNVERIFIED',
    'reason':'本上下文没有接收R7完整canonical/alias；不臆造ID，不修改原27/56/92记录。'},
 'dependencies':{'direct':['ELR-I01','ELR-I05','ELR-I07'],'transitive':['ELR-I04'],
    'blocking_for_required':'实际独立反证、主审分类与去重；运行宿主缺席不阻塞有限静态判定。',
    'primary_batch':'NOT_ASSIGNED_BY_ROOT','shared_receiver':'主审','closure':'独立反证及主审裁决后另行手动整改与非作者验收；此报告不执行。'},
 'excluded_claims':['所有UI资源全部可翻译','任意B尺寸都运行等价','原生加载/像素通过','默认18份文本自动成为当前语言','参考源码缺陷已修复']
}
dump('proposals.json',{'schema':'gr8-external-localization-proposals/v1','proposed':1,'required_decided':0,
   'optional_decided':0,'policy_decided':0,'no_required_decided':0,'withdrawn':0,
   'independent_counterreviews_received':0,'proposals':[proposal],
   'decision_boundary':'只有主审实际独立反证及裁决可改变分类；0 required不是NO_REQUIRED_UPDATE或PASS。'})

identity('R','Data/messages_core.dat')
contracts=[]
for name in ['localization_records.md','localization_records.json','eighth-global-review-prompt.md','review-SKILL.md','AGENTS.md']:
    p=ROOT/'evidence/contracts'/name; data=p.read_bytes()
    contracts.append({'path':str(p.relative_to(ROOT)),'commit':CC,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
        'reading':'FULL_READ','use':'审查授权/语义合同；最新用户明确覆盖原写集与禁止commit/push条款。'})
dump('identities.json',{'schema':'gr8-external-localization-identities/v1','frozen_B8':B8,'frozen_R':RC,
   'contract_commit':CC,'contracts':contracts,'payloads':list(identities.values()),
   'paths':{'current_spec':'/workspace/pokemon-essentials-clean-room','current_reference':'/workspace/pokemon-essentials',
     'historical_mac_spec':'/Users/dingshinn/Desktop/pokemon-framework-reference',
     'historical_mac_reference':'/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials',
     'historical_mac_preparation':'/Users/dingshinn/Documents/pokemon-review-handoffs/2026-10-16-eighth-review-ready',
     'historical_preparation_status':'NOT_PRESENT_IN_THIS_CLOUD; not inferred to be protected or read'},
   'git_identity':{'spec_origin':'https://github.com/y805939188/pokemon-essentials-clean-room.git',
     'reference_observed_origin':'https://github.com/y805939188/pokemon-essentials.git',
     'reference_contract_upstream':'Maruno17/pokemon-essentials','qualification':'固定R commit/tree匹配；观察到的fork origin与历史upstream分列。',
     'local_main':'ABSENT','cached_origin_main':'ABSENT','live_remote_main':B8,'live_delivery_tag':B8},
   'authorization_override':{'source':'本轮用户明确授权','branch':'codex/r8-external-localization-records-20261016',
     'write_set':str(ROOT.relative_to(B))+'/', 'commit_push':'Only own directory; ordinary push; no main merge/tag/formal/reference/public ledger changes','spawn':'PROHIBITED; actual 0'},
   'configuration':{'requested':{'model':'gpt-6.1-sol','effort':'ultra','tier':'default','fast':False},
      'actual':{k:'UNVERIFIED' for k in ['model','effort','tier','fast','platform_agent_id','platform_session_id']},
      'logical_context':'/root external delegation','source_thread_id':'01a13f49-a154-7054-9b04-ce31f924d01c'},
   'startup':'READY_WITH_LIMITS','inventory_qualification':'Payload identities and assignment metadata do not grant reading or semantic reception.'})

dump('evidence/execution-boundaries.json',{'schema':'gr8-localization-execution/v1','utc':NOW,
   'new_reference_behavior_executions':0,'independent_model_executions':0,'host_demo_executions':0,
   'native_media_executions':0,'real_save_replay_executions':0,'derived_vectors':'NOT_EXECUTED',
   'tool_validation':'Python lossless renderers, identity/hash/line inventories, Git transport/status; never promoted to business-test success.',
   'source_static':'Full primary corpus plus exact named dependency units.',
   'original_io':'Public renderer outputs preserved under evidence/reads and evidence/units; metadata-only commands have bounded I/O JSON. Earlier platform exec outputs remain on platform and are not a fully exported private event stream.',
   'historical_io':'NOT_RECEIVED; no historical exit/UTC/configuration filled retroactively.',
   'known_locator_failures':['Initial broad rg included inaccessible /tmp/codex-daemon-1000 (exit2).',
    'Several locator commands used non-existent guessed script paths or ran Data/Scripts rg from B, exit2; followed by exact-path recovery. No negative feature conclusion drawn.',
    'Initial contract git object absent; exact no-tags fetch recovered CC. Cached origin/main absent, exit128 preserved in preflight I/O.'],
   'display_truncations':'Missing visible spans were reread; see reading-ledger qualifications.',
   'not_executed_or_unverified':['No raw Marshal object execution, no install, no production service/game/save interaction.',
     'Native bitmap/pixel/audio output and full Demo NOT_EXECUTED.',
     'Actual model/effort/tier/fast/platform IDs UNVERIFIED.',
     'Historical Mac readiness and other worktrees not available in this isolated cloud; no global stop-the-world claim.']})

progress=json.loads((ROOT/'progress.json').read_text())
progress.update(updated_utc=NOW,ended_utc=NOW,process_status='COMPLETED',
    semantic_status='PRIMARY_READ_COMPLETE; WAIT_ROOT_RECEPTION_AND_INDEPENDENT_COUNTERREVIEW',
    primary_reference_full_read=18,primary_unread=0,primary_records_full_read=10697,
    primary_lines_full_read=21466,primary_structure_units_full_read=10715,
    primary_formal_files=0,additional_formal_full_read=3,additional_formal_partial_read=2,
    additional_unread_pbs_files=len(pbs),incoming_interfaces_not_received=len(interfaces),
    root_acceptance_pending_primary_files=18,proposal_count=1,independent_counterreview_pending=1,
    publication_status='CORE_READY_TO_COMMIT; final transport identity in publication-receipt.json after publication',
    start_time_qualification='started_utc is first persisted task record; earlier context launch UTC was not echoed and is UNVERIFIED',
    blockers=['Global semantic closure: 7 incoming interface groups NOT_RECEIVED; PBS inventory has '+str(len(pbs))+' readable UNREAD files.',
       'Proposal classification: actual independent non-proposer counterreview and root decision NOT_RECEIVED.'],
    update_status='UPDATE_NOT_STARTED')
dump('progress.json',progress)

rows='\n'.join('| '+Path(x['identity'].split(':',1)[1]).name+' | '+str(x['structures']['records'])+' | 1–'+str(inventory[x['identity'].split(':',1)[1]]['lines'])+' | FULL_READ |' for x in files)
report=f'''# 第八轮独立审读：external_localization_records

本上下文已完整审读 primary 的18文件、841,275 bytes、21,466物理行、10,697条键/译文记录及18个文件头结构（合计10,715结构单元、21,394记录字段），primary未读0。primary正式文件分配为0；为双向核验另完整读取WP08、WP69主文和附表，部分读取WP15与共享测试目录。此为有限任务交付，**不构成全系统PASS或接口接收完成**。当前状态为 `WAIT_ROOT_RECEPTION_AND_INDEPENDENT_COUNTERREVIEW`、`UPDATE_NOT_STARTED`。

## 固定输入、授权与路径

- B8 `{B8}`，workspace tree `751dfde81048c81390f89a65ca1d1a565ba8e1ca`，formal tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`。
- R `{RC}`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。实际容器spec为`/workspace/pokemon-essentials-clean-room`，参考为`/workspace/pokemon-essentials`；Mac历史路径单列在identities，不冒称其准备资料或其它worktree已经核验。
- 合同commit `{CC}`；任务prompt、完整全局prompt、指定skill和AGENTS已完整读取。全局prompt36653 bytes/SHA256 `63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b`。指定clean-document-revision全文已读；其最终态正文规则不替代本审计规范，本任务不修正式正文。
- 最新用户授权替代旧任务prompt的写目录及禁止commit/push规则：唯一分支`codex/r8-external-localization-records-20261016`，唯一写集为本目录。未spawn，未整改；不改公共台账、正式规格、main、tag、R或他人目录。
- cloud本地main和origin/main缓存缺席；实时远端main/tag均解析为B8。没有用reset或覆盖其它分支掩盖差异。原参考origin是用户fork，contract upstream Maruno17另列，固定commit/tree一致。

## 完整覆盖与资格

| primary文件 | 完整记录 | 连续物理行 | 资格 |
| --- | ---: | --- | --- |
{rows}

逐记录键和值均实际显示阅读，相等字段以一个完整字面值明确同时代表两字段，差异字段分别显示；记录i精确对应物理行2i+3/2i+4。此是无损全结构视图，不按样本、搜索命中或相同blob授信用。三次显示截断的缺段均单独完整重读；原视图及恢复区间保留。BOM/CRLF、bytes/SHA/blob由机械校验另列，不升级为语义证明。

正向映射逐记录继承具名域事实组：完整原始键/值→过滤/逆转义/规范键→成功编译载荷→显式语言加载→真实文本getter/脚本入口→WP08当前合同。正式正文不复制整套语料；名称、生态叙述和技能描述作为文本数据处置，不冒称其玩法已经接线。WP08完整逐条读取，子断言、源位置、有限前提和待接收条件在reverse-mapping分列。共享测试LZ01–LZ41完整行及限定说明已读，全部新向量NOT_EXECUTED。

已补读：完整823行翻译服务，相关PBS替换/形态追加/默认持久化/顶层路径选择，七类数据构造与getter，调试导出/导入完整菜单单位，启动/载入语言选择直写单位，完整Slot456行、动画包装228行及必要缓存/IconSprite入口。非primary源文件只按reading-ledger记载的真实区间授信用，不把局部单元覆盖扩大为整文件批准。

## 事实与疑似提案

语料18域全部为哈希键/译文材料；domain编号不把物种名、招式名变成数组索引。运行game→core与作者默认core/game分层正确。存在5条键/译文差异：ITEM_DESCRIPTIONS R253；SCRIPT_TEXTS R1991、R2043、R2061、R2202。它们分别保留空格或换行差异；当前WP08键规范化与译文值分离的合同已容纳，不作为新required。普通导入、缺译、空译、作者取消及截断旧产物分别核对，未用理想往返代替源行为。

**GR8-ELR-001（疑似缺项，建议P3，尚未裁决）**：Slot的7个图像身份经语言查找后交动画/精灵入口；完整WP08指定消费者表、WP15对应接点、完整WP69及附表没有给出Slot这一消费者接点。有限反例是在有效当前语言把转轮图A映射为可加载的同尺寸B，A仍存在：实际源请求B；只照当前列举集合固定Slot原身份的实现会请求A。缺译对照请求A。身份角色、源/正文完整载荷身份、前提、普通对照、取消/失败/部分提交、负证据范围、最小建议修订、保留scope、验收与历史待查已写入proposals.json。没有运行宿主或修改正文。

此提案只能由实际不同的非提出者上下文独立反证、检查其它主合同覆盖及历史别名后交主审裁决。required已裁决0、独立反证已接收0，不能把这些0解释成NO_REQUIRED_UPDATE。其它资源匹配63处仅为跨域导航，不据字符串存在增加已确认问题。

## 未读、未接收与执行边界

- primary未读0/18文件、0/10,697记录；主审尚未接收18/18文件的本任务贡献，不能把本地已读冒称全局已接收。
- 新发现默认/备用PBS依赖{len(pbs)}份均可读但本上下文UNREAD、NOT_RECEIVED，精确path/commit/tree/blob/bytes/SHA在库存与identities。其主责分属PBS当前、备用及战斗领域；不以语料替代这些全文或玩法核验。
- incoming接口7组，收到0、未接收7：kernel/WP08；编译生命周期；默认/备用PBS；messages_core及脚本归档；所有UI/战斗图像caller；世界/保存/消息/物品后继消费者；历史资格/原limit/当前有效补充。接口条目给出准确已知路径和现有证据。18文件的局部阅读不因它们未接收而虚改为未读，接口也不因局部映射而关闭。
- `messages_core.dat`存在且963270 bytes，未在本上下文解码或语义阅读；`messages_game.dat`在此固定R中不存在。可恢复资料未读不改标opaque/宿主limit；其它UI资源caller只定位的部分同样保持UNREAD/待主责接收。
- 新参考行为执行0、独立行为模型0、完整宿主/Demo0、原生媒体0、真实存档/重放0。所有反例与回归为SOURCE_STATIC/DERIVED_VECTOR，NOT_EXECUTED。Python/Git只作资料呈现与身份/传输核验。
- 请求gpt-6.1-sol/ultra/default/Fast off；平台未逐项回显model/effort/tier/speed/agent/session，实际均UNVERIFIED。只有当前平台逻辑上下文及source thread引用可见，不虚造服务配置或独立审者。
- evidence保留公开读取视图及受控命令I/O。完整私有平台事件流没有导出，资格UNVERIFIED；早期定位错误、显示截断、缺失缓存及恢复路径具名保留，历史I/O与exit/UTC不倒填。

## 交付与主审入口

progress.json、identities.json、reading-ledger.json、forward-mapping.json、reverse-mapping.json、interfaces.json、proposals.json及本review.md为主交付。evidence内含合同、逐记录完整视图、连续源单位视图、机械库存、原始定位I/O及执行边界。publication-receipt.json在后继发布提交绑定实际core commit/tree、目录tree和逐文件完整远端回读；此正文不写自身未来commit。所有核心文件完整远端回读结果只证明传输身份，不增加语义阅读信用。

主审可按本目录普通Git blob完整读入，先检查未接收队列、实际独立反证与历史去重，决定有限事实接收及GR8-ELR-001分类。后续整改须另行手动委派，本任务没有启动。
'''
(ROOT/'review.md').write_text(report)
print(json.dumps({'primary_files':18,'records':len(forwards),'units':len(units),
 'dependency_range_reads':len(dependency_reads),'identities':len(identities),'pbs_unread':len(pbs),
 'wp08_clause_records':len(reverse),'wp08_subassertions':sum(len(x['subassertions']) for x in reverse),
 'LZ_tests':len(test_ids),'incoming_not_received':len(interfaces),'proposal_count':1},ensure_ascii=False))
