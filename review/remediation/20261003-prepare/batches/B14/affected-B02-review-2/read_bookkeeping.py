"""New static document identity/range bookkeeping; no reference execution."""
import subprocess, json, hashlib, pathlib, os
OUT = pathlib.Path(__file__).parent
C3='c06db6cd964188b3c693a9b7820e3a8aaffe0b04'
C2='af39efbf32549be964cb083bd49bed6d1d5c0d2a'
BASE='1e6b11a47370f1c7c4659a32443fc1afda597bac'
GLOBAL='93e10babe0b9c9ef8b3f5277754541b447beeeb4'
PLAN='41fffb540c6483f5296ea0d33b789b75180d27ed'
PREV='6350e56d8d6e692caa0f8ba2e7f3e71789b34bd8'
SOURCE='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REF=os.environ.get('B14_REFERENCE_ROOT')
def git(*args, source=False):
    if source and not REF: raise ValueError('Supply the private reference materialization through B14_REFERENCE_ROOT; it is not a public report identity.')
    cmd=['git']+(['-C',REF] if source else [])+list(args)
    return subprocess.check_output(cmd)
def read(commit,path,source=False):
    return git('show',commit+':'+path,source=source)
def identity(commit,path,source=False):
    b=read(commit,path,source)
    return dict(commit=commit,path=path,git_blob=git('rev-parse',commit+':'+path,source=source).decode().strip(),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),lines=len(b.splitlines()))
def save(name,data):
    (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def emit(commit,path,start=1,end=None,source=False):
    b=read(commit,path,source); lines=b.decode().splitlines(); end=end or len(lines)
    print('DOCUMENT',commit,path,'RANGE',start,end,'OF',len(lines))
    for n in range(start,min(end,len(lines))+1): print(str(n)+': '+lines[n-1])
    log=OUT/'delivery-receipts.jsonl'
    with log.open('a') as f: f.write(json.dumps(dict(identity=identity(commit,path,source),start=start,end=min(end,len(lines)),semantic_read='MODEL_MUST_ATTEST_AFTER_DELIVERY',source=source))+'\n')
def obj(commit,path): return json.loads(read(commit,path))
def treepaths(commit,prefix=''): return git('ls-tree','-r','--name-only',commit,prefix).decode().splitlines()
def emit_diff_values(start,end):
    scopes=json.loads((OUT/'diff-manifest.json').read_text())
    entries=json.loads((OUT/'formal-diff-value-map.json').read_text())['entries']
    cache={}
    for ent in entries[start:end]:
        p=ent['locators'][0];key=(p['scope'],p['path'])
        if key not in cache:cache[key]=git('diff','--no-ext-diff','--no-textconv',scopes[p['scope']]['base'],C3,'--',p['path']).decode().splitlines()
        line=cache[key][p['patch_line']-1]
        print(ent['index'],line)
def emit_review_values(start,end):
    entries=json.loads((OUT/'review-payload-value-map.json').read_text())['entries'];cache={}
    for ent in entries[start:end]:
        if ent['known_control'] or ent['formal_line_duplicate'] or ent['identity_scalar']:continue
        ptr=ent['pointers'][0];path,loc=ptr.split('#',1)
        if path not in cache:cache[path]=obj(C3,path) if path.endswith('.json') else read(C3,path).decode().splitlines(keepends=True)
        v=cache[path]
        tokens=loc.strip('/').split('/')
        if not path.endswith('.json'): tokens=tokens[1:]
        for key in tokens:
            key=key.replace('~1','/').replace('~0','~')
            v=v[int(key)] if isinstance(v,list) else v[key]
        print(ent['id'],path.split('/B14/',1)[-1]+loc,json.dumps(v,ensure_ascii=False))
