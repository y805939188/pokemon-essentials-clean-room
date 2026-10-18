#!/usr/bin/env python3
"""Mechanical provenance-carrier navigation only; no reader/FULL/config credit."""
import argparse,array,collections,gzip,hashlib,importlib.util,io,json,pathlib,re,subprocess,sys
sys.dont_write_bytecode=True
OUT=pathlib.Path(__file__).resolve().parent;ROOT=OUT.parents[4]
A="fd414a2c6ec0a0f746b48e0924e5692221ea5d5a";B="8ab43a609e60430492b219f0dce14ef4fdb8e47f";BASE="review/remediation-eighth-20261016-prepare"
def module(name,file):
 s=importlib.util.spec_from_file_location(name,OUT/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
nav=module("nav","reading-navigation-build.py");storage=module("provenance_storage","provenance-reading-storage.py")
ALLOWLIST=("repo","commit","tree","workspace_tree","report_tree","formal_tree","path","pointer","json_pointer","mode","blob","bytes","sha256")
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*args):return subprocess.check_output(["git",*args],cwd=ROOT)
def compact(v):return json.dumps(v,ensure_ascii=False,separators=(",",":"))
def write(name,value):return storage.write_payload(OUT/("provenance-reading-"+name),(json.dumps(value,ensure_ascii=False,indent=2)+"\n").encode())
def write_lines(name,rows):return storage.write_payload(OUT/("provenance-reading-"+name),"".join(compact(r)+"\n" for r in rows).encode())
def load_tree():
 rows=[]
 for line in git("ls-tree","-rl",A,"--",BASE).decode().splitlines():
  meta,path=line.split("\t");mode,kind,blob,size=meta.split();rows.append({"path":path,"mode":mode,"kind":kind,"blob":blob,"bytes":int(size)})
 return rows
def batch_bytes(rows):
 blobs=list(dict.fromkeys(r["blob"] for r in rows));raw=subprocess.run(["git","cat-file","--batch"],cwd=ROOT,input="".join(x+"\n" for x in blobs).encode(),capture_output=True,check=True).stdout;s=io.BytesIO(raw);data={}
 for blob in blobs:
  header=s.readline().decode().split();assert header[:2]==[blob,"blob"];n=int(header[2]);data[blob]=s.read(n);assert s.read(1)==b"\n"
 assert not s.read();return {r["path"]:data[r["blob"]] for r in rows}
def main():
 parser=argparse.ArgumentParser();parser.add_argument("--sources-only",action="store_true");args=parser.parse_args()
 manifest=json.loads(git("show",B+":"+BASE+"/final/independent-review-input.json"))
 coordinator_names={"task-registry.json","candidate-review-receptions.json","six-actual-r1-reception.json","U06-actual-continuation-reception.json","U04-r2-final-publication-reception.json","U04-r2-pending-publication.json","continuation-delivery-20261017.json","first-two-candidate-checks.json","ownership-and-dependency-checks.json","optional-disposition.json","catalog-denominator-qualification.json"}
 def selected(path):
  return path.startswith(BASE+"/candidates/") or path.startswith(BASE+"/independent-reviews/") or path.startswith(BASE+"/reviews/") or (path.startswith(BASE+"/integration/") and not path.startswith(BASE+"/integration/tagging-")) or (path.startswith(BASE+"/acceptance/") and not path.startswith(BASE+"/acceptance/tagging-")) or (path.startswith(BASE+"/coordination/") and pathlib.PurePosixPath(path).name in coordinator_names)
 rows=[r for r in load_tree() if selected(r["path"])];assert not any("/reviews/final-ultra/" in r["path"] for r in rows)
 data=batch_bytes(rows);mechanical=json.loads(gzip.decompress((OUT/"final-mechanical.json.gz").read_bytes()));origins=collections.defaultdict(list)
 for i,g in enumerate(mechanical["nine_batch_source_groups"]):
  for f in g["files"]:
   assert f["full_bytes_equal"] and f["mode_blob_bytes_sha256_equal"];origins[f["source"]["path"]].append({"source_group_id":i,"source_commit":g["commit"],"source_prefix":g["prefix"],"source_identity":f["source"]})
 formal=[];documents=[]
 for i,r in enumerate(rows):
  b=data[r["path"]];assert len(b)==r["bytes"];r={"source_index":i,"artifact_commit":A,**r,"sha256":sha(b),"source_group_origins":origins[r["path"]]}
  if "/mirror/deliverables/final-specification-set/" in r["path"]:
   r["projection_disposition"]="FORMAL_CANDIDATE_MIRROR_SEPARATE_IDENTITY_SCOPE";r["formal_target_path"]="deliverables/final-specification-set/"+r["path"].split("/mirror/deliverables/final-specification-set/",1)[1];formal.append(r)
  else:r["projection_disposition"]="NONFORMAL_PROVENANCE_CARRIER_INCLUDED_LOSSLESS";documents.append(r)
 entries=[]
 for b in manifest["batches"]:
  def within(prefix):return [r["path"] for r in documents if r["path"].startswith(prefix)]
  candidateprefix=BASE+"/candidates/"+b["batch"]+"/";reviewprefix=str(pathlib.PurePosixPath(b["candidate_review_report"]["report_path"]).parent)+"/";actualprefix=str(pathlib.PurePosixPath(b["actual_integrated_review_report"]["report_path"]).parent)+"/"
  related=list(dict.fromkeys(within(candidateprefix)+within(reviewprefix)+within(actualprefix)))
  named=[p for p in related if any(s in pathlib.PurePosixPath(p).name.lower() for s in ("config","creation","qualification","startup"))]
  entries.append({"batch":b["batch"],"candidate_entry":{"commit":b["candidate_commit"],"path":b["candidate_manifest_path"],"kind":b["candidate_entry_kind"]},"candidate_independent_entry":b["candidate_review_report"],"actual_independent_entry":b["actual_integrated_review_report"],"accepted_entry":b["batch_ACCEPTED_receipt"],"author_thread_id_from_manifest":b["author_thread_id"],"candidate_reviewer_thread_id_from_manifest":b["independent_reviewer_thread_id"],"actual_reviewer_context_from_manifest":b["actual_integrated_review_report"].get("context"),"configuration_or_creation_filename_navigation":named,"configuration_creation_common_registry":BASE+"/coordination/task-registry.json","full_nonformal_related_paths":related})
 source_report={"schema":"r8-final-provenance-reading-source-selection/v1","qualification":"MECHANICAL_NAVIGATION_ONLY_NO_SEMANTIC_FULL_OR_CONFIG_CREDIT","input_binding":B,"artifact":A,"selection_rule":"All nine-batch candidate and independent-review directories; all fixed artifact reviews (none are current final review); all non-tagging integration and acceptance directories; the named eleven nine-batch coordination/creation/reception records. Entire source directories include predecessor failures and historical qualifications. Formal candidate mirrors are separately enumerated by the exact mirror/deliverables/final-specification-set path segment, not content; the U07 review/navigation mirror remains included.","included_nonformal_document_count":len(documents),"included_nonformal_bytes":sum(r["bytes"] for r in documents),"separately_enumerated_formal_candidate_mirrors":len(formal),"formal_mirror_bytes":sum(r["bytes"] for r in formal),"total_path_count":len(rows),"all_source_paths":[r["path"] for r in rows],"nonformal_documents":documents,"formal_candidate_mirror_identity_scope":formal,"batch_reader_config_create_report_entries":entries,"named_common_coordination_files":sorted(coordinator_names),"reading_credit_note":"Paths, role names, prior ledger claims, config fields and creation receipts are navigation only. Requested/created/runtime configuration and independent readers are judged only by the root; no source locator or old reader FULL is transferred."}
 write("sources.json",source_report);print(json.dumps({"source_paths":len(rows),"nonformal_documents":len(documents),"nonformal_bytes":source_report["included_nonformal_bytes"],"formal_mirrors_separate":len(formal),"sources_entry":"provenance-reading-sources.json"}));sys.stdout.flush()
 if args.sources_only:return
 unique=[];unique_index={};nodes=[];shells=[];shell_index={};virtual=[];parse_failures=[];byteindexes={}
 def bytepos(path):
  if path not in byteindexes:
   t=data[path].decode();pos=array.array("Q",[0]);n=0
   for ch in t:n+=len(ch.encode());pos.append(n)
   byteindexes[path]=pos
  return byteindexes[path]
 def add_json(path,name,text,base=0):
  value,ns=nav.Parser(text,base).parse();bi=bytepos(path);whole=data[path].decode()
  for pointer,n in ns.items():
   start,end=n["unicode_start"],n["unicode_end"];row={"document":name,"source_path":path,**n,"byte_start":bi[start],"byte_end":bi[end],"raw_token_sha256":sha(whole[start:end].encode())}
   if "value" in row:
    val=row.pop("value");key=(n["type"],compact(val))
    if key not in unique_index:unique_index[key]=len(unique);unique.append({"value_index":len(unique),"type":n["type"],"value":val,"occurrences":[]})
    vi=unique_index[key];row["value_index"]=vi;unique[vi]["occurrences"].append({"document":name,"source_path":path,"pointer":pointer,"unicode_start":start,"unicode_end":end})
   nodes.append(row)
  root=ns[""];virtual.append({"document":name,"source_path":path,"unicode_start":root["unicode_start"],"unicode_end":root["unicode_end"],"node_count":len(ns),"parsed_value_sha256":sha(compact(value).encode())})
  return value
 def add_shell(path,start,end):
  t=data[path].decode()[start:end];offset=start;bi=bytepos(path)
  for part in re.split(r"(\n[ \t]*\n)",t):
   if not part:continue
   if part not in shell_index:shell_index[part]=len(shells);shells.append({"shell_index":len(shells),"text":part,"bytes":len(part.encode()),"sha256":sha(part.encode()),"whitespace_only":not bool(part.strip()),"occurrences":[]})
   shells[shell_index[part]]["occurrences"].append({"source_path":path,"unicode_start":offset,"unicode_end":offset+len(part),"byte_start":bi[offset],"byte_end":bi[offset+len(part)]});offset+=len(part)
  assert offset==end
 for d in documents:
  path=d["path"];text=data[path].decode("utf-8");d["unicode_characters"]=len(text)
  if path.endswith(".json"):
   add_json(path,path,text);d["format"]="JSON"
  elif path.endswith(".jsonl"):
   pos=0;count=0
   for li,line in enumerate(text.splitlines(keepends=True)):
    if line.strip():add_json(path,path+"#jsonl/"+str(li),line,pos);count+=1
    else:add_shell(path,pos,pos+len(line))
    pos+=len(line)
   assert pos==len(text);d["format"]="JSONL";d["JSONL_values"]=count
  else:
   try:
    json.loads(text)
   except (json.JSONDecodeError,ValueError):
    pos=0;fences=0
    for fi,m in enumerate(re.finditer(r"^```json\n([\s\S]*?)\n```",text,re.M)):
     try:json.loads(m[1])
     except (json.JSONDecodeError,ValueError) as ex:parse_failures.append({"source_path":path,"fence_index":fi,"failure":"Fenced json text is not a complete JSON value; retained unchanged in nonJSON shell.","parser_message":str(ex)});continue
     if pos<m.start():add_shell(path,pos,m.start())
     add_shell(path,m.start(),m.start(1));add_json(path,path+"#json-fence/"+str(fi),m[1],m.start(1));add_shell(path,m.end(1),m.end());pos=m.end();fences+=1
    if pos<len(text):add_shell(path,pos,len(text))
    d["format"]="NONJSON_TEXT_WITH_JSON_FENCES" if fences else "NONJSON_TEXT";d["JSON_fences"]=fences
   else:add_json(path,path,text);d["format"]="COMPLETE_JSON_VALUE_IN_TEXT_CARRIER"
 # Strict all-occurrence metadata exclusion; no content-based filtering.
 retained=[];excluded=[];useindex=[];stream=[];offset=0
 for v in unique:
  uses=[]
  for oc in v["occurrences"]:
   key=oc["pointer"].split("/")[-1].replace("~1","/").replace("~0","~") if oc["pointer"] else ""
   uses.append({**oc,"exact_terminal_key":key,"explicit_metadata_key":key in ALLOWLIST})
  record={**v,"occurrences":uses,"all_occurrences_explicit_metadata":all(u["explicit_metadata_key"] for u in uses)}
  if record["all_occurrences_explicit_metadata"]:excluded.append(record);continue
  ni=len(retained);body=v["value"] if v["type"]=="string" else compact(v["value"]);piece=f"[N{ni} V{v['value_index']} {v['type']} U{ni}]\n"+body+"\n";record.update(narrative_index=ni,projection_unicode_start=offset,projection_unicode_end=offset+len(piece));offset+=len(piece);stream.append(piece);retained.append(record);useindex.append({k:val for k,val in record.items() if k!="value"})
 shellstream=[];offset=0
 for s in shells:
  piece=f"[S{s['shell_index']}]\n"+s["text"]+"\n";s.update(projection_unicode_start=offset,projection_unicode_end=offset+len(piece));offset+=len(piece);shellstream.append(piece)
 outputs=[write_lines("nodes.jsonl",nodes),write_lines("values.jsonl",unique),write_lines("strict-narrative-use-index.jsonl",useindex),write_lines("strict-narrative-excluded.jsonl",excluded),write_lines("shells.jsonl",shells)]
 for name,parts in (("strict-narrative.txt",stream),("shell.txt",shellstream)):
  p=OUT/("provenance-reading-"+name);b="".join(parts).encode();p.write_bytes(b);outputs.append({"path":str(p.relative_to(ROOT)),"bytes":len(b),"sha256":sha(b),"unicode_characters":len(b.decode())})
 write("sources.json",source_report)
 counts={"included_nonformal_documents":len(documents),"formal_candidate_mirrors_separate":len(formal),"JSON_virtual_documents":len(virtual),"JSON_node_rows":len(nodes),"unique_typed_scalar_values":len(unique),"typed_scalar_occurrences":sum(len(v["occurrences"]) for v in unique),"retained_unique_typed_values":len(retained),"excluded_unique_typed_values":len(excluded),"unique_nonJSON_shell_paragraphs":len(shells),"nonJSON_shell_occurrences":sum(len(s["occurrences"]) for s in shells),"strict_narrative_unicode_characters":sum(map(len,stream)),"nonJSON_shell_unicode_characters":sum(map(len,shellstream))}
 write("inventory.json",{"schema":"r8-final-provenance-reading-lossless-navigation/v1","qualification":"MECHANICAL_NAVIGATION_ONLY_NO_SEMANTIC_FULL_OR_CONFIG_CREDIT","input_binding":B,"artifact":A,"source_list":"provenance-reading-sources.json","exact_metadata_terminal_key_allowlist":list(ALLOWLIST),"exclusion_rule":"Only exact final JSON pointer keys; omit a unique typed value from narrative iff every original occurrence key is in the closed allowlist. No value-content/path/hash heuristic. Every omitted original value and every original use retained in excluded carrier and all originals remain in values carrier.","counts":counts,"files":outputs,"JSON_virtual_documents":virtual,"nonJSON_json_fence_parse_failures_retained_as_shell":parse_failures,"prior_preexecution_failures_retained":"provenance-reading-preexecution-failure.json","no_full_credit":True,"no_business_Ruby_execution":True})
 print(json.dumps(counts));print("Provenance navigation generated; no semantic/FULL/config qualification assigned.")
if __name__=="__main__":main()
