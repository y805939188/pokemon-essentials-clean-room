# 5.3 整数进化参数候选 r1：独立规格复审

**结论：PASS。** 固定候选的 30 项绑定、版本差异、边界期望与所核静态来源相符；没有发现 P1–P3 级规格错误。此结论只放行净化证据供协调者审定，不等于正式规格已更新、原版实际运行通过或框架实现通过。

## 对象与证据边界

- 固定对象：同级 `candidate-r1/` 的 `BOUNDARY-VECTORS.csv`、`HANDOFF.zh.md`、`METHOD-BINDINGS.csv`、`README.zh.md`、`SOURCES.json`。`SHA256SUMS` 自身 SHA-256 为 `88157e401cb0d1e72db9a7685eff54d6b3d1cb540d9b6fa04a1e60392c159e40`；其列出的五个文件逐项校验均为 OK。未改候选或正式规格。
- 范围清单只取 `.handoff/step5-3-06ac-B-plan-r2-20261025T172436Z/INTEGER-PARAM-GAP.r2.zh.md` 与 `METHOD-REGISTRY.r2.csv` 中逻辑 `integer` 的 30 项。正式缺口对照 `wp31-basic-evolution.md` §3、`wp03-content-identity-and-schema.md` §5.1、`wp04-pbs-lifecycle.md` §4.2/§4.5。输入文件及三份正式规格的 SHA-256 与 `SOURCES.json` 相符。
- 发行根 `/Users/dingshinn/Desktop/pokemon-essentials` 为 `v21.1`/HEAD `ea7b5d56d2436591160983c4e641a2ceee2d875a`；参考 R 根 `pokemon-framework-reference/reference/pokemon-essentials` HEAD 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。两工作树 clean。各自四个定点 Ruby 文件的 SHA-256、Git blob 与 `SOURCES.json` 相符；30 项登记行范围也逐项核对。维护者的 [v21.1 发布页](https://github.com/Maruno17/pokemon-essentials/releases/tag/v21.1)确认标签指向 `ea7b5d5`，但不提供此参数域的详细规则。
- 仅静态读两版的进化登记、Species PBS schema、通用行/CSV/值转换、物种及形态参数校验路径，并核所需参数用途。没有读取框架 TS 或 `.handoff` 输入快照中的 TS；没有运行 Ruby、原版、GUI、NW.js、框架或其测试。以下全部为 **NOT_EXECUTED** 静态期望。

## 复核结果

| 项目 | 结论与定位 |
| --- | --- |
| 30 项绑定 | **PASS。** 名单完整唯一；两版进化登记均将这 30 项声明为 Integer，物种及形态终检据此统一使用 PBS `u`，无 `i`/`v` 例外。登记逐项行号在 `METHOD-BINDINGS.csv`；转换位置为两版 `Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb` 的物种终检约 332–350 行、形态终检约 479–500 行。 |
| 词法与分词 | **PASS。** `-1`、`+1`、`1.0`、`1e2`、`1x` 于终检整数转换拒绝；`0`→0、`1`→1、`01`→1。末尾空位和完全缺第三位都形成缺值；复数列表内侧空文本仍是文本，到整数终检拒绝。行预处理、CSV、记录求值与 `u` 转换见两版 `Data/Scripts/021_Compiler/001_Compiler.rb` 约 72–76、95–143、255–292、384–406、690–736 行。[Ruby 3.1 分词文档](https://docs.ruby-lang.org/en/3.1/String.html#method-i-split)确认默认抑制尾空字段；[正则文档](https://docs.ruby-lang.org/en/3.1/Regexp.html)确认 `\d` 为 ASCII 十进制数字。 |
| 版本/入口与缺参 | **PASS。** v21.1 的 schema 只消费复数 `Evolutions`；语法正常的单数 `Evolution` 不产生条目。v21.1 基础物种的有参方法缺值到全表终检才失败；显式形态条目缺值被形态终检跳过，可在其余前提正常时进入保存。R 同时消费单、复数，且两者在条目校验时对有参方法缺值拒绝，早于当前条目登记。schema 见两版 `Data/Scripts/010_Data/002_PBS data/008_Species.rb` 103–109 行；校验/登记/保存见两版 `Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb` 4–72、294–354、380–440、448–525 行。 |
| 附加域与用途 | **PASS。** 24 项等级阈值、Beauty、BattleDealCriticalHit、Location、Region、Event、EventAfterDamageTaken 的登记用途与候选一致；所核编译链没有额外要求正等级/次数、地图或区域存在、美丽值上限。编译接受和实际命中分层正确；尤其要害计数需有成员记录，EventAfterDamageTaken 的参数是事件编号而非伤害阈值。用途定位见两版 `Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb` 候选 CSV 各行的登记行号。 |
| 大整数 | **PASS。** `u` 路径没有 JS 安全整数门；十进制转换可保留大于 `2^53-1` 的参考整数，候选以十进制文本交付结果是恰当的。[Ruby 整数文档](https://docs.ruby-lang.org/en/3.1/syntax/literals_rdoc.html#label-Integer+Literals)、[十进制文本转换文档](https://docs.ruby-lang.org/en/3.1/String.html#method-i-to_i)与 [ECMAScript 安全整数定义](https://tc39.es/ecma262/multipage/numbers-and-dates.html#sec-number.max_safe_integer)支持将参考接受域与 JS Number 表示域分开。无资源耗尽保证。 |
| CSV 交付 | **PASS。** `METHOD-BINDINGS.csv` 30 行与固定名单逐项一致。`BOUNDARY-VECTORS.csv` 2880 行，恰为 30 方法 × 6 版本/入口 × 16 边界，组合唯一且齐全；各版本、行形态、中间值、接受/失败阶段字段相符。30+2880 行的证明状态均为 `NOT_EXECUTED`，无原版运行用例冒称。 |

## 非阻塞编辑建议

**P4，仅措辞。** `README.zh.md` §2 的“未访问……其它原版算法”可改成“仅对所列四个文件的相关路径取证，未调查或交付范围外算法”。这样与定点版本差异查看时可能出现的相邻字段上下文更精确；不影响任何行为判断，也无需改动本次封存候选。

## 模型与限制

用户要求独立 `sol ultra`、Standard/nonFast 复审。执行环境没有回显有效模型、推理档位或服务档位，三项均记 **UNVERIFIED**，不宣称已设置。本复审没有执行原版行为或真实编译；“显式形态缺参可编译”受候选写明的合法目标、其它字段及外部依赖正常等前提约束。后续是否纳入正式 clean-room，由协调者在保持 v21.1 与 R 版本分层后决定。
