"""Seal identities without inventing a self hash or a future commit ID."""
import json
from build_candidate import B, H, R, ROOT, OUT, EVID, git, identity, dump

def main():
    mirrors=json.loads((EVID/'mirror-identities.json').read_bytes())
    allowed={r['candidate_path'] for r in mirrors['files']}
    files=[]
    for path in sorted(OUT.rglob('*')):
        if path.is_dir(): continue
        relative=str(path.relative_to(ROOT))
        assert relative in allowed or relative.startswith('candidates/R7-U12/evidence/author/')
        assert not path.is_symlink() and '__pycache__' not in path.parts
        if path==EVID/'artifact-manifest.json': continue
        files.append({'path':relative,'baseline':{'commit':B,'exists':False,'bytes':None,'sha256':None,'git_blob':None},'new':identity(path.read_bytes())})
    for r in mirrors['files']:
        assert identity((ROOT/r['candidate_path']).read_bytes())==r['new']
    dump(EVID/'artifact-manifest.json',{'schema':'r7.u12.author-artifact-manifest.v1',
        'status':'CANDIDATE_READY_NOT_REVIEWED','baseline_commit':B,
        'baseline_root_tree':'84f79ec6e772aacbf3a464fde68cdc5a280e2950',
        'baseline_formal_tree':'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c',
        'branch':'codex/r7-u12-author-20261015-wave1','scope':'Exactly six authorized mirrors plus evidence/author; no formal/reference/public ledger writes.',
        'mirrors':mirrors['files'],'historical_targets':mirrors['historical_targets'],
        'all_new_commit_files_except_self':files,
        'self_binding':'This manifest excludes only its own hash; final commit/tree and full-file remote readback externally bind it. No recursive/future self hash is asserted.',
        'expected_total_files_in_final_commit':len(files)+1,
        'effective_model_configuration':'UNVERIFIED','candidate_review':'PENDING different actual context ultra reviewer'})
    print(json.dumps({'status':'MANIFEST_SEALED','new_files':len(files)+1,'mirrors':6,'manifest':identity((EVID/'artifact-manifest.json').read_bytes())}))

if __name__=='__main__':main()
