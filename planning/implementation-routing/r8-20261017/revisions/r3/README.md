# R3 累计校准与精准作者返修

本候选已经应用9批ACCEPTED最终来源 `5f87743293290de2e219ecdd6c19e88280f60c9a`，已收到c0f62d9的固定独立报告34202eb：分类/职责/范围/依赖及原七项修正PASS，当前来源摘要两根七行FAIL；后继[七行作者修复](../r3-calibration-repair/README.md)仍等待真正非作者 ultra/default 有界复核。来源包为 `8336249c78b4698cd77445653d3b05ff6a76ce94:review/remediation-eighth-20261016-prepare/accepted-cumulative/calibration-input.json`；U04最后接受回执为 `a974eb133bdb280ac46f2684df4b309a18fc6cc1`。工作区正式正文保留B8，current从独立Git对象读取。

131文档、历史2683标题/当前2704（新增21）、736活跃/33完整退役/33元数据；38文件变更、40目标贡献（含共享历史贡献）、9接受事件；230整改绑定全部回填，pending/partial均0，较旧191新增39行或新增/扩展47行。39项源接受为29 required+10 optional，CLOSED仍0。[最终校准证据](tools/final-calibration-proof.json)逐15项核对这些口径。

## 7 项作者修正

固定 R2 FAIL 为 `0ef0b7ad5f9465cfe31da0d7a35f56b5ccba5add`，受审旧候选为 `a32873d2860b15d9f5e27727db8f131f4ec433b6`。本轮收到94份输出，[消费台账](review-input-consumption.json)区分语义完整读、JSON/AST解析与机器字节核对。

| 问题 | 作者处置 |
| --- | --- |
| COMBAT-R2-DEP-001 | 61/66/69移除739的PP错边，保留真实740；68/71的PP对照保留。 |
| R2-CRE-DEP-001 | 186/190退款定位正常终局31，192白雾建立/期限定位39，清除错误外层治疗/侧交换用途。 |
| R2-CRE-DEP-002 | 244清六类PBS编辑器263/265错边；741战斗金钱统计改420，训练家共享工具742保留。 |
| POK-WORLD-R2-DEP-001 | 20行逐实际scope清同号/异体系错链，补真实地图/天气/存储/成长/暂停/过滤道具消费者；664额外159–161及751/760额外355同根修正具名留证。 |
| SOURCE-R2-001 | 当前改变内容须匹配真实接受目标身份；陈旧路径回执不能授权后继未接受字节。 |
| SOURCE-R2-002 | 完整prospective覆盖在写核心/归档前验schema；null归一化与初次旧代码应用失败分开留证。 |
| SOURCE-R2-003 | 治理豁免限固定三文档/46标题；普通行为章不能用ALL_FORMAL_FEATURES清空消费者。 |

固定c0f62d9独立R3报告已判上表七项修正PASS；本表保留作者处置依据，不替代本轮七行来源摘要校准的后继独立判断，也不宣布全轮CLOSED。详见[7项映射](finding-resolution.json)、[28行逐边理由](dependency-repairs.json)、[工具处置](tool-finding-resolution.json)、[736行处置](feature-resolution.json)、[44组传播](retained-pass-propagation.json)、[facet继承矩阵](facet-inheritance.json)。旧708 PASS仅对未改变且未受源/目标变化影响的facet保留信用，整行字节相等不证明依赖有真实用途。

## 来源和精确变更

[38文件来源重估](source-file-reassessment.json)、[51直接变源单元](feature-source-deltas.json)、[21新标题消费者](new-heading-mappings.json)、[39项接受接收](issue-source-reception.json)、[作者阅读范围](source-reading-scope.json)保存固定来源。原10个pending U04建议按最终5f实读并重估，尤其UI65 L152/L210实际与WP12运动门同步，不是改标签。

[6行职责/依赖精化](source-plan-refinements.json)已应用：645/647末端运动门、92纹理查询、397蛋群目录、699/703语言图像与失败前缀。去向类别不变、无新增或退役ID。[统一补丁](source-refinement-patch.json)在接受后归档 `tools/post-source-pre-semantic-35175c7094b0.json.gz` 上以before/after描述78行/162字段；原始[应用回执](author-refinement-application.json)与[来源摘要纠正回执](source-narrative-correction.json)分开保存，最终补丁可以重建完整最终manifest。

最终manifest SHA256为 `c6b2d3ea0346c82f4aa224b67a176c21901b50efc337df25af7aa26e0242e3ea`，补丁为 `6351505a314c88b1bed3aab98c6808639b319461e25f796ded87221225e0418b`。语义补丁保全source/current/upstream、类别/伙伴、阶段/实现与验收；58份R1/R2历史文件原字节保全，历史覆盖仍为2683。

[相对 R2 的精确文件差分](changes-from-r2.json)列出每个变化文件的前后字节数、SHA256、Git blob 与行数；身份总表另绑定整个固定候选。

## 实际检查与交接

[最终10命令I/O](tools/actual-command-io.json)为 `cumulative-source`：全部exit0，17登记输入哈希稳定。27结构负例、9自检、2导航负例、11生成物、19保全检查、5接受绑定负例、2704覆盖及4负例、4来源门隔离夹具（覆盖3项工具问题）均通过。显式导航36父/39子/39边。这些仅为作者静态工具证据，新的语义累计复审仍必要。

初次累计应用确实用旧代码并暴露1776 null，相关旧代码/失败I/O/归一化证据完整保留，[工具记录](tool-finding-resolution.json)不倒填当时已有prospective门。阅读为完整差异与定向有效源章，不冒称131篇本轮新全文；机器解析不等同语义阅读。

全部736行仍待验证、待定/未批准、未实现、未验收，四原型未运行；框架307/Showdown74/协作130/MZ225/排除0。没有Ruby/参考游戏/业务/宿主/未来框架执行，未自行独立验收。下一步由父任务固定新候选SHA并使用[七行有界复核prompt](../r3-calibration-repair/review-prompt.md)另建ultra/default任务；配置有效echo缺失仍UNVERIFIED。来源9批接受不替代目标兼容、用户范围/阶段决定或全轮CLOSED。

21条新标题来源证据的标题hash保留`SHA256_UTF8_TITLE_ONLY`口径；current定位使用的原Markdown标题行hash单列保存。原映射字节与初sourceapply I/O匹配并已归档，初次口径探针与修正见[记录](tools/new-heading-hash-convention.json)；这是证据口径显式化，不改标题/消费者或核心17输入。
