Installation
============

Python installers can be obtained from the `official website`_. (*Note*: As
you'll see below, installation of the Python on its own is not necessary, so
you can skip this step if you'd like. But the information that follows in this
paragraph is useful for reference purposes.) Currently, Python comes in two
major versions: 2 and 3. Python3 has numerous improvements and added advanced
features compared to older versions; however, these modifications broke
backward compatibility. (That means old code won't run unmodified with
Python3.) Many of the third party scientific packages have yet to be ported to
this newer version, so it is best to use Python2 for the time being. If you're
feeling adventurous, though, I would give Python3 a try. The largest and most
important scientific packages are Python3 compatible, so you should be able to
do most everything with this new version. From a new user perspective, the
differences between versions are minimal, so they won't be discussed here.

Installation of third party packages can be tedious (if not damn near
impossible) to do by hand.  Fortunately, some kind souls have put together
all-in-one installers that make this process much less painful. For
Windows, there is `Python(x,y)`_, which is loaded with scientific packages and integrates
well with Windows explorer. Although it is only available for Windows,
the website does have a nice listing of third party packages that can
be useful to browse. For all OS's, there are two installers prepared by
commercial developers: `Canopy`_ and `Anaconda`_.  Both of these options are
free (for academics), but they also require some form of registration. In
order to assure that everyone gets a uniform experience, I'm going to assume
that you will install and use `Anaconda`_, but I'm not necessarily endorsing it
over the other options.

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
