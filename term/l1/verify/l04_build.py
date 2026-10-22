"""Wrapper for Lesson 4: applies l04_ext (in-memory template patches), then runs the normal validate/build.

    python3 term/l1/verify/l04_build.py            validate, then build every output (what build.sh 04 does)
    python3 term/l1/verify/l04_build.py validate   validate only
"""
import os, runpy, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import l04_ext
l04_ext.install()
TOOLS = os.path.join(os.path.dirname(HERE), 'tools')
mode = sys.argv[1] if len(sys.argv) > 1 else 'build'
sys.argv = [sys.argv[0], '04']
runpy.run_path(os.path.join(TOOLS, 'validate.py' if mode == 'validate' else 'build.py'), run_name='__main__')
