# candidate-v2 有限身份增量核验

结论：PASS_LIMITED_IDENTITY_DELTA_ONLY。候选 d7875398e130b5bfa621c55d6c016ee0f8965cf7 / tree 8c763de4279e5140e64cd0a9fe58a820ea2cb92b 与发布后继 165b01ce06ff88e5c5f50df7a11d017417ed1213 身份一致，后继只新增发布回执。

正式C1→C2恰好2文件、2新增/2删除，只改变R4-PD05第220行与R4-DX05第785行的前提单元格；输出与NOT_EXECUTED列完整bytes不变。其余10批准文件及全131正式集的129未改文件完整bytes保持，2文件其余行完整bytes保持；全131当前候选/发布/工作树完整bytes相等。

v2完整46镜像中仅PD05/DX05两个full_row字段改变，其余44完整对象不变，全部位置/行匹配新候选，均为未执行静态设计。原作者execution.json在C1/E1/C2/E2/工作树完整bytes一致，原4历史调用与例外资格按原证据引用复用，未rerun。

原29标准PASS与标准6的旧规则/反向限定证据仅引用固定独立报告 0bdfd26ef95ced597db5d924a69d0e35de9a188b，没有重签旧全域或重新计算23/229/341；修正后的标准6语义满足由根审者另决。本子审新增参考/模型/宿主/Demo行为执行0，NOT_EXECUTED_THIS_UPDATE。

真实thread 01a130e1-9768-7067-99d9-c5b20c2bb015，请求sol/ultra/default/Fast=false，实际echo UNVERIFIED。只写本json/md，未改author/正式/参考/登记，未提交推送、接受或关闭依赖。无身份增量阻断。必要身份与分组实际读取记录见JSON。
