#!/usr/bin/env python3
"""Print exact fixed-source values. Logs navigation only; never grants FULL credit."""
import argparse,datetime,hashlib,importlib.util,json,pathlib,subprocess,sys
sys.dont_write_bytecode=True
OUT=pathlib.Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("reading_navigation_builder",OUT/"reading-navigation-build.py");mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
P=argparse.ArgumentParser()
g=P.add_mutually_exclusive_group(required=True)
g.add_argument("--record",help="canonical contract ID or 0-based index")
g.add_argument("--document",help="contracts | global-prompt | global-manifest | accepted | history | policy | readset-U01...U09 | prompt-U01...U09 | reviewer-U01...U09")
g.add_argument("--path",help="exact handoff source path")
g.add_argument("--stream",choices=("values","shell","strict-narrative"))
g.add_argument("--value",type=int,help="unique exact typed scalar index")
g.add_argument("--shell",type=int,help="unique exact prompt shell paragraph index")
g.add_argument("--catalog",action="store_true")
P.add_argument("--pointer",default="",help="JSON pointer; exact source token is printed")
P.add_argument("--start",type=int,default=0,help="Unicode start within selected exact source/value/stream")
P.add_argument("--end",type=int,default=None,help="Unicode exclusive end within selected source/value/stream")
P.add_argument("--no-log",action="store_true")
a=P.parse_args();meta={"qualification":"TOOL_NAVIGATION_ONLY_NO_FULL_OR_SEMANTIC_CREDIT","artifact":mod.ARTIFACT}
if a.catalog:
 d=json.loads(mod.raw(mod.HANDOFF+"/contracts.zh.json"));selected="\n".join(json.dumps({"index":i,"id":r["id"],"pointer":"/records/"+str(i),"classification":r["classification"],"severity":r["severity"],"keys":list(r)},ensure_ascii=False) for i,r in enumerate(d["records"]))+"\n";meta["selection"]="contract_catalog_only"
elif a.stream:
 selected=(OUT/("reading-navigation-"+a.stream+".txt")).read_text();meta["selection"]="lossless_exact_deduplicated_"+a.stream+"_projection"
elif a.value is not None or a.shell is not None:
 kind="values" if a.value is not None else "shell-paragraphs";i=a.value if a.value is not None else a.shell
 rows=[json.loads(line) for line in mod.storage.read_text(OUT/("reading-navigation-"+kind+".jsonl")).splitlines()];r=rows[i]
 selected=(r["value"] if r["type"]=="string" else mod.encoded(r["value"])) if a.value is not None else r["text"]
 meta.update(selection=kind,index=i,occurrences=r["occurrences"])
else:
 aliases={"contracts":"contracts.zh.json","global-prompt":"cloud-eighth-update-handoff-prompt.md","global-manifest":"cloud-eighth-update-handoff-manifest.json","accepted":"accepted-facts-and-mandatory-companions.json","history":"history-qualifications.json","policy":"policy-and-preservation.json"}
 if a.record is not None:path=mod.HANDOFF+"/contracts.zh.json"
 elif a.path:path=a.path
 elif a.document in aliases:path=mod.HANDOFF+"/"+aliases[a.document]
 else:
  kind,unit=a.document.split("-",1);assert unit in [f"U{i:02d}" for i in range(1,10)];name={"readset":"readset.json","prompt":"prompt.md","reviewer":"reviewer-prompt.md"}[kind];path=mod.HANDOFF+"/batches/R8-"+unit+"/"+name
 b=mod.raw(path);text=b.decode();meta.update(source_path=path,source_bytes=len(b),source_sha256=mod.sha(b));pointer=a.pointer
 inv=OUT/"reading-navigation-inventory.json"
 if inv.exists():
  expected=next(d for d in json.loads(inv.read_text())["documents"] if d["path"]==path);assert expected["bytes"]==len(b) and expected["sha256"]==mod.sha(b)
 if a.record is not None:
  d=json.loads(text);index=int(a.record) if a.record.isdigit() else next(i for i,r in enumerate(d["records"]) if r["id"]==a.record);pointer="/records/"+str(index);meta["record_id"]=d["records"][index]["id"]
 if pointer:
  d,nodes=mod.Parser(text).parse();n=nodes[pointer];selected=text[n["unicode_start"]:n["unicode_end"]];meta.update(pointer=pointer,source_token_unicode_start=n["unicode_start"],source_token_unicode_end=n["unicode_end"])
 else:selected=text
end=len(selected) if a.end is None else a.end
assert 0<=a.start<=end<=len(selected),(a.start,end,len(selected))
chunk=selected[a.start:end];meta.update(selected_unicode_characters=len(selected),returned_unicode_start=a.start,returned_unicode_end=end,returned_characters=len(chunk),returned_bytes=len(chunk.encode()),returned_sha256=mod.sha(chunk.encode()))
print(json.dumps(meta,ensure_ascii=False));sys.stdout.write(chunk);sys.stdout.write("\n")
if not a.no_log:
 with (OUT/"reading-navigation-tool-navigation.jsonl").open("a") as f:f.write(json.dumps({"at_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),**meta},ensure_ascii=False)+"\n")
