# R4-U02 完整冻结finding任务正文

### GR4-M03-001 · P2 · REQUIRED — 范围随机移动只承接了路线让出时机，未承接原始位置边界与单轴规则

领域 M03；分类 缺能力；独立审者 thread `01a12fc9-af72-7402-a6d1-0e3abf8b16e8`；辅助证据目录 `modules/M03/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/004_Game classes/006_Game_Character.rb` · 669–700：范围随机选择有负/零/正三态、原始锚点及UD/LR变体。（固定R；blob `9de49c288ec6c5d8c962b14f1b959ad90ae3d662`）
- `Data/Scripts/004_Game classes/006_Game_Character.rb` · 376–385,539–548,553–565：落位不改原始锚点；脚本调用后按字面让出；选向后普通移动可受阻。（固定R；blob `9de49c288ec6c5d8c962b14f1b959ad90ae3d662`）
- `Data/Scripts/004_Game classes/007_Game_Event.rb` · 9–18：事件原始锚点取地图事件数据。（固定R；blob `aca6d0992927e1d6ce37f08c2cb75e73ebcb7374`）

**现规格依据**

- `deliverables/final-specification-set/engine-overworld/wp12-terrain-movement-vehicles.md` · §4.3 L146–148：只有四正向随机、接近/远离和自主策略。（固定B；blob `177f675ec04ae3d5124dfec69693845e3c0162cc`）
- `deliverables/final-specification-set/engine-overworld/wp13-move-route-matrix.md` · §1 L18；§2 9/45行：只定义三前缀调度，没有两个范围输入的行为。（固定B；blob `b79888af1ce084dc0441b0688661b5c4511f029c`）
- `deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md` · MR08、MR10–15、MR18–21：只测试求值/前缀/推进。（固定B；blob `18382cf43e137a671b245a1dd8d836694e6754ee`）
- `deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md` · L235：跨域命中也只承接同一前缀语义。（固定B；blob `f87c6edf5b09c2ee43b51a514bb7ef81e55e4062`）

**参考实际行为**

以事件建立时的原始位置作锚点。每轴负范围允许该轴两方向，零禁该轴，正范围依当前位置相对原始边界筛方向。对候选等概率只抽一次并尝试普通移动；碰撞不重抽。无候选直接返回。两个单轴变体禁用另一轴；之后移位不自动重定锚点。 对正横界r，左当x>x0−r、右当x<x0+r；对正纵界s，下当y<y0+s、上当y>y0−s。固定参考候选序是左、右、下、上，保留满足门的方向后仅作一次均匀索引选择；此序用于解释固定参考抽样，不规定未来容器或跨语言随机序列。方向选择不预转向，移动成功后的转向沿WP12。

**现规格的说法**

已明确普通四向随机和三种脚本文本前缀的同帧/下帧区别；没有说明这些辅助实际如何限制移动范围。

**差异/缺口**

兼容字面被保留，但实现者仍不能从正式行为合同决定其方向候选、锚点与零/负值语义。

**必要前提**

- 1×1普通地图事件，原始锚点(5,5)，当前(7,5)，无方向固定/强制外部写入；地图内普通地面、所有方向通行。
- 执行范围随机能力，横范围2、纵范围0；固定R无额外覆写。

**最小反例**

```json
{
  "input": "上述状态调用一次范围随机移动。",
  "reference": "唯一候选为左，尝试到(6,5)；右移到(8,5)不会被选。",
  "formal_gap": "四向等概率规则会容许向右/纵移；三前缀条款只能决定何时让出，无法排除这些错误结果。",
  "evidence": "DERIVED_VECTOR; NOT_EXECUTED"
}
```

**正常对照**

从原始(5,5)且当前位置同点，横2/纵0，两横向候选各半；普通通过后位移一格。

**失败/边界对照**

横纵0：没有随机抽取/移动；横2纵0位于右界且左格阻挡：只尝试左、不重抽其它方向；负横范围为不限制该轴。另给事件被落位到范围外的输入，锚点仍原值，不承诺自动钳回。

**独立实现影响**

会把受限游走实现成四向漫游、以当前位置不断重定边界，或受阻后重抽；改变NPC活动范围和随机消费。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-evidence.json",
    "key": "GR4-M03-001",
    "scope_file_count": 131,
    "context_results": [
      "全部131文件按原标识和中文范围/随机/单轴/原始位置别名搜索。",
      "相关命中仅WP13路线§1、MR08/10–15/18–21、WP75 L235；逐读均是调度/求值合同。WP12§4.3普通随机并不定义有界族。",
      "原始位置的其它命中属玩家元数据/储存位置，随机漫游命中属游走宝可梦等别域，不补本规则。",
      "源端仅此一组定义，原始坐标赋值见角色初始化及事件初始化；未定位默认Demo调用，调用能力可由路线45到达。"
    ],
    "source_followup": "固定R所有脚本检索定义、同名覆写及所涉状态读写；追踪下述source anchors的实际入口/消费者；不把缺Demo当不存在。"
  },
  "primary_relative_paths_base": "modules/M03",
  "independent_counterevidence": {
    "search_ids": [
      "M03-range",
      "M03-definitions"
    ],
    "words": [
      "move_random|范围.{0,10}(随机|移动)|随机.{0,15}(范围|单轴|边界)|原始.{0,10}(位置|坐标)|左.{0,5}右.{0,5}下.{0,5}上"
    ],
    "scope": {
      "baseline": "1f36475d22120a0d1175967d5b17d71fe8311d88",
      "root": "deliverables/final-specification-set/",
      "files": 131,
      "includes": "正文、共享条款、数据附表及静态测试目录；并非131篇逐篇重新验收"
    },
    "source_countersearch": [
      {
        "id": "M03-definitions",
        "pattern": "move_random_range|move_random_UD|move_random_LR|original_x|original_y|surf_base_coords|ending_surf|def command_116|def pbEraseThisEvent|def addErasedEvent|def pbCancelVehicles|def transfer_player",
        "files": 312
      }
    ],
    "contexts_read_and_assessed": [
      "WP12 §4.3已给普通随机不预转向/成功后转向",
      "路线§1/45、MR08/10–22、WP75 §8.6均只给脚本文本调度；不是范围候选算法"
    ],
    "conclusion": "候选过滤/原始锚点/单轴能力未承接；阻挡时不预转向和通用移动应引用现有合同，不另计缺失。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CA"
}
```

**下一轮最小修订**

在WP12或WP13正文补实现无关的范围随机规则，路线矩阵引用该合同；加边界/空候选/受阻/落位后锚点对照。不得把源方法或类结构当未来API。

**验收标准**

```json
[
  "静态：分别列横纵负/零/正语义、原始锚点生命周期、候选等概率及一次尝试不重抽。",
  "静态：区分UD/LR单轴与普通四向；保留既有前缀调度，不把移动成败当推进门。",
  "静态向量：原始(5,5)/当前(7,5)/横2纵0、双0、左阻挡、当前位置移出原范围；均标NOT_EXECUTED。",
  "运行：本修订不以宿主执行为前置；将来动态验证需要合法地图夹具与真实随机控制，不能以文档/JSON校验充数。",
  {
    "kind": "SPEC_STATIC",
    "criterion": "写出严格比较式和固定参考候选序，并区分方向过滤/越界钳回；受阻不重抽、不预转向的行为引用已有WP12合同。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/engine-overworld/wp12-terrain-movement-vehicles.md
- deliverables/final-specification-set/engine-overworld/wp13-move-route-matrix.md
- deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md
- deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md

**共享合同**

- WP11地图状态/转移
- WP12运动与通行
- WP13事件/路线及测试目录

**依赖**

- 有效地图/事件夹具
- 固定参考默认定义，无插件覆写
- 普通调用和指定更新机会

**能力范围引用**

- GR4-CAP-M03-011
- GR4-CAP-M03-012

**关联新问题**

无。

**根因身份**

GR4-M03-001

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "third_round": null,
  "second_round": null,
  "note": "未知第二轮关联不猜ID；旧CLOSED身份不修改。",
  "independent_scope_assessment": {
    "relation": "new_bounded_scope",
    "assessment": "本项在固定B/R独立成立；未把原模块历史PASS当证据，未重开旧关闭项，未扩审229。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- DERIVED_VECTOR

**执行状态**

NOT_EXECUTED

**置信限定**

HIGH_STATIC_WITH_STATED_PRECONDITIONS

**未知**

- 实际Demo使用/事件可达性未知；宿主和媒体结果未执行。
- 默认Demo调用未证；源路线45可调用不等于真实NPC素材/事件链已运行；任意非整数/非法范围未穷尽。

**排除的主张**

- 不要求修参考、不实现框架或保留源API/结构。
- 不宣称全部本域或全套规格均已审。

**用户政策边界**

无需决定是否补事实；若未来实现选择不同兼容政策，应另阶段明确，不由本审者代定。

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CA",
    "thread_id": "01a1301e-5efe-77a2-9450-fc09ff6830c1",
    "path": "modules/CA/verdicts.json",
    "pointer": "/records/5",
    "decision": "CONFIRM_WITH_REFINEMENT",
    "reason": "ROOT候选序及严格比较经原函数独立核对正确。源选向后调用普通不预转向移动，受阻不重抽；原始锚点独立于当前位置。既有路线前缀只决定让出，不足以决定范围边界。",
    "required_refinements": [
      "补一般比较式、负/零/正三态、UD/LR禁用另一轴；说明是方向过滤而非越界自动钳回。",
      "候选序只用于固定参考抽样索引解释，不要求未来保留源容器结构或跨语言随机序列。",
      "将不预转向/成功转向引用WP12既有规则，不新增重复根因；WP75的正确调度无需重写。"
    ],
    "execution_evidence_assessment": {
      "ca_rerun": false,
      "receipt": "../M03/execution.json",
      "kind": "SOURCE_STATIC / SPEC_STATIC / DERIVED_VECTOR",
      "assessment": "原模块记录的Python清点/JSON/路径校验仅为TOOL_VALIDATION，不支持行为运行通过；CA未执行该脚本或参考函数。",
      "host_or_demo": "NOT_EXECUTED"
    },
    "historical_relation_assessment": {
      "relation": "new_bounded_scope",
      "assessment": "本项在固定B/R独立成立；未把原模块历史PASS当证据，未重开旧关闭项，未扩审229。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M03-002 · P2 · REQUIRED — WP59声称转移重置冲浪临时残留，但转移链没有该清理

领域 M03；分类 状态或时序错误；独立审者 thread `01a12fc9-af72-7402-a6d1-0e3abf8b16e8`；辅助证据目录 `modules/M03/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb` · 705–751：上水先写底座后前跳；清理位于有底座的玩家步后通知。（固定R；blob `841e0c66cce7bbb34c07d4991f952d31a27cc469`）
- `Data/Scripts/004_Game classes/006_Game_Character.rb` · 767–799：跳跃落点拒绝不启动运动，前跳返回false。（固定R；blob `9de49c288ec6c5d8c962b14f1b959ad90ae3d662`）
- `Data/Scripts/003_Game processing/002_Scene_Map.rb` · 72–101,121–133,165–175：转移及正常201消费者；没有两个临时字段写入。（固定R；blob `8be1640f36b293f44329a3bbe6ccf3e13fb0d825`）
- `Data/Scripts/004_Game classes/008_Game_Player.rb` · 64–100,262–266,575–592：实际覆写/载具更新也不清底座或结束标志。（固定R；blob `8f49870b94fdda6dbb53cbaeebfaf458498cd02d`）
- `Data/Scripts/005_Sprites/005_Sprite_SurfBase.rb` · 44–79：保游泳且底座非空时，显示输入仍取底座。（固定R；blob `323f35ce4438cd140f34bb669c0bb8cf91a80858`）
- `Data/Scripts/003_Game processing/003_Interpreter.rb` · 116–123：结束冲浪标志另为解释器等待门。（固定R；blob `21666002e7f4038dd3763b632538becaae5f8d7d`）

**现规格依据**

- `deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md` · §7 L296：明确写中断（如转移）时残留按转移流程重置。（固定B；blob `a2bda5c3e0d5b967d8ef050bc36b4cac8ed8c420`）
- `deliverables/final-specification-set/engine-overworld/wp12-terrain-movement-vehicles.md` · §5.2 L169–171：上水失败无回滚、步后清理三门已有准确限定。（固定B；blob `177f675ec04ae3d5124dfec69693845e3c0162cc`）
- `deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md` · §4 L59–71：列明取消载具/落位流程，无补充临时残留清理。（固定B；blob `7482ac4dc1bdf3720a3d6d5c5c1c8b2a38e12f0d`）
- `deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md` · MV05、WT19及MP显式传送族：没有失败上水后无步通知转移的对照。（固定B；blob `18382cf43e137a671b245a1dd8d836694e6754ee`）

**参考实际行为**

默认转移入口和载具取消都不清surf_base_coords/ending_surf；这些临时量不能由转移本身保证重置。清底座需地图场景、玩家通知、有底座；结束标志又要为真才清。无此通知前的转移返回可保留残留。

**现规格的说法**

WP59§7给了转移重置保证，同时WP12/WP61把清理正确绑定玩家步后通知；WP11被引用但无此重置。

**差异/缺口**

把后续有条件的收尾写成转移本身的无条件保证。

**必要前提**

- 合法20×20同图，玩家初始静止(5,5)、向右，无冰瀑/强制移动/跟随者；无其它字段改写。
- 直接上水入口前跳(6,5)因具名非through阻挡事件拒绝；相关资源调用正常，故surfing=true、底座(6,5)，未启动跳跃。
- 随后正常201转同图(10,10)、方向右，由场景按false保游泳；没有完成步或额外步后通知、无执行移动的其它事件/公共事件；所有宿主调用正常。
- 玩家through=false，无调试Ctrl穿透；ending_surf初始false。失败跳跃不启动运动计时，初始无未完成运动/步后通知。

**最小反例**

```json
{
  "input": "上述失败上水后的同图201保游泳传送，观察转移正常返回。",
  "reference": "玩家到(10,10)，surfing仍真，底座仍(6,5)；显示选择仍读旧底座，不自动跟玩家新位置。",
  "formal": "按WP59残留重置一句会预期底座已清、显示跟随玩家。",
  "evidence": "DERIVED_VECTOR; NOT_EXECUTED；只断言状态和显示输入，不声称可见像素"
}
```

**正常对照**

成功上水跳跃完成，满足玩家步后通知三门时清底座；成功上岸且结束标记真才额外取消载具/重置遭遇/音乐并清标记。

**失败/边界对照**

取消游泳参数true只清冲浪/潜水标志，未独立清临时底座/结束字段；后继合格步通知仍可能清理。人为ending_surf=true只用于直接转移与等待门的条件事实：正常事件201会先受解释器等待门阻止，不能用它证明该人工状态可越门，也不宣称默认流程必软锁。

**独立实现影响**

独立实现可能在每次传送额外清临时量，掩盖失败上水残留，并错误解除结束冲浪等待；状态与显示输入、继续时机可能与R不同。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-evidence.json",
    "key": "GR4-M03-002",
    "scope_file_count": 131,
    "context_results": [
      "全部131文件检索两个字段、底座/基点、残留/中断、载具取消/取消游泳。",
      "WP12§5.2和WP61§3.2只给步后门；WP11显式/边缘入口无临时量清理。测试MV05/WT19只正常收尾，不能证明转移重置。",
      "源端全脚本检索：底座清空只在field 743，结束标志清假为临时状态初始化与field 749；转移、玩家moveto覆写、载具类型设置、同图显示重建均未清。",
      "正常上岸后可能后续步后通知清理，所以反例明确无完成步通知；不把所有转移都说成一定永远残留。"
    ],
    "source_followup": "固定R所有脚本检索定义、同名覆写及所涉状态读写；追踪下述source anchors的实际入口/消费者；不把缺Demo当不存在。"
  },
  "primary_relative_paths_base": "modules/M03",
  "independent_counterevidence": {
    "search_ids": [
      "M03-surf",
      "M03-definitions",
      "CA-shared-alias-supplement",
      "CA-boundary-supplement"
    ],
    "words": [
      "surf_base_coords|ending_surf|冲浪.{0,20}(残留|中断|重置|收尾)|底座|基底|取消游泳|玩家步后",
      "过渡坐标|冲浪基点|冲浪.{0,8}清|动态形态查询|资源消费.{0,15}形态|形态.{0,15}副作用|计时.{0,10}变量|变量.{0,10}计时|PP.{0,20}(补给|补充|活体|存活)|翻译.{0,10}(重复|合并)|文本域.{0,10}(覆盖|冲突)"
    ],
    "scope": {
      "baseline": "1f36475d22120a0d1175967d5b17d71fe8311d88",
      "root": "deliverables/final-specification-set/",
      "files": 131,
      "includes": "正文、共享条款、数据附表及静态测试目录；并非131篇逐篇重新验收"
    },
    "source_countersearch": [
      {
        "id": "M03-definitions",
        "pattern": "move_random_range|move_random_UD|move_random_LR|original_x|original_y|surf_base_coords|ending_surf|def command_116|def pbEraseThisEvent|def addErasedEvent|def pbCancelVehicles|def transfer_player",
        "files": 312
      },
      {
        "id": "CA-boundary-supplement",
        "pattern": "def nil_or_empty\\?|def refresh\\b|def getFacingCoords|def pbGetSeason|on_leave_tile|def gsub!?|def to_s|def sprintf",
        "files": 312
      }
    ],
    "contexts_read_and_assessed": [
      "WP59 §7转移重置保证",
      "WP12 §5.2/ WP61 §3.2只保证玩家步后通知清理",
      "WP11同图转移、MP20/21与WP16 §4.3/B04-W07分别是车辆标记与显示消费，不提供临时坐标清理"
    ],
    "conclusion": "固定源字段写点没有转移独立清理；已有正确步后/显示合同不能使WP59的无条件转移重置句成立。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CA"
}
```

**下一轮最小修订**

将WP59保证更正为入口/消费者分层，明确传送不提供两临时量的独立清理保证；WP11/12引用统一；补失败上水→同图保游泳转移及正常步后清理对照。固定异常事实与未来是否主动清理的政策分开。

**验收标准**

```json
[
  "静态：分别说明surfing/diving、底座和结束标志，不把载具取消等同全部临时状态重置。",
  "静态：给出无步通知转移返回的观察点与后续步后门，不能声称永久卡死或默认Demo可达。",
  "静态向量：上述(5,5)失败跳→(10,10)转移保底座；对照成功完成步清底座；标NOT_EXECUTED。",
  "运行：真实可视位置/继续时机需宿主地图及资源；不要求本轮补造运行证据。",
  {
    "kind": "SPEC_STATIC",
    "criterion": "反例明确through=false、无Ctrl穿透、ending_surf=false、未启动运动计时；直接转移、正常201与步后清理分层。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/engine-overworld/wp59-world-time-weather-field-moves.md
- deliverables/final-specification-set/engine-overworld/wp12-terrain-movement-vehicles.md
- deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md
- deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md

**共享合同**

- WP11转移
- WP12冲浪提交/步后收尾
- WP61步后通知
- WP16/M10冲浪显示输入

**依赖**

- 有效地图/事件夹具
- 固定参考默认定义，无插件覆写
- 普通调用和指定更新机会

**能力范围引用**

- GR4-CAP-M03-002
- GR4-CAP-M03-003
- GR4-CAP-M03-007

**关联新问题**

无。

**根因身份**

GR4-M03-002

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "third_round": null,
  "second_round": null,
  "note": "未知第二轮关联不猜ID；旧CLOSED身份不修改。",
  "independent_scope_assessment": {
    "relation": "producer_cleanup_vs_existing_display_consumer",
    "ids": [
      "GIR-FD82-C064"
    ],
    "assessment": "已读旧qualified_scope及B WP16/B04-W07。C064的基点已清稳定冲浪/visible与opacity是显示消费者；新项质疑临时量何时清，不改旧显示合同，关系准确。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- DERIVED_VECTOR

**执行状态**

NOT_EXECUTED

**置信限定**

HIGH_STATIC_WITH_STATED_PRECONDITIONS

**未知**

- 实际Demo使用/事件可达性未知；宿主和媒体结果未执行。
- 完整宿主像素、真实Demo上水/转移链、外部脚本改写和所有转移组合未运行。

**排除的主张**

- 不要求修参考、不实现框架或保留源API/结构。
- 不宣称全部本域或全套规格均已审。

**用户政策边界**

无需决定是否补事实；若未来实现选择不同兼容政策，应另阶段明确，不由本审者代定。

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CA",
    "thread_id": "01a1301e-5efe-77a2-9450-fc09ff6830c1",
    "path": "modules/CA/verdicts.json",
    "pointer": "/records/6",
    "decision": "CONFIRM_WITH_REFINEMENT",
    "reason": "源码追至玩家jump覆写、普通更新、转移moveto、显示重建与步后通知，失败跳跃没有进入update_move，转移也不单独生成清理通知。WP59多给了一项保证；报告需保持有界条件与观察点，不能推广成默认软锁。",
    "required_refinements": [
      "将玩家through=false、无调试Ctrl穿透、ending_surf=false及未启动运动计时写成反例前提。",
      "区分正常201保游泳、直接默认转移取消游泳及步后通知清理；保留显示输入与真实像素未证的区别。",
      "人工ending_surf=true仅作直接转移/等待门的条件事实，不能称正常201可穿过该等待门。"
    ],
    "execution_evidence_assessment": {
      "ca_rerun": false,
      "receipt": "../M03/execution.json",
      "kind": "SOURCE_STATIC / SPEC_STATIC / DERIVED_VECTOR",
      "assessment": "原模块记录的Python清点/JSON/路径校验仅为TOOL_VALIDATION，不支持行为运行通过；CA未执行该脚本或参考函数。",
      "host_or_demo": "NOT_EXECUTED"
    },
    "historical_relation_assessment": {
      "relation": "producer_cleanup_vs_existing_display_consumer",
      "ids": [
        "GIR-FD82-C064"
      ],
      "assessment": "已读旧qualified_scope及B WP16/B04-W07。C064的基点已清稳定冲浪/visible与opacity是显示消费者；新项质疑临时量何时清，不改旧显示合同，关系准确。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M03-003 · P2 · REQUIRED — 事件命令116的消去记录写入及让出规则未承接，三入口对照含混

领域 M03；分类 实现信息不足；独立审者 thread `01a12fc9-af72-7402-a6d1-0e3abf8b16e8`；辅助证据目录 `modules/M03/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/003_Game processing/004_Interpreter_Commands.rb` · 11–35,502–509：分派116：正事件ID先安全消去再登记；即使缺实例仍登记；本条索引+1、false让出。（固定R；blob `58167231199f1cb8bdc499a61f5ada544d3f7616`）
- `Data/Scripts/004_Game classes/007_Game_Event.rb` · 46–49：普通erase只改实例/刷新。（固定R；blob `aca6d0992927e1d6ce37f08c2cb75e73ebcb7374`）
- `Data/Scripts/003_Game processing/003_Interpreter.rb` · 84–135,292–300：false中断本轮；记录式辅助另有事件存在门。（固定R；blob `21666002e7f4038dd3763b632538becaae5f8d7d`）
- `Data/Scripts/012_Overworld/002_Overworld_Metadata.rb` · 154–168：登记取当前地图，不检查实例存在。（固定R；blob `148211a6c6f94ed0219134f52dcfff817e6bd0fd`）

**现规格依据**

- `deliverables/final-specification-set/engine-overworld/wp13-interpreter-command-matrix.md` · 116行 L37：只描述当前事件被删除和刷新，没有控制结果/局部记录门。（固定B；blob `bfff8453529890f2ea6e7d00ed9b7e1033da0130`）
- `deliverables/final-specification-set/engine-overworld/wp13-map-events-npc-followers.md` · §3.3 L50：辅助有存在门后，将一般实例消去/116并列为不能自动视为同一记录操作。（固定B；blob `6c8046fb3691e6208b588c9090fb85dc7ea4ead4`）
- `deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md` · GR3-MR12 L490：输入将普通实例消去/116并列，预期只有普通实例不登记，没有116明确输出。（固定B；blob `18382cf43e137a671b245a1dd8d836694e6754ee`）
- `deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md` · §6.2 L120：记录式入口概要引用WP13，不补116差别。（固定B；blob `7482ac4dc1bdf3720a3d6d5c5c1c8b2a38e12f0d`）

**参考实际行为**

三个入口有不同合同：普通实例消去不记录；记录式脚本辅助只在当前事件存在时消去并记录；命令116只以事件ID>0为登记门，缺实例可安全跳过消去但仍登记当前图/ID真。116无论ID是否正都推进一项并停止本轮，后条待下一解释器更新机会。

**现规格的说法**

记录式辅助与普通实例的区别已覆盖，但116仅一行粗述，并与一般实例消去在正文/向量中并列；未明确其正ID登记、缺实例登记以及推进让出。

**差异/缺口**

这不是断言规格逐字写了“116绝不登记”；问题是正式三入口对照无法独立推导116的真实生产端和继续时机。 通用“假结果停止当前更新”的调度合同已经存在；只缺116本身选择这一控制结果并在内部推进一项的具名绑定，不另报通用解释器算法缺失。

**必要前提**

- 当前图B、局部记录对象存在，记录表空；解释器绑定事件ID7；合法命令列表中116后还有一条可观察全局开关命令；无其它写入。
- 正常例B中有事件7；边界例只改为B中没有事件7，解释器ID仍正。
- 主解释器记录的地图与当前地图相同，无消息/移动/冲浪等等待门；116不是终止项，后续全局开关命令之后还有正常终止项。

**最小反例**

```json
{
  "input": "边界例在一次解释器更新机会执行116。",
  "reference": "实例消去安全跳过，但(B,7)消去记录为真；索引指向后条且本次不执行后条开关。",
  "formal_gap": "若套记录式辅助缺事件不登记或普通实例不登记，将得到空记录；矩阵没有后条延后判据。",
  "evidence": "DERIVED_VECTOR; NOT_EXECUTED"
}
```

**正常对照**

B中事件7存在：消去/刷新实例，登记(B,7)真，然后推进一项并本轮停止。与直接实例消去不登记作对照。

**失败/边界对照**

ID0：不消去、不登记，仍推进/停止本轮。正ID缺实例：仍登记；局部记录对象为空时安全跳过登记。不借此承诺正常读档还原旧表，进入通知先清记录仍成立。

**独立实现影响**

独立事件兼容实现可能漏记录、把缺实例门套错，或立即连跑116后的全局命令；影响局部状态和当次更新顺序。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-evidence.json",
    "key": "GR4-M03-003",
    "scope_file_count": 131,
    "context_results": [
      "全131文件检索116/删除事件/消去记录/erasedEvents/pbEraseThisEvent及消去-登记别名。",
      "只有WP13矩阵116、WP13§3.3、WP11§6.2和GR3-MR12相关。另116为战斗评分数值和调试目录E116，不是事件命令。",
      "逐读上述及恢复端MR01–13：说明正常读档清表和辅助恢复，不能代替116生产端。",
      "源端command_116仅一处定义且直接主分派可达；addErasedEvent无实例门；Game_Event.erase和脚本辅助的门分别追踪。"
    ],
    "source_followup": "固定R所有脚本检索定义、同名覆写及所涉状态读写；追踪下述source anchors的实际入口/消费者；不把缺Demo当不存在。"
  },
  "primary_relative_paths_base": "modules/M03",
  "independent_counterevidence": {
    "search_ids": [
      "M03-erase",
      "M03-definitions"
    ],
    "words": [
      "\\b116\\b|pbEraseThisEvent|erasedEvents|消去|删除事件|本轮停止"
    ],
    "scope": {
      "baseline": "1f36475d22120a0d1175967d5b17d71fe8311d88",
      "root": "deliverables/final-specification-set/",
      "files": 131,
      "includes": "正文、共享条款、数据附表及静态测试目录；并非131篇逐篇重新验收"
    },
    "source_countersearch": [
      {
        "id": "M03-definitions",
        "pattern": "move_random_range|move_random_UD|move_random_LR|original_x|original_y|surf_base_coords|ending_surf|def command_116|def pbEraseThisEvent|def addErasedEvent|def pbCancelVehicles|def transfer_player",
        "files": 312
      }
    ],
    "contexts_read_and_assessed": [
      "WP13 §4.1和矩阵§2已有false本轮停止规则",
      "矩阵116缺其具体返回/推进；WP13 §3.3及GR3-MR12只确定辅助与普通实例两者区别",
      "WP11/09恢复端不提供116登记门"
    ],
    "conclusion": "不能把已有通用停止/推进说成全局缺失；缺的是116与这条规则的绑定，以及正ID而非实例存在的登记门。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CA"
}
```

**下一轮最小修订**

明确三入口表，修116矩阵的状态/缺事件/推进列，拆分GR3-MR12中的普通实例和116预期，并补正ID缺实例/ID0反向向量；保留读档先清表及历史CLOSED身份。

**验收标准**

```json
[
  "静态：三入口分别写是否登记及门；116正ID缺实例仍登记。",
  "静态：116索引推进一项并停止本轮，下一更新才尝试后条；不把返回false写成业务失败。",
  "静态向量：有实例、缺实例、ID0；局部记录为空可单独限定；后条开关作观察点，全部NOT_EXECUTED。",
  "历史：GR3-M03-004已关闭记录不改；按新增116消费者审查范围登记new_scope_same_root，不给旧全项重新签名。",
  {
    "kind": "SPEC_STATIC",
    "criterion": "只补116的具名推进/让出结果，复用已有通用调度；后条在下一次解释器更新机会尝试，不硬说下一渲染帧。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/engine-overworld/wp13-interpreter-command-matrix.md
- deliverables/final-specification-set/engine-overworld/wp13-map-events-npc-followers.md
- deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md
- deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md

**共享合同**

- WP11地图状态/转移
- WP12运动与通行
- WP13事件/路线及测试目录

**依赖**

- 有效地图/事件夹具
- 固定参考默认定义，无插件覆写
- 普通调用和指定更新机会

**能力范围引用**

- GR4-CAP-M03-009
- GR4-CAP-M03-010
- GR4-CAP-M03-024

**关联新问题**

无。

**根因身份**

GR4-M03-003

**旧GR3/229/341关系**

```json
{
  "relation": "new_scope_same_root",
  "third_round": "GR3-M03-004",
  "second_round": null,
  "note": "未知第二轮关联不猜ID；旧CLOSED身份不修改。",
  "independent_scope_assessment": {
    "relation": "new_scope_same_root",
    "ids": [
      "GR3-M03-004"
    ],
    "assessment": "B当前已标该历史条款并承接辅助/恢复部分；本项补主分派116生产端。保留旧关闭身份，不宣称旧全项重验，不与它简单MERGE而丢失新入口缺口。"
  }
}
```

**证据级别**

- SOURCE_STATIC
- SPEC_STATIC
- DERIVED_VECTOR

**执行状态**

NOT_EXECUTED

**置信限定**

HIGH_STATIC_WITH_STATED_PRECONDITIONS

**未知**

- 实际Demo使用/事件可达性未知；宿主和媒体结果未执行。
- 真实Demo安排、并行解释器销毁后的继续、宿主更新时机未运行；本例限定主解释器。

**排除的主张**

- 不要求修参考、不实现框架或保留源API/结构。
- 不宣称全部本域或全套规格均已审。

**用户政策边界**

无需决定是否补事实；若未来实现选择不同兼容政策，应另阶段明确，不由本审者代定。

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CA",
    "thread_id": "01a1301e-5efe-77a2-9450-fc09ff6830c1",
    "path": "modules/CA/verdicts.json",
    "pointer": "/records/7",
    "decision": "CONFIRM_WITH_REFINEMENT",
    "reason": "116的真实分派、实例安全消去和记录函数分别核实；当前正式三入口对照无法唯一推出其结果。通用false停止规则存在但116行没有给出它返回false及命令体自推进，所以仍需有界修正。",
    "required_refinements": [
      "明确解释器地图=当前图、无等待门及116不在终止项位置的夹具。",
      "以通用推进合同已有为前提，只补116具体控制结果，不重复报通用算法缺失。",
      "三入口分别列门；保持旧恢复清表合同与历史关闭状态。"
    ],
    "execution_evidence_assessment": {
      "ca_rerun": false,
      "receipt": "../M03/execution.json",
      "kind": "SOURCE_STATIC / SPEC_STATIC / DERIVED_VECTOR",
      "assessment": "原模块记录的Python清点/JSON/路径校验仅为TOOL_VALIDATION，不支持行为运行通过；CA未执行该脚本或参考函数。",
      "host_or_demo": "NOT_EXECUTED"
    },
    "historical_relation_assessment": {
      "relation": "new_scope_same_root",
      "ids": [
        "GR3-M03-004"
      ],
      "assessment": "B当前已标该历史条款并承接辅助/恢复部分；本项补主分派116生产端。保留旧关闭身份，不宣称旧全项重验，不与它简单MERGE而丢失新入口缺口。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```
