"""Final bounded B14-G document/identity bookkeeping; no actual quality certification."""
import bookkeeping as k
import pathlib,json,csv,io,hashlib,re,subprocess,os
G=k.G;B=k.B;A=k.A;C=k.C;P='review/remediation/20261003-prepare/';BP=P+'batches/B14/'
env=dict(os.environ,GIT_OPTIONAL_LOCKS='0',PYTHONDONTWRITEBYTECODE='1')
def gitargs(*args):return subprocess.check_output(['git',*args],env=env)
def rows(data):return [l for l in data.splitlines(keepends=True) if re.match(rb'^\|\s*[A-Z][A-Za-z0-9_-]*\d[A-Za-z0-9_-]*\s*\|',l)]
checks=[]
def check(name,result,detail=None):
 checks.append(dict(check=name,result=bool(result),detail=detail));assert result,name
check('HEAD remains accepted predecessor',gitargs('rev-parse','HEAD').decode().strip()==A)
check('Exact C3 tree',gitargs('show','--no-patch','--format=%T',C).decode().strip()==B['candidate_tree'])
for x in json.loads((G/'copy-identities.json').read_text())['files']:
 data=pathlib.Path(x['path']).read_bytes();check('Unchanged exact copy '+x['path'],data==k.git(x['commit'],x['path']))
protected=[]
for p in [p for p in B['formal_paths'] if '/test-catalog/' in p]:
 old=rows(k.git(B['frozen_C2'],p));now=rows(pathlib.Path(p).read_bytes());keep=[l for l in now if not re.match(rb'^\|\s*WT4[1-4]\s*\|',l)]
 check('C2 full row bytes/order/multiplicity '+p,keep==old)
 if 'pokemon-rules-' in p:check('Whole second catalog C2-identical',pathlib.Path(p).read_bytes()==k.git(B['frozen_C2'],p))
 before=k.git(A,p).splitlines(keepends=True);after=pathlib.Path(p).read_bytes().splitlines(keepends=True)
 def owner_segments(ls):
  out=[];local=False
  for l in ls:
   if l.startswith(b'## '):local=bool(re.match(rb'^## (?:I\.|J\.|BP[:\xef]|FP[:\xef])',l) or re.match(rb'^## (?:BP|FP)',l))
   if not local:out.append(l)
  return out
 check('Accepted nonlocal whole catalog segments '+p,owner_segments(before)==owner_segments(after))
 protected.append(dict(path=p,old_C2_rows=len(old),current_rows=len(now),all_old_line_bytes_order_multiplicity=True,nonlocal_accepted_segments=True))
check('Catalog totals361+148',sum(x['current_rows'] for x in protected)==509 and sum(x['old_C2_rows'] for x in protected)==505)
for p in [P+'approval-ledger.tsv',P+'traceability-successor.tsv']:
 before=k.git(A,p);after=pathlib.Path(p).read_bytes();rs=list(csv.DictReader(io.StringIO(after.decode()),delimiter='\t'));check('170 complete accepted rows unchanged '+p,after.startswith(before));check('Exactly194 public rows '+p,len(rs)==194);check('Exactly24 B14 rows '+p,len(rs[170:])==24)
 reg=json.loads((G/'finding-registration.json').read_text());check('24 distinct contribution record keys',len({r['record_key'] for r in reg['dispositions']})==24)
check('No accepted B14 rows',reg['accepted_B14']==0 and all(not r['accepted_B14_contribution'] for r in reg['dispositions']))
check('Eight distinct pending actual packages',len(json.loads((G/'gate-requests.json').read_text())['separate_packages'])==8)
changed=gitargs('diff','--no-ext-diff','--no-textconv','--no-renames','--name-only',A).decode().splitlines();untracked=gitargs('ls-files','--others','--exclude-standard').decode().splitlines()
authorized=set(B['formal_paths']+B['evidence_paths']+B['public_paths']+[p for r in B['report_bindings'] for p in r['paths']])
check('No unexpected tracked change',set(changed)<=authorized)
check('No unexpected untracked path',all(p in authorized or p.startswith(G.as_posix()+'/') for p in untracked))
check('All ten authorized public paths changed',all(p in changed for p in B['public_paths']))
# Each immutable known full stream is separately identified; no raw source/private payload archive is copied.
diffs=[]
for start in [A,B['frozen_C2']]:
 args=['diff','--no-ext-diff','--no-textconv','--no-renames','--binary','--full-index','--no-color',start,C]
 data=gitargs(*args);names=gitargs('diff','--no-ext-diff','--no-textconv','--no-renames','--name-only',start,C).decode().splitlines()
 diffs.append(dict(before_commit=start,after_commit=C,command='git '+' '.join(args),path_filter=None,complete_scope=names,path_count=len(names),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),lines=len(data.splitlines()),storage='Exact frozen-endpoint reproduction, no new raw source/private archive',binding='Historical candidate comparison only, never an actual receipt'))
check('Exact unfiltered candidate diff format',[(x['path_count'],x['bytes']) for x in diffs]==[(61,988409),(18,304458)])
k.save('unfiltered-source-diff-identities.json',dict(stage='B14-G',diffs=diffs,future_actual='All eight packages require full unfiltered predecessor→ACT and C3→ACT after external identity; pending, not substituted by these historical streams.'))
# Static reference object identities only. No source body is copied into these records.
reference=os.environ['B14_STATIC_REFERENCE_MATERIALIZATION'];S='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';T='7589c800b61ba13a13040ed0d686979b80a84fd0'
check('Fixed reference tree',subprocess.check_output(['git','-C',reference,'show','--no-patch','--format=%T',S]).decode().strip()==T)
source={}
def walk(v):
 if isinstance(v,dict):
  p=v.get('path')
  if isinstance(p,str) and p.startswith(('Data/','PBS/')) and v.get('commit')==S and ('sha256' in v or 'git_blob' in v):source[p]=v
  for w in v.values():walk(w)
 elif isinstance(v,list):
  for w in v:walk(w)
walk(reg);sourceids=[]
for p,v in source.items():
 data=subprocess.check_output(['git','-C',reference,'show',S+':'+p]);x=k.identity(data,p,'REFERENCE_STATIC_GIT_IDENTITY_ONLY',S)
 for f in ['git_blob','sha256','bytes']:
  if f in v:check('Source lineage '+p+'/'+f,x[f]==v[f])
 sourceids.append(x)
k.save('source-lineage.json',dict(stage='B14-G',logical_reference='reference/pokemon-essentials/',commit=S,tree=T,identity_checks=sourceids,source_semantic_read_by_G=False,source_execution=0,behavior_proof=False,evidence_lineage=BP+'review-round-3/contribution-review.json#records/*/current_evidence/source_trace',limits=G.as_posix()+'/source-limits.json'))
check('JSON structure of all bounded new records',all(isinstance(json.loads(p.read_text()),(dict,list)) for p in G.glob('*.json')))
# New source-lineage/current records need no production tests; these booleans are document bookkeeping.
k.save('conflict-and-validation.json',dict(stage='B14-G',status='DOCUMENT_BOOKKEEPING_COMPLETED_NOT_QUALITY_PASS',checks=checks,copy_count=216,formal12_unchanged_from_C3=True,evidence49_unchanged_from_C3=True,reports155_unchanged_at_exact_supplied_commits=True,catalogs=protected,public_schema_unchanged=True,accepted_rows170_preserved=True,new_B14_records=24,accepted_B14=0,public_total194=True,conflict_record=dict(method='Initial clean accepted predecessor; copy each exact authorized source object without textual merge or conflict resolution; tracked/untracked full path scopes checked.',textual_conflicts=[],unexpected_semantic_conflict_observed=False,semantic_NOT_AFFECTED_certified=False,ours_theirs_used=False,additional_path_amendment_required=False,actual_gates_pending=8),Git_writer_actions='No add/stage/commit/push/fetch/switch/reset/clean/update-ref/index mutation command issued; coordinator performs mechanical freeze.',index_ref_byte_attestation='Not asserted; initial status was read without a prior index checksum. Later scope checks disable optional locks.',runtime_observations=0,proven_Demo_chains=0,behavior_vectors_executed=0,configuration=B['configuration'],writer_actual_PASS=False,acceptance=False))
print('Document checks',len(checks),'completed; actual quality gates8 still pending; copied216/public10 only plus boundedG records.')
