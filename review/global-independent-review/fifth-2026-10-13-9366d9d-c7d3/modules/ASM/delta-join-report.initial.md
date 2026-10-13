ASM 有限整合草案已完成；这里只完成本次接收与定位工作，不代表全局矩阵获批、规格全支持或全部最后增量已收齐。所有输出位于 modules/ASM/，未写根矩阵、源、规格或其他审者文件；未启动其他任务，未执行参考、行为模型或宿主。

入口是 matrix-draft.json；按领域分片的 matrix-*.json 共1460个稳定审计 scope，绝非1460个独立产品功能。projection-draft.json 保留1295个投影，inverse-index.json 保留25704个逆向单位，semantic-index.json 保留3849个语义记录身份。723个文件保留432 R、131 formal、113 original、47 context的原分母和固定历史版本。

每个范围均有目的、领域、源/规格锚点、caller/override、前提、配置/宿主、实际审查范围、标准status及理由、审者/证据、发现、依赖和未知字段。具体事实由 evidence-fields.json 中的字段值与原文件/JSON pointer承接；来源为原始能力记录、同审者且范围重叠的具名语义段、明确登记ID、共享合同和已接受有限处置。相邻范围的规则上下文不自动成为该行每个条件。主审完整声明与规格supported/partial/missing/unresolved/not_reviewed分开。

字段定位仍保留431项：caller_override=97，dependencies=49，preconditions=246，status_reason=39。这些是本有限接收中未单独具名或仅有通用声明的字段定位，并非对应源未审或功能缺失判决；不能把列数当行为缺陷数。field-gaps.json逐项给scope、原始pointer、已查语义记录与草案字段位置。既有规则正文完整保留，未用统一‘无附加条件’补空。

已接收的后继证据：M05最终38个能力记录与当前分段、C00/BIN的6个条件父映射及909个精确候选定义连接、M08的原稿差异/精确复用及Shadow参数纠正、M02的6条/37子范围和006–008规范发现、REG的113原稿比较与最终接收、10个有效附件以及0–999形态上界纠正。root的33条有限处置逐项按(module, local_id)接入，旧root pending仅M02/REG由相应C00回执替代。

发现并处理M05快照指针漂移：222个不同旧/新pointer连接记录见 M05-pointer-relocations.json。按实际文件路径匹配当前记录；旧逆向单元可能对应当前多个更细分段，保留旧单位身份而不假装数组下标或分段不变。

39条M01责任路由明确连接原capability_refs与247字段合同中的对应记录；仅证明责任路由，不取得行为支持分数。5条RES范围投影到M12-ROOT-21/22/23/24/25，保留新格式/定义证据和运行边界。M10图鉴外域行保留自身not_reviewed签名，同时明确投影到已完成M11主审，不形成全局图鉴未审结论。M11的47条宽partial另列具名005子范围接收：只有匹配时序/谓词部分接必修，资源/图集/布局可选或无必修部分不扩张为整个源范围必修。

两个same_source_scope候选均不合并：四类迁移改变不同状态并具有不同兼容条件；区域地图页面交互与文本导入/导出是不同工作流。1295投影都有实际父身份；M12B root-tools一行仅责任导航，其余使用具名或条件化父连接。identity-aliases.json保留module/local_id/input_ref/scope_id/shared aliases，供父会话接JXN，未替代JXN裁决。

file-dispositions.json逐文件保留旧物理缺口、比较缺口、当前实审范围、精确复用、字段坐标、限定排除与接收证据。88个旧物理gap文件均有处置。空白、Markdown标题/列头、静态/历史证据资格与真正夹具前提分开；M04 assigned_semantic_ranges、M06明示shared premises、M02家族注释、M03分配范围和GCV13夹具/67边均按实际记录承接。LICENSE与历史manifest不伪签游戏正文，JSON字段审查不伪签全序列化行。资源分别保留完整已解码定义/格式和native/host限制，不以header签full。

剩余可得语义/上下文范围：
- `deliverables/final-specification-set/test-catalog/creature-rpg-wp27-28-29-30-33.md` [[242, 242]]：本草案没有找到覆盖这些具体段的主审接收记录，标为精确接收缺口；材料可得，不归缺宿主。详见该文件的 recorded_review_scopes 与 excluded_scope_dispositions。

M01的60项最后处置与JXN的97共享身份/182领域路由仍为 pending_parent_final_delta；没有读取未接受增量来伪造完成，也不等待它们阻塞本草案。父会话唯一负责根矩阵写入。

validation.json仅校验固定分母、稳定身份、父连接、字段引用值、文件范围和状态词；不充当语义重审或行为测试。模型/推理档位/service tier/Fast实际回显均UNVERIFIED。
