Installation
============

Python is currently available in two major versions: 2 and 3.  Python3 has
added numerous improvements and advanced features to the older version;
however, these modifications broke backward compatibility. (That means old
code won't run unmodified with Python3.) Many of the third-party scientific
packages have yet to be ported to this newer version, so it is best to use
Python2 for the time being. If you're feeling adventurous, though, I would
give Python3 a try.  The largest and most important scientific packages are
Python3 compatible, so you should be able to do most everything with this new
version. From a new user perspective, the differences between versions are
minimal, so they won't be discussed here.

There are several installation options for Python on the web. Python
installers can be obtained from the `official website`_; however, installation
of third-party packages can be tedious (if not damn near impossible) to do by
hand.  Fortunately, some kind souls have put together all-in-one installers
that make this process much less painful. For Windows, there is
`Python(x,y)`_, which is loaded with scientific packages and integrates well
with Windows explorer. Although it is only available for Windows, the website
does have a nice listing of third party packages that can be useful to browse.
For all OS's, there are two installers prepared by commercial developers:
`Canopy`_ and `Anaconda`_.  Both of these options are free (for academics),
but they require some form of registration. In order to assure that everyone
gets a uniform experience, I'm going to assume that you will install and use
`Canopy`_, but I'm not necessarily endorsing it over the other options.
:doc:`Appendix B <./appendix_b/appendix_b>` has some optional detailed
instructions for setting up Canopy so that everyone gets a uniform experience.
You don't have to follow these instructions, but if you find that something on
this site does not work as expected, be sure to check this page to see if
there is anything that you need to change with your setup.

*32 Bit Versus 64 Bit*

As a side note, you'll see many of these packages and installers come in *32
bit* and *64 bit* varieties. Modern operating systems are 64 bit, and from a
user perspective, this is simply going to affect the amount of memory a
program can use at a given time. It is best to try and install the 64 bit
version first. If that fails, fall back on the 32 bit version. It is important
to remember which version you install, though, because this will affect the
choice of installers for other Python code packages in the future.

.. _official website: http://python.org
.. _Canopy: https://www.enthought.com/products/canopy/
.. _Anaconda: https://store.continuum.io/
.. _Python(x,y): https://code.google.com/p/pythonxy/
.. _IPython: http://ipython.org/ 
