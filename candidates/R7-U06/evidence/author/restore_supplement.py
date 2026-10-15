"""Restore only four newly named raw-binding dependencies from immutable C2."""
from pathlib import Path
import importlib.util
import json
import subprocess
import sys
import threading
sys.dont_write_bytecode = True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
DEST=Path('/workspace/r7-context/R7-U06-author')
C2='4580645dfbfec4a3c7ccbad56ae293cc619b0d25'
tool=Path('/workspace/r7-bootstrap/R7-U06-author/tools/restore_container_context.py')
assert tool.read_bytes()==subprocess.check_output(['git','show','658488c81f1f3181a488298ab27850c8af951d73:review/remediation-seventh-20261015-prepare/tools/restore_container_context.py'],cwd=ROOT)
spec=importlib.util.spec_from_file_location('fixed_restore',tool)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
bindings=json.loads((DEST/'evidence/tasks/R7-C13/raw-binding-manifest.json').read_bytes())
shas={'3290b8a77f8f3779c8726b32d7a53573fbdcaeea8149487246f4a9a500db1c51',
      '9f68b18a4a3f12cff0b452977d24171aca0165b74f3a50a615c95f9927f9765c',
      '7810265e729eb25b29a846b97112b7eea9c171e4cb5e9c98376dd162bca2fe37',
      '54cdf48d7ddd401574d9cc04471d9478511d0bd4b609bd95eab845d10fc343fe'}
found={}
def walk(obj):
    if isinstance(obj,dict):
        if obj.get('sha256') in shas:found[obj['sha256']]=obj
        for v in obj.values():walk(v)
    elif isinstance(obj,list):
        for v in obj:walk(v)
walk(bindings)
assert set(found)==shas
rows=[]
for sha, bound in sorted(found.items()):
    transport=f'objects/{sha[:2]}/{sha}.gz'
    path='review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-transport/core/'+transport
    encoded=subprocess.check_output(['git','show',C2+':'+path],cwd=ROOT)
    rows.append(dict(logical_path='tasks/R7-C13/'+bound['c13_snapshot'],transport_path=transport,
        bytes=bound['bytes'],sha256=sha,git_blob_content_id=bound['content_git_blob'],
        repository='y805939188/pokemon-essentials-clean-room',commit=C2,path=path,
        encoded_identity=module.identity(encoded),local_path='evidence/tasks/R7-C13/'+bound['c13_snapshot']))
    module.TRANSPORT_LOCKS[transport]=threading.Lock()
(HERE/'supplemental-plan.json').write_text(json.dumps(rows,indent=2)+'\n')
receipt={'start_utc':module.utc(),'qualification':'Bounded named dependencies, not a whole-package scan; identity only.', 'files':[]}
try:
    for row in rows:receipt['files'].append(module.restore_one(DEST,row,encoded=True))
    receipt['status']='SUPPLEMENT_BYTES_VERIFIED'
except Exception as error:
    receipt['status']='PARTIAL_PRESERVED'
    receipt['error']=str(error)
    raise
finally:
    receipt['end_utc']=module.utc()
    (HERE/'supplemental-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':receipt['status'],'files':len(receipt['files']),'bytes':sum(x['bytes'] for x in receipt['files'])}))
