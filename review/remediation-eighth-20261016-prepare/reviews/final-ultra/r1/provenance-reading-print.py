#!/usr/bin/env python3
"""Exact mechanical navigation printer; never grants FULL or semantic credit."""
import argparse,datetime,importlib.util,json,pathlib,subprocess,sys
sys.dont_write_bytecode=True
OUT=pathlib.Path(__file__).resolve().parent;ROOT=OUT.parents[4]
def module(name,file):
 spec=importlib.util.spec_from_file_location(name,OUT/file);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod
nav=module("nav","reading-navigation-build.py");storage=module("provenance_storage","provenance-reading-storage.py")
P=argparse.ArgumentParser();g=P.add_mutually_exclusive_group(required=True)
g.add_argument("--role",help="R8-U01...R8-U09 exact role entry navigation");g.add_argument("--metadata",choices=("sources","inventory","checks","role-entries","compression-map"));g.add_argument("--stream",choices=("strict-narrative","shell"));g.add_argument("--document",help="exact included source path, virtual JSON document name or source_index integer");g.add_argument("--value",type=int);g.add_argument("--shell",type=int);g.add_argument("--use-index",type=int);g.add_argument("--sources",action="store_true")
P.add_argument("--pointer",default="");P.add_argument("--start",type=int,default=0);P.add_argument("--end",type=int);P.add_argument("--no-log",action="store_true");a=P.parse_args();meta={"qualification":"TOOL_NAVIGATION_ONLY_NO_SEMANTIC_FULL_OR_CONFIG_CREDIT","artifact":"fd414a2c6ec0a0f746b48e0924e5692221ea5d5a"}
if a.role or a.metadata:
 name="role-entries" if a.role else a.metadata;value=json.loads(storage.read_text(OUT/("provenance-reading-"+name+".json")))
 if a.role:value=next(r for r in value["batches"] if r["batch"]==a.role)
 if a.pointer:
  for key in a.pointer.split("/")[1:]:
   key=key.replace("~1","/").replace("~0","~");value=value[int(key)] if isinstance(value,list) else value[key]
 selected=json.dumps(value,ensure_ascii=False,indent=2);meta.update(selection="derived_navigation_metadata",metadata=name,role=a.role,pointer=a.pointer)
elif a.stream:selected=(OUT/("provenance-reading-"+a.stream+".txt")).read_text();meta["selection"]="exact_deduplicated_"+a.stream+"_projection"
elif a.sources:
 source=json.loads((OUT/"provenance-reading-sources.json").read_text());selected="".join(r["path"]+"\n" for r in source["nonformal_documents"]);meta["selection"]="all_nonformal_source_paths"
elif a.value is not None or a.shell is not None or a.use_index is not None:
 name="values" if a.value is not None else "shells" if a.shell is not None else "strict-narrative-use-index";index=a.value if a.value is not None else a.shell if a.shell is not None else a.use_index;r=None
 for row_index,row in enumerate(storage.iter_jsonl(OUT/("provenance-reading-"+name+".jsonl"))):
  if row_index==index:r=row
 assert r is not None,index
 if a.value is not None:selected=r["value"] if r["type"]=="string" else nav.encoded(r["value"])
 elif a.shell is not None:selected=r["text"]
 else:selected=json.dumps(r,ensure_ascii=False,indent=2)
 meta.update(selection=name,index=index,occurrence_count=len(r.get("occurrences",[])))
else:
 source=json.loads((OUT/"provenance-reading-sources.json").read_text());docs=source["nonformal_documents"];name=a.document
 if name.isdigit():row=next(r for r in docs if r["source_index"]==int(name));path=row["path"];virtual=None
 else:
  path=name.split("#json",1)[0];row=next(r for r in docs if r["path"]==path);virtual=name if "#json" in name else None
 raw=subprocess.check_output(["git","show",meta["artifact"]+":"+path],cwd=ROOT);assert len(raw)==row["bytes"] and nav.sha(raw)==row["sha256"];whole=raw.decode();meta.update(source_path=path,source_sha256=row["sha256"],source_bytes=len(raw));start=0;end=len(whole)
 if virtual:
  inv=json.loads(storage.read_text(OUT/"provenance-reading-inventory.json"));v=next(v for v in inv["JSON_virtual_documents"] if v["document"]==virtual);start,end=v["unicode_start"],v["unicode_end"];meta["virtual_document"]=virtual
 if a.pointer:
  _,nodes=nav.Parser(whole[start:end],start).parse();n=nodes[a.pointer];start,end=n["unicode_start"],n["unicode_end"];meta["pointer"]=a.pointer
 selected=whole[start:end];meta.update(source_token_unicode_start=start,source_token_unicode_end=end)
end=len(selected) if a.end is None else a.end;assert 0<=a.start<=end<=len(selected),(a.start,end,len(selected));chunk=selected[a.start:end]
meta.update(selected_unicode_characters=len(selected),returned_unicode_start=a.start,returned_unicode_end=end,returned_bytes=len(chunk.encode()),returned_sha256=nav.sha(chunk.encode()));print(json.dumps(meta,ensure_ascii=False));sys.stdout.write(chunk);sys.stdout.write("\n")
if not a.no_log:
 with (OUT/"provenance-reading-tool-navigation.jsonl").open("a") as f:f.write(json.dumps({"at_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),**meta},ensure_ascii=False)+"\n")
