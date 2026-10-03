# RUN-C-013：总审控制流疑点的更正

原 root/language-semantics-review-note.md 将非局部退出按 return 的包围方法寿命讨论。回读固定源并收到A在揭示首轮结论前保存的独立判断后，确认实际控制词是 **break**；原疑点使用了不适用的语义前提。原记录保留，不作为当前裁决依据。

固定参考 Debug_MenuCommands:1076–1099 将普通闭包作为值创建、存入菜单登记；单角色分支先显示消息，随后请求退出创建该块的调用。创建调用已完成后，效果才经 HandlerHash 原样存储和 MenuHandlers 延后调用。正常菜单调用点没有此处的异常捕获。该顺序无需知道更外层加载方法是否仍存活。

[官方 Ruby 3.1 Proc 说明](https://docs.ruby-lang.org/en/3.1/Proc.html#class-Proc-label-Lambda+and+non-lambda+semantics)区分两种退出目标；普通闭包的 break 在其创建调用已经返回后发生，会产生 LocalJumpError。这里采用固定参考的常规语言语义，未运行文档示例、参考或自建模拟器，未解包Scripts.rxdata。未见语言改写不被假设为存在；未知宿主的最终错误画面、最外层捕获和进程是否退出仍不作运行断言。

当前裁决：**RUN-C-013 / P2 / CONFIRMED_REQUIRED_REVISION（具名静态语言条件）**。需要记录提示已显示、角色未改、选择列表未打开及错误向本菜单调用层传播，不能概括为安全返回。A的第一判断与其后比较报告独立保存；本更正不是对原C报告的静默改写。

项目基线e1e01bb18d824931e54f182dd61af5a9f908ba85；参考8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。额外直接核对：Debug_Menus:127–145；Event_HandlerCollections:80–86,118–123；Event_Handlers:97–112。官方语言文档是辅助语义证据，不代表宿主版本或运行验证。
