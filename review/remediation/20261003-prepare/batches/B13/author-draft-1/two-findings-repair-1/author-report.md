# B13 两项有限返修及原稿新范围提案

当前仅作者返修／提案，非独立PASS。正式FIX_BASE仍B12-C `8e67f780c204d593d89f364f585d2c6c2fe74631`；两份review均审旧候选 `5845e8084ced280e51c51a4081ec8583a9c2ca39`，其输入未改。父要求把FULL B13-R01/B027及affected B13-AFFECTED-F1/B029一次整理，canonical增量0、B030不计。

B027：源正常回调的nil左值原样返回；空列表对象提交后返回false。仅新增WS-W35及当前轨迹／B027处置返修：JSON null+return_identity=nil，falsey另列，不覆盖历史冻结证据。WP55、旧W28/W29、进行中／未进行中状态与默认UI人数门保留；无B027原稿新扩围。

B029：独立定点核实初始属性快照先于正常入场，入场最终全场速度扫描先真实降阶物品、再跨严格整数半HP能力，首个真停止；非EOR的选择可在首命令槽之前追加／回放同点消费。攻击后清选择不再行动限定仅用于已有攻击；开场清旧选择不取消随后首命令。EOR只召回离场、询问留后段；EJECTPACK先耗后选、负选返假却已耗，负值仍记录。净WP58§5.2分开这些时点，保留随机／Arena／W16，补未执行RC-W26；WP58§7/目录只同步数量和导航，现137静态设计（旧136+1，初始127+10），没有执行向量。

[两问题映射](two-findings-repair-map.json)逐条连到最小返修；[当前轨迹](static-transition-traces-successor.json)明确替代旧nil false oracle及未覆盖的entry timing；[当前8项处置](finding-dispositions-successor.json)保留完整原控制、root/extension、有效反例、最低验收、非本地义务及主责计数，不用两个focus代替8/5。[来源及consumer导航](source-and-consumer-navigation-successor.json)记录准确fresh局部范围、current WP41/WP49/WP50主稿三个必要只读增量，未扩大owner写入或重新阅读全历史。

唯一待许可原稿是 [WP58§5.2新精确提案](original-scope-proposal-2/README.md)，before绑定当前1dc5cc8原稿、完整after和whole.patch逐字绑定。旧四补丁许可仅保留旧字节，不延伸；本轮未在原稿树应用新补丁。父必须先确认这个新scope，随后作者可应用固定字节、重冻结完整候选，原独立FULL及B09/B11做OLD→NEW有限复核。当前净稿／原稿尚未同步，不能给完整验收或G/C。

[新metadata](repair-metadata-verification.json)确认只有2正式路径变化，旧目录全部ID顺序/多重性、W16/W24/W25/W28/W29及他方行保持；仅改新增WS-W35、加RC-W26，其余所有旧输出与四原稿保持。所有已冻结报告/许可/输入原件保留，不向reviewer旧candidate写入。

全部源限制与U01–U10/G01–G12/AX01–AX20、树果条件67、具名未读内容、B16 WP67-A与双向依赖保持；无reference/Ruby/game/行为向量/历史程序执行，只本轮新文本／Git／JSON／SHA元数据。无main／公共登记／reference写入，无自开review任务、无质量签字。新publication及OLD→NEW完整未过滤流与远端ref/FETCH_HEAD/tree/全部输出读回在 [当前返修入口](../../candidate-1/two-findings-repair-1/review-dispatch.md) 后继收据中。
