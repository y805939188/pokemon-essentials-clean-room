# R8 GitHub 收尾预检与条件清单

这是只读盘点形成的准备材料。尚未合并 main、删除分支、创建归档标签或修改保护规则。清单中的删除步骤只有在正文、可选、累计打标、整轮独立 ultra/default 验收及正式闭环全部完成，并正常合并 main 后才可执行。打标当前仍为 R2 FAIL 7 项，整轮未冻结。

## 固定快照

盘点开始于 `2026-10-17T16:22:20.996410+00:00`。远端 main 为 `fd1df570cad987dc3852a3b958f03916e317f7fe`，整改分支为 `62c5dd3f6d9f57b99104ab3e5e7b96e4af7ae01a`。main 是整改分支祖先，提交差为 main 独有 0、整改分支独有 71。开始、独立抓取与结束三份引用清单一致；这只说明盘点窗口内未漂移，不能替代执行前复查。

共 103 个分支、257 个标签，完整提交图包含 1,393 个提交。用于图核验的独立 bare 仓库无 shallow、无 alternates，采用 `blob:none`；它已抓取提交与树，**不是完整文件字节或离线备份**。当前交接、接受、路线图和打标记录明确引用的 53 个内部提交均可由远端公布的引用到达。该 53 项是列明输入记录的范围，不代表重新审查了全部历史报告。

## 保留与清理去向

- 保留默认分支 main 及全部 257 个现有标签。
- 3 个其他分支头已在当前 main 中，2 个分支头可随整改分支正常合并进入 main，2 个分支头已有保留标签保护；这些共 7 个分支仍须通过最终门槛、归属完成及实时身份检查，之后才可删除。
- 其余 95 个分支头目前未被 main、整改分支或现有标签保留。为每个原始头准备一个完整 SHA 命名的 `archive/eighth-20261017/branch-tips/<SHA>` 标签，逐项核验后才可删除原分支。此方案沿用既有按原始头归档的审计方式；保留来源分支到原始提交的直接映射。
- 整改分支和打标作者分支处于 active hold。其他分支也须核实任务已结束；名称所示的历史角色不等于作者已确认可删除。

精确的 103 行列表见 [branch-list.md](branch-list.md)，完整条件、原始 SHA、现有恢复引用及保护字段见 [branch-dispositions.json](branch-dispositions.json)。95 个待建归档引用见 [archive-tag-plan.json](archive-tag-plan.json)。现有标签逐项保留表见 [tag-retention.json](tag-retention.json)，已发布成果身份及其当前保护引用见 [published-commit-reachability.json](published-commit-reachability.json)。

删除分支不能删除其独有 review 证据。通过 main 或保留标签持续保留原提交图、树及文件对象；原 FAIL、WAIT、UTC、模型资格和未执行限定保持原样。原始材料即使已复制到正式目录，也不能只凭文件副本或文本 SHA 删除唯一的 Git 引用。

## 执行前的正常合并路径

1. 等待累计打标独立 ultra/default PASS、整轮冻结输入独立 ultra/default PASS、正式闭环和最终完整回读。固定最终已批准的整改头及内容清单。
2. 重新抓取 main、整改头、分支/标签、开放 PR、规则集、保护及必需 review/checks。任何头或内容漂移都要先定位并重新核对；不能 reset、force push 或把未审内容混入批准范围。若合并前需要处理新 main 内容，保留双方提交并对影响本轮正确性的改动补充相应独立复核。
3. 确认同一 head/base 尚无 PR 后，按当前分支正常建立到 main 的 PR。仓库快照允许 merge commit；采用 `merge_method=merge`，提交 `expected_head_sha=<最终批准头>`。保留整改提交图；满足 GitHub 当时的保护、review 和 checks 后再合并。不得启用提前自动合并或绕过规则。
4. 从工具结果和新的远端引用核实真实 merge SHA、main SHA、父提交关系及批准正文、路线图、打标和交接文件身份。读取当时 CI 状态；无检查时写 `NO_CHECKS_OBSERVED`，不能写 CI PASS。
5. 再生成最终清理执行清单。按实际头创建归档标签，不替换同名不同对象的标签；回读原对象、归档引用及祖先关系。用新的远端仓库抓取需要保留的完整 Git 对象并核验完整性/文件身份，或建立并验证包含完整对象的可恢复 bundle；本次部分抓取不满足该步骤。归档未证实前保留原分支。
6. 确认任务完成、原分支当前 SHA 仍等于执行清单、没有保护或未处理独有内容后，才逐项删除该分支。删除须以原 SHA 为条件；可在专用临时仓库使用仅允许清单项的 pre-push 核对，将服务端刚公布的旧 SHA 与归档清单逐项比较，再执行普通删除，由 Git 更新协议检查该旧 SHA。不得使用 force 参数，也不覆盖用户 hooks。若无法验证该条件，则保留分支。保留清单、恢复入口和原始提交 URL。
7. 最终再读 main、保留标签、分支、必需检查及全部交付身份，输出真实 main SHA 和清理操作记录给父任务。用户本地的 35 分支/8 worktree 及约 25.5GB untracked 的归档与同步由父任务单独负责；此处不操作、不认证用户本地。

## CI 与保护观察

[controls-and-ci.json](controls-and-ci.json) 保存本次结果及限制，原始接口响应保存在 [raw/](raw/)。两页 branches API 共 103 个分支均返回 `protected=false`；main 摘要的 protection 为 disabled，包含上级的规则集列表为空。详细 branch-protection 接口返回 managed integration 403，不能声称已读取其详细对象。仓库元数据的 admin 字段不能替代该接口实际权限。

main 和整改头的受控树中均无 `.github/` 文件，仓库 workflow run 总数为 0；两个提交的 check run、status 列表均为空。workflow collection 与 active-main-rules 路径不在连接器 fetch 白名单中，`gh api` 后备读取也返回 Forbidden。结论是快照范围内未观察到 CI 检查，不授予执行通过。实际合并时须重新读取可见规则和检查，并由正常 GitHub 合并端点执行保护约束。

## 核验范围

这是 xhigh 协调任务的引用、祖先关系和元数据机械核验，不增加独立 review 票，不改变 29/10/9 已接受计数或 `CLOSED=0`。未运行 Ruby、游戏、开发框架或 Showdown 原型，未处理参考仓库。
