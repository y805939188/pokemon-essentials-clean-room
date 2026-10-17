"""Static document/package validation only. Never executes reference Ruby or a game model."""
from pathlib import Path
from collections import Counter
from fractions import Fraction
import datetime,hashlib,json,re,subprocess,sys
P=Path(__file__).resolve().parents[5];C=Path(__file__).resolve().parents[1];E=C/'evidence';M=C/'mirror';BASE='4575e80d041ab0c74a42e2e36399d05791dbaa5b';R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';B='deliverables/final-specification-set/';RR='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e';checks=[]
def record(label,passed,details):
 checks.append({'check':label,'passed':bool(passed),'details':details});assert passed,(label,details)
def run(args,repo=P):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(args,cwd=repo,text=True,capture_output=True);end=datetime.datetime.now(datetime.timezone.utc).isoformat()
 with (E/'commands.jsonl').open('a') as f:f.write(json.dumps({'start_utc':start,'end_utc':end,'cwd':str(repo),'argv':args,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'credit':'TOOL_VALIDATION only; not reference behavior execution'},ensure_ascii=False)+'\n')
 assert r.returncode==0,(args,r.stderr);return r.stdout.strip()
branch=run(['git','branch','--show-current']);record('independent branch',branch=='codex/r8-u06-revision-20261017',branch)
run(['git','merge-base','--is-ancestor',BASE,'HEAD'])
formal=run(['git','rev-parse','HEAD:'+B.rstrip('/')]);record('formal tree unchanged at checkout HEAD',formal=='f292698cdd4a8e725525a9be6dc34b75faaf151e',formal)
record('reference fixed HEAD',run(['git','rev-parse','HEAD'],Path('/workspace/pokemon-essentials'))==R,R)
record('reference worktree unchanged',run(['git','status','--porcelain'],Path('/workspace/pokemon-essentials'))=='','')
record('formal working files unchanged',run(['git','diff',BASE,'--',B])=='','entire formal tree diff empty')
a=json.loads((P/RR/'handoff/batch-assignment.json').read_text());batch=next(x for x in a['batches'] if x['id']=='R8-U06')
# The candidate manifest is authoritative for the frozen 12-file payload.
m=json.loads((E/'candidate-files.json').read_text());manifest=m['files'];expected={x['candidate'] for x in manifest};actual={p.relative_to(C).as_posix() for p in M.rglob('*') if p.is_file()};record('mirror exact file set',actual==expected,{'expected':len(expected),'actual':len(actual)})
authorized={'mirror/'+p for p in batch['actual_target_write_set']}|{'mirror/'+B+'combat-requirements/wp58-battle-recording-and-playback.md'}
record('contract write set plus selected F05',actual==authorized,{'extra':sorted(actual-authorized),'missing':sorted(authorized-actual)})
record('12 files including authorized F05 WP58',len(actual)==12 and 'mirror/'+B+'combat-requirements/wp58-battle-recording-and-playback.md' in actual,sorted(actual))
for x in manifest:
 p=C/x['candidate'];raw=p.read_bytes();record('frozen mirror identity: '+x['formal_destination'],len(raw)==x['candidate_bytes'] and hashlib.sha256(raw).hexdigest()==x['candidate_sha256'],x['candidate_sha256'])
d=json.loads((E/'dispositions.json').read_text());req=[x for x in d['records'] if x['classification']=='required'];opt=[x for x in d['records'] if x['classification']=='optional'];record('required / optional dispositions',len(req)==11 and len(opt)==3 and all(x['optional_adopted'] for x in opt),{'required':len(req),'optional':len(opt)})
record('no self acceptance',all(not x[k] for x in d['records'] for k in ['canonical_closed','candidate_independent_PASS','actual_integration_PASS','ACCEPTED','CLOSED']),'all four gates pending')
record('input identity checks',all(x['verified'] for x in json.loads((E/'input-identity-checks.json').read_text())['checks']),'132/132; identity only')
# Preserve every existing catalog row, except the explicitly revised same-ID T02.
for name in ['combat-requirements-wp39-40-41-42-45.md','combat-requirements-wp49-51-52.md','pokemon-rules-wp19-21-22-23-34.md']:
 rel=B+'test-catalog/'+name;old=subprocess.check_output(['git','show',BASE+':'+rel],cwd=P).decode();new=(M/rel).read_text();rows=lambda s:Counter(l for l in s.splitlines() if l.startswith('|'))
 oldrows=rows(old);newrows=rows(new)
 if 'wp49-51-52' in name:
  t=[l for l in oldrows if l.startswith('| T02 |')];assert len(t)==1;oldrows.pop(t[0]);record('original AE-family T02 identity retained',len([l for l in newrows if l.startswith('| T02 |')])==1,'row content revised without renumbering')
 record('all other original catalog rows retained: '+name,not(oldrows-newrows),{'original_row_multiset':sum(oldrows.values()),'missing':list((oldrows-newrows).elements())})
# Read-only consumers and correct data tables are checked bytewise within their existing scope.
for rel in ['combat-requirements/wp39-battle-context-and-participants.md','combat-requirements/wp40-commands-obedience-and-action-order.md','combat-requirements/wp41-switching-positioning-and-escape.md','combat-requirements/wp52-a-generic-numerical-and-status-evaluation.md','pokemon-rules/wp19-attributes-ability-and-stats.md','user-interface/wp67-a-battle-interaction-and-presentation.md']:
 path=B+rel;old=subprocess.check_output(['git','show',BASE+':'+path],cwd=P).decode();new=(M/path).read_text();oldrows=Counter(l for l in old.splitlines() if l.startswith('|'));newrows=Counter(l for l in new.splitlines() if l.startswith('|'))
 if 'wp40-' in rel:
  for l in list(oldrows):
   if l.startswith('| MECHANICS_GENERATION |'):oldrows.pop(l)
 record('existing behavior tables retained: '+rel,not(oldrows-newrows),{'missing_rows':list((oldrows-newrows).elements())})
# New anchors must be unique; source locators/code are kept in evidence, never introduced into clean prose.
for x in manifest:
 p=C/x['candidate'];new=p.read_text();old=subprocess.check_output(['git','show',BASE+':'+x['formal_destination']],cwd=P).decode();anchors=re.findall(r'<a id="([^"]+)"',new);record('unique anchors: '+p.name,len(anchors)==len(set(anchors)),anchors)
 added=[l[1:] for l in __import__('difflib').unified_diff(old.splitlines(),new.splitlines()) if l.startswith('+') and not l.startswith('+++')]
 record('no source code/path added to clean body: '+p.name,not any(re.search(r'Data/Scripts|\.rb\b|^\s*(?:def |class |module )',l) for l in added),'data IDs and behavior formulas only')
# Pure arithmetic checks for the documented static constants. These are not a source emulator.
ceil=lambda x:(x.numerator+x.denominator-1)//x.denominator
schedule={'dedicated_1s':ceil(Fraction(20))+2,'ordinary_1s_pitch75':ceil(Fraction(20)/Fraction(3,4))+2,'missing':10+2,'resolved_zero':ceil(Fraction(0))+2}
record('static schedule arithmetic',schedule=={'dedicated_1s':22,'ordinary_1s_pitch75':29,'missing':12,'resolved_zero':2},schedule)
record('EV interval arithmetic',252-255==-3 and 0>252-255,{'lower':0,'upper':252-255,'credit':'arithmetic only; reversed clamp behavior is source-static evidence'})
src=subprocess.check_output(['git','show',R+':Data/Scripts/011_Battle/005_AI/008_AI_Utilities.rb'],cwd='/workspace/pokemon-essentials').decode();adds=re.findall(r'^Battle::AI::Handlers::AbilityRanking\.add\(',src,re.M);copies=re.findall(r'^Battle::AI::Handlers::AbilityRanking\.copy\(([^\n]+)',src,re.M);targets=sum(len(re.findall(r':\w+',x))-1 for x in copies)
record('AbilityRanking fixed declaration census',len(adds)==20 and targets==5,{'direct_add':len(adds),'copied_targets':targets,'expanded':len(adds)+targets,'copy_calls':copies})
# New standalone navigation links resolve in the exclusive package (proof files may be generated later).
for p in [C/'README.md']:
 missing=[]
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if ':' in target or target.startswith('#'):continue
  if not (p.parent/target.split('#')[0]).exists() and target not in ['evidence/static-validation.json','evidence/commands.jsonl']:missing.append(target)
 record('package navigation links',not missing,missing)
# Staged and unstaged tracked mutations must stay within this batch; untracked package files are expected.
tracked=run(['git','diff','--name-only',BASE]);prefix=C.relative_to(P).as_posix()+'/'
record('tracked write scope',all(p.startswith(prefix) for p in tracked.splitlines()),tracked.splitlines())
run(['git','diff','--cached','--check'])
result={'schema':'r8-u06-static-validation/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result':'STATIC_PACKAGE_CHECKS_PASS_NOT_INDEPENDENT_ACCEPTANCE','checks':checks,'behavior_reference_Ruby_game_native':'NOT_EXECUTED','formal_review':'NOT_PERFORMED_BY_THIS_AUTHOR','prior_tool_output_qualification':'commands.jsonl contains actual verification commands recorded here, not a reconstruction of every earlier preparation tool call. Earlier failed path/census navigation and clipped displays add zero reading credit; corrected complete reads are in author ledger.'}
(E/'static-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'result':result['result'],'checks':len(checks),'mirrors':len(manifest),'behavior_runs':0},ensure_ascii=False))
