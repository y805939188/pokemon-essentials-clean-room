# legacy_g1 恢复结果（S01–S05）

**用途原文已实读60/60事件；完整事件签收仍为 INCOMPLETE。UPDATE_NOT_STARTED。** 本恢复替代原未交付入口，不增加独立票，不替父协调签 task-final。

固定合同 `2d44dafe215842de6355f46de7d4d273d8b4c264`，原目录 `tasks/receive_external_legacy_manifest_currentness/` 的 dispatch 与 S01–S05 prompt/readset。目标 C `93d7df7f66adcaa25811fd6ff09352b754577af0`，workspace tree `dd8105c747b6f66663d9f63254a686594791cae8`，原目标任务 tree `e4e557611f94473568b69b7f1a6608896f700128`。B8 `fd1df570cad987dc3852a3b958f03916e317f7fe` / formal tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`；R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。本机路径分别为 `/workspace/pokemon-essentials-clean-room` 与 `/workspace/pokemon-essentials`。

实际环境回显 context/session 均为 `01a144ee-2560-737b-991a-fa11fc09202e`，区别于目标作者 `01a143c7-a558-738e-9580-11a8f12d903f`、原有限入口 `01a1448d-da42-75d4-8fe6-ced9ef75a012`。没有 spawn。model/effort/tier/speed/Fast实际配置逐项 UNVERIFIED，不把用户请求或来源线程当运行证明。

## 原任务复用与实际增量

首次远端读取原分支为合同 C `2d44dafe…`，没有 `shards/S01–S05` 成果；恢复分支当时不存在。以该 C 建立 `codex/r8-recovery-legacy-g1-20261016`。提交前、发布后再读原 ref；结果见 `remote-verification.json`。原分支若后续交付，父协调按事件ID/原文字节去重，本次新增票数为0。

独立bare从远端fetch固定目标，再按readset恢复33普通载荷，共3,736,917B；集合及每文件mode/blob/bytes/SHA全部匹配。只保留本次身份凭据与可复现查看工具，不提交原行政载荷副本，也不执行恢复的旧脚本。当前正式路由与固定provider输入的身份核对另见interfaces；这些验证均不授语义信用。

| 分片 | 事件 | 内容段 | 内容字节 | 实读结果 |
| --- | ---: | ---: | ---: | --- |
| S01 | 15 | 89 | 31,192 | LM-E016–030原文及完整事件用途字段已读 |
| S02 | 13 | 81 | 31,159 | LM-E031–043原文及完整事件用途字段已读 |
| S03 | 9 | 68 | 28,978 | LM-E044–052原文及完整事件用途字段已读 |
| S04 | 11 | 90 | 31,833 | LM-E053–063原文及完整事件用途字段已读 |
| S05 | 12 | 53 | 30,966 | LM-E064–065、073–082；摘要与详细段均读 |
| 合计 | 60 | 381 | 154,128 | 559物理行/159,470B；用途原文未读0 |

这些人口重叠，不相加为需求数。五份附件精确相同，只给一次实际阅读信用；独有分片前缀均逐份读。已全文读global prompt、适用AGENTS与review-SKILL；skill说明其不适用审计报告，本次没有修订正式正文或整改prompt。

## 实质接收

[event-notes.tsv](event-notes.tsv)是60个逐事件人工判断；[reception-ledger.json](reception-ledger.json)绑定原文范围/字节/SHA、具体后继、当前正式路由及未接接口。未删旧错误、取消/失败/部分提交、旧WAIT/ReviewPending或后继澄清。段落用途的共同资格字段读一次；每段reason/后继/路由与所属事件逐项相等，无例外。混合段的业务文字均按完整原段读取，身份字段的typed处置不豁免其余文字。

已接收的现行用途是版本恢复、原输入限定批准出处、修正链及回归线索。正面依据是manifest第3–4/4115–4127行、B21 README/scope第7行、当前交付入口及extraction-plan第3行；既不能把整个manifest废为无用行政，也不能把旧批准传给B8。旧禁止提交/停止条款是原阶段记录，当前授权以本次恢复指令为准。

另外实读固定WORLD/WORLD-INTERPRETER的12个完整选定记录，逐pointer确认与固定 `30cfed0996003b6ebf4b5c51cc04f31ca9255440` 原件相等，并核了以下五条必要R定义到结束行、实际caller/receiver与B8条款：

1. 事件201排队后两场景消费者保留游泳；直接省参调用取消游泳。骑行独立查目的地，跨图进入通知才可能强制上/下车。
2. 运动开始写逻辑坐标/距离/条件离格；正常完成后的合格玩家入口才加全局步数。强制路线/解释器早退与通知后部分提交保留。
3. 跟随实际location入口与strict能力不同；同轴一/两格按许可尝试，其余非重合直接定位。临时through只在正常返回恢复，持久记录在每次正常调用后写回。
4. SystemExit/类名Reset原样抛，普通异常成为带事件上下文错误；不意味成功、全回滚或宿主最终呈现已验证。
5. 显式缺图按音频分期，路径无选图恢复；读档重建的ENOENT才有调试选图/取消退出与非调试报错。nil事件集合与存在的空集合不同。

精确源/规范范围、实际输出chunk及范围SHA见[reading-ledger.json](reading-ledger.json)，有限事实见[interfaces.json](interfaces.json)。完整记录中的其他副断言、全部WORLD域、全部S01事件均未因此升级通过。N01后继E066–072完整原文已作为依赖读；仅接收固定H001反证的文档资格理由，未借其作者阅读声明签全部N01源或额外独立票。

## 本次发现的接收证据问题

- **REC-G1-METADATA-01**：目标LM-E050–052用途说明把WP48/49称为“物品/AI”；原文明确为特性计算修正/阶段触发。逐事件记录已纠正接收含义；原用途表保持原字节。它不证明正式规格错误，不新增正式required。
- **REC-G1-RANGE-01**：E-V2-WP11写166–194，但同一固定文件仅190行，完整文件身份仍匹配。本次实读166–190，越界报错保留；不存在的191–194不能获得已读信用，其余五份B8条款已另批补读。
- **R8-LMC-H001**：固定counter全文的最强NO_REQUIRED理由是父B21明确保留旧待审时点。支持该有限文档资格理由；不重写旧N01、不重开R7 27项、不代主审作canonical/最终关闭。

## 精确未接收与边界

**完整事件接收0/60，60事件均仍有必要的当前定义/消费者签收未完成。** “用途实读60”不能改写为“本有限合同已全部完成”。[interfaces.json](interfaces.json)逐provider列出受影响事件及固定对象，区分：

- **CRE-C固定贡献缺实质记录**：合同绑定的正反向映射均为`records:[]`、`denominator_frozen:false`、OPEN。影响形态/成长/进化/Shadow等关联事件。它们存在且可读取，但没有可接收的完成事实，不能以路径存在或旧PASS补签。
- **CRE-D固定载体无完成贡献**：仅有精确readset绑定，获得/寄养/遗传/孵化/遭遇/捕获相关当前事实无完成provider。此为该固定载体缺口，不宣称R源码不可得。
- **其余固定贡献可得但尚未完整语义接收**：KERNEL、CRE-A/B/E、WORLD（除上述五链）、WORLD-INTERPRETER（除五链）、WORLD-RESOURCES、UI/UI66/MINIGAMES、CORE、MOVE、ABILITY-ITEM、AI、FACILITY、ACTIVITIES、SHARED。原合同的current_routes逐事件列于ledger；不能将这些可得未接对象改标宿主或材料limit。已读provider记录也未导入整文件FULL_READ。

S06及以后不争主责；外域和后继只按依赖读取。父协调继续完成上述必要接收后才能逐事件签收。本次没有提出或实施正式修订、政策采纳、main合并、源修改或游戏执行。

业务向量、参考观察、独立模型、完整宿主/Demo、原生媒体、真实存档/回放均 **NOT_EXECUTED / 0**。Git/JSON/哈希/视图/远端回读仅TOOL_VALIDATION。报告唯一写集为本目录；发布只普通commit/push恢复分支。远端核验的固定core与后继发布tip由外部工具结果及`remote-verification.json`绑定，避免自哈希循环。
