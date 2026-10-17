#!/usr/bin/env python3
"""Freeze file identities and R2 delta after all authorized author documents end."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
INV = HERE.parents[2]
ROOT = INV.parents[2]
PREVIOUS = 'a32873d2860b15d9f5e27727db8f131f4ec433b6'
BRANCH = 'codex/r8-disposition-tagging-20261017'
FORMAL = 'deliverables/final-specification-set'
B8_TREE = 'f292698cdd4a8e725525a9be6dc34b75faaf151e'
PREFIX = str(INV.relative_to(ROOT)) + '/'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def identity(data):
    try:
        lines = len(data.decode('utf-8').splitlines())
    except UnicodeDecodeError:
        lines = None
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'lines': lines,
            'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}


def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def main():
    assert git('branch', '--show-current').decode().strip() == BRANCH
    assert git('rev-parse', 'HEAD').decode().strip() == PREVIOUS, 'Freeze must occur before final commit'
    changed = set(git('diff', '--name-only', PREVIOUS).decode().splitlines())
    changed.update(git('ls-files', '--others', '--exclude-standard').decode().splitlines())
    outside = sorted(path for path in changed if not path.startswith(PREFIX))
    assert not outside, outside
    formal_worktree_diff = git('diff', '--name-only', '--', FORMAL).decode().splitlines()
    formal_index_diff = git('diff', '--cached', '--name-only', '--', FORMAL).decode().splitlines()
    formal_tree = git('rev-parse', 'HEAD:' + FORMAL).decode().strip()
    assert formal_tree == B8_TREE and not formal_worktree_diff and not formal_index_diff
    refs = git('ls-remote', 'origin', 'refs/heads/main', 'refs/heads/' + BRANCH).decode().splitlines()
    remote = {line.split('\t')[1]: line.split('\t')[0] for line in refs}
    assert remote['refs/heads/' + BRANCH] == PREVIOUS, 'Remote author work changed; refuse overwrite'
    proof = {'schema_version':'routing-r3-pre-publication-protection.v1',
             'role':'AUTHOR_READ_ONLY_PROTECTION_CHECK; not review approval',
             'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
             'branch':BRANCH,'head_before_publication':PREVIOUS,'remote_before_publication':remote,
             'working_formal_tree':formal_tree,'formal_worktree_changes':formal_worktree_diff,
             'formal_index_changes':formal_index_diff,'changed_paths_outside_independent_inventory':outside,
             'authorized_publication':'Commit and fast-forward push only this independent branch; no main merge, force or deletion',
             'all_passed':True}
    save(HERE/'pre-publication-protection.json',proof)
    old_paths = git('ls-tree', '-r', '--name-only', PREVIOUS, '--', str(INV.relative_to(ROOT))).decode().splitlines()
    prior = {path: identity(git('show',PREVIOUS+':'+path)) for path in old_paths}
    current_paths = {str(path.relative_to(ROOT)):path for path in INV.rglob('*') if path.is_file() and '__pycache__' not in path.parts}
    manifest_path = str((INV/'candidate-file-manifest.json').relative_to(ROOT))
    delta_path = str((INV/'revisions/r3/changes-from-r2.json').relative_to(ROOT))
    excluded = {manifest_path,delta_path}
    changes = []
    for path in sorted(set(prior)|set(current_paths)):
        if path in excluded:
            continue
        current = identity(current_paths[path].read_bytes()) if path in current_paths else None
        old = prior.get(path)
        if old != current:
            changes.append({'path':path,'change':'ADD' if old is None else ('DELETE' if current is None else 'MODIFY'),
                            'previous':old,'current':current})
    assert not any(x['change']=='DELETE' for x in changes), 'No data deletion authorized'
    save(ROOT/delta_path,{'schema_version':'routing-r3-exact-file-delta.v1','previous_candidate':PREVIOUS,
        'current_commit_binding':'New exact Git commit supplied in parent handoff; no self-referential future SHA',
        'identity_exclusions':{'paths':sorted(excluded),'reason':'The delta excludes its own bytes and the enclosing identity manifest; both are independently bound by the final Git commit, and the enclosing manifest includes this delta.'},
        'semantic_field_delta':'revisions/r3/source-refinement-patch.json; exact post-source input plus162 before/after fields, verified as complete object by preservation-results.json',
        'source_field_delta':'revisions/r3/tools/accepted-backfill-result.json;131 exact current identities,736 locators and9 raw receipt-bound events; historical source unchanged',
        'counts':{'changed_payload_files':len(changes),'added':sum(x['change']=='ADD' for x in changes),
                  'modified':sum(x['change']=='MODIFY' for x in changes),'deleted':0},'files':changes})
    paths=sorted(p for p in INV.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p != INV/'candidate-file-manifest.json')
    entries=[{'path':str(path.relative_to(ROOT)),**identity(path.read_bytes())} for path in paths]
    save(INV/'candidate-file-manifest.json',{'schema_version':'routing-candidate-file-manifest.v3',
        'source_delivery_commit':'4575e80d041ab0c74a42e2e36399d05791dbaa5b','previous_candidate':PREVIOUS,
        'candidate_commit_binding':'Parent handoff supplies final40-hex Git commit; this file does not invent a future self SHA',
        'self_identity':'This manifest excludes itself; verify its exact Git blob/bytes at the fixed candidate commit',
        'binary_line_count':'lines:null for binary files; bytes/sha256/git_blob still exact',
        'files':entries,'payload_file_count':len(entries)})
    for entry in entries:
        assert identity((ROOT/entry['path']).read_bytes()) == {k:entry[k] for k in ['bytes','sha256','lines','git_blob']}
    print(json.dumps({'payload_files':len(entries),'total_files_including_identity_manifest':len(entries)+1,
                      'delta_counts':json.loads((ROOT/delta_path).read_text())['counts'],
                      'all_file_identities_verified':True,'remote_before_publication':remote},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
