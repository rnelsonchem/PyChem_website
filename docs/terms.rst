Special Terminology
===================

Python programmers use some specialized terminology, which present a barrier
to finding useful help on the internet. This section details some of the more
important terminology that you will encounter to help you decode some the vast
amounts of information on the web.

.. _mutable:

Mutability
----------

Several data types, such as lists and dictionaries, are mutable, which means
they can be modified in place. 

.. code-block:: ipython

    In [114]: a_list = ['Hello', 'World']
    
    In [115]: a_list[0] = 'Ryan'
    
    In [116]: a_list
    Out[116]: ['Ryan', 'World']

This is in contrast to strings and tuples, which are immutable. 

.. code-block:: ipython

    In [119]: a_tuple = ('Hello', 'World')
    
    In [120]: a_tuple[0] = 'Ryan'
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-120-93d344c80c43> in <module>()
    ----> 1 a_tuple[0] = 'Ryan'
    
    TypeError: 'tuple' object does not support item assignment
    
    In [121]: a_tuple = ('Ryan', ) + a_tuple[1:]
    
    In [122]: a_tuple
    Out[122]: ('Ryan', 'World')
    
    In [123]: a_string = 'Hello World'
    
    In [124]: a_string[0] = 'h'
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-124-35d795448c1c> in <module>()
    ----> 1 a_string[0] = 'h'
    
    TypeError: 'str' object does not support item assignment
    
    In [125]: a_string = 'h' + a_string[1:]
    
    In [126]: a_string
    Out[126]: 'hello World'

The reasons for this behavior are subtle, but nevertheless, it is very
important to keep in mind. This has many consequences for later behavior, so
we'll come back to this occasionally.

Namespaces
----------

As programs get larger and start to incorporate third-party code, it is
important to have a way to separate variable names, otherwise you run the risk
of variable name clashes. Namespaces are containers for variable names, which
are called *attributes* in this context. This has the effect of separating
variable names into different compartments. The *global* namespace refers to
variables that are directly defined in your code.  Some constructs, such as
functions, objects, and modules, have a *local* namespace which is attributes
that are separated from the global namespace. This definition is perhaps not
the most intuitive, but it becomes easier to understand in the context of
modules and objects given below. This concept is fairly important, so it might
be useful to find a more detailed explanation on the internet to get more
information.

Modules and Packages
--------------------

Modules are collections of extra code that can be imported into your code to
help accomplish additional tasks. Python contains a number of built-in
modules, called the `Standard Library`_. Third-party modules can be downloaded
and installed as *packages*, which are simply installation files of one or
more modules. In addition, it is possible to write your own modules, if you
have code that you reuse frequently and want to have it in one location.
Modules are accessed in your code by the ``import`` statement.  Modules have
their own namespace, so module attributes are accessed by using the name
of the module followed by a ``.`` and then the name of the attribute.

.. code-block:: ipython

    In [138]: import math # Mathematical functions, part of Standard Library
    
    In [139]: math.sin(1.5)
    Out[139]: 0.9974949866040544
    
    In [140]: sin(1.5) # This variable isn't pulled into your main code
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-140-0122361a1847> in <module>()
    ----> 1 sin(1.5)
    
    NameError: name 'sin' is not defined
    
In IPython, you can see the variables that are contained in a module by using
the <Tab> key. 

.. code-block:: ipython

    In [136]: math.<tab> # <tab> refers to the Tab key, don't type it out

You can rename a module on import to give it a more manageable name with the
``as`` keyword. Occasionally, you will see some imports with ``*``. I never
recommend this import method as it brings all of the variables from the module
into your global namespace. This is a great way to accidentally overwrite a
variable in your code, and it also makes it quite difficult to know where
variables came from when you're looking at your code later.

.. code-block:: ipython

    In [141]: import numpy as np # Third-party numerical array library
    
    In [142]: from math import * # Never do this
    
    In [143]: from math import sin # Sometimes okay, but don't overuse

Module imports only happen once, so if you are working on your own module
using IPython, you will need to use the ``reload`` function to get the changes
to take effect. This is a bit more advanced, so we'll leave it up to you to
learn more.

Object-Oriented
---------------

Python is an object-oriented programming language. Objects, also called
*classes* in Python, are abstracted definitions of a data type. These
abstractions can have associated variables and functions (also called
*methods*) that operate on that data. 

This can be very confusing at first, so let's look at a simple example to help
us get started. Let's conceptually define a new object called ``Rectangle``.
In general, what kind of data would a Rectangle require? You might expect that
it would at least be necessary to define two pieces of data: *length* and
*width*. What kind of functions, or manipulations, could we do with this data?
For starters, we may want to know the area and circumference of our rectangle,
so we could define functions to calculate those values.  These attributes --
length, width, area, circumference -- will form our base description a
rectangle *class*.  We can make many different *instances* of our class by
assigning values to *length* and *width*. The :download:`following
file<rectangle.py>` is an implementation of this rectangle class. You don't
need to understand the way it is written, but let's import it and see how this
works. Put this file in any folder, and move you IPython session to that
location (either using the ``%cd`` magic function or with you Python IDE).

First, import the ``Rectangle`` object from our ``rectangle`` module (in this
case our 'rectangle.py' file is the module). Because ``Rectangle`` is the only
attribute of the ``rectangle`` module, we'll use the ``from ... import ...``
syntax.

.. code-block:: ipython

    In [159]: from rectangle import Rectangle

Now that we've imported our new object, we can make a couple of instances with
different attributes.

.. code-block:: ipython

    In [160]: x = Rectangle(length=10., width=5.)
    
    In [161]: y = Rectangle(length=4., width=4.)

There are two functions defined in our Rectangle class -- ``calc_area`` and
``calc_circ`` -- that calculate the area and circumference of our rectangle,
respectively. Just as with modules, these attributes are accessed using the
``.`` separator. (Actually modules are just a type of object.)  

.. code-block:: ipython

    In [162]: x.calc_circ()
    Circumference = 30.0000
    
    In [163]: y.calc_circ()
    Circumference = 16.0000
    
    In [164]: x.calc_area()
    Area = 50.0000
    
    In [165]: y.calc_area()
    Area = 16.0000

We can view or change attributes of our class at any time as well.

.. code-block:: ipython

    In [166]: x.length
    Out[166]: 10.0
    
    In [167]: x.length = 20.0
    
    In [168]: x.length
    Out[168]: 20.0
    
    In [169]: x.calc_area()
    Area = 100.0000

Every piece of data in Python is an *object*, so they will always have
associated data and methods. This is very, very important as these methods can
function to make your life substantially easier. As an example, let's look at
some of the attributes of a string object.

.. code-block:: ipython

    In [152]: a_string = "Here's my test string.  "

    In [153]: print a_string
    Here's my test string.  
    
    In [154]: a_string.<Tab> # Tab key! Should see a bunch of attributes here.

    In [155]: a_string.upper()
    Out[155]: "HERE'S MY TEST STRING.  "
    
    In [156]: a_string.split()
    Out[156]: ["Here's", 'my', 'test', 'string.']

This can be a bit overwhelming at first. IPython helps you a lot by providing
'Tab completion' and the ``?`` help system. This can make your exploration of
various classes much easier, and it will be good to practice this as much as
possible to make it second nature.

.. code-block:: ipython

    In [170]: import math
    
    In [171]: math.<Tab> # Press the Tab key, don't type out the letters
    
    In [171]: math.sin?
    Type:       builtin_function_or_method
    String Form:<built-in function sin>
    Docstring:
    sin(x)
    
    Return the sine of x (measured in radians).


.. _Standard Library: http://docs.python.org/2/library/
