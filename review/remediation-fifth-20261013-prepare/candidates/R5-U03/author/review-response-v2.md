# R5-U03 有限 v2：作者定向返修

接受独立报告 `0fd3fe285f4c726d736a7281f9949a5f3c91e0e9` / tree `8830d80fd553f76720e2f9c31bf5e9066c7595b2` 的唯一候选 FAIL。v1 替换 B5 WP18 第198行时，我遗漏了NPC使用简单形态写入及非空/默认招式入口的绑定。v2在同一WP18片段的§4.3.1前提段恢复该绑定，新四字段覆盖表、普通创建/缓存、IV/EV、钩子与失败前缀边界保持；WP24原委托该节，委托文字无需改动。

恢复的规则：给定形态（包括0）走简单存储写入，本次不调用形态处理器、不登记图鉴、不清特性缓存，仍重算；随后持物、招式，显式列表存在且非空则按给定顺序逐个静默学习，否则按当前等级可达学习表重建默认招式。通用细节引用WP20§5.1，不复制API或参考代码。

新增R5U03-M01-006-08/09/10三条DERIVED_VECTOR/NOT_EXECUTED：简单形态的中间观察时点，非空[TAILWHIP,TACKLE]，以及默认RATTATA L5的省略/记录空列表均得[TACKLE,TAILWHIP,QUICKATTACK]。先前66条向量完整内容保持。WP18片段、同一测试目录镜像、operations、fragment-manifest、formal-diff.patch及派生身份同步；normative targets仅2个。

两处冻结历史整文件SHA是过时导航，仍为MISMATCH，不能宣称旧SHA通过。后继navigation-corrections.json绑定c0ff的两实际文件bytes/SHA256/blob与四个精确记录指针/hash；本次直接核四条，其余17条只复用0fd3fe2的具名独立证据，不报新增验证。未改冻结历史或旧状态，未增加全局必修。

其余10项按v2-response.json的精确未变findings/向量/规则贡献复用原报告PASS；共享文件总hash变化不能自动授予整文件接受。GR5-M01-006只报告作者STATIC_RESTORED，须原审者对新固定字节复验，不自签PASS。U01实际接受仍WAIT，R5-I实际整合/同审者actual复审/唯一登记门均未执行。

本update新增参考/模型/宿主/Demo行为执行0；R4历史隔离4、R5review隔离4分开保留且未重跑。请求sol/xhigh/default普速禁Fast保持，实际回显UNVERIFIED。无模型切换、无额度审计、无main/公共正式/登记/Mac修改、无审者启动。

复验入口仍为冻结contracts/R5-U03/reviewer-entry.md。最终候选/证据commit/tree由外部回执绑定；先看v2-response.json与导航后继说明，再定向读006片段/三个向量及派生差异。
