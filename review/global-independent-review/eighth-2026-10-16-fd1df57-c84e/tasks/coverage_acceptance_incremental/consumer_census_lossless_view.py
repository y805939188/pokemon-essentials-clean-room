"""Lossless repeated-path representation of a frozen lexical census.
No claim is omitted or upgraded; source reading and acceptance stay separate.
"""
from pathlib import Path
import hashlib, json, datetime
root = Path(__file__).resolve().parent
source = root / 'fact-views/152.semantic-fields.json'
raw = source.read_bytes()
data = json.loads(raw)
paths = []
def path_id(path):
    if path not in paths:
        paths.append(path)
    return paths.index(path)
rows = []
restored = {k:v for k,v in data.items() if k not in {'settings','stats'}}
for section in ['settings', 'stats']:
    restored[section] = {}
    for name, value in data[section].items():
        assert set(value) == {'declarations','references'}
        declarations = []
        references = []
        for row in value['declarations']:
            assert set(row) == {'path','line'}
            declarations.append([path_id(row['path']), row['line']])
        for row in value['references']:
            assert set(row) == {'path','line','file_read','semantic_consumer_acceptance'}
            assert row['semantic_consumer_acceptance'] == 'PENDING_CROSS_DOMAIN_JOIN'
            references.append([path_id(row['path']), row['line'], row['file_read']])
        rows.append({'section':section,'name':name,'declarations_pathID_line':declarations,'references_pathID_line_author_file_read':references,'every_reference_semantic_consumer_acceptance':'PENDING_CROSS_DOMAIN_JOIN'})
        restored[section][name] = {'declarations':[{'path':paths[p],'line':n} for p,n in declarations], 'references':[{'path':paths[p],'line':n,'file_read':r,'semantic_consumer_acceptance':'PENDING_CROSS_DOMAIN_JOIN'} for p,n,r in references]}
assert restored == data
assert len(rows) == 195
lines = [json.dumps({'all_root_fields':{k:v for k,v in data.items() if k not in {'settings','stats'}},'representation':'Exact repeated path table. Each reference preserves file_read bool; no source meaning inferred.'},ensure_ascii=False)]
lines += [json.dumps({'pathID':i,'exact_path':p},ensure_ascii=False) for i,p in enumerate(paths)]
lines += [json.dumps(row,ensure_ascii=False,separators=(',',':')) for row in rows]
rendered = '\n'.join(lines)+'\n'
(root / 'consumer-census-lossless.txt').write_text(rendered)
receipt = {'source':str(source.relative_to(root)), 'source_bytes':len(raw), 'source_sha256':hashlib.sha256(raw).hexdigest(), 'rendering_lines':len(lines), 'rendering_bytes':len(rendered.encode()),'rendering_sha256':hashlib.sha256(rendered.encode()).hexdigest(),'symbols':len(rows),'paths':len(paths),'all_fields_exactly_reconstructed':True,'source_credit':False,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(root / 'consumer-census-lossless-view-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
