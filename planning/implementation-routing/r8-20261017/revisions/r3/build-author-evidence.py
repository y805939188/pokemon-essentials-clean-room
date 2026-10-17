
# Historical author step: never overwrite later calibrated evidence.
import hashlib as _r3_hashlib, pathlib as _r3_pathlib
_r3_guard_manifest = _r3_pathlib.Path(__file__).resolve().parent.parent.parent / 'routing-manifest.json'
if _r3_hashlib.sha256(_r3_guard_manifest.read_bytes()).hexdigest() != '35175c7094b008e77af35cf6a7811c5fcd6f1a0dd20020b64d32b40d5670256e':
    raise SystemExit('Historical R3 author step refuses changed/final manifest; use fixed archive and recorded patch for audit.')
import json,pathlib,subprocess,hashlib,datetime,re
ROOT=pathlib.Path('/workspace/r8-disposition-tagging'); H=ROOT/'planning/implementation-routing/r8-20261017'; R=H/'revisions/r3'; P=pathlib.Path('/tmp/r8-cumulative-8336249c'); FINAL='5f87743293290de2e219ecdd6c19e88280f60c9a'; B8='fd1df570cad987dc3852a3b958f03916e317f7fe'; DELIVERY='4575e80d041ab0c74a42e2e36399d05791dbaa5b'; OLD='a32873d2860b15d9f5e27727db8f131f4ec433b6'; PACKAGE='8336249c78b4698cd77445653d3b05ff6a76ce94'; INTER='0eee6d141f33758eda34bd8ebad94a3e2b617f5a'
def git(*a):return subprocess.check_output(['git',*a],cwd=ROOT)
def show(c,p):return git('show',c+':'+p)
def sha(b):return hashlib.sha256(b).hexdigest()
def write(p,d): (R/p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
m=json.loads(show(OLD,str((H/'routing-manifest.json').relative_to(ROOT)))); fs={f['feature_id']:f for f in m['features']}; finalm=json.loads((H/'routing-manifest.json').read_text()); finalfs={f['feature_id']:f for f in finalm['features']}
manual={
'wp39-battle-context-and-participants.md':('缺失野生数量与既存零可战斗队伍分开；原队伍顺序可形成配置布局、创建/存活席位、旧优先队列和场景实际遍历不同集合；普通无战斗返回和末尾动画复位边界一并澄清。','框架提供持久创建输入，战斗侧消费临时布局/命令/优先队列，MZ显示实际遍历；仍需验证这些集合与先行失败前缀而非仅核对数值。'),
'wp40-commands-obedience-and-action-order.md':('Powder到门必失败而自损另受有效天气/间接伤害门；STALL优先括号与TRUANT行动拒绝、野生额外席位不自动补队列、KINGSSHIELD世代阶级与HYPERCUTTER免疫各自区分。','仍由战斗规则承载；框架与战斗方交接真实命令/缓存，需验证顺序、已消费PP和取消尾，不按名字等同规则。'),
'wp41-switching-positioning-and-escape.md':('开启替补后速度重算时，在send-out后、入场特性消费前更新旧队列速度；不重掷tie/bracket，也不添加缺失队列项。','已有换人/入场时序合同可承载；目标引擎须验证缓存刷新点和入场天气先后。'),
'wp42-growth-end-of-round-and-battle-outcomes.md':('普通非Shadow成长按WP19的正常模板HP255/攻击255（总量510）对照，在HP单项余量252−255=−3的首项反向区间失败，尚未到总量夹限及本接收者EV/经验写入或后续刷新；此前受领者与回调前缀不保证回滚，默认非内部设施仍在更早成长门返回。正常核心返回并完成外层善后及结束通知后，复位玩家行走动画状态与转向预锁记录；此处不写面向方向。','成长持久写入与战斗调用继续为协作候选；单项余量与总量余量按先后门分别验证，外层行走动画/转向预锁复位归世界交接，异常前缀和表现尾仍待验证。'),
'wp52-a-generic-numerical-and-status-evaluation.md':('纹理直接目标贡献查询发现候选不查PP，匹配计算类型伤害槽时仅作PP过滤且只加14一次；正常User/0目标路径不消费该贡献；能力评级20直接+5复制计数澄清。','框架拥有策略/评分，战斗侧提供实际状态/计算类型查询；应细化FR92职责和消费路径，不接入新的默认AI路径。'),
'wp58-battle-recording-and-playback.md':('局部随机Bag/Call/Fight属于直接DebugScene helper；正常设施/回放scene factory与controlPlayer=true AI路径分开。','仍是既有记录/回放与调试边界，不能提升为完全随机隔离，也不重开既有五元组/18字段合同。'),
'wp18-creature-identity-species-ownership.md':('物种/形态EggGroups接受15精确身份，省略基础默认和形态克隆分开；未登记身份严格拒绝。','框架内容身份与亲本消费者分工不变，FR397须增加物种/寄养/后代消费者。'),
'wp26-acquisition-gifts-and-script-trade.md':('记录战斗的收服存储为空操作；回放另按WP58 §6.2–6.4的副本、实时依赖及正常结束/中止分层合同，不能由记录战斗存储空操作推定回放隔离。','既有获得/存储与记录/回放交界分责保持；目标须分别验证记录战斗存储空操作、回放副本和实时依赖以及正常终局/中止，不把记录存储合同扩成回放整体隔离。'),
'wp30-growth-learning-and-friendship.md':('普通非Shadow战斗成长消费正常设施模板HP255/攻击255（总量510）时，先在HP单项余量252−255=−3的夹限失败，尚未到总量夹限和本接收者EV/经验写入或后续重算；先前前缀与默认非内部设施的更早成长门分别保留。','成长协作候选保持；分别验证单项/总量夹限的实际首失败位置、本接收者未写状态、此前受领者前缀及非内部设施早退，不扩张到Shadow/道具。'),
'wp36-wild-encounters-and-modifiers.md':('接受的负步骤概率前缀沿同一算法处理，累加器及整数商可为负；累加器除以200的整数商向下取整，不钳零。','既有框架遭遇触发候选保持；验证接受负概率、负累加器的向下取整及不钳零，不改变原有Repel比较成员规则。'),
'wp64-mail-and-mystery-gift.md':('命名ESC返回原非空名可成功；空文选择停止才nil，已发生的别名/获得地前缀不回滚。','框架礼物持久处理与MZ命名/确认交接仍足够，需保留前缀及公共获得包装的不同返回。'),
'wp11-map-topology-transfer.md':('并非仅目标图切换：邻图预取集合、玩家跨图会话、连接无效/重复的实际失败、运行时事件定位与存档/标题邻接消费者明确分开。','MZ地图/事件适配与框架地图数据、保存快照协作继续适用；新增5.2.1/5.2.2不另造伪功能。'),
'wp12-terrain-movement-vehicles.md':('普通移动/碰撞计时与独立跳跃计时分开；逻辑地图末端门不额外等待活动跳跃，消息/新请求/已有请求消费门和微更新各自分开。','FR330已有运动合同足够，但FR645/647须新增明确运动消费者引用及生产/消费职责。'),
'wp13-interpreter-command-matrix.md':('强制路线/等待的非字符指令、非法动态目标、并行解释器的生命周期/局部结束边界由新增3.4与矩阵指令行明确。','框架事件状态与MZ解释器时序边界已有消费者；不把返回或局部停止当整体事务清理。'),
'wp13-map-events-npc-followers.md':('邻图/路线目标会话、事件容器与并行解释器的刷新/结束边界补明；事件编号与映射所属图不可混为单一当前图查找。','既有事件/跟随与MZ生命周期适用，需验证直接地图缓存消费者和失败前缀。'),
'wp14-random-dungeons.md':('随机地牢连接/边界拒绝与地图缓存/出生位置等直接交界按有限入口修订；保留合法生成和空间邻格合同。','同一生成数据与MZ地图接入边界，源修订不表示未来生成算法实现或宿主行为已通过。'),
'wp15-resource-matching-and-audio.md':('普通位图包装捕获、空白创建后继失败与帧前缀独立加载分开；语言改选图像身份仍沿实际入口，不一律重试原身份。','资源解析/MZ媒体接入现有类别可承载；Slot图像消费者需增加具体依赖和异常前缀职责。'),
'wp03-content-identity-and-schema.md':('新增15蛋群固定作者身份精确表，定义顺序不等于界面排序/数值ID；基础/形态省略、严格枚举前缀及寄养/后代消费者分开。','FR397框架目录职责需精化并显式交给WP18/33/34消费者，不能把身份校验等同生育规则。'),
'wp04-pbs-lifecycle.md':('写回PBS时保留实际修改与刷新行为，删除无证据的Changes made提示承诺。','框架内容编译/写回责任不变，显示提示不再作为验收前提。'),
'wp08-localization.md':('Slot指定图像角色按当前语言SCRIPT_TEXTS先game再core；空译为命中，不按缺译回退。','现有框架语言身份服务与MZ图像加载分界适用；FR699/703需显式消费，媒体/像素并未执行。'),
'wp09-save-startup-continue.md':('主档先于备份删除，部分失败保留前缀且下次主档存在门可能跳过备份；空表适配、启动装配/语言、有效性与删除分流独立。','保存/迁移/标题交接类别不变；源非原子删除不自动成为目标政策，仍需明确兼容选择。'),
'wp10-migration-failure-recovery.md':('新增可读旧序列转空表后的正常返回、装配启动项/语言后再验证失败，以及相邻备份/删除递归的分流边界。','既有框架适配器/启动消费者和MZ标题职责可承载；成功适配不等于可继续存档。'),
'wp19-attributes-ability-and-stats.md':('正常设施模板HP/攻击各255、其余0，总量510符合总量上限而超过单项252；属性重算保留存储值，普通非Shadow成长先在HP单项负余量夹限失败，未到总量夹限及本接收者写入。','属性领域与战斗成长交接类别保持；区分总量510但单项255越252的模板、重算不归一化、单项/总量实际失败顺序及设施internalBattle更早门。'),
'wp23-shadow-data-and-vectors.md':('旧式SHADOW类别使用精确合法字段；资料附表不凭命名意图扩充有效接受域。','既有Shadow数据与规则消费边界足够，特殊玩法范围仍待用户决策。'),
'wp31-basic-evolution.md':('作者未知进化方法在严格枚举编译处拒绝；已存在运行时记录扫描失败与作者前门分开。','框架内容/进化职责保持，拒绝阶段与已有状态前缀不能合并。'),
'wp34-inheritance-and-offspring.md':('BR23与后代/蛋群目录的消费定位澄清，精确作者身份和亲本角色/集合交集保持区分。','框架遗传规则保持；增加FR397到本消费者的引用不改变生成规则所有权。'),
'wp60-berry-plants.md':('3/15/2,5参数由多数说法改为明确CHERI/CHESTO/PECHA/RAWST/ASPEAR五身份范围。','参数域更精确，不改变植物生命周期或MZ表现承载假设。'),
'wp61-field-passive-effects-and-blackout.md':('Repel遭遇允许门默认比较首个非蛋成员（含濒死），替代配置才取首位可战成员；野生等级低于所选成员等级时拒绝并清累积，计步与遭遇判定仍分别归现有消费者。','既有框架野外被动/计步和遭遇消费者分责保持；验证Repel默认首非蛋（含濒死）与替代首可战的配置差别，不以概率取整替代成员选择合同。'),
'combat-requirements-wp39-40-41-42-45.md':('新增野生零/原序/稀疏席位与EV超额异常对照，分别观测配置、实际遍历、优先集合及写入前缀。','作为现有功能验收目录映射，不为静态用例新造功能；数值一致不能证明时序集合覆盖。'),
'combat-requirements-wp49-51-52.md':('AE-T02保留ID并纠正普通User/0与直接纹理贡献区别，新增CV01–05限定PP/原始类型/计算类型和单次加分。','目录指向FR92及正常候选FR76，保持评分策略/真实命令分界。'),
'creature-rpg-wp35-36-57-64-68.md':('神秘礼物名称取消对照准确区分ESC非空与空文停止，链接公共获得前缀。','只修已有目录消费者，不新建礼物功能或排除特殊活动。'),
'engine-overworld-wp11-15-59-60.md':('新增PBS/邻图/路线/逻辑跳跃/并行解释器/边界六组对照；按源第三级章节消费者逐组绑定，原16节同WP号错误关联清理结果保留。','新增十标题是现有功能证据导航；最终JT绑定已修UI65两处和WP12，仍非已执行场景。'),
'generic-kernel-wp05-06-07-08-09-10.md':('新增删除主档/备份顺序与失败前缀，以及旧序列空表启动/语言/有效性分流静态目录。','目录映射到保存/迁移/语言/标题现有功能，不把用例当实现边界。'),
'pokemon-rules-wp19-21-22-23-34.md':('新增设施EV不归一化与普通战斗成长负上界失败的静态对照，保留正常/Shadow/道具边界。','目录映射属性/成长/战斗成长三主合同，仍需协作原型。'),
'wp65-title-load-options-pause-and-pc.md':('启动空表/保存No的副作用与持久写分开；最终L152/L210统一普通移动/碰撞计时定义，活动跳跃不额外阻止末端登记/消费。','FR645/647需精化逻辑运动门依赖；消息、解释器/强制路线新请求门与已有请求消费门不同，不能保证全UI跳跃暂停/取消/恢复。'),
'wp66-a-party-and-summary-ui.md':('Shadow INFO底部仍为普通经验条，心之计量显示和经验条不能凭属性名等同。','MZ摘要呈现与框架成长/Shadow状态交接保持；不新建/排除Shadow功能。'),
'wp67-a-battle-interaction-and-presentation.md':('场景配置布局与实际席位遍历、无有效玩家与野生零队列边界分开；倒下cry普通/专用音频及并行排期和胜利标记先于BGM前缀明确。','MZ呈现/音频和战斗领域faint/结果交接已有类别足够，时钟和已提交状态仍需具体兼容验证。'),
'wp69-slot-machine.md':('新增七图像角色语言选择、固定背景例外、实际高度影响时间分区，以及空译/加载/后续错误与随机/财务前缀。','FR699/703需精化语言/资源职责和依赖，不改变框架随机/财务与MZ图像时钟的既有类别。')}
changes=json.loads((P/'source-file-changes.json').read_text())['changed_formal_documents']; assert len(manual)==len(changes)==38
records=[]
for c in changes:
 path=c['path'];name=path.split('/')[-1];old=show(DELIVERY,path);new=show(FINAL,path);inter=show(INTER,path); patch=git('diff','--unified=3',DELIVERY,FINAL,'--',path); headers=[l for l in patch.decode().splitlines() if l.startswith('@@')]
 if name=='wp65-title-load-options-pause-and-pc.md': mode='R2_FULL_DIFF_PLUS_R3_FINAL_UI65_REPAIR_REREAD'; inherited={'prior_stage':'revisions/r2/accepted-source-reading.json#/complete_diff_reading','pre_final_commit':INTER,'final_delta_only_this_document':True,'final_repair_ref':PACKAGE+':review/remediation-eighth-20261016-prepare/accepted-cumulative/last-UI65-repair.patch'}
 elif name in ['wp04-pbs-lifecycle.md','wp60-berry-plants.md']:mode='R3_COMPLETE_BASELINE_TO_FINAL_DIFF_READ';inherited=None
 else:
  assert inter==new
  middle='49a558f7d5498680ba88d532f3815e07d7844459'; b49=show(middle,path)
  oc,nc=('908273093e1f6b27fc58249417675dd62d146224',middle) if b49==new else (middle,INTER)
  assert show(oc,path)==old and show(nc,path)==new
  priorpatch=git('diff','--unified=3',oc,nc,'--',path);assert priorpatch==patch
  mode='R2_COMPLETE_DIFF_REUSED_BY_EXACT_BYTES_PROOF';inherited={'prior_stage':'revisions/r2/accepted-source-reading.json#/complete_diff_reading','previous_read_old_commit':oc,'previous_read_new_commit':nc,'old_file_bytes_equal':True,'new_file_bytes_equal':True,'entire_per_file_patch_bytes_equal':True,'per_file_patch_sha256':sha(patch)}
 features=[i for i,f in fs.items() if f['source']['document']==path]; direct=[i for i in json.loads((R/'tools/accepted-backfill-result.json').read_text())['directly_changed_feature_units_vs_fixed_functional_source'] if fs[i]['source']['document']==path]
 records.append({'document':path,'baseline_identity':c['old_identity'],'final_identity':c['cumulative_accepted_identity'],'accepted_owner_batches':c['accepted_owner_batches'],'additional_to_original_required_write_set':c['additional_to_original_required_write_set'],'reading_mode':mode,'inherited_reading_proof':inherited,'complete_diff_identity':{'bytes':len(patch),'sha256':sha(patch),'hunk_headers':headers},'source_fact_reassessment':manual[name][0],'future_plan_reassessment':manual[name][1],'existing_document_feature_refs':features,'direct_source_changed_feature_refs':direct,'category_change_required':False,'new_function_id_required':False,'runtime_and_compatibility_evidence':False})
write('source-file-reassessment.json',{'schema_version':'routing-r3-source-file-reassessment.v1','role':'AUTHOR_SOURCE_RECEPTION_NOT_INDEPENDENT_REVIEW','fixed_package_commit':PACKAGE,'baseline_commit':DELIVERY,'accepted_final_commit':FINAL,'changed_documents':38,'unchanged_documents':93,'full_diff_reading_reused_by_exact_identity':35,'final_UI65_repair_reread':1,'U02_U03_complete_diffs_reread':2,'records':records})
# All direct source changes are quantified by parent source locator checker, then explained from the actually read section and per-document facts.
direct=json.loads((R/'tools/accepted-backfill-result.json').read_text())['directly_changed_feature_units_vs_fixed_functional_source']; bydoc={x['document']:x for x in records}; fr=[]
unit_narratives={'FR-000029': '普通非Shadow成长按WP19的正常模板HP255/攻击255（总量510）对照，在HP单项余量252−255=−3的首项反向区间失败，尚未到总量夹限及本接收者EV/经验写入或后续刷新；此前受领者与回调前缀不保证回滚，默认非内部设施仍在更早成长门返回。', 'FR-000032': '正常核心返回并完成外层善后及结束通知后，复位玩家行走动画状态与转向预锁记录；此处不写面向方向。'}
for i in direct:
 f=fs[i];cur=finalfs[i];d=bydoc[f['source']['document']]; oldparts=[show(B8,f['source']['document']).decode().splitlines(keepends=True)[a-1:b] for a,b in f['functional_scope']['line_ranges']];newparts=[show(FINAL,f['source']['document']).decode().splitlines(keepends=True)[a-1:b] for a,b in cur['current_applicability']['locator']['line_ranges']]
 fr.append({'feature_id':i,'name':f['name'],'immutable_source':f['source'],'baseline_functional_scope':f['functional_scope'],'current_source':{'commit':FINAL,'document':f['source']['document'],**cur['current_applicability']['locator']},'changed_unit_comparison':{'baseline_effective_sha256':sha(''.join(''.join(x) for x in oldparts).encode()),'current_effective_sha256':sha(''.join(''.join(x) for x in newparts).encode()),'compared_equal':oldparts==newparts},'source_fact_delta':unit_narratives.get(i,d['source_fact_reassessment']),'future_boundary_reassessment':d['future_plan_reassessment'],'category_retained':f['future_plan']['destination'],'destination_verified':False,'stage_approved':False,'responsibility_dependency_refinement_ref': 'source-plan-refinements.json#'+i if i in ['FR-000092','FR-000397','FR-000645','FR-000647','FR-000699','FR-000703'] else None,'underlying_file_reassessment':'source-file-reassessment.json#'+f['source']['document']})
write('feature-source-deltas.json',{'schema_version':'routing-r3-feature-source-deltas.v1','role':'AUTHOR_CURRENT_SOURCE_DELTA_NOT_COMPATIBILITY_PROOF','direct_source_changed_units_count':len(fr),'unit_detection_authority':'tools/accepted-backfill-result.json#/directly_changed_feature_units_vs_fixed_functional_source','records':fr,'document_wide_bound_units_are_not_all_direct_text_changes':True,'inserted_or_revised_test_catalogs_are_metadata_consumers':True})
# Specific author refinements. Historical source stays untouched; dependencies use existing B8 headings, current anchors remain separate.
def dependency(fid,reason):
 f=fs[fid];return {'document':f['source']['document'],'anchor':f['source']['anchor'],'reason':reason}
def evidence(fid):
 f=finalfs[fid];return {'commit':FINAL,'document':f['source']['document'],**f['current_applicability']['locator']}
rows=[]
def row(fid,basis,resps,refids,rationale,questions):
 f=fs[fid];rows.append({'feature_id':fid,'source_facts':basis,'immutable_source_preserved':f['source'],'current_source_evidence':evidence(fid),'existing_destination_retained':f['future_plan']['destination'],'reason_refinement_is_needed':'当前来源细化了既有边界；原通用职责/依赖未明确消费点，不能由类别未变推定已充分记录。','proposed_future_plan_rationale':rationale,'proposed_responsibilities':[{'party':p,'scope':s} for p,s in resps],'append_feature_refs':[x for x in refids if x not in f['dependencies']['feature_refs']],'append_direct_refs':[dependency(x,'已接受当前源明确消费的既有功能边界；引用是B8真实标题，新增当前子锚点另见current_source_evidence；不证明兼容。') for x in refids if not any(d['document']==fs[x]['source']['document'] and d['anchor']==fs[x]['source']['anchor'] for d in f['dependencies']['direct_refs'])],'append_questions':questions,'append_difference':basis+'；这是已接受源事实与未来验证问题的区分，未运行原型、未批准实现阶段、未证明目标兼容。','destination_verification_remains':'待验证','implementation_and_acceptance_remain':['未实现','未验收']})
row('FR-000092','final WP52-A §6明确直调纹理贡献查询的原始类型候选、PP受限的计算类型伤害匹配及只加14一次；普通User/0目标候选不消费该贡献，能力评级20+5计数不改变行为。',[('框架','拥有类型/能力偏好、原始类型候选和贡献评分；保留直调查询与普通User/0不消费的两条路径，不把候选总分固定100或新接默认消费。'),('Showdown','提供当前类型/招式PP与伤害分类、计算后类型等实际规则查询；PP过滤不是Disable/Taunt完整命令资格，兼容性须固定版本验证。')],['FR-000076'],'框架拥有类型进攻覆盖/能力评级策略，战斗侧提供实际状态查询；GR8-AI-001当前源已ACCEPTED，普通候选消费路径与直调贡献仍需目标验证。',['验证原始类型候选与计算后类型匹配、仅PP过滤和一次+14；确认普通User/0路径不新增消费，也不推定总分100。'])
row('FR-000397','final WP03 §6.2给出15个精确蛋群作者身份和省略/严格拒绝规则；物种字段、寄养兼容性和后代亲本角色是分别的消费者。',[('框架','维护15个精确蛋群目录及合法扩展、严格作者枚举接受域；基础默认/形态继承交WP18，Undiscovered先行门及Ditto/性别/集合交集交WP33，亲本角色/生成交WP34；目录顺序不强制为显示顺序。')],['FR-000137','FR-000214','FR-000508'],'框架拥有固定规则目录和作者数据身份；新增蛋群精确目录按物种、寄养、后代三个既有消费者交接，身份校验不替代领域规则。',['核对15身份与合法扩展接受域、Water1/2/3无空格、未知值登记前失败和已有清空/成功前缀；分别验证基础/形态省略与寄养/亲本消费者。'])
for fid,kind in [('FR-000645','暂停菜单'),('FR-000647','快捷菜单')]:
 row(fid,'final UI65 L152/L210与WP12 r8-terminal-motion统一：静止仅无普通移动/碰撞计时，活动跳跃不额外阻止末端登记或消费；消息提前返回、新请求门和已有请求消费门、微更新分别处理。',[('MZ',f'把地图常规更新中的{kind}请求生产、优先消费和菜单循环接入WP12逻辑运动门；消息窗提前返回，微更新不检测/分派，活动跳跃不额外阻止末端请求。'),('框架',f'提供{kind}领域资格/请求状态与直接消费者交接；区分解释器/强制移动阻止新输入和已有请求消费，保留未消费标记，菜单结果依原领域合同提交。')],['FR-000330'],f'{kind}由MZ接入与表现重建，框架维护资格/请求与领域提交；当前源补明WP12逻辑移动门，不将跳跃动画计时当普通移动门。',['逐项验证消息窗/解释器/强制移动/普通移动/活动跳跃，以及常规更新/微更新的新请求与已有请求消费；不外推为全UI跳跃取消、暂停或恢复。'])
row('FR-000699','final Slot §2.2限定七图像角色逐请求采用当前语言game优先core，缺译用原身份而空译为有效命中；转轮符号图实际高度继续参与§2.1时区，固定背景等不翻译。',[('框架','拥有初始/停止抽样与重玩样本消费，并在每个指定图像请求提供当前语言SCRIPT_TEXTS的game/core身份选择；空译与缺译分开，固定背景等不翻译。'),('MZ','按真实所选位图H/v/t处理时间区间、先停或顶部提交和更新先于输入；用实际语言后身份加载且核对布局/高度，不能假定替换图片等尺寸等行为。')],['FR-000440','FR-000352','FR-000354'],'框架维护随机和语言身份选择，MZ维护实际图像/时间/输入更新；所选转轮图高度直接影响既有停止时序，需联合验证。',['在同高度同布局条件下分别验证game/core/缺译/空译的请求身份；另验证非等尺寸替换图、实际加载高度与停止时区，静态向量不等于媒体/像素执行。'])
row('FR-000703','final Slot §6.1区别提示空译清旧图、转轮空名求值早失败、普通缓存加载的有限捕获与帧前缀独立加载；对象/随机/奖额/音效和财务尾的已完成前缀不回滚。',[('MZ','承担图像请求、加载和后继操作的分入口失败：提示空译清旧图、转轮空名更早失败，普通捕获后空白创建仍可失败，帧前缀无同一保证，不重试原身份或保证整体清理。'),('框架','维护当前语言身份输入、已消费随机和场景账/奖额/玩家币额/统计的提交边界；图像失败保留已完成对象/随机/奖额/音效前缀，未到财务尾不提前写玩家余额或统计。')],['FR-000440','FR-000354','FR-000699','FR-000702'],'既有MZ图像/场景和框架语言/随机/财务合同需按实际错误位置协作；源中没有本地整体回滚/清理保证，未来政策仍待验证。',['分别验证提示空译、转轮空名、普通加载捕获、空白创建失败、帧前缀错误及中奖图失败时的随机/奖额/音效/币额/统计前缀；不将fallback存在当整体成功。'])
write('source-plan-refinements.json',{'schema_version':'routing-r3-author-source-plan-refinements.v1','role':'AUTHOR_PROPOSAL_FOR_PARENT_SINGLE_CORE_WRITER','status':'PROPOSED_PENDING_PARENT_APPLICATION_AND_INDEPENDENT_REVIEW','no_destination_category_change':True,'no_new_or_retired_id':True,'no_immutable_source_change':True,'records':rows})
print('wrote',len(records),'files,',len(fr),'direct units,',len(rows),'specific refinements')
