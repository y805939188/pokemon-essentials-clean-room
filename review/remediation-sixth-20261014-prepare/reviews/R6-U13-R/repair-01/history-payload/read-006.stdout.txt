# R6-U13-A 修订01

本后继针对固定非作者报告 `3ef4854ef43eac92fd1dc57350e4cf6aa160082b:review/remediation-sixth-20261014-prepare/reviews/R6-U13-R/review-report.md` 的 FAIL。报告及相关 S001、历史/工具审计、R5路径恢复和 WP66-A 接收载荷均已完整读过，身份列于 checks.json。旧候选 `00b45de642f07cee9953e42f04cce9c35d77346f` 与冻结 FAIL 保留，不改写其裁决，不预签本后继独立 PASS。

镜像仅改 pokemon 测试目录第40行 SF30；其余七份镜像、该测试目录其它原始行和全部非 SF 后缀逐字不变。没有新增 ID，QC49/WS36/PA32/RC29/SF40、新增14个 ID口径保持。WP53 已保留对应正文，未改写已通过的其它七项规则，也未恢复活动模式广义保存禁令。

| 原正确控制 | 新 SF30 承接 | 判断与界限 |
| --- | --- | --- |
| 旧 b：正常结束后保存→载入，非活动会话/统计持久 | d：两会话正常结束、持久值/保存/普通载入依赖有效且无其它改写，正常保存→载入；仍为未开始/已结束态、模式统计持久 | 作者静态设计；计时起点等运行时刻的重载语义仍未知。未执行真实保存/载入，不把普通载入的其它统计更新说成全部统计不变 |
| 旧 c：保存转换检索，无两模式专用格式迁移 | e：固定参考当前默认转换集合及注册者，排除插件/动态追加；无 Safari/捕虫专用格式转换 | 新完整读取固定 Conversion 1–223 与 SaveConversions 1–420；限定默认集合，不推任意版本/插件或整个存档无迁移 |
| 已核新 a/b/c：Save 与普通 Quit Game/专用退出集合 | 两列原菜单文字作为完整前缀逐字保持，再追加 d/e | 不把专门 Save 隐藏扩大为所有保存禁用，不把保存活动对象改回只有非活动对象 |

R5 三个 `retrieval_note` 与 bind_history.py 已纠正。初期本地精确路径读取失败是真的，但不能由其诊断文本推出固定提交无该路径，失败原因未记录、保持 UNKNOWN。原作者已取回两枚准确 blob 并读取三个原资格投影，本后继不改这些投影。当前按准确 f49d commit/path，通过 GitHub 完整取回两原件，再从本地已 fetch 固定对象完整读取；bytes/SHA256/Git blob 全等：

- root-M07/canonical-findings.json：58751 bytes，`bbdee0813200953d50abf647b73341466d5559c9`，SHA256 `8f4e67617983a96a2f1fdc76a40d24cb97ad0d189c623670f6a711d6295cb6f6`。
- root-JXN/canonical-findings.json：162386 bytes，`7b21312f9f3512bfdd57e21a17cfb83096074050`，SHA256 `8de2ac509bc7ff2ddefc0d40536afc9a3247acdedfa828e179ff0f973ca8e4e8`。

完整精确路径和新远端回执在 r5-path-recovery.json。旧失败/错误推断所在候选 commit 继续可读；后继转换记录明确撤回“路径不存在”的推断并保留初期失败，不补造原失败 UTC。生成脚本现在实际读取固定 commit/path、核对预期完整身份与 mode/blob 后才生成恢复说明，防止重跑写回错误结论。

撤回旧 verify_candidate.py 的两个过强证明：先转字典再比较唯一性，不能查原始重复 ID；允许 SF30 整行变化后跳过比较，不能证明正确旧子例保全。修后先保存原始 ID 序列、检查总行数/唯一数/重复计数，再建索引；对 SF30 单独核 d/e 的前提、预期和边界文本，并核 a/b/c 两列前缀。check_repair.py 的受控文档反向检查确认：冻结 FAIL 版缺 d/e 会被拒绝；注入第二条 SF30 会在建索引前被拒绝。此为机械文本检查；上表的语义保留是作者静态对照，不用关键词存在性冒充任意子例完整证明。

因子30仍按已审原规则作 DERIVED 预期常量；本工具并未独立计算概率因子。tool-validation.json 已把两次整数除法和给定常量比较，与 `expected_constants_not_computed` 分列，明确撤回概率语义的工具证明。没有为已通过 V005 新建行为模型或重做全量审查。

七个已审通过 ID 的镜像字节未变，保留原冻结审查范围；S001 的 SF30 改动及证据勘误提交同一父线程指定非作者审者重新核验。SOURCE_STATIC、DERIVED、TOOL 分开；本后继参考/serializer/宿主/Demo、真实保存/读档执行仍为0。actual model/effort/tier/speed/UUID仍 UNVERIFIED，未检查配置或派代理。

WP66-A §4.6 正数人数容量门、读取值焦点及最终判断区别的完整接收载荷已读，归 R6-I 唯一整合者后置责任；本作者未越写集修改它。该接口实际接收、共享全文复审、正式接受及 CLOSED 仍阻塞。后继作者检查完成不能代替这些门。
