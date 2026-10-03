# 第一组三包 v3 元数据收尾：仅 GROUP1-C02

在 `/Users/dingshinn/Desktop/pokemon-framework-reference` 工作。先读AGENTS、planning/extraction-plan.md §2.2、本目录report.md／findings.json／registration-checks.json／metadata-checks.json／inputs.json／final-checks.json。

本次复审确认：原29项全部CLOSED，GROUP1-C01 CLOSED；GROUP1-C02仅剩元数据说明。不得重做行为提取、重开已关闭问题或改写三份主稿。WP66-A 49f373e2／44,563、WP63 154de9e6／33,115、WP64 2e875f8f／25,927三个完整身份以本目录inputs为准，须保持不变；fixed和三份self-checks当前版本／场景／身份已核对正确，保持不变。

## 只做以下收尾

1. 修改活动组摘要 `review/wp66a-wp63-wp64-delivery-2026-10-01/delivery-summary.md`：
   - 第3行仍写“当前修订v2”，改为当前v3与实际收尾状态。
   - §6明确v2是历史初修阶段、v3是本次补修；准确写原29项和GROUP1-C01已获本次复审关闭，GROUP1-C02正在做元数据收尾，不自行宣称其已通过。
   - §7仍写第78轮／v53、主稿v2，应明确历史与当前。当前输入登记为第79轮／v54（1057／962行），后续收尾若产生新登记轮次，按实际最终结果写；不要把这些旧数字硬编码成新最终数字。
   - 保留已正确的全部行为摘要、三份正文身份、场景数量41／33／30与历史被审身份。
2. 新建 `review/wp66a-wp63-wp64-revision-2026-10-01/v3-metadata-closure/` 保存收尾回应、摘要diff和实测检查。明确更正“恰13项漂移”：相对v2复审25个输入，在v3登记全部完成后实测14项，多的一项是组阶段registration-final-checks.json；没有越界修改。列出完整路径和计数时点，不把较早13的声明继续当最终结果。
3. 原v3修订目录及其checks／registration-final-checks留史不改。活动组阶段复核中相同13项声明可追加具名勘误，保留原轮次记录的历史角色；更新当前最终身份时以本次磁盘实测为准。
4. 同步必要的manifest／主TSV登记。摘要只写轮次、行数和核验文件链接，不嵌入会注册摘要自身的TSV最终哈希；最终manifest／TSV身份另存登记完成后的独立检查，避免自引用循环。当前角色与历史角色都要明确。
5. 最终验证：三个主稿、fixed、self-checks身份完全不变；其余改动仅限摘要、必要行政登记、活动组阶段检查和新收尾目录；登记对磁盘无偏差、无重复；摘要各处当前版本一致；漂移范围／数量在最终状态下如实测量。

交付后停止送收尾核验，不自行关闭GROUP1-C02、不启动WP65／WP67-A／WP67-B。较早GR-001～016仍待有界整改，不在本次元数据收尾中顺手修订；N01已通过范围不重开，管理性回填与B批整合另记。

reference只读；不执行参考实现、游戏、编译转换／生成器、真实网络或未知载荷；不实现框架；不创建任务／Agent、不发跨会话消息、不提交／推送。
