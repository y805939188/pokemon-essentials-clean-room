#!/usr/bin/env python3
"""Compose qualified contracts and bind actual published C35. No review or update."""
import copy
import hashlib
import json
from collections import Counter
from pathlib import Path
import subprocess

REPO = Path('/workspace/pokemon-essentials-clean-room')
RRREL = 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
RR = REPO / RRREL
OUT = RR / 'handoff'
BASE = RR / 'tasks/handoff_final_five_root_deltas'
E = BASE / 'effective39'
ORIGIN = '5caff3bd1a1b062b48b7eda46777a614921946f3'
OLD = RR / f'evidence/external-recovered/handoff_preparation_cloud/{ORIGIN}'
C35 = '2460370f1e410bd49cc29e377b89662838aed2b3'
WTREE = 'd43c425a3cfed29014f5cdfb94a3f8d947508d5f'
RTREE = '2e0487366deed90fdf34c64d47b372ff94530f10'
STATE = 'READY_FOR_USER_MANUAL_UPDATE'
ROLE = '/root/handoff_final_five_root_deltas'

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])

def load(p):
    return json.loads(Path(p).read_text())

def core(n):
    return json.loads(git('show', f'{C35}:{RRREL}/{n}'))

def blob(b):
    return hashlib.sha1(f'blob {len(b)}\0'.encode() + b).hexdigest()

TREE = {}
for row in git('ls-tree', '-rz', C35, '--', RRREL).split(b'\0'):
    if row:
        left, path = row.split(b'\t', 1)
        mode, kind, oid = left.decode().split()
        TREE[path.decode()] = (mode, oid)
assert git('rev-parse', C35+'^{tree}').decode().strip() == WTREE
assert git('rev-parse', C35+':'+RRREL).decode().strip() == RTREE

def identity(p, purpose='', published=True):
    p = Path(p)
    if not p.is_absolute():
        p = RR / p
    rel = p.relative_to(REPO).as_posix()
    if published:
        mode, oid = TREE[rel]
        b = git('show', f'{C35}:{rel}')
        assert blob(b) == oid
    else:
        b = p.read_bytes()
        mode, oid = ('100755' if p.stat().st_mode & 0o111 else '100644'), blob(b)
    d = dict(repo=str(REPO), commit=C35 if published else None,
             workspace_tree=WTREE if published else None,
             report_tree=RTREE if published else None,
             path=rel, mode=mode, bytes=len(b), sha256=hashlib.sha256(b).hexdigest(), blob=oid,
             type='REPORT_OR_QUALIFIED_EVIDENCE', purpose=purpose)
    if not published:
        d['publication_binding'] = 'POST_C35_SUCCESSOR_PAYLOAD; actual enclosing commit/tree bound externally after ordinary publication'
    return d

def dump(n, x):
    p = OUT / n
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2)+'\n')

def write(n, s):
    p = OUT / n
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s)

def guard():
    paths = []
    for parent in [BASE, E]:
        m = load(parent/'delivery-manifest.json')
        paths += [(REPO / r['path'], r) for r in m['payloads']]
        paths.append((parent/'delivery-manifest.json', identity(parent/'delivery-manifest.json')))
    for name in ['prior-freeze-v1','prior-freeze-v2']:
        ix = E/name/'archive-index.json'
        ar = load(ix)
        paths += [(REPO / r['archived_path'], r) for r in ar['files']]
        paths.append((ix, identity(ix)))
    verified = {}
    for p, expected in paths:
        b = p.read_bytes()
        assert len(b) == expected['bytes'] and hashlib.sha256(b).hexdigest() == expected['sha256'] and blob(b) == expected['blob'], str(p)
        assert p.is_file() and not p.is_symlink() and not (p.stat().st_mode & 0o111)
        verified[p.relative_to(REPO).as_posix()] = {k:expected[k] for k in ['mode','bytes','sha256','blob']}
    assert len(verified) == 106
    return verified

protected = guard()
cm = core('core-manifest.json')
findings = core('findings.json')
summary = core('summary.json')
history = core('adjudication/root-final-history-and-canonical-reception.v1.json')
registry = core('adjudication/root-primary-task-final-registry.final.json')
typed = core('coverage/final-typed-denominators.json')
wp = core('coverage/wp-final-coverage.json')
execution = core('coverage/final-execution-classification.json')
em = load(E/'handoff/cloud-eighth-update-handoff-manifest.json')
old33 = load(OLD/'handoff/contracts.zh.json')
new5 = load(BASE/'handoff/contracts.delta.zh.json')['records']
f05 = load(E/'handoff/contracts.f05.zh.json')
root_records = findings['records']
canonical = {r['id']:r for r in history['canonical_records']}
base_batches = load(E/'handoff/batch-assignment.json')['batches']

CORE = dict(commit=C35, workspace_tree=WTREE, report_tree=RTREE,
            status='FROZEN_COMMITTED_PUSHED_FRESH_REMOTE_VERIFIED')
PUBLICATION = dict(enclosing_handoff_commit=None, workspace_tree=None, report_tree=None,
                   status='SUCCESSOR_PUBLICATION_EXTERNAL_BINDING_REQUIRED',
                   rule='本包不包含自身未来hash；root后继普通commit/push及完整远端回读后由外部真实发布入口绑定。C35是语义core，不是本新handoff的enclosing commit。')
proof = load(RR/'publication/root-actual-semantic-core-binding.v1.json')
assert proof['core']['commit'] == C35 and proof['verified_report_files'] == 25239
assert proof['transport_events'] == {'expected_target_absent_cat_file_probes_exit128':2,'successful_recorded_operations_exit0':12,'unexpected_nonzero':0}
proof_ids = [identity('publication/r8-final-semantic-core-readback-35.json', 'C35之后生成的25239逐文件远端传输/116恢复身份；/files及/compressed_originals为全量精确表', False),
             identity('publication/root-actual-semantic-core-binding.v1.json','root实际接收C35远端传输及51核心权威精确匹配；不是新语义审查',False)]

# Replace preparation-state administration in the operative document. Historical
# source/decision snapshots remain immutable at their exact C35 locators.
REPLACEMENTS = {
 'BOUNDED_PREPARATION_COMPLETE_PENDING_ROOT_CORE_FREEZE': STATE,
 'READY_PENDING_ROOT_CORE_FREEZE': STATE,
 'PROVISIONAL_GLOBAL_HISTORY_DEDUP_OPEN': 'ROOT_FINAL_CANONICAL_HISTORY_ACCEPTED',
 'PROVISIONAL_OPTIONAL_QUALIFICATION_HISTORY_DEDUP_OPEN': 'ROOT_FINAL_OPTIONAL_CANONICAL_HISTORY_ACCEPTED',
 'CLASSIFIED_BOUNDED_SCOPE_PENDING_GLOBAL_HISTORY_AND_INTERFACE_RECEPTION': 'ROOT_FINAL_CURRENT_HISTORY_AND_INTERFACE_RECEPTION_COMPLETE',
 'PENDING_ROOT_CORE_FREEZE': 'CORE_C35_FROZEN_REMOTE_VERIFIED',
 'OPTIONAL_ONLY_PENDING_EXPLICIT_POLICY_CHOICE_AND_FINAL_BATCH_FREEZE': 'OPTIONAL_UNSELECTED_USER_CHOICE_REQUIRED',
 'PROVISIONAL_OPTIONAL_HISTORY_DEDUP_OPEN': 'ROOT_FINAL_OPTIONAL_HISTORY_ACCEPTED',
 'PROVISIONAL_REQUIRED_HISTORY_DEDUP_OPEN': 'ROOT_FINAL_REQUIRED_HISTORY_ACCEPTED',
 'exact historical root ID reception is OPEN under root/history owner.': 'exact historical root ID reception is complete under the C35 final history authority.',
 'R6/R7具体issue-key和原未知资格由root/history另接收，当前OPEN；': 'R6/R7具体issue-key和原未知资格按C35最终历史接收保留；',
 '历史全量去重仍OPEN。': '',
 '全量历史去重仍OPEN。': '',
 '全量历史去重与接口仍OPEN。': '',
 '临时canonical；全局历史根因/等价可选/原ELR接口仍OPEN，如已有等价根则alias归并，不重开旧27或重复计根。广原proposal仅此有限子facet采用，其它policy仍OPEN。': '最终canonical及历史关系按C35完整根接收；原27项关闭保持，仅采用本有限子facet。独立视觉policy保持UNSELECTED。',
 '全球历史等价仍OPEN。': '当前必要历史等价关系已由C35最终根接收。',
 'Finite complete36 resource caller methods now read and original UI source facts received. Full broader formal and original R6/R7 canonical roots are still not fully received; no full-global negative claim.': 'The finite complete36 resource caller methods and original UI source facts retain their original scope. Broader formal and original R6/R7 canonical relationships are now received by the C35 final authority; this local negative search is not a universal runtime claim.',
 '没有宣称所有任意扩展脚本/插件无验证；默认附带数据未见负概率，根因是否已在其它域/历史处理尚未接收。': '没有宣称所有任意扩展脚本/插件无验证；默认附带数据未见负概率。其它域/历史关系按C35最终canonical及历史接收资格处理。',
 '不同于FAC001 trainer scalar、W04 skip prefix、CD003 recording-vs-playback storage、CP01 victory mark、CP002 faint audio；38当前既有entries保留，不增同根票。早期历史精确归并继续原owner。': '不同于FAC001 trainer scalar、W04 skip prefix、CD003 recording-vs-playback storage、CP01 victory mark、CP002 faint audio；当前39修订义务entries保留。按C35最终历史资格，这是已知WP76-R12关闭事实上的未选WP58 attribution facet，保R6-DX-DEBUG-004/GIR-FD82-B029，不新增历史根或独立票。',
 'actual different nonproposer full counterreview pending': 'actual different nonproposer counterreview accepted by C35 root final reception; future edit acceptance still requires an actual non-author reviewer',
 '若已有同根澄清则alias并入': 'canonical关系按C35最终历史接收',
 '若已有同根精度项则alias去重': 'canonical关系按C35最终历史接收',
 '若全历史具名现行同根存在则alias去重': 'canonical关系按C35最终历史接收',
 '全局历史dedup/等价资格facet仍OPEN；若已有同根可选修订则alias合并，不重复计根。原34031查询与异议不改写。': '最终历史关系按C35 canonical记录接收；原34031查询、异议与原生成时点资格保留于只读审计载荷。',
 '全局task/core未完成，本记录不授权update。': 'C35语义core及当前必要历史/消费者已完整接收；用户另行手动启动整改。',
 'root core及全历史/接口接收冻结，后继真实enclosing commit与core绑定，再由用户手动启动；optional须另行选择。': 'C35语义core及全历史/必要接口已冻结接收；本handoff后继真实发布绑定后由用户手动启动；optional须另行选择。',
}

def clean(x):
    if isinstance(x, list): return [clean(v) for v in x]
    if isinstance(x, dict):
        y = {k:clean(v) for k,v in x.items()}
        for k in ['global_task_core','global_core']:
            if k in y: y[k] = 'C35_FROZEN_CURRENT_NECESSARY_RECEPTIONS_COMPLETE'
        if 'whole_review_complete' in y: y['whole_review_complete'] = True
        # Exact current recovery is a second identity, never a fabricated origin.
        if isinstance(y.get('path'),str) and ('sha256' in y or 'blob' in y):
            path = y['path']
            rel = path if path.startswith(RRREL+'/') else RRREL+'/'+path
            if rel in TREE:
                actual = identity(REPO/rel, 'C35当前可得精确载荷；原来源身份按original_provenance保留')
                same = all(y.get(k,actual[k]) == actual[k] for k in ['bytes','sha256','blob','mode'])
                if same and y.get('commit') is None:
                    for k in ['repo','commit','workspace_tree','report_tree']:
                        y[k] = actual[k]
                    if y.get('tree') is None: y['tree'] = WTREE
                    y.pop('commit_binding',None)
                elif same and y.get('commit') != C35:
                    y['current_recovered_at'] = actual
        return y
    if isinstance(x,str):
        for a,b in REPLACEMENTS.items(): x=x.replace(a,b)
        return x
    return x

records = []
admin_deltas = []
def changed_existing(a,b,p=''):
    if isinstance(a,dict) and isinstance(b,dict):
        out=[]
        for k in a:
            if k in b: out+=changed_existing(a[k],b[k],p+'/'+k)
        return out
    if isinstance(a,list) and isinstance(b,list) and len(a)==len(b):
        out=[]
        for j,(u,v) in enumerate(zip(a,b)): out+=changed_existing(u,v,p+'/'+str(j))
        return out
    return [] if a==b else [dict(pointer=p,original=a,final=b)]
for i,r in enumerate(root_records):
    rid = r['id']; c = canonical[rid]
    if i < 33:
        original = old33[i]
        contract = clean(original['seven_groups'])
        one = contract['1_身份与结论']
        one['canonical_status'] = 'ROOT_FINAL_CANONICAL_HISTORY_ACCEPTED'
        one['canonical_root'] = c['canonical_root']; one['facet'] = c['facet']
        one['historical_relation'] = c['historical_relation']
        contract['7_依赖接收与关闭']['blocking'] = ['用户另行手动启动', '真实非作者候选及实际整合全文/累计保留接收', '唯一正式接收及独立关闭登记']
        if r['classification']=='optional':
            contract['7_依赖接收与关闭']['blocking'].insert(0,'用户明确选择本optional；未选择不阻required')
        contract['7_依赖接收与关闭']['excluded_claims'] = [s for s in contract['7_依赖接收与关闭']['excluded_claims'] if s!='全局review完成']
        origin = dict(commit=ORIGIN, original_path=f'{RRREL}/tasks/handoff_preparation_cloud/handoff/contracts.zh.json', pointer=f'/{i}', recovered_at=identity(OLD/'handoff/contracts.zh.json','原33完整合同，原来源5caff与C35恢复位置分别绑定'))
    else:
        original = new5[i-33] if i < 38 else f05
        contract = clean(original['complete_contract'])
        # Original adjudication text is immutable evidence, current closure gate
        # is provided below for every record rather than inherited early gates.
        origin = dict(original_full_contract=identity(BASE/'handoff/contracts.delta.zh.json' if i<38 else E/'handoff/contracts.f05.zh.json','已合格完整合同原字节'), pointer=f'/records/{i-33}/complete_contract' if i<38 else '/complete_contract')
    batch = next(b['id'] for b in base_batches if rid in b['required_ids']+b['optional_ids_if_later_selected'])
    original_contract=original['seven_groups'] if i<33 else original['complete_contract']
    for d in changed_existing(original_contract,contract):
        admin_deltas.append(dict(id=rid,**d,kind='CURRENT_ADMINISTRATIVE_STATUS_OR_EXACT_RECOVERY_IDENTITY',
          original_audit_source=origin,
          rationale='C35已合格最终接收及实际身份绑定；行为前提、反例、规则、验收与正确scope保留。'))
    records.append(dict(id=rid,classification=r['classification'],severity=r.get('severity'),
       selection='UNSELECTED' if r['classification']=='optional' else 'REQUIRED_NOT_STARTED',
       canonical_root=c['canonical_root'],facet=c['facet'],historical_relation=c['historical_relation'],
       root_reason=clean(r['root_reason']),current_history_and_consumer_conditions=r['current_necessary_history_and_consumer_conditions'],
       full_contract=contract,full_contract_original_provenance=origin,
       root_adjudication=dict(path='findings.json',commit=C35,report_tree=RTREE,pointer=f'/records/{i}'),
       required_primary_batch=batch if r['classification']=='required' else None,
       conditional_batch_if_user_selects=batch if r['classification']=='optional' else None,
       operation=dict(status=STATE, direct_semantic_required_ids=[],transitive_semantic_required_ids=[],
          candidate_writer=batch, actual_target_writer='R8-INTEGRATOR',
          author_entry=f'R8-A-{batch}',reviewer_entry=f'R8-R-{batch}',
          roles=em['common_roles'],
          release_gate='真实后继发布绑定和用户另行手动启动；optional另需用户明确选择。C35当前必要历史/接口接收已完成。',
          acceptance_gates=['candidate PASS','actual integrated PASS','ACCEPTED','CLOSED'],
          independent_acceptance='实际非作者完整读取原输入、候选及受影响实际整合全文/累计保留；本人不能最终签收本人改动。',
          vectors='NOT_EXECUTED',update_started=False)))

dump('contracts.zh.json',dict(schema='r8-final-complete-39-operative-contracts/v1',status=STATE,
    classification_authority=identity('findings.json','C35唯一最终39分类/严重度与完整根合同权威'),
    current_history_authority=identity('adjudication/root-final-history-and-canonical-reception.v1.json','全部39历史关系与全必要历史接收'),
    records=records,record_count=39,new_historical_roots_claimed=False,update_started=False))
dump('administrative-field-deltas.json',dict(schema='r8-qualified-contract-final-administrative-normalization/v1',
 scope='仅最终当前态canonical/history/core/whole-review资格、未来关闭门和精确现可得恢复身份；不是新语义审查或新裁决。',
 original_source_bytes_preserved=True,field_deltas=admin_deltas,field_delta_count=len(admin_deltas),
 new_contexts=0,new_independent_votes=0,new_source_FULL_credit=0,new_business_runs=0,update_started=False))

policies = clean(load(E/'handoff/policy-and-preservation.json'))
policies['status']=STATE
policies['mandatory_accepted_fact_companions']='handoff/accepted-facts-and-mandatory-companions.json'
dump('policy-and-preservation.json',policies)
facts=clean(load(E/'handoff/accepted-facts-and-mandatory-companions.json')); facts['status']=STATE
facts['final_root_acceptance']=identity('adjudication/root-final-history-and-canonical-reception.v1.json','完整CREB来源纠正和最终消费者资格均已接收')
dump('accepted-facts-and-mandatory-companions.json',facts)
hq=clean(load(E/'handoff/history-qualifications.json')); hq['R8_core']=CORE
hq['current_final_history_authority']=identity('adjudication/root-final-history-and-canonical-reception.v1.json','当前全历史0未接收；旧局部生成时点保持原资格')
hq['task_contexts']=summary['task_independence']
hq['population_rule']='42是R7唯一任务ID；12实际审者且U04/U05共享context，continuation+0；本轮29主责任务、125已知context不同口径。'
dump('history-qualifications.json',hq)

batches=[]
for prior in base_batches:
    b=copy.deepcopy(prior)
    for k in ['inherited_effective38_prompt','inherited_complete_prompt','inherited_complete_readset','current_history_qualifications','current_negative_dispositions','mandatory_accepted_fact_companions','launch_methods','additional_contract_pointer','input_commit_rule','inherited_semantic_scope']:
        b.pop(k,None)
    b=clean(b); bid=b['id']
    b.update(input_contract_commit=C35,R8_core=CORE,state='PLANNED_NOT_STARTED',
      current_launch_blocker='用户尚未手动启动；本新handoff由root后继真实发布绑定',
      enclosing_handoff_publication=PUBLICATION,
      complete_contracts=[dict(id=rid,path='handoff/contracts.zh.json',pointer=f'/records/{next(i for i,x in enumerate(records) if x["id"]==rid)}') for rid in b['required_ids']+b['optional_ids_if_later_selected']],
      complete_original_readset=identity(OLD/f'handoff/batches/{bid}/readset.json','原完整必要读集；固定源/规格身份和原读范围继续有效'),
      complete_original_prompt_audit=identity(OLD/f'handoff/batches/{bid}/prompt.md','原完整行为/读写/保留合同只读审计；执行以本最终态prompt/全合同为准'),
      complete_delta_readset=identity(BASE/'handoff/source-spec-readset.delta.json','五新增根完整固定source/spec单位及必要完整单位'),
      mandatory_accepted_fact_companions='handoff/accepted-facts-and-mandatory-companions.json',
      current_history_qualifications='handoff/history-qualifications.json',
      current_negative_dispositions='handoff/policy-and-preservation.json', launch_methods='handoff/launch-methods.json',
      author_prompt=f'handoff/batches/{bid}/prompt.md',reviewer_prompt=f'handoff/batches/{bid}/reviewer-prompt.md',
      actual_formal_writer='R8-INTEGRATOR')
    batches.append(b)
    readset=dict(schema='r8-final-batch-complete-readset/v1',id=bid,R8_core=CORE,B8=em['B8'],R=em['R'],
      inherited_complete_readset=b['complete_original_readset'],
      inherited_contents=clean(load(OLD/f'handoff/batches/{bid}/readset.json')),
      delta_complete_readset=b['complete_delta_readset'],
      delta_contents=clean(load(BASE/'handoff/source-spec-readset.delta.json')) if b['additional_contract_ids'] or b['optional_additional_contract_ids'] else '本批无新增五根必修/可选单位；原完整读集有效。',
      contracts=b['complete_contracts'], mandatory_companions=['handoff/accepted-facts-and-mandatory-companions.json','handoff/history-qualifications.json','handoff/policy-and-preservation.json'],
      future_full_read_requirement='作者/非作者均完整读取本批全合同、全部相关源/规格单元、前提、控制和最终受影响整文件；身份或原审者FULL不能代替本人实读。',update_started=False)
    if bid=='R8-U06': readset['conditional_F05_readset']=clean(load(E/'handoff/readset.f05.json'))
    readset['inherited_contents']['R8_core']=CORE
    readset['inherited_contents']['contract_commit']=C35
    readset['inherited_contents']['records']=b['complete_contracts']
    dump(f'batches/{bid}/readset.json',readset)

dump('batch-assignment.json',dict(schema='r8-final-nine-batches/v1',status=STATE,R8_core=CORE,batches=batches,
    batch_count=9,one_required_one_primary=True,optional_selected_count=0,update_started=False))
dg=clean(load(E/'handoff/dependency-graph.json'));dg.update(R8_core=CORE,status=STATE,
 common_release='C35已完整冻结及远端核验；root以真实后继绑定本handoff后，用户另行手动启动。',
 first_wave_after_common_release_count=9, currently_startable=[],currently_startable_count=0)
dump('dependency-graph.json',dg)
fg=clean(load(E/'handoff/file-conflict-graph.json'));fg['status']=STATE
dump('file-conflict-graph.json',fg)

# All source/spec identities retain their original fixed commits. Full report
# evidence identities are not recopied: the exact post-core proof has 25239 rows.
auth=[]
for a in cm['core_authority_payloads']:
    d=identity(a['path'],a.get('purpose','最终当前语义权威'))
    assert all(d[k]==a[k] for k in ['mode','bytes','sha256','blob'])
    auth.append(d)
extras=['core-manifest.json','final-report.md','summary.json','findings.json',
 'coverage/final-typed-denominators.json','coverage/wp-final-coverage.json',
 'coverage/final-execution-classification.json','publication/compressed-artifacts.json',
 'adjudication/root-primary-task-final-registry.final.json',
 'adjudication/root-handoff-39-preparation-reception.final.json',
 'adjudication/root-final-history-and-canonical-reception.v1.json',
 'adjudication/coverage-task-final-readset-identity-purpose.tsv',
 'tasks/com_move/integration-membership/final-current/paths-563.json',
 'inputs/eighth-global-review-prompt.md','inputs/review-SKILL.md']
inputs=dict(schema='r8-final-exact-input-payloads/v1',R8_core=CORE,
 source_and_formal=cm['input_file_identities'],source_and_formal_count=563,
 core_authority_payloads=auth,core_authority_count=51,
 additional_binding_authorities=[identity(n,'完整身份/覆盖/有效补充/历史/执行/报告权威') for n in extras],
 complete_typed_scope=typed, complete_WP_coverage=wp,
 current_effective_supplementary_identity_purpose_table=identity('adjudication/coverage-task-final-readset-identity-purpose.tsv','301载荷/289异SHA/274当前语义及15用途处置，表与根完整接收共同适用'),
 all_report_evidence_identities=dict(proof=proof_ids[0],json_pointer='/files',file_count=25239,bytes=2423831391,
  tree=RTREE,commit=C35,recovery='git show <actual C35>:<exact row path>; modes/blobs compare actual C35 tree. /files every row contains path/mode/blob/bytes/SHA256. No new semantic reading credit.'),
 compressed_originals=dict(container_manifest=identity('publication/compressed-artifacts.json','116无损恢复对象原path/mode/bytes/SHA/blob及恢复方法'),proof=proof_ids[0],json_pointer='/compressed_originals',count=116,restored_bytes=1204403716,
  rule='只按原manifest恢复已理解资料，不执行被恢复程序。'),
 post_core_publication_evidence=proof_ids,
 inherited_qualified_complete_manifest=dict(original_commit=ORIGIN,original_path=f'{RRREL}/tasks/handoff_preparation_cloud/handoff/cloud-eighth-update-handoff-manifest.json',recovered_at=identity(OLD/'handoff/cloud-eighth-update-handoff-manifest.json','原完整源/规格/有效补充/报告证据及历史恢复身份；原来源不是C35')),
 local_mapping=dict(project=str(REPO),reference='/workspace/pokemon-essentials',original_user_project='/Users/dingshinn/Desktop/pokemon-framework-reference',report_root=RRREL),
 purpose_rule='身份/结构覆盖与语义实读分别登记；完整原审者与有效用途留在被绑定的最终台账，本整合source FULL信用0。',update_started=False)
dump('input-payloads.json',inputs)

launch=clean(load(E/'handoff/launch-methods.json'))
launch['schema']='r8-final-evidence-backed-manual-launch/v1'
launch['launch_gate']='仅用户未来另行手动派发；C35已冻结远端VERIFIED，本新handoff使用root后继真实发布绑定；optional需另选。本准备不调用未来任务。'
for name,effort,prefix in [('author_example','xhigh','R8-A'),('nonauthor_reviewer_example','ultra','R8-R')]:
    msg=(f'仅用户未来另行手动启动后执行。逻辑入口{prefix}-R8-U06；项目{REPO}，只读参考/workspace/pokemon-essentials。'
       f'完整读取{OUT}/batches/R8-U06/'+('prompt.md' if effort=='xhigh' else 'reviewer-prompt.md')+f'及{OUT}/cloud-eighth-update-handoff-manifest.json、{OUT}/batches/R8-U06/readset.json与全部对应完整合同/必要伴件。'
       f'固定语义core {C35}，workspace tree {WTREE}，RR tree {RTREE}；本handoff实际后继发布身份由外部真实绑定提供，不能编造。'
       +('作者只在本批独占候选镜像/证据目录写；' if effort=='xhigh' else '审者只写自己独占的review证据目录，不改作者候选或正式文件；')+
       '正式目标由R8-INTEGRATOR唯一写。F05未选不写WP58；WP67-A候选唯一writer处理COM同步与faintaudio，CP01未选不改。'
       f'请求gpt-6.1-sol/{effort}/default normal/Fast off，实际无权威echo逐字段UNVERIFIED。'
       '另冻结实际候选/整合输入；作者不能最终接收本人改动，非作者完整核受影响全文/累计保留，四门分别登记。保存实际返回task ID与独立实读/进度/命令I/O/manifest。')
    launch['cloud'][name]['arguments']['message']=msg
launch['CLI']['stdin_prompt']=RRREL+'/handoff/batches/R8-U06/prompt.md'
dump('launch-methods.json',launch)

COMMON = f'''# 第八轮手动整改完整执行合同

当前工作仅修订实现无关规格和必要追溯。用户另行手动启动后，按本文的唯一主批次完成29项必修，每项只计一次。10项optional及1项独立视觉policy均UNSELECTED，只有用户明确选择对应项才进入写集。状态UPDATE_NOT_STARTED；未来整改启动0。

固定B8 `{em['B8']['commit']}`，workspace tree `{em['B8']['tree']}`，formal tree `{em['B8']['formal_tree']}`。只读R `{em['R']['commit']}` / tree `{em['R']['tree']}`。项目 `{REPO}`，参考 `/workspace/pokemon-essentials`，报告 `{RRREL}`。

实际R8语义core commit `{C35}`，workspace tree `{WTREE}`，RR subtree `{RTREE}`，已普通commit/push并完整fresh远端VERIFIED。core-manifest为563500B/SHA256 d2650e97c5e8e3d2ed8f6c71de810fd7077036ebb1ef7cd5e5c31fa4dd09f7b8。C35之后生成的回读proof和root binding在input-payloads.json分别给精确path/mode/bytes/SHA/blob，其真实enclosing属于后继发布；它们不冒称C35成员。本新handoff enclosing commit/tree留null，root实际后继发布与外部绑定收口后核验，不能填未来hash。

全量合同语义审查及当前必要消费者/历史接收已完成：563固定源/正式文件=432R（44,906,485B）+131F（4,364,108B，111正文/17catalog/3shared）；87WP行=84内容+3阶段，18领域、113feature groups、395规划边、9crosscut。当前有效补充301载荷路径/289异SHA/274当前语义及15严格或混合用途处置，分母不可相加冒充统一atom。最终29主责任务、原9外部任务9/9全部root task-final接收；源/正式clause/必要consumer/history未读或未接收0。29逻辑primary不等于29实际context；已知累计125实际context=本地含root61+外部64，最终整合新增0。R7的42是唯一任务ID、12实际reviewer，U04/U05共享及续turn+0保持。

最终39是当前修订义务entries：29required（2P2、27P3）+10optional；独立14有限NO_REQUIRED、4binary负例、1视觉policy另列。UI003经GR7-M13-002 alias到R6-UI-PARTY-003；ELR为R6-D-LZ-002 parent上的新Slot consumer precision facet，保旧四family关闭；F05是在已知WP76-R12关闭事实上的未选WP58 attribution facet，保R6-DX-DEBUG-004/GIR-FD82-B029资格。这些不是39个新历史根。

行为证据分型严格保留：实际7个数学/有限证书过程和1个环境探针；旧PBS摘要1的原ID、I/O、exit、OS UTC仍UNVERIFIED/alias_UNRESOLVED，非阻塞且不另计第8数学过程。SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION分开；参考Ruby/游戏/原生、真实保存回放、像素声音观察信用0。已有7+1的真实I/O及资格由coverage/final-execution-classification.json绑定；本handoff准备新增业务运行0。材料/宿主/opaque limits仍限原范围，可得未读不改标limit。语义审查完成不等于B8合规PASS，也不等于运行等价。

先完整读取AGENTS.md、inputs/review-SKILL.md、本文、同目录manifest、contracts.zh.json中所属ID的完整合同、所属完整readset及对应accepted-facts/history/policy伴件。按clean-document-revision直接形成正确最终文字；不抄源码、逐行转译、不开发新框架。原始完整根裁决和审计链按C35精确路径只读恢复。原33合同来源5caff的original commit/path与C35恢复路径双身份保留，不能把所有历史事实来源改成C35。

候选作者请求gpt-6.1-sol/xhigh，实际非作者审者请求gpt-6.1-sol/ultra，均default普速/Fast off；actual model/effort/tier/speed/Fast无权威echo逐项UNVERIFIED。原作者不能独立最终验收本人改动，角色名/同context续turn不产生独立性。每批作者只写其独占candidate mirror和证据；正式目标、共享整文件、planning/audit及公共台账仅R8-INTEGRATOR写。保留R、B8、main、原tag、旧报告、原接受/关闭回执和其它worktree。候选PASS、实际整合PASS、ACCEPTED、CLOSED四门分别登记；actual输入必须真实冻结，非作者完整核受影响整文件及累计保留，不能以候选PASS代替实际接收。

九批语义编辑DAG直接/传递边均0；共同发布/用户启动门满足后第一波9批可独立准备，实际并发服从工具slots，当前已启动0。共享写冲突通过整合单写者及逐贡献接收解决，不新增语义依赖。独立policy仅阻塞实际选择并依赖该policy的范围，未选optional不阻required关闭。

WP67-A由U06唯一候选writer接收原COM同步与faintaudio必修；CP01独立optional未选。F05仅用户选择时由U06候选writer改WP58 §5.1 L105相关短语，WP76/RC-W11正确只读，保RC29原ID/计数，当前WP58不进入必修candidate/actual写集。WP64与共享Creature catalog由U09候选贡献、R8-INTEGRATOR正式整文件唯一writer，完整保EG/EN/FC/TT/MG、Factory/Triad/E，32条计数/原ID/别名前缀。MG32精确输入为删空名字后RETURN并确认停止；邻近已有非空名ESCAPE成功不停止；不可把两者混同。

CREB对应facet必须同时使用accepted-facts-and-mandatory-companions.json完整根资格与12源单位伴件。rawfalse存储、nil清除、typed getter参数验证、Mail先赋引用再getter自清/失败前缀、pinch check_gluttony=false及普通有效ID/nil输入域各按原完整前提；不扩普通输入域，不增加正式根。WP31保64注册身份/52手工意义组、None/Level/guard/首成功及BE01–37。完整controls、read/write、preserve、acceptance及历史/独立裁决链均在下列逐项合同，不能以概要代替。

''' 

def contract_text(rs):
    return '\n\n'.join('## '+r['id']+' — '+r['classification']+' / '+str(r['severity'])+'\n\n```json\n'+json.dumps(r,ensure_ascii=False,indent=2)+'\n```' for r in rs)+'\n'

table='| 批次 | 必修 | 未选optional |\n| --- | --- | --- |\n'+''.join('| '+b['id']+' '+b['title']+' | '+', '.join(b['required_ids'])+' | '+', '.join(b['optional_ids_if_later_selected'])+' |\n' for b in batches)
launchtext='''## 用户未来手动启动入口与日志

本环境实际成功入口为云平台collaboration.spawn_agent；launch-methods.json给作者xhigh/真实非作者ultra的完整arguments、逻辑ID与实际返回ID映射方法。每批的prompt.md与reviewer-prompt.md是独立完整入口，readset.json为完整读集。保存实际返回canonical task名/平台ID，使用collaboration.list_agents、send_message、wait_agent及平台任务卡查看可见状态；同context followup不增审者。每未来任务在独占目录记录progress、reading-ledger、commands.jsonl及真实stdout/stderr/exit/UTC、候选manifest；记录实际存在后可tail，不伪造私有平台流。

CLI备用仅语法已实际核验：codex-cli 0.159.0-alpha.3与exec --help均exit0；-C、-m、-s workspace-write、--json、-o、stdin“-”可见。原实际启动失败为readonly filesystem使in-process app-server client初始化失败，并非flag错误。完整argv、stdin及日志路径见launch-methods.json；help不证明授权、模型任务或业务成功，未核具体effort/tier配置key不编造。Desktop本云环境不可用。所有未来手动任务启动仍0。

'''
launchtext+='云作者完整API模板（仅未来用户手动调用）：\n\n```json\n'+json.dumps(launch['cloud']['author_example'],ensure_ascii=False,indent=2)+'\n```\n\n实际非作者独立API模板：\n\n```json\n'+json.dumps(launch['cloud']['nonauthor_reviewer_example'],ensure_ascii=False,indent=2)+'\n```\n\nCLI备用完整argv：\n\n```json\n'+json.dumps(launch['CLI']['example_argv_only'],ensure_ascii=False,indent=2)+'\n```\n\n完整prompt由stdin提供，stdout JSONL、stderr、真实exit及last-message分别保存，具体路径见launch-methods.json。\n\n'
contract_id=identity(OUT/'contracts.zh.json','全部39条完整规范合同唯一正文载荷',False)
record_table='| 稳定ID | 分类 / 严重度 | 唯一主批次或条件批次 | 完整合同JSON pointer |\n| --- | --- | --- | --- |\n'+''.join('| '+r['id']+' | '+r['classification']+' / '+str(r['severity'])+' | '+str(r['required_primary_batch'] or r['conditional_batch_if_user_selects'])+('（未选）' if r['classification']=='optional' else '')+' | `/records/'+str(i)+'` |\n' for i,r in enumerate(records))
resolution=f'''## 全部39条完整规范合同及逐项入口

全部39合同的唯一完整规范正文为同目录 `contracts.zh.json`，Git mode {contract_id['mode']}，{contract_id['bytes']}B，SHA256 `{contract_id['sha256']}`，Git blob `{contract_id['blob']}`。该文件完整保存每项身份/分类、双向证据及定位、前提与普通/最小反例、失败/取消/部分提交、最小修订/精确read-write/preserve、验收/回归、实际独立裁决链、历史关系及依赖/接收门；正文未删减成摘要或空链接。

每位作者及非作者reviewer必须完整读取所属批次全部required ID的对应JSON对象、其必要源/规格完整单元、共同前提与companions；optional只有用户选择后才进入修订，但必须正确保留未选边界。按下表pointer提取完整对象，可用Python json.load后records[index]或支持JSON pointer的工具；不得将索引/检索命中/身份核验当完整语义阅读。所有合同均有稳定ID复核，索引顺序不改变ID。逐ID完整内容与去重前完全一致的哈希证明见contract-deduplication-proof.json。

每批 `batches/R8-Uxx/prompt.md` 和 `reviewer-prompt.md` 给独立完整执行合同及所属逐项正文，`readset.json`给完整固定读集。manifest、records-index.json及batch-assignment.json使用同一39 ID集。原根审计来源、原提案/反方、历史资格由合同original provenance及C35 findings恢复，原字节只读。

'''
main=COMMON+'## 九批唯一主责\n\n'+table+'\n'+launchtext+resolution+record_table+'\nUPDATE_NOT_STARTED\n'
write('cloud-eighth-update-handoff-prompt.md',main)
for b in batches:
    bid=b['id']; rs=[r for r in records if r['id'] in b['required_ids']+b['optional_ids_if_later_selected']]
    lead=COMMON+f'## 本批 {bid}：{b["title"]}\n\n完整assignment如下。完整事实/反例/控制/验收合同随后给出；optional全部保持未选。\n\n```json\n'+json.dumps(b,ensure_ascii=False,indent=2)+'\n```\n\n'
    write(f'batches/{bid}/prompt.md',lead+'作者逻辑入口'+b['author']['logical_entry']+'，请求xhigh；只写本批候选镜像及证据，不能自签最终接收。完整读本批readset.json。\n\n'+contract_text(rs)+launchtext+'\nUPDATE_NOT_STARTED\n')
    write(f'batches/{bid}/reviewer-prompt.md',lead+'独立reviewer逻辑入口'+b['reviewer']['logical_entry']+'，请求ultra。必须实际不同于作者；先另接收真实candidate/actual commit/tree/path/bytes/SHA/blob。完整读取原输入、受影响候选与实际整合整文件、全部累计保留及共享贡献；逐条给证据、最强反方、判定、未决条件。不能修改作者候选或正式文件，不以角色改名自验。分别报告candidate PASS / actual integrated PASS，root再独立登记ACCEPTED / CLOSED。\n\n'+contract_text(rs)+'\nUPDATE_NOT_STARTED\n')

dedup_rows=[]
on_disk=load(OUT/'contracts.zh.json')['records']
for i,(before,after) in enumerate(zip(records,on_disk)):
    encode=lambda v: json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
    # before is the same normalized complete object that contract_text would
    # embed in the pre-deduplication main; after is its complete on-disk object.
    bh=hashlib.sha256(encode(before['full_contract'])).hexdigest()
    ah=hashlib.sha256(encode(after['full_contract'])).hexdigest()
    assert before==after and bh==ah
    dedup_rows.append(dict(id=before['id'],pointer=f'/records/{i}',before_dedup_complete_contract_sha256=bh,
      after_dedup_complete_contract_sha256=ah,complete_business_and_controls_identical=True,
      object_sha256=hashlib.sha256(encode(after)).hexdigest()))
dump('contract-deduplication-proof.json',dict(schema='r8-final-contract-structural-deduplication-proof/v1',
 method='Canonical UTF-8 JSON sort_keys=true, compact separators, ensure_ascii=false. The exact normalized full_contract objects formerly embedded by contract_text are now resolved from the complete contracts.zh.json. Compare every full object, not a facts summary.',
 contracts_file=contract_id,records=dedup_rows,record_count=39,all_equal=True,
 administration_normalization_separate='administrative-field-deltas.json records original qualified preparation state versus C35 final current state; structural deduplication itself changes no contract field.',
 new_semantic_review_layers=0,new_source_FULL_credit=0,new_independent_votes=0,update_started=False))

index=[{k:r[k] for k in ['id','classification','severity','selection','canonical_root','facet','historical_relation','required_primary_batch','conditional_batch_if_user_selects']}|{'full_contract':{'path':'handoff/contracts.zh.json','pointer':f'/records/{i}'},'root_adjudication':r['root_adjudication']} for i,r in enumerate(records)]
dump('records-index.json',dict(schema='r8-final-39-record-index/v1',records=index,record_count=39,update_started=False))
manifest=dict(schema='r8-final-cloud-eighth-manual-update-handoff/v1',language='zh-CN',status=STATE,
 B8=em['B8'],R=em['R'],R8_core=CORE,final_handoff_publication=PUBLICATION,
 classification_authority=identity('findings.json','唯一当前最终39分类、严重度及根合同'),records=index,
 counts=dict(current_revision_obligations=39,required=29,required_P2=2,required_P3=27,optional=10,optional_selected=0,bounded_NO_REQUIRED=14,binary_negatives=4,independent_policy=1,independent_policy_selected=0,batches=9),
 current_root_task_receptions=dict(primary_registry=identity('adjudication/root-primary-task-final-registry.final.json','最终29 qualified primary task-final完整接收'),accepted_primary_count=29,external_original_tasks_accepted=9,external_original_tasks_total=9,all_necessary_history_and_interfaces_received=True),
 final_history_authority=identity('adjudication/root-final-history-and-canonical-reception.v1.json','最终H canonical/dedup及最后完整历史接收'),
 full_contracts=identity(OUT/'contracts.zh.json','全部39完整合同含原qualified语义和最终当前态',False),
 whole_prompt=identity(OUT/'cloud-eighth-update-handoff-prompt.md','完整干净中文主prompt和39全合同',False),
 administrative_field_deltas=identity(OUT/'administrative-field-deltas.json','原→最终已知非业务字段精确差异，供root有限接收',False),
 input_payloads=identity(OUT/'input-payloads.json','563源/正式身份、51权威、87WP typed覆盖、全部报告proof与116恢复身份入口',False),
 core_publication_proof=proof_ids, core_remote_verified=True,
 core_remote_counts=dict(report_files=25239,report_bytes=2423831391,new_changed_full_readback=602,exact_prior_verified_reused=24637,gzip_restored=116,restored_bytes=1204403716,expected_absent_probes_exit128=2,successful_operations_exit0=12),
 scope=dict(reference=432,formal=131,formal_main=111,catalogs=17,shared=3,WP_rows=87,content_WP=84,stages=3,domains=18,features=113,planning_edges=395,crosscut=9,effective_carrier_paths=301,different_SHA=289,current_semantic_fields=274,purpose_dispositions=15,source_unread=0,formal_clauses_unmapped=0,necessary_consumer_unreceived=0,necessary_history_unreceived=0),
 source_spec_report_identity_rule='原source/spec来源commit保R/B8；original5caff保真且C35恢复位置另绑定；完整报告身份在post-C35 proof /files，不能冒称proof属于C35。',
 history_qualifications='handoff/history-qualifications.json',accepted_facts='handoff/accepted-facts-and-mandatory-companions.json',policy_and_preservation='handoff/policy-and-preservation.json',
 batch_assignment='handoff/batch-assignment.json',dependency_graph='handoff/dependency-graph.json',file_conflict_graph='handoff/file-conflict-graph.json',launch_methods='handoff/launch-methods.json',
 semantic_edit_edges=[],transitive_semantic_edit_edges=[],first_wave_after_release_count=9,currently_started=0,
 actual_formal_writer='R8-INTEGRATOR',common_roles=em['common_roles'],shared_catalog=em['shared_catalog'],
 acceptance_gates=['candidate PASS','actual integrated PASS','ACCEPTED','CLOSED'],
 execution=dict(classification=identity('coverage/final-execution-classification.json','7数学/有限证书+1环境probe，旧PBS摘要原过程identity UNVERIFIED非额外过程'),actual_math_finite_processes=7,environment_probe=1,old_PBS_summary=1,old_PBS_alias='UNRESOLVED_NONBLOCKING_NOT_EXTRA_PROCESS',reference_game_native_observation=0,new_runs_from_this_handoff=0,vectors='NOT_EXECUTED'),
 preservation=dict(original106_exact_file_identities_unchanged=True,proof=identity(BASE/'final-binding-preparation/manifest.json','原106保护对象前置验证及精确归档入口'),current_recheck='handoff/verification/validation.json',source_formal_git_index_main_mutated=False),
 composition_credit=dict(actual_context=ROLE,new_contexts=0,new_independent_votes=0,new_semantic_review_layers=0,new_source_FULL_credit=0,new_business_runs=0),
 B8_compliance_PASS=False,update_started=False,final_marker='UPDATE_NOT_STARTED',
 self_binding='manifest和payload-manifest不含自身未来hash；外部真实后继commit/tree及最终发布入口收口。')
dump('cloud-eighth-update-handoff-manifest.json',manifest)

checks={
 'C35_commit_workspace_RR_trees_actual':CORE['commit']==C35 and CORE['workspace_tree']==WTREE and CORE['report_tree']==RTREE,
    '39_ID_classification_severity_exact_final_findings':[(r['id'],r['classification'],r['severity']) for r in records]==[(r['id'],r['classification'],r.get('severity')) for r in root_records],
 '29_required_each_exactly_one_primary':Counter(x for b in batches for x in b['required_ids'])==Counter(r['id'] for r in records if r['classification']=='required'),
 '10_optional_exactly_assigned_and_unselected':Counter(x for b in batches for x in b['optional_ids_if_later_selected'])==Counter(r['id'] for r in records if r['classification']=='optional') and all(not b['selected_optional_ids'] for b in batches),
 'nine_batches_required_targets_unchanged':len(batches)==9 and all(b['actual_target_write_set']==p['actual_target_write_set'] and b['candidate_write_set']==p['candidate_write_set'] for b,p in zip(batches,base_batches)),
 'DAG_direct_and_transitive_zero':dg['semantic_edit_edges']==dg['transitive_closure_edit_edges']==[],
 '563_fixed_inputs_432R_131F':len(cm['input_file_identities'])==563 and Counter(x['kind'] for x in cm['input_file_identities'])=={'reference':432,'formal':131},
 '51_exact_current_core_authorities':len(auth)==51,
 'post_C35_proof_not_misbound_as_C35_member':all(x['commit'] is None and x['path'] not in TREE for x in proof_ids),
 'handoff_future_enclosing_hash_null':manifest['final_handoff_publication']['enclosing_handoff_commit'] is None,
 '14_NO_REQUIRED_separate':policies['current_bounded_no_required_count']==14,
 '29_required_2P2_27P3_exact':Counter(r['severity'] for r in records if r['classification']=='required')=={'P2':2,'P3':27},
 '4_binary_negatives_1_policy_unselected':policies['binary_negative']['count']==4 and policies['independent_policy']['selection']=='UNSELECTED' and not policies['independent_policy']['write_set'],
 'final29_registry_current_all_received':registry['count']==29 and registry['all_current_necessary_primary_receipts_accepted'] and registry['original_external_nine_accepted']==9,
 'no_WP58_required_writer':all('wp58-battle-recording' not in p for b in batches for p in b['actual_target_write_set']+b['candidate_write_set']),
 'original106_protected_files_exact_unchanged':protected==guard(),
 'all39_complete_contracts_nonempty':all(r['full_contract'] and len(r['full_contract'])>=7 for r in records),
 'all39_in_main_body':all(r['id'] in main for r in records),
 'all_batch_prompts_exact_ID_sets':all(all(rid in (OUT/f'batches/{b["id"]}/prompt.md').read_text() and rid in (OUT/f'batches/{b["id"]}/reviewer-prompt.md').read_text() for rid in b['required_ids']+b['optional_ids_if_later_selected']) for b in batches),
 'no_obsolete_core_pending_marker_in_main':'PENDING_ROOT_CORE_FREEZE' not in main,
 'future_starts_votes_source_FULL_business_zero':all(v==0 for k,v in manifest['composition_credit'].items() if k!='actual_context') and not manifest['update_started'],
}
assert all(checks.values()),checks
dump('verification/validation.json',dict(schema='r8-final-handoff-composition-validation/v1',passed=True,checks=checks,
 scope='TOOL_VALIDATION only; no new semantic review, classification or independent acceptance',
 original_protected_files=106,protected_exact_identities=protected,new_contexts=0,new_independent_votes=0,new_business_runs=0,update_started=False))
dump('reading-ledger.json',dict(schema='r8-final-handoff-same-context-binding-ledger/v1',actual_context=ROLE,
 inherited_qualified_preparation=identity('adjudication/root-handoff-39-preparation-reception.final.json','root接受原完整39准备；本轮不重审38/39'),
 prior_actual_reads=identity(E/'reading-ledger.json','原同context全部有效合同及新增伴件实读台账，原bytes不改'),
 final_binding_reads=['C35 final-report全文','summary全文','findings全部39分类/严重度及当前接收字段','最终H全部39 canonical/关系字段及顶层接收资格','final29 registry完整类型/状态','typed denominators完整用途与实际语义范围字段','WP87全覆盖已qualified权威及顶层分母','完整9个execution行及分型资格','C35 core-manifest全部非数组语义与身份数组机械解析','post-C35 root实际core绑定全文和完整proof结构/身份用途'],
 reading_qualification='本整合复用已合格完整39合同，身份/typed投影不转移原审者源全文信用，不重读源、不新业务执行、不新独立审查层。',
 available_assigned_contract_unread=0,available_assigned_contract_unreceived=0,
 requested=dict(model='gpt-6.1-sol',effort='ultra',tier='default',speed='normal',Fast='off'),
 actual={k:'UNVERIFIED' for k in ['model','effort','tier','speed','Fast','platform_session_id']},
 new_contexts=0,new_independent_votes=0,new_source_FULL_credit=0,new_business_runs=0,update_started=False))
write('remaining.md','''# 最终手动交接状态

READY_FOR_USER_MANUAL_UPDATE / UPDATE_NOT_STARTED。

C35语义core已真实冻结、普通push及完整fresh远端VERIFIED。当前全部必要源/正式/消费者/历史未读或未接收0；本次只做原合格内容的最终态组合与真实身份绑定，无新context/票/审查层/source FULL/业务运行。

本新handoff自身的普通发布、完整远端回读与实际enclosing commit/tree由root真实后继外部绑定完成；本包字段保持null，不能伪造自身未来hash。C35后的proof/root binding同属后继发布身份。用户尚未另行手动启动整改，未来authors/reviewers实际启动0。10optional与独立视觉policy仍未选。原effective39、v1/v2与最早26件共106保护文件逐byte保持。
''')
payloads=[]
for p in sorted(OUT.rglob('*')):
    if p.is_file() and p.name!='payload-manifest.json':
        d=identity(p,'最终handoff后继发布载荷',False)
        payloads.append(d)
dump('payload-manifest.json',dict(schema='r8-final-handoff-payload-manifest/v1',R8_core=CORE,
 final_handoff_publication=PUBLICATION,payloads=payloads,payload_file_count=len(payloads),payload_bytes=sum(x['bytes'] for x in payloads),
 self_binding='本清单排除自身，外部真实后继commit/tree绑定其实际bytes/SHA/blob；不递归selfhash。',
 records=39,required=29,required_P2=2,required_P3=27,optional=10,bounded_NO_REQUIRED=14,binary_negatives=4,independent_policy=1,batches=9,
 update_started=False,final_marker='UPDATE_NOT_STARTED'))
print(json.dumps({'status':STATE,'payloads':len(payloads),'bytes':sum(x['bytes'] for x in payloads),'checks':checks,
 'main':identity(OUT/'cloud-eighth-update-handoff-prompt.md','主prompt',False),
 'manifest':identity(OUT/'cloud-eighth-update-handoff-manifest.json','完整manifest',False),
 'payload_manifest':identity(OUT/'payload-manifest.json','精确载荷清单',False)},ensure_ascii=False))
