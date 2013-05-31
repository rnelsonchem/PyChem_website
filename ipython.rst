.. _ipy:

IPython
=======

The default Python shell is convenient but has limited functionality.
`IPython`_, an advanced interactive interpreter, was developed as an answer to
these problems. IPython has many different interfaces: the simplest is
accessed from the terminal by typing ``ipython``. Although it appears very
similar to the regular Python shell, IPython has a number of special features,
such as command history memory, introspection tools, syntax coloring, and
built-in macros.  Over the past couple of years in particular, IPython has
become of very powerful tool, and it's use is always recommended over the
regular Python shell. In addition to terminal-based IPython, two much more
powerful IPython interfaces have recently been added -- the :ref:`qtconsole`
and :ref:`notebook` -- which will be described below.

IPython has a number of built-in 'magic' commands, which are essentially
built-in macros. Several of these commands are very important, because they
make the IPython shell behave in much the same way as a terminal window. These
commands are preceded by a ``%``, and the most important are going to be
``%cd``, ``%pwd``, and ``%run``. The first two do the same thing as described
for the terminal. The last one is special. The run magic allows you to run a
Python program file from inside the IPython session. All of the code that was
in that file will then be loaded into IPython just as if you had typed it in
by hand. This is a very useful way to build up a program file and inspect the
data as it is being generated. A full listing of other magic commands can be
found on the web or in the 'Magic' drop-down menu in the Qt Console.

.. _qtconsole:

Qt Console
----------

The Qt Console is an IPython shell inside of a nice GUI window, which gives
you some nice drop down menus and the ability to cut-and-paste (not possible
from terminal IPython in Windows). It can be accessed by typing ``ipython
qtconsole`` in the terminal. This version of the IPython shell should always
be preferred when you need a Python shell.

.. _notebook:

Notebook
--------

The IPython notebook is a web-based interactive shell, which is started from
the terminal via ``ipython notebook``. This command should open your web
browser to the 'IPython Dashboard', which will look pretty empty at first. The
'New Notebook' button on the top right can be used to start an interactive
session. Each notebook acts as its own IPython session, and you can have as
many notebooks running as you'd like. 

Coding is a bit different in the notebook than the other Python shells,
though. In notebooks, code is input into cells. Each cell can have multiple
lines of code, and to run a cell, you can either type 'Shift-Enter' or
'Ctrl-Enter', each of which does slightly different things. Try them out for
yourself to see the difference. The advantage of the notebook interface is
that you can work interactively with your data, but you can save the notebooks
as well to be able to come back to it at a later time. (Saving is accomplished
using the disk icon at the upper left corner or under File->Save...) In this
way, the notebooks are the best of both worlds: an interactive shell and a
text editor rolled into one.

For this tutorial, we will work with IPython notebooks, and some of the
examples will be downloadable as interactive notebooks files. Each notebook is
simply a specially-formatted text file, and they are saved in the folder where
the notebook server was started. However, notebook files can be stored in
any/many locations on your computer, but only the notebooks that live in the
folder where you start the notebook server will be visible at any given time.
This means that you will need to know how to navigate to different folders
using the terminal (see above). If you can double-click Python files to run
them, then the :download:`following Python program<run_notebook.py>` can be
used to open the IPython notebook in whatever folder it resides.

.. _IPython: http://ipython.org/ 


