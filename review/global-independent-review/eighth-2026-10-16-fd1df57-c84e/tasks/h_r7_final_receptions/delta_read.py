import sys,json,hashlib
from pathlib import Path
from read_projection import ROWS,prune,squash
base=int(sys.argv[1]);target=int(sys.argv[2]);a=json.load(open(ROWS[base]['local_path']));b=json.load(open(ROWS[target]['local_path']));receipts=[]
def delta(a,b,p=''):
 if a==b:
  raw=json.dumps(b,ensure_ascii=False,separators=(',',':')).encode();receipts.append({'from':'payload'+str(target)+'#'+p,'to':'payload'+str(base)+'#'+p,'canonical_bytes':len(raw),'canonical_sha256':hashlib.sha256(raw).hexdigest(),'basis':'Complete actual semantic values already read in this context at target pointer; no old PASS inheritance'})
  return {'_exact_same_currently_read_pointer':'payload'+str(base)+'#'+p}
 if isinstance(a,dict) and isinstance(b,dict):return {k:delta(a[k],v,p+'/'+k) if k in a else v for k,v in b.items()}
 if isinstance(a,list) and isinstance(b,list) and len(a)==len(b):return [delta(x,y,p+'/'+str(i)) for i,(x,y) in enumerate(zip(a,b))]
 return b
def compact(x):
 if isinstance(x,dict):return {k:compact(v) for k,v in x.items() if not (isinstance(v,dict) and set(v)=={'_exact_same_currently_read_pointer'})}
 if isinstance(x,list):return [compact(v) for v in x]
 return x
q=delta(a,b);admin=[];q=squash(prune(q,admin=admin));print(json.dumps(compact(q),ensure_ascii=False,indent=2))
Path(__file__).with_name('associations-'+str(base)+'-'+str(target)+'.json').write_text(json.dumps({'qualification':'Unchanged exact values already actually read here; all differing target fields must independently be read before recording credit','associations':receipts,'administrative_dispositions':admin},ensure_ascii=False,indent=2)+'\n')
