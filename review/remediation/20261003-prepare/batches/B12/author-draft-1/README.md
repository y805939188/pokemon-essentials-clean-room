# B12 作者候选发布说明

本轮完成 9 项贡献、6 项主责的 11 份获准正式文件修订，附上 15 条新增静态设计、原／最终集合比较及独立复审请求。父任务已批准上一草案发布的精确五路径补丁，原规格已同步，状态为 **COMPLETE_AUTHOR_CANDIDATE / PENDING_INDEPENDENT_REVIEW**。范围批准不是质量 PASS；尚无候选 PASS、整合 G、实际版本 PASS、正式接受 C 或 canonical 关闭。

正式输入是 B15-C `1d06c45cc0a744fca181ac80ee573cc9ebb9b862`，tree `5c99f51ec4cc084bc1c2b081306f1b55370744df`。管理包 `9ad5539f38544fef6037356018015fe418021514` 只用 `git show` 消费。作者分支为 `codex/cloud-dot-B12-author-1-20261009`，从正式输入建立，没有把管理后继作为修订基线。完整发布 SHA 由最终交付外部提供，避免包内自哈希循环。

## 逐项成果与静态设计

| 贡献 | 主责 | 本轮有界改动 | 新静态设计 |
| --- | --- | --- | --- |
| GIR-FD82-003 | 否，B21 | WP52 指定源定位移审计，保留族、身份、复制缺源默认与最终有效行为 | CE/C59 |
| GIR-FD82-A046 | 否，B07 | WP51 AI 估量回指已接受 WP28 §5.1 实际回复量，保留 WP50 持有触发分工 | AI/I08 |
| GIR-FD82-B017 | 否，B10 | WP52 痛楚平分评分回指已接受 WP46 §6.4，区分未夹限比例与真实整数平均/写入/物品检查 | BE/B63 |
| GIR-FD82-B020 | 是 | 完整道具列表先资格，具名参数、缺索引/上下文边界、整阶段失败、无消费与继续阶段 | AI/I06、I07 |
| GIR-FD82-B021 | 是 | 每个残余分量的取整/最低量/资格/符号/倍率顺序、Wish/Perish 例外及下游局部消费 | AI/S08、S09；AE/G13 |
| GIR-FD82-B022 | 是 | Assurance 目标身份、OHKOIce 独立失败、Helping Hand/Imprison 阶段；完整 A/B/C 出现及复制源回核 | BE/B02b、B61；CE/C56、C57 |
| GIR-FD82-B023 | 是 | 默认 Geomancy User/目标数 0 的可达性，保留目标处理器条件合同 | BE/B62 |
| GIR-FD82-B024 | 是 | 正文/附表明确机制世代比较，保留基础 6、18 类型映射及 B024/D011 两个最低要求 | CE/C58 |
| GIR-FD82-B026 | 是 | 单敌/允许覆盖公开门，伙伴优先于一员假门；普通双打与大会预算/保留/通知边界 | SF/SF35 |

完整原控制、批准验收对象身份和当前 qualified 字段见 [qualified-control-bindings.json](qualified-control-bindings.json)，局部最小反例、反向对照及保留项见 [contribution-matrix.json](../candidate-1/contribution-matrix.json)。这些局部说明不替代绑定的 whole control。

完整集合回核还定位到 B 附表多列 Morpeko 整体评分直接项、青草治疗目标失败直接项，已移除假直接项并保留真实 copy；A 能力评级实际 20 add＋5 copy，标题由 23 改为 25，不改变 A 总量。

## 作者核验与证据边界

- [reading-log.json](reading-log.json)：57 个计划输入身份全部核对（55 当前、2 immutable）。语义读取为本贡献必要条款与上下文，不宣称整文件、全部原 233 对象或历史每次出现已重读。另读原 A 附表用于完整集合比较。
- [source-reading-log.json](source-reading-log.json)：固定参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` 的有界只读源定位；已有精确版本证据复用。源码未复制入正式输出。
- [registration-collection-comparison.json](registration-collection-comparison.json)：A334/B270/C167 的族＋身份＋复制源出现多重集合全部相等，missing/extra 均空；不只比较总数。比较范围不冒充全源行为覆盖。
- [catalog-preservation.json](catalog-preservation.json)：两个目录原 230/157 行的 ID、顺序、重复和完整行文本全部保持；新结果 244/158 行，新增 14＋1 条静态设计。所有其他 owner 行、B15 C122/C109 保持。
- [sanitization-audit-map.json](sanitization-audit-map.json)：迁出的源定位及原输入行绑定；必要最终行为与原审计证据仍保留。
- [metadata-checks.json](metadata-checks.json)：保留上一草案的作者核验记录，绑定其原稿未应用阶段，不能作为当前原稿应用结果。[当前候选核验](../candidate-1/metadata-checks.json) 另记录五路径授权、before/patch/after、原／净同步、全范围与完整 diff。两者均为作者元数据核验，不是独立 PASS。

所有新设计只作静态推导，执行向量、参考/游戏/Ruby/编译/转换/生成/反序列化、runtime 观察和已证 Demo 链均为 0。U01–U10、G01–G12、AX01–AX20、具名未读、条件树果 67、插件/宿主/配置/媒体与非局部义务按 [source-limits.json](../candidate-1/source-limits.json) 原样保留。参数 requested 为 gpt-6.1-sol/xhigh/Standard，缺可信回显的 admission/effective 分项见 [configuration.json](../candidate-1/configuration.json)，不伪称实参核实。

## 精确原规格扩围与应用

[scope-amendment-1.json](scope-amendment-1.json) 记录父任务授权：精确批准草案 `b452594ca55a9b9e39d073794684c13ec9fa18d9` 的 proposal blob `7d379d3725b35c90532c72eae87887d1a1bc2c57` 和五份完整 patch。每个 before blob/SHA256/bytes、patch blob/SHA256 及 approved-after SHA256 全部核对后应用，没有扩其它原稿。提案 4 原标签 §3 已改成实际 §4，以精确 before/after/patch 内容为授权范围，补丁身份不变。

[original-scope-proposal.json](original-scope-proposal.json) 保留逐 ID/path/clause 的 before、完整 patch 和 after，并记录授权绑定与应用状态。[original-output-identities.json](../candidate-1/original-output-identities.json) 给出实际五原稿输出 blob/SHA256/bytes，全部等于父批准的 proposed-after。11 份正式文件输出字节仍与上一草案相同。

| 精确批准并应用的路径 | 问题与条款 | 补丁 |
| --- | --- | --- |
| specs/combat/wp51-ai-action-selection-and-skill.md | B020 §4；B021 §3.3 | [1](original-proposal-1.patch) |
| specs/combat/wp52-b-field-damage-healing-and-target-evaluation.md | B023 §3 | [2](original-proposal-2.patch) |
| specs/combat/wp52-c-items-calling-and-control-evaluation.md | B024 §2.1 | [3](original-proposal-3.patch) |
| specs/combat/wp52-c-item-control-coverage-and-data.md | B024 §4 | [4](original-proposal-4.patch) |
| specs/pokemon-rules/wp53-safari-and-bug-catching-contest.md | B026 §6.1 | [5](original-proposal-5.patch) |

原规格同步门已满足。此次授权仅本 B12 五路径定点补丁，未沿用 B11/B15 原稿许可，也不改变任何其它 owner 的接受成果。没有执行行为测试。

## 下游与独立复审交接

[cross-input-report.json](cross-input-report.json) 精确列出 B12 写／B16 读的 5 路径和 B16 将写／B12 读的 WP65、WP66-A 两路径。父任务确认 B16 私有准备已完成、不会并发写正式文件。B12 独立候选、必要 affected、G、实际版本检查和 C 齐备后，父任务重新冻结 B16 的这些正式输入及原稿/caller 扩围；不能沿用变化前的读取身份。

[affected-interface-proposals.json](../candidate-1/affected-interface-proposals.json) 只是版本精确的 potential 导航，作者未代签 PASS/NOT_AFFECTED。[public-registration-proposals.json](../candidate-1/public-registration-proposals.json) 逐 ID 交 sole A-REG，作者未改公共账本、root/index、traceability 或接受统计。

[independent-review-dispatch.md](../candidate-1/independent-review-dispatch.md) 是 FULL 与必要 affected 的派发入口，[independent-review-request.json](../candidate-1/independent-review-request.json) 绑定完整需求，请父任务按最终交付的完整候选 SHA/tree 派发 ultra FULL（9 项贡献/6 项最低验收）及真正受影响的 candidate/actual 门。作者未创建任何子任务或独立复审，没有代签自己。

完整未过滤 diff 取外部交付的完整发布 SHA，命令为 `git diff --binary --no-ext-diff --no-textconv 1d06c45cc0a744fca181ac80ee573cc9ebb9b862 <PUBLICATION_SHA>`；包括所有正式和证据/提案文件，不按目录过滤。后续实际 G 必须分别提供当时已接受前驱→actual、candidate→actual 的两份完整 diff。远端 readback 的 ref/FETCH_HEAD/tree/逐变更文件字节核验和该完整 diff 身份由最终交付外部记录，避免证据自包含循环。
