"""Print every selected historical value and its original locator without summarizing it."""
import json, pathlib, sys
root = pathlib.Path(__file__).resolve().parent / 'payload-audit' / 'historical-packets'
d = json.loads((root / sys.argv[1]).read_text())
rows = d if isinstance(d, list) else d['records']
a, b = int(sys.argv[2]), int(sys.argv[3])
print('COMPLETE_SELECTED_VALUES', len(rows), 'RANGE', a, b)
for i in range(a - 1, min(b, len(rows))):
    r = rows[i]
    print(json.dumps({'index': i + 1, 'pointer': r['pointer'], 'value': r['value']}, ensure_ascii=False, separators=(',', ':')))
