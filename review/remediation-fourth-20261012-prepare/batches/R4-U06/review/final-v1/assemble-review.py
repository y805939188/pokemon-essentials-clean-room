#!/usr/bin/env python3
"""Assemble the final reviewer's judgments and supporting independent notes."""
import datetime
import hashlib
import json
import os
import pathlib
import subprocess

HERE=pathlib.Path(__file__).resolve().parent
REPO=next(p for p in HERE.parents if (p/'AGENTS.md').is_file())
PREFIX='review/remediation-fourth-20261012-prepare/'
PACK=PREFIX+'registration/R4-U06/'
OUT=str(HERE.relative_to(REPO))+'/'
INPUT='1dd05964f59772886de9b808a929c168c73fa184'
TREE='778481a38dad208ebb54127ca3b4a58078c4bc0e'
TASK='7897037ae93af82aa9246a097c4badbd344a15b1'
TASK_TREE='f4026ead2457d3cccc693beb3bb240c69ec24cad'
BRANCH='codex/r4-u06-final-review-20261012-7897037'
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
REVIEWER_THREAD='01a13183-411d-7017-93db-a79fe18bf037'

def git(*a):return subprocess.check_output(['git',*a],cwd=REPO)
def load(p):return json.loads((REPO/p).read_text())
def write(n,d):(HERE/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def identity(p,commit=None):
    b=git('show',commit+':'+p) if commit else (REPO/p).read_bytes()
    result={'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
            'git_blob':hashlib.sha1(('blob '+str(len(b))+'\0').encode()+b).hexdigest()}
    if commit:result['commit']=commit
    return result

RATIONALE={
 'GR4-M01-001':'合法同域同形态的后键/后位置覆盖与独有键、稀疏位置保留，仍与运行game/core优先及PBS整条替换分开；Map形态门、A013头及完整导入先截断保留。',
 'GR4-M01-002':'本地化普通/地图参数解释发生在WP17接收之前；反斜线1先删除、反斜线&恢复占位，不会被新布局或输入规则改成显示暂停；格式化对照独立。',
 'GR4-M02-001':'变量槽墙钟记录、严格大于/提前查询清0及一般天数公式保持；事件私有冷却、累计游戏时间与个体time_form_set不混用，取消保存不撤销查询写入。',
 'GR4-M02-002':'POST字符串键/符号键/空格失败和便利空串分开；构造发生在宿主调用之前，不影响GET合同，精确异常只保留原Ruby2.6回执资格。',
 'GR4-M02-003':'有状态轮次及1/7重复、6/7未见选择保持；耗尽重开不等于每n次必全覆盖，未扩为其它系统的默认策略或统计执行。',
 'GR4-M03-001':'原始锚点、各轴负/零/正严格筛选、固定参考候选序及一次尝试保持；当前位置变化不重设锚点，受阻不重抽，路线调度与转换消费者无额外提交。',
 'GR4-M03-002':'转移/载具取消与临时字段清理分开；SF04可冲浪水域只清基点保surfing，SF06陆地完成才额外收尾；新皮肤/消息/排版无独立清理，ending真阻通常201。',
 'GR4-M03-003':'116正ID缺实例仍登记且推进一次/让出；辅助实例门与正常进入清表/恢复保留，下一更新机会仍过等待门，UI消息不变为全部解释器停止保证。',
 'GR4-M04-001':'个体取图先求动态形态再匹配，严格五日界/forced/battle/storage保留；缺图不回滚已提交前缀，变量计时清槽不套到个体时间戳；A053孵化分层保持。',
 'GR4-M05-001':'五种主动PP战斗HP>0资格位于登记扣减前，场外濒死可补PP而不复活；类型2取消回成员、资格拒绝留循环，数量与退款均保持各自入口/阶段。',
 'GR4-M06-001':'普通单持物双不同Power只继承3项；合法Knot+至多一Power且gen≥6才5项，gen5为3；同属性去重与正确WP34/孵化原合同保留。',
 'GR4-M10-001':'命令BACK优先、逐位数字方向后USE、件数首动作及命名局部次序各自成立；事件103取消默认初值，通用取消-1不移作事件默认。',
 'GR4-M10-002':'冷链首命中/全缺与显式Missing后暖读空分开；空w单窗清空保留，新皮肤结果不推出冲浪临时清理或所有窗口同步。',
 'GR4-M10-003':'本地化先返回文本再按词边界/+2门排版；A B宽22/21一行/移B，无空白长词不硬拆，消息行满与摘要固定宽度不承诺像素全可见。',
 'GR4-M10-004':'108默认身份格及六槽意义可消费，精确hit偏移/默认无偏移、OppMove优先和媒体分开；WP74关联编译、旧缓存及零有效项保旧映射不矛盾。',
 'GR4-M11-001':'图鉴普通请求只消费性别/形态且保末次异色；多项Forms首轮写false是另一分支；J11 Area/J13获得记录不被冒作普通刷新证明，资源通用合同保持。',
 'GR4-M12-001':'整集零槽过滤但率/后缀保留、单类型空Copy保条目仍分开；登记/PBS省略/No档案重载与当前快照装配逐阶段判断，U02转换和U03输入无隐含热刷新。'
}

HANDSHAKES=[
 {'id':'U06-H01','contract':'本地化输出 → 布局/输入','verdict':'PASS_SCOPED',
  'anchors':['generic-kernel/wp08-localization.md §5.3/§6.3.2','user-interface/wp17-draw-text-tags.md §3.1','user-interface/wp17-messages-windows-input.md §4.1/§5.4','user-interface/wp66-c-bag-item-storage-and-shop-ui.md §5.1'],
  'normal':'Q正常插入；返回A B后按给定A/B8、空格4，宽22一行、21移B。',
  'failure_or_boundary':'反斜线1参数在本地化返回前删除，不再生成显示暂停；长无空白AB不硬拆，不签字体/像素。',
  'cancel':'命令BACK先、数字USE先且越界不处理同轮BACK；数量与光标命名独立，不全局统一取消。',
  'repeat':'同域后值覆盖/独有键保留不影响每次布局；商店方向重复仅编辑，需后继确认。',
  'committed_prefix':'显示阶段失败不恢复翻译导入累计内存或已截断产物，不能由退出UI推事务。'},
 {'id':'U06-H02','contract':'临时世界状态 → 当前显示/等待','verdict':'PASS_SCOPED',
  'anchors':['engine-overworld/wp11-map-topology-transfer.md §4','engine-overworld/wp12-terrain-movement-vehicles.md §5.2','engine-overworld/wp59-world-time-weather-field-moves.md §7','engine-overworld/wp16-world-rendering-and-visual-transitions.md §4.3','pokemon-rules/wp61-field-passive-effects-and-blackout.md §3.2','user-interface/wp17-messages-windows-input.md §7'],
  'normal':'合格地图场景/玩家/非空基点通知清基点；ending真才额外收尾。SF04水域对照和SF06陆地对照分开。',
  'failure_or_boundary':'失败前跳后正常201保游泳/旧基点；人工ending真先阻解释器到达通常201，不推永久软锁。',
  'cancel':'确认前拒绝未提交；载具取消只改载具标记，皮肤/消息关闭不独立清临时字段。',
  'repeat':'无合格通知时显示持续消费旧基点；地图微更新有场景/淡出门，不能替代通常解释器更新或保证每次帧通知。',
  'committed_prefix':'先surfing/统计/基点再尝试跳跃；失败不回滚。116登记与让出仍独立，不保证下一渲染帧执行。'},
 {'id':'U06-H03','contract':'主动PP资格 → 取消/确认/数量','verdict':'PASS_SCOPED',
  'anchors':['creature-rpg/wp28-item-use-and-training.md §5.2','user-interface/wp67-a-battle-interaction-and-presentation.md §5.2/§5.3','user-interface/wp17-messages-windows-input.md §5.4','user-interface/wp66-c-bag-item-storage-and-shop-ui.md §5.1','combat-requirements/wp40-commands-obedience-and-action-order.md §4.2'],
  'normal':'五种主动PP已过通用门且HP>0/缺PP才战斗登记；独立場外HP0可恢复，HP仍0，每次用1。',
  'failure_or_boundary':'HP0战斗拒绝留成员循环，库存1/PP0，发生在登记扣减前；满PP无效果，AI/被动LEPPA独立。',
  'cancel':'类型2选招取消回成员，未扣；成员取消回物品列表，不以普通数字/商店规则改取消层级。',
  'repeat':'补满后再次使用失败不扣；+10封顶/回满与选招、逐槽恢复按原合同。',
  'committed_prefix':'已登记后资格变化复检/退款/消费身份残留按J07旧合同；登记前HP0拒绝没有本次退款身份。'},
 {'id':'U06-H04','contract':'编辑登记 → PBS → 当前运行快照','verdict':'PASS_SCOPED',
  'anchors':['demo-dx/wp73-b-world-editors.md §6.1–§6.5','generic-kernel/wp04-pbs-lifecycle.md §5.5','creature-rpg/wp36-wild-encounters-and-modifiers.md §3.1/§9','demo-dx/wp75-project-conversion-and-authoring-tools.md §8.6','user-interface/wp17-messages-windows-input.md §4.1/§5.4'],
  'normal':'源Land0槽/21，整集Copy目标无Land条目但保率/后缀；单类型Copy到Cave保空条目。',
  'failure_or_boundary':'精确目标冲突拒绝；PBS仅随后省空类型；同版本赋值早退，真实异值且合法上下文才装配快照。',
  'cancel':'Copy前地图/版本取消不登记；No依原档案且重载成功消未保存副本，不恢复所有消费者。',
  'repeat':'重新新增列表按目标类型条目而非残留率；不把反复保存/调试包装当快照刷新。',
  'committed_prefix':'登记、档案保存、PBS写出、实际装配分开；已写档案/PBS前缀失败不总回滚，输入/转换不广播热更新。'}
]

def main():
    note_names=['u01-u02.json','u03.json','u04-u05.json','legacy-junctions.json','identities-gates.json']
    notes={n:json.loads((HERE/'subreviews'/n).read_text()) for n in note_names}
    assert os.environ.get('CODEX_THREAD_ID') == REVIEWER_THREAD
    assert all(not notes[n].get(k,[]) for n in note_names for k in ['blockers','blocking_issues','required_blockers','mandatory_blockers','required_changes','remaining_blockers_in_reviewed_scope'])
    packet=load(PACK+'findings-and-criteria.json')
    formal=load(PACK+'formal-identities.json')['records']
    validation=load(OUT+'input-validation.json')
    assert validation['status']=='PASS_FIXED_INPUT_IDENTITIES_AND_BOUNDARIES'
    assert set(RATIONALE)=={r['id'] for r in packet['records']}
    dependency=load(PACK+'dependencies-and-shared-proposals.json')
    findings=[]; criteria=[]
    note_for_batch={'R4-U01':'u01-u02.json','R4-U02':'u01-u02.json','R4-U03':'u03.json','R4-U04':'u04-u05.json','R4-U05':'u04-u05.json'}
    for ri,r in enumerate(packet['records']):
        fid=r['id']; sub='subreviews/'+note_for_batch[r['batch']]
        findings.append({'id':fid,'batch':r['batch'],'title':r['canonical_background']['record']['title'],
            'verdict':'FINAL_PASS_SCOPED','criteria_count':r['criteria_count'],
            'final_composition_reason':RATIONALE[fid],
            'original_finding':r['canonical_background'],'qualified_chain':r['exact_qualified_chain'],
            'exact_final_formal_files':r['current_formal_file_identities'],
            'current_state':'ACCEPTED_SCOPED','CLOSED':False,
            'closure_eligibility':'ELIGIBLE_FOR_UNIQUE_REGISTRAR_SCOPED_CLOSURE_AFTER_PUBLISHED_FINAL_REVIEW_ACCEPTANCE',
            'new_mandatory_changes':[],'independent_auxiliary_assessment':sub})
        for ci,c in enumerate(r['all_actual_criterion_results']):
            cid=c.get('criterion_id',fid+'/C'+str(ci+1).zfill(2))
            text=c.get('criterion',c.get('complete_criterion'))
            kind=c.get('kind')
            if isinstance(text,dict):kind=kind or text.get('kind');text=text.get('criterion')
            boundary=bool(kind and ('runtime' in kind.lower() or 'execution_optional' in kind.lower() or 'executed_host' in kind.lower())) or (isinstance(text,str) and text.startswith('运行：'))
            if r['batch'] in ['R4-U01','R4-U02']:
                aux_findings=notes['u01-u02.json']['findings']
                ai=next(i for i,x in enumerate(aux_findings) if x['id']==fid)
                auxiliary=aux_findings[ai]['criteria'][ci]
                aux_pointer=f'/findings/{ai}/criteria/{ci}'
                aux_reason=auxiliary['independent_final_reason']
            elif r['batch']=='R4-U03':
                ai=next(i for i,x in enumerate(notes['u03.json']['criteria']) if x['finding_id']==fid and x['criterion_number']==ci+1)
                auxiliary=notes['u03.json']['criteria'][ai]
                aux_pointer=f'/criteria/{ai}'
                aux_reason=auxiliary['final_input_basis']
            else:
                ai=next(i for i,x in enumerate(notes['u04-u05.json']['criteria']) if x['finding_id']==fid and x['id'].endswith('/AC'+str(ci+1)))
                auxiliary=notes['u04-u05.json']['criteria'][ai]
                aux_pointer=f'/criteria/{ai}'
                aux_reason=auxiliary['independent_final_reason']
            criteria.append({'criterion_id':cid,'finding_id':fid,'batch':r['batch'],
                'ordinal':ci+1,'kind_as_published':kind,'complete_criterion':text,
                'verdict':'FINAL_PASS_SCOPED','pass_meaning':'EVIDENCE_BOUNDARY_COMPLIANCE_ONLY' if boundary else 'SCOPED_STATIC_FACT_AND_FINAL_COMPATIBILITY',
                'original_current_mapping':{'commit':INPUT,'path':PACK+'findings-and-criteria.json','pointer':f'/records/{ri}/all_actual_criterion_results/{ci}'},
                'prior_actual_criterion_record':c,'basis':'EXACT_UNCHANGED_INDEPENDENT_SCOPED_EVIDENCE_REUSE_PLUS_NEW_FINAL_COMPOSITION_CHECK',
                'new_final_composition_reason':RATIONALE[fid],'independent_auxiliary_assessment':{'path':sub,'pointer':aux_pointer,'criterion_specific_reason':aux_reason},
                'criterion_identity_note':'Final-review deterministic finding/ordinal identity; exact originally published identity retained in prior record/pointer',
                'new_execution':'NOT_EXECUTED_THIS_UPDATE','blockers':[]})
    assert len(findings)==17 and len(criteria)==len({c['criterion_id'] for c in criteria})==76
    identity_data={'role':'R4-U06-final-reviewer','task':'/root','source_thread_id':'01a10d94-84b9-759e-aa1d-edb0d9b6d0e2',
        'source_thread_role':'Delegating parent only, never falsely the reviewer runtime thread',
        'runtime_reviewer_thread_echo':REVIEWER_THREAD,'runtime_thread_echo_source':'CODEX_THREAD_ID single field only; no full environment or model backend inspected',
        'independence':'Dedicated new delegated final review; verified new thread differs from delegating parent, all five original author threads and all five original actual reviewer threads; no authorship or registrar action in this task; evidence-only branch and write scope',
        'excluded_author_thread_ids':load(PACK+'final-review-handoff.json')['author_thread_ids'],
        'excluded_registrar':'fourth-preparation-registrar','requested_model':{'model':'gpt-6.1-sol (sol)','reasoning_effort':'ultra','service_tier':'Standard / default','fast':False},
        'actual_model_reasoning_tier_fast_echo':'UNVERIFIED','backend_or_quota_audit_performed':False,
        'final_input':{'commit':INPUT,'tree':TREE},'task_publication':{'commit':TASK,'tree':TASK_TREE},
        'review_branch':BRANCH,'review_write_root':OUT,'formal_write_paths':[],'registration_write_paths':[],
        'source_reference':{'commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','read_only':True,'new_behavior_execution':0},
        'skill_check':{'paths':['/workspace/.agents/skills','/workspace/r4-u06-final-review/.agents/skills','task publication .agents tree'],'result':'NOT_PRESENT','AGENTS_md':'READ_AND_APPLIED'},
        'formal131':formal,'auxiliary_review_tasks':['/root/u01_u02_composition','/root/u03_criteria_regression','/root/u04_u05_handshakes','/root/legacy_junctions','/root/identity_gates'],
        'auxiliary_runtime_thread_echo':{'u03':'01a13185-7962-7617-a629-6c848d78503c (single CODEX_THREAD_ID echo, see note)','others':'UNVERIFIED'},'signed_at':NOW}
    assert REVIEWER_THREAD not in identity_data['excluded_author_thread_ids']
    assert REVIEWER_THREAD != identity_data['source_thread_id']
    old_reviewers=[r['same_candidate_actual_reviewer_thread_id'] for r in notes['identities-gates.json']['five_complete_chains']]
    assert REVIEWER_THREAD not in old_reviewers
    identity_data['excluded_old_actual_reviewer_thread_ids']=old_reviewers
    write('identity.json',identity_data)
    write('findings.json',{'verdict':'FINAL_PASS_SCOPED','final_input':{'commit':INPUT,'tree':TREE},'findings':findings,'blockers':[],
        'effective_CLOSED_GR4':0,'registration_performed':False,'closure_eligibility':'17 ELIGIBLE_FOR_REGISTRAR_SCOPED_CLOSURE; acceptance/closure remains the unique registrar action'})
    write('criteria-results.json',{'verdict':'FINAL_PASS_SCOPED','count':76,'boundary_compliance_only':sum(c['pass_meaning']=='EVIDENCE_BOUNDARY_COMPLIANCE_ONLY' for c in criteria),
        'count_is_not_execution_cases_or_GR3_standards':True,'records':criteria,'blockers':[]})
    write('dependencies-handshakes.json',{'verdict':'FINAL_PASS_SCOPED','final_input':{'commit':INPUT,'tree':TREE},
        'entry_dependencies':[dict(e,final_verdict='MET_IN_FIXED_FINAL_INPUT') for e in dependency['dependency_edges']],
        'four_final_handshakes':HANDSHAKES,'shared_and_reverse_proposal_review':'subreviews/identities-gates.json',
        'shared_registry_count':25,'new_formal_writer_conflicts':[],'extra_required_formal_edits':[],
        'remaining_mandatory_review_dependencies':[],'remaining_administrative_action':'Unique registrar accepts published exact final verdict, then registers scoped closure; reviewer does neither'})
    junctions=[]
    for r,aux in zip(load(PACK+'junction-dispositions.json')['records'],notes['legacy-junctions.json']['junction_dispositions']):
        assert r['id']==aux['id']
        junctions.append(dict(r,final_review_disposition=aux['review_disposition'],final_review_reason=aux['reason'],
            remainder_qualification=aux['remainder'],whole_chain_new_PASS=False,new_behavior_execution=0))
    write('junction-dispositions.json',{'classification':'BOUNDED_FINAL_CONSUMER_PROJECTIONS_AND_OLD_SCOPE_RETENTION','count':14,
        'final_input':{'commit':INPUT,'tree':TREE},'independent_review':'subreviews/legacy-junctions.json',
        'records':junctions,
        'final_judgment':'Affected projections are consistent with fixed final bytes; original supported/partial/not_reviewed/material restrictions unchanged; J08/J09 reused, not reexecuted; no 14 or 80 fresh whole-chain PASS',
        'guards':['J11 Area support does not certify new ordinary appearance','J13 acquisition/partial commit does not certify Pokedex refresh','J07 refund does not certify PP eligibility','J14 static connection is not Demo execution']})
    historical_path='review/global-independent-review/fourth-2026-10-12-1f36475-c92e/execution-evidence.json'
    historical=json.loads(git('show','417e99d4eab78c512b6b002db2a67eadefbee7e7:'+historical_path))
    exec_records=[]
    for i,r in enumerate(historical['reference_probe_runs']):
        data=r['record']
        exec_records.append({'origin_module':r['origin_module'],'original_identity':identity(historical_path,'417e99d4eab78c512b6b002db2a67eadefbee7e7'),
            'original_pointer':'/reference_probe_runs/'+str(i),'module_artifact':r['artifact'],'module_pointer':r['pointer'],
            'version':data['version'],'inputs':data.get('inputs',data.get('input')),
            'limits':data.get('limits',data.get('limitations')),'side_effects':data['side_effects'],
            'status':'HISTORICAL_EXECUTED_REFERENCE_REUSED_NOT_RERUN','is_new_execution':False})
    write('execution-and-limits.json',{'historical_fourth_review':{'EXECUTED_REFERENCE':4,'M01':1,'M02':2,'M12_rating_settlement':1,'records':exec_records,'record_count_not_case_count':True},
        'this_final_review':{'EXECUTED_REFERENCE':0,'EXECUTED_MODEL':0,'EXECUTED_HOST_OR_DEMO':0,'status':'NOT_EXECUTED_THIS_UPDATE'},
        'evidence_levels':{'SOURCE_STATIC':'Prior exact signed source facts reused; no global reread','SPEC_STATIC':'Current fixed clauses and final affected consumers','DERIVED_VECTOR':'NOT_EXECUTED','TOOL_VALIDATION':'Git/JSON/bytes/identity and remote readback only','runtime_criteria':'Evidence boundary compliance, never runtime PASS'},
        'retained_limits':load(PACK+'execution-and-limits.json'),
        'retained_old_qualifications':'GR3 CLOSED23; original229 and exact341 scope/owner/tuple not enlarged; 341 contributions are not features; optional/U08 and NO_REQUIRED_REVISION remain unchanged'})
    root_full=[PACK+'final-review-task.md',PACK+'README.md',PACK+'review-recommendation.md',PREFIX+'registration/ownership.md','AGENTS.md']
    root_full += [PREFIX+f'batches/R4-U0{i}/review/actual-v1/report.md' for i in range(1,6)]
    task_files=validation['checks']['task_packets']
    root_projection_paths=['generic-kernel/wp08-localization.md','user-interface/wp17-draw-text-tags.md','user-interface/wp17-messages-windows-input.md',
        'user-interface/wp66-c-bag-item-storage-and-shop-ui.md','user-interface/wp67-a-battle-interaction-and-presentation.md',
        'engine-overworld/wp13-interpreter-command-matrix.md','engine-overworld/wp11-map-topology-transfer.md','engine-overworld/wp59-world-time-weather-field-moves.md',
        'engine-overworld/wp16-world-rendering-and-visual-transitions.md','pokemon-rules/wp61-field-passive-effects-and-blackout.md',
        'creature-rpg/wp36-wild-encounters-and-modifiers.md','generic-kernel/wp04-pbs-lifecycle.md','demo-dx/wp73-b-world-editors.md',
        'creature-rpg/wp28-item-use-and-training.md','user-interface/wp66-b-storage-and-pokedex-ui.md','pokemon-rules/wp62-pokedex-records-regions-and-content.md']
    write('read-ledger.json',{'policy':'Full team semantic reads of assigned packet records and necessary evidence; root reviews current controls and all auxiliary conclusions; metadata full-byte validation is separate from semantic signing',
        'root_complete_semantic_reads':[dict(identity(p,TASK),read_mode='FULL_TEXT') for p in root_full],
        'all_u06_packets_full_bytes_and_JSON_parsed':task_files,
        'root_packet_semantic_mode':'17/76 original preconditions/counterexamples/criteria and 14 normal/failure/cancel/repeat/prefix controls consumed in structured projections; full unique detailed records delegated to the named auxiliary reviewers; repeated identity rows mechanically checked, not whole-file new semantic signatures',
        'root_current_consumer_clause_reads':[dict(identity('deliverables/final-specification-set/'+p,INPUT),read_mode='NAMED_CLAUSES_AND_BOUNDED_SEARCH; not full-file semantic PASS') for p in root_projection_paths],
        'root_historical_execution_read':dict(identity(historical_path,'417e99d4eab78c512b6b002db2a67eadefbee7e7'),read_mode='All four reference_probe_runs records read; other tool entries not behavior signed'),
        'independent_auxiliary_complete_notes':[dict(identity(OUT+'subreviews/'+n),read_mode='COMPLETE_JSON_BYTES_CONSUMED; final reviewer semantically read all criteria/conclusions/control projections; repeated identities programmatically checked') for n in note_names],
        'auxiliary_source_read_ledgers':{n:'subreviews/'+n for n in note_names},
        'formal131_full_byte_verification':'input-validation.json','historical_qualified_reuse_details':'subreviews/identities-gates.json and subreviews/legacy-junctions.json',
        'historical_direct_fetch_scope':['Fixed final input and task publication','Fixed original fourth report417e99d4 for necessary ledgers/4execution records'],
        'absent_historical_candidate_actual_trees':'Not re-downloaded; exact signed original comparison/tuple and full inherited payload identity reused, never falsely marked fresh tree reads',
        'all_reexecutions':0})
    write('validation-result.json',{'status':'PASS_TOOL_IDENTITIES_AND_FINAL_SCOPE','semantic_verdict':'FINAL_PASS_SCOPED','evidence_level':'TOOL_VALIDATION',
        'identity_result':'input-validation.json','auxiliary_results':note_names,'findings':17,'criteria':76,'formal':131,'amended':28,'unchanged_B':103,
        'entry_dependencies_met':5,'handshakes_scoped_pass':4,'old_junction_dispositions':14,'shared_single_owners':25,
        'GR3_CLOSED_preserved':23,'old_qualified_objects':229,'exact_owner_contributions':341,
        'new_mandatory_conflicts':[],'reviewer_acceptance_writes':[],'reviewer_closure_writes':[],'new_behavior_execution':0,
        'publication_status':'Successor publication-readback.json and externally returned final commit/tree; not self-embedded',
        'errors':[]})
    rows='\n'.join('| '+r['id']+' | '+r['batch']+' | '+str(r['criteria_count'])+'/'+str(r['criteria_count'])+' | FINAL_PASS_SCOPED | '+RATIONALE[r['id']]+' |' for r in packet['records'])
    report='''# R4-U06 独立最终组合复审

**FINAL_PASS_SCOPED。17项、76个当前标准、五个进入门及四条最终握手均在本固定输入的限定范围内满足；没有剩余必修矛盾或整改阻塞。17项具备交唯一登记员办理有限关闭的资格，当前仍是ACCEPTED_SCOPED17、CLOSED0。本reviewer未登记接受或关闭。**

判定绑定最终输入 `'''+INPUT+'''` / tree `'''+TREE+'''`；任务发布 `'''+TASK+'''` / tree `'''+TASK_TREE+'''`。正式子树 `d5a462b4c6f8b78c3264a25d6b5495230fa265e2`，131完整身份为28已接受整改/103不变B，owner数量U01=4、U02=8、U03=12、U04=2、U05=2。固定最终输入与任务发布的正式字节完全相同。此为精确身份分区，不是131篇或全部功能的新语义签署。

独立角色R4-U06-final-reviewer，实际thread `'''+REVIEWER_THREAD+'''` 来自单一CODEX_THREAD_ID回显，已核不同于五位原作者、五位原actual审者及派发父thread；本次只写 `'''+OUT+'''`，分支 `'''+BRANCH+'''`。五位原作者及唯一登记员不由本角色承担。source_thread_id是派发父身份，没有冒充审者。请求sol/ultra/Standard（合同default）/Fast=false，实际模型、推理、档位及Fast回显UNVERIFIED；未审计后台、额度或凭据。`.agents/skills`在本工作区和发布树不存在；AGENTS.md已读并遵守只读参考及clean-room要求。

## 逐项与逐标准

| Finding | 唯一批次 | 当前标准 | 最终裁决 | 组合判断 |
| --- | --- | --- | --- | --- |
'''+rows+'''

全部76完整标准、原actual独立证据pointer和限定复用/新增组合依据见 [criteria-results.json](criteria-results.json)，17原背景、精确链、当前正式身份及逐项关闭资格见 [findings.json](findings.json)。Runtime及optional执行标准的通过仅表示证据边界合规。原B问题描述是冻结历史背景；旧v1的REQUIRES_CHANGES及修复过程保原字节，不把它们再算当前未决。

## 最终组合结论

这次不是五份PASS的加总。对全部五批并置后的当前正文，另外检查正常、失败、取消、重复和已提交前缀，完整判断在 [dependencies-handshakes.json](dependencies-handshakes.json)：

- H01：WP08先返回字符串，WP17再布局/显示。A B在给定测量下宽22/21一行/移B；反斜线1先删除不会生成显示暂停。命令、数字、数量、商店、命名各有入口顺序，取消不统归一个规则。
- H02：失败上水已写冲浪/统计/基点，转移、载具取消和新UI没有独立临时清理。SF04水域通知仅清旧基点，SF06陆地才上岸收尾；ending真阻通常201，微更新与正常解释器机会分层。稳定C064不扩大为残留/真实像素已证。
- H03：HP0主动PP拒绝在登记扣减前，留成员循环；类型2取消选招回成员。场外成功补PP但不复活，每次1。登记后复检/退款残留保J07资格，不能把J07退款签名当HP资格证明，也不以普通数字/商店次序改变物品业务。
- H04：整集空类型Copy在登记阶段滤空但保率/后缀，单类型Copy保空条目；PBS省略是后续写出。No依原档案正常重载，保存/Compile/同版本/调试包装不装配当前快照；真实异值且合法上下文才装配，不推实际遇敌或一步开战。

五进入门均由精确actual独立报告及唯一接受回执满足。候选→独立候选→actual→独立actual→唯一接受全链的当前载荷完整核验，历史树未在浅仓库的部分依已签未变identity/publication精确tuple复用，详 [身份与门子审](subreviews/identities-gates.json)。没有声称重新下载/读取缺席历史树。原25共享契约各有唯一primary owner；公共提案和反向引用没有剩余实际必修，来源追溯在新不可变作者/独立证据中，可选导航锚点不增新写者或整改。

## 旧链与旧资格

14条逐去向及normal/failure/cancel/repeat/prefix边界见 [junction-dispositions.json](junction-dispositions.json)、[独立旧链子审](subreviews/legacy-junctions.json)。J01–07、J10–14仅核受影响consumer projection；J08/J09保原immutable qualified scope/not_reexecuted。原supported/partial、not_reviewed及材料限制均保留，不把14/80条全部改成新PASS。J11 Area不覆盖M11普通外观，J13获得/部分提交不覆盖图鉴刷新，J07退款不覆盖PP资格，J14静态新游戏链不是Demo运行。

旧GR3保持23 CLOSED；A013翻译头/完整入口先截断、A053动态孵化、C064稳定显示、数量/命名、116辅助/恢复、探测仪/退款和CV/GN保护按原精确scope复用并有限核受影响交界。5份保护全文及42条具名旧测试行与B相同；GR3-MR12是本轮为三入口/116明确边界而改写，单列有限澄清，不误报其字节未变；MR01–11/13保持原字节。原229逐qualified对象与341 candidate/actual/独立报告/owner贡献元组锚定不变，一个贡献不代表全部owner，341不是功能数。没有重开、补签或把静态资格改成执行；GR3-M09-001 OPTIONAL/U08 NOT_STARTED及GR3-M02-003 NO_REQUIRED_REVISION仍保原状态。

## 执行与限制

历史第四review确有4条隔离EXECUTED_REFERENCE：M01本地化×1、M02 HTTP/墙钟×2、M12评级结算×1；原Ruby2.6.10、输入、版本、nil/empty/常量、时钟/地图/网络替身及初始化限制保留。M02首轮安全字符串键也FrozenError的记录保留；M12评级没有执行遭遇Copy。本次新增参考/模型/宿主/Demo行为执行均0，NOT_EXECUTED_THIS_UPDATE。详情见 [execution-and-limits.json](execution-and-limits.json)。

SOURCE_STATIC复用、当前SPEC_STATIC、DERIVED_VECTOR未执行及TOOL_VALIDATION身份/读回分列。字体实测、真实物理输入、像素、动画播放、网络、真实存档、完整地图/资源/宿主/Demo仍未验证；原300重叠能力记录、131身份/责任及旧229/341都不是全部能力完备证明。未来兼容政策、补材料与旧optional事项不阻塞本次限定事实整改，仍未代选。没有实现引擎、翻译Ruby源码、修改参考或正式规格。

## 交付与关闭资格

本范围必须整改/技术阻塞：无。全部17具备唯一登记员有限关闭资格，条件是登记员接受本精确发布报告及身份回执后另发接受/关闭回执；本reviewer不把CLOSED0自行改为17。其后组织、合main或清理均不在本次行为中。

复审阅读、未变复用和机械验证范围分别在 [read-ledger.json](read-ledger.json)、[identity.json](identity.json)、[input-validation.json](input-validation.json)、[validation-result.json](validation-result.json)；五份辅助完整证据置于subreviews，最终签名由本reviewer作出。报告普通推送独立分支；后继 [publication-readback.json](publication-readback.json)绑定首份报告commit/tree并从origin独立对象库完整读回每份实际交付载荷，含回执的最终提交再完整读回，最终commit/tree由外部回应给出，避免递归自嵌。131未变正式身份沿精确子树及已核未变证据复用。
'''
    (HERE/'report.md').write_text(report)
    print(json.dumps({'assembled_findings':len(findings),'criteria':len(criteria),'boundary_only':sum(c['pass_meaning']=='EVIDENCE_BOUNDARY_COMPLIANCE_ONLY' for c in criteria),'notes':note_names,'verdict':'FINAL_PASS_SCOPED'}))

if __name__=='__main__':main()
