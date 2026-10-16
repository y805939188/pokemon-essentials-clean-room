"""Compatibility entrypoint; checkpoint implementation retained in Git history."""
import pathlib, runpy
runpy.run_path(str(pathlib.Path(__file__).with_name('validate-final.py')),run_name="__main__")
