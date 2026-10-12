# GR3-U06 作者候选交付

状态：**CANDIDATE**。本批仅 GR3-M12-001、GR3-M12-002 两项作者事实修订完成；不是全轮23项完成、独立PASS、正式接受或CLOSED。全部行为／静态案例 NOT_EXECUTED。

## 固定身份与角色

- 管理：`d0371f693f4a0dc713ee5cc6e43a20ff465269a8` / tree `0e217b059c1350b6c4ca93b29ad86fae75b48a54`。
- 分支：`codex/gr3-u06-author-20261012`，由精确管理版本新建；未在共享checkout中切换其他作者分支。
- 交接 H：`d5b6af3ebbabc57ed7fbdc2e1fb2c4736dbf9a65` / tree `c8a523150d75c8d1bede346857263ddd00ef0035`。
- 正式 D：`86b4d7e1d8645e75af91a215240f8786a5bb4ca8` / tree `42c29efb5422772a1d90f657f25983600f500f28`。
- 只读参考 R：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，在本执行器新获取并验身份的 `/workspace/pokemon-essentials-reference-fixed`；未假设准备环境路径可复用。
- 候选正文 payload commit：`b7cf57c4ea3b9072982722f08b4f462e976e0fe4` / tree `ab83f9495743f2def57c2315e904d39649f22917`。这一提交仅包含三份完整镜像；本报告与manifest随下一次作者附属提交交付。最终包含全部产物的精确commit/tree由实际远端读回后在外部交付答复返回，避免文档自身commit哈希循环。
- 根AGENTS已读；固定管理版本和当前环境无适用`.agents/skills`。模型请求 gpt-6.1-sol/xhigh/default已接纳；模型、推理和速度实际回显均UNVERIFIED，见model-request-receipt.json。不查额度，不启动CLI模型、隐藏任务或作者自己的独立review。

## 修订结果与逐项检查

| 项目 | 实际候选条款与案例 | 作者事实自检及保留限制 |
| --- | --- | --- |
| GR3-M12-001 | WP75 §13.2/§13.3/§16-8/§17；目录CV-M30 | 两个根目录BMP分别列路径、用途、246字节、8×8头部和SHA256；默认区域底图及Graphics仍缺失。仅静态可得性，不承诺浏览器加载/解码/外观、完整页面、宿主或Demo通过。 |
| GR3-M12-002 | WP76 §2/§6.4/§7.4/§7.4a/§11；目录GN-M14/GN-M20 | 区分已结算C、待结算h、可见C+h；70＋12成功后82/0/可见82，238＋12后250，退休要求评分70/至少2成员/排序后下标<600及前三支不命中。跨轮只累计新增；空历史增量0；清历史前失败不承诺评级全字段回滚。 |

完整前提、正常/失败/边界、验收标准逐项对应、保留unknown与实际行定位见author-self-check.json；来源精确R文件blob/SHA256/bytes及实际阅读范围见traceability-proposal.json。没有按源码结构翻译、复制源表达式或设计新框架/API。

## 有界自检证据

- 三份镜像从固定H完整复制；逐文件base/new blob、SHA256、字节数在candidate-identities.json。H与D及管理版本的对应正式字节一致。
- 固定输入身份核验：12核心文件、5正式读取文件、5参考文件、4模块限定输入均匹配冻结blob/SHA256/bytes。身份核对不计语义全读或行为覆盖。
- 正式131份文件逐字节保持D/H原值；参考工作树无改动；旧报告、其他批目录、公共登记、reference/、main无作者提交变化。
- DX目录只改CV-M30、GN-M14、GN-M20；其它211条具名行逐字保持，未增删案例ID。WP75§5.5页条件、§7.2a跟随链及WP76活动评级数学/空历史偏差条款逐字保持。
- 派发10个旧控制、全部精确贡献tuple与qualified范围保留；仅验证本候选未改相关条款/行，不转移历史PASS。原229/341完整资格引用不重新全局复审。D012为PP4/−10/C41不同前提，不重开。
- M09有限接口联验只读WP55§2.1、WP57§1.3/§8/§9；生成器队伍场次不是会话胜场/交换计数，无消费者文件改写或新全域设施签署。
- candidate.patch为三个正式路径的完整差异，47678字节，SHA256 `775eee686fa8bea2a1acd8b84ba2ffde0fba9ce272eb127c240a09f34344d869`；`git apply --check --whitespace=error`返回0，未apply正式目录。初次目录检查解析器误把重复ID表头当案例ID，排除表头后去重重试一次，候选/补丁未因此改变。另处理嵌入补丁的14条空白上下文空格，以标准suppressBlankEmpty式抑制空格前缀后重核apply --check返回0；候选正文未改。
- 参考/Ruby/游戏/浏览器工具、行为案例、静态案例、运行观察、已证明真实Demo链全部0。仅文件、头部、JSON、文字与补丁适用性检查有执行，不能当游戏行为PASS。

## 交付与未决

本作者写入范围为三候选镜像及七附属路径：author-report.md、author-self-check.json、candidate-identities.json、candidate.patch、traceability-proposal.json、registration-proposal.json、model-request-receipt.json。公共表只给提案；其中source-traceability的旧“区域地图生成素材缺失”行须由唯一整合员在真正接受新字节后有界更新，未越权直接修改。

无作者材料/写范围阻塞。下一步由父任务指定独立ultra reviewer复核最终作者commit/tree和manifest；接受后仍须唯一整合员核base，实际应用、独立实际整合复审及登记。未来bug保留/兼容模式/现代行为、产品尺寸/视觉范围、缺资源补交和真实运行仍UNDECIDED，不阻塞本批事实补文；U08未启动，M02-003不重开。

正常推送与远端实际读回在附属提交完成后进行；其精确结果以最终交付答复为准，本报告不预签成功。
