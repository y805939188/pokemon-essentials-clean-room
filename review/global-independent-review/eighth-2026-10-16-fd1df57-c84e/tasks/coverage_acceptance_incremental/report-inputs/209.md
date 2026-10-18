# R8 云端有限预检

结论：**READY_WITH_LIMITS**，可在本任务独占目录继续静态审读。`UPDATE_NOT_STARTED`。这不是全量语义审查完成或游戏运行通过。

合同 `eighth-global-review-prompt.md` 已从指定 Library 文件完整恢复并阅读全文，36653 bytes、SHA256 `63944b6f264a8e4ed1415db710443a0673f250b8a248af2274a425a314ea068b`。根 AGENTS 已全文读取。指定 `clean-document-revision` 本地未找到，经 Library 精确标题检索恢复 `review-SKILL.md`（3598 bytes、SHA256 `ac3c8560f38192269b65b061673896a77f5eb794b90e90644e3c445b2c3be1f8`）；全文已读，适用于最终态整改交接正文，明确不用于改写审计历史。

## 当前身份与保护

- 启动核验时 B8 HEAD `fd1df570cad987dc3852a3b958f03916e317f7fe`，当前分支 `codex/review-eighth-20261016-fd1df57-c84e`；另保留原 `work`。后继本任务观测到主会话合法纯报告提交 `7478d8daf357d569ac12bea211b4b5f257861930`，其formal tree仍为固定 `f292698cdd4a8e725525a9be6dc34b75faaf151e`；受审对象始终是固定B8/R，后继工具按固定对象校验，不要求报告分支HEAD永远等于B8。本机无 main、origin/main 或 tag。原题 Mac 中35分支/257tag/8worktree库存不属于此云端 clone。
- R HEAD `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，当前分支 work；本机仅一个worktree、一个本地分支。R origin 为 `y805939188/pokemon-essentials`，不能写作本机 origin 为 Maruno17；原来源身份与远端核验由主会话另存。
- `evidence/command-records.json` 绑定两仓 staged、unstaged、untracked、ignored、refs、worktree、remote、HEAD 的实际 argv、完整分离输出、底层exit及UTC。初查 staged/unstaged均空；R untracked/ignored均0；B8报告任务正并行新增，按时点的untracked库存不等同冻结输入或保护前67,835个文件。
- 云端 `/Users/dingshinn/.../readiness.json`、`final-input-binding.json`、原嵌套reference路径均不存在；本轮实际R路径为 `/workspace/pokemon-essentials`。本机未找到 `.bundle/.bak/.backup` 或上述两准备文件。搜索只证明指定类型/名字的有限备份导航结果，不证明不存在任何恢复字节。历史gzip报告对象在B8中可读。
- 本任务从未改动R、formal、planning/audit、历史记录、原refs或其他worktree；未git add/commit/push。独占写集为本目录。

## 可用能力

Linux x86_64。实测 Python3.12.14、Node24.19.0、Git2.52.0、file5.46、GNU binutils objdump/readelf/strings2.44、ripgrep15.2、fontconfig2.15.0、fonttools/ttx4.61.1、ImageMagick7.1.1-43。Ruby、mono、monodis、dotnet、wine不在PATH；未安装。原Mac Ruby/Python/Node版本与隔离执行不能继承为云端能力。

Codex CLI0.159.0-alpha.3的 `--help` 与 `agents --help` 已真实核验，后者为交互会话浏览入口，没有回显全局 JSON 状态或实际模型配置。CLI输出的只读PATH aliases警告保留，exit0不证明后台会话/行为运行成功。未调用login、doctor、认证或额度接口。

请求 model=`gpt-6.1-sol`、effort=`ultra`、tier=`default普速`、speed=`Fast off`；实际model/effort/tier/speed及平台session ID逐项 **UNVERIFIED**。collaboration可见同一任务树7个running agent；操作系统仅有限进程名检查。外部/全部Desktop/云端会话与其写锁不可全局证明，未见本独占路径的具体冲突写者。无需等待不存在的全会话停机证明。

## 材料与恢复

R资源实际齐备：8字体、2BMP、SF2、Game.exe、animmaker.exe、extendtext.exe、Ruby310 DLL、zlib DLL、Scripts.rxdata、messages_core.dat、mkxp.json及2根scripts工具。无完整Graphics/Audio或RMXP工程数据；432 tracked/现存无额外文件由库存任务独立核验，不能冒称Mac准备时434。

R6 `9aa72...:review/remediation-sixth-20261014-prepare/inputs/limit-records.json` 可由git show恢复，与B8的14319 bytes完全同字节；L01–L14已全文读取。R6原报告commit76038...在本机缺失。R7 C2 commit458064...可用，B8保留完整gzip内容运输。已有恢复导航不是本轮语义阅读信用。

`restore_selected.py` 已先审懂再运行：只从固定本地payload-index读取选定125个resource/工具对象，在此前不存在的 `recovered-resource-evidence/` 目录输出104487771 bytes；逐对象核gzip bytes/SHA256及解码bytes/SHA256/Git内容身份，详见receipt。不联网、不运行恢复程序，语义信用0。该恢复工具第一次只成功一次；后续当前literal提取发生一次locator缺sha错误，失败与partial目录保持；v2写入独立新目录后成功，不覆写失败证据。

本轮当前可读程序新提取720单元：55完整shader正文、5prelude、6误识别非shader数据、650 C模板/诊断候选、3兼容Ruby与extendtext机器码小体。源码偏移与SHA身份见 `current-programs-v2/inventory.json`；55完整shader、5prelude、6误识别候选及3兼容Ruby已连续完整阅读。650候选随后也按220/220/210完整读取，分类为646条件C生成片段与4处标点/字符表误命中；片段不授完整native generator控制流或执行资格。controller1666记录已完整结构解析（含2个特殊xinput身份），记录内容仍待本轮语义阅读，不能把恢复/结构解析标为FULL_READ。

后继又独立扫描5 PE全部当前字节的5条明确ASCII程序marker规则，315候选中248包含已读单元，67另行完整新读：13条额外条件C生成片段、53条诊断/metadata非程序和1条已读shader尾接字节。故已读C片段至少659条；旧650候选不是发现完备证明。此扫描仅闭合具名有限规则，Unicode/UTF16、压缩、其他语法/native CFG仍不外推，详见 `literal-discovery-reception.json`。

为主会话后继独立新上下文另冻结精确有限min4字符串库存：ASCII258727、UTF16LE的ASCII子集1434，共260161候选，其中255158尚未逐项接收，包含大量可打印机器码/随机候选而不自动是真实文本。controller1666及全部候选的精确offset/length/SHA/decoder/记录结构和consumer导航在 `handoff/readset-index.json`，完整可派发提示为 `handoff/next-context-prompt.md`。这批已定位可得未读明记UNREAD，不属于L04。初版慢提取中断的真实exit254/partial证据保留，优化v2 exit0；没有语义升级。

animmaker是.NET托管程序；extendtext是原生Win32程序，不能称两者都有IL。animmaker全15方法/743指令/1670CIL bytes/11EH已本轮全文读取。extendtext全部有限1740byte `.text`控制流、17导入和数据请求已读；0x40129b填充使线性反汇编误对齐，已从真实callback0x40129c重建。两者仅SOURCE_STATIC，不是工具业务运行。

## 具名执行边界

L01完整工程/Demo、L02完整媒体、L03兼容宿主、L04原生selector/全机器码CFG、L05 GPU/后端供参/像素、L06图像/XML库效果、L07 Win32真实返回/几何/周期、L08目标字体发现/渲染/hinting、L09原生SF2装载/guard/合成、L10原生loader/语言质量、L11无界插件组合、L12真实服务/存档、L13许可法律结论和历史PASS资格、L14历史执行元数据缺口均继续按原准确前提保留。现存可读材料的未读仍列UNREAD，不转成limit。

本任务的参考行为、独立行为模型、完整宿主/Demo、原生媒体、真实存档/回放执行均0，不能把本任务计数外推为整轮。主会话通知Creature任务有1个Python数值探索进程（exit0、stdout含空结果 `[]`，缺startUTC、无验证信用）；全局执行台账由主会话按实际汇总，参考/宿主仍0。静态解析与身份工具另计；本任务行为向量 `NOT_EXECUTED`。早期本任务的若干直接读取仅保留于平台tool回显，未伪造为当时已本地捕获；后继run_logged工具才有单独本地stdout/stderr/UTC/exit。
