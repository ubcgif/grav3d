.. _example_sensitivity:

.. note:: This example has been developed to demonstrate functionality specific to v6.0. The example can be completed using v5.0, however some functionality may not exist in v5.0 and the format of certain input files may differ slightly.


Computing Sensitivities
=======================

Here the code **gzsen3d_v60.exe** is used to compute and output the sensitivities for use in the inversion. Here, we generate we use the input file **sensitivity_L2.inp** to generate sensitivities for a standard smooth inversion. We then use the input file **sensitivity_sparse.inp** to generate sensitivities that can be used for sparse inversion.

Before running this example, you may want to do the following:

	- `Download and open the zip folder containing the entire grav3d example <https://github.com/ubcgif/grav3d/raw/master/assets/grav3d_example.zip>`__ (if not done already)
	- Learn how to :ref:`compute sensitivities and learn the format of the input files <gzsen3d>`


Smooth Inversion
^^^^^^^^^^^^^^^^

For standard L2 inversion, you can generate the sensitivities using the input file **sensitivity_L2.inp** and supporting files in the sub-folder *sensitivity_L2*. This input file is shown below.


.. figure:: images/sensitivity_L2_input.png
     :align: center
     :width: 700


Smooth Inversion
^^^^^^^^^^^^^^^^

The last line of the input file must be set to 0 to compute sensitivities for sparse inversion. In this case, the sensitivities were generated using the input file **sensitivity_sparse.inp** and supporting files in the sub-folder *sensitivity_sparse*. This input file is shown below.


.. figure:: images/sensitivity_sparse_input.png
     :align: center
     :width: 700

