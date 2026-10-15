"""Inventory every nonself evidence file; actual Git/remote readback binds self."""
from pathlib import Path
import json,datetime,os
from run_logged import identity
E=Path(__file__).resolve().parent.parent;rows=[]
for p in sorted(E.rglob('*')):
    if not p.is_file() or p==E/'artifact-manifest.json':continue
    assert not p.is_symlink() and '__pycache__' not in p.parts,p
    rows.append({'path':str(p.relative_to(E)),'mode':'100644',**identity(p.read_bytes())})
d={'schema':'r7.u13.actual-ir.artifact-manifest.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pid':os.getpid(),'batch':'R7-U13','verdict_scope':'GR7-D07-001 PASS_SCOPED_ACTUAL_INTEGRATION only','files_nonself':len(rows),'bytes_nonself':sum(r['bytes'] for r in rows),'artifacts':rows,'self_binding':'Excluded from its own table. The actual immutable result commit/tree and full every-file remote readback bind this manifest as an ordinary file. No guessed final hash or recursive attestation.','runtime_credit':False,'effective_configuration':'UNVERIFIED','ACCEPTED':False,'CLOSED':False}
(E/'artifact-manifest.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'files_nonself':len(rows),'bytes_nonself':d['bytes_nonself']}))
