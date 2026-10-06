# Independent current ACT document/registry checks, not behavioral evidence.
import subprocess,json,pathlib,re,hashlib,csv,io,collections
D=pathlib.Path(__file__).parent;A='d48197f365c39925f795c1d325988c0d74e59979';B='1e6b11a47370f1c7c4659a32443fc1afda597bac';C='c06db6cd964188b3c693a9b7820e3a8aaffe0b04';O='93e10babe0b9c9ef8b3f5277754541b447beeeb4';P='41fffb540c6483f5296ea0d33b789b75180d27ed';G='review/remediation/20261003-prepare/batches/B14/integration-stage-1/'
def get(c,p):return subprocess.check_output(['git','show',c+':'+p])
def js(p):return json.loads(get(A,G+p))
def hash(b):return hashlib.sha256(b).hexdigest()
def ident(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
reg=js('finding-registration.json');locs=js('clause-location-bindings.json');gate=js('actual-request-B07.json');records={x['id']:x for x in reg['dispositions']};results=[]
assert len(records)==24 and reg['primary']==19 and reg['shared']==5 and reg['accepted_B14']==0
for id,r in records.items():
 assert r['record_key']=='B14/'+id
 assert locs['records'][id]['current_formal_locations']==r['current_formal_locations']
 for doc in r['current_formal_locations']:
  data=get(A,doc['path']);lines=data.splitlines(keepends=True);meta=doc['identity'];assert len(data)==meta['bytes'] and hash(data)==meta['sha256'] and ident(data)==meta['git_blob']
  for l in doc['current_heading_locators']:
   raw=lines[l['line']-1];assert raw.decode().rstrip('\r\n')==l['heading'];assert hash(raw)==l['heading_sha256'];m=re.match(r'^#{2,6}\s+(\d+(?:\.\d+)*)\.?\s',l['heading']);assert m and m[1]==l['section_number']
   if l.get('selection_kind')=='SINGLE_AUTHORIZED_SPLASH_SENTENCE':
    line=lines[l['selected_line']-1];part=line[l['utf8_byte_start']:l['utf8_byte_end_exclusive']];assert hash(line)==l['line_sha256'] and hash(part)==l['selected_sentence_sha256'] and len(part)==l['selected_sentence_bytes'];assert part.decode().startswith('Rain类别') and part.decode().rstrip().endswith('。')
  for b in doc['clause_bindings']:
   ns=[]
   for term in b['selector'].split('/'):
    m=re.fullmatch(r'§(\d+(?:\.\d+)*)(?:–(\d+(?:\.\d+)*))?',term);assert m
    first=tuple(map(int,m[1].split('.')))
    if m[2]:
     last=tuple(map(int,m[2].split('.')));assert first[:-1]==last[:-1];ns += ['.'.join(map(str,first[:-1]+(i,))) for i in range(first[-1],last[-1]+1)]
    else:ns.append(m[1])
   assert b['expanded_sections']==list(dict.fromkeys(ns))
 results.append({'id':id,'record_key':r['record_key'],'formal_documents':len(r['current_formal_locations']),'exact_document_heading_sentence_and_expansion_bindings':True})
receipts={x['owner']:x['report_commit'] for x in gate['all_applicable_candidate_receipts']};tables=[]
for path in ['review/remediation/20261003-prepare/approval-ledger.tsv','review/remediation/20261003-prepare/traceability-successor.tsv']:
 rs=list(csv.DictReader(io.StringIO(get(A,path).decode()),delimiter='\t'));tail=rs[170:];assert len(tail)==24 and [r['finding_id'] for r in tail]==list(records)
 for row in tail:
  r=records[row['finding_id']];ob=json.loads(row['remaining_obligations']);assert ob['record_key']==r['record_key'];assert set(ob['actual_gates'])==set(receipts);assert all('PENDING' in z for z in ob['actual_gates'].values());assert ob['parent_C']=='NOT_PERFORMED' and not ob['canonical_closure'];assert ob['current_clause_bindings']==G+'clause-location-bindings.json#records/'+r['id']
  for cr in ob['candidate_receipts']:assert cr['reviewed_candidate']==C and cr['report_commit']==receipts[cr['owner']]
  if path.endswith('approval-ledger.tsv'):
   assert row['candidate_commit']==C and row['candidate_review_commit']==receipts['FULL'];assert row['public_registration_verdict']=='INTEGRATED_PENDING_ACTUAL';assert not row['reviewed_integration_commit'] and not row['integration_review_commit']
  if 'current_clause_inputs' in row:assert json.loads(row['current_clause_inputs'])['formal']==r['current_formal_locations']
 tables.append({'path':path,'24_distinct_pending_records_correct_candidate_receipts_and_current_formal_mirrors':True,'accepted_prefix_preserved':get(A,path).startswith(get(B,path))})
# Whole protected catalog sections, not just row counts.
segments=[]
for p in ['deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md','deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md']:
 def protect(b):
  out=[];local=False
  for l in b.splitlines(keepends=True):
   if l.startswith(b'## '):local=bool(re.match(rb'^## (?:I\.|J\.|BP[:\xef]|FP[:\xef]|BP|FP)',l))
   if not local:out.append(l)
  return b''.join(out)
 assert protect(get(A,p))==protect(get(B,p));segments.append({'path':p,'protected_whole_sections_headers_blank_lines_rows_terminators_exact':True})
# Every accepted/historical tree entry outside the enumerated changes has exact mode/type/blob.
old={};now={}
for c,target in [(B,old),(A,now)]:
 for line in subprocess.check_output(['git','ls-tree','-r',c]).decode().splitlines():
  identity,p=line.split('\t',1);target[p]=identity
changed=set(subprocess.check_output(['git','diff','--no-ext-diff','--no-textconv','--no-renames','--name-only',B,A]).decode().splitlines())
assert all(now.get(p)==v for p,v in old.items() if p not in changed)
res={'reviewed_ACT':A,'clause_and_registration_checks':results,'public_relationship_checks':tables,'whole_catalog_protection':segments,'unaffected_predecessor_entries_exact':sum(p not in changed for p in old),'accepted_and_historical_outside_authorized_changes_protected':True,'eight_candidate_report_commits_by_role':receipts,'reading_vs_check':'These exact-identity/structure checks supplement manual clause/caller/condition reading. No prior PASS is transferred.'}
(D/'integration-relationship-checks.json').write_text(json.dumps(res,indent=2)+'\n');print('CURRENT BINDINGS VERIFIED',len(results),'records',len(receipts),'candidate receipts; public mirrors and whole owner segments exact')
