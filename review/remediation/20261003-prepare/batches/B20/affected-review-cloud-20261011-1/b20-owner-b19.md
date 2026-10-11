# B20 NEW 对 B19 的独立有界静态复审

审查对象 NEW `1abaefb1db5818ff9404392143c476979d34c21a` / tree `2e40f9ad0e8fa40377d39e5a19eaa74cc2e05e85`；基线 C `de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f` / tree `88a400af08253bea8d97ee2ef2fa6636f0900f92`。派发 `669997ac28258f26d0bafc81b1d081abb407a3a1` 的完整合同和 `/interfaces/18`，入口 `9a46a131ba2f7ea82b6eed823aa892cb57b0fba7` 的 `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-1/affected.md`，最终读回包 `272885cca76c36cd04dde27b6be2c654759ec4c2`。源只静态读取 `/tmp/b20-reference` 固定 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。

结论：B19 的 24 个局部接受贡献/19 个主责资格在支持接口范围内未回退；不能为本 NEW 给零阻塞 PASS。新增共享目录 B20-C003 对 CN 的预期有 AF-03/P2 语义错误，必须修正。它不撤销 B19 旧资格。本文不签 FULL19/15、actual、正式 C 或 canonical；所有案例 NOT_EXECUTED，运行观察和 Demo 已证明链均为 0。

## 固定接受与六个实际输入

B19 固定接受来自 C 的 `review/remediation/20261003-prepare/batches/B19/acceptance-stage-1/contribution-acceptance.json`；其 actual 是 `a022325260df386cb8d8033314c8464be6edc2e7` / tree `8d82cd04b4925b874a16167e3779666b18adda87`，FULL actual 报告 `9dfbf89aba953a872a2680ff22946464a89d9861:review/remediation/20261003-prepare/batches/B19/actual-full-review-20261010-1/contribution-review.json`。独立读取其 24 行 qualification、旧回归及有限非局部义务，继续绑定完整 root/extension/current qualification，并没有把 scope 许可当质量 PASS。

相对 B18→B19 真正改变的六个输入，在本次 C→NEW 中，正式 WP72/WP73-A/WP73-B 和原稿 WP72/WP73-A 五份逐字相同；共享目录有界改变。独立重新读取 git 对象计算的具体 identity 在同目录 JSON `six_real_inputs`，包括 C/NEW blob、SHA256 和 bytes。五份 SHA256：WP72 `18e9ec45f08b760648e2fa4f459c96ea2443d39f22b900e8d36d3f64068fba66`，WP73-A `02b63271965d2b7cec1c45dc481fe8207f50d02348db6ee3492efedc5672d41c`，WP73-B `ef3372a419206c9972e5f316fb047432b54447b22e2d8790dbd3fbd70926dcef`；原稿 WP72 `6b50e82e43035f0eeba573a6004bee5a3fb021aaa5c4ee43131f21483a1733a9`，原稿 WP73-A `87f89a9338fd59e3cf89131895945a37ec44f4cb7230d5d9e7a979c888aa65d1`。

身份不变只证明未改写；以下消费者条件检查支持有界保留判断。

## 逆向消费者与条件边界

1. **WP72 调试可达性和 120 效果。** 正式 WP72:213–216/303–447 保留完整成员83/阵营22/全场13/席位2，各项行为/类型/登记默认/范围/复位与表外禁止。独立 C/NEW120行（每行LF计入）同为 SHA256 `0cb237496cb3708aa709327d4bb830a5516a605c4a710ed19d2975726f2064dd`；源 `006_Debug_BattleExtraCode.rb:5–176` 静态文本完整允许项仍为83/22/13/2。E005伤害0–999、E088登记−2/显示基线−1/ACTION−1、成员当前指向空位失败与候选跳空位/RIGHT无尾界搜索不被 B20 声称改变。B20 改动的 WP74 单元/帧/时序和 WP75 事件转换并不以这120表作为编辑允许输入；其直接消费者是动画集合/命令页。WP75 编译入口沿 WP72:260–273 的工具归属，源 `Debug_MenuCommands.rb:1335–1344` 调强制全量编译；不扩成普通玩家可达，不把调试编辑当正常招式流程，不给取消或自动存档新保证。WP77:150 同样把工具入口与 Demo 玩家事件链分开。

2. **WP73-A 编辑、取消、档案/PBS/缓存。** 正式 WP73-A:17–25/65–75/81–101/131–148 的父门/子页返回、共享嵌套规范化、新建类型立即写出带出既有训练家编辑、外层No重载档案但不回滚已写PBS，以及 Evolution单复数差异仍保留。WP75:76–79 的反向调用只消费训练家缺失新建入口和字符图查询：源 `Compiler_MapsAndEvents.rb:440–467` 先经调试与不再问门，类型存在才缺训练家三回答；:569–577 的图名为空在拼目录前失败。该编译器调用链不吞掉 WP73-A 内部取消/落盘分层，也不等同底层独立缺失入口的非调试异常。组织器同文件源 `EditorScreens.rb:1252–1257/1291–1318`：首槽空拒绝；内存换序/删插立即，Yes才写档案清集合缓存，No不写盘，Cancel继续。这与 WP73-A:147 和 NEW WP74:350/408 一致。B20 显式补默认Yes/BACK=Cancel而没有改成所有取消不写、所有保存热更新。

3. **WP73-B 世界消费者。** 正式 WP73-B:17/48–55/74/91–105/127/141–163 保留遭遇登记、档案、PBS、当前地图快照四阶段：Land0档案保存为0而PBS省概率后成功重编译21；OldRod0重编译0；同版本赋值/普通保存/No/调试Compile均不重装当前快照，真实新版本或入图才刷新，宽限4→0、累积210保留。指标输出按保存时非零形态后缀选路径、等值省行、档案已存后PBS失败不总回滚、已有战斗布局不广播重定位。WP75新改事件转换写地图/公共事件和系统开关表，不向这些快照/指标布局宣称全局刷新；源 `Compiler.rb:1020–1036` 的 compile_all 仅按 PBS→动画→事件→消息顺序调，各调试入口不调用全局数据清理。B19 C004/C005/C016目录行均逐字相同。原稿 WP72:278–306/WP73-A:162–174 保留源审计入口和这些限制，无改写源组织要求。

4. **资源筛选与先复制。** 源 `Debug_MenuExtraCode.rb:597–633` 先收目录、从载入结果取集合、按文件名末3字符筛选后安全复制音图，再处理 `.anm`；:634–659逐项坏解码局部跳过、非空目录末尾无条件保存和清集合缓存。`.midi`并不匹配末3字符，而`.mid/.wav/png`等合格资源仍在坏动画之前复制；安全复制源 `Editor_Utilities.rb:16–43` 以存在/同内容/不同内容确认三门控制。WP73-A音乐列表器是不同消费者：`Editor_Listers.rb:212–229`直接glob `*.midi`可列它；不能把这里的支持移植为批量导入必复制。C/NEW旧AN-M28:131、NEW WP74:368和B20-C003:270的midi不复制/mid先复制均正确。affected入口短句“.midi先复制资源”不精确，不按其字面推回归，也不能据此改写正确旧行。

5. **CommonEvent 真正可达块。** 源 `Compiler_MapsAndEvents.rb:473–490`拼连续注释并经13前缀收集；:523–565按顺序只消费首个解析支，独立CommonEvent无收集资格；Battle首块吞续行；EndBattle支更早吞其续行；EndSpeech有收集无解析，末续行CommonEvent可到该支。:567–570还需真实Battle，:695–715在有RegSpeech的电话登记链消费公共事件号。正式WP75:63–78和原C/NEW目录CV-M03:146保持上述区别，B20-C003未退回虚假的Battle/CommonEvent组合成功预期。

6. **精确ASCII、动画编译/战斗lookup/cache。** 必要兼容字符由已接受B19 s:/全角s：对照与C/NEW旧CV-M02:145/CV-M07:150/CV-M11:154/AN-M29:132逐字保留；新B20-INTAKE:287明确ASCII冒号/括号/逗号不能全角替换。源 `Compiler_CompilePBS.rb:1274–1319`读取磁盘集合、从空映射建立，Move:/OppMove:ASCII冒号后匹配空白消费而尾/内部空白保留、注册标识大小写敏感、同侧后槽覆盖；任一有效条目写出、零有效旧映射保留。源 `Scene_PlayAnimations.rb:412–485/491–519/568–578`先侧映射→对方回退→类别/类型→TACKLE，关联槽可加连击号；普通Common和球爆Common都直接拼Common:与输入名，精确匹配。没有统一前缀去空白，Common:X和Common: X仅随输入名X/空格X各自命中。NEW WP74:396–399、AN-M29:132、B20-INTAKE:287支持这一区分。

动画缓存另见源 `MiscPBSData.rb:39–52`：已有集合缓存优先，映射缓存首次装载后持有；源 `AnimEditor_Functions.rb:994–1001/1157–1169`临时另建集合与两确认分开，组织器/导入只清集合缓存，不自动清映射缓存；`MiscPBSData.rb:11–22`全局清理才同时清两缓存并有具名前提。NEW WP74:43–57/403–421未把保存、换序、编译与战斗读取混为即时更新；重编译更新磁盘映射、缓存读者须另有相应失效，不能从编译成功推所有既有消费者同步。与B19编辑取消/缓存资格保留相容。

## 整个共享目录独立核验

目录固定path `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md`，C SHA256 `ffd8992eef39f39892709d5dd591780669c97a0bd59dda9cc0f55818fee2e9f1`（90084 bytes），NEW SHA256 `6e9e463d4f6b7d7591d0d30e457787b759c56c4a3638080a15e92e63eb84cc45`（100779 bytes）。独立解析整个C/NEW，195旧ID在214新ID前缀中顺序和重数完全一致；193旧行逐字不变，只有 AN-M23:126 和 CV-M18:161 更新；追加19行位于末尾。17个B19行和3个PA040行全部逐字相同。AN-M23只把原过粗渐变说法收敛到实际共享旧值/访问/RGBA合同；CV-M18修复与WP75新完整35兼容转换目录的交叉引用，不移除原赋值/比较/右操作数/变量号5/队伍变量号3事实。这不替代本批实际动画/转换FULL质量门。

完整未过滤差异只引用 `f325f625f879105f7811713d9a38cc58da875de2:review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-1/stream/C-to-NEW.full.diff`，blob `54c4dcf3be88f175fcceaca5c3642c29c532adfe`，SHA256 `0889ed6d2a4d300325c0fa5d319d9fd89b72bdaeec8e8a0401c7185a25f9eccb`，1189663 bytes。未复制差异或旧报告全文。

## AF-03 / P2：新增CN预期错误

静态前提：消息文本含受识别的CN控制码、存在合法玩家及coins状态，按普通消息消费者；不需Demo事件、反序列化或任何运行。NEW目录B20-C003:270写“CN金银铜钱”；同NEW `review/remediation/20261003-prepare/batches/B20/author-draft-1/per-ID-remediation-and-static-cases.json:32` 的 unique_expected重复该说法。旧C/NEW CV-M14:157则准确写CN为代币窗。固定源 `011_Messages.rb:330–343`窗口只读玩家coins并显示Coins，:587–589识别cn只调用这一个代币窗；gold窗口是不同g分支（:584–586）。不存在CN金/银/铜钱分档或替换规则。新增预期不准确，使同一正式目录对必要格式码的结果不一致；旧资格仍成立，但本NEW有界消费者案例门不能零阻塞通过。

最低验收：仅将新增B20-C003及其同一预期JSON映射改为“CN代币窗（读取玩家coins）”等精确文字；准确区分G金钱窗；保持旧CV-M14、17个B19、3个PA040旧行、195旧ID顺序和重数及其它四个midi/CommonEvent/ASCII边界。修后在新固定NEW逐项静态读回正文/目录/JSON一致，普通发布并独立读回；既有差异流按固定引用，不递归复制。若其余门通过再由原主审判自己的candidate结论，后续ACT另行独立两门；本报告不自签actual或正式接受。

同目录JSON保存六输入逐条真实逆向消费者/范围/保留判定、24项B19有界义务理由、独立identity、目录重建、固定source SHA256/bytes和范围及AF-03对象；没有把哈希检查冒充新语义阅读。未运行参考游戏、Ruby、编译器、转换器、反序列化器、行为向量或历史执行脚本；未修改仓库、参考、main、旧证据或接受登记。
