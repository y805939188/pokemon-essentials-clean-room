"""Read only one published own-task tree and all its complete raw payloads."""
from pathlib import Path
import concurrent.futures, datetime, gzip, hashlib, json, subprocess, sys
import urllib.parse, urllib.request

TASK=Path(__file__).resolve().parents[1]
REPO=TASK.parents[4]
PREFIX=str(TASK.relative_to(REPO))
OWNER_REPO='y805939188/pokemon-essentials-clean-room'
COMMIT=sys.argv[1]
OUTPUT=TASK/'publication'/sys.argv[2]
assert len(COMMIT)==40 and all(x in '0123456789abcdef' for x in COMMIT)
assert OUTPUT.parent==TASK/'publication' and not OUTPUT.exists()

def get(url):
    request=urllib.request.Request(url,headers={'User-Agent':'r8-external-review-readback'})
    with urllib.request.urlopen(request,timeout=60) as resp:
        return resp.read()

def api(path):
    # GitHub API CONNECT is unavailable in this shell; these exact remote
    # responses were obtained with the authorized GitHub connector.
    key=path.replace('?recursive=1','_recursive_1').replace('/','_')+'.json'
    return json.loads((TASK/'publication/api-cache'/key).read_text())

def digest(data):
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}

commit=api('git/commits/'+COMMIT)
assert commit['sha']==COMMIT
tree=commit['tree']['sha'];chain=[]
for part in PREFIX.split('/'):
    listing=api('git/trees/'+tree)
    assert listing['sha']==tree and not listing.get('truncated',False)
    row=next(x for x in listing['tree'] if x['path']==part)
    assert row['type']=='tree' and row['mode']=='040000'
    chain.append({'parent_tree':tree,'path':part,'mode':row['mode'],'tree':row['sha']})
    tree=row['sha']
listing=api('git/trees/'+tree+'?recursive=1')
assert listing['sha']==tree and not listing.get('truncated',False)
remote={x['path']:x for x in listing['tree'] if x['type']=='blob'}
raw=subprocess.check_output(['git','ls-tree','-r','-z',COMMIT,'--',PREFIX],cwd=REPO)
local={}
for line in raw.split(b'\0'):
    if not line:continue
    header,path=line.decode().split('\t');mode,kind,sha=header.split()
    assert kind=='blob' and path.startswith(PREFIX+'/')
    local[path[len(PREFIX)+1:]]={'mode':mode,'sha':sha}
assert set(remote)==set(local)
catalog=json.loads((TASK/'payload-catalog.json').read_text())
expected_decoded={}
for row in catalog['rows']:
    z=row['input']
    expected_decoded[row['decoded_object']]={k:z[k] for k in ['bytes','sha256','git_blob']}
    if row['encoded_object']:expected_decoded[row['encoded_object']]={k:z[k] for k in ['bytes','sha256','git_blob']}
manifest=json.loads((TASK/'core-payload-manifest.json').read_text())
for row in manifest['rows']:
    if 'decoded_identity'in row:expected_decoded[row['path']]=row['decoded_identity']

def verify(path):
    row=remote[path];assert row['mode']==local[path]['mode'] and row['sha']==local[path]['sha']
    full=PREFIX+'/'+path
    url='https://raw.githubusercontent.com/'+OWNER_REPO+'/'+COMMIT+'/'+urllib.parse.quote(full,safe='/')
    data=get(url);actual=digest(data)
    assert actual['git_blob']==row['sha'] and actual['bytes']==row['size']
    local_bytes=subprocess.check_output(['git','show',COMMIT+':'+full],cwd=REPO)
    assert data==local_bytes
    out={'path':full,'mode':row['mode'],**actual,'raw_url':url,'complete_remote_readback':True}
    if path in expected_decoded:
        decoded=digest(gzip.decompress(data));assert decoded==expected_decoded[path]
        out['decoded_identity']=decoded;out['decoded_identity_verified']=True
    return out

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    rows=list(pool.map(verify,sorted(remote)))
out={'schema':'r8.external-r6-remote-readback.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'commit':COMMIT,'workspace_tree':commit['tree']['sha'],'task_directory_tree':tree,
     'tree_metadata_transport':'authorized GitHub connector; exact cached API JSON',
     'raw_blob_transport':'fresh HTTPS raw.githubusercontent.com complete bodies',
     'remote_tree_membership_chain':chain,'payloads':len(rows),'remote_bytes':sum(x['bytes'] for x in rows),
     'compressed_decoded_identity_verified':sum(x.get('decoded_identity_verified',False) for x in rows),
     'all_path_mode_blob_bytes_sha256_match':True,'remote_git_tree_truncated':False,'rows':rows,
     'semantic_credit_from_remote_readback':False,'status':'FULL_PUBLISHED_TASK_PAYLOAD_READBACK_VERIFIED'}
OUTPUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['rows','remote_tree_membership_chain']},ensure_ascii=False))
