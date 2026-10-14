"""Independent fixed-object/byte checks. Does not load or execute reference code."""
import concurrent.futures
import datetime
import difflib
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import subprocess
import sys
import urllib.parse
import urllib.request

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
PREP = OUT.parents[1]
C = '7f2010c97f152054ba890974a3320ca1478f7318'
P = 'bcd194b0e4c293764998b7040b0154af8041bf41'
BASE = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
R_GIT = '/tmp/R6-U03-R-reference.git'
CORE = '5210b009db5191f307301115845e31475cd798ef'
REPORT = 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/'
SCRATCH = Path('/tmp/R6-U03-R-inputs')

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def git(*args, reference=False):
    prefix = ['git', '--git-dir=' + R_GIT] if reference else ['git']
    return subprocess.check_output(prefix + list(args), cwd=ROOT)

def ident(b):
    return dict(bytes=len(b), sha256=hashlib.sha256(b).hexdigest(),
                git_blob=hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest())

def raw(ref, path, repository='y805939188/pokemon-essentials-clean-room'):
    url = 'https://raw.githubusercontent.com/' + repository + '/' + ref + '/' + urllib.parse.quote(path)
    start = now()
    try:
        b = urllib.request.urlopen(url, timeout=30).read()
        return b, dict(ref=ref, path=path, repository=repository, url=url,
                       start_utc=start, end_utc=now(), **ident(b))
    except Exception as exc:
        return None, dict(ref=ref, path=path, start_utc=start, end_utc=now(), error=str(exc))

def downloads():
    paths = git('ls-tree', '-r', '--name-only', P, str((PREP/'candidates/R6-U03').relative_to(ROOT))).decode().splitlines()
    jobs = [(P, path) for path in paths]
    jobs += [(CORE, REPORT + path) for path in [
        'tasks/R6-H/report.md', 'tasks/R6-H/forward-matrix.json',
        'tasks/R6-H/reverse-matrix.json', 'tasks/R6-O/fishing-random-boundaries.rb',
        'tasks/R6-O/fishing-random-boundaries-results.json',
        'findings/normative-records.json', 'findings/aliases-and-tombstones.json',
        'findings/policy-records.json', 'findings/limit-records.json',
        'handoff/update-batches.json', 'handoff/dependency-graph.json', 'handoff/file-conflict-graph.json']]
    rows = []
    SCRATCH.mkdir(exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for (ref, path), (b, row) in zip(jobs, pool.map(lambda j: raw(*j), jobs)):
            if b is not None:
                target = SCRATCH/ref/path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(b)
                row['local_scratch'] = str(target)
                if ref == P:
                    expected = git('cat-file', 'blob', ref + ':' + path)
                    row['full_bytes_equal_fixed_git'] = b == expected
                    row['mode_type'] = git('ls-tree', ref, '--', path).decode().split()[:2]
            rows.append(row)
    receipt = dict(start_utc=rows[0]['start_utc'], end_utc=now(), rows=rows,
                   candidate_payload_count=len(paths), candidate_all_matched=all(
                       x.get('full_bytes_equal_fixed_git') for x in rows[:len(paths)]),
                   classification='TOOL_VALIDATION; byte retrieval is not semantic reading')
    (OUT/'input-readback.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='rows'}))
    print(json.dumps([x for x in rows if 'error' in x], ensure_ascii=False))

def checks():
    start = now()
    checks = []
    def check(name, ok, detail=None):
        checks.append(dict(name=name, result='PASS' if ok else 'FAIL', detail=detail))
    contract = json.loads((PREP/'contracts/R6-U03.json').read_text())
    prompt = (PREP/'prompts/R6-U03-R.md').read_bytes()
    check('review_prompt', ident(prompt) == dict(bytes=153142,sha256='770b9b12ef73660a9960bc95cd39a35d52eb91ced4d01aaee409b0231eae422a',git_blob='b5f304cb30f70a34670dcd200bc5a2ce74ce0747'))
    check('complete_prompt_contract', json.loads(prompt.decode().split('```json\n')[1].split('\n```')[0]) == contract)
    check('C_tree', git('rev-parse',C+'^{tree}').decode().strip()=='33824456d41f8528e0353218576e734fa5f227eb')
    check('P_tree', git('rev-parse',P+'^{tree}').decode().strip()=='284935e30063fcdd922fbd9196903cbe88a7434b')
    check('P_parent', git('rev-parse',P+'^').decode().strip()==C)
    check('R_tree', git('rev-parse',R+'^{tree}',reference=True).decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0')
    check('formal_unmodified', not git('diff','--name-only',MAIN,P,'--','deliverables'))
    mirror = PREP/'candidates/R6-U03/mirror'
    oldnew = {}
    identities = []
    for path in contract['candidate_formal_paths']:
        old=git('show',MAIN+':'+path); new=(mirror/path).read_bytes()
        candidate_path=str((mirror/path).relative_to(ROOT))
        check('baseline_mirror:'+path,git('show',BASE+':'+candidate_path)==old)
        check('C_P_mirror_same:'+path,git('show',C+':'+candidate_path)==git('show',P+':'+candidate_path)==new)
        ops=difflib.SequenceMatcher(None,old.splitlines(keepends=True),new.splitlines(keepends=True),autojunk=False).get_opcodes()
        oldnew[path]=(old,new,ops)
        identities.append(dict(formal_path=path,candidate_path=candidate_path,baseline=ident(old),candidate=ident(new),mode='100644',type='blob',changes=[dict(op=t,old=[a+1,b],new=[c+1,d]) for t,a,b,c,d in ops if t!='equal']))
    frozen=json.loads((PREP/'inputs/frozen-inputs.json').read_text())
    sources=[]
    for path in contract['read_only_reference_paths']:
        b=git('show',R+':'+path,reference=True)
        row=next(x for x in frozen['source_materials'] if x['path']==path)
        check('source_identity:'+path,ident(b)=={k:row[k] for k in ident(b)})
        sources.append(dict(path=path,commit=R,**ident(b)))
    author=json.loads((PREP/'candidates/R6-U03/evidence/static-checks.json').read_text())
    check('author_actual136',len(author['checks'])==136 and all(x['result']=='PASS' for x in author['checks']))
    hist=json.loads((PREP/'candidates/R6-U03/evidence/historical-regression-input.json').read_text())
    spans=[]
    for row in hist['relevant_file_spans']:
        consumer=row['consumer']; path=consumer['path']; s,e=consumer['lines']
        old,new,ops=oldnew[path]; ol=old.splitlines(keepends=True); nl=new.splitlines(keepends=True)
        original=b''.join(ol[s-1:e]); positions=[]
        for tag,a,b,c,d in ops:
            if tag=='equal': positions += [c+i-a+1 for i in range(max(a,s-1),min(b,e))]
        projection=b''.join(nl[i-1] for i in positions)
        check('history:'+row['id']+':'+path+':'+str(s),len(positions)==e-s+1 and projection==original and hashlib.sha256(original).hexdigest()==consumer['span_sha256'])
        spans.append(dict(id=row['id'],path=path,original_lines=[s,e],candidate_original_positions=positions,original_sha256=hashlib.sha256(original).hexdigest(),contiguous=positions[-1]-positions[0]+1==len(positions),new_containing_sha256=hashlib.sha256(b''.join(nl[positions[0]-1:positions[-1]])).hexdigest()))
    check('33spans',len(spans)==33 and sum(x['contiguous'] for x in spans)==32)
    manifest=json.loads((PREP/'candidates/R6-U03/evidence/candidate-manifest.json').read_text())
    for row in manifest['payloads']:
        b=git('show',P+':'+row['path'])
        check('candidate_manifest:'+row['path'],ident(b)=={k:row[k] for k in ident(b)} and git('ls-tree',P,'--',row['path']).decode().split()[:2]==[row['mode'],row['type']])
    all_paths=git('ls-tree','-r','--name-only',P,str((PREP/'candidates/R6-U03').relative_to(ROOT))).decode().splitlines()
    check('20_complete_candidate_payloads',set(all_paths)=={x['path'] for x in manifest['payloads']}|{manifest['self_hash_exclusion'],manifest['finite_publication_appendix']} and len(all_paths)==20)
    changed=git('diff','--name-only',BASE,P).decode().splitlines()
    prefix=str((PREP/'candidates/R6-U03').relative_to(ROOT))+'/'
    check('candidate_only_writes',all(x.startswith(prefix+'evidence/') or x.startswith(prefix+'mirror/') for x in changed) and len(changed)==20)
    check('input_remote20',json.loads((OUT/'input-readback.json').read_text())['candidate_all_matched'])
    forward=json.loads((SCRATCH/CORE/REPORT/'tasks/R6-H/forward-matrix.json').read_text())
    relevant={x['consumer']['path'] for x in hist['relevant_file_spans']}
    fresh=[dict(id=row['id'],consumer=x,candidate_clause=row['candidate_clause'],activation_lines=row['activation_lines'],frozen_scope=row['frozen_scope'],native_count=row['native_count'],schema_count=row['schema_count']) for row in forward for x in row['formal_consumers'] if x['path'] in relevant]
    check('independently_recovered33_histories',fresh==hist['relevant_file_spans'])
    check('complete_M03_007_H_projection',next(x for x in forward if x['id']=='GR5-M03-007')==hist['immediate_interpreter_fishing_qualification'])
    batch=json.loads((SCRATCH/CORE/REPORT/'handoff/batch-assignment.json').read_text())
    check('fixed_handoff_U03_contract',next(x for x in batch['batches'] if x['id']=='R6-U03')==contract)
    for n, expected in [(98,[]),(99,[101]),(100,[101])]:
        check('finite_freeze_arithmetic:'+str(n),list(range(101,n+3,101))==expected,dict(terminal=n+1,empty_list=n+2,requests=expected))
    for rod,expected in [(1,[45,68]),(2,[70,100]),(3,[95,100])]:
        normal=20+25*rod; fast=Fraction(normal)*Fraction(3,2)
        counts=[sum(x<t for x in range(100)) for t in [normal,fast]]
        check('finite_probability_arithmetic:'+str(rod),counts==expected,dict(thresholds=[str(normal),str(fast)],accepted_integers=counts))
    normative=SCRATCH/CORE/REPORT/'findings/normative-records.json'
    if normative.exists():
        o=json.loads(normative.read_text()); records=o if isinstance(o,list) else o['records']
        for c in contract['scope_contracts']:
            check('full_original_normative:'+c['id'],next(x for x in records if x['id']==c['id'])==c)
    output=dict(start_utc=start,end_utc=now(),cwd=str(ROOT),argv=sys.argv,checks=checks,candidate_identities=identities,source_identities=sources,historical_spans=spans,new_reference_execution=0,new_host_execution=0,new_full_model_execution=0,result='PASS' if all(x['result']=='PASS' for x in checks) else 'FAIL')
    (OUT/'independent-checks.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(result=output['result'],checks=len(checks),failures=[x for x in checks if x['result']=='FAIL']),ensure_ascii=False))
    return 0 if output['result']=='PASS' else 1

if __name__=='__main__':
    if sys.argv[1]=='downloads': downloads()
    elif sys.argv[1]=='checks': sys.exit(checks())
