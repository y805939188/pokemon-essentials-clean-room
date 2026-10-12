# R4-U03 actual：当前世界/UI等待与公共audit限定核对

**ACTUAL_PASS_SCOPED**；无本范围必修问题。此范围另签新UI消费关系，不继承U02旧消费者的整文件签名。

## A-WORLD-01

前提：固定R，无插件；合法地图场景、未淡出、正常消息循环确实到达地图微更新；surfing=true，临时基点非空；失败上水未启动运动且无额外合格步通知/其它字段写入。

结果：消息等待/长词暂停/冷或显式皮肤读取没有独立清临时基点/结束标记写入；缺少合格通知时原基点可保留，显示输入仍取基点。不能仅由UI更新或一次消息正常返回推断临时状态已清。

证据：WP17 L78–88/243–246；WP12 L187–189；WP59 L296；WP16 L130；R Messages L18–20/631–652、Scene_Map L121–133、FieldMoves L705–751、SurfBase L44–79。

## A-WORLD-02

前提：独立正常合法运动完成对照；有Scene_Map、通知event为Game_Player、临时基点非空；分别给定ending_surf=false/true。不声称真实输入或默认Demo可达。

结果：合格完成通知可清基点；只有ending_surf=true才额外取消载具/重置遭遇/恢复BGM/清结束标记。NPC通知、无基点或非地图任一不合格时不清；不把所有UI等待都称永远保留或必清。

证据：WP12 L188–189；WP59 L296；WP61 L37；R Character L970–983、FieldMoves L738–751。

## A-WORLD-03

前提：两场景独立：正常事件解释器更新且ending_surf=true；另已合法到达或直接调用数字UI的初值1一位无符号夹具。

结果：解释器的ending_surf守卫早于命令执行，人工真值不能证明正常101/103或201可达。数字窗口同轮UP+USE+BACK确认2、仅BACK返回初值1只判已进入合法交互的消费；不保证所有等待状态都能到达该窗口。地图micro不等同normal update：前者没有直接pbMapInterpreter.update调用。

证据：WP12 L189；WP59 L296；WP17 L238–246；R Interpreter L104–132、Scene_Map L121–133/165–175；事件默认取消专项input-skin。

## A-WORLD-04

前提：合法临时会话与放电低电量；独立frame handler被调度对照，message_window_showing=true/false；假时其它menu/battle/route/interpreter门也假，且warned_low_battery=false。

结果：消息窗真时门阻止，不置警告状态；全门通过则先置warned=true再请求消息，当前会话不由新文本排版/暂停重复请求。只签handler发生时的门，不说每次micro必调frame handler，不推宿主时机/电池实际读数。

证据：WP61 L36/46；WP17 L238–251；R Messages L391–399、Overworld L47–54。

## A-AUDIT-01

前提：作者公共提案audit mirror为“如需”；当前audit完整bytes等于B；旧条目显式列各冻结输入身份、历史审查与无运行限制；新来源读ledger/author/两候选报告在本actual中完整保留。

结果：NO_SHARED_EDIT_REQUIRED：旧来源索引不是新actual整文件或UI签名。本独立报告绑定新actual/来源/有限新消费者并保留原未证限制；没有具体行为矛盾要求改公共audit，额外镜像会是非必要行政返工。

证据：audit L313–325/1236–1249/1340–1352/1460–1474；author/shared-file-proposals.md；identity-integration frozen51；本read-ledger。

新增行为执行0 / NOT_EXECUTED_THIS_UPDATE；旧四次历史归属单列保持。所有条件案例是静态推导；完整场景运行、真实字体/资源/像素、物理输入、Demo及插件未知。本批无接受/关闭登记，U04/U05/U06门保持。
