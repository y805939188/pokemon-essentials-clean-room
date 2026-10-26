# 5.3 进化整数参数：五文件正式规格候选

**候选，未正式接收；未 push/merge。** 在 reference 独立分支 `codex/spec-integer-evolution-20261025`、worktree `/Users/dingshinn/Desktop/pokemon-framework/.worktrees/reference-integer-spec-20261025` 上，基于 `main@dae67763071cfe135b99f90639d71425410b1ed3` 准备最小修订。原 main 与既有调查封印不变。

## 范围及版本决策边界

只改下列五个正式文档/目录文件；对应净化行为已由前序独立调查复审 PASS，见 inputs/INVESTIGATION-REVIEW.zh.md。此次仍须对固定新候选做独立差异复审；前序PASS不自动签新字节。

1. `pokemon-rules/wp31-basic-evolution.md`：§3.9新增30项逻辑Integer→u绑定、词法/缺参阶段、领域上界及大整数；§3.8标明既有单复数合并适用R，测试导航引用BEINT。
2. `generic-kernel/wp03-content-identity-and-schema.md`：§5.1指向绑定；§5.2必需参数行限定本次30项及两个来源差异，不改通用i/u/v定义。
3. `generic-kernel/wp04-pbs-lifecycle.md`：§4.5仅补进化参数行/CSV/条目/终检阶段和版本映射；既有合并段加R限定。
4. `test-catalog/pokemon-rules-wp31-32-37-38.md`：BEINT逐方法边界、领域/版本对照，链接已净化的2880静态展开向量。
5. `test-catalog/generic-kernel-wp02-03-04.md`：S53-INT七个阶段向量。

发行 v21.1 `ea7b5d56…` 与既有参考 R `8c5911e4…` 并列保留，**未为实施者选择新目标版本**。两来源均全u、允许0/前导零，参考无安全整数上限；单数支持与缺参差异不能揉成统一事实。v21形态缺参编译缺陷不要求未来兼容；有限整数表示或兼容政策仍由已授权实施目标决定，不由本候选暗改。

## 现有锁定流程核对

已读根AGENTS、当前HEAD/分支/状态及CURRENT-DELIVERY/历史导航；进一步核实真实HEAD已包含第八轮。实际131文件正式树为 `93dc967b4cdb653359afc123d3b8b318d6475fdd`，不是根旧导航保留的第七轮树。第八轮final-report、closure/final及接受记录要求固定输入、候选/实际独立复审、协调接收分层，并保留既有冻结业务/证据身份；未发现禁止在新分支提出候选的通用规则。当前授权明确只本地候选，不push/merge。

因此在干净新worktree中建立 `BASELINE.json` 全131身份；五文件改动只是待审候选。原有发布封印、所有历史审查/接受台账、CURRENT-DELIVERY、范围说明、routing/planning和其它126正式文件均不改，不把本候选计入旧ACCEPTED/CLOSED计数。协调者未来若接收须以新固定SHA处理整合/必要actual复核，不能覆盖旧封印或把作者PASS当实际接收。

## 净化输入和验证资格

`inputs/investigation-r1/` 六文件及 `inputs/INVESTIGATION-REVIEW.zh.md` 从原调查按字节复制，只有行为/向量/定位/哈希，无Ruby片段、实现TS或源码快照。原调查根与其SHA清单不改。`SOURCES.json`内本地路径仅供审计，实施者不应打开原版路径。

所有行为仍为 SOURCE_STATIC／DERIVED_VECTOR／**NOT_EXECUTED**。本轮仅进行Git、哈希、计数、导航与文档差异检查，不运行原版、GUI、NW、框架或其测试，不新增源调查。请求独立gpt-6-sol/ultra与Standard/nonFast；有效配置无完整回显则UNVERIFIED。

## CSV 原始行尾与空白检查资格

初次全包默认 `git diff --cached --check` 把封存CSV的CRLF报为尾部空白；同一shell命令未在此停止，已形成内容提交，未amend或隐藏该失败。默认全包检查不是PASS。五份正式文档检查为PASS；保持通常三种空白检查、仅显式允许CRLF数据行尾的临时命令检查全包PASS。原CSV与调查封印字节一致，不规范化或改全局/仓库配置。两检查退出、2912条行尾诊断计数及摘要见 `CHECK-QUALIFICATION.json`；这只是数据运输格式资格，不是行为运行验证。
