# B20 ACT 有界独立整合挑战

结果：**NO_SUPPORTED_ADDITIONAL_AFFECTED_BLOCKER；新增阻塞0**。本支持检查绑定 ACT `6babcf657aef559dbf101aeb093a1beb730ab507` / tree `7f511347be10a55ed1341f4132e198ac6bdedede`。它不是 root 的完整 affected actual 签署，不替代 FULL 门、正式 C 或 canonical 关闭。

管理包 M `66ba31f7895067c9d925aba20ce3de046fbf60e7` / tree `2f30f3ae648c593a32c52e2598a968bf677317ea`，入口为 `review/remediation/20261003-prepare/batches/B20/actual-freeze-1/affected-actual-dispatch.json`。独立确认 ACT 的唯一父提交是 G `405d7884058d30d94655be0b75f8f12eb07a15d9` / tree `31ed364e0d9617c1f126019476be9f768594e947`；M 是 ACT 后的管理发布包，不混为被审 ACT。

未变语义只归属固定已审 NEW2 `3f521e6dea0b442e4bb174a9715c458416386b37` / tree `49f406a6de8ca2786e5dda27abada19780fdfa05` 的独立 affected 报告 `cecc826263aab5e11cb51d1653bfb191306332c8`、最终包 `7c5309763a6cf2e31564a1fe42786ebcbfecbef5` 下 `review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-2/report.md`。该固定报告 blob `2c685037f1fdb6b5812a7fab42342b73c002d709` / SHA256 `2437ce8aebebcd829a07f9f238de858dc4564c7a2355aa8096f0e00925b1945e` / 15,232 bytes。新 actual 判定仍须检查整合消费者、管理增量及证据绑定；没有转签 candidate PASS。

## 独立挑战及判断

| 可能缺口 | 本检查的具体证据与判断 |
| --- | --- |
| ACT 自称七 payload 相同，但实际有漂移或额外规格写入 | 从固定 ACT 与 NEW2 各取全文件字节、blob、SHA256 和大小，七项全同；直接 G→ACT name-status 恰七个规格 M 路径；NEW2→ACT 112个路径均为管理/证据变化，规格变化0。相同身份支持复用既有源语义证据，不能自动给 ACT 质量签名。逐项身份在 companion JSON 的 `payloads`。 |
| 删掉候选大包使旧接受证据或当前案例断链 | NEW2→ACT 75个删除路径全在 B20 `author-draft-1/`；C→ACT 没有 B01–B19旧 owner 证据路径变化。当前 full19 active case map 显式绑定外部固定对象：14旧案例在 `005b747898137720f78548f0fb24bdf40f375232`，5修复案例按完整 map 的固定 NEW2 上下文绑定 NEW2，不按 ACT 缺失的本地相对路径取读。19 pointer全可解，选中case ID与目录ID匹配且都为 NOT_EXECUTED；51子例没有替代14旧对象或整个 qualified 合同。不存在“ACT必须复制所有候选证据才可审”的新增门。 |
| G 用标题、本地例子或许可缩减原合同 | 对 ACT G registration 的19条记录与固定 scope `924c7c3a7a5029b07ad18085cf2dadb594512186` 的完整 overlay，逐项核对 id/primary/primary owner、whole原对象与批准验收 binding、accepted与pending contributor。19整对象指针未缩减；38个原 finding/批准 acceptance 的 canonical对象SHA256均按固定原JSON重新计算匹配。两项 entire effective case aggregates 的完整指针可解。scope仅保留写入授权身份，未成为质量支持。 |
| 候选 FULL 或 affected PASS 被当作 ACT/正式接受 | 独立读取 FULL 固定最终包 `2d854ca5462876156d371554c56fd51b0003a472` 的四引用身份与19个per-ID pointer，全部匹配且均为candidate、NOT_EXECUTED、actual_gate_signature=false。affected19条导航行的精确UTF-8含LF哈希也全同。ACT新增19公共记录均 canonical OPEN、actual门PENDING、C NOT_PERFORMED；G registration的actual门同样待 exact ACT。M的public-registration-actual-binding只把原pending条目绑定ACT身份，没有签质量或C。 |
| 308旧接受被327物理行或新19 pending覆盖 | C `de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f` 的approval-ledger.tsv、traceability-successor.tsv及final-integration-review.md原字节都作为ACT相同前缀保留。两TSV旧308个原行和完整解析对象不变，新增19行（15主责）按G的19 ID次序追加，accepted/remaining contributors与whole控制一致。327物理行不是327接受。 |
| G后的源限制、非局部或旧消费者门被遗忘 | ACT integration/source-limits与M source-limits绑定固定 NEW2 completion/source-limits以及完整旧author contract，逐身份核定。U01–U10/G01–G12/AX01–AX20、runtime0、Demo0、static NOT_EXECUTED及whole root/extension/known source/nonlocal条件保留。NEW2→ACT没有旧规格、真实caller/data/conditions更改；仍要求root逐19owner实际消费边界判断，不能用owner自身文件不变或作者空route排除B05/B06/B11等间接路由。 |

上述有限引用核验共 **196个唯一固定对象身份、467个JSON pointer解析、38个完整原/批准对象SHA256和19个精确owner导航行哈希**，全部匹配。它是Git/JSON/hash/text元数据核验；没有无变化整库语义重读，也没有另存完整差异。完整C→ACT与NEW2→ACT流的唯一发布、无过滤独立重建由root统一核验并引用；本子检查只读取name-status和固定管理元数据，不宣称代做全流门。

## 旧计数说明纠正

旧报告保留，不回写。固定旧最终包 `be3363e8711bdf17b0f08e22517ec3bb00f9ef55` 的 `affected-review-cloud-20261011-1/b20-preservation.md` 曾写“B10–B19本地158条完整控制哈希”。同包固定 `b20-preservation.json` 的 `local_acceptance_control_hashes` 十个数组实际为 **138**：B10–B19分别7/6/9/8/24/16/24/12/8/24。此次独立重数为138，并确认十份固定C接受receipt在ACT全字节相同。这是旧支持prose计数笔误，不能把138当作308总接受的替代，不能据此宣称20贡献丢失或缩减任何完整qualified条款。新actual报告应透明写正确计数并继续引用旧固定证据；不新增质量阻塞。

## 输出及执行界限

详细支持数据为同目录的 `b20-act-challenge.json`。本子审只生成自己的 `/tmp` Markdown/JSON；只读fetch缺失的固定FULL候选对象后再判身份，没有把本地未取对象误判为已发布路径缺失。未改repo正文、main、原稿、参考、旧报告或接受状态，未commit或push。

没有执行参考游戏、Ruby、编译器、转换器、反序列化器、生成器、行为向量或历史脚本；只运行新写Git/JSON/hash/text元数据代码。所有静态案例均未运行，runtime observations0、proven Demo chains0。未签FULL、C或canonical关闭。
