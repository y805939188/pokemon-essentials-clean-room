"""REG read-only evidence navigation and local checkpoint serialization.

Never executes reference code; only git show and text/JSON parsing.
"""
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
B = '9366d9d17aaeac3b4414236468affa650fb3dd27'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REF = Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
R4PATH = 'review/remediation-fourth-20261012-prepare/registration/R4-U06/findings-and-criteria.json'
R3PATH = 'review/remediation-third-20261012-prepare/U07/actual-integration/required23-matrix.json'
BASE = {'schema_version': 'gr5.review.v1', 'module': 'REG', 'reviewer': 'REG independent historical regression reviewer', 'specification_baseline': B, 'source_baseline': R, 'model_request': {'requested_model': 'gpt-6-astra', 'requested_reasoning_effort': 'ultra', 'requested_service_tier': 'default', 'actual_parameters': 'UNVERIFIED', 'fast': 'not_requested', 'configuration_investigation': False}, 'execution_status': 'NOT_EXECUTED; static review only'}

def fixed(path, version=B, repo=ROOT):
    return subprocess.check_output(['git', '-C', str(repo), 'show', version+':'+path]).decode('utf-8')

def jfixed(path, version=B, repo=ROOT):
    return json.loads(fixed(path, version, repo))

def save(name, data):
    temp=HERE/(name+'.tmp')
    temp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    temp.replace(HERE/name)

def read(path, ranges=None, source=False, version=None):
    text = fixed(path, version or (R if source else B), REF if source else ROOT)
    lines = text.splitlines()
    print('\nFILE',path,'VERSION',version or (R if source else B),'TOTAL',len(lines))
    for a,b in ranges or [(1,len(lines))]:
        for n in range(a,min(b,len(lines))+1): print(f'{n}: {lines[n-1]}')

def checkpoint(label, source_entries, spec_entries, judgments, next_scope):
    coverage=json.loads((HERE/'reading-coverage.json').read_text())
    refs=[]
    for entries,key,version,repo in [(source_entries,'sources',R,REF),(spec_entries,'specifications',B,ROOT)]:
        for path,ranges,rule,comparison in entries:
            total=len(fixed(path,version,repo).splitlines())
            read_set={n for a,b in ranges for n in range(a,b+1)}
            missing=[]
            for n in range(1,total+1):
                if n not in read_set:
                    if missing and missing[-1][1]==n-1: missing[-1][1]=n
                    else: missing.append([n,n])
            row={'id':f'REG-{label}-{key}-{len(coverage[key])+1:03d}','path':path,'version':version,'line_count':total,'read_ranges':ranges,'semantic_ranges':[{'lines':[a,b],'entry_or_rule':rule,'comparison':comparison} for a,b in ranges],'review_extent':'partial' if missing else 'full','material_availability':'available_text','evidence_level':'SOURCE_STATIC' if key=='sources' else 'SPEC_STATIC','unreviewed_intervals':missing,'extent_boundary':'REG finite historical scope; unread file intervals are not claimed reviewed by REG'}
            coverage[key].append(row);refs.append({'path':'reading-coverage.json','pointer':'/'+key+'/'+str(len(coverage[key])-1),'id':row['id']})
    save('reading-coverage.json',coverage)
    for name in ['regression-fourth-17.json','regression-third-23.json']:
        d=json.loads((HERE/name).read_text())
        for record in d['records']:
            if record['id'] not in judgments: continue
            per=judgments[record['id']]
            assert len(per)==len(record['criteria']),(record['id'],len(per),len(record['criteria']))
            for c,assessment in zip(record['criteria'],per):
                c['current_R5_semantic_review']={'status':'supported','evidence_level':'supported_static','boundary':'Static source/specification regression only; no reference/model/host execution, no transfer of historical acceptance.','assessment':assessment,'evidence':refs}
            record['current_R5_semantic_review']={'status':'supported','evidence_level':'supported_static','supported_boundary':'All listed finite criteria independently compared against R and B5; wider feature/global/domain completion not claimed.','evidence':refs,'fresh_global_review_join':'not_reviewed; to map exact fresh capability records separately','checkpoint':label}
        save(name,d)
    for filename,key in [('source-to-spec.json','capabilities'),('spec-to-source.json','clauses')]:
        d=json.loads((HERE/filename).read_text())
        for id,assessments in judgments.items():
            d[key].append({'id':'REG-'+id,'historical_control':id,'current_R5_semantic_review':True,'historical_identity_scope_reuse':'criteria, premises, exclusions and identity only','status':'supported','evidence_level':'supported_static','execution_status':'NOT_EXECUTED','comparison':assessments,'source_anchors':[{'path':p,'version':R,'lines':r,'scope':s} for p,r,s,c in source_entries],'spec_anchors':[{'path':p,'version':B,'lines':r,'scope':s} for p,r,s,c in spec_entries],'coverage_refs':refs})
        save(filename,d)
    d=json.loads((HERE/'progress.json').read_text());d['completed_finite_reviews']+=list(judgments);d['next_actual_scope']=next_scope;d['last_checkpoint']=label;save('progress.json',d)
    (HERE/'progress.md').write_text('# REG 当前进度\n\ncomplete=false；静态审查，未执行参考或模型。参数实际回显 UNVERIFIED。\n\n已逐条直接核对：'+', '.join(d['completed_finite_reviews'])+'。\n\n下一实际范围：'+next_scope+'。\n\nGR4 17/76、GR3 23/76 分开；229/341精确范围与最新主审记录 join 尚未完成。历史 CLOSED/PASS 未转签。本目录JSON为可续接检查点。\n')

def bootstrap():
    r4=jfixed(R4PATH);r3=jfixed(R3PATH)
    for filename,raw,is4 in [('regression-fourth-17.json',r4,True),('regression-third-23.json',r3,False)]:
        records=[]
        for i,r in enumerate(raw['records']):
            old=r['canonical_background']['record'] if is4 else r['canonical']['complete_record']
            criteria=r['all_actual_criterion_results'] if is4 else r['acceptance_criteria']
            out=[]
            for j,c in enumerate(criteria):
                if isinstance(c,str): c={'criterion':c}
                wording=c.get('criterion',c.get('complete_criterion',c.get('text')))
                out.append({'criterion_id':c.get('criterion_id',r['id']+'/C'+str(j+1).zfill(2)),'historical_input_pointer':f'/records/{i}/'+('all_actual_criterion_results' if is4 else 'acceptance_criteria')+f'/{j}','criterion':wording,'kind':c.get('kind',wording.get('kind','static_or_boundary') if isinstance(wording,dict) else 'static_or_boundary'),'current_R5_semantic_review':{'status':'not_reviewed','evidence':[]}})
            records.append({'id':r['id'],'title':old['title'],'batch_owner':r['batch'],'historical_identity_scope_reuse':{'input':R4PATH if is4 else R3PATH,'version':B,'pointer':f'/records/{i}','qualification':'Identity, original acceptance scope and criteria only. Historical PASS/CLOSED not reused as current evidence.','original_scope':{k:old[k] for k in ['preconditions','premises','excluded_claims','unknowns','historical_relation','history_links'] if k in old},'acceptance_reference':r.get('exact_qualified_chain',{}).get('acceptance') if is4 else r['current_local_receipt']},'criteria':out,'current_R5_semantic_review':{'status':'not_reviewed','evidence':[],'supported_boundary':None}})
        save(filename,{**BASE,'complete':False,'denominator':{'records':len(records),'criteria':sum(len(r['criteria']) for r in records),'not_interchangeable_with_other_round':True},'records':records})
    save('reading-coverage.json',{**BASE,'complete':False,'sources':[],'specifications':[],'historical_inputs':[], 'fresh_review_inputs':[]})
    save('source-to-spec.json',{**BASE,'complete':False,'capabilities':[]})
    save('spec-to-source.json',{**BASE,'complete':False,'clauses':[]})
    save('shared-interfaces.json',{**BASE,'complete':False,'interfaces':[]})
    save('findings.json',{**BASE,'complete':False,'findings':[]})
    save('progress.json',{**BASE,'complete':False,'status':'in_progress','completed_finite_reviews':[],'next_actual_scope':'R4/GR3 localization source and current full contracts','pending_joins':[]})

if __name__=='__main__':
    raise SystemExit('REG evidence helper module; import explicit helpers. Completed review artifacts are not bootstrapped or overwritten by direct invocation.')
