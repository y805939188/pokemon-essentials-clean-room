# U06 实际整合独立复审任务

请父任务复用形成候选独立报告 `471c63bb7585c44d08571e7d09631694eea57632` 的同一独立reviewer；该角色继续独立于作者 `c9d6e3c81c88c778abf2f822977275d0e632581e` 与唯一整合登记员。gpt-6.1-sol／ultra／default，显式请求接纳有效，回显不足UNVERIFIED，不审额度、不启动模型CLI。此任务包不创建review角色。

真正受审actual：`266539d5db6d84116a355f503df8830d309c7937` / tree `d4efb94a34fd5fc5d3c3eb66bf861782c23cbbcc`，整改branch `codex/third-remediation-20261012`。整合base：`d0371f693f4a0dc713ee5cc6e43a20ff465269a8`。精确review输入为本目录 `actual-review-input.json`，单份权威完整差异为 `actual.patch`（全部9个payload变化路径；已从base在临时副本重建9/9匹配）。包自身所在最终commit由父任务从整合回执绑定，不能用浮动HEAD替P。此包后继提交只承载复审输入，不另改正式/公共字节。

只复审 GR3-M12-001、GR3-M12-002 的真正整合字节、公共承接和必要有限交界。P中 WP75、WP76、DX目录与此前独立PASS三候选逐字相等；仍需本次实际input-snapshot和逐ID判定，不直接把候选签名改名为actual签名。读取根AGENTS及适用环境指令，固定R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0` 只读。来源/前提/验收见本批findings和P中source-successor.json。

新公共变化也在本次独立范围：audit/source-traceability.md只把一条区域素材泛称改为根目录两BMP可得、底图/宿主未知；planning/feature-matrix.md追加F18-04/F18-05的第三轮状态与来源，保留旧Reviewed/PASS_SCOPED原历史范围。核两者与正式正文、CV-M30/GN-M14/GN-M20及来源后继一致，所有actual独立复审/接受/关闭保持PENDING/false；这两处新增公共字节没有候选正文PASS代签。

核完整actual差异仅3正式、2公共、4管理记录，其余128正式/旧报告/229和341历史/参考未改；U01/U03候选、U08和M02-003不纳入。比对新增来源状态记录，不重新全仓review，不递归读所有旧raw/ACT。必要M01/M03资源与M09生成器/会话计数接口按旧qualified范围定点复核。保持底图、真实工程、浏览器/宿主/异常与检查点未证，所有行为/静态案例NOT_EXECUTED；字节/JSON/patch检查不算运行PASS。

复审只写 `review/remediation-third-20261012-prepare/U06/actual-integration/independent-review/attempt-01/` 下六文件：input-snapshot.json、report.md、findings.json、per-id-verdicts.json、output-identities.json、model-request-receipt.json。父任务先从冻结包commit建独立review分支或工作目录；输入snapshot绑定P/tree、base、作者、旧候选报告、新正式/公共/管理文件的完整blob/SHA/bytes、实际读取范围及角色分离。输出新PASS/NEEDS_REVISION/BLOCKED应逐ID给真实actual条款与公共承接证据；不得改任何受审文件或登记接受/CLOSED。完成后返回真实报告commit/tree与路径，正常提交推送并读回，不force、不清理未知文件。

实际review合格后才由唯一整合登记员依授权登记正式接受。最终关闭仍须必要后续/全局U07整合条件满足；当前2/23实际字节已整合、0/23正式接受、0/23关闭，六主题批分母不变，U07未完成。U06没有U01/U03前置，不等待旁批候选。每有实质进展汇报；技术取消先核任务/commit去重，真正用户停止或权限拒绝遵守。
