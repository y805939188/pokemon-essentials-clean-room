"""Mechanical validation only: original bytes, IDs, ranges and deliverables. No semantic inference."""
from pathlib import Path
import json,gzip,hashlib,collections
P=Path(__file__).resolve().parent
read=lambda n:json.loads((P/n).read_text())
def rows(n):return [json.loads(l) for l in (gzip.open(P/n,'rt') if n.endswith('.gz') else (P/n).open())]
a=rows('remaining-unread.jsonl');b=rows('full-disposition-ledger.jsonl.gz');assert len(a)==len(b)==57948
key=('candidate_id','path','inventory_line','encoding','start','end_exclusive','sha256');assert [[x[k] for k in key] for x in a]==[[x[k] for k in key] for x in b]
assert len({x['candidate_id'] for x in b})==57948
m=read('bidirectional-mapping.json');assert len(m['source_texts'])==41849;assert len(m['candidate_to_read_id'])==57948
lookup={r['candidate_id']:t for t in rows('remaining-text-readset.jsonl') for r in t['refs']};src={n:Path('/workspace/pokemon-essentials',n).read_bytes() for n in {x['path'] for x in a}}
for x in b:
 raw=src[x['path']][x['start']:x['end_exclusive']];assert hashlib.sha256(raw).hexdigest()==x['sha256'];assert len(raw)==x['bytes'];text=raw.decode('ascii' if x['encoding']=='ascii' else 'utf-16-le');assert text==lookup[x['candidate_id']]['text'];assert x['read_id']==lookup[x['candidate_id']]['read_id'];assert m['candidate_to_read_id'][x['candidate_id']]==x['read_id']
assert collections.Counter(x['path'] for x in b)=={'Game.exe':37041,'x64-msvcrt-ruby310.dll':20817,'zlib1.dll':90}
continuation=read('game-continuation-readset.json');part=read('continuation-partition.json');covered={x['original_view_line'] for x in part['covered_rows']};assert len(covered)==1539;cs={x['original_view_line'] for x in continuation};assert len(cs)==11615;assert not cs&covered;assert cs|covered==set(range(10451,23605))
validids={x['candidate_id'] for x in b if x['path']=='Game.exe' and x['semantic_status']!='FULL_LITERAL_READ_WITH_CONSUMER_AND_TYPE_LIMITS'}
for q in part['covered_rows']:assert set(q['covered_candidate_ids'])<=validids
new=read('new-program-and-data-inventory.json');assert len(new['units'])==16
byid={x['candidate_id']:x for x in b}
for u in new['units']:
 assert set(u['candidate_ids'])<=set(byid)
 if 'start' in u:
  z=src['Game.exe'][u['start']:u['end_exclusive']];assert hashlib.sha256(z).hexdigest()==u['sha256'] and len(z)==u['bytes']
  assert all(u['start']<=byid[c]['start'] and byid[c]['end_exclusive']<=u['end_exclusive'] for c in u['candidate_ids'])
required=['progress.json','identities.json','full-disposition-ledger.jsonl.gz','reading-ledger.json','bidirectional-mapping.json','consumers.json','remaining.json','proposals.json','review.md']
for n in required:assert (P/n).stat().st_size>0
for n in required:
 if n.endswith('.json'):read(n)
rem=read('remaining.json');openids=[x['candidate_id'] for x in b if x['path']=='Game.exe' and x['semantic_status']=='FULL_LITERAL_READ_WITH_CONSUMER_AND_TYPE_LIMITS'];assert rem['Game_open_candidate_ids']==openids and len(openids)==18166
rl=read('reading-ledger.json');assert rl['finite_coverage']['Game_original_view_lines']+rl['finite_coverage']['Game_continuation_lines']+rl['finite_coverage']['original_removed_exact_type_or_controller_covered_rows']==23604
assert len(read('proposals.json')['discoveries'])==5
for p in read('proposals.json')['discoveries']:assert len(p['eight_sections'])==8
print(json.dumps({'validation':'TOOL_VALIDATION_ONLY','candidate_rows':57948,'distinct_texts':41849,'original_raw_bytes_all_verified':True,'candidate_sets_unique_complete':True,'Game_literal_open_semantic_boundaries':18166,'new_Game_units':16,'no_target_execution':True,'source_sha256':{k:hashlib.sha256(v).hexdigest() for k,v in src.items()}}))
