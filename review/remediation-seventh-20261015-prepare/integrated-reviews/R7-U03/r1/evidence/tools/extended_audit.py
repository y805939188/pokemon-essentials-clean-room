exec(compile(open('/workspace/r7-ir-R7-U03-final/bootstrap/mechanical_audit.py').read(), 'mechanical_audit.py', 'exec'))
out2={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tool_pid':os.getpid(),'scope':'TOOL_VALIDATION','candidate_manifests':[],'candidate_diff_checks':[]}
for commit,prefix,local,mfield in [('11bff8e7912a98de09691ad7d7b7a2d3194e2757','candidates/R7-U03/',root/'actual-input/candidate','evidence_and_mirror_inventory'),('a8a65bc4f29e2b19c8b63fd59c9c2a0941be6520','candidates/R7-U03/evidence/reviewer/r2/',root/'actual-input/candidate-review','files')]:
 manifest_path=prefix+('evidence/author/' if mfield.startswith('evidence_') else '')+'artifact-manifest.json';d=json.loads((local/manifest_path).read_text());rows=d[mfield]
 for r in rows:
  b=(local/r['path']).read_bytes();a=check(b,r);assert a['git_blob']==r.get('git_blob',r.get('git_blob_content_id'))
 changes=git('diff','--name-status',B,commit).decode().splitlines();assert len(changes)==84 and all(x.startswith('A\t'+prefix) for x in changes)
 out2['candidate_manifests'].append(dict(commit=commit,manifest=manifest_path,nonself_entries=len(rows),complete_diff_files=len(changes),bytes=sum(len((local/x.split('\t')[1]).read_bytes()) for x in changes)))
assert out2['candidate_manifests'][0]['nonself_entries']==83 and out2['candidate_manifests'][1]['nonself_entries']==83
for f in j['cumulative_files']:
 p=f['path'];bl=(git('show',B+':'+p).decode().splitlines(keepends=True) if git('ls-tree',B,'--',p) else [])
 for batch in sorted(set(h['batch_id'] for h in f['hunks'])):
  hs=[h for h in f['hunks'] if h['batch_id']==batch];h=hs[0];cl=git('show',h['candidate_commit']+':'+h['candidate_path']).decode().splitlines(keepends=True)
  expected=[(h['kind'],*h['base_line_indices_half_open'],*h['candidate_line_indices_half_open']) for h in hs]
  actual=[(tag,a,z,ca,cz) for tag,a,z,ca,cz in difflib.SequenceMatcher(None,bl,cl,autojunk=False).get_opcodes() if tag!='equal']
  assert expected==actual,(p,batch,'independent full candidate diff differs',expected,actual)
  out2['candidate_diff_checks'].append(dict(path=p,batch=batch,opcodes=actual,complete_candidate_diff_matches_journal=True))
out2['peer_shared_preservation_checks']=json.loads((root/'actual-plans/R7-U03.json').read_text())['shared_preservation_checks']
previous=j['previous_actual_MI'];new_changed=git('diff','--name-only',previous,MI,'--','deliverables/final-specification-set').decode().splitlines()
assert sorted(new_changed)==sorted(j['new_candidate_targets'])
out2['previous_actual_formal_preservation']=dict(previous_actual_MI=previous,changed_paths=new_changed,unchanged_formal_paths=126,qualification='Every formal file outside these five targets is byte-identical to previous MI; the two shared targets are independently assembled preserving prior clauses. Does not reapprove other IDs.')
# Check the root's complete r2 reception file table against immutable Git bytes.
r=json.loads((root/'actual-input/root-reception/reception.json').read_text());out2['root_reception']=dict(parent_receipt=r['parent_receipt'],counts=r['counts'],file_table_entries=len(r['files']))
# Every member of the restoration plan has already been compared against this commit.
assert r['parent_receipt']['result_commit']=='a8a65bc4f29e2b19c8b63fd59c9c2a0941be6520' and r['counts']==dict(files=84,bytes=706129)
logs=[json.loads(x) for x in (root/'audit/read-log.jsonl').read_text().splitlines()]
mandatory=['AGENTS.md','audit/source-traceability.md','planning/feature-matrix.md']+['deliverables/final-specification-set/'+p for p in ['engine-overworld/wp12-terrain-movement-vehicles.md','engine-overworld/wp16-world-rendering-and-visual-transitions.md','generic-kernel/wp06-time-random-steps-stats.md','pokemon-rules/wp34-inheritance-and-offspring.md','pokemon-rules/wp61-field-passive-effects-and-blackout.md','test-catalog/engine-overworld-wp11-15-59-60.md','test-catalog/engine-overworld-wp16.md','test-catalog/pokemon-rules-wp19-21-22-23-34.md','test-catalog/pokemon-rules-wp53-60-61-62-69-70.md']]
coverage=[]
for p in mandatory:
 b=(root/'actual-input/actual'/p).read_bytes();n=len(b.decode().splitlines());covered=set();records=[]
 for x in logs:
  if (root/x['path']).resolve()==(root/'actual-input/actual'/p).resolve():
   records.append(x)
   if x['mode']=='full':covered.update(range(1,n+1))
   elif x['mode']=='lines':covered.update(range(x['lines'][0],x['lines'][1]+1))
 assert set(range(1,n+1))<=covered,(p,'missing printed reads')
 coverage.append(dict(path=p,total_lines=n,**ident(b),recorded_reads=records,qualification='Read output coverage plus semantic evaluation. Full mode may have been display-truncated; all known missing display ranges were separately re-read. This is not an automated semantic verdict.'))
out2['mandatory_full_read_coverage']=coverage
# Bind all named reference snapshots to the frozen R inventory; unread complements stay explicit.
inv={r['path']:r for r in json.loads((root/'supplement/original-bound/inventory/source.json').read_text())};sources=[]
for base in [root/'original/inputs/reference',root/'supplement/reference']:
 for p in base.rglob('*.rb'):
  rel=str(p.relative_to(base));b=p.read_bytes();check(b,inv[rel]);ranges=[x.get('lines','FULL') for x in logs if (root/x['path']).resolve()==p.resolve()]
  sources.append(dict(path=rel,commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',**ident(b),read_ranges=ranges,qualification='Selected snapshot only. Remainder of this file outside listed ranges has identity credit only; no complete R-tree or runtime certification.'))
out2['reference_identity_and_read_scope']=sources
(root/'audit/extended-audit.json').write_text(json.dumps(out2,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifests':out2['candidate_manifests'],'independent_candidate_diffs':len(out2['candidate_diff_checks']),'mandatory_full_reads':len(coverage),'reference_files':len(sources)},ensure_ascii=False,indent=2))
