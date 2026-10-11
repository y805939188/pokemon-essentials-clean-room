# B20 NEW2 五组修复独立挑战检查

固定 NEW2 `3f521e6dea0b442e4bb174a9715c458416386b37` / tree `49f406a6de8ca2786e5dda27abada19780fdfa05`；入口 `81d3be653e87e6424d0d8cd38dab14a9aafc97a1` / `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-2/affected.md`。

**结论：五组增量内未发现残余实质阻塞。** 当前条款与后继静态案例正确排除旧反例；没有新增可支持的反例或增量回归。这是独立挑战子任务，不替代全部 owner 或19/15候选总审，不签 actual、正式接受或 canonical 关闭。

参考固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，只静态阅读。所有案例 NOT_EXECUTED，运行观察及已证明 Demo 链均0。

## C003

CN 绑定玩家 coins 单值窗、G 绑定 money；coins=37/0 与 money=1200 的独立对照准确；增量未改变资源先复制、midi 排除、CommonEvent 收集与首匹配门。

挑战输入：coins 37/0 与独立 money 1200；资源复制后坏动画；独立 CommonEvent 与有 Battle 的末续行。

当前证据：

- `3f521e6dea0b442e4bb174a9715c458416386b37` / `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md`；行 270–270；blob `d77a72b65a44f8d91b62dd06f0b324e7bfac774a`；SHA-256 `603ee184ceaed66dc6d5f6010542fb84e6a7f4da5d326e61b1227c6ad8ca9eb1`。
- `bfc6264bf47478bd174412289de2e31f4da2d9a6` / `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-fix-1/five-group-static-cases.json`；JSON pointer /static_cases/0；blob `1bcabfa4982655b6ccf971dba508e5ea690efc3b`；SHA-256 `14e51d538294bbbe8bfdd10dfd78b1091a99fa5f5ea39d7771dcfacae7196515`。

固定源依据：

- `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/007_Objects and windows/011_Messages.rb`；行 310–343,584–592；blob `91c985bd0fda9a2368c894dee0ebbc9a476e9886`；SHA-256 `88e72c557c53da5a72e4d5b4de7431bbfbd03f4f8f27bcf44ac231a5141b8536`。
- `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/015_Trainers and player/004_Player.rb`；行 11–16,76–87；blob `3a2f3b83a6050831a6fe881b0ccb0ab6ac6e8fd6`；SHA-256 `9b9daa93633906e50430f4d94b3a4ae821d0b0cd568148714f9d3c23952521a3`。

边界：仅合法玩家前提；不扩展到玩家不存在等输入，不重签 B06/B19 旧资格。

## C024

顺序准确为数量门→建/清输出树→逐节输出→备份→装载器，编号只为布局；正常收尾与失败阶段分开，没有必达备份、回滚或异常清理保证。

挑战输入：9/10/11 在两入口各判数量门；清树成功后首文件打开失败，旧备份有/无分设；清树、后续文件、备份、装载器失败按阶段判断已发生前缀/可能截断。

当前证据：

- `3f521e6dea0b442e4bb174a9715c458416386b37` / `deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md`；行 46–48,275–288；blob `d29ea4f31cf0b076991bf2cfda391c7703cd3040`；SHA-256 `9778e9a4909b492812034b1c687e27360f18fd96052d87067ddf32d455d6b237`。
- `3f521e6dea0b442e4bb174a9715c458416386b37` / `specs/demo/wp75-project-conversion-and-authoring-tools.md`；行 297–309；blob `3796ec9ff81a2b3d41fc42a952167c2925e0ca46`；SHA-256 `e4c9c56c7ddf3c80d69f2911c25d3bfb5e55510f1f6700dc1cd155ecf70ed820`。
- `3f521e6dea0b442e4bb174a9715c458416386b37` / `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md`；行 273–273；blob `d77a72b65a44f8d91b62dd06f0b324e7bfac774a`；SHA-256 `603ee184ceaed66dc6d5f6010542fb84e6a7f4da5d326e61b1227c6ad8ca9eb1`。
- `bfc6264bf47478bd174412289de2e31f4da2d9a6` / `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-fix-1/five-group-static-cases.json`；JSON pointer /static_cases/1；blob `1bcabfa4982655b6ccf971dba508e5ea690efc3b`；SHA-256 `14e51d538294bbbe8bfdd10dfd78b1091a99fa5f5ea39d7771dcfacae7196515`。

固定源依据：

- `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `scripts_extract.rb`；行 12–66,71–73,154–179；blob `094c156e87e881d585ba0d326264c13e593d2063`；SHA-256 `4ffa2f449c07d492a248f76247d772e4d0b480c8a2a831a359fbf112cbba7d3f`。
- `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `scripts_combine.rb`；行 76–116；blob `56773c9d99fdfbfd8eb36be70a1fc49121ebcbb4`；SHA-256 `ae85c1e8c8de9ef95a33d5523b2311b63c9e758c607bb2c4878952a46bbc004e`。

边界：静态分阶段 IO 分析，没有运行提取/合并/加载/反序列化。

## C028

训练家 max 版本与联系人地图全局遭遇版独立；四种缺资料正常回退准确，不覆盖空队伍、非法参数/物种；播放开始消息后各计算一次并全段复用。

挑战输入：联系人 current=1/start=2；全局遭遇版3独立；无训练家；请求版缺且0版在；双版缺；三表缺空；队伍 A/A/B；遭遇五槽 A/A/B/C/D 任意权重；无占位符/多段仍计算；TP 或 TE 异常按阶段判断。

当前证据：

- `3f521e6dea0b442e4bb174a9715c458416386b37` / `deliverables/final-specification-set/demo-dx/wp77-demo-evidence-and-capability-coverage.md`；行 113–121；blob `e792348b0a7f35145736f7d595e86ec290b420b8`；SHA-256 `d1ba7c694f41ee5c3763a725467996632264e504563be74036c20d6ad5021ca6`。
- `3f521e6dea0b442e4bb174a9715c458416386b37` / `specs/demo/wp77-demo-evidence-and-capability-coverage.md`；行 137–145；blob `64fc5fcf9ace768deaa640cc7f9a4190473785ea`；SHA-256 `46a5e1883baa6c524779f080feb7bec0602f14c3b62b0ff7c2ae41bb4cbb7180`。
- `3f521e6dea0b442e4bb174a9715c458416386b37` / `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md`；行 277–277；blob `d77a72b65a44f8d91b62dd06f0b324e7bfac774a`；SHA-256 `603ee184ceaed66dc6d5f6010542fb84e6a7f4da5d326e61b1227c6ad8ca9eb1`。
- `bfc6264bf47478bd174412289de2e31f4da2d9a6` / `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-fix-1/five-group-static-cases.json`；JSON pointer /static_cases/2；blob `1bcabfa4982655b6ccf971dba508e5ea690efc3b`；SHA-256 `14e51d538294bbbe8bfdd10dfd78b1091a99fa5f5ea39d7771dcfacae7196515`。

固定源依据：

- `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/013_Items/004_Item_Phone.rb`；行 414–439,506–535；blob `f98163636a7d6082c2e1a8875ecd6e3b9b8fb007`；SHA-256 `81519d2fb0b6926ac2ca08f693e2f08e3800878628ba90f5a7d2a314ff1c60f4`。
- `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/010_Data/002_PBS data/013_Encounter.rb`；行 30–35；blob `e69d300dd0e21690e5970452017e4c2bd457021a`；SHA-256 `d7ebeb1d00434f5da96165ad407101a14d007bce03fa0d0e267c5ee293c183f7`。

边界：电话首槽抽样区别于实时遇敌权重；未执行播放、随机、Demo 注册或公共事件链；WP63 只读资格引用。

## C029

普通读取、处理器真正到达、简化读取已区分；forced=0 优先，战斗与仓库分别返回 stored 0/1，两状态假才求动态0/1及提交不同候选；原稿正确局部审计保持并附外层门。

挑战输入：stored0 加宝珠或旗标，战斗与仓库各为真；stored1 无宝珠无旗标，战斗与仓库各为真；forced0 覆盖 stored1 及动态条件；正常状态动态0写回；form_simple 不求动态；其他物种不可借用 GIRATINA 规则。

当前证据：

- `3f521e6dea0b442e4bb174a9715c458416386b37` / `deliverables/final-specification-set/demo-dx/wp77-demo-evidence-and-capability-coverage.md`；行 142–147；blob `e792348b0a7f35145736f7d595e86ec290b420b8`；SHA-256 `d1ba7c694f41ee5c3763a725467996632264e504563be74036c20d6ad5021ca6`。
- `3f521e6dea0b442e4bb174a9715c458416386b37` / `specs/demo/wp77-demo-evidence-and-capability-coverage.md`；行 168–176；blob `64fc5fcf9ace768deaa640cc7f9a4190473785ea`；SHA-256 `46a5e1883baa6c524779f080feb7bec0602f14c3b62b0ff7c2ae41bb4cbb7180`。
- `3f521e6dea0b442e4bb174a9715c458416386b37` / `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md`；行 278–278；blob `d77a72b65a44f8d91b62dd06f0b324e7bfac774a`；SHA-256 `603ee184ceaed66dc6d5f6010542fb84e6a7f4da5d326e61b1227c6ad8ca9eb1`。
- `bfc6264bf47478bd174412289de2e31f4da2d9a6` / `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-fix-1/five-group-static-cases.json`；JSON pointer /static_cases/3；blob `1bcabfa4982655b6ccf971dba508e5ea690efc3b`；SHA-256 `14e51d538294bbbe8bfdd10dfd78b1091a99fa5f5ea39d7771dcfacae7196515`。

固定源依据：

- `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/014_Pokemon/001_Pokemon.rb`；行 147–165；blob `55e7e42c93cc8c0ae91f8594e7a7b9560eb9c22f`；SHA-256 `3a7f233156f09a6d2e3729bdaa9d1962bfa946aaaa7403042aaea5dcdcdf8cb4`。
- `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb`；行 267–273；blob `d643bcc5fc09d233880174bb2b7004c843d224ac`；SHA-256 `09697fb94d9e8565049cb45401cbb0bf7e610203068417bdc70741add590ae97`。

边界：不据地图进入推断即时变形；WP18/WP21 提交及旧资格只引用，不重新批准。

## WP80-INTAKE-R01

正向四前缀冒号明确 U+003A，U+FF1A 只为负例；前缀大小写不敏感与身份、有效页面和 Battle 门独立；Type 全角例仅排除该类型提供，不误断全部收集为空。

挑战输入：item/hiddenitem 大小写与只换冒号码点；Battle 大小写正例与没有其他有效 Battle 的全角例；Type 全角例仍另有有效 Name/Battle；招式与 Common 名称、其他括号/逗号/大小写门不外推。

当前证据：

- `3f521e6dea0b442e4bb174a9715c458416386b37` / `deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md`；行 22–29；blob `d29ea4f31cf0b076991bf2cfda391c7703cd3040`；SHA-256 `9778e9a4909b492812034b1c687e27360f18fd96052d87067ddf32d455d6b237`。
- `3f521e6dea0b442e4bb174a9715c458416386b37` / `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md`；行 287–287；blob `d77a72b65a44f8d91b62dd06f0b324e7bfac774a`；SHA-256 `603ee184ceaed66dc6d5f6010542fb84e6a7f4da5d326e61b1227c6ad8ca9eb1`。
- `bfc6264bf47478bd174412289de2e31f4da2d9a6` / `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-fix-1/five-group-static-cases.json`；JSON pointer /static_cases/4；blob `1bcabfa4982655b6ccf971dba508e5ea690efc3b`；SHA-256 `14e51d538294bbbe8bfdd10dfd78b1091a99fa5f5ea39d7771dcfacae7196515`。

固定源依据：

- `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/021_Compiler/004_Compiler_MapsAndEvents.rb`；行 473–529,556–570,771–807；blob `cb302adb0c236984c0b4acc5ea61d31c7048dcca`；SHA-256 `3fd9c8c754f3af9bb6204b2492d266fb252cbcd8771593a6650f70601b9b13cc`。

边界：无变化的 Move/OppMove/Common/Trainer/SellItem/s: 条款依固定旧独立证据及字节保留；未重读全部播放/编译；CV-M07 历史字节保留而当前解释明确。

## 独立元数据核验

独立核对 repair-navigation 的34个固定对象身份，均匹配。51个子例按 C003/C024/C028/C029/INTAKE 为3/12/14/12/10，均明确未执行、无观察或质量自签；固定案例对象在 NEW2 字节相同。

NEW→NEW2 的214个目录 ID 次序、重复次数相同；209行字节保留，只变化五个本批目标行。六个只读依赖及两份 WP74 字节不变；WP63/WP18/WP21 新相对链接目标在 NEW2 存在。

完整 OLD_NEW→NEW2 差异只在内存重建：45路径，1884759bytes，SHA-256 `e06540c61ffcc6e1ef8e05e6008b6af999d7c4c5de53cdd860a15ccef6803e5b`。没有再次输出或保存差异流；根复审者另核本轮唯一发布完整差异。

未变的全量义务引用固定旧 affected `680e3988c4144db269e063971991134b8e0bd678` 及 FULL `df1539b67988d4f161b31935752a7f13aec8556b`；并非重新批准旧 owner。各对象及行范围哈希、旧报告身份见 [b20-r2-challenge.json](b20-r2-challenge.json)。

只创建 /tmp 自己的两个最终输出，未修改仓库/正文/原稿/main/旧证据/参考，未 commit/push，未运行任何禁用程序。
