"""Freeze exact disjoint candidate subset; no semantic dispositions."""
import gzip,json,pathlib,hashlib,datetime
ROOT=pathlib.Path(__file__).resolve().parent;REPORT=ROOT.parent.parent;REPO=REPORT.parents[2]
OUT=ROOT/'ruby-zlib-subtask';OUT.mkdir(exist_ok=False)
def save(n,b): (OUT/n).write_bytes(b)
def sha(b):return hashlib.sha256(b).hexdigest()
for src,name in [(REPORT/'inputs/eighth-global-review-prompt.md','global-prompt.md'),(REPORT/'inputs/review-SKILL.md','review-SKILL.md'),(REPO/'AGENTS.md','AGENTS.md'),(REPORT/'delegation/prompts/binary_remaining_texts.md','parent-prompt.md')]:save(name,src.read_bytes())
paths={'x64-msvcrt-ruby310.dll','zlib1.dll'}
rows=[]
for line in (ROOT/'remaining-text-readset.jsonl').read_text().splitlines():
 r=json.loads(line);refs=[v for v in r['refs'] if v['path'] in paths]
 if refs:rows.append(dict(r,refs=refs))
u=[json.loads(l) for l in (ROOT/'remaining-unread.jsonl').read_text().splitlines()];u=[r for r in u if r['path'] in paths]
assert len(u)==20907 and sum(len(r['refs']) for r in rows)==20907
assert {r['candidate_id'] for r in u}=={ref['candidate_id'] for r in rows for ref in r['refs']}
save('readset.jsonl.gz',gzip.compress(('\n'.join(json.dumps(r,ensure_ascii=False,separators=(',',':')) for r in rows)+'\n').encode(),mtime=0))
save('unread.jsonl.gz',gzip.compress(('\n'.join(json.dumps(r,ensure_ascii=False,separators=(',',':')) for r in u)+'\n').encode(),mtime=0))
save('text-view.txt.gz',gzip.compress(('\n'.join(r['read_id']+' '+r['text'].replace('\r','\\r').replace('\n','\\n') for r in rows)+'\n').encode(),mtime=0))
prompt='''# R8 Ruby/zlib完整剩余有限文本独立子任务

先完整读取本目录global-prompt.md、AGENTS.md、review-SKILL.md、parent-prompt.md及manifest.json；它们是完整合同，不得只读此摘要。父任务为/root/binary_remaining_texts，root全局总责。请求gpt-6.1-sol / ultra / default普速 / Fast off；实际无权威回显逐项UNVERIFIED。独占写根由root另行指定，当前本目录只读；不commit/push/install/spawn，不执行EXE/DLL/Ruby/C/GLSL或其它目标程序。R/formal/planning/audit/旧任务均只读，UPDATE_NOT_STARTED，业务向量全部NOT_EXECUTED。

你只负责精确过滤的Ruby20817和zlib90出处，共20907；readset.jsonl.gz中的全部不同字面文本必须实际完整读或按精确结构证据具证类型处置，不能样本/marker/脚本分类代读。每个ref保留原candidate_id/inventory_line/offset/end/SHA及所有本子集出处；相同文本的Game出处由父任务主责，不得改其状态。原全域57948起分母不能因此消失。源为/workspace/pokemon-essentials，固定R commit8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/tree7589c800b61ba13a13040ed0d686979b80a84fd0。B8 fd1df570cad987dc3852a3b958f03916e317f7fe/tree751dfde81048c81390f89a65ca1d1a565ba8e1ca/formaltreef292698cdd4a8e725525a9be6dc34b75faaf151e。先核manifest容器和整体解码身份，再核原始源字节。

20907出处均为当前真实UNREAD。大多数在Ruby.rdata，含有真正诊断、配置、API/GUI、运行库数据和可能程序片段，不得全标opaque L04。PE COFF符号表、真实DIR64重定位指针、原生具体引用和完整数字表结构可用于精确类型处置，但名称/统计本身不授语义信用。引用到文字的指针字节与目标文字分别处理。已读659C片段和六个新MJIT片段不免除当前候选；发现新程序须完整读结构与必要消费者/接线。审计decoder先完整读懂，复制到自己新的隔离目标，保完整I/O/exit/UTC；不要在父任务或旧任务目录运行写工具。

完整源集合是本目录readset/unread而非早期semantic-text-readset。父任务已读取原controller任务review.md、reading-ledger.json、disposition-summary.json、identities.json；你如引用该贡献必须完整读相关证据，不冒自己FULL_READ。旧四GR8-BIN-*已由root作有限新context no-required反证，但不构成当前全域通过。

交付progress.json、identities.json、full-disposition-ledger.jsonl.gz（本20907出处逐一守恒）、reading-ledger.json（连续精确范围和语义/类型信用区别）、bidirectional-mapping.json、consumers.json、remaining.json（真正剩余及其精确逐候选集）、proposals.json、review.md。每类类型证据可共同引用但逐候选必须精确；所有真正意义文字完整接收。每个新finding遵循完整七节合同并补历史关系第八节，具源/规格双向身份、普通/最小反例、失败/取消/部分提交、正确保留、最小读写/回归范围和真实消费者，交root安排非提出者独立反证，不自签required/no-required全局结论。材料/宿主/nativeCFG未知与可读未读分开。任何未完成如实保留，不能以工具exit0或角色重命名代替审读。
'''
save('prompt.md',prompt.encode())
files=[]
for p in sorted(OUT.iterdir()):
 b=p.read_bytes();r={'path':p.name,'bytes':len(b),'sha256':sha(b)}
 if p.suffix=='.gz':
  d=gzip.decompress(b);r['decoded']={'bytes':len(d),'sha256':sha(d),'lines':len(d.splitlines())}
 files.append(r)
manifest={'schema':'gr8.binary.ruby-zlib.split/v1','frozen_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'parent_task':'/root/binary_remaining_texts','source_inventory':'../remaining-text-readset.jsonl','scope_paths':sorted(paths),'occurrences':20907,'distinct_texts':len(rows),'candidate_set_sha256':sha(('\n'.join(sorted(r['candidate_id'] for r in u))+'\n').encode()),'files':files,'business_execution':0,'update_status':'UPDATE_NOT_STARTED'}
save('manifest.json',(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode());print(json.dumps(manifest,ensure_ascii=False))
