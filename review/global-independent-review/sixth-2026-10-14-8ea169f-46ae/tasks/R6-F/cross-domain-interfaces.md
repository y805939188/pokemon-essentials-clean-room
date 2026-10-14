接口接合记录（独立阅读，不替代其它主审）

- 核心C：Battle_Clauses 306行全读；单场包装144行全读；Tower/Palace/Arena记录种类，内部战斗false，通用准备209–304完整单元可覆盖尺寸；决定码由核心终局负责，设施只布尔返回/统计。条款精准消费者和已知OHKO alias加载差异沿WP54§6，未重复mandatory根因。
- UI：报名完整单元1051–1139和BattleSwap247行全读；人数0加入门提案GR6-F-002；完整Summary/Scene演出由UI primary，本域只保静态命令与提交顺序。
- K/Creature：Pokemon级/EXP写入口、完整治疗、重算/构造及Owner完整文件新读；工厂空trainer为默认属主，EV除项数、固定IV、个体号重摇；两侧原EXP/item按位置恢复。完整个体/成长曲线仍K primary。
- DX/Compiler：compile_trainer_lists951–1022、compile_battle_tower_trainers1024–1063、write_trainer_lists511–529、write_battle_tower_trainers534–568、write_battle_tower_pokemon573–619完整相关单元新读。表字段逐项映射见data-field-consumer-matrix.json。生成器4文件与Debug必要入口交generator子域；不得以默认表存在签consumer。
- D：PBS73全结构由D primary。R6-F新读battle_facility_lists25行并绑定实际默认/四杯声明；逐行consumer兼容性census由generator，Gen5备份目录只限所需标识兼容输入，既不自动被装载也不签备份整个语义。
- 保存：全局metadata challenge/lastbattle懒建与初始化、global_metadata登记、SaveData82行全文、Game.save111–124完整单元。隔离Game.save为只记内存请求，未调用真实保存本体。
- 共享测试目录：三篇全文呈现/阅读；本域QC/WS/PA/RC/FC/SF逐项来源审查。EG/EN/MG/TT/BP/FP/PD/VF/LT等余域只审核前提与设施/捕虫接点，记录cross-domain依赖，不对其全部实现签PASS；root对对应primary矩阵裁决。
