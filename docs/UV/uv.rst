Plotting UV/Vis Data
====================

Goal
----

Make a simple plot of a UV/Vis data set.

Skills
------

* Writing a custom file reader with Python's `open function`_ and a `for
  loop`_.

* Breaking apart a string with the `split`_ function.

* Adding data to an empty list with the `append`_ function.

* Converting a list to a `Numpy array`_. 

Data
----

:download:`UV/VIs Data Set<uv_data.txt>`

Final Product
-------------

.. plot::
    
    import numpy as np
    import matplotlib.pyplot as plt

    wn, ab = [], []

    data_file = open('uv_data.txt')

    for line in data_file:
        sp = line.split(',')
        wn.append( sp[0] )
        ab.append( sp[1] )

    data_file.close()

    wn = np.array(wn, dtype=float)
    ab = np.array(ab, dtype=float)

    plt.plot(wn, ab)
    plt.xlim(500,750)
    plt.ylim(-0.01, 0.05)

    plt.show()


Publication Quality
-------------------

.. plot:: UV/uv_final.py
   
.. _open function: http://docs.python.org/2/library/functions.html#open 
.. _for loop: http://docs.python.org/2/tutorial/controlflow.html#for-statements
.. _append: http://docs.python.org/2/tutorial/datastructures.html#more-on-lists
.. _Numpy array: http://docs.scipy.org/doc/numpy/user/basics.creation.html
.. _split: http://docs.python.org/2/library/stdtypes.html#str.split
