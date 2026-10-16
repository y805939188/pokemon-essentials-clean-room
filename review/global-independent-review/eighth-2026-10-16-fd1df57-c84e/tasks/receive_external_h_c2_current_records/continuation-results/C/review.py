"""Inert exact restoration and lossless displays; never imports restored programs."""
from pathlib import Path
import argparse, datetime, gzip, hashlib, json, os, subprocess

T = Path(__file__).resolve().parent
P = T.parent.parent
W = T / '.work'
TARGET = '967b90fac83a6b0c3313087d8871312b4eac18b9'
C2 = '4580645dfbfec4a3c7ccbad56ae293cc619b0d25'
REPO = 'https://github.com/y805939188/pokemon-essentials-clean-room.git'

def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def enc(v): return json.dumps(v, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
def ident(b): return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(), 'git_blob': hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def save(p,v): p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def git(*a): return subprocess.check_output(['git',*a])
def bg(*a): return git('--git-dir='+str(W/'remote.git'),*a)
def ptr(v,p):
    for k in p.split('/')[1:]:
        k=k.replace('~1','/').replace('~0','~');v=v[int(k)] if isinstance(v,list) else v[k]
    return v

def render(v,p,s,local):
    h=ident(enc(v))['sha256']
    if len(enc(v))>100:
        if h in s.get('pool',{}): return {'$exact_already_read_sha256':h}
        if h in local: return {'$exact_same_display_sha256':h}
        local[h]=p
    if isinstance(v,dict):
        if set(v)=={'字段','完整值引用'}:
            s.setdefault('typed_bindings',[]).append({'pointer':p,'value':v,'purpose':'FIELD_TO_IMMUTABLE_LOCATOR; target has zero reading credit'})
            return {'$field_binding':len(s['typed_bindings'])-1,'field':v['字段']}
        keys={'document','sha256','bytes','json_pointer','original_report_path','binding_id','canonical_sha256','input_sha256','raw_member_byte_offsets','raw_member_bytes','raw_member_sha256','file','file_bytes','file_sha256'}
        if set(v).issubset(keys) and {'document','binding_id','file'} & set(v):
            s.setdefault('typed_bindings',[]).append({'pointer':p,'value':v,'purpose':'EXACT_IDENTITY_LOCATOR; target has zero reading credit'})
            return {'$typed_binding':len(s['typed_bindings'])-1}
        return {k:render(x,p+'/'+k.replace('~','~0').replace('/','~1'),s,local) for k,x in v.items()}
    if isinstance(v,list): return [render(x,p+'/'+str(n),s,local) for n,x in enumerate(v)]
    return v

def pool(v,p,s):
    s.setdefault('pool',{}).setdefault(ident(enc(v))['sha256'],p)
    if isinstance(v,dict):
        for k,x in v.items():pool(x,p+'/'+k.replace('~','~0').replace('/','~1'),s)
    elif isinstance(v,list):
        for n,x in enumerate(v):pool(x,p+'/'+str(n),s)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('action');ap.add_argument('label',nargs='?');ap.add_argument('--file',type=int);ap.add_argument('--pointer',default='');ap.add_argument('--path');ap.add_argument('--part',type=int,default=0);ap.add_argument('--note');a=ap.parse_args()
    W.mkdir(exist_ok=True)
    if a.action=='restore':
        bare=W/'remote.git';assert not bare.exists()
        git('init','--bare',str(bare))
        # Reuse exact immutable old objects, then fetch the target independently.
        (bare/'objects/info/alternates').write_text(str(Path.cwd()/'.git/objects')+'\n')
        bg('fetch','--no-tags',REPO,TARGET)
        readset=json.loads((P/'continuation-v2/C.complete.json').read_text())
        assert bg('rev-parse',TARGET+'^{tree}').decode().strip()==readset['target_checkout_tree']
        source_root='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/external_h_c2_current_records'
        tree=bg('ls-tree','-rz',TARGET,source_root).split(b'\0')
        actual={x.split(b'\t',1)[1].decode() for x in tree if x};assert actual=={r['remote_path_at_target_commit'] for r in readset['files']}
        records=[]
        for r in readset['files']:
            b=bg('show',TARGET+':'+r['remote_path_at_target_commit']);i=ident(b)
            assert all(i[k]==r[k] for k in i)
            mode=bg('ls-tree',TARGET,r['remote_path_at_target_commit']).decode().split()[0];assert mode==r['mode']
            dest=W/'target'/r['relative_to_target_task'];dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
            records.append({**r,'actual':i,'actual_mode':mode,'credit':'IDENTITY_ONLY'})
        inv=json.loads((W/'target/material-inventory.json').read_text());original=[]
        (W/'originals').mkdir()
        for r in inv:
            path=r.get('transport_path',r['path']);raw=bg('show',C2+':'+path);data=gzip.decompress(raw) if r.get('transport_path') else raw;i=ident(data)
            assert i['bytes']==r['bytes'] and i['sha256']==r['sha256'] and i['git_blob']==r.get('git_blob',r.get('actual_git_blob'))
            (W/'originals'/str(r['index'])).write_bytes(data)
            original.append({'input':r,'encoded':ident(raw),'decoded':i,'remote_path':path,'credit':'IDENTITY_ONLY'})
        save(T/'recovery.json',{'utc':now(),'target':TARGET,'checkout_tree':readset['target_checkout_tree'],'target_task_tree':readset['target_task_tree_observed_from_fixed_commit'],'files':records,'original_C2':C2,'originals':original,'cache':'bare alternates reference existing exact local objects; target fetched from remote; no restored code executed','reading_credit':0})
        save(T/'independence.json',{'utc':now(),'CODEX_THREAD_ID':os.environ.get('CODEX_THREAD_ID','UNVERIFIED'),'CODEX_SESSION_ID':os.environ.get('CODEX_SESSION_ID','UNVERIFIED'),'target_author':'01a143b2-b02d-7094-808b-a4e9de51301b','parent_receiver':'01a14465-f204-7783-a526-9b43e91ea005','spawned':0,'configuration':{k:'UNVERIFIED' for k in ['model','effort','tier','speed','Fast']}})
        print('Restored',len(records),'target files and',len(original),'originals. Identity only.');return
    state_path=T/'display-ledger.json';s=json.loads(state_path.read_text()) if state_path.exists() else {'prepared':{},'reads':[]}
    if a.action=='prepare':
        assert a.label and a.label not in s['prepared']
        path=Path(a.path) if a.path else W/'originals'/str(a.file)
        data=path.read_bytes();v=ptr(json.loads(data),a.pointer) if a.file is not None or a.pointer or path.suffix=='.json' else data.decode()
        anchor=('file'+str(a.file) if a.file is not None else str(path.relative_to(T)) if path.is_relative_to(T) else str(path))+'#'+a.pointer
        txt=json.dumps(render(v,anchor,s,{}),ensure_ascii=False,separators=(',',':')) if not isinstance(v,str) else v
        parts=[txt[n:n+10000] for n in range(0,len(txt),10000)] or ['']
        (T/'views').mkdir(exist_ok=True)
        paths=[]
        for n,p in enumerate(parts):
            q=T/'views'/f'{a.label}.{n}.txt';q.write_text(p);paths.append(str(q.relative_to(T)))
        s['prepared'][a.label]={'path':str(path),'pointer':a.pointer,'source_identity':ident(data),'selected_value_identity':ident(enc(v)),'parts':paths,'shown':[],'ack':False};print(a.label,len(parts),len(txt))
    elif a.action=='show':
        r=s['prepared'][a.label];print('EXACT',a.label,a.part+1,'/',len(r['parts']),r['path'],r['pointer']);print((T/r['parts'][a.part]).read_text());r['shown'].append(a.part)
    elif a.action=='ack':
        r=s['prepared'][a.label];assert set(r['shown'])==set(range(len(r['parts']))) and a.note;r['ack']=True;r['note']=a.note;r['utc']=now();s['reads'].append(a.label)
        data=Path(r['path']).read_bytes()
        try:v=ptr(json.loads(data),r['pointer'])
        except json.JSONDecodeError:v=data.decode()
        assert ident(enc(v))==r['selected_value_identity'];pool(v,r['path']+'#'+r['pointer'],s);print('Read acknowledgement:',a.label)
    save(state_path,s)

if __name__=='__main__': main()
