.. GIFtoolsCookbook documentation master file, created by
   sphinx-quickstart on Wed Oct 28 13:40:17 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

GRAV3D v6.0 package
===================

GRAV3D v6.0 is a program library for carrying out 3D forward modelling and inversion of gravity data.


.. figure:: images/title_image.PNG
     :align: center
     :width: 700

     True model, gravity anomaly data and the recovered model.


Highlights of Grav3D v6.0
^^^^^^^^^^^^^^^^^^^^^^^^^

Many advancements have been made since the previous version of this coding package.
Highlights of Grav3D v6.0 include:


    - the ability to forward model and invert surface, borehole, and airborne gravity data in 3D
    - sensitivity weighting so that targets recovered through inversion are placed at the correct depth
    - the ability to recover compact and/or blocky models using sparse norms, in additional to smooth models using a standard least-squares approach
    - implementing wavelet compression to reduce the storage cost of the sensitivity matrix and allow the user to solve larger problems


Sponsorship
^^^^^^^^^^^

The current improvements have been funded by the GIFtools Consortium which included “Potential fields and software for advanced inversion” (2012-2020) sponsored by Teck, Glencore, BHP Billiton, Vale, Cameco, Barrick, Rio Tinto, and Anglo American.



Contents
^^^^^^^^


.. toctree::
    :numbered:
    :maxdepth: 2

    Package overview <content/overview>
    Background theory <content/theory>
    Elements <content/elements>    
    Running the programs <content/runPrograms>
    Example <content/examples>
    References <references>
    
..  Need to run examples: maybe nutcracker?
..    Examples <content/examples>


