"""Fetch the published report into a new isolated bare repo and read every byte.

The original checkout is never used as an object alternate. A verification is
transport evidence, not semantic review. No push or source checkout is made.
"""
import argparse
import datetime
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess

def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def identity(raw):
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
            'git_blob': hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}

def main():
    ap=argparse.ArgumentParser()
    for k in ('remote','branch','commit','report-root','bare-dir','output'):
        ap.add_argument('--'+k, required=True)
    a=ap.parse_args()
    bare=Path(a.bare_dir).resolve(); out=Path(a.output).resolve()
    if bare.exists() or out.exists():
        raise FileExistsError('new bare directory and receipt required')
    out.parent.mkdir(parents=True,exist_ok=True)
    logdir=out.parent/(out.name+'.commands')
    logdir.mkdir()
    commands=[]
    git_env=dict(os.environ)
    removed=[]
    for key in list(git_env):
        if key in ('GIT_DIR','GIT_WORK_TREE','GIT_COMMON_DIR','GIT_OBJECT_DIRECTORY','GIT_ALTERNATE_OBJECT_DIRECTORIES','GIT_INDEX_FILE','GIT_CONFIG','GIT_CONFIG_COUNT','GIT_CONFIG_PARAMETERS') or key.startswith(('GIT_CONFIG_KEY_','GIT_CONFIG_VALUE_')):
            git_env.pop(key);removed.append(key)
    git_env['GIT_OPTIONAL_LOCKS']='0'
    def run(argv):
        start=utc(); p=subprocess.run(argv,capture_output=True,env=git_env)
        stem=logdir/('command-'+str(len(commands)))
        stdout=Path(str(stem)+'.stdout');stderr=Path(str(stem)+'.stderr')
        with stdout.open('xb') as f:f.write(p.stdout)
        with stderr.open('xb') as f:f.write(p.stderr)
        commands.append({'argv':argv,'start_utc':start,'end_utc':utc(),
                         'exit_code':p.returncode,'stdout':str(stdout),'stderr':str(stderr)})
        if p.returncode:
            failure=Path(str(out)+'.failed.json')
            with failure.open('x') as f:f.write(json.dumps(commands,ensure_ascii=False,indent=2)+'\n')
            raise RuntimeError(p.stderr.decode(errors='replace'))
        return p.stdout
    run(['git','init','--bare',str(bare)])
    run(['git','-C',str(bare),'fetch','--no-tags','--depth=1',a.remote,'refs/heads/'+a.branch])
    if (bare/'objects/info/alternates').exists():raise RuntimeError('unexpected bare object alternates file')
    fetched=run(['git','-C',str(bare),'rev-parse','FETCH_HEAD']).decode().strip()
    if fetched!=a.commit:
        raise RuntimeError('remote report branch differs from expected publication')
    tree=run(['git','-C',str(bare),'rev-parse',a.commit+'^{tree}']).decode().strip()
    subtree=run(['git','-C',str(bare),'rev-parse',a.commit+':'+a.report_root]).decode().strip()
    listing=run(['git','-C',str(bare),'ls-tree','-r','-z',a.commit,'--',a.report_root])
    entries=[]
    for entry in listing.split(b'\0'):
        if not entry: continue
        meta,path=entry.split(b'\t',1); mode,kind,oid=meta.decode().split()
        if kind!='blob': raise RuntimeError('unexpected report tree member kind')
        entries.append((mode,oid,path.decode()))
    indexes=[]; object_targets={}
    for mode,oid,path in entries:
        if path.endswith('/payload-index.json') and '/publication-transport/' in path:
            index=json.loads(run(['git','-C',str(bare),'show',a.commit+':'+path]))
            indexes.append((path,index))
            prefix=str(Path(path).parent)
            first={}
            for v in index['logical_files']: first.setdefault(v['sha256'],v)
            for obj in index['compressed_objects']:
                object_targets[prefix+'/'+obj['transport_path']]=(obj,first[obj['sha256']])
    batch_argv=['git','-C',str(bare),'cat-file','--batch']
    start=utc(); error_path=logdir/'cat-file.stderr'
    members=[]; decoded=[]; checked={}
    with error_path.open('xb') as err:
        child=subprocess.Popen(batch_argv,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=err,env=git_env)
        try:
            for mode,oid,path in entries:
                child.stdin.write((oid+'\n').encode()); child.stdin.flush()
                header=child.stdout.readline().decode().strip().split()
                if len(header)!=3 or header[:2]!=[oid,'blob']:
                    raise RuntimeError('invalid cat-file header')
                size=int(header[2]); raw=child.stdout.read(size)
                if len(raw)!=size or child.stdout.read(1)!=b'\n':
                    raise RuntimeError('truncated remote blob')
                ident=identity(raw)
                if ident['git_blob']!=oid: raise RuntimeError('remote blob identity mismatch')
                members.append({'path':path,'mode':mode,**ident})
                if path in object_targets:
                    obj,logical=object_targets[path]
                    for k in ('bytes','sha256'):
                        if ident[k]!=obj['transport_'+k]: raise RuntimeError('encoded identity mismatch')
                    if ident['git_blob']!=obj['transport_git_blob_content_id']:
                        raise RuntimeError('encoded Git blob mismatch')
                    digest=hashlib.sha256(); bid=hashlib.sha1(b'blob '+str(logical['bytes']).encode()+b'\0'); count=0
                    with gzip.GzipFile(fileobj=io.BytesIO(raw)) as stream:
                        while chunk:=stream.read(1024*1024):
                            count+=len(chunk); digest.update(chunk); bid.update(chunk)
                    checked[logical['sha256']]={'bytes':count,'sha256':digest.hexdigest(),'git_blob_content_id':bid.hexdigest()}
            child.stdin.close(); exit_code=child.wait()
        except BaseException as error:
            if child.poll() is None:child.terminate()
            try:exit_code=child.wait(timeout=5)
            except subprocess.TimeoutExpired:child.kill();exit_code=child.wait()
            failure={'status':'REMOTE_READBACK_FAILED','error':repr(error),'commands':commands,
                     'cat_file':{'argv':batch_argv,'start_utc':start,'end_utc':utc(),'exit_code':exit_code,'stderr':str(error_path)},
                     'verified_partial_members':members,'qualification':'Failure retained; no success receipt generated.'}
            with Path(str(out)+'.failed.json').open('x') as f:f.write(json.dumps(failure,ensure_ascii=False,indent=2)+'\n')
            raise
    if exit_code: raise RuntimeError('cat-file failed')
    commands.append({'argv':batch_argv,'start_utc':start,'end_utc':utc(),'exit_code':exit_code,
                     'stdin':'ordered full blob OID set from ls-tree; listed in members',
                     'stdout':'all binary bytes streamed through SHA256/Git-blob validation; not duplicated',
                     'stderr':str(error_path)})
    bypath={v['path']:v for v in members}
    for index_path,index in indexes:
        prefix=str(Path(index_path).parent)
        objects={v['sha256']:v for v in index['compressed_objects']}
        for logical in index['logical_files']:
            h=logical['sha256']; obj=objects[h]; path=prefix+'/'+obj['transport_path']
            actual=bypath[path]
            for k in ('bytes','sha256'):
                if actual[k]!=obj['transport_'+k]: raise RuntimeError('encoded identity mismatch')
            if actual['git_blob']!=obj['transport_git_blob_content_id']:
                raise RuntimeError('encoded Git blob mismatch')
            if h not in checked: raise RuntimeError('compressed payload was not fully read')
            if any(logical[k]!=checked[h][k] for k in ('bytes','sha256','git_blob_content_id')):
                raise RuntimeError('decoded logical identity mismatch')
            decoded.append({'index_path':index_path,'logical_path':logical['logical_path'],
                            **checked[h],'actual_encoded_tree_member':path,'status':'FULL_DECODED_BYTES_VERIFIED'})
    result={'schema':'r7.full-remote-readback.v1','status':'FULL_REMOTE_READBACK_VERIFIED',
            'completed_utc':utc(),'remote':a.remote,'branch':a.branch,'publication_commit':a.commit,
            'workspace_tree':tree,'report_root':a.report_root,'report_tree':subtree,
            'isolated_bare_repository':str(bare),'object_alternates_used':False,
            'git_environment_redirect_keys_removed':removed,'alternates_file_absent':True,
            'physical_members':members,'decoded_logical_members':decoded,
            'counts':{'physical_files':len(members),'logical_files':len(decoded),'unique_decoded_payloads':len(checked)},
            'commands':commands,'qualification':'Complete remote transport byte readback only; no semantic or behavior execution credit.'}
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'counts':result['counts'],'publication_commit':a.commit}))

if __name__=='__main__': main()
