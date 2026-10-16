# 精确载荷恢复与用途

`exact-payload-bytes.json.gz`包含64个原始/强制后继及8个适用指令/后继伴件的原始字节。每条base64解码后按同条mode/blob/bytes/SHA256核验；commit/tree/path是其冻结来源，不是本包自身身份。`preserve_payload_bytes.py`可从已核固定Git对象重建。`verify_remote_publication.py`对隔离网络克隆的每个压缩附件核完整恢复后字节，并对72条原始载荷逐条恢复核验。

`exact-inputs.json.gz`与`typed-input-graph.json`是完整JSON语义结构及精确值去重图，保留字段、列表顺序和当前/旧版本关系；它们不保存原JSON排版，原字节以上述base64包为准。图的完整恢复见`validate_package.py`的decode。`exact-additional-inputs.json.gz`的content是完整原文本。`received-root-records.json.gz`保留完整root裁决结构。`reading-projections.json.gz`保留实际阅读投影及后继窄窗补读，不是独立裁决或新的完整source覆盖证明。

解压、哈希、结构恢复、路径核等与脚本成功只授工具/传输证据，不授语义阅读、非作者验收或行为执行信用。参考代码只保留在审计输入，不能进入后续净化规格。
