#!/usr/bin/env python3
"""Strict structural metadata exclusion projection, never semantic/FULL credit."""
import hashlib,importlib.util,json,pathlib,re,subprocess,sys
sys.dont_write_bytecode=True
OUT=pathlib.Path(__file__).resolve().parent
ROOT=OUT.parents[4]
storage_spec=importlib.util.spec_from_file_location("reading_navigation_storage",OUT/"reading-navigation-storage.py");storage=importlib.util.module_from_spec(storage_spec);storage_spec.loader.exec_module(storage)
ARTIFACT="fd414a2c6ec0a0f746b48e0924e5692221ea5d5a"
HANDOFF="review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff"
ALLOWLIST=("repo","commit","tree","workspace_tree","report_tree","formal_tree","path","pointer","json_pointer","mode","blob","bytes","sha256")
def sha(b):return hashlib.sha256(b).hexdigest()
def unescape(p):return p.replace("~1","/").replace("~0","~")
def loadlines(p):return [json.loads(line) for line in storage.read_text(p).splitlines()]
values=loadlines(OUT/"reading-navigation-values.jsonl")
checks=json.loads((OUT/"reading-navigation-checks.json").read_text())
records=json.loads((OUT/"reading-navigation-contracts-index.json").read_text())["records"]
byindex={r["index"]:r["id"] for r in records};fencerecord={r["path"]+"#json-fence/"+str(r["fence_index"]):r["id"] for r in checks["embedded_prompt_contract_checks"]}
retained=[];excluded=[];useindex=[];parts=[];offset=0
for item in values:
 uses=[];all_metadata=True
 for oc in item["occurrences"]:
  tokens=[unescape(t) for t in oc["pointer"].split("/")[1:]];key=tokens[-1] if tokens else "";is_meta=key in ALLOWLIST
  # No value-content, prefix, filename, hash-looking or ancestor-key heuristic.
  all_metadata=all_metadata and is_meta
  use={**oc,"exact_terminal_key":key,"explicit_metadata_key":is_meta}
  if oc["source_path"]==HANDOFF+"/contracts.zh.json" and len(tokens)>1 and tokens[0]=="records":use["canonical_record_id"]=byindex[int(tokens[1])]
  elif oc["document"] in fencerecord:use["canonical_record_id"]=fencerecord[oc["document"]]
  uses.append(use)
 record={"value_index":item["value_index"],"type":item["type"],"value":item["value"],"occurrence_count":len(uses),"all_occurrences_explicit_metadata":all_metadata,"all_occurrences":uses}
 if all_metadata:
  excluded.append(record)
 else:
  ni=len(retained);body=item["value"] if item["type"]=="string" else json.dumps(item["value"],ensure_ascii=False,separators=(",",":"))
  piece=f"[N{ni} V{item['value_index']} {item['type']} U{ni}]\n"+body+"\n"
  record.update(narrative_index=ni,projection_unicode_start=offset,projection_unicode_end=offset+len(piece));offset+=len(piece);parts.append(piece);retained.append(record)
  useindex.append({"narrative_index":ni,"original_value_index":item["value_index"],"type":item["type"],"occurrence_count":len(uses),"projection_unicode_start":record["projection_unicode_start"],"projection_unicode_end":record["projection_unicode_end"],"all_occurrences":uses})
assert len(retained)+len(excluded)==len(values)
assert all(not r["all_occurrences_explicit_metadata"] for r in retained)
assert all(r["all_occurrences_explicit_metadata"] and all(x["exact_terminal_key"] in ALLOWLIST for x in r["all_occurrences"]) for r in excluded)
stream="".join(parts);streamfile=OUT/"reading-navigation-strict-narrative.txt";streamfile.write_text(stream)
for name,rows in (("strict-narrative-use-index.jsonl",useindex),("strict-narrative-excluded.jsonl",excluded)):
 storage.write_payload(OUT/("reading-navigation-"+name),"".join(json.dumps(row,ensure_ascii=False,separators=(",",":"))+"\n" for row in rows).encode())
summary={"schema":"r8-final-strict-structural-metadata-projection/v1","qualification":"MECHANICAL_NAVIGATION_ONLY_NO_SEMANTIC_FULL_OR_CONFIG_CREDIT","artifact":ARTIFACT,"source_lossless_values":"reading-navigation-values.jsonl","exact_metadata_terminal_key_allowlist":list(ALLOWLIST),"exclusion_rule":"Exclude a unique typed scalar iff every original occurrence has its exact final JSON pointer key in this closed allowlist. Array numeric indices are not metadata keys. If any occurrence has a different or absent terminal key, retain. No examination of value wording, contents, path-looking or hash-looking form is used.","all_values_still_retained_in_lossless":True,"counts":{"source_unique_typed_values":len(values),"retained_unique_typed_values":len(retained),"excluded_unique_typed_values":len(excluded),"retained_occurrences":sum(r["occurrence_count"] for r in retained),"excluded_occurrences":sum(r["occurrence_count"] for r in excluded),"projection_unicode_characters":len(stream),"projection_bytes":len(stream.encode())},"projection_sha256":sha(stream.encode()),"excluded_value_indices":[r["value_index"] for r in excluded],"excluded_values_and_all_exact_uses":"reading-navigation-strict-narrative-excluded.jsonl","retained_values_all_exact_uses_and_document_record_pointers":"reading-navigation-strict-narrative-use-index.jsonl","root_reception_note":"The printed stream contains complete original typed values with links by exact index to every occurrence. The root separately receives object structure/identity metadata and decides its actual reading scope. Neither parsing nor this projection grants FULL."}
(OUT/"reading-navigation-strict-narrative-summary.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"counts":summary["counts"],"projection_sha256":summary["projection_sha256"],"exact_metadata_terminal_key_allowlist":list(ALLOWLIST)},ensure_ascii=False))
