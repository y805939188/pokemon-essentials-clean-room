本轮验证分层：

- 静态：全新定区间阅读，固定git blob与工作区字节逐次校验。
- 推导：规则布尔、循环终止条件、状态/引用时序，见双向矩阵。
- 工具：只使用审读后绑定的read_bound.py及新编隔离脚本；两次越界区间读请求被断言拒绝，随后以真实25/126行边界补读。不是语义失败/通过。
- 隔离实际参考：isolated_facility_checks.rb仅加载已全文审读的会话/规则文件和已完整审读的UI单元；输入SHA256断言，所有存档/场景/地图为内存替身。第一次脚本exit1源于替身错误选Summary而非Entry，已纠正并exit0；不将该替身失误报告为参考发现。
- 独立模型：未运行独立设施模型；其它子域如有记录自行列明。
- 完整hostDemo：未运行，不接真实存档、未知脚本或外部服务。

重复开始的隔离对照显示原队伍快照会由活动报名队伍覆盖；WP55已明确开始总按当前引用保存、无禁止重复开始的前门，本轮登记边界，不另外提出重复的mandatory根因。

第二隔离脚本：isolated_record_terrain.rb仅实际ActiveField、实际录制/恢复方法、两实际setter和内存base Battle替身；没有执行完整Battle初始化/开战/命令。首次exit0；给None/Electric两输入、当前Rain对照，见isolated-record-terrain.json。只验证快照字段和恢复赋值边界。

跨域反证：R6-UI-PARTY-004声称Entry命令0跨loop block调用残留；本轮精确2人数SpeciesClause三成员夹具与实际完整entry方法在Ruby2.6.10下未调用Summary，先错误再下一选择/BACK返回nil。独立纯Ruby loop block局部变量控制为首轮0、次轮nil。见countercheck-ui-entry-stale-command.json；不将未知宿主Ruby直接签全局结论。generator对GR6-F002的下游反证建议含同一未执行残留假设，应与此负证据并读。人数0的上限提案只限此前Entry前缀，仍有独立支持。
