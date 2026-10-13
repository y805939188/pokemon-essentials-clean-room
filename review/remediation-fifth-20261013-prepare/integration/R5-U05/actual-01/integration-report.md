# U05 actual-01：两份审定镜像机械接入

U04唯一限定接受在 `e697d047f445691934dcde1835f68c70c4e2cc60` 已完成，7owner/32条件/28操作被接受；累计66owner/386条件/203canonical操作。WP39只接本批1524bytes贡献，整份仍待U06。

U05固定作者 `4bdfd36aca3dbfb6ef0c61ef6e7af057acd6820b` / tree `ca2dfe5eefb2ffc021bcc7191baf1f825f0ec219`、原独审 `70893d9cfd47cb28604a672df6d8fd40b9a96fe4` / tree `419d72ba5a07220d46e0ecd6ca59e1af6fbefc89` 的GR5-M09-001 1项/4标准、B64–B71候选PASS保留原签名。仅两个独占正式镜像按原10173bytes补丁机械接入，无共享写、语义改写或锚点冲突。

[精确映射](candidate-to-actual.json)、[原审定补丁](current-to-actual.patch)、[依赖/消费者](upstream-impact-and-gates.json)、[机械核验](mechanical-validation.json)、[正式131身份](formal-tree.json)。两目标仍为B5，原62接受路径未变；当前U04正文有改动的三个消费者文件中，必要四段§2.2/§6.1/§4.1/§5.1与B5逐字节相同，不能把这资格扩大为整文件B5未变。

候选旧WAIT不回写，当前门由U04接受回执满足；实际正文与候选精确相同亦不授actualPASS。U05实际独审/接受0，CLOSED0；实际commit/tree由后继locator绑定，交[原审者入口](reviewer-entry.md)。局部分数不代表最终选招或宿主/分布/真实治疗执行。

所有旧失败、两处MISMATCH、SC-U07-001及GR3-M09-001 OPTIONAL/DEFERRED/旧U08未启动保持。U06未发布域/环境不动，不归档/释放/危险恢复；原环境只安全重试。main不合并，Mac不动，本update新增参考/模型/宿主行为执行0。
