# R5-U08 candidate G02 独立审查

G02 在固定当前组合 `e4ea8d03b0e2c7c20fc41fce92f0b2b7b7f02514` 上限定 **PASS**：92 finding、410 原冻结静态条件、568 原接收 reviewer-schema 条件均有本审独立结果、当前证据定位和判断理由。候选整体仍因 UI shared16 的三处过宽取消/无写入语句在 G03/G09 **FAIL**；本支持审不签整包接受或 CLOSED。

| 批次 | finding 单位 | 原static单位 | 原schema row单位 | 额外限定check单位 |
| --- | ---: | ---: | ---: | ---: |
| R5-U01 | 34 | 146 | 248 | 102 |
| R5-U02 | 14 | 46 | 46 | 0 |
| R5-U03 | 11 | 60 | 60 | 0 |
| R5-U04 | 7 | 28 | 32 | 4 |
| R5-U05 | 1 | 4 | 4 | 0 |
| R5-U06 | 18 | 93 | 145 | 52 |
| R5-U07 | 7 | 33 | 33 | 0 |
| 合计 | 92 | 410 | 568 | 158 |

410 个冻结 commit/path/pointer 各唯一映射到一条原接收 schema row。额外 158 单独保留原单位：U01 preserve 27、vectors 42、reference_facts_to_cover 33（102）；U04 preserve 4；U06 preserve_correct_scope 11、runtime_claim_gate 11、preserve 6、additional_proven_conditions 19、runtime_boundary 5（52）。额外行不增加 410 分母。逐项结果见 `criterion-results.json` 的三个主结果数组、额外数组及唯一映射。

我读了七批 task packet 的每项正常、最小反例、前提、失败/边界、排除范围及每条验收条件，对当前 producer、consumer、目录和必要交界作组合核验。原独立审结的未变公式、常数表、阶段与固定 R 证据按精确主体/记录 hash/片段 hash 复用；当前新增或改动交界单独读内容。1930 个原 scoped anchor 关联可在当前定位到精确字节，另54 个重复 broad anchor 属8种原范围的当前插入/限定变化，已用差异映射重新定位并实读改动。字节机械核对本身不提供语义 PASS。日志列清精确输入、实际读取、组合变化和证据复用，不把未改内容制造成新的全局 review。

SC-U07-001：`GR5-M12-002/C01` 只签源一致的纠正前提。六族括号捕获体不能跨 LF；外围空白可以跨行，周围独立行仍可能命中后被整字段替换丢弃。冻结 author 的“捕获体可跨行”子主张已显式排除，原 finding 与 410 分母不变；U07 为32普通static加1纠正条件，不扩大六族运行证明。

U03 `GR5-M05-004/static/04` 当前目录 L294 的461字节行已直接重核：WING 须合法作者记录、非重要、有效消费真（省略/true）才能沿正常效果与后段成功链扣1。Consumable=false 的合法原反例不满足该新行前提；有效false规则保持。原8b25实际 FAIL、1eda报告及两个 advisory MISMATCH 保留，当前只绑定df2实际02及本次e4组合，未转成新全11审。

相邻阻塞：`test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md` L206 A05、L207 A06、L242 A41 中“无其它写入/无任何写入”没有限定换位动作。合法 FURFROU1/t 在目标 pbRefresh 第一次到 t+432001 可先提交 form0、时间/cache/重算/登记前缀，BACK只取消交换。最小修正只限定三句动作范围；这是整篇共享交界 FAIL，不能据此新增93finding。M04-002 的四条原static和四个 required_sync targets 本身仍正确；该总UI目录不在其 required_sync 中，故不虚改 G02 的410/568结果。

WP03 L108 的旧“尚待接入”行政引用保持冻结 U01生成时点及B5资格；实际producer WP27由当前正式接受承接，镜像新增后继段已限定旧PENDING/WAIT时点，没有把旧句改签成当前行为阻塞。

全部新向量为 DERIVED_VECTOR / NOT_EXECUTED。历史R4=4、R5 review=4、更新新执行=0均保持各自有限范围。实际模型/effort/tier/speed回显为 UNVERIFIED；未作模型或额度审计。未改正式、未提交/推送、未登记接受或 CLOSED。

## 逐 finding 独立判断

### GR5-M01-001 — PASS（有界当前组合）

当前WP04接受门与十分之一尺寸最近整数化可逐输入推出点号1/1.0为10和三个符号指数拒绝；基础省略默认1、形态省略继承H与PBS前井号、q/引号位置规则分开，当前WP66B的单位差异保持。

当前证据：generic-kernel/wp04-pbs-lifecycle.md:94–98；test-catalog/generic-kernel-wp02-03-04.md:89–92；generic-kernel/wp04-pbs-lifecycle.md:58–102；generic-kernel/wp03-content-identity-and-schema.md:127–127；generic-kernel/wp03-content-identity-and-schema.md:151–151；test-catalog/generic-kernel-wp02-03-04.md:83–92；creature-rpg/wp18-creature-identity-species-ownership.md:84–99；creature-rpg/wp18-creature-identity-species-ownership.md:291–303；demo-dx/wp73-a-content-editors.md:36–45；demo-dx/wp73-a-content-editors.md:133–138；user-interface/wp66-b-storage-and-pokedex-ui.md:225–231；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:607–607；generic-kernel/wp04-pbs-lifecycle.md:62–76；generic-kernel/wp04-pbs-lifecycle.md:197–197。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-002 — PASS（有界当前组合）

当前默认core同域规范键过滤、替换重建/追加保留旧A/Z、地图只同m桶规则可算出各集合；招式终检/形态脚本/公共地图真实caller分列，作者目标语言导出只按默认非空原文选条，运行回退及先删后写不被改。

当前证据：generic-kernel/wp08-localization.md:97–107；generic-kernel/wp08-localization.md:111–131；test-catalog/generic-kernel-wp05-06-07-08-09-10.md:214–217。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-003 — PASS（有界当前组合）

当前先逐行边连续空白后长度至少2折叠，双LF与单LF命中T、双空格命中U；译文值不经键变换，导入过滤/逆转义、碰撞后覆盖及普通窗口控制各阶段仍独立。

当前证据：generic-kernel/wp08-localization.md:30–34；generic-kernel/wp08-localization.md:69–83；generic-kernel/wp08-localization.md:136–171；test-catalog/generic-kernel-wp05-06-07-08-09-10.md:218–221。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-004 — PASS（有界当前组合）

当前作者BaseStats/Trainer IV/EV列HP攻防速特攻特防明确，不等值/尾缺重复首值/显式0/全省略IV10EV30向量齐；Species EVs具名对不同入口，与公式/Mega/个性环及编辑BACK补0不冲突。

当前证据：generic-kernel/wp03-content-identity-and-schema.md:180–193；generic-kernel/wp04-pbs-lifecycle.md:100–102；demo-dx/wp73-a-content-editors.md:63–70；generic-kernel/wp03-content-identity-and-schema.md:186–193；test-catalog/generic-kernel-wp02-03-04.md:93–96；generic-kernel/wp03-content-identity-and-schema.md:182–193；pokemon-rules/wp19-attributes-ability-and-stats.md:77–115；pokemon-rules/wp19-attributes-ability-and-stats.md:140–200；pokemon-rules/wp22-transformation-data.md:1–77；test-catalog/pokemon-rules-wp19-21-22-23-34.md:71–83；user-interface/wp66-a-party-and-summary-ui.md:142–161；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:610–610；pokemon-rules/wp19-attributes-ability-and-stats.md:162–174；demo-dx/wp76-facility-content-generation-and-simulation.md:112–115；test-catalog/demo-dx-wp72-73-74-75-76-77.md:261–261。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-008 — PASS（有界当前组合）

当前普通归档先全节、恰一节才散文件、可读插件后公共/地图扫描门及次序明确；双引号首片段/单引号排除/注释也匹配、普通与事件反斜线解码不同、非续行/列表末提交的原文差异已同步四向量，002/003原根因保持。

当前证据：generic-kernel/wp08-localization.md:87–107；test-catalog/generic-kernel-wp05-06-07-08-09-10.md:222–226。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-009 — PASS（有界当前组合）

当前CR/LF/TAB/控制1或行首方括号才编码，前空格[Q]不保护并分节先使旧K哈希奇数失败；真实TAB门保护全部括号、无前空格正例及完整入口先截旧输出/单解析不写分别具名，不将运行空译/数字首键规则改掉。

当前证据：generic-kernel/wp08-localization.md:111–119；generic-kernel/wp08-localization.md:135–171；test-catalog/generic-kernel-wp05-06-07-08-09-10.md:227–230。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-010 — PASS（有界当前组合）

当前布尔八文本集合及ASCII任意大小写精确，off/显式空拒绝、省略走字段默认；Consumable=N假、原始false与重要物有效消费分离，井号预处理与浮点事实保持。

当前证据：generic-kernel/wp03-content-identity-and-schema.md:138–151；test-catalog/generic-kernel-wp02-03-04.md:97–99；test-catalog/generic-kernel-wp02-03-04.md:85–85；test-catalog/generic-kernel-wp02-03-04.md:97–97；test-catalog/generic-kernel-wp02-03-04.md:98–98；test-catalog/generic-kernel-wp02-03-04.md:99–99。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-011 — PASS（有界当前组合）

当前类型Gender和成员Gender精确别名范围、FieldUse/BattleUse/Category词表齐，MALE/成员Unknown/数字0拒绝与省略内部0有对照；没有把布尔不分大小写套内联枚举。

当前证据：generic-kernel/wp03-content-identity-and-schema.md:138–151；creature-rpg/wp28-item-use-and-training.md:135–139；test-catalog/generic-kernel-wp02-03-04.md:100–102；test-catalog/generic-kernel-wp02-03-04.md:85–85；test-catalog/generic-kernel-wp02-03-04.md:100–100；test-catalog/generic-kernel-wp02-03-04.md:101–101；test-catalog/generic-kernel-wp02-03-04.md:102–102；creature-rpg/wp28-item-use-and-training.md:381–383；creature-rpg/wp24-player-trainers-partners.md:145–158。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-012 — PASS（有界当前组合）

当前定長先CSV后只求规定位置、额外junk不求值，与空Moves出现仍尝试必需首组拒绝/省略才默认分开；q、大写可选位、六能力及引号耗尽/普通后覆盖/^累加既有路径保持。

当前证据：generic-kernel/wp04-pbs-lifecycle.md:58–102；test-catalog/generic-kernel-wp02-03-04.md:103–105；test-catalog/generic-kernel-wp02-03-04.md:85–85；test-catalog/generic-kernel-wp02-03-04.md:103–103；test-catalog/generic-kernel-wp02-03-04.md:104–104；test-catalog/generic-kernel-wp02-03-04.md:105–105。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-013 — PASS（有界当前组合）

当前类别×威力矩阵在词法后校验再登记，Physical/Special0警告改Status、Status正值拒绝、正常40/0及双缺明确；当前失败不登记且先前条目前缀不回滚，不把警告当拒绝或改变战斗公式。

当前证据：generic-kernel/wp04-pbs-lifecycle.md:137–148；test-catalog/generic-kernel-wp02-03-04.md:106–108；test-catalog/generic-kernel-wp02-03-04.md:85–85；test-catalog/generic-kernel-wp02-03-04.md:106–106；test-catalog/generic-kernel-wp02-03-04.md:107–107；test-catalog/generic-kernel-wp02-03-04.md:108–108；pokemon-rules/wp43-types-accuracy-and-damage.md:13–23；generic-kernel/wp04-pbs-lifecycle.md:231–243。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-014 — PASS（有界当前组合）

当前区域表最终0..最大编号缺席拒绝、显式空0和任意节顺序可补齐、空文件可保存空集合、物种无节读取错与重复各分层；UI全国回退不冒充编译补空，数据空表计数旧失败保持。

当前证据：pokemon-rules/wp62-pokedex-records-regions-and-content.md:95–116；demo-dx/wp73-a-content-editors.md:145–155；test-catalog/pokemon-rules-wp53-60-61-62-69-70.md:263–269。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-015 — PASS（有界当前组合）

当前全局0合法Home在条目登记前、全输入读完0先于1存在门和先全局保存后玩家分阶段明确；玩家2不代1、玩家Home非必需，已登记前缀不撤回/两保存不原子，不凭Home推新游戏起点。

当前证据：generic-kernel/wp04-pbs-lifecycle.md:148–148；test-catalog/generic-kernel-wp02-03-04.md:109–112；test-catalog/generic-kernel-wp02-03-04.md:85–85；test-catalog/generic-kernel-wp02-03-04.md:109–109；test-catalog/generic-kernel-wp02-03-04.md:110–110；test-catalog/generic-kernel-wp02-03-04.md:111–111；test-catalog/generic-kernel-wp02-03-04.md:112–112；generic-kernel/wp03-content-identity-and-schema.md:51–52；creature-rpg/wp24-player-trainers-partners.md:71–79；test-catalog/creature-rpg-wp18-20-24-25-26.md:94–98；demo-dx/wp73-a-content-editors.md:140–143。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-016 — PASS（有界当前组合）

当前有限默认表TownMap/Ability/Ribbon/Move/TrainerType/Metadata逐字段明确，StorageCreator缺空才翻译Bill、份名缺字段回普通而空译不回、地图缺Name查基本信息先失败与显式值绕过齐；M05四默认producer已接、历史pending引用只旧时点。

当前证据：generic-kernel/wp03-content-identity-and-schema.md:93–110；test-catalog/generic-kernel-wp02-03-04.md:113–119；generic-kernel/wp03-content-identity-and-schema.md:110–110；test-catalog/generic-kernel-wp02-03-04.md:85–85；test-catalog/generic-kernel-wp02-03-04.md:113–113；test-catalog/generic-kernel-wp02-03-04.md:114–114；test-catalog/generic-kernel-wp02-03-04.md:115–115；test-catalog/generic-kernel-wp02-03-04.md:116–116；test-catalog/generic-kernel-wp02-03-04.md:117–117；test-catalog/generic-kernel-wp02-03-04.md:118–118；test-catalog/generic-kernel-wp02-03-04.md:119–119；creature-rpg/wp28-item-use-and-training.md:135–139；creature-rpg/wp18-creature-identity-species-ownership.md:84–102；test-catalog/creature-rpg-wp18-20-24-25-26.md:33–33；combat-requirements/wp51-ai-action-selection-and-skill.md:19–25；creature-rpg/wp28-item-use-and-training.md:381–383；generic-kernel/wp08-localization.md:56–65；demo-dx/wp77-demo-evidence-and-capability-coverage.md:49–55；test-catalog/demo-dx-wp72-73-74-75-76-77.md:221–221。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-017 — PASS（有界当前组合）

当前正式形态导出与再编译两阶段将Generation1基/0形态及Grassland基/None形态省略后继承写清，写出当场内存不变；正2和同值省略对照不称损失，普通基础编辑不冒充形态导出caller。

当前证据：generic-kernel/wp04-pbs-lifecycle.md:212–227；test-catalog/generic-kernel-wp02-03-04.md:120–123；generic-kernel/wp04-pbs-lifecycle.md:195–208。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-018 — PASS（有界当前组合）

当前正遭遇版本写出保留、非正省后读0，独立−1与正1及−1/0双表同节头第二拒绝前缀齐；原概率/槽、宽松版本输入和单查询/枚举区别保持，不收紧未来策略。

当前证据：generic-kernel/wp04-pbs-lifecycle.md:128–135；generic-kernel/wp04-pbs-lifecycle.md:212–227；test-catalog/generic-kernel-wp02-03-04.md:124–126。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-021 — PASS（有界当前组合）

当前空图块集未知整数7失败与非空首7回退明确，参数双回退后未登记默认是另一能力；WP03/WP14/向量同步，不以缺布局映射回0替空表成功。

当前证据：generic-kernel/wp03-content-identity-and-schema.md:54–55；engine-overworld/wp14-random-dungeons.md:56–65；engine-overworld/wp14-random-dungeons.md:298–298；test-catalog/engine-overworld-wp11-15-59-60.md:269–269；test-catalog/engine-overworld-wp11-15-59-60.md:662–664；test-catalog/generic-kernel-wp02-03-04.md:127–129。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-022 — PASS（有界当前组合）

当前文本完全缺Autotile或Tile整类在构造前失败，两类提供后才适用缺用途回0；两单边负例/正常对照齐，直接空列表不同输入，当前条目不登记且前缀保留。

当前证据：engine-overworld/wp14-random-dungeons.md:65–65；engine-overworld/wp14-random-dungeons.md:228–243；generic-kernel/wp04-pbs-lifecycle.md:150–150；test-catalog/engine-overworld-wp11-15-59-60.md:665–667；test-catalog/generic-kernel-wp02-03-04.md:130–132。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-023 — PASS（有界当前组合）

当前合法非末姓名真实反斜线引号包围A,2/版本0首次登记，再q节头不保护逗号、重编译改A/2；A无逗号正常、A,B版本拒绝及内存与后续电话身份消费分开，U06电话输入次序不改变此序列化事实。

当前证据：generic-kernel/wp04-pbs-lifecycle.md:184–229；user-interface/wp63-pokegear-map-music-and-phone.md:68–156；generic-kernel/wp03-content-identity-and-schema.md:24–58。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-024 — PASS（有界当前组合）

当前14体型/10色/10栖息身份和定义序、体型0..13图标关联全部具名；HeadArms/Gray/WatersEdge接受/未知拒与Head/Red/None默认保持，U06搜索导航仅改焦点转移、Area仍遭遇/地图不由Habitat字段。

当前证据：generic-kernel/wp03-content-identity-and-schema.md:209–262；creature-rpg/wp18-creature-identity-species-ownership.md:49–101；user-interface/wp66-b-storage-and-pokedex-ui.md:154–246；pokemon-rules/wp62-pokedex-records-regions-and-content.md:118–164。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-025 — PASS（有界当前组合）

当前合并先普通复数后重复单数、跨拼写文本先后不改分组，C单数先/B复数后仍B,C及两个单数自身次序可推出；前向首符合选B、旧复数编辑空与单数导出区别保持。

当前证据：generic-kernel/wp04-pbs-lifecycle.md:152–152；pokemon-rules/wp31-basic-evolution.md:112–154；generic-kernel/wp04-pbs-lifecycle.md:208–208；demo-dx/wp73-a-content-editors.md:19–19；demo-dx/wp73-a-content-editors.md:133–138。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-026 — PASS（有界当前组合）

当前基础首次发现反向前身A/B定义序与最低等级16/30、形态对应关系优先再基础的分层齐；所有前向保留、不合并最小最大或随机前身，WP34回溯消费一致且无环限定。

当前证据：pokemon-rules/wp31-basic-evolution.md:112–126；pokemon-rules/wp34-inheritance-and-offspring.md:46–79；creature-rpg/wp18-creature-identity-species-ownership.md:49–101；demo-dx/wp73-a-content-editors.md:19–19；demo-dx/wp73-a-content-editors.md:133–138。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-027 — PASS（有界当前组合）

当前连接第一端方向才要求反向，整数第一端不执行配对；1,0,0,2,W,0接受、E/W正例、W/0拒绝齐，WP11按端运行换算不保证混合输入所有后续成功。

当前证据：generic-kernel/wp04-pbs-lifecycle.md:154–154；engine-overworld/wp11-map-topology-transfer.md:41–55；generic-kernel/wp04-pbs-lifecycle.md:191–193；generic-kernel/wp03-content-identity-and-schema.md:65–70。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-028 — PASS（有界当前组合）

当前区域词先大写再端修剪及Nidoran具名改写，bulbasaur接受而仅Foo登记词变FOO拒；一般直接身份查询仍精确大小写，不把专用词规则全局化。

当前证据：pokemon-rules/wp62-pokedex-records-regions-and-content.md:95–104；generic-kernel/wp03-content-identity-and-schema.md:24–58。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-029 — PASS（有界当前组合）

当前训练家专用杂行/合法节未知属性跳过与节前等号属性/首Pokemon前IV拒绝四路明确，普通装载WP18覆盖后继仍独立；不将未知跳过泛化无成员/等级/IV/EV或所有非法文本保存。

当前证据：generic-kernel/wp04-pbs-lifecycle.md:156–156；creature-rpg/wp24-player-trainers-partners.md:145–169；creature-rpg/wp24-player-trainers-partners.md:240–258；generic-kernel/wp03-content-identity-and-schema.md:118–124；generic-kernel/wp03-content-identity-and-schema.md:296–298。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-030 — PASS（有界当前组合）

当前非重要Consumable=false正式输出保false是真正通用省略例外，true省略再读真、重要原位真/假有效恒假分开；WP28consumer同步，ShowQuantity不被类推。

当前证据：generic-kernel/wp03-content-identity-and-schema.md:42–42；generic-kernel/wp04-pbs-lifecycle.md:210–229；creature-rpg/wp28-item-use-and-training.md:135–139；creature-rpg/wp28-item-use-and-training.md:343–348；generic-kernel/wp03-content-identity-and-schema.md:110–110。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-031 — PASS（有界当前组合）

当前按定义序先未加入族、每层排序后深度展开/根前/重复首见可推出A,B,D,C而非作者边序/广度，单链及None连族非可进化对照齐；主编辑No不保存，WP62编号接收一致。

当前证据：pokemon-rules/wp34-inheritance-and-offspring.md:46–71；pokemon-rules/wp62-pokedex-records-regions-and-content.md:95–116；demo-dx/wp73-a-content-editors.md:145–155；demo-dx/wp73-a-content-editors.md:164–178；pokemon-rules/wp31-basic-evolution.md:112–154。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M02-001 — PASS（有界当前组合）

当前变量false/缺值0、普通开关0原样、自开关仅true的三表可判定，5000/5001及原始不刷新/便利地图门不变；不把整体持久类型校验当槽值布尔校验，U02消费者判据兼容。

当前证据：generic-kernel/wp09-save-startup-continue.md:83–93；test-catalog/generic-kernel-wp05-06-07-08-09-10.md:231–234。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M02-002 — PASS（有界当前组合）

当前单项只删精确登记、不删条件组与整体两种清空状态分开，X精确D优先删后C、删G仍C、全清不命中具名；命名通知删除合同及解析复制边界未混用。

当前证据：generic-kernel/wp05-events-extensions-plugins.md:28–53；test-catalog/generic-kernel-wp05-06-07-08-09-10.md:235–238。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M02-003 — PASS（有界当前组合）

当前ABC归档给定ASCII流的尾N−offset、恰N EOF假/空串后EOF、长读内部推进/外显夹限、行数和关闭/块重关失败全可推出；真实归档/本地流/byte协议未合并。

当前证据：generic-kernel/wp07-diagnostics-files-http.md:29–56；test-catalog/generic-kernel-wp05-06-07-08-09-10.md:239–243。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M02-004 — PASS（有界当前组合）

当前64树果/4敷料成员逐对固定源再读一致，6旧/7-8新槽布局及389阶段2×3h=21600完整；5/9跳过、未知树果/敷料、符号保持、单项非符号不填仍替换及查询失败前缀分开，不造旧档执行。

当前证据：generic-kernel/wp10-migration-failure-recovery.md:78–109；generic-kernel/wp10-migration-failure-recovery.md:111–209；test-catalog/generic-kernel-wp05-06-07-08-09-10.md:244–248。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M02-005 — PASS（有界当前组合）

当前关键段正常1/普通错诊断后0与DEBUG主入口自身1/脚本循环结束分离，Reset/SystemExit、Hangup紧急保存/Reset及诊断错另路；WP40局部诊断及阶段包装不借此等同场景恢复。

当前证据：generic-kernel/wp07-diagnostics-files-http.md:119–153；generic-kernel/wp09-save-startup-continue.md:110–112；generic-kernel/wp05-events-extensions-plugins.md:47–53；test-catalog/generic-kernel-wp05-06-07-08-09-10.md:249–252。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M02-006 — PASS（有界当前组合）

当前派生两查询先取T可推进锚点、正整数/浮点除法及负保存差不夹齐，无锚5.0/2与L7、锚9→12/13两查询独立可算；会话默认及保存前缀保持，不声称页面或异常S0保护。

当前证据：generic-kernel/wp06-time-random-steps-stats.md:25–40；generic-kernel/wp06-stats-directory.md:118–143；generic-kernel/wp09-save-startup-continue.md:79–79；generic-kernel/wp09-save-startup-continue.md:104–105；generic-kernel/wp09-save-startup-continue.md:125–131；test-catalog/generic-kernel-wp05-06-07-08-09-10.md:253–256。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M02-007 — PASS（有界当前组合）

当前双整数闭[a,b]配底层偏移给5/6/7与等端5，区间优先忽次参、数值非数次参/空首/文本首的委派分别明确；电话20...40与钓鱼原域保持，仅静态给定偏移不认证跨语言序列。

当前证据：generic-kernel/wp06-time-random-steps-stats.md:109–164；test-catalog/generic-kernel-wp05-06-07-08-09-10.md:257–260。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M02-008 — PASS（有界当前组合）

当前小端Σbyte256^j和signed8、短低位/低宽截断与首byte失败前缀可手算；8byte索引M=首偏移/8、合法查询位置/越界读首4/零長不跳偏移齐，整数byte提供方限定不转归档字符流。

当前证据：generic-kernel/wp07-diagnostics-files-http.md:71–86；test-catalog/generic-kernel-wp05-06-07-08-09-10.md:261–265。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-JXN-001 — PASS（有界当前组合）

当前WP11的三材料生命周期表与WP08查找值、WP65先服务再存档名展开相接。两语言域均空限定重复读的确定性，空译先命中后消费者回基本名；新键命中、既有别名、显式保存和UI后段失败逐个保留，不将所有PN显示认成共享写入。

当前证据：engine-overworld/wp11-map-topology-transfer.md:107–115；test-catalog/engine-overworld-wp11-15-59-60.md:585–585；user-interface/wp65-title-load-options-pause-and-pc.md:57–59；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:914–914；engine-overworld/wp11-map-topology-transfer.md:117–119；test-catalog/engine-overworld-wp11-15-59-60.md:586–586；test-catalog/engine-overworld-wp11-15-59-60.md:590–590；engine-overworld/wp11-map-topology-transfer.md:107–113；test-catalog/engine-overworld-wp11-15-59-60.md:588–588；engine-overworld/wp11-map-topology-transfer.md:111–115；engine-overworld/wp11-map-topology-transfer.md:105–119；generic-kernel/wp08-localization.md:67–67；user-interface/wp65-title-load-options-pause-and-pc.md:45–59；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:136–136。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M03-001 — PASS（有界当前组合）

当前页设置与路线41都按原方向/原图案各自变化门，原下当前右+新下保持右，新上才写两值并清预锁；同页、其它有效页、无页及后续动画观察点分开。

当前证据：engine-overworld/wp13-map-events-npc-followers.md:33–35；engine-overworld/wp13-move-route-matrix.md:27–27；engine-overworld/wp13-move-route-matrix.md:74–74；test-catalog/engine-overworld-wp11-15-59-60.md:591–594；engine-overworld/wp13-map-events-npc-followers.md:33–33。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M03-002 — PASS（有界当前组合）

当前角色键查B而私有键查绑定A的双图例前提完整；207/209跟随覆盖与正常结束只解当前图同ID是明确例外，缺当前实例或失联不错误回查绑定实例。

当前证据：test-catalog/engine-overworld-wp11-15-59-60.md:595–597；engine-overworld/wp13-map-events-npc-followers.md:81–94；engine-overworld/wp13-map-events-npc-followers.md:92–104；engine-overworld/wp13-interpreter-command-matrix.md:19–19；engine-overworld/wp13-interpreter-command-matrix.md:33–33；engine-overworld/wp13-interpreter-command-matrix.md:45–45；test-catalog/engine-overworld-wp11-15-59-60.md:595–598。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M03-003 — PASS（有界当前组合）

当前秒式n>t+s严格门与日式商余数加本地日内修正都可推出1010/1011、跨午夜及r=h对照；登记一次墙钟先持久A后私有t，临时A、无记录与失败刷新没有混同WP06游戏变量。

当前证据：engine-overworld/wp13-map-events-npc-followers.md:37–39；engine-overworld/wp59-world-time-weather-field-moves.md:29–29；test-catalog/engine-overworld-wp11-15-59-60.md:599–602；test-catalog/engine-overworld-wp11-15-59-60.md:602–602。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M03-004 — PASS（有界当前组合）

当前209安装立刻尝试首项、运动早退、R1/R2只保存首次非空R0与路线结束恢复相接；空路线悬置、有效页清forcing/无页不清和自主0.74/0.75门保持，未保证安装完成或固定帧。

当前证据：engine-overworld/wp13-move-route-matrix.md:9–25；engine-overworld/wp13-interpreter-command-matrix.md:66–67；test-catalog/engine-overworld-wp11-15-59-60.md:603–605；engine-overworld/wp13-map-events-npc-followers.md:33–35；engine-overworld/wp13-move-route-matrix.md:23–23；test-catalog/engine-overworld-wp11-15-59-60.md:604–605；engine-overworld/wp13-map-events-npc-followers.md:146–146；engine-overworld/wp13-move-route-matrix.md:25–25；test-catalog/engine-overworld-wp11-15-59-60.md:606–607。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M03-005 — PASS（有界当前组合）

当前WP12对角一次两轴逻辑提交且不增加各距离，失败可先改方向但不产生四向触碰/碰撞；WP06及路线表同步，普通一步/非零跳跃正例与一般步完成守卫独立。

当前证据：engine-overworld/wp12-terrain-movement-vehicles.md:146–150；engine-overworld/wp13-move-route-matrix.md:38–41；generic-kernel/wp06-time-random-steps-stats.md:92–96；test-catalog/engine-overworld-wp11-15-59-60.md:608–608；engine-overworld/wp12-terrain-movement-vehicles.md:148–150；test-catalog/engine-overworld-wp11-15-59-60.md:609–610。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M03-006 — PASS（有界当前组合）

当前直接零偏移跳跃绕转身和占格许可并产生jumping，路线状态推进仍沿既有门；非零阻挡和前/后包装0反例已分列，没有凭原地跳强称全局步数增。

当前证据：engine-overworld/wp12-terrain-movement-vehicles.md:99–109；engine-overworld/wp13-move-route-matrix.md:47–47；test-catalog/engine-overworld-wp11-15-59-60.md:611–613；test-catalog/engine-overworld-wp11-15-59-60.md:64–64；engine-overworld/wp13-move-route-matrix.md:9–18；test-catalog/engine-overworld-wp11-15-59-60.md:611–611。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M03-007 — PASS（有界当前组合）

当前解释器公共事件正常空返回使脚本直接钓鱼在事件后仍内置，普通物品true替代整段；正ID最小例、负索引条件、普通取消/失败正常清理和异常不保证清理分别准确。

当前证据：engine-overworld/wp60-fishing.md:69–79；engine-overworld/wp13-map-events-npc-followers.md:98–98；test-catalog/engine-overworld-wp11-15-59-60.md:614–615；test-catalog/engine-overworld-wp11-15-59-60.md:388–390；test-catalog/engine-overworld-wp11-15-59-60.md:614–617；test-catalog/engine-overworld-wp11-15-59-60.md:653–654；engine-overworld/wp60-fishing.md:72–76；engine-overworld/wp60-fishing.md:121–121；test-catalog/engine-overworld-wp11-15-59-60.md:616–616。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M03-008 — PASS（有界当前组合）

当前力量预检查严格双端通行，门过先增计数再尝试普通步再条件记录；普通步未变仍可留计数/快照，仅确变才音效锁定等待，不能从true推成功位移。

当前证据：engine-overworld/wp12-terrain-movement-vehicles.md:86–90；engine-overworld/wp59-world-time-weather-field-moves.md:221–227；test-catalog/engine-overworld-wp11-15-59-60.md:618–618；engine-overworld/wp59-world-time-weather-field-moves.md:225–227；generic-kernel/wp06-stats-directory.md:31–31；test-catalog/engine-overworld-wp11-15-59-60.md:619–621；engine-overworld/wp12-terrain-movement-vehicles.md:89–90；engine-overworld/wp59-world-time-weather-field-moves.md:223–227；engine-overworld/wp13-map-events-npc-followers.md:66–66。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M03-009 — PASS（有界当前组合）

当前202直接/变量/交换三路、主后副落位与仅主方向请求明确；缺副还可转主，缺主/战斗全略、方向固定只阻转，身份复用双图规则未重立缺陷。

当前证据：engine-overworld/wp13-interpreter-command-matrix.md:59–59；engine-overworld/wp13-map-events-npc-followers.md:140–140；test-catalog/engine-overworld-wp11-15-59-60.md:622–622；test-catalog/engine-overworld-wp11-15-59-60.md:623–624；engine-overworld/wp13-interpreter-command-matrix.md:19–19；engine-overworld/wp13-map-events-npc-followers.md:92–94。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M03-010 — PASS（有界当前组合）

当前页/公共并行refresh真值、111开关严格布尔比较、111脚本原值与公共自动原槽形成四消费判据；s:nil比较得false可Else而脚本nil两支跳，正常二值与旧IM保持。

当前证据：engine-overworld/wp13-map-events-npc-followers.md:96–96；engine-overworld/wp13-interpreter-command-matrix.md:33–34；test-catalog/engine-overworld-wp11-15-59-60.md:625–625；test-catalog/engine-overworld-wp11-15-59-60.md:626–626；test-catalog/engine-overworld-wp11-15-59-60.md:627–627。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M03-011 — PASS（有界当前组合）

当前采摘入场取定qty，消息未退出轮的合格微更新可重植；86399→86400后拒摘/满包不reset也不复原成熟，快速拒摘明确排除时间推进，成功仍用旧qty并在尾部返回真后才外层reset。

当前证据：pokemon-rules/wp60-berry-plants.md:124–134；pokemon-rules/wp60-berry-plants.md:147–161；test-catalog/pokemon-rules-wp53-60-61-62-69-70.md:63–70；test-catalog/pokemon-rules-wp53-60-61-62-69-70.md:249–258。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M03-012 — PASS（有界当前组合）

当前355单次辅助加外层推进使紧邻121跳过，缺实例仍推进；116自身推进+false让出是反向，相邻脚本先合并、正常返回及无额外索引/状态干预完整保留。

当前证据：engine-overworld/wp13-map-events-npc-followers.md:56–72；engine-overworld/wp13-interpreter-command-matrix.md:15–17；engine-overworld/wp13-interpreter-command-matrix.md:39–39；engine-overworld/wp13-interpreter-command-matrix.md:120–120；test-catalog/engine-overworld-wp11-15-59-60.md:628–630。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M03-013 — PASS（有界当前组合）

当前WP14各34/136八条件与测试逐输出相同，空角优先固定、第一墙/最上读层及下corridor/上void分开；全未中只重绘、其它修复掩码先重绘再错与初始256表独立，不推出全图/seed/终止。

当前证据：engine-overworld/wp14-random-dungeons.md:149–196；test-catalog/engine-overworld-wp11-15-59-60.md:262–262；test-catalog/engine-overworld-wp11-15-59-60.md:290–290；test-catalog/engine-overworld-wp11-15-59-60.md:631–652。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-JXN-003 — PASS（有界当前组合）

当前StartMoney文本非负校验不夹M，创建保留1000000；零价全成功商店仍写钱包故999999。默认/恰界/先普通写入/确认取消对照和物品→统计→钱包→筛库存次序闭合，未变旧购买回退不扩张。

当前证据：creature-rpg/wp24-player-trainers-partners.md:95–102；creature-rpg/wp24-player-trainers-partners.md:100–100；creature-rpg/wp29-shops-and-exchanges.md:53–63；creature-rpg/wp29-shops-and-exchanges.md:129–148；creature-rpg/wp29-shops-and-exchanges.md:178–178；creature-rpg/wp24-player-trainers-partners.md:102–102；test-catalog/creature-rpg-wp18-20-24-25-26.md:290–294；test-catalog/creature-rpg-wp27-28-29-30-33.md:276–280；test-catalog/creature-rpg-wp27-28-29-30-33.md:128–130；test-catalog/creature-rpg-wp27-28-29-30-33.md:142–142；creature-rpg/wp29-shops-and-exchanges.md:60–62；creature-rpg/wp29-shops-and-exchanges.md:131–148；test-catalog/creature-rpg-wp18-20-24-25-26.md:92–92；user-interface/wp66-c-bag-item-storage-and-shop-ui.md:128–134；test-catalog/creature-rpg-wp18-20-24-25-26.md:284–294。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-005 — PASS（有界当前组合）

当前容量全部负号6与只有−1队伍寻址明确分开，−2/38同盒不同扫描边界及−2读取格29完整；更小负号不保证可寻址，也不认证选择模式后续UI。

当前证据：creature-rpg/wp25-party-and-storage.md:35–65；creature-rpg/wp25-party-and-storage.md:173–173；test-catalog/creature-rpg-wp18-20-24-25-26.md:295–298；creature-rpg/wp25-party-and-storage.md:65–65；user-interface/wp66-b-storage-and-pokedex-ui.md:41–41；user-interface/wp66-b-storage-and-pokedex-ui.md:91–126。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M01-006 — PASS（有界当前组合）

当前WP18普通NPC覆盖表确写缺槽0、性别按类型、异色先普通/超级再Shadow、Nature完整登记零基位置取余；WP24和各向量相接，IV/EV、创建缓存、装载钩子及设施预建例外保留。

当前证据：creature-rpg/wp18-creature-identity-species-ownership.md:202–223；creature-rpg/wp24-player-trainers-partners.md:156–158；creature-rpg/wp18-creature-identity-species-ownership.md:218–223；pokemon-rules/wp19-attributes-ability-and-stats.md:77–115；test-catalog/creature-rpg-wp18-20-24-25-26.md:304–304；creature-rpg/wp18-creature-identity-species-ownership.md:215–223；test-catalog/creature-rpg-wp18-20-24-25-26.md:299–304；creature-rpg/wp18-creature-identity-species-ownership.md:164–195；creature-rpg/wp18-creature-identity-species-ownership.md:219–223；creature-rpg/wp24-player-trainers-partners.md:158–158；creature-rpg/wp24-player-trainers-partners.md:204–217；creature-rpg/wp24-player-trainers-partners.md:249–249；test-catalog/creature-rpg-wp18-20-24-25-26.md:305–305。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M04-001 — PASS（有界当前组合）

当前枚举不限自然两项、不压缩空位索引且保留同索引冲突；PATCH取最后2候选的消息与实际隐藏解析分离，调试只写索引/H标签一致，原resolver与CAPSULE门未被改。

当前证据：pokemon-rules/wp19-attributes-ability-and-stats.md:64–75；creature-rpg/wp18-creature-identity-species-ownership.md:74–74；creature-rpg/wp18-creature-identity-species-ownership.md:96–96；creature-rpg/wp28-item-use-and-training.md:254–265；creature-rpg/wp28-item-use-and-training.md:135–139；creature-rpg/wp28-item-use-and-training.md:343–346；test-catalog/pokemon-rules-wp19-21-22-23-34.md:300–302；demo-dx/wp72-debug-contexts-and-controls.md:149–171；test-catalog/pokemon-rules-wp19-21-22-23-34.md:303–303；creature-rpg/wp28-item-use-and-training.md:234–234；creature-rpg/wp28-item-use-and-training.md:261–265；test-catalog/pokemon-rules-wp19-21-22-23-34.md:294–305。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M04-002 — PASS（有界当前组合）

当前摘要保证继承动态读取例外，与既有R4-IF恰界/forced/battle/storage相接；PRISONBOTTLE普通队伍首次内层提交0后外层请求1只写时间，最终0/新时间/库存1，fresh-time、再用、裸提交与资源失败对照齐备。

当前证据：user-interface/wp66-a-party-and-summary-ui.md:222–225；creature-rpg/wp18-creature-identity-species-ownership.md:148–156；test-catalog/pokemon-rules-wp19-21-22-23-34.md:264–275；test-catalog/pokemon-rules-wp19-21-22-23-34.md:306–307；creature-rpg/wp28-item-use-and-training.md:304–304；creature-rpg/wp28-item-use-and-training.md:321–333；user-interface/wp66-a-party-and-summary-ui.md:109–109；test-catalog/pokemon-rules-wp19-21-22-23-34.md:308–310；test-catalog/creature-rpg-wp27-28-29-30-33.md:283–285；test-catalog/pokemon-rules-wp19-21-22-23-34.md:306–312；test-catalog/creature-rpg-wp27-28-29-30-33.md:281–287；creature-rpg/wp28-item-use-and-training.md:325–333；creature-rpg/wp28-item-use-and-training.md:69–77；creature-rpg/wp28-item-use-and-training.md:323–333；user-interface/wp66-a-party-and-summary-ui.md:225–225；creature-rpg/wp18-creature-identity-species-ownership.md:135–158；creature-rpg/wp18-creature-identity-species-ownership.md:348–348；test-catalog/pokemon-rules-wp19-21-22-23-34.md:91–91；test-catalog/pokemon-rules-wp19-21-22-23-34.md:127–127；test-catalog/pokemon-rules-wp19-21-22-23-34.md:264–293。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M05-001 — PASS（有界当前组合）

当前PC Give先提示、临挂原M、失配自清再访问空物品的失败点清楚，成员无物/邮件、信箱原对象/快照保持；正常背包写信/Take、已有持物/蛋、取消及HP-24同步，不将提示当成功或要求参考补丁。

当前证据：creature-rpg/wp64-mail-and-mystery-gift.md:65–71；creature-rpg/wp64-mail-and-mystery-gift.md:137–140；user-interface/wp66-a-party-and-summary-ui.md:22–22；user-interface/wp66-a-party-and-summary-ui.md:107–107；test-catalog/creature-rpg-wp35-36-57-64-68.md:107–107；test-catalog/creature-rpg-wp35-36-57-64-68.md:174–176；creature-rpg/wp64-mail-and-mystery-gift.md:69–71；test-catalog/creature-rpg-wp35-36-57-64-68.md:174–174；creature-rpg/wp20-hp-status-moves-helditem.md:188–188；test-catalog/creature-rpg-wp18-20-24-25-26.md:65–65；creature-rpg/wp64-mail-and-mystery-gift.md:58–80；test-catalog/creature-rpg-wp35-36-57-64-68.md:99–108；test-catalog/creature-rpg-wp35-36-57-64-68.md:175–176；creature-rpg/wp64-mail-and-mystery-gift.md:71–71；creature-rpg/wp64-mail-and-mystery-gift.md:166–168；test-catalog/creature-rpg-wp35-36-57-64-68.md:167–176。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M05-002 — PASS（有界当前组合）

当前DNA主队伍会话许可仍真下，嵌套把同一K存盒后R是最后可用，形态/融合先写而删除false仍完成工具替换；正常/嵌套取消/关桥/第三可用四对照齐，别的融合处理器只签已证结构不转签全组合。

当前证据：creature-rpg/wp28-item-use-and-training.md:337–341；test-catalog/creature-rpg-wp27-28-29-30-33.md:288–292；user-interface/wp66-a-party-and-summary-ui.md:101–109；creature-rpg/wp28-item-use-and-training.md:339–339；creature-rpg/wp28-item-use-and-training.md:337–339；creature-rpg/wp28-item-use-and-training.md:307–311；creature-rpg/wp28-item-use-and-training.md:339–341；creature-rpg/wp25-party-and-storage.md:109–149。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M05-003 — PASS（有界当前组合）

当前邮件快照规则将k来源、读取玩家party容器与实际收信者分开；盒0/1/越界/暂持0/普通party例都可推出，快照为字段值而非融合活引用，Withdraw阅读正常消费不借PC Give失败链。

当前证据：creature-rpg/wp64-mail-and-mystery-gift.md:29–38；user-interface/wp66-b-storage-and-pokedex-ui.md:109–111；creature-rpg/wp64-mail-and-mystery-gift.md:31–36；test-catalog/creature-rpg-wp35-36-57-64-68.md:177–183；user-interface/wp66-a-party-and-summary-ui.md:127–188；test-catalog/creature-rpg-wp35-36-57-64-68.md:183–183；user-interface/wp66-a-party-and-summary-ui.md:184–188。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M05-004 — PASS（有界当前组合）

当前六能力三族身份表按语义映射，WING条件登记、ZYGARDE例外、候选消息/索引/解析分层和DIREHIT1/2/3阈值都有正文及向量；N02b/HP/PP/Nature算法保持，FocusEnergy1只签给定状态。当前目录L294重新核过合法WING还须非重要且有效消费真（Consumable省略/true）；合法false只增EV不扣的原反例排除于新向量，旧实际FAIL和其余59条不变限定不转签为新全审。

当前证据：creature-rpg/wp28-item-use-and-training.md:241–293；creature-rpg/wp28-item-use-and-training.md:243–252；creature-rpg/wp28-item-use-and-training.md:254–265；creature-rpg/wp28-item-use-and-training.md:263–293；test-catalog/creature-rpg-wp27-28-29-30-33.md:294–294。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M05-006 — PASS（有界当前组合）

当前六个原向量把缺省字段、普通ShowQuantity false仍真、重要图标遮数/PC逐槽、消耗资格和文本枚举域分开；当前WP03引用的U01待接时点保留为历史行政语，实际producer WP27已由当前接受主体承接，不据旧句否定当前字段事实。

当前证据：creature-rpg/wp27-bag-and-item-storage.md:45–62；test-catalog/creature-rpg-wp27-28-29-30-33.md:299–299；user-interface/wp66-c-bag-item-storage-and-shop-ui.md:28–30；user-interface/wp66-c-bag-item-storage-and-shop-ui.md:86–90；creature-rpg/wp27-bag-and-item-storage.md:63–68；test-catalog/creature-rpg-wp27-28-29-30-33.md:300–300；creature-rpg/wp27-bag-and-item-storage.md:69–69；test-catalog/creature-rpg-wp27-28-29-30-33.md:301–301；test-catalog/creature-rpg-wp27-28-29-30-33.md:302–302；creature-rpg/wp27-bag-and-item-storage.md:62–68；test-catalog/creature-rpg-wp27-28-29-30-33.md:303–303；creature-rpg/wp27-bag-and-item-storage.md:45–60；test-catalog/creature-rpg-wp27-28-29-30-33.md:304–304。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M05-007 — PASS（有界当前组合）

当前袋选择>0与给定列表/转换>=0门、NONE/nil/公开0/false不合并；成对转换先验源再清、首匹配物种失败留清空而不重试，函数无匹配为完整对数，与无库存/造个体作用及355继续相容。

当前证据：creature-rpg/wp27-bag-and-item-storage.md:136–149；test-catalog/creature-rpg-wp27-28-29-30-33.md:305–305；test-catalog/creature-rpg-wp27-28-29-30-33.md:306–306；creature-rpg/wp27-bag-and-item-storage.md:145–149；test-catalog/creature-rpg-wp27-28-29-30-33.md:307–307；creature-rpg/wp27-bag-and-item-storage.md:145–150；test-catalog/creature-rpg-wp27-28-29-30-33.md:308–308；test-catalog/creature-rpg-wp27-28-29-30-33.md:309–309；creature-rpg/wp27-bag-and-item-storage.md:151–155；test-catalog/creature-rpg-wp27-28-29-30-33.md:310–310；test-catalog/creature-rpg-wp27-28-29-30-33.md:311–311；test-catalog/creature-rpg-wp27-28-29-30-33.md:312–312；test-catalog/creature-rpg-wp27-28-29-30-33.md:313–313；test-catalog/creature-rpg-wp27-28-29-30-33.md:314–314。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-JXN-002 — PASS（有界当前组合）

当前WP40是普通已选动作异常唯一主合同，完成轮号与失败历史独立；诊断全正常后重取priority按存活/选择/已动过滤，在E全部限定前提下整招PP5→4→3而不是恢复第二击。PP1、单击、前拒、已动后错、裸调用、诊断错及类型覆盖对照保持旧消费前缀。

当前证据：combat-requirements/wp40-commands-obedience-and-action-order.md:198–208；combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md:41–41；combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md:255–257；combat-requirements/wp47-a-move-attributes-targeting-and-calling.md:92–92；combat-requirements/wp40-commands-obedience-and-action-order.md:198–209；test-catalog/combat-requirements-wp47-ab.md:98–109；combat-requirements/wp40-commands-obedience-and-action-order.md:202–204；combat-requirements/wp40-commands-obedience-and-action-order.md:260–270；test-catalog/combat-requirements-wp39-40-41-42-45.md:271–271；combat-requirements/wp40-commands-obedience-and-action-order.md:176–188；combat-requirements/wp40-commands-obedience-and-action-order.md:200–202；combat-requirements/wp40-commands-obedience-and-action-order.md:204–206；test-catalog/combat-requirements-wp39-40-41-42-45.md:271–275；combat-requirements/wp40-commands-obedience-and-action-order.md:208–208；test-catalog/combat-requirements-wp39-40-41-42-45.md:276–282；test-catalog/combat-requirements-wp39-40-41-42-45.md:283–283；combat-requirements/wp47-a-move-attributes-targeting-and-calling.md:76–92；pokemon-rules/wp46-damage-multihit-and-healing.md:29–35；pokemon-rules/wp50-held-item-triggers-and-consumption.md:113–121；user-interface/wp67-a-battle-interaction-and-presentation.md:252–252；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:704–708；combat-requirements/wp47-a-move-attributes-targeting-and-calling.md:90–92；combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md:35–55；combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md:177–191；combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md:251–257。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M07-001 — PASS（有界当前组合）

当前最先拒绝门布尔表保留原顺序，回复/天空摔投/不服从终止是假而显式选择拒绝/普通混乱等真；完整存活尾复制后跺脚75/150准确，false不证明动作成功。

当前证据：combat-requirements/wp40-commands-obedience-and-action-order.md:156–156；combat-requirements/wp40-commands-obedience-and-action-order.md:174–186；test-catalog/combat-requirements-wp39-40-41-42-45.md:249–257；combat-requirements/wp40-commands-obedience-and-action-order.md:218–247；combat-requirements/wp40-commands-obedience-and-action-order.md:174–189；combat-requirements/wp40-commands-obedience-and-action-order.md:188–188；test-catalog/combat-requirements-wp39-40-41-42-45.md:253–254；test-catalog/combat-requirements-wp39-40-41-42-45.md:258–258；combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md:145–154；pokemon-rules/wp46-damage-multihit-and-healing.md:165–165；pokemon-rules/wp46-damage-multihit-and-healing.md:87–87；combat-requirements/wp40-commands-obedience-and-action-order.md:180–188；test-catalog/combat-requirements-wp39-40-41-42-45.md:255–258；combat-requirements/wp40-commands-obedience-and-action-order.md:146–157；combat-requirements/wp47-a-move-attributes-targeting-and-calling.md:179–183。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M07-002 — PASS（有界当前组合）

当前节拍器到更新点按最近身份，无前次最终成功门；免疫后同招0→1/F1.2、前置早退不更新但清身份、异招归0、无效持物/调用壳跳与内层边界分开，倍率min5不误作计数封顶。

当前证据：combat-requirements/wp40-commands-obedience-and-action-order.md:156–160；combat-requirements/wp40-commands-obedience-and-action-order.md:190–194；pokemon-rules/wp50-held-item-triggers-and-consumption.md:55–68；combat-requirements/wp40-commands-obedience-and-action-order.md:190–197；combat-requirements/wp40-commands-obedience-and-action-order.md:192–196；test-catalog/combat-requirements-wp39-40-41-42-45.md:259–262；pokemon-rules/wp50-held-item-triggers-and-consumption.md:64–64；combat-requirements/wp47-a-move-attributes-targeting-and-calling.md:179–183；combat-requirements/wp40-commands-obedience-and-action-order.md:194–194；test-catalog/combat-requirements-wp39-40-41-42-45.md:262–263。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M07-003 — PASS（有界当前组合）

当前WP39合法单侧多业主三打生产缺秩，WP41健康持久B0与离场局部HP0分开，幻觉数值比较错在B1绑定前；2v2、持久失能、B三成员、不触发查询反向限制了异常范围，未改变正常准入或序图。

当前证据：combat-requirements/wp39-battle-context-and-participants.md:174–180；test-catalog/combat-requirements-wp39-40-41-42-45.md:264–264；combat-requirements/wp39-battle-context-and-participants.md:159–165；combat-requirements/wp39-battle-context-and-participants.md:184–189；combat-requirements/wp41-switching-positioning-and-escape.md:85–91；combat-requirements/wp39-battle-context-and-participants.md:174–181；combat-requirements/wp41-switching-positioning-and-escape.md:75–91；test-catalog/combat-requirements-wp39-40-41-42-45.md:265–265；combat-requirements/wp39-battle-context-and-participants.md:176–180；combat-requirements/wp41-switching-positioning-and-escape.md:106–109；combat-requirements/wp41-switching-positioning-and-escape.md:85–92；combat-requirements/wp39-battle-context-and-participants.md:180–180；combat-requirements/wp41-switching-positioning-and-escape.md:91–91；test-catalog/combat-requirements-wp39-40-41-42-45.md:264–269；combat-requirements/wp41-switching-positioning-and-escape.md:46–69；combat-requirements/wp41-switching-positioning-and-escape.md:89–91；test-catalog/combat-requirements-wp39-40-41-42-45.md:265–269；combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md:251–258；user-interface/wp67-a-battle-interaction-and-presentation.md:168–189。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M08-001 — PASS（有界当前组合）

当前四原值实际合同与RAW向量给整数平均、同值写两端、空间读/写分离、替身差异、刷新/接力边界；四Shadow独立接收给当前HP半量/反伤、两伤标记/半血、物品扫描后回复、固定天空5与双侧四屏障，不把SHADOWSHED相近名字当绑定。

当前证据：combat-requirements/wp47-a-move-attributes-targeting-and-calling.md:37–55；combat-requirements/wp47-a-attributes-targeting-calling-data.md:208–214；pokemon-rules/wp23-shadow-data-and-vectors.md:216–228；pokemon-rules/wp44-effect-coverage.md:142–152；pokemon-rules/wp46-damage-healing-coverage.md:43–53；test-catalog/combat-requirements-wp47-ab.md:111–138；pokemon-rules/wp46-damage-multihit-and-healing.md:272–284；combat-requirements/wp45-weather-terrain-side-and-position-effects.md:83–90；combat-requirements/wp45-weather-terrain-side-and-position-effects.md:170–177。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M08-002 — PASS（有界当前组合）

当前鸟嘴加热在已损δ/扣PP/记录后、攻击者自身替身资格查询失败，未灼伤及未到后段明确；无自身替身、已有状态、护具/无接触各早门对照，不机械套自然之恩PP3或宿主恢复。

当前证据：combat-requirements/wp47-b-switching-control-and-item-changes.md:78–84；test-catalog/combat-requirements-wp47-ab.md:141–151；combat-requirements/wp47-b-switching-control-and-item-changes.md:78–85。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M08-003 — PASS（有界当前组合）

当前合法未知实现变化招在使用失败而伤害分类沿普通公式，已扣PP/历史不退；None缺省与空串/非法名称分离，两个人工向量和可选SHADOWSHED未启用条件准确，不修改未来政策。

当前证据：pokemon-rules/wp43-types-accuracy-and-damage.md:29–35；test-catalog/pokemon-rules-wp43-44-46-48-50.md:233–246；pokemon-rules/wp43-types-accuracy-and-damage.md:29–36；combat-requirements/wp47-a-move-attributes-targeting-and-calling.md:13–17；combat-requirements/wp47-a-move-attributes-targeting-and-calling.md:175–183。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M09-001 — PASS（有界当前组合）

当前生命水滴评分独立可恢复守卫先于HPAware且不受预测开关控制，满血保留100、半血107、3/4为95；预测开/Score关本体未入、HPAware关保留100、封锁盟友可达而U封锁先拒，均局部分不授予最终动作分布。

当前证据：combat-requirements/wp52-b-field-damage-healing-and-target-evaluation.md:119–119；test-catalog/combat-requirements-wp49-51-52.md:216–227；test-catalog/combat-requirements-wp49-51-52.md:225–226；combat-requirements/wp52-b-field-damage-healing-and-target-evaluation.md:11–15；combat-requirements/wp52-b-field-damage-healing-and-target-evaluation.md:119–120。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M10-001 — PASS（有界当前组合）

当前真实三行两行窗对照明确七族共享/Party确认忙门及普通显示/商店/帮助反向；局部仍更新不返回，PC前/后业务写点与净化首消息前统计/Shadow/Hyper/缎带前缀精确，未声称EV/经验也提交。

当前证据：user-interface/wp17-messages-windows-input.md:86–102；user-interface/wp66-a-party-and-summary-ui.md:242–244；user-interface/wp66-c-bag-item-storage-and-shop-ui.md:90–92；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:787–906。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M10-002 — PASS（有界当前组合）

当前Move与Common全影子操作分开，第三影子混合真/假对照及无动画早退/正常恢复门齐；焦点正常恢复不自动给异常保证，标记请求不认证像素。

当前证据：user-interface/wp67-a-battle-interaction-and-presentation.md:267–267；user-interface/wp67-a-battle-interaction-and-presentation.md:271–273；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:787–906。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M10-003 — PASS（有界当前组合）

当前bg/message各自时段回退、平台base0决定同base1前缀的有限链闭合，组合基础胜独立夜间、有T不多加B回退；base1缺仅命名不变，解析/加载/包装捕获三层未混。

当前证据：user-interface/wp67-a-battle-interaction-and-presentation.md:45–60；engine-overworld/wp15-resource-matching-and-audio.md:86–90；combat-requirements/wp39-battle-context-and-participants.md:251–253；test-catalog/engine-overworld-wp11-15-59-60.md:540–577。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M10-004 — PASS（有界当前组合）

当前片尾FadeToBlack8/20=.4目标、无DURATION覆写、后更新到期明确，原BGM2秒请求/释放/标记/恢复次序及首次不可跳过保持，不声称8帧或测墙钟。

当前证据：user-interface/wp67-b-lifecycle-presentations-and-history.md:173–173；user-interface/wp67-b-lifecycle-presentations-and-history.md:176–178；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:787–906。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M10-005 — PASS（有界当前组合）

当前轨道第一次实际update起钟、同图同刻按登记顺序首次处理取样与迟到按计划插值闭合；X100/50/0和迟到20→70、回调改起点及多图并行向量正确，聚合下一无轨道更新只限定消费者。

当前证据：engine-overworld/wp16-world-rendering-and-visual-transitions.md:297–313；user-interface/wp67-a-battle-interaction-and-presentation.md:256–256；test-catalog/engine-overworld-wp16.md:153–201。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M10-006 — PASS（有界当前组合）

当前标准帮助BACK先派空回调仍压同轮USE；稳定USE/BACK/双键与换页回调清空独立。只USE推进/末页退出、无其它键、无实际caller及旧等待门保持。

当前证据：user-interface/wp65-controls-help-appendix.md:32–53；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:825–832。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M10-007 — PASS（有界当前组合）

当前HOF BACK先退出，否则USE/LEFT/RIGHT独立覆盖continue；一届三成员LEFT再RIGHT使临时届1/员0/继续并显示K+1，持久历史/K保持。单键、BACK、上限0历史例分开。

当前证据：user-interface/wp67-b-lifecycle-presentations-and-history.md:137–166；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:418–431；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:834–841。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M10-008 — PASS（有界当前组合）

当前播放/停止矩阵按具体入口，BGMStop0无重置而BGSStop0空播放有；系统空播放与通用nil早返不混，音频状态/位置/音量/default覆盖保持，仅签参考显式请求。

当前证据：engine-overworld/wp15-resource-matching-and-audio.md:129–174；engine-overworld/wp16-world-rendering-and-visual-transitions.md:256–269；test-catalog/engine-overworld-wp11-15-59-60.md:401–418；test-catalog/engine-overworld-wp11-15-59-60.md:559–567。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M10-009 — PASS（有界当前组合）

当前雾名/色相才资源重设并重置，opacity只是投影；WP16§5.2/§6同步，清名与hue对照、原零时长保留任务/全景门保持，不设计缓存。

当前证据：engine-overworld/wp16-world-rendering-and-visual-transitions.md:217–235；engine-overworld/wp16-world-rendering-and-visual-transitions.md:256–269；test-catalog/engine-overworld-wp16.md:74–77；test-catalog/engine-overworld-wp16.md:169–176。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M10-010 — PASS（有界当前组合）

当前逐字op×非空起始SE四格及空SE优先分支齐，op抑制默认而不抑显式E，空名不交付也不补默认；仅逻辑请求保留嵌入参数、暂停/结束音效独立。

当前证据：user-interface/wp17-messages-windows-input.md:25–93；engine-overworld/wp15-resource-matching-and-audio.md:130–174；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:540–554；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:843–852。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M10-011 — PASS（有界当前组合）

当前合法前缀N等宽切片、d缺/0取5、创建t0相位与未更新0明确；.375创建/.625为1能反证错误全局2，迟到跳帧/静止回0/127不整除及GIF边界与专用图标相位不混。

当前证据：engine-overworld/wp15-resource-matching-and-audio.md:90–125；user-interface/wp17-messages-windows-input.md:75–84；user-interface/wp17-messages-windows-input.md:235–249；test-catalog/engine-overworld-wp11-15-59-60.md:540–544；test-catalog/engine-overworld-wp11-15-59-60.md:569–581。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M10-012 — PASS（有界当前组合）

当前已有屏幕动画先锚256后父+10返回266、下一静止重归256；父零移/首次标记后建/临时格先位置后推进及相对定位反向保持，不把锚点常数误判或保证像素。

当前证据：engine-overworld/wp16-world-rendering-and-visual-transitions.md:155–174；test-catalog/engine-overworld-wp16.md:178–186；engine-overworld/wp13-interpreter-command-matrix.md:19–19；engine-overworld/wp13-interpreter-command-matrix.md:64–66；demo-dx/wp74-battle-animation-authoring-and-exchange.md:304–330。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M10-013 — PASS（有界当前组合）

当前相同记录位置3请求间无实际父尾clear使第二空单元，已建地图两临时格48→32非零差先失败；构造后clear不补建、请求间clear/零差/0-2/同异父/角色标记各区分，首动画定时与第二登记前缀不回滚。

当前证据：engine-overworld/wp16-world-rendering-and-visual-transitions.md:176–184；test-catalog/engine-overworld-wp16.md:188–201。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M11-001 — PASS（有界当前组合）

当前有限ASCII1-9占位0/x空、已有字符不补尾及地图资格/可见Point并集同步WP62/66B；2/1/0/x/9及Point关闭对照齐，原HAB静态资格保留不扩大Unicode或默认PBS。

当前证据：pokemon-rules/wp62-pokedex-records-regions-and-content.md:127–127；pokemon-rules/wp62-pokedex-records-regions-and-content.md:130–130；user-interface/wp66-b-storage-and-pokedex-ui.md:231–231；test-catalog/pokemon-rules-wp53-60-61-62-69-70.md:222–247。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M11-002 — PASS（有界当前组合）

当前参数普通网格和排序例外表可推出名字空白/U/Z/Cancel、排序0/2/4/OK/Cancel5及半列末行对照；方向仅焦点、USE本地选、OK外层提交、Cancel弃稿三层清楚，单键范围不复制003。

当前证据：user-interface/wp66-b-storage-and-pokedex-ui.md:192–219；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:787–906。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M11-003 — PASS（有界当前组合）

当前具名UI互斥/两阶段顺序与各同轮向量一致：Mining ACTION压USE、Voltorb相反、Tile界外方向吃BACK、Map先移逻辑再模式按钮、Phone先重排再落定/回滚、图鉴子页/主画面、Triad/Pokegear区别齐。未扩大旧optional/no-required。

当前证据：user-interface/wp66-b-storage-and-pokedex-ui.md:213–219；user-interface/wp63-pokegear-map-music-and-phone.md:34–36；user-interface/wp63-pokegear-map-music-and-phone.md:58–62；user-interface/wp63-pokegear-map-music-and-phone.md:76–78；creature-rpg/wp68-triple-triad.md:98–113；pokemon-rules/wp69-voltorb-flip.md:47–61；user-interface/wp70-mining.md:41–49；user-interface/wp71-tile-puzzles.md:72–76；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:787–906。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M11-004 — PASS（有界当前组合）

当前q=floor(vt/H)新边界先停旧顶部、正滑移先减仍转再下一界停，A/B五观察与无停/首次迟到对照可逐项手算；两次旧执行仅设施失败+五限定观察，不认证媒体/支付或全部字段。

当前证据：user-interface/wp69-slot-machine.md:34–48；user-interface/wp69-slot-reels.md:1–3；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:787–906。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M11-005 — PASS（有界当前组合）

当前Mining档10/11工具钟、.25闪光重叠和终局先行、Map发起当轮按钮/后轮插值锁、Tile提交早于末淡入、Triad1.5通知与结果USE及Voltorb/Duel提交阶段都有具名对照；61+13裁片属optional，不按其缺目录扩大必修，全部新向量未执行。

当前证据：user-interface/wp63-pokegear-map-music-and-phone.md:58–62；creature-rpg/wp68-triple-triad.md:98–113；pokemon-rules/wp69-voltorb-flip.md:47–61；user-interface/wp70-mining.md:41–49；user-interface/wp71-tile-puzzles.md:106–120；user-interface/wp68-duel.md:71–89；test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md:787–906；test-catalog/pokemon-rules-wp53-60-61-62-69-70.md:222–247；test-catalog/creature-rpg-wp35-36-57-64-68.md:158–166。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M12-001 — PASS（有界当前组合）

当前散文件每层文件先于目录各排序、大小写.rb及隐藏文件/目录差异明确；读文件在求值保护前，脚本错误族/普通错改消息后899/900与日志失败各阶段，已加载/失败脚本前缀无全滚回，L01–03仅未执行设计。

当前证据：demo-dx/wp75-project-conversion-and-authoring-tools.md:337–341；test-catalog/demo-dx-wp72-73-74-75-76-77.md:299–303；demo-dx/wp75-project-conversion-and-authoring-tools.md:341–352；test-catalog/demo-dx-wp72-73-74-75-76-77.md:304–305；demo-dx/wp75-project-conversion-and-authoring-tools.md:337–352；demo-dx/wp75-project-conversion-and-authoring-tools.md:432–436；test-catalog/demo-dx-wp72-73-74-75-76-77.md:297–305。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M12-002 — PASS（有界当前组合）

当前六族按完整合法行门且捕获体不跨LF，外围空白LF与独立前后普通行丢文另列；六族优先、参数占位/存在/文本规则及18旧核心/默认/可败顺序和trainer-only空分支重访保持。重新定向读固定源六门，排除冻结author错误capture body跨LF子主张；仅C01登记前提纠正限定PASS。

当前证据：demo-dx/wp75-project-conversion-and-authoring-tools.md:219–232；test-catalog/demo-dx-wp72-73-74-75-76-77.md:291–291；test-catalog/demo-dx-wp72-73-74-75-76-77.md:306–306；demo-dx/wp75-project-conversion-and-authoring-tools.md:221–234；demo-dx/wp75-project-conversion-and-authoring-tools.md:223–236；demo-dx/wp75-project-conversion-and-authoring-tools.md:284–291；test-catalog/demo-dx-wp72-73-74-75-76-77.md:170–173。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M12-003 — PASS（有界当前组合）

当前门路径c两页精确方向/穿透/透明/2/6/8/独立等路线顺序齐，位置假仍条件外写临时A；Door enter只具名不猜音参，独立Exit Door80/100与fade无的原目的链分开，路径a/b先行重注册及跟随快照保持。

当前证据：demo-dx/wp75-project-conversion-and-authoring-tools.md:123–132；demo-dx/wp75-project-conversion-and-authoring-tools.md:137–147；test-catalog/demo-dx-wp72-73-74-75-76-77.md:160–160；test-catalog/demo-dx-wp72-73-74-75-76-77.md:307–307；demo-dx/wp75-project-conversion-and-authoring-tools.md:132–147；demo-dx/wp75-project-conversion-and-authoring-tools.md:134–147；test-catalog/demo-dx-wp72-73-74-75-76-77.md:292–292；demo-dx/wp75-project-conversion-and-authoring-tools.md:123–151；demo-dx/wp75-project-conversion-and-authoring-tools.md:284–290；test-catalog/demo-dx-wp72-73-74-75-76-77.md:160–164；test-catalog/demo-dx-wp72-73-74-75-76-77.md:175–175。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M12-004 — PASS（有界当前组合）

当前每事件两族初假、TRUE/YES累计真且后NO/FALSE不撤、首页再战同最终值与下一事件重置四格各族齐；采集门/每块一支先吞边界保留，标量后写/列表追加不被类推锁存。

当前证据：demo-dx/wp75-project-conversion-and-authoring-tools.md:70–84；test-catalog/demo-dx-wp72-73-74-75-76-77.md:308–308；demo-dx/wp75-project-conversion-and-authoring-tools.md:60–107；test-catalog/demo-dx-wp72-73-74-75-76-77.md:153–157；test-catalog/demo-dx-wp72-73-74-75-76-77.md:287–287。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M12-101 — PASS（有界当前组合）

当前新类型/新道具原始Unnamed/???与输入ID/成功提示和dat/PBS/本地化消费分开，已schema文本Yes可改且不承诺其它字段恒等；已有败词父Yes已登记...、外Yes才Trainer.dat、外No重载而嵌套只保存类型dat却反写两PBS的三层表齐，取消/失败/旧进化边界保持。

当前证据：demo-dx/wp73-a-content-editors.md:84–84；demo-dx/wp73-a-content-editors.md:115–115；test-catalog/demo-dx-wp72-73-74-75-76-77.md:309–309；demo-dx/wp73-a-content-editors.md:113–113；demo-dx/wp73-a-content-editors.md:129–129；test-catalog/demo-dx-wp72-73-74-75-76-77.md:310–310；demo-dx/wp73-a-content-editors.md:91–91；demo-dx/wp73-a-content-editors.md:106–106；demo-dx/wp73-a-content-editors.md:169–169；test-catalog/demo-dx-wp72-73-74-75-76-77.md:55–55；test-catalog/demo-dx-wp72-73-74-75-76-77.md:268–268；test-catalog/demo-dx-wp72-73-74-75-76-77.md:299–300；demo-dx/wp73-a-content-editors.md:131–131；test-catalog/demo-dx-wp72-73-74-75-76-77.md:311–311；demo-dx/wp73-a-content-editors.md:90–90；demo-dx/wp73-a-content-editors.md:102–105；demo-dx/wp73-a-content-editors.md:106–108；demo-dx/wp73-a-content-editors.md:108–108；demo-dx/wp73-a-content-editors.md:17–17；demo-dx/wp73-a-content-editors.md:19–19；demo-dx/wp73-a-content-editors.md:136–136；test-catalog/demo-dx-wp72-73-74-75-76-77.md:58–58；test-catalog/demo-dx-wp72-73-74-75-76-77.md:261–262。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M12-102 — PASS（有界当前组合）

当前默认REPEL只打开工作0/???尚不登记，BACK Yes再登记/档案/PBS各成功阶段齐；No/Cancel、BP2/显式1省、非空/空串/缺席份量与SellPrice半价对照不混，零价影响只实际库存无正价覆盖，后段写失败不回撤前缀。

当前证据：demo-dx/wp73-a-content-editors.md:119–127；test-catalog/demo-dx-wp72-73-74-75-76-77.md:312–312；demo-dx/wp73-a-content-editors.md:129–129；test-catalog/demo-dx-wp72-73-74-75-76-77.md:313–313；demo-dx/wp73-a-content-editors.md:123–129；test-catalog/demo-dx-wp72-73-74-75-76-77.md:312–313；demo-dx/wp73-a-content-editors.md:131–131；test-catalog/demo-dx-wp72-73-74-75-76-77.md:299–300。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。

### GR5-M12-103 — PASS（有界当前组合）

当前后置非准备非蛋只限定额外显式登记，普通提交与在场写穿仍登记全局图鉴、场下简化不登记；准备/蛋×seen/forms/owned/seen_egg/首写末次以及ShellosBACK/同值、处理器重算先错/刷新后错齐，既有Summary动态读上游规则保持不复制或自动存档。

当前证据：demo-dx/wp72-debug-contexts-and-controls.md:129–129；demo-dx/wp72-debug-contexts-and-controls.md:160–160；pokemon-rules/wp21-dynamic-forms-and-display.md:187–197；pokemon-rules/wp62-pokedex-records-regions-and-content.md:34–46；pokemon-rules/wp62-pokedex-records-regions-and-content.md:71–90；test-catalog/demo-dx-wp72-73-74-75-76-77.md:314–316；demo-dx/wp72-debug-contexts-and-controls.md:206–206；pokemon-rules/wp62-pokedex-records-regions-and-content.md:15–28；demo-dx/wp72-debug-contexts-and-controls.md:195–207；creature-rpg/wp18-creature-identity-species-ownership.md:144–158；pokemon-rules/wp21-dynamic-forms-and-display.md:189–196；test-catalog/demo-dx-wp72-73-74-75-76-77.md:315–316；demo-dx/wp72-debug-contexts-and-controls.md:284–289；pokemon-rules/wp21-dynamic-forms-and-display.md:191–196；user-interface/wp66-a-party-and-summary-ui.md:220–227；test-catalog/pokemon-rules-wp19-21-22-23-34.md:262–275；test-catalog/pokemon-rules-wp19-21-22-23-34.md:306–312；pokemon-rules/wp62-pokedex-records-regions-and-content.md:145–165。正常/最小反例/失败取消与部分提交/保留及直接同步的逐项判据见 JSON 的本 finding `case_review` 和各 row。
