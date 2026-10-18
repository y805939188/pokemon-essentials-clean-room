#!/usr/bin/env python3
"""Mechanical reconstruction and role/pointer navigation, never semantic credit."""
import array,collections,hashlib,importlib.util,json,pathlib,re,subprocess,sys
sys.dont_write_bytecode=True
OUT=pathlib.Path(__file__).resolve().parent;ROOT=OUT.parents[4]
def module(name,file):
 s=importlib.util.spec_from_file_location(name,OUT/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
build=module("provenance_build","provenance-reading-build.py");nav=build.nav;storage=build.storage
A=build.A;B=build.B;BASE=build.BASE
sources=json.loads((OUT/"provenance-reading-sources.json").read_text());inventory=json.loads(storage.read_text(OUT/"provenance-reading-inventory.json"));source_by_path={r["path"]:r for r in sources["nonformal_documents"]};data=build.batch_bytes(sources["nonformal_documents"]);texts={p:b.decode() for p,b in data.items()}
for path,row in source_by_path.items():
 assert len(data[path])==row["bytes"] and build.sha(data[path])==row["sha256"]
 for o in row["source_group_origins"]:
  src=o["source_identity"];assert all(src[k]==row[k] for k in ("path","mode","blob","bytes","sha256"))
values=[];original_uses=[];value_keys=set();scalar_occurrences=0
for v in storage.iter_jsonl(OUT/"provenance-reading-values.jsonl"):
 assert v["value_index"]==len(values);assert nav.typ(v["value"])==v["type"];key=(v["type"],nav.encoded(v["value"]));assert key not in value_keys;value_keys.add(key);values.append((v["type"],v["value"]));original_uses.append(build.sha(nav.encoded(v["occurrences"]).encode()));scalar_occurrences+=len(v["occurrences"])
config_keys={"model","model_request","model_requested","requested_model","actual_model","runtime_model","thinking","thinking_request","requested_thinking","reasoning_effort","requested_effort","requested_reasoning_effort","actual_effort","effort","service_tier","requested_service_tier","requested_tier","actual_tier","runtime_tier","tier","speed","Fast","fast","runtime_echo","runtime_authoritative_echo","authoritative_echo","configuration","requested_configuration","created_requested_configuration","configuration_request","configuration_evidence","creation_evidence","creation_request","parent_creation_evidence","parent_creation_receipt","admissionOutcome","admission_outcome","threadId","thread_id","turnId","turn_id","environmentConfigId","reader","reader_id","reader_context","reader_thread_id","context","context_id","independent_reader","independent_reviewer","author","author_context","author_thread_id","independent_from_author","actual_non_author_reviewer"}
config_by_path=collections.defaultdict(list);node_count=0;typed_nodes=0;doc_count=0;document=None;ns={};active_path=None;byte_index=None
virtual={v["document"]:v for v in inventory["JSON_virtual_documents"]}
def rebuild(nodes,p=""):
 n=nodes[p]
 if n["type"]=="object":return {k:rebuild(nodes,p+"/"+nav.esc(k)) for k in n["keys"]}
 if n["type"]=="array":return [rebuild(nodes,p+"/"+str(i)) for i in range(n["length"])]
 return values[n["value_index"]][1]
def finish_doc(name,nodes):
 global doc_count
 if name is None:return
 v=virtual[name];raw=texts[v["source_path"]][v["unicode_start"]:v["unicode_end"]];restored=rebuild(nodes);assert nav.encoded(restored)==nav.encoded(json.loads(raw));assert build.sha(nav.encoded(restored).encode())==v["parsed_value_sha256"];assert len(nodes)==v["node_count"];doc_count+=1
for n in storage.iter_jsonl(OUT/"provenance-reading-nodes.jsonl"):
 if n["document"]!=document:finish_doc(document,ns);document=n["document"];ns={}
 ns[n["pointer"]]=n;node_count+=1;path=n["source_path"];text=texts[path]
 if path!=active_path:
  active_path=path;byte_index=array.array("Q",[0]);p=0
  for c in text:p+=len(c.encode());byte_index.append(p)
 s,e=n["unicode_start"],n["unicode_end"];raw=text[s:e].encode();assert byte_index[s]==n["byte_start"] and byte_index[e]==n["byte_end"] and build.sha(raw)==n["raw_token_sha256"]
 if "value_index" in n:
  t,v=values[n["value_index"]];assert n["type"]==t;assert nav.encoded(json.loads(raw))==nav.encoded(v);typed_nodes+=1
 key=n["pointer"].split("/")[-1].replace("~1","/").replace("~0","~") if n["pointer"] else ""
 if key in config_keys:config_by_path[path].append({"document":n["document"],"json_pointer":n["pointer"],"exact_key":key,"type":n["type"],"source_unicode_start":s,"source_unicode_end":e,"source_byte_start":n["byte_start"],"source_byte_end":n["byte_end"],"raw_token_sha256":n["raw_token_sha256"]})
finish_doc(document,ns)
assert doc_count==len(virtual)==inventory["counts"]["JSON_virtual_documents"];assert node_count==inventory["counts"]["JSON_node_rows"];assert typed_nodes==scalar_occurrences==inventory["counts"]["typed_scalar_occurrences"]
strict=(OUT/"provenance-reading-strict-narrative.txt").read_text();shell=(OUT/"provenance-reading-shell.txt").read_text();seen=set();retained=0;excluded=0;last=0
for u in storage.iter_jsonl(OUT/"provenance-reading-strict-narrative-use-index.jsonl"):
 vi=u["value_index"];assert vi not in seen;seen.add(vi);t,v=values[vi];assert t==u["type"];assert u["narrative_index"]==retained
 orig=[{k:x[k] for k in ("document","source_path","pointer","unicode_start","unicode_end")} for x in u["occurrences"]];assert build.sha(nav.encoded(orig).encode())==original_uses[vi];assert not all(x["explicit_metadata_key"] for x in u["occurrences"])
 body=v if t=="string" else nav.encoded(v);piece=f"[N{retained} V{vi} {t} U{retained}]\n"+body+"\n";assert u["projection_unicode_start"]==last and strict[last:u["projection_unicode_end"]]==piece;last=u["projection_unicode_end"];retained+=1
for x in storage.iter_jsonl(OUT/"provenance-reading-strict-narrative-excluded.jsonl"):
 vi=x["value_index"];assert vi not in seen;seen.add(vi);assert (x["type"],nav.encoded(x["value"]))==(values[vi][0],nav.encoded(values[vi][1]));assert all(o["exact_terminal_key"] in build.ALLOWLIST and o["explicit_metadata_key"] for o in x["occurrences"])
 orig=[{k:o[k] for k in ("document","source_path","pointer","unicode_start","unicode_end")} for o in x["occurrences"]];assert build.sha(nav.encoded(orig).encode())==original_uses[vi];excluded+=1
assert len(seen)==len(values) and last==len(strict)
shell_count=0;shell_occ=0;last=0;shell_by_path=collections.defaultdict(list)
for s in storage.iter_jsonl(OUT/"provenance-reading-shells.jsonl"):
 assert s["shell_index"]==shell_count;piece=f"[S{shell_count}]\n"+s["text"]+"\n";assert s["projection_unicode_start"]==last and shell[last:s["projection_unicode_end"]]==piece;last=s["projection_unicode_end"]
 for o in s["occurrences"]:
  assert texts[o["source_path"]][o["unicode_start"]:o["unicode_end"]]==s["text"];assert data[o["source_path"]][o["byte_start"]:o["byte_end"]]==s["text"].encode();shell_by_path[o["source_path"]].append({"shell_index":shell_count,**o});shell_occ+=1
 shell_count+=1
assert last==len(shell)
manifest=json.loads(build.git("show",B+":"+BASE+"/final/independent-review-input.json"));registry_path=BASE+"/coordination/task-registry.json";registry=json.loads(texts[registry_path]);_,registry_nodes=nav.Parser(texts[registry_path]).parse()
def endpoint(path,pointer=None,source_commit=None):
 row=source_by_path[path];res={"path":path,"bytes":row["bytes"],"sha256":row["sha256"],"mode":row["mode"],"blob":row["blob"],"artifact_commit":A,"source_commit_from_manifest":source_commit,"json_pointer":pointer,"format":row["format"]}
 if pointer is not None:
  _,nodes=nav.Parser(texts[path]).parse();n=nodes[pointer];res.update(source_unicode_start=n["unicode_start"],source_unicode_end=n["unicode_end"],pointed_type=n["type"])
 else:res.update(source_unicode_start=0,source_unicode_end=len(texts[path]))
 return res
roles=[]
for i,b in enumerate(manifest["batches"]):
 bid=b["batch"];ci=b["candidate_review_report"];ai=b["actual_integrated_review_report"];ac=b["batch_ACCEPTED_receipt"];candidate_prefix=BASE+"/candidates/"+bid+"/";ci_prefix=str(pathlib.PurePosixPath(ci["report_path"]).parent)+"/";ai_prefix=str(pathlib.PurePosixPath(ai["report_path"]).parent)+"/"
 def config_entries(prefix):
  return [{"entry":endpoint(path,"" if source_by_path[path]["format"] in ("JSON","COMPLETE_JSON_VALUE_IN_TEXT_CARRIER") else None),"exact_matching_key_navigation":matches} for path,matches in config_by_path.items() if path.startswith(prefix)]
 ri=next(j for j,r in enumerate(registry["tasks"]) if r["batch"]==bid);registry_entries=[]
 for key in ("author","candidate","independent_review","actual_integration"):
  pointer=f"/tasks/{ri}/"+key
  if pointer in registry_nodes:registry_entries.append(endpoint(registry_path,pointer,A))
 role={"batch":bid,"manifest_record_json_pointer":"/batches/"+str(i),"candidate_manifest_or_change_record":endpoint(b["candidate_manifest_path"],"",b["candidate_commit"]),"candidate_independent_report":endpoint(ci["report_path"],None,ci["commit"]),"candidate_independent_result":endpoint(ci["result_path"],"",ci["commit"]),"candidate_directory_configuration_creation_reader_key_entries":config_entries(candidate_prefix),"candidate_review_directory_configuration_creation_reader_key_entries":config_entries(ci_prefix),"actual_independent_report":endpoint(ai["report_path"],None,ai["commit"]),"actual_independent_result":endpoint(ai["result_path"],"",ai["commit"]),"actual_review_directory_configuration_creation_reader_key_entries":config_entries(ai_prefix),"ACCEPTED_receipt":endpoint(ac["path"],ac["record_pointer"],ac["commit"]),"registry_author_candidate_independent_actual_objects":registry_entries,"nonJSON_report_complete_shell_navigation":{"candidate_report":shell_by_path[ci["report_path"]],"actual_report":shell_by_path[ai["report_path"]]}}
 roles.append(role)
build.write("role-entries.json",{"schema":"r8-final-provenance-role-entry-navigation/v1","qualification":"MECHANICAL_PATH_STRUCTURE_NAVIGATION_ONLY_NO_SEMANTIC_FULL_OR_CONFIG_CREDIT","input_binding":B,"artifact":A,"entry_rule":"Each role uses the exact final manifest path/commit. JSON roots/objects have real JSON pointers and exact source token ranges; Markdown has null JSON pointer and complete file/shell ranges. Config/create/reader keys are exact key-name navigation only, not eligibility or configuration authority. Parent/task request, created configuration and runtime echo remain distinct original fields; no interpretation is supplied.","exact_configuration_creation_reader_navigation_keys":sorted(config_keys),"batches":roles,"common_coordination_configuration_creation_reader_keys":[{"entry":endpoint(path,""),"exact_matching_key_navigation":config_by_path[path]} for path in sorted(config_by_path) if path.startswith(BASE+"/coordination/")]})
for entry in inventory["files"]:
 if pathlib.PurePosixPath(entry["path"]).suffix==".txt":
  p=ROOT/entry["path"];assert p.stat().st_size==entry["bytes"] and build.sha(p.read_bytes())==entry["sha256"]
checks={"schema":"r8-final-provenance-reading-reconstruction/v1","qualification":"MECHANICAL_RECONSTRUCTION_ONLY_NO_SEMANTIC_FULL_OR_CONFIG_CREDIT","input_binding":B,"artifact":A,"source_documents_whole_raw_identities_verified":len(source_by_path),"source_group_original_and_artifact_identities_equal":True,"JSON_virtual_documents_rebuilt_with_exact_typed_values_and_order":doc_count,"JSON_node_token_unicode_byte_ranges_and_raw_hash_verified":node_count,"typed_scalar_occurrences_verified_against_original_source":typed_nodes,"all_unique_typed_values_present_once":len(values),"strict_narrative_retained_values_original_exact_all_uses_and_offsets_verified":retained,"strict_narrative_excluded_values_original_exact_all_uses_and_metadata_key_rule_verified":excluded,"nonJSON_exact_shell_paragraphs_verified":shell_count,"nonJSON_exact_shell_occurrences_verified":shell_occ,"strict_narrative_unicode_characters":len(strict),"strict_narrative_sha256":build.sha(strict.encode()),"nonJSON_shell_unicode_characters":len(shell),"nonJSON_shell_sha256":build.sha(shell.encode()),"role_entries_with_exact_manifest_paths_bytes_and_real_pointers":len(roles),"all_checks_passed":True,"business_Ruby_execution":False,"new_semantic_reading_or_FULL_credit":False,"preexecution_failure_record_preserved":"provenance-reading-preexecution-failure.json"}
build.write("checks.json",checks);print(json.dumps(checks,ensure_ascii=False))
