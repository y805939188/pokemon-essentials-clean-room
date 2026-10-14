# 第五轮激活后的主分支与历史保留盘点

本轮92 mandatory已按确切候选、同原非作者关闭复核与唯一回执激活。激活core为 `12df95a8e81061a606d50d3f0a0528793b2e6b2c` / tree `9dcbca8504b6b576b64059f5aba69cfb1c98f703`；最终核验发布为 `0378dc85cab61642ca1467e5a901b3c829df976a` / tree `8ddacd032ef6524b7ddcaa63fa8b4bf116086b9e`。正式131的tree仍 `1046fbb657882e84b3dfc6d017943a9edf7782e5`，support3及R没有改写。有效OPEN0/CLOSED92只限原已审静态整改与具名有限组合，13材料/宿主限制与所有历史资格保持。

最新用户允许本轮结束后整理GitHub和本地、merge/push及清理；父任务明确要求先给证据与推荐顺序，等其协调本地同步后执行。此目录是只读盘点及可审查计划，尚未merge main、建/删tag或分支、清理文件、操作Mac或原环境生命周期。

## 已有证据

- 远端29 heads、149 tags；主分支仍B5 `9366d9d17aaeac3b4414236468affa650fb3dd27`。
- B5是最终发布0378的祖先，left/right为0/36；当前可普通快进，预期正式tree1046不变。实际执行时必须重新核最终head，不能用本快照覆盖后来本地同步产生的新main提交。
- 59个本轮索引/原owner/实际映射所需项目commit目前有远端引用保护；其中37个不是整改发布线祖先。JSON/Markdown中的SHA不是Git可达性根，直接删除独立作者/审者分支会让部分证据失去可靠保存点。
- 23个分支有相对其它已知远端根的独有历史；这是保守计数，142个旧tag的历史对象未在本云端加载，未借此声称独有历史无用。149旧tag全部保留。
- 连接的GitHub只读PR搜索返回0 open PR。匿名REST尝试存在transport失败，未审计认证/额度；最终PR证据来自成功的连接读取。执行前仍重查保护/PR要求。
- 当前整合云端工作树clean；这不证明其它作者/审者环境或用户Mac没有未发布工作。父任务须先收交接，本任务不扫描或删除其它环境资料。

完整逐分支tip/tree、祖先/独有历史、关键commit覆盖见 [remote-branch-inventory.json](remote-branch-inventory.json)；逐候选预期tip和归档/删除门见 [conservation-plan.json](conservation-plan.json)。

## 推荐顺序

1. 父任务衔接本地同步：确认所有作者/审者已发布/未发布成果保存位置、当前分支tip，避免用户Mac和云端同时改main。不另要求用户重复授予已给出的清理权限。
2. 重新获取远端head/tag元资料并比对预期tip。保留main、整改发布线、第五轮全局报告分支和最终关闭复核分支四个重要分支；149历史tag保持。其它25工作分支只列为“归档后可退役别名”，不能因旧名字或PASS就丢弃内容。
3. 普通创建并推送 `archive/fifth-20261014/branch-tips/<原tipSHA>` 指向待退役tip；逐项核远端tag目标和59关键commit覆盖。若一个关键commit不在任何保存tip祖先链，另外给该commit准确保存根。tag名冲突只复用相同目标或选择新名，绝不force/改旧tag。
4. 父任务协调后核main仍为确认的起点，整改最新tip仅增加已登记交接资料，正式1046/support身份未变；普通快进发布main。如果有保护规则走正常PR/所需检查；若main已有新提交，停止机械覆盖并据新差异作必要协调，不force、不重写已审规格。
5. 核新main commit/tree、formal131/support3、92激活及新发布载荷完整读回；在此确切main创建普通交付tag `delivery/fifth-round-closed-final-20261014`。未通过远端核验前不删工作分支。
6. 仅删除已经保存、当前tip仍等于预期、没有活动PR/保护需要、没有独有未发布成果的25候选工作分支别名。若tip变化，保留并更新有限盘点；不删除149旧tag，不改R，不丢历史FAIL/SC/MISMATCH/冻结包/接受候选。
7. 云端临时文件只按明确自有临时范围检查后整理，不删可追溯材料、不归档释放原环境。用户Mac的checkout/同步/本地branch整理由父任务另行协调；本任务当前不操作Mac。
8. 收尾后用确切最终main、formal tree、交付tag和报告索引填实 [sixth-full-review-prompt-draft.md](sixth-full-review-prompt-draft.md) 的基线字段，再提供给用户手动本地启动。它要求全量新双向审读，禁止只验第五轮92项或仅抽样/只看修改文件。

## 当前待衔接项

唯一激活及完整读回已结束；主分支发布、归档保护、工作分支退役与Mac同步都等待父任务按上述顺序衔接，尚未执行。第六轮prompt完整范围已拟好，但最终主分支身份未填实，明确不得据草稿启动审查。
