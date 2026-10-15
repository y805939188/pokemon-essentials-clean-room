import pathlib,json,hashlib,subprocess,datetime,time,io,gzip,re,collections,os
RR=pathlib.Path("review/global-independent-review/seventh-2026-10-14-e646432-7a91").resolve()
PROJECT=RR.parents[2];OUT=RR/"publication-staging/C21";PKG=RR/"handoff";CORE="28e0d9df6ca4f75de9773a502ebdaa177cc0752c"
REPORT_REL=str(RR.relative_to(PROJECT));PREFIX=REPORT_REL+"/publication-transport/core"
errors=[];checks={};gitnum=0;gitcommands=[]
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(name,x):(OUT/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n")
def ident(raw):return {"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"git_blob_content_id":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}
def equal(name,a,b):
 ok=a==b;checks[name]=ok
 if not ok:errors.append({"check":name,"actual_type":type(a).__name__,"expected_type":type(b).__name__})
 return ok
def git(*args):
 global gitnum
 argv=["git","-C",str(PROJECT),*args];name="git-read-"+str(gitnum).zfill(3);gitnum+=1;t=utc()
 p=subprocess.run(argv,capture_output=True)
 (OUT/"logs"/(name+".stdout")).write_bytes(p.stdout);(OUT/"logs"/(name+".stderr")).write_bytes(p.stderr)
 row={"argv":argv,"start_utc":t,"end_utc":utc(),"exit_code":p.returncode,"stdout":"logs/"+name+".stdout","stderr":"logs/"+name+".stderr"}
 dump("logs/"+name+".json",row);gitcommands.append(row)
 if p.returncode:raise RuntimeError(row)
 return p.stdout
core_ids={"commit":git("rev-parse",CORE+"^{commit}").decode().strip(),"workspace_tree":git("rev-parse",CORE+"^{tree}").decode().strip(),"report_path":REPORT_REL,"report_tree":git("rev-parse",CORE+":"+REPORT_REL).decode().strip()}
equal("core_commit",core_ids["commit"],CORE);equal("core_workspace",core_ids["workspace_tree"],"a2e8143f5f514ac8db5fcc36e8cbdaaaaf428133")
equal("core_report",core_ids["report_tree"],"3583466aef215439358c9578f956871afa1f98af")
equal("fixed_formal_tree",git("rev-parse",CORE+":deliverables/final-specification-set").decode().strip(),"ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c")
manifest_raw=(PKG/"cloud-seventh-update-handoff-manifest.json").read_bytes();M=json.loads(manifest_raw);members=json.loads((PKG/"package-members.json").read_bytes())
equal("manifest_core",M["core"],core_ids);equal("package_index_core",members["core"],core_ids)
index_raw=git("show",CORE+":"+PREFIX+"/payload-index.json");INDEX=json.loads(index_raw)
equal("manifest_full_core_index_object",M["all_core_logical_payloads"],INDEX)
equal("manifest_core_index_identity",{k:M["core_transport_index"][k] for k in ident(index_raw)},ident(index_raw))
LOGICAL={x["logical_path"]:x for x in INDEX["logical_files"]};OBJECTS={x["sha256"]:x for x in INDEX["compressed_objects"]}
equal("logical_count",len(INDEX["logical_files"]),34251);equal("unique_logical_paths",len(LOGICAL),34251);equal("object_count",len(INDEX["compressed_objects"]),21449);equal("unique_decoded_sha",len(OBJECTS),21449)
logical_binding_errors=[]
for row in INDEX["logical_files"]:
 obj=OBJECTS.get(row["sha256"])
 if obj is None or row["transport_path"]!=obj["transport_path"] or pathlib.PurePosixPath(row["transport_path"]).is_absolute() or ".." in pathlib.PurePosixPath(row["transport_path"]).parts:logical_binding_errors.append(row["logical_path"])
equal("all_logical_to_object_bindings",logical_binding_errors,[])
listing=git("ls-tree","-r","-z",CORE,"--",PREFIX)
TREE={}
for entry in listing.split(b"\0"):
 if not entry:continue
 meta,path=entry.split(b"\t",1);mode,kind,oid=meta.decode().split();TREE[path.decode()]={"mode":mode,"kind":kind,"oid":oid}
physical_binding_errors=[]
for obj in INDEX["compressed_objects"]:
 p=PREFIX+"/"+obj["transport_path"];t=TREE.get(p)
 if not t or t["kind"]!="blob" or t["oid"]!=obj["transport_git_blob_content_id"]:physical_binding_errors.append(p)
equal("all_encoded_tree_oid_bindings",physical_binding_errors,[])
batch_argv=["git","-C",str(PROJECT),"cat-file","--batch"]
request="".join(OBJECTS[h]["transport_git_blob_content_id"]+"\n" for h in sorted(OBJECTS)).encode();(OUT/"logs/encoded-objects.stdin").write_bytes(request)
t=utc();results=[];total=0
with (OUT/"logs/encoded-objects.stderr").open("wb") as err:
 child=subprocess.Popen(batch_argv,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=err)
 try:
  for h in sorted(OBJECTS):
   obj=OBJECTS[h];oid=obj["transport_git_blob_content_id"];child.stdin.write((oid+"\n").encode());child.stdin.flush()
   head=child.stdout.readline().decode().strip().split()
   if len(head)!=3 or head[:2]!=[oid,"blob"]:raise ValueError("invalid object header")
   size=int(head[2]);sha=hashlib.sha256();blob=hashlib.sha1(b"blob "+str(size).encode()+b"\0");n=0
   while n<size:
    b=child.stdout.read(min(1024*1024,size-n))
    if not b:raise ValueError("truncated object bytes")
    n+=len(b);sha.update(b);blob.update(b)
   if child.stdout.read(1)!=b"\n":raise ValueError("missing batch separator")
   ok=n==obj["transport_bytes"] and sha.hexdigest()==obj["transport_sha256"] and blob.hexdigest()==oid
   if not ok:errors.append({"check":"encoded_full_byte_identity","transport_path":obj["transport_path"]})
   results.append({"transport_path":obj["transport_path"],"decoded_sha256":h,"bytes":n,"sha256":sha.hexdigest(),"git_blob_content_id":blob.hexdigest(),"match":ok});total+=n
  child.stdin.close();code=child.wait()
 except BaseException:
  child.kill();code=child.wait();raise
batch_receipt={"argv":batch_argv,"start_utc":t,"end_utc":utc(),"exit_code":code,"stdin":"logs/encoded-objects.stdin","stdout":"Every encoded object byte consumed exactly once through SHA256/Git-blob calculation; full per-object results in encoded-object-full-byte-check.json; raw1GB not duplicated","stderr":"logs/encoded-objects.stderr"}
dump("logs/encoded-objects.command.json",batch_receipt);gitcommands.append(batch_receipt);equal("batch_exit",code,0)
dump("encoded-object-full-byte-check.json",{"objects":results,"count":len(results),"encoded_bytes_read":total,"qualification":"Full encoded bytes and all tree bindings only; this does not re-decompress all13.7GB historical platform archives or give semantic credit."})
core_decoded=[]
def core_read(rel):
 row=LOGICAL[rel];obj=OBJECTS[row["sha256"]];encoded=git("show",CORE+":"+PREFIX+"/"+row["transport_path"])
 ei=ident(encoded)
 if any(ei[k]!=obj["transport_"+k] for k in ei):raise ValueError("selected encoded mismatch "+rel)
 raw=gzip.decompress(encoded)
 if ident(raw)!={k:row[k] for k in ident(raw)}:raise ValueError("selected decoded mismatch "+rel)
 core_decoded.append({"logical_path":rel,**ident(raw),"actual_encoded_tree_member":PREFIX+"/"+row["transport_path"]})
 return raw
def core_json(rel):return json.loads(core_read(rel))
approval=core_json("evidence/final-root-reception.json")
equal("approval_actual_final_status",approval["status"],"FINAL_REVIEW_INPUT_ACCEPTED");equal("approval_pending",approval["pending"],[]);equal("approval_effective_unread",approval["effective_unread"],0)
for rel,expected in approval["accepted_payload_sha256"].items():equal("accepted_core_hash:"+rel,LOGICAL[rel]["sha256"],expected)
payload_map={"root_records":"findings.json","canonical_records":"canonical-records.json","complete_chinese_contracts":"tasks/R7-C13/chinese-contracts.json","batch_assignment":"batch-plan.final.json","dependency_graph":"dependency-graph.json","file_conflict_graph":"file-conflict-graph.json","fixed_inputs":"startup/fixed-inputs.json","optional_navigation_facets":"evidence/root-h22-counter/counter-review-and-facets.json"}
for key,rel in payload_map.items():equal("core_decoded_object:"+key,M[key],core_json(rel))
equal("section_names",set(M["coverage_and_qualification_sections"]),set(approval["json_sections"]))
for name,rel in approval["json_sections"].items():equal("core_decoded_section:"+name,M["coverage_and_qualification_sections"][name],core_json(rel))
rootmap={r["id"]:r for r in M["root_records"]["records"]};canmap={r["id"]:r for r in M["canonical_records"]["records"]};zhmap={r["id"]:r for r in M["complete_chinese_contracts"]["records"]}
equal("record_id_sets",set(rootmap),set(canmap));equal("chinese_record_id_set",set(rootmap),set(zhmap))
class_counts=dict(collections.Counter(r["classification"] for r in rootmap.values()));equal("37_classification_counts",class_counts,{"required":27,"optional":7,"no_required_revision":1,"policy":2})
group_errors=[]
for rid,r in rootmap.items():
 c=canmap[rid];z=zhmap[rid]
 if len(c["groups"])!=7 or len(z["groups"])!=7 or c["groups"]!=z["groups"] or c["classification"]!=r["classification"] or z["classification"]!=r["classification"] or c["severity"]!=r["severity"] or z["severity"]!=r["severity"]:group_errors.append(rid)
equal("all_37_classes_severities_seven_groups_equal_C13",group_errors,[])
sev=dict(collections.Counter(r["severity"] for r in rootmap.values() if r["classification"]=="required"));equal("required_severity",sev,{"P2":10,"P3":17})
plan=M["batch_assignment"];req={k for k,v in rootmap.items() if v["classification"]=="required"}
equal("primary_required_exact_set",set(plan["primary_batch_by_required"]),req);equal("batches13",len(plan["batches"]),13);equal("firstwave13",len(plan["first_wave"]),13);equal("firstwave_declared13",plan["first_wave_count"],13)
equal("no_tasks_launched",plan["tasks_launched"],0);equal("no_service_slots_claimed",plan["service_slots_claimed"],False)
equal("no_blocking_author_edges",M["dependency_graph"]["blocking_author_edges"],[])
fac=M["optional_navigation_facets"];equal("optional_facets2",len(fac["records"]),2);equal("facets_required_added0",fac["required_count_added"],0);equal("facets_new_roots0",fac["new_canonical_roots"],0);equal("facets_empty_required_writes",all(x["required_write_set"]==[] for x in fac["records"]),True)
equal("H08_embedded_optional_facets",rootmap["GR7-H08-001"]["optional_facets"],fac["records"])
files={str(p.relative_to(PKG)):p for p in PKG.rglob("*") if p.is_file()};declared={r["path"]:r for r in members["members"]}
equal("package32_plus_index33",set(files),set(declared)|{"package-members.json"});equal("package33_actual",len(files),33)
file_results=[]
for name,p in sorted(files.items()):
 raw=p.read_bytes();ii=ident(raw);match=name=="package-members.json" or all(ii[k]==declared[name][k] for k in ii)
 if not match:errors.append({"check":"package_member_full_byte_identity","path":name})
 file_results.append({"path":name,**ii,"listed_in_self_excluding_index":name in declared,"match":match})
dump("package-full-byte-check.json",{"files":file_results,"actual_files":len(files),"listed_files":len(declared),"index_self_identity_external_only":True})
main_raw=(PKG/"cloud-seventh-update-handoff-prompt.md").read_bytes();zh_body=core_read("tasks/R7-C13/chinese-handoff.md");fac_body=core_read("evidence/root-h22-counter/optional-navigation-facets.zh.md")
equal("full_C13_handoff_verbatim_in_prompt",zh_body in main_raw,True);equal("full_two_optional_facets_verbatim_in_prompt",fac_body in main_raw,True)
fences=[]
for b in re.findall(rb"```json[^\n]*\n(.*?)\n```",main_raw,re.S):
 try:fences.append(json.loads(b))
 except (ValueError,UnicodeDecodeError):pass
def walk(x):
 yield x
 if isinstance(x,dict):
  for v in x.values():yield from walk(v)
 elif isinstance(x,list):
  for v in x:yield from walk(v)
found=set()
for block in fences:
 for x in walk(block):
  if isinstance(x,dict) and x.get("id") in zhmap and x.get("groups")==zhmap[x["id"]]["groups"]:found.add(x["id"])
equal("all37_complete_group_objects_in_prompt_fences",found,set(zhmap))
for name in ["historical_qualifications","inherited_nonmandatory","limits","execution"]:equal("prompt_full_section:"+name,any(b==M["coverage_and_qualification_sections"][name] for b in fences),True)
inv=json.loads((PKG/"cli-invocations.json").read_bytes());expected={f"R7-U{i:02d}-{s}" for i in range(1,14) for s in ["A","R"]};equal("26_cli_unique_expected",{r["entry_id"] for r in inv},expected);equal("26_cli_rows",len(inv),26)
equal("26_prompt_file_set",{n for n in files if n.startswith("prompts/")},{"prompts/"+r["entry_id"][:-2]+"-"+r["role"]+".md" for r in inv})
equal("all_cli_not_started",all(r["status"]=="NOT_STARTED" for r in inv),True)
equal("all_actual_profiles_unverified",all(set(r["actual"].values())=={"UNVERIFIED"} for r in inv),True)
equal("future_paths_unverified",M["future_environment"]["actual_cloud_paths"],"UNVERIFIED_FUTURE_TASK_NOT_STARTED")
equal("manifest_update_not_started",M["update_started"],False)
summary={"schema":"r7.c21.actual-handoff-structure-check.v1","checked_utc":utc(),"core":core_ids,"manifest":ident(manifest_raw),"checks":checks,"errors":errors,"counts":{"records":len(rootmap),"classes":class_counts,"required_severities":sev,"logical_payloads":len(LOGICAL),"compressed_objects":len(OBJECTS),"encoded_object_bytes_read":total,"decoded_selected_inputs":len(core_decoded),"package_files":len(files),"CLI_entries":len(inv),"prompt_json_group_contracts_found":len(found)},"core_selected_decode_results":core_decoded,"git_commands":gitcommands,"next_inspection":{"canonical_status":M["canonical_records"]["status"],"plan_first_wave":plan["first_wave"],"batch_first_keys":list(plan["batches"][0]),"overlay":plan["nonmandatory_facet_overlay"],"c18_provenance":plan["c18_overlay_provenance"],"limits_section_keys":list(M["coverage_and_qualification_sections"]["limits"]),"inherited_keys":list(M["coverage_and_qualification_sections"]["inherited_nonmandatory"])},"qualification":"Complete actual handoff bytes/JSON structure, all encoded objects and all logical bindings; selected consumed core payloads fully decoded. No source semantic/global PASS or launcher/network/update."}
dump("structure-and-bytes-check.json",summary)
print(json.dumps({"errors":errors,"counts":summary["counts"],"failed_checks":[k for k,v in checks.items() if not v],"next_inspection":summary["next_inspection"]},ensure_ascii=False,indent=2))
