from __future__ import print_function
import sys
import re
import os
import pyximport; pyximport.install()

USE_CYTHON = True

def extract_cython(path_in, force=False):
    if not path_in.endswith('.py'):
        raise ValueError("%s is not a python file" % path_in)
    
    path_out = path_in.replace('.py', '_cy.pyx')
    if (not force and os.path.exists(path_out)
        and os.path.getctime(path_out) >= os.path.getctime(path_in)):
        print("File %s already exists" % path_out)
        return
    
    print("Creating %s" % path_out)
    with open(path_out, 'w') as fobj:
        for line in open(path_in):
            line = line.rstrip()
            m = re.match(r'( *)(.*)#p *$', line)
            if m:
                line = m.group(1) + '#p ' + m.group(2)
            else:
                line = re.sub(r'#c ', '', line)
            fobj.write(line + '\n')

def cythonize(func):
    module_name = func.__module__
    module = __import__(module_name)
    path = module.__file__.replace('.pyc', '.py')
    extract_cython(path)
    def wrapper(*arg, **kw):
        if USE_CYTHON:
            module = __import__(func.__module__ + '_cy')
            func2 = getattr(module, func.__name__)
            return func2(*arg, **kw)
        else:
            return func(*arg, **kw)
    return wrapper

if __name__ == '__main__':
    extract_cython(sys.argv[1])
