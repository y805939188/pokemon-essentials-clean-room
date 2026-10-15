"""Validate the actual U13 original seven-group raw slices and canonical refs."""
from pathlib import Path
import json,hashlib,datetime
from run_logged import identity
W=Path('/workspace/r7-ir-R7-U13');T=Path(__file__).parent
C=json.loads((W/'original/dispatch/delegation/contracts/R7-U13.json').read_bytes())
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':[],'scope':'U13 seven groups only; hashes are TOOL_VALIDATION'}
def visit(x,ptr=''):
    if isinstance(x,dict):
        if 'file' in x and 'file_bytes' in x and 'file_sha256' in x:
            path=W/'original/evidence/tasks/R7-C13'/x['file'];b=path.read_bytes()
            assert len(b)==x['file_bytes'] and hashlib.sha256(b).hexdigest()==x['file_sha256']
            data=json.loads(b);jp=x.get('json_pointer','')
            for k in jp.strip('/').split('/') if jp else []:data=data[int(k)] if isinstance(data,list) else data[k]
            out['checks'].append({'contract_pointer':ptr,'source_path':str(path),'source_pointer':jp,'file_identity':identity(b),'selected_json_sha256':hashlib.sha256(json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()})
        # Some transport references include byte-offset and canonical bindings.
        for k,v in x.items():visit(v,ptr+'/'+k)
    elif isinstance(x,list):
        for i,v in enumerate(x):visit(v,ptr+'/'+str(i))
visit(C)
bindings=json.loads((W/'original/evidence/tasks/R7-C13/raw-binding-manifest.json').read_bytes())
out['related_raw_bindings']=[b for b in bindings if any(s in json.dumps(b,ensure_ascii=False) for s in ['GR7-D07-001','R7-D07/','R7-C11/','ec1d2d33c2d1a0ca9de59a97f043fe86c32f04c3d6be4f5f9452ade3c807f2d3'])]
root=json.loads((W/'original/evidence/tasks/R7-C13/inputs/delta-j16/findings.json').read_bytes())['records'][30]
counter=json.loads((W/'original/evidence/tasks/R7-C13/inputs/evidence/received-final-proposals/GR7-D07-001/counter-review.json').read_bytes())
proposal=json.loads((W/'supplemental/tasks/R7-D07/findings.json').read_bytes())
canon=lambda x:hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert root['original_proposal']==proposal['findings'][0]
assert canon(root['original_proposal'])==root['proposal_canonical_sha256']
assert root['independent_adjudication']['decision_record']==counter['findings'][0]
assert root['counter_payload_not_author_update']['current_record']==counter['findings'][0]
assert canon(root['counter_payload_not_author_update']['current_record'])==root['counter_payload_not_author_update']['canonical_sha256']
out['canonical_checks']={'original_proposal_exact':True,'original_proposal_canonical_sha256':root['proposal_canonical_sha256'],'independent_counter_exact':True,'counter_preserved_separately_not_author_change':True,'C13_old_P02_raw_manifest_note':'No row for this later received proposal/counter in old P02 raw binding manifest; six explicit seven-group references and delta record30/frozen full payloads bind it. No missing row fabricated.'}
(T/'original-binding-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'seven_group_reference_checks':len(out['checks']),'related_raw_bindings':len(out['related_raw_bindings'])}))
