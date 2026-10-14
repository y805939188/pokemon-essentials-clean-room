"""Finite static identity, scope, preserved-clause and catalogue checks only."""
from pathlib import Path
import json,hashlib,re,subprocess,datetime,urllib.request,sys
ROOT=Path.cwd();P=Path('review/remediation-sixth-20261014-prepare');B=P/'candidates/R6-U01';E=B/'evidence';M=B/'mirror';BASE='469a268b92daed7b4d28d7fd0da75520cbb7228f';MAIN='8ea169fbd0f33f378b5d732fd6bea59e854e04a6';R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
ident=lambda b:{'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
git=lambda *args:subprocess.check_output(['git',*args]);checks=[]
def check(name,predicate,details):
 assert predicate,name
 checks.append({'check':name,'result':'PASS_TOOL_CHECK','scope':details})
c=json.loads((P/'contracts/R6-U01.json').read_text());f=json.loads((P/'inputs/frozen-inputs.json').read_text());reps=json.loads((E/'exact-replacements.json').read_text());new_paths=[];payloads=[];baseline_unchanged=[]
for path in c['candidate_formal_paths']:
 orig=git('show',MAIN+':'+path);prep=git('show',BASE+':'+str(M/path));candidate=(M/path).read_bytes();r=next(x for x in f['formal_materials'] if x['path']==path)
 check('frozen_formal_identity:'+path,all(ident(orig)[k]==r[k] for k in ident(orig)),ident(orig))
 check('prepare_mirror_is_baseline:'+path,orig==prep,'Exact fixed main bytes, not accepted remediation')
 replay=orig.decode()
 for rp in [x for x in reps if x['path']==str(M/path)]:
  check('replacement_unique:'+path+':'+str(len(checks)),replay.count(rp['old'])==1,'Bounded original text replaced once')
  replay=replay.replace(rp['old'],rp['new'])
 check('declared_change_replay:'+path,replay.encode()==candidate,'No undeclared candidate changes')
 if orig!=candidate:new_paths.append(str(M/path))
 else:baseline_unchanged.append(path)
 payloads.append({'formal_path':path,'candidate_path':str(M/path),'baseline':ident(orig),'candidate':ident(candidate),'changed':orig!=candidate,'mode':'100644','type':'blob'})
 check('protected_original:'+path,(ROOT/path).read_bytes()==orig,'Actual deliverables remains fixed main')
 # Existing complete table rows are invariant; new rows must not duplicate IDs.
 if '/test-catalog/' in path:
  rowid=lambda line:re.match(r'^\|\s*([A-Za-z][\w-]*\d)\s*\|',line)
  olds={rowid(x).group(1):x for x in orig.decode().splitlines() if rowid(x)}
  news=[(rowid(x).group(1),x) for x in candidate.decode().splitlines() if rowid(x)];ns=dict(news)
  check('catalogue_unique_ids:'+path,len(news)==len(ns),'All existing and new concrete table row IDs')
  check('all_historical_catalogue_rows_preserved:'+path,all(ns.get(k)==v for k,v in olds.items()),{'existing_row_count':len(olds),'new_row_count':len(news)-len(olds)})
expected=set(str(M/p) for p in c['candidate_formal_paths'] if 'wp27-bag' not in p and 'wp21-dynamic' not in p)
check('exact_seven_changed_mirrors',set(new_paths)==expected,new_paths)
changed=git('diff','--name-only',BASE).decode().splitlines();untracked=git('ls-files','--others','--exclude-standard').decode().splitlines()
check('complete_write_allowlist',all(p in expected or p.startswith(str(E)+'/') for p in changed+untracked),'No actual formal/shared ledger/other author/reference writes')
check('actual_formal_tree_preserved',git('diff','--quiet',MAIN,'--','deliverables/final-specification-set')==b'','All actual formal paths compare to fixed main')
# Validate remote R commit, tree and exact mode/blob for each source in this batch.
extra=json.loads((E/'additional-readset-registration.json').read_text())['additional_source_materials'];source_paths=c['read_only_reference_paths']+[x['path'] for x in extra]
# The GitHub REST endpoint returned proxy403; preserve that failed receipt.
# Normal fixed-object Git fetch succeeded into a separate scratch bare repository.
refgit=lambda *args:subprocess.check_output(['git','-C','/tmp/r6-u01-reference-objects.git',*args])
tree_sha=refgit('rev-parse',R+'^{tree}').decode().strip()
check('reference_commit_tree',refgit('rev-parse','FETCH_HEAD').decode().strip()==R and tree_sha==f['reference_tree'],'Actual fetched fixed commit/tree; no checkout or reference execution')
source_receipts=[]
for path in source_paths:
 row=next(x for x in f['source_materials'] if x['path']==path);raw=refgit('ls-tree',R,'--',path).decode().strip();meta=raw.split('\t',1)[0].split();entry={'mode':meta[0],'type':meta[1],'sha':meta[2]};b=(Path('/tmp/r6-u01-frozen/Maruno17/pokemon-essentials')/R/path).read_bytes()
 check('source_identity:'+path,all(ident(b)[k]==row[k] for k in ident(b)) and entry['sha']==row['git_blob'] and entry['type']=='blob' and entry['mode']==row['mode'],{'commit':R,'tree':tree_sha,'path':path,**ident(b),'mode':entry['mode'],'type':entry['type']})
 source_receipts.append({'commit':R,'tree':tree_sha,'path':path,**ident(b),'mode':entry['mode'],'type':entry['type']})
# SHELLOS positive complete record and focused negative evolution/registry scope.
rroot=Path('/tmp/r6-u01-frozen/Maruno17/pokemon-essentials')/R
pbs=(rroot/'PBS/pokemon.txt').read_text(encoding='utf-8-sig');forms=(rroot/'PBS/pokemon_forms.txt').read_text(encoding='utf-8-sig');shell=re.search(r'^\[SHELLOS\]\n(.*?)(?=^\[|\Z)',pbs,re.M|re.S).group(1)
check('Shellos_record',all(x in shell for x in ['HatchSteps = 5120','Flags = InheritFormFromMother','FormName = West Sea']) and 'DefaultForm_' not in shell and 'Offspring =' not in shell,'Fixed complete default record, not compiled/runtime data load')
targets=[]
for name,t in [('PBS/pokemon.txt',pbs),('PBS/pokemon_forms.txt',forms)]:
 for n,line in enumerate(t.splitlines(),1):
  if re.match(r'^Evolutions?\s*=',line) and re.search(r'\bSHELLOS\b',line):targets.append([name,n,line])
check('focused_Shellos_predecessor_target_search',not targets,{'scope':'Evolution field lines in two fixed default species PBS files','matches':targets,'not_full_semantic_PBS_read':True})
handlers=(rroot/'Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb').read_text();check('Shellos_default_handler_absence','SHELLOS' not in handlers,'Full registry was semantically read; excludes plugin/dynamic registration')
# Changed prose links resolve against overlay plus fixed baseline; finite file existence check.
for path in new_paths:
 p=Path(path);txt=p.read_text()
 for target in re.findall(r'\]\(([^)]+)\)',txt):
  if '://' in target or target.startswith('#'):continue
  fragment=target.partition('#');candidate=(p.parent/fragment[0]).resolve();rel=candidate.relative_to((ROOT/M).resolve())
  check('link_file:'+str(p)+':'+target,candidate.exists() or (ROOT/rel).exists(),'Candidate overlay file or protected fixed main target exists')
check('source_free_new_specification',all('Data/Scripts/' not in x['new'] and 'def ' not in x['new'] and 'class ' not in x['new'] for x in reps),'No source snippets, engine/framework implementation or class design in new formal text')
check('no_self_signed_review',not (E/'independent-review.json').exists(),'Independent ultra author-external review remains pending')
# Exact untouched clauses for original R1 / R2 / R3 / R4 / R5 consumers.
spans={'creature-rpg/wp18-creature-identity-species-ownership.md':[(47,101),(135,239),(248,253),(255,340),(348,349)],'generic-kernel/wp10-migration-failure-recovery.md':[(21,77),(84,87),(89,209)],'pokemon-rules/wp34-inheritance-and-offspring.md':[(22,99),(103,150),(152,175),(177,211)],'pokemon-rules/wp62-pokedex-records-regions-and-content.md':[(11,41),(44,44),(52,60),(64,172)]}
span_receipts=[]
for suffix,ranges in spans.items():
 path='deliverables/final-specification-set/'+suffix;orig=git('show',MAIN+':'+path).decode().splitlines(keepends=True);current=(M/path).read_text()
 for lo,hi in ranges:
  content=''.join(orig[lo-1:hi]);check('preserved_baseline_span:'+path+f':{lo}-{hi}',content in current,'Exact original bytes within candidate, no historical PASS transfer')
  span_receipts.append({'path':path,'baseline_commit':MAIN,'baseline_lines':[lo,hi],'sha256':hashlib.sha256(content.encode()).hexdigest(),'bytes':len(content.encode()),'candidate_contains_identical_span':True})
(E/'candidate-payload-identities.json').write_text(json.dumps(payloads,ensure_ascii=False,indent=2)+'\n');(E/'source-payload-identities.json').write_text(json.dumps(source_receipts,ensure_ascii=False,indent=2)+'\n');(E/'historical-span-preservation.json').write_text(json.dumps(span_receipts,ensure_ascii=False,indent=2)+'\n')
receipt={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'evidence_level':'TOOL_VALIDATION','result':'AUTHOR_STATIC_TOOL_CHECKS_PASS','behavior_execution':0,'host_execution':0,'independent_review':'PENDING_NONAUTHOR_ULTRA','checks':checks,'changed_mirrors':new_paths,'preserved_baseline_mirrors':baseline_unchanged}
(E/'validation.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'checks':len(checks),'result':receipt['result'],'changed_mirrors':len(new_paths),'preserved_baseline_mirrors':baseline_unchanged,'reference_execution':0},ensure_ascii=False))
