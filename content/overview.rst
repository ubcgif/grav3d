.. _overview:

GRAV3D v5.0 Package Overview
============================

Description
-----------

GRAV3D is a program library for carrying out forward modelling and inversion
of surface and airborne gravity data over 3D structures. The program
library carries out the following functions:

#. Forward modelling of the vertical component of the gravity response
   to a 3D volume of density contrast.

#. The model is specified in the mesh of rectangular cells, each with a
   constant value of density contrast. Topography is included in the
   mesh. The vertical gravity response can be calculated anywhere within
   the model volume, including above the topography to simulate ground
   or airborne surveys. There is also a capability to simulate and
   invert data collected beneath the surface (e.g. borehole surveys) and
   combinations of ground and borehole surveys.

   -  The inversion is solved as an optimization problem with the
      simultaneous goals of (i) minimizing a model objective function
      and (ii) generating synthetic data that match observations to
      within a degree of misfit consistent with the statistics of those
      data.

   -  To counteract the inherent lack of information about the distance
      between source and measurement, the formulation incorporates depth
      or distance weighting.

   -  By minimizing the model objective function, distributions of
      subsurface susceptibility contrast are found that are both close
      to a reference model and smooth in three dimensions. The degree to
      which either of these two goals dominates is controlled by the
      user by incorporating a priori geophysical or geological
      information into the inversion. Explicit prior information may
      also take the form of upper and lower bounds on the susceptibility
      contrast in any cell.

   -  The regularization parameter (controlling relative importance of
      objective function and misfit terms) is determined in either of
      three ways, depending upon how much is known about errors in the
      measured data.

   -  Implementation of parallel computing architecture (OpenMP) allows
      the user to take full advantage of multi-core processors on a CPU.
      A cluster-based code using Message Passing Interface (MPI) is also
      available. Notes on computation speed are found at the end of this
      section.

#. The large size of 3D inversion problems is mitigated by the use of
   wavelet compression. Parameters controlling the implementation of
   this compression are available for advanced users.

The initial research underlying this program library was funded principally by the mineral industry consortium "Joint and Cooperative Inversion of Geophysical and Geological Data" (1991 - 1997) which was sponsored by NSERC and the following 11 companies: BHP Minerals, CRA Exploration, Cominco Exploration, Falconbridge, Hudson Bay Exploration and Development, INCO Exploration & Technical Services, Kennecott Exploration Company, Newmont Gold Company, Noranda Exploration, Placer Dome, and WMC.

The current improvements have been funded by the consortium "Potential fields and software for advanced inversion" (2012-2016) sponsored by Newmont, Teck, Xstrata, BHP Billiton, Vale, Computational Geoscience Inc, Cameco, Barrick, Rio Tinto, and Anglo American.

Program library content
-----------------------

Executable programs
^^^^^^^^^^^^^^^^^^^

This package consists of five major programs:

   - PFWEIGHT: calculates the depth/distance weighting function
   - GZFOR3D: performs forward modelling
   - GZSEN3D: calculates the sensitivity matrix
   - GZPRE3D: multiplies the sensitivity file by the model to get the predicted data
   - GZINV3D: performs 3D gravity inversion

Graphical user interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^
GUI-based utilities for these codes include respective viewers for the data and models. They are only available on Windows platforms and can be freely downloaded through the UBC-GIF website:

   - `GM_DATA_VIEWER <http://www.eos.ubc.ca/~rshekhtm/utilities/gm-data-viewer.zip>`__: a utility for viewing raw surface or airborne data (not borehole data), error distributions, and for comparing observed to predicted data directly or as difference maps.
   - `MeshTools3D <http://www.eos.ubc.ca/~rshekhtm/utilities/MeshTools3d.zip>`__: a utility for displaying resulting 3D models as volume renderings. Susceptibility volumes can be sliced in any direction, or isosurface renderings can be generated.
   - `GUI <http://gif.eos.ubc.ca/sites/default/files/grav3d-gui.zip>`__: a GUI to run GRAV3D v5.0 on either Linux or Windows. **NOTE: The download does not contain the inversion/modelling codes.**

Licensing
---------

A **constrained educational version** of the program is available with
the `IAG <http://www.flintbox.com/public/project/1605/>`__ package
(please visit `UBC-GIF website <http://gif.eos.ubc.ca>`__ for details).
The educational version is fully functional so that users can learn how
to carry out effective and efficient 3D inversions of magnetic data.
**However, RESEARCH OR COMMERCIAL USE IS NOT POSSIBLE because the
educational version only allows a limited number of data and model
cells**.

Licensing for an unconstrained academic version is available - see the
`Licensing policy document <http://gif.eos.ubc.ca/software/licenses>`__.

**NOTE:** All academic licenses will be **time-limited to one year**.
You can re-apply after that time. This ensures that everyone is using
the most recent versions of codes.

Licensing for commercial use is managed by third party distributors.
Details are in the `Licensing policy document <http://gif.eos.ubc.ca/software/licenses>`__.

Installing
----------

There is no automatic installer currently available for the . Please
follow the following steps in order to use the software:

#. Extract all files provided from the given zip-based archive and place
   them all together in a new folder such as

#. Add this directory as new path to your environment variables.

Two additional notes about installation:

-  Do not store anything in the "bin" directory other than executable
   applications and Graphical User Interface applications (GUIs).

-  A Message Pass Interface (MPI) version is available for Linux upon
   and the installation instructions will accompany the code.

Highlights of changes from version 3.2
--------------------------------------

The principal upgrades, described below, allow the new code to take advantage of current multi-core computers and also provide greater flexibility to incorporate the geological information.

Improvements since the previous version:

#. A new projected gradient algorithm is used to implement hard
   constraints.

#. Fully parallelized computational capability (for both sensitivity matrix calculations and inversion calculations).

#. A facility to have active and inactive (i.e. fixed) cells.

#. Bounds are be specified through two separate files, rather than one two-column file.

#. Additional flexibility for incorporating the reference model in the model objective function facilitates the generation of smooth models when borehole constraints are incorporated.

#. The ``gzinv3d.log`` file has been simplified and detailed information on the inversion can be found in the ``gzinv3d.out`` file.

#. Backward compatibility: The new version has changed the input file format and the bounds file. Data, mesh, model, and topographic file formats have not changed.

Notes on computation speed
^^^^^^^^^^^^^^^^^^^^^^^^^^

-  For large problems, GZSEN3D is significantly faster than the previous single
   processor inversion because of the parallelization for computing the
   sensitivity matrix computation and inversion calculations. Using
   multiple threads for running the parallelized version resulted in
   sensitivity matrix calculation speedup proportional to the number of
   threads. The increase in speed for the inversion was less pronounced,
   but still substantial.

-  It is strongly recommended to use multi-core processors for running
   the and . The calculation of the sensitivity matrix (:math:`\mathbf{G}`) is
   directly proportional to the number of data. The parallelized
   calculation of the :math:`n` rows of :math:`\mathbf{G}` is split
   between :math:`p` processors. By default, all available processors
   are used. There is a feature to limit :math:`p` to a user-defined
   number of processors.

-  In the parallelized inversion calculation,
   :math:`\mathbf{G}^T \mathbf{G}` is multiplied by a vector, therefore
   each parallel process uses only a sub-matrix of :math:`\mathbf{G}`
   and then the calculations are summed. Since there is significant
   communication between the CPUs, the speedup is less than a direct
   proportionality to the number of processors. However when running the
   same inversion under MPI environment on multiple computers the
   advantage is that a single computer does not have to store the entire
   sensitivity matrix.

-  For incorporating bound information, the implementation of the projected gradient algorithm in version 5.0 is primarily that the projected gradient results in a significantly faster solution than the logarithmic barrier technique used in earlier versions.


