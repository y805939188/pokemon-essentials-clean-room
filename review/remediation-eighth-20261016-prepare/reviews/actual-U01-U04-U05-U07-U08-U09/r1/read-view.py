"""Fixed-object, line-numbered reading aid; viewing does not itself confer FULL credit."""
import json, pathlib, subprocess, sys
ROOT=pathlib.Path(__file__).resolve().parents[5]
SNAP='49a558f7d5498680ba88d532f3815e07d7844459'
HAND='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/'
def blob(path, ref=SNAP):
    return subprocess.check_output(['git','show',ref+':'+path],cwd=ROOT).decode()
def prune(x):
    if isinstance(x,dict):
        return {k:prune(v) for k,v in x.items() if k not in {'sha256','blob','bytes','mode','tree','workspace_tree','report_tree','binding_validation','source_evidence','formal_evidence','fixed_R','fixed_B8'}}
    if isinstance(x,list): return [prune(v) for v in x]
    return x
mode=sys.argv[1]
if mode=='contract':
    ids=json.loads(blob('review/remediation-eighth-20261016-prepare/integration/U01-U04-U05-U07-U08-U09/actual-review-input.json','3cc8e017c6629a0fc8cb0827bc16dda0e9adca91'))['batches']
    wanted=next(b for b in ids if b['batch']==sys.argv[2]); wanted=set(wanted['required_ids']+wanted['selected_optional_ids'])
    records=json.loads(blob(HAND+'contracts.zh.json'))['records']
    for r in records:
        if r['id'] in wanted: print(json.dumps(prune(r),ensure_ascii=False,indent=2))
elif mode=='file':
    path=sys.argv[2]; start=int(sys.argv[3]) if len(sys.argv)>3 else 1; stop=int(sys.argv[4]) if len(sys.argv)>4 else 999999
    lines=blob(path).splitlines(); print('OBJECT',SNAP,path,'TOTAL_LINES',len(lines))
    for n,s in enumerate(lines,1):
        if start<=n<=stop:print(f'{n}: {s}')
elif mode=='report':
    d=json.loads(blob('review/remediation-eighth-20261016-prepare/integration/U01-U04-U05-U07-U08-U09/actual-review-input.json','3cc8e017c6629a0fc8cb0827bc16dda0e9adca91'))
    b=next(b for b in d['batches'] if b['batch']==sys.argv[2]);print(blob(b['candidate_review_report_path']))
