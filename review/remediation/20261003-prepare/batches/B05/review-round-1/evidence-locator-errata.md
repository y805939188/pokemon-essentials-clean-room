# 冻结首判证据定位勘误

发布校验发现首判证据目录的一处相邻文件名误记，以及若干读取区间的末端超过实际文件末尾。首判两文件保持冻结字节；本后继材料修正定位，未改变任何候选字节、逐ID前提、静态反例结果或PASS_SCOPED结论。没有新增候选缺陷。

所有正确定位均属于固定参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。

| 首判定位 | 正确可回查定位 |
| --- | --- |
| S19误写 `019_Utilities/002_Utilities_Pokemon.rb:450–490` | TR教学包装器在 `Data/Scripts/019_Utilities/001_Utilities.rb:450–490`，实际登记函数从452开始，成功后首招记录接点在479。发布校验再次直接读取该范围，与独立判断的成功/拒绝/记录门一致。 |
| S01 Nature 30–176 | `Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb:30–173`，173为文件末尾，25行身份/修正表无变化。 |
| S04 Pokemon 到1228 | `Data/Scripts/014_Pokemon/001_Pokemon.rb` 文件末尾为1227；创建段到1227。 |
| S11 Move 1–125 | `Data/Scripts/014_Pokemon/004_Pokemon_Move.rb:1–77` 为实际全文；读取请求1–125只返回这77行。 |
| S21 Summary 1380–1410 | `Data/Scripts/016_UI/006_UI_Summary.rb:1380–1400`，1400为文件末尾。 |

[源阅读日志](source-reading-log.json) 已以实际路径和有界区间保存，并另保留原读取请求区间。源码内容没有复制到本勘误。冻结散列继续满足 [首阶段冻结](first-phase-freeze.json)；定位修正是独立证据发布校验的补充，不重写先于作者比较的首判。
