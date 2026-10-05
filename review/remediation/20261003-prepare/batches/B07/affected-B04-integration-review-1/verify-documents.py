"""Independent actual Git/text/hash audit only; no repository or reference program execution."""
import collections,csv,difflib,hashlib,json,pathlib,re,subprocess
R=pathlib.Path('/workspace/pokemon-essentials-clean-room');REFROOT=pathlib.Path('/tmp/rb04-reference');TMP=pathlib.Path('/tmp/b07-b04-actual')
ACT='adca83d63d18c94429cdb52aef9eaf7b8aa00189';UP='259a1c158f317c5e32830e04838a76aa82f4d20a';BASE='219cc3c182750155e9dbf2cb619f420b3922de27';CAND='a22df6b1d9465b68e45558c57bc69c61939baeaf';PREV='3e88d42b8d9313e1adbbc8944e54faa1b45e71a0';R07='19e2d5f9de40a9220059a62f785ac0bbc13b2154';ORIG='93e10babe0b9c9ef8b3f5277754541b447beeeb4';PLAN='41fffb540c6483f5296ea0d33b789b75180d27ed';REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
P='review/remediation/20261003-prepare/';D=P+'batches/B07/integration-stage-1/'
checks=[];cache={};identities={};diffs=[]
def git(*x,cwd=R):return subprocess.check_output(['git',*x],cwd=cwd)
def data(c,p):
 key=(c,p)
 if key not in cache:cache[key]=git('show',c+':'+p,cwd=REFROOT if c==REF else R)
 return cache[key]
def obj(c,p):return json.loads(data(c,p))
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
def check(n,v):checks.append({'check':n,'passed':bool(v)})
def ident(c,p):
 b=data(c,p);x={'commit':c,'path':p,'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'sha256':sha(b),'bytes':len(b)};identities[(c,p)]=x;return x
seen=set()
def verify(c,x):
 key=(c,x['path'],x['git_blob'],x['sha256'],x['bytes'])
 if key in seen:return
 seen.add(key);z=ident(c,x['path']);check('frozen identity '+c[:8]+':'+x['path'],all(z[k]==x[k] for k in ['git_blob','sha256','bytes']))
def walk(x):
 if isinstance(x,dict):
  if all(k in x for k in ['path','git_blob','sha256','bytes']) and isinstance(x['git_blob'],str):verify(x.get('commit',ACT),x)
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
def statuses(b,t):return [{'change':s,'path':p} for s,p in (x.split('\t') for x in git('diff','--no-renames','--name-status',b,t).decode().splitlines())]
m=obj(ACT,D+'integration-manifest.json');f=obj(ACT,D+'diff-and-freeze.json');h=obj(ACT,D+'downstream-handshake.json');counts=obj(ACT,D+'scope-counts.json');registration=obj(ACT,D+'finding-registration.json')['dispositions']
check('actual real commit exact single parent payload',git('rev-list','--parents','-n','1',ACT).decode().strip()==ACT+' 94aa281d6ff10d5b3e80c7df066d0ccd6d0f0c6f')
check('actual exact tree',git('rev-parse',ACT+'^{tree}').decode().strip()=='392c60655eff833399e796e081b18ae344cdaa82')
check('payload parent ordinary second merge',git('rev-parse',ACT+'^^').decode().strip()=='a0d2cec8af3a46e0e5a377966f4ee492ac9cd90e')
for row in obj(ACT,D+'merge-and-dependency-impact.json')['normal_merges']:
 check('merge exact parents/tree '+row['commit'],git('rev-list','--parents','-n','1',row['commit']).decode().strip().split()==[row['commit'],*row['parents']] and git('rev-parse',row['commit']+'^{tree}').decode().strip()==row['tree'])
check('final three evidence additions only',statuses(f['payload_commit'],ACT)==[{'change':'A','path':p} for p in sorted(f['final_actual_changed_paths'])])
formal=sorted(x['candidate']['path'] for x in obj(CAND,P+'batches/B07/dependency-manifest.json')['outputs14'])
public=sorted(x['path'] for x in m['current_public_paths']);sources=sorted(x['path'] for x in m['source_identities']);stage=sorted(git('ls-tree','-r','--name-only',ACT,D).decode().splitlines())
check('formal14 split8 final6 bounded originals',len(formal)==14 and sum(p.startswith('deliverables/') for p in formal)==8 and sum(p.startswith('specs/') for p in formal)==6)
check('incoming57 splitformal14 author11 reports32',len(sources)==57 and len(stage)==13 and len(public)==10)
expected=[{'change':'M' if p in formal else 'A','path':p} for p in sources]+[{'change':'M','path':p} for p in public]+[{'change':'A','path':p} for p in stage]
check('unfiltered actual80 scope no outside mutations',statuses(UP,ACT)==sorted(expected,key=lambda x:x['path']))
for label,base,n in [('upstream-to-actual',UP,80),('candidate-to-actual',CAND,59),('baseline-to-actual',BASE,84)]:
 b=git('diff','--no-ext-diff','--no-textconv','--no-renames','--binary',base,ACT);check('saved full '+label,b==(TMP/(label+'.diff')).read_bytes() and len(statuses(base,ACT))==n)
 diffs.append({'label':label,'base':base,'target':ACT,'bytes':len(b),'sha256':sha(b),'complete_paths':statuses(base,ACT),'semantic_read_policy':'All paths assessed; exact copied source/report bytes verified against independently fixed originals; structured registration objects read; no claim of renewed full business audit of unchanged historical content.'})
for row in m['source_identities']:
 verify(row['commit'],row);verify(ACT,row);check('incoming exact source equality '+row['path'],data(ACT,row['path'])==data(row['commit'],row['path']))
for row in f['full_patches']:
 b=data(ACT,row['path']);x=git('diff',*row['git_diff_options'],row['base_commit'],row['target_commit'])
 check('complete frozen payload patch '+row['path'],b==x and sha(b)==row['sha256'] and len(b)==row['bytes'] and statuses(row['base_commit'],row['target_commit'])==row['complete_path_statuses'])
for name in stage:
 if name.endswith('.json') and not name.endswith('validation-results.json'):
  walk(obj(ACT,name))
# Author/A-REG check totals are never used as proof, nor are their programs executed.
for row in obj(CAND,P+'batches/B07/dependency-manifest.json')['fixed_input_identities116']:verify(row['commit'],row)
bh=obj(BASE,P+'batches/B04/acceptance-stage-1/downstream-handshake.json');bm=obj(CAND,P+'batches/B07/dependency-manifest.json')
b04=sorted({x['current_acceptance_successor']['path'] for x in bh['B04_changed_B07_readers5']}|{x['path'] for x in bm['additional_B04_input_identities8']})
check('B04 five readers +eight other outputs13',len(b04)==13)
for p in b04:
 check('B04 oldactual accepted upstream candidate actual bytes '+p,all(data(c,p)==data(ACT,p) for c in ['9e2dadfa650e2111b77f9eae1f834cc00b8805d5',BASE,UP,CAND]));ident(ACT,p)
wp24='deliverables/final-specification-set/creature-rpg/wp24-player-trainers-partners.md'
check('B06 WP24 exact accepted candidate actual',data(BASE,wp24)==data(CAND,wp24)==data(UP,wp24)==data(ACT,wp24));ident(ACT,wp24)
for p in formal:check('all14 actual exact candidate '+p,data(ACT,p)==data(CAND,p))
fd=git('diff','--no-ext-diff','--no-textconv','--no-renames','--binary',BASE,ACT,'--',*formal);check('complete formal diff equals own prior independent formal',fd==data(PREV,P+'batches/B07/affected-B04-review-round-1/formal.diff'));(TMP/'formal.diff').write_bytes(fd)
# Exact xhigh correction and earlier accepted evidence, no history rewriting.
for x in statuses(BASE,UP):
 if '/batches/B04/acceptance-stage-1/' in x['path']:check('xhigh correction preserved '+x['path'],data(UP,x['path'])==data(ACT,x['path']))
statpath=P+'batches/B04/acceptance-stage-1/completion-statistics-successor.json';statistics=obj(UP,statpath)
check('114 accepted statistics immutable',data(UP,statpath)==data(ACT,statpath) and statistics==counts['prior_accepted_statistics_preserved'] and statistics['contribution_records']==114 and statistics['distinct_touched_IDs']==105 and statistics['primary_denominator']==75 and statistics['specific_revision_counts']=={'satisfied_scoped':74,'missing_specific_consumer':1,'insufficient_evidence':0} and statistics['strict_all_planned_contribution_counts']=={'all_contributor_batches_accepted':71,'pending':4})
g={x['id']:x for x in obj(ORIG,'review/global-independent-review/2026-10-03-fd82a639/findings.json')};a=obj(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json')
check('original canonical/history and approved plan not mutated',git('ls-tree',ACT,'review/global-independent-review/2026-10-03-fd82a639/findings.json')==git('ls-tree',UP,'review/global-independent-review/2026-10-03-fd82a639/findings.json') and data(ACT,'review/remediation-20261003-prepare/finding-acceptance.json')==data(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json'))
check('19 candidate registration/12primary/zero accepted',len(registration)==19 and sum(x['B07_primary'] for x in registration)==12 and counts['accepted_B07_contributions']==0)
for row in registration:
 o=g[row['id']];ac=a[row['id']]
 check('complete original/acceptance bound '+row['id'],row['original_complete_object_sha256']==sha(canon(o)) and row['acceptance_object_sha256']==sha(canon(ac)))
 check('effective original controls retained '+row['id'],all(row[k]==o.get(k) for k in ['current_qualifications','adjudication_precedence','effective_case_constraints','root_adjudications']) and row['all_extensions_controls']==[{k:e.get(k) for k in ['report','raw_id','adjudication','root_review']} for e in o.get('extensions',[])])
 check('registration remains pending OPEN '+row['id'],row['canonical_state']=='OPEN' and not row['canonical_edited'] and row['actual_R_B07_verdict']=='NOT_REVIEWED_PENDING_ULTRA' and row['actual_R_B04_verdict']=='NOT_REVIEWED_PENDING_ULTRA' and row['parent_C_acceptance']=='NOT_PERFORMED')
check('C003 all8 extensions retained',len(g['GIR-FD82-C003']['extensions'])==8)
prior=obj(PREV,P+'batches/B07/affected-B04-review-round-1/B04-conclusion-dispositions.json')
check('historical35/23 contribution scope preserved',len(prior['rows'])==35 and sum(x['role']=='PRIMARY' for x in prior['rows'])==23 and prior==obj(ACT,D+'scope-and-authorization-registration.json')['affected_R_B04_conclusion_dispositions_preserved'])
for row in prior['rows']:check('original/acceptance unchanged B04 '+row['id'],row['full_original_object_sha256']==sha(canon(g[row['id']])) and row['full_acceptance_object_sha256']==sha(canon(a[row['id']])))
# Public append and textual state, independent of A-REG totals.
publicrows={}
for name in ['approval-ledger','traceability-successor']:
 p=P+name+'.tsv';old=data(UP,p);cur=data(ACT,p);rows=list(csv.DictReader(cur.decode().splitlines(),delimiter='\t'));oldrows=list(csv.DictReader(old.decode().splitlines(),delimiter='\t'));new=rows[len(oldrows):]
 check('public old114 append exact '+name,cur.startswith(old) and len(oldrows)==114 and len(rows)==133 and len(new)==19 and {r['finding_id'] for r in new}=={r['id'] for r in registration})
 publicrows[name]=new
 for r in new:
  x=next(z for z in registration if z['id']==r['finding_id']);ob=json.loads(r['remaining_obligations'])
  check('public candidate state/binding '+name+':'+r['finding_id'],r['canonical_state']=='OPEN' and r['candidate_commit']==CAND and r['candidate_review_commit']==R07 and ob['actual_R_B07']=='PENDING_ULTRA' and ob['actual_R_B04']=='PENDING_ULTRA' and ob['parent_C']=='NOT_PERFORMED' and ob['other_batch_obligations']==x['other_batch_obligations'] and ob['affected_B04_candidate_report']==PREV)
  if name=='approval-ledger':check('approval actual no premature acceptance '+r['finding_id'],r['integration_verdict']=='NOT_REVIEWED_PENDING_TWO_ULTRA' and r['downstream_gate']=='BLOCKED' and 'CANDIDATE_SCOPED_PENDING_BOTH_ACTUAL_REVIEWS' in r['accepted_contribution_kind'])
  else:
   inputs=json.loads(r['current_clause_inputs']);check('trace actual clause identity '+r['finding_id'],inputs['reviewed_candidate']==CAND and inputs['locator']==x['formal_clause_locator'] and r['static_test_ids_not_executed']==x['static_locator'] and inputs['related_file_identities']==x['related_formal_file_identities'])
for p in public:
 if not p.endswith('.md'):continue
 cur=data(ACT,p).decode();old=data(UP,p).decode()
 if p.endswith('test-catalog/README.md'):
  added='\n\n## B07-G当前目录登记';prefix=cur[:cur.index(added)]
  expected=old.rstrip().replace('BE01–BE35、CX01–CX38','BE01–BE37、CX01–CX42').replace('IU01–IU48、SH01–SH26、GR01–GR44','IU01–IU59、SH01–SH28、GR01–GR53')
  check('catalog index only two ranges plus new status',prefix==expected)
 else:check('old public heading/body exact retained '+p,old in cur or (cur.startswith(''.join(old.splitlines(keepends=True)[:2])) and cur.endswith(''.join(old.splitlines(keepends=True)[2:]))))
 for target in re.findall(r'\]\(([^)]+)\)',cur[:max(0,len(cur)-len(old))+900]):
  if '://' not in target and not target.startswith('#'):check('new public relative link '+p+':'+target,(R/pathlib.Path(p).parent/target.split('#')[0]).exists())
 check('public retains limited scope and other owners '+p,'B07尚未接受' in cur or 'B07当前0接受贡献' in cur)
# Catalog deltas and section guards, no vector evaluation.
cat=[]
for p in [z for z in formal if '/test-catalog/' in z]:
 def rows(b):return [(m.group(1),s) for s in b.decode().splitlines() if (m:=re.match(r'^\| ((?:IU-|SH-|GR-|BG-|DC-|BE|CX|RM|CP)\d+) \|',s))]
 old=rows(data(BASE,p));new=rows(data(ACT,p));om=dict(old);added=[i for i,s in new if i not in om];changed=[i for i,s in new if i in om and s!=om[i]]
 check('catalog old ordered multiplicities '+p,[i for i,s in new if i in om]==[i for i,s in old])
 for sec in ['BG','DC','RM','CP']:
  def section(b):
   m=re.search(r'^## '+sec+r'[:：].*?(?=^## |\Z)',b.decode(),re.M|re.S);return m.group(0) if m else None
  check('protected whole section '+sec+' '+p,section(data(BASE,p))==section(data(ACT,p)))
 cat.append({'path':p,'old_count':len(old),'new_count':len(new),'new_ids':added,'changed_old':changed})
check('28 new/8 exact old static design premises',sum(len(x['new_ids']) for x in cat)==28 and sum(len(x['changed_old']) for x in cat)==8 and {i for x in cat for i in x['changed_old']}=={'SH-08','GR-15','GR-30','GR-31','GR-32','GR-33','GR-34','CX22'})
# Downstream exact input set and guard; no semantic parallelism acceptance.
batches=obj(PLAN,'review/remediation-20261003-prepare/batches.json')
(TMP/'plan-batches-shape.json').write_text(json.dumps({'type':type(batches).__name__,'sample_keys':list(batches[0]) if isinstance(batches,list) else list(batches)[:10]}))
check('downstream remains blocked and original permission absent',h['status']=='BLOCKED_BOTH_B07_ACTUAL_ULTRA_AND_PARENT_C' and not h['B08']['accepted'] and not h['B08']['task_dispatched'] and not h['B08']['original_specs_write_authorized'] and h['downstream_tasks_dispatched']==0 and 'READ_ONLY' in h['B08']['WP34_body'])
check('downstream79/8/17/9 and reverse5/change3',len(h['B08']['planned_reads'])==79 and len(h['B08']['allowed_writes'])==8 and len(h['B08']['full17_control_bindings'])==17 and len(h['B08']['primary_IDs'])==9 and len(h['B08']['changed_planned_B07_readers3'])==3 and len(h['B08_to_B07_reverse_readers5'])==5)
check('bounded inquiry no parallel permission',h['bounded_parallel_inquiry']['tasks_created']==0 and h['bounded_parallel_inquiry']['writers_authorized_in_parallel']==0)
for c,p in [(ORIG,'review/global-independent-review/2026-10-03-fd82a639/findings.json'),(PLAN,'review/remediation-20261003-prepare/finding-acceptance.json'),(UP,statpath),(ACT,D+'diff-and-freeze.json')]:ident(c,p)
check('reference real pinned commit tree clean',git('cat-file','-t',REF,cwd=REFROOT).strip()==b'commit' and git('rev-parse','HEAD',cwd=REFROOT).decode().strip()==REF and git('rev-parse','HEAD^{tree}',cwd=REFROOT).decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0' and git('remote','get-url','origin',cwd=REFROOT).decode().strip()=='https://github.com/Maruno17/pokemon-essentials.git' and not git('status','--porcelain',cwd=REFROOT))

# Recompute the six original-sync content identities; never infer past chronology.
sync=obj(CAND,P+'batches/B07/original-sync-plan.json');parts=[]
for row in sync['files']:
 p=row['path'];old=data(BASE,p);new=data(ACT,p)
 part=''.join(difflib.unified_diff(old.decode().splitlines(keepends=True),new.decode().splitlines(keepends=True),fromfile='a/'+p,tofile='b/'+p)).replace('\n \n','\n\n');parts.append(part)
 check('actual original sync old/new/diff '+p,sha(old)==row['before_sha256'] and sha(new)==row['after_sha256'] and sha(part.encode())==row['diff_sha256'])
check('actual full textual six-original patch',data(ACT,P+'batches/B07/original-sync.patch')=='\n'.join(parts).encode())
b8=next(x for x in batches if x['id']=='B08')
check('B08 planned reads/writes exact fixed plan sets',{x['path'] for x in h['B08']['planned_reads']}==set(b8['read_paths']) and set(h['B08']['allowed_writes'])==set(b8['write_paths']) and set(h['B08']['primary_IDs'])==set(b8['primary_finding_ids']) and {x['id'] for x in h['B08']['full17_control_bindings']}==set(b8['contribution_finding_ids']))
for row in h['B08']['full17_control_bindings']:
 o=g[row['id']];ac=a[row['id']]
 check('B08 fixed control guard only '+row['id'],row['original_complete_object_sha256']==sha(canon(o)) and row['acceptance_object_sha256']==sha(canon(ac)) and row['root_adjudications']==o['root_adjudications'] and row['current_qualifications']==o['current_qualifications'] and row['effective_case_constraints']==o.get('effective_case_constraints'))
check('229 mandatory fixed acceptance objects unchanged no canonical closure in actual registration',len(a)==229 and counts['canonical_required_OPEN']==229 and counts['CLOSED']==0 and all(x['canonical_state']=='OPEN' and not x['canonical_edited'] for x in registration))
result={'kind':'INDEPENDENT_ACTUAL_GIT_HASH_JSON_TEXT_AUDIT_NOT_BEHAVIOR_EXECUTION','reviewed_actual':ACT,'actual_tree':'392c60655eff833399e796e081b18ae344cdaa82','management_upstream':UP,'candidate':CAND,'checks':checks,'passed':sum(x['passed'] for x in checks),'failed':[x for x in checks if not x['passed']],'identities':list(identities.values()),'full_diffs':diffs,'catalog_changes':cat,'public_new_rows':publicrows,'B04_formal13':b04,'B07_formal14':formal,'execution':{'reference':0,'runtime':0,'vectors':0,'demo':0}}
(TMP/'independent-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'passed':result['passed'],'failed':result['failed'],'identity_count':len(identities),'catalog_changes':cat},ensure_ascii=False,indent=2))
if result['failed']:raise SystemExit(1)
