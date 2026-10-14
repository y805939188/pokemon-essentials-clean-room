# U07 actual-01：已审字节与SC限定范围机械接入

U06限定接受固定 `3168619bbc510cadeb99c82fcdfbda0fa9f0c003` 已核，累计85owner/535条件/248作者操作；U01/U03/U06所需准确门满足。固定作者 `367827c70622071bdbbd1db91111bc8e208a946f` / tree `25d8cfe853347d7afa5dbf1f7ec1097e48862491`、证据 `70d1d4773af04fab74cdf3a91fbb0d4ecff924f1` / tree `afe9e4a48739d33f90b8f59c93a1b0ff9640ce6e`、原独审 `eb95457623e001968510335dc29dcd0e5b04dbac` / tree `36aa1675fb87750449be1655c2ac64c0ffaf8ba4` 的7项/33条件（32正常＋1纠正前提）仅作当前实际来源资格。

四正式目标：WP75独占完整镜像精确相同，WP72/WP73-A/Demo测试三共享路径13原片段按当前接受基线机械接入。13锚唯一、3旧贡献完整保留且1新组合可逆，原75接受路径全文blob未变，无未解冲突或语义改写。原B5补丁在scratch独立重放；当前补丁保留已有U01/U03字节，整共享B5投影不覆盖当前文件。

[精确映射](candidate-to-actual.json)、[当前补丁](current-to-actual.patch)、[上游/共享/SC](upstream-impact-and-gates.json)、[机械核验](mechanical-validation.json)、[正式131身份](formal-tree.json)。SC-U07-001沿已注册后继：捕获体不跨LF、完整独立call行可命中并整字段丢周围行、外围空白LF另述。author/findings/1/failure_cancel_partial_submit的错误子句只保留原证据身份，明确排除当前事实/语义签名；不删002 required、不改冻结报告或合同、不要求正确候选返修。

实际commit/tree由后继locator绑定，交[原独审入口](reviewer-entry.md)。U07实际PASS/正式接受0、CLOSED0；33当前条件仍须独立判定，不能将candidate/TOOL_PASS转签。U08和整共享资格/最后关闭字节/唯一激活另保留。

所有旧FAIL/两MISMATCH/SC及optional/政策/宿主限制保持，原环境与未发布成果不触碰，不归档/释放/危险恢复；main不合并、Mac不动，新增参考/模型/宿主行为执行0。固定包只机械应用一次，重复用已冻结actual。
