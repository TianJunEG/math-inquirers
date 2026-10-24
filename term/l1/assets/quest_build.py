#!/usr/bin/env python3
"""Shim: the Quest builder now lives in tools/b_quest.py and runs from build.sh / tools/build.py. This file still works:  python3 term/l1/assets/quest_build.py 10"""
import os, runpy, sys
sys.argv = [sys.argv[0]] + sys.argv[1:]
runpy.run_path(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools', 'b_quest.py'), run_name='__main__')
