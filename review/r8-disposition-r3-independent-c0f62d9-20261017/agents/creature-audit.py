"""Independent static creature R3 reconciliation; no author or business execution."""
import ast, collections, copy, datetime, hashlib, json, pathlib, re, subprocess

C='c0f62d973180679134f2eb1a488c1dc359c8658f'
R2C='a32873d2860b15d9f5e27727db8f131f4ec433b6'
R2R='0ef0b7ad5f9465cfe31da0d7a35f56b5ccba5add'
A='5f87743293290de2e219ecdd6c19e88280f60c9a'
OLD_A='908273093e1f6b27fc58249417675dd62d146224'
B8='fd1df570cad987dc3852a3b958f03916e317f7fe'
P='planning/implementation-routing/r8-20261017/'
RP='review/r8-disposition-r2-independent-a32873d-20261017/'
BASE='deliverables/final-specification-set/'
OUT=pathlib.Path(__file__).parent
commands=[]
def sha(b): return hashlib.sha256(b).hexdigest()
def git(*args):
    t=datetime.datetime.now(datetime.timezone.utc).isoformat()
    q=subprocess.run(['git',*args],capture_output=True)
    commands.append(dict(argv=['git',*args],start_utc=t,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),exit_code=q.returncode,stdout_bytes=len(q.stdout),stdout_sha256=sha(q.stdout),stderr=q.stderr.decode()))
    q.check_returncode();return q.stdout
cache={}
def read(p,c=C):
    if (c,p) not in cache: cache[c,p]=git('show',c+':'+p)
    return cache[c,p]
def js(p,c=C): return json.loads(read(p,c))
def ident(p,c):
    b=read(p,c)
    return dict(commit=c,path=p,bytes=len(b),sha256=sha(b),git_blob=git('rev-parse',c+':'+p).decode().strip(),lines=len(b.splitlines()))
def fid(n): return f'FR-{n:06d}'
def unit(row,c):
    lines=read(row['source']['document'],c).splitlines(keepends=True)
    return b''.join(b''.join(lines[a-1:b]) for a,b in row['current_applicability']['locator']['line_ranges'])
def projection_superset(g,l): return all(g.get(k)==v for k,v in l.items())

inputs={}
entry_inputs=[]
for path,c in [('AGENTS.md',C),(P+'review-prompt.md',C),(P+'revisions/r3/README.md',C),('review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/inputs/review-SKILL.md','4575e80d041ab0c74a42e2e36399d05791dbaa5b'),('review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/cloud-eighth-update-handoff-prompt.md','4575e80d041ab0c74a42e2e36399d05791dbaa5b'),('review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/cloud-eighth-update-handoff-manifest.json','4575e80d041ab0c74a42e2e36399d05791dbaa5b')]:
    b=read(path,c)
    entry_inputs.append(dict(path=path,commit=c,sha256=sha(b),bytes=len(b),consumption='FULL_STRUCTURED_PARSE' if path.endswith('.json') else 'FULL_PROSE_READ'))
    if path.endswith('.json'):json.loads(b)
for n in ['REPORT.md','findings.json','feature-results.json','finding-results.json','issue-results.json','reading-coverage.json','section-results.json','agents/creature-report.md','agents/creature-results.json','agents/creature-dependency-crosscheck.json','agents/creature-evidence.json','agents/creature-audit.py','agents/creature-dependency-crosscheck.py']:
    b=read(RP+n,R2R)
    local=pathlib.Path('/workspace/r8-disposition-r2-review')/RP/n
    assert b==local.read_bytes(),n
    inputs[n]=dict(commit=R2R,path=RP+n,bytes=len(b),sha256=sha(b),physical_tree_equal_fixed_git=True,consumption='FULL_STRUCTURED_PARSE_AND_ALLOCATED_PROJECTION_RECONCILIATION' if n.endswith('.json') else ('FULL_PROSE_READ' if n.endswith('.md') else 'FULL_STATIC_SOURCE_PARSE'))
    if n.endswith('.json'): inputs[n]['parsed']=json.loads(b)
    if n.endswith('.py'): ast.parse(b)
r=inputs['agents/creature-results.json']['parsed']
cross=inputs['agents/creature-dependency-crosscheck.json']['parsed']
ids=[x['feature_id'] for x in r['active_feature_results']]
primary=[x['path'] for x in r['reading_ledger']]
assert len(ids)==122 and len(primary)==18 and len(r['old_feature_results'])==116
root=inputs['feature-results.json']['parsed'];ra={x['feature_id']:x for x in root['active_feature_results']};ro={x['feature_id']:x for x in root['old_feature_results']}
assert all(projection_superset(ra[x['feature_id']],x) for x in r['active_feature_results'])
assert all(projection_superset(ro[x['feature_id']],x) for x in r['old_feature_results'])
rg={x['finding_id']:x for x in inputs['finding-results.json']['parsed']['finding_results']}
assert all(projection_superset(rg[x['finding_id']],x) for x in r['original_group_results'])
ri={x['issue_id']:x for x in inputs['issue-results.json']['parsed']['issue_results']}
assert projection_superset(ri['R1-CRE-DEP-001'],r['issue_results'][0])
rf={x.get('finding_id',x.get('id')):x for x in inputs['findings.json']['parsed']['findings']}
assert all(rf[x['finding_id']]['cases']==x['cases'] for x in r['new_findings'])
rr={x['path']:x for x in inputs['reading-coverage.json']['parsed']['documents']}
assert all(rr[x['path']]['current_identity']['sha256']==x['sha256'] for x in r['reading_ledger'])
rs=inputs['section-results.json']['parsed']['sections']
assert len(rs)==2683 and len(inputs['section-results.json']['parsed']['catalog_and_metadata_results'])==424

objects=[]
for c in [C,R2C,R2R,A,OLD_A,B8,'d62b41f4d620e50bb04c80a7505374bd284d8210','a0352c7fba38391afc535525988245701d5ce202','5666b7b912e2fb79b5119283ee6a37401a7071db','8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8','4575e80d041ab0c74a42e2e36399d05791dbaa5b','8336249c78b4698cd77445653d3b05ff6a76ce94']:
    objects.append(dict(commit=c,resolved=git('rev-parse',c+'^{commit}').decode().strip(),type=git('cat-file','-t',c).decode().strip()))
assert git('rev-parse',A+':deliverables/final-specification-set').decode().strip()=='93dc967b4cdb653359afc123d3b8b318d6475fdd'
m=js(P+'routing-manifest.json');om=js(P+'routing-manifest.json',R2C)
f={x['feature_id']:x for x in m['features']};of={x['feature_id']:x for x in om['features']}
prior={x['feature_id']:x for x in r['active_feature_results']}
sc=js(P+'current-section-coverage.json');hist=js(P+'section-coverage.json')
assert len(sc['sections'])==2704 and len(hist['sections'])==2683
assert read(P+'section-coverage.json')==read(P+'section-coverage.json',R2C)
changed_fields={i:[k for k in set(f[i])|set(of[i]) if f[i].get(k)!=of[i].get(k)] for i in ids}
assert all(f[i]['source']==of[i]['source'] for i in ids)
assert all(f[i]['future_plan']==of[i]['future_plan'] for i in ids)
assert all(f[i]['functional_scope']==of[i]['functional_scope'] for i in ids)

fresh={
'creature-rpg/wp18-creature-identity-species-ownership.md':[[47,163]],
'creature-rpg/wp20-hp-status-moves-helditem.md':[[46,82],[121,205]],
'creature-rpg/wp24-player-trainers-partners.md':[[89,229]],
'creature-rpg/wp26-acquisition-gifts-and-script-trade.md':[[122,142]],
'creature-rpg/wp27-bag-and-item-storage.md':[[45,105]],
'creature-rpg/wp28-item-use-and-training.md':[[112,122],[174,226],[276,294]],
'creature-rpg/wp30-growth-learning-and-friendship.md':[[79,126],[155,159]],
'creature-rpg/wp33-daycare-and-breeding-session.md':[[107,158]],
'creature-rpg/wp36-wild-encounters-and-modifiers.md':[[115,161]],
'creature-rpg/wp64-mail-and-mystery-gift.md':[[84,157]],
'test-catalog/creature-rpg-wp35-36-57-64-68.md':[[110,128]],
'generic-kernel/wp03-content-identity-and-schema.md':[[313,338]],
'generic-kernel/wp06-stats-directory.md':[[73,103]],
'user-interface/wp17-messages-windows-input.md':[[186,199]],
'combat-requirements/wp39-battle-context-and-participants.md':[[47,211],[276,294]],
'combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md':[[59,96],[166,250]],
'combat-requirements/wp45-weather-terrain-side-and-position-effects.md':[[102,177]],
'combat-requirements/wp58-battle-recording-and-playback.md':[[1,14],[144,165]],
'engine-overworld/wp12-terrain-movement-vehicles.md':[[92,186]],
'pokemon-rules/wp19-attributes-ability-and-stats.md':[[126,240]],
'pokemon-rules/wp34-inheritance-and-offspring.md':[[22,51]],
'pokemon-rules/wp50-held-item-triggers-and-consumption.md':[[153,170]],
'pokemon-rules/wp61-field-passive-effects-and-blackout.md':[[22,57]],
'demo-dx/wp73-a-content-editors.md':[[77,169],[177,192]],
'test-catalog/combat-requirements-wp39-40-41-42-45.md':[[299,317]],
'test-catalog/pokemon-rules-wp19-21-22-23-34.md':[[344,356]],
}
fresh={BASE+k:v for k,v in fresh.items()}
reading=[];extra=[];diffs=[]
for x in r['reading_ledger']:
    p=x['path'];oldid=ident(p,OLD_A);newid=ident(p,A)
    assert oldid['sha256']==x['sha256']
    patch=git('diff',OLD_A,A,'--',p)
    if patch: diffs.append(dict(path=p,sha256=sha(patch),bytes=len(patch),text=patch.decode()))
    reading.append(dict(path=p,primary_document=True,historical_identity=oldid,current_identity=newid,source_identity=ident(p,B8),fresh_ranges=fresh.get(p,[]),new_semantic_read_ranges=fresh.get(p,[]),full_diff_freshly_read=bool(patch),prior_credit=dict(commit=R2R,path=RP+'agents/creature-results.json',pointer='/reading_ledger/'+str(r['reading_ledger'].index(x)),record=x),inheritance_scope='Only unchanged effective clauses/facets; changed clauses and every nonPASS/same-root source scope freshly read as listed. Changed-file credit is segment-bound, not whole-file identity.',limitation='No claim of 18 fresh full reads; structured parse, byte comparison and semantic reading remain separate.'))
for p,ran in fresh.items():
    if p not in primary: extra.append(dict(path=p,commit=A,identity=ident(p,A),fresh_ranges=ran,new_semantic_read_ranges=ran,role='SUPPLEMENTARY_CONSUMER_NOT_PRIMARY_COUNT'))
assert len(diffs)==6

repair_reasons={
(186,31):'WP28 §3.5 L117保留已退款物品身份；最终WP42 §6 L177及§6.0 L183–191在普通共同终局再次消费该身份并清选择，FR31真实拥有该阶段。',
(190,31):'主动药品沿§3.5登记/执行及退款；FR31正常终局消费残留物品身份。已去掉外层伙伴全队治疗32，不把它当主动药品治疗。',
(192,39):'WP28 L282 GUARDSPEC同种正值拒绝、成功设Mist5；最终WP45 §6.2 L127准确拥有五回合建立与侧计时递减，FR39是实际状态规则。',
(741,420):'WP24 §4.4 L139–140按钱包实际增/减累计；WP06 stats §6 L82–83真实字段battle_money_gained/lost由FR420拥有，§7货币421仅商店/币/BP/煤灰。',
}
removed={(186,32):(186,31),(190,32):(190,31),(192,40):(192,39),(741,421):(741,420)}
oldedges={(x['source_feature_id'],x['target_feature_id']):x for x in cross['edges']}
current_pairs={(i,t) for i in ids for t in f[i]['dependencies']['feature_refs']}
assert len(oldedges)==57 and len(current_pairs)==55
assert len({i for i,t in current_pairs})==17
edges=[];oldedge_results=[];target_ids={t for s,t in current_pairs}
changed_target_ids=[]
for t in sorted(target_ids):
    if unit(f[t],A)!=unit(of[t],OLD_A):changed_target_ids.append(t)
for s,t in sorted(current_pairs):
    key=(int(s[3:]),int(t[3:]));prev=oldedges.get((s,t))
    assert prev is not None or key in repair_reasons
    reason=repair_reasons.get(key,prev['limited_actual_use'] if prev else '')
    if prev: assert prev['verdict']=='PASS'
    target=f[t];src=f[s]
    edges.append(dict(source_feature_id=s,target_feature_id=t,r2_verdict=prev['verdict'] if prev else 'NEW_REPLACEMENT',verdict='PASS',candidate_pointer='/features/'+str(m['features'].index(src))+'/dependencies/feature_refs/'+str(src['dependencies']['feature_refs'].index(t)),source_document=src['source']['document'],source_current_ranges=src['current_applicability']['locator']['line_ranges'],target_document=target['source']['document'],target_current_ranges=target['current_applicability']['locator']['line_ranges'],target_excluded_child_refs=target['functional_scope']['excluded_child_refs'],target_current_unit_sha256=sha(unit(target,A)),target_effective_bytes_equal_r2=unit(target,A)==unit(of[t],OLD_A),target_fresh_ranges=fresh.get(target['source']['document'],[]),reason=reason,current_reassessment='Every surviving edge actual use retained after full own R2 edge parse and current source-scope review. Changed target scopes 1/2/29/32/204/330/596 freshly read. 39/420 new replacements freshly read. Unaffected target full-body credit remains bound to fixed R2 current unit identity.',explicit_indirect_navigation=({'FR-000579':['FR-000755'],'FR-000147':['FR-000739']}.get(t,[])),finding_refs=[]))
for (s,t),x in oldedges.items():
    ns,nt=int(s[3:]),int(t[3:]);k=(ns,nt)
    if (s,t) in current_pairs: status='RETAINED_ACTUAL_USE';replacement=t;reason=next(y['reason'] for y in edges if y['source_feature_id']==s and y['target_feature_id']==t)
    elif k in removed: status='REPLACED_WRONG_TARGET';replacement=fid(removed[k][1]);reason=repair_reasons[removed[k]]
    else:
        assert k in {(244,263),(244,265)}
        status='REMOVED_WRONG_TOOL_FAMILY';replacement=None;reason='GiftMaster/current-session/Export/manual-online独立四层与WP73-A六类PBS编辑/取消不是同一调用；删除该边正确。742真实训练家新建共享263/265仍保留。'
    oldedge_results.append(dict(source_feature_id=s,r2_target_feature_id=t,r2_verdict=x['verdict'],current_state=status,replacement_target=replacement,verdict='PASS',reason=reason))

cal_reasons={fid(173):'当前WP26 §5 L138改为录像记录战斗的收服存储为空操作，并明确回放另按WP58 §6.2–6.4分层；本行differences/1却声称神秘礼物ESC命名变化。该事实属于244/WP64，未描述173的当前源差分。',fid(227):'当前WP36 §4.2 L132新增负概率前缀、负累加器向下整除及不钳零；本行differences/1却称Repel比较成员差别。Repel配置选择在B8/908的L143已经存在，不能作为此次当前变源校准。'}
cal_reasons[fid(204)]='当前WP19§5.3 L174/178的正常模板HP255/攻击255合计510，并未超EV总量；FR204 differences/1却称“设施模板超EV总量…”。实际首失败来自HP单项超过252、单项余量上界−3；此时尚未检查总量夹限。'
delta_reasons={fid(137):'15精确蛋群作者值、未登记拒绝和基础默认/形态克隆由WP03§6.2共同定义；物种字段与内容身份仍为框架输入合同，不把目录校验当繁殖可行性。',fid(173):cal_reasons[fid(173)],fid(204):'普通非Shadow EV首项反向区间失败在当前WP30 L122与WP19 L178–180/WP42 L73一致；接收者EV/经验未写与早先回调/接收者前缀分开，非内部设施早门保留，协作粗标足够。',fid(227):cal_reasons[fid(227)],fid(244):'当前WP64 L127–128的ESC非空原名成功/空文停止与共享对象前缀，MG32三对照保留；框架载体/共享状态及MZ输入/确认职责已经覆盖，不需要新功能ID。'}
active=[]
for i in ids:
    x=f[i];p=prior[i];cal='FAIL' if i in cal_reasons else 'PASS';changed=unit(x,A)!=unit(of[i],OLD_A)
    assert sha(unit(x,A))==x['current_applicability']['locator']['unit_sha256'],i
    assert sha(read(x['source']['document'],A))==x['current_applicability']['locator']['file_sha256'],i
    reason=cal_reasons.get(i,delta_reasons.get(i,p['reason']))
    if i in {fid(n) for n in [186,190,192,741]}:reason='R2错误依赖已逐有效源/目标新读并正确替换；详dependency_edge_results。'
    if i==fid(244):reason=delta_reasons[i]+' R2错族263/265边已删，241/243实际载体/领取调用仍保留。'
    affected_targets=[t for s,t in current_pairs if s==i and (t in changed_target_ids or (int(s[3:]),int(t[3:])) in repair_reasons)]
    active.append(dict(feature_id=i,r2_verdict=p['verdict'],verdict=cal,classification='PASS',responsibility='PASS',scope='PASS',dependency='PASS',current_calibration=cal,classification_semantics='PASS',responsibility_semantics='PASS',scope_semantics='PASS',dependency_semantics='PASS',current_calibration_semantics=cal,candidate_pointer='/features/'+str(m['features'].index(x)),reason=reason,method='FRESH_AFFECTED_EFFECTIVE_SOURCE_AND_DEPENDENCY_REVIEW' if changed or affected_targets or p['verdict']=='FAIL' or x['dependencies']['feature_refs'] else 'IDENTITY_BOUND_UNAFFECTED_R2_FACET_CREDIT_WITH_DEPENDENCY_NONIMPACT_CHECK',source=x['source'],functional_scope=x['functional_scope'],current_applicability=x['current_applicability'],r2_current_unit_equal=not changed,r2_future_plan_equal=True,r2_dependencies_equal=x['dependencies']==of[i]['dependencies'],affected_fields=changed_fields[i],fresh_source_ranges=fresh.get(x['source']['document'],[]),affected_target_ids=sorted(affected_targets),inheritance_evidence=dict(commit=R2R,path=RP+'agents/creature-results.json',pointer='/active_feature_results/'+str(r['active_feature_results'].index(p)),reason='Source IDs/B8 body and future plan/scope preserved independently. Only exact unchanged effective clauses and unaffected facets inherit; all57 old edge cases reconciled,55 current actual uses individually reviewed. Byte equality alone is never overall semanticPASS.'),destination_verification='待验证',stage_approval='未批准',implementation='未实现',target_acceptance='未验收',finding_refs=['R3-CRE-CAL-001'] if cal=='FAIL' else []))
old_results=[];ar={x['feature_id']:x for x in active}
for x in r['old_feature_results']:
    a=ar[x['feature_id']]
    old_results.append(dict(feature_id=x['feature_id'],r2_verdict=x['new_verdict'],new_verdict=a['verdict'],verdict=a['verdict'],active=True,disposition='active',current_state='ACTIVE',reason=a['reason'],method=a['method'],finding_refs=a['finding_refs']))

groups=[]
for x in r['original_group_results']:
    y=copy.deepcopy(x);y['r2_verdict']=x['new_verdict'];y['new_verdict']='PASS';y['verdict']='PASS';y['original_case_verdict']='PASS';y['current_scope_verdict']='PASS';y['reason']='All original cases retained/rechecked. CK-DEP exact13 cases and R2 extra244/741 repaired and all current55 edges PASS. New173/204/227 annotation calibration is separately reported and is not an invented failure of unrelated original case.'
    for z in y.get('all_original_cases',[])+y.get('new_related_features',[]):
        z['r2_verdict']=z.get('verdict','PASS');z['verdict']='PASS'
        case_id=z.get('feature_id',z.get('new_feature_id',z.get('old_feature_id')))
        if case_id in ar: z['reason']=ar[case_id]['reason'];z['finding_refs']=ar[case_id]['finding_refs']
    y['same_root_affected_PASS_evidence']='Full17-row57-old/55-current edge reconciliation; source137/173/204/227/244 + all changed target uses reviewed, R3-SOURCE-ATTRIBUTION-001 andR3-EV-BOUNDARY-001 separately assigned current-calibration facet.'
    groups.append(y)
issues=[]
for idd,caseids in [('R2-CRE-DEP-001',[186,190,192]),('R2-CRE-DEP-002',[244,741]),('R1-CRE-DEP-001',[155,157,158,186,190,191,192])]:
    issues.append(dict(issue_id=idd,r2_verdict='FAIL',verdict='PASS',all_cases=[dict(feature_id=fid(n),verdict='PASS',reason=ar[fid(n)]['reason']) for n in caseids],same_root_propagation_checked=True,same_root_affected_ids=[fid(n) for n in [147,153,154,155,157,158,186,187,190,191,192,204,207,244,723,739,740,741,742]],current_feature_ref_edges=55,original_edge_results=57,finding_refs=[]))
sections=[]
secidx={(s['path'],s['anchor']):s for s in sc['sections']}
for x in r['section_metadata_results']:
    source_hist=hist['sections'][int(x['candidate_pointer'].split('/')[-1])]
    s=secidx[(x['path'],source_hist['anchor'])]
    sections.append(dict(path=x['path'],title=s['title'],anchor=s['anchor'],r2_verdict=x['verdict'],verdict='PASS',current_ranges=[[s['line_start'],s['line_end']]],consumer_feature_refs=s['feature_refs'],metadata_refs=s['metadata_refs'],reason='Existing body/catalog/governance navigation remains actual. ChangedMG32 maps to244 Gift tool, notPBS; current source annotations173/227 are separate feature calibration failures and do not invalidate these real consumer mappings.',method='FULL_R2_RECORD_PARSE_CURRENT_ANCHOR_CONSUMER_RECONCILIATION_AND_AFFECTED_CLAUSE_READ',finding_refs=[]))
assert len(sections)==158

headings=[]
for x in js(P+'revisions/r3/new-heading-mappings.json')['accepted_mappings']:
    relevant=sorted(set(x['feature_refs'])&set(ids))
    if not relevant:continue
    b=read(x['document'],A);lines=b.splitlines(keepends=True);a,z=x['line_ranges'][0];si=x['source_identity']
    assert sha(b)==si['file_sha256'] and sha(b''.join(lines[a-1:z]))==si['unit_sha256']
    assert sha(x['title'].encode())==si['heading_sha256'] and sha(lines[a-1])==si['raw_markdown_heading_sha256']
    headings.append(dict(document=x['document'],anchor=x['anchor'],title=x['title'],current_ranges=x['line_ranges'],allocated_primary_owner=False,review_role='SUPPLEMENTARY_CREATURE_CONSUMER_CROSSCHECK_NOT_DUPLICATE_HEADING_OWNER',creature_consumer_ids=relevant,all_declared_consumer_ids=x['feature_refs'],verdict='PASS',source_identity=si,reason='EggGroups directory137/214 actual species/default/breeding gate consumers; EV catalog204 actual ordinary nonShadow receiver failure consumer. Existing domain owners own heading results; no new function required.'))
assert len(headings)==3
changedsource=[]
for d in diffs:
    p=d['path'];units=[i for i in ids if f[i]['source']['document']==p and unit(f[i],A)!=unit(of[i],OLD_A)]
    changedsource.append(dict(document=p,r2_current_identity=ident(p,OLD_A),current_identity=ident(p,A),complete_diff_sha256=d['sha256'],changed_effective_feature_ids=units,source_acceptance_verdict='ROOT_RECEIPT_AUDIT_SEPARATE',source_to_routing_calibration_verdict='FAIL' if set(units)&set(cal_reasons) else 'PASS',category_responsibility_scope_verdict='PASS',source_fact_reason='; '.join(delta_reasons[i] for i in units) if units else 'MG32 preserves Gift editing static RETURN/ESC/stop-confirm distinctions and prior alias prefixes; existing244 is correct catalog consumer.',fresh_effective_ranges=fresh.get(p,[]),finding_refs=['R3-CRE-CAL-001'] if set(units)&set(cal_reasons) else []))

finding=dict(finding_id='R3-CRE-CAL-001',severity='P3',verdict='FAIL',facet='current_calibration',title='Two current-source change annotations describe a different or pre-existing behavior',candidate_commit=C,current_source_commit=A,candidate_path=P+'routing-manifest.json',feature_ids=[fid(173),fid(227)],cases=[
dict(feature_id=fid(173),candidate_pointer='/features/161/differences/1',source_document=f[fid(173)]['source']['document'],source_effective_ranges=[[122,142]],changed_effective_ranges=[[138,138]],source_identity=ident(f[fid(173)]['source']['document'],A),actual_fact='Recording-battle capture storage is a no-op; replay is separately governed by WP58§6.2–6.4 copy/live dependencies and normal-end/abort contracts.',candidate_fact='Claims Mystery Gift ESC original-name/empty-stop refinement.',distinguishing_counterexample='A replay with a player-side consumedPOTION can debit live bag and normal end can run ordinary terminal callbacks; recorded-battle storage no-op does not imply replay isolation or all capture/playback no-op. The Gift ESC note conveys none of this distinction.',related_candidate_pointers=[P+'revisions/r3/feature-source-deltas.json#FR-000173/source_fact_delta',P+'revisions/r3/source-file-reassessment.json#WP26/source_fact_reassessment'],minimum_fix='Replace173 current-delta annotation and corresponding author source-reassessment records with actualWP26L138 recording/replay split; retain244 genuine GiftESC note and preserve source/future routing category.'),
dict(feature_id=fid(227),candidate_pointer='/features/215/differences/1',source_document=f[fid(227)]['source']['document'],source_effective_ranges=[[115,161]],changed_effective_ranges=[[132,132]],source_identity=ident(f[fid(227)]['source']['document'],A),actual_fact='Negative accepted probability prefix can produce negative accumulator and floor integer quotient; no clamp to0.',candidate_fact='Claims Repel first nonEgg/fainted vs first able selection change, which is already inB8/current908L143.',distinguishing_counterexample='With accepted negative base probability and accumulator−1, floor(−1/200)=−1, not0; new clause forbids clamping negative accumulator. Repel comparison member configuration does not establish that calculation and was already specified.',related_candidate_pointers=[P+'revisions/r3/feature-source-deltas.json#FR-000227/source_fact_delta',P+'revisions/r3/source-file-reassessment.json#WP36/source_fact_reassessment'],minimum_fix='Replace227 current-delta annotation and corresponding reassessment records with actualWP36L132 negative-prefix/floor/no-clamp semantics; retain pre-existingRepel selector and category/responsibility.' )],same_root_scope='All five creature directly changed units and six changed primary/catalog files examined; 173/227 attribution annotations mismatch actual accepted diff;204 per-stat/totalEV precision is separately reported. These calibration failures do not re-open correct dependency repairs.',required_fix='Correct source-to-routing change narratives only; no newfeatureID or target design required.')
for case in finding['cases']:
    delta=js(P+'revisions/r3/feature-source-deltas.json')['records']
    files=js(P+'revisions/r3/source-file-reassessment.json')['records']
    di=next(i for i,x in enumerate(delta) if x['feature_id']==case['feature_id'])
    fi=next(i for i,x in enumerate(files) if x['document']==case['source_document'])
    case['related_candidate_pointers']=[dict(path=P+'revisions/r3/feature-source-deltas.json',pointer='/records/'+str(di)+'/source_fact_delta'),dict(path=P+'revisions/r3/feature-source-deltas.json',pointer='/records/'+str(di)+'/future_boundary_reassessment'),dict(path=P+'revisions/r3/source-file-reassessment.json',pointer='/records/'+str(fi)+'/source_fact_reassessment'),dict(path=P+'revisions/r3/source-file-reassessment.json',pointer='/records/'+str(fi)+'/future_plan_reassessment')]
    pi=18 if case['feature_id']==fid(173) else 20
    case['related_candidate_pointers'].append(dict(path=P+'revisions/r3/source-refinement-patch.json',pointer='/records/'+str(pi)+'/field_changes/0/after/1'))
    case['minimum_fix']+=' Keep the uniform patch reconstruction and derived evidence synchronized with the corrected final fields.'
finding['canonical_root_finding_id']='R3-SOURCE-ATTRIBUTION-001'
finding['local_alias']='R3-CRE-CAL-001'
finding['counting_qualification']='Two creature cases of the root merged attribution finding; do not count local alias as another independent issue.'
for row in active:
    if row['finding_refs']:
        row['local_finding_refs']=['R3-CRE-CAL-002'] if row['feature_id']==fid(204) else row['finding_refs'];row['finding_refs']=['R3-EV-BOUNDARY-001'] if row['feature_id']==fid(204) else ['R3-SOURCE-ATTRIBUTION-001']
for row in old_results:
    if row['finding_refs']:
        row['local_finding_refs']=['R3-CRE-CAL-002'] if row['feature_id']==fid(204) else row['finding_refs'];row['finding_refs']=['R3-EV-BOUNDARY-001'] if row['feature_id']==fid(204) else ['R3-SOURCE-ATTRIBUTION-001']
for row in changedsource:
    if row['finding_refs']:
        evcase=fid(204) in row['changed_effective_feature_ids']
        row['local_finding_refs']=['R3-CRE-CAL-002'] if evcase else row['finding_refs'];row['finding_refs']=['R3-EV-BOUNDARY-001'] if evcase else ['R3-SOURCE-ATTRIBUTION-001']
        if evcase:row['source_fact_reason']+=' '+cal_reasons[fid(204)]
evfinding=dict(finding_id='R3-CRE-CAL-002',canonical_root_finding_id='R3-EV-BOUNDARY-001',local_alias='R3-CRE-CAL-002',severity='P3',verdict='FAIL',facet='current_calibration',title='FR204 calls single-stat EV overflow a total EV overflow',candidate_commit=C,current_source_commit=A,candidate_path=P+'routing-manifest.json',feature_ids=[fid(204)],cases=[dict(feature_id=fid(204),candidate_pointer='/features/192/differences/1',source_document=f[fid(204)]['source']['document'],source_effective_ranges=[[79,126]],changed_effective_ranges=[[122,122]],source_identity=ident(f[fid(204)]['source']['document'],A),actual_fact='HP255/ATK255 template has total510; HP exceeds per-stat252, giving first single-stat upper bound−3 before total bound is reached.',candidate_fact='设施模板超EV总量受普通非Shadow战斗成长消费时在首项负余量门失败。',distinguishing_counterexample='NormalHP255/ATK255 template totals510 exactly. HP yield0 still fails theHP single-stat clamp[0,−3], before total clamp. Correct totals cannot be treated as total-overflow eligibility or automatic normalization.',related_candidate_pointers=[dict(path=P+'revisions/r3/feature-source-deltas.json',pointer='/records/14/source_fact_delta'),dict(path=P+'revisions/r3/source-file-reassessment.json',pointer='/records/8/source_fact_reassessment'),dict(path=P+'revisions/r3/source-refinement-patch.json',pointer='/records/19/field_changes/0/after/1')],minimum_fix='Replace total-overflow description with per-stat overflow and first per-stat negative-allowance failure; preserve total510, no recipient EV/EXP write, and earlier-prefix limits. Synchronize final annotation, source reassessment and reconstruction patch.')],same_root_scope='One creature case of root mergedEV finding; root owns combat29/32 and world456 cases. Existing classification/responsibility/scope/dependency judgments remainPASS.',counting_qualification='Do not count creature local alias as another issue beyond canonicalroot finding.')

result=dict(schema_version='r3-independent-domain-review/v1',reviewer_task='/root/r3_creature',candidate_commit=C,prior_candidate_commit=R2C,prior_review_commit=R2R,current_source_commit=A,verdict='FAIL_CURRENT_CALIBRATION_ONLY',configuration=dict(requested_model='gpt-6.1-sol',requested_effort='ultra',requested_service_tier='default',requested_speed='normal',requested_Fast='off',effective_model='UNVERIFIED',effective_effort='UNVERIFIED',effective_service_tier='UNVERIFIED',effective_speed='UNVERIFIED',effective_Fast='UNVERIFIED',cloud_task_uuid='UNVERIFIED',qualification='No authoritative runtime echo; logical agent path is not cloudUUID. One independent review division, not additional acceptancevote.'),summary=dict(original_ids=116,old_PASS=113,old_FAIL=3,active_ids=122,active_PASS=119,active_FAIL=3,classification_PASS=122,responsibility_PASS=122,scope_PASS=122,dependency_PASS=122,current_calibration_PASS=119,current_calibration_FAIL=3,retired_features=0,metadata_records=0,original_groups=7,original_group_PASS=7,original_group_FAIL=0,allocated_R2_issues=2,R2_issue_PASS=2,allocated_R1_residual_issues=1,R1_residual_issue_PASS=1,primary_documents=18,body_documents=15,catalog_documents=3,changed_primary_catalog_documents=6,directly_changed_creature_feature_units=5,section_metadata=158,section_metadata_PASS=158,owned_new_headings=0,supplementary_new_heading_consumer_crosschecks=3,feature_ref_rows_checked=17,original_feature_ref_edges_checked=57,current_feature_ref_edges_checked=55,current_feature_ref_edges_PASS=55,new_findings=2),old_feature_results=old_results,active_feature_results=active,retired_metadata_results=[],issue_results=issues,original_group_results=groups,reading_ledger=reading,extra_consumer_reading=extra,section_metadata_results=sections,new_heading_results=headings,changed_source_results=changedsource,dependency_edge_results=edges,original_dependency_edge_results=oldedge_results,new_findings=[finding,evfinding],execution_boundary='StaticMarkdown/JSON/Git/Python review only. Ruby/game/business/host/Showdown/framework/prototype execution0. No author/formal/reference/main/oldreview edits, no commit.',inheritance_boundary='Exact R2 source identity/full semantic credit + actual nonimpact reasoning for unaffected facets only. All nonPASS, changed effective source and changed referenced target scopes fresh as listed; no automatic oldPASS transfer.',evidence_file='creature-evidence.json')
ev=dict(candidate_commit=C,current_source_commit=A,objects=objects,entry_inputs=entry_inputs,mandatory_r2_inputs={n:{k:v for k,v in x.items() if k!='parsed'} for n,x in inputs.items()},root_reconciliation=dict(old_feature_projections=116,active_feature_projections=122,original_groups=7,residual_issues=1,primary_reading_records=18,root_sections_parsed=2683,root_catalog_metadata_results_parsed=424,root_active_results_parsed=736,root_old_results_parsed=721,root_retired_metadata_results_parsed=33,root_original_groups_parsed=44,root_issue_results_parsed=12,root_findings_parsed=7,all_allocated_projections_equal=True),r3_manifest_invariants=dict(allocated_source_equal_R2=True,allocated_future_plan_equal_R2=True,allocated_functional_scope_equal_R2=True,historical_section_coverage_equal_R2=True,rows_current_snapshot_verified=122),changed_primary_patches=diffs,changed_target_effective_ids=changed_target_ids,dependency_edges=edges,original_dependency_edges=oldedge_results,static_command_receipts=commands,collection_errors=['An exploratoryunit concatenation first raisedTypeError before anyoutputwrite; fixed by flattening list slices. One exploratoryWP58path undercreature-rpg did notexist; corrected tocombat-requirements; no reading credit for rejected path. Truncated mixed output WP39/73 was reread in explicit ranges; no unread credit.'])
(OUT/'creature-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(OUT/'creature-evidence.json').write_text(json.dumps(ev,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result['summary'],ensure_ascii=False))
