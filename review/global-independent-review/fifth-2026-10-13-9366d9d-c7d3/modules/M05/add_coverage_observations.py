import review_state as s
from pathlib import Path

d=s.load('findings')
def sa(path,lines,fact):
 return {'path':path,'version':s.R,'lines':lines,'caller_config':fact,'supporting_fact':fact}
def pa(path,section,text):
 return {'path':path,'version':s.B,'section':section,'current_statement':text}
def negative(path,ranges,result):return {'path':path,'version':s.B,'read_ranges':ranges,'result':result}
def base(id,title,root):
 return {'id':id,'title':title,'module':'M05','severity':'P3','disposition':'unresolved','status':'candidate_pending_independent_counterevidence','reviewer':d['reviewer'],'category':'bounded_contract_coverage','source_baseline':d['source_baseline'],'specification_baseline':d['specification_baseline'],'root_cause_group':root,'priority':'P3 coverage disposition for parent','batch_owner':'parent to assign; M05 business/M10 UI or author-facing boundary','history_links':[],'related_findings':[],'evidence_level':'static_semantic_review','execution_status':'not_executed; no reference/model/network execution','confidence':{'source_behavior':'high','absence_in_read_contracts':'high','required_revision_disposition':'unresolved'},'unknowns':['父会话对低层作者输入/事件辅助合同的必修范围裁决；不涉及尚未读取的指定源段。','宿主表现与Demo可达性未执行。'],'excluded_claims':['不是默认物品全部表现错误。','不要求未来保留参考类、方法或数组布局。','不把未找到合同等同功能不存在。'],'user_decision_needed':False,'review_resolution':{'own_counterevidence':'completed_for_bounded_coverage_observation','independent_counterevidence':'pending_parent_review','final_required_revision':'not_self_signed','disposition_meaning':'unresolved is a scope/priority judgment, not unfinished source reading'},'acceptance_criteria':{'static':[],'execution_required_now':False,'deferred_execution':'Only if parent separately authorizes a runtime objective; no execution needed to review these source/text facts.'}}
P='deliverables/final-specification-set/'
x=base('GR5-M05-006','Item 部分缺省与 ShowQuantity=false 的实际语义未在领域合同给全（覆盖裁决待定）','item.record-defaults-and-quantity-visibility')
x.update({
 'source_anchors':[sa('Data/Scripts/010_Data/002_PBS data/006_Item.rb',[119,137],'记录缺字段：Pocket1、Price0、BP1、两使用上下文0、空Flags；Consumable缺省与明确false分开。'),sa('Data/Scripts/010_Data/002_PBS data/006_Item.rb',[167,202],'重要性为KeyItem/HM/TM；普通物品即使ShowQuantity=false仍可显示数量，重要物品明确true才放行该查询。'),sa('Data/Scripts/016_UI/007_UI_Bag.rb',[1,115],'背包行数量消费show_quantity查询并受登记图标遮挡；无图标普通物是可观察输入。')],
 'spec_anchors':[pa(P+'generic-kernel/wp03-content-identity-and-schema.md','§4.3/§7','只举卖价一半/BP1等默认样本，完整字段交领域。'),pa(P+'creature-rpg/wp27-bag-and-item-storage.md','§8','给口袋配置/容量，未给记录缺Pocket和Price的完整默认。'),pa(P+'user-interface/wp66-c-bag-item-storage-and-shop-ui.md','§3.1','数量仅当物品显示数量且无登记图标，未说明明确false不能隐藏普通物。')],
 'expected_reference_behavior':'普通已登记非重要I、ShowQuantity=false、包中2件且无登记图标时，数量查询仍真，背包显示数量。省Pocket取1，省Price取0，省FieldUse/BattleUse取0；明确false Consumable则可不耗，不能把两布尔处理等同。',
 'current_spec_behavior':'规格给消费属性与重要物的主规则和若干价默认，显示侧仅委托“显示数量”查询；独立读者无法唯一决定这一明确false输入和所有记录缺省。',
 'gap':'属于输入/默认覆盖不足，而非已知正常默认物品的矛盾；是否必须把所有作者字段展开需要父会话裁决。',
 'preconditions':['已登记合法普通物I（不是KeyItem/TM/HM），ShowQuantity=false，2件在有效背包槽。','正常背包行无登记图标且资源正常；不改参考/不运行。'],
 'minimal_counterexample':'上述I的数量查询为真并显示x2；只按一般布尔字段直觉实现false→隐藏会得到不同结果。',
 'normal_case':'普通物未给ShowQuantity同样显示；重要物缺省不显示。记录已给合法Pocket/Price时保持所给数值。',
 'failure_or_boundary_case':'重要物明确ShowQuantity=true可使查询真，但UI登记图标仍可遮挡数量；不能只用查询真保证所有消费者都画数量。',
 'impact_on_independent_implementation':'可影响自定义物品缺省落袋/价格/可用性，以及作者设置false后背包是否显示数量。',
 'negative_evidence_search':[negative(P+'generic-kernel/wp03-content-identity-and-schema.md',[[1,240]],'全文默认/schema/字段归属没有完整Item缺省或ShowQuantity判定。'),negative(P+'creature-rpg/wp27-bag-and-item-storage.md',[[1,174]],'全文及BG01–31已读；只有重要物流程与显示约束。'),negative(P+'creature-rpg/wp28-item-use-and-training.md',[[1,346]],'全文消费分类与登记默认不等于记录缺省表。'),negative(P+'creature-rpg/wp29-shops-and-exchanges.md',[[1,208]],'价格覆盖/售价/BP语义已给；未补全记录缺Price。'),negative(P+'user-interface/wp66-c-bag-item-storage-and-shop-ui.md',[[1,203]],'全文只消费显示谓词，没有false/重要性矩阵。'),negative(P+'demo-dx/wp73-a-content-editors.md',[[1,174]],'作者字段清单/编辑器不提供该运行查询矩阵。')],
 'proposed_spec_change':'若归本轮完整作者输入合同，增一小表列已注册Item的缺省字段及两种布尔的独立判定；UI仅引用，避免设计具体API。若父会话明确排除这层覆盖，记录该范围排除而不称supported。',
 'affected_files':[P+'creature-rpg/wp27-bag-and-item-storage.md',P+'creature-rpg/wp28-item-use-and-training.md',P+'user-interface/wp66-c-bag-item-storage-and-shop-ui.md',P+'test-catalog/creature-rpg-wp27-28-29-30-33.md'],
 'shared_contracts':['item.record-defaults','inventory.quantity-visibility'],'dependencies':['WP03 content input','WP66-C display consumer'],'related_capabilities':['item.data'],
})
x['acceptance_criteria']['static']=['明确ordinary/important × 未给/false/true数量查询矩阵及图标遮挡层。','缺Pocket/Price/使用上下文与明确0/false区别由交付可唯一推导。','不声称所有默认数据当前都使用了缺省字段；不做文本描述准确性评价。']
d['findings']=[q for q in d['findings'] if q['id']!=x['id']]+[x]

x=base('GR5-M05-007','事件物品选择与变量转换仅有过滤入口概述，返回和部分写入合同未给全（覆盖裁决待定）','item.event-selection-and-conversion-contract')
x.update({
 'source_anchors':[sa('Data/Scripts/013_Items/001_Item_Utilities.rb',[859,917],'三个袋选择辅助取消返回空；正变量写NONE。列表按输入序保留重复，仅已有且持有者入选；空/取消写NONE。'),sa('Data/Scripts/019_Utilities/001_Utilities.rb',[489,520],'转换先严格解析当前物品、再清事件变量；成对首匹配；奇数尾忽略。物品目标原样写，物种目标先严格解析；失败可保留清空，且均不扣库存。')],
 'spec_anchors':[pa(P+'creature-rpg/wp27-bag-and-item-storage.md','§4.3','列树果/覆盖物/杏子/化石/驱虫等过滤消费者和游标恢复。'),pa(P+'user-interface/wp66-c-bag-item-storage-and-shop-ui.md','§2–3','选择画面回物品或nil；未包含事件变量适配和转换工具。'),pa(P+'engine-overworld/wp13-map-events-npc-followers.md','§4–5','一般脚本命令合同，不提供物品变量转换规则。'),pa(P+'demo-dx/wp77-demo-evidence-and-capability-coverage.md','§7/§9','Demo入口缺失和静态能力分开，不包含这些辅助的完整返回/写入合同。')],
 'expected_reference_behavior':'取消普通/球果/化石袋选择：函数返回空，正编号事件变量写NONE；列表选择过滤未知和未持有、保输入顺序/重复。转换不改背包：先解析现值，后清变量，再以成对首匹配写目标；转物种时目标查询失败会在清空后发生。',
 'current_spec_behavior':'只保证底层过滤选择和一般事件脚本，未唯一给出变量NONE与nil区别、首匹配/重复/奇数尾、无库存变化及失败前清空。',
 'gap':'可读静态辅助功能的合同粒度不足；真实Demo未给不能证明这批函数无行为。是否作为本轮必要事件能力或可选兼容适配由父会话裁决。',
 'preconditions':['事件变量V为合法POTION身份，合法源物品存在、事件变量/地图对象有效。','转换表第一匹配目标为未登记物种INVALID，后面可有其它有效配对；不执行参考。'],
 'minimal_counterexample':'物品→物种转换先把V清为空，查询INVALID失败；库存及个体集合不变，V不恢复POTION。只按“转换失败无变化”会不一致。',
 'normal_case':'V=POTION、首匹配目标为合法CATERPIE：V变规范CATERPIE身份；不生成个体、不消费POTION。未匹配则V保持刚清空的值。',
 'failure_or_boundary_case':'最初V不是已知物品时严格查询先失败，尚未清V；选择工具取消写NONE而不是转换无匹配后的空值；两种空结果不可合并。',
 'impact_on_independent_implementation':'事件条件分支可能读不同哨兵值；错误时是否清变量、是否消费材料会不同。',
 'negative_evidence_search':[negative(P+'creature-rpg/wp27-bag-and-item-storage.md',[[1,174]],'全文仅过滤消费者概述。'),negative('specs/creature-rpg/wp27-bag-and-item-storage.md',[[1,len((s.REPO/'specs/creature-rpg/wp27-bag-and-item-storage.md').read_text().splitlines())]],'原稿全文无独有详细转换合同。'),negative(P+'creature-rpg/wp28-item-use-and-training.md',[[1,346]],'全文主动效果/变量工具非同一功能。'),negative(P+'user-interface/wp66-c-bag-item-storage-and-shop-ui.md',[[1,203]],'完整选择/交易返回仅UI层。'),negative(P+'engine-overworld/wp13-map-events-npc-followers.md',[[1,190]],'全文无具体物品转换语义。'),negative(P+'demo-dx/wp77-demo-evidence-and-capability-coverage.md',[[1,230]],'全文未提供这些工具的运行合同。'),{'path':'deliverables/final-specification-set (B5 entire text navigation)','read_ranges':['literal helper names; 杏子/球果/化石/转换/选择列表 synonyms'],'result':'全树检索仅命中过滤/进化/挖矿等非同义合同；实际反证正文如上，搜索不单独充当语义证据。'}],
 'proposed_spec_change':'若在完整事件能力范围内，用输入/输出/提交顺序表补选择适配与转换语义，再给取消、无匹配、无效源、无效物种目标四类静态向量；不要求保留原方法名。',
 'affected_files':[P+'creature-rpg/wp27-bag-and-item-storage.md',P+'test-catalog/creature-rpg-wp27-28-29-30-33.md'],'shared_contracts':['item.event-selection','item.event-variable-conversion'],'dependencies':['WP03 strict identities','WP13 event variables','WP66-C selection'],'related_capabilities':['item.event-tools']})
x['acceptance_criteria']['static']=['分别给函数返回和事件变量最终值，不把NONE与空值合并。','表过滤/重复/首匹配/奇数尾/源与目标失败的提交前缀明确。','不推成实际化石复活/球果换球Demo链，不添加未发生的库存扣除或个体生成。']
d['findings']=[q for q in d['findings'] if q['id']!=x['id']]+[x]
s.save('findings',d)
