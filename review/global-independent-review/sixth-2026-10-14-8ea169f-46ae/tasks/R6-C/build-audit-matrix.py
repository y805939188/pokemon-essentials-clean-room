import json,re,hashlib,collections
from pathlib import Path
b=Path(__file__).parent; inv=json.loads((b/'inventory.json').read_text()); ledger=[json.loads(x)for x in(b/'reading-ledger.jsonl').read_text().splitlines()];facts=[json.loads(x)for x in(b/'forward-map.jsonl').read_text().splitlines()]
# This helper computes indices from already-read files. It never marks an unread span as read.
read={}
for r in ledger:
 if r['status']=='READ':read.setdefault(r['path'],set()).update(range(r['start'],r['end']+1))
owned=[r for r in inv if r['kind']=='source' and any(x in r['path']for x in ['/001_Battle/','/002_Battler/','/004_Scene/','/007_Other battle code/'])]
owned.extend(r for r in inv if r['kind']=='source' and '002_BattleSettings.rb'in r['path'])
units=[]
for r in owned:
 p=r['path'];lines=Path(p).read_text().splitlines();markers=[]
 for i,t in enumerate(lines,1):
  m=re.match(r'^\s*def\s+([^\s(]+)',t);h=re.match(r'^Battle::(Ability|Item)Effects::(\w+)\.(add|copy)\((.*)',t)
  if m:markers.append((i,'method',m.group(1),None))
  elif h:markers.append((i,'handler-'+h.group(3),h.group(2),h.group(4)))
 if not markers:markers=[(1,'bounded-state-data',Path(p).stem,None)]
 elif markers[0][0]>1:markers.insert(0,(1,'file-state/metadata-prefix',Path(p).stem,None))
 for k,(a,typ,name,body)in enumerate(markers):
  z=markers[k+1][0]-1 if k+1<len(markers)else len(lines)
  if typ.startswith('handler'):
   if lines[a-1].rstrip().endswith(')'):z=a
   else:
    for j in range(a,min(z,len(lines))):
     if (typ=='handler-copy' and ')' in lines[j]) or lines[j]==')':z=j+1;break
  linked=[f['fact_id']for f in facts if f['source']['path']==p and f['source']['start']<=z and a<=f['source']['end']]
  spans=[f['consumer']for f in facts if f['fact_id']in linked]
  units.append({'unit_id':f'R6-C-U{len(units)+1:04d}','path':p,'start_line':a,'end_line':z,'audit_unit_name':name,'unit_kind':typ,'sha256':r['sha256'],'blob':r['blob'],'actual_new_read':all(x in read.get(p,set())for x in range(a,z+1)),'linked_fact_ids':linked,'consumer_clauses':spans,'disposition':'FRESH_READ_WITH_NAMED_FACT_PARENT'if linked else 'FRESH_READ_AUDIT_COMMENT_CONTAINER'if typ=='file-state/metadata-prefix'else 'FRESH_READ_FORWARD_JOIN_PENDING','evidence':'SOURCE_STATIC','aggregate_pass':False})
(b/'source-unit-index.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n'for x in units))
owned_formal=[r['path']for r in inv if r['kind']=='formal' and (any('/'+x in r['path']for x in ['wp39-','wp40-','wp41-','wp42-','wp45-','wp49-','wp38-','wp48-','wp50-'])or'/test-catalog/'in r['path']and any(x in r['path']for x in ['wp39-40-41-42-45','wp49-51-52','wp31-32-37-38','wp43-44-46-48-50']))]
owned_formal.append('deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md')
vectors=[json.loads(x)for x in(b/'test-vector-map.jsonl').read_text().splitlines()] if (b/'test-vector-map.jsonl').exists() else []
vector_index={(v['path'],v['line']):v for v in vectors}
manual=[json.loads(x)for x in(b/'manual-clause-joins.jsonl').read_text().splitlines()] if (b/'manual-clause-joins.jsonl').exists() else []
peer=[json.loads(x)for x in(b/'peer-clause-joins.jsonl').read_text().splitlines()] if (b/'peer-clause-joins.jsonl').exists() else []
blocks=json.loads(Path('review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/inventory/formal-block-denominator.json').read_text());out=[]
for q in blocks:
 if q['path']not in owned_formal:continue
 p=q['path'];a=q['start_line'];z=q['end_line'];lines=Path(p).read_text().splitlines();t='\n'.join(lines[a-1:z]);fresh=all(i in read.get(p,set())for i in range(a,z+1));links=[f for f in facts if f['consumer']['path']==p and f['consumer']['start']<=a and z<=f['consumer']['end']]
 row={'block_id':q['id'],'path':p,'start_line':a,'end_line':z,'actual_new_read':fresh,'evidence':'SOURCE_STATIC','aggregate_pass':False,'fact_ids':[f['fact_id']for f in links],'source_units':[f['source']for f in links]}
 if p.endswith('wp67-a-battle-interaction-and-presentation.md') and a<=228<=z:
  row.update(disposition='EXTERNAL_PROPOSAL_R6-UI-001_ROOT_DECIDES',source_units=[{'path':'reference/pokemon-essentials/Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb','start':35,'end':80}],reason='pause与delete顺序冲突由UI提案及C独立新source/正式段核；不另立重复C根因')
 elif not fresh:row.update(disposition='NOT_YET_READ',reason='未被真实ledger覆盖，不以链接或hash补阅读')
 elif re.match(r'^\s*(#+\s|---\s*$|\|\s*[-:]+)',t):row.update(disposition='STRUCTURAL_CONTAINER_NEW_READ',reason='本块为标题/分隔/表头结构，只连接正文语义；不独立构成可执行行为证明')
 elif 'wp40-'in p and a<=84<=z:row.update(disposition='PROPOSAL_GR6-C-002_ROOT_DECIDES',reason='禁用身份条件消费者由具名提案与非提出者反证支持，最小84行修订由root裁决')
 elif any(j['path']==p and j['start']<=a and z<=j['end'] for j in peer):
  js=[j for j in peer if j['path']==p and j['start']<=a and z<=j['end']];row['source_units']=[v for j in js for v in j['source_units']];row['peer_source_receipts']=js;row.update(disposition=js[0]['disposition'],responsible_domain=js[0]['responsible_domain'],reason=js[0]['semantic_assessment'])
 elif links:row.update(disposition='FRESH_STATIC_MAPPING_WITH_ENTRY_PREMISES',reason='本轮全文与具名单位核对；source与入口前提见fact，不升级为宿主观察或全域PASS')
 elif '/test-catalog/'in p and (p,a) in vector_index and a==z:
  v=vector_index[(p,a)];row['vector_id']=v['id'];row['vector_owner']=v['owner'];row['source_units']=v.get('source_pipeline',[])+v.get('identity_specific_source_units',[]);row['vector_evidence']=v
  if v['status']in['STATIC_VECTOR_ENTRY_PREMISES_REVIEWED','DELEGATE_RESULT_RECEIVED_PREMISES_REVIEWED_BY_CA','EXTERNAL_SHADOW_BINDING_RECEIVED_CORE_REVIEWED','CM_PRODUCER_REVIEW_RECEIVED_C_CORE_CONSUMER_JOINED','CM_NAMED_CONTROL_FIELD_PRODUCERS_RECEIVED_C_CONSUMERS_JOINED','CURRENT_O_WORLD_SOURCE_RECEIPT_JOINED_C_CORE','CURRENT_K_PRIMARY_AND_NECESSARY_CONSUMER_FACTS_RECEIVED']:
   row.update(disposition='FRESH_STATIC_VECTOR_WITH_NAMED_CONSUMERS',reason='该向量及全部前提全文亲读；具名source单位/身份/独立委派的具体derive记录接合；未执行战斗')
  else:row.update(disposition='FRESH_VECTOR_NAMED_DOMAIN_JOIN_PENDING',responsible_domain=v['owner'],reason=v.get('assessment','按具体derive前提等待独立domain source结果'))
 elif '/test-catalog/'in p:
  row.update(disposition='STATIC_CATALOG_SCHEMA_FIXTURE_OR_SCOPE_REVIEWED',reason='本轮整篇逐行阅读的表头/共同输入/不执行及跨目录界限；共同夹具随各vector record保留，不把输入声明计运行PASS');out.append(row);continue
  domain='R6-CA'if'wp49-51-52'in p and a>=43 else 'R6-CM'if'wp43-44-46-48-50'in p and a<137 else 'R6-K/R6-O'if'wp31-32-37-38'in p and a<138 else 'R6-C'
  row.update(disposition='FRESH_TEST_VECTOR_CONSUMER_JOIN_PENDING',reason='整块静态向量全文已读；需精确连接该向量生产者/消费者，不将目录已读当已执行测试',responsible_domain=domain)
 elif t.startswith('分类：') or (t.startswith('|') and any(x in t for x in ['| 术语 |','| ID |','| 配置/数据 |','| 身份 |','| 族 |','| 族/身份 |','| 角色 |'])):
  row.update(disposition='CLASSIFICATION_OR_TABLE_SCHEMA_NEW_READ',reason='分类/列名与本文件正文责任核对；结构身份不构成独立运行行为或未来架构')
 elif any(s in t for s in ['未运行','无运行','没有参考运行','上游：','下游：','前置依赖','完成依赖','示例场景','已 CLOSED','性质：','目的**','范围**','未来 API','不设计','目录记录是行为作用域','注册名仅追溯','参数、对象、有效性和消费','持久 HP/状态/持物','均已限定通过','覆盖**','目的、范围','| 免疫身份 |','回源核对','不能从名字','**WP67-A 完成','未决','未验证','未执行','待运行','非目标','不定义','不是已执行','前向','测试目录','证据定位','工作包','审计材料','Source','traceability']):row.update(disposition='SCOPE_OR_AUDIT_METADATA_NEW_READ',reason='本轮审计边界/链接/状态文字检查；历史限定通过不当本轮PASS，实际执行为0')
 elif 'wp39-'in p and (47<=a<125 or 227<=a<278):row.update(disposition='CROSS_DOMAIN_JOIN_R6-O_PENDING',reason='本formal真实全读，创建包装/音频/世界输入source在O主审；待其本轮具名接口记录接合',responsible_domain='R6-O')
 elif 'wp42-'in p and 203<=a<261:row.update(disposition='CROSS_DOMAIN_JOIN_R6-O_K_PENDING',reason='核心已读，外层世界善后/进化/拾取source需O/K本轮证据；不以旧限定通过替代',responsible_domain='R6-O/R6-K')
 elif 'wp45-'in p and (147<=a<178 or 83<=a<91):row.update(disposition='CM_NAMED_PRODUCER_FACTS_RECEIVED_C_CONSUMERS_JOINED',reason='CM新全文场域/清场/交换producer逐unit事实已收到，与C ownedcore consumer接合；不升任意插件/组合 PASS',responsible_domain='R6-CM',peer_receipt_artifact=str(b/'received-CM-control-field-units.json'))
 elif 'wp45-'in p and 34<=a<=38:
  row.update(disposition='CROSS_DOMAIN_JOIN_R6-O_PENDING',responsible_domain='R6-O',reason='创建世界标识/类别和默认来源由O新读prepareBattle source，需要精确消费者接合')
 elif any(j['path']==p and j['start']<=a and z<=j['end'] for j in manual):
  js=[j for j in manual if j['path']==p and j['start']<=a and z<=j['end']];row['source_units']=[v for j in js for v in j['source_units']];row['manual_semantic_assessments']=js;row.update(disposition=js[0]['disposition'],responsible_domain=js[0]['responsible_domain'],reason=js[0]['semantic_assessment'])
 elif 'wp45-'in p and (147<=a<178 or 83<=a<91):
  row.update(disposition='CM_NAMED_PRODUCER_FACTS_RECEIVED_C_CONSUMERS_JOINED',reason='CM current完整控制/场域producer逐unit事实接合C core已读consumer',peer_receipt_artifact=str(b/'received-CM-control-field-units.json'))
 else:row.update(disposition='FRESH_READ_REVERSE_JOIN_PENDING',reason='已全文真实阅读；尚未给本块精确consumer与前提关联，明确未闭合',responsible_domain='R6-C')
 out.append(row)
(b/'formal-block-matrix.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n'for x in out))
summary={'source_units':len(units),'source_units_actual_read':sum(x['actual_new_read']for x in units),'source_unit_dispositions':dict(collections.Counter(x['disposition']for x in units)),'formal_owned_files':len(owned_formal),'formal_blocks':len(out),'formal_blocks_actual_new_read':sum(x['actual_new_read']for x in out),'block_dispositions':dict(collections.Counter(x['disposition']for x in out)),'read_complete':False,'mapping_complete':False,'note':'Pending rows are outstanding work, not exceptions used to close review.'}
(b/'matrix-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n');print(json.dumps(summary,ensure_ascii=False,indent=2))
