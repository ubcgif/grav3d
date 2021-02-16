.. _gzpre3d:

GZPRE3D
=======

This utility multiplies a model by the stored sensitivity matrix in to produce predicted data. This program is included so that users who are not familiar with the wavelet transform and the structure of could utilize the available sensitivity matrix to carry out modelling exercises.

Running the Program
^^^^^^^^^^^^^^^^^^^

To run the executable, open a command window. In order, enter the path to the *gzpre3d* executable, the path to the sensitivity matrix file (*gzinv3d.mtz*), the path to the :ref:`survey file <gravfile>` and the path to the :ref:`density contrast model file <modelfile>`. This in shown below.


.. figure:: images/run_pre.PNG
     :align: center
     :width: 700


Output Files
^^^^^^^^^^^^

The output file is a :ref:`predicted data file <gravFile>` (omitting uncertainty column) and is named ``gzpre3d.grv``. This program can be used to reproduce output predicted files from :ref:`grav3d_fwd`.
