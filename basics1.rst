Python Basics Part 1
====================

This section details some of the most basic information that you'll need to
write Python code. It certainly won't be comprehensive, but it should give you
a good start.

Data Type Overview
------------------

Python has several built-in data types. To simplify our introduction, we'll
narrow our focus to just a few: none, booleans, integers, floating point
numbers, complex numbers, strings, and lists (tuples). Types that not covered
here are dictionaries and sets, which are extremely useful but not necessary
for the examples presented here.

None
----

The special term ``None`` can be used as a placeholder to represent nothing.
It seems like this wouldn't be at all useful, but it can be quite helpful at
times.

Booleans
--------

Boolean is just a fancy term that we use for true and false. There are two
ways to represent both of these values in Python. For true, you can either use
``1`` or ``True`` (first letter must be capitalized): for false, use either
``0`` or ``False``. The ``1`` and ``0`` versions will still work in math
equations, if you use them in that context. Booleans are going to be most
useful when we look at comparison testing later.

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

Mathematical operators have an execution precedence, which means that certain
operations are done before others. This is true of any computer program or
calculator, so it is important to keep this in mind. I don't know the exact
order, and perhaps very few others do either. To be safe, use parentheses
(``()``) judiciously to avoid any problems. Here's an example of what I mean.

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
(although very long numbers will end in 'L', which you can ignore).
:ref:`Strings<strings>` and floating point numbers can be forced to integers
with the ``int`` function. For example:

.. code-block:: ipython

    In [1]: 4 + 7
    Out[1]: 11
    
    In [2]: 3 * (2**3)
    Out[2]: 24
    
    In [3]: 314**23
    Out[3]: 2687706896485028279945969132153957153803623321581014482944L

    In [4]: int('7')
    Out[4]: 7
    
    In [5]: int(7.0)
    Out[5]: 7
    
    
Floating Point
--------------

Floating point numbers (or float) have a decimal, even if the number after the
decimal is zero or nonexistent. These numbers have a certain precision
associated with them, which means that there are a limited number of digits
that can be displayed after the decimal. Exponential multiples of 10 can be
represented with the ``e`` suffix notation. :ref:`Strings<strings>` and
integers can be forced to floating point values with the ``float`` function.
For example:

.. code-block:: ipython

    In [1]: 4.7*1.4
    Out[1]: 6.58
    
    In [2]: 3.2/1.99
    Out[2]: 1.6080402010050252

    In [3]: 1e13
    Out[3]: 10000000000000.0

    In [4]: float('7')
    Out[4]: 7.0
    
    In [5]: float(7)
    Out[5]: 7.0

Complex Numbers
---------------

Complex numbers have a real and imaginary component, the latter is indicated
by a trailing ``j``. Both the real and imaginary component can be integers or
floating point numbers. :ref:`Strings<strings>`, floats, and integers 
can be forced to complex numbers with the ``complex`` function. For example:

.. code-block:: ipython

    In [1]: 1.7+4j
    Out[1]: (1.7+4j)
    
    In [2]: (1.7+4j) * (1.2-2.8j)
    Out[2]: (13.239999999999998+0.040000000000000036j)

    In [3]: complex('7')
    Out[3]: (7+0j)
    
    In [4]: complex('7+2j')
    Out[4]: (7+2j)
    
    In [5]: complex(7)
    Out[5]: (7+0j)

Math Pitfalls
-------------

You can mix number types in calculations, and the answer will always be
represented by the most complex partner. Here are some examples.

.. code-block:: ipython

    In [1]: 1+2
    Out[1]: 3
    
    In [2]: 1+2.
    Out[2]: 3.0
    
    In [3]: 7*10
    Out[3]: 70
    
    In [4]: 7.*10
    Out[4]: 70.0
    
    In [5]: 32**22
    Out[5]: 1298074214633706907132624082305024L
    
    In [6]: 32.**22
    Out[6]: 1.298074214633707e+33
    
You need to be very careful with integers and division. This type of division
will not work as you expect, so you need to force one or both of the values in
a division operation to be a floating point or complex number.

.. code-block:: ipython

    In [1]: 1/2
    Out[1]: 0
    
    In [2]: 1/2.
    Out[2]: 0.5

Floating point numbers can not be represented exactly in a computer, so *they
will always contain some amount of error*. This is easily represented below,
where the ``==`` is simply a comparison operator (coming up later) that checks
if two things are the same. These errors accumulate as you do more
calculations, which can affect the accuracy of your results. When we get to
comparison tests, it will be very important to keep this limitation in mind.
*NOTE:* This is not a limitation of Python, but a general limitation of the
way computers represent floating point numbers. Programs like Excel will
sometimes do tricks behind the scenes to 'avoid' these errors, but they are
always there.

.. code-block:: ipython

    In [1]: 0.3 == 0.3
    Out[1]: True
    
    In [2]: 0.3 == 0.1 + 0.2
    Out[2]: False

.. _strings:

Strings (aka Text)
------------------

Strings are the fancy name for text in Python (and many other computer
languages). Strings can be wrapped in single or double quotes, it usually
doesn't matter what you choose. However, if you want to use either a single or
double quote in your text then, you can't use that type of quote to wrap your
string.

.. code-block:: ipython

    In [1]: 'This is a string'
    Out[1]: 'This is a string'
    
    In [2]: "So is this."
    Out[2]: 'So is this.'

Sometimes you may want your text to span multiple lines. You can do that by
using a triple single/double quote notation. This is heavily used in
:ref:`commenting<comment>`.

.. code-block:: ipython

    In [29]: """Here's some multi-
        ...: line text"""
    Out[29]: "Here's some multi-\nline text"

This last example also illustrates the use of special characters. In strings,
the ``\`` is called an escape character, and the character directly after will
then be given a special meaning. Below is a listing of some common escaped
special characters.

* ``\\`` -- Just adds a '\\' to your string. This can get really annoying when
  your working with file and folder paths in Windows.

* ``\n`` -- New line. This forces the text to go to the next line. This is the
  most common and preferred way to start a new line of text.

* ``\r`` -- Carriage return. This also forces the text to go to the next line.
  This was commonly used in older Mac OS versions and you will also see it in
  conjunction with the new line character on Windows (e.g. ``\r\n``).

* ``\t`` -- Tab.

There are a couple of other types of special strings: raw and unicode strings.
Raw strings have an 'r' preceding the first quote mark (e.g. ``r'A raw
string'``). Unicode are preceded by a 'u' (e.g. ``u'Unicode'``). The usage of
these is specialized, so I'll leave it up to you to read about them online if
you find that they are needed.

Lists and Tuples
----------------

Lists and tuples are ordered, arbitrary collections of Python objects.  The
difference between a tuple and a list is both in their construction and
something called :ref:`mutability<mutable>`, which will be discussed later.
Lists are wrapped in block brackets, ``[]``, whereas tuples are wrapped in
circle brackets ``()``. If a tuple contains only a single item, then it must
be followed by a comma (see the last two examples below). For most things,
lists are going to be the most common collection type, so use that as your
default container.

.. code-block:: ipython

    In [30]: ['A', 'Simple', 'list']
    Out[30]: ['A', 'Simple', 'list']
    
    In [31]: ('a', 'Simple', 'tuple')
    Out[31]: ('a', 'Simple', 'tuple')
    
    In [32]: [1, 'hello', [1, 2, 3]]
    Out[32]: [1, 'hello', [1, 2, 3]]
    
    In [33]: (1,)
    Out[33]: (1,)
    
    In [34]: (1) 
    Out[34]: 1        
