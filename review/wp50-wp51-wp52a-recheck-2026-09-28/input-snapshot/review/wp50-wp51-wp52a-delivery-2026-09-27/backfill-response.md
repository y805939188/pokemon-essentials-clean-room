# WP46／47-A／47-B限定回填与批准同步回应

2026-09-27；提取方执行记录。权威为[独立报告](../wp46-wp47-review-2026-09-27/report.md)及[下一批提示](../wp46-wp47-review-2026-09-27/next-batch-prompt.md)。本报告授权三条观察实际同步后CLOSED及旧三包管理回填；新WP50/51/52-A不能自行Reviewed。

## 1. 固定预检

九必检＋五补检（14件）完整SHA-256／字节及逐字节均匹配本轮input-snapshot；另七件级联规格匹配。预检详值在self-checks的preflight／cascade_preflight，记录被审身份而非更正后身份；未覆盖快照。reviewer本轮顶层13件保持原件（包括review-notes.json）。

## 2. 获批准的语义同步

### WP47-B-N01 — CLOSED

回源核实SwitchingActing:97–115、UseMove:381–430/456–505、SuccessChecks:435–445：尚存反射标记可能改变换出候选，外层实计击数仍是后段门。修改WP41 §8及场景、WP47-B观察状态。静态验收：普通单目标反射，反回降阶可成功、外层0击、后段不换；普通成功换出仍有资格／存活／后备门。保留边界：没有泛化为所有反射永不能换出，不重开登记/UI/执行分层。

### WP47-B-N02 — CLOSED

回源核实UseMove:136–157/180–206/522–539及SuccessChecks:183–236。修改WP40 §5.2步骤18和场景：消费时最近招找真实槽，specialUsage=false，普通前置后才扣PP。静态验收PP2→1；未醒睡眠在扣PP前拒仍2；正常恢复保存的已行动轮。保留边界：未将原行动保留写成PP／最近记录不变，未改舞者／普通简单调用和已闭合无防守。

### BATCH-N03 — CLOSED

回源核实SwitchingActing:229–252、UseMove:660–707、Move_Usage:232–237。修改WP41 §8与破替身对照：野生主要效果读当前耐久0或绕替身，非野生后段读本击吸收标记。静态验收：唯一存活野生、canRun与等级门过、替身5破至0且T活→决定3；未破不置3；非野生同击拒拖出。保留原无替身场景，不加吸盘／扎根到野生分支。

三项已由2026-09-27独立报告§3 CONFIRMED且明确授权；本次实际写入／验收／差异登记完成记CLOSED，不声称首审原版已有新字节。

## 3. C01维护与管理回填分列

1. WP46来源467–485、1–80拆开，只有记法，未添未读范围。
2. WP47-B鸟嘴加热：UseMove:660–686与UseMoveTriggerEffects:47–60证实HP提交后每击反应才反灼；首击不重算，后续击可读新灼伤；保留接触／接触许可／可灼伤门。
3. WP46附表神秘守护归WP45建立／期限、WP44免疫查询；shared分布1/29/31保持。

三主稿／附表回填Reviewed（限定静态范围，首审PASS_SCOPED）：WP46 A～F139、WP47-A A～E55、WP47-B A～F60。六被审首稿身份留史，状态回填、上述维护与三条语义更正分别记账。其它受影响规格只级联实际完整引用，不改额外旧行为；WP44附表未变，因此无空diff。

## 4. 原被审／更正回填后实测身份

| 文件 | 旧完整SHA-256 | 旧字节 | 当前完整SHA-256 | 当前字节 |
| --- | --- | ---: | --- | ---: |
| `specs/combat/wp40-commands-obedience-and-action-order.md` | `13ac33470f375f2a3c5f0af7acddb6b038b98ba058e73397f39babf592d32b42` | 42,751 | `8c80e5f3f4c3d6ad151bfa65c8a4fce5691adafb318b14565f89f929b24acbe8` | 43,769 |
| `specs/combat/wp41-switching-positioning-and-escape.md` | `1b7e395b98727e3aa7272ad73d3873c77f4581d0acd18ac71cc6703736a77ccb` | 31,948 | `a5232a1ed18dc24257748c34b2ec83eca9730e2c8ef077c7be638ff3b4d38036` | 33,281 |
| `specs/pokemon-rules/wp43-types-accuracy-and-damage.md` | `b5ac8946316fae5cac765db52d2344767bca2f9e5abed52ebfc331a216040ed7` | 30,921 | `d8ba547b3c1f8338f9f00fdac67c146ecd147942c94d576f77d27e4375cb905b` | 30,921 |
| `specs/pokemon-rules/wp44-statuses-stat-stages-and-immunities.md` | `a4e82ddf09d9d9db4e4d610e8dc074d5ef093136b74290dd83b84f764a6bdf9c` | 50,426 | `3d4d9c40d83746459df0c89353a046abd8d4ca32e82e2de76e0ab44499273d1e` | 50,426 |
| `specs/combat/wp45-weather-terrain-side-and-position-effects.md` | `7ddb026aa71e8576d54ab2f98df5e78e84066e28eccbada4f551ca5ae58e5d95` | 36,525 | `046e8bf04fc663e41a6e48c3f9aaa193022d141fea39752eeb2db87a306bd597` | 36,525 |
| `specs/combat/wp42-growth-end-of-round-and-battle-outcomes.md` | `8b8149c3b1f6ee7d130802a4fe1638404a5ac76e7927ee4ce77c85ee5127620f` | 41,759 | `126e2612e2776c41557475a98cd97b8ef40a0a7f02fd95f16c434de49855a3eb` | 41,759 |
| `specs/pokemon-rules/wp48-ability-calculation-modifiers.md` | `457a47b0438a5664fa75e1988251e5aefea2620efec0c006c4f78f7c12a00611` | 35,320 | `1c701d507747d95ba456f3df8a2697b0a1e409d1508dd2d8651b7d50d102403c` | 35,320 |
| `specs/combat/wp49-ability-phase-triggers.md` | `b5c083209e218dc17d7490cc2f171a653502d05e58ec66b83b403ea6d96b4e25` | 53,127 | `e41ca96da9f15bc88526f31337aefe3ba767b9b19776ceba0a6472df1061253c` | 53,127 |
| `specs/pokemon-rules/wp46-damage-healing-coverage.md` | `170e063faaea4b66b5e8a7fc0b9bba907ff7aba7b4c15d8f435ff50d51f7ce88` | 36,408 | `549cd587095df207bf359c34fd66f14f2dda0c93ce1dcaec6bf4f63fc4d084c1` | 36,824 |
| `specs/pokemon-rules/wp46-damage-multihit-and-healing.md` | `0e5a676e234a71a949602d93a2a6aeb4c26cf09acc894e47eee66eb3c1e8a323` | 47,352 | `aa9a7f1e206275ce934a1bc3cf860813bafac852795a5d939316c6f5d9e8bf4c` | 47,646 |
| `specs/combat/wp47-a-attributes-targeting-calling-data.md` | `1c164a68ed2d35c1dceaa9314038a9fe0f6a011c845a9adf512f740a466a898c` | 18,920 | `49e343003be7c22653cad121f3c037b915212da18b6240cda12e653d07c91a17` | 19,340 |
| `specs/combat/wp47-a-move-attributes-targeting-and-calling.md` | `ad6a6d6c4d5c90dbf32f5cd0c843a84dad605319ee4a99c1d5d3d04f8f57b49c` | 33,207 | `1b1dea7cee12b38d867f81122718e328857bc8f17096632e9178bf07b5ff6675` | 33,611 |
| `specs/combat/wp47-b-control-items-coverage-data.md` | `3a092b6653b0d283a47e45aa4ed9b06b04ca62683a14b17b42048829bf00d83c` | 17,454 | `0736044d556367392e2a0204a4a934a903d3472c9cb28435b4765798d915d13a` | 17,922 |
| `specs/combat/wp47-b-switching-control-and-item-changes.md` | `24185ce4179387c900b11e3505d9309f1869ba8587aa2bd263609f1eec25c0bd` | 37,934 | `0287e0b2ea569d24330933ae06498e61237eb0dc9d4116efa9783cc72f739317` | 38,558 |
| `planning/feature-matrix.md` | `9b0ac4a232ec2df4855f8ad31b32d9ef2d9511185d4384647f57c515b434efc8` | 48,848 | `35935419cb9648d4bfd60665d7a7719a9d79230b9d7585bf852a9120ef87ab30` | 49,556 |
| `review/wp46-wp47-delivery-2026-09-27/self-checks.json` | `da4c44a0fbd29ce8d656e98a102d331b8a13c0acd6de4b8c62b511b13c59d57b` | 203,805 | `eda9101ab5b563f5c3b53e53b029a6d0c82ec8e96a7358c3e4e0c6c7be2318c9` | 209,456 |
| `review/wp46-wp47-delivery-2026-09-27/boundary-checks.json` | `b39ff17c64ab09e136b031968ed44d3cfbaf826d81517103bbbb7b27f215503b` | 10,413 | `2cb48235c7794e4167128a399f04c9cb3465e299c9096da1ecde6e49f9d6dae0` | 23,256 |
| `review/wp46-wp47-delivery-2026-09-27/delivery-summary.md` | `85f4df02f5592cca3d91fbbb46aec7d86ea5378f83012661455f04910beb0554` | 6,945 | `73226fe59a5b6036bdabb913f121d5cadd76e23ad2f62c9a54dc686d173697c6` | 6,036 |

## 5. 差异与新批边界

[backfill-diffs](backfill-diffs/)共18份，基线均为本轮wp46-wp47-review/input-snapshot；包含14份实际改动旧规格（WP40/41、必要级联、旧六主附表）、矩阵及旧摘要/self/boundary三件。diff由文本生成，最后逐块重建检查；不覆盖历史回应和原差异。

限定通过集合＝WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP49（WP47为A/B）、WP59–WP60。新三包见[交付摘要](delivery-summary.md)，只ReviewPending；WP52-B/C和任何第四包未启动，运行与阶段出口保留。新包内AI近似差异属于预测合同，不据此静默扩改旧真规则。
