#!/usr/bin/env python3
"""Fetch from origin, fully read delivered reviewer blobs, compare exact bytes."""
import argparse
import datetime
import hashlib
import json
import pathlib
import subprocess

HERE = pathlib.Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p/'AGENTS.md').is_file())
PREFIX = str(HERE.relative_to(REPO)) + '/'
INPUT = '1dd05964f59772886de9b808a929c168c73fa184'
TASK = '7897037ae93af82aa9246a097c4badbd344a15b1'
BRANCH = 'codex/r4-u06-final-review-20261012-7897037'

def run(where, *args):
    return subprocess.check_output(['git', *args], cwd=where, stderr=subprocess.PIPE)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('commit')
    parser.add_argument('--store', required=True)
    parser.add_argument('--output', required=True)
    a = parser.parse_args()
    store = pathlib.Path(a.store)
    origin = run(REPO,'remote','get-url','origin').decode().strip()
    if not store.exists():
        store.mkdir(parents=True)
        run(store,'init','--bare')
        run(store,'remote','add','origin',origin)
        run(store,'config','remote.origin.promisor','true')
        run(store,'config','remote.origin.partialclonefilter','blob:none')
    assert run(store,'remote','get-url','origin').decode().strip() == origin
    assert not (store/'objects/info/alternates').exists()
    run(store,'fetch','--no-tags','--depth=1','--filter=blob:none','origin',a.commit)
    tree = run(store,'rev-parse',a.commit+'^{tree}').decode().strip()
    assert tree == run(REPO,'rev-parse',a.commit+'^{tree}').decode().strip()
    paths = run(store,'ls-tree','-r','--name-only',a.commit,PREFIX).decode().splitlines()
    local_paths = run(REPO,'ls-tree','-r','--name-only',a.commit,PREFIX).decode().splitlines()
    assert paths == local_paths and paths
    identities=[]
    for p in paths:
        remote = run(store,'show',a.commit+':'+p)
        local = run(REPO,'show',a.commit+':'+p)
        assert remote == local, p
        blob=run(store,'rev-parse',a.commit+':'+p).decode().strip()
        identities.append({'path':p,'bytes':len(remote),'sha256':hashlib.sha256(remote).hexdigest(),
                           'git_blob':blob,'full_remote_bytes_read':True,'byte_for_byte_local_commit_match':True})
        if p.endswith('.json'):
            json.loads(remote)
    formal_tree=run(store,'rev-parse',a.commit+':deliverables/final-specification-set').decode().strip()
    assert formal_tree == 'd5a462b4c6f8b78c3264a25d6b5495230fa265e2'
    changed=run(REPO,'diff','--name-only',TASK,a.commit).decode().splitlines()
    assert changed and all(p.startswith(PREFIX) for p in changed)
    advertisement=run(store,'ls-remote','origin','refs/heads/'+BRANCH,'refs/heads/main','refs/heads/codex/remediation-fourth-20261012-1f36475').decode().splitlines()
    refs={line.split('\t')[1]:line.split('\t')[0] for line in advertisement}
    assert refs['refs/heads/'+BRANCH] == a.commit
    result={'status':'PASS_COMPLETE_REMOTE_REVIEW_PAYLOAD','evidence_level':'TOOL_VALIDATION',
            'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'review_publication_commit':a.commit,'review_publication_tree':tree,
            'review_branch':BRANCH,'final_input_commit':INPUT,
            'final_input_tree':'778481a38dad208ebb54127ca3b4a58078c4bc0e',
            'task_publication_commit':TASK,'task_publication_tree':'f4026ead2457d3cccc693beb3bb240c69ec24cad',
            'independent_remote_object_store':str(store),'no_local_objects_or_alternates_copied':True,
            'fetch_policy':'Remote shallow partial clone; reviewer deliverables fetched and read completely; unrelated historical blobs not downloaded',
            'complete_delivery_files':len(identities),'complete_delivery_bytes':sum(x['bytes'] for x in identities),
            'file_identities':identities,'changed_paths_from_task':changed,
            'formal_tree_preserved':formal_tree,'formal131_identity_policy':'Exact unchanged formal subtree and prior signed full-byte identities reused; not new semantic or runtime signature',
            'remote_advertisement':refs,'registrar_branch_mutated_by_reviewer':False,
            'main_mutated_by_reviewer':False,'closed_registered_by_reviewer':0,
            'new_behavior_execution':{'reference':0,'model':0,'host_or_demo':0},'errors':[]}
    pathlib.Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','review_publication_commit','review_publication_tree','complete_delivery_files','complete_delivery_bytes','errors']}))

if __name__ == '__main__':
    main()
