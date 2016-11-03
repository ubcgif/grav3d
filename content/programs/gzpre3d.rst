.. _gzpre3d:

GZPRE3D
=======

This utility multiplies a model by the stored sensitivity matrix in to produce predicted data. This program is included so that users who are not familiar with the wavelet transform and the structure of could utilize the available sensitivity matrix to carry out modelling exercises. The command line usage is:

``gzpre3d gzinv3d.mtx obs.loc model.den``

Input files
-----------

#. ``gzinv3d.mtx``: The sensitivity matrix file create from :ref:`gzsen3d`.

#. ``obs.loc``: The gravity :ref:`location file <gravLocFile>`.

#. ``model.den``: The density contrast :ref:`model file <modelFile>`.


Output file
-----------

The output file is a :ref:`predicted data file <gravPreFile>` (omitting uncertainty column) and is named ``gzpre3d.grv``. This program can be used to reproduce output predicted files from :ref:`gzinv3d`.
