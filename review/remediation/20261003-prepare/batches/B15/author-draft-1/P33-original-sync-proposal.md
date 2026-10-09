# R-B15-AFF-B03-001 原WP63精确范围提案

准确affected内容报告 `4e5f50c1c2235595c09e17fada56ac03ed23f02c`（发布 `4fbd895d7e11ec57fe24f27859852114e74abfb0`）审查 `cc08a9150131b7e9fae8424fb0ede890169dd64f`，唯一B03有界P2为C109/P33最终查询区域前提不唯一；原稿§8一条泛称也被minimum_revision明确要求同步限定。净化正确§3.1/§8不改，nil四行修复 `180a0e1757a74cdf500411845c6f9a6d3bf8f7e0` 全部保持。

已修净化P33为两失败：无定位回退0未登记；有定位99未登记且请求-1/未知请求使最终仍查99。两成功反向：0缺失但当前位置1合法且跟随；当前99缺失但合法不同区域请求1。仅最终实际查询未登记才Unknown ID，成功均查1而不查询缺失0/99。正常元数据/UI前置与无插件明确，实际渲染及全部向量执行未证。

仅申请 `specs/ui/wp63-pokegear-map-music-and-phone.md` 中两条文本：§8区域查询失败的C109泛称、P33一行静态设计。before `180a0e1757a74cdf500411845c6f9a6d3bf8f7e0` 中原稿的完整blob/SHA-256/字节、逐条before/after全文、拟after身份、完整patch/hash均在P33-original-sync-proposal.json与P33-original-sync.patch。没有申请其它正文/其它owner行/B16/公共台账；不继承已批准W32/W33权限。原稿当前尚未应用，待父对此完整精确补丁另批准范围。

批准后原稿精确应用并核对after，最终同一新候选含nil和P33两组修复，由原FULL和affected reviewer分别增量核对新diff后绑定；其它B04/B08/B14旧PASS及B02/B06/B07/B09/B10旧NOT_AFFECTED仍仅旧SHA，不直接转移。
