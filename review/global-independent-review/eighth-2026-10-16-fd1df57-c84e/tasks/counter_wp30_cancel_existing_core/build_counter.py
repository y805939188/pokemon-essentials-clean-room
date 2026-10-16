import datetime
import hashlib
import json
import pathlib
import subprocess

Q = pathlib.Path(__file__).resolve().parent
F = pathlib.Path('/workspace/pokemon-essentials-clean-room')
R = pathlib.Path('/workspace/pokemon-essentials')
RC = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
BC = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
READER = '/root/core_atomic_reception'
now = datetime.datetime.now(datetime.timezone.utc).isoformat()

def sha(b):
    return hashlib.sha256(b).hexdigest()

def write(name, data):
    raw = (json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode()
    (Q / name).write_bytes(raw)
    return {'path': name, 'bytes': len(raw), 'sha256': sha(raw)}

def unit(repo, commit, path, lo, hi, label):
    raw = subprocess.check_output(['git', '-C', str(repo), 'show', commit + ':' + path])
    assert (repo / path).read_bytes() == raw
    lines = raw.decode().splitlines(keepends=True)
    assert hi <= len(lines)
    return {'id': label, 'repository': str(repo), 'commit': commit, 'path': path,
            'parent_bytes': len(raw), 'parent_sha256': sha(raw),
            'git_blob': subprocess.check_output(['git', '-C', str(repo), 'rev-parse', commit + ':' + path]).decode().strip(),
            'range': [lo, hi], 'text': ''.join(lines[lo-1:hi]),
            'actual_reader': READER, 'credit': 'Own actual selected complete necessary definition/context; not whole parent unless separately stated.'}

e = json.loads((Q / 'evidence.input.json').read_text())
ident = json.loads((Q / 'input-identities.work.json').read_text())
source_units = []
for x in e['complete_necessary_source_units']:
    p = e['source_identities'][x['source_identity_key']]['path']
    u = unit(R, RC, p, *x['range'], x['id'])
    assert u['text'].rstrip() == x['text'].rstrip()
    u['original_supplier_reader'] = e['actual_reader']
    source_units.append(u)
x = e['complete_FURFROU_handler']
u = unit(R, RC, x['identity']['path'], *x['range'], x['id'])
assert u['text'].rstrip() == x['text'].rstrip()
source_units.append(u)
source_units.extend([
    unit(R, RC, 'Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb', 4, 36, 'MultipleForms-complete-module'),
    unit(R, RC, 'Data/Scripts/003_Game processing/005_Event_Handlers.rb', 148, 197, 'HandlerHashSymbol-complete-class'),
    unit(R, RC, 'Data/Scripts/003_Game processing/005_Event_Handlers.rb', 288, 289, 'SpeciesHandlerHash-complete-class'),
])
formal_units = [
    unit(F, BC, 'deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md', 1, 286, 'WP30-complete-current-contract'),
    unit(F, BC, 'deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md', 1, 327, 'WP21-complete-current-contract'),
    unit(F, BC, 'deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md', 51, 69, 'WP15-complete-section-4.1'),
    unit(F, BC, 'deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md', 1, 13, 'WP66A-scope'),
    unit(F, BC, 'deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md', 192, 229, 'WP66A-complete-forget-learning-and-invariants-context'),
    unit(F, BC, 'deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md', 183, 189, 'GR27-complete-row-and-neighbours'),
]
evidence = {'schema': 'gr8-existing-core-wp30-cancel-source-evidence/v1', 'recorded_utc': now,
            'actual_reader': READER, 'fixed_R': RC, 'fixed_B8': BC,
            'source_units': source_units, 'current_formal_units': formal_units,
            'original_inputs': ident['frozen_inputs'],
            'qualification': 'All listed bodies were actually read, including closure. Original 17+FURFROU provider objects were fully received and independently compared to fixed Git; own whole-source qualifications remain separate. New module/handler bodies were actually read. Whole WP30 286 and WP21 327 were actually read; other formal files only listed necessary contexts. Integrity checks are not target execution.',
            'business': 'NOT_EXECUTED', 'update': 'UPDATE_NOT_STARTED'}
ev_id = write('complete-evidence-units.json', evidence)

facts = [
 {'id': 'CANCEL-F01', 'units': ['items:pbLearnMove', 'pokemon:name', 'pokemon:hasMove?'],
  'meaning': 'Generic learning resolves target ID, rejects nil/egg (unless debug)/Shadow and already-known cases, then adds directly below MAX_MOVES. Full-slot positive first confirmation invokes pbForgetMove on the same Pokemon. Initial negative first confirmation never enters this ForgetScene chain. No default FURFROU natural-learning or demo/API reachability claim is needed or made.'},
 {'id': 'CANCEL-F02', 'units': ['items:pbForgetMove', 'summary:pbStartForgetScreen', 'summary:pbStartForgetScene', 'icon:initialize', 'icon:pokemon=', 'speciesfiles:self.icon_filename_from_pokemon'],
  'meaning': 'The singleton party contains the original Pokemon reference. StartForgetScreen calls StartForgetScene before ChooseMoveToForget; scene constructs PokemonIconSprite for that object; initialize calls its pokemon setter. Evaluating icon_filename_from_pokemon arguments reads pkmn.form before constructing the icon AnimatedBitmap and before any BACK input. Resource/scene success is a premise for later normal cancellation, not a condition for the earlier argument-side commit.'},
 {'id': 'CANCEL-F03', 'units': ['pokemon:form', 'pokemon:form=', 'MultipleForms-complete-module', 'HandlerHashSymbol-complete-class', 'SpeciesHandlerHash-complete-class', 'C21-REG-FURFROU', 'time:pbGetTimeNow', 'pokemon:calc_stats', 'dex:register'],
  'meaning': 'For forced_form=nil and outside battle/storage, form calls registered getForm, and a truthy different result is submitted through form=. FURFROU missing timestamp or current seconds strictly greater than timestamp+432000 yields 0. From stored1 this writes stored0, clears ability cache, calls onSetForm (time_form_set=nil), recalculates stats and conditionally registers player dex. There is no equality short-circuit in explicit form=; dynamic getter itself checks different result. Recalculation and dex lookup can read further derived/cache state. No numeric stat change or final cache-nil guarantee is inferred.'},
 {'id': 'CANCEL-F04', 'units': ['summary:pbChooseMoveToForget', 'summary:pbStartForgetScreen', 'summary:pbEndScene', 'items:pbLearnMove'],
  'meaning': 'With normal four valid old moves/first render and dependencies, BACK returns -1, the forget screen ends, and Give-up=Yes returns false without reaching the slot replacement or machine happiness writer. No captured form snapshot, inverse setter or model rollback appears in this complete chain. Four old move objects/IDs/PP/PP-up values remain unchanged by this FURFROU dynamic form path, while prior stored form/timestamp/cache/recalculation/dex prefixes can persist. Returning false does not undo them.'},
 {'id': 'CANCEL-F05', 'units': ['items:pbLearnMove'],
  'meaning': 'The positive old-slot result path constructs a fresh Pokemon::Move and assigns that single slot before later messages/happiness. by_machine plus keep-old-PP condition optionally clamps new PP. The local replacement atomic step means one fresh move state rather than half-replacing its ID/PP; the complete method contains no global transaction across rendering, messages, form getters or external callbacks. Later failures retain earlier reached writes.'},
 {'id': 'CANCEL-F06', 'formal_units': ['WP30-complete-current-contract', 'WP21-complete-current-contract', 'WP15-complete-section-4.1', 'WP66A-complete-forget-learning-and-invariants-context', 'GR27-complete-row-and-neighbours'],
  'meaning': 'WP30 purpose/scope and section6 define learning/replacement result and explicitly refer to WP21/summary UI; section9 line242 couples unchanged with single-slot+PP replacement. WP21 section3.4 already explicitly describes the exact FURFROU t+432001 individual-icon/summary commit, guards and no resource rollback; section4.2 separately disallows interpreting rejected learning as rolling back prior form changes. WP15 section4.1 applies dynamic form before icon matching. WP66A section6.5/7 defines BACK then give-up and section8 explicitly says selection returns cannot guarantee side-effect-free display. These are positive current-contract qualifications, not an absent-example excuse.'},
]
sections = [
 {'number': 1, 'title': '确切争点与有限范围', 'disposition': 'NO_REQUIRED_BOUNDED_SCOPE',
  'text': '独立反证接受源trace真实：进入遗忘画面后，图标读取过期FURFROU形态可在BACK之前提交；随后确认放弃只保持学习招式结果。争点是当前完整WP30:242是否承诺任意Pokemon字段全局冻结。结合whole WP30、whole WP21及WP15/WP66A明确显示例外，局部学习提交解释成立。本counter不建议新增required或optional，不改正式；root独占最终分类。'},
 {'number': 2, 'title': '完整输入、真实阅读与未接范围',
  'inputs': ident['frozen_inputs'], 'text': '完整8164B观察全部8节、32733B证据全部317行以及1995B强制范围伴件逐字段实际收到。本人不继承proposer的wholeFULL信用；原17完整单位+FURFROU注册全文实际读并逐段核固定Git，另读完整MultipleForms模块/HandlerHashSymbol/Species子类。whole WP30 1–286、whole WP21 1–327实际读；WP21中段外层截断后260–327单独补足。WP15读1–107，采用完整§4.1；WP66A读1–15及155–245，采用完整指定上下文；GR27及相邻行实际读。不声称whole WP15/WP66A、所有绘制/消息/资源/默认数据/外部事件或历史全量阅读。伴件正确保留proposer旧07:26真实FULL，当前1–271另补272–286，不撤旧FULL、不算新行为finding。'},
 {'number': 3, 'title': '独立源到调用者、接收者及当前正式推导', 'complete_facts': facts,
  'trace': ['Full-slot generic learning first confirmation Yes', 'pbForgetMove original Pokemon singleton', 'StartForgetScreen -> StartForgetScene', 'PokemonIconSprite.new -> pokemon=', 'icon_filename_from_pokemon -> original Pokemon.form', 'MultipleForms FURFROU getForm expired -> original Pokemon.form=', 'stored form0/cacheclear/timeclear/recalc/conditional dex', 'first render and input succeed -> BACK -1 -> EndScene', 'Give-up Yes -> false; no slot assignment'],
  'text': '普通完整调用链并未克隆个体。形态提交与学习动作写入是两个领域步骤。当前正式已经给出每个必要跳转的组合规则，不能把WP30边界行从它显式引用的Summary/形态合同中孤立读成全对象事务。'},
 {'number': 4, 'title': '合法正常与失败对照',
  'vectors': [
   {'id': 'V1', 'premise': '合法非蛋非Shadow FURFROU，stored1，forcednil，非战斗/非仓库，time=t整数；4个合法已知招，新招已登记且未知；此前无触发回退的读取；正常字体/数据/资源/回调到输入与收尾。首次有关form读取时now.to_i=t+432001。', 'actions': '首次询问Yes -> ForgetScene BACK -> Give-up Yes', 'static_expected': 'stored0、时间清空及提交prefix；学招false，四旧招/PP不由本路径替换；不保证每个数值必变或图鉴每字段必新增。'},
   {'id': 'V2', 'premise': '同V1但首次询问No', 'static_expected': '不进入这个ForgetScene/icon读取链；学习false且无该链引入的动态形态提交。不能推广为任何消息/插件均纯读。'},
   {'id': 'V3', 'premise': '同V1但形态读取now.to_i恰t+432000', 'static_expected': 'getForm不返回回退值；该读取不提交0。时间可在交互中前进，若后继读取越界须重新按当时值判断，非整场冻结。'},
   {'id': 'V4', 'premise': '同V1且读取时battle/storage guard真，或forced1', 'static_expected': '普通form不执行这次getForm提交；forced0直接读0但保留stored1/t。'},
   {'id': 'V5', 'premise': '正常首绘，选择合法旧槽而非BACK', 'static_expected': '进入单槽fresh Move替换；普通新PP满，by_machine且配置开才旧PP夹限。图标已完成的形态prefix不因后来学招成功而取消。'},
   {'id': 'V6', 'premise': 'V1已完成动态提交后后段资源/首绘/消息依赖失败', 'static_expected': '前缀已留存，可能尚不能处理BACK或返回false；不声称宿主进程崩溃、正常cleanup或最终外观。'},
  ]},
 {'number': 5, 'title': '取消、失败与部分提交',
  'text': '初次No和进入画面后BACK再Give-up是不同路径。后者的-1只是选槽结果，不是回滚令牌。给定FURFROU handler不改招式，因此学习分支不新增/替换且旧招PP保持；它确能改变form/time/cache/recalculated/dex状态。若form=的handler、calc_stats或dex中途失败，已经执行的写入仍是前缀，后继icon/输入/false未必到达。若新Move构造失败，赋槽尚未发生；若赋槽后消息失败，新槽已在。这里均未运行，不把工具exit0当游戏执行。'},
 {'number': 6, 'title': '最强反方与范围建议',
  'strongest_required_argument': '“个体与招式集不变（无部分提交）”字面覆盖form/time，而FURFROU动态提交是同一次正常UI调用内部发生，因此无须缺陷宿主或插件即可反驳全对象冻结；WP30 line242读者可能自然理解更广。',
  'counter': '承认字面风险与真实trace；完整合同的学习标题、前后句单槽/PP原子说明、§6.2对WP21的显式引用、§6.3对Summary的实际交互说明，以及WP21/15/66已明写的同一个体icon/summary先动态提交与不据取消返回推纯读，共同限定该句为学习提交域。尤其WP66A§8直接禁止以选择返回值承诺无副作用，WP21给出的正是FURFROU整数秒普通向量，非泛泛“可能插件有副作用”。全对象冻结解释会同时否定这些当前正条款，局部域解释可以无冲突实现全部合同。新增这一组合向量会有帮助，但完整合同未遗漏必要规则，不能仅因可写更明确就强制改稿。',
  'recommendation': 'NO_REQUIRED_BOUNDED_SCOPE；无强制新fixture/改字，optional也不自动计。仅在root选择编辑澄清时，可将“个体与招式集不变”限为“本次学习不新增/替换招式及PP；显示读取沿WP21”，保持既有规则，不将真实动态提交描述成不存在。'},
 {'number': 7, 'title': '最小人工handoff、正确控制与静态验收',
  'handoff': '保留完整观察与source facts；root可按本counter有限裁定，无自动整改。若采用NO_REQUIRED，正式正文和GR27保持，工作证据明确记录域限定即可。',
  'preserve': ['GR27当前仅招式集不变/false，不扩大到战斗或外层重学；该行并非本YES→BACK→Give-up具体向量。', 'WP21动态getter/forced/battle/storage/秒边界/资源后段不回滚全部正确规则。', 'WP66A四旧招+新招、HM门、BACK→-1、二次Give-up与取消返回首次绘制前提。', '普通单槽fresh Move与机器保留PP差异。'],
  'static_validation': '全部21完整必要R单位及6F上下文按固定Git核identity/range；原输入hash保持。JSON解析与字节核验仅证据I/O，无Ruby/游戏/媒体/宿主执行。无需为本反证新增或运行测试。'},
 {'number': 8, 'title': '历史关系、不同实际作者与执行资格',
  'text': '提出者/root/creature_a_atomic_reception；实际独立counterreader/root/core_atomic_reception，真实不同上下文而非改角色名。此followup新增context/票0。GR27等完整历史全量去重尚未证明，本counter不作全局完成声明。源trace与原观察字节保留，NO_REQUIRED只裁完整当前合同的有限scope。主责CORE仍IN_PROGRESS，完成本反证后恢复CORE-C0642。',
  'requested': {'model': 'gpt-6.1-sol', 'reasoning_effort': 'ultra', 'tier': 'default', 'speed': 'normal', 'Fast': 'off'},
  'actual_authoritative_echo': {k: 'UNVERIFIED' for k in ['model', 'reasoning_effort', 'tier', 'speed', 'Fast', 'opaqueID']},
  'business': 'NOT_EXECUTED', 'update': 'UPDATE_NOT_STARTED', 'new_required': 0, 'new_optional': 0, 'new_contexts': 0, 'new_votes': 0},
]
counter = {'schema': 'gr8-existing-core-wp30-cancel-counterreview/v1', 'recorded_utc': now,
           'actual_reader': READER, 'proposer': '/root/creature_a_atomic_reception',
           'fixed_B8': BC, 'fixed_formal_tree': 'f292698cdd4a8e725525a9be6dc34b75faaf151e',
           'fixed_R': RC, 'fixed_R_tree': '7589c800b61ba13a13040ed0d686979b80a84fd0',
           'bounded_recommendation': 'NO_REQUIRED_BOUNDED_SCOPE', 'root_final_classification': 'PENDING_ROOT',
           'complete_evidence': ev_id, 'sections': sections,
           'business': 'NOT_EXECUTED', 'update': 'UPDATE_NOT_STARTED'}
counter_id = write('counterreview.json', counter)

ios = []
for f in sorted((Q / 'io').glob('*.json')):
    d = json.loads(f.read_text())
    ios.append({'record': 'io/' + f.name, **d})
ledger = {'schema': 'gr8-existing-core-counter-reading-ledger/v1', 'recorded_utc': now, 'actual_reader': READER,
          'entries': ios, 'source_units': [{'id': u['id'], 'path': u['path'], 'range': u['range'], 'parent_sha256': u['parent_sha256']} for u in source_units],
          'formal_units': [{'id': u['id'], 'path': u['path'], 'range': u['range'], 'parent_sha256': u['parent_sha256']} for u in formal_units],
          'outer_output_recovery': 'WP21 141–290 initial combined outer output was truncated near268; later standalone actual260–327 read supplies the entire missing remainder. No complete credit rests on truncated tail.',
          'failed_io_credit': 'FileNotFound/incorrect guessed paths are retained as failed I/O, zero source/formal credit. Direct rg path discovery failures likewise provide no coverage. No target invocation.',
          'actual_utc_qualification': 'Helper UTC and artifact capture UTC are subprocess datetime captures. No model-estimated or retrospective semantic-reading times.',
          'prior_source_FULL': 'Previously own ItemUtilities917, OverworldTime309 and EventHandlers298 exist separately; this counter neither creates new wholeFULL nor lends that status to another reader.',
          'business': 'NOT_EXECUTED', 'update': 'UPDATE_NOT_STARTED'}
ledger_id = write('reading-ledger.json', ledger)
manifest = {'schema': 'gr8-existing-core-counter-manifest/v1', 'recorded_utc': now,
            'deliverables': [counter_id, ev_id, ledger_id], 'immutable_inputs': ident['frozen_inputs'],
            'bounded_recommendation': 'NO_REQUIRED_BOUNDED_SCOPE', 'root_final_classification': 'PENDING_ROOT',
            'write_scope': 'tasks/counter_wp30_cancel_existing_core/', 'main_task': 'IN_PROGRESS; resume CORE-C0642',
            'business': 'NOT_EXECUTED', 'update': 'UPDATE_NOT_STARTED'}
manifest_id = write('manifest.json', manifest)
for x in [counter_id, ev_id, ledger_id, manifest_id]:
    print(json.dumps(x, ensure_ascii=False))
