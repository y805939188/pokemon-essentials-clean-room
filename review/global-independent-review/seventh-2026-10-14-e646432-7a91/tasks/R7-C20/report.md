# C20 有限发布工具静态复核

三脚本的已报缺陷均已在根修订中静态解决；本次检查范围内没有剩余阻断。不签全局PASS，也未调用发布、远端或启动流程。

最终精确输入：

| 脚本 | SHA256 |
| --- | --- |
| build_root_package.py | e8354e36fcbbc90f24c9efb3df3725354e6df9c2a5b1c7935c7b7dff5c4c68ec |
| manual_launch.py | 7702acfbf7f00f2fb9637babd5db6e20d3df15ff9b2319950e171504515148ff |
| remote_readback.py | 49af54d1cced79680d84a1bd7a5f63a1ede7dc6d41e6f6442399a47df3d75673 |

最初renderer把core索引与工作区正文混用；修订后approval、正文、JSON、26份prompt和CLI输入均从完整core SHA的实际gzip树成员恢复，并核encoded/decoded的bytes、SHA和content-blob。C0/C1/C2身份分层及不自包含package index保持；实际生产core/C1/C2仍由根另行绑定。

启动器现只把同一次读取且比对package-members身份的data传给stdin，日志解析后必须留在准确候选execution目录。无--launch只打印请求，不自动启动update。未来cloud路径明确UNVERIFIED，使用者须手动绑定实际project/package；请求模型配置不冒充实际回显。没有改main/tag、源checkout或自动推送逻辑。未来agent的候选写集仍依授权和提示合同，不把workspace-write夸成系统级reference只读隔离。

远端脚本原先对带点输出名使用with_suffix，导致命令日志相互覆盖；现在独占新.commands目录、追加后缀并拒绝覆盖。cat-file验证异常现会terminate/wait，必要时kill/wait，保存真实exit和已验证前缀。Git子进程现清除具名目录/对象/alternate/config注入环境，fetch后核不存在alternates文件，才记录object_alternates_used=False。

静态核查确认：37条root/canonical/中文对象按完整core对象嵌入，两个optional导航facet单列；当前root图从core读取，P03只贡献原批入口。现有P03输入恰有26个唯一入口及26个匹配prompt，13 author/13 reviewer，后缀与角色一致。所有最终脚本AST解析通过。远端算法遍历每个物理blob并核身份，再完整gzip读取并对每个logical成员核decoded身份；这不是本次已完成远端读回的声明。

详细缺陷/修正关系、精确读取收据和边界见 publication-tools-static-review.json、current-input-identities.json、finite-checks.json 与 logs/。初版和过渡版本保留；只写本任务目录，未修改根脚本或原材料。

真实限制：本C20未运行publisher/launcher/remote_readback，未调用Git、网络、agent或update，也未执行reference/native/行为模型。根另述的fixture结果未在本任务独立核完整收据，不作本审者运行证据。新assemble_root_core不在本次范围。实际模型配置UNVERIFIED，无额度/认证探测。UPDATE_NOT_STARTED。
