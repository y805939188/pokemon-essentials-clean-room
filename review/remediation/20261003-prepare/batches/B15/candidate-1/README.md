# B15 两组有界修复完整候选

正式基线 `0cfe99094b76f8d75fded0d638694677855a5f0c`；旧FULL及affected reviewed `cc08a9150131b7e9fae8424fb0ede890169dd64f`。16本地贡献/10主责继续保持。两项质量需修已由作者定点修复，待两个原reviewer对新SHA增量判断，**作者未签新候选PASS或正式接受**。

- C122 / R-B15-C1-001：PD32/PD33及原W32/W33明确原始/本地化nil、合法空串邻近反向；正确§6.1保持。原两行批准/应用见 `../author-draft-1/label-nil-original-sync-application.json`。
- C109 / R-B15-AFF-B03-001：最终及原P33明确最终实际查询未登记的两个失败及两个成功反向，原§8只修本项过宽泛称；正确净化§3.1/§8保持。精确批准/应用见 `../author-draft-1/P33-original-sync-application.json`。
- `combined-repair-delta-and-protection.json`：九正式路径，精确四路径/六设计行+一原C109句，三净化正文整文件及其余14贡献/control/design不变；旧行ID顺序/重复与其它owner保护保持。
- `formal-identities.json` / `finding-revisions.json` / `report.md`：完整前后身份、逐finding控制/修订/静态正反前提及限制。
- `catalog-protection.json`：18目录，2,995旧行与2,907其它owner行保护；只改本批已批准旧P29/MG-29/P33，43新增设计的ID/顺序不变。
- `independent-review-request.md` / `independent-review-requirements.json` / `affected-interface-assessment.json`：两个原reviewer增量派发范围及旧结论新diff核对后绑定的规则；未来actual门另行。
- 新候选完整SHA、正式基线→候选及旧FULL→候选的完整未过滤diff、九输出、远端读回均由后继 `../author-draft-1/publication-receipt-repair-2.json` 绑定；后继只发布diff/身份资料。

批准的frozen proposal/patch原字节保持，其pending/false字段是批准前历史，当前应用由各application receipt辨认。nil-only中间候选180a及旧阶段证明按准确版本留存，不作最终组合SHA的PASS依据。原FULL报告e089…与affected内容4e5f…/发布4fbd…均只旧cc08版本；其它affected B04/B08/B14旧PASS与B02/B06/B07/B09/B10旧NOT_AFFECTED不能直接转移。

作者原稿写入阻塞已解除。下一步同FULL reviewer增量检查C122和组合delta回归、原affected reviewer检查C109/B03与其它旧接口的准确新版本绑定；父可并行调度，作者不派重复任务。soleA-REG整合后新actual独立门与正式接受仍未完成。B16/公共台账/index/导航/参考不改；U01–U10/G01–G12/AX01–AX20及具名未证项保持，运行/向量/demo全0。
