"""Validate the bounded document candidate, without executing reference behavior."""
from pathlib import Path
import subprocess,json,hashlib,difflib,re,datetime,sys
ROOT=Path(__file__).resolve().parents[5]
PREFIX='review/remediation-eighth-20261016-prepare/candidates/R8-U01'
BASE='4575e80d041ab0c74a42e2e36399d05791dbaa5b'
E=ROOT/PREFIX/'evidence'; checks=[]
def check(name,condition,detail=None):
 checks.append({'name':name,'ok':bool(condition),'detail':detail})
def git(*args):return subprocess.check_output(['git','-C',str(ROOT),*args])
manifest=json.loads((E/'candidate-manifest.json').read_text())['files']
a=json.loads((ROOT/'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/batch-assignment.json').read_text())['batches'][0]
files=sorted(str(p.relative_to(ROOT)) for p in (ROOT/PREFIX/'mirror').rglob('*') if p.is_file())
check('exact_candidate_write_set',files==sorted(a['candidate_write_set']),{'count':len(files)})
check('independent_branch',git('branch','--show-current').decode().strip()=='revision/r8-u01-20261017')
check('fixed_input_is_ancestor',subprocess.run(['git','-C',str(ROOT),'merge-base','--is-ancestor',BASE,'HEAD']).returncode==0)
for x in manifest:
 target=x['target'];p=ROOT/x['candidate'];data=p.read_bytes();old=git('show',BASE+':'+target)
 check('candidate_identity:'+p.name,len(data)==x['bytes'] and hashlib.sha256(data).hexdigest()==x['sha256'] and git('hash-object',str(p)).decode().strip()==x['blob'])
 check('formal_unchanged:'+p.name,(ROOT/target).read_bytes()==old)
 check('B8_formal_baseline:'+p.name,old==git('show','fd1df570cad987dc3852a3b958f03916e317f7fe:'+target))
 ops=[op for op in difflib.SequenceMatcher(a=old.decode().splitlines(True),b=data.decode().splitlines(True),autojunk=False).get_opcodes() if op[0]!='equal']
 if p.name=='wp09-save-startup-continue.md':
  check('WP09_only_two_rule_lines',len(ops)==2 and all(o[0]=='replace' and o[2]-o[1]==o[4]-o[3]==1 for o in ops))
 elif p.name=='wp65-title-load-options-pause-and-pc.md':
  check('UI65_only_boot_and_refusal_lines',len(ops)==2 and all(o[0]=='replace' and o[2]-o[1]==o[4]-o[3]==1 for o in ops))
  check('UI65_existing_partial_failure_preserved','- **删除部分失败**：仅按「All saved data could not be deleted.」消息区分，不重试、不回滚。' in data.decode())
  check('UI65_refusal_clarity','（不调用持久层保存）' in data.decode() and '确认前/覆盖确认前发生的更改不回滚' in data.decode())
 elif p.name=='wp10-migration-failure-recovery.md':
  check('WP10_only_delete_failure_section',len(ops)==1 and ops[0][1:3]==(227,228))
  check('new_target_anchor_resolves','### 5.1.1 有序删除与下次载入门' in data.decode())
 else:
  check('catalog_all_previous_bytes_preserved',data.startswith(old))
  ids=re.findall(r'^\| (KER00[12]-[^ |]+) \|',data.decode(),re.M)
  expected=[v for rec in json.loads((E/'remediation-record.json').read_text())['records'][:2] for v in rec['vectors']]
  check('catalog_13_unique_new_rows',len(ids)==len(set(ids))==13 and set(ids)==set(expected),ids)
  check('catalog_no_executed_claim','SOURCE_STATIC / DERIVED_VECTOR，NOT_EXECUTED' in data.decode()[len(old.decode()):])
 proc=subprocess.run(['git','diff','--no-index','--check','--',str(ROOT/target),str(p)],capture_output=True,text=True)
 check('whitespace:'+p.name,proc.returncode in (0,1) and not (proc.stdout or proc.stderr),{'exit':proc.returncode,'stdout':proc.stdout,'stderr':proc.stderr})
 added='\n'.join(''.join(data.decode().splitlines(True)[o[3]:o[4]]) for o in ops)
 check('no_source_implementation_added:'+p.name,not re.search(r'(?m)^\s*(?:def |class |module |require |import |export )',added))
ledger=json.loads((E/'reading-ledger.json').read_text())
check('21_full_read_file_identities',len(ledger['source_spec_files'])==21 and all(x['identity_verified'] for x in ledger['source_spec_files']))
check('72_report_identity_and_purpose_checks',len(ledger['report_identity_checks'])==72 and all(x['identity_verified'] and x['recovered_verified'] is not False for x in ledger['report_identity_checks']))
for x in ledger['source_spec_files']:
 data=(Path(x['repo'])/x['path']).read_bytes()
 check('read_only_input_identity:'+x['path'],hashlib.sha256(data).hexdigest()==x['sha256'])
tracked=git('diff','--name-only',BASE).decode().splitlines()
untracked=git('ls-files','--others','--exclude-standard').decode().splitlines()
check('all_changes_exclusive_candidate',all(p.startswith(PREFIX+'/') for p in tracked+untracked),tracked+untracked)
check('reference_HEAD_fixed',subprocess.check_output(['git','-C','/workspace/pokemon-essentials','rev-parse','HEAD']).decode().strip()==ledger['reference_commit'])
result={'schema':'r8-u01-document-validation/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'level':'TOOL_VALIDATION','business_execution':'NOT_EXECUTED','formal_review':'NOT_PERFORMED','checks':checks,'passed':sum(x['ok'] for x in checks),'failed':sum(not x['ok'] for x in checks)}
(E/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'level':result['level'],'passed':result['passed'],'failed':result['failed'],'business_execution':'NOT_EXECUTED','failures':[x for x in checks if not x['ok']]},ensure_ascii=False))
sys.exit(bool(result['failed']))
