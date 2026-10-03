# WP77修订v3：R03/R07残留＋N01地图标签三处收尾

工作目录 `/Users/dingshinn/Desktop/pokemon-framework-reference`。本轮WP77 v2有界复审结论REQUIRES_REVISION：原9项中R01/R02/R04/R05/R06/R08/R09共7项已关闭；R03/R07两项P2仍OPEN，另新增WP77-N01一项P3。先读本目录report.md、findings.json、independent-checks.json、registration-checks.json、source-read-log.json、input-manifest.json及AGENTS.md。

当前被审主稿v2：40f21b99acec8571df27447b281529d9463dffbc0a3b6c4f182e42cb8d431cee／41,773字节；v2附表95d38a6c905df41112f132c02bc4990e0e5e147a5dd9bbf337bb4329f252c234／7,628；v2缺口表891793ebf6dbb609743b8d0782200b9f76a2e32c345bdf80ff0de635587aecee／4,454。开工重新实测；当前登记第132轮、TSV v107。

1. R03：主稿第100行前半6条飞行/5目的地正确，但后半普通18条示例仍含Cedolan第二点。两个Cedolan坐标(13,10)/(14,10)都带飞行目的地，都应只属于飞行组。修正普通点示例，保留18＋6＋2、5目的地、4个治疗点匹配。按行号/坐标核分组成员，不只求总和。
2. R07：主稿第120行“MAGIKARP与FEEBAS各重复槽位”错误。Safari内区水/钓表MAGIKARP有3条（OldRod两条、GoodRod一条），FEEBAS只在GoodRod出现1条。修正解释，保持14条/12种、陆遇12条/11种、Tiall6＋2及正确备份身份；不合并不同池权重、不增删来源记录。
3. N01：主稿第87行将045归到Route5错误。源注释及Name均属Route6。更正为Route5（041）、Route6（044/045），或分列自行车道；不要改已有正确的041↔045连接。

只修改WP77主稿及直接关联的新交付文字，新材料放 `review/wp77-delivery-2026-10-03/revision-v3/`。v1/v2交付、本review与首审原件/快照保持；已关闭7项不重做。附表或缺口表行为没有变化时可以保持并明确引用已核身份，不为增加diff制造变更。

提供三项逐项回应、修订摘要、自检、来源身份及相对本review/input-snapshot冻结v2的严格diff与绑定。新N01明确为本轮补充发现，不伪称原9项之一。按最终字节实测场景/表/链接和计数，扫除同根错误解释。

只更新F18-06/F18-07的WP77修订待审子范围及必要manifest/TSV，历史只追加；通常续第133轮/v108，以真实现状为准。末检独立保存避免自哈希。完成停止送三项短复审，不自行CLOSED/Reviewed，不进入WP78/79/80。缺事件/运行证据边界继续保持，不编造已演示。

reference只读且HEAD保持8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b；不运行参考/游戏/编译器/反序列化/行为模拟器，不写新框架，不创建聊天/Agent、不跨会话发消息、不提交推送。
