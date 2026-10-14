"""Independent immutable binding and reading coverage checks, not game execution."""
import datetime, hashlib, json, pathlib, re, subprocess
ROOT = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path('/workspace/pokemon-essentials-clean-room')
ACTUAL = '86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
TREE = '67e8c55d520fa8cad2928cb4b95e24c3ed602d5a'
FORMAL = 'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
BASE = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
PREFIX = str(ROOT.relative_to(REPO))
REQUIRED = ['GR6-K-001','GR6-K-002','GR6-K-003','GR6-O-001','GR6-O-002',
            'R6-D-LZ-001','R6-D-LZ-002','R6-D-PBS-C05','R6-D-PBS-C06',
            'R6-D-PBS-C07','R6-D-DATA-C01']
checks = []
def git(*args):
    return subprocess.check_output(['git', *args], cwd=REPO)
def identity(raw):
    return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
            'git_blob':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}
def check(name, result, details=None):
    checks.append({'check':name,'pass':bool(result),'details':details})
    if not result: raise AssertionError(name)
def load(name): return json.loads((ROOT/'payload-audit'/name).read_text())
check('exact HEAD',git('rev-parse','HEAD').decode().strip()==ACTUAL)
check('workspace tree',git('rev-parse',ACTUAL+'^{tree}').decode().strip()==TREE)
check('formal tree',git('rev-parse',ACTUAL+':deliverables/final-specification-set').decode().strip()==FORMAL)
binding = load('actual-input-group-A-extraction.json')
check('exact 11-ID coverage',binding['required_ids']==REQUIRED)
input_path = binding['input_path']
check('full actual input identity',identity(git('show',ACTUAL+':'+input_path))==binding['input_identity'])
paths = [r['path'] for r in binding['files']]
paths += [r['path'] for r in binding['unchanged_prospective_paths']]
check('22 distinct appointed full texts',len(paths)==22 and len(set(paths))==22)
receipts = [json.loads(line) for line in (ROOT/'commands.jsonl').read_text().splitlines()]
coverage = {}; source_reads = []
for row in receipts:
    if row['exit'] != 0: continue
    raw = (ROOT/row['stdout']).read_text(errors='replace')
    match = re.match(r'INPUT (file|source) (.*?) TOTAL_LINES (\d+) READ (\d+)-(\d+)\n',raw)
    if not match: continue
    mode,path,total,a,b=match.groups(); total,a,b=map(int,(total,a,b))
    record={'path':path,'total_lines':total,'read_range':[a,b],'command':row['number']}
    # The stdout is complete on disk. Root additionally repaired UI truncations.
    if mode=='source': source_reads.append(record)
    elif path in paths: coverage.setdefault(path,[]).append(record)
full = []
for path in paths:
    raw = git('show',ACTUAL+':'+path)
    check('immutable body '+path,raw==(REPO/path).read_bytes())
    row=next(r for r in binding['files']+binding['unchanged_prospective_paths'] if r['path']==path)
    expected=row.get('actual',row.get('identity'))
    check('full metadata '+path,identity(raw)==expected)
    total=len(raw.decode().splitlines()); covered=set()
    for receipt in coverage.get(path,[]):covered.update(range(receipt['read_range'][0],receipt['read_range'][1]+1))
    check('complete root reading receipts '+path,covered>=set(range(1,total+1)))
    full.append({'path':path,'identity':identity(raw),'lines':total,'complete_receipt_ranges':coverage[path],
                 'semantic_read':'ROOT_ACTUAL_FULL_TEXT_WITH_UI_GAPS_REPAIRED'})
wp21='deliverables/final-specification-set/pokemon-rules/wp21-form-change-layer.md'
wp21=next(p for p in paths if '/wp21-' in p)
check('protected WP21 byte equality',git('show',ACTUAL+':'+wp21)==git('show',BASE+':'+wp21))
shared = load('shared-composition-complete-metadata.json')
check('21 changed shared files, all owners received',len(shared)==21 and all(not r['pending_primary_writers'] for r in shared))
check('31 shared contributions',sum(len(r['all_contributions']) for r in shared)==31)
for commit, name, digest in [
 ('f1a8f14fe521070c51abb821c9876e95e6a20d1c','R6-U01-R/report.md','b6638cbf687339cd34769fcd91055836514c20c18a089d16230128c2a73027ac'),
 ('034403bb9fbce7e49ea2784d38295c5260a1e0dd','R6-U03-R/report.md','cc3875268d0a559f0ce10dee9c60dd59f9644ff248858efb158efa7b26dac644'),
 ('7cdf74a0b2494e2ec71ca39db6d917f81f420973','R6-U14-R/review-report.md','5cf6a38c7209966ab87a6826f07637ddec475020e7a572a534c83eb3b7f04083')]:
    path='review/remediation-sixth-20261014-prepare/reviews/'+name
    raw=git('--git-dir=/tmp/r6-actual-a-payload-20261014.git','show',commit+':'+path)
    check('old report fixed-object preservation '+name,identity(raw)['sha256']==digest,
          {'commit':commit,'path':path,'identity':identity(raw),'qualification':'Separate original review objects, not presumed merged into actual tree'})
check('no tracked mutation outside report',not git('diff','--name-only').strip())
status=git('status','--porcelain','--untracked-files=all').decode().splitlines()
check('only authorized new files',all(line[3:].startswith(PREFIX+'/') for line in status))
check('selected history complete original value match',load('summary.json')['verified_U14_original_qualification_fields']==118 and load('summary.json')['verified_U14_original_case_fields']==78)
source_identity=[]
for path in sorted({r['path'] for r in source_reads}):
    raw=git('--git-dir=/tmp/r6-u01-r-reference.git','show',REF+':'+path)
    source_identity.append({'commit':REF,'path':path,**identity(raw),
        'read_ranges':[r for r in source_reads if r['path']==path]})
ledger={'schema':'r6.actual.group-a.root-reading-ledger.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'actual_commit':ACTUAL,'workspace_tree':TREE,'formal_tree':FORMAL,'appointed_formal_count':len(full),
 'appointed_formal_lines':sum(r['lines'] for r in full),'formal_full_reads':full,'fresh_source_ranges':source_identity,
 'reuse':{'U01_original_contract_source_and_history':'Identity matched prior direct root review f1a8f14fe521070c51abb821c9876e95e6a20d1c; no semantic verdict inheritance',
         'U14_activation':'Exact original activation identity reused from prior U01 history review; current historical status only'},
 'UI_gap_repairs':'All appointed formal display gaps reread at narrower ranges; complete raw outputs retained. Large optional metadata display does not count as a full semantic read.',
 'reference_model_host_execution':0}
(ROOT/'reading-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
out={'schema':'r6.actual.group-a.root-independent-validation.v1','utc':ledger['utc'],'evidence_level':'TOOL_VALIDATION',
 'checks':checks,'count':len(checks),'failed':[],'actual_commit':ACTUAL,'formal_tree':FORMAL,
 'semantic_verdict_source':'Root direct per-ID source/counter/formal/consumer/historical reasoning in report and findings',
 'reference_model_host_execution':0}
(ROOT/'independent-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'all_pass':True,'formal_full_files':len(full),'formal_lines':ledger['appointed_formal_lines'],
 'fresh_source_files':len(source_identity),'source_range_receipts':len(source_reads)},ensure_ascii=False))
