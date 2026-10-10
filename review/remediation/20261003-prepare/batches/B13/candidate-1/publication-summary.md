# B13 候选普通发布与独立读回

冻结候选：`57c79e4a9db6a9b987a8000c3afc5bdcd8dd9aa6`，tree `82a700aac54b7a0d3c0a2357edd06c20abe91232`。分支 `codex/cloud-dot-B13-author-1-20261010`；普通push，无force。远端 `ls-remote` 与重新抓取的 `FETCH_HEAD`、tree 分别相等，47份全部变更输出逐文件通过Git blob／SHA-256／字节数及实际字节读回比对；7份正式稿＋40份本批作者证据。[完整收据](publication-receipt.json)记录每份身份。

未过滤正式FIX_BASE→候选全流见 [base-to-candidate.full.patch](base-to-candidate.full.patch)：SHA-256 `c5ea06ec875b3fa7ee356d3b3c53dd56cf4ab543ecabd987532d871734ee0818`，2101596字节。正式7稿 `git diff --check` 干净；全流的差异格式空白诊断仅来自保存的真实whole patch上下文空行，完整诊断在收据中保留，没有归一化历史或提案字节。

入口：[独立复审派发](review-dispatch.md)。原稿范围确认尚未到达；whole patch `11bfdbd21211dce18016569c7bb5dd9447b90531475f70920e737ae77df0e769` 未应用，B027/B028/B029原／净一致最低门未满足。父先确认精确四份范围、应用并重冻结后，独立Ultra FULL8/5＋必要受影响候选门；通过才G，actual两未过滤流独立门通过才C。作者没有签复审／G/C，B16仍只读、canonical未关闭、B030非必修。

全部行为是静态文本推导；52身份核验不是整历史阅读，136项为未执行设计。参考／Ruby／游戏／向量／历史程序均未执行，继承全部源限制及具名未读范围。后继报告提交追加本收据与完整流；它不是替换上述冻结候选。
