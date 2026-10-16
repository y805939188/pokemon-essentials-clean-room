本域 16 个主读文件已逐文件、逐结构、逐字段完整审读，有限适用条款的双向映射已交付。状态为 `LOCAL_PRIMARY_REVIEW_COMPLETE_PENDING_MAIN`：主审尚未接收 6,712 个结构及 9 项原接口、3 项入站字段接合，故不作全局 PASS、最终分类或 `NO_REQUIRED_UPDATE` 声明。`UPDATE_NOT_STARTED`，未整改正式规格或参考实现。

固定依据为委派提交 `30cfed0996003b6ebf4b5c51cc04f31ca9255440`、B8 `fd1df570cad987dc3852a3b958f03916e317f7fe`、R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。B8 根树为 `751dfde81048c81390f89a65ca1d1a565ba8e1ca`，formal 树为 `f292698cdd4a8e725525a9be6dc34b75faaf151e`；R 树为 `7589c800b61ba13a13040ed0d686979b80a84fd0`。实际云端根为 `/workspace/pokemon-essentials-clean-room` 与 `/workspace/pokemon-essentials`。R 实际克隆 origin 是 y805939188 fork，声明上游为 Maruno17；固定上游 master 身份核验见 identities/preflight。历史本机路径不充当云端路径。

实际审者为本次 `/root` 上下文，没有启动子代理。源线程标识为 `01a13f49-a154-7054-9b04-ce31f924d01c`；平台实际 session、model、effort、tier、Fast 回显均为 `UNVERIFIED`，请求配置不冒充实际回显。首先完整读取固定委派 prompt、readset，再完整读取其引用的全局 prompt、skill 与 AGENTS；逐项原文副本及固定身份保存在 `inputs/`、`identities.json`，读取次序见 `reading-ledger.json`。

| 代际 | 基础种族 | 形态 | metrics | 遭遇 | 结构合计 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Gen 5 | 649 | 86 | 674 | 19 | 1,428 |
| Gen 6 | 721 | 188 | 674 | 19 | 1,602 |
| Gen 7 | 809 | 250 | 674 | 19 | 1,752 |
| Gen 8 | 898 | 339 | 674 | 19 | 1,930 |
| 合计 | 3,077 | 863 | 2,696 | 76 | 6,712 |

主读分母为 16 个文件、4,692,651 字节、102,507 行、6,712 个结构、89,067 条属性／类型／槽行；全部 `FULL_READ`，主读未读文件、未读结构、未映射显式字段均为 0。重复列表、顺序、全部 Pokedex 文本及字面差异均纳入实读。metrics 的逐记录无损表述及其覆盖证明已登记。哈希、parser、同 blob、机械检查和旧轮结论均不增加实际阅读信用。Gen 5 五段早期显示的原工具 chunk ID 无可验证回显，登记 `UNVERIFIED_CHUNK_ID`，不补造编号。

必要依赖共 64 个文件：R 为 40 个全文、4 个精确范围读取；B8 formal／测试目录为 14 个全文、6 个精确范围读取。没有整文件完全未读的已发现依赖。10 个外域文件仍有本人未读余段，共 4,147 行；`gaps.json` 按文件与闭区间列出，未标为全文读取，也未将可得材料包装为 limit。原 40 条依赖路由均已有本域必要读取范围和精确接合。这些外域余段按主审有限接口合同保留其 primary 归属，不扩大为本域全文件义务。

`field-contracts.json` 记录 45 个字段／结构条目及各自语法、缺省、形态继承、含义和消费者，共 180 个字段原子断言；另有 32 个跨链原子断言及 4 项头部结构合同。`forward-mapping.json` 逐一覆盖 6,712 个结构、89,067 个显式绑定及 75,313 项缺省／继承处置，保留行号、值哈希、槽数与基础种族锚点；`reverse-mapping.json` 给出全部 212 个原子断言的源／规格范围及前提。坐标脚本只整理已经实读的材料，不复制参考源码为规格或交接，不宣称替代语义审读。全部断言的最终接收为 `PENDING_MAIN_REVIEWER`。

审读中保留的关键语义如下，各项完整源定位、适用条款、普通对照和边界在映射及 `semantic-notes.json`：

- 备份路径的发现、激活和后缀选择具有前提；不能把四代备份同时视为运行时生效数据。Species 形态 schema 与编译器继承各有职责：Name、GenderRatio、GrowthRate、Incense 虽不在形态作者 schema，仍可由编译器继承；FormName 不继承，PokedexForm 缺省为本形态。空集合、复制的嵌套数组以及仅当三项均缺失才继承的野生持物池分别处理。
- `get_species_form` 可回退基础记录；metrics 缺失形态记录时复制基础／默认值，与显式存在但部分字段缺省的记录不同。编辑器坐标含倍率和敌我／正背面条件；保存先写二进制再写 PBS，存在部分提交边界。导出后缀与省略相同形态内容的条件分别登记，未声称现存战斗布局自动广播刷新。
- Pokemon 动态形态读取可能触发提交；显式 setter 的能力缓存、handler、属性重算和图鉴条件，以及 forced、storage、battle 等前提均纳入。能力、性别、成长、学习顺序、重复招式保留、亲密度、进化、血缘和持物消费者分别映射。原始持物赋值与可携带判断分开；PBS 初始亲密度与后续夹取边界分开。
- 遭遇版本直取、版本迭代器和地图快照分别审读，未合并其行为。图鉴别名、登记名与最近见到名、区域／可见性筛选、BACK 后保留状态，以及孵化、交换、资源匹配和 Mega 的激活前提均有接合。
- 存档对象保存、Marshal 失败及 `shows_shadow?` 的源事实分别列为 G31、G32、G11 的 `SOURCE_PREMISE_ONLY`，其 foreign formal 接收待主审；没有用 PBS 二进制生命周期条款代替存档规范，也没有把注释掉的逻辑视为运行逻辑。
- Gen 6／7 Mega Alakazam、Gen 6 Slowbro 形态编号等差异保留其代际和激活前提。Gen 8 Sobble EV、Meltan 等级和 Zamazenta 数值等字面内容按固定 R 审读，不凭外部游戏常识改写或直接定为规格缺陷。Evolution registry 中 LevelAfternoon、DayHoldItem、NightHoldItem 已实际复核存在，早期缺失猜测不作为发现。

主审新增合同固定为 `ea3359282fe4e27132fa3ceaa2d8f308b0831510` 的 `delegation/external-cross-domain-reception.current.json`。已完整读取与本域有关的 13 个精确接口对象和 8 个 PBS 归属对象；原整份合同的首次展示被截断，未授予整份全文阅读信用。精确投影、原始对象身份、选择条件及实际读取范围保存在 `central-contract-projection.json`。合同的 35 个 PBS 归属为 battle 20／world 1／current 6／backups 8；本任务原定主读分母仍为 16，ELR 本地化子分母为 8。

待主审累计接收的是 IF01–IF09，以及 ELR-I03（原始本地化字段）、CD-I01（血缘／Incense／Egg 字段）、CD-I06（parser／导出／激活）。9 项原接口覆盖发现／schema／注册／保存／缓存，基础与形态、Pokemon 与动态形态，metrics／cry／孵化／交换，编辑／取消／保存／重载，遭遇快照／生成，图鉴迭代／直取／可见性，别名／登记／存档，成长／学习／进化／血缘，以及野生持物生成／赋值／查询／持久化。本人接收信用为 0；不会以接口提供者报告或身份校验代替主审接收。

唯一提案 `GR8-XPCB-001` 的本地处置为 `WITHDRAWN_AS_NEW_REQUIRED_PROPOSAL_ALREADY_DOCUMENTED`。四代相同遭遇材料中地图 5 的 v0 PokeRadar 槽有 STARLY，v1 无该槽：直取 `(5,1)` 与 `each_of_version(1)` 结果不同；WP36 §3.1 和 WP62 §5.3 已明确保留这种差异，因此撤回作为新 required 提案。`proposals.json` 保留固定身份、最小输入、普通对照、失败／取消／部分提交边界、负证据范围、影响、验收与回归。真正不同的主审上下文独立反证和最终接收仍未完成，未由同一上下文更名冒充。各最终分类计数为 0 表示尚未裁决，不表示已证明零问题。

所有 R 编译、writer、游戏、存档、宿主／UI 和行为向量均为 `NOT_EXECUTED`，执行计数 0。`validation.json` 只记录报告身份、坐标、范围、分母、引用和写集一致性检查；179,580 项检查通过不产生语义、行为或接收信用。可得但截断或失败的显示及修复情况保留于 `execution.json`／读取台账；WP67A 的截断尝试未取得全文信用。

没有材料、权限或环境实质阻塞。本域交付完整，剩余为主审累计接收、独立反证及全局裁决；个人外域未读余段与主读未接收数均如实保留。本报告仅写本任务目录，使用用户授权的专用分支普通 commit／push，不修改 main、tag、formal、R、公共台账或他人目录。先前 `962204c` 为历史不完整检查点，本次交付取代其本域状态。最终 commit、根树、报告树和独立远端全量回读结果以交付消息及 `/tmp/r8-xpcb-final-complete-readback.json` 为准，避免在文件中伪造尚未产生的自身 commit。
