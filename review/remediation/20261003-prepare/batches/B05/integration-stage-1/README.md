# B05-G 实际整合受影响核验交接

**INTEGRATED_PENDING_ULTRA**。本目录是A-REG登记送审材料。完整候选 `1914cd379bcb7c8b6feb13dc3e872b7ded27d9a4`的R-B05报告 `0da269077aa5a02d5cef08021171acf3719e1b69`给出16项贡献PASS_SCOPED，十主责/六协作；报告SHA不是被审候选或本次实际integration SHA。本次公共新字节及最终新SHA须同一R-B05作Ultra受影响核验。

## 固定输入与完整保留

B02接受起点 `9576f00e7d3aeb96f7ca8c42caccfba8f808505e`，对应实际被审 `1b1e169faf273e89ad6b7f5e46fd7b60d87d3946`和Ultra报告 `361e4e69126559c266a08fdf093082dbbcd83f8d`。B05旧作者起点 `0a12de641542f9a59909d2a950c1de8df17ca09d`、v1 `7dc7dd5dfc986788fd6d9ce7b2bdaa6208837b4e`、完整v2 `1914cd379bcb7c8b6feb13dc3e872b7ded27d9a4`与直接后继报告 `0da269077aa5a02d5cef08021171acf3719e1b69`完整合并；[合并独立性](merge-independence.json)列三提交全路径与双向读集合比较、正常merge身份。66来源路径与B02接受链路径无交集，冻结B05正式读集合与B02更改无交集，十五正式写文件与B02读集合无交集。正常无冲突合并，未discard/ours/theirs。

十五正式文件（十净化正文/附表/静态目录＋五已授权原稿）原字节保留；33作者记录、2授权记录、16独立报告记录均原样接入。五原稿批准条款见 [原授权](../scope-amendment/approval.json)及 [manifest](integration-manifest.json)。新旧文件身份、独立候选身份与本次公共待审身份分列，不借旧Reviewed或旧批准覆盖新hash。WP18 §8旧句和批准§9/Nature缓存限定、正确原Mega/Shadow表和原h255/G0保持。

原完整finding对象和计划最小验收分别与固定原报告 `93e10babe0b9c9ef8b3f5277754541b447beeeb4`、批准计划 `41fffb540c6483f5296ea0d33b789b75180d27ed`逐项相等；所有原字段仍在冻结author输入与规范报告，哈希/raw_id/责任/有效case在 [逐ID登记](finding-registration.json)绑定。A022为当前统一P2；A020/A026/A044扩展及C124/C126有效case不收窄。原规范ID均OPEN，规范229必修与42贡献行分开计数。中央finding-ledger原字节不改，approval/trace旧26行不改，只追加16个B05待审贡献；B01/B02旧manifest/hash/审查/接受/PRE0/计划及整个中央旧交接不回填。

## 公共登记与尚待验收

audit/coverage/Feature/勘误新增限定后继，保留整个历史正文；README/scope说明B02已接受与B05待审，测试索引仅更新本批两行。独立源定位以 [既有定位勘误](../review-round-1/evidence-locator-errata.md)和源日志为准，不改冻结首判或提升读取/运行证据。当前所有受影响公共hash见 [current-hashes.tsv](current-hashes.tsv)。

两个目录当前164/213，共377行，相对B02接受基线新增38；仅旧FM15/FM20/SH06改动，无删除。PT/PS/AQ与BR整个尾段原字节保持，B01/B02目录99+51不变；131最终Markdown、17静态目录文件数不变。[scope-counts.json](scope-counts.json)区分文本清单、既有R-B05数据审查与作者自检数量，均不作行为向量执行数。

A020/A024/A026仍有B07；A040有B07/B17；A044有B07/B16；C124/C126有B16。所有逐ID候选局部判定、原/净化/测试映射、原批准界限与剩余责任按原独立报告和作者v2登记建议保留。B05实际整合未审，B06/B07/B08/B10/B15/B19/B21等依赖门不自动开放；最终关闭需各贡献与最终Ultra。

B03只消费已交接的 `9576f00e7d3aeb96f7ca8c42caccfba8f808505e`冻结输入及原七写路径/共享整文件锁，本作业不派发或替换冻结。本次公共audit/README与其旧读集合有交集，不能声称B03在新SHA全读集合不变；正式写路径无交集，相关差别具名在合并独立性材料。

## 精确新SHA与完整差异

先提交公共payload，再仅新增 [upstream-to-payload.patch](upstream-to-payload.patch)、[candidate-to-payload.patch](candidate-to-payload.patch)及 [diff-and-freeze.json](diff-and-freeze.json)。两patch覆盖B02接受起点→payload与B05候选→payload全部路径，无排除；证据后继只增加三文件，十五正式/公共payload及原报告原字节不动。最终实际SHA由普通push/远端回读给出，完整最终差异可用 `git diff 9576f00e7d3aeb96f7ca8c42caccfba8f808505e <actual-integration-SHA>`及 `git diff 1914cd379bcb7c8b6feb13dc3e872b7ded27d9a4 <actual-integration-SHA>`重建。有限证据链避免自引用patch/提交hash。

R-B05须核精确新SHA的十五正式字节、五原稿授权边界、B01/B02输入保护、全部来源提交与差异、两个共享目录、公共层/链接/身份/计数、229OPEN/跨批剩余；不得仅凭候选PASS或文件hash宣布本次公共语义通过。[validation-results.json](validation-results.json)只记A-REG自己的Git/JSON/文本结构核验，不代替独立Ultra。

作者请求gpt-6.1-sol Max/Standard，独立复审要求Ultra/Standard；实际三项UNVERIFIED，未fallback/改配置。固定参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`只读；未执行作者/复审脚本、参考程序、游戏、编译、转换、生成、反序列化、模拟或求解，行为向量/运行观察/真实Demo均0。U01–U10/G01–G12/AX01–AX20及素材/宿主/插件/可选启用未知保留。普通push并回读最终SHA后停止，等待父任务安排R-B05实际复审。
