#!/usr/bin/env python3
"""Lossless storage for new navigation outputs; never reading/semantic credit."""
import argparse,gzip,hashlib,json,pathlib,subprocess,sys
sys.dont_write_bytecode=True
OUT=pathlib.Path(__file__).resolve().parent
ROOT=OUT.parents[4]
MAP=OUT/"provenance-reading-compression-map.json"
THRESHOLD=1024*1024
def sha(data):return hashlib.sha256(data).hexdigest()
def mapping():
 return json.loads(MAP.read_text()) if MAP.exists() else {"schema":"r8-final-provenance-reading-lossless-compression/v1","qualification":"MECHANICAL_STORAGE_ONLY_NO_FULL_SEMANTIC_OR_CONFIG_CREDIT","input_binding":"8ab43a609e60430492b219f0dce14ef4fdb8e47f","artifact":"fd414a2c6ec0a0f746b48e0924e5692221ea5d5a","compression":"gzip level 9, mtime 0; original raw bytes retained by exact decompression","threshold_plain_bytes_strictly_greater_than":THRESHOLD,"scope":"Only this task's newly generated uncommitted provenance-reading-* JSON/JSONL carriers; no fixed input, old proof, projection txt or prior failure record removed.","entries":[]}
def save_mapping(m):
 temp=MAP.with_suffix(".json.tmp");temp.write_text(json.dumps(m,ensure_ascii=False,indent=2)+"\n");temp.replace(MAP)
def entry_for(path):
 return next((e for e in mapping()["entries"] if e["original_plain_name"]==path.name),None)
def ensure_untracked(path):
 result=subprocess.run(["git","ls-files","--error-unmatch","--",str(path.relative_to(ROOT))],cwd=ROOT,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 if result.returncode==0:raise RuntimeError("Refusing to remove tracked plain payload "+str(path))
def write_payload(path,data):
 path=pathlib.Path(path)
 if not (path.name.startswith("provenance-reading-") and path.suffix in (".json",".jsonl") and len(data)>THRESHOLD):
  path.write_bytes(data);return {"path":str(path.relative_to(ROOT)),"bytes":len(data),"sha256":sha(data)}
 ensure_untracked(path)
 m=mapping();old=next((e for e in m["entries"] if e["original_plain_name"]==path.name),None)
 if old is not None and (old["original_plain_bytes"]!=len(data) or old["original_plain_sha256"]!=sha(data)):
  raise RuntimeError("Refusing to overwrite original raw-byte identity in compression map: "+path.name)
 compressed=gzip.compress(data,compresslevel=9,mtime=0);assert gzip.decompress(compressed)==data
 gz=path.with_name(path.name+".gz");temp=gz.with_name(gz.name+".tmp");temp.write_bytes(compressed);assert gzip.decompress(temp.read_bytes())==data;temp.replace(gz)
 e={"original_plain_name":path.name,"original_plain_path":str(path.relative_to(ROOT)),"original_plain_bytes":len(data),"original_plain_sha256":sha(data),"gzip_name":gz.name,"gzip_path":str(gz.relative_to(ROOT)),"gzip_bytes":len(compressed),"gzip_sha256":sha(compressed),"decompressed_bytes":len(data),"decompressed_sha256":sha(gzip.decompress(compressed)),"exact_decompressed_bytes_equal_original":True,"plain_file_untracked_before_removal":True,"removed_only_new_recoverable_plain_derivative":True,"recovery":"gzip.decompress(Path(gzip_path).read_bytes()) returns the complete original raw bytes; verify original_plain_bytes and original_plain_sha256 before use."}
 if old is None:m["entries"].append(e)
 else:m["entries"][m["entries"].index(old)]=e
 save_mapping(m)
 if path.exists():
  assert path.read_bytes()==data;path.unlink()
 return {"path":str(path.relative_to(ROOT)),"bytes":len(data),"sha256":sha(data),"storage":"gzip","stored_path":str(gz.relative_to(ROOT)),"stored_bytes":len(compressed),"stored_sha256":sha(compressed),"compression_map":str(MAP.relative_to(ROOT))}
def read_bytes(path):
 path=pathlib.Path(path);e=entry_for(path)
 if path.exists():data=path.read_bytes()
 else:
  gz=path.with_name(path.name+".gz");compressed=gz.read_bytes()
  if e is not None:assert len(compressed)==e["gzip_bytes"] and sha(compressed)==e["gzip_sha256"]
  data=gzip.decompress(compressed)
 if e is not None:assert len(data)==e["original_plain_bytes"] and sha(data)==e["original_plain_sha256"]
 return data
def read_text(path):return read_bytes(path).decode("utf-8")
def iter_jsonl(path):
 path=pathlib.Path(path);e=entry_for(path);gz=path.with_name(path.name+".gz")
 if path.exists():stream=path.open("rb")
 else:
  compressed=gz.read_bytes()
  if e is not None:assert len(compressed)==e["gzip_bytes"] and sha(compressed)==e["gzip_sha256"]
  stream=gzip.open(gz,"rb")
 digest=hashlib.sha256();count=0
 with stream:
  for rawline in stream:
   digest.update(rawline);count+=len(rawline)
   if rawline.strip():yield json.loads(rawline)
 if e is not None:assert count==e["original_plain_bytes"] and digest.hexdigest()==e["original_plain_sha256"]
def verify_all():
 m=mapping();result=[]
 for e in m["entries"]:
  p=OUT/e["original_plain_name"];assert not p.exists()
  if p.suffix==".jsonl":row_count=sum(1 for _ in iter_jsonl(p))
  else:data=read_bytes(p);json.loads(data);row_count=None
  result.append({"name":p.name,"plain_absent":True,"gzip_present":True,"original_bytes":e["original_plain_bytes"],"original_sha256":e["original_plain_sha256"],"gzip_sha256":e["gzip_sha256"],"JSONL_rows":row_count,"raw_bytes_identity_and_JSON_parse_valid":True})
 return result
if __name__=="__main__":
 parser=argparse.ArgumentParser();parser.add_argument("--compress-new",action="store_true");parser.add_argument("--verify-all",action="store_true");args=parser.parse_args()
 if args.compress_new:
  for p in sorted(OUT.glob("provenance-reading-*")):
   if p.is_file() and p.suffix in (".json",".jsonl") and p.stat().st_size>THRESHOLD:write_payload(p,p.read_bytes())
 if args.verify_all:print(json.dumps({"qualification":"MECHANICAL_STORAGE_ONLY","entries":verify_all()},ensure_ascii=False))
