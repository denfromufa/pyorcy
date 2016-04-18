from __future__ import print_function
import sys
from time import time
import pyorcy

from compute_function import f

def main():
    n = int(sys.argv[1])
    t1 = timef(n, use_cython=False)
    t2 = timef(n, use_cython=True)
    if t2 != 0:
        print("speedup: %.1f" % (t1 / t2))

def timef(n, use_cython):
    pyorcy.USE_CYTHON = use_cython
    t1 = time()
    v = f(n, n)
    delta = time() - t1
    print("n = %d f = %.1f use_cython = %s time: %.3fs"
          % (n, v, use_cython, delta))
    return delta

main()
