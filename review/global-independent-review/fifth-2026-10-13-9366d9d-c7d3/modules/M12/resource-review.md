# 主会话资源补充审查

固定R中的两个BMP已检查全部8×8像素；八份字体已检查SFNT结构、Unicode映射/度量并查看全部映射字符预览。它们不证明原生宿主字体选择、hinting、游戏画面或区域地图工具实际呈现。

音色库按[E-mu格式原始文档](https://www.synthfont.com/SFSPEC21.PDF)解析全部记录和样本范围。236预设、240乐器、505样本及1524链接已登记；bank0含0–127全程序。42处名义参数范围观察和样本尾保护区差异保留，不能以索引检查无错误推完整格式合规或播放正常。mkxp配置明确选择此文件；实际宿主接受、合成音色和异常处理未知。格式文档只是解析依据，不替代R实际行为，也不要求新引擎采用该合成器。

Game.exe、两DLL、animmaker.exe、extendtext.exe仅完成容器/依赖检查；未反编译完整native/managed行为、未执行。Data/Scripts.rxdata已安全解析到唯一Main装载内容并与两个脚本工具的嵌入装载文本同字节对照；未启动游戏或执行装载器。

本轮新参考执行仍为2条编译器局部记录；上述解析、字体预览不计EXECUTED_REFERENCE或EXECUTED_HOST_OR_DEMO。
