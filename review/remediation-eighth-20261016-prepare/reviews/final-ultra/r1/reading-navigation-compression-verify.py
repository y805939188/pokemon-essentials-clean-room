#!/usr/bin/env python3
"""Mechanical gzip-only reconstruction regression; no source semantic reading."""
import ast,collections,hashlib,importlib.util,json,pathlib,subprocess,sys
sys.dont_write_bytecode=True
OUT=pathlib.Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("navigation_builder",OUT/"reading-navigation-build.py");nav=importlib.util.module_from_spec(spec);spec.loader.exec_module(nav);storage=nav.storage
inv=json.loads((OUT/"reading-navigation-inventory.json").read_text())
receipts={p.name:{"bytes":p.stat().st_size,"sha256":nav.sha(p.read_bytes())} for p in [OUT/"reading-navigation-inventory.json",OUT/"reading-navigation-self-checks.json",OUT/"reading-navigation-strict-narrative-self-checks.json",OUT/"reading-navigation-checks.json"]}
entries=storage.verify_all();assert len(entries)==4
values=[json.loads(l) for l in storage.read_text(OUT/"reading-navigation-values.jsonl").splitlines()]
nodes=[json.loads(l) for l in storage.read_text(OUT/"reading-navigation-nodes.jsonl").splitlines()]
bydoc=collections.defaultdict(dict)
for node in nodes:bydoc[node["document"]][node["pointer"]]=node
cache={d["path"]:nav.raw(d["path"]).decode() for d in inv["documents"]}
for d in inv["documents"]:assert len(cache[d["path"]].encode())==d["bytes"] and nav.sha(cache[d["path"]].encode())==d["sha256"]
def rebuild(ns,p=""):
 n=ns[p]
 if n["type"]=="object":return {k:rebuild(ns,p+"/"+nav.esc(k)) for k in n["keys"]}
 if n["type"]=="array":return [rebuild(ns,p+"/"+str(i)) for i in range(n["length"])]
 return values[n["value_index"]]["value"]
for name,ns in bydoc.items():
 r=rebuild(ns);n=ns[""];t=cache[n["source_path"]];assert nav.encoded(r)==nav.encoded(json.loads(t[n["unicode_start"]:n["unicode_end"]]))
summary=json.loads((OUT/"reading-navigation-strict-narrative-summary.json").read_text());strict=(OUT/"reading-navigation-strict-narrative.txt").read_text();assert len(strict)==summary["counts"]["projection_unicode_characters"] and nav.sha(strict.encode())==summary["projection_sha256"]
uses=[json.loads(l) for l in storage.read_text(OUT/"reading-navigation-strict-narrative-use-index.jsonl").splitlines()];excluded=[json.loads(l) for l in storage.read_text(OUT/"reading-navigation-strict-narrative-excluded.jsonl").splitlines()];allow=set(summary["exact_metadata_terminal_key_allowlist"]);seen=set();last=0
for u in uses:
 v=values[u["original_value_index"]];assert v["value_index"] not in seen;seen.add(v["value_index"]);assert len(v["occurrences"])==u["occurrence_count"]
 assert all(all(oc[k]==full[k] for k in oc) for oc,full in zip(v["occurrences"],u["all_occurrences"]))
 assert not all(t["explicit_metadata_key"] for t in u["all_occurrences"])
 body=v["value"] if v["type"]=="string" else nav.encoded(v["value"]);piece=f"[N{u['narrative_index']} V{v['value_index']} {v['type']} U{u['narrative_index']}]\n"+body+"\n"
 assert last==u["projection_unicode_start"] and strict[last:u["projection_unicode_end"]]==piece;last=u["projection_unicode_end"]
for e in excluded:
 assert e["value_index"] not in seen;seen.add(e["value_index"]);assert nav.encoded(e["value"])==nav.encoded(values[e["value_index"]]["value"]);assert all(o["exact_terminal_key"] in allow and o["explicit_metadata_key"] for o in e["all_occurrences"])
assert len(seen)==len(values) and last==len(strict)
text_projections=[]
for name in ("reading-navigation-values.txt","reading-navigation-shell.txt"):
 expected=next(d for d in inv["files"] if pathlib.Path(d["path"]).name==name);b=(OUT/name).read_bytes();assert len(b)==expected["bytes"] and nav.sha(b)==expected["sha256"];text_projections.append({"name":name,"bytes":len(b),"sha256":nav.sha(b),"unchanged_from_prior_navigation_inventory":True})
text_projections.append({"name":"reading-navigation-strict-narrative.txt","bytes":len(strict.encode()),"unicode_characters":len(strict),"sha256":nav.sha(strict.encode()),"unchanged_from_prior_strict_projection_summary":True})
printer=OUT/"reading-navigation-print.py"
def printer_case(args,expected):
 result=subprocess.run([sys.executable,str(printer),*args,"--no-log"],cwd=nav.ROOT,capture_output=True,text=True);assert result.returncode==0,result.stderr
 header,sep,body=result.stdout.partition("\n");meta=json.loads(header);assert body==expected+"\n",args
 return {"args":args,"exit_code":0,"exact_expected_chunk_equal":True,"returned_bytes":len(expected.encode()),"returned_sha256":nav.sha(expected.encode()),"qualification":meta["qualification"]}
contract_text=cache[nav.HANDOFF+"/contracts.zh.json"];contract_values,contract_nodes=nav.Parser(contract_text).parse();n=contract_nodes["/records/0"];record=contract_text[n["unicode_start"]:n["unicode_end"]]
value0=values[0]["value"] if values[0]["type"]=="string" else nav.encoded(values[0]["value"])
shell0=json.loads(storage.read_text(OUT/"reading-navigation-shell-paragraphs.jsonl").splitlines()[0])["text"]
cases=[printer_case(["--stream","strict-narrative","--start","6000","--end","6120"],strict[6000:6120]),printer_case(["--record","GR8-KER-001","--start","0","--end","120"],record[:120]),printer_case(["--document","history","--start","20","--end","100"],cache[nav.HANDOFF+"/history-qualifications.json"][20:100]),printer_case(["--document","contracts","--pointer","/records/0/severity"], '"P3"'),printer_case(["--value","0"],value0),printer_case(["--shell","0","--start","0","--end",str(min(120,len(shell0)))],shell0[:120])]
for name,old in receipts.items():p=OUT/name;assert p.stat().st_size==old["bytes"] and nav.sha(p.read_bytes())==old["sha256"]
narrative_tree=ast.parse((OUT/"reading-navigation-narrative-build.py").read_text());load_fn=next(n for n in narrative_tree.body if isinstance(n,ast.FunctionDef) and n.name=="loadlines");load_namespace={"json":json,"storage":storage};exec(compile(ast.Module(body=[load_fn],type_ignores=[]),str(OUT/"reading-navigation-narrative-build.py"),"exec"),load_namespace);assert len(load_namespace["loadlines"](OUT/"reading-navigation-values.jsonl"))==len(values)
m=storage.mapping();result={"schema":"r8-final-reading-navigation-gzip-regression/v1","qualification":"MECHANICAL_TOOL_STORAGE_VALIDATION_ONLY_NO_SEMANTIC_FULL_OR_CONFIG_CREDIT","artifact":nav.ARTIFACT,"gzip_only_carriers":entries,"plain_bytes_total":sum(e["original_plain_bytes"] for e in m["entries"]),"gzip_bytes_total":sum(e["gzip_bytes"] for e in m["entries"]),"reconstructed_JSON_source_or_fence_documents_from_gzip_nodes_and_values":len(bydoc),"node_rows_available_after_exact_decompression":len(nodes),"strict_projection_all_original_retained_values_and_exact_uses_preserved":len(uses),"strict_projection_all_original_excluded_values_and_exact_uses_preserved":len(excluded),"all_typed_values_partition_preserved":len(seen),"unchanged_plain_text_projections":text_projections,"unchanged_prior_navigation_and_failure_receipts":receipts,"printer_actual_gzip_fallback_regression_cases":cases,"narrative_builder_actual_loadlines_function_gzip_fallback_validated":True,"narrative_builder_fallback_values_loaded":len(values),"all_checks_passed":True,"business_Ruby_execution":False,"new_semantic_reading_or_FULL_credit":False,"scope":"Only new uncommitted reading-navigation carriers compressed; original fixed inputs and all old evidence left unchanged."}
(OUT/"reading-navigation-compression-checks.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n");print(json.dumps({"all_checks_passed":True,"gzip_carriers":len(entries),"original_bytes":result["plain_bytes_total"],"gzip_bytes":result["gzip_bytes_total"],"reconstructed_JSON_documents":len(bydoc),"printer_cases":len(cases),"strict_projection_unicode_characters":len(strict),"strict_projection_sha256":nav.sha(strict.encode())}))
