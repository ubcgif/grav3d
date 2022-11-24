.. _running:

.. important:: The features and executable names within the GRAV3D the v6.0, v6.0.1 and v6.0.2 packages remain the same. Differences in version number correspond to improvements in performance.

Running the programs
====================

This section provides describes how to run all executables pertaining to the GRAV3D v6 package.

.. note::

    All executable files, input files, output filenames and files specified within input files can be specified in the following manner:

    - as just the filename if contained within the current working directory (Example: *filename.txt*)
    - as a file path relative to the current working directory (Example: *sub_dir\\filename.txt*)
    - as the full path (Example: *C:\\Users\\Name\\Tests\\filename.txt*)

    Executable files should **not** be renamed. However, input file names can be specified by the user if desired..

Introduction
------------

All programs in the package can be executed under Windows or Linux environments. They can be run by typing the program name followed by a control file in the ``command prompt`` (Windows) or ``terminal`` (Linux). They can be executed directly on the command line or in a shell script or batch file. When a program is executed without any arguments, it will print the usage to screen.


Executables
-----------

The program library consists of the programs:

    - **gzfor3d_60.exe**: A code for forward modeling gravity anomaly data from a density contrast model model.

    - **gzsen3d_60.exe**: calculates the sensitivity matrix for the inversion and outputs sensitivity weights.

    - **gzinv3d_60.exe**: performs 3D inversion of gravity anomaly data to recover a density contrast model.

    - **gzpre3d_60.exe**: multiplies the sensitivity file by the model to get the predicted data. This rarely used utility multiplies a model by the sensitivity matrix in to produce the predicted data. This program is included so that users who are not familiar with the wavelet transform and the structure of can utilize the available sensitivity matrix to carry out model studies.

Utility codes relevant to this package include:

   - **blk3cell.exe:** A utility for generating block models on tensor meshes

   - **pfweight_60.exe:** A utility for computing depth or distance weighting for potential field inversion


Contents
--------

  .. toctree::
    :maxdepth: 1

    Create model <programs/createModel>
    Forward modelling <programs/gzfor3d>
    Depth/distance weighting <programs/pfweight>
    Sensitivity calculation <programs/gzsen3d>
    Inversion <programs/gzinv3d>
    Predicted data from sensitivity <programs/gzpre3d>
    Single computer vs cluster <programs/general>

