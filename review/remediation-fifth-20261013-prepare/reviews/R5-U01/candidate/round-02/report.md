# R5-U01 非作者有限候选复验 — round-02

**v2限定候选PASS**：只新增复验016、021的5个原失败标准，5 PASS/0 FAIL/0 WAIT；原243个已通过标准及其它32项对应限定贡献签名经实际未变身份核验后保持。组合34项/248标准为限定静态PASS，无内容返修阻塞。这不是新全批/全局审查。

固定候选 `005fc4fc48be9bad9d95fc4fa6afcc8fd00eddd6` / tree `925cb233989fb4b1be120fb1f5ac65a6e3bd46b7`；证据 `105de4e9e9c6a565867c8a064e47bba7c48e257a` / tree `16becbeb57958541a534da5a260f46968304b4dd`；原非作者round01 `1d0e9b30b474362a1fd8aad6e602a7a51cfb4fcd` / tree `6396b1914bffb3b52d76c96893f4a7e4518db04d`。

016/static/06：真实WP03行110与O003末句已明确GR5-M05-006／R5-U03及22fba冻结作者交接入口，说明仅投影、不复制四默认、主责贡献待实际接入、不声称B5已完成。原16 PASS条件与7向量保持。U01上游仍为空，U03依赖U01；不增加反向依赖循环。

021/static/01、02、04、reference_facts_to_cover/02：O048与真实WP14行267明确有效整数未知ID在非空表回首条、空表查询失败且不新建图块集/不回图块0；区域/版本与基础区域都缺失时新建未登记默认参数实例是另一分支。O049／DG17行269补非空表与有效整数未知ID前提，原成功结果保留。原空表7失败、非空首条7/未知23、参数缺配置默认向量及022邻文保持；旧全文冲突已消除。

逐项裁决（复用行仅保留原审者对应未变scope签名）：

| ID | v2候选 | 本轮新复验标准 | 保持原PASS标准 |
| --- | --- | ---: | ---: |
| GR5-M01-001 | PASS | 0 | 4 |
| GR5-M01-002 | PASS | 0 | 4 |
| GR5-M01-003 | PASS | 0 | 3 |
| GR5-M01-004 | PASS | 0 | 4 |
| GR5-M01-008 | PASS | 0 | 9 |
| GR5-M01-009 | PASS | 0 | 7 |
| GR5-M01-010 | PASS | 0 | 6 |
| GR5-M01-011 | PASS | 0 | 8 |
| GR5-M01-012 | PASS | 0 | 8 |
| GR5-M01-013 | PASS | 0 | 8 |
| GR5-M01-014 | PASS | 0 | 9 |
| GR5-M01-015 | PASS | 0 | 10 |
| GR5-M01-016 | PASS | 1 | 16 |
| GR5-M01-017 | PASS | 0 | 10 |
| GR5-M01-018 | PASS | 0 | 10 |
| GR5-M01-021 | PASS | 4 | 4 |
| GR5-M01-022 | PASS | 0 | 9 |
| GR5-M01-023 | PASS | 0 | 9 |
| GR5-M01-024 | PASS | 0 | 11 |
| GR5-M01-025 | PASS | 0 | 9 |
| GR5-M01-026 | PASS | 0 | 9 |
| GR5-M01-027 | PASS | 0 | 9 |
| GR5-M01-028 | PASS | 0 | 9 |
| GR5-M01-029 | PASS | 0 | 10 |
| GR5-M01-030 | PASS | 0 | 9 |
| GR5-M01-031 | PASS | 0 | 9 |
| GR5-M02-001 | PASS | 0 | 3 |
| GR5-M02-002 | PASS | 0 | 3 |
| GR5-M02-003 | PASS | 0 | 3 |
| GR5-M02-004 | PASS | 0 | 4 |
| GR5-M02-005 | PASS | 0 | 3 |
| GR5-M02-006 | PASS | 0 | 4 |
| GR5-M02-007 | PASS | 0 | 4 |
| GR5-M02-008 | PASS | 0 | 6 |

[逐标准裁决与精确原签名指针](criterion-results.json)、[必要实读及原证据复用](source-reading-log.json)、[限定回归结果](regression-results.json)、[独立验证](independent-validation.json)、[字节清单](review-manifest.json)。实际25文件投影只出现WP03:110、WP14:267、DG17:269三条单行替换；其它22投影、46原操作、32响应记录、243原PASS映射和133向量保持。49操作重建、完整B5补丁及v1→v2增量补丁在隔离/tmp应用均得到相同25份v2字节；171项TOOL_VALIDATION通过，不替代5项语义复验。

内容返修阻塞：无。实际接入/正式接受/关闭的剩余门：

| 门 | 状态及原因 | commit/tree |
| --- | --- | --- |
| GR5-M05-006实际贡献 | WAIT；本轮仅修主责引用，下游R5-U03贡献尚待实际接入 | 尚未提供实际接入身份 |
| R5-I实际整合及整共享文件 | WAIT；只能由唯一写者接入已通过限定贡献，整文件还须其它贡献 | 尚未提供固定实际commit/tree |
| 原非作者实际字节复审与唯一接受回执 | WAIT；候选签名不能移到实际字节 | 尚未提供受审实际commit/tree及回执 |
| U08有限整合/关闭门 | WAIT；正式接受和最终CLOSED均未发生 | 尚未提供关闭字节身份 |

M05实际贡献WAIT不反向阻塞此次U01引用修正候选PASS，也不新增U01→U03依赖边。候选PASS不等于实际整合、正式接受、整份共享文件接受或关闭；正式接受0、CLOSED0。

| 执行分期 | 记录或新增行为执行 |
| --- | ---: |
| R4历史review隔离参考记录（未重跑） | 4 |
| R4云端update新增 | 0 |
| R5 review历史隔离参考记录（未重跑） | 4 |
| 本R5-U01作者update新增 | 0 |
| 本round02非作者复验新增 | 0 |

原生宿主/Demo、真实文件/存档/归档、地图媒体、统计随机/跨宿主序列、动态扩展和无界输入组合保留NOT_EXECUTED或准确有界未知；133向量保持DERIVED_VECTOR。optional7、no-required7、政策6及M11-005 optional隔离。请求gpt-6.1-sol/ultra/default普速禁Fast；实际模型/effort/tier回显UNVERIFIED，不作额度/认证审计。

同一原审者任务 `01a1352e-01d1-765f-975a-e2917852301a`。本轮只写 `review/remediation-fifth-20261013-prepare/reviews/R5-U01/candidate/round-02/` 的6份review载荷，不改候选、正式131文件、公共台账、冻结历史或round01；未merge/push main，未动Mac。普通推送独立分支 `codex/r5-u01-independent-review-v2-20261013-22fba778`，完整新增载荷读回以审阅清单publication后继和最终输出绑定。
