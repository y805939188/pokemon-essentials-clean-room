# R4-U03 candidate-v2 有限返修

状态 AUTHOR_READY_FOR_LIMITED_INDEPENDENT_RECHECK；只回应 R4-U03-REVIEW-001 / GR4-M11-001 标准6，不自签独立PASS，不登记实际接受或关闭。

仅更改两个正式测试目录的R4-PD05、R4-DX05各一行输入前提：默认RATTATA、显示全部关闭、基础雄性0与具名且展示自身的Alolan雄性1均已见（可仅异色），初始[0,1]确在可列列表。预期[0,1,false]、普通刷新保留true、单项BULBASAUR不写及NOT_EXECUTED标记原样保留。精确差异见formal-diff.patch。

必要固定R静态核对支持：正向匹配首轮[0,1,false]；仅雌Alolan已见且雄性末次不可列的独立反向仍回基础雄性首项[0,0,false]；普通刷新与单项对照保持。完整前提、推导和旧PD31/PD34/B38保护证明见criterion-6-response.json及correction-and-verification.json。没有执行参考函数、行为模型、UI或写真实记录。

本目录derived-vectors.json为candidate-v2的完整46项镜像：仅两项输入行同步，剩44项原样复用。上级author目录的v1证据保持冻结，绑定原候选58cd8b1；对新候选只使用本目录新镜像/身份。复审原29条PASS保留原报告0bdfd26的限定身份，不改成新的v2PASS；其余10正式文件完整字节未变，未重做全球/历史审查。源/模型/宿主新增执行0，原第四review4次限定历史回执身份保持，媒体/输入/像素未知。

复审入口：本目录author-report.md、criterion-6-response.json、formal-diff.patch及后继candidate-publication.json。父任务复用原独立reviewer安排有限复验；模型回显UNVERIFIED。发布候选及精确tree在后继回执绑定，避免自嵌候选hash。
