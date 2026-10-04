"""B04 document/identity checks only. Never imports or executes reference code.

Reference mode is optional, uses byte reads + git object identity only:
  python self-check.py --reference /path/to/detached/reference
Run from the author repository root. No game, compiler, converter, deserializer,
media reader or behavioral/vector simulator is invoked.
"""
from pathlib import Path
import argparse, collections, csv, hashlib, json, re, subprocess

BASE = '6452c0e03025605222f3de9a272221e2b82eeda4'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
PREFIX = 'review/remediation/20261003-prepare/batches/B04/'
OUT = Path(PREFIX) / 'author-round-1'
ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode().strip())
parser = argparse.ArgumentParser()
parser.add_argument('--reference', type=Path)
args = parser.parse_args()
checks = []
def check(name, condition, detail=None):
    if not condition: raise AssertionError((name, detail))
    checks.append(dict(check=name,detail=detail))
def git(*argv): return subprocess.check_output(['git','-C',str(ROOT),*argv])
def sha(data): return hashlib.sha256(data).hexdigest()
def blob(data): return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def doc(name): return json.loads((ROOT/OUT/name).read_text())
h=json.loads((ROOT/'review/remediation/20261003-prepare/batches/B06/acceptance-stage-1/downstream-handshake.json').read_text())
allow=set(h['B04']['allowed_formal_write_paths']+h['B04']['allowed_original_sync_paths'])
check('accepted baseline is ancestor',subprocess.run(['git','-C',str(ROOT),'merge-base','--is-ancestor',BASE,'HEAD']).returncode==0)
check('author branch',git('branch','--show-current').decode().strip()=='remediation/20261003-prepare/batch-B04')
gate=doc('read-freeze-gate.json')
for row in gate['identities_checked']:
    data=git('show',row['commit']+':'+row['path'])
    check('input '+row['path'],sha(data)==row['sha256'] and blob(data)==row['blob'] and len(data)==row['bytes'])
check('input gate cardinality',len(gate['identities_checked'])==103 and gate['planned_reads']==74)
ctl=doc('finding-controls.json')
for row in h['B04']['contribution_controls']:
    for key,hashkey in [('original','original_object_sha256'),('acceptance','acceptance_object_sha256')]:
        data=json.dumps(ctl[row['id']][key],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
        check('canonical control '+row['id']+' '+key,sha(data)==row[hashkey])
check('all 35 controls',set(ctl)==set(h['B04']['contribution_finding_ids']) and len(ctl)==35)
changed=set(git('diff','--name-only',BASE).decode().splitlines())
untracked=set(git('ls-files','--others','--exclude-standard').decode().splitlines())
check('13 authorized formal files changed',changed- {p for p in changed if p.startswith(PREFIX)} ==allow)
check('no other tracked writes',all(p in allow or p.startswith(PREFIX) for p in changed))
check('untracked evidence only',all(p.startswith(PREFIX) for p in untracked))
check('ignore/reference/public/plan/history untouched',not any(p.startswith('reference/') or '.gitignore'==p or (p.startswith('review/') and not p.startswith(PREFIX)) for p in changed))
identities=doc('formal-artifact-identities.json')['files']
for row in identities:
    data=(ROOT/row['candidate']['path']).read_bytes()
    check('candidate artifact '+row['candidate']['path'],sha(data)==row['candidate']['sha256'] and len(data)==row['candidate']['bytes'] and blob(data)==row['candidate']['git_blob'])
check('formal diff identity',(ROOT/OUT/'formal-full.diff').read_bytes()==git('diff','--full-index','--unified=0',BASE,'--',*h['B04']['allowed_formal_write_paths'],*h['B04']['allowed_original_sync_paths']))

catalogs=[p for p in allow if '/test-catalog/' in p]
row_re=re.compile(r'^\| ([A-Z][A-Z0-9-]*) \|',re.M)
def rows(text):
    return [line for line in text.splitlines() if row_re.match(line) and not line.startswith('| ID |')]
permitted={'engine-overworld-wp11-15-59-60.md':{'RS09','RS10','RS17'},'engine-overworld-wp16.md':{'WR06','WR12'},'user-interface-wp17-63-65-66-67-68-69-70-71.md':{'MG23','DT03','DT07'}}
all_new=[]
for path in sorted(catalogs):
    old=git('show',BASE+':'+path).decode();new=(ROOT/path).read_text();before=rows(old);after=rows(new);ids=[row_re.match(x)[1] for x in before];newids=[row_re.match(x)[1] for x in after]
    check('existing IDs retained '+path,set(ids)<=set(newids))
    protected=[x for x in before if row_re.match(x)[1] not in permitted[Path(path).name]]
    surviving=[x for x in after if row_re.match(x)[1] in set(ids) and row_re.match(x)[1] not in permitted[Path(path).name]]
    check('other-owner/existing row bytes '+path,protected==surviving,dict(protected_rows=len(protected)))
    added=[x for x in after if row_re.match(x)[1] not in set(ids)]
    for line in added:
        check('new three-cell row '+row_re.match(line)[1],len(re.split(r'(?<!\\)\|',line))==5)
    extra=[row_re.match(x)[1] for x in added];check('new IDs unique '+path,len(extra)==len(set(extra)));all_new+=extra
check('111 static designs',len(all_new)==111 and set(all_new)==set(doc('static-design-inventory.json')['new_ids']))
check('XC 34 design rows',len([x for x in all_new if x.startswith('XC-')])==34)

response=doc('finding-responses.json')['responses']
check('35 response and proposal identities',set(x['id'] for x in response)==set(ctl)==set(x['id'] for x in doc('registry-proposals.json')['proposals']))
for row in response:
    check('source/design/clause assigned '+row['id'],bool(row['source_evidence'] and row['static_designs'] and row['clauses']))
    check('author not closing '+row['id'],row['state']=='AUTHOR_CANDIDATE_UNREVIEWED' and row['canonical_state']=='OPEN')
    for clause in row['clauses']:
        line=(ROOT/clause['path']).read_text().splitlines()[clause['line']-1]
        check('clause locator '+row['id']+' '+clause['section'],line.lstrip('# ')==clause['heading'])
    for test in row['static_designs']:
        line=(ROOT/test['path']).read_text().splitlines()[test['line']-1]
        check('static row locator '+test['id'],line==test['fixture_and_expected'] and line.startswith('| '+test['id']+' |'))
for row in doc('original-sync-ledger.json')['entries']:
    check('conditional original delta '+row['original_path'],(ROOT/row['diff']['path']).read_bytes()==git('diff','--full-index','--unified=0',BASE,'--',row['original_path']))
    original=(ROOT/row['original_path']).read_text();old=git('show',BASE+':'+row['original_path']).decode()
    # Keep old review identity/history/source-locator lines that do not contain a
    # corrected B04 clause. These are audit history, not approvals of new bytes.
    history=[line for line in old.splitlines() if '规格状态' in line or ('被审哈希' in line and line.startswith('|'))]
    check('old review history preserved '+row['original_path'],all(line in original for line in history) and 'B04 后继候选' in original)

W=ROOT/'deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md'
M=ROOT/'deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md'
wt=W.read_text();mt=M.read_text()
patterns=re.findall(r'(?<!\d)(\d+):(?:\d+,){3}\d+',wt)
check('48 pattern data identities',collections.Counter(map(int,patterns))==collections.Counter(range(48)))
character_rows=[x for x in mt.splitlines() if re.match(r'^\| [0-4] \| `',x)]
check('20 thirteen-character compatibility rows',len(character_rows)==5 and all(len(v)==13 for x in character_rows for v in re.findall(r'`([^`]+)`',x)))
hour_part=wt.split('默认24整点四通道')[1].split('四通道均按分钟')[0]
hour_rows=[x.split('|')[1].strip() for x in hour_part.splitlines() if re.match(r'^\| \d',x)]
hours=[]
for row in hour_rows:
    for part in row.split('、'):
        ends=list(map(int,part.split('–')));hours.extend(range(ends[0],ends[-1]+1))
check('24-hour data coverage without overlap',collections.Counter(hours)==collections.Counter(range(24)))
handoff=doc('interface-handoff.json')
check('B07/B06 five changed readers each',len(handoff['B04_to_B07']['changed_readers'])==len(handoff['B04_to_B06']['changed_readers'])==5)
limits=doc('authorization-and-limits.json')
check('model actual unverified and no execution',limits['effective_configuration']=='UNVERIFIED' and all(limits[k]==0 for k in ['runtime_observations','proven_demo_event_chains','vector_executions','reference_execution']))
check('global open unchanged',limits['canonical_required_open']==229 and limits['canonical_closed']==0)

source=list(csv.DictReader((ROOT/OUT/'source-reading-log.tsv').open(),delimiter='\t'))
for row in source:
    check('bounded source range '+row['path'],row['commit']==REF and 1<=int(row['first'])<=int(row['last'])<=int(row['actual_lines']))
if args.reference:
    ref=args.reference.resolve()
    check('fixed reference commit',subprocess.check_output(['git','-C',str(ref),'rev-parse','HEAD']).decode().strip()==REF)
    check('reference clean',not subprocess.check_output(['git','-C',str(ref),'status','--porcelain']))
    files={}
    for row in source:
        p=row['path']
        if p not in files:
            data=(ref/p).read_bytes();fixed=subprocess.check_output(['git','-C',str(ref),'show',REF+':'+p]);check('reference worktree bytes '+p,data==fixed);files[p]=data
        data=files[p];lines=data.splitlines(keepends=True);a,b=int(row['first']),int(row['last'])
        check('full and bounded source hashes '+p,len(lines)==int(row['actual_lines']) and sha(data)==row['full_sha256'] and blob(data)==row['full_blob'] and sha(b''.join(lines[a-1:b]))==row['range_sha256'])
proc=subprocess.run(['git','-C',str(ROOT),'diff','--check',BASE],capture_output=True,text=True)
check('diff whitespace',proc.returncode==0,proc.stdout+proc.stderr)
print(json.dumps(dict(state='AUTHOR_DOCUMENT_CHECKS_COMPLETED',independent_review=False,check_count=len(checks),checks=checks,static_source_range_rows=len(source),reference_files=len(set(x['path'] for x in source)),static_design_rows=111,runtime_observations=0,demo_chains=0,vector_executions=0,model_effective='UNVERIFIED'),ensure_ascii=False,indent=2))
