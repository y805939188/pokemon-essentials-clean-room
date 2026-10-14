# R6-B shader 独立子审报告

本子审完成固定 R 的全部 55 个可读 shader unit、1297 行逐 unit 全文语义阅读，并直接核原字节及提取文本的 55 份 SHA256，全部吻合。另读三个有限前缀。本轮新必修发现 0；既有 GR5-BIN-001 的可选范围判定保持。root 当轮 55 份 shader 事实由非提出者独立核对，未发现其数学、分支或 optional/宿主选择边界需要纠正。

固定 main `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`，工作树 `6ab3429170d2762607fbc2237014c3a160449fa1`；正式树 `1046fbb657882e84b3dfc6d017943a9edf7782e5`，131 文件。R commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0` 已直接核。没有修改参考或正式文件，没有运行参考、Ruby、shader、GPU、行为模型、宿主或 Demo。

## 阅读与反证范围

[reading-ledger.json](reading-ledger.json) 逐一记录 55 unit 的完整阅读段、精确数学/分支行、独立手写事实、边界及身份核验。全文通过四批工具输出阅读；自动枚举、JSON装载与哈希只属 TOOL_VALIDATION。55 unit 包含 66 个函数定义，其中图案混合的未直接消费标量重载也读。0053 的可打印尾字节 I 已计入全文；完整 unit 不能误解为所有文本均可独立编译。

当前 WP15（220 行）、WP16 世界绘制正文（343 行）、scope（153 行）及对应 WP16 测试目录（201 行）均全文语义读；mkxp 配置159行全文读，图片消费者58行全文读。其余雾/画面、缓存/色相/合成、灌木与转场消费者为明确行段实读，见 [support-reading-ledger.json](support-reading-ledger.json)。不宣称本 agent 全审131，也不代签 controller1678行、compat脚本、CIL工具、字体/SF2或PBS。

[forward-traceability.json](forward-traceability.json) 为每个 shader 的事实→可定位外部逻辑请求／native 未证→现行可选或逻辑条款；[reverse-traceability.json](reverse-traceability.json) 从当前具体条款和测试边界回查，未把属性请求当作 shader 选择。缓存色相及合成的宿主请求可定位，实际 program、参数归一、配对、拼接与上传长度仍未证明。

[root-counterevidence.json](root-counterevidence.json) 绑定本轮 root 的 `evidence/shader-reading.json` 哈希，逐55条给 root 精确行为行及本agent新源行。支持结论只及给定输入下的可读定义。当前另未见root的独立shader必修提案；如后来该文件改字节或另提必修，需要按新候选重新核，不转授本次判定。

## 数学与顺序裁决

可区分的关键次序已经核清：49灰度→色调→主体alpha不透明度→覆盖色；56随后闪光；61先图案后灰度、覆盖后可反相、最后灌木alpha门。57先形成源有效alpha及剩余目标alpha，零总alpha仍保留源RGB，非零才归一。42在区域乘0前已经读取帧表和做除法，区域外不是保护；37的第二门读取第一次偏移之后的横坐标，两个门非互斥。61纹理y等于深度落较暗侧。470与471的采样alpha语义不同，YUV双平面UV通道顺序和三系数族不能混同；497读取两个变换系数而没有把原角转换成sin/cos。

[math-vectors.json](math-vectors.json) 给18个普通／最小对照设计，全部 DERIVED_VECTOR / NOT_EXECUTED。例如49指定红样本、全灰度、红偏移.1及蓝覆盖.5时得到RGB=(.1995,.1495,.6495)、alpha=.25；把偏移改晚，红=.2495。这个差异证明定义数学有意义，未证明当前游戏选择49，也未与现行属性级合同矛盾。47的核常因子经每轴权重归一消除，不因该原始因子缺失指控恒定色变暗。

[prefix-and-order.json](prefix-and-order.json) 区分文本词法作用和native拼接：默认精度／桌面别名前缀、矩形采样及UV比例.5前缀、UV比例1前缀均新读。前缀必须在使用前生效才能影响后续词法；二进制储存偏移不证明其被拼在何处或实际选中。提取目录中的非55登记孤立影像 BIN-0466.txt / BIN-0481.txt 与该ID inventory原跨度不同，故明确不用作这些ID来源；三个前缀直接按固定原字节核，不新增 shader 分母。

## 规格范围裁决

[findings.json](findings.json) 重确认同一个历史 GR5-BIN-001，不新增 canonical，不升级 mandatory。现行 WP16 第3–11行及scope第139–153行保留架构中立／宿主未证／optional隔离；旧GR5的具体optional登记只用于范围审核，不代替本轮源与当前正文实读。全正式根相关归一数学关键词0命中，以及Data/Scripts直接shader绑定词0命中，见 [negative-search.json](negative-search.json)；它们只是辅助负搜，不是不存在native或动态消费者的证明。

如后续明确纳入可选视觉兼容数学，可建立实施独立的输入／阶段／分支／边界附表并同步正文链接、测试、Feature Matrix和追溯；不得要求独立实现采用55个原GPU程序、GLSL或旧类层级。此审查没有授权或启动该 update。

## 保留限制与完成状态

[limits.json](limits.json) 给7个精确边界。可读shader文本未读余量0；native选择、GPU精度／采样／输出夹值、实际纹理／媒体／像素与Demo仍未证明。无参考／模型／GPU新执行，运行观察0，已证Demo链0。实际 model、effort、tier、speed和UUID均 UNVERIFIED；未探测认证、会话、配置或额度。

仅写本 task 子目录。status 为 `COMPLETE_SCOPED_STATIC_REVIEW`；这是55unit的限定静态完工，不是全Game.exe native或未来renderer兼容验收。
