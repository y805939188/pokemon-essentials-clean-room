# R5-U02 作者 v2 有限返修交接

两项FAIL已完成作者有限返修，待原独立审者复验。固定复审 `4a6e11ca2ad84b53ff2faab8f3b6eb98c5a87b64` / tree `fd345f68daed91f6e4c6afa545424fca9fd31bd4` 原裁决12项限定PASS、2项FAIL；原45/46 mandatory static PASS及007消费者FAIL保留归属，不自签新PASS。其余12项范围/向量/作者finding record未变，精确旧复审pointer与身份复用见revision-receipt.json。

| 项目 | v2作者结果 | 独立状态 |
| --- | --- | --- |
| GR5-JXN-001 | NAME02三分支/NAME07三个边界各用独立可满足前提，前置查找失败不要求成功查找；主正文及NAME01/05不改 | 待原审者限定复验STATIC-03 |
| GR5-M03-007 | WP60§3/5/7/8/9区分等待结果与物品回调消费；FS04/15限定普通物品入口；新增FS05/06直接与普通成功对照 | 原3条mandatory PASS归属保留；待消费者限定复验 |
| M03-001～006、008～013（12项） | 限定贡献字节、向量及finding record均未变 | 复用原固定复审的限定PASS；不签共享整文件/实际整合 |

B5、R、任务冻结与准备基线均沿v1；实际正式131子树仍 `d5a462b4c6f8b78c3264a25d6b5495230fa265e2`。候选有8镜像、8共享目标的18片段、46条必修映射及75个DERIVED_VECTOR/NOT_EXECUTED_THIS_UPDATE。实际投影仅钓鱼正文与engine测试目录两目标改变；14份其余镜像/片段文件按完整字节保持。普通分支codex/r5-u02-author-20261013，v1固定commit保留，v2候选/证据commit/tree由发布后外部回执绑定。

直接等待成功：count＋1、battles不变、遭遇请求0；普通物品回调成功：count＋1、消费true后battles＋1、再请求对应竿类型一次。相关公共事件/消息/清理正常且无额外消费者或统计写入是前提，请求一次不保证实际战斗/胜利。

复现仍用rebuild-candidate.py/validate-candidate.py，仅处理文档/补丁/身份；投影写/tmp/r5-u02-projection。169项当前工具校验通过，另外revision-receipt.json逐个证明12项限定贡献未变。formal-diff.patch提供B5完整候选投影，v1→v2必要差异可按固定提交比较。片段仍只供R5-I按精确锚点接入。

原审者有限入口：复验NAME02/07及JXN STATIC-03；复验WP60/FS04/15/FS05/06生产者→消费者一致性；核派生载荷及身份，未变12项无需重做。冻结contracts/R5-U02/reviewer-entry.md保持；本任务不启动审者。R5-U01实际接受依赖仍WAIT，没有actual签名、正式接受或CLOSED，不改公共正式/登记/main。

本v2新增参考/行为模型/原生宿主/Demo执行均0；R4历史隔离4与R5全局review隔离4分别保留。optional/no-required/兼容政策不扩入；材料、媒体、宿主和插件边界沿v1。实际模型回显UNVERIFIED，不审计额度/认证。
