"""Recover exact C2 hash-addressed data bindings; never execute decoded files."""
from recover import T, C2, ident, save
import json,gzip,subprocess
def main():
    originals=T/'.work/originals'; recs=json.loads((originals/'0').read_text())['records'][1:13]
    bindings={}
    def walk(v):
        if isinstance(v,dict):
            if 'document' in v and 'sha256' in v and 'bytes' in v:
                bindings[v['sha256']]=v
            for x in v.values():walk(x)
        elif isinstance(v,list):
            for x in v:walk(x)
    for r in recs:walk(r)
    existing={ident(f.read_bytes())['sha256']:f.name for f in originals.iterdir()}
    receipts=[]
    for sha,f in bindings.items():
        if sha in existing:continue
        path='review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-transport/core/objects/'+sha[:2]+'/'+sha+'.gz'
        encoded=subprocess.check_output(['git','--git-dir='+str(T/'.work/remote.git'),'show',C2+':'+path]);b=gzip.decompress(encoded);a=ident(b)
        assert a['bytes']==f['bytes'] and a['sha256']==sha
        (originals/sha).write_bytes(b);receipts.append(dict(binding=f,encoded=ident(encoded),decoded=a,path=path,credit=0))
    save(T/'extra-recovery.json',receipts);print('extra inert originals',len(receipts));print('\n'.join(x['binding']['document'] for x in receipts))
if __name__=='__main__':main()
