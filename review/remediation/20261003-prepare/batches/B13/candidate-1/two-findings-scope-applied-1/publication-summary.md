# B13 scope2应用后最终候选发布

最终 NEW candidate：`db9e6ed1997efe5bf94dac952aad44fd3b9ebd21`；tree：`d7e8953fb0f3eff949c3dbee1f9361b0b8f71804`。复审OLD：`5845e8084ced280e51c51a4081ec8583a9c2ca39`；正式FIX_BASE：`8e67f780c204d593d89f364f585d2c6c2fe74631` / tree `ae2f491294eb4f97be6b75f75706c16279f9bf46`。作者分支 `codex/cloud-dot-B13-author-1-20261010` 普通push成功；独立ls-remote及fresh FETCH_HEAD/tree一致，全部118输出actual byte读回一致。后续publication仅加本summary、receipt、完整OLD→NEW流，不改候选载荷。

WP58 scope-amendment-2 `231c9f25df4dd64961fb9290ff52302782a9fdb8` 的固定patch `8d186d65c9eb2bc0e03a27728bfa0ea8476f4753bb863054b41cdb3b79459b0d` 已精确应用原稿§5.2；全文件after SHA256 `0dbd9207664b04d6ea869c5252bb91c8f4559eff0072656ea733f0a4043b5bc4`，其它条款未变。B027 nil精确身份修复、B029净稿/RC-W26/entry轨迹导航全部保持，未扩展原稿B027或邻域写域。

完整未过滤差异 `OLD-to-NEW.full.patch`：2008347字节，SHA256 `0319f0e2a4d4ed0c520724e9eeb67b84ef254f46abdd62ec54ed3f7982be0aff`；生成命令`git diff --binary --no-ext-diff --no-textconv 5845e8084ced280e51c51a4081ec8583a9c2ca39 db9e6ed1997efe5bf94dac952aad44fd3b9ebd21`无路径过滤。FIX_BASE→NEW及上一publication→NEW亦整体生成、绑定完整字节和命令于receipt。

以 review-dispatch.md/json 入手，由父任务协调原Ultra FULL complete8/5和原Ultra affected B09/B11增量复核；逐问题响应、完整原控制对象、最低验收、保护/有限影响接口都在作者successor目录。原OLD的FULL NEEDS_REVISION及affected REQUEST_CHANGES保持历史身份；范围许可不代替新质量结论。

目录137条静态设计全部未执行；W16/W24/W25及其他原行保持，上一publication的99个其它输出字节一致。formal diff-check PASS；完整流的whitespace诊断只在精确保留的raw .patch上下文，receipt保留原诊断，未将全文check伪称PASS。未运行参考/Ruby/游戏/行为向量/历史程序，未自签门、未新开子任务、未G/actual/C、未合main；canonical/B030增量0，B16仍依赖B13-C。
