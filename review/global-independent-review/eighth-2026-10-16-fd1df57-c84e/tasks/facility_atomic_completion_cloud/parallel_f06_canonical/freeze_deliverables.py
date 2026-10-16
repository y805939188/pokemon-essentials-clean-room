from pathlib import Path
import json,hashlib,datetime
rr=Path.cwd();p=rr/'tasks/facility_atomic_completion_cloud/parallel_f06_canonical'
def read(f):return json.loads((p/f).read_text())
def dump(f,x):(p/f).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
packet=read('canonical-meaning-packet.json');facts=read('received-facts.factored.json');nf=read('necessary-new-meanings.json');frozen=read('frozen-inputs.json');ids={a['id'] for a in facts['rows']};nids={a['id'] for a in nf['facts']};case=read('received-cases.exact.json');cids={a.get('case',a.get('id')) for a in case['cases']};missing=[]
for row in packet['structures']:
 for ref in row['support_refs']:
  if ref.startswith('FAC-A') and ref not in ids:missing.append(ref)
  if ref.startswith('F06-S') and ref not in nids:missing.append(ref)
  if ref.startswith('SF') and ref not in cids:missing.append(ref)
assert not missing,missing
assert {a['old_locator_id'] for a in frozen['targets']}=={a['old_locator_id'] for a in packet['structures']}
assert len(ids)==len(facts['rows'])==441
assert all(a['actual_read']=='ACTUAL_COMPLETE_NAMED_UNIT_READ' for a in nf['facts'])
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
validation={'schema':'gr8-f06-mechanical-reference-validation/v1','utc':now,'fixed_B8':packet['fixed_B8'],'fixed_R':packet['fixed_R'],'formal_lines_actually_read':288,'target_structures':156,'disposition_structures':len(packet['structures']),'manual_components':sum(len(a['components']) for a in packet['structures']),'finite_parent_facts_actually_received':441,'parent_fact_common_envelopes':len(facts['common']),'finite_case_rows_actually_received':34,'finite_case_children_actually_received':208,'finite_save_child_count':36,'new_necessary_child_fact_groups':len(nf['facts']),'missing_exact_refs':missing,'claimed_full_or_global_PASS':False,'unresolved_classification':['F06-ORDER-START'],'new_required':0,'new_optional':0,'new_decision_votes':0,'actual_new_contexts':1,'business':'NOT_EXECUTED','semantic_qualification':'Mechanical ID/count/identity checks give no reading/entailment credit. All481 components manually authored after actual whole formal and finite semantic receipt. L120 ordering requires nonproposer counter.','UPDATE_NOT_STARTED':True}
dump('validation.json',validation)
dump('support-reference-membership.json',{'qualification':'Mechanical membership only. All authoring ranges expanded to explicit IDs; Save aliases resolved.','missing_referenced_parent_facts':[],'parent_finite_facts_received':441})
fr=read('finite-provider-receptions.json');fr['selected_facts']='All441 exact fact bodies including6 necessary critical-threshold/charm facts, plus14common envelopes and36source identities actually received; no inheritedFULL.';fr['fact_count']=441;dump('finite-provider-receptions.json',fr)
view=['F06 current WP53 Safari/Contest: all156 original structures /481 manually authored meaning components.','B8 '+packet['fixed_B8']+'; R '+packet['fixed_R'],packet['common_premise'],packet['shared_component_support_rule'],'L120 ordering undecided. No global/FAC PASS; runtime/Demo/opaque limits retained.','']
for row in packet['structures']:
 view.append(row['old_locator_id']+' ['+row['disposition']+'] refs='+','.join(row['support_refs']))
 for c in row['components']:view.append('  '+c['id']+' '+c['meaning'])
 if row.get('open_candidate'):view.append('  OPEN '+row['open_candidate'])
(p/'canonical-meaning-packet.complete.view.txt').write_text('\n'.join(view)+'\n')
dump('progress.json',{'schema':'gr8-f06-bounded-canonical-progress/v1','utc':now,'reader':packet['reader'],'status':'COMPLETE_MEANING_PACKET_PARENT_RECEPTION_PENDING_ONE_COUNTER','whole_formal':packet['whole_formal_actual_read'],'structures':156,'manual_components':481,'candidate':'ordering-candidate.eight-sections.json / ordering-candidate.necessary-readset.json','remaining_blockers':['Actual nonproposer classification of F06-ORDER-START','Parent actual full reception of481meaning components and17necessary join groups'],'actual_new_contexts':1,'new_votes':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True})
(p/'review.md').write_text('''F06 固定当前文件为 WP53 Safari/捕虫正文，共288行；初次派发的WP76标签已由父纠正。本子任务完整读正文并处置原dispatch全部156剩余结构，列出481个当前意义组件。结构数不是原子真分母；scope、历史资格引用、排版与未执行边界分别处置。

实际接收441条必要父FAC-A原意与14共同前提包络、34条SF共208子意义、旧Save六原行共36子意义、六项统计事实及I09/I10完整有限现行资格。17个必要薄源接点以子命名空间记录。35个普通源身份bytes/SHA匹配，Main保留既有惰性解码身份而无执行。截断输出及错误路径均补读，失败无信用。

一项候选F06-ORDER-START：L120“逐项”列缩队先于NPC采样，完整Start实际先采样再替换party。成功终态相同，采样错误可暴露不同中间队伍。最强反方是“逐项”仅列完成效果，不能把helper任意异常升级为未来公共兼容义务。八节合同与必要小单位readset已冻结，提出者不自标required或投独立票。其余155结构与L120正常终态可独立接收。

业务/RNG/模型/Ruby/游戏/编译/图证明/原生执行均0。时钟重载、媒体、真实写盘与roundtrip、宿主退出和Demo维持准确未知。待父全文接收新意义及root实际不同上下文有限裁决；无全FAC/global PASS。UPDATE_NOT_STARTED。
''')
dump('reading-ledger.json',{'instructions':['Applicable rootAGENTS full; globalprompt241lines; review-SKILL51lines (audit exclusion); full delegation prompt; full complete-readset1130lines with truncated gaps repaired.'],'formal':packet['formal'],'formal_actual_read':'All1–288, contiguous1–180/181–288','finite_semantic_receipts':['finite-provider-receptions.json','received-facts.factored.json','received-cases.exact.json'],'necessary_source_units':'necessary-new-meanings.json all17 exact complete named unit groups, not blanket whole source FULL.','identity_check':'source-identity-checks.json35regularmatches; Main finite inert identity retained.','execution':'Static Python file/identity/reference bookkeeping only; business NOT_EXECUTED.','skill':'clean-document-revision explicitly excludes audit records; no cloud skill applied.','scope_correction':'Parent confirmed F06 is WP53/156 structures, not mistakenWP76/279.','UPDATE_NOT_STARTED':True})
items=[]
for z in sorted(p.iterdir()):
 if z.is_file() and z.name!='artifact-manifest.json':
  b=z.read_bytes();items.append({'path':str(z.relative_to(rr)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
dump('artifact-manifest.json',{'schema':'gr8-f06-frozen-artifact-manifest/v1','utc':now,'scope':'Child F06/WP53 all156 original structures','files':items,'count':len(items),'manifest_self_hash':'Excluded; exact bytes/hash externally frozen by parent receipt.','global_or_FAC_PASS':False,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True})
for name in ['canonical-meaning-packet.json','canonical-meaning-packet.complete.view.txt','necessary-new-meanings.json','ordering-candidate.eight-sections.json','ordering-candidate.necessary-readset.json','artifact-manifest.json','validation.json']:
 b=(p/name).read_bytes();print(name,len(b),hashlib.sha256(b).hexdigest())
