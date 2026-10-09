# B12 affected candidate-1：B09

结论：**PASS_SCOPED**。范围：新增 WP51 结果→WP40 命令/资源；WP53 普通回退→WP39/42。阻塞0，最小修复范围为空。此报告由独立affected角色对本owner接口作出，不代签旧owner、FULL、actual、G/C或canonical关闭。

冻结 reviewed SHA `8ddba850af71f24e7bd77a80b7605c456c31dc7a`，tree `c8af1998818447f0e8969bada0b23fc83dfd24fd`；FIX_BASE `1d06c45cc0a744fca181ac80ee573cc9ebb9b862`，tree `5c99f51ec4cc084bc1c2b081306f1b55370744df`。管理导航 `9ad5539f38544fef6037356018015fe418021514` 不替代正式前驱。

作者potential reader导航主要是WP52；完整diff另揭示WP51 Items异常和WP53双敌回退真实消耗B09的命令登记、参战者与普通善后接口。故独立判为affected并增加有界检查，不因B09正文不变直接NOT_AFFECTED。

WP40只调用AI接口、不定义其策略；非玩家物品资源在登记时从所属业主列表移除，效果/复检留执行。I06异常发生在choose_item_to_use返回和pbRegisterItem之前，无UseItem且无消费；正常报告返回后继续后续阶段。I07仅POTION完整扫描后才登记/移除一次，符合WP40§4.2且不从玩家背包或对方业主偷取。

WP39公开单敌＋允许覆盖才派发/通知，双敌进入普通核心。有效伙伴且无noPartner，两个敌允许组装玩家＋伙伴，原尺寸缺省触发double；B026夹具明确无残留single/noPartner。WP42§7.1普通伙伴善后治疗两队，单敌野生通知由公开包装另门，故SF35的双敌无该通知并不删除普通结束通知。大会预算/保留没有传入普通Battle。

WP51§3.3的新整数d仅AI近似，明确不逐步写HP、不替代真实残余顺序/终局预测；WP42全员/逐员阶段、决定检查和部分副作用保留。C正文撤退射击清理源定位仍保留真实反射外层0击拒换、普通换出阶段门，WP41接受合同未改。

WP38–42所有原／净正文和已接受BC/CM/ER等目录字节保持；本PASS限于以上新增caller结果交接及003锚点删除的保真，不重审旧20贡献或全批行为。

精确定位（下列均为冻结candidate；同路径before/after身份见result.json及共享元数据）：

- `deliverables/final-specification-set/combat-requirements/wp51-ai-action-selection-and-skill.md:106` — 普通主动道具资格
- `deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md:74` — I06
- `deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md:75` — I07
- `deliverables/final-specification-set/pokemon-rules/wp53-safari-and-bug-catching-contest.md:154` — 上游单候选前提
- `deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md:97` — ### 4.2
- `deliverables/final-specification-set/combat-requirements/wp39-battle-context-and-participants.md:49` — ### 3.1
- `deliverables/final-specification-set/combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md:195` — ### 7.1
- `deliverables/final-specification-set/combat-requirements/wp51-ai-action-selection-and-skill.md:76` — 估计净损失 d
- `deliverables/final-specification-set/combat-requirements/wp52-c-items-calling-and-control-evaluation.md:142` — 撤退射击：

当前已接受依据：`review/remediation/20261003-prepare/batches/B15/acceptance-stage-1/completion-statistics-successor.json`，FIX_BASE精确blob `de8ab48ab51fa98a799fa5eb69c656e65ca99dd6`；本owner相关历史receipt以[result.json](result.json)中的精确candidate/actual/report绑定为准。仅复用已接受且当前保留的条款身份，没有递归历史读取或执行历史review程序；历史PASS不替代本轮有界判定。

共享身份/完整diff/11正式+5获准原稿/原控制/目录旧行核验只做一次，见[B02共享索引](../B02/README.md)。全部静态设计为未执行；保留U01–U10、G01–G12、AX01–AX20与条件性67树果、非局部贡献。Data/Scripts.rxdata/全部二进制和序列化数据、exe/DLL、mkxp.json、实际地图事件、媒体/字体/声库/宿主/容量、8杯赛名单及pokemon_metrics.txt样本、备份/生成目录、真实插件组合/动态分派/弃用别名/EventScene/动态阴影及真实Demo链仍未读/未证。参考/游戏/Ruby/编译/转换/生成/反序列化/行为模拟/历史作者或reviewer程序执行、行为向量执行、运行观察、已证Demo链均为0。

请求gpt-6.1-sol ultra/Standard（service_tier=default）。admission为当前委派任务已运行、无可信参数回显；effective四项均UNVERIFIED，依获准Plan A继续，缺回显本身非阻塞，未发现明确不支持/降级证据；未作额度/凭据探测，未启动额外任务。详见[配置记录](../B02/configuration.json)。

报告提交SHA在最终交付外部给出。本candidate判定不批准任何actual整合；actual需其精确双diff与独立必要门。
