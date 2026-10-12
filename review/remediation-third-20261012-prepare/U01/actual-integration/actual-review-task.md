# U01 实际整合独立复审（复用同reviewer）

请父任务复用产生 `f8f48c1ccd7d596dd55b4fd1f496597cce7cea6e`（U01 attempt-02）的同一独立reviewer，保持独立于作者 `d0eb4da6374f9f85e811ab3ccef39c7070039dd0` 和唯一整合登记员。gpt-6.1-sol／ultra／default，请求接纳有效、回显缺失UNVERIFIED，不查额度、不使用隐藏或CLI模型。本包不启动角色。

真正受审actual：`31cb88c323d690eebb5b1bfca8270d38bb90a933` / tree `e7240d6483a41eceb040d12f34e86a1d3e8a1678`。本次增量base：`35e21c42d51547f66c0e912e4ea270e0023c3b3b` / tree `f68bac5e2bba8572c95d0174491e1f51710e81a3`（U06已冻结包）。整改branch `codex/third-remediation-20261012`。从父任务交付的精确包commit读取本目录 actual-review-input.json 和单份权威 actual.patch；全部15个payload变化已从base临时重建逐字匹配。包后继仅复审资料，不另改payload。读取根AGENTS和适用环境指令，参考 R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0` 只读。

无论复审工作树保留旧attempt02分支或从本包建分支，所有受审正式/公共/状态字节必须按固定P git对象读取，禁止用旧工作树D、旧作者候选或浮动HEAD替代。七正式文件逐字等于作者d0冻结候选，包含新版KR15/KL36同有效type/name/version和无更早失败前提；六候选PASS只作有限证据，不自动转为actual PASS。逐ID验证真实正式路径上下文/引用与六项完整验收、19条标准及具名前提；已相同的源/前提/候选字节可按精确对象有限复用，改字节/前提才定点重验，不重做全229/341或全局review。

新公共字节也在本次独立范围：audit/source-traceability.md及planning/feature-matrix.md仅追加U01六项事实、来源、待实际复审状态，核与正式正文/静态设计/source-successor一致，不复制参考代码、不扩大历史scope/默认17登记或运行结论。核所有新增接受/关闭仍false、NOT_EXECUTED保持；M02通知源有效定位与原交接导航差异保持透明。

必要U06公共定点核验必须显式记录：读取P中u06-public-delta.json及input内两新公共blob/SHA/bytes，证明旧U06整个文件文本是精确前缀、其中标记图/底图/未知行及F18-04/F18-05状态段未变；检查新U01追加没有弱化U06限界、混淆来源或代签接受。U06的3正式及14管理/任务包文件继续原字节，旧actual `266539d5db6d84116a355f503df8830d309c7937` 的review输入仍绑定旧payload。即使已有/将有U06旧actual PASS，也不能把它签给这两个新whole-file hash；本次新的独立报告要给这两个当前P公共文件必要定点核验结果，父任务可同时提供给U06 reviewer消费。范围仅这些共同文件和必要消费者，不增新全局审核门。

WP09记录只观测P新字节（blob `d9a256cbc1054cc3ad190f83231bfdfa564ac4a2`），不是批准交接：wp09-pending-handover.json中的approved_handover/U02_start_allowed必须false。本次actual通过后，唯一登记员才可正式接受并冻结批准prior/new身份，再由父任务派U02；reviewer不得自行放行或登记。U03候选、U08、M02-003和旧attempt01均不纳入改写，全部未知/宿主/真实资料限制保留。

只写 `review/remediation-third-20261012-prepare/U01/actual-integration/independent-review/attempt-01/` 六文件：input-snapshot.json、report.md、findings.json、per-id-verdicts.json、output-identities.json、model-request-receipt.json。输入snapshot绑定P/tree、base、d0、RV、每个实际读文件的blob/SHA/bytes及角色分离；报告逐ID输出actual PASS/NEEDS_REVISION/BLOCKED，并单列U06公共新字节定点结果与WP09门禁。禁止修改受审文件/作者/公共/登记台账，禁止接受或CLOSED。正常提交推送自己的独立分支并读回，给精确报告commit/tree/path；不force、不清理未知资料。每有实质进展汇报；技术取消先查任务/commit去重，用户停止或权限拒绝遵守。

当前8/23必修字节已实际整合（U01六项、U06两项），2/6主题payload冻结，正式接受0/23、关闭0/23，U07未完成。复审次数不计完成率。有限标准全部有处置后结束，不递归证明所有旧raw/ACT。未来历史bug兼容、资源补交与真实运行不阻塞准确静态事实，也不默认未来复刻缺陷。
