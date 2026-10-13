#!/usr/bin/env python3
"""Read every report blob from a freshly fetched remote object database.

This validates report artifacts, not reference behavior. It never fetches,
publishes, changes a checkout, or reads credentials itself.
"""
import argparse, datetime, hashlib, json, pathlib, subprocess

ap=argparse.ArgumentParser()
ap.add_argument('--git-dir',required=True)
ap.add_argument('--commit',required=True)
ap.add_argument('--output',required=True)
ap.add_argument('--branch',required=True)
ap.add_argument('--fetch-evidence',required=True)
a=ap.parse_args()
O=pathlib.Path(__file__).resolve().parents[1]
W=O.parents[2]
prefix=O.relative_to(W).as_posix()
gd=pathlib.Path(a.git_dir).resolve()
if (gd/'objects/info/alternates').exists():
 raise SystemExit('Refuse alternates: remote readback must use the separately fetched database.')
base=['git','--git-dir='+str(gd)]
def git(*args):return subprocess.check_output(base+list(args))
commit=git('rev-parse',a.commit+'^{commit}').decode().strip()
tree=git('rev-parse',commit+'^{tree}').decode().strip()
raw=git('ls-tree','-rz','-r',commit,'--',prefix+'/')
entries=[]
for row in raw.split(b'\0'):
 if not row:continue
 meta,path=row.split(b'\t',1);mode,kind,blob=meta.decode().split()
 if kind!='blob':raise SystemExit('Non-blob report entry: '+path.decode())
 entries.append((path.decode(),mode,blob))
if not entries:raise SystemExit('No report files in fetched commit.')
records=[];errors=[]
intended={p.relative_to(W).as_posix() for p in O.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and p.name!='.DS_Store'}
remote_paths={p for p,_,_ in entries}
missing_remote=sorted(intended-remote_paths)
unexpected_remote=sorted(remote_paths-intended)
errors.extend('missing remote artifact: '+p for p in missing_remote)
errors.extend('unexpected remote artifact: '+p for p in unexpected_remote)
proc=subprocess.Popen(base+['cat-file','--batch'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
for path,mode,blob in entries:
 proc.stdin.write((blob+'\n').encode());proc.stdin.flush()
 header=proc.stdout.readline().decode().strip().split()
 if len(header)!=3 or header[:2]!=[blob,'blob']:raise SystemExit('Unexpected batch header: '+repr(header))
 length=int(header[2]);remaining=length
 digest=hashlib.sha256();object_digest=hashlib.sha1(b'blob '+str(length).encode()+b'\0')
 while remaining:
  buf=proc.stdout.read(min(1024*1024,remaining))
  if not buf:raise SystemExit('Unexpected end of remote blob: '+path)
  digest.update(buf);object_digest.update(buf);remaining-=len(buf)
 if proc.stdout.read(1)!=b'\n':raise SystemExit('Missing object delimiter: '+path)
 local=W/path
 same=local.is_file() and local.stat().st_size==length and hashlib.sha256(local.read_bytes()).hexdigest()==digest.hexdigest()
 ok=object_digest.hexdigest()==blob and same
 records.append({'path':path,'mode':mode,'bytes':length,'sha256':digest.hexdigest(),'git_blob':blob,'remote_blob_read_in_full':True,'computed_git_blob_matches':object_digest.hexdigest()==blob,'local_artifact_same_bytes':same,'result':'PASS' if ok else 'FAIL'})
 if not ok:errors.append(path)
proc.stdin.close();code=proc.wait()
if code:errors.append('cat-file exit '+str(code))
receipt={'schema_version':'gr5.remote-full-byte-readback.v1','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repository':'https://github.com/y805939188/pokemon-essentials-clean-room','branch':a.branch,'commit':commit,'tree':tree,'report_prefix':prefix,'source':'fresh independent remote fetch; no object alternates','fetch_evidence':a.fetch_evidence,'method':'git cat-file --batch: every complete report blob streamed, size/SHA256/computed Git blob and local intended bytes compared','file_count':len(records),'total_bytes_read':sum(r['bytes']for r in records),'files':records,'errors':errors,'result':'PASS' if not errors else 'FAIL','evidence_level':'TOOL_VALIDATION','behavior_execution':False,'self_identity_rule':'This external result is not included recursively in the commit it verifies.'}
receipt['exact_file_set']={'intended_count':len(intended),'remote_count':len(remote_paths),'missing_remote':missing_remote,'unexpected_remote':unexpected_remote,'same':intended==remote_paths}
out=pathlib.Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:receipt[k]for k in ('commit','tree','file_count','total_bytes_read','result')},ensure_ascii=False))
raise SystemExit(1 if errors else 0)
