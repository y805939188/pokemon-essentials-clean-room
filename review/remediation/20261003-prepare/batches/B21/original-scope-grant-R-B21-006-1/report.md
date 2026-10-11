# B21 R-B21-006 精确局部写入许可

结论：许可原作者在隔离候选分支应用固定提案的三个完整 after。本登记只增加许可元数据，三份正文/案例当前仍是已接受 B20/C 的 before；不签质量、候选通过、actual、B21接受、关闭或FINAL。

固定提案 `a740b86cb6b721c61e23fbcea5e365180fc4523e`，tree `56217c655291fd68641dd74acf9980e223fea928`；来源分支 `codex/cloud-dot-B21-author-fix-1-20261011`。提案入口为 `../author-draft-1/candidate-fix-1/scope-proposal-R-B21-006/scope-request.json`。唯一完整补丁 SHA256 为 `c2cf46c223ba8d91cc20326aab2c7eb99db62219d76cef2b210709a43265e95f`；本目录引用固定身份，不复制补丁。

| 精确路径 | 许可边界 |
| --- | --- |
| specs/demo/wp75-project-conversion-and-authoring-tools.md | §8.6仅一段，原行257 |
| deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md | §8.6仅一段，原行235 |
| deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md | MR17后仅插入MR18–MR22与一个空行，旧目录逐字节保全 |

完整 before/after 的 blob、SHA256、字节数及唯一hunk身份见 [scope-grant.json](scope-grant.json)。新文本解析核对了全补丁并逐文件重建完整 after；三路径在 C、登记输入D、旧NEW、旧发布及作者提案提交仍为同一before，WP13及MR08保留。三处限制之外所有行不变，两份WP75的修订段落仅链接位置不同。上述是身份与范围检查，静态案例均未执行。

必要性来自固定 FULL `03b821815477bd1f6834d22b2764f897f19fea0d` 的 R-B21-006：WP75把前缀限制为字符0，与已接受WP13任一行行首边界冲突；具名许可是该最低修订要求。完整 GIR-FD82-C007 控制及批准 RUN-C-007 资格身份已解引用。原B21的22正式写路径及空原稿写范围不包含这三路径，因此此许可只对固定提案作精确局部例外；原范围及历史文件本身不改写。

两路复审仍针对旧 NEW `5c3e19831e1e29450247fa6061f3c2feac2f893e`。FULL八问题与 affected `7db07543137cc11ef76b725e0a3c8975796bc7b0` 去重共九修复单元：八个已作者修订待复审，本项获许可后才可应用；这些状态均未质量通过。父任务续原作者应用、刷新真正变化的依赖并另冻NEW2；随后续原独立FULL与affected复审核九单元、14贡献/9主责完整合同和 [regression-and-source-limits.json](regression-and-source-limits.json) 的B20/B03/B14/B19接口回归。模型保持作者gpt-6.1-sol/xhigh、独立gpt-6.1-sol/ultra，default Standard；本文不创建任务。

B20既有回执保留，新WP75字节须明确纳入新审查，历史PASS不能自动转授。候选通过后仍需G/精确actual及原独立整合复审，满足才B21接受；FINAL-1、有证据的关闭/最终冻结、FINAL-2另行完成。当前仍20/21、327已接受贡献，229 OPEN、0 CLOSED。

验证细节见 [scope-validation.json](scope-validation.json)，四个输出身份见 [manifest.json](manifest.json)。发布采用普通commit/push，独立新bare环境按远端完整字节读回，结果放在外部回执，不递归追加证明提交。
