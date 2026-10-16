"""Inert source recovery and lossless reading views. No semantic credit is generated."""
from pathlib import Path
import subprocess,json,hashlib
T=Path(__file__).resolve().parent;P=T/'recovered/18d21310bdc360c87d7ffd886df7d06aef8604a7';V=T/'views';V.mkdir(exist_ok=True)
def dump(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
d=json.loads((P/'reading-ledger.json').read_text()); rows=d['primary']
extra=['Data/Scripts/005_Sprites/010_PictureEx.rb','Data/Scripts/010_Data/002_PBS data/009_Species_files.rb']
ids=[]
for r in rows+[{'path':p}for p in extra]:
 path=r['path']; raw=subprocess.check_output(['git','--git-dir=/tmp/r8-cp-reference-R.git','show','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:'+path]);oid=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest();sha=hashlib.sha256(raw).hexdigest()
 if 'git_blob'in r:assert oid==r['git_blob']and sha==r['sha256']and len(raw)==r['bytes']
 target=T/'reference-R'/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
 ids.append({'path':path,'local_path':str(target.relative_to(T)),'commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','mode':'100644','blob':oid,'bytes':len(raw),'sha256':sha,'lines':len(raw.splitlines()),'semantic_credit':0})
dump(T/'reference-identities.json',ids)
a=json.loads((P/'atomic-assertions.json').read_text());groups={}
for r in a['assertions']:groups.setdefault(r['group'],[]).append(r)
for g,rs in groups.items():dump(V/(g+'.json'),rs)
for name in ['release-variance-fields.json','capture-variance-fields.json','ball-color-fields.json']:
 d=json.loads((P/name).read_text()); lines=[json.dumps({k:v for k,v in d.items()if k!='records'},ensure_ascii=False,separators=(',',':'))]
 for r in d['records']:
  if 'fields'in r:
   lines.append(json.dumps({k:v for k,v in r.items()if k!='fields'},ensure_ascii=False,separators=(',',':')))
   for f in r['fields']:lines.append(json.dumps(f,ensure_ascii=False,separators=(',',':')))
  else:lines.append(json.dumps(r,ensure_ascii=False,separators=(',',':')))
 (V/(name+'.jsonl')).write_text('\n'.join(lines)+'\n')
print('Recovered inert R',len(ids),'source bytes',sum(x['bytes']for x in ids),'manual views',len(groups),'all views credit0')
