# B16 author-preparation-1

本目录是有限准备提交，**正式写入 0、候选 0、独立复审 0、整合/正式接受 0**。作者按派发执行后在普通推送和远端读回处结束，不自动转完整作者，不代签复审或关闭问题。公共登记由父任务处理。

正式输入为 B15-C `1d06c45cc0a744fca181ac80ee573cc9ebb9b862`，tree `5c99f51ec4cc084bc1c2b081306f1b55370744df`。派发包 `9ad5539f38544fef6037356018015fe418021514` 是该输入的管理后继，只通过 `git show` 读取合同、范围、精确输入和限定，不作为正式输入。原 review `93e10babe0b9c9ef8b3f5277754541b447beeeb4` 与批准控制 `41fffb540c6483f5296ea0d33b789b75180d27ed` 的完整对象身份保持。

请求配置是 `gpt-6.1-sol / xhigh / default / Standard`；无可信后端回显，effective 为 **UNVERIFIED**。没有探测额度、替换模型或启动独立复审。用户另指定的 ultra 复审仍须由父任务独立派发。

| 文件 | 可复用结果与边界 |
| --- | --- |
| [input-verification.json](input-verification.json) | 74 个计划读输入、6 个未来正式输入、5 个原文与5个当前管理输入身份；24×2完整控制对象相等。身份核验不等于74份完整语义读审 |
| [contribution-analysis.json](contribution-analysis.json) | 派发顺序24贡献/20主责，每项完整当前限定及原始绑定、当前UI位置、来源/调用者、静态反例与相邻反向设计、预期中立条款和仍缺最低验收 |
| [source-reading-log.json](source-reading-log.json) | 本轮确实读取的参考与UI范围、整文件与范围哈希；只静态读取，不执行来源或行为向量 |
| [original-sync-proposals.json](original-sync-proposals.json) | 21份ID/路径/条款/精确before/fullpatch/proposed_after建议，20个qualified ID、五份原文；原文未修改，需父任务唯一登记人精确确认后才能应用 |
| [original-proposals/](original-proposals/) | 每ID补丁可独立审阅；不要顺序套用互相基于同一旧输入的逐ID补丁。每文件combined补丁提供完整合并方案。采用完整零上下文unified diff，以`git apply --check --unidiff-zero`只读检查；任何未来应用须先确认精确输入blob/hash与before条款 |
| [dependency-and-refreeze-plan.json](dependency-and-refreeze-plan.json) | B15 A055/A056/C122已接受的限定结果与仍需B16 UI；B12五个正向/两个反向真实交叉，11个既有批次的影响导航及后续重冻结/复用步骤，无作者影响复审结论 |
| [catalog-preservation.json](catalog-preservation.json) | UI测试目录全量旧表行ID/物理顺序/重数与行哈希；既有接受语义保护，整文件身份不能替代逐条含义 |
| [source-limits.json](source-limits.json) | 完整继承U01–U10/G01–G12/AX01–AX20以及未读/未证限制、本轮静态范围和零运行计数 |
| [verification.json](verification.json) | 作者私有记录格式/哈希/范围自检及26份补丁dry-check；没有独立质量PASS |

主要准备发现：交换成功后仍持原目标Y；空重学首绘严格ID失败；零招式普通四空位可画、详情/忘招首绘失败；BoxLink存入压缩队伍后旧换位源未重绑，可先写`[空,A]`再面板失败，B仍入盒；有限槽回退保总量但可改槽分布；BP数量窗按数量乘单价整除2显示，而实扣全价。搜索失败后模式写入、已接受的结构形态门、首次形态选择写入、哨兵、last-able守卫等均保留。

B15 A055是B15主责/B16局部贡献；A056/C122在B15仅局部接受，B16主责最低验收仍未完成。当前UI的A044/A055与空/非空启动分支已经正确，不再建议修改正确原文。C003仅准备PT A23/A31/A33；其他已裁决扩展和所有其他owner行继续保留。

当前完整作者的真实阻塞是B12接受前的相互读写及共有003语义。五个B12写/B16读输入为四份WP52与**Pokémon规则测试目录**；B12反向读B16未来会写的WP65标题与WP66A。待B12精确candidate/必要affected/G/actual/C通过且发布，由父任务以最新接受SHA/tree重新冻结，绑定变化输入、加入B12已接受影响，复用精确不变证据，再派发完整B16作者和独立ultra复审。没有新增PLAN依赖或人类阶段确认门。

参考仅静态读取 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。派发指定的bare缓存缺失，恢复固定对象到`/tmp/b16-reference.git`，未checkout、执行或改写参考。实际素材、宿主输出、动态调用/插件及Demo链仍未证。本轮读取的是新增/受影响的有界来源，不递归重读历史报告或旧证明。

可恢复身份核验：`python inspect-inputs.py verify`；按精确来源读取：`python inspect-inputs.py read reference '<path>' '<start-end;start-end>'`。`prepare.py`、`propose-originals.py`、`resume-plan.py`仅生成本目录的Git/JSON/hash/text准备记录与文字补丁，不是运行测试、规格实现或来源程序。使用`PYTHONDONTWRITEBYTECODE=1`避免额外缓存。

规范状态仍为 required OPEN 229 / CLOSED 0。本提交的作者自检、推送与读回不会产生候选PASS、整合复审、正式C接受或问题关闭。
