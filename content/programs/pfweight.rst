.. _grav3d_pfweight:

Depth/Distance Weighting
========================

The program **pfweight.exe** create the depth or distance weighting that is to be used in the inversion. 

Running the Program
^^^^^^^^^^^^^^^^^^^

The weights are constructed by opening a command line window and typing the path to the code **pfweight.exe**, followed by a space, followed by the path to the :ref:`input file<grav3d_weight_input>` (denoted here as **pfweight.inp**). Optionally, the use made also include the number of threads. The syntax is as follows.


.. figure:: images/run_pfweight.PNG
     :align: center
     :width: 700


The argument *nThreads* specifying the number of CPU threads used in the OpenMP format is optional. If this argument is not given to the program, chooses to use all of the CPU threads on the machine. This argument allows the user to specify half, for example, of the threads so that the program does not take all available RAM. Note that this option is not available in the MPI-based code used for clusters.

Output files
^^^^^^^^^^^^

The program outputs ``x_weight.txt``. A file in the format, which contains weights for each cell, based on :ref:`depth weighting <depthWeight>` (x = "depth") or :ref:`distance weighting <distWeight>`  (x = "distance"). A log file ``pfweight.log`` is also written.
