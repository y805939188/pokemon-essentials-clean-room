# PRE0 + B01 作者候选交接

状态：**AUTHOR_CANDIDATE_PENDING_INDEPENDENT_ULTRA**。仅执行PRE0与B01-A；父任务指派新的独立Ultra，未派生任务、未自行审查/批准、未整合作者改动、未启动下游、未关闭finding。

- REVIEW_BASE：e1e01bb18d824931e54f182dd61af5a9f908ba85
- REVIEW_REPORT：93e10babe0b9c9ef8b3f5277754541b447beeeb4
- FIX_BASE／方案：41fffb540c6483f5296ea0d33b789b75180d27ed
- PRE0／候选父提交：8f3a811855fc43b5fe5eb7809931b4e1749200de
- RUN_ID：20261003-prepare
- 候选分支：remediation/20261003-prepare/batch-B01
- 独立integration分支：remediation/20261003-prepare/integration；停留PRE0，不消费未审作者候选。

作者范围5个WP，14贡献／7主责；正式差异仅6个允许文件。源finding完整对象及当前有效限定都继承93e10报告，优先级与规范ID不改变。14个响应不等于14个已解决finding；尤其WP01仅提案、跨域ID尚有其他批贡献。

材料：

- [author-response.md](author-response.md)、[finding-responses.json](finding-responses.json)：逐ID变更、前提、唯一静态结果、反向对照、来源与剩余范围。
- [original-findings.json](original-findings.json)、[reading-leaf-references.json](reading-leaf-references.json)、[reading-leaf-values.jsonl](reading-leaf-values.jsonl)：原14对象的全部字段、无损阅读引用及573个原值。
- [source-reading-log.tsv](source-reading-log.tsv)：固定源的实际编号文本阅读范围；只作导航，不表示分支覆盖。
- [static-vectors.json](static-vectors.json)：31条相关静态测试行、A001真实字符序列及文档检查对照，未执行行为程序。
- [registry-proposals.json](registry-proposals.json)、[historical-errata.md](historical-errata.md)、[scope-conflicts.md](scope-conflicts.md)：公共登记建议、历史后继更正、最小范围冲突。
- [candidate-manifest.json](candidate-manifest.json)、[formal-diff.patch](formal-diff.patch)、[validation-results.json](validation-results.json)：父身份、6文件内容哈希、正式完整差异及结构检查。
- [candidate-ledger.tsv](candidate-ledger.tsv)：14项仅登记为待独立复审，规范状态OPEN；PRE0的229项全局开放台账不改为通过。

当前明确请求gpt-6.1-sol / Max / Standard(default)；没有Max不支持证据，未降为xhigh，未改任何配置。实际生效模型/推理/速度仍UNVERIFIED，继承用户已批准的方案A披露；不以作者自述作为平台证据，不读认证、令牌或/root/.codex/sessions。未来独立复审必须请求Ultra/Standard并单独留回执。

所有行为结果仍是静态推导。只运行自有文本/JSON/Git结构检查工具，未运行参考、游戏、编译、转换、生成、反序列化、模拟器或求解器；未写入参考/PBS/.dat/地图/存档。U01–U10、G01–G12、AX01–AX20及素材/宿主/插件未知保持，运行观察及真实Demo链均0。

复审应针对本分支最终冻结SHA与PRE0父提交的实际完整差异，同时核对只读原规格与跨批剩余条款；候选SHA由提交与推送后的独立publication-receipt记录，避免在提交内自引用尚未生成的哈希。若涉及范围扩展，由父任务依scope-conflicts裁定；本作者没有提前消费其批准。
