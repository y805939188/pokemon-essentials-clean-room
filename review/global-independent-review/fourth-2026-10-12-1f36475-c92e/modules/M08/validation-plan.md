# 产物结构验证计划

目的：验证本模块JSON可解析、必需字段存在、能力ID唯一、正式文件清单为131、本域正文/附表/测试均已登记、所引用源路径/规格路径存在。此验证不判断行为正确，也不运行参考或数学模型。

命令：`python3 review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/M08/validate-artifacts.py`。版本由同一驱动读取 `python3 --version` 并写 execution.json。

输入：本模块JSON、已固定B的正式文件名与R参考文件名。预期：全部结构断言通过、exitcode=0。区分点：遗漏字段/断链/越界文件清单应失败；没有失败不升级静态语义支持为运行通过。

副作用：验证本身只读；外层记录仅写本M08 execution.json及validation-result.json。无参考/正式文件/存档/网络写入。
