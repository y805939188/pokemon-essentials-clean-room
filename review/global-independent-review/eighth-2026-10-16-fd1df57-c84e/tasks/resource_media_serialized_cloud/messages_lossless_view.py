"""Build complete present-data views; no Marshal/Ruby execution or reading credit."""
import json
from pathlib import Path
from collections import defaultdict

OUT = Path(__file__).resolve().parent
tree = json.loads((OUT / 'static-recovery-001/current-serialized/messages_core.dat.json').read_text())
rows = [json.loads(x) for x in (OUT / 'subcontracts/messages-all-pairs.jsonl').read_text().splitlines()]
by_hash = defaultdict(list)
for row in rows:
    by_hash[row['hash_start']].append(row)
viewdir = OUT / 'messages-current-views'
viewdir.mkdir(exist_ok=True)
index = []
for bucket, node in enumerate(tree['root']['items']):
    if bucket == 0:
        positions = [{'position': i, 'type': x['type'], 'start': x['start'],
                      'end_exclusive': x['end_exclusive'],
                      'pairs': len(x.get('pairs', [])) if x['type'] == '{' else None}
                     for i, x in enumerate(node['items'])]
        (viewdir / 'bucket-00-positions.json').write_text(json.dumps(positions, indent=2) + '\n')
        assert all(x['type'] in ('{', '0') and not x.get('pairs') for x in node['items'])
        index.append({'bucket': bucket, 'type': '[', 'positions': len(positions), 'pairs': 0})
        continue
    assert node['type'] == '{'
    chosen = by_hash[node['start']]
    assert len(chosen) == len(node['pairs'])
    lines = ['Current exact pairs; `=` means this actual key text equals its entire actual value. '
             'Other values are printed in full. JSON escaping preserves all characters.']
    for row in chosen:
        key = json.dumps(row['key'], ensure_ascii=False)
        value = '=' if row['key'] == row['value'] else json.dumps(row['value'], ensure_ascii=False)
        lines.append(str(row['pair']) + ' ' + key + ' -> ' + value)
    name = 'bucket-' + str(bucket).zfill(2) + '.txt'
    (viewdir / name).write_text('\n'.join(lines) + '\n')
    index.append({'bucket': bucket, 'type': '{', 'source_span': [node['start'], node['end_exclusive']],
                  'hash_object': node['object_index'], 'pairs': len(chosen), 'view': name,
                  'full_key_value_equal_count': sum(x['key'] == x['value'] for x in chosen)})
assert sum(x['pairs'] for x in index) == len(rows) == 10697
(viewdir / 'index.json').write_text(json.dumps(index, indent=2) + '\n')
print(json.dumps({'complete_present_pairs': len(rows), 'buckets': len(index),
                  'semantic_reading_credit': 0, 'target_execution': False}))
