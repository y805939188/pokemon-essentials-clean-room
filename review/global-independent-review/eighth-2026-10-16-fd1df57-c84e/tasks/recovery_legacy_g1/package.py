"""Package explicitly authored recovery notes; never infer semantic PASS."""
import csv
import datetime
import hashlib
import json
from pathlib import Path
import subprocess

TASK = Path(__file__).resolve().parent
ROOT = TASK.parents[1]
REPO = ROOT.parents[2]
OLD = ROOT / 'tasks/receive_external_legacy_manifest_currentness'
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
CONTRACT = '2d44dafe215842de6355f46de7d4d273d8b4c264'

def dump(name, value):
    (TASK / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def git(*args, reference=False):
    return subprocess.check_output(['git', '-C', '/workspace/pokemon-essentials' if reference else str(REPO), *args])

def identity(commit, path, reference=False):
    raw = git('show', commit + ':' + path, reference=reference)
    mode, kind, blob = git('ls-tree', commit, '--', path, reference=reference).decode().split('\t')[0].split()
    assert kind == 'blob'
    return {'commit': commit, 'path': path, 'mode': mode, 'blob': blob, 'bytes': len(raw),
            'sha256': hashlib.sha256(raw).hexdigest()}, raw

def main():
    ds = [json.loads((OLD / f'split-contracts/S{i:02}.complete.json').read_text()) for i in range(1, 6)]
    notes = list(csv.DictReader((TASK / 'event-notes.tsv').open(), delimiter='\t'))
    es = {e['id']: (d['id'], e) for d in ds for e in d['events_all_fields']}
    assert len(notes) == len(es) == len({n['event'] for n in notes}) == 60
    assert {n['event'] for n in notes} == set(es)
    target_dir = TASK / '.cache/target-93d7df7f'
    old_tsv = {int(x['round']): x for x in csv.DictReader((target_dir/'event-judgments.v2.tsv').open(), delimiter='\t')}
    for _, event in es.values():
        assert old_tsv[event['round']]['current_purpose_judgment'] == event['reader_judgment']
    manifest_id, manifest = identity(B8, 'planning/review-manifest-2026-09-19.md')
    lines = manifest.splitlines(keepends=True)
    receipt = json.loads((TASK / 'input-identities.json').read_text())
    all_lines = {p['line'] for d in ds for p in d['physical_line_identities']}
    paragraphs = {p['line'] for d in ds for p in d['paragraph_dispositions_all_fields'] if p['structure'] == 'content_paragraph'}
    assert (len(all_lines), len(paragraphs)) == (559, 381)
    denominator = {'schema': 'r8-recovery-legacy-g1-denominator/v1', 'contract': CONTRACT,
                   'scope': ['S01', 'S02', 'S03', 'S04', 'S05'], 'freeze_observed_utc': receipt['utc'],
                   'source_identity': manifest_id, 'events': sorted(es), 'physical_lines': len(all_lines),
                   'content_paragraphs': len(paragraphs), 'content_bytes': sum(len(lines[i-1]) for i in paragraphs),
                   'physical_bytes': sum(len(lines[i-1]) for i in all_lines),
                   'exact_line_set': 'input-identities.json#/shards/*/lines',
                   'population_note': '事件/物理行/内容段相互重叠，不相加为需求数；S05摘要与详细版均计入实际阅读。'}
    dump('frozen-denominator.json', denominator)
    events = []
    for n in notes:
        shard, e = es[n['event']]
        raw = b''.join(b''.join(lines[a-1:b]) for a,b in e['line_ranges'])
        events.append({'event': n['event'], 'shard': shard, 'ranges': e['line_ranges'],
                       'source_bytes': len(raw), 'source_sha256': hashlib.sha256(raw).hexdigest(),
                       'meaning': n['meaning_and_retained_boundary'], 'interface_group': n['interface_group'],
                       'purpose_reception': 'MANUALLY_READ_VERSION_PURPOSE_RETAINED',
                       'complete_event_reception': 'OPEN_NECESSARY_CURRENT_DEFINITION_AND_CONSUMER_RECEPTION',
                       'current_routes': e['current_formal_routes'], 'successors': e['actual_successor_events'],
                       'contract_event_pointer': f'split-contracts/{shard}.complete.json#/events_all_fields/id={e["id"]}',
                       'strongest_no_required_ref': '#/common_no_required',
                       'unreceived_ref': 'interfaces.json#/providers via current_routes'})
    dump('reception-ledger.json', {'schema': 'r8-recovery-legacy-g1-reception/v1', 'actual_context': '01a144ee-2560-737b-991a-fa11fc09202e',
         'mode': 'REPLACEMENT_RECOVERY_NOT_ADDITIONAL_VOTE', 'additional_independent_votes': 0,
         'status': 'INCOMPLETE', 'purpose_read_events': 60, 'complete_event_receptions': 0,
         'reason': '完整事件接收不能由用途实读/路由/旧批准推定；跨域固定材料缺口和可得未接收分开列明。',
         'common_no_required': 'B21明确限定旧时点；具体错误按逐事件修订链保留，旧待审/旧PASS及回填身份不构成B8正文新缺陷或当前批准。当前行为是否完备仍需固定primary逐事实接收；这不是对未读当前行为给NO_REQUIRED。',
         'events': events, 'business_execution': 'NOT_EXECUTED', 'UPDATE_NOT_STARTED': True})

    # These are actual tool-output references from this session, not an invented exported transcript.
    output_refs = {'S01': ['423b20', '68541b'], 'S02': ['635bb3', '91ed04'],
                   'S03': ['b1987f', '34a17c'], 'S04': ['3b6d01', '307281'], 'S05': ['e157fc', '30040c']}
    reads = []
    def add_read(commit, path, ranges, output, level, reference=False):
        ident, data = identity(commit, path, reference=reference)
        ls = data.splitlines(keepends=True)
        rs = []
        for a,b in ranges:
            assert 1 <= a <= b <= len(ls)
            raw = b''.join(ls[a-1:b])
            rs.append({'lines': [a,b], 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
        reads.append({**ident, 'ranges': rs, 'actual_output_chunks': output, 'credit': level})
    for shard, outputs in output_refs.items():
        d = next(d for d in ds if d['id'] == shard)
        ranges = [x for e in d['events_all_fields'] for x in e['line_ranges']]
        add_read(B8, manifest_id['path'], ranges, outputs, 'FULL_ORIGINAL_TEXT_AND_EVENT_PURPOSE_READ')
    add_read(B8, manifest_id['path'], [[3341,3402],[1933,1940]], ['9eed32','52f893'], 'DEPENDENCY_ONLY_E066_E072_NO_PRIMARY_CREDIT')
    add_read(CONTRACT, str((ROOT/'inputs/eighth-global-review-prompt.md').relative_to(REPO)), [[1,241]], ['2981ea','541777','455b23'], 'FULL_CONTRACT_READ')
    add_read(CONTRACT, str((ROOT/'inputs/review-SKILL.md').relative_to(REPO)), [[1,51]], ['455b23'], 'FULL_READ_NOT_APPLIED_TO_AUDIT_REPORT')
    add_read(B8, 'AGENTS.md', [[1,297]], ['767aeb'], 'FULL_APPLICABLE_INSTRUCTIONS_READ')
    for path, ranges, outputs in [
        ('deliverables/final-specification-set/README.md',[[1,11]],['a156e1']),
        ('deliverables/final-specification-set/scope-statement.md',[[1,11]],['dac499']),
        ('CURRENT-DELIVERY.md',[[1,13]],['a156e1']),
        ('planning/extraction-plan.md',[[1,20]],['a156e1']),
        (manifest_id['path'],[[1,8],[4115,4127]],['a156e1'])]:
        add_read(B8,path,ranges,outputs,'BOUNDED_CURRENT_QUALIFICATION_READ')
    for path, ranges, outputs in [
        ('Data/Scripts/003_Game processing/002_Scene_Map.rb',[[1,101],[116,252]],['353920','c43a2b']),
        ('Data/Scripts/003_Game processing/004_Interpreter_Commands.rb',[[722,751]],['353920']),
        ('Data/Scripts/004_Game classes/008_Game_Player.rb',[[141,193],[416,555],[575,616]],['353920']),
        ('Data/Scripts/004_Game classes/006_Game_Character.rb',[[362,400],[893,993]],['c43a2b']),
        ('Data/Scripts/012_Overworld/001_Overworld.rb',[[69,218],[223,315]],['c43a2b','46ea0d']),
        ('Data/Scripts/003_Game processing/003_Interpreter.rb',[[138,206]],['c43a2b']),
        ('Data/Scripts/004_Game classes/010_Game_Follower.rb',[[1,215]],['46ea0d']),
        ('Data/Scripts/004_Game classes/011_Game_FollowerFactory.rb',[[155,191]],['46ea0d']),
        ('Data/Scripts/003_Game processing/001_StartGame.rb',[[37,104]],['46ea0d']),
        ('Data/Scripts/004_Game classes/005_Game_MapFactory.rb',[[1,88],[134,160]],['46ea0d','4533fb']),
        ('Data/Scripts/004_Game classes/004_Game_Map.rb',[[1,132]],['46ea0d'])]:
        add_read(R,path,ranges,outputs,'BOUNDED_SOURCE_STATIC_FIVE_WORLD_CHAINS',reference=True)
    for x in ds[0]['source_evidence_catalog']['items']:
        if x['id'].startswith('E-V2-WP'):
            actual = [[a,min(b,len(git('show',B8+':'+x['path']).splitlines()))] for a,b in x['ranges']]
            add_read(B8,x['path'],actual,['9bcba8'] if x['id']=='E-V2-WP11' else ['2929f3'],'BOUNDED_CURRENT_FORMAL_READ')
    dump('reading-ledger.json', {'schema':'r8-recovery-legacy-g1-reading/v1', 'reads': reads,
         'shared_attachment': {'sha256':'7753e800061b892e468a4a16a9758534a76cdd9e40b14e8713ddff4be0189f3e',
         'treatment':'五份Sxx附件精确相同，只读一次合同/global/skill/AGENTS；各Sxx独有前缀另逐份读。'},
         'truncation': [{'output':'69a420','treatment':'重复附件过大；按2981ea/541777/455b23全文补读，Sxx独有前缀由856710逐份补读。'},
                        {'output':'06764c','treatment':'依赖视图含重复段落元数据而截断；9eed32/52f893按原文全范围补读。'},
                        {'output':'ea1844','treatment':'标签路由渲染截断不授缺失部分阅读；381段原文已在10个Sxx输出完整呈现。段用途原因/后继/路由逐项等于所属事件，经c4cc4b验证无例外；身份字段只核身份。'},
                        {'output':'9bcba8','treatment':'WP11已读59–88/166–190；请求191–194越界报错，明确更正定位；其余五份由2929f3补读。'}],
         'private_io':'仅记录真实可见chunk标识和可复现命令，不声称私有平台完整流已导出/发布。',
         'no_generated_credit':'视图、恢复和本打包程序只作工具证据；人工内容在event-notes.tsv。'})

    routes = {x['id']: x for d in ds for x in d['current_routes_all_fields']}
    providers = {x['id']: x for d in ds for x in d['providers_all_fields']}
    provider_rows = []
    for pid, p in providers.items():
        verified=[]
        for x in p.get('fixed_items',[]):
            ident, data = identity(x['commit'],x['path'])
            assert (ident['mode'],ident['blob'],ident['bytes'],ident['sha256']) == (x['mode'],x['blob'],x['bytes'],x['sha256'])
            verified.append({'commit':ident['commit'],'path':ident['path'],'sha256':ident['sha256'],
                             'mode_blob_bytes_sha_match_contract':True})
        state = 'OPEN_AVAILABLE_NOT_SEMANTICALLY_RECEIVED'
        if pid == 'CRE-C':
            assert all(json.loads(git('show',x['commit']+':'+x['path']))['records']==[] for x in p['fixed_items'])
            state = 'OPEN_FIXED_PROVIDER_HAS_EMPTY_RECORDS'
        if pid == 'CRE-D':
            assert not p.get('fixed_items')
            state = 'OPEN_NO_COMPLETED_PROVIDER_IN_FIXED_CARRIER'
        provider_rows.append({'id':pid,'state':state,'fixed_items':verified,
             'contract_pointer':f'Sxx.complete.json#/providers_all_fields/id={pid}',
             'events':[e['id'] for _,e in es.values() if any(pid in routes[r]['provider_ids'] for r in e['current_formal_routes'])],
             'received_selected_record_ids':['WFS-004','WFS-005','WFS-025','WFS-028','WFS-031','WFS-032'] if pid=='WORLD' else ['WI04','WI18','WI19','WI21','WI22','WI26'] if pid=='WORLD-INTERPRETER' else [],
             'selected_record_boundary':'完整记录已读；只核其中五条指定链的源/条款，不导入整条记录全部副断言的独立通过。'})
    for route in routes.values():
        expected = route['current_formal_identity']
        actual, _ = identity(expected['commit'], expected['path'])
        assert all(actual[k] == expected[k] for k in ['path','mode','blob','bytes','sha256'])
    dump('interfaces.json', {'schema':'r8-recovery-legacy-g1-interfaces/v1',
         'carrier':'30cfed0996003b6ebf4b5c51cc04f31ca9255440',
         'route_identity_proof':'本范围全部current_formal_identity逐path/mode/blob/bytes/SHA与固定B8对象一致；完整原身份复用2d44dafe各Sxx.complete.json，不复制行政载荷。',
         'routes':[{k:x[k] for k in ['id','path','provider_ids']} for x in routes.values()],
         'providers':provider_rows,
         'five_world_chains':[
           {'id':'WORLD5-VEHICLE','source':'Scene_Map:72–101/121–134/165–230; command201:722–747; Player:575–616; Overworld:267–276; MapFactory:142–149',
            'formal':'WP11:64–73; WP12:184–196','fact':'201守卫排队后两场景以false消费而保留游泳；直接省参清游泳，骑行按目的地另查。跨图进入通知可上/下车，同图无该次通知。前序helper异常保留已到前缀。'},
           {'id':'WORLD5-STEP','source':'Player:141–193/416–555; Character:362–400/893–992; Overworld:172–218',
            'formal':'WP12:97–113; WP06:82–97','fact':'逻辑坐标/距离/条件离格先于动画完成；完成后合格玩家入口才全局步数加一并31位回绕。强制路线/解释器早退只发一般通知；不把距离零等同周期不进。'},
           {'id':'WORLD5-FOLLOW','source':'Follower:36–111/134–215; Factory:155–191; Scene_Map:72–101',
            'formal':'WP13:154–168; WP12:86–89','fact':'实际location入口与strict能力不同；同轴1/2格按许可尝试，其它非重合直接定位。临时through仅正常返回恢复；逐跟随者正常调用后才写持久记录，显式转移同时写runtime/记录。'},
           {'id':'WORLD5-ERROR','source':'Interpreter:138–206','formal':'WP13:104–109',
            'fact':'SystemExit及类名Reset原样抛，其他异常构造带上下文EventScriptError；正常表达式返回原值。异常包装不撤销前写入；错误格式化/宿主呈现本次未证明。'},
           {'id':'WORLD5-MISSINGMAP','source':'Scene_Map:56–101; StartGame:63–104; MapFactory:7–27; Map:39–74',
            'formal':'WP11:64–66/171; WP09:95–109; WP10:243–247',
            'fact':'显式缺图无选图恢复；有BGM/BGS时先读目标图而失败，皆无时可在重建后失败。读档仅magic/safesave重建路径捕ENOENT，调试选图/取消退出、非调试抛错；nil事件集合与空集合不同。'}],
         'world_chain_status':'SOURCE_STATIC_FINITE_FACTS_RECEIVED; 不能扩成全部S01事件/整个WORLD贡献接收。',
         'host':'NOT_EXECUTED', 'remaining_kind':'固定provider缺口与可得未接收均阻止完整事件签收；后者不是材料limit。'})
    dump('proposal-counters.json', {'schema':'r8-recovery-legacy-g1-counters/v1','new_required_formal_findings':0,
         'canonical_authority':'ROOT_ONLY','items':[
          {'id':'REC-G1-METADATA-01','events':['LM-E050','LM-E051','LM-E052'],
           'objection':'目标reader_judgment把WP48/49称为物品/AI。',
           'evidence':'B8 LM-L3161–3162/3173–3174/3186；对应当前正式路径wp48-ability-calculation-modifiers、wp49-ability-phase-triggers。',
           'counter':'最强NO_REQUIRED是它仅影响接收说明，不证明正式规格行为错；仍须按实际特性事实接收，不能按错误标签移给AI或物品primary。',
           'disposition':'LOCAL_RECEPTION_MEANING_CORRECTED_ORIGINAL_UNCHANGED'},
          {'id':'REC-G1-RANGE-01','objection':'目标catalog E-V2-WP11声称166–194，但同一身份文件仅190行。',
           'evidence':'whole-file mode/blob/bytes/SHA一致；actual physical_lines=190；本次输出9bcba8实际读到190并因191越界报错。',
           'counter':'没有191–194实际文本被漏读；属于范围声明错误，不能宣称不存在的四行已读，也不据此创建正式必修。',
           'disposition':'LOCAL_RANGE_CORRECTED_TO_166_190'},
          {'id':'R8-LMC-H001','disposition':'BOUNDED_DOCUMENTARY_NO_REQUIRED_REASON_RECEIVED_ROOT_DECISION_SEPARATE',
           'evidence':'固定counter-h001.md全文；B8 README/scope:1–11；目标proposals.json全文；依赖E066–072原文。',
           'reason':'父B21明确旧待审按原时点保留；不能仅因B8树中出现待审句重开N01。原反证完整行为接收/真实独立配置与未穷尽后继仍由其原证据承担，本次不冒签其物理输入或所有N01源。',
           'additional_votes':0}]})

    purposes = {
      'bounded-consumer-search.json':'全文读取；argv/stdout/positive_consumer/limitations只作有界导航依据，无全域不存在证明。',
      'build-evidence.py':'历史v1工具普通载荷；不执行、不以其产物生成授语义信用。业务判断以已读目标JSON/事件原文为准。',
      'complete-purpose-v2.py':'历史序列化工具普通载荷；不执行、不将脚本生成视图当阅读；选定事件语义以readset与已读原文为准。',
      'core-github-api.json':'全部commit/subtree字段为旧传输/身份记录；不认证本轮语义。',
      'core-readback-execution-attempt1.json':'全部command/exit/stdout/stderr为旧失败传输证据，保留原固定路径；403失败不删除。',
      'core-readback-execution-attempt2.json':'全部command/exit/stdout为旧成功传输，不能抹前次失败或转本轮行为执行。',
      'core-remote-readback.json':'全部顶层与files为旧mode/blob/bytes/SHA/集合回读；纯TOOL_VALIDATION。',
      'current-primary-contribution-routes.v2.json':'formal_routes选本60事件current_formal_routes并读取purpose/owner/provider用途；身份字段逐对象核对；providers相关固定项目仅按interfaces.json实际接收，其余未读不冒签。',
      'event-judgments.v2.tsv':'本60事件行的judgment与readset逐事件一致；已呈现读；其余事件在范围外。',
      'evidence-catalog.json':'全部items是身份/源与规范范围定位；范围不能充当实际已读。使用E-V2时实读并更正WP11越界；其它catalog业务对象未由身份接受。',
      'forward-mapping.json':'全部10条事实/前提/源/消费者/规范/排除字段已读；5条WORLD链另实读源/规范；5条N01仅贡献含义已读，不认证全部源。',
      'frozen-primary-structure.json':'units选本559物理行，offset/长度/SHA/physical_type核身份；UNREAD为原冻结时态，不是本次状态。其余结构范围外。',
      'gaps.json':'全文读取；各gap动作和剩余边界与新接收状态分列，不继承原unread=0为本次完成。',
      'identities.json':'全部身份、paths、preflight、configuration为原作者身份/环境声称；仅本次实查的B8/R/目标核真，未知实际配置不借用。',
      'interfaces.json':'全文读取；六接口的完整scope/facts/retained/not_transferred已读；本次是否签收单列。',
      'progress.json':'全部计数/状态/时点为原作者过程声称，不是本次语义信用；本次分母独立冻结。',
      'proposals.json':'全文读取完整H001所有字段；原反证未派发是其原时点；固定后继counter另读，最终裁决不代签。',
      'protection-after-core-push.json':'全部operations/scope为原保护工具记录，只核固定载荷身份，不当本环境全树保护或行为证明。',
      'protection-before-push.json':'全部operations/limits为原保护工具记录，不能外推当前环境。',
      'publication-operations.json':'全部operations是旧普通提交/推送工具记录，不复制为本次发布成果。',
      'publication.json':'全文读取；保留旧v1 incomplete与v2 purpose complete的阶段差异，以及403失败/后继成功。',
      'purpose-dispositions.json':'units选本559结构的所有字段：身份独立核验；内容/标题/布局原文均读。reason/successor/route逐项与事件一致且无例外；共同资格字段只读一次，不豁免混合段的任何业务文字。',
      'purpose-rules.v2.json':'全文读取；版本事件/当前批准/限制工作流三规则及not_a_blanket_exemption均已结合B21正面限定核对。',
      'read-chunks.json':'全部分片行界/字节为原阅读索引，不把脚本分片/原read记成本次实读。',
      'reading-ledger.json':'全部原primary/supplemental/added reads等为作者阅读声称；范围说明/旧truncation与v1纠正不等于本次已读，实际值只由本reading-ledger给出。',
      'remote-readback.py':'旧网络传输工具普通载荷，不执行；不含本次需要运行的行为合同。',
      'reverse-mapping.json':'完整当前规范反向接受尚未做，不借其full_read_files或clauses认证本次；相关有限WORLD条款由本次源/规范实读单列，其他必要条款OPEN。',
      'review.md':'全文读取；原用途结论、两链、精确handoff、H001、执行与限制全部作为提出者贡献接收，不能自批。',
      'semantic-purpose-freeze.v2.json':'units选本60事件所有语义字段和完整line_ids；原冻结时点与本次冻结分列，其余96事件不争主责。',
      'semantic-purpose-review.v2.json':'units选本60事件所有字段逐项读；依赖E066–072只读原文与judgment，不作本次主责或整事件接受。',
      'validate-evidence.py':'旧机械校验工具普通载荷，不执行；旧exit0不认证业务。',
      'validation.json':'全部checks/command/stdout/stderr是旧机械校验记录；不转成新行为执行。',
      'world-interface-reception.v2.json':'两fixed_contributions全部12记录所有字段已读，逐pointer与30cfed0固定原件精确相等；只给本次明确五链的有限源/消费者信用。'}
    assert set(purposes)=={f['path'].rsplit('/',1)[1] for f in receipt['files']}
    exact_fields = {}
    for name, purpose in purposes.items():
        if name.endswith('.json'):
            value = json.loads((target_dir/name).read_text())
            exact_fields[name] = list(value) if isinstance(value,dict) else ['/*']
        elif name.endswith('.tsv'):
            exact_fields[name] = list(next(csv.DictReader((target_dir/name).open(),delimiter='\t')))
        else:
            exact_fields[name] = ['whole_file']
    dump('field-purposes.json', {'schema':'r8-recovery-legacy-g1-field-purposes/v1','files':purposes,'exact_top_level_fields':exact_fields,
         'not_read':'typed身份/原作者阅读声称不等于当前语义接受；有未接的有效业务值继续OPEN，见interfaces/reception-ledger。',
         'raw_inputs':'已在本目录自有.cache独立恢复后核验；不提交行政副本；固定目标Git对象/33路径及identity proof可恢复。'})
    print(json.dumps({'events':60,'paragraphs':381,'physical_lines':559,'purpose_unread':0,
          'complete_event_receptions':0,'status':'INCOMPLETE','files_with_exact_purpose':len(purposes)},ensure_ascii=False))

if __name__ == '__main__':
    main()
