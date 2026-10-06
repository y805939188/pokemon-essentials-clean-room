"""Own report document/privacy/snapshot consistency checks; no behavior tests."""
import pathlib,json,hashlib,gzip,re
O=pathlib.Path(__file__).parent;D='review/remediation/20261003-prepare/batches/B14/affected-B02-actual-review-2/';A='d48197f365c39925f795c1d325988c0d74e59979'
def h(b):return hashlib.sha256(b).hexdigest()
def get(n):return json.loads((O/n).read_text())
def save(n,x):(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
# Current completion labels distinguish mapped semantic reading from literal delivery history.
r=get('reading-log.json')
for e in r['complete_unfiltered_sections']:
 e['preliminary_semantic_state']=e.pop('semantic_state',None);e['semantic_state']='COMPLETE_MANUAL_UNIQUE_VALUE_CONSUMPTION_AND_EXACT_CONTEXT_REUSE; NATIVE_ORDER_TYPES_RELATIONSHIPS_VERIFIED';e['remaining_read_rule']='No unresolved mandatory semantics remain; source unlisted-range limits retained.'
r['semantics_are_not_runtime_evidence']=True;save('reading-log.json',r)
m=get('review-manifest.json');m['accepted_statistics']={'batches':'9/21','accepted_contribution_records':170,'public_contribution_records':194,'touched_IDs':142,'primary_IDs':109,'specific_minimum_satisfied':109,'minimum_missing':0,'minimum_insufficient':0,'strict_satisfied':100,'strict_pending':9,'canonical_OPEN':229,'canonical_CLOSED':0,'B14_unaccepted_contributions':24,'B14_primary':19};save('review-manifest.json',m)
# Bind every final fixed source read including continuation; identical source objects may have multiple read ranges.
sources=r['source_reads'];save('source-reading-identities.json',{'repository':'reference/pokemon-essentials','commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','read_mode':'STATIC_EXACT_GIT_SHOW_ONLY','ranges':sources,'ranges_not_branch_coverage':True,'execution':0})
checks=[]
def check(n,c):assert c,n;checks.append({'check':n,'passed':True})
cp=get('continuation-checkpoint.json');check('All36 preliminary file snapshots retain exact bytes',cp['file_count']==36)
for x in cp['preliminary_files']:
 rel=x['snapshot_path'][len(D):];b=(O/rel).read_bytes();check('Snapshot '+rel,len(b)==x['bytes'] and h(b)==x['sha256'])
check('First judgment immutable',h((O/'independent-first-judgment.md').read_bytes())==cp['immutable_first_document_sha256']=='5f2dfe6e4f6a889191df1ff2033d38882dbc2b118ddb7f06c48e1e9788591007')
check('First receipt immutable',h((O/'first-judgment-receipt.json').read_bytes())==cp['immutable_first_receipt_sha256'])
for n in ['report.md','findings.json','independent-first-judgment.md','author-comparison.md','review-manifest.json','input-identities.json','reading-log.json','static-designs.json']:check('Required '+n,(O/n).is_file())
f=get('findings.json');check('Current exact-ACT B02 PASS_SCOPED and no open local defect',f['reviewed_actual']==A and f['verdict']=='PASS_SCOPED' and not f['ACT_payload_findings'] and not f['gate_local_review_findings'])
check('All four historical process/coverage observations explicitly disposed',len(f['historical_review_observation_dispositions'])==4)
check('Mandatory reading complete',r['semantic_complete'] and r['mandatory_reading_complete'] and not r['unresolved_scope'])
check('Every459 unfiltered section complete and unexempted',len(r['complete_unfiltered_sections'])==459 and all(x['semantic_complete'] and not x['unfiltered_scope_exempted'] for x in r['complete_unfiltered_sections']))
n=get('native-reconstruction-verification.json');check('Native types/order/context/fresh reconstruction verified',n['native_types_key_array_orders_all_contexts_verified'] and n['fresh_fixed_Git_reconstruction_equals_preserved_v2_map'] and not n['unconfirmed_real_semantic_values'])
check('Final strict semantic index no unresolved values',not get('continuation-semantic-index.json')['unconfirmed'])
check('All24 qualified contribution dispositions',len(get('contribution-dispositions.json')['all24_current_qualified_dispositions'])==24)
check('All12 current B02 dispositions',len(get('accepted-owner-dispositions.json')['dispositions'])==12)
check('Full owner original/PLAN/root supplement consumed',get('owner-original-qualified-supplement.json')['all_new_semantic_values_consumed'])
check('Report identity externally assigned and B14 unaccepted',m['report_commit'] is None and not m['B14_accepted'] and not m['AREG_C_permitted_by_this_report'])
check('No pristine-order or index/ref byte attestation invented',not m['evidence_first_assessment']['pristine_literal_operational_order'] and m['index_ref_byte_attestation'] is None)
check('Effective backend remains UNVERIFIED','UNVERIFIED' in m['configuration']['effective_backend'])
check('No runtime/Demo/vector execution',m['runtime_observations']==m['proven_Demo']==m['behavior_vectors_executed']==0)
check('No transient raw-value cache published',not (O/'continuation-transient-corpus.json.gz').exists())
# Stream privacy scan includes compressed maps and immutable snapshots; do not emit matched values.
pattern=re.compile(rb'/(?:Users/|private/|tmp/|var/folders/)');violations=[];files=[]
for p in sorted(O.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(O).as_posix();data=p.read_bytes()
 if p.suffix=='.gz':
  with gzip.open(p,'rb') as z:
   tail=b''
   while True:
    q=z.read(1048576)
    if not q:break
    if pattern.search(tail+q):violations.append(rel)
    tail=q[-32:]
 elif pattern.search(data):violations.append(rel)
 if p.suffix=='.json':json.loads(data)
 if p.suffix=='.jsonl':
  for l in data.splitlines():
   if l:json.loads(l)
 files.append({'path':D+rel,'sha256':h(data),'bytes':len(data),'role':'IMMUTABLE_PRELIMINARY_CHECKPOINT' if rel.startswith('preliminary-checkpoint-1/') else 'CURRENT_REPORT_OR_DOCUMENT_BOOKKEEPING'})
check('All report/public payloads free of private host materialization paths',not violations)
save('report-qa.json',{'reviewed_actual':A,'type':'DOCUMENT_HASH_JSON_PRIVACY_SNAPSHOT_CHECKS_ONLY','checks':checks,'behavior_tests_executed':0,'privacy_violations':[],'no_backend_or_index_ref_certificate':True,'no_quality_inferred_from_QA':True})
# Manifest excludes itself. QA is produced first; no circular peer hashes or containing commit recursion.
files=[]
for p in sorted(O.rglob('*')):
 if p.is_file() and p.name!='report-file-manifest.json':
  rel=p.relative_to(O).as_posix();b=p.read_bytes();files.append({'path':D+rel,'sha256':h(b),'bytes':len(b),'role':'IMMUTABLE_PRELIMINARY_CHECKPOINT' if rel.startswith('preliminary-checkpoint-1/') else 'CURRENT_REPORT_OR_DOCUMENT_BOOKKEEPING'})
# The immutable old manifest is itself a checkpoint artifact and may be included by its relative path.
p=O/'preliminary-checkpoint-1/report-file-manifest.json';b=p.read_bytes();files.append({'path':D+'preliminary-checkpoint-1/report-file-manifest.json','sha256':h(b),'bytes':len(b),'role':'IMMUTABLE_PRELIMINARY_CHECKPOINT'})
save('report-file-manifest.json',{'reviewed_actual':A,'report_commit':None,'verdict':'PASS_SCOPED_B02_ONLY','self_hash_omitted':True,'contains':files,'first_receipt_and_preliminary36_immutable':True,'publication':'Coordinator mechanical publication only; no Git mutation or acceptance by reviewer.'})
print('Final QA passed',len(checks),'document checks;',len(files),'artifact identities; no private-path matches; first receipt and36 snapshots exact.')
