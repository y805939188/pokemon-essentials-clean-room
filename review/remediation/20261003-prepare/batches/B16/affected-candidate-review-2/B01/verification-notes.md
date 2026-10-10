**B16 增量共同元数据核验**

新脚本可按固定Git对象复现；它只读Git bytes、仓库JSON、摘要和目录行，不运行参考、Ruby、行为向量或旧作者/reviewer程序：

```sh
python review/remediation/20261003-prepare/batches/B16/affected-candidate-review-2/B01/verify-metadata.py --repo /workspace/pokemon-essentials-clean-room --reference-git /tmp/b16-reference.git --scratch-dir /tmp/b16-affected-independent-repeat-2
```

完整OLD→NEW与FIX_BASE→NEW流先无过滤读入并逐路径解析，再从该完整流派生三条当前文本变化。新增JSON均作为元数据完整读取/解析；不将嵌套旧diff、旧trace、partial状态或author pending声明误当当前质量裁决。两个publication拷贝必须完整字节一致。

identity-and-protection独立验证author protection的36,414 OLD既有保护路径、11输出的8个不变、3个单行、36,339 BASE保护路径、240接受贡献、目录484行的483字节保持及BASE460旧行；scope4对一文件一条款完整before/patch/after核身份，单一hunk与实际新整份after相同，其余四原稿与scope3结果一致。

qualified-controls-and-reuse保留24/20完整当前根/扩展/minimum和12有效条件，精确复用原报告对象及哈希。不重新执行旧核验程序，不重新批准旧owner全域。C120及奶招当前实际接口分别独立读固定源和条件；旧报告缺漏通过NEW有界结论说明，旧对象不改写。

普通提交推送后，在新bare缓存独立fetch远端完整ref，核tree并读取报告的全部文件字节（包括文件清单自身）与本地Git/工作区一致；报告SHA对外交付，避免自身commit循环引用。
