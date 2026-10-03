#!/usr/bin/env python3
"""WP02 逐定义配置清单：控制台清单程序（独立复核用）。

与 wp02_build_appendix.py 共用 wp02_settings_common.py 的解析/求值逻辑；
本程序只向 stdout 输出统计与逐定义行，不生成 Markdown 附表。
只读解析固定基线，不修改 reference；未求值项显式报告。
"""
from collections import Counter
from wp02_settings_common import FILES, parse_settings

constants, methods, meta, unevaluated = parse_settings(gen=8)

c1 = [r for r in constants if r[0] == FILES[0]]
c2 = [r for r in constants if r[0] == FILES[1]]
gen1 = [r for r in c1 if r[3].startswith("世代")]
gen2 = [r for r in c2 if r[3].startswith("世代")]
sd = [r for r in constants if r[3].startswith("设置间")]
thr = dict(sorted(Counter(r[3] for r in constants if r[3].startswith("世代")).items()))

print(f"001 Settings constants: {len(c1)} (gen-derived {len(gen1)})")
print(f"002 Settings constants: {len(c2)} (gen-derived {len(gen2)})")
print(f"total Settings constants: {len(constants)} "
      f"(gen-derived {len(gen1)+len(gen2)}, setting-derived {len(sd)})")
print(f"method-type: {[m[2] for m in methods]}")
print(f"Essentials metadata: {[(m[2], m[3]) for m in meta]}")
print("threshold groups:", thr)
print(f"unevaluated: {unevaluated if unevaluated else '无（全部求值）'}")
print()
print("file|line|name|derivation|gen8_value|value_status")
for r in constants:
    print("|".join([r[0], str(r[1]), r[2], r[3], r[4], r[5]]))
