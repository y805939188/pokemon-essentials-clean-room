import json, subprocess, hashlib, re, datetime
from pathlib import Path
from collections import Counter
OUT=Path(__file__).resolve().parent
MAIN='8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
FIFTH='f49d870c6fd616ab6736754a218a4553b5acac7f'
ACTUAL='debf59f3c5370df253706969fd4dd1c103300bf2'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
H='review/global-independent-review/fifth-2026-10-13-9366d9d-c7d3/'
P='review/remediation-fifth-20261013-prepare/'
inputs=[]; checks=[]
def fetch(commit,path,ref=False):
    cmd=['git','-C','reference/pokemon-essentials'] if ref else ['git']
    raw=subprocess.check_output(cmd+['show',commit+':'+path])
    inputs.append({'commit':commit,'path':path,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'read_mode':'STRUCTURAL_TOOL_VALIDATION_NOT_SEMANTIC_PASS'})
    return raw
def obj(commit,path):return json.loads(fetch(commit,path))
def check(name,value,detail=None):checks.append({'check':name,'result':'PASS'if value else'FAIL','evidence':detail,'evidence_level':'TOOL_VALIDATION'})
def digest(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
f=obj(FIFTH,H+'findings.json'); q=obj(MAIN,P+'registration/quarantined-scope.json'); u=obj(FIFTH,H+'unresolved-decisions.json')
count=Counter(x['disposition']for x in f['findings']); sev=Counter(x['severity']for x in f['findings']if x['disposition']=='required')
check('106 canonical IDs, 92 required + 7 optional + 7 no-required',len({x['id']for x in f['findings']})==106 and count=={'required':92,'optional':7,'no_required_revision':7},dict(count))
check('51 P2 and 41 P3 are required-only severity units',sev=={'P2':51,'P3':41},dict(sev))
oldq=[x for x in f['findings']if x['disposition']!='required']; check('all 14 quarantined full records unchanged',q['findings']==oldq,{'IDs':[x['id']for x in oldq]})
check('all six policy full records and boundaries unchanged',q['policy']==u and len(u['decisions'])==6,{'IDs':[x['id']for x in u['decisions']]})
oldlimits=fetch(FIFTH,H+'limits-and-missing-materials.md'); newlimits=fetch(MAIN,P+'frozen-input/limits-and-missing-materials.md')
check('13 material/host limits byte-identical',oldlimits==newlimits and len(re.findall(rb'^\| L\d\d ',oldlimits,re.M))==13)
reg=obj(FIFTH,H+'regression-fourth-17.json'); orig=obj(MAIN,'review/remediation-fourth-20261012-prepare/registration/R4-U06/findings-and-criteria.json')
records=reg['records']; cs=[x for r in records for x in r['criteria']]; status=Counter(r['current_R5_semantic_review']['status']for r in records); cstatus=Counter(x['current_R5_semantic_review']['status']for x in cs)
check('R4 original 17 records/76 criteria present',len(records)==17 and len(cs)==76 and len({x['criterion_id']for x in cs})==76)
check('B5 supported16/75; sole partial GR4-M04-001/C01',status=={'supported':16,'partial':1}and cstatus=={'supported':75,'partial':1}and[x['criterion_id']for x in cs if x['current_R5_semantic_review']['status']=='partial']==['GR4-M04-001/C01'],{'records':dict(status),'criteria':dict(cstatus)})
check('fixed main original R4 17/76 scope remains',len(orig['records'])==17 and sum(len(r['all_actual_criterion_results'])for r in orig['records'])==76 and [r['id']for r in orig['records']]==[r['id']for r in records])
hist=obj(MAIN,P+'integration/R5-U08/candidate-01/historical-regression-input.json'); h4=[r for r in hist['records']if r['historical_file']=='regression-fourth-17.json']
bindings=[]
for i,(old,new)in enumerate(zip(records,h4)):
    scope=old['historical_identity_scope_reuse']; bindings.append({'id':old['id'],'owner':old['batch_owner'],'record_pointer':f'/records/{i}','record_digest_match':digest(old)==new['frozen_record']['record_sha256'],'scope_digest_match':digest(scope)==new['qualified_scope_binding']['record_sha256'],'tuple_match':new['qualified_scope_binding']['required_identity_tuple']=={'id':old['id'],'record_key':None,'batch_owner':old['batch_owner']}})
check('all17 exact original record/owner/qualified-scope bindings',len(h4)==17 and all(x['record_digest_match']and x['scope_digest_match']and x['tuple_match']for x in bindings))
err=obj(MAIN,P+'registration/successors/20261013-candidate-progress-u05-u07/SC-U07-001-erratum.json');receipt=obj(MAIN,P+'registration/successors/20261014-u07-formal-acceptance/U07-formal-acceptance.json')
check('SC eight wrong fields + 32 normal/1 corrected; no false PASS',len(err['original_wrong_claim_locations'])==8 and err['U07_signed_standard_counts']=={'normal_scoped_static':32,'premise_corrected_scoped_static':1} and not err['false_original_subclaim_marked_PASS'])
check('SC current actual receipt excludes wrong author field',receipt['SC_U07_001']['excluded_author_field']['status']=='INHERITED_WRONG_CROSS_BODY_LF_CLAUSE_SIGNATURE_EXCLUDED_NOT_CURRENT_FACT' and not receipt['SC_U07_001']['false_original_cross_body_LF_subclaim_PASS'])
src=fetch(R,'Data/Scripts/021_Compiler/004_Compiler_MapsAndEvents.rb',True).decode().splitlines(); predicates=[src[i-1].strip()for i in [1000,1016,1034,1053,1075,1100]]
check('six fixed-source predicates: plain dot body + line anchors; no m/inline option',all('(.+)'in l and '^'in l and '$/'in l and '(?'not in l and not l.endswith('/m]')for l in predicates),{'source_lines':[1000,1016,1034,1053,1075,1100],'source_execution':False})
boundary=obj(ACTUAL,P+'reviews/R5-U08/actual/round-01/boundary-results.json')
check('current actual boundary sets preserve all 7/7/6/13 original IDs',set(boundary['optional']['IDs'])=={x['id']for x in oldq if x['disposition']=='optional'} and set(boundary['no_required']['IDs'])=={x['id']for x in oldq if x['disposition']=='no_required_revision'} and set(boundary['named_policy']['IDs'])=={x['id']for x in u['decisions']} and boundary['named_material_host_limits']['IDs']==[f'L{i:02d}'for i in range(1,14)])
activation=obj(MAIN,P+'registration/successors/20261014-final-activation/activation-receipt.json');check('current activation excludes 7/7/6/13 and preserves bounded Summary/LF history',activation['preserved_exclusions']['optional']==7 and activation['preserved_exclusions']['noRequired']==7 and activation['preserved_exclusions']['independent_compatibility_policy']==6 and activation['preserved_exclusions']['material_host_limits']==13 and activation['effective_counts']['CLOSED']==92 and activation['effective_counts']['OPEN_REQUIRED']==0)
evidence_structure=[]
def walk(v,pointer=''):
    if isinstance(v,dict):
        yield pointer,'object',len(v)
        for k,x in v.items():yield from walk(x,pointer+'/'+str(k).replace('~','~0').replace('/','~1'))
    elif isinstance(v,list):
        yield pointer,'array',len(v)
        for i,x in enumerate(v):yield from walk(x,pointer+'/'+str(i))
    else:yield pointer,type(v).__name__,None
for i,r in enumerate(records):
    nodes=list(walk(r)); evidence_structure.append({'id':r['id'],'pointer':f'/records/{i}','all_nodes_visited':len(nodes),'schema_types':dict(Counter(t for _,t,_ in nodes)),'scope_semantic_projection_read':True,'criteria_semantic_projection_read':len(r['criteria']),'evidence_generated_address_layers':'FULL_STRUCTURE_ONLY; underlying old game findings not re-signed','leaf_assertions_not_read_individually':[p for p,t,_ in nodes if t=='str' and ('fresh_global_review_join'in p or '/evidence/'in p)]})
result={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'evidence_level':'TOOL_VALIDATION_ONLY','inputs':inputs,'checks':checks,'failures':sum(x['result']=='FAIL'for x in checks),'R4_bindings':bindings,'R4_full_structure_disposition':evidence_structure,'semantic_PASS':False,'new_reference_execution':0,'new_independent_model_execution':0,'new_host_Demo_execution':0}
(OUT/'qualification-tool-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
with(OUT/'reading-ledger.jsonl').open('a')as f:f.write(json.dumps({'mode':'FULL_STRUCTURE_TOOL_VALIDATION','inputs':inputs,'checks':len(checks),'failure_count':result['failures'],'semantic_pass':False},ensure_ascii=False)+'\n')
print(json.dumps({'checks':len(checks),'failures':result['failures'],'summary':checks,'outputs':['qualification-tool-validation.json']},ensure_ascii=False))
