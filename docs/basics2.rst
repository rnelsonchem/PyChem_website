Python Basics Part 2
====================

Print Statement
---------------

The print statement is your friend. This statement writes things either to the
screen (default) or to files. You can print pretty much anything, and you will
get some kind of output, which will be dependant on the data type. This
statement is commonly used for debugging code.  In the examples below, notice
the special usage of the comma.

.. code-block:: ipython

    In [36]: print 'Hello world'
    Hello world
    
    In [37]: print 7.0
    7.0
    
    In [38]: print 'Hello', "World"
    Hello World
    
    In [39]: print 7, 'Hello'
    7 Hello

    In [40]: print 'Hello\nWorld'
    Hello
    World

Variables
---------

Variables are labels used to reference a particular value. Variables are set
with the ``=``, which is called the assignment operator. This operator assigns
a piece of data or an expression (on the right) to a variable name (on the
left). There are some rules to writing variable names, for example, the name
can't start with a number and can't contain spaces or ``-`` characters. There
may be more extensive lists on the web.

.. code-block:: ipython

    In [49]: i = 7
    
    In [50]: first_variable = 'Hello'
    
    In [51]: Another = 'there'

Variable names can be used later as references for the data they contain. In
this way, they abstract some of the values in your code. In Python, you can
reassign a variable at any time that you want. In addition, you can reassign
the variable with a reference to it's previous state. This is done in the
third-to-the-last line below. Variable names must be assigned a value before
they can be used as in the last example. 

.. code-block:: ipython

    In [58]: x = 7
    
    In [59]: y = 10.2
    
    In [60]: x*y
    Out[60]: 71.39999999999999
    
    In [61]: y = 137
    
    In [62]: x*y
    Out[62]: 959
    
    In [63]: y = y + 1.2
    
    In [64]: print y
    138.2

    In [66]: print no_data_assigned
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    <ipython-input-66-937432be0f81> in <module>()
    ----> 1 print no_data_assigned
    
    NameError: name 'no_data_assigned' is not defined

.. _functions:

Functions
---------

Functions are small bits of code that do a particular task. These will have a
name associated with them, like a variable, but to *call* (i.e. use) them they
must end with a pair of round brackets, ``()``, which may contain some extra
information.  Python has many built-in functions, a few of which you've
already seen: ``str``, ``int``, ``float``, and ``complex``.  

Another very common function is ``range``, which creates a list of integers.
Here's a few examples of it's usage. In IPython, you can find out what a
function does typing the name of a function followed a ``?``.  

.. code-block:: ipython

    In [68]: range(10)
    Out[68]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    In [69]: range(2,10)
    Out[69]: [2, 3, 4, 5, 6, 7, 8, 9]
    
    In [70]: range(2,20,2)
    Out[70]: [2, 4, 6, 8, 10, 12, 14, 16, 18]

    In [71]: range?
    Type:       builtin_function_or_method
    String Form:<built-in function range>
    Namespace:  Python builtin
    Docstring:
    range([start,] stop[, step]) -> list of integers
    
    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.

The values that are *passed* to a function are called *arguments*. As you can
see from the description of ``range``, it can accept up to three arguments.
The ones in square brackets are optional, so at the minimum, range must have
one argument, which is the *stop* value. Additional arguments are processed in
the order they appear in the description above. These are called *positional
arguments*. 

Some functions have arguments that are passed into the function using a
specific word for each value. These are called *keyword arguments*. These must
come after the position arguments (if any), but can be passed into the
function in any order. Below is an example with the ``dict`` function, which
creates dictionaries (these are another data type that were not discussed).

.. code-block:: ipython

    In [84]: dict(one=1, two=2, three=3)
    Out[84]: {'one': 1, 'three': 3, 'two': 2}
    
    In [85]: dict(two=2, three=3, one=1)
    Out[85]: {'one': 1, 'three': 3, 'two': 2}

We will see many, many types of functions, so it is good to make sure that you
understand the terminology here. You can also create your own functions, but
we'll save that lesson until the examples section.

.. _comment:

Commenting Code
---------------

Comments are little notes that you add to your code, but are ignored when the
program is executed. Commenting your code is one of the most important things
you can do. This provides a mechanism to keep track of what you were doing.
This may seem like a waste of time, but when you come back to something after
a couple of months, it can be very painful to decipher what you were doing.
Comments can be added to your code in several ways. The most common is going
to be the ``#`` character. Everything to the right of this character on a
particular line will be ignored and treated as a comment. In addition, triple
quotes can be used to enclose multi-line comments.

.. code-block:: ipython

    In [86]: print 'Hello!'
    Hello!
    
    In [87]: # print 'Hello!'
        ...: 
    
    In [88]: # It looks like I commented-out the last example.
        ...: 
    
    In [89]: print 'Hello!' # This comment comes after some code
    Hello!
    
    In [90]: '''This is a multi-
        ...: line bit of commenting that can be used for long
        ...: comments. This can not come after code, but must start on
        ...: its own line.'''
    Out[90]: 'This is a multi-\nline bit of commenting that can be used for long\ncomments. This can not come after code, but must start on\nits own line.'
    
    In [91]: # In the above example, nothing would get printed if that was found
        ...: # in a Python program file.
        ...: # It's only in IPython that something gets printed.
        ...: 

Indexing
--------

Strings, lists, and tuples are all ordered data types, and the individual
elements can be extracted numerically in a process called *indexing*. The
*index* is a number contained in square brackets directly following the name
of the variable. This number is a positional reference to an individual
element of the underlying data. Index values start at zero and can not
exceed the length of the data. This is best seen by example.

.. code-block:: ipython

    In [93]: a_string = 'Hello World'
    
    In [94]: a_list = ['Hello', 'World']
    
    In [95]: a_tuple = ('Hello', 'World')
    
    In [96]: a_string[0] # The first element
    Out[96]: 'H'
    
    In [97]: a_list[0]
    Out[97]: 'Hello'
    
    In [98]: a_tuple[0]
    Out[98]: 'Hello'
    
    In [99]: a_string[2]
    Out[99]: 'l'
    
    In [100]: a_string[100]
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    <ipython-input-100-ea0b7e207709> in <module>()
    ----> 1 a_string[100]
    
    IndexError: string index out of range
    
The built-in function ``len`` returns the length of the data and will help you
to avoid indexing errors.

.. code-block:: ipython

    In [101]: len(a_string)
    Out[101]: 11
    
    In [102]: len(a_list)
    Out[102]: 2
    
    In [103]: len(a_tuple)
    Out[103]: 2
    
Indexing can also be used to slice a segment of the data, with an optional
skip as well, by separating index values with a ``:``. This can be very useful
for removing portions of the data or renaming strings. If one of the index
values is missing, it is taken as either the start or end of the data.
Negative values can be used if you want to go in the reverse direction.

.. code-block:: ipython

    In [105]: a_string[2:6] # Does not include the 6th index (i.e. 7th element)
    Out[105]: 'llo '
    
    In [106]: a_string[2:11:2] # skip every other element
    Out[106]: 'loWrd'
    
    In [107]: a_string[5:]
    Out[107]: ' World'
    
    In [108]: a_string[:5]
    Out[108]: 'Hello'
    
    In [109]: filename = 'picture.jpg'
    
    In [110]: filename[-3:]
    Out[110]: 'jpg'
    
    In [111]: filename[:-3]
    Out[111]: 'picture.'
    
    In [112]: newfilename = filename[:-3] + 'png'
    
    In [113]: newfilename
    Out[113]: 'picture.png'

For lists only, indexing can be used to change the values at a specific
location, but this is covered in the :ref:`mutability<mutable>` section.
