Python Basics
=============

This section details some of the most basic information that you'll need to
write Python code. It certainly won't be comprehensive, but it should give you
a good start.

Data Type Overview
------------------

Python has several built-in data types. For this tutorial, we'll focus on a
few, namely integers, floating point numbers, complex numbers, strings, and
lists (tuples). A couple of types not covered here are dictionaries and sets.
Both of these types are extremely useful, but they are not necessary for the
examples presented here.

Numbers in Python
-----------------

There are three different types of numbers in Python: integers, floating
point, and complex. There are some very important caveats to using numbers,
and those will be outlined after these types are introduced. All numbers can
be manipulated using the standard arithmetic operators, which are shown
below.

    * ``+`` - Addition
    
    * ``-`` - Subtraction

    * ``*`` - Multiplication

    * ``/`` - Division 

    * ``**`` - Power

    * ``%`` - Modulo (gives you the remainder of a division)

Mathematical operators have a precedence associated with them, which means
that certain operations are done before others. This is true of any computer
program or calculator, so it is important to keep this in mind. I don't know
the exact order, and perhaps very few others do either. Use parentheses (``(
)``) judiciously to avoid any problems. Here's an example of what I mean.

.. math::

    3 * 2^{3} = ?

    (3 * 2)^{3} = 216

    3 * (2^{3}) = 24

And in Python:

.. code-block:: ipython

    In [1]: 3*2**3
    Out[1]: 24
    
Integers
--------

Integers are any number that does not have a decimal point. These values can
be represented exactly by a computer, and in Python, they can be any size
(although very long numbers will end in 'L', which you can ignore). For
example:

.. code-block:: ipython

    In [1]: 4 + 7
    Out[1]: 11
    
    In [2]: 3 * (2**3)
    Out[2]: 24
    
    In [3]: 314**23
    Out[3]: 2687706896485028279945969132153957153803623321581014482944L
    
Floating Point
--------------

Floating point numbers (or float) have a decimal, even if the number after
the decimal is zero or nonexistent. These numbers have a certain precision
associated with them, which means that there are a limited number of digits
that can be displayed after the decimal. For example:

.. code-block:: ipython

    In [1]: 4.7*1.4
    Out[1]: 6.58
    
    In [2]: 3.2/1.99
    Out[2]: 1.6080402010050252

Complex Numbers
---------------

Complex numbers have a real and imaginary component, the latter is indicated
by a trailing ``j``. Both the real and imaginary component can be integers or
floating point numbers. For example:

.. code-block:: ipython

    In [1]: 1.7+4j
    Out[1]: (1.7+4j)
    
    In [2]: (1.7+4j) * (1.2-2.8j)
    Out[2]: (13.239999999999998+0.040000000000000036j)

Math Pitfalls
-------------

Variables
---------

Functions
---------

Commenting Code
---------------



