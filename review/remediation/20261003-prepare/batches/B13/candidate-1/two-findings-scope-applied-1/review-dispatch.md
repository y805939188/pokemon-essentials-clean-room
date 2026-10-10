# B13 原两个 Ultra 增量复核入口

当前状态：两问题作者返修完成，WP58新原稿固定补丁已获scope-amendment-2并精确应用；**等待原独立FULL/affected增量复核，尚无质量PASS、G或C**。

正式FIX_BASE `8e67f780c204d593d89f364f585d2c6c2fe74631` / tree `ae2f491294eb4f97be6b75f75706c16279f9bf46`；复审OLD `5845e8084ced280e51c51a4081ec8583a9c2ca39` / tree `23f92a9c446f5f0fbcee44df2f57d85df4dd0e3c`保持。最终NEW candidate SHA/tree、完整未过滤OLD→NEW diff及远端ref/FETCH_HEAD/全部输出读回见随后同目录 publication-receipt.json / publication-summary.md。

1. 原Ultra FULL角色：以 `review/remediation/20261003-prepare/batches/B13/author-draft-1/two-findings-scope-applied-1/finding-dispositions-successor.json` 及 current-evidence-index.json 核验完整8贡献/5主责及所有原控制/最低验收；B13-R01 的当前 WS-W35、nil null/return_identity=nil、空列表false后态和UI人数门位于保留的 `review/remediation/20261003-prepare/batches/B13/author-draft-1/two-findings-repair-1/static-transition-traces-successor.json`。历史原trace中的false只作为冻结旧错误证据。
2. 原Ultra affected角色：B09/B11复核B13-AFFECTED-F1，见新净稿WP58 §5.2、原稿WP58 §5.2、RC-W26及保留的当前entry_final_scan轨迹/consumer导航；WP41/WP49/WP50及WP47-B只读身份和完整既有有限影响范围见 affected-interface-navigation-successor.json。检查逐成员item后ability、首真即停、开场首命令前录制/回放、攻击后行动限定、取消先耗物和EOR延后选择；保留W16/W24/W25/随机/Arena门。

两个问题的完整逐项响应见 `review/remediation/20261003-prepare/batches/B13/author-draft-1/two-findings-scope-applied-1/two-findings-repair-map-successor.json`；许可与精确after见 scope-application-receipt.json。新scope `231c9f25df4dd64961fb9290ff52302782a9fdb8`仅许可固定patch `8d186d65c9eb2bc0e03a27728bfa0ea8476f4753bb863054b41cdb3b79459b0d`，不改变OLD评审结论，不扩展B027或邻域作者范围。

保留catalog137未执行设计（QC47/WS35/PA28/RC27）及全部非本次问题正确内容，证据见 protection-and-metadata-verification.json 和 all-11-formal-output-identities.json。历史pending提案及原两位reviewer输出保持原身份；当前successor才表示已应用。旧其他affected verdict只限OLD，不代签NEW。

作者未开子任务、未自签门，未运行参考/Ruby/游戏/行为向量/历史程序。独立candidate门后才可G，actual FULL/affected另复核，C由唯一登记者处理；canonical/B030增量0，B16/WP67-A依赖保持。
