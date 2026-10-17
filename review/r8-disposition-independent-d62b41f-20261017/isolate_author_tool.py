#!/usr/bin/env python3
"""Invoke the unmodified author CLI logic with its output root isolated."""
from pathlib import Path
import sys
sys.dont_write_bytecode=True
root=Path(__file__).resolve().parents[2]
source=root/'planning/implementation-routing/r8-20261017/routing.py'
namespace={'__file__':str(source),'__name__':'isolated_author_tool'}
exec(compile(source.read_bytes(),str(source),'exec'),namespace)
namespace['HERE']=Path(__file__).resolve().parent/'evidence/cli-isolation'
sys.exit(namespace['main']())
