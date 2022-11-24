.. _example:

.. note:: The latest example has been generated using GRAV3D v6.0.2. The exercise can be completed using previous versions. However some functionality has been added since v5.0, and improvements in performance since v6.0 and v6.0.1 may result in slightly different recovered models.

Examples
========

.. figure:: example/images/model_sparse.png
     :align: center
     :width: 700


Here, the program libraries for GRAV3D v6 will be used to:

    - define a density contrast model on a tensor mesh
    - predict gravity anomaly data for a synthetic density contrast model
    - generate sensitivity weights for the inverse problem
    - compute and store the sensitivity matrix
    - invert gravity anomaly data to recover a density contrast model


Zip folders containing all necessary files can be downloaded here:

    - `Files for grav3d v6 example <https://github.com/ubcgif/grav3d/raw/v6.0/assets/grav3d_v6_example.zip>`__


The full example is parsed into 5 sections:

.. toctree::
    :maxdepth: 1

    Create tensor model <example/create_model>
    Forward modeling <example/fwd>
    Weights <example/weights>
    Least-squares inversion <example/inv_L2>
    Sparse norm inversion <example/inv_sparse>