"""Finalize review evidence only. Does not execute reference code or a behavior model."""
import sys, json, re, datetime, hashlib
from pathlib import Path
sys.dont_write_bytecode=True
from ledger import read,write,ROOT,complement
cov=read('reading-coverage.json');src=read('source-to-spec.json');rev=read('spec-to-source.json');findings=read('findings.json');shared=read('shared-interfaces.json');prog=read('progress.json');data=read('data-audit.json')
rv=cov['source_baseline']['commit'];bv=cov['specification_baseline']['commit']

def ranges(anchor):
    value=anchor.get('lines',[])
    if not value:return []
    return [value] if isinstance(value[0],int) else value

def overlaps(a,b):return a[0]<=b[1] and b[0]<=a[1]

groups={k:v for k,v in rev['source_anchor_groups'].items() if k.startswith('M08-CLOSED-')}
assert all(c['review_extent']=='full' and c['evidence_level']=='static_semantic_clause_comparison' and c.get('source_anchor_group_ref') in groups for s in rev['specifications'] for c in s['clause_mappings'])
rev['source_anchor_groups']=groups
rev['common_clause_boundary']='All1906 primary-scope clauses/tables/vectors have explicit finite semantic comparisons and source anchors. Complete review does not imply every capability is supported; candidate gaps remain missing/partial/unresolved. supported means supported_static at fixed R/B5, never runtime confirmation.'
rev['review_status']='semantic_work_complete_artifact_validation_pending'
for s in rev['specifications']:
    s['clause_mapping_status']='complete_finite_clause_comparison'
    for c in s['clause_mappings']:
        c.pop('comparison_note',None) # the exact note is canonical in its group
    s['current_review_result']='full_comparison_of_assigned_clauses; capability_outcomes_are_separate'

# Every source retains actual whole-file reading extent and exact unreviewed intervals.
# Cross-domain whole-file residuals are not silently upgraded to full.
by_source={f['path']:[] for f in cov['sources']}
for gid,g in groups.items():
    perpath={}
    for a in g['source_anchors']:
        if a.get('path') in by_source:perpath.setdefault(a['path'],[]).extend(ranges(a))
    for path,rs in perpath.items():
        unique=sorted(set(tuple(r) for r in rs))
        by_source[path].append({'comparison_group_id':gid,'source_ranges':[list(r) for r in unique],
            'specification_path':g['specification_path'],'specification_lines':g['specification_lines'],
            'capability_status':g['capability_status']})

for f in cov['sources']:
    f['M08_scope_review_extent']='full'
    f['M08_scope_material_availability']='available'
    f['within_M08_unreviewed_ranges']=[]
    f['current_contract_comparison_refs']=[x['comparison_group_id'] for x in by_source[f['path']]]
    if f['scope_role']=='primary':
        assert f['review_extent']=='full' and not f['unreviewed_ranges']
        f['scope_boundary']='Entire assigned source body and every definition/handler/default/branch reviewed; whole phases/AI and runtime are not signed.'
    elif f['path'] in ['PBS/abilities.txt','PBS/items.txt','PBS/moves.txt']:
        f['scope_boundary']=f.get('M08_scope','Named combat data projections only.')
        f['outside_M08_semantic_content']='All unreviewed full lines and unrelated tokens on a reviewed Flags line; display/localization/economy/authoring/hatching and full compilation are other-owner domains.'
    else:
        f['scope_boundary']='Only explicit semantic_ranges/data_semantic_ranges and named consumer/override projections are signed. Other whole-file intervals remain outside M08.'
        f['outside_M08_semantic_content']='Exact unreviewed_ranges below; no inference that these source behaviors are absent.'
    for r in f['semantic_ranges']:
        r['comparison_stage']='first_pass_record_retained'
        r['current_resolution_note']='Follow current_contract_comparison_refs and source-to-spec capabilities for final scoped outcome; earlier 待/未读 wording records extraction sequence, not a remaining M08 task.'
    if f['path'].endswith('002_ShadowPokemon_Other.rb'):
        f['body_read_ranges']=[[1,460]]
        f['scope_boundary']='M08 semantic scope183–221 and330–408; other file content read as domain context, not whole M04 lifecycle sign-off.'
        f['shadow_effect_resolution']='GR5-M08-001 merged missing receiving contracts; original source-only326–408 note superseded by individual four-effect comparisons.'
    if f.get('data_semantic_ranges'):
        covered=[r['lines'] for r in f['semantic_ranges']]
        covered.extend(z for r in f['data_semantic_ranges'] for z in r['lines'])
        f['unreviewed_ranges']=complement(f['line_count'],covered)

# Canonical effect results. Earlier partial flags were unfinished comparison stages,
# now closed by the complete source bodies and current clause/consumer comparisons.
helper_names={'StatUpMove','MultiStatUpMove','StatDownMove','TargetStatDownMove','TargetMultiStatDownMove','FixedDamageMove','TwoTurnMove','HealingMove','RecoilMove','ProtectMove','WeatherMove','PledgeMove'}
gap_names={'UserSwapBaseAtkDef','UserTargetSwapBaseSpeed','UserTargetAverageBaseAtkSpAtk','UserTargetAverageBaseDefSpDef','AllBattlersLoseHalfHPUserSkipsNextTurn','UserLosesHalfHP','RemoveAllScreensAndSafeguard'}
for cap in src['capabilities']:
    if any(not isinstance(a,dict) for a in cap.get('source_anchors',[])):
        contract=next((c for c in shared['contracts'] if c['id']==cap['id']),None)
        if not contract:raise ValueError('Unresolved legacy source anchor: '+cap['id'])
        cap['source_anchors']=contract['source_anchors']
    cap['first_pass_capability_status']=cap['capability_status']
    name=cap['name']
    if name in gap_names:cap['capability_status']='missing';cap['related_findings']=['GR5-M08-001']
    elif name=='StartShadowSkyWeather':cap['capability_status']='partial';cap['related_findings']=['GR5-M08-001']
    elif name=='Unimplemented':cap['capability_status']='missing';cap['related_findings']=['GR5-M08-003']
    elif name=='BurnAttackerBeforeUserActs':cap['capability_status']='unresolved';cap['related_findings']=['GR5-M08-002']
    else:cap['capability_status']='supported'
    cap['review_extent']='full'
    cap['evidence_level']='static_source_and_current_clause_comparison'
    cap['supported_boundary']='supported_static: complete local definition/handler and explicitly audited consumer/data projection at fixed R/B5; no runtime, arbitrary plugin, or other-owner whole-domain guarantee' if cap['capability_status']=='supported' else None
    cap['review_completion']='complete_within_M08; capability_gap_is_result_not_unread_material'
    cap['unit_kind']='shared_helper_contract' if name in helper_names else 'internal_action_contract' if name=='Confusion' else 'resolution_fallback_contract' if name=='Unimplemented' else 'canonical_registered_or_direct_effect_rule'
    precise=[]
    for gid,g in groups.items():
        found=False
        for ca in cap.get('source_anchors',[]):
            for ga in g['source_anchors']:
                if not isinstance(ga,dict):continue
                if ca.get('path')!=ga.get('path'):continue
                if any(tuple(x)==tuple(y) for x in ranges(ca) for y in ranges(ga)):
                    found=True;break
            if found:break
        if found:precise.append({'group_id':gid,'path':g['specification_path'],'version':bv,'lines':[g['specification_lines']]})
    cap['precise_specification_links']=precise
    if name=='Unimplemented':
        cap['rules_checked']=next(f['expected_reference_behavior'] for f in findings['findings'] if f['id']=='GR5-M08-003')
    if name in gap_names or name=='StartShadowSkyWeather':
        cap['counterevidence_record']='findings.json#GR5-M08-001; outgoing contracts and exact negative reading scope'
    if name=='BurnAttackerBeforeUserActs':cap['counterevidence_record']='findings.json#GR5-M08-002'

src['source_files']=[{'path':f['path'],'version':f['version'],'actual_semantic_ranges':f['semantic_ranges'],
    'data_semantic_ranges':f.get('data_semantic_ranges',[]),'review_extent':f['review_extent'],
    'M08_scope_review_extent':f['M08_scope_review_extent'],'material_availability':f['material_availability'],
    'evidence_level':f['evidence_level'],'unreviewed_ranges':f['unreviewed_ranges'],'scope_boundary':f['scope_boundary'],
    'precise_comparison_links':by_source[f['path']]} for f in cov['sources']]
src.pop('precise_contract_comparisons',None)
src['comparison_group_definitions']='spec-to-source.json#/source_anchor_groups; each source-file inverse link contains exact local ranges and exact current specification ranges'
src['unmapped_source_scope']={'within_assigned_M08_scope':[],'outside_scope':'reading-coverage.json sources[].unreviewed_ranges and explicit field exclusions; not reviewed or signed as other-owner behavior'}
src['move_index_navigation_gaps_resolved']={'Unimplemented':'GR5-M08-003 missing fallback contract','Confusion':'WP43/WP46 internal action exact group anchors','shared_base_definitions':'WP44/46/47/45 common rules mapped through exact effect/method groups; no literal source name required in clean specification'}
src.pop('move_index_navigation_gaps',None)
src['review_status']='semantic_work_complete_artifact_validation_pending'
src['coverage_interpretation']='Shared helpers, aliases, reopens, default records and consumers are projections of canonical rules. Structural definition totals are not product-feature totals. All M08 source bodies/required consumers/current clauses have been compared; gaps are results, not incomplete reading.'

# Refresh the source entry inventory statuses without treating literal names as proof.
cap_index={c['id']:c for c in src['capabilities']}
for f in cov['sources']:
    for entry in f.get('effect_entry_inventory',[]):
        cid=entry.get('shared_rule_id');c=cap_index.get(cid)
        if c:
            entry['capability_status']=c['capability_status'];entry['review_extent']='full'
            entry['current_contract_comparison_refs']=[r['group_id'] for r in c['precise_specification_links']]
            entry['related_findings']=c.get('related_findings',[])
    if f['path'].endswith('002_ShadowPokemon_Other.rb'):
        f['effect_entry_inventory']=[{'entry':c['name'],'line':ranges(c['source_anchors'][0])[0][0],
            'lines':ranges(c['source_anchors'][0])[0],'shared_rule_id':c['id'],'review_extent':'full',
            'material_availability':'available','evidence_level':'static_source_and_current_contract_counterevidence',
            'capability_status':c['capability_status'],'related_findings':['GR5-M08-001'],'unreviewed_ranges':[]}
            for c in src['capabilities'] if c['name'] in ['AllBattlersLoseHalfHPUserSkipsNextTurn','UserLosesHalfHP','StartShadowSkyWeather','RemoveAllScreensAndSafeguard']]

cov['coverage_warning']='Whole-file extent and scoped M08 semantic completion are separate. No inventory/byte count/string match is used as semantic proof; all registered bodies were read and compared. Gaps do not mean unread material.'
cov['strict_review_interpretation'].update(overall_semantic_contract_closure='COMPLETE_WITHIN_ASSIGNED_STATIC_SCOPE',anonymous_clause_navigation_count=0,anonymous_clause_navigation_is_not_full_review=False)
cov['strict_review_interpretation']['review_extent_full']='Entire source body has explicit semantic disposition. Dependencies may retain partial whole-file extent while their required M08 projection is complete. Supported always means supported_static.'
cov['strict_review_interpretation']['independent_counterevidence']='Root independently confirmed original001/002/003 with qualifiers; subsequent Shadow extension to001 and optional input addition to003 are separately scoped. Canonical integration is parent-owned.'
for f in cov['specifications']:
    other=next(z for z in rev['specifications'] if z['path']==f['path'])
    f['precise_clause_comparison_status']=other['clause_mapping_status']
    f['M08_scope_review_extent']='full';f['within_M08_unreviewed_ranges']=[]
# Newly read current audit entries remain bounded and do not import historical PASS.
trace=next((z for z in cov['current_supplement_and_boundary_reading'] if z['path']=='audit/source-traceability.md'),None)
if trace:
    trace['lines']=sorted(trace['lines']+[[233,244],[525,550],[633,644],[1020,1031]])
    trace['semantic_scope']='Current WP03/23/39/43/47 traceability and relevant U04 successor link; navigation only, historical PASS not proof.'

# Missing physical demo/runtime material is explicitly not reviewed and not a static-scope blocker.
cov['material_availability_boundary']['completion_effect']='Unavailable engine/demo/media are excluded from this authorized static review; all available assigned source/data/contracts were reviewed. No execution permission was sought or used.'

for c in shared['contracts']:
    if c['id']=='M08-RAW-STATS':c['boundary']='GR5-M08-001 raw-stat sub-scope: four outgoing delegated effects lack actual receiver; parent independently confirmed this original sub-scope with shared substitute-bypass and no-intervening-refresh qualifiers.'
    c['review_completion']='M08 static semantic review complete; gap outcome distinct from review extent'
    if c.get('supported_boundary'):c['supported_boundary']='supported_static within fixed R/B5 and explicit source/caller projections; no whole M07/M09/M04 or runtime sign-off'
for cid,title,status,names,consumers,boundary,fid in [
('M08-SHADOW-EFFECTS','四个Shadow专属真实战斗效果','partial',['AllBattlersLoseHalfHPUserSkipsNextTurn','UserLosesHalfHP','StartShadowSkyWeather','RemoveAllScreensAndSafeguard'],[{'module':'M04','projection':'WP23生命周期/可选输入交付；效果接收归M08，不自动启用样本。'},{'module':'M09','projection':'AI评分/失败预测不能替代实际HP/屏障/天气提交。'}],'GR5-M08-001同根因扩展；ShadowHalf/End/双侧清屏障missing、Sky入口partial。此扩展尚未被原root反证覆盖。','GR5-M08-001'),
('M08-EFFECT-RESOLUTION','合法缺失效果解析与分类回退','missing',['Unimplemented'],[{'module':'M03','projection':'内容ID存在与FunctionCode实现存在不是同一判定。'},{'module':'M07','projection':'普通PP在整招失败之前；调用/特殊PP按各自合同。'},{'module':'M04','projection':'可选SHADOWSHED绑定RemoveAllScreens；不替换为相近清屏障定义。'}],'nil/缺省归None，不包括空字符串；合法未解析实现status失败，damage普通回退。','GR5-M08-003')]:
    shared['contracts']=[c for c in shared['contracts'] if c['id']!=cid]
    cs=[next(c for c in src['capabilities'] if c['name']==n) for n in names]
    shared['contracts'].append({'id':cid,'title':title,'owner':'M08','classification':['Pokémon Rules','Combat Requirements'],'capability_status':status,'supported_boundary':None,'source_anchors':[a for c in cs for a in c['source_anchors']],'specification_anchors':[a for c in cs for a in c['specification_anchors']],'canonical_rule_ids':[c['id'] for c in cs],'consumer_projections':consumers,'boundary':boundary,'related_findings':[fid],'evidence_level':'static_source_and_current_contract_counterevidence','execution_status':'NOT_EXECUTED','review_completion':'complete_within_M08','counting_rule':'Umbrella cross-domain contract; referenced canonical effects are not counted again.'})
shared['contracts'].append({'id':'M08-WEIGHT-CONSUMER','title':'重量经过能力与道具后交捕获','owner':'M08 (weight); M06 (capture)','capability_status':'supported','supported_boundary':'supported_static AB24/HI35 inputs only; capture RNG/outcomes remain M06','source_anchors':[{'path':'Data/Scripts/011_Battle/007_Other battle code/010_Battle_PokeBallEffects.rb','version':rv,'lines':[[125,148]]},{'path':'Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb','version':rv,'lines':[[206,229]]}],'consumer_projections':[{'module':'M06','projection':'0.1kg current weight, two independent ability/item gates, HeavyBall adjustment then HP/status float and floor x.'}],'evidence_level':'static_source_and_contract_comparison','execution_status':'NOT_EXECUTED','counting_rule':'Consumer projection, not new capture capability.'})

# Optional input display prose is not reproduced in the evidence data table.
for row in data.get('optional_shadow_move_records',[]):
    row['data']={k:v for k,v in row['data'].items() if k not in ['Name','Description']}
    row['display_fields']='Read and classified as non-normative display content; text not reproduced.'

outside=[{'path':f['path'],'whole_file_review_extent':f['review_extent'],'unreviewed_ranges':f['unreviewed_ranges'],'reason':f.get('outside_M08_semantic_content','No unreviewed whole-file lines'), 'signed_scope':f['scope_boundary']} for f in cov['sources'] if f['unreviewed_ranges']]
prog['not_reviewed']={'within_assigned_available_static_scope':[],'unavailable_or_unexecuted':['engine/game/reference/model execution','missing serialized demo maps/events and media (availability recorded in reading-coverage.json)']}
prog['outside_module_scope']={'source_file_residuals':outside,'shared_test_residuals':[{'path':s['path'],'unreviewed_ranges':s['unreviewed_ranges'],'owner_boundary':'M07/M09 remaining chapters; M08 rows fully reviewed'} for s in rev['specifications'] if s['unreviewed_ranges']], 'domains':['M07 full battle phases/commands/order/endings','M09 whole AI','M04 whole Shadow growth/purification and individual data','other domains outside named consumer projections']}
prog['current_range']='All assigned static semantic work complete; final artifact consistency validation'
prog['next_actual_range']='No available assigned source/contract/vector remains unread. Parent canonical integration and independent review of the added Shadow sub-scope remain separate from module reading completion.'
prog['last_completed_finite_range']='All primary source bodies, all handler branches, required callers/overrides/default-data projections and1906 current clauses/tables/vectors have explicit static comparisons; Shadow receiving gap merged into001 and optionalSHADOWSHED strengthens003.'
prog['deliverable_kind']='completed_static_module_review_pending_artifact_validation'
prog['status']='in_progress';prog['complete']=False
prog['required_revision_signed_off']=False
prog['candidate_findings']=[f['id'] for f in findings['findings']]
prog['reviewed_capability_gaps']={c['id']:c['capability_status'] for c in src['capabilities'] if c['capability_status']!='supported'}
prog['model_parameter_echo']='UNVERIFIED';prog['reference_execution_count']=0;prog['behavior_model_execution_count']=0
prog['updated_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
prog['parent_counterevidence_boundary']='Original001 raw4/002/003 independently confirmed by root with qualifiers, canonical merge pending. Added Shadow4 within001 not covered by that original root resolution; no proposer final required sign-off.'
for name,obj in [('reading-coverage.json',cov),('source-to-spec.json',src),('spec-to-source.json',rev),('shared-interfaces.json',shared),('progress.json',prog),('data-audit.json',data)]:write(name,obj)
print('Canonical review indices compacted, current outcomes aligned, all outside-owner whole-file residuals explicit; complete remains false until artifact validation.')
