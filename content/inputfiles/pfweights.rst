.. _grav3d_weight_input:

PF Weights
==========

Gravity inversion has a tendancy place anomalous bodies near the observation locations due to high sensitivities.
The executable **pfweight.exe** creates a depth-based or distance based weighting to counteract these effects.
The lines of input file for the executable are as follows:

.. tabularcolumns:: |L|C|C|

+--------+--------------------------------------------------------------------+-------------------------------------------------------------------+
| Line # | Description                                                        | Description                                                       |
+========+====================================================================+===================================================================+
| 1      | :ref:`Type<grav3d_input_weight_ln1>`                               | *MAG*, *GRAV* or *GG*                                             |
+--------+--------------------------------------------------------------------+-------------------------------------------------------------------+
| 2      | :ref:`Mesh file<grav3d_input_weight_ln2>`                          | mesh file                                                         |
+--------+--------------------------------------------------------------------+-------------------------------------------------------------------+
| 3      | :ref:`Observations file<grav3d_input_weight_ln3>`                  | survey or observations file                                       |
+--------+--------------------------------------------------------------------+-------------------------------------------------------------------+
| 4      | :ref:`Topography<grav3d_input_weight_ln4>`                         | topography                                                        |
+--------+--------------------------------------------------------------------+-------------------------------------------------------------------+
| 5      | :ref:`Weighting type<grav3d_input_weight_ln5>`                     | depth or distance weighting                                       |
+--------+--------------------------------------------------------------------+-------------------------------------------------------------------+
| 6      | :ref:`alpha z0<grav3d_input_weight_ln6>`                           | Weighting parameters or *null*                                    |
+--------+--------------------------------------------------------------------+-------------------------------------------------------------------+


An example of the input file for creating weights is shown below.

.. figure:: images/pfweight_input.png
     :align: center
     :width: 700

     Example input file for creating distance weighting (`Download <https://github.com/ubcgif/grav3d/raw/v6.0/assets/grav3d_input/pfweight.inp>`__ ).


Line Descriptions
^^^^^^^^^^^^^^^^^

.. _grav3d_input_weight_ln1:

    - **Type:** in this case, enter a flag of *GRAV*

.. _grav3d_input_weight_ln2:

    - **Tensor Mesh:** file path to a :ref:`tensor mesh <meshfile>` file

.. _grav3d_input_weight_ln3:

    - **Data File:** file path to the :ref:`observations file<gravfile>`

.. _grav3d_input_weight_ln4:

    - **Topography:** there are two options for defining the topography.

        - type *null* for no defined topography (all cells are active)
        - provide the *filepath* to to a :ref:`topography file <topofile>`

.. _grav3d_input_weight_ln5:

    - **Weighting type:** An integer type specifying if depth or distance weighting is being created.

        - 1: for depth weighting (not applicable to borehole data)
        - 2: for distance weighting

.. _grav3d_input_weight_ln6:

    - **alpha z0:** Parameters for the depth or distance weighting being applied. Use the flag *null* if you would like to use standard values for the paramters. To see how these parameters impact the inversion and to see a default set of values, consult the theory section.

        - :ref:`theory for depth weighting<depthWeight>`
        - :ref:`theory for distance weighting<distWeight>`


