# R4-U05 完整冻结finding任务正文

### GR4-M12-001 · P3 · REQUIRED — 遭遇整集复制未承接空类型被丢弃而步数率保留的边界

领域 M12；分类 数据或资源契约缺口；独立审者 thread `01a12ffe-6148-76d0-8038-a1eb8e8bf390`；辅助证据目录 `modules/M12/`。当前状态CONFIRMED，只授权事实修订，没有应用任何正式修改。

**源依据**

- `Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb` · 69–99;139–154;187–234;256–339：整集复制全部步数率但跳过空类型；单类型复制始终建立目标类型；正常新类型可零槽返回（固定R；blob `97c7f39247411587d204a432eb5f7c99b76769e5`）
- `Data/Scripts/010_Data/002_PBS data/013_Encounter.rb` · 62–68：初始化直接接收概率和类型，不补回遗漏键（固定R；blob `e69d300dd0e21690e5970452017e4c2bd457021a`）
- `Data/Scripts/010_Data/001_GameData.rb` · 78–85：登记只建立记录（固定R；blob `ccfd971a29b3bab107e2da6865ac0050ed3256b0`）
- `Data/Scripts/010_Data/001_Hardcoded data/013_EncounterType.rb` · 29–33：Land默认率21（固定R；blob `79cbafb8bd3e5e827cd09b6ca070a13bb70d94aa`）
- `Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb` · 1163–1169：调试菜单直接调用遭遇编辑器，未另加数据清理（固定R；blob `6dd0c35a31040174efadefa2ba24a1c85a2499f9`）
- `Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb` · 423–438：空槽类型在后续PBS写出也会省略，但这是另一步（固定R；blob `be1b3de320d0635d7eca1e24332973344188b53c`）

**现规格依据**

- `deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md` · §6.1 line73/§6.2 line80：本次核对条款（固定B；blob `f75fa5a23f157f434e3e57da69757e4a429a0edc`）
- `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md` · WE-M11 line85：本次核对条款（固定B；blob `255464a58f8e45e30ca1807250926aa47e0791a6`）
- `deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md` · §6.4 line91：空槽类型不输出限定PBS往返，未覆盖编辑器Copy（固定B；blob `f75fa5a23f157f434e3e57da69757e4a429a0edc`）

**参考实际行为**

正常作者流程新增遭遇类型后可不加槽直接返回，源集仍显示该类型(x0)。整集Copy逐项复制所有步数率，但不为零槽类型建立目标类型条目；目标只剩该率而无该类型，原集不变。单类型Copy不同：即使源零槽也先建目标空类型。

**现规格的说法**

WP73-B§6.1只说明复制步数率和各槽内容、保持编辑独立及后缀；WE-M11无输入限制地称深拷贝。没有说明空类型不复制和步数率残留；§6.4的空槽省略专指随后PBS写出。

**差异/缺口**

一个可由正常编辑流程到达的结构过滤分支未明确，独立实现通常会保留空类型，从而与参考的目标编辑列表/可新增类型集合不同。

**必要前提**

- 固定R、调试菜单或合法直接编辑入口，合法地图列表和窗口宿主
- 原集地图5版本0，Land已注册且步数率21，槽数0（新增类型后立即BACK可达）
- 目标地图7版本1未占用；Copy成功，尚未退出总保存门；无插件/外部修改

**最小反例**

```json
{
  "input": "原集仅含Land类型(0槽)、Land率21，整集复制至空闲(7,1)",
  "reference_output": "原集保留Land(0槽)；目标类型列表没有Land，而步数率仍有Land=21，后缀保留。打开目标可再次新增Land。",
  "naive_spec_output": "按WE-M11无条件深拷贝，目标也显示Land(0槽)，新增类型列表排除Land。",
  "evidence_level": "DERIVED_VECTOR",
  "execution_status": "NOT_EXECUTED"
}
```

**正常对照**

Land含一个合法非空槽时复制保留类型和独立槽副本；同图同版本冲突仍拒绝。

**失败/边界对照**

这是合法空槽边界而非异常。反向对照：在同一集把空Land类型复制到未用Cave类型，参考保留Cave空类型及复制率。复制本身仅登记，退出No仍按原档案重载；不声称产生真实遇敌差异。

**独立实现影响**

编辑器复制结果、类型(x0)显示、可再次新增类型的集合以及保存的登记结构可不同；不影响已有非空槽复制正常结论，限P3。

**已完成的反证**

```json
{
  "primary_review": {
    "artifact": "negative-evidence-search.json",
    "scope": "全部131正式Markdown含正文/附表/测试",
    "terms": [
      "遭遇集|encounter set|pbEncountersEditor|WE-M11",
      "空槽类型|空类型|空遭遇|empty encounter|empty.{0,20}slots?",
      "复制.{0,25}(遭遇|步数率)|遭遇.{0,25}(复制|拷贝)|Copy.{0,25}encounter"
    ],
    "contexts_reviewed": [
      "WP73-B§6.1–6.5/§10–11",
      "WE-M11–13",
      "WP04遭遇概率往返",
      "WP36空表/编译/快照合同"
    ],
    "result": "没有条款说明整集Copy丢空类型但留概率；查得空槽省略只在PBS输出。源端检查唯一编辑定义、菜单caller、登记构造及单类型Copy，未发现补回空键的路径。"
  },
  "primary_relative_paths_base": "modules/M12",
  "independent_counterevidence": {
    "search_ids": [
      "CB-N06",
      "CB-N06b"
    ],
    "terms": [
      "遭遇集|encounter set|pbEncountersEditor|WE-M11|空槽类型|空类型|空遭遇|empty.{0,20}(encounter|slot)|复制.{0,25}(遭遇|步数率)|遭遇.{0,25}(复制|拷贝)|Copy.{0,25}encounter",
      "(遭遇|类型|步数率|触发概率).{0,30}(空|复制|拷贝|过滤)|(空|复制|拷贝|过滤).{0,30}(遭遇|类型|步数率|触发概率)|WE-M1[123]"
    ],
    "scope": "B 固定正式131篇，正文、scope、共享合同、附表和测试全部纳入；各检索文件字节与 git show B 相等",
    "contexts_actually_read": [
      "WP73-B §6.1–6.5/§10–11",
      "WE-M10–14",
      "WP04 §5.5",
      "WP36 §3.1–3.2.1/§9",
      "WP73-A空集合与校验分界"
    ],
    "conclusion": "未找到整集Copy滤空类型但保留率的条款。WP04/WP73-B省空类型明确是PBS输出，WP36空表是运行消费者。WE-M11无非空前提的深拷贝表述无法唯一得出目标列表无Land。",
    "artifact": "negative-evidence.json"
  },
  "counter_relative_paths_base": "modules/CB"
}
```

**下一轮最小修订**

在WP73-B整集Copy条款补充零槽类型不建立目标条目、概率照复制；显式区分单类型Copy。限定WE-M11非空正例并补一条空类型与概率残留静态对照。保持参考事实，未来保留或修正该行为由后续政策选择，不修参考。

**验收标准**

```json
[
  {
    "kind": "static",
    "criterion": "整集空Land21复制后原集不变、目标无Land类型而Land率21存在；保留后缀和未保存状态层次。"
  },
  {
    "kind": "static",
    "criterion": "给出非空Land独立复制和单类型空Land→Cave仍保留空类型的反向对照。"
  },
  {
    "kind": "static",
    "criterion": "不把PBS写出时省空类型当成本次编辑Copy行为，不扩大为运行/遇敌差异。"
  },
  {
    "kind": "runtime",
    "criterion": "本修订验收不要求宿主运行；若后来执行必须独立记宿主/素材/夹具，不冒用本轮证据。"
  }
]
```

**受影响正式文件**

- deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md
- deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md

**共享合同**

- WP04 PBS反写与WP36当前地图快照只作相邻消费；无需修改其正确规则

**依赖**

- WP73-A通用选择器
- GameData遭遇登记
- WP72编辑器入口

**能力范围引用**

- GR4-CAP-M12-005

**关联新问题**

无。

**根因身份**

M12-encounter-set-copy-empty-type-filter

**旧GR3/229/341关系**

```json
{
  "relation": "new",
  "gr3_related_ids": [],
  "second_round_relation": null,
  "note": "GR3-M12-001/002为BMP与结算累计，不同根因；不重开历史CLOSED。第二轮关联未追认。",
  "independent_scope_assessment": {
    "relation": "new_within_reviewed_scope",
    "related_ids": [
      "GR3-M12-001",
      "GR3-M12-002"
    ],
    "assessment": "BMP材料与评级累计是不同根因。M01–M06无编辑器整集筛空候选，不与翻译逐项合并、遗传或运行遭遇规则合并；不重做旧回归签署。"
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

high on source branch; bounded P3 documentation sufficiency judgment

**未知**

- 当前完整编辑器宿主表现未运行
- 是否有下游自定义插件补回类型未知
- 真实宿主、媒体、物理输入与完整Demo未执行；外部插件不在固定R证明范围。

**排除的主张**

- 不宣称参考必须修bug
- 不宣称所有Copy错误或会丢非空槽
- 不宣称当前地图遇敌率立即改变
- 不把当前缺完整Demo归为本发现缺能力

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
    "pointer": "/records/5",
    "decision": "CONFIRM",
    "reason": "原报告的有效输入可通过编辑器正常新增/立即返回得到；没有登记构造或caller补回被滤掉类型。缺口有限且不影响非空复制正确规则，P3维持；无需把参考过滤当作未来引擎永久要求。",
    "required_refinements": [],
    "execution_evidence_assessment": "本候选为SOURCE_STATIC/SPEC_STATIC/DERIVED_VECTOR，未执行。另读M12 rating-probe.rb及rating-execution.json：回执是Ruby2.6.10隔离评级/结算，绕过队伍构造，无编辑器调用，不支持本候选也不是随附Ruby3.1宿主实测。CB只评价该回执可支持范围，不重跑或重新认证其数值。",
    "historical_relation_assessment": {
      "relation": "new_within_reviewed_scope",
      "related_ids": [
        "GR3-M12-001",
        "GR3-M12-002"
      ],
      "assessment": "BMP材料与评级累计是不同根因。M01–M06无编辑器整集筛空候选，不与翻译逐项合并、遗传或运行遭遇规则合并；不重做旧回归签署。"
    }
  },
  "root_judgment": "已阅读完整事实、前提、反证和范围；采纳具名精确化，保持仅事实规格修订，不重开旧CLOSED或冒运行证明。",
  "severity_change": null,
  "formal_revision_applied": false
}
```

