"""Bounded inert recovery of a fixed shard readset; never execute recovered files."""
from pathlib import Path
import argparse,hashlib,json,subprocess,gzip,io,datetime
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--readset',required=True);p.add_argument('--readset-sha256',required=True)
p.add_argument('--git-dir',required=True);p.add_argument('--dispatch-commit',required=True)
p.add_argument('--project-root',required=True);p.add_argument('--write-root',required=True)
a=p.parse_args();C=a.dispatch_commit
assert len(C)==40 and all(x in '0123456789abcdef'for x in C)
project=Path(a.project_root).resolve();W=Path(a.write_root)
assert not W.is_symlink() and not any(x.is_symlink()for x in W.parents)
W=W.resolve();raw=Path(a.readset).read_bytes();assert hashlib.sha256(raw).hexdigest()==a.readset_sha256
readset=json.loads(raw);assert W.relative_to(project).as_posix()==readset['exclusive_write_set'].rstrip('/')
W.mkdir(parents=True,exist_ok=True);dest=W/'inputs-recovered-1';assert not dest.exists();dest.mkdir()
G='--git-dir='+str(Path(a.git_dir).resolve());files=[]
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
for row in readset['exact_payloads']:
 ref=row.get('carrier_commit',C);assert len(ref)==40 and all(x in '0123456789abcdef'for x in ref)
 rel=Path(row['path']);assert not rel.is_absolute()and '..'not in rel.parts
 listing=subprocess.check_output(['git',G,'ls-tree','-z',ref,'--',row['path']]).split(b'\0');assert len([x for x in listing if x])==1
 meta,path=listing[0].split(b'\t',1);mode,typ,oid=meta.decode().split();assert path.decode()==row['path']and typ=='blob'and mode==row['mode']and oid==row['git_blob']
 b=subprocess.check_output(['git',G,'cat-file','blob',oid]);actual=ident(b)
 assert all(actual[k]==row[k]for k in actual)
 out=dest/'encoded'/row['sha256'];out.parent.mkdir(parents=True,exist_ok=True)
 if out.exists():assert out.read_bytes()==b
 else:out.write_bytes(b)
 item={'source':row,'actual_encoded':actual,'encoded_local_path':str(out.relative_to(W)),'credit':0,'executed':False}
 if 'decoded_identity'in row:
  expected=row['decoded_identity']
  with gzip.GzipFile(fileobj=io.BytesIO(b))as stream:d=stream.read(expected['bytes']+1)
  di=ident(d);assert all(di[k]==expected[k]for k in di)
  out=dest/'decoded'/expected['sha256'];out.parent.mkdir(parents=True,exist_ok=True)
  if out.exists():assert out.read_bytes()==d
  else:out.write_bytes(d)
  item.update(actual_decoded=di,decoded_local_path=str(out.relative_to(W)))
 files.append(item)
receipt={'schema':'gr8.h-early-fanout.inert-recovery/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'dispatch_commit':C,'dispatch_tree':subprocess.check_output(['git',G,'rev-parse',C+'^{tree}']).decode().strip(),'shard':readset['id'],'files':files,'count':len(files),'semantic_credit':0,'executed_restored_code':False}
(W/'input-recovery.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'shard':readset['id'],'file_count':len(files),'status':'ENCODED_AND_BOUNDED_DECODED_IDENTITIES_MATCH','semantic_credit':0}))
