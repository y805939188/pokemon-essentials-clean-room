# R7-U08 独立云端author派发

只执行本次具名角色，不创建子任务或其它作者/reviewer。父会话唯一负责 cloud_threads.create；无用户设置的并发数量上限，但不要把可并行当成已创建或服务slots证明。父会话已报告U01=01a13f52-add1-7706-b7ec-54e07e0d7013、U04=01a13f52-cc74-7568-9e75-85ac773c6015、U05=01a13f52-ecf8-73f9-8c9b-f5c164f0c017为inProgress，不重复创建它们。其它批次以父会话真实task登记去重；本静态派发文本不是创建回执。

本角色请求 gpt-6.1-sol / xhigh / service_tier=default 普通速度，禁Fast。模型/档位/速度的实际有效回参缺失时逐项UNVERIFIED，不以请求argv、自报或成功退出认证配置，不查额度/认证。实际task/context/PID、请求、UTC、完整可发布工具I/O和退出分开留存；私有模型流不作为公共证据推送。

仓库 https://github.com/y805939188/pokemon-essentials-clean-room.git 。输入远端分支 `codex/remediation-seventh-20261015-cloud`；固定准备提交 `4bd152023b4bcb3dd5a3654deffe75aeebc40f10`。行为基线B `e646432c644dec04d306842cc5a559a29c718fbc`，正式tree ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c。参考固定R为 Maruno17/pokemon-essentials 的8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/tree7589c800b61ba13a13040ed0d686979b80a84fd0。只在云端工作，不操作用户Mac，不用浮动HEAD替代固定输入。先读实际项目AGENTS.md。

原完整七组合同：提交 `f622356f3beb9e84ea8cff9db07c7fb382565d3f` 的 `review/remediation-seventh-20261015-prepare/delegation/contracts/R7-U08.json`。
原角色入口：同提交 `review/remediation-seventh-20261015-prepare/delegation/prompts/R7-U08-author.md`。
固定恢复工具：提交 `658488c81f1f3181a488298ab27850c8af951d73` 的 `review/remediation-seventh-20261015-prepare/tools/restore_container_context.py`。
逐批证据恢复清单：同提交 `review/remediation-seventh-20261015-prepare/recovery/batches/R7-U08.json`。
跨容器说明：同提交 `review/remediation-seventh-20261015-prepare/recovery/independent-containers.md`。
上述固定文件可由 `https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/<完整固定commit>/<精确路径>` 读取，不必下载80MB Manifest或扫描完整core包。先完整阅读工具和本批清单再执行；不盲跑下载程序、不执行恢复出的参考/native程序。

独立容器不共享整合者本地目录。将工具和本批清单分别保存为 `/workspace/r7-bootstrap/R7-U08-author/tools/restore_container_context.py` 与 `/workspace/r7-bootstrap/R7-U08-author/recovery/batches/R7-U08.json`，运行：

```bash
python3 /workspace/r7-bootstrap/R7-U08-author/tools/restore_container_context.py --plan-directory /workspace/r7-bootstrap/R7-U08-author/recovery/batches --batch R7-U08 --destination /workspace/r7-context/R7-U08-author
```

工具定向恢复本批原载荷、身份/原绑定及L01-L14、固定源/正式读输入和冻结合同/Prompt。原 `/workspace/r7-evidence` 映射到 `/workspace/r7-context/R7-U08-author/evidence`；原 `/workspace/r7-reference` 映射到 `.../inputs/reference`；固定正文在 `.../inputs/project/`，原入口在 `.../dispatch/delegation/`。这些只是有界文件快照，不是完整Git checkout或运行认证。已有匹配恢复可复用；连接中断保留目录、同环境同目录加--resume，不覆盖冲突字节、不另起替代任务。有新的具体可读依赖应具名定向补取，不能伪标limit。

规格只描述可供从零重写的独立功能、逻辑、行为，不实现引擎/TypeScript包/适配器，不移植Ruby结构或复制源表达式。完整前提、普通对照、取消/异常/部分提交、最小规则、正确保留scope、消费者和历史回归按原七组及已接非作者反证审读，不复活已被反证排除的宽提案。7 optional、2额外导航facet、1 no-required、2 policy均未采用；同一必修的条件同步须给具体矛盾和依据，不自动扩大。

L01-L14和旧56/92关闭边界保持。SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION、REFERENCE_OBSERVATION、独立完整模型、游戏宿主/Demo/native媒体/真实存档回放分开。未执行向量保持NOT_EXECUTED，身份/退出0不替代语义验收。有效配置UNVERIFIED，宿主等0不得提升。进度分母固定27项/13批；只有R7-I写正式正文、公共台账和整合分支，不改main/tag/旧证据、不force、不提前关闭依赖问题。

本批必修：GR7-M13-001、GR7-J16-001、GR7-J16-002、GR7-J16-003。作者前置批次：无；所有作者仅写各自镜像，可同时准备，不能因此同时覆盖共享正式文件。

## GR7-M13-001

{
  "最小行为合同": "WP67-A的颜色请求应以动画当下显示HP h和总HP T判断：h≤floor(T/4)为红，否则h≤floor(T/2)为黄，其余绿。不能先把h取整，不能用最终HP或精确分数阈值替代。",
  "正确保留范围": [
    "不把数字显示的临时整数用于颜色；数字显示开关与颜色独立。",
    "保留约1秒等待、EffectsOff仍进行HP动画、宽度比例及偶数取整；队伍/摘要条和图标不随本项改。",
    "本次接受的是静态数值与颜色请求，不继承B17/U05/R4的全局PASS。"
  ],
  "禁止扩大": "本中文视图不得复活已被反证排除的普通游戏故障、统一事务、宿主成功或未来架构强制。"
}

{
  "验收条件": [
    "正文、目录及必要同步只陈述本记录最小行为合同，所有保留范围均不变。",
    "按下列具名前提/普通对照/取消/失败/部分提交分别核验；执行阶段按第七组真实证据标记。",
    "后续实际变更须由非作者核验，根接受中文视图不等于已经修订或关闭。"
  ],
  "回归向量与可判观察点": [
    "T101：51→50在t0.5/1分别h50.5绿、50黄。",
    "T101：26→25在t0.75/1分别h25.25黄、25红。",
    "T100与T101整数边界、数字显示开/关、EffectsOff各作独立对照。"
  ]
}

## GR7-J16-001

{
  "最低合同": "最低必要修订为WP67-B L141的一句顺序限定。全文§2把音乐纳入演出，§7.1又把BGM列为演出首项，因此“先于演出”不能在未说明的情况下改读成“先于逐成员视觉”。该句与非空音乐的静态请求次序相反。",
  "精确必修级别": "MAIN_TEXT_ORDER_WORDING_ONLY",
  "必须保留": [
    "克隆和默认蛋收录",
    "正/负/0上限及每次只删一届",
    "累计编号不回退与PC门",
    "无取消、无自动保存/片尾",
    "记录先于视觉滑入",
    "实际媒体/宿主未知"
  ],
  "排除写集": [
    "L22等正确向量无需改写；不要求新增全局测试ID。",
    "reference/**；WP23；WP67-A；旧报告、旧资格、公共台账。"
  ],
  "未来政策": "无需决定未来是否修复参考；这是文字顺序校正，不要求未来重现宿主错误。",
  "不扩张": "不以中文翻译升级RGBA或新增净化规则；原作者错误经验driver只保留原字节，由C14真实283–293取代支持定位。"
}

{
  "全组具名向量": [
    {
      "id": "C14-HOF-A",
      "given": "非空音乐、初始[]/0，观察首逻辑BGM请求入口",
      "expected": "历史[]/编号0；未登记",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-HOF-B",
      "given": "同一请求正常返回，登记正常完成",
      "expected": "克隆一届/编号1，再视觉成员链",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-HOF-C",
      "given": "独立空音乐配置",
      "expected": "无该请求；仍可登记并先于视觉链",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-HOF-D",
      "given": "条件化请求内异常且不返回",
      "expected": "未到登记；此前资源/音频侧状态不承诺回滚或清理",
      "execution": "NOT_EXECUTED"
    }
  ],
  "限定": "原全部向量NOT_EXECUTED；验收只覆盖最低文字/测试前提及正确保留范围，后续实际更改另由非作者核验。"
}

## GR7-J16-002

{
  "最低合同": "最低必要修订是WP67-A L196和L248去掉不受支持的白色断言（改为“0.2秒闪光”即可）。可选再登记蓝青色RGBA请求，但不能要求白色或蓝青色最终像素。",
  "精确必修级别": "TWO_LOCAL_COLOR_WORDS_ONLY",
  "必须保留": [
    "1.75秒比例与满槽名义0.2秒",
    "经验先提交和逐级顺序",
    "满槽音效/等待门",
    "无条立即完成",
    "动画开关Off仍播放",
    "像素/素材/宿主未知"
  ],
  "排除写集": [
    "不改K22/K35、不新增强制像素断言。",
    "reference/**、经验公式/成长/学招/HP颜色规则、旧资格及公共台账。"
  ],
  "未来政策": "没有新增未来兼容政策；最低修订只是撤回无证白色断言。",
  "不扩张": "不以中文翻译升级RGBA或新增净化规则；原作者错误经验driver只保留原字节，由C14真实283–293取代支持定位。"
}

{
  "全组具名向量": [
    {
      "id": "C14-EXP-A",
      "given": "玩家单席位，从区间0/331到331/331，前序正常",
      "expected": "本框及正常未释放子精灵收到RGBA64/200/248/192及名义.2秒请求；不认证像素",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-EXP-B",
      "given": "同框只到100/331",
      "expected": "无满槽闪光；原增益声音与结束门保持",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-EXP-C",
      "given": "多席位或对方无条",
      "expected": "经验动画立即完成，无满槽请求",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-EXP-D",
      "given": "满槽SE或某个闪光请求内条件化失败",
      "expected": "只保留已提交经验/已交付前缀，不保证所有子精灵或统一恢复",
      "execution": "NOT_EXECUTED"
    }
  ],
  "限定": "原全部向量NOT_EXECUTED；验收只覆盖最低文字/测试前提及正确保留范围，后续实际更改另由非作者核验。"
}

## GR7-J16-003

{
  "最低合同": "L13是输入→推导预期表中的单条向量，输入只给“存在合格组”，不足以保证完整存放/清中心后续，更不足以保证有下一组询问。最低必要是仅收紧L13的前提或把预期缩到入口/条件后续；WP23、WP67-B和L16/L17无需改写。",
  "精确必修级别": "TEST_VECTOR_PREMISE_AND_CONDITIONAL_SUFFIX_ONLY",
  "必须保留": [
    "旧跨级失败及部分提交",
    "同级S0/遗迹石对照",
    "双满正常返回仍清中心",
    "选择链正常UI/特殊负位置/直接调用三层",
    "下一组拒绝只停止后续",
    "资源/错误呈现/清理未知"
  ],
  "排除写集": [
    "WP23、WP67-B主文均正确，不改。",
    "L16/L17/L18/L19、SH38/39/43/44/45保持原义，不新增重复领域测试。",
    "reference/**、原裁决、旧资格及公共台账。"
  ],
  "未来政策": "不决定未来是否兼容缺操作错误；只保持参考静态事实及既有政策边界。",
  "不扩张": "不以中文翻译升级RGBA或新增净化规则；原作者错误经验driver只保留原字节，由C14真实283–293取代支持定位。"
}

{
  "全组具名向量": [
    {
      "id": "C14-PURIFY-A",
      "given": "一合格Pikachu L10/E1000/G0/S500，默认包装，前序正常",
      "expected": "目标1400；实际前缀到L11/E1331，首窗更新失败；未精确写1400、未存放/清中心",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-PURIFY-B",
      "given": "同一夹具仅S0，前序/存放正常返回、拒绝昵称、一组",
      "expected": "可存放/清中心；无下一组询问",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-PURIFY-C",
      "given": "两合格同级S0组，第一组前序/存放正常返回，拒绝switch sets",
      "expected": "第一组清中心，第二组保留，关闭并停止",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-PURIFY-D",
      "given": "同级S0确实到通用存放且双满，提示正常返回",
      "expected": "存放未成功仍清中心；不把前提收紧为必须成功",
      "execution": "NOT_EXECUTED"
    },
    {
      "id": "C14-PURIFY-E",
      "given": "同跨级数值改由遗迹石包装，窗口与后续正常",
      "expected": "不在相同缺更新点失败；等级辅助正常返回后才精确写1400",
      "execution": "NOT_EXECUTED"
    }
  ],
  "限定": "原全部向量NOT_EXECUTED；验收只覆盖最低文字/测试前提及正确保留范围，后续实际更改另由非作者核验。"
}

精确允许写集仅为下列完整候选镜像及本批 `evidence/author/`：

- required: `candidates/R7-U08/deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md`
- required: `candidates/R7-U08/deliverables/final-specification-set/user-interface/wp67-a-battle-interaction-and-presentation.md`
- required: `candidates/R7-U08/deliverables/final-specification-set/user-interface/wp67-b-lifecycle-presentations-and-history.md`

冲突组：CG06。父会话/R7-I使用固定 `f622356f3beb9e84ea8cff9db07c7fb382565d3f` 的 `review/remediation-seventh-20261015-prepare/delegation/conflict-groups.json` 中各实际路径和当前完整合同判定共享接收，候选隔离不等于正式合入无冲突。

在自己的独立容器/checkout从固定B `e646432c644dec04d306842cc5a559a29c718fbc` 创建唯一成果分支 `codex/r7-u08-author-20261015-wave1`。如存在同名分支、未发布成果或父会话已登记本批实际task，先核HEAD/status/远端并保护原成果，不覆盖、不reset、不force、不自换替代分支；若共享整合者工作树，不切换其分支，回报父会话取得隔离工作树。

本派发按本轮普通提交/推送授权和父会话要求，**仅覆盖旧精简入口“不提交/不推送”的成果传输限制**：可普通提交本批candidates镜像及证据，只普通push至 `codex/r7-u08-author-20261015-wave1`。与B的差异必须全部位于 `candidates/R7-U08/`；不夹带bootstrap、恢复输入、其它批次、正式文件或公共台账。不得推送整合分支或main，不合并main、不移动tag。原行为合同和验收范围未改变。

以固定B原字节建立完整镜像，定点修订最低规则。交 `candidates/R7-U08/evidence/author/report.md`、`per-id.json`、`artifact-manifest.json`：逐文件原B/新bytes/SHA/blob、精确scope/读写集、全部必要向量的阶段/结果、失败/取消/部分提交、未满足依赖、真实task/context、请求与实际配置资格、命令I/O和退出。新文件必须进入候选提交，不只回报容器绝对路径。

返回真实候选commit/tree、唯一分支、普通push和逐新文件完整远端读回证据；完成后冻结停止写入。只报告 CANDIDATE_READY_NOT_REVIEWED，不自称独立PASS、ACCEPTED或CLOSED。R7-I核完整差异/身份后生成candidate-input.json，再由不同实际context的ultra reviewer审候选；之后R7-I逐条整合，再由新的R7-IR审实际整合字节。候选PASS、整合PASS、ACCEPTED、CLOSED分开，共享接收和直接/传递依赖/历史回归未满足保持OPEN。
