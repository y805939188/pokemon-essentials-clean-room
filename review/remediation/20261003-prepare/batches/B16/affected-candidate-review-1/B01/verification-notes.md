**共享身份、控制与保护核验**

核验输入为固定 Git 对象；所有源和旧作者程序均未执行。新脚本仅读 Git bytes，解析仓库 JSON、计算摘要和目录行身份，不模拟任何行为向量。

在具备准确仓库对象及准确参考 bare Git 的环境，可复现：

```sh
python review/remediation/20261003-prepare/batches/B16/affected-candidate-review-1/B01/verify-metadata.py --repo /workspace/pokemon-essentials-clean-room --reference-git /tmp/b16-reference.git --scratch-dir /tmp/b16-independent-repeat
```

脚本直接从固定 commit 读取 dispatch、完整合同、24控制、12有效条件、scope3、manifest、14导航与准确旧静态证据；不依赖此前临时导出的JSON，也不自动拉取历史或执行旧脚本。缺少固定对象应补齐所列精确对象后重做，不拿移动branch或不准确版本代替。

`identity-and-preservation.json` 留下11完整before/after身份、74固定计划输入身份、24原对象/批准对象与当前控制摘要、12完整effective相等、五原稿精确scope匹配、完整78路径差异、36,339保护路径投影摘要、240接受贡献数组摘要及逐批计数。目录用section＋ID＋occurrence及原始行字节独立解析；460旧行不删不改名不重排，451保持、9修订、24本批新增。

准确先前参考证据复用只限固定参考commit：33完整源文件身份和既有有界行摘要相符；18补读文件身份相符。六个旧项目快照不代替现在的FIX_BASE/candidate，当前输入和11完整差异独立读取。完整qualified-control-coverage保留所有根/扩展、20主责及非主责003/006/A055/C003；本地接口判断不消去非局部义务和待完贡献。

静态metadata PASS与owner质量结论分开。原稿scope3只是精确范围许可；candidate质量阻断为B06/C120的类型前提，其余owner按各自caller/data/condition判定。本材料不签FULL、ACT、G、C或任何canonical关闭。

普通提交后推送独立报告分支，读取远端完整ref、精确tree及全部新报告文件字节（含文件清单自身）并与本地比较；最终SHA在对外交付中给出，避免报告自身commit循环引用。
