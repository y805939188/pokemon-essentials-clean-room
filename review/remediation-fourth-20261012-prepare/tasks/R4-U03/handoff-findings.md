# R4-U03 完整冻结finding任务正文

### GR4-M04-001 · P2 · REQUIRED — 按个体取图会求值动态形态，WP18却将图像归为简化形态读取

领域 M04；分类 状态或时序错误；独立审者 thread `01a12fdc-618e-7ea1-be11-c267b26fdb3d`；辅助证据目录 `modules/M04/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/010_Data/002_PBS data/009_Species_files.rb` · 92–109;123–124：个体正/背精灵及图标在选择资源前读取动态形态（固定R；blob `2a2e2fb92e7c05ec3b2f586edfda64cd4eeeaba3`）
- `Data/Scripts/014_Pokemon/001_Pokemon.rb` · 113–115;147–165：物种记录用简化读取；动态读取则可提交变化（固定R；blob `55e7e42c93cc8c0ae91f8594e7a7b9560eb9c22f`）
- `Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb` · 422–431：FURFROU超5天或缺时间戳回0，提交0清时间戳（固定R；blob `d643bcc5fc09d233880174bb2b7004c843d224ac`）
- `Data/Scripts/014_Pokemon/001_Pokemon-related/003_Pokemon_Sprites.rb` · 49–60;124–134：精灵和图标入口调用上述个体取图（固定R；blob `12da4a054e9cd244039c75e3b427153a676d4c0c`）
- `Data/Scripts/016_UI/006_UI_Summary.rb` · 117–134：摘要构造包含该精灵/图标调用链（固定R；blob `8a7dff8b8b0d41a4fb9a405ea726fa06365b6e9b`）
- `PBS/pokemon_forms.txt` · 1635–1661;FURFROU,1…9：默认剪毛形态数据存在；不证明图像资源存在（固定R；blob `08ae264e420484e31a81087eb3125d6f0c7fdaf6`）

**现规格依据**

- `deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md` · §3.4;149–151：普通form/简化form差异正确，但把图像列为简化读取例子（固定B；blob `cb30c0f4a1199b78b860ed513956eedd40c2c970`）
- `deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md` · §4.1;48–50：只说按个体形态取图，未指定动态/简化入口（固定B；blob `23c487115d8b01638ed2db062546ef2a58abdc9f`）
- `deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md` · §3.2-R03;157–163;§3.4;179–180：图像读取副作用一般声明与限时条件分别存在（固定B；blob `a11179facf0ff7822386945aca30aa8a9767528c`）
- `deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md` · FM07;U03-SP07–10：未连接到期形态与个体取图边界（固定B；blob `50086b77a48a2714af17cd8c86174d271397a942`）
- `deliverables/final-specification-set/creature-rpg/wp35-eggs-and-hatching.md` · §5.2/§9；99–122,158–169：已准确承接孵化核心与演出动态读取，必须保留的强反证。（固定B；blob `64308f9d5b6f13f71ac9d2fa408a143e0db8b6ca`）
- `deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md` · EG-13/EG-20；21–32,75：动态孵化对照已有承接，不重新报缺失。（固定B；blob `bb775bf94bd77dd3ff88d587ea093a6ec00076d5`）

**参考实际行为**

按个体取得精灵/图标时先求值普通动态形态；有forced则用forced，战斗/仓库中用存储值，否则动态候选不同会经完整形态提交，再以所得形态选资源。物种记录的基础能力读取用简化形态，两者不能合并。

**现规格的说法**

WP18 §3.4把“图像”列为简化形态读取消费者，属于明确的过宽分类。WP21已有动态读取/提交与守卫；WP35 §5.2/§9及EG-13/20还明确承接孵化演出先读动态形态的副作用。这些是实质反证和已正确部分，但不能消解WP18相反泛称；本项限于入口归属及跨文档一致性。

**差异/缺口**

混淆内容记录读取与按个体取图。会遗漏取图触发的限时形态回退、时间戳清理和完整提交副作用；不仅影响所选图像，也影响个体状态。

**必要前提**

- 合法非蛋FURFROU，存储形态1，forced为空，time_form_set=t
- 普通世界状态in_battle=false、in_storage=false；当前时刻t+432001秒，期间未先读动态形态
- 有效物种/形态和运行状态对象、无插件改写；直接按个体取图到达形态求值；若讨论摘要入口，前序界面资源/构造正常
- 若比较画面，另需不同形态资源存在；状态差异本身不依赖真实位图已显示
- 时间戳t为整数秒；物种资料、能力重算和图鉴依赖正常。显式参数对照先给定数值，不能以低层纯消费反推整条调用链纯读。

**最小反例**

```json
{
  "input": "同上，仅调用一次按个体取正面精灵入口。",
  "reference_static_result": "在资源查找前形态从1提交到0，time_form_set清空；清特性缓存、重算并条件图鉴登记，然后按形态0查图。",
  "result_if_following_incorrect_clause": "简化读取返回1；不触发到期判断/提交，时间戳仍t，按形态1查图。",
  "evidence_level": "DERIVED_VECTOR",
  "execution_status": "NOT_EXECUTED"
}
```

**正常对照**

整数t恰加432000秒不回退。低层按显式物种/形态取图只消费已求值的数值参数；若上游为获得参数先读个体动态形态，调用链仍可能有副作用，孵化即有已承接对照。

**失败/边界对照**

战斗/仓库为真或forced=1时，个体取图同样先走普通形态读取，但其守卫阻止动态回退；forced=0则返回0而不改存储1。无匹配资源时可取不到位图，之前已发生的形态求值/提交不因此成为简化读取或回滚。实际宿主失败和像素未知。

**独立实现影响**

按WP18实现无副作用的图像形态快照，会延迟或遗漏到期回退，并与普通形态查询、图鉴登记、后续能力/界面状态不一致。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-evidence-search.json",
    "corpus": "deliverables/final-specification-set",
    "file_count": 131,
    "queries": [
      "form_simple|简化形态",
      "取图|图像.*读取|个体.*图像|按个体",
      "FURFROU|HOOPA|限时形态|5 天|五天",
      "动态形态|读取副作用"
    ],
    "source_rebuttal": "全Scripts检索def form/def form_simple及个体取图定义；个体实现仅主Pokemon文件，Sprite里的form=是另一个类而非个体覆写。确认普通精灵、图标及摘要调用。",
    "conclusion": "不是缺少动态形态模块；是已存在的具体消费者分类错误。SPINDA纯像素数学与本项独立。"
  },
  "primary_relative_paths_base": "modules/M04",
  "independent_counterevidence": {
    "search_ids": [
      "M04-form",
      "M04-form-overrides",
      "CA-shared-alias-supplement"
    ],
    "words": [
      "form_simple|简化形态|取图|图像.{0,12}(读取|形态|副作用)|FURFROU|限时形态|五天|5 天",
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
        "id": "M04-form-overrides",
        "pattern": "def (self\\.)?(form\\b|form_simple\\b|sprite_bitmap_from_pokemon|icon_filename_from_pokemon|icon_bitmap_from_pokemon)|FURFROU|DEERLING|def pbHatch",
        "files": 312
      }
    ],
    "contexts_read_and_assessed": [
      "WP18 §3.4明确把图像归简化读取",
      "WP21 §3.2-R03已保留读取副作用、FM07/08已给限时回退",
      "强反证：WP35 §5.2/§9和EG-13/20已有孵化资源动态读写的明确合同"
    ],
    "conclusion": "不能声称正式集完全没有图像动态读取副作用；WP35已有具体承接。它与WP18泛称形成矛盾，仍不能让按个体正背精灵/图标的入口归属无歧义。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CA"
}
```

**下一轮最小修订**

最低修订是纠正WP18的图像泛称，并明确按个体精灵/图标入口继承普通动态读取合同；WP15/21按需要对齐引用，复用已正确的WP21/35提交与守卫。增具名静态对照，不重建动态形态整域，不修改WP35正确规则。

**验收标准**

```json
[
  {
    "kind": "STATIC",
    "criterion": "只凭正式集可区分物种内容记录读取与按个体精灵/图标取图；不再声称图像统一用简化形态。"
  },
  {
    "kind": "STATIC",
    "criterion": "给定t+432001反例推出形态0/时间戳空；t+432000仍1；守卫和强制形态对照准确。"
  },
  {
    "kind": "STATIC",
    "criterion": "说明状态求值先于图像匹配；不把无素材当作静态入口不可分析，不宣称真实像素/游戏通过。"
  },
  {
    "kind": "RUNTIME",
    "criterion": "本轮不要求运行参考/宿主；如以后执行，须独立记录输入/工具/输出与素材前提。"
  },
  {
    "kind": "SPEC_STATIC",
    "criterion": "保留WP35/EG-13/20已正确的动态孵化合同；显式物种资源接口仅在输入形态已求值时为纯消费，不外推调用者。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md
- deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md
- deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md
- deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md

**共享合同**

- 个体形态读取与资源消费交界
- 形态提交→时间戳/特性缓存/能力/图鉴

**依赖**

- M03资源匹配
- M10摘要/图标呈现
- WP21动态形态

**能力范围引用**

- GR4-CAP-M04-016

**关联新问题**

无。

**根因身份**

M04-image-consumer-form-read-dispatch

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "third_round": "GR3-M04-001 remains CLOSED; adjacent image consumer, different rule (dynamic form dispatch versus SPINDA pixel mathematics)",
  "second_round": null,
  "note": "没有据未知第二轮ID猜关联；不重开旧SPINDA整改。",
  "independent_scope_assessment": {
    "relation": "adjacent_dynamic_form_consumer_with_existing_shared_contract",
    "ids": [
      "GIR-FD82-A053",
      "GR3-M04-001"
    ],
    "assessment": "已读A053限定scope、孵化源链和B EG-13/20。A053是孵化核心与演出查询分层；M04是通用按个体取图/摘要入口及WP18上游分类。二者共享动态查询机制但不同消费范围，邻接关系准确；不重开A053，也不混SPINDA像素旧项。"
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

HIGH (fixed-source static dispatch and explicit spec claim)

**未知**

- 真实形态图是否存在、像素显示及宿主错误
- 插件/地图动态改写
- 实际资源和宿主像素未证；图鉴/能力重算只按依赖正常的静态调用链判定，插件改写未证。

**排除的主张**

- 不认定所有图像消费者均动态求值
- 不声称真实摘要成功运行
- 不要求保留源API或实现图形模块
- 不把SPINDA历史关闭改为未解决

**用户政策边界**

```json
false
```

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CA",
    "thread_id": "01a1301e-5efe-77a2-9450-fc09ff6830c1",
    "path": "modules/CA/verdicts.json",
    "pointer": "/records/8",
    "decision": "CONFIRM_WITH_REFINEMENT",
    "reason": "原R正背精灵/图标入口读取普通形态，形态提交链与FURFROU严格超5天条件均有明确源证。WP35是必须承认的已覆盖部分，但不能消除WP18直接相反的泛称；整改应收窄为入口归属/跨文档一致性，不重建整个动态形态规格。",
    "required_refinements": [
      "将WP35 §5.2/§9和EG-13/20作为已承接的强反证加入结论。",
      "最低整改是纠正WP18图像泛称，并明确个体入口继承动态读取合同；复用WP21/35既有提交/守卫，不重复扩成全域必修。",
      "显式物种/形态对照须提供已求值的数值参数；上游可能先读取个体，不能笼统称所有物种入口调用链无副作用。"
    ],
    "execution_evidence_assessment": {
      "ca_rerun": false,
      "receipt": "../M04/execution.json",
      "kind": "SOURCE_STATIC / SPEC_STATIC / DERIVED_VECTOR",
      "assessment": "原模块记录的Python清点/JSON/路径校验仅为TOOL_VALIDATION，不支持行为运行通过；CA未执行该脚本或参考函数。",
      "host_or_demo": "NOT_EXECUTED"
    },
    "historical_relation_assessment": {
      "relation": "adjacent_dynamic_form_consumer_with_existing_shared_contract",
      "ids": [
        "GIR-FD82-A053",
        "GR3-M04-001"
      ],
      "assessment": "已读A053限定scope、孵化源链和B EG-13/20。A053是孵化核心与演出查询分层；M04是通用按个体取图/摘要入口及WP18上游分类。二者共享动态查询机制但不同消费范围，邻接关系准确；不重开A053，也不混SPINDA像素旧项。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M06-001 · P3 · REQUIRED — BR18 在双不同力量道具前提下错误保留五项 IV 继承分支

领域 M06；分类 事实错误；独立审者 thread `01a12fe0-a4a3-75a0-87bd-03c04ac176c8`；辅助证据目录 `modules/M06/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/012_Overworld/007_Overworld_DayCare.rb` · 21–45,173–212：先3项，gen≥6且亲本持DESTINYKNOT才5；每个力量属性扣一次，其余不同属性抽样。（固定R；blob `302921c96ecfc4767d9ab9515d8d1e7820aa858c`）
- `Data/Scripts/014_Pokemon/001_Pokemon.rb` · 551–577：每个亲本持物读取/比较来自单一规范身份。（固定R；blob `55e7e42c93cc8c0ae91f8594e7a7b9560eb9c22f`）
- `PBS/items.txt` · 766–774,1423–1439：DESTINYKNOT、POWERWEIGHT、POWERBRACER是不同登记项。（固定R；blob `f0d40d5e111b85a606185101c326e24c832348d9`）

**现规格依据**

- `deliverables/final-specification-set/pokemon-rules/wp34-inheritance-and-offspring.md` · §7，128–134：正文的3/5数量及力量属性扣减是正确规则。（固定B；blob `be4e24a8a3941af83514c9837afc71c7a1e64262`）
- `deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md` · BR16–19，239–242：BR18错误地给双不同力量道具列5−2分支。（固定B；blob `50086b77a48a2714af17cd8c86174d271397a942`）
- `deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md` · §6.1–6.2：本轮仅核此合同／向量，不签全文件通过（固定B；blob `b8b953375034a8977abab199f2e1c715dec75e71`）

**参考实际行为**

普通单持物亲本各持不同力量道具时，均不持羁绊之绳，基础继承数恒3；两种不同属性各固定1项，只再从其余4属性无放回选1项。世代≥6不会单独把3变5。

**现规格的说法**

WP34 §7正文正确，但BR18明列固定2项后剩余采样1（3−2）或3（5−2）；后者在该行前提下不可达。

**差异/缺口**

静态测试接受了一个需要第三件亲本持物的预期，违反同集单持物与羁绊之绳必要条件。不是正文算法缺失。

**必要前提**

- 参考默认普通亲本、每个体一项持物、无插件或自定义多持物覆写；世代8。
- 两亲本可用合法♂/♀PIKACHU，分别持POWERWEIGHT和POWERBRACER；合法数据/场景/玩家。
- 只观察IV继承通道，不要求随机具体输出、孵化或领取。

**最小反例**

```json
{
  "input": "母POWERWEIGHT、父POWERBRACER；母HP31、父ATTACK31；其余亲本IV均0；蛋创建六IV均1（合法条件化随机输入）。",
  "expected": "HP31、ATTACK31；其余4属性中恰1项被继承为0、3项保创建值1。总继承属性3。",
  "incorrect_allowed_result": "若按BR18的5−2分支，再写3项为0，仅1项保创建值1，总继承属性5。",
  "evidence_level": "DERIVED_VECTOR",
  "execution_status": "NOT_EXECUTED"
}
```

**正常对照**

无Knot/无Power继承3项；双不同Power固定2+随机1；双相同Power固定同项一次+随机2。

**失败/边界对照**

合法五项对照应为一方DESTINYKNOT、另一方POWERWEIGHT（gen≥6）：固定HP1项、再选4项；gen5下同一配对仅3项（固定1+随机2）。

**独立实现影响**

照BR18构建验收会允许或要求不可能的5项组合，使正确3项实现的测试预期不唯一；正文已有正确规则，影响局限于向量质量，定P3。

**已完成的反证**

```json
{
  "primary_review": {
    "search_id": "M06-NEG-IV-01",
    "universe": {
      "root": "deliverables/final-specification-set/",
      "count": 131,
      "baseline": "1f36475d22120a0d1175967d5b17d71fe8311d88"
    },
    "query": "BR18|5−2|5-2|DESTINYKNOT|羁绊之绳|红线|力量道具|Power (?:Weight|Bracer|items?)",
    "method": "全套正式Markdown合理别名搜索；命中上下文按繁育主规则、静态向量、持物共享合同与纯物品目录区分。",
    "hits": [
      {
        "path": "deliverables/final-specification-set/combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md",
        "line_numbers": [
          225,
          227,
          245
        ]
      },
      {
        "path": "deliverables/final-specification-set/combat-requirements/wp47-b-control-items-coverage-data.md",
        "line_numbers": [
          72
        ]
      },
      {
        "path": "deliverables/final-specification-set/combat-requirements/wp52-a-generic-numerical-and-status-evaluation.md",
        "line_numbers": [
          205
        ]
      },
      {
        "path": "deliverables/final-specification-set/combat-requirements/wp52-c-item-control-coverage-and-data.md",
        "line_numbers": [
          105
        ]
      },
      {
        "path": "deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md",
        "line_numbers": [
          345
        ]
      },
      {
        "path": "deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md",
        "line_numbers": [
          241
        ]
      },
      {
        "path": "deliverables/final-specification-set/creature-rpg/wp24-player-trainers-partners.md",
        "line_numbers": [
          272
        ]
      },
      {
        "path": "deliverables/final-specification-set/creature-rpg/wp25-party-and-storage.md",
        "line_numbers": [
          203
        ]
      },
      {
        "path": "deliverables/final-specification-set/creature-rpg/wp26-acquisition-gifts-and-script-trade.md",
        "line_numbers": [
          192
        ]
      },
      {
        "path": "deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md",
        "line_numbers": [
          252
        ]
      },
      {
        "path": "deliverables/final-specification-set/generic-kernel/wp02-rule-configuration-and-data-variants.md",
        "line_numbers": [
          197
        ]
      },
      {
        "path": "deliverables/final-specification-set/pokemon-rules/wp34-inheritance-and-offspring.md",
        "line_numbers": [
          128,
          130,
          131,
          160,
          175,
          188,
          202
        ]
      },
      {
        "path": "deliverables/final-specification-set/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md",
        "line_numbers": [
          74
        ]
      },
      {
        "path": "deliverables/final-specification-set/pokemon-rules/wp50-held-item-triggers-and-consumption.md",
        "line_numbers": [
          163
        ]
      },
      {
        "path": "deliverables/final-specification-set/test-catalog/README.md",
        "line_numbers": [
          38
        ]
      },
      {
        "path": "deliverables/final-specification-set/test-catalog/combat-requirements-wp39-40-41-42-45.md",
        "line_numbers": [
          160
        ]
      },
      {
        "path": "deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md",
        "line_numbers": [
          129
        ]
      },
      {
        "path": "deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md",
        "line_numbers": [
          239,
          240,
          241
        ]
      }
    ],
    "contexts_read": [
      "WP34 §7, §9, §10, §11；BR16–19；WP20 §6.1–6.3",
      "WP30/WP02配置EV项；WP42 Pickup稀有池；WP44/WP50/WP52A及相应测试的迷恋效果；WP47B/WP52C纯物品身份行",
      "其余WP18/24/25/26及测试README命中来自文件名中的5-2，已读命中上下文，为导航而非IV规则"
    ],
    "result": "仅BR18含双不同力量物品仍可5−2的预期；WP34明确五项必须亲本持DESTINYKNOT，WP20单持物合同并未豁免；其它命中为战斗/EV或物品目录，不改变遗传持物门。",
    "source_countercheck": {
      "query": "inherit_IVs|DESTINYKNOT|POWERWEIGHT|POWERBRACER (all Data/Scripts)",
      "result": "仅DayCare生成链定义并调用inherit_IVs；其它命中是战斗/AI/物品效果。生成入口不接收独立继承数量或多持物参数；Pokemon持物单一身份，默认PBS三物品互异。"
    },
    "evidence_level": [
      "SOURCE_STATIC",
      "SPEC_STATIC"
    ],
    "execution_status": "NOT_EXECUTED"
  },
  "primary_relative_paths_base": "modules/M06",
  "independent_counterevidence": {
    "search_ids": [
      "M06-power",
      "M06-iv-overrides"
    ],
    "words": [
      "BR18|5−2|DESTINYKNOT|羁绊之绳|红线|力量道具|POWERWEIGHT|POWERBRACER"
    ],
    "scope": {
      "baseline": "1f36475d22120a0d1175967d5b17d71fe8311d88",
      "root": "deliverables/final-specification-set/",
      "files": 131,
      "includes": "正文、共享条款、数据附表及静态测试目录；并非131篇逐篇重新验收"
    },
    "source_countersearch": [
      {
        "id": "M06-iv-overrides",
        "pattern": "inherit_IVs|def hasItem\\?|DESTINYKNOT|POWERWEIGHT|POWERBRACER",
        "files": 312
      }
    ],
    "contexts_read_and_assessed": [
      "WP34 §7数量规则正确；BR16/17/19与BR18对照",
      "WP20单一持物及同一身份比较",
      "力量EV/速度、红线迷恋/拾取、AI评级附表均不提供第三持物或额外继承数量"
    ],
    "conclusion": "BR18的5−2分支没有满足羁绊之绳门的普通输入；正确正文不能让错误验收分支成立。不是整个遗传算法缺失。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CA"
}
```

**下一轮最小修订**

仅修BR18为固定2+随机1；可补单Knot+单Power的合法5项及gen5对照。保留WP34正确数量规则和持物合同，不改参考或发明多持物能力。

**验收标准**

```json
[
  {
    "kind": "static",
    "criterion": "双不同Power向量只允许3个不同继承属性，两个固定、一个其余属性。"
  },
  {
    "kind": "static",
    "criterion": "若保留5项对照，前提明确gen≥6、一个Knot持有者和至多一个Power持有者；固定1+其余4。"
  },
  {
    "kind": "static",
    "criterion": "正文与测试不暗含每亲本多件持物，且同Power重复属性只计一次。"
  },
  {
    "kind": "runtime",
    "criterion": "本轮不要求宿主或参考运行；任何后续执行须另立隔离记录，不能把本推导升格为执行。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md

**共享合同**

- deliverables/final-specification-set/pokemon-rules/wp34-inheritance-and-offspring.md §7
- deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md §6

**依赖**

- WP33两槽生成入口
- WP20单持物身份
- 世代配置

**能力范围引用**

- GR4-CAP-M06-015

**关联新问题**

无。

**根因身份**

M06_IV_VECTOR_UNSATISFIABLE_HELD_ITEM_COMBINATION

**旧GR3/229/341关系**

```json
{
  "relationship": "new",
  "third_round_related_id": null,
  "second_round_related_id": null,
  "note": "未猜第二轮ID；与GR3-M06-001经验提示时点根因不同，不重开旧CLOSED。",
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

high_static

**未知**

- 第三方多持物插件可改行为，但无此材料且不在该向量前提。
- 第三方多持物/重写比较可改变前提，但无该材料且不属于普通BR18输入；未运行繁育。

**排除的主张**

- 不认定WP34正文继承算法错误
- 不认定官方游戏规则是证据
- 不声称运行捕获/繁育/宿主
- 不把随机数值恰等于亲本值视作该属性实际继承

**用户政策边界**

```json
false
```

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CA",
    "thread_id": "01a1301e-5efe-77a2-9450-fc09ff6830c1",
    "path": "modules/CA/verdicts.json",
    "pointer": "/records/10",
    "decision": "CONFIRM",
    "reason": "源数量门要求Knot，两个普通持物槽已被不同Power占满且三身份确实不同；B正文正确而BR18接受不可能分支。最小反例条件可满足，P3局部测试纠错合适。",
    "required_refinements": [],
    "execution_evidence_assessment": {
      "ca_rerun": false,
      "receipt": "../M06/execution.json",
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

### GR4-M10-001 · P2 · REQUIRED — 通用命令选择与逐位数字输入的同轮优先序仍缺少合同

领域 M10；分类 状态或时序错误；独立审者 thread `01a12ff1-a1b1-7212-84b3-c3fdcd6552a9`；辅助证据目录 `modules/M10/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/007_Objects and windows/011_Messages.rb` · 166–205;721–801：数字先组件更新，再USE/elif BACK；普通及帮助命令先BACK，取消无效时仍可USE。（固定R；blob `91c985bd0fda9a2368c894dee0ebbc9a476e9886`）
- `Data/Scripts/007_Objects and windows/005_SpriteWindow_text.rb` · 687–729;862–923：数字/列表方向处理均在确认出口之前，故可同轮改值/改索引并返回。（固定R；blob `e8be64d69b3bcb02def7a0cc09c0a5d4027cc628`）
- `Data/Scripts/003_Game processing/004_Interpreter_Commands.rb` · 325–334：事件数字输入调用同一逐位数字入口，结果写变量。（固定R；blob `58167231199f1cb8bdc499a61f5ada544d3f7616`）
- `Data/Scripts/016_UI/019_UI_PC.rb` · 4–16;116–153：正常PC菜单消费者使用普通/帮助命令入口。（固定R；blob `254fd995a55ad17bd82a341d1b13eb7cb6fc212b`）

**现规格依据**

- `deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md` · §4 L92–99、§5.2–5.3 L114–121、§7.2：仅定义单键结果和更新机会，没有各入口竞争结果。（固定B；blob `81b14a0b09327bc030e5d9ef9f907089bd68cb82`）
- `deliverables/final-specification-set/user-interface/wp66-c-bag-item-storage-and-shop-ui.md` · §5.1 L88–108：旧同轮表明确是共享物品数量/两商店。（固定B；blob `f49d1e3a64e64fb61e1351372f34302a7b925e78`）
- `deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md` · MG12–MG20、B04-M07–09、U05-QN01–04：分别覆盖单键、光标命名、物品数量，不覆盖普通命令和逐位数字竞争。（固定B；blob `5dbb1fbed36800c39844a549939b5123c4b3c1c5`）

**参考实际行为**

命令/带帮助命令：允许取消时同轮BACK+USE返回取消编码；取消项0时BACK无效但本轮USE仍返回当前索引。逐位数字：先编辑方向再USE；合法值当轮确认，USE与BACK同时成立仍确认；越界USE只蜂鸣继续，BACK不被处理。

**现规格的说法**

命令与数字各有确认/取消条款，但未给竞争裁决。已有明确同轮表的“共享数量”是按件数增减窗口，不能泛用于逐位数字；命名的优先序同样是另一入口。

**差异/缺口**

缺少两个实际默认消费者的同轮返回/继续判据；从单键规则无法唯一推出确认还是取消，以及方向能否与确认同轮发生。

**必要前提**

- 无插件，窗口已正常进入循环；列出的输入查询同采样轮为真，其余假。
- 命令为两项、默认索引0；取消项分别2与0。数字范围[0,9]、初值1、显式取消值−1。
- 方向值由正常组件更新产生；数字越界对照采用范围[3,3]初值3同轮UP。
- 无传入块改写值或输入；USE/BACK是给定按下沿，方向是给定repeat查询，不是已实测物理按键。事件103的默认取消值为初值；显式取消−1只是独立通用数字夹具。

**最小反例**

```json
{
  "input": "普通命令取消项2/索引0，USE+BACK；独立数字范围[0,9]/当前1/取消−1，USE+BACK。",
  "reference_output": "前者返回1；后者返回1作为确认，绝非取消−1。",
  "distinguishing_alternative": "全局“取消优先”会使数字返回−1；全局“确认优先”会使命令返回0。"
}
```

**正常对照**

两项命令单独USE返回0、单独BACK在取消项2时返回1；数字单独USE返回1、单独BACK返回−1。

**失败/边界对照**

- 数字当前1，UP+USE→先变2再立即返回2；它不遵守物品数量一轮只执行首个动作。
- 数字范围[3,3]初值3，UP+USE+BACK→先变4，确认越界蜂鸣，留循环；同轮BACK不会救出。
- 命令取消项0，USE+BACK→BACK无效后仍返回当前索引0；带帮助入口相同。

**独立实现影响**

独立实现若采用统一按钮裁决会产生不同的选择/事件变量值，或在参考仍等待的越界场景提前取消。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-searches.json",
    "search_ids": [
      "selector_competition",
      "selector_priority_exact"
    ],
    "scope": "全部131正式文件",
    "relevant_contexts_read": [
      "deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md §4/5/6.2.1/7.2",
      "deliverables/final-specification-set/user-interface/wp66-c-bag-item-storage-and-shop-ui.md §5.1",
      "deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md MG/B04-M/U05-QN",
      "deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md §7"
    ],
    "result": "确认已存在的光标命名与物品数量竞争规则均不同入口；未找到普通命令/帮助命令或逐位数字的上述裁决。其它命中为录像/转换的同轮概念，不能承接此行为。"
  },
  "primary_relative_paths_base": "modules/M10",
  "independent_counterevidence": {
    "search_ids": [
      "CB-N01"
    ],
    "terms": [
      "同轮|同一轮|同时.{0,20}(USE|BACK|确认|取消)|竞争|取消优先|确认优先|逐位|命令选择|MG1[2-9]|MG20|U05-QN"
    ],
    "scope": "B 固定正式131篇，正文、scope、共享合同、附表和测试全部纳入；各检索文件字节与 git show B 相等",
    "contexts_actually_read": [
      "WP17 §4/§5/§6.2.1/§6.4/§7.2",
      "WP66-C §5.1 与 U05-QN01–04",
      "WP67-A §9.1 与 U05-TX01–04",
      "WP65 §7.2；WP13命令103"
    ],
    "conclusion": "命名、共享件数、商店与战斗列表确有局部规则，但均不能推出普通命令和逐位数字的不同竞争结果。MG12的不可取消及MG18的越界只给单独输入；没有全局确认/取消优先规则可补此缺口。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CB"
}
```

**下一轮最小修订**

在WP17按入口增加一个简短竞争表：命令的可取消/不可取消分流；数字先编辑再确认、USE优先及越界仍压过BACK。给定静态查询前提，不规定输入调度实现。

**验收标准**

```json
[
  {
    "kind": "SPEC_STATIC",
    "criterion": "仅凭正式集可唯一推出上述命令2/0与数字合法/越界四分支。"
  },
  {
    "kind": "DERIVED_VECTOR",
    "criterion": "增加单键对照、UP+USE与越界UP+USE+BACK案例，标NOT_EXECUTED。"
  },
  {
    "kind": "SPEC_STATIC",
    "criterion": "保留U05物品数量/商店与光标命名合同，不把其顺序统一化。"
  },
  {
    "kind": "EXECUTED_HOST_OR_DEMO",
    "criterion": "如未来声称物理键可达/真实UI通过，须另供宿主证据；本修订不要求先运行。"
  },
  {
    "kind": "SPEC_STATIC",
    "criterion": "事件数字消费者另用默认取消等于初值的夹具；例如初1同轮UP+USE+BACK确认2，不能把通用取消−1称为该事件默认。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md
- deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md

**共享合同**

- WP65 PC命令
- WP13事件数字输入
- WP66-C数量窗口分界

**依赖**

- WP17通用UI
- WP15资源访问
- 宿主输入/字体或媒体接口的条件前提

**能力范围引用**

- GR4-CAP-M10-002

**关联新问题**

无。

**根因身份**

```json
{
  "id": "GR4-M10-001-ROOT",
  "description": "缺少两个实际默认消费者的同轮返回/继续判据；从单键规则无法唯一推出确认还是取消，以及方向能否与确认同轮发生。"
}
```

**旧GR3/229/341关系**

```json
{
  "relation": "new_scope_same_root",
  "third_round": "GR3-M10-002",
  "second_round": null,
  "note": "GR3-M10-002对物品数量/钱店/BP的修订仍满足，当前新增普通命令与逐位数字入口，非旧项未解决或回归。",
  "independent_scope_assessment": {
    "relation": "new_scope_same_root",
    "related_ids": [
      "GR3-M10-002"
    ],
    "assessment": "B中U05件数/商店条款已存在且范围明确；本项是同类问题的新增消费者范围，不是该旧范围回归，不重开或补签旧关闭。M01–M06十一候选无同根；M03路线时序不同。"
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

HIGH_STATIC

**未知**

- 真实宿主/媒体/输入未运行；未推断完整Demo可达。
- 真实宿主、媒体、物理输入与完整Demo未执行；外部插件不在固定R证明范围。

**排除的主张**

- 不要求采用源类/方法/容器组织。
- 不修改参考或决定未来产品必须保留该兼容细节。

**用户政策边界**

```json
false
```

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CB",
    "thread_id": "01a13036-2ee9-7e43-8d09-4699ed1b03f4",
    "path": "modules/CB/verdicts.json",
    "pointer": "/records/0",
    "decision": "CONFIRM",
    "reason": "确认有实际调用与清楚的最小差异。先更新组件与之后两个出口的相对次序决定返回值或继续等待，现有各入口单键规则不能唯一决定它。范围限通用命令/帮助命令及逐位数字，不推广为全部UI；P2针对可改变有效选择和事件变量的行为合同。",
    "required_refinements": [],
    "execution_evidence_assessment": "该候选没有参考行为执行。原模块工具校验只证明产物结构/锚点等，不能证明本候选行为；CB未运行参考函数、行为模型、UI、输入或宿主。以下结果为源码/规格静态核对及条件化推导。",
    "historical_relation_assessment": {
      "relation": "new_scope_same_root",
      "related_ids": [
        "GR3-M10-002"
      ],
      "assessment": "B中U05件数/商店条款已存在且范围明确；本项是同类问题的新增消费者范围，不是该旧范围回归，不重开或补签旧关闭。M01–M06十一候选无同根；M03路线时序不同。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M10-002 · P3 · REQUIRED — 默认皮肤冷读取的回退链与显式设置空结果未进入资源合同

领域 M10；分类 数据或资源契约缺口；独立审者 thread `01a12ff1-a1b1-7212-84b3-c3fdcd6552a9`；辅助证据目录 `modules/M10/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/007_Objects and windows/002_MessageConfig.rb` · 35–85：冷读取先选项皮肤，后系统名、System/Window、001-Blue01；显式设置只解析一次并保留空结果。（固定R；blob `47813fd34df588b24a5cc84f9928d9a55f4bcfc6`）
- `Data/Scripts/007_Objects and windows/004_SpriteWindow.rb` · 818–868：窗口默认皮肤消费缓存；显式setSkin解析失败提前返回，不自动使用默认链。（固定R；blob `c579631b93f6f9fe160bfebaeea3543233706021`）
- `Data/Scripts/007_Objects and windows/011_Messages.rb` · 380–394;444–450：普通消息采用speech默认；空w标签直接清windowskin，属不同操作。（固定R；blob `91c985bd0fda9a2368c894dee0ebbc9a476e9886`）
- `Data/Scripts/016_UI/015_UI_Options.rb` · 492–519：选项值先写再显式设置皮肤缓存及预览。（固定R；blob `cb4a2285bf3c7c3dc4464e36f0769b3d1835321f`）

**现规格依据**

- `deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md` · §3.1 L35、§3.4 L86–87、§7.3 L229：提供空w清皮肤与按选项选肤；资源缺失转引WP15。（固定B；blob `81b14a0b09327bc030e5d9ef9f907089bd68cb82`）
- `deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md` · §3.1、§5.1、§7：有通用图像解析/包装失败，没有窗口默认候选链。（固定B；blob `23c487115d8b01638ed2db062546ef2a58abdc9f`）
- `deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md` · §5.2 L123–124：Speech/Menu Frame正常预览，但缺专属回退条件。（固定B；blob `5a4a629a56ef240de1c34b7e71d428def08a4737`）
- `deliverables/final-specification-set/generic-kernel/wp02-rule-configuration-and-data-variants.md` · 配置目录 SPEECH_WINDOWSKINS/MENU_WINDOWSKINS：仅表数量/角色，不提供回退选择。（固定B；blob `f0fed00b433c0e169b5e75f70f54d944009486a0`）

**参考实际行为**

未初始化的菜单/消息皮肤分别先解析选项指向的资源；未命中才解析系统登记名，再通用Graphics/System/Window，再Graphics/Windowskins/001-Blue01，最终为空。显式设置解析失败后记录空值，后续读取把它当已设置结果，不重新走冷读取回退。

**现规格的说法**

正式集从选项皮肤直接转引通用解析失败规则；未给这一专用搜索链，也未区分“尚未求默认”与“明确设置为空”。

**差异/缺口**

缺少可以独立决定备用皮肤身份的资源选择规则；即便准备相同可用素材，也无法由正式集确定结果。

**必要前提**

- 皮肤配置索引在范围内；初取的缓存未初始化；无插件。
- 所选皮肤缺失，系统登记名Custom有效，Custom与两个通用候选均可解析；图像加载正常。
- 显式设置对照独立开始，输入一个无法解析的皮肤名，后续只检查逻辑解析结果；不承诺已释放图像的实际画面。
- 显式设置对照指定完整逻辑资源位置，不假设任意裸名自动加目录；未提供选项对象时从配置首项开始。

**最小反例**

```json
{
  "input": "初取消息皮肤：选项资源Missing不存在、系统windowskin名Custom存在、System/Window和001-Blue01也存在。",
  "reference_output": "选择Custom；不返回nil，也不直接采用通用Window。",
  "distinguishing_alternative": "正式仅有通用“解析未命中nil”不足以确定这一身份选择。"
}
```

**正常对照**

所选皮肤能解析时直接使用，不尝试系统/通用备用。

**失败/边界对照**

- 系统名也不存在→System/Window；再缺→001-Blue01；全缺→空逻辑皮肤。
- 相同备用资源存在，显式设置Missing后读取仍为空；不再冷回退Custom。
- 消息中的空w标签直接清除皮肤，不应与显式设置不存在名称等同。

**独立实现影响**

默认UI在缺少一个皮肤资源时可能错误地选空白或选错备用；设置项的后续读取也可能错误恢复默认。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-searches.json",
    "search_ids": [
      "font_skin",
      "skin_fallback_exact"
    ],
    "scope": "全部131正式文件",
    "relevant_contexts_read": [
      "deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md §3.1/3.4/7.3",
      "deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md §3/5/7",
      "deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md §5.2",
      "deliverables/final-specification-set/generic-kernel/wp02-rule-configuration-and-data-variants.md 配置表",
      "deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md §失败边界"
    ],
    "result": "字体Arial、形态皮肤、编辑器Windowskins目录异常、w空标签及普通资源解析均不是本回退链；未见001-Blue01/System/Window或冷取与显式设置分层合同。"
  },
  "primary_relative_paths_base": "modules/M10",
  "independent_counterevidence": {
    "search_ids": [
      "CB-N02"
    ],
    "terms": [
      "皮肤|windowskin|001-Blue01|System/Window|Speech Frame|Menu Frame"
    ],
    "scope": "B 固定正式131篇，正文、scope、共享合同、附表和测试全部纳入；各检索文件字节与 git show B 相等",
    "contexts_actually_read": [
      "WP17 §3.1/3.4/7.3",
      "WP15 §3.1/5.1",
      "WP65 §5.1/5.2",
      "WP02配置表",
      "WP73-A §9/CE-M18；WP13命令131；MG05"
    ],
    "conclusion": "未发现默认候选身份链或未初始化与显式空结果的区别。通用解析nil、空文件名空白图、空w、未匹配配置名和编辑器目录失败都有各自前提，不能替代冷取。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CB"
}
```

**下一轮最小修订**

补默认菜单/消息皮肤候选优先级、每步存在性门、最终空结果与显式设置的区别；限定逻辑结果，不补造缺图后的像素恢复或新类结构。

**验收标准**

```json
[
  {
    "kind": "SPEC_STATIC",
    "criterion": "给出选项命中、系统命中、两个通用备用依次命中及全缺的结果。"
  },
  {
    "kind": "DERIVED_VECTOR",
    "criterion": "相同素材条件下，冷读取Missing得到Custom而显式设置Missing后读取为空，标未执行。"
  },
  {
    "kind": "SPEC_STATIC",
    "criterion": "空w标签保持原直接清空合同；不把逻辑空值等于所有既有窗口统一无皮肤。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md
- deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md
- deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md

**共享合同**

- WP02皮肤列表
- WP65皮肤预览

**依赖**

- WP17通用UI
- WP15资源访问
- 宿主输入/字体或媒体接口的条件前提

**能力范围引用**

- GR4-CAP-M10-004
- GR4-CAP-M10-015

**关联新问题**

无。

**根因身份**

```json
{
  "id": "GR4-M10-002-ROOT",
  "description": "缺少可以独立决定备用皮肤身份的资源选择规则；即便准备相同可用素材，也无法由正式集确定结果。"
}
```

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "third_round": null,
  "second_round": null,
  "note": "不猜第二轮ID，不据旧PASS判定本轮支持。",
  "independent_scope_assessment": {
    "relation": "new_within_reviewed_scope",
    "related_ids": [],
    "assessment": "未见与M01–M06同根。没有据历史PASS或旧政策确定完整性；不追认未知第二轮ID。"
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

HIGH_STATIC

**未知**

- 所有皮肤图像缺失；无真实窗口验证。
- 显式换肤失败时先释放旧定制资源后的具体宿主画面未验证，未据此声称保持原画面或崩溃。
- 皮肤媒体和真实窗口未取得/未运行；空名称后既有窗口的实际呈现、旧资源释放效果不在本结论。
- 未来是否采用相同候选身份属于兼容政策，事实修订不预先决定。

**排除的主张**

- 不要求采用源类/方法/容器组织。
- 不修改参考或决定未来产品必须保留该兼容细节。
- 逻辑空资源名称不等于既有窗口必定清皮肤、保持旧图或必崩溃；这些真实像素与对象失效结果未证。

**用户政策边界**

```json
false
```

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CB",
    "thread_id": "01a13036-2ee9-7e43-8d09-4699ed1b03f4",
    "path": "modules/CB/verdicts.json",
    "pointer": "/records/1",
    "decision": "CONFIRM",
    "reason": "候选补的是按同一资源集合如何选择备用身份，而不是一般资源缺失标题。原报告已正确排除了空w与单窗设置的画面推论。P3限于缺资源时的默认选择及后续读取，非整个资源系统缺失。",
    "required_refinements": [],
    "execution_evidence_assessment": "该候选没有参考行为执行。原模块工具校验只证明产物结构/锚点等，不能证明本候选行为；CB未运行参考函数、行为模型、UI、输入或宿主。以下结果为源码/规格静态核对及条件化推导。",
    "historical_relation_assessment": {
      "relation": "new_within_reviewed_scope",
      "related_ids": [],
      "assessment": "未见与M01–M06同根。没有据历史PASS或旧政策确定完整性；不追认未知第二轮ID。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M10-003 · P2 · REQUIRED — 长无空格文本的超宽不逐字折行边界未被规格承接

领域 M10；分类 实现信息不足；独立审者 thread `01a12ff1-a1b1-7212-84b3-c3fdcd6552a9`；辅助证据目录 `modules/M10/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/007_Objects and windows/010_DrawText.rb` · 128–205;611–658;1035–1040：两格式化路径都需要非行首词边界才把整词移至下一行；无空格行首长串不会按字符拆行。（固定R；blob `2d6b723b705cc8ecabc6015e13d96359c3b16d81`）
- `Data/Scripts/007_Objects and windows/005_SpriteWindow_text.rb` · 316–347：普通消息将内容宽度传给格式化，依据生成的换行插暂停。（固定R；blob `e8be64d69b3bcb02def7a0cc09c0a5d4027cc628`）
- `Data/Scripts/016_UI/006_UI_Summary.rb` · 519–537;560–587;637：获得文本/地名进入宽268的格式化备忘录，源端不是专用长词换行器。（固定R；blob `8a7dff8b8b0d41a4fb9a405ea726fa06365b6e9b`）

**现规格依据**

- `deliverables/final-specification-set/user-interface/wp17-draw-text-tags.md` · §3、§6 L93：只描述显式对齐/换行，完整排版改为以绘制函数为准。（固定B；blob `0e643fe2440bc78ac6095d9e6fb4d15fca3994b0`）
- `deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md` · §3.3 L82：自动行满暂停示例含显式换行，未给自动宽度换行规则。（固定B；blob `81b14a0b09327bc030e5d9ef9f907089bd68cb82`）
- `deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md` · §5.2 L143–160：列长文本消费者字段，未给超宽词结果。（固定B；blob `04ecf28f8e63958ff848abce99e082736fdbf4c0`）

**参考实际行为**

在正常测量下，行首的一段连续非空白文本即使超过请求行宽，仍在同一逻辑行产生绘制项；不会按字符硬折行。有此前词边界的下一词超宽时可整词移到下一行；显式换行仍生效。这同时存在于无标记快路径和带格式标记的一般路径。 固定参考的换行宽度判定还预留额外2个同单位的测量量；需非行首词边界及对应内容条件成立才移词，不能概括为裸文字宽大于请求行宽。

**现规格的说法**

正式给出标签、行数/行满暂停和摘要字段；排版正文把完整换行算法留在参考绘制函数，没有实现无关的长词边界或案例。

**差异/缺口**

文本可见行为依赖未移交的分词/折行条件，独立实现无法区分自动逐字折行与保持超宽单行。

**必要前提**

- 有效位图/字体测量接口；默认允许自动折行；高度不限制行；无插件和图像/等待控制符。
- 静态测量夹具：A/B各宽8、空格宽4，请求行宽12；不声称真实Power Green有这些度量。
- 比较直接AB与A B；再以已识别无动作pg标签使同一文字走一般路径。
- 普通样式、起点x=0、非斜体、无额外描边，自动与显式换行均开启；高度不限制。<pg>只用于路径对照，比较逻辑行归属，不要求两个路径绝对纵坐标相同。

**最小反例**

```json
{
  "input": "行宽12、测量A=B=8，文本AB；独立对照A B（空格4）。",
  "reference_output": "AB仍只有一个文字行，B横向起点8；A B把B移至下一文字行。带pg标记仍有同样行归属差异。",
  "distinguishing_alternative": "常规逐字折行会把AB中的B移到下一行，改变消息后续行满暂停位置与摘要布局。"
}
```

**正常对照**

短文字在宽内保持一行；显式A换行B形成两行。

**失败/边界对照**

- 长无空格词/连续无空白本地化文本不硬拆行；只承诺生成的布局请求，不宣称屏外字形最终如何裁切。
- 有词边界的A B可整词移行；不能据此泛化任何长词都能装入宽度。
- 摘要备忘录固定宽度输入不增加额外滚动或长词策略；最终像素仍依赖字体和宿主。
- 同一度量A=8、B=8、ASCII空格=4，A B在行宽22保持一行、行宽21时B移下一行；此边界体现额外2单位，不是字体实测或裸宽比较。

**独立实现影响**

语言较长或无空格的文本可能产生不同的可见行数、被遮挡内容和暂停时点；仅凭现集需重新读源才能保持参考行为。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-searches.json",
    "search_ids": [
      "summary_particles",
      "long_text_wrap"
    ],
    "scope": "全部131正式文件",
    "relevant_contexts_read": [
      "deliverables/final-specification-set/user-interface/wp17-draw-text-tags.md §3/6",
      "deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md §3.3/6.3",
      "deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md §5.2",
      "deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md DT04/B04-M14",
      "deliverables/final-specification-set/generic-kernel/wp08-localization.md 非目标"
    ],
    "result": "命中的是显式换行、命令文本转换或编辑长度限制；DT04是对齐触发换行，B04-M14依赖显式换行。未见无空白长词/自动折行边界；§6明确留空不等于有可用净室合同。"
  },
  "primary_relative_paths_base": "modules/M10",
  "independent_counterevidence": {
    "search_ids": [
      "CB-N03",
      "CB-N03b"
    ],
    "terms": [
      "无空[格白]|长词|超宽|折行|自动换行|word.?wrap|wrap.?word|分词|行首|文本.{0,12}换行|换行.{0,12}文本|getFormattedText|B04-M14|DT04",
      "排版|折行|自动换行|word.?wrap|无空格|无空白|超宽|长文本|长词"
    ],
    "scope": "B 固定正式131篇，正文、scope、共享合同、附表和测试全部纳入；各检索文件字节与 git show B 相等",
    "contexts_actually_read": [
      "WP17绘制附表§3/§6；主文§3.3/§6.3",
      "WP66-A §5.2",
      "DT04、DT08、B04-M14",
      "WP08非目标；WP73-A文本长度；scope媒体限制"
    ],
    "conclusion": "未找到无空白串不硬折行或普通自动宽度换行的行为规则。显式换行、对齐换行、输入字数上限及文本转换是不同条件。附表转回参考绘制函数并不能让净室实现者推出AB/A B结果。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CB"
}
```

**下一轮最小修订**

补一个最小行为规则与两条测量夹具：基于词边界的自动折行、行首超宽连续串不硬拆、显式换行优先；说明消息/摘要消费，保留最终像素与未来改善策略自由。无需复写排版函数。

**验收标准**

```json
[
  {
    "kind": "SPEC_STATIC",
    "criterion": "说明无空白长串与含词边界文本的不同结果，不以参考函数名代替规则。"
  },
  {
    "kind": "DERIVED_VECTOR",
    "criterion": "AB、A B、显式换行、带pg四组独立夹具给行归属；注明测量是假定输入、未运行字体。"
  },
  {
    "kind": "SPEC_STATIC",
    "criterion": "不会把消息行满暂停/摘要坐标说明扩成保证所有长文本可见，也不要求逐像素复刻。"
  },
  {
    "kind": "SPEC_STATIC",
    "criterion": "明确额外2个测量单位及适用的词边界/内容门；补A B宽22不换、21换的独立对照，并限定普通样式和起点0。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md
- deliverables/final-specification-set/user-interface/wp17-draw-text-tags.md
- deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md
- deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md

**共享合同**

- WP08本地化后的文本消费
- 消息行满暂停
- 摘要备忘录

**依赖**

- WP17通用UI
- WP15资源访问
- 宿主输入/字体或媒体接口的条件前提

**能力范围引用**

- GR4-CAP-M10-006
- GR4-CAP-M10-020

**关联新问题**

无。

**根因身份**

```json
{
  "id": "GR4-M10-003-ROOT",
  "description": "文本可见行为依赖未移交的分词/折行条件，独立实现无法区分自动逐字折行与保持超宽单行。"
}
```

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "third_round": null,
  "second_round": null,
  "note": "不猜第二轮ID，不据旧PASS判定本轮支持。",
  "independent_scope_assessment": {
    "relation": "new_within_reviewed_scope",
    "related_ids": [],
    "assessment": "M01的本地化参数替换发生在上游文本结果层；本项固定AB输入后的布局，互不合并。没有把旧行满暂停已承接合同重开。"
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

HIGH_STATIC

**未知**

- 真实宿主/媒体/输入未运行；未推断完整Demo可达。
- 真实宿主、媒体、物理输入与完整Demo未执行；外部插件不在固定R证明范围。

**排除的主张**

- 不要求全字符排版算法逐行翻译。
- 不声称默认中文文本、所有长字符串都会实际丢字；字体测量和宿主裁切未运行。
- 不把固定摘要坐标要求成未来框架布局架构。

**用户政策边界**

```json
false
```

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CB",
    "thread_id": "01a13036-2ee9-7e43-8d09-4699ed1b03f4",
    "path": "modules/CB/verdicts.json",
    "pointer": "/records/2",
    "decision": "CONFIRM_WITH_REFINEMENT",
    "reason": "原AB/A B最小反例成立，且消息消费者会依据布局换行插入暂停，故不是要求逐像素复刻。须收紧拟补规则的宽度阈值；只写“超过请求行宽”可能漏掉刚好容纳文字却仍换行的边界。保持P2，精确化并不推翻原缺口，也不另立根因。",
    "required_refinements": [
      "拟补自动折行规则须注明固定参考会预留额外2个测量单位，只有非行首词边界及相应内容条件成立时移词；不得概括为裸文本宽大于行宽才折行。",
      "向量明确普通样式、起点0、自动折行开启和测量夹具；<pg>对照比较逻辑行归属，不宣称两个内部路径绝对像素相同。",
      "正文仅登记固定参考的不硬拆长词行为；未来改善无空格语言排版属于独立兼容政策。"
    ],
    "execution_evidence_assessment": "该候选没有参考行为执行。原模块工具校验只证明产物结构/锚点等，不能证明本候选行为；CB未运行参考函数、行为模型、UI、输入或宿主。以下结果为源码/规格静态核对及条件化推导。",
    "historical_relation_assessment": {
      "relation": "new_within_reviewed_scope",
      "related_ids": [],
      "assessment": "M01的本地化参数替换发生在上游文本结果层；本项固定AB输入后的布局，互不合并。没有把旧行满暂停已承接合同重开。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M10-004 · P2 · REQUIRED — 战斗动画的类型默认映射只有表名和查找顺序，缺少可消费数据

领域 M10；分类 数据或资源契约缺口；独立审者 thread `01a12ff1-a1b1-7212-84b3-c3fdcd6552a9`；辅助证据目录 `modules/M10/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb` · 412–485：18类型×6槽明确指定默认招式身份，未映射按本格/对应单目标/变化/TACKLE回退。（固定R；blob `5df4c2c08d2bcca3063ad9fd104d33df37e75cb7`）
- `Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb` · 492–518：普通动画调用真实消费查找结果；有动画才进入播放。（固定R；blob `5df4c2c08d2bcca3063ad9fd104d33df37e75cb7`）
- `Data/Scripts/011_Battle/001_Battle/001_Battle.rb` · 838–843：正常战斗域包装在showAnims为真调用场景播放。（固定R；blob `ce89d430743e1c1a27e8aab603fdc3be60288fed`）
- `Data/Scripts/010_Data/002_PBS data/005_Move.rb` · 22–55;79–96：登记type/category/target决定分格；raw category与世代physical?/special?不同入口。（固定R；blob `47949c4ca821c591957cbf4ecea370fa6c7f41f6`）
- `Data/Scripts/010_Data/001_Hardcoded data/017_Target.rb` · 26–33;136–141：NearOther目标数1；目标数量/敌侧属性参与分格。（固定R；blob `b00c9a22be53f3cacffaf1d11c4c15e02550a769`）
- `Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb` · 39–53：映射与数据库加载分层，可用缓存为条件。（固定R；blob `b6bddb6730dfa407e3691653a1e7ffa7d50c1812`）
- `PBS/moves.txt` · FLAMETHROWER2603–2613;EMBER2782–2792;SUNNYDAY2819–2827;TACKLE5326–5336：默认数据支持火系特殊单目标样本及回退身份存在。（固定R；blob `fa5dbaf2739b6b6f55ba5cc5d7d599b4a15b68ca`）

**现规格依据**

- `deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md` · §9.4 L251–254：称类型默认表并定义六槽/回退骨架，没有表内容。（固定B；blob `f4167d75f73bb10ac7729ee96dea6aa6de780ffe`）
- `deliverables/final-specification-set/demo-dx/wp74-battle-animation-authoring-and-exchange.md` · §15 L396–399：关联编译与播放侧再次引用同一缺表。（固定B；blob `42b214af3267436755339815ced7d67f67a3add1`）
- `deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md` · BT K36：只给全部缺失的结果，无法确定正常默认命中的身份。（固定B；blob `5dbb1fbed36800c39844a549939b5123c4b3c1c5`）
- `deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md` · §非注册表产物 L67：move2anim产物身份不能替代脚本内的类型默认映射。（固定B；blob `c6623b3200cd2a7ee16af96dd02f628076f423e0`）

**参考实际行为**

例：FLAMETHROWER无精确映射时按其火系特殊单目标格选择EMBER映射；EMBER亦无映射时再尝试火系变化默认SUNNYDAY，最后TACKLE。各被选默认身份在对方侧也优先OppMove再普通映射。默认表含18类型、每类六槽及空槽。

**现规格的说法**

给出“查类型默认表”和查找链，但全正式集未提供该表的身份数据；WP74只是回指，不能确定火系特殊对应EMBER。

**差异/缺口**

缺少决定最终资源身份的固定默认内容；算法名和六槽结构不能代替数据。

**必要前提**

- 普通战斗动画开启，无插件，合法FLAMETHROWER/默认type-category-target记录。
- 已正常得到双方映射与动画集合（条件夹具），FLAMETHROWER无精确映射；EMBER、SUNNYDAY、TACKLE映射指向不同有效动画槽。
- hitNum=0；实际媒体存在/内容不用于证明查找结果，未加载二进制动画。
- 映射10/20/30及对方11均为条件夹具中的有效槽，不是默认媒体真实编号；双方映射容器均有效，排除容器异常的局部救援空结果。

**最小反例**

```json
{
  "input": "己方FLAMETHROWER精确映射空；EMBER→10、SUNNYDAY→20、TACKLE→30；三槽均有效。",
  "reference_output": "选择槽10（EMBER）；删EMBER映射则槽20；再删SUNNYDAY则槽30；全部删才空。",
  "distinguishing_alternative": "只凭当前正式集无法在火系的EMBER、FIREPUNCH或其他默认身份中作出唯一选择。"
}
```

**正常对照**

FLAMETHROWER精确映射存在时直接使用它；这一骨架已有正文支持。

**失败/边界对照**

- 对方侧EMBER存在OppMove→11且普通→10时选11；对方项空才选10。
- 默认身份未登记或该候选无映射时继续；不把资源/数据库存在性与映射选择合并。
- 世代物理/特殊机制变化不自动重写raw类别的动画分格；无需假定全部世代运行已验证。

**独立实现影响**

实现者即使拥有相同动画库和招式数据也无法按正式规格选择相同默认动画，作者为新招式省略专用动画时表现不确定。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-searches.json",
    "search_ids": [
      "animation_defaults"
    ],
    "scope": "全部131正式文件",
    "relevant_contexts_read": [
      "deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md §9.4",
      "deliverables/final-specification-set/demo-dx/wp74-battle-animation-authoring-and-exchange.md §15/16",
      "deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md L67",
      "deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md K35–36"
    ],
    "result": "语义相关命中只有WP67-A表名/骨架、WP74前向引用、加载产物说明和缺失测试；FIREPUNCH/EMBER等表成对标识搜索无映射表。钓鱼公共事件回退和Safari数据是其他功能。"
  },
  "primary_relative_paths_base": "modules/M10",
  "independent_counterevidence": {
    "search_ids": [
      "CB-N04",
      "CB-N04b"
    ],
    "terms": [
      "类型默认|默认.{0,16}动画|动画.{0,16}(默认|回退)|move2anim|EMBER|FIREPUNCH|SUNNYDAY|OppMove|K36",
      "火花|火焰拳|喷射火焰|类型.{0,15}动画|动画.{0,15}(火系|物理|特殊|变化)|单目标物理|多目标特殊|typeDefaultAnim"
    ],
    "scope": "B 固定正式131篇，正文、scope、共享合同、附表和测试全部纳入；各检索文件字节与 git show B 相等",
    "contexts_actually_read": [
      "WP67-A §9.4",
      "WP74 §15/§16",
      "WP03非类产物/交界表；WP04 §5.1",
      "K35/K36；中英文火系身份别名及类型/动画交叉匹配"
    ],
    "conclusion": "实质动画命中只有表名/查找骨架、作者命名编译和全落空测试；英文身份或中文别名的其它命中属于招式效果、天气、钓鱼或演出目录，没有默认类型到身份的可用附表。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CB"
}
```

**下一轮最小修订**

以实现无关附表补18类型×六种用途到默认招式身份/空值的映射，说明原始类别/目标分格与候选存在性门；增加正常默认命中和逐级落空对照。不要复制Ruby表表达式或设计播放类。

**验收标准**

```json
[
  {
    "kind": "SPEC_STATIC",
    "criterion": "正式交付包含完整默认类型映射数据及六槽含义，能独立解析身份。"
  },
  {
    "kind": "DERIVED_VECTOR",
    "criterion": "火系特殊10→20→30→空及OppMove11优先案例给明确输入/输出且NOT_EXECUTED。"
  },
  {
    "kind": "SPEC_STATIC",
    "criterion": "保持精确映射hitNum、默认候选查找、动画数据库/媒体缺失分层；不把结构校验称播放测试。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md
- deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md

**共享合同**

- WP74动画命名编译
- WP03动画产物
- 战斗showAnims开关

**依赖**

- WP17通用UI
- WP15资源访问
- 宿主输入/字体或媒体接口的条件前提

**能力范围引用**

- GR4-CAP-M10-027

**关联新问题**

无。

**根因身份**

```json
{
  "id": "GR4-M10-004-ROOT",
  "description": "缺少决定最终资源身份的固定默认内容；算法名和六槽结构不能代替数据。"
}
```

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "third_round": null,
  "second_round": null,
  "note": "不猜第二轮ID，不据旧PASS判定本轮支持。",
  "independent_scope_assessment": {
    "relation": "new_within_reviewed_scope",
    "related_ids": [],
    "assessment": "M01–M06无同根。M12动画作者域没有相同候选；WP74命名编译是共享前置，不与默认选择数据合并。"
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

HIGH_STATIC

**未知**

- Data/move2anim.dat与PkmnAnimations.rxdata在参考材料中不可用；未反序列化。
- 本文映射号10/20/30/11是条件静态夹具，不代表默认素材库实际编号。
- 参考材料缺可用move2anim/动画集合及媒体；映射槽号为静态夹具，未加载二进制或播放。
- 未来是否采用相同默认身份是政策问题，不由本事实审计决定。

**排除的主张**

- 不要求采用源类/方法/容器组织。
- 不修改参考或决定未来产品必须保留该兼容细节。

**用户政策边界**

```json
false
```

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CB",
    "thread_id": "01a13036-2ee9-7e43-8d09-4699ed1b03f4",
    "path": "modules/CB/verdicts.json",
    "pointer": "/records/3",
    "decision": "CONFIRM",
    "reason": "六槽的名字不能唯一决定火系特殊单目标采用EMBER；没有别处数据可推出这一身份。默认缺专用映射是明示支持的普通查找分支，补完整固定映射是数据合同修订，不是抄写源表表达式或规定新播放架构。P2维持。",
    "required_refinements": [],
    "execution_evidence_assessment": "该候选没有参考行为执行。原模块工具校验只证明产物结构/锚点等，不能证明本候选行为；CB未运行参考函数、行为模型、UI、输入或宿主。以下结果为源码/规格静态核对及条件化推导。",
    "historical_relation_assessment": {
      "relation": "new_within_reviewed_scope",
      "related_ids": [],
      "assessment": "M01–M06无同根。M12动画作者域没有相同候选；WP74命名编译是共享前置，不与默认选择数据合并。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

### GR4-M11-001 · P2 · REQUIRED — 图鉴预览和条目固定请求普通外观的消费规则未进入正式合同

领域 M11；分类 实现信息不足；独立审者 thread `01a13017-c27c-7020-a9f8-9bb66eb74f64`；辅助证据目录 `modules/M11/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb` · 195–227：首次登记和最近见到均可保留异色true（固定R；blob `fb3afe4df6443fd2704958a4ed4664f793c6299f`）
- `Data/Scripts/016_UI/003_UI_Pokedex_Main.rb` · 264–295、417–448、766–768：选中物种预览读取性别/形态，固定普通外观（固定R；blob `536002291f1eb837ab5173933b87c5ea31a5c3a0`）
- `Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb` · 5–67、71–116、139–151、582–617：完整、摘要单种及简略入口均复用固定普通外观刷新；Info、Forms前/后/图标请求false（固定R；blob `c2b43b0ed024526681dc0ecd5d56dbaa8affd972`）
- `Data/Scripts/014_Pokemon/001_Pokemon-related/003_Pokemon_Sprites.rb` · 64–68、253–258：外观参数透传至资源选择（固定R；blob `12da4a054e9cd244039c75e3b427153a676d4c0c`）
- `Data/Scripts/010_Data/002_PBS data/009_Species_files.rb` · 3–34、47–52、86–89、118–120：普通请求不尝试异色目录（固定R；blob `2a2e2fb92e7c05ec3b2f586edfda64cd4eeeaba3`）

**现规格依据**

- `deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md` · ：本次读取的对应行为条款（固定B；blob `664778d344a13628f2f313d9ee62f6bacf020bc7`）
- `deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md` · ：本次读取的对应行为条款（固定B；blob `6054d7b6e30812d922af092fc55bbb0a5e88e509`）
- `deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md` · ：本次读取的对应行为条款（固定B；blob `23c487115d8b01638ed2db062546ef2a58abdc9f`）
- `deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md` · ：本次读取的对应行为条款（固定B；blob `5dbb1fbed36800c39844a549939b5123c4b3c1c5`）
- `deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md` · ：本次读取的对应行为条款（固定B；blob `9561dc1abc078cc26b98caf4480a3cbea5a70847`）

**参考实际行为**

图鉴保留seen-form及末次形态中的异色记录，但主列表选中物种预览与条目刷新只消费保存的性别/形态，图像选择固定为普通外观。完整Info/Forms前图、背图、Forms物种图标及获得后的简略Info同样处理；没有异色浏览切换。普通刷新本身不把末次记录的true改false，进入形态选择器的首轮写入是另一条已经记载的副作用。

**现规格的说法**

WP62描述异色维度与末次三元组、展示消费者；WP66-B说明图像/形态展示及选择器三参写入导致异色默认false，但没有规定选择器以外的图像请求固定false。WP15只给按已提供属性的资源选择与回退。

**差异/缺口**

仅依正式集合不能确定末次异色true时应请求普通还是异色图像；现有通用资源合同允许两种调用方输入，无法唯一复现参考。

**必要前提**

- 固定R，无插件或临时外部改写；合法已见/已拥有BULBASAUR雄性形态0，末次形态为[0,0,true]。可由合法异色个体登记/最近见到形成，不要求执行真实事件。
- 普通图鉴入口资格、地区/物种/metrics/消息/输入/宿主成立；用于区分视觉的假设资源同时提供相互不同的普通和异色前图/背图/图标。本轮这些媒体实际不可得。
- 先检查普通预览和Info，未进入Forms选择器；以直接符合条件的简略条目入口作另一个独立夹具。
- 最小BULBASAUR夹具先不进入形态选择器；若验证首轮另写异色false，另设>1可列形态的独立夹具，不能用单项个体证明该分支。

**最小反例**

```json
{
  "input": "上述末次异色true，打开主列表选中BULBASAUR，随后打开完整Info；不调用形态选择器。",
  "reference": "两处请求普通前图；保存末次异色仍true。独立简略Info同样请求普通前图。",
  "alternative_allowed_by_current_spec": "实现方把末次三元组完整传给通用资源服务，从而显示异色；数据/资格/形式切换描述都可满足，视觉仍偏离R。",
  "evidence_level": "DERIVED_VECTOR",
  "execution_status": "NOT_EXECUTED"
}
```

**正常对照**

相同输入只有末次异色false：仍请求普通外观；读取性别、形态和已见/拥有资格不变。

**失败/边界对照**

仅异色见过可满足形态资格，图像仍普通；若没有普通/通用图而只有异色图，普通请求不据保存true改查异色，最终依WP15普通请求回退/无图合同，不臆测宿主崩溃。进入多项形态选择器后首轮会另将末次异色写false，此已有合同不可冒充进入前的消费规则。

**独立实现影响**

玩家仅见到/获得异色后首次打开图鉴，就可能看到与参考不同的外观；错误会贯穿列表预览、完整条目和简略条目，并可能把正确的异色记录误清除来达到普通显示。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-evidence.json",
    "scope": "all 131 formal Markdown files including appendices, tests and scope",
    "queries": [
      "(图鉴|Pokédex|Pokedex).{0,80}(普通|异色|闪光|shiny)",
      "(异色|闪光|shiny).{0,80}(图鉴|Pokédex|Pokedex)",
      "(忽略|丢弃|固定|强制|不显示|不展示).{0,40}(异色|闪光|shiny)",
      "(普通外观|普通配色|非闪光|non.?shiny)",
      "(last_form_seen|pbUpdateDummyPokemon|setIconBitmap)"
    ],
    "result": "未找到图鉴选中预览/条目图像固定普通外观的承接。命中记录写入、调试登记、摘要红编号、邮件个体快照及通用资源回退，均不补足本调用方的固定参数。",
    "source_counter_search": {
      "scope": "R/Data/Scripts 全部脚本",
      "terms": [
        "class PokemonPokedexInfo_Scene",
        "def pbUpdateDummyPokemon",
        "def setIconBitmap",
        "shiny",
        "DEX_SHOWS_ALL_FORMS"
      ],
      "result": "本固定脚本集只定位这两处图鉴消费者定义；直接读取入口调用和取图透传，未见后续覆写或配置改为采用保存的异色字段。插件未取得、不推断不存在。"
    }
  },
  "primary_relative_paths_base": "modules/M11",
  "independent_counterevidence": {
    "search_ids": [
      "CB-N05",
      "CB-N05b"
    ],
    "terms": [
      "(图鉴|Pokédex|Pokedex).{0,100}(普通|异色|闪光|shiny)|(异色|闪光|shiny).{0,100}(图鉴|Pokédex|Pokedex)|普通外观|普通配色|非闪光|non.?shiny|last_form_seen|pbUpdateDummyPokemon|setIconBitmap",
      "异色|闪光|shiny|末次形态|最近形态|最近见到|最后.*形态"
    ],
    "scope": "B 固定正式131篇，正文、scope、共享合同、附表和测试全部纳入；各检索文件字节与 git show B 相等",
    "contexts_actually_read": [
      "WP62 §2/§3/§4/§6 与 PD03–05/PD19/PD31–34",
      "WP66-B §6/§7，B30/B33/B38",
      "WP15 §4.1；WP17共享图标",
      "WP66-A邮件/摘要；WP21形态提交"
    ],
    "conclusion": "记录异色、通用资源闪光参数、摘要红编号、邮件快照以及Forms选择器首轮写false都有明文；均不能推出未进入选择器的主预览/Info固定请求普通且保持末次true。跨行异色/末次别名补检也未找到该调用方规则。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CB"
}
```

**下一轮最小修订**

在WP62记录→展示交界及WP66-B列明哪些图像请求固定普通外观，保留性别/形态选择和异色记录；明确普通刷新不清记录、Forms选择器才有既有写入。补true/false成对静态向量，并为完整/简略入口交叉引用。只补参考事实，不要求未来沿用同名方法/对象，不自行决定是否改进异色浏览政策。

**验收标准**

```json
[
  {
    "kind": "STATIC",
    "criterion": "仅读正式集合即可判定末次异色true时主列表选中预览、完整Info/Forms前后图及图标、简略Info均请求普通外观。"
  },
  {
    "kind": "STATIC",
    "criterion": "普通预览/Info刷新不改变保存的异色true；与进入Forms选择器首轮写false的已有合同明确分开。"
  },
  {
    "kind": "STATIC",
    "criterion": "有同性别/形态的末次true/false成对向量，及仅异色已见的形态资格对照；不将资源回退误作固定普通选择的原因。"
  },
  {
    "kind": "STATIC",
    "criterion": "不改WP15通用按属性取图合同，不把规则推广到队伍/摘要/战斗个体外观；新向量标记未执行。"
  },
  {
    "kind": "RUNTIME_OPTIONAL",
    "criterion": "不以当前无媒体/宿主阻止事实修订；如后来运行，应另提供正常/异色相异资源、命令输入及实际输出记录，不能把本轮静态推导标成执行。"
  },
  {
    "kind": "SPEC_STATIC",
    "criterion": "普通刷新保留true/false原记录与多项Forms选择器首轮写false分开；多项选择器反向例需独立合法多项夹具。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md
- deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md
- deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md
- deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md

**共享合同**

- WP62记录消费
- WP66-B图鉴UI
- WP15通用物种图像参数与回退；不要求修改通用规则

**依赖**

- 图鉴普通登记/最近见到
- 物种图像与图标资源选择
- 完整/简略条目入口

**能力范围引用**

- GR4-CAP-M11-006

**关联新问题**

无。

**根因身份**

M11-pokedex-record-versus-image-variant

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "third_round": null,
  "second_round": null,
  "note": "GR3-M11-001仅栖息地掩码，独立回归仍支持CLOSED；本项不是重开。未知第二轮关联不猜ID。",
  "independent_scope_assessment": {
    "relation": "new_within_reviewed_scope",
    "related_ids": [
      "GR3-M11-001"
    ],
    "assessment": "旧栖息地格规则与本次资源请求无同根。M04个体取图动态形态与本项共享资源文件，但前者读取个体并可能提交形态，后者只消费记录的性别/形态且固定异色假；不合并。M10未另报同项，WP66-B只是投影。"
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

HIGH_STATIC

**未知**

- 实际图像像素、媒体/宿主效果
- 未来产品是否主动提供异色浏览的政策取舍
- 外部插件行为
- 真实宿主、媒体、物理输入与完整Demo未执行；外部插件不在固定R证明范围。

**排除的主张**

- 不声称图鉴不记录异色
- 不声称普通刷新清除末次异色
- 不把主列表预览误称每行拥有标记图标
- 不声称真实地图/事件已可达或运行成功
- 不判定参考固定普通外观是应修复的游戏bug

**用户政策边界**

```json
false
```

**独立反证与最终裁决**

```json
{
  "decision": "CONFIRMED_AFTER_INDEPENDENT_CHALLENGE",
  "root_adjudicator": "parent /root; 01a12fc2-e8c0-7e43-a721-ccfe659d75c8",
  "independent_counterreview": {
    "task": "CB",
    "thread_id": "01a13036-2ee9-7e43-8d09-4699ed1b03f4",
    "path": "modules/CB/verdicts.json",
    "pointer": "/records/4",
    "decision": "CONFIRM",
    "reason": "独立确认的是记录→资源请求交界缺口。通用按属性资源规则可接受true/false两种输入；现有记录与选择器条款没有规定选择器以外传入固定false。不是图鉴不记录异色，也不是每行拥有标记图标的颜色问题。P2针对多正常入口的可见外观差异。",
    "required_refinements": [],
    "execution_evidence_assessment": "该候选没有参考行为执行。原模块工具校验只证明产物结构/锚点等，不能证明本候选行为；CB未运行参考函数、行为模型、UI、输入或宿主。以下结果为源码/规格静态核对及条件化推导。",
    "historical_relation_assessment": {
      "relation": "new_within_reviewed_scope",
      "related_ids": [
        "GR3-M11-001"
      ],
      "assessment": "旧栖息地格规则与本次资源请求无同根。M04个体取图动态形态与本项共享资源文件，但前者读取个体并可能提交形态，后者只消费记录的性别/形态且固定异色假；不合并。M10未另报同项，WP66-B只是投影。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

