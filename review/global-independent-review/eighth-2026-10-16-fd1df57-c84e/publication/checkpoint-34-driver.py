"""Authorized C34 report-only publication; freezes bytes, never changes semantics."""
from pathlib import Path
import concurrent.futures,datetime,hashlib,json,os,stat,subprocess,sys
REPO=Path('/workspace/pokemon-essentials-clean-room')
RR=REPO/'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
PUB=RR/'publication';IO=PUB/'checkpoint-34-io';IO.mkdir(exist_ok=True)
PREFIX=str(RR.relative_to(REPO))+'/'
HEAD='c7fec918d511a0ead8ab325c934e9346d7c43cac'
BRANCH='codex/review-eighth-20261016-fd1df57-c84e'
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def put(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
events=[]
def run(args,label,stdin=None):
 a=utc();q=subprocess.run(args,cwd=REPO,input=stdin,capture_output=True);z=utc()
 (IO/(label+'.stdout')).write_bytes(q.stdout);(IO/(label+'.stderr')).write_bytes(q.stderr)
 e={'args':args,'start_utc':a,'end_utc':z,'exit':q.returncode,'stdout':'publication/checkpoint-34-io/'+label+'.stdout','stderr':'publication/checkpoint-34-io/'+label+'.stderr','stdout_bytes':len(q.stdout),'stdout_sha256':sha(q.stdout),'stderr_bytes':len(q.stderr),'stderr_sha256':sha(q.stderr)}
 put(IO/(label+'.operation.json'),e);events.append(e);assert q.returncode==0,e
 return q.stdout
def git(*args,label):return run(['git','-C',str(REPO),*args],label)
def guard(label):
 assert git('rev-parse','HEAD',label=label+'-head').decode().strip()==HEAD
 assert git('branch','--show-current',label=label+'-branch').decode().strip()==BRANCH
 assert not git('diff','--cached','--name-only','-z',label=label+'-index')

def prepare():
 guard('initial-guard')
 old=json.loads((PUB/'preflight-before-checkpoint-33.json').read_bytes())
 args=[e['args'] for e in old['events']];assert len(args)==9
 with concurrent.futures.ThreadPoolExecutor(max_workers=9) as ex:
  results=list(ex.map(lambda x:run(x[1],f'preflight-{x[0]+1:02d}'),enumerate(args)))
 assert results[0].decode().strip()==BRANCH
 assert results[1].decode().strip()=='751dfde81048c81390f89a65ca1d1a565ba8e1ca'
 assert results[2].decode().strip()=='f292698cdd4a8e725525a9be6dc34b75faaf151e'
 delta=[x.decode() for x in results[3].split(b'\0') if x];assert all(x.startswith(PREFIX) for x in delta)
 statuses=[x for x in results[4].split(b'\0') if x];assert all(x[3:].decode().startswith(PREFIX) for x in statuses)
 assert results[5].decode().strip()=='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
 assert results[6].decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0'
 assert not results[7]
 refs=results[8].decode().splitlines();assert len(refs)==2 and all(x.startswith('fd1df570cad987dc3852a3b958f03916e317f7fe\t') for x in refs)
 preflight={'schema':'gr8-checkpoint34-protected-input-preflight/v1','utc':utc(),'status':'PASS9','events':[json.loads((IO/f'preflight-{i+1:02d}.operation.json').read_bytes()) for i in range(9)],'report_only_tracked_delta_count':len(delta),'worktree_status_record_count':len(statuses),'protected_path_differences':[],'all_report_only':True,'semantic_credit':'NONE','UPDATE_NOT_STARTED':True}
 put(PUB/'checkpoint-34-preflight.json',preflight)
 registry=json.loads((RR/'adjudication/root-primary-task-final-registry.v1.json').read_bytes());assert registry['count']==len(registry['accepted'])==27
 for x in registry['accepted']:
  raw=(RR/x['receipt']['path']).read_bytes();assert len(raw)==x['receipt']['bytes'] and sha(raw)==x['receipt']['sha256']
 caches=[('receive_external_com_battler','d1e713ccd22454a2039a16c615ffb578f2646a8f',160),('receive_external_h_early_qualifications','4dd33cacb54cdf1a95a9a6c5ce053082d71b12e7',491),('receive_external_legacy_manifest_currentness','b5ed789c44dcd78eec891871ba9716dbd8009f1a',255),('receive_external_localization_records','3f7971a430ec87af7decd149b0b32caad53a5884',496),('recovery_ability01','271b422246567f089c2cf118f6a9426534d0f67d',13),('external_ability_atomic_completion','374337a82c0ce7ac6306534d9061a6ba4132c15e',26),('ability_cont_02','5c1e9a4679f66f4f1a6a8fb85c21335dd46eb0b1',17),('ability_cont_03','1395d861b6f3043c13da4619de0dd3f6bfe78d47',13)]
 cache_scopes=[];pub_allowed={'publication/r8-qualified-primary21-and-recoveries-readback-33.json','publication/checkpoint-33-root-push-receipt.json','publication/cli-startup-capability-checks.v1.json','publication/recover-independent-task-checkpoint.v2.py','publication/recover-independent-task-checkpoint.v3.py'}
 for group,c,n in caches:
  p=RR/'evidence/external-recovered'/group/c;fs=[x for x in p.rglob('*') if x.is_file()];assert len(fs)==n,(group,len(fs),n)
  cache_scopes.append(str(p.relative_to(RR))+'/')
  proof='publication/external-'+group+'-'+c[:8]+'-recovery.json';assert (RR/proof).is_file();pub_allowed.add(proof)
 scopes=['adjudication/','tasks/creature_b/','tasks/reference_metadata_completion/','tasks/reference_metadata/root-completion/','tasks/com_move/integration-membership/']+cache_scopes
 comp=json.loads((PUB/'compressed-artifacts.json').read_bytes())['artifacts'];assert len(comp)==116
 cmap={x['original_path']:x for x in comp};materialized=[]
 for e in comp:
  p=RR/e['original_path']
  if p.exists():
   assert p.is_file() and not p.is_symlink();raw=p.read_bytes()
   materialized.append({'path':e['original_path'],'bytes':len(raw),'sha256':sha(raw),'matches_published_compressed_original':len(raw)==e['original_bytes'] and sha(raw)==e['original_sha256']})
  container=RR/e['container_path'];assert container.is_file()
 changed=set(x.decode() for x in git('diff','--name-only','-z',label='candidate-tracked-changes').split(b'\0') if x)
 changed.update(x.decode() for x in git('ls-files','--others','--exclude-standard','-z',label='candidate-untracked-changes').split(b'\0') if x)
 rows=[];excluded=[];formats=[];hash_events=[]
 def select(path):
  if not path.startswith(PREFIX):return False
  rel=path[len(PREFIX):]
  if any(s.endswith('.git') for s in Path(rel).parts) or 'tmp_pack_'in rel or '__pycache__'in Path(rel).parts or rel.endswith(('.pyc','.tmp')):return False
  if rel.startswith('publication/checkpoint-34-io/'):return False
  return any(rel.startswith(s) for s in scopes) or rel in pub_allowed or rel in ['publication/checkpoint-34-driver.py','publication/checkpoint-34-preflight.json']
 for path in sorted(changed):
  if not select(path):excluded.append({'path':path,'reason':'OUTSIDE_EXACT_COMPLETED_ALLOWLIST_OR_TEMP_FILTER'});continue
  p=REPO/path;st=p.lstat();assert stat.S_ISREG(st.st_mode) and not p.is_symlink();raw=p.read_bytes()
  rel=path[len(PREFIX):]
  if rel in cmap:
   e=cmap[rel]
   if len(raw)==e['original_bytes'] and sha(raw)==e['original_sha256']:
    excluded.append({'path':path,'reason':'EXACT_PUBLISHED_GZIP_ORIGINAL_BYTES_AND_SHA_MATCH','bytes':len(raw),'sha256':sha(raw)});continue
  assert len(raw)<100000000
  fmt='RAW_BYTES_NOT_JSON'
  if p.suffix in ['.json','.jsonl','.ndjson']:
   try:
    if p.suffix in ['.jsonl','.ndjson']:raise ValueError('EXPLICIT_LINE_FORMAT')
    json.loads(raw);fmt='WHOLE_JSON_PARSED_MECHANICALLY'
   except (json.JSONDecodeError,UnicodeDecodeError,ValueError) as err:
    lines=[x for x in raw.splitlines() if x.strip()]
    try:
     assert lines
     for line in lines:json.loads(line)
     fmt='EXPLICIT_NDJSON_ALL_NONEMPTY_LINES_PARSED'
     formats.append({'path':path,'format':fmt,'original_whole_json_exception':str(err),'nonempty_lines':len(lines)})
    except Exception as err2:
     fmt='RAW_ORIGINAL_JSON_PARSE_ANOMALY_PRESERVED_NOT_JSON_PASS';formats.append({'path':path,'format':fmt,'whole_json_exception':str(err),'line_parse_exception':str(err2)})
  oid=blob(raw);a=utc();q=subprocess.run(['git','-C',str(REPO),'hash-object','-w','--stdin'],input=raw,capture_output=True);b=utc();assert q.returncode==0 and q.stdout.decode().strip()==oid
  hash_events.append({'path':path,'args':['git','-C',str(REPO),'hash-object','-w','--stdin'],'start_utc':a,'end_utc':b,'exit':q.returncode,'stdin_bytes':len(raw),'stdin_sha256':sha(raw),'stdout':q.stdout.decode(),'stderr':q.stderr.decode()})
  assert raw==p.read_bytes(),('changed_during_freeze',path)
  rows.append({'path':path,'mode':'100644','type':'blob','blob':oid,'bytes':len(raw),'sha256':sha(raw),'actual_filesystem_mode':oct(stat.S_IMODE(st.st_mode)),'format':fmt})
 put(IO/'freeze-hash-object-events.json',{'events':hash_events,'semantic_credit':'NONE'})
 guard('freeze-final-guard')
 ready={'schema':'gr8-checkpoint34-frozen-status/v1','utc':utc(),'state':'FROZEN_COMPLETED_EVIDENCE_ONLY_NOT_YET_COMMITTED','HEAD_guard':HEAD,'branch':BRANCH,'root_registry_count':27,'local_actual_contexts':61,'external_actual_contexts':64,'known_actual_contexts':125,'new_contexts':0,'new_independent_votes':0,'review_state':'ACTIVE','UPDATE_NOT_STARTED':True,'whole_required':None,'whole_global_history_canonical':'UNFROZEN','whole_review_complete':False,'selected_files_before_selection_envelope':len(rows),'selected_bytes':sum(x['bytes'] for x in rows),'excluded_live_handoff':True,'old_c699_ELR_duplicate_cache_excluded':True,'root_post_freeze_writes_excluded':True}
 put(PUB/'checkpoint-34-status.json',ready)
 for extra in [PUB/'checkpoint-34-status.json']+sorted(x for x in IO.iterdir() if x.is_file()):
  raw=extra.read_bytes();oid=blob(raw);q=subprocess.run(['git','-C',str(REPO),'hash-object','-w','--stdin'],input=raw,capture_output=True);assert q.returncode==0 and q.stdout.decode().strip()==oid
  assert len(raw)<100000000
  if extra.suffix=='.json':json.loads(raw)
  rows.append({'path':str(extra.relative_to(REPO)),'mode':'100644','type':'blob','blob':oid,'bytes':len(raw),'sha256':sha(raw),'format':'WHOLE_JSON_PARSED_MECHANICALLY' if extra.suffix=='.json' else 'RAW_COMMAND_IO_BYTES'})
 frozen={'schema':'gr8-checkpoint34-exact-frozen-candidates/v1','utc':utc(),'baseline_HEAD':HEAD,'branch':BRANCH,'root_registry_count':27,'files':rows,'count':len(rows),'bytes':sum(x['bytes'] for x in rows),'selected_cache_roots':cache_scopes,'selected_publication_exact_allowlist':sorted(pub_allowed),'format_qualifications':formats,'all_original_compressed_map_entries':116,'materialized_original_identity_checks':materialized,'excluded':excluded,'own_manifest_envelope':'publication/checkpoint-34-candidates.json will be added by exact preannouncedSHA; no self-hash recursion','post_freeze_live_writes':'NOT_SELECTED; index will use frozen Git blobs only','review_status':'ACTIVE_UPDATE_NOT_STARTED','whole_required':None,'whole_history_canonical':'UNFROZEN','semantic_credit':'NONE added by publication'}
 put(PUB/'checkpoint-34-candidates.json',frozen)
 raw=(PUB/'checkpoint-34-candidates.json').read_bytes()
 print(json.dumps({'status':'FROZEN','HEAD':HEAD,'branch':BRANCH,'count':len(rows),'bytes':frozen['bytes'],'candidate_path':'publication/checkpoint-34-candidates.json','candidate_bytes':len(raw),'candidate_sha256':sha(raw),'preflight':'PASS9','registry':27,'format_qualifications':len(formats),'raw_json_parse_anomalies':sum(x['format'].startswith('RAW_') for x in formats),'materialized_originals':len(materialized),'materialized_exact_matches':sum(x['matches_published_compressed_original'] for x in materialized)},ensure_ascii=False))

if __name__=='__main__':
 assert sys.argv[1:]==['prepare']
 prepare()
