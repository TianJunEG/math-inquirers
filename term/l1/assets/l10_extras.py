"""Moved: the end-of-term check generator is now tools/b_check.py and is built by `bash term/l1/build.sh 10`. This shim only forwards when run as a script."""
import os, sys
if __name__ == '__main__':
    sys.exit(os.system(f'bash {os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "build.sh")} 10') >> 8)
