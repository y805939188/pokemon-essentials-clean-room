"""Historical v1 writer. Do not rerun over the completed v2 purpose judgments.

Use complete-purpose-v2.py for v2 evidence; this original method is preserved as
process evidence. No script execution grants semantic review credit.

Only files adjacent to this script are written. No reference program is executed.
The reader's recorded judgments below are intentionally incomplete, not defaults
that turn historical paragraphs into accepted current contracts.
"""
import collections
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess

OUT = Path(__file__).resolve().parent
REPO = Path('/workspace/r8-external-legacy')
REF = Path('/workspace/pokemon-essentials')
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
CARRIER = '30cfed0996003b6ebf4b5c51cc04f31ca9255440'
ROOT = 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
MANIFEST = 'planning/review-manifest-2026-09-19.md'
FORMAL = 'deliverables/final-specification-set/'
WP23 = FORMAL + 'pokemon-rules/wp23-shadow-hyper-and-purification.md'
UI66 = FORMAL + 'user-interface/wp66-b-storage-and-pokedex-ui.md'
CAT = FORMAL + 'test-catalog/pokemon-rules-wp19-21-22-23-34.md'
STORAGE = 'Data/Scripts/016_UI/017_UI_PokemonStorage.rb'
CHAMBER = 'Data/Scripts/016_UI/023_UI_PurifyChamber.rb'
CONTAINER = 'Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb'
SAVE = 'Data/Scripts/002_Save data/004_Game_SaveValues.rb'
SETTINGS = 'Data/Scripts/001_Settings.rb'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args])

def dump(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

catalog = []
def evidence(eid, path, ranges=None, scope=None, reference=False, commit=None):
    repo = REF if reference else REPO
    revision = commit or (R if reference else B8)
    payload = git(repo, 'show', f'{revision}:{path}')
    assert (repo / path).read_bytes() == payload
    lines = payload.splitlines(keepends=True)
    obj = {
        'id': eid, 'repository': 'Maruno17/pokemon-essentials' if reference else 'y805939188/pokemon-essentials-clean-room',
        'commit': revision, 'tree': git(repo, 'rev-parse', f'{revision}^{{tree}}').decode().strip(),
        'path': path, 'mode': git(repo, 'ls-tree', revision, '--', path).decode().split()[0],
        'blob': git(repo, 'rev-parse', f'{revision}:{path}').decode().strip(),
        'bytes': len(payload), 'sha256': hashlib.sha256(payload).hexdigest(), 'physical_lines': len(lines),
        'read_scope': scope or ('FULL_READ' if ranges is None else 'FULL_READ_RANGES_ONLY'),
        'ranges': ranges if ranges is not None else [[1, len(lines)]],
        'whole_file_read': ranges is None and scope is None,
        'reader': 'actual /root external delegated context', 'root_reception': 'UNRECEIVED',
    }
    if ranges:
        obj['range_identities'] = [
            {'lines': [a,b], 'byte_start': sum(map(len, lines[:a-1])), 'byte_end': sum(map(len, lines[:b])),
             'bytes': len(b''.join(lines[a-1:b])), 'sha256': hashlib.sha256(b''.join(lines[a-1:b])).hexdigest()}
            for a,b in ranges]
    catalog.append(obj)
    return eid

evidence('E-MANIFEST', MANIFEST, [[1,65],[1835,2079],[2795,4127]])
evidence('E-AGENTS', 'AGENTS.md')
for eid, path in [('E-TASK',ROOT+'/delegation/prompts/legacy_manifest_currentness.md'),
                  ('E-READSET',ROOT+'/delegation/readsets/legacy_manifest_currentness.json'),
                  ('E-GLOBAL',ROOT+'/inputs/eighth-global-review-prompt.md'),
                  ('E-SKILL',ROOT+'/inputs/review-SKILL.md')]:
    evidence(eid,path,commit=CARRIER)
for eid,path in [('E-ROOT','README.md'),('E-CURRENT','CURRENT-DELIVERY.md'),
                 ('E-R7','delivery/2026-10-16-seventh/README.md'),
                 ('E-CLEANUP','delivery/2026-10-16-seventh/cleanup-report.md'),
                 ('E-EXTRACTION','planning/extraction-plan.md'),
                 ('E-FORMAL-README',FORMAL+'README.md'),
                 ('E-SCOPE',FORMAL+'scope-statement.md'),
                 ('E-WP23',WP23),('E-UI66',UI66),
                 ('E-N01-HISTORY','review/wp23-n01-review-2026-10-01/recheck-v3/report.md'),
                 ('E-R7-ERRATA','review/remediation-seventh-20261015-prepare/current-navigation-errata.json')]:
    evidence(eid,path)
evidence('E-INVENTORY',ROOT+'/tasks/inventory_denominator/manifest-purpose-disposition.json',[],
         'FULL_READ_TOP_LEVEL_EXCEPT_lines; sections FULL_READ; lines MECHANICALLY_PARSED_ONLY',commit=CARRIER)
evidence('E-COVERAGE',ROOT+'/tasks/coverage_acceptance_audit/review.md',commit=CARRIER)
evidence('E-COVERAGE-CONTRACT',ROOT+'/tasks/coverage_acceptance_audit/coverage-gaps.json',[],
         'FULL_READ supplemental_contracts[4] ONLY',commit=CARRIER)
evidence('E-R8-INPUTS','delivery/2026-10-16-seventh/eighth-review-inputs.json',[],
         'FULL_READ top-level except formal_files; formal_files IDENTITY_PARSED_ONLY')
evidence('E-HISTORY-NAV','delivery/2026-10-16-seventh/history-navigation.json',[],
         'PARTIAL: initial oversized display; retained_qualifications, restore_branch, old56_92 and other bounded top-level fields read; no whole-file credit')
evidence('E-AUDIT','audit/source-traceability.md',[[525,548],[1305,1335]])
evidence('E-MATRIX','planning/feature-matrix.md',[[184,187]])
evidence('E-SH34',CAT,[[199,201]])
evidence('E-R-SELECTOR',STORAGE,[[837,938],[1705,1770],[1964,2021]],reference=True)
evidence('E-R-CHAMBER',CHAMBER,[[361,546],[1270,1308]],reference=True)
evidence('E-R-CONTAINER',CONTAINER,[[1,275]],reference=True)
evidence('E-R-SAVE',SAVE,[[86,107]],reference=True)
evidence('E-R-SETTINGS',SETTINGS,[[210,230]],reference=True)
dump('evidence-catalog.json', {'schema':'r8-external-legacy-evidence/v1','as_of_utc':NOW,
     'identity_checks_are_tool_validation_only':True,'items':catalog})

# Every frozen physical unit is retained. These groups are reader-authored
# observations of fully read text, not a regex-based currentness exemption.
groups = [
 ('G-IDENTITY',[(1933,1934),(3368,3376)],'CLOSURE-R01仅登记身份更正；18错误字段由2795–2827勘误取代，原正确17条与旧报告保留。该段还含限定通过/后续待办，整段不能降为hash索引。',['E-MANIFEST:2795–2827','E-R7','E-CURRENT']),
 ('G-N01',[(1935,1940),(3377,3402)],'N01修订历程；v1空格→false和v2操作表的过强概括被1937/1939及3388/3397逐项修正；正确三层、取消及既有写入合同被B8 WP23§8.1继承。历史待审不是本轮批准。',['E-N01-HISTORY:1–76','E-WP23:133–153','E-UI66:39–41,134–143','F-N01-01–05']),
 ('G-UI-FIRST',[(1941,1956),(3403,3449)],'覆盖优先/先修已知问题授权按R73→R77时点变化；首稿UI/mail/地图/电话与第一组29项修订为版本历程。当前授权由用户本轮覆盖，当前行为以B8正式文和R为主，旧Drafted/PASS不转授。',['E-EXTRACTION:52–89','E-CURRENT','E-FORMAL-README:1–21']),
 ('G-GR',[(1957,1976),(3450,3511)],'GR001–016逐批修订与残留修订记录，含真实行为及复合案例，不能以批次结案代替当前源/条款阅读。传送/移动/Encounter、参与索引、Fling、概率表/EV等需按各当前owner接收。',['E-MANIFEST:3450–3511','E-CURRENT','E-R8-INPUTS:/full_review_scope']),
 ('G-INITIAL',[(2849,2926)],'WP11–17交界及v1/v2/v3修订/有限通过。2849不是纯行政：车辆、步数、跟随、异常、缺图等事实；2855–2858/GR004/005/011给过强概括的具体后继。当前源与正式条款仍须独立接收。',['E-MANIFEST:2855–2858,3453–3454,3480–3489,3997–4003','E-EXTRACTION:95–211','E-CURRENT']),
 ('G-CREATURE-EARLY',[(2927,3036)],'WP18–30初稿、修订、闭合及新包开始；身份/统计/PP/接收返回与领域写入/背包/成长等属于行为快照与回归候选。原通过身份限定旧输入，不能当B8批准。',['E-MANIFEST:2939–3036,4039–4059','E-FORMAL-README:5–9','E-CURRENT']),
 ('G-EVO-BREED',[(3037,3108)],'物品/进化/商店及寄养繁殖、时间天气/遭遇/树果/钓鱼的修订序列；后续v3等更正初稿精确门和先后，不以同域PASS认证当前字节。',['E-MANIFEST:3045–3108,4018–4024','E-FORMAL-README:5–9','E-CURRENT']),
 ('G-BATTLE',[(3109,3311)],'战斗命令/回合/效果/AI/道具/设施/回放/捕获/图鉴的版本及跨合同修订。BATCH-C01/C02/C03与N01等各自有条件；不能压成统一已通过，也不能把源缺陷改成理想规则。',['E-MANIFEST:3148–3311,4025–4031,4060–4087','E-CURRENT','E-R8-INPUTS:/full_review_scope']),
 ('G-SHADOW-UI-PUZZLE',[(3312,3367)],'WP22/23/32及WP66-B/C/71旧限定通过和修订记录；WP23 N01为后来专项，不能让早先通过覆盖其选择可达性；拼图有限合法态前提保留。',['E-MANIFEST:3377–3402','E-N01-HISTORY','E-WP23:147–153','E-FORMAL-README:5–9']),
 ('G-UI-LIFECYCLE',[(1977,1992),(3512,3586)],'WP65/67A/67B首稿→v2→v3；UI取消结果不等于领域回滚、经验/图鉴/HOF时点与显示层区别。旧作者修订完成/待审是历史阶段，当前合同另需逐条核。',['E-MANIFEST:3520–3586,4088–4094','E-FORMAL-README:5–9','E-CURRENT']),
 ('G-ROAM-CONTEST',[(1993,1999),(3587,3637)],'WP37/53初稿由v2/v3细化：路线键/能力缓存/PP/异色公式、Safari/contest状态、计数、重复和预算方向；原草稿非最终行为。',['E-MANIFEST:3595–3637,4018–4024,4032–4038','E-FORMAL-README:5–9','E-CURRENT']),
 ('G-PASSIVE-DEBUG',[(2000,2011),(3638,3690)],'WP61毒扣血/blackout与缺home前缀修订、WP72debug归属/入口及WP73初稿；后继不支持取消全无写入或missing home恒清escape等强断言。',['E-MANIFEST:3646–3667,3691–3718','E-R7-ERRATA','E-CURRENT']),
 ('G-EDITORS',[(2012,2021),(3691,3718)],'WP72/73合审v2/v3/v4及v5记录更正；嵌套新建PBS写入与共享容器修改不由外层No回滚，v5仅记录而非再改case。',['E-MANIFEST:3691–3718,4095–4102','E-FORMAL-README:5–9','E-CURRENT']),
 ('G-ANIMATION',[(2022,2029),(3719,3746)],'WP74首稿到18/6/2项收尾：cache identity、浅拷贝、当前帧守卫、0长度、采样和文件部分写入修正首稿概括。各条真实执行仍0。',['E-MANIFEST:3726–3746,4095–4102','E-FORMAL-README:5–9','E-CURRENT']),
 ('G-CONVERTERS',[(2030,2037),(3747,3774)],'WP75首稿/20项及7/2残留：35映射、非幂等、逐段插入失败、9/10/11守卫、文本前提/转义/位置别名与文件前缀副作用，不能采首版理想归纳。',['E-MANIFEST:3754–3774,4095–4102','E-FORMAL-README:5–9','E-CURRENT']),
 ('G-GENERATOR',[(2038,2045),(3775,3802)],'WP76首稿到20/5/2项修订：普通抽样返回、标志、重复EV340、容量与有效队伍终止、科学计数及缩放更新，不是成功生成或全域EV510保证。',['E-MANIFEST:3782–3802,4095–4102','E-FORMAL-README:5–9','E-CURRENT']),
 ('G-IMPORTED',[(2046,2049),(3803,3819)],'九原输入整合、41状态+5导航共46项管理回填；旧46+5由v2精确更正，后6个B链接另计。B21明确九原输入曾获限定批准但新输出不继承批准。',['E-MANIFEST:3812–3819,4115–4127','E-FORMAL-README:5–9','E-SCOPE:5–9','E-CURRENT']),
 ('G-DEMO',[(2050,2059),(3820,3854)],'WP77初稿及9/3项修订、有限管理回填；配置→事件/地图→消费者范围分别记，不把EvidenceInventory或事件缺失变成运行可达确认。',['E-MANIFEST:3827–3854,4095–4102','E-FORMAL-README:5–9','E-CURRENT']),
 ('G-JUNCTIONS',[(2060,2073),(3855,3904)],'WP78交界30/39→51→54及8链的精确计数与109文件不同read方法；原静态范围通过不授全source覆盖，新增接口仍需接收。',['E-MANIFEST:3870–3904','E-FORMAL-README:5–9','E-R8-INPUTS:/full_review_scope']),
 ('G-COVERAGE',[(2074,2079),(3905,3947)],'WP79逐轮覆盖判断校准；20 AI评分文件由排除改为全行为读取、补战前过渡/参数与失败重试范围；312源范围不等于432源后继或本轮全量已读。',['E-MANIFEST:3927–3947','E-FORMAL-README:5–9','E-R8-INPUTS:/full_review_scope']),
 ('G-WP80',[(3948,4114)],'WP80导航、批次1–15净化与作者完成报告；语义零变化/同字节/PASS引用是作者自检或旧输入阶段，不是本轮独立签收。111正文/18测试/2根=131与113原输入/84包/87行/113Feature分别保留。B21作者候选后继及R7最终导航明确更晚状态。',['E-MANIFEST:4115–4127','E-FORMAL-README:1–21','E-SCOPE:1–21','E-CURRENT','E-R7','E-R8-INPUTS']),
]
frozen = json.loads((OUT/'frozen-primary-structure.json').read_text())
raw = (REPO/MANIFEST).read_bytes().splitlines(keepends=True)
units=[]
for old in frozen['units']:
    n=old['line']; text=raw[n-1].decode().strip()
    matches=[g for g in groups if any(a<=n<=b for a,b in g[1])]
    assert len(matches)==1, (n,[g[0] for g in matches])
    g=matches[0]
    typ='layout' if not text else ('heading' if text.startswith('**第') else 'content_paragraph')
    units.append({
       'id':old['id'],'line':n,'byte_start':old['byte_start'],'byte_end':old['byte_end'],
       'bytes':old['bytes'],'sha256':old['sha256'],'structure':typ,'read':'FULL_READ',
       'purpose_group':g[0],
       'purpose_status':'LAYOUT_NO_ASSERTION' if typ=='layout' else ('HISTORICAL_STAGE_HEADING' if typ=='heading' else 'READ_CURRENT_FACT_INHERITANCE_NOT_CLOSED'),
       'historical_context_reason':g[2], 'exact_successor_or_qualification_evidence':g[3],
       'current_behavior_reliance':'NO_ASSERTION_IN_THIS_UNIT' if typ!='content_paragraph' else 'UNVERIFIED_PER_ATOMIC_ASSERTION',
       'atomic_assertions':'NOT_APPLICABLE' if typ!='content_paragraph' else 'UNDECOMPOSED',
       'root_reception':'UNRECEIVED',
       'exemption':'None: a mixed paragraph is never inventory_only merely because it contains identities or an old date.'
    })
counts=collections.Counter(x['structure'] for x in units)
assert counts=={'content_paragraph':881,'layout':381,'heading':151}, counts
dump('purpose-dispositions.json',{
 'schema':'r8-external-legacy-purpose/v1','input':'E-MANIFEST','ranges':[[1933,2079],[2849,4114]],
 'reader':'actual /root external delegated context','counts':dict(counts),
 'status':'INCOMPLETE_NO_PASS','qualification':'Each physical structure has a reason and routing. This is not a completed atomic currentness disposition; all 881 content paragraphs conservatively retain an unresolved inheritance/acceptance obligation. No paragraph is dismissed by date or negative search.',
 'groups':[{'id':g[0],'ranges':g[1],'reason':g[2],'successors':g[3]} for g in groups], 'units':units})

search_args=['rg','-n','--glob','*.md','--glob','*.json','--glob','!review-manifest-2026-09-19.md',
 'review-manifest-2026-09-19|版本清单','README.md','CURRENT-DELIVERY.md','delivery/2026-10-16-seventh','planning','audit',FORMAL.rstrip('/')]
search=subprocess.run(search_args,cwd=REPO,capture_output=True,text=True)
dump('bounded-consumer-search.json',{'schema':'r8-external-legacy-search/v1','utc':NOW,'commit':B8,
 'argv':search_args,'stdout':search.stdout,'stderr':search.stderr,'exit_code':search.returncode,
 'purpose':'Locator and bounded negative evidence only, not full semantic read or absence proof.',
 'positive_consumer':'E-EXTRACTION:3 directs current execution progress to manifest together with per-WP records and feature-matrix.',
 'limitations':'No dynamic/generated/synonym reference absence proof; history outside selected roots not exhaustively searched.'})

facts=[
 {'id':'F-N01-01','premise':'Ordinary storage-selection call from chamber; preceding UI/resource calls return normally; base storage; no monkey patch.',
  'fact':'Mode1 returns internal box selection without opening the normal party tab; the party button emits a special position. Empty mapped member repeats the outer loop; a present member reaches the menu and Select alone returns its original position.',
  'source':['E-R-SELECTOR:837–938,1964–2021','E-R-CHAMBER:1273–1281','E-R-CONTAINER:159–178'],
  'consumer':['E-R-CHAMBER:400–407,423–546'],'spec':['E-WP23:147–151','E-UI66:39–41'],'legacy':['LM-L1935','LM-L1937','LM-L1939','LM-L3380','LM-L3388','LM-L3397'],
  'status':'SOURCE_STATIC_BOUNDED; NOT_ROOT_RECEIVED','excluded':'Does not certify every special-position Withdraw/Item/Mark or held-member descendant.'},
 {'id':'F-N01-02','premise':'Selection loop reaches confirmation; confirmation returns its normal yes/no meaning; media helpers return normally.',
  'fact':'BACK: Yes continues and No/cancel exits with empty position; Close Box: Yes exits and No/cancel continues. Empty position means no new chamber placement/replacement.',
  'source':['E-R-SELECTOR:1964–2021','E-R-CHAMBER:400–407,423–546,1273–1281'],
  'consumer':['E-R-CHAMBER:400–407,495–529'],'spec':['E-WP23:137,149','E-UI66:132–143'],'legacy':['LM-L1937','LM-L1939','LM-L3388','LM-L3397'],
  'status':'SOURCE_STATIC_BOUNDED; NOT_ROOT_RECEIVED','excluded':'Confirmation wrapper/input service internals are dependencies not fully read in this context; no real key or resource execution.'},
 {'id':'F-N01-03','premise':'One JUMP box switch or one valid completed Withdraw has already returned normally before later selection cancellation; base container; party has room for Withdraw.',
  'fact':'Current-box writes and completed box→party move precede the later empty return. The selector and chamber empty-result path have no inverse operation restoring these writes.',
  'source':['E-R-SELECTOR:837–938,1705–1722,1964–2021','E-R-CONTAINER:129–178,180–211,254–260'],
  'consumer':['E-R-CHAMBER:400–407,423–546'],'spec':['E-WP23:149','E-UI66:76–78,134–143'],'legacy':['LM-L1937','LM-L1939','LM-L3388','LM-L3397'],
  'status':'SOURCE_STATIC_BOUNDED; NOT_ROOT_RECEIVED','excluded':'No actual save/reload or media/host observation; item/mark descendants not re-proved merely by this move example.'},
 {'id':'F-N01-04','premise':'Direct caller supplies a valid party position; target chamber slot meets egg/Shadow placement gates; all invoked presentation helpers return normally.',
  'fact':'Successful placement precedes source deletion; party deletion compacts without a last-able-member check in these bounded functions. This direct-call fact does not establish ordinary UI reachability of party positions.',
  'source':['E-R-CHAMBER:361–407','E-R-CONTAINER:159–178,254–260'],
  'consumer':['E-R-CHAMBER:400–407'],'spec':['E-WP23:137,151','E-SH34:200'],'legacy':['LM-L1935','LM-L1937','LM-L3380','LM-L3388'],
  'status':'SOURCE_STATIC_BOUNDED; NOT_ROOT_RECEIVED','excluded':'No global no-guard assertion; surrounding PC/storage guards remain outside this direct path.'},
 {'id':'F-N01-05','premise':'Default base container construction, 40 boxes of 30 slots, special position[-2,-1]; ordinary Ruby array negative indexing; loaded storage remains the expected class.',
  'fact':'Special position selects zero-based box38 slot29, not the party. New-game storage constructor and save registration bind the base container; no actual native save roundtrip was performed.',
  'source':['E-R-CONTAINER:1–77,159–178','E-R-SETTINGS:216–225','E-R-SAVE:97–102'],
  'consumer':['E-R-SELECTOR:1984–2001','E-R-CHAMBER:400–407,495–529'],'spec':['E-WP23:150','E-UI66:41'],'legacy':['LM-L1935','LM-L1937','LM-L3380','LM-L3388'],
  'status':'SOURCE_STATIC_BOUNDED; NOT_ROOT_RECEIVED','excluded':'Ruby negative indexing is language-level reading, not a newly executed model; save framework serialization/load internals and RegionalStorage are not certified.'},
]
dump('forward-mapping.json',{'schema':'r8-external-legacy-forward/v1','status':'PARTIAL_MAPPING_NOT_COMPLETION',
 'all_primary_structure_dispositions':'purpose-dispositions.json#/units','facts':facts,
 'remaining':'All881 mixed content paragraphs require atomic decomposition/current-fact and acceptance-purpose disposition, including other facts in N01 paragraphs. These5 bounded facts are explicit positive inheritance, not sampling evidence for any remaining paragraph.'})
dump('reverse-mapping.json',{'schema':'r8-external-legacy-reverse/v1','status':'PARTIAL_MAPPING_NOT_COMPLETION',
 'clauses':[{'spec':s,'fact':f['id'],'premise':f['premise'],'source':f['source'],'qualification':f['status']} for f in facts for s in f['spec']],
 'full_read_files':['E-WP23','E-UI66'],'full_reverse_acceptance_files':0,
 'gaps':'Full text reading of2 current files does not certify all their clauses. Data supplements, complete test families, all source definitions/receivers and every composite clause are not reverse-closed here.'})
dump('interfaces.json',{'schema':'r8-external-legacy-interfaces/v1', 'root_reception':'UNRECEIVED',
 'interfaces':[
 {'id':'I-LMC-NAV','producer':'E-EXTRACTION:3','consumer':'E-MANIFEST historical progress','finding':'Positive surviving navigation; negative B8-string search is insufficient to dismiss historical behavioral paragraphs.','state':'READ_NOT_ROOT_RECEIVED'},
 {'id':'I-LMC-N01','producer':'F-N01-01–05','consumers':['WP23','WP66-B','WP25 base container','SH34','feature F06-08','source-traceability T-WP23-01/T-WP66B-01'],
  'state':'BOUNDED_STATIC_CHAIN_NOT_ROOT_RECEIVED','not_closed':['Confirmation/input wrappers','All item/mark/held/special-position descendants','Full WP25 contracts and all current vectors','Real save/reload/host/resource observation']},
 {'id':'I-LMC-2849','producer':'E-MANIFEST:2849','consumers':['WP11/WP12 vehicle/steps','WP13 following','WP07 exception boundary','WP09/10 map loading'],
  'state':'PRIMARY_READ_CURRENT_SOURCE_AND_CLAUSE_RECEPTION_PENDING','successor_candidates':['E-MANIFEST:2855–2858,3453–3454,3480–3489,3997–4003'],'warning':'No source-to-current-formal certification by reading these historic statements.'},
 {'id':'I-LMC-WP80','producer':'E-MANIFEST:3948–4114','consumers':['E-FORMAL-README','E-SCOPE','E-CURRENT','E-R7'],
  'state':'STAGE_QUALIFICATION_READ; ATOMIC_ACCEPTANCE_DEPENDENCIES_NOT_CLOSED','finding':'Author completion/semantic-zero/old PASS is not current independent acceptance;131/113/84/87/432 are distinct denominators.'},
 {'id':'I-LMC-ALL-OTHER','producer':'purpose-dispositions.json#/units','consumer':'B8 corresponding formal/source owners and root history/coverage receiver',
  'state':'PENDING_EXACT_ATOMIC_MAPPING','blocking':'Blocks currentness completion and zero-unreceived claim; readable work, not host/material limit.'}
 ]})

# A suspicion plus its contrary evidence; no self-appointed independent counter.
dump('proposals.json',{'schema':'r8-external-legacy-proposals/v1','required_count':0,'canonical_GR8_ID_assignment':'ROOT_ONLY',
 'items':[{
  'id':'R8-LMC-H001','classification':'SUSPECTED_CURRENT_QUALIFICATION_DRIFT','severity':'P3_PROVISIONAL; navigation/acceptance interpretation only, no newly proven source behavior mismatch',
  'module_WP':'WP23 / WP66-B / current history qualification','root_cause_key':'N01-wait-versus-closed-snapshot-scope','canonical_alias':'LOCAL_PROPOSAL_ONLY; not an allocated GR8 required ID',
  'history':['WP23-N01','WP23-N01-R01','WP23-N01-C01'],'state':'SUBMITTED_WITH_CONTRARY_EVIDENCE_FOR_ROOT_NONPROPOSER_RECEPTION',
  'proposer':'actual /root external delegated context','independent_counter_reader':'NOT_ASSIGNED_NOT_EXECUTED','root_decision':'UNRECEIVED',
  'evidence':['E-UI66:5,39–41,304–311','E-WP23:147–151','E-SH34:200','E-AUDIT:529–541,1318–1328','E-MATRIX:186','E-N01-HISTORY:1–76','E-FORMAL-README:5–21','E-SCOPE:5–21','E-CURRENT','E-R7-ERRATA'],
  'bidirectional_fact_chain':'F-N01-01–05 in forward-mapping.json, with reverse clause links in reverse-mapping.json. Full path/commit/tree/blob/bytes/SHA/range identities resolve through evidence-catalog.json; recover with git show <commit>:<path>.',
  'premise':'B8 reader navigates current formal WP66-B §12.4 and audit T-WP66B-01, then current WP23 §8.1 and SH34. Question is whether waiting wording asserts a current unresolved N01 or preserves a qualified historical snapshot.',
  'ordinary_control':'WP23 §8.1/SH34 and historical v3 report agree on finite three-layer contract and scoped N01 closure; retained special-position descendant/host/resource limits still open.',
  'minimal_counterexample_steps':['At fixed B8 read E-UI66:309 and E-AUDIT:1328: N01 is described as waiting for special handling.','Read E-WP23:147–151, E-SH34:200 and E-N01-HISTORY:1–76: same finite selection contract has scoped closure.','Then read parent E-FORMAL-README:5–9 and E-SCOPE:5–9 before deciding: they explicitly preserve old pending records at original time; E-CURRENT gives later R7 delivery status. This is material contrary evidence, not resolved by a search.'],
  'source_expectation_and_current_difference':'Bounded source chain supports the three-layer conditional behavior, not a waiting/closed administrative state. The suspected difference is between two current-tree status descriptions, with explicit parent historical qualification potentially resolving it.',
  'normal_cancel_failure_partial_commit':'F-N01-02/03 distinguish cancellation from rollback; F-N01-04 direct caller and F-N01-05 special negative mapping have finite premises. UI/media/helper failures keep reached writes and do not prove normal return or cleanup. No new engine change proposed.',
  'negative_evidence':'E-R7-ERRATA was fully read and concerns GR7-H08-001 / WP72 label, not N01. bounded-consumer-search.json has only a bounded literal-navigation scope; it proves no universal absence. Other exact history/current owner evidence remains unreceived.',
  'impact':'If the wording is treated as current pending, a reader could reopen a previously finite closed N01. If parent qualification already makes the historical scope unambiguous, no required revision is warranted.',
  'evidence_levels':['SOURCE_STATIC bounded chain','DERIVED_VECTOR paper cases only NOT_EXECUTED','TOOL_VALIDATION identities/search only'],
  'minimum_correction_if_confirmed':'Replace only currently operative stale N01 status/navigation with an exact scoped historical closure pointer; retain the frozen old records and all unexhausted-descendant, direct-call, host/media/default-data limits. If parent historical qualification is sufficient, preserve the original text and record no-required with exact rationale.',
  'suggested_read_set':['E-UI66 FULL','E-WP23 FULL','E-SH34:199–201','E-AUDIT T-WP23-01/T-WP66B-01','E-MATRIX F06-08','E-N01-HISTORY FULL','E-FORMAL-README FULL','E-SCOPE FULL','E-CURRENT FULL','F-N01-01–05 source ranges'],
  'suggested_write_set_if_required':['deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md:309 status only','audit/source-traceability.md:1328 current qualification only','separately authorized receiving evidence'],
  'write_authorization':'NONE in this task; UPDATE_NOT_STARTED; even proposed formal edits require the separately launched update.',
  'acceptance_regression':['Different actual nonproposer reads the exact qualification and relevant contrary evidence, then records required/no-required/optional with reason.','No blanket closure of old WP23 R01–03, GR001–016, special-position descendants or host/media limits.','Preserve N01 BACK Yes continue/No exit and Close Box Yes exit/No continue, empty-member loop, Select return gate, prior write retention, direct-call-only last-able absence.','Do not rewrite historical reports or transfer their PASS to B8. Any adopted status sync has one root-owned canonical ID and received exact bytes.'],
  'dependencies':{'blocking':['Actual different-context counterevidence','Root currentness/coverage reception'],'nonblocking':['No runtime needed to decide the document-status scope; all behavioral vectors remain NOT_EXECUTED'],
    'conflicts':['WP66-B and audit are shared with UI/history/source-traceability owners; root must designate one writer if any change is accepted'],
    'batch':'UNASSIGNED_ROOT_ONLY','author':'NOT_STARTED','reviewer':'NOT_ASSIGNED','shared_receiver':'Main reviewer/root',
    'closure':'Root decision on exact bytes plus nonproposer counterevidence; no closure performed here'},
  'contrary_evidence_assessment':'The proposer currently sees substantial reason for NO_REQUIRED_REVISION because B21 parent expressly preserves old pending status at original time. This is the proposer’s analysis, not an independent counter or root adjudication.',
  'excluded_claims':['No confirmed new required defect','No all-paragraph currentness certification','No global PASS','No implementation/runtime equivalence']
 }]})

ledger=json.loads((OUT/'reading-ledger.json').read_text())
ledger['updated_utc']=NOW
ledger['current_purpose']='INCOMPLETE; see purpose-dispositions.json; no zero-qualification-gap claim'
ledger['actual_counts']={'primary_physical_lines':1413,'primary_bytes':627400,'primary_read':1413,'primary_unread':0,
 'primary_unreceived':1413,'navigation_read_lines':230,'manifest_total_read_lines':1643,'manifest_other_lines_not_semantically_read':2484,
 'content_paragraphs':881,'headings':151,'layout_lines':381,'atomic_assertion_denominator':'UNFROZEN','currentness_unclosed_content_paragraphs':881,
 'formal_full_read_files':2,'formal_all_clause_reverse_closed_files':0,'bounded_fact_mappings':5,'new_required_findings':0}
ledger['frozen_inventory_note']='frozen-primary-structure.json records the pre-read UNREAD state; this reading ledger and purpose-dispositions.json are the authoritative later read state. Its paragraph_line type corresponds to151 stage headings. Physical units are not atomic clauses.'
ledger['additional_full_reads']=['E-EXTRACTION','E-FORMAL-README','E-SCOPE','E-WP23','E-UI66','E-N01-HISTORY','E-R7-ERRATA']
ledger['additional_field_or_range_reads']=['E-R8-INPUTS','E-HISTORY-NAV','E-AUDIT','E-MATRIX','E-SH34','E-R-SELECTOR','E-R-CHAMBER','E-R-CONTAINER','E-R-SAVE','E-R-SETTINGS']
ledger['range_authority']='evidence-catalog.json exact ranges override loose method-name descriptions. Out-of-range source lines not credited.'
ledger['truncation_handling']='Initial oversized displays of global prompt/primary or navigation were reread in bounded complete ranges where FULL_READ is claimed. Huge inventory JSON lines array, history navigation whole file, locator searches, failed path lookups and clipped rg output do not receive whole-file semantic credit.'
dump('reading-ledger.json',ledger)

progress=json.loads((OUT/'progress.json').read_text())
progress.update({'updated_utc':NOW,'status':'INCOMPLETE_NO_PASS_EVIDENCE_READY_FOR_ROOT_RECEPTION','update_started':False,
 'review_reading_end_utc':NOW,'publication':'NOT_YET_PUSHED',
 'structure_denominator':dict(counts),'atomic_assertion_denominator':'UNFROZEN',
 'currentness_unclosed_content_paragraphs':881,'root_received_primary_lines':0,
 'pending':['Atomic decomposition and per-assertion current behavior/acceptance-purpose qualification of881 mixed content paragraphs',
 'Exact source/formal/consumer obligations outside5 bounded N01 facts, notably manifest2849 interfaces',
 'Different-context nonproposer reception of R8-LMC-H001 and contrary evidence; root final adjudication',
 'Root reception of all1413 primary lines and shared currentness mappings',
 'Commit/ordinary push and full remote byte readback']})
dump('progress.json',progress)

dump('gaps.json',{'schema':'r8-external-legacy-gaps/v1','status':'INCOMPLETE_NO_PASS','gaps':[
 {'id':'LMC-GAP-ATOMIC','type':'READABLE_REVIEW_WORK_NOT_LIMIT','denominator':'881 fully read content paragraphs; atomic assertion denominator UNFROZEN',
  'unclosed_ids':[x['id'] for x in units if x['structure']=='content_paragraph'],
  'missing':'Complete per-assertion decomposition, premises, exact current source/formal/consumer/acceptance-purpose disposition. A group reason is routing, not atomic reception.'},
 {'id':'LMC-GAP-ROOT','type':'INDEPENDENT_RECEPTION_REQUIRED','denominator':1413,
  'unreceived_ranges':[[1933,2079],[2849,4114]],'missing':'Actual main-reviewer/root acceptance, not role renaming in this context.'},
 {'id':'LMC-GAP-CONSUMERS','type':'READABLE_REVIEW_WORK_NOT_LIMIT','missing':'All current consumers and complete current formal/test/data source chains beyond the bounded N01 facts; even two full-read formal files have0 fully reverse-accepted file certificates.'},
 {'id':'LMC-GAP-EXECUTION','type':'NOT_EXECUTED','missing':'All new reference observations, independent behavior model, game/host/Demo/native media/save/replay and business vectors remain0; tool validation is separate.'},
 {'id':'LMC-GAP-CONFIG','type':'UNVERIFIED','missing':'Actual model/effort/tier/speed/Fast and opaque execution session/platform log ID are not echoed. Source-thread ID is origin, not execution ID.'}
 ]})
print(json.dumps({'catalog_entries':len(catalog),'physical_units':len(units),'counts':dict(counts),'mapped_bounded_facts':len(facts),'status':'INCOMPLETE_NO_PASS'},ensure_ascii=False))
