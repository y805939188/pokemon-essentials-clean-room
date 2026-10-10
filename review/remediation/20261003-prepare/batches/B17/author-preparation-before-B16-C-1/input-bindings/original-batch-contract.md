# B17：战斗与生命周期UI、设施作者入口

计划状态：PLANNED；未执行、未修订、未关闭。WP：WP67-A, WP67-B, WP76。
作者任务1（A-B17，gpt-6.1-sol Max Standard）；独立复审任务1（R-B17，Ultra Standard）。同一复审任务还须核实际 integration 的受影响范围。

上游：B09, B10, B13, B16。下游：B19, B20, B21。

BACK调用层、无石Mega、NearAlly三席存活/邻接差异、末帧取消、直接调试辅助失败；正常入口与直接入口分列。

规范ID主责任（唯一责任，不代表允许提前关闭）：

GIR-FD82-005, GIR-FD82-A059, GIR-FD82-B031, GIR-FD82-B032, GIR-FD82-B033, GIR-FD82-B034, GIR-FD82-C119

本批全部贡献ID（主责任与协作均保留原编号）：

GIR-FD82-003, GIR-FD82-005, GIR-FD82-A040, GIR-FD82-A050, GIR-FD82-A059, GIR-FD82-B031, GIR-FD82-B032, GIR-FD82-B033, GIR-FD82-B034, GIR-FD82-C003, GIR-FD82-C119, GIR-FD82-D018

拟修改文件边界（只改finding关联条款/本WP测试行；同文件其他批次行保持）：

- `deliverables/final-specification-set/demo-dx/wp76-facility-content-generation-and-simulation.md`
- `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md`
- `deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md`
- `deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md`
- `deliverables/final-specification-set/user-interface/wp67-b-lifecycle-presentations-and-history.md`

各项验收必须同时读取 [finding-acceptance.json](../finding-acceptance.json) 对应对象和原 findings 完整对象。前提、最小反例、最低修订、确定复核、current_qualifications、effective_case_constraints、二审和扩展裁决均按原文继承；本段焦点不能替代它们。

公共登记由 A-REG 在 G/C 阶段应用，其他作者仅交逐ID建议。原 specs、AGENTS、冻结 review 和参考只读；错误历史记录由新目录后继勘误解释。

实际可写集合以 batches.json 为准；全部读路径在同一对象。physical-conflicts.tsv 按整文件加锁，semantic-dependencies.tsv 按语义依赖排序；上游变化使旧下游输入失效，须重冻结并按影响复审。

交付：冻结候选SHA/父SHA、精确差异、原ID→条款→附表→测试→新登记建议、静态前后状态与邻近反向对照、未触及范围。候选复审和integration核验均成功后仅登记本批贡献；跨域ID须全部贡献完成且经最终Ultra再由A-REG关闭。
