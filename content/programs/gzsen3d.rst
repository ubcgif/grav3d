.. _grav3d_sens:

Sensitivity Matrix
==================

The binary file containing the sensitivity matrix and distance weighting is created with the executable **gzsen3d_60.exe**.

Running the Program
^^^^^^^^^^^^^^^^^^^

The sensitivity matrix file is constructed by opening a command line window and typing the path to the code **gzsen3d_60.exe**, followed by a space, followed by the path to the :ref:`input file<grav3d_sens_input>` (denoted here as **sens.inp**). Optionally, the use made also include the number of threads. The syntax is as follows.

.. figure:: images/run_sens.png
    :align: center
    :width: 600


The argument specifying the number of CPU threads used in the OpenMP format is optional. If this argument is not given to the program, chooses to use all of the CPU threads on the machine. This argument allows the user to specify half, for example, of the threads so that the program does not take all available RAM. Note that this option is not available in the MPI-based code used for clusters.

Output Files
^^^^^^^^^^^^

The program **gzsen3d_60.exe** creates the following output files:

    - **gzsen3d.log**: A log file summarizing the run of the program.

    - **gzinv3d.mtx**: The sensitivity matrix file to be used in the inversion. This file contains the sensitivity matrix, generalized depth weighting function, mesh, and discretized surface topography. It is produced by the program and it's name is not adjustable. It is very large and may be deleted once the work is completed.

    - **sensitivity.txt**: This file is a :ref:`model file <modelFile>` that contains the average sensitivity for each cell. This file can be used for depth of investigation analysis or for use in designing special model objective function weighting.

    - Diagnostic files as described above to examine the wavelet compression properties, if chosen (**Diag=1**).

