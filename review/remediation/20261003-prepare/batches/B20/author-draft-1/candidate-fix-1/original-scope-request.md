# B20 五组P2修复的精确原稿范围请求

修复基线固定为 `272885cca76c36cd04dde27b6be2c654759ec4c2`（先前冻结NEW为`1abaefb1db5818ff9404392143c476979d34c21a`）。两份复审的6个finding按C029重叠去重为5组，映射在repair-map.json。本包只向唯一登记者请求2文件、3完整hunk；身份和逐hunk before/after文本、哈希及声明映射见original-proposal/identities.json和declaration-map.json。

- WP75原稿：C024仅补§12.1分阶段失败及无独立索引产物；已正确方向、正常收尾及9/10/11门保留。
- WP77原稿：C028完整替换本批§5.4电话消费段；C029在§6.4后新增有界外层消费者门，原§6.4局部FormHandlers源审计句逐字保留。

原稿当前未应用。许可只准本包精确after，不代表质量PASS。现有第一轮19hunk许可不扩张为这次3hunk许可。ASCII定义错误只在正式WP75，原稿已有ASCII正确字面；CN错误仅改新B20-C003及后继case。旧195目录行、14个无改B20行、accepted owner规格和全部旧证据保留。

正式可写正文已修，后继5case与19项入口已建立。所有静态对照NOT_EXECUTED，运行观察和已证明Demo链0。父任务协调登记后才应用原稿；随后冻结NEW2、发布独立FULL及affected复审入口。作者不自签复审/接受/C/关闭。

大包规则：先前C→NEW的唯一完整差异继续按固定D/path/hash引用，不复制。后继拟只存一次本轮BASE→NEW2完整无过滤增量，连同旧C→NEW固定流与NEW→BASE三次元数据发布提交引用，形成可复算完整链；不会把旧差异文件内容再次包进一个递归C→NEW2大流。
