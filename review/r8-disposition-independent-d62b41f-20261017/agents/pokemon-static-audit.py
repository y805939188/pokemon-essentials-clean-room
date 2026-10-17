import json, re, subprocess, hashlib, unicodedata, collections
from pathlib import Path
C="d62b41f4d620e50bb04c80a7505374bd284d8210"
S="fd1df570cad987dc3852a3b958f03916e317f7fe"
D="4575e80d041ab0c74a42e2e36399d05791dbaa5b"
ROOT="planning/implementation-routing/r8-20261017/"
OUT=Path("review/r8-disposition-independent-d62b41f-20261017/agents")
def git(*args): return subprocess.check_output(["git",*args])
def get(path,c=C): return git("show",c+":"+path)
def h(b): return hashlib.sha256(b).hexdigest()
def headings(raw):
 lines=raw.decode().splitlines(keepends=True); result=[]; fence=None; used=collections.Counter()
 for no,line in enumerate(lines,1):
  z=line.lstrip()
  if z.startswith("```") or z.startswith("~~~"):
   tok=z[:3]
   if fence is None:fence=tok
   elif fence==tok:fence=None
   continue
  if fence:continue
  m=re.match(r"^(#{1,6})[ \t]+(.+?)\s*$",line)
  if not m:continue
  title=re.sub(r"\s+#+\s*$","",m[2])
  slug=re.sub(r"<[^>]*>","",title).lower()
  slug="".join(x for x in slug if x in "-_ " or unicodedata.category(x)[0] in "LN")
  slug=slug.replace(" ","-"); base=slug
  if used[base]:slug += "-"+str(used[base])
  used[base]+=1
  result.append({"level":len(m[1]),"title":title,"line_start":no,"anchor":slug,"heading_sha256":h(line.encode())})
 return result
m=json.loads(get(ROOT+"routing-manifest.json")); sec=json.loads(get(ROOT+"section-coverage.json"))["sections"]
paths=[p for p in git("ls-tree","-r","--name-only",S,"deliverables/final-specification-set").decode().splitlines() if "/pokemon-rules/" in p or "/test-catalog/pokemon-rules-" in p]
docs={d["source"]["path"]:d for d in m["documents"] if d["source"]["path"] in paths}
features=[f for f in m["features"] if f["source"]["document"] in paths]
errors=[]; ledger=[]
for path in paths:
 raw=get(path,S); now=get(path,C); delivery=get(path,D); parsed=headings(raw); mapped=[s for s in sec if s["path"]==path]; doc=docs.get(path)
 if not doc:errors.append([path,"missing_document"])
 if now!=raw or delivery!=raw:errors.append([path,"source_bytes_changed"])
 if doc and (doc["source"]["sha256"]!=h(raw) or doc["source"]["git_blob"]!=git("rev-parse",S+":"+path).decode().strip()):errors.append([path,"doc_identity_mismatch"])
 actual={(v["level"],v["title"],v["line_start"],v["anchor"],v["heading_sha256"]) for v in parsed}
 recorded={(v["level"],v["title"],v["line_start"],v["anchor"],v["heading_sha256"]) for v in mapped}
 if actual!=recorded:errors.append([path,"heading_map_diff",list(actual-recorded),list(recorded-actual)])
 ledger.append({"path":path,"lines":len(raw.splitlines()),"sha256":h(raw),"git_blob":git("rev-parse",S+":"+path).decode().strip(),"candidate_bytes_same":now==raw,"delivery_bytes_same":delivery==raw,"heading_count":len(parsed),"heading_map_count":len(mapped),"feature_count":sum(f["source"]["document"]==path for f in features),"full_semantic_read_ranges":[[1,len(raw.splitlines())]],"read_mode":"分块完整输出并语义阅读；无标题抽样替代；对工具截断处补读"})
for f in features:
 s=f["source"]; raw=get(s["document"],S); lines=raw.splitlines(keepends=True); parsed=headings(raw)
 selected=b"".join(v for a,b in s["line_ranges"] for v in lines[a-1:b])
 if h(selected)!=s["unit_sha256"]:errors.append([f["feature_id"],"unit_sha_mismatch"])
 if not any(x["title"]==s["heading"] and x["anchor"]==s["anchor"] and x["heading_sha256"]==s["heading_sha256"] for x in parsed):errors.append([f["feature_id"],"invalid_heading_selector"])
 if s["file_sha256"]!=h(raw):errors.append([f["feature_id"],"file_sha_mismatch"])
 if f["destination_verification"]["status"]!="待验证" or f["implementation"]["status"]!="未实现" or f["implementation"]["acceptance_status"]!="未验收" or f["future_plan"]["stage"]!="待定":errors.append([f["feature_id"],"unexpected_state"])
 if f["future_plan"]["destination"]=="不纳入目标":errors.append([f["feature_id"],"exclusion_in_scope"])
view=get(ROOT+"views/pokemon-rules.md").decode().splitlines(); rows=[(n,l) for n,l in enumerate(view,1) if l.startswith("| FR-")]
rowids=[re.search(r"FR-\d+",l).group() for _,l in rows]
if set(rowids)!={f["feature_id"] for f in features} or len(rowids)!=len(features):errors.append(["view","row_set_mismatch"])
view_checks=[]
for f in features:
 n,l=next((n,l) for n,l in rows if l.startswith("| "+f["feature_id"]+" /"));s=f["source"];p=f["future_plan"]
 checks={"destination":p["destination"] in l,"partners":" / ".join(p["partners"]) in l,"verification":f["destination_verification"]["status"] in l,"source_commit":s["commit"] in l,"source_anchor":"`#"+s["anchor"]+"`" in l,"source_excerpt":s["fact_excerpt"].replace("|","\\|").replace("\n"," ") in l,"upstream":all(x in l for x in f["upstream"]["batches"]),"prototype":all(x in l for x in p["prototype_refs"]),"decisions":all(x in l for x in f["decision_refs"])}
 view_checks.append({"feature_id":f["feature_id"],"view_line":n,"checks":checks})
 if not all(checks.values()):errors.append([f["feature_id"],"view_projection_mismatch",checks])
batches=json.loads(get("review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/handoff/batch-assignment.json"))["batches"]
for path,d in docs.items():
 expected=sorted(b["id"] for b in batches if path in b["actual_target_write_set"])
 if sorted(d["upstream"]["batches"])!=expected:errors.append([path,"upstream_batch_diff",expected])
 for f in features:
  if f["source"]["document"]==path and (sorted(f["upstream"]["batches"])!=expected or (expected and f["upstream"]["status"]!="待整改后核对")):errors.append([f["feature_id"],"upstream_binding_diff",expected])
report={"candidate_commit":C,"source_commit":S,"delivery_commit":D,"formal_tree":git("rev-parse",C+":deliverables/final-specification-set").decode().strip(),"counts":{"documents":len(paths),"formal_pokemon_documents":sum("/pokemon-rules/" in p for p in paths),"catalog_documents":sum("/test-catalog/" in p for p in paths),"formal_lines":sum(x["lines"] for x in ledger if "/pokemon-rules/" in x["path"]),"catalog_lines":sum(x["lines"] for x in ledger if "/test-catalog/" in x["path"]),"headings":sum(x["heading_count"] for x in ledger),"features":len(features),"generated_view_rows":len(rows)},"errors":errors,"reading_ledger":ledger,"view_checks":view_checks,"limitations":["只分析Git/Markdown/JSON；未执行Ruby、参考游戏、Showdown、宿主、框架或业务向量","生成view全部165行以字段投影核对；重复字段去重语义读取，来源事实已由正文全文读取","模型/effort/tier/Fast实际执行telemetry无权威echo，UNVERIFIED"]}
(OUT/"pokemon-static-evidence.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"counts":report["counts"],"errors":errors},ensure_ascii=False,indent=2))
