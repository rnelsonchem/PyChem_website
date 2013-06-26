Plotting FTIR Data
==================

Goal
----

Make a simple plot of an FTIR data set.

Skills
------

* Introduction to Numpy_ -- Python's numerical array package

* Introduction to Matplotlib_ -- A very nice 2D/3D plotting package

* Reading data from a file using Numpy's loadtxt_ fuction.

* Creating an interactive line plot with Matplotlib's plot_ function.

* Setting and reversing the limits of the `x`_ and `y axis`_.

Data
----

:download:`FTIR Data Set<ftir_data.txt>`

Final Product
-------------

.. plot::
    
    import numpy as np
    import matplotlib.pyplot as plt

    wn, ab = np.loadtxt('ftir_data.txt', unpack=True)

    plt.plot(wn, ab)
    plt.xlim(4000, 1400)
    plt.ylim(0.2, 1.6)

    plt.show()


Publication Quality
-------------------

.. plot:: ftir/ftir_final.py
   

.. _Numpy: http://www.numpy.org/
.. _Matplotlib: http://matplotlib.org/
.. _plot: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
.. _loadtxt: http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html
.. _x: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.xlim
.. _y axis: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.ylim
