"""Write the current report/progress after successful artifact validation."""
import datetime
import review_state as s

assert s.read('artifact-validation.json')['result']=='PASS'
report='''# M01 第五轮全局独立审查

`schema_version: gr5.review.v1`

**complete：已完成所分配、可取得材料的 M01 全量静态语义审查。** 这表示源与现行合同的比较完成，不表示所有合同充分、所有组合兼容或运行通过。`partial` 表示具名合同覆盖不足；共享交界中的 `unresolved` 保留未裁定问题，不以审阅完成消除它们。

固定规格 B5：`9366d9d17aaeac3b4414236468affa650fb3dd27`，正式子树 `d5a462b4c6f8b78c3264a25d6b5495230fa265e2`。固定参考 R：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。逐路径 blob、SHA-256、实际阅读范围和比较结果见 [reading-coverage.json](reading-coverage.json)。请求参数登记为 gpt-6-astra / ultra / service_tier=default / 禁 Fast；实际参数回显 **UNVERIFIED**，未调查额度、认证、会话或后端。

完成范围：

- 45 份主责源文件：两个设置文件、Intl、010_Data 全部文件、Compiler 001/002/003。声明、注册、分支、默认、失败与必要调用分别比较，不以全文读取或命中数量代替语义结论。
- 73 份 PBS 的全部实际记录和字段，包括各世代、可选 Shadow、设施与工具消费者；247 条按 schema 族登记的字段约束。这些是字段/证据分区，不是独立功能计数。36 份世代备份逐记录比较，精确相同 blob 的复用保留每条路径语境。
- 18 份翻译文件的全部 10,697 条记录，以及安全基础类型解析的 `messages_core.dat` 全部 963,270 字节。逐键域归属、生产者/消费者、占位参数、转义和键值差异均有记录。安全解析器不执行对象钩子；二进制与文本一致性只是证据的一层。
- 124 项声明（118 个设置常量、3 个方法型内容配置、3 条引擎元信息）及 140 组具名消费者：117 组有界 `supported_static`，23 组保留具体 `partial`。注释和停用块不算活跃消费者。
- wp02/wp03/wp04/wp08 当前正文、有效原稿/库存附录与 93 条主责静态向量均有反向映射。责任目录只认证归属，不冒充具体规则。另追踪必要跨域来源；这些文件仍按实际范围标 `partial`，不认证整个消费领域。

全量数据比较保留了有意义的差异：旧世代存在而当前不存在的 STICK/VICEGRIP、设施池重复位置、同一 SLOWBRO 形态键跨数据集改变含义、可回退基础记录的 DefaultForm、翻译旧标签和非直接字面调用键。设施的宽容未知引用已有当前合同覆盖，不重复立必修。成长率全部 606 个字面表格单元及表外公式已读；没有执行 600 项重算，也没有借用历史算术 PASS。

候选结果如下。**全部保持 `candidate_pending_independent_counterevidence`，最终 required 为 0。** 每项完整前提、源/规格锚点、正常/边界对照、反证范围、影响与验收条件见 [findings.json](findings.json)。

| ID | 级别／处置 | 具名差异 |
| --- | --- | --- |
| GR5-M01-001 | P2／unresolved | 活跃浮点文本识别接受单独小数点，却拒绝负号、加号和指数形式；一般“浮点”类别不足以确定这一边界。 |
| GR5-M01-002 | P2／unresolved | 默认消息生成的 core 排除、set/add 差异和导出键集合，不能由运行时语言回退规则推出。 |
| GR5-M01-003 | P2／unresolved | 翻译键逐行端部处理与其后连续空白归一的顺序，影响内部换行键身份；实际 Controls 记录有对应证据。 |
| GR5-M01-004 | P2／unresolved | 通用 PBS 六列顺序未明确与能力登记/公式列序分开。WP22 已明确其自身表序，作为反证保留，待独立裁定是否已足够构成引用覆盖。 |
| GR5-M01-005 | P2／unresolved | 容量查询对所有负盒号取队伍上限；只有 −1 在成员寻址时代表队伍。现行 −1 特例不能替代所有负号的容量规则。 |
| GR5-M01-006 | P2／unresolved | NPC 成员缺省特性槽、性别、异色及 Nature 登记位置规则，未由“按数据覆盖”完整确定；实际 Unknown 类型训练家提供正常数据反例。 |
| GR5-M01-007 | P3／optional | 库存附录生成器及旧生成输出仍写“调试菜单切换语言”；当前正式正文和有效附录已正确，限辅助材料漂移，不重开正确主合同。 |

[source-to-spec.json](source-to-spec.json) 保留其余细粒度覆盖限制，包括部分解析/反写归一、直接世代阈值、图鉴区域配置和构造缺省边界。[shared-interfaces.json](shared-interfaces.json) 将同一能力按消费者投影登记；其中招式未知效果回退、地图名共享文本原地替换、空地牢配置等观察保留源事实与裁定边界，不静默升级为最终必修或未来兼容政策。

主要证据入口：

- [spec-to-source.json](spec-to-source.json)：主责条款、表、124 项声明和 93 向量的反向来源。
- [schema-field-contracts.json](schema-field-contracts.json)、[pbs-data-inspection.json](pbs-data-inspection.json)：逐字段规则、默认、实际记录证据及世代比较索引。
- [configuration-branch-reviews.json](configuration-branch-reviews.json)、[flag-consumer-contracts.json](flag-consumer-contracts.json)：配置分支及全部实际标记值的消费语义。
- [corpus-semantic-review.json](corpus-semantic-review.json)：18 份语料的逐记录语义投影与生产者不确定性。
- [artifact-validation.json](artifact-validation.json)：产物 JSON、锚点、哈希、引用和范围一致性检查 **PASS**；这不是行为测试。

本轮未运行参考/Ruby/游戏、独立行为模型或场景向量；只使用静态阅读与获准的数据解析、字面值/身份关系核对。未认证宿主、媒体、真实事件可达性、插件动态扩展、完整编译往返或任意世代组合。没有修改正式规格、参考、历史输入或共享报告，没有提交、推送、update、安装工具或启动子会话。共享 Feature Matrix 未写入；本任务目录保留 [本地分类投影](feature-matrix-projection.json)。GR3-M09-001 暂缓与 GR3-M02-003 NO_REQUIRED 保持，不重新开启。

父会话下一步可直接据七条候选与共享交界进行独立反证和归属裁定。本轮没有待补的主责可得阅读范围。
'''
(s.OUT/'report.md').write_text(report)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
summary=s.read('review-summary.json')
summary.update(complete=True,phase='assigned M01 static semantic review complete',completed_at=now)
s.write('review-summary.json',summary)
progress=s.read('progress.json');cov=s.read('reading-coverage.json')
completed=[]
for e in cov['sources']:
    if e.get('review_extent')=='full':
        completed.append(dict(path=e['path'],read_ranges=e.get('read_ranges',[]),read_byte_ranges=e.get('read_byte_ranges',[]),
                              review_extent='full',scope=e.get('review_completion_scope')))
assert len(completed)==137
progress.update(status='complete',complete=True,phase='M01 assigned available static semantic review complete',review_extent='full',
 completed_semantic_ranges=completed,next_actual_range=None,not_reviewed=[],remaining_work=[],
 latest_semantic_summary='45 primary source files,73 PBS,18 text corpora and safe binary inspection complete for assigned M01 scope;124 declarations,140 consumer groups,247 field contracts and93 primary vectors mapped. Seven provisional candidates; no final required sign-off.',
 checkpoint_at=now,model_parameters_actual='UNVERIFIED',candidate_findings=7,required_findings_finalized=0,
 source_local_full_read_files=45,source_entries_total=287,
 primary_record_data_inspection='Complete inert record/key/field inspection plus independent source/consumer comparison; not a count-only semantic assertion.',
 completion_boundary='Complete review is not a claim of complete specification sufficiency, arbitrary compatibility or runtime success. Foreign-domain files remain partial at actual ranges.',
 pending_independent_adjudication=[f['id'] for f in s.read('findings.json')['findings']],
 unexecuted=['reference/game/host execution','behavior models and scenario vectors','full compile/import/export round trips','600-positive-level GrowthRate recomputation'],
 shared_observations='See shared-interfaces.json; unresolved cross-owner scope/policy is not silently marked supported.',
 validation='artifact-validation.json: PASS (artifact consistency only)')
s.write('progress.json',progress)
old=s.OUT/'progress.md'
if old.exists() and not (s.OUT/'progress-history.md').exists():
    (s.OUT/'progress-history.md').write_text(old.read_text())
old.write_text('# M01 当前进度\n\nschema_version: gr5.review.v1\n\n**complete=true；所分配可得材料的全量静态语义审查完成。**\n\n45份主责源、73份PBS、18份语料及安全二进制解析完成；124项声明、140组消费者、247条字段约束及93条主责向量均有映射。消费者117组supported_static、23组partial，后者是已比较后的合同限制，不是漏读。\n\n7条候选：6条P2 unresolved、1条P3 optional，全部candidate_pending_independent_counterevidence；最终required=0。参数实际回显UNVERIFIED。未执行参考、游戏、行为模型或场景向量。\n\n产物一致性检查PASS。主责待读范围为空；跨域文件只认证记录的M01投影。父会话可进入候选反证/归属裁定；详见[report.md](report.md)、[findings.json](findings.json)和[shared-interfaces.json](shared-interfaces.json)。\n\n完成时间：'+now+'\n')
print('Final report/progress written; assigned M01 static review complete')
