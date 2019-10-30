#!/usr/bin/env python
# encoding=utf8
import sys
import os
import pip
import json
import yaml
from distutils.sysconfig import get_python_lib
from pip._internal.operations.freeze import freeze


def is_venv():
    return hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)


packes = []
for requirement in freeze(local_only=True):
    packes.append(requirement)
if is_venv():
    venv = 'Yes, ' + sys.prefix
else:
    venv = 'No'
with open('Output.json', 'w', encoding='utf-8') as outfile:
    json.dump({'Python SysInformer': {
        'Python version:': sys.version,
        'Working inside virtualenv or venv': venv,
        'Python executables location:': sys.executable,
        'pip version is': pip.__version__,
        'pip location is': pip.__path__,
        'PYTHONPATH variable is:': os.getenv('PYTHONPATH'),
        'Packages location is': get_python_lib(),
        'Packages with version': packes,
    }}, outfile, ensure_ascii=False, indent=2)

with open('Output.yml', 'w') as outfile:
    yaml.dump({'Python SysInformer': {
        'Python version:': sys.version,
        'Working inside virtualenv or venv': venv,
        'Python executables location:': sys.executable,
        'pip version is': pip.__version__,
        'pip location is': pip.__path__,
        'PYTHONPATH variable is:': os.getenv('PYTHONPATH'),
        'Packages location is': get_python_lib(),
        'Packages with version': packes,
    }}, stream=outfile, default_flow_style=False, indent=3)
