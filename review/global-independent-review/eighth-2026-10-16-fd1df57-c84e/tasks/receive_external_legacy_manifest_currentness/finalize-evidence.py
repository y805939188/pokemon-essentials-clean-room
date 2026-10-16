"""Bookkeeping and exact dispatch preparation; generation never grants reading credit."""
from pathlib import Path
import json, hashlib, subprocess, datetime

TASK = Path(__file__).resolve().parent
ROOT = TASK.parents[1]
REPO = ROOT.parents[2]
SRC = TASK / 'inputs/target-93d7df7f'

def read(path):
    return json.loads(path.read_text())

def write(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}

def main():
    utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    freeze = read(TASK / 'frozen-denominator.json')
    events = read(SRC / 'semantic-purpose-review.v2.json')['units']
    dispositions = read(SRC / 'purpose-dispositions.json')['units']
    lines = (REPO / 'planning/review-manifest-2026-09-19.md').read_bytes().splitlines(keepends=True)
    for u in freeze['physical_units']:
        data = lines[u['line'] - 1]
        assert u['bytes'] == len(data) and u['sha256'] == hashlib.sha256(data).hexdigest()
    assert len(events) == 156 and len(dispositions) == 1413
    assert len({n for e in events for n in e['content_paragraph_lines']}) == 881
    assert {n for e in events for a,b in e['line_ranges'] for n in range(a,b+1)} == {u['line'] for u in freeze['physical_units']}

    # Handwritten findings for the actual eight displayed events. Other events stay OPEN.
    notes = {
      66: ('bb01ba', '保留首审12P2/2P3及三包修订身份。搜索先写模式、负盒位、双属性/端点/形态首写与当前WP66-B相接；N01仅登记而未闭合。背包与拼图细节全文已读，但其当前主责/源尚未独立接合，不能签完整事件。'),
      67: ('cc3e5e', '分清11/14关闭与3项待审，37候选的旧len36检查撤回，持久模式/列表/会话/草稿四量保持。拼图合法初态、偶数交集、完成中断前提作为完整历史反例保留；没有读其当前源，不授新通过。'),
      68: ('cc3e5e', '原14项关闭和管理回填不是当前全局批准。N01当时仍待专项，CLOSURE-R01只针对身份登记；行为批准与身份修复两层不能互相豁免。后继066–072链已读，其余外域回执仍待接。'),
      69: ('52c81e', '保留18错误身份、17原正确记录及35/36可测身份的自哈希例外；更正只替代错误字段，不能推翻旧正确行为。该事件属于恢复定位与资格证据；尚未回读其具名原冻结快照，原工具成功不继承。'),
      70: ('52c81e', '初稿把特殊位空格直接送放置并false，漏外层成员门；071纠正，072再纠正确认句。直接队伍位置缺末成员门有效，但不得据此补UI队伍可达。其行为部分已用F-N01链复核，158等未读后继仍保留OPEN。'),
      71: ('4aef15', '接受外层空成员继续循环、Select才公开返回、空返回不回滚、正常输入未发备用暂持命令的前提。操作表仍残留统一Yes语句与摘要身份滞后，必须连072；不把这次修订当最终通过。'),
      72: ('4aef15', '按BACK/Close分别解释Yes，原v2错误回应留史。最终self/boundary身份与原v3报告列值吻合；旧通过仅受理三层选择链，不关闭其他R/GR及特殊位置所有后继。129/158当前路由未接，完整事件不签收。'),
      169: ('3e3d1a', '完整读UI十七输入、401静态向量分族、十三审计条目及输入/当前身份分列；四份B批待审没有自动升级。净化室五层取消、失败前缀、搜索写模式、拼图限制均保留为历史贡献；未独立接收整批UI提供者，不以语义变化0或链接0错授当前通过。'),
    }
    ledger = read(TASK / 'reception-ledger.json')
    for row in ledger['events']:
        n = int(row['id'][4:])
        if n in notes:
            evidence, note = notes[n]
            row.update(status='FULL_TEXT_READ_PARTIAL_RECEPTION', reason=note,
                       output_evidence=evidence, lossless_view='evidence/event-views/' + row['id'] + '.json',
                       complete_event_acceptance=False,
                       current_domain_provider_reception='OPEN; precise routing and non-N01 consumers not inherited')
    source_notes = [
      ('F-N01-01', '选择以模式1启动，正常队伍页不打开；空成员继续循环、有成员先菜单且Select才公开返回。', ['1c01f3','561cbf','cce4c5']),
      ('F-N01-02', '补读确认包装和完整命令返回门：BACK Yes继续/No或取消退出，Close Yes退出/No或取消继续。', ['1c01f3','561cbf','037dba']),
      ('F-N01-03', '切盒直接写currentBox；完成取出先复制入队再删盒格；后来空返回没有逆向恢复，取消本次新位置不撤销既有提交。', ['1c01f3','08c4aa']),
      ('F-N01-04', '有效直接队伍位置经蛋/Shadow放置门，放置之后删除并压紧，有限链无最后可战斗门；普通UI可达性另列。', ['1c01f3','08c4aa','cf77ed']),
      ('F-N01-05', '基础构造40盒×30格，仅-1为队伍；-2/-1映射盒38格29；保存登记绑定基础容器，真实往返未执行。', ['08c4aa','1c01f3']),
    ]
    forward = read(SRC / 'forward-mapping.json')['facts']
    reverse = read(SRC / 'reverse-mapping.json')['clauses']
    ledger['facts'] = [{**next(f for f in forward if f['id']==key),
                        'status':'RECEIVED_SCOPED_STATIC', 'independent_meaning':note,
                        'output_evidence':evidence,
                        'reverse_clauses':[r for r in reverse if r['fact']==key],
                        'inherited_author_read_credit':False} for key,note,evidence in source_notes]
    ledger['facts'] += [{**f,'status':'OPEN_SOURCE_CONSUMER_RECEPTION','reason':'仅已全文读取提案矩阵，尚未读取必要WORLD提供者记录及完整当前定义。'} for f in forward if not f['id'].startswith('F-N01-')]
    read_lines = {n for e in events if e['round'] in notes for a,b in e['line_ranges'] for n in range(a,b+1)}
    para_lines = {n for e in events if e['round'] in notes for n in e['content_paragraph_lines']}
    summary = {'events_denominator':156,'events_full_text_read':8,'events_complete_reception':0,
               'events_unread':148,'events_read_but_necessary_joins_open':8,
               'paragraphs_denominator':881,'paragraphs_full_text_read':len(para_lines),
               'paragraphs_unread':881-len(para_lines), 'primary_lines_denominator':1413,
               'primary_lines_full_text_read':len(read_lines), 'primary_lines_unread':1413-len(read_lines),
               'primary_bytes_read':sum(len(lines[n-1]) for n in read_lines),
               'primary_bytes_unread':627400-sum(len(lines[n-1]) for n in read_lines),
               'content_bytes_read':sum(len(lines[n-1]) for n in para_lines),
               'facts_received_scoped_static':5,'world_facts_open':5,'required_new_confirmed':0,
               'H001_counter_suggestion':'NO_REQUIRED_BOUNDED_SCOPE; ROOT_DECISION_PENDING',
               'unavailable_materials_for_static_reception':0,
               'capacity_is_not_material_or_host_limit':True}
    ledger.update(status='INCOMPLETE',utc=utc,summary=summary)
    write(TASK/'reception-ledger.json',ledger)
    freeze.update(status='FROZEN_EXACT_NOT_COMPLETE_ACCEPTANCE', independent_counts=summary,
                  identity_check='evidence/catalog-identity-check.json', semantic_credit_from_generation=0)
    write(TASK/'frozen-denominator.json',freeze)

    reading=read(TASK/'reading-ledger.json')
    for filename, ranges, evidence in [
      ('deliverables/final-specification-set/pokemon-rules/wp23-shadow-hyper-and-purification.md',[[1,110],[111,199]],['be87c0','303803']),
      ('deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md',[[1,100],[101,210],[211,313]],['be87c0','303803','e24b53']),
      ('review/wp23-n01-review-2026-10-01/recheck-v3/report.md',[[1,76]],['e24b53']),
      ('deliverables/final-specification-set/README.md',[[1,21]],['e24b53']),
      ('deliverables/final-specification-set/scope-statement.md',[[1,21]],['e24b53']),
      ('CURRENT-DELIVERY.md','FULL',['e24b53']),
      ('delivery/2026-10-16-seventh/README.md','FULL',['a78221']),
      ('review/remediation-seventh-20261015-prepare/current-navigation-errata.json','FULL',['037dba']),
      ('audit/source-traceability.md',[[525,548],[1305,1335]],['561cbf']),
      ('planning/feature-matrix.md',[[184,187]],['561cbf']),
      ('deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md',[[199,201]],['561cbf']),
      ('planning/extraction-plan.md',[[1,8]],['a78221']),
      ('planning/review-manifest-2026-09-19.md',[[1,65],[4115,4127]],['a78221']),
    ]:
        data=subprocess.check_output(['git','show','fd1df570cad987dc3852a3b958f03916e317f7fe:'+filename],cwd=REPO)
        reading['items'].append({'repository':'B8','commit':'fd1df570cad987dc3852a3b958f03916e317f7fe',
                                 'path':filename,**identity(data),'ranges':ranges,'output_evidence':evidence,
                                 'credit':'ACTUAL_TEXT_READ; clause reception only as individually stated'})
    source_ranges = [
      ('Data/Scripts/016_UI/017_UI_PokemonStorage.rb',[[585,720],[716,945],[1490,1505],[1675,1778],[1964,2022]],['1c01f3','561cbf','037dba','cce4c5']),
      ('Data/Scripts/016_UI/023_UI_PurifyChamber.rb',[[52,348],[361,546],[1160,1308]],['1c01f3','561cbf','037dba','cf77ed']),
      ('Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb',[[1,310]],['08c4aa']),
      ('Data/Scripts/002_Save data/004_Game_SaveValues.rb',[[80,113]],['08c4aa']),
      ('Data/Scripts/001_Settings.rb',[[210,230]],['08c4aa']),
      ('Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb',[[90,112]],['037dba']),
    ]
    for filename,ranges,evidence in source_ranges:
        data=subprocess.check_output(['git','show','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:'+filename],cwd='/workspace/pokemon-essentials')
        reading['items'].append({'repository':'R','commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',
                                 'path':filename,**identity(data),'ranges':ranges,'output_evidence':evidence,
                                 'credit':'ACTUAL_DISPLAYED_RANGES_ONLY; incidental cut starts/ends do not certify adjacent functions',
                                 'accepted_complete_functions':'Only necessary complete definitions enumerated in F-N01 facts/counter-h001.md'})
    for n,(evidence,note) in notes.items():
        e=next(e for e in events if e['round']==n)
        reading['items'].append({'path':'evidence/event-views/'+e['id']+'.json','range':'FULL',
                                 'original_manifest_ranges':e['line_ranges'],'output_evidence':evidence,
                                 'credit':'FULL_TEXT_READ; EVENT_COMPLETE_RECEPTION_FALSE','meaning':note})
    reading['items'] += [{'path':'inputs/target-93d7df7f/'+name,'range':'FULL','output_evidence':ev,'credit':'ACTUAL_TEXT_READ; independent reception per fact'} for name,ev in [('forward-mapping.json','cf77ed'),('reverse-mapping.json','cf77ed'),('bounded-consumer-search.json','3e3d1a'),('gaps.json','3e3d1a')]]
    reading.update(status='INCOMPLETE',utc=utc,summary=summary,
                   output_truncations=[{'evidence':'initial Github global prompt','repair':'Github lines105–200 plus local1–105/201–end'},
                                       {'evidence':'6fb970','repair':'bb01ba complete066 and cc3e5e complete067; no lost paragraph accepted'}],
                   public_projection_limit='Tool output identifiers identify actual platform reads; complete private platform stream is not exported or claimed remote-read-back.')
    write(TASK/'reading-ledger.json',reading)
    interfaces=read(TASK/'interfaces.json')
    for row in interfaces['interfaces']:
        row['independent_reception']='RECEIVED_FIVE_FACTS_SCOPED_STATIC' if row['id']=='I-LMC-N01' else 'OPEN'
        if row['id']=='I-LMC-N01':row['facts']=[f['id'] for f in ledger['facts'] if f['status']=='RECEIVED_SCOPED_STATIC']
    interfaces.update(status='INCOMPLETE',utc=utc,root_final_acceptance='ROOT_ONLY')
    write(TASK/'interfaces.json',interfaces)
    counters=read(TASK/'proposal-counters.json'); counters['items'][0].update(state='INDEPENDENT_COUNTER_COMPLETE_SCOPED_ROOT_DECISION_PENDING',classification='NO_REQUIRED_BOUNDED_SCOPE_PROPOSED',evidence='counter-h001.md',new_required=0)
    counters.update(status='INCOMPLETE_TASK_COUNTER_SCOPED_COMPLETE',utc=utc)
    write(TASK/'proposal-counters.json',counters)

    # Exact, executable-by-parent dispatch contracts. No child is started here.
    full_readset=read(ROOT/'delegation/readsets/receive_external_legacy_manifest_currentness.complete.json')
    routes=read(SRC/'current-primary-contribution-routes.v2.json')
    remaining=[e for e in events if e['round'] not in notes]
    groups=[]; group=[]; nbytes=0
    for e in remaining:
        size=sum(len(lines[n-1]) for n in e['content_paragraph_lines'])
        if group and nbytes+size>32000:groups.append(group);group=[];nbytes=0
        group.append(e);nbytes+=size
    groups.append(group)
    base_prompt=(ROOT/'delegation/prompts/receive_external_legacy_manifest_currentness.md').read_text()
    appendices='\n\n---\n\n# 全文合同附件\n\n'+base_prompt+'\n\n'+(ROOT/'inputs/eighth-global-review-prompt.md').read_text()+'\n\n'+(ROOT/'inputs/review-SKILL.md').read_text()+'\n\n'+(REPO/'AGENTS.md').read_text()
    dispatch=[]
    for index,g in enumerate(groups,1):
        sid=f'S{index:02d}'
        ids={e['id'] for e in g}; selected_lines={n for e in g for a,b in e['line_ranges'] for n in range(a,b+1)}
        rids={rid for e in g for rid in e['current_formal_routes']}
        rs={**full_readset,'schema':'r8-lmc-capacity-exact-shard/v1','id':sid,
            'parent_contract_commit':'40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232',
            'events_all_fields':g,'paragraph_dispositions_all_fields':[r for r in dispositions if r['line'] in selected_lines],
            'physical_line_identities':[r for r in freeze['physical_units'] if r['line'] in selected_lines],
            'current_routes_all_fields':[r for r in routes['formal_routes'] if r['id'] in rids],
            'providers_all_fields':[r for r in routes['providers'] if any(r['id'] in cr['provider_ids'] for cr in routes['formal_routes'] if cr['id'] in rids)],
            'source_evidence_catalog':read(SRC/'evidence-catalog.json'),
            'exclusive_write_set':str((TASK/'shards'/sid).relative_to(ROOT))+'/',
            'status':'PLANNED_NOT_STARTED','semantic_credit':0,
            'selection_is_complete_event_set':True,'complete_parent_acceptance':False}
        write(TASK/'split-contracts'/f'{sid}.complete.json',rs)
        text=f'''# {sid}：legacy manifest 完整事件接收\n\n父线程直接派发材料；尚未实际启动。固定合同40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232、目标93d7df7f66adcaa25811fd6ff09352b754577af0及B8/R身份完全保持。实际审者须不同于01a143c7-a558-738e-9580-11a8f12d903f；不得假造新context/票，不自行spawn。\n\n唯一主责事件：{', '.join(e['id'] for e in g)}。完整读集见同名{sid}.complete.json，包含每个事件全部字段、所有原始段落身份、完整用途字段和当前路由/提供者。按该读集从B8恢复每个原文段，完整呈现并实际阅读；范围中摘要与详细版均读，原错误和后继澄清不可删除。相关后继事件可以只读依赖接收，不争夺其他shard主责。\n\n唯一写集 {rs['exclusive_write_set']}。报告、阅读与接收ledger、逐事实接口、未接对象及必要证据都只写该子目录。普通提交/推送只有父线程再次实际派发时明确绑定的专用分支才执行；本计划不授权写其他分支、main/tag或他人目录。\n\n先全文读取本文件附件、同名完整readset和全部33目标输入的精确字段用途。原作者的FULL_READ/用途0、恢复/哈希/视图生成均不授本轮语义信用。每个事件给完整意义、实际源/当前B8条款及消费者、历史用途/后继、最强NO_REQUIRED、输出凭证、未决。必要定义读到完整结束行；发现未接提供者须具名OPEN，不以当前路由存在冒签。已读不等于已完整接收。执行向量NOT_EXECUTED，UPDATE_NOT_STARTED。\n\n完成全部选定事件及其必要边界后报告精确固定C/tree与内容身份；任何必要对象未收则INCOMPLETE。父线程独占根最终签收。\n'''+appendices
        (TASK/'split-contracts'/f'{sid}.md').write_text(text)
        dispatch.append({'id':sid,'event_ids':[e['id'] for e in g],'events':len(g),
                         'content_paragraphs':sum(len(e['content_paragraph_lines']) for e in g),
                         'content_bytes':sum(len(lines[n-1]) for e in g for n in e['content_paragraph_lines']),
                         'readset':f'split-contracts/{sid}.complete.json','prompt':f'split-contracts/{sid}.md',
                         'write_set':rs['exclusive_write_set'],'status':'PLANNED_NOT_STARTED'})
    open_files=[r['relative_to_target_task'] for r in full_readset['files'] if r['relative_to_target_task'] not in {'review.md','proposals.json','interfaces.json','purpose-rules.v2.json','forward-mapping.json','reverse-mapping.json','bounded-consumer-search.json','gaps.json'}]
    extras=[
      ('S21','五条WORLD事实和完整必要接口',{'fact_ids':[f['id'] for f in ledger['facts'] if f['status'].startswith('OPEN')], 'mandatory_whole_objects':['world-interface-reception.v2.json'], 'source_catalog_ids':[r['id'] for r in read(SRC/'evidence-catalog.json')['items'] if r['id'].startswith('E-V2-')], 'instructions':'完整接收两个固定提供者的12条record及所有字段，逐事实核完整源定义、caller/receiver与B8条款；原作者截断end必须补读，不能继承外域FULL_READ。'}),
      ('S22','131当前路由及已读8事件必要接合',{'mandatory_whole_objects':['current-primary-contribution-routes.v2.json'], 'event_ids':[f'LM-E{n:03d}' for n in notes], 'instructions':'所有131 formal_routes、20 providers逐字段区分身份/用途和业务接收；逐个核已读8事件未接后继129/130/158/171等、WP66-C/WP71及整批UI必要提供者。完整read不重算为新票，必要消费者未收不得签完整事件。'}),
      ('S23','工具/身份/审读资格及旧失败载荷',{'mandatory_whole_objects':open_files, 'instructions':'对余25目标载荷逐对象/字段完整用途处置；包含scripts时只读不执行，当前有效手写语义须真实读或证明与已接对象逐值等价。完整保留attempt1/2、旧v1错误和后继clarifier；传输/身份字段不得掩盖业务断言。与S01–22重叠内容只按精确对象/字段别名去重，不能二次加信用。'}),
    ]
    for sid,title,details in extras:
        rs={**full_readset,'schema':'r8-lmc-capacity-exact-shard/v1','id':sid,'details':details,
            'exclusive_write_set':str((TASK/'shards'/sid).relative_to(ROOT))+'/',
            'source_evidence_catalog':read(SRC/'evidence-catalog.json'),'status':'PLANNED_NOT_STARTED','semantic_credit':0}
        write(TASK/'split-contracts'/f'{sid}.complete.json',rs)
        (TASK/'split-contracts'/f'{sid}.md').write_text(f'# {sid}：{title}\n\n仅供父线程直接派发，尚未启动。完整范围/对象/字段/身份见{sid}.complete.json。\n\n{details["instructions"]}\n\n唯一写集 {rs["exclusive_write_set"]}；不自行spawn、不整改、不合main、不执行恢复的旧脚本。实际审者必须不同于原作者。所有必要对象实际完整接收且逐事实接合之前INCOMPLETE；父线程最终签收独占。发布须由父实际派发明确专用分支。本计划本身不启动任务。\n'+appendices)
        dispatch.append({'id':sid,'title':title,'readset':f'split-contracts/{sid}.complete.json','prompt':f'split-contracts/{sid}.md','write_set':rs['exclusive_write_set'],'status':'PLANNED_NOT_STARTED'})
    assigned=[x for d in dispatch[:20] for x in d['event_ids']]
    assert len(assigned)==len(set(assigned))==148 and set(assigned)=={e['id'] for e in remaining}
    write(TASK/'split-contracts/dispatch.json',{'schema':'r8-lmc-exact-capacity-dispatch/v1','utc':utc,
          'reason':'627400B primary / 613079B actual content plus source/consumer and operative metadata exceeds this single bounded context; readable unread remains OPEN, not host/material limit.',
          'parent_contract_commit':'40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232',
          'target_commit':full_readset['target_commit'],'actual_spawned_here':0,'planned':dispatch,
          'remaining_events':148,'remaining_paragraphs':832,'parent_root_final_acceptance':'ROOT_ONLY; receive exact reports and cumulative joins, do not mark all complete from split generation',
          'planning_semantic_credit':0})
    write(TASK/'evidence/semantic-summary.json',summary)
    print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':
    main()
