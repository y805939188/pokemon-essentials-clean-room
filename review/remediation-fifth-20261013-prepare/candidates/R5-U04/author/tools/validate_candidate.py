#!/usr/bin/env python3
"""Rebuild scoped document bytes in scratch; never execute reference/model behavior."""
import argparse,difflib,hashlib,json,re,subprocess,tempfile
from pathlib import Path

def identity(data):
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,required=True,help='Existing checkout containing immutable B5 Git objects')
    parser.add_argument('--output',type=Path,help='Optional TOOL_VALIDATION JSON output, only scratch or this author directory')
    args=parser.parse_args();repo=args.repo.resolve();author=Path(__file__).resolve().parents[1]
    records=json.loads((author/'finding-responses.json').read_text())
    log=json.loads((author/'source-reading-log.json').read_text())
    ops=json.loads((author/'edit-operations.json').read_text());frags=json.loads((author/'fragment-manifest.json').read_text())
    batch='R5-U04';base='9366d9d17aaeac3b4414236468affa650fb3dd27'
    prefix='review/remediation-fifth-20261013-prepare/candidates/R5-U04/author/'
    ids=records['required_ids'];assert len(ids)==7 and len(set(ids))==7
    perms={f['id']:set(f['formal_permissions']) for f in records['findings']}
    projections={};original={};source_anchor_checks=[]
    for op in ops:
        p=op['target_path'];assert p.startswith('deliverables/final-specification-set/') and '..' not in Path(p).parts
        assert all(p in perms[id] for id in op['finding_ids'])
        if p not in projections:
            data=subprocess.check_output(['git','show',base+':'+p],cwd=repo)
            original[p]=data;projections[p]=data.decode('utf-8')
        text=projections[p];mode=op['operation']
        if mode=='append':text=text.rstrip()+'\n\n'+op['replacement'].strip()+'\n'
        else:
            anchor=op['B5_anchor'];assert text.count(anchor)==1,(p,anchor)
            text=text.replace(anchor,(op['replacement']+anchor) if mode=='insert_before' else op['replacement'],1)
        projections[p]=text
    direct=[]
    for p,text in projections.items():
        if p.endswith('wp39-battle-context-and-participants.md'):
            assert not (author/'formal'/p).exists()
            f=frags['fragments'][0];assert f['target_path']==p and f['B5_identity']['git_blob']==identity(original[p])['git_blob']
            assert (repo/f['fragment_path']).read_text()==f['replacement']
        else:
            data=(author/'formal'/p).read_bytes();assert data==text.encode('utf-8'),p
            direct.append({'formal_path':p,'candidate_path':prefix+'formal/'+p,**identity(data),'B5':identity(original[p])})
    patch=''.join(''.join(difflib.unified_diff(original[p].decode().splitlines(True),text.splitlines(True),fromfile='a/'+p,tofile='b/'+p)) for p,text in sorted(projections.items()))
    assert patch.encode()==(author/'formal-diff.patch').read_bytes()
    with tempfile.TemporaryDirectory(prefix='r5-u04-projection-') as tmp:
        scratch=Path(tmp)
        for p,data in original.items():
            out=scratch/p;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(data)
        subprocess.run(['git','apply','--check','--whitespace=error-all',str(author/'formal-diff.patch')],cwd=scratch,check=True,capture_output=True)
        subprocess.run(['git','apply','--whitespace=error-all',str(author/'formal-diff.patch')],cwd=scratch,check=True,capture_output=True)
        assert all((scratch/p).read_bytes()==text.encode() for p,text in projections.items())
    reg=json.loads((author/'regression-results.json').read_text())
    for p,text in projections.items():
        if '/test-catalog/' in p:assert text.encode().startswith(original[p])
    for r in reg['old_vector_checks']:
        line=next(l for l in projections[r['path']].splitlines() if l.startswith('| '+r['id']+' |'))
        assert hashlib.sha256((line+'\n').encode()).hexdigest()==r['B5_line_sha256']
    vectors=json.loads((author/'static-vectors.json').read_text());vmap={v['id']:v for v in vectors['vectors']}
    assert len(vmap)==vectors['design_count']==len(vectors['vectors'])
    for f in records['findings']:
        assert f['id'] in ids and f['CLOSED'] is False and f['formal_acceptance']=='NOT_REGISTERED'
        assert f['mandatory_criteria'] and not f['optional_added_to_mandatory']
        for q in f['mandatory_criteria']:
            for v in q.get('vectors',[]):assert v in vmap
            for r in q.get('receivers',[]):
                rel=Path(r['candidate_path']).relative_to(prefix);txt=(author/rel).read_text()
                assert r['heading'] in txt.splitlines()[r['candidate_line']-1]
        assert set(f['scenario_dimensions'])=={'normal','failure','cancellation','partial_commit'}
    # Resolve links newly introduced in owned formal text against B5 or a projected target.
    link_checks=[]
    def slug(h):
        h=re.sub(r'[^\w\s-]','',h.strip().lower());return re.sub(r'\s+','-',h)
    for p,text in projections.items():
        old_links=set(re.findall(r'\]\(([^)]+)\)',original[p].decode()))
        for link in set(re.findall(r'\]\(([^)]+)\)',text))-old_links:
            if '://' in link:continue
            target,_,anchor=link.partition('#');from pathlib import PurePosixPath
            parts=[]
            for part in (PurePosixPath(p).parent/PurePosixPath(target)).parts:
                if part=='..':parts.pop()
                elif part!='.':parts.append(part)
            tp='/'.join(parts)
            target_text=projections.get(tp)
            if target_text is None:target_text=subprocess.check_output(['git','show',base+':'+tp],cwd=repo).decode()
            if anchor:assert anchor in {slug(l.lstrip('#')) for l in target_text.splitlines() if l.startswith('#')},(p,link)
            link_checks.append({'from':p,'link':link,'result':'RESOLVED_STATIC_TARGET'})
    json_files=[]
    for p in sorted(author.rglob('*.json')):
        json.loads(p.read_text());json_files.append(str(p.relative_to(author)))
    for p in sorted(author.rglob('*')):
        if not p.is_file() or p.suffix not in ['.md','.json','.py']:continue
        assert '\r' not in p.read_text()
        assert all(l==l.rstrip() for l in p.read_text().splitlines()),p
    working=subprocess.check_output(['git','diff','--name-only',base],cwd=repo).decode().splitlines()
    assert all(p.startswith(prefix) for p in working),working
    assert subprocess.check_output(['git','rev-parse',base+':deliverables/final-specification-set'],cwd=repo).decode().strip()=='d5a462b4c6f8b78c3264a25d6b5495230fa265e2'
    result={'schema':'r5.u04.tool-validation.v1','evidence_level':'TOOL_VALIDATION','status':'PASS_TOOL_VALIDATION_ONLY',
            'B5_commit':base,'projected_direct_files':direct,'projected_shared_files':1,'operations':len(ops),
            'git_apply_check_and_scratch_apply':'PASS','reconstructed_payloads_equal':'PASS','path_and_per_finding_permissions':'PASS',
            'old_catalog_full_prefixes_equal_B5':'PASS','old_vector_rows':len(reg['old_vector_checks']),
            'static_designs':len(vmap),'mandatory_criterion_mappings':sum(len(f['mandatory_criteria']) for f in records['findings']),
            'JSON_files_parsed':json_files,'new_link_checks':link_checks,'live_formal_or_registration_changes':[],
            'new_behavior_execution':0,'reference_or_model_interpreter_run':False,'independent_review':'PENDING_NOT_SIGNED_BY_AUTHOR',
            'actual_integration':'WAIT_R5-U03','formal_acceptance':False,'CLOSED':False}
    if args.output:
        out=args.output.resolve()
        assert out.is_relative_to(author) or str(out).startswith('/tmp/'),out
        out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','operations','old_vector_rows','static_designs','mandatory_criterion_mappings','new_behavior_execution','actual_integration']}))

if __name__=='__main__':main()
