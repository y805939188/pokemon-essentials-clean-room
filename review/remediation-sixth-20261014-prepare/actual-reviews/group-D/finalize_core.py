import datetime, hashlib, json, pathlib, subprocess
OUT=pathlib.Path(__file__).resolve().parent
PREFIX='review/remediation-sixth-20261014-prepare/actual-reviews/group-D/'
ACTUAL='86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
for u in ['u10','u11','u12']:
    assert (OUT/'peers'/u/'final-increment'/'report.md').is_file()
    p=OUT/'peers'/u/'final-increment'/('peer-review.json' if u=='u10' else 'report.json')
    assert p.is_file()
for p in OUT.rglob('*.json'):json.loads(p.read_bytes())
for p in OUT.rglob('*.jsonl'):
    for line in p.read_text().splitlines():json.loads(line)
status=subprocess.check_output(['git','status','--porcelain','--untracked-files=all']).decode().splitlines()
assert all(line[3:].startswith(PREFIX) for line in status),status
assert subprocess.run(['git','diff','--quiet',ACTUAL,'--','deliverables/final-specification-set','planning','audit',
                        'review/remediation-sixth-20261014-prepare/candidates',
                        'review/remediation-sixth-20261014-prepare/reviews']).returncode==0
assert subprocess.check_output(['git','rev-parse','HEAD']).decode().strip()==ACTUAL
paths=sorted(p for p in OUT.rglob('*') if p.is_file() and 'publication' not in p.relative_to(OUT).parts and p.name!='manifest.json')
records=[]
for p in paths:
    d=p.read_bytes()
    records.append({'path':PREFIX+str(p.relative_to(OUT)),'mode':'100644','bytes':len(d),
                    'sha256':hashlib.sha256(d).hexdigest(),
                    'git_blob':hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest()})
manifest={'schema':'r6.actual.group-d.core-manifest.v1','recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'reviewed_final_commit':ACTUAL,'workspace_tree':'67e8c55d520fa8cad2928cb4b95e24c3ed602d5a',
          'formal_tree':'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c','scope':'D9 plus explicit F002 receiver interface',
          'files':records,'file_count_excluding_manifest':len(records),'bytes_excluding_manifest':sum(f['bytes'] for f in records),
          'manifest_self_excluded':True,'publication_tail_excluded':True,
          'qualification':'Core commit externally binds this manifest and all payloads; no future self SHA fabricated.'}
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'core_files_with_manifest':len(records)+1,'bytes_without_manifest':manifest['bytes_excluding_manifest'],
                  'scope_only':True,'json_valid':True,'protected_bytes_unchanged':True}))
