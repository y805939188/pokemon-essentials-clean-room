# B12 affected candidate-1：B08

结论：**PASS_SCOPED**。范围：WP36 双遭遇优先序／WP37 公开覆盖／WP53 大会接管。阻塞0，最小修复范围为空。此报告由独立affected角色对本owner接口作出，不代签旧owner、FULL、actual、G/C或canonical关闭。

冻结 reviewed SHA `8ddba850af71f24e7bd77a80b7605c456c31dc7a`，tree `c8af1998818447f0e8969bada0b23fc83dfd24fd`；FIX_BASE `1d06c45cc0a744fca181ac80ee573cc9ebb9b862`，tree `5c99f51ec4cc084bc1c2b081306f1b55370744df`。管理导航 `9ad5539f38544fef6037356018015fe418021514` 不替代正式前驱。

WP53原／净§6.1及SF35新增上游基数门和伙伴回退，是对B08已接受WP36/37的真实caller接口修订。WP36/37正文与旧EN/RM相关目录字节保持。

精确静态链：Bug开始只缩玩家队伍为选员且不清伙伴；普通步进触发/允许通过→force-single假、非Safari时伙伴真早于一员假→第二候选→公开包装两个敌不派发覆盖→普通核心准备玩家＋伙伴并在无single/noPartner的夹具下双打。不是从大会直接入口倒推公开链必接管。

普通双敌正常胜利夹具不构造大会战斗，无大会Ball菜单、预算传入/回写或保留K覆写，Sport预算20/K保持；普通伙伴善后治疗两队，公开双敌不发单敌野生结束通知。无伙伴或前置force-single真时只得单敌；允许覆盖且handled空、有效会话、无更早接管才入大会，其自身预算初始化/消费/保留/通知规则保持。单敌但can_override假不派发覆盖。

正反对照固定合法选员、可参战伙伴、普通Natural Park BugContest表、无雷达/漫游、无残留single/noPartner、正常返回前未到期。缩队不保证接管；Safari拒绝仍早于伙伴。实际Demo是否设置此组合保持U01，未声称运行覆盖。五原稿获准补丁只证明范围与字节，条款质量由这次静态链独立核对。

精确定位（下列均为冻结candidate；同路径before/after身份见result.json及共享元数据）：

- `deliverables/final-specification-set/creature-rpg/wp36-wild-encounters-and-modifiers.md:147` — ### 4.4
- `deliverables/final-specification-set/creature-rpg/wp36-wild-encounters-and-modifiers.md:151` — ### 4.5
- `deliverables/final-specification-set/pokemon-rules/wp37-roaming-and-poke-radar.md:113` — **战斗结束钩子**
- `deliverables/final-specification-set/pokemon-rules/wp53-safari-and-bug-catching-contest.md:116` — ### 5.1
- `deliverables/final-specification-set/pokemon-rules/wp53-safari-and-bug-catching-contest.md:151` — ### 6.1
- `deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md:43` — SF35
- `specs/pokemon-rules/wp53-safari-and-bug-catching-contest.md:173` — ### 6.1

当前已接受依据：`review/remediation/20261003-prepare/batches/B15/acceptance-stage-1/completion-statistics-successor.json`，FIX_BASE精确blob `de8ab48ab51fa98a799fa5eb69c656e65ca99dd6`；本owner相关历史receipt以[result.json](result.json)中的精确candidate/actual/report绑定为准。仅复用已接受且当前保留的条款身份，没有递归历史读取或执行历史review程序；历史PASS不替代本轮有界判定。

共享身份/完整diff/11正式+5获准原稿/原控制/目录旧行核验只做一次，见[B02共享索引](../B02/README.md)。全部静态设计为未执行；保留U01–U10、G01–G12、AX01–AX20与条件性67树果、非局部贡献。Data/Scripts.rxdata/全部二进制和序列化数据、exe/DLL、mkxp.json、实际地图事件、媒体/字体/声库/宿主/容量、8杯赛名单及pokemon_metrics.txt样本、备份/生成目录、真实插件组合/动态分派/弃用别名/EventScene/动态阴影及真实Demo链仍未读/未证。参考/游戏/Ruby/编译/转换/生成/反序列化/行为模拟/历史作者或reviewer程序执行、行为向量执行、运行观察、已证Demo链均为0。

请求gpt-6.1-sol ultra/Standard（service_tier=default）。admission为当前委派任务已运行、无可信参数回显；effective四项均UNVERIFIED，依获准Plan A继续，缺回显本身非阻塞，未发现明确不支持/降级证据；未作额度/凭据探测，未启动额外任务。详见[配置记录](../B02/configuration.json)。

报告提交SHA在最终交付外部给出。本candidate判定不批准任何actual整合；actual需其精确双diff与独立必要门。
