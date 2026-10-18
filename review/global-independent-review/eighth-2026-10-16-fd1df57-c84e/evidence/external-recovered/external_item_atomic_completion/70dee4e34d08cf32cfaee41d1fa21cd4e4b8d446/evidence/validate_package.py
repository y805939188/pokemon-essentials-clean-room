"""Static consistency of authored review evidence; never gameplay tests."""
from pathlib import Path
import collections,datetime,gzip,hashlib,json,subprocess
OUT=Path(__file__).resolve().parent.parent
ROOT=Path('/workspace/pokemon-essentials-clean-room')
CONTRACT='40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232'
def git(*args,cwd=ROOT,input=None):
    return subprocess.check_output(['git','-C',str(cwd),*args],input=input).decode().strip()
def read(name):return json.loads((OUT/name).read_text())
for path in OUT.rglob('*.py'):compile(path.read_text(),str(path),'exec')
parsed=[]
for p in sorted(OUT.rglob('*.json')):
    json.loads(p.read_text());parsed.append(str(p.relative_to(OUT)))
for p in OUT.rglob('*.ndjson'):
    for l in p.read_text().splitlines():json.loads(l)
required=['review.md','progress.json','identities.json','reading-ledger.json','forward-mapping.json','reverse-mapping.json','interfaces.json','proposals.json','validation.json','next-dispatch.json']
assert all((OUT/p).is_file() for p in required)
binding=read('evidence/decoded-payload-binding.json')
packed=(OUT/binding['path']).read_bytes();raw=gzip.decompress(packed);a=json.loads(raw)
assert len(raw)==binding['decoded_bytes'] and hashlib.sha256(raw).hexdigest()==binding['decoded_sha256']
assert len(packed)==binding['compressed_bytes'] and hashlib.sha256(packed).hexdigest()==binding['compressed_sha256']
assert git('hash-object','--stdin',input=raw)==binding['decoded_git_blob']
atoms={x['id']:x for x in a['assertions']};groups={x['id']:x for x in a['groups']};units=a['handler_units']
assert len(atoms)==len(a['assertions'])==698
assert len(groups)==len(a['groups'])==247
assert len(units)==196 and len({(u['family'],u['item']) for u in units})==196
assert collections.Counter(u['operation'] for u in units)==dict(add=165,copy=31)
assert len({u['item'] for u in units})==180
for g in groups.values():
    assert all(x in atoms for x in g['assertions'])
    assert g['ordinary_control'] and g['minimal_branch_or_boundary'] and g['failure_prefix']
for u in units:
    assert all(x in atoms for x in u['atom_ids'])
    assert all(x in groups for x in u['shared_semantic_groups']+u['mandatory_common_groups'])
    assert u['actual_callers']
    if u['operation']=='copy':assert all(x in atoms for x in u['resolved_atom_ids'])
for x in atoms.values():
    assert x['meaning'] and x['source']['ranges'] and x['operative'] and x['execution']=='NOT_EXECUTED'
    for op in x['operative']:
        assert (ROOT/op['path']).read_text().splitlines()[op['line']-1]==op['text']
rr=read('reverse-mapping.json')['rows'];f=read('evidence/finite-body-reception.json')
fr={x['id'] for x in f['receipts']}
for r in rr:
    assert (ROOT/r['path']).read_text().splitlines()[r['line']-1]==r['full_current_clause']
    assert all(x in atoms for x in r['manual_supporting_atoms'])
    assert all(x in groups for x in r['required_group_support'])
    if 'finite_complete_receipt' in r:assert r['finite_complete_receipt']['id'] in fr
    if r['meaning_class']=='OPERATIVE_BODY':assert r['manual_supporting_atoms'] or r['required_group_support']
assert len(f['receipts'])==10
for i in read('identities.json')['payloads']:
    repo=Path(i['repo']);b=(repo/i['path']).read_bytes()
    assert len(b)==i['bytes'] and hashlib.sha256(b).hexdigest()==i['sha256']
    assert git('hash-object','--stdin',cwd=repo,input=b)==i['blob']
    assert git('rev-parse',i['commit']+':'+i['path'],cwd=repo)==i['blob']
assert git('rev-parse','HEAD')==CONTRACT or git('merge-base','HEAD',CONTRACT)==CONTRACT
assert git('status','--porcelain',cwd=Path('/workspace/pokemon-essentials'))==''
assert git('rev-parse','HEAD',cwd=Path('/workspace/pokemon-essentials'))=='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
prefix=str(OUT.relative_to(ROOT))+'/'
changed=git('diff',CONTRACT,'--name-only').splitlines()
untracked=git('ls-files','--others','--exclude-standard').splitlines()
assert all(p.startswith(prefix) for p in changed+untracked)
assert git('diff',CONTRACT,'--','deliverables/final-specification-set')==''
assert read('proposals.json')['new_proposal_count']==0
assert read('interfaces.json')['finite_necessary_gameplay_joins_unreceived']==0
result=dict(schema='gr8-item-local-static-check/v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    checks='PASS',scope='Authored evidence consistency, fixed input bytes, precise operative text, bindings, finite receipts and write boundary only',
    required_core_files=len(required),parsed_JSON_files=len(parsed),assertions=len(atoms),groups=len(groups),handler_pairs=len(units),reverse_rows=len(rr),
    identities_checked=len(read('identities.json')['payloads']),finite_direct_receipts=len(fr),
    source_execution='NOT_EXECUTED',behavior_tests='NOT_EXECUTED',root_reception='PENDING',remediation='UPDATE_NOT_STARTED')
(OUT/'evidence/local-static-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
