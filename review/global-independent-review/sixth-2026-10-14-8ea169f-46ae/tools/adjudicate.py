"""Explicit root decisions; no automatic inference of source behavior."""
import collections,datetime,json,pathlib
root=pathlib.Path(__file__).resolve().parents[1]
rows=json.loads((root/'findings/proposals-complete.json').read_text())
rows.append({'id':'R6-C-P02','origin':'findings/additional-C-P02.json','reader':'R6-C',
             'original_record':json.loads((root/'findings/additional-C-P02.json').read_text())})
optional={
'R6-C-P02':'首次满槽源侧发RGBA(64,200,248,192)，不是白色请求；原“闪白”可为实际视觉简称，缺原生资源/宿主不能裁最终像素。可选参数/观察层澄清，不列必修。',
'R6-CM-FB-01':'有界作者数据可命中不可构造的既有绑定；现有回退语句及R5向量限定名称缺席，均保持正确。保留源边界为可选兼容澄清，不要求未来以源命名空间查询实现。',
'R6-UI-PARTY-003':'只证明Shadow仍发经验条绘制请求，不能证明最终可见像素；正文经验信息替换存在文字/区域解释空间。可选请求层精度补充，保留实际画面未知。',
'UI-ST-002':'本条上下文可限定单纯导航期间的暂持预览。成功交换后重启/换预览的事实保留，但不能截掉上下文裁为无条件冻结错误。',
'GR6-F-003':'18个保存键及现有不完整状态合同已经蕴含地形/默认场地未记录；本轮完整记录该有限丢失及恢复对照，可选具名兼容向量，不新计重复必修。',
'GR6-F-010':'当前/Gen5两个默认模板的身份损失已由正确通用解析合同及本轮逐数据事实覆盖；可选具名语料回归，不是新错误条款。',
'R6-D-FONT-C01':'没有证实原文承诺遍历八字体或跨档自动替代；实际候选/空名边界保留为可选精度补充，文件存在不证明宿主发现。',
'R6-D-PBS-C08':'编辑器None标签与数值0资源请求层需区分；缺Graphics，仅人工0资源前提。原资源选择条款正确，可选观察层限定，不宣称真实阴影。'}
no_required={'R6-UI-PARTY-004':'精确原方法的2人数/SpeciesClause/三成员隔离反证没有Summary调用，BACK正常nil。Ruby循环块局部command并不保留旧Entry0。原提出/支持反证和相反实证全部保留；未证明原生全版本，但不能把已反证假设列必修。'}
p3={'GR6-O-001','GR6-O-002','GR6-K-001','R6-B-001','R6-CA-EA-P001','R6-DX-E002','R6-DX-AN-005','R6-DX-AN-007','R6-DX-DEBUG-004','R6-DX-DEBUG-005','R6-DX-COMP-003','GR6-UI-BAG-001','GR6-UI-BAG-002','GR6-F-001','R6-D-LZ-002','R6-D-PBS-C05','R6-D-DATA-C01'}
specific={
'R6-B-001':'到达局部救援的缺图块集对象/属性异常仅两个ID；坐标/层属无效tile另支。正常表返回nil不一概保证相同描述。',
'R6-B-002':'＋可为动作集合，不裁字面反序；必需补生成提示先于接收入口及收费已扣前缀。接收内步骤引用正确WP27，不重写WP29一般商店。',
'R6-DX-E002':'正文7.5/B19-C016正确保留；只把独立WE-M20的省略主语限定非零形态，避免单行测试误省基础记录。',
'R6-DX-AN-005':'只补类型正确、结构损坏的接受/替换/后续失败前缀；不指控原文已承诺所有坏结构回滚，不推广正常UI产物。',
'R6-DX-AN-007':'必修仅默认控制点的0.3333/0.6666近似请求及宿主量化未知；浮点递推的逐位端点兼容另列optional facet，保持N5精确示例。',
'GR6-F-001':'取消仅重置内层，残留身份使随后结束回收记录；既有W30空原队伍写入正确，主修重置范围与组合向量，不重复W30。',
'GR6-F-004':'完成目标处理状态不等同实际命中成功，Protect和无目标反射生产者与存活结算门须接合；直接状态评分表/最后行动限定保持。C AF001并入本根因。',
'GR6-F-009':'专门Save隐藏正确；普通Quit Game的共享保存可接收仍活动的模式对象。只证明正常依赖下序列化可达，不证明真实写盘/重载时钟或数据损失。',
'R6-D-PBS-C05':'新建Item Unnamed/???既有合同正确不重复；主补独立NamePlural默认及Type/Move有限省略原始值与语言输出分层。',
'R6-D-DATA-C01':'只限定特性Flags显式空的首元素/后续字符串查询，省略空列表仍正确；不扩大为所有列表失败或全部孵化崩溃。',
'R6-UI-001':'实际party删除先于暂停；以原方法/默认Peer独立探针及Storage反证为准，保护后续记忆移位/N加入未知前缀。',
'R6-DX-COMP-002':'同会话三缓存与区域导出回写分别观察；新Game_Temp正例不清类级连接缓存，不授统一广播或全缓存刷新。',
'R6-CA-EA-P001':'四危害失败locator5.1→5.2为精确导航修订；行为/评分正文正确，不计AI运行缺陷。'}
decisions=[]
for row in rows:
    id=row['id'];kind='optional' if id in optional else 'no_required_revision' if id in no_required else 'required'
    sev=None if kind=='no_required_revision' else 'P3' if kind=='optional' or id in p3 else 'P2'
    prior=root/'findings'/('independent-'+id.removeprefix('GR6-')+'.json')
    prior_reason=json.loads(prior.read_text()).get('reason_and_minimum_scope','') if prior.exists() else ''
    reason=optional.get(id,no_required.get(id,specific.get(id,prior_reason)))
    if not reason:reason='接受当前原提案的行为差异/具名遗漏及非提出者回源反证；修订范围限定原记录的有效前提、最小规则、正确scope与静态验收，不授运行或永久缺陷兼容。'
    decisions.append({**row,'classification':kind,'severity':sev,'root_decision_reason':reason,'root_arbitrator':'R6-I /root','state':'OPEN_NOT_UPDATED' if kind=='required' else 'OPTIONAL_NOT_STARTED' if kind=='optional' else 'NO_REQUIRED_REVISION','update_started':False,'decided_at':datetime.datetime.now(datetime.timezone.utc).isoformat()})
facet={'id':'R6-DX-AN-007::FLOAT_RECURRENCE','parent_id':'R6-DX-AN-007','classification':'optional','severity':'P3','reason':'一般N逐次浮点加步的端点位级误差作为兼容精度观察；默认点数值必修独立，未证明实际像素/不要求旧浮点实现。'}
(root/'findings/adjudicated-records.json').write_text(json.dumps(decisions,ensure_ascii=False,indent=2)+'\n')
(root/'findings/optional-facets.json').write_text(json.dumps([facet],ensure_ascii=False,indent=2)+'\n')
counts={'registered_records':len(rows),'full_original_proposals':len(rows)-1,'additional_bounded_precision_potential':1,'classification':dict(collections.Counter(x['classification'] for x in decisions)),'required_severity':dict(collections.Counter(x['severity'] for x in decisions if x['classification']=='required')),'optional_facets_separate':1,'runtime_approval':False,'update_started':False}
(root/'findings/adjudication-counts.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n');print(json.dumps(counts,ensure_ascii=False))
