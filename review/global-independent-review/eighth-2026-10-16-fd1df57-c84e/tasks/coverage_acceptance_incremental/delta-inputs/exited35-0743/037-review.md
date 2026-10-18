# R8 Ruby / zlib 精确剩余文本接收报告

本子任务已接收固定读集的全部 **20907 个候选出处（Ruby 20817、zlib 90）及 13574 个不同完整文本**。候选集合 SHA-256 为 `8cdc30800211e75e7f04abc71eb242b88712bbe00222aac6fb7e9a682c5873e6`。先验证 gzip 容器与整体 decoded 身份，再逐候选验证真实 R 原始切片；没有使用 marker、抽样、脚本分类或旧任务批准代替实际阅读。全部不同文本按连续范围读至末行，截断位置已补读。此为本子集的实际接收，**不签署全域最终通过或 no-required**，父任务原 57948 分母及 Game 同文本出处不由本报告消除。

R 固定 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。B8 固定 commit `fd1df570cad987dc3852a3b958f03916e317f7fe` / tree `751dfde81048c81390f89a65ca1d1a565ba8e1ca` / formal tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`。报告分支 HEAD 不替代 B8。所用 18 件 R 消费者文件与 7 件 B8 规格逐件核字节、SHA、git blob；实际只读部分的文件不冒整件 FULL_READ。

| 逐候选处置 | 出处数 | 实际信用 |
| --- | ---: | --- |
| Ruby 运行库完整字面 | 19711 | 完整文字、名字、诊断、词汇、数值形数据及编译语法片段已读；不凭最近 COFF 符号授行为信用 |
| 完整跨行 NUL 字符串 | 553 | 536 个原始完整字符串、16235 字节已全部读到真实 NUL 边界 |
| 新恢复 YARB 程序 | 542 | 16 个容器全部结构、字面对象、ISEQ 与接线已读 |
| PE header / overlay 字面 | 9 | 原始切片及完整文本已读；不据外形扩大类型豁免 |
| Ruby `.data` 字面 | 2 | 原始切片及完整文本已读 |
| zlib 独立 DLL 字面 | 90 | 全部完整文本与原始切片已读 |
| 合计 | **20907** | **候选字面未读 0；不同文本未读 0** |

536 个完整字符串含诊断换行、AST 展示格式、源码行提示、预处理与 MJIT/C 语法片段。已按其完整内容接收，未把它们说成 536 个完整程序，也未把格式片段当其原生 emitter 控制流。真实 DIR64 指针检查没有覆盖本读集任何候选，故没有以指针或正则外形免读任何候选。

本上下文新发现并完整恢复了 **16 个真正的 YARB 3.1 builtin 容器，共 34524 字节、171 个 ISEQ、654 个对象、1002 条指令**。独立 inert decoder 只读取字节，不加载 DLL、不使用目标 Ruby、不构造目标对象或执行字节码。恢复保留全部指令、操作数、调用数据、局部变量、可选/关键字参数、catch、位置表与原始字段；所有非 padding 字节均落入解析结构，余隙全为零。202 项 opcode 名称/类型/长度取自目标 PE 表，固定官方 Ruby 源码仅作格式参考。`fields.location_first_lineno` 保留 serialized VALUE，不应直接当已解码源码行号；此限制已登记。

实际原生接线进一步证明：16 项 `builtin_binary` 的名字、payload 指针和长度逐项相符；`ruby_opt_init.part.0` 的 16 个调用使用相应 feature 与 builtin 表；115 个实际 builtin 表记录保留原始位置、argc/index/name、native 函数与 compiler 指针；120 个字节码 builtin 引用的 index/name 全部相符。三件 loader 函数完整反汇编及 16 个 caller 上下文已经实际读完；64 MB 完整反汇编仅生成并索引，**没有冒称全体原生 CFG 已读**。

已读程序的有限事实包括 Marshal.load 的 proc=nil / freeze:false 和 restore 别名，pack 的 buffer:nil、unpack 的 offset:0，Dir.open 的无 block 返回与有 block ensure-close，Time 初始化重复 zone 拒绝，GC.start 的三个 true 默认与第四 false，gem_prelude 的条件 require / LoadError 路径，以及 Ractor/AST/TracePoint 等能力的 wrapper 结构。它们证明可恢复的定义与分支，不能证明默认游戏会调用每项能力，也不能证明原生叶函数或真实宿主结果。

R 消费者已核脚本提取/组合、插件压缩/加载与 GC、文本收集、动画交换、神秘礼物、消息文件、保存/转换/语言直写以及 Marshal 拷贝/战斗记录。反向核读对应 B8 的 WP05/07/08/09/64/74/75 有界条款；双向关系与完整来源身份见映射与 consumers 文件。所读压缩/序列化、取消、局部保护、已完成前缀和无整体回滚边界，没有在本子任务形成可独立成立的必修规范缺陷；这不是全局 no-required 裁决。

依赖分开记账：Ruby 显式初始化内建 Init_zlib，但其 PE import descriptors 中没有 `zlib1.dll`。父 binary_remaining_texts 已独立核 Game 静态导入独立 zlib 的 `deflate`、`deflateEnd`、`deflateInit2_`、`deflateReset`；本上下文只额外完整读其该 descriptor 与四项，未借此认领全 Game 接收。静态导入不等于运行时选中路径。

交付入口：

- `identities.json`：合同、压缩容器、decoded 与两件原始 DLL 身份。
- `full-disposition-ledger.jsonl.gz`：逐 20907 原候选，保留 ID / inventory_line / encoding / offset / end / SHA 与精确阅读链接。
- `reading-ledger.json`：真实连续范围、补读、完整程序/字符串阅读，以及不得借用的信用。
- `bidirectional-mapping.json`、`consumers.json`、`consumer-source-identities.json`：逐候选、逐不同文本、程序事实、消费者与有界规格的正反向关系。
- `new-program-inventory.json`、`yarb-decoded.json`：16 容器完整身份、结构与真实 caller/native 接线；`proposals.json` 为八节新程序证据发现，提交 root 安排另 context 接收/反证。
- `remaining.json`：空的候选未读集合与具体 115 项 native leaf/compiler CFG、独立 zlib native、宿主执行及独立接收待决；没有把可读未读藏进材料限制。
- `progress.json`、`runtime-settings.json` 与 I/O receipts：真实状态、设置可验证性与全部工具成败证据。

目标行为始终 **NOT_EXECUTED**，正式修改 **UPDATE_NOT_STARTED**。没有 commit、push、安装或 spawn；输出只写 root 指定的本隔离目录，未改原证据。请求模型 gpt-6.1-sol、ultra、default/normal、Fast off；实际 model / effort / tier / Fast 四字段均 **UNVERIFIED**，因为没有权威实际回显。
