Writing and Running Programs
============================

Writing Program Files
---------------------

Python programs are simply text (ASCII or Unicode) files, sometimes with a
'.py' file extension.  Because you'll be reading and writing a lot of these
files, invest some time looking for a good text editor.  Do *NOT* use MS
Notepad, Wordpad, or Word! There are many free text editors available, so
spend a little time to look them over.  Useful features will be syntax
highlighting (different keywords get highlighted different colors) and the
ability to uses spaces rather than tabs (see :ref:`Pitfalls` below). All three
of the all-in-one installers come with a nice text editor. Anaconda and
Python(x,y) come with Spyder; Canopy has a built-in editor. (Spyder is
probably the best. See :doc:`Appendix B <./appendix_b/appendix_b>` for info on
how to set up Spyder and also install it in Canopy.)

Running Programs
----------------

With some Python installations, '.py' files are associated with the Python
interpreter, so these programs run by simply double clicking on the icon.  If
this is not the case, things can be trickier (but not overly difficult).  You
need to know how to use the terminal, which is also called the command prompt
on Windows. (Although, we'll just call it terminal from now on.) A quick
search on the `internet`_ will turn up lots of useful information on how to
open a terminal for your particular OS. From the terminal, type ``python
file_name.py`` to run the program, as long as your program is in the current
working folder of the terminal. If not, then you'll need to use the commands
below.

There are a couple of commands that are essential to know to effectively use a
terminal.  First of all, you can move to different folders with the ``cd``
command, which stands for 'change directory' or 'current directory' (directory
= folder). On Windows, typing ``cd`` on its own will tell you the current
folder location.  On Mac and Linux machines, the command ``pwd``, or 'present
working directory', prints the current location. Below is an example of what
this might look like on a Mac.  (The ``$`` character denotes an input line of
the terminal and should not be explicitly typed out. The slashes need to be
reversed for Mac/Linux systems.)::

    $ pwd
    /Users/Ryan Nelson/
    $ cd /Users/Ryan Nelson/Desktop/Test Folder/
    $ python myprogram.py

Interactive Shell
-----------------

For many scientific applications, writing programs will actually be the final
step in the process. This is because Python comes equipped with a very nice
interactive interpreter, or shell. The shell can be accessed by simply typing
``python`` in the terminal, after which, you will see a ``>>>`` prompt appear.
At this point, anything you type is interpreted as a line of Python code, and
is executed once you type 'Enter'. In this way, you can test out short bits of
code to see what they do. For example, try the following::

    $ python
    Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 3+2
    5
    >>> print 'Hello world'
    Hello world
    >>> 3.7/4.8
    0.7708333333333334
    >>> exit() # or Ctrl-d

Python IDEs
-----------

Python has a number of Integrated Development Environments (IDE) that combine
both text editors and interactive shells into one program. Spyder is one
example of an IDE, and we'll assume you're using that for the rest of this
intro. Once you open a file with Spyder, you can run it by typing the 'F5'
key, or pressing the little green circle with a runner inside.

.. _pitfalls:

Pitfalls
--------

..  Text files are essentially platform independent, which makes them a highly
    portable storage medium. (I'll leave out my rant about storing research data
    as text files as well.)

There are a few things that will potentially cause problems when you're first
getting started programming. A few of these - file extensions, tabs vs spaces,
return characters -- are detailed here for reference. Others will be pointed
out as needed.

Knowing full file extensions will be very important. For example,
'file_name.py' is very different from 'file_name.py.txt'. Be sure to tell you
operating system to display file extensions for every file.  Information on
how to accomplish this can be `found on the web`_.

Before you start writing Python programs, be sure to tell your text editor to
use a specific number of spaces (usually 4) rather than tab characters. Spaces
and tabs are both special characters in text files. We perceive spaces and
tabs to be either a single space or multiple spaces between characters,
respectively.  However, to the computer reading the text file, a space and a
tab are both a single character. Unfortunately, there is no uniform definition
for how many spaces represent one tab. Some computers may treat this as 4
spaces, others 2 spaces, and still others 8 spaces. This is a big problem for
Python, because the initial indentation of a line has a very special meaning.
If you mix tab characters and spaces, you code may run fine for a while, but
it will most likely not be portable and may break when you upgrade your Python
installation. You've been warned. Most dedicated Python editors and IDEs, such
as Spyder, automatically set tabs to be 4 spaces.

Another minor annoyance is the way different operating systems represent new
line in a text file. Again, we perceive new lines as a break that moves us
to the next line in a file; however, depending on the OS, new lines are
defined as one or more special characters. Unfortunately,  each
operating system uses slightly different sequences of new line characters. If
you're trying to read a text file, and you find that it behaves differently
than you'd expect, it may be due to this issue. Again, the web has a lot of
resources to help you work through this problem, so I won't detail the
solutions here.

.. Create an appendix with some code for breaking up different return types.

Now that we've seen how to write and run some programs, let's get to the good
stuff. 

.. _Anaconda: https://store.continuum.io/
.. _found on the web: http://google.com/
.. _internet: http://google.com
