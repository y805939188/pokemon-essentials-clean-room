"""Extract exact bounded qualification fields; no behavioral code is loaded."""
import datetime, hashlib, json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5]
OUT=Path(__file__).resolve().parent
records=[]
def read(ref,path):
    data=subprocess.check_output(['git','show',ref+':'+path],cwd=ROOT)
    return json.loads(data),dict(commit=ref,path=path,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=subprocess.check_output(['git','rev-parse',ref+':'+path],cwd=ROOT,text=True).strip())
def add(identity,pointer,value):
    records.append(dict(payload=identity,pointer=pointer,value=value,record_sha256=hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()))
r5='c0ff33024aea424c68d29f9778fe7c8e807d21e8'
base='review/global-independent-review/fifth-2026-10-13-9366d9d-c7d3/'
d,identity=read(r5,base+'regression-legacy-scope.json')
for i in [6,10,15,20,22,23,106,151,203]:
    x=d['controls'][i]
    add(identity,f'/controls/{i}/historical_identity_scope_reuse',x['historical_identity_scope_reuse'])
    add(identity,f'/controls/{i}/current_B5_paths',x['current_B5_paths'])
for i in [5,14]:
    x=d['contributions'][i]
    for field in ['historical_identity_scope_reuse','original_contribution_scope','accepted_local_scope_fields','accepted_local_scope_extraction']:
        add(identity,f'/contributions/{i}/{field}',x[field])
for file,indices in [('regression-third-23.json',[0,1,2]),('regression-fourth-17.json',[0,1])]:
    d,identity=read(r5,base+file)
    for i in indices:
        add(identity,f'/records/{i}/historical_identity_scope_reuse',d['records'][i]['historical_identity_scope_reuse'])
        for j,x in enumerate(d['records'][i]['criteria']):
            for field in ['criterion_id','historical_input_pointer','criterion','kind']:
                add(identity,f'/records/{i}/criteria/{j}/{field}',x[field])
selected={'GR5-M01-002','GR5-M01-003','GR5-M01-008','GR5-M01-009','GR5-M01-012','GR5-M01-013','GR5-M01-016','GR5-M01-017','GR5-M01-006','GR5-M05-006','GR5-M12-101','GR5-M04-002','GR5-M10-011'}
accepted='13fddb0a217b36974c75657aa68da0caf104ee48'
prep='review/remediation-fifth-20261013-prepare/'
for batch in ['R5-U01','R5-U03','R5-U06','R5-U07']:
    d,identity=read(accepted,prep+'contracts/'+batch+'/task-packet.json')
    findings=d['findings']
    for i,x in enumerate(findings):
        if x['id'] in selected:
            for field in ['id','acceptance_criteria']:
                add(identity,f'/findings/{i}/{field}',x[field])
            for field in ['premises','retained_scope','minimum_revision','history_relationship']:
                if field in x:add(identity,f'/findings/{i}/{field}',x[field])
d,identity=read('12df95a8e81061a606d50d3f0a0528793b2e6b2c',prep+'registration/successors/20261014-final-activation/activation-receipt.json')
add(identity,'',d)
output=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='Exact selected fields with original JSON pointers, not summaries. Unselected historical review payload is not claimed read.',records=records)
(OUT/'historical-qualified-spans.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(selected_fields=len(records),bytes=(OUT/'historical-qualified-spans.json').stat().st_size,semantic_read='PENDING_DISPLAY_AND_INSPECTION')))
