Elements of the program GRAV3D
==============================

Introduction
------------

The program library consists of the programs:

#. **GZFOR3D**: performs forward modelling.

#. **PFWEIGHT**: calculates depth or distance weighting function.

#. **GZSEN3D**: calculates sensitivity for the inversion.

#. **GZINV3D**: performs 3D gravity inversion.

#. **GZPRE3D**: multiplies the sensitivity file by the model to get the predicted data. This rarely used utility multiplies a model by the sensitivity matrix in to produce the predicted data. This program is included so that users who are not familiar with the wavelet transform and the structure of can utilize the available sensitivity matrix to carry out model studies.

Each of the above programs requires input files and the specification of parameters in order to run. However, some files are used by a number of programs. Before detailing the procedures for running each of the above programs, we first present information about these general files.

General files for GRAV3D programs
---------------------------------

There are seven general files which are used in GRAV3D. All are in ASCII text format. Input files can have any user-defined name. *Program output files have restricted file names that will be over-written if already in the directory*. Also the filename extensions are not important. Many prefer to use the filename convention so that files are more easily read and edited in the Windows environment. File and file locations may have spaces in the name or path, but it is discouraged. The file name (absolute or relative path) must be 500 characters or less in length. The files contain components of the inversion:

.. toctree::
    :maxdepth: 1

    Mesh <files/mesh>
    Topography <files/topo>
    Location <files/loc>
    Observation <files/obs>
    Model <files/model>
    Weighting <files/weight>
    Active <files/active>    



