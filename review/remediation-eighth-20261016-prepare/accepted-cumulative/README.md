# 九批已接受源：累计打标校准交接

正式规格统一读取固定 `5f87743293290de2e219ecdd6c19e88280f60c9a`，formal tree为 `93dc967b4cdb653359afc123d3b8b318d6475fdd`。当前整改分支正式正文与此快照逐字节相同。29必改、10选入可选、9批均ACCEPTED；整轮与打标尚未最终验收，CLOSED为0，main尚未合并。

入口：[校准输入](calibration-input.json)、[九批精确回执](batch-receipts.json)、[39项状态与原合同/场景链](issue-status.json)。文件与章节：[131文件身份](formal-file-identities.json)、[38变化/6扩展文件及U07元数据](source-file-changes.json)、[新增21标题](heading-delta.json)、[完整正式差异](full-formal-changes.patch)、[最后UI65两行差异](last-UI65-repair.patch)。

131正式文件没有增删；38变化、93保持。标题2683→2704，新增21、删除0；其中10标题归U04，其他11归已接受的其它批。U04新增必要消费者UI65与U01共享；其余261行及U01保存/启动/No保留，最后U04接受身份覆盖两行定义。6份额外受影响正式文档来自选入可选贡献，不能仍只按原required写集绑定。U07为NO_FORMAL_DELTA，仅接收历史导航资格。

目前打标a328候选只实际应用U02/U03，八批回执/0eee定位为准备，不是累计应用完成。请独立打标owner接收本包后完成九批累计源切换、2704标题及当前行为定位/依赖校准；保留source/stable ID/旧FAIL和旧计数时点。产出真实后继commit后再独立ultra/default复审，随后才冻结整轮验收。去向仍可待验证，无Ruby/框架/Showdown原型执行信用。
