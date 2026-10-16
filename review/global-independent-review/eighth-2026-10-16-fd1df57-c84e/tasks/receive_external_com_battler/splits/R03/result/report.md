# 第八轮 Battler 接收组4：R03

状态：FINITE_COMPARISON_COMPLETE_PARENT_FINAL_OPEN；UPDATE_NOT_STARTED。本片完整处理 5 个原消费者事实及必要定义/生产端/当前正式条款；最终中央接口签收仍为0，不能据此宣布父任务或B8全局PASS。

固定报告合同 02c8206651676effe40ff9a33dbb70998b79c1b1；继承合同40f45ddd；目标5cf9503a99a855c06a8ac9c932e6778b57e71049（tree1f7faa21b90bce1e7d89623407dd90133f260eb2，任务tree34bf2e1922a7cc2f4742df0fe09ea0b3b7ff1355）；B8 fd1df570cad987dc3852a3b958f03916e317f7fe，R 8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。只有本组四个result为写集。10件目标原字节、共2,576,539 bytes全取回核SHA256/blob，复用在H01/result/recovered/；它们不授全文语义信用。

## 有限实读结论

| 事实 | 已核完整意义与限定 |
| --- | --- |
| RX-POKEMON-SET | 持久HP钳[0,totalhp]，归0请求heal_status但其蛋守卫保留蛋异常/计数，ready_to_evolve仍清。status setter先拒不可用，再解析并写规范身份。Battler先写本地HP/状态/等级，再调用持久接收者。 等级越界可在本地已改后由持久入口报错；HP持久钳制不回读改写Battler局部值。未知持久物品输入被忽略，Battler解析为空后写穿清除，二者不同。 形态提交先写形态、清能力值缓存，再handler、重算与条件图鉴登记；不清能力索引或forced_form。calc_stats按HP上限差调整且正路径最少1，写穿持久HP；动态form读取在非战斗/非仓库且无forced值时可先提交。 |
| RX-POKEMON-PP | 持久Move.pp=钳到0/总PP，总PP=基础PP+整数(基础PP×ppup/5)；修改id或ppup后再钳当前PP，ppup本身不夹限。 Battle Move独立复制当前PP并持真实Move引用；pbSetPP先写包装PP，仅真实关联存在、同id且非Transform才写持久PP。直接包装字段不触发同步，Transform新招PP/总PP5不写回原持久槽。 |
| RX-SHADOW-HP | 后加载hp=别名先调用普通持久HP入口，再在最终HP≤0时清hyper_mode；它叠加普通HP蛋例外与进化准备清理，不能推整Shadow生命周期已接。 |
| RX-SHADOW-BATTLER | 初始化覆盖先查旧pokemonIndex>0且旧副本有效Hyper才清旧持久标志，然后基础绑定；新Shadow仅在SHADOW类型已注册时改场上类型，玩家拥有才减入场心量表。 Hyper进入要求存活、Shadow、当前非有效Hyper、玩家拥有；battle.pbRandom使用heart_gauge并以≤max/4判定。有效Hyper读取另受heart_gauge0或HP0遮蔽，不等于存储标志自动清除。 服从门对非Hyper/空招/SHADOW类型放行，其余用裸rand(100)<20；外层普通服从资格仍适用，不把20%套所有战斗。 |
| RX-PEER | 默认构造使用普通Peer，NullPeer是独立未用替身。普通Peer开始/入场/离场有不同MultipleForms参数与后置，不能统一为空操作。 离场先拒缺Pokemon，询问带usedInBattle/endBattle参数的形态；非空且不同才提交，再钳超过上限HP并调用后继形态处理。Mega/Primal显式撤销在濒死等实际caller，不能归给所有Peer调用。 正常终局遍历玩家侧参与集合并按当前位置读取参战/还原记录；实际换下、濒死、终局和捕获不等同同一清理或保证。 |

每项完整原对象、前提、正常对照、取消/失败/部分提交、源与正式定位在reception-ledger.json；实际来源范围在reading-ledger.json。强制八事实伴件与31个完整必要单元全部读完并按固定源比较；未执行任何行为向量。没有新required/optional；既有STALL/TRUANT问题只有限佐证GR8-COM-001，不重复计数。

## 真实剩余与交接

本片不是810个producer子断言或160个反向条款的主责。H01累计签收需原接收者把本组24有限定义与P01A..P10各完整producer/条款贡献逐项接合，四接口及有限历史资格按原owner保留。这里不把可得未读正文叫宿主limit，也不借24事实比较关闭整个810/160。两有限NO_REQUIRED不需新建canonical；全历史无重复或重开资格仍未作。

指定/workspace执行环境启动失败；本次使用GitHub连接读取固定对象与JavaScript字节校验，通过Git Data API发布。没有本地bare、磁盘工作树、shell命令或git push日志，不能声称隔离bare验证完成。API完整远端增量回读由后继publication绑定。宿主画面/音频/真实存档未执行。实际model/effort/tier/speed/Fast/opaque UUID逐项UNVERIFIED，source_thread_id不是自身UUID；由父最终绑定实际身份。本组不spawn、不改正式/R/旧原对象、不合main、不强推，全部行为执行0。
