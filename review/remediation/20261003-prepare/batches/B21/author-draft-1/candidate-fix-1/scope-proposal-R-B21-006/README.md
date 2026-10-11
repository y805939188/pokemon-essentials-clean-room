# R-B21-006 具名局部写入提案（尚未应用）

固定FULL报告指出：WP75原稿与最终正文§8.6都把匹配限定为字符0，而已接受WP13矩阵为原串任一行行首。需要同步两份WP75，防止原稿/最终正文分歧；现有WP13正文及MR08准确，不请求改写它们。增加MR18–MR22给多行、匹配行前空白/接收者、后续行仍可匹配与求值异常对照；原MR01–MR17保留。

请求范围恰三路径：原稿 specs/demo/wp75-project-conversion-and-authoring-tools.md 的§8.6一段；最终 demo-dx/wp75-project-conversion-and-authoring-tools.md 的§8.6一段；最终 test-catalog/engine-overworld-wp11-15-59-60.md 仅在MR17后新增MR18–MR22。没有实现代码、原参考代码拷贝或行为执行。

[scope-request.json](scope-request.json) 给精确before/after blob、bytes、SHA256及逐路径必要性。[complete-proposed.patch](complete-proposed.patch) 是这三路径的完整修改，仅发布一次；before/after目录保存完整UTF-8原件和拟稿，供唯一登记许可核对。补丁已在隔离Git索引从旧NEW验证到全部三个after blob；没有写入工作区的这些保护路径。

B21原合同 allowed_original_write_paths_now=[]、22正式写路径不包括这三路径，FULL R-B21-006明确要求父任务先协调具名局部许可；本轮用户指令同样要求先提案再应用。这是实际权限边界，作者不能自行豁免。由父任务协调唯一登记员记录精确许可后，获准owner/作者才应用这些字节并刷新真正变化的来源/条款/案例依赖，重新冻结NEW并交原独立R-B21复审。旧327接受、历史证据和原NEW保留，不移签或自签接受/关闭/FINAL。
