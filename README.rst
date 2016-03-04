======
pyorcy
======

Pyorcy has 2 purposes:

#. Allow the mix of python and cython code in a single file. This can also
   be done with cython pure python mode, but unlike pyorcy this approach does
   not offer you all the cython capabilities.

#. Launch the automatic compilation, triggered by a function decorator.

Check the examples: test.py and compute.py for a quick understanding
the mechanism.

Mechanism
---------

The user writes a python file which is the module. The function which
is to have a speedup is decorated with the @cythonize decorator.

A cython (.pyx) file is extracted from the python file (cf. function
extract_cython in the pyorcy.py).

This file will differ from the corresponding .py file is two ways;
- the comments starting with '#c ' are uncommented.
- the lines ending with '#p' are commented out.

Getting started
---------------

In a command prompt, change into the pyorcy directory and type::

 python test.py 5000

Type the command once again to see what happens when the cython code is
already compiled.

Installation
------------

Put pyorcy.py somewhere in your PYTHONPATH.

Troubleshooting
---------------

If you get

ImportError: Building module compute_cy failed: ['DistutilsPlatformError: Unable to find vcvarsall.bat\n']

like me, contact me. I have a workaround.

Tests
-----

Here is what I get:

#. When runnining for the first time (or removing the compiled files
   from ~/.pyxbld)::

    $ python test.py 5000
    [...]
    n = 5000 f = 131250000.0 use_cython = False time: 11.799
    n = 5000 f = 131250000.0 use_cython = True time: 3.868s

#. Running for a second time, code already compiled.::

    $ python test.py 5000
    [...]
    n = 5000 f = 131250000.0 use_cython = False time: 11.687s
    n = 5000 f = 131250000.0 use_cython = True time: 0.172s

  This means that the compilation takes 3s.

#. Commenting out the pyximport line in pyorcy.py::

    $ python test.py 5000
    n = 5000 f = 131250000.0 use_cython = False time: 11.559s
    n = 5000 f = 131250000.0 use_cython = True time: 0.032s

  This means that the pyximport check takes 0.14s.
