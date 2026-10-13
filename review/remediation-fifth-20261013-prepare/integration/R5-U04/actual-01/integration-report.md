# R5-U04 actual-01：审定v2机械接入

原作者v2 `f7dba61471c674c6e45efb0595be06bf3cdc773b` / tree `02499fe1cea46dc9e04a1b127d32702fddf42c7c`、证据 `e22def9449b65ef83e11dc267dc0c7937245eace` / tree `dce5aa8c1634cbbd51fdb1613eccd43482b3e953`、原独审 `262669581b0dd3f4ef2689c5cead8395959b2342` / tree `866ce1feb8941f2cf348d74ffab9035d9cef756c` 的7必修/32标准限定候选PASS已核。R5-I仅接入原28操作，作者正式投影和增量字节不改写。

16当前目标全部仍是B5，故已审完整B5补丁亦为当前精确补丁；15专属镜像逐字节相同，WP39仅插入U04具名显示秩片段。1共享路径仍需U06贡献和相应整份验收，不影响本批单独实际复审。无内容冲突；与已接受U01/U02/U03的46路径无交集，46当前blob全部保留。正式131中改变16、未变115。

[逐操作/文件/32条件映射](candidate-to-actual.json)、[审定精确补丁](current-to-actual.patch)、[上游与共享门禁](upstream-impact-and-gates.json)、[机械身份核验](mechanical-validation.json)、[正式131身份](formal-tree.json)。55静态设计和33旧向量沿原独审精确范围保留；本次只做文档/身份/patch检查，不执行参考或行为模型。

U03限定接受门在debf已满足。原U04v1的5PASS/2FAIL及30PASS/2FAIL、v2两项定向修复/一项证明传播/29条件限定复用保持各自固定身份；不回写旧失败或把候选PASS授给actual。原U03 FAIL、两处MISMATCH、SC-U07-001亦保留。

当前U04 actualPASS/正式接受均0，CLOSED0；累计已接受仍59owner scope/175canonical操作，U05继续等待本批实际独审与接受。实际commit/tree将在后继locator绑定，交[原审者入口](reviewer-entry.md)复审。原审者thread引用01a136cc-11ea-742e-af80-a75168aed020由父任务派发；thread不是opaque task UUID。

U04安全恢复且候选/独审发布的固定证据已核；没有替代作者或复审域。U06尚未确认恢复，未触碰未发布成果、原环境或任何归档/释放/危险恢复。main不合并、不动Mac，原92/optional/政策及宿主媒体/真实存档/完整Demo限制保持；本update新增参考/模型/宿主行为执行0。
