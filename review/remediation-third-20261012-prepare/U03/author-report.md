# GR3-U03 U03-M04-R01 定点返修候选

状态 **CANDIDATE**，等待同一独立 reviewer 定点复核；作者不自签 PASS、正式接受或 CLOSED。

基于作者提交 `5450e35caae225cad69d3f754200b4e7062989e9` / tree `b5e51359cd8e1efabd98a41ac1fdc7d9ca9fdaee` 正常续写 `codex/gr3-u03-author-20261012`。固定独立复审 commit `baea5d632f469bdc9b3a32052ba97b68508fc94b` / tree `6df26a846e8825da3a23a976c924f4db862b72d6`，attempt-01 的 report/findings/per-ID 仅只读；精确 blob/SHA256/bytes 见自检 revision。管理M、H、正式D、只读参考R仍为 candidate-identities.json 中原冻结身份，根AGENTS已读、无适用本地skills。gpt-6.1-sol/xhigh/default请求承接，配置回显UNVERIFIED；无后台审计、模型CLI或子任务。

## 唯一返修内容

- WP21:101 及 §3.2-R03:157–163：逐帧各一次／不串色限定为文件名指定分帧、可枚举独立帧的 PNG。宿主原生两帧 GIF/bitmap 只记录一次宿主位图修饰请求，内部各帧读写覆盖、显示及时序未知；不推只改首帧或显示必成功／失败。
- SP07:263 明示上述两帧分帧 PNG 前提，保留数学终色 `(200,85,125)` 与 `(100,0,25)`；SP10:266 新增原生动画反向静态记录。共同前提:253 和正文目录导航同步。
- traceability-proposal.json 仅修 M04 的帧说明并加入固定 R `008_AnimatedBitmap.rb` 定点证据。源路径／行／hash只在审计提案与自检，不复制源码或设计框架结构。

GR3-M05-001、GR3-M05-002、GR3-M06-001 的 attempt-01 独立 PASS 保留在固定原报告，不重做；对应六份完整候选镜像及三项作者自检对象逐字／逐对象不变。共享目录中已有 ST/FM/ME/SH/BR 等旧行以及 SP01–06/SP08–09 保持原字节，编号、四形状、颜色、共享2×2、重叠与蛋／正背／物种入口事实未改坏。历史原229/341及资格均不重开、不转签新字节。

现在共有46条新增静态设计（只比上一版多SP10），全部NOT_EXECUTED；625条原静态目录行保全数字仅是文字检查，不能当语义PASS。游戏、参考Ruby、像素／动画宿主、行为案例／模拟与真实Demo链执行均0，无新素材。原生覆盖、真实资源／宿主与未来bug／视觉政策继续未知，不阻塞事实限定。

8份候选仍是完整上下文镜像，manifest只更新受影响两文件的new身份及全patch身份。candidate.patch 仍是全部8正式路径对固定H/D的完整差异；只在临时副本核验，未apply正式目录。作者本次 delta 仅7个允许路径，registration/model receipt 未改，旧独立报告、正式131、公共登记、main及reference只读。临时patch／字节与有界保全结果见 author-self-check.json；作者写范围无阻塞。

返修内容提交的精确commit/tree在一次内容提交后由本报告绑定，最终报告载体身份在最终交接回显，不递归自嵌SHA。

同reviewer复核后仍需唯一整合员提交实际字节并独立实际复审；WP28候选字节未变，仍须U03真正整合独立接受后以精确actual commit/blob交U04，U05消费冻结结果。U08不启动，M02-003不重开。

本次 changed paths：

- `review/remediation-third-20261012-prepare/U03/candidate/deliverables/final-specification-set/pokemon-rules/wp21-dynamic-forms-and-display.md`
- `review/remediation-third-20261012-prepare/U03/candidate/deliverables/final-specification-set/test-catalog/pokemon-rules-wp19-21-22-23-34.md`
- `review/remediation-third-20261012-prepare/U03/author-report.md`
- `review/remediation-third-20261012-prepare/U03/author-self-check.json`
- `review/remediation-third-20261012-prepare/U03/candidate-identities.json`
- `review/remediation-third-20261012-prepare/U03/candidate.patch`
- `review/remediation-third-20261012-prepare/U03/traceability-proposal.json`

manifest SHA256 `7a62ad282d6990100219068c3a17ea1121dc4ca6169b153a6980e2dd0f91fc03`；完整patch SHA256 `dd1de8ee2cf12cf5c81344bae889cfbe58dcc367ebc820331fd38f9c23b2bf97`。
