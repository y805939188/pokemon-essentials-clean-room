# 实现侧：已接收的5.3参数规格补充

本补充已技术接受，内容固定 `6af2f193a5852e12ee6e17152d382efdbccdb40e`；接收记录与五文件真实SHA-256见同目录ACCEPTANCE.json。只读本净化交接、五份规格/目录及已净化表/向量即可，不打开来源元数据中的Ruby定位，也无需原版源码快照。

## 可执行的合同输入（不是测试通过声明）

- 30个逻辑integer方法全部PBS u；0/1/01分别为0/1/1，-1/+1/1.0/1e2/1x拒绝；精确逐方法绑定见WP31 §3.9与上级inputs中的METHOD-BINDINGS.csv。
- 本期采用参考R两拼写Evolution/Evolutions；有参方法缺值在当前条目登记前拒绝，非空非法数字在全表整数转换拒绝。不复制发行v21.1显式形态缺参漏洞；发行事实仍单列。
- 不新增level≤上限、count≥1、Beauty≤255或Location/Region目录存在门。运行不匹配与编译拒绝不同；要害记录缺席与已知计数0不同；EventAfterDamageTaken参数为事件编号，战后伤害阈值仍固定49。
- 参考u没有JS安全整数上限。另行采用DEVIATION-PBS-INT-01：实施表示域0..9007199254740991；超域明确unsupported-integer-representation/零新产物，不舍入或钳制，不冒称参考拒绝。先核u词法，再精确核值域；前导零按值处理，不因位数另设门。不得先Number化舍入大整数，也不删作者输入或旧缓存。
- 原2880向量是参考静态期望；框架缩域期望另列，不能把参考大整数接受行改成拒绝，或把NOT_EXECUTED改写实测。

## 五份已接收正文/向量目录

仓库相对路径（均在deliverables/final-specification-set下）：
1. pokemon-rules/wp31-basic-evolution.md
2. generic-kernel/wp03-content-identity-and-schema.md
3. generic-kernel/wp04-pbs-lifecycle.md
4. test-catalog/pokemon-rules-wp31-32-37-38.md
5. test-catalog/generic-kernel-wp02-03-04.md

当前从整改分支/worktree读取本补充；clean-room main尚未合入。全部行为NOT_EXECUTED，技术资料门可用不替代B方案/共享合同/实现测试/独立代码复审等门，也不是产品验收PASS。远端同步结果另由发布回执说明。
