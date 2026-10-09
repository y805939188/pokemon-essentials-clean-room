接手 B11 有界作者整改（A-B11）。配置必须请求 gpt-6.1-sol / xhigh / default(Standard)，保存 requested/admission/effective；依批准 Plan A，缺后端回显记 UNVERIFIED，不做额度/回参审计；明确不支持或降级立即报告父任务，不用CLI/native替代。全局活跃任务上限3；不要派生任务。作者不能作为独立复审。

仓库 y805939188/pokemon-essentials-clean-room，origin https://github.com/y805939188/pokemon-essentials-clean-room.git。工作分支建议 codex/cloud-dot-B11-author-1-20261009；从精确正式接受基线 0cfe99094b76f8d75fded0d638694677855a5f0c 开始隔离工作树。父任务另提供本派发资料发布SHA，仅管理文件，不改变正式输入；通过 git show 读取本包，不把 dispatch 提交误当 FIX_BASE。

先读 AGENTS.md、handoff/cloud-dot-20261009/original-contract.md 和本包 review/remediation/20261003-prepare/batches/B11/refreeze-after-B10-C-1/B11-downstream-contract.json，以及 original-and-acceptance-controls.json 中完整6原finding/PLAN验收对象（3项主责）。35计划读 / 8正式写边界以冻结清单为准：两份全局原报告输入从 93e10babe0b9c9ef8b3f5277754541b447beeeb4 静态取，其余从 0cfe99094b76f8d75fded0d638694677855a5f0c 取。焦点：幽灵诅咒动态目标与重定向、148特性/196持物身份统计、阶段/消费顺序；缺陷与统计分别登记。 不把焦点替代完整 qualified 控制、反例、反向对照和扩展/二审限制。

参考源码只可在 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b 静态只读，禁止运行参考/游戏/Ruby/编译/转换/生成/反序列化/行为模拟器和历史作者review程序。新Git/JSON/hash/文本元数据脚本可以；运行观察/静态向量执行/demo已证均为0。保留U01–U10/G01–G12/AX01–AX20及具名未证项。

修订批准集合内与本批finding关联的原净化正文/覆盖/测试行，保持正确条款、兼容字面/ID/数量口径，保护整测试目录里其它WP原行、顺序和重复性；不能删问题声明/内容来消失问题。原spec暂只读：确实是原提取错误，先在自己 author-draft-1 交逐ID/path/clause/前身份/完整patch/后身份的有界同步方案，父协调记录具体scope amendment后才应用；正确原稿不动，B10旧原稿许可不继承。无需重新问用户阶段许可。

B11与B15计划读写和贡献ID交集为0，各自仅本地WP贡献；共享外部状态保持冻结已接受语义。发现需要修改另一个作者读入语义、新路径或未知共同前提，先定点报告协调，继续不受影响部分；依赖不明不能假定独立。公共台账、index、导航、覆盖、全局状态由唯一A-REG串行写，作者只提供逐ID建议。受影响接口见 affected-interface-map.json：精确判断 clause/caller/data/condition，作者结论不代独立评估；实际影响须独立Ultra candidate+actual，未影响须有准确独立依据；不扩成所有旧批次重审。

交付可审查的 bounded candidate：完整每ID证据/修订/前提/最小反例和邻近反向静态设计/验收及限制；输入/输出完整身份、未过滤diff、保护owner行证据、原稿同步授权与实际应用（如有）、登记建议和独立复审请求。冻结完整候选SHA、普通commit/push并读回远端ref/FETCH_HEAD/tree/改动文件；不force、不main、不改参考/历史交接。记录可恢复的新增/受影响阅读，不需要一个读者重读全部历史、反复证明读取或恢复旧证明树。

完成后返回候选SHA/branch/资料路径/对每项局部控制实际产出及未解阻塞；不能把作者自检、候选通过、实际通过、正式接受或canonical最终关闭混称完成。独立 reviewer 后续由父任务以gpt-6.1-sol/ultra/default另派。有限结束条件是候选与可复审证据全部交付，发现实质缺口明确解决动作。
