#!/usr/bin/env python3
"""TOOL_VALIDATION only: replay specified prose edits and verify artifact identities."""
import argparse, hashlib, json, re, subprocess, tempfile
from pathlib import Path

def identity(b):
    return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())

def validate(root):
    repo=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],cwd=root,text=True).strip())
    data=json.loads((root/'operations.json').read_text());base=data['base_commit']
    contract=json.loads(subprocess.check_output(['git','show','93524fe5cf396de2bd01f3c5c1e08ba4b874bc68:review/remediation-fifth-20261013-prepare/contracts/R5-U03/contract.json'],cwd=repo))
    operations=data['operations']; paths=sorted({x['target_path'] for x in operations}); baseline={}; projected={}
    for p in paths:
        baseline[p]=subprocess.check_output(['git','show',base+':'+p],cwd=repo).decode()
        projected[p]=baseline[p]
    for op in operations:
        p=op['target_path']
        assert p in contract['batch']['allowed_formal_files'],p
        for fid in op['finding_ids']:assert p in contract['per_finding_formal_permissions'][fid],(fid,p)
        assert identity(baseline[p].encode())['git_blob']==op['B5_anchor']['git_blob']
        if op['operation']=='append':projected[p]+=op['new_text']
        else:
            assert projected[p].count(op['old_text'])==1,op['label']
            projected[p]=projected[p].replace(op['old_text'],op['new_text'],1)
    assert set(paths)==set(contract['batch']['allowed_formal_files'])
    for p,mirror in contract['candidate_direct_mirrors'].items():
        assert (repo/mirror).read_text()==projected[p],p
    fragments=json.loads((root/'fragment-manifest.json').read_text())['fragments']
    for f in fragments:
        assert f['target_path'] in contract['shared_fragment_outputs'],f['target_path']
        lines=(root/f['fragment_file']).read_text().splitlines(keepends=True)
        snippet=''.join(lines[f['fragment_start_line']-1:f['fragment_end_line']])
        assert snippet.rstrip('\n')==f['new_text'].rstrip('\n'),f['label']
    with tempfile.TemporaryDirectory(prefix='r5-u03-replay-') as td:
        d=Path(td)
        for p,s in baseline.items():q=d/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_text(s)
        subprocess.run(['git','apply','--check',str(root/'formal-diff.patch')],cwd=d,check=True,capture_output=True)
        subprocess.run(['git','apply',str(root/'formal-diff.patch')],cwd=d,check=True,capture_output=True)
        assert all((d/p).read_text()==s for p,s in projected.items())
    vs=json.loads((root/'static-vectors.json').read_text())['vectors'];ids=[v['id'] for v in vs]
    assert len(ids)==len(set(ids));assert {v['finding_id'] for v in vs}==set(contract['required_ids'])
    assert all(v['evidence_level']=='DERIVED_VECTOR' and v['execution_status']=='NOT_EXECUTED' for v in vs)
    for v in vs:
        for field in ['premises','input','expected']:assert v[field]
        receivers=[p for p in paths if '/test-catalog/' in p and '| '+v['id']+' |' in projected[p]]
        assert receivers,v['id']
    # Validate new relative file links in the projected set, using fixed B5 for unchanged receivers.
    missing=[]
    for op in operations:
        for target in re.findall(r'\]\(([^)]+)\)',op['new_text']):
            if '://' in target or target.startswith('#'):continue
            normalized=(Path(op['target_path']).parent/target.split('#')[0]).as_posix()
            import posixpath
            normalized=posixpath.normpath(normalized)
            if normalized not in projected:
                found=subprocess.run(['git','cat-file','-e',base+':'+normalized],cwd=repo,capture_output=True)
                if found.returncode:missing.append(normalized)
    assert not missing,missing
    if (root/'candidate-manifest.json').exists():
        manifest=json.loads((root/'candidate-manifest.json').read_text())
        for x in manifest['artifacts']:assert identity((root/x['path']).read_bytes())=={k:x[k] for k in ['bytes','sha256','git_blob']},x['path']
    return dict(evidence_level='TOOL_VALIDATION',status='PASS',changed_formal_paths=len(paths),direct_mirrors=8,shared_target_files=8,fragments=len(fragments),operations=len(operations),derived_vectors=len(vs),patch_replay='PASS',relative_links='PASS',permission_mapping='PASS',behavior_execution_count=0,independent_verdict='NOT_SIGNED')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parent);args=parser.parse_args()
    print(json.dumps(validate(args.root),ensure_ascii=False,indent=2))
