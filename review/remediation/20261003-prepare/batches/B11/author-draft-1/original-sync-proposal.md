# B11 有界原规格同步提案（待父统筹登记）

正式基线 `0cfe99094b76f8d75fded0d638694677855a5f0c`；派发管理资料 `4cb51a33402ec6559a396226239afe308a4b8849`。本提案不修改原规格，不是可复审候选，不构成质量批准。

唯一 finding：GIR-FD82-B019。两个原规格已静态回读，原错误与净化稿同源：WP47-A §5.1把重定向前门称为“目标原始数据”，WP47-B §3.1诅咒行只列初选而未连接最终重定向目标。原完整身份、条款、完整diff和拟议后身份在 `original-sync-proposal.json`；可应用patch在 `original-sync-proposal.patch`。

请求父A-REG仅登记这两个路径/条款的scope amendment。其它原稿、原测试、既有批准记录均不纳入。作者须收到具体登记批准再应用。该要求来自本批派发合同的 `potential_original_sync_contract`：“coordinating public writer records batch-specific amendment before apply”；不是新的用户阶段批准，也不继承B10许可。

静态依据：固定参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 的目标构造、重定向入口均查动态类别；类别的单目标/可敌方属性和当前列表恰1分别判断。CURSE在当前幽灵使用者下为RandomNearFoe（旧代NearFoe），与默认User不同；AllNearFoes的类别多目标，即使列表1也拒重定向。龙箭先扩展再PROPELLERTAIL/STALWART返回保持。

最小静态设计：世代8双打，U席0当前幽灵HP101/101，无禁止重定向能力；席1/3存活邻近且未咒，无其它目标阻挡/半无敌/吸引/恢复物；席1已合法跟我来标记1，CURSE随机初选固定席3。本次类别RandomNearFoe，最终席1诅咒真、席3假、U扣floor(101/2)=50至51。清除跟我来且其它输入不变，最终席3诅咒真、席1假、U仍51。精神场地接地U使用EXPANDINGFORCE、本次AllNearFoes且列表恰1时，即使当前唯一对手有跟我来标记，也不能进入重定向。均未执行。
