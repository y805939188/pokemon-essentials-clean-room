# WP65 交付摘要（首版，2026-10-01）

提取方。依据 `review/gr013-gr016-review-2026-10-01/recheck-v2/`（GR-001～016 全部 CLOSED 的通过报告、WP65 执行提示、next-task-inputs.json）。**本批只做 WP65**：标题/载入/选项/暂停/PC 主导航（F16-01）与野外快捷菜单（F16-02）。未做 WP67-A/B、集中回填、B 批整合或整体 double review。

## 产出

| 文件 | 完整 SHA-256 | 字节 | 状态 |
| --- | --- | ---: | --- |
| `specs/ui/wp65-title-load-options-pause-and-pc.md` | `d4f208b972bb56611928de696d80e39d457ecde58cb0ae0620f518eeb147cabd` | 47,141 | **ReviewPending（A～F 具名静态范围，待统一 review）** |

主稿单文件承载 A～F 范围（目录长度可控，未拆附表）。场景标识 T01–T36，文件内唯一；对既有规则仅按章节引用。

## 来源覆盖（全部磁盘程序化实测身份，见 checks.json）

- **七份主 UI 全文**：SplashesAndTitleScreen（129 行）、UI_Load（356）、UI_Save（139）、UI_Options（544）、UI_PauseMenu（321）、UI_PC（237）、UI_ReadyMenu（331）——与 next-task-inputs 身份逐项一致。
- **调用者/机制**：999_Main（60 行）、StartGame:21–34、Scene_Map:95–111, 205–220、Event_HandlerCollections:80–123（MenuHandlers 排序/条件/动态名）。
- **跨文件注册**：SafariZone:180、BugContest:426、PurifyChamber:1299、HallOfFame:452——**29 项注册（pause_menu 12／pc_menu 5／options_menu 12）逐条核对并建立覆盖映射**，与交接检索集合一致，无漏项；注册数 ≠ 任一时刻可见数（条件逐项判定）。
- **配置/字段**：Settings（LANGUAGES 默认空、SKIP_CONTINUE_SCREEN=false、SPEECH_WINDOWSKINS 21 项、MENU_WINDOWSKINS 28 项、SCREEN_SCALE=1.0、SAFARI_STEPS=600）、BattleSettings:96（NEW_CAPTURE_CAN_REPLACE_PARTY_MEMBER = MECHANICS_GENERATION ≥ 7）、Game_Temp 临时字段、PokemonBag 游标字段（默认 [0,0,1]）与迁移点、Player 可见条件字段（seen_storage_creator 默认 false）。
- **四份计划内完成依赖**（WP09/WP10/WP17/WP24）与 14 份边界规格身份均与交接快照一致；引用其具名通过范围，未重开已闭合问题。

## 自检结果（详见 checks.json）

- **8 类场景定点核对**（提示 §4 各类要求）全部与来源一致：启动分流（T01–T06）、删除流程（T07–T09）、无效存档备份分层（T09–T10）、保存拒绝/覆盖警告/成功失败（T11–T14）、紧急保存（T15）、选项即时应用/端点/可见集合/载入画面差别（T16–T23）、暂停项条件与会话退出交界（T24–T26）、PC 入口门与信箱（T27–T29）、快捷菜单候选/游标/确认/执行返回（T30–T34）、面板缺失值与游标持久边界（T35–T36）。
- **一致性/交界检查**：三层状态变化（界面即时／游戏状态／持久写入）全文一致；"离开选项画面不落盘"与"载入语言路径直写存档"分开；子屏幕取消与退出整个流程分开；候选资格与执行成功分开；WP08 已正确 UI 行为、WP09/WP10 存档规则、WP24 语言区分仅引用未改。
- **案例编号唯一性**：T01–T36 无重复，交叉引用可解析。
- **未证项具名保留**：地图事件调用者（U01/E31）、资源存在与播放（U01/E11）、宿主窗口行为、异常清理、可见条件字段正常写入者、ready_menu_selection 完整写入者目录。

## 边界与依赖绑定

- **WP08（语言/本地化）**：界面语言索引与直写存档边界——引用其已登记规则；本包不泛化为训练家/Owner 语言编号来源（WP24 已区分）。
- **WP09（存档/启动/继续）**：保存流程、载入、备份——调用点与分流；不另写第二套规则。
- **WP10（迁移/恢复）**：紧急保存 UI 交界、旧格式游标迁移——只登记交界。
- **WP17（消息/窗口/输入）**：文本输入方式与消息层——引用。
- **WP24（玩家字段）**：visible 条件字段（跑鞋/图鉴/Pokégear/储存创建者/净化室）——引用，写入者多为事件（材料缺口）。
- **WP27/WP28/WP59/WP63/WP64/WP66-A/B/C/WP23/WP25/WP53/WP62/WP15**：登记列表、道具执行、隐藏招式许可、地图/Pokégear、邮件与神秘礼物、队伍/储存/商店界面、净化、容量、会话结算、图鉴、音频状态——各领域规则仅按具名通过范围引用。

## 登记与停止

- manifest 第九十轮、主 TSV v65、Feature Matrix F16-01／F16-02 本轮具名状态（ReviewPending）；阶段最终检查独立保存（registration-final-checks.json，不登记进其描述的清单）。
- **停止送统一 review**：主稿 ReviewPending，不自行标 Reviewed、不宣称通过；不继续做 WP67-A/B、集中回填、B 批整合或整体 double review。reference 固定 commit、Git 清洁；未创建任务／Agent、未发跨会话消息、未提交／推送。
