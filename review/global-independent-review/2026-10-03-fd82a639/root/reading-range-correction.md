# 读取范围边界更正

早期独立首判中部分范围写的是工具请求上界；实际显示到文件EOF即止。后续规范化阅读表已改为实际EOF，不改变独立行为判断，也不把不存在的行计入覆盖：ExpAndMoveLearning 290→271；ShadowPokemon_Other 461→460；DayCare 566→564；EggHatching 274→268；Trading 248→243；Evolution 279→276；PokemonBag 316→301；UI_PokemonStorage 2025→2022。旧首判及已发布版本保留，实际读证以修正后的 reading-supplement.tsv 为准。引用段落中的旧请求上界不能用来推算额外行数。

补充：Messages请求819–872的显示实际止于EOF859；peer-reading-log已按实际范围更正。
