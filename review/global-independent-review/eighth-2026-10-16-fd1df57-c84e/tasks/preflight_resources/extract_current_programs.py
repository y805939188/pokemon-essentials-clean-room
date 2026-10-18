"""Recheck historical literal locators against R bytes, then extract without executing.
Old locators are navigation only. Identity verification earns no semantic credit.
"""
from pathlib import Path
import collections,hashlib,json
ROOT=Path(__file__).resolve().parent
REF=Path('/workspace/pokemon-essentials')
OLD=ROOT/'recovered-resource-evidence/tasks/R7-D09/program-unit-dispositions.json'
OUT=ROOT/'current-programs-v2'
OUT.mkdir(exist_ok=False)
units=json.loads(OLD.read_text())['units']
records=[]
for row in units:
    source=row.get('source',{})
    if row.get('kind') not in ['GLSL_LITERAL_OR_PRELUDE','C_TEMPLATE_FRAGMENT','EMBEDDED_RUBY_COMPATIBILITY_TEXT','X86_SMALL_PROGRAM']: continue
    path=source['path']; start,end=source['bytes']; b=(REF/path).read_bytes()[start:end]
    if 'sha256' in source:
        assert hashlib.sha256(b).hexdigest()==source['sha256'],row['id']
    kind=row['kind']; target=OUT/(row['id']+('.bin' if kind=='X86_SMALL_PROGRAM' else '.txt'))
    target.write_bytes(b)
    records.append({'id':row['id'],'kind':kind,'path':path,'start':start,'end_exclusive':end,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'lines':len(b.splitlines()),'extracted_path':str(target.relative_to(ROOT)),'semantic_status':'UNREAD','behavior_executed':False})
(OUT/'inventory.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files':len(records),'kinds':dict(collections.Counter(x['kind'] for x in records)),'bytes':sum(x['bytes'] for x in records),'executed_programs':0}))
