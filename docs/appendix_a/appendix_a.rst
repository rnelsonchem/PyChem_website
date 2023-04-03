Appendix A
==========

This is a partial listing of third party packages and programs that
incorporate Python for various scientific disciplines. In some cases, it can
be useful to look at `Python(x,y)`_, `Anaconda`_, and `Canopy`_ package lists
for a more complete listing.

.. _Python(x,y): https://code.google.com/p/pythonxy/wiki/StandardPlugins
.. _Anaconda: http://docs.continuum.io/anaconda/pkgs.html
.. _Canopy: https://www.enthought.com/products/canopy/package-index/

General Purpose
---------------

* Numpy_

  Provides N-dimensional numerical array objects and some linear algebra
  routines. Pretty much the base of every scientific package for Python.

.. _Numpy: http://www.numpy.org/

* Scipy_

  A broad range of scientific functions for integration, optimization, linear
  algebra, Fourier transforms, image processing, etc. See the documentation_
  for more details.

.. _Scipy: http://www.scipy.org/
.. _documentation: http://docs.scipy.org/doc/scipy/reference/

* Matplotlib_

  The de facto 2D plotting library for Python. Has some limited 3D
  capabilities as well.

.. _Matplotlib: http://matplotlib.org/

* Veusz_

  A GUI based plotting package. This is designed to be more interactive than
  Matplotlib but has much of the same functionality.

.. _Veusz: http://home.gna.org/veusz/

* Pandas_

  A very powerful data analysis library. Provides DataFrames, which are based
  on a similar concept in R, which essentially act like Excel spreadsheets on
  steroids. 

.. _Pandas: http://pandas.pydata.org/

* PyTables_

  A package for working with HDF5 files, which are an open-source file type
  designed for working with very large amounts of data. This is very useful if
  you have really large amounts of data that won't fit entirely into memory.

.. _PyTables: http://www.pytables.org/moin

* lmfit-py_

  An extension of Scipy's non-linear least squares functions, leastsq_ and
  curve_fit_, that lets you set bounds on parameters

.. _lmfit-py: http://newville.github.io/lmfit-py/
.. _leastsq: http://docs.scipy.org/doc/scipy/reference/generated/
    scipy.optimize.leastsq.html
.. _curve_fit: http://docs.scipy.org/doc/scipy/reference/generated/
    scipy.optimize.curve_fit.html

* nbviewer_

  A website that displays freely available IPython_ notebooks on the web.

.. _nbviewer: http://nbviewer.ipython.org/
.. _IPython: http://ipython.org/

Chemistry
---------

* nmrglue_

  A module for working with NMR data in Python

.. _nmrglue: https://code.google.com/p/nmrglue/

* Topspin_

  Bruker's NMR control and processing software uses Python for automation and
  pulse sequence design.

.. _Topspin: http://www.bruker.com/products/mr/nmr/nmr-software/software/
    topspin/overview.html

* Avogadro_ 

  A 3D molecule builder and viewer. This uses Python for scripting.  A newer
  version is being developed by Kitware.

.. _Avogadro: http://avogadro.openmolecules.net/wiki/Main_Page

* ChemPython_

  Python for chemical informatics

.. _ChemPython: http://chempython.org/

* `ChemDraw and ChemFinder`_

  Python is used as the internal scripting language for these products.

.. _ChemDraw and ChemFinder:
    http://chembionews.cambridgesoft.com/featureclips/Default.aspx?
    featureclipID=155

* Larch_

  A software for analysis of XAS data. The next generation of IFeffit.

.. _Larch: http://cars.uchicago.edu/xraylarch/

* PyMca_

  X-ray fluorescence toolkit, developed as ESRF

.. _PyMca: http://pymca.sourceforge.net/index.html

Biology
-------

* Biopython_

  Freely available tools for biological computations.

.. _Biopython: http://biopython.org/wiki/Main_Page

* Rosalind_

  Platform for bioinformatics.

.. _Rosalind: http://rosalind.info/problems/locations/

Earth and Oceanographic Science
-------------------------------

* ArcGIS_

  ArcGIS uses Python as its scripting language for automation through it's
  ArcPy_ module.

.. _ArcGIS: http://resources.arcgis.com/en/communities/python/
.. _ArcPy: http://help.arcgis.com/en/arcgisdesktop/10.0/help/
    index.html#//000v000000v7000000

* Shapely_

  Analysis of geometric (2D) objects. Apparently built on top of the GEOS and
  ITS libraries.

.. _Shapely: http://toblerity.github.io/shapely/

* Basemap_

  A Matplotlib toolkit for plotting on top of maps.

.. _Basemap: http://matplotlib.org/basemap/

* Iris_

  Visualization and analysis of meteorological and oceanographic data.

.. _Iris: http://scitools.org.uk/iris/

Mathematics
-----------

* Sage_

  Ridiculously powerful mathematics software that uses Python as it's
  interface language. Aims to be an open-source alternative to Mathematica,
  Matlab, etc.

.. _Sage: http://www.sagemath.org/ 

* SymPy_

  Symbolic mathematics library. Very useful if you don't need all of the stuff
  that comes with Sage.

.. _Sympy: http://sympy.org/en/index.html

* statsmodels_

  Statistical modeling package.

.. _statsmodels: http://statsmodels.sourceforge.net/

Astronomy
---------

* astropy_

  A suite of astronomy packages.

.. _astropy: http://www.astropy.org/

Cloud Computing Services
------------------------

* PiCloud_

  An online serves for distributed computing.

.. _PiCloud: http://www.picloud.com/

* `Google App Engine`_

  Python is used to develop Google Apps

.. _Google App Engine: https://developers.google.com/appengine/docs/python/
    gettingstartedpython27/introduction

* `Amazon Web Services`_

  Another site that lets you develop web applications in Python.

.. _Amazon Web Services: http://aws.amazon.com/python/

Documentation Generation
------------------------

* Sphinx_

  The standard Python documenation system. Used to make the main Python
  documenation. This website is a Sphinx-generated site.

.. _Sphinx: http://sphinx-doc.org/

* Dexy_

  Another more recent documentation system for scientific document automation.

.. _Dexy: http://www.dexy.it/features/

* rst2pdf_

  Convert restructuredtext_ files to pdf documents.

.. _rst2pdf: https://code.google.com/p/rst2pdf/
.. _restructuredtext: http://docutils.sourceforge.net/rst.html
