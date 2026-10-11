# B21 exact ACT affected navigation / qualification / public G independent subreview

结论：**PASS_SCOPED_EXACT_ACT_AFFECTED_NAVIGATION_QUALIFICATION_G**。对本次精确 ACT 的导航、批准资格、B01/B18 公共管理接口及新 G/actual 绑定，没有剩余本范围阻塞。此结论新签 ACT 受影响子范围，不是沿用 NEW2 候选 PASS 代签 actual；未给 FULL、B21 C、canonical 关闭、FINAL-1/FINAL-2 或 main merge 签名。

被审 ACT `d7b9f0882ce873eade1e57bf2a4aa76f7b329b0e`，tree `aed1622a540c3fb9c898e1c7b94741be319f7a83`；唯一 G 父提交 `d13eedb893abaf39322a022beba1d0a24f43b8aa`。外部管理包 `b49aa3c2c1aa6992539b06a555477db33b75c0a4`，tree `72fdb37b03fdf59caa522f262becd85f25fac7c7`，不是 ACT。候选 NEW2 `e58486178e746273fb6fab55df00722807f1dc44`，正式基线 B20 C `e9c140dc33de1cb0662521318b051174909e4509`。

先读管理包 `review/remediation/20261003-prepare/batches/B21/actual-freeze-1/affected-actual-dispatch.md/json`、`frozen-output-identities.json`、`public-registration-actual-binding.json`；然后读 ACT 的 `integration-stage-1` 新登记与明确限定，并依据原派发 `eb1885265fcde2a52767077de3193862036c3a71` 的完整控制核对新登记。原资格、未变语义采用此前独立证据的精确归属；本轮新读的是实际管理差异、当前位置/身份和新的登记绑定。

使用新写只读 Git、UTF-8 文档、JSON/TSV、哈希元数据代码；不执行仓库或旧审计脚本，不执行参考/游戏/Ruby/编译器/转换器/反序列化器/行为向量或案例。参考执行0、静态案例执行0、运行观察0。本子审仅写 `/tmp` 新文件，不改仓库任何文件。检查数量是审计范围记录，不是质量通过依据。

## 完整差异与精确不变复用

两条未过滤完整差异独立重建为 Git 默认 rename detection 的 `--no-ext-diff --binary --full-index` 输出，逐字节与管理包已发布对象相同；只固定引用，不复制差异。

| 固定管理包 M 中路径 | Git blob | SHA256 | bytes |
|---|---|---|---:|
| `review/remediation/20261003-prepare/batches/B21/actual-freeze-1/complete-C-to-ACT.diff` | `ea8912a48c1a1771176361218bad0beb6a6de449` | `7c293d12cae6badaa58f9361c607811f273830a63653815ef0b6cce3621fcd48` | 2297767 |
| `review/remediation/20261003-prepare/batches/B21/actual-freeze-1/complete-NEW2-to-ACT.diff` | `aa769a802b884cdf0615646d01f4a79c514d0f95` | `7dce7af42a9ea2fee958d981a896463d896d78dca85a8b7c62cdbef4a4d5c995` | 4520793 |

NEW2→ACT 的默认差异展示含两项 rename；其删除/新增展开计数按 `--no-renames` 的62路径事件解释，不能把展示块计数当作缺漏。候选完整流只保留原 P2 固定引用，不替代 actual 流。

22份复制 payload 在 ACT 与 NEW2 的 path/blob/原始字节身份相同；三份公共管理路径与 G 同字节、与 NEW2 管理层不同。所有111个实际当前 consumer 的文件身份在 ACT 重新核对，并与此前独立核验的 SHA256/bytes 相同。当前两份 WP75 与最终 engine 目录的身份取 ACT 实际路径，不能以授权提案 after 文件替代；它们与已独立审查的 NEW2 对应实际字节相同。B20 新段落不受历史 B20 C 旧批准自动覆盖；其本 ACT 行为回归由对应 owner 子审另行给限定结论。

此前自身导航证据的固定复用入口：`53a14af81c1c139da047c51450a84aa7bee9b225:review/remediation/20261003-prepare/batches/B21/affected-review-cloud-20261011-2/navigation-and-junction-review.json`，SHA256 `eb6f770ccf517eece80ce6ba01287920f80faa08fdb2f91f6d11267edb19af47`。同目录 `.md` SHA256 `7a24430cf40203ab467b665fb3d3e9f212f831fb927cc3dc7f0466cc782d07b8`。本轮重核其14个审计容器身份；47 mapping、54当前交界（解码JSON列的规范对象）和8链的原始独立对象哈希逐项相同。语义证据只作固定 pointer 归属复用，没有递归复制旧报告、完整批准对象或历史证据包。

## 外部固定证据的消费可达性

ACT 本树没有候选 `author-draft-1` 的32个证据路径。22份原样复制 payload 中共有14个不同的 author 命名空间消费路径：13个由管理包 `frozen-output-identities.json#/author32_evidence_fixed_at_NEW2_not_actual_paths` 明确固定在 NEW2；`freeze-2/frozen-NEW2.json` 由同文件 `/candidate_author_freeze` 固定在 P2 `9b6d16e34daf59e205f8a3df20e24930175064ed`。所有使用路径都有上述精确 commit/path/blob/SHA256/bytes 映射，未发现未映射目标。公共 trace 的14新行另外把 `whole_author_trace` 和 `nine_repairs` 明确绑定 NEW2；scope/regression 管理证据也把 application/dependency-refresh 绑定 NEW2。

因此本复审在**ACT 加已明确提供的固定外部管理包/NEW2/P2 证据**范围可消费这些索引。正文中的旧相对 Markdown 链接及 wp78 的裸 author index 不是 ACT 本树可点击链接，不能声称 ACT 自带这32个文件；完整候选取证保存在对应固定提交。冻结管理包将其位置分层，是本次允许固定证据复用的实际入口；不把文件缺席误判为原作者证据被毁，也不把裸路径本身当作本树可达证明。

当前54交界/source432/config35/UI17实际 payload 不变；8链和47批准映射在固定 NEW2 可准确定位，111当前 consumer 在 ACT 实际路径存在且身份匹配。所有未读/备份/二进制/宿主/插件/动态激活/缓存/样本限定继续存在，不因路径存在或旧 PASS 扩大为全读、运行或启用保证。

## 新公共 G 与 ACT 绑定的独立判断

ACT 新 `integration-stage-1/finding-registration.json` blob `17d226fef6b7105c1d957314c4da494b6a06e53a`，SHA256 `927c70293fd5e7115f5a474dce7c328c0ad2bdddc1d4c8784137c0049d41ac63`，39280 bytes，`/records/0..13` 全部重新核对：ID/顺序、9primary/5shared、原主责、完整原对象与批准对象哈希、原 complete-control pointer、已接受与待接受 contributor 集合与原 D 合同及旧独立14对象记录一致。`remaining_contributors` 都只含 B21，没有把新字节授予旧 owner 接受，也没有把同 ID 当作 whole qualification 的替代。

两份公共 TSV data rows328–341 的 `remaining_obligations` 逐行一致，并与对应 G record 一致；实际 G pointer 解析到 ACT 本树 `/records/0..13`。候选 FULL/affected 分别引用其固定报告提交，actual review gate 仍待执行，B21 C/closure/FINAL 均未执行。字段名 `accepted_candidate_contribution` 中的值明确是 `B21_G_INTEGRATED_PENDING_EXACT_ACTUAL_AND_C`，不是接受签名。327旧行的原始字节前缀在两表完全保留。

管理包 `public-registration-actual-binding.json` blob `d0e709cfb0e858fbcc3b90e0a7b8242fb58b21ba`，SHA256 `1d0a3d8891653b8049fb2699114ec9178e895ab9d3e8940fb69e503e71e66a8d`，19395 bytes，其 `/new14_rows/0..13` 的每个 public row index、G对象身份和 exact ACT/tree 绑定均已核对。ACT 表中 `EXTERNAL_ACT_FREEZE_REQUIRED` 是 G 的冻结前占位；由此固定外部对象对本 ACT 唯一消解，不是 actual 已通过，也不改变历史 ACT 绑定。管理包的 quality_verdict/B21_C 仍 null。

三公共路径 actual 身份如下，固定 commit 都为 ACT：

| path | SHA256 | bytes |
|---|---|---:|
| `review/remediation/20261003-prepare/approval-ledger.tsv` | `401fa6e8984c8b75acd382cd5a0f47a8671bce7fb27d4040cdb8cf8f0b9768fc` | 740356 |
| `review/remediation/20261003-prepare/traceability-successor.tsv` | `da1e2003ae43264233b2e2f8d64f9a8d7ef8913e87fd9eea698ea81f33048a6a` | 1035830 |
| `review/remediation/20261003-prepare/final-integration-review.md` | `0cebc77c6580f2d871437ba41aed89dc47d4fe43454d47855649d7bfd2959979` | 104051 |

新的最终管理附录明确：旧327接受维持；新14仅 G 注册；22 payload 被复制且需要 exact actual 复审；后续 C/229关闭/FINAL 门不在 G 执行。旧作者 header 的“等待 R-B21”作为冻结候选层保留，当前登记优先级依据新公共G段及外部 ACT 绑定；不会把保留旧 header 解释成撤销已发布候选报告或已接受旧贡献。

## G9-3、B01/B18 与九原输入资格

G9-3 五个限定管理条款在 ACT 实际路径原样存在，其限定区间 SHA256 与旧独立 NEW2 证据相同：

| 当前 ACT 条款 | lines | range SHA256 |
|---|---|---|
| `planning/feature-matrix.md` | 1–16 | `199856ceab0c6a6d55e62c98c453e6de2febcd01f21a4a216204cb956e3860fb` |
| `planning/review-manifest-2026-09-19.md` | 4115–4127 | `caff5115fb27503be8bf08595aa4c074034385e1e9a2adccbd1424e445ef55b9` |
| `audit/source-traceability.md` | 1–18 | `318f62c9379fb666dbc3bdfd5c1081065cc83d5942d490805013b6276bc4b1fd` |
| `deliverables/final-specification-set/README.md` | 1–16 | `c7fb64de645801993206c0b7153e3db0b0aac24a6299d814c674529d0cc9dc51` |
| `deliverables/final-specification-set/scope-statement.md` | 1–16 | `6c4f03c86c06ed760af924c309c69d8082a56cd1453f19eb38533da1e13814ad` |

本轮实际读取这些条款，并与新 G 公共层联合判断：原输入批准、候选字节、旧已接受贡献、新 pending G、exact ACT 审查和 canonical 关闭仍各有资格，327接受不能推为229关闭。原 audit 固定旧 NEW whole identity 的差异只在随后追加部分；本轮引用的是当前 ACT 整文件身份及同字节限定1–18行，不把旧 whole SHA 当作 current whole SHA。

B01/B18 真正旧 scoped 证据在 ACT 的 B20 completion-statistics 与公共 trace 中再次逐对象核验：

| owner / contribution | receipt pointer | receipt object SHA256 | trace data row |
|---|---|---|---:|
| B01 / GIR-FD82-001 | `/accepted_contribution_receipts/0` | `5fb446c8a83d7fe2ee509346c5aff9ee8948e078f6cb9f28a79ac0eea6567b40` | 1 |
| B18 / GIR-FD82-001 | `/accepted_contribution_receipts/276` | `e972644594a9a560d160751768b6b473e8afc40055fd705d9883e625383ac530` | 277 |
| B18 / WP80-INTAKE-R02 | `/accepted_contribution_receipts/283` | `da9e324e49fc1999fef0a2016a302b1f93d4d752e4aa6558f6600dd39d7bc43c` | 284 |

新 G `/records/0` GIR001 的 old accepted contributors 仍 B01/B18，pending仅 B21；`/records/13` R02 old accepted 仍 B18，pending仅 B21。旧 owner 的限定接受有效，新管理字节单独由本 ACT 审查判断；没有向旧 owner 借签名。两表旧327原始前缀完整保留，本子审亲核上述三个 scoped 对象；全部327逐对象保全由父审计另行完成。

九原输入的原/最终18个当前文件和9个旧 snapshot 在 ACT、NEW2/C 的固定身份相同。先前独立直接字节推导的2同字节/7各唯一路径重映射且+41，以及原批准报告资格，按固定证据 `#/nine_input_fresh_byte_derivation` 复用，本轮没有重做整套历史语义审查。`nine-input-approval-successor.json` 固定 NEW2 SHA256 `9c2a34d7ed15738b68d9863c110571d7669ccac0491e1f6c42843bf3e0dca7f7`；旧批准不移交给当前修改正文、不移交给新 B21 接受。

## 原 NAV、C029 与当前支持范围

原 NAV-001 的 FD003 record4/9/14/15 保持真正的 B19 WP72/73、B17 WP67-A/WP76、B14/15/16 WP60/61/63/65、B16/17 WP66-A/WP67-B 具名消费与完整限定批准。C029 record39 与 trace record9 的真实形态 owner 仍是 B20/WP77 §6.4；B05/WP18/21 一般机制和 B19 editor 只是另外的消费者，不成为 C029 已接受贡献。ACT 新 G `/records/9` 及新公共对应行只列 B20 旧接受、B21 pending，原 OBS 归属修复没有回退。

CFG25/26、SRC392/393 保持具名 current consumer 的机制、局部样本及启用未知分层；同字节 source/config/UI 的 qualified consumer 不被管理G扩展为PBS全读/自动激活。收获 A23/A31/A33 的 WP28机制/WP66-A UI 与 L09 的 WP35机制/WP67-B UI 保持分列，未再误归彩票/挖掘。新的 scope-grant-after WP75 bridge 与 CHAIN6、G7-4/G8-2/G8-3 的当前 ACT 文件身份已由111 consumer和22 payload的字节同一性覆盖。

原 NAV-002 所要求五条管理入口、真实 B01/B18 scoped receipt/trace、九原输入批准链在 ACT+固定外部管理入口下可准确消费；新公共G/ACT绑定另有本轮独立判断。47完整批准映射、14 whole控制与54交界8链的限定语义引用原独立报告对应 pointer 保留，未用局部例子、同ID或作者完成数量代替。

本范围验收条件已满足：同一 exact ACT/tree、明确管理包与外部证据身份、可归属的当前 consumer、原批准/旧接受/新待接受分层、新G不越权签 actual/C/closure。最终 all20 affected actual 结论由父审合并；FULL actual、B21 C、原 FINAL-1、证据支持的唯一登记员关闭与最终冻结、FINAL-2 仍须逐门另行协调。伴随 JSON 记录本轮实际身份、public14新绑定、current111、五G9条款、九输入保全、外部14路径映射及核验结果，不含完整差异或递归历史证明。
