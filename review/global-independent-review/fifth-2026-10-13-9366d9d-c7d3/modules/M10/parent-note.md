# 父会话新增精确范围（同一B5/R，不是新全局轮）

M02完成时只签自己的语义范围。请M10承接这些可读剩余区间并写明确去向：
- 001_Technical/001_MKXP_Compatibility.rb:11–29（文字偏移）。
- 001_Technical/002_RubyUtilities.rb:35–53、130–140、172–334（文字/矩形/颜色相关；据具体行为核归属，不能仅因未在初始路径表而跳过）。
- 004_Game classes/002_Game_System.rb:41–273（音频/资源与控制）。
- 019_Utilities/003_Utilities_BattleAudio.rb 全149行（选择和回退）；必要与M05训练家、M07战斗入口交界。
- 019_Utilities/001_Utilities.rb:48–62、193–280、284–428、521–624 是M02未签领域部分。请与实际职责分段接收，你负责其中UI/音频/呈现；剩余列出精确owner建议交父会话，不自签其它业务。

字体与根媒体由root做材料解析：modules/M12/font-cmap-metrics-inspection.json记录8字体的全部cmap/度量/边界及FreeType样张；default字体族名称已与MessageConfig1–176对照（Green27/Small21/Narrow27）。这不是原生游戏字体/像素/Font.exist?证明。两个BMP全部64像素已解析；Scripts.rxdata装载器解码也在M12，避免重复身份审计。你仍须自行完整审查UI源算法和相关合同，不以root资源解析替代语义审查。

若已开始，请在下一分段或最终覆盖检查时读此提示；不重读已完成无关范围。


C00补充：B5 review/remediation/20261003-prepare/batches/B17/author-draft-1/static-cases.json 全40记录，与B09/candidate-2/static-cases.json中AUDIO-MATRIX/AUDIO-MEMORY-CONSUMERS/FORGET-CANCEL为有效具名夹具补充。B21已接受候选 e58486178e746273fb6fab55df00722807f1dc44:review/remediation/20261003-prepare/batches/B21/author-draft-1/static-cases.json 含ARROW-PHASE、AUDIO-ORDER、CASE-DISPATCH；当前树无该文件可用git show，不是缺资料。对你已审范围补精确承接，避免重读无关全域。主会话C00只作语料分类不代源验证。另根Fonts/BMP/soundfont由主会话解析，见modules/M12/resource-review.md与content-inspection；M10无需重复二进制解析，需音频/字体的接入/资源选择合同比对。
