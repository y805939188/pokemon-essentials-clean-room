# 父会话云端委派输入

读取本文件所属固定提交中的 README.md、delegation/batches.json、delegation/conflict-groups.json。作者可从13个AUTHOR_READY入口按真实服务slot并行启动；使用同目录prompts/<批次>-author.md和contracts/<批次>.json。模型GPT6.1 sol xhigh、普通速度default，禁Fast；实际回参未知继续UNVERIFIED。每批只写自己的candidates镜像，不改正式文件，不提交推送，不派生子任务。

作者完成后由唯一整合者R7-I先固定真实context和候选提交/逐文件身份；再创建不同context的GPT6.1 sol ultra/default普通速度reviewer，提供同批-reviewer.md和candidate-input.json。未完成候选不启动reviewer。候选PASS不等于整合PASS、接受或关闭。

候选逐条整合后，再建新的独立R7-IR，绑定实际整合commit/tree并核所有已合贡献和共享文件。R7-I据真实证据分别登记候选PASS、实际PASS、ACCEPTED、CLOSED，分母始终27项/13批。独立复审不由作者自审替代。用户已经授权提交、普通push整改分支和正式接受达标批次，禁止合并main/force/删除旧证据。

发布提交身份由外部最终回传绑定，本文件不写自身commit。若本云端无法按指定模型/普通速度创建独立任务，父会话使用这些精简入口创建；核对launch-attempts与ledger避免重复开工。PID或thread存在不等于有效模型配置认证。
