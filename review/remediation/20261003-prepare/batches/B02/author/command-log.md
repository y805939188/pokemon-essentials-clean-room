# A-B02 操作与证据记录

仅记录当前执行环境的实际动作；命令输出里的源码只用于静态读取，不复制到正文。原计划/全局review/批准台账均未写入。

1. 等待选定执行环境就绪；初始提供checkout只作身份检查，没有当交接使用、没有编辑。
2. `/workspace/remediation-b02-20261003-prepare` 独立 Git 初始化、配置主项目origin、fetch精确交接 SHA，checkout `remediation/20261003-prepare/batch-B02`；起始SHA/tree/clean核验。
3. 读 `AGENTS.md`，以 `rg --files` 在当前项目及挂载 `.agents`/`.codex` 搜索相关 `SKILL.md`，未发现适用本仓的本地技能文件；没有读取身份凭证或会话配置。
4. 从Git固定对象获取原全局findings、批准批次/验收对象；完整核本批B02.md/JSON、12对象current_qualifications/二审/扩展。读取stage-locks JSON及physical/semantic/shared-premise TSV的相关门与完整输入结构；原冻结文件保持字节。
5. 核B01被审整合→交接仅报告/登记差异，并读实际report/downstream-freeze与导航勘误；A006旧原稿仍是待修目标。B02/B05正式集合交集为0。
6. `/workspace/pokemon-essentials-reference-b02` 独立Git init、fetch --no-tags --depth=1固定参考、checkout --detach；HEAD/tree/status核验。此后只用 `nl`/`sed`/`rg` 原始文本读取及Git blob/原始字节身份核验；实际行范围见source-reading-log。
7. 只写七份许可正式文件与本author目录；原规格六路径建议先登记scope-conflicts，未自动扩围。公共audit八处旧路径/正确路径存在性逐项核验，建议交A-REG。
8. Python仅用于**本项目review JSON**抽取、作者报告/清单和文本/哈希/差异自检；没有解码或执行参考二进制、游戏脚本、编译器、转换器，也没有计算/运行参考静态向量。
9. 冻结前核git diff --check、七文件/作者范围、所有EP段字节、未授权/历史原字节、ID/严重度/别名、静态表数量与源身份；详细结果见validation-results。候选提交/推送及远端精确SHA另记发布回执。

所有“通过”仅指作者文件/身份/差异检查。请求模型参数按用户委派保留，实际有效仍UNVERIFIED。作者任务无子代理；没有main/force/integration操作。
