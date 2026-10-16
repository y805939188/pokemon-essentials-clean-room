"""Fresh isolated copy of fully read JSON-only table helper, for existing exact views."""
import datetime,hashlib,json,re,sys
from pathlib import Path
OWN=Path(__file__).resolve().parent
relative,label=sys.argv[1:]
assert re.fullmatch('[a-z0-9-]+',label)
p=OWN/relative
assert p.resolve().is_relative_to(OWN)
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
raw=p.read_bytes();original=json.loads(raw)
def exact_json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
def encode(value):
    if isinstance(value, dict):
        assert '$exact_table' not in value and '$exact_blocks' not in value
        return {key: encode(child) for key, child in value.items()}
    if isinstance(value, list):
        if len(value) >= 2 and all(isinstance(row, dict) and set(row) == set(value[0]) for row in value):
            common = {key: value[0][key] for key in value[0] if all(exact_json(row[key]) == exact_json(value[0][key]) for row in value)}
            columns = [key for key in value[0] if key not in common]
            return {'$exact_table': {'common_fields_for_every_row': encode(common), 'varying_columns_in_order': columns, 'rows_in_original_order': [[encode(row[key]) for key in columns] for row in value]}}
        if len(value) >= 2 and all(isinstance(row, dict) for row in value):
            groups = []
            for row in value:
                if not groups or set(groups[-1][0]) != set(row):
                    groups.append([])
                groups[-1].append(row)
            return {'$exact_blocks': [encode(group) for group in groups]}
        return [encode(child) for child in value]
    return value
def decode(value):
    if isinstance(value, dict):
        if set(value) == {'$exact_blocks'}:
            return [row for block in value['$exact_blocks'] for row in decode(block)]
        if set(value) == {'$exact_table'}:
            table = value['$exact_table']
            common = decode(table['common_fields_for_every_row'])
            return [dict(common, **dict(zip(table['varying_columns_in_order'], [decode(child) for child in row]))) for row in table['rows_in_original_order']]
        return {key: decode(child) for key, child in value.items()}
    if isinstance(value, list):
        return [decode(child) for child in value]
    return value
def display(value, depth=0):
    pad = ' ' * depth
    if isinstance(value, dict):
        return '{\n' + ',\n'.join(' '*(depth+1)+json.dumps(key,ensure_ascii=False)+': '+display(child,depth+1) for key,child in value.items())+'\n'+pad+'}'
    if isinstance(value, list):
        if all(not isinstance(child,(list,dict)) for child in value):
            return json.dumps(value, ensure_ascii=False)
        return '[\n'+',\n'.join(' '*(depth+1)+display(child,depth+1) for child in value)+'\n'+pad+']'
    return json.dumps(value, ensure_ascii=False)

encoded=encode(original)
assert exact_json(decode(encoded))==exact_json(original)
out=OWN/(label+'-columnar-existing-view.json')
assert not out.exists()
text=display(encoded)+'\n'
assert json.loads(text)==encoded
out.write_text(text)
r={'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':0,'input':relative,'input_bytes':len(raw),'input_sha256':hashlib.sha256(raw).hexdigest(),'output':out.name,'output_bytes':len(text.encode()),'output_lines':len(text.splitlines()),'output_sha256':hashlib.sha256(text.encode()).hexdigest(),'exact_decode_equals_input_view':True,'generation_reading_credit':0}
(OWN/(label+'-columnar-existing-generation.json')).write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r))
