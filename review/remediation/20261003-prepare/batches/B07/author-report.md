# B07 作者候选报告 — RUN_ID20261003-prepare

本候选提交 WP28–32 的 19 项贡献（12 项主责），修订冻结的 8 份正式正文／附表／静态目录，并仅同步六份原稿的错误条款。所有项均为作者候选、待独立 Ultra；未批准、未关闭、未整合、未派发下一批。公共登记只交给 AREG 建议。

唯一作者基线为 `219cc3c182750155e9dbf2cb619f420b3922de27`；批准计划为 `41fffb540c6483f5296ea0d33b789b75180d27ed`，原 finding 最终报告为 `93e10babe0b9c9ef8b3f5277754541b447beeeb4`。完整合同是该基线的 `review/remediation/20261003-prepare/batches/B04/acceptance-stage-1/downstream-handshake.json`，不是旧 actual 或浮动分支。64 计划读、8 追加 B04 输入、35 冻结证据、2 管理输入和 7 固定计划身份共116条，均核对 commit／Git blob／SHA256／bytes；全量哈希不代表全文件语义阅读。精确身份见 [input-identities.json](input-identities.json)，本轮实际文本范围及未读部分见 [source-reading-log.json](source-reading-log.json)。

作者请求配置遵循用户2026-10-04 13:46最新指令：gpt-6.1-sol／xhigh／Standard(default)，覆盖合同旧 Max 管理措辞；实际有效配置无可信回显，保留 UNVERIFIED。方案 A 已接受，无新增认证或确认门。复审仍请求 Ultra／Standard(default)，其有效配置同样不能由作者认证。

六原稿同步依据本轮明确授权“同步错误原稿/净化正文/静态设计及本批追溯，正确原稿不反改”。先把路径、原 ID、旧／新 SHA256 与精确差异准备为 [original-sync-plan.json](original-sync-plan.json) 和 [original-sync.patch](original-sync.patch)，再写入；旧合同 read-only 门只在这六条具名错误路径和差异上由最新指令覆盖。WP29 原正确 BP 公式、WP31 正确取消条款及 BE13、WP32 原正确扫描时序均保留；WP19／WP21 已接受映射不反改。原稿新增定界状态说明只指本轮后继，不改历史批准对象。

行为改动恢复了主动回复量和上下文资格、树果数量三层及 EV 写入者边界、满级糖果取消后消费、入口相关 TR 记录、经验逐步截断／零份额早退、最初记录消费／空重学首次失败、遗忘摘要布局、进化白色预演及满队替换前提。条件范围先查原完整 controls、current_qualifications、effective_case_constraints、root_adjudications 和全部扩展，再落入本批消费者；其他主责路径不越界写。

逐 ID 作者验收映射见 [acceptance-map.json](acceptance-map.json) 与 [traceability.tsv](traceability.tsv)。下表是定位索引，完整验收、反例、资格、共责和未完成贡献以冻结合同与原 finding／finding-acceptance 为准；同根多定位仍仅沿用一个原 ID。

| 原 ID | B07 主责 | 正文定位 | 本批静态对照 |
| --- | --- | --- | --- |
| GIR-FD82-A020 | 是 | WP28 §5.3 → WP19 §3.5完整表N | IU-56;ST完整既有目录 |
| GIR-FD82-A024 | 否 | WP30 §6.3 最初记录实际消费者 | GR-49;GR-52 |
| GIR-FD82-A026 | 是 | WP28 §5.6 → WP21 §4.2完整表F | IU-57;FM既有目录 |
| GIR-FD82-A039 | 是 | WP28 §5.3 原始数量上限三层 | IU-49;IU-14;IU-15 |
| GIR-FD82-A040 | 是 | WP28 §6.6 → WP19 §5.3 | IU-50;IU-09～17 |
| GIR-FD82-A041 | 是 | WP28 §5.1 上下文拒绝/效果表 | IU-51 |
| GIR-FD82-A043 | 是 | WP29 §3.4及原稿售出·正常 | SH-08;SH-27 |
| GIR-FD82-A044 | 否 | WP28 §5.4、WP30 §6.3 | IU-58;GR-49 |
| GIR-FD82-A045 | 是 | WP28 §5.3/§6.2/§7 → WP31 §6 | IU-54;BE13原行 |
| GIR-FD82-A046 | 是 | WP28 §5.1主动HP请求表 | IU-52;IU-53 |
| GIR-FD82-A047 | 是 | WP30 §4.2 | GR-45～48;GR-15修前提;GR-08～18其它原行 |
| GIR-FD82-A048 | 否 | WP30 §6.3 | GR-50;GR-30～34原ID非空资格 |
| GIR-FD82-A049 | 是 | WP30 §6.1/§6.3 | GR-51;GR-25/26 |
| GIR-FD82-A050 | 是 | WP31 §5.1 | BE36;BE37 |
| GIR-FD82-A051 | 是 | WP32 §5、附表§4 | CX22原ID;CX39 |
| GIR-FD82-B008 | 否 | WP28 §3.5/§6.5 | IU-55 |
| GIR-FD82-B013 | 否 | WP32 §5持物依赖（§4/T2→当前持物读取） | CX40～42 |
| GIR-FD82-C003 | 否 | WP28 §5.1、WP30 §6.3 | IU-59;GR-52;GR-53 |
| GIR-FD82-D023 | 否 | WP29 §4正确表保留、§8显示边界 | SH-25原行;SH-28 |

两个整个目录保持旧 ID 顺序与重复出现次数。新增28行：IU-49～59、SH-27～28、GR-45～53、BE36～37、CX39～42；必要旧行修正仅 SH-08、GR-15、GR-30～34、CX22（8行）。BG/DC、RM/CP 章节完整原字节保持。CP20 的另一责任批更正仍待 B09，不因本批伙伴反例而倒写目录。所有新增记录都给静态预期和相邻反向对照，不称执行测试。

WP28 与 WP30 的正文发生变化，因此触发单独受影响 R-B04 复审。不能套用 B04 actual `9e2dadfa650e2111b77f9eae1f834cc00b8805d5` 的旧批准或报告 `acda1abc811cc07ea83c6a0930872e9a8cea174e`。正文变更前／后 blob、SHA256、bytes，追加8份 B04 输入和全部116固定依赖精确字节见 [dependency-manifest.json](dependency-manifest.json)。候选和实际整合版本各需独立 R-B04 Ultra，不能由 R-B07 或作者自检替代。具体调用边界见 [review-request.md](review-request.md)。

B06 WP24 输入精确为 `9e2dadfa650e2111b77f9eae1f834cc00b8805d5` 的 wp24-player-trainers-partners.md，blob `bb181b68d143f2a8bd09ba4e447a9867ed791336`、SHA256 `74ae842aed64fbb8a683ab8263c69113bdf89ceb0f3384855089dcbd24f224e2`、29351 bytes。仅保持已接受 §5.4／PT41–63 的六逻辑请求及引子交付前记忆，播放／暂停／恢复和正常返回清预置仍属 B04；不扩大为伙伴／雷达／完整 BattleAudio 批准。

已完成15项作者文本／Git 身份检查，全部通过，记录见 [self-checks.json](self-checks.json)：116固定输入、14输出身份、19／12 controls、六原稿差异、目录旧顺序／重复／保护章节、新链接、JSON／追溯、独立索引、参考精确且干净、主工作区未改及 diff --check。检查没有运行行为向量，不构成独立验收。

参考检出独立固定于 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，准备后只读。没有游戏／Ruby／编译器／转换器／生成器／反序列化器／参考模拟器执行，没有复制源码、逐行伪码、框架或 TS API。保留 U01–10／G01–12／AX01–20；二进制、mkxp 配置、实际素材／字体／宿主输出、插件与动态调用、备份、实际地图事件、具名未读配置与样本限制见 source-reading-log。运行观察0、行为向量执行0、参考执行0、已证 demo 链0。

本候选完整 commit／tree SHA 由提交后外部交付与普通 push/readback 收据给出，避免自引用。复审应在该完整 SHA 上读取全部新证据和未过滤 `baseline→candidate` 差异，而非只按摘要筛选正文。只向主仓 B07 分支普通 push，不写 main、不 force、不向参考仓 push；本报告不预先声称尚未取得的远端回读成功。

仍待 R-B07 全19／12候选 Ultra、单独受影响 R-B04 候选 Ultra；AREG 后续实际整合须绑定实际 SHA，再做 R-B07 与单独 R-B04 的受影响 Ultra，收到精确报告 SHA 后由父任务 C 接受。共有根、其他批贡献和严格条款各守其门；中央229 OPEN／0 CLOSED不变。登记建议只见 [areg-proposals.json](areg-proposals.json)。作者完成候选后停止，不自行批准、关闭或进入下一批。
