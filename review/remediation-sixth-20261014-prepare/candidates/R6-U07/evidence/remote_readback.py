#!/usr/bin/env python3
"""Read every changed candidate payload from its published immutable commit."""
import sys, json, hashlib, subprocess, urllib.request, urllib.parse
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor

commit = sys.argv[1]
out = Path(sys.argv[2]).resolve()
prefix = 'review/remediation-sixth-20261014-prepare/candidates/R6-U07'
base = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
branch = 'codex/remediation-sixth-r6-u07-author-20261014'
start = datetime.now(timezone.utc).isoformat()

def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'R6-U07-fixed-payload-readback'}), timeout=45) as r:
        return r.read()

api = 'https://api.github.com/repos/y805939188/pokemon-essentials-clean-room/git/'
tree = subprocess.check_output(['git','rev-parse',commit+'^{tree}'],text=True).strip()
subtree = subprocess.check_output(['git','rev-parse',commit+':'+prefix],text=True).strip()
remote_commit = json.loads(get(api+'commits/'+commit))
assert remote_commit['sha'] == commit and remote_commit['tree']['sha'] == tree
remote_tree = json.loads(get(api+'trees/'+subtree+'?recursive=1'))
assert remote_tree['sha'] == subtree and not remote_tree.get('truncated')
entries={prefix+'/'+x['path']:x for x in remote_tree['tree'] if x['type']=='blob'}
changed=subprocess.check_output(['git','diff','--name-only',base,commit],text=True).splitlines()
assert changed and all(x.startswith(prefix+'/') for x in changed)

def read(path):
    expected=subprocess.check_output(['git','show',commit+':'+path])
    url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path,safe='/')
    actual=get(url)
    blob=hashlib.sha1(b'blob '+str(len(actual)).encode()+b'\0'+actual).hexdigest()
    assert actual==expected and entries[path]['sha']==blob and entries[path]['mode']=='100644',path
    return {'path':path,'bytes':len(actual),'sha256':hashlib.sha256(actual).hexdigest(),
            'git_blob':blob,'mode':entries[path]['mode'],'type':entries[path]['type'],
            'url':url,'full_remote_bytes_equal':True}

with ThreadPoolExecutor(max_workers=6) as pool:
    rows=list(pool.map(read,changed))
ref=subprocess.check_output(['git','ls-remote','--heads','origin',branch],text=True).strip()
assert ref.split()[0]==commit,ref
out.mkdir(parents=True,exist_ok=True)
receipt={'argv':sys.argv,'cwd':str(Path.cwd()),'utc_start':start,
         'utc_end':datetime.now(timezone.utc).isoformat(),'commit':commit,'tree':tree,
         'candidate_directory_tree':subtree,'remote_ref':ref,'remote_commit_url':remote_commit['url'],
         'remote_commit_parents':[x['sha'] for x in remote_commit['parents']],
         'changed_payload_count':len(rows),'payloads':rows,'undeclared_diff':[],
         'exit_code':0,'level':'TOOL_VALIDATION_FULL_REMOTE_PAYLOAD_READBACK',
         'semantic_review':False,'independent_review':'PENDING'}
dest=out/'remote-readback.json'
assert not dest.exists(),'Preserve previous receipt'
dest.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['commit','tree','candidate_directory_tree','changed_payload_count','exit_code']},ensure_ascii=False))
