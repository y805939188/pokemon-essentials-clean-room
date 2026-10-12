# U07 外部冻结记录

实际P `8a0b36520b5c9c57dd893d9116cfae8620aea229` / tree `8fca4c1e4dbf051d7749276060623e2480f23992`；父AC `c2eb74c7cbcf8a190d5e902d871fbce44904efd6`。本伴随包只新增任务、输入、原样diff和此冻结记录；Q的commit/tree在正常提交后由外部返回，不嵌入自SHA。审核对象是P的22改动及真实current formal字节，独立角色输出另开分支。

完整patch见 `actual.patch`：2730324bytes / SHA256 `45ba6db7855816ca657a738249949961731198990dc6651a92c648959d9a01a4`。原样 `git diff --binary --full-index AC P`；五个标准Git diff空context行（7/23/39/55/31101）有必需的单空格前缀，外层artifact diff-check会标记这五处；不改写transport。除原样patch外的伴随文件正常diff-check，实际应用及22文件完整重建以whitespace-error检查为准。

23/23必修、6/6主题批正式接受；最终CLOSED0、U07独立待审。后续关闭新字节仍需有限独立影响接受；不新增无界全局review，不合main、不删除分支。

执行器已用独立临时index从AC检查并应用完整patch（`--whitespace=error`），重建整tree `8fca4c1e4dbf051d7749276060623e2480f23992` 与P完全相同；22实际产物完整重建。六批实际报告各自精确commit均仍为远端活动分支tip，具体refs见actual-review-input.json。
