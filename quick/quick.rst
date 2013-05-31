Is this really hard?
====================

The 'simple' answer to that question is, 'it will be as hard as you make it.'
But that's not really satisfactory, is it?

A Quick Example
---------------

As another way to answer that question, let's take a look at some real world
data, and a simple Python analysis program. These data are *all* of the
crystallographically measured manganese oxygen distances between 1.2 and 2.6 Å
saved as a comma separated value (csv) text file. (These data were tabulated
around 2008.) The ultimate goal is to make a histogram of these values, so
that we can determine the average (and extreme) distances for different
manganese oxygen bond types.

The first ten lines of the :download:`data file<./MnO.csv>` are shown below:
the full file is over 43,000 lines long.

**Manganese-Oxygen Distances File**

.. literalinclude:: MnO.csv
    :language: text
    :linenos: 
    :lines: 1-10 

A Python program that analyzes these data and its output are shown below.
Notice that were were able to accomplish our goal in 5 lines of code.  *Note*:
The plot shown here is not the exact output of this program. If you were to
run this as a standalone program, the plot would open in an interactive
window, with support for panning, zooming, saving, etc. (Don't worry if the
commands don't make sense.  That's the point of reading this document!)

.. plot:: ./quick/MnO.py
    :include-source:

There. That wasn't so bad, was it? If this seems like something you'd like to
learn, then keep reading.

*BONUS*: Looking at this plot, what are the approximate average bond distance
for a manganese oxygen single bond? And a double bond?

Publication Quality Plot
------------------------

With some modifications, our simple plot can be made publication ready as
shown below.

.. plot:: ./quick/MnO_pub.py


