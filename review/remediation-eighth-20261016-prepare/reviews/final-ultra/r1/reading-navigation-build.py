#!/usr/bin/env python3
"""Mechanical navigation only: no semantic verdict, FULL status or config credit."""
import argparse,collections,hashlib,importlib.util,json,pathlib,re,subprocess,sys
sys.dont_write_bytecode=True
ROOT=pathlib.Path(__file__).resolve().parents[5]
OUT=pathlib.Path(__file__).resolve().parent
storage_spec=importlib.util.spec_from_file_location("reading_navigation_storage",OUT/"reading-navigation-storage.py");storage=importlib.util.module_from_spec(storage_spec);storage_spec.loader.exec_module(storage)
BINDING="8ab43a609e60430492b219f0dce14ef4fdb8e47f"
ARTIFACT="fd414a2c6ec0a0f746b48e0924e5692221ea5d5a"
HANDOFF="review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff"
PREFIX="reading-navigation-"
def sha(b):return hashlib.sha256(b).hexdigest()
def encoded(v):return json.dumps(v,ensure_ascii=False,separators=(",",":"))
def git(*args):return subprocess.check_output(["git",*args],cwd=ROOT)
def raw(path,commit=ARTIFACT):return git("show",commit+":"+path)
def esc(v):return str(v).replace("~","~0").replace("/","~1")
def typ(v):
 if v is None:return "null"
 if isinstance(v,bool):return "boolean"
 if isinstance(v,str):return "string"
 if isinstance(v,int):return "integer"
 if isinstance(v,float):return "number"
 return "object" if isinstance(v,dict) else "array"
def leaves(v,p=""):
 if isinstance(v,dict):
  for k,a in v.items():yield from leaves(a,p+"/"+esc(k))
 elif isinstance(v,list):
  for i,a in enumerate(v):yield from leaves(a,p+"/"+str(i))
 else:yield p,typ(v),v
class Parser:
 def __init__(self,text,base=0):self.text=text;self.base=base;self.nodes={};self.dec=json.JSONDecoder()
 def ws(self,i):
  while i<len(self.text) and self.text[i].isspace():i+=1
  return i
 def parse(self):
  value,end=self.val(self.ws(0),"");assert self.ws(end)==len(self.text);assert value==json.loads(self.text)
  return value,self.nodes
 def val(self,i,p):
  start=i;c=self.text[i];keys=[];keyspans=[]
  if c=="{":
   value={};i=self.ws(i+1)
   while self.text[i]!="}":
    ks=i;k,i=self.dec.raw_decode(self.text,i);assert isinstance(k,str);assert k not in value
    keys.append(k);keyspans.append([k,self.base+ks,self.base+i]);i=self.ws(i);assert self.text[i]==":";i=self.ws(i+1)
    a,i=self.val(i,p+"/"+esc(k));value[k]=a;i=self.ws(i)
    if self.text[i]=="}":break
    assert self.text[i]==",";i=self.ws(i+1)
   i+=1
  elif c=="[":
   value=[];i=self.ws(i+1)
   while self.text[i]!="]":
    a,i=self.val(i,p+"/"+str(len(value)));value.append(a);i=self.ws(i)
    if self.text[i]=="]":break
    assert self.text[i]==",";i=self.ws(i+1)
   i+=1
  else:value,i=self.dec.raw_decode(self.text,i)
  node={"pointer":p,"type":typ(value),"unicode_start":self.base+start,"unicode_end":self.base+i}
  if isinstance(value,dict):node.update(keys=keys,key_unicode_spans=keyspans)
  elif isinstance(value,list):node["length"]=len(value)
  else:node["value"]=value
  self.nodes[p]=node
  return value,i

def main():
 paths=[HANDOFF+"/contracts.zh.json",HANDOFF+"/cloud-eighth-update-handoff-prompt.md",HANDOFF+"/cloud-eighth-update-handoff-manifest.json"]
 paths += [HANDOFF+"/"+n for n in ("accepted-facts-and-mandatory-companions.json","history-qualifications.json","policy-and-preservation.json")]
 for i in range(1,10):paths += [HANDOFF+f"/batches/R8-U{i:02d}/"+n for n in ("prompt.md","reviewer-prompt.md","readset.json")]
 originals={p:raw(p) for p in paths};texts={p:b.decode("utf-8") for p,b in originals.items()}
 contractpath=paths[0];contracts,contractnodes=Parser(texts[contractpath]).parse();records=contracts["records"];assert len(records)==39
 byid={r["id"]:r for r in records};assert len(byid)==39
 documents=[];node_rows=[];unique_values=[];value_ids={};fence_checks=[];ref_checks=[];prompt_ranges=[];paragraphs=[];paragraph_ids={};record_rows=[];node_maps={};parsed_docs={}
 def add_nodes(path,name,text,base=0):
  value,nodes=Parser(text,base).parse();node_maps[name]=nodes;parsed_docs[name]=value
  for p,n in nodes.items():
   row={"document":name,"source_path":path,**n};start,end=n["unicode_start"],n["unicode_end"]
   row["byte_start"]=len(texts[path][:start].encode());row["byte_end"]=len(texts[path][:end].encode());row["raw_token_sha256"]=sha(texts[path][start:end].encode())
   if "value" in row:
    key=(row["type"],encoded(row.pop("value")))
    if key not in value_ids:
     value_ids[key]=len(unique_values);unique_values.append({"value_index":len(unique_values),"type":n["type"],"value":n["value"],"occurrences":[]})
    vi=value_ids[key];row["value_index"]=vi;unique_values[vi]["occurrences"].append({"document":name,"source_path":path,"pointer":p,"unicode_start":start,"unicode_end":end})
   node_rows.append(row)
  return value,nodes
 def segment(path,start,end,kind,index):
  t=texts[path][start:end];entry={"path":path,"kind":kind,"segment_index":index,"unicode_start":start,"unicode_end":end,"byte_start":len(texts[path][:start].encode()),"byte_end":len(texts[path][:end].encode()),"bytes":len(t.encode()),"sha256":sha(t.encode())}
  off=start
  for part in re.split(r"(\n[ \t]*\n)",t):
   if not part:continue
   k=part
   if k not in paragraph_ids:
    paragraph_ids[k]=len(paragraphs);paragraphs.append({"paragraph_index":len(paragraphs),"text":part,"bytes":len(part.encode()),"sha256":sha(part.encode()),"whitespace_only":not bool(part.strip()),"occurrences":[]})
   paragraphs[paragraph_ids[k]]["occurrences"].append({"path":path,"segment_index":index,"unicode_start":off,"unicode_end":off+len(part),"byte_start":len(texts[path][:off].encode()),"byte_end":len(texts[path][:off+len(part)].encode())});off+=len(part)
  assert off==end
  prompt_ranges.append(entry)
 for path in paths:
  b=originals[path];t=texts[path];tree=git("ls-tree",ARTIFACT,"--",path).decode().strip().split(None,3)
  documents.append({"path":path,"commit":ARTIFACT,"bytes":len(b),"unicode_characters":len(t),"sha256":sha(b),"mode":tree[0],"blob":tree[2],"line_count":len(t.splitlines()),"working_tree_bytes_equal":(ROOT/path).read_bytes()==b})
  if path.endswith(".json"):add_nodes(path,path,t)
  else:
   contract_spans=[]
   for i,m in enumerate(re.finditer(r"^```json\n([\s\S]*?)\n```",t,re.M)):
    name=path+"#json-fence/"+str(i);v,n=add_nodes(path,name,m[1],m.start(1))
    if isinstance(v,dict) and v.get("id") in byid and "full_contract" in v:
     expected=byid[v["id"]];l1=list(leaves(v));l2=list(leaves(expected));ok=encoded(v)==encoded(expected) and l1==l2
     fence_checks.append({"path":path,"fence_index":i,"id":v["id"],"all_values_and_order_equal":ok,"all_typed_leaves_equal":l1==l2,"typed_leaf_count":len(l1),"canonical_pointer":"/records/"+str(next(j for j,r in enumerate(records) if r["id"]==v["id"]))});assert ok
     contract_spans.append([m.start(),m.end()])
   spans=[];pos=0
   for i,(s,e) in enumerate(contract_spans):
    if pos<s:segment(path,pos,s,"preamble" if i==0 else "between_contracts",len(spans));spans.append([pos,s])
    spans.append([s,e]);pos=e
   if pos<len(t):segment(path,pos,len(t),"tail" if contract_spans else "whole_noncontract_prompt",len(spans));spans.append([pos,len(t)])
   assert "".join(t[s:e] for s,e in spans)==t
 for path,value in parsed_docs.items():
  if not path.endswith("/readset.json"):continue
  for p,n in node_maps[path].items():
   if n["type"]!="object":continue
   cur=value
   for part in p.split("/")[1:]:
    part=part.replace("~1","/").replace("~0","~");cur=cur[int(part)] if isinstance(cur,list) else cur[part]
   if isinstance(cur,dict) and cur.get("id") in byid:
    if "full_contract" in cur:
     ok=list(leaves(cur))==list(leaves(byid[cur["id"]]));ref_checks.append({"document":path,"pointer":p,"id":cur["id"],"kind":"embedded_complete_contract","all_typed_leaves_equal":ok});assert ok
    elif cur.get("path")=="handoff/contracts.zh.json" and "pointer" in cur:
     target=contracts
     for part in cur["pointer"].split("/")[1:]:target=target[int(part)] if isinstance(target,list) else target[part]
     ok=target["id"]==cur["id"];ref_checks.append({"document":path,"pointer":p,"id":cur["id"],"kind":"canonical_pointer_reference","target_pointer":cur["pointer"],"id_matches_target":ok});assert ok
 for i,r in enumerate(records):
  n=contractnodes["/records/"+str(i)];s,e=n["unicode_start"],n["unicode_end"];t=texts[contractpath][s:e];record_rows.append({"index":i,"id":r["id"],"pointer":"/records/"+str(i),"unicode_start":s,"unicode_end":e,"byte_start":len(texts[contractpath][:s].encode()),"byte_end":len(texts[contractpath][:e].encode()),"source_raw_bytes":len(t.encode()),"source_raw_sha256":sha(t.encode()),"parsed_compact_bytes":len(encoded(r).encode()),"parsed_compact_sha256":sha(encoded(r).encode()),"top_level_keys":list(r),"typed_leaf_count":len(list(leaves(r))),"classification":r["classification"],"severity":r["severity"],"primary_batch":r["required_primary_batch"],"conditional_batch":r["conditional_batch_if_user_selects"]})
 oldledgerpath="review/remediation-eighth-20261016-prepare/reviews/actual-U06/r1/continuation-reading-ledger.json"
 oldledger=json.loads(raw(oldledgerpath));oldrows=oldledger["complete_contract_records"];u06=[]
 for row in oldrows:
  old=json.loads(raw(row["carrier_path"],row["carrier_commit"]));oldvalue=old
  for part in row["carrier_pointer"].split("/")[1:]:oldvalue=oldvalue[int(part)] if isinstance(oldvalue,list) else oldvalue[part]
  current=byid[row["id"]];ok=encoded(oldvalue)==encoded(current) and list(leaves(oldvalue))==list(leaves(current));assert ok
  u06.append({"id":row["id"],"old_carrier_commit":row["carrier_commit"],"old_carrier_pointer":row["carrier_pointer"],"old_carrier_path":row["carrier_path"],"old_recorded_compact_sha256":row["parsed_value_canonical_sha256"],"old_computed_compact_sha256":sha(encoded(oldvalue).encode()),"current_compact_sha256":sha(encoded(current).encode()),"all_typed_leaves_and_order_equal":ok,"prior_ledger_reading_attestation":row["root_reading"],"navigation_grants_new_reading_credit":False})
 assert len(u06)==14
 projected=[];offset=0
 for value in unique_values:
  body=value["value"] if value["type"]=="string" else encoded(value["value"])
  piece=f"=== value {value['value_index']} type {value['type']} ===\n"+body+"\n"
  value["projection_unicode_start"]=offset;offset+=len(piece);value["projection_unicode_end"]=offset;projected.append(piece)
 shellproject=[];offset=0
 for para in paragraphs:
  piece=f"=== shell paragraph {para['paragraph_index']} ===\n"+para["text"]+"\n"
  para["projection_unicode_start"]=offset;offset+=len(piece);para["projection_unicode_end"]=offset;shellproject.append(piece)
 def write_json(suffix,value):
  p=OUT/(PREFIX+suffix);return storage.write_payload(p,(json.dumps(value,ensure_ascii=False,indent=2)+"\n").encode())
 def write_jsonl(suffix,rows):
  p=OUT/(PREFIX+suffix);return storage.write_payload(p,"".join(json.dumps(row,ensure_ascii=False,separators=(",",":"))+"\n" for row in rows).encode())
 outputs=[]
 outputs.append(write_json("contracts-index.json",{"qualification":"MECHANICAL_NAVIGATION_ONLY_NO_SEMANTIC_FULL_OR_CONFIG_CREDIT","records":record_rows}))
 outputs.append(write_jsonl("nodes.jsonl",node_rows));outputs.append(write_jsonl("values.jsonl",unique_values));outputs.append(write_jsonl("shell-paragraphs.jsonl",paragraphs))
 for name,parts in (("values.txt",projected),("shell.txt",shellproject)):
  p=OUT/(PREFIX+name);p.write_text("".join(parts));outputs.append({"path":str(p.relative_to(ROOT)),"bytes":p.stat().st_size,"sha256":sha(p.read_bytes())})
 checks={"qualification":"MECHANICAL_COMPARISON_ONLY_NO_SEMANTIC_FULL_OR_CONFIG_CREDIT","input_binding":BINDING,"artifact":ARTIFACT,"contract_count":len(records),"embedded_prompt_contract_checks":fence_checks,"readset_canonical_contract_checks":ref_checks,"prior_same_context_U06_contract_identity_checks":u06,"prompt_noncontract_exact_ranges":prompt_ranges,"scope_note":"Old named reader ledgers and source locators remain their own evidence; neither this parser nor prior helpers confer current root FULL or configuration eligibility."}
 outputs.append(write_json("checks.json",checks))
 inventory={"schema":"r8-final-lossless-reading-navigation/v1","qualification":"MECHANICAL_NAVIGATION_ONLY_NO_SEMANTIC_FULL_OR_CONFIG_CREDIT","input_binding":BINDING,"artifact":ARTIFACT,"documents":documents,"counts":{"documents":len(documents),"canonical_records":len(records),"JSON_node_rows":len(node_rows),"unique_typed_scalar_values":len(unique_values),"scalar_occurrences":sum(len(v["occurrences"]) for v in unique_values),"contract_fences_compared":len(fence_checks),"readset_contract_pointer_or_full_checks":len(ref_checks),"unique_shell_paragraphs":len(paragraphs),"shell_paragraph_occurrences":sum(len(p["occurrences"]) for p in paragraphs),"value_projection_unicode_characters":sum(map(len,projected)),"shell_projection_unicode_characters":sum(map(len,shellproject))},"files":outputs,"reconstruction":"Each JSON source is preserved at fixed artifact, all node pointers/types/object ordered keys/array lengths and every exact scalar value retained; the printer verifies source bytes before returning document/record/pointer/Unicode chunks. Every prompt noncontract character is range-partitioned and every paragraph (including whitespace) retained exactly. No reader status is assigned."}
 write_json("inventory.json",inventory);print(json.dumps(inventory["counts"],ensure_ascii=False));print("All embedded contract, readset reference and prior U06 exact-value comparisons succeeded.")
if __name__=="__main__":main()
