# R5-U05 作者候选：GR5-M09-001

本候选补全生命水滴的独立可恢复评分守卫。预测关闭时，满血目标仍保持局部输入分 100；可恢复的 50/100 目标为 107，75/100 目标为 95。预测、评分和 HP 意识三个标记按各自阶段控制。

状态：`AUTHOR_READY_FOR_INDEPENDENT_REVIEW`，1/1 必修已提供完整静态映射；作者核对不是独立复审 PASS，也不是正式接受或 CLOSED。上游 R5-U04 实际贡献接受门为 `WAIT`。候选准备不受该门阻塞，R5-I 实际整合必须等门满足。

## 固定输入与角色

- 仓库：`y805939188/pokemon-essentials-clean-room`。
- B5：`9366d9d17aaeac3b4414236468affa650fb3dd27`；tree `594e65edcb192a19110540245fc1663bae2de007`；正式 131 文件子树 `d5a462b4c6f8b78c3264a25d6b5495230fa265e2`。
- R：`Maruno17/pokemon-essentials`，commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，定向只读源与完整文件身份已核验。
- 合同冻结：`22fba7786b0090a1955ce6211315b0036cddfbcd`；tree `21f3484d167d8cab7a288e0204c72f275414d52e`。
- 准备发布/候选分支基点：`93524fe5cf396de2bd01f3c5c1e08ba4b874bc68`；tree `4ade8d22d56b7facb46ad5bd8245a027f0d833c6`。
- 语义报告：`c0ff33024aea424c68d29f9778fe7c8e807d21e8`；tree `8390e04b850136d2c7b7d9c970cb23f64d3adf99`。发布证据：`f49d870c6fd616ab6736754a218a4553b5acac7f`；tree `e5dc6aaf626885666e7d472865563f0c9bfbdf46`。
- 独立作者分支：`codex/r5-u05-author-candidate-20261013`。请求参数依合同为 `gpt-6.1-sol / xhigh / default`，禁 Fast；实际模型/推理/速度回显 `UNVERIFIED`，未审计额度或认证。
- 作者工作角色 `/root`；本次真实后台任务 ID 未在执行环境回显，由父任务绑定。来源线程 ID 不是本作者任务 ID，不冒用。没有启动本批审者。

## 修改与验收

`formal/` 下两个完整 B5 镜像构成唯一正文候选。WP52-B §4 只替换生命水滴一行，明确不可恢复时保持 s、仅可恢复且 HPAware 开才算比例；§7 同步 BE 数量/目录。测试目录新增 B64–B71，共同夹具与 8 条对照均标 `DERIVED_VECTOR`。

| 必修标准 | 作者核对与落点 |
| --- | --- |
| C1：独立守卫与预测门分列 | WP52-B §4 的 LIFEDEW 行逐阶段写出三个资格拒绝与 s 保留；B64/B67 给预测关闭的可达反例 |
| C2：满血、50%、75%、预测开、盟友封锁、使用者封锁 | B64/B65/B66/B68/B67/B71 分别给 100/107/95/NOT_ENTERED/100/候选先拒 |
| C3：HP 意识/评分关闭及阶段边界 | B70 保持 100；B69 不进评分体；所有案例限定局部，不推最后动作 |
| C4：收窄原表述 | B5 表述允许在分离门下导出 95，不能唯一复现 100；不声称每个实现者必然减 5 或最终选错 |

完整逐标准、向量、正常/失败/取消/部分提交与消费者映射见 [finding-responses.json](finding-responses.json)。[formal-diff.patch](formal-diff.patch) 以 B5 正式路径为目标，可在隔离目录重放并逐字节得到镜像。这里只提供候选，未修改正式正文或公共登记。

## 反向保护与消费者

固定 R 的目标失败预测和目标效果评分分别读取可恢复资格。SkillLevel32 配 AntiPredictMoveFailure 可正常保留 ScoreMoves/HPAware；默认 LIFEDEW 是同侧多目标，满血不属于普通可选招拒绝门。封锁盟友对照使用未封锁 U；U 自身封锁会更早拒候选，倒下目标不进入普通存活目标枚举。

丛林治疗的既有错族调用、B26 状态项、真实 WP46 的治疗写入以及 WP52-A/51 的通用修正、平均、多目标偏好、权重和动作登记保持。局部 s 保留不表示整条候选最终为 s。新规则不推广到其它治疗评分族；局部评分不提交 HP/状态/PP/物品或行动，也不把整个 AI 准备过程说成无副作用。

没有本局部菜单取消或 HP 部分提交案例。更早候选拒绝、预测排除和评分关闭按其各自阶段保留；评估准备可能写临时类型/忽略能力状态，既有异常/已写前缀规则继续由 WP52-A/51 承接，未添加全链回滚保证。精确旧回归关系见 [regression-results.json](regression-results.json)：GR3-M09-001 的 OPTIONAL/DEFERRED、旧 U08 未启动保持，不转签历史 PASS。

## 复现与复审入口

在仓库根运行：

```text
python review/remediation-fifth-20261013-prepare/candidates/R5-U05/author/verify-candidate.py
```

该工具仅检验 JSON、字节/hash/blob、限定范围、旧向量字节和 patch 重放，归 `TOOL_VALIDATION`；不执行参考或行为模型，不代替独立语义验收。候选 commit/tree 和 manifest 自身身份由父任务从本次推送返回绑定，避免自哈希递归。

独立审者入口：[contracts/R5-U05/reviewer-entry.md](../../../contracts/R5-U05/reviewer-entry.md)。父任务提供本候选固定 commit/tree 后安排非作者审查；实际字节复审另依 actual-reviewer-entry，候选签名不得转签。

## 保留边界

本 update 新增参考/模型/宿主/Demo 行为执行 `0 / NOT_EXECUTED`。R4 历史隔离执行 4 条与 R5 review 新增隔离执行 4 条分别保留，未重新执行或计为本候选行为证据。最终选招/权重分布、默认训练家样本是否配置 AntiPredictMoveFailure、原生宿主/完整 Demo/媒体及任意插件组合仍未验证。optional7、no-required7、政策6 与 M11-005 内 optional 方面均未纳入本必修。没有合并 main、删分支、修改参考/冻结历史、公共登记或访问 Mac。
