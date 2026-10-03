"""Independent reviewer: read-only identities, literal tables and fixed arithmetic.
No Ruby evaluation, game simulation, random sampling, or main-workspace writes.
"""
from pathlib import Path
from collections import Counter
import hashlib, json, re, subprocess

B = Path('/Users/dingshinn/Desktop/pokemon-spec-parallel-minigames')
MAIN = Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
REF = MAIN/'reference/pokemon-essentials'
OUT = B/'review/wp68-wp70-review-2026-09-30'
COMMIT = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'

def meta(p):
    content = p.read_bytes()
    return {'sha256': hashlib.sha256(content).hexdigest(), 'bytes': len(content)}

def matches(p, row):
    return p.is_file() and meta(p) == {k: row[k] for k in ('sha256', 'bytes')}

def read(p): return json.loads(p.read_text())
def save(n, data): (OUT/n).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

frozen = read(OUT/'input-manifest.json')['inputs']
assert len(frozen) == 48
assert all(matches(B/x['path'], x) and matches(OUT/'input-snapshot'/x['path'], x) for x in frozen)
ctx = read(B/'delivery/input-manifest.json')
context = []
for group in ('frozen_inputs', 'review_authority', 'handoff_inputs'):
    for row in ctx[group]:
        original = Path(row.get('frozen_source_path') or row['path'])
        local = Path(row['local_copy_path'])
        assert matches(original, row) and matches(local, row)
        context.append({'path': str(local.relative_to(B)), 'source': str(original), 'both_match': True})
assert len(context) == 20

prop = read(B/'delivery/integration-proposal.json')
payload = prop['new_artifacts']
allowed = prop['allowed_import_whitelist']
assert len(payload) == len(allowed) == len(set(allowed)) == 25
assert set(allowed) == {x['local_relative_path'] for x in payload}
assert not (set(allowed) & {x['path'] for x in context})
assert len({x['suggested_main_relative_path'] for x in payload}) == 25
assert all(matches(B/x['local_relative_path'], x) for x in payload)
conflicts = [x['suggested_main_relative_path'] for x in payload if (MAIN/x['suggested_main_relative_path']).exists()]
assert not conflicts
inventory = {x['path'] for x in frozen}
assert inventory == set(allowed) | {x['path'] for x in context} | {x['path'] for x in prop['transport_only_exclusions']}

tsv = []
for line in (B/'delivery/current-hashes.tsv').read_text().splitlines():
    if not line or line.startswith('#') or line.startswith('sha256'): continue
    h, n, p = line.split('\t')
    row = {'path': p, 'sha256': h, 'bytes': int(n)}
    assert matches(B/p, row), p
    tsv.append(row)
assert len(tsv) == len({x['path'] for x in tsv})

new_specs = [x for x in payload if x['local_relative_path'].startswith('specs/')]
links, scenarios = [], {}
for row in new_specs:
    p = B/row['local_relative_path']; text = p.read_text()
    ids = re.findall(r'^\| ([DTVSLM]\d{2}) \|', text, re.M)
    assert len(ids) == len(set(ids))
    scenarios[row['local_relative_path']] = ids
    for dest in re.findall(r'\]\(([^)]+)\)', text):
        assert (p.parent/dest).is_file(), (p, dest)
        links.append({'file': row['local_relative_path'], 'target': dest})
assert sum(map(len, scenarios.values())) == 108
assert len(links) == 43
jsons = [x['path'] for x in frozen if x['path'].endswith('.json')]
for p in jsons: read(B/p)
bindings = []
for group in read(B/'delivery/boundary-checks.json')['checks']:
    for d in group['dependencies']:
        assert matches(B/d['path'], d)
        bindings.append({'group': group['id'], 'path': d['path'], 'matches_frozen_copy': True})
live = []
for row in ctx['frozen_inputs']:
    rel = row['logical_path']
    if rel.startswith('specs/') or rel == 'AGENTS.md':
        p = MAIN/rel
        live.append({'path': rel, 'matches_frozen': matches(p,row), 'current': meta(p)})
save('identity-checks.json', {'frozen_files_stable':48,'context':context,'local_TSV_rows':len(tsv),
     'proposal_payload':25,'import_conflicts_at_check':conflicts,'selected_live_dependencies':live,
     'registered_contexts_never_imported':20,'transport_only_excluded':3,
     'note':'Live main metadata is not required to equal the historical whole snapshot. Integrator must recheck targets and dependency applicability later.'})
save('link-json-scenario-checks.json', {'JSON_valid':len(jsons),'links':links,'scenario_IDs':scenarios,
     'scenario_count':108,'boundary_dependency_bindings':bindings,'note':'Counts/links/identities do not prove expected behavior.'})

entries = read(B/'delivery/evidence/source-manifest.json')['entries']
source = {}
for row in entries:
    p = REF/row['path']; assert matches(p,row)
    blob = subprocess.run(['git','--no-optional-locks','-C',str(REF),'show',COMMIT+':'+row['path']], capture_output=True, check=True).stdout
    assert p.read_bytes() == blob
    source[row['path']] = {'path':row['path'],**meta(p),'commit_blob_match':True}
assert len(entries) == 33 and len(source) == 28
save('source-checks.json', {'commit':COMMIT,'delivery_scope_records':33,'distinct_files':28,'entries':list(source.values()),
     'note':'Hash/blob checks are separate from fresh semantic reading recorded in static-review.json. No reference code was executed.'})

# Literal numeric data, not parsed executable Ruby or a gameplay model.
src_dir = REF/'Data/Scripts/017_Minigames'
slot = (src_dir/'003_Minigame_SlotMachine.rb').read_text()
reels = [[int(v) for v in m.split(',')] for m in re.findall(r'\[([0-7](?:,\s*[0-7]){21})\]', slot)]
assert len(reels) == 3
labels = ['樱桃','小磁怪','大舌贝','皮卡丘','可达鸭','红7','蓝7','重玩']
rows = re.findall(r'^\| (\d+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$', (B/'specs/ui/wp69-slot-reels.md').read_text(), re.M)
assert len(rows) == 22
for idx,a,b,c in rows: assert [a,b,c] == [labels[r[int(idx)]] for r in reels]
freq = [[Counter(r)[i] for r in reels] for i in range(8)]
freq_rows = re.findall(r'^\| ([^0-9|][^|]*) \| (\d+) \| (\d+) \| (\d+) \|$', (B/'specs/ui/wp69-slot-reels.md').read_text(), re.M)
assert len(freq_rows) == 8
for row, expected in zip(freq_rows, freq): assert list(map(int,row[1:])) == expected

vf = (src_dir/'004_Minigame_VoltorbFlip.rb').read_text().split('  def update')[0]
vsource = [tuple(map(int,m)) for m in re.findall(r'\[(\d+), (\d+), (\d+), (\d+), (\d+)\]', vf)]
vrows = [tuple(map(int,m)) for m in re.findall(r'^\| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$', (B/'specs/pokemon-rules/wp69-voltorb-layouts.md').read_text(), re.M)]
assert len(vsource) == len(vrows) == 75
for row,expected in zip(vrows,vsource):
    level,idx,bombs,two,three,one,f,g,prize=row
    assert (bombs,two,three,f,g)==expected and bombs+two+three+one==25 and prize==2**two*3**three
assert [sum(x[0]==i for x in vrows) for i in range(1,9)] == [5,10,10,10,10,10,10,10]

mining = (src_dir/'006_Minigame_Mining.rb').read_text()
msource = re.findall(r'\[:([A-Z0-9]+), (\d+), (\d+), (\d+), (\d+), (\d+), \[([01, ]+)\]\]', mining)
annex = (B/'specs/ui/wp70-mining-data.md').read_text()
mrows = re.findall(r'^\| (\d+) \| ([A-Z0-9]+) \| (\d+) \| (\d+)×(\d+) \| (\d+) \| `([#./]+)` \|$', annex,re.M)
assert len(msource)==len(mrows)==61
for row,s in zip(mrows,msource):
    idx,name,wgt,w,h,n,mask=row;sn,swgt,gx,gy,sw,sh,pat=s
    bits=[int(v) for v in pat.split(',')]
    assert (name,wgt,w,h)==(sn,swgt,sw,sh) and int(n)==sum(bits)
    assert mask.replace('/','')==''.join('#' if v else '.' for v in bits)
    assert len(mask.split('/'))==int(h) and all(len(x)==int(w) for x in mask.split('/'))
assert len({x[0] for x in msource})==48 and sum(int(x[1]) for x in msource)==2370
isource=re.findall(r'\[(\d+), (\d+), (\d+), (\d+), \[([01, ]+)\]\]',mining.split('  IRON = [')[1].split('  def update')[0])
irows=re.findall(r'^\| (\d+) \| (\d+)×(\d+) \| (\d+) \| `([#./]+)` \|$',annex,re.M)
assert len(isource)==len(irows)==13
for row,s in zip(irows,isource):
    idx,w,h,n,mask=row;gx,gy,sw,sh,pat=s;bits=[int(v) for v in pat.split(',')]
    assert (w,h)==(sw,sh) and int(n)==sum(bits)
    assert mask.replace('/','')==''.join('#' if v else '.' for v in bits)
items=(REF/'PBS/items.txt').read_text();pockets={}
for name in {x[0] for x in msource}:
    m=re.search(r'^\['+name+r'\]\s*$([\s\S]*?)(?=^\[|\Z)',items,re.M);assert m
    pockets[name]=int(re.search(r'^Pocket\s*=\s*(\d+)',m[1],re.M)[1])
assert {k for k,v in pockets.items() if v==2}=={'REVIVE','MAXREVIVE'}
assert all(v==1 for k,v in pockets.items() if k not in {'REVIVE','MAXREVIVE'})
save('literal-data-checks.json',{'slot_order_rows':22,'slot_frequencies':freq,'voltorb_rows':75,'voltorb_largest_fixed_prize':max(x[-1] for x in vrows),
    'mining_rows':61,'mining_unique_IDs':48,'mining_weight_sum':2370,'iron_rows':13,'PBS_pockets':pockets,
    'result':'All literal ordered rows/dimensions/masks/counts match. No generator, shuffle or runtime data load.'})

fixed = {'lottery_seed_date_2026_09_30':30+32*9+512*2026,
 'card_bulbasaur_unquantized':(9+9+16+16+2*16)*4*14//10,
 'card_all10_unquantized':(400+200)*10*40//10,
 'min_slip_numerators':[144-36,36-9,9-1,1],
 'max_slip_numerators':[36,81-36,121-81,144-121],
 'voltorb_max':2**7*3**3,'mining_pick_limit':49,'mining_hammer_hits_to_reach49':(49+1)//2}
assert fixed['lottery_seed_date_2026_09_30']==1037630 and fixed['card_bulbasaur_unquantized']==459 and fixed['card_all10_unquantized']==24000
assert fixed['min_slip_numerators']==[108,27,8,1] and fixed['max_slip_numerators']==[36,45,40,23]
save('constant-checks.json',{'examples':fixed,'method':'Independent fixed arithmetic only, no reference function execution or behavioral model.'})
head=subprocess.run(['git','--no-optional-locks','-C',str(REF),'rev-parse','HEAD'],capture_output=True,text=True,check=True).stdout.strip()
status=subprocess.run(['git','--no-optional-locks','-C',str(REF),'status','--porcelain'],capture_output=True,text=True,check=True).stdout
assert head==COMMIT and not status
save('reference-checks.json',{'HEAD':head,'ordinary_git_status':status})
print(json.dumps({'inputs':48,'contexts':20,'payload':25,'source_records':33,'distinct_sources':28,'scenarios':108,
 'links':43,'JSON':len(jsons),'TSV':len(tsv),'ordered_tables':[22,75,61,13],
 'dependency_drift':[x['path'] for x in live if not x['matches_frozen']],'target_conflicts':conflicts,'reference_clean':True},ensure_ascii=False,indent=2))
