# 资料格式只读检查计划

目的：确认本机knownpoint/selpoint BMP的格式头、现有编译数据与工具的文件类型，以及实际资源缺项。输入为已固定R及本地清单。使用Python标准库读取BMP头、JSON配置及file命令识别文件，不加载游戏、不反序列化游戏对象、不解码媒体像素。输出仅本轮evidence/material-validation.json；所有输入只读，无网络或外部账户副作用。该证据类别仅TOOL_VALIDATION，不能用于宣称渲染、宿主或Demo通过。
