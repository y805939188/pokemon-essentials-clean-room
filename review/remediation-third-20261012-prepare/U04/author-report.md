# U04 作者候选交付

状态：CANDIDATE_READY_FOR_INDEPENDENT_REVIEW。仅作者修订和自检；没有独立候选判定、actual写入、正式接受或CLOSED。作者角色为本云端委托任务 /root，与父任务随后派出的独立reviewer、唯一整合登记员分离。

固定派发 `9d5993edb2f1aa543074cf6e767271523851cbf9` / tree `595aece95a1a7812ba252e9146a2c3e7f4086f42`；接受基线 `3538202ff571268fb712c4b83cd555b83d6424b4` / tree `c5771cb2c864da5581a7f63799c2fcc6d29510d7`；原交接H `d5b6af3ebbabc57ed7fbdc2e1fb2c4736dbf9a65`。只读参考R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0` 在本环境按固定SHA获取，未运行或修改其文件。作者分支 `remediation/third-20261012-u04-author`，独立工作树 `/workspace/u04-author`。本文件不循环嵌入自身commit，真实commit/tree及远端完整读回结果由外部最终交付绑定。

12份完整候选均从接受base完整字节复制后有界改写；WP28从批准U03的 `daaa7d1e1ec6b73999cb4c6aae980aebd145aa77` / 43439 bytes继承。8份作者附属产物合计20个允许新路径，正式路径、公共同步、U02及其它批次、旧报告/229状态/341精确贡献元组未写。U02正式候选写集交集0。

| finding | 正文与覆盖映射 | 静态设计及确定结果 |
| --- | --- | --- |
| GR3-M07-001 / N12 | WP28 §3.5.1及执行/容量段；WP40 §3.2/§4.2/§4.2.1；WP42共同次序/§6.0 | U04-RF01–RF06：POTION2→两登记0→首治满清身份→次资格失败退1仍有身份→同轮普通毒伤终局再退2；继续下一命令1、正式失能清身份1；首份未执行正常回退2→1→2；两退款容量拒绝独立边界；Direct5资格通过空效果仍0 |
| GR3-M08-001 / N13 | WP47-A表行/§3.1.1与自然之恩数据§3；WP46 §2.1.1/亲子爱行及覆盖§3；WP50 §5.1.1与HPHeal/OnBeingHit覆盖行 | U04-NG01–NG04、U04-MH01–03、U04-HI01–03：H160/h81 ORAN/亲子爱/存活JABO首击基底80及目标δ1提交→反傷20到61→ORAN回复10到71、C/I条件清/RP与序号/Belch提交→第二击空持物身份首次失败，早于get/默认1/第二击HP；h101到81不自耗而正常续击，单击无再查询；物品仍存在但标志不完整另得1 |

三份测试目录的原完整字节均是新目录前缀，原行/顺序/重复/静态向量保留。新案例均具名前提、步骤、终值或首次失败点、前缀与反例，execution全部NOT_EXECUTED。目标δ1明确为首击普通规则的已提交正损失且目标仍存活；没有为本修订补全任意伤害输入或执行模拟。

10个qualified控制按本包完整控制对象/准确元组绑定，局部保留理由见author-self-check：003架构中立、A046主动/持物/AI回复分工、B003完整规则键、B007重量单位独立门、B008资格过无效果不退款、B010最终OHKO资格、B013伙伴一次还原错位、B014成功击与HP损失、B015未来攻击早清关系、B017整数均分及两端物品。五有限交界G4-9/G6-2/G6-3/G7-5/CHAIN-3和N12/N13分别映射，不新签捕获/Arena/录像/完整AI，也不以同ID承载者增加其它owner义务。冻结JSON完整解析/字节核验与相关实质投影审读区分；无全局历史重跑。229/341仍是原问题及scoped贡献口径，计数/哈希不是行为或质量证明。

静态核验：20个正式读取身份、21个必需参考身份、15个核心/模块H身份及U03接受/交接2身份完整字节匹配；另只读一个正常裁判接点。补丁仅含12允许正式映射，base/派发可应用检查与正式映射/非补丁文件空白检查完成（补丁26个空行上下文前缀按diff格式保留）；在第二个临时Git index重建补丁，12个完整blob与候选逐字节相等。未apply正式工作树。U03探测仪、经验糖果/HP/TR/取消/EXP资格与旧控制相关段、伙伴恢复和所有旧测试精确保护范围在自检中记录。

AI只读WP52-B §2.1 / WP52-A §3.2当前ORAN预测；未将真实JABO/自耗续击故障推广到AI，也不传播早期WP52-C误指。WP67-A/UI只交ui-consumer-proposal给U05，未放行U05。历史缺陷未来兼容/修正由用户在实现阶段另决；外层诊断/继续/恢复/进程退出、真实媒体/地图/宿主/Demo未运行认证。不因这些unknown另开补文门。

产物入口：[candidate-identities](candidate-identities.json)、[完整整合补丁](candidate.patch)、[作者自检](author-self-check.json)、[追溯提案](traceability-proposal.json)、[登记提案](registration-proposal.json)、[UI消费者提案](ui-consumer-proposal.json)、[模型请求记录](model-request-receipt.json)。缺模型回显记UNVERIFIED，不审额度/后台模型，不用隐藏CLI。

父任务独立reviewer入口：[independent-review-task.md](independent-review-task.md)。必须使用外部最终交付的真实作者commit/tree，读取12完整候选与identities/patch/本报告，按两finding全前提和有限10控制独立判定。reviewer不是作者/登记员，只写其六文件输出根；合格候选后唯一整合员再核base实际应用，独立actual复审之后方可登记正式接受，CLOSED仍待U07/必要依赖。本作者未启动或代签这两个复审阶段。
