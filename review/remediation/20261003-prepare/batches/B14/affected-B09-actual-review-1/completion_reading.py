import json,pathlib,sys,subprocess,hashlib,re,collections
from read_bookkeeping import get,ACT,PRE,REF
D=pathlib.Path(__file__).parent
FLAGS=["--no-ext-diff","--no-textconv","--no-renames","--binary","--full-index","--no-color"]
def formal_units():
 paths=json.loads(get(ACT,"review/remediation/20261003-prepare/batches/B14/integration-stage-1/boundary-and-bindings.json"))["formal_paths"]
 raw=subprocess.check_output(["git","diff",*FLAGS,PRE,ACT]);blocks=[];units=[];seen={}
 for block in re.split(rb"(?=^diff --git )",raw,flags=re.M):
  if not block:continue
  path=block.split(b" b/",1)[1].split(b"\n",1)[0].decode()
  if path not in paths:continue
  current=None;relations=[]
  for i,line in enumerate(block.decode().splitlines(keepends=True)):
   if line.startswith("@@"):current=line.rstrip("\n")
   elif line[:1] in "+- " and not line.startswith(("+++","---")):
    value=line[1:];key=value
    if key not in seen:
     seen[key]=len(units);units.append({"n":len(units),"path":path,"block_line":i+1,"hunk":current,"sign":line[0],"value":value})
    relations.append({"line":i+1,"hunk":current,"sign":line[0],"unit":seen[key]})
  blocks.append({"path":path,"bytes":len(block),"sha256":hashlib.sha256(block).hexdigest(),"ordered_relations":relations})
 # Exact reuse only for literal current formal lines actually delivered in this same review.
 receipts=[json.loads(x) for x in (D/"display-receipts.jsonl").read_text().splitlines()]
 known={}
 for rec in receipts:
  if rec.get("repository")!="project" or rec.get("commit")!=ACT or rec.get("path") not in paths:continue
  ls=get(ACT,rec["path"]).decode().splitlines(keepends=True)
  for i in range(rec["line_start"]-1,rec["line_end"]):known.setdefault(ls[i],{"path":rec["path"],"line":i+1,"commit":ACT})
 for x in units:
  if x["value"] in known:x["read_reuse"]=known[x["value"]]
 return units,blocks

def scalar_key(v):return json.dumps(v,ensure_ascii=False,separators=(",",":"))
def metadata(v,pointer):
 if not isinstance(v,str):
  # Numeric/type relationships in business fixtures must remain reviewable; opaque audit indexes are metadata.
  return not any(t in pointer.lower() for t in ["/premises/","/expected","/result","/fixture","/inputs/","/reverse","/case/"])
 if any(t in pointer.lower().split("/") for t in ["pointer","pointers","selector","selectors","loci","source_pointer","first_pointer","source_selector","literal_selector"]):return True
 if re.search(r"/(?:mapping|structures|structure|ordered_trees|roots|shape|container_type_length_map)/",pointer) and (pointer.endswith("/$value") or re.search(r"/children/\d+$",pointer) or re.search(r"/keys/\d+$",pointer) or re.search(r"/mapping/\d+/(?:0|1)$",pointer)):return True
 if re.search(r"/(?:keys|children)/\d+$",pointer):return True
 if re.fullmatch(r"(?:GIR-FD82-[A-Z0-9-]+|WP80-[A-Z0-9-]+|RUN-[A-Z0-9-]+|[A-Z]{1,5}-?\d{1,3}|B\d\d(?:-[A-Z0-9-]+)?)",v):return True
 if re.fullmatch(r"[0-9a-f]{6,64}",v):return True
 if re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*:[0-9a-f]{6,64}",v):return True
 if v.startswith(("Unchanged exact copy ","Source lineage ","All context/removal ")) and ("/" in v):return True
 if "current-hashes.tsv" in pointer:return True
 if v.startswith(("specs/","deliverables/","review/","planning/","audit/","Data/Scripts/","PBS/")) and not "\n" in v and len(v.split())<=4:return True
 if re.fullmatch(r"[\d:/.,;\[\] ()~+-]+",v):return True
 # Opaque identity and pointer strings in an audit map are mechanically checked, never behavior claims.
 if re.match(r"^(?:[0-9a-f]{7,40}[:/])?(?:review|specs|deliverables|planning|audit|Data|PBS)/",v) and ("#" in v or "/line/" in v or "/lines/" in v):return True
 if re.fullmatch(r"(?:control|evidence|known|source|formal|value|unit|plain|text|line)(?::|_)[0-9a-f]+",v):return True
 if any(k in pointer.lower() for k in ["source_thread_id","user_message_id","private_provenance","source_path"]):return True
 return False

def audit_units():
 from semantic_bookkeeping import pool
 seed,_=pool("owner");seen={scalar_key(x["value"]):("prior_pool",x["n"]) for x in seed};units=[];schemas={};maps=[];counts=collections.Counter()
 inventory=json.loads((D/"diff-inventories.json").read_text())[0];paths=[x["header"].split(" b/",1)[1] for x in inventory["blocks"] if "/B14/" in x["header"]]
 # Read complete formal outer-hunk value dictionary first, then permit only exact string reuse.
 formals,_=formal_units()
 for x in formals:
  for value in [x["value"],x["value"].rstrip("\r\n")]:
   seen.setdefault(scalar_key(value),("formal_unit",x["n"]))
   for prefix in ["+","-"," "]:seen.setdefault(scalar_key(prefix+value),("formal_unit_with_exact_diff_prefix",x["n"],prefix))
 def leaf(v,path,ptr):
  key=scalar_key(v);h=hashlib.sha256(key.encode()).hexdigest();counts["scalar_occurrences"]+=1
  if key in seen:return {"reuse":seen[key],"value_sha256":h,"type":type(v).__name__}
  if isinstance(v,str) and len(v)>80 and v.lstrip().startswith(("{","[")):
   try:embedded=json.loads(v)
   except (ValueError,RecursionError):embedded=None
   if isinstance(embedded,(dict,list)):
    seen[key]=("embedded_JSON_string_source",path,ptr)
    return {"type":"string_containing_JSON_document","raw_value_sha256":h,"source":[path,ptr],"typed_embedded_relationships":walk(embedded,path,ptr+"/@embedded_JSON")}
  if isinstance(v,str) and "\n" in v.rstrip("\r\n"):
   # Preserve the entire raw string type, exact source pointer and ordered line relationships.
   relationships=[leaf(line,path,ptr+"/@text_line/"+str(i)) for i,line in enumerate(v.splitlines(keepends=True))]
   seen[key]=("text_source",path,ptr);return {"type":"multiline_string","exact_value_sha256":h,"lines":relationships}
  if metadata(v,ptr):
   seen[key]=("metadata_source",path,ptr);counts["unique_metadata"]+=1;return {"metadata_source":[path,ptr],"type":type(v).__name__,"value_sha256":h}
  seen[key]=("semantic_unit",len(units));units.append({"n":len(units),"path":path,"pointer":ptr,"type":type(v).__name__,"value":v,"value_sha256":h})
  return {"semantic_unit":len(units)-1,"type":type(v).__name__,"value_sha256":h}
 def walk(o,path,ptr):
  if isinstance(o,dict):
   schema=tuple(o.keys());schemas.setdefault(schema,{"first":[path,ptr],"keys":list(schema),"occurrences":0})["occurrences"]+=1
   # Relationship graph is hashed without retaining enormous duplicate public wrappers.
   children=[]
   for k,v in o.items():children.append([k,walk(v,path,ptr+"/"+k.replace("~","~0").replace("/","~1"))])
   return {"type":"object","ordered_members_sha256":hashlib.sha256(scalar_key(children).encode()).hexdigest(),"keys":list(o),"member_count":len(o)}
  if isinstance(o,list):
   children=[walk(v,path,ptr+"/"+str(i)) for i,v in enumerate(o)]
   return {"type":"array","length":len(o),"ordered_children_sha256":hashlib.sha256(scalar_key(children).encode()).hexdigest()}
  return leaf(o,path,ptr)
 for path in paths:
  b=get(ACT,path);text=b.decode();counts["files"]+=1
  if path.endswith(".json"):root=walk(json.loads(text),path,"")
  elif path.endswith(".jsonl"):root=walk([json.loads(x) for x in text.splitlines() if x],path,"/@jsonl")
  else:root=walk(text.splitlines(keepends=True),path,"/@lines")
  maps.append({"commit":ACT,"path":path,"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest(),"root":root})
 return units,maps,list(schemas.values()),dict(counts)

def print_page(units,a,b):
 for x in units[a:b]:
  print(str(x["n"])+" "+x["path"].split("/B14/")[-1]+" "+x.get("pointer",str(x.get("block_line")))+" "+json.dumps(x["value"],ensure_ascii=False))
 if units[a:b]:
  with (D/"completion-display-receipts.jsonl").open("a") as f:f.write(json.dumps({"mode":sys.argv[1],"first":a,"last_exclusive":min(b,len(units)),"display":"Bounded complete dictionary values; output truncation requires supplement, not automatic completion."})+"\n")

if __name__=="__main__":
 mode=sys.argv[1]
 if mode=="formal":u,m=formal_units();s=[];c={}
 else:u,m,s,c=audit_units()
 if len(sys.argv)==2:
  (D/("completion-"+mode+"-map.json")).write_text(json.dumps({"mode":mode,"ACT":ACT,"external_fixed_values_preserved":True,"original_types_orders_contexts_retained_at_exact_Git_sources":True,"maps":m,"schemas":s,"semantic_units":[{k:v for k,v in x.items() if k!="value"} for x in u],"counts":c},ensure_ascii=False,indent=2)+"\n")
  # Bounded pages chosen by character size, not guessed token count.
  pages=[];start=0;chars=0
  for i,x in enumerate(u):
   length=0 if (mode=="formal" and "read_reuse" in x) else len(json.dumps(x["value"],ensure_ascii=False))+len(x["path"])+len(x.get("pointer",""))+50
   if chars+length>6000 and i>start:pages.append([start,i]);start=i;chars=0
   chars+=length
  if start<len(u):pages.append([start,len(u)])
  (D/("completion-"+mode+"-pages.json")).write_text(json.dumps(pages)+"\n")
  print(mode,"units",len(u),"value_chars",sum(len(str(x["value"])) for x in u),"pages",len(pages),"schema_count",len(s),"counts",c)
 else:
  selected=u[int(sys.argv[2]):int(sys.argv[3])]
  if mode=="formal":
   selected=[x for x in selected if "read_reuse" not in x]
  for x in selected:print(str(x["n"])+" "+x["path"].split("/B14/")[-1]+" "+x.get("pointer",str(x.get("block_line")))+" "+json.dumps(x["value"],ensure_ascii=False))
  with (D/"completion-display-receipts.jsonl").open("a") as f:f.write(json.dumps({"mode":mode,"first":int(sys.argv[2]),"last_exclusive":min(int(sys.argv[3]),len(u)),"literal_new_values":len(selected),"exact_prior_reuse":len(u[int(sys.argv[2]):int(sys.argv[3])])-len(selected),"status":"DISPLAYED_BOUNDED; truncations require supplements"})+"\n")
