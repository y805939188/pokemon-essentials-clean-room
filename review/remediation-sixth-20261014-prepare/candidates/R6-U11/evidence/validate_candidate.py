"""Validate finite artifact identity, scope and preserved text; no behavior model/source evaluation."""
from pathlib import Path
import json,subprocess,hashlib,difflib,sys,datetime
root=Path.cwd();prepare=Path('review/remediation-sixth-20261014-prepare');owned=prepare/'candidates/R6-U11';ev=owned/'evidence'
fixed='469a268b92daed7b4d28d7fd0da75520cbb7228f';formal='8ea169fbd0f33f378b5d732fd6bea59e854e04a6';ref='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
contract=json.loads((prepare/'contracts/R6-U11.json').read_text());paths=contract['candidate_formal_paths']
def git(*a):return subprocess.check_output(['git',*a])
def digest(b):return hashlib.sha256(b).hexdigest()
def clause(s,start,end):return s.split(start,1)[1].split(end,1)[0]
assert git('branch','--show-current').decode().strip()=='codex/remediation-sixth-r6-u11-author-20261014'
changed=git('diff','--name-only',fixed).decode().splitlines();others=git('ls-files','--others','--exclude-standard').decode().splitlines()
allowed={str(owned/'mirror'/p) for p in paths}
assert all(p in allowed or p.startswith(str(ev)+'/') for p in changed+others),(changed,others)
assert not git('diff',fixed,'--','deliverables','audit','planning','reference')
files=[];texts={};oldtexts={}
for p in paths:
 q=owned/'mirror'/p;b=q.read_bytes();old=git('show',fixed+':'+str(q));frozen=git('show',formal+':'+p);assert old==frozen;assert b!=old;assert b.endswith(b'\n') and b'\r' not in b
 texts[p]=b.decode();oldtexts[p]=old.decode();assert '\n```ruby' not in texts[p] and '\n```typescript' not in texts[p]
 a=old.decode().splitlines();z=b.decode().splitlines();ops=[{'kind':tag,'baseline_lines':[i+1,j],'candidate_lines':[k+1,l]} for tag,i,j,k,l in difflib.SequenceMatcher(a=a,b=z,autojunk=False).get_opcodes() if tag!='equal']
 files.append({'path':str(q),'formal_path':p,'bytes':len(b),'sha256':digest(b),'git_blob':git('hash-object',str(q)).decode().strip(),'mode':'100644','type':'text','baseline_bytes':len(old),'baseline_sha256':digest(old),'delta':ops})
# Every original vector/table row remains exact and in order in the catalogs.
rowchecks=[]
for p in paths:
 if '/test-catalog/' not in p:continue
 oldrows=[x for x in oldtexts[p].splitlines() if x.startswith('|')];newrows=[x for x in texts[p].splitlines() if x.startswith('|')]
 cursor=0
 for row in oldrows:
  while cursor<len(newrows) and newrows[cursor]!=row:cursor+=1
  assert cursor<len(newrows),(p,row)
  cursor+=1
 rowchecks.append({'path':p,'old_table_rows':len(oldrows),'all_original_rows_byte_equal_in_original_order':True})
wp=paths[3];pd=paths[0];ut=paths[2];pt=paths[1]
protected=[]
for p,start,end in [(wp,'### 6.2 搜索','## 7. 图鉴'),(wp,'### 7.1 三页与翻页','### 7.2 可列形态'),(wp,'### 3.2 暂持','## 4. 盒子'),(wp,'### 4.4 退出与确认','## 5. 图鉴'),(pd,'### 3.4 逐入口契约','## 4. 身份'),(pd,'### 5.3 区域与地图数据','## 6. 展示')]:
 old=clause(oldtexts[p],start,end);new=clause(texts[p],start,end);assert old==new;protected.append({'path':p,'clause_start':start,'clause_end':end,'sha256':digest(old.encode()),'byte_equal':True})
start='可列形态计算：';old=oldtexts[wp].split(start,1)[1].split('\n\n',1)[0];new=texts[wp].split(start,1)[1].split('\n\n',1)[0];assert old==new
protected.append({'path':wp,'clause':'§7.2完整资格/结构/两性/标签段','sha256':digest(old.encode()),'byte_equal':True})
for p,prefix,n in [(ut,'R6-BX',11),(ut,'R6-DX',4),(pt,'R6-PD',3)]:
 for i in range(1,n+1):assert texts[p].count('| '+prefix+str(i).zfill(2)+' |')==1
# Range coverage proves only delivery/completeness, not meaning.
ledger=[json.loads(x) for x in (ev/'reading-ledger.jsonl').read_text().splitlines()];early=json.loads((ev/'early-reading-and-attempts.json').read_text())['early_complete_reads'];coverage=[]
for commit,p,n in [(ref,'Data/Scripts/016_UI/017_UI_PokemonStorage.rb',2022),(ref,'Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb',619),(ref,'Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb',361),(ref,'Data/Scripts/016_UI/003_UI_Pokedex_Main.rb',1302)]+[(formal,p,len(oldtexts[p].splitlines())) for p in paths]:
 ranges=[x['range'] for x in ledger if x.get('commit')==commit and x.get('path')==p and 'range' in x]
 ranges += [r for x in early if x.get('commit')==commit and x.get('path')==p for r in x['ranges']]
 covered=set(v for lo,hi in ranges for v in range(lo,hi+1));assert set(range(1,n+1))<=covered
 coverage.append({'commit':commit,'path':p,'lines':n,'ranges':ranges,'complete_range_delivery':True,'not_automatic_semantic_PASS':True})
for x in ledger:
 if x.get('commit')==ref:
  b=git('show',ref+':'+x['path']);assert len(b)==x['bytes'] and digest(b)==x['sha256']
check=subprocess.run(['git','diff','--check'],capture_output=True);assert check.returncode==0,check.stderr.decode()+check.stdout.decode()
result={'evidence_level':'TOOL_VALIDATION','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cwd':str(root),'runtime':sys.version,'files':files,'old_catalog_rows':rowchecks,'preserved_clauses':protected,'complete_primary_read_ranges':coverage,'changed_paths':changed,'untracked_paths_at_check':others,'git_diff_check':{'exit':check.returncode,'stdout':check.stdout.decode(),'stderr':check.stderr.decode()},'all_path_writes_within_allowlist':True,'formal_public_ledger_reference_unmodified':True,'new_reference_model_host_Demo_save_executions':0,'candidate_non_author_review':'PENDING','formal_acceptance':'NOT_PERFORMED','CLOSED':'NOT_REGISTERED'}
(ev/'tool-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result':'ARTIFACT_CHECKS_OK_NOT_BEHAVIOR_EXECUTION','changed_mirror_files':4,'old_table_rows_preserved':sum(x['old_table_rows'] for x in rowchecks),'primary_full_reads':len(coverage),'ui_rows':15,'domain_mirrors':3,'reference_executions':0,'independent_review':'PENDING'},ensure_ascii=False))
