#!/usr/bin/env python3
"""Freeze exact file deltas and candidate identities without self-hash cycles."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
INV = HERE.parents[1]
ROOT = INV.parents[2]
BASE = 'c0f62d973180679134f2eb1a488c1dc359c8658f'
R2 = 'a32873d2860b15d9f5e27727db8f131f4ec433b6'
BRANCH = 'codex/r8-r3-seven-line-recovery-20261017'
PREFIX = str(INV.relative_to(ROOT)) + '/'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def identity(data):
    try:
        lines = len(data.decode('utf-8').splitlines())
    except UnicodeDecodeError:
        lines = None
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'lines': lines,
            'git_blob': hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')


def main():
    assert git('branch', '--show-current').decode().strip() == BRANCH
    assert git('rev-parse', 'HEAD').decode().strip() == BASE
    changed = set(git('diff', '--name-only', BASE).decode().splitlines())
    changed.update(git('ls-files', '--others', '--exclude-standard').decode().splitlines())
    assert all(p.startswith(PREFIX) for p in changed), sorted(changed)
    assert not git('diff', BASE, '--', 'deliverables/final-specification-set', 'reference')
    refs = git('ls-remote', 'origin', 'refs/heads/main', 'refs/heads/codex/r8-disposition-tagging-20261017', 'refs/heads/'+BRANCH).decode().splitlines()
    remote = {line.split('\t')[1]: line.split('\t')[0] for line in refs}
    assert 'refs/heads/'+BRANCH not in remote, 'Recovery remote branch already exists; inspect before writing.'
    assert git('rev-parse', BASE+':deliverables/final-specification-set').decode().strip() == 'f292698cdd4a8e725525a9be6dc34b75faaf151e'
    assert json.loads((HERE/'command-io.json').read_bytes())['all_commands_exit_zero']
    assert json.loads((HERE/'repair-proof.json').read_bytes())['all_passed']
    save(HERE/'pre-publication-protection.json', {
        'schema_version':'routing-r3-repair-publication-protection.v1', 'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'branch':BRANCH, 'base_candidate':BASE, 'remote_before_publication':remote,
        'formal_tree':'f292698cdd4a8e725525a9be6dc34b75faaf151e', 'formal_and_reference_diff_empty':True,
        'changed_paths_outside_routing':[], 'authorized_action':'Ordinary push of this new independent branch only; no force, main/original-branch mutation or merge.',
        'post_push_requirement':'Fresh independent no-alternates clone, exact new commit, full-byte read of every routing file including self-excluded identity artifacts.',
        'all_passed':True})
    manifest_path = INV/'candidate-file-manifest.json'
    r2_delta = INV/'revisions/r3/changes-from-r2.json'
    c0_delta = HERE/'changes-from-c0.json'
    excluded = {str(p.relative_to(ROOT)) for p in [manifest_path, r2_delta, c0_delta]}
    current_paths = {str(p.relative_to(ROOT)):p for p in INV.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
    for commit, output in [(R2,r2_delta),(BASE,c0_delta)]:
        prior_paths = git('ls-tree','-r','--name-only',commit,'--',str(INV.relative_to(ROOT))).decode().splitlines()
        prior = {p:identity(git('show',commit+':'+p)) for p in prior_paths if p not in excluded}
        changes=[]
        for path in sorted((set(prior)|set(current_paths))-excluded):
            old=prior.get(path)
            cur=identity(current_paths[path].read_bytes()) if path in current_paths else None
            if old!=cur:
                assert cur is not None, 'No deletion authorized: '+path
                changes.append({'path':path,'change':'ADD' if old is None else 'MODIFY','previous':old,'current':cur})
        save(output, {'schema_version':'routing-r3-repair-exact-file-delta.v1','previous_candidate':commit,
            'current_commit_binding':'Final40-hex Git commit supplied by author handoff; no future self SHA.',
            'identity_exclusions':{'paths':sorted(excluded),'reason':'Both file deltas and enclosing manifest exclude cross/self hashes; exact final Git commit independently binds all three. Candidate manifest includes both deltas.'},
            'manifest_semantic_delta':'Exactly seven differences/1 leaves relative toc0; archive-to-final cumulative patch remains78 rows/162 fields.',
            'counts':{'changed_payload_files':len(changes),'added':sum(c['change']=='ADD' for c in changes),'modified':sum(c['change']=='MODIFY' for c in changes),'deleted':0},
            'files':changes})
    paths=sorted(p for p in INV.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p!=manifest_path)
    entries=[{'path':str(p.relative_to(ROOT)),**identity(p.read_bytes())} for p in paths]
    save(manifest_path, {'schema_version':'routing-candidate-file-manifest.v4','source_delivery_commit':'4575e80d041ab0c74a42e2e36399d05791dbaa5b',
        'previous_candidate':BASE,'previous_R2_candidate':R2,
        'candidate_commit_binding':'Final40-hex Git commit supplied by author handoff; no future self SHA.',
        'self_identity':'Excluded from own entries; verify exact blob and all bytes from final fixed Git commit.',
        'binary_line_count':'lines:null for binary; bytes/sha256/git_blob remain exact.',
        'files':entries,'payload_file_count':len(entries)})
    for row in entries:
        assert identity((ROOT/row['path']).read_bytes()) == {k:row[k] for k in ['bytes','sha256','lines','git_blob']}
    print(json.dumps({'payload_files':len(entries),'total_routing_files':len(entries)+1,
                      'changes_from_c0':json.loads(c0_delta.read_bytes())['counts'],
                      'remote_before_publication':remote,'all_file_identities_verified':True},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
