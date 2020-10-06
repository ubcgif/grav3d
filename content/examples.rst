.. _example:

Examples
========

Here, the program libraries for Grav3d will be used to:

    - define a density contrast model on a tensor mesh
    - predict gravity anomaly data for a synthetic density contrast model
    - generate sensitivity weights for the inverse problem
    - compute and store the sensitivity matrix
    - invert gravity anomaly data to recover a density contrast model

Zip folders containing all necessary files can be downloaded here:

    .. - `Files for example using E3D version 1 <https://github.com/ubcgif/E3D/raw/e3dinv/assets/E3D_manual_ver1.zip>`__

The full examples are parse into 5 sections:

.. toctree::
    :maxdepth: 2

    Create tensor model <example/create_model>
    Forward modeling <example/fwd>
    Weights <example/weights>
    Generate sensitivity matrix <example/sensitivity>
    Inversion <example/inv>


A legacy example using the Grav3d package can be found here:

.. toctree::
	Legacy example <example/old_example>

