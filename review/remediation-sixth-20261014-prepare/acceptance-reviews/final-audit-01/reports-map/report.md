# 有限最终登记审计：五报告签名、资格与56指针

结论：**PASS_REPORT_SIGNATURE_AND_56_POINTER_MAP_SCOPED_STATIC**。本分项无最小登记必修项。独立核五份完整根actual报告的签名／资格、五份structured verdict准确身份与56逐ID指针，以及一主组／一主批、severity、合同和当前接收映射。该分项满足后继有限formal acceptance的报告签名与映射条件；整包`FINAL_REGISTRY_DEPENDENCY_PASS_SCOPED_STATIC`及eligible布尔由根审者结合两个公共56行层和110条原依赖审计决定，本辅助不代签其它分项或修改接受状态。

审计入口为`229260cfd5177581bb88bafd84770ceb1c11b117`；被审登记`d35356005f79b9fdffc5a4202a0b39e9255a36fa`、workspace tree `a86a6a77e4f0196f4e5b9aa435d346518640773b`。实际语义版本`86bbc99b28d93db4ed9d6897daf5f3725ccd1808`及formal tree `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`精确保持。请求gpt-6.1-sol/ultra/default/普速与有效配置分开：有效model/effort/tier/speed/UUID仍全部**UNVERIFIED**。正式接受0、CLOSED0、OPEN56未改变。

## 新完整读取及固定签名

AGENTS297行、prompt13行完整新读。输入1700行分为1–560、561–1120、1121–1700完整新读，bytes72694、SHA256 `24f93c5d56fe8f0fc127d789ca1700994c18ad37df3434e1879b10d3cfc5fa8a`、blob `b2532b56dd5d4c7ba512ae21316e8db35e34aebd`。五报告分别从输入声明的准确commit读取，不要求它们存在于d353工作树。51个有限身份绑定、17项owned静态机械检查通过；所有mode100644、type/blob和commit所属tree按Git对象核，真实命令及输出指纹保留在`reports-map-validation.json`。字节核验不替代语义阅读；十份frozen readset只作本分项必要身份检查，公共规则语义由对应分项承担。

| 主组／主批 | 完整根报告／新读行数 | 固定报告commit | 签名结果与最小内容修复 |
| --- | --- | --- | --- |
| A／U01,U03,U14（11） | `actual-reviews/group-A/report.md`，1–175 | `988ed0bc551f72dbdcc654d37822c7ccf2397c20` | ACTUAL_PASS_STATIC；0 |
| B／U02,U04,U05（9） | `actual-reviews/group-B/report.md`，1–72 | `c5b65ec4d5d3b21c7ddd77ee8a220a5d1eb78ada` | ACTUAL_INTEGRATED_PASS_SCOPED_STATIC；0 |
| C／U06,U07,U08,U09（19） | `actual-reviews/group-C/report.md`，1–47 | `386e8a5b2c5206e6fa963b1c85875eabf96d6cd1` | ACTUAL_PASS_SCOPED_STATIC；0 |
| D／U10,U11,U12（9） | `actual-reviews/group-D/report.md`，1–70 | `7a637751bc26b3a7b6cc30d281ef9663d3a7f692` | ACTUAL_PASS_SCOPED_STATIC；0 |
| E／U13（8） | `actual-reviews/group-E/review-report.md`，1–78 | `915f0ef84ca5c544c98978ddfb0ee76149a2e033` | INTEGRATED_CONTENT_PASS_SCOPED_STATIC；0 |

所有相对路径均以`review/remediation-sixth-20261014-prepare/`为前缀。完整报告/structured bytes、SHA256、blob、workspace tree、directory tree及范围在`five-report-signatures.json`，没有省略metadata靠简称绑定。报告正文各自明确86bbc/ebbe；所有有明确binding字段的structured根/逐项对象均匹配，B的formal绑定由其准确完整根报告给出，不伪造JSON不存在的字段。云端thread仅按输入parent-verified声明身份读取，不把source-thread引用或用户请求当当前UUID回显。各报告均为非作者有界静态裁决，没有整体56全局签名或配置认证；作者候选PASS与新actual判断分列。

## 56精确pointer与唯一归属

`report_per_id_pointer`实际作用于对应`structured_verdict_path`：A findings.json `/records/*`；B criteria-results.json `/ids/*`；C per-id-review.json `/rows/*`；D per-id-review.json `/per_id/*`；E verdict.json `/per_id/*`。它不是Markdown报告的JSON指针。五份structured完整字节解析、身份核验；逐56必要身份／verdict／zero repairs／owner／合同接点核验，不重复其完整行为事实。每项目标ID精确相等，56个(group,pointer)唯一，所有verdict与该组原签名结果一致。

先检查五组原始record lists及56mapping原始list的唯一性，再建立字典。56恰一主group、恰一当前主batch：A11+B9+C19+D9+E8=56；39P2/17P3、P1=0。完整逐项表在`per56-pointer-results.json`，包含exact commit/path/pointer、目标record canonical SHA、contract bytes/SHA/blob和record canonical SHA、current candidate、severity、public/dependency落点及剩余门。14合同在86bbc及469a字节完全相同，各指针落到同ID、同severity、同primary_batch，原依赖和necessary_consumers指针同值；B七组canonical证据值、C合同定位及D七组contract pointers也逐项匹配。

公共registry指针落到d353 `integration/public-sync-20261014/sync-input.json /items/*`，dependency落到同版本`dependency-status.json /per_id/*`，并与ledger required同ID接合；三处实际主审引用的report/verdict path/identity、commit/tree、per_id_pointer、actual/formal、必要修复0、UNVERIFIED和未接受/未关闭分期相同。56项静态内容条件满足不等于正式接受：各处formal_acceptance=null/false或A原报告NOT_GRANTED均是未授予，CLOSED=false。

F002只计E主责，D的ACTUAL_INTERFACE_PASS补充不加入D九项；Arena V004只计E主责，B WP40补充不加入B九项；U14六项只计A主责，C消费者接合不增required分母。E七组外部声明来源及semantic_report的16处引用字节身份已核，八个声明record按实际JSON容器精确解析并记录pointer/canonical SHA，未将正文同名文本当成员资格证明，也未额外重签其行为。

## 资格和同期后置条件

A报告54/62/78/94/110/144–146、B72、C47、D62、E73–76中行政同步／正式接受／关闭均是报告产生当时待后续完成的条件。它们不否定11/9/19/9/8已签静态内容，不要求新增源执行、全宿主、原政策或可选facet。当前d353公共同步已应用，需由本次准确registry/dependency审计判定其后置门是否满足；仅R6-I随后登记formal acceptance/CLOSED，本辅助没有倒改旧报告的pending句。

A共享表34–39中若干Uxx为跨历史叙述简称，不能变成本轮candidate收据。当前14批／candidate/path/contribution均按86bbc实际input精确映射：WP10/WP34仅U01；WP13/WP60/engine目录仅U03；WP62为U01/U09/U11；pokemon WP53域目录为U11/U13。`current14-batch-map.json`和validation的实际贡献字段给出准确命名空间。input对历史简称已明确限定，当前登记采用正确一主批，不要求重写既有报告历史叙述。

五报告明确SOURCE_STATIC/SPEC_STATIC/DERIVED/TOOL分期、normal controls/异常已到前缀/未执行范围及有限历史复用；未把旧18次Ruby尝试变18成功，不从原R5 92CLOSED转签本轮，也未因物料定位/二进制字节核验声称新增反序列化或全文源语义。当前配置没有可信回显，保持UNVERIFIED而不补造证书；其与内容资格和登记接受分开。

## 实际失败与执行边界

setup首次从当前worktree复制本人旧helper失败已保留，未据此判固定报告不存在。owned audit首跑把A的NOT_GRANTED漏出允许的未接受表示，退出1；原script/stdout/stderr/receipt保留，修正后退出0、17项全PASS。一次便捷诊断猜错两个未声明helper文件名退出128，也明确保留为审者路径猜测错误；随后依实际declared paths解析成员，未当候选/登记缺陷。组合读输出截断的input缺段已由read004重读补齐，报告read007–011无截断。真实UTC/cwd/argv/runtime/退出、stdout/stderr和范围见reading-ledger.jsonl、execution-notes.json；未单独捕获的UTC不伪补。

本辅助只运行自有Git/JSON/hash/pointer静态脚本，作者脚本/参考程序/行为模型/宿主Demo/真实保存全部0，no spawn/no CLI配置探针/no checkout/no formal edits/no commit/push。只写本reports-map允许目录，发布由根统一处理。最小登记修复：无。本分项可支持根最终有限登记资格；整包公共规则/110边独立审计及唯一写者后续接受/关闭按原门处理，不另加未来引擎或宿主要求。
