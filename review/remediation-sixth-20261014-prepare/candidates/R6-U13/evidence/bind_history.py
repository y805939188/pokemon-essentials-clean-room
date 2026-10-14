"""Bind finite affected historical qualifications; no prior verdict transfer."""
from pathlib import Path
import datetime, hashlib, json, subprocess

REPO=Path(__file__).resolve().parents[5]
OUT=Path(__file__).resolve().parent
FIX='c0ff33024aea424c68d29f9778fe7c8e807d21e8'
BASE='review/global-independent-review/fifth-2026-10-13-9366d9d-c7d3/'

def blob(commit,path):
    return subprocess.check_output(['git','show',commit+':'+path],cwd=REPO)

def identity(b):
    return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
            'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}

hp='review/remediation-fifth-20261013-prepare/integration/R5-U08/candidate-01/historical-regression-input.json'
hb=blob('469a268b92daed7b4d28d7fd0da75520cbb7228f',hp)
history=json.loads(hb)
manifest=json.loads((OUT/'candidate-manifest.json').read_text())
paths={x['formal_path'] for x in manifest}
nav=[]
for r in history['records']:
    matched=[z for z in r.get('current_formal_paths',[]) if z['path'] in paths]
    if matched:
        nav.append({'id':r['id'],'owner':r['batch_owner'],'record_key':r.get('record_key'),
                    'frozen_record':r['frozen_record'],'qualified_scope_binding':r['qualified_scope_binding'],
                    'matched_paths':matched,'role':'FINITE_NAVIGATION_NO_VERDICT_TRANSFER'})

qualified=[];fileids={}
for p,indices in [('regression-fourth-17.json',[8,9,10,15,16]),
                  ('regression-third-23.json',[10,11,12,13,14,15,20,21,22])]:
    b=blob(FIX,BASE+p);x=json.loads(b);fileids[p]=identity(b)
    for i in indices:
        r=x['records'][i]
        qualified.append({'id':r['id'],'owner':r['batch_owner'],'commit':FIX,'path':BASE+p,
                          'pointer':f'/records/{i}/historical_identity_scope_reuse',
                          'qualified_scope':r['historical_identity_scope_reuse'],
                          'current_check':'WP40 old text exact after deleting sole Arena addition; pokemon test BP/FP/PD/VF/LT suffix exact. These shared-file correlations do not broaden original scope or sign the old dynamic consumer.'})

rb=blob(FIX,BASE+'regression-legacy-scope.json');rx=json.loads(rb)
fileids['regression-legacy-scope.json']=identity(rb)
bindings=[{'index':i,'scope':rx['contributions'][i]['historical_identity_scope_reuse']}
          for i in range(231,240)]
cp='review/remediation/20261003-prepare/batches/B13/author-draft-1/original-and-acceptance-controls.json'
cb=blob('d81562bfe0e79ca4df3233ada38fa09e800bdafc',cp);cx=json.loads(cb)
fields=[]
for i,r in enumerate(cx['controls']):
    f=r['complete_current_control_fields']
    if i==0:
        # Whole relevant extension records, not snippets or search hits.
        projected={k:v for k,v in f.items() if k not in ['extensions','extension_decisions','minimum_revision','determinate_recheck']}
        projected['extensions']=[e for e in f.get('extensions',[]) if any(p in json.dumps(e,ensure_ascii=False) for p in paths)]
        projected['projection_boundary']='Common root qualification plus complete extensions naming affected paths only; unrelated source-organization extensions not adopted.'
    else: projected=f
    fields.append({'id':r['id'],'owner':'B13','pointer':f'/controls/{i}/complete_current_control_fields',
                   'qualified_scope':projected,'scope_rule':r['scope_rule']})

r5=[]
r5_commit='f49d870c6fd616ab6736754a218a4553b5acac7f'
r5_sources=[
 ('root-M07/canonical-findings.json','bbdee0813200953d50abf647b73341466d5559c9',58751,'8f4e67617983a96a2f1fdc76a40d24cb97ad0d189c623670f6a711d6295cb6f6'),
 ('root-JXN/canonical-findings.json','7b21312f9f3512bfdd57e21a17cfb83096074050',162386,'8de2ac509bc7ff2ddefc0d40536afc9a3247acdedfa828e179ff0f973ca8e4e8')]
for suffix,oid,size,sha in r5_sources:
    source_path=BASE+'counterevidence/'+suffix
    b=blob(r5_commit,source_path)
    assert identity(b)=={'bytes':size,'sha256':sha,'git_blob':oid}
    entry=subprocess.check_output(['git','ls-tree',r5_commit,'--',source_path],cwd=REPO).decode().strip()
    assert entry==f'100644 blob {oid}\t{source_path}'
    x=json.loads(b)
    for i,r in enumerate(x['findings']):
        if r['id'] in ['GR5-M07-001','GR5-M07-002','GR5-JXN-002']:
            r5.append({'id':r['id'],'binding_blob':oid,**identity(b),'pointer':f'/findings/{i}',
                'source_commit':r5_commit,'source_path':source_path,'git_entry':entry,
                'retrieval_note':'The initial local commit/path read did not succeed; that failure did not establish path absence and its cause remains UNKNOWN. The prior author recovered and read the exact declared blob. Repair-01 now recovered the full payload at the exact f49d commit/path and verified bytes/SHA256/Git blob, independently through GitHub and local Git. The prior absence inference is withdrawn; no historical path was rewritten.',
                'retrieval_transition':{'prior_candidate':'00b45de642f07cee9953e42f04cce9c35d77346f','prior_failure_record_preserved':True,'original_failure_cause':'UNKNOWN_NOT_RECONSTRUCTED','initial_blob_recovery_retained':True,'fixed_path_exists':True,'repair_receipt':'repair-01/r5-path-recovery.json','independent_FAIL_report':'3ef4854ef43eac92fd1dc57350e4cf6aa160082b:review/remediation-sixth-20261014-prepare/reviews/R6-U13-R/review-report.md'},
                'qualified_scope':{k:r[k] for k in ['preconditions','expected_reference_behavior','minimal_counterexample','normal_case','failure_or_boundary_case','proposed_spec_change','acceptance_criteria','review_resolution']},
                'current_check':'Only sentence-tail Arena addition to WP40; entire previous text remains byte-equal after removing it. Prior failure Boolean, Metronome identity and exact ERR01/controls remain unchanged; new Arena recharge uses same precheck gate.'})

checks=[
 {'scope':'R1 original WP facts','check':'Fixed formal inherited boundaries and unrelated chapters/rows retained. WP53 budget/expiry/mode exits unchanged; WP54 member/team/final count and cups3/4 unchanged; WP55 old W30 retained; WP56 probability tables/mind/body/continuous judgment retained; WP58 exact18 keys and selective omissions retained.'},
 {'scope':'R2 B13/B003/B010/B025','check':'QC Q41/Q43/Q44/Q47 exact: clause keys/load qualification, ice q30/r19/r20 and saved-song-source outcome remain. No new optional clause or source architecture imposed.'},
 {'scope':'R2 B13/B027','check':'WP54 nil-vs-empty receiver paragraph and WS W28/W29/W35 exact; new count0 does not permit final empty confirmation or silently submit cancel.'},
 {'scope':'R2 B13/B028','check':'PA P20/P28 exact; count>=3, mind/skill/baseline/start-message retention untouched. New recharge P31 does not reset judgment cycle.'},
 {'scope':'R2 B13/B029','check':'RC W16/W24/W25/W26 exact and WP58 §5.2 unchanged; preparation capture stays before initial entry/first command and does not shift switch consumer phases.'},
 {'scope':'R2 B13/B018','check':'RC W22b retained; independently counted29 current rows, QC49 WS36 PA32 and SF40 synchronized; no identity loss.'},
 {'scope':'R2 B12/B026','check':'SF35 exact and WP53 encounter selection/gate chapters unchanged; active-save singleton party does not claim singleton implies contest battle takeover.'},
 {'scope':'S001 retained SF30 normal/conversion controls','check':'SF30 d restores normal end→save→load with nonactive session/mode statistics persistence and unknown runtime-clock semantics. SF30 e restores the fixed current default conversion-set search with no dedicated Safari/contest migration, excluding arbitrary versions/plugins. Mechanical subcase presence is checked by verify_candidate.py; semantic comparison is author static evidence, not runtime or independent acceptance.'},
 {'scope':'R3/R4 shared-file only correlations','check':'Fourteen exact original scope bindings read; old WP40 prefix preserved and pokemon shared non-SF suffix byte-equal. GR3-M08 first-error/GR4-J08 restricted old chain is not replaced by Arena target-completion description.'},
 {'scope':'R5 M07-001/M07-002/JXN-002','check':'Exact blob scope read; verification confirms WP40 old full text retained. Recharge precheck result, same-move Metronome count and diagnostic retry preconditions preserve earlier contracts.'},
 {'scope':'Consumers WP09/17/65/66-A','check':'Read-only bounded units identity recorded in reading-ledger. Save failure prefix, normal-return exit, expiry callbacks and UI count interface separately reconciled. WP66-A unqualified count sentence handed to sole integrator.'}
]
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'input':{'path':hp,**identity(hb)},
 'fixed_historical_files':{'commit':FIX,'files':fileids},'affected_path_navigation':nav,
 'R3_R4_exact_scopes_read':qualified,'R2_exact_owner_contribution_bindings_read':bindings,
 'R2_B13_controls':{'commit':'d81562bfe0e79ca4df3233ada38fa09e800bdafc','path':cp,**identity(cb),'assigned_scopes':fields},
 'R2_B12_qualified_scope_read':rx['controls'][84]['historical_identity_scope_reuse'],
 'R5_exact_scopes_read':r5,'new_author_regression_checks':checks,
 'denominators_preserved':{'R1':'original WP scope only','R2':'229 controls/21 batches/341 qualified contributions','R3':'23/76; M09 optional/U08 historical not started; M02 no required','R4':'current17/76; B5 old16/75 and Summary supplement distinct','R5':'only92CLOSED,51P2/41P3; original410static/568schema; extra158 separate'},
 'historical_verdict_transferred':False,'author_static_check':'BOUNDED_DOCUMENT_CHECKS_AND_SF30_SUBCASE_REPAIR_COMPLETE_AWAITING_NON_AUTHOR_REVIEW',
 'independent_candidate_review':'PENDING_PARENT_ASSIGNED_NON_AUTHOR','integrated_regression':'PENDING_R6_I_ACTUAL_COMPOSITION','reference_or_host_execution':False}
(OUT/'historical-regression.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'finite_navigation_records':len(nav),'exact_R3_R4_scopes':len(qualified),'R2_owner_bindings':len(bindings),'R5_scopes':len(r5),'old_PASS_adopted':False},ensure_ascii=False))
