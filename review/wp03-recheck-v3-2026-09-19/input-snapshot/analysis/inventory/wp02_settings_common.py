#!/usr/bin/env python3
"""WP02 共享解析模块：设置文件只读解析与有限求值。

供 wp02_settings_inventory.py（控制台清单程序）与
wp02_build_appendix.py（Markdown 附表生成器）共同使用，避免重复解析漂移。

求值器只覆盖固定基线两个设置文件中实际出现的有限表达式形式：
- (MECHANICS_GENERATION <op> <int>) 及其 || 复合
- 上述条件的三元 (cond) ? a : b
- 字面量（整数、布尔、字符串、简单整数乘积、数组/哈希起始符）
- 设置间引用（= 另一设置名，单级解析）
不执行任意源码表达式（不使用 eval 处理条件）；无法解析时显式报告"未求值"及原因。
"""
import re
from pathlib import Path

R = Path("/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/Data/Scripts")
PBS = Path("/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials/PBS")
FILES = ["001_Settings.rb", "002_BattleSettings.rb"]

const_re = re.compile(r"^\s*([A-Z][A-Z0-9_]*)\s*=\s*(.+?)\s*$")
method_re = re.compile(r"^\s*def self\.(\w+)")
comment_strip = re.compile(r"#.*$")

# GameData 声明的 19 个基名（010_Data 各文件 PBS_BASE_FILENAME，Species 含 2 个）
# 加编译器合并的 3 个（battle_facility_lists、map_connections、regional_dexes）
PBS_BASE_NAMES = [
    "battle_facility_lists", "dungeon_parameters", "dungeon_tilesets",
    "map_connections", "map_metadata", "metadata", "pokemon_metrics",
    "pokemon_forms", "pokemon", "regional_dexes", "shadow_pokemon",
    "trainer_types", "trainers", "abilities", "berry_plants", "encounters",
    "ribbons", "town_map", "types", "moves", "items", "phone",
]

_OPS = {
    ">=": lambda a, b: a >= b,
    "<=": lambda a, b: a <= b,
    "==": lambda a, b: a == b,
    ">": lambda a, b: a > b,
    "<": lambda a, b: a < b,
}


def _eval_condition(cond: str, gen: int):
    """求值世代条件；返回 True/False，无法解析返回 None。
    覆盖：MECHANICS_GENERATION <op> <int>，及两个此类条件的 || 复合（可带外层括号）。"""
    cond = cond.strip()
    if cond.startswith("(") and cond.endswith(")"):
        cond = cond[1:-1].strip()
    parts = [p.strip() for p in cond.split("||")]
    results = []
    for p in parts:
        m = re.fullmatch(r"MECHANICS_GENERATION\s*(>=|<=|==|>|<)\s*(\d+)", p)
        if not m:
            return None
        results.append(_OPS[m.group(1)](gen, int(m.group(2))))
    return any(results)


def eval_setting(rhs: str, gen: int, resolved: dict):
    """对单条设置的右值求世代 gen 下的默认值。
    返回 (value, status)：status 为 "求值"、"跟随 <设置名>" 或 "未求值：<原因>"。"""
    rhs = comment_strip.sub("", rhs).strip()
    if "MECHANICS_GENERATION" in rhs:
        m = re.match(r"^\(?(.+?)\)?\s*\?\s*([^:]+?)\s*:\s*(.+)$", rhs)
        if m:
            cond_val = _eval_condition(m.group(1), gen)
            if cond_val is None:
                return ("未求值", f"未求值：条件无法解析 {m.group(1)}")
            return (m.group(2).strip() if cond_val else m.group(3).strip(), "求值")
        val = _eval_condition(rhs, gen)
        if val is None:
            return ("未求值", f"未求值：表达式无法解析 {rhs}")
        return ("true" if val else "false", "求值")
    if rhs in resolved:
        val, status = resolved[rhs]
        if status == "求值":
            return (val, f"跟随 {rhs}")
        return ("未求值", f"未求值：引用项 {rhs} 亦未求值（{status}）")
    if re.fullmatch(r"\d+\s*[*+\-/]\s*[\d\s*+\-/()]*\d", rhs):
        try:
            return (f"{rhs}（= {eval(rhs)}）", "求值")
        except Exception:
            return ("未求值", f"未求值：算术表达式无法解析 {rhs}")
    return (rhs, "求值")


def gen_class(rhs: str) -> str:
    rhs = comment_strip.sub("", rhs).strip()
    if "MECHANICS_GENERATION" in rhs:
        if "||" in rhs:
            return "世代(==5或≥7)"
        m = re.search(r"MECHANICS_GENERATION\s*(>=|<=|==|>|<)\s*(\d+)", rhs)
        return (f"世代({m.group(1).replace('>=', '≥').replace('<=', '≤')}{m.group(2)})"
                if m else "世代(表达式)")
    if rhs in ("AFFECTION_EFFECTS",):
        return f"设置间(={rhs})"
    return "独立"


def parse_settings(gen: int = 8):
    """解析两个设置文件，返回 (constants, methods, meta, unevaluated)。
    constants: (file, line, name, derivation, value, value_status)
    methods:   (file, line, name)
    meta:      (file, line, name, value)
    unevaluated: 显式报告的未求值项列表（无则空）。"""
    raw = []
    methods, meta = [], []
    for fname in FILES:
        in_settings = False
        for i, line in enumerate((R / fname).read_text(encoding="utf-8").splitlines(), 1):
            if re.match(r"^module Settings", line):
                in_settings = True
            elif re.match(r"^module Essentials", line):
                in_settings = False
            mc = const_re.match(line)
            if mc and not line.strip().startswith("#"):
                rhs_clean = comment_strip.sub("", mc.group(2)).strip()
                rec = (fname, i, mc.group(1), gen_class(rhs_clean), rhs_clean)
                (raw if in_settings else meta).append(rec)
            mm = method_re.match(line)
            if mm and in_settings:
                methods.append((fname, i, mm.group(1)))

    # 第一轮：求世代表达式与字面量；设置间引用第二轮解析
    resolved = {}
    for fname, i, name, deriv, rhs in raw:
        if rhs in {r[2] for r in raw} and "MECHANICS_GENERATION" not in rhs:
            continue  # 设置间引用，留待第二轮
        val, status = eval_setting(rhs, gen, resolved)
        resolved[name] = (val, status)

    constants, unevaluated = [], []
    for fname, i, name, deriv, rhs in raw:
        if rhs in resolved and "MECHANICS_GENERATION" not in rhs and rhs in {r[2] for r in raw}:
            # 设置间引用
            ref_val, ref_status = resolved[rhs]
            if ref_status == "求值":
                constants.append((fname, i, name, deriv, ref_val, f"跟随 {rhs}"))
            else:
                constants.append((fname, i, name, deriv, "未求值", f"未求值：引用项 {rhs}（{ref_status}）"))
        else:
            val, status = resolved.get(name, ("未求值", "未求值：未解析"))
            constants.append((fname, i, name, deriv, val, status))
        if constants[-1][4] == "未求值":
            unevaluated.append((name, constants[-1][5]))

    meta_rows = [(m[0], m[1], m[2], eval_setting(m[4], gen, resolved)[0]) for m in meta]
    return constants, methods, meta_rows, unevaluated


def parse_facility_lists():
    """解析 battle_facility_lists.txt，返回 (sections, refs)。
    sections: (name, {field: value})；refs: (section, field, path)（仅 Trainers/Pokemon）。"""
    path = PBS / "battle_facility_lists.txt"
    sections = []
    current = None
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if line.startswith("[") and line.endswith("]"):
            current = (line[1:-1], {})
            sections.append(current)
        elif "=" in line and current is not None and not line.startswith("#"):
            k, v = line.split("=", 1)
            current[1][k.strip()] = v.strip()
    refs = []
    for name, fields in sections:
        for f in ("Trainers", "Pokemon"):
            if f in fields:
                refs.append((name, f, fields[f]))
    return sections, refs


def facility_candidates():
    """PBS 顶层 battle_tower/cup 候选文件（目录存在集合）。"""
    return sorted(f.name for f in PBS.glob("*.txt")
                  if f.name.startswith(("battle_tower", "cup_")))


def matches_discovery(filename: str) -> bool:
    """普通发现匹配：完全基名相等，或以 基名+下划线 开头（按最长基名优先不影响布尔结果）。"""
    base = filename[:-4] if filename.endswith(".txt") else filename
    for b in PBS_BASE_NAMES:
        if base == b or filename.startswith(b + "_"):
            return True
    return False
