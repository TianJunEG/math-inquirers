"""Lesson 4 no longer needs a wrapper: the 100-square pictures are in the shared template. Use  bash term/l1/build.sh 04"""
import os, runpy, sys
sys.argv = [sys.argv[0], '04']
runpy.run_path(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools', 'build.py'), run_name='__main__')
