#!/usr/bin/env python3
"""Assemble review-only artifacts from adjudicated evidence. Never edits R or formal specifications."""
from pathlib import Path
import json, hashlib, subprocess, collections, copy, re, datetime
O=Path(__file__).resolve().parents[1]
W=O.parents[2]
R=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
B5='9366d9d17aaeac3b4414236468affa650fb3dd27'
RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
BRANCH='codex/review-fifth-2026-10-13-9366d9d-c7d3'
REPO='https://github.com/y805939188/pokemon-essentials-clean-room'
PREFIX=str(O.relative_to(W))
def read(p): return json.loads((O/p).read_text())
def write(p,d):
 q=O/p
 q.parent.mkdir(parents=True,exist_ok=True)
 q.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*args): return subprocess.check_output(['git',*args],cwd=W).decode().strip()
def input_ref(p,pointer=''):
 return {'path':p,'pointer':pointer,'bytes':(O/p).stat().st_size,'sha256':sha(O/p)}
def batch_for(f):
 m=f['module'];i=f['id']
 if i in ('GR5-M01-005','GR5-M01-006'): return 'R5-U03'
 if m in ('M01','M02'): return 'R5-U01'
 if m=='M03' or i=='GR5-JXN-001': return 'R5-U02'
 if m in ('M04','M05','M06') or i=='GR5-JXN-003': return 'R5-U03'
 if m in ('M07','M08') or i=='GR5-JXN-002': return 'R5-U04'
 if m=='M09': return 'R5-U05'
 if m in ('M10','M11'): return 'R5-U06'
 if m in ('M12','M12B'): return 'R5-U07'
 raise ValueError((m,i))
STALE_UNKNOWNS={
 'Independent parent counterevidence and final required/optional decision pending.',
 'C00 global corpus closure remains parent-owned; this targeted set is complete.',
 'Canonical integration and final historical joins remain parent-owned.'}
def findings():
 rows=[]
 for p in sorted(O.glob('counterevidence/root-*/canonical-findings.json')):
  d=json.loads(p.read_text());a=d if isinstance(d,list)else d['findings']
  for n,f in enumerate(a):
   f=copy.deepcopy(f);f['canonical_input']=input_ref(str(p.relative_to(O)),f'/{n}' if isinstance(d,list)else f'/findings/{n}')
   old=f.get('unknowns',[])
   if isinstance(old,list):
    f['unknowns']=[x for x in old if not isinstance(x,str) or x not in STALE_UNKNOWNS]
    removed=[x for x in old if isinstance(x,str) and x in STALE_UNKNOWNS]
    if removed:f['closed_administrative_dependencies']={'prior_statements':removed,'resolution':'独立反证及主汇总裁决已完成；原审者冻结候选记录保留。'}
   f['schema_version']='gr5.canonical-finding.v2'
   f['review_resolution']['complete']=True
   f['review_resolution']['completion_basis']='主汇总者已接受的定稿目录；各条保留非提出者实读反证与定向整合裁决，不以此标记代替所列证据。'
   if f['disposition']=='required': f['batch_owner']=batch_for(f)
   else:f['batch_owner']=None
   rows.append(f)
 assert len({f['id']for f in rows})==len(rows)
 for f in rows:
  if f['disposition']=='required':
   assert f['review_resolution'].get('complete') is True,f['id']
   for k in ('source_anchors','spec_anchors','preconditions','minimal_counterexample','normal_case','failure_or_boundary_case','negative_evidence_search','acceptance_criteria'):
    assert f.get(k), (f['id'],k)
 return rows
BATCHES={
 'R5-U01':('内容、编译、本地化及通用内核',[]),
 'R5-U02':('地图、事件、移动及野外交互',['R5-U01']),
 'R5-U03':('个体、NPC队伍、储存、道具及邮件',['R5-U01']),
 'R5-U04':('战斗实际执行、效果与异常调度',['R5-U03']),
 'R5-U05':('AI评分与实际执行的对应',['R5-U04']),
 'R5-U06':('资源选择、演出时间及界面操作',['R5-U02','R5-U03','R5-U04','R5-U05']),
 'R5-U07':('开发工具、内容编辑与转换',['R5-U01','R5-U03','R5-U06']),
 'R5-U08':('有限跨批整合、实际字节复审与登记',['R5-U01','R5-U02','R5-U03','R5-U04','R5-U05','R5-U06','R5-U07'])}
CATALOGS={
 'M03':['deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md','deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md'],
}
def planned_files(f):
 out=list(f['affected_files'])
 if f['module']=='M01' and int(f['id'].rsplit('-',1)[1])>=19:
  # Finite new author-input cases need a concrete current vector receiver.
  out.append('deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md')
  if f['id'] in ('GR5-M01-021','GR5-M01-022','GR5-M01-027'):
   out.append('deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md')
  if f['id']=='GR5-M01-031':
   out.append('deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md')
 # Vector receiver additions are selected per finding, not a blanket permission to alter all catalogs.
 if f['module']=='M03':
  if f['id']=='GR5-M03-011':name='pokemon-rules-wp53-60-61-62-69-70.md'
  elif f['id'] in ('GR5-M03-007','GR5-M03-008'):name='engine-overworld-wp11-15-59-60.md'
  else:name='engine-overworld-wp11-15-59-60.md'
  target='deliverables/final-specification-set/test-catalog/'+name
  if not (W/target).exists():
   candidates=list((W/'deliverables/final-specification-set/test-catalog').glob('*11*'))
   raise ValueError(('catalog needs actual receiver',f['id'],target,[str(x)for x in candidates]))
  out.append(target)
 return sorted(set(out))
def batch_plan(rows):
 required=[f for f in rows if f['disposition']=='required'];byfile=collections.defaultdict(set);byid={}
 for f in required:
  fs=planned_files(f);byid[f['id']]=fs
  for p in fs: byfile[p].add(f['batch_owner'])
 owners={p:('R5-I' if len(bs)>1 else next(iter(bs)))for p,bs in byfile.items()}
 batches=[]
 for k,(title,deps) in BATCHES.items():
  rr=[f for f in required if f['batch_owner']==k];fs=sorted({p for f in rr for p in byid[f['id']]})
  batches.append({'id':k,'title':title,'finding_ids':[f['id']for f in rr],'dependencies':deps,
   'author_role':'独立规格修订作者；gpt-6.1-sol / xhigh / default / 禁Fast',
   'independent_reviewer_role':'非本批作者；gpt-6.1-sol / ultra / default / 禁Fast',
   'fixed_input':{'formal_commit':B5,'reference_commit':RC,'report_snapshot':'由最终manifest的review_snapshot绑定'},
   'allowed_formal_files':fs,'direct_writer_files':[p for p in fs if owners[p]==k],
   'shared_fragments_for_single_writer':[p for p in fs if owners[p]=='R5-I'],
   'acceptance':'逐项执行本批findings的static验收；保留正常/失败/取消/部分提交与既有正确合同。独立候选复审后，由R5-I按依赖顺序整合，再由非作者复审实际commit/tree及限定字节；登记者只能登记已满足条件的限定贡献。候选PASS不等同正式接受。',
   'parallel_preparation':'可并行只读准备及在独立候选目录撰写本批片段；依赖完成前不得整合、接受或关闭对应问题。',
   'execution':'无宿主或媒体时以静态事实验收，不伪造运行PASS；若新增执行，先明确输入、命令、边界和输出。'})
 return {'schema_version':'gr5.update-batches.v1','complete_plan':False,'batches':batches,'finding_file_permissions':byid,'dependency_edges':[[p,k]for k,(_,ds)in BATCHES.items()for p in ds]}, {'schema_version':'gr5.shared-file-owners.v1','owner_rule':'每个正式路径只有一个实际写者。共享文件R5-I接收各批片段后按限定scope整合；最后贡献到齐前不得关闭整份共享文件。','files':[{'path':p,'writer':owners[p],'contributing_batches':sorted(bs),'findings':[f['id']for f in required if p in byid[f['id']]],'historical_files_writable':False}for p,bs in sorted(byfile.items())]}
FIELD_LABELS={
 'id':'发现编号','title':'标题','module':'领域','severity':'严重度','disposition':'处置','status':'状态','reviewer':'提出及审查角色','category':'分类',
 'source_anchors':'固定参考锚点及直接事实','spec_anchors':'当前规格锚点及表述','expected_reference_behavior':'参考实际行为','current_spec_behavior':'当前规格行为','gap':'差异',
 'preconditions':'完整前提','minimal_counterexample':'最小反例','normal_case':'正常对照','failure_or_boundary_case':'失败或边界对照','negative_evidence_search':'反证范围与排除依据',
 'impact_on_independent_implementation':'对独立实现的影响','proposed_spec_change':'最小规格修订','affected_files':'发现所涉及文件','shared_contracts':'共享合同',
 'acceptance_criteria':'逐项验收标准','dependencies':'依赖','related_capabilities':'相关能力','related_findings':'关联发现','root_cause_group':'根因组','priority':'优先级','batch_owner':'唯一主责批次',
 'history_links':'GR4、GR3及旧229/341限定关系','evidence_level':'证据类别','execution_status':'实际执行边界','confidence':'置信依据','unknowns':'仍未知事项','excluded_claims':'明确排除的主张','user_decision_needed':'用户决策边界','review_resolution':'独立反证及最终裁决',
 'source_baseline':'固定参考版本','specification_baseline':'固定规格版本','required_subscopes':'必修子范围','optional_facets_not_authorized_as_required':'不属必修的可选方面','no_required_revision_facets':'无需修订的方面','affected_consumer_reverse_review':'受影响消费者的反向复查','merged_provenance_ids':'合并的提出编号',
 'required_receiver_files':'必修承接文件','required_shared_contract_owner':'共享合同唯一归属','item_identity_legend':'道具身份对照','order_and_mathematics':'顺序与数学规则'}
HANDOFF_RULES='''## 目标、输入和授权

这是用户在第五轮Desktop独立审查完成后，另行交回并明确要求开始时才执行的第五次云端update任务书。本文件的生成、发布或被读取不自动启动整改。长期目标是从固定Pokémon Essentials参考中提取完整、准确、实现独立的行为规格，供日后从零实现高质量新引擎。本次只修订规格及必要测试/附表/追溯，不实现框架，不移植Ruby，不采用原类层级或组织作为新架构，不替未来TypeScript引擎选择框架。

参考目录只读；正式基线B5固定，不能用浮动main暗换输入。固定源的实际缺陷、异常、时序和部分提交如实描述，未来是否长期兼容它们是另一决策。每条必修的全部前提、正常/反例/失败、排除范围及静态验收都在下文展开。源路径与符号仅供审计；新规格应以领域事实、表、数学、顺序和可独立推出的案例表达，不复制源实现。

用户后续授权执行本任务后，可在本文件必修和有限允许文件内组织作者、真正独立复审、实际整合复审、登记及普通push整改分支，并持续推进依赖已满足的后继批次。不得合并或push main、force、改写参考或冻结历史、启动实现工程、将可选或未决政策擅自转为必修。用户以后有新指示时以最新明确指示为准。

## 启动步骤及角色

1. 核验下列固定报告、handoff、manifest身份、B5/R与当前正式子树；核对必要产物的完整bytes、SHA256和Git blob。保护现有tracked/untracked/ignored、stash和worktree，不reset/clean/自动stash或覆盖。发现漂移列实际差异；B5可读则隔离继续，不以重新做一遍全局review替代整改。
2. 在独立整改分支/工作目录准备本轮状态账。先读对应发现、唯一文件写者、批次依赖和限定验收；只读准备可并行，实写按本任务的单一写者规则。
3. 作者、修订与登记者请求gpt-6.1-sol、reasoning_effort=xhigh、service_tier=default；独立review请求gpt-6.1-sol、reasoning_effort=ultra、service_tier=default。均禁Fast。第五轮Desktop审查用的是gpt-6-astra/ultra/default，不能混用两个阶段约定。请求成功即可继续，回显不可得记UNVERIFIED，不查额度、认证、后端或私有会话，不改全局配置求证明；明确拒绝时说明，不静默换模型。
4. 每位作者/审者只写自己候选/复审目录，登记真实任务ID、角色、固定输入、范围、输出、模型请求和状态。共享正式文件由R5-I唯一整合写者处理；非共享文件的内容写者按shared-file-owners指定，R5-I只机械接入其已独立通过的精确字节，不另作语义改写。保持可见进度，已完成语义不因导航变化反复重审。

## 修订、验收、实际整合和登记门

每个必修只归一个主责批次。作者先提交有完整输入身份和最小改动的候选，列逐条差异、所有同步接收文件、原来正确的行为、前提、推导向量及未运行边界。禁止修改已冻结历史报告、旧接受账或旧失败记录来消除冲突；历史应由新后继登记解释。当前有效补充若需要同步，只修改本批明确允许的现行接收物，保留旧候选/复审字节。

非作者独立审者必须实际读候选差异、固定R必要路径和当前承接正文/附表/测试/共享条款，逐项核查本任务验收标准与反向对照。输出按发现及限定贡献的结论；不能凭作者声明、文件同名、旧PASS或机械格式通过批准。一次有效质疑和一次定向整合即可过门；只有新证据或实质改动才重开，不无限review review。

候选通过不等于正式接受。R5-I只在本批所有依赖所需贡献已接受后，把通过的精确片段实际整合至规定正式路径，生成实际commit/tree及受影响文件bytes/SHA256/blob清单。真正独立审者再对实际字节复审，确认精确语义、附表/向量、消费者和限定旧控制保持。共享文件须等全部依赖贡献到齐后才可作整份接收；任何未到依赖不提前关闭。

唯一登记者只依据已绑定实际字节、独立复审和依赖握手的证据记录接受。每个问题的全部必修子范围、必需同步文件、受影响消费者和历史限定关系满足后才CLOSED；局部接受只能登记该scope。可选/未决仍保留自己的状态。若失败或有争议，保留原证据、指出具体条件和最小恢复项，继续无依赖工作，不把候选PASS转签给新字节。

## 回归和共享合同

逐批复查本次受影响的正常、异常、取消、先写后失败、回退、缓存、显示读取及持久读取；别把一个调用者的规则扩张到其它入口。共享合同主身份及生产→写入→消费→展示→持久/清理顺序见下文和shared-contracts。主规则只写一处，其余是有条件消费者引用，不复制成多份互相冲突的规则。

GR4的17控制/76标准、GR3的23控制/76标准和旧229控制/341精确贡献均保持原owner/scope资格。第五轮已重新比较当前事实：GR4为16控制/75标准supported，余下Summary表述由GR5-M04-002承接；不能据此篡改R4当时CLOSED或声称已证明是整改引入。GR3全部23/76在限定范围supported；GR3-M09-001保持OPTIONAL、U08未启动，GR3-M02-003保持NO_REQUIRED。旧341各限定当前关联见回归账，不扩成整个ID/整个能力通过。

本次新发现有单独GR5身份；邻近旧项只做精确关系与反向保护，不以主题相似乱配旧编号。所需回归是当前受影响条件的静态或有条件运行验证，不能通过历史身份一致继承旧语义签名。末批R5-U08核全部必修、依赖DAG、共享文件、当前Feature Matrix/两向映射及接受登记一致，禁止把低风险导航更新当新全局语义审查。

## 运行与材料边界

固定R没有完整地图、事件、Graphics/Audio及完整示例工程；原生Windows/RGSS/mkxp/.NET宿主未建立。两个根BMP存在且像素已读；八字体、soundfont和可恢复内嵌程序有具名静态范围。Game.exe/运行库机器码的完整控制流、GPU实际选用/像素、原生字体/合成声音和完整Demo均未验证。可读有限材料的完成与这些边界分开，不把已存在二进制叫作缺失文件，也不把仅格式/导入名检查叫作全机器码语义完成。

R4本地review四条隔离参考执行保留，R4云端update新增执行零。R5新增四条隔离参考执行；具体案例、替身、失败进程与成功进程均在execution-evidence，记录条数不是案例数量。R5独立模型、原生宿主及Demo执行零。新写的静态向量是DERIVED_VECTOR，格式、hash、链接、解析与数量是TOOL_VALIDATION，均不是运行PASS。

静态修订不要求伪造缺宿主的运行验收。确需新隔离执行时，先写所区分行为、固定版本、命令、输入、输出目录及副作用，再在已授权安全条件执行；不改参考、真实存档、生产账户，不擅自安装软件/更改安全配置/取得凭据或外传参考。记录实际exit、输出与业务结果，捕获异常的exit0不等于业务成功。不能用少量运行样本签全部静态范围。

本轮可选资源剖面和兼容政策均不自动执行。兼容选择不清楚但事实已明确时，记录design_decision/unresolved_policy并继续必修；只有确需用户决定的步骤才提问。
'''
def markdown_value(v,depth=0):
 if v is None:return '无。'
 if isinstance(v,bool):return '是。' if v else '否。'
 if isinstance(v,str):return v
 if isinstance(v,(int,float)):return str(v)
 if isinstance(v,list):
  if not v:return '无。'
  return '\n\n'.join(f'（{i+1}）'+markdown_value(x,depth+1)for i,x in enumerate(v))
 return '\n\n'.join('**'+FIELD_LABELS.get(str(k),str(k))+'：** '+markdown_value(x,depth+1)for k,x in v.items())
def render_finding(f):
 out=[f"### {f['id']} · {f['severity'] or '—'} · {f['title']}"]
 for k,v in f.items():
  if k in ('id','title','schema_version','canonical_input'):continue
  out.extend(['', '**'+FIELD_LABELS.get(k,k)+'**', '',markdown_value(v)])
 return '\n'.join(out)
def assemble_regressions(rows):
 """Copy the accepted finite ledger and append qualified late canonical relations."""
 reception=input_ref('modules/C00/REG-final-reception.json')
 for name in ('regression-fourth-17.json','regression-third-23.json','regression-legacy-scope.json'):
  d=read('modules/REG/'+name)
  assert d['complete'] is True
  d['parent_reception']=reception
  d['canonical_input']=input_ref('modules/REG/'+name)
  d['relative_reference_base']='modules/REG/'
  d['root_adjudication']={
   'historical_status_unchanged':True,
   'current_review_is_new_static_comparison':True,
   'execution':'本账本无新增参考/模型/宿主执行；历史执行仅按原记录限定引用。',
   'fourth':'17个原控制和76标准均实际复查；16控制/75标准supported，GR4-M04-001的C01为partial，其Summary残留由GR5-M04-002接收。不是证明R4整改引入回归，也不改写旧CLOSED。',
   'third':'23个原必修及76标准均在各自限定范围supported；GR3-M09-001保持OPTIONAL/U08未启动，GR3-M02-003保持NO_REQUIRED。',
   'legacy':'229控制/341贡献的原owner、local scope和资格均保留；当前事实逐条复查，不能将其结果扩大到整项产品能力。',
   'late_primary_completion':'REG中Q8/Q9等保留的M05待交接措辞是冻结过程注记；M05最终实审及C05的006/007反证均已完成，按C00/M05-final-reception.json接收；原限定范围不扩张。',
   'duplicate_correction':'M05-005归并M12-101；M12-102只为相邻编辑器投影，不取代101。'}
  if name=='regression-legacy-scope.json':
   d['history_relationships']='modules/REG/history-relations.json'
   old=read('modules/REG/history-relations.json')['records']
   known={x['finding_id'] for x in old}
   d['canonical_history_relations']=copy.deepcopy(old)
   for f in rows:
    if f['id'] not in known:
     d['canonical_history_relations'].append({'finding_id':f['id'],'scope_relation':'late_canonical_qualified_relation','history_links':f['history_links'],'root_cause_group':f['root_cause_group'],'related_findings':f['related_findings'],'canonical_disposition':f['disposition'],'historical_status_modified':False,'boundary':'只复用各所列身份/限定范围；无明确旧控制对应时不凭路径或主题猜配229/341编号。','canonical_input':f['canonical_input']})
   d['canonical_history_count']=len(d['canonical_history_relations'])
  write(name,d)
if __name__=='__main__':
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('--inspect',action='store_true');args=ap.parse_args()
 if args.inspect:
  ff=findings(); print(json.dumps({'count':len(ff),'dispositions':dict(collections.Counter(f['disposition']for f in ff)),'required_severity':dict(collections.Counter(f['severity']for f in ff if f['disposition']=='required'))},ensure_ascii=False))
 else: raise SystemExit('No publishing or final generation default. Parent explicitly assembles after semantic closure.')
