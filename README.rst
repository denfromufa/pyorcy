======
pyorcy
======

Pyorcy has 2 purposes:

#. Allow the mix of python and cython code in a single file. This can also
   be done with cython pure python mode, but unlike pyorcy this approach does
   not offer you all the cython capabilities.

#. Launch the automatic compilation, triggered by a function decorator.

Check the examples: ``examples/compute_main.py`` and
``examples/compute_function.py`` for a quick understanding the
mechanism.

Note that pyorcy provides a decorator mechanism which is similar to what numba
offers.

Mechanism
---------

The user writes a python file which is the module. The function which
is to have a speedup is decorated with the @cythonize decorator.

A cython (``.pyx``) file is extracted from the python file (cf. function
extract_cython in ``pyorcy.py``).

This extracted ``.pyx`` file will differ from the corresponding ``.py``
file is two ways:

- The comments starting with '#c ' are uncommented.

- The lines ending with '#p' are commented out.

Getting started
---------------

In the command prompt, stay in the main pyorcy directory and type::

  $ PYTHONPATH=. examples/compute_main.py 1000
  Creating .../pyorcy/examples/compute_function_cy.pyx
  n = 1000 f = 5250000.0 use_cython = False time: 0.373s
  n = 1000 f = 5250000.0 use_cython = True time: 0.001s
  speedup: 311.9

Type the command once again to see what happens when the cython code is
already compiled and execution is immediate::

  $ PYTHONPATH=. python examples/compute_main.py 1000
  File .../pyorcy/examples/compute_function_cy.pyx already exists
  n = 1000 f = 5250000.0 use_cython = False time: 0.375s
  n = 1000 f = 5250000.0 use_cython = True time: 0.001s
  speedup: 314.2

Testing
-------

Before installing, you can test the package like this::

  $ py.test pyorcy

And after installing with::

  $ python -c"import pyorcy; pyorcy.test()

Installation
------------

If you have downloaded the sources, just install as usual::

  $ python setup.py install

or just install from PyPI directly::

  $ pip install pyorcy

and you are ready to go.

Troubleshooting
---------------

If you get::

 ImportError: Building module compute_cy failed: ['DistutilsPlatformError: Unable to find vcvarsall.bat\n']

like I did, contact me. I have found a workaround.

My use case
-----------

Here is why is pyorcy is important for my work.

I work in a team of engineers and mathematicians. They have learnt
python but not cython. Recently I have proposed a library with some
cython code. This added dependency has created resistance to the
acceptance of my code. Firstly, we met problems with compatibility
with Cython, Anaconda and virtual environments. Secondly, when my
collegues find bugs, they are not happy to depend on my help. They
want to do the debugging themselves. As they don't know Cython and are
uncomfortable with the compilation issues, I decided to provide two
versions of my code, one in pure python and another in Cython. Of
course maintaining two versions of my functions is not an advisable
approach. Using cython pure python mode is not an option since the
code needs advanced cython capabilities.

With pyorcy the user can then add a ``pyorcy.USE_CYTHON = False``
before the function call that they want to debug and proceed the
debugging in the pure python version, being able to add prints and
pbd without having to recompile, nor having to learn cython.

Before presenting pyorcy, a colleague suggested me to switch from
cython to numba. This would solve some of the issues, but I would
loose the freedom that cython gives (e.g. mix pure C code when needed)
and the wonderful html output (which gives us a perfect control of
what runs behind the scenes). Pyorcy comes partly as an answer to his
suggestion.
