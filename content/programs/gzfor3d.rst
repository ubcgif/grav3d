.. _grav3d_fwd:

Forward Modeling
================

The program **gzfor3d.exe** performs the 3D forward modelling of gravity data for a density contrast model defined on a tensor mesh.

Running the Program
^^^^^^^^^^^^^^^^^^^

To run the executable, open a command window. In order, enter the path to the *gzfor3d* executable, the :ref:`tensor mesh file <meshfile>`, the :ref:`survey file <gravfile>`, the :ref:`density contrast model file <modelfile>` and a :ref:`topography file <topofile>` (optional). This in shown below.

.. figure:: images/run_fwd.PNG
     :align: center
     :width: 700


Units
^^^^^

    - **Data:** gravity anomaly in mGal
    - **Model:** density contrast model in g/cc


Output Files
^^^^^^^^^^^^

The program **gzfor3d.exe** creates the following output files:

    - **gzfor3d.grv:** Predicted data file.

    - **gzfor3d.log:** Log file which provides details about the parameters used in the forward modelling and diagnostic information about the results.

