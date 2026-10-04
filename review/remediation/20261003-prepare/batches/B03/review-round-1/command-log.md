# R-B03 可复核命令与执行界限

本次命令只用于Git、原文本阅读与报告元数据。参考Git在主项目外准备为 `/workspace/reference-b03`，固定 detached HEAD；核HEAD/tree/status后只读。没有运行参考Ruby/游戏/编译/转换/生成/反序列化/模拟器/求解器。审查者新写的Python只核Git/JSON/行ID与受保护字节，不导入参考、求值参考表达式或执行静态向量。

## 获取与冻结

主项目：`https://github.com/y805939188/pokemon-essentials-clean-room`。

```sh
git fetch origin '+refs/heads/remediation/20261003-prepare/*:refs/remotes/origin/remediation/20261003-prepare/*' '+refs/heads/review/2026-10-03-fd82a639/*:refs/remotes/origin/review/2026-10-03-fd82a639/*'
git switch -c remediation/20261003-prepare/review-B03-1 76b6f6c6f14f1d676f370be72b61cb2f0a069633
git ls-remote origin refs/heads/remediation/20261003-prepare/batch-B03
```

远端作者分支核得交接 `76b6f6c6f14f1d676f370be72b61cb2f0a069633`。从原review Git对象提取完整findings、root index及34场景；未以作者重新整理字段替代原对象。AGENTS全文已读，未发现适用本地SKILL.md。B02接受/整合报告、B03合同/验收/依赖/锁与批准原稿同步材料按冻结身份读取。

```sh
git -C /workspace/reference-b03 rev-parse HEAD
git -C /workspace/reference-b03 rev-parse 'HEAD^{tree}'
git -C /workspace/reference-b03 status --porcelain
git diff --name-status 9576f00e7d3aeb96f7ca8c42caccfba8f808505e 1e395a21eb3d5ed0be9426ed3d3f4443129b5ce8
git diff --name-status 1e395a21eb3d5ed0be9426ed3d3f4443129b5ce8 76b6f6c6f14f1d676f370be72b61cb2f0a069633
```

reference SHA `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree `7589c800b61ba13a13040ed0d686979b80a84fd0`、status空；结束前再次核验。38完整候选差异路径，交接仅3证据新增；13正式文件byte/blob/SHA256一致。

## 独立阅读、首判及比较

`rg`定位后以`sed`/`cat`/`nl`读固定原文本。13正式候选全文、27原完整对象/current_qualifications/二审和全部扩展、验收与相关上下文均纳入。来源阅读具体范围/身份在source-reading-log.json；范围是导航，不表示分支运行覆盖。

`independent-first-judgment.json`保存于 `2026-10-04T12:20:46.804206+00:00`，准确工具时间在文件中；其保存时作者自检/响应/追溯/建议尚未读，scope/identity材料已读。保存文件SHA256：`d6d443910cfd24195ace9bf4c42c199cf3896b5a073f2193b355aa9256cf00af`。之后读取作者两轮审计脚本及最新结果/verification/响应/追溯/建议/来源日志；首判保持，三个反例由额外定点来源阅读再次支持。

## 独立机械核验

```sh
python review/remediation/20261003-prepare/batches/B03/review-round-1/verify-inputs.py --project /workspace/pokemon-essentials-clean-room --reference /workspace/reference-b03
git diff --check
```

结果为 `PASS_IDENTITY_AND_PROTECTED_BYTES`，语义为 `REQUEST_CHANGES`。检查57＋1＋22身份、27完整原与验收对象、全部候选/证据路径、13正式一致、16旧作者证据、历史审批尾部、B01段/行、139原ID/96新增/235未执行行和WP15/59/60共享尾部。首次审计把B02身份字典与含额外verified/in_fix_base的作者字典直接比较，后改为只比较五个身份字段；字段及身份全部一致，不是候选缺陷。

没有执行作者自检脚本（其默认范围会包含新增审查文件），只阅读并独立核其声称。固定墙/自动邻接表和九谓词/四组编号为人工原文本逐组比较，未编写/运行公式或生成器行为验证器。

## 普通发布

```sh
git add -- review/remediation/20261003-prepare/batches/B03/review-round-1
git diff --cached --check
git diff --cached --name-only
git commit -m 'review(B03): independently review full candidate and record three P2 discrepancies'
git push origin HEAD:refs/heads/remediation/20261003-prepare/review-B03-1
git ls-remote origin refs/heads/remediation/20261003-prepare/review-B03-1
git status --short
```

发布提交SHA由最终执行回报单独给父任务，避免报告自身commit自引用。仅本报告新目录允许写；无main/force/reference上游推送，无正式/旧review/canonical状态修改。普通push后核远端分支SHA与本地HEAD相等；实际integration仍须父任务提供新SHA再核。
