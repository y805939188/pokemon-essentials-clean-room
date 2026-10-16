"""Finite report integrity; never executes reference behavior."""
import datetime,hashlib,json,pathlib,subprocess
ROOT=pathlib.Path(__file__).resolve().parents[1]
SPEC=pathlib.Path('/workspace/pokemon-essentials-clean-room');REF=pathlib.Path('/workspace/pokemon-essentials')
TASK=ROOT.relative_to(SPEC).as_posix();B8='fd1df570cad987dc3852a3b958f03916e317f7fe';R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
checks=[]
def read(n):return json.loads((ROOT/n).read_text())
def git(repo,*a):return subprocess.check_output(['git','-C',str(repo),*a])
def check(n,c):
 checks.append((n,bool(c)))
 if not c:raise ValueError(n)
def full(a,b,ranges):return all(any(x<=n<=z for x,z in ranges) for n in range(a,b+1))
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
try:
 for p in ROOT.glob('*.json'):json.loads(p.read_text())
 ids=read('identities.json')['payloads'];led=read('reading-ledger.json')
 for k,i in ids.items():
  b=git(i['repo'],'show',i['commit']+':'+i['path']);blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
  check(k+'identity',len(b)==i['bytes'] and blob==i['blob'] and hashlib.sha256(b).hexdigest()==i['sha256'])
  check(k+'unchanged',(ROOT/i['copy']).read_bytes()==b if k.startswith('I') else (pathlib.Path(i['repo'])/i['path']).read_bytes()==b)
 sec={s['id']:(f,s) for f in led['primary'] for s in f['all_sections']}
 check('16full/6712sections',len(led['primary'])==16 and len(sec)==6712 and all(f['file_status']=='FULL_READ' and not f['unread_ranges'] for f in led['primary']))
 ranges={d['identity_id']:d['read_ranges'] for d in led['read_dependencies']};ranges.update({f['identity_id']:f['read_ranges'] for f in led['primary']})
 def ref(r):
  k=r['identity_id'];a,z=r['lines'];check('readref'+k,k in ids and 1<=a<=z<=ids[k]['lines'] and full(a,z,ranges[k]))
 contracts=read('field-contracts.json');byid={c['id']:c for c in contracts['contracts']}
 for c in contracts['contracts']:
  check(c['id']+'4atoms',len(c['atoms'])==4)
  for r in c['source']+c['spec']:ref(r)
 fwd=read('forward-mapping.json');records=fwd['records'];cache={};fields=0;omissions=0
 check('allmappedonce',len(records)==6712 and {v['section_id'] for v in records}==set(sec))
 for row in records:
  f,s=sec[row['section_id']];k=f['identity_id']
  if k not in cache:cache[k]=(REF/f['path']).read_text(encoding='utf-8-sig').splitlines()
  check(row['section_id']+'coordinates',[[x[0],x[1]] for x in row['fields']]==s['fields_line_key'])
  seen=set();om=set()
  for n,key,cid,digest,arity in row['fields']:
   raw=cache[k][n-1];v=raw.split('=',1)[1].strip() if '=' in raw else raw.strip()
   check(row['section_id']+str(n)+'binding',byid[cid]['key']==key and digest==hashlib.sha256(v.encode()).hexdigest() and arity>=1);seen.add(key);fields+=1
  for key,cid,disp,base in row['omitted']:
   check(row['section_id']+key+'omission',key not in seen and key not in om and byid[cid]['key']==key and (base is None or base in sec));om.add(key);omissions+=1
  check(row['section_id']+'base',row['kind']!='FORM' or row['base_section'] in sec)
 check('exactdenominators',fields==89067 and omissions==75313 and fwd['physical_field_denominator']==fields and fwd['omitted_dispositions']==omissions)
 atoms=read('reverse-mapping.json')['atomic_assertions'];check('212uniqueatoms',len(atoms)==212 and len({a['id'] for a in atoms})==212)
 for a in atoms:
  for r in a['source']+a['spec']:ref(r)
  check(a['id']+'mainpending',a['acceptance']=='PENDING_MAIN_REVIEWER')
 check('9plus3interfaces',len(read('interfaces.json')['interfaces'])==12 and read('interfaces.json')['accepted_interfaces']==0)
 check('noexecutionoracceptance',read('execution.json')['behavior_executions']==0 and led['counts']['accepted_primary_sections']==0 and not read('coverage.json')['NO_REQUIRED_UPDATE'])
 check('withdrawalretained',read('proposals.json')['records'][0]['local_disposition']=='WITHDRAWN_AS_NEW_REQUIRED_PROPOSAL_ALREADY_DOCUMENTED' and read('proposals.json')['records'][0]['independent_disproof']['state']=='PENDING_MAIN_REVIEWER')
 check('owncomplete/mainpending',read('progress.json')['semantic_status']=='OWNED_PRIMARY_AND_FINITE_MAPPING_DELIVERED' and not read('gaps.json')['primary_unread'])
 check('branch',git(SPEC,'branch','--show-current').decode().strip()=='codex/r8-external-pbs-creature-backups-20261016')
 check('Rclean',git(REF,'rev-parse','HEAD').decode().strip()==R and not git(REF,'status','--porcelain=v1','--untracked-files=all'))
 changes=git(SPEC,'diff','--name-only',B8).decode().splitlines()+git(SPEC,'ls-files','--others','--exclude-standard').decode().splitlines()+git(SPEC,'diff','--cached','--name-only').decode().splitlines()
 check('ownwriteonly',all(p.startswith(TASK+'/') for p in changes));check('formalunchanged',git(SPEC,'rev-parse','HEAD:deliverables/final-specification-set').decode().strip()=='f292698cdd4a8e725525a9be6dc34b75faaf151e')
 status='PASS_REPORT_INTEGRITY_ONLY'
except Exception as e:status='FAIL_REPORT_INTEGRITY';checks.append((repr(e),False))
result=dict(schema='r8-xpcb-final-validation/v2',start_utc=start,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status=status,check_count=len(checks),failed_checks=[n for n,c in checks if not c],successful_check_name_sha256=hashlib.sha256('\n'.join(n for n,c in checks if c).encode()).hexdigest(),semantic_credit_added=0,behavior_executions_added=0,acceptance_credit_added=0,limits='Coordinates/identity/partition/readrange consistency only; not engine behavior or independent semantic reception.')
(ROOT/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False));raise SystemExit(0 if status.startswith('PASS') else 1)
