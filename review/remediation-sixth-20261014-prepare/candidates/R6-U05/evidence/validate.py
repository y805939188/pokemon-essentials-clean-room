#!/usr/bin/env python3
"""Finite text, identity, preservation and scope checks; no reference execution."""
from pathlib import Path
import json,hashlib,subprocess,re,difflib,datetime
E=Path(__file__).resolve().parent
R=E.parents[2]
REPO=R.parents[1]
C=json.loads((R/'contracts/R6-U05.json').read_text())
PREP='469a268b92daed7b4d28d7fd0da75520cbb7228f'
MAIN=C['frozen_main']
M=E.parent/'mirror'
def identity(b):
 return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def git(*args):return subprocess.check_output(['git',*args],cwd=REPO)
checks=[]
def check(name,condition,detail=None):
 checks.append({'name':name,'result':'PASS' if condition else 'FAIL','detail':detail})
 assert condition,(name,detail)
p=(R/'prompts/R6-U05-A.md').read_bytes()
check('exact_prompt_identity',identity(p)=={'bytes':269810,'sha256':'41f463ab3a9ce1bc72161ddb4d6e459027f9d560fba3a566d8ade48c58898ac2','git_blob':'fbd9c97051e58dfeb5bf828cda6e4fde4e22840d'})
check('author_branch',git('branch','--show-current').decode().strip()=='codex/remediation-sixth-r6-u05-author-20261014')
changes=json.loads((E/'edits.json').read_text())+json.loads((E/'refinement.json').read_text())
restored={p:(M/p).read_text() for p in C['candidate_formal_paths']}
for change in reversed(changes):
 p='deliverables/final-specification-set/'+change['path']
 if 'append' in change:
  check('exact_append_suffix:'+change['path'],restored[p].endswith(change['append']))
  restored[p]=restored[p][:-len(change['append'])]
 else:
  check('exact_edit_uniqueness:'+change['path'],restored[p].count(change['new'])==1)
  restored[p]=restored[p].replace(change['new'],change['old'])
files=[]
for p in C['candidate_formal_paths']:
 old=git('cat-file','blob',MAIN+':'+p)
 now=(M/p).read_bytes()
 check('formal_untouched:'+p,(REPO/p).read_bytes()==old)
 check('all_differences_declared:'+p,restored[p].encode()==old)
 check('baseline_is_prepare_original:'+p,git('cat-file','blob',PREP+':'+str((M/p).relative_to(REPO)))==old)
 check('text_and_no_source_code:'+p,b'\0' not in now and '```ruby' not in now.decode() and 'class Battle::' not in now.decode())
 opcodes=difflib.SequenceMatcher(a=old.decode().splitlines(),b=now.decode().splitlines(),autojunk=False).get_opcodes()
 spans=[{'operation':tag,'baseline_lines':[a+1,b],'candidate_lines':[c+1,d]} for tag,a,b,c,d in opcodes if tag!='equal']
 files.append({'formal_path':p,'candidate_path':str((M/p).relative_to(REPO)),'baseline':identity(old),'candidate':identity(now),'mode':'100644','type':'text','changed_spans':spans})
 for target in re.findall(r'\]\(([^)]+)\)',now.decode()):
  if '://' in target or target.startswith('#'):continue
  path=target.split('#')[0]
  resolved=(REPO/p).parent/path
  check('existing_markdown_link:'+p+':'+target,resolved.exists())
for p in C['candidate_formal_paths']:
 if '/test-catalog/' not in p:continue
 old=git('cat-file','blob',MAIN+':'+p).decode().splitlines()
 now=(M/p).read_text().splitlines()
 oldrows=[x for x in old if x.startswith('|')]
 check('every_original_test_row_preserved:'+p,all(x in now for x in oldrows),len(oldrows))
 for x in oldrows:
  check('original_test_row_count:'+p,now.count(x)>=old.count(x))
 newids=[x.split('|')[1].strip() for x in now if re.match(r'^\| MA-T1[1-6] \|',x) or re.match(r'^\| SS(?:4[3-9]|5[0-9]) \|',x)]
 expected=['MA-T'+str(i) for i in range(11,17)] if 'wp47-ab' in p else ['SS'+str(i) for i in range(43,60)]
 check('new_vector_ids:'+p,newids==expected,expected)
history=[]
for row in json.loads((E/'historical-relations.json').read_text())['relations']:
 p=row['formal_path'];a,b=row['formal_lines'];old=git('cat-file','blob',MAIN+':'+p).decode().splitlines();now=(M/p).read_text().splitlines();text='\n'.join(old[a-1:b]);status='EXACT_UNCHANGED_CONTIGUOUS_SPAN'
 if text not in '\n'.join(now):
  # The one Sleep Talk paragraph gains a bounded consumer sentence; existing wording is preserved.
  oldpara=old[180]
  added='候选可为精神转移；外壳真睡眠检查后仍睡且其它门通过时，内层能到达 WP44 §6 的通用异常资格，专用睡眠/冰冻条款门不因此补跑。'
  stripped='\n'.join(now).replace(added,'')
  check('historical_existing_scope_preserved:'+row['historical_scope_consumer'],text in stripped,{'path':p,'lines':[a,b]})
  status='EXISTING_SCOPE_VERBATIM_PRESERVED_WITH_BOUNDED_NEW_CONSUMER_SENTENCE'
 history.append({**row,'baseline_span_sha256':hashlib.sha256(text.encode()).hexdigest(),'new_check':status,'new_semantic_verdict':'AUTHOR_FINITE_PRESERVATION_ONLY_NOT_INDEPENDENT_PASS'})
check('charge_math_and_random_thresholds',101//2==50 and 101-101//2==51 and 5<10 and not 99<10,'Constant arithmetic only; not behavior/model execution')
inputs=json.loads((R/'inputs/frozen-inputs.json').read_text())
for rec in [json.loads(x) for x in (E/'reading-ledger.jsonl').read_text().splitlines()]:
 if rec['kind']=='source':
  p=Path('/tmp/r6-u05-frozen/Maruno17/pokemon-essentials')/C['frozen_reference']/rec['path']
  check('read_source_still_fixed:'+rec['path'],identity(p.read_bytes())==rec['identity'])
actual_changed=git('diff','--name-only',PREP).decode().splitlines()
allowed={x['candidate_path'] for x in files}
check('tracked_write_allowlist',set(actual_changed)<=allowed,actual_changed)
untracked=git('ls-files','--others','--exclude-standard').decode().splitlines()
check('untracked_write_allowlist',all(p.startswith(str(E.relative_to(REPO))+'/') for p in untracked),untracked)
check('diff_whitespace',subprocess.run(['git','diff','--check'],cwd=REPO,capture_output=True).returncode==0)
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'level':'TOOL_VALIDATION','result':'PASS_FINITE_STATIC_IDENTITY_PRESERVATION_SCOPE_CHECKS','checks':checks,'candidate_files':files,'historical_span_checks':history,'execution':{'isolated_reference':0,'independent_behavior_model':0,'host_demo':0,'real_save_network_production_services':0},'independent_review':'PENDING_NON_AUTHOR'}
(E/'validation-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result':result['result'],'checks':len(checks),'candidate_files':len(files),'old_qualified_relations_preserved':len(history),'new_vectors':23,'reference_model_host_execution':0},ensure_ascii=False))
