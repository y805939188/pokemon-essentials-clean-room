# GR3-U03 独立候选定点复核 attempt-02

**四 ID 均 PASS（固定候选静态范围）。** 唯一返修问题 `U03-M04-R01` 的原验收条件已满足，当前没有必修阻塞或新增问题；这不是实际整合复审、正式接受或 CLOSED。所有设计仍 `NOT_EXECUTED`，参考／游戏／像素／动画／行为案例／模拟／真实 Demo 运行均 0。

受审返修作者 commit `c2c33502e88c14b90c3936d4cf00a6d5281b4cd5` / tree `6eaae6cda23cbde383e1ee5fbf084dea6b492d26`。原作者 commit `5450e35caae225cad69d3f754200b4e7062989e9` / tree `b5e51359cd8e1efabd98a41ac1fdc7d9ca9fdaee`；独立 attempt-01 commit `baea5d632f469bdc9b3a32052ba97b68508fc94b` / tree `6df26a846e8825da3a23a976c924f4db862b72d6`。正式 D、管理 M、H、只读 R 均沿用原固定身份，见 [input-snapshot.json](input-snapshot.json)。

复核由原独立主角色 `/root` 与原细项角色 `/root/spinda_review` 完成，均独立于作者和唯一整合登记员。根 AGENTS 已读，适用范围无本地补充 skills。`gpt-6.1-sol/ultra/default` 请求继续接纳，配置回显及不可见作者任务 ID 保留 `UNVERIFIED`，未查额度／后台、未用隐藏模型 CLI。仅新增本 attempt-02 六文件，attempt-01 与作者／正式／旧报告／参考／main／公共台账只读。

## 原唯一问题的定点验收

| 原验收条件 | 新候选位置 | 独立复核结果 |
| --- | --- | --- |
| WP21 概述及帧合同限定分帧 PNG；原生只证明一次宿主位图修饰请求 | WP21:101、157、159、161、163 | PASS：可枚举独立帧的分帧 PNG 才保证各帧各一次／不串色；原生内部各帧读写覆盖、显示及时序仍未知，没有“只改首帧”或必然成功／失败断言 |
| SP07 明示双帧 PNG；保留数学预期；原生反向不签两帧终色 | 测试目录:253、263、266（SP10） | PASS：两朝向的 SP07 限定文件名指定双帧独立 PNG；两个单次命中块由 RGB200／100 分别推出 (200,85,125)／(100,0,25)。SP10 改为原生两帧输入，只记录副本宿主位图一次请求及内部覆盖未知；两组均 NOT_EXECUTED |
| 追踪提案同步限定并更新完整镜像、identities、全 patch；其它数学和入口不改坏 | traceability-proposal `/entries/0/source_evidence/1..2`；八文件 manifest／patch | PASS：帧说明一致，新增固定 AnimatedBitmap 证据身份正确；八镜像身份匹配、完整 patch 在临时副本检查及应用后八结果一致；相关数学／形状／颜色／重叠及既有入口与旧静态行保留 |

固定源仍是 `Maruno17/pokemon-essentials` 的 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。本次定点复读 `009_Species_files.rb:86–109`，以及 `008_AnimatedBitmap.rb:14–18,25–33,48–64,105–106,119–123,167–172,202–205`（实际多读的相邻行在 snapshot 标明）。资源副本交付项修饰与两种枚举模式支持新限定；没有源码内逐个切换原生帧的证据。未运行或生成任何素材，不要求宿主运行补证。

位置均相对返修提交下 `review/remediation-third-20261012-prepare/U03/candidate/deliverables/final-specification-set/`。WP21 对应 `pokemon-rules/wp21-dynamic-forms-and-display.md`，测试目录对应 `test-catalog/pokemon-rules-wp19-21-22-23-34.md`。

## 四 ID 裁决与证据复用

| ID | 裁决 | 本次依据 |
| --- | --- | --- |
| GR3-M04-001 | PASS | 原数学／形状／颜色／重叠验收在完全相同条款字节和原前提下复用；动画边界由以上 fresh 定点复核补齐，原反例现在被明确限定 |
| GR3-M05-001 | PASS | 六份未变镜像中 WP18、WP24 与尺寸目录逐字等于原受审字节；复用 attempt-01 `/verdicts/1` 的完整前提、反例、两条验收和局部未知 |
| GR3-M05-002 | PASS | WP28 与道具目录逐字未变；复用 attempt-01 `/verdicts/2` 的过滤、三路响应、取消／部分提交与宿主限定证据 |
| GR3-M06-001 | PASS | WP30、WP28 与经验目录逐字未变；复用 attempt-01 `/verdicts/3` 的提示时点、钳制差量、友好／等级门与糖果前向限定 |

原完整前提／反例／验收和原报告 exact identity／JSON pointer／对象 hash 均见 [per-id-verdicts.json](per-id-verdicts.json) 与 snapshot。此次限定复用的是相同字节、相同前提的局部证据，未将旧 PASS 转移到变更条款或新范围。原 18 控制／39 局部贡献的 complete qualified scope、IHC-003/004 排除与原身份 joins 仍由固定 attempt-01 snapshot 承接；regression-scope 和关联未变正文／静态行字节不变，不重审全 229/341。

实际作者 delta 恰为 7 个允许路径：WP21、对应 Pokémon Rules 测试目录、author-report、author-self-check、candidate-identities、candidate.patch、traceability-proposal。完整 delta 已独立读取。只有两份候选镜像更新；其余六份字节、其余三项作者自检对象及 traceability 对象未变，registration/model receipt 未变。WP21 的位组、锚点／形状、RGB／2×2、重叠及数学对照段逐字未变；旧测试目录前缀、SP01–06/SP08–09 行逐字未变。案例计数只作保全记录，不作语义质量证据。

新完整 patch 为 47396 bytes，SHA256 `dd1de8ee2cf12cf5c81344bae889cfbe58dcc367ebc820331fd38f9c23b2bf97`；在仅临时副本执行 `git apply --check --whitespace=error` 及 apply，八结果逐字等于冻结镜像。15 件作者交付已从隔离 Git 远端实际读回，全字节／身份匹配。未改或 apply 到正式文件。

WP28 归 U03 唯一候选作者；此次候选 PASS 之后仍须唯一整合登记员建立真实 actual commit/tree/changed-path identities，再另行独立复审实际整合字节及公共承接。U03 实际整合独立接受后才以精确新 WP28 commit/blob 顺序交 U04，U05 消费 U03/U04 接受后的冻结结果。U08 未启动，M02-003 未重开。

资源／越界像素／原生内部帧／显示／音效／时序／异常会话／真实 Demo 保持未知；未来 bug 政策、尺寸产品范围及默认艺术／视觉重设计不作本次新增阻塞。报告不可递归嵌入自身 commit；普通提交推送并远端读回后的精确 commit/tree/path 在最终外部回执给出。
