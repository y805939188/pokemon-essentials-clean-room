# B05 作者候选交接

RUN_ID：`20261003-prepare`；作者：`A-B05`；阶段：`B05-A`。本候选修订批准白名单十个正式文件，交付十个主责、十六个贡献 finding 的条款、附表、静态目录与逐 ID 登记建议。原稿五路径的最小同步仍待父任务明确批准，尚未写入。独立 Ultra 尚未开始，实际 integration 尚未开始，所有规范 ID 继续 OPEN；本报告不构成批准或关闭。

## 冻结输入和分支

- 分支：`remediation/20261003-prepare/batch-B05`，独立工作区 `/workspace/batch-B05`。
- 唯一候选父 SHA：`0a12de641542f9a59909d2a950c1de8df17ca09d`；父 tree：`af09467c1a868685a761f5483e4bcf5fb36aaaea`。直接从该已通过 B01 的交接建立，没有使用旧 main。
- B01 被审整合：`93d0714ddfdb4900e946c0acd1cc80cf6431f0a0`；Ultra 报告：`8a1fdfb2b582df4cefb408b56eea144a2e53dcfe`。后继交接只新增报告／接受记录，正式正文、原稿、planning 和 audit 对被审整合无差异。B01 接受的是 WP03/KR13 性格身份、顺序和映射依赖；本候选自行交付 WP19 完整 25 性格表，未把 WP28 消费条款视为已完成。
- 原 review 基线：`e1e01bb18d824931e54f182dd61af5a9f908ba85`；完整对象报告：`93e10babe0b9c9ef8b3f5277754541b447beeeb4`，`review/global-independent-review/2026-10-03-fd82a639/`。
- 批准规划：`41fffb540c6483f5296ea0d33b789b75180d27ed`，`review/remediation-20261003-prepare/`。规划目录在交接中保持原字节，未改历史批准、review 或冻结记录。
- 固定参考：独立 Git `/workspace/reference-B05-pokemon-essentials`；来源 `https://github.com/Maruno17/pokemon-essentials.git`；SHA `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。在主项目 Git 外精确获取并验证 SHA/tree/clean，随后只读。

候选的精确 SHA、父 SHA、tree 与远端分支核验在提交后的交接消息／发布回执提供；本报告随候选提交冻结，避免在文件中声称可自引用其包含的提交 SHA。所有输入 blob 与 SHA-256 见 [input-freeze.json](input-freeze.json)。

## 修改与反向对照

下表中的编号均保留 `GIR-FD82-` 前缀，省写仅用于阅读。每项原对象、current_qualifications、有效二审／扩展裁决与批准 acceptance 均完整继承；完整对象和无遗漏阅读凭据见 [finding-inputs.json](finding-inputs.json)、[finding-reading-receipt.json](finding-reading-receipt.json)。完整的原稿状态 → 净化路径／条款 → 附表 → 静态目录 → A-REG 建议见 [finding-dispositions.json](finding-dispositions.json)。

| ID | 本候选结果与邻近反例 | 静态目录 |
| --- | --- | --- |
| A020（贡献） | WP19 完整 25 序号／性格身份／升降属性，20 修正、5 中性；具名 LONELY/BRAVE/ADAMANT 和覆盖、缓存、双重取整反向对照；B01 WP03 依赖与 B07 WP28 责任分别保留 | ST60–63；原 ST27/39/40/49/50 保留 |
| A021（主责） | WP18 全字段默认：`Unnamed`、`???`、继承形态图鉴号、解除形态／Mega 消息 0、后缀空字符串、空列表与空值明确区分；手工记录示例不承诺编译有效性 | CI-25 |
| A022（主责） | 基础初始化“两类随机”与创建复检分开；UNOWN 0–27、PUMPKABOO/GOURGEIST 3/2/1/0 的 5/15/45/35% 和创建开关／非零形态反例；同值显式提交、动态读取守卫与缓存副作用分开 | CI-26–28 |
| A023（主责） | 四槽限于具体入口；整表与克隆可保留五项／重复项，静默新增只删除首项一次，已有招移到末尾保留对象及 PP；reset、交互学习与整表边界区分 | HP-35–37；原 HP-13–20 保留 |
| A024（主责） | 重学候选来自等级表与开关控制的首招记录，记录先于等级表再去重；不直接加入整个物种蛋招；BULBASAUR/AMNESIA 与首招开关对照 | HP-40–41 |
| A025（主责） | 直接遗忘接受 `−n≤i<n`，负索引映射、越界无变化；调试取消守卫仍拒绝负值 | HP-38–39 |
| A026（贡献） | WP21 表 F 逐种列明 ROTOM/KYUREM/NECROZMA/CALYREX/ZACIAN/ZAMAZENTA 招式身份、PP、已有招去重、缺数据门和部分失败；直接白→黑 KYUREM 不虚构改写；B07 WP28 独立贡献仍待完成 | FM15/20 修明前提；FM36–39/41–43 |
| A027（主责） | ROTOM 同值裸提交可删唯一招并留下零招式，保留参考行为；外层交互拒绝同值与裸提交区别，THUNDERSHOCK 保底只在原条件下发生 | FM40；HP-39/44–45 |
| A028（主责） | 净化 Mega 表 `BANETTEITE` 修为有效 `BANETTITE`；全部 48 行身份／条件／基础能力顺序对照，具名 BANETTE 正例与错误石／无石反例；正确原稿保持 | ME26 |
| A029（主责） | 两个 Scent 门均为友好度 h=255 且 G=0；h254 正例、满友好拒绝／不扣道具、battle 重检回补对照，隐藏 Hyper 与有效 Hyper 区分；正确原稿保持 | SH47/48/51 |
| A030（主责） | 净化 Shadow 表修正 GROWLITHE 与 SNORUNT 招式；全部 131 身份／量／招式、25 降量表、18 效果绑定、4 道具与 SHADOW 类型字段对照；仅可选注册条件下适用，未启用备份集 | SH50；原 SH14–21 保留 |
| A031（主责） | W06 指定 HARDY/M4000/G2500/H4/h80/JOY×1 → G2410/H4/h80；LONELY → G2370/H3/h80；保持先前 H4 的友好阶段门、性格存储与计算覆盖区别 | SH06 修明前提；SH49/52 |
| A040（贡献） | WP19 保留普通 EV252/510 培养合同与设施构建例外；CATERPIE/FOCUSBAND/QUIRKY/HP,ATK/TACKLE,STRINGSHOT 的 255/255 及整除 63 具名对照；B07/B17 未完成责任保留 | ST67；原 ST56–59 保留 |
| A044（贡献） | 背包 TR 成功后追加首招记录，与队伍入口及普通学习区分；TM57/CHARGEBEAM、取消／失败／消耗／遗忘后重学反例；原 UI 部分正确，不扩大缺陷结论 | HP-42–43 |
| C124（贡献） | WP19 补 rawIV 消费者特征 6×5 含义表、HP→攻击→防御→速度→特攻→特防 环、PID%6 起点、严格较大与余数；IVmax/Nature/calcStats 不替代 rawIV；B16 UI 层仍待完成 | ST64–66 |
| C126（贡献） | 合法零招式对象与 UI 失败边界：展示页四空槽可用，直接遗忘／事件选招首先读首招而失败，尚未到取消输入；普通无招学习走空槽可成功；B16 UI 层仍待完成 | HP-39/44–45 |

本批十个主责为 A021–A025、A027–A031；全部贡献共十六个。全部 ID 保持开放；不替 B07 的 WP28/WP30、B16 的 WP66A 或 B17 的 WP76 交付正文／测试，不把 B01 依赖接受扩张为本批完成。

## 静态自检与精确差异

- [static-validation.json](static-validation.json)：94 项 `PASS_STATIC_TEXT_AND_FIXED_ARITHMETIC_ONLY`；包括固定输入、B01 后继字节对照、B02 实际规划写／读交集、许可范围、共享目录尾部、完整数据身份顺序、固定取整与 Shadow 阶段算术。复现脚本：[verify-static.py](verify-static.py)。
- [evidence-integrity.json](evidence-integrity.json) 另核对原完整 finding／批准 acceptance、全部叶值指针、阅读回执、冻结输入／输出哈希、原稿零写入与登记未应用；这是证据完整性检查，不是行为向量执行。
- 目录新增 38 行：CI-25–28、HP-35–45、ST60–67、FM36–43、ME26、SH47–52；现有 FM15/FM20/SH06 仅修明本批前提。本批目录计数 CI28、HP45、ST67、FM43、ME26、SH52。
- WP24–26 的 PT/PS/AQ 与 WP34 的 BR 区，包含文件结尾的原字节，保持不变。B05/B06、B05/B08 的整文件冲突仍须统筹串行整合、重冻结和按影响复审；B02 与 B05 规划写集合及双向读写交集为空，不增加互相前提。本容器外 B02 运行状态未独立核验。
- 十个正式文件相对父提交为 182 行新增、41 行删除；全文 diff 已检查条款、边界、反向对照与许可范围，正文和非补丁作者记录的 `git diff --check` 通过。两个原生 unified diff 证据保留必要的空行上下文标记，单独核对精确字节与补丁适用性。冻结 diff 见 [formal-diff.patch](formal-diff.patch)，文件哈希与完整候选路径清单见 [candidate-manifest.json](candidate-manifest.json)。作者证据均新增于本目录；公共索引、Feature Matrix、coverage、trace、公共哈希／批准及历史记录未写。
- 26 个固定参考文件的读取范围和 SHA-256 见 [source-reading-log.json](source-reading-log.json)。未运行参考游戏、Ruby、编译、转换、生成、反序列化、模拟器或求解器；未修改参考 ignore，未跟踪到主项目或推送参考上游。
- **运行观察 0；demo 链 0；行为静态向量未执行。** 文本身份比较与独立固定算术不充当运行测试。U01–U10、G01–G12、AX01–AX20、可选内容启用及宿主／媒体／插件／运行组合未知限制继续保留。

## 原稿待批范围与后继责任

完整可审建议见 [original-scope-request.md](original-scope-request.md) 和 [original-synchronization-proposed.patch](original-synchronization-proposed.patch)：五路径、233 行 diff，仅对 `specs/` 中 WP18 默认／创建随机、WP20 招式入口／记录／重学／索引与零招式、WP19 完整性格表、WP21 具名形态招式、WP23 W06 最小同步。补丁已通过只检查适用性，未应用；原稿路径保持父提交字节。批准依据仍待父任务答复。

本候选因此只能交付白名单内作者贡献；原稿层同步尚未完成，不能据此声称原／净化两层全部验收通过。净化稿失真的 Mega 石、h255 与 Shadow 两行，均以固定参考和正确原稿为依据修净化稿，未反向破坏原稿。

公共登记建议单独交 A-REG：[registrar-proposals.json](registrar-proposals.json)。须先完成候选独立 Ultra 与实际 integration 受影响范围 Ultra，再登记本批有效贡献；跨域 ID 仍须其他贡献完成和最终 Ultra。此次没有自行 integration、公共登记或 CLOSED。

模型请求：`gpt-6.1-sol / Max / Standard(default)`；实际 model、reasoning effort、service tier 未独立核验，按用户方案 A 保留 UNVERIFIED 披露。未请求其他降档／加速，未使用 xhigh fallback，未派生任务；详见 [model-request-receipt.json](model-request-receipt.json)。候选推送主项目本批分支并核远端后停止，等待独立 R-B05 Ultra。
