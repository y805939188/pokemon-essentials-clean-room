# R6-UI 独立全量双向 review

本域指定文本与源的全量审读已完成，可审未读为 **0**；这不是正式批准或运行 PASS。12 项提案均已附非提出者的新阅读反证，最终分类交本轮外部 global root。没有启动 update。

固定输入：main `8ea169fbd0f33f378b5d732fd6bea59e854e04a6` / workspace tree `6ab3429170d2762607fbc2237014c3a160449fa1`；formal tree `1046fbb657882e84b3dfc6d017943a9edf7782e5`（全局131件中本域9份主文/附表）；R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。首读 AGENTS.md 全文，未读取旧 PASS/blob 充当语义证据。末尾只读核验身份仍一致、正式保护路径无 tracked diff、参考工作树干净。

## 覆盖与分母

| 对象 | 新读/实审范围 | 未读 |
| --- | --- | ---: |
| `Data/Scripts/016_UI` | 全32源文件、16853编号行；场景/模型/工具/入口、输入/取消/失败/结果消费者 | 0 |
| WP63、WP65及Controls/Card附表、WP66-A/B/C、WP67-A/B | 全9份、1925行；公共分母1262非空block逐clause记账 | 0 |
| UI test-catalog | 整篇914行、793公共block；保留各行完整前提、取消/异常和未执行限定 | 0 |
| 源结构 | 993个class/module/instance/singleton声明节点全部关联人工审读事实；注册/常量另在事实组 | 0未绑定 |

连续大文件按真实区间输出，截断区间重读；记录在 `reading-ledger.jsonl`、各分域台账与合并 `reading-ledger-combined.jsonl`。原始 `delivery-ledger.jsonl` / `read-logs/` 只证明交付；`structural-inventory.json` 只证明解析。没有把这些阶段自动判为语义通过。早期进度口头写16852，最终按固定blob与公共inventory逐文件核对为16853，未发生源修改。

`forward-matrix.jsonl` 汇总916条人工事实/单元记录，逐unit→fact→必要consumer→spec；`reverse-matrix.jsonl` 共2345条（含重叠的专项测试贡献与整篇目录记录），精确公共clause ID/行→来源与前提。计数与绑定工具只编译记录，不生成语义 PASS；结构、范围/依赖、静态支持、未知呈现及待反证缺口均分开。子域分母不可相加当作另一套Ruby方法总数：Party用连续功能分区，Storage/Bag有方法和事实两层；993为统一结构库存。

WP17由O主审，本域新读必要message/窗口/文本消费者；minigames目录全文已读，源全审仍归O。战斗scene与完整规则C主审，本域独立新读菜单、消息、背包恢复、目标、成员/捕获/学招提交、资源请求与必要caller接合；没有据局部UI前缀认证完整战斗规则、AI或全部招式。此责任划分不是缺读本域32源或9主文；域外批准仍由原owner和global root汇总。

## 12项独立提案与非提出者结果

| ID | 精确主文接点 | 非提出者结论；最终均pending |
| --- | --- | --- |
| R6-UI-001 | WP67-A228 | Storage支持：旧成员送盒成功→从party删除→送盒暂停→消息返回后记忆左移→新成员入队。正文将暂停放在删除前。相关226入队消息后才回填初始道具的观察单列，交root决定合并/单列。 |
| R6-UI-002 | WP67-A304 | Bag支持：Safari球容量拒绝需party与全部盒双满；party有位/盒全满仍扣球并发投球请求。WP53既有双满条款保持，不重写其结算。 |
| GR6-UI-BAG-001 | WP66-C120；WP29:88 | UI/root支持限定：省略问候才两条默认欢迎；自定义问候只一条替换，正常两条告别不变。 |
| GR6-UI-BAG-002 | WP66-C64/90；C12 | UI/root支持**覆盖缺口**：Bag成功提示入口数量仍5，提示返回后丢3为2；PC先删再提示已2。C12终态仍正确，不把逗号描述硬判成反序断言。 |
| R6-UI-PARTY-001 | WP66-A182 | Storage支持默认[]缺槽ACTION的提交前失败边界；“非空清零”并非明确声明缺槽安全，只补边界，保USE/OK/BACK控制。 |
| R6-UI-PARTY-002 | WP66-A216 | Storage支持：仅未会且不在等级候选的最初记录前置。非首项重叠GROWL仍留TACKLE/GROWL；WP30精确条件保持。 |
| R6-UI-PARTY-003 | WP66-A145 | Storage只支持LOW绘制请求澄清：Shadow替经验文字，低于最大等级仍请求经验条；非零EXP须在makeShadow前建立，不认证像素。 |
| R6-UI-PARTY-004 | WP66-A132/236 | Storage支持：合法作者2人规则/SpeciesClause的非法组合确认，旧Entry命令0可落到Confirm空成员摘要，在item_id失败。合法、取消、无旧命令/旧非0控制必须保持。 |
| UI-ST-001 | WP66-B65 | UI/root支持：队伍末按钮6专门UP→5/DOWN→0，不能全按成员±2/越界6描述。 |
| UI-ST-002 | WP66-B264 | UI/root主动反证强冲突：本行“暂持跨页”上下文可限定单纯导航；源交换会重启预览并请求新暂持Y这一事实成立。建议root按可选澄清/降级处理，不能截掉上下文判无条件冻结。 |
| UI-ST-003 | WP66-B239 | UI/root支持形态选择首末回绕的覆盖补充；首端隐藏箭头不门UP，移动下一轮写末次，BACK不恢复。物种/页面夹限仍保持。 |
| UI-ST-005 | WP66-B65 | UI/root支持局部两阶段补充：方向repeat优先后独立按钮，RIGHT+USE可先移再选、JUMP胜BACK；切盒内部再次Input.update必须列前提。 |

各提案的精确source/spec、完整前提、普通对照、最小反例、取消/异常/已提交前缀、负证据搜索范围、必要消费者、影响、最小修订、保留scope、同步文件、验收及依赖在 `findings.json`（12项合并，保留原分域完整记录）。该文件逐项链接非提出者报告：`storage/counterreview-party.json`、`storage/counterreview-R6-UI-001.json`、`bag/counterreview-R6-UI-002.json`、`root/counterreview-bag.json`、`root/counterreview-storage.json`。没有替global root作最终required/optional/reject裁决。

K/O的旧袋key迁移、Owner验证两项由Bag以本轮新读必要消费者作非提出者核查，详见 `bag/counterreview.json`。旧袋值残留/旧版本context重复转换与正常链版本推进分开；Owner相同数值条件遮蔽与独立name writer拒绝分开。读取root已有裁决只登记其状态，不替代新源证据。这两项不是本域新增提案；源bug及畸形输入是否未来兼容保留用户独立政策，不变永久兼容义务。

净化模型的三个诊断种入unit另归Demo/DX。其伪对象辅助依赖`PseudoPokemon`在固定Data/Scripts全文检索未找到定义，正常调用只找到注释，插件/运行时来源保留；见 `additional-open-questions.json`。这不是把诊断辅助当正常UI按钮或已证可达路径，未据此增加正常用户缺陷或阻塞本域可读输入。

## 验证层次与不成立的疑点

静态：本轮全文及必要caller/data/config新阅读。推导：逐场景和具名前提状态/数学向量。工具：固定git对象/哈希、Ruby AST与记录JSON/覆盖绑定，只证明身份/记录完整性。

隔离实际参考：Bag Toss原协调器3向量（提示前后数量/受控异常），以及root捕获存放原方法+默认Peer的正常尾与受控消息异常。依赖替身、原source范围/哈希、stdout/stderr及退出记录分开持久化。root探针为存放阶段夹具，借Shadow旗标旁路命名；不证明真实捕获、窗口、素材或默认Demo全链。源方法顺序观察没有改参考。

净化首绘角度疑点**不成立**：首轮夹具遗漏继承Sprite.angle，V1/V2的NameError只属坏替身，不能记参考失败；补属性的V3条件化首绘完成，已撤疑。三次日志均保留在 `tool-evidence-status.json` 及对应stdout/stderr，不拿退出0自动替语义结论。

独立模型：Party仅三条算术检查，未执行完整行为模型。完整hostDemo、实际画面/物理键/Input采样、声音/听感、真实存档均未运行；相关结果UNKNOWN。播放/绘图请求、逻辑属性与实际宿主结果严格分开。取消没有统一回滚承诺；holding、旧对象/物品/命令、mutable共享、缓存、正常restore与异常未必到尾均按具体入口记录。

## 权限与程序性偏差

没有git切换/提交/push、安装下载、外部服务、安全配置、真实存档操作；没有归档/释放环境或启动update。正式/specs/planning/audit/旧报告/参考未改，末尾只读检查无保护路径tracked diff，R工作树干净。

**不能声称全程只写tasks**：Party首次汇总命令遗漏cwd，短暂在仓库根生成未跟踪`build_review.py`与`forward-matrix.jsonl`，后移动到其owned目录；当前两个根路径均不存在。这违反用户的严格瞬时写入范围，事实已保存在其report/status及主status；没有抹去这一偏差或把当前无残留冒充从未发生。

请求模型gpt-6.1-sol、effort ultra、tier/speed default、禁Fast；实际model/effort/tier/speed/UUID无有效回显全部UNVERIFIED。没有查额度/认证或反复追配置。所有结论停在上述证据级别，等待global root查看文件并统一裁决；本域不启动修订。
