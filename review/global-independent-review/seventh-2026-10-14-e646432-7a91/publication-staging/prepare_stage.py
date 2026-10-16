import datetime,hashlib,json,subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1];P=R.parents[2]
def get(*args):return subprocess.check_output(['git','-C',str(P),*args]).decode().strip()
index=json.loads((R/'publication-transport/core/payload-index.json').read_bytes());a=json.loads((R/'evidence/final-root-reception.json').read_bytes());by={v['logical_path']:v for v in index['logical_files']}
assert all(by[p]['sha256']==h for p,h in a['accepted_payload_sha256'].items())
assert get('rev-parse','HEAD')=='e646432c644dec04d306842cc5a559a29c718fbc'
assert not get('diff','--name-only') and not get('diff','--cached','--name-only')
for name,prefix in [('source','reference/pokemon-essentials/'),('formal','')]:
 for row in json.loads((R/('inventory/'+name+'.final.json')).read_bytes()):
  assert hashlib.sha256((P/(prefix+row['path'])).read_bytes()).hexdigest()==row['sha256']
selected=['README.md','final-report.md','summary.md','findings.json','canonical-records.json','batch-plan.final.json','dependency-graph.json','file-conflict-graph.json','progress.final.json','progress.md','reading-ledger.final.json','coverage/summary.final.json','coverage/module-primary-map.json','coverage/current-interface-reception.json','inventory/source.final.json','inventory/formal.final.json','inventory/supplements.final.json','inventory/reference-working-extras.json','startup/fixed-inputs.json','startup/readiness.md','history/qualifications.final.json','history/inherited-nonmandatory.final.json','history/recovery-identity-verification.json','evidence/final-root-reception.json','tasks/R7-C17/final-report.md','tasks/R7-C17/coverage-summary.json','tasks/R7-C17/final-unreceived-ids.json','tasks/R7-C17/validation.json','tasks/R7-C18/report.md','tasks/R7-C19/final-adjudication-integrity.json','tasks/R7-C20/report.md','execution/phase-summary.final.json']
selected += [str(p.relative_to(R)) for p in (R/'publication-tools').glob('*.py')]
selected += [str(p.relative_to(R)) for p in (R/'publication-transport/core').rglob('*') if p.is_file()]
paths=sorted({str((R/p).relative_to(P)) for p in selected})
bad=[p for p in paths if not (P/p).is_file() or (P/p).stat().st_size>=104857600]
if bad:raise ValueError('Actual stage members invalid: '+repr(bad))
out=R/'publication-staging/core-stage-paths.nul'
with out.open('xb') as f:f.write(b'\0'.join(p.encode() for p in paths)+b'\0')
summary={'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'paths':len(paths),'physical_bytes':sum((P/p).stat().st_size for p in paths),'max_member_bytes':max((P/p).stat().st_size for p in paths),'logical_files':len(index['logical_files']),'accepted_payload_hash_matches':len(a['accepted_payload_sha256']),'path_file':str(out),'source_formal_working_hashes_match':True,'scope':'Exact new R7 allowlist only; original diff/staged empty before add.'}
(R/'publication-staging/pre-stage-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary))
