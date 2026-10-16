"""Independent inert restoration and exact-value reading views. No restored code runs.

Rendering only creates evidence. An explicit ack with a reviewer explanation follows
actual display of every continuous part. A prior author's reading state is never used.
"""
from pathlib import Path
import argparse, datetime, gzip, hashlib, json, re, subprocess

T = Path(__file__).resolve().parent
W = T / '.work'
C2 = '4580645dfbfec4a3c7ccbad56ae293cc619b0d25'
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def canon(v): return json.dumps(v, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
def sha(b): return hashlib.sha256(b).hexdigest()
def ident(b): return {'bytes':len(b), 'sha256':sha(b), 'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def save(p,v): p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def pointer(v,p):
    for x in p.split('/')[1:]:
        x=x.replace('~1','/').replace('~0','~'); v=v[int(x)] if isinstance(v,list) else v[x]
    return v
def state():
    p=T/'view-state.json'
    return json.loads(p.read_text()) if p.exists() else {'pool':{},'pending':{},'acks':[], 'metadata':[]}
def load(i):
    p=W/'originals'/str(i)
    return json.loads(p.read_text()) if p.suffix=='.json' else json.loads(p.read_text())
def add(v,p,s):
    s['pool'].setdefault(sha(canon(v)),p)
    if isinstance(v,dict):
        for k,x in v.items():add(x,p+'/'+k.replace('~','~0').replace('/','~1'),s)
    elif isinstance(v,list):
        for n,x in enumerate(v):add(x,p+'/'+str(n),s)
def render(v,p,s,local):
    h=sha(canon(v))
    if len(canon(v))>100:
        if h in s['pool']: return {'=':h[:12]}
        if h in local: return {'=':h[:12]}
        local[h]=p
    if isinstance(v,dict):
        locator_keys={'repository_id','commit','tree','path','bytes','sha256','git_blob','scope','binding_id','inventory_member_ref','original_locator_ref','semantic_reading_inherited'}
        if 'repository_id' in v and 'path' in v and set(v).issubset(locator_keys) and isinstance(v.get('scope'),dict) and set(v['scope']).issubset({'lines','byte_offsets'}):
            s['metadata'].append({'pointer':p,'value':v,'purpose':'exact source/spec locator identity only; no reading of target or behavior credit'})
            return {'@locator':len(s['metadata'])-1}
        refkeys={'document','sha256','bytes','json_pointer','original_report_path','binding_id','canonical_sha256','input_sha256','raw_member_byte_offsets','raw_member_bytes','raw_member_sha256','file','file_bytes','file_sha256'}
        if set(v).issubset(refkeys) and ('document' in v or 'binding_id' in v or 'file_sha256' in v):
            s['metadata'].append({'pointer':p,'value':v,'purpose':'complete immutable binding; target body has no reading credit'})
            return {'@':len(s['metadata'])-1}
        if set(v)=={'字段','完整值引用'}:
            s['metadata'].append({'pointer':p,'value':v,'purpose':'exact field-to-immutable-pointer index; no target-body reading credit'})
            return {'@':len(s['metadata'])-1,'field':v['字段']}
        out={}
        for k,x in v.items():
            q=p+'/'+k.replace('~','~0').replace('/','~1')
            if (k in {'bytes','file_bytes','raw_member_bytes','raw_member_byte_offsets','byte_offsets','mode','logical_posix_mode','git_blob','git_blob_content_id','identity_id','transport_bytes','transport_git_blob_content_id'} or k.endswith('sha256')) and isinstance(x,(int,str,list)):
                s['metadata'].append({'pointer':q,'value':x,'purpose':'exact identity atom; no behavior credit'})
                out[k]={'#':len(s['metadata'])-1}
            else:out[k]=render(x,q,s,local)
        return out
    if isinstance(v,list):return [render(x,p+'/'+str(n),s,local) for n,x in enumerate(v)]
    return v
def main():
    ap=argparse.ArgumentParser();ap.add_argument('action');ap.add_argument('label',nargs='?');ap.add_argument('--file');ap.add_argument('--pointer',default='');ap.add_argument('--part',type=int,default=0);ap.add_argument('--note');a=ap.parse_args();W.mkdir(exist_ok=True)
    if a.action=='restore':
        inv=json.loads((T/'recovered-target/material-inventory.json').read_text());dest=W/'originals';dest.mkdir();receipts=[]
        for r in inv:
            encoded_path=r.get('transport_path',r['path'])
            raw=subprocess.check_output(['git','show',C2+':'+encoded_path]);data=gzip.decompress(raw) if r.get('transport_path') else raw
            actual=ident(data)
            for k in ['bytes','sha256']:assert actual[k]==r[k],(r['index'],k)
            assert actual['git_blob']==r.get('git_blob',r.get('actual_git_blob'))
            (dest/str(r['index'])).write_bytes(data)
            receipts.append({'input':r,'decoded':actual,'remote_path':encoded_path,'encoded':ident(raw),'local':str((dest/str(r['index'])).relative_to(T)),'credit':0})
        save(T/'original-recovery.json',{'utc':now(),'commit':C2,'files':receipts,'credit':0});print('restored',len(receipts));return
    s=state();(T/'views').mkdir(exist_ok=True)
    if a.action=='prepare':
        assert re.fullmatch('[a-zA-Z0-9_-]+',a.label) and a.label not in s['pending']
        obj=pointer(load(a.file),a.pointer);anchor=f'file{a.file}#{a.pointer}';txt=json.dumps(render(obj,anchor,s,{}),ensure_ascii=False,separators=(',',':'))
        parts=[txt[n:n+9500] for n in range(0,len(txt),9500)] or ['']; paths=[]
        for n,p in enumerate(parts):
            q=T/'views'/f'{a.label}.{n}.txt';q.write_text(p);paths.append(str(q.relative_to(T)))
        s['pending'][a.label]={'file':a.file,'pointer':a.pointer,'anchor':anchor,'original_sha256':sha(canon(obj)),'display_sha256':sha(txt.encode()),'parts':paths,'shown':[],'prepared_utc':now()};print(a.label, len(parts),len(txt))
    elif a.action=='show':
        r=s['pending'][a.label];p=T/r['parts'][a.part];print('EXACT',a.label,a.part+1,'/',len(r['parts']),r['anchor']);print(p.read_text());r['shown'].append(a.part)
    elif a.action=='ack':
        r=s['pending'].pop(a.label);assert set(r['shown'])==set(range(len(r['parts']))) and a.note
        obj=pointer(load(r['file']),r['pointer']);assert sha(canon(obj))==r['original_sha256'];add(obj,r['anchor'],s)
        r.update(ack_utc=now(),reviewer_note=a.note,reading_status='EXACT_DISPLAY_READ_IDENTITY_SEPARATE',behavior='NOT_EXECUTED');s['acks'].append(r);print('ack',a.label)
    elif a.action=='status': print(json.dumps({'acknowledged':len(s['acks']),'pending':s['pending'],'metadata_atoms':len(s['metadata'])}))
    save(T/'view-state.json',s)
if __name__=='__main__':main()
