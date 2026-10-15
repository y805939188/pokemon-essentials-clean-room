"""Assemble current root reception after the named independent deliveries exist.

All original task outputs stay untouched. Joins/identity checks add no reading.
"""
import collections
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT.parents[2]
ROOT_ID='01a13d67-1bcb-72f2-8f3e-fcada717c8d4'
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(rel):return json.loads((ROOT/rel).read_bytes())
def rawid(raw):return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'git_blob_content_id':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}
def dump(rel,value):
    p=ROOT/rel
    if p.exists():raise FileExistsError('new root reception only: '+rel)
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def main():
    c17=read('tasks/R7-C17/coverage-summary.json');unread=read('tasks/R7-C17/final-unreceived-ids.json');valid=read('tasks/R7-C17/validation.json')
    if c17['exact_unreceived_count'] or valid['issues'] or any(v for k,v in unread.items() if isinstance(v,list)):
        raise ValueError('actual exact review reception still open')
    if 'FINAL' not in str(read('tasks/R7-C17/task.json').get('status','')):
        raise ValueError('C17 has not sealed actual final delivery')
    f=read('findings.json');zh=read('tasks/R7-C13/chinese-contracts.json');candidate=read('tasks/R7-C19/canonical-37.candidate.json')
    integrity=read('tasks/R7-C19/final-adjudication-integrity.json')
    if rawid((ROOT/'findings.json').read_bytes())['sha256']!=integrity['input']['root_findings']['sha256']:
        raise ValueError('root findings drifted after C19 reception')
    if integrity['summary']['missing_chains'] or integrity['summary']['effective_remaining_unresolved_assembly_fields']:
        raise ValueError('adjudication chain/field gap')
    contexts={'R7-I':ROOT_ID,'R7-M01':'01a13d94-ace2-7212-908f-48f56a290fda','R7-M02':'01a13d94-fb64-7d42-ac1d-00537e33823c','R7-M03':'01a13d95-406a-7e42-84d6-410b9499e047','R7-C14':'01a13e0a-7a77-7572-8d38-bfe7d3082fe1'}
    for p in (ROOT/'tasks').glob('R7-*/events.jsonl'):
        with p.open() as inp:
            for line in inp:
                try:v=json.loads(line)
                except ValueError:continue
                if v.get('type')=='thread.started':contexts[p.parent.name]=v['thread_id'];break
    for old,new in {'R7-C01':'R7-M02','R7-C07':'R7-M02','R7-C10':'R7-M02','R7-C12':'R7-M02','R7-C17':'R7-M02','R7-C02':'R7-M01','R7-C08':'R7-M01','R7-C03':'R7-M03','R7-C13':'R7-M03','R7-C18':'R7-M03','R7-C19':'R7-C14','R7-C20':'R7-C14','R7-J09':'R7-M03'}.items():contexts[old]=contexts[new]
    def actor(label):
        if 'events_plugins' in label:return '01a13d9a-87a4-7c51-b739-e48485b8eaad'
        if 'diagnostics_localization' in label:return '01a13d9a-b6ad-79a2-a960-865c8c5b8b5e'
        match=re.search(r'R7-(?:[A-Z][0-9]{2}|I)(?![0-9])',label)
        if not match or match.group() not in contexts:raise ValueError('actual actor unresolved '+label)
        return contexts[match.group()]
    records=candidate['records']
    if {v['id']:(v['classification'],v['severity']) for v in records}!={v['id']:(v['classification'],v['severity']) for v in zh['records']}:raise ValueError('Chinese identity/classification drift')
    zh_byid={v['id']:v for v in zh['records']}
    for x in records:
        # C19 supplies seven original-field binding groups. C13 supplies the
        # fully expanded Chinese normative groups. Preserve both schemas;
        # a reference-only group must not stand in for the complete contract.
        x['original_field_binding_groups']=x['groups']
        x['groups']=zh_byid[x['id']]['groups']
        x['complete_chinese_groups_origin']={'path':'tasks/R7-C13/chinese-contracts.json','sha256':rawid((ROOT/'tasks/R7-C13/chinese-contracts.json').read_bytes())['sha256'],'record_id':x['id'],'root_reception':'evidence/chinese-contract-view-root-reception.json'}
        a=x['authority'];a['proposer_actual_context']=actor(a['原提出者']);a['counter_actual_context']=actor(a['非提出者'])
        if a['proposer_actual_context']==a['counter_actual_context']:raise ValueError('self-only counter '+x['id'])
        a.update(root_actual_context=ROOT_ID,canonical_root_acceptance='FINAL_REVIEW_RECORD_ACCEPTED',root_reception='evidence/final-root-reception.json')
        x['status']='FINAL_REVIEW_RECORD_ACCEPTED_UPDATE_NOT_STARTED'
        if x.get('primary_batch'):x['primary_batch']['status']='MANUAL_PLAN_READY_NOT_STARTED'
    canonical={**candidate,'schema':'r7.canonical-records.final.v1','status':'FINAL_ROOT_ACCEPTED','root_adjudicator':'R7-I','root_actual_context':ROOT_ID,'root_final_acceptance':'Actual R7-I accepts complete C19 view against root/C13 and independent narrowing; generation-time candidate values remain preserved in original task payload.','reference_base':'tasks/R7-C19','records':records,'pending':[],'update_started':False}
    dump('canonical-records.json',canonical)
    corrected='tasks/R7-C18/corrected-candidate/'
    for src,dst in [('batch-candidates.json','batch-plan.final.json'),('dependency-candidates.json','dependency-graph.json'),('file-conflict-candidates.json','file-conflict-graph.json')]:
        doc=read(corrected+src);doc.update(status='FINAL_MANUAL_PLAN_READY_NOT_STARTED',update_started=False,root_reception='evidence/final-root-reception.json')
        dump(dst,doc)
    source=read('inventory/source.json');formal=read('inventory/formal.json');supp=read('inventory/supplements.json')
    if not all(isinstance(v,list) for v in (source,formal,supp)):raise ValueError('inventory schema')
    current_source={v['path']:v for v in read('tasks/R7-C17/canonical-source-coverage.json')['files']}
    for v in source:v['current_review']={'status':'BOUNDED_REVIEW_RECEIVED','axis':current_source[v['path']]['axis'],'exact_file_unit_fact_consumer_clause_receiver':'tasks/R7-C17/canonical-source-coverage.json','original_reading_axes_and_ranges':'C17 source-purpose-input-bindings + primary named reading-ledgers, C12 visible display recovery; opaque machine scope L04 is explicit.'}
    for v in formal:v['current_review']={'literal':'FULL_READ','lines':[1,v['lines']],'current_clauses':'tasks/R7-C17/canonical-formal-coverage.json','full_subassertion_scope_registry':'tasks/R7-C17/canonical-clause-registry.json','status':'BOUNDED_STATIC_CLAUSE_RECEPTION_COMPLETE','not_unique_requirement_count':True}
    for v in supp:v['current_review']={'status':'FULL_PURPOSE_STRUCTURE_OR_MARKDOWN_RECEPTION_COMPLETE','fields_and_cases':'tasks/R7-C17/canonical-supplement-purpose-index.json','actual_readers':'H06/H07/H08/H15/H19/H20/H21/H22; C17 purpose-qualified reception','old_states':'Preserved at generation time; no R6 PASS borrowed.'}
    dump('inventory/source.final.json',source);dump('inventory/formal.final.json',formal);dump('inventory/supplements.final.json',supp)
    inherited={};inputs=[];commit='9aa72bc99a4cf52c8fb9cad8a637a963341388b0'
    for key,name in [('optional','optional-records.json'),('FLOAT','optional-facets.json'),('policy','policy-records.json'),('limits','limit-records.json'),('no_required','no-required-revision-records.json')]:
        path='review/remediation-sixth-20261014-prepare/inputs/'+name;raw=subprocess.check_output(['git','-C',str(PROJECT),'show',commit+':'+path]);d=json.loads(raw)
        inherited[key]=d.get('records') if isinstance(d,dict) else d
        inputs.append({'commit':commit,'path':path,**rawid(raw),'full_original_container':d,'current_reception':'tasks/R7-H14 + tasks/R7-C17/limits-and-alias-reception.json'})
    inherited['qualification']='Original categories and fields fully retained. CurrentR7 facts separately received; no policy selected and no original ledger reopened.'
    dump('history/inherited-nonmandatory.final.json',inherited)
    rounds=[{'round':'R1','scope':'逐WP与primary主合同；不臆造问题总数'},
            {'round':'R2','controls':229,'batches':21,'owner_contributions':341},
            {'round':'R3','controls':23,'standards':76,'retain':['GR3-M09-001 optional/U08尚未启动的原时点','GR3-M02-003 NO_REQUIRED']},
            {'round':'R4','current_controls':17,'current_standards':76,'B5_then':[16,75],'qualification':'Summary残余后继有限补充来源和时点分开'},
            {'round':'R5','required_closed':92,'P2':51,'P3':41,'open':0,'optional':7,'no_required':7,'policy':6,'limits':13,'native_static':410,'schema':568,'extra_units':158,'shared_receipts':21,'dependencies':18,'solewriters':85,'contributions':262,'administrative_transfers':6,'correction_contributions':3,'retain':['唯一激活','旧FAIL/定向修订','SC-U07-001原错误与纠正']},
            {'round':'R6','required':56,'P2':39,'P3':17,'P1':0,'batches':14,'group_required':{'A':11,'B':9,'C':19,'D':9,'E':8},'stages':['实际候选接收','五组实际内容独立审查','最终登记依赖独立审查','正式ACCEPTED','CLOSED'],'open':0,'optional':8,'FLOAT':1,'policy':7,'limits':14,'no_required':1,'dependency_nodes':100,'dependency_edges':110,'retain':['U13旧FAIL/修订后PASS','14候选及14独立审查不同于实际整合','有限静态流程门不升级执行','全部实际模型/effort/tier/speed UNVERIFIED'],'source':'tasks/R7-C17/current56-contract-reception.json'}]
    dump('history/qualifications.final.json',{'schema':'r7.historical-current-qualification.v1','rounds':rounds,'nonmandatory_fixed_inputs':inputs,'original_qualification_reports':{k:(ROOT/'tasks'/k/'report.md').read_text() for k in ('R7-H10','R7-H11','R7-H12','R7-H14')},'current56':read('tasks/R7-C17/current56-contract-reception.json'),'recovery43':'history/recovery-identity-verification.json','no_old_workflow_restarted':True})
    dump('evidence/aliases-and-tombstones.final.json',{'records':[{'id':v['id'],'canonical_id':v.get('canonical_id'),'canonical_root_id':v.get('canonical_root_id'),'aliases':v.get('aliases',[]),'historical_relation':v.get('historical_relation'),'classification':v['classification']} for v in f['records']],'additional_facets':read('evidence/root-h22-counter/counter-review-and-facets.json'),'qualification':'All original proposals/objections/counters retained; no deleted identities or unsupported old-ledger reopening. No-required and optional/policy dispositions are not erased proposals.'})
    dump('coverage/current-interface-reception.json',{'schema':'r7.current-interface-reception.v1','scope':'Every current source fact retains exact necessary consumers/premises/spec facets, resolved through the final canonical source/clause indexes. Finite current material, not unbounded plugin/config composition certification.','all_source_fact_contracts':'tasks/R7-C17/canonical-source-fact-registry.json','all_clause_contracts':'tasks/R7-C17/canonical-clause-registry.json','primary_domains':'coverage/module-primary-map.json','exact_overlay_receivers':['tasks/R7-C03/map-errata.json','tasks/R7-C07/reception-results.json','tasks/R7-J09/report.md','tasks/R7-C15/report.md','tasks/R7-C16/report.md','tasks/R7-C17/late-clause-reception.json','tasks/R7-C17/data-successor-reception-02.json','tasks/R7-C17/current56-contract-reception.json'],'unreceived':[],'qualification':'Original locator joins do not create semantics; all authored subassertions and receiver narrowing remain authoritative. C17 final exact sets are zero, old WAIT snapshots preserved.'})
    dump('coverage/summary.final.json',{'schema':'r7.root-final-review-coverage.v1','status':'STATIC_REVIEW_COMPLETED_WITH_REQUIRED_REVISIONS_AND_LIMITS','root_accepted_utc':utc(),'root_actual_context':ROOT_ID,'source':{'files':432,'bytes':44906485,'read_or_precisely_disposed':432,'unread':0,'initial_text_lines':389604,'literal_and_structural_axes_separate':True},'formal':{'files':131,'bytes':4264366,'lines':29493,'structural_blocks':21702,'read_and_mapped_or_precisely_disposed':21702,'unread':0},'supplements':{'fixed_files':9,'bytes':2643357,'JSON_nodes':39434,'markdown_lines':2424,'derived_purpose_payloads':323,'unread_effective':0},'canonical_reception':c17,'exact_unreceived':unread,'findings':{'required':27,'P2':10,'P3':17,'optional_entries':7,'additional_optional_facets':2,'no_required_revision':1,'policy_entries':2},'not_proven':['完整游戏/宿主/Demo/native媒体/真实保存回放','无界配置/插件组合认证','全部机器码CFG','翻译语言质量审校'],'update_started':False})
    print(json.dumps({'assembled':'root canonical and exact coverage reception','required':27,'unread':0,'update_started':False}))
if __name__=='__main__':main()
