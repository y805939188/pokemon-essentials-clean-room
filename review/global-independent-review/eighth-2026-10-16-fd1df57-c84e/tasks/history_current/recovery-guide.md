# 准确恢复与继续阅读

本目录所有恢复均只取得材料，没有执行被恢复程序或授予语义阅读信用。固定原始包保留在C2的`publication-transport/core/`，报告原树和主clone引用保持只读。

## 已有路径

- `recovered-fixed/`：24个按9aa/C2固定Git对象恢复的文件，详见`recovery-manifest.json`。
- `recovered-transport/`、`recovered-facets/`、`recovered-early-history/`、`recovered-r6-actual-fields/`：选择性gz恢复；对应`*-recovery-manifest.json`保留原logical path、编码/解码身份和本地路径。
- `recovered-cache-r6/`：15份按原不可变提交恢复的R6报告/交接/裁决，详见`cached-r6-recovery-manifest.json`。
- `object-cache.git/`：local-only隔离bare缓存；准确origin、7个commit/tree和真实fetch I/O见`isolated-git-recovery*.json`。禁止将嵌套bare仓库整体加入报告发布。
- `readset-materialized-*/`：构建读集时对尚无本地精确副本的已核blob建立的新隔离快照；准确路径保存在各readset的`local_path`。

## 新上下文

先读根合同、AGENTS、本报告根`inputs/review-SKILL.md`及所分配的`dispatch-ready/*.md`。readset里的`local_path`是已核载荷；固定B8路径、原来源提交路径、解码logical path和Git树中的压缩路径各自保留。

需要恢复gz时，先完整读`recover_transport.py`，在新任务授权write_root内复制该已读helper并将TASK设为该目录。选择一个原先不存在的新名字，例如：

```text
python3 <本任务已读helper副本> --name new-c2-readset --select tasks/R7-C17/current56-contract-reception.json
```

该helper从已核C2本地index选择准确对象，拒绝绝对/父级穿越及含symlink的目标，验证编码bytes/SHA/blob、有限解码并验证解码bytes/SHA/blob，只写新隔离目录和真实receipt。保持原gz，不执行恢复文件。

准确历史Git对象在主clone缺失时，不能标成材料limit。按冻结history-navigation的准确commit/archive映射，使用自己的新bare缓存、同一origin及精确SHA普通fetch。可把既有B8/本任务缓存objects设为只读alternates以减少传输；不要在其他任务的cache内触发懒取写入。使用自己的cache读取并在自己的新隔离目录保存，核原bytes/SHA/blob/mode/tree。`fetch_historical.py`和`recover_cached_r6.py`是本次实际流程及范围的可审示例，不盲运行未读工具。

本次7个准确历史提交和15份声明载荷均恢复成功。最初LOCAL_MISSING已经解除；后续工作受限于尚未实际阅读/接收，不能把它改标材料或宿主限制。所有大JSON按真实结构连续分块，身份表、行政字段、历史副本与当前有效语义分层，覆盖/解析/解码/哈希不替语义实读。
