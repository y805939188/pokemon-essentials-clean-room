"""One optional current auxiliary-material drift; no generator execution."""
import copy
import review_state as s
import review_ops as o
F='deliverables/final-specification-set/'
d=s.read('findings.json');x=copy.deepcopy(d['findings'][0])
path='Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb'
coverage=next(e for e in s.read('reading-coverage.json')['sources'] if e['path']==path)
x.update(id='GR5-M01-007',title='库存附录生成器与其旧输出仍把翻译导出目标选择标作游戏语言切换',
 severity='P3',priority='P3 optional',disposition='optional',status='candidate_pending_independent_counterevidence',
 category='auxiliary_material_drift',root_cause_group='M01-INVENTORY-LANGUAGE-ROLE-DRIFT',
 source_anchors=[dict(path=path,version=dict(commit=s.R,git_blob=coverage['git_blob']),lines=[1420,1463],
   symbol_or_data_keys='extract_text debug menu',caller_config='LANGUAGES author target; core/game selector',
   supporting_fact='选择语言片段传给翻译导出；不写玩家语言选项或重载当前游戏消息。后续取消类别在导出前返回。')],
 spec_anchors=[
  dict(path='analysis/inventory/wp02_build_appendix.py',version=s.B,lines=[156,156],section_or_vector='generated language-consumer row',current_statement='生成的消费说明仍为调试菜单切换语言。'),
  dict(path='analysis/inventory/out/wp02-settings-inventory-appendix.md',version=s.B,lines=[200,200],section_or_vector='§7.3 generated output',current_statement='旧输出同样把此入口列为调试菜单切换语言。'),
  dict(path='specs/kernel/wp02-settings-inventory-appendix.md',version=s.B,lines=[200,200],section_or_vector='§7.3 effective appendix',current_statement='已正确限定为作者导出目标，不改变玩家语言和当前消息。'),
  dict(path=F+'generic-kernel/wp02-rule-configuration-and-data-variants.md',version=s.B,lines=[237,244],section_or_vector='§6.3',current_statement='正式正文已区分玩家切换与作者导出。'),
  dict(path=F+'generic-kernel/wp08-localization.md',version=s.B,lines=[90,96],section_or_vector='§6.2',current_statement='正式本地化导出合同同样已正确。')],
 expected_reference_behavior='调试翻译提取选择B仅决定作者导出目标与所用翻译材料；当前玩家语言及消息集A保持。随后取消core/game选择也不写输出。',
 current_spec_behavior='现行正文与有效规格附录正确；辅助生成器的固定输出行及analysis/inventory/out旧产物仍保留错误角色。',
 gap='辅助材料之间存在可复现的语义漂移；将来重新生成该附录可能重新引入已经修正的角色误述。不是现行主规格缺失，也不是新的玩家切换缺陷。',
 preconditions=['固定B5辅助脚本与当前输出材料；固定R翻译提取回调','本轮仅阅读生成器固定文本，不执行它','重生成风险限该已读固定行，不推整个历史管理包失效'],
 minimal_counterexample=dict(input='静态检查生成器语言消费者表中的调试入口输出行',static_expected='该固定行仍会称“切换语言”，与当前正式§6.3及有效附录角色不同',execution='GENERATOR_NOT_EXECUTED'),
 normal_case=dict(input='当前正式WP02§6.3、有效附录§7.3与WP08§6.2',static_expected='均正确说明作者导出参数，不能据本项要求再次改写正确主合同'),
 failure_or_boundary_case=dict(input='当前游戏A、作者目标选B后取消core/game类别',static_expected='玩家/消息仍A，无导出；辅助说明不应把此当游戏语言切换'),
 impact_on_independent_implementation='直接按正确正式交付实现不受影响；依赖辅助生成材料或后续重生成时会误判语言状态写入点。',
 negative_evidence_search=[
  dict(path='analysis/inventory/wp02_build_appendix.py',read_ranges=[[1,191]],result='全文静态阅读；目标说明是固定生成文字，不是根据回调状态写入分析推得。未执行。'),
  dict(path='analysis/inventory/out/wp02-settings-inventory-appendix.md',read_ranges=[[1,236]],result='全文已读；旧输出保留同一角色。'),
  dict(path='specs/kernel/wp02-settings-inventory-appendix.md',read_ranges=[[1,236]],result='全文已读；有效附录已修正，是本项仅属辅助漂移的重要反证。'),
  dict(path=F+'generic-kernel/wp02-rule-configuration-and-data-variants.md',read_ranges=[[1,278]],result='正式主合同已正确，不能重复立主规格必修。'),
  dict(path=F+'generic-kernel/wp08-localization.md',read_ranges=[[1,191]],result='导出与运行切换分层已正确，相关静态向量已独立读源映射。')],
 proposed_spec_change='可选同步辅助生成器的固定角色说明；若后续获准重新生成，只更新对应辅助产物并核对有效附录，避免覆盖其已正确修订。主责正式规则无需因本项修改。',
 affected_files=['analysis/inventory/wp02_build_appendix.py','analysis/inventory/out/wp02-settings-inventory-appendix.md'],
 shared_contracts=['M01-CONFIG-DECLARATIONS','M01-LZ-EXPORT'],related_capabilities=['M01-CONFIG-DECLARATIONS','M01-LZ-EXPORT'],
 related_findings=[],dependencies=['auxiliary inventory maintenance owner'],history_links=[],
 acceptance_criteria=dict(static=['辅助说明与当前正式作者导出角色一致','保留现行已正确的玩家切换/导出分层','不把重新运行生成器视为本次已授权或已执行'],must_execute=[]),
 evidence_level='static_source_and_current_auxiliary_text_comparison',execution_status='NOT_EXECUTED; generator/reference/model not run',
 confidence=dict(source_behavior='high_static',contract_gap='high_for_exact_auxiliary_row'),
 unknowns=['未来是否继续保留该生成器由维护者决定','没有进行实际重生成或UI验证'],
 excluded_claims=['不重新打开现行已正确的WP02/WP08语言合同','不将纯名称/排版差异立必修；本项是可选语义漂移','不修改正式规格、历史证据或参考源'],
 user_decision_needed=dict(required_now=False,later_policy='维护者决定是否同步辅助生成工具；不阻塞当前正确正式规格的使用。'),
 review_resolution='可选候选待独立反证；不自签最终必修，不运行生成器。')
o.upsert('findings.json','findings',[x],'id')
print('Optional auxiliary drift recorded as GR5-M01-007')
