"""Independent document preservation audit. No behavior interpreter/model is run."""
import pathlib,json,subprocess,difflib,re,collections,hashlib
HERE=pathlib.Path(__file__).resolve().parents[1]
CAN=pathlib.Path('/workspace/r7-review-input/R7-U03-r1-11bff8e7912a98de09691ad7d7b7a2d3194e2757/candidate/candidates/R7-U03')
B='e646432c644dec04d306842cc5a559a29c718fbc'
rows=json.load(open('/workspace/r7-review-bootstrap/R7-U03-r1/candidate-input.json'))['candidate_and_author_evidence_file_identities']
allowed={
'engine-overworld/wp12-terrain-movement-vehicles.md':[(97,98,97,98),(101,102,101,103),(103,104,104,105),(107,107,108,110),(228,229,231,233),(237,238,241,242)],
'pokemon-rules/wp61-field-passive-effects-and-blackout.md':[(14,15,14,15),(32,32,32,36),(187,188,191,192)],
'test-catalog/engine-overworld-wp11-15-59-60.md':[(40,42,40,42),(117,117,117,134)],
'test-catalog/engine-overworld-wp16.md':[(8,9,8,9),(25,25,25,38)],
'test-catalog/pokemon-rules-wp53-60-61-62-69-70.md':[(115,115,115,132)]}
result=[];old_kept=0
for r in rows:
 if r['role']!='candidate_mirror':continue
 p=r['formal_target'];base=subprocess.check_output(['git','show',B+':'+p]);d=(CAN/p).read_bytes()
 a=base.splitlines(keepends=True);b=d.splitlines(keepends=True)
 ops=difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes();changed=[(i,j,k,l) for t,i,j,k,l in ops if t!='equal']
 assert changed==allowed[p.split('final-specification-set/')[1]],(p,changed)
 preserved=[]
 for tag,i,j,k,l in ops:
  if tag=='equal':
   assert a[i:j]==b[k:l];preserved.append(dict(base_lines=[i+1,j],candidate_lines=[k+1,l],bytes=sum(map(len,a[i:j]))))
 changed_base_indices={n for t,i,j,k,l in ops if t!='equal' for n in range(i,j)}
 newrows=collections.Counter(s for s in b if s.startswith(b'|'))
 keep=[s for n,s in enumerate(a) if s.startswith(b'|') and n not in changed_base_indices]
 assert not (collections.Counter(keep)-newrows)
 old_kept+=len(keep)
 # Every local Markdown link resolves through its mirror or fixed B formal tree.
 links=[]
 for target in re.findall(r'\]\(([^)]+)\)',d.decode()):
  if '://' in target or target.startswith('#'):continue
  q=target.split('#')[0];normal=pathlib.Path(__import__('os').path.normpath(str(pathlib.Path(p).parent/q)))
  if (CAN/normal).is_file():qualified='CURRENT_BATCH_MIRROR'
  else:
   assert subprocess.run(['git','cat-file','-e',B+':'+str(normal)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode==0,(p,target)
   qualified='UNCHANGED_FIXED_B_TARGET'
  links.append(dict(link=target,resolved_path=str(normal),qualification=qualified))
 result.append(dict(path=p,changed_zero_based_half_open=[list(x) for x in changed],unchanged_spans=preserved,preserved_old_table_rows=len(keep),logical_links=links))
# Historical case rows retained in both shared catalogs and camera catalog.
selected={
'engine-overworld-wp11-15-59-60.md':['MV04','MV18','MV19','MR02','MR17','R5-DI02'],
'pokemon-rules-wp53-60-61-62-69-70.md':['FP01','FP02','FP05','FP24','FP25','FP33'],
'engine-overworld-wp16.md':['WR16','GR3-CAM06','GR3-CAM07','GR3-CAM08','GR3-CAM12','GR3-CAM15','GR3-CAM16','GR3-CAM17']}
history=[]
for name,ids in selected.items():
 p='deliverables/final-specification-set/test-catalog/'+name
 a=subprocess.check_output(['git','show',B+':'+p]).decode().splitlines();b=(CAN/p).read_text().splitlines()
 for id in ids:
  old=[s for s in a if s.startswith('| '+id+' |')];new=[s for s in b if s.startswith('| '+id+' |')]
  assert len(old)==len(new)==1 and old==new
  history.append(dict(path=p,id=id,old_bytes_equal=True,source_static_reassessment='Documented in per-id.json; byte retention alone is not semantic credit.'))
# These correct consumers were deliberately not mirrored.
for p in ['deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md','deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md','deliverables/final-specification-set/engine-overworld/wp13-move-route-matrix.md']:
 assert not (CAN/p).exists()
out=dict(schema='r7-u03-r1.document-scope-audit.v1',qualification='TOOL_VALIDATION only; no reference/model/host behavior execution',mirrors=result,preserved_old_table_rows=old_kept,historical_rows=history)
(HERE/'document-scope-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status='EXACT_MINIMAL_DIFF_AND_OLD_ROW_PRESERVATION',mirrors=len(result),preserved_old_table_rows=old_kept,historical_rows=len(history),logical_links=sum(len(r['logical_links']) for r in result),behavior_execution='NOT_EXECUTED')))
