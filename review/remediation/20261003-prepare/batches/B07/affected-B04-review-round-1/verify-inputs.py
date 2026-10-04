"""Own Git/hash/document checks only; never execute reference or behavior vectors."""
import collections, difflib, hashlib, json, pathlib, re, subprocess
ROOT=pathlib.Path('/workspace/pokemon-essentials-clean-room')
BASE='219cc3c182750155e9dbf2cb619f420b3922de27'
CAND='a22df6b1d9465b68e45558c57bc69c61939baeaf'
ACTUAL='9e2dadfa650e2111b77f9eae1f834cc00b8805d5'
FINAL='93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN='41fffb540c6483f5296ea0d33b789b75180d27ed'
REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
P='review/remediation/20261003-prepare/batches/'
checks=[]; cache={}; identities=[]
def git(*args, cwd=ROOT):return subprocess.check_output(['git',*args],cwd=cwd)
def data(commit,path):
 key=(commit,path)
 if key not in cache:cache[key]=git('show',commit+':'+path)
 return cache[key]
def obj(commit,path):return json.loads(data(commit,path))
def sha(b):return hashlib.sha256(b).hexdigest()
def canonical(o):return json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def check(n,c,details=None):checks.append({'check':n,'passed':bool(c),'details':details})
def ident(c,p):
 b=data(c,p);r={'commit':c,'path':p,'git_blob':blob(b),'sha256':sha(b),'bytes':len(b)};identities.append(r);return r
def verify(c,r):
 a=ident(c,r['path']);check('identity '+c+':'+r['path'],all(a[k]==r[k] for k in ['git_blob','sha256','bytes']))
h=obj(BASE,P+'B04/acceptance-stage-1/downstream-handshake.json')
m=obj(CAND,P+'B07/dependency-manifest.json')
check('candidate exact one parent',git('rev-list','--parents','-n','1',CAND).decode().strip()==CAND+' '+BASE)
check('candidate tree',git('rev-parse',CAND+'^{tree}').decode().strip()=='336fc0f3693d20b733d40f60d42d3bbe6323e52f')
check('accepted parent report chain',git('rev-parse',BASE+'^').decode().strip()=='acda1abc811cc07ea83c6a0930872e9a8cea174e')
for r in m['fixed_input_identities116']:verify(r['commit'],r)
check('fixed input count116',len(m['fixed_input_identities116'])==116)
statuses=[l.split('\t') for l in git('diff','--no-ext-diff','--no-textconv','--no-renames','--name-status',BASE,CAND).decode().splitlines()]
formal=sorted(r['candidate']['path'] for r in m['outputs14'])
check('14 distinct formal identities',len(formal)==14 and len(set(formal))==14)
check('8 final and6 originals',sum(p.startswith('deliverables/') for p in formal)==8 and sum(p.startswith('specs/') for p in formal)==6)
check('only formal14 and batch author11',len(statuses)==25 and all((s=='M' and p in formal) or (s=='A' and p.startswith(P+'B07/') and '/' not in p[len(P+'B07/'):]) for s,p in statuses))
for r in m['outputs14']:
 verify(BASE,r['baseline']);verify(CAND,r['candidate'])
for r in h['B04_changed_B07_readers5']:
 a=r['current_acceptance_successor'];verify(BASE,a);verify(CAND,a)
for r in m['additional_B04_input_identities8']:verify(BASE,r);verify(CAND,r)
b04formal=sorted(set([r['current_acceptance_successor']['path'] for r in h['B04_changed_B07_readers5']]+[r['path'] for r in m['additional_B04_input_identities8']]))
check('all13 B04 formal actual accepted candidate unchanged',len(b04formal)==13 and all(data(ACTUAL,p)==data(BASE,p)==data(CAND,p) for p in b04formal))
wp24='deliverables/final-specification-set/creature-rpg/wp24-player-trainers-partners.md'
check('B06 WP24 actual accepted candidate byte identical',data(ACTUAL,wp24)==data(BASE,wp24)==data(CAND,wp24))
for r in m['B04_changed_B07_consumers']:
 verify(BASE,r['before']);verify(CAND,r['after']);check('reverse consumer really changed '+r['path'],data(BASE,r['path'])!=data(CAND,r['path']))
g=obj(FINAL,'review/global-independent-review/2026-10-03-fd82a639/findings.json')
a=obj(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json')
gm={r['id']:r for r in g}
check('fixed original 233 and acceptance229',len(g)==233 and len(a)==229)
for r in h['contribution_controls']:
 check('full original control '+r['id'],canonical(r['complete_original_object'])==canonical(gm[r['id']]))
 check('full acceptance control '+r['id'],canonical(r['complete_approved_acceptance'])==canonical(a[r['id']]))
 check('control object hashes '+r['id'],sha(canonical(gm[r['id']]))==r['original_complete_object_sha256'] and sha(canonical(a[r['id']]))==r['acceptance_object_sha256'])
check('C003 all8 final extensions',len(gm['GIR-FD82-C003']['extensions'])==8)
catalog_changes=[]
def rows(b):return [(m.group(1),line) for line in b.decode().splitlines() if (m:=re.match(r'^\| ((?:IU-|SH-|GR-|BG-|DC-|BE|CX|RM|CP)\d+) \|',line))]
for p in [x for x in formal if '/test-catalog/' in x]:
 old=rows(data(BASE,p));new=rows(data(CAND,p));oldids=[x[0] for x in old];newids=[x[0] for x in new]
 check('old catalog order and occurrences '+p,[i for i in newids if i in set(oldids)]==oldids)
 om={i:line for i,line in old};changed=[i for i,line in new if i in om and om[i]!=line];added=[i for i,line in new if i not in om]
 catalog_changes.append({'path':p,'added':added,'changed_old':changed})
 for prefix in ['BG-','DC-','RM','CP']:
  check('protected rows '+prefix+' '+p,[v for i,v in old if i.startswith(prefix)]==[v for i,v in new if i.startswith(prefix)])
 # Full protected sections, including headings and blank lines.
 for sec in ['BG','DC','RM','CP']:
  def section(b):
   mt=re.search(r'^## '+sec+r'[:：].*?(?=^## |\Z)',b.decode(),re.M|re.S);return mt.group(0) if mt else None
  check('protected whole section '+sec+' '+p,section(data(BASE,p))==section(data(CAND,p)))
check('28 added static records',sum(len(r['added']) for r in catalog_changes)==28)
check('8 necessary old row corrections',sum(len(r['changed_old']) for r in catalog_changes)==8)
check('exact corrected old IDs',set(i for r in catalog_changes for i in r['changed_old'])=={'SH-08','GR-15','GR-30','GR-31','GR-32','GR-33','GR-34','CX22'})
for s,p in statuses:
 if s=='A' and p.endswith('.json'):
  check('new author JSON parses '+p,isinstance(obj(CAND,p),(dict,list)))
patch=data(CAND,P+'B07/original-sync.patch')
syncplan=obj(CAND,P+'B07/original-sync-plan.json')
parts=[]
for row in syncplan['files']:
 p=row['path'];old=data(BASE,p);new=data(CAND,p)
 part=''.join(difflib.unified_diff(old.decode().splitlines(keepends=True),new.decode().splitlines(keepends=True),fromfile='a/'+p,tofile='b/'+p)).replace('\n \n','\n\n')
 parts.append(part)
 check('original sync old/new and prepared diff hashes '+p,sha(old)==row['before_sha256'] and sha(new)==row['after_sha256'] and sha(part.encode())==row['diff_sha256'])
check('six original sync complete content in declared unified display format',patch=='\n'.join(parts).encode(), 'Own initial expectation of native Git headers was corrected: author uses textual unified diff, no diff --git/index headers, empty context lines have no leading space, one blank separator between files. Full reconstructed hunks and per-file hashes checked; no behavior execution.')
check('candidate diff whitespace',subprocess.run(['git','diff','--check',BASE,CAND],cwd=ROOT,capture_output=True).returncode==0)
refroot=pathlib.Path('/tmp/rb04-reference')
check('independent reference real commit type',git('cat-file','-t',REF,cwd=refroot).decode().strip()=='commit')
check('independent reference HEAD',git('rev-parse','HEAD',cwd=refroot).decode().strip()==REF)
check('independent reference tree',git('rev-parse',REF+'^{tree}',cwd=refroot).decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0')
check('independent reference origin',git('remote','get-url','origin',cwd=refroot).decode().strip()=='https://github.com/Maruno17/pokemon-essentials.git')
check('independent reference remains clean',git('status','--porcelain',cwd=refroot)==b'')
diffs=[]
for label,ps in [('complete',[]),('formal',formal),('reverse', [r['path'] for r in m['B04_changed_B07_consumers']])]:
 b=git('diff','--no-ext-diff','--no-textconv','--no-renames','--binary',BASE,CAND,*(['--']+ps if ps else []));pathlib.Path('/tmp/b07-b04-'+label+'.diff').write_bytes(b);diffs.append({'label':label,'before':BASE,'after':CAND,'bytes':len(b),'sha256':sha(b),'paths':ps})
# Additional checks performed only after independent-first-judgment was frozen.
am=obj(CAND,P+'B07/acceptance-map.json')['contributions']
check('author mapping exact19 and12 primary',len(am)==19 and sum(r['B07_primary'] for r in am)==12 and {r['id'] for r in am}==set(h['contribution_finding_ids']))
for r in am:
 fid=r['id'];f=gm[fid];ac=a[fid]
 check('author mapping fixed hashes '+fid,r['original_complete_object_sha256']==sha(canonical(f)) and r['acceptance_object_sha256']==sha(canonical(ac)))
 check('author mapping current qualifications '+fid,r['current_qualifications']==f['current_qualifications'])
 check('author mapping final adjudications '+fid,r['root_adjudications']==f['root_adjudications'])
check('traceability 19 rows',len(data(CAND,P+'B07/traceability.tsv').decode().splitlines())==20)
source=obj(CAND,P+'B07/source-reading-log.json')
for r in source['files']:
 b=git('show',REF+':'+r['path'],cwd=refroot);lines=b.splitlines()
 check('author source fixed bytes '+r['path'],sha(b)==r['sha256'] and blob(b)==r['git_blob'] and len(b)==r['bytes'] and len(lines)==r['line_count'])
 readset=set();unreadset=set()
 for target,key in [(readset,'inspected_ranges'),(unreadset,'remaining_ranges_unread')]:
  for x,z in r[key]:target.update(range(x,z+1))
 check('author source range accounting '+r['path'],not(readset&unreadset) and readset|unreadset==set(range(1,len(lines)+1)))
for r in obj('acda1abc811cc07ea83c6a0930872e9a8cea174e',P+'B04/integration-review-1/finding-dispositions.json')['rows']:
 check('historical B04 fixed original/acceptance objects '+r['id'],sha(canonical(gm[r['id']]))==r['original_complete_object_sha256'] and sha(canonical(a[r['id']]))==r['acceptance_object_sha256'])
for p in formal:
 old=data(BASE,p).decode();new=data(CAND,p).decode()
 for target in set(re.findall(r'\]\(([^)]+\.md)\)',new))-set(re.findall(r'\]\(([^)]+\.md)\)',old)):
  check('new dependency link resolves '+p+':'+target,(ROOT/pathlib.Path(p).parent/target).is_file())
check('WP31 cancellation paragraph3 unchanged',next(x for x in data(BASE,formal[3]).decode().splitlines() if x.startswith('3. **取消**'))==next(x for x in data(CAND,formal[3]).decode().splitlines() if x.startswith('3. **取消**')))
result={'kind':'independent Git/hash/document bookkeeping; no behavior execution','reviewed_candidate':CAND,'baseline':BASE,'checks':checks,'passed':sum(r['passed'] for r in checks),'failed':[r for r in checks if not r['passed']],'identities':identities,'catalog_changes':catalog_changes,'diffs':diffs,'runtime_observations':0,'reference_execution':0,'behavior_vectors_executed':0,'proven_demo_chains':0}
pathlib.Path('/tmp/b07-b04-independent-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'passed':result['passed'],'failed':result['failed'],'catalog_changes':catalog_changes,'diffs':[{k:v for k,v in x.items() if k!='paths'} for x in diffs]},ensure_ascii=False,indent=2))
