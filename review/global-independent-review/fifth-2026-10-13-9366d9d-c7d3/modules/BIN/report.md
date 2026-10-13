**BIN：RES-L05 的有限明文审查已闭合；不签 Game.exe 全部原生语义。**

固定 B5 `9366d9d17aaeac3b4414236468affa650fb3dd27`，正式根 `deliverables/final-specification-set`，正式 tree `d5a462b4c6f8b78c3264a25d6b5495230fa265e2`。固定只读 R 为 `/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials`，commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。身份沿用母任务，未重做行政核验。

请求 `gpt-6-astra / reasoning_effort=ultra / service_tier=default`，禁 Fast；实际参数回显为 **UNVERIFIED**。未调查配置、额度、认证、私有会话或后端，未创建其它会话/agent。参考、行为模型、宿主、Demo、shader 编译执行均为 **0**；运行的只有自编静态解析与产物校验。没有提交、推送、安装、下载或实现引擎。结果只写本 `modules/BIN`，临时原文只放 `/tmp/gr5-bin-readable`；正式、R、原稿、历史及他人目录未改。

先读 RES 的 [报告](../RES/report.md)、[限制](../RES/limits.json)和 `binary-interface-audit.json#/records/0/embedded_readable`，再直接读取 R/Game.exe。文件为14,732,288字节，SHA-256 `5c75e92fcbb6ec50b9f8fc61913d751a8945d6a1fc69c3017c7b8686b532bf04`；60个原长块的偏移、长度和哈希均与 RES 逐项吻合。该核对服务于提取范围，不重做版本行政审核。

| 有限范围 | 实际处置与证据 |
| --- | --- |
| 3块兼容脚本 | 偏移/长度分别为10704000/22410、10726432/23043、10749504/38461。共225个函数、988条字段访问声明；新审194函数，音频尾部31函数精确复用RES。每个构造默认值、条件、公式、资源接口及失败边界见[脚本账本](script-behavior.json)。源名称仅作审计定位，不是未来架构。 |
| 原29个长着色器候选 | **28份实际程序＋1份词典误报B52**。逐份审读函数、输入、分支、数学与常量；未把原标签当事实。 |
| 字符串补查所得程序 | 另有**27份短/单行着色器**，因此实际着色器共55份、66个函数，另5个编译前缀。见[着色器账本](shader-behavior.json)。另1段条件加载zlib的可读脚本见[短脚本账本](additional-script-behavior.json)。 |
| 原26个其它多行块 | 加入误标B52后共27块：24段词典片段、2段纯数值9/10表、1段库诊断说明。完整[数据处置](data-block-disposition.json)保留每块边界、哈希、类型和理由。 |
| 词典结构 | 邻接长度/偏移表完整覆盖122,784字节、4–24字节宽度的13,504个单元。24个长块均落在这些单元区域；HTML、脚本和uniform字样是词条片段。13个单元不是完整UTF-8，按字节片段保留，不编造程序或解码故障。 |
| 161,104条字符串候选 | 与RES两种ASCII/UTF16LE扫描完全同分母；原选284、原未选160,820，全部有偏移、长度、哈希、类型和处置引用。另检查665个短多行跨度及两组代码疑似池。见[逐候选分类](string-inventory.json)和[补查记录](candidate-search-audit.json)。这是完整类型处置，不声称每个机器码偶合串都有独立行为。 |
| 控制器映射 | RES的偏移9774912、长度442647、1678物理行/1666记录仅核身份并复用。字符串池中**另256记录**已逐字段解码；忽略platform后与RES逐序比较：102相同、151同GUID但名称/绑定不同、3新GUID；4个绑定值为空。见[新增数据](additional-controller-data.json)。不把记录数当设备数，不推定双表优先级。 |
| 字体与manifest | 可打印字体候选按已核19表SFNT容器区间归类，未扩审字体字节码。manifest的DPI aware/PerMonitorV2声明与RES一致；字体存在和DPI声明都不证明实际选择或显示。 |

程序审查不仅登记名字。[脚本账本](script-behavior.json)包含三套地图/事件/路线/数据库默认值、目标范围谓词、经验与装备公式、公式求值的局部异常回退、缓存共享/切片/清空、精灵效果与定时、16单元动画和旧天气循环。[着色器账本](shader-behavior.json)包含顺序相关自动元件区域、帧数索引先读后门、图案坐标、36采样缩放、灰度/色调/覆盖/闪光次序、零alpha混合、HSV转换、转场遮罩、图案混合/反转/草丛alpha、YUV三组系数及各平面/通道变体。原生选择和GPU精度不由这些定义反推。

已跨到23份外部可读源文件，逐范围记录于[阅读覆盖](reading-coverage.json)，并读完现行 WP13 三份、WP15、WP16 两份、WP17 两份。当前命令/路线矩阵、绘制标记附表、相关静态测试、M12 host-config合同及M10共享接口均参与反查。[source-to-spec](source-to-spec.json)给出每个脚本函数、着色器函数组、前缀和长块的映射；[spec-to-source](spec-to-source.json)给出34处有界条款反向关联。15个本地能力组只是审计索引，不替换共享Feature Matrix或扩大整体覆盖数。

交界核对得到以下处置：

- 当前外部脚本覆盖内嵌缓存加载/切图，但继承目录转发和clear。空名32×32、非空缺失异常、动画包装回退及资源有效期与 WP15 现行合同相容。clear丢弃缓存索引并请求GC，不证明同步销毁全部外部资源。
- 当前外部精灵动画采用运行时间、默认20fps及多请求上下文；旧内嵌偶数帧推进和单动画替换不能覆盖 WP16。重复屏幕请求的空槽坐标失败已属于 **GR5-M10-013**，父坐标末尾偏移属于 **GR5-M10-012**；本次关联证据，不重复编号或替别人签字。
- 内嵌旧天气创建40槽却从1开始遍历，最多更新39个实际槽；当前天气全部同名方法已被外部覆盖，采用60粒子、注册数据和阶段渐变。旧39槽不构成现行天气错误。
- B11/B12的四层地图、标准RPG参数/经验/范围规则，以及背景字段不一致、兼容敌队构造引用本块未定义名称等，均保留定义级事实。当前调用和版本选择未证，不能变成宝可梦战斗要求。
- 当前音频先走系统登记/选项/文件门，缺系统才可能选兼容包装或直接Audio。精确复用的音频尾部为B11行872–968、B12行919–1004、B13行1466–1476；没有重复全文或混成唯一宿主规则。
- 当前图块动画由可读地图渲染代码编排，不能直接套内嵌七自动元件shader的索引与除法边界。普通宿主过渡和脚本具名过渡也分列；明文vague除零不等于已经证明外层过渡失败。
- 输入别名、F8、鼠标窗口守卫和字体存在性调用均有外部消费者。控制器表、字体名字和错误消息不补出实际键位、死区、重复延迟、Font.exist?结果或字宽。

**新增候选仅1项：GR5-BIN-001，P3，optional，待独立反证。** 建议把新取得的颜色/位图运算定义整理为有界宿主静态附录；这属于范围扩充，**没有认定现行正文矛盾，也没有自签必修**。[完整用户schema](findings.json)包括source/spec锚点、前提、正常/反向/边界场景、顺序与数学、negative search、影响、建议、验收、历史、执行和未知。实际反查与零命中词法辅助见[negative-search](negative-search.json)。现有范围声明作为反证约束保留。

未解除的具名未知为：原生版本/后端选择；shader源码长度与前缀拼接、uniform归一化及纹理绑定；GPU精度、采样、钳制和实际画面；双控制器表的注册/优先级及空绑定语义；原生字体/音频/输入结果。机器码、CRT、完整第三方库与字体字节码不在有限明文任务内。以上是准确的证明边界，**实际阻塞0、分配明文未审区间0**，没有把可读未审伪装成缺材料；无需继续追逐所有native入口。

全部JSON、字节锚点、候选分母、函数覆盖、词典/控制器数据以及双向映射的一致性由[校验记录](artifact-validation.json)登记。校验仅证明取证和产物结构，不是运行行为验收。[progress.json](progress.json)的`complete`为布尔值，有限范围完成后置true；未修改RES原限制记录或共享关闭登记。

复现使用本目录[extract_candidates.py](extract_candidates.py) → [build_script_ledger.py](build_script_ledger.py) → [build_shader_ledger.py](build_shader_ledger.py) → [classify_candidates.py](classify_candidates.py) → [build_review.py](build_review.py) → [build_findings.py](build_findings.py) → [validate_artifacts.py](validate_artifacts.py)。这些只安全读取固定R和现有证据，产物限BIN、原文限/tmp；不导入或执行参考程序。
