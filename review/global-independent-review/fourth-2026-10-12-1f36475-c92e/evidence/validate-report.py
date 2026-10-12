import pathlib,json,hashlib,collections,re,datetime,sys
r=pathlib.Path(__file__).resolve().parent.parent
errors=[]
def ck(v,msg):
 if not v:errors.append(msg)
files=[p for p in r.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc']
for p in files:
 if p.suffix=='.json':
  try:json.loads(p.read_text())
  except Exception as e:errors.append(str(p.relative_to(r))+': '+str(e))
f=json.loads((r/'findings.json').read_text());fs=f['findings'];schema=json.loads((r/'findings.schema.json').read_text());required=schema['properties']['findings']['items']['required'];props=schema['properties']['findings']['items']['properties']
ck(f['status']=='FINAL_ADJUDICATED','findings not final');ck(len(fs)==17,'17 canonical');ck(len({x['id'] for x in fs})==17,'unique canonical IDs')
formal={x['path'] for x in json.loads((r/'evidence/formal-identity-check.json').read_text())};src={x['path'] for x in json.loads((r/'evidence/reference-inventory.json').read_text())};caps=json.loads((r/'source-to-spec-coverage.json').read_text())['capability_scope_records'];capids={x['capability_id'] for x in caps}
for x in fs:
 ck(all(k in x for k in required),x['id']+' fields');ck(x['category'] in props['category']['enum'],x['id']+' category');ck(x['disposition'] in props['disposition']['enum'],x['id']+' disposition');ck(x['severity'] in props['severity']['enum'],x['id']+' severity');ck(all(e in props['evidence_level']['items']['enum'] for e in x['evidence_level']),x['id']+' evidence enum');ck(x['status']=='CONFIRMED',x['id']+' unconfirmed');ck(x['review_resolution']['independent_counterreview']['decision'] in ['CONFIRM','CONFIRM_WITH_REFINEMENT'],x['id']+' independent challenge missing')
 for a in x['source_anchors']:ck(a['path'] in src,x['id']+' source path '+a['path'])
 for a in x['spec_anchors']:ck(a['path'] in formal,x['id']+' formal path '+a['path'])
 for p in x['affected_files']:ck(p in formal,x['id']+' affected nonformal '+p)
 for cid in x['related_capabilities']:ck(cid in capids,x['id']+' cap '+cid)
ck(collections.Counter(x['severity'] for x in fs)=={'P2':11,'P3':6},'severity counts')
s=json.loads((r/'spec-to-source-coverage.json').read_text())['files'];ck(len(s)==131 and {x['path'] for x in s}==formal,'all131 exact ownership');ck(all(x['status']!='not_reviewed' and x['contracts_and_evidence'] for x in s),'some file no scoped semantic record')
ck(len(caps)==300 and len(capids)==300,'scope records count/IDs')
g=json.loads((r/'regression-third-23.json').read_text());ck(len(g['records'])==23 and all(x['actual_semantic_reviews'] for x in g['records']),'23 regression mapping')
l=json.loads((r/'regression-legacy-scope.json').read_text());ck(len(l['original229'])==229 and len(l['exact341'])==341,'229/341 mappings')
ck(all(x['fourth_review_status']=='historical_qualified_evidence_reused' for x in l['exact341']),'341 improper full reapproval')
j=json.loads((r/'junction-review.json').read_text());ck(len(j['records'])==14 and len(j['historical_navigation_and_projections']['records'])==80,'14/80 junction mapping')
plan=json.loads((r/'proposed-update-batches.json').read_text());owners=json.loads((r/'shared-file-owners.json').read_text());assigned=[i for b in plan['author_batches'] for i in b['finding_ids']];ck(sorted(assigned)==sorted(x['id'] for x in fs),'unique required batch coverage');allpaths=[p for b in plan['author_batches'] for p in b['allowed_formal_write_paths']];ck(len(allpaths)==len(set(allpaths)),'cross-batch write collision');ck(set(allpaths)=={p for x in fs for p in x['affected_files']},'allowed path union')
for task in ['CA','CB','J']:
 inp=json.loads((r/'tasks'/(task+'-input-identities.json')).read_text())
 for x in inp['files']+inp.get('supplemental_files',[]):
  b=(r/x['path']).read_bytes();ck(len(b)==x['bytes'] and hashlib.sha256(b).hexdigest()==x['sha256'],task+' changed input '+x['path'])
for task in [f'M{i:02d}' for i in range(1,13)]+['CA','CB','J']:
 d=json.loads((r/'tasks'/(task+'-launch.json')).read_text());ck(d['status']=='PROCESS_COMPLETED' and d['exit_code']==0,task+' incomplete');ck(d['requested']=={'model':'gpt-6-astra','reasoning_effort':'ultra','service_tier':'default','fast':False},task+' request mismatch')
ck(not any(p.is_symlink() for p in r.rglob('*')),'symlink in report')
expected=['README.md','baseline.json','readiness.md','progress.json','progress.md','source-to-spec-coverage.json','spec-to-source-coverage.json','coverage-summary.md','findings.json','findings-summary.md','regression-third-23.json','regression-legacy-scope.json','junction-review.md','junction-review.json','execution-evidence.json','limits-and-missing-materials.md','proposed-update-batches.json','shared-file-owners.json','final-report.md']
ck(all((r/p).is_file() for p in expected),'required semantic artifact missing')
# Required report navigation; standalone terminal echo links intentionally resolved against workspace root.
for name in ['README.md','findings-summary.md','coverage-summary.md','junction-review.md','final-report.md']:
 for match in re.finditer(r'\]\(([^)]+)\)',(r/name).read_text()):
  target=match.group(1).split('#')[0].strip('<>')
  if not target or '://' in target or target.startswith('/'):continue
  ck((r/target).exists(),name+' bad link '+target)
result={'schema_version':'1.0','evidence_level':'TOOL_VALIDATION','status':'PASS' if not errors else 'FAIL','time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':['python3','evidence/validate-report.py'],'python':sys.version,'inputs':'All current round artifacts, fixed formal/source inventories; frozen independent input identities','outputs':'evidence/report-validation.json','exit_code':0 if not errors else 1,'checks_scope':'JSON/schema-required fields/enums/counts/unique IDs/source and formal paths/frozen-input bytes/ownership/dependencies/required navigation; NOT semantic or game execution','counts':{'json_files':sum(p.suffix=='.json' for p in files),'findings':17,'formal_files':131,'scope_records':300,'GR3':23,'legacy_findings':229,'legacy_contributions':341,'junctions':14,'historical_junctions_and_chains':80,'required_batches':5,'allowed_write_paths':len(allpaths)},'errors':errors,'excluded_from_publication':['**/__pycache__/**','**/*.pyc','/tmp/gr4-c92e-cli raw event logs'],'side_effects':'Only this validation receipt in new review directory'}
(r/'evidence/report-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False));sys.exit(result['exit_code'])
