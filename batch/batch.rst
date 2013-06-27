Batch Processing Plots
======================

Goal
----

* Make a single plot of several UV/Vis data sets.

* Process several data sets and plot each as a separate figure.

Skills
------

* Define `custom functions`_.

* Automatically read and process a series of files from a folder using
  functions from Python's built-in `os`_ module.

* Learn about string customization using `string formatting`_.

* Optional: Learn about the compact list generator process called `list
  comprehension`_

Data
----

:download:`UV/Vis Data Sets<batch.zip>` - This is a zip file, so you will need
to extract the data sets to be able to work with the data.

Final Product
-------------

All files in one plot:

.. plot:: batch/batch01.py
     
Each file plotted individually:

Download the :download:`following file<batch02.py>` and run from the directory
containing the UV/Vis data files.

Publication Quality
-------------------

Not complete...

.. _os: http://docs.python.org/2/library/os.html 
.. _custom functions: http://docs.python.org/2/tutorial/controlflow.html#defining-functions 
.. _string formatting: http://docs.python.org/2/library/string.html#formatstrings
.. _list comprehension: http://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
