"""Structural corroboration only; no code from the reference project is run."""
import json, hashlib, subprocess, pathlib, datetime
from recover import T, ident, save

sha = lambda b: hashlib.sha256(b).hexdigest()
state = json.loads((T/'view-state.json').read_text())
assert not state['pending']
checks = []
for a in state['acks']:
    assert set(a['shown']) == set(range(len(a['parts'])))
    shown = ''.join((T/p).read_text() for p in a['parts']).encode()
    assert sha(shown) == a['display_sha256'], a['anchor']
    obj = json.loads((T/'.work/originals'/str(a['file'])).read_text())
    for token in a['pointer'].split('/')[1:] if a['pointer'] else []:
        token = token.replace('~1','/').replace('~0','~')
        obj = obj[int(token)] if isinstance(obj,list) else obj[token]
    canon = json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
    assert sha(canon) == a['original_sha256']
    checks.append({'anchor':a['anchor'],'original_and_display_digest':True,
                   'all_parts_shown':True,'semantic_credit':'No automated credit'})

ds = json.loads((T/'source-displays.json').read_text())
# These original larger displays were truncated; replacement displays were read.
bad = []
for i,d in enumerate(ds):
    if (d['path'].endswith('wp41-switching-positioning-and-escape.md') and d['range']==[100,220]) or (d['path'].endswith('pokemon-rules-wp53-60-61-62-69-70.md') and d['range']==[75,108]):
        bad.append(i)
    if d['path'].endswith('wp42-growth-end-of-round-and-battle-outcomes.md') and d['range']==[100,144]:
        if any(e['path']==d['path'] and e['range']==d['range'] for e in ds[i+1:]):
            bad.append(i)
cache = {}
for i,d in enumerate(ds):
    key=(d['repo'],d['path'])
    if key not in cache:
        repo='/workspace/pokemon-essentials' if d['repo']=='R' else '/workspace/pokemon-essentials-clean-room'
        cache[key]=subprocess.check_output(['git','-C',repo,'show',d['commit']+':'+d['path']])
    b=cache[key]
    assert ident(b)==d['identity']
    lines=b.decode().splitlines();s,e=d['range']
    shown='\n'.join(f'{n+1:5}: {lines[n]}' for n in range(s-1,e)).encode()
    assert ident(shown)==d['display']
    d['receipt_index']=i
    d['actual_read_disposition']='TRUNCATED_ORIGINAL_NO_CREDIT_USE_REPAIRS' if i in bad else 'ACTUALLY_DISPLAYED_AND_READ_FOR_STATED_SCOPE'
    d['semantic_credit']='Only per-record human judgments; displaying a neighboring partial method does not claim that definition complete.'
save(T/'source-reading-ack.json',ds)

obligations=json.loads((T/'initial-read-obligations.json').read_text())
missing=[]
for path,ranges in obligations.items():
    have={n for i,d in enumerate(ds) if d['path']==path and i not in bad
          for n in range(d['range'][0],d['range'][1]+1)}
    need={n for s,e in ranges for n in range(s,e+1)}-have
    if need:missing.append({'path':path,'lines':sorted(need)})
assert not missing, missing
save(T/'remaining-display-inventory.json',{'missing_initial_line_anchors':missing,
   'qualification':'Mechanical union only, no source approval. Old byte readsets retained as literal history, not current whole-file reading. Complete methods and necessary consumers judged in reception-ledger.json.'})

ledger=json.loads((T/'reception-ledger.json').read_text())
expected=[s['id'] for s in json.loads((T.parent.parent/'continuation-v2/A.complete.json').read_text())['semantic_objects']]
assert [r['id'] for r in ledger['records']]==expected and len(expected)==12
assert sum(len(r['seven_groups']) for r in ledger['records'])==84
assert all(not r['own_unread'] and not r['new_required_proposal'] for r in ledger['records'])
assert sum(r['original_current_values_preserved']['classification']=='required' for r in ledger['records'])==8
assert sum(r['original_current_values_preserved']['classification']=='optional' for r in ledger['records'])==4
parsed=[]
for p in T.rglob('*.json'):
    if '.work' in p.parts or '__pycache__' in p.parts:continue
    json.loads(p.read_text());parsed.append(str(p.relative_to(T)))
save(T/'validation.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
  'result':'PASS_STRUCTURAL_CORROBORATION_ONLY','scope':'A only',
  'canonical_records':12,'canonical_groups':84,'original_P02_records_separate':12,
  'old_required_covered_current':8,'optional_not_adopted':4,'new_required':0,
  'exact_display_checks':checks,'fixed_source_and_B8_display_checks':len(ds),
  'truncated_original_display_indices_not_credited':bad,
  'initial_line_anchor_union_missing':missing,'json_parsed':parsed,
  'behavior':'NOT_EXECUTED','human_judgment':'reception-ledger.json; no test or checksum creates semantic PASS'})
print('PASS:',len(checks),'exact display receipts;',len(ds),'fixed source/spec displays;12 records/84 groups; no missing initial line anchors; behavior NOT_EXECUTED.')
