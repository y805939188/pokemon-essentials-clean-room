"""Validate/manifest review artifacts only; no source or behavior execution."""
import gzip
import hashlib
import json
import pathlib
import subprocess
from read_range import ROOT, OUT, verify

verify()
review = ROOT/'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae'

def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()

receipts=[]
json_count=0
for p in sorted(OUT.rglob('*.json')):
    if p.name in {'launcher-status.json'}:continue
    d=json.loads(p.read_text());json_count+=1
    if isinstance(d,dict) and d.get('artifact_encoding')=='gzip_json':
        q=p.parent/d['artifact']
        assert q.resolve().is_relative_to(OUT)
        assert q.stat().st_size==d['compressed_bytes']
        assert digest(q)==d['compressed_sha256']
        h=hashlib.sha256();n=0
        with gzip.open(q,'rb') as stream:
            for block in iter(lambda:stream.read(1024*1024),b''):
                n+=len(block)
                assert n<=d['uncompressed_bytes']
                h.update(block)
        assert n==d['uncompressed_bytes'] and h.hexdigest()==d['uncompressed_sha256']
        receipts.append(dict(receipt=str(p.relative_to(OUT)),artifact=str(q.relative_to(OUT)),
            compressed_bytes=q.stat().st_size,uncompressed_bytes=n,verified=True,
            validation_extent='gzip CRC, all bytes, declared lengths and SHA256; semantic approval not inferred'))

input_checks=[]
for record in json.loads((OUT/'inventory.json').read_text())['files']:
    p=ROOT/'reference/pokemon-essentials'/record['path']
    assert digest(p)==record['sha256']
    input_checks.append(record['path'])
formal=json.loads((review/'inventory/formal131.json').read_text())
for record in formal:
    assert digest(ROOT/record['path'])==record['sha256'],record['path']
assert len(input_checks)==104 and len(formal)==131

def artifact(path, coverage, semantics):
    p=OUT/path
    return dict(path=path,bytes=p.stat().st_size,sha256=digest(p),coverage=coverage,
                semantics=semantics,exact_locations='within the artifact, not inferred from filename')

forward=[
 artifact('source-to-spec-matrix.jsonl','29 PBS;28278 source record/field units','15 manual static rules; predicates not automatic PASS'),
 artifact('pbs-bulk/source-to-spec-matrix.json','44 PBS;16732 full-record maps;104 actual field rules','116 manually read rules including omissions; compressed array receipt'),
 artifact('pbs-bulk/field-semantic-rules.json','116 author-field rules;9 header rules separate','data acceptance/default/inheritance/consumer handoffs; not full downstream algorithms'),
 artifact('localization/source-to-formal.json','18 texts;10697 record units','all bodies read this round; binary equality separate'),
 artifact('fonts/source-unit-matrix.json','8 fonts;104 tables;2326glyphs;128pixels','all structure and conditional consumers; native rendering UNKNOWN'),
 artifact('fonts/traceability.json','8 font and2 BMP behavior/resource links','font default/tag and BMP consumer clauses; no installed font assertion'),
 artifact('config-forward-matrix.json','33 active/commented configuration property positions','9 active top-level declarations; native effects UNKNOWN')]
reverse=[
 artifact('spec-to-source-matrix.json','334 special-PBS clause/rule rows','owned data portions only'),
 artifact('pbs-bulk/spec-to-source-matrix.json','all bulk field-rule and existing-vector formal joins','compressed receipt; proposals separated'),
 artifact('localization/formal-to-source.json','68 clause/vector rows','current source reading, not historical execution signoff'),
 artifact('fonts/traceability.json','font/BMP clause and vector relations','conditional selection/structure boundaries'),
 artifact('config-reverse-matrix.json','70 configuration boundary joins','literal declarations and preserved host scope'),
 artifact('data-contract-counter/clause-to-source-counter-matrix.json','33 clause units','independent author-data counter review'),
 artifact('data-contract-counter/vector-to-source-counter-matrix.json','135 indexed IDs;120 in scope;77 added data vectors reviewed','15 named other-domain vectors read/classified without approval')]
(OUT/'forward-matrix-index.json').write_text(json.dumps(forward,ensure_ascii=False,indent=2)+'\n')
(OUT/'reverse-matrix-index.json').write_text(json.dumps(reverse,ensure_ascii=False,indent=2)+'\n')

ledgers=[]
with (OUT/'combined-reading-ledger.jsonl').open('w') as output:
    for p in [OUT/'reading-ledger.jsonl',OUT/'fonts/reading-ledger.jsonl',
              OUT/'localization/reading-ledger.jsonl',OUT/'localization/pokedex/reading-ledger.jsonl',
              OUT/'pbs-bulk/reading-ledger.jsonl',OUT/'data-contract-counter/reading-ledger.jsonl']:
        assert p.exists(),p
        count=0
        for line in p.read_text().splitlines():
            row=json.loads(line)
            output.write(json.dumps(dict(origin_ledger=str(p.relative_to(OUT)),original_entry=row),ensure_ascii=False)+'\n')
            count+=1
        ledgers.append(dict(path=str(p.relative_to(OUT)),rows=count,sha256=digest(p),
            interpretation='Original distinctions preserved; no status promotion by this merge.'))

proposals=json.loads((OUT/'findings.json').read_text())
counters=json.loads((OUT/'counter-review.json').read_text())
covered={r['proposal'] for r in counters['reviews']}
assert all(p['id'] in covered for p in proposals['proposals'])
assert all(p['id'] in covered for p in proposals['non_new_defect_candidates'])

main_diff=subprocess.check_output(['git','--no-optional-locks','-C',str(ROOT),'diff','--name-only',
    '8ea169fbd0f33f378b5d732fd6bea59e854e04a6','--','reference','deliverables','specs','planning','audit'],text=True)
ref_diff=subprocess.check_output(['git','--no-optional-locks','-C',str(ROOT/'reference/pokemon-essentials'),
    'diff','--name-only','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'],text=True)
assert not main_diff and not ref_diff
validation=dict(status='PASS_TOOL_VALIDATION_ONLY',source_execution=0,behavior_model_execution=0,host_demo_execution=0,
    own_json_artifacts_parsed=json_count,scoped_reference_hashes_checked=len(input_checks),formal_hashes_checked=len(formal),
    compressed_receipts=receipts,reading_ledgers=ledgers,proposal_count=len(proposals['proposals']),
    independently_countered_candidates=len(counters['reviews']),protected_tracked_diffs_empty=True,
    scope='Artifact integrity and protected byte identities. Not a semantic or runtime PASS.',
    actual_model_effort_tier_speed_UUID='UNVERIFIED')
(OUT/'final-artifact-validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(json_artifacts=json_count,reference_inputs=104,formal_inputs=131,
    gzip_receipts=len(receipts),ledger_rows=sum(x['rows'] for x in ledgers),
    proposals=len(proposals['proposals']),counters=len(counters['reviews']),status=validation['status'])))
