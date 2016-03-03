from __future__ import print_function
import sys
from time import time
import pyorcy

from compute import f

def main():
    n = int(sys.argv[1])
    timef(n, False)
    timef(n, True)
    
def timef(n, use_cython):
    pyorcy.USE_CYTHON = use_cython
    t1 = time()
    v = f(n, n)
    print("n = %d f = %.1f use_cython = %s time: %.3fs"
          % (n, v, use_cython, time() - t1))

main()
