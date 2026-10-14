"""Immutable payload and contribution audit; no reference or behavior model runs."""
import collections, datetime, difflib, hashlib, json, pathlib, subprocess, sys

ROOT=pathlib.Path('/workspace/pokemon-essentials-clean-room')
OWN=pathlib.Path(__file__).resolve().parent
ACTUAL='86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
PREP='469a268b92daed7b4d28d7fd0da75520cbb7228f'
MAIN='8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
PREFIX='review/remediation-sixth-20261014-prepare/'
INPUT=PREFIX+'integration/U01-U14-final-composite-20261014/actual-review-input.json'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def payload(c,p):return git('show',c+':'+p)
def identity(c,p):
 d=payload(c,p); ent=git('ls-tree',c,'--',p).decode().strip().split(maxsplit=3)
 return dict(commit=c,path=p,mode=ent[0],type=ent[1],git_blob=ent[2],bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),lines=len(d.splitlines()))
def save(p,j): (OWN/p).write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
checks=[]
def check(name,ok,detail=None):checks.append(dict(name=name,PASS=bool(ok),detail=detail))
j=json.loads(payload(ACTUAL,INPUT)); batches=[b for b in j['batches'] if b['batch'] in ['R6-U02','R6-U04','R6-U05']]
paths=sorted({p for b in batches for p in b['all_candidate_allowlist_paths']})
check('actual_workspace_tree',git('rev-parse',ACTUAL+'^{tree}').decode().strip()=='67e8c55d520fa8cad2928cb4b95e24c3ed602d5a')
check('actual_formal_tree',git('rev-parse',ACTUAL+':deliverables/final-specification-set').decode().strip()=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c')
check('group_required_nine',sum(len(b['required_ids']) for b in batches)==9)
bindings=[]; changes=[]; diffs=[]
for b in batches:
 for c,p,want in [(ACTUAL,b['contract_path'],b['contract_identity']),(b['independent_review']['review_commit'],b['independent_review']['report_path'],b['independent_review']['report_identity'])]:
  got=identity(c,p);check('bound_input:'+p,all(got[k]==v for k,v in want.items()),got);bindings.append(got)
 check('contract_same_prepare:'+b['batch'],payload(ACTUAL,b['contract_path'])==payload(PREP,b['contract_path']))
for f in j['files']:
 if f['path'] not in paths:continue
 p=f['path'];got=identity(ACTUAL,p);bindings.append(got)
 check('actual_file:'+p,all(got[k]==v for k,v in f['actual'].items()) and got['mode']==f['mode'] and got['type']==f['type'])
 check('baseline_file:'+p,all(identity(MAIN,p)[k]==v for k,v in f['baseline'].items()))
 check('no_pending_writer:'+p,not f['pending_primary_writers'])
 base=payload(MAIN,p).decode().splitlines(keepends=True);actual=payload(ACTUAL,p).decode()
 for c in f['contributions']:
  cand=payload(c['candidate_commit'],c['candidate_path']).decode();ci=identity(c['candidate_commit'],c['candidate_path']);bindings.append(ci)
  check('candidate:'+c['batch']+':'+p,all(ci[k]==v for k,v in c['identity'].items()))
  lines=cand.splitlines(keepends=True)
  diffs.append(''.join(difflib.unified_diff(base,lines,fromfile='baseline/'+p,tofile=c['batch']+'/'+p,n=2)))
  for tag,i1,i2,k1,k2 in difflib.SequenceMatcher(None,base,lines,autojunk=False).get_opcodes():
   if tag=='equal':continue
   added=''.join(lines[k1:k2]);deleted=''.join(base[i1:i2])
   row=dict(batch=c['batch'],path=p,kind=tag,baseline_lines=[i1+1,i2],candidate_lines=[k1+1,k2],added=added,removed=deleted,added_block_present=(not added or added in actual),added_nonblank_lines_present=all(not s.strip() or s in actual for s in lines[k1:k2]))
   changes.append(row)
   check('contribution_lines:'+c['batch']+':'+p+':'+str(k1+1),row['added_nonblank_lines_present'])
 for family in ['S','B','SS','MA-T','HI10']:
  ids=[]; section=''
  for line in actual.splitlines():
   if line.startswith('## '):section=line
   if not line.startswith('| '):continue
   key=line.split('|')[1].strip()
   if key.startswith(family) and key not in ['Shadow','Sleep']:ids.append((section,key))
  if ids:check('raw_unique:'+p+':'+family,len(ids)==len(set(ids)),ids)
save('input-bindings.json',dict(actual_commit=ACTUAL,workspace_tree=git('rev-parse',ACTUAL+'^{tree}').decode().strip(),formal_tree=git('rev-parse',ACTUAL+':deliverables/final-specification-set').decode().strip(),input=identity(ACTUAL,INPUT),batches=batches,formal_paths=paths,bindings=bindings,administrative_sync=j['administrative_sync']))
save('contribution-preservation.json',dict(level='TOOL_PAYLOAD_ONLY_NOT_SEMANTIC_OR_RUNTIME_PROOF',changes=changes))
patch='\n'.join(diffs)
(OWN/'candidate-differences.patch').write_text(patch)
save('candidate-differences.patch.json',dict(format='Lossless JSON string of reviewed unified diff; raw working copy retained ignored, no deletion',raw_bytes=len(patch.encode()),raw_sha256=hashlib.sha256(patch.encode()).hexdigest(),raw_lines=len(patch.splitlines()),patch=patch))
save('static-verification.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),level='TOOL_PAYLOAD_ONLY',checks=checks,count=len(checks),failed=sum(not x['PASS'] for x in checks),new_reference_execution=0,new_model_execution=0,new_host_execution=0))
print(json.dumps(dict(count=len(checks),failed=[x for x in checks if not x['PASS']],formal_files=len(paths),contributions=len({(r['batch'],r['path']) for r in changes}),change_blocks=len(changes)),ensure_ascii=False))
sys.exit(1 if any(not x['PASS'] for x in checks) else 0)
