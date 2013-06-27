Plotting Bruker NMR Data
========================

Goal
----

Make a simple plot of a Bruker NMR data set.

Skills
------

* Learning about `comparison operations`_ and `if and elif`_ statements.

* Finding items in a sequence with the `in`_ operator.

* Creating a *lin*\ early *space*\ d array of numbers with Numpy's `linspace`
  function

Data
----

:download:`NMR Data Set<nmr_data.txt>`

Final Product
-------------

.. plot::
     
    import numpy as np
    import matplotlib.pylab as plt

    data_file = open('nmr_data.txt')

    intensity = []

    for line in data_file:
        if 'LEFT' in line:
            sp = line.split()
            left = float(sp[3])
            right = float(sp[-2])

        elif 'SIZE' in line:
            sp = line.split()
            size = int(sp[3])

        elif line[0] == '#': 
            continue

        else: 
            intensity.append( line )

    ppm = np.linspace(left, right, size)
    intensity = np.array(intensity, dtype=float)

    plt.plot(ppm, intensity, '-')
    plt.xlim(8.9, 0.5)
    plt.yticks([])
    plt.tick_params(top='off')

    plt.show()


Publication Quality
-------------------

Version 1:

.. plot:: nmr/nmr_finalv1.py

Version 2:

.. plot:: nmr/nmr_finalv2.py
   
.. _comparison operations: http://docs.python.org/2/library/stdtypes.html#comparisons
.. _if and elif: http://docs.python.org/2/reference/compound_stmts.html#if
.. _linspace: http://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html
.. _in: http://docs.python.org/2/tutorial/datastructures.html#more-on-conditions
