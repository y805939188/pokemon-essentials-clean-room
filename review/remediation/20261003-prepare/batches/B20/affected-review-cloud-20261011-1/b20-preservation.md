# B20 独立旧接受贡献与共享目录保留核验

固定审查 NEW `1abaefb1db5818ff9404392143c476979d34c21a` / tree `2e40f9ad0e8fa40377d39e5a19eaa74cc2e05e85`，基线 C `de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f` / tree `88a400af08253bea8d97ee2ef2fa6636f0900f92`。入口包 `9a46a131ba2f7ea82b6eed823aa892cb57b0fba7` 的 `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-1/affected.md`；派发 `669997ac28258f26d0bafc81b1d081abb407a3a1`。

本分工结论：`PASS_STATIC_IDENTITY_AND_CATALOG_PRESERVATION`，无旧记录、资格字节或目录保留阻塞。仅签静态身份与明确字节边界；实际消费者的语义影响由其它独立复审分工判断，不能由此签 B20 整包质量 PASS、actual 门或正式 C。作者保留数量声明未作为核验依据。自己的 `/tmp/b20-preservation-check.py` 只读取 Git、文本、JSON 元数据并求哈希；未运行参考游戏、Ruby、编译器、转换器、反序列化器、行为向量或旧执行脚本。全部静态案例仍 `NOT_EXECUTED`。

## 独立重建及精确来源

从固定原 PLAN 前 19 个 owner 的 `contribution_finding_ids` / `primary_finding_ids` 重建 `(owner, ID)`，得到 308 个贡献键、205 个主责、216 个触及 ID；不存在重复 `(owner, ID)`。与固定 C 的全部 308 条 `accepted_contribution_receipts` 对照，逐键、主责标志全部一致；与固定派发的逐 owner `accepted_receipts_at_C` 对照，每条 receipt 的全字段一致。C 统计保留历史接受次序（B14 在 B10 前，B15 在 B12 前），派发表按 B01–B19 分组；这是导航分组顺序不同，旧 C 文件本身没有被重排或修改。

固定独立来源如下；JSON 输出另外给出逐 owner 的接受路径/blob/SHA256、原 PLAN 顺序的贡献/主责 ID、所有 216 个触及 ID 的完整原对象与完整批准验收对象 SHA256，未嵌入旧证据正文。

| 来源 commit | 路径 | blob | SHA256 |
| --- | --- | --- | --- |
| `41fffb540c6483f5296ea0d33b789b75180d27ed` | `review/remediation-20261003-prepare/batches.json` | `9dd98a6b96d49294d214f7e9a53eac8738c1484c` | `3758c04581500a29c0fa8dd727d8d6026a4ed2934c42b1778b1ff18e6fdbb02f` |
| `93e10babe0b9c9ef8b3f5277754541b447beeeb4` | `review/global-independent-review/2026-10-03-fd82a639/findings.json` | `6f3d96fd99b5a026bb88e463b3ad6e46658e3c01` | `7c2f0b9159f7be21d8ae9d647399521017500fe4c40ffed042c004492c6a242d` |
| `41fffb540c6483f5296ea0d33b789b75180d27ed` | `review/remediation-20261003-prepare/finding-acceptance.json` | `e178e5706771f5f7465bcf3351b5c632a5d68bab` | `54e4c86be3db493a5463ce4bcdef81c7184f1a1d89e6b3bbea358f14cc347225` |
| C | `review/remediation/20261003-prepare/batches/B19/acceptance-stage-1/completion-statistics-successor.json` | `6b97a0b5772fa5794406459e6cb4b668e958c932` | `7ac25e4772a9e761c234000e93564422e4be3a9ae4d125ee0d0fd60b2912013a` |
| `669997ac28258f26d0bafc81b1d081abb407a3a1` | `review/remediation/20261003-prepare/batches/B20/refreeze-after-B19-C-1/accepted-interface-map.json` | `265041e0830bd47130492e314c67520bb738f562` | `80dde444746b204e6d2a1985da7d41e5bb51e8ae3e2557b9847e8c91055ee28c` |
| `669997ac28258f26d0bafc81b1d081abb407a3a1` | `review/remediation/20261003-prepare/batches/B20/refreeze-after-B19-C-1/catalog-preservation-locks.json` | `f545a0891be7ffa4ad339620aa989e704d607d83` | `2be6a2f9254b0ebc4533630450bcff184efb1e1242979e57d66b9a5e9778160b` |

205 条已接受主责的原 finding / 批准 acceptance 对象 canonical SHA256 从上述固定完整对象重新计算，与 C 统计逐条绑定一致。B10–B19 的本地 `contribution-acceptance.json` 中全部 158 条贡献的完整原对象/验收对象哈希也分别重算匹配。所有 216 个触及 ID 均保留完整 qualified 原对象与完整批准验收对象的引用，root/extension 决策、有效 cases、前提、最低修订、确定再检、证据限制及其它 owner/最终全局义务不因本检查缩减。原 finding 大文件在固定外部 commit，未被递归复制到 C；其绑定的 C 接受记录和 qualified 控制副本未改变。原 PLAN 与批准 finding-acceptance 文件在 C/NEW 都是同一固定 blob。

## 逐 owner 保留范围

下表贡献数从原 PLAN 与 C 逐键重建；旧证据文件数是该 owner 在固定 C 的 `review/remediation/20261003-prepare/batches/Bxx/` 子树文件数量。全部 2,757 个旧 owner 证据文件在 NEW 都保持相同 blob。原 PLAN 所有已存在的各 owner 正式 write 路径也逐个比较：仅 B17/B19 共写的共享目录变动，其余 owner 正式文件全部原样。此处的保留结论不代替 16 条实际 supported interface 的语义回归判断。

| owner | 贡献 / 主责 | 旧证据文件（全部原样） | 原 owner 正式路径变化 | 有界结论 |
| --- | --- | --- | --- | --- |
| B01 | 14 / 7 | 46 | 无 | 接受记录与 qualified 控制原样；须审目录 reverse reader |
| B02 | 12 / 9 | 66 | 无 | 接受记录与 qualified 控制原样；须审 WP74/目录 |
| B03 | 27 / 19 | 106 | 无 | 接受记录与 qualified 控制原样；须审实际消费路线 |
| B04 | 35 / 23 | 121 | 无 | 接受记录与 qualified 控制原样；须审实际消费路线 |
| B05 | 16 / 10 | 76 | 无 | 没有直接 declared route；原接受范围与正文原样，未作总体质量推论 |
| B06 | 10 / 7 | 130 | 无 | 没有直接 declared route；原接受范围与正文原样，未作总体质量推论 |
| B07 | 19 / 12 | 98 | 无 | 接受记录与 qualified 控制原样；须审 supported interface |
| B08 | 17 / 9 | 187 | 无 | 接受记录与 qualified 控制原样；须审 supported interface |
| B09 | 20 / 13 | 298 | 无 | 接受记录与 qualified 控制原样；须审 supported interface |
| B10 | 7 / 2 | 95 | 无 | 接受记录与 qualified 控制原样；须审 supported interface |
| B11 | 6 / 3 | 142 | 无 | 没有直接 declared route；原接受范围与正文原样，未作总体质量推论 |
| B12 | 9 / 6 | 155 | 无 | 接受记录与 qualified 控制原样；须审 supported interface |
| B13 | 8 / 5 | 249 | 无 | 接受记录与 qualified 控制原样；须审 supported interface |
| B14 | 24 / 19 | 247 | 无 | 接受记录与 qualified 控制原样；须审 supported interface |
| B15 | 16 / 10 | 222 | 无 | 接受记录与 qualified 控制原样；须审 supported interface |
| B16 | 24 / 20 | 252 | 无 | 接受记录与 qualified 控制原样；须审 supported interface |
| B17 | 12 / 7 | 83 | 共享 demo 目录 | 原接受记录及 PA040 保留，目录全文件边界见下 |
| B18 | 8 / 5 | 94 | 无 | 接受记录与 qualified 控制原样；三个只读目录原样 |
| B19 | 24 / 19 | 90 | 共享 demo 目录 | 正式 WP72/WP73-A/WP73-B 与原稿 WP72/73-A 原样；目录 B19 行原样 |
| 合计 | **308 / 205** | **2,757** | 只有共享目录 | 静态保留通过；未签整包语义通过 |

## 全共享目录旧/新边界

路径 `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md`：C blob `17ea088afe9e3fb67e4cbeaf5a7e6faa2eff940d`，SHA256 `ffd8992eef39f39892709d5dd591780669c97a0bd59dda9cc0f55818fee2e9f1`，90,084 bytes；NEW blob `a4a5279c9826d87e9663780c6e35a92cc733ffef`，SHA256 `6e9e463d4f6b7d7591d0d30e457787b759c56c4a3638080a15e92e63eb84cc45`，100,779 bytes。

独立解析全 C/NEW，C 原 195 个 ID 的顺序完全等于 NEW 前 195 项，每项原重数均为 1，NEW 同样为 1；无丢失、重排或新增旧 ID 重复。原 195 行中 193 行逐字相同，只改同位置第 126 行 AN-M23、第 161 行 CV-M18；整份原 261 行除这两行外全部相同，包括标题、说明、行外文字和链接。NEW 末尾追加 26 行、19 个新 B20 ID（总 214 项），未插到旧目录中间。重新算 C 全 table row 哈希与派发 locks 一致。

| 行 | C 行 SHA256（不含 LF） | NEW 行 SHA256（不含 LF） | 修订边界 |
| --- | --- | --- | --- |
| 126 AN-M23 | `21f86f266d21175a86be08afe2be5376af5fc615ec6c43eabf078148c6a34d4a` | `a69be02b84e60e2df9ad1c16f13cb9b0aac8824d4d468cbfebcc2fe474bb7a63` | 将泛化渐变一句绑定 WP74 §10.2a，原 20fps、恢复、对方侧、静音和可见标志事实逐字保留 |
| 161 CV-M18 | `0d56469a3dacab50099d9797f305d562cab0e8ebfbfa5556d59621ec92a438cf` | `0d0104748b1826bb6de583b01dcc8416f65c60e1445be330fe7001e43dbbcf4d` | 仅将“后续 WP75”改成已补全 §8.1 合同定位；原 a–e 文本/预期和未执行标志逐字保留 |

B19 17 行全部相同，PA040 三行第 235–237 行全部相同：`B17-PA040-double` / `B17-PA040-training` / `B17-PA040-duplicate`。三行 SHA256 依序为 `44db9b3c35a6aa1792fcea2d4ebcbd4a011e5c7282dac3ff8939bc02884fac0c`、`56003ac20927c82bae0d3c01e5f0c4715e97e318612e7405c724afc2ae0e5956`、`1a116b40c05567fc1c1d1370a560bcdbcd7c55a0432ad6efdaefdc9369f4d406`。这些行旧预期的语义重新接受并未被本报告改写。

全文件唯一显式 Markdown 链接在第 231 行，指向 `review/remediation/20261003-prepare/batches/B17/author-draft-1/traceability.json`，NEW 中路径存在且旧 blob 保留；无新增坏链接。AN-M23 引用的 WP74 §10.2a 对应 NEW 第 317 行标题；CV-M18 的 WP75 §8.1 对应 NEW 第 143 行标题。19 新案例都标 `NOT_EXECUTED`；append 说明继续记录运行观察和 Demo 证明链为 0，未把静态目录升级为测试执行证据。

完整未过滤差异只引用固定发布件：commit `f325f625f879105f7811713d9a38cc58da875de2`，path `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-1/stream/C-to-NEW.full.diff`，blob `54c4dcf3be88f175fcceaca5c3642c29c532adfe`，SHA256 `0889ed6d2a4d300325c0fa5d319d9fd89b72bdaeec8e8a0401c7185a25f9eccb`，1,189,663 bytes（本分工独立读固定件验证 bytes/hash）；未复制差异流或旧证据正文。

## 尚需其它门完成的验收条件

本分工没有发现保留阻塞。此结果仅成立于精确 NEW/tree 与上述 C。新渐变、转换、目录附加案例的行为正确性及 16 条 supported route 是否保留实际条件、数据来源与先行副作用，必须由消费者语义分工作独立判断；B05/B06/B11 的没有直接声明路线也只支持保持现有接受范围，不支持整包质量结论。候选门后，sole registrar 固定唯一 G/ACT，再由原独立 reviewers 分别完成 exact ACT actual 门；本报告不自签 actual 或正式接受。
